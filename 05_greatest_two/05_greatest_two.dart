import 'dart:io';

// program to find greates among two numbers

int greatestAmongTwo(int a, int b) {
  if (a > b) {
    return a;
  } else {
    return b;
  }
}

void main() {
  try {
    stdout.write("Enter a valid inteer value : ");
    int a = int.parse(stdin.readLineSync()!);
    stdout.write("Enter a valid integer value : ");
    int b = int.parse(stdin.readLineSync()!);

    if (a == b) {
      print("Number a equal");
    } else {
      int result = greatestAmongTwo(a, b);
      print("Greates number is $result");
    }
  } on FormatException catch (e) {
    print("Invalid Input : $e");
  } catch (e) {
    print("Exception caught : {e}");
  }
}
