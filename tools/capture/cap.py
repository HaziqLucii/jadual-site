import ui, time, sys, os, subprocess
S = ui.S + '/shots'
NAV = {'today': (150, 2232), 'week': (410, 2232), 'subjects': (670, 2232), 'wall': (929, 2232)}
def shot(name):
    time.sleep(1.2)
    subprocess.run([ui.A, 'emu', 'screenrecord', 'screenshot', f'{S}/{name}.png'], capture_output=True)
def nav(k): ui.tapxy(NAV[k]); time.sleep(1.5)
def app_screens(lang):
    os.makedirs(f'{S}/{lang}', exist_ok=True)
    nav('today'); ui.swipe(540,900,540,1900,300); ui.swipe(540,900,540,1900,300); shot(f'{lang}/today')
    nav('week'); shot(f'{lang}/week')
    nav('subjects'); shot(f'{lang}/subjects')
    nav('wall'); shot(f'{lang}/wall')
    nav('today')
if __name__ == '__main__':
    app_screens(sys.argv[1])
