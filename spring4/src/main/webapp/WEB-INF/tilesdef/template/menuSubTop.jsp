<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
Menu Sub Top
<sec:authorize access="isAuthenticated()">
	<a href="<c:url value="/logout" />">Log Out</a>
</sec:authorize>
