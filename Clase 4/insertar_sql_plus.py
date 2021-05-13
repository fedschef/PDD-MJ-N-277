import mysql.connector
#Establecer la conexión
conexion = mysql.connector.connect(
                              host='cloud.eant.tech',
                              database='',
                              user='',
                              password='eantpass')
cursor = conexion.cursor()
dnis = []
cursor.execute("SELECT dni FROM alumnos")
for dni in cursor:
   dnis.append(dni[0])

while True:
   dni = input("Ingrese el dni del alumno: ")
   if int(dni) in dnis: print("Este alumno ya fue ingresado en la base de datos")
   else:
      nombre = input("Ingrese el nombre del alumno: ")
      apellido = input("Ingrese el apellido del alumno: ") 
      email = input("Ingrese el email del alumno: ")
      fecha_nac = input("Ingrese la fecha de nacimiento del alumno (AAAA-MM-DD): ")
      sql = "INSERT INTO alumnos(nombre, apellido, dni, email, fecha_nac)\
         VALUES(%s,%s,%s,%s,%s)"
      cursor.execute(sql, (nombre, apellido, dni, email, fecha_nac))
      dnis.append(int(dni))
   nuevo = input("Querés ingresar un nuevo registro? s/n: ").upper()
   if nuevo == 'N': break
conexion.commit()
print("Datos subidos")
cursor.close()
conexion.close()