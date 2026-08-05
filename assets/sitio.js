// Activa el modo JS (los reveal solo se ocultan si esto corre)
document.documentElement.classList.add('js');

// Menú móvil
const toggle = document.getElementById('navToggle');
const links = document.getElementById('navLinks');
if (toggle && links) {
    toggle.addEventListener('click', () => links.classList.toggle('open'));
    links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
}

// Reveal al entrar en pantalla
const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('active'); io.unobserve(e.target); } });
}, { threshold: .15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Contadores de las cifras
const animateCount = el => {
    const target = +el.dataset.count, dur = 1200, t0 = performance.now();
    const tick = now => {
        const p = Math.min((now - t0) / dur, 1);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
};
const ioStats = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) { e.target.querySelectorAll('[data-count]').forEach(animateCount); ioStats.unobserve(e.target); }
    });
}, { threshold: .4 });
document.querySelectorAll('.stats').forEach(el => ioStats.observe(el));
