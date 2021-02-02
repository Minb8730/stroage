#include<stdio.h>

// ------ ����ü ------------
// ���� ���� ������� ��Ƽ� �ϳ��� ���ο� �ڷ����� ����� ���
// ����ü ������ ����� ������ ���� ����ü����.��� �������� �����Ѵ�.
//							ex)	struct Data. d;
//								d.data1 = 10;
// ����ü�� ũ��� ����ü ������� ��� ���� ũ���̴�.
//
// �⺻ ����ü ����:
// struct ����ü�̸� {
//		���;
// };
//
//

//// �⺻ ����ü ����:
//struct Data {     // �ڷ����� ����� �ذ� ���̰� ������ �Ҵ� ���� ���� �ƴϴ�. ex) int, double ��ü�� ������ �Ҵ� �޴°� �ƴϴ�.
//	int data1;  // 4byte
//	int data2;  // 4byte
//};
//
//// ��Ī�� �̿��� ����ü ����:   // -> ��Ī�� �̿��ؼ� ������ ���� ����ü �̸�, ��Ī ��� ��� ����
//typedef struct Data {
//	int data1;
//	int data2;
//}Da;
//
//
//// �͸� ����ü ����:		// -> �͸� ����ü�� ����ϸ� ����ü �̸����� ���� ���� X, ��Ī�� ��� ���� 
//typedef struct {
//	int data1;
//	int data2;
//}Da2;
//


//------------------------------- ���� Ǯ�� ---------------------------------

typedef struct {
	int kor;
	int math;
	int eng;
	int total;
	double avg;
	char grade;
}scores;


void Total(int kor, int math, int eng, int* total)
{
	*total = kor + math + eng;
}

void Avg(int total, double* avg)
{
	*avg = total / 3.0;
}

void Grade(double avg, char* grade)
{
	switch ((int)avg / 10)
	{
	case 10:
	case 9:
		*grade = 'A';
		break;
	case 8:
		*grade = 'B';
		break;
	case 7:
		*grade = 'C';
		break;
	case 6:
		*grade = 'D';
		break;
	Default:
		*grade = 'F';
		break;
	}
}



int main()
{

	//struct Data d;

	//d.data1 = 10;          // struct ���� ������ ���� �Ҵ��ϱ�
	//d.data2 = 20;

	//printf("%d %d \n", d.data1, d.data2);
	//printf("d�� ũ�� : %d \n", sizeof(d));   // -> 8
	////					stack
	//-----------------------------------------------------------------------
	//main		  10		 20
	//			 data1		data2
	//					d
	//-----------------------------------------------------------------------


	//Da d2;
	//Da2 d3;

	//	---------------------------------------------------------------------------------------------

	//Q1 ö���� ������ ����, ����, ���� ������ �Է� ���� �� 
	//�� ������ ������ ������ total ������ �Ҵ����ִ� �Լ�,
	//������ ����� ������ avg ������ �Ҵ����ִ� �Լ�,
	//��տ� �ش��ϴ� ����� ������ ������ grade ������ �Ҵ����ִ� �Լ��� ����ÿ�.
	//����� �ݵ�� main�Լ����� �����ϼ���.
	//��� �Լ��� ��ȯ���� �������� �ʴ� ���·� �ۼ��غ�����.
	//�ʿ��� �������� ����ü�� ���ؼ� �����ϼ���.
	//90�� �̻��� A, 80�� �̻��� B, 70�� �̻��� C, 60�� �̻��� D, 60�� �̸��� F
	

	scores data;

	printf("����, ����, ���� ���� �Է� : ");
	scanf("%d %d %d", &data.kor, &data.math, &data.eng);


	Total(data.kor, data.math, data.eng, &data.total);
	Avg(data.total, &data.avg);
	Grade(data.avg, &data.grade);

	printf("���� : %d\n", data.total);
	printf("��� : %.2lf\n", data.avg);
	printf("��� : %c\n", data.grade);















	return 0;
}
