Galpi_Music
===========

2021년 창업동아리 활동을 하며 진행했던 갈피 프로젝트 중 하나.   
쉽게 나누기 힘든 주제인 죽음을 좀 더 사려깊게 주변 사람들에게 전달하기 위한 서비스.   

[텀블벅](https://tumblbug.com/galpi_me)에서 후원을 받아 진행했다.   

galpi_music은 프로젝트 홍보를 위해 누구나 무료로 즐길 수 있게 만들었다.   
본격적으로 내 삶의 마무리에 대해 생각하기 전에   
흥미 위주의 최근 유행하고 있는 심리테스트 웹을 제작하게 되었다.   
### "장례식에 흘러나올 내 인생의 주제곡은?"   
을 타이틀로 무겁지 않지만 여운을 줄 수 있도록 만들었다.   
   
후원시 제공되는 [심화 테스트](https://github.com/jeongkite/Galpi_Talk)도 함께 개발했다.    
   
   ***
   
## 해당 프로젝트를 통해 처음 경험했던 것   
- **기획자, 디자이너 역할 구분이 확실한 개발 프로젝트**   
  고등학교때 디자이너로는 참여해봤지만 개발자로서 역할 구분이 확실한 프로젝트는 처음이었다.
  동아리에서는 개자이너였는데 이 프로젝트에서는 딱 개발만 했다. 기획자겸 팀장님의 전공이 it와 무관했고 관련 경험도 없으셔서 초반엔 서로 의사소통이 원활하지 않았지만 관련 지식을 얻을 수 있는 책과 영상 자료를 추천해드리니 금방 습득하셔서 그 다음 회의때 favicon을 만들어 오셔서 놀랐다. 그 favicon을 사용하진 않았지만 정말 멋진 분이구나 느꼈던 일화. 프로젝트에 대한 이해도가 조금씩 생기니 의사소통도 원활해졌고, 의견도 더 적극적으로 낼 수 있었다.
- **Lottie를 이용한 애니메이션 삽입**   
  개인적으로 스스로에게 실망했고, 더 열심히 해야겠다 생각했던 부분. 이런저런 자료를 찾아 띄우려고 노력했는데 진짜 되질 않아서 3일동안 헤맸다. 디자이너 친구한테 파일 다시 내보내기 해달라고 부탁도 해보고 별에별짓을 다 했는데 cdn을 잘못 불러오는 실수 때문이었다. 이를 통해 앞으로는 공식 문서를 제대로 읽어야 겠다 생각했다. 그러려면 우선 영어공부를 해야하는데.. 새해마다 다짐하지만 올해도 쉽지 않다.
- **url에서 민감한 정보 가리기**
   이 부분은 동아리에서 만난 멋진 분이 코드를 피드백해주시며 알게되었다. django로 개발하다보니 사용자가 테스트를 시작할 때마다 mbti 요소 값이 들어있는 객체를 생성해 테스트를 진행하는 동안 끌고다니는데, 기존에는 오브젝트의 pk값이 url에 그대로 드러나있었다. 이를 가리기 위해 hashlib 모듈의 sha256 알고리즘을 사용해 임의의 문자열을 만들어 url에 포함시켜 끌고다니도록 바꿨다.
   
## 앞으로 고치고 싶은 부분
- **Django가 아니라 React**
  이때는 스스로 만들 수 있는 방법이 django 뿐이라 이렇게 만들었지만 사실 서버에서 무언가를 할 필요가 전혀 없긴 하다. 요즘 React Native를 배우기 위해 Vanilla JS, React 등을 배우며 스터디를 진행중인데, 나중에 React를 이용해서 다시 개발해보고 싶다.   
  
## 마지막으로..
팀 내에 개발자가 나 혼자라는 점이 참 힘들었다. 힘들어하는 어린 양을 도와주는 분들이 계셔 너무 다행이었다. 그래도 누군가와 함께 지속적으로 개발 방향에 대해 의논하고 더 나은 방법을 고민할 수 없어 아쉬웠다. 특히 
   
   
   <br>
   <br>
###### 서버 내려서 시크릿키 제외하지 않고 올립니다~ 궁금하시면 로컬에서 돌려보세요~~
