import subprocess, re, sys, time
import os, shutil
A=os.environ.get('ADB') or shutil.which('adb') or '/opt/homebrew/share/android-commandlinetools/platform-tools/adb'
S=os.environ.get('JADUAL_CAPTURE_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'))
def sh(*a): return subprocess.run([A,'shell',*a],capture_output=True,text=True).stdout
def dump():
    sh('uiautomator','dump','/sdcard/u.xml'); return sh('cat','/sdcard/u.xml')
def find(label, exact=False):
    x=dump()
    for m in re.finditer(r'<node [^>]*>', x):
        n=m.group(0)
        mt=re.search(r' text="([^"]*)"',n); md=re.search(r'content-desc="([^"]*)"',n)
        t=mt.group(1) if mt else ''; d=md.group(1) if md else ''
        v=(t+' '+d).replace('&#10;',' ')
        ok = (label==t or label==d) if exact else (label in v)
        if ok:
            b=list(map(int,re.findall(r'\d+',re.search(r'bounds="([^"]*)"',n).group(1))))
            return ((b[0]+b[2])//2,(b[1]+b[3])//2)
    return None
def tap(label, exact=False, dy=0):
    p=find(label, exact)
    if not p: raise SystemExit(f'not found: {label}')
    sh('input','tap',str(p[0]),str(p[1]+dy)); time.sleep(1.0)
def typ(s): sh('input','text',s.replace(' ','%s')); time.sleep(.6)
def shot(name):
    time.sleep(.8); subprocess.run([A,'emu','screenrecord','screenshot',f'{S}/{name}.png'],capture_output=True)
def key(k): sh('input','keyevent',str(k)); time.sleep(.6)
def swipe(*a): sh('input','swipe',*map(str,a)); time.sleep(1)
def edits():
    x=dump(); out=[]
    for m in re.finditer(r'<node [^>]*class="android.widget.EditText"[^>]*>', x):
        b=list(map(int,re.findall(r'\d+',re.search(r'bounds="([^"]*)"',m.group(0)).group(1))))
        out.append(((b[0]+b[2])//2,(b[1]+b[3])//2))
    return out
def tapxy(p): sh('input','tap',str(p[0]),str(p[1])); time.sleep(.8)
def clear_heads(): swipe(540,300,540,10,100)
