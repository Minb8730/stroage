package com.itbank.service;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.member.MemberDAO;
import com.itbank.member.MemberDTO;

@Service
public class MemberService {

	@Autowired private MemberDAO dao;
	
	public MemberDTO select(String userid) {
		MemberDTO dto = dao.select(userid);
		if(dto != null)
			dto.setUserpw("******");	// 비밀번호 노출시키고 싶지 않을때
		return dto;
	}

	public int insert(MemberDTO dto) {
		return dao.insert(dto);
	}

	public List<HashMap<String, String>> selectList() {
		return dao.selectList();
	}

	public int deleteMember(String userid) {
		int result = dao.deleteMember(userid);
		return result;
	}

	public int update(MemberDTO dto) {
		return dao.update(dto);
	}

	
	
	
	
}
