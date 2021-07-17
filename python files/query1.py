#!C:\Users\Tondra\AppData\Local\Programs\Python\Python38\python
import cgi, cgitb
import mysql.connector
mydb = mysql.connector.connect(user='root', password='password',
                                 host='127.0.0.1',
                                 database='supplydb')
mycursor = mydb.cursor()
  
form = cgi.FieldStorage()
if 'pname' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a parts"s name</p>')
else:
    print('<table align="center" border>')
    print('<tr>')
    pname = form['pname'].value
    info = form.getlist('supplierInfor')
    
    if 'cost' in info:
        s1= "SELECT cost FROM catalog WHERE pid = ALL (SELECT pid FROM parts WHERE pname = '"+pname+"');"
        print('<th>Cost</th>')
        mycursor.execute(s1)
        mr = mycursor.fetchall()
        for x in mr:
            print('<tr><td>'+str(x[0])+'</td></tr>')
    
    print('<th>Suppliers sid</th>')
    print('<th>Suppliers name</th>')
    print('<th>Suppliers address</th>')
    print('</tr>')
    sql = "SELECT sid, sname, address FROM suppliers WHERE sid = ANY (SELECT sid FROM catalog WHERE pid = ALL (SELECT pid FROM parts WHERE pname = '"+pname+"'));"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print('<tr>')
        for i in range(3):
            print('<td>'+str(x[i])+'</td>'),
        print('</tr>')
    print('</table>')

mycursor.close()
mydb.close()