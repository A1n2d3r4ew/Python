# Напишите программу для печати всех 
# уникальных значений в словаре.

# [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"V":"S005"},
# {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

# {'S005','S002','S007','S009'}


list_dict = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},
{"V":"S005"},{"VII":" S005 "},{"V":" S009 "},{"VIII":" S007 "}]

print(set(list(i.values())[0].strip() for i in list_dict))
