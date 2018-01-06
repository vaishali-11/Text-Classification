package message;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import org.apache.commons.io.FileUtils;
import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

public class File_sep {

	public static void main(String[] args) throws IOException {
				
		String CSV_file = "C:\\Users\\Vaishali\\Desktop\\job_classification\\file_info3.csv";
		CSVReader reader = new CSVReader(new FileReader(CSV_file));
		String[] cell;
		String err_file = "F:/resume_data/08_new/files_error.csv";
		
		while((cell=reader.readNext())!=null){
    		String job_name = cell[0];
    		String file_name = cell[1];
    		if (new File("F:/resume_data/08_new/" + job_name).exists()) {
    		System.out.println("Folder exists");
    		 			
    		}
    		else {
    			
    			File  f = new File("F:/resume_data/08_new/" + job_name);
        		System.out.println(f.mkdir());
        		System.out.println("folder created");
    		}
    					
    			File source = new File("C:\\Users\\Vaishali\\Desktop\\text_08_all\\" + file_name);
    			File dest = new File("F:/resume_data/08_new/" + job_name);
    		
    			try {
    			    FileUtils.copyFileToDirectory(source, dest);
    			} catch (IOException e) {
    			     System.out.println("FILE NOT FOUND" + file_name);
    			     CSVWriter Writer = new CSVWriter(new FileWriter(err_file));
    			     String[] info = {job_name,file_name};
    			     Writer.writeNext(info);
    			     Writer.close();
    			     e.printStackTrace();
    			     }
    		
    			
    			
    		}
		
		
		reader.close();
	}

}
