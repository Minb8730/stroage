package com.itbank.model;

import java.sql.ResultSet;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

@Repository
public class SnackbarDAO {

	@Autowired
	private JdbcTemplate jt;
	

	public List<SnackDTO> selectList() {
		String sql = "select * from snackbar order by idx";
		
		RowMapper<SnackDTO> mapper = (ResultSet rs, int rowNum)->{
			SnackDTO dto = new SnackDTO();
			dto.setCnt(rs.getInt("cnt"));
			dto.setIdx(rs.getInt("idx"));
			dto.setName(rs.getString("name"));
			dto.setPrice(rs.getInt("price"));
			return dto;
		};
		return jt.query(sql, mapper);
	}


	public int insertSnack(SnackDTO dto) {	// update, delete 도 동일한 방식으로 사용하면 된다. primitive 로 받지 말고 hashmap 이나 dto와 같은 방식으로 받도록 연습
		String sql = "insert into snackbar values(snackbar_seq.nextval, ?, ?, ?) ";
		int row= jt.update(sql, dto.getName(), dto.getPrice(), 0);
		return row;
	}


	public SnackDTO selectOne(int idx) {
		String sql = "select * from snackbar where idx =" + idx;
		
		RowMapper<SnackDTO> mapper = (ResultSet rs, int rowNum)->{
			SnackDTO dto = new SnackDTO();
			dto.setCnt(rs.getInt("cnt"));
			dto.setIdx(rs.getInt("idx"));
			dto.setName(rs.getString("name"));
			dto.setPrice(rs.getInt("price"));
			return dto;
		};
		return jt.queryForObject(sql, mapper);
	}


	public int update(SnackDTO dto) {
		String sql = "update snackbar set name=?, price=?, cnt=? where idx=?";
		return jt.update(sql, dto.getName(), dto.getPrice(), dto.getCnt(), dto.getIdx());
	}


	public int delete(int idx) {
		String sql = "delete snackbar where idx = ?";
		return jt.update(sql, idx);
	}
	
	
	
}
