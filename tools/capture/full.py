import ui, cap, walls, widcrop, time, sys, os, subprocess
SET = (995, 220)
LANGNAME = {'en': 'English', 'ms': 'Bahasa Melayu', 'id': 'Bahasa Indonesia'}
THEME = {'en': ('Theme', 'Light', 'Dark'), 'ms': ('Tema', 'Cerah', 'Gelap'), 'id': ('Tema', 'Terang', 'Gelap')}
def settings():
    walls.unlock(); walls.app(); cap.nav('today'); ui.tapxy(SET); time.sleep(1.5)
def set_lang(cur):
    settings()
    for _ in range(3):
        p = ui.find(LANGNAME[cur])
        if p: break
        ui.swipe(540, 1900, 540, 900, 300)
    ui.tapxy(p); time.sleep(2)
    ui.key(4); time.sleep(1)
def toggle_theme(l):
    settings()
    ui.tap(THEME[l][0]); time.sleep(2)
    ui.key(4); time.sleep(1)
def widgets(l, tag):
    ui.key(3); time.sleep(1); ui.key(3); time.sleep(1.5)
    got = {}
    for i in range(3):
        ui.swipe(900, 1200, 150, 1200, 300); time.sleep(2.5)
        for kind, _ in widcrop.grab(f'{l}/_p{i}'):
            src = f'{cap.S}/{l}/_p{i}_{kind}.png'
            if kind not in got:
                os.replace(src, f'{cap.S}/{l}/wid_{tag}_{kind}.png'); got[kind] = 1
    for f in os.listdir(f'{cap.S}/{l}'):
        if f.startswith('_p'): os.remove(f'{cap.S}/{l}/{f}')
    return got
def run(l):
    os.makedirs(f'{cap.S}/{l}', exist_ok=True)
    walls.unlock(); walls.app()
    cap.app_screens(l)
    ui.tap({'en': 'Academic English'}.get(l, 'Academic English')); time.sleep(1.5); cap.shot(f'{l}/sheet'); ui.key(4); time.sleep(1)
    walls.run(l)
    print('light', widgets(l, 'light'))
    toggle_theme(l)
    print('dark', widgets(l, 'dark'))
    toggle_theme(l)
if __name__ == '__main__':
    run(sys.argv[1])
