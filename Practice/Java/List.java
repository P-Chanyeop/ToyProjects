import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class List {
    public List(){
        // ArrayList
        // add
        ArrayList pitches = new ArrayList();
        pitches.add("138");
        pitches.add("129");
        pitches.add("142");
        pitches.add(0,"133");
        System.out.println(pitches.getClass().getName());

        // get
        System.out.println(pitches.get(1));     // 2번째 투구 스피드 출력.

        // size
        System.out.println(pitches.size());     // 리스트 요소의 갯수 출력

        // contains
        System.out.println(pitches.contains("142"));    // 해당 항목이 리스트에 있는지 판별. true 출력

        // remove
        System.out.println(pitches.remove("138"));    // 해당하는 항목을 리스트에서 제거후 삭제한 결과 리턴. true 출력
        System.out.println(pitches.remove(0));  // 0번째 인덱스에 해당하는 항목을 제거하고 제거된 항목을 리턴. 138

        // Generics
        // 어떤 객체를 포함하는지에 대하여 명확하게 표현할 것을 권고.
        // <String> 의 경우에는 arrayList 안에 담을 수 있는 객체는 String 타입 뿐이라고 알려주는 것.
        // ArrayList 모두 Object 자료형으로 인식되기 때문에, ArrayList에서
        // 값을 가져올 때에는 Object 자료형에서 String 자료형으로 casting 해야함.
        // 하지만 제네릭스를 사용하면 형변환이 필요없다.
        String [] data = {"138", "129", "142"};
        ArrayList<String> arrayList = new ArrayList<>(Arrays.asList(data));
        System.out.println(arrayList);

        // String.join
        // join 을 통해 리스트의 각 요소에 구분자를 삽입하여 하나의 문자열로 만들 수 있다. 배열에도 사용 가능
        String result = String.join(",", arrayList);
        String speed[] = new String[]{"138", "129", "142"};
        result = String.join(",", speed);
        System.out.println(result);

        // sort
        arrayList.sort(Comparator.naturalOrder());  // 오름차순 정렬
        arrayList.sort(Comparator.reverseOrder());  // 내림차순 정렬
    }
}
