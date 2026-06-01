from pydantic import BaseModel


class SemanticVersion(BaseModel):
    major: int
    minor: int
    patch: int
    pre_release: str = ""

    @property
    def version_string(self) -> str:
        base = f"{self.major}.{self.minor}.{self.patch}"
        if self.pre_release:
            return f"{base}-{self.pre_release}"
        return base

    @classmethod
    def parse(cls, version_str: str) -> "SemanticVersion":
        parts = version_str.split("-")
        core_parts = parts[0].split(".")
        if len(core_parts) != 3:
            raise ValueError(
                "Invalid semantic version format. Expected MAJOR.MINOR.PATCH"
            )

        return cls(
            major=int(core_parts[0]),
            minor=int(core_parts[1]),
            patch=int(core_parts[2]),
            pre_release=parts[1] if len(parts) > 1 else "",
        )
