# RoboWorld_UE4.22 Учебный проект

Пилил на коленке для вуза. 

<a href=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/Thesis.docx> Ссылка на диссертацию </a> <br>
<a href=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/Presenration.pptx> Ссылка на презентацию PowerPoint </a>

Проект работает только на версии движка UE4.22. Кроме того, <b>в процессе восстановления проекта Tensorflow перестал работать и мне пришлось заменить нейронку обычным поиском по словарю. </b>

Так что, представленное ниже работает, но на костылях, и только в режиме дебага. 

Для запуска проекта нужно сгенерировать Visual Studio проект, через контекстное меню RoboWorld_BP22.uproject, и скомпилировать все в Visual Studio. 
Кроме того, для корректной работы Python плагина нужно, чтобы в системе был установлен Python 3.6


****
<h2> Эксперимент 1 : Выполнение команды </h2>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0>
  <tr>
   <td> № </td>
   <td> Команда </td>
   <td> Скриншот </td>
   <td> Описание </td>
 </tr>
 <tr>
   <td> 1 </td>
   <td> Принеси воды </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/1_1.png></td>
   <td> Робот перемещается к стакану, расположенному в кухне, и берет его в свободную руку. </td>
 </tr>
  <tr>
   <td> 2 </td>
   <td>  </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/1_2.png></td>
   <td> Затем робот отправляется к ближайшему источнику воды, в данном случае к раковине в кухне, и набирает воду в стакан. </td>
 </tr>
  
  <tr>
   <td> 3 </td>
   <td>  </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/1_3.png></td>
   <td> После чего, идет в зал к журнальному столику и ставит стакан на него </td>
 </tr>
  
</table>

<h2> Эксперимент 2 - Анафорическая неясность </h2>
Во втором эксперименте проверим, как система решит анафорическую неясность во время выполнения другой команды. Сначала будет дана команда «принеси воды», а потом сразу же вторая команда «нет, сначала лекарство».  
  <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/2.png>
 Здесь:
<li>1.	Предполагаемый источник команды (пользователь)</li>
<li>2.	Начальное положение робота</li>
<li>3.	Пустой стакан</li>
<li>4.	Кухонная раковина</li>
<li>5.	Журнальный столик, на который необходимо принести стакан с водой</li>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0>
  <tr>
   <td> № </td>
   <td> Команда </td>
   <td> Скриншот </td>
   <td> Описание </td>
 </tr>
  <tr>
   <td> 1 </td>
   <td> Принеси воды </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/3_1.png> </td>
   <td> Робот перемещается к стакану, и берет его в свободную руку. </td>
 </tr>
  
  <tr>
   <td> 2 </td>
   <td>   </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/3_2.png> </td>
   <td> Затем робот набирает воду в стакан. </td>
 </tr>
 
 <tr>
   <td> 3 </td>
   <td>Нет, сначала лекарство  </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/3_3.png> </td>
   <td> Система принимает новую команду, прекращает выполнение текущее команды, но запоминает не выполненные действия. Робот начинает выполнять следующую команду и, держа стакан с водой в правой руке, немедленно перемещается к лекарству. </td>
 </tr>
 
 <tr>
   <td> 4 </td>
   <td>  </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/3_4.png> </td>
   <td> Робот берет лекарство в свободную (правую) руку и отправляется к журнальному столику.   </td>
 </tr>
 
 <tr>
   <td> 5 </td>
   <td>  </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/3_5.png> </td>
   <td> Робот ставит лекарство на столик.    </td>
 </tr>
 
  <tr>
   <td> 6 </td>
   <td>  </td>
   <td> <img src=https://github.com/Mukudori/RoboWorld_UE4.22/blob/master/Docs/3_6.png> </td>
   <td> Затем возвразается к предыдущей незаконченной команде и ставит на столик стакан.    </td>
 </tr>
 </table>

