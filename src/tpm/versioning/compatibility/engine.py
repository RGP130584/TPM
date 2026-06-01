from tpm.versioning.semver.model import SemanticVersion


class CompatibilityEngine:
    @staticmethod
    def is_backward_compatible(v_old: SemanticVersion, v_new: SemanticVersion) -> bool:
        """
        Garante que a nova versão é backward compatible com a velha, assumindo regras strict semver.
        Major changes quebram compatibility.
        """
        if v_new.major > v_old.major:
            return False
        return True
