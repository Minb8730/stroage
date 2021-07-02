package com.itbank.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.model.BoardDAO;
import com.itbank.model.BoardDTO;

@Service
public class BoardService {
	
	@Autowired private BoardDAO dao;

	public List<BoardDTO> selectAll() {
		return dao.selectAll();
	}

	public int insert(BoardDTO dto) {
		return dao.insert(dto);
	}

	public int delete(int idx) {
		return dao.delete(idx);
	}

	public BoardDTO selectOne(int idx) {
		BoardDTO dto = dao.selectOne(idx);
		dto.setViewCount(dto.getViewCount() + 1);

		return dto;
	}

	public int update(int idx, String content) {
		return dao.update(idx, content);
	}
	
	

}
