# CLAUDE.md — Cliente: Arriaza Consulting (arriazaconsulting.cl)

Clon de cliente DIXDY. Manda la doctrina del maestro
(`/Users/alejandroriveracarrasco/SaSS/DIXDY/CLAUDE.md` y `docs/23-doctrina-dixdy.md`).

## El negocio

Consultora tributaria/estratégica en Santiago de Chile. Fundadora: **Regina Pastora
Arriaza Benítez** (Contadora Auditora, Ingeniera en Control de Gestión, Magíster en
Tributación, Diplomada en IFRS y en Comunicación Estratégica). Posicionamiento 2026:
**"Comprendemos las decisiones. Protegemos el futuro."** con metodología propia
**I.D.E.A.** (Interpretar, Diagnosticar, Evaluar, Acompañar). Fuentes del contenido en
`docs/` (PDF de posicionamiento + arquitectura web del cliente).

## Categoría

🌱 En incorporación (2026-08-04). Por ahora: solo web (rediseño). Sin Ads, sin panel,
sin correo-worker.

## Infraestructura

- **Repo:** github.com/depsu/arriazaconsulting.cl → **deploy automático por `git push`
  a Vercel** (proyecto `arriazaconsulting-cl`). ⚠️ Un push publica en vivo.
- **URL viva:** https://arriazaconsulting-cl.vercel.app (el dominio propio aún NO sirve).
- **DNS:** arriazaconsulting.cl delegado a Cloudflare (janet/rodney.ns.cloudflare.com)
  pero la **zona está vacía** (sin A ni www) y NO está en nuestra cuenta Cloudflare →
  la administra el cliente u otro tercero. Tutorial para apuntarla:
  `docs/mensaje-cliente-dudas.md`.
- `vercel.json` con `cleanUrls: true` (enlazar `/terminos`, no `/terminos.html`).
- Blog tributario existente en `/blog` (3 posts) — se conserva.
- El repo viejo local (`proyectos-personales/old-no-tomar-en-cuenta/arriazaconsulting.cl`)
  NO se usa.

## Estado del rediseño (2026-08-04)

`index.html` reescrito según el mockup del cliente (navy #0F172A + dorado #C5A059,
Playfair Display). **NO publicado aún** — pendientes antes del push:

1. Confirmar teléfono/correo: sitio viejo usa +56 9 4092 1033 / admin@; el mockup dice
   +56 9 6188 6452 / gerencia@. Hoy la página usa los VIEJOS (verificados).
2. Fotos reales (hero y retrato de Regina son Unsplash provisorias, marcadas con
   comentario `FOTO PROVISORIA` en el HTML).
3. Links reales de redes sociales (hoy `href="#"`).
4. Confirmar cifras (10+ empresas, 80+ fiscalizaciones, 10+ años).
5. OG image nueva (og.jpg sigue siendo la del diseño viejo).

Dudas completas para el cliente: `docs/mensaje-cliente-dudas.md`.
