from abc import ABC, abstractmethod
import random


class State(ABC):
    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def withdraw_money(self):
        pass

    @abstractmethod
    def load_money(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def insert_card(self):
        pass


class AuthenticationState(State):
    def __init__(self, atm):
        self.atm = atm

    def enter_pin(self):
        if atm.enter():
            atm.set_state(atm.OperationExecutionState)

    def withdraw_money(self):
        print("PIN-код не введен")

    def load_money(self):
        print("PIN-код не введен")

    def stop(self):
        atm.set_state(atm.WaitingState)

    def insert_card(self):
        print("Карта уже вставлена")


class WaitingState(State):
    def __init__(self, atm):
        self.atm = atm

    def enter_pin(self):
        print("Карта не вставлена")

    def load_money(self):
        atm.load()
        atm.set_state(atm.WaitingState)
        if atm.total_money == 0:
            print("В банкомате нет денег")
            atm.set_state(atm.BlockedState)

    def withdraw_money(self):
        print("Карта не вставлена")

    def stop(self):
        print("Вставьте карту")

    def insert_card(self):
        print("Начата работа")
        atm.set_state(atm.AuthenticationState)


class OperationExecutionState(State):
    def __init__(self, atm):
        self.atm = atm

    def enter_pin(self):
        print("Pin-код уже введен")

    def withdraw_money(self):
        atm.withdraw()
        if atm.total_money == 0:
            print("В банкомате нет денег")
            atm.set_state(atm.BlockedState)

    def load_money(self):
        print("Перейдите в режим ожидания")

    def stop(self):
        atm.set_state(atm.AuthenticationState)

    def insert_card(self):
        print("Карта уже вставлена")


class BlockedState(State):
    def __init__(self, atm):
        self.atm = atm

    def enter_pin(self):
        print("В банкомате нет денег")

    def withdraw_money(self):
        print("В банкомате нет денег")

    def load_money(self):
        atm.load()
        atm.set_state(atm.WaitingState)
        if atm.total_money == 0:
            print("В банкомате нет денег")
            atm.set_state(atm.BlockedState)

    def stop(self):
        print("В банкомате нет денег")

    def insert_card(self):
        print("В банкомате нет денег")


class ATM:
    def __init__(self, id, total_money, failure_probability):
        self.id = id
        self.total_money = total_money
        self.failure_probability = failure_probability
        self.WaitingState = WaitingState(self)
        self.AuthenticationState = AuthenticationState(self)
        self.BlockedState = BlockedState(self)
        self.OperationExecutionState = OperationExecutionState(self)
        self.state = WaitingState(self)

    def set_state(self, state):
        self.state = state

    def enter_pin(self):
        self.state.enter_pin()

    def insert_card(self):
        self.state.insert_card()

    def withdraw_money(self):
        self.state.withdraw_money()

    def load_money(self):
        self.state.load_money()

    def stop(self):
        self.state.stop()

    def withdraw(self):
        print("Введите сумму")
        n = int(input())
        if n > 0:
            if atm.total_money >= n:
                atm.total_money -= n
                print("Деньги сняты")
            else:
                print("Недостаточно средств в банкомате")
        else:
            print("Некорректная сумма")

    def load(self):

        print("Введите сумму")
        n = int(input())
        if n > 0:
            atm.total_money += n
            print("Деньги в банкомате")
        else:
            print("Некорректная сумма")

    def enter(self):
        print("Введите Pin-код")
        pin = input()
        if self.failure_probability > random.random():
            print("Ошибка связи с банком")
        elif pin == "1234":  # Пример проверки PIN-кода
            print("PIN-код корректный, можно снимать деньги")
            return True
        else:
            print("Неверный PIN-код. Попробуйте еще раз.")
        return False


if __name__ == "__main__":
    atm = ATM("ATM001", 10000, 0.5)
    print(
        """1: Вставить карту
2: Ввести Pin-код
3: Снять деньги
4: Загрузить деньги в банкомат
5: Выйти""")
    while True:
        n = int(input())
        if n == 1:
            atm.insert_card()
        elif n == 2:
            atm.enter_pin()
        elif n == 3:
            atm.withdraw_money()
        elif n == 4:
            atm.load_money()
        elif n == 5:
            atm.stop()
        else:
            print("Некорректная команда")
