import 'dart:io';

int sumOfNNumbers(int num) {
  return (num * (num + 1) ~/ 2);
}

void main() {
  try {
    stdout.write('Enter a valid Integer value : ');
    int num = int.parse(stdin.readLineSync()!);

    if (num < 0) {
      print('Enter a valid positive Integer value.');
    } else {
      int result = sumOfNNumbers(num);
      print("Sum of First $num numbers : $result");
    }
  } on FormatException catch (e) {
    print('Invalid Input : $e');
  } on UnsupportedError catch (e) {
    print("Divide By Zero Error : $e");
  } catch (e) {
    print('Unexcepted error occured : $e');
  }
}
