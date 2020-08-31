<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<html>
<head>
<title>Home</title>
</head>
<body>
	<h1>
		<spring:message code="header.welcome" />
	</h1>

	<small>
		<spring:message code="label.multilang" />
		: <a href="?defaultlang=en">english</a> | <a href="?defaultlang=kr">kr</a>
	</small>

	<P>The time on the server is ${serverTime}.</P>

	<ul>
		<li><a href="<c:url value="/member/edit" />"> Member Edit </a></li>
	</ul>
	<ul>
		<li><a href="<c:url value="/book/edit" />"> BOOK Edit </a></li>
	</ul>
	<ul>
		<li><a href="<c:url value="/mail/send" />"> Mail Send </a></li>
	</ul>
	<ul>
		<li><a href="<c:url value="/crawl/list" />"> Crawl Send </a></li>
	</ul>

</body>
</html>
