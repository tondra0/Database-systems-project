#!C:\Users\Tondra\AppData\Local\Programs\Python\Python38\python
import cgi
import mysql.connector
mydb = mysql.connector.connect(user='root', password='password',
                                 host='127.0.0.1',
                                 database='supplydb')
mycursor = mydb.cursor()
  
form = cgi.FieldStorage()
if 'pid' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a pid</p>')
else:
    print('<table align="center" border>')
    print('<tr>')
    print('<th>Suppliers name</th>')
    print('<th>Suppliers address</th>')
    print('</tr>')
    pid = form['pid'].value
    #print(pid)
    sql = "SELECT sname, address FROM suppliers WHERE sid = ALL (SELECT sid FROM catalog WHERE cost = ALL(SELECT max(cost) FROM catalog WHERE pid = '"+pid+"'));"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print('<tr>')
        for i in range(2):
            print('<td>'+str(x[i])+'</td>'),
        print('</tr>')
    print('</table>')

mycursor.close()
mydb.close()