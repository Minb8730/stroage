package com.itbank.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.itbank.member.MemberDTO;
import com.itbank.service.MemberService;

@RestController
public class AjaxController {

	@Autowired private MemberService ms;
	
	
	@PostMapping("/login")
	public boolean login(@RequestBody MemberDTO member, HttpSession session) {
		
		MemberDTO login = ms.login(member);
		if(login != null) {
			session.setAttribute("login", login);
			session.setMaxInactiveInterval(60*60*3);
			return true;
		}else {
			return false;
		}
	}
}
