package com.itbank.model;

import java.util.HashMap;
import java.util.List;

public interface BoardDAO {

	List<BoardDTO> selectAll(HashMap<String, String> param);

	BoardDTO selectOne(int idx);

	int insert(BoardDTO dto);

	int selectMaxIdx();

	int updateViewCount(int idx);

	int deleteBoard(HashMap<String, Object> map);

	Integer checkPassword(BoardDTO dto);

	int modify(BoardDTO dto);

	int selectBoardCount(HashMap<String, String> param);

	List<ReplyDTO> selectReplyList(int idx);

	int insertReply(ReplyDTO dto);

}
