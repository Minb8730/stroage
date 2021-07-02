package com.itbank.controller;

import java.io.UnsupportedEncodingException;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.Member;

// 파라미터 주고받기

@Controller
public class Test1Controller {

	// test1 주소에 GET방식으로 접근하면 호출되는 메서드
	@RequestMapping(value="test1", method=RequestMethod.GET)
	public String test1() {
		return "test1-form";
		// request.getRequeispatcher("/WEB-INF/views/test1-form.jsp").foward(request, response) 와 같은 주소가 된다.
	}
	// test1 주소에 POST방식으로 접근하면 호출되는 메서드
//	@RequestMapping(value="test1", method = RequestMethod.POST)
//	public String test1(HttpServletRequest request) throws UnsupportedEncodingException {	// HttpServletRequest : 데이터를 컨트롤러에 보냈을 때, 
//		request.setCharacterEncoding("utf-8");												// HttpServletRequest 객체안의 모든 데이터들이 들어가게 된다.
//		
//		String name = request.getParameter("name");
//		int age = Integer.parseInt(request.getParameter("age"));
//		
//		System.out.println("name : " + name);
//		System.out.println("age : " + age);
//		
//		request.setAttribute("name", name);
//		request.setAttribute("age", age);
//		
//		return "test1-result";
//	}
//	

//	@PostMapping("test1")
//	public ModelAndView test1(String name, int age) {
//		ModelAndView mav = new ModelAndView();
//		mav.setViewName("test1-result");
//		mav.addObject("name", name);	// request.setAttribute("name", value);
//		mav.addObject("age", age);
//		return mav;
//	}

	@PostMapping("test1")  // == @RequestMapping(value="test1", method=RequestMethod.POST)
	public ModelAndView test1(@ModelAttribute("mem") Member mem) { // 기본 생성자가 있어야 사용가능하다.
		ModelAndView mav = new ModelAndView("test1-result"); // Model 이 Request를 처리 ex) 미리 던지고 자신이 가서 잡는다. 동시에 처리
		//mav.addObject("mem",mem); //@ModelAttribute("mem") 를 사용하므로써 Member mem을 바로 넣어주기 때문에 사용할 필요가 없어진다.
//		if(mem.getAge() == 0){ 				// Redirect를 사용하고 싶다면 if문으로 처리를 해주어야한다.
//			mav.setViewName("redirect:http://www.naver.com");
//		}
		return mav; // 반환형은 기본적으로 뷰를 지정하는데 사용한다. 만약 void를 사용한다면 @PostMapping 안의 것에 prefix, suffix 를 붙여서 주소를 찾는다.
	}



	
}
