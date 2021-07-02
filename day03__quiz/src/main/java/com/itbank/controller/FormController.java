package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class FormController {
	
	@GetMapping({"", "/", "home"}) // 여러개의 주소를 사용하고 싶으면 배열 {, , ,} 형식으로 사용하면 된다.
	public String home() {
		return "home";
	}
}




