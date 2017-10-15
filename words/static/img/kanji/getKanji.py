import codecs
import requests
from multiprocessing import Pool

def getHex(input):
	return hex(ord(input))[2:].upper()

def getUrl(input, bool=False):
	if (bool):
		return "http://www.yosida.com/images/kanji/"+input+"_still.gif"
	else:
		return "http://www.yosida.com/images/kanji/"+input+".gif"

def getKanji(input):
	# folder = "1/"
	# partname = ".gif"
	# still = False
	folder = "1_static/"
	partname = "_still.gif"
	still = True
	r = requests.get(getUrl(input, still))
	f = open(folder+input+partname, 'wb')
	f.write(r.content)
	f.close()
	print(folder+input+partname)

f = codecs.open('l1.txt', encoding='utf-8')
listKanji = []

for line in f:
	j = getHex(line.strip())
	listKanji.append(j)

# print(listKanji)	
if __name__ == '__main__':
	pool = Pool(10)
	pool.map(getKanji, listKanji)
	# pool.map(getKanji(3))
	# pool.wait_completion()
