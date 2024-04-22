package database;


import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;
import java.sql.Blob;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;



public class SimpleLogIn {

	static final String JDBC_URL = "jdbc:mysql://localhost:3306/DevEnviroTests";
    static final String USERNAME = "root";
    static final String PASSWORD = "Root123456"; // null password

    
	public SimpleLogIn() throws IOException {
		try {
            // Register JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Open a connection
            System.out.println("Connecting to database...");
            Connection connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);

            // Execute a query
            System.out.println("Creating statement...");
            Statement statement = connection.createStatement();
            
            
            String sql = "SELECT * FROM Users where name = 'Ali'";
            
            
            ResultSet resultSet = statement.executeQuery(sql);

            // Go through the result set to print it
            while (resultSet.next()) {
                // Retrieve data by column name
                String userName = resultSet.getString(1);
                String userPass = resultSet.getString(2);
                
                //Blob blob = resultSet.getBlob(2);
                //byte[] blobBytes = blob.getBytes(1, (int) blob.length());
                //String userPass = new String(blobBytes, StandardCharsets.UTF_8);
             
                System.out.println("userName: " + userName + ", userPass: " + userPass);
            }

            // Close external resources
            resultSet.close();
            statement.close();
            connection.close();

        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			new SimpleLogIn();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
