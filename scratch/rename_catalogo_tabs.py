import re

file_path = "frontend/src/app/catalogo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Tab type definition
content = content.replace(
    'type Tab = "familias" | "titulo" | "cursos" | "modulos" | "incual";',
    'type Tab = "familias" | "titulos" | "modulos" | "ra-ce" | "ecp-incual";'
)

# Replace activeTab initialization validation
content = content.replace(
    '["familias", "titulo", "cursos", "modulos", "incual"]',
    '["familias", "titulos", "modulos", "ra-ce", "ecp-incual"]'
)

# Replace setActiveTab and router.replace logic
content = content.replace(
    'setActiveTab("cursos");\n    router.replace(`/catalogo?tab=cursos`',
    'setActiveTab("modulos");\n    router.replace(`/catalogo?tab=modulos`'
)
content = content.replace(
    'setActiveTab("titulo");\n    router.replace(`/catalogo?tab=titulo`',
    'setActiveTab("titulos");\n    router.replace(`/catalogo?tab=titulos`'
)
content = content.replace(
    'setActiveTab("modulos");\n    router.replace(`/catalogo?tab=modulos`',
    'setActiveTab("ra-ce");\n    router.replace(`/catalogo?tab=ra-ce`'
)

# Replace TAB_LABELS keys
content = content.replace('titulo: t(\'tabs.titulos\'', 'titulos: t(\'tabs.titulos\'')
content = content.replace('cursos: t(\'tabs.modulos\'', 'modulos: t(\'tabs.modulos\'')
content = content.replace('modulos: \'RA → CE\'', "'ra-ce': 'RA → CE'")
content = content.replace('incual: "ECP INCUAL"', "'ecp-incual': \"ECP INCUAL\"")

# Replace tabs list definitions
content = content.replace('{ id: "titulo" as Tab', '{ id: "titulos" as Tab')
content = content.replace('{ id: "cursos" as Tab', '{ id: "modulos" as Tab')
content = content.replace('{ id: "modulos" as Tab, label: <span className="flex items-center gap-2"><Layers className="w-4 h-4" /> RA → CE</span> }', '{ id: "ra-ce" as Tab, label: <span className="flex items-center gap-2"><Layers className="w-4 h-4" /> RA → CE</span> }')
content = content.replace('{ id: "incual" as Tab', '{ id: "ecp-incual" as Tab')

# Replace conditional renderings
content = content.replace('activeTab === "titulo"', 'activeTab === "titulos"')
content = content.replace('activeTab === "cursos"', 'activeTab === "modulos"')
# Modulos -> ra-ce (Be careful with this one, need to make sure we don't accidentally replace the new "modulos" we just added)
content = content.replace('activeTab === "modulos" && (', 'activeTab === "ra-ce" && (')
content = content.replace('activeTab === "incual"', 'activeTab === "ecp-incual"')

# Replace infoMap keys
content = content.replace("'titulo': { desc", "'titulos': { desc")
content = content.replace("'cursos': { desc", "'modulos': { desc")
content = content.replace("'modulos': { desc", "'ra-ce': { desc")
content = content.replace("'incual': { desc", "'ecp-incual': { desc")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacements!")
