"""Builds index.html, ms/index.html and id/index.html.

The markup and the copy are ported from the Claude Design file
`design/Jadual Paper Landing.dc.html` in the app repo. Every phone, widget
and wallpaper is a real screenshot from the app (assets/screens/). The
Malay and Indonesian copy is the design's own, written separately per
language; edit the three dicts in C together.

Run: python3 tools/build.py
"""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://haziqlucii.github.io/jadual-site/'
CONTACT = 'haziq.support.dev@gmail.com'
SAMPAI = 'https://haziqlucii.github.io/sampai-site/'

HL = {'ds': '#8EC5FF', 'la': '#FFE45C', 'cn': '#9FE8C8', 'db': '#FF94C2',
      'ti': '#B5CF84', 'en': '#FFB070', 'se': '#E8836F'}
SUB = {'ds': 'CS201', 'la': 'MA202', 'cn': 'CS210', 'db': 'CS230',
       'ti': 'MPU3123', 'en': 'EN110', 'se': 'CS250'}
RAW = [('ds', 0, 480, 590, 'DK 3'), ('la', 0, 600, 710, 'DK 5'), ('cn', 0, 840, 950, 'BK 2'),
       ('db', 1, 540, 650, 'DK 1'), ('en', 1, 660, 770, 'BT 4'), ('ds', 1, 840, 1010, 'MK 2 · A'),
       ('la', 2, 480, 590, 'BT 2'), ('ti', 2, 600, 710, 'DSP'), ('se', 2, 900, 1010, 'DK 4'),
       ('cn', 3, 480, 590, 'BT 3'), ('se', 3, 600, 770, 'MK 1'), ('ds', 3, 840, 950, 'BT 1'),
       ('db', 4, 480, 590, 'BT 5'), ('en', 4, 600, 710, 'DK 2'), ('cn', 4, 900, 1010, 'MK 3'),
       ('db', 1, 840, 1010, 'MK 2 · B')]

C = {
 'en': dict(
  htmlLang='en', title='Jadual: your class timetable, on your home and lock screen',
  desc='Jadual is an Android class timetable for students. Type your timetable once and see it as widgets and as a lock screen wallpaper. Offline, no account, no ads. English, Malay, Indonesian.',
  navWeek='The week', navWall='Wallpaper', navWid='Widgets', getApp='Coming soon',
  kicker='Android timetable · Offline · EN / MS / ID', tagline='Type your timetable once. See it everywhere.',
  heroP='On your home screen as a widget, and on your lock screen as a wallpaper built around your clock. No account, no cloud, no ads.',
  getOn='COMING SOON TO', watch='Watch a week fill in ↓', fig='Fig.', fig1='Friday, 11:18', week7='WEEK 7',
  q1='Question 1.', q2='Question 2.', q3='Question 3.', q4='Question 4.',
  h1='Sixteen slots. Typed once.',
  p1='One subject can have many slots: a lecture, a tutorial, a lab on alternating weeks. Add each once and the week builds itself, every subject marked in its own highlighter.',
  of16='of 16 slots · 7 subjects', weekTitle='Week 7',
  h2='Where do I need to be next?',
  p2='Today answers it in two seconds: the class you are in and how long it has left, the next one and when it starts, and the free periods in between, including the long Friday break.',
  fig2='The week, tap any block',
  h3='Your lock screen, as a timetable.',
  p3='Pick a layout and Jadual draws a wallpaper around your clock and icons, so nothing important hides under them. With Jadual Pro it redraws at 06:00, so today is always today.',
  h4='Three widgets, on paper or at night.',
  p4='Next class with a countdown, Today with the current class inverted, and the whole week at 4×4.',
  galH='The whole semester, on one sheet.', turn='turn over →', crossed='Crossed out, on purpose.',
  sampai='Need a reminder to actually go? That is <a href="{s}">Sampai</a>, from the same developer. It rings until you tap Done.',
  freeOn='Coming soon to Google Play', fw0='Type', fw1='it', fw2='once.',
  foot='Android · No account · Your timetable stays on your phone',
  privacy='Privacy', terms='Terms', contact='Contact',
  sep=':', days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], types=['Tutorial', 'Lecture', 'Lab'],
  now='Now · 32 min left', next='Next · in 3 h 42 min',
  layouts=['Today list', 'Week grid', 'Next class'], places=['Lock screen', 'Home screen'],
  facts=[('Typed', 'Once'), ('Account', 'None'), ('Price', 'Free'), ('Languages', 'EN · MS · ID')],
  gallery=[('First run', 'Name the semester once, or import a file.'), ('Today', 'Now, next, and the free gaps.'),
           ('Week', 'Five days at 360 dp. A and B weeks.'), ('Edit a slot', 'Chips for common times. Hold to delete.'),
           ('Subjects', 'Code, highlighter, lecturer, hours.'), ('Wallpaper', 'Built around your clock and icons.'),
           ('Archive', 'Past semesters, read-only, exportable.')],
  nos=[('An account', 'Open it and type'), ('The cloud', 'Stored on this phone'), ('Ads', ''),
       ('Social feeds', 'Your timetable stays yours'), ('Trackers', 'No analytics, no ad IDs')],
  widTitle=('Light · widgets', 'Dark · widgets'), widNext='Next class', widToday='Today', widWeek='Week',
  shot='Screenshot from the app'),
 'ms': dict(
  htmlLang='ms', title='Jadual: jadual kelas anda, di skrin utama dan skrin kunci',
  desc='Jadual ialah aplikasi jadual kelas Android untuk pelajar. Taip jadual anda sekali dan lihat sebagai widget dan kertas dinding skrin kunci. Luar talian, tiada akaun, tiada iklan.',
  navWeek='Minggu', navWall='Kertas dinding', navWid='Widget', getApp='Akan datang',
  kicker='Jadual Android · Luar talian · EN / MS / ID', tagline='Taip jadual anda sekali. Lihat di mana-mana.',
  heroP='Di skrin utama sebagai widget, dan di skrin kunci sebagai kertas dinding yang dibina di sekitar jam anda. Tiada akaun, tiada awan, tiada iklan.',
  getOn='AKAN DATANG DI', watch='Lihat jadual seminggu terisi ↓', fig='Rajah', fig1='Jumaat, 11:18', week7='MINGGU 7',
  q1='Soalan 1.', q2='Soalan 2.', q3='Soalan 3.', q4='Soalan 4.',
  h1='Enam belas slot. Ditaip sekali.',
  p1='Satu subjek boleh ada banyak slot: kuliah, tutorial, makmal pada minggu berselang. Tambah setiap satu sekali dan minggu anda tersusun sendiri, setiap subjek ditanda dengan pen penanda sendiri.',
  of16='daripada 16 slot · 7 subjek', weekTitle='Minggu 7',
  h2='Ke mana saya perlu pergi seterusnya?',
  p2='Hari ini menjawabnya dalam dua saat: kelas yang sedang anda hadiri dan berapa lama lagi, kelas seterusnya dan bila ia bermula, serta waktu kosong di antaranya, termasuk rehat panjang hari Jumaat.',
  fig2='Minggu ini, ketik mana-mana blok',
  h3='Skrin kunci anda, sebagai jadual.',
  p3='Pilih susun atur dan Jadual melukis kertas dinding di sekitar jam dan ikon anda, supaya tiada yang penting tersembunyi. Dengan Jadual Pro, ia dilukis semula pada 06:00, jadi hari ini sentiasa hari ini.',
  h4='Tiga widget, di atas kertas atau pada waktu malam.',
  p4='Kelas seterusnya dengan kiraan detik, Hari ini dengan kelas semasa diserlahkan, dan seluruh minggu pada saiz 4×4.',
  galH='Seluruh semester, pada satu helaian.', turn='sila lihat sebelah →', crossed='Dipangkah, dengan sengaja.',
  sampai='Perlukan peringatan untuk benar-benar pergi? Itu <a href="{s}ms/">Sampai</a>, daripada pembangun yang sama. Ia berdering sehingga anda ketik Selesai.',
  freeOn='Akan datang di Google Play', fw0='Taip', fw1='sekali', fw2='sahaja.',
  foot='Android · Tiada akaun · Jadual anda kekal di telefon anda',
  privacy='Privasi', terms='Terma', contact='Hubungi',
  sep=':', days=['Isn', 'Sel', 'Rab', 'Kha', 'Jum'], types=['Tutorial', 'Kuliah', 'Makmal'],
  now='Kini · 32 min lagi', next='Seterusnya · dalam 3 j 42 min',
  layouts=['Senarai hari ini', 'Grid minggu', 'Kelas seterusnya'], places=['Skrin kunci', 'Skrin utama'],
  facts=[('Ditaip', 'Sekali'), ('Akaun', 'Tiada'), ('Harga', 'Percuma'), ('Bahasa', 'EN · MS · ID')],
  gallery=[('Mula', 'Namakan semester sekali, atau import fail.'), ('Hari ini', 'Kini, seterusnya, dan waktu kosong.'),
           ('Minggu', 'Lima hari pada 360 dp. Minggu A dan B.'), ('Ubah slot', 'Cip untuk waktu biasa. Tahan untuk padam.'),
           ('Subjek', 'Kod, penanda, pensyarah, jam.'), ('Kertas dinding', 'Dibina di sekitar jam dan ikon anda.'),
           ('Arkib', 'Semester lalu, baca sahaja, boleh dieksport.')],
  nos=[('Akaun', 'Buka dan terus taip'), ('Awan', 'Disimpan di telefon ini'), ('Iklan', ''),
       ('Suapan sosial', 'Jadual anda milik anda'), ('Penjejak', 'Tiada analitik, tiada ID iklan')],
  widTitle=('Cerah · widget', 'Gelap · widget'), widNext='Kelas seterusnya', widToday='Hari ini', widWeek='Minggu',
  shot='Tangkapan skrin daripada aplikasi'),
 'id': dict(
  htmlLang='id', title='Jadual: jadwal kuliahmu, di layar utama dan layar kunci',
  desc='Jadual adalah aplikasi jadwal kuliah Android untuk mahasiswa. Ketik jadwalmu sekali dan lihat sebagai widget dan wallpaper layar kunci. Luring, tanpa akun, tanpa iklan.',
  navWeek='Minggu', navWall='Wallpaper', navWid='Widget', getApp='Segera hadir',
  kicker='Jadwal Android · Luring · EN / MS / ID', tagline='Ketik jadwalmu sekali. Lihat di mana saja.',
  heroP='Di layar utama sebagai widget, dan di layar kunci sebagai wallpaper yang dibuat di sekitar jammu. Tanpa akun, tanpa cloud, tanpa iklan.',
  getOn='SEGERA HADIR DI', watch='Lihat jadwal seminggu terisi ↓', fig='Gambar', fig1='Jumat, 11.18', week7='MINGGU 7',
  q1='Soal 1.', q2='Soal 2.', q3='Soal 3.', q4='Soal 4.',
  h1='Enam belas slot. Diketik sekali.',
  p1='Satu mata kuliah bisa punya banyak slot: kuliah, tutorial, praktikum di minggu bergantian. Tambahkan masing-masing sekali dan jadwal seminggu tersusun sendiri, tiap mata kuliah ditandai dengan stabilonya sendiri.',
  of16='dari 16 slot · 7 mata kuliah', weekTitle='Minggu 7',
  h2='Ke mana aku harus pergi berikutnya?',
  p2='Hari ini menjawabnya dalam dua detik: kuliah yang sedang berlangsung dan sisa waktunya, kuliah berikutnya dan kapan dimulai, serta jam kosong di antaranya, termasuk jeda panjang hari Jumat.',
  fig2='Minggu ini, ketuk blok mana saja',
  h3='Layar kuncimu, sebagai jadwal.',
  p3='Pilih tata letak dan Jadual menggambar wallpaper di sekitar jam dan ikonmu, jadi tidak ada yang penting tertutup. Dengan Jadual Pro, digambar ulang pukul 06.00, jadi hari ini selalu hari ini.',
  h4='Tiga widget, di atas kertas atau di malam hari.',
  p4='Kuliah berikutnya dengan hitung mundur, Hari ini dengan kuliah yang sedang berlangsung disorot, dan seminggu penuh di ukuran 4×4.',
  galH='Satu semester penuh, di satu lembar.', turn='balik halaman →', crossed='Dicoret, dengan sengaja.',
  sampai='Butuh pengingat supaya benar-benar berangkat? Itu <a href="{s}id/">Sampai</a>, dari pengembang yang sama. Ia berbunyi sampai kamu mengetuk Selesai.',
  freeOn='Segera hadir di Google Play', fw0='Ketik', fw1='sekali', fw2='saja.',
  foot='Android · Tanpa akun · Jadwalmu tetap di ponselmu',
  privacy='Privasi', terms='Ketentuan', contact='Kontak',
  sep='.', days=['Sen', 'Sel', 'Rab', 'Kam', 'Jum'], types=['Tutorial', 'Kuliah', 'Praktikum'],
  now='Sekarang · sisa 32 mnt', next='Berikutnya · 3 j 42 mnt lagi',
  layouts=['Daftar hari ini', 'Kisi minggu', 'Kuliah berikutnya'], places=['Layar kunci', 'Layar utama'],
  facts=[('Diketik', 'Sekali'), ('Akun', 'Tidak ada'), ('Harga', 'Gratis'), ('Bahasa', 'EN · MS · ID')],
  gallery=[('Mulai', 'Beri nama semester sekali, atau impor file.'), ('Hari ini', 'Sekarang, berikutnya, dan jam kosong.'),
           ('Minggu', 'Lima hari di 360 dp. Minggu A dan B.'), ('Ubah slot', 'Cip untuk jam umum. Tahan untuk hapus.'),
           ('Mata kuliah', 'Kode, stabilo, dosen, jam.'), ('Wallpaper', 'Dibuat di sekitar jam dan ikonmu.'),
           ('Arsip', 'Semester lalu, hanya baca, bisa diekspor.')],
  nos=[('Akun', 'Buka dan langsung ketik'), ('Cloud', 'Tersimpan di ponsel ini'), ('Iklan', ''),
       ('Feed sosial', 'Jadwalmu tetap milikmu'), ('Pelacak', 'Tanpa analitik, tanpa ID iklan')],
  widTitle=('Terang · widget', 'Gelap · widget'), widNext='Kuliah berikutnya', widToday='Hari ini', widWeek='Minggu',
  shot='Tangkapan layar dari aplikasi'),
}

GALLERY_SHOTS = ['first', 'today', 'week', 'sheet', 'subjects', 'wall', 'archive']
# Wallpaper b is shown on the lock screen: on a Pixel home screen the
# launcher's date sits over the week grid's title.
WALLS = [('a.', 'wall_a', 0), ('b.', 'wall_b', 0), ('c.', 'wall_c', 0)]

e = html.escape


def style(d):
    return ';'.join(f'{k}:{v}' for k, v in d.items())


def mark(c, dark):
    if dark:
        return style({'font-family': "'Instrument Serif',serif", 'font-size': '28px', 'line-height': '1.2',
                      'background': c, 'color': '#1b2233', 'padding': '0 5px', 'border-radius': '2px'})
    return style({'font-family': "'Instrument Serif',serif", 'font-size': '28px', 'line-height': '1.15',
                  'background-image': f'linear-gradient(100deg,transparent 1%,{c} 2.5%,{c} 97%,transparent 99%)',
                  'background-repeat': 'no-repeat', 'background-position': '0 88%', 'background-size': '100% 55%',
                  'padding': '0 4px', 'margin': '0 -4px'})


def grid_html(c):
    gut, head = 7, 6
    colw, rh = (100 - gut) / 5, (100 - head) / 9
    pc = lambda v: f'{v:.4f}%'
    out = []
    for h in range(10):
        out.append(f'<div style="position:absolute;left:0;right:0;top:{pc(head + h * rh)};border-top:1px solid rgba(var(--k),.18)">'
                   f'<span style="position:absolute;left:0;top:2px;font-size:11px;color:rgba(var(--k),.7);font-variant-numeric:tabular-nums">{8 + h:02d}</span></div>')
    for i, d in enumerate(c['days']):
        extra = 'background:rgb(var(--k));color:rgb(var(--g));' if i == 4 else ''
        out.append(f'<div style="position:absolute;top:0;left:calc({pc(gut + i * colw)} + 2px);width:calc({pc(colw)} - 4px);height:{pc(head - 1.2)};'
                   f'display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;border-radius:2px;{extra}">{e(d)} {21 + i}</div>')
    for i, (sid, d, s, en, room) in enumerate(RAW):
        half = 1 if i == 5 else 2 if i == 15 else 0
        left = gut + (d + (0.5 if half == 2 else 0)) * colw
        width = colw / 2 if half else colw
        st = (f'position:absolute;left:calc({pc(left)} + 2px);width:calc({pc(width)} - 4px);top:calc({pc(head + (s - 480) / 60 * rh)} + 2px);'
              f'height:calc({pc((en - s) / 60 * rh)} - 4px);background:{HL[sid]};color:#1b2233;border-radius:2px;padding:5px;box-sizing:border-box;'
              'display:flex;flex-direction:column;gap:1px;overflow:hidden;transform:rotate(-.3deg)')
        out.append(f'<div data-blk="" style="{st}"><span style="font-size:clamp(10px,1vw,12px);font-weight:700;line-height:1.2;white-space:nowrap">{SUB[sid]}</span>'
                   f'<span style="font-size:clamp(9px,.9vw,11px);line-height:1.2;white-space:nowrap">{e(room)}</span></div>')
    return '\n'.join(out)


def day_rows(c):
    tt = lambda h: h + c['sep'] + '00'
    rows = [(tt('08'), 'Database Systems', 'CS230 · BT 5 · ' + c['types'][0], 'db', '', False, True),
            (tt('10'), 'Academic English', 'EN110 · DK 2 · ' + c['types'][1], 'en', c['now'], True, False),
            (tt('15'), 'Computer Networks', 'CS210 · MK 3 · ' + c['types'][2], 'cn', c['next'], False, False),
            (c['days'][0], 'Data Structures', 'CS201 · DK 3 · ' + c['types'][1], 'ds', '', False, False)]
    out = []
    for t, name, meta, sid, state, inv, past in rows:
        st = ('display:grid;grid-template-columns:56px minmax(0,1fr);gap:14px;padding:16px 12px;margin:0 -12px;'
              f'border-bottom:1px solid rgba(var(--k),.25);border-radius:2px;opacity:{".45" if past else "1"};'
              + ('background:rgb(var(--k));color:rgb(var(--g));' if inv else ''))
        state_html = (f'<div style="font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">{e(state)}</div>'
                      if state else '')
        out.append(f'<div data-row="" style="{st}"><span style="font-size:15px;font-weight:600;font-variant-numeric:tabular-nums">{e(t)}</span>'
                   f'<div style="min-width:0">{state_html}<span data-rmark="" style="{mark(HL[sid], inv)}">{e(name)}</span>'
                   f'<div style="font-size:13px;opacity:.75;margin-top:6px">{e(meta)}</div></div></div>')
    return '\n'.join(out)


def phone(src, alt, w, h, radius, rotate='0deg', offset=6, extra=''):
    return (f'<div style="width:{w}px;height:{h}px;overflow:hidden;border-radius:{radius}px;outline:1.5px solid rgb(var(--k));'
            f'outline-offset:{offset}px;transform:rotate({rotate});{extra}"><img src="{src}" alt="{e(alt)}" width="{w}" height="{h}" '
            f'loading="lazy" decoding="async" style="display:block;width:100%;height:100%;object-fit:cover"></div>')


def widget_panel(c, prefix, tag, i):
    dark = tag == 'dark'
    wall = '#3a4456' if dark else '#8a9bb3'
    label = 'rgba(236,232,220,.85)' if dark else '#1b2233'
    lab = f'font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{label}'
    img = lambda k, w, h: (f'<img src="{prefix}wid_{tag}_{k}.jpg" alt="{e(c["shot"])}" width="{w}" height="{h}" loading="lazy" '
                           f'style="display:block;width:{w}px;height:{h}px;border-radius:20px">')
    return (f'<div data-wid="" style="border-radius:8px;overflow:hidden;outline:1.5px solid rgb(var(--k));background:{wall};'
            'padding:28px 28px 32px;display:flex;flex-direction:column;gap:22px;width:412px;max-width:100%;box-sizing:border-box">'
            f'<div style="{lab};font-size:12px">{e(c["widTitle"][i])}</div>'
            f'<div style="display:flex;gap:12px;align-items:flex-start">{img("next", 172, 224)}'
            f'<div style="{lab};line-height:1.7;padding-top:4px">2 × 2<br>{e(c["widNext"])}</div></div>'
            f'<div>{img("today", 356, 221)}<div style="{lab};margin-top:8px">4 × 2 · {e(c["widToday"])}</div></div>'
            f'<div>{img("week", 356, 458)}<div style="{lab};margin-top:8px">4 × 4 · {e(c["widWeek"])}</div></div></div>')


def page(lang):
    c = C[lang]
    up = '' if lang == 'en' else '../'
    shots = f'{up}assets/screens/{lang}/'
    here = BASE if lang == 'en' else f'{BASE}{lang}/'
    lang_links = ''.join(
        f'<a href="{up}{"" if k == "en" else k + "/"}" hreflang="{k}"{" aria-current=\"page\"" if k == lang else ""} '
        f'style="height:34px;min-width:38px;padding:0 8px;display:flex;align-items:center;justify-content:center;border-radius:2px;'
        f'text-decoration:none;font-size:13px;font-weight:600;'
        + ('background:rgb(var(--k));color:rgb(var(--g))' if k == lang else 'color:rgb(var(--k))') + f'">{t}</a>'
        for k, t in (('en', 'EN'), ('ms', 'BM'), ('id', 'ID')))
    play = (f'<a href="#get" style="display:inline-flex;align-items:center;gap:14px;height:58px;padding:0 22px;background:rgb(var(--k));'
            'color:rgb(var(--g));border-radius:2px;text-decoration:none"><span style="display:flex;flex-direction:column;line-height:1.15">'
            f'<span style="font-size:10px;font-weight:600;letter-spacing:.14em">{e(c["getOn"])}</span>'
            '<span style="font-size:18px;font-weight:600">Google Play</span></span></a>')
    letters = ''.join(f'<span style="display:inline-block;overflow:hidden;padding-bottom:.12em"><span data-hl="" style="display:inline-block">{ch}</span></span>'
                      for ch in 'Jadual')
    facts = ''.join(f'<div data-fact="" style="padding:18px 20px 20px 0"><div style="font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;'
                    f'color:rgba(var(--k),.7)">{e(k)}</div><div style="font-family:\'Instrument Serif\',serif;font-size:clamp(30px,3.2vw,44px);line-height:1;'
                    f'margin-top:8px">{e(v)}</div></div>' for k, v in c['facts'])
    wopts = ''.join(f'<div data-wopt="" style="display:grid;grid-template-columns:34px minmax(0,1fr) auto;gap:10px;align-items:baseline;padding:14px 0;'
                    f'border-bottom:1px solid rgba(var(--k),.3);opacity:{1 if i == 0 else .35}"><span style="font-family:\'Instrument Serif\',serif;font-style:italic;'
                    f'font-size:24px">{n}</span><span style="font-family:\'Instrument Serif\',serif;font-size:28px">{e(c["layouts"][i])}</span>'
                    f'<span style="font-size:13px;font-weight:600;color:rgba(var(--k),.75)">{e(c["places"][p])}</span></div>'
                    for i, (n, _, p) in enumerate(WALLS))
    wphones = ''.join(f'<div data-wph="" style="position:absolute;inset:0;overflow:hidden;border-radius:26px;outline:1.5px solid rgb(var(--k));'
                      f'outline-offset:6px;opacity:{1 if i == 0 else 0}"><img src="{shots}{f}.jpg" alt="{e(c["layouts"][i])}" width="290" height="644" '
                      'loading="lazy" style="display:block;width:100%;height:100%;object-fit:cover"></div>'
                      for i, (_, f, _) in enumerate(WALLS))
    gallery = ''.join(
        '<div style="flex:none;width:252px;display:flex;flex-direction:column;gap:14px">'
        + phone(f'{up}assets/screens/first.jpg' if s == 'first' else f'{shots}{s}.jpg', t, 252, 560, 22, offset=4)
        + f'<div style="display:grid;grid-template-columns:30px minmax(0,1fr);gap:8px;margin-top:6px"><span style="font-family:\'Instrument Serif\',serif;'
          f'font-style:italic;font-size:20px;color:var(--rule)">{i + 1}.</span><div><div style="font-family:\'Instrument Serif\',serif;font-size:22px;'
          f'line-height:1">{e(t)}</div><div style="font-size:13px;line-height:1.5;color:rgba(var(--k),.75);margin-top:5px">{e(d)}</div></div></div></div>'
        for i, (s, (t, d)) in enumerate(zip(GALLERY_SHOTS, c['gallery'])))
    nos = ''.join(f'<div data-no="" style="display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:6px 0 12px;'
                  'border-bottom:1px solid rgba(var(--k),.3)"><span style="position:relative;font-family:\'Instrument Serif\',serif;'
                  f'font-size:clamp(46px,7.6vw,122px);line-height:1.05">{e(t)}<span data-strike="" style="position:absolute;left:-2%;right:-2%;top:54%;'
                  'height:clamp(3px,.4vw,6px);background:var(--rule);transform:rotate(-1.2deg);transform-origin:0 50%;border-radius:3px"></span></span>'
                  f'<span style="font-size:13px;font-weight:600;color:rgba(var(--k),.75);text-align:right;max-width:220px">{e(s)}</span></div>'
                  for t, s in c['nos'])
    mq_items = [('Timetable.', '#FFE45C'), ('Jadual.', '#8EC5FF'), ('Jadwal.', '#FF94C2')] * 2
    marquee = ''.join(f'<span style="padding-right:.6em;font-family:\'Instrument Serif\',serif;font-size:clamp(70px,11vw,180px);line-height:1.1">'
                      f'<span style="{mark(col, True).replace("font-size:28px", "font-size:inherit").replace("padding:0 5px", "padding:0 .12em")}">{t}</span></span>'
                      for t, col in mq_items)
    fw = lambda i, it='': (f'<span style="display:inline-block;overflow:hidden;padding-bottom:.08em"><span data-fw="" style="display:inline-block{it}">'
                           f'{e(c["fw" + str(i)])}</span></span>')
    serif = "font-family:'Instrument Serif',serif"
    q = lambda k, r=True: (f'<div{" data-r=\"\"" if r else ""} style="{serif};font-style:italic;font-size:26px;color:var(--rule)">{e(c[k])}</div>')
    h2 = lambda k, mw, r=True: (f'<h2{" data-r=\"\"" if r else ""} style="margin:10px 0 0;{serif};font-weight:400;font-size:clamp(44px,6vw,88px);'
                                f'line-height:.98;letter-spacing:-.015em;max-width:{mw}px">{e(c[k])}</h2>')
    para = lambda k, mw, r=True: (f'<p{" data-r=\"\"" if r else ""} style="margin:22px 0 0;font-size:16px;line-height:1.7;color:rgba(var(--k),.8);'
                                  f'max-width:{mw}px;text-wrap:pretty">{e(c[k])}</p>')
    pad = 'padding-left:clamp(48px,7vw,104px);padding-right:clamp(20px,4vw,56px)'
    hreflang = ''.join(f'<link rel="alternate" hreflang="{k}" href="{BASE}{"" if k == "en" else k + "/"}">' for k in ('en', 'ms', 'id'))

    return f'''<!doctype html>
<html lang="{c['htmlLang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<meta property="og:title" content="{e(c['title'])}">
<meta property="og:description" content="{e(c['desc'])}">
<meta property="og:image" content="{BASE}assets/screens/{lang}/today.jpg">
<meta property="og:url" content="{here}">
<meta name="theme-color" content="#f3f0e6">
<link rel="canonical" href="{here}">
{hreflang}
<link rel="icon" href="{up}assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<div data-root="" style="position:relative;z-index:1;font-family:'IBM Plex Sans',sans-serif;color:rgb(var(--k))">

<div data-prog="" style="position:fixed;top:0;left:0;right:0;height:3px;background:#FFE45C;transform:scaleX(0);transform-origin:0 50%;z-index:80"></div>

<nav data-nav="" style="position:fixed;top:0;left:0;right:0;z-index:75;background:rgba(var(--g),.94);border-bottom:1.5px solid rgb(var(--k))">
<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;height:64px;padding:0 clamp(20px,4vw,56px) 0 clamp(48px,7vw,104px)">
<a href="#top" style="{serif};font-style:italic;font-size:28px;text-decoration:none">Jadual</a>
<div style="display:flex;align-items:center;gap:clamp(12px,2.4vw,32px);font-size:14px;font-weight:500">
<a data-navlink="" href="#week" style="text-decoration:none">{e(c['navWeek'])}</a>
<a data-navlink="" href="#wallpaper" style="text-decoration:none">{e(c['navWall'])}</a>
<a data-navlink="" href="#widgets" style="text-decoration:none">{e(c['navWid'])}</a>
<div role="group" aria-label="Language" style="display:flex;gap:2px;padding:2px;border:1.5px solid rgb(var(--k));border-radius:2px">{lang_links}</div><a data-navget="" href="#get" style="height:40px;padding:0 16px;display:flex;align-items:center;border:1.5px solid rgb(var(--k));border-radius:2px;text-decoration:none;font-weight:600;white-space:nowrap">{e(c['getApp'])}</a>
</div>
</div>
</nav>

<header id="top" data-hero="" style="position:relative;min-height:100vh;padding:130px clamp(20px,4vw,56px) 56px clamp(48px,7vw,104px);box-sizing:border-box;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));gap:48px;align-items:center;overflow:hidden">
<div style="position:relative;z-index:2">
<div data-hf="" style="font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:rgba(var(--k),.7)">{e(c['kicker'])}</div>
<h1 aria-label="Jadual" style="margin:20px 0 0;{serif};font-weight:400;font-size:clamp(110px,18vw,280px);line-height:.84;letter-spacing:-.025em;display:flex">{letters}</h1>
<p style="margin:14px 0 0;max-width:560px"><span data-mark="" style="{serif};font-style:italic;font-size:clamp(28px,3.2vw,44px);line-height:1.2;background-image:linear-gradient(100deg,transparent 1%,#FFE45C 2%,#FFE45C 97%,transparent 99%);background-repeat:no-repeat;background-position:0 88%;background-size:100% 55%;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:0 4px;margin:0 -4px;color:#1b2233">{e(c['tagline'])}</span></p>
<p data-hf="" style="margin:22px 0 0;font-size:16px;line-height:1.7;color:rgba(var(--k),.8);max-width:480px;text-wrap:pretty">{e(c['heroP'])}</p>
<div data-hf="" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:32px;align-items:center">
{play}
<a href="#week" style="height:58px;padding:0 20px;display:inline-flex;align-items:center;gap:10px;border:1.5px solid rgb(var(--k));border-radius:2px;text-decoration:none;font-size:15px;font-weight:600">{e(c['watch'])}</a>
</div>
</div>
<div data-hpar="" style="position:relative;z-index:1;justify-self:center"><div data-hphone="" style="display:flex;flex-direction:column;gap:12px">
{phone(shots + 'today.jpg', c['gallery'][1][0], 290, 644, 26, '1.5deg')}
<div style="display:flex;justify-content:space-between;{serif};font-style:italic;font-size:17px;color:rgba(var(--k),.75);margin-top:10px"><span>{e(c['fig'])} 1</span><span>{e(c['fig1'])}</span></div>
</div></div>
<span data-stamp="" style="position:absolute;right:clamp(20px,6vw,90px);top:110px;width:120px;height:120px;border:2px solid var(--rule);border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--rule);transform:rotate(-12deg);{serif};z-index:3"><span style="font-style:italic;font-size:56px;line-height:.9">A+</span><span style="font-size:11px;font-family:'IBM Plex Sans',sans-serif;font-weight:600;letter-spacing:.1em">{e(c['week7'])}</span></span>
</header>

<div data-facts="" style="border-top:1.5px solid rgb(var(--k));border-bottom:1.5px solid rgb(var(--k));margin-left:clamp(48px,7vw,104px);display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));background:rgba(var(--g),.7)">
{facts}
</div>

<section id="week" data-wk="" style="position:relative;height:100vh;padding:90px clamp(20px,4vw,56px) 32px clamp(48px,7vw,104px);box-sizing:border-box;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:40px;align-items:center;overflow:hidden">
<div>
{q('q1', False)}
{h2('h1', 560, False)}
{para('p1', 440, False)}
<div style="display:flex;align-items:baseline;gap:14px;margin-top:28px"><span data-wkn="" style="{serif};font-size:clamp(110px,12vw,170px);line-height:.8;font-variant-numeric:tabular-nums">16</span><span style="font-size:14px;font-weight:600;color:rgba(var(--k),.75)">{e(c['of16'])}</span></div>
</div>
<div style="position:relative;width:100%;max-width:580px;justify-self:center;padding:18px;background:rgb(var(--g));border:1.5px solid rgb(var(--k));box-sizing:border-box;transform:rotate(-.6deg)">
<div style="display:flex;justify-content:space-between;align-items:baseline;padding-bottom:10px;border-bottom:1.5px solid rgb(var(--k))"><span style="{serif};font-size:32px">{e(c['weekTitle'])}</span><span style="font-size:13px;font-weight:600">Sem 1 2026/27 · A</span></div>
<div data-grid="" style="position:relative;height:min(58vh,500px);margin-top:10px">
{grid_html(c)}
</div>
</div>
</section>

<section data-sec="" style="position:relative;padding:130px clamp(20px,4vw,56px) 130px clamp(48px,7vw,104px);display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,400px),1fr));gap:56px;align-items:center;border-top:1.5px solid rgb(var(--k))">
<div>
{q('q2')}
{h2('h2', 900)}
{para('p2', 460)}
<div style="margin-top:32px;border-top:1.5px solid rgb(var(--k));max-width:520px">
{day_rows(c)}
</div>
</div>
<div data-cphone="" style="justify-self:center;display:flex;flex-direction:column;gap:12px">
{phone(shots + 'week.jpg', c['gallery'][2][0], 290, 644, 26, '-1.5deg')}
<div style="display:flex;justify-content:space-between;{serif};font-style:italic;font-size:17px;color:rgba(var(--k),.75);margin-top:10px"><span>{e(c['fig'])} 2</span><span>{e(c['fig2'])}</span></div>
</div>
</section>

<section id="wallpaper" data-wall="" style="position:relative;height:100vh;padding:90px clamp(20px,4vw,56px) 32px clamp(48px,7vw,104px);box-sizing:border-box;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:40px;align-items:center;overflow:hidden;border-top:1.5px solid rgb(var(--k))">
<div>
{q('q3', False)}
{h2('h3', 560, False)}
{para('p3', 440, False)}
<div style="margin-top:26px;border-top:1.5px solid rgb(var(--k));max-width:440px">
{wopts}
</div>
</div>
<div data-wfit="" style="justify-self:center;position:relative;width:290px;height:644px;transform:scale(var(--ws,1));transform-origin:50% 50%;margin:calc((var(--ws,1) - 1) * 322px) 0">
{wphones}
</div>
</section>

<section id="widgets" style="position:relative;padding:130px clamp(20px,4vw,56px) 130px clamp(48px,7vw,104px);border-top:1.5px solid rgb(var(--k))">
{q('q4')}
{h2('h4', 860)}
{para('p4', 560)}
<div style="display:flex;flex-wrap:wrap;gap:24px;margin-top:48px">
{widget_panel(c, shots, 'light', 0)}
{widget_panel(c, shots, 'dark', 1)}
</div>
</section>

<section data-gal="" style="position:relative;height:100vh;overflow:hidden;border-top:1.5px solid rgb(var(--k));display:flex;flex-direction:column;justify-content:center">
<div style="display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:0 clamp(20px,4vw,56px) 0 clamp(48px,7vw,104px)">
<h2 style="margin:0;{serif};font-weight:400;font-size:clamp(38px,4.4vw,64px);line-height:1">{e(c['galH'])}</h2>
<span data-turn="" style="{serif};font-style:italic;font-size:22px;white-space:nowrap">{e(c['turn'])}</span>
</div>
<div data-track="" style="display:flex;gap:40px;padding:36px clamp(20px,4vw,56px) 0 clamp(48px,7vw,104px);width:max-content">
{gallery}
</div>
</section>

<section style="position:relative;padding:140px clamp(20px,4vw,56px) 140px clamp(48px,7vw,104px);border-top:1.5px solid rgb(var(--k))">
{q('crossed')}
<div style="margin-top:30px">
{nos}
</div>
<p data-r="" style="margin:48px 0 0;font-size:16px;line-height:1.7;color:rgba(var(--k),.8);max-width:560px">{c['sampai'].format(s=SAMPAI)}</p>
</section>

<section style="position:relative;padding:100px 0;border-top:1.5px solid rgb(var(--k));overflow:hidden">
<div style="{pad};font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:rgba(var(--k),.75)">English · Bahasa Melayu · Bahasa Indonesia</div>
<div data-mq="" style="display:flex;width:max-content;margin-top:30px;white-space:nowrap">
{marquee}
</div>
</section>

<footer id="get" style="position:relative;padding:140px clamp(20px,4vw,56px) 40px clamp(48px,7vw,104px);border-top:1.5px solid rgb(var(--k));overflow:hidden">
{q('freeOn')}
<h2 style="margin:12px 0 0;{serif};font-weight:400;font-size:clamp(70px,13vw,220px);line-height:.9;letter-spacing:-.02em;display:flex;flex-wrap:wrap;gap:0 .2em">{fw(0)}{fw(1)}{fw(2, ';font-style:italic')}</h2>
<div data-r="" style="display:flex;flex-wrap:wrap;gap:14px;margin-top:44px;align-items:center">
{play}
<span style="font-size:14px;font-weight:500;color:rgba(var(--k),.75)">{e(c['foot'])}</span>
</div>
<div style="margin-top:140px;padding-top:18px;border-top:1.5px solid rgb(var(--k));display:flex;flex-wrap:wrap;justify-content:space-between;gap:16px;font-size:13px;font-weight:500">
<span>© 2026 Jadual</span>
<div style="display:flex;gap:20px"><a href="{up}privacy/" style="text-decoration:none">{e(c['privacy'])}</a><a href="{up}terms/" style="text-decoration:none">{e(c['terms'])}</a><a href="mailto:{CONTACT}" style="text-decoration:none">{e(c['contact'])}</a></div>
</div>
</footer>
</div>
<script src="{up}assets/vendor/gsap.min.js"></script>
<script src="{up}assets/vendor/ScrollTrigger.min.js"></script>
<script src="{up}assets/vendor/lenis.min.js"></script>
<script src="{up}assets/landing.js"></script>
</body>
</html>
'''


def main():
    for lang in ('en', 'ms', 'id'):
        out = ROOT / ('index.html' if lang == 'en' else f'{lang}/index.html')
        out.parent.mkdir(parents=True, exist_ok=True)
        text = page(lang)
        assert '—' not in text, f'em-dash in {lang}'
        out.write_text(text)
        print('wrote', out.relative_to(ROOT))


if __name__ == '__main__':
    main()
