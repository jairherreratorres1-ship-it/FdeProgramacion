email = [
    'ana@gmail.com',
    'luis@outlook.com',
    'mia@gmail.com',
    'juan@yahoo.com'
]

cuenta_emails = sum(1 for gmail in email if gmail.endswith('gmail.com'))
print(f"Cantidad de correos que terminan con gmail.com: {cuenta_emails}")

for com in email:
    if com.endswith('.com'):
        print(com)

cuenta_luis = 'luis@outlook.com' in email
print(f"¿El correo de Luis está en la lista? {cuenta_luis}")