#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, shutil, sys
from pathlib import Path
from typing import Any, Dict, List
ROOT=Path(__file__).resolve().parent
CORE=ROOT/'core'/'templates'
ADAPTERS=ROOT/'adapters'/'agents'

def load_context(path:Path)->Dict[str,Any]:
    txt=path.read_text(encoding='utf-8'); suf=path.suffix.lower()
    if suf=='.json': return json.loads(txt)
    if suf in {'.yaml','.yml'}:
        try:
            import yaml
        except Exception as e:
            raise RuntimeError('YAML requires PyYAML. Use JSON or install PyYAML.') from e
        return yaml.safe_load(txt)
    raise ValueError('context file must be .json, .yaml or .yml')

def val(ctx,dotted):
    cur=ctx
    for part in dotted.split('.'):
        if isinstance(cur,dict) and part in cur: cur=cur[part]
        else: return 'TODO_'+dotted.replace('.','_').upper()
    return cur

def render(txt,ctx):
    def r(m):
        v=val(ctx,m.group(1).strip())
        if isinstance(v,list): return '\n'.join(f'- {x}' for x in v)
        if isinstance(v,dict): return json.dumps(v,indent=2,ensure_ascii=False)
        return str(v)
    return re.sub(r'\{\{\s*([^}]+)\s*\}\}',r,txt)

def copy_tree(src:Path,dst:Path,ctx,dry=False):
    made=[]
    for item in sorted(src.rglob('*')):
        rel=str(item.relative_to(src))
        if rel.endswith('.j2'): rel=rel[:-3]
        tgt=dst/rel
        if item.is_dir():
            if not dry: tgt.mkdir(parents=True,exist_ok=True)
            continue
        if item.suffix=='.j2':
            content=render(item.read_text(encoding='utf-8'),ctx)
            if not dry:
                tgt.parent.mkdir(parents=True,exist_ok=True); tgt.write_text(content,encoding='utf-8')
        else:
            if not dry:
                tgt.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(item,tgt)
        made.append(tgt)
    return made

def agents(s): return [x.strip() for x in (s or '').split(',') if x.strip()]

def install(context,output,agent_list,dry=False,force=False):
    ctx=load_context(context); output=output.resolve()
    if not dry and not force:
        existing=[p for p in [output/'AGENTS.md',output/'SDD_INDEX.md',output/'.sdd'] if p.exists()]
        if existing:
            print('Refusing to overwrite existing SDD files without --force:')
            for p in existing: print('  -',p)
            return 2
    if not dry: output.mkdir(parents=True,exist_ok=True)
    print(('DRY-RUN ' if dry else '')+f'Installing SDD workspace into: {output}')
    made=copy_tree(CORE,output,ctx,dry)
    for a in agent_list:
        d=ADAPTERS/a
        if not d.exists(): print(f'[WARN] unknown adapter {a}, skipping'); continue
        made+=copy_tree(d,output,ctx,dry)
    for p in made:
        try: print('  -',p.relative_to(output))
        except ValueError: print('  -',p)
    return 0

def validate(path):
    path=path.resolve()
    req=['AGENTS.md','SDD_INDEX.md','.sdd/CONTEXT_LOADING.md','.sdd/WORKSPACE_STATE.md','.sdd/steering/README.md','.sdd/steering/product.md','.sdd/steering/architecture.md','.sdd/steering/tech.md','.sdd/steering/principles.md','.sdd/steering/agent-workflow.md','.sdd/operations/README.md','.sdd/operations/action-rules.md','.sdd/operations/git-workflow.md','.sdd/operations/memory-policy.md','.sdd/operations/agent-compatibility.md','.sdd/operations/tooling-and-mcp-policy.md','.sdd/decisions/README.md','.sdd/decisions/decision-template.md','.sdd/templates/spec-template/context.md','.sdd/templates/spec-template/requirements.md','.sdd/templates/spec-template/design.md','.sdd/templates/spec-template/tasks.md','.sdd/templates/spec-template/notes.md']
    missing=[r for r in req if not (path/r).exists()]
    if missing:
        print('SDD validation failed. Missing files:')
        for r in missing: print('  -',r)
        return 1
    unresolved=[]
    for r in req:
        p=path/r
        if p.is_file() and '{{' in p.read_text(encoding='utf-8',errors='ignore'): unresolved.append(r)
    if unresolved:
        print('SDD validation warning. Unresolved placeholders:')
        for r in unresolved: print('  -',r)
        return 2
    print('SDD validation passed.'); return 0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--context',type=Path); ap.add_argument('--output',type=Path,default=Path('.'))
    ap.add_argument('--agents',default=''); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true')
    ap.add_argument('--validate',type=Path)
    args=ap.parse_args()
    if args.validate: return validate(args.validate)
    if not args.context: ap.error('--context is required unless --validate is used')
    return install(args.context,args.output,agents(args.agents),args.dry_run,args.force)
if __name__=='__main__': raise SystemExit(main())
