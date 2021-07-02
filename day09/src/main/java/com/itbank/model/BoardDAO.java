package com.itbank.model;

import java.util.HashMap;
import java.util.List;

public interface BoardDAO {

	List<BoardDTO> selectAll();

	BoardDTO selectOne(int idx);

	int insert(BoardDTO dto);

	int selectMaxIdx();

	int updateViewCount(int idx);

	int deleteBoard(HashMap<String, Object> map);

	Integer checkPassword(BoardDTO dto);

	int modify(BoardDTO dto);

	List<BoardDTO> selectSearch(HashMap<String, String> param);

}
