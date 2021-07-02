package com.itbank.service;

import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.List;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.model.BoardDAO;
import com.itbank.model.BoardDTO;

@Service
public class BoardService {

	@Autowired private BoardDAO dao;
	
	private final String uploadPath = "D:\\upload";

	public List<BoardDTO> selectAll(HashMap<String, String> param) {
		boolean flag1 = false, flag2 = false;
		if(param != null) {
			flag1 = param.size() == 2;
//			flag2 = param.get("search").equals("") == false;
		}
		return (flag1 && param.get("search").equals("") == false) ? dao.selectSearch(param) : dao.selectAll();
	}

	public BoardDTO selectOne(int idx) {
		return dao.selectOne(idx);
	}

	public int insertBoard(BoardDTO dto) {
		int row = 0;
		// 첨부파일이 있으면 작동하는 코드
		if(dto.getFile().getOriginalFilename().equals("") == false) {
			String fileName = UUID.randomUUID().toString().replaceAll("-", "");
			int beginIndex = dto.getFile().getOriginalFilename().indexOf(".");
			String extName = dto.getFile().getOriginalFilename().substring(beginIndex);
			fileName += extName;
			
			File f = new File(uploadPath, fileName);
			
			try {
				dto.getFile().transferTo(f);
				
			} catch (IllegalStateException | IOException e) {
				System.out.println("업로드 문제 발생 : " + e);
			}
			dto.setUploadFile(fileName);
		}
		// 패스워드를 해시처리하여 저장하는 코드
		String password = dto.getPassword();
		try {
			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.reset();
			
			md.update(password.getBytes("UTF-8"));
			String hash = String.format("%0128x", new BigInteger(1, md.digest()));
			dto.setPassword(hash);
			
		} catch (NoSuchAlgorithmException | UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		
		row = dao.insert(dto);
		if(row != 0) {
			return dao.selectMaxIdx();
		}
		return row;
	}

	public int updateViewCount(int idx) {
		return dao.updateViewCount(idx);
	}

	public int deleteBoard(int idx, String password) {
		String hash = null;
		try {
			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.reset();
			
			md.update(password.getBytes("UTF-8"));
			hash = String.format("%0128x", new BigInteger(1, md.digest()));
			
		} catch (NoSuchAlgorithmException | UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		// myBatis에서는 파라미터의 개수가 최대 1개로 제한되어 있다
		HashMap<String, Object> map = new HashMap<String, Object>();
		map.put("idx", idx);
		map.put("password", hash);
		int row = dao.deleteBoard(map);
		return row;
	}

	public int modify(BoardDTO dto) {
		// 비밀번호가 일치하지 않으면 중단한다
		String hash = null;
		int row = 0;
		try {
			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.reset();
			
			md.update(dto.getPassword().getBytes("UTF-8"));
			hash = String.format("%0128x", new BigInteger(1, md.digest()));
			
		} catch (NoSuchAlgorithmException | UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		// 첨부파일이 있으면 작동하는 코드
		if(dto.getFile().getOriginalFilename().equals("") == false) {
			String fileName = UUID.randomUUID().toString().replaceAll("-", "");
			int beginIndex = dto.getFile().getOriginalFilename().indexOf(".");
			String extName = dto.getFile().getOriginalFilename().substring(beginIndex);
			fileName += extName;
			
			File f = new File(uploadPath, fileName);
			
			try {
				dto.getFile().transferTo(f);
				
			} catch (IllegalStateException | IOException e) {
				System.out.println("업로드 문제 발생 : " + e);
			}
			dto.setUploadFile(fileName);
		}
		
		dto.setPassword(hash);
		Integer idx = dao.checkPassword(dto);
		if(idx != null) {
			row = dao.modify(dto);
		}
		
		return row;
	}
}











