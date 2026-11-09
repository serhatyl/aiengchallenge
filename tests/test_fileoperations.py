from pathlib import Path

from file_catalog import describe_file, list_files


def test_describe_file_reads_file_metadata(tmp_path: Path) -> None:
    path = tmp_path / "notlar.txt"
    path.write_text("merhaba", encoding="utf-8")

    info = describe_file(path)

    assert info.name == "notlar.txt"
    assert info.suffix == ".txt"
    assert info.size == 7


def test_list_files(tmp_path: Path) -> None:
    (tmp_path / "notlar.txt").write_text("merhaba dünya", encoding="utf-8")
    (tmp_path / "veri.csv").write_text("a,b", encoding="utf-8")
    (tmp_path / "alt_klasor").mkdir()

    files = list_files(tmp_path)
    names = sorted(file.name for file in files)

    assert names == ["notlar.txt", "veri.csv"]


def test_list_files_returns_empty_list_for_empty_folder(tmp_path: Path) -> None:
    assert list_files(tmp_path) == []
