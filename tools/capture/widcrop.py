import ui, cap, time, re, subprocess, sys
def bounds():
    x = ui.dump()
    out = []
    for m in re.finditer(r'<node [^>]*resource-id="io.github.haziqlucii.jadual:id/widget_image"[^>]*>', x):
        b = list(map(int, re.findall(r'\d+', re.search(r'bounds="([^"]*)"', m.group(0)).group(1))))
        d = re.search(r'content-desc="([^"]*)"', m.group(0))
        out.append((b, d.group(1) if d else ''))
    return out
def grab(prefix):
    """Screenshot the current home page and crop every Jadual widget on it."""
    cap.shot(prefix + '_page')
    res = []
    for i, (b, d) in enumerate(bounds()):
        w, h = b[2] - b[0], b[3] - b[1]
        kind = 'week' if h > 800 else ('today' if w > 700 else 'next')
        out = f'{cap.S}/{prefix}_{kind}.png'
        subprocess.run(['magick', f'{cap.S}/{prefix}_page.png', '-crop', f'{w}x{h}+{b[0]}+{b[1]}', '+repage', out])
        res.append((kind, b))
    return res
if __name__ == '__main__':
    print(grab(sys.argv[1]))
