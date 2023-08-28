from marshmallow import Schema, fields, validate

class UserDto(Schema):
    id = fields.Int(dump_only=True)  # dump_only significa que esse campo só será serializado, não deserializado.
    username = fields.Str(required=True, validate=validate.Length(min=2, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=6, max=120))  # Senha deve ser tratada com cuidado
    email = fields.Email(required=True, validate=validate.Length(max=120))
    name = fields.Str(required=True, validate=validate.Length(min=2, max=120))
    cpf = fields.Str(required=True, validate=validate.Length(equal=11))  # CPF deve sempre ter 11 caracteres
    roles = fields.Str()
