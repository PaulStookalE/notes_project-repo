from . import app
from flask import redirect, render_template, request
from .models import session, Notes



# Створення головної сторінки, де виводитимуться всі нотатки.
@app.route('/')
def read_all_notes():
    notes = session.query(Notes).all()
    return render_template('read_all_notes.html', notes=notes)



# Створення сторінки з таблицею з деталями про конкретну нотатку.
@app.route('/read_note/<int:id>')
def read_note(id):
    note_details = session.query(Notes).get(id)
    return render_template('read_note.html', note_details=note_details)



# Створення сторінки для зміни нотатки.
@app.route('/update_note/<int:id>', methods=['GET', 'POST'])
def update_note(id):
    note_details = session.query(Notes).get(id)

    if request.method == 'POST':
        
        try:

            heading = request.form['heading']
            text = request.form['text']

            note_details.heading = heading
            note_details.text = text

            session.commit()

            return redirect('/')
        
        except Exception as exc:
            return exc
        
        finally:
            session.close()

    else:
        return render_template('update_note.html', note_details=note_details)
    


# Створення сторінки для видалення нотатки.
@app.route('/delete_note/<int:id>')
def delete_note(id):
    note_to_delete = session.query(Notes).get(id)

    if note_to_delete:
        session.delete(note_to_delete)
        session.commit()

    session.close()

    return redirect('/')



# Створення сторінки з формою для вводу для створення нової нотатки.
@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    
    if request.method == 'POST':
        
        heading = request.form['heading']
        text = request.form['text']

        new_note = Notes(
            heading = heading,
            text = text
        )

        try:
            
            session.add(new_note)
            session.commit()

            return redirect('/')
        
        except Exception as exc:
            return exc
        
        finally:
            session.close()

    else:
        return render_template('create_note.html')