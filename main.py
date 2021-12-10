import random
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id":random.randint(0,90000)})


# API-ключ созданный ранее
token = "d867f0b8984cbe07f44baffc56e29a77acf98a3006bd9277b9f9ea9901f80b523043fe302d4891200cb3d"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)


allCurse4 = ['ДО12СС21', 'ДОУиА13СС21', 'ИС15СС21', 'М19КР21', 'МД17КР21', 'МР18КР21', 'ПК18КР21', 'С14КР21', 'СД15СС21', 'ССА17СС21', 'СТПП21', 'ТО11СС21', 'ТПИ14СС21', 'ГД15КР20', 'ДО12СС20', 'ИС15СС20', 'МР18КР20', 'ООП12СС20', 'ОЭВМ11ПП20', 'ПК18КР20', 'С14КР20', 'СД15СС20', 'ТО11СС20', 'ТЭ13СС20', 'ЭБ16СС20', 'ГД15КР19', 'ДО11СС19', 'ДО12СС19', 'М19КР19', 'МР18КР19', 'ПК18КР19', 'СД15СС19', 'ССА17СС19', 'ТО11СС19', 'ПК18КР18', 'ССА17СС18', 'ТПИ14СС18']
allCurse = [['ДО12СС21'], ['ДОУиА13СС21'], ['ИС15СС21'], ['М19КР21'], ['МД17КР21'], ['МР18КР21'], ['ПК18КР21'], ['С14КР21'], ['СД15СС21'], ['ССА17СС21'], ['СТПП21'], ['ТО11СС21'], ['ТПИ14СС21'], ['ГД15КР20'], ['ДО12СС20'], ['ИС15СС20'], ['МР18КР20'], ['ООП12СС20'], ['ОЭВМ11ПП20'], ['ПК18КР20'], ['С14КР20'], ['СД15СС20'], ['ТО11СС20'], ['ТЭ13СС20'], ['ЭБ16СС20'], ['ГД15КР19'], ['ДО11СС19'], ['ДО12СС19'], ['М19КР19'], ['МР18КР19'], ['ПК18КР19'], ['СД15СС19'], ['ССА17СС19'], ['ТО11СС19'], ['ПК18КР18'], ['ССА17СС18'], ['ТПИ14СС18']]
days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
karDays = ["ПН","ВТ","СР","ЧТ","ПТ"]
dayNedel = []

def newRas():

    all2 = []
    url = "http://www.sovprocollege.ru/club-5.php"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    all2.append(soup.get_text())
    day2 = 1
    raspisanie = allCurse

    for da in range(5):
        n = all2[0].replace("\n", "|")
        n = n.replace("\xa0", "")
        n.find("1    курс")
        n = n[n.find(days[da]):len(n)]
        if da == 4:
            poned = n[0:n.find(days[day2])]
        else:
            poned = n[0:n.find(days[day2]) - 345]
        poned = poned.split("|")
        dayNedel.append(poned[0])
        print(dayNedel)
        del poned[0]
        ras2 =[]
        newd = 1
        oldd = 40
        day = poned[newd:oldd]
        t = 0
        y = 1
        nudjen = 1
        for dey in range(7):
            if dey == 6:
                day = poned[242:280]
            for r in range(len(allCurse)):
                for x in range(len(raspisanie)):
                    if raspisanie[x] == allCurse[r]:
                        ras2.append(raspisanie[x])
                        ras2[x].append(day[t])
                        t = t + 1

            y = y + 1
            t = 0
            newd = newd + 40
            oldd = oldd + 40
            if y == 6:
                nudjen = 2
            day = poned[nudjen+40*y:40+40*y]
            raspisanie = ras2
            ras2 = []
        day2 = day2 + 1

def goden(num,prDay):
    g = num
    f = prDay
    mrs = []
    iu = 0
    mrs.append(allCurse[g][0]+"\n")
    if prDay == 0:
        kolvoDay = 5
    else:
        kolvoDay = 1
        yt = 0
        ferd = 0
        for l in karDays:
            if prDay == l:
                f = yt
                iu = ferd
                break
            ferd = ferd + 1
            yt = yt + 7
    for t in range(kolvoDay):
        mrs.append("\n")
        mrs.append(dayNedel[iu])
        mrs.append("\n")
        for e in range(7):
            f = f + 1
            if allCurse[g][f] != "":
                mrs.append(f"{e+1} пара: "+allCurse[g][f]+"\n")
            elif allCurse[g][f] == "":
                mrs.append(f"Нет {e+1} пары" + "\n")

        iu = iu + 1
    return "".join([str(_) for _ in mrs])

def timme():
    current_datetime = datetime.now()
    hour = current_datetime.hour
    return hour


newRas()
print("Готова")
print(allCurse4)
chasi = timme()
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            # Сообщение от пользователя
            request = event.text
            # Каменная логика ответа
            newChasi = timme()
            if newChasi != chasi:
                newRas()
                chasi = timme()
            print("Готова2")
            if request:
                request = request.upper()
                messs = request
                messs = messs.split(" ")
                print(messs)
                u = 0
                for e in allCurse4:
                    if request == e:
                        iy = goden(u,0)
                        write_msg(event.user_id, f"{iy}")
                        stat = True
                        break
                    elif messs[0] == e:
                        stat = True
                        for l in karDays:
                            if messs[1] == l:
                                iy = goden(u, messs[1])
                                write_msg(event.user_id, f"{iy}")
                                statDay = True
                                break
                            else:
                                statDay = False
                        if statDay == False:
                            write_msg(event.user_id, "Неверно указан день недели")
                        break
                    else:
                        stat = False
                    u = u + 1
                if stat == False:
                    if len(request) > 20:
                        write_msg(event.user_id, f"Не существует группы")
                    else:
                        write_msg(event.user_id, f"Не существует группы {request}")

