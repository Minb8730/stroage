package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.Member;

@Controller
public class NaverController {

	@RequestMapping(value="naver", method=RequestMethod.GET)
	public String naver() {
		return "naver-form";
	}
	
	@PostMapping("naver")
	public ModelAndView naver (@ModelAttribute("mem") Member mem) {
		ModelAndView mav = new ModelAndView("naver-result");
		return mav;
	}
	
	
	
	
	
}