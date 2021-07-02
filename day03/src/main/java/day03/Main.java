package day03;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Main {

	public static void main(String[] args) {
		ApplicationContext ctx =
				new GenericXmlApplicationContext("classpath:appCtx.xml");
		
		Member m0 = new Member("테스트",20);
		Member m1 = ctx.getBean("m1", Member.class);	// 값 주입 안함
		Member m2 = ctx.getBean("m2", Member.class);	// 생성자 매개변수 (constructor-arg)
		Member m3 = ctx.getBean("m3", Member.class);	// setter	(property)

		System.out.println(m0.getName());
		System.out.println(m1.getName());
		System.out.println(m2.getName());
		System.out.println(m3.getName());
		
		System.out.println(m0);
		m0 = new Member("테스트2", 22);
		System.out.println(m0); // 새로운 객체 생성
		
		System.out.println(m1);
		m1 = ctx.getBean("m1", Member.class);
		System.out.println(m1); // 기존의 객체를 다시 불러옴
				
		System.out.println("====================================================");
		
		Toy t1 = (Toy)ctx.getBean("t1");
		
		Toy t2 = ctx.getBean("t2", Toy.class);
		
		Toy t3 = ctx.getBean("t3", Toy.class);
		
		Battery b1 = ctx.getBean(Battery.class); // 베터리 자료형의 객체가 하나이기 때문에 이름을 설정해 주지 않아도 된다.
		
		t1.show(); // Toy.java 에서 @Autowired 로 인해서 자동으로 베터리 객체가 참조 된다. 어노테이션을 삭제하면 베터리 참조가 해제된다.
		t2.show();
		t3.show();
		
		System.out.println(b1);
		System.out.println(b1 == t2.getB());
		System.out.println(t2.getB() == t3.getB());
	}
}
