package com.itbank.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.StudentDTO;
import com.itbank.service.StudentService;

@Controller
public class HomeController {

	@Autowired
	private StudentService ss;
	
	@GetMapping("")
	public ModelAndView home(ModelAndView mav) {
		List<StudentDTO> list = ss.selectAll();
		mav.addObject("list", list);
		
		mav.setViewName("home");
		return mav;
	}
	
		
	
	
}
