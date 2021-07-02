package day02;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;


public class TestDAO {
	private DataSource ds;
	private Connection con;
	private PreparedStatement ps;
	private ResultSet rs;
	private Context init;
	private static final TestDAO instance = new TestDAO();
	
	public static TestDAO getInstance() {
		return instance;
	}
	
	private TestDAO() {
		System.out.println("testDAO 생성자 호출!!");
		try {
			init = new InitialContext();
			ds = (DataSource) init.lookup("java:comp/env/jdbc/oracle");
		}catch(NamingException e) {
			System.out.println("생성자 예외 발생 : " + e);
		}
	}
	
	public String test() throws Exception{
		String sql = "select * from v$version";
		con = ds.getConnection();
		ps = con.prepareStatement(sql);
		rs = ps.executeQuery();
		if(rs.next()) {
			return rs.getString(1);
		}
		return null;
	}
	
	// 게시글의 목록을 불러와서 리스트 형태로 반환하는 메서드
	public HashMap<String, Object> selectList(int page){
		return null;
	}
	
	// 조건을 전달받아서, 조건에 맞는 리스트를 반환하는 메서드
	public HashMap<String, Object> selectList(int page, String type, String word){
		return null;
	}
	
	// idx로 글을 하나불러오는 메서드
	public BoardDTO selectOne(int idx) {
		return null;
	}
	
	// dot를 전달받아서 삭제 처리(update)하는 메서드
	
	public List<BoardDTO> selectList(){
		ArrayList<BoardDTO> list = null;
		String sql = "select * from board order by idx desc";
		try {
			con = ds.getConnection();
			ps = con.prepareStatement(sql);
			rs = ps.executeQuery();
			list = new ArrayList<BoardDTO>();
			while(rs.next()) {
				BoardDTO dto = new BoardDTO();
				dto.setContent(rs.getString("content"));
				dto.setIdx(rs.getInt("idx"));
				dto.setIpaddr(rs.getString("ipaddr"));
				dto.setTitle(rs.getString("tilte"));
				dto.setVcnt(rs.getInt("vcnt"));
				dto.setWdate(rs.getString("wdate"));
				dto.setWriter(rs.getString("writer"));
				list.add(dto);
			}
		} catch (SQLException e) {
			System.out.println("SelectList : " + e);
		}finally {
			try {
				if(rs != null) rs.close();
				if(ps != null) ps.close();
				if(con != null) con.close();
			}catch(Exception e){
			}
		}
		
		return list;
	}
	
	public void insertList() {
		String sql = "insert into board(idx, title, writer, content, vcnt, ipaddr) values (board_seq.nextval, ?, ?, ?, ?, ?)"; 
		try {
			con = ds.getConnection();
			ps = con.prepareStatement(sql);
			ps.setString(1, "title");
			ps.setString(2, "writer");
			ps.setString(3, "content");
			ps.setString(4, "vcnt");
			ps.setString(5, "ipaddr");
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	
	public boolean deleteList() {
		String sql = "delete from board where idx = ?";
		try {
			con = ds.getConnection();
			ps = con.prepareStatement(sql);
			ps.setString(1, "idx");
			int result = ps.executeUpdate();
			if(result == 1) {
				return true;
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return false;
	}
	
	public void updateList() {
		
	}
	
	
	
	
	
}
