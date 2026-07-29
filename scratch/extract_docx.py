import zipfile
import xml.etree.ElementTree as ET
import sys

docx_path = r'c:\GD-rsp\APP-CuadernoFP\RF Ideas\PD+ FP v1 - Ejemplo.docx'

try:
    z = zipfile.ZipFile(docx_path)
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = tree.findall('.//w:p', nsmap)
    
    output = []
    for i, p in enumerate(paragraphs):
        texts = []
        for r in p.findall('.//w:r', nsmap):
            for t in r.findall('.//w:t', nsmap):
                if t.text:
                    texts.append(t.text)
        line = ''.join(texts).strip()
        if line:
            output.append(f'{i:4d}: {line}')
    
    # Write to file instead of stdout
    with open(r'c:\GD-rsp\APP-CuadernoFP\temp_headings.txt', 'w', encoding='utf-8') as f:
        f.write(f'Total paragraphs: {len(paragraphs)}\n')
        f.write(f'Text paragraphs: {len(output)}\n\n')
        for line in output:
            f.write(line[:300] + '\n')
    
    print(f'Done. {len(output)} text paragraphs written to temp_headings.txt')
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
    import traceback
    traceback.print_exc()
