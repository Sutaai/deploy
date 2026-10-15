from pathlib import Path

scriptdir = Path(__file__).parent.resolve()

recipients: dict[str, str] = {}

for file in scriptdir.joinpath("public").iterdir():
    if file.name != "recipients.txt":
        recipients[file.stem] = file.read_text()

scriptdir.joinpath("public", "recipients.txt").write_text(
    "\n".join(f"# {k}\n{v}" for k, v in recipients.items())
)

print(f"Recipients updated. Total: {len(recipients)}")
