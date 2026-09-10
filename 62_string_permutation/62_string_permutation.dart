import 'dart:io';

List<String> subStrings(String str) {
  List<String> allSubString = [];
  for (int i = 0; i < str.length; i++) {
    for (int j = i + 1; j <= str.length; j++) {
      allSubString.add(str.substring(i, j));
    }
  }
  return allSubString;
}

void main() {
  try {
    while (true) {
      // program to find all possible sub-string combination
      stdout.write("Enter string : ");
      String str = stdin.readLineSync()!;

      if (str.isEmpty) {
        print("Enter some string values");
      } else {
        List<String> result = subStrings(str);
        print(result);
      }

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
