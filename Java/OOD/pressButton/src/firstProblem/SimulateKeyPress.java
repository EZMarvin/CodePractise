package firstProblem;

/**
 * @description: 根据输入信号模拟按键操作
 * @author EZMarvin
 */
public class SimulateKeyPress extends Thread{
    private KeyController keyController;
    private int[] signalStream;
    private int timeInterval;

    SimulateKeyPress(KeyController keyController, int[] signalStream, int timeInterval){
        this.keyController = keyController;
        this.signalStream = signalStream;
        this.timeInterval = timeInterval;
    }

    public void simulateKeyPress(KeyController controller, int[] signalStream) throws InterruptedException{
        for(int i = 1; i < signalStream.length; i++){
            if(signalStream[i] == 0 && signalStream[i-1] != 0){
                controller.releaseEvent();
                System.out.println("Control - Key Release");
            }
            if(signalStream[i] != 0 && signalStream[i-1] == 0){
                controller.pressEvent();
                System.out.println("Control - Key Press");
                
            }
            Thread.sleep(timeInterval);
        }
    }

    @Override
    public void run(){
        try {
            simulateKeyPress(keyController, signalStream);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
}
