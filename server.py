import os
from databasesetup import initialize
from flask import Flask, redirect, url_for, render_template, request, session
from psycopg2 import extensions
from querytemplate import *

extensions.register_type(extensions.UNICODE)
extensions.register_type(extensions.UNICODEARRAY)
currentTime = time.strftime('%d.%m.%Y')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'testtesttest'


def listtostring(liste, seperator=' '):
    return seperator.join(liste)

@app.route("/")
def home_page():
    usercount = return_row_count("users")
    hashcount = return_row_count("hashes")
    ipcount = return_row_count("ipaddresses")
    urlcount = return_row_count("urls")
    emailcount = return_row_count("emails")
    return render_template("home.html", usercount = usercount, hashcount = hashcount, ipcount = ipcount, urlcount = urlcount, emailcount = emailcount)

@app.route("/ipaddresses", methods = ['GET','POST'])
def ipaddresses_page():
    if request.method == "GET":
        y = ip_user_join()
        return render_template("ipaddresses.html", rows = y)
    elif request.method == "POST":
        if("DeleteQueryElement" in request.form):
            delete_row(request.form["DeleteQueryElement"],"ipaddresses")
            y = ip_user_join()
            return render_template("ipaddresses.html", rows=y)
        else:
            newrows = search_term(request.form['search'], 'ipaddresses')
            return render_template("ipaddresses.html", rows=newrows)

@app.route("/emails", methods = ['GET','POST'])
def emails_page():
    if request.method == "GET":
        a = []
        relations = []
        b = ["","","","",""]
        y = email_user_join()
        list1 = hash_email_join()
        list2 = hash_url_join()
        list3 = url_email_join()
        listtotal = list1 + list2 + list3
        for i in y:
            b[0] = i[0]
            b[1] = i[1]
            b[3] = i[3]
            b[4] = i[2]
            for j in listtotal:
                if j[0] == i[0]:
                    relations.append(j[1])
                elif j[1] == i[0]:
                    relations.append(j[0])
            if not (len(relations) > 0):
                b[2] = "-"
            else :
                b[2] = listtostring(relations," - ")
            a.append(b)
            relations.clear()
            b = ["", "", "", "", ""]
        return render_template("emails.html", rows = a)
    elif request.method == "POST":
        if ("DeleteQueryElement" in request.form):
            try:
                delete_from_urlemail(search_id(request.form["DeleteQueryElement"],"emails")[0],"email")
                delete_from_hashemail(search_id(request.form["DeleteQueryElement"], "emails")[0], "email")
            except:
                pass
            delete_row(request.form["DeleteQueryElement"], "emails")
            a = []
            relations = []
            b = ["", "", "", "", ""]
            y = email_user_join()
            list1 = hash_email_join()
            list2 = hash_url_join()
            list3 = url_email_join()
            listtotal = list1 + list2 + list3
            for i in y:
                b[0] = i[0]
                b[1] = i[1]
                b[3] = i[3]
                b[4] = i[2]
                for j in listtotal:
                    if j[0] == i[0]:
                        relations.append(j[1])
                    elif j[1] == i[0]:
                        relations.append(j[0])
                if not (len(relations) > 0):
                    b[2] = "-"
                else:
                    b[2] = listtostring(relations, " - ")
                a.append(b)
                relations.clear()
                b = ["", "", "", "", ""]
            return render_template("emails.html", rows=a)
        else:
            y = search_term(request.form['search'], 'emails')
            a = []
            relations = []
            b = ["", "", "", "", ""]
            list1 = hash_email_join()
            list2 = hash_url_join()
            list3 = url_email_join()
            listtotal = list1 + list2 + list3
            for i in y:
                b[0] = i[0]
                b[1] = i[1]
                b[3] = i[3]
                b[4] = i[2]
                for j in listtotal:
                    if j[0] == i[0]:
                        relations.append(j[1])
                    elif j[1] == i[0]:
                        relations.append(j[0])
                if not (len(relations) > 0):
                    b[2] = "-"
                else:
                    b[2] = listtostring(relations, " - ")
                a.append(b)
                relations.clear()
                b = ["", "", "", "", ""]
            return render_template("emails.html", rows=a)

@app.route("/hashes", methods = ['GET','POST'])
def hashes_page():
    if request.method == "GET":
        a = []
        relations = []
        b = ["","","","",""]
        y = hash_user_join()
        list1 = hash_email_join()
        list2 = hash_url_join()
        list3 = url_email_join()
        listtotal = list1 + list2 + list3
        for i in y:
            b[0] = i[0]
            b[1] = i[1]
            b[3] = i[3]
            b[4] = i[2]
            for j in listtotal:
                if j[0] == i[0]:
                    relations.append(j[1])
                elif j[1] == i[0]:
                    relations.append(j[0])
            if not (len(relations) > 0):
                b[2] = "-"
            else :
                b[2] = listtostring(relations," - ")
            a.append(b)
            relations.clear()
            b = ["", "", "", "", ""]
        return render_template("hashes.html", rows = a)
    elif request.method == "POST":
        if ("DeleteQueryElement" in request.form):
            try:
                delete_from_hashurl(search_id(request.form["DeleteQueryElement"],"hashes")[0],"hash")
                delete_from_hashemail(search_id(request.form["DeleteQueryElement"], "hashes")[0], "hash")
            except:
                pass
            delete_row(request.form["DeleteQueryElement"], "hashes")
            a = []
            relations = []
            b = ["", "", "", "", ""]
            y = hash_user_join()
            list1 = hash_email_join()
            list2 = hash_url_join()
            list3 = url_email_join()
            listtotal = list1 + list2 + list3
            for i in y:
                b[0] = i[0]
                b[1] = i[1]
                b[3] = i[3]
                b[4] = i[2]
                for j in listtotal:
                    if j[0] == i[0]:
                        relations.append(j[1])
                    elif j[1] == i[0]:
                        relations.append(j[0])
                if not (len(relations) > 0):
                    b[2] = "-"
                else:
                    b[2] = listtostring(relations, " - ")
                a.append(b)
                relations.clear()
                b = ["", "", "", "", ""]
            return render_template("hashes.html", rows=a)
        else:
            y = search_term(request.form['search'], 'hashes')
            a = []
            relations = []
            b = ["", "", "", "", ""]
            list1 = hash_email_join()
            list2 = hash_url_join()
            list3 = url_email_join()
            listtotal = list1 + list2 + list3
            for i in y:
                b[0] = i[0]
                b[1] = i[1]
                b[3] = i[3]
                b[4] = i[2]
                for j in listtotal:
                    if j[0] == i[0]:
                        relations.append(j[1])
                    elif j[1] == i[0]:
                        relations.append(j[0])
                if not (len(relations) > 0):
                    b[2] = "-"
                else:
                    b[2] = listtostring(relations, " - ")
                a.append(b)
                relations.clear()
                b = ["", "", "", "", ""]
            return render_template("hashes.html", rows=a)

@app.route("/urls", methods = ['GET','POST'])
def urls_page():
    if request.method == "GET":
        a = []
        relations = []
        b = ["","","","",""]
        y = url_user_join()
        list1 = hash_email_join()
        list2 = hash_url_join()
        list3 = url_email_join()
        listtotal = list1 + list2 + list3
        for i in y:
            b[0] = i[0]
            b[1] = i[1]
            b[3] = i[3]
            b[4] = i[2]
            for j in listtotal:
                if j[0] == i[0]:
                    relations.append(j[1])
                elif j[1] == i[0]:
                    relations.append(j[0])
            if not (len(relations) > 0):
                b[2] = "-"
            else :
                b[2] = listtostring(relations," - ")
            a.append(b)
            relations.clear()
            b = ["", "", "", "", ""]
        return render_template("urls.html", rows = a)
    elif request.method == "POST":
        if ("DeleteQueryElement" in request.form):
            try:
                delete_from_hashurl(search_id(request.form["DeleteQueryElement"][0],"urls"),"url")
                delete_from_urlemail(search_id(request.form["DeleteQueryElement"][0], "urls"), "url")
            except:
                pass
            delete_row(request.form["DeleteQueryElement"], "urls")
            a = []
            relations = []
            b = ["", "", "", "", ""]
            y = url_user_join()
            list1 = hash_email_join()
            list2 = hash_url_join()
            list3 = url_email_join()
            listtotal = list1 + list2 + list3
            for i in y:
                b[0] = i[0]
                b[1] = i[1]
                b[3] = i[3]
                b[4] = i[2]
                for j in listtotal:
                    if j[0] == i[0]:
                        relations.append(j[1])
                    elif j[1] == i[0]:
                        relations.append(j[0])
                if not (len(relations) > 0):
                    b[2] = "-"
                else:
                    b[2] = listtostring(relations, " - ")
                a.append(b)
                relations.clear()
                b = ["", "", "", "", ""]
            return render_template("urls.html", rows=a)
        else:
            y = search_term(request.form['search'], 'urls')
            a = []
            relations = []
            b = ["", "", "", "", ""]
            list1 = hash_email_join()
            list2 = hash_url_join()
            list3 = url_email_join()
            listtotal = list1 + list2 + list3
            for i in y:
                b[0] = i[0]
                b[1] = i[1]
                b[3] = i[3]
                b[4] = i[2]
                for j in listtotal:
                    if j[0] == i[0]:
                        relations.append(j[1])
                    elif j[1] == i[0]:
                        relations.append(j[0])
                if not (len(relations) > 0):
                    b[2] = "-"
                else:
                    b[2] = listtostring(relations, " - ")
                a.append(b)
                relations.clear()
                b = ["", "", "", "", ""]
            return render_template("urls.html", rows=a)

@app.route("/signup", methods = ['GET','POST'])
def signup_page():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        if(request.form['name'] == ""):
            message = "User name can't be empty"
            return render_template("signup.html", message=message)
        if(request.form['password'] == ""):
            message = "Password can't be empty"
            return render_template("signup.html", message=message)
        if(request.form['password'] != request.form['passwordr']):
            message = "Password and Password Again must be same"
            return render_template("signup.html", message=message)
        if(search_user(request.form['name']) > 0):
            message = "{} is already taken".format(request.form['name'])
            return render_template("signup.html", message=message)
        insert_user(request.form['name'],request.form['password'])
        message = "Successfully signed up"
        return render_template("signup.html", message = message)

@app.route("/login", methods = ['GET','POST'])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        message = "Test"
        username = request.form['name']
        userpassword = request.form['password']
        if(userpassword == ""):
            message = "Password can't be empty"
            return render_template("login.html", message=message)
        if(username == ""):
            message = "Username can't be empty"
            return render_template("login.html", message=message)
        if(search_user(username) < 1):
            message = "User name can't be found"
            return render_template("login.html", message=message)
        if(check_password(username) != userpassword):
            message = "Wrong Password or Wrong Username"
            return render_template("login.html", message=message)
        a = user_session_info(username)
        session["id"] = a[0]
        session["name"] = a[1]
        session["status"] = a[2]
        return home_page()

@app.route("/logout", methods = ['GET','POST'])
def logout_page():
    session["id"] = None
    session["name"] = None
    session["status"] = None
    return home_page()

@app.route("/addmodifyip", methods = ['GET','POST'])
def add_modify_ip_page():
    if request.method == "GET":
        return render_template("addmodifyip.html")
    elif request.method == "POST":
        if(session["id"] == None):
            message = "You must login to add/modify data"
            return render_template("addmodifyip.html", message=message)
        if(request.form['ipaddress'] == ""):
            message = "IP Address can not be empty"
            return render_template("addmodifyip.html", message=message)
        if(request.form['country'] == ""):
            message = "Country can not be empty"
            return render_template("addmodifyip.html", message=message)
        if request.form['operation'] == 'Add':
            if (check(request.form['ipaddress'], "ipaddresses") > 0):
                message = "{} already exists in database".format(request.form['ipaddress'])
                return render_template("addmodifyip.html", message=message)
            currentTime = time.strftime('%d.%m.%Y')
            insert_ip(request.form['ipaddress'],request.form['country'],currentTime,session["id"])
            message = "{} successfully added".format(request.form['ipaddress'])
            return render_template("addmodifyip.html", message=message)
        elif request.form['operation'] == 'Modify':
            if (check(request.form['ipaddress'], "ipaddresses") == 0):
                message = "Given IP Address can not be found"
                return render_template("addmodifyip.html", message=message)
            modify_ip(request.form['ipaddress'],request.form['country'])
            message = "{} successfully modified".format(request.form['ipaddress'])
            return render_template("addmodifyip.html", message = message)

@app.route("/addmodifyemail", methods = ['GET','POST'])
def add_modify_email_page():
    if request.method == "GET":
        return render_template("addmodifyemail.html")
    elif request.method == "POST":
        if(session["id"] == None):
            message = "You must login to add/modify data"
            return render_template("addmodifyemail.html", message=message)
        if(request.form['email'] == ""):
            message = "E-Mail can not be empty"
            return render_template("addmodifyemail.html", message=message)
        if(request.form['type'] == ""):
            message = "Type can not be empty"
            return render_template("addmodifyemail.html", message=message)
        if request.form['operation'] == 'Add':
            currentTime = time.strftime('%d.%m.%Y')
            insert_email(request.form['email'],request.form['type'],currentTime,session["id"])
            message = "{} successfully added".format(request.form['email'])
            return render_template("addmodifyemail.html", message=message)
        elif request.form['operation'] == 'Modify':
            if (check(request.form['email'], "emails") == 0):
                message = "Given E-Mail can not be found".format(request.form['email'])
                return render_template("addmodifyemail.html", message=message)
            modify_email(request.form['email'],request.form['type'])
            message = "{} successfully modified".format(request.form['email'])
            return render_template("addmodifyemail.html", message = message)

@app.route("/addmodifyhash", methods = ['GET','POST'])
def add_modify_hash_page():
    if request.method == "GET":
        return render_template("addmodifyhash.html")
    elif request.method == "POST":
        if(session["id"] == None):
            message = "You must login to add/modify data"
            return render_template("addmodifyhash.html", message=message)
        if(request.form['hash'] == ""):
            message = "Hash can not be empty"
            return render_template("addmodifyhash.html", message=message)
        if(request.form['type'] == ""):
            message = "File Type can not be empty"
            return render_template("addmodifyhash.html", message=message)
        if request.form['operation'] == 'Add':
            if (check(request.form['hash'], "hashes") > 0):
                message = "{} already exists in database".format(request.form['hash'])
                return render_template("addmodifyhash.html", message=message)
            currentTime = time.strftime('%d.%m.%Y')
            insert_hash(request.form['hash'],request.form['type'],currentTime,session["id"])
            message = "{} successfully added".format(request.form['hash'])
            return render_template("addmodifyhash.html", message=message)
        elif request.form['operation'] == 'Modify':
            if (check(request.form['hash'], "hashes") == 0):
                message = "Given Hash can not be found"
                return render_template("addmodifyhash.html", message=message)
            modify_hash(request.form['hash'],request.form['type'])
            message = "{} successfully modified".format(request.form['hash'])
            return render_template("addmodifyhash.html", message = message)

@app.route("/addmodifyurl", methods = ['GET','POST'])
def add_modify_url_page():
    if request.method == "GET":
        return render_template("addmodifyurl.html")
    elif request.method == "POST":
        if(session["id"] == None):
            message = "You must login to add/modify data"
            return render_template("addmodifyurl.html", message=message)
        if(request.form['url'] == ""):
            message = "URL can not be empty"
            return render_template("addmodifyhash.html", message=message)
        if(request.form['status'] == ""):
            message = "Status can not be empty"
            return render_template("addmodifyurl.html", message=message)
        if request.form['operation'] == 'Add':
            if (check(request.form['url'], "urls") > 0):
                message = "{} already exists in database".format(request.form['url'])
                return render_template("addmodifyurl.html", message=message)
            currentTime = time.strftime('%d.%m.%Y')
            insert_url(request.form['url'],request.form['status'],currentTime,session["id"])
            message = "{} successfully added".format(request.form['url'])
            return render_template("addmodifyurl.html", message=message)
        elif request.form['operation'] == 'Modify':
            if (check(request.form['url'], "urls") == 0):
                message = "Given URL can not be found"
                return render_template("addmodifyurl.html", message=message)
            modify_url(request.form['url'],request.form['status'])
            message = "{} successfully modified".format(request.form['url'])
            return render_template("addmodifyurl.html", message = message)

@app.route("/connect", methods = ['GET','POST'])
def connect_page():
    if request.method == "GET":
        return render_template("connect.html")
    elif request.method == "POST":
        message =""
        if(request.form['t1'] == '' or request.form['t2'] == ''):
            message = "Please fill all the forms"
            return render_template("connect.html", message = message)

        if(request.form['type1operation'] == 'Hash'):
            index1 = search_id(request.form['t1'],"hashes")
        elif(request.form['type1operation'] == 'E-Mail'):
            index1 = search_id(request.form['t1'],"emails")
        elif(request.form['type1operation'] == 'URL'):
            index1 = search_id(request.form['t1'],"urls")


        if(request.form['type2operation'] == 'Hash'):
            index2 = search_id(request.form['t2'],"hashes")
        elif(request.form['type2operation'] == 'E-Mail'):
            index2 = search_id(request.form['t2'],"emails")
        elif(request.form['type2operation'] == 'URL'):
            index2 = search_id(request.form['t2'],"urls")

        if(index1 == None or index2 == None):
            message = "Please check the inputs again. At least one of the types can't be found"
            return render_template("connect.html", message = message)

        if(request.form['type1operation'] == request.form['type2operation']):
            message = "Relation can't exist between same types"
            return render_template("connect.html", message = message)

        index1 = int(index1[0])
        index2 = int(index2[0])

        if(request.form['type1operation'] == 'Hash' and request.form['type2operation'] == 'URL'):
            insert_junction("hash","url",index1,index2)
            message = "Relation succesfully created"
            return render_template("connect.html", message = message)
        elif(request.form['type1operation'] == 'URL' and request.form['type2operation'] == 'Hash'):
            insert_junction("hash","url",index2,index1)
            message = "Relation succesfully created"
            return render_template("connect.html", message = message)
        elif(request.form['type1operation'] == 'Hash' and request.form['type2operation'] == 'E-Mail'):
            insert_junction("hash","email",index1,index2)
            message = "Relation succesfully created"
            return render_template("connect.html", message = message)
        elif(request.form['type1operation'] == 'E-Mail' and request.form['type2operation'] == 'Hash'):
            insert_junction("hash","email",index2,index1)
            message = "Relation succesfully created"
            return render_template("connect.html", message = message)
        elif(request.form['type1operation'] == 'URL' and request.form['type2operation'] == 'E-Mail'):
            insert_junction("url","email",index1,index2)
            message = "Relation succesfully created"
            return render_template("connect.html", message = message)
        elif(request.form['type1operation'] == 'E-Mail' and request.form['type2operation'] == 'URL'):
            insert_junction("url","email",index2,index1)
            message = "Relation succesfully created"
            return render_template("connect.html", message = message)

        print(index1,index2)

        return render_template("connect.html")



if __name__ == "__main__":
    app.run()