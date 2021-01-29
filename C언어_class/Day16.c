#include<stdio.h>

// 함수의 정의 -> 함수를 정의한다.
// 반환형 : 함수 내용의 작업을 마치고 값을 반환해줄 때 사용할 자료형
// 함수 이름 : 함수를 사용하기 위해 호출할 때 사용할 이름
// 매개 변수 : 함수를 호출할 때 값을 전해줄 수 있는데, 이 때 값을 저장하는 변수
// 함수 기능 : 함수의 기능을 맡아줄 코드들이 작성되는 영역
// 
// 함수의 정의 원형 설명
// int ->반환형  Add -> 함수 이름 (int a, int b)  -> 매개 변수
// {		함수 기능 작성
//	return a + b;
// }

// 함수의 정의 원형
// int Add (int a, int b)
// {
//		return a + b;
// }

// 함수의 호출
// 반환값을 저장할 변수 : 함수가 반환해주는 값을 저장할 변수
// 호출할 함수 이름 : 정의된 함수 중 사용할 함수의 이름
// 인수 : 함수가 동작할 때 필요한 값
//
// 반환값을 저장할 변수 = 호출할 함수 이름(인수);   -> 반환값이 존재하는 함수 호출 원형
// 호출할 함수 이름(인수);      -> 반환값이 존재하지 않는 함수 호출 원형

// --------- 함 수 --------------
// 함수를 정의할 때는 반드시 다른 함수 바깥에 정의해야 된다.









int Add(int n1, int n2)
{
	return n1 + n2;
}


void Add2(int n1, int n2)
{
	printf("연산 결과 : %d\n", n1 + n2);

}


void add(int n1, int n2)
{
	printf("더한 값 : %d\n", n1 + n2);
}

void sub(int n1, int n2)
{
	printf("뺀 값 : %d\n", n1 - n2);
}

int multi(int n1, int n2)
{
	return n1 * n2;
}

int div(int n1, int n2)
{
	return n1 / n2;
}


void Calc(int num1, char mark, int num2)    // 이 함수가 위의 함수보다 먼저 되어 있다면 add sub multi div  의 정의를 받지 못하기 때문에 Error가 발생된다.
{
	switch (mark)
	{
	case '+':       // 문자로 입력해도 아스키 코드 43 으로 입력된다.
		add(num1, num2);
		break;
	case '-':
		sub(num1, num2);
		break;
	case '*':
		printf("곱한 값: %d\n", multi(num1, num2));
		break;
	case '/':
		printf("나눈 값 : %d\n", div(num1, num2));
		break;

	}
}

int total(int kor, int math, int eng)
{
	return kor + math + eng;
}


double avg(int kor, int math, int eng)
{
	return total(kor, math, eng) / 3.0;
}

char grade(int kor, int math, int eng)
{

	switch ((int)avg(kor, math, eng)/10)
	{
	case 10:
	case 9:
		return 'A';
	case 8:
		return 'B';
	case 7:
		return 'C';
	case 6:
		return 'D';
	default:
		return 'F';

	}




	return kor + math + eng;
}




int main()
{
	/*int result;
	result = Add(62, 9);
	printf("연산 결과 : %d\n", result);

	result = Add(34, 93);
	printf("연산 결과 : %d\n", result);
*/

	

	/*Add2(8, 31);
	Add2(3, 41);*/


	// Q1 각 연산 결과를 도출 해주는 함수를 작성하시오.
	// + - 반환값 없이
	// * / 반환값 존재


	/*int n1, n2;
	int m_result, d_result;

	printf("두 수 입력 : ");
	scanf("%d %d", &n1, &n2);

	add(n1, n2);
	sub(n1, n2);
	m_result = multi(n1, n2);
	d_result = div(n1, n2);
	printf("곱한 값 : %d\n", m_result);
	printf("나눈 값 : %d\n", d_result);

	printf("곱한 값 : %d\n", multi(n1, n2));
	printf("나눈 값 : %d\n", div(n1, n2));
*/

	// -------------------------------------------------------------------------

	//// Q2 각 연산 결과를 도출 해주는 함수를 작성하세요

	//int num1, num2;
	//char mark;


	//printf("연산 입력 : ");
	//scanf("%d %c %d", &num1, &mark, &num2);

	//Calc(num1, mark, num2);






	//Q1) 철수의 성적을 국어, 수학, 영어 순서로 입력 받은 뒤 총합을 변수 total에 반환해주는 함수,
	/*그 값을 받아 평균을 변수 avg에 반환해주는 함수,
		평균을 비교해 등급을 변수 grade에 반환해주는 함수를
		작성하고 main에서 각 총합, 평균, 등급을 출력해보세요.
		(90점 이상은 A, 80점 이상은 B, 70점 이상은 C, 60점 이상은 D, 60점 미만은 F*/

	int kor, math, eng;

	printf("국어, 수학, 영어 성적 입력 : ");
	scanf("%d %d %d", &kor, &math, &eng);
	printf("총합 : %d\n", total(kor, math, eng));

	printf("평균 : %.2lf\n", avg(kor, math, eng));


	printf("등급 : %c\n", grade(kor, math, eng));






	return 0;
}