package com.itbank.controller;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.itbank.service.Hash;
import com.itbank.service.MailService;

@RestController
public class MailController {

	@Autowired private MailService mailService;
	
	
	@GetMapping(value = "/mailto/{mailAddress}/", produces = "application/text; charset=utf-8")
	public String mailto(@PathVariable String mailAddress, HttpSession session) throws IOException {
		System.out.println("mailto 함수 호출!!");
	
		// 지정한 파일에 기록된 계정 정보를 문자열 형태로 불러오기
		String filePath = session.getServletContext().getRealPath("WEB-INF/data/mailAccount.dat");
		File f = new File(filePath);
		if(f.exists() == false) {
			return "메일 전송에 필요한 계정 정보를 찾을 수 없습니다.";
		}
		Scanner sc = new Scanner(f);
		String account = null;
		while(sc.hasNextLine()) {
			account = sc.nextLine();
			System.out.println(account);
		}
		sc.close();
		
		String authNumber = mailService.getAuthNumber();		// 인증번호 6 자리를 받아서
		String hashNumber = Hash.getHash(authNumber);			// 해시 처리하고
		
		session.setAttribute("hashNumber", hashNumber);			// 일단 세션에 저장해둔다.
		
		System.out.println("메일 받을 주소 : " + mailAddress);
		
		String result = mailService.sendMail(mailAddress, authNumber, account);
		
		if(result.equals(authNumber)) { // 만들어낸 인증번호와 서비스에서 메일을 보낸 인증번호가 서로 일치한다.
			return hashNumber;			// 인증번호의 해시값을 반환한다.
		}else {
			return result;
		}
		
	}
	
	
	
	@GetMapping(value = "/getAuthResult/{userNumber}")
	public boolean getAuthResult(@PathVariable String userNumber, HttpSession session) {
		String hashNumber = (String)session.getAttribute("hashNumber");
		boolean flag = hashNumber.equals(Hash.getHash(userNumber));
		// getHash(authNumber) == getHash(userNumber)
		
		return flag;
	}
	
}
