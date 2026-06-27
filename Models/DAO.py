import json

class DAO:
    def __init__(self, classe, arquivo):
        self._objetos = []
        self.__classe = classe
        self.__arquivo = arquivo

    def inserir(self, obj):
        self.abrir()
        if len(self._objetos) == 0: id = 1
        else: id = (max(self._objetos, key = lambda x : x.get_id())).get_id() + 1
        obj.set_id(id)
        self._objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        return self._objetos

    def listar_id(self, id):
        self.abrir()
        for obj in self._objetos:
            if obj.get_id() == id: return obj
        return None        

    def atualizar(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self._objetos.remove(x)
            self._objetos.append(obj)
            self.salvar()

    def excluir(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self._objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(self._objetos, arquivo, default = self.__classe.to_json, indent=4)

    def abrir(self):
        self._objetos = []
        try:
            with open(self.__arquivo, mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = self.__classe.from_json(dic)
                    self._objetos.append(c)
        except FileNotFoundError:
            self._objetos = []