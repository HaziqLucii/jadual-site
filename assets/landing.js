// Scroll scenes ported from the design file's setup(). Without GSAP, with
// reduced motion, or on narrow screens the page stays fully static and
// readable: every element's resting state is its final state.
(function () {
  var g = window.gsap, ST = window.ScrollTrigger;
  var root = document.querySelector('[data-root]');
  var fit = function () {
    root.style.setProperty('--ws', String(Math.min(1, Math.max(.5, (window.innerHeight - 150) / 644))));
  };
  fit();
  window.addEventListener('resize', fit);
  if (!g || !ST || !root) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('[data-wopt]').forEach(function (o) { o.style.opacity = 1; });
    return;
  }
  g.registerPlugin(ST);
  var q = g.utils.selector(root);
  // Pin the scenes only where a whole scene fits on screen, as the design does.
  var wide = window.innerWidth >= 761 && window.innerHeight >= 720;
  q('[data-pinsec]').forEach(function (el) {
    el.style.height = wide ? '100vh' : 'auto';
    el.style.overflow = wide ? 'hidden' : 'visible';
  });
  var walls = q('[data-wph]'), wopts = q('[data-wopt]');

  var start = function () {
    g.to(q('[data-prog]'), { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: .3 } });
    var nav = q('[data-nav]')[0];
    ST.create({ start: 0, end: 'max', onUpdate: function (self) {
      g.to(nav, { yPercent: (self.direction === 1 && self.scroll() > 120) ? -100 : 0, duration: .2, ease: 'power2.out', overwrite: true });
    } });
    g.from(q('[data-hl]'), { yPercent: 115, duration: 1.1, ease: 'power4.out', stagger: .06, delay: .1 });
    g.fromTo(q('[data-mark]'), { backgroundSize: '0% 55%' }, { backgroundSize: '100% 55%', duration: .9, ease: 'power2.inOut', delay: .7 });
    g.from(q('[data-hf]'), { y: 18, opacity: 0, duration: .8, ease: 'power3.out', stagger: .09, delay: .45 });
    g.from(q('[data-hphone]'), { y: 90, opacity: 0, duration: 1.2, ease: 'power3.out', delay: .3 });
    g.from(q('[data-stamp]'), { scale: 2.2, opacity: 0, rotate: -40, duration: .35, ease: 'power4.in', delay: 1.3 });
    var hero = q('[data-hero]')[0];
    g.to(q('[data-hpar]'), { y: -140, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
    g.to(q('[data-stamp]'), { y: -220, rotate: -4, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
    g.from(q('[data-fact]'), { y: 20, opacity: 0, duration: .7, ease: 'power3.out', stagger: .08, scrollTrigger: { trigger: q('[data-fact]')[0], start: 'top 92%' } });
    q('[data-r]').forEach(function (el) {
      g.from(el, { y: 26, opacity: 0, duration: .8, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 88%' } });
    });

    var blks = q('[data-blk]'), cnt = q('[data-wkn]')[0], o = { v: 0 };
    cnt.textContent = '0';
    var tl = g.timeline({ scrollTrigger: wide
      ? { trigger: q('[data-wk]')[0], start: 'top top', end: '+=240%', pin: true, scrub: .6, anticipatePin: 1 }
      : { trigger: q('[data-wk]')[0], start: 'top 70%' } });
    tl.fromTo(blks, { clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)', duration: .4, stagger: wide ? .25 : .08, ease: 'power2.inOut' }, 0)
      .to(o, { v: 16, duration: (wide ? .25 : .08) * 15 + .4, ease: 'none', onUpdate: function () { cnt.textContent = String(Math.round(o.v)); } }, 0);
    if (wide) tl.to({}, { duration: .6 });

    q('[data-row]').forEach(function (r) {
      var t2 = g.timeline({ scrollTrigger: { trigger: r, start: 'top 84%' } });
      t2.from(r, { opacity: 0, y: 14, duration: .4, ease: 'power2.out' });
      var m = r.querySelector('[data-rmark]');
      if (m && getComputedStyle(m).backgroundSize.indexOf('55%') > -1) {
        t2.fromTo(m, { backgroundSize: '0% 55%' }, { backgroundSize: '100% 55%', duration: .6, ease: 'power2.inOut' }, '-=.1');
      }
    });
    g.from(q('[data-cphone]'), { y: 80, opacity: 0, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: q('[data-cphone]')[0], start: 'top 85%' } });

    var wt = g.timeline({ scrollTrigger: wide
      ? { trigger: q('[data-wall]')[0], start: 'top top', end: '+=220%', pin: true, scrub: .5, anticipatePin: 1 }
      : { trigger: q('[data-wall]')[0], start: 'top 40%', end: 'bottom 30%', scrub: .5 } });
    for (var i = 1; i < walls.length; i++) {
      wt.to(walls[i - 1], { opacity: 0, yPercent: -4, rotate: -2, duration: .5 }, i)
        .fromTo(walls[i], { opacity: 0, yPercent: 4, rotate: 2 }, { opacity: 1, yPercent: 0, rotate: 0, duration: .5 }, i)
        .to(wopts[i - 1], { opacity: .35, duration: .3 }, i)
        .to(wopts[i], { opacity: 1, duration: .3 }, i);
    }
    wt.to({}, { duration: .8 });

    g.from(q('[data-wid]'), { y: 60, opacity: 0, rotate: function (i) { return i ? 1.5 : -1.5; }, duration: .9, ease: 'power3.out', stagger: .12,
      scrollTrigger: { trigger: q('[data-wid]')[0], start: 'top 85%' } });

    if (wide) {
      var gal = q('[data-gal]')[0], track = q('[data-track]')[0];
      var dist = function () { return Math.max(0, track.scrollWidth - gal.clientWidth); };
      g.to(track, { x: function () { return -dist(); }, ease: 'none',
        scrollTrigger: { trigger: gal, start: 'top top', end: function () { return '+=' + dist(); }, pin: true, scrub: .5, invalidateOnRefresh: true, anticipatePin: 1 } });
    }

    q('[data-no]').forEach(function (l) {
      g.fromTo(l.querySelector('[data-strike]'), { scaleX: 0, rotation: -1.2 }, { scaleX: 1, rotation: -1.2, ease: 'power1.inOut', scrollTrigger: { trigger: l, start: 'top 80%', end: 'top 55%', scrub: true } });
    });

    var mq = q('[data-mq]')[0], mt = g.to(mq, { xPercent: -50, repeat: -1, duration: 40, ease: 'none' });
    ST.create({ trigger: mq, start: 'top bottom', end: 'bottom top', onUpdate: function (self) {
      var v = self.getVelocity();
      g.to(mt, { timeScale: (v < 0 ? -1 : 1) * (1 + Math.min(Math.abs(v) / 250, 6)), duration: .2, overwrite: true });
      g.to(mt, { timeScale: v < 0 ? -1 : 1, duration: 1.2, delay: .2, ease: 'power2.out' });
    } });

    g.from(q('[data-fw]'), { yPercent: 110, duration: 1, ease: 'power4.out', stagger: .1, scrollTrigger: { trigger: q('[data-fw]')[0], start: 'top 88%' } });

    if (window.Lenis) {
      var lenis = new window.Lenis({ lerp: .1, smoothWheel: true });
      lenis.on('scroll', ST.update);
      g.ticker.add(function (t) { lenis.raf(t * 1000); });
      g.ticker.lagSmoothing(0);
      root.querySelectorAll('a[href^="#"]').forEach(function (a) {
        a.addEventListener('click', function (ev) {
          var id = a.getAttribute('href').slice(1), el = id && document.getElementById(id);
          if (el) { ev.preventDefault(); lenis.scrollTo(el, { duration: 1.4 }); }
        });
      });
    }
    setTimeout(function () { ST.refresh(); }, 400);
    window.addEventListener('load', function () { ST.refresh(); });
  };

  var go = function () { start(); };
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(go, go); else go();
})();
