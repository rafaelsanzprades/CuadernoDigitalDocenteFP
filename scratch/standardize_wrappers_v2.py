import os
import re

app_dir = r"c:\GD-rsp\APP-CuadernoFP\frontend\src\app"

for root, dirs, files in os.walk(app_dir):
    for file in files:
        if file.endswith(".tsx"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            
            # 1. Update MotionWrapper to flex-col gap-6 (instead of gap-5)
            new_content = re.sub(
                r'<MotionWrapper className="flex flex-col gap-5([^"]*)"',
                r'<MotionWrapper className="flex flex-col gap-6\1"',
                new_content
            )

            # 2. Update the Title Block div from gap-5 to gap-2
            new_content = re.sub(
                r'<div className="flex flex-col gap-5">\s*<h1',
                r'<div className="flex flex-col gap-2">\n              <h1',
                new_content
            )

            # 3. Remove hardcoded mb-8 or mb-6 on Tabs
            new_content = re.sub(
                r'<Tabs([^>]*)className="([^"]*)mb-8([^"]*)"',
                r'<Tabs\1className="\2\3"',
                new_content
            )
            # clean up empty className or double spaces
            new_content = re.sub(r'className="\s+"', '', new_content)
            new_content = re.sub(r'className="([^"]*)\s{2,}([^"]*)"', r'className="\1 \2"', new_content)

            # 4. Remove the specific crossed out text from metodologia
            if "metodologia" in filepath:
                new_content = re.sub(
                    r'para el módulo <strong className="text-foreground">\{activeModuleId\}</strong>\.',
                    r'',
                    new_content
                )
                # Trim trailing space
                new_content = new_content.replace('diversidad .', 'diversidad.')
                new_content = new_content.replace('diversidad  .', 'diversidad.')

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
