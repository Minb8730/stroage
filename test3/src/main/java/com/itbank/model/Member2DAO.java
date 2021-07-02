package com.itbank.model;

import java.util.HashMap;

public interface Member2DAO {

	Member2DTO login(Member2DTO inputData);

	int insert(Member2DTO dto);

	Member2DTO selectOne(String userId);

	int updateMember(Member2DTO dto);

	int delete(String userId);

	int updatePassword(Member2DTO dto);

}
