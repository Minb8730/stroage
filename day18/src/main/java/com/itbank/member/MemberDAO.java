package com.itbank.member;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

public interface MemberDAO {

	
	@Select("select * from member2 where userid = #{userid}")
	MemberDTO select(String userid);
	
	@Insert("insert into member2 values(#{userid}, #{userpw}, #{username}, #{birth}, #{email}, #{gender}, #{address})")
	int insert(MemberDTO dto);

	@Select("select userid, username, email from member2 order by userid")
	List<HashMap<String, String>> selectList();

	@Delete("delete from member2 where userid = #{userid}")
	int deleteMember(String userid);

	@Update("update member2 set "
			+ "username = #{username}, "
			+ "birth = #{birth}, "
			+ "email = #{email}, "
			+ "gender = #{gender}, "
			+ "address = #{address}"
			+ "where userid = #{userid}")
	int update(MemberDTO dto);

}
