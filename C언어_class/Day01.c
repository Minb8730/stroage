#include <stdio.h> // 전처리기: 프로그램이 실행될 때 가장 먼저 실행되는 부분
					// stdio.h 헤더파일을 포함시켜주는 코드
					// stdio.h : 기본 입출력을 가능하게 만들어주는 헤더파일
					// 기본 원형, 필수적으로 작성되어야 한다.

//--- 주석 ---
// 코드에 대한 코멘트를 작성할 때 사용
// 기본적으로 //(슬래시 두개) 를 사용해서 주석을 작성
// 프로그램을 실행하는데 영향을 끼치지 않는 부분
// 여러줄을 한번에 주석처리 하고 싶을때는 /* 로 주석을 열고 */ 로 주석을 닫을 수 있다.


//----- C언어의 특성 -------
// C언어에서 작성되는 코드는 ;(세미 콜론)으로 끝나야 한다.
// C언어는 대소문자를 구분한다.
// C언어는 자유 형식을 (free-format)을 허용한다. -> ex) int main(){printf("Hello World!");return0;} 이라고 써도 출력된다.
// C언어는 절차지향적 언어이다. (위에서부터 아래의 순서로 절차에 따라서 진행)



//----- 제어 문자 ------
// 출력 결과를 제어해주는 문자
// \n : New line 개행, 커서를 다음줄로 옮김
// \t : Tab 탭, 탭 만큼 공간을 띄움
// \r : Carriage return, 커서를 문자열의 처음으로 옮김
// \b : Back space, 커서 바로 이전의 문자 한 개를 지워줌
// \a : Alert, 경고음을 한 번 발생









int main()								// 주된 코드의 영역을 알려주는 코드
{										// 주된 영역은 반드시 단 하나만 존재해야 된다.
	//printf("Hello World!\n");				// printf : ""(큰 따옴표) 안에 작성된 문자열을 출력해주는 함수 
	//printf("Hello World!");

	//printf("Hello \nworld\n"); // Hello
	//						   // world
	//printf("Hello \tworld\n"); // Hello		world
	//printf("Hello \rworld\n"); // world (Hello가 존재하긴 하지만 Hello 위에 world 가 덮어씌여서 보여주는 것) 
	//printf("Hello \bworld\n"); // Helloworld


	printf("웃음:\t(*^o^*)\n");
	printf("사랑:\t(♥.♥)\n");
	printf("슬픔:\t(ㅠ.ㅠ)\n");
	printf("화남:\t(-_-^)\n");

	printf("이름: 민성기\n");
	printf("나이: 28\n");
	printf("주소: 경남 양산시\n");
	printf("키: 181.3\t몸무게: 73.4Kg\n");


	return 0;							// return 값을 반환해주는 코드
}