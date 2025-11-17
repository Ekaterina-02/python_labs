def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        return ValueError
    if type(rec[0]) != str or type(rec[1]) != str:
        return ValueError
    if type(rec[2]) != float:
        return ValueError
    fio = rec[0].split()
    group = rec[1]
    gpa_new = rec[2]
    gpa = f"{gpa_new:.2f}"
    fio1 = ""
    f = 0

    for i in range(len(fio)):
        if fio[i] != "" and f == 0:
            first = fio[i][0].upper()
            fio1 = first + fio[i][1:]
            f = 1
        elif fio[i] != "" and f == 1:
            first = fio[i][0].upper()
            fio1 = fio1 + " " + first + "."
    result = f"{fio1},гр. {group}, GPA {gpa}"
    return result


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
