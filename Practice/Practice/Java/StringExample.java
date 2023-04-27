public class StringExample {
    public StringExample(){
        // StringBuffer
        // 생성된 StringBuffer 객체에 문자열을 추가해 나갈 수 잇다.
        StringBuffer sb = new StringBuffer();
        sb.append("hello");
        sb.append(" ");
        sb.append("jump to java");
        // sb 객체는 String 타입이 아니기 떄문에, toString()으로 문자열로 변환
        String result = sb.toString();
        System.out.println(result);

        // String 자료형은 값이 생성되면 변경할 수 없다. 즉, 값을 추가할 때 마다 String 객체가 새로 생성된다.
        String str = "";
        str += "hello";
        str += " ";
        str += "jump to java";
        System.out.println(str);

        // StringBuilder
        StringBuilder sb1 = new StringBuilder();
        sb1.append("hello");
        sb1.append(" " + "jump to java");
        System.out.println(sb1.toString());

        // 결론
        // StringBuffer 자료형은 String 자료형보다 무겁기 떄문에,
        // StringBuffer 객체를 사용하는 것은 문자열 추가나 변경등의 작업이 많을 경우에 주로 사용
        // 동기화를 고려할 필요가 없을경우, StringBuilder 를 사용하는 것이 유리하다.

        // insert. 특정 인덱스의 위치에 해당 문자열 삽입
        StringBuilder sb2 = new StringBuilder();
        sb2.append("jump to java");
        sb2.insert(0, "hello "); // 0번째의 위치에 문자열 삽입
        System.out.println(sb2.toString());


        // substring.
        StringBuilder sb3 = new StringBuilder();
        sb3.append("Hello jump to java");
        System.out.println(sb3.substring(0, 4));    // 0번째부터 3번째 인덱스의 문자열 출력. 4번째 인덱스는 포함되지 않는다.

    }
}
