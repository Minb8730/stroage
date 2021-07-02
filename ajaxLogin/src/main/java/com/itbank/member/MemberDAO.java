package com.itbank.member;

import org.apache.ibatis.annotations.Select;

public interface MemberDAO {

	@Select("select * from member2 where userid = #{userid} and userpw = #{userpw}")
	public MemberDTO login(MemberDTO member);

}
