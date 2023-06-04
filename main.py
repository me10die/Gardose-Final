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


@app.route('/empti/')
def empti_details(empti_ID):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursor.DictCursor)
        cursor.execute("SELECT customerID, name, age, phone, address FROM empti WHERE customerID = %s", empti_ID)
        emptiRow = cursor.fetchone()
        response = jsonify(emptiRow)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['PUT'])
def update_empti():
    try:
        _json = request.json
        _customerID = _json['customerID']
        _name = _json['name']
        _age = _json['age']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _age and _phone and _address and _customerID and request.method == 'PUT':
            sqlQuery = "UPDATE empti SET name=%s, age=%s, phone=%s, address=%s WHERE customerID=%s"
            bindData = (_name, _age, _phone, _address, _customerID,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify("The Data updated successfully!")
            response.status_code = 200
            return response
        else:
            return showMessage()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


@app.route('/delete/', methods=['DELETE'])
def delete_empti(customerID):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM empti WHERE customerID=%s", (customerID))
        conn.commit()
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()