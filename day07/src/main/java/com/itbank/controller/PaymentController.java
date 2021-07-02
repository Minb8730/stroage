package com.itbank.controller;

import java.util.HashMap;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.StudentDTO;
import com.itbank.service.StudentService;

@Controller
public class PaymentController {

	@Autowired private StudentService ss;
	
	// 돈과 같이 민감한 정보의 변경은 Session 보다 DB를 바로 연결해서 사용하자
	@GetMapping("payment")
	public ModelAndView payment(HttpSession session) {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("payment");
		
		StudentDTO login = (StudentDTO)session.getAttribute("login");
		if(login == null) {
			mav.setViewName("redirect:/login");
			return mav;
		}
		
		// 현재 접속자가 보유한 결제 정보를 view에게 넘겨주는 코드
		HashMap<String, Object> map = ss.selectPayInfo(login.getIdx()); // DTO 대신 사용할 수 있는 class HashMap
		mav.addObject("payinfo", map);
		
		
		return mav;
	}
	
	
	// 만약 구글링을 하고 싶으면, spring controller method argument hashmap  과 같이 중요순부터 앞에서부터
	// 커맨드 객체 대신 HashMap을 사용한다면, 매개변수 앞에 @RequestParam 을 작성하자
	@PostMapping("payment")
	public String payment(@RequestParam HashMap<String, Object> param) {
	//	System.out.println(param);
		int row = ss.updatePayment(param);
		return "redirect:/payment";
	}
}
