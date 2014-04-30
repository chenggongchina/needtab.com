package com.needtab.indexer;

import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.wltea.analyzer.lucene.IKAnalyzer;

import com.needtab.db.DbManager;

public class IndexCreator {

	private Connection conn = null;  
	
	private static int BLOCKSIZE = 1000;
	
	public void Create() throws Exception{
		System.out.println("indexing data");
		Directory indexDir = FSDirectory.open(new File("E:\\lucene\\index")); 
		Analyzer luceneAnalyzer = new IKAnalyzer();  
		IndexWriter indexWriter = new IndexWriter(indexDir, luceneAnalyzer,  
	            true, IndexWriter.MaxFieldLength.LIMITED); 
		int page = 0;
		while(true){
			Connection conn = DbManager.getConnect();
			String sql = "select * from tab limit "+page*BLOCKSIZE+","+BLOCKSIZE;
			PreparedStatement pstmt = conn.prepareStatement(sql); 
			ResultSet rset=pstmt.executeQuery();  
			boolean existFlag = false;
			while(rset.next()){
				existFlag = true;
				String title = rset.getString("title");
				String artist = rset.getString("artist");
				String ref_url = rset.getString("ref_url");
				String network = rset.getString("network");
				String type = rset.getString("type");
				//System.out.println(title+"-"+artist+"-"+ref_url);
				Document document = new Document();
				Field fieldTitle = new Field("title", title, Field.Store.YES,  
	                    Field.Index.ANALYZED,  
	                    Field.TermVector.WITH_POSITIONS_OFFSETS); 
				Field fieldArtist = new Field("artist", artist, Field.Store.YES,  
	                    Field.Index.ANALYZED,  
	                    Field.TermVector.WITH_POSITIONS_OFFSETS);				
				Field fieldRefUrl = new Field("ref_url", ref_url,  
                        Field.Store.YES, Field.Index.NO); 
				Field filedNetwork = new Field("network", network,  
                        Field.Store.YES, Field.Index.NO); 
				Field fieldType = new Field("type", type,  
                        Field.Store.YES, Field.Index.NO); 
				document.add(fieldTitle);  
	            document.add(fieldArtist);
	            document.add(fieldRefUrl);
	            document.add(filedNetwork);
	            document.add(fieldType);
	            indexWriter.addDocument(document);
			}
			if( !existFlag )
				break;
			page++;
			rset.close();
			pstmt.close();
			conn.close();
		}
		indexWriter.close();
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try{
			IndexCreator c = new IndexCreator();
			c.Create();
		}
		catch(Exception e){
			e.printStackTrace();
		}
		System.out.println("finished");
	}

	
	
}
