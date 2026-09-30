---
layout: page
title: Método
# El permalink NO cambia con el rótulo: /about/ está enlazado desde el pie de los
# formularios (#privacidad), desde otras páginas del sitio y desde fuera. El nombre
# visible es "Método"; la dirección se queda donde está.
permalink: /about/
# La usa _includes/seo.html para la meta description y el og:description de esta página.
description: "Qué son Doble Click y Doble Lectura, cómo se arma cada entrada con ayuda de IA y sin revisión humana previa, quién lo hace y cómo se usa tu correo si te suscribes."
---

**Doble Click** es un blog diario sobre inteligencia artificial con perspectiva latinoamericana. Cada día reunimos lo más relevante que ocurrió en IA (lanzamientos, investigación, gobernanza, movimientos de la industria) y lo contamos en una sola entrada, pensada para un público general informado, en español neutro.

Los lunes se suma **[Doble Lectura](/doble-lectura/)**: el análisis semanal de un paper o un informe de política pública, leído con calma. Primero qué dice el documento y después qué significa desde la región. Son dos cadencias de la misma cosa: el diario corre con la noticia y la lectura se detiene en un texto. Llegan juntas si te suscribes al newsletter.

El foco es **la región**: qué de todo esto importa para América Latina, qué oportunidades abre y qué conversaciones conviene tener.

## Cómo se hace {#como-se-hace}

Las entradas se generan de forma **automática** a partir de fuentes públicas (blogs oficiales de laboratorios, universidades, organismos multilaterales, prensa especializada y reguladores de la región) y enlazan siempre a la fuente original para poder profundizar.

## Qué fuentes revisamos

Miramos un conjunto amplio de fuentes, algunas cada día y otras en un barrido semanal: los **laboratorios de IA frontera**, **universidades y centros de investigación de América Latina**, **ministerios y reguladores** de la región, **organismos multilaterales** y estándares, equipos de **seguridad y evaluación** de modelos, **análisis e industria**, **prensa latinoamericana** e **investigación con curaduría**.

**[Ver la lista de fuentes →](/fuentes/)**

Esa lista es **representativa, no exhaustiva**: muestra a qué clase de fuente le prestamos atención y con ejemplos de cada categoría, pero la curaduría interna es más amplia y cambia con lo que va apareciendo. ¿Crees que falta alguna? **[Sugiérenos una fuente →](/fuentes/#sugerir)**: la revisamos y, si encaja, la sumamos.

## Una aclaración importante

Las entradas se publican **sin revisión humana previa**. Hacemos lo posible por ser precisos y enlazar siempre a la fuente, pero puede haber errores de interpretación o de resumen. Conviene tomar este blog como un punto de partida, no como una fuente definitiva: antes de citar una noticia o tomar decisiones a partir de ella, verifica en el enlace a la fuente original.

## Quién responde por esto {#responsable}

El proyecto lo mantiene **José Guridi**, investigador. Doble Click es un experimento personal de automatización editorial: no hay redacción, ni equipo, ni institución detrás.

**Qué es automático.** Prácticamente todo lo que ves: la curación de fuentes cada día, la redacción de las entradas y de las Doble Lectura (con Claude, los modelos de Anthropic), el audio de cada pieza (voz sintética) y el envío del newsletter. No hay una persona escribiendo ni aprobando cada texto antes de que salga.

**Qué supervisión hay.** Una revisión periódica, no previa a la publicación. Cada Doble Lectura pasa además por una segunda revisión automática, contra el documento original, antes de que salga el correo del lunes. Y los reportes que dejan los lectores se procesan cada noche: cuando un error se verifica, la página se corrige y queda una **fe de erratas al pie**, para que la corrección se vea y no se disimule.

**Cómo se corrige un error.** Al final de cada entrada y de cada lectura hay un formulario **"¿Viste un error?"**. Es la vía más rápida y la que deja registro: cuéntanos qué está mal, citando la frase si puedes, y, si la tienes, la fuente que lo corrige.

**Cómo contactar.** Para cualquier otra cosa (una fuente que falta, una consulta, una queja que no es una errata): [j.guridi.b@gmail.com](mailto:j.guridi.b@gmail.com).

## Newsletter

¿Prefieres recibirlo por correo? Te llega la entrada de cada mañana y, los lunes, la Doble Lectura: es una sola lista, te suscribes una vez y recibes las dos cosas. Antes de empezar te enviamos un único correo para confirmar, y la suscripción parte cuando haces clic en él.

<form class="sub-form" action="{{ site.newsletter_endpoint }}" method="post" target="sub-sink">
  <input class="sub-input" type="email" name="email" placeholder="tu@correo.com" required aria-label="Tu correo electrónico">
  <span class="sub-hp" aria-hidden="true"><input type="text" name="website" tabindex="-1" autocomplete="off"></span>
  <button class="sub-btn" type="submit">Suscribirme</button>
</form>
<iframe name="sub-sink" title="suscripción" style="display:none"></iframe>
<p class="sub-ok" role="status" aria-live="polite" hidden>Solicitud enviada. Si la dirección es válida, te llegará un correo para confirmar la suscripción. 📬</p>
<p class="sub-note">Solo usamos tu dirección para enviarte el newsletter y puedes darte de baja cuando quieras. <a href="{{ '/about/' | relative_url }}#privacidad">Cómo usamos tu correo →</a></p>

## Privacidad {#privacidad}

Tu correo se guarda en una **planilla privada de Google (Sheets)** que administra quien hace este blog. No hay nada más detrás: ni plataforma de marketing, ni perfilado, ni seguimiento de quién abre qué.

Lo usamos **exclusivamente** para enviarte el newsletter. No lo compartimos con nadie ni lo usamos para ninguna otra cosa.

Para darte de baja, al pie de cada correo hay un enlace **Darte de baja**: al hacer clic, tu dirección se elimina de la planilla. No hay que escribirle a nadie ni dar explicaciones.

**Estadísticas del sitio.** Las visitas se cuentan con [GoatCounter](https://www.goatcounter.com/), un contador de código abierto que no usa cookies ni guarda datos que identifiquen a quien lee. Además de las páginas vistas, suma algunos gestos: si alguien llegó al final de una entrada, le dio play al audio, abrió una fuente o envió un formulario. Nunca registra lo que escribes: ni tu correo, ni el texto de un reporte, ni lo que buscas en el archivo. Sirve para saber qué se lee y qué conviene mejorar, no quién lo lee.
