import urllib
import urllib.request
from urllib.request import urlopen
import tkinter
from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM
import codecs
from io import BytesIO
from PIL import Image
from subprocess import Popen, PIPE

#armazenando a imagem do download
download = urllib.request.urlopen('https://c.tenor.com/pw9ZsUdsEYgAAAAj/capoo-blue-cat.gif')

#converte o http_response em string
def convert_html(http):
	data = Popen.communicate(Popen(['import','-w','0x02a00001','png:-'], stdout=PIPE))[0]
	#encoding = http.headers.get_content_charset('utf-8')
	#decode = html_resposta.decode(encoding)
	fdata = http.read()
	fdata = fdata.open(BytesIO(data))
	return fdata

'''ainda preciso encontar um jeito de fazer a comunicação
entre o tkinter e o xwindow'''

# cria o arquivo para colocar a imagem
file = open("capoo-blue-cat.gif")
file.write(convert_html(download).read())
file.close()

#interface gráfica
root = Tk()
root.title(" Brumzius Brum")
photo = file
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text="Helloups")
text.pack(side=BOTTOM)
root.mainloop()
