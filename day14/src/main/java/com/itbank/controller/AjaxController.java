package com.itbank.controller;

import java.util.HashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.itbank.service.MemberService;

@RestController				// @ResponseBody 를 모든 메서드에 적용한다. : 응답내용은 HTML 코드가 아니다. 
@RequestMapping("/ajax")
public class AjaxController {

	@Autowired private MemberService ms;
	
	
	@PostMapping(value="/checkId", 
				consumes = "application/json; charset=utf-8",	// 함수의 입장에서 소비하는 것, 매개변수 -> json으로 들어오니 utf-8 적용을 시킨다. 매개변수의 유형
				produces = "application/json; charset=utf-8")	// 함수의 입장에서 반환하는 것, return 값 -> 문자열로 반환하니 파싱하지 말고 utf-8을 적용 시킨다. 반환값의 유형
	public String checkId(@RequestBody HashMap<String, String> map) {	// 요청에 들어온 객체( xml에 의해서 jackson 설정을 통해,String 으로 처리된 객체)
		
		boolean flag = ms.exist(map.get("id"));
		
		return flag ? "사용 가능한 ID입니다." : "이미 사용중인 ID입니다.";
	}
	
}



