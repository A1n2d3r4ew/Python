# За день машина проезжает n километров.Сколько дней нужно, чтобы проехать
# маршрут длиной m километров?

n = int(input("Введите количество км:  \n"))
m = int(input("Введите количество всех км\n"))

print(-(-m//n))