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
            
            # Fix subtitle margin (mt-2 -> mt-4)
            new_content = re.sub(
                r'className="text-muted mt-2 text-sm"',
                r'className="text-muted mt-4 text-sm"',
                new_content
            )

            # Fix info box margins (remove mb-6 mt-4)
            new_content = re.sub(
                r'border-accent/20 mb-6 mt-4"',
                r'border-accent/20"',
                new_content
            )

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
