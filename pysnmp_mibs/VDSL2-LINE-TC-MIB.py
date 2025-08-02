_AR='sixteenSymbols'
_AQ='fifteenSymbols'
_AP='fourteenSymbols'
_AO='thirteeSymbols'
_AN='twelveSymbols'
_AM='elevenSymbols'
_AL='tenSymbols'
_AK='nineSymbols'
_AJ='eightSymbols'
_AI='sevenSymbols'
_AH='sixSymbols'
_AG='fiveSymbols'
_AF='fourSymbols'
_AE='threeSymbols'
_AD='twoSymbols'
_AC='singleSymbol'
_AB='noProtection'
_AA='noResources'
_A9='unsupported'
_A8='inProgress'
_A7='g9932AnnexC'
_A6='g9932AnnexB'
_A5='g9932AnnexA'
_A4='reserved12'
_A3='g9925AnnexMPotsOverlapped'
_A2='g9925AnnexMPotsNonOverlapped'
_A1='g9925AnnexJAllDigOverlapped'
_A0='g9925AnnexJAllDigNonOverlapped'
_z='g9925AnnexIAllDigOverlapped'
_y='g9925AnnexIAllDigNonOverlapped'
_x='reserved11'
_w='reserved10'
_v='g9925isdnOverlapped'
_u='g9925IsdnNonOverlapped'
_t='g9925PotsOverlapped'
_s='g9925PotsNonOverlapped'
_r='g9923AnnexMPotsOverlapped'
_q='g9923AnnexMPotsNonOverlapped'
_p='g9923AnnexLMode4Overlapped'
_o='g9923AnnexLMode3Overlapped'
_n='g9923AnnexLMode2NonOverlapped'
_m='g9923AnnexLMode1NonOverlapped'
_l='g9924AnnexIAllDigOverlapped'
_k='g9924AnnexIAllDigNonOverlapped'
_j='g9923AnnexJAllDigOverlapped'
_i='g9923AnnexJAllDigNonOverlapped'
_h='g9923AnnexIAllDigOverlapped'
_g='g9923AnnexIAllDigNonOverlapped'
_f='reserved9'
_e='reserved8'
_d='g9924potsOverlapped'
_c='g9924potsNonOverlapped'
_b='reserved7'
_a='reserved6'
_Z='g9923isdnOverlapped'
_Y='g9923IsdnNonOverlapped'
_X='g9923PotsOverlapped'
_W='g9923PotsNonOverlapped'
_V='reserved5'
_U='reserved4'
_T='reserved3'
_S='reserved2'
_R='reserved1'
_Q='g9921tcmIsdnSymmetric'
_P='g9922tcmIsdnOverlapped'
_O='g9922tcmIsdnNonOverlapped'
_N='g9922potsOverlapped'
_M='g9922potsNonOverlapped'
_L='g9921tcmIsdnOverlapped'
_K='g9921tcmIsdnNonOverlapped'
_J='g9921isdnOverlapped'
_I='g9921IsdnNonOverlapped'
_H='g9921PotsOverlapped'
_G='g9921PotsNonOverlapped'
_F='ansit1413'
_E='downstream'
_D='upstream'
_C='noDefect'
_B='none'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vdsl2TCMIB=ModuleIdentity((1,3,6,1,2,1,10,251,3))
if mibBuilder.loadTexts:vdsl2TCMIB.setRevisions(('2009-09-30 00:00',))
class Xdsl2Unit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('xtuc',1),('xtur',2)))
class Xdsl2Direction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
class Xdsl2Band(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_D,1),(_E,2),('us0',3),('ds1',4),('us1',5),('ds2',6),('us2',7),('ds3',8),('us3',9),('ds4',10),('us4',11)))
class Xdsl2TransmissionModeType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_F,0),('etsi',1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),(_P,11),(_Q,12),(_R,13),(_S,14),(_T,15),(_U,16),(_V,17),(_W,18),(_X,19),(_Y,20),(_Z,21),(_a,22),(_b,23),(_c,24),(_d,25),(_e,26),(_f,27),(_g,28),(_h,29),(_i,30),(_j,31),(_k,32),(_l,33),(_m,34),(_n,35),(_o,36),(_p,37),(_q,38),(_r,39),(_s,40),(_t,41),(_u,42),(_v,43),(_w,44),(_x,45),(_y,46),(_z,47),(_A0,48),(_A1,49),(_A2,50),(_A3,51),(_A4,52),('reserved13',53),('reserved14',54),('reserved15',55),(_A5,56),(_A6,57),(_A7,58),('reserved16',59),('reserved17',60),('reserved18',61),('reserved19',62),('reserved20',63)))
class Xdsl2RaMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('raInit',2),('dynamicRa',3)))
class Xdsl2InitResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noFail',0),('configError',1),('configNotFeasible',2),('commFail',3),('noPeerAtu',4),('otherCause',5)))
class Xdsl2OperationModes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,20,21,22,23,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,48,49,50,51,52,53,58,59,60)));namedValues=NamedValues(*(('defMode',1),(_F,2),('etsi',3),(_G,4),(_H,5),(_I,6),(_J,7),(_K,8),(_L,9),(_M,10),(_N,11),(_O,12),(_P,13),(_Q,14),(_W,20),(_X,21),(_Y,22),(_Z,23),(_c,26),(_d,27),(_g,30),(_h,31),(_i,32),(_j,33),(_k,34),(_l,35),(_m,36),(_n,37),(_o,38),(_p,39),(_q,40),(_r,41),(_s,42),(_t,43),(_u,44),(_v,45),(_y,48),(_z,49),(_A0,50),(_A1,51),(_A2,52),(_A3,53),(_A5,58),(_A6,59),(_A7,60)))
class Xdsl2PowerMngState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('l0',1),('l1',2),('l2',3),('l3',4)))
class Xdsl2ConfPmsForce(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('l3toL0',0),('l0toL2',2),('l0orL2toL3',3)))
class Xdsl2LinePmMode(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('allowTransitionsToIdle',0),('allowTransitionsToLowPower',1)))
class Xdsl2LineLdsf(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inhibit',0),('force',1)))
class Xdsl2LdsfResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_B,1),('success',2),(_A8,3),(_A9,4),('cannotRun',5),('aborted',6),('failed',7),('illegalMode',8),('adminUp',9),('tableFull',10),(_AA,11)))
class Xdsl2LineBpsc(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('measure',2)))
class Xdsl2BpscResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_B,1),('success',2),(_A8,3),(_A9,4),('failed',5),(_AA,6)))
class Xdsl2LineReset(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('reset',2)))
class Xdsl2LineProfiles(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('profile8a',0),('profile8b',1),('profile8c',2),('profile8d',3),('profile12a',4),('profile12b',5),('profile17a',6),('profile30a',7)))
class Xdsl2LineClassMask(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_B,1),('a998ORb997M1cORc998B',2),('b997M1xOR998co',3),('b997M2x',4),('b998M1x',5),('b998M2x',6),('b998AdeM2x',7),('bHpeM1',8)))
class Xdsl2LineLimitMask(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('profile8Limit1',0),('profile8Limit2',1),('profile8Limit3',2),('profile8Limit4',3),('profile8Limit5',4),('profile8Limit6',5),('profile8Limit7',6),('profile8Limit8',7),('profile8Limit9',8),('profile8Limit10',9),('profile8Limit11',10),('profile8Limit12',11),('profile8Limit13',12),('profile8Limit14',13),('profile8Limit15',14),('profile8Limit16',15),('profile12Limit1',16),('profile12Limit2',17),('profile12Limit3',18),('profile12Limit4',19),('profile12Limit5',20),('profile12Limit6',21),('profile12Limit7',22),('profile12Limit8',23),('profile12Limit9',24),('profile12Limit10',25),('profile12Limit11',26),('profile12Limit12',27),('profile12Limit13',28),('profile12Limit14',29),('profile12Limit15',30),('profile12Limit16',31),('profile17Limit1',32),('profile17Limit2',33),('profile17Limit3',34),('profile17Limit4',35),('profile17Limit5',36),('profile17Limit6',37),('profile17Limit7',38),('profile17Limit8',39),('profile17Limit9',40),('profile17Limit10',41),('profile17Limit11',42),('profile17Limit12',43),('profile17Limit13',44),('profile17Limit14',45),('profile17Limit15',46),('profile17Limit16',47),('profile30Limit1',48),('profile30Limit2',49),('profile30Limit3',50),('profile30Limit4',51),('profile30Limit5',52),('profile30Limit6',53),('profile30Limit7',54),('profile30Limit8',55),('profile30Limit9',56),('profile30Limit10',57),('profile30Limit11',58),('profile30Limit12',59),('profile30Limit13',60),('profile30Limit14',61),('profile30Limit15',62),('profile30Limit16',63)))
class Xdsl2LineUs0Disable(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('profile8Us0Disable1',0),('profile8Us0Disable2',1),('profile8Us0Disable3',2),('profile8Us0Disable4',3),('profile8Us0Disable5',4),('profile8Us0Disable6',5),('profile8Us0Disable7',6),('profile8Us0Disable8',7),('profile8Us0Disable9',8),('profile8Us0Disable10',9),('profile8Us0Disable11',10),('profile8Us0Disable12',11),('profile8Us0Disable13',12),('profile8Us0Disable14',13),('profile8Us0Disable15',14),('profile8Us0Disable16',15),('profile12Us0Disable1',16),('profile12Us0Disable2',17),('profile12Us0Disable3',18),('profile12Us0Disable4',19),('profile12Us0Disable5',20),('profile12Us0Disable6',21),('profile12Us0Disable7',22),('profile12Us0Disable8',23),('profile12Us0Disable9',24),('profile12Us0Disable10',25),('profile12Us0Disable11',26),('profile12Us0Disable12',27),('profile12Us0Disable13',28),('profile12Us0Disable14',29),('profile12Us0Disable15',30),('profile12Us0Disable16',31),('profile17Us0Disable1',32),('profile17Us0Disable2',33),('profile17Us0Disable3',34),('profile17Us0Disable4',35),('profile17Us0Disable5',36),('profile17Us0Disable6',37),('profile17Us0Disable7',38),('profile17Us0Disable8',39),('profile17Us0Disable9',40),('profile17Us0Disable10',41),('profile17Us0Disable11',42),('profile17Us0Disable12',43),('profile17Us0Disable13',44),('profile17Us0Disable14',45),('profile17Us0Disable15',46),('profile17Us0Disable16',47),('profile30Us0Disable1',48),('profile30Us0Disable2',49),('profile30Us0Disable3',50),('profile30Us0Disable4',51),('profile30Us0Disable5',52),('profile30Us0Disable6',53),('profile30Us0Disable7',54),('profile30Us0Disable8',55),('profile30Us0Disable9',56),('profile30Us0Disable10',57),('profile30Us0Disable11',58),('profile30Us0Disable12',59),('profile30Us0Disable13',60),('profile30Us0Disable14',61),('profile30Us0Disable15',62),('profile30Us0Disable16',63)))
class Xdsl2LineUs0Mask(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('eu32',0),('eu36',1),('eu40',2),('eu44',3),('eu48',4),('eu52',5),('eu56',6),('eu60',7),('eu64',8),('eu128',9),(_R,10),(_S,11),(_T,12),(_U,13),(_V,14),(_a,15),('adlu32',16),('adlu36',17),('adlu40',18),('adlu44',19),('adlu48',20),('adlu52',21),('adlu56',22),('adlu60',23),('adlu64',24),('adlu128',25),(_b,26),(_e,27),(_f,28),(_w,29),(_x,30),(_A4,31)))
class Xdsl2SymbolProtection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_AB,1),('halfSymbol',2),(_AC,3),(_AD,4),(_AE,5),(_AF,6),(_AG,7),(_AH,8),(_AI,9),(_AJ,10),(_AK,11),(_AL,12),(_AM,13),(_AN,14),(_AO,15),(_AP,16),(_AQ,17),(_AR,18)))
class Xdsl2SymbolProtection8(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_AB,1),(_AC,2),(_AD,3),(_AE,4),(_AF,5),(_AG,6),(_AH,7),(_AI,8),(_AJ,9),(_AK,10),(_AL,11),(_AM,12),(_AN,13),(_AO,14),(_AP,15),(_AQ,16),(_AR,17)))
class Xdsl2MaxBer(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eminus3',1),('eminus5',2),('eminus7',3)))
class Xdsl2ChInitPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('policy0',1),('policy1',2)))
class Xdsl2ScMaskDs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
class Xdsl2ScMaskUs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
class Xdsl2CarMask(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class Xdsl2RfiBands(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class Xdsl2PsdMaskDs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
class Xdsl2PsdMaskUs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
class Xdsl2Tssi(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
class Xdsl2LastTransmittedState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320)));namedValues=NamedValues(*(('atucG9941',0),('atucQuiet1',1),('atucComb1',2),('atucQuiet2',3),('atucComb2',4),('atucIcomb1',5),('atucLineprob',6),('atucQuiet3',7),('atucComb3',8),('atucIComb2',9),('atucMsgfmt',10),('atucMsgpcb',11),('atucQuiet4',12),('atucReverb1',13),('atucTref1',14),('atucReverb2',15),('atucEct',16),('atucReverb3',17),('atucTref2',18),('atucReverb4',19),('atucSegue1',20),('atucMsg1',21),('atucReverb5',22),('atucSegue2',23),('atucMedley',24),('atucExchmarker',25),('atucMsg2',26),('atucReverb6',27),('atucSegue3',28),('atucParams',29),('atucReverb7',30),('atucSegue4',31),('atucShowtime',32),('aturG9941',100),('aturQuiet1',101),('aturComb1',102),('aturQuiet2',103),('aturComb2',104),('aturIcomb1',105),('aturLineprob',106),('aturQuiet3',107),('aturComb3',108),('aturIcomb2',109),('aturMsgfmt',110),('aturMsgpcb',111),('aturReverb1',112),('aturQuiet4',113),('aturReverb2',114),('aturQuiet5',115),('aturReverb3',116),('aturEct',117),('aturReverb4',118),('aturSegue1',119),('aturReverb5',120),('aturSegue2',121),('aturMsg1',122),('aturMedley',123),('aturExchmarker',124),('aturMsg2',125),('aturReverb6',126),('aturSegue3',127),('aturParams',128),('aturReverb7',129),('aturSegue4',130),('aturShowtime',131),('vtucG9941',200),('vtucQuiet1',201),('vtucChDiscov1',202),('vtucSynchro1',203),('vtucPilot1',204),('vtucQuiet2',205),('vtucPeriodic1',206),('vtucSynchro2',207),('vtucChDiscov2',208),('vtucSynchro3',209),('vtucTraining1',210),('vtucSynchro4',211),('vtucPilot2',212),('vtucTeq',213),('vtucEct',214),('vtucPilot3',215),('vtucPeriodic2',216),('vtucTraining2',217),('vtucSynchro5',218),('vtucMedley',219),('vtucSynchro6',220),('vtucShowtime',221),('vturG9941',300),('vturQuiet1',301),('vturChDiscov1',302),('vturSynchro1',303),('vturLineprobe',304),('vturPeriodic1',305),('vturSynchro2',306),('vturChDiscov2',307),('vturSynchro3',308),('vturQuiet2',309),('vturTraining1',310),('vturSynchro4',311),('vturTeq',312),('vturQuiet3',313),('vturEct',314),('vturPeriodic2',315),('vturTraining2',316),('vturSynchro5',317),('vturMedley',318),('vturSynchro6',319),('vturShowtime',320)))
class Xdsl2LineStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_C,0),('lossOfFraming',1),('lossOfSignal',2),('lossOfPower',3),('initFailure',4)))
class Xdsl2ChInpReport(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inpComputedUsingFormula',1),('inpEstimatedByXtur',2)))
class Xdsl2ChAtmStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_C,0),('noCellDelineation',1),('lossOfCellDelineation',2)))
class Xdsl2ChPtmStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_C,0),('outOfSync',1)))
class Xdsl2UpboKLF(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('override',2),('disableUpbo',3)))
class Xdsl2BandUs(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,7,9,11)));namedValues=NamedValues(*(('us1',5),('us2',7),('us3',9),('us4',11)))
class Xdsl2LinePsdMaskSelectUs(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('adlu32Eu32',1),('adlu36Eu36',2),('adlu40Eu40',3),('adlu44Eu44',4),('adlu48Eu48',5),('adlu52Eu52',6),('adlu56Eu56',7),('adlu60Eu60',8),('adlu64Eu64',9)))
class Xdsl2LineCeFlag(TextualConvention,Bits):status=_A;namedValues=NamedValues(('enableCyclicExtension',0))
class Xdsl2LineSnrMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('virtualNoiseDisabled',1),('virtualNoiseEnabled',2)))
class Xdsl2LineTxRefVnDs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
class Xdsl2LineTxRefVnUs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
class Xdsl2BitsAlloc(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class Xdsl2MrefPsdDs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,192))
class Xdsl2MrefPsdUs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
mibBuilder.exportSymbols('VDSL2-LINE-TC-MIB',**{'Xdsl2Unit':Xdsl2Unit,'Xdsl2Direction':Xdsl2Direction,'Xdsl2Band':Xdsl2Band,'Xdsl2TransmissionModeType':Xdsl2TransmissionModeType,'Xdsl2RaMode':Xdsl2RaMode,'Xdsl2InitResult':Xdsl2InitResult,'Xdsl2OperationModes':Xdsl2OperationModes,'Xdsl2PowerMngState':Xdsl2PowerMngState,'Xdsl2ConfPmsForce':Xdsl2ConfPmsForce,'Xdsl2LinePmMode':Xdsl2LinePmMode,'Xdsl2LineLdsf':Xdsl2LineLdsf,'Xdsl2LdsfResult':Xdsl2LdsfResult,'Xdsl2LineBpsc':Xdsl2LineBpsc,'Xdsl2BpscResult':Xdsl2BpscResult,'Xdsl2LineReset':Xdsl2LineReset,'Xdsl2LineProfiles':Xdsl2LineProfiles,'Xdsl2LineClassMask':Xdsl2LineClassMask,'Xdsl2LineLimitMask':Xdsl2LineLimitMask,'Xdsl2LineUs0Disable':Xdsl2LineUs0Disable,'Xdsl2LineUs0Mask':Xdsl2LineUs0Mask,'Xdsl2SymbolProtection':Xdsl2SymbolProtection,'Xdsl2SymbolProtection8':Xdsl2SymbolProtection8,'Xdsl2MaxBer':Xdsl2MaxBer,'Xdsl2ChInitPolicy':Xdsl2ChInitPolicy,'Xdsl2ScMaskDs':Xdsl2ScMaskDs,'Xdsl2ScMaskUs':Xdsl2ScMaskUs,'Xdsl2CarMask':Xdsl2CarMask,'Xdsl2RfiBands':Xdsl2RfiBands,'Xdsl2PsdMaskDs':Xdsl2PsdMaskDs,'Xdsl2PsdMaskUs':Xdsl2PsdMaskUs,'Xdsl2Tssi':Xdsl2Tssi,'Xdsl2LastTransmittedState':Xdsl2LastTransmittedState,'Xdsl2LineStatus':Xdsl2LineStatus,'Xdsl2ChInpReport':Xdsl2ChInpReport,'Xdsl2ChAtmStatus':Xdsl2ChAtmStatus,'Xdsl2ChPtmStatus':Xdsl2ChPtmStatus,'Xdsl2UpboKLF':Xdsl2UpboKLF,'Xdsl2BandUs':Xdsl2BandUs,'Xdsl2LinePsdMaskSelectUs':Xdsl2LinePsdMaskSelectUs,'Xdsl2LineCeFlag':Xdsl2LineCeFlag,'Xdsl2LineSnrMode':Xdsl2LineSnrMode,'Xdsl2LineTxRefVnDs':Xdsl2LineTxRefVnDs,'Xdsl2LineTxRefVnUs':Xdsl2LineTxRefVnUs,'Xdsl2BitsAlloc':Xdsl2BitsAlloc,'Xdsl2MrefPsdDs':Xdsl2MrefPsdDs,'Xdsl2MrefPsdUs':Xdsl2MrefPsdUs,'vdsl2TCMIB':vdsl2TCMIB})