import twitter4j.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
public class tweetExtractor {
public static void main(String[] args)
{
Twitter twitter = new TwitterFactory().getInstance();
try {
Query query = new Query("");
QueryResult result;
File file = new File("outputs/tweets.txt");
FileWriter fw = new FileWriter(file, true);
BufferedWriter bw = new BufferedWriter(fw);
do {
result = twitter.search(query);
List<Status> tweets = result.getTweets();
for (Status tweet : tweets) {
System.out.println("@" + tweet.getUser().getScreenName() + " - " + tweet.getText() + "\n");
bw.write("@" + tweet.getUser().getScreenName() + " - " + tweet.getText() +"\n");
}
}
while ((query = result.nextQuery()) != null);
System.exit(0);
bw.close();
} catch (TwitterException te) {
te.printStackTrace();
System.out.println("Failed to search tweets: " + te.getMessage());
System.exit(-1);
} catch (IOException e) {    e.printStackTrace();    }
}
}
