# Auditoría Title Case en español — APP Cuaderno FP
# Fecha: 19 julio 2026 (re-auditoría 24 julio 2026)

## Resumen
- **es.json**: 9 correcciones — ✅ APLICADAS
- **Componentes TSX**: ~30 strings visibles con Title Case incorrecto — ✅ APLICADAS
- **en.json**: NO tocar (inglés sí usa Title Case)
- **Otros locales** (ca, va, eu, gl, ba): Pendiente de revisión
- **Build**: ✅ 22 rutas, 0 errores TypeScript (24 julio 2026)

---

## 1. `frontend/src/i18n/locales/es.json` — 9 correcciones ✅ APLICADAS

| Línea | ❌ Actual | ✅ Correcto | Contexto |
|-------|----------|------------|----------|
| 40 | "Archivos en la Nube" | "Archivos en la nube" | tabs |
| 41 | "Archivos Locales" | "Archivos locales" | tabs |
| 86 | "En Obras" | "En obras" | sidebar |
| 89 | "Abrir Grupo" | "Abrir grupo" | sidebar |
| 107 | "Seguimiento Diario" | "Seguimiento diario" | pages |
| 115 | "Matrices de Relación" | "Matrices de relación" | pages |
| 121 | "Gestor de Archivos" | "Gestor de archivos" | pages |
| 123 | "Documentos Oficiales" | "Documentos oficiales" | pages |
| 129 | "Aviso Legal" | "Aviso legal" | pages |

---

## 2. Componentes TSX — Title Case incorrecto en strings visibles ✅ APLICADAS

### `AISettingsPanel.tsx`
- L40: `Motor de Inteligencia Artificial` → ok (nombre propio)
- L47: `Google Gemini (Recomendado - gratis para desarrolladores)` → ok (marca)
- L48: `OpenAI ChatGPT (Requiere saldo en la cuenta)` → ok (marca)

### `BoletinesTab.tsx`
- L128: `Boletín Individual de Calificaciones` → "Boletín individual de calificaciones"
- L132: `Imprimir Boletín` → "Imprimir boletín"
- L143: `INFORME DE EVALUACIÓN` → ok (título documento, mayúsculas deliberadas)
- L145: `Módulo Profesional` → "Módulo profesional"
- L148: `Título de FP` → ok (sigla)

### `ContextoGrupoTab.tsx`
- L22: `title="Características del Alumnado"` → "Características del alumnado"

### `FeoeTab.tsx`
- L70: `title="Organización y Modalidad de FEOE"` → "Organización y modalidad de FEOE"
- L75: `title="Seguimiento de FEOE"` → ok (sigla)
- L198: `title="Anexo Convenio"` → "Anexo convenio"
- L201: `title="Plan de Formación"` → "Plan de formación"

### `TutoriaTab.tsx`
- L137: `<option value="Equipo Docente">` → "Equipo docente"
- L150: `<option value="Teléfono">Llamada Telefónica</option>` → "Llamada telefónica"
- L151: `<option value="Email">Correo Electrónico</option>` → "Correo electrónico"

### `ChatbotWidget.tsx`
- L215: `title="Adjuntar PDF o Imagen"` → "Adjuntar PDF o imagen"

### `ProcedimientosTab.tsx`
- L23: `title="Información al Alumnado y Familias"` → "Información al alumnado y familias"
- L28: `title="Pérdida de Evaluación Continua"` → "Pérdida de evaluación continua"
- L33: `title="Procedimiento de Recuperación"` → "Procedimiento de recuperación"
- L38: `title="Plan de Recuperación de Módulos Pendientes"` → "Plan de recuperación de módulos pendientes"

### `BurocraciaTab.tsx`
- L15: `title="Bibliografía y Recursos"` → "Bibliografía y recursos"
- L20: `title="Publicidad de la Programación"` → "Publicidad de la programación"

### `MetodologiaContextoTab.tsx`
- L26: `title="Contexto Geográfico"` → "Contexto geográfico"
- L31: `title="Contexto Socioeconómico"` → "Contexto socioeconómico"
- L36: `title="Contexto Escolar"` → "Contexto escolar"
- L57: `title="Labor Coordinada"` → "Labor coordinada"
- L62: `title="Medidas de Inclusión"` → "Medidas de inclusión"
- L83: `title="Contingencia: Profesorado"` → "Contingencia: profesorado"
- L88: `title="Contingencia: Alumnado"` → "Contingencia: alumnado"

### `SessionTable.tsx`
- L64: `title="Configurar Unidad didáctica"` → "Configurar unidad didáctica"

### `TaskTable.tsx`
- L44: `title="Configurar Tarea Competencial"` → "Configurar tarea competencial"

### `MatrizCalificacionesTab.tsx`
- L154: `title="Alerta Abandono (PDEvC): >15% faltas"` → "Alerta abandono (PDEvC): >15% faltas"

### `AttendanceGrid.tsx` / `AttendanceAccumulated.tsx`
- L134/L136: `title="Menor de edad"` → ok (correcto)

### `AsistenciaTab.tsx`
- L46: `title="Ningún curso activo"` → ok (correcto)

### `DiversidadTab.tsx`
- L160: `title="Eliminar registro"` → ok (correcto)

### `InstallPwaButton.tsx`
- L53: `title="Instalar App"` → "Instalar app"

### Toast messages (visibles al usuario)
- `WelcomeWizard.tsx:24`: `"Inyectando Archivos de demostración..."` → "Inyectando archivos de demostración..."
- `WelcomeWizard.tsx:28`: `"Archivos de demostración cargado!"` → "Archivos de demostración cargados!" (también error gramatical)
- `WelcomeWizard.tsx:44`: `"Creando tu nuevo Archivos..."` → "Creando tu nuevo archivos..."
- `WelcomeWizard.tsx:71`: `"Error al crear el Archivos."` → "Error al crear el archivos."
- `TaskConfigModal.tsx:57`: `"Error al exportar la Tarea Competencial."` → "Error al exportar la tarea competencial."
- `UdConfigModal.tsx:56`: `"Error al exportar la Unidad didáctica."` → "Error al exportar la unidad didáctica."

---

## 3. Excepciones válidas (NO cambiar)

- Siglas: FP, FEOE, IA, DEMO, PDF, PDEvC, BOE, BOA, BYOK, API, FCT, FOL, UD, UT, RA, CE, OG
- Nombres propios: Google, OpenAI, ChatGPT, Gemini, OneDrive, Drive, Moodle, Classroom
- Títulos de documentos: "INFORME DE EVALUACIÓN" (mayúsculas deliberadas)
- Una sola palabra con mayúscula inicial: correcto en español

---

## 4. Otros locales pendientes

- `ca.json` (catalán): Revisar
- `va.json` (valenciano): Revisar
- `eu.json` (euskera): Revisar
- `gl.json` (gallego): Revisar
- `ba.json` (bable): Revisar
- `en.json` (inglés): NO tocar (Title Case es correcto en inglés)

---

## 5. Correcciones adicionales (re-auditoría 24 julio 2026)

### `title=` attributes adicionales corregidos
| Archivo | Corrección |
|---------|-----------|
| `documentos/page.tsx` | "PDF Preview" → "Vista previa PDF" |
| `informes/page.tsx` | "PDF Preview" → "Vista previa PDF" |
| `magia/page.tsx` | "PDF Preview" → "Vista previa PDF" |
| `archivos/page.tsx` | "Crea un curso y su archivo Grupo asociado" → "...grupo asociado" |
| `archivos/page.tsx` | "Curso Importado" → "Curso importado" (string visible) |

### Verificación final (24 julio 2026)
- Búsqueda `[A-Z][a-z]+ [A-Z][a-z]` en todos los `.tsx`: solo quedan excepciones válidas (siglas FEOE, IA, PDF, CE + marcas Google/Drive)
- Build Next.js: ✅ 22 rutas, 0 errores
