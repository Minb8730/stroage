package com.itbank.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.member2.MemberDTO;
import com.itbank.service.MemberService;

@Controller
@RequestMapping("/member")
public class MemberController {

	@Autowired private MemberService ms;
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
	
	@GetMapping("/login")
	public void login() {}
	
	@PostMapping("/login")
	public ModelAndView login(MemberDTO dto, HttpSession session, String url) {
		String viewName = "redirect:";
		viewName += url == null ? "/" : url;
		MemberDTO login = ms.login(dto);
		ModelAndView mav = new ModelAndView();					// viewName을 생성자에서 넣지 않고
		mav.setViewName(login != null ? viewName : "msg");
		
		if(login == null) {
			mav.addObject("msg", "로그인 실패");
//			redirect시에 mav에 addObject를 하면 queryString 파라미터로 전달된다
		}
		session.setAttribute("login", login);
		session.setMaxInactiveInterval(600);
		return mav;
	}
	
	@GetMapping("/join")
	public void join() {}
	
	@PostMapping("/join")
	public ModelAndView join(MemberDTO dto) {
		int row = ms.join(dto);
		ModelAndView mav = new ModelAndView("msg");
		mav.addObject("msg", row == 1 ? "회원 가입 성공 !!" : "회원 가입 실패...");
		mav.addObject("url", row == 1 ? "/member/login" : "");
		return mav;
	}
	
	@GetMapping("/info")
	public ModelAndView info(HttpSession session) {
		// ModelAndView 객체가 viewName을 지정받지 않으면 void반환형과 똑같이 작동한다
		
		ModelAndView mav = new ModelAndView();	
		if(session.getAttribute("login") == null) {
			mav.setViewName("msg");
			mav.addObject("msg", "잘못된 접근입니다");
			return mav;
		}
		return mav;
	}
	
	@GetMapping("/delete")
	public ModelAndView delete(HttpSession session) {
		ModelAndView mav = new ModelAndView("msg");

		MemberDTO login = (MemberDTO)session.getAttribute("login");
		int row = ms.delete(login);

		mav.addObject("msg", row == 1 ? "탈퇴처리가 완료되었습니다" : "탈퇴 실패 !!");
		mav.addObject("url", row == 1 ? "/" : "");
		if(row == 1) {
			session.invalidate();
		}

		return mav;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
