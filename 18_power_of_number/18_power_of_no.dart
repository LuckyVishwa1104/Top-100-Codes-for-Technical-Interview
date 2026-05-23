import 'dart:io';

double powerOfNumber(int num, int pow) {
  double result = 1;

  int limit = pow.abs();

  for (int i = 0; i < limit; i++) {
    result = result * num;
  }

  if (pow < 0){
    return (1 / result);
  }

  return result;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a number : ");
      int num = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a number : ");
      int pow = int.parse(stdin.readLineSync()!);

      if (num == 0 && pow == 0) {
        print("Enter positive integer value");
      }
      else {
        double result = powerOfNumber(num, pow);
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
