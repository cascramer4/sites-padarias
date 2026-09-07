import os

BASE_DIR = r"E:\SANTINI DIGITAL\MARKETING\pages\SITES PADARIAS"

old_digits = "5511999999999"
new_digits = "5511999999999"

old_display = "(11) 99999-9999"
new_display = "(11) 99999-9999"

modified_count = 0

for root, dirs, files in os.walk(BASE_DIR):
    if ".git" in root:
        continue
    for f in files:
        if f.endswith(".html") or f.endswith(".py"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            needs_update = False
            if old_digits in content or old_display in content or "(11) 99999-9999" in content:
                content = content.replace(old_digits, new_digits)
                content = content.replace("(11) 99999-9999", new_display)
                content = content.replace(old_display, new_display)
                needs_update = True
            
            if needs_update:
                with open(fpath, "w", encoding="utf-8") as file:
                    file.write(content)
                modified_count += 1

print(f"Substituído com sucesso em {modified_count} arquivos!")
