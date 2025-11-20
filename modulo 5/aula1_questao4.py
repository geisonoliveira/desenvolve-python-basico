from datetime import datetime

now = datetime.now()
print(f"Data: {now.strftime('%d/%m/%Y')}")
print(f"Hora: {now.strftime('%H:%M')}")