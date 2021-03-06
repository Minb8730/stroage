#include<stdio.h>

// ------ 구조체 ------------
// 여러 개의 멤버들을 모아서 하나의 새로운 자료형을 만드는 방식
// 구조체 변수의 멤버에 접근할 때는 구조체변수.멤버 형식으로 접근한다.
//							ex)	struct Data. d;
//								d.data1 = 10;
// 구조체의 크기는 구조체 멤버들을 모두 더한 크기이다.
//
// 기본 구조체 원형:
// struct 구조체이름 {
//		멤버;
// };
//
//

//// 기본 구조체 정의:
//struct Data {     // 자료형을 만들어 준것 뿐이고 공간을 할당 받은 것은 아니다. ex) int, double 자체가 공간을 할당 받는건 아니다.
//	int data1;  // 4byte
//	int data2;  // 4byte
//};
//
//// 별칭을 이용한 구조체 정의:   // -> 별칭을 이용해서 정의할 때는 구조체 이름, 별칭 모두 사용 가능
//typedef struct Data {
//	int data1;
//	int data2;
//}Da;
//
//
//// 익명 구조체 정의:		// -> 익명 구조체를 사용하면 구조체 이름으로 변수 선언 X, 별칭만 사용 가능 
//typedef struct {
//	int data1;
//	int data2;
//}Da2;
//
//
// ------ 구조체 포인터 ----------
// 구조체 포인터를 이용해서 역참조를 진행할 때는 기본적으로 ->(애로우)를 사용해서 진행할 수 있다.
// 별도로 *를 사용할 수 있는데 이때는 우선순위 때문에 괄호로 묶어줘야 한다.
//		ex) (*d).data1 == d->data1
//
//




//------------------------------- 문제 풀이 1---------------------------------

//typedef struct {
//	int kor;
//	int math;
//	int eng;
//	int total;
//	double avg;
//	char grade;
//}scores;
//
//
//void Total(int kor, int math, int eng, int* total)
//{
//	*total = kor + math + eng;
//}
//
//void Avg(int total, double* avg)
//{
//	*avg = total / 3.0;
//}
//
//void Grade(double avg, char* grade)
//{
//	switch ((int)avg / 10)
//	{
//	case 10:
//	case 9:
//		*grade = 'A';
//		break;
//	case 8:
//		*grade = 'B';
//		break;
//	case 7:
//		*grade = 'C';
//		break;
//	case 6:
//		*grade = 'D';
//		break;
//	Default:
//		*grade = 'F';
//		break;
//	}
//}

//---------------------------------------------------------------------------------------

//
//typedef struct {
//	int data1;
//	int data2;
//}Da;
//

//void Func(Da d)
//{
//	d.data1 = 11;
//	d.data2 = 22;
//}

//
//void Func(Da* d)
//{
//	(*d).data1 = 11;   // *d.data1 을 사용하면 .이 먼저 실행되기 때문에 애스탈리스크를 먼저 사용하기 위해 식을 바꾸어준다.
//	d->data2 = 22; //  = (*d).data2 
//}




//------------------------------- 문제 풀이 2---------------------------------
//각 함수에서는 구조체의 모든 멤버에 접근할 수 있어야 합니다.

typedef struct {
	int kor;
	int math;
	int eng;
	int total;
	double avg;
	char grade;
}scores;


void Total(scores* data)
{
	data->total = data->kor + data->math+ data->eng;    // (*data).total = (*data).kor + (*data).math + (*data).eng
}

void Avg(scores* data)
{
	data->avg = data->total / 3.0;
}

void Grade(scores* data)
{
	switch ((int)data->avg / 10)
	{
	case 10:
	case 9:
		data->grade = 'A';
		break;
	case 8:
		data->grade = 'B';
		break;
	case 7:
		data->grade = 'C';
		break;
	case 6:
		data->grade = 'D';
		break;
	Default:
		data->grade = 'F';
		break;
	}
}

int main()
{

	//struct Data d;

	//d.data1 = 10;          // struct 안의 변수에 값을 할당하기
	//d.data2 = 20;

	//printf("%d %d \n", d.data1, d.data2);
	//printf("d의 크기 : %d \n", sizeof(d));   // -> 8
	////					stack
	//-----------------------------------------------------------------------
	//main		  10		 20
	//			 data1		data2
	//					d
	//-----------------------------------------------------------------------


	//Da d2;
	//Da2 d3;

	//	---------------------------------------------------------------------------------------------

	//Q1 철수의 성적을 국어, 수학, 영어 순서로 입력 받은 후 
	//세 성적의 총합을 메인의 total 변수에 할당해주는 함수,
	//성적의 평균을 메인의 avg 변수에 할당해주는 함수,
	//평균에 해당하는 등급을 나누고 메인의 grade 변수에 할당해주는 함수를 만드시오.
	//출력은 반드시 main함수에서 진행하세요.
	//모든 함수는 반환값이 존재하지 않는 형태로 작성해보세요.
	//필요한 변수들은 구조체를 통해서 선언하세요.
	//90점 이상은 A, 80점 이상은 B, 70점 이상은 C, 60점 이상은 D, 60점 미만은 F
	

	/*scores data;

	printf("국어, 수학, 영어 성적 입력 : ");
	scanf("%d %d %d", &data.kor, &data.math, &data.eng);


	Total(data.kor, data.math, data.eng, &data.total);
	Avg(data.total, &data.avg);
	Grade(data.avg, &data.grade);

	printf("총합 : %d\n", data.total);
	printf("평균 : %.2lf\n", data.avg);
	printf("등급 : %c\n", data.grade);*/

	//-----------------------------------------------------------------------------------------


	//Da d;
	//d.data1 = 10;
	//d.data2 = 20;

	//Func(d);


	//printf("%d %d\n", d.data1, d.data2); // -> 10, 20


	//					stack
	//-----------------------------------------------------------------------
	//main		  10		 20
	//			 data1		data2
	//					d
	//-----------------------------------------------------------------------
	//Func		  11		 22
	//			 data1		data2		-> 실행 후 삭제
	//					d
	//-----------------------------------------------------------------------

	//Da d;
	//d.data1 = 10;
	//d.data2 = 20;

	//Func(&d);


	//printf("%d %d\n", d.data1, d.data2); // -> 11, 22

	//					stack
	//-----------------------------------------------------------------------
	//main		  10		 20
	//			 data1		data2
	//					d
	//-----------------------------------------------------------------------
	//Func		  11		 22
	//			 data1		data2		-> 값을 main에 넘겨준다.
	//					d
	//-----------------------------------------------------------------------


	// ------------ 문제 2 -----------------------------------------------

	//Q1 철수의 성적을 국어, 수학, 영어 순서로 입력 받은 후 
	//세 성적의 총합을 메인의 total 변수에 할당해주는 함수,
	//성적의 평균을 메인의 avg 변수에 할당해주는 함수,
	//평균에 해당하는 등급을 나누고 메인의 grade 변수에 할당해주는 함수를 만드시오.
	//출력은 반드시 main함수에서 진행하세요.
	//모든 함수는 반환값이 존재하지 않는 형태로 작성해보세요.
	//필요한 변수들은 구조체를 통해서 선언하세요.
	//각 함수에서는 구조체의 모든 멤버에 접근할 수 있어야 합니다.
	//90점 이상은 A, 80점 이상은 B, 70점 이상은 C, 60점 이상은 D, 60점 미만은 F
	//각 함수는 메인에 존재하는 모든 멤버에 접근할 수 있어야한다는거예요~~!!


	scores data;

	printf("국어, 수학, 영어 성적 입력 : ");
	scanf("%d %d %d", &data.kor, &data.math, &data.eng);


	Total(&data);
	Avg(&data);
	Grade(&data);

	printf("총합 : %d\n", data.total);
	printf("평균 : %.2lf\n", data.avg);
	printf("등급 : %c\n", data.grade);

	
	return 0;
}
