import mysql.connector
#Establecer la conexión
conexion = mysql.connector.connect(
                              host='cloud.eant.tech',
                              database='pdp_base024',
                              user='pdp_usuario024',
                              password='eantpass')
cursor = conexion.cursor()

sql = "SELECT dni FROM alumnos"

cursor.execute(sql)
#alumnos = cursor.fetchall()#Devuelve un lista de tuplas con la información

for alumno in cursor:
     print(alumno[0])

cursor.close()
conexion.close()