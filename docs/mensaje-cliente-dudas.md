# Estado del cliente Arriaza Consulting

## DNS — ✅ RESUELTO 2026-08-04 (noche)

El dominio quedó funcionando. Verificado en vivo:

- NIC Chile ya delega a `ns1.vercel-dns.com` / `ns2.vercel-dns.com`.
- `https://arriazaconsulting.cl` → **200 OK** con el sitio nuevo y certificado válido.
- `https://www.arriazaconsulting.cl` → **301** al dominio sin www.

**Ojo (corregido acá):** Vercel venía con la redirección al revés (apex → www), pero el
canonical, el sitemap, `llms.txt` y el propio footer apuntan a la versión SIN www. Se
invirtió por la API de Vercel: el apex sirve el sitio y www redirige con 301. Si alguna
vez se vuelve a agregar el dominio, revisar que el apex NO tenga `redirect`.

## Respondido por Regina (2026-08-04, WhatsApp)

- ✅ **Teléfono: +56 9 6188 6452.** Aplicado en todo el sitio (footer, botones flotantes,
  todos los enlaces de WhatsApp y también en el blog y `llms.txt`). El teléfono viejo
  (+56 9 4092 1033) ya no aparece en ningún archivo.
- ✅ **Foto de Regina.** Guardada en `img/regina-arriaza.jpg` (optimizada de 1.4 MB a
  135 KB) y montada en la tarjeta "Sobre mí" con encuadre ajustado para que el degradado
  no le tape el rostro.
- ⏸️ **Foto de oficina:** no tiene por ahora (trabaja desde casa) → el hero sigue con una
  imagen provisoria de Unsplash, marcada en el HTML con `FOTO PROVISORIA`.

## Pendientes (aún sin respuesta)

1. **Correo:** el sitio publica `admin@arriazaconsulting.cl`; el mockup traía
   `gerencia@arriazaconsulting.cl`. Sin confirmar.
2. **WhatsApp:** se asumió que el +56 9 6188 6452 también es WhatsApp (todos los botones
   apuntan ahí). Confirmar.
3. **Empresas cliente:** autorización para nombrarlas + logos reales (hoy: iconos).
4. **Cifras:** 10+ empresas, 80+ fiscalizaciones, 10+ años, 100%.
5. **Redes sociales:** los 4 iconos del footer apuntan a `#`.
6. **Agendamiento:** hoy los CTA abren WhatsApp; ¿prefiere Calendly u otra agenda?
7. **"Recursos":** hoy apunta al blog existente.
