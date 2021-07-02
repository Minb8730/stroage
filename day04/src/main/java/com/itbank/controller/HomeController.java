package com.itbank.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.TestDAO;

@Controller
public class HomeController {

	@Autowired
	private TestDAO testDAO;
	
	
	@GetMapping("")
	public String home(Model model) {  	//지금은 Model을 request 라고 생각해보자
		List<String> dbTest = testDAO.test();			// DAO의 메서드 호출 결과를 리스트로 저장하고
		
		model.addAttribute("dbTest", dbTest); 	// 받아온 리스트를 모델 객체에 추가하면(request에 넣으면)		//(name, value)
		return "home";									// home.jsp 에서 값을 출력할 수 있다.
	}
	
	@GetMapping("quiz1")
	public String time(Model model) {
		List<String> dbTime = testDAO.time();
		
		model.addAttribute("time", dbTime);
		return "quiz1";
	}

	/* 위와 같다.
	 * @GetMapping("quiz1") 
	 * public ModelAndView quiz1(ModelAndView mav) {
	 * 		String time = testDAO.getTime();
	 * 		mav.addObject("time", time);
	 * 		mav.setViewName("quiz1");
	 * 
	 * 		model.addAttribute("time", time); 
	 * return "quiz1"; }
	 */	
}
