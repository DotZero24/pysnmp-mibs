_Bi='initReady'
_Bh='initStarted'
_Bg='rxBerLevel3'
_Bf='rxBerLevel2'
_Be='rxBerLevel1'
_Bd='electrical'
_Bc='tp10BaseT'
_Bb='tp100BaseT'
_Ba='tp1000BaseT'
_BZ='notPresent'
_BY='enabled'
_BX='normal'
_BW='ch918'
_BV='ch9175'
_BU='ch917'
_BT='ch9165'
_BS='ch916'
_BR='ch9155'
_BQ='ch915'
_BP='ch9145'
_BO='ch914'
_BN='ch9135'
_BM='transparent'
_BL='alarm'
_BK='disabled'
_BJ='ch961'
_BI='ch9605'
_BH='ch960'
_BG='ch9595'
_BF='ch959'
_BE='ch9585'
_BD='ch958'
_BC='ch9575'
_BB='ch957'
_BA='ch9565'
_B9='ch956'
_B8='ch9555'
_B7='ch955'
_B6='ch9545'
_B5='ch954'
_B4='ch9535'
_B3='ch953'
_B2='ch9525'
_B1='ch952'
_B0='ch9515'
_A_='ch951'
_Az='ch9505'
_Ay='ch950'
_Ax='ch9495'
_Aw='ch949'
_Av='ch9485'
_Au='ch948'
_At='ch9475'
_As='ch947'
_Ar='ch9465'
_Aq='ch946'
_Ap='ch9455'
_Ao='ch945'
_An='ch9445'
_Am='ch944'
_Al='ch9435'
_Ak='ch943'
_Aj='ch9425'
_Ai='ch942'
_Ah='ch9415'
_Ag='ch941'
_Af='ch9405'
_Ae='ch940'
_Ad='ch9395'
_Ac='ch939'
_Ab='ch9385'
_Aa='ch938'
_AZ='ch9375'
_AY='ch937'
_AX='ch9365'
_AW='ch936'
_AV='ch9355'
_AU='ch935'
_AT='ch9345'
_AS='ch934'
_AR='ch9335'
_AQ='ch933'
_AP='ch9325'
_AO='ch932'
_AN='ch9315'
_AM='ch931'
_AL='ch9305'
_AK='ch930'
_AJ='ch9295'
_AI='ch929'
_AH='ch9285'
_AG='ch928'
_AF='ch9275'
_AE='ch927'
_AD='ch9265'
_AC='ch926'
_AB='ch9255'
_AA='ch925'
_A9='ch9245'
_A8='ch924'
_A7='ch9235'
_A6='ch923'
_A5='ch9225'
_A4='ch922'
_A3='ch9215'
_A2='ch921'
_A1='ch9205'
_A0='ch920'
_z='ch9195'
_y='ch919'
_x='ch9185'
_w='ch909'
_v='ch907'
_u='ch905'
_t='ch903'
_s='ch901'
_r='ch899'
_q='ch897'
_p='ch895'
_o='ch893'
_n='ch891'
_m='ch889'
_l='ch887'
_k='ch885'
_j='ch883'
_i='ch881'
_h='ch879'
_g='ch877'
_f='ch875'
_e='ch873'
_d='ch871'
_c='w1610'
_b='w1590'
_a='w1570'
_Z='w1550'
_Y='w1530'
_X='w1510'
_W='w1490'
_V='w1470'
_U='w1450'
_T='w1430'
_S='w1410'
_R='w1390'
_Q='w1370'
_P='w1350'
_O='w1330'
_N='w1310'
_M='w1290'
_L='w1270'
_K='w850'
_J='b1500'
_I='b1300'
_H='255a'
_G='up'
_F='down'
_E='undefined'
_D='notAvailable'
_C='d'
_B='notApplicable'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,=mibBuilder.importSymbols('LUM-REG','lumModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lumTcModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,2))
if mibBuilder.loadTexts:lumTcModule.setRevisions(('2018-12-21 00:00','2018-06-29 00:00','2018-04-16 00:00','2017-06-15 00:00','2016-11-30 00:00','2015-11-30 00:00','2014-09-30 00:00','2014-05-16 00:00','2013-11-15 00:00','2013-05-01 00:00','2012-12-20 00:00','2011-12-20 00:00','2011-05-11 00:00','2005-07-07 00:00','2002-04-10 00:00','2002-03-05 00:00','2001-12-03 00:00','2001-10-23 00:00','2001-10-11 00:00','2001-09-04 00:00','2001-08-14 00:00','2001-08-09 00:00','2001-03-12 00:00'))
class MgmtNameString(TextualConvention,OctetString):status=_A;displayHint=_H;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class FaultStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_BL,2)))
class SubrackNumber(TextualConvention,Unsigned32):status=_A;displayHint=_C;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
class SlotNumber(TextualConvention,Unsigned32):status=_A;displayHint=_C;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,22))
class PortNumber(TextualConvention,Unsigned32):status=_A;displayHint=_C;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,116))
class SignalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uni',1),('biDi',2)))
class PortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rx',1),('tx',2),('biDi',3)))
class LambdaType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('fixed',1),('range',2),(_BM,3),('interleavedOdd',4),('interleavedEven',5),('interleaved50GHzOdd',6),('interleaved50GhzEven',7)))
class LambdaFrequency(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,130,150,850,1270,1290,1310,1330,1350,1370,1390,1410,1430,1450,1470,1490,1510,1530,1550,1570,1590,1610,18710,18730,18750,18770,18790,18810,18830,18850,18870,18890,18910,18930,18950,18970,18990,19010,19030,19050,19070,19090,19135,19140,19145,19150,19155,19160,19165,19170,19175,19180,19185,19190,19195,19200,19205,19210,19215,19220,19225,19230,19235,19240,19245,19250,19255,19260,19265,19270,19275,19280,19285,19290,19295,19300,19305,19310,19315,19320,19325,19330,19335,19340,19345,19350,19355,19360,19365,19370,19375,19380,19385,19390,19395,19400,19405,19410,19415,19420,19425,19430,19435,19440,19445,19450,19455,19460,19465,19470,19475,19480,19485,19490,19495,19500,19505,19510,19515,19520,19525,19530,19535,19540,19545,19550,19555,19560,19565,19570,19575,19580,19585,19590,19595,19600,19605,19610)));namedValues=NamedValues(*((_E,0),('iWdmPonFrequency',1),('otclg',2),(_I,130),(_J,150),(_K,850),(_L,1270),(_M,1290),(_N,1310),(_O,1330),(_P,1350),(_Q,1370),(_R,1390),(_S,1410),(_T,1430),(_U,1450),(_V,1470),(_W,1490),(_X,1510),(_Y,1530),(_Z,1550),(_a,1570),(_b,1590),(_c,1610),(_d,18710),(_e,18730),(_f,18750),(_g,18770),(_h,18790),(_i,18810),(_j,18830),(_k,18850),(_l,18870),(_m,18890),(_n,18910),(_o,18930),(_p,18950),(_q,18970),(_r,18990),(_s,19010),(_t,19030),(_u,19050),(_v,19070),(_w,19090),(_BN,19135),(_BO,19140),(_BP,19145),(_BQ,19150),(_BR,19155),(_BS,19160),(_BT,19165),(_BU,19170),(_BV,19175),(_BW,19180),(_x,19185),(_y,19190),(_z,19195),(_A0,19200),(_A1,19205),(_A2,19210),(_A3,19215),(_A4,19220),(_A5,19225),(_A6,19230),(_A7,19235),(_A8,19240),(_A9,19245),(_AA,19250),(_AB,19255),(_AC,19260),(_AD,19265),(_AE,19270),(_AF,19275),(_AG,19280),(_AH,19285),(_AI,19290),(_AJ,19295),(_AK,19300),(_AL,19305),(_AM,19310),(_AN,19315),(_AO,19320),(_AP,19325),(_AQ,19330),(_AR,19335),(_AS,19340),(_AT,19345),(_AU,19350),(_AV,19355),(_AW,19360),(_AX,19365),(_AY,19370),(_AZ,19375),(_Aa,19380),(_Ab,19385),(_Ac,19390),(_Ad,19395),(_Ae,19400),(_Af,19405),(_Ag,19410),(_Ah,19415),(_Ai,19420),(_Aj,19425),(_Ak,19430),(_Al,19435),(_Am,19440),(_An,19445),(_Ao,19450),(_Ap,19455),(_Aq,19460),(_Ar,19465),(_As,19470),(_At,19475),(_Au,19480),(_Av,19485),(_Aw,19490),(_Ax,19495),(_Ay,19500),(_Az,19505),(_A_,19510),(_B0,19515),(_B1,19520),(_B2,19525),(_B3,19530),(_B4,19535),(_B5,19540),(_B6,19545),(_B7,19550),(_B8,19555),(_B9,19560),(_BA,19565),(_BB,19570),(_BC,19575),(_BD,19580),(_BE,19585),(_BF,19590),(_BG,19595),(_BH,19600),(_BI,19605),(_BJ,19610)))
class BoardOrInterfaceAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('service',2),(_G,3)))
class BoardOrInterfaceOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_BZ,1),(_F,2),(_G,3)))
class CommandString(TextualConvention,OctetString):status=_A;displayHint=_H
class SignalFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,2147483647)));namedValues=NamedValues(*(('other',1),('stm1',2),('stm4',3),('stm16',4),('gbE',5),('stm64',6),('fc1Gb',7),('fc2Gb',8),('wan10GbE',9),('unused',10),('lan10GbE',11),('escon',12),('esconLL',13),('dvb270',14),('oc3',15),('oc12',16),('oc48',17),('oc192',18),('hdtv1485',19),('ethernet',20),('fastEthernet',21),('lan10GbEFec',22),('wan10GbEStm64Fec',23),('fc4Gb',24),('etr',25),('auto',26),(_F,27),('stm1Oc3',28),('stm4Oc12',29),('stm16Oc48',30),('stm64Oc192',31),('gbe9Line',32),('ddgbeLine',34),('gbEorTrm5500',35),('fc8Gb',36),('otu2',37),('otu2e',38),('e1',39),('t1',40),('mbh2Gb5',41),('syncE',42),('line4G',43),('mbh4Gbps',44),('fecLan10GbE1A',45),('fecLan10GbE1B',46),('sdi3G',47),('iWdm4G',48),('sdSdi270',49),('hdtvNTSC',50),('oc768',51),('stm256',52),('lan40GbE',53),('wan40GbE',54),('sfStm256Oc768',55),('iwdm40Gb',56),('otu4',57),('lan100GbE',58),('transpLan10GbE',59),('cpri1',60),('cpri2',61),('cpri3',62),('cpri4',63),('cpri5',64),('cpri6',65),('cpri7',66),('fc10Gb',67),('fc16Gb',68),('cpri8',69),('obsai1x',70),('obsai2x',71),('obsai4x',72),('obsai8x',73),('otu1',74),('iwdm11G',75),('rw100G',76),('rw200G',77),('otu4SdFec',78),('otuj1',79),('otuj2',80),(_B,2147483647)))
class TrxMedia(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),('optical',1),(_Ba,2),(_Bb,3),(_Bc,4),(_Bd,5)))
class OtnMonitorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sm',0),('pm',1),('tcm',2)))
class OtnMonitorConfig(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('terminated',0),(_BM,1)))
class OtnTIMDetMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sapi',0),('dapi',1),('both',2)))
class ObjectProperty(TextualConvention,Unsigned32):status=_A;displayHint=_C;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class PmReset(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_BX,1),('reset',2)))
class EnableDisable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_BK,1),(_BY,2)))
class SyncSourceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_BX,1),('failed',2),('waitToRestore',3)))
class SyncSourceMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_BK,0),(_BY,1),('lockedOut',2)))
class AdminStatusWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,2147483647)));namedValues=NamedValues(*((_F,1),('service',2),(_G,3),(_B,2147483647)))
class OperStatusWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,2147483647)));namedValues=NamedValues(*((_BZ,1),(_F,2),(_G,3),(_B,2147483647)))
class SignalStatusWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,2147483647)));namedValues=NamedValues(*((_F,1),('degraded',2),(_G,3),(_B,2147483647)))
class Unsigned32WithNA(TextualConvention,Unsigned32):status=_A;displayHint=_C;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967292),ValueRangeConstraint(4294967293,4294967293),ValueRangeConstraint(4294967294,4294967294))
class EnabledDisabledWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*((_BK,1),(_BY,2),(_B,2147483647)))
class Layer(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483646),ValueRangeConstraint(2147483647,2147483647))
class Time7200min(TextualConvention,Integer32):status=_A;displayHint=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200),ValueRangeConstraint(2147483647,2147483647))
class Time7200minNo0(TextualConvention,Integer32):status=_A;displayHint=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200),ValueRangeConstraint(2147483647,2147483647))
class Integer32WithNA(TextualConvention,Integer32):status=_A;displayHint=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483645),ValueRangeConstraint(2147483646,2147483646),ValueRangeConstraint(2147483647,2147483647))
class Activated(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('activated',1),('deactivated',2),(_B,2147483647)))
class ResetWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('reset',1),(_BX,2),(_B,2147483647)))
class FaultStatusWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ok',1),(_BL,2),(_B,2147483647)))
class MgmtNameStringWithNA(TextualConvention,OctetString):status=_A;displayHint=_H;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class DisplayStringWithNA(TextualConvention,OctetString):status=_A;displayHint=_H;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SignalStructure(TextualConvention,Integer32):status='deprecated';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,2147483647)));namedValues=NamedValues(*(('phyTrxOptOtsOptOchOtnOtuOtnOduOtnmonSmOtnmonPm',1),('phyTrxOptOtsOptOchSdhRsSdhMs',2),('phyTrxOptOtsOptOchSonetSectionSonetLine',3),('phyTrxOptOtsOptOchEthPhys',4),(_B,2147483647)))
class Signed32WithNA(TextualConvention,Integer32):status=_A;displayHint=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483645),ValueRangeConstraint(2147483646,2147483646),ValueRangeConstraint(2147483647,2147483647))
class LaserMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('forcedOn',1),('als',2),(_B,2147483647)))
class OnOff(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483646,2147483647)));namedValues=NamedValues(*(('off',1),('on',2),(_D,2147483646),(_B,2147483647)))
class LaneFrequency(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,130,150,850,1270,1290,1297,1301,1305,1309,1310,1330,1350,1370,1390,1410,1430,1450,1470,1490,1510,1523,1530,1531,1539,1547,1550,1555,1563,1570,1571,1579,1587,1590,1595,1610,18710,18730,18750,18770,18790,18810,18830,18850,18870,18890,18910,18930,18950,18970,18990,19010,19030,19050,19070,19090,19185,19190,19195,19200,19205,19210,19215,19220,19225,19230,19235,19240,19245,19250,19255,19260,19265,19270,19275,19280,19285,19290,19295,19300,19305,19310,19315,19320,19325,19330,19335,19340,19345,19350,19355,19360,19365,19370,19375,19380,19385,19390,19395,19400,19405,19410,19415,19420,19425,19430,19435,19440,19445,19450,19455,19460,19465,19470,19475,19480,19485,19490,19495,19500,19505,19510,19515,19520,19525,19530,19535,19540,19545,19550,19555,19560,19565,19570,19575,19580,19585,19590,19595,19600,19605,19610,2147483646,2147483647)));namedValues=NamedValues(*((_E,0),(_I,130),(_J,150),(_K,850),(_L,1270),(_M,1290),('w1297',1297),('w1301',1301),('w1305',1305),('w1309',1309),(_N,1310),(_O,1330),(_P,1350),(_Q,1370),(_R,1390),(_S,1410),(_T,1430),(_U,1450),(_V,1470),(_W,1490),(_X,1510),('w1523',1523),(_Y,1530),('w1531',1531),('w1539',1539),('w1547',1547),(_Z,1550),('w1555',1555),('w1563',1563),(_a,1570),('w1571',1571),('w1579',1579),('w1587',1587),(_b,1590),('w1595',1595),(_c,1610),(_d,18710),(_e,18730),(_f,18750),(_g,18770),(_h,18790),(_i,18810),(_j,18830),(_k,18850),(_l,18870),(_m,18890),(_n,18910),(_o,18930),(_p,18950),(_q,18970),(_r,18990),(_s,19010),(_t,19030),(_u,19050),(_v,19070),(_w,19090),(_x,19185),(_y,19190),(_z,19195),(_A0,19200),(_A1,19205),(_A2,19210),(_A3,19215),(_A4,19220),(_A5,19225),(_A6,19230),(_A7,19235),(_A8,19240),(_A9,19245),(_AA,19250),(_AB,19255),(_AC,19260),(_AD,19265),(_AE,19270),(_AF,19275),(_AG,19280),(_AH,19285),(_AI,19290),(_AJ,19295),(_AK,19300),(_AL,19305),(_AM,19310),(_AN,19315),(_AO,19320),(_AP,19325),(_AQ,19330),(_AR,19335),(_AS,19340),(_AT,19345),(_AU,19350),(_AV,19355),(_AW,19360),(_AX,19365),(_AY,19370),(_AZ,19375),(_Aa,19380),(_Ab,19385),(_Ac,19390),(_Ad,19395),(_Ae,19400),(_Af,19405),(_Ag,19410),(_Ah,19415),(_Ai,19420),(_Aj,19425),(_Ak,19430),(_Al,19435),(_Am,19440),(_An,19445),(_Ao,19450),(_Ap,19455),(_Aq,19460),(_Ar,19465),(_As,19470),(_At,19475),(_Au,19480),(_Av,19485),(_Aw,19490),(_Ax,19495),(_Ay,19500),(_Az,19505),(_A_,19510),(_B0,19515),(_B1,19520),(_B2,19525),(_B3,19530),(_B4,19535),(_B5,19540),(_B6,19545),(_B7,19550),(_B8,19555),(_B9,19560),(_BA,19565),(_BB,19570),(_BC,19575),(_BD,19580),(_BE,19585),(_BF,19590),(_BG,19595),(_BH,19600),(_BI,19605),(_BJ,19610),(_D,2147483646),(_B,2147483647)))
class Frequency(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,130,150,850,1270,1290,1310,1330,1350,1370,1390,1410,1430,1450,1470,1490,1510,1530,1550,1570,1590,1610,18710,18730,18750,18770,18790,18810,18830,18850,18870,18890,18910,18930,18950,18970,18990,19010,19030,19050,19070,19090,19135,19140,19145,19150,19155,19160,19165,19170,19175,19180,19185,19190,19195,19200,19205,19210,19215,19220,19225,19230,19235,19240,19245,19250,19255,19260,19265,19270,19275,19280,19285,19290,19295,19300,19305,19310,19315,19320,19325,19330,19335,19340,19345,19350,19355,19360,19365,19370,19375,19380,19385,19390,19395,19400,19405,19410,19415,19420,19425,19430,19435,19440,19445,19450,19455,19460,19465,19470,19475,19480,19485,19490,19495,19500,19505,19510,19515,19520,19525,19530,19535,19540,19545,19550,19555,19560,19565,19570,19575,19580,19585,19590,19595,19600,19605,19610,2147483646,2147483647)));namedValues=NamedValues(*((_E,0),(_I,130),(_J,150),(_K,850),(_L,1270),(_M,1290),(_N,1310),(_O,1330),(_P,1350),(_Q,1370),(_R,1390),(_S,1410),(_T,1430),(_U,1450),(_V,1470),(_W,1490),(_X,1510),(_Y,1530),(_Z,1550),(_a,1570),(_b,1590),(_c,1610),(_d,18710),(_e,18730),(_f,18750),(_g,18770),(_h,18790),(_i,18810),(_j,18830),(_k,18850),(_l,18870),(_m,18890),(_n,18910),(_o,18930),(_p,18950),(_q,18970),(_r,18990),(_s,19010),(_t,19030),(_u,19050),(_v,19070),(_w,19090),(_BN,19135),(_BO,19140),(_BP,19145),(_BQ,19150),(_BR,19155),(_BS,19160),(_BT,19165),(_BU,19170),(_BV,19175),(_BW,19180),(_x,19185),(_y,19190),(_z,19195),(_A0,19200),(_A1,19205),(_A2,19210),(_A3,19215),(_A4,19220),(_A5,19225),(_A6,19230),(_A7,19235),(_A8,19240),(_A9,19245),(_AA,19250),(_AB,19255),(_AC,19260),(_AD,19265),(_AE,19270),(_AF,19275),(_AG,19280),(_AH,19285),(_AI,19290),(_AJ,19295),(_AK,19300),(_AL,19305),(_AM,19310),(_AN,19315),(_AO,19320),(_AP,19325),(_AQ,19330),(_AR,19335),(_AS,19340),(_AT,19345),(_AU,19350),(_AV,19355),(_AW,19360),(_AX,19365),(_AY,19370),(_AZ,19375),(_Aa,19380),(_Ab,19385),(_Ac,19390),(_Ad,19395),(_Ae,19400),(_Af,19405),(_Ag,19410),(_Ah,19415),(_Ai,19420),(_Aj,19425),(_Ak,19430),(_Al,19435),(_Am,19440),(_An,19445),(_Ao,19450),(_Ap,19455),(_Aq,19460),(_Ar,19465),(_As,19470),(_At,19475),(_Au,19480),(_Av,19485),(_Aw,19490),(_Ax,19495),(_Ay,19500),(_Az,19505),(_A_,19510),(_B0,19515),(_B1,19520),(_B2,19525),(_B3,19530),(_B4,19535),(_B5,19540),(_B6,19545),(_B7,19550),(_B8,19555),(_B9,19560),(_BA,19565),(_BB,19570),(_BC,19575),(_BD,19580),(_BE,19585),(_BF,19590),(_BG,19595),(_BH,19600),(_BI,19605),(_BJ,19610),(_D,2147483646),(_B,2147483647)))
class FrequencyOnlyNotApplicable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,130,150,850,1270,1290,1310,1330,1350,1370,1390,1410,1430,1450,1470,1490,1510,1530,1550,1570,1590,1610,18710,18730,18750,18770,18790,18810,18830,18850,18870,18890,18910,18930,18950,18970,18990,19010,19030,19050,19070,19090,19135,19140,19145,19150,19155,19160,19165,19170,19175,19180,19185,19190,19195,19200,19205,19210,19215,19220,19225,19230,19235,19240,19245,19250,19255,19260,19265,19270,19275,19280,19285,19290,19295,19300,19305,19310,19315,19320,19325,19330,19335,19340,19345,19350,19355,19360,19365,19370,19375,19380,19385,19390,19395,19400,19405,19410,19415,19420,19425,19430,19435,19440,19445,19450,19455,19460,19465,19470,19475,19480,19485,19490,19495,19500,19505,19510,19515,19520,19525,19530,19535,19540,19545,19550,19555,19560,19565,19570,19575,19580,19585,19590,19595,19600,19605,19610,2147483647)));namedValues=NamedValues(*((_E,0),(_I,130),(_J,150),(_K,850),(_L,1270),(_M,1290),(_N,1310),(_O,1330),(_P,1350),(_Q,1370),(_R,1390),(_S,1410),(_T,1430),(_U,1450),(_V,1470),(_W,1490),(_X,1510),(_Y,1530),(_Z,1550),(_a,1570),(_b,1590),(_c,1610),(_d,18710),(_e,18730),(_f,18750),(_g,18770),(_h,18790),(_i,18810),(_j,18830),(_k,18850),(_l,18870),(_m,18890),(_n,18910),(_o,18930),(_p,18950),(_q,18970),(_r,18990),(_s,19010),(_t,19030),(_u,19050),(_v,19070),(_w,19090),(_BN,19135),(_BO,19140),(_BP,19145),(_BQ,19150),(_BR,19155),(_BS,19160),(_BT,19165),(_BU,19170),(_BV,19175),(_BW,19180),(_x,19185),(_y,19190),(_z,19195),(_A0,19200),(_A1,19205),(_A2,19210),(_A3,19215),(_A4,19220),(_A5,19225),(_A6,19230),(_A7,19235),(_A8,19240),(_A9,19245),(_AA,19250),(_AB,19255),(_AC,19260),(_AD,19265),(_AE,19270),(_AF,19275),(_AG,19280),(_AH,19285),(_AI,19290),(_AJ,19295),(_AK,19300),(_AL,19305),(_AM,19310),(_AN,19315),(_AO,19320),(_AP,19325),(_AQ,19330),(_AR,19335),(_AS,19340),(_AT,19345),(_AU,19350),(_AV,19355),(_AW,19360),(_AX,19365),(_AY,19370),(_AZ,19375),(_Aa,19380),(_Ab,19385),(_Ac,19390),(_Ad,19395),(_Ae,19400),(_Af,19405),(_Ag,19410),(_Ah,19415),(_Ai,19420),(_Aj,19425),(_Ak,19430),(_Al,19435),(_Am,19440),(_An,19445),(_Ao,19450),(_Ap,19455),(_Aq,19460),(_Ar,19465),(_As,19470),(_At,19475),(_Au,19480),(_Av,19485),(_Aw,19490),(_Ax,19495),(_Ay,19500),(_Az,19505),(_A_,19510),(_B0,19515),(_B1,19520),(_B2,19525),(_B3,19530),(_B4,19535),(_B5,19540),(_B6,19545),(_B7,19550),(_B8,19555),(_B9,19560),(_BA,19565),(_BB,19570),(_BC,19575),(_BD,19580),(_BE,19585),(_BF,19590),(_BG,19595),(_BH,19600),(_BI,19605),(_BJ,19610),(_B,2147483647)))
class Rate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483646,2147483647)));namedValues=NamedValues(*(('sdh156',1),('sdh2488',2),(_D,2147483646),(_B,2147483647)))
class TrxMediaWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,2147483646,2147483647)));namedValues=NamedValues(*((_E,0),('optical',1),(_Ba,2),(_Bb,3),(_Bc,4),(_Bd,5),(_D,2147483646),(_B,2147483647)))
class FecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,2147483647)));namedValues=NamedValues(*((_BK,0),('g709',1),('g9751I4',2),('g9751I7',3),('sdFec',4),(_B,2147483647)))
class TruthValueWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2147483646,2147483647)));namedValues=NamedValues(*(('true',0),('false',1),(_D,2147483646),(_B,2147483647)))
class TcmMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*(('operational',0),(_BM,1),('monitor',2),(_B,2147483647)))
class TcmNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,2147483647)));namedValues=NamedValues(*(('tcm1',0),('tcm2',1),('tcm3',2),('tcm4',3),('tcm5',4),('tcm6',5),(_B,2147483647)))
class OtnTIMDetModeWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,2147483647)));namedValues=NamedValues(*(('off',0),('sapi',1),('dapi',2),('both',3),(_B,2147483647)))
class OtnDirectionWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*(('none',0),('rx',1),('tx',2),(_B,2147483647)))
class OtnAlarmMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*(('ignore',0),(_BL,1),('display',2),(_B,2147483647)))
class CcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*(('addDrop',0),('broadcast',1),('select',2),(_B,2147483647)))
class AutoNegotiationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,2147483646,2147483647)));namedValues=NamedValues(*(('incomplete',1),('halfDuplex',2),('fullDuplex',3),('halfDuplexRxPauseOn',4),('halfDuplexTxPauseOn',5),('halfDuplexRxTxPauseOn',6),('fullDuplexRxPauseOn',7),('fullDuplexTxPauseOn',8),('fullDuplexRxTxPauseOn',9),('fullDuplexFec',10),('fec',11),(_D,2147483646),(_B,2147483647)))
class FlowControlMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,2147483647)));namedValues=NamedValues(*(('noPause',1),('rxPause',2),('txPause',3),('bothPause',4),(_B,2147483647)))
class OtnType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sm',0),('tcm',1),('pm',2)))
class OtnTypeWithNA(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,2147483646,2147483647)));namedValues=NamedValues(*(('sm',0),('pm',1),('tcm1',2),('tcm2',3),('tcm3',4),('tcm4',5),('tcm5',6),('tcm6',7),(_D,2147483646),(_B,2147483647)))
class AuType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('au4Type64c',0),('au4Type16c',1),('au4Type4c',2),('au4',3),('au3',4)))
class VcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('vc4Type64c',0),('vc4Type16c',1),('vc4Type4c',2),('vc4',3),('vc3',4)))
class StsType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('stsType192c',0),('stsType48c',1),('stsType3c',2),('sts3',3),('sts1',4)))
class StsSpeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('sts192cSpe',0),('sts48cSpe',1),('sts12cSpe',2),('sts3cSpe',3),('sts1Spe',4)))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
class BerLevelMTOSI(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,12,13,15)));namedValues=NamedValues(*(('osnrMargin1',5),('osnrMargin2',10),(_Be,12),(_Bf,13),(_Bg,15)))
class BerLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(12,13,15)));namedValues=NamedValues(*((_Be,12),(_Bf,13),(_Bg,15)))
class AutoAlarmStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,2147483647)));namedValues=NamedValues(*(('suppressTrxAndSignal',1),('suppressSignal',2),('suppressNone',3),(_B,2147483647)))
class InterfaceStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,2147483647)));namedValues=NamedValues(*(('outOfService',1),('autoInService',2),('inService',3),('maintenance',4),(_B,2147483647)))
class OpticalLayerMappingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('fourOpticalLanes',1),('tenOpticalLanes',2),('singleOpticalChannel',3)))
class PhysicalLayerMappingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dualFiber',1),('singleFiber',2)))
class TribPortIdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,2147483647)));namedValues=NamedValues(*(('unused',0),('tp1',1),('tp2',2),('tp3',3),('tp4',4),('tp5',5),('tp6',6),('tp7',7),('tp8',8),('tp9',9),('tp10',10),('tp11',11),(_B,2147483647)))
class ServiceIdWithNotUsed(TextualConvention,Integer32):status=_A;displayHint=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
class TrxRxState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,2147483647)));namedValues=NamedValues(*(('missing',0),(_Bh,1),(_Bi,2),('frequencyReady',3),('inputSignalReceived',4),('adConverterReady',5),('dispersionCompensated',6),('ready',7),(_B,2147483647)))
class TrxTxState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,2147483647)));namedValues=NamedValues(*(('missing',0),(_Bh,1),(_Bi,2),('dataPathLocked',3),('laserReadyOff',4),('laserReady',5),('laserBiasReady',6),('ready',7),(_B,2147483647)))
class DispersionSearchLimit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(22500,30000)));namedValues=NamedValues(*(('medium',22500),('high',30000)))
class SignalDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,2147483646)));namedValues=NamedValues(*(('rx',1),('tx',2),('biDir',3),('txRx',4),(_D,2147483646)))
class RsFecMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forcedOff',0),('forcedOn',1),('auto',2)))
class RsFecOnOff(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),(_E,2)))
class MplsLabel(TextualConvention,Unsigned32):status=_A;displayHint=_C;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
class InterfaceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,2147483646,2147483647)));namedValues=NamedValues(*(('individual',1),('bundled',2),('bundledSplit',3),(_D,2147483646),(_B,2147483647)))
class ConnectorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('connector4x10Gb',1),('connector1x100Gb',2),(_B,2147483647)))
class Platform(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('unknown',0),('cuosc',1),('cusfpv1',2),('cusfpv2',3),('cusfpv3',4),('culessTU1',5),('culessTU2',6),('culessTU3',7),('culessTU4',8),('pizzaboxFHA1UDC',9),('pizzaboxEMXP1UDC',10),('pizzaboxHDEA1600',11)))
mibBuilder.exportSymbols('LUM-TC',**{'MgmtNameString':MgmtNameString,'FaultStatus':FaultStatus,'SubrackNumber':SubrackNumber,'SlotNumber':SlotNumber,'PortNumber':PortNumber,'SignalType':SignalType,'PortType':PortType,'LambdaType':LambdaType,'LambdaFrequency':LambdaFrequency,'BoardOrInterfaceAdminStatus':BoardOrInterfaceAdminStatus,'BoardOrInterfaceOperStatus':BoardOrInterfaceOperStatus,'CommandString':CommandString,'SignalFormat':SignalFormat,'TrxMedia':TrxMedia,'OtnMonitorType':OtnMonitorType,'OtnMonitorConfig':OtnMonitorConfig,'OtnTIMDetMode':OtnTIMDetMode,'ObjectProperty':ObjectProperty,'PmReset':PmReset,'EnableDisable':EnableDisable,'SyncSourceState':SyncSourceState,'SyncSourceMode':SyncSourceMode,'AdminStatusWithNA':AdminStatusWithNA,'OperStatusWithNA':OperStatusWithNA,'SignalStatusWithNA':SignalStatusWithNA,'Unsigned32WithNA':Unsigned32WithNA,'EnabledDisabledWithNA':EnabledDisabledWithNA,'Layer':Layer,'Time7200min':Time7200min,'Time7200minNo0':Time7200minNo0,'Integer32WithNA':Integer32WithNA,'Activated':Activated,'ResetWithNA':ResetWithNA,'FaultStatusWithNA':FaultStatusWithNA,'MgmtNameStringWithNA':MgmtNameStringWithNA,'DisplayStringWithNA':DisplayStringWithNA,'SignalStructure':SignalStructure,'Signed32WithNA':Signed32WithNA,'LaserMode':LaserMode,'OnOff':OnOff,'LaneFrequency':LaneFrequency,'Frequency':Frequency,'FrequencyOnlyNotApplicable':FrequencyOnlyNotApplicable,'Rate':Rate,'TrxMediaWithNA':TrxMediaWithNA,'FecType':FecType,'TruthValueWithNA':TruthValueWithNA,'TcmMode':TcmMode,'TcmNumber':TcmNumber,'OtnTIMDetModeWithNA':OtnTIMDetModeWithNA,'OtnDirectionWithNA':OtnDirectionWithNA,'OtnAlarmMode':OtnAlarmMode,'CcType':CcType,'AutoNegotiationStatus':AutoNegotiationStatus,'FlowControlMode':FlowControlMode,'OtnType':OtnType,'OtnTypeWithNA':OtnTypeWithNA,'AuType':AuType,'VcType':VcType,'StsType':StsType,'StsSpeType':StsSpeType,'AdminStatus':AdminStatus,'BerLevelMTOSI':BerLevelMTOSI,'BerLevel':BerLevel,'AutoAlarmStatus':AutoAlarmStatus,'InterfaceStatus':InterfaceStatus,'OpticalLayerMappingType':OpticalLayerMappingType,'PhysicalLayerMappingType':PhysicalLayerMappingType,'TribPortIdType':TribPortIdType,'ServiceIdWithNotUsed':ServiceIdWithNotUsed,'TrxRxState':TrxRxState,'TrxTxState':TrxTxState,'DispersionSearchLimit':DispersionSearchLimit,'SignalDirection':SignalDirection,'RsFecMode':RsFecMode,'RsFecOnOff':RsFecOnOff,'MplsLabel':MplsLabel,'InterfaceType':InterfaceType,'ConnectorType':ConnectorType,'Platform':Platform,'lumTcModule':lumTcModule})