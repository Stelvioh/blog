from marshmallow import Schema, fields, validate

class PostDto(Schema):
    id = fields.Int(dump_only=True)  # dump_only significa que esse campo só será serializado, não deserializado.
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))  # Títulos entre 1 a 200 caracteres
    content = fields.Str(required=True)  # Você pode adicionar validações de comprimento, se necessário.
    author_id = fields.Int(required=True)  # Id do autor do post
