import 'dart:io';

// method to reverse the ouptput string
String reverseString(String num) {
  String revString = "";
  for (int i = num.length - 1; i >= 0; i--) {
    revString = revString + num[i];
  }
  return revString;
}

// method to conver decimal to equivalent hexal value
String decimalToHex(int decimal) {
  const Map<int, String> hexMap = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
  };

  if (decimal == 0) {
    return "0";
  }
  String hexNum = "";
  while (decimal > 0) {
    int remainder = decimal % 16;
    decimal = decimal ~/ 16;
    hexNum = hexNum + hexMap[remainder]!;
  }
  return reverseString(hexNum);
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0) {
        print("Enter the value in decimal larger than zero");
      } else {
        String result = decimalToHex(num);
        print("Decimal $num = $result Hex");
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
