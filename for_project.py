# Додавання нотатки
def add_note(text, tags, notes):
    new_note = {"text": text, "tags": tags}
    notes.append(new_note)
    print("Нотатка була успішно додана.")


# Редагування інформації про нотатку
def edit_note(index, text, tags, notes):
    if 0 <= index < len(notes):
        notes[index]["text"] = text
        notes[index]["tags"] = tags
        print(f"Нотатка під індексом {index} була успішно відредагована.")
    else:
        print(f"Нотатки з індексом {index} не існує. Редагування неможливе.")


# Видалення нотатки за індексом
def delete_note(title, notes):
    for note in notes:
        if note['title'] == title:
            notes.remove(note)
            print(f"Нотатка з назвою '{title}' була успішно видалена.")
            return
    print(f"Нотатки з назвою '{title}' не існує. Видалення неможливе.")

