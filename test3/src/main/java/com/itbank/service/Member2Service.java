package com.itbank.service;

import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.model.Member2DAO;
import com.itbank.model.Member2DTO;

@Service
public class Member2Service {

	@Autowired Member2DAO dao;
	
	private String getHash(String password) {
		String hash = null;
		try {
			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.reset();
			
			md.update(password.getBytes("UTF-8"));
			hash = String.format("%0128x", new BigInteger(1, md.digest()));
		} catch (NoSuchAlgorithmException |UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		
		return hash;
	}
	
	
	
	public Member2DTO login(Member2DTO dto) {
		dto.setUserPw(getHash(dto.getUserPw()));
		
		return dao.login(dto);
	}



	public int insert(Member2DTO dto) {
		dto.setUserPw(getHash(dto.getUserPw()));
		return dao.insert(dto);
	}



	public Member2DTO selectOne(String userId) {
		return dao.selectOne(userId);
	}



	public int updateMember(Member2DTO dto) {
		return dao.updateMember(dto);
	}



	public int delete(String userId) {
		return dao.delete(userId);
	}



	public int updatePassword(Member2DTO dto) {
		dto.setUserPw(getHash(dto.getUserPw()));
		return dao.updatePassword(dto);
	}
	
}
