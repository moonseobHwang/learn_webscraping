package com.mahau.incubate.util;

import java.io.File;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.core.MethodParameter;
import org.springframework.web.bind.support.WebDataBinderFactory;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.method.support.HandlerMethodArgumentResolver;
import org.springframework.web.method.support.ModelAndViewContainer;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

import com.mahau.incubate.model.ParamCollector;

/**
 * Controller 클래스가 로드되기 전 파라미터 값에 따른 파일 업로드를 수행하기 위한 클래스이다.
 * 
 * @param <E>
 */
public class MapFileUploadResolver implements HandlerMethodArgumentResolver {

	@Override
	public boolean supportsParameter(MethodParameter methodParameter) {
		// TODO Auto-generated method stub
		return ParamCollector.class.isAssignableFrom(methodParameter
				.getParameterType());
	}

	@Override
	public Object resolveArgument(MethodParameter methodParameter,
			ModelAndViewContainer mavContainer, NativeWebRequest webRequest,
			WebDataBinderFactory binderFactory) throws Exception {
		Class<?> clazz = methodParameter.getParameterType();
		String paramName = methodParameter.getParameterName();
		ParamCollector requestMap = new ParamCollector();

		if (clazz.equals(ParamCollector.class)
				&& paramName.equals("requestMap")) {

			HttpServletRequest request = webRequest
					.getNativeRequest(HttpServletRequest.class);

			Enumeration<?> enumeration = request.getParameterNames();

			while (enumeration.hasMoreElements()) {
				String key = (String) enumeration.nextElement();
				String[] values = request.getParameterValues(key);
				if (values != null) {
					requestMap.put(key, (values.length > 1) ? values
							: values[0]);
				}
			}

			if (request instanceof MultipartHttpServletRequest) {
				MultipartHttpServletRequest multipartRequest = (MultipartHttpServletRequest) request;
				multipartRequest.getFileNames();
				requestMap.put("fileList", setMultipartList(multipartRequest));
			}
		}

		return requestMap;
	}

	private List<Object> setMultipartList(
			MultipartHttpServletRequest multipartRequest) {
		Map<Object, Object> fileMap = null;
		List<Object> fileList = new ArrayList<Object>();

		int attachFileSize = 0;
		String filePath = "";

		String filePathRoot = "/Users/ohsanghun/Downloads/";
		String filePathSub = "";
		filePath = filePathRoot + filePathSub;

		MultipartFile multiFile = null;

		Iterator<String> multiFileList = multipartRequest.getFileNames();

		while (multiFileList.hasNext()) {
			fileMap = new HashMap<Object, Object>();

			String fileName = multiFileList.next();

			multiFile = multipartRequest.getFile(fileName);

			// limit file size
			if (multiFile.getSize() > attachFileSize) {
				// return UNRESOLVED;
			}

			// original filename (ex. neopets.jpg)
			String originalFileName = multiFile.getOriginalFilename().trim();

			if (originalFileName == "" || originalFileName.isEmpty()) {
				continue;
			}

			// convert original filename with FileUtils.java to virtual
			// filename to upload in ftp
			String multiFileName = null;

			multiFileName = FileUtils.getNewFileName(originalFileName);

			// file 저장경로 + fileName
			String attachFileName = filePath + multiFileName;

			// file size (ex. 1KByte -> 1048)
			String fileSize = multiFile.getSize() + "";

			// get ContentType (ex. jpg(original file type) -> images/JPEG
			// ...)
			String fileContentType = multiFile.getContentType();

			try {
				// file 저장위치에 이동
				multiFile.transferTo(new File(attachFileName));
				fileMap.put("LOGICALFILENAME", originalFileName);
				fileMap.put("PHYSICALFILENAME", multiFileName);
				fileMap.put("FILECONTENTTYPE", fileContentType);
				fileMap.put("FILESIZE", fileSize);
				fileMap.put("PHYSICALFILEDIRECTORY", filePathSub);
				fileMap.put("FILETYPE", fileName); // 멀티업로드시, 파일 구분을위한
				fileMap.put("PHYSICALTHUMBNAILFILENAME", "");
				fileMap.put("PHYSICALTHUMBNAILDIRECTORY", "");

				fileList.add(fileMap);

			} catch (Exception e) {
				File file = new File(attachFileName);
				file.delete();
				e.printStackTrace();
			}
		}
		return fileList;
	}
}
