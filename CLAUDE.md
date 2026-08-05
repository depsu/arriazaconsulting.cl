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

1. ✅ Correo `gerencia@arriazaconsulting.cl` y teléfono/WhatsApp +56 9 6188 6452.
2. ✅ Hero: imagen propia que mandó la clienta (`img/hero-reunion.jpg`) con su texto nuevo.
3. ✅ Redes: solo LinkedIn (es el único link que dio). Faltan Instagram y Facebook.
4. ✅ Cifras: se reemplazaron por 4 pilares cualitativos, porque las 80 fiscalizaciones
   eran de su carrera y no de la empresa (ella misma lo advirtió).
5. ⏳ OG image: `og.jpg` sigue siendo la del diseño viejo.
6. ✅ «Sobre mí» usa una **escena genérica de asesoría** (`img/sobre-mi-asesoria.jpg`)
   que mandó la clienta el 05-08, en reemplazo del retrato de stock. No retrata a Regina
   y el `alt` no lo afirma. Se cambia cuando ella tenga su foto profesional.

Dudas completas para el cliente: `docs/mensaje-cliente-dudas.md`.

## SEO e indexación (2026-08-05)

**Estructura publicada:** además del home, el sitio tiene páginas hijas propias, todas
generadas por `scripts/generar-paginas.py` (NO editar el HTML de esas páginas a mano;
se regeneran). El CSS y el JS son compartidos en `/assets/` — el home también los usa.

- `/metodologia-idea` — la metodología I.D.E.A. en detalle
- `/servicios` — los 6 servicios con anclas (`#estrategia-tributaria`, etc.)
- `/casos` + 3 casos con **texto textual de la clienta** (`docs/casos-reales-cliente.md`)
- `/sobre-regina-arriaza` — perfil profesional

Cada página lleva canonical, Open Graph, migas y schema.org (Service / Article / Person /
BreadcrumbList). `sitemap.xml` (14 URLs) y `llms.txt` están al día.

**Search Console:** la propiedad `sc-domain:arriazaconsulting.cl` está verificada por TXT
en Vercel DNS y dada de alta con `scripts/gsc-add-vercel.py` **del maestro** (hermano de
`gsc-add.py`, que solo sabe de Cloudflare). Sitemap enviado y 8 URLs empujadas por la
Indexing API.
⚠️ La propiedad quedó bajo la **service account**, así que `gsc-queries.py` (que usa el
refresh token OAuth) NO la lista. Para que los reportes la vean, hay que darle acceso al
usuario del OAuth desde la interfaz de Search Console (gestión de Alejandro).

**Los casos van SIN imagen** por pedido de la clienta (05-08): sus piezas de LinkedIn
competían con el texto, que es lo que quiere que se lea. Si alguna vez se vuelven a usar,
ojo: llevan datos impresos y una mostraba `arriazaconsulting-cl.vercel.app` y
`Admin@arriazaconsulting.cl`, ambos obsoletos.
