package day01;

import java.util.Arrays;
import java.util.List;


abstract class Unit{
	
	private String name;
	
	public Unit(String name) { // 반드시 매개변수를 전달해야만 객체를 생성할 수 있다.
		this.name = name;
	}
	public abstract void intro();	//반드시 intro를 재정의해야만 객체를 생성할 수 있다.
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
}

public class Ex03 {
	public static void main(String[] args) {
		Unit u1 = new Unit("마린") {
			@Override
			public void intro() {
				System.out.println(super.getName() + " : Who wanna piece of meat?");
				}
		};
		
		
		Unit u2 = new Unit("파이어뱃") {	// 익명 클래스는 기존 클래스를 상속받는 이름없는 새로운 클래스
			@Override
			public void intro() {
				System.out.println(super.getName() + " : Need a lighter...?");
			}
		};
		Unit[] arr = { u1,u2};
		List<Unit> list = Arrays.asList(arr);
		list.forEach((unit) -> unit.intro()); //함수 자체를 개체로 사용하지 못하고 함수형 인터페이스는 람다식으로 개체를 생성할수 있다.
		
	}
		
	
}
