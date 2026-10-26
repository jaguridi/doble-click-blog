---
layout: lectura
numero: 28
tags: [gobernanza, latam, ética]
title: "Eticas cuenta menos de veinte auditorías de IA en el Sur Global"
description: "Galdon Clavell y Magaard sostienen que la brecha de evaluación es de financiamiento, no de capacidad, y proponen que los financiadores exijan evaluaciones independientes y su publicación."
date: 2026-10-26
paper_titulo: "Open Veins of Algorithmic Auditing: Why AI Assessment Lags Behind Its Deployment in the Global South"
paper_autores: "Galdon Clavell y Magaard"
paper_publicado: "arXiv (preprint, Eticas Foundation), 2026"
paper_doi: "https://arxiv.org/abs/2607.21317"
paper_archivo: "cola-01-open-veins-algorithmic-auditing.pdf"
paper_keywords: "algorithmic auditing, AI evaluation, Global South, AI governance, accountability, algorithmic impact assessment"
audio: true
---

## La ficha

- **Qué es:** *Open Veins of Algorithmic Auditing: Why AI Assessment Lags Behind Its Deployment in the Global South*. La portada del PDF lo titula *Open Veins of AI Auditing*.
- **Quiénes:** [Gemma Galdon Clavell](https://scholar.google.com/scholar?q=%22Gemma+Galdon+Clavell%22) y [Alexandra Magaard](https://scholar.google.com/scholar?q=%22Alexandra+Magaard%22). Es una publicación de Eticas Foundation, el brazo sin fines de lucro de Eticas.
- **Dónde:** [arXiv](https://arxiv.org/abs/2607.21317), 23 de julio de 2026, de acceso abierto. Los autores lo presentan como borrador previo a futuras publicaciones, sin revisión por pares.
- **Tipo:** artículo de posición apoyado en la práctica de la propia organización: una auditoría publicada, dos inéditas, evaluaciones rápidas durante la pandemia, trece evaluaciones en África subsahariana y Asia Pacífico, y un estudio regional para el PNUD.

## Primera lectura: qué hace y qué encuentra

Galdon Clavell y Magaard empiezan por contar. Definen auditoría en sentido estricto: una evaluación independiente de un sistema concreto, ya desplegado o por desplegarse, que deja hallazgos documentados. Con esa vara revisan una década de trabajo publicado en África, América Latina, el Caribe y el sur y sudeste de Asia. Cuentan menos de veinte auditorías y evaluaciones hechas por alguien distinto del desarrollador. Con el criterio más estricto quedan entre diez y quince. En África subsahariana, el sudeste asiático y el Caribe, su equipo no encontró ninguna auditoría completa publicada.

La parte más concreta es una auditoría que Eticas entregó en marzo de 2020 y que nunca se publicó. Evaluó un sistema nacional de alerta de riesgo infantil en un país del Cono Sur, sin identificar por confidencialidad:

- el modelo puntúa a 3,9 millones de niños con 280 variables tomadas de siete registros administrativos;
- el evento que predice ocurre en unos 3 de cada 1.000 niños;
- la métrica que se comunicaba, un área bajo la curva ROC de 0,94, mide qué tan bien el modelo ordena a todos los niños por riesgo y se acerca a 1 cuanto mejor los ordena;
- en el umbral que dispara las alertas, el modelo detectaba el 73% de los casos, de modo que cerca de uno de cada cuatro niños separados de su familia había sido clasificado sin riesgo.

Con un evento tan raro, explica el paper, la primera métrica se infla porque el modelo ordena bien a la gran mayoría que nunca estuvo en riesgo, y no dice nada del punto de corte que se usa. La auditoría encontró además que la variable predicha, el ingreso a un programa con separación familiar, se eligió por ser la más fácil de predecir. Los niños indígenas recibían más riesgo predicho aunque esa condición se había excluido del modelo.

El segundo caso es Robot Laura, un sistema brasileño que anticipa el deterioro de pacientes hospitalizados. Su auditoría, encargada por el BID y publicada en 2021, halló que el sistema sobrestima a propósito la mortalidad y subestima con más frecuencia el riesgo de mujeres jóvenes.

De estos casos y de las trece evaluaciones, el texto extrae cuatro patrones y cinco lecciones. La tesis es que la brecha es de financiamiento: cada evaluación de su registro existió porque un banco de desarrollo, una agencia o un programa de la ONU decidió pagarla, y ninguna por obligación legal.

El paper sostiene que, en cada sistema que su equipo examinó, aparecieron problemas que la institución usuaria no había detectado. Cuán extendidos están esos problemas, el paper no lo mide.

## Segunda lectura: desde América Latina

Las tres auditorías del paper son de sistemas latinoamericanos, y la comparación entre dos de ellas es su argumento central. Según el texto, la auditoría que un financiador decidió publicar informó a quien usaba el sistema y a un programa regional; la que quedó a criterio de la institución contratante no informó a nadie, pese a ser la más alarmante.

A juicio del blog, el primer lugar donde poner a prueba esa idea es el BID. El paper le atribuye el encargo de la auditoría de Robot Laura, dentro de su iniciativa fAIr LAC, y la adopción de una evaluación ética de 2020 como herramienta interna permanente. Si esa herramienta exigiera por contrato la publicación de las auditorías, la decisión de publicar saldría de manos de la institución auditada, que es justo el punto donde se perdió el caso infantil. El paper afirma que, hasta donde saben sus firmantes, ninguno de los cerca de doce financiadores que concentran el dinero para IA en desarrollo exige hoy como condición una evaluación independiente.

Brasil ofrece la segunda prueba, esta vez presupuestaria. Según el paper, de los cerca de 4.250 millones de dólares que el Plan Brasileño de Inteligencia Artificial compromete hasta 2028, menos del medio por ciento va a supervisión y gobernanza. A juicio del blog, el tamaño de esa línea fijaría cuántas auditorías como la de Robot Laura podría pagar el propio Estado, sin esperar a un financiador externo.

En Chile, el paper registra que el GobLab de la Universidad Adolfo Ibáñez mantiene un repositorio público de algoritmos estatales y que ha evaluado más de una docena de modelos, publicados como resúmenes de caso y no como auditorías. Contar cuántos algoritmos del repositorio tienen alguna evaluación publicada, y de qué profundidad, daría para un país la cifra que el paper estima para todo el Sur Global.

El argumento de la publicación descansa en dos casos de la misma organización. Antes de convertirlo en regla, la región necesitaría saber cuántas auditorías se encargaron y nunca vieron la luz.

## La letra chica

- Conflicto de interés: el brazo comercial de Eticas vende auditorías, y el paper pide que los financiadores paguen evaluaciones independientes. La propia publicación declara que quien firma en primer lugar preside la International Association of Algorithmic Auditors. Es evidencia interna de un actor del mercado.
- La auditoría infantil sigue inédita y anonimizada: sus cifras no se pueden contrastar con el informe original.
- El conteo de auditorías se presenta como "to our knowledge" y depende de criterios de inclusión; el paper no describe cómo se hizo la búsqueda.
- Transparencia: el paper analiza críticamente una alianza entre Anthropic, que desarrolla Claude, el modelo que escribe esta sección, y la Fundación Gates.
- Los casos auditados son los que alguien decidió financiar. Sirven para mostrar que evaluar es posible y encuentra fallas, no para estimar con qué frecuencia fallan los sistemas de la región.
