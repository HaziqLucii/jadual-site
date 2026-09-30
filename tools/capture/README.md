# Screenshot capture

Real screenshots for the site, taken on the Android emulator (AVD `sampai36`,
1080 × 2400, run with a window) from debug builds of the app. `v2.py` drives
the build 11 app (Wallpaper Studio, ten papers, reminders); the older
`full.py`, `walls.py` and `arch.py` are kept for the First run and Archive
shots (`first.jpg`, `archive.jpg`), which were not retaken.

Set `JADUAL_CAPTURE_DIR` to a scratch folder; shots land in `$JADUAL_CAPTURE_DIR/shots/<lang>/`.

1. Three APKs from the app repo:
   - demo: `flutter build apk --debug --dart-define=JADUAL_DEMO=true --dart-define=JADUAL_FORCE_PRO=true` (Fri 25.09.2026 11:18)
   - Thursday: the same plus `--dart-define=JADUAL_NOW=2026-09-24T21:40` (Tomorrow wallpaper, so tomorrow is a Friday with classes)
   - real clock: `flutter build apk --debug --dart-define=JADUAL_FORCE_PRO=true` (reminders never fire in demo builds)
2. `adb uninstall io.github.haziqlucii.jadual && adb install demo.apk`, then `adb root`,
   `settings put global auto_time 0`, `date 092511182026.00`, `settings put system time_12_24 24`,
   `settings put global sysui_demo_allowed 1`, `locksettings set-disabled false`,
   `settings put secure lockscreen_use_double_line_clock 0`, `settings put secure lock_screen_show_notifications 0`,
   `pm grant io.github.haziqlucii.jadual android.permission.POST_NOTIFICATIONS`. `v2.py` turns on system UI demo mode itself.
3. Push to `/sdcard/Download/`: `jadual-sample-exam.jadual` (the sample timetable plus a CS230 exam on Wed 30.09, week 8,
   09:00 in DSP Hall), `jadual-sample-routine-site.jadual` (the weekly routine sample with its start moved to 14.09) and
   `jadual-sample-photo.jpg` (a neutral generated gradient, `magick`). Import the exam file once from Settings.
4. Pin the three widgets: `adb shell am start -n io.github.haziqlucii.jadual/.MainActivity --es jadual_debug_pin next_class`
   (then `today`, `week`) and tap Add to home screen each time.
5. Demo build: `python3 -c "import v2; v2.run('en')"`, then for ms and id `v2.set_lang(l); v2.run(l)`.
   The week shot switches the emulator to 360 dp (`wm density 480`) and back.
6. `adb install -r thu.apk` (keeps the data), then `v2.wall_b(l)` per language.
7. `adb install -r real.apk`, `v2.reminder_setup('en')` once, then `v2.notifications(l)` per language (sets the clock just
   before Fri 14:50 and Tue 20:00 so the class and evening-before reminders fire, then crops them from the shade).
8. `python3 convert.py en ms id` writes the JPEGs into `assets/screens/<lang>/`; rerun `python3 tools/build.py`.

Afterwards restore the emulator: `auto_time 1`, `settings delete system time_12_24`, demo mode exit,
`locksettings set-disabled true`, `settings put secure lock_screen_show_notifications 1`,
delete `lockscreen_use_double_line_clock`, remove the pushed files, and shut it down.
