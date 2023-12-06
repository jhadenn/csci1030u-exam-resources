class Investment: 
    def __init__(self, value, name) :
        self.value = value
        self.name = name

    def __str__(self) :
        return f'Name: {self.name} (value: ${self.value:.2f})'

class SavingsAccount(Investment) :
    def __init__(self, value, name, annual_interest_rate):
        super().__init__(value, name)
        self.annual_interest_rate = annual_interest_rate
    
    def calculate_growth(self) :
        monthly_interest = self.annual_interest_rate / 12
        self.value += self.value * monthly_interest

class SP500(Investment):
    def __init__(self, value, name):
        super().__init__(value, name)
        self.current_growth_rate = 0.0

    def set_current_growth_rate(self, rate) :
        self.current_growth_rate = rate

    def calculate_growth(self): 
        self.value += self.value * self.current_growth_rate

investment1 = SavingsAccount(1000.00, 'Pro Savings Plus', 0.055)
investment1.calculate_growth() # month 1
investment1.calculate_growth() # month 2
print(f'{str(investment1)}')
# output: Name: Pro Savings Plus (value: $1113.03)

investment2 = SP500(1000.00, 'Standard and Poor 500')
investment2.set_current_growth_rate(0.063)
investment2.calculate_growth() # month 1
investment2.set_current_growth_rate(0.058)
investment2.calculate_growth() # month 2
print(f'{str(investment2)}')
# output: Name: Standard and Poor 500 (value: $1124.65)