<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
	<img src=<c:url value="/upload/${resultMap.PHYSICALFILENAME}" /> />
	<br /> <spring:message code="label.book.bookname" /> :
	<c:out value="${resultMap.BOOKNAME}" />
	<br /> <spring:message code="label.book.publisher" /> :
	<c:out value="${resultMap.PUBLISHER}" />
	<br /> <spring:message code="label.book.author" /> :
	<c:out value="${resultMap.AUTHOR}" />
	<br /> <spring:message code="label.book.bookinformation" /> : 
	<pre>${resultMap.BOOKINFORMATION}</pre>
	<a href="<c:url value='/book/edit' />">
				Book Edit</a>
</body>
</html>