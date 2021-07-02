package com.itbank.service;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.model.SnackDTO;
import com.itbank.model.SnackbarDAO;

@Service
public class SnackbarService {

	// service는 DAO를 참조하게 한다.
	@Autowired
	private SnackbarDAO dao;

	public List<SnackDTO> getSnackList(){
		return dao.selectList();
	}

	public int insertSnack(SnackDTO dto) {
		return dao.insertSnack(dto);
	}

	public SnackDTO selectOne(int idx) {
		return dao.selectOne(idx);
	}

	public int update(SnackDTO dto) {
		return dao.update(dto);
	}

	public int delete(int idx) {
		return dao.delete(idx);
	}
	
	
	
	
}
