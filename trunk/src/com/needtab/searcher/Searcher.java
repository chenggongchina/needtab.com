package com.needtab.searcher;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.lucene.document.Document;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.wltea.analyzer.lucene.IKQueryParser;
import org.wltea.analyzer.lucene.IKSimilarity;

public class Searcher {
	
	    public static List<ResultTip> searcher(String keyword) {  
	    	File indexDir = new File("E:\\lucene\\index");  
	    	List<ResultTip> rst = new ArrayList<ResultTip>();
	        IndexSearcher isearcher = null;  
	        Directory directory = null;  
	        try {   
	            directory = FSDirectory.open(indexDir);  
	            String[] fileds = {"title","artist"};
	            
	            Query query = IKQueryParser.parseMultiField(fileds,keyword);
	            isearcher = new IndexSearcher(directory, true); 
	            isearcher.setSimilarity(new IKSimilarity());
	            TopDocs ts = isearcher.search(query, 1000);  
	            int totalHits = ts.totalHits; 
	            ScoreDoc[] hits = ts.scoreDocs;  
	            for (int i = 0; i < hits.length; i++) {  
	                Document hitDoc = isearcher.doc(hits[i].doc);   
	                String title = (hitDoc.getField("title").stringValue());  
	                String artist = (hitDoc.getField("artist").stringValue()); 
	                String ref_url = (hitDoc.getField("ref_url").stringValue());
	                int network = Integer.parseInt((hitDoc.getField("network").stringValue()));
	                int type = Integer.parseInt((hitDoc.getField("type").stringValue()));
	                //System.out.println(title + "-" + artist + "-" + ref_url);
	                ResultTip tip = new ResultTip();
	                tip.setArtist(artist);
	                tip.setTitle(title);
	                tip.setUrl(ref_url);
	                tip.setType(type);
	                tip.setNetwork(ResultTip.getNetworkById(network));
	                
	                rst.add(tip);
	            }  
	              
	        } catch (IOException e) {  
	            e.printStackTrace();  
	        } finally {  
	            if (isearcher != null) {  
	                try {  
	                    isearcher.close(); 
	                } catch (IOException e) {  
	                    e.printStackTrace();  
	                }  
	            }  
	            if (directory != null) {  
	                try {  
	                    directory.close(); 
	                } catch (IOException e) {  
	                    e.printStackTrace();  
	                }  
	            }  
	        }  
	        return rst;
	    }  
	  
	    public static void main(String[] args) {  
	        //CreateIndexerDir.index(src, destDir);  
	        searcher("test");
	    }  
}
