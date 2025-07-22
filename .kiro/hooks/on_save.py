# .kiro/hooks/on_save.py
from kiro import Kiro
import os
import pathlib

def detect_language(file_path):
    ext = pathlib.Path(file_path).suffix
    return {
        ".py": "python",
        ".js": "javascript"
    }.get(ext, None)

def on_file_save(file_path):
    language = detect_language(file_path)
    if not language:
        return
    
    kiro = Kiro(spec="docs.yaml")
    code = open(file_path).read()
    
    # Generate docs
    prompt = f"Generate {language} docs for this code:\n{code}"
    docs = kiro.generate(prompt)
    
    # Save alongside original file
    output_path = f"{file_path}.docs.md"
    with open(output_path, "w") as f:
        f.write(f"# Documentation for {file_path}\n\n{docs}")