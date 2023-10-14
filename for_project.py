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
def delete_note(index, notes):
    if 0 <= index < len(notes):
        deleted_note = notes.pop(index)
        print(f"Нотатка під індексом {index} була успішно видалена.")
        return deleted_note
    else:
        print(f"Нотатки з індексом {index} не існує. Видалення неможливе.")
        return None
