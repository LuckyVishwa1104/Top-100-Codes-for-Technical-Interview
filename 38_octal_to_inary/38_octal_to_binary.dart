import 'dart:io';

Map<int, String> octalToBinaryMap = {
  0: "000",
  1: "001",
  2: "010",
  3: "011",
  4: "100",
  5: "101",
  6: "110",
  7: "111",
};

String octalToBinary(int octal) {
  if (octal == 0) {
    return "0";
  }

  String binaryNum = "";
  while (octal > 0) {
    int remainder = octal % 10;
    binaryNum = octalToBinaryMap[remainder]! + binaryNum;
    octal = octal ~/ 10;
  }
  return binaryNum.replaceFirst(RegExp(r'^0+'), '');
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0) {
        print("Enter the value in decimal larger than zero");
      } else {
        String result = octalToBinary(num);
        print("Binary $num = $result Octal");
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
