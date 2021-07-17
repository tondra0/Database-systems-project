#!C:\Users\Tondra\AppData\Local\Programs\Python\Python38\python
import cgi
import mysql.connector
mydb = mysql.connector.connect(user='root', password='password',
                                 host='127.0.0.1',
                                 database='supplydb')
mycursor = mydb.cursor()
  
form = cgi.FieldStorage()
if 'cost' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a value for cost</p>')
else:
    print('<table align="center" border>')
    print('<tr>')
    print('<th>Suppliers name</th>')
    print('</tr>')
    cost = form['cost'].value
    #print(cost)
    sql = "SELECT sname FROM suppliers WHERE sid = ANY (SELECT sid FROM catalog WHERE cost = "+cost+" or cost > "+cost+");"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print('<tr><td>'+str(x[0])+'</td></tr>')
    print('</table>')

mycursor.close()
mydb.close()