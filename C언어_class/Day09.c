#include<stdio.h>


// ----- 조건문 -------
// switch ~ case 의 원형:
// switch (비교할 값)
// {
//		case 해당 값:		// 각 조건
//			 종속 문장;
//			 break;
//		default:			// 나머지 // else 와 같은 조건
//			 종속 문장;
//			 break;
// }
//
// switch ~ case 문에서 break 구문은 해당 문법을 탈출하는 용도로 사용된다.
// 하지만 프로그래머가 의도적으로 break를 작성하지 않는 경우도 있다.
//
// switch ~ case 문에서 비교할 값 공간에는 정수, 정수로 변환할 수 있는 값, 정수가 저장된 변수만 작성할 수 있다.
// 각 case 에 작성되는 값은 반드시 상수로 작성해줘야 한다.
//







int main()
{
	/*int num;

	printf("입력 : ");
	scanf_s("%d", &num);

	switch (num)
	{
		case 1:
			printf("num은 1입니다.\n");
			break;
		case 2:
			printf("num은 2입니다.\n");
			break;
		case 3:
			printf("num은 3입니다.\n");
			break;
		case 4:
			printf("num은 4입니다.\n");
			break;
		default:
			printf("1 ~ 4 중 하나를 입력해주세요.\n");
			break;
	}	*/


	//int num;

	//printf("입력 : ");
	//scanf_s("%d", &num);

	//switch (num)  // -> double , float 등 정수 형태가 아니면 Error 발생
	//{
	//case 4:   // -> 변수 작성 Error 발생. 상수만 입력
	//	printf("4");
	//case 3:
	//	printf("3");
	//case 2:
	//	printf("2");
	//case 1:
	//	printf("1");
 //
	//	// break 구문을 일부러 작성하지 않을수도 있다.
	//}



	// Q1) 숫자를 입력 받고 해당 숫자가 14이상일 때는 "14보다 크거나 같은 수"를 출력
	// 14미만일 때는 "14보다 작은 수"를 출력 해주는 프로그램 작성 switch case

	int num;

	printf("숫자 입력 : ");
	scanf_s("%d", &num);

	
	switch (num > 13)
	{
	case 0:
		printf("14보다 작은 수\n");
		break;
	default:
		printf("14보다 크거나 같은 수\n");
		break;
	}


	//Q2 숫자를 입력 받고 숫자가 3의 배수일 때는 참, 아닐 때는 거짓을 출력하는 프로그램 작성

	printf("숫자 입력 : ");
	scanf_s("%d", &num);


	switch (num % 3)
	{
	case 0:
		printf("참\n");
		break;
	default:
		printf("거짓\n");
		break;
	}


	// Q1


	int kor, math, eng;
	double avg;

	printf("국어 점수 입력 : ");
	scanf_s("%d", &kor);
	printf("수학 점수 입력 : ");
	scanf_s("%d", &math);
	printf("영어 점수 입력 : ");
	scanf_s("%d", &eng);
	printf("평균 : %.2f\n", avg = (kor + math + eng) / 3.0);
	switch ((int)avg /10)
	{
	case 10:
	case 9:
		printf("등급 : A");
		break;
	case 8:
		printf("등급 : B");
		break;
	case 7:
		printf("등급 : C");
		break;
	case 6:
		printf("등급 : D");
		break;
	default:
		printf("등급 : F");

	}


	return 0;
}