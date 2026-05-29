import 'dart:io';

// strong number - a number whose sum of factorial each digit is equal to number itself is call strong number

int factorial(int num){
  int fact = 1;
  for (int i = 1; i <= num; i++){
    fact = fact * i;
  }
  return fact;
}

bool isStrongNumber(int num){
  int strongValue = 0;
  int temp = num;
  while (num > 0){
    strongValue = strongValue + factorial(num % 10);
    num = num ~/ 10;
  }

  if (temp == strongValue){
    return true;
  }
  return false;
}

void main(){
  try{
    while(true){
      stdout.write("Enter integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 0){
        print("Enter a positive integer value");
      }
      else{
        bool result = isStrongNumber(num);
        if(result){
          print("$num is a strong number.");
        }
        else{
          print("$num is not a strong number");
        }
      }

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!;

      if(choice.toLowerCase() == "n"){
        print("Program Finished!");
        break;
      }
    }
  }

  on FormatException catch(e){
    print("Invalid input : $e");
  }

  on UnsupportedError catch(e){
    print("Divide by zero exception : $e");
  }

  on Exception catch(e){
    print("Exceptino caught : $e");
  }

}