import 'dart:io';

String convert_two_digit(int num) {

  Map<int, String> ones = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
  };

  Map<int, String> teens = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
  };

  Map<int, String> tens = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
  };

  if (num < 10) {
    return ones[num]!;
  } else if (num < 20) {
    return teens[num]!;
  } else {
    int ten = num ~/ 10;
    int one = num % 10;

    if (0 == one) {
      return tens[ten]!;
    }

    return tens[ten]! + " " + ones[one]!;
  }
}

String convert_three_digit(int num){
  if (num < 100){
    return convert_two_digit(num);
  }

  int hundred = num ~/ 100;
  int remainder = num % 100;

  String result = "";

  result += convert_two_digit(hundred) + " Hundred ";

  if (0 != remainder){
    result += convert_two_digit(remainder);
  }

  return result;
}

String convert_four_digit(int num){
  if (num < 1000){
    return convert_three_digit(num);
  }

  int thausand = num ~/ 1000;
  int remainder = num % 1000;

  String result = "";

  result += convert_three_digit(thausand) + " Thausand ";

  if (remainder != 0){
    result += convert_three_digit(remainder);
  }

  return result;
}

String convert_six_digit(int num){
  if (0 == num){
    return "Zero";
  }

  if(num < 1000000){
    return convert_four_digit(num);
  }

  int million = num ~/ 1000000;
  int remainder = num % 1000000;

  String result = "";

  result += convert_four_digit(million) + " Million ";
  
  if(0 != remainder){
    result += convert_four_digit(remainder);
  }

  return result;
}

String digitToWords(int num) {
  return convert_six_digit(num);
}

void main() {
  try {
    while (true) {
      stdout.write("Enter number in integer form : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0){
        print("Enter positive integer number");
      }

      else{
        String result = digitToWords(num);
        print("$num  ===>  $result");
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