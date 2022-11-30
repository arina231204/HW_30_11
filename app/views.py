from flask import render_template,redirect, url_for, request, flash
from app import db
from .models import Transaction, User
from .forms import TransactionForm,UserForm
from flask_login import login_user, logout_user, login_required

def transactions_list():
    transactions = Transaction.query.all()
    return render_template('transactions_list.html',transactions=transactions )


@login_required
def transaction_create():
    form = TransactionForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            transaction = Transaction()
            form.populate_obj(transaction)
            db.session.add(transaction)
            db.session.commit()
            flash('Tранзакция сохранена', 'success')
            return redirect(url_for('transactions_list'))
    return render_template('transaction_form.html', form=form)

def transaction_detail(id):
    transaction = Transaction.query.get(id)
    return render_template('transaction_detail.html', transaction=transaction)


@login_required
def transaction_update(id):
    transaction = Transaction.query.get(id)
    form = TransactionForm(request.form, obj=transaction)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(transaction)
            db.session.add(transaction)
            db.session.commit()
            return redirect(url_for('transactions_list'))
    return render_template('transaction_form.html', form=form)


@login_required
def transaction_delete(id):
    transaction = Transaction.query.get(id)
    if request.method == 'POST':
        db.session.delete(transaction)
        db.session.commit()
        return redirect(url_for('transactions_list'))
    return render_template('transaction_delete.html', transaction=transaction)


def register_view():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            flash (f'Пользователь {user.username} успешно зарегистрирован', 'success')
            return redirect(url_for('login'))
    return render_template('user_form.html', form=form)


def login():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                db.session.add(user)
                db.session.commit()

                flash('Успешно авторизован', 'primary')
                return redirect(url_for('transactions_list'))
            else:
                flash('Неправильно введены данные', 'danger')
    return render_template('user_login_form.html', form=form)

def logout_view():
    logout_user()
    return redirect(url_for('login'))