from password_validator import PasswordValidator


schema = PasswordValidator()

schema.min(8)  
schema.max(20)  
schema.has().uppercase()  
schema.has().lowercase()  
schema.has().digits()  
schema.has().symbols()  


def validate_password(password: str) -> bool:
    if ' ' in password:
        return False
    return schema.validate(password)