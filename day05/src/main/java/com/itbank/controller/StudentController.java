package com.itbank.controller;

import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.StudentDTO;
import com.itbank.service.StudentService;

@Controller
public class StudentController {

	@Autowired
	private StudentService ss;

	@GetMapping("login")
	public void login() {}
	
	@PostMapping("login")
	public String login(StudentDTO inputData, HttpSession session) throws NoSuchAlgorithmException, UnsupportedEncodingException { 
		StudentDTO login = ss.login(inputData);	// id와 pw 가 일치하는 계정 하나를 반환
		session.setAttribute("login", login);
		session.setMaxInactiveInterval(600);
//		ModelAndView mav = new ModelAndView();
//		mav.setViewName(login == null? "alert" : "redirect:/");
//		mav.addObject("msg", login == null ? "계정이나 비밀번호가 일치하지 않습니다." : "성공(메세지 출력 안함)");
		return "redirect:/";
	}
	
	@ExceptionHandler(EmptyResultDataAccessException.class)
	public ModelAndView notfound() {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("alert");
		mav.addObject("msg", "계정이나 비밀번호가 일치하지 않습니다." );
		return mav;
	}
	
	@GetMapping("join")
	public void join() {}

	
	@PostMapping("join")		// controller 의 throws 처리는 DispatcherServlet 으로가고 여기서 처리가 안되면 Advice로 넘긴다.
	public ModelAndView join(StudentDTO dto) throws DataAccessException, NoSuchAlgorithmException, UnsupportedEncodingException{	// 스프링 커맨드 객체;
		ModelAndView mav = new ModelAndView("redirect:/");
		int row = ss.insert(dto); // 영향받은 줄의 수를 반환, 0이 될 경우는 pk의 중복, unique 키의 중복 등
//		if(row == 0 ) {				// 때문에 이 처리는 무결성에 위반되기 때문에 ExceptionHandler가 처리해준다.
//			mav.addObject("msg","회원 가입 실패!!");
//			mav.setViewName("alert");	//jsp로 팝업 띄우고 다른 페이지로 이동하는 기능
//		}
		
		return mav; 
	}
	
	@ExceptionHandler(DataIntegrityViolationException.class)  // ExceptionHandler 가 @Repository 에서 발생하는 에러를 묶어서 Controller 로 전가
	public ModelAndView studentException(DataAccessException e) {		// Controller 혹은 ControllerAdvice 에서 사용 가능
		ModelAndView mav = new ModelAndView("alert");						
		mav.addObject("msg","회원 가입 실패!!");
		return mav;
		
	}
	
	
}
