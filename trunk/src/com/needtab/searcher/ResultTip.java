package com.needtab.searcher;

public class ResultTip {

	static public String getNetworkById(int id){
		switch(id){
		case 1:
			return "吉他谱";
		case 2:
			return "虫虫吉他";
		case 3:
			return "52吉他";
		case 4:
			return "GTPCN";
		case 5:
			return "缘分66";
		default:
			return "未知";
		}
	}
	
	static public String getPicByType(int type){
		switch(type){
		case 1:
			return "<img src='pics/txt.jpg' width=30 height=30/>";
		case 2:
			return "<img src='pics/image.jpg' width=30 height=30/>";
		case 3:
			return "<img src='pics/gtp.jpg' width=30 height=30/>";
		default:
			return "error";
		}
	}
	
	String title;
	String artist;
	String network;
	int type;
	String url;
	
	/**
	 * @return the title
	 */
	public String getTitle() {
		return title;
	}
	/**
	 * @param title the title to set
	 */
	public void setTitle(String title) {
		this.title = title;
	}
	/**
	 * @return the artist
	 */
	public String getArtist() {
		return artist;
	}
	/**
	 * @param artist the artist to set
	 */
	public void setArtist(String artist) {
		this.artist = artist;
	}
	/**
	 * @return the network
	 */
	public String getNetwork() {
		return network;
	}
	/**
	 * @param network the network to set
	 */
	public void setNetwork(String network) {
		this.network = network;
	}
	/**
	 * @return the type
	 */
	public String getPic() {
		return getPicByType(type);
	}
	/**
	 * @param type the type to set
	 */
	public void setType(int type) {
		this.type = type;
	}
	/**
	 * @return the url
	 */
	public String getUrl() {
		return url;
	}
	/**
	 * @param url the url to set
	 */
	public void setUrl(String url) {
		this.url = url;
	}

	public String toString()
	{
		return title+"-"+artist+"-"+url;
	}
}
