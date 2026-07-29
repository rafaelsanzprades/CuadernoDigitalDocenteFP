import os, re
for r, d, files in os.walk('frontend/src/app'):
    for f in files:
        if f == 'page.tsx':
            path = os.path.join(r, f)
            with open(path, encoding='utf8') as f_in:
                content = f_in.read()
            match = re.search(r'const TABS\s*=\s*\[(.*?)\];', content, re.DOTALL)
            if match:
                labels = re.findall(r'label:\s*(?:t\()?[\'\"\`]([^\'\"\`]+)[\'\"\`]', match.group(1))
                if labels:
                    print(f"{os.path.basename(r)}: {labels}")
