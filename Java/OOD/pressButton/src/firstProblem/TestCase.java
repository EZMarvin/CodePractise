package firstProblem;

public class TestCase {
    public static void main(String[] args){
        Key key = new Key();
        KeyController keyController = new KeyController(key);


        // 单击
        int[] singleClick = {0,0,1,1,0,0,0};
        // 双击
        int[] douleClick = {0,0,1,1,0,1,1,0,0,0};
        // 长按
        int[] longPress = {0,0,1,1,1,1,1,1,1,0,0,0,0};
        // 长按+快速单击 = 双击
        int[] longPressDouble = {0,0,1,1,1,1,1,0,1,0,0,0};
        // 单机 + 长按
        int[] singleWithLongPress = {0,0,1,1,0,1,1,1,1,0,0,0};
        SimulateKeyPress simulateKeyPress = new SimulateKeyPress(keyController, longPressDouble, 300);
        SimulateKeyCheck simulateKeyCheck = new SimulateKeyCheck(keyController, longPressDouble.length * 2, 200);
        
        
        simulateKeyPress.start();
        simulateKeyCheck.start();
        
    }
    
}
