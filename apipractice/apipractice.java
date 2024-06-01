import java.util.*;
import java.io.*;
import java.net.*;
import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;


public class apipractice {
    public static void main(String[] args){
        try{
            Scanner sc=new Scanner(System.in);
            String city;
        do{
            System.out.println("==============================================");
            System.out.print("Enter the city (Say no to quit) : ");
            city=sc.nextLine();
            if(city.equalsIgnoreCase("no")){
                break;
            }
            JSONObject cityLocationData=(JSONObject) getLocationData(city);
            double latitude =(double) cityLocationData.get("latitude");
            double longitude=(double) cityLocationData.get("longitude");
            displayWeatherData(latitude,longitude);


        }while(!city.equalsIgnoreCase("no"));
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    private static JSONObject getLocationData(String city){
        city=city.replaceAll(" ","+");
        String url="https://geocoding-api.open-meteo.com/v1/search?name="+
                city+"&count=1&language=en&format=json";
        try{
            HttpURLConnection conn=(HttpURLConnection) fetchApiResponse(url);

            if(conn.getResponseCode()!=200){
                System.out.println("Sorry: Could not connect to Api");
                return null;
            }

            String JsonResponse= readApiResponse(conn);

            JSONParser parser=new JSONParser();
            JSONObject jsonObject=(JSONObject) parser.parse(JsonResponse);
            JSONArray locationData= (JSONArray) jsonObject.get("results");
            return (JSONObject)locationData.get(0);

        }catch(Exception e){
            e.printStackTrace();
        }
        return null;

    }

    private static HttpURLConnection fetchApiResponse(String url){
        try {
            URL urlString = new URL(url);

            HttpURLConnection conn=(HttpURLConnection) urlString.openConnection();

            conn.setRequestMethod("GET");

            return conn;

        }catch(IOException e){
            e.printStackTrace();
        }
        return null;
    }


    private static String readApiResponse(HttpURLConnection conn){
        try{
        StringBuilder  resultJson =new StringBuilder();
        Scanner sc=new Scanner(conn.getInputStream());

        while(sc.hasNext()){
            resultJson.append(sc.nextLine());
        }
        return resultJson.toString();

        }catch(IOException e){
            e.printStackTrace();
        }
        return null;
    }


    private static void displayWeatherData(double latitude,double longitude){
        try {
            String url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude +
                    "&longitude=" + longitude +
                    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m&hourly=temperature_2m";

            HttpURLConnection apiConnection=fetchApiResponse(url);

            if(apiConnection.getResponseCode()!=200){
                System.out.println("Sorry: Could not connect to api");
                return;
            }
             String apiResponse=readApiResponse(apiConnection);

            JSONParser parser=new JSONParser();
            JSONObject jsonObject=(JSONObject) parser.parse(apiResponse);
            JSONObject currentWeatherJSON=(JSONObject) jsonObject.get("current");

            String time=(String) currentWeatherJSON.get("time");
            System.out.println("Current time : "+time);
            System.out.println("Temperature : "+currentWeatherJSON.get("temperature_2m"));
            System.out.println("Relative humidity : "+currentWeatherJSON.get("relative_humidity_2m"));
            System.out.println("Wind speed : "+currentWeatherJSON.get("wind_speed_10m"));


        }catch(Exception e){
            e.printStackTrace();
        }


    }




}

