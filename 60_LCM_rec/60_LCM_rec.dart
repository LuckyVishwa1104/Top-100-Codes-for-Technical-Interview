import 'dart:io';

void main() {
  try {
    while (true) {
      // program to find LCM using formula (num1 * num2) // hcf - hcf by eucludian method

      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a positive integer value : ");
      int num2 = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      int euclideanHcf(int a, int b){
        if (b == 0) return a;
        return euclideanHcf(b, a % b);
      }

      if (num1 > maxLimit || num2 > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num1 == 0 || num2 == 0) {
        print("Enter a valid integer value : ");
      } else {
        int hcf = euclideanHcf(num1, num2);
        int lcm = (num1 * num2) ~/ hcf;
        print("LCM - $lcm");
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
