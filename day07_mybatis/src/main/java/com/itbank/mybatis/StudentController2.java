package com.itbank.mybatis;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.StudentDTO;
import com.itbank.service.StudentService;

@Controller
public class StudentController2 {

	@Autowired private StudentService ss;
	
	@GetMapping("/studentList2")
	public ModelAndView studentList2() {
		ModelAndView mav = new ModelAndView("studentList2");
		
		List<StudentDTO> list = ss.selectStudentList2();
		
		mav.addObject("list", list);
		
		return mav;
	}
	
}
