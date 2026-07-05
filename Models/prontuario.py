from DAO import DAO
from datetime import datetime

class Prontuario:
    def __init__(self, id, id_pet, id_doenca, data_entrada, data_saida, status):
        self.set_id(id) 
        self.set_id_pet(id_pet)
        self.set_id_doenca(id_doenca)
        self.set_data_entrada(data_entrada)
        self.set_data_saida(data_saida)
        self.set_status(status)

    def get_id(self):              return self.__id
    def get_id_pet(self):          return self.__id_pet
    def get_id_doenca(self):       return self.__id_doenca
    def get_data_entrada(self):    return self.__data_entrada
    def get_data_saida(self):      return self.__data_saida
    def get_status(self):     return self.__status


    def set_id(self, id):
        if (id > -1) and (id == int(id)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")

    def set_id_pet(self, id_pet):
        if (id_pet > -1) and (id_pet == int(id_pet)):
            self.__id_pet = id_pet
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")

    def set_id_doenca(self, id_doenca):
        if (id_doenca > -1) and (id_doenca == int(id_doenca)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")

    def set_data_entrada(self, data_entrada):

        try: 
            data_convertida = datetime.strptime(data_entrada, '%d/%m/%Y')
            self.__data_entrada = data_convertida
        except:
            raise ValueError("Data de entrada inválida.")

    def set_data_saida(self, data_saida):
        try: 
            data_convertida = datetime.strptime(data_saida, '%d/%m/%Y')
            self.__data_saida = data_convertida
        except:
            raise ValueError("Data de entrada inválida.")

    def set_status(self, status):
        status = status.lower()
        opcoes_validas = ["liberado", "interno", "finalizado"]

        if status in opcoes_validas:
            self.__status = status
        else:
            raise ValueError("Status inválido. Opções válidas: 'liberado', 'interno', 'finalizado'.")
    
    def __str__(self):
        return f"ID: {self.get_id()} - ID Pet: {self.get_id_pet()} - ID Doença: {self.get_id_doenca()} - Data de Entrada: {self.get_data_entrada().strftime('%d/%m/%Y')} - Data de Saída: {self.get_data_saida().strftime('%d/%m/%Y')} - Status: {self.get_status()}"
    
    def to_json(self):
        return {
            "id": self.get_id(),
            "id_pet": self.get_id_pet(),
            "id_doenca": self.get_id_doenca(),
            "data_entrada": self.get_data_entrada().strftime('%d/%m/%Y'),
            "data_saida": self.get_data_saida().strftime('%d/%m/%Y'),
            "status": self.get_status()
        }
    
    @staticmethod
    def from_json(dic):
        return Prontuario(dic["id"], dic["id_pet"], dic["id_doenca"], dic["data_entrada"], dic["data_saida"], dic["status"])
    

class ProntuarioDAO(DAO):
    def __init__(self):
        super().__init__(Prontuario, "Data/prontuario.json")