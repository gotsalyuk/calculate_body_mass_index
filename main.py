class ParamsMixin:
    """ Получение входных параметров
    """
    def __init__(self):
        self.__error_text = "Введеный тип данных не верен, должно быть целое число"
        self.height = self._input_height()
        self.weight = self._input_weight()

    
    def _input_height(self) -> int:
        """ ввод параметра - рост

        Returns:
            int: рост
        """
        while True:
            _ = input("Напишите рост в сантиметрах:")

            if _.isnumeric():
                return int(_)
            else:
                print(self.__error_text)
    

    def _input_weight(self) -> int:
        """ ввод параметра - вес

        Returns:
            int: вес
        """
        while True:
            _ = input("Напишите вес в килограммах:")

            if _.isnumeric():
                return int(_)
            else:
                print(self.__error_text)


class Program(ParamsMixin):
    def __init__(self):
        ParamsMixin.__init__(self)
        
        self.table_recomendations = {
            "underweight": self.__underweight,
            "overweight": self.__overweight,
            "obesity": self.__obesity,
       }


    def __underweight(self, height: int, weight: int) -> str:
        """ расчет рекомендаций при не достаточной массе

        Args:
            height (int): рост
            weight (int): вес

        Returns:
            str: рекомендации
        """
        normal_weight = 0.00185 * (height**2)
        recomend = round(normal_weight - weight)
        return f"у вас не достаток веса, не обходимо набрать {recomend} кг"


    def __overweight(self, height: int, weight: int) -> str:
        """ расчет рекомендаций при избыточной массе

        Args:
            height (int): рост
            weight (int): вес

        Returns:
            str: рекомендации
        """
        normal_weight = 0.0025 * (height**2)
        recomend = round(weight - normal_weight)
        return f"у вас избыточная масса тела, не обходимо сбросить {recomend} кг"


    def __obesity(self, height: int, weight: int) -> str:
        """ расчет рекомендаций при ожирении

        Args:
            height (int): рост
            weight (int): вес

        Returns:
            str: рекомендации
        """
        normal_weight = 0.0025 * (height ** 2)
        recomend = round(weight - normal_weight)
        return f"у вас ожирение, не обходимо сбросить {recomend} кг"
        

    def __calculate_body_mass_index(self) -> float:
        """ расчет индекса массы тела

        Returns:
            float: индекс массы тела
        """
        return round(self.weight / (self.height ** 2), 5) * 10000


    def recomendations(self) -> str:
        """ точка входа

        Returns:
            str: результат выполнения
        """
        bmi = self.__calculate_body_mass_index()


        if bmi < 18.5:
            text = "underweight"
        elif 18.5 <= bmi < 25:
            return "У вас нормальный вес тела"
        elif 25 <= bmi < 30:
            text = "overweight"
        else:
            text = "obesity"

        return self.table_recomendations.get(text)(weight=self.weight, height=self.height)
        
        

if __name__ == "__main__":
    program = Program()
    print(program.recomendations())