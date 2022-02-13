package secondProblem;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;

/**
 * 按键控制类
 * 
 * @author EZMarvin
 */
public class PriorityKeysController {
    HashMap<Integer, PriorityKey> keyMap;

    PriorityKeysController(int keyNum) {
        keyMap = new HashMap<Integer, PriorityKey>();
        for (int i = 1; i <= keyNum; i++) {
            keyMap.put(i, new PriorityKey(i));
        }
    }

    /**
     * @description: 输入控制数据流，输出相应时间输出信号
     * @param pressInput 输入的按键序列，每个元素1s
     * @return 当前时间输出信号，1s
     * @author EZMarvin
     */
    public List<Integer> priorityKeysOutput(int[] pressInput){
        Stack<PriorityKey> remainStack = new Stack<>();
        List<Integer> ans = new ArrayList<>();

        PriorityKey currentOutput = null;

        for(int press : pressInput){
            // 无按键， 无响应
            if (press == 0 && currentOutput == null && remainStack.isEmpty()){
                ans.add(0);
                continue;
            }

            if (currentOutput == null){
                if (remainStack.isEmpty()){
                    currentOutput = keyMap.get(press);
                    currentOutput.trigger();
                } else{
                    currentOutput = remainStack.pop();
                }
                
            }else{
                // 当前有相应信号，忽略所有相等或小于当前优先级的输入
                if(press > currentOutput.getPriority()){
                    remainStack.push(currentOutput);
                    currentOutput = keyMap.get(press);
                    currentOutput.trigger();
                }
            }

            ans.add(currentOutput.outPut());

            // 输出后检查剩余时间
            if (currentOutput.getRemainTime() == 0){
                currentOutput = null;
            }
  
        }

        while(currentOutput != null || !remainStack.isEmpty()){
            ans.add(currentOutput.outPut());
            
            if (currentOutput.getRemainTime() == 0){
                currentOutput = null;
            }

            if (currentOutput == null && !remainStack.isEmpty()){
                currentOutput = remainStack.pop();
            }
        }

        return ans;
    }
}
