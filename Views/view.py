from Models.usuario import Usuario, UsuarioDAO
from Models.medicamentos import Medicamentos, MedicamentosDAO
from Models.aplicacao import Aplicacao, AplicacaoDAO
from Models.prontuario import Prontuario, ProntuarioDAO
from Models.doenca import Doenca, DoencaDAO
from Models.pet import Pet, PetDAO
from datetime import datetime

class View:

    # OPERAÇÕES USUÁRIOS: CRUD 

    @staticmethod
    def listar_usuarios():
        return UsuarioDAO().listar()    

    @staticmethod
    def criar_admim():
        for obj in View.listar_usuarios():
            if "admin@abc.com" in obj.get_email(): return
        View.inserir_usuario("Admin", "admin@abc.com", "admin123", "admin" )
    
    @staticmethod
    def autentica_usuario(email, senha):
        usuarios = UsuarioDAO().listar()
        for info in usuarios:
            if (info.get_email() == email) and (info.get_senha() == senha):
                return info.get_id()
        raise ValueError("Usuário ou senha inválidos.")
    
    @staticmethod
    def inserir_usuario(nome, email, senha, funcao):
        u= Usuario(0, nome, email, senha, funcao)
        UsuarioDAO().inserir(u)

    @staticmethod
    def listar_usuario_id(id):
        return UsuarioDAO().listar_id(id)
    
    @staticmethod
    def atualizar_usuario(id, nome, email, senha, funcao):
        u = Usuario(id, nome, email, senha, funcao)
        UsuarioDAO().atualizar(u)

    @staticmethod
    def excluir_usuario(id):
        UsuarioDAO().excluir(id)
    
    @staticmethod
    def listar_usuarios_nome_parcial(nome_parcial):
        todos_usuarios = UsuarioDAO().listar()
        return [u for u in todos_usuarios if nome_parcial.lower() in u.get_nome().lower()]
    
    #OPERAÇÕES MEDICAMENTOS: CRUD

    @staticmethod
    def listar_medicamentos():
        return MedicamentosDAO().listar()
    
    @staticmethod
    def inserir_medicamento(nome, descricao, quantidade, unidade_medida):
        m = Medicamentos(0, nome, descricao, quantidade, unidade_medida)
        MedicamentosDAO().inserir(m)

    @staticmethod
    def listar_medicamento_id(id):
        return MedicamentosDAO().listar_id(id)

    @staticmethod
    def atualizar_medicamento(id, nome, descricao, quantidade, unidade_medida):
        m = Medicamentos(id, nome, descricao, quantidade, unidade_medida)
        MedicamentosDAO().atualizar(m)

    @staticmethod
    def excluir_medicamento(id):
        MedicamentosDAO().excluir(id)
    
    @staticmethod
    def listar_medicamentos_nome_parcial(nome_parcial):
        todos_medicamentos = MedicamentosDAO().listar()
        return [m for m in todos_medicamentos if nome_parcial.lower() in m.get_nome().lower()]
    
    # OPERAÇÕES APLICAÇÃO: CRUD
    @staticmethod
    def listar_aplicacoes():
        return AplicacaoDAO().listar()
    
    @staticmethod
    def inserir_aplicacao(id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status):
        a = Aplicacao(0, id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status)
        AplicacaoDAO().inserir(a)

    @staticmethod
    def listar_aplicacao_id(id):
        return AplicacaoDAO().listar_id(id)
    
    @staticmethod
    def atualizar_aplicacao(id, id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status):
        a = Aplicacao(id, id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status)
        AplicacaoDAO().atualizar(a)
    
    @staticmethod
    def excluir_aplicacao(id):
        AplicacaoDAO().excluir(id)

    @staticmethod
    def listar_aplicacoes_por_prontuario(id_prontuario):
        todas_aplicacoes = AplicacaoDAO().listar()
        return [a for a in todas_aplicacoes if a.get_id_prontuario() == id_prontuario]
    
    @staticmethod
    def listar_aplicacoes_por_medicamento(id_medicamento):
        todas_aplicacoes = AplicacaoDAO().listar()
        return [a for a in todas_aplicacoes if a.get_id_medicamento() == id_medicamento]
    
    @staticmethod
    def listar_aplicacoes_por_nome_parcial(nome_parcial):
        todas_aplicacoes = AplicacaoDAO().listar()
        resultado = []
        for a in todas_aplicacoes:
            m = View.listar_medicamento_id(a.get_id_medicamento())
            if m and nome_parcial.lower() in m.get_nome().lower():
                resultado.append(a)
        return resultado

    # OPERAÇÕES PET: CRUD

    @staticmethod
    def listar_pets():
        return PetDAO().listar()
    
    @staticmethod
    def inserir_pet(nome, especie, raca, idade, tutor):        
        p = Pet(0, nome, especie, raca, idade, tutor)
        PetDAO().inserir(p)

    @staticmethod
    def listar_pet_id(id):
        return PetDAO().listar_id(id)

    @staticmethod
    def atualizar_pet(id, nome, especie, raca, idade, tutor):
        p = Pet(id, nome, especie, raca, idade, tutor)
        PetDAO().atualizar(p)

    @staticmethod
    def excluir_pet(id):
        PetDAO().excluir(id)

    @staticmethod
    def listar_pets_nome_parcial(nome_parcial):
        todos_pets = PetDAO().listar()
        return [p for p in todos_pets if nome_parcial.lower() in p.get_nome().lower()]