package com.mahau.incubate.service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.springframework.stereotype.Component;

@Component
public class CrawlService {
	
	public Object processPage(Map<?, ?> paramObject) throws IOException {

		
		List<Object> result = new ArrayList<Object>();

		//get useful information
		Document doc = Jsoup.connect("http://www.mit.edu/").get();

		//get all links and recursively call the processPage method
		Elements questions = doc.select("a[href]");
		for(Element link: questions){
			if(link.attr("href").contains("mit.edu"))
				result.add(link.attr("abs:href"));
		}
		return result;
	}

}
