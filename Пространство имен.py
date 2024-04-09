def test_function():  # Создаем новую функцию
    def inner_function():
        def other_function():  # Создаем другую функцию внутри функции inner_function
            print('Я в области видимости функции test_function')

        other_function()

    inner_function()


test_function()
# вызываем inner_function вне функции test_function:
# inner_function() # ошибка name 'inner_function' is not defined.
