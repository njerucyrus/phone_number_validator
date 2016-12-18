
class CleanPhoneNumber():
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def validate_phone_number(self):
        phone_number = self.phone_number
        phone = list(phone_number)
        prefix = phone[0]
        length = len(phone_number)
    
        if prefix == '0' and length== 10 and phone[1]== '7':
            phone[0] = '+254'
            return "".join(phone)

        elif prefix == '+' and length == 13  and phone[4] == '7':
            return str(phone_number)

        elif length < 10 :
            print 'invalid phone number length'

        else:
            print 'invalid phone number'

if __name__ == '__main__':
    phone_number = raw_input('Enter phone number:\n')
    obj = CleanPhoneNumber(phone_number).validate_phone_number()
    print obj
        
    
            
    
        



            
            
        
        
