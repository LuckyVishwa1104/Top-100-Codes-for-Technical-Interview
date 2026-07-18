import 'dart:io';
import 'dart:math';

List<double> roots(int a, int b, int c){
  double D = sqrt(pow(b, 2) - 4 * a * c);

  if(0 == D){
    double x1 = b / 2*a;
    return [x1];
  }
  else{
    double x1 = (-b + D) / (2 * a);
    double x2 = (-b - D) / (2 * a);

    return [x1, x2];
  }
}

void main() {
  try {
    while (true) {
      stdout.write("Enter the coefficient of x^2 :");
      int a = int.parse(stdin.readLineSync()!);

      stdout.write("Enter the coefficient of x :");
      int b = int.parse(stdin.readLineSync()!);

      stdout.write("Enter the constant term :");
      int c = int.parse(stdin.readLineSync()!);

      List<double> result = roots(a, b, c);
      print("$result");

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
