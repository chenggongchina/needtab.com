package filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public class CharacterEncodingFilter implements Filter {
	
	private String encoding ="utf8";
    private boolean ignore = true;
        
    public void init(FilterConfig filterConfig) throws ServletException {
        
    	String param_encoding = filterConfig.getInitParameter("encoding");
        if (param_encoding != null) {
            encoding =  param_encoding;
        }
        String param_ignore = filterConfig.getInitParameter("ignore");
        if(param_ignore == null){
            this.ignore = true;
        }else if (param_ignore.equalsIgnoreCase("false") || param_ignore.equalsIgnoreCase("no")) {
            this.ignore = false;
        }
	}
    
    public void doFilter(ServletRequest request, ServletResponse response,
    		FilterChain chain) throws IOException, ServletException {
    	
    	if (!ignore || (request.getCharacterEncoding() == null || response.getCharacterEncoding() == null)) {
    		request.setCharacterEncoding(this.encoding);
    		response.setCharacterEncoding(this.encoding);
    	}
   	
    	chain.doFilter(request, response);
    }

    public void destroy(){
    }

}
