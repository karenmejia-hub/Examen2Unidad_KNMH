
import mysql.connector.connect

conexion = mysql.connector.connect(  # type: ignore
    host="localhost", user="root", password="123456789", database="Restaurante_db"
)


print("BIENVENIDO AL SITEMA DE RESTAURANTE ")
while True:
    print("SELECCIONE UNA OPCION")
    print("1. Agregar un plato")
    print("2. Eliminar un plato")
    print("3. Mostrar menu ")
    print("4. Salir ")

    op = int(input("R// "))

    if op == 1:  # añadir un plato nuevo
        nuevoplato = input("Escriba el nombre del plato nuevo").strip
        if nuevoplato:
            sql = "INSERT INTO platos (nombre) VALUES (%s)"
            values = nuevoplato
            cursor.execute(sql, values)
            conexion.commit()
            print(f"nuevo plato agregado {nuevoplato} con exito")
        else:
            print("Error al intentar agregar el nuevo palto. intentelo de nuevo")

    elif op == 2:  # eliminar un plato
        eliminarplato = input("Ingrese el nombre del plato a eliminar").strip
        sql = "DELETE FROM platos WHERE nombre = %s"
        values = eliminarplato
        cursor.execute(sql, values)
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"Plato eliminado {eliminarplato} con exito")
        else:
            print("Error. no se pudo eliminar el plato.")

    elif op == 3:  # mostrar el menu.
        cursor.execute("SELECT id, nombre FROM platos")
        platos = cursor.fetchall()
        if len(platos) == 0:
            print("No hay platos. Anañada ")
        else:
            print("Catalogo de platos")
            for plato in platos:
                print(f"libro {plato[0]}, {platos[1]}")
    elif op == 4:
        print("Saliendo...")
        cursor.closed()
        conexion.closed()
        break
    else:
        print("Intentelo de nuevo. Datos incorrectos.")