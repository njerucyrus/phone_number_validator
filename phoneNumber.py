
class CleanPhoneNumber():
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def validate_phone_number(self):
        phone_number = self.phone_number
        phone = list(phone_number)
        prefix = phone[0]
        length = len(phone_number)
    
        if prefix == '0' and length== 10:
            phone[0] = '+254'
            return "".join(phone)

        elif prefix == '+' and length == 13 :
            return str(phone_number)

        elif length < 10 :
            print 'invalid phone number length'

        else:
            print 'invalid phone number'

if __name__ == '__main__':
    """
        testing the code with some test data

    """
    phone_list = ['YOUR LIST OF NUMBERS']
    clean_phone_list = []

    for number in phone_list:
        clean_num = CleanPhoneNumber(number).validate_phone_number()
        clean_phone_list.append(clean_num)
    
    print ",".join(clean_phone_list)
     
        
    
            
    
        



            
            
        
        
