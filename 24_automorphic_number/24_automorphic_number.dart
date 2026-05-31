import 'dart:io';

// Automorphic number - a number which is eqaul to end of its sqaure is a automorphic number

bool isAutomorphic(int num) {
  int numSquare = num * num;

  while (num > 0) {
    if (num % 10 != numSquare % 10) {
      return false;
    }
    num = num ~/ 10;
  }
  return true;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      if (num > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num <= 0) {
        print("Enter a valid integer value : ");
      } else {
        bool result = isAutomorphic(num);
        if (result) {
          print("$num is automorphic number");
        } else {
          print("$num is not automorphic number");
        }
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
