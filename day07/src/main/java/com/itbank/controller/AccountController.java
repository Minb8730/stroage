package com.itbank.controller;

import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.StudentDTO;
import com.itbank.service.StudentService;

@Controller
public class AccountController {

	@Autowired private StudentService ss;
	
	@GetMapping("updatePassword/{id}")
	public String updatePassword() {
		return "updatePassword";
	}
	
	@PostMapping("updatePassword/{id}")
	public String updatePassword(StudentDTO dto, HttpSession session) throws NoSuchAlgorithmException, UnsupportedEncodingException {
		int row = ss.updatePassword(dto);
		if(row == 1) {
			session.invalidate();
			return "redirect:/login";
		}else {
			return "redirect:/updatePassword/" + dto.getId();  // redirect 는 주소를 바라본다. 즉 GetMapping 의 updatePassword로 간다.
		}
	}
	
	
	
	@GetMapping("findID")
	public void findID() {} // findID.jsp 를 찾는다.
	
	@PostMapping("findID")
	public ModelAndView findId(StudentDTO dto) {
		ModelAndView mav = new ModelAndView("findID"); // findID.jsp 를 찾는다.
		String id = ss.findId(dto);
		String msg = String.format("당신의 ID는 [%s] 입니다.", id);
		mav.addObject("msg", msg);
		return mav;
	}
	
	@ExceptionHandler(EmptyResultDataAccessException.class)
	public ModelAndView emptyId(EmptyResultDataAccessException e) {
		ModelAndView mav = new ModelAndView("findID");
		mav.addObject("msg", "입력한 정보에 맞는 ID가 없습니다.");
		return mav;
	}
	
	@GetMapping("renewPw")
	public void renewPw() {}
	
	@PostMapping("renewPw")
	public ModelAndView renewPw(StudentDTO dto) throws NoSuchAlgorithmException, UnsupportedEncodingException {
		ModelAndView mav = new ModelAndView("renewPw");
		String newPw = ss.renewPw(dto);
		mav.addObject("newPw", newPw); // 해시처리하기 전의 비밀번호
		
		return mav;
	}
	
	
	
	
}
