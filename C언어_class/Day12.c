#include<stdio.h>
#include<windows.h>

// ---- ��Ÿ �Լ� ------
// system() : system("��ɾ�"), ""(ū ����ǥ) �ȿ� �ۼ��Ǵ� ��ɾ ��������ִ� �Լ�
// Sleep(): Sleep(������ �ð�), �ð� ���� 1/1000�� �̴�.           // �ݵ�� �빮�� S ����Ұ�
// �ܼ�â�� ��� ����ִ� �Լ�, ���� �شٰ� �� �� �ִ�.
// system �Լ�, Sleep �Լ��� ����ϱ� ���ؼ��� windows.h ��������� ���� ������Ѵ�.
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

	//Sleep(5000);   // 5�� Sleep

	//printf("IJKL\n");



	// Q1) ī�� �ܾ��� ���� �� ����� �� �ִ� ���α׷��� ����ÿ�
	// ī�� �ܾ�: 10000
	// 1. ī�� �ܾ� ����
	// 2. ī�� �ܾ� ���   // �ܾ׺��� ū �ݾ� ����� ��� �ܾ��� �����մϴ�. -> ����ȭ������ ���ư��°� �ƴ϶� �ٽ� 2�� ȭ������ ���ƿ´�.
	// 3. ����
	// switch case

	//int num, money, balance = 10000;
	//printf("ī�� �ܾ� : %d �� \n", balance);

	//do
	//{
	//	printf("1. ī�� �ܾ� ����\n");
	//	printf("2. ī�� �ܾ� ���\n");
	//	printf("3. ����\n");
	//	printf("�Է� : ");
	//	scanf_s("%d", &num);

	//	switch (num)
	//	{
	//	case 1:
	//		printf("������ �ݾ� �Է� : \n");
	//		scanf_s("%d", &money);
	//		system("cls");
	//		printf("���� �Ϸ�!\nī�� �ܾ� : %d ��\n", balance = balance + money);
	//		break;

	//	case 2:
	//		printf("����� �ݾ� �Է� : \n");
	//		scanf_s("%d", &money);
	//		system("cls");
	//		if (balance > money)
	//			printf("ī�� ���!\nī�� �ܾ� : %d ��\n", balance = balance - money);
	//		else
	//			printf("�ܾ��� �����մϴ�.\n");

	//		break;
	//	default:
	//		printf("�߸��� ��ȣ �Է�");
	//	}


	//		} while (num != 3);




	int bal = 10000, sel = 1, money;
	
	while (sel != 3)  // Ȥ�� do while(sel !=3) ��
	{
		system("cls");
		printf("ī�� �ܾ�: %d\n", bal);
		printf("1. ī�� �ܾ� ����\n");
		printf("2. ī�� �ܾ� ���\n");
		printf("3. ����\n");
		printf("�Է� : ");
		scanf_s("%d", &sel);


		switch (sel)
		{
		case 1:
			system("cls");
			printf("ī�� �ܾ� : %d\n", bal);
			printf("���� �ݾ� �Է� : ");
			scanf_s("%d", &money);

			printf("&d �� �����ؼ� %d �� ��밡���մϴ�.", money, bal += money);
			Sleep(3000);
			break;
		
		case 2:
			while(1)
			{
			system("cls");
			printf("ī�� �ܾ� : %d\n", bal);
			printf("��� �ݾ� �Է� : ");
			scanf_s("%d", &money);
		
			if (bal >= money)
			{
				printf("&d �� ����ϰ� %d �� ���ҽ��ϴ�.\n", money, bal -= money);
				break;
			}
			printf("�ܾ��� �����մϴ�.\n");
			Sleep(3000);
			}
			Sleep(3000);
			break;
		
		case 3:
			printf("���α׷��� �����մϴ�.\n");
			Sleep(3000);
			break;
		default:
			printf("1~3 �� �ϳ��� �Է����ּ���.\n");
			Sleep(1500);
			break;
		
		}

	} 
	return 0;
}