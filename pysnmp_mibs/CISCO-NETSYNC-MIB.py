_Af='cnsMIBNotifEnablesGroup'
_Ae='ciscoNetsyncMIBNotificationGroup'
_Ad='cnsT4ClkSrcObjectGroup'
_Ac='cnsExtOutputObjectGroup'
_Ab='cnsInputSourceObjectGroup'
_Aa='cnsSelectedInputSourceObjectGroup'
_AZ='cnsClkSelGlobalObjectGroup'
_AY='ciscoNetsyncInputAlarmStatus'
_AX='ciscoNetsyncInputSignalFailureStatus'
_AW='ciscoNetsyncSelectedT4Clock'
_AV='ciscoNetsyncSelectedT0Clock'
_AU='cnsMIBEnableStatusNotification'
_AT='cnsT4ClkSrcMSW'
_AS='cnsT4ClkSrcFSW'
_AR='cnsT4ClkSrcAlarmInfo'
_AQ='cnsT4ClkSrcAlarm'
_AP='cnsT4ClkSrcSignalFailure'
_AO='cnsT4ClkSrcLockout'
_AN='cnsT4ClkSrcWtrTime'
_AM='cnsT4ClkSrcHoldoffTime'
_AL='cnsT4ClkSrcQualityLevelRx'
_AK='cnsT4ClkSrcQualityLevelTx'
_AJ='cnsT4ClkSrcQualityLevelRxCfg'
_AI='cnsT4ClkSrcQualityLevelTxCfg'
_AH='cnsT4ClkSrcSSMCap'
_AG='cnsT4ClkSrcESMCCap'
_AF='cnsExtOutSquelch'
_AE='cnsExtOutMSW'
_AD='cnsExtOutFSW'
_AC='cnsExtOutPriority'
_AB='cnsExtOutQualityLevel'
_AA='cnsExtOutIntfType'
_A9='cnsExtOutSelNetsyncIndex'
_A8='cnsInpSrcMSW'
_A7='cnsInpSrcFSW'
_A6='cnsInpSrcAlarm'
_A5='cnsInpSrcSignalFailure'
_A4='cnsInpSrcLockout'
_A3='cnsInpSrcWtrTime'
_A2='cnsInpSrcHoldoffTime'
_A1='cnsInpSrcQualityLevel'
_A0='cnsInpSrcQualityLevelRx'
_z='cnsInpSrcQualityLevelTx'
_y='cnsInpSrcQualityLevelRxCfg'
_x='cnsInpSrcQualityLevelTxCfg'
_w='cnsInpSrcSSMCap'
_v='cnsInpSrcESMCCap'
_u='cnsInpSrcPriority'
_t='cnsSelInpSrcMSW'
_s='cnsSelInpSrcFSW'
_r='cnsSelInpSrcTimestamp'
_q='cnsClkSelGlobCurrHoldoverSeconds'
_p='cnsClkSelGlobLastHoldoverSeconds'
_o='cnsClkSelGlobNofSources'
_n='cnsClkSelGlobWtrTime'
_m='cnsClkSelGlobHoldoffTime'
_l='cnsClkSelGlobNetworkOption'
_k='cnsClkSelGlobEECOption'
_j='cnsClkSelGlobESMCMode'
_i='cnsClkSelGlobRevertiveMode'
_h='cnsClkSelGlobNetsyncEnable'
_g='cnsClkSelGlobClockMode'
_f='cnsClkSelGlobProcessMode'
_e='accessible-for-notify'
_d='cnsT4ClkSrcNetsyncIndex'
_c='cnsInpSrcNetsyncIndex'
_b='cnsSelInpSrcNetsyncIndex'
_a='CiscoNetsyncNetworkOption'
_Z='CiscoNetsyncEECOption'
_Y='cnsClkSelGloProcIndex'
_X='cnsT4ClkSrcQualityLevel'
_W='cnsT4ClkSrcPriority'
_V='cnsT4ClkSrcIntfType'
_U='cnsT4ClkSrcName'
_T='cnsExtOutName'
_S='cnsInpSrcFailClear'
_R='cnsInpSrcAlarmClear'
_Q='cnsInpSrcAlarmInfo'
_P='cnsSelInpSrcPriority'
_O='cnsSelInpSrcIntfType'
_N='cnsSelInpSrcQualityLevel'
_M='cnsSelInpSrcName'
_L='cnsExtOutListIndex'
_K='milliseconds'
_J='cnsInpSrcIntfType'
_I='cnsInpSrcName'
_H='seconds'
_G='not-accessible'
_F='TruthValue'
_E='SnmpAdminString'
_D='Unsigned32'
_C='read-only'
_B='CISCO-NETSYNC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_F)
ciscoNetsyncMIB=ModuleIdentity((1,3,6,1,4,1,9,9,761))
if mibBuilder.loadTexts:ciscoNetsyncMIB.setRevisions(('2010-10-15 00:00',))
class CiscoNetsyncIfType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('netsyncIfTypeUnknown',1),('netsyncIfTypeInternal',2),('netsyncIfTypeEthernet',3),('netsyncIfTypeSonet',4),('netsyncIfTypeTop',5),('netsyncIfTypeExt',6),('netsyncIfTypeController',7),('netsyncIfTypeGps',8),('netsyncIfTypeAtm',9)))
class CiscoNetsyncNetworkOption(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('netsyncNetworkOptionUnknown',1),('netsyncNetworkOption1',2),('netsyncNetworkOption2Gen1',3),('netsyncNetworkOption2Gen2',4),('netsyncNetworkOption3',5),('netsyncNetworkOptionInvalid',6)))
class CiscoNetsyncEECOption(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('netsyncEECOptionUnknown',1),('netsyncEECOption1',2),('netsyncEECOption2',3),('netsyncEECOptionInvalid',4)))
class CiscoNetsyncQLMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('netsyncQLModeUnknown',1),('netsyncQLModeQlDisabled',2),('netsyncQLModeQlEnabled',3)))
class CiscoNetsyncClockMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('netsyncClockModeUnknown',1),('netsyncClockModeFreerun',2),('netsyncClockModeHoldover',3),('netsyncClockModeLocked',4)))
class CiscoNetsyncQualityLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)));namedValues=NamedValues(*(('netsyncQualityLevelNULL',1),('netsyncQualityLevelDNU',2),('netsyncQualityLevelDUS',3),('netsyncQualityLevelFAILED',4),('netsyncQualityLevelINV0',5),('netsyncQualityLevelINV1',6),('netsyncQualityLevelINV2',7),('netsyncQualityLevelINV3',8),('netsyncQualityLevelINV4',9),('netsyncQualityLevelINV5',10),('netsyncQualityLevelINV6',11),('netsyncQualityLevelINV7',12),('netsyncQualityLevelINV8',13),('netsyncQualityLevelINV9',14),('netsyncQualityLevelINV10',15),('netsyncQualityLevelINV11',16),('netsyncQualityLevelINV12',17),('netsyncQualityLevelINV13',18),('netsyncQualityLevelINV14',19),('netsyncQualityLevelINV15',20),('netsyncQualityLevelNSUPP',21),('netsyncQualityLevelPRC',22),('netsyncQualityLevelPROV',23),('netsyncQualityLevelPRS',24),('netsyncQualityLevelSEC',25),('netsyncQualityLevelSMC',26),('netsyncQualityLevelSSUA',27),('netsyncQualityLevelSSUB',28),('netsyncQualityLevelST2',29),('netsyncQualityLevelST3',30),('netsyncQualityLevelST3E',31),('netsyncQualityLevelST4',32),('netsyncQualityLevelSTU',33),('netsyncQualityLevelTNC',34),('netsyncQualityLevelUNC',35),('netsyncQualityLevelUNK',36)))
class CiscoNetsyncSSMCap(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('netsyncSSMCapNone',1),('netsyncSSMCapTxRx',2),('netsyncSSMCapTx',3),('netsyncSSMCapRx',4),('netsyncSSMCapInvalid',5)))
class CiscoNetsyncESMCCap(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('netsyncESMCCapNone',1),('netsyncESMCCapTxRx',2),('netsyncESMCCapTx',3),('netsyncESMCCapRx',4),('netsyncESMCCapInvalid',5)))
class CiscoNetsyncAlarmInfo(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('netsyncSrcAlarmReasonAIS',0),('netsyncSrcAlarmReasonOOR',1),('netsyncSrcAlarmReasonOIR',2),('netsyncSrcAlarmReasonInternal',3)))
_CiscoNetsyncMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNetsyncMIBNotifs=_CiscoNetsyncMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,761,0))
_CiscoNetsyncMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNetsyncMIBObjects=_CiscoNetsyncMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,761,1))
_CiscoNetsyncMIBTables_ObjectIdentity=ObjectIdentity
ciscoNetsyncMIBTables=_CiscoNetsyncMIBTables_ObjectIdentity((1,3,6,1,4,1,9,9,761,1,1))
_CnsClkSelGlobalTable_Object=MibTable
cnsClkSelGlobalTable=_CnsClkSelGlobalTable_Object((1,3,6,1,4,1,9,9,761,1,1,1))
if mibBuilder.loadTexts:cnsClkSelGlobalTable.setStatus(_A)
_CnsClkSelGlobalEntry_Object=MibTableRow
cnsClkSelGlobalEntry=_CnsClkSelGlobalEntry_Object((1,3,6,1,4,1,9,9,761,1,1,1,1))
cnsClkSelGlobalEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:cnsClkSelGlobalEntry.setStatus(_A)
class _CnsClkSelGloProcIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CnsClkSelGloProcIndex_Type.__name__=_D
_CnsClkSelGloProcIndex_Object=MibTableColumn
cnsClkSelGloProcIndex=_CnsClkSelGloProcIndex_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,1),_CnsClkSelGloProcIndex_Type())
cnsClkSelGloProcIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cnsClkSelGloProcIndex.setStatus(_A)
_CnsClkSelGlobProcessMode_Type=CiscoNetsyncQLMode
_CnsClkSelGlobProcessMode_Object=MibTableColumn
cnsClkSelGlobProcessMode=_CnsClkSelGlobProcessMode_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,2),_CnsClkSelGlobProcessMode_Type())
cnsClkSelGlobProcessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobProcessMode.setStatus(_A)
_CnsClkSelGlobClockMode_Type=CiscoNetsyncClockMode
_CnsClkSelGlobClockMode_Object=MibTableColumn
cnsClkSelGlobClockMode=_CnsClkSelGlobClockMode_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,3),_CnsClkSelGlobClockMode_Type())
cnsClkSelGlobClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobClockMode.setStatus(_A)
class _CnsClkSelGlobNetsyncEnable_Type(TruthValue):defaultValue=2
_CnsClkSelGlobNetsyncEnable_Type.__name__=_F
_CnsClkSelGlobNetsyncEnable_Object=MibTableColumn
cnsClkSelGlobNetsyncEnable=_CnsClkSelGlobNetsyncEnable_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,4),_CnsClkSelGlobNetsyncEnable_Type())
cnsClkSelGlobNetsyncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobNetsyncEnable.setStatus(_A)
class _CnsClkSelGlobRevertiveMode_Type(TruthValue):defaultValue=2
_CnsClkSelGlobRevertiveMode_Type.__name__=_F
_CnsClkSelGlobRevertiveMode_Object=MibTableColumn
cnsClkSelGlobRevertiveMode=_CnsClkSelGlobRevertiveMode_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,5),_CnsClkSelGlobRevertiveMode_Type())
cnsClkSelGlobRevertiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobRevertiveMode.setStatus(_A)
class _CnsClkSelGlobESMCMode_Type(TruthValue):defaultValue=2
_CnsClkSelGlobESMCMode_Type.__name__=_F
_CnsClkSelGlobESMCMode_Object=MibTableColumn
cnsClkSelGlobESMCMode=_CnsClkSelGlobESMCMode_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,6),_CnsClkSelGlobESMCMode_Type())
cnsClkSelGlobESMCMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobESMCMode.setStatus(_A)
class _CnsClkSelGlobEECOption_Type(CiscoNetsyncEECOption):defaultValue=1
_CnsClkSelGlobEECOption_Type.__name__=_Z
_CnsClkSelGlobEECOption_Object=MibTableColumn
cnsClkSelGlobEECOption=_CnsClkSelGlobEECOption_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,7),_CnsClkSelGlobEECOption_Type())
cnsClkSelGlobEECOption.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobEECOption.setStatus(_A)
class _CnsClkSelGlobNetworkOption_Type(CiscoNetsyncNetworkOption):defaultValue=1
_CnsClkSelGlobNetworkOption_Type.__name__=_a
_CnsClkSelGlobNetworkOption_Object=MibTableColumn
cnsClkSelGlobNetworkOption=_CnsClkSelGlobNetworkOption_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,8),_CnsClkSelGlobNetworkOption_Type())
cnsClkSelGlobNetworkOption.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobNetworkOption.setStatus(_A)
class _CnsClkSelGlobHoldoffTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CnsClkSelGlobHoldoffTime_Type.__name__=_D
_CnsClkSelGlobHoldoffTime_Object=MibTableColumn
cnsClkSelGlobHoldoffTime=_CnsClkSelGlobHoldoffTime_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,9),_CnsClkSelGlobHoldoffTime_Type())
cnsClkSelGlobHoldoffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobHoldoffTime.setStatus(_A)
if mibBuilder.loadTexts:cnsClkSelGlobHoldoffTime.setUnits(_K)
class _CnsClkSelGlobWtrTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CnsClkSelGlobWtrTime_Type.__name__=_D
_CnsClkSelGlobWtrTime_Object=MibTableColumn
cnsClkSelGlobWtrTime=_CnsClkSelGlobWtrTime_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,10),_CnsClkSelGlobWtrTime_Type())
cnsClkSelGlobWtrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobWtrTime.setStatus(_A)
if mibBuilder.loadTexts:cnsClkSelGlobWtrTime.setUnits(_H)
class _CnsClkSelGlobNofSources_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CnsClkSelGlobNofSources_Type.__name__=_D
_CnsClkSelGlobNofSources_Object=MibTableColumn
cnsClkSelGlobNofSources=_CnsClkSelGlobNofSources_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,11),_CnsClkSelGlobNofSources_Type())
cnsClkSelGlobNofSources.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobNofSources.setStatus(_A)
if mibBuilder.loadTexts:cnsClkSelGlobNofSources.setUnits('clock sources')
_CnsClkSelGlobLastHoldoverSeconds_Type=Gauge32
_CnsClkSelGlobLastHoldoverSeconds_Object=MibTableColumn
cnsClkSelGlobLastHoldoverSeconds=_CnsClkSelGlobLastHoldoverSeconds_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,12),_CnsClkSelGlobLastHoldoverSeconds_Type())
cnsClkSelGlobLastHoldoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobLastHoldoverSeconds.setStatus(_A)
if mibBuilder.loadTexts:cnsClkSelGlobLastHoldoverSeconds.setUnits(_H)
_CnsClkSelGlobCurrHoldoverSeconds_Type=Gauge32
_CnsClkSelGlobCurrHoldoverSeconds_Object=MibTableColumn
cnsClkSelGlobCurrHoldoverSeconds=_CnsClkSelGlobCurrHoldoverSeconds_Object((1,3,6,1,4,1,9,9,761,1,1,1,1,13),_CnsClkSelGlobCurrHoldoverSeconds_Type())
cnsClkSelGlobCurrHoldoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsClkSelGlobCurrHoldoverSeconds.setStatus(_A)
if mibBuilder.loadTexts:cnsClkSelGlobCurrHoldoverSeconds.setUnits(_H)
_CnsSelectedInputSourceTable_Object=MibTable
cnsSelectedInputSourceTable=_CnsSelectedInputSourceTable_Object((1,3,6,1,4,1,9,9,761,1,1,2))
if mibBuilder.loadTexts:cnsSelectedInputSourceTable.setStatus(_A)
_CnsSelectedInputSourceEntry_Object=MibTableRow
cnsSelectedInputSourceEntry=_CnsSelectedInputSourceEntry_Object((1,3,6,1,4,1,9,9,761,1,1,2,1))
cnsSelectedInputSourceEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:cnsSelectedInputSourceEntry.setStatus(_A)
class _CnsSelInpSrcNetsyncIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnsSelInpSrcNetsyncIndex_Type.__name__=_D
_CnsSelInpSrcNetsyncIndex_Object=MibTableColumn
cnsSelInpSrcNetsyncIndex=_CnsSelInpSrcNetsyncIndex_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,1),_CnsSelInpSrcNetsyncIndex_Type())
cnsSelInpSrcNetsyncIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cnsSelInpSrcNetsyncIndex.setStatus(_A)
class _CnsSelInpSrcName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CnsSelInpSrcName_Type.__name__=_E
_CnsSelInpSrcName_Object=MibTableColumn
cnsSelInpSrcName=_CnsSelInpSrcName_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,2),_CnsSelInpSrcName_Type())
cnsSelInpSrcName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsSelInpSrcName.setStatus(_A)
_CnsSelInpSrcIntfType_Type=CiscoNetsyncIfType
_CnsSelInpSrcIntfType_Object=MibTableColumn
cnsSelInpSrcIntfType=_CnsSelInpSrcIntfType_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,3),_CnsSelInpSrcIntfType_Type())
cnsSelInpSrcIntfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsSelInpSrcIntfType.setStatus(_A)
_CnsSelInpSrcQualityLevel_Type=CiscoNetsyncQualityLevel
_CnsSelInpSrcQualityLevel_Object=MibTableColumn
cnsSelInpSrcQualityLevel=_CnsSelInpSrcQualityLevel_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,4),_CnsSelInpSrcQualityLevel_Type())
cnsSelInpSrcQualityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsSelInpSrcQualityLevel.setStatus(_A)
class _CnsSelInpSrcPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnsSelInpSrcPriority_Type.__name__=_D
_CnsSelInpSrcPriority_Object=MibTableColumn
cnsSelInpSrcPriority=_CnsSelInpSrcPriority_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,5),_CnsSelInpSrcPriority_Type())
cnsSelInpSrcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsSelInpSrcPriority.setStatus(_A)
_CnsSelInpSrcTimestamp_Type=TimeStamp
_CnsSelInpSrcTimestamp_Object=MibTableColumn
cnsSelInpSrcTimestamp=_CnsSelInpSrcTimestamp_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,6),_CnsSelInpSrcTimestamp_Type())
cnsSelInpSrcTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsSelInpSrcTimestamp.setStatus(_A)
_CnsSelInpSrcFSW_Type=TruthValue
_CnsSelInpSrcFSW_Object=MibTableColumn
cnsSelInpSrcFSW=_CnsSelInpSrcFSW_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,7),_CnsSelInpSrcFSW_Type())
cnsSelInpSrcFSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsSelInpSrcFSW.setStatus(_A)
_CnsSelInpSrcMSW_Type=TruthValue
_CnsSelInpSrcMSW_Object=MibTableColumn
cnsSelInpSrcMSW=_CnsSelInpSrcMSW_Object((1,3,6,1,4,1,9,9,761,1,1,2,1,8),_CnsSelInpSrcMSW_Type())
cnsSelInpSrcMSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsSelInpSrcMSW.setStatus(_A)
_CnsInputSourceTable_Object=MibTable
cnsInputSourceTable=_CnsInputSourceTable_Object((1,3,6,1,4,1,9,9,761,1,1,3))
if mibBuilder.loadTexts:cnsInputSourceTable.setStatus(_A)
_CnsInputSourceEntry_Object=MibTableRow
cnsInputSourceEntry=_CnsInputSourceEntry_Object((1,3,6,1,4,1,9,9,761,1,1,3,1))
cnsInputSourceEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:cnsInputSourceEntry.setStatus(_A)
class _CnsInpSrcNetsyncIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnsInpSrcNetsyncIndex_Type.__name__=_D
_CnsInpSrcNetsyncIndex_Object=MibTableColumn
cnsInpSrcNetsyncIndex=_CnsInpSrcNetsyncIndex_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,1),_CnsInpSrcNetsyncIndex_Type())
cnsInpSrcNetsyncIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cnsInpSrcNetsyncIndex.setStatus(_A)
class _CnsInpSrcName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CnsInpSrcName_Type.__name__=_E
_CnsInpSrcName_Object=MibTableColumn
cnsInpSrcName=_CnsInpSrcName_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,2),_CnsInpSrcName_Type())
cnsInpSrcName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcName.setStatus(_A)
_CnsInpSrcIntfType_Type=CiscoNetsyncIfType
_CnsInpSrcIntfType_Object=MibTableColumn
cnsInpSrcIntfType=_CnsInpSrcIntfType_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,3),_CnsInpSrcIntfType_Type())
cnsInpSrcIntfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcIntfType.setStatus(_A)
class _CnsInpSrcPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnsInpSrcPriority_Type.__name__=_D
_CnsInpSrcPriority_Object=MibTableColumn
cnsInpSrcPriority=_CnsInpSrcPriority_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,4),_CnsInpSrcPriority_Type())
cnsInpSrcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcPriority.setStatus(_A)
_CnsInpSrcESMCCap_Type=CiscoNetsyncESMCCap
_CnsInpSrcESMCCap_Object=MibTableColumn
cnsInpSrcESMCCap=_CnsInpSrcESMCCap_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,5),_CnsInpSrcESMCCap_Type())
cnsInpSrcESMCCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcESMCCap.setStatus(_A)
_CnsInpSrcSSMCap_Type=CiscoNetsyncSSMCap
_CnsInpSrcSSMCap_Object=MibTableColumn
cnsInpSrcSSMCap=_CnsInpSrcSSMCap_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,6),_CnsInpSrcSSMCap_Type())
cnsInpSrcSSMCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcSSMCap.setStatus(_A)
_CnsInpSrcQualityLevelTxCfg_Type=CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelTxCfg_Object=MibTableColumn
cnsInpSrcQualityLevelTxCfg=_CnsInpSrcQualityLevelTxCfg_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,7),_CnsInpSrcQualityLevelTxCfg_Type())
cnsInpSrcQualityLevelTxCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcQualityLevelTxCfg.setStatus(_A)
_CnsInpSrcQualityLevelRxCfg_Type=CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelRxCfg_Object=MibTableColumn
cnsInpSrcQualityLevelRxCfg=_CnsInpSrcQualityLevelRxCfg_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,8),_CnsInpSrcQualityLevelRxCfg_Type())
cnsInpSrcQualityLevelRxCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcQualityLevelRxCfg.setStatus(_A)
_CnsInpSrcQualityLevelTx_Type=CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelTx_Object=MibTableColumn
cnsInpSrcQualityLevelTx=_CnsInpSrcQualityLevelTx_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,9),_CnsInpSrcQualityLevelTx_Type())
cnsInpSrcQualityLevelTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcQualityLevelTx.setStatus(_A)
_CnsInpSrcQualityLevelRx_Type=CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelRx_Object=MibTableColumn
cnsInpSrcQualityLevelRx=_CnsInpSrcQualityLevelRx_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,10),_CnsInpSrcQualityLevelRx_Type())
cnsInpSrcQualityLevelRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcQualityLevelRx.setStatus(_A)
_CnsInpSrcQualityLevel_Type=CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevel_Object=MibTableColumn
cnsInpSrcQualityLevel=_CnsInpSrcQualityLevel_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,11),_CnsInpSrcQualityLevel_Type())
cnsInpSrcQualityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcQualityLevel.setStatus(_A)
class _CnsInpSrcHoldoffTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CnsInpSrcHoldoffTime_Type.__name__=_D
_CnsInpSrcHoldoffTime_Object=MibTableColumn
cnsInpSrcHoldoffTime=_CnsInpSrcHoldoffTime_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,12),_CnsInpSrcHoldoffTime_Type())
cnsInpSrcHoldoffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcHoldoffTime.setStatus(_A)
if mibBuilder.loadTexts:cnsInpSrcHoldoffTime.setUnits(_K)
class _CnsInpSrcWtrTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CnsInpSrcWtrTime_Type.__name__=_D
_CnsInpSrcWtrTime_Object=MibTableColumn
cnsInpSrcWtrTime=_CnsInpSrcWtrTime_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,13),_CnsInpSrcWtrTime_Type())
cnsInpSrcWtrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcWtrTime.setStatus(_A)
if mibBuilder.loadTexts:cnsInpSrcWtrTime.setUnits('Seconds')
_CnsInpSrcLockout_Type=TruthValue
_CnsInpSrcLockout_Object=MibTableColumn
cnsInpSrcLockout=_CnsInpSrcLockout_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,14),_CnsInpSrcLockout_Type())
cnsInpSrcLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcLockout.setStatus(_A)
_CnsInpSrcSignalFailure_Type=TruthValue
_CnsInpSrcSignalFailure_Object=MibTableColumn
cnsInpSrcSignalFailure=_CnsInpSrcSignalFailure_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,15),_CnsInpSrcSignalFailure_Type())
cnsInpSrcSignalFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcSignalFailure.setStatus(_A)
_CnsInpSrcAlarm_Type=TruthValue
_CnsInpSrcAlarm_Object=MibTableColumn
cnsInpSrcAlarm=_CnsInpSrcAlarm_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,16),_CnsInpSrcAlarm_Type())
cnsInpSrcAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcAlarm.setStatus(_A)
_CnsInpSrcAlarmInfo_Type=CiscoNetsyncAlarmInfo
_CnsInpSrcAlarmInfo_Object=MibTableColumn
cnsInpSrcAlarmInfo=_CnsInpSrcAlarmInfo_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,17),_CnsInpSrcAlarmInfo_Type())
cnsInpSrcAlarmInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcAlarmInfo.setStatus(_A)
_CnsInpSrcFSW_Type=TruthValue
_CnsInpSrcFSW_Object=MibTableColumn
cnsInpSrcFSW=_CnsInpSrcFSW_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,18),_CnsInpSrcFSW_Type())
cnsInpSrcFSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcFSW.setStatus(_A)
_CnsInpSrcMSW_Type=TruthValue
_CnsInpSrcMSW_Object=MibTableColumn
cnsInpSrcMSW=_CnsInpSrcMSW_Object((1,3,6,1,4,1,9,9,761,1,1,3,1,19),_CnsInpSrcMSW_Type())
cnsInpSrcMSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsInpSrcMSW.setStatus(_A)
_CnsExtOutputTable_Object=MibTable
cnsExtOutputTable=_CnsExtOutputTable_Object((1,3,6,1,4,1,9,9,761,1,1,4))
if mibBuilder.loadTexts:cnsExtOutputTable.setStatus(_A)
_CnsExtOutputEntry_Object=MibTableRow
cnsExtOutputEntry=_CnsExtOutputEntry_Object((1,3,6,1,4,1,9,9,761,1,1,4,1))
cnsExtOutputEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cnsExtOutputEntry.setStatus(_A)
class _CnsExtOutListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnsExtOutListIndex_Type.__name__=_D
_CnsExtOutListIndex_Object=MibTableColumn
cnsExtOutListIndex=_CnsExtOutListIndex_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,1),_CnsExtOutListIndex_Type())
cnsExtOutListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cnsExtOutListIndex.setStatus(_A)
class _CnsExtOutSelNetsyncIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnsExtOutSelNetsyncIndex_Type.__name__=_D
_CnsExtOutSelNetsyncIndex_Object=MibTableColumn
cnsExtOutSelNetsyncIndex=_CnsExtOutSelNetsyncIndex_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,2),_CnsExtOutSelNetsyncIndex_Type())
cnsExtOutSelNetsyncIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutSelNetsyncIndex.setStatus(_A)
class _CnsExtOutName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CnsExtOutName_Type.__name__=_E
_CnsExtOutName_Object=MibTableColumn
cnsExtOutName=_CnsExtOutName_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,3),_CnsExtOutName_Type())
cnsExtOutName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutName.setStatus(_A)
_CnsExtOutIntfType_Type=CiscoNetsyncIfType
_CnsExtOutIntfType_Object=MibTableColumn
cnsExtOutIntfType=_CnsExtOutIntfType_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,4),_CnsExtOutIntfType_Type())
cnsExtOutIntfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutIntfType.setStatus(_A)
_CnsExtOutQualityLevel_Type=CiscoNetsyncQualityLevel
_CnsExtOutQualityLevel_Object=MibTableColumn
cnsExtOutQualityLevel=_CnsExtOutQualityLevel_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,5),_CnsExtOutQualityLevel_Type())
cnsExtOutQualityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutQualityLevel.setStatus(_A)
class _CnsExtOutPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnsExtOutPriority_Type.__name__=_D
_CnsExtOutPriority_Object=MibTableColumn
cnsExtOutPriority=_CnsExtOutPriority_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,6),_CnsExtOutPriority_Type())
cnsExtOutPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutPriority.setStatus(_A)
_CnsExtOutFSW_Type=TruthValue
_CnsExtOutFSW_Object=MibTableColumn
cnsExtOutFSW=_CnsExtOutFSW_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,7),_CnsExtOutFSW_Type())
cnsExtOutFSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutFSW.setStatus(_A)
_CnsExtOutMSW_Type=TruthValue
_CnsExtOutMSW_Object=MibTableColumn
cnsExtOutMSW=_CnsExtOutMSW_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,8),_CnsExtOutMSW_Type())
cnsExtOutMSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutMSW.setStatus(_A)
_CnsExtOutSquelch_Type=TruthValue
_CnsExtOutSquelch_Object=MibTableColumn
cnsExtOutSquelch=_CnsExtOutSquelch_Object((1,3,6,1,4,1,9,9,761,1,1,4,1,9),_CnsExtOutSquelch_Type())
cnsExtOutSquelch.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsExtOutSquelch.setStatus(_A)
_CnsT4ClockSourceTable_Object=MibTable
cnsT4ClockSourceTable=_CnsT4ClockSourceTable_Object((1,3,6,1,4,1,9,9,761,1,1,5))
if mibBuilder.loadTexts:cnsT4ClockSourceTable.setStatus(_A)
_CnsT4ClockSourceEntry_Object=MibTableRow
cnsT4ClockSourceEntry=_CnsT4ClockSourceEntry_Object((1,3,6,1,4,1,9,9,761,1,1,5,1))
cnsT4ClockSourceEntry.setIndexNames((0,_B,_L),(0,_B,_d))
if mibBuilder.loadTexts:cnsT4ClockSourceEntry.setStatus(_A)
class _CnsT4ClkSrcNetsyncIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnsT4ClkSrcNetsyncIndex_Type.__name__=_D
_CnsT4ClkSrcNetsyncIndex_Object=MibTableColumn
cnsT4ClkSrcNetsyncIndex=_CnsT4ClkSrcNetsyncIndex_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,1),_CnsT4ClkSrcNetsyncIndex_Type())
cnsT4ClkSrcNetsyncIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cnsT4ClkSrcNetsyncIndex.setStatus(_A)
class _CnsT4ClkSrcName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CnsT4ClkSrcName_Type.__name__=_E
_CnsT4ClkSrcName_Object=MibTableColumn
cnsT4ClkSrcName=_CnsT4ClkSrcName_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,2),_CnsT4ClkSrcName_Type())
cnsT4ClkSrcName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcName.setStatus(_A)
_CnsT4ClkSrcIntfType_Type=CiscoNetsyncIfType
_CnsT4ClkSrcIntfType_Object=MibTableColumn
cnsT4ClkSrcIntfType=_CnsT4ClkSrcIntfType_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,3),_CnsT4ClkSrcIntfType_Type())
cnsT4ClkSrcIntfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcIntfType.setStatus(_A)
class _CnsT4ClkSrcPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnsT4ClkSrcPriority_Type.__name__=_D
_CnsT4ClkSrcPriority_Object=MibTableColumn
cnsT4ClkSrcPriority=_CnsT4ClkSrcPriority_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,4),_CnsT4ClkSrcPriority_Type())
cnsT4ClkSrcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcPriority.setStatus(_A)
_CnsT4ClkSrcESMCCap_Type=CiscoNetsyncESMCCap
_CnsT4ClkSrcESMCCap_Object=MibTableColumn
cnsT4ClkSrcESMCCap=_CnsT4ClkSrcESMCCap_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,5),_CnsT4ClkSrcESMCCap_Type())
cnsT4ClkSrcESMCCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcESMCCap.setStatus(_A)
_CnsT4ClkSrcSSMCap_Type=CiscoNetsyncSSMCap
_CnsT4ClkSrcSSMCap_Object=MibTableColumn
cnsT4ClkSrcSSMCap=_CnsT4ClkSrcSSMCap_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,6),_CnsT4ClkSrcSSMCap_Type())
cnsT4ClkSrcSSMCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcSSMCap.setStatus(_A)
_CnsT4ClkSrcQualityLevelTxCfg_Type=CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelTxCfg_Object=MibTableColumn
cnsT4ClkSrcQualityLevelTxCfg=_CnsT4ClkSrcQualityLevelTxCfg_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,7),_CnsT4ClkSrcQualityLevelTxCfg_Type())
cnsT4ClkSrcQualityLevelTxCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcQualityLevelTxCfg.setStatus(_A)
_CnsT4ClkSrcQualityLevelRxCfg_Type=CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelRxCfg_Object=MibTableColumn
cnsT4ClkSrcQualityLevelRxCfg=_CnsT4ClkSrcQualityLevelRxCfg_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,8),_CnsT4ClkSrcQualityLevelRxCfg_Type())
cnsT4ClkSrcQualityLevelRxCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcQualityLevelRxCfg.setStatus(_A)
_CnsT4ClkSrcQualityLevelTx_Type=CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelTx_Object=MibTableColumn
cnsT4ClkSrcQualityLevelTx=_CnsT4ClkSrcQualityLevelTx_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,9),_CnsT4ClkSrcQualityLevelTx_Type())
cnsT4ClkSrcQualityLevelTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcQualityLevelTx.setStatus(_A)
_CnsT4ClkSrcQualityLevelRx_Type=CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelRx_Object=MibTableColumn
cnsT4ClkSrcQualityLevelRx=_CnsT4ClkSrcQualityLevelRx_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,10),_CnsT4ClkSrcQualityLevelRx_Type())
cnsT4ClkSrcQualityLevelRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcQualityLevelRx.setStatus(_A)
_CnsT4ClkSrcQualityLevel_Type=CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevel_Object=MibTableColumn
cnsT4ClkSrcQualityLevel=_CnsT4ClkSrcQualityLevel_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,11),_CnsT4ClkSrcQualityLevel_Type())
cnsT4ClkSrcQualityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcQualityLevel.setStatus(_A)
class _CnsT4ClkSrcHoldoffTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CnsT4ClkSrcHoldoffTime_Type.__name__=_D
_CnsT4ClkSrcHoldoffTime_Object=MibTableColumn
cnsT4ClkSrcHoldoffTime=_CnsT4ClkSrcHoldoffTime_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,12),_CnsT4ClkSrcHoldoffTime_Type())
cnsT4ClkSrcHoldoffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcHoldoffTime.setStatus(_A)
if mibBuilder.loadTexts:cnsT4ClkSrcHoldoffTime.setUnits(_K)
class _CnsT4ClkSrcWtrTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CnsT4ClkSrcWtrTime_Type.__name__=_D
_CnsT4ClkSrcWtrTime_Object=MibTableColumn
cnsT4ClkSrcWtrTime=_CnsT4ClkSrcWtrTime_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,13),_CnsT4ClkSrcWtrTime_Type())
cnsT4ClkSrcWtrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcWtrTime.setStatus(_A)
if mibBuilder.loadTexts:cnsT4ClkSrcWtrTime.setUnits(_H)
_CnsT4ClkSrcLockout_Type=TruthValue
_CnsT4ClkSrcLockout_Object=MibTableColumn
cnsT4ClkSrcLockout=_CnsT4ClkSrcLockout_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,14),_CnsT4ClkSrcLockout_Type())
cnsT4ClkSrcLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcLockout.setStatus(_A)
_CnsT4ClkSrcSignalFailure_Type=TruthValue
_CnsT4ClkSrcSignalFailure_Object=MibTableColumn
cnsT4ClkSrcSignalFailure=_CnsT4ClkSrcSignalFailure_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,15),_CnsT4ClkSrcSignalFailure_Type())
cnsT4ClkSrcSignalFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcSignalFailure.setStatus(_A)
_CnsT4ClkSrcAlarm_Type=TruthValue
_CnsT4ClkSrcAlarm_Object=MibTableColumn
cnsT4ClkSrcAlarm=_CnsT4ClkSrcAlarm_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,16),_CnsT4ClkSrcAlarm_Type())
cnsT4ClkSrcAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcAlarm.setStatus(_A)
_CnsT4ClkSrcAlarmInfo_Type=CiscoNetsyncAlarmInfo
_CnsT4ClkSrcAlarmInfo_Object=MibTableColumn
cnsT4ClkSrcAlarmInfo=_CnsT4ClkSrcAlarmInfo_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,17),_CnsT4ClkSrcAlarmInfo_Type())
cnsT4ClkSrcAlarmInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcAlarmInfo.setStatus(_A)
_CnsT4ClkSrcFSW_Type=TruthValue
_CnsT4ClkSrcFSW_Object=MibTableColumn
cnsT4ClkSrcFSW=_CnsT4ClkSrcFSW_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,18),_CnsT4ClkSrcFSW_Type())
cnsT4ClkSrcFSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcFSW.setStatus(_A)
_CnsT4ClkSrcMSW_Type=TruthValue
_CnsT4ClkSrcMSW_Object=MibTableColumn
cnsT4ClkSrcMSW=_CnsT4ClkSrcMSW_Object((1,3,6,1,4,1,9,9,761,1,1,5,1,19),_CnsT4ClkSrcMSW_Type())
cnsT4ClkSrcMSW.setMaxAccess(_C)
if mibBuilder.loadTexts:cnsT4ClkSrcMSW.setStatus(_A)
_CnsNotifObjects_ObjectIdentity=ObjectIdentity
cnsNotifObjects=_CnsNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,761,1,2))
_CnsInpSrcFailClear_Type=TruthValue
_CnsInpSrcFailClear_Object=MibScalar
cnsInpSrcFailClear=_CnsInpSrcFailClear_Object((1,3,6,1,4,1,9,9,761,1,2,1),_CnsInpSrcFailClear_Type())
cnsInpSrcFailClear.setMaxAccess(_e)
if mibBuilder.loadTexts:cnsInpSrcFailClear.setStatus(_A)
_CnsInpSrcAlarmClear_Type=TruthValue
_CnsInpSrcAlarmClear_Object=MibScalar
cnsInpSrcAlarmClear=_CnsInpSrcAlarmClear_Object((1,3,6,1,4,1,9,9,761,1,2,2),_CnsInpSrcAlarmClear_Type())
cnsInpSrcAlarmClear.setMaxAccess(_e)
if mibBuilder.loadTexts:cnsInpSrcAlarmClear.setStatus(_A)
_CiscoNetsyncMIBNotifControl_ObjectIdentity=ObjectIdentity
ciscoNetsyncMIBNotifControl=_CiscoNetsyncMIBNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,761,1,3))
class _CnsMIBEnableStatusNotification_Type(TruthValue):defaultValue=2
_CnsMIBEnableStatusNotification_Type.__name__=_F
_CnsMIBEnableStatusNotification_Object=MibScalar
cnsMIBEnableStatusNotification=_CnsMIBEnableStatusNotification_Object((1,3,6,1,4,1,9,9,761,1,3,1),_CnsMIBEnableStatusNotification_Type())
cnsMIBEnableStatusNotification.setMaxAccess('read-write')
if mibBuilder.loadTexts:cnsMIBEnableStatusNotification.setStatus(_A)
_CiscoNetsyncMIBConform_ObjectIdentity=ObjectIdentity
ciscoNetsyncMIBConform=_CiscoNetsyncMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,761,2))
_CiscoNetsyncMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNetsyncMIBCompliances=_CiscoNetsyncMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,761,2,1))
_CiscoNetsyncMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNetsyncMIBGroups=_CiscoNetsyncMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,761,2,2))
cnsClkSelGlobalObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,761,2,2,1))
cnsClkSelGlobalObjectGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cnsClkSelGlobalObjectGroup.setStatus(_A)
cnsSelectedInputSourceObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,761,2,2,2))
cnsSelectedInputSourceObjectGroup.setObjects(*((_B,_M),(_B,_N),(_B,_r),(_B,_s),(_B,_t),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cnsSelectedInputSourceObjectGroup.setStatus(_A)
cnsInputSourceObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,761,2,2,3))
cnsInputSourceObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_Q),(_B,_A7),(_B,_A8),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cnsInputSourceObjectGroup.setStatus(_A)
cnsExtOutputObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,761,2,2,4))
cnsExtOutputObjectGroup.setObjects(*((_B,_T),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:cnsExtOutputObjectGroup.setStatus(_A)
cnsT4ClkSrcObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,761,2,2,5))
cnsT4ClkSrcObjectGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_X),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:cnsT4ClkSrcObjectGroup.setStatus(_A)
cnsMIBNotifEnablesGroup=ObjectGroup((1,3,6,1,4,1,9,9,761,2,2,6))
cnsMIBNotifEnablesGroup.setObjects((_B,_AU))
if mibBuilder.loadTexts:cnsMIBNotifEnablesGroup.setStatus(_A)
ciscoNetsyncSelectedT0Clock=NotificationType((1,3,6,1,4,1,9,9,761,0,1))
ciscoNetsyncSelectedT0Clock.setObjects(*((_B,_M),(_B,_O),(_B,_N),(_B,_P)))
if mibBuilder.loadTexts:ciscoNetsyncSelectedT0Clock.setStatus(_A)
ciscoNetsyncSelectedT4Clock=NotificationType((1,3,6,1,4,1,9,9,761,0,2))
ciscoNetsyncSelectedT4Clock.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_X),(_B,_W)))
if mibBuilder.loadTexts:ciscoNetsyncSelectedT4Clock.setStatus(_A)
ciscoNetsyncInputSignalFailureStatus=NotificationType((1,3,6,1,4,1,9,9,761,0,3))
ciscoNetsyncInputSignalFailureStatus.setObjects(*((_B,_I),(_B,_J),(_B,_S)))
if mibBuilder.loadTexts:ciscoNetsyncInputSignalFailureStatus.setStatus(_A)
ciscoNetsyncInputAlarmStatus=NotificationType((1,3,6,1,4,1,9,9,761,0,4))
ciscoNetsyncInputAlarmStatus.setObjects(*((_B,_I),(_B,_J),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoNetsyncInputAlarmStatus.setStatus(_A)
ciscoNetsyncMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,761,2,2,7))
ciscoNetsyncMIBNotificationGroup.setObjects(*((_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:ciscoNetsyncMIBNotificationGroup.setStatus(_A)
ciscoNetsyncMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,761,2,1,1))
ciscoNetsyncMIBCompliance.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:ciscoNetsyncMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoNetsyncIfType':CiscoNetsyncIfType,_a:CiscoNetsyncNetworkOption,_Z:CiscoNetsyncEECOption,'CiscoNetsyncQLMode':CiscoNetsyncQLMode,'CiscoNetsyncClockMode':CiscoNetsyncClockMode,'CiscoNetsyncQualityLevel':CiscoNetsyncQualityLevel,'CiscoNetsyncSSMCap':CiscoNetsyncSSMCap,'CiscoNetsyncESMCCap':CiscoNetsyncESMCCap,'CiscoNetsyncAlarmInfo':CiscoNetsyncAlarmInfo,'ciscoNetsyncMIB':ciscoNetsyncMIB,'ciscoNetsyncMIBNotifs':ciscoNetsyncMIBNotifs,_AV:ciscoNetsyncSelectedT0Clock,_AW:ciscoNetsyncSelectedT4Clock,_AX:ciscoNetsyncInputSignalFailureStatus,_AY:ciscoNetsyncInputAlarmStatus,'ciscoNetsyncMIBObjects':ciscoNetsyncMIBObjects,'ciscoNetsyncMIBTables':ciscoNetsyncMIBTables,'cnsClkSelGlobalTable':cnsClkSelGlobalTable,'cnsClkSelGlobalEntry':cnsClkSelGlobalEntry,_Y:cnsClkSelGloProcIndex,_f:cnsClkSelGlobProcessMode,_g:cnsClkSelGlobClockMode,_h:cnsClkSelGlobNetsyncEnable,_i:cnsClkSelGlobRevertiveMode,_j:cnsClkSelGlobESMCMode,_k:cnsClkSelGlobEECOption,_l:cnsClkSelGlobNetworkOption,_m:cnsClkSelGlobHoldoffTime,_n:cnsClkSelGlobWtrTime,_o:cnsClkSelGlobNofSources,_p:cnsClkSelGlobLastHoldoverSeconds,_q:cnsClkSelGlobCurrHoldoverSeconds,'cnsSelectedInputSourceTable':cnsSelectedInputSourceTable,'cnsSelectedInputSourceEntry':cnsSelectedInputSourceEntry,_b:cnsSelInpSrcNetsyncIndex,_M:cnsSelInpSrcName,_O:cnsSelInpSrcIntfType,_N:cnsSelInpSrcQualityLevel,_P:cnsSelInpSrcPriority,_r:cnsSelInpSrcTimestamp,_s:cnsSelInpSrcFSW,_t:cnsSelInpSrcMSW,'cnsInputSourceTable':cnsInputSourceTable,'cnsInputSourceEntry':cnsInputSourceEntry,_c:cnsInpSrcNetsyncIndex,_I:cnsInpSrcName,_J:cnsInpSrcIntfType,_u:cnsInpSrcPriority,_v:cnsInpSrcESMCCap,_w:cnsInpSrcSSMCap,_x:cnsInpSrcQualityLevelTxCfg,_y:cnsInpSrcQualityLevelRxCfg,_z:cnsInpSrcQualityLevelTx,_A0:cnsInpSrcQualityLevelRx,_A1:cnsInpSrcQualityLevel,_A2:cnsInpSrcHoldoffTime,_A3:cnsInpSrcWtrTime,_A4:cnsInpSrcLockout,_A5:cnsInpSrcSignalFailure,_A6:cnsInpSrcAlarm,_Q:cnsInpSrcAlarmInfo,_A7:cnsInpSrcFSW,_A8:cnsInpSrcMSW,'cnsExtOutputTable':cnsExtOutputTable,'cnsExtOutputEntry':cnsExtOutputEntry,_L:cnsExtOutListIndex,_A9:cnsExtOutSelNetsyncIndex,_T:cnsExtOutName,_AA:cnsExtOutIntfType,_AB:cnsExtOutQualityLevel,_AC:cnsExtOutPriority,_AD:cnsExtOutFSW,_AE:cnsExtOutMSW,_AF:cnsExtOutSquelch,'cnsT4ClockSourceTable':cnsT4ClockSourceTable,'cnsT4ClockSourceEntry':cnsT4ClockSourceEntry,_d:cnsT4ClkSrcNetsyncIndex,_U:cnsT4ClkSrcName,_V:cnsT4ClkSrcIntfType,_W:cnsT4ClkSrcPriority,_AG:cnsT4ClkSrcESMCCap,_AH:cnsT4ClkSrcSSMCap,_AI:cnsT4ClkSrcQualityLevelTxCfg,_AJ:cnsT4ClkSrcQualityLevelRxCfg,_AK:cnsT4ClkSrcQualityLevelTx,_AL:cnsT4ClkSrcQualityLevelRx,_X:cnsT4ClkSrcQualityLevel,_AM:cnsT4ClkSrcHoldoffTime,_AN:cnsT4ClkSrcWtrTime,_AO:cnsT4ClkSrcLockout,_AP:cnsT4ClkSrcSignalFailure,_AQ:cnsT4ClkSrcAlarm,_AR:cnsT4ClkSrcAlarmInfo,_AS:cnsT4ClkSrcFSW,_AT:cnsT4ClkSrcMSW,'cnsNotifObjects':cnsNotifObjects,_S:cnsInpSrcFailClear,_R:cnsInpSrcAlarmClear,'ciscoNetsyncMIBNotifControl':ciscoNetsyncMIBNotifControl,_AU:cnsMIBEnableStatusNotification,'ciscoNetsyncMIBConform':ciscoNetsyncMIBConform,'ciscoNetsyncMIBCompliances':ciscoNetsyncMIBCompliances,'ciscoNetsyncMIBCompliance':ciscoNetsyncMIBCompliance,'ciscoNetsyncMIBGroups':ciscoNetsyncMIBGroups,_AZ:cnsClkSelGlobalObjectGroup,_Aa:cnsSelectedInputSourceObjectGroup,_Ab:cnsInputSourceObjectGroup,_Ac:cnsExtOutputObjectGroup,_Ad:cnsT4ClkSrcObjectGroup,_Af:cnsMIBNotifEnablesGroup,_Ae:ciscoNetsyncMIBNotificationGroup})