clear all
close all
clear variables
Fs = 250;
T = readtable('testleftright2');
%delete start up values
T([1:200],:) = [];
data = T.EXGChannel4
%data = lowpass(T.EXGChannel4,62,250);

N = length(data);
xdft = fft(data);
xdft = xdft(1:N/2+1);
psdx = (1/(Fs*N)) * abs(xdft).^2;
psdx(2:end-1) = 2*psdx(2:end-1);
freq = 0:Fs/length(data):Fs/2;

plot(freq,10*log10(psdx))
grid on
title('Periodogram Using FFT')
xlabel('Frequency (Hz)')
ylabel('Power/Frequency (dB/Hz)')