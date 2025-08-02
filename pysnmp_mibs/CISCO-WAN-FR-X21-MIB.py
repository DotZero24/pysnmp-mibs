_w='ciscoWanFrX21AlarmGroup'
_v='ciscoWanFrX21AlarmConfGroup'
_u='ciscoWanFrX21PortGroup'
_t='ciscoWanFrX21LineGroup'
_s='x21AlarmClrButton'
_r='x21LineEIAStatus'
_q='x21LineAlarmState'
_p='x21Severity'
_o='x21LineNumofValidEntries'
_n='serialLineRateVariation'
_m='serialLineRate'
_l='x21ClkFrequencyThreshold'
_k='x21LineInterfaceType'
_j='x21InvertClock'
_i='x21ConnectorType'
_h='x21LineLoopbackCodeDetection'
_g='x21LineSendCode'
_f='x21LineLoopbackCommand'
_e='x21LineRate'
_d='x21LineType'
_c='x21LineEnable'
_b='x21portEgrSvcBandW'
_a='x21portIngrSvcBandW'
_Z='x21portDeleteSvcs'
_Y='x21portSvcDlciHigh'
_X='x21portSvcDlciLow'
_W='x21portSvcLcnHigh'
_V='x21portSvcLcnLow'
_U='x21portSvcShareLcn'
_T='x21portSvcInUse'
_S='x21portSvcStatus'
_R='x21portType'
_Q='x21portAdmin'
_P='x21portSpeed'
_O='x21portEqueueServiceRatio'
_N='x21portFlagsBetweenFrames'
_M='x21portRowStatus'
_L='x21portLineNum'
_K='enable'
_J='disable'
_I='x21portNum'
_H='x21AlmLineNum'
_G='x21AlmCnfLineNum'
_F='x21LineNum'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-FR-X21-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
frPortCnfX21PortGrp,x21=mibBuilder.importSymbols('BASIS-MIB','frPortCnfX21PortGrp','x21')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanFrX21MIB=ModuleIdentity((1,3,6,1,4,1,351,150,49))
if mibBuilder.loadTexts:ciscoWanFrX21MIB.setRevisions(('2002-09-19 00:00',))
_X21CnfGrp_ObjectIdentity=ObjectIdentity
x21CnfGrp=_X21CnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,5,1))
_X21CnfGrpTable_Object=MibTable
x21CnfGrpTable=_X21CnfGrpTable_Object((1,3,6,1,4,1,351,110,4,5,1,1))
if mibBuilder.loadTexts:x21CnfGrpTable.setStatus(_A)
_X21CnfGrpEntry_Object=MibTableRow
x21CnfGrpEntry=_X21CnfGrpEntry_Object((1,3,6,1,4,1,351,110,4,5,1,1,1))
x21CnfGrpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:x21CnfGrpEntry.setStatus(_A)
class _X21LineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_X21LineNum_Type.__name__=_C
_X21LineNum_Object=MibTableColumn
x21LineNum=_X21LineNum_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,1),_X21LineNum_Type())
x21LineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:x21LineNum.setStatus(_A)
class _X21LineEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('modify',3)))
_X21LineEnable_Type.__name__=_C
_X21LineEnable_Object=MibTableColumn
x21LineEnable=_X21LineEnable_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,2),_X21LineEnable_Type())
x21LineEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:x21LineEnable.setStatus(_A)
class _X21LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('dteST',3)))
_X21LineType_Type.__name__=_C
_X21LineType_Object=MibTableColumn
x21LineType=_X21LineType_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,3),_X21LineType_Type())
x21LineType.setMaxAccess(_D)
if mibBuilder.loadTexts:x21LineType.setStatus(_A)
class _X21LineRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108)));namedValues=NamedValues(*(('r48Kbps',1),('r56Kbps',2),('r64Kbps',3),('r112Kbps',4),('r128Kbps',5),('r168Kbps',6),('r192Kbps',7),('r224Kbps',8),('r256Kbps',9),('r280Kbps',10),('r320Kbps',11),('r336Kbps',12),('r384Kbps',13),('r392Kbps',14),('r448Kbps',15),('r512Kbps',16),('r768Kbps',17),('r1024Kbps',18),('r1536Kbps',19),('r1544Kbps',20),('r1792Kbps',21),('r1920Kbps',22),('r1984Kbps',23),('r2048Kbps',24),('r3097Kbps',25),('r3157Kbps',26),('r4096Kbps',27),('r4645Kbps',28),('r4736Kbps',29),('r6195Kbps',30),('r6315Kbps',31),('r7744Kbps',32),('r7899Kbps',33),('r8192Kbps',34),('r9289Kbps',35),('r9472Kbps',36),('r10240Kbps',37),('r10890Kbps',38),('r11060Kbps',39),('r12390Kbps',40),('r12630Kbps',41),('r13900Kbps',42),('r14220Kbps',43),('r14340Kbps',44),('r15490Kbps',45),('r15800Kbps',46),('r16380Kbps',47),('r20030Kbps',48),('r24990Kbps',49),('r52Mbps',50),('r17370Kbps',51),('r18950Kbps',52),('r20530Kbps',53),('r22100Kbps',54),('r23680Kbps',55),('r3088Kbps',56),('r4632Kbps',57),('r6176Kbps',58),('r7720Kbps',59),('r9264Kbps',60),('r10808Kbps',61),('r12352Kbps',62),('r13896Kbps',63),('r15440Kbps',64),('r16984Kbps',65),('r18528Kbps',66),('r20072Kbps',67),('r21616Kbps',68),('r23160Kbps',69),('r24704Kbps',70),('r26248Kbps',71),('r27792Kbps',72),('r29336Kbps',73),('r30880Kbps',74),('r32424Kbps',75),('r33968Kbps',76),('r35512Kbps',77),('r37056Kbps',78),('r38600Kbps',79),('r40144Kbps',80),('r41688Kbps',81),('r43232Kbps',82),('r44776Kbps',83),('r46320Kbps',84),('r47864Kbps',85),('r49408Kbps',86),('r50952Kbps',87),('r6144Kbps',88),('r12288Kbps',89),('r14336Kbps',90),('r16384Kbps',91),('r18432Kbps',92),('r20480Kbps',93),('r22528Kbps',94),('r24576Kbps',95),('r26624Kbps',96),('r28672Kbps',97),('r30720Kbps',98),('r32768Kbps',99),('r34816Kbps',100),('r36864Kbps',101),('r38912Kbps',102),('r40960Kbps',103),('r43008Kbps',104),('r45056Kbps',105),('r47104Kbps',106),('r49152Kbps',107),('r51200Kbps',108)))
_X21LineRate_Type.__name__=_C
_X21LineRate_Object=MibTableColumn
x21LineRate=_X21LineRate_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,4),_X21LineRate_Type())
x21LineRate.setMaxAccess(_D)
if mibBuilder.loadTexts:x21LineRate.setStatus(_A)
class _X21LineLoopbackCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('x21NoLoop',1),('x21DiagnosticMetallicLoop',2),('x21DiagnosticFrontcardLoop',3),('x21RemoteLoop',4),('v35MetallicLoop',5)))
_X21LineLoopbackCommand_Type.__name__=_C
_X21LineLoopbackCommand_Object=MibTableColumn
x21LineLoopbackCommand=_X21LineLoopbackCommand_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,5),_X21LineLoopbackCommand_Type())
x21LineLoopbackCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:x21LineLoopbackCommand.setStatus(_A)
class _X21LineSendCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('x21NoCode',1),('x21SendLoopACode',2),('x21SendLoopBCode',3),('x21SendLocalLoopCode',4),('x21SendRemoteLoopCode',5),('x21SendUnLoopCode',6)))
_X21LineSendCode_Type.__name__=_C
_X21LineSendCode_Object=MibTableColumn
x21LineSendCode=_X21LineSendCode_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,6),_X21LineSendCode_Type())
x21LineSendCode.setMaxAccess(_D)
if mibBuilder.loadTexts:x21LineSendCode.setStatus(_A)
class _X21LineLoopbackCodeDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('codeDetectDisabled',1),('codeDetectEnabled',2)))
_X21LineLoopbackCodeDetection_Type.__name__=_C
_X21LineLoopbackCodeDetection_Object=MibTableColumn
x21LineLoopbackCodeDetection=_X21LineLoopbackCodeDetection_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,7),_X21LineLoopbackCodeDetection_Type())
x21LineLoopbackCodeDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:x21LineLoopbackCodeDetection.setStatus(_A)
class _X21ConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('x21Backcard',1),('hssiBackcard',2),('v35Backcard',3)))
_X21ConnectorType_Type.__name__=_C
_X21ConnectorType_Object=MibTableColumn
x21ConnectorType=_X21ConnectorType_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,8),_X21ConnectorType_Type())
x21ConnectorType.setMaxAccess(_E)
if mibBuilder.loadTexts:x21ConnectorType.setStatus(_A)
class _X21InvertClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nonInvertedAndNotLooped',1),('invertedAndNotLooped',2),('nonInvertedAndLooped',3),('invertedAndLooped',4)))
_X21InvertClock_Type.__name__=_C
_X21InvertClock_Object=MibTableColumn
x21InvertClock=_X21InvertClock_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,9),_X21InvertClock_Type())
x21InvertClock.setMaxAccess(_D)
if mibBuilder.loadTexts:x21InvertClock.setStatus(_A)
class _X21LineInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hssi',1),('x21',2),('v35',3)))
_X21LineInterfaceType_Type.__name__=_C
_X21LineInterfaceType_Object=MibTableColumn
x21LineInterfaceType=_X21LineInterfaceType_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,10),_X21LineInterfaceType_Type())
x21LineInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:x21LineInterfaceType.setStatus(_A)
class _X21ClkFrequencyThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_X21ClkFrequencyThreshold_Type.__name__=_C
_X21ClkFrequencyThreshold_Object=MibTableColumn
x21ClkFrequencyThreshold=_X21ClkFrequencyThreshold_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,11),_X21ClkFrequencyThreshold_Type())
x21ClkFrequencyThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:x21ClkFrequencyThreshold.setStatus(_A)
class _SerialLineRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(48000,51840000))
_SerialLineRate_Type.__name__=_C
_SerialLineRate_Object=MibTableColumn
serialLineRate=_SerialLineRate_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,12),_SerialLineRate_Type())
serialLineRate.setMaxAccess(_D)
if mibBuilder.loadTexts:serialLineRate.setStatus(_A)
class _SerialLineRateVariation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SerialLineRateVariation_Type.__name__=_C
_SerialLineRateVariation_Object=MibTableColumn
serialLineRateVariation=_SerialLineRateVariation_Object((1,3,6,1,4,1,351,110,4,5,1,1,1,13),_SerialLineRateVariation_Type())
serialLineRateVariation.setMaxAccess(_E)
if mibBuilder.loadTexts:serialLineRateVariation.setStatus(_A)
class _X21LineNumofValidEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_X21LineNumofValidEntries_Type.__name__=_C
_X21LineNumofValidEntries_Object=MibScalar
x21LineNumofValidEntries=_X21LineNumofValidEntries_Object((1,3,6,1,4,1,351,110,4,5,1,2),_X21LineNumofValidEntries_Type())
x21LineNumofValidEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:x21LineNumofValidEntries.setStatus(_A)
_X21AlmCnfGrp_ObjectIdentity=ObjectIdentity
x21AlmCnfGrp=_X21AlmCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,5,2))
_X21AlmCnfGrpTable_Object=MibTable
x21AlmCnfGrpTable=_X21AlmCnfGrpTable_Object((1,3,6,1,4,1,351,110,4,5,2,1))
if mibBuilder.loadTexts:x21AlmCnfGrpTable.setStatus(_A)
_X21AlmCnfGrpEntry_Object=MibTableRow
x21AlmCnfGrpEntry=_X21AlmCnfGrpEntry_Object((1,3,6,1,4,1,351,110,4,5,2,1,1))
x21AlmCnfGrpEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:x21AlmCnfGrpEntry.setStatus(_A)
class _X21AlmCnfLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_X21AlmCnfLineNum_Type.__name__=_C
_X21AlmCnfLineNum_Object=MibTableColumn
x21AlmCnfLineNum=_X21AlmCnfLineNum_Object((1,3,6,1,4,1,351,110,4,5,2,1,1,1),_X21AlmCnfLineNum_Type())
x21AlmCnfLineNum.setMaxAccess(_D)
if mibBuilder.loadTexts:x21AlmCnfLineNum.setStatus(_A)
class _X21Severity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minor',1),('major',2),('dontcare',3)))
_X21Severity_Type.__name__=_C
_X21Severity_Object=MibTableColumn
x21Severity=_X21Severity_Object((1,3,6,1,4,1,351,110,4,5,2,1,1,2),_X21Severity_Type())
x21Severity.setMaxAccess(_D)
if mibBuilder.loadTexts:x21Severity.setStatus(_A)
_X21AlmGrp_ObjectIdentity=ObjectIdentity
x21AlmGrp=_X21AlmGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,5,3))
_X21AlmGrpTable_Object=MibTable
x21AlmGrpTable=_X21AlmGrpTable_Object((1,3,6,1,4,1,351,110,4,5,3,1))
if mibBuilder.loadTexts:x21AlmGrpTable.setStatus(_A)
_X21AlmGrpEntry_Object=MibTableRow
x21AlmGrpEntry=_X21AlmGrpEntry_Object((1,3,6,1,4,1,351,110,4,5,3,1,1))
x21AlmGrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:x21AlmGrpEntry.setStatus(_A)
class _X21AlmLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_X21AlmLineNum_Type.__name__=_C
_X21AlmLineNum_Object=MibTableColumn
x21AlmLineNum=_X21AlmLineNum_Object((1,3,6,1,4,1,351,110,4,5,3,1,1,1),_X21AlmLineNum_Type())
x21AlmLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:x21AlmLineNum.setStatus(_A)
class _X21LineAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_X21LineAlarmState_Type.__name__=_C
_X21LineAlarmState_Object=MibTableColumn
x21LineAlarmState=_X21LineAlarmState_Object((1,3,6,1,4,1,351,110,4,5,3,1,1,2),_X21LineAlarmState_Type())
x21LineAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:x21LineAlarmState.setStatus(_A)
class _X21LineEIAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_X21LineEIAStatus_Type.__name__=_C
_X21LineEIAStatus_Object=MibTableColumn
x21LineEIAStatus=_X21LineEIAStatus_Object((1,3,6,1,4,1,351,110,4,5,3,1,1,3),_X21LineEIAStatus_Type())
x21LineEIAStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:x21LineEIAStatus.setStatus(_A)
class _X21AlarmClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('clear',2)))
_X21AlarmClrButton_Type.__name__=_C
_X21AlarmClrButton_Object=MibTableColumn
x21AlarmClrButton=_X21AlarmClrButton_Object((1,3,6,1,4,1,351,110,4,5,3,1,1,4),_X21AlarmClrButton_Type())
x21AlarmClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:x21AlarmClrButton.setStatus(_A)
_FrPortCnfX21PortGrpTable_Object=MibTable
frPortCnfX21PortGrpTable=_FrPortCnfX21PortGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1))
if mibBuilder.loadTexts:frPortCnfX21PortGrpTable.setStatus(_A)
_FrPortCnfX21PortGrpEntry_Object=MibTableRow
frPortCnfX21PortGrpEntry=_FrPortCnfX21PortGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1))
frPortCnfX21PortGrpEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:frPortCnfX21PortGrpEntry.setStatus(_A)
class _X21portNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_X21portNum_Type.__name__=_C
_X21portNum_Object=MibTableColumn
x21portNum=_X21portNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,1),_X21portNum_Type())
x21portNum.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portNum.setStatus(_A)
class _X21portLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_X21portLineNum_Type.__name__=_C
_X21portLineNum_Object=MibTableColumn
x21portLineNum=_X21portLineNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,2),_X21portLineNum_Type())
x21portLineNum.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portLineNum.setStatus(_A)
class _X21portRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_X21portRowStatus_Type.__name__=_C
_X21portRowStatus_Object=MibTableColumn
x21portRowStatus=_X21portRowStatus_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,3),_X21portRowStatus_Type())
x21portRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portRowStatus.setStatus(_A)
class _X21portFlagsBetweenFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_X21portFlagsBetweenFrames_Type.__name__=_C
_X21portFlagsBetweenFrames_Object=MibTableColumn
x21portFlagsBetweenFrames=_X21portFlagsBetweenFrames_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,4),_X21portFlagsBetweenFrames_Type())
x21portFlagsBetweenFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portFlagsBetweenFrames.setStatus(_A)
class _X21portEqueueServiceRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_X21portEqueueServiceRatio_Type.__name__=_C
_X21portEqueueServiceRatio_Object=MibTableColumn
x21portEqueueServiceRatio=_X21portEqueueServiceRatio_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,5),_X21portEqueueServiceRatio_Type())
x21portEqueueServiceRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portEqueueServiceRatio.setStatus(_A)
class _X21portSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_X21portSpeed_Type.__name__=_C
_X21portSpeed_Object=MibTableColumn
x21portSpeed=_X21portSpeed_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,6),_X21portSpeed_Type())
x21portSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portSpeed.setStatus(_A)
class _X21portAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('write-Only',3)))
_X21portAdmin_Type.__name__=_C
_X21portAdmin_Object=MibTableColumn
x21portAdmin=_X21portAdmin_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,7),_X21portAdmin_Type())
x21portAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portAdmin.setStatus(_A)
class _X21portType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('frame-relay',1),('frFUNI',2),('frame-forward',3)))
_X21portType_Type.__name__=_C
_X21portType_Object=MibTableColumn
x21portType=_X21portType_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,8),_X21portType_Type())
x21portType.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portType.setStatus(_A)
class _X21portSvcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_X21portSvcStatus_Type.__name__=_C
_X21portSvcStatus_Object=MibTableColumn
x21portSvcStatus=_X21portSvcStatus_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,9),_X21portSvcStatus_Type())
x21portSvcStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portSvcStatus.setStatus(_A)
class _X21portSvcInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-use',1),('in-use',2)))
_X21portSvcInUse_Type.__name__=_C
_X21portSvcInUse_Object=MibTableColumn
x21portSvcInUse=_X21portSvcInUse_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,10),_X21portSvcInUse_Type())
x21portSvcInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portSvcInUse.setStatus(_A)
class _X21portSvcShareLcn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port-based',1),('card-based',2)))
_X21portSvcShareLcn_Type.__name__=_C
_X21portSvcShareLcn_Object=MibTableColumn
x21portSvcShareLcn=_X21portSvcShareLcn_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,11),_X21portSvcShareLcn_Type())
x21portSvcShareLcn.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portSvcShareLcn.setStatus(_A)
class _X21portSvcLcnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,271))
_X21portSvcLcnLow_Type.__name__=_C
_X21portSvcLcnLow_Object=MibTableColumn
x21portSvcLcnLow=_X21portSvcLcnLow_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,12),_X21portSvcLcnLow_Type())
x21portSvcLcnLow.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portSvcLcnLow.setStatus(_A)
class _X21portSvcLcnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,271))
_X21portSvcLcnHigh_Type.__name__=_C
_X21portSvcLcnHigh_Object=MibTableColumn
x21portSvcLcnHigh=_X21portSvcLcnHigh_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,13),_X21portSvcLcnHigh_Type())
x21portSvcLcnHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portSvcLcnHigh.setStatus(_A)
class _X21portSvcDlciLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_X21portSvcDlciLow_Type.__name__=_C
_X21portSvcDlciLow_Object=MibTableColumn
x21portSvcDlciLow=_X21portSvcDlciLow_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,14),_X21portSvcDlciLow_Type())
x21portSvcDlciLow.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portSvcDlciLow.setStatus(_A)
class _X21portSvcDlciHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_X21portSvcDlciHigh_Type.__name__=_C
_X21portSvcDlciHigh_Object=MibTableColumn
x21portSvcDlciHigh=_X21portSvcDlciHigh_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,15),_X21portSvcDlciHigh_Type())
x21portSvcDlciHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portSvcDlciHigh.setStatus(_A)
class _X21portDeleteSvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delete',1),('other',2)))
_X21portDeleteSvcs_Type.__name__=_C
_X21portDeleteSvcs_Object=MibTableColumn
x21portDeleteSvcs=_X21portDeleteSvcs_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,16),_X21portDeleteSvcs_Type())
x21portDeleteSvcs.setMaxAccess(_D)
if mibBuilder.loadTexts:x21portDeleteSvcs.setStatus(_A)
class _X21portIngrSvcBandW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_X21portIngrSvcBandW_Type.__name__=_C
_X21portIngrSvcBandW_Object=MibTableColumn
x21portIngrSvcBandW=_X21portIngrSvcBandW_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,17),_X21portIngrSvcBandW_Type())
x21portIngrSvcBandW.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portIngrSvcBandW.setStatus(_A)
class _X21portEgrSvcBandW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_X21portEgrSvcBandW_Type.__name__=_C
_X21portEgrSvcBandW_Object=MibTableColumn
x21portEgrSvcBandW=_X21portEgrSvcBandW_Object((1,3,6,1,4,1,351,110,5,1,1,1,3,1,1,18),_X21portEgrSvcBandW_Type())
x21portEgrSvcBandW.setMaxAccess(_E)
if mibBuilder.loadTexts:x21portEgrSvcBandW.setStatus(_A)
_CwfX21MIBConformance_ObjectIdentity=ObjectIdentity
cwfX21MIBConformance=_CwfX21MIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,49,2))
_CwfX21MIBGroups_ObjectIdentity=ObjectIdentity
cwfX21MIBGroups=_CwfX21MIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,49,2,1))
_CwfX21MIBCompliances_ObjectIdentity=ObjectIdentity
cwfX21MIBCompliances=_CwfX21MIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,49,2,2))
ciscoWanFrX21PortGroup=ObjectGroup((1,3,6,1,4,1,351,150,49,2,1,1))
ciscoWanFrX21PortGroup.setObjects(*((_B,_I),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ciscoWanFrX21PortGroup.setStatus(_A)
ciscoWanFrX21LineGroup=ObjectGroup((1,3,6,1,4,1,351,150,49,2,1,2))
ciscoWanFrX21LineGroup.setObjects(*((_B,_F),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoWanFrX21LineGroup.setStatus(_A)
ciscoWanFrX21AlarmConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,49,2,1,3))
ciscoWanFrX21AlarmConfGroup.setObjects(*((_B,_G),(_B,_p)))
if mibBuilder.loadTexts:ciscoWanFrX21AlarmConfGroup.setStatus(_A)
ciscoWanFrX21AlarmGroup=ObjectGroup((1,3,6,1,4,1,351,150,49,2,1,4))
ciscoWanFrX21AlarmGroup.setObjects(*((_B,_H),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ciscoWanFrX21AlarmGroup.setStatus(_A)
cwfX21Compliance=ModuleCompliance((1,3,6,1,4,1,351,150,49,2,2,1))
cwfX21Compliance.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cwfX21Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'x21CnfGrp':x21CnfGrp,'x21CnfGrpTable':x21CnfGrpTable,'x21CnfGrpEntry':x21CnfGrpEntry,_F:x21LineNum,_c:x21LineEnable,_d:x21LineType,_e:x21LineRate,_f:x21LineLoopbackCommand,_g:x21LineSendCode,_h:x21LineLoopbackCodeDetection,_i:x21ConnectorType,_j:x21InvertClock,_k:x21LineInterfaceType,_l:x21ClkFrequencyThreshold,_m:serialLineRate,_n:serialLineRateVariation,_o:x21LineNumofValidEntries,'x21AlmCnfGrp':x21AlmCnfGrp,'x21AlmCnfGrpTable':x21AlmCnfGrpTable,'x21AlmCnfGrpEntry':x21AlmCnfGrpEntry,_G:x21AlmCnfLineNum,_p:x21Severity,'x21AlmGrp':x21AlmGrp,'x21AlmGrpTable':x21AlmGrpTable,'x21AlmGrpEntry':x21AlmGrpEntry,_H:x21AlmLineNum,_q:x21LineAlarmState,_r:x21LineEIAStatus,_s:x21AlarmClrButton,'frPortCnfX21PortGrpTable':frPortCnfX21PortGrpTable,'frPortCnfX21PortGrpEntry':frPortCnfX21PortGrpEntry,_I:x21portNum,_L:x21portLineNum,_M:x21portRowStatus,_N:x21portFlagsBetweenFrames,_O:x21portEqueueServiceRatio,_P:x21portSpeed,_Q:x21portAdmin,_R:x21portType,_S:x21portSvcStatus,_T:x21portSvcInUse,_U:x21portSvcShareLcn,_V:x21portSvcLcnLow,_W:x21portSvcLcnHigh,_X:x21portSvcDlciLow,_Y:x21portSvcDlciHigh,_Z:x21portDeleteSvcs,_a:x21portIngrSvcBandW,_b:x21portEgrSvcBandW,'ciscoWanFrX21MIB':ciscoWanFrX21MIB,'cwfX21MIBConformance':cwfX21MIBConformance,'cwfX21MIBGroups':cwfX21MIBGroups,_u:ciscoWanFrX21PortGroup,_t:ciscoWanFrX21LineGroup,_v:ciscoWanFrX21AlarmConfGroup,_w:ciscoWanFrX21AlarmGroup,'cwfX21MIBCompliances':cwfX21MIBCompliances,'cwfX21Compliance':cwfX21Compliance})