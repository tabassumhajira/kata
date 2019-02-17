import java.util.Arrays;
import java.util.Scanner;
class Lex {

	public static void main(String[] args) {
System.out.println(" ");
Scanner in=new Scanner(System.in);
String s=in.next();
char c1[]=s.toCharArray();
char[] c=s.toCharArray();
Arrays.sort(c);
int l=c.length,count=0,count1=0,i=0;
char ch=c[c.length-1];
for(int j=0;j<c1.length;j++){
	if(ch==c1[j]){
	System.out.println(s.substring(j));
	}}}}
