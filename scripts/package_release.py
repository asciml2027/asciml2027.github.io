#!/usr/bin/env python3
"""Package portable Jekyll source and an optional prebuilt HTML preview."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-dir", type=Path)
    parser.add_argument(
        "--output", type=Path,
        default=root / "downloads" / "asian-sciml-2027-jekyll.zip",
    )
    args = parser.parse_args()
    skip_dirs = {
        ".git", ".openai", ".bundle", ".jekyll-cache", ".sass-cache",
        "__pycache__", "_site", "dist", "preview", "downloads", "vendor", "node_modules",
    }
    skip_names = {"_config.preview.yml", ".jekyll-metadata", ".DS_Store"}
    preview = args.preview_dir.resolve() if args.preview_dir else None
    if preview and not (preview / "index.html").is_file():
        parser.error("--preview-dir must contain a complete Jekyll build with index.html")
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    prefix = "asian-sciml-2027"
    with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(root.rglob("*")):
            relative = path.relative_to(root)
            if not path.is_file() or path.is_symlink() or path.resolve() == output:
                continue
            if any(part in skip_dirs for part in relative.parts) or path.name in skip_names:
                continue
            if path.suffix == ".log":
                continue
            archive.write(path, f"{prefix}/{relative.as_posix()}")
        if preview:
            for path in sorted(preview.rglob("*")):
                relative = path.relative_to(preview)
                if path.is_file() and not path.is_symlink() and "downloads" not in relative.parts:
                    archive.write(path, f"{prefix}/preview/{relative.as_posix()}")
    print(f"Created {output} ({output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()

