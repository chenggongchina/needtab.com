<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<HTML>
<META content="text/html; charset=utf-8" http-equiv=Content-Type>
<HEAD>
<title>找谱网 - 最新最全的专业吉他谱搜索</title>
<meta name="description" content="找谱网是更新最快的吉他谱搜索引擎，其聚合全网曲谱资源。用户体验超赞！找谱网及时为您更新曲谱，保证曲谱来源最全，是数千万网民搜谱首选。找谱网收录了来自各个主流曲谱网站的最新资源。needtab.com" />
<meta name="keywords" content="找谱网,找谱,吉他谱,吉他,曲谱,指弹" />
<meta name="copyright" content="needtab.com" />
<meta name="author" content="needtab Team" />
<meta name="robots" content="all" />
<meta name="revisit-after" content="1 days" />
<link href="css/topsearch.css" rel="stylesheet" type="text/css">
</HEAD>

<%@ page contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
<%@ page import="com.needtab.searcher.*" %>
<%@ page import="com.needtab.history.*" %>
<%@ page import="java.util.List" %>
<%
	String path = request.getContextPath();
	String keyword= request.getParameter("Keyword");
	History.Insert(keyword,request.getRemoteAddr());
	List<ResultTip> rst = Searcher.searcher(keyword);
	int count = 0;
%>

<body >

<table width="100%" align="center" background="pics/bar.gif">
<form name=mainform method="get" action="search.jsp" >
	
	<tr>
		<td valign=bottom>
			<br><br><br><br><br><br><br><br><br><br>
				<input class="SEARCHTEXT" type=text name="Keyword" style="width: 325px" value="<%=keyword %>">
				<input class="SEARCHBUTTON" type="submit" value="我要找谱" >
			<br><br>
		</td>
	</tr>

	<tr>
		<td nowrap class="NORMALTEXT" align="left">
			关键字:<%=keyword %>
			结果总数:<%=rst.size() %>
		</td>
	</tr>
</form>
</table>


<table border=0 align=center valign=top width="95%">
	
	<tr>
	<%for(ResultTip t:rst){ %>
			<td border = 0 width="20%" height=80 align=left valign=top class="NORMALTEXT" onmouseover="this.style.backgroundColor='#ffffdc'" onmouseout="this.style.backgroundColor='#f0f0dc'">
			<a href="<%=t.getUrl() %>" title="<%=t.getTitle() %>" target=_blank class="style1">
			  <%=t.getPic() %>
			  <%=t.getTitle()%><br>
			</a>
			  <%=t.getArtist()%>
			  @ <%=t.getNetwork() %><br>
			</td>
	<% count++;if(count%5==0) out.print("</tr><tr>");}%>
	</tr>
	
	<tr>
	<td colspan=5>
	</td>
	</tr>
	
	<tr>
	<td colspan=5" align="center">
		<p><a href="index.html" class="style1">Needtab.com</a> | <a href="about.html" class="style1">关于找谱网</a> | <a href="copyright.html" class="style1">版权申明</a> | <a href="mailto:needtab@gmail.com" class="style1">联系我们</a></p>
	</td>
	</tr>
</table>

</body>