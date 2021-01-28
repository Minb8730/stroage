#include<stdio.h>
//
// ----- 문자열 입력받는 방법 -------
// scanf()함수를 통해 문자열을 입력받을 때는 배열이름 앞에 &나 배열의 뒤에 인덱스를 작성하지 않는다.
// 문자열의 끝에는 항상 문자열의 끝을 알려주는 NULL문자가 들어간다.
// 문자열을 배열에 저장할 때는 반드시 NULL 문자의 크기까지 고려해줘야 한다.
// NULL 문자를 표기할 때는 정수 0, 문자'\0', NULL로 표기할 수 있다. 따옴표 차이 구분할 것 
// 문자열을 담을 배열을 초기화 할 때는 ""(큰 따옴표) 안에 문자열을 작성해주면 된다. 
//				ex) char str[6] = "Hello";
// 문자열을 담을 배열을 NULL 문자로 초기화 할 때는
// char str[10] = { 0, }; 과 같이 작성하면 된다.
//
//
//
//
//
//
//

int main()
{

	//char str[5];  // Hello 출력

	//printf("문장 입력 : ");
	//scanf("%s", str);    // 문자열을 저장하고 나서 문자열이 끝난다는 것을 알려주는 NULL로 끝마치게 되는데 5개에 딱 맞게 Hello 를 써 넣게 되면 Error 가 발생한다.
	//			   		 // Hello(Null)

	//str[2] = 0;  // '\0' , NULL   따옴표 차이 구분하기  -> He 까지 출력되고 NULL을 만나서 He만 출력

	//printf("출력 : %s\n", str);



	//char str[6] = "Hello";
	//printf("출력 : %s\n", str);



	//char str[10] = { 0, };

	//printf("입력 : ");
	//scanf("%s", str);

	//str[5] = 'a';  // Null 자리에 a를 실수로 대입했을때 값이 이상하게 출력. 이때 변수를 0으로 초기화해 둔다면 Error는 발생하지 않는다.

	//printf("출력 : %s\n", str);


	//Q1) 이름, 나이, 주소, 키, 몸무게를 입력 받고 아래와 같이 출력되는 프로그램을 만드시오

	char name[10], adr[100];
	int age;
	float height, weight;
	

	printf("이름: ");
	scanf("%s", name);
	printf("나이: ");
	scanf("%d", &age);
	printf("주소: ");
	scanf("%s", adr);
	printf("키: ");
	scanf("%f", &height);
	printf("몸무게: ");
	scanf("%f", &weight);
	system("cls");


	printf("출력\n");
	printf("----------------------------------\n");
	printf("이름: %s\n", name);
	printf("나이: %d\n", age);
	printf("주소: %s\n", adr);
	printf("키: %.1f cm			몸무게: %.2f kg", height, weight);
	





	return 0;
}