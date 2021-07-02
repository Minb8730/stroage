package day03;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

//작동 안함, 종류만 나열
@Component	 	// 단순 스프링 빈, 역할을 명시하기 애매한 경우
@Controller		// DispatcherServlet 으로부터 request를 받아서 처리하는 클래스
@Service		// Controller와 Repository 사이에서 순수 자바 로직을 구성하는 클래스
@Repository		// Data의 저장소(Repository), 즉 DB에 접근하는 클래스

public class Battery {

	@Override
	public String toString() {
		return "베터리~";
	}
}
