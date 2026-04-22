class Stack:
    """Реализация стека на основе списка"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Добавить элемент в стек"""
        self.items.append(item)
    
    def pop(self):
        """Удалить и вернуть верхний элемент стека"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Посмотреть верхний элемент без удаления"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Проверить, пуст ли стек"""
        return len(self.items) == 0
    
    def size(self):
        """Получить размер стека"""
        return len(self.items)


class ExpressionCalculator:
    """Калькулятор для вычисления математических выражений"""
    
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.right_associative = {'^'}
    
    def infix_to_postfix(self, expression):
        """Преобразовать инфиксную нотацию в постфиксную (алгоритм Шунтинг-ярд)"""
        output = []
        operator_stack = Stack()
        
        # Удалить пробелы
        expression = expression.replace(" ", "")
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            # Если число (может быть многозначное)
            if char.isdigit():
                num = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'): 
                    num += expression[i]
                    i += 1
                output.append(float(num))
                continue
            
            # Если оператор
            elif char in self.precedence:
                while (not operator_stack.is_empty() and
                       operator_stack.peek() in self.precedence and
                       (self.precedence[operator_stack.peek()] > self.precedence[char] or
                        (self.precedence[operator_stack.peek()] == self.precedence[char] and 
                         char not in self.right_associative))):
                    output.append(operator_stack.pop())
                
                operator_stack.push(char)
            
            # Если открывающая скобка
            elif char == '(': 
                operator_stack.push(char)
            
            # Если закрывающая скобка
            elif char == ')':
                while not operator_stack.is_empty() and operator_stack.peek() != '(': 
                    output.append(operator_stack.pop())
                
                if not operator_stack.is_empty():
                    operator_stack.pop()  # Удалить '('
            
            i += 1
        
        # Добавить оставшиеся операторы
        while not operator_stack.is_empty():
            output.append(operator_stack.pop())
        
        return output
    
    def evaluate_postfix(self, postfix):
        """Вычислить постфиксное выражение используя стек"""
        stack = Stack()
        
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.push(token)
            else:
                # Оператор
                if stack.size() < 2:
                    raise ValueError("Некорректное выражение")
                
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("Деление на ноль")
                    result = a / b
                elif token == '^':
                    result = a ** b
                
                stack.push(result)
        
        if stack.size() != 1:
            raise ValueError("Некорректное выражение")
        
        return stack.pop()
    
    def calculate(self, expression):
        """Основной метод: вычислить выражение"""
        try:
            postfix = self.infix_to_postfix(expression)
            result = self.evaluate_postfix(postfix)
            return result
        except Exception as e:
            return f"Ошибка: {str(e)}"


def main():
    """Главная функция программы"""
    calculator = ExpressionCalculator()
    
    print("=" * 50)
    print("Калькулятор выражений со стеком")
    print("=" * 50)
    print("Поддерживаемые операции: +, -, *, /, ^")
    print("Пример: 3+5*2, (10-5)*2, 2^3")
    print("Введите 'выход' для завершения\n")
    
    while True:
        expression = input("Введите выражение: ").strip()
        
        if expression.lower() == 'выход':
            print("До встречи!")
            break
        
        if not expression:
            print("Пожалуйста, введите выражение\n")
            continue
        
        result = calculator.calculate(expression)
        print(f"Результат: {result}\n")


if __name__ == "__main__":
    main()