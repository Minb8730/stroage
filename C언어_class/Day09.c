#include<stdio.h>


// ----- ���ǹ� -------
// switch ~ case �� ����:
// switch (���� ��)
// {
//		case �ش� ��:		// �� ����
//			 ���� ����;
//			 break;
//		default:			// ������ // else �� ���� ����
//			 ���� ����;
//			 break;
// }
//
// switch ~ case ������ break ������ �ش� ������ Ż���ϴ� �뵵�� ���ȴ�.
// ������ ���α׷��Ӱ� �ǵ������� break�� �ۼ����� �ʴ� ��쵵 �ִ�.
//
// switch ~ case ������ ���� �� �������� ����, ������ ��ȯ�� �� �ִ� ��, ������ ����� ������ �ۼ��� �� �ִ�.
// �� case �� �ۼ��Ǵ� ���� �ݵ�� ����� �ۼ������ �Ѵ�.
//







int main()
{
	/*int num;

	printf("�Է� : ");
	scanf_s("%d", &num);

	switch (num)
	{
		case 1:
			printf("num�� 1�Դϴ�.\n");
			break;
		case 2:
			printf("num�� 2�Դϴ�.\n");
			break;
		case 3:
			printf("num�� 3�Դϴ�.\n");
			break;
		case 4:
			printf("num�� 4�Դϴ�.\n");
			break;
		default:
			printf("1 ~ 4 �� �ϳ��� �Է����ּ���.\n");
			break;
	}	*/


	//int num;

	//printf("�Է� : ");
	//scanf_s("%d", &num);

	//switch (num)  // -> double , float �� ���� ���°� �ƴϸ� Error �߻�
	//{
	//case 4:   // -> ���� �ۼ� Error �߻�. ����� �Է�
	//	printf("4");
	//case 3:
	//	printf("3");
	//case 2:
	//	printf("2");
	//case 1:
	//	printf("1");
 //
	//	// break ������ �Ϻη� �ۼ����� �������� �ִ�.
	//}



	// Q1) ���ڸ� �Է� �ް� �ش� ���ڰ� 14�̻��� ���� "14���� ũ�ų� ���� ��"�� ���
	// 14�̸��� ���� "14���� ���� ��"�� ��� ���ִ� ���α׷� �ۼ� switch case

	int num;

	printf("���� �Է� : ");
	scanf_s("%d", &num);

	
	switch (num > 13)
	{
	case 0:
		printf("14���� ���� ��\n");
		break;
	default:
		printf("14���� ũ�ų� ���� ��\n");
		break;
	}


	//Q2 ���ڸ� �Է� �ް� ���ڰ� 3�� ����� ���� ��, �ƴ� ���� ������ ����ϴ� ���α׷� �ۼ�

	printf("���� �Է� : ");
	scanf_s("%d", &num);


	switch (num % 3)
	{
	case 0:
		printf("��\n");
		break;
	default:
		printf("����\n");
		break;
	}


	// Q1


	int kor, math, eng;
	double avg;

	printf("���� ���� �Է� : ");
	scanf_s("%d", &kor);
	printf("���� ���� �Է� : ");
	scanf_s("%d", &math);
	printf("���� ���� �Է� : ");
	scanf_s("%d", &eng);
	printf("��� : %.2f\n", avg = (kor + math + eng) / 3.0);
	switch ((int)avg /10)
	{
	case 10:
	case 9:
		printf("��� : A");
		break;
	case 8:
		printf("��� : B");
		break;
	case 7:
		printf("��� : C");
		break;
	case 6:
		printf("��� : D");
		break;
	default:
		printf("��� : F");

	}


	return 0;
}