# -*- coding: utf-8 -*-

from flask import Flask, jsonify, redirect
import mysql.connector

app = Flask(__name__)

# Ruta de inicio para redirigir a la lista de productos
@app.route('/')
def inicio():
    return redirect('/productos')

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        # Establecer conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhostmysql.mysql.database.azure.com',
            user='rootAlex',
            password='contrasena123$',
            database='pruebabdd_2'
        )

        cursor = conexion.cursor()

        # Consulta SQL para obtener los productos
        consulta = "SELECT idProductos, nombre, descripcion, precio FROM productos"
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

        # Crear una lista de productos utilizando una comprensión de lista
        productos = [{
            "idProductos": producto[0],
            "nombre": producto[1],
            "descripcion": producto[2],
            "precio": producto[3]
        } for producto in resultados]

        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()

        # Devolver la lista de productos como respuesta en formato JSON
        return jsonify(productos)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para crear un nuevo producto (POST)
@app.route('/productos', methods=['POST'])
def crear_producto():
    return jsonify({'message': 'Función de crear producto desactivada'})

# Ruta para actualizar un producto existente (PUT)
@app.route('/productos/<int:idProducto>', methods=['PUT'])
def actualizar_producto(idProducto):
    return jsonify({'message': 'Función de actualizar producto desactivada'})

# Ruta para eliminar un producto existente (DELETE)
@app.route('/productos/<int:idProducto>', methods=['DELETE'])
def eliminar_producto(idProducto):
    return jsonify({'message': 'Función de eliminar producto desactivada'})

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
