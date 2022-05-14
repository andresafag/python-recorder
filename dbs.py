import mysql.connector as mysql


connection=mysql.connect(user='andresito', password='frontend',database='testingthisshit', host='localhost')

cursor=connection.cursor()

# def convert_data(pic):
#     with open(pic, 'rb') as picture:
#         binary_data=picture.read()
#     return binary_data
#
# photo_converted=convert_data('pruebita.png')
# numero=9
#
#
# query="""INSERT INTO ejemplo(numero, imagen) values (%s,%s)"""
#
# result=cursor.execute(query, (numero, photo_converted))
#
# selecciona="SELECT imagen FROM ejemplo WHERE numero = 9"
#
#
# connection.commit()


cursor.execute(selecciona)

fotico=cursor.fetchone()[0]


def extraer(data, filename):
    with open(filename, 'wb') as escribir:
        escribir.write(data)

extraer(fotico, 'nuevafoto.png')



cursor.close()
connection.close()
