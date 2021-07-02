package com.itbank.model;

import java.util.HashMap;
import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;


@Repository
public class TestDAO {

	@Autowired private SqlSessionTemplate sst;

	public List<String> getTest() {
		List<String> list = sst.selectList("test");
		
//		String statement = null;
		
//		sst.selectOne("mapper 내부 sql의 이름"); 					// 단일 객체 반환(DTO 사용 가능)
//		sst.selectList(statement);								// 다수 객체를 리스트로 반환
//		sst.selectMap(statement, null);							// Map형식 반환
//		sst.insert(statement, new Object());					// 매개변수로 아무 객체나 받을 수 있음
//		sst.update(statement, new HashMap<String, Object>());	// 매개변수 Map으로 전달 가능
//		sst.delete(statement,1);								// 매개변수 primitive도 가능
		return list;
	}


}
