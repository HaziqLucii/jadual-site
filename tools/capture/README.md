# Screenshot capture

Real screenshots for the site, taken on the Android emulator (AVD `sampai36`,
1080 × 2400) from a demo build of the app:

1. In the app repo: `flutter build apk --debug --dart-define=JADUAL_DEMO=true`, then
   `adb uninstall io.github.haziqlucii.jadual && adb install build/app/outputs/flutter-apk/app-debug.apk`.
2. Set the emulator clock to the demo moment and clean the status bar and lock screen:
   `adb root; adb shell settings put global auto_time 0; adb shell date 092511182026.00`,
   system UI demo mode (clock 1118, full battery and Wi-Fi, notifications hidden),
   `adb shell locksettings set-disabled false`,
   `adb shell settings put secure lockscreen_use_double_line_clock 0`,
   `adb shell settings put secure lock_screen_show_notifications 0`.
3. Pin the three widgets: `adb shell am start -n io.github.haziqlucii.jadual/.MainActivity --es jadual_debug_pin next_class` (then `today`, `week`).
4. `python3 -c "import full; full.run('en')"`, then switch language with `full.set_lang('en')` and run `ms`, then `id`.
   `arch.py` archives the semester for the First run and Archive shots; run it last.
5. Convert into `assets/screens/<lang>/` (580 px wide JPEGs; widget crops at full size) and rerun `python3 tools/build.py`.

Afterwards restore the emulator: `auto_time 1`, demo mode exit, `locksettings set-disabled true`,
and delete `lockscreen_use_double_line_clock`.
