from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Optional

class EmpresaForm(FlaskForm):
    nome_empresa = StringField('Nome da Empresa', validators=[DataRequired(), Length(max=255)])
    nif = StringField('NIF (Número de Identificação Fiscal)', validators=[
        DataRequired(),
        Length(min=9, max=9, message="O NIF deve ter 9 dígitos"),
        Regexp(r'^\d{9}$', message="O NIF deve conter apenas dígitos")
    ])
    endereco = StringField('Endereço', validators=[DataRequired(), Length(max=255)])
    codigo_postal = StringField('Código Postal', validators=[
        DataRequired(),
        Regexp(r'^\d{4}-\d{3}$', message="Código Postal deve estar no formato 1234-567")
    ])
    localidade = StringField('Localidade', validators=[DataRequired(), Length(max=255)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=255)])
    telefone = TelField('Telefone', validators=[
        DataRequired(),
        Regexp(r'^\d{9}$', message="O telefone deve ter 9 dígitos")
    ])
    website = URLField('Website (Opcional)', validators=[Optional(), Length(max=255)])
    submit = SubmitField('Registar Empresa')