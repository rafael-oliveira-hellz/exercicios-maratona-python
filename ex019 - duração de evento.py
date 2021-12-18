hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duracao = int(input("Event duration (minutes): "))

# Write your code here.
final_mins = (mins + duracao) % 60

final_hour = (hour + (mins + duracao) // 60) % 24

print(f'\n O fim do evento se dará às {final_hour}:{final_mins}.')