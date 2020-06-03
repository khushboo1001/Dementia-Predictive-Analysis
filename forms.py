from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class Test(FlaskForm):

    Gender_Select=[('','Gender'),(1, 'Male'),(0, 'Female')]
    SES_Select=[('','Socio Economic Status'),(5,  'Poor'),(4 , 'Lower Middle Class'),(3, 'Middle Class'),(2 , 'Upper Middle Class'),(1 , 'Rich')]
    CDR_Select=[('', 'Clinical Dementia Rating'),(0,'Not Demented'),(0.5,'Mildly Demented'),(1,'Moderately Demented')]
    
    Name=StringField('Name',validators=[DataRequired()], render_kw={ "placeholder" : "Name"})
    Email=StringField('EmailID',validators=[DataRequired()], render_kw={ "placeholder" : "Email"})

    Gender=SelectField('Gender',choices=Gender_Select)
    Age=IntegerField('Age',validators=[DataRequired()], render_kw={ "placeholder" : "Age"})
    YoE=IntegerField('Eudc',validators=[DataRequired()], render_kw={ "placeholder" : "Years of Education"})

    SES=SelectField('SES',choices=SES_Select)

    MMSE=IntegerField('MMSE',validators=[DataRequired()], render_kw={ "placeholder" : "Mini Mental State Examination"})
    
    CDR=SelectField('CDR', choices=CDR_Select)
    
    eTIV=IntegerField('eTIV',validators=[DataRequired()], render_kw={ "placeholder" : "Estimated Total Intracranial Volume (mm3)"})
    ASF=StringField('ASF',validators=[DataRequired()], render_kw={ "placeholder" : "Atlas Scaling Factor"})
    nWBV=StringField('nWBV',validators=[DataRequired()], render_kw={ "placeholder" : "Normalized Whole Brain Volume"})
    
    submit=SubmitField('CHECK')
