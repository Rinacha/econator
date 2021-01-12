from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, JsonResponse
from django.utils import timezone

from django.views import View
from django.http import HttpResponse,Http404
from django.http.response import JsonResponse
from django.conf import settings
#from django.core.mail import BadHeaderError, send_mail 
#from .forms import ContactForm
#from shop.forms import ContactForm

from shop import models
import sqlite3
from .models import Post

def index(request):
    return render(request, 'shop/index.html')

def explain(request):
    return render(request, 'shop/explanation.html')

def search(request):
    return render(request, 'shop/search.html')
    
"""
# 送信完了画面
def complete(request):
    return render(request, 'contact/templates/complete.html')

def tmp(request):
    return render(request, 'shop/tmp.html')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 追記
            subject = form.cleaned_data['subject']
            subject = form.clean_subject()
            message = form.cleaned_data['message']
            message = form.clean_message()
            sender = form.cleaned_data['sender']
#            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]
#            if form.clean_subject
#            if myself:
#                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return render(request, 'contact/complete.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
"""

def list_view(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute("SELECT * FROM product")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL": row[10],
        }
        lst.append(data)

    con.close()
    return render(request, 'shop/list_view.html', {'products': lst})


def detail(request, pk):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE product_id={pk}")
    row = list(cursor)[0]
    product = {
        "product_id": row[0],
        "product_name": row[1],
        "price": row[2],
        "form": row[3],
        "mate": row[4],
        "method": row[5],
        "color": row[6],
        "size_d": row[7],
        "size_w": row[8],
        "URL": row[9],
        "pictureURL":row[10],
    }
    con.close()
    return render(request, 'shop/detail.html', {'product': product})


##################################################################################
#################################################################################
# color #
def search_color(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product GROUP BY color")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/search_color.html', {'products': lst})


def color_black(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE color = 'black'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/color_black.html', {'products': lst})

def color_blue(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE color = 'blue'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/color_blue.html', {'products': lst})

def color_gray(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE color = 'gray'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/color_gray.html', {'products': lst})

def color_green(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE color = 'green'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/color_green.html', {'products': lst})

def color_red(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE color = 'red'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/color_red.html', {'products': lst})

def color_white(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE color = 'white'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/color_white.html', {'products': lst})

def color_yellow(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE color = 'yellow'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'color/color_yellow.html', {'products': lst})


###################################################################################
#####################################################################################
#  形 #
def search_form(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product GROUP BY form")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/search_form.html', {'products': lst})

def carry(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'キャリーバッグ'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/carry.html', {'products': lst})

def shoulder(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'ショルダーバッグ'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/shoulder.html', {'products': lst})

def toto(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'トートバッグ'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/toto.html', {'products': lst})

def drop(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'ドロップ'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/drop.html', {'products': lst})

def netcloth(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'ネットクロス'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/net.html', {'products': lst})

def bag(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'バッグ'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/bag.html', {'products': lst})

def ryukku(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'リュック'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/ryukku.html', {'products': lst})

def reji_bag(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'レジかご'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/reji_bag.html', {'products': lst})

def reji(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE form = 'レジ袋'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'form/reji.html', {'products': lst})


###################################################################################
#########################################################################################
# 値段 #
def search_price(request):
    return render(request, 'price/search_price.html')

def hund(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE price <= 1000")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'price/hund.html', {'products': lst})

def two_hund(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE price > 1000 and price <= 2000")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'price/two_hund.html', {'products': lst})

def three_hund(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE price > 2000 and price <= 3000")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'price/three_hund.html', {'products': lst})

def four_hund(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE price > 3000 and price <= 4000")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'price/four_hund.html', {'products': lst})

def five_hund(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE price > 4000 and price <= 5000")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'price/four_hund.html', {'products': lst})

def five_hund(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE price > 4000 and price <= 5000")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'price/five_hund.html', {'products': lst})

def over(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE price > 5000")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'price/over.html', {'products': lst})




####################################################################################
#######################################################################################
# 販売元 #
def search_seller(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'seller/search_seller.html', {'products': lst})

def amazon(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE  pictureURL LIKE '%amazon%'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'seller/amazon.html', {'products': lst})

def rakuten(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE pictureURL LIKE '%rakuten%'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'seller/rakuten.html', {'products': lst})

def yahoo(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE pictureURL LIKE '%shopping.c%'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'seller/yahoo.html', {'products': lst})


#################################################################################
###################################################################################
# mate #
def search_mate(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product GROUP BY mate")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'mate/search_material.html', {'products': lst})


def jusi(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE mate = 'EVA樹脂'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'mate/jusi.html', {'products': lst})

def nylone(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE mate = 'ナイロン'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'mate/nylone.html', {'products': lst})

def net(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE mate = 'ネットクロス'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'mate/net.html', {'products': lst})

def pori(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE mate = 'ポリエステル'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'mate/pori.html', {'products': lst})

def unknown(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE mate = '不明'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'mate/unknown.html', {'products': lst})


###################################################################################
###################################################################################3
# 管理方法  #
def search_method(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product GROUP BY method")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'method/search_method.html', {'products': lst})

def natural(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE method = 'そのまま'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'method/natural.html', {'products': lst})

def fold(request):
    db = 'econator_sql.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    lst = []
    cursor = cur.execute(f"SELECT * FROM product WHERE method = '折り畳み'")
    for row in cursor:
        data = {
            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "form": row[3],
            "mate": row[4],
            "method": row[5],
            "color": row[6],
            "size_d": row[7],
            "size_w": row[8],
            "URL": row[9],
            "pictureURL":row[10],
        }
        lst.append(data)
    con.close()
    return render(request, 'method/fold.html', {'products': lst})
