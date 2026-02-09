class Libro:
    def __init__(self, titulo, author, paginas):
        self.titulo = titulo
        self.author = author
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} escrito por: {self.author}"

    def __len__(self):
        return self.paginas


libro = Libro(
    titulo="IT Chapter I",
    author="Stephen King",
    paginas=1489
)

print(libro)
print(len(libro))
