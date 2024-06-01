import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.util.*;

public class WeatherApi {
    public static void main(String[] args){
        try{
            Scanner scanner =new Scanner(System.in);
            String city;
            do{
                System.out.println("===========================================");
                System.out.print("Please enter the city name: ");
                city = scanner.nextLine();
                if(city.equalsIgnoreCase("no")){
                    break;
                }
                //get location data
                JSONObject cityLocationData=(JSONObject) getLocationData(city);
                double latitude=(double) cityLocationData.get("latitude");
                double longitude=(double) cityLocationData.get("longitude");

                displayWeatherData(latitude,longitude);
            }while(!city.equalsIgnoreCase("no"));
        }catch (Exception e){
           e.printStackTrace();
        }

    }
    private static JSONObject getLocationData(String city){
        city = city.replaceAll(" ", "+");

        //geo coding api to get the latitudes and longitudes of city
        String urlString="https://geocoding-api.open-meteo.com/v1/search?name="+
                city+"&count=1&language=en&format=json";
        try{
            //fetch the api response based on api link
            HttpURLConnection apiConnection=fetchApiresponse(urlString);

            //check for api response status
            //200 - means that the connection was a success
             if(apiConnection.getResponseCode()!=200){
                 System.out.println("Sorry : Could not connect to API");
                 return null;
             }

             //2- read the response and convert store String type
            String jsonResponse=readApiResponse(apiConnection);

             //3- Parse the String into json object
            JSONParser parser=new JSONParser();
            JSONObject resultsJsonObject=(JSONObject) parser.parse(jsonResponse);

            //4- Retrieve location data
            JSONArray locationData=(JSONArray) resultsJsonObject.get("results");
            return (JSONObject) locationData.get(0);

        }catch(Exception e){
            e.printStackTrace();
        }
        return null;
    }
    private static HttpURLConnection fetchApiresponse(String urlString) {
        try {
            URL url=new URL(urlString);

            //attempt t create connection
            HttpURLConnection conn=(HttpURLConnection) url.openConnection();

            //set request method to get
            conn.setRequestMethod("GET");

             return conn;

        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    private static String readApiResponse(HttpURLConnection apiconnection){
        try{
            //create a string builder to store the resultin json data
            StringBuilder resultJson=new StringBuilder();

            //create a scanner to read from the input stream of the http urlconnection
            Scanner scanner =new Scanner(apiconnection.getInputStream());

            //loop through each line in the response and append it to the string builder
            while(scanner.hasNext()){
                resultJson.append(scanner.nextLine());
            }
            scanner.close();


            return  resultJson.toString();
        }catch(IOException e){
            e.printStackTrace();
        }
        return null;
    }
    private static void displayWeatherData(double latitude,double longitude){
        try {
            //fetch the api response based on api link
            String url = "https://api.open-meteo.com/v1/forecast?latitude=" +
                    latitude + "&longitude=" + longitude + "&current=temperature_2m,relative_humidity_2m,wind_speed_10m&hourly=temperature_2m";
            HttpURLConnection apiConnection = fetchApiresponse(url);

            //check for repsonse status
            // 200- means connection was a succes
            if (apiConnection.getResponseCode() != 200) {
                System.out.println("Sorry: could not connect ot api");
                return;
            }

            //2- read the response and convert store String
            String jsonResponse = readApiResponse(apiConnection);

            //3- parse the string into JSON object
            JSONParser parser=new JSONParser();
            JSONObject jsonObject=(JSONObject) parser.parse(jsonResponse);
            JSONObject currentWeatherJson=(JSONObject) jsonObject.get("current");



            String time=(String) currentWeatherJson.get("time");
            System.out.println("Current time : "+time);
            double temperature=(double) currentWeatherJson.get("temperature_2m");
            System.out.println("temperature : "+temperature);
            long relativeHumidity=(long) currentWeatherJson.get("relative_humidity_2m");
            System.out.println("Relative humidty : "+relativeHumidity);
            double windspeed=(double) currentWeatherJson.get("wind_speed_10m");
            System.out.println("Windspeed : "+windspeed);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
