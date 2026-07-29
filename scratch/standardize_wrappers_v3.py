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
            
            # 1. Update MotionWrapper to flex-col gap-4
            new_content = re.sub(
                r'<MotionWrapper className="flex flex-col gap-\d+([^"]*)"',
                r'<MotionWrapper className="flex flex-col gap-4\1"',
                new_content
            )

            # 2. Update the Title Block div from gap-2 or gap-5 to gap-4
            new_content = re.sub(
                r'<div className="flex flex-col gap-\d+">\s*<h1',
                r'<div className="flex flex-col gap-4">\n              <h1',
                new_content
            )

            # 3. Strip mb-8, mb-6, mb-4, mt-4 from all <Tabs> tags
            # We use a loop to repeatedly clean up margins inside <Tabs ... className="...">
            def remove_margins(match):
                before = match.group(1)
                class_content = match.group(2)
                after = match.group(3)
                
                # Remove margin classes
                class_content = re.sub(r'\b(mb-\d+|mt-\d+|my-\d+)\b', '', class_content)
                # Cleanup spaces
                class_content = re.sub(r'\s+', ' ', class_content).strip()
                
                return f'<Tabs{before}className="{class_content}"{after}'

            # Using re.DOTALL to match across newlines inside Tabs tag
            new_content = re.sub(r'<Tabs(.*?)className="([^"]*)"(.*?)>', remove_margins, new_content, flags=re.DOTALL)
            
            # Cleanup any empty classNames created by the above
            new_content = re.sub(r'className=""\s*', '', new_content)

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
