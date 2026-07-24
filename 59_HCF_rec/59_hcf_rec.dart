import 'dart:io';

void main() {
  try {
    while (true) {
      // program to reverse a number using a arithmatic operators

      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a positive integer value : ");
      int num2 = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      void euclideanHcf(a){
        if (a <= 0)return;
        int temp = num1;
        num1 = a;
        euclideanHcf(num2 % temp);
      }

      if (num1 > maxLimit || num2 > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num1 == 0 || num2 == 0) {
        print("Enter a valid integer value : ");
      } else {
        euclideanHcf(num2);
        print("HCF - $num1");
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
