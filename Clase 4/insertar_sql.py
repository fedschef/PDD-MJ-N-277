import mysql.connector
#Establecer la conexión
conexion = mysql.connector.connect(
                              host='cloud.eant.tech',
                              database='',
                              user='',
                              password='eantpass')
cursor = conexion.cursor()

nombre = 'Gabriel'
apellido = 'Perez'
dni = '26865478'
email = 'gabriel@nada.com'
fecha_nac = '1985-01-15'

#sql = "INSERT INTO alumnos(nombre, apellido, dni, email, fecha_nac)\
   #VALUES('Edgardo', 'Lopez', '45963258', 'eddy@nada.com', '2005-05-05')"
   
#sql = "INSERT INTO alumnos(nombre, apellido, dni, email, fecha_nac)\
   #VALUES('"+nombre+"','"+apellido+"','"+dni+"','"+email+"','"+fecha_nac+"')"

sql = "INSERT INTO alumnos(nombre, apellido, dni, email, fecha_nac)\
   VALUES(%s,%s,%s,%s,%s)"
cursor.execute(sql, (nombre, apellido, dni, email, fecha_nac))
conexion.commit()

print("Datos subidos")
cursor.close()
conexion.close()