from flask import Flask,render_template,url_for, flash, redirect, Response, request
from forms import Test
import mri_dementia

app = Flask(__name__)  # Flask looks for templates and static files here

app.config['SECRET_KEY'] = '6556fe38b5b2fcfa663b130766ceaf66'

@app.route('/')
@app.route('/home')   # Home page of website
def home():
    return render_template('home.html',title='HOME PAGE')


@app.route('/test',methods=['GET','POST'])
def test():
    form = Test()
    if form.is_submitted():
        try:
            Name= form.Name.data
            gender= int(request.form.get('Gender'))
            age = form.Age.data
            educ = form.YoE.data
            SES = int(request.form.get('SES'))
            MMSE = form.MMSE.data
            CDR = float(request.form.get('CDR'))
            eTIV = form.eTIV.data
            ASF = float(form.ASF.data)
            nWBV = float(form.nWBV.data)

            Result = mri_dementia.main(gender,age,educ,SES,MMSE,CDR,eTIV,nWBV,ASF)
            if(Result[0]=="Demented"):
                flash("{0}, you might have Dementia leading to Alzheimers!".format(Name), 'success')
            else:
                flash("{0}, you don't have Dementia!".format(Name), 'success')
            return redirect(url_for('home'))
        except Exception as e:
            print(e)    

    return render_template('test.html',form=form)



if __name__=='__main__':
    app.run(debug=True)
