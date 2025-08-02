_d='g9925AnnexMPotsOverlapped'
_c='g9925AnnexMPotsNonOverlapped'
_b='g9925AnnexJAllDigOverlapped'
_a='g9925AnnexJAllDigNonOverlapped'
_Z='g9925AnnexIAllDigOverlapped'
_Y='g9925AnnexIAllDigNonOverlapped'
_X='g9925isdnOverlapped'
_W='g9925IsdnNonOverlapped'
_V='g9925PotsOverlapped'
_U='g9925PotsNonOverlapped'
_T='g9923AnnexMPotsOverlapped'
_S='g9923AnnexMPotsNonOverlapped'
_R='g9923AnnexLMode4Overlapped'
_Q='g9923AnnexLMode3Overlapped'
_P='g9923AnnexLMode2NonOverlapped'
_O='g9923AnnexLMode1NonOverlapped'
_N='g9924AnnexIAllDigOverlapped'
_M='g9924AnnexIAllDigNonOverlapped'
_L='g9923AnnexJAllDigOverlapped'
_K='g9923AnnexJAllDigNonOverlapped'
_J='g9923AnnexIAllDigOverlapped'
_I='g9923AnnexIAllDigNonOverlapped'
_H='g9924potsOverlapped'
_G='g9924potsNonOverlapped'
_F='g9923isdnOverlapped'
_E='g9923IsdnNonOverlapped'
_D='g9923PotsOverlapped'
_C='g9923PotsNonOverlapped'
_B='noDefect'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adsl2TCMIB=ModuleIdentity((1,3,6,1,2,1,10,238,2))
if mibBuilder.loadTexts:adsl2TCMIB.setRevisions(('2006-10-04 00:00',))
class Adsl2Unit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('atuc',1),('atur',2)))
class Adsl2Direction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstream',1),('downstream',2)))
class Adsl2TransmissionModeType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('ansit1413',0),('etsi',1),('g9921PotsNonOverlapped',2),('g9921PotsOverlapped',3),('g9921IsdnNonOverlapped',4),('g9921isdnOverlapped',5),('g9921tcmIsdnNonOverlapped',6),('g9921tcmIsdnOverlapped',7),('g9922potsNonOverlapped',8),('g9922potsOverlapped',9),('g9922tcmIsdnNonOverlapped',10),('g9922tcmIsdnOverlapped',11),('g9921tcmIsdnSymmetric',12),('reserved1',13),('reserved2',14),('reserved3',15),('reserved4',16),('reserved5',17),(_C,18),(_D,19),(_E,20),(_F,21),('reserved6',22),('reserved7',23),(_G,24),(_H,25),('reserved8',26),('reserved9',27),(_I,28),(_J,29),(_K,30),(_L,31),(_M,32),(_N,33),(_O,34),(_P,35),(_Q,36),(_R,37),(_S,38),(_T,39),(_U,40),(_V,41),(_W,42),(_X,43),('reserved10',44),('reserved11',45),(_Y,46),(_Z,47),(_a,48),(_b,49),(_c,50),(_d,51),('reserved12',52),('reserved13',53),('reserved14',54),('reserved15',55)))
class Adsl2RaMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('raInit',2),('dynamicRa',3)))
class Adsl2InitResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noFail',0),('configError',1),('configNotFeasible',2),('commFail',3),('noPeerAtu',4),('otherCause',5)))
class Adsl2OperationModes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,8,9,10,11,14,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,36,37,38,39,40,41)));namedValues=NamedValues(*(('defMode',1),('adsl',2),(_C,8),(_D,9),(_E,10),(_F,11),(_G,14),(_H,15),(_I,18),(_J,19),(_K,20),(_L,21),(_M,22),(_N,23),(_O,24),(_P,25),(_Q,26),(_R,27),(_S,28),(_T,29),(_U,30),(_V,31),(_W,32),(_X,33),(_Y,36),(_Z,37),(_a,38),(_b,39),(_c,40),(_d,41)))
class Adsl2PowerMngState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('l0',1),('l1',2),('l2',3),('l3',4)))
class Adsl2ConfPmsForce(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('l3toL0',0),('l0toL2',2),('l0orL2toL3',3)))
class Adsl2LConfProfPmMode(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('allowTransitionsToIdle',0),('allowTransitionsToLowPower',1)))
class Adsl2LineLdsf(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inhibit',0),('force',1)))
class Adsl2LdsfResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',1),('success',2),('inProgress',3),('unsupported',4),('cannotRun',5),('aborted',6),('failed',7),('illegalMode',8),('adminUp',9),('tableFull',10),('noResources',11)))
class Adsl2SymbolProtection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('noProtection',1),('halfSymbol',2),('singleSymbol',3),('twoSymbols',4),('threeSymbols',5),('fourSymbols',6),('fiveSymbols',7),('sixSymbols',8),('sevenSymbols',9),('eightSymbols',10),('nineSymbols',11),('tenSymbols',12),('elevenSymbols',13),('twelveSymbols',14),('thirteeSymbols',15),('fourteenSymbols',16),('fifteenSymbols',17),('sixteenSymbols',18)))
class Adsl2MaxBer(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eminus3',1),('eminus5',2),('eminus7',3)))
class Adsl2ScMaskDs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class Adsl2ScMaskUs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class Adsl2RfiDs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class Adsl2PsdMaskDs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
class Adsl2PsdMaskUs(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
class Adsl2Tssi(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
class Adsl2LastTransmittedState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131)));namedValues=NamedValues(*(('atucG9941',0),('atucQuiet1',1),('atucComb1',2),('atucQuiet2',3),('atucComb2',4),('atucIcomb1',5),('atucLineprob',6),('atucQuiet3',7),('atucComb3',8),('atucIComb2',9),('atucMsgfmt',10),('atucMsgpcb',11),('atucQuiet4',12),('atucReverb1',13),('atucTref1',14),('atucReverb2',15),('atucEct',16),('atucReverb3',17),('atucTref2',18),('atucReverb4',19),('atucSegue1',20),('atucMsg1',21),('atucReverb5',22),('atucSegue2',23),('atucMedley',24),('atucExchmarker',25),('atucMsg2',26),('atucReverb6',27),('atucSegue3',28),('atucParams',29),('atucReverb7',30),('atucSegue4',31),('atucShowtime',32),('aturG9941',100),('aturQuiet1',101),('aturComb1',102),('aturQuiet2',103),('aturComb2',104),('aturIcomb1',105),('aturLineprob',106),('aturQuiet3',107),('aturComb3',108),('aturIcomb2',109),('aturMsgfmt',110),('aturMsgpcb',111),('aturReverb1',112),('aturQuiet4',113),('aturReverb2',114),('aturQuiet5',115),('aturReverb3',116),('aturEct',117),('aturReverb4',118),('aturSegue1',119),('aturReverb5',120),('aturSegue2',121),('aturMsg1',122),('aturMedley',123),('aturExchmarker',124),('aturMsg2',125),('aturReverb6',126),('aturSegue3',127),('aturParams',128),('aturReverb7',129),('aturSegue4',130),('aturShowtime',131)))
class Adsl2LineStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_B,0),('lossOfFrame',1),('lossOfSignal',2),('lossOfPower',3),('initFailure',4)))
class Adsl2ChAtmStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_B,0),('noCellDelineation',1),('lossOfCellDelineation',2)))
class Adsl2ChPtmStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_B,0),('outOfSync',1)))
mibBuilder.exportSymbols('ADSL2-LINE-TC-MIB',**{'Adsl2Unit':Adsl2Unit,'Adsl2Direction':Adsl2Direction,'Adsl2TransmissionModeType':Adsl2TransmissionModeType,'Adsl2RaMode':Adsl2RaMode,'Adsl2InitResult':Adsl2InitResult,'Adsl2OperationModes':Adsl2OperationModes,'Adsl2PowerMngState':Adsl2PowerMngState,'Adsl2ConfPmsForce':Adsl2ConfPmsForce,'Adsl2LConfProfPmMode':Adsl2LConfProfPmMode,'Adsl2LineLdsf':Adsl2LineLdsf,'Adsl2LdsfResult':Adsl2LdsfResult,'Adsl2SymbolProtection':Adsl2SymbolProtection,'Adsl2MaxBer':Adsl2MaxBer,'Adsl2ScMaskDs':Adsl2ScMaskDs,'Adsl2ScMaskUs':Adsl2ScMaskUs,'Adsl2RfiDs':Adsl2RfiDs,'Adsl2PsdMaskDs':Adsl2PsdMaskDs,'Adsl2PsdMaskUs':Adsl2PsdMaskUs,'Adsl2Tssi':Adsl2Tssi,'Adsl2LastTransmittedState':Adsl2LastTransmittedState,'Adsl2LineStatus':Adsl2LineStatus,'Adsl2ChAtmStatus':Adsl2ChAtmStatus,'Adsl2ChPtmStatus':Adsl2ChPtmStatus,'adsl2TCMIB':adsl2TCMIB})