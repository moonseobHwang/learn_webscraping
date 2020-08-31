<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<!-- %@ taglib prefix="nav" uri="/pNavi-tags"% -->

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<script type="text/javascript"
	src="<c:url value='/resources/js/jquery-1.11.3.min.js' />"></script>
<script src="<c:url value="/resources/js/jscommon.js" />"
	type="text/javascript"></script>

</head>
<body>
	<table>
		<tr>
			<td>
				<table border=1>
					<thead>
						<tr>
							<th>LinkURL</th>
						</tr>
					</thead>
					<tbody>
						<c:forEach items="${resultList}" var="resultData">
							<tr>
								<td>${resultData}</td>
							</tr>
						</c:forEach>
					</tbody>
				</table>
			</td>
		</tr>
	</table>
</body>
</html>