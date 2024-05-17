class ArmazenamentoDeListas:
    _instance = None

    def __new__(Arm):
        if Arm._instance is None:
            Arm._instance = super().__new__(Arm)
            Arm._listas = []
        return Arm._instance

    def adicionarLista(self, lista: ListaCompras):
        self._listas.append(lista)

    def editarLista(self, index: int, novaLista: ListaCompras):
        self._listas[index] = novaLista

    def removerLista(self, index: int):
        del self._listas[index]

    def listar(self):
        for lista in self._listas:
            print(f"Nome: {lista.getNome()}")
            print(f"Itens: {lista.getitens()}")
            print("-" * 20)
