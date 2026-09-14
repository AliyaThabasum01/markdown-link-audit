# 🔗 Markdown Link Audit

A lightweight Python CLI tool that scans Markdown files for empty or incomplete Markdown links.

## Features

- Scan Markdown files
- Detect empty link text
- Detect empty URLs
- Simple CLI interface
- No external dependencies

## Run

```bash
python main.py
```

## Example

For:

```markdown
[GitHub](https://github.com)

[](https://example.com)

[Broken]()
```

The tool reports:

```text
⚠️ Problems found:
- Empty link text
- Empty URL for: [Broken]
```

## Built With

- Python
- Regular Expressions
- File Handling
