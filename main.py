from datetime import datetime
from bs4 import BeautifulSoup
import requests
import sqlite3
def zaman():
    vb = sqlite3.connect("gostiks.db")
    kurs = vb.cursor()
    kurs.execute("select SayiminBitdiyiSaat from gostiks")
    data2 = kurs.fetchone()
    return data2[0]
def indikizaman():
    indi = datetime.now()
    deqiq_vaxt = indi.strftime("%d.%m.%Y, %H:%M")


    return deqiq_vaxt

def tapGelBaxis(url):
    sorgu=requests.get(url)
    sorgu_metn= BeautifulSoup(sorgu.text, "html.parser")
    baxisSayi=sorgu_metn.select_one('meta[itemprop="interactionCount"][content]')['content']
    # basliq=sorgu_metn.select_one('meta[itemprop="name"][content]')['content']
    # yayimTarixi=sorgu_metn.select_one('meta[itemprop="datePublished"][content]')['content']
    baxisSayi=int(baxisSayi)
    return baxisSayi#basliq,yayimTarixi
def tapGelBasliq(url):
    sorgu2 = requests.get(url)
    sorgu_metn2 = BeautifulSoup(sorgu2.text, "html.parser")
    basliq = sorgu_metn2.select_one('meta[itemprop="name"][content]')['content']
    # yayimTarixi=sorgu_metn2.select_one('meta[itemprop="datePublished"][content]')['content']
    return basliq
def tapGelZaman(url):
    sorgu3 = requests.get(url)
    sorgu_metn3 = BeautifulSoup(sorgu3.text, "html.parser")
    yayimTarixi = sorgu_metn3.select_one('meta[itemprop="datePublished"][content]')['content']
    return yayimTarixi
vb = sqlite3.connect("gostiks.db")
kurs = vb.cursor()
kurs.execute("select View from gostiks")
data = kurs.fetchall()
liste2=[]
for i in data:
    liste2.append(i[0])



list1=[tapGelBaxis("https://www.youtube.com/watch?v=KDfQKTdCOy8"),tapGelBasliq("https://www.youtube.com/watch?v=KDfQKTdCOy8"),tapGelZaman("https://www.youtube.com/watch?v=KDfQKTdCOy8"),tapGelBaxis("https://www.youtube.com/watch?v=KDfQKTdCOy8")-liste2[0],zaman(),indikizaman()]
list2=[tapGelBaxis("https://www.youtube.com/watch?v=c7wUVsREFnQ"),tapGelBasliq("https://www.youtube.com/watch?v=c7wUVsREFnQ"),tapGelZaman("https://www.youtube.com/watch?v=c7wUVsREFnQ"),tapGelBaxis("https://www.youtube.com/watch?v=c7wUVsREFnQ")-liste2[1],zaman(),indikizaman()]
list3=[tapGelBaxis("https://www.youtube.com/watch?v=651M4cvO6yE"),tapGelBasliq("https://www.youtube.com/watch?v=651M4cvO6yE"),tapGelZaman("https://www.youtube.com/watch?v=651M4cvO6yE"),tapGelBaxis("https://www.youtube.com/watch?v=651M4cvO6yE")-liste2[2],zaman(),indikizaman()]
list4=[tapGelBaxis("https://www.youtube.com/watch?v=YSf4KbRnrbY"),tapGelBasliq("https://www.youtube.com/watch?v=YSf4KbRnrbY"),tapGelZaman("https://www.youtube.com/watch?v=YSf4KbRnrbY"),tapGelBaxis("https://www.youtube.com/watch?v=YSf4KbRnrbY")-liste2[3],zaman(),indikizaman()]
list5=[tapGelBaxis("https://www.youtube.com/watch?v=afVhKxFKEuQ"),tapGelBasliq("https://www.youtube.com/watch?v=afVhKxFKEuQ"),tapGelZaman("https://www.youtube.com/watch?v=afVhKxFKEuQ"),tapGelBaxis("https://www.youtube.com/watch?v=afVhKxFKEuQ")-liste2[4],zaman(),indikizaman()]
kurs.execute("delete from  gostiks")
# kurs.execute("create table if not exists gostiks(View int,Title text,UploadTime text)")
# kurs.execute("alter table gostiks add Saat text")
# kurs.execute("alter table gostiks rename 'Sayimin Basladigi Saat'  to SayiminBasladigiSaat")
# kurs.execute("alter table gostiks rename 'Sayimin Bitdiyi Saat' to SayiminBitdiyiSaat")
kurs.execute("insert into gostiks values(?,?,?,?,?,?)",list1)
kurs.execute("insert into gostiks values(?,?,?,?,?,?)",list2)
kurs.execute("insert into gostiks values(?,?,?,?,?,?)",list3)
kurs.execute("insert into gostiks values(?,?,?,?,?,?)",list4)
kurs.execute("insert into gostiks values(?,?,?,?,?,?)",list5)
vb.commit()
vb.close()
print("Toplam Izlenme:"+str(list1[0]+list2[0]+list3[0]+list4[0]))




