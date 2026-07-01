from DAO import DAO

class Pet:
    def __init__(self, id, nome, especie, raca, idade, tutor):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especie(especie)
        self.set_raca(raca)
        self.set_idade(idade)
        self.set_tutor(tutor)

    def get_id(self):              return self.__id
    def get_nome(self):            return self.__nome
    def get_especie(self):         return self.__especie
    def get_raca(self):            return self.__raca
    def get_idade(self):           return self.__idade
    def get_tutor(self):           return self.__tutor
    

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
        
    def set_especie(self, especie):
        if isinstance(especie, str):
            self.__especie = especie
        else:
            raise ValueError("O nome precisa ser do tipo str")
    
    def set_raca(self, raca):
        if isinstance(raca, str):
            self.__raca = raca
        else:
            raise ValueError("O nome precisa ser do tipo str")
        
    def set_idade(self, idade):
        if isinstance(idade, int):
            self.__idade = idade
        else:
            raise ValueError("O nome precisa ser do tipo inteiro")

    def set_tutor(self, tutor):
        if isinstance(tutor, str):
            self.__tutor = tutor
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")
        

    def __str__(self):
        return f"ID: {self.get_id()} - Nome: {self.get_nome()} - Especie: {self.get_especie()} - Raça: {self.get_raca()} - Idade: {self.get_idade()} - Tutor: {self.get_tutor()}"
    
    def to_json(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "especie": self.get_especie(),
            "raça": self.get_raca(),
            "idade": self.get_idade(),
            "id_cliente": self.get_tutor()
        }
    
    staticmethod    
    def from_json(dic):
        return Pet(dic["id"], dic["nome"], dic["especie"], dic["raça"], dic["idade"], dic["tutor"])
    
class PetDAO(DAO):
    def __init__(self):
        super().__init__(Pet, "Data/pets.json")