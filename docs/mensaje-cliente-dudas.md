# Mensajes para el cliente (Arriaza Consulting)

## Estado DNS — verificado 2026-08-04 (tarde)

⚠️ **El cambio de NS todavía NO está aplicado.** Verificado sin caché:

- `dig +norec @b.nic.cl arriazaconsulting.cl NS` → sigue devolviendo
  `janet.ns.cloudflare.com` / `rodney.ns.cloudflare.com`. Como se consultó al
  autoritativo del TLD .cl, no es caché local: es lo que NIC tiene publicado.
- La zona de Cloudflare tampoco tiene registro A ni www (`dig @janet...` vacío).
- **Del lado de Vercel está todo listo:** `dig @ns1.vercel-dns.com arriazaconsulting.cl A`
  ya responde `64.29.17.1` / `64.29.17.65`. Apenas NIC publique la delegación, funciona solo.
- Monitoreado 4 min sin cambios. Si Alejandro guardó el cambio en NIC, esperar y
  reverificar; si no aparece en ~1 hora, revisar que el cambio quedó guardado.

Dos caminos válidos (cualquiera sirve):
- **NIC:** servidores de nombre → `ns1.vercel-dns.com` y `ns2.vercel-dns.com`.
- **Cloudflare (si se quedan ahí):** registro `A @ 76.76.21.21` + `CNAME www
  cname.vercel-dns.com`, ambos en "DNS only" (nube gris).

## Dudas pendientes (ninguna respondida aún) — mensaje de WhatsApp

Ver bloque de copy-paste en la respuesta de la sesión. Resumen de lo que falta:

1. **Teléfono y correo definitivos** — hoy publicado: +56 9 4092 1033 /
   admin@arriazaconsulting.cl. El mockup traía +56 9 6188 6452 / gerencia@.
2. **Fotos reales** — hero y retrato de Regina son Unsplash provisorias (marcadas en el
   HTML con `FOTO PROVISORIA`).
3. **Empresas cliente** — autorización para nombrarlas + logos reales (hoy: iniciales).
4. **Cifras** — 10+ empresas, 80+ fiscalizaciones, 10+ años, 100% (¿confirmadas?).
5. **Redes sociales** — los 4 iconos del footer apuntan a `#`.
6. **Agendamiento** — hoy los CTA abren WhatsApp; ¿prefiere Calendly u otra agenda?
7. **"Recursos"** — hoy apunta al blog existente; confirmar si va contenido propio.
