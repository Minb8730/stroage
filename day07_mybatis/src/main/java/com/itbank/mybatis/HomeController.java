package com.itbank.mybatis;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.service.TestService;

@Controller
public class HomeController {
	
	
	@Autowired private TestService ts;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView home(ModelAndView mav) {
		mav.setViewName("home");
		
		List<String> list = ts.getTest();
		
		mav.addObject("list", list);
		
		return mav;
	}
	
}
