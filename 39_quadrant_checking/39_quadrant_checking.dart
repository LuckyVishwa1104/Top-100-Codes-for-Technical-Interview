import 'dart:io';
// program to check the quadratn of point in 2D cartesian system
String checkQuadrant(int x, int y) {
  if (x == 0 && y == 0) {
    return "Origin";
  }

  if (x == 0) {
    return y > 0 ? "Posivite Y-axis" : "Negative Y-axis";
  }

  if (y == 0) {
    return x > 0 ? "Positive X-axis" : "Negative X-axis";
  }

  if (x > 0 && y > 0) {
    return "First Quadrant";
  }

  if (x > 0 && y < 0) {
    return "Fourth Quadrant";
  }

  if (x < 0 && y > 0) {
    return "Second Quadrant";
  }

  if (x < 0 && y < 0) {
    return "Third Quadrant";
  }

  return "does not lies on cartesian system";
}

// driver program
void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);
      int num2 = int.parse(stdin.readLineSync()!);

      String result = checkQuadrant(num1, num2);
      print("($num1, $num2) lies on $result");

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
