import 'dart:io';

// euclidean algorithm - log(min(a,b))

int euclideanHcf(int num1, num2) {
  while (num2 > 0) {
    int temp = num1;
    num1 = num2;
    num2 = temp % num2;
  }
  return num1;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a positive integer value : ");
      int num2 = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      if (num1 > maxLimit || num2 > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num1 == 0 || num2 == 0) {
        print("Enter a valid integer value : ");
      } else {
        int result = euclideanHcf(num1.abs(), num2.abs());
        print("HCF - $result");
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
