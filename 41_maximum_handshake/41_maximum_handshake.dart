import 'dart:io';

int maxHandShake(int num){
  return (num * (num - 1)) ~/ 2;
}

void main(){
  try {
    while (true) {
      stdout.write("Enter number of Person : ");
      int num1 = int.parse(stdin.readLineSync()!);

      if(num1 <= 0){
        print("Enter a positive integer values");
      }
      else{
        int result = maxHandShake(num1);
        print("$result hand shake are possible.");
      }

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program finished!");
        break;
      }
    }
  } on FormatException catch (e) {
    print("Invalid input : $e");
  } on UnsupportedError catch (e) {
    print("Divide by zero exception : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }
}
