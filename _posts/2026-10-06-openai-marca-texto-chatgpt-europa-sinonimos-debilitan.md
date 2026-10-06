---
layout: post
title: "OpenAI marca el texto de ChatGPT en Europa; los sinónimos la debilitan"
description: "Con 10% de palabras cambiadas, la detección baja de cerca de 92% a 66%, según pruebas de OpenAI citadas por BleepingComputer. Al comienzo, el detector será solo para investigadores."
date: 2026-10-06 09:11:08 -0300
tags: [ética, lanzamientos, latam]
audio: true
fuentes:
  - nombre: "OpenAI"
    fecha: "2026-10-05"
    url: "https://openai.com/index/eu-text-provenance"
    tipo: empresarial
    nivel: 4
  - nombre: "TechCrunch"
    fecha: "2026-10-05"
    url: "https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/"
    tipo: prensa
    nivel: 3
  - nombre: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/artificial-intelligence/openai-is-adding-invisible-watermarks-to-chatgpt-and-codex-text-in-the-eu/"
    tipo: prensa
    nivel: 3
  - nombre: "Convergência Digital"
    fecha: "2026-10-02"
    url: "https://convergenciadigital.com.br/inovacao/tribunal-de-justica-do-rio-grande-do-sul-cria-agentes-ia-proprios-para-reduzir-custo-dos-tokens/"
    tipo: prensa
    nivel: 3
---

## En 60 segundos

- **Qué pasó.** OpenAI anunció que pondrá una marca invisible en los textos que ChatGPT y Codex generen para usuarios de la Unión Europea, en las próximas semanas.
- **Por qué importa.** Quien use el detector para juzgar un trabajo o una prueba recibirá una probabilidad que una edición menor del texto puede cambiar bastante.
- **Qué falta saber.** Cuándo y en qué condiciones podrán usar el detector universidades, tribunales o empleadores, y si habrá evaluaciones independientes de su precisión.

El sistema se llama textGrain y funciona ajustando la elección de palabras del modelo. Así deja un patrón que un detector puede reconocer, aunque el lector no lo note, según [la publicación de OpenAI](https://openai.com/index/eu-text-provenance) del 5 de octubre. Llegará a todos los planes en la Unión Europea. En la interfaz de programación, que usan los desarrolladores para construir sus propios productos, la marca es opcional en todo el mundo y viene desactivada, según [TechCrunch](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/). El medio la vincula a las reglas de transparencia del AI Act, la ley europea de IA, vigentes desde el 2 de agosto.

Las cifras de desempeño vienen de pruebas de la propia empresa, sin evaluación independiente. En ellas, la detección cae de cerca de 92% a 66% si se cambia 10% de las palabras por sinónimos, y a 17% si se cambia 25%, según [BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/openai-is-adding-invisible-watermarks-to-chatgpt-and-codex-text-in-the-eu/).

Esas cifras sugieren un límite para quien quiera usar la marca como prueba. Una universidad que revise un ensayo, o un empleador que evalúe un informe, obtendría un resultado probabilístico, y una edición menor podría bajarlo mucho. Un resultado negativo, entonces, podría decir poco sobre el origen del texto. Fuera de Europa, además, el texto quedará marcado solo si el desarrollador de cada producto activa la opción. Anthropic ya había incorporado una marca similar en Claude, según [la entrada del 12 de agosto](https://dobleclick.jaguridi.cl/2026/08/12/anthropic-marca-texto-claude-no-prueba-autoria.html), con la advertencia de que indica procesamiento y no autoría.

## También hoy

- **[OpenAI pide disculpas ante el Parlamento australiano por el acceso de sus agentes a sitios del gobierno](https://citynewsqbn.com.au/2026/ai-giants-fly-in-as-safety-copyright-debates-heat-up/)**: Jason Kwon dijo en Sídney que la empresa debió responder mejor. Detectó en agosto un acceso de junio a un sitio de Medicare y avisó en septiembre, según la agencia AAP.
- **[OpenAI, Anthropic, Google y Meta declaran bajo juramento ante el Concejo de Nueva York](https://www.amny.com/news/ai-giants-nyc-council-whistleblower-warnings/)**: no se comprometieron a frenar lanzamientos que fallen una auditoría independiente, y xAI no se presentó pese a una citación, según amNY.
- **[Bain estima entre 5 y 6,5 billones de dólares para sumar cerca de 150 GW de centros de datos](https://www.bain.com/insights/ai-data-center-boom-can-we-build-it-if-they-come-technology-report-2026/)**: es la proyección hacia 2030 de su Technology Report 2026, publicado el 29 de septiembre.

## En la región

En Brasil, el Tribunal de Justicia de Rio Grande do Sul tiene en homologación agentes de IA propios, desarrollados con Amazon Web Services. Buscan bajar lo que paga por tokens, las unidades de texto con que se cobra el uso de un modelo. Su director de tecnología, Antônio Braz da Silva Neto, habló con [Convergência Digital](https://convergenciadigital.com.br/inovacao/tribunal-de-justica-do-rio-grande-do-sul-cria-agentes-ia-proprios-para-reduzir-custo-dos-tokens/). Según dijo, la herramienta Gaia procesará cerca de 1.500 de las 5.000 causas nuevas diarias y llegará a 350.000 abogados. El tribunal creó además una división que investiga el mal uso de IA en las peticiones y puede recomendar sanciones.

## Lanzamientos

- **[Beam](https://reflection.ai/blog/introducing-beam)**: modelo de Reflection con pesos abiertos, descargables para servidores propios. La empresa dice que iguala a GLM-5.2 en razonamiento con 3 a 4 veces menos cómputo, y publicará los pesos en octubre.

## Hilos que seguimos

El acceso de un agente de OpenAI a un portal de Medicare lo confirmó el gobierno australiano, según [la entrada del 25 de septiembre](https://dobleclick.jaguridi.cl/2026/09/25/empresas-ia-consejo-seguridad-onu.html). La comparecencia de Kwon en Sídney suma ahora una disculpa ante el Parlamento.
