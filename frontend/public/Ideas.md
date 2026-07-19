# 💡 Backlog de Ideas y Mejoras - Cuaderno FP

> **Última actualización:** 19 julio 2026  
> **Fuentes analizadas:** 49 documentos organizados en `RF Ideas/referencia/` (ver `INDICE.md`)
> - Normativa: LO 3/2022, RD 659/2023, RD 69/2025, RD 532/2025, D 91/2024 Aragón, O ECD/1005/2018
> - Guía PD v1 (Javier Edo Gual, CIFPA), Curso PD JJ (8 módulos), Modelos UD/Tarea/Instrumento
> - CIFPA Cuaderno v10, Ejemplo PD IED 2024-25, PD completa IED, TFM RSP, Indicadores, Memoria

*(Nota: Las Fases 2, 4 (parcial), 5 (parcial) y 6 se han completado y eliminado de este backlog para mayor legibilidad).*

---

## Sprint A: Instrumentos de Evaluación y Generación (Fases 3 y 5)
*Objetivo: Dotar a la aplicación de herramientas para crear rúbricas, exámenes y emitir boletines a las familias.*

1. **Instrumentos de Evaluación (Fase 3):**
   - Construir UI para diseñar **Rúbricas** dinámicas conectadas a los Criterios de Evaluación (CE).
   - Generadores de **Listas de control** y **Escalas de Valoración (Likert)**.
   - Banco de preguntas para la generación automática de **Exámenes tipo test**.
2. **Documentación Administrativa (Fase 5):**
   - Generación en PDF de **Boletines de calificaciones** individuales para los alumnos (con desglose por RA/CE).
   - Generación de **Actas de evaluación**.
   - Informes de evaluación individualizados y certificados académicos.
   - **Envío de Emails automatizado**: Conectar un servicio SMTP para enviar boletines a alumnos/familias.
3. **Generación Didáctica Específica (Fase 5):**
   - Generador en PDF/DOCX de **Unidades Didácticas (UD)** con el desglose metodológico completo.
   - Generador en PDF/DOCX de **Tareas Competenciales** (escenario, evidencias, técnicas).
   - Generación de la tabla obligatoria **Anexo I** con la ponderación de RAs/CEs.

---

## Sprint B: Arquitectura LO 3/2022 y Multi-Territorio (Fase 1)
*Objetivo: Hacer que la aplicación sirva para cualquier Comunidad Autónoma y adapte toda la nomenclatura a la nueva Ley de FP.*

1. **Gestión de Grados y Estándares (Fase 1):**
   - Implementar el modelo de datos para Grados A (Microacreditaciones), Grados B (Certificados de Competencia) y Grados C (Certificados Profesionales).
   - Conectar la BBDD a los **Estándares de Competencia Profesional (INCUAL)** (niveles 1, 2, 3).
   - Vinculación cruzada: RA <-> Competencia Profesional <-> Competencia Clave.
2. **Selector Multi-Territorio (Fase 1):**
   - Implementar el selector de jurisdicción: **Territorio MEC (Ceuta y Melilla)** y las **17 Comunidades Autónomas**.
   - Cargar calendarios escolares dinámicos y festivos según la CCAA seleccionada.
   - Base de datos multi-currículo (poder descargar los RAs/CEs del DOGC, BOC, BOA, etc.).
3. **Internacionalización y Localización (Fase 1):**
   - Implementar `i18n` para soportar Catalán, Euskera, Gallego, Valenciano, etc.
   - Exportación de documentos adaptada a la terminología de cada CCAA (ej. "Mòdul professional" en Cataluña).

---

## Sprint C: FP Dual y Calidad EQAVET (Fase 4)
*Objetivo: Integrar el seguimiento intensivo en empresa de la nueva FP y parámetros de calidad europeos.*

1. **Gestión de la FP Dual (Fase 4):**
   - Soporte para **Régimen General** e **Intensivo**.
   - **Distribución Centro-Empresa**: Panel para definir qué RAs (o porcentaje de CEs) se imparten en el centro educativo y cuáles se asumen en la empresa.
2. **Calidad y Mejora Continua (Fase 4):**
   - Módulo básico **EQAVET** para autoevaluación docente.
   - Panel de establecimiento de objetivos de calidad del departamento.