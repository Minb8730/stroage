package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller	// 이 클래스는 스프링 컨트롤러로 작동하는 클래스인깐, 스프링 빈으로 등록해두세요
			// 첫번째 패키지는 context-component:scan의 대상으로 등록되어 있습니다.
public class HomeController {

	@RequestMapping("") 	// 요청주소가 "" 이면, 아래 메서드를 실행하며 문자열을 반환합니다. form과 같이 다음으로 넘겨줄 요청주소 작성
	public String home() {
		return "home";		// 반환되는 문자열은 prefix + 문자열 + suffix 가 되어서 jsp를 가리킵니다.
							// DispatcherServlet은 가리키는 jsp로 forward해서 응답을 만들어냅니다.
	}
	
}
