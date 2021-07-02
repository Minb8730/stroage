package com.itbank.model;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class StudentDAO {

	@Autowired private SqlSessionTemplate sst;

	public List<StudentDTO> selectStudentList() {

		return sst.selectList("studentList");
	}
	
	
	
}
