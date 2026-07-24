# Buscar Title Case en strings visibles al usuario (español)
# Excluye: imports, className, const, type, interface, comentarios
# Incluye: contenido entre > y <, toast.*, title=", placeholder=", aria-label=", label="

$patterns = @(
  # Text between tags: > Some Title Case Text <
  '>([\s]*)([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)\s+([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)',
  # Attributes
  '(title|placeholder|aria-label|label)="([^"]*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+[^"]*)"'
)

$excludePatterns = @('className', 'import ', 'from ', 'const ', '//', 'interface ', 'type ', 'export ', 'function ', 'return ', 'console\.', 'useState', 'useEffect', 'useRef', 'localStorage', 'fetch\(', 'process\.env', 'className=', 'onClick', 'onChange', 'onSubmit', 'variant=', 'w-\d', 'h-\d', 'text-', 'bg-', 'px-', 'py-', 'gap-', 'flex', 'grid', 'items-', 'justify-', 'rounded', 'border', 'shadow', 'space-', 'min-h', 'max-w', 'overflow', 'relative', 'absolute', 'sticky', 'z-\d', 'opacity', 'transition', 'animate', 'cursor', 'select', 'outline', 'ring-', 'font-', 'leading', 'tracking', 'uppercase', 'lowercase', 'truncate', 'line-clamp', 'sr-only', 'dark:', 'hover:', 'focus:', 'active:', 'disabled:', 'first:', 'last:', 'odd:', 'even:', 'sm:', 'md:', 'lg:', 'xl:', '2xl:')

Get-ChildItem -Recurse -Include *.tsx -Path 'frontend\src\components','frontend\src\app' |
  Where-Object { $_.FullName -notmatch 'node_modules|\.next' } |
  ForEach-Object {
    $file = $_.Name
    $relPath = $_.FullName -replace '.*frontend\\src\\', ''
    $lines = Get-Content $_.FullName
    for ($i = 0; $i -lt $lines.Count; $i++) {
      $line = $lines[$i]
      $trimmed = $line.Trim()
      
      # Skip lines that match exclude patterns
      $excluded = $false
      foreach ($ex in $excludePatterns) {
        if ($trimmed -match $ex) { $excluded = $true; break }
      }
      if ($excluded) { continue }
      
      # Check for Title Case in visible text
      if ($trimmed -match '(>[^<]*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+|title="[^"]*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+|placeholder="[^"]*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+|aria-label="[^"]*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+|toast\.\w+\("[^"]*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)') {
        $short = $trimmed
        if ($short.Length -gt 160) { $short = $short.Substring(0, 160) + '...' }
        Write-Output "$relPath`:$($i+1): $short"
      }
    }
  }
