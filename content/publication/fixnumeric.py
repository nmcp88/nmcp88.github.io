import yaml
from pathlib import Path

CSL_TO_NUMERIC = {
    "article-journal": "1",
    "paper-conference": "2",
    "book": "3",
    "book-chapter": "4",
    "thesis": "5",
    "report": "6",
    "other": "7",
}

def fix_publication_types(folder):
    files_fixed = 0
    for file in Path(folder).rglob("*.md"):
        try:
            content = file.read_text()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    fm = yaml.safe_load(parts[1])
                    pt = fm.get("publication_types", [])
                    if isinstance(pt, list) and pt:
                        original_type = pt[0]
                        numeric_type = CSL_TO_NUMERIC.get(original_type)
                        if numeric_type:
                            fm["publication_types"] = [numeric_type]
                            parts[1] = yaml.dump(fm, sort_keys=False)
                            file.write_text("---\n" + parts[1] + "---" + parts[2])
                            print(f"✅ Fixed: {file} ({original_type} → {numeric_type})")
                            files_fixed += 1
        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

    if files_fixed == 0:
        print("ℹ️ No files needed fixing. Either they’re already numeric or weren’t matched.")
    else:
        print(f"🎉 Finished. {files_fixed} files updated.")

# Run in current directory (e.g. inside content/publication/)
if __name__ == "__main__":
    fix_publication_types(".")
