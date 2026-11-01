"""Builds assets/screens/<lang>/ images from the Jadual Playbook capture set, so the landing page and the Playbook show the
same app. Source frames: ~/Projects/jadual/.frames/playbook/<lang>/*.png (1080x2400 Graph light, clock 11:18).
    python3 tools/capture/from_playbook.py en ms id
Phone screens are 580 px wide, paper cards 520, widgets 934 (wide) or 451 (small), flattened on the board colour."""
import os, subprocess, sys

HOME = os.path.expanduser('~')
FRAMES = os.path.join(HOME, 'Projects', 'jadual', '.frames', 'playbook')
BOOK = os.path.join(HOME, 'Projects', 'jadual', 'tools')
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

PHONES = {'today': 'today', 'week': 'week', 'sheet': 'classsheet', 'subjects': 'subjects', 'routine': 'rt_today', 'wall': 'wall_top',
          'notes_editor': 'note_editor', 'notes_canvas': 'canvas_drawn', 'notes_list': 'notes_list', 'backup': 'backup_sheet', 'papers': 'theme_picker_1', 'first': 'fr_path'}
PAPERS = ['graph', 'graph_dark', 'ledger', 'kraft', 'washi', 'ulangkaji', 'arang', 'kopitiam', 'marmar', 'jubin', 'papan_menu']
# site widget file -> (playbook frame, width)
WIDGETS = {'next_exam': ('next_exam', 451), 'note_pinned': ('note_pinned', 451), 'exam_strip': ('exam_strip', 934),
           'quick_note': ('quick_note', 934), 'exams': ('exams_list', 934), 'due': ('due', 934), 'todo': ('todo', 934),
           'notes_latest': ('notes_latest', 934), 'revise': ('revise', 934)}


def mg(*a):
    subprocess.run(['magick', *a], check=True)


def run(l):
    src, dst = os.path.join(FRAMES, l), os.path.join(ROOT, 'assets', 'screens', l)
    os.makedirs(dst, exist_ok=True)
    for name, f in PHONES.items():
        p = os.path.join(src, f + '.png')
        if os.path.exists(p):
            mg(p, '-resize', '580x', '-quality', '84', os.path.join(dst, name + '.jpg'))
        else:
            print('MISSING', l, f)
    for n in PAPERS:
        p = os.path.join(src, f'theme_{n}.png')
        mg(p, '-crop', '1080x926+0+150', '+repage', '-resize', '520x', '-quality', '84', os.path.join(dst, f'th_{n}.jpg'))
    p = os.path.join(src, 'today_exam.png')
    mg(p, '-crop', '1000x180+40+775', '+repage', '-resize', '840x', '-quality', '84', os.path.join(dst, 'exam_strip.jpg'))
    p = os.path.join(src, 'today_note2.png')
    if os.path.exists(p):
        mg(p, '-crop', '1000x560+40+1390', '+repage', '-resize', '700x', '-quality', '84', os.path.join(dst, 'note_today.jpg'))
    for name, (f, w) in WIDGETS.items():
        mg(os.path.join(src, f'widget_{f}.png'), '-background', '#8a9bb3', '-flatten', '-resize', f'{w}x', '-quality', '84',
           os.path.join(dst, f'wid_light_{name}.jpg'))
    book = 'playbook' if l == 'en' else f'playbook-{l}'
    cover = os.path.join(BOOK, book, 'img', 'wallpaper_cover.jpg')
    mg(cover, '-resize', '580x', '-quality', '86', os.path.join(dst, 'wall_a.jpg'))
    print('done', l)


if __name__ == '__main__':
    for l in sys.argv[1:]:
        run(l)
