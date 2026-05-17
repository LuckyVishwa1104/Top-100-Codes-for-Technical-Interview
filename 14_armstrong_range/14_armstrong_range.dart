import 'dart:io';

// Program to find Armstrong number in Particular range

int isArmStrong(int num){
  int num_len = 0;
  while (num~/10 > 0){
    num_len += 1;
  }

  double pow = (1 / num_len);
  double sumOfDigit = 0;
  while (num > 0){
    sumOfDigit = sumOfDigit + ((num % 10) * pow);
    num = num ~/ 10;
  }
  return sumOfDigit.toInt();
}

void main(){
  try{
    while (true){

      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num > 0){
        print("Enter a value positve and greate than or equal to zero");
      }
      else{
        for(int i = 1; i <= num; i ++){
          int result = isArmStrong(num);
          if(i == result){
            print(i);
          }
        }
      }

      stdout.write("Do you want to continue? (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program Finished");
        break;
      }
    }
  }

  on FormatException catch(e){
    print("Invalid input : $e");
  }

  on Exception catch(e){
    print("Exception caught : $e");
  }
}

