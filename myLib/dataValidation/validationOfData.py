#creating the Such Kind of the Validation Libary which can Handle User Validation

class Validation:


    @staticmethod
    def String(*agrs, message, error):
        
        byPassKey = True
        while(byPassKey):

            userInput = input(message)
            agrsTemp = [s.lower() for s in agrs]
            byPassKey = False
            tempInput = userInput.lower()
            try:
                if tempInput in agrsTemp:
                    return userInput
                else:
                    raise TypeError()
            except TypeError:
                print(error)
                byPassKey = True



    @staticmethod
    def Integer(*agrs, message, error):
            
            byPassKey = True
            while(byPassKey):
                byPassKey = False

                try:
                    userInput = int(input(message))
                    if userInput.is_integer :
                        if int(userInput) in agrs:
                            return userInput
                        else :
                            raise ValueError
                    else:
                        print (error)
                        raise ValueError

                except ValueError:
                    print(error)
                    byPassKey = True
