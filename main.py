date = '15.07.2022'


def read_message_file():
    try:
        with open('message.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("File message.txt was not found")
    else:
        return content


def get_data():
    """currently data typed in program, in future data will be from csv file"""
    students_data = list()
    tmp_data = {'names': 'James Smith', 'missing_assignments': [3, 4], 'mark': [4]}
    students_data.append(tmp_data)
    tmp_data = {'names': 'Basil Cooper', 'missing_assignments': [7, 8], 'mark': [4, 3, 4, 2]}
    students_data.append(tmp_data)
    tmp_data = {'names': 'Audrey Baldwin', 'missing_assignments': [1, 2], 'mark': [5, 4, 3, 4, 2]}
    students_data.append(tmp_data)
    return students_data


def personalize_message(message, student):
    current_message = message.replace('[name]', student['names'])
    current_message = current_message.replace('[missing tasks]', str(student['missing_assignments']))
    grade = sum(student['mark']) // len(student['mark'])
    current_message = current_message.replace('[current grade]', str(grade))
    current_message = current_message.replace('[potential grade]', str(grade + 1))
    current_message = current_message.replace('[date]', date)
    return current_message


def write_messages(message, students_data):
    for student in students_data:
        print(personalize_message(message, student))
        print('\n' * 3)


def main():
    message_text = read_message_file()
    students_data = get_data()
    write_messages(message_text, students_data)


if __name__ == '__main__':
    main()
