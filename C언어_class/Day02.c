#include <stdio.h>

//------ 제어 문자 --------
/*
\" : (큰 따옴표) 출력
\' : (작은 따옴표) 출력



*/

//------- 서식 지정자 ------------
/*
%c : Character, 하나의 문자
%s : String, 문자열
%d : Decimal, 10진수 정수
%f : Float, 실수
%o : Octal, 8진수 정수
%x : Hexadecimal : 16진수 정수
%p : pointer, 주소
%u : unsigened, 부호가 없는 10진수 정수
%% : %를 출력해주는 탈출 문자

서식 지정자에서 소수점 자리수를 지정해주는 방법 : % 와 f 사이에 (.출력할 소수점 자리수)를 작성해준다.
					ex) %.2f -> 소수점 2번째 자리까지 출력
서식 지정자에서 오른쪽 정렬을 진행하는 방법 : %와 d 사이에 확보할 공간의 개수를 작성한다.
					ex) %3d -> 3개의 공간을 확보하고 해당 공간에서 오른쪽 정렬 진행
서식 지정자에서 왼쪽 정렬을 진행하는 방법 : %와 d 사이에 확보할 공간의 개수를 작성하고 그 앞에 -를 붙여준다.
					ex) %-3d -> 3개의 공간을 확보하고 해당 공간에서 왼쪽 정렬 진행
서식 지정자에서 오른쪽 정렬을 진행하고 남은 공간에 0을 채우는 방법 : %와 d 사이에 확보할 공간의 개수를 작성하고 그 앞에 0을 붙여준다.
					ex)  %03d -> 3개의 공간을 확보하고 해당 공간에서 오른쪽 정렬 진행 후 남은 공간에 0을 채워준다.

*/


// ----- C언어에서 데이터를 표기하는 방법 -----
/*
문자 : ''(작은 따옴표)로 감싸준다. ex) 'A'  문자는 반드시 단 한 개만 존재해야 한다.
문자열 : ""(큰 따옴표)로 감싸준다. ex) "AB" 
정수 : 숫자 그대로 작성한다.
실수 : 숫자 뒤에 소수점까지 작성해준다.
*/


int main()
{
	/*printf("%c\n", 'G');
	printf("%s\n", "Abcd");
	printf("%d\n", 347);
	printf("%.3f\n", 17.257);*/

	//printf("%d %d\n", 'A', 'F');  //아스키 코드로 치환해줌

	//printf("%-10d %10d\n", 10, 20);  // 왼쪽 정렬, 오른쪽 정렬 예시

	//printf("%010d %d\n", 10, 20);  // 남은 공간 대체 문자 출력 예시

	/*printf("%%c\n");

	printf("\"Hello\"\n");*/
	
	printf("%s: %s\n", "이름", "홍길동");
	printf("%s: %d\n", "나이", 30);
	printf("%s: %s\n", "주소", "서울특별시 종로구 묘동 단성사");
	printf("%s: %s\t%s: %s\n", "키", "183.2cm", "몸무게", "70.53kg");

	printf("%%c를 이용한 출력: \'%c\'\n", 'C');        // '\'c\'' -> 총 3개의 문자열로 취급된다. 탈출문자 + 문자 는 한 문자로 취급
	printf("%%s를 이용한 출력: \"%s\"\n", "Hello");
	printf("%%d를 이용한 출력: %d\n", 4315);
	printf("%%f를 이용한 출력: %.3f\n", 73.235);

	return 0;
}