package firstProblem;

/**
 * 按键类
 * 
 * @author EZMarvin
 */
public class Key {

    private Status currentStatus = Status.UP;
    public enum Status {
        UP, DOWN
    }

    public int getCurrentStatus(){
        if(currentStatus == Status.UP){
            return 0;
        }
        if(currentStatus == Status.DOWN){
            return 1;
        }
        return -1;
    }

    public int keyPress(){
        currentStatus = Status.DOWN;
        return 1;
    }

    public int keyRelease(){
        currentStatus = Status.UP;
        return 0;
    }
}
