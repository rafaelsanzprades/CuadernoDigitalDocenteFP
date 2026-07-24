Get-ChildItem -Recurse -Include *.tsx -Path 'frontend\src\components','frontend\src\app' |
  Where-Object { $_.FullName -notmatch 'node_modules|\.next' } |
  ForEach-Object {
    $file = $_.Name
    $lines = Get-Content $_.FullName
    for ($i = 0; $i -lt $lines.Count; $i++) {
      $line = $lines[$i]
      if ($line -match '(>[\s]*[A-Z][a-z]+ [A-Z]|title="[A-Z][a-z]+ [A-Z]|placeholder="[A-Z][a-z]+ [A-Z]|aria-label="[A-Z][a-z]+ [A-Z]|toast\.\w+\("[A-Z][a-z]+ [A-Z]|label="[A-Z][a-z]+ [A-Z])' -and
          $line -notmatch 'className|import |from |const |//|interface|type ') {
        $short = $line.Trim()
        if ($short.Length -gt 140) { $short = $short.Substring(0, 140) }
        Write-Output "$file`:$($i+1): $short"
      }
    }
  }
