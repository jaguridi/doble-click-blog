---
layout: lectura
numero: 34
tags: [agentes, gobernanza, latam]
title: "84 posibles casos de servicios públicos inundados por textos de IA"
description: "Schmitz, Hammond y Chan postulan que el fenómeno probablemente ya ocurre en muchos servicios, casi siempre vía texto generado, y que la respuesta más rápida, cobrar o poner trabas, suele restar acceso."
date: 2026-11-16
paper_titulo: "Characterizing Agentic Flooding of Government Services"
paper_autores: "Schmitz, Hammond y Chan"
paper_publicado: "arXiv (preprint), agosto de 2026; actas de AIES 2026"
paper_doi: "https://arxiv.org/abs/2608.16603"
paper_archivo: "cola-06-agentic-flooding-government.pdf"
paper_keywords: "inundación agéntica, servicios públicos, carga administrativa, agentes de IA, identidad digital"
audio: true
---

## La ficha

- **El paper:** *Characterizing Agentic Flooding of Government Services*.
- **Autores:** [Chris Schmitz](https://scholar.google.com/scholar?q=%22Chris+Schmitz%22), del Centre for Digital Governance de la Hertie School; [Lewis Hammond](https://scholar.google.com/scholar?q=%22Lewis+Hammond%22), de la Cooperative AI Foundation, y [Alan Chan](https://scholar.google.com/scholar?q=%22Alan+Chan%22), de GovAI.
- **Publicación:** [arXiv](https://arxiv.org/abs/2608.16603), de acceso abierto. La primera versión se subió el 17 de agosto de 2026 y la segunda, el 19. Según la portada, aparecerá en las actas de la 9.ª conferencia AIES de AAAI, celebrada en octubre de 2026. La base de casos está en [GitHub](https://github.com/CLSchmitz/flooding-dataset).
- **Método:** recopilación cualitativa de casos con un flujo asistido por modelos de lenguaje y revisión humana, más una matriz de riesgo y un mapa de respuestas construidos sobre precedentes y teoría.

## Primera lectura: qué hace y qué encuentra

En los tribunales sociales de Alemania, algunos escritos superaron las 4.000 páginas. Figura en una base que Schmitz, Hammond y Chan armaron para saber si los agentes de IA, al abaratar el trato con el Estado, ya provocan alzas de demanda que tensionan los servicios. Llaman a eso inundación agéntica (*agentic flooding*) y le exigen dos condiciones: que la causen agentes que interactúan con el servicio y que la tensión sea sustancial. Separan la inundación cuantitativa, más solicitudes, de la cualitativa, solicitudes más complejas.

El equipo revisó 13 dominios de gobierno en 12 países, entre ellos Brasil, el único de tradición administrativa latinoamericana. Un caso entraba solo con tres requisitos: un mecanismo plausible, evidencia de cambio en la demanda y una atribución explícita a la IA, hecha por el gobierno o por una fuente externa confiable. Las cifras de la base:

- 84 casos en 11 jurisdicciones;
- en 58 de ellos (69%), son funcionarios quienes afirman que la IA intervino;
- en 87%, el mecanismo es un modelo de lenguaje que redacta a bajo costo textos jurídicamente sofisticados;
- 60% se codifica como inundación cuantitativa y 90% como cualitativa;
- en 56% el gobierno respondió de forma explícita.

El patrón es casi uniforme: texto generado con IA, presentado por personas que hacen a mano el resto del trámite. Usos más sofisticados, como agentes que naveguen solos los portales, todavía no se ven en la base, según los autores. Los impactos observados son moderados, escriben, y un colapso operativo agudo les parece improbable.

Hacia adelante, a partir de los rasgos comunes de su base, el paper postula que el riesgo cercano parece mayor en servicios financieramente atractivos cuya demanda frenaba la complejidad del trámite, como los impuestos y los tribunales, y advierte que ese patrón puede reflejar también qué casos notan los funcionarios. Para evaluar cada servicio propone una matriz de trece factores. Después ordena las respuestas en dos estrategias, y según el precedente revisado ambas probablemente bastarían. Suprimir la demanda con cobros, citas presenciales o límites por persona es lo más rápido de aplicar. Pasó en 14 casos: Australia evaluó reponer cobros por solicitudes de acceso a la información y Japón bloqueó envíos por dirección IP en una consulta pública. El costo, advierten los autores, es que esa fricción disuade sobre todo a usuarios más pobres o con menos alfabetización digital. Aumentar la capacidad, rediseñando servicios o usando IA para procesar, podría evitar ese costo, pero exige tiempo e inversión, y un rediseño estructural puede tomar años.

La base sostiene algo más acotado que su tamaño: hay muchos episodios, en varios países, en que quienes administran un servicio atribuyen a la IA una carga nueva. Cuánta inundación hay y qué papel exacto cumplen los agentes queda fuera de su alcance, porque el método, aclaran ellos mismos, no admite afirmaciones causales ni cuantitativas.

## Segunda lectura: desde América Latina

El caso brasileño de la base es el auxílio-doença del INSS, el beneficio por incapacidad temporal. Los autores lo codifican como inundación cualitativa y lo usan como ejemplo de mala fe: personas que buscan el beneficio con certificados médicos generados con IA. También registran la respuesta, herramientas de IA para detectar esos certificados falsos.

A juicio de este blog, el caso reúne dos factores de la matriz a la vez. Es un pago en dinero, el tipo de servicio que el paper ve más expuesto, y su vía digital prescinde de un filtro que, según los autores, ningún agente atraviesa: la cita presencial. En abril de 2026, el [Ministerio de Previdência Social anunció](https://www.gov.br/previdencia/pt-br/noticias/2026/abril/atestados-medicos-de-ate-90-dias-nao-tem-mais-pericia-presencial) que los certificados médicos de hasta 90 días ya no pasan por pericia presencial. Si el patrón del caso brasileño se mantiene, esa ampliación cargaría más peso sobre la detección automática que el INSS ya adoptó. Para saberlo habría que comparar la proporción de certificados rechazados por falsos antes y después del cambio, un dato que el INSS podría publicar.

Chile ofrece un contraste por el lado legal. El paper advierte que algunas formas de fricción pueden estar prohibidas por ley y recomienda revisar qué respuestas permite la ley antes de una oleada. Para las solicitudes de acceso a la información, la [Ley 20.285](https://www.bcn.cl/leychile/navegar?idNorma=276363), en su texto vigente a noviembre de 2026, fija la gratuidad como principio (artículo 11, letra k) y su artículo 18 limita el cobro a los costos directos de reproducción. El atajo australiano de reponer cobros no estaría disponible sin reformar la ley. Ante un alza atribuida a la IA, quedarían las fricciones que no cobran, como el bloqueo por dirección IP que usó Japón o los límites por persona, y las respuestas lentas del mapa: rediseñar el canal o sumar capacidad. Si la ley chilena admite esas fricciones es la revisión legal que el paper recomienda hacer antes de una oleada.

Ninguna de las dos es un hallazgo del estudio, que no compara países. Son la matriz aplicada a dos servicios de la región, y su prueba depende de series de volumen que la mayoría de los casos de la base no trae.

## La letra chica

- Solo 25 casos tienen series de volumen, así que el paper descarta incluso afirmaciones correlativas. Algunas series de su figura 1 suben antes del lanzamiento de ChatGPT.
- Exigir atribución pública probablemente deja fuera casos reales y podría incluir otros mal atribuidos.
- El flujo usó Gemini 3.1 Pro Preview y Flash-Lite, con instrucciones en inglés y un costo cercano a 200 dólares. El revisor humano fue el primer autor; no hubo codificación entre evaluadores.
- Los países se eligieron porque informan públicamente sobre su administración, sin pretensión de representatividad.
- La matriz se apoya sobre todo en precedentes y teoría, más que en los datos, y falta validarla.
- Financiamiento: la Dieter Schwarz Foundation, vía la Hertie School; parte del trabajo se hizo en una beca de GovAI, la institución de Chan.
- El resultado alcanza para auditar servicios con una lista de factores. La magnitud del fenómeno sigue sin medirse.

<small>**Revisado el 16 de noviembre de 2026.** El riesgo de los servicios lucrativos y complejos se atribuye ahora al análisis de la base y no a la matriz, la vía de capacidad se dice como posible y no inmediata, y el párrafo sobre Chile ya no reduce las opciones a las respuestas lentas.</small>
