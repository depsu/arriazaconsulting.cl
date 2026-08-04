# Mensaje para el cliente (Arriaza Consulting) — DNS + dudas

Borrador listo para copiar/pegar (WhatsApp o correo). Redactado en simple.

---

Hola Regina 👋 Te cuento avances del sitio nuevo y necesito confirmar algunas cosas
para dejarlo perfecto. Es un solo mensaje con todo, para no molestarte de a gotitas:

**1) El dominio arriazaconsulting.cl está "desconectado" 🔌**

Tu dominio existe y está bien registrado, pero hoy no muestra el sitio: le faltan dos
"flechas" (registros DNS) que lo apunten al servidor donde vive la página. Por eso el
sitio solo se ve en la dirección provisoria (arriazaconsulting-cl.vercel.app).

El dominio está administrado en una plataforma llamada **Cloudflare**. Hay dos caminos
(el A es el más fácil para ti):

- **Opción A (recomendada):** me das acceso a esa cuenta de Cloudflare (o me dices
  quién la maneja, quizá quien te registró el dominio) y yo dejo todo conectado en
  5 minutos, con candadito de seguridad (https) incluido.
- **Opción B (mini tutorial, ~5 min):**
  1. Entrar a dash.cloudflare.com con la cuenta donde está arriazaconsulting.cl.
  2. Elegir el sitio **arriazaconsulting.cl** → menú **DNS** → **Records**.
  3. Crear registro: Tipo **A**, Nombre **@**, Dirección IPv4 **76.76.21.21**,
     y apagar la nubecita naranja (que quede "DNS only").
  4. Crear otro: Tipo **CNAME**, Nombre **www**, Destino **cname.vercel-dns.com**,
     también "DNS only".
  5. Guardar y avisarme: yo termino la conexión del otro lado y activo el candado
     de seguridad. En unas horas ya funciona www.arriazaconsulting.cl.

**2) Teléfono y correo de contacto ☎️**

En el diseño nuevo aparece **+56 9 6188 6452** y **gerencia@arriazaconsulting.cl**,
pero el sitio actual usa **+56 9 4092 1033** y **admin@arriazaconsulting.cl**.
¿Cuál teléfono y cuál correo dejamos? ¿Y el WhatsApp es ese mismo número?

**3) Fotos reales 📸**

Para que el sitio transmita confianza necesito: una foto profesional tuya (para la
sección "Liderazgo") y, si tienes, fotos de tu oficina o de reuniones con clientes.
Mientras tanto puse fotos genéricas provisorias.

**4) Empresas cliente 🏢**

El diseño muestra a Espacios Constructora, Condominio Villaseca, Control Común y
Restaurante Empanadas de Pamela Díaz. ¿Autorizan aparecer? ¿Tienes sus logos?

**5) Cifras ✔️**

¿Confirmas estos números para publicarlos? **10+ empresas asesoradas, 80+ procesos de
fiscalización acompañados, 10+ años de experiencia**.

**6) Redes sociales 🔗**

El diseño trae iconos de LinkedIn, Instagram, Facebook y YouTube. Pásame los links de
las cuentas que realmente uses (las que no existan, las saco).

**7) Menú "Recursos" 📚**

El diseño incluye una sección "Recursos". ¿Qué te imaginas ahí? Hoy tu sitio tiene un
blog con 3 artículos tributarios que puedo mantener y potenciar. ¿Lo dejamos como
"Blog" o quieres algo más (guías descargables, etc.)?

**8) Agendar reuniones 📅**

Los botones "Agenda un diagnóstico" hoy abren WhatsApp. ¿Te acomoda así, o usas
alguna agenda online (tipo Calendly) para conectarla?

Con esas respuestas dejo el sitio listo para publicar en tu dominio. ¡Gracias! 🙌

---

## Notas internas (no enviar)

- DNS verificado 2026-08-04: NS = janet/rodney.ns.cloudflare.com, zona SIN registros
  (dig A @ y www vacíos). La zona NO está en nuestra cuenta CF (API respondió 0 zonas).
- Falta además: agregar el dominio al proyecto de Vercel `arriazaconsulting-cl`
  (lado nuestro, cuenta de Vercel de Alejandro) — hacerlo cuando el cliente confirme
  el camino A o B.
- IP A de Vercel: 76.76.21.21 · CNAME: cname.vercel-dns.com (estándar Vercel).
