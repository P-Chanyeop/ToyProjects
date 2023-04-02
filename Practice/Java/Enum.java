
enum CoffeeType{
    AMERICANO,
    ICE_AMERICANO,
    CAFE_LATTE
};

public class Enum {
    public Enum(){
        // Enum?
        // 서로 관련있는 여러개의 상수 집합을 정의할 때 사용하는 자료형
        System.out.println(CoffeeType.AMERICANO);   // AMERICANO 출력
        System.out.println(CoffeeType.ICE_AMERICANO);   // ICE_AMERICANO 출력
        System.out.println(CoffeeType.CAFE_LATTE);  // CAFE_LATTE 출력

        for(CoffeeType type: CoffeeType.values()){      // CoffeeType.values() 는 CoffeeType의 배열을 리턴.
            System.out.println(type);
        }

        // Enum의 장점
        // CoffeeType에 정의된 상수만 파라미터로 전달할 수 메서드를 만들어 엉뚱한 값에 의한 오류를 방지할 수 있다.
        // 매직넘버(1과 같은 숫자 상수값. 프로그래밍에서 상수로 선언하지 않은 순자)를 사용할 때보다 코드가 명확해 진다.
        // 잘못된 값을 사용함으로 인해 발생할 수 있는 위험성이 사라진다.

    }
}
