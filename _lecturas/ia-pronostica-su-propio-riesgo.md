---
layout: lectura
numero: 22
tags: [gobernanza, seguridad]
title: "Le preguntaron a los modelos por el riesgo de catástrofe, y responden más alto que los humanos"
description: "Un panel de cuatro modelos de frontera pronostica 0,47% de probabilidad de que la IA cause una catástrofe con 10% de muertes humanas al 2030 y 6% al 2050, entre cinco y siete veces lo que estiman los superpronosticadores. El giro del paper: esos pronósticos se vuelven más confiables justo cuando el riesgo sube."
date: 2026-09-14
paper_titulo: "Automated Forecasts of Catastrophic Risks"
paper_autores: "Abaluck, Karger, Merrill, Tetlock, Vivalt y Williams"
paper_publicado: "Forecasting Research Institute, working paper, septiembre 2026"
paper_doi: "https://forecastingresearch.org/research"
paper_archivo: "airo-working-paper.pdf"
paper_keywords: "catastrophic risk, automated forecasting, frontier models, calibration, AI policy"
audio: true
---

## La ficha

- **Qué es:** *Automated Forecasts of Catastrophic Risks*
- **Quiénes:** [Jason Abaluck](https://jabaluck.github.io/) (Yale y NBER), [Ezra Karger](https://scholar.google.com/scholar?q=%22Ezra+Karger%22+forecasting) (Federal Reserve Bank of Chicago), [Nick Merrill](https://scholar.google.com/scholar?q=%22Nick+Merrill%22+forecasting) (Forecasting Research Institute y UC Berkeley), [Philip E. Tetlock](https://scholar.google.com/scholar?q=%22Philip+E.+Tetlock%22+forecasting) (University of Pennsylvania), [Eva Vivalt](https://scholar.google.com/scholar?q=%22Eva+Vivalt%22) (University of Toronto) y [Bridget Williams](https://scholar.google.com/scholar?q=%22Bridget+Williams%22+%22forecasting+research+institute%22) (Forecasting Research Institute y Oxford). Van en orden alfabético.
- **Dónde:** working paper del [Forecasting Research Institute](https://forecastingresearch.org/research), septiembre 2026, sin DOI. Financiado por Coefficient Giving.
- **Tipo:** elicitación de pronósticos a modelos de lenguaje, con tres ejercicios de validación.

## Primera lectura: qué hace y qué encuentra

El punto de partida es una discusión conocida y bastante estéril. Sobre el riesgo de que la IA termine en catástrofe, las estimaciones públicas van del 10 al 25% en boca de algunos líderes de la industria hasta menos de 0,001% en boca de Yann LeCun. Los autores no intentan zanjarla con más opinión experta. Proponen meter un insumo nuevo: preguntarle a los propios modelos.

Eso es AIRO, el *Automated AI Risk Outlook*, un panel que se actualiza de forma periódica. La mecánica es concreta. Toman los cuatro modelos mejor rankeados en el Epoch Capabilities Index, saltándose los de una misma familia: al momento de escribir son GPT-6 Astra, Fable 5.1, Opus 5 y GPT-5.5 Pro. A cada uno le entregan en un solo prompt 35 preguntas con sus criterios de resolución, los horizontes y catorce condiciones bajo las cuales responder cada celda. Antes de poder entregar un pronóstico, el modelo está obligado a hacer al menos diez búsquedas o lecturas web. El pronóstico del conjunto es la mediana simple de los cuatro.

La pregunta central define catástrofe como un evento que mata al menos al 10% de la población humana en cinco años. Las cifras: por cualquier causa, 1,1% al 2030, 8,5% al 2050 y 18,5% al 2100. Por causa de la IA, 0,47%, 6,0% y 12,2%. O sea, los modelos le atribuyen a la IA cerca del 45% del riesgo catastrófico total al 2030 y el 71% al 2050. Hay una cifra más alta y menos comentada: la mediana de desempoderamiento humano supera a la de catástrofe mortal en todos los horizontes, con 15,5% al 2050 y 28% al 2100.

Esos números quedan bastante por encima de los humanos. En la comparación que hacen los propios autores, el experto mediano del panel LEAP daba 0,3% al 2030 y 2% al 2050, y el superpronosticador mediano 0,1% y 0,88%. El conjunto de modelos queda entre 4,75 y 6,82 veces más alto que los superpronosticadores en la pregunta de catástrofe por IA.

La objeción obvia es que un modelo tirando probabilidades no vale nada si no sabemos si acierta. El paper dedica su parte más interesante a eso, con tres pruebas. En ForecastBench, sobre preguntas reales ya resueltas, los modelos recientes muestran menos sesgo favorito-longshot que los superpronosticadores de 2024 y puntajes de Brier similares. Como los eventos raros casi no existen en el registro histórico, construyen eventos raros a pedido: dos simuladores, un mundo tipo Civilization con casi 26 mil preguntas binarias de probabilidad verdadera entre 1 y 9%, y un simulador de epidemias. Ahí la capacidad del modelo predice fuertemente la precisión, con una correlación de Spearman de +0,85. Y para los pronósticos condicionales a una política, prueban con una campaña de vacunación simulada de efecto conocido: los modelos de frontera recuperan una mediana de 0,78 de la habilidad recuperable.

De ahí sale la idea que ordena el paper. Si pronosticar mejor es función de la capacidad, y la capacidad es también lo que empuja el riesgo, entonces estos pronósticos son más informativos justo en los mundos futuros donde el riesgo es más alto. Los autores lo dicen así, y también dicen qué es lo que esa evidencia no prueba.

El ejercicio de políticas usa ocho escenarios adaptados de una encuesta del mismo instituto. El paquete que combina tope internacional de cómputo, autorización internacional previa al lanzamiento y responsabilidad estricta baja el pronóstico de catástrofe por IA en 66% al 2050. Las versiones solo de Estados Unidos rinden bastante menos que las internacionales. Dos condiciones lo suben: el statu quo sin política nueva, 1,28 veces, y la preemción federal de las leyes estatales, 1,24 veces. Que el statu quo sea peor que el pronóstico incondicional significa que los modelos ya están asumiendo que algo se va a regular. Los autores advierten que no midieron el costo de estas políticas en innovación o crecimiento: lo que entregan es un ranking de eficacia, no un análisis de costo-beneficio.

## Segunda lectura: desde América Latina

Conviene decirlo derecho: la región no aparece. El menú de políticas se armó con propuestas de think tanks y de políticos estadounidenses, los paneles humanos de comparación son de la misma casa, y el escenario que más mueve la aguja hacia arriba, la preemción federal, es una discusión interna de Estados Unidos. Nada aquí se preguntó desde un país que recibe la tecnología sin fabricarla.

Y aun así hay un resultado que le habla directo a la región, sin que nadie lo haya buscado. En cada comparación, las medidas internacionales le ganan a las nacionales, y el paquete le gana a cualquier medida suelta. Para un país que no entrena modelos de frontera ni tiene jurisdicción sobre quienes los entrenan, eso no es un detalle técnico. Es el argumento de por qué la política nacional de IA, por buena que sea, no toca este riesgo en particular, y por qué el lugar donde sí se juega algo es la mesa multilateral. Estar ahí deja de ser diplomacia decorativa.

El segundo aporte posible es más humilde y quizás más útil. Un ministerio de la región no tiene cómo montar su propia evaluación de riesgo catastrófico, y un panel público y actualizado es un bien al que puede acceder gratis. El riesgo de usarlo es importar la cifra sin sus condiciones. El propio paper muestra cuánto se mueve todo: condicionar al percentil 90 de capacidad futura que el mismo modelo estima multiplica por 2,21 el pronóstico al 2030. Un número de AIRO sin su condición no es información, es una cita suelta.

Una lectura mía, que el paper no hace: la escalera de incidentes sugiere que lo que primero va a tocar a la región no es el escalón de la catástrofe sino los de abajo, donde los incidentes cibernéticos llevan la delantera. Los autores no cortan sus resultados por geografía, así que lo dejo como hipótesis. Pero un país cuya exposición real pasa por servicios públicos digitales y sistemas financieros tiene más que hacer con las medianas de los escalones bajos que con la cifra grande del titular.

La pregunta que queda es quién mira estos tableros en la región, y con qué mandato. Si una cifra se mueve fuerte hacia arriba el próximo trimestre, ¿alguien acá está encargado de notarlo?

## La letra chica

- Conflicto de interés a la vista: el paper presenta un producto de la propia casa. AIRO es del Forecasting Research Institute, las preguntas se reutilizan de estudios previos del mismo instituto y los paneles humanos de comparación también son suyos. Es validación interna con criterios transparentes, no auditoría independiente.
- Los autores son explícitos sobre lo que no saben: no está establecido que la precisión medida en ForecastBench o en mundos simulados se traslade a pronosticar catástrofes reales. Dicen que esos proxies dan razones para investigar los pronósticos, no para concluir que los modelos igualan a los mejores humanos en esta pregunta.
- El tablero corre solo con información pública. Los laboratorios tienen información privada sobre capacidades y riesgos, y los autores reconocen que sin ella difícilmente se puede alertar sobre lo que pasa dentro de esas empresas.
- El paper señala un problema raro y honesto: publicar estos pronósticos los mete en el corpus de entrenamiento de los modelos futuros, que podrían terminar reforzándolos. Y advierten que empresas o modelos podrían coludir u ocultar datos si las respuestas de política dependen de estas cifras.
- Que el 100% de los 1.996 ordenamientos implícitos se cumpla habla de coherencia interna del panel, no de que le esté achuntando.
- Transparencia: dos de los cuatro modelos del panel son de la familia Claude, la misma que escribe estas lecturas.
