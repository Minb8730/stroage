package com.itbank.model;

import java.sql.ResultSet;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

@Repository
public class StudentDAO {

	@Autowired
	private JdbcTemplate jt; // Connection -> DataSource -> JdbcTemlate
	
	public List<StudentDTO> selectAll() {
		String sql = "select * from student";
		
		RowMapper<StudentDTO> rowMapper = (ResultSet rs, int row) ->{
			StudentDTO dto = new StudentDTO();
			dto.setBirth(rs.getString("birth"));
			dto.setDue(rs.getInt("due"));
			dto.setId(rs.getString("id"));
			dto.setIdx(rs.getInt("idx"));
			dto.setName(rs.getString("name"));
			dto.setPayment(rs.getInt("payment"));
			dto.setPhone(rs.getString("phone"));
			dto.setPw(rs.getString("pw"));
			dto.setRdate(rs.getString("rdate"));
			dto.setSfund(rs.getInt("sfund"));
			dto.setStatus(rs.getString("status"));
			dto.setStype(rs.getString("stype"));
			return dto;
		};
		return jt.query(sql, rowMapper);
	}

	public int insert(StudentDTO dto) throws DataAccessException 
	{		// 무결성 에러에 대한 예외 처리, pk나 uk가 중복될 경우 발생 ss 로 넘겨준후 ss는 controller로 넘겨주어서 예외처리를 한번에 한다.
		String sql = "insert into student(idx, stype, id, pw, name, phone, birth, due, sfund)"
				+ "values(student_seq.nextval, ?, ?, ?, ?, ?, ?, ?, ?)";
		int row = jt.update(sql , dto.getStype(), dto.getId(), dto.getPw(), dto.getName(), dto.getPhone(), dto.getBirth(), dto.getDue(), dto.getSfund());
		return row;
	}


	
	public StudentDTO selectOne(StudentDTO inputData) {
		String sql="select * from student where id =? and pw = ?";
		
		RowMapper<StudentDTO> rowMapper = (ResultSet rs, int row) ->{
			StudentDTO dto = new StudentDTO();
			dto.setBirth(rs.getString("birth"));
			dto.setDue(rs.getInt("due"));
			dto.setId(rs.getString("id"));
			dto.setIdx(rs.getInt("idx"));
			dto.setName(rs.getString("name"));
			dto.setPayment(rs.getInt("payment"));
			dto.setPhone(rs.getString("phone"));
			dto.setPw(rs.getString("pw"));
			dto.setRdate(rs.getString("rdate"));
			dto.setSfund(rs.getInt("sfund"));
			dto.setStatus(rs.getString("status"));
			dto.setStype(rs.getString("stype"));
			return dto;
		};
		Object[] args = {inputData.getId(), inputData.getPw()};
		
		return jt.queryForObject(sql, args, rowMapper);
	}

}
