TimeStamp = 0;
TargetFreq1=25;
TargetFreq2=10;
Sensitivity = 0.2;
while true
    update = false;
    
    while update == false
        TimeStampbBefore =TimeStamp;
        FileInfo = dir('filename') ;
        TimeStamp = FileInfo.date;
        % Get individual components of date & time in 1 Sec resolution
        if TimeStampBefore ~= TimeStamp
            update = True;
            clear all
            close all
            clear variables
            samplefreq = 250;
            T = readtable('filename');
            %delete start up values
            T([1:200],:) = [];
            data = T.EXGChannel4;
            %data = lowpass(T.EXGChannel4,62,250);
            timedata = T.Timestamp_Formatted_;
            pointsize= 1250;
            points = length(data)/pointsize;
            p = bandpower(data,250,[8,12]);
            datapointlistleft = [];
            datapointlistright = [];
            timelist=[];
            for n = 0:points-1
                x=data(((n*pointsize)+1):((n+1)*pointsize));
                datapointleft = bandpower(x,samplefreq,[TargetFreq1-Sensitivity,TargetFreq1+Sensitivity]);
                datapointright = bandpower(x,samplefreq,[TargetFreq2-Sensitivity,TargetFreq2+Sensitivity]);
                timepoint =timedata((n+1)*pointsize);
                timelist=[timelist timepoint];
                datapointlistleft=[datapointlistleft datapointleft];
                datapointlistright = [datapointlistright datapointright];
            end

            N= length(data);
            plot(timelist,datapointlistleft);
            hold on
            plot(timelist,datapointlistright);
            hold off
        end
    end
end