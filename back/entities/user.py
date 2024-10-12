class User():
    def __init__(self, nusp, email, senha, nivel):
        self.nusp = nusp
        self.email = email
        self.senha = senha
        self.nivel = nivel
   
    def to_dict(self):
        return {
            'nusp': self.nusp,
            'email': self.email,
            'nivel': self.nivel
        }