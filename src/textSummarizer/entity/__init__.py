from dataclasses import dataclass
from pathlib import Path

# entity - a class that is used to store the configuration of the project
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path