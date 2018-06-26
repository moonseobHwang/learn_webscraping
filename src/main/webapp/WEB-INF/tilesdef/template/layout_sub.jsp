<%@ taglib uri="http://tiles.apache.org/tags-tiles" prefix="tiles"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title><tiles:getAsString name="title" /></title>
</head>
<body>
	<table border='1'>
		<tr>
			<th colspan=2>
				<tiles:insertAttribute name="menuTop" />
			</th>
		</tr>
		<tr>
			<td>
				<tiles:insertAttribute name="menuRight" />
			</td>
			<td>
				<tiles:insertAttribute name="body" />
			</td>
		</tr>
	</table>
</body>
</html>
