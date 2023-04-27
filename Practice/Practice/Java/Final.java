import java.util.ArrayList;
import java.util.Arrays;

public class Final {
    public Final(){
        // 형 변환 예시
        // 문자열 -> 정수(Integer.parseInt)
        String num = "123";
        System.out.println(Integer.parseInt(num));  // 123(정수) 출력

        // 정수 -> 문자열 ("")
        int n = 123;
        System.out.println("" + n);     // 123(문자열) 출력

        n = 123;
        System.out.println(String.valueOf(n).getClass().getName());     // 문자열 123
        System.out.println(Integer.toString(n).getClass().getName());   // 문자열 123

        // 실수 -> 문자열 (Double.parseDouble)
        num = "123.456";
        System.out.println(Double.parseDouble(num));     // 실수 123.456 출력


        // 정수를 실수로 변환할때에는 캐스팅이 필요없다.
        // 실수를 정수로 변환할떄에는 캐스팅을 반드시 해주어야 한다.
        int n1 = 123;
        double d1 = n1;
        System.out.println(d1);     // 123.0 출력

        double d2 = 123.123;
        int n2 = (int) d2;
        System.out.println(n2);     // 소숫점이 생략된 123 출력

        // 단, 실수 형태의 문자열을 정수로 변환하려고 하면 NumberFormatException이 발생
        num = "123.456";
//      System.out.println(Integer.parseInt(num));



        // final 자료형
        // 값을 단 한번만 설정할 수 있게 강제하는 키워드. 값을 한번 설정하면 그 값을 다시 설정할 수 없다.
        final int number = 123;
//      number = 456    // 컴파일 에러.

        // 리스트의 경우에도 final로 선언시 재할당 불가능
        // 단 리스트의 경우 add, remove는 가능. 만약 add, remove도 불가능하게 만들려면 List.of로 수정이 불가능한 리스트를 만든다.(Unmodifiable List)기
        final ArrayList<String> a = new ArrayList<>(Arrays.asList("a", "b"));
//      a = new ArrayList<>(Arrays.asList("c", "d"));   // 컴파일 에러

    }

}
