import math

def calculate_factorial(n):
    """Функция для вычисления факториала числа."""
    return math.factorial(n)

def main():
    while True:
        user_input = input("Введите положительное целое число для вычисления его факториала: ")
        
        try:
            # Проверка, что введенные данные числовые
            number = int(user_input)
            
            # Проверка, что число положительное
            if number < 0:
                raise ValueError("Введите положительное число.")
            
            # Вычисление факториала
            result = calculate_factorial(number)
            print(f"Факториал числа {number} равен {result}.")
            break  # Выход из цикла после успешного вычисления
            
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
