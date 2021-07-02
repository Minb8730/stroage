package com.itbank.service;

import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Service;

import com.itbank.model.StudentDAO;
import com.itbank.model.StudentDTO;

@Service
public class StudentService {

	@Autowired
	private StudentDAO dao;
	
	public List<StudentDTO> selectAll() {
		return dao.selectAll();
	}

	public int insert(StudentDTO dto) throws DataAccessException, NoSuchAlgorithmException, UnsupportedEncodingException {
		// 단순 사용자 입력값과, insert 문에 필요한 값의 차이가 있는데, 이를 다듬어서 SQL에 들어가기 직전의 형태로 잡아준다.
		dto.setDue(dto.getStype().equals("ib") ? 1500000 : 700000);
		dto.setSfund(dto.getStype().equals("ib") ? 1200000 : 0);

		// 평문 비밀번호를 sha-512로 hashing 하기 위해서, utf-8방식으로 읽은 후, 128자리의 16진수 형태로 변경한 값을 dto에 setting
//		String pw = dto.getPw();
//		MessageDigest md = MessageDigest.getInstance("SHA-512");  // hash 알고리즘 이름, 알고리즘 못찾을 경우 예외처리
//		md.reset();
//		
//		md.update(pw.getBytes("utf-8")); // encoding 예외처리
//		String hashpw = String.format("%0128x", new BigInteger(1, md.digest()));
//		
//		dto.setPw(hashpw);
		
		dto.setPw(getHash(dto.getPw()));
		
		return dao.insert(dto);
	}

	private String getHash(String text) throws NoSuchAlgorithmException, UnsupportedEncodingException {
		
		MessageDigest md = MessageDigest.getInstance("SHA-512");  // hash 알고리즘 이름, 알고리즘 못찾을 경우 예외처리
		md.reset();
		
		md.update(text.getBytes("utf-8")); // encoding 예외처리
		String hashpw = String.format("%0128x", new BigInteger(1, md.digest()));
		
		return hashpw;
	}

	public StudentDTO login(StudentDTO inputData) throws NoSuchAlgorithmException, UnsupportedEncodingException {
		inputData.setPw(getHash(inputData.getPw()));
		return dao.selectOne(inputData);

	}


	
}