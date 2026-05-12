import 'dart:io';

// Program to check whether a number is a prime number or not
// Prime number - a number which is divisible by 1 and itself only us prime number
// prime number have exactly two factors

bool isPrime(int num) {
  for (int i = 2; i < (num); i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

void main() {
  while (true) {
    try {
      stdout.write("Enter integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 1) {
        print("Enter a interger value greater than 1");
      } else {
        if (isPrime(num)) {
          print("$num is a Prime number");
        } else {
          print("$num is not a Prime number");
        }
      }
    } on FormatException catch (e) {
      print("Invalid input : $e");
    } on Exception catch (e) {
      print("Exception caught : $e");
    }
    stdout.write("Do you want to continue? (y/n) : ");
    String choice = stdin.readLineSync()!.toLowerCase();
    if (choice == 'n') {
      print("Program Finished");
      break;
    }
  }
}
