class Local:
	url = ''
	urlaux = ''
	compra = 0
	venta = 0
	error = ''

	def __init__(self,url,compra,venta,error):
		self.url = url
		self.compra = compra
		self.venta = venta
		self.error = error
