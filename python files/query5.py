#!C:\Users\Tondra\AppData\Local\Programs\Python\Python38\python
import cgi
import mysql.connector
mydb = mysql.connector.connect(user='root', password='password',
                                 host='127.0.0.1',
                                 database='supplydb')
mycursor = mydb.cursor()
  
form = cgi.FieldStorage()
if 'address' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a supplier"s address</p>')
else:
    print('<table align="center" border>')
    print('<tr>')
    print('<th>Suppliers sid</th>')
    print('<th>Suppliers name</th>')
    print('</tr>')
    address = form['address'].value
    #print(address)
    sql = "SELECT sid, sname FROM suppliers WHERE address = '"+address+"' AND sid NOT IN (SELECT sid FROM catalog);"
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