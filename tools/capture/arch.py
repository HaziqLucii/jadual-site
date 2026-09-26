import ui, cap, walls, full, time, sys
ARCH = {'en': 'Archive semester', 'ms': 'Arkibkan semester', 'id': 'Arsipkan semester'}
LOOK = {'en': 'Look around first', 'id': 'Lihat-lihat dulu'}
PAST = {'en': 'Past semesters', 'ms': 'Semester lalu', 'id': 'Semester lalu'}
def scroll_find(label):
    for _ in range(4):
        p = ui.find(label)
        if p: return p
        ui.swipe(540, 1900, 540, 900, 300); time.sleep(0.8)
    raise SystemExit('not found ' + label)
def archive_and_first(l, look):
    full.settings()
    ui.tapxy(scroll_find(ARCH[l])); time.sleep(1.5)
    x = ui.dump()
    ps = ui.find(ARCH[l])  # dialog action shares the label; tap the last match
    import re
    nodes = [m for m in re.finditer(r'<node [^>]*>', x) if ARCH[l] in m.group(0)]
    b = list(map(int, re.findall(r'\d+', re.search(r'bounds="([^"]*)"', nodes[-1].group(0)).group(1))))
    ui.tapxy(((b[0]+b[2])//2, (b[1]+b[3])//2)); time.sleep(3)
    cap.shot(f'{l}/first')
    ui.tap(look); time.sleep(3)
def archive_screen(l):
    full.settings()
    ui.tapxy(scroll_find(PAST[l])); time.sleep(2)
    cap.shot(f'{l}/archive')
    ui.key(4); time.sleep(1); ui.key(4); time.sleep(1)
