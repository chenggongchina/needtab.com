package com.needtab.db;

import java.sql.Connection;
import java.sql.DriverManager;

public class DbManager {
	
	private static String userName = "root";  
    private static String password = "123456";  
    private static String databaseIP = "127.0.0.1";  
    private static String databaseName = "tabs"; 
    
	static public Connection getConnect(){
		Connection conn = null;  
		try{
			String url = "jdbc:mysql://"+ databaseIP + "/" + databaseName + "?characterEncoding=gbk";  
			Class.forName ("com.mysql.jdbc.Driver").newInstance(); 
			conn = DriverManager.getConnection (url, userName, password);  
		}
		catch(Exception e){
			e.printStackTrace();  
		}
		return conn;
	}
}
