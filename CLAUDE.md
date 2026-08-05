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
- **URL viva:** https://arriazaconsulting.cl ✅ (desde 2026-08-04). `www` redirige 301 al
  apex. La `.vercel.app` sigue existiendo como respaldo.
- **DNS:** NIC Chile delega a `ns1/ns2.vercel-dns.com` (ya NO pasa por Cloudflare). La
  zona la sirve Vercel; no hay panel de DNS externo que tocar.
  ⚠️ El apex NO debe tener `redirect` en Vercel (venía apuntando a www y se invirtió por
  API): el canonical, el sitemap y `llms.txt` usan la versión SIN www.
- `vercel.json` con `cleanUrls: true` (enlazar `/terminos`, no `/terminos.html`).
- Blog tributario existente en `/blog` (3 posts) — se conserva.
- El repo viejo local (`proyectos-personales/old-no-tomar-en-cuenta/arriazaconsulting.cl`)
  NO se usa.

## Estado del rediseño (2026-08-04)

`index.html` reescrito según el mockup del cliente (navy #0F172A + dorado #C5A059,
Playfair Display) y **EN VIVO en el dominio propio**. La estructura calca el mockup:
header blanco, hero con foto sangrada a la derecha, **tríptico** (Servicios | Empresas |
Sobre mí en tarjeta oscura), metodología I.D.E.A., banda de cifras + CTA, y footer de 5
columnas con la cita y la firma "RA".

Ya aplicado con datos reales de Regina: **teléfono +56 9 6188 6452** (en todo el repo,
incluido el blog) y su **foto oficial** en `img/regina-arriaza.jpg`.

Pendientes de contenido (esperando respuesta del cliente):

1. Correo: hoy publica `admin@`; el mockup decía `gerencia@`. Sin confirmar.
2. Foto del hero: sigue provisoria de Unsplash (no tiene fotos de oficina todavía).
   Marcada con el comentario `FOTO PROVISORIA` en el HTML.
3. Links reales de redes sociales (hoy `href="#"`).
4. Confirmar cifras (10+ empresas, 80+ fiscalizaciones, 10+ años).
5. OG image nueva (og.jpg sigue siendo la del diseño viejo).

Dudas completas para el cliente: `docs/mensaje-cliente-dudas.md`.
