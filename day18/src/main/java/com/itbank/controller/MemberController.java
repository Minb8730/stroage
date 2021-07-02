package com.itbank.controller;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.itbank.member.MemberDTO;
import com.itbank.service.MemberService;

@RestController
@RequestMapping("/member")
public class MemberController {

	@Autowired private MemberService ms;
	private ObjectMapper mapper = new ObjectMapper();
	
	
	@DeleteMapping(value="/{userid}")
	public int deleteMember(@PathVariable String userid) {
		return ms.deleteMember(userid);
	}
	
	
	// 맴버 변수를 소비하면 consumes, return 값이 있으면 produces 작성
	@GetMapping(value="/", produces="application/json; charset=utf-8")
	public String memberList() throws JsonProcessingException {
		List<HashMap<String, String>> list = ms.selectList(); // MemberDTO로 받으면 지정한 필드 이외의 값도 전부 받아와서 null 처리를 하기때문에 hashmap 으로 받고 싶은 값만 받아온다.
		String json = mapper.writeValueAsString(list);
//		System.out.println(json);
		return json;
	}
	
	
	
	@GetMapping(value = "/{userid}")
	public String member(@PathVariable String userid) throws JsonProcessingException{
		// 전달받은 userid를 이용하여 service -> dao 형식으로 객체를 하나 불러온다.
		MemberDTO dto = ms.select(userid);
		String json = mapper.writeValueAsString(dto); // 객체를 String 으로 변환
		System.out.println(json);
		return json;
	}
	
//			consumes = "application/json; charset=utf-8") // headers 를 포함할 경우 작성
	@PostMapping("/")
	@ResponseBody
	public String member(MemberDTO dto) {
		int row = ms.insert(dto);
		return row + "";
	}
	
	@PutMapping(value = "/", consumes = "application/json; charset=utf-8")
	public int update(@RequestBody MemberDTO dto) {
		return ms.update(dto);
	}
	
	
	
	
}
