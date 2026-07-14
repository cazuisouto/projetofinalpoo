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
    