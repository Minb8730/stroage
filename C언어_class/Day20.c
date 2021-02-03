#include<stdio.h>
#include<stdlib.h>

// ------ 포인터와 배열의 관계 -----------------------
// 포인터와 배열은 밀접한 관계를 갖고 있으나, 분명한 차이점이 있다.
// 배열은 선언하게 되면 기본적으로 배열 자기 자신의 시작 주소를 갖고 있다.

//---------(메모리 공간) 동적 할당 ---------------------------
// 메모리 공간의 크기를 지정해서 할당 받고 그 공간을 사용 후, 원하는 시점에서 공간을 해제하는 방식  <-> 기존에는 변수선언과 같은 고정된 메모리 크기를 통해 할당 받음.
// 메모리 공간을 할당받을 때는 malloc() 함수를 사용해서 할당 받을 수 있다.(memory allocation)
// 이때, 반드시 stdlib.h 헤더파일을 선언해줘야 한다.
// malloc()함수 원형:
// malloc(할당 받고 싶은 크기의 byte) -> 반환값이 있음.
// 
// 주소를 저장할 변수 = (저장할 변수의 자료형)malloc(크기);
// 동적 할당을 통해서 할당받은 메모리 공간은 Heap영역에 해당한다. 
// 동적 할당받은 메모리 공간을 해제할 때는 free(해제할 공간의 주소); 형식으로 해제할 수 있다.
// 한 번의 동적 할당에는 반드시 한 번의 동적해제가 진행돼야 한다.
// malloc() 함수에서 크기를 넘겨줄 때는 기본적으로 sizeof() 연산자를 이용해서 넘겨준다.


typedef struct {
	int data1;
	int data2;
	int data3;
}Da;



int main()
{

	Da d;
	Da* pd;

	pd = &d;

	printf("d의 크기 : %d\n", sizeof(d));  // 12byte의 크기 data1 data2 data3 각각 4byte
	printf("pd의 크기 : %d\n", sizeof(pd)); // 4byte-> 주소값의 크기  pd는 별도의 멤버가 존재하지 않음. 포인터 변수는 주소를 저장해주기 위해 존재하기 때문에 4byte 고정이다.

	printf("\npd의 값 : %p\n", pd); // 16진수 8자리로 주소값을 출력 -> 2진수로 전환하면 32bit 이기 때문에 주소값은 4byte 이다.



	//char str[10];

	//printf("str의 주소 : %p\n", &str);
	//printf("str의 값 : %p\n", str);  // 주소 값을 가지고 있다.

	//printf("입력 : ");
	//scanf_s("%s", str); // 때문에 &str 로 작성하지 않아도 된다.

	//printf("출력: %s\n", str);


	char str1[10] = "Hello";
	char* str2 = "Abcde";

	printf("str1 : %s\n", str1);
	printf("str2 : %s\n", str2);

	str1[0] = 'B'; // char 형태로 저장되어 있는 데이터를 여러번 출력하는것이기 때문에 문제 없음
	//str2[0] = 'Z'; // 리터럴 상수 형태로 저장되어 있는 str2 은 수정할 수 없음
	printf("str1 : %c%c%c%c%c\n", str1[0], str1[1], str1[2], str1[3], str1[4]);
	printf("str2 : %c%c%c%c%c\n", str2[0], str2[1], str2[2], str2[3], str2[4]);


	//int* ptr;
	//ptr = (int*)malloc(4);
	//
	//*ptr = 5;
	//printf("%d", *ptr);

	//free(해제할 공간의 주소);
	//free(ptr); // 출력 결과로는 해제되었는지 확인 할 수 없음.


	//int* ptr;
	//ptr = (int*)malloc(8);

	//ptr[0] = 10;
	//ptr[1] = 20;

	//printf("%d %d\n", ptr[0], ptr[1]);
	//free(ptr);



	int* ptr;
	ptr = (int*)malloc(sizeof(int) * 2);  // 위와 다르게 가독성을 높일 수 있음

	ptr[0] = 10;
	ptr[1] = 20;

	printf("%d %d\n", ptr[0], ptr[1]);
	free(ptr);










	return 0;
}