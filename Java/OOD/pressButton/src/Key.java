import javax.swing.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
public class Key {
    public enum Status {
        UP, DOWN
    }

    private Status currentStatus = Status.UP;

    Key(){

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
