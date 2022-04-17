class Pessoa(): 
	def __init__(self, nome, idade, sexo, profissao):
		self._nome = nome
		self._idade = idade
		if sexo == 'F' or sexo == 'f':
			self._sexo = "Feminino"
		else:
			self._sexo = "Masculino"
		self._profissao = profissao

	def get_nome(self):
		return self._nome 

	def get_idade(self):
		return self._idade

	def get_sexo(self):
		return self._sexo  

	def get_prof(self):
		return self._profissao  

	def info (self):
		print(f"Nome: {self.get_nome()}")
		print(f"Idade: {self.get_idade()}")
		print(f"Sexo: {self.get_sexo()}")
		print(f"profissao: {self.get_prof()}")
		
		

if __name__ == "__main__":
	Pessoa1 = Pessoa("Carlos", 15, "M", "Estudante")
	Pessoa1.info()
	print()

	Pessoa2 = Pessoa ("Maria", 25, "F",  "Psicóloga")
	Pessoa2.info()
	print()

	Pessoa3 = Pessoa ("João", 37, "M", "Eletricista")
	Pessoa3.info()
	print()