clear all
close all
clear variables
T = readtable('test1data');
T([1],:) = [];
% plot(T.Timestamp_Formatted_, T.EXGChannel0);
filtered = lowpass(T.EXGChannel4,62,250);
hold on
%plot(T.Timestamp_Formatted_,T.EXGChannel4);
plot(T.Timestamp_Formatted_,filtered);
% plot(T.Timestamp_Formatted_, T.EXGChannel1);
% plot(T.Timestamp_Formatted_, T.EXGChannel2);
% plot(T.Timestamp_Formatted_, T.EXGChannel3);
% plot(T.Timestamp_Formatted_, T.EXGChannel4);
% plot(T.Timestamp_Formatted_, T.EXGChannel5);
% plot(T.Timestamp_Formatted_, T.EXGChannel6);
% %plot(T.Timestamp_Formatted_, T.EXGChannel7);
% plot(T.Timestamp_Formatted_, T.AccelChannel0);
% plot(T.Timestamp_Formatted_, T.AccelChannel1);
legend ("ech1","ech2","ech3","ech4","ech5","ech6","a0","a1")
%plot(T.Timestamp_Formatted_, T.AccelChannel2);
hold off
