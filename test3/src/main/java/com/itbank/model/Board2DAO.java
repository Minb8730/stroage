package com.itbank.model;

import java.util.HashMap;
import java.util.List;

public interface Board2DAO {

	List<Board2DTO> selectAll(HashMap<String, String> param);

	int selectBoardCount(HashMap<String, String> param);

	Board2DTO selectOne(int idx);

	int updateViewCount(int idx);



	
	
}
