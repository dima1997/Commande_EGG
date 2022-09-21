
clear all
close all
clear variables
T = readtable('test1data');
%delete start up values
T([1:200],:) = [];
X=detrend_2d([T.EXGChannel1,T.Timestamp]);

data = X(:,1);
time = X(:,2);
time2 = T.Timestamp_Formatted_;

for k = 1:length(data)
    data(k) = data(k)+time(k);
end
plot(time2,data)
%the x value needs to x + y

%plot(T.Timestamp,T.EXGChannel1)