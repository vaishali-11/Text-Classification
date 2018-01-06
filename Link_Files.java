package message;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

public class Link_Files {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String infile1 = "C:\\Users\\Vaishali\\Desktop\\job_classification\\files_content3.csv";
		String infile2 = "C:\\Users\\Vaishali\\Desktop\\job_classification\\candidate_info.csv";
		CSVReader reader = new CSVReader(new FileReader(infile1));
		
		
		String[] cell;
		String outfile = "F:/resume_data/08_new/candidates_info.csv";
		
		while((cell=reader.readNext())!=null){
    
			String job_name = cell[0];
    		String file_name = cell[1];
    		String content = cell[2];
    		//String content1 = cell[3];
    		String[] part = file_name.split("_");
			//int id = NumberUtils.toInt(part[0]);
    		String id = part[0];
			//System.out.println("file1 " + id);
    		String[] cells;
    		CSVReader read = new CSVReader(new FileReader(infile2));
loop1:   		while((cells=read.readNext())!=null) {
    			String id1 = cells[0];
    			String name = cells[1];
    			String email = cells[2];
    			//System.out.println("file2 " + id1);
    			if((id1.equals(id)))
    			{ String[] info = {id1,id,name,email,file_name,job_name,content};//,content1};
    			System.out.println("MATCH FOUND");
    			CSVWriter Writer = new CSVWriter(new FileWriter(outfile,true));
    			Writer.writeNext(info);
			     Writer.close();
    			break loop1;
    			
    			}
    			else {System.out.println("MATCH NOT FOUND");}
    		
    		}read.close();
    		}reader.close();
		}

	}


