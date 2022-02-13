package secondProblem;

public class TestCase {
    public static void main(String[] args){

        PriorityKeysController pkController = new PriorityKeysController(3);
        int[] pressInput = {0,0,1,1,0,2,2,0,0,0,3,3,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2};
        System.out.println(pkController.priorityKeysOutput(pressInput));

    }
}
