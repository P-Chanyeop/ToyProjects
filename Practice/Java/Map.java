import java.util.HashMap;

public class Map {
    public Map(){
        // Map 자료형은 대응관계를 표현할 수 있게 해주는 자료형이다.
        // Associative array, Hash 라고도 불린다.
        // 순서에 의존하지 않고 key로 value를 얻어오는것
        // 입력된 순서대로 데이터를 저장하려면 LinkedHashMap을 사용
        // 입력된 key의 오름차순 순서로 데이터를 저장하려면 TreeMap을 사용한다.

        // HashMap 생성 및 추가(put)
        HashMap<String, String> map = new HashMap<>();
        map.put("people", "사람");
        map.put("baseball", "야구");
        System.out.println(map);    // {baseball=야구, people=사람} 출력

        // key에 해당하는 value값 얻기(get)
        System.out.println(map.get("people"));  // 사람 출력
        System.out.println(map.getOrDefault("java", "자바"));  // key에 해당하는 value가 없을 경우에 null 출력. getOrDefault를 통해 기본값 얻을 수 있음.

        // Map에 해당키가 있는지 조사하여 참, 거짓으로 리턴(ContainsKey)
        System.out.println(map.containsKey("people"));  // True 출력

        // key에 해당하는 {key,value} 아이템을 삭제한 후 value값을 리턴
        System.out.println(map.remove("people"));   // 사람 출력

        // Map의 요소 갯수 리턴
        System.out.println(map.size());

        // Map의 모든 key를 모아 리턴
        map.put("people", "사람");
        System.out.println(map.keySet());   // [baseball, people] 출력. set자료형으로 리턴을 한다.(중복 제거, 순서 없음)


    }
}
