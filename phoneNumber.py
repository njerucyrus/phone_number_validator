class CleanPhoneNumber():
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def validate_phone_number(self):
        phone_number = self.phone_number
        phone = list(phone_number)
        prefix = phone[0]
        if prefix == '0' and len(phone_number)== 10 :
            phone[0] = '+254'
            return "".join(phone)

        elif prefix == '+' and len(phone_number) == 13 :
            return str(phone_number)

        elif len(phone_number)<10:
            print 'invalid phone_number length'
        
        
