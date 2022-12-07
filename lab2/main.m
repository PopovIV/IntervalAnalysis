% Коэффициенты ИСЛАУ
A = [infsup(0, 2), infsup(1, 3); 1, infsup(-4, -2); infsup(0.75, 1.25), 0; 0, infsup(0.75, 1.25)];
b = [infsup(3, 7); infsup(-0.5, 0.5); infsup(3, 5); infsup(0, 2)];
% Распознающий функционал
Tol = @(A,b,x) min(rad(b) - mag(mid(b) - A * x));

[tolMax,argMax,envs,ccode] = tolsolvty(inf(A), sup(A), inf(b), sup(b));
tolMax
argMax
%  Допусковое множество решений интервальной линейной системы пусто


n = 100;
levels = 30;
drawContour(A,b,n,levels)

%% Коррекция вектора b
e = [infsup(-1, 1); infsup(-1, 1); infsup(-1, 1); infsup(-1, 1)];
C = 1.5 * abs(tolMax);
b1 = b + C * e;
b1
drawContour(A,b1,n,levels)

[tolMax1,argMax1,~,~] = tolsolvty(inf(A), sup(A), inf(b1), sup(b1));
tolMax1
argMax1
ive1 = ive(A, b1);
rve1 = rve(A, tolMax1);
iveBox = [midrad(argMax1(1), ive1);midrad(argMax1(2), ive1)];
rveBox = [midrad(argMax1(1), rve1);midrad(argMax1(2), rve1)];
rectangle('position', [inf(iveBox(1)), inf(iveBox(2)), sup(iveBox(1)) - inf(iveBox(1)), sup(iveBox(2)) - inf(iveBox(2))])
rectangle('position', [inf(rveBox(1)), inf(rveBox(2)), sup(rveBox(1)) - inf(rveBox(1)), sup(rveBox(2)) - inf(rveBox(2))])

%% Коррекция матрицы А
koef = 1.5;
b2 = [infsup(0, 9); infsup(-3, 3); infsup(0, 7); infsup(-2, 5)];
[tolMax2,argMax2,~,~] = tolsolvty(inf(A), sup(A), inf(b2), sup(b2));
E = 1.036 * [argMax2(1) * 0.23 0.96455; -5.0 0.1; argMax2(1) * 1.23 7.4; 0 argMax2(1) * 0];
A1 = infsup(inf(A) + E, sup(A) - E);
A1
drawContour(A1,b2,n,levels);

[tolMax2,argMax2,~,~] = tolsolvty(inf(A1), sup(A1), inf(b2), sup(b2));
tolMax2
argMax2
ive2 = ive(A1, b2);
rve2 = rve(A1, tolMax2);
iveBox2 = [midrad(argMax2(1), ive2);midrad(argMax2(2), ive2)];
rveBox2 = [midrad(argMax2(1), rve2);midrad(argMax2(2), rve2)];
rectangle('position', [inf(iveBox(1)), inf(iveBox(2)), sup(iveBox(1)) - inf(iveBox(1)), sup(iveBox(2)) - inf(iveBox(2))])
rectangle('position', [inf(rveBox(1)), inf(rveBox(2)), sup(rveBox(1)) - inf(rveBox(1)), sup(rveBox(2)) - inf(rveBox(2))])


%% Положение максимума Tol
n = 100;
levels = 30;
drawContour(A,b,n,levels)

iterations = 10;
figure
A2 = A;
for i = 1:iterations
    A2 = A2 ./ 2;
    [~,argMax,~,~] = tolsolvty(inf(A2), sup(A2), inf(b), sup(b));
    plot(argMax(1), argMax(2), '*b');
    hold on
end
grid on

%Положение максимумов Tol
A2 = A;
line1 = [1, 1; 0, 0; 0, 0; 0, 0]
line2 = [0, 0; 1, 1; 0, 0; 0, 0]
line3 = [0, 0; 0, 0; 1, 1; 0, 0]
line4 = [0, 0; 0, 0; 0, 0; 1, 1]
figure
drawTolMax(A2, b, line1, iterations)
figure
drawTolMax(A2, b, line2, iterations)
figure
drawTolMax(A2, b, line3, iterations)
figure
drawTolMax(A2, b, line4, iterations)

