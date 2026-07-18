# 💡 Backlog de Ideas y Mejoras - Cuaderno FP

> **Última actualización:** 13 julio 2026  
> **Fuentes analizadas:** 49 documentos organizados en ``RF Ideas/referencia/`` (ver ``INDICE.md``)
> - Normativa: LO 3/2022, RD 659/2023, RD 69/2025, RD 532/2025, D 91/2024 Aragón, O ECD/1005/2018
> - Guía PD v1 (Javier Edo Gual, CIFPA), Curso PD JJ (8 módulos), Modelos UD/Tarea/Instrumento
> - CIFPA Cuaderno v10, Ejemplo PD IED 2024-25, PD completa IED, TFM RSP, Indicadores, Memoria
> - **3 niveles de PD:** PD- (minima), PD= (suficiente BOA/Aragon), PD+ (detallada) — ver ``referencia/50-PD-tres-niveles-sintesis.md``

---

## 1. 🎓 Cuaderno de Calificaciones y Aula (Prioridad Alta)

### 1.1 Evaluación por Indicadores (CIFPA v10)

> **Fuente:** CIFPA Cuaderno v10 Manual (27p), Guía PD v1 §4 (67p), Módulo 4 Curso JJ (3 partes)

- [ ] **[Fase 3]** **Matriz de Calificación Diaria:** Cuaderno tipo Excel de doble entrada (Alumnado vs. Indicadores) interactivo en la web para registrar notas ágilmente.
  - *CIFPA v10:* Hoja `INTRO_Calificaciones` — cada fila es un alumno, cada columna un indicador, con escala discreta/continua y conversión automática.
  - *Guía PD v1 §4.1:* Las actividades de evaluación generan evidencias que se recogen con técnicas e instrumentos. Cada instrumento produce una calificación que alimenta los CE.

- [ ] **[Fase 3]** **Módulo de Instrumentos e Indicadores:** Creación de Rúbricas o Listas de Control vinculadas a los CE.
  - *CIFPA v10:* Hoja `INTRO_Instrumentos` — define tipo (rúbrica, lista de control, escala valoración, prueba objetiva, registro observación, diario, etc.), escala (discreta/continua), agentes (heteroevaluación, coevaluación, autoevaluación), evaluación (parcial/final), peso por CE, campo Rec para recuperaciones.
  - *Guía PD v1 §4.1:* Instrumentos de evaluación vs instrumentos de calificación. Los primeros recogen evidencias, los segundos ponderan para nota.
  - *Modelo Instrumento:* Alineación curricular (vinculado a CE), claridad (verbos precisos, desempeños medibles), ponderación equilibrada, validez y fiabilidad, función formativa y retroalimentación.

- [ ] **[Fase 3]** **Cadena de trazabilidad completa:** Implementar la cascada **Indicador → CE → RA → Módulo** con ponderaciones en cada nivel.
  - *CIFPA v10:* Hoja `INTRO_Indicadores` — cada indicador tiene peso dentro del CE. Hoja `CONF_CE` — cada CE tiene peso dentro del RA. Hoja `CONF_RA` — cada RA tiene peso dentro del módulo.
  - *Módulo 2 Curso JJ:* Jerarquía: CPE → OG → RA → CE → Contenidos. Los RA son objeto directo de evaluación y calificación. Los CE son descriptores observables y evaluables.

- [ ] **[Fase 3]** **Tipos de dato y escalas:** Soporte para datos discretos (1-4, A-D) y continuos (0-10) con coeficiente de conversión configurable por instrumento.
  - *CIFPA v10:* Hoja `INTRO_Instrumentos` — campo "Tipo de dato" (discreto/continuo) y "Escala" (1-4, 0-10, etc.).

- [ ] **[Fase 3]** **Agentes de evaluación:** Distinguir heteroevaluación, coevaluación y autoevaluación en cada instrumento.
  - *CIFPA v10:* Campo "Agentes" en `INTRO_Instrumentos`.

- [ ] **[Fase 3]** **Modificación Manual Justificada:** Permitir sobrescribir la nota calculada de un RA añadiendo una justificación pedagógica (requisito legal).
  - *CIFPA v10:* Hoja `RA_Mod` — campo "Mod" que prevalece sobre el cálculo automático.
  - *D 91/2024 Art. 19.3:* El profesorado recogerá información permanente del proceso de enseñanza-aprendizaje, con especial atención a los criterios de evaluación.

- [ ] **[Fase 3]** **Sistema de Alerta de Abandono:** Marcar alumnos con <3 asistencias en las primeras 2 semanas.
  - *D 91/2024 Art. 19.5:* Pérdida del derecho a evaluación continua con máximo 15% de faltas respecto a la duración total del módulo.

- [ ] **[Fase 3]** **Cortes de Evaluación:** Emitir notas parciales basadas solo en el % de RA evaluado hasta esa fecha.
  - *CIFPA v10:* Hojas `EV_Parcial` con Ev1, Ev2, Ev3 independientes y acumulables.
  - *Guía PD v1 §4.2:* Evaluación inicial (no calificativa, diagnóstica), evaluaciones parciales y evaluaciones finales.

- [ ] **[Fase 3]** **Evaluación Inicial Diagnóstica:** Prueba o actividad al inicio del módulo para detectar conocimientos previos y adaptar la programación. No es calificativa, sino orientativa.
  - *Guía PD v1 §4.2:* Evaluación inicial como herramienta de diagnóstico, no de calificación.
  - *IED 2024-25 §2.2.1:* PH0 como criterio de práctica docente (40 puntos).

- [ ] **[Fase 3]** **Mecanismo "Mejor Nota" Extraordinaria:** Guardar RAs superados en la ordinaria y reevaluar solo suspensos.
  - *CIFPA v10:* Hoja `EV_Final-Extraordinaria` — solo recalifica RAs suspendidos, manteniendo aprobados.
  - *Guía PD v1 §4.2.4:* Segunda evaluación final para alumnado que no superó la primera.

### 1.2 Evaluación y Calificación (CIFPA v10)

> **Fuente:** CIFPA v10 Manual, Guía PD v1 §4.7, Módulo 4 Curso JJ Parte 3

- [ ] **[Fase 3]** **Ponderación por niveles de CE:** Permitir definir niveles (1, 2, 3...) con peso relativo configurable.
  - *CIFPA v10:* Campo "Nivel" en `CONF_CE` que activa ponderación por niveles.

- [ ] **[Fase 3]** **Grupos de evaluación (GEv):** Soporte para alumnos en diferentes grupos de evaluación dentro del mismo módulo.
  - *CIFPA v10:* Campo GEv por alumno en `CONF_ALUM`.

- [ ] **[Fase 3]** **Pérdida de derecho a evaluación continua (PDEvC):** Flag por alumno para indicar pérdida del derecho.
  - *CIFPA v10:* Campo PDEvC en `CONF_ALUM`.
  - *D 91/2024 Art. 19.5:* Máximo 15% de faltas. Cada centro indica el porcentaje en el Proyecto Curricular.
  - *Módulo 4 Curso JJ Parte 2:* 15% sobre duración total, excluyendo horas de FEOE, desde fecha de matrícula. Solo afecta a la 1ª evaluación final; en la 2ª concurre en igualdad.

- [ ] **[Fase 3]** **Estado de baja (B):** Marcar alumnos en situación de baja sin eliminar sus datos.
  - *CIFPA v10:* Campo B en `CONF_ALUM`.

- [ ] **[Fase 3]** **Nota mínima de supletoriedad y compensación:** Configurar nota mínima para considerar RA superado y nota mínima para aplicar criterios de compensación.
  - *CIFPA v10:* "Nota mín. sup." y "Nota mín. comp." en `CONF_EV`.
  - *Módulo 4 Curso JJ Parte 3:* Un RA se considera superado con ≥5 sobre 10. Para compensación, se indica calificación mínima (no inferior a 3 ni superior a 5).

- [ ] **[Fase 3]** **Recuperaciones R1, R2, R3 y RF:** Sistema de hasta 3 recuperaciones ordinarias + recuperación final, cada una con sus propios instrumentos.
  - *CIFPA v10:* Campo "Rec" en `INTRO_Instrumentos` (valores: 1, 2, 3, F).
  - *Guía PD v1 §4.5:* Procedimiento de recuperación con momentos clave (al finalizar cada RA no superado, al finalizar cada evaluación parcial, antes de la evaluación final).

- [ ] **[Fase 3]** **Evaluación ordinaria vs extraordinaria:** Dos procedimientos diferenciados con reglas de cálculo distintas.
  - *CIFPA v10:* Hojas `EV_Final-Ordinaria` y `EV_Final-Extraordinaria`.
  - *D 91/2024 Art. 21:* Convocatorias de evaluación final (primera y segunda).

- [ ] **[Fase 3]** **Estadísticas de evaluación:** Hojas de estadísticas automáticas por evaluación.
  - *CIFPA v10:* Hojas `EV_FO-Estadísticas`, `EV_FE-Estadísticas`, `EV_Parcial-Estadísticas`.

- [ ] **[Fase 3]** **Proceso jerárquico de cálculo:**
  1. CE: Calculado a partir de los instrumentos de calificación.
  2. RA: Media ponderada de sus CE.
  3. Calificación Final: Media ponderada de las calificaciones de todos los RA.
  - *Módulo 4 Curso JJ Parte 3:* Calificación final ≥5 sobre 10 para superar. Expresión en valores enteros (1-10), sin decimales.

### 1.3 Informes individuales (CIFPA v10)

> **Fuente:** CIFPA v10 Manual

- [ ] **[Fase 5]** **Informe de RA individual:** Vista detallada de un RA concreto para un alumno, con desglose por CE y peso en el módulo. *(CIFPA: hoja `INFO_RA`)*
- [ ] **[Fase 5]** **Informe de instrumento individual:** Detalle completo de un instrumento para un alumno con trazabilidad hasta indicadores. *(CIFPA: hoja `INFO_Instrumento`)*
- [ ] **[Fase 5]** **Informe de módulo profesional:** Resumen global del módulo con todos los RA, CE, instrumentos y calificaciones. *(CIFPA: hoja `INFO_MP`)*
- [ ] **[Fase 5]** **Informe RA-CE consolidado:** Vista cruzada de todos los RA y CE con su estado de evaluación. *(CIFPA: hoja `INFO_MP-RA-CE`)*

---

## 2. 🏢 FP Dual y FEOE (Ley 3/2022)

> **Fuente:** LO 3/2022, RD 659/2023, D 91/2024, Guía PD v1 §2.9, Módulo 2 Curso JJ, Módulo 4 Curso JJ Parte 3

### 2.1 Grados formativos

- [ ] **[Fase 1]** **Selector de Grados Formativos:** Permitir gestionar grados A, B, C, D y E.
  - *LO 3/2022:* A=acreditación parcial/microacreditaciones, B=certificado de competencia, C=certificado profesional, D=título CFGB/CFGM/CFGS, E=curso especialización.
  - *D 91/2024 Art. 4:* Grado D = Ciclos Formativos de Grado Básico, Medio y Superior. Grado E = Cursos de Especialización de Grado Medio o Superior.

- [ ] **[Fase 1]** **Itinerario Formativo Personalizado:** Gestión de secuencias formativas individuales que permiten al alumno avanzar por diferentes grados (A→B→C→D→E) según su ritmo y necesidades.
  - *D 91/2024 Art. 15:* Itinerarios formativos como eje del sistema de FP.
  - *RD 69/2025:* Sistema Nacional de Formación Profesional como marco de coordinación.

- [ ] **[Fase 1]** **Catálogo modular de FP:** Integrar el Catálogo Modular Nacional con módulos profesionales de cada familia y grado.
  - *RD 69/2025:* Crea el Catálogo Nacional de Estándares de Competencias Profesionales (sustituye al antiguo Catálogo Nacional de Cualificaciones).

- [ ] **[Fase 1]** **Estándares de competencia profesional:** Vincular módulos con estándares del Catálogo Nacional (niveles 1, 2, 3).
  - *RD 532/2025:* Desarrolla los estándares de competencia profesional.
  - *Módulo 2 Curso JJ:* Los ECP se incluyen en la PD con código, denominación, familia y nivel.

- [ ] **[Fase 1]** **Microacreditaciones (Grado A):** Soporte para formación modular corta con acreditación parcial de competencia.
- [ ] **[Fase 1]** **Certificados de competencia (Grado B):** Gestión de certificados asociados a módulos profesionales individuales.
- [ ] **[Fase 1]** **Certificados profesionales (Grado C):** Agrupación de módulos para obtener certificado profesional acumulable.

### 2.2 FP Dual

- [ ] **[Fase 4]** **Modalidades Duales:** Soporte para Régimen General e Intensivo.
  - *Módulo 2 Curso JJ:* FEOE tiene dos opciones: con RA en FEOE o sin RA en FEOE. Cada una con modalidad (régimen general/intensivo).

- [ ] **[Fase 4]** **Distribución Centro-Empresa:** Definir qué RAs se dan en el instituto, en la empresa o compartidos.
  - *CIFPA v10:* Hoja `INTRO_FP-Dual`.
  - *Módulo 2 Curso JJ:* FEOE Opción A (con RA) — se especifican RA desarrollados en la empresa, desarrollo parcial o total, justificación pedagógica. FEOE Opción B (sin RA) — solo actividades de seguimiento.

- [ ] **[Fase 4]** **Evaluación del Tutor de Empresa:** Interfaz/registro para volcar la rúbrica (1 a 4) del tutor externo.
  - *Módulo 4 Curso JJ Parte 3:* El tutor/a dual de empresa valora cada actividad con puntuación de 1 a 4. Un RA se considera superado si la media de sus actividades es >2. Se incluye valoración cualitativa.

- [ ] **[Fase 4]** **Generación Anexo XI b:** Plan de formación individualizado automático.

### 2.3 FEOE (Formación en Centros de Trabajo)

- [ ] **[Fase 4]** **Gestión de FEOE completa:** Empresa, tutor, horas, evaluación del tutor, convenio.
  - *CIFPA v10:* Hoja `M02.T03_E FEOE`.
  - *Guía PD v1 §2.9:* Organización temporal (fechas inicio/fin, duración horas), RA desarrollados, actividades, seguimiento (reuniones quincenales presenciales, visitas a empresa, comunicaciones puntuales).

- [ ] **[Fase 4]** **Generación automática de documentación FEOE:** Convenios, anexos, evaluaciones de empresa.
  - *D 91/2024 Art. 49:* Exención del periodo de FEOE por experiencia laboral (últimos 5 años).

- [ ] **[Fase 4]** **Plataforma de Firma Digital y Conformidad:** Sistema integrado para gestionar el volumen masivo de anexos, planes de formación individualizados y firmas electrónicas (co-evaluación) con los tutores de empresa, esencial dado el carácter dual de toda la nueva FP.

---

## 3. 📄 Generación de Documentos (Pestaña Descargas)

> **Fuente:** Guía PD v1 completa, Modelos UD/Tarea/Instrumento, Ejemplo PD IED, PD completa IED, PD BOA/Aragon (Anexo I), PD Aragón (16p), PD BOA (10p), Síntesis 3 niveles

*(Todo lo que esté en Descargas debe ser exportación final: .docx o .pdf)*

### 3.1 Programación didáctica completa

#### 3.1.1 Selector de nivel de detalle (3 niveles)

El usuario elige el nivel de detalle al generar la PD. Cada nivel incluye los anteriores:

| Nivel | Nombre | Secciones | Fuente |
|-------|--------|-----------|--------|
| **PD-** | Mínima | 10 secciones (sin Anexo I) | ``referencia/48-PD-BOA-10p.md`` (10p BOA) |
| **PD=** | Suficiente | 11 secciones (con Anexo I) | ``referencia/49-PD-Aragon-16p.md`` (16p Aragón) |
| **PD+** | Detallada | 11 secciones + Anexo I completo + metadatos | ``referencia/50-PD-tres-niveles-sintesis.md`` (síntesis) |

**Secciones comunes (PD-):**
1. Datos identificativos
2. Introducción (justificación, normativa, contexto)
3. Contextualización (centro, entorno, alumnado, recursos)
4. Elementos curriculares (ECP, CPE, OG, RA, CE, Contenidos)
5. Metodología didáctica
6. Organización temporal (secuenciación UD)
7. Procedimiento de evaluación y calificación
8. Medidas inclusión (ACNEAE)
9. Actividades complementarias
10. Plan de contingencia

**Sección adicional (PD= y PD+):**
11. **Anexo I: Tabla RA/CE/Contenidos/Indicadores/Evaluación** (obligatorio BOA/Aragón)

**Contenido extra (PD+):**
- Anexo I con ponderaciones por evaluación (Ev1/Ev2/Ev3)
- Metadatos: fecha creación, última modificación, autor, versión
- Justificación pedagógica en cada sección
- Referencias cruzadas entre secciones

#### 3.1.2 Generador DOCX (todos los niveles)

- [ ] **[Fase 5]** **Programación Didáctica Completa (DOCX):** Generador DOCX con el índice completo según Guía PD v1:
  1. **Introducción** (§1): Identificación (centro, grado, módulo, curso, modalidad), Marco normativo (LO 3/2022, RD 659/2023, D 91/2024), Contextualización (entorno geográfico/sociocultural, socioeconómico/productivo, contexto escolar, características alumnado, infraestructura/recursos)
  2. **Desarrollo curricular** (§2): Estándares de competencia profesional, CPE, Objetivos generales, RA y CE, Contenidos, Relación entre elementos curriculares, Organización y distribución temporal (UD), Duración/ubicación/distribución horaria, FEOE
  3. **Metodología didáctica** (§3): Enfoque metodológico, Estrategias didácticas, Agrupamientos, Materiales y recursos, Actividades complementarias/extraescolares
  4. **Procedimiento de evaluación y calificación** (§4): Actividades/técnicas/instrumentos, Evaluaciones (inicial, parciales, finales), Información del procedimiento, Pérdida derecho evaluación continua, Procedimiento de recuperación, Evaluación FEOE, Criterios de calificación y ponderación, Plan de recuperación módulos pendientes
  5. **Medidas de respuesta educativa para la inclusión** (§5): Adaptaciones curriculares no significativas, ajustes metodológicos/organativos/de acceso/de evaluación
  6. **Actividades complementarias y extraescolares** (§6)
  7. **Plan de contingencia** (§7)
  8. **Publicidad de la programación didáctica** (§8)

### 3.2 Unidades didácticas

- [ ] **[Fase 5]** **Generador de UD:** Según modelo CIFPA, cada UD incluye:
  - Duración (horas asignadas)
  - Temporización (periodo del curso, relación con otras UD)
  - Intención educativa (vinculación perfil profesional, CPE, transversalidad, conocimientos previos)
  - Competencias profesionales y para la empleabilidad
  - Objetivos generales
  - RA, CE y Contenidos
  - Estrategias metodológicas
  - Materiales y recursos
  - Agrupamientos (gran grupo, pequeño grupo, individual)
  - Actividades de evaluación y/o calificación
  - Secuencia de actividades de enseñanza-aprendizaje (con fases: inicio/desarrollo/cierre)
  - Actividades de refuerzo
  - Actividades de ampliación

### 3.3 Tareas competenciales

- [ ] **[Fase 5]** **Generador de Tareas Competenciales:** Según modelo CIFPA:
  - Identificación (UD, código actividad, título)
  - Contexto profesional (producto/proceso/mixto, situación laboral creíble)
  - Objetivo (en términos de desempeño: demostrar, gestionar, aplicar)
  - Scenario o Briefing (encargo específico: correo, llamada, documentación técnica)
  - RA y CE asociados
  - Desarrollo de la tarea (pasos)
  - Evidencias a generar y entregar
  - Técnicas e instrumentos de evaluación
  - Entrega (formato, plazo)

### 3.4 Instrumentos de evaluación

- [ ] **[Fase 3]** **Generación de Rúbricas:** Plantillas configurables por CE/indicador con escalas personalizadas.
  - *Modelo Instrumento:* Alineación con CE, indicadores claros y observables, ponderaciones correctas, validez y fiabilidad, retroalimentación.
- [ ] **[Fase 3]** **Generación de Listas de Control:** Checklists vinculadas a indicadores (presencia/ausencia).
- [ ] **[Fase 3]** **Generación de Escalas de Valoración:** Escalas tipo Likert para evaluación de proyectos y defensas.
- [ ] **[Fase 3]** **Exámenes tipo test:** Generador de pruebas objetivas con banco de preguntas.
  - *D 91/2024 Art. 19.4:* Instrumentos: rúbricas, listas de cotejo, guía de observación, cuaderno de clase, exámenes, mapas conceptuales, trabajos, investigaciones, grabaciones audio/vídeo.
- [ ] **[Fase 3]** **Tabla Anexo I (RA/CE/Contenidos/Indicadores):** Generación automática de la tabla resumen obligatoria en PD= y PD+. Incluye: RA, CE, Contenidos, Indicadores de evaluación, Técnicas/instrumentos, Ponderación por evaluación (Ev1/Ev2/Ev3). Fuente: ``referencia/49-PD-Aragon-16p.md`` §Anexo I.

### 3.5 Documentos administrativos

- [ ] **[Fase 5]** **Actas de evaluación:** Generación automática con calificaciones por RA y nota final.
  - *D 91/2024 Art. 44:* Actas de evaluación con calificaciones.
- [ ] **[Fase 5]** **Boletines de calificaciones:** Por alumno con desglose por RA y CE.
- [ ] **[Fase 5]** **Informe de evaluación individualizado:** *(D 91/2024 Art. 45)*
- [ ] **[Fase 5]** **Certificado académico:** *(D 91/2024 Art. 46)*
- [ ] **[Fase 5]** **Documento de evaluación provisional:** *(D 91/2024 Art. 47)* — calificaciones antes de FEOE.
- [ ] **[Fase 5]** **Envío de Emails Automatizado:** Enviar boletines e informes a correos de alumnos/familias.

---

## 4. 📊 Dashboards y Analítica Visual (Web)

> **Fuente:** CIFPA v10 hojas de estadísticas, Guía PD v1 §4

*(Para el uso interactivo del docente dentro del resto de la aplicación)*

- [ ] **[Fase 6]** **Dashboard de Estadísticas Interactivo:** Gráficas de rendimiento académico (sexo, edad, nacionalidad), % aprobados y comparativas por RA.
- [ ] **[Fase 6]** **Dashboard de Indicadores:** Visualización de los indicadores del Sistema Estatal a nivel de módulo.
- [ ] **[Fase 6]** **Estadísticas por evaluación:** Distribución de notas en Ev1, Ev2, Ev3, EvFO, EvFE.
  - *CIFPA v10:* Hojas `EV_FO-Estadísticas`, `EV_FE-Estadísticas`, `EV_Parcial-Estadísticas`.
- [ ] **[Fase 6]** **Análisis de trazabilidad:** Visualización de la cadena Indicador → CE → RA → Módulo con pesos y resultados.
- [ ] **[Fase 6]** **Comparativa ordinaria vs extraordinaria:** Análisis de mejora entre evaluaciones.

---

## 5. 🤝 Acción Tutorial y Seguimiento

> **Fuente:** CIFPA v10 hojas `INTRO_Tutoría`, `INTRO_Seguimiento`, `INFO_Calendario`, `INFO_Seguimiento`

### 5.1 Tutoría

- [ ] **[Fase 4]** **Registro Básico de Tutorías:** Panel de mínimos para que el docente anote sus propias observaciones de tutoría individual.
  - *CIFPA v10:* Hoja `INTRO_Tutoría` — campos: Fecha, Hora inicio/fin, Alumno/a, Ámbito, Canal, Tipo, Tema, Participantes, Desarrollo, Acuerdos.
  - *Ámbitos:* grupo completo, alumno/a, familia, equipo docente, orientación.
  - *Canales:* reunión presencial, llamada telefónica, correo electrónico, etc.
  - *Tipos:* seguimiento académico, evaluación, convivencia, orientación.

- [ ] **[Fase 4]** **Módulo de Calidad (EQAVET) Básico:** Autoevaluación del docente/módulo y establecimiento de objetivos de calidad.

### 5.2 Seguimiento diario

- [ ] **[Fase 4]** **Distribución temporal visual:** Calendario interactivo con bloques temporales asignados a UD.
  - *CIFPA v10:* Hoja `INTRO_Dist-Temporal` con tipos de bloque configurables. Hoja `CONF_DIST-TEMP` para definir tipos.
  - *Módulo 2 Curso JJ:* Organización de UD: secuencial, paralela o mixta.

- [ ] **[Fase 4]** **Seguimiento de impartición:** Registro de qué se ha impartido realmente vs lo planificado.
  - *CIFPA v10:* Hoja `INTRO_Seguimiento`. Hoja `INFO_Seguimiento` para informe.

- [ ] **[Fase 4]** **Calendario escolar automático:** Generación desde fechas de inicio/fin y festivos.
  - *CIFPA v10:* Hoja `INFO_Calendario` — generado automáticamente desde `CONF_Fechas`.

---

## 6. 🚀 Módulos Transversales

> **Fuente:** LO 3/2022, LOMLOE, Guía PD v1 §1.3, §5, Módulo 2 Curso JJ

- [ ] **[Fase 2]** **Digitalización y Sostenibilidad:** Inclusión de competencias transversales.
  - *Guía PD v1 §1.3:* Elementos transversales (sostenibilidad, igualdad, digitalización).

- [ ] **[Fase 2]** **Plan de Contingencia Digital:** Estrategia para garantizar la continuidad del proceso de enseñanza-aprendizaje ante interrupciones (pandemia, emergencias, etc.). Incluye alternativas digitales, recursos online y adaptación de actividades.
  - *Guía PD v1 §7:* Plan de contingencia como sección obligatoria de la PD.
  - *IED 2024-25 §Q:* PH0 en la estructura de la PD.

- [ ] **[Fase 2]** **Registro de Innovación:** Proyectos de emprendimiento y equidad/DUA (necesidades de apoyo).
- [ ] **[Fase 2]** **Competencias clave:** Desarrollo y evaluación de competencias clave (CL, CSTEM, CD, CCEC, CPSAA, CE, CIEC).
  - *LOMLOE/LO 3/2022:* 7 competencias clave del sistema educativo.
  - *Indicadores IED 2024-25:* "Las programaciones incluyen el desarrollo de las competencias clave" (4 puntos).

- [ ] **[Fase 2]** **Itinerario Personal para la Empleabilidad (IPE I e IPE II):** Tratamiento específico para estos nuevos módulos que sustituyen a los clásicos FOL y EIE, gestionando sus particularidades curriculares según la nueva ley.
- [ ] **[Fase 2]** **Proyecto Intermodular Continuo:** Gestión del Proyecto Intermodular como eje vertebrador del aprendizaje de forma conjunta entre varios módulos (especialmente en Grados C y D), más allá del antiguo "módulo de proyecto" que se hacía solo al final del ciclo.

---

## 7. 🌍 Multi-territorio: Comunidades Autónomas y Territorio MEC

> **Fuente:** LO 3/2022, RD 659/2023, D 91/2024 Aragón, todofp.es

### 7.1 Arquitectura multi-territorio

- [ ] **[Fase 1]** **Selector de territorio/jurisdicción:** Al configurar el curso, el docente selecciona su comunidad autónoma o "Territorio MEC" (Ceuta y Melilla). Esto determina:
  - Normativa aplicable (LO 3/2022 + desarrollo autonómico)
  - Currículos de módulos (RA/CE adaptados por la CCAA)
  - Calendario escolar autonómico
  - Procedimientos de evaluación específicos
  - Terminología local (si difiere)

### 7.2 Territorio MEC (Ceuta y Melilla)

- [ ] **[Fase 1]** **Gestión directa del Ministerio:** Ceuta y Melilla dependen directamente del Ministerio de Educación.
- [ ] **[Fase 1]** **Currículo estatal puro:** Aplicar los currículos del RD 659/2023 y órdenes ministeriales sin adaptación autonómica.
- [ ] **[Fase 1]** **Calendario escolar MEC:** Calendario específico para Ceuta y Melilla.

### 7.3 Comunidades Autónomas (17 CCAA)

- [ ] **[Fase 1]** **Andalucía:** Consejería de Educación y Deporte. Currículos propios (O ECD-841/842/843-2024).
- [ ] **[Fase 1]** **Aragón:** Departamento de Educación, Cultura y Deporte. D 91/2024 de ordenación FP grados D y E. Currículos propios (O ECD-841/842/843-2024).
- [ ] **[Fase 1]** **Asturias (Principado de):** Consejería de Educación.
- [ ] **[Fase 1]** **Islas Baleares:** Dirección General de FP y Ordenación Educativa.
- [ ] **[Fase 1]** **Canarias:** Consejería de Educación, FP, Actividad Física y Deportes.
- [ ] **[Fase 1]** **Cantabria:** Consejería de Educación, FP y Universidades.
- [ ] **[Fase 1]** **Castilla-La Mancha:** Consejería de Educación.
- [ ] **[Fase 1]** **Castilla y León:** Consejería de Educación.
- [ ] **[Fase 1]** **Cataluña:** Departament d'Educació. Terminología propia (mòdul professional, criteri d'avaluació, resultat d'aprenentatge).
- [ ] **[Fase 1]** **Extremadura:** Consejería de Educación y Empleo.
- [ ] **[Fase 1]** **Galicia:** Consellería de Cultura, Educación, FP e Universidades. Terminología propia.
- [ ] **[Fase 1]** **Comunidad de Madrid:** Consejería de Educación y Universidades.
- [ ] **[Fase 1]** **Región de Murcia:** Consejería de Educación.
- [ ] **[Fase 1]** **Navarra (Comunidad Foral de):** Departamento de Educación.
- [ ] **[Fase 1]** **País Vasco:** Departamento de Educación. Terminología propia (modulu profesional, ebaluazio irizpidea, ikaskuntza emaitza).
- [ ] **[Fase 1]** **La Rioja:** Consejería de Educación.
- [ ] **[Fase 1]** **Comunidad Valenciana:** Conselleria d'Educació, Cultura, Universitats i Esport. Terminología propia.

### 7.4 Implementación técnica multi-territorio

- [ ] **[Fase 1]** **Catálogo de currículos por CCAA:** Base de datos con RA/CE adaptados por comunidad autónoma y módulo. *(Actualmente solo hay currículos de Aragón en `src/data/curriculos/`)*
- [ ] **[Fase 1]** **Normativa por territorio:** Referencias legales específicas (BOE + BOA/BOCA/DOG/DOGC/DOGV/etc.)
- [ ] **[Fase 1]** **Calendarios escolares autonómicos:** Festivos autonómicos y locales específicos por CCAA.
- [ ] **[Fase 1]** **i18n/Internacionalización:** Soporte para castellano, catalán, euskera, gallego, valenciano, aranés. *(Ya existe estructura `frontend/src/i18n/`)*
- [ ] **[Fase 1]** **Exportación adaptada:** Los documentos generados deben incluir la normativa y terminología de la CCAA correspondiente.

---

## 8. 📋 Denominaciones LO 3/2022 (Nuevas terminologías)

> **Fuente:** LO 3/2022, RD 659/2023, RD 69/2025, D 91/2024, Guía PD v1

### 8.1 Denominaciones a incorporar

| Término actual en APP | Nuevo término LO 3/2022 | Notas |
|---|---|---|
| Ciclo formativo | **Título de FP** (Grado D) | LO 3/2022: "título" en lugar de "ciclo formativo" |
| CFGM / CFGS / CFGB | **Grado D** (con nivel 1/2/3) | CFGB=nivel 1, CFGM=nivel 2, CFGS=nivel 3 |
| Módulo profesional | **Módulo profesional** | Se mantiene |
| Resultado de aprendizaje (RA) | **Resultado de aprendizaje (RA)** | Se mantiene |
| Criterio de evaluación (CE) | **Criterio de evaluación (CE)** | Se mantiene |
| — | **Competencia profesional** | Nueva: conjunto de competencias asociadas al título |
| — | **Competencia general** | Nueva: competencia general del título |
| — | **Unidad de competencia** | Nueva: bloque de competencia dentro de la competencia profesional |
| — | **Estándar de competencia profesional** | Nueva: unidad mínima del Catálogo Nacional (niveles 1, 2, 3) |
| — | **Microacreditación** (Grado A) | Nueva: acreditación parcial de competencia |
| — | **Certificado de competencia** (Grado B) | Nueva: asociado a un módulo profesional |
| — | **Certificado profesional** (Grado C) | Nueva: agrupación de módulos acumulables |
| — | **Curso de especialización** (Grado E) | Nueva: formación complementaria de especialización |
| FCT / FCTDual | **FEOE** (Formación en Centros de Trabajo) | LO 3/2022 unifica denominación |
| Programación didáctica | **Programación didáctica** | Se mantiene |
| Unidad didáctica | **Unidad didáctica** | Se mantiene |
| — | **Itinerario formativo** | Nueva: secuencia personalizada de grados/módulos |
| — | **Sistema Nacional de Formación Profesional** | RD 69/2025: marco de coordinación estatal |
| — | **Proyecto intermodular** | D 91/2024 Art. 10: proyecto que vincula varios módulos |
| — | **Bloque formativo** | D 91/2024: agrupación de módulos para convalidación |

### 8.2 Competencias profesionales y clave

- [ ] **[Fase 1]** **Competencias profesionales del título:** Cada título (Grado D) define competencias profesionales que deben estar vinculadas a los módulos.
  - *Módulo 2 Curso JJ:* Las CPE no son objeto directo de evaluación ni calificación. Se incluyen solo las asociadas al módulo profesional.
- [ ] **[Fase 1]** **Competencias clave:** CL, CSTEM, CD, CCEC, CPSAA, CE, CIEC. *(LOMLOE/LO 3/2022)*
- [ ] **[Fase 1]** **Vinculación RA → Competencia profesional:** Cada RA debe estar vinculado a una o varias competencias profesionales del título.
- [ ] **[Fase 1]** **Vinculación RA → Competencia clave:** Cada RA debe indicar qué competencias clave contribuye a desarrollar.

### 8.3 Catálogo Nacional de Estándares de Competencia Profesional

- [ ] **[Fase 1]** **Integración del buscador de estándares:** Conectar con el catálogo nacional para vincular módulos con estándares de competencia profesional (niveles 1, 2, 3). *(INCUAL)*
- [ ] **[Fase 1]** **Niveles de cualificación:** Soporte para los 3 niveles del Catálogo Nacional.

---

## 9. 📐 Estructura del Cuaderno del Profesorado (Referencia CIFPA v10)

> **Fuente:** CIFPA Cuaderno v10 Manual (27p), CIFPA v10.1.xlsx (3.1MB)

### 9.1 Hojas de configuración (CONF_*)

| Hoja | Contenido | Campos clave |
|------|-----------|--------------|
| `CONF_Fechas` | Fechas del curso académico | Inicio, fin, evaluaciones |
| `CONF_MP` | Datos del módulo profesional | Ciclo, familia, curso, horas |
| `CONF_ALUM` | Listado de alumnado | Datos identificativos, GEv, PDEvC, B |
| `CONF_EV` | Configuración de evaluaciones | Ev1, Ev2, Ev3, EvFO, EvFE con ponderaciones por nivel de CE. Nota mín. sup., Nota mín. comp. |
| `CONF_RA` | Configuración de RA | Pesos relativos dentro del módulo |
| `CONF_CE` | Configuración de CE | Pesos relativos dentro del RA, niveles opcionales |
| `CONF_DIST-TEMP` | Tipos de bloques temporales | Para distribución |

### 9.2 Hojas de introducción de datos (INTRO_*)

| Hoja | Contenido | Campos clave |
|------|-----------|--------------|
| `INTRO_Tutoría` | Registro de actuaciones tutorial | Fecha, Hora inicio/fin, Alumno/a, Ámbito, Canal, Tipo, Tema, Participantes, Desarrollo, Acuerdos |
| `INTRO_Dist-Temporal` | Distribución temporal del módulo | Asignación de UD a bloques |
| `INTRO_Seguimiento` | Seguimiento de impartición | Qué se ha impartido vs lo planificado |
| `INTRO_FP-Dual` | Configuración de FP Dual | Distribución centro-empresa |
| `INTRO_Instrumentos` | Definición de instrumentos | Tipo, escala, agentes, evaluación, peso por CE, campo Rec |
| `INTRO_Indicadores` | Definición de indicadores | Vinculados a RA y CE con pesos |
| `INTRO_Calificaciones` | Matriz de calificación diaria | Alumnado × indicadores |

### 9.3 Hojas de cálculo automático (RA, EV_*)

| Hoja | Contenido |
|------|-----------|
| `RA_Mod` | Calificación de RA con modificación manual justificada |
| `RA` | Vista detallada de un RA seleccionado con desglose por CE |
| `EV_Parcial` | Evaluación parcial (Ev1, Ev2, Ev3) |
| `EV_Final-Ordinaria` | Evaluación final ordinaria (EvFO) |
| `EV_Final-Extraordinaria` | Evaluación final extraordinaria (EvFE) |
| `EV_FO-Estadísticas` | Estadísticas automáticas EvFO |
| `EV_FE-Estadísticas` | Estadísticas automáticas EvFE |
| `EV_Parcial-Estadísticas` | Estadísticas automáticas parciales |

### 9.4 Hojas de información (INFO_*)

| Hoja | Contenido |
|------|-----------|
| `INFO_MP` | Informe del módulo profesional |
| `INFO_RA` | Informe individual de RA |
| `INFO_Instrumento` | Informe individual de instrumento con trazabilidad |
| `INFO_MP-RA-CE` | Vista consolidada de todos los RA y CE |
| `INFO_Calendario` | Calendario escolar generado automáticamente |
| `INFO_Seguimiento` | Informe de seguimiento de impartición |

### 9.5 Hojas auxiliares (AUX_*)

| Hoja | Contenido |
|------|-----------|
| `AUX_EV_Final-RA` | Cálculos intermedios RA |
| `AUX_EV_Final-CE` | Cálculos intermedios CE |
| `AUX_EV_Parcial_RA` | Cálculos parciales RA |
| `EV_Ord-Parcial_CE` | Cálculos parciales CE |
| `AUX_CAL-IND-P` | Cálculos de calificaciones indicadores |
| `AUX_CAL-INST-CE` | Cálculos de calificaciones instrumentos-CE |
| `AUX-RA-CE` | Tablas auxiliares RA-CE |
| `AUX-General` | Tablas auxiliares generales |

---

## 🗺️ Roadmap Sugerido de Implementación (Fases)

Para abordar todas estas ideas de forma estructurada sin romper la aplicación, se sugiere el siguiente orden de desarrollo:

### **[Fase 1] Arquitectura Base y Catálogo (Actual)**
* **Objetivo:** Sentar las bases del sistema, multi-territorio (CCAA/MEC), denominaciones LO 3/2022 y catálogo de grados formativos.
* **Secciones:** 2.1, 7 y 8.

### **[Fase 2] Currículo y Configuración del Módulo**
* **Objetivo:** Permitir al docente configurar su módulo, asociar elementos transversales, competencias clave, atención a la diversidad y planes de contingencia.
* **Secciones:** 6 y 10.

### **[Fase 3] Instrumentos, Calificaciones y Matriz Core**
* **Objetivo:** El "corazón" de CuadernoFP. Matriz diaria de notas, rúbricas, escalas, jerarquía de cálculo (Indicador → CE → RA → Final) y cortes de evaluación.
* **Secciones:** 1.1, 1.2 y 3.4.

### **[Fase 4] Seguimiento, Tutorías y FP Dual**
* **Objetivo:** Gestión del día a día (asistencias, tutorías, calendario) y la integración de la FEOE (empresa, tutores externos).
* **Secciones:** 2.2, 2.3, 5.1 y 5.2.

### **[Fase 5] Generación Documental y PD**
* **Objetivo:** Volcar toda la información recogida en las fases anteriores para exportar documentos oficiales (Actas, Informes, Unidades Didácticas y la PD completa).
* **Secciones:** 1.3, 3.1, 3.2, 3.3 y 3.5.

### **[Fase 6] Dashboards, Analítica y Mejoras Técnicas**
* **Objetivo:** Capa visual de estadísticas, analíticas y mejoras técnicas como exportaciones Excel y offline.
* **Secciones:** 4 y 12.

### **~~[Fase 7] Accesibilidad WCAG 2.2 AA~~ (Completada por MIMO Xiaomi ✅)**
* **Objetivo:** Conformidad con WCAG 2.2 nivel AA para cumplimiento normativo y mejora de usabilidad.
* **Estado:** Completada
* **Prioridad:** Alta — bloquea declaracion de conformidad CIFPA