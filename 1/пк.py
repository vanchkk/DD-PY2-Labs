class Computer(ABC):
    def __init__(self, brand: str, ram: int, storage: int):
        """Создание и подготовка к работе объекта "Компьютер".

        :param brand: Бренд компьютера.
        :param ram: Объем оперативной памяти в ГБ.
        :param storage: Объем хранилища в ГБ.

        Примеры:
        >>> computer = Computer("Apple", 16, 512)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str) or not brand:
            raise ValueError("Бренд должен быть непустой строкой.")
        if not isinstance(ram, int) or ram <= 0:
            raise ValueError("Объем RAM должен быть положительным целым числом.")
        if not isinstance(storage, int) or storage <= 0:
            raise ValueError("Объем хранилища должен быть положительным целым числом.")

        self.brand = brand
        self.ram = ram
        self.storage = storage

    @abstractmethod
    def boot(self) -> str:
        """Запуск компьютера.

        :return: Строка с сообщением о запуске компьютера.

        Примеры:
        >>> computer = Computer("Apple", 16, 512)
        >>> computer.boot()
        """
        ...

    @abstractmethod
    def shutdown(self) -> str:
        """Выключение компьютера.

        :return: Строка с сообщением о выключении компьютера.

        Примеры:
        >>> computer = Computer("Apple", 16, 512)
        >>> computer.shutdown()
        """
        ...