from dataclasses import asdict, dataclass
from pathlib import Path

from pydantic import ValidationError

from schemas import FileOutput, ScanRequest, ScanResponse


@dataclass
class FileInfo:
    name: str
    suffix: str
    size: int


def scan(raw_input: dict[str, object]) -> ScanResponse:
    request = ScanRequest.model_validate(raw_input)

    directory = Path(request.directory)
    file_infos = list_files(directory)[: request.max_files]

    output_files = [FileOutput(**asdict(file_info)) for file_info in file_infos]

    return ScanResponse(
        directory=str(directory),
        total_files=len(output_files),
        files=output_files,
    )


def describe_file(file_path: Path):
    return FileInfo(
        name=file_path.name,
        suffix=file_path.suffix or "uzantısız",
        size=file_path.stat().st_size,
    )


def list_files(directory_path: Path) -> list[FileInfo]:
    """
    This function lists all files in a directory.
    """
    if not directory_path.exists():
        raise FileNotFoundError(f"Directory {directory_path} does not exist")
    if not directory_path.is_dir():
        raise NotADirectoryError(f"Path {directory_path} is not a directory")

    files = []

    for path in directory_path.iterdir():
        if path.is_file():
            files.append(describe_file(path))

    return files


def main() -> None:
    # sample_directory = Path(__file__).parent / "sample_files"
    sample_directory = ""

    raw_input = {
        "directory": str(sample_directory),
        "max_files": 100,
    }

    try:
        response = scan(raw_input)
        print(response.model_dump_json(indent=2))
    except ValidationError as error:
        print(f"Validation error: {error}")
        print(f"Invalid input: {raw_input}")
    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"Klasör Hatası: {error}")


if __name__ == "__main__":
    main()
