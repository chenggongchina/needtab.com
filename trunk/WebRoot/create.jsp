<%@ page contentType="text/html; charset=utf8" pageEncoding="utf8"%>
<%@ page import="com.needtab.indexer.*" %>
<%
		try{
			IndexCreator c = new IndexCreator();
			c.Create();
		}
		catch(Exception e){
			e.printStackTrace();
		}
		out.println("finished");
%>
