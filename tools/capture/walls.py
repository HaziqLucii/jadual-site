import ui, cap, time, sys
L = {
 'en': dict(today='Today list', week='Week grid', next='Next class', dark='Dark', light='Light', lock='Lock screen', home='Home screen', set='Set as wallpaper'),
 'ms': dict(today='Senarai hari ini', week='Grid minggu', next='Kelas seterusnya', dark='Gelap', light='Cerah', lock='Skrin kunci', home='Skrin utama', set='Tetapkan kertas dinding'),
 'id': dict(today='Daftar hari ini', week='Kisi minggu', next='Kuliah berikutnya', dark='Gelap', light='Terang', lock='Layar kunci', home='Layar utama', set='Pasang sebagai wallpaper'),
}
A = ui.A
def app():
    ui.sh('am', 'start', '-n', 'io.github.haziqlucii.jadual/.MainActivity'); time.sleep(2.5)
def clock(): ui.sh('date', '092511182026.00')
def unlock():
    ui.key(224); time.sleep(1); ui.swipe(540, 2000, 540, 500, 250); time.sleep(1.5)
def lockshot(name):
    clock(); ui.key(223); time.sleep(1.5); ui.key(224); time.sleep(3); cap.shot(name)
def set_wall(l, layout, theme, place):
    unlock(); app(); cap.nav("wall")
    ui.tap(L[l][layout], exact=True); ui.tap(L[l][theme], exact=True); ui.tap(L[l][place], exact=True)
    ui.tap(L[l]['set']); time.sleep(4)
def run(l):
    set_wall(l, 'today', 'light', 'lock'); lockshot(f'{l}/wall_a'); unlock()
    set_wall(l, 'next', 'light', 'lock'); lockshot(f'{l}/wall_c'); unlock()
    set_wall(l, 'week', 'dark', 'lock'); lockshot(f'{l}/wall_b'); unlock()
if __name__ == '__main__':
    run(sys.argv[1])
