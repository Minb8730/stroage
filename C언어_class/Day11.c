#include<stdio.h>

// ------- 반복문 --------
// while() 문의 원형:
//		초기식;
//
// while (조건식)
//		{
//			종속 문장 및 변화식;
//		}
// while() 문에서 초기식은 while 문 바깥에 존재해야 하고, 변화식은 종속 문장과 같이 존재한다.
// while() 문에서 무한루프를 사용할 때는 조건식에 1을 작성해주면 된다.
// while() 문에서 종속 문장이 한 줄일때는 {}(중괄호)를 생략해줄 수 있다.
// 하지만 종속 문장에 변화식이 같이 작성되기 때문에 {}(중괄호)를 생략하는 경우는 거의 없다.
//
// do - while() 문의 원형:
//		초기식;
//
// do
//		{
//			종속 문장 및 변화식;
//		} while (조건식);
// 
// do ~ while() 문은 while 문과 전체적으로 비슷하지만 종속 문장을 최소 한 번은 실행시킨다는 특징을 갖고있다.
// do ~ while() 문에서 무한루프를 사용하고 싶을 때는 while 문과 마찬가지로 조건식에 1을 작성해주면 된다.
//
//
//
//
//
//
//
//
//
//
//
//

int main()
{
	//초기식;

	//while (조건식)
	//{
	//	종속 문장 및 변화식;

	//}

	//int i = 0;

	//while (i < 10)
	//{
	//	printf("Hello world\n");
	//	i++;
	//}

	//
	//// 무한 루프
	//while (1)
	//{
	//	printf("Hello world infinity loop\n");
	//}





	////Q1 별도의 입력 없이 알파벳 A~Z까지 출력되는 프로그램을 작성

	//int i = 'A';

	//while (i <= 'Z')
	//{
	//	printf("%c\n", i);
	//	i++;
	//}



	////Q2

	//char alpha;
	//int c = 'a';

	//printf("알파벳 하나 입력 : ");
	//scanf_s("%c", &alpha);

	//while (c <= alpha)
	//{
	//	printf("%c\n", c);
	//	c++;
	//}



	////Q3

	//int beta;

	//while (1)
	//{
	//	printf("숫자 하나 입력 : ");
	//	scanf_s("%d", &beta);

	//	if (beta == 9)
	//		break;
	//}


	//int i = 7;

	// do
	//{
	//	printf("Hello world!\n");
	//	i--;
	//} while (i <= 6);   // 무한 루프 그리고 while(1) 도 초기식 없이 무한루프로 사용.  



	// Q1) 반복적으로 숫자를 입력, 출력 하는데 이 때, 짝수가 입력되면 종료되게 만드시오.

	int num;
	
	do
	{
		printf("숫자 입력 : ");
		scanf_s("%d", &num);
	} while (num % 2);

	printf("짝수가 입력되어 프로그램을 종료합니다.");





	return 0;
}