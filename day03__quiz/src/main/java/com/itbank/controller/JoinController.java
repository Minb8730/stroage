package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.MemberDTO;

@Controller
public class JoinController {

//	@GetMapping("join")
//	public String join() {
//		return "join";
//	}

	@GetMapping("join") // 반환형이 void이면 요청 주소를 반환 문자열로 간주한다(JSP의 이름)
	public void join() {}
	
	@PostMapping("join")
	public String join(@ModelAttribute("newbie") MemberDTO newbi) {
		return "joinResult";
	}
}
