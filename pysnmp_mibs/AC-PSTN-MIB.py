_U='acNFASGroupStatusIndex'
_T='acSDHKLMNumberingSchemeTrunkIndex'
_S='acDigitalLegsLegIndex'
_R='acSonetSDHIndex'
_Q='acCASFileIndex'
_P='OctetString'
_O='dChannelStandby'
_N='dChannelActive'
_M='dChannelNotApplicable'
_L='not-accessible'
_K='obsolete'
_J='enable'
_I='disable'
_H='SnmpAdminString'
_G='acTrunkIndex'
_F='AC-PSTN-MIB'
_E='read-only'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acBoardMibs,acGeneric,acProducts,acRegistrations,audioCodes=mibBuilder.importSymbols('AUDIOCODES-TYPES-MIB','acBoardMibs','acGeneric','acProducts','acRegistrations','audioCodes')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TAddress','TextualConvention')
acPSTN=ModuleIdentity((1,3,6,1,4,1,5003,9,10,9))
_AcPSTNConfiguration_ObjectIdentity=ObjectIdentity
acPSTNConfiguration=_AcPSTNConfiguration_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1))
_AcTrunkConfig_ObjectIdentity=ObjectIdentity
acTrunkConfig=_AcTrunkConfig_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1))
_AcTrunk_ObjectIdentity=ObjectIdentity
acTrunk=_AcTrunk_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,1))
_AcTrunkTable_Object=MibTable
acTrunkTable=_AcTrunkTable_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1))
if mibBuilder.loadTexts:acTrunkTable.setStatus(_A)
_AcTrunkEntry_Object=MibTableRow
acTrunkEntry=_AcTrunkEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1))
acTrunkEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkEntry.setStatus(_A)
class _AcTrunkIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,83))
_AcTrunkIndex_Type.__name__=_D
_AcTrunkIndex_Object=MibTableColumn
acTrunkIndex=_AcTrunkIndex_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,1),_AcTrunkIndex_Type())
acTrunkIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkIndex.setStatus(_A)
class _AcTrunkAdministrativeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('locked',0),('unLocked',1)))
_AcTrunkAdministrativeState_Type.__name__=_C
_AcTrunkAdministrativeState_Object=MibTableColumn
acTrunkAdministrativeState=_AcTrunkAdministrativeState_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,2),_AcTrunkAdministrativeState_Type())
acTrunkAdministrativeState.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkAdministrativeState.setStatus(_A)
class _AcTrunkProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,50,51,52,53,54,55,56,57)));namedValues=NamedValues(*(('nONE',0),('e1EuroISDN',1),('t1Cas',2),('t1RawCas',3),('t1Transparent',4),('e1Transparent31',5),('e1Transparent30',6),('e1Mfcr2',7),('e1CasR2',8),('e1RawCAS',9),('t1-NI2ISDN',10),('t1-4EssISDN',11),('t1-5Ess-9-ISDN',12),('t1-5Ess-10-ISDN',13),('t1-Dms100-ISDN',14),('j1-TRANSPARENT',15),('t1-NTT-ISDN',16),('e1-AUSTEL-ISDN',17),('e1-HKT-ISDN',18),('e1-KOR-ISDN',19),('t1-HKT-ISDN',20),('e1-QSIG',21),('e1-TNZ-22',22),('t1-EXTRA-23',23),('t1-IUA',28),('e1-IUA',29),('e1-EXTRA-30',30),('e1-FRENCH-VN3-ISDN',31),('t1-EXTRA-32',32),('eXTRA-33',33),('t1-EURO-ISDN',34),('t1-DMS100-MERIDIAN-ISDN',35),('t1-NI1-ISDN',36),('e1-DUA',37),('e1-Q931-PACKETS',38),('t1-Q931-PACKETS',39),('e1-NI2-ISDN',40),('e1-CAS-R15',41),('v5',43),('bRI-EURO-ISDN',50),('bRI-NI-2',51),('bRI-DMS100',52),('bRI-5ESS',53),('bRI-QSIG',54),('bRI-VNG',55),('bRI-NTT',56),('bRI-IUA',57)))
_AcTrunkProtocolType_Type.__name__=_C
_AcTrunkProtocolType_Object=MibTableColumn
acTrunkProtocolType=_AcTrunkProtocolType_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,3),_AcTrunkProtocolType_Type())
acTrunkProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkProtocolType.setStatus(_A)
class _AcTrunkClockMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('acCLOCK-MASTER-OFF',0),('acCLOCK-MASTER-ON',1)))
_AcTrunkClockMaster_Type.__name__=_C
_AcTrunkClockMaster_Object=MibTableColumn
acTrunkClockMaster=_AcTrunkClockMaster_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,4),_AcTrunkClockMaster_Type())
acTrunkClockMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkClockMaster.setStatus(_A)
class _AcTrunkFramingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6,7,8,9,10,11)));namedValues=NamedValues(*(('eXTENDED-SUPER-FRAME',0),('sUPER-FRAME',1),('e1-FRAMING-DDF',2),('e1-FRAMING-MFF-CRC4',3),('e1-FRAMING-MFF-CRC4-EXT',4),('t1-FRAMING-F4',6),('t1-FRAMING-F12',7),('t1-FRAMING-ESF',8),('t1-FRAMING-ESF-CRC6',9),('t1-FRAMING-F72',10),('t1-FRAMING-ESF-CRC6-JT',11)))
_AcTrunkFramingMethod_Type.__name__=_C
_AcTrunkFramingMethod_Object=MibTableColumn
acTrunkFramingMethod=_AcTrunkFramingMethod_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,5),_AcTrunkFramingMethod_Type())
acTrunkFramingMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkFramingMethod.setStatus(_A)
class _AcTrunkLineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('acB8ZS',0),('acAMI',1),('acHDB3',2)))
_AcTrunkLineCode_Type.__name__=_C
_AcTrunkLineCode_Object=MibTableColumn
acTrunkLineCode=_AcTrunkLineCode_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,6),_AcTrunkLineCode_Type())
acTrunkLineCode.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkLineCode.setStatus(_A)
class _AcTrunkTraceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,10,11,12,15)));namedValues=NamedValues(*(('acNO-TRACE',0),('acFULL-ISDN-TRACE',1),('acLAYER3-ISDN-TRACE',2),('acONLY-ISDN-Q931-MSGS-TRACE',3),('acLAYER3-ISDN-TRACE-NO-DUPLICATION',4),('acFULL-ISDN-TRACE-WITH-DUPLICATION',5),('acISDN-Q931-RAW-DATA-TRACE',6),('acISDN-Q921-RAW-DATA-TRACE',7),('acISDN-Q931-Q921-RAW-DATA-TRACE',8),('acSS7-MTP2',10),('acSS7-MTP2-AND-APPLI',11),('acSS7-MTP2-SL-L3-NO-MSU',12),('acSS7-AAL',15)))
_AcTrunkTraceLevel_Type.__name__=_C
_AcTrunkTraceLevel_Object=MibTableColumn
acTrunkTraceLevel=_AcTrunkTraceLevel_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,7),_AcTrunkTraceLevel_Type())
acTrunkTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkTraceLevel.setStatus(_A)
class _AcTrunkDialPlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_AcTrunkDialPlanName_Type.__name__=_H
_AcTrunkDialPlanName_Object=MibTableColumn
acTrunkDialPlanName=_AcTrunkDialPlanName_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,8),_AcTrunkDialPlanName_Type())
acTrunkDialPlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkDialPlanName.setStatus(_A)
class _AcTrunkLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11,12,21)));namedValues=NamedValues(*(('lineTypeE1',10),('lineTypeT1',11),('lineTypeBRI',12),('lineTypeUnknown',21)))
_AcTrunkLineType_Type.__name__=_C
_AcTrunkLineType_Object=MibTableColumn
acTrunkLineType=_AcTrunkLineType_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,9),_AcTrunkLineType_Type())
acTrunkLineType.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkLineType.setStatus(_A)
class _AcTrunkAutoClockPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AcTrunkAutoClockPriority_Type.__name__=_D
_AcTrunkAutoClockPriority_Object=MibTableColumn
acTrunkAutoClockPriority=_AcTrunkAutoClockPriority_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,10),_AcTrunkAutoClockPriority_Type())
acTrunkAutoClockPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkAutoClockPriority.setStatus(_A)
class _AcTrunkDeactivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notAvailable',0),('deActivated',1),('activated',2)))
_AcTrunkDeactivate_Type.__name__=_C
_AcTrunkDeactivate_Object=MibTableColumn
acTrunkDeactivate=_AcTrunkDeactivate_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,11),_AcTrunkDeactivate_Type())
acTrunkDeactivate.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkDeactivate.setStatus(_A)
class _AcTrunkLoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noLoop',0),('lineLoop',1)))
_AcTrunkLoopbackConfig_Type.__name__=_C
_AcTrunkLoopbackConfig_Object=MibTableColumn
acTrunkLoopbackConfig=_AcTrunkLoopbackConfig_Object((1,3,6,1,4,1,5003,9,10,9,1,1,1,1,1,12),_AcTrunkLoopbackConfig_Type())
acTrunkLoopbackConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkLoopbackConfig.setStatus(_A)
_AcTrunkLine_ObjectIdentity=ObjectIdentity
acTrunkLine=_AcTrunkLine_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,2))
_AcTrunkLineTable_Object=MibTable
acTrunkLineTable=_AcTrunkLineTable_Object((1,3,6,1,4,1,5003,9,10,9,1,1,2,1))
if mibBuilder.loadTexts:acTrunkLineTable.setStatus(_A)
_AcTrunkLineEntry_Object=MibTableRow
acTrunkLineEntry=_AcTrunkLineEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,1,2,1,1))
acTrunkLineEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkLineEntry.setStatus(_A)
class _AcTrunkLineBuildOutLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ac0DB',0),('ac7-5DB',1),('ac15DB',2),('ac22-5DB',3)))
_AcTrunkLineBuildOutLoss_Type.__name__=_C
_AcTrunkLineBuildOutLoss_Object=MibTableColumn
acTrunkLineBuildOutLoss=_AcTrunkLineBuildOutLoss_Object((1,3,6,1,4,1,5003,9,10,9,1,1,2,1,1,1),_AcTrunkLineBuildOutLoss_Type())
acTrunkLineBuildOutLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkLineBuildOutLoss.setStatus(_A)
class _AcTrunkLineBuildOutOverwrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('acNO-OVER-WRITE',0),('acOVER-WRITE',1)))
_AcTrunkLineBuildOutOverwrite_Type.__name__=_C
_AcTrunkLineBuildOutOverwrite_Object=MibTableColumn
acTrunkLineBuildOutOverwrite=_AcTrunkLineBuildOutOverwrite_Object((1,3,6,1,4,1,5003,9,10,9,1,1,2,1,1,2),_AcTrunkLineBuildOutOverwrite_Type())
acTrunkLineBuildOutOverwrite.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkLineBuildOutOverwrite.setStatus(_A)
class _AcTrunkLineBuildOutXPM0_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcTrunkLineBuildOutXPM0_Type.__name__=_D
_AcTrunkLineBuildOutXPM0_Object=MibTableColumn
acTrunkLineBuildOutXPM0=_AcTrunkLineBuildOutXPM0_Object((1,3,6,1,4,1,5003,9,10,9,1,1,2,1,1,3),_AcTrunkLineBuildOutXPM0_Type())
acTrunkLineBuildOutXPM0.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkLineBuildOutXPM0.setStatus(_A)
class _AcTrunkLineBuildOutXPM1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcTrunkLineBuildOutXPM1_Type.__name__=_D
_AcTrunkLineBuildOutXPM1_Object=MibTableColumn
acTrunkLineBuildOutXPM1=_AcTrunkLineBuildOutXPM1_Object((1,3,6,1,4,1,5003,9,10,9,1,1,2,1,1,4),_AcTrunkLineBuildOutXPM1_Type())
acTrunkLineBuildOutXPM1.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkLineBuildOutXPM1.setStatus(_A)
class _AcTrunkLineBuildOutXPM2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcTrunkLineBuildOutXPM2_Type.__name__=_D
_AcTrunkLineBuildOutXPM2_Object=MibTableColumn
acTrunkLineBuildOutXPM2=_AcTrunkLineBuildOutXPM2_Object((1,3,6,1,4,1,5003,9,10,9,1,1,2,1,1,5),_AcTrunkLineBuildOutXPM2_Type())
acTrunkLineBuildOutXPM2.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkLineBuildOutXPM2.setStatus(_A)
_AcTrunkISDN_ObjectIdentity=ObjectIdentity
acTrunkISDN=_AcTrunkISDN_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,3))
_AcTrunkISDNCommon_ObjectIdentity=ObjectIdentity
acTrunkISDNCommon=_AcTrunkISDNCommon_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,3,1))
_AcTrunkISDNCommonTable_Object=MibTable
acTrunkISDNCommonTable=_AcTrunkISDNCommonTable_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1))
if mibBuilder.loadTexts:acTrunkISDNCommonTable.setStatus(_A)
_AcTrunkISDNCommonEntry_Object=MibTableRow
acTrunkISDNCommonEntry=_AcTrunkISDNCommonEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1))
acTrunkISDNCommonEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkISDNCommonEntry.setStatus(_A)
class _AcTrunkISDNCommonTerminationSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('acUSER-TERMINATION-SIDE',0),('acNETWORK-TERMINATION-SIDE',1)))
_AcTrunkISDNCommonTerminationSide_Type.__name__=_C
_AcTrunkISDNCommonTerminationSide_Object=MibTableColumn
acTrunkISDNCommonTerminationSide=_AcTrunkISDNCommonTerminationSide_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,1),_AcTrunkISDNCommonTerminationSide_Type())
acTrunkISDNCommonTerminationSide.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonTerminationSide.setStatus(_A)
class _AcTrunkISDNCommonQ931LayerResponseBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_AcTrunkISDNCommonQ931LayerResponseBehavior_Type.__name__=_C
_AcTrunkISDNCommonQ931LayerResponseBehavior_Object=MibTableColumn
acTrunkISDNCommonQ931LayerResponseBehavior=_AcTrunkISDNCommonQ931LayerResponseBehavior_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,2),_AcTrunkISDNCommonQ931LayerResponseBehavior_Type())
acTrunkISDNCommonQ931LayerResponseBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonQ931LayerResponseBehavior.setStatus(_A)
class _AcTrunkISDNCommonIncomingCallsBehavior_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AcTrunkISDNCommonIncomingCallsBehavior_Type.__name__=_D
_AcTrunkISDNCommonIncomingCallsBehavior_Object=MibTableColumn
acTrunkISDNCommonIncomingCallsBehavior=_AcTrunkISDNCommonIncomingCallsBehavior_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,3),_AcTrunkISDNCommonIncomingCallsBehavior_Type())
acTrunkISDNCommonIncomingCallsBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonIncomingCallsBehavior.setStatus(_A)
class _AcTrunkISDNCommonOutgoingCallsBehavior_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcTrunkISDNCommonOutgoingCallsBehavior_Type.__name__=_D
_AcTrunkISDNCommonOutgoingCallsBehavior_Object=MibTableColumn
acTrunkISDNCommonOutgoingCallsBehavior=_AcTrunkISDNCommonOutgoingCallsBehavior_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,4),_AcTrunkISDNCommonOutgoingCallsBehavior_Type())
acTrunkISDNCommonOutgoingCallsBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonOutgoingCallsBehavior.setStatus(_A)
class _AcTrunkISDNCommonGeneralCCBehavior_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcTrunkISDNCommonGeneralCCBehavior_Type.__name__=_D
_AcTrunkISDNCommonGeneralCCBehavior_Object=MibTableColumn
acTrunkISDNCommonGeneralCCBehavior=_AcTrunkISDNCommonGeneralCCBehavior_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,5),_AcTrunkISDNCommonGeneralCCBehavior_Type())
acTrunkISDNCommonGeneralCCBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonGeneralCCBehavior.setStatus(_A)
class _AcTrunkISDNCommonIuaInterfaceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcTrunkISDNCommonIuaInterfaceId_Type.__name__=_C
_AcTrunkISDNCommonIuaInterfaceId_Object=MibTableColumn
acTrunkISDNCommonIuaInterfaceId=_AcTrunkISDNCommonIuaInterfaceId_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,6),_AcTrunkISDNCommonIuaInterfaceId_Type())
acTrunkISDNCommonIuaInterfaceId.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkISDNCommonIuaInterfaceId.setStatus(_A)
class _AcTrunkISDNCommonDuplicateQ931BuffMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcTrunkISDNCommonDuplicateQ931BuffMode_Type.__name__=_D
_AcTrunkISDNCommonDuplicateQ931BuffMode_Object=MibTableColumn
acTrunkISDNCommonDuplicateQ931BuffMode=_AcTrunkISDNCommonDuplicateQ931BuffMode_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,7),_AcTrunkISDNCommonDuplicateQ931BuffMode_Type())
acTrunkISDNCommonDuplicateQ931BuffMode.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonDuplicateQ931BuffMode.setStatus(_A)
class _AcTrunkISDNCommonBRILayer2Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bRI-L2-MODE-P2P',0),('bRI-L2-MODE-P2MP',1)))
_AcTrunkISDNCommonBRILayer2Mode_Type.__name__=_C
_AcTrunkISDNCommonBRILayer2Mode_Object=MibTableColumn
acTrunkISDNCommonBRILayer2Mode=_AcTrunkISDNCommonBRILayer2Mode_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,8),_AcTrunkISDNCommonBRILayer2Mode_Type())
acTrunkISDNCommonBRILayer2Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonBRILayer2Mode.setStatus(_A)
class _AcTrunkISDNCommonNSBehaviour2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcTrunkISDNCommonNSBehaviour2_Type.__name__=_D
_AcTrunkISDNCommonNSBehaviour2_Object=MibTableColumn
acTrunkISDNCommonNSBehaviour2=_AcTrunkISDNCommonNSBehaviour2_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,9),_AcTrunkISDNCommonNSBehaviour2_Type())
acTrunkISDNCommonNSBehaviour2.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonNSBehaviour2.setStatus(_A)
class _AcTrunkISDNCommonRestartBChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,31))
_AcTrunkISDNCommonRestartBChannel_Type.__name__=_C
_AcTrunkISDNCommonRestartBChannel_Object=MibTableColumn
acTrunkISDNCommonRestartBChannel=_AcTrunkISDNCommonRestartBChannel_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,1,1,1,10),_AcTrunkISDNCommonRestartBChannel_Type())
acTrunkISDNCommonRestartBChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNCommonRestartBChannel.setStatus(_A)
_AcTrunkISDNNfas_ObjectIdentity=ObjectIdentity
acTrunkISDNNfas=_AcTrunkISDNNfas_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,3,2))
_AcTrunkISDNNfasTable_Object=MibTable
acTrunkISDNNfasTable=_AcTrunkISDNNfasTable_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,2,1))
if mibBuilder.loadTexts:acTrunkISDNNfasTable.setStatus(_A)
_AcTrunkISDNNfasEntry_Object=MibTableRow
acTrunkISDNNfasEntry=_AcTrunkISDNNfasEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,2,1,1))
acTrunkISDNNfasEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkISDNNfasEntry.setStatus(_A)
class _AcTrunkISDNNfasDchConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('acDCH-CONFIG-PRIMARY',0),('acDCH-CONFIG-BACKUP',1),('acDCH-CONFIG-NFAS',2)))
_AcTrunkISDNNfasDchConfig_Type.__name__=_C
_AcTrunkISDNNfasDchConfig_Object=MibTableColumn
acTrunkISDNNfasDchConfig=_AcTrunkISDNNfasDchConfig_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,2,1,1,1),_AcTrunkISDNNfasDchConfig_Type())
acTrunkISDNNfasDchConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNNfasDchConfig.setStatus(_A)
class _AcTrunkISDNNfasInterfaceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcTrunkISDNNfasInterfaceId_Type.__name__=_D
_AcTrunkISDNNfasInterfaceId_Object=MibTableColumn
acTrunkISDNNfasInterfaceId=_AcTrunkISDNNfasInterfaceId_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,2,1,1,2),_AcTrunkISDNNfasInterfaceId_Type())
acTrunkISDNNfasInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNNfasInterfaceId.setStatus(_A)
class _AcTrunkISDNNfasGroupNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_AcTrunkISDNNfasGroupNumber_Type.__name__=_D
_AcTrunkISDNNfasGroupNumber_Object=MibTableColumn
acTrunkISDNNfasGroupNumber=_AcTrunkISDNNfasGroupNumber_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,2,1,1,3),_AcTrunkISDNNfasGroupNumber_Type())
acTrunkISDNNfasGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNNfasGroupNumber.setStatus(_A)
_AcTrunkISDNDpnss_ObjectIdentity=ObjectIdentity
acTrunkISDNDpnss=_AcTrunkISDNDpnss_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,3,3))
_AcTrunkISDNDpnssTable_Object=MibTable
acTrunkISDNDpnssTable=_AcTrunkISDNDpnssTable_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,3,1))
if mibBuilder.loadTexts:acTrunkISDNDpnssTable.setStatus(_A)
_AcTrunkISDNDpnssEntry_Object=MibTableRow
acTrunkISDNDpnssEntry=_AcTrunkISDNDpnssEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,3,1,1))
acTrunkISDNDpnssEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkISDNDpnssEntry.setStatus(_A)
class _AcTrunkISDNDpnssBehavior_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcTrunkISDNDpnssBehavior_Type.__name__=_D
_AcTrunkISDNDpnssBehavior_Object=MibTableColumn
acTrunkISDNDpnssBehavior=_AcTrunkISDNDpnssBehavior_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,3,1,1,1),_AcTrunkISDNDpnssBehavior_Type())
acTrunkISDNDpnssBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNDpnssBehavior.setStatus(_A)
class _AcTrunkISDNDpnssNumRealChannels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AcTrunkISDNDpnssNumRealChannels_Type.__name__=_D
_AcTrunkISDNDpnssNumRealChannels_Object=MibTableColumn
acTrunkISDNDpnssNumRealChannels=_AcTrunkISDNDpnssNumRealChannels_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,3,1,1,2),_AcTrunkISDNDpnssNumRealChannels_Type())
acTrunkISDNDpnssNumRealChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNDpnssNumRealChannels.setStatus(_A)
class _AcTrunkISDNDpnssNumVirtualChannels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_AcTrunkISDNDpnssNumVirtualChannels_Type.__name__=_D
_AcTrunkISDNDpnssNumVirtualChannels_Object=MibTableColumn
acTrunkISDNDpnssNumVirtualChannels=_AcTrunkISDNDpnssNumVirtualChannels_Object((1,3,6,1,4,1,5003,9,10,9,1,1,3,3,1,1,3),_AcTrunkISDNDpnssNumVirtualChannels_Type())
acTrunkISDNDpnssNumVirtualChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkISDNDpnssNumVirtualChannels.setStatus(_A)
_AcTrunkCAS_ObjectIdentity=ObjectIdentity
acTrunkCAS=_AcTrunkCAS_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,4))
_AcTrunkCASTable_Object=MibTable
acTrunkCASTable=_AcTrunkCASTable_Object((1,3,6,1,4,1,5003,9,10,9,1,1,4,1))
if mibBuilder.loadTexts:acTrunkCASTable.setStatus(_A)
_AcTrunkCASEntry_Object=MibTableRow
acTrunkCASEntry=_AcTrunkCASEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,1,4,1,1))
acTrunkCASEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkCASEntry.setStatus(_A)
class _AcTrunkCASTablesIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcTrunkCASTablesIndex_Type.__name__=_D
_AcTrunkCASTablesIndex_Object=MibTableColumn
acTrunkCASTablesIndex=_AcTrunkCASTablesIndex_Object((1,3,6,1,4,1,5003,9,10,9,1,1,4,1,1,1),_AcTrunkCASTablesIndex_Type())
acTrunkCASTablesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkCASTablesIndex.setStatus(_A)
class _AcTrunkCASTablePerChannel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AcTrunkCASTablePerChannel_Type.__name__=_H
_AcTrunkCASTablePerChannel_Object=MibTableColumn
acTrunkCASTablePerChannel=_AcTrunkCASTablePerChannel_Object((1,3,6,1,4,1,5003,9,10,9,1,1,4,1,1,2),_AcTrunkCASTablePerChannel_Type())
acTrunkCASTablePerChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkCASTablePerChannel.setStatus(_A)
_AcTrunkV5_ObjectIdentity=ObjectIdentity
acTrunkV5=_AcTrunkV5_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,5))
_AcTrunkV5Table_Object=MibTable
acTrunkV5Table=_AcTrunkV5Table_Object((1,3,6,1,4,1,5003,9,10,9,1,1,5,1))
if mibBuilder.loadTexts:acTrunkV5Table.setStatus(_A)
_AcTrunkV5Entry_Object=MibTableRow
acTrunkV5Entry=_AcTrunkV5Entry_Object((1,3,6,1,4,1,5003,9,10,9,1,1,5,1,1))
acTrunkV5Entry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkV5Entry.setStatus(_A)
class _AcTrunkV5NumberOfCChannels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcTrunkV5NumberOfCChannels_Type.__name__=_D
_AcTrunkV5NumberOfCChannels_Object=MibTableColumn
acTrunkV5NumberOfCChannels=_AcTrunkV5NumberOfCChannels_Object((1,3,6,1,4,1,5003,9,10,9,1,1,5,1,1,1),_AcTrunkV5NumberOfCChannels_Type())
acTrunkV5NumberOfCChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkV5NumberOfCChannels.setStatus(_A)
class _AcTrunkV5ProtocolSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('an-Side',0),('le-Side',1)))
_AcTrunkV5ProtocolSide_Type.__name__=_C
_AcTrunkV5ProtocolSide_Object=MibTableColumn
acTrunkV5ProtocolSide=_AcTrunkV5ProtocolSide_Object((1,3,6,1,4,1,5003,9,10,9,1,1,5,1,1,2),_AcTrunkV5ProtocolSide_Type())
acTrunkV5ProtocolSide.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkV5ProtocolSide.setStatus(_A)
_AcTrunkGlobal_ObjectIdentity=ObjectIdentity
acTrunkGlobal=_AcTrunkGlobal_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,1,8))
class _AcTrunkGlobalLifeLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('hW-Only',0),('hW-And-Link-Detection',1),('hW-And-Link-And-Network-Detection',2)))
_AcTrunkGlobalLifeLineType_Type.__name__=_C
_AcTrunkGlobalLifeLineType_Object=MibScalar
acTrunkGlobalLifeLineType=_AcTrunkGlobalLifeLineType_Object((1,3,6,1,4,1,5003,9,10,9,1,1,8,1),_AcTrunkGlobalLifeLineType_Type())
acTrunkGlobalLifeLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkGlobalLifeLineType.setStatus(_A)
class _AcTrunkGlobalBChannelAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AcTrunkGlobalBChannelAlarms_Type.__name__=_C
_AcTrunkGlobalBChannelAlarms_Object=MibScalar
acTrunkGlobalBChannelAlarms=_AcTrunkGlobalBChannelAlarms_Object((1,3,6,1,4,1,5003,9,10,9,1,1,8,2),_AcTrunkGlobalBChannelAlarms_Type())
acTrunkGlobalBChannelAlarms.setMaxAccess(_B)
if mibBuilder.loadTexts:acTrunkGlobalBChannelAlarms.setStatus(_A)
_AcISDNConfig_ObjectIdentity=ObjectIdentity
acISDNConfig=_AcISDNConfig_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,2))
_AcMiscISDN_ObjectIdentity=ObjectIdentity
acMiscISDN=_AcMiscISDN_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,2,1))
class _AcMiscISDNQ931RelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*(('none',0),('activateLAPDmessaging',1),('layer3-IS-IUA',3)))
_AcMiscISDNQ931RelayMode_Type.__name__=_C
_AcMiscISDNQ931RelayMode_Object=MibScalar
acMiscISDNQ931RelayMode=_AcMiscISDNQ931RelayMode_Object((1,3,6,1,4,1,5003,9,10,9,1,2,1,1),_AcMiscISDNQ931RelayMode_Type())
acMiscISDNQ931RelayMode.setMaxAccess(_B)
if mibBuilder.loadTexts:acMiscISDNQ931RelayMode.setStatus(_A)
class _AcMiscISDNDuplicateQ931BuffMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcMiscISDNDuplicateQ931BuffMode_Type.__name__=_D
_AcMiscISDNDuplicateQ931BuffMode_Object=MibScalar
acMiscISDNDuplicateQ931BuffMode=_AcMiscISDNDuplicateQ931BuffMode_Object((1,3,6,1,4,1,5003,9,10,9,1,2,1,2),_AcMiscISDNDuplicateQ931BuffMode_Type())
acMiscISDNDuplicateQ931BuffMode.setMaxAccess(_B)
if mibBuilder.loadTexts:acMiscISDNDuplicateQ931BuffMode.setStatus(_K)
_AcDS3Config_ObjectIdentity=ObjectIdentity
acDS3Config=_AcDS3Config_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,3))
class _AcDS3ConfigFramingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dS3-M23',0),('dS3-C-BIT-PARITY',1)))
_AcDS3ConfigFramingMethod_Type.__name__=_C
_AcDS3ConfigFramingMethod_Object=MibScalar
acDS3ConfigFramingMethod=_AcDS3ConfigFramingMethod_Object((1,3,6,1,4,1,5003,9,10,9,1,3,1),_AcDS3ConfigFramingMethod_Type())
acDS3ConfigFramingMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:acDS3ConfigFramingMethod.setStatus(_K)
class _AcDS3ConfigClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('acClock-Source-External',0),('acClock-Source-Local-Board',1),('acClock-Source-Local-PLL',2)))
_AcDS3ConfigClockSource_Type.__name__=_C
_AcDS3ConfigClockSource_Object=MibScalar
acDS3ConfigClockSource=_AcDS3ConfigClockSource_Object((1,3,6,1,4,1,5003,9,10,9,1,3,2),_AcDS3ConfigClockSource_Type())
acDS3ConfigClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:acDS3ConfigClockSource.setStatus(_K)
class _AcDS3ConfigLineBuiltOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('acLINE-BUILT-OUT-LEVEL-1',0),('acLINE-BUILT-OUT-LEVEL-2',1),('acLINE-BUILT-OUT-LEVEL-3',2),('acLINE-BUILT-OUT-LEVEL-4',3),('acLINE-BUILT-OUT-LEVEL-5',4),('acLINE-BUILT-OUT-LEVEL-6',5)))
_AcDS3ConfigLineBuiltOut_Type.__name__=_C
_AcDS3ConfigLineBuiltOut_Object=MibScalar
acDS3ConfigLineBuiltOut=_AcDS3ConfigLineBuiltOut_Object((1,3,6,1,4,1,5003,9,10,9,1,3,3),_AcDS3ConfigLineBuiltOut_Type())
acDS3ConfigLineBuiltOut.setMaxAccess(_B)
if mibBuilder.loadTexts:acDS3ConfigLineBuiltOut.setStatus(_K)
_AcCasConfig_ObjectIdentity=ObjectIdentity
acCasConfig=_AcCasConfig_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,4))
class _AcCasConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AcCasConfigEnable_Type.__name__=_C
_AcCasConfigEnable_Object=MibScalar
acCasConfigEnable=_AcCasConfigEnable_Object((1,3,6,1,4,1,5003,9,10,9,1,4,1),_AcCasConfigEnable_Type())
acCasConfigEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:acCasConfigEnable.setStatus(_A)
_AcCASFile_ObjectIdentity=ObjectIdentity
acCASFile=_AcCASFile_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,4,2))
_AcCASFileTable_Object=MibTable
acCASFileTable=_AcCASFileTable_Object((1,3,6,1,4,1,5003,9,10,9,1,4,2,1))
if mibBuilder.loadTexts:acCASFileTable.setStatus(_A)
_AcCASFileEntry_Object=MibTableRow
acCASFileEntry=_AcCASFileEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,4,2,1,1))
acCASFileEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:acCASFileEntry.setStatus(_A)
class _AcCASFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcCASFileIndex_Type.__name__=_D
_AcCASFileIndex_Object=MibTableColumn
acCASFileIndex=_AcCASFileIndex_Object((1,3,6,1,4,1,5003,9,10,9,1,4,2,1,1,1),_AcCASFileIndex_Type())
acCASFileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acCASFileIndex.setStatus(_A)
class _AcCASFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AcCASFileName_Type.__name__=_H
_AcCASFileName_Object=MibTableColumn
acCASFileName=_AcCASFileName_Object((1,3,6,1,4,1,5003,9,10,9,1,4,2,1,1,2),_AcCASFileName_Type())
acCASFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:acCASFileName.setStatus(_A)
_AcSonetSDH_ObjectIdentity=ObjectIdentity
acSonetSDH=_AcSonetSDH_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,1,5))
_AcSonetSDHTable_Object=MibTable
acSonetSDHTable=_AcSonetSDHTable_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1))
if mibBuilder.loadTexts:acSonetSDHTable.setStatus(_A)
_AcSonetSDHEntry_Object=MibTableRow
acSonetSDHEntry=_AcSonetSDHEntry_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1,1))
acSonetSDHEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:acSonetSDHEntry.setStatus(_A)
class _AcSonetSDHIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AcSonetSDHIndex_Type.__name__=_D
_AcSonetSDHIndex_Object=MibTableColumn
acSonetSDHIndex=_AcSonetSDHIndex_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1,1,1),_AcSonetSDHIndex_Type())
acSonetSDHIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:acSonetSDHIndex.setStatus(_A)
class _AcSonetSDHFbrGrpMappingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,15)));namedValues=NamedValues(*(('asynchronousVT15andDS1',0),('asynchronousTU12andE1',1),('sTS1asynchronousDS3',3),('undefined',15)))
_AcSonetSDHFbrGrpMappingType_Type.__name__=_C
_AcSonetSDHFbrGrpMappingType_Object=MibTableColumn
acSonetSDHFbrGrpMappingType=_AcSonetSDHFbrGrpMappingType_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1,1,2),_AcSonetSDHFbrGrpMappingType_Type())
acSonetSDHFbrGrpMappingType.setMaxAccess(_B)
if mibBuilder.loadTexts:acSonetSDHFbrGrpMappingType.setStatus(_A)
class _AcSonetSDHFbrGrpKlmNumberingScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('numberingScheme-MLK',0),('numberingScheme-LMK',1),('numberingScheme-KLM',2)))
_AcSonetSDHFbrGrpKlmNumberingScheme_Type.__name__=_C
_AcSonetSDHFbrGrpKlmNumberingScheme_Object=MibTableColumn
acSonetSDHFbrGrpKlmNumberingScheme=_AcSonetSDHFbrGrpKlmNumberingScheme_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1,1,3),_AcSonetSDHFbrGrpKlmNumberingScheme_Type())
acSonetSDHFbrGrpKlmNumberingScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:acSonetSDHFbrGrpKlmNumberingScheme.setStatus(_A)
class _AcSonetSDHFbrGrpAPSDirectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unidirectional',0),('bidirectional',1)))
_AcSonetSDHFbrGrpAPSDirectionMode_Type.__name__=_C
_AcSonetSDHFbrGrpAPSDirectionMode_Object=MibTableColumn
acSonetSDHFbrGrpAPSDirectionMode=_AcSonetSDHFbrGrpAPSDirectionMode_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1,1,4),_AcSonetSDHFbrGrpAPSDirectionMode_Type())
acSonetSDHFbrGrpAPSDirectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:acSonetSDHFbrGrpAPSDirectionMode.setStatus(_A)
class _AcSonetSDHFbrGrpAPSRevertMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nonRevertive',0),('revertive',1)))
_AcSonetSDHFbrGrpAPSRevertMode_Type.__name__=_C
_AcSonetSDHFbrGrpAPSRevertMode_Object=MibTableColumn
acSonetSDHFbrGrpAPSRevertMode=_AcSonetSDHFbrGrpAPSRevertMode_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1,1,5),_AcSonetSDHFbrGrpAPSRevertMode_Type())
acSonetSDHFbrGrpAPSRevertMode.setMaxAccess(_B)
if mibBuilder.loadTexts:acSonetSDHFbrGrpAPSRevertMode.setStatus(_A)
class _AcSonetSDHFbrGrpAPSWaitToRestoreTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,12))
_AcSonetSDHFbrGrpAPSWaitToRestoreTime_Type.__name__=_D
_AcSonetSDHFbrGrpAPSWaitToRestoreTime_Object=MibTableColumn
acSonetSDHFbrGrpAPSWaitToRestoreTime=_AcSonetSDHFbrGrpAPSWaitToRestoreTime_Object((1,3,6,1,4,1,5003,9,10,9,1,5,1,1,6),_AcSonetSDHFbrGrpAPSWaitToRestoreTime_Type())
acSonetSDHFbrGrpAPSWaitToRestoreTime.setMaxAccess(_B)
if mibBuilder.loadTexts:acSonetSDHFbrGrpAPSWaitToRestoreTime.setStatus(_A)
_AcPSTNStatus_ObjectIdentity=ObjectIdentity
acPSTNStatus=_AcPSTNStatus_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,2))
_AcTrunkStatus_ObjectIdentity=ObjectIdentity
acTrunkStatus=_AcTrunkStatus_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,2,1))
_AcTrunkStatusTable_Object=MibTable
acTrunkStatusTable=_AcTrunkStatusTable_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1))
if mibBuilder.loadTexts:acTrunkStatusTable.setStatus(_A)
_AcTrunkStatusEntry_Object=MibTableRow
acTrunkStatusEntry=_AcTrunkStatusEntry_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1))
acTrunkStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acTrunkStatusEntry.setStatus(_A)
class _AcTrunkStatusLedStatusColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('red',1),('green',2)))
_AcTrunkStatusLedStatusColor_Type.__name__=_C
_AcTrunkStatusLedStatusColor_Object=MibTableColumn
acTrunkStatusLedStatusColor=_AcTrunkStatusLedStatusColor_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,1),_AcTrunkStatusLedStatusColor_Type())
acTrunkStatusLedStatusColor.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusLedStatusColor.setStatus(_A)
class _AcTrunkStatusLedStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('steady',0),('blink',1)))
_AcTrunkStatusLedStatusState_Type.__name__=_C
_AcTrunkStatusLedStatusState_Object=MibTableColumn
acTrunkStatusLedStatusState=_AcTrunkStatusLedStatusState_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,2),_AcTrunkStatusLedStatusState_Type())
acTrunkStatusLedStatusState.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusLedStatusState.setStatus(_A)
class _AcTrunkStatusChannels_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AcTrunkStatusChannels_Type.__name__=_P
_AcTrunkStatusChannels_Object=MibTableColumn
acTrunkStatusChannels=_AcTrunkStatusChannels_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,3),_AcTrunkStatusChannels_Type())
acTrunkStatusChannels.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusChannels.setStatus(_A)
class _AcTrunkStatusV5InterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,31))
_AcTrunkStatusV5InterfaceNum_Type.__name__=_C
_AcTrunkStatusV5InterfaceNum_Object=MibTableColumn
acTrunkStatusV5InterfaceNum=_AcTrunkStatusV5InterfaceNum_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,4),_AcTrunkStatusV5InterfaceNum_Type())
acTrunkStatusV5InterfaceNum.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusV5InterfaceNum.setStatus(_A)
class _AcTrunkStatusV5LinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,62))
_AcTrunkStatusV5LinkID_Type.__name__=_C
_AcTrunkStatusV5LinkID_Object=MibTableColumn
acTrunkStatusV5LinkID=_AcTrunkStatusV5LinkID_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,5),_AcTrunkStatusV5LinkID_Type())
acTrunkStatusV5LinkID.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusV5LinkID.setStatus(_A)
class _AcTrunkStatusDChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,10)));namedValues=NamedValues(*(('dChannelEstablished',0),('dChannelNotEstablished',1),(_M,10)))
_AcTrunkStatusDChannel_Type.__name__=_C
_AcTrunkStatusDChannel_Object=MibTableColumn
acTrunkStatusDChannel=_AcTrunkStatusDChannel_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,6),_AcTrunkStatusDChannel_Type())
acTrunkStatusDChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusDChannel.setStatus(_A)
class _AcTrunkStatusAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('greyDisabled',0),('greenActive',1),('redLosLof',2),('blueAis',3),('yellowRai',4),('orangeDChannel',5),('purpleLowerLayerDown',6),('darkOrangeNFASAlarm',7)))
_AcTrunkStatusAlarm_Type.__name__=_C
_AcTrunkStatusAlarm_Object=MibTableColumn
acTrunkStatusAlarm=_AcTrunkStatusAlarm_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,7),_AcTrunkStatusAlarm_Type())
acTrunkStatusAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusAlarm.setStatus(_A)
class _AcTrunkStatusDchannelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_M,2)))
_AcTrunkStatusDchannelActivity_Type.__name__=_C
_AcTrunkStatusDchannelActivity_Object=MibTableColumn
acTrunkStatusDchannelActivity=_AcTrunkStatusDchannelActivity_Object((1,3,6,1,4,1,5003,9,10,9,2,1,1,1,8),_AcTrunkStatusDchannelActivity_Type())
acTrunkStatusDchannelActivity.setMaxAccess(_E)
if mibBuilder.loadTexts:acTrunkStatusDchannelActivity.setStatus(_A)
_AcDigitalLegs_ObjectIdentity=ObjectIdentity
acDigitalLegs=_AcDigitalLegs_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,2,2))
_AcDigitalLegsTable_Object=MibTable
acDigitalLegsTable=_AcDigitalLegsTable_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1))
if mibBuilder.loadTexts:acDigitalLegsTable.setStatus(_A)
_AcDigitalLegsEntry_Object=MibTableRow
acDigitalLegsEntry=_AcDigitalLegsEntry_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1))
acDigitalLegsEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:acDigitalLegsEntry.setStatus(_A)
class _AcDigitalLegsLegIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcDigitalLegsLegIndex_Type.__name__=_D
_AcDigitalLegsLegIndex_Object=MibTableColumn
acDigitalLegsLegIndex=_AcDigitalLegsLegIndex_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,1),_AcDigitalLegsLegIndex_Type())
acDigitalLegsLegIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:acDigitalLegsLegIndex.setStatus(_A)
class _AcDigitalLegsCallIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcDigitalLegsCallIndex_Type.__name__=_D
_AcDigitalLegsCallIndex_Object=MibTableColumn
acDigitalLegsCallIndex=_AcDigitalLegsCallIndex_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,2),_AcDigitalLegsCallIndex_Type())
acDigitalLegsCallIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsCallIndex.setStatus(_A)
class _AcDigitalLegsTrunk_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcDigitalLegsTrunk_Type.__name__=_D
_AcDigitalLegsTrunk_Object=MibTableColumn
acDigitalLegsTrunk=_AcDigitalLegsTrunk_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,3),_AcDigitalLegsTrunk_Type())
acDigitalLegsTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsTrunk.setStatus(_A)
class _AcDigitalLegsBchannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76500))
_AcDigitalLegsBchannel_Type.__name__=_D
_AcDigitalLegsBchannel_Object=MibTableColumn
acDigitalLegsBchannel=_AcDigitalLegsBchannel_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,4),_AcDigitalLegsBchannel_Type())
acDigitalLegsBchannel.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsBchannel.setStatus(_A)
class _AcDigitalLegsEchoCanceller_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AcDigitalLegsEchoCanceller_Type.__name__=_C
_AcDigitalLegsEchoCanceller_Object=MibTableColumn
acDigitalLegsEchoCanceller=_AcDigitalLegsEchoCanceller_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,5),_AcDigitalLegsEchoCanceller_Type())
acDigitalLegsEchoCanceller.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsEchoCanceller.setStatus(_A)
class _AcDigitalLegsDTMFDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AcDigitalLegsDTMFDetection_Type.__name__=_C
_AcDigitalLegsDTMFDetection_Object=MibTableColumn
acDigitalLegsDTMFDetection=_AcDigitalLegsDTMFDetection_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,6),_AcDigitalLegsDTMFDetection_Type())
acDigitalLegsDTMFDetection.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsDTMFDetection.setStatus(_A)
class _AcDigitalLegsVoiceVolume_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_AcDigitalLegsVoiceVolume_Type.__name__=_D
_AcDigitalLegsVoiceVolume_Object=MibTableColumn
acDigitalLegsVoiceVolume=_AcDigitalLegsVoiceVolume_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,7),_AcDigitalLegsVoiceVolume_Type())
acDigitalLegsVoiceVolume.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsVoiceVolume.setStatus(_A)
class _AcDigitalLegsHighPassFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AcDigitalLegsHighPassFilter_Type.__name__=_C
_AcDigitalLegsHighPassFilter_Object=MibTableColumn
acDigitalLegsHighPassFilter=_AcDigitalLegsHighPassFilter_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,8),_AcDigitalLegsHighPassFilter_Type())
acDigitalLegsHighPassFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsHighPassFilter.setStatus(_A)
class _AcDigitalLegsInputGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AcDigitalLegsInputGain_Type.__name__=_C
_AcDigitalLegsInputGain_Object=MibTableColumn
acDigitalLegsInputGain=_AcDigitalLegsInputGain_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,9),_AcDigitalLegsInputGain_Type())
acDigitalLegsInputGain.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsInputGain.setStatus(_A)
class _AcDigitalLegsDSPDevice_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_AcDigitalLegsDSPDevice_Type.__name__=_D
_AcDigitalLegsDSPDevice_Object=MibTableColumn
acDigitalLegsDSPDevice=_AcDigitalLegsDSPDevice_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,10),_AcDigitalLegsDSPDevice_Type())
acDigitalLegsDSPDevice.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsDSPDevice.setStatus(_A)
class _AcDigitalLegsLegName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AcDigitalLegsLegName_Type.__name__=_H
_AcDigitalLegsLegName_Object=MibTableColumn
acDigitalLegsLegName=_AcDigitalLegsLegName_Object((1,3,6,1,4,1,5003,9,10,9,2,2,1,1,11),_AcDigitalLegsLegName_Type())
acDigitalLegsLegName.setMaxAccess(_E)
if mibBuilder.loadTexts:acDigitalLegsLegName.setStatus(_A)
_AcSDHKLMNumberingScheme_ObjectIdentity=ObjectIdentity
acSDHKLMNumberingScheme=_AcSDHKLMNumberingScheme_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,2,3))
_AcSDHKLMNumberingSchemeTable_Object=MibTable
acSDHKLMNumberingSchemeTable=_AcSDHKLMNumberingSchemeTable_Object((1,3,6,1,4,1,5003,9,10,9,2,3,1))
if mibBuilder.loadTexts:acSDHKLMNumberingSchemeTable.setStatus(_A)
_AcSDHKLMNumberingSchemeEntry_Object=MibTableRow
acSDHKLMNumberingSchemeEntry=_AcSDHKLMNumberingSchemeEntry_Object((1,3,6,1,4,1,5003,9,10,9,2,3,1,1))
acSDHKLMNumberingSchemeEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:acSDHKLMNumberingSchemeEntry.setStatus(_A)
class _AcSDHKLMNumberingSchemeTrunkIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcSDHKLMNumberingSchemeTrunkIndex_Type.__name__=_D
_AcSDHKLMNumberingSchemeTrunkIndex_Object=MibTableColumn
acSDHKLMNumberingSchemeTrunkIndex=_AcSDHKLMNumberingSchemeTrunkIndex_Object((1,3,6,1,4,1,5003,9,10,9,2,3,1,1,1),_AcSDHKLMNumberingSchemeTrunkIndex_Type())
acSDHKLMNumberingSchemeTrunkIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:acSDHKLMNumberingSchemeTrunkIndex.setStatus(_A)
class _AcSDHKLMNumberingSchemeTUG3OrSTS1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AcSDHKLMNumberingSchemeTUG3OrSTS1_Type.__name__=_D
_AcSDHKLMNumberingSchemeTUG3OrSTS1_Object=MibTableColumn
acSDHKLMNumberingSchemeTUG3OrSTS1=_AcSDHKLMNumberingSchemeTUG3OrSTS1_Object((1,3,6,1,4,1,5003,9,10,9,2,3,1,1,2),_AcSDHKLMNumberingSchemeTUG3OrSTS1_Type())
acSDHKLMNumberingSchemeTUG3OrSTS1.setMaxAccess(_E)
if mibBuilder.loadTexts:acSDHKLMNumberingSchemeTUG3OrSTS1.setStatus(_A)
class _AcSDHKLMNumberingSchemeTUG2OrVTG_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AcSDHKLMNumberingSchemeTUG2OrVTG_Type.__name__=_D
_AcSDHKLMNumberingSchemeTUG2OrVTG_Object=MibTableColumn
acSDHKLMNumberingSchemeTUG2OrVTG=_AcSDHKLMNumberingSchemeTUG2OrVTG_Object((1,3,6,1,4,1,5003,9,10,9,2,3,1,1,3),_AcSDHKLMNumberingSchemeTUG2OrVTG_Type())
acSDHKLMNumberingSchemeTUG2OrVTG.setMaxAccess(_E)
if mibBuilder.loadTexts:acSDHKLMNumberingSchemeTUG2OrVTG.setStatus(_A)
class _AcSDHKLMNumberingSchemeTU12OrVT15_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AcSDHKLMNumberingSchemeTU12OrVT15_Type.__name__=_D
_AcSDHKLMNumberingSchemeTU12OrVT15_Object=MibTableColumn
acSDHKLMNumberingSchemeTU12OrVT15=_AcSDHKLMNumberingSchemeTU12OrVT15_Object((1,3,6,1,4,1,5003,9,10,9,2,3,1,1,4),_AcSDHKLMNumberingSchemeTU12OrVT15_Type())
acSDHKLMNumberingSchemeTU12OrVT15.setMaxAccess(_E)
if mibBuilder.loadTexts:acSDHKLMNumberingSchemeTU12OrVT15.setStatus(_A)
_AcFiberGroupStatus_ObjectIdentity=ObjectIdentity
acFiberGroupStatus=_AcFiberGroupStatus_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,2,4))
class _AcFiberGroupStatusActiveLink_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcFiberGroupStatusActiveLink_Type.__name__=_D
_AcFiberGroupStatusActiveLink_Object=MibScalar
acFiberGroupStatusActiveLink=_AcFiberGroupStatusActiveLink_Object((1,3,6,1,4,1,5003,9,10,9,2,4,1),_AcFiberGroupStatusActiveLink_Type())
acFiberGroupStatusActiveLink.setMaxAccess(_E)
if mibBuilder.loadTexts:acFiberGroupStatusActiveLink.setStatus(_A)
_AcNFASGroupStatus_ObjectIdentity=ObjectIdentity
acNFASGroupStatus=_AcNFASGroupStatus_ObjectIdentity((1,3,6,1,4,1,5003,9,10,9,2,5))
_AcNFASGroupStatusTable_Object=MibTable
acNFASGroupStatusTable=_AcNFASGroupStatusTable_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1))
if mibBuilder.loadTexts:acNFASGroupStatusTable.setStatus(_A)
_AcNFASGroupStatusEntry_Object=MibTableRow
acNFASGroupStatusEntry=_AcNFASGroupStatusEntry_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1))
acNFASGroupStatusEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:acNFASGroupStatusEntry.setStatus(_A)
class _AcNFASGroupStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_AcNFASGroupStatusIndex_Type.__name__=_D
_AcNFASGroupStatusIndex_Object=MibTableColumn
acNFASGroupStatusIndex=_AcNFASGroupStatusIndex_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,1),_AcNFASGroupStatusIndex_Type())
acNFASGroupStatusIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:acNFASGroupStatusIndex.setStatus(_A)
class _AcNFASGroupStatusGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*(('notExists',-1),('inService',0),('outOfService',1),('swactInProgress',2)))
_AcNFASGroupStatusGroupStatus_Type.__name__=_C
_AcNFASGroupStatusGroupStatus_Object=MibTableColumn
acNFASGroupStatusGroupStatus=_AcNFASGroupStatusGroupStatus_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,2),_AcNFASGroupStatusGroupStatus_Type())
acNFASGroupStatusGroupStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:acNFASGroupStatusGroupStatus.setStatus(_A)
class _AcNFASGroupStatusPrimaryDChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,83))
_AcNFASGroupStatusPrimaryDChannel_Type.__name__=_C
_AcNFASGroupStatusPrimaryDChannel_Object=MibTableColumn
acNFASGroupStatusPrimaryDChannel=_AcNFASGroupStatusPrimaryDChannel_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,3),_AcNFASGroupStatusPrimaryDChannel_Type())
acNFASGroupStatusPrimaryDChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:acNFASGroupStatusPrimaryDChannel.setStatus(_A)
class _AcNFASGroupStatusBackupDChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,83))
_AcNFASGroupStatusBackupDChannel_Type.__name__=_C
_AcNFASGroupStatusBackupDChannel_Object=MibTableColumn
acNFASGroupStatusBackupDChannel=_AcNFASGroupStatusBackupDChannel_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,4),_AcNFASGroupStatusBackupDChannel_Type())
acNFASGroupStatusBackupDChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:acNFASGroupStatusBackupDChannel.setStatus(_A)
class _AcNFASGroupStatusAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('actionDone',0),('switchOver',1)))
_AcNFASGroupStatusAction_Type.__name__=_C
_AcNFASGroupStatusAction_Object=MibTableColumn
acNFASGroupStatusAction=_AcNFASGroupStatusAction_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,5),_AcNFASGroupStatusAction_Type())
acNFASGroupStatusAction.setMaxAccess(_B)
if mibBuilder.loadTexts:acNFASGroupStatusAction.setStatus(_A)
class _AcNFASGroupStatusActionResult_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcNFASGroupStatusActionResult_Type.__name__=_H
_AcNFASGroupStatusActionResult_Object=MibTableColumn
acNFASGroupStatusActionResult=_AcNFASGroupStatusActionResult_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,6),_AcNFASGroupStatusActionResult_Type())
acNFASGroupStatusActionResult.setMaxAccess(_E)
if mibBuilder.loadTexts:acNFASGroupStatusActionResult.setStatus(_A)
class _AcNFASGroupStatusPrimaryDChannelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_M,2)))
_AcNFASGroupStatusPrimaryDChannelActivity_Type.__name__=_C
_AcNFASGroupStatusPrimaryDChannelActivity_Object=MibTableColumn
acNFASGroupStatusPrimaryDChannelActivity=_AcNFASGroupStatusPrimaryDChannelActivity_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,7),_AcNFASGroupStatusPrimaryDChannelActivity_Type())
acNFASGroupStatusPrimaryDChannelActivity.setMaxAccess(_E)
if mibBuilder.loadTexts:acNFASGroupStatusPrimaryDChannelActivity.setStatus(_A)
class _AcNFASGroupStatusBackupDChannelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_M,2)))
_AcNFASGroupStatusBackupDChannelActivity_Type.__name__=_C
_AcNFASGroupStatusBackupDChannelActivity_Object=MibTableColumn
acNFASGroupStatusBackupDChannelActivity=_AcNFASGroupStatusBackupDChannelActivity_Object((1,3,6,1,4,1,5003,9,10,9,2,5,1,1,8),_AcNFASGroupStatusBackupDChannelActivity_Type())
acNFASGroupStatusBackupDChannelActivity.setMaxAccess(_E)
if mibBuilder.loadTexts:acNFASGroupStatusBackupDChannelActivity.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'acPSTN':acPSTN,'acPSTNConfiguration':acPSTNConfiguration,'acTrunkConfig':acTrunkConfig,'acTrunk':acTrunk,'acTrunkTable':acTrunkTable,'acTrunkEntry':acTrunkEntry,_G:acTrunkIndex,'acTrunkAdministrativeState':acTrunkAdministrativeState,'acTrunkProtocolType':acTrunkProtocolType,'acTrunkClockMaster':acTrunkClockMaster,'acTrunkFramingMethod':acTrunkFramingMethod,'acTrunkLineCode':acTrunkLineCode,'acTrunkTraceLevel':acTrunkTraceLevel,'acTrunkDialPlanName':acTrunkDialPlanName,'acTrunkLineType':acTrunkLineType,'acTrunkAutoClockPriority':acTrunkAutoClockPriority,'acTrunkDeactivate':acTrunkDeactivate,'acTrunkLoopbackConfig':acTrunkLoopbackConfig,'acTrunkLine':acTrunkLine,'acTrunkLineTable':acTrunkLineTable,'acTrunkLineEntry':acTrunkLineEntry,'acTrunkLineBuildOutLoss':acTrunkLineBuildOutLoss,'acTrunkLineBuildOutOverwrite':acTrunkLineBuildOutOverwrite,'acTrunkLineBuildOutXPM0':acTrunkLineBuildOutXPM0,'acTrunkLineBuildOutXPM1':acTrunkLineBuildOutXPM1,'acTrunkLineBuildOutXPM2':acTrunkLineBuildOutXPM2,'acTrunkISDN':acTrunkISDN,'acTrunkISDNCommon':acTrunkISDNCommon,'acTrunkISDNCommonTable':acTrunkISDNCommonTable,'acTrunkISDNCommonEntry':acTrunkISDNCommonEntry,'acTrunkISDNCommonTerminationSide':acTrunkISDNCommonTerminationSide,'acTrunkISDNCommonQ931LayerResponseBehavior':acTrunkISDNCommonQ931LayerResponseBehavior,'acTrunkISDNCommonIncomingCallsBehavior':acTrunkISDNCommonIncomingCallsBehavior,'acTrunkISDNCommonOutgoingCallsBehavior':acTrunkISDNCommonOutgoingCallsBehavior,'acTrunkISDNCommonGeneralCCBehavior':acTrunkISDNCommonGeneralCCBehavior,'acTrunkISDNCommonIuaInterfaceId':acTrunkISDNCommonIuaInterfaceId,'acTrunkISDNCommonDuplicateQ931BuffMode':acTrunkISDNCommonDuplicateQ931BuffMode,'acTrunkISDNCommonBRILayer2Mode':acTrunkISDNCommonBRILayer2Mode,'acTrunkISDNCommonNSBehaviour2':acTrunkISDNCommonNSBehaviour2,'acTrunkISDNCommonRestartBChannel':acTrunkISDNCommonRestartBChannel,'acTrunkISDNNfas':acTrunkISDNNfas,'acTrunkISDNNfasTable':acTrunkISDNNfasTable,'acTrunkISDNNfasEntry':acTrunkISDNNfasEntry,'acTrunkISDNNfasDchConfig':acTrunkISDNNfasDchConfig,'acTrunkISDNNfasInterfaceId':acTrunkISDNNfasInterfaceId,'acTrunkISDNNfasGroupNumber':acTrunkISDNNfasGroupNumber,'acTrunkISDNDpnss':acTrunkISDNDpnss,'acTrunkISDNDpnssTable':acTrunkISDNDpnssTable,'acTrunkISDNDpnssEntry':acTrunkISDNDpnssEntry,'acTrunkISDNDpnssBehavior':acTrunkISDNDpnssBehavior,'acTrunkISDNDpnssNumRealChannels':acTrunkISDNDpnssNumRealChannels,'acTrunkISDNDpnssNumVirtualChannels':acTrunkISDNDpnssNumVirtualChannels,'acTrunkCAS':acTrunkCAS,'acTrunkCASTable':acTrunkCASTable,'acTrunkCASEntry':acTrunkCASEntry,'acTrunkCASTablesIndex':acTrunkCASTablesIndex,'acTrunkCASTablePerChannel':acTrunkCASTablePerChannel,'acTrunkV5':acTrunkV5,'acTrunkV5Table':acTrunkV5Table,'acTrunkV5Entry':acTrunkV5Entry,'acTrunkV5NumberOfCChannels':acTrunkV5NumberOfCChannels,'acTrunkV5ProtocolSide':acTrunkV5ProtocolSide,'acTrunkGlobal':acTrunkGlobal,'acTrunkGlobalLifeLineType':acTrunkGlobalLifeLineType,'acTrunkGlobalBChannelAlarms':acTrunkGlobalBChannelAlarms,'acISDNConfig':acISDNConfig,'acMiscISDN':acMiscISDN,'acMiscISDNQ931RelayMode':acMiscISDNQ931RelayMode,'acMiscISDNDuplicateQ931BuffMode':acMiscISDNDuplicateQ931BuffMode,'acDS3Config':acDS3Config,'acDS3ConfigFramingMethod':acDS3ConfigFramingMethod,'acDS3ConfigClockSource':acDS3ConfigClockSource,'acDS3ConfigLineBuiltOut':acDS3ConfigLineBuiltOut,'acCasConfig':acCasConfig,'acCasConfigEnable':acCasConfigEnable,'acCASFile':acCASFile,'acCASFileTable':acCASFileTable,'acCASFileEntry':acCASFileEntry,_Q:acCASFileIndex,'acCASFileName':acCASFileName,'acSonetSDH':acSonetSDH,'acSonetSDHTable':acSonetSDHTable,'acSonetSDHEntry':acSonetSDHEntry,_R:acSonetSDHIndex,'acSonetSDHFbrGrpMappingType':acSonetSDHFbrGrpMappingType,'acSonetSDHFbrGrpKlmNumberingScheme':acSonetSDHFbrGrpKlmNumberingScheme,'acSonetSDHFbrGrpAPSDirectionMode':acSonetSDHFbrGrpAPSDirectionMode,'acSonetSDHFbrGrpAPSRevertMode':acSonetSDHFbrGrpAPSRevertMode,'acSonetSDHFbrGrpAPSWaitToRestoreTime':acSonetSDHFbrGrpAPSWaitToRestoreTime,'acPSTNStatus':acPSTNStatus,'acTrunkStatus':acTrunkStatus,'acTrunkStatusTable':acTrunkStatusTable,'acTrunkStatusEntry':acTrunkStatusEntry,'acTrunkStatusLedStatusColor':acTrunkStatusLedStatusColor,'acTrunkStatusLedStatusState':acTrunkStatusLedStatusState,'acTrunkStatusChannels':acTrunkStatusChannels,'acTrunkStatusV5InterfaceNum':acTrunkStatusV5InterfaceNum,'acTrunkStatusV5LinkID':acTrunkStatusV5LinkID,'acTrunkStatusDChannel':acTrunkStatusDChannel,'acTrunkStatusAlarm':acTrunkStatusAlarm,'acTrunkStatusDchannelActivity':acTrunkStatusDchannelActivity,'acDigitalLegs':acDigitalLegs,'acDigitalLegsTable':acDigitalLegsTable,'acDigitalLegsEntry':acDigitalLegsEntry,_S:acDigitalLegsLegIndex,'acDigitalLegsCallIndex':acDigitalLegsCallIndex,'acDigitalLegsTrunk':acDigitalLegsTrunk,'acDigitalLegsBchannel':acDigitalLegsBchannel,'acDigitalLegsEchoCanceller':acDigitalLegsEchoCanceller,'acDigitalLegsDTMFDetection':acDigitalLegsDTMFDetection,'acDigitalLegsVoiceVolume':acDigitalLegsVoiceVolume,'acDigitalLegsHighPassFilter':acDigitalLegsHighPassFilter,'acDigitalLegsInputGain':acDigitalLegsInputGain,'acDigitalLegsDSPDevice':acDigitalLegsDSPDevice,'acDigitalLegsLegName':acDigitalLegsLegName,'acSDHKLMNumberingScheme':acSDHKLMNumberingScheme,'acSDHKLMNumberingSchemeTable':acSDHKLMNumberingSchemeTable,'acSDHKLMNumberingSchemeEntry':acSDHKLMNumberingSchemeEntry,_T:acSDHKLMNumberingSchemeTrunkIndex,'acSDHKLMNumberingSchemeTUG3OrSTS1':acSDHKLMNumberingSchemeTUG3OrSTS1,'acSDHKLMNumberingSchemeTUG2OrVTG':acSDHKLMNumberingSchemeTUG2OrVTG,'acSDHKLMNumberingSchemeTU12OrVT15':acSDHKLMNumberingSchemeTU12OrVT15,'acFiberGroupStatus':acFiberGroupStatus,'acFiberGroupStatusActiveLink':acFiberGroupStatusActiveLink,'acNFASGroupStatus':acNFASGroupStatus,'acNFASGroupStatusTable':acNFASGroupStatusTable,'acNFASGroupStatusEntry':acNFASGroupStatusEntry,_U:acNFASGroupStatusIndex,'acNFASGroupStatusGroupStatus':acNFASGroupStatusGroupStatus,'acNFASGroupStatusPrimaryDChannel':acNFASGroupStatusPrimaryDChannel,'acNFASGroupStatusBackupDChannel':acNFASGroupStatusBackupDChannel,'acNFASGroupStatusAction':acNFASGroupStatusAction,'acNFASGroupStatusActionResult':acNFASGroupStatusActionResult,'acNFASGroupStatusPrimaryDChannelActivity':acNFASGroupStatusPrimaryDChannelActivity,'acNFASGroupStatusBackupDChannelActivity':acNFASGroupStatusBackupDChannelActivity})