from flask import Blueprint, request, jsonify
from model.Predio import Predio
from model.Predio import Tipo_Predio
from utils.db import db

Predios=Blueprint('Predios',__name__)

@Predios.route('/Predios/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@Predios.route('/Predios/v1/listar',methods=['GET'])
def getPredios():
    result={}
    Predios=Predio.query.all()    
    result["data"]=Predios
    result["status_code"]=200
    result["msg"]="Se recupero los contactos sin inconvenientes"
    return jsonify(result),200

@Predios.route('/Predios/v1/insert',methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo= body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    Predios=Predio(id_tipo_predio,descripcion,ruc,telefono,correo,direccion,idubigeo)
    db.session.add(Predios)
    db.session.commit()
    result["data"]=Predios
    result["status_code"]=201
    result["msg"]="Se agrego el contacto"
    return jsonify(result),201

@Predios.route('/Predios/v1/update',methods=['POST'])
def update():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo= body.get('idubigeo')
    
    if not id_predio or not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    Predios=Predio.query.get(id_predio)
    if not Predios:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    Predios.id_tipo_predio=id_tipo_predio
    Predios.descripcion=descripcion
    Predios.ruc=ruc    
    Predios.telefono=telefono
    Predios.correo= correo
    Predios.direccion = direccion
    Predios.idubigeo = idubigeo
    db.session.commit()
    
    result["data"]=Predios
    result["status_code"]=202
    result["msg"]="Se modificó el contacto"
    return jsonify(result),202

@Predios.route('/Predios/v1/delete',methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')    
    if not id_predio:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400
    
    Predios=Predio.query.get(id_predio)
    if not Predios:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    db.session.delete(Predios)
    db.session.commit()
    
    result["data"]=Predios
    result["status_code"]=200
    result["msg"]="Se eliminó el contacto"
    return jsonify(result),200

Tipo_Predios=Blueprint('Tipo_Predios',__name__)

@Tipo_Predios.route('/Tipo_Predios/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@Tipo_Predios.route('/Tipo_Predios/v1/listar',methods=['GET'])
def getTipo_Predios():
    result={}
    Tipo_Predios=Tipo_Predio.query.all()    
    result["data"]=Tipo_Predios
    result["status_code"]=200
    result["msg"]="Se recupero los contactos sin inconvenientes"
    return jsonify(result),200

@Tipo_Predios.route('/Tipo_Predios/v1/insert',methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    nomre_predio=body.get('nomre_predio')
    
    if not nomre_predio:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    Tipo_Predios=Tipo_Predio(nomre_predio)
    db.session.add(Tipo_Predios)
    db.session.commit()
    result["data"]=Tipo_Predios
    result["status_code"]=201
    result["msg"]="Se agrego el contacto"
    return jsonify(result),201

@Tipo_Predios.route('/Tipo_Predios/v1/update',methods=['POST'])
def update():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')
    nomre_predio=body.get('nomre_predio') 
    
    if not id_tipo_predio or not nomre_predio:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    Tipo_Predios=Tipo_Predio.query.get(id_tipo_predio)
    if not Tipo_Predios:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    Tipo_Predios.id_tipo_predio=id_tipo_predio
    Tipo_Predios.nomre_predio=nomre_predio
    db.session.commit()
    
    result["data"]=Tipo_Predios
    result["status_code"]=202
    result["msg"]="Se modificó el contacto"
    return jsonify(result),202

@Tipo_Predios.route('/Tipo_Predios/v1/delete',methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')    
    if not id_tipo_predio:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400
    
    Tipo_Predios=Tipo_Predio.query.get(id_tipo_predio)
    if not Tipo_Predios:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    db.session.delete(Tipo_Predios)
    db.session.commit()
    
    result["data"]=Tipo_Predios
    result["status_code"]=200
    result["msg"]="Se eliminó el contacto"
    return jsonify(result),200