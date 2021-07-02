package com.itbank.service;


import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.model.Board2DAO;
import com.itbank.model.Board2DTO;

@Service
public class Board2Service {

	@Autowired Board2DAO dao;

	public List<Board2DTO> selectAll(HashMap<String, String> param) {
		return dao.selectAll(param);
	}

	public int selectBoardCount(HashMap<String, String> param) {
		return dao.selectBoardCount(param);
	}

	public Board2DTO selectOne(int idx) {
		return dao.selectOne(idx);
	}

	public int updateViewCount(int idx) {
		return dao.updateViewCount(idx);
	}
	

}
