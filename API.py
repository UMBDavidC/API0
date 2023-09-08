from flask import Flask, jsonify, request,render_template
import mysql.connector
#import os
import random

app = Flask(__name__)

#Funcion para consultar un alimento aleatorio entre los alimentos del desayuno
def products_Select(random_id):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    #Codigo para un numero random
    random_id = random.randint(1, 5)
    sql = "Select * from Desayuno where id = %s"
    val = (random_id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult

#Funcion para insertar un alimento en la tabla Desayuno
def products_Insert(Dcodigo , Dnombre_ali, Dprecio_ali):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO Desayuno (id, alimento, Precio) VALUES (%s, %s, %s)"
    val = (Dcodigo, Dnombre_ali,Dprecio_ali)
    mycursor.execute(sql,val)
    mydb.commit()
    return True

# Función para actualizar un registro en la base de datos en la tabla Desayuno
def products_Update(codigo, nuevo_nombre,  nuevo_precio):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "UPDATE Desayuno SET alimento = %s, Precio = %s WHERE id = %s"
    val = (nuevo_nombre, nuevo_precio, codigo)
    mycursor.execute(sql, val)
    mydb.commit()
    return True

# Función para eliminar un registro de la base de datos en la tabla Desayuno
def products_Delete(codigo):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM Desayuno WHERE id = %s"
    val = (codigo,)
    mycursor.execute(sql, val)
    mydb.commit()
    return True

#---------------------------------------------------------------------------------------------------------------

#Funcion para consultar un alimento aleatorio entre los alimentos del Almuerzo
def products_Select_Al(random_idA):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    #Codigo para un numero random
    random_idA = random.randint(1, 10)
    sql = "Select * from Almuerzo where id_Al = %s"
    val = (random_idA,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult

#Funcion para insertar un alimento en la tabla Almuerzo
def products_Insert_Al(codigo , nombre_ali, precio_ali):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO Almuerzo (id_Al, alimento, Precio) VALUES (%s, %s, %s)"
    val = (codigo, nombre_ali,precio_ali)
    mycursor.execute(sql,val)
    mydb.commit()
    return True

# Función para actualizar un registro en la base de datos en la tabla Almuerzo
def products_Update_Al(codigo, nuevo_nombre, nuevo_precio):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "UPDATE Almuerzo SET alimento = %s, Precio = %s WHERE id_Al = %s"
    val = (nuevo_nombre, nuevo_precio,codigo)
    mycursor.execute(sql, val)
    mydb.commit()
    return True

# Función para eliminar un registro de la base de datos en la tabla Almuerzo
def products_Delete_Al(codigo):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM Almuerzo WHERE id_Al = %s"
    val = (codigo,)
    mycursor.execute(sql, val)
    mydb.commit()
    return True

#---------------------------------------------------------------------------------------


#Funcion para consultar un alimento aleatorio entre los alimentos de la Cena
def products_Select_Ce(random_idC):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    #Codigo para un numero random
    random_idC = random.randint(1, 5)
    sql = "Select * from Cena where id_Cen = %s"
    val = (random_idC,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult

#Funcion para insertar un alimento en la tabla Cena
def products_Insert_Ce(codigo , nombre_ali, precio_ali):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO Cena (id_Cen, alimento, Precio) VALUES (%s, %s, %s)"
    val = (codigo, nombre_ali,precio_ali)
    mycursor.execute(sql,val)
    mydb.commit()
    return True

# Función para actualizar un registro en la base de datos en la tabla Cena
def products_Update_Ce(codigo, nuevo_nombre, nuevo_precio):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "UPDATE Cena SET alimento = %s, Precio = %s WHERE id_Cen = %s"
    val = (nuevo_nombre, nuevo_precio, codigo)
    mycursor.execute(sql, val)
    mydb.commit()
    return True

# Función para eliminar un registro de la base de datos en la tabla Cena
def products_Delete_Ce(codigo):
    mydb = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10644883",
        password="PmqFHiXd2e",
        database="sql10644883",
        port=3306
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM Cena WHERE id_Cen = %s"
    val = (codigo,)
    mycursor.execute(sql, val)
    mydb.commit()
    return True

#-----------------------------------------------------------------------------------------

#Endpoint de la pagina de inicio
@app.route('/')
def index():
    return render_template('index.html')

#Endpoint get de desayuno
@app.route('/Desayuno', methods=['GET'])
def products_get():
    args = request.args
    s_category = args.get("Desayuno")
    respuesta = products_Select(s_category)
    return jsonify({"msg":"success","Desayuno":respuesta})

#Endpoint post del Desayuno
@app.route('/Desayuno', methods=['POST'])
def Desayunopost():
    try:
        alimento_codigo = request.form['codigo']
        alimento_nombre = request.form['nombre_ali']
        alimento_precio = request.form['precio_ali']
        respuesta = products_Insert(alimento_codigo,alimento_nombre,alimento_precio)
        if(respuesta):
            return jsonify({"message":"success"})
    except Exception as e:
        return jsonify({"message":"Error. " + str(e)}), 400 

#Endpoint put de la tabla Desayuno
@app.route('/Desayuno', methods=['PUT'])
def products_put():
    try:
        alimento_codigo = request.form['codigo']
        nuevo_nombre = request.form['nombre_ali']
        nuevo_precio = request.form['precio_ali']
        respuesta = products_Update(alimento_codigo, nuevo_nombre, nuevo_precio)
        if respuesta:
            return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({"message": "Error. " + str(e)}), 400

#Endpoint delete de la tabla Desayuno
@app.route('/Desayuno', methods=['DELETE'])
def products_delete():
    try:
        alimento_codigo = request.form['codigo']
        respuesta = products_Delete(alimento_codigo)  
        if respuesta:
            return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({"message": "Error. " + str(e)}), 400

#----------------------------------------------------------------------------

#Endpoint get de Almuerozo
@app.route('/Almuerzo', methods=['GET'])
def Almuerzo_products_get():
    args = request.args
    s_category = args.get("Almuerzo")
    respuesta = products_Select_Al(s_category)
    return jsonify({"msg":"success","Almuerzo":respuesta})

#Endpoint post del Almuerozo
@app.route('/Almuerzo', methods=['POST'])
def Almuerzo_post():
    try:
        alimento_codigo = request.form['codigo']
        alimento_nombre = request.form['nombre_ali']
        alimento_precio = request.form['precio_ali']
        respuesta = products_Insert_Al(alimento_codigo,alimento_nombre,alimento_precio)
        if(respuesta):
            return jsonify({"message":"success"})
    except Exception as e:
        return jsonify({"message":"Error. " + str(e)}), 400 

#Endpoint put de la tabla Almuerozo
@app.route('/Almuerzo', methods=['PUT'])
def Almuerzo_put():
    try:
        alimento_codigo = request.form['codigo']
        nuevo_nombre = request.form['nombre_ali']
        nuevo_precio = request.form['precio_ali']
        respuesta = products_Update_Al(alimento_codigo, nuevo_nombre, nuevo_precio)
        if respuesta:
            return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({"message": "Error. " + str(e)}), 400

#Endpoint delete de la tabla Almuerozo
@app.route('/Almuerzo', methods=['DELETE'])
def Almuerzo_products_delete():
    try:
        alimento_codigo = request.form['codigo']
        respuesta = products_Delete_Al(alimento_codigo)  
        if respuesta:
            return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({"message": "Error. " + str(e)}), 400

#---------------------------------------------------------------------------------------

#Endpoint get de Cena
@app.route('/Cena', methods=['GET'])
def Cena_products_get():
    args = request.args
    s_category = args.get("Cena")
    respuesta = products_Select_Ce(s_category)
    return jsonify({"msg":"success","Cena":respuesta})

#Endpoint post de la Cena
@app.route('/Cena', methods=['POST'])
def Cena_post():
    try:
        alimento_codigo = request.form['codigo']
        alimento_nombre = request.form['nombre_ali']
        alimento_precio = request.form['precio_ali']
        respuesta = products_Insert_Ce(alimento_codigo,alimento_nombre,alimento_precio)
        if(respuesta):
            return jsonify({"message":"success"})
    except Exception as e:
        return jsonify({"message":"Error. " + str(e)}), 400 

#Endpoint put de la tabla Cena
@app.route('/Cena', methods=['PUT'])
def Cena_put():
    try:
        alimento_codigo = request.form['codigo']
        nuevo_nombre = request.form['nombre_ali']
        nuevo_precio = request.form['precio_ali']
        respuesta = products_Update_Ce(alimento_codigo, nuevo_nombre, nuevo_precio)
        if respuesta:
            return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({"message": "Error. " + str(e)}), 400

#Endpoint delete de la tabla Cena
@app.route('/Cena', methods=['DELETE'])
def Cena_products_delete():
    try:
        alimento_codigo = request.form['codigo']
        respuesta = products_Delete_Ce(alimento_codigo)  
        if respuesta:
            return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({"message": "Error. " + str(e)}), 400



if __name__ == '__main__':
    app.run(debug=True) 
    #app.run(debug=True, port=os.getenv("PORT", default=5000 )) 

