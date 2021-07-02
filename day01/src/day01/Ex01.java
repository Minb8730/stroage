package day01;

public class Ex01 {
	public static void main(String[] args) {
		//컴퓨터의 모든 데이터는 2진수로 구성되어 있음
		
		/*
		 * 원시형(primitive type)
		 * boolean	true/false		1/0		0000 0001/ 0000 0000	1byte
		 * byte		2^8			-128 ~127							/1byte
		 * short	2^16		-32768 ~ 32767						2byte
		 * char		2^16(unsigned, +만 있음) 0 ~ 65535					2byte
		 * int		2^32		-21억~ + 21억
		 * float
		 * long		2^64
		 * double
		 * 
		 * 각 원시형에 대응하는 wrapper class 알아보기
		 * 
		 * 참조형(reference tpye)
		 */ 
		// 지역변수, 멤버필드, 정적변수
		// 형변환, (up-casting, down-casting)
		// Wrapper Class 의 활용(static 메서드)
		
		// 연산자, 연산자 우선순위. [.은 어떤 연산자보다도 우선한다.]
		// 단항 연산, 다항 연산, 삼항 연산, 연산자는 값을 만들거나 변경한다.
		// 연산자는 한 줄 안에 처리가 가능하다.
		
		// 제어문
		// if : 무조건 else if 로 처리하려고 하지 말기. 중첩된 단순 if 가 더 효율적인 경우도 있다.
		// switch ~ case : break 안쓸수도 있다. 문자열 비교 가능. Map으로 대체할 수 있다.
		// while : 제사용가능한 if이다. 그냥 while로 사용해도 무방
		// for : 향상된 for문 사용법 익히기. 컬렉션.forEach 익히기. 순차처리는 효율이 좋지 않다.
		// break : 경우에 따라서는 return이 더 나을 수도 있다.
		// continue : 안써도 되는 경우가 있다.
		// return : 메서드는 어떤 상황에서도 반드시 값을 return 하도록(void, 생성자 제외)
		
		//for문 안에 return해도 for문 끝날때 return도 해줘야한다.
	
		// 함수
		// 매개변수, 반환형의 이해.
		// 프로그램 자체도 거대한 하나의 함수이다.
		// 입력이 있고, 출력이 있고, 처리 과정이 있다면 그건 함수 (= 알고리즘, 문제 해결, 메서드)
		// 오버로딩 : 비슷한 기능의 함수가 서로 이름이 달라서 호출하는 입장에서 불편하니까 생겼음.
		
		// 배열
		// 같은 자료형이면 무조건 배열로 묶을 수 있다.
		// 배열은 리스트로 변환 가능
		// 인덱스는 항상 0부터 시작해서 [길이-1] 까지 존재한다.
		// arr.length / string.lenth() / list.size()
		// 객체의 배열인 경우, 배열이 생성되어도 객체 생성자가 호출되지 않으면 null이다.
		// {null, null, null}
		
		
		
		
		
		
	}
}
