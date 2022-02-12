public class KeyController {
    private Key mkey;
    private int state = 0;
    private int key_switch_up_flag = 0;
    private long actionStartTime;
    private long actionCheckTime;

    public enum KeyAction{
        SINGLECLICK,
        LONGPRESS,
        DOUBLECLICK,
        RELEASE,
        PRESS

    }
    KeyController(Key key){
        this.mkey = key;
    }

    public void pressEvent(){
        mkey.keyPress();
    }

    public void releaseEvent(){
        mkey.keyRelease();
    }

    public void status(){
        mkey.getCurrentStatus();
    }

    public String actionDetect(){
        if (state == 0 && mkey.getCurrentStatus() == 0 && key_switch_up_flag == 0){
            state = 1;
            actionStartTime = System.currentTimeMillis();
        }

        if (state == 1){
            actionCheckTime = System.currentTimeMillis();
            long timeDiff = actionCheckTime - actionStartTime;

            // 长按
            if(timeDiff > 50000){
                state = 2;
            }

            // 按键回弹
            if(mkey.getCurrentStatus() == 1){
                state = 3;
                actionStartTime = System.currentTimeMillis();
            }
        }

        if(state == 2){
            state = 0;
            key_action = 3;
        }

        if(state == 3 && key_up_flag == 0){

        }

        return key_action
    }
}
