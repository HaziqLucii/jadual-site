"""Build 11 captures (landing page v2). Run per language from a Pro demo build
with the exam sample imported (see README). Needs: python3 -c "import v2; v2.run('en')"."""
import ui, cap, walls, widcrop, full, time, os, re, subprocess

L = {
 'en': dict(today='Today', tomorrow='Tomorrow', bg='Background', paper='Paper', photo='Photo', done='Done',
            set='Set as wallpaper', ex='Exam countdown', choose='Choose a photo', theme='Theme', imp='Import',
            apply='Apply {}', undo='Tap to undo', lang='English', settings='Settings'),
 'ms': dict(today='Hari ini', tomorrow='Esok', bg='Latar belakang', paper='Kertas', photo='Foto', done='Siap',
            set='Jadikan latar skrin', ex='Kiraan detik peperiksaan', choose='Pilih foto', theme='Tema', imp='Import',
            apply='Gunakan {}', undo='Ketik untuk batal', lang='Bahasa Melayu', settings='Tetapan'),
 'id': dict(today='Hari ini', tomorrow='Besok', bg='Latar belakang', paper='Kertas', photo='Foto', done='Selesai',
            set='Pasang sebagai wallpaper', ex='Hitung mundur ujian', choose='Pilih foto', theme='Tema', imp='Impor',
            apply='Terapkan {}', undo='Ketuk untuk membatalkan', lang='Bahasa Indonesia', settings='Pengaturan'),
}
THEMES = ['Graph', 'Graph dark', 'Ledger', 'Kraft', 'Washi', 'Ulangkaji', 'Kopitiam', 'Marmar', 'Jubin', 'Papan menu']
EXAM_FILE = 'jadual-sample-exam.jadual'
ROUTINE_FILE = 'jadual-sample-routine-site.jadual'


_demo_on = [False]


def demo():
    b = lambda *a: ui.sh('am', 'broadcast', '-a', 'com.android.systemui.demo', *a)
    if not _demo_on[0]:
        b('-e', 'command', 'exit'); time.sleep(.5)
        b('-e', 'command', 'enter')
        b('-e', 'command', 'battery', '-e', 'level', '100', '-e', 'plugged', 'false')
        b('-e', 'command', 'network', '-e', 'wifi', 'show', '-e', 'level', '4', '-e', 'fully', 'true')
        b('-e', 'command', 'network', '-e', 'mobile', 'hide')
        b('-e', 'command', 'notifications', '-e', 'visible', 'false')
        _demo_on[0] = True
    b('-e', 'command', 'clock', '-e', 'hhmm', '1118')


SKIP = ('Skip tips', 'Langkau tip', 'Lewati tips')


def skip_tips():
    for n in nodes():
        if n['t'] in SKIP or n['d'] in SKIP:
            ui.tapxy(centre(n['b'])); time.sleep(1.2); return


def shot(name):
    skip_tips(); _demo_on[0] = False; demo(); cap.shot(name)


def nodes():
    x = ui.dump(); out = []
    for m in re.finditer(r'<node [^>]*>', x):
        n = m.group(0)
        t = re.search(r' text="([^"]*)"', n).group(1); d = re.search(r'content-desc="([^"]*)"', n).group(1)
        b = list(map(int, re.findall(r'\d+', re.search(r'bounds="([^"]*)"', n).group(1))))
        out.append(dict(t=t, d=d.replace('&#10;', '\n').replace('&amp;', '&'), b=b, checked='checked="true"' in n))
    return out


def centre(b): return ((b[0] + b[2]) // 2, (b[1] + b[3]) // 2)


def find_node(pred, scroll=True):
    for _ in range(5):
        for n in nodes():
            if pred(n): return n
        if not scroll: return None
        ui.swipe(540, 1900, 540, 900, 300); time.sleep(.8)
    raise SystemExit('node not found')


def top():
    for _ in range(3): ui.swipe(540, 1100, 540, 2100, 250)
    time.sleep(.8)


def crop(src, dst, b, pad=0):
    w, h = b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad
    subprocess.run(['magick', src, '-crop', f'{w}x{h}+{b[0] - pad}+{b[1] - pad}', '+repage', dst], check=True)


def P(name): return f'{cap.S}/{name}.png'


def settings():
    full.settings(); top()


def set_lang(l):
    settings()
    for _ in range(4):
        n = find_node(lambda n: n['d'].startswith(('Language\n', 'Bahasa\n')))
        if n['d'].endswith(L[l]['lang']): break
        ui.tapxy((n['b'][0] + 400, n['b'][3] - 60)); time.sleep(2)
    ui.key(4); time.sleep(1)


def import_file(l, fname):
    settings()
    n = find_node(lambda n: n['d'].startswith(L[l]['imp'] + '\n'))
    ui.tapxy(centre(n['b'])); time.sleep(3)
    n = find_node(lambda n: n['t'] == fname)
    ui.tapxy(centre(n['b'])); time.sleep(4)
    _demo_on[0] = False


def today_shots(l):
    walls.unlock(); walls.app(); cap.nav('today'); top(); time.sleep(3)
    shot(f'{l}/today')
    n = find_node(lambda n: 'DSP Hall' in n['d'] and n['b'][3] - n['b'][1] < 260, scroll=False)
    crop(P(f'{l}/today'), P(f'{l}/exam_strip'), n['b'])
    ui.tap('Academic English'); time.sleep(1.5); shot(f'{l}/sheet'); ui.key(4); time.sleep(1)
    cap.nav('subjects'); shot(f'{l}/subjects')


def week_shot(l):
    """7-day week at 360 dp with Wed CS250 moved up two hours; the exam
    sample is imported again afterwards to put it back."""
    ui.sh('wm', 'density', '480'); time.sleep(4); _demo_on[0] = False
    walls.app(); time.sleep(1); cap.nav('week'); time.sleep(1.5)
    skip_tips()
    ns = nodes()
    se = sorted([n for n in ns if n['d'].startswith('Software Engineering,')], key=lambda n: n['b'][1])
    hr = sorted((int(n['d']), n['b'][1]) for n in ns if re.fullmatch(r'\d\d', n['d']) and n['b'][0] < 250)
    per_hour = (hr[-1][1] - hr[0][1]) / (hr[-1][0] - hr[0][0])
    b = se[-1]['b']
    x, y0 = (b[0] + b[2]) // 2, b[1] + 60
    y1 = y0 - 2 * per_hour
    moves = '; '.join(f'input motionevent MOVE {x} {int(y0 + (y1 - y0) * k / 8)}; sleep 0.05' for k in range(1, 9))
    ui.sh(f'input motionevent DOWN {x} {y0}; sleep 1.2; {moves}; sleep 0.6; input motionevent UP {x} {y1}')
    demo(); time.sleep(.5); cap.shot(f'{l}/week')
    ui.sh('wm', 'density', 'reset'); time.sleep(4); _demo_on[0] = False
    import_file(l, EXAM_FILE)


def wall_tab():
    walls.unlock(); walls.app(); cap.nav('wall'); top()


def set_switch(label, on):
    n = find_node(lambda n: n['d'].startswith(label + '\n'))
    if n['checked'] != on: ui.tapxy(centre(n['b'])); time.sleep(1.2)


def background(l, name=None, photo=False):
    n = find_node(lambda n: n['d'].startswith(L[l]['bg'] + ','))
    ui.tapxy(centre(n['b'])); time.sleep(1.5)
    if photo:
        n = find_node(lambda n: n['d'].startswith(L[l]['photo'] + '\n'), scroll=False)
        ui.tapxy(centre(n['b'])); time.sleep(1)
        ui.tap(L[l]['choose']); time.sleep(3)
        n = find_node(lambda n: n['d'].startswith('jadual-sample-photo.jpg,'), scroll=False)
        ui.tapxy((n['b'][0] + 60, n['b'][3] - 60)); time.sleep(4)
    else:
        n = [x for x in nodes() if x['t'] == L[l]['paper'] or x['d'] == L[l]['paper']]
        ui.tapxy(centre(n[0]['b'])); time.sleep(1)
        n = find_node(lambda n: n['d'] == name or n['d'].startswith(name + ','), scroll=False)
        ui.tapxy(centre(n['b'])); time.sleep(1.5)
    ui.tap(L[l]['done'], exact=True); time.sleep(1.5)



def layout(l, which):
    top()
    n = [x for x in nodes() if (x['d'] == L[l][which] or x['t'] == L[l][which]) and x['b'][0] > 400][0]
    ui.tapxy(centre(n['b'])); time.sleep(1.2)


def set_now(l):
    n = find_node(lambda n: n['d'] == L[l]['set'] or n['t'] == L[l]['set'])
    ui.tapxy(centre(n['b'])); time.sleep(4)


def lockshot(name, hhmm='1118', date='09251118'):
    ui.sh('date', f'{date}2026.00'); ui.key(223); time.sleep(1.5); ui.key(224); time.sleep(3)
    demo(); ui.sh('am', 'broadcast', '-a', 'com.android.systemui.demo', '-e', 'command', 'clock', '-e', 'hhmm', hhmm)
    time.sleep(1); cap.shot(name)
    ui.sh('date', '092511182026.00')


def walls_ac(l):
    wall_tab(); layout(l, 'today'); background(l, 'Graph'); set_switch(L[l]['ex'], False)
    top(); shot(f'{l}/wall')
    set_now(l); lockshot(f'{l}/wall_a')
    wall_tab(); background(l, photo=True); set_switch(L[l]['ex'], True)
    set_now(l); lockshot(f'{l}/wall_c')
    wall_tab(); set_switch(L[l]['ex'], False); background(l, 'Graph')


def wall_b(l):
    """Tomorrow on Jubin, from the Thursday 21:40 build."""
    wall_tab(); layout(l, 'tomorrow'); background(l, 'Jubin'); set_switch(L[l]['ex'], False)
    set_now(l); lockshot(f'{l}/wall_b', '2140', '09242140')
    wall_tab(); layout(l, 'today'); background(l, 'Graph')


def apply_theme(l, name):
    settings()
    n = find_node(lambda n: n['d'].startswith(L[l]['theme'] + '\n'))
    ui.tapxy(centre(n['b'])); time.sleep(2)
    n = find_node(lambda n: n['d'].startswith(name + ','))
    ui.tapxy(centre(n['b'])); time.sleep(2)
    p = ui.find(L[l]['apply'].format(name))
    if p: ui.tapxy(p); time.sleep(3)
    else: ui.key(4); time.sleep(1)
    ui.key(4); time.sleep(1); ui.key(4); time.sleep(1)


def theme_cards(l):
    settings()
    n = find_node(lambda n: n['d'].startswith(L[l]['theme'] + '\n'))
    ui.tapxy(centre(n['b'])); time.sleep(2)
    shot(f'{l}/papers')
    for name in THEMES:
        top()
        n = find_node(lambda n: n['d'].startswith(name + ','))
        ui.tapxy(centre(n['b'])); time.sleep(2.5)
        slug = name.lower().replace(' ', '_')
        shot(f'{l}/_th')
        crop(P(f'{l}/_th'), P(f'{l}/th_{slug}'), [42, 262, 743, 866])
        ui.key(4); time.sleep(1.2)
    os.remove(P(f'{l}/_th'))
    ui.key(4); time.sleep(1)


def widgets(l):
    apply_theme(l, 'Graph'); print('light', full.widgets(l, 'light'))
    apply_theme(l, 'Graph dark'); print('dark', full.widgets(l, 'dark'))
    for name in ('Kopitiam', 'Washi'):
        apply_theme(l, name); got = full.widgets(l, name.lower())
        for k in ('next', 'week'):
            f = P(f'{l}/wid_{name.lower()}_{k}')
            if os.path.exists(f): os.remove(f)
    apply_theme(l, 'Graph')


def routine(l):
    import_file(l, ROUTINE_FILE); time.sleep(2)
    walls.app(); cap.nav('today'); top(); time.sleep(2); shot(f'{l}/routine')
    import_file(l, EXAM_FILE)


def run(l):
    os.makedirs(f'{cap.S}/{l}', exist_ok=True)
    today_shots(l)
    week_shot(l)
    walls_ac(l)
    theme_cards(l)
    widgets(l)
    routine(l)


PKG = 'io.github.haziqlucii.jadual'


def reminder_setup(l):
    """Real-clock Pro build: lead 10 min and the exam evening-before on."""
    settings()
    n = find_node(lambda n: n['d'] == '10' and n['b'][1] < 1400, scroll=False)
    ui.tapxy(centre(n['b'])); time.sleep(1)
    n = find_node(lambda n: n['d'].startswith(('Exam evening before', 'Malam sebelum')), scroll=False)
    if not n['checked']: ui.tapxy(centre(n['b'])); time.sleep(1)


def fire(date, restart=True):
    """App restarted (a force-stopped app misses TIME_SET), then the clock
    moved to just before a reminder, then wait for it."""
    if restart:
        # Force-stop also removes the app's posted notifications.
        ui.sh('rm', '-f', f'/data/data/{PKG}/shared_prefs/reminders.xml')
        ui.sh('am', 'force-stop', PKG)
        ui.sh('am', 'start', '-n', f'{PKG}/.MainActivity'); time.sleep(4)
        ui.key(3); time.sleep(1)
    ui.sh('date', date); time.sleep(30)


def row_boxes():
    x = ui.dump()
    return [list(map(int, re.findall(r'\d+', re.search(r'bounds="([^"]*)"', m.group(0)).group(1))))
            for m in re.finditer(r'<node [^>]*resource-id="com.android.systemui:id/expandableNotificationRow"[^>]*>', x)]


def one_row(code):
    """The smallest notification row holding a title with this code."""
    t = [n for n in nodes() if code in n['t']]
    if not t: raise SystemExit('no notification ' + code)
    y = t[0]['b'][1]
    return min((b for b in row_boxes() if b[1] <= y <= b[3]), key=lambda b: (b[2] - b[0]) * (b[3] - b[1]))


def shade_crop(l, code, name):
    ui.sh('cmd', 'statusbar', 'expand-notifications'); time.sleep(2.5)
    b = one_row(code)
    exp = [n for n in nodes() if n['d'] == 'Expand' and b[1] <= n['b'][1] <= b[3]]
    if exp: ui.tapxy(centre(exp[0]['b'])); time.sleep(1.5)
    b = one_row(code)
    _demo_on[0] = False; demo()
    ui.sh('am', 'broadcast', '-a', 'com.android.systemui.demo', '-e', 'command', 'clock', '-e', 'hhmm', '2000')
    time.sleep(1); cap.shot(f'{l}/_shade')
    crop(P(f'{l}/_shade'), P(f'{l}/{name}'), b)
    p = ui.find('Clear all')
    if p: ui.tapxy(p); time.sleep(1.5)
    ui.sh('cmd', 'statusbar', 'collapse'); time.sleep(1)


def notifications(l):
    ui.sh('cmd', 'statusbar', 'expand-notifications'); time.sleep(2)
    p = ui.find('Clear all')
    if p: ui.tapxy(p); time.sleep(1.5)
    ui.sh('cmd', 'statusbar', 'collapse'); time.sleep(1)
    fire('092514492026.40')
    shade_crop(l, 'CS210', 'notif_class')
    fire('092919592026.40', restart=False)
    shade_crop(l, 'CS230', 'notif_eve')
    os.remove(P(f'{l}/_shade'))
    ui.sh('date', '092511182026.00')


def reminder_settings_shot(l):
    settings(); shot(f'{l}/reminders')
