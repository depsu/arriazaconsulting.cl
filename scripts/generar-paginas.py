#!/usr/bin/env python3
"""Genera las páginas hijas del sitio a partir de una plantilla común.

El contenido de los casos es TEXTUAL de Regina Arriaza (docs/casos-reales-cliente.md).
No se inventan datos: si algo no lo dijo la clienta, no va.

Uso: python3 scripts/generar-paginas.py
"""
import html
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = "https://arriazaconsulting.cl"
WSP = "https://wa.me/56961886452"
CORREO = "gerencia@arriazaconsulting.cl"
TEL_HUMANO = "+56 9 6188 6452"

ISOTIPO = ('<span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 64 64" fill="none">'
           '<rect x="3" y="3" width="58" height="58" rx="7" stroke="currentColor" stroke-width="3.2"/>'
           '<path d="M31.5 14 17 50h7.6l9.2-24.4L38 38l-3.4 3.6L37 50h9L31.5 14Z" fill="currentColor"/>'
           '<path d="M40.4 20.6 47 50h-6.2l-4-18.6 3.6-10.8Z" fill="currentColor" opacity=".85"/>'
           '</svg></span>')

FLECHA = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
          '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')

MENU = [("/", "Inicio"), ("/metodologia-idea", "Metodología"), ("/servicios", "Servicios"),
        ("/casos", "Casos"), ("/sobre-regina-arriaza", "Sobre mí"), ("/blog", "Blog")]


def cabecera(activo):
    items = []
    for url, txt in MENU:
        cls = ' class="active"' if url == activo else ''
        items.append(f'                <li><a href="{url}"{cls}>{txt}</a></li>')
    return f'''    <header>
        <div class="wrap nav">
            <a href="/" class="brand" aria-label="Arriaza Consulting — Inicio">
                {ISOTIPO}
                <span>
                    <span class="brand-name">ARRIAZA</span>
                    <span class="brand-sub">Consulting</span>
                    <span class="brand-tagline">Estrategia Tributaria &amp; Control de Decisiones Empresariales</span>
                </span>
            </a>
            <button class="nav-toggle" id="navToggle" aria-label="Abrir menú">☰</button>
            <ul class="nav-links" id="navLinks">
{chr(10).join(items)}
                <li class="nav-cta"><a href="/#contacto" class="btn btn-gold">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>
                    Contacto</a></li>
            </ul>
        </div>
    </header>
'''


PIE = f'''    <!-- ============ CTA ============ -->
    <div class="band" id="contacto">
        <div class="band-grid">
            <div class="band-cta">
                <div class="inner">
                    <div class="reveal">
                        <h2 class="serif">Hablemos de tus decisiones,<br>hablemos de tu futuro.</h2>
                        <p>Agendemos una reunión y evaluemos juntos cómo la metodología I.D.E.A. puede fortalecer las
                            decisiones de tu empresa.</p>
                    </div>
                    <div class="actions reveal reveal-d1">
                        <a class="btn btn-gold" href="{WSP}?text=Hola,%20quisiera%20agendar%20una%20reuni%C3%B3n%20con%20Arriaza%20Consulting.">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>
                            Agendar reunión</a>
                        <a class="btn btn-ghost-dark" href="mailto:{CORREO}">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6L22 7"/></svg>
                            Escríbenos</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <div class="wrap foot-grid">
            <div class="foot-brand">
                <a href="/" class="brand">
                    {ISOTIPO}
                    <span>
                        <span class="brand-name">ARRIAZA</span>
                        <span class="brand-sub">Consulting</span>
                    </span>
                </a>
                <p>Estrategia Tributaria &amp; Control de Decisiones Empresariales</p>
                <div class="socials">
                    <a href="https://www.linkedin.com/in/regina-arriaza-624526264/" target="_blank" rel="noopener"
                        aria-label="LinkedIn de Regina Arriaza"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.2 8h4.6v14.8H.2V8zm7.6 0h4.4v2h.06c.62-1.16 2.12-2.4 4.36-2.4 4.66 0 5.52 3.07 5.52 7.06v8.14h-4.6v-7.2c0-1.72-.04-3.94-2.4-3.94-2.4 0-2.77 1.87-2.77 3.8v7.34H7.8V8z"/></svg></a>
                </div>
            </div>
            <div>
                <h4>Enlaces</h4>
                <ul>
                    <li><a href="/">Inicio</a></li>
                    <li><a href="/metodologia-idea">Metodología I.D.E.A.</a></li>
                    <li><a href="/servicios">Servicios</a></li>
                    <li><a href="/casos">Casos reales</a></li>
                    <li><a href="/sobre-regina-arriaza">Sobre mí</a></li>
                    <li><a href="/blog">Blog</a></li>
                </ul>
            </div>
            <div>
                <h4>Servicios</h4>
                <ul>
                    <li><a href="/servicios#estrategia-tributaria">Estrategia Tributaria</a></li>
                    <li><a href="/servicios#control-de-decisiones">Control de Decisiones</a></li>
                    <li><a href="/servicios#gestion-de-riesgos">Gestión de Riesgos</a></li>
                    <li><a href="/servicios#fiscalizaciones">Fiscalizaciones y Defensa</a></li>
                    <li><a href="/servicios#reportes">Reportes y Análisis</a></li>
                    <li><a href="/servicios#asesoria-corporativa">Asesoría Corporativa</a></li>
                </ul>
            </div>
            <div>
                <h4>Contacto</h4>
                <ul class="foot-contact" style="display:grid;gap:13px;">
                    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 01-2.2 2A19.8 19.8 0 012 4.2 2 2 0 014 2h3.1a2 2 0 012 1.7c.13.96.36 1.9.7 2.8a2 2 0 01-.45 2.1L8.1 9.9a16 16 0 006 6l1.3-1.25a2 2 0 012.1-.45c.9.34 1.84.57 2.8.7a2 2 0 011.7 2z"/></svg>
                        <a href="tel:+56961886452">{TEL_HUMANO}</a></li>
                    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6L22 7"/></svg>
                        <a href="mailto:{CORREO}">{CORREO}</a></li>
                    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-7-5.3-7-11a7 7 0 1114 0c0 5.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>
                        Santiago de Chile</li>
                </ul>
            </div>
            <div class="foot-quote-col">
                <span class="qmark">“</span>
                <p>La información por sí sola no genera valor. La comprensión y el criterio transforman decisiones en
                    resultados sostenibles.</p>
                <div class="ra">RA</div>
            </div>
        </div>
        <div class="foot-bottom wrap">
            © 2026 Arriaza Consulting. Todos los derechos reservados. ·
            <a href="/politica-privacidad">Política de privacidad</a> · <a href="/terminos">Términos</a>
        </div>
    </footer>

    <div class="floaters">
        <a class="f-phone" href="tel:+56961886452" aria-label="Llamar">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 01-2.2 2A19.8 19.8 0 012 4.2 2 2 0 014 2h3.1a2 2 0 012 1.7c.13.96.36 1.9.7 2.8a2 2 0 01-.45 2.1L8.1 9.9a16 16 0 006 6l1.3-1.25a2 2 0 012.1-.45c.9.34 1.84.57 2.8.7a2 2 0 011.7 2z"/></svg>
        </a>
        <a class="f-wsp" href="{WSP}?text=Hola,%20necesito%20asesor%C3%ADa%20para%20mi%20empresa." aria-label="WhatsApp">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2a9.9 9.9 0 00-8.5 15L2 22l5.15-1.5A9.94 9.94 0 1012.04 2zm5.8 14.1c-.24.68-1.4 1.3-1.94 1.35-.5.05-1.13.24-3.8-.8-3.2-1.26-5.24-4.53-5.4-4.74-.16-.21-1.3-1.73-1.3-3.3 0-1.57.83-2.34 1.12-2.66.3-.32.64-.4.85-.4h.61c.2 0 .46-.07.72.55.27.64.9 2.2.98 2.36.08.16.13.35.03.56-.1.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.34-.14.66.19.32.83 1.37 1.78 2.22 1.22 1.09 2.25 1.43 2.57 1.59.32.16.5.13.69-.08.19-.21.79-.92 1-1.24.21-.32.42-.26.7-.16.29.11 1.85.87 2.17 1.03.32.16.53.24.61.37.08.14.08.78-.16 1.44z"/></svg>
        </a>
    </div>

    <script src="/assets/sitio.js" defer></script>
</body>

</html>
'''


def pagina(slug, titulo, descripcion, activo, cuerpo, schema=None, migas=None):
    """Arma una página completa. slug '' = raíz."""
    url = f"{SITIO}/{slug}" if slug else f"{SITIO}/"
    schema_html = ""
    bloques = []
    if migas:
        items = [{"@type": "ListItem", "position": i + 1, "name": n,
                  "item": f"{SITIO}{u}"} for i, (u, n) in enumerate(migas)]
        bloques.append({"@context": "https://schema.org", "@type": "BreadcrumbList",
                        "itemListElement": items})
    if schema:
        bloques.append(schema)
    if bloques:
        import json
        schema_html = "\n".join(
            f'    <script type="application/ld+json">\n{json.dumps(b, ensure_ascii=False, indent=2)}\n    </script>'
            for b in bloques)

    migas_html = ""
    if migas:
        partes = []
        for i, (u, n) in enumerate(migas):
            if i == len(migas) - 1:
                partes.append(f'<span aria-current="page">{html.escape(n)}</span>')
            else:
                partes.append(f'<a href="{u}">{html.escape(n)}</a>')
        migas_html = ('    <nav class="migas" aria-label="Ruta">\n        <div class="wrap">'
                      + ' <span class="sep">›</span> '.join(partes) + '</div>\n    </nav>\n')

    return f'''<!DOCTYPE html>
<html lang="es" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(titulo)}</title>
    <meta name="description" content="{html.escape(descripcion)}">
    <link rel="canonical" href="{url}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html.escape(titulo)}">
    <meta property="og:description" content="{html.escape(descripcion)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITIO}/og.jpg">
    <meta property="og:site_name" content="Arriaza Consulting">
    <meta property="og:locale" content="es_CL">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(titulo)}">
    <meta name="twitter:description" content="{html.escape(descripcion)}">
    <meta name="twitter:image" content="{SITIO}/og.jpg">
    <link rel="icon"
        href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='8' fill='%230A101F'/%3E%3Cpath d='M31.5 14 17 50h7.6l9.2-24.4L38 38l-3.4 3.6L37 50h9L31.5 14Z' fill='%23C5A059'/%3E%3Cpath d='M40.4 20.6 47 50h-6.2l-4-18.6 3.6-10.8Z' fill='%23C5A059'/%3E%3C/svg%3E">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Archivo:wght@400;500;600;700&family=Allura&display=swap"
        rel="stylesheet">
{schema_html}
    <link rel="stylesheet" href="/assets/estilos.css">
</head>

<body>

{cabecera(activo)}
{migas_html}{cuerpo}
{PIE}'''


# ---------------------------------------------------------------- contenidos

SERVICIOS = [
    ("estrategia-tributaria", "Estrategia Tributaria",
     "Planificación fiscal eficiente y cumplimiento normativo para optimizar resultados con fundamentos sólidos.",
     ['Diseñamos la estrategia tributaria de la empresa mirando el negocio completo, no solo la declaración de '
      'impuestos. El objetivo es que cada decisión quede correctamente sustentada desde el día uno.',
      'Trabajamos la planificación fiscal, el cumplimiento normativo y la coherencia entre la contabilidad, la '
      'información financiera y los registros tributarios.']),
    ("control-de-decisiones", "Control de Decisiones Empresariales",
     "Información financiera y tributaria integrada para apoyar cada decisión estratégica de la empresa.",
     ['Integramos la información financiera, tributaria y operativa para que el dueño o la gerencia puedan ver el '
      'impacto completo de una decisión antes de tomarla.',
      'Es el corazón de nuestra metodología I.D.E.A.: no analizamos áreas por separado, analizamos decisiones.']),
    ("gestion-de-riesgos", "Gestión de Riesgos",
     "Identificamos, evaluamos y mitigamos los riesgos tributarios y financieros antes de que afecten a la empresa.",
     ['Identificamos los riesgos tributarios y financieros de las operaciones relevantes, los evaluamos y proponemos '
      'cómo mitigarlos antes de que se conviertan en una contingencia.',
      'Un riesgo frecuente no nace de una mala decisión, sino de perder la capacidad de acreditar y respaldar '
      'técnicamente una operación con el paso del tiempo.']),
    ("fiscalizaciones", "Fiscalizaciones y Defensa ante el SII",
     "Acompañamiento integral ante procesos de fiscalización del Servicio de Impuestos Internos.",
     ['Acompañamos a la empresa durante todo el proceso de fiscalización: revisión de los antecedentes, '
      'reconstrucción de las operaciones cuestionadas y elaboración de la respuesta técnica.',
      'El trabajo consiste en sustentar la realidad económica de cada operación con evidencia contable, financiera, '
      'bancaria y tributaria.']),
    ("reportes", "Reportes y Análisis",
     "Reportes a medida para monitorear, proyectar y tomar decisiones con mayor confianza.",
     ['Construimos reportes hechos a la medida del negocio, para monitorear lo que realmente importa y proyectar '
      'escenarios antes de comprometer recursos.',
      'La información sirve cuando permite decidir: por eso el reporte se diseña a partir de las decisiones que la '
      'empresa necesita tomar.']),
    ("asesoria-corporativa", "Asesoría Corporativa",
     "Soluciones integrales para estructuración societaria, inversión y operaciones especiales.",
     ['Asesoramos en estructuración societaria, inversiones y operaciones especiales, cuidando que la estructura '
      'responda a una finalidad económica real y pueda sostenerse en el tiempo.',
      'Una reorganización no se sostiene solo porque esté bien redactada: también debe poder demostrar por qué '
      'responde a necesidades del negocio.']),
]

PASOS_IDEA = [
    ("I", "Interpretar", "Comprender el negocio, su contexto y lo que realmente está en juego detrás de cada decisión.",
     'Antes de analizar cifras, entendemos el negocio: qué hace la empresa, cómo genera valor y qué se está '
     'decidiendo realmente. Sin ese contexto, cualquier análisis queda incompleto.'),
    ("D", "Diagnosticar", "Identificar riesgos y oportunidades en lo financiero, tributario, operativo y legal.",
     'Revisamos la decisión desde todas las dimensiones relevantes a la vez, porque una decisión financiera puede '
     'modificar la carga tributaria y una operativa puede incrementar un riesgo legal.'),
    ("E", "Evaluar", "Desarrollar soluciones sostenibles, con fundamentos que se sostengan incluso años después.",
     'Evaluamos las alternativas y proponemos la que mejor equilibra impacto y respaldo técnico, pensando en que '
     'deberá sostenerse incluso años después de ejecutada.'),
    ("A", "Acompañar", "Respaldar la implementación y defender cada decisión ante fiscalizaciones y revisiones.",
     'Acompañamos la implementación y respaldamos la decisión frente a fiscalizaciones o revisiones posteriores, '
     'con la documentación y el sustento técnico correspondiente.'),
]



# Encabezados que Regina usa en sus casos. Lista explícita: adivinar por largo
# convertía en título frases que eran parte del texto.
ENCABEZADOS = {"El desafío", "Nuestro enfoque", "El resultado", "Nuestra conclusión",
               "Lo que aprendimos", "Nuestra forma de trabajar"}


def _formatear(lineas):
    """Convierte el texto de la clienta en HTML respetando encabezados y listas."""
    partes, lista = [], []

    def cerrar_lista():
        if lista:
            items = "".join(f'<li>{html.escape(x)}</li>' for x in lista)
            partes.append(f'<ul class="lista-caso">{items}</ul>')
            lista.clear()

    esperando_items = False
    for linea in lineas:
        limpia = linea.strip()
        if not limpia:
            continue
        if limpia in ENCABEZADOS:
            cerrar_lista()
            esperando_items = False
            partes.append(f'<h2>{html.escape(limpia)}</h2>')
        elif limpia.startswith("Confidencialidad:"):
            cerrar_lista()
            esperando_items = False
            partes.append(f'<p class="nota-confid">{html.escape(limpia)}</p>')
        elif limpia.endswith(":"):
            cerrar_lista()
            esperando_items = True
            partes.append(f'<p class="intro-lista">{html.escape(limpia)}</p>')
        elif esperando_items and len(limpia) < 90:
            lista.append(limpia.rstrip("."))
        else:
            cerrar_lista()
            esperando_items = False
            partes.append(p(limpia))
    cerrar_lista()
    return partes


def leer_casos():
    """Saca los 3 casos en versión web del documento de la clienta."""
    ruta = os.path.join(RAIZ, "docs", "casos-reales-cliente.md")
    txt = open(ruta, encoding="utf-8").read()
    bloques = re.split(r'\n## Caso \d+\n', txt)[1:]
    por_titulo = {}
    for b in bloques:
        lineas = [l.strip() for l in b.strip().split('\n') if l.strip()]
        por_titulo[lineas[0].rstrip('.')] = lineas
    return por_titulo


# Los casos van SIN imagen por pedido de la clienta (WhatsApp 05-08-2026): las piezas
# gráficas competían con el texto, que es lo que ella quiere que se lea.
CASOS_META = [
    ("fiscalizacion-sii-otros-activos",
     "Cuando el verdadero riesgo no estaba en el impuesto",
     "Caso real: una fiscalización del SII sobre una partida en «Otros Activos» y cómo se acreditó su naturaleza económica.",
     "Fiscalización SII", None),
    ("decisiones-que-explican-los-resultados",
     "Cuando el problema no estaba en los números",
     "Caso real: una empresa con rentabilidad a la baja donde el origen no estaba en las cifras, sino en decisiones analizadas por separado.",
     "Control de decisiones", None),
    ("reorganizacion-empresarial-razon-de-negocios",
     "Una reorganización empresarial no siempre fracasa por su estructura",
     "Caso real: una reorganización societaria correctamente estructurada que no podía acreditar su legítima razón de negocios.",
     "Reorganización societaria", None),
]


# ---------------------------------------------------------------- páginas

def p(txt):
    return f'<p>{html.escape(txt)}</p>'


def escribir(ruta_rel, contenido):
    destino = os.path.join(RAIZ, ruta_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, "w", encoding="utf-8").write(contenido)
    print(f"  ✓ {ruta_rel}  ({len(contenido)//1024} KB)")


def hero_interno(kicker, titulo, bajada):
    return f'''    <section class="hero-interno">
        <div class="wrap">
            <span class="hero-kicker">{html.escape(kicker)}</span>
            <h1>{titulo}</h1>
            <p class="bajada">{html.escape(bajada)}</p>
        </div>
    </section>
'''


def gen_metodologia():
    pasos = "\n".join(f'''                <article class="paso reveal">
                    <div class="letra">{l}</div>
                    <div>
                        <h2>{n}</h2>
                        <p class="resumen">{html.escape(res)}</p>
                        <p>{html.escape(det)}</p>
                    </div>
                </article>''' for l, n, res, det in PASOS_IDEA)
    cuerpo = hero_interno("Nuestra metodología",
                          'Metodología <span class="gold">I.D.E.A.</span>',
                          "Inteligencia para las Decisiones Empresariales Aplicadas: comprender el impacto completo "
                          "de cada decisión antes de ejecutarla.") + f'''
    <section class="contenido">
        <div class="wrap prosa">
            <p class="destacado">Las contingencias empresariales rara vez nacen por falta de información. Nacen
                cuando una decisión se analiza desde una sola perspectiva.</p>
            <p>Las empresas toman cientos de decisiones cada año y todas tienen algo en común: generan consecuencias
                que rara vez pertenecen a una sola área. Una decisión financiera puede modificar la carga tributaria;
                una decisión tributaria puede afectar la caja; una decisión operativa puede incrementar un riesgo
                legal.</p>
            <p>I.D.E.A. integra el análisis financiero, tributario, operativo, legal y estratégico en cuatro pasos.
                No fue creada para producir más información: fue creada para generar mejores decisiones.</p>
        </div>
        <div class="wrap pasos">
{pasos}
        </div>
        <div class="wrap prosa">
            <h2>Qué cambia con este enfoque</h2>
            <p>Cuando una decisión se evalúa de forma integrada, la empresa no solo resuelve el problema de hoy:
                queda en condiciones de explicar y sostener esa decisión años después, que es justamente cuando suele
                llegar la revisión.</p>
            <p>Puedes ver cómo se aplica en <a href="/casos">casos reales</a> o revisar
                <a href="/servicios">nuestros servicios</a>.</p>
        </div>
    </section>
'''
    escribir("metodologia-idea.html", pagina(
        "metodologia-idea", "Metodología I.D.E.A. | Arriaza Consulting",
        "I.D.E.A. (Inteligencia para las Decisiones Empresariales Aplicadas): metodología que integra el análisis "
        "financiero, tributario, operativo y estratégico antes de ejecutar una decisión.",
        "/metodologia-idea", cuerpo,
        migas=[("/", "Inicio"), ("/metodologia-idea", "Metodología I.D.E.A.")]))


def gen_servicios():
    bloques = []
    for slug, nombre, resumen, parrafos in SERVICIOS:
        cuerpo_p = "\n                    ".join(p(x) for x in parrafos)
        bloques.append(f'''            <article class="servicio-detalle reveal" id="{slug}">
                <h2>{html.escape(nombre)}</h2>
                <p class="resumen">{html.escape(resumen)}</p>
                <div class="prosa-corta">
                    {cuerpo_p}
                </div>
                <a class="btn btn-ghost-dark" href="{WSP}?text=Hola,%20quisiera%20consultar%20por%20{nombre.replace(' ', '%20')}.">
                    Consultar por este servicio {FLECHA}</a>
            </article>''')
    schema = {"@context": "https://schema.org", "@type": "ItemList",
              "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                   "item": {"@type": "Service", "name": n,
                                            "description": r,
                                            "provider": {"@type": "ProfessionalService", "name": "Arriaza Consulting"},
                                            "areaServed": "Chile",
                                            "url": f"{SITIO}/servicios#{s}"}}
                                  for i, (s, n, r, _) in enumerate(SERVICIOS)]}
    cuerpo = hero_interno("Soluciones",
                          "Nuestros servicios",
                          "Asesoría tributaria, financiera y estratégica para empresas y empresarios en Chile.") + f'''
    <section class="contenido">
        <div class="wrap servicios-lista">
{chr(10).join(bloques)}
        </div>
    </section>
'''
    escribir("servicios.html", pagina(
        "servicios", "Servicios | Asesoría Tributaria y Estratégica — Arriaza Consulting",
        "Estrategia tributaria, control de decisiones, gestión de riesgos, defensa ante fiscalizaciones del SII, "
        "reportes y asesoría corporativa para empresas en Chile.",
        "/servicios", cuerpo, schema=schema,
        migas=[("/", "Inicio"), ("/servicios", "Servicios")]))


def gen_casos():
    casos = leer_casos()
    fichas = []
    for slug, titulo, desc, etiqueta, imagen in CASOS_META:
        lineas = casos.get(titulo)
        if not lineas:
            print(f"  ! sin texto para: {titulo}")
            continue
        # el primer elemento es el título; el resto, el cuerpo tal como lo escribió la clienta
        cuerpo_txt = lineas[1:]
        partes = _formatear(cuerpo_txt)
        img_html = (f'<img class="caso-img" src="/{imagen}" alt="{html.escape(titulo)}" loading="lazy">'
                    if imagen else '')
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": titulo, "description": desc,
                  "inLanguage": "es-CL",
                  "author": {"@type": "Person", "name": "Regina Pastora Arriaza Benítez"},
                  "publisher": {"@type": "Organization", "name": "Arriaza Consulting"},
                  "mainEntityOfPage": f"{SITIO}/casos/{slug}"}
        cuerpo = hero_interno(etiqueta, html.escape(titulo),
                              "Caso real adaptado para resguardar la identidad del cliente.") + f'''
    <section class="contenido">
        <div class="wrap prosa">
            {img_html}
            {chr(10).join('            ' + x for x in partes).strip()}
            <p class="volver"><a href="/casos">{FLECHA} Ver todos los casos</a></p>
        </div>
    </section>
'''
        escribir(f"casos/{slug}.html", pagina(
            f"casos/{slug}", f"{titulo} | Casos — Arriaza Consulting", desc,
            "/casos", cuerpo, schema=schema,
            migas=[("/", "Inicio"), ("/casos", "Casos"), (f"/casos/{slug}", etiqueta)]))
        fichas.append(f'''            <article class="ficha-caso reveal">
                <span class="etiqueta">{html.escape(etiqueta)}</span>
                <h2><a href="/casos/{slug}">{html.escape(titulo)}</a></h2>
                <p>{html.escape(desc)}</p>
                <a class="leer" href="/casos/{slug}">Leer el caso {FLECHA}</a>
            </article>''')

    cuerpo = hero_interno("Experiencia aplicada", "Casos reales",
                          "Situaciones reales de fiscalización, reorganización y decisiones empresariales. "
                          "Todos los casos fueron adaptados para resguardar la identidad del cliente.") + f'''
    <section class="contenido">
        <div class="wrap casos-grid">
{chr(10).join(fichas)}
        </div>
    </section>
'''
    escribir("casos.html", pagina(
        "casos", "Casos reales | Fiscalizaciones y decisiones empresariales — Arriaza Consulting",
        "Casos reales de fiscalizaciones del SII, reorganizaciones societarias y control de decisiones "
        "empresariales, adaptados para resguardar la identidad del cliente.",
        "/casos", cuerpo,
        migas=[("/", "Inicio"), ("/casos", "Casos")]))


def gen_sobre():
    creds = ["Contadora Auditora", "Ingeniera en Control de Gestión", "Magíster en Tributación",
             "Diplomada en IFRS", "Diplomada en Comunicación Estratégica"]
    lista = "\n".join(f'                <li>{c}</li>' for c in creds)
    schema = {"@context": "https://schema.org", "@type": "Person",
              "name": "Regina Pastora Arriaza Benítez",
              "jobTitle": "Contadora Auditora, Ingeniera en Control de Gestión, Magíster en Tributación",
              "worksFor": {"@type": "Organization", "name": "Arriaza Consulting"},
              "url": f"{SITIO}/sobre-regina-arriaza",
              "sameAs": ["https://www.linkedin.com/in/regina-arriaza-624526264/"]}
    cuerpo = hero_interno("Liderazgo", "Regina Pastora Arriaza Benítez",
                          "Experiencia, criterio y compromiso con cada decisión.") + f'''
    <section class="contenido">
        <div class="wrap prosa">
            <h2>El pensamiento que dio origen a Arriaza Consulting</h2>
            <p>Durante años participé en procesos de planificación tributaria, análisis financiero y fiscalizaciones
                empresariales. Caso tras caso apareció el mismo patrón: las empresas contaban con información,
                profesionales y experiencia, pero las decisiones seguían analizándose por separado.</p>
            <p>Comprendí que el problema no era la falta de conocimiento, sino la falta de integración. Ese
                descubrimiento cambió mi forma de ejercer la profesión y dio origen a Arriaza Consulting.</p>

            <h2>Formación</h2>
            <ul class="creds-lista">
{lista}
            </ul>
            <p>Más allá de los títulos, mi propósito es ayudar a las empresas a tomar decisiones que puedan
                sostenerse con fundamentos sólidos, incluso años después de haber sido ejecutadas.</p>

            <h2>Nuestro compromiso</h2>
            <p>No aspiramos únicamente a resolver contingencias. Queremos ayudar a construir empresas que puedan
                tomar decisiones con mayor claridad, menor incertidumbre y una visión integral de sus consecuencias.
                Porque una buena decisión no solo debe resolver el problema de hoy: debe proteger el futuro de la
                empresa.</p>
            <p class="firma-prosa">Regina Arriaza</p>
            <p>Conoce la <a href="/metodologia-idea">metodología I.D.E.A.</a> o revisa
                <a href="/casos">casos reales</a>.</p>
        </div>
    </section>
'''
    escribir("sobre-regina-arriaza.html", pagina(
        "sobre-regina-arriaza", "Regina Pastora Arriaza Benítez | Arriaza Consulting",
        "Contadora Auditora, Ingeniera en Control de Gestión y Magíster en Tributación. Fundadora de Arriaza "
        "Consulting y creadora de la metodología I.D.E.A.",
        "/sobre-regina-arriaza", cuerpo, schema=schema,
        migas=[("/", "Inicio"), ("/sobre-regina-arriaza", "Sobre mí")]))


if __name__ == "__main__":
    print("Generando páginas hijas:")
    gen_metodologia()
    gen_servicios()
    gen_casos()
    gen_sobre()
    print("Listo.")
