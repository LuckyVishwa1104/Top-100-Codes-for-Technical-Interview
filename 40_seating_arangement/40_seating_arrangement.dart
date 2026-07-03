import 'dart:io';

int seatingCombinatino(int per, int seat){
  int combination = 1;
  while (per >= seat){
    combination = combination * per;
    per -= 1;
  }
  return combination;
}

void main(){
  try {
    while (true) {
      stdout.write("Enter number of Person : ");
      int num1 = int.parse(stdin.readLineSync()!);
      stdout.write("Enter number of Seats : ");
      int num2 = int.parse(stdin.readLineSync()!);

      if(num1 <= 0 && num2 <= 0){
        print("Enter a positive integer values");
      }
      else if (num1 < num2){
        print("Number of should be greater than number of seats");
      }
      else{
        int result = seatingCombinatino(num1, num2);
        print("$num1 persons can seat in $result combination in $num2 seats.");
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
