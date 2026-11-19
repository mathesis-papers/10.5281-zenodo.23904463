/* The same mathematical construction as the bilingual reading and seminar.
   All scenes use the installed deterministic film engine. */
'use strict';
const words = ['000','001','010','011','100','101','110','111'];
function heading(zh, en) {
  txt(zh, 960, 215, {size:54, fam:F.zh, align:'center', c:C.white});
  txt(en, 960, 272, {size:30, fam:F.disp, align:'center', c:C.cyan});
}
function bars(values, x, y, width, height, colour, a=1) {
  const step=width/8;
  ctx.save(); ctx.globalAlpha=a;
  values.forEach((v,i)=>{
    ctx.fillStyle=colour; ctx.fillRect(x+i*step+12,y+height-v*height/0.25,step-24,v*height/0.25);
    txt(words[i],x+(i+0.5)*step,y+height+36,{size:24,fam:F.mono,align:'center',c:C.white});
  }); ctx.restore();
}
function wheel(x,y,k,a) {
  ctx.save();ctx.globalAlpha=a;ctx.strokeStyle=C.dim;ctx.lineWidth=3;
  ctx.beginPath();ctx.arc(x,y,100,0,Math.PI*2);ctx.stroke();
  for(let r=0;r<3;r++){
    const q=-Math.PI/2+r*Math.PI*2/3;
    dot(x+100*Math.cos(q),y+100*Math.sin(q),9,'c',a);
  }
  const q=-Math.PI/2+k*Math.PI*2/3;
  ctx.strokeStyle=C.now;ctx.lineWidth=8;ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+90*Math.cos(q),y+90*Math.sin(q));ctx.stroke();
  ctx.restore();
}
SCENES.question = S => {
  heading('最近态一定有整齐的形状吗？','Must the nearest state have the proposed shape?');
  panel(160,350,740,365,1,C.cyan,'INDEPENDENT RECIPES');
  panel(1020,350,740,365,at(S,1,0.8),C.cyan,'RANDOM MIXTURE');
  ['A','B','C'].forEach((q,i)=>{chip(315+i*215,420,150,95,q,C.cyan,at(S,0,0.8),42,F.disp);});
  txt('product state',530,620,{size:40,fam:F.disp,align:'center',c:C.white});
  txt('Σ weights × recipes',1390,515,{size:38,fam:F.math,align:'center',c:C.white,a:at(S,1,0.8)});
  txt('fully separable',1390,620,{size:40,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.8)});
  txt('D = Σ |entry difference|²',960,800,{size:42,fam:F.math,align:'center',c:C.cyan,a:at(S,2,0.8)});
};
SCENES.shape = S => {
  heading('把八个概率压进三个分组','A restriction on populations');
  panel(100,335,830,460,1,C.cyan,'TARGET ρ');
  bars([.2,.2,.2,.2,0,0,0,.2],145,400,740,230,C.cyan);
  txt('corner coherence = 11 / 112',515,740,{size:29,fam:F.math,align:'center',c:C.white});
  panel(990,335,830,460,at(S,1,0.8),C.argued,'PROPOSED FAMILY: S*');
  bars([3/16,3/16,3/16,3/16,1/48,1/48,1/48,3/16],1035,400,740,230,C.argued,at(S,1,0.8));
  txt('A  B  B  B  C  C  C  A',1405,740,{size:28,fam:F.mono,align:'center',c:C.white,a:at(S,1,0.8)});
  txt('restricted minimum = 109 / 23520',960,850,{size:38,fam:F.math,align:'center',c:C.white,a:at(S,2,0.8)});
};
SCENES.bound = S => {
  badgeQ(S, [[0, 'linear inequality', 'argued']]);
  heading('配方：常数之外全非负','A lower bound for every feasible state of the shape');
  panel(180,350,1560,450,1,C.argued,'EXACT SQUARE COMPLETION');
  txt('D(ρ,S) = 109 / 23520',960,450,{size:52,fam:F.math,align:'center',c:C.white});
  txt('+ 2(A−3/16)² + 3(B−3/16)² + 3(C−1/48)²',960,555,{size:37,fam:F.math,align:'center',c:C.white,a:at(S,1,1)});
  txt('+ 2(x−1/16)² + 2y² + h/7',960,635,{size:42,fam:F.math,align:'center',c:C.white,a:at(S,1,1)});
  txt('h ≥ 0 comes from full separability',960,735,{size:32,fam:F.disp,align:'center',c:C.cyan,a:at(S,1,1)});
  txt('S* makes every extra term zero',960,855,{size:38,fam:F.disp,align:'center',c:C.white,a:at(S,2,0.8)});
};
SCENES.phases = S => {
  heading('相位抵消，乘积结构保留','Nine product recipes and one basis state');
  const k=Math.min(8,Math.floor(S.p*9));
  const r=k%3,s=Math.floor(k/3);
  wheel(470,455,r,1);wheel(960,455,s,1);wheel(1450,455,(-r-s+6)%3,1);
  ['r','s','−r−s'].forEach((q,i)=>txt(q,470+i*490,625,{size:42,fam:F.math,align:'center',c:C.white}));
  txt('1 + ω + ω² = 0',960,720,{size:48,fam:F.math,align:'center',c:C.cyan,a:at(S,1,0.8)});
  txt('9 × (5/54) + 1/6 = 1',960,820,{size:40,fam:F.math,align:'center',c:C.white,a:at(S,2,0.8)});
};
SCENES.escape = S => {
  heading('只改 1/400，便越过形状限制','A small feasible perturbation gives a strict improvement');
  panel(120,350,1680,170,1,C.cyan,'LOCAL PROBABILITIES');
  txt('(9/10, 1/2, 1/2)  →  (9/10, 199/400, 199/400)',960,455,{size:43,fam:F.math,align:'center',c:C.white});
  txt('same mixture structure • same weights',960,575,{size:37,fam:F.disp,align:'center',c:C.cyan,a:at(S,1,0.8)});
  panel(220,625,1480,175,at(S,2,0.8),C.argued,'EXACT POSITIVE GAP');
  txt('109/23520 − D(ρ,τ) = 84926789/12902400000000 > 0',960,730,{size:37,fam:F.math,align:'center',c:C.white,a:at(S,2,0.8)});
};
SCENES.scope = S => {
  badgeQ(S, [[0, 'universal shape conjecture is false', 'lean'], [1, 'extra equality of populations', 'argued'], [2, 'true nearest state', 'open']]);
  const question = Q(S,2,'true nearest state') > 0;
  if (question) heading('真正的最近态是什么？','What is the actual global minimum?');
  else if (at(S,1,0.5)>0) heading('角支撑保留，额外概率等式失效','Keep corner support; release the extra equalities');
  else heading('普遍形状猜想不成立','The universal shape conjecture is false');
  panel(210,350,1500,190,1,C.cyan,'THE PRECISE LESSON');
  txt(question ? 'This finite-n optimum remains to be determined.' : 'Keep corner support. Release the population equalities.',960,460,{size:38,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.8)});
  txt('Symmetry must preserve the target AND the feasible set.',960,620,{size:36,fam:F.disp,align:'center',c:C.cyan,a:at(S,2,0.8)});
  txt('Haobo Ma · Wenlin Zhang',960,755,{size:38,fam:F.disp,align:'center',c:C.white,a:at(S,3,0.8)});
  txt('Question: M. Consiglio · T. J. G. Apollaro · M. Wieśniak',960,815,{size:28,fam:F.disp,align:'center',c:C.dim,a:at(S,3,0.8)});
};
FILM.poster = () => {
  heading('最近态，逃出猜想形状','Escaping the conjectured closest-state shape');
  panel(180,355,1560,405,1,C.cyan,'ONE FEASIBLE CHALLENGER');
  txt('D(ρ,τ) < 109 / 23520',960,495,{size:76,fam:F.math,align:'center',c:C.white});
  txt('ten product states  •  exact positive gap',960,610,{size:40,fam:F.disp,align:'center',c:C.cyan});
  txt('Haobo Ma · Wenlin Zhang',960,705,{size:32,fam:F.disp,align:'center',c:C.white});
};
