from app import db, Person, app

with app.app_context():
    db.create_all()

    kapil = Person('Kapil', 67)
    modi = Person('Modi', 34)
    print(kapil.id)  # Prints assigned ID
    print(modi.id)

    db.session.add_all([kapil, modi])
    db.session.commit()

    print(kapil.id)  # Prints assigned ID
    print(modi.id)  # Prints assigned ID
