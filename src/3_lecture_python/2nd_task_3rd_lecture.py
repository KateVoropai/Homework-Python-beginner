def people_not_read_required_literature(required_literature, literature):
    people_read_required_lit = set()
    for book in required_literature:
        people_read_required_lit.add(literature[book])
    people_not_read_required_lit = people - people_read_required_lit
    return people_not_read_required_lit
    
    
people = {"Васильева В.М.", "Новиков С.В.", "Артемов А.И.", "Филиппова А.Н.", "Мартынова В.И.", 
        "Романова С.М.", "Носков Г.B.", "Журавлева М.Е.", "Сойко В.В.", "Козлов С.Д."}

read_literature = {'book1', 'book2', 'book3', 'book4', 'book5', 'book6', 'book7', 'book8', 'book9', 'book10'}

required_literature = {'book1', 'book3', 'book5', 'book7', 'book10'}

literature = dict(zip(read_literature, people))

print(people_not_read_required_literature(required_literature, literature))