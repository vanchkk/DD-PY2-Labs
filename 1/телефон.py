class Smartphone(ABC):
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """Создание и подготовка к работе объекта "Смартфон".

        :param brand: Бренд смартфона.
        :param model: Модель смартфона.
        :param battery_capacity: Емкость батареи в мАч.

        Примеры:
        >>> smartphone = Smartphone("Samsung", "Galaxy S21", 4000)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str) or not brand:
            raise ValueError("Бренд должен быть непустой строкой.")
        if not isinstance(model, str) or not model:
            raise ValueError("Модель должна быть непустой строкой.")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Емкость батареи должна быть положительным целым числом.")

        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    @abstractmethod
    def make_call(self, number: str) -> str:
        """Совершение звонка.

        :param number: Номер для звонка.
        :return: Строка с сообщением о звонке.

        Примеры:
        >>> smartphone = Smartphone("Samsung", "Galaxy S21", 4000)
        >>> smartphone.make_call("123456789")
        """
        ...

    @abstractmethod
    def send_message(self, number: str, message: str) -> str:
        """Отправка сообщения.

        :param number: Номер получателя.
        :param message: Текст сообщения.
        :return: Строка с подтверждением доставки сообщения.

        Примеры:
        >>> smartphone = Smartphone("Samsung", "Galaxy S21", 4000)
        >>> smartphone.send_message("123456789", "Привет!")
        """
        ...