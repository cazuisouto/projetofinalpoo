from Models.DAO import DAO

class Doenca:
    def __init__(self, id, nome):
        self.set_id(id)
        self.set_nome(nome)

    def get_id(self):          return self.__id
    def get_nome(self):        return self.__nome

    def set_id(self,id):
        if (id > -1) and (id == int(id)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")
    
    def set_nome(self, nome):
        if (nome != "") and (isinstance(nome, str)):
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser do tipo string e não pode ser vazio.")
    
    def __str__(self):
        return f"ID: {self.get_id()} - Nome: {self.get_nome()}"
    
    def to_json(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome()
        }
    
    @staticmethod
    def from_json(dic):
        return Doenca(dic["id"], dic["nome"])
    
class DoencaDAO(DAO):
    def __init__(self):
        super().__init__(Doenca, "Data/doencas.json")
