from dataclasses import dataclass
from pathlib import Path


@dataclass
class FileInfo:
    name: str
    suffix: str
    size_bytes: int


def describe_file(path: Path) -> FileInfo:
    return FileInfo(
        name=path.name,
        suffix=path.suffix or "(uzantısız)",
        size_bytes=path.stat().st_size,
    )


def list_files(directory: Path) -> list[FileInfo]:
    if not directory.exists():
        raise FileNotFoundError(f"Klasör bulunamadı: {directory}")

    if not directory.is_dir():
        raise NotADirectoryError(f"Bu bir klasör değil: {directory}")

    files = []

    for path in directory.iterdir():
        if path.is_file():
            files.append(describe_file(path))

    return files


def main() -> None:
    sample_directory = Path(__file__).parent / "sample_files"
    files = list_files(sample_directory)

    for file_info in files:
        print(f"{file_info.name} | {file_info.suffix} | {file_info.size_bytes} byte")


if __name__ == "__main__":
    main()
