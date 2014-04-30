package com.needtab.history;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import com.needtab.db.DbManager;

public class History {
	
	static public void Insert(String keyword,String ip) throws UnsupportedEncodingException{
		Date date=new Date();
		String dt = new String(new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(date));
		
		String sql = "insert into search_history values(null,'"+keyword+"','"+ip+"','"+dt+"')";
		Connection conn = DbManager.getConnect();
		PreparedStatement pstmt = null;
		try {
			pstmt = conn.prepareStatement(sql);
			pstmt.execute();
			pstmt.close();
			conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
	}
	
	static public List<HisTip> Query() throws Exception{
		List<HisTip> rst = new ArrayList<HisTip>();
		String sql = "select * from search_history order by create_time desc";
		Connection conn = DbManager.getConnect();
		PreparedStatement pstmt = conn.prepareStatement(sql); 
		ResultSet rset=pstmt.executeQuery();  
		while(rset.next()){
			HisTip tip = new HisTip();
			tip.setIp(rset.getString("ip"));
			tip.setKeyword(rset.getString("keyword"));
			tip.setTime(rset.getString("create_time"));
			rst.add(tip);
		}
		conn.close();
		pstmt.close();
		rset.close();
		return rst;
	}
	
	static public void main(String[] argvs) throws Exception{
		//History.Insert("test", "test");
		List<HisTip> t = (Query());
		for(HisTip s : t){
			System.out.println(s.getIp());
			System.out.println(s.getTime());
			System.out.println(s.getKeyword());
		}
	}
}
