package com.itbank.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.model.StudentDAO;
import com.itbank.model.StudentDAO2;
import com.itbank.model.StudentDTO;

@Service
public class StudentService {
	
	@Autowired private StudentDAO dao;
	@Autowired private StudentDAO2 dao2;
	
	public List<StudentDTO> selectStudentList() {
		return dao.selectStudentList();
	}

	public List<StudentDTO> selectStudentList2() {
		return dao2.selectStudentList2();
	}

	
}
