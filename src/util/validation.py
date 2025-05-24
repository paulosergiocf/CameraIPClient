
class Validation:
    
    @staticmethod
    def string(entry: str, size: int) -> str:
        if (len(entry.strip())) <= 0:
            raise ValueError("Entrada vazia")

        return entry

    @staticmethod
    def integer(entry: str) -> int:
        if (len(entry.strip())) <= 0:
            raise ValueError("Entrada vazia")
        
        return int(entry)