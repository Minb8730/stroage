package com.itbank.controller;

import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.Member2DTO;
import com.itbank.service.Member2Service;

@Controller
@RequestMapping("/member")
public class MemberController {

	@Autowired Member2Service ms;
	
	@PostMapping("updatePassword/{userId}")
	public String updatePassword(Member2DTO dto, HttpSession session) {
		int row = ms.updatePassword(dto);
		if(row == 1) {
			session.invalidate();
			return "redirect:/member/login";
		}else {
			return "redirect:/updatePassword/" + dto.getUserId();  // redirect 는 주소를 바라본다. 즉 GetMapping 의 updatePassword로 간다.
		}
	}
	
	@GetMapping("/updatePassword/{userId}")
	public ModelAndView updatePassword(@PathVariable String userId) {
		ModelAndView mav = new ModelAndView("member/updatePassword");
		Member2DTO dto = ms.selectOne(userId);
		mav.addObject("dto", dto);
		return mav;
	}
	
	@GetMapping("delete/{userId}")
	public String deleteMember(@PathVariable String userId, HttpSession session) {
		int row= ms.delete(userId);		
		if(row==1) {				
			session.invalidate();	
			return "redirect:/";	
		}
		return "redirect:/mypage";
	}
	
	
	
	
	@GetMapping("/update/{userId}")
	public ModelAndView update(@PathVariable String userId) {
	ModelAndView mav = new ModelAndView("member/update");
		
		Member2DTO dto = ms.selectOne(userId); 
		mav.addObject("dto", dto);
		
		return mav;
	}

	@PostMapping("/update/{userId}")
	public String updateMember(Member2DTO dto, HttpSession session) {
		int row = ms.updateMember(dto);
		session.invalidate();
		
		return "redirect:/member/login";
	}
			
	
	@GetMapping("/mypage")
	public ModelAndView myPage(ModelAndView mav) {
		mav.setViewName("member/mypage");
		return mav;
	}
	
	
	@GetMapping("/insert")
	public String insertMember() {
		return "member/insert";
	}
	
	
	@GetMapping("logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/member/login";
	}
	
	@PostMapping("/insert")
	public ModelAndView insert(Member2DTO dto) {
		
		int row = ms.insert(dto);
		
		ModelAndView mav = new ModelAndView("redirect:/member/login");
		return mav;
	}
	
	
	
	@GetMapping("/login")
	public String loginMember() {
		return "member/login";
	}
	
	@PostMapping("/login")
	public String login(Member2DTO dto, HttpSession session) throws NoSuchAlgorithmException, UnsupportedEncodingException { 
		Member2DTO login = ms.login(dto);	
		
		session.setAttribute("login", login);
		session.setMaxInactiveInterval(1000);
		return "redirect:/board/list?page=1&type=&search=";
	}	
	
	@ExceptionHandler(EmptyResultDataAccessException.class)
	public ModelAndView notfound() {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("alert");
		mav.addObject("msg", "계정이나 비밀번호가 일치하지 않습니다." );
		return mav;
	}
	
	@ExceptionHandler(DataIntegrityViolationException.class)  
	public ModelAndView studentException(DataAccessException e) {		
		ModelAndView mav = new ModelAndView("alert");						
		mav.addObject("msg","회원 가입 실패!!");
		return mav;
		
	}
	
	
}
