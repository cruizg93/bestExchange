import json
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
from array import array
from Local import Local

class Medellin():

	def __init__(self):
		print('Medellin init')

	def getTrm(self):
		#TRMM
		url="https://www.superfinanciera.gov.co/jsp/index.jsf"
		print(url)
		thepage = urllib.request.urlopen(url)
		soup = BeautifulSoup(thepage, "html.parser")
		try:
			trm = soup.find("div",{"class":"cont_Indicador"}).find("table").findAll("tr")[1].findAll("td")[1].text
		except Exception as e:
			print("Error getting TRM")
			trm = "Error"
			print(e)

		return json.dumps({'status':'ok','trm':trm})


	def getDolar(self):

		bestCompraUrl = ''
		bestCompra = '0'
		bestVentaUrl = ''
		bestVenta = ''


		url= "http://www.efecternet.com/Clientes/Interdolar/"
		urlaux= "http://www.interdolar.co/"
		print(urlaux)

		try:
			thepage = urllib.request.urlopen(url)
			soup = BeautifulSoup(thepage, "html.parser")
			rows = soup.findAll("span",{"class":"style16"})
			compra1 = re.findall(r'\d+',rows[0].find("font").text)[0]+re.findall(r'\d+',rows[0].find("font").text)[1]
			venta1 = re.findall(r'\d+',rows[1].find("font").text)[0]+re.findall(r'\d+',rows[1].find("font").text)[1]
			#Local1
			local1 = Local(urlaux,compra1,venta1,'')
			bestCompraUrl = urlaux
			bestCompra = compra1
			bestVentaUrl = urlaux
			bestVenta = venta1
		except Exception as e:
			print("Error with "+urlaux)
			print(e)
			local1 = Local('',0,0,'Error with '+url)


		url= "http://www.surcambios.com/"
		print(url)

		try:
			thepage = urllib.request.urlopen(url)
			soup = BeautifulSoup(thepage, "html.parser")
			compra2aux = soup.find("table",{"class":"currency-exchange"}).findAll("td")[2].text
			compra2 = re.findall(r'\d+',compra2aux)[0] + re.findall(r'\d+',compra2aux)[1]
			venta2=re.findall(r'\d+',soup.find("table",{"class":"currency-exchange"}).findAll("td")[3].text)[0]
			#Local2
			local2 = Local(url,compra2,venta2,'')
			if compra2 > bestCompra:
				bestCompra = compra2
				bestCompraUrl = url

			if venta2 < bestVenta:
				bestVenta = venta2
				bestVentaUrl = url
		except Exception as e:
			print("Error with "+url)
			print(e)
			local2 = Local('',0,0,'Error with '+url)


		url= "http://www.valoresyservicios.com/"
		print(url)
			
		try:
			thepage = urllib.request.urlopen(url)
			soup = BeautifulSoup(thepage, "html.parser")
			compra3 = re.findall(r'\d+',soup.find("table").find("tr").findNext('tr').findAll("td")[2].text)[0]
			venta3 = re.findall(r'\d+',soup.find("table").find("tr").findNext('tr').findAll("td")[3].text)[0]
			#Local3
			local3 = Local(url,compra3,venta3,'')
			if compra3 > bestCompra:
				bestCompra = compra2
				bestCompraUrl = url

			if venta3 < bestVenta:
				bestVenta = venta2
				bestVentaUrl = url
		except Exception as e:
			print("Error with "+url)
			print(e)
			local3 = Local('',0,0,'Error with '+url)


		url="http://www.divismarket.com/"
		print(url)
			

		try:
			thepage = urllib.request.urlopen(url)
			soup = BeautifulSoup(thepage, "html.parser")
			compra4 = "2760"
			venta4 = "2830"
			print("********************************")
			print(compra4)
			print(venta4)
			print("********************************")
			#Local4
			local4 = Local(url,compra4,venta4,'')
			if compra4 > bestCompra:
				bestCompra = compra4
				bestCompraUrl = url

			if venta4 < bestVenta:
				bestVenta = venta4
				bestVentaUrl = url
		except Exception as e:
			print("*Error with "+url)
			print(e)
			local4 = Local('',0,0,'Error with '+url)
			

		url= "http://www.nutifinanzas.com"
		print(url)
			

		try:
			thepage = urllib.request.urlopen(url)
			soup = BeautifulSoup(thepage, "html.parser")
			compra5 = re.findall(r'\d+',soup.find("div",{"class":"col-md-9"}).text.strip().split()[1])[0]+re.findall(r'\d+',soup.find("div",{"class":"col-md-9"}).text.strip().split()[1])[1]
			venta5 = re.findall(r'\d+',soup.find("div",{"class":"col-md-9"}).text.strip().split()[3])[0]+re.findall(r'\d+',soup.find("div",{"class":"col-md-9"}).text.strip().split()[3])[1]
			#Local5
			local5 = Local(url,compra5,venta5,'')
			if compra5 > bestCompra:
				bestCompra = compra5
				bestCompraUrl = url

			if venta5 < bestVenta:
				bestVenta = venta5
				bestVentaUrl = url
		except Exception as e:
			print("Error with "+url)
			print(e)
			local5 = Local('',0,0,'Error with '+url)

		url="http://www.cambiosenvigado.com/"
		print(url)
			

		try:
			thepage = urllib.request.urlopen(url)
			soup = BeautifulSoup(thepage, "html.parser")
			compra6 = re.findall(r'\d+',soup.find("table",{"class":"modernTable withHeader"}).findAll("tr")[1].findAll("td")[1].text)[0]+re.findall(r'\d+',soup.find("table",{"class":"modernTable withHeader"}).findAll("tr")[1].findAll("td")[1].text)[1]
			venta6 = re.findall(r'\d+',soup.find("table",{"class":"modernTable withHeader"}).findAll("tr")[2].findAll("td")[1].text)[0]+re.findall(r'\d+',soup.find("table",{"class":"modernTable withHeader"}).findAll("tr")[2].findAll("td")[1].text)[1]
			#Local6
			local6 = Local(url,compra6,venta6,'')
			if compra6 > bestCompra:
				
				bestCompra = compra6
				bestCompraUrl = url

			if venta6 < bestVenta:
				bestVenta = venta6
				bestVentaUrl = url
		except Exception as e:
			print("Error with "+url)
			print(e)
			local6 = Local('',0,0,'Error with '+url)

		url ="http://www.cashcambios.com/"
		print(url)

		try:
			thepage = urllib.request.urlopen(url)
			soup = BeautifulSoup(thepage, "html.parser")

			compra7 = "2780"
			venta7 = "2820"
			#Local7
			local7 = Local(url,compra7,venta7,'')
			if compra7 > bestCompra:
				
				bestCompra = compra7
				bestCompraUrl = url

			if venta7 < bestVenta:
				bestVenta = venta7
				bestVentaUrl = url
		except Exception as e:
			print("Error with "+url)
			print(e)
			local7 = Local('',0,0,'Error with '+url)



		url ="http://www.divisasriosur.com/"
		print(url)

		try:
			#thepage = urllib.request.urlopen(url)
			#soup = BeautifulSoup(thepage, "html.parser")
			
			compra8 ="2770" 
			print(compra8)
			venta8 = "2820"
			#Local8
			local8 = Local(url,compra8,venta8,'')
			if compra8 > bestCompra:
				
				bestCompra = compra8
				bestCompraUrl = url

			if venta8 < bestVenta:
				bestVenta = venta8
				bestVentaUrl = url
		except Exception as e:
			print("Error with "+url)
			print(e)
			local8 = Local('',0,0,'Error with '+url)


		url ="http://sites.amarillasinternet.com/tropicaldecambios/"
		urlaux= "http://www.tropicaldecambios.com/"
		print(url)

		try:
			#thepage = urllib.request.urlopen(url)
			#print(thepage)
			#soup = BeautifulSoup(thepage, "html.parser")
			
			#compra9 =re.findall(r'\d+',soup.find("div",{"id":"mainContainer"}).find("div",{"class":"text"}).findAll("table"))
			compra9 = "2800"
			venta9 = "2820"
			#Local8
			local9 = Local(urlaux,compra9,venta9,'')
			if compra9 > bestCompra:
				
				bestCompra = compra9
				bestCompraUrl = urlaux

			if venta9 < bestVenta:
				bestVenta = venta9
				bestVentaUrl = url
		except Exception as e:
			print("Error with "+url)
			print(e)
			local9 = Local('',0,0,'Error with '+url)

		best = {'bestCompraUrl':bestCompraUrl,'bestCompra':bestCompra,'bestVentaUrl':bestVentaUrl,'bestVenta':bestVenta}
		locals = {'local1':{'url':local1.url,'compra':local1.compra,'venta':local1.venta,'error':local1.error}
				,'local2':{'url':local2.url,'compra':local2.compra,'venta':local2.venta,'error':local2.error}
				,'local3':{'url':local3.url,'compra':local3.compra,'venta':local3.venta,'error':local3.error}
				,'local4':{'url':local4.url,'compra':local4.compra,'venta':local4.venta,'error':local4.error}
				,'local5':{'url':local5.url,'compra':local5.compra,'venta':local5.venta,'error':local5.error}
				,'local6':{'url':local6.url,'compra':local6.compra,'venta':local6.venta,'error':local6.error}
				,'local7':{'url':local7.url,'compra':local7.compra,'venta':local7.venta,'error':local7.error}
				,'local8':{'url':local8.url,'compra':local8.compra,'venta':local8.venta,'error':local8.error}
				,'local9':{'url':local9.url,'compra':local9.compra,'venta':local9.venta,'error':local9.error}}
				
		return json.dumps({'status':'ok','best':best, 'locals':locals})
