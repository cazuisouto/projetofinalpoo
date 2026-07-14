from DAO import DAO

class Medicamentos:
    def __init__(self, id, nome, descricao, quantidade, unidade_medida):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_quantidade(quantidade)
        self.set_unidade_medida(unidade_medida)

    def get_id(self):              return self.__id
    def get_nome(self):            return self.__nome
    def get_descricao(self):       return self.__descricao
    def get_quantidade(self):      return self.__quantidade
    def get_unidade_medida(self):  return self.__unidade_medida

    def set_id(self, id):
        if (id > -1) and (id == int(id)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")
        
    def set_nome(self, nome):
        if (nome != "") and (isinstance(nome, str)):
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser do tipo string e não pode ser vazio.")
        
    def set_descricao(self, descricao):
        if (descricao != "") and (isinstance(descricao, str)):
            self.__descricao = descricao
        else:
            raise ValueError("Descrição deve ser do tipo string e não pode ser vazia.")
        
    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            raise ValueError("Quantidade deve ser um número inteiro não negativo.")
        
    def set_unidade_medida(self, unidade_medida):
        if isinstance(unidade_medida, str) and (len(unidade_medida) > 0):
            self.__unidade_medida = unidade_medida
        else:
            raise ValueError("A unidade de medida deve ser do tipo str e tem que ter mais que um caractere")

    def __str__(self):
        return f"ID: {self.get_id()} - Nome: {self.get_nome()} - Descrição: {self.get_descricao()} - Quantidade: {self.get_quantidade()} - Unidade de Medida: {self.get_unidade_medida()}"
    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "descricao": self.get_descricao(),
            "quantidade": self.get_quantidade(),
            "unidade_medida": self.get_unidade_medida()
        }

    @staticmethod    
    def from_json(dic):
        return Medicamentos(dic["id"], dic["nome"], dic["descricao"], dic["quantidade"], dic["unidade_medida"])
    
class MedicamentosDAO(DAO):
    def __init__(self):
        super().__init__(Medicamentos, "Data/mendicamentos.json")
