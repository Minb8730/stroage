package day01;

// 보안과 유지 보수를 위해 계층을 나누어서 동작시킨다.

class DTO {
	// 단위 유닛 클래스에 대한 정의(자바 빈즈 형식)
	// 다양한 형태라면 상속을 활용할 수 있다.
}

class Storage {
	// 개별 객체를 관리할 수 있는 컬렉션과 대응되는 메서드의 구현
	// 다형성을 고려하여 컬렉션을 분리할 수 있다.
}

class Handler {
	// Storage 에 저장된 데이터를 CRUD하는 메서드를 정의하고, Storage에 접근하는 내용
	// 슈퍼클래스로 분류하거나, 서브클래스로 분류하여 메서드에 영향받는 범위를 조절할 수 있다.
}

public class Ex05 {
	public static void main(String[] args) {
		// 사용자 입력을 전달받아서 Handler의 메서드를 호출하는 기능 구현

	
	
	}
}
