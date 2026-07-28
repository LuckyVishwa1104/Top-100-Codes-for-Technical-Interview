import 'dart:io';

void main() {
  try {
    while (true) {
      // program to reverse a number using a arithmatic operators

      stdout.write("Enter a positive integer value : ");
      String str = stdin.readLineSync()!;

      int strLength(String str){
        if (str.isEmpty) return 0;
        return 1 + strLength(str.substring(1));
      }

      int stringLength = strLength(str);

      print(stringLength);

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program finished!");
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
