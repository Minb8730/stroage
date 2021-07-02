package com.itbank.model;

import java.util.List;

public interface BoardDAO {

	List<BoardDTO> selectAll();

	int insert(BoardDTO dto);

	int delete(int idx);

	BoardDTO selectOne(int idx);

	int update(int idx, String content);

}
