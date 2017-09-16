%% 导入数据
data_frame = xlsread('/Users/apple/Documents/Atom/3VModeling_20170914/A/Frame1.xlsx','frame1');
data_mould = xlsread('/Users/apple/Documents/Atom/3VModeling_20170914/A/A_attachment.xlsx','sheet2');
data_q2 = xlsread('/Users/apple/Documents/Atom/3VModeling_20170914/A/A_attachment.xlsx','sheet3');
data_q3 = xlsread('/Users/apple/Documents/Atom/3VModeling_20170914/A/A_attachment.xlsx','sheet5');

%% 数据处理
frame_CT = radon(data_frame, 30:209, 1024);
frame_set = iradon(frame_CT, 30:209, 512);
% 从frame图像的变化可以看到，得到结果的区域为(99:458, 110:469)

%% 得到原始的图像
mould_back = iradon(data_mould, 30:209, 512);
q2_back = iradon(data_q2, 30:209, 512);
q3_back = iradon(data_q3, 30:209, 512);

%% 改变图像的大小
mould = shrink(mould_back(99:458, 110:469));
q2 = shrink(q2_back(99:458, 110:469));
q3 = shrink(q3_back(99:458, 110:469));
% 通过mould的图像来验证方法的可行性

%% 另存为Excel表格
xlswrite('/Users/apple/Documents/Atom/3VModeling_20170914/Alpha/extra/mould.xls', mould);
xlswrite('/Users/apple/Documents/Atom/3VModeling_20170914/Alpha/extra/problem2.xls', q2);
xlswrite('/Users/apple/Documents/Atom/3VModeling_20170914/Alpha/extra/problem3.xls', q3);

%% 函数
function [result]  = shrink(matrix)
% 用于缩放图像的函数
[R, C] = size(matrix);
timesX = 256 / 360;
timesY = 256 / 360;
tras = [1/timesX 0 0; 0 1/timesY 0; 0 0 1];
result = zeros(timesX * R, timesY * C);
for i = 1 : timesX * R
    for j = 1 : timesY * C
        temp = [i; j; 1];
        temp = tras * temp;
        x = int16(temp(1, 1));
        y = int16(temp(2, 1));
        result(i, j) = matrix(x, y);
    end
end
end
% imagesc(frame_set)
