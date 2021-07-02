package day01;

class StaticTest{
	static int n1;
	int n2;
	
	static int f1() {
		return n1;
	}
	int f2() {
		return n2;
	}
	static int f3(){
		//return n2;
		//Cannot make a static reference to the non-static field n2
		return 0;
		}
}

public class Ex02 {
	public static void main(String[] args) {
		// 클래스
		// 변수 : 단일 데이터를 저장하는 메모리 공간
		// 배열 : 같은 자료형의 변수를 연속된 메모리 공간에묶어서 관리
		// 구조체(C언어) : 서로 다른 자료형의 변수를 묶어서 관리하는 사용자 정의 자료형
		// 구조체는 자료형이고, 구조체를 이용한 변수를 만들어야 데이터를 저장할 수 있다.
		
		// 클래스 : 구조체 + 함수 
		// 전부 자료형을 기반으로 설명이 가능
		
		// OOP : Object Oriented Programming  클래스 기반, 객체가 있어야 실행될 수 있지만 main 함수는 static 이기 때문에 실행 가능
 		// Procedure Oriented Programming 	함수 기반
		// 객체 지향 <=> 절차 지향 (X) - 절차 지향이 진화해서 객체 지향
		
		// 객체가 메서드를 포함하기 때문에, 절차 지향에서 객체 지향으로 넘어가면 메인함수의 코드가 짧아진다.
		// ex) 절차 지향은 결혼에 대한 모든 것을 작성해야 하지만 객체 지향은 결혼이란 행위만 작성하고 내용들은 클래스들을 가져다가 사용
		
		// 필드, 메서드, 생성자, 접근제한자 +(GC) // GC는 수준급이 아니면 직접제한하기를 권고하지 않는다.
		// getter / setter
		// static / final // final 을 method에 사용하면 override 불가능
		
		// static 요소의 로딩 시점
		// 프로그램 실행 -> 클래스 로딩 - > 메인함수 호출 -> 객체 생성 -> 메인함수 종료
		//				import		main		new Object()	return
		//				static // static 요소는 none static 요소를 참조할 수 없다. 즉 객체 등을 참조 불가능 StaticTest 에 설명
		
		// 상속
		// extends : 기존 클래스를 물려받아서, 개념을 확장하여 새로운 클래스를 만들어낸다.
		// 하나부터 열까지 내가 다 만들 필요가 없다.
		// 자바는 다중 상속의 문제를 회피하기 위해서, 특수한 경우를 제외하고 단일 상속만 가능하다.
		// super는 하나만 가리킨다.
		// implements 도 크게보면 상속이지만, 구분하기 위해서 단어를 다르게 쓴다.
		
		// 받은거 그대로 쓸거면, 굳이 왜 상속을 할까? 그냥 가져와서 사용하면 되는데
		// 변경하기 위해서 상속하는 거고, 대표적인 방법이 오버라이딩이다.
		
		// 오버라이딩 시 신경쓰지 않으면 오버로딩이 되버릴 수 있으므로, 이노테이션을 활용해라(가독성이나 컴파일러에게 알려주기 위해)
		
		// Object
		// 모든 객체는 같은 형태로 취급 가능하다.
		// 객체라면 가지는 필수 요소가 Object에 정의되어 있다.
		
		// 추상 클래스 : 추상 메서드를 포함할 수 있는 클래스(일반 메서드도 포함한다.)  // interface 는 하나부터 열까지 모두 구현해야 될떄
		// 추상 메서드 : 내용(body, 몸체)가 정의되지 않는 메서드, 호출할 수 없으나 오버라이딩 가능
		// 인터페이스 : static final 필드와 추상 메서드만 포함할 수 있는 클래스
		
		Runnable r1 = new Runnable() {
			
			@Override
			public void run() {
				System.out.println("r1");
			}
		};
		
		Runnable r2 = () -> System.out.println("r2");	// java 1.8 이상부터 사용할 수 있는 람다식
		
		r1.run();
		r2.run();
		
		// java.util. 에 대한 공부
		// Thread 중요하지만 기본적으로 어렵고, 다른 바라의 개념이 충부해야 이해 가능
		// File 파일을 읽는 정도는 기본적으로 할수 있도록
		// InputStream, OutputStream, Socket, URL, InetAddress 스트림에 대한 이해
		
		// Map의 key는 Array/List의 index와 동일한 역할이다.
		// 중복 배제를 하고싶으면 Set을 사용하면 된다
		// 대부분의 컬렉션은 기본 for문과 연동할 수 있는 자료형을 제공한다 (Iterator, Enumeration)
		// 컬렉션의 static method 를 이용하면 정렬이나 탐색을  수월하게 수행할 수 있다.(DB가 하면 굳이 할 필요 없음)
		// List와 Map은 계~속 사용한다.
		// List, Set, Map 은 인터페이스 형태이다. (서브 클래스가 상속/ 구현 하여 완성된다.)
		// Comparator, Comparable 연습해보기
		
		// Socket/ Buffer 공부해보기
		
		// web이든 app이든 terminal 프로그램이든, 특정 자료형에 대한 CRUD는 거의 필수이다.
		
		// 개념 충돌이 나면은 SOLID를 찾아볼것
		
		
		
		
		
		
		
		
		
		
		
	}
}
