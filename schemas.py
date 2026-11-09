from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    directory: str = Field(min_length=1, max_length=255)
    max_files: int = Field(default=100, ge=1, le=500)


class FileOutput(BaseModel):
    name: str
    suffix: str
    size: int = Field(ge=0)


class ScanResponse(BaseModel):
    directory: str
    total_files: int = Field(ge=0)
    files: list[FileOutput]


class AskRequest(BaseModel):
    question: str
    instructions: str
