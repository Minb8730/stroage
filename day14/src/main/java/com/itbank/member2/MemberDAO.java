package com.itbank.member2;

public interface MemberDAO {

	int insert(MemberDTO dto);

	MemberDTO login(MemberDTO dto);

	int delete(MemberDTO login);

	int exist(String id);

}
