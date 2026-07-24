import 'dart:io';

void main() {
  try {
    while (true) {
      // program to reverse a number using a arithmatic operators
      stdout.write("Enter the number : ");
      int number = int.parse(stdin.readLineSync()!);
      int revNumber = 0;
      void reverseNumber(int num){
        if (num <= 0) return; // recursion termination

        int lastDigit = num % 10;
        revNumber = (revNumber * 10) + lastDigit;
        reverseNumber(num ~/ 10); // recursion iteration
      }
      reverseNumber(number); // recursion initialization

      print("$number ===>  $revNumber");

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
