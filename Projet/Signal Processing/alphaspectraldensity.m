clear all
close all
clear variables
samplefreq = 250;
T = readtable('testleftright2');
%delete start up values
T([1:200],:) = [];
data = T.EXGChannel4;
%data = lowpass(T.EXGChannel4,62,250);
timedata = T.Timestamp_Formatted_;
pointsize= 1250
points = length(data)/pointsize;

p = bandpower(data,250,[8,12]);
datapointlistleft = [];
datapointlistright = [];
timelist=[];
for n = 0:points-1
    x=data(((n*pointsize)+1):((n+1)*pointsize))
    datapointleft = bandpower(x,samplefreq,[7.8,8.2]);
    datapointright = bandpower(x,samplefreq,[14.8,15.2])*1.7;
    timepoint =timedata((n+1)*pointsize);
    timelist=[timelist timepoint];
    datapointlistleft=[datapointlistleft datapointleft];
    datapointlistright = [datapointlistright datapointright];
end

N= length(data);

plot(timelist,datapointlistleft);
hold on
plot(timelist,datapointlistright);