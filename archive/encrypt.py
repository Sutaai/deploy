import pathlib
import subprocess

import pathspec
from pathspec.patterns.gitignore.spec import GitIgnoreSpecPattern

root = pathlib.Path(__file__).parent.resolve()
gitignore = root / ".gitignore"

ignore_lines = [line for line in gitignore.read_text().splitlines() if line != ""]
spec = pathspec.GitIgnoreSpec.from_lines([".git", *ignore_lines])

files = [
    pathlib.Path(path.path).resolve()
    for path in spec.match_tree_entries(root)
]

count = 0
for file in files:
    if file.name.startswith("decrypted."):
        print(f"Encrypting {file.relative_to(root)}...")
        subprocess.run(
            [
                "age",
                "--encrypt",
                "--identity",
                "keys/private/sutaai-desktop.key.txt",
                "--recipients-file",
                str(root / "keys" / "public" / "recipients.txt"),
                "--output",
                file.relative_to(root).with_name(
                    f"{file.name.lstrip('decrypted.')}.age"
                ),
                file.resolve(),
            ]
        )
        file.unlink()
        count += 1

print(f"Done. {count} files encrypted total.")
