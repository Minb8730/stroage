package com.itbank.board2;

import java.util.List;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;

public interface BoardDAO {

	@Select("select * from board2 order by idx desc")
	List<BoardDTO> selectAll();

	@Select("select * from board2 where idx = #{idx}")
	BoardDTO select(int idx);

	@Insert("insert into board2 values "
			+ "("
			+ "	board2_seq.nextval, "
			+ "	#{title}, "
			+ "	#{writer}, "
			+ "	#{content}, "
			+ "	#{uploadFile}, "
			+ "	0, "
			+ "	to_char(sysdate, 'yyyy-MM-dd')"
			+ ")")
	int insert(BoardDTO dto);
	
	
	
}
