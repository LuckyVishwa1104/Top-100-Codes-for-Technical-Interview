import 'dart:io';

void main(){

  stdout.write('Enter a Integer value : ');
  int a = int.parse(stdin.readLineSync()!);

  if(a > 0){
    print('Number is positive');
  }
  else if (a < 0){
    print('Number is negative');
  }
  else{
    print('Enter number is Zero');
  }

}
