#!C:\Users\Tondra\AppData\Local\Programs\Python\Python38\python
import cgi
import mysql.connector
mydb = mysql.connector.connect(user='root', password='password',
                                 host='127.0.0.1',
                                 database='supplydb')
mycursor = mydb.cursor()

form = cgi.FieldStorage()
if 'address' not in form or 'color' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a color and address</p>')
else:
    print('<table align="center" border>')
    print('<tr>')
    print('<th>Parts name</th>')
    print('</tr>')
    color = form['color'].value
    address = form['address'].value
    #print(color, address)
    sql = "SELECT pname FROM parts WHERE color = '"+color+"' AND pid = ANY (SELECT pid FROM catalog WHERE sid = ANY (SELECT sid FROM suppliers WHERE address = '"+address+"'));"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print('<tr><td>'+str(x[0])+'</td></tr>')
    print('</table>')

mycursor.close()
mydb.close()