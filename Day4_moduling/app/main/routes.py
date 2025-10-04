from flask import render_template, flash
from app.main import main_bp
from app.forms.registration import RegistrationForm

@main_bp.route('/')
def basic():
    register_form = RegistrationForm()
    return render_template('registerroute.html', register_form=register_form)

@main_bp.route('/register', methods=['GET', 'POST'])
def registerform():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        name = register_form.name.data
        password = register_form.password.data
        email = register_form.email.data
        confirm_password = register_form.confirm_password.data

        flash('Data has been saved', 'success')
        return render_template('thanks.html', register_form=register_form)
    return render_template('registerroute.html', register_form=register_form)
