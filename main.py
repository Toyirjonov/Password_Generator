import random
import string

def generate_password(length=8):
    
    characters = string.ascii_letters  
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Введите длину пароля (по умолчанию 8): ") or 8)
    except ValueError:
        print("Введите корректное число.")
        return
    
    password = generate_password(length)
    print(f"Ваш сгенерированный пароль: {password}")

if __name__ == "__main__":
    main()
