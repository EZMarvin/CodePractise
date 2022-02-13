package secondProblem;

/**
 * 带优先级按键类
 * 
 * @author EZMarvin
 */
public class PriorityKey {
    private int priority;
    private int remainTime;

    PriorityKey(int priority){
        this.priority = priority;
        this.remainTime = 0;
    }

    public void trigger(){
        if (remainTime == 0){
            remainTime = 10;
        }
    }

    public int getPriority(){
        return priority;
    }

    public int getRemainTime(){
        return remainTime;
    }

    public int outPut(){
        if (remainTime > 0){
            remainTime--;
            return priority;
        }
        return 0;
    }
}
