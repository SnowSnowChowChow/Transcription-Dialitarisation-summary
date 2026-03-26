import json
import re

file_path = "pipeline_transcription.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# On parcourt les cellules pour trouver celle qui définit HF_TOKEN
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        new_source = []
        for line in source:
            # On cherche la ligne HF_TOKEN
            if "HF_TOKEN" in line and "=" in line:
                    # Remplacer par os.getenv
                    new_line = re.sub(r'HF_TOKEN\s*=\s*".*?"', "HF_TOKEN           = os.getenv('HF_TOKEN')", line)
                    new_source.append(new_line)
            else:
                new_source.append(line)
        cell["source"] = new_source

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook mis à jour pour lire HF_TOKEN depuis l'environnement !")
