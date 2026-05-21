import 'dart:io';

int factorialValue(int num) {
  int fac = 0;

  if (num == 0) {
    return 1;
  } else {
    for (int i = 1; i <= num; i++) {
      fac = fac * i;
    }
    return fac;
  }
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0) {
        print("Enter a value greater than or equal to ZERO");
      } else {
        int result = factorialValue(num);
        print(result);
      }

      stdout.write("Do you want to continue? (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program Finished");
        break;
      }
    }
  } on FormatException catch (e) {
    print("Invalid input : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }
}
