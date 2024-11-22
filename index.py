from myLib.dataValidation import Validation

print(Validation.String('y', 'n',message="Enter between y or n\nYour Choise: " , error="\noh.. this is an Error. Try Again\n"))