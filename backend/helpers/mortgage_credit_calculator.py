class CreditRatingCalculator:
    def __init__(self, credit_score, loan_amount, property_value, annual_income, debt_amount, loan_type, property_type):
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.property_value = property_value
        self.annual_income = annual_income
        self.debt_amount = debt_amount
        self.loan_type = loan_type
        self.property_type = property_type
        self.risk_score = 0
    
    def calculate_ltv_ratio(self):
        ltv = (self.loan_amount / self.property_value) * 100
        if ltv > 90:
            self.risk_score += 2
        elif ltv > 80:
            self.risk_score += 1
    
    def calculate_dti_ratio(self):
        dti = (self.debt_amount / self.annual_income) * 100
        if dti > 50:
            self.risk_score += 2
        elif dti > 40:
            self.risk_score += 1
    
    def evaluate_credit_score(self):
        if self.credit_score >= 700:
            self.risk_score -= 1
        elif self.credit_score < 650:
            self.risk_score += 1
    
    def evaluate_loan_type(self):
        if self.loan_type == 'fixed':
            self.risk_score -= 1
        elif self.loan_type == 'adjustable':
            self.risk_score += 1
    
    def evaluate_property_type(self):
        if self.property_type == 'condo':
            self.risk_score += 1
    
    def calculate_credit_rating(self, avg_credit_score=None):
        self.calculate_ltv_ratio()
        self.calculate_dti_ratio()
        self.evaluate_credit_score()
        self.evaluate_loan_type()
        self.evaluate_property_type()
        
        if avg_credit_score is not None:
            if avg_credit_score >= 700:
                self.risk_score -= 1
            elif avg_credit_score < 650:
                self.risk_score += 1
        
        if self.risk_score <= 2:
            return "AAA"
        elif 3 <= self.risk_score <= 5:
            return "BBB"
        else:
            return "C"

