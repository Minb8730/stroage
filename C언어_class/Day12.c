#include<stdio.h>
#include<windows.h>

// ---- 기타 함수 ------
// system() : system("명령어"), ""(큰 따옴표) 안에 작성되는 명령어를 실행시켜주는 함수
// Sleep(): Sleep(멈춰줄 시간), 시간 단위 1/1000초 이다.           // 반드시 대문자 S 사용할것
// 콘솔창을 잠깐 재워주는 함수, 멈춰 준다고 볼 수 있다.
// system 함수, Sleep 함수를 사용하기 위해서는 windows.h 헤더파일을 선언 해줘야한다.
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
	//printf("ABCD\n");

	//system("cls");

	//printf("EFGH\n");

	//Sleep(5000);   // 5초 Sleep

	//printf("IJKL\n");



	// Q1) 카드 잔액을 충전 및 사용할 수 있는 프로그램을 만드시오
	// 카드 잔액: 10000
	// 1. 카드 잔액 충전
	// 2. 카드 잔액 사용   // 잔액보다 큰 금액 사용할 경우 잔액이 부족합니다. -> 메인화면으로 돌아가는게 아니라 다시 2번 화면으로 돌아온다.
	// 3. 종료
	// switch case

	//int num, money, balance = 10000;
	//printf("카드 잔액 : %d 원 \n", balance);

	//do
	//{
	//	printf("1. 카드 잔액 충전\n");
	//	printf("2. 카드 잔액 사용\n");
	//	printf("3. 종료\n");
	//	printf("입력 : ");
	//	scanf_s("%d", &num);

	//	switch (num)
	//	{
	//	case 1:
	//		printf("충전할 금액 입력 : \n");
	//		scanf_s("%d", &money);
	//		system("cls");
	//		printf("충전 완료!\n카드 잔액 : %d 원\n", balance = balance + money);
	//		break;

	//	case 2:
	//		printf("사용할 금액 입력 : \n");
	//		scanf_s("%d", &money);
	//		system("cls");
	//		if (balance > money)
	//			printf("카드 사용!\n카드 잔액 : %d 원\n", balance = balance - money);
	//		else
	//			printf("잔액이 부족합니다.\n");

	//		break;
	//	default:
	//		printf("잘못된 번호 입력");
	//	}


	//		} while (num != 3);




	int bal = 10000, sel = 1, money;
	
	while (sel != 3)  // 혹은 do while(sel !=3) 로
	{
		system("cls");
		printf("카드 잔액: %d\n", bal);
		printf("1. 카드 잔액 충전\n");
		printf("2. 카드 잔액 사용\n");
		printf("3. 종료\n");
		printf("입력 : ");
		scanf_s("%d", &sel);


		switch (sel)
		{
		case 1:
			system("cls");
			printf("카드 잔액 : %d\n", bal);
			printf("충전 금액 입력 : ");
			scanf_s("%d", &money);

			printf("&d 원 충전해서 %d 원 사용가능합니다.", money, bal += money);
			Sleep(3000);
			break;
		
		case 2:
			while(1)
			{
			system("cls");
			printf("카드 잔액 : %d\n", bal);
			printf("사용 금액 입력 : ");
			scanf_s("%d", &money);
		
			if (bal >= money)
			{
				printf("&d 원 사용하고 %d 원 남았습니다.\n", money, bal -= money);
				break;
			}
			printf("잔액이 부족합니다.\n");
			Sleep(3000);
			}
			Sleep(3000);
			break;
		
		case 3:
			printf("프로그램을 종료합니다.\n");
			Sleep(3000);
			break;
		default:
			printf("1~3 중 하나를 입력해주세요.\n");
			Sleep(1500);
			break;
		
		}

	} 
	return 0;
}