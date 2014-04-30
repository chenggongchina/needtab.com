<%@ page contentType="text/html; charset=utf8" pageEncoding="utf8"%>
<%@ page import="com.needtab.history.*" %>
<%@ page import="java.util.List" %>
<%
	List<HisTip> rst = History.Query();
	int count = 0;
%>
<table border=5>
<tr><td>关键字</td><td>IP</td><td>搜索时间</td></tr>
<%
	for(HisTip t:rst){
		out.println("<tr><td>"+t.getKeyword()+"</td><td>"+t.getIp()+"</td><td>"+t.getTime()+"</td></tr>");
	}
%>
</table>

