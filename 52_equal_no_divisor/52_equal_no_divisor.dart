import 'dart:io';

int equalDivisor(int num, int divi){

  int count = 0;
  for (int i = 1; i < num + 1; i++){
    int divisorCount = 0;

    for (int j = 1; j < i+1; j++){
      if(i % j == 0){
        divisorCount += 1;
      }
    }
    if(divisorCount == divi) count += 1;
  }
  return count;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter number : ");
      int number = int.parse(stdin.readLineSync()!);

      stdout.write("Enter divisor : ");
      int divisor = int.parse(stdin.readLineSync()!);

      if (divisor <= 0 || number <= 0) {
        print("Enter positive integer number for digits");
      }
      else{
        int result = equalDivisor(number, divisor);
        print("$result numbers have $divisor divisors.");
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
