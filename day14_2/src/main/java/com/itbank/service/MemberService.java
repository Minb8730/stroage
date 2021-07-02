package com.itbank.service;

import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.member2.MemberDAO;
import com.itbank.member2.MemberDTO;

@Service
public class MemberService {
	
	@Autowired private MemberDAO dao;

	private String getHash(String input) {
		String hash = null;
		try {
			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.reset();
			md.update(input.getBytes("UTF-8"));
			hash = String.format("%0128x", new BigInteger(1, md.digest()));
		} catch (NoSuchAlgorithmException | UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		return hash;
	}
	
	public int join(MemberDTO dto) {
		dto.setUserpw(getHash(dto.getUserpw()));
		return dao.insert(dto);
	}

	public MemberDTO login(MemberDTO dto) {
		dto.setUserpw(getHash(dto.getUserpw()));
		return dao.login(dto);
	}

	public int delete(MemberDTO login) {
		return dao.delete(login);
	}

}
