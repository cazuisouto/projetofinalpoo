from Models.DAO import DAO

class Aplicacao:
    def __init__(self, id, id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status):
        self.set_id(id)
        self.set_id_prontuario(id_prontuario)
        self.set_id_medicamento(id_medicamento)
        self.set_id_veterinario(id_veterinario)
        self.set_id_auxiliar(id_auxiliar)
        self.set_dose_prescrita(dose_prescrita)
        self.set_instrucoes(instrucoes)
        self.set_status(status)
    
    def get_id(self):                return self.__id
    def get_id_prontuario(self):     return self.__id_prontuario
    def get_id_medicamento(self):    return self.__id_medicamento
    def get_id_veterinario(self):    return self.__id_veterinario
    def get_id_auxiliar(self):       return self.__id_auxiliar
    def get_dose_prescrita(self):    return self.__dose_prescrita
    def get_instrucoes(self):        return self.__instrucoes
    def get_status(self):            return self.__status

    def set_id(self, id):
        if (id > -1) and (id == int(id)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")
    
    def set_id_prontuario(self, id_prontuario):
        if (id_prontuario > -1) and (id_prontuario == int(id_prontuario)):
            self.__id_prontuario = id_prontuario
        else:
            raise ValueError("ID do prontuário deve ser um número inteiro positivo.")

    def set_id_medicamento(self, id_medicamento):
        if (id_medicamento > -1) and (id_medicamento == int(id_medicamento)):
            self.__id_medicamento = id_medicamento
        else:
            raise ValueError("ID do medicamento deve ser um número inteiro positivo.")

    def set_id_veterinario(self, id_veterinario):
        if (id_veterinario > -1) and (id_veterinario == int(id_veterinario)):
            self.__id_veterinario = id_veterinario
        else:
            raise ValueError("ID do veterinário deve ser um número inteiro positivo.")

    def set_id_auxiliar(self, id_auxiliar):
        if (id_auxiliar > -1) and (id_auxiliar == int(id_auxiliar)):
            self.__id_auxiliar = id_auxiliar
        else:
            raise ValueError("ID do auxiliar deve ser um número inteiro positivo.")

    def set_dose_prescrita(self, dose_prescrita):
        if (dose_prescrita > 0) and (dose_prescrita == float(dose_prescrita)):
            self.__dose_prescrita = dose_prescrita
        else:
            raise ValueError("Dose prescrita deve ser um número real positivo.")

    def set_instrucoes(self, instrucoes):
        if isinstance(instrucoes, str) and len(instrucoes) > 0:
            self.__instrucoes = instrucoes
        else:
            raise ValueError("Instruções devem ser uma string não vazia.")

    def set_status(self, status):
        status = status.lower()
        opcoes_validas = ["cancelado", "pendente", "finalizado"]

        if status in opcoes_validas:
            self.__status = status
        else:
            raise ValueError("Status inválido. Opções válidas: 'cancelado', 'em andamento', 'finalizado'.")
        
    def __str__(self):
        return f"ID: {self.get_id()} - ID Prontuário: {self.get_id_prontuario()} - ID Medicamento: {self.get_id_medicamento()} - ID Veterinário: {self.get_id_veterinario()} - ID Auxiliar: {self.get_id_auxiliar()} - Dose Prescrita: {self.get_dose_prescrita()} - Instruções: {self.get_instrucoes()} - Status: {self.get_status()}"
    
    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        return {
            "id": self.get_id(),
            "id_prontuario": self.get_id_prontuario(),
            "id_medicamento": self.get_id_medicamento(),
            "id_veterinario": self.get_id_veterinario(),
            "id_auxiliar": self.get_id_auxiliar(),
            "dose_prescrita": self.get_dose_prescrita(),
            "instrucoes": self.get_instrucoes(),
            "status": self.get_status()
        }
    
    @staticmethod
    def from_json(dic):
        return Aplicacao(
            dic["id"],
            dic["id_prontuario"],
            dic["id_medicamento"],
            dic["id_veterinario"],
            dic["id_auxiliar"],
            dic["dose_prescrita"],
            dic["instrucoes"],
            dic["status"]
        )
    
class AplicacaoDAO(DAO):
    def __init__(self):
        super().__init__(Aplicacao, "Data/aplicacoes.json")