package day03;

import org.springframework.beans.factory.annotation.Autowired;

public class Toy {
	
	@Autowired private Battery b;
	
	public Toy() {}
	public Toy(Battery b) {
		this.b = b;
	}
	public void show() {
		System.out.println(b != null ? "장난감이 움직입니다." : "베터리가 없습니다.");
	}
	public void setB(Battery b) {
		this.b = b;
	}
	public Battery getB() {
		return this.b;
	}
	
}
