#include<stdio.h>

// �Լ��� ���� -> �Լ��� �����Ѵ�.
// ��ȯ�� : �Լ� ������ �۾��� ��ġ�� ���� ��ȯ���� �� ����� �ڷ���
// �Լ� �̸� : �Լ��� ����ϱ� ���� ȣ���� �� ����� �̸�
// �Ű� ���� : �Լ��� ȣ���� �� ���� ������ �� �ִµ�, �� �� ���� �����ϴ� ����
// �Լ� ��� : �Լ��� ����� �þ��� �ڵ���� �ۼ��Ǵ� ����
// 
// �Լ��� ���� ���� ����
// int ->��ȯ��  Add -> �Լ� �̸� (int a, int b)  -> �Ű� ����
// {		�Լ� ��� �ۼ�
//	return a + b;
// }

// �Լ��� ���� ����
// int Add (int a, int b)
// {
//		return a + b;
// }

// �Լ��� ȣ��
// ��ȯ���� ������ ���� : �Լ��� ��ȯ���ִ� ���� ������ ����
// ȣ���� �Լ� �̸� : ���ǵ� �Լ� �� ����� �Լ��� �̸�
// �μ� : �Լ��� ������ �� �ʿ��� ��
//
// ��ȯ���� ������ ���� = ȣ���� �Լ� �̸�(�μ�);   -> ��ȯ���� �����ϴ� �Լ� ȣ�� ����
// ȣ���� �Լ� �̸�(�μ�);      -> ��ȯ���� �������� �ʴ� �Լ� ȣ�� ����

// --------- �� �� --------------
// �Լ��� ������ ���� �ݵ�� �ٸ� �Լ� �ٱ��� �����ؾ� �ȴ�.









int Add(int n1, int n2)
{
	return n1 + n2;
}


void Add2(int n1, int n2)
{
	printf("���� ��� : %d\n", n1 + n2);

}


void add(int n1, int n2)
{
	printf("���� �� : %d\n", n1 + n2);
}

void sub(int n1, int n2)
{
	printf("�� �� : %d\n", n1 - n2);
}

int multi(int n1, int n2)
{
	return n1 * n2;
}

int div(int n1, int n2)
{
	return n1 / n2;
}


void Calc(int num1, char mark, int num2)    // �� �Լ��� ���� �Լ����� ���� �Ǿ� �ִٸ� add sub multi div  �� ���Ǹ� ���� ���ϱ� ������ Error�� �߻��ȴ�.
{
	switch (mark)
	{
	case '+':       // ���ڷ� �Է��ص� �ƽ�Ű �ڵ� 43 ���� �Էµȴ�.
		add(num1, num2);
		break;
	case '-':
		sub(num1, num2);
		break;
	case '*':
		printf("���� ��: %d\n", multi(num1, num2));
		break;
	case '/':
		printf("���� �� : %d\n", div(num1, num2));
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
	printf("���� ��� : %d\n", result);

	result = Add(34, 93);
	printf("���� ��� : %d\n", result);
*/

	

	/*Add2(8, 31);
	Add2(3, 41);*/


	// Q1 �� ���� ����� ���� ���ִ� �Լ��� �ۼ��Ͻÿ�.
	// + - ��ȯ�� ����
	// * / ��ȯ�� ����


	/*int n1, n2;
	int m_result, d_result;

	printf("�� �� �Է� : ");
	scanf("%d %d", &n1, &n2);

	add(n1, n2);
	sub(n1, n2);
	m_result = multi(n1, n2);
	d_result = div(n1, n2);
	printf("���� �� : %d\n", m_result);
	printf("���� �� : %d\n", d_result);

	printf("���� �� : %d\n", multi(n1, n2));
	printf("���� �� : %d\n", div(n1, n2));
*/

	// -------------------------------------------------------------------------

	//// Q2 �� ���� ����� ���� ���ִ� �Լ��� �ۼ��ϼ���

	//int num1, num2;
	//char mark;


	//printf("���� �Է� : ");
	//scanf("%d %c %d", &num1, &mark, &num2);

	//Calc(num1, mark, num2);






	//Q1) ö���� ������ ����, ����, ���� ������ �Է� ���� �� ������ ���� total�� ��ȯ���ִ� �Լ�,
	/*�� ���� �޾� ����� ���� avg�� ��ȯ���ִ� �Լ�,
		����� ���� ����� ���� grade�� ��ȯ���ִ� �Լ���
		�ۼ��ϰ� main���� �� ����, ���, ����� ����غ�����.
		(90�� �̻��� A, 80�� �̻��� B, 70�� �̻��� C, 60�� �̻��� D, 60�� �̸��� F*/

	int kor, math, eng;

	printf("����, ����, ���� ���� �Է� : ");
	scanf("%d %d %d", &kor, &math, &eng);
	printf("���� : %d\n", total(kor, math, eng));

	printf("��� : %.2lf\n", avg(kor, math, eng));


	printf("��� : %c\n", grade(kor, math, eng));






	return 0;
}