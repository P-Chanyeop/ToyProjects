import java.util.Arrays;
import java.util.HashSet;

public class Set {
    public Set(){
        // Set 자료형!
        // 중복을 허용하지 않고, 순서가 없는 자료형(인덱싱을 지원X) Map 자료형과 유사함
        // 입력 순서로 데이터를 가져오고 싶은경우 LinkedHashSet,
        // 오름차순으로 정렬된 데이터를 가져오고 싶을 경우에는 TreeSet 사용.

        // 교집합 구하기(retainAll)
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(3, 4, 5, 6, 7));
        HashSet<Integer> intersection = new HashSet<>(s1);  // s1객체를 복사하여 intersection 생성
        intersection.retainAll(s2); // 교집합 수행
        System.out.println(intersection);   // [3, 4, 5] 출력

        // 합집합 구하기(addAll)
        HashSet<Integer> union = new HashSet<>(s1);
        union.addAll(s2);   // 합집합 수행
        System.out.println(union);   // [1, 2, 3, 4, 5, 6, 7] 출력

        // 차집합 구하기(removeAll)
        HashSet<Integer> substract = new HashSet<>(s1);
        substract.removeAll(s2);
        System.out.println(substract);  // [1, 2] 출력


        // 집합 자료형 관련 메소드
        // 값 추가하기(add)
        HashSet<String> set = new HashSet<>();
        set.add("Jump");
        set.add("To");
        set.add("Java");
        System.out.println(set);    // [Java, To, Jump] 출력

        // 값 여러개 추가하기(addAll)
        set.addAll(Arrays.asList("Jump","To", "Java"));
        System.out.println(set);    // [Java, To, Jump] 출력. 중복 제거

        // 특정 값 제거(remove)
        set.remove("To");
        System.out.println(set);    // [Java, Jump] 출력
    }
}
