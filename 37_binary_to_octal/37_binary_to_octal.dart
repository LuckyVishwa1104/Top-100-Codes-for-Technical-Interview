import 'dart:io';

Map<String, String> binaryToOctalMap = {
  "0": "0",
  "1": "1",
  "00": "0",
  "01": "1",
  "10": "2",
  "11": "3",
  "000": "0",
  "001": "1",
  "010": "2",
  "011": "3",
  "100": "4",
  "101": "5",
  "110": "6",
  "111": "7",
};

String binaryToOctal(int binaryNum) {
  if (binaryNum == 0) {
    return "0";
  }
  String octalNum = "";
  while (binaryNum > 0) {
    int remainder = binaryNum % 1000;
    binaryNum = binaryNum ~/ 1000;
    octalNum = octalNum + binaryToOctalMap[remainder.toString()]!;
  }
  return octalNum;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0) {
        print("Enter the value in decimal larger than zero");
      } else {
        String result = binaryToOctal(num);
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
