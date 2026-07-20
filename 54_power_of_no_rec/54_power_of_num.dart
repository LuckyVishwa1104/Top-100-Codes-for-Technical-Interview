import 'dart:io';

void main() {
  try {
    while (true) {
      stdout.write("Enter number :");
      int number = int.parse(stdin.readLineSync()!);

      stdout.write("Enter power :");
      int power = int.parse(stdin.readLineSync()!);

      int result = 1;

      void expo(int num){
        if (num > power) return;
        result *= number;
        expo(num +1);
      }
      expo(1);

      print("$number ^ $power = $result");

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
