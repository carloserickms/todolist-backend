from app.db_config import db
from app.models.tables.user import User
from flask import jsonify, request, Blueprint
from app.models.schemas.user_schema import UserSchema
from werkzeug.security import generate_password_hash, check_password_hash
import os, jwt


user_route = Blueprint('user_routes', __name__)

@user_route.route('/api/v1/user/create_user', methods=["POST"])
def create_user():
    if request.method == 'POST':
        try:
            body = request.get_json()
            username = body['username']
            password = body['password']
            re_password = body['re_password']

            if password != re_password:
                return jsonify({
                    'status': 'error',
                    'message': 'Atenção, Senhas não coencidem'
                }), 400
            
            password_hash = generate_password_hash(password)

            user = User(username=username, password_hash=password_hash)
            db.session.add(user)
            db.session.commit()
            db.session.close()

            return jsonify({
                'status': 'ok',
                'message': 'Usuário cadastrado com secesso!'
            }), 201
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        

@user_route.route('/api/v1/user/delete_user/<string:user_id>', methods=["DELETE"])
def delete_user(user_id):
    
    user = User.query.get(user_id)

    if not user:
        return jsonify({
            'status': 'error',
            'message': 'Usuário não existe na base de dados.'
        }), 404
    
    try:
        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Usuário removido!'
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': f'Erro ao deletar: {str(e)}'
        }), 500