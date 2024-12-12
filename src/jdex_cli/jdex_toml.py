from pathlib import Path
import tomlkit
from tomlkit import toml_file


class JdexToml:
    def __init__(self, doc: tomlkit.TOMLDocument):
        self.doc = doc

    @classmethod
    def new(cls):
        return JdexToml(tomlkit.document())

    @classmethod
    def from_file(cls, config_path: Path):
        if config_path.exists() and config_path.is_file():
            return cls(toml_file.TOMLFile(config_path).read())
        return cls.new()

    def write(self, path: Path):
        toml_file.TOMLFile(path).write(self.doc)

    def __str__(self):
        return tomlkit.dumps(self.doc)
