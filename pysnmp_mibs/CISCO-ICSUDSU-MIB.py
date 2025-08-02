_A3='ciscoICsuDsuMIBSw56kGroup'
_A2='ciscoICsuDsuMIBT1Group'
_A1='ciscoICsuDsuMIBGroup'
_A0='ciscoICsuDsuEnableSw56kLoopStatusNotification'
_z='ciscoICsuDsuSw56kLoopRateSearches'
_y='ciscoICsuDsuSw56kLostFrameSyncs'
_x='ciscoICsuDsuSw56kLostReceiveSignals'
_w='ciscoICsuDsuSw56kLostSealingCurrents'
_v='ciscoICsuDsuSw56kReceivedOosOofs'
_u='ciscoICsuDsuSw56kDialingStatus'
_t='ciscoICsuDsuSw56kRemoteLoopbackEnabled'
_s='ciscoICsuDsuSw56kScramblerEnabled'
_r='ciscoICsuDsuSw56kLoopRate'
_q='ciscoICsuDsuSw56kClockSource'
_p='ciscoICsuDsuSw56kNetworkType'
_o='ciscoICsuDsuEnableT1LoopStatusNotification'
_n='ciscoICsuDsuT1AlarmIndicationSignals'
_m='ciscoICsuDsuT1RemoteAlarmIndications'
_l='ciscoICsuDsuT1LossOfFrames'
_k='ciscoICsuDsuT1LossOfSignals'
_j='ciscoICsuDsuT1PayloadRemoteLoopcode'
_i='ciscoICsuDsuT1FullBandwidthRemoteLoopcode'
_h='ciscoICsuDsuT1SupportRemoteAlarmIndication'
_g='ciscoICsuDsuT1DteLineCode'
_f='ciscoICsuDsuT1LineBuildOut'
_e='ciscoICsuDsuEndTimeOfLastLoopback'
_d='ciscoICsuDsuLoopbackCode'
_c='ciscoICsuDsuUserDefinedPattern'
_b='ciscoICsuDsuLoopbackPattern'
_a='ciscoICsuDsuLoopbackPoint'
_Z='ciscoICsuDsuLoopbackDuration'
_Y='ciscoICsuDsuLoopbackNumErrors'
_X='ciscoICsuDsuLoopbackStatus'
_W='ciscoICsuDsuTimeOfLastReset'
_V='ciscoICsuDsuNumResets'
_U='ciscoICsuDsuTimeOfLastSelfTest'
_T='ciscoICsuDsuLastSelfTestResult'
_S='ciscoICsuDsuProtocolRevision'
_R='ciscoICsuDsuSwRevision'
_Q='ciscoICsuDsuHwRevision'
_P='ciscoICsuDsuType'
_O='ciscoICsuDsuT1ConfigEntry'
_N='read-write'
_M='disabled'
_L='ciscoICsuDsuSw56kLoopStatus'
_K='ciscoICsuDsuT1LoopStatus'
_J='alternate'
_I='standard'
_H='TruthValue'
_G='DisplayString'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='CISCO-ICSUDSU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
dsx1ConfigEntry,=mibBuilder.importSymbols('RFC1406-MIB','dsx1ConfigEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TimeStamp',_H)
ciscoICsuDsuMIB=ModuleIdentity((1,3,6,1,4,1,9,9,44))
_CiscoICsuDsuObjects_ObjectIdentity=ObjectIdentity
ciscoICsuDsuObjects=_CiscoICsuDsuObjects_ObjectIdentity((1,3,6,1,4,1,9,9,44,1))
_CiscoICsuDsuGeneral_ObjectIdentity=ObjectIdentity
ciscoICsuDsuGeneral=_CiscoICsuDsuGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,44,1,1))
_CiscoICsuDsuStaticConfigTable_Object=MibTable
ciscoICsuDsuStaticConfigTable=_CiscoICsuDsuStaticConfigTable_Object((1,3,6,1,4,1,9,9,44,1,1,1))
if mibBuilder.loadTexts:ciscoICsuDsuStaticConfigTable.setStatus(_A)
_CiscoICsuDsuStaticConfigEntry_Object=MibTableRow
ciscoICsuDsuStaticConfigEntry=_CiscoICsuDsuStaticConfigEntry_Object((1,3,6,1,4,1,9,9,44,1,1,1,1))
ciscoICsuDsuStaticConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ciscoICsuDsuStaticConfigEntry.setStatus(_A)
class _CiscoICsuDsuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fractionalT1',1),('twoWireSwitched56k',2),('fourWireSwitched56k',3),('unknown',4)))
_CiscoICsuDsuType_Type.__name__=_D
_CiscoICsuDsuType_Object=MibTableColumn
ciscoICsuDsuType=_CiscoICsuDsuType_Object((1,3,6,1,4,1,9,9,44,1,1,1,1,1),_CiscoICsuDsuType_Type())
ciscoICsuDsuType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuType.setStatus(_A)
class _CiscoICsuDsuHwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CiscoICsuDsuHwRevision_Type.__name__=_G
_CiscoICsuDsuHwRevision_Object=MibTableColumn
ciscoICsuDsuHwRevision=_CiscoICsuDsuHwRevision_Object((1,3,6,1,4,1,9,9,44,1,1,1,1,2),_CiscoICsuDsuHwRevision_Type())
ciscoICsuDsuHwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuHwRevision.setStatus(_A)
class _CiscoICsuDsuSwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CiscoICsuDsuSwRevision_Type.__name__=_G
_CiscoICsuDsuSwRevision_Object=MibTableColumn
ciscoICsuDsuSwRevision=_CiscoICsuDsuSwRevision_Object((1,3,6,1,4,1,9,9,44,1,1,1,1,3),_CiscoICsuDsuSwRevision_Type())
ciscoICsuDsuSwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSwRevision.setStatus(_A)
class _CiscoICsuDsuProtocolRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CiscoICsuDsuProtocolRevision_Type.__name__=_G
_CiscoICsuDsuProtocolRevision_Object=MibTableColumn
ciscoICsuDsuProtocolRevision=_CiscoICsuDsuProtocolRevision_Object((1,3,6,1,4,1,9,9,44,1,1,1,1,4),_CiscoICsuDsuProtocolRevision_Type())
ciscoICsuDsuProtocolRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuProtocolRevision.setStatus(_A)
_CiscoICsuDsuTestReportTable_Object=MibTable
ciscoICsuDsuTestReportTable=_CiscoICsuDsuTestReportTable_Object((1,3,6,1,4,1,9,9,44,1,1,2))
if mibBuilder.loadTexts:ciscoICsuDsuTestReportTable.setStatus(_A)
_CiscoICsuDsuTestReportEntry_Object=MibTableRow
ciscoICsuDsuTestReportEntry=_CiscoICsuDsuTestReportEntry_Object((1,3,6,1,4,1,9,9,44,1,1,2,1))
ciscoICsuDsuTestReportEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ciscoICsuDsuTestReportEntry.setStatus(_A)
_CiscoICsuDsuLastSelfTestResult_Type=Integer32
_CiscoICsuDsuLastSelfTestResult_Object=MibTableColumn
ciscoICsuDsuLastSelfTestResult=_CiscoICsuDsuLastSelfTestResult_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,1),_CiscoICsuDsuLastSelfTestResult_Type())
ciscoICsuDsuLastSelfTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuLastSelfTestResult.setStatus(_A)
_CiscoICsuDsuTimeOfLastSelfTest_Type=TimeStamp
_CiscoICsuDsuTimeOfLastSelfTest_Object=MibTableColumn
ciscoICsuDsuTimeOfLastSelfTest=_CiscoICsuDsuTimeOfLastSelfTest_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,2),_CiscoICsuDsuTimeOfLastSelfTest_Type())
ciscoICsuDsuTimeOfLastSelfTest.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuTimeOfLastSelfTest.setStatus(_A)
_CiscoICsuDsuNumResets_Type=Counter32
_CiscoICsuDsuNumResets_Object=MibTableColumn
ciscoICsuDsuNumResets=_CiscoICsuDsuNumResets_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,3),_CiscoICsuDsuNumResets_Type())
ciscoICsuDsuNumResets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuNumResets.setStatus(_A)
_CiscoICsuDsuTimeOfLastReset_Type=TimeStamp
_CiscoICsuDsuTimeOfLastReset_Object=MibTableColumn
ciscoICsuDsuTimeOfLastReset=_CiscoICsuDsuTimeOfLastReset_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,4),_CiscoICsuDsuTimeOfLastReset_Type())
ciscoICsuDsuTimeOfLastReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuTimeOfLastReset.setStatus(_A)
class _CiscoICsuDsuLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('completed',1),('inProgress',2),('neverPerformed',3),('failed',4),('noSyncWithTestPattern',5)))
_CiscoICsuDsuLoopbackStatus_Type.__name__=_D
_CiscoICsuDsuLoopbackStatus_Object=MibTableColumn
ciscoICsuDsuLoopbackStatus=_CiscoICsuDsuLoopbackStatus_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,5),_CiscoICsuDsuLoopbackStatus_Type())
ciscoICsuDsuLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuLoopbackStatus.setStatus(_A)
_CiscoICsuDsuLoopbackNumErrors_Type=Integer32
_CiscoICsuDsuLoopbackNumErrors_Object=MibTableColumn
ciscoICsuDsuLoopbackNumErrors=_CiscoICsuDsuLoopbackNumErrors_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,6),_CiscoICsuDsuLoopbackNumErrors_Type())
ciscoICsuDsuLoopbackNumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuLoopbackNumErrors.setStatus(_A)
_CiscoICsuDsuLoopbackDuration_Type=TimeTicks
_CiscoICsuDsuLoopbackDuration_Object=MibTableColumn
ciscoICsuDsuLoopbackDuration=_CiscoICsuDsuLoopbackDuration_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,7),_CiscoICsuDsuLoopbackDuration_Type())
ciscoICsuDsuLoopbackDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuLoopbackDuration.setStatus(_A)
class _CiscoICsuDsuLoopbackPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('dtePayload',1),('dteFull',2),('lineFull',3),('linePayload',4),('remoteSmartJack',5),('remoteFull',6),('remotePayload',7)))
_CiscoICsuDsuLoopbackPoint_Type.__name__=_D
_CiscoICsuDsuLoopbackPoint_Object=MibTableColumn
ciscoICsuDsuLoopbackPoint=_CiscoICsuDsuLoopbackPoint_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,8),_CiscoICsuDsuLoopbackPoint_Type())
ciscoICsuDsuLoopbackPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuLoopbackPoint.setStatus(_A)
class _CiscoICsuDsuLoopbackPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('noPattern',1),('patternQRW',2),('pattern0In1',3),('pattern1In1',4),('pattern1In2',5),('pattern1In3',6),('pattern1In5',7),('pattern1In8',8),('pattern3In24',9),('patternUser',10),('pattern2047',11),('pattern511',12),('patternStressDDS1',13),('patternStressDDS2',14),('patternStressDDS3',15),('patternStressDDS4',16)))
_CiscoICsuDsuLoopbackPattern_Type.__name__=_D
_CiscoICsuDsuLoopbackPattern_Object=MibTableColumn
ciscoICsuDsuLoopbackPattern=_CiscoICsuDsuLoopbackPattern_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,9),_CiscoICsuDsuLoopbackPattern_Type())
ciscoICsuDsuLoopbackPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuLoopbackPattern.setStatus(_A)
class _CiscoICsuDsuUserDefinedPattern_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_CiscoICsuDsuUserDefinedPattern_Type.__name__=_G
_CiscoICsuDsuUserDefinedPattern_Object=MibTableColumn
ciscoICsuDsuUserDefinedPattern=_CiscoICsuDsuUserDefinedPattern_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,10),_CiscoICsuDsuUserDefinedPattern_Type())
ciscoICsuDsuUserDefinedPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuUserDefinedPattern.setStatus(_A)
class _CiscoICsuDsuLoopbackCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('v54',3)))
_CiscoICsuDsuLoopbackCode_Type.__name__=_D
_CiscoICsuDsuLoopbackCode_Object=MibTableColumn
ciscoICsuDsuLoopbackCode=_CiscoICsuDsuLoopbackCode_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,11),_CiscoICsuDsuLoopbackCode_Type())
ciscoICsuDsuLoopbackCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuLoopbackCode.setStatus(_A)
_CiscoICsuDsuEndTimeOfLastLoopback_Type=TimeStamp
_CiscoICsuDsuEndTimeOfLastLoopback_Object=MibTableColumn
ciscoICsuDsuEndTimeOfLastLoopback=_CiscoICsuDsuEndTimeOfLastLoopback_Object((1,3,6,1,4,1,9,9,44,1,1,2,1,12),_CiscoICsuDsuEndTimeOfLastLoopback_Type())
ciscoICsuDsuEndTimeOfLastLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuEndTimeOfLastLoopback.setStatus(_A)
_CiscoICsuDsuT1_ObjectIdentity=ObjectIdentity
ciscoICsuDsuT1=_CiscoICsuDsuT1_ObjectIdentity((1,3,6,1,4,1,9,9,44,1,2))
_CiscoICsuDsuT1ConfigTable_Object=MibTable
ciscoICsuDsuT1ConfigTable=_CiscoICsuDsuT1ConfigTable_Object((1,3,6,1,4,1,9,9,44,1,2,1))
if mibBuilder.loadTexts:ciscoICsuDsuT1ConfigTable.setStatus(_A)
_CiscoICsuDsuT1ConfigEntry_Object=MibTableRow
ciscoICsuDsuT1ConfigEntry=_CiscoICsuDsuT1ConfigEntry_Object((1,3,6,1,4,1,9,9,44,1,2,1,1))
if mibBuilder.loadTexts:ciscoICsuDsuT1ConfigEntry.setStatus(_A)
class _CiscoICsuDsuT1LineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('buildOut0',1),('buildOut7p5',2),('buildOut15',3)))
_CiscoICsuDsuT1LineBuildOut_Type.__name__=_D
_CiscoICsuDsuT1LineBuildOut_Object=MibTableColumn
ciscoICsuDsuT1LineBuildOut=_CiscoICsuDsuT1LineBuildOut_Object((1,3,6,1,4,1,9,9,44,1,2,1,1,1),_CiscoICsuDsuT1LineBuildOut_Type())
ciscoICsuDsuT1LineBuildOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1LineBuildOut.setStatus(_A)
class _CiscoICsuDsuT1DteLineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('inverted',2)))
_CiscoICsuDsuT1DteLineCode_Type.__name__=_D
_CiscoICsuDsuT1DteLineCode_Object=MibTableColumn
ciscoICsuDsuT1DteLineCode=_CiscoICsuDsuT1DteLineCode_Object((1,3,6,1,4,1,9,9,44,1,2,1,1,2),_CiscoICsuDsuT1DteLineCode_Type())
ciscoICsuDsuT1DteLineCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1DteLineCode.setStatus(_A)
_CiscoICsuDsuT1SupportRemoteAlarmIndication_Type=TruthValue
_CiscoICsuDsuT1SupportRemoteAlarmIndication_Object=MibTableColumn
ciscoICsuDsuT1SupportRemoteAlarmIndication=_CiscoICsuDsuT1SupportRemoteAlarmIndication_Object((1,3,6,1,4,1,9,9,44,1,2,1,1,3),_CiscoICsuDsuT1SupportRemoteAlarmIndication_Type())
ciscoICsuDsuT1SupportRemoteAlarmIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1SupportRemoteAlarmIndication.setStatus(_A)
class _CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_M,3)))
_CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Type.__name__=_D
_CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Object=MibTableColumn
ciscoICsuDsuT1FullBandwidthRemoteLoopcode=_CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Object((1,3,6,1,4,1,9,9,44,1,2,1,1,4),_CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Type())
ciscoICsuDsuT1FullBandwidthRemoteLoopcode.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1FullBandwidthRemoteLoopcode.setStatus(_A)
class _CiscoICsuDsuT1PayloadRemoteLoopcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_M,3),('v54',4)))
_CiscoICsuDsuT1PayloadRemoteLoopcode_Type.__name__=_D
_CiscoICsuDsuT1PayloadRemoteLoopcode_Object=MibTableColumn
ciscoICsuDsuT1PayloadRemoteLoopcode=_CiscoICsuDsuT1PayloadRemoteLoopcode_Object((1,3,6,1,4,1,9,9,44,1,2,1,1,5),_CiscoICsuDsuT1PayloadRemoteLoopcode_Type())
ciscoICsuDsuT1PayloadRemoteLoopcode.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1PayloadRemoteLoopcode.setStatus(_A)
_CiscoICsuDsuT1StatusTable_Object=MibTable
ciscoICsuDsuT1StatusTable=_CiscoICsuDsuT1StatusTable_Object((1,3,6,1,4,1,9,9,44,1,2,2))
if mibBuilder.loadTexts:ciscoICsuDsuT1StatusTable.setStatus(_A)
_CiscoICsuDsuT1StatusEntry_Object=MibTableRow
ciscoICsuDsuT1StatusEntry=_CiscoICsuDsuT1StatusEntry_Object((1,3,6,1,4,1,9,9,44,1,2,2,1))
ciscoICsuDsuT1StatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ciscoICsuDsuT1StatusEntry.setStatus(_A)
_CiscoICsuDsuT1LoopStatus_Type=Integer32
_CiscoICsuDsuT1LoopStatus_Object=MibTableColumn
ciscoICsuDsuT1LoopStatus=_CiscoICsuDsuT1LoopStatus_Object((1,3,6,1,4,1,9,9,44,1,2,2,1,1),_CiscoICsuDsuT1LoopStatus_Type())
ciscoICsuDsuT1LoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1LoopStatus.setStatus(_A)
_CiscoICsuDsuT1LossOfSignals_Type=Counter32
_CiscoICsuDsuT1LossOfSignals_Object=MibTableColumn
ciscoICsuDsuT1LossOfSignals=_CiscoICsuDsuT1LossOfSignals_Object((1,3,6,1,4,1,9,9,44,1,2,2,1,2),_CiscoICsuDsuT1LossOfSignals_Type())
ciscoICsuDsuT1LossOfSignals.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1LossOfSignals.setStatus(_A)
_CiscoICsuDsuT1LossOfFrames_Type=Counter32
_CiscoICsuDsuT1LossOfFrames_Object=MibTableColumn
ciscoICsuDsuT1LossOfFrames=_CiscoICsuDsuT1LossOfFrames_Object((1,3,6,1,4,1,9,9,44,1,2,2,1,3),_CiscoICsuDsuT1LossOfFrames_Type())
ciscoICsuDsuT1LossOfFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1LossOfFrames.setStatus(_A)
_CiscoICsuDsuT1RemoteAlarmIndications_Type=Counter32
_CiscoICsuDsuT1RemoteAlarmIndications_Object=MibTableColumn
ciscoICsuDsuT1RemoteAlarmIndications=_CiscoICsuDsuT1RemoteAlarmIndications_Object((1,3,6,1,4,1,9,9,44,1,2,2,1,4),_CiscoICsuDsuT1RemoteAlarmIndications_Type())
ciscoICsuDsuT1RemoteAlarmIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1RemoteAlarmIndications.setStatus(_A)
_CiscoICsuDsuT1AlarmIndicationSignals_Type=Counter32
_CiscoICsuDsuT1AlarmIndicationSignals_Object=MibTableColumn
ciscoICsuDsuT1AlarmIndicationSignals=_CiscoICsuDsuT1AlarmIndicationSignals_Object((1,3,6,1,4,1,9,9,44,1,2,2,1,5),_CiscoICsuDsuT1AlarmIndicationSignals_Type())
ciscoICsuDsuT1AlarmIndicationSignals.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuT1AlarmIndicationSignals.setStatus(_A)
_CiscoICsuDsuSw56k_ObjectIdentity=ObjectIdentity
ciscoICsuDsuSw56k=_CiscoICsuDsuSw56k_ObjectIdentity((1,3,6,1,4,1,9,9,44,1,3))
_CiscoICsuDsuSw56kConfigTable_Object=MibTable
ciscoICsuDsuSw56kConfigTable=_CiscoICsuDsuSw56kConfigTable_Object((1,3,6,1,4,1,9,9,44,1,3,1))
if mibBuilder.loadTexts:ciscoICsuDsuSw56kConfigTable.setStatus(_A)
_CiscoICsuDsuSw56kConfigEntry_Object=MibTableRow
ciscoICsuDsuSw56kConfigEntry=_CiscoICsuDsuSw56kConfigEntry_Object((1,3,6,1,4,1,9,9,44,1,3,1,1))
ciscoICsuDsuSw56kConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ciscoICsuDsuSw56kConfigEntry.setStatus(_A)
class _CiscoICsuDsuSw56kNetworkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dds',1),('att',2),('sprint',3),('otherCarrier',4)))
_CiscoICsuDsuSw56kNetworkType_Type.__name__=_D
_CiscoICsuDsuSw56kNetworkType_Object=MibTableColumn
ciscoICsuDsuSw56kNetworkType=_CiscoICsuDsuSw56kNetworkType_Object((1,3,6,1,4,1,9,9,44,1,3,1,1,1),_CiscoICsuDsuSw56kNetworkType_Type())
ciscoICsuDsuSw56kNetworkType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kNetworkType.setStatus(_A)
class _CiscoICsuDsuSw56kClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('line',2)))
_CiscoICsuDsuSw56kClockSource_Type.__name__=_D
_CiscoICsuDsuSw56kClockSource_Object=MibTableColumn
ciscoICsuDsuSw56kClockSource=_CiscoICsuDsuSw56kClockSource_Object((1,3,6,1,4,1,9,9,44,1,3,1,1,2),_CiscoICsuDsuSw56kClockSource_Type())
ciscoICsuDsuSw56kClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kClockSource.setStatus(_A)
class _CiscoICsuDsuSw56kLoopRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('bps2400',1),('bps4800',2),('bps9600',3),('bps19k',4),('bps38k',5),('bps56k',6),('bps64k',7)))
_CiscoICsuDsuSw56kLoopRate_Type.__name__=_D
_CiscoICsuDsuSw56kLoopRate_Object=MibTableColumn
ciscoICsuDsuSw56kLoopRate=_CiscoICsuDsuSw56kLoopRate_Object((1,3,6,1,4,1,9,9,44,1,3,1,1,3),_CiscoICsuDsuSw56kLoopRate_Type())
ciscoICsuDsuSw56kLoopRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLoopRate.setStatus(_A)
_CiscoICsuDsuSw56kScramblerEnabled_Type=TruthValue
_CiscoICsuDsuSw56kScramblerEnabled_Object=MibTableColumn
ciscoICsuDsuSw56kScramblerEnabled=_CiscoICsuDsuSw56kScramblerEnabled_Object((1,3,6,1,4,1,9,9,44,1,3,1,1,4),_CiscoICsuDsuSw56kScramblerEnabled_Type())
ciscoICsuDsuSw56kScramblerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kScramblerEnabled.setStatus(_A)
_CiscoICsuDsuSw56kRemoteLoopbackEnabled_Type=TruthValue
_CiscoICsuDsuSw56kRemoteLoopbackEnabled_Object=MibTableColumn
ciscoICsuDsuSw56kRemoteLoopbackEnabled=_CiscoICsuDsuSw56kRemoteLoopbackEnabled_Object((1,3,6,1,4,1,9,9,44,1,3,1,1,5),_CiscoICsuDsuSw56kRemoteLoopbackEnabled_Type())
ciscoICsuDsuSw56kRemoteLoopbackEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kRemoteLoopbackEnabled.setStatus(_A)
_CiscoICsuDsuSw56kLineStatusTable_Object=MibTable
ciscoICsuDsuSw56kLineStatusTable=_CiscoICsuDsuSw56kLineStatusTable_Object((1,3,6,1,4,1,9,9,44,1,3,2))
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLineStatusTable.setStatus(_A)
_CiscoICsuDsuSw56kLineStatusEntry_Object=MibTableRow
ciscoICsuDsuSw56kLineStatusEntry=_CiscoICsuDsuSw56kLineStatusEntry_Object((1,3,6,1,4,1,9,9,44,1,3,2,1))
ciscoICsuDsuSw56kLineStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLineStatusEntry.setStatus(_A)
class _CiscoICsuDsuSw56kDialingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('dialing',2),('online',3),('noWinkFromSwitch',4),('numberBusy',5),('noAnswer',6)))
_CiscoICsuDsuSw56kDialingStatus_Type.__name__=_D
_CiscoICsuDsuSw56kDialingStatus_Object=MibTableColumn
ciscoICsuDsuSw56kDialingStatus=_CiscoICsuDsuSw56kDialingStatus_Object((1,3,6,1,4,1,9,9,44,1,3,2,1,1),_CiscoICsuDsuSw56kDialingStatus_Type())
ciscoICsuDsuSw56kDialingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kDialingStatus.setStatus(_A)
_CiscoICsuDsuSw56kLoopStatus_Type=Integer32
_CiscoICsuDsuSw56kLoopStatus_Object=MibTableColumn
ciscoICsuDsuSw56kLoopStatus=_CiscoICsuDsuSw56kLoopStatus_Object((1,3,6,1,4,1,9,9,44,1,3,2,1,2),_CiscoICsuDsuSw56kLoopStatus_Type())
ciscoICsuDsuSw56kLoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLoopStatus.setStatus(_A)
_CiscoICsuDsuSw56kReceivedOosOofs_Type=Counter32
_CiscoICsuDsuSw56kReceivedOosOofs_Object=MibTableColumn
ciscoICsuDsuSw56kReceivedOosOofs=_CiscoICsuDsuSw56kReceivedOosOofs_Object((1,3,6,1,4,1,9,9,44,1,3,2,1,3),_CiscoICsuDsuSw56kReceivedOosOofs_Type())
ciscoICsuDsuSw56kReceivedOosOofs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kReceivedOosOofs.setStatus(_A)
_CiscoICsuDsuSw56kLostSealingCurrents_Type=Counter32
_CiscoICsuDsuSw56kLostSealingCurrents_Object=MibTableColumn
ciscoICsuDsuSw56kLostSealingCurrents=_CiscoICsuDsuSw56kLostSealingCurrents_Object((1,3,6,1,4,1,9,9,44,1,3,2,1,4),_CiscoICsuDsuSw56kLostSealingCurrents_Type())
ciscoICsuDsuSw56kLostSealingCurrents.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLostSealingCurrents.setStatus(_A)
_CiscoICsuDsuSw56kLostReceiveSignals_Type=Counter32
_CiscoICsuDsuSw56kLostReceiveSignals_Object=MibTableColumn
ciscoICsuDsuSw56kLostReceiveSignals=_CiscoICsuDsuSw56kLostReceiveSignals_Object((1,3,6,1,4,1,9,9,44,1,3,2,1,5),_CiscoICsuDsuSw56kLostReceiveSignals_Type())
ciscoICsuDsuSw56kLostReceiveSignals.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLostReceiveSignals.setStatus(_A)
_CiscoICsuDsuSw56kLostFrameSyncs_Type=Counter32
_CiscoICsuDsuSw56kLostFrameSyncs_Object=MibTableColumn
ciscoICsuDsuSw56kLostFrameSyncs=_CiscoICsuDsuSw56kLostFrameSyncs_Object((1,3,6,1,4,1,9,9,44,1,3,2,1,6),_CiscoICsuDsuSw56kLostFrameSyncs_Type())
ciscoICsuDsuSw56kLostFrameSyncs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLostFrameSyncs.setStatus(_A)
_CiscoICsuDsuSw56kLoopRateSearches_Type=Counter32
_CiscoICsuDsuSw56kLoopRateSearches_Object=MibTableColumn
ciscoICsuDsuSw56kLoopRateSearches=_CiscoICsuDsuSw56kLoopRateSearches_Object((1,3,6,1,4,1,9,9,44,1,3,2,1,7),_CiscoICsuDsuSw56kLoopRateSearches_Type())
ciscoICsuDsuSw56kLoopRateSearches.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLoopRateSearches.setStatus(_A)
_CiscoICsuDsuMIBNotificationEnables_ObjectIdentity=ObjectIdentity
ciscoICsuDsuMIBNotificationEnables=_CiscoICsuDsuMIBNotificationEnables_ObjectIdentity((1,3,6,1,4,1,9,9,44,2))
class _CiscoICsuDsuEnableT1LoopStatusNotification_Type(TruthValue):defaultValue=2
_CiscoICsuDsuEnableT1LoopStatusNotification_Type.__name__=_H
_CiscoICsuDsuEnableT1LoopStatusNotification_Object=MibScalar
ciscoICsuDsuEnableT1LoopStatusNotification=_CiscoICsuDsuEnableT1LoopStatusNotification_Object((1,3,6,1,4,1,9,9,44,2,1),_CiscoICsuDsuEnableT1LoopStatusNotification_Type())
ciscoICsuDsuEnableT1LoopStatusNotification.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoICsuDsuEnableT1LoopStatusNotification.setStatus(_A)
class _CiscoICsuDsuEnableSw56kLoopStatusNotification_Type(TruthValue):defaultValue=2
_CiscoICsuDsuEnableSw56kLoopStatusNotification_Type.__name__=_H
_CiscoICsuDsuEnableSw56kLoopStatusNotification_Object=MibScalar
ciscoICsuDsuEnableSw56kLoopStatusNotification=_CiscoICsuDsuEnableSw56kLoopStatusNotification_Object((1,3,6,1,4,1,9,9,44,2,2),_CiscoICsuDsuEnableSw56kLoopStatusNotification_Type())
ciscoICsuDsuEnableSw56kLoopStatusNotification.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoICsuDsuEnableSw56kLoopStatusNotification.setStatus(_A)
_CiscoICsuDsuMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoICsuDsuMIBNotificationPrefix=_CiscoICsuDsuMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,44,3))
_CiscoICsuDsuMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoICsuDsuMIBNotifications=_CiscoICsuDsuMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,44,3,0))
_CiscoICsuDsuMIBConformance_ObjectIdentity=ObjectIdentity
ciscoICsuDsuMIBConformance=_CiscoICsuDsuMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,44,4))
_CiscoICsuDsuMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoICsuDsuMIBCompliances=_CiscoICsuDsuMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,44,4,1))
_CiscoICsuDsuMIBGroups_ObjectIdentity=ObjectIdentity
ciscoICsuDsuMIBGroups=_CiscoICsuDsuMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,44,4,2))
dsx1ConfigEntry.registerAugmentions((_B,_O))
ciscoICsuDsuT1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
ciscoICsuDsuMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,44,4,2,1))
ciscoICsuDsuMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ciscoICsuDsuMIBGroup.setStatus(_A)
ciscoICsuDsuMIBT1Group=ObjectGroup((1,3,6,1,4,1,9,9,44,4,2,2))
ciscoICsuDsuMIBT1Group.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_K),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoICsuDsuMIBT1Group.setStatus(_A)
ciscoICsuDsuMIBSw56kGroup=ObjectGroup((1,3,6,1,4,1,9,9,44,4,2,3))
ciscoICsuDsuMIBSw56kGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_L),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ciscoICsuDsuMIBSw56kGroup.setStatus(_A)
ciscoICsuDsuT1LoopStatusNotification=NotificationType((1,3,6,1,4,1,9,9,44,3,0,1))
ciscoICsuDsuT1LoopStatusNotification.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoICsuDsuT1LoopStatusNotification.setStatus(_A)
ciscoICsuDsuSw56kLoopStatusNotification=NotificationType((1,3,6,1,4,1,9,9,44,3,0,2))
ciscoICsuDsuSw56kLoopStatusNotification.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoICsuDsuSw56kLoopStatusNotification.setStatus(_A)
ciscoICsuDsuMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,44,4,1,1))
ciscoICsuDsuMIBCompliance.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:ciscoICsuDsuMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoICsuDsuMIB':ciscoICsuDsuMIB,'ciscoICsuDsuObjects':ciscoICsuDsuObjects,'ciscoICsuDsuGeneral':ciscoICsuDsuGeneral,'ciscoICsuDsuStaticConfigTable':ciscoICsuDsuStaticConfigTable,'ciscoICsuDsuStaticConfigEntry':ciscoICsuDsuStaticConfigEntry,_P:ciscoICsuDsuType,_Q:ciscoICsuDsuHwRevision,_R:ciscoICsuDsuSwRevision,_S:ciscoICsuDsuProtocolRevision,'ciscoICsuDsuTestReportTable':ciscoICsuDsuTestReportTable,'ciscoICsuDsuTestReportEntry':ciscoICsuDsuTestReportEntry,_T:ciscoICsuDsuLastSelfTestResult,_U:ciscoICsuDsuTimeOfLastSelfTest,_V:ciscoICsuDsuNumResets,_W:ciscoICsuDsuTimeOfLastReset,_X:ciscoICsuDsuLoopbackStatus,_Y:ciscoICsuDsuLoopbackNumErrors,_Z:ciscoICsuDsuLoopbackDuration,_a:ciscoICsuDsuLoopbackPoint,_b:ciscoICsuDsuLoopbackPattern,_c:ciscoICsuDsuUserDefinedPattern,_d:ciscoICsuDsuLoopbackCode,_e:ciscoICsuDsuEndTimeOfLastLoopback,'ciscoICsuDsuT1':ciscoICsuDsuT1,'ciscoICsuDsuT1ConfigTable':ciscoICsuDsuT1ConfigTable,_O:ciscoICsuDsuT1ConfigEntry,_f:ciscoICsuDsuT1LineBuildOut,_g:ciscoICsuDsuT1DteLineCode,_h:ciscoICsuDsuT1SupportRemoteAlarmIndication,_i:ciscoICsuDsuT1FullBandwidthRemoteLoopcode,_j:ciscoICsuDsuT1PayloadRemoteLoopcode,'ciscoICsuDsuT1StatusTable':ciscoICsuDsuT1StatusTable,'ciscoICsuDsuT1StatusEntry':ciscoICsuDsuT1StatusEntry,_K:ciscoICsuDsuT1LoopStatus,_k:ciscoICsuDsuT1LossOfSignals,_l:ciscoICsuDsuT1LossOfFrames,_m:ciscoICsuDsuT1RemoteAlarmIndications,_n:ciscoICsuDsuT1AlarmIndicationSignals,'ciscoICsuDsuSw56k':ciscoICsuDsuSw56k,'ciscoICsuDsuSw56kConfigTable':ciscoICsuDsuSw56kConfigTable,'ciscoICsuDsuSw56kConfigEntry':ciscoICsuDsuSw56kConfigEntry,_p:ciscoICsuDsuSw56kNetworkType,_q:ciscoICsuDsuSw56kClockSource,_r:ciscoICsuDsuSw56kLoopRate,_s:ciscoICsuDsuSw56kScramblerEnabled,_t:ciscoICsuDsuSw56kRemoteLoopbackEnabled,'ciscoICsuDsuSw56kLineStatusTable':ciscoICsuDsuSw56kLineStatusTable,'ciscoICsuDsuSw56kLineStatusEntry':ciscoICsuDsuSw56kLineStatusEntry,_u:ciscoICsuDsuSw56kDialingStatus,_L:ciscoICsuDsuSw56kLoopStatus,_v:ciscoICsuDsuSw56kReceivedOosOofs,_w:ciscoICsuDsuSw56kLostSealingCurrents,_x:ciscoICsuDsuSw56kLostReceiveSignals,_y:ciscoICsuDsuSw56kLostFrameSyncs,_z:ciscoICsuDsuSw56kLoopRateSearches,'ciscoICsuDsuMIBNotificationEnables':ciscoICsuDsuMIBNotificationEnables,_o:ciscoICsuDsuEnableT1LoopStatusNotification,_A0:ciscoICsuDsuEnableSw56kLoopStatusNotification,'ciscoICsuDsuMIBNotificationPrefix':ciscoICsuDsuMIBNotificationPrefix,'ciscoICsuDsuMIBNotifications':ciscoICsuDsuMIBNotifications,'ciscoICsuDsuT1LoopStatusNotification':ciscoICsuDsuT1LoopStatusNotification,'ciscoICsuDsuSw56kLoopStatusNotification':ciscoICsuDsuSw56kLoopStatusNotification,'ciscoICsuDsuMIBConformance':ciscoICsuDsuMIBConformance,'ciscoICsuDsuMIBCompliances':ciscoICsuDsuMIBCompliances,'ciscoICsuDsuMIBCompliance':ciscoICsuDsuMIBCompliance,'ciscoICsuDsuMIBGroups':ciscoICsuDsuMIBGroups,_A1:ciscoICsuDsuMIBGroup,_A2:ciscoICsuDsuMIBT1Group,_A3:ciscoICsuDsuMIBSw56kGroup})