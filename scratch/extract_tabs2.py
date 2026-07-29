import os, re
files_to_check = ['contexto/page.tsx', 'metodologia/page.tsx', 'evaluacion/page.tsx', 'secuenciacion/page.tsx', 'calendario/page.tsx', 'alumnado/page.tsx', 'diario/page.tsx', 'seguimiento/page.tsx', 'calificaciones/page.tsx', 'curriculo/page.tsx', 'informes/page.tsx', 'magia/page.tsx']
for f in files_to_check:
    path = os.path.join('frontend/src/app', f)
    if os.path.exists(path):
        with open(path, encoding='utf8') as fin:
            content = fin.read()
        match = re.search(r'const TABS\s*=\s*\[(.*?)\];', content, re.DOTALL)
        if match:
            ids = re.findall(r'id:\s*[\'\"\`]([^\'\"\`]+)[\'\"\`]', match.group(1))
            labels = re.findall(r'label:\s*(?:t\([\`\'\"]|[\`\'\"])([^\`\'\"\)]+)', match.group(1))
            print(f'{f}: {list(zip(ids, labels))}')
        else:
            print(f'{f}: No TABS found')
