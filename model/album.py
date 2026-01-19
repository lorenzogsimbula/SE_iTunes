from dataclasses import dataclass

@dataclass
class Album:
    id: int
    title: str
    artist_id: int
    duration: float

    def __str__(self):
        return f'(-{self.title}({self.durata}))'

    def __repr__(self):
        return f'{self.title}({self.durata})'

    def __hash__(self):
        return hash(self.id)
