def ChangesAndReturnsParamterList(ParameterList):
    ParameterList.pop()                                                                                 # FunctionExecution                         FunctionStart
    print('ParamterList (InsideFunction-DuringFunctionExecution): ' + str(ParameterList))                    # FunctionExecution
    return ParameterList                                                                                # FunctionExecution     FunctionReturn      FunctionEnd


ArgumentList = [1,2,3]
print('ArgumentList (OutsideFunction-BeforeFunctionCall): ' + str(ArgumentList))                        # BeforeFunctionCall

ChangesAndReturnsParamterList(ArgumentList)                                                             # FunctionCall


print('ArgumentList (OutsideFunction-AfterFunctionReturn): ' + str(ArgumentList))                       # AfterFunctionCall


# Program confirms that:
#   The List used as argument is changed by the function manipulating its parameter.

#   A function can have an effect on variables outside its own scope - 
#       by manipulating its parameters
#       it also manipulates the arguments that exists/lives outside the function scope.

#       The VariableName passed as argument
#   AND The VariableName received as paramter
#       PointsTo/RefersTo the Same object in memory.
