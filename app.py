from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

# Database Model
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# Create the DB on first run
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = InventoryItem.query.order_by(InventoryItem.date_added.desc()).all()
    total = sum([item.quantity for item in items])
    return render_template('index.html', items=items, total=total)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['item_name']
    quantity = int(request.form['item_qty'])
    category = request.form['item_category']
    if name and quantity:
        new_item = InventoryItem(name=name, quantity=quantity, category=category)
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
