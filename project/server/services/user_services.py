# /usr/bin/env python3

import datetime
import jwt

# from project.server import app, bcrypt
from project.server.domain import user_domain
from project.server.models import user_models


def encode_auth_token(user_id):
    """ Generates the Auth Token.
        
        Args:
            user_id: User ID of the user.

        Returns: str.
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """ Validates the auth token.
        
        Args:
            auth_token: str. Authorization token for the session.
        
        Returns:
            int|str: 
    """
    try:
        jwt.decode(auth_token, app.config.get('SECRET_KEY'))
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def get_user_from_model(user_data_model):
    return user_domain.UserDomain(
        user_data_model.id,
        user_data_model.username, user_data_model.email,
        user_data_model.password,
        user_data_model.first_name, user_data_model.last_name,
        user_data_model.gender, user_data_model.contact_number,
        user_data_model.profile_picture, user_data_model.organisation,
        user_data_model.subscription
    )


def get_user_by_user_id(user_id):
    """Gets the user by user ID.
    
        Args:
            user_id: str. User ID of the user.
        
        Returns:
            UserDomain.
    """
    user_data_model = user_models.UserModel.objects(user_id=user_id).first()
    user = get_user_from_model(user_data_model)
    return user


def get_user_by_email_id(email_id):
    """Gets the user by email ID.
    
        Args:
            email_id: str. Email ID of the user.
        
        Returns:
            UserDomain.
    """
    user_data_model = user_models.UserModel.objects(email=email_id).first()
    user = get_user_from_model(user_data_model)
    return user
    

def create_user_model_from_data(
    username, password, email, first_name, last_name, gender,
    contact_number, profile_picture, organisation, subscription):
    
    user = user_models.UserModel(
        username = username,
        email = email,
        password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode(),
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        contact_number = contact_number,
        profile_picture = profile_picture,
        organisation = organisation,
        subscription = subscription
    )
    user.save()
