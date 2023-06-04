import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/create', methods=['POST'])
def create_empti():
    try:
        _json = request.json
        _name = _json['name']
        _age = _json['age']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _age and _phone and _address and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO empti(name, age, phone, address) VALUES(%s, %s, %s, %s)"
            bindData = (_name, _age, _phone, _address)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('The data added succesfully!')
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/empti')
def empti():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT customerID, name, email, phone, address FROM empti")
        emptiRow = cursor.fetchone()
        response = jsonify(epmtiRow)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

