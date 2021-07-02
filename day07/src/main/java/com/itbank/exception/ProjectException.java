package com.itbank.exception;

import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;

import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.ModelAndView;

// 프로젝트 전역에 걸쳐 적용되는 예외 처리 클래스

@ControllerAdvice
public class ProjectException {

	// Controller 혹은 ControllerAdvice 에서 사용 가능
	
	@ExceptionHandler(NoSuchAlgorithmException.class)
	public String nsa() {
		return "redirect:/";
	}
	
	@ExceptionHandler(UnsupportedEncodingException.class)
	public String usee() {
		return "redirect:/";
	}
	
	@ExceptionHandler(NullPointerException.class)
	public ModelAndView npe(NullPointerException e) {
		ModelAndView mav = new ModelAndView("alert");
		mav.addObject("msg", "널 포인터 예외가 발생했습니다. 관리자에게 문의바랍니다.");
		return mav;
	}
}
