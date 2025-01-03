# [Platinum V] 색깔 하노이 탑 - 18122 

[문제 링크](https://www.acmicpc.net/problem/18122) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

다이나믹 프로그래밍, 수학

### 제출 일자

2024년 3월 20일 14:36:00

### 문제 설명

<p>하노이 탑 게임은 3개의 기둥과 여러 장의 크기가 모두 다른 원판을 이용한 게임이다. 처음에는 1번째 기둥에 크기가 큰 원판이 밑에 오도록 모든 원판이 크기 순서대로 놓여 있고, 다음 규칙을 지키면서 모든 원판을 3번째 기둥으로 옮겨야 한다.</p>

<ul>
	<li>작은 원판 위에 큰 원판이 올라올 수 없다.</li>
	<li>한 번에 1개의 원판만 옮길 수 있다.</li>
</ul>

<p>이 규칙을 토대로 원판의 색깔이 두 개인 하노이 탑 게임을 만들려고 한다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 503px; height: 200px;"></p>

<p>처음에는 1번째 기둥에 크기 1인 빨간 원판, 크기 1인 검은 원판, 크기 2인 빨간 원판, 크기 2인 검은 원판, …, 크기 <em>N</em>인 빨간 원판, 크기 <em>N</em>인 검은 원판이 위에서부터 차례대로 놓여 있다.</p>

<p>위의 규칙을 지키면서 원판을 움직여 3번째 기둥에 크기 1인 빨간 원판, 크기 1인 검은 원판, 크기 2인 빨간 원판, 크기 2인 검은 원판, …, 크기 <em>N</em>인 빨간 원판, 크기 <em>N</em>인 검은 원판이 위에서부터 차례대로 오도록 놓아야 한다면, 원판을 최소로 이동시킬 때 총 몇 번 이동해야 할까?</p>

### 입력 

 <p>첫 번째 줄에 정수 <em>N </em>(1 ≤ N ≤ 10<sup>6</sup>)이 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 원판의 최소 이동 횟수를 출력하여라. 수가 커질 수도 있으니, 최소 이동 횟수를 10<sup>9</sup> + 7로 나눈 나머지를 출력하여라.</p>

