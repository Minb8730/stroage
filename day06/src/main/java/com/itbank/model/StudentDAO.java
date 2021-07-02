package com.itbank.model;

import java.sql.ResultSet;
import java.util.HashMap;
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

	public int delete(String id) {
		String sql = "delete student where id=?";
		int row = jt.update(sql, id);
		return row;
	}

	public HashMap<String, Object> selectPayInfo(int idx) {
		String sql = "select due, sfund, payment, status, (due - sfund) as need"
				+ " from student where idx=?";
		
		HashMap<String, Object> map = new HashMap<String, Object>(jt.queryForMap(sql, idx));
		// 대부분의 컬렉션 생성자는 다른 컬렉션을 매개변수로 받을 수 있다.
		
		System.out.println(map);
		// hashmap 으로 받으면 toString 을 받을 필요 없이 syso 를 통해 값을 알아볼 수 있다. 그리고 json으로 변환 할 때도 용이하다.
		
		return map;
	}

	public int updatePayment(HashMap<String, Object> param) {
		String sql ="update student" + 
				"    set " + 
				"		payment = payment + ?, " + 
				"        status=  " + 
				"            case " + 
				"                when(due-sfund = payment + ?) then '완료' " + 
				"                when(due-sfund < payment + ?) then '초과' " + 
				"                else '미납'" + 
				"            end" + 
				"		where idx= ?";
		int row = jt.update(sql, 
				param.get("payment"), 
				param.get("payment"), 
				param.get("payment"), 
				param.get("idx") );
		return row;
	}

	public StudentDTO selectOne(String id) {
		String sql = "select * from student where id =?";
		
		RowMapper<StudentDTO> rowMapper = (ResultSet rs, int row) ->{
			StudentDTO dto = new StudentDTO();
			dto.setBirth(rs.getString("birth"));
			dto.setId(rs.getString("id"));
			dto.setIdx(rs.getInt("idx"));
			dto.setName(rs.getString("name"));
			dto.setPhone(rs.getString("phone"));
//			dto.setPw(rs.getString("pw"));	 // 비밀번호 변경은 나중에 따로 빼내서 구현
			dto.setRdate(rs.getString("rdate"));
			dto.setStype(rs.getString("stype"));
			return dto;
		};
		Object[] args = { id };
		
		return jt.queryForObject(sql, args, rowMapper);
	}

	public int updateInfo(StudentDTO dto) {
		String sql = "update student set name=?, phone=?, birth=? where id=?";
		int row = jt.update(sql, dto.getName(), dto.getPhone(), dto.getBirth(), dto.getId());
		return row;
	}

}
