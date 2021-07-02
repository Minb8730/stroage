package com.itbank.model;

import java.sql.ResultSet;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;


@Repository //- 데이터 저장소에 접근하는 클래스
public class TestDAO {

	@Autowired
	private JdbcTemplate jt; // (dataSource를 통해)Connection, Statement, executeQuery 등의 일련의 과정을 자동으로 처리해줌, 여러개로 결과가 나오면 자동으로 List로 반환해줌
	
	/*
	 * private void practice() { String sql =""; jt.query(sql, rowMapper); // SQL을
	 * 실행하고 rowMapper의 내용대로 객체를 반환 jt.queryForObject(sql, rowMapper); // 단일 객체 하나만을
	 * 반환할 때 jt.update(sql, args); // insert, update, delete 사용하여 int를 반환 //args는
	 * 가변인자
	 * 
	 * // ps.excuteQuery(); // select // ps.excuteQueryUpdate(); // insert, update,
	 * delete
	 * 
	 * }
	 */	
	public List<String> test(){
		String sql="select * from v$version";
		// 어떤 SQL을 실행할지?
		
		RowMapper<String> mapper = (ResultSet rs, int rowNum)-> { // DB에서 select 쿼리를 수행할때 한 줄에 대해서 어떻게 처리를 할것인가에 대한 서술하는 객체
			return rs.getString(1); 
		}; // 결과를 어떤 형식으로 처리할지?(HashMap에 담을지, List에 담을지, DTO에 담을지, 첫번째 값을 그대로 반환할지 등등)
		return jt.query(sql, mapper);  // mapper 한 객체를 sql 문을 적용시켜 넘겨주겠다.
		// 어떤 쿼리문을 수행하며, 어떻게 객체로 맵핑할지 전달하면 jdbcTemlpate가 이 쿼리를 수행하여 결과를 반환한다.
	}
	
	public List<String> time(){
		String sql = "select to_char(sysdate, 'yyyy-mm-dd hh24:mi') as time from dual";
		
		RowMapper<String> mapper = (ResultSet rs, int rowNum)->{
			return rs.getString(1);
		};
		return jt.query(sql, mapper);
	}
	
	public String getTime() {
		String sql = "select to_char(sysdate, 'yyyy-mm-dd hh24:mi') as time from dual";
		RowMapper<String> mapper = (ResultSet rs, int rowNum)->{
			String time = rs.getString("time");
			return time;
		};
		return jt.queryForObject(sql, mapper); // 시간을 가져오는 쿼리는 단일 객체를 반환하기 때문에 
	}											// 단일 객체를 받는 queryForObject 사용
	


	
}
