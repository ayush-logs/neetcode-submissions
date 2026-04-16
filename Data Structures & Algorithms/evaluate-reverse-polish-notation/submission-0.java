class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>(); 

        for(String s : tokens){
            switch(s){
                case "+":{
                    int val2 = stack.pop(); 
                    int val1 = stack.pop(); 
                    stack.push(val1 + val2); 
                    break; 
                }
                case "-":{
                    int val2 = stack.pop(); 
                    int val1 = stack.pop(); 
                    stack.push(val1 - val2); 
                    break;  
                }

                case "*":{
                    int val2 = stack.pop(); 
                    int val1 = stack.pop(); 
                    stack.push(val1 * val2); 
                    break;
                }

                case "/":{
                    int val2 = stack.pop(); 
                    int val1 = stack.pop(); 
                    stack.push(val1 / val2); 
                    break;
                }

                default:stack.push(Integer.parseInt(s)); 
            }
            
        }

        return stack.peek(); 
    }
}
