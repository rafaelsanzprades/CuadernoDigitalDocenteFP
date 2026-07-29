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
            
            # 1. Update MotionWrapper
            # Some are <MotionWrapper className="space-y-4 pb-12">
            # Some might have other classes. Let's just find <MotionWrapper ... pb-12"> or similar
            new_content = re.sub(
                r'<MotionWrapper className="[^"]*space-y-\d+([^"]*)"',
                r'<MotionWrapper className="flex flex-col gap-4\1"',
                new_content
            )
            # if they had no space-y, but we still want them to be flex flex-col gap-4
            new_content = re.sub(
                r'<MotionWrapper>',
                r'<MotionWrapper className="flex flex-col gap-4 pb-12">',
                new_content
            )

            # 2. Update the Title Block div. Find <div> immediately preceding <h1 className="text-2xl font-bold tracking-tight
            # We must be careful not to match other divs.
            new_content = re.sub(
                r'(<div[^>]*>)\s*<h1 className="text-2xl font-bold tracking-tight',
                r'<div className="flex flex-col gap-4">\n              <h1 className="text-2xl font-bold tracking-tight',
                new_content
            )
            # Also handle variations like font-extrabold or text-lg
            new_content = re.sub(
                r'(<div[^>]*>)\s*<h1 className="text-lg font-extrabold',
                r'<div className="flex flex-col gap-4">\n              <h1 className="text-2xl font-bold tracking-tight',
                new_content
            )
            new_content = re.sub(
                r'(<div[^>]*>)\s*<h1 className="text-2xl font-extrabold',
                r'<div className="flex flex-col gap-4">\n              <h1 className="text-2xl font-bold tracking-tight',
                new_content
            )
            
            # Remove any mb-* from the h1 itself
            new_content = re.sub(r'<h1 className="([^"]*)mb-\d+([^"]*)"', r'<h1 className="\1\2"', new_content)
            
            # 3. Clean up Subtitle <p>
            new_content = re.sub(
                r'<p className="text-muted mt-\d+([^"]*)">',
                r'<p className="text-muted\1">',
                new_content
            )

            # 4. Remove mb-* from Tabs component
            new_content = re.sub(
                r'<Tabs([^>]*)className="([^"]*)mb-\d+([^"]*)"',
                r'<Tabs\1className="\2\3"',
                new_content
            )

            # 5. Overwrite TabsList completely
            new_content = re.sub(
                r'<TabsList className="[^"]*">',
                r'<TabsList className="max-w-full flex-wrap h-auto gap-1">',
                new_content
            )

            # 6. Info box clean up (remove mb-6 mt-4, just keep standard padding)
            new_content = re.sub(
                r'<div className="flex items-start gap-3 p-4 rounded-xl bg-accent/5 border border-accent/20[^"]*">',
                r'<div className="flex items-start gap-3 p-4 rounded-xl bg-accent/5 border border-accent/20">',
                new_content
            )
            # Also handle single quotes
            new_content = re.sub(
                r"<div className='flex items-start gap-3 p-4 rounded-xl bg-accent/5 border border-accent/20[^']*'>",
                r'<div className="flex items-start gap-3 p-4 rounded-xl bg-accent/5 border border-accent/20">',
                new_content
            )

            # 7. Remove the crossed out text from metodologia
            if "metodologia" in filepath:
                new_content = re.sub(
                    r'para el módulo <strong className="text-foreground">\{activeModuleId\}</strong>\.',
                    r'',
                    new_content
                )
                new_content = new_content.replace('diversidad .', 'diversidad.')
                new_content = new_content.replace('diversidad  .', 'diversidad.')

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
