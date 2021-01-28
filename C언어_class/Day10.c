#include<stdio.h>

// ----- 반복문 ---------
// 조건식을 비교하면서 참일 경우 종속 문장을 실행시키고 변화식을 거쳐 조건식을 또 다시 비교하는 문법
// for(), while(), do ~ while() 3가지가 존재
//
// for문의 기본 원형:
// for (초기식; 조건식; 변화식)
// {
//		종속 문장;
// }
//
// 초기식 -> 조건식 -> 종속 문장 -> 변화식 -> 조건식 -> 종속 문장 -> 변화식 -> ... 순으로 진행 된다.
// for 문에서 무한루프를 사용하고 싶을때는 초기식, 조건식, 변화식을 생략하면 된다.  ex) for(;;)
// for 문에서 종속 문장이 한 줄일때는 {}(중괄호}를 생략할 수 있다.

// ----- 기타 구문 ----------
// break: 해당 구문을 만나게 되면 반복문을 탈출
// continue: 해당 구문을 만나게 되면 continue 보다 아래 있는 종속 문장은 실행하지 않고 진행된다.
//
//
//



int main()
{

	//int i;  // 옛날에는 for 문 밖에 변수를 지정해주었지만 비효율적인 문법이므로 for 안으로 변수를 넣었다.


	//for (int i = 0; i < 10; i++)
	//{
	//	printf("Hello world\n");
	//}

	////printf("i의 값 : %d", i);  // for 문 밖에서 변수를 선언 했을 때 10의 값을 출력 하지만 for 문 안에서 변수를 선언 했을 때는 지역변수가 되어서 i 의 값에 접근 할수 없다.


	//for (; ; )   // 무한 루프를 하기 위해서 초기식, 조건식, 변화식을 생략해준다.
	//{
	//	printf("Hello world");
	//}


	//for (;;)	// 종속문장에 중괄호가 없을 경우 다음 문장 하나만 무한 루프가 진행된다.
	//	printf("Hello world\n");
	//	printf("End!!\n");


	//for (int i = 0; i < 10; i++)
	//{
	//	if (i == 5)
	//		break;
	//	printf("Hello world! i : %d\n", i);
	//}


	//for (int i = 0; i < 10; i++)
	//{
	//	if (i == 5)
	//		continue;
	//	printf("Hello world! i : %d\n", i);
	//}

	//Q1 별도의 입력 없이 알파벳 A~Z 까지 출력되는 프로그램을 작성
	/*for (int i = 65; i < 91 ; i++)
		printf("%c\n", i);

	for (int i = "A"; i <= "Z"; i++)
		printf("%c\n", i);*/
		
		////Q2 소문자 알파벳 하나를 입력 받고, a부터 입력 받은 알파벳 까지 출력되는 프로그램을 작성

	//char alpha;

	//printf("알파벳 하나 입력 : ");
	//scanf_s("%c", &alpha);

	//for (int i = "a"; i <= alpha; i++)
	//	printf("%c\n", i);

	//Q3 숫자 한 개를 입력 받고 출력을 반복 하다가 숫자 9가 입력 됐을 때 종료되는 프로그램 작성

	
	//int num;

	//for (;;) {

	//	printf("숫자 한개 입력 : ");
	//	scanf_s("%d", &num);
	//	if (num == 9)
	//		break;
	//	printf("%d\n", num);
	//}


	// 25번 반복
	/*for (int i = 0; i < 5; i++ )
	{
		for (int j = 0; j < 5; j++)
		{
			printf("i : %d, j : %d", i, j);
		}
		printf("\n");
	}*/


	//*****
	//*****
	//*****
	//*****
	//*****
	for (int i = 0; i < 5; i++)
	{
		for (int i = 0; i < 5; i++)
		{
			printf("*");
		}
		printf("\n");

	}

	//**   
	// **
	//  **
	//   **
	//    **

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < i; j++) // 0,1,2,3,4
		{
			printf(" ");
		}
		printf("**\n");
	}

	
	//    *   
	//   ***
	//  *****
	// *******
	//*********

	for (int i = 0; i < 5; i++)		// 5층 까지
	{
		for (int j = i; j < 4; j++)    // 4, 3, 2, 1, 0
		{
			printf(" ");
		}

		for (int k = 0; k < i * 2 + 1; k++)    // 1, 3, 5, 7, 9
		{
			printf("*");
		}
		printf("\n");
	}


	for (int i = 0; i < 5; i++)		// 5층 까지
	{
		for (int j = 0; j < i; j++)    /// 0, 1, 2, 3, 4
		{
			printf(" ");
		}

		for (int k = 0 ; k < 9 - (i * 2); k++)    // 9, 7, 5, 3, 1
		{
			printf("*");
		}
		printf("\n");
	}






	//3)  for 문 결합
	//*********      9
	//**     **    2  5  2
	//* *   * *  1 1 1 3 1 1 1
	//*  * *  *  1 2 1 1 1 2 1
	//*   *   *    1 3 1 3 1 
	//*  * *  *  1 2 1 1 1 2 1
	//* *   * *  1 1 1 3 1 1 1
	//**     **    2  5  2
	//*********       9

	for (int i = 0; i < 9; i++)		// 9층 까지
	{
		for (int j = 0; j <= i; j++)    // 처음 * 숫자
		{
			if (8 % j == 0)   
				printf("*");

			else if (8 % 2 == 0)
				printf("*");

			else
				printf("*");
		}

		for (int c = 0; c = i; c++)  // 가운데 * 숫자
		{
			if (i % 4 == 0)
				printf("*");
		}
			
			


		//for (int k = 0; k < 9 - (i * 2); k++)    // 9, 7, 5, 3, 1
		//{
		//	printf(" ");
		//}
		//printf("\n");
	}





	return 0;
}