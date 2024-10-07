import functools
import datetime
import time


# Декоратор для логирования вызовов методов
def log_methods(time_format: str):
    def decorator(cls):
        for attr_name, attr_value in list(cls.__dict__.items()):
            if callable(attr_value) and not attr_name.startswith(
                    "__"):  # Проверяем, является ли атрибут методом и не является ли специальным методом
                original_method = attr_value

                @functools.wraps(attr_value)
                def wrapped_method(self, *args, **kwargs):
                    # Текущее время для логов
                    start_time = datetime.datetime.now()
                    formatted_time = start_time.strftime(time_format)

                    # Логируем запуск метода
                    print(
                        f"Запускается '{cls.__name__}.{original_method.__name__}'. Дата и время запуска: {formatted_time}.")

                    # Измеряем время выполнения
                    start_perf = time.perf_counter()
                    result = original_method(self, *args, **kwargs)
                    end_perf = time.perf_counter()

                    # Время выполнения метода
                    elapsed_time = end_perf - start_perf

                    # Логируем завершение метода
                    print(
                        f"Завершение '{cls.__name__}.{original_method.__name__}', время работы = {elapsed_time:.3f} s.")

                    return result

                # Заменяем метод обернутым методом
                setattr(cls, attr_name, wrapped_method)
        return cls

    return decorator


# Базовый класс
class A:
    def test_sum_1(self):
        print("Тут метод test_sum_1.")


# Наследуемый класс
@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self):
        # Логируем вызов метода родительского класса
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника.")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


# Пример использования
b = B()
b.test_sum_1()
b.test_sum_2()
