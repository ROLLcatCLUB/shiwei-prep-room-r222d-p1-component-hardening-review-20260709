import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'R222D_P1_hardened_fixture_component_cards.json').read_text(encoding='utf-8'))
EXPECTED = ['compare_two_images','circle_and_annotate','match_cards','guess_from_clue','material_mystery_box','technique_step_demo','tiered_challenge','gallery_walk','keyword_feedback','learning_sheet_record','mini_quiz','photo_submit']
FORBIDDEN = {'active_component','runtime_component','implemented_component','production_component','static_screen_component','interactive_prototype','classroom_pilot'}
GENERIC = ['帮助教师把学习困难转化为可操作的课堂任务','看任务、做动作、说理由、留证据']
checks=[]
def check(name, cond, detail=''):
    checks.append({'name': name, 'passed': bool(cond), 'detail': detail})
cards = DATA.get('hardened_fixture_component_cards', [])
check('stage_id', DATA.get('stage_id') == '1013R_R222D_P1_COMPONENT_PEDAGOGICAL_HARDENING')
check('ui_disabled', DATA.get('ui_enabled') is False)
check('runtime_disabled', DATA.get('runtime_enabled') is False)
check('r97b_untouched', DATA.get('r97b_touched') is False)
check('fixture_count_12', len(cards) == 12)
check('expected_ids', [c.get('component_id') for c in cards] == EXPECTED)
check('active_component_count_zero', DATA.get('active_component_count') == 0)
for c in cards:
    cid=c.get('component_id','<missing>')
    check(f'{cid}: implementation fixture only', c.get('implementation_status') == 'fixture_component')
    check(f'{cid}: no forbidden status', c.get('implementation_status') not in FORBIDDEN)
    check(f'{cid}: p1 status', c.get('p1_hardening_status') == 'pedagogically_hardened_fixture')
    check(f'{cid}: concrete student problem', len(c.get('student_problem_solved','')) >= 35)
    check(f'{cid}: why use specific', len(c.get('why_use','')) >= 45 and not any(g in c.get('why_use','') for g in GENERIC))
    how=c.get('how_to_use',[])
    check(f'{cid}: how_to_use 4-6 steps', 4 <= len(how) <= 6)
    check(f'{cid}: how_to_use not generic startup', not any(step.startswith('启动“') for step in how))
    media=c.get('media_requirements_detail')
    check(f'{cid}: media_requirements_detail exists', isinstance(media,dict) and len(media) >= 5)
    check(f'{cid}: media has sheet fields', bool(media.get('learning_sheet_fields')))
    check(f'{cid}: sample_use_cases >=2', len(c.get('sample_use_cases',[])) >= 2)
    check(f'{cid}: sample cases have evidence', all(x.get('evidence') for x in c.get('sample_use_cases',[])))
    check(f'{cid}: teacher_language_examples >=2', len(c.get('teacher_language_examples',[])) >= 2)
    check(f'{cid}: teacher language natural length', all(12 <= len(x) <= 90 for x in c.get('teacher_language_examples',[])))
    check(f'{cid}: screen_prompt_examples >=1', len(c.get('screen_prompt_examples',[])) >= 1)
    check(f'{cid}: screen prompts short', all(len(x) <= 40 for x in c.get('screen_prompt_examples',[])))
    check(f'{cid}: evidence examples >=1', len(c.get('learning_sheet_or_evidence_examples',[])) >= 1)
    check(f'{cid}: misuse_boundary exists', len(c.get('misuse_boundary','')) >= 30)
    rel=c.get('component_relation')
    check(f'{cid}: component_relation exists', isinstance(rel,dict) and rel.get('role') and rel.get('merge_policy'))
    check(f'{cid}: source_basis exists', len(c.get('source_basis',[])) >= 3)
for name in ['R222D_P1_hardened_fixture_component_cards.json','R222D_P1_hardened_fixture_component_cards.md','R222D_P1_component_relation_and_merge_notes.md','R222D_P1_media_requirement_detail_matrix.md','R222D_P1_teacher_language_examples.md','R222D_P1_screen_prompt_examples.md','R222D_P1_evidence_output_examples.md','R222D_P1_report.md','README_FOR_GPT_REVIEW.md']:
    check(f'file exists: {name}', (ROOT/name).exists())
result={'passed': all(c['passed'] for c in checks), 'check_count': len(checks), 'failed': sum(1 for c in checks if not c['passed']), 'fixture_component_count': len(cards), 'active_component_count': DATA.get('active_component_count'), 'failed_checks':[c for c in checks if not c['passed']]}
(ROOT/'validate_1013R_R222D_P1_component_pedagogical_hardening_result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))
raise SystemExit(0 if result['passed'] else 1)
