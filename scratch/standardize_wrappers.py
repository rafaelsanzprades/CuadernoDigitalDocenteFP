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
            
            # 1. Change MotionWrapper from space-y to flex flex-col gap-5
            new_content = re.sub(
                r'<MotionWrapper className="[^"]*space-y-\d+\s+([^"]+)"',
                r'<MotionWrapper className="flex flex-col gap-5 \1"',
                new_content
            )
            # also handle cases without trailing classes
            new_content = re.sub(
                r'<MotionWrapper className="space-y-\d+"',
                r'<MotionWrapper className="flex flex-col gap-5"',
                new_content
            )

            # 2. Add flex-col gap-5 to the div wrapping the h1 and p
            # Match <div> or <div className="..."> right before <h1
            # We must be careful. Let's just find the h1 and its previous div.
            # A safer regex: find <div>\s*<h1 className="text-2xl
            new_content = re.sub(
                r'<div>\s*<h1 className="text-2xl font-extrabold',
                r'<div className="flex flex-col gap-5">\n              <h1 className="text-2xl font-extrabold',
                new_content
            )

            # 3. Remove any mt-4 or mt-2 from the subtitle p tag to let gap handle it
            new_content = re.sub(
                r'<p className="text-muted mt-\d+ text-sm">',
                r'<p className="text-muted text-sm">',
                new_content
            )

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
