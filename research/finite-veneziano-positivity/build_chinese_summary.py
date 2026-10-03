from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
p=Path(__file__).parent
pdfmetrics.registerFont(TTFont('NotoSansSCSummary', str(p/'presentation_fonts'/'ChineseSummary-Regular.ttf')))
styles={
 'title':ParagraphStyle('title',fontName='NotoSansSCSummary',fontSize=20,leading=28,spaceAfter=13,textColor=colors.black),
 'subtitle':ParagraphStyle('subtitle',fontName='NotoSansSCSummary',fontSize=12,leading=19,spaceAfter=17,textColor=colors.black),
 'heading':ParagraphStyle('heading',fontName='NotoSansSCSummary',fontSize=14,leading=22,spaceBefore=13,spaceAfter=7,textColor=colors.black),
 'body':ParagraphStyle('body',fontName='NotoSansSCSummary',fontSize=11,leading=18,spaceAfter=9,textColor=colors.black,wordWrap='CJK'),
 'small':ParagraphStyle('small',fontName='NotoSansSCSummary',fontSize=9,leading=14,spaceAfter=7,textColor=colors.black,wordWrap='CJK')}
story=[]
def P(s,kind='body'):story.append(Paragraph(s,styles[kind]))
def H(s):P(s,'heading')
P('有限 Veneziano 乘积的全自旋维数界','title')
P('中文执行摘要 / 版本 2<br/>潘奕成 / Yicheng Pan<br/>2026 年 10 月 3 日 / 公开 AI 辅助预印本','subtitle')
P('本版本把上一版的有限 n 结论推进为整个振幅家族的统一证明候选：对任意整数 n ≥ 3，所有能级、所有整数自旋的树级四点部分波正性，恰好成立于 3 &lt; D ≤ d<sub>n</sub>。这里 d<sub>n</sub> 是第 3 能级标量部分波的唯一零点。端点允许该系数等于零。')
H('一 从有限样本到任意 n')
P('上一版已证明第 3 能级的统一性质，并验证一组有限乘积。本版本没有依靠扩大样本来推断无限情形，而是找到固定宽度的解析机制：在 D = 51/5 = 10.2 时，相关中心阶乘多项式的所有部分波都非负，唯一例外正是对应第 3 能级的标量。')
P('将这一问题写成 Bessel 递推后，只有目标附近三步需要额外处理。精确展开得到一个含 182 项的整数多项式；每个非零系数都为正，最小系数为 2500，常数项为 3381984900。因此它一次性覆盖无限多个能级和自旋，无须逐个扫描。')
P('有限乘积的修正因子保持正性。结合 d<sub>n</sub> 严格下降，以及精确不等式 F<sub>35</sub>(10.2) &lt; -3/100000，可证明全部 n ≥ 35。剩余 n = 3 至 34 是经过解析缩减后的有限基础：560 个残差与 32 个维数上界均以精确有理数证书验证。两部分合起来覆盖任意 n。')
H('二 统一结论')
P('d<sub>n</sub> 在 10 与 14 之间唯一存在，随 n 严格下降到 10，并满足：<br/>d<sub>n</sub> = 10 + 72/(11n) + 13032/(1331n<super>2</super>) + O(n<super>-3</super>)。')
P('对整数维度 D ≥ 4，整个已指定振幅家族的正性范围为：<br/>n = 1、2：无维度上限；n = 3：D ≤ 13；n = 4：D ≤ 12；n = 5、6、7：D ≤ 11；n ≥ 8：D ≤ 10。')
P('这些数字描述四点振幅的正性阈值。它们不构成十三维新弦理论，也不改变既有弦理论的临界维数。原论文的数值表已提示这些转换；本版本的候选新增内容是统一证明。')
story.append(PageBreak())
P('既有方法与评审边界','title')
H('三 哪些属于先前工作')
P('Shao-Vichi 的 arXiv:2607.27300v2 已给出振幅家族、数值临界维数、标量公式和趋近 10 的极限。正幂级数的 Gegenbauer 正性方法、Bessel 表示以及低自旋主导的观察均有文献先例。')
P('本证明明确借鉴 Chen-Yin 的中心阶乘与“首次退出”方法；Arkani-Hamed、Eberhardt、Huang、Mizera 已研究相关 Bessel 表示；Mansfield 也已对另一类振幅使用“排除一个低能级后建立更高维正性”的策略。因此，这些思想与通用方法不作为原创性主张。')
P('有边界的当前文献排查尚未发现精确相同的 D = 51/5 不等式、182 项证书及本有限乘积家族的任意 n 定理。最稳妥的定位是值得专家评审的新证明候选，不能由此保证全球首创。')
H('四 已验证与尚未验证')
P('另行编写的 AI 生成检查重新推导了共轭微分方程和首次退出恒等式，并独立重放全部 560 个残差及 32 个上界。额外的对抗性检查不用计算机代数系统，以有理数稀疏多项式重建 182 个系数，并复核若干困难边界残差。关键检查未发现数学缺口。')
P('这些是 AI 辅助数学与计算交叉检查，不是人类专家审稿、同行评审或形式化证明助手认证。论文仍需要署名作者审阅、专家核查论证，并判断其原创性与学术意义。')
P('定理只涉及四点树级部分波正性。高点一致性、圈级幺正性、局域性、正范数态空间构造和物理紫外完备性均未由此证明。不能把这项结果直接称作完整弦理论突破。')
H('五 复现与下一步')
P('修订研究包包含英文 LaTeX 稿、中文摘要、完整固定多项式证书、有限基础证书及主程序与独立验证程序。所有关键符号判定采用精确算术，显示的小数仅方便阅读。初版文件已保留，修订不覆盖其历史。')
P('下一步最有价值的是专家复核和独立复现。数学上可继续寻找更直观的正性表示，减少有限基础计算，或求出排除第 3 能级后的最大统一余量。要进一步研究物理完备性，需要新的高点与圈级论证。')
P('本稿由 OpenAI AI 辅助研究、推导、写作和编程。本版本为公开预印本；任何投稿前仍须完成作者确认和相应披露。')

def footer(c,d):
 c.setFont('NotoSansSCSummary',9);c.drawString(51,34,'潘奕成 / Yicheng Pan / 公开 AI 辅助预印本 v2');c.drawRightString(A4[0]-51,34,str(d.page))
doc=SimpleDocTemplate(str(p/'finite_veneziano_summary_zh.pdf'),pagesize=A4,initialFontName='NotoSansSCSummary',rightMargin=51,leftMargin=51,topMargin=45,bottomMargin=52,title='有限 Veneziano 乘积的全自旋维数界 中文执行摘要',author='潘奕成 / Yicheng Pan')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('Created',p/'finite_veneziano_summary_zh.pdf')
