import 'dart:io';

void main() {
  try {
    while (true) {
      stdout.write("Enter the number : ");
      int number = int.parse(stdin.readLineSync()!);

      bool notPrime = true;
      void isPrime(num) {
        if (num >= number) return; // terminating recursion
        if (number % num == 0) {
          notPrime = false;
        }
        isPrime(num + 1); // incrementing iteration for recurssion
      }

      isPrime(2); // initializig recurssion

      if (notPrime)
        print("$number is prime");
      else
        print("$number is not prime");

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if ("n" == choice) {
        print("Program terminated!");
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
