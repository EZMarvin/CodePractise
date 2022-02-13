package firstProblem;

/**
 * 按键控制类
 * 
 * @author EZMarvin
 */
public class KeyController {
    private Key mkey;
    /** 当前按键状态，分离两个状态 目的模仿防抖，以及判定长按键的组合操作
    * 0 - normal 正常弹起状态
    * 1 - press
    * 2 - long press
    */
    private int state = 0;
    /** 最近一次下按时间 */
    private long lastPressTime;
    /** 最近一次释放时间 */
    private long lastReleaseTime;
    /** 判定为长按的时间阀值 ms*/
    private int longPressThreshold = 1200;
    /** 判定为双击的时间阀值 ms*/
    private int douleClickThreshold = 1500;
    /** 刷新操作记录的时间阀值 ms*/
    private int refreshThreshold = 1000;

    private KeyController.KeyAction key_action = KeyAction.RELEASE;

    public enum KeyAction{
        SINGLECLICK,
        LONGPRESS,
        DOUBLECLICK,
        PRESS,
        RELEASE
    }

    KeyController(Key key){
        this.mkey = key;
    }

    KeyController(Key key, int longPressThreshold, int douleClickThreshold, int refreshThreshold){
        this.mkey = key;
        this.longPressThreshold = longPressThreshold;
        this.douleClickThreshold = douleClickThreshold;
        this.refreshThreshold = refreshThreshold;
    }

    public void pressEvent(){
        mkey.keyPress();
        key_action = KeyAction.PRESS;

        // 从0到1为按下
        if (state == 0 && mkey.getCurrentStatus() == 1){
            state = 1;
            lastPressTime = System.currentTimeMillis();
        }
    }

    public void releaseEvent(){
        mkey.keyRelease();
        key_action = KeyAction.RELEASE;

        // 已经判定为长按情况
        if (state == 2){
            state = 0;
            key_action = KeyAction.LONGPRESS;
            lastReleaseTime = System.currentTimeMillis();
        }

        // 正常释放，状态判定
        // 双击看两次release 时间
        // 长按 + 短按 = 可以成为双击
        // 短按 + 长按 = 当做一次单击，一次长按
        if(state == 1 && mkey.getCurrentStatus() == 0){
            long markTime = System.currentTimeMillis();

            if (markTime - lastPressTime > longPressThreshold){
                key_action = KeyAction.LONGPRESS;
            }else if (markTime - lastReleaseTime > douleClickThreshold){
                key_action = KeyAction.SINGLECLICK;
            }else{
                key_action = KeyAction.DOUBLECLICK;
            }
            state = 0;
            lastReleaseTime = System.currentTimeMillis();
        }
        
    }

    public int status(){
        return state;
    }

    public String actionDetect(){
        long markTime = System.currentTimeMillis();

        // 按键按下过程中查看状态
        if (state == 1){
            
            long timeDiff = markTime - lastPressTime;

            // 长按判定
            if(timeDiff > longPressThreshold){
                state = 2;
                key_action = KeyAction.LONGPRESS;
            }
        }
        
        // 长时间没有操作 则更新状态
        if (state == 0 && key_action != KeyAction.RELEASE && System.currentTimeMillis() - lastReleaseTime > refreshThreshold){
            key_action = KeyAction.RELEASE;
        }

        return key_action.toString();
    }
}
