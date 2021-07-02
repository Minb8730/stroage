package com.itbank.service;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.board2.BoardDAO;
import com.itbank.board2.BoardDTO;

@Service
public class BoardService {

	@Autowired private BoardDAO dao;
	
	private final String uploadPath = "D:\\upload";

	public List<BoardDTO> selectAll() {
		return dao.selectAll();
	}

	public BoardDTO select(int idx) {
		return dao.select(idx);
	}

	public int insert(BoardDTO dto) {
		
		dto.setUploadFile("default.jpg");
		
		if(dto.getFile().getOriginalFilename().equals("") == false) {
			// 파일이 포함되었다면 수행할 코드
			File target = new File(uploadPath, dto.getFile().getOriginalFilename());
			File dir = new File(uploadPath);
			dir.mkdirs();
			try {
				dto.getFile().transferTo(target);
			} catch (IllegalStateException | IOException e) {
				e.printStackTrace();
			}
			dto.setUploadFile(dto.getFile().getOriginalFilename());
		}
		
		return dao.insert(dto);
	}
	
}
