"""Converts the PNG captures in $JADUAL_CAPTURE_DIR/shots/<lang>/ into the
site's JPEGs in assets/screens/<lang>/. Phone screens 580 px wide, widget
crops at full size, theme cards and notification crops at twice their
displayed size. Run: python3 convert.py en ms id"""
import os, subprocess, sys
import ui

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
PHONE = ['today', 'week', 'sheet', 'subjects', 'wall', 'wall_a', 'wall_b', 'wall_c', 'routine', 'papers', 'reminders']
WIDTH = {'exam_strip': 840, 'notif_class': 760, 'notif_eve': 760}


def run(l):
    src, dst = f'{ui.S}/shots/{l}', os.path.join(ROOT, 'assets', 'screens', l)
    for f in sorted(os.listdir(src)):
        name, ext = os.path.splitext(f)
        if ext != '.png' or name.startswith('_'):
            continue
        if name in PHONE:
            size = ['-resize', '580x']
        elif name.startswith('th_'):
            size = ['-resize', '520x']
        elif name in WIDTH:
            size = ['-resize', f'{WIDTH[name]}x']
        else:
            size = []
        subprocess.run(['magick', f'{src}/{f}', *size, '-quality', '84', f'{dst}/{name}.jpg'], check=True)
        print(l, name)


if __name__ == '__main__':
    for l in sys.argv[1:]:
        run(l)
