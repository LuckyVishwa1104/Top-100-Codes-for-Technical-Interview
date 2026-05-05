import 'dart:io';

void main() {
  stdout.write('Enter a valid numeric value : ');
  int a = int.parse(stdin.readLineSync()!);

  if (a % 2 == 0 && a != 0) {
    print('$a is even number.');
  } 
  else if (a % 2 == 1) {
    print('$a is a odd number');
  } 
  else {
    print('Input is Zero');
  }
}


