from csv import DictReader
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
    try:
        students_data = list()
        with open('students.csv') as f:
            reader = DictReader(f, delimiter=';')
            for student in reader:
                students_data.append(student)
        return students_data
    except FileNotFoundError:
        print('There is no students.csv file in directory')
        return False


def personalize_message(message, student):
    current_message = message.replace('[name]', student['name'])
    current_message = current_message.replace('[surname]', student['surname'])
    current_message = current_message.replace('[missing tasks]', str(student['missing_tasks']))
    grade = student['marks'].split(',')
    grade = [int(i.strip()) for i in grade]
    grade = sum(grade) // len(grade)
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
    if not students_data:
        return
    write_messages(message_text, students_data)


if __name__ == '__main__':
    main()
