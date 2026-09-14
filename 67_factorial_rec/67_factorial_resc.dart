import 'dart:io';

int factorial(int num){
  if (num <=1 ) return 1;
  return (num * factorial(num - 1));
}

void main(){
  try {
    while (true) {
      // program to find last non zero digit of a factorial of a particular number
      stdout.write('Enter the number : ');
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 20) {
        int result = factorial(num);
        print(result);
      } else {
        print("Input is to large");
      }

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program finished!");
        break;
      }
    }
  } on FormatException catch (fe) {
    print("Invalid Input - $fe");
  } on UnsupportedError catch (ue) {
    print("Divide by zero exception - $ue");
  } on Exception catch (e) {
    print("Exception caught - $e");
  }
}
