class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        """Создание и подготовка к работе объекта "Транспортное средство".

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Camry", 2020)  # инициализация экземпляра класса
        """
        if not isinstance(make, str) or not make:
            raise ValueError("Производитель должен быть непустой строкой.")
        if not isinstance(model, str) or not model:
            raise ValueError("Модель должна быть непустой строкой.")
        if not isinstance(year, int) or year <= 1885:  # Год 1886 - первый автомобиль
            raise ValueError("Год выпуска должен быть целым числом больше 1885.")

        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> str:
        """Запуск двигателя.

        :return: Строка с сообщением о запуске двигателя.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Camry", 2020)
        >>> vehicle.start_engine()
        """
        ...

    @abstractmethod
    def stop_engine(self) -> str:
        """Остановка двигателя.

        :return: Строка с сообщением о остановке двигателя.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Camry", 2020)
        >>> vehicle.stop_engine()
        """
        ...