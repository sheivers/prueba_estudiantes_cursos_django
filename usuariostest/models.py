
class Respuesta( object ):

	def __init__(self, **kwargs ):
		self.status = kwargs.get('st', None)
		self.data = kwargs.get('data', None)
		self.message = kwargs.get('ms', None)
		self.check = False
  
  
	def trans(self):
     
		response = {}
		
		if( self.message == None ):
			# Respuestas positivas
			if( self.status == "0.0"):
				self.message = "Petición entregada correctamente."; self.check = True

			# Respuestas Negativas
			if( self.status == "1.0"):
				self.message = "Petición entregada incorrectamente."; self.check = True

			# Peticiones con error
			if( self.status == "2.0"):
				self.message = "Parametros incorrectos.";self.check = True

			# Peticiones con error
			if( self.status == "3.0"):
				self.message = "Método no valido.";self.check = True

		if( self.status != ""):
			response["status"] = self.status
			response["message"] = self.message
		else:
			response["status"] = "1.0"

		if( self.data != None and self.data ): 
			response["data"] = self.data

		return response



def parametros( jsondata , requeridas , opcionales, mayusculas = True ):
	
	opcionales.append("date_up")
	opcionales.append("date_in")
 
	for clave in requeridas:
		if( clave not in jsondata.keys() ):
				raise Exception()
	limpio = {}
	for clave, valor in jsondata.items():
		if( clave in ( requeridas + opcionales )):
			if( mayusculas ):
				limpio[clave] = valor.upper() if isinstance(valor, str) else valor
			else:
				limpio[clave] = valor
	return limpio
		

