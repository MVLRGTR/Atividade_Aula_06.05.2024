class ListaCompras:
    def __init__(self, nome: str, itens: List[str]):
        self._nome = nome
        self._itens = itens

    def getNome(self):
        return self._nome

    def getitens(self):
        return self._itens

    def setNome(self, nome: str):
        self._nome = nome

    def setitens(self, itens: List[str]):
        self._itens = itens