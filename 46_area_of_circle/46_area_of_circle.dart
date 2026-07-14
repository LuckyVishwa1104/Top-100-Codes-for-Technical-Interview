import 'dart:io';
import 'dart:math';

double circleArea(int radius){
  return (pi * pow(radius, 2));
}

void main() {
  try {
    while (true) {
      stdout.write("Enter number in integer form : ");
      int num = int.parse(stdin.readLineSync()!);

      double result = circleArea(num.abs());
      print("Area of Circle with radius $num : $result");


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
