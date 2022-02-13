package firstProblem;

/**
 * @description: 模仿定时查看当前按键操作状态
 * @author EZMarvin
 */
public class SimulateKeyCheck extends Thread{
    private KeyController keyController;
    private int checkTime;
    private int timeInterval = 200;

    SimulateKeyCheck(KeyController keyController, int checkTime, int timeInterval){
        this.keyController = keyController;
        this.checkTime = checkTime;
        this.timeInterval = timeInterval;
    }

    public String getLastestAction(){
        return keyController.actionDetect();
    }

    @Override
    public void run(){
        for(int i = 0; i < checkTime; i++){
            
            System.out.println("KeyStatus -- " + getLastestAction());
            try {
                Thread.sleep(timeInterval);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
