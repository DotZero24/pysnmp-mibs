_AK='h3cOnuSmlkSecondPonStatus'
_AJ='h3cOnuSmlkFirstPonStatus'
_AI='h3cEponOnuLaserState'
_AH='h3cEponStpPortState'
_AG='h3cEponStpPortDescr'
_AF='h3cEponOperationResult'
_AE='h3cOnuUpdateFileName'
_AD='h3cOnuRegType'
_AC='h3cOnuUpdateResult'
_AB='h3cEponLoopbackPortDescr'
_AA='h3cEponLoopbackPortIndex'
_A9='h3cOltPortAlarmLlidMismatchThreshold'
_A8='h3cOltPortAlarmLlidMisFrames'
_A7='h3cOltPortAlarmFerThreshold'
_A6='h3cOltPortAlarmFer'
_A5='h3cOltPortAlarmBerThreshold'
_A4='h3cOltPortAlarmBer'
_A3='h3cOnuUpdateByOnuTypeIndex'
_A2='updateONU'
_A1='resetUnknown'
_A0='h3cEponBatchOperationBySlotIndex'
_z='absent'
_y='notExist'
_x='h3cOnuCosToLocalPrecedenceCosIndex'
_w='h3cOnuDbaReportQueueId'
_v='h3cEponOnuTypeIndex'
_u='h3cOnuMacIndex'
_t='h3cOltUsingOnuNum'
_s='h3cOnuSilentMacAddr'
_r='notSetFilename'
_q='fileNotExist'
_p='update'
_o='h3cEponMulticastVlanId'
_n='h3cEponOuiIndex'
_m='h3cOnuBindMacAddress'
_l='h3cEponOnuRegSilentMac'
_k='h3cOamEventLogLocation'
_j='h3cOamEventLogType'
_i='h3cEponSoftwareErrorCode'
_h='h3cOamVendorSpecificAlarmCode'
_g='h3cEponOnuRegErrorMacAddr'
_f='h3cOltPortAlarmFerDirect'
_e='h3cOltPortAlarmBerDirect'
_d='h3cOnuRS485SessionIndex'
_c='h3cOnuSmlkGroupID'
_b='h3cEponStpPortIndex'
_a='h3cOnuQueueId'
_Z='h3cOnuQueueDirection'
_Y='fail'
_X='DisplayString'
_W='hwLswSlotIndex'
_V='hwLswFrameIndex'
_U='null'
_T='down'
_S='h3cOnuRS485SerialIndex'
_R='other'
_Q='h3cEponSlotIndex'
_P='A3COM-HUAWEI-DEVICE-MIB'
_O='disable'
_N='enable'
_M='not-accessible'
_L='OctetString'
_K='read-create'
_J='accessible-for-notify'
_I='ifDescr'
_H='TruthValue'
_G='A3COM-HUAWEI-EPON-MIB'
_F='ifIndex'
_E='Integer32'
_D='IF-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwLswFrameIndex,hwLswSlotIndex=mibBuilder.importSymbols(_P,_V,_W)
h3cEpon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cEpon')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_I,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_X,'MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
h3cEponMibObjects=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1))
_H3cEponSysMan_ObjectIdentity=ObjectIdentity
h3cEponSysMan=_H3cEponSysMan_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,1))
class _H3cEponAutoAuthorize_Type(TruthValue):defaultValue=2
_H3cEponAutoAuthorize_Type.__name__=_H
_H3cEponAutoAuthorize_Object=MibScalar
h3cEponAutoAuthorize=_H3cEponAutoAuthorize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,1),_H3cEponAutoAuthorize_Type())
h3cEponAutoAuthorize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutoAuthorize.setStatus(_A)
_H3cEponMonitorCycle_Type=Integer32
_H3cEponMonitorCycle_Object=MibScalar
h3cEponMonitorCycle=_H3cEponMonitorCycle_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,2),_H3cEponMonitorCycle_Type())
h3cEponMonitorCycle.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponMonitorCycle.setStatus(_A)
class _H3cEponMsgTimeOut_Type(Integer32):defaultValue=600
_H3cEponMsgTimeOut_Type.__name__=_E
_H3cEponMsgTimeOut_Object=MibScalar
h3cEponMsgTimeOut=_H3cEponMsgTimeOut_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,3),_H3cEponMsgTimeOut_Type())
h3cEponMsgTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponMsgTimeOut.setStatus(_A)
class _H3cEponMsgLoseNum_Type(Integer32):defaultValue=20
_H3cEponMsgLoseNum_Type.__name__=_E
_H3cEponMsgLoseNum_Object=MibScalar
h3cEponMsgLoseNum=_H3cEponMsgLoseNum_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,4),_H3cEponMsgLoseNum_Type())
h3cEponMsgLoseNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponMsgLoseNum.setStatus(_A)
_H3cEponSysHasEPONBoard_Type=TruthValue
_H3cEponSysHasEPONBoard_Object=MibScalar
h3cEponSysHasEPONBoard=_H3cEponSysHasEPONBoard_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,5),_H3cEponSysHasEPONBoard_Type())
h3cEponSysHasEPONBoard.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponSysHasEPONBoard.setStatus(_A)
class _H3cEponMonitorCycleEnable_Type(TruthValue):defaultValue=1
_H3cEponMonitorCycleEnable_Type.__name__=_H
_H3cEponMonitorCycleEnable_Object=MibScalar
h3cEponMonitorCycleEnable=_H3cEponMonitorCycleEnable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,6),_H3cEponMonitorCycleEnable_Type())
h3cEponMonitorCycleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponMonitorCycleEnable.setStatus(_A)
class _H3cEponOltSoftwareErrAlmEnable_Type(TruthValue):defaultValue=1
_H3cEponOltSoftwareErrAlmEnable_Type.__name__=_H
_H3cEponOltSoftwareErrAlmEnable_Object=MibScalar
h3cEponOltSoftwareErrAlmEnable=_H3cEponOltSoftwareErrAlmEnable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,7),_H3cEponOltSoftwareErrAlmEnable_Type())
h3cEponOltSoftwareErrAlmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponOltSoftwareErrAlmEnable.setStatus(_A)
class _H3cEponPortLoopBackAlmEnable_Type(TruthValue):defaultValue=1
_H3cEponPortLoopBackAlmEnable_Type.__name__=_H
_H3cEponPortLoopBackAlmEnable_Object=MibScalar
h3cEponPortLoopBackAlmEnable=_H3cEponPortLoopBackAlmEnable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,8),_H3cEponPortLoopBackAlmEnable_Type())
h3cEponPortLoopBackAlmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponPortLoopBackAlmEnable.setStatus(_A)
_H3cEponMonitorCycleMinVal_Type=Integer32
_H3cEponMonitorCycleMinVal_Object=MibScalar
h3cEponMonitorCycleMinVal=_H3cEponMonitorCycleMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,9),_H3cEponMonitorCycleMinVal_Type())
h3cEponMonitorCycleMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponMonitorCycleMinVal.setStatus(_A)
_H3cEponMonitorCycleMaxVal_Type=Integer32
_H3cEponMonitorCycleMaxVal_Object=MibScalar
h3cEponMonitorCycleMaxVal=_H3cEponMonitorCycleMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,10),_H3cEponMonitorCycleMaxVal_Type())
h3cEponMonitorCycleMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponMonitorCycleMaxVal.setStatus(_A)
_H3cEponMsgTimeOutMinVal_Type=Integer32
_H3cEponMsgTimeOutMinVal_Object=MibScalar
h3cEponMsgTimeOutMinVal=_H3cEponMsgTimeOutMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,11),_H3cEponMsgTimeOutMinVal_Type())
h3cEponMsgTimeOutMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponMsgTimeOutMinVal.setStatus(_A)
_H3cEponMsgTimeOutMaxVal_Type=Integer32
_H3cEponMsgTimeOutMaxVal_Object=MibScalar
h3cEponMsgTimeOutMaxVal=_H3cEponMsgTimeOutMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,12),_H3cEponMsgTimeOutMaxVal_Type())
h3cEponMsgTimeOutMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponMsgTimeOutMaxVal.setStatus(_A)
_H3cEponMsgLoseNumMinVal_Type=Integer32
_H3cEponMsgLoseNumMinVal_Object=MibScalar
h3cEponMsgLoseNumMinVal=_H3cEponMsgLoseNumMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,13),_H3cEponMsgLoseNumMinVal_Type())
h3cEponMsgLoseNumMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponMsgLoseNumMinVal.setStatus(_A)
_H3cEponMsgLoseNumMaxVal_Type=Integer32
_H3cEponMsgLoseNumMaxVal_Object=MibScalar
h3cEponMsgLoseNumMaxVal=_H3cEponMsgLoseNumMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,14),_H3cEponMsgLoseNumMaxVal_Type())
h3cEponMsgLoseNumMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponMsgLoseNumMaxVal.setStatus(_A)
_H3cEponSysScalarGroup_ObjectIdentity=ObjectIdentity
h3cEponSysScalarGroup=_H3cEponSysScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,1,15))
_H3cEponSysManTable_Object=MibTable
h3cEponSysManTable=_H3cEponSysManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16))
if mibBuilder.loadTexts:h3cEponSysManTable.setStatus(_A)
_H3cEponSysManEntry_Object=MibTableRow
h3cEponSysManEntry=_H3cEponSysManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1))
h3cEponSysManEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:h3cEponSysManEntry.setStatus(_A)
_H3cEponSlotIndex_Type=Integer32
_H3cEponSlotIndex_Object=MibTableColumn
h3cEponSlotIndex=_H3cEponSlotIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1,1),_H3cEponSlotIndex_Type())
h3cEponSlotIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEponSlotIndex.setStatus(_A)
class _H3cEponModeSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cmode',1),('hmode',2)))
_H3cEponModeSwitch_Type.__name__=_E
_H3cEponModeSwitch_Object=MibTableColumn
h3cEponModeSwitch=_H3cEponModeSwitch_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1,2),_H3cEponModeSwitch_Type())
h3cEponModeSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponModeSwitch.setStatus(_A)
class _H3cEponAutomaticMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cEponAutomaticMode_Type.__name__=_E
_H3cEponAutomaticMode_Object=MibTableColumn
h3cEponAutomaticMode=_H3cEponAutomaticMode_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1,3),_H3cEponAutomaticMode_Type())
h3cEponAutomaticMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutomaticMode.setStatus(_A)
class _H3cEponOamDiscoveryTimeout_Type(Integer32):defaultValue=30
_H3cEponOamDiscoveryTimeout_Type.__name__=_E
_H3cEponOamDiscoveryTimeout_Object=MibTableColumn
h3cEponOamDiscoveryTimeout=_H3cEponOamDiscoveryTimeout_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1,4),_H3cEponOamDiscoveryTimeout_Type())
h3cEponOamDiscoveryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponOamDiscoveryTimeout.setStatus(_A)
class _H3cEponEncryptionNoReplyTimeOut_Type(Integer32):defaultValue=30
_H3cEponEncryptionNoReplyTimeOut_Type.__name__=_E
_H3cEponEncryptionNoReplyTimeOut_Object=MibTableColumn
h3cEponEncryptionNoReplyTimeOut=_H3cEponEncryptionNoReplyTimeOut_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1,5),_H3cEponEncryptionNoReplyTimeOut_Type())
h3cEponEncryptionNoReplyTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponEncryptionNoReplyTimeOut.setStatus(_A)
class _H3cEponEncryptionUpdateTime_Type(Integer32):defaultValue=10
_H3cEponEncryptionUpdateTime_Type.__name__=_E
_H3cEponEncryptionUpdateTime_Object=MibTableColumn
h3cEponEncryptionUpdateTime=_H3cEponEncryptionUpdateTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1,6),_H3cEponEncryptionUpdateTime_Type())
h3cEponEncryptionUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponEncryptionUpdateTime.setStatus(_A)
class _H3cEponAutoBindStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cEponAutoBindStatus_Type.__name__=_E
_H3cEponAutoBindStatus_Object=MibTableColumn
h3cEponAutoBindStatus=_H3cEponAutoBindStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,16,1,7),_H3cEponAutoBindStatus_Type())
h3cEponAutoBindStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutoBindStatus.setStatus(_A)
_H3cEponAutoUpdateTable_Object=MibTable
h3cEponAutoUpdateTable=_H3cEponAutoUpdateTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,17))
if mibBuilder.loadTexts:h3cEponAutoUpdateTable.setStatus(_A)
_H3cEponAutoUpdateEntry_Object=MibTableRow
h3cEponAutoUpdateEntry=_H3cEponAutoUpdateEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,17,1))
h3cEponAutoUpdateEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:h3cEponAutoUpdateEntry.setStatus(_A)
class _H3cEponAutoUpdateFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponAutoUpdateFileName_Type.__name__=_X
_H3cEponAutoUpdateFileName_Object=MibTableColumn
h3cEponAutoUpdateFileName=_H3cEponAutoUpdateFileName_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,17,1,1),_H3cEponAutoUpdateFileName_Type())
h3cEponAutoUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutoUpdateFileName.setStatus(_A)
class _H3cEponAutoUpdateSchedStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cEponAutoUpdateSchedStatus_Type.__name__=_E
_H3cEponAutoUpdateSchedStatus_Object=MibTableColumn
h3cEponAutoUpdateSchedStatus=_H3cEponAutoUpdateSchedStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,17,1,2),_H3cEponAutoUpdateSchedStatus_Type())
h3cEponAutoUpdateSchedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutoUpdateSchedStatus.setStatus(_A)
class _H3cEponAutoUpdateSchedTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponAutoUpdateSchedTime_Type.__name__=_L
_H3cEponAutoUpdateSchedTime_Object=MibTableColumn
h3cEponAutoUpdateSchedTime=_H3cEponAutoUpdateSchedTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,17,1,3),_H3cEponAutoUpdateSchedTime_Type())
h3cEponAutoUpdateSchedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutoUpdateSchedTime.setStatus(_A)
class _H3cEponAutoUpdateSchedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('daily',1),('weekly',2),('comingdate',3)))
_H3cEponAutoUpdateSchedType_Type.__name__=_E
_H3cEponAutoUpdateSchedType_Object=MibTableColumn
h3cEponAutoUpdateSchedType=_H3cEponAutoUpdateSchedType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,17,1,4),_H3cEponAutoUpdateSchedType_Type())
h3cEponAutoUpdateSchedType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutoUpdateSchedType.setStatus(_A)
class _H3cEponAutoUpdateRealTimeStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cEponAutoUpdateRealTimeStatus_Type.__name__=_E
_H3cEponAutoUpdateRealTimeStatus_Object=MibTableColumn
h3cEponAutoUpdateRealTimeStatus=_H3cEponAutoUpdateRealTimeStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,17,1,5),_H3cEponAutoUpdateRealTimeStatus_Type())
h3cEponAutoUpdateRealTimeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponAutoUpdateRealTimeStatus.setStatus(_A)
_H3cEponOuiIndexNextTable_Object=MibTable
h3cEponOuiIndexNextTable=_H3cEponOuiIndexNextTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,18))
if mibBuilder.loadTexts:h3cEponOuiIndexNextTable.setStatus(_A)
_H3cEponOuiIndexNextEntry_Object=MibTableRow
h3cEponOuiIndexNextEntry=_H3cEponOuiIndexNextEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,18,1))
h3cEponOuiIndexNextEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:h3cEponOuiIndexNextEntry.setStatus(_A)
_H3cEponOuiIndexNext_Type=Integer32
_H3cEponOuiIndexNext_Object=MibTableColumn
h3cEponOuiIndexNext=_H3cEponOuiIndexNext_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,18,1,1),_H3cEponOuiIndexNext_Type())
h3cEponOuiIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponOuiIndexNext.setStatus(_A)
_H3cEponOuiTable_Object=MibTable
h3cEponOuiTable=_H3cEponOuiTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,19))
if mibBuilder.loadTexts:h3cEponOuiTable.setStatus(_A)
_H3cEponOuiEntry_Object=MibTableRow
h3cEponOuiEntry=_H3cEponOuiEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,19,1))
h3cEponOuiEntry.setIndexNames((0,_G,_Q),(0,_G,_n))
if mibBuilder.loadTexts:h3cEponOuiEntry.setStatus(_A)
_H3cEponOuiIndex_Type=Integer32
_H3cEponOuiIndex_Object=MibTableColumn
h3cEponOuiIndex=_H3cEponOuiIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,19,1,1),_H3cEponOuiIndex_Type())
h3cEponOuiIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEponOuiIndex.setStatus(_A)
class _H3cEponOuiValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_H3cEponOuiValue_Type.__name__=_L
_H3cEponOuiValue_Object=MibTableColumn
h3cEponOuiValue=_H3cEponOuiValue_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,19,1,2),_H3cEponOuiValue_Type())
h3cEponOuiValue.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponOuiValue.setStatus(_A)
class _H3cEponOamVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponOamVersion_Type.__name__=_L
_H3cEponOamVersion_Object=MibTableColumn
h3cEponOamVersion=_H3cEponOamVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,19,1,3),_H3cEponOamVersion_Type())
h3cEponOamVersion.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponOamVersion.setStatus(_A)
_H3cEponOuiRowStatus_Type=RowStatus
_H3cEponOuiRowStatus_Object=MibTableColumn
h3cEponOuiRowStatus=_H3cEponOuiRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,19,1,4),_H3cEponOuiRowStatus_Type())
h3cEponOuiRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponOuiRowStatus.setStatus(_A)
_H3cEponMulticastControlTable_Object=MibTable
h3cEponMulticastControlTable=_H3cEponMulticastControlTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,20))
if mibBuilder.loadTexts:h3cEponMulticastControlTable.setStatus(_A)
_H3cEponMulticastControlEntry_Object=MibTableRow
h3cEponMulticastControlEntry=_H3cEponMulticastControlEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,20,1))
h3cEponMulticastControlEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:h3cEponMulticastControlEntry.setStatus(_A)
_H3cEponMulticastVlanId_Type=Integer32
_H3cEponMulticastVlanId_Object=MibTableColumn
h3cEponMulticastVlanId=_H3cEponMulticastVlanId_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,20,1,1),_H3cEponMulticastVlanId_Type())
h3cEponMulticastVlanId.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEponMulticastVlanId.setStatus(_A)
class _H3cEponMulticastAddressList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponMulticastAddressList_Type.__name__=_L
_H3cEponMulticastAddressList_Object=MibTableColumn
h3cEponMulticastAddressList=_H3cEponMulticastAddressList_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,20,1,2),_H3cEponMulticastAddressList_Type())
h3cEponMulticastAddressList.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponMulticastAddressList.setStatus(_A)
_H3cEponMulticastStatus_Type=RowStatus
_H3cEponMulticastStatus_Object=MibTableColumn
h3cEponMulticastStatus=_H3cEponMulticastStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,1,20,1,3),_H3cEponMulticastStatus_Type())
h3cEponMulticastStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponMulticastStatus.setStatus(_A)
_H3cEponFileName_ObjectIdentity=ObjectIdentity
h3cEponFileName=_H3cEponFileName_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,2))
class _H3cEponDbaUpdateFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cEponDbaUpdateFileName_Type.__name__=_L
_H3cEponDbaUpdateFileName_Object=MibScalar
h3cEponDbaUpdateFileName=_H3cEponDbaUpdateFileName_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,2,1),_H3cEponDbaUpdateFileName_Type())
h3cEponDbaUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponDbaUpdateFileName.setStatus(_A)
class _H3cEponOnuUpdateFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cEponOnuUpdateFileName_Type.__name__=_L
_H3cEponOnuUpdateFileName_Object=MibScalar
h3cEponOnuUpdateFileName=_H3cEponOnuUpdateFileName_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,2,2),_H3cEponOnuUpdateFileName_Type())
h3cEponOnuUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponOnuUpdateFileName.setStatus(_A)
_H3cEponOltMan_ObjectIdentity=ObjectIdentity
h3cEponOltMan=_H3cEponOltMan_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,3))
_H3cOltSysManTable_Object=MibTable
h3cOltSysManTable=_H3cOltSysManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1))
if mibBuilder.loadTexts:h3cOltSysManTable.setStatus(_A)
_H3cOltSysManEntry_Object=MibTableRow
h3cOltSysManEntry=_H3cOltSysManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1))
h3cOltSysManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOltSysManEntry.setStatus(_A)
class _H3cOltLaserOnTime_Type(Integer32):defaultValue=96
_H3cOltLaserOnTime_Type.__name__=_E
_H3cOltLaserOnTime_Object=MibTableColumn
h3cOltLaserOnTime=_H3cOltLaserOnTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1,1),_H3cOltLaserOnTime_Type())
h3cOltLaserOnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltLaserOnTime.setStatus(_A)
class _H3cOltLaserOffTime_Type(Integer32):defaultValue=96
_H3cOltLaserOffTime_Type.__name__=_E
_H3cOltLaserOffTime_Object=MibTableColumn
h3cOltLaserOffTime=_H3cOltLaserOffTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1,2),_H3cOltLaserOffTime_Type())
h3cOltLaserOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltLaserOffTime.setStatus(_A)
class _H3cOltMultiCopyBrdCast_Type(TruthValue):defaultValue=2
_H3cOltMultiCopyBrdCast_Type.__name__=_H
_H3cOltMultiCopyBrdCast_Object=MibTableColumn
h3cOltMultiCopyBrdCast=_H3cOltMultiCopyBrdCast_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1,3),_H3cOltMultiCopyBrdCast_Type())
h3cOltMultiCopyBrdCast.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltMultiCopyBrdCast.setStatus(_A)
class _H3cOltEnableDiscardPacket_Type(TruthValue):defaultValue=2
_H3cOltEnableDiscardPacket_Type.__name__=_H
_H3cOltEnableDiscardPacket_Object=MibTableColumn
h3cOltEnableDiscardPacket=_H3cOltEnableDiscardPacket_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1,4),_H3cOltEnableDiscardPacket_Type())
h3cOltEnableDiscardPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltEnableDiscardPacket.setStatus(_A)
class _H3cOltSelfTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('selftest',1))
_H3cOltSelfTest_Type.__name__=_E
_H3cOltSelfTest_Object=MibTableColumn
h3cOltSelfTest=_H3cOltSelfTest_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1,5),_H3cOltSelfTest_Type())
h3cOltSelfTest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltSelfTest.setStatus(_A)
class _H3cOltSelfTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('ok',2),(_Y,3)))
_H3cOltSelfTestResult_Type.__name__=_E
_H3cOltSelfTestResult_Object=MibTableColumn
h3cOltSelfTestResult=_H3cOltSelfTestResult_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1,6),_H3cOltSelfTestResult_Type())
h3cOltSelfTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltSelfTestResult.setStatus(_A)
_H3cOltMaxRtt_Type=Unsigned32
_H3cOltMaxRtt_Object=MibTableColumn
h3cOltMaxRtt=_H3cOltMaxRtt_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,1,1,7),_H3cOltMaxRtt_Type())
h3cOltMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltMaxRtt.setStatus(_A)
_H3cOltInfoTable_Object=MibTable
h3cOltInfoTable=_H3cOltInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2))
if mibBuilder.loadTexts:h3cOltInfoTable.setStatus(_A)
_H3cOltInfoEntry_Object=MibTableRow
h3cOltInfoEntry=_H3cOltInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1))
h3cOltInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOltInfoEntry.setStatus(_A)
_H3cOltFirmMajorVersion_Type=OctetString
_H3cOltFirmMajorVersion_Object=MibTableColumn
h3cOltFirmMajorVersion=_H3cOltFirmMajorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,1),_H3cOltFirmMajorVersion_Type())
h3cOltFirmMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltFirmMajorVersion.setStatus(_A)
_H3cOltFirmMinorVersion_Type=OctetString
_H3cOltFirmMinorVersion_Object=MibTableColumn
h3cOltFirmMinorVersion=_H3cOltFirmMinorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,2),_H3cOltFirmMinorVersion_Type())
h3cOltFirmMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltFirmMinorVersion.setStatus(_A)
_H3cOltHardMajorVersion_Type=OctetString
_H3cOltHardMajorVersion_Object=MibTableColumn
h3cOltHardMajorVersion=_H3cOltHardMajorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,3),_H3cOltHardMajorVersion_Type())
h3cOltHardMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltHardMajorVersion.setStatus(_A)
_H3cOltHardMinorVersion_Type=OctetString
_H3cOltHardMinorVersion_Object=MibTableColumn
h3cOltHardMinorVersion=_H3cOltHardMinorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,4),_H3cOltHardMinorVersion_Type())
h3cOltHardMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltHardMinorVersion.setStatus(_A)
_H3cOltAgcLockTime_Type=Integer32
_H3cOltAgcLockTime_Object=MibTableColumn
h3cOltAgcLockTime=_H3cOltAgcLockTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,5),_H3cOltAgcLockTime_Type())
h3cOltAgcLockTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltAgcLockTime.setStatus(_A)
_H3cOltAgcCdrTime_Type=Integer32
_H3cOltAgcCdrTime_Object=MibTableColumn
h3cOltAgcCdrTime=_H3cOltAgcCdrTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,6),_H3cOltAgcCdrTime_Type())
h3cOltAgcCdrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltAgcCdrTime.setStatus(_A)
_H3cOltMacAddress_Type=MacAddress
_H3cOltMacAddress_Object=MibTableColumn
h3cOltMacAddress=_H3cOltMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,7),_H3cOltMacAddress_Type())
h3cOltMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltMacAddress.setStatus(_A)
class _H3cOltWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('open',2),('reset',3),('closed',4)))
_H3cOltWorkMode_Type.__name__=_E
_H3cOltWorkMode_Object=MibTableColumn
h3cOltWorkMode=_H3cOltWorkMode_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,8),_H3cOltWorkMode_Type())
h3cOltWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltWorkMode.setStatus(_A)
_H3cOltOpticalPowerTx_Type=Integer32
_H3cOltOpticalPowerTx_Object=MibTableColumn
h3cOltOpticalPowerTx=_H3cOltOpticalPowerTx_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,9),_H3cOltOpticalPowerTx_Type())
h3cOltOpticalPowerTx.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltOpticalPowerTx.setStatus(_A)
_H3cOltOpticalPowerRx_Type=Integer32
_H3cOltOpticalPowerRx_Object=MibTableColumn
h3cOltOpticalPowerRx=_H3cOltOpticalPowerRx_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,2,1,10),_H3cOltOpticalPowerRx_Type())
h3cOltOpticalPowerRx.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltOpticalPowerRx.setStatus(_A)
_H3cOltDbaManTable_Object=MibTable
h3cOltDbaManTable=_H3cOltDbaManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3))
if mibBuilder.loadTexts:h3cOltDbaManTable.setStatus(_A)
_H3cOltDbaManEntry_Object=MibTableRow
h3cOltDbaManEntry=_H3cOltDbaManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1))
h3cOltDbaManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOltDbaManEntry.setStatus(_A)
class _H3cOltDbaEnabledType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_H3cOltDbaEnabledType_Type.__name__=_E
_H3cOltDbaEnabledType_Object=MibTableColumn
h3cOltDbaEnabledType=_H3cOltDbaEnabledType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1,1),_H3cOltDbaEnabledType_Type())
h3cOltDbaEnabledType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltDbaEnabledType.setStatus(_A)
class _H3cOltDbaDiscoveryLength_Type(Integer32):defaultValue=41500
_H3cOltDbaDiscoveryLength_Type.__name__=_E
_H3cOltDbaDiscoveryLength_Object=MibTableColumn
h3cOltDbaDiscoveryLength=_H3cOltDbaDiscoveryLength_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1,2),_H3cOltDbaDiscoveryLength_Type())
h3cOltDbaDiscoveryLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltDbaDiscoveryLength.setStatus(_A)
class _H3cOltDbaDiscovryFrequency_Type(Integer32):defaultValue=50
_H3cOltDbaDiscovryFrequency_Type.__name__=_E
_H3cOltDbaDiscovryFrequency_Object=MibTableColumn
h3cOltDbaDiscovryFrequency=_H3cOltDbaDiscovryFrequency_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1,3),_H3cOltDbaDiscovryFrequency_Type())
h3cOltDbaDiscovryFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltDbaDiscovryFrequency.setStatus(_A)
class _H3cOltDbaCycleLength_Type(Integer32):defaultValue=65535
_H3cOltDbaCycleLength_Type.__name__=_E
_H3cOltDbaCycleLength_Object=MibTableColumn
h3cOltDbaCycleLength=_H3cOltDbaCycleLength_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1,4),_H3cOltDbaCycleLength_Type())
h3cOltDbaCycleLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltDbaCycleLength.setStatus(_A)
_H3cOltDbaVersion_Type=OctetString
_H3cOltDbaVersion_Object=MibTableColumn
h3cOltDbaVersion=_H3cOltDbaVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1,5),_H3cOltDbaVersion_Type())
h3cOltDbaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaVersion.setStatus(_A)
class _H3cOltDbaUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_p,1))
_H3cOltDbaUpdate_Type.__name__=_E
_H3cOltDbaUpdate_Object=MibTableColumn
h3cOltDbaUpdate=_H3cOltDbaUpdate_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1,6),_H3cOltDbaUpdate_Type())
h3cOltDbaUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltDbaUpdate.setStatus(_A)
class _H3cOltDbaUpdateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),('ok',2),(_Y,3),(_q,4),(_r,5)))
_H3cOltDbaUpdateResult_Type.__name__=_E
_H3cOltDbaUpdateResult_Object=MibTableColumn
h3cOltDbaUpdateResult=_H3cOltDbaUpdateResult_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,3,1,7),_H3cOltDbaUpdateResult_Type())
h3cOltDbaUpdateResult.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaUpdateResult.setStatus(_A)
_H3cOltPortAlarmThresholdTable_Object=MibTable
h3cOltPortAlarmThresholdTable=_H3cOltPortAlarmThresholdTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4))
if mibBuilder.loadTexts:h3cOltPortAlarmThresholdTable.setStatus(_A)
_H3cOltPortAlarmThresholdEntry_Object=MibTableRow
h3cOltPortAlarmThresholdEntry=_H3cOltPortAlarmThresholdEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1))
h3cOltPortAlarmThresholdEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOltPortAlarmThresholdEntry.setStatus(_A)
class _H3cOltPortAlarmBerEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmBerEnabled_Type.__name__=_H
_H3cOltPortAlarmBerEnabled_Object=MibTableColumn
h3cOltPortAlarmBerEnabled=_H3cOltPortAlarmBerEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,1),_H3cOltPortAlarmBerEnabled_Type())
h3cOltPortAlarmBerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmBerEnabled.setStatus(_A)
class _H3cOltPortAlarmBerDirect_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('berUplink',1),('berDownlink',2),('berAll',3)))
_H3cOltPortAlarmBerDirect_Type.__name__=_E
_H3cOltPortAlarmBerDirect_Object=MibTableColumn
h3cOltPortAlarmBerDirect=_H3cOltPortAlarmBerDirect_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,2),_H3cOltPortAlarmBerDirect_Type())
h3cOltPortAlarmBerDirect.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmBerDirect.setStatus(_A)
class _H3cOltPortAlarmBerThreshold_Type(Integer32):defaultValue=10
_H3cOltPortAlarmBerThreshold_Type.__name__=_E
_H3cOltPortAlarmBerThreshold_Object=MibTableColumn
h3cOltPortAlarmBerThreshold=_H3cOltPortAlarmBerThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,3),_H3cOltPortAlarmBerThreshold_Type())
h3cOltPortAlarmBerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmBerThreshold.setStatus(_A)
class _H3cOltPortAlarmFerEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmFerEnabled_Type.__name__=_H
_H3cOltPortAlarmFerEnabled_Object=MibTableColumn
h3cOltPortAlarmFerEnabled=_H3cOltPortAlarmFerEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,4),_H3cOltPortAlarmFerEnabled_Type())
h3cOltPortAlarmFerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmFerEnabled.setStatus(_A)
class _H3cOltPortAlarmFerDirect_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ferUplink',1),('ferDownlink',2),('ferAll',3)))
_H3cOltPortAlarmFerDirect_Type.__name__=_E
_H3cOltPortAlarmFerDirect_Object=MibTableColumn
h3cOltPortAlarmFerDirect=_H3cOltPortAlarmFerDirect_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,5),_H3cOltPortAlarmFerDirect_Type())
h3cOltPortAlarmFerDirect.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmFerDirect.setStatus(_A)
class _H3cOltPortAlarmFerThreshold_Type(Integer32):defaultValue=1
_H3cOltPortAlarmFerThreshold_Type.__name__=_E
_H3cOltPortAlarmFerThreshold_Object=MibTableColumn
h3cOltPortAlarmFerThreshold=_H3cOltPortAlarmFerThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,6),_H3cOltPortAlarmFerThreshold_Type())
h3cOltPortAlarmFerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmFerThreshold.setStatus(_A)
class _H3cOltPortAlarmLlidMismatchEnabled_Type(TruthValue):defaultValue=2
_H3cOltPortAlarmLlidMismatchEnabled_Type.__name__=_H
_H3cOltPortAlarmLlidMismatchEnabled_Object=MibTableColumn
h3cOltPortAlarmLlidMismatchEnabled=_H3cOltPortAlarmLlidMismatchEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,7),_H3cOltPortAlarmLlidMismatchEnabled_Type())
h3cOltPortAlarmLlidMismatchEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmLlidMismatchEnabled.setStatus(_A)
class _H3cOltPortAlarmLlidMismatchThreshold_Type(Integer32):defaultValue=5000
_H3cOltPortAlarmLlidMismatchThreshold_Type.__name__=_E
_H3cOltPortAlarmLlidMismatchThreshold_Object=MibTableColumn
h3cOltPortAlarmLlidMismatchThreshold=_H3cOltPortAlarmLlidMismatchThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,8),_H3cOltPortAlarmLlidMismatchThreshold_Type())
h3cOltPortAlarmLlidMismatchThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmLlidMismatchThreshold.setStatus(_A)
class _H3cOltPortAlarmRemoteStableEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmRemoteStableEnabled_Type.__name__=_H
_H3cOltPortAlarmRemoteStableEnabled_Object=MibTableColumn
h3cOltPortAlarmRemoteStableEnabled=_H3cOltPortAlarmRemoteStableEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,9),_H3cOltPortAlarmRemoteStableEnabled_Type())
h3cOltPortAlarmRemoteStableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmRemoteStableEnabled.setStatus(_A)
class _H3cOltPortAlarmLocalStableEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmLocalStableEnabled_Type.__name__=_H
_H3cOltPortAlarmLocalStableEnabled_Object=MibTableColumn
h3cOltPortAlarmLocalStableEnabled=_H3cOltPortAlarmLocalStableEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,10),_H3cOltPortAlarmLocalStableEnabled_Type())
h3cOltPortAlarmLocalStableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmLocalStableEnabled.setStatus(_A)
class _H3cOltPortAlarmRegistrationEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmRegistrationEnabled_Type.__name__=_H
_H3cOltPortAlarmRegistrationEnabled_Object=MibTableColumn
h3cOltPortAlarmRegistrationEnabled=_H3cOltPortAlarmRegistrationEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,11),_H3cOltPortAlarmRegistrationEnabled_Type())
h3cOltPortAlarmRegistrationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmRegistrationEnabled.setStatus(_A)
class _H3cOltPortAlarmOamDisconnectionEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmOamDisconnectionEnabled_Type.__name__=_H
_H3cOltPortAlarmOamDisconnectionEnabled_Object=MibTableColumn
h3cOltPortAlarmOamDisconnectionEnabled=_H3cOltPortAlarmOamDisconnectionEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,12),_H3cOltPortAlarmOamDisconnectionEnabled_Type())
h3cOltPortAlarmOamDisconnectionEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmOamDisconnectionEnabled.setStatus(_A)
class _H3cOltPortAlarmEncryptionKeyEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmEncryptionKeyEnabled_Type.__name__=_H
_H3cOltPortAlarmEncryptionKeyEnabled_Object=MibTableColumn
h3cOltPortAlarmEncryptionKeyEnabled=_H3cOltPortAlarmEncryptionKeyEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,13),_H3cOltPortAlarmEncryptionKeyEnabled_Type())
h3cOltPortAlarmEncryptionKeyEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmEncryptionKeyEnabled.setStatus(_A)
class _H3cOltPortAlarmVendorSpecificEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmVendorSpecificEnabled_Type.__name__=_H
_H3cOltPortAlarmVendorSpecificEnabled_Object=MibTableColumn
h3cOltPortAlarmVendorSpecificEnabled=_H3cOltPortAlarmVendorSpecificEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,14),_H3cOltPortAlarmVendorSpecificEnabled_Type())
h3cOltPortAlarmVendorSpecificEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmVendorSpecificEnabled.setStatus(_A)
class _H3cOltPortAlarmRegExcessEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmRegExcessEnabled_Type.__name__=_H
_H3cOltPortAlarmRegExcessEnabled_Object=MibTableColumn
h3cOltPortAlarmRegExcessEnabled=_H3cOltPortAlarmRegExcessEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,15),_H3cOltPortAlarmRegExcessEnabled_Type())
h3cOltPortAlarmRegExcessEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmRegExcessEnabled.setStatus(_A)
class _H3cOltPortAlarmDFEEnabled_Type(TruthValue):defaultValue=1
_H3cOltPortAlarmDFEEnabled_Type.__name__=_H
_H3cOltPortAlarmDFEEnabled_Object=MibTableColumn
h3cOltPortAlarmDFEEnabled=_H3cOltPortAlarmDFEEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,4,1,16),_H3cOltPortAlarmDFEEnabled_Type())
h3cOltPortAlarmDFEEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOltPortAlarmDFEEnabled.setStatus(_A)
_H3cOltLaserOnTimeMinVal_Type=Integer32
_H3cOltLaserOnTimeMinVal_Object=MibScalar
h3cOltLaserOnTimeMinVal=_H3cOltLaserOnTimeMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,5),_H3cOltLaserOnTimeMinVal_Type())
h3cOltLaserOnTimeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltLaserOnTimeMinVal.setStatus(_A)
_H3cOltLaserOnTimeMaxVal_Type=Integer32
_H3cOltLaserOnTimeMaxVal_Object=MibScalar
h3cOltLaserOnTimeMaxVal=_H3cOltLaserOnTimeMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,6),_H3cOltLaserOnTimeMaxVal_Type())
h3cOltLaserOnTimeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltLaserOnTimeMaxVal.setStatus(_A)
_H3cOltLaserOffTimeMinVal_Type=Integer32
_H3cOltLaserOffTimeMinVal_Object=MibScalar
h3cOltLaserOffTimeMinVal=_H3cOltLaserOffTimeMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,7),_H3cOltLaserOffTimeMinVal_Type())
h3cOltLaserOffTimeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltLaserOffTimeMinVal.setStatus(_A)
_H3cOltLaserOffTimeMaxVal_Type=Integer32
_H3cOltLaserOffTimeMaxVal_Object=MibScalar
h3cOltLaserOffTimeMaxVal=_H3cOltLaserOffTimeMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,8),_H3cOltLaserOffTimeMaxVal_Type())
h3cOltLaserOffTimeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltLaserOffTimeMaxVal.setStatus(_A)
_H3cOltDbaDiscoveryLengthMinVal_Type=Integer32
_H3cOltDbaDiscoveryLengthMinVal_Object=MibScalar
h3cOltDbaDiscoveryLengthMinVal=_H3cOltDbaDiscoveryLengthMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,9),_H3cOltDbaDiscoveryLengthMinVal_Type())
h3cOltDbaDiscoveryLengthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaDiscoveryLengthMinVal.setStatus(_A)
_H3cOltDbaDiscoveryLengthMaxVal_Type=Integer32
_H3cOltDbaDiscoveryLengthMaxVal_Object=MibScalar
h3cOltDbaDiscoveryLengthMaxVal=_H3cOltDbaDiscoveryLengthMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,10),_H3cOltDbaDiscoveryLengthMaxVal_Type())
h3cOltDbaDiscoveryLengthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaDiscoveryLengthMaxVal.setStatus(_A)
_H3cOltDbaDiscovryFrequencyMinVal_Type=Integer32
_H3cOltDbaDiscovryFrequencyMinVal_Object=MibScalar
h3cOltDbaDiscovryFrequencyMinVal=_H3cOltDbaDiscovryFrequencyMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,11),_H3cOltDbaDiscovryFrequencyMinVal_Type())
h3cOltDbaDiscovryFrequencyMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaDiscovryFrequencyMinVal.setStatus(_A)
_H3cOltDbaDiscovryFrequencyMaxVal_Type=Integer32
_H3cOltDbaDiscovryFrequencyMaxVal_Object=MibScalar
h3cOltDbaDiscovryFrequencyMaxVal=_H3cOltDbaDiscovryFrequencyMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,12),_H3cOltDbaDiscovryFrequencyMaxVal_Type())
h3cOltDbaDiscovryFrequencyMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaDiscovryFrequencyMaxVal.setStatus(_A)
_H3cOltDbaCycleLengthMinVal_Type=Integer32
_H3cOltDbaCycleLengthMinVal_Object=MibScalar
h3cOltDbaCycleLengthMinVal=_H3cOltDbaCycleLengthMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,13),_H3cOltDbaCycleLengthMinVal_Type())
h3cOltDbaCycleLengthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaCycleLengthMinVal.setStatus(_A)
_H3cOltDbaCycleLengthMaxVal_Type=Integer32
_H3cOltDbaCycleLengthMaxVal_Object=MibScalar
h3cOltDbaCycleLengthMaxVal=_H3cOltDbaCycleLengthMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,14),_H3cOltDbaCycleLengthMaxVal_Type())
h3cOltDbaCycleLengthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltDbaCycleLengthMaxVal.setStatus(_A)
_H3cOltPortAlarmLlidMisMinVal_Type=Integer32
_H3cOltPortAlarmLlidMisMinVal_Object=MibScalar
h3cOltPortAlarmLlidMisMinVal=_H3cOltPortAlarmLlidMisMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,15),_H3cOltPortAlarmLlidMisMinVal_Type())
h3cOltPortAlarmLlidMisMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltPortAlarmLlidMisMinVal.setStatus(_A)
_H3cOltPortAlarmLlidMisMaxVal_Type=Integer32
_H3cOltPortAlarmLlidMisMaxVal_Object=MibScalar
h3cOltPortAlarmLlidMisMaxVal=_H3cOltPortAlarmLlidMisMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,16),_H3cOltPortAlarmLlidMisMaxVal_Type())
h3cOltPortAlarmLlidMisMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltPortAlarmLlidMisMaxVal.setStatus(_A)
_H3cOltPortAlarmBerMinVal_Type=Integer32
_H3cOltPortAlarmBerMinVal_Object=MibScalar
h3cOltPortAlarmBerMinVal=_H3cOltPortAlarmBerMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,17),_H3cOltPortAlarmBerMinVal_Type())
h3cOltPortAlarmBerMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltPortAlarmBerMinVal.setStatus(_A)
_H3cOltPortAlarmBerMaxVal_Type=Integer32
_H3cOltPortAlarmBerMaxVal_Object=MibScalar
h3cOltPortAlarmBerMaxVal=_H3cOltPortAlarmBerMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,18),_H3cOltPortAlarmBerMaxVal_Type())
h3cOltPortAlarmBerMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltPortAlarmBerMaxVal.setStatus(_A)
_H3cOltPortAlarmFerMinVal_Type=Integer32
_H3cOltPortAlarmFerMinVal_Object=MibScalar
h3cOltPortAlarmFerMinVal=_H3cOltPortAlarmFerMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,19),_H3cOltPortAlarmFerMinVal_Type())
h3cOltPortAlarmFerMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltPortAlarmFerMinVal.setStatus(_A)
_H3cOltPortAlarmFerMaxVal_Type=Integer32
_H3cOltPortAlarmFerMaxVal_Object=MibScalar
h3cOltPortAlarmFerMaxVal=_H3cOltPortAlarmFerMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,20),_H3cOltPortAlarmFerMaxVal_Type())
h3cOltPortAlarmFerMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltPortAlarmFerMaxVal.setStatus(_A)
_H3cOnuSilentTable_Object=MibTable
h3cOnuSilentTable=_H3cOnuSilentTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,21))
if mibBuilder.loadTexts:h3cOnuSilentTable.setStatus(_A)
_H3cOnuSilentEntry_Object=MibTableRow
h3cOnuSilentEntry=_H3cOnuSilentEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,21,1))
h3cOnuSilentEntry.setIndexNames((0,_D,_F),(0,_G,_s))
if mibBuilder.loadTexts:h3cOnuSilentEntry.setStatus(_A)
_H3cOnuSilentMacAddr_Type=MacAddress
_H3cOnuSilentMacAddr_Object=MibTableColumn
h3cOnuSilentMacAddr=_H3cOnuSilentMacAddr_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,21,1,1),_H3cOnuSilentMacAddr_Type())
h3cOnuSilentMacAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuSilentMacAddr.setStatus(_A)
_H3cOnuSilentTime_Type=Integer32
_H3cOnuSilentTime_Object=MibTableColumn
h3cOnuSilentTime=_H3cOnuSilentTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,21,1,2),_H3cOnuSilentTime_Type())
h3cOnuSilentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSilentTime.setStatus(_A)
_H3cOltUsingOnuTable_Object=MibTable
h3cOltUsingOnuTable=_H3cOltUsingOnuTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,22))
if mibBuilder.loadTexts:h3cOltUsingOnuTable.setStatus(_A)
_H3cOltUsingOnuEntry_Object=MibTableRow
h3cOltUsingOnuEntry=_H3cOltUsingOnuEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,22,1))
h3cOltUsingOnuEntry.setIndexNames((0,_D,_F),(0,_G,_t))
if mibBuilder.loadTexts:h3cOltUsingOnuEntry.setStatus(_A)
class _H3cOltUsingOnuNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cOltUsingOnuNum_Type.__name__=_E
_H3cOltUsingOnuNum_Object=MibTableColumn
h3cOltUsingOnuNum=_H3cOltUsingOnuNum_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,22,1,1),_H3cOltUsingOnuNum_Type())
h3cOltUsingOnuNum.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOltUsingOnuNum.setStatus(_A)
_H3cOltUsingOnuIfIndex_Type=Integer32
_H3cOltUsingOnuIfIndex_Object=MibTableColumn
h3cOltUsingOnuIfIndex=_H3cOltUsingOnuIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,22,1,2),_H3cOltUsingOnuIfIndex_Type())
h3cOltUsingOnuIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOltUsingOnuIfIndex.setStatus(_A)
_H3cOltUsingOnuRowStatus_Type=RowStatus
_H3cOltUsingOnuRowStatus_Object=MibTableColumn
h3cOltUsingOnuRowStatus=_H3cOltUsingOnuRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,3,22,1,3),_H3cOltUsingOnuRowStatus_Type())
h3cOltUsingOnuRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOltUsingOnuRowStatus.setStatus(_A)
_H3cEponOnuMan_ObjectIdentity=ObjectIdentity
h3cEponOnuMan=_H3cEponOnuMan_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,5))
_H3cOnuSysManTable_Object=MibTable
h3cOnuSysManTable=_H3cOnuSysManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1))
if mibBuilder.loadTexts:h3cOnuSysManTable.setStatus(_A)
_H3cOnuSysManEntry_Object=MibTableRow
h3cOnuSysManEntry=_H3cOnuSysManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1))
h3cOnuSysManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuSysManEntry.setStatus(_A)
class _H3cOnuEncryptMan_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('downlink',2),('updownlink',3)))
_H3cOnuEncryptMan_Type.__name__=_E
_H3cOnuEncryptMan_Object=MibTableColumn
h3cOnuEncryptMan=_H3cOnuEncryptMan_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,1),_H3cOnuEncryptMan_Type())
h3cOnuEncryptMan.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuEncryptMan.setStatus(_A)
class _H3cOnuReAuthorize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reAuthorize',1))
_H3cOnuReAuthorize_Type.__name__=_E
_H3cOnuReAuthorize_Object=MibTableColumn
h3cOnuReAuthorize=_H3cOnuReAuthorize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,2),_H3cOnuReAuthorize_Type())
h3cOnuReAuthorize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuReAuthorize.setStatus(_A)
class _H3cOnuMulticastFilterStatus_Type(TruthValue):defaultValue=2
_H3cOnuMulticastFilterStatus_Type.__name__=_H
_H3cOnuMulticastFilterStatus_Object=MibTableColumn
h3cOnuMulticastFilterStatus=_H3cOnuMulticastFilterStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,3),_H3cOnuMulticastFilterStatus_Type())
h3cOnuMulticastFilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuMulticastFilterStatus.setStatus(_A)
class _H3cOnuDbaReportQueueSetNumber_Type(Integer32):defaultValue=2
_H3cOnuDbaReportQueueSetNumber_Type.__name__=_E
_H3cOnuDbaReportQueueSetNumber_Object=MibTableColumn
h3cOnuDbaReportQueueSetNumber=_H3cOnuDbaReportQueueSetNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,4),_H3cOnuDbaReportQueueSetNumber_Type())
h3cOnuDbaReportQueueSetNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDbaReportQueueSetNumber.setStatus(_A)
class _H3cOnuRemoteFecStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cOnuRemoteFecStatus_Type.__name__=_E
_H3cOnuRemoteFecStatus_Object=MibTableColumn
h3cOnuRemoteFecStatus=_H3cOnuRemoteFecStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,5),_H3cOnuRemoteFecStatus_Type())
h3cOnuRemoteFecStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuRemoteFecStatus.setStatus(_A)
class _H3cOnuPortBerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cOnuPortBerStatus_Type.__name__=_E
_H3cOnuPortBerStatus_Object=MibTableColumn
h3cOnuPortBerStatus=_H3cOnuPortBerStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,6),_H3cOnuPortBerStatus_Type())
h3cOnuPortBerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuPortBerStatus.setStatus(_A)
class _H3cOnuReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_H3cOnuReset_Type.__name__=_E
_H3cOnuReset_Object=MibTableColumn
h3cOnuReset=_H3cOnuReset_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,7),_H3cOnuReset_Type())
h3cOnuReset.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuReset.setStatus(_A)
class _H3cOnuMulticastControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('igmpsnooping',1),('multicastcontrol',2)))
_H3cOnuMulticastControlMode_Type.__name__=_E
_H3cOnuMulticastControlMode_Object=MibTableColumn
h3cOnuMulticastControlMode=_H3cOnuMulticastControlMode_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,8),_H3cOnuMulticastControlMode_Type())
h3cOnuMulticastControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuMulticastControlMode.setStatus(_A)
_H3cOnuAccessVlan_Type=Integer32
_H3cOnuAccessVlan_Object=MibTableColumn
h3cOnuAccessVlan=_H3cOnuAccessVlan_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,9),_H3cOnuAccessVlan_Type())
h3cOnuAccessVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuAccessVlan.setStatus(_A)
class _H3cOnuEncryptKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cOnuEncryptKey_Type.__name__=_X
_H3cOnuEncryptKey_Object=MibTableColumn
h3cOnuEncryptKey=_H3cOnuEncryptKey_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,10),_H3cOnuEncryptKey_Type())
h3cOnuEncryptKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuEncryptKey.setStatus(_A)
class _H3cOnuUniUpDownTrapStatus_Type(TruthValue):defaultValue=2
_H3cOnuUniUpDownTrapStatus_Type.__name__=_H
_H3cOnuUniUpDownTrapStatus_Object=MibTableColumn
h3cOnuUniUpDownTrapStatus=_H3cOnuUniUpDownTrapStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,11),_H3cOnuUniUpDownTrapStatus_Type())
h3cOnuUniUpDownTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuUniUpDownTrapStatus.setStatus(_A)
class _H3cOnuFecStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cOnuFecStatus_Type.__name__=_E
_H3cOnuFecStatus_Object=MibTableColumn
h3cOnuFecStatus=_H3cOnuFecStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,12),_H3cOnuFecStatus_Type())
h3cOnuFecStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuFecStatus.setStatus(_A)
_H3cOnuMcastCtrlHostAgingTime_Type=Integer32
_H3cOnuMcastCtrlHostAgingTime_Object=MibTableColumn
h3cOnuMcastCtrlHostAgingTime=_H3cOnuMcastCtrlHostAgingTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,13),_H3cOnuMcastCtrlHostAgingTime_Type())
h3cOnuMcastCtrlHostAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuMcastCtrlHostAgingTime.setStatus(_A)
_H3cOnuMulticastFastLeaveEnable_Type=TruthValue
_H3cOnuMulticastFastLeaveEnable_Object=MibTableColumn
h3cOnuMulticastFastLeaveEnable=_H3cOnuMulticastFastLeaveEnable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,14),_H3cOnuMulticastFastLeaveEnable_Type())
h3cOnuMulticastFastLeaveEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuMulticastFastLeaveEnable.setStatus(_A)
_H3cOnuPortIsolateEnable_Type=TruthValue
_H3cOnuPortIsolateEnable_Object=MibTableColumn
h3cOnuPortIsolateEnable=_H3cOnuPortIsolateEnable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,1,1,15),_H3cOnuPortIsolateEnable_Type())
h3cOnuPortIsolateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuPortIsolateEnable.setStatus(_A)
_H3cOnuLinkTestTable_Object=MibTable
h3cOnuLinkTestTable=_H3cOnuLinkTestTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2))
if mibBuilder.loadTexts:h3cOnuLinkTestTable.setStatus(_A)
_H3cOnuLinkTestEntry_Object=MibTableRow
h3cOnuLinkTestEntry=_H3cOnuLinkTestEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1))
h3cOnuLinkTestEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuLinkTestEntry.setStatus(_A)
class _H3cOnuLinkTestFrameNum_Type(Integer32):defaultValue=20
_H3cOnuLinkTestFrameNum_Type.__name__=_E
_H3cOnuLinkTestFrameNum_Object=MibTableColumn
h3cOnuLinkTestFrameNum=_H3cOnuLinkTestFrameNum_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,1),_H3cOnuLinkTestFrameNum_Type())
h3cOnuLinkTestFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuLinkTestFrameNum.setStatus(_A)
class _H3cOnuLinkTestFrameSize_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1514))
_H3cOnuLinkTestFrameSize_Type.__name__=_E
_H3cOnuLinkTestFrameSize_Object=MibTableColumn
h3cOnuLinkTestFrameSize=_H3cOnuLinkTestFrameSize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,2),_H3cOnuLinkTestFrameSize_Type())
h3cOnuLinkTestFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuLinkTestFrameSize.setStatus(_A)
class _H3cOnuLinkTestDelay_Type(TruthValue):defaultValue=1
_H3cOnuLinkTestDelay_Type.__name__=_H
_H3cOnuLinkTestDelay_Object=MibTableColumn
h3cOnuLinkTestDelay=_H3cOnuLinkTestDelay_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,3),_H3cOnuLinkTestDelay_Type())
h3cOnuLinkTestDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuLinkTestDelay.setStatus(_A)
class _H3cOnuLinkTestVlanTag_Type(TruthValue):defaultValue=1
_H3cOnuLinkTestVlanTag_Type.__name__=_H
_H3cOnuLinkTestVlanTag_Object=MibTableColumn
h3cOnuLinkTestVlanTag=_H3cOnuLinkTestVlanTag_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,4),_H3cOnuLinkTestVlanTag_Type())
h3cOnuLinkTestVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuLinkTestVlanTag.setStatus(_A)
class _H3cOnuLinkTestVlanPriority_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cOnuLinkTestVlanPriority_Type.__name__=_E
_H3cOnuLinkTestVlanPriority_Object=MibTableColumn
h3cOnuLinkTestVlanPriority=_H3cOnuLinkTestVlanPriority_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,5),_H3cOnuLinkTestVlanPriority_Type())
h3cOnuLinkTestVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuLinkTestVlanPriority.setStatus(_A)
class _H3cOnuLinkTestVlanTagID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cOnuLinkTestVlanTagID_Type.__name__=_E
_H3cOnuLinkTestVlanTagID_Object=MibTableColumn
h3cOnuLinkTestVlanTagID=_H3cOnuLinkTestVlanTagID_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,6),_H3cOnuLinkTestVlanTagID_Type())
h3cOnuLinkTestVlanTagID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuLinkTestVlanTagID.setStatus(_A)
_H3cOnuLinkTestResultSentFrameNum_Type=Integer32
_H3cOnuLinkTestResultSentFrameNum_Object=MibTableColumn
h3cOnuLinkTestResultSentFrameNum=_H3cOnuLinkTestResultSentFrameNum_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,7),_H3cOnuLinkTestResultSentFrameNum_Type())
h3cOnuLinkTestResultSentFrameNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestResultSentFrameNum.setStatus(_A)
_H3cOnuLinkTestResultRetFrameNum_Type=Integer32
_H3cOnuLinkTestResultRetFrameNum_Object=MibTableColumn
h3cOnuLinkTestResultRetFrameNum=_H3cOnuLinkTestResultRetFrameNum_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,8),_H3cOnuLinkTestResultRetFrameNum_Type())
h3cOnuLinkTestResultRetFrameNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestResultRetFrameNum.setStatus(_A)
_H3cOnuLinkTestResultRetErrFrameNum_Type=Integer32
_H3cOnuLinkTestResultRetErrFrameNum_Object=MibTableColumn
h3cOnuLinkTestResultRetErrFrameNum=_H3cOnuLinkTestResultRetErrFrameNum_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,9),_H3cOnuLinkTestResultRetErrFrameNum_Type())
h3cOnuLinkTestResultRetErrFrameNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestResultRetErrFrameNum.setStatus(_A)
_H3cOnuLinkTestResultMinDelay_Type=Integer32
_H3cOnuLinkTestResultMinDelay_Object=MibTableColumn
h3cOnuLinkTestResultMinDelay=_H3cOnuLinkTestResultMinDelay_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,10),_H3cOnuLinkTestResultMinDelay_Type())
h3cOnuLinkTestResultMinDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestResultMinDelay.setStatus(_A)
_H3cOnuLinkTestResultMeanDelay_Type=Integer32
_H3cOnuLinkTestResultMeanDelay_Object=MibTableColumn
h3cOnuLinkTestResultMeanDelay=_H3cOnuLinkTestResultMeanDelay_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,11),_H3cOnuLinkTestResultMeanDelay_Type())
h3cOnuLinkTestResultMeanDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestResultMeanDelay.setStatus(_A)
_H3cOnuLinkTestResultMaxDelay_Type=Integer32
_H3cOnuLinkTestResultMaxDelay_Object=MibTableColumn
h3cOnuLinkTestResultMaxDelay=_H3cOnuLinkTestResultMaxDelay_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,2,1,12),_H3cOnuLinkTestResultMaxDelay_Type())
h3cOnuLinkTestResultMaxDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestResultMaxDelay.setStatus(_A)
_H3cOnuBandWidthTable_Object=MibTable
h3cOnuBandWidthTable=_H3cOnuBandWidthTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3))
if mibBuilder.loadTexts:h3cOnuBandWidthTable.setStatus(_A)
_H3cOnuBandWidthEntry_Object=MibTableRow
h3cOnuBandWidthEntry=_H3cOnuBandWidthEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1))
h3cOnuBandWidthEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuBandWidthEntry.setStatus(_A)
class _H3cOnuDownStreamBandWidthPolicy_Type(TruthValue):defaultValue=2
_H3cOnuDownStreamBandWidthPolicy_Type.__name__=_H
_H3cOnuDownStreamBandWidthPolicy_Object=MibTableColumn
h3cOnuDownStreamBandWidthPolicy=_H3cOnuDownStreamBandWidthPolicy_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,1),_H3cOnuDownStreamBandWidthPolicy_Type())
h3cOnuDownStreamBandWidthPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDownStreamBandWidthPolicy.setStatus(_A)
class _H3cOnuDownStreamMaxBandWidth_Type(Integer32):defaultValue=1000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_H3cOnuDownStreamMaxBandWidth_Type.__name__=_E
_H3cOnuDownStreamMaxBandWidth_Object=MibTableColumn
h3cOnuDownStreamMaxBandWidth=_H3cOnuDownStreamMaxBandWidth_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,2),_H3cOnuDownStreamMaxBandWidth_Type())
h3cOnuDownStreamMaxBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDownStreamMaxBandWidth.setStatus(_A)
class _H3cOnuDownStreamMaxBurstSize_Type(Integer32):defaultValue=8388480;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388480))
_H3cOnuDownStreamMaxBurstSize_Type.__name__=_E
_H3cOnuDownStreamMaxBurstSize_Object=MibTableColumn
h3cOnuDownStreamMaxBurstSize=_H3cOnuDownStreamMaxBurstSize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,3),_H3cOnuDownStreamMaxBurstSize_Type())
h3cOnuDownStreamMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDownStreamMaxBurstSize.setStatus(_A)
class _H3cOnuDownStreamHighPriorityFirst_Type(TruthValue):defaultValue=2
_H3cOnuDownStreamHighPriorityFirst_Type.__name__=_H
_H3cOnuDownStreamHighPriorityFirst_Object=MibTableColumn
h3cOnuDownStreamHighPriorityFirst=_H3cOnuDownStreamHighPriorityFirst_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,4),_H3cOnuDownStreamHighPriorityFirst_Type())
h3cOnuDownStreamHighPriorityFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDownStreamHighPriorityFirst.setStatus(_A)
class _H3cOnuDownStreamShortFrameFirst_Type(TruthValue):defaultValue=2
_H3cOnuDownStreamShortFrameFirst_Type.__name__=_H
_H3cOnuDownStreamShortFrameFirst_Object=MibTableColumn
h3cOnuDownStreamShortFrameFirst=_H3cOnuDownStreamShortFrameFirst_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,5),_H3cOnuDownStreamShortFrameFirst_Type())
h3cOnuDownStreamShortFrameFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDownStreamShortFrameFirst.setStatus(_A)
class _H3cOnuP2PBandWidthPolicy_Type(TruthValue):defaultValue=2
_H3cOnuP2PBandWidthPolicy_Type.__name__=_H
_H3cOnuP2PBandWidthPolicy_Object=MibTableColumn
h3cOnuP2PBandWidthPolicy=_H3cOnuP2PBandWidthPolicy_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,6),_H3cOnuP2PBandWidthPolicy_Type())
h3cOnuP2PBandWidthPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuP2PBandWidthPolicy.setStatus(_A)
class _H3cOnuP2PMaxBandWidth_Type(Integer32):defaultValue=1000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_H3cOnuP2PMaxBandWidth_Type.__name__=_E
_H3cOnuP2PMaxBandWidth_Object=MibTableColumn
h3cOnuP2PMaxBandWidth=_H3cOnuP2PMaxBandWidth_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,7),_H3cOnuP2PMaxBandWidth_Type())
h3cOnuP2PMaxBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuP2PMaxBandWidth.setStatus(_A)
class _H3cOnuP2PMaxBurstSize_Type(Integer32):defaultValue=8388480;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388480))
_H3cOnuP2PMaxBurstSize_Type.__name__=_E
_H3cOnuP2PMaxBurstSize_Object=MibTableColumn
h3cOnuP2PMaxBurstSize=_H3cOnuP2PMaxBurstSize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,8),_H3cOnuP2PMaxBurstSize_Type())
h3cOnuP2PMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuP2PMaxBurstSize.setStatus(_A)
class _H3cOnuP2PHighPriorityFirst_Type(TruthValue):defaultValue=2
_H3cOnuP2PHighPriorityFirst_Type.__name__=_H
_H3cOnuP2PHighPriorityFirst_Object=MibTableColumn
h3cOnuP2PHighPriorityFirst=_H3cOnuP2PHighPriorityFirst_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,9),_H3cOnuP2PHighPriorityFirst_Type())
h3cOnuP2PHighPriorityFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuP2PHighPriorityFirst.setStatus(_A)
class _H3cOnuP2PShortFrameFirst_Type(TruthValue):defaultValue=2
_H3cOnuP2PShortFrameFirst_Type.__name__=_H
_H3cOnuP2PShortFrameFirst_Object=MibTableColumn
h3cOnuP2PShortFrameFirst=_H3cOnuP2PShortFrameFirst_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,3,1,10),_H3cOnuP2PShortFrameFirst_Type())
h3cOnuP2PShortFrameFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuP2PShortFrameFirst.setStatus(_A)
_H3cOnuSlaManTable_Object=MibTable
h3cOnuSlaManTable=_H3cOnuSlaManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4))
if mibBuilder.loadTexts:h3cOnuSlaManTable.setStatus(_A)
_H3cOnuSlaManEntry_Object=MibTableRow
h3cOnuSlaManEntry=_H3cOnuSlaManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1))
h3cOnuSlaManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuSlaManEntry.setStatus(_A)
_H3cOnuSlaMaxBandWidth_Type=Integer32
_H3cOnuSlaMaxBandWidth_Object=MibTableColumn
h3cOnuSlaMaxBandWidth=_H3cOnuSlaMaxBandWidth_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1,1),_H3cOnuSlaMaxBandWidth_Type())
h3cOnuSlaMaxBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuSlaMaxBandWidth.setStatus(_A)
_H3cOnuSlaMinBandWidth_Type=Integer32
_H3cOnuSlaMinBandWidth_Object=MibTableColumn
h3cOnuSlaMinBandWidth=_H3cOnuSlaMinBandWidth_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1,2),_H3cOnuSlaMinBandWidth_Type())
h3cOnuSlaMinBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuSlaMinBandWidth.setStatus(_A)
_H3cOnuSlaBandWidthStepVal_Type=Integer32
_H3cOnuSlaBandWidthStepVal_Object=MibTableColumn
h3cOnuSlaBandWidthStepVal=_H3cOnuSlaBandWidthStepVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1,3),_H3cOnuSlaBandWidthStepVal_Type())
h3cOnuSlaBandWidthStepVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSlaBandWidthStepVal.setStatus(_A)
class _H3cOnuSlaDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_H3cOnuSlaDelay_Type.__name__=_E
_H3cOnuSlaDelay_Object=MibTableColumn
h3cOnuSlaDelay=_H3cOnuSlaDelay_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1,4),_H3cOnuSlaDelay_Type())
h3cOnuSlaDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuSlaDelay.setStatus(_A)
_H3cOnuSlaFixedBandWidth_Type=Integer32
_H3cOnuSlaFixedBandWidth_Object=MibTableColumn
h3cOnuSlaFixedBandWidth=_H3cOnuSlaFixedBandWidth_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1,5),_H3cOnuSlaFixedBandWidth_Type())
h3cOnuSlaFixedBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuSlaFixedBandWidth.setStatus(_A)
class _H3cOnuSlaPriorityClass_Type(Integer32):defaultValue=0
_H3cOnuSlaPriorityClass_Type.__name__=_E
_H3cOnuSlaPriorityClass_Object=MibTableColumn
h3cOnuSlaPriorityClass=_H3cOnuSlaPriorityClass_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1,6),_H3cOnuSlaPriorityClass_Type())
h3cOnuSlaPriorityClass.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuSlaPriorityClass.setStatus(_A)
_H3cOnuSlaFixedPacketSize_Type=Integer32
_H3cOnuSlaFixedPacketSize_Object=MibTableColumn
h3cOnuSlaFixedPacketSize=_H3cOnuSlaFixedPacketSize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,4,1,7),_H3cOnuSlaFixedPacketSize_Type())
h3cOnuSlaFixedPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuSlaFixedPacketSize.setStatus(_A)
_H3cOnuInfoTable_Object=MibTable
h3cOnuInfoTable=_H3cOnuInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5))
if mibBuilder.loadTexts:h3cOnuInfoTable.setStatus(_A)
_H3cOnuInfoEntry_Object=MibTableRow
h3cOnuInfoEntry=_H3cOnuInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1))
h3cOnuInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuInfoEntry.setStatus(_A)
_H3cOnuHardMajorVersion_Type=OctetString
_H3cOnuHardMajorVersion_Object=MibTableColumn
h3cOnuHardMajorVersion=_H3cOnuHardMajorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,1),_H3cOnuHardMajorVersion_Type())
h3cOnuHardMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuHardMajorVersion.setStatus(_A)
_H3cOnuHardMinorVersion_Type=OctetString
_H3cOnuHardMinorVersion_Object=MibTableColumn
h3cOnuHardMinorVersion=_H3cOnuHardMinorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,2),_H3cOnuHardMinorVersion_Type())
h3cOnuHardMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuHardMinorVersion.setStatus(_A)
_H3cOnuSoftwareVersion_Type=OctetString
_H3cOnuSoftwareVersion_Object=MibTableColumn
h3cOnuSoftwareVersion=_H3cOnuSoftwareVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,3),_H3cOnuSoftwareVersion_Type())
h3cOnuSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSoftwareVersion.setStatus(_A)
class _H3cOnuUniMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('mii',2),('gmii',3),('tbi',4)))
_H3cOnuUniMacType_Type.__name__=_E
_H3cOnuUniMacType_Object=MibTableColumn
h3cOnuUniMacType=_H3cOnuUniMacType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,4),_H3cOnuUniMacType_Type())
h3cOnuUniMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuUniMacType.setStatus(_A)
_H3cOnuLaserOnTime_Type=Integer32
_H3cOnuLaserOnTime_Object=MibTableColumn
h3cOnuLaserOnTime=_H3cOnuLaserOnTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,5),_H3cOnuLaserOnTime_Type())
h3cOnuLaserOnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLaserOnTime.setStatus(_A)
_H3cOnuLaserOffTime_Type=Integer32
_H3cOnuLaserOffTime_Object=MibTableColumn
h3cOnuLaserOffTime=_H3cOnuLaserOffTime_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,6),_H3cOnuLaserOffTime_Type())
h3cOnuLaserOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLaserOffTime.setStatus(_A)
class _H3cOnuGrantFifoDep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255),ValueRangeConstraint(2147483647,2147483647))
_H3cOnuGrantFifoDep_Type.__name__=_E
_H3cOnuGrantFifoDep_Object=MibTableColumn
h3cOnuGrantFifoDep=_H3cOnuGrantFifoDep_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,7),_H3cOnuGrantFifoDep_Type())
h3cOnuGrantFifoDep.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuGrantFifoDep.setStatus(_A)
class _H3cOnuWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('on',2),('pending',3),('off',4)))
_H3cOnuWorkMode_Type.__name__=_E
_H3cOnuWorkMode_Object=MibTableColumn
h3cOnuWorkMode=_H3cOnuWorkMode_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,8),_H3cOnuWorkMode_Type())
h3cOnuWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuWorkMode.setStatus(_A)
_H3cOnuPCBVersion_Type=OctetString
_H3cOnuPCBVersion_Object=MibTableColumn
h3cOnuPCBVersion=_H3cOnuPCBVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,9),_H3cOnuPCBVersion_Type())
h3cOnuPCBVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPCBVersion.setStatus(_A)
_H3cOnuRtt_Type=Unsigned32
_H3cOnuRtt_Object=MibTableColumn
h3cOnuRtt=_H3cOnuRtt_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,10),_H3cOnuRtt_Type())
h3cOnuRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRtt.setStatus(_A)
_H3cOnuEEPROMVersion_Type=OctetString
_H3cOnuEEPROMVersion_Object=MibTableColumn
h3cOnuEEPROMVersion=_H3cOnuEEPROMVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,11),_H3cOnuEEPROMVersion_Type())
h3cOnuEEPROMVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuEEPROMVersion.setStatus(_A)
_H3cOnuRegType_Type=OctetString
_H3cOnuRegType_Object=MibTableColumn
h3cOnuRegType=_H3cOnuRegType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,12),_H3cOnuRegType_Type())
h3cOnuRegType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRegType.setStatus(_A)
_H3cOnuHostType_Type=OctetString
_H3cOnuHostType_Object=MibTableColumn
h3cOnuHostType=_H3cOnuHostType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,13),_H3cOnuHostType_Type())
h3cOnuHostType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuHostType.setStatus(_A)
_H3cOnuDistance_Type=Integer32
_H3cOnuDistance_Object=MibTableColumn
h3cOnuDistance=_H3cOnuDistance_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,14),_H3cOnuDistance_Type())
h3cOnuDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuDistance.setStatus(_A)
_H3cOnuLlid_Type=Integer32
_H3cOnuLlid_Object=MibTableColumn
h3cOnuLlid=_H3cOnuLlid_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,15),_H3cOnuLlid_Type())
h3cOnuLlid.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLlid.setStatus(_A)
_H3cOnuVendorId_Type=OctetString
_H3cOnuVendorId_Object=MibTableColumn
h3cOnuVendorId=_H3cOnuVendorId_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,16),_H3cOnuVendorId_Type())
h3cOnuVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuVendorId.setStatus(_A)
_H3cOnuFirmwareVersion_Type=OctetString
_H3cOnuFirmwareVersion_Object=MibTableColumn
h3cOnuFirmwareVersion=_H3cOnuFirmwareVersion_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,17),_H3cOnuFirmwareVersion_Type())
h3cOnuFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuFirmwareVersion.setStatus(_A)
_H3cOnuOpticalPowerReceivedByOlt_Type=Integer32
_H3cOnuOpticalPowerReceivedByOlt_Object=MibTableColumn
h3cOnuOpticalPowerReceivedByOlt=_H3cOnuOpticalPowerReceivedByOlt_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,5,1,18),_H3cOnuOpticalPowerReceivedByOlt_Type())
h3cOnuOpticalPowerReceivedByOlt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuOpticalPowerReceivedByOlt.setStatus(_A)
_H3cOnuMacAddrInfoTable_Object=MibTable
h3cOnuMacAddrInfoTable=_H3cOnuMacAddrInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,6))
if mibBuilder.loadTexts:h3cOnuMacAddrInfoTable.setStatus(_A)
_H3cOnuMacAddrInfoEntry_Object=MibTableRow
h3cOnuMacAddrInfoEntry=_H3cOnuMacAddrInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,6,1))
h3cOnuMacAddrInfoEntry.setIndexNames((0,_D,_F),(0,_G,_u))
if mibBuilder.loadTexts:h3cOnuMacAddrInfoEntry.setStatus(_A)
_H3cOnuMacIndex_Type=Integer32
_H3cOnuMacIndex_Object=MibTableColumn
h3cOnuMacIndex=_H3cOnuMacIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,6,1,1),_H3cOnuMacIndex_Type())
h3cOnuMacIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuMacIndex.setStatus(_A)
class _H3cOnuMacAddrFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bound',1),('registered',2),('run',3),('regIncorrect',4)))
_H3cOnuMacAddrFlag_Type.__name__=_E
_H3cOnuMacAddrFlag_Object=MibTableColumn
h3cOnuMacAddrFlag=_H3cOnuMacAddrFlag_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,6,1,2),_H3cOnuMacAddrFlag_Type())
h3cOnuMacAddrFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuMacAddrFlag.setStatus(_A)
_H3cOnuMacAddress_Type=MacAddress
_H3cOnuMacAddress_Object=MibTableColumn
h3cOnuMacAddress=_H3cOnuMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,6,1,3),_H3cOnuMacAddress_Type())
h3cOnuMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuMacAddress.setStatus(_A)
_H3cOnuBindMacAddrTable_Object=MibTable
h3cOnuBindMacAddrTable=_H3cOnuBindMacAddrTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,7))
if mibBuilder.loadTexts:h3cOnuBindMacAddrTable.setStatus(_A)
_H3cOnuBindMacAddrEntry_Object=MibTableRow
h3cOnuBindMacAddrEntry=_H3cOnuBindMacAddrEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,7,1))
h3cOnuBindMacAddrEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuBindMacAddrEntry.setStatus(_A)
_H3cOnuBindMacAddress_Type=MacAddress
_H3cOnuBindMacAddress_Object=MibTableColumn
h3cOnuBindMacAddress=_H3cOnuBindMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,7,1,1),_H3cOnuBindMacAddress_Type())
h3cOnuBindMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuBindMacAddress.setStatus(_A)
_H3cOnuBindType_Type=Integer32
_H3cOnuBindType_Object=MibTableColumn
h3cOnuBindType=_H3cOnuBindType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,7,1,2),_H3cOnuBindType_Type())
h3cOnuBindType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuBindType.setStatus(_A)
_H3cOnuFirmwareUpdateTable_Object=MibTable
h3cOnuFirmwareUpdateTable=_H3cOnuFirmwareUpdateTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,8))
if mibBuilder.loadTexts:h3cOnuFirmwareUpdateTable.setStatus(_A)
_H3cOnuFirmwareUpdateEntry_Object=MibTableRow
h3cOnuFirmwareUpdateEntry=_H3cOnuFirmwareUpdateEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,8,1))
h3cOnuFirmwareUpdateEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuFirmwareUpdateEntry.setStatus(_A)
class _H3cOnuUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_p,1))
_H3cOnuUpdate_Type.__name__=_E
_H3cOnuUpdate_Object=MibTableColumn
h3cOnuUpdate=_H3cOnuUpdate_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,8,1,1),_H3cOnuUpdate_Type())
h3cOnuUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuUpdate.setStatus(_A)
class _H3cOnuUpdateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('updating',1),('ok',2),(_Y,3),(_q,4),(_r,5),('fileNotMatchONU',6),('timeout',7),('otherError',8)))
_H3cOnuUpdateResult_Type.__name__=_E
_H3cOnuUpdateResult_Object=MibTableColumn
h3cOnuUpdateResult=_H3cOnuUpdateResult_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,8,1,2),_H3cOnuUpdateResult_Type())
h3cOnuUpdateResult.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuUpdateResult.setStatus(_A)
class _H3cOnuUpdateFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cOnuUpdateFileName_Type.__name__=_L
_H3cOnuUpdateFileName_Object=MibTableColumn
h3cOnuUpdateFileName=_H3cOnuUpdateFileName_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,8,1,3),_H3cOnuUpdateFileName_Type())
h3cOnuUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuUpdateFileName.setStatus(_A)
_H3cOnuLinkTestFrameNumMinVal_Type=Integer32
_H3cOnuLinkTestFrameNumMinVal_Object=MibScalar
h3cOnuLinkTestFrameNumMinVal=_H3cOnuLinkTestFrameNumMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,9),_H3cOnuLinkTestFrameNumMinVal_Type())
h3cOnuLinkTestFrameNumMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestFrameNumMinVal.setStatus(_A)
_H3cOnuLinkTestFrameNumMaxVal_Type=Integer32
_H3cOnuLinkTestFrameNumMaxVal_Object=MibScalar
h3cOnuLinkTestFrameNumMaxVal=_H3cOnuLinkTestFrameNumMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,10),_H3cOnuLinkTestFrameNumMaxVal_Type())
h3cOnuLinkTestFrameNumMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuLinkTestFrameNumMaxVal.setStatus(_A)
_H3cOnuSlaMaxBandWidthMinVal_Type=Integer32
_H3cOnuSlaMaxBandWidthMinVal_Object=MibScalar
h3cOnuSlaMaxBandWidthMinVal=_H3cOnuSlaMaxBandWidthMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,11),_H3cOnuSlaMaxBandWidthMinVal_Type())
h3cOnuSlaMaxBandWidthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSlaMaxBandWidthMinVal.setStatus(_A)
_H3cOnuSlaMaxBandWidthMaxVal_Type=Integer32
_H3cOnuSlaMaxBandWidthMaxVal_Object=MibScalar
h3cOnuSlaMaxBandWidthMaxVal=_H3cOnuSlaMaxBandWidthMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,12),_H3cOnuSlaMaxBandWidthMaxVal_Type())
h3cOnuSlaMaxBandWidthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSlaMaxBandWidthMaxVal.setStatus(_A)
_H3cOnuSlaMinBandWidthMinVal_Type=Integer32
_H3cOnuSlaMinBandWidthMinVal_Object=MibScalar
h3cOnuSlaMinBandWidthMinVal=_H3cOnuSlaMinBandWidthMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,13),_H3cOnuSlaMinBandWidthMinVal_Type())
h3cOnuSlaMinBandWidthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSlaMinBandWidthMinVal.setStatus(_A)
_H3cOnuSlaMinBandWidthMaxVal_Type=Integer32
_H3cOnuSlaMinBandWidthMaxVal_Object=MibScalar
h3cOnuSlaMinBandWidthMaxVal=_H3cOnuSlaMinBandWidthMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,14),_H3cOnuSlaMinBandWidthMaxVal_Type())
h3cOnuSlaMinBandWidthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSlaMinBandWidthMaxVal.setStatus(_A)
_H3cEponOnuTypeManTable_Object=MibTable
h3cEponOnuTypeManTable=_H3cEponOnuTypeManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,15))
if mibBuilder.loadTexts:h3cEponOnuTypeManTable.setStatus(_A)
_H3cEponOnuTypeManEntry_Object=MibTableRow
h3cEponOnuTypeManEntry=_H3cEponOnuTypeManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,15,1))
h3cEponOnuTypeManEntry.setIndexNames((0,_G,_v))
if mibBuilder.loadTexts:h3cEponOnuTypeManEntry.setStatus(_A)
_H3cEponOnuTypeIndex_Type=Integer32
_H3cEponOnuTypeIndex_Object=MibTableColumn
h3cEponOnuTypeIndex=_H3cEponOnuTypeIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,15,1,1),_H3cEponOnuTypeIndex_Type())
h3cEponOnuTypeIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEponOnuTypeIndex.setStatus(_A)
_H3cEponOnuTypeDescr_Type=OctetString
_H3cEponOnuTypeDescr_Object=MibTableColumn
h3cEponOnuTypeDescr=_H3cEponOnuTypeDescr_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,15,1,2),_H3cEponOnuTypeDescr_Type())
h3cEponOnuTypeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponOnuTypeDescr.setStatus(_A)
_H3cOnuPacketManTable_Object=MibTable
h3cOnuPacketManTable=_H3cOnuPacketManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,16))
if mibBuilder.loadTexts:h3cOnuPacketManTable.setStatus(_A)
_H3cOnuPacketManEntry_Object=MibTableRow
h3cOnuPacketManEntry=_H3cOnuPacketManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,16,1))
h3cOnuPacketManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuPacketManEntry.setStatus(_A)
class _H3cOnuPriorityTrust_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dscp',1),('ipprecedence',2),('cos',3)))
_H3cOnuPriorityTrust_Type.__name__=_E
_H3cOnuPriorityTrust_Object=MibTableColumn
h3cOnuPriorityTrust=_H3cOnuPriorityTrust_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,16,1,1),_H3cOnuPriorityTrust_Type())
h3cOnuPriorityTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuPriorityTrust.setStatus(_A)
class _H3cOnuQueueScheduler_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('spq',1),('wfq',2)))
_H3cOnuQueueScheduler_Type.__name__=_E
_H3cOnuQueueScheduler_Object=MibTableColumn
h3cOnuQueueScheduler=_H3cOnuQueueScheduler_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,16,1,2),_H3cOnuQueueScheduler_Type())
h3cOnuQueueScheduler.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuQueueScheduler.setStatus(_A)
_H3cOnuProtocolTable_Object=MibTable
h3cOnuProtocolTable=_H3cOnuProtocolTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17))
if mibBuilder.loadTexts:h3cOnuProtocolTable.setStatus(_A)
_H3cOnuProtocolEntry_Object=MibTableRow
h3cOnuProtocolEntry=_H3cOnuProtocolEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1))
h3cOnuProtocolEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuProtocolEntry.setStatus(_A)
class _H3cOnuStpStatus_Type(TruthValue):defaultValue=1
_H3cOnuStpStatus_Type.__name__=_H
_H3cOnuStpStatus_Object=MibTableColumn
h3cOnuStpStatus=_H3cOnuStpStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,1),_H3cOnuStpStatus_Type())
h3cOnuStpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuStpStatus.setStatus(_A)
class _H3cOnuIgmpSnoopingStatus_Type(TruthValue):defaultValue=1
_H3cOnuIgmpSnoopingStatus_Type.__name__=_H
_H3cOnuIgmpSnoopingStatus_Object=MibTableColumn
h3cOnuIgmpSnoopingStatus=_H3cOnuIgmpSnoopingStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,2),_H3cOnuIgmpSnoopingStatus_Type())
h3cOnuIgmpSnoopingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIgmpSnoopingStatus.setStatus(_A)
class _H3cOnuDhcpsnoopingOption82_Type(TruthValue):defaultValue=2
_H3cOnuDhcpsnoopingOption82_Type.__name__=_H
_H3cOnuDhcpsnoopingOption82_Object=MibTableColumn
h3cOnuDhcpsnoopingOption82=_H3cOnuDhcpsnoopingOption82_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,3),_H3cOnuDhcpsnoopingOption82_Type())
h3cOnuDhcpsnoopingOption82.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDhcpsnoopingOption82.setStatus(_A)
class _H3cOnuDhcpsnooping_Type(TruthValue):defaultValue=2
_H3cOnuDhcpsnooping_Type.__name__=_H
_H3cOnuDhcpsnooping_Object=MibTableColumn
h3cOnuDhcpsnooping=_H3cOnuDhcpsnooping_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,4),_H3cOnuDhcpsnooping_Type())
h3cOnuDhcpsnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDhcpsnooping.setStatus(_A)
class _H3cOnuPppoe_Type(TruthValue):defaultValue=2
_H3cOnuPppoe_Type.__name__=_H
_H3cOnuPppoe_Object=MibTableColumn
h3cOnuPppoe=_H3cOnuPppoe_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,5),_H3cOnuPppoe_Type())
h3cOnuPppoe.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuPppoe.setStatus(_A)
_H3cOnuIgmpSnoopingHostAgingT_Type=Integer32
_H3cOnuIgmpSnoopingHostAgingT_Object=MibTableColumn
h3cOnuIgmpSnoopingHostAgingT=_H3cOnuIgmpSnoopingHostAgingT_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,6),_H3cOnuIgmpSnoopingHostAgingT_Type())
h3cOnuIgmpSnoopingHostAgingT.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIgmpSnoopingHostAgingT.setStatus(_A)
_H3cOnuIgmpSnoopingMaxRespT_Type=Integer32
_H3cOnuIgmpSnoopingMaxRespT_Object=MibTableColumn
h3cOnuIgmpSnoopingMaxRespT=_H3cOnuIgmpSnoopingMaxRespT_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,7),_H3cOnuIgmpSnoopingMaxRespT_Type())
h3cOnuIgmpSnoopingMaxRespT.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIgmpSnoopingMaxRespT.setStatus(_A)
_H3cOnuIgmpSnoopingRouterAgingT_Type=Integer32
_H3cOnuIgmpSnoopingRouterAgingT_Object=MibTableColumn
h3cOnuIgmpSnoopingRouterAgingT=_H3cOnuIgmpSnoopingRouterAgingT_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,8),_H3cOnuIgmpSnoopingRouterAgingT_Type())
h3cOnuIgmpSnoopingRouterAgingT.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIgmpSnoopingRouterAgingT.setStatus(_A)
class _H3cOnuIgmpSnoopingAggReportS_Type(TruthValue):defaultValue=2
_H3cOnuIgmpSnoopingAggReportS_Type.__name__=_H
_H3cOnuIgmpSnoopingAggReportS_Object=MibTableColumn
h3cOnuIgmpSnoopingAggReportS=_H3cOnuIgmpSnoopingAggReportS_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,9),_H3cOnuIgmpSnoopingAggReportS_Type())
h3cOnuIgmpSnoopingAggReportS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIgmpSnoopingAggReportS.setStatus(_A)
class _H3cOnuIgmpSnoopingAggLeaveS_Type(TruthValue):defaultValue=1
_H3cOnuIgmpSnoopingAggLeaveS_Type.__name__=_H
_H3cOnuIgmpSnoopingAggLeaveS_Object=MibTableColumn
h3cOnuIgmpSnoopingAggLeaveS=_H3cOnuIgmpSnoopingAggLeaveS_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,17,1,10),_H3cOnuIgmpSnoopingAggLeaveS_Type())
h3cOnuIgmpSnoopingAggLeaveS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIgmpSnoopingAggLeaveS.setStatus(_A)
_H3cOnuDot1xTable_Object=MibTable
h3cOnuDot1xTable=_H3cOnuDot1xTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,18))
if mibBuilder.loadTexts:h3cOnuDot1xTable.setStatus(_A)
_H3cOnuDot1xEntry_Object=MibTableRow
h3cOnuDot1xEntry=_H3cOnuDot1xEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,18,1))
h3cOnuDot1xEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuDot1xEntry.setStatus(_A)
_H3cOnuDot1xAccount_Type=OctetString
_H3cOnuDot1xAccount_Object=MibTableColumn
h3cOnuDot1xAccount=_H3cOnuDot1xAccount_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,18,1,1),_H3cOnuDot1xAccount_Type())
h3cOnuDot1xAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDot1xAccount.setStatus(_A)
_H3cOnuDot1xPassword_Type=OctetString
_H3cOnuDot1xPassword_Object=MibTableColumn
h3cOnuDot1xPassword=_H3cOnuDot1xPassword_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,18,1,2),_H3cOnuDot1xPassword_Type())
h3cOnuDot1xPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDot1xPassword.setStatus(_A)
_H3cOnuPriorityQueueTable_Object=MibTable
h3cOnuPriorityQueueTable=_H3cOnuPriorityQueueTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,19))
if mibBuilder.loadTexts:h3cOnuPriorityQueueTable.setStatus(_A)
_H3cOnuPriorityQueueEntry_Object=MibTableRow
h3cOnuPriorityQueueEntry=_H3cOnuPriorityQueueEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,19,1))
h3cOnuPriorityQueueEntry.setIndexNames((0,_D,_F),(0,_G,_Z),(0,_G,_a))
if mibBuilder.loadTexts:h3cOnuPriorityQueueEntry.setStatus(_A)
class _H3cOnuQueueDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_H3cOnuQueueDirection_Type.__name__=_E
_H3cOnuQueueDirection_Object=MibTableColumn
h3cOnuQueueDirection=_H3cOnuQueueDirection_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,19,1,1),_H3cOnuQueueDirection_Type())
h3cOnuQueueDirection.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuQueueDirection.setStatus(_A)
class _H3cOnuQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cOnuQueueId_Type.__name__=_E
_H3cOnuQueueId_Object=MibTableColumn
h3cOnuQueueId=_H3cOnuQueueId_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,19,1,2),_H3cOnuQueueId_Type())
h3cOnuQueueId.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuQueueId.setStatus(_A)
_H3cOnuQueueSize_Type=Integer32
_H3cOnuQueueSize_Object=MibTableColumn
h3cOnuQueueSize=_H3cOnuQueueSize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,19,1,3),_H3cOnuQueueSize_Type())
h3cOnuQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuQueueSize.setStatus(_A)
_H3cOnuCountTable_Object=MibTable
h3cOnuCountTable=_H3cOnuCountTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,20))
if mibBuilder.loadTexts:h3cOnuCountTable.setStatus(_A)
_H3cOnuCountEntry_Object=MibTableRow
h3cOnuCountEntry=_H3cOnuCountEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,20,1))
h3cOnuCountEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuCountEntry.setStatus(_A)
_H3cOnuInCRCErrPkts_Type=Counter64
_H3cOnuInCRCErrPkts_Object=MibTableColumn
h3cOnuInCRCErrPkts=_H3cOnuInCRCErrPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,20,1,1),_H3cOnuInCRCErrPkts_Type())
h3cOnuInCRCErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuInCRCErrPkts.setStatus(_A)
_H3cOnuOutDroppedFrames_Type=Counter64
_H3cOnuOutDroppedFrames_Object=MibTableColumn
h3cOnuOutDroppedFrames=_H3cOnuOutDroppedFrames_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,20,1,2),_H3cOnuOutDroppedFrames_Type())
h3cOnuOutDroppedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuOutDroppedFrames.setStatus(_A)
_H3cEponOnuScalarGroup_ObjectIdentity=ObjectIdentity
h3cEponOnuScalarGroup=_H3cEponOnuScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21))
_H3cOnuPriorityQueueSizeMinVal_Type=Integer32
_H3cOnuPriorityQueueSizeMinVal_Object=MibScalar
h3cOnuPriorityQueueSizeMinVal=_H3cOnuPriorityQueueSizeMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21,1),_H3cOnuPriorityQueueSizeMinVal_Type())
h3cOnuPriorityQueueSizeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPriorityQueueSizeMinVal.setStatus(_A)
_H3cOnuPriorityQueueSizeMaxVal_Type=Integer32
_H3cOnuPriorityQueueSizeMaxVal_Object=MibScalar
h3cOnuPriorityQueueSizeMaxVal=_H3cOnuPriorityQueueSizeMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21,2),_H3cOnuPriorityQueueSizeMaxVal_Type())
h3cOnuPriorityQueueSizeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPriorityQueueSizeMaxVal.setStatus(_A)
_H3cOnuPriorityQueueBandwidthMinVal_Type=Integer32
_H3cOnuPriorityQueueBandwidthMinVal_Object=MibScalar
h3cOnuPriorityQueueBandwidthMinVal=_H3cOnuPriorityQueueBandwidthMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21,3),_H3cOnuPriorityQueueBandwidthMinVal_Type())
h3cOnuPriorityQueueBandwidthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPriorityQueueBandwidthMinVal.setStatus(_A)
_H3cOnuPriorityQueueBandwidthMaxVal_Type=Integer32
_H3cOnuPriorityQueueBandwidthMaxVal_Object=MibScalar
h3cOnuPriorityQueueBandwidthMaxVal=_H3cOnuPriorityQueueBandwidthMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21,4),_H3cOnuPriorityQueueBandwidthMaxVal_Type())
h3cOnuPriorityQueueBandwidthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPriorityQueueBandwidthMaxVal.setStatus(_A)
_H3cOnuPriorityQueueBurstsizeMinVal_Type=Integer32
_H3cOnuPriorityQueueBurstsizeMinVal_Object=MibScalar
h3cOnuPriorityQueueBurstsizeMinVal=_H3cOnuPriorityQueueBurstsizeMinVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21,5),_H3cOnuPriorityQueueBurstsizeMinVal_Type())
h3cOnuPriorityQueueBurstsizeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPriorityQueueBurstsizeMinVal.setStatus(_A)
_H3cOnuPriorityQueueBurstsizeMaxVal_Type=Integer32
_H3cOnuPriorityQueueBurstsizeMaxVal_Object=MibScalar
h3cOnuPriorityQueueBurstsizeMaxVal=_H3cOnuPriorityQueueBurstsizeMaxVal_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21,6),_H3cOnuPriorityQueueBurstsizeMaxVal_Type())
h3cOnuPriorityQueueBurstsizeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPriorityQueueBurstsizeMaxVal.setStatus(_A)
_H3cOnuUpdateByTypeNextIndex_Type=Integer32
_H3cOnuUpdateByTypeNextIndex_Object=MibScalar
h3cOnuUpdateByTypeNextIndex=_H3cOnuUpdateByTypeNextIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,21,7),_H3cOnuUpdateByTypeNextIndex_Type())
h3cOnuUpdateByTypeNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuUpdateByTypeNextIndex.setStatus(_A)
_H3cOnuQueueBandwidthTable_Object=MibTable
h3cOnuQueueBandwidthTable=_H3cOnuQueueBandwidthTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,22))
if mibBuilder.loadTexts:h3cOnuQueueBandwidthTable.setStatus(_A)
_H3cOnuQueueBandwidthEntry_Object=MibTableRow
h3cOnuQueueBandwidthEntry=_H3cOnuQueueBandwidthEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,22,1))
h3cOnuQueueBandwidthEntry.setIndexNames((0,_D,_F),(0,_G,_Z),(0,_G,_a))
if mibBuilder.loadTexts:h3cOnuQueueBandwidthEntry.setStatus(_A)
_H3cOnuQueueMaxBandwidth_Type=Integer32
_H3cOnuQueueMaxBandwidth_Object=MibTableColumn
h3cOnuQueueMaxBandwidth=_H3cOnuQueueMaxBandwidth_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,22,1,1),_H3cOnuQueueMaxBandwidth_Type())
h3cOnuQueueMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuQueueMaxBandwidth.setStatus(_A)
_H3cOnuQueueMaxBurstsize_Type=Integer32
_H3cOnuQueueMaxBurstsize_Object=MibTableColumn
h3cOnuQueueMaxBurstsize=_H3cOnuQueueMaxBurstsize_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,22,1,2),_H3cOnuQueueMaxBurstsize_Type())
h3cOnuQueueMaxBurstsize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuQueueMaxBurstsize.setStatus(_A)
_H3cOnuQueuePolicyStatus_Type=TruthValue
_H3cOnuQueuePolicyStatus_Object=MibTableColumn
h3cOnuQueuePolicyStatus=_H3cOnuQueuePolicyStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,22,1,3),_H3cOnuQueuePolicyStatus_Type())
h3cOnuQueuePolicyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuQueuePolicyStatus.setStatus(_A)
_H3cOnuIpAddressTable_Object=MibTable
h3cOnuIpAddressTable=_H3cOnuIpAddressTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23))
if mibBuilder.loadTexts:h3cOnuIpAddressTable.setStatus(_A)
_H3cOnuIpAddressEntry_Object=MibTableRow
h3cOnuIpAddressEntry=_H3cOnuIpAddressEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23,1))
h3cOnuIpAddressEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuIpAddressEntry.setStatus(_A)
_H3cOnuIpAddress_Type=IpAddress
_H3cOnuIpAddress_Object=MibTableColumn
h3cOnuIpAddress=_H3cOnuIpAddress_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23,1,1),_H3cOnuIpAddress_Type())
h3cOnuIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIpAddress.setStatus(_A)
_H3cOnuIpAddressMask_Type=IpAddress
_H3cOnuIpAddressMask_Object=MibTableColumn
h3cOnuIpAddressMask=_H3cOnuIpAddressMask_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23,1,2),_H3cOnuIpAddressMask_Type())
h3cOnuIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIpAddressMask.setStatus(_A)
_H3cOnuIpAddressGateway_Type=IpAddress
_H3cOnuIpAddressGateway_Object=MibTableColumn
h3cOnuIpAddressGateway=_H3cOnuIpAddressGateway_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23,1,3),_H3cOnuIpAddressGateway_Type())
h3cOnuIpAddressGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuIpAddressGateway.setStatus(_A)
_H3cOnuDhcpallocate_Type=TruthValue
_H3cOnuDhcpallocate_Object=MibTableColumn
h3cOnuDhcpallocate=_H3cOnuDhcpallocate_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23,1,4),_H3cOnuDhcpallocate_Type())
h3cOnuDhcpallocate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDhcpallocate.setStatus(_A)
_H3cOnuManageVID_Type=Integer32
_H3cOnuManageVID_Object=MibTableColumn
h3cOnuManageVID=_H3cOnuManageVID_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23,1,5),_H3cOnuManageVID_Type())
h3cOnuManageVID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuManageVID.setStatus(_A)
_H3cOnuManageVlanIntfS_Type=TruthValue
_H3cOnuManageVlanIntfS_Object=MibTableColumn
h3cOnuManageVlanIntfS=_H3cOnuManageVlanIntfS_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,23,1,6),_H3cOnuManageVlanIntfS_Type())
h3cOnuManageVlanIntfS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuManageVlanIntfS.setStatus(_A)
_H3cOnuChipSetInfoTable_Object=MibTable
h3cOnuChipSetInfoTable=_H3cOnuChipSetInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,24))
if mibBuilder.loadTexts:h3cOnuChipSetInfoTable.setStatus(_A)
_H3cOnuChipSetInfoEntry_Object=MibTableRow
h3cOnuChipSetInfoEntry=_H3cOnuChipSetInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,24,1))
h3cOnuChipSetInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuChipSetInfoEntry.setStatus(_A)
class _H3cOnuChipSetVendorId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cOnuChipSetVendorId_Type.__name__=_L
_H3cOnuChipSetVendorId_Object=MibTableColumn
h3cOnuChipSetVendorId=_H3cOnuChipSetVendorId_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,24,1,1),_H3cOnuChipSetVendorId_Type())
h3cOnuChipSetVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuChipSetVendorId.setStatus(_A)
class _H3cOnuChipSetModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cOnuChipSetModel_Type.__name__=_L
_H3cOnuChipSetModel_Object=MibTableColumn
h3cOnuChipSetModel=_H3cOnuChipSetModel_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,24,1,2),_H3cOnuChipSetModel_Type())
h3cOnuChipSetModel.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuChipSetModel.setStatus(_A)
_H3cOnuChipSetRevision_Type=Integer32
_H3cOnuChipSetRevision_Object=MibTableColumn
h3cOnuChipSetRevision=_H3cOnuChipSetRevision_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,24,1,3),_H3cOnuChipSetRevision_Type())
h3cOnuChipSetRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuChipSetRevision.setStatus(_A)
_H3cOnuChipSetDesignDate_Type=DateAndTime
_H3cOnuChipSetDesignDate_Object=MibTableColumn
h3cOnuChipSetDesignDate=_H3cOnuChipSetDesignDate_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,24,1,4),_H3cOnuChipSetDesignDate_Type())
h3cOnuChipSetDesignDate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuChipSetDesignDate.setStatus(_A)
_H3cOnuCapabilityTable_Object=MibTable
h3cOnuCapabilityTable=_H3cOnuCapabilityTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25))
if mibBuilder.loadTexts:h3cOnuCapabilityTable.setStatus(_A)
_H3cOnuCapabilityEntry_Object=MibTableRow
h3cOnuCapabilityEntry=_H3cOnuCapabilityEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1))
h3cOnuCapabilityEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuCapabilityEntry.setStatus(_A)
class _H3cOnuServiceSupported_Type(Bits):namedValues=NamedValues(*(('geinterfacesupport',0),('feinterfacesupport',1),('voipservicesupport',2),('tdmservicesupport',3)))
_H3cOnuServiceSupported_Type.__name__='Bits'
_H3cOnuServiceSupported_Object=MibTableColumn
h3cOnuServiceSupported=_H3cOnuServiceSupported_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,1),_H3cOnuServiceSupported_Type())
h3cOnuServiceSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuServiceSupported.setStatus(_A)
_H3cOnuGEPortNumber_Type=Integer32
_H3cOnuGEPortNumber_Object=MibTableColumn
h3cOnuGEPortNumber=_H3cOnuGEPortNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,2),_H3cOnuGEPortNumber_Type())
h3cOnuGEPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuGEPortNumber.setStatus(_A)
_H3cOnuFEPortNumber_Type=Integer32
_H3cOnuFEPortNumber_Object=MibTableColumn
h3cOnuFEPortNumber=_H3cOnuFEPortNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,3),_H3cOnuFEPortNumber_Type())
h3cOnuFEPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuFEPortNumber.setStatus(_A)
_H3cOnuPOTSPortNumber_Type=Integer32
_H3cOnuPOTSPortNumber_Object=MibTableColumn
h3cOnuPOTSPortNumber=_H3cOnuPOTSPortNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,4),_H3cOnuPOTSPortNumber_Type())
h3cOnuPOTSPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuPOTSPortNumber.setStatus(_A)
_H3cOnuE1PortsNumber_Type=Integer32
_H3cOnuE1PortsNumber_Object=MibTableColumn
h3cOnuE1PortsNumber=_H3cOnuE1PortsNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,5),_H3cOnuE1PortsNumber_Type())
h3cOnuE1PortsNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuE1PortsNumber.setStatus(_A)
_H3cOnuUpstreamQueueNumber_Type=Integer32
_H3cOnuUpstreamQueueNumber_Object=MibTableColumn
h3cOnuUpstreamQueueNumber=_H3cOnuUpstreamQueueNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,6),_H3cOnuUpstreamQueueNumber_Type())
h3cOnuUpstreamQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuUpstreamQueueNumber.setStatus(_A)
_H3cOnuMaxUpstreamQueuePerPort_Type=Integer32
_H3cOnuMaxUpstreamQueuePerPort_Object=MibTableColumn
h3cOnuMaxUpstreamQueuePerPort=_H3cOnuMaxUpstreamQueuePerPort_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,7),_H3cOnuMaxUpstreamQueuePerPort_Type())
h3cOnuMaxUpstreamQueuePerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuMaxUpstreamQueuePerPort.setStatus(_A)
_H3cOnuDownstreamQueueNumber_Type=Integer32
_H3cOnuDownstreamQueueNumber_Object=MibTableColumn
h3cOnuDownstreamQueueNumber=_H3cOnuDownstreamQueueNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,8),_H3cOnuDownstreamQueueNumber_Type())
h3cOnuDownstreamQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuDownstreamQueueNumber.setStatus(_A)
_H3cOnuMaxDownstreamQueuePerPort_Type=Integer32
_H3cOnuMaxDownstreamQueuePerPort_Object=MibTableColumn
h3cOnuMaxDownstreamQueuePerPort=_H3cOnuMaxDownstreamQueuePerPort_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,9),_H3cOnuMaxDownstreamQueuePerPort_Type())
h3cOnuMaxDownstreamQueuePerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuMaxDownstreamQueuePerPort.setStatus(_A)
_H3cOnuBatteryBackup_Type=TruthValue
_H3cOnuBatteryBackup_Object=MibTableColumn
h3cOnuBatteryBackup=_H3cOnuBatteryBackup_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,10),_H3cOnuBatteryBackup_Type())
h3cOnuBatteryBackup.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuBatteryBackup.setStatus(_A)
_H3cOnuIgspFastLeaveSupported_Type=TruthValue
_H3cOnuIgspFastLeaveSupported_Object=MibTableColumn
h3cOnuIgspFastLeaveSupported=_H3cOnuIgspFastLeaveSupported_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,11),_H3cOnuIgspFastLeaveSupported_Type())
h3cOnuIgspFastLeaveSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuIgspFastLeaveSupported.setStatus(_A)
_H3cOnuMCtrlFastLeaveSupported_Type=TruthValue
_H3cOnuMCtrlFastLeaveSupported_Object=MibTableColumn
h3cOnuMCtrlFastLeaveSupported=_H3cOnuMCtrlFastLeaveSupported_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,25,1,12),_H3cOnuMCtrlFastLeaveSupported_Type())
h3cOnuMCtrlFastLeaveSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuMCtrlFastLeaveSupported.setStatus(_A)
_H3cOnuDbaReportTable_Object=MibTable
h3cOnuDbaReportTable=_H3cOnuDbaReportTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,26))
if mibBuilder.loadTexts:h3cOnuDbaReportTable.setStatus(_A)
_H3cOnuDbaReportEntry_Object=MibTableRow
h3cOnuDbaReportEntry=_H3cOnuDbaReportEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,26,1))
h3cOnuDbaReportEntry.setIndexNames((0,_D,_F),(0,_G,_w))
if mibBuilder.loadTexts:h3cOnuDbaReportEntry.setStatus(_A)
_H3cOnuDbaReportQueueId_Type=Integer32
_H3cOnuDbaReportQueueId_Object=MibTableColumn
h3cOnuDbaReportQueueId=_H3cOnuDbaReportQueueId_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,26,1,1),_H3cOnuDbaReportQueueId_Type())
h3cOnuDbaReportQueueId.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuDbaReportQueueId.setStatus(_A)
_H3cOnuDbaReportThreshold_Type=Integer32
_H3cOnuDbaReportThreshold_Object=MibTableColumn
h3cOnuDbaReportThreshold=_H3cOnuDbaReportThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,26,1,2),_H3cOnuDbaReportThreshold_Type())
h3cOnuDbaReportThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDbaReportThreshold.setStatus(_A)
class _H3cOnuDbaReportStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cOnuDbaReportStatus_Type.__name__=_E
_H3cOnuDbaReportStatus_Object=MibTableColumn
h3cOnuDbaReportStatus=_H3cOnuDbaReportStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,26,1,3),_H3cOnuDbaReportStatus_Type())
h3cOnuDbaReportStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuDbaReportStatus.setStatus(_A)
_H3cOnuCosToLocalPrecedenceTable_Object=MibTable
h3cOnuCosToLocalPrecedenceTable=_H3cOnuCosToLocalPrecedenceTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,27))
if mibBuilder.loadTexts:h3cOnuCosToLocalPrecedenceTable.setStatus(_A)
_H3cOnuCosToLocalPrecedenceEntry_Object=MibTableRow
h3cOnuCosToLocalPrecedenceEntry=_H3cOnuCosToLocalPrecedenceEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,27,1))
h3cOnuCosToLocalPrecedenceEntry.setIndexNames((0,_D,_F),(0,_G,_x))
if mibBuilder.loadTexts:h3cOnuCosToLocalPrecedenceEntry.setStatus(_A)
class _H3cOnuCosToLocalPrecedenceCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cOnuCosToLocalPrecedenceCosIndex_Type.__name__=_E
_H3cOnuCosToLocalPrecedenceCosIndex_Object=MibTableColumn
h3cOnuCosToLocalPrecedenceCosIndex=_H3cOnuCosToLocalPrecedenceCosIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,27,1,1),_H3cOnuCosToLocalPrecedenceCosIndex_Type())
h3cOnuCosToLocalPrecedenceCosIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuCosToLocalPrecedenceCosIndex.setStatus(_A)
class _H3cOnuCosToLocalPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cOnuCosToLocalPrecedenceValue_Type.__name__=_E
_H3cOnuCosToLocalPrecedenceValue_Object=MibTableColumn
h3cOnuCosToLocalPrecedenceValue=_H3cOnuCosToLocalPrecedenceValue_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,27,1,2),_H3cOnuCosToLocalPrecedenceValue_Type())
h3cOnuCosToLocalPrecedenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuCosToLocalPrecedenceValue.setStatus(_A)
_H3cEponOnuStpPortTable_Object=MibTable
h3cEponOnuStpPortTable=_H3cEponOnuStpPortTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,28))
if mibBuilder.loadTexts:h3cEponOnuStpPortTable.setStatus(_A)
_H3cEponOnuStpPortEntry_Object=MibTableRow
h3cEponOnuStpPortEntry=_H3cEponOnuStpPortEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,28,1))
h3cEponOnuStpPortEntry.setIndexNames((0,_D,_F),(0,_G,_b))
if mibBuilder.loadTexts:h3cEponOnuStpPortEntry.setStatus(_A)
class _H3cEponStpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,144))
_H3cEponStpPortIndex_Type.__name__=_E
_H3cEponStpPortIndex_Object=MibTableColumn
h3cEponStpPortIndex=_H3cEponStpPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,28,1,1),_H3cEponStpPortIndex_Type())
h3cEponStpPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponStpPortIndex.setStatus(_A)
_H3cEponStpPortDescr_Type=OctetString
_H3cEponStpPortDescr_Object=MibTableColumn
h3cEponStpPortDescr=_H3cEponStpPortDescr_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,28,1,2),_H3cEponStpPortDescr_Type())
h3cEponStpPortDescr.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponStpPortDescr.setStatus(_A)
class _H3cEponStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('discarding',2),('learning',3),('forwarding',4)))
_H3cEponStpPortState_Type.__name__=_E
_H3cEponStpPortState_Object=MibTableColumn
h3cEponStpPortState=_H3cEponStpPortState_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,28,1,3),_H3cEponStpPortState_Type())
h3cEponStpPortState.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponStpPortState.setStatus(_A)
_H3cOnuPhysicalTable_Object=MibTable
h3cOnuPhysicalTable=_H3cOnuPhysicalTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,29))
if mibBuilder.loadTexts:h3cOnuPhysicalTable.setStatus(_A)
_H3cOnuPhysicalEntry_Object=MibTableRow
h3cOnuPhysicalEntry=_H3cOnuPhysicalEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,29,1))
h3cOnuPhysicalEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cOnuPhysicalEntry.setStatus(_A)
_H3cOnuBridgeMac_Type=MacAddress
_H3cOnuBridgeMac_Object=MibTableColumn
h3cOnuBridgeMac=_H3cOnuBridgeMac_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,29,1,1),_H3cOnuBridgeMac_Type())
h3cOnuBridgeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuBridgeMac.setStatus(_A)
_H3cOnuFirstPonMac_Type=MacAddress
_H3cOnuFirstPonMac_Object=MibTableColumn
h3cOnuFirstPonMac=_H3cOnuFirstPonMac_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,29,1,2),_H3cOnuFirstPonMac_Type())
h3cOnuFirstPonMac.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuFirstPonMac.setStatus(_A)
class _H3cOnuFirstPonRegState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_y,1),(_z,2),('offline',3),('silent',4),(_T,5),('up',6)))
_H3cOnuFirstPonRegState_Type.__name__=_E
_H3cOnuFirstPonRegState_Object=MibTableColumn
h3cOnuFirstPonRegState=_H3cOnuFirstPonRegState_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,29,1,3),_H3cOnuFirstPonRegState_Type())
h3cOnuFirstPonRegState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuFirstPonRegState.setStatus(_A)
_H3cOnuSecondPonMac_Type=MacAddress
_H3cOnuSecondPonMac_Object=MibTableColumn
h3cOnuSecondPonMac=_H3cOnuSecondPonMac_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,29,1,4),_H3cOnuSecondPonMac_Type())
h3cOnuSecondPonMac.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSecondPonMac.setStatus(_A)
class _H3cOnuSecondPonRegState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_y,1),(_z,2),('offline',3),('silent',4),(_T,5),('up',6)))
_H3cOnuSecondPonRegState_Type.__name__=_E
_H3cOnuSecondPonRegState_Object=MibTableColumn
h3cOnuSecondPonRegState=_H3cOnuSecondPonRegState_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,29,1,5),_H3cOnuSecondPonRegState_Type())
h3cOnuSecondPonRegState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSecondPonRegState.setStatus(_A)
_H3cOnuSmlkTable_Object=MibTable
h3cOnuSmlkTable=_H3cOnuSmlkTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,30))
if mibBuilder.loadTexts:h3cOnuSmlkTable.setStatus(_A)
_H3cOnuSmlkEntry_Object=MibTableRow
h3cOnuSmlkEntry=_H3cOnuSmlkEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,30,1))
h3cOnuSmlkEntry.setIndexNames((0,_D,_F),(0,_G,_c))
if mibBuilder.loadTexts:h3cOnuSmlkEntry.setStatus(_A)
_H3cOnuSmlkGroupID_Type=Integer32
_H3cOnuSmlkGroupID_Object=MibTableColumn
h3cOnuSmlkGroupID=_H3cOnuSmlkGroupID_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,30,1,1),_H3cOnuSmlkGroupID_Type())
h3cOnuSmlkGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSmlkGroupID.setStatus(_A)
class _H3cOnuSmlkFirstPonRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),(_U,3)))
_H3cOnuSmlkFirstPonRole_Type.__name__=_E
_H3cOnuSmlkFirstPonRole_Object=MibTableColumn
h3cOnuSmlkFirstPonRole=_H3cOnuSmlkFirstPonRole_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,30,1,2),_H3cOnuSmlkFirstPonRole_Type())
h3cOnuSmlkFirstPonRole.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSmlkFirstPonRole.setStatus(_A)
class _H3cOnuSmlkFirstPonStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('standby',2),(_T,3),(_U,4)))
_H3cOnuSmlkFirstPonStatus_Type.__name__=_E
_H3cOnuSmlkFirstPonStatus_Object=MibTableColumn
h3cOnuSmlkFirstPonStatus=_H3cOnuSmlkFirstPonStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,30,1,3),_H3cOnuSmlkFirstPonStatus_Type())
h3cOnuSmlkFirstPonStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSmlkFirstPonStatus.setStatus(_A)
class _H3cOnuSmlkSecondPonRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),(_U,3)))
_H3cOnuSmlkSecondPonRole_Type.__name__=_E
_H3cOnuSmlkSecondPonRole_Object=MibTableColumn
h3cOnuSmlkSecondPonRole=_H3cOnuSmlkSecondPonRole_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,30,1,4),_H3cOnuSmlkSecondPonRole_Type())
h3cOnuSmlkSecondPonRole.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSmlkSecondPonRole.setStatus(_A)
class _H3cOnuSmlkSecondPonStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('standby',2),(_T,3),(_U,4)))
_H3cOnuSmlkSecondPonStatus_Type.__name__=_E
_H3cOnuSmlkSecondPonStatus_Object=MibTableColumn
h3cOnuSmlkSecondPonStatus=_H3cOnuSmlkSecondPonStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,30,1,5),_H3cOnuSmlkSecondPonStatus_Type())
h3cOnuSmlkSecondPonStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuSmlkSecondPonStatus.setStatus(_A)
_H3cOnuRS485PropertiesTable_Object=MibTable
h3cOnuRS485PropertiesTable=_H3cOnuRS485PropertiesTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31))
if mibBuilder.loadTexts:h3cOnuRS485PropertiesTable.setStatus(_A)
_H3cOnuRS485PropertiesEntry_Object=MibTableRow
h3cOnuRS485PropertiesEntry=_H3cOnuRS485PropertiesEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1))
h3cOnuRS485PropertiesEntry.setIndexNames((0,_D,_F),(0,_G,_S))
if mibBuilder.loadTexts:h3cOnuRS485PropertiesEntry.setStatus(_A)
class _H3cOnuRS485SerialIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cOnuRS485SerialIndex_Type.__name__=_E
_H3cOnuRS485SerialIndex_Object=MibTableColumn
h3cOnuRS485SerialIndex=_H3cOnuRS485SerialIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,1),_H3cOnuRS485SerialIndex_Type())
h3cOnuRS485SerialIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuRS485SerialIndex.setStatus(_A)
class _H3cOnuRS485BaudRate_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('baudRate300',1),('baudRate600',2),('baudRate1200',3),('baudRate2400',4),('baudRate4800',5),('baudRate9600',6),('baudRate19200',7),('baudRate38400',8),('baudRate57600',9),('baudRate115200',10)))
_H3cOnuRS485BaudRate_Type.__name__=_E
_H3cOnuRS485BaudRate_Object=MibTableColumn
h3cOnuRS485BaudRate=_H3cOnuRS485BaudRate_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,2),_H3cOnuRS485BaudRate_Type())
h3cOnuRS485BaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuRS485BaudRate.setStatus(_A)
class _H3cOnuRS485DataBits_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('five',1),('six',2),('seven',3),('eight',4)))
_H3cOnuRS485DataBits_Type.__name__=_E
_H3cOnuRS485DataBits_Object=MibTableColumn
h3cOnuRS485DataBits=_H3cOnuRS485DataBits_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,3),_H3cOnuRS485DataBits_Type())
h3cOnuRS485DataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuRS485DataBits.setStatus(_A)
if mibBuilder.loadTexts:h3cOnuRS485DataBits.setUnits('bit')
class _H3cOnuRS485Parity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3),('mark',4),('space',5)))
_H3cOnuRS485Parity_Type.__name__=_E
_H3cOnuRS485Parity_Object=MibTableColumn
h3cOnuRS485Parity=_H3cOnuRS485Parity_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,4),_H3cOnuRS485Parity_Type())
h3cOnuRS485Parity.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuRS485Parity.setStatus(_A)
class _H3cOnuRS485StopBits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('one',1),('two',2),('oneAndHalf',3)))
_H3cOnuRS485StopBits_Type.__name__=_E
_H3cOnuRS485StopBits_Object=MibTableColumn
h3cOnuRS485StopBits=_H3cOnuRS485StopBits_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,5),_H3cOnuRS485StopBits_Type())
h3cOnuRS485StopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuRS485StopBits.setStatus(_A)
if mibBuilder.loadTexts:h3cOnuRS485StopBits.setUnits('bit')
class _H3cOnuRS485FlowControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('hardware',2),('xonOrxoff',3)))
_H3cOnuRS485FlowControl_Type.__name__=_E
_H3cOnuRS485FlowControl_Object=MibTableColumn
h3cOnuRS485FlowControl=_H3cOnuRS485FlowControl_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,6),_H3cOnuRS485FlowControl_Type())
h3cOnuRS485FlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuRS485FlowControl.setStatus(_A)
_H3cOnuRS485TXOctets_Type=Integer32
_H3cOnuRS485TXOctets_Object=MibTableColumn
h3cOnuRS485TXOctets=_H3cOnuRS485TXOctets_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,7),_H3cOnuRS485TXOctets_Type())
h3cOnuRS485TXOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRS485TXOctets.setStatus(_A)
_H3cOnuRS485RXOctets_Type=Integer32
_H3cOnuRS485RXOctets_Object=MibTableColumn
h3cOnuRS485RXOctets=_H3cOnuRS485RXOctets_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,8),_H3cOnuRS485RXOctets_Type())
h3cOnuRS485RXOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRS485RXOctets.setStatus(_A)
_H3cOnuRS485TXErrOctets_Type=Integer32
_H3cOnuRS485TXErrOctets_Object=MibTableColumn
h3cOnuRS485TXErrOctets=_H3cOnuRS485TXErrOctets_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,9),_H3cOnuRS485TXErrOctets_Type())
h3cOnuRS485TXErrOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRS485TXErrOctets.setStatus(_A)
_H3cOnuRS485RXErrOctets_Type=Integer32
_H3cOnuRS485RXErrOctets_Object=MibTableColumn
h3cOnuRS485RXErrOctets=_H3cOnuRS485RXErrOctets_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,10),_H3cOnuRS485RXErrOctets_Type())
h3cOnuRS485RXErrOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRS485RXErrOctets.setStatus(_A)
class _H3cOnuRS485ResetStatistics_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('counting',1),('clear',2)))
_H3cOnuRS485ResetStatistics_Type.__name__=_E
_H3cOnuRS485ResetStatistics_Object=MibTableColumn
h3cOnuRS485ResetStatistics=_H3cOnuRS485ResetStatistics_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,31,1,11),_H3cOnuRS485ResetStatistics_Type())
h3cOnuRS485ResetStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOnuRS485ResetStatistics.setStatus(_A)
_H3cOnuRS485SessionSummaryTable_Object=MibTable
h3cOnuRS485SessionSummaryTable=_H3cOnuRS485SessionSummaryTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,32))
if mibBuilder.loadTexts:h3cOnuRS485SessionSummaryTable.setStatus(_A)
_H3cOnuRS485SessionSummaryEntry_Object=MibTableRow
h3cOnuRS485SessionSummaryEntry=_H3cOnuRS485SessionSummaryEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,32,1))
h3cOnuRS485SessionSummaryEntry.setIndexNames((0,_D,_F),(0,_G,_S))
if mibBuilder.loadTexts:h3cOnuRS485SessionSummaryEntry.setStatus(_A)
class _H3cOnuRS485SessionMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cOnuRS485SessionMaxNum_Type.__name__=_E
_H3cOnuRS485SessionMaxNum_Object=MibTableColumn
h3cOnuRS485SessionMaxNum=_H3cOnuRS485SessionMaxNum_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,32,1,1),_H3cOnuRS485SessionMaxNum_Type())
h3cOnuRS485SessionMaxNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRS485SessionMaxNum.setStatus(_A)
class _H3cOnuRS485SessionNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_H3cOnuRS485SessionNextIndex_Type.__name__=_E
_H3cOnuRS485SessionNextIndex_Object=MibTableColumn
h3cOnuRS485SessionNextIndex=_H3cOnuRS485SessionNextIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,32,1,2),_H3cOnuRS485SessionNextIndex_Type())
h3cOnuRS485SessionNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRS485SessionNextIndex.setStatus(_A)
_H3cOnuRS485SessionTable_Object=MibTable
h3cOnuRS485SessionTable=_H3cOnuRS485SessionTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33))
if mibBuilder.loadTexts:h3cOnuRS485SessionTable.setStatus(_A)
_H3cOnuRS485SessionEntry_Object=MibTableRow
h3cOnuRS485SessionEntry=_H3cOnuRS485SessionEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1))
h3cOnuRS485SessionEntry.setIndexNames((0,_D,_F),(0,_G,_S),(0,_G,_d))
if mibBuilder.loadTexts:h3cOnuRS485SessionEntry.setStatus(_A)
class _H3cOnuRS485SessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cOnuRS485SessionIndex_Type.__name__=_E
_H3cOnuRS485SessionIndex_Object=MibTableColumn
h3cOnuRS485SessionIndex=_H3cOnuRS485SessionIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1,1),_H3cOnuRS485SessionIndex_Type())
h3cOnuRS485SessionIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuRS485SessionIndex.setStatus(_A)
class _H3cOnuRS485SessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tcpClient',2),('tcpServer',3)))
_H3cOnuRS485SessionType_Type.__name__=_E
_H3cOnuRS485SessionType_Object=MibTableColumn
h3cOnuRS485SessionType=_H3cOnuRS485SessionType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1,2),_H3cOnuRS485SessionType_Type())
h3cOnuRS485SessionType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuRS485SessionType.setStatus(_A)
_H3cOnuRS485SessionAddType_Type=InetAddressType
_H3cOnuRS485SessionAddType_Object=MibTableColumn
h3cOnuRS485SessionAddType=_H3cOnuRS485SessionAddType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1,3),_H3cOnuRS485SessionAddType_Type())
h3cOnuRS485SessionAddType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuRS485SessionAddType.setStatus(_A)
_H3cOnuRS485SessionRemoteIP_Type=InetAddress
_H3cOnuRS485SessionRemoteIP_Object=MibTableColumn
h3cOnuRS485SessionRemoteIP=_H3cOnuRS485SessionRemoteIP_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1,4),_H3cOnuRS485SessionRemoteIP_Type())
h3cOnuRS485SessionRemoteIP.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuRS485SessionRemoteIP.setStatus(_A)
class _H3cOnuRS485SessionRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_H3cOnuRS485SessionRemotePort_Type.__name__=_E
_H3cOnuRS485SessionRemotePort_Object=MibTableColumn
h3cOnuRS485SessionRemotePort=_H3cOnuRS485SessionRemotePort_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1,5),_H3cOnuRS485SessionRemotePort_Type())
h3cOnuRS485SessionRemotePort.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuRS485SessionRemotePort.setStatus(_A)
class _H3cOnuRS485SessionLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_H3cOnuRS485SessionLocalPort_Type.__name__=_E
_H3cOnuRS485SessionLocalPort_Object=MibTableColumn
h3cOnuRS485SessionLocalPort=_H3cOnuRS485SessionLocalPort_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1,6),_H3cOnuRS485SessionLocalPort_Type())
h3cOnuRS485SessionLocalPort.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuRS485SessionLocalPort.setStatus(_A)
_H3cOnuRS485SessionRowStatus_Type=RowStatus
_H3cOnuRS485SessionRowStatus_Object=MibTableColumn
h3cOnuRS485SessionRowStatus=_H3cOnuRS485SessionRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,33,1,7),_H3cOnuRS485SessionRowStatus_Type())
h3cOnuRS485SessionRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuRS485SessionRowStatus.setStatus(_A)
_H3cOnuRS485SessionErrInfoTable_Object=MibTable
h3cOnuRS485SessionErrInfoTable=_H3cOnuRS485SessionErrInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,34))
if mibBuilder.loadTexts:h3cOnuRS485SessionErrInfoTable.setStatus(_A)
_H3cOnuRS485SessionErrInfoEntry_Object=MibTableRow
h3cOnuRS485SessionErrInfoEntry=_H3cOnuRS485SessionErrInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,34,1))
h3cOnuRS485SessionErrInfoEntry.setIndexNames((0,_D,_F),(0,_G,_S),(0,_G,_d))
if mibBuilder.loadTexts:h3cOnuRS485SessionErrInfoEntry.setStatus(_A)
_H3cOnuRS485SessionErrInfo_Type=DisplayString
_H3cOnuRS485SessionErrInfo_Object=MibTableColumn
h3cOnuRS485SessionErrInfo=_H3cOnuRS485SessionErrInfo_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,5,34,1,1),_H3cOnuRS485SessionErrInfo_Type())
h3cOnuRS485SessionErrInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOnuRS485SessionErrInfo.setStatus(_A)
_H3cEponBatchOperationMan_ObjectIdentity=ObjectIdentity
h3cEponBatchOperationMan=_H3cEponBatchOperationMan_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,6))
_H3cEponBatchOperationBySlotTable_Object=MibTable
h3cEponBatchOperationBySlotTable=_H3cEponBatchOperationBySlotTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,1))
if mibBuilder.loadTexts:h3cEponBatchOperationBySlotTable.setStatus(_A)
_H3cEponBatchOperationBySlotEntry_Object=MibTableRow
h3cEponBatchOperationBySlotEntry=_H3cEponBatchOperationBySlotEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,1,1))
h3cEponBatchOperationBySlotEntry.setIndexNames((0,_G,_A0))
if mibBuilder.loadTexts:h3cEponBatchOperationBySlotEntry.setStatus(_A)
_H3cEponBatchOperationBySlotIndex_Type=Integer32
_H3cEponBatchOperationBySlotIndex_Object=MibTableColumn
h3cEponBatchOperationBySlotIndex=_H3cEponBatchOperationBySlotIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,1,1,1),_H3cEponBatchOperationBySlotIndex_Type())
h3cEponBatchOperationBySlotIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEponBatchOperationBySlotIndex.setStatus(_A)
class _H3cEponBatchOperationBySlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,9,10)));namedValues=NamedValues(*((_A1,1),('updateDba',9),(_A2,10)))
_H3cEponBatchOperationBySlotType_Type.__name__=_E
_H3cEponBatchOperationBySlotType_Object=MibTableColumn
h3cEponBatchOperationBySlotType=_H3cEponBatchOperationBySlotType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,1,1,2),_H3cEponBatchOperationBySlotType_Type())
h3cEponBatchOperationBySlotType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponBatchOperationBySlotType.setStatus(_A)
class _H3cEponBatchOperationBySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('batOpBySlot',1))
_H3cEponBatchOperationBySlot_Type.__name__=_E
_H3cEponBatchOperationBySlot_Object=MibTableColumn
h3cEponBatchOperationBySlot=_H3cEponBatchOperationBySlot_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,1,1,3),_H3cEponBatchOperationBySlot_Type())
h3cEponBatchOperationBySlot.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponBatchOperationBySlot.setStatus(_A)
_H3cEponBatchOperationBySlotResult_Type=Integer32
_H3cEponBatchOperationBySlotResult_Object=MibTableColumn
h3cEponBatchOperationBySlotResult=_H3cEponBatchOperationBySlotResult_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,1,1,4),_H3cEponBatchOperationBySlotResult_Type())
h3cEponBatchOperationBySlotResult.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponBatchOperationBySlotResult.setStatus(_A)
_H3cEponBatchOperationByOLTTable_Object=MibTable
h3cEponBatchOperationByOLTTable=_H3cEponBatchOperationByOLTTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,2))
if mibBuilder.loadTexts:h3cEponBatchOperationByOLTTable.setStatus(_A)
_H3cEponBatchOperationByOLTEntry_Object=MibTableRow
h3cEponBatchOperationByOLTEntry=_H3cEponBatchOperationByOLTEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,2,1))
h3cEponBatchOperationByOLTEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cEponBatchOperationByOLTEntry.setStatus(_A)
class _H3cEponBatchOperationByOLTType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*((_A1,1),(_A2,5)))
_H3cEponBatchOperationByOLTType_Type.__name__=_E
_H3cEponBatchOperationByOLTType_Object=MibTableColumn
h3cEponBatchOperationByOLTType=_H3cEponBatchOperationByOLTType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,2,1,1),_H3cEponBatchOperationByOLTType_Type())
h3cEponBatchOperationByOLTType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponBatchOperationByOLTType.setStatus(_A)
class _H3cEponBatchOperationByOLT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('batOpByOlt',1))
_H3cEponBatchOperationByOLT_Type.__name__=_E
_H3cEponBatchOperationByOLT_Object=MibTableColumn
h3cEponBatchOperationByOLT=_H3cEponBatchOperationByOLT_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,2,1,2),_H3cEponBatchOperationByOLT_Type())
h3cEponBatchOperationByOLT.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponBatchOperationByOLT.setStatus(_A)
_H3cEponBatchOperationByOLTResult_Type=Integer32
_H3cEponBatchOperationByOLTResult_Object=MibTableColumn
h3cEponBatchOperationByOLTResult=_H3cEponBatchOperationByOLTResult_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,2,1,3),_H3cEponBatchOperationByOLTResult_Type())
h3cEponBatchOperationByOLTResult.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponBatchOperationByOLTResult.setStatus(_A)
_H3cOnuFirmwareUpdateByTypeTable_Object=MibTable
h3cOnuFirmwareUpdateByTypeTable=_H3cOnuFirmwareUpdateByTypeTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,3))
if mibBuilder.loadTexts:h3cOnuFirmwareUpdateByTypeTable.setStatus(_A)
_H3cOnuFirmwareUpdateByTypeEntry_Object=MibTableRow
h3cOnuFirmwareUpdateByTypeEntry=_H3cOnuFirmwareUpdateByTypeEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,3,1))
h3cOnuFirmwareUpdateByTypeEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:h3cOnuFirmwareUpdateByTypeEntry.setStatus(_A)
_H3cOnuUpdateByOnuTypeIndex_Type=Integer32
_H3cOnuUpdateByOnuTypeIndex_Object=MibTableColumn
h3cOnuUpdateByOnuTypeIndex=_H3cOnuUpdateByOnuTypeIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,3,1,1),_H3cOnuUpdateByOnuTypeIndex_Type())
h3cOnuUpdateByOnuTypeIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cOnuUpdateByOnuTypeIndex.setStatus(_A)
class _H3cOnuUpdateByTypeOnuType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_H3cOnuUpdateByTypeOnuType_Type.__name__=_L
_H3cOnuUpdateByTypeOnuType_Object=MibTableColumn
h3cOnuUpdateByTypeOnuType=_H3cOnuUpdateByTypeOnuType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,3,1,2),_H3cOnuUpdateByTypeOnuType_Type())
h3cOnuUpdateByTypeOnuType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuUpdateByTypeOnuType.setStatus(_A)
class _H3cOnuUpdateByTypeFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cOnuUpdateByTypeFileName_Type.__name__=_L
_H3cOnuUpdateByTypeFileName_Object=MibTableColumn
h3cOnuUpdateByTypeFileName=_H3cOnuUpdateByTypeFileName_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,3,1,3),_H3cOnuUpdateByTypeFileName_Type())
h3cOnuUpdateByTypeFileName.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuUpdateByTypeFileName.setStatus(_A)
_H3cOnuUpdateByTypeRowStatus_Type=RowStatus
_H3cOnuUpdateByTypeRowStatus_Object=MibTableColumn
h3cOnuUpdateByTypeRowStatus=_H3cOnuUpdateByTypeRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,6,3,1,4),_H3cOnuUpdateByTypeRowStatus_Type())
h3cOnuUpdateByTypeRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cOnuUpdateByTypeRowStatus.setStatus(_A)
_H3cEponErrorInfo_ObjectIdentity=ObjectIdentity
h3cEponErrorInfo=_H3cEponErrorInfo_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,7))
_H3cEponSoftwareErrorCode_Type=Integer32
_H3cEponSoftwareErrorCode_Object=MibScalar
h3cEponSoftwareErrorCode=_H3cEponSoftwareErrorCode_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,1),_H3cEponSoftwareErrorCode_Type())
h3cEponSoftwareErrorCode.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponSoftwareErrorCode.setStatus(_A)
_H3cOamVendorSpecificAlarmCode_Type=Integer32
_H3cOamVendorSpecificAlarmCode_Object=MibScalar
h3cOamVendorSpecificAlarmCode=_H3cOamVendorSpecificAlarmCode_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,2),_H3cOamVendorSpecificAlarmCode_Type())
h3cOamVendorSpecificAlarmCode.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cOamVendorSpecificAlarmCode.setStatus(_A)
_H3cEponOnuRegErrorMacAddr_Type=OctetString
_H3cEponOnuRegErrorMacAddr_Object=MibScalar
h3cEponOnuRegErrorMacAddr=_H3cEponOnuRegErrorMacAddr_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,3),_H3cEponOnuRegErrorMacAddr_Type())
h3cEponOnuRegErrorMacAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponOnuRegErrorMacAddr.setStatus(_A)
_H3cOamEventLogType_Type=Unsigned32
_H3cOamEventLogType_Object=MibScalar
h3cOamEventLogType=_H3cOamEventLogType_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,4),_H3cOamEventLogType_Type())
h3cOamEventLogType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cOamEventLogType.setStatus(_A)
class _H3cOamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_H3cOamEventLogLocation_Type.__name__=_E
_H3cOamEventLogLocation_Object=MibScalar
h3cOamEventLogLocation=_H3cOamEventLogLocation_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,5),_H3cOamEventLogLocation_Type())
h3cOamEventLogLocation.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cOamEventLogLocation.setStatus(_A)
_H3cEponLoopbackPortIndex_Type=Integer32
_H3cEponLoopbackPortIndex_Object=MibScalar
h3cEponLoopbackPortIndex=_H3cEponLoopbackPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,6),_H3cEponLoopbackPortIndex_Type())
h3cEponLoopbackPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponLoopbackPortIndex.setStatus(_A)
class _H3cEponLoopbackPortDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponLoopbackPortDescr_Type.__name__=_L
_H3cEponLoopbackPortDescr_Object=MibScalar
h3cEponLoopbackPortDescr=_H3cEponLoopbackPortDescr_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,7),_H3cEponLoopbackPortDescr_Type())
h3cEponLoopbackPortDescr.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponLoopbackPortDescr.setStatus(_A)
_H3cOltPortAlarmLlidMisFrames_Type=Unsigned32
_H3cOltPortAlarmLlidMisFrames_Object=MibScalar
h3cOltPortAlarmLlidMisFrames=_H3cOltPortAlarmLlidMisFrames_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,8),_H3cOltPortAlarmLlidMisFrames_Type())
h3cOltPortAlarmLlidMisFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cOltPortAlarmLlidMisFrames.setStatus(_A)
_H3cOltPortAlarmBer_Type=Unsigned32
_H3cOltPortAlarmBer_Object=MibScalar
h3cOltPortAlarmBer=_H3cOltPortAlarmBer_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,9),_H3cOltPortAlarmBer_Type())
h3cOltPortAlarmBer.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cOltPortAlarmBer.setStatus(_A)
_H3cOltPortAlarmFer_Type=Unsigned32
_H3cOltPortAlarmFer_Object=MibScalar
h3cOltPortAlarmFer=_H3cOltPortAlarmFer_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,10),_H3cOltPortAlarmFer_Type())
h3cOltPortAlarmFer.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cOltPortAlarmFer.setStatus(_A)
_H3cEponOnuRegSilentMac_Type=OctetString
_H3cEponOnuRegSilentMac_Object=MibScalar
h3cEponOnuRegSilentMac=_H3cEponOnuRegSilentMac_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,11),_H3cEponOnuRegSilentMac_Type())
h3cEponOnuRegSilentMac.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponOnuRegSilentMac.setStatus(_A)
class _H3cEponOperationResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponOperationResult_Type.__name__=_L
_H3cEponOperationResult_Object=MibScalar
h3cEponOperationResult=_H3cEponOperationResult_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,12),_H3cEponOperationResult_Type())
h3cEponOperationResult.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponOperationResult.setStatus(_A)
class _H3cEponOnuLaserState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('laserAlwaysOn',2),('signalDegradation',3),('endOfLife',4)))
_H3cEponOnuLaserState_Type.__name__=_E
_H3cEponOnuLaserState_Object=MibScalar
h3cEponOnuLaserState=_H3cEponOnuLaserState_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,7,13),_H3cEponOnuLaserState_Type())
h3cEponOnuLaserState.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEponOnuLaserState.setStatus(_A)
_H3cEponTrap_ObjectIdentity=ObjectIdentity
h3cEponTrap=_H3cEponTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,8))
_H3cEponTrapPrefix_ObjectIdentity=ObjectIdentity
h3cEponTrapPrefix=_H3cEponTrapPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0))
_H3cEponStat_ObjectIdentity=ObjectIdentity
h3cEponStat=_H3cEponStat_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,1,9))
_H3cEponStatTable_Object=MibTable
h3cEponStatTable=_H3cEponStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,9,1))
if mibBuilder.loadTexts:h3cEponStatTable.setStatus(_A)
_H3cEponStatEntry_Object=MibTableRow
h3cEponStatEntry=_H3cEponStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,9,1,1))
h3cEponStatEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cEponStatEntry.setStatus(_A)
_H3cEponStatFER_Type=Counter64
_H3cEponStatFER_Object=MibTableColumn
h3cEponStatFER=_H3cEponStatFER_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,9,1,1,1),_H3cEponStatFER_Type())
h3cEponStatFER.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponStatFER.setStatus(_A)
_H3cEponStatBER_Type=Counter64
_H3cEponStatBER_Object=MibTableColumn
h3cEponStatBER=_H3cEponStatBER_Object((1,3,6,1,4,1,43,45,1,10,2,42,1,9,1,1,2),_H3cEponStatBER_Type())
h3cEponStatBER.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponStatBER.setStatus(_A)
h3cEponPortAlarmBerTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,1))
h3cEponPortAlarmBerTrap.setObjects(*((_D,_F),(_D,_I),(_G,_e),(_G,_A4),(_G,_A5)))
if mibBuilder.loadTexts:h3cEponPortAlarmBerTrap.setStatus(_A)
h3cEponPortAlarmFerTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,2))
h3cEponPortAlarmFerTrap.setObjects(*((_D,_F),(_D,_I),(_G,_f),(_G,_A6),(_G,_A7)))
if mibBuilder.loadTexts:h3cEponPortAlarmFerTrap.setStatus(_A)
h3cEponErrorLLIDFrameTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,3))
h3cEponErrorLLIDFrameTrap.setObjects(*((_D,_F),(_D,_I),(_G,_A8),(_G,_A9)))
if mibBuilder.loadTexts:h3cEponErrorLLIDFrameTrap.setStatus(_A)
h3cEponLoopBackEnableTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,4))
h3cEponLoopBackEnableTrap.setObjects(*((_D,_F),(_D,_I),(_G,_AA),(_G,_AB)))
if mibBuilder.loadTexts:h3cEponLoopBackEnableTrap.setStatus(_A)
h3cEponOnuRegistrationErrTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,5))
h3cEponOnuRegistrationErrTrap.setObjects(*((_D,_F),(_D,_I),(_G,_g)))
if mibBuilder.loadTexts:h3cEponOnuRegistrationErrTrap.setStatus(_A)
h3cEponOamDisconnectionTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,6))
h3cEponOamDisconnectionTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOamDisconnectionTrap.setStatus(_A)
h3cEponEncryptionKeyErrTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,7))
h3cEponEncryptionKeyErrTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponEncryptionKeyErrTrap.setStatus(_A)
h3cEponRemoteStableTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,8))
h3cEponRemoteStableTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponRemoteStableTrap.setStatus(_A)
h3cEponLocalStableTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,9))
h3cEponLocalStableTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponLocalStableTrap.setStatus(_A)
h3cEponOamVendorSpecificTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,10))
h3cEponOamVendorSpecificTrap.setObjects(*((_D,_F),(_D,_I),(_G,_h)))
if mibBuilder.loadTexts:h3cEponOamVendorSpecificTrap.setStatus(_A)
h3cEponSoftwareErrTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,11))
h3cEponSoftwareErrTrap.setObjects(*((_P,_V),(_P,_W),(_G,_i)))
if mibBuilder.loadTexts:h3cEponSoftwareErrTrap.setStatus(_A)
h3cEponPortAlarmBerRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,12))
h3cEponPortAlarmBerRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_e)))
if mibBuilder.loadTexts:h3cEponPortAlarmBerRecoverTrap.setStatus(_A)
h3cEponPortAlarmFerRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,13))
h3cEponPortAlarmFerRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_f)))
if mibBuilder.loadTexts:h3cEponPortAlarmFerRecoverTrap.setStatus(_A)
h3cEponErrorLLIDFrameRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,14))
h3cEponErrorLLIDFrameRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponErrorLLIDFrameRecoverTrap.setStatus(_A)
h3cEponLoopBackEnableRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,15))
h3cEponLoopBackEnableRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponLoopBackEnableRecoverTrap.setStatus(_A)
h3cEponOnuRegistrationErrRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,16))
h3cEponOnuRegistrationErrRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_g)))
if mibBuilder.loadTexts:h3cEponOnuRegistrationErrRecoverTrap.setStatus(_A)
h3cEponOamDisconnectionRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,17))
h3cEponOamDisconnectionRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOamDisconnectionRecoverTrap.setStatus(_A)
h3cEponEncryptionKeyErrRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,18))
h3cEponEncryptionKeyErrRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponEncryptionKeyErrRecoverTrap.setStatus(_A)
h3cEponRemoteStableRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,19))
h3cEponRemoteStableRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponRemoteStableRecoverTrap.setStatus(_A)
h3cEponLocalStableRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,20))
h3cEponLocalStableRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponLocalStableRecoverTrap.setStatus(_A)
h3cEponOamVendorSpecificRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,21))
h3cEponOamVendorSpecificRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_h)))
if mibBuilder.loadTexts:h3cEponOamVendorSpecificRecoverTrap.setStatus(_A)
h3cEponSoftwareErrRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,22))
h3cEponSoftwareErrRecoverTrap.setObjects(*((_P,_V),(_P,_W),(_G,_i)))
if mibBuilder.loadTexts:h3cEponSoftwareErrRecoverTrap.setStatus(_A)
h3cDot3OamThresholdRecoverEvent=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,23))
h3cDot3OamThresholdRecoverEvent.setObjects(*((_D,_F),(_G,_j),(_G,_k)))
if mibBuilder.loadTexts:h3cDot3OamThresholdRecoverEvent.setStatus(_A)
h3cDot3OamNonThresholdRecoverEvent=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,24))
h3cDot3OamNonThresholdRecoverEvent.setObjects(*((_D,_F),(_G,_j),(_G,_k)))
if mibBuilder.loadTexts:h3cDot3OamNonThresholdRecoverEvent.setStatus(_A)
h3cEponOnuRegExcessTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,25))
h3cEponOnuRegExcessTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOnuRegExcessTrap.setStatus(_A)
h3cEponOnuRegExcessRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,26))
h3cEponOnuRegExcessRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOnuRegExcessRecoverTrap.setStatus(_A)
h3cEponOnuPowerOffTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,27))
h3cEponOnuPowerOffTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOnuPowerOffTrap.setStatus(_A)
h3cEponOltSwitchoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,28))
h3cEponOltSwitchoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOltSwitchoverTrap.setStatus(_A)
h3cEponOltDFETrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,29))
h3cEponOltDFETrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOltDFETrap.setStatus(_A)
h3cEponOltDFERecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,30))
h3cEponOltDFERecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:h3cEponOltDFERecoverTrap.setStatus(_A)
h3cEponOnuSilenceTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,31))
h3cEponOnuSilenceTrap.setObjects(*((_D,_F),(_D,_I),(_G,_l)))
if mibBuilder.loadTexts:h3cEponOnuSilenceTrap.setStatus(_A)
h3cEponOnuSilenceRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,32))
h3cEponOnuSilenceRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_l)))
if mibBuilder.loadTexts:h3cEponOnuSilenceRecoverTrap.setStatus(_A)
h3cEponOnuUpdateResultTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,33))
h3cEponOnuUpdateResultTrap.setObjects(*((_D,_F),(_D,_I),(_G,_m),(_G,_AC),(_G,_AD),(_G,_AE)))
if mibBuilder.loadTexts:h3cEponOnuUpdateResultTrap.setStatus(_A)
h3cEponOnuAutoBindTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,34))
h3cEponOnuAutoBindTrap.setObjects(*((_D,_F),(_D,_I),(_G,_m),(_G,_AF)))
if mibBuilder.loadTexts:h3cEponOnuAutoBindTrap.setStatus(_A)
h3cEponOnuPortStpStateTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,35))
h3cEponOnuPortStpStateTrap.setObjects(*((_D,_F),(_D,_I),(_G,_b),(_G,_AG),(_G,_AH)))
if mibBuilder.loadTexts:h3cEponOnuPortStpStateTrap.setStatus(_A)
h3cEponOnuLaserFailedTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,36))
h3cEponOnuLaserFailedTrap.setObjects(*((_D,_F),(_D,_I),(_G,_AI)))
if mibBuilder.loadTexts:h3cEponOnuLaserFailedTrap.setStatus(_A)
h3cOnuSmlkSwitchoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,1,8,0,37))
h3cOnuSmlkSwitchoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_c),(_G,_AJ),(_G,_AK)))
if mibBuilder.loadTexts:h3cOnuSmlkSwitchoverTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'h3cEponMibObjects':h3cEponMibObjects,'h3cEponSysMan':h3cEponSysMan,'h3cEponAutoAuthorize':h3cEponAutoAuthorize,'h3cEponMonitorCycle':h3cEponMonitorCycle,'h3cEponMsgTimeOut':h3cEponMsgTimeOut,'h3cEponMsgLoseNum':h3cEponMsgLoseNum,'h3cEponSysHasEPONBoard':h3cEponSysHasEPONBoard,'h3cEponMonitorCycleEnable':h3cEponMonitorCycleEnable,'h3cEponOltSoftwareErrAlmEnable':h3cEponOltSoftwareErrAlmEnable,'h3cEponPortLoopBackAlmEnable':h3cEponPortLoopBackAlmEnable,'h3cEponMonitorCycleMinVal':h3cEponMonitorCycleMinVal,'h3cEponMonitorCycleMaxVal':h3cEponMonitorCycleMaxVal,'h3cEponMsgTimeOutMinVal':h3cEponMsgTimeOutMinVal,'h3cEponMsgTimeOutMaxVal':h3cEponMsgTimeOutMaxVal,'h3cEponMsgLoseNumMinVal':h3cEponMsgLoseNumMinVal,'h3cEponMsgLoseNumMaxVal':h3cEponMsgLoseNumMaxVal,'h3cEponSysScalarGroup':h3cEponSysScalarGroup,'h3cEponSysManTable':h3cEponSysManTable,'h3cEponSysManEntry':h3cEponSysManEntry,_Q:h3cEponSlotIndex,'h3cEponModeSwitch':h3cEponModeSwitch,'h3cEponAutomaticMode':h3cEponAutomaticMode,'h3cEponOamDiscoveryTimeout':h3cEponOamDiscoveryTimeout,'h3cEponEncryptionNoReplyTimeOut':h3cEponEncryptionNoReplyTimeOut,'h3cEponEncryptionUpdateTime':h3cEponEncryptionUpdateTime,'h3cEponAutoBindStatus':h3cEponAutoBindStatus,'h3cEponAutoUpdateTable':h3cEponAutoUpdateTable,'h3cEponAutoUpdateEntry':h3cEponAutoUpdateEntry,'h3cEponAutoUpdateFileName':h3cEponAutoUpdateFileName,'h3cEponAutoUpdateSchedStatus':h3cEponAutoUpdateSchedStatus,'h3cEponAutoUpdateSchedTime':h3cEponAutoUpdateSchedTime,'h3cEponAutoUpdateSchedType':h3cEponAutoUpdateSchedType,'h3cEponAutoUpdateRealTimeStatus':h3cEponAutoUpdateRealTimeStatus,'h3cEponOuiIndexNextTable':h3cEponOuiIndexNextTable,'h3cEponOuiIndexNextEntry':h3cEponOuiIndexNextEntry,'h3cEponOuiIndexNext':h3cEponOuiIndexNext,'h3cEponOuiTable':h3cEponOuiTable,'h3cEponOuiEntry':h3cEponOuiEntry,_n:h3cEponOuiIndex,'h3cEponOuiValue':h3cEponOuiValue,'h3cEponOamVersion':h3cEponOamVersion,'h3cEponOuiRowStatus':h3cEponOuiRowStatus,'h3cEponMulticastControlTable':h3cEponMulticastControlTable,'h3cEponMulticastControlEntry':h3cEponMulticastControlEntry,_o:h3cEponMulticastVlanId,'h3cEponMulticastAddressList':h3cEponMulticastAddressList,'h3cEponMulticastStatus':h3cEponMulticastStatus,'h3cEponFileName':h3cEponFileName,'h3cEponDbaUpdateFileName':h3cEponDbaUpdateFileName,'h3cEponOnuUpdateFileName':h3cEponOnuUpdateFileName,'h3cEponOltMan':h3cEponOltMan,'h3cOltSysManTable':h3cOltSysManTable,'h3cOltSysManEntry':h3cOltSysManEntry,'h3cOltLaserOnTime':h3cOltLaserOnTime,'h3cOltLaserOffTime':h3cOltLaserOffTime,'h3cOltMultiCopyBrdCast':h3cOltMultiCopyBrdCast,'h3cOltEnableDiscardPacket':h3cOltEnableDiscardPacket,'h3cOltSelfTest':h3cOltSelfTest,'h3cOltSelfTestResult':h3cOltSelfTestResult,'h3cOltMaxRtt':h3cOltMaxRtt,'h3cOltInfoTable':h3cOltInfoTable,'h3cOltInfoEntry':h3cOltInfoEntry,'h3cOltFirmMajorVersion':h3cOltFirmMajorVersion,'h3cOltFirmMinorVersion':h3cOltFirmMinorVersion,'h3cOltHardMajorVersion':h3cOltHardMajorVersion,'h3cOltHardMinorVersion':h3cOltHardMinorVersion,'h3cOltAgcLockTime':h3cOltAgcLockTime,'h3cOltAgcCdrTime':h3cOltAgcCdrTime,'h3cOltMacAddress':h3cOltMacAddress,'h3cOltWorkMode':h3cOltWorkMode,'h3cOltOpticalPowerTx':h3cOltOpticalPowerTx,'h3cOltOpticalPowerRx':h3cOltOpticalPowerRx,'h3cOltDbaManTable':h3cOltDbaManTable,'h3cOltDbaManEntry':h3cOltDbaManEntry,'h3cOltDbaEnabledType':h3cOltDbaEnabledType,'h3cOltDbaDiscoveryLength':h3cOltDbaDiscoveryLength,'h3cOltDbaDiscovryFrequency':h3cOltDbaDiscovryFrequency,'h3cOltDbaCycleLength':h3cOltDbaCycleLength,'h3cOltDbaVersion':h3cOltDbaVersion,'h3cOltDbaUpdate':h3cOltDbaUpdate,'h3cOltDbaUpdateResult':h3cOltDbaUpdateResult,'h3cOltPortAlarmThresholdTable':h3cOltPortAlarmThresholdTable,'h3cOltPortAlarmThresholdEntry':h3cOltPortAlarmThresholdEntry,'h3cOltPortAlarmBerEnabled':h3cOltPortAlarmBerEnabled,_e:h3cOltPortAlarmBerDirect,_A5:h3cOltPortAlarmBerThreshold,'h3cOltPortAlarmFerEnabled':h3cOltPortAlarmFerEnabled,_f:h3cOltPortAlarmFerDirect,_A7:h3cOltPortAlarmFerThreshold,'h3cOltPortAlarmLlidMismatchEnabled':h3cOltPortAlarmLlidMismatchEnabled,_A9:h3cOltPortAlarmLlidMismatchThreshold,'h3cOltPortAlarmRemoteStableEnabled':h3cOltPortAlarmRemoteStableEnabled,'h3cOltPortAlarmLocalStableEnabled':h3cOltPortAlarmLocalStableEnabled,'h3cOltPortAlarmRegistrationEnabled':h3cOltPortAlarmRegistrationEnabled,'h3cOltPortAlarmOamDisconnectionEnabled':h3cOltPortAlarmOamDisconnectionEnabled,'h3cOltPortAlarmEncryptionKeyEnabled':h3cOltPortAlarmEncryptionKeyEnabled,'h3cOltPortAlarmVendorSpecificEnabled':h3cOltPortAlarmVendorSpecificEnabled,'h3cOltPortAlarmRegExcessEnabled':h3cOltPortAlarmRegExcessEnabled,'h3cOltPortAlarmDFEEnabled':h3cOltPortAlarmDFEEnabled,'h3cOltLaserOnTimeMinVal':h3cOltLaserOnTimeMinVal,'h3cOltLaserOnTimeMaxVal':h3cOltLaserOnTimeMaxVal,'h3cOltLaserOffTimeMinVal':h3cOltLaserOffTimeMinVal,'h3cOltLaserOffTimeMaxVal':h3cOltLaserOffTimeMaxVal,'h3cOltDbaDiscoveryLengthMinVal':h3cOltDbaDiscoveryLengthMinVal,'h3cOltDbaDiscoveryLengthMaxVal':h3cOltDbaDiscoveryLengthMaxVal,'h3cOltDbaDiscovryFrequencyMinVal':h3cOltDbaDiscovryFrequencyMinVal,'h3cOltDbaDiscovryFrequencyMaxVal':h3cOltDbaDiscovryFrequencyMaxVal,'h3cOltDbaCycleLengthMinVal':h3cOltDbaCycleLengthMinVal,'h3cOltDbaCycleLengthMaxVal':h3cOltDbaCycleLengthMaxVal,'h3cOltPortAlarmLlidMisMinVal':h3cOltPortAlarmLlidMisMinVal,'h3cOltPortAlarmLlidMisMaxVal':h3cOltPortAlarmLlidMisMaxVal,'h3cOltPortAlarmBerMinVal':h3cOltPortAlarmBerMinVal,'h3cOltPortAlarmBerMaxVal':h3cOltPortAlarmBerMaxVal,'h3cOltPortAlarmFerMinVal':h3cOltPortAlarmFerMinVal,'h3cOltPortAlarmFerMaxVal':h3cOltPortAlarmFerMaxVal,'h3cOnuSilentTable':h3cOnuSilentTable,'h3cOnuSilentEntry':h3cOnuSilentEntry,_s:h3cOnuSilentMacAddr,'h3cOnuSilentTime':h3cOnuSilentTime,'h3cOltUsingOnuTable':h3cOltUsingOnuTable,'h3cOltUsingOnuEntry':h3cOltUsingOnuEntry,_t:h3cOltUsingOnuNum,'h3cOltUsingOnuIfIndex':h3cOltUsingOnuIfIndex,'h3cOltUsingOnuRowStatus':h3cOltUsingOnuRowStatus,'h3cEponOnuMan':h3cEponOnuMan,'h3cOnuSysManTable':h3cOnuSysManTable,'h3cOnuSysManEntry':h3cOnuSysManEntry,'h3cOnuEncryptMan':h3cOnuEncryptMan,'h3cOnuReAuthorize':h3cOnuReAuthorize,'h3cOnuMulticastFilterStatus':h3cOnuMulticastFilterStatus,'h3cOnuDbaReportQueueSetNumber':h3cOnuDbaReportQueueSetNumber,'h3cOnuRemoteFecStatus':h3cOnuRemoteFecStatus,'h3cOnuPortBerStatus':h3cOnuPortBerStatus,'h3cOnuReset':h3cOnuReset,'h3cOnuMulticastControlMode':h3cOnuMulticastControlMode,'h3cOnuAccessVlan':h3cOnuAccessVlan,'h3cOnuEncryptKey':h3cOnuEncryptKey,'h3cOnuUniUpDownTrapStatus':h3cOnuUniUpDownTrapStatus,'h3cOnuFecStatus':h3cOnuFecStatus,'h3cOnuMcastCtrlHostAgingTime':h3cOnuMcastCtrlHostAgingTime,'h3cOnuMulticastFastLeaveEnable':h3cOnuMulticastFastLeaveEnable,'h3cOnuPortIsolateEnable':h3cOnuPortIsolateEnable,'h3cOnuLinkTestTable':h3cOnuLinkTestTable,'h3cOnuLinkTestEntry':h3cOnuLinkTestEntry,'h3cOnuLinkTestFrameNum':h3cOnuLinkTestFrameNum,'h3cOnuLinkTestFrameSize':h3cOnuLinkTestFrameSize,'h3cOnuLinkTestDelay':h3cOnuLinkTestDelay,'h3cOnuLinkTestVlanTag':h3cOnuLinkTestVlanTag,'h3cOnuLinkTestVlanPriority':h3cOnuLinkTestVlanPriority,'h3cOnuLinkTestVlanTagID':h3cOnuLinkTestVlanTagID,'h3cOnuLinkTestResultSentFrameNum':h3cOnuLinkTestResultSentFrameNum,'h3cOnuLinkTestResultRetFrameNum':h3cOnuLinkTestResultRetFrameNum,'h3cOnuLinkTestResultRetErrFrameNum':h3cOnuLinkTestResultRetErrFrameNum,'h3cOnuLinkTestResultMinDelay':h3cOnuLinkTestResultMinDelay,'h3cOnuLinkTestResultMeanDelay':h3cOnuLinkTestResultMeanDelay,'h3cOnuLinkTestResultMaxDelay':h3cOnuLinkTestResultMaxDelay,'h3cOnuBandWidthTable':h3cOnuBandWidthTable,'h3cOnuBandWidthEntry':h3cOnuBandWidthEntry,'h3cOnuDownStreamBandWidthPolicy':h3cOnuDownStreamBandWidthPolicy,'h3cOnuDownStreamMaxBandWidth':h3cOnuDownStreamMaxBandWidth,'h3cOnuDownStreamMaxBurstSize':h3cOnuDownStreamMaxBurstSize,'h3cOnuDownStreamHighPriorityFirst':h3cOnuDownStreamHighPriorityFirst,'h3cOnuDownStreamShortFrameFirst':h3cOnuDownStreamShortFrameFirst,'h3cOnuP2PBandWidthPolicy':h3cOnuP2PBandWidthPolicy,'h3cOnuP2PMaxBandWidth':h3cOnuP2PMaxBandWidth,'h3cOnuP2PMaxBurstSize':h3cOnuP2PMaxBurstSize,'h3cOnuP2PHighPriorityFirst':h3cOnuP2PHighPriorityFirst,'h3cOnuP2PShortFrameFirst':h3cOnuP2PShortFrameFirst,'h3cOnuSlaManTable':h3cOnuSlaManTable,'h3cOnuSlaManEntry':h3cOnuSlaManEntry,'h3cOnuSlaMaxBandWidth':h3cOnuSlaMaxBandWidth,'h3cOnuSlaMinBandWidth':h3cOnuSlaMinBandWidth,'h3cOnuSlaBandWidthStepVal':h3cOnuSlaBandWidthStepVal,'h3cOnuSlaDelay':h3cOnuSlaDelay,'h3cOnuSlaFixedBandWidth':h3cOnuSlaFixedBandWidth,'h3cOnuSlaPriorityClass':h3cOnuSlaPriorityClass,'h3cOnuSlaFixedPacketSize':h3cOnuSlaFixedPacketSize,'h3cOnuInfoTable':h3cOnuInfoTable,'h3cOnuInfoEntry':h3cOnuInfoEntry,'h3cOnuHardMajorVersion':h3cOnuHardMajorVersion,'h3cOnuHardMinorVersion':h3cOnuHardMinorVersion,'h3cOnuSoftwareVersion':h3cOnuSoftwareVersion,'h3cOnuUniMacType':h3cOnuUniMacType,'h3cOnuLaserOnTime':h3cOnuLaserOnTime,'h3cOnuLaserOffTime':h3cOnuLaserOffTime,'h3cOnuGrantFifoDep':h3cOnuGrantFifoDep,'h3cOnuWorkMode':h3cOnuWorkMode,'h3cOnuPCBVersion':h3cOnuPCBVersion,'h3cOnuRtt':h3cOnuRtt,'h3cOnuEEPROMVersion':h3cOnuEEPROMVersion,_AD:h3cOnuRegType,'h3cOnuHostType':h3cOnuHostType,'h3cOnuDistance':h3cOnuDistance,'h3cOnuLlid':h3cOnuLlid,'h3cOnuVendorId':h3cOnuVendorId,'h3cOnuFirmwareVersion':h3cOnuFirmwareVersion,'h3cOnuOpticalPowerReceivedByOlt':h3cOnuOpticalPowerReceivedByOlt,'h3cOnuMacAddrInfoTable':h3cOnuMacAddrInfoTable,'h3cOnuMacAddrInfoEntry':h3cOnuMacAddrInfoEntry,_u:h3cOnuMacIndex,'h3cOnuMacAddrFlag':h3cOnuMacAddrFlag,'h3cOnuMacAddress':h3cOnuMacAddress,'h3cOnuBindMacAddrTable':h3cOnuBindMacAddrTable,'h3cOnuBindMacAddrEntry':h3cOnuBindMacAddrEntry,_m:h3cOnuBindMacAddress,'h3cOnuBindType':h3cOnuBindType,'h3cOnuFirmwareUpdateTable':h3cOnuFirmwareUpdateTable,'h3cOnuFirmwareUpdateEntry':h3cOnuFirmwareUpdateEntry,'h3cOnuUpdate':h3cOnuUpdate,_AC:h3cOnuUpdateResult,_AE:h3cOnuUpdateFileName,'h3cOnuLinkTestFrameNumMinVal':h3cOnuLinkTestFrameNumMinVal,'h3cOnuLinkTestFrameNumMaxVal':h3cOnuLinkTestFrameNumMaxVal,'h3cOnuSlaMaxBandWidthMinVal':h3cOnuSlaMaxBandWidthMinVal,'h3cOnuSlaMaxBandWidthMaxVal':h3cOnuSlaMaxBandWidthMaxVal,'h3cOnuSlaMinBandWidthMinVal':h3cOnuSlaMinBandWidthMinVal,'h3cOnuSlaMinBandWidthMaxVal':h3cOnuSlaMinBandWidthMaxVal,'h3cEponOnuTypeManTable':h3cEponOnuTypeManTable,'h3cEponOnuTypeManEntry':h3cEponOnuTypeManEntry,_v:h3cEponOnuTypeIndex,'h3cEponOnuTypeDescr':h3cEponOnuTypeDescr,'h3cOnuPacketManTable':h3cOnuPacketManTable,'h3cOnuPacketManEntry':h3cOnuPacketManEntry,'h3cOnuPriorityTrust':h3cOnuPriorityTrust,'h3cOnuQueueScheduler':h3cOnuQueueScheduler,'h3cOnuProtocolTable':h3cOnuProtocolTable,'h3cOnuProtocolEntry':h3cOnuProtocolEntry,'h3cOnuStpStatus':h3cOnuStpStatus,'h3cOnuIgmpSnoopingStatus':h3cOnuIgmpSnoopingStatus,'h3cOnuDhcpsnoopingOption82':h3cOnuDhcpsnoopingOption82,'h3cOnuDhcpsnooping':h3cOnuDhcpsnooping,'h3cOnuPppoe':h3cOnuPppoe,'h3cOnuIgmpSnoopingHostAgingT':h3cOnuIgmpSnoopingHostAgingT,'h3cOnuIgmpSnoopingMaxRespT':h3cOnuIgmpSnoopingMaxRespT,'h3cOnuIgmpSnoopingRouterAgingT':h3cOnuIgmpSnoopingRouterAgingT,'h3cOnuIgmpSnoopingAggReportS':h3cOnuIgmpSnoopingAggReportS,'h3cOnuIgmpSnoopingAggLeaveS':h3cOnuIgmpSnoopingAggLeaveS,'h3cOnuDot1xTable':h3cOnuDot1xTable,'h3cOnuDot1xEntry':h3cOnuDot1xEntry,'h3cOnuDot1xAccount':h3cOnuDot1xAccount,'h3cOnuDot1xPassword':h3cOnuDot1xPassword,'h3cOnuPriorityQueueTable':h3cOnuPriorityQueueTable,'h3cOnuPriorityQueueEntry':h3cOnuPriorityQueueEntry,_Z:h3cOnuQueueDirection,_a:h3cOnuQueueId,'h3cOnuQueueSize':h3cOnuQueueSize,'h3cOnuCountTable':h3cOnuCountTable,'h3cOnuCountEntry':h3cOnuCountEntry,'h3cOnuInCRCErrPkts':h3cOnuInCRCErrPkts,'h3cOnuOutDroppedFrames':h3cOnuOutDroppedFrames,'h3cEponOnuScalarGroup':h3cEponOnuScalarGroup,'h3cOnuPriorityQueueSizeMinVal':h3cOnuPriorityQueueSizeMinVal,'h3cOnuPriorityQueueSizeMaxVal':h3cOnuPriorityQueueSizeMaxVal,'h3cOnuPriorityQueueBandwidthMinVal':h3cOnuPriorityQueueBandwidthMinVal,'h3cOnuPriorityQueueBandwidthMaxVal':h3cOnuPriorityQueueBandwidthMaxVal,'h3cOnuPriorityQueueBurstsizeMinVal':h3cOnuPriorityQueueBurstsizeMinVal,'h3cOnuPriorityQueueBurstsizeMaxVal':h3cOnuPriorityQueueBurstsizeMaxVal,'h3cOnuUpdateByTypeNextIndex':h3cOnuUpdateByTypeNextIndex,'h3cOnuQueueBandwidthTable':h3cOnuQueueBandwidthTable,'h3cOnuQueueBandwidthEntry':h3cOnuQueueBandwidthEntry,'h3cOnuQueueMaxBandwidth':h3cOnuQueueMaxBandwidth,'h3cOnuQueueMaxBurstsize':h3cOnuQueueMaxBurstsize,'h3cOnuQueuePolicyStatus':h3cOnuQueuePolicyStatus,'h3cOnuIpAddressTable':h3cOnuIpAddressTable,'h3cOnuIpAddressEntry':h3cOnuIpAddressEntry,'h3cOnuIpAddress':h3cOnuIpAddress,'h3cOnuIpAddressMask':h3cOnuIpAddressMask,'h3cOnuIpAddressGateway':h3cOnuIpAddressGateway,'h3cOnuDhcpallocate':h3cOnuDhcpallocate,'h3cOnuManageVID':h3cOnuManageVID,'h3cOnuManageVlanIntfS':h3cOnuManageVlanIntfS,'h3cOnuChipSetInfoTable':h3cOnuChipSetInfoTable,'h3cOnuChipSetInfoEntry':h3cOnuChipSetInfoEntry,'h3cOnuChipSetVendorId':h3cOnuChipSetVendorId,'h3cOnuChipSetModel':h3cOnuChipSetModel,'h3cOnuChipSetRevision':h3cOnuChipSetRevision,'h3cOnuChipSetDesignDate':h3cOnuChipSetDesignDate,'h3cOnuCapabilityTable':h3cOnuCapabilityTable,'h3cOnuCapabilityEntry':h3cOnuCapabilityEntry,'h3cOnuServiceSupported':h3cOnuServiceSupported,'h3cOnuGEPortNumber':h3cOnuGEPortNumber,'h3cOnuFEPortNumber':h3cOnuFEPortNumber,'h3cOnuPOTSPortNumber':h3cOnuPOTSPortNumber,'h3cOnuE1PortsNumber':h3cOnuE1PortsNumber,'h3cOnuUpstreamQueueNumber':h3cOnuUpstreamQueueNumber,'h3cOnuMaxUpstreamQueuePerPort':h3cOnuMaxUpstreamQueuePerPort,'h3cOnuDownstreamQueueNumber':h3cOnuDownstreamQueueNumber,'h3cOnuMaxDownstreamQueuePerPort':h3cOnuMaxDownstreamQueuePerPort,'h3cOnuBatteryBackup':h3cOnuBatteryBackup,'h3cOnuIgspFastLeaveSupported':h3cOnuIgspFastLeaveSupported,'h3cOnuMCtrlFastLeaveSupported':h3cOnuMCtrlFastLeaveSupported,'h3cOnuDbaReportTable':h3cOnuDbaReportTable,'h3cOnuDbaReportEntry':h3cOnuDbaReportEntry,_w:h3cOnuDbaReportQueueId,'h3cOnuDbaReportThreshold':h3cOnuDbaReportThreshold,'h3cOnuDbaReportStatus':h3cOnuDbaReportStatus,'h3cOnuCosToLocalPrecedenceTable':h3cOnuCosToLocalPrecedenceTable,'h3cOnuCosToLocalPrecedenceEntry':h3cOnuCosToLocalPrecedenceEntry,_x:h3cOnuCosToLocalPrecedenceCosIndex,'h3cOnuCosToLocalPrecedenceValue':h3cOnuCosToLocalPrecedenceValue,'h3cEponOnuStpPortTable':h3cEponOnuStpPortTable,'h3cEponOnuStpPortEntry':h3cEponOnuStpPortEntry,_b:h3cEponStpPortIndex,_AG:h3cEponStpPortDescr,_AH:h3cEponStpPortState,'h3cOnuPhysicalTable':h3cOnuPhysicalTable,'h3cOnuPhysicalEntry':h3cOnuPhysicalEntry,'h3cOnuBridgeMac':h3cOnuBridgeMac,'h3cOnuFirstPonMac':h3cOnuFirstPonMac,'h3cOnuFirstPonRegState':h3cOnuFirstPonRegState,'h3cOnuSecondPonMac':h3cOnuSecondPonMac,'h3cOnuSecondPonRegState':h3cOnuSecondPonRegState,'h3cOnuSmlkTable':h3cOnuSmlkTable,'h3cOnuSmlkEntry':h3cOnuSmlkEntry,_c:h3cOnuSmlkGroupID,'h3cOnuSmlkFirstPonRole':h3cOnuSmlkFirstPonRole,_AJ:h3cOnuSmlkFirstPonStatus,'h3cOnuSmlkSecondPonRole':h3cOnuSmlkSecondPonRole,_AK:h3cOnuSmlkSecondPonStatus,'h3cOnuRS485PropertiesTable':h3cOnuRS485PropertiesTable,'h3cOnuRS485PropertiesEntry':h3cOnuRS485PropertiesEntry,_S:h3cOnuRS485SerialIndex,'h3cOnuRS485BaudRate':h3cOnuRS485BaudRate,'h3cOnuRS485DataBits':h3cOnuRS485DataBits,'h3cOnuRS485Parity':h3cOnuRS485Parity,'h3cOnuRS485StopBits':h3cOnuRS485StopBits,'h3cOnuRS485FlowControl':h3cOnuRS485FlowControl,'h3cOnuRS485TXOctets':h3cOnuRS485TXOctets,'h3cOnuRS485RXOctets':h3cOnuRS485RXOctets,'h3cOnuRS485TXErrOctets':h3cOnuRS485TXErrOctets,'h3cOnuRS485RXErrOctets':h3cOnuRS485RXErrOctets,'h3cOnuRS485ResetStatistics':h3cOnuRS485ResetStatistics,'h3cOnuRS485SessionSummaryTable':h3cOnuRS485SessionSummaryTable,'h3cOnuRS485SessionSummaryEntry':h3cOnuRS485SessionSummaryEntry,'h3cOnuRS485SessionMaxNum':h3cOnuRS485SessionMaxNum,'h3cOnuRS485SessionNextIndex':h3cOnuRS485SessionNextIndex,'h3cOnuRS485SessionTable':h3cOnuRS485SessionTable,'h3cOnuRS485SessionEntry':h3cOnuRS485SessionEntry,_d:h3cOnuRS485SessionIndex,'h3cOnuRS485SessionType':h3cOnuRS485SessionType,'h3cOnuRS485SessionAddType':h3cOnuRS485SessionAddType,'h3cOnuRS485SessionRemoteIP':h3cOnuRS485SessionRemoteIP,'h3cOnuRS485SessionRemotePort':h3cOnuRS485SessionRemotePort,'h3cOnuRS485SessionLocalPort':h3cOnuRS485SessionLocalPort,'h3cOnuRS485SessionRowStatus':h3cOnuRS485SessionRowStatus,'h3cOnuRS485SessionErrInfoTable':h3cOnuRS485SessionErrInfoTable,'h3cOnuRS485SessionErrInfoEntry':h3cOnuRS485SessionErrInfoEntry,'h3cOnuRS485SessionErrInfo':h3cOnuRS485SessionErrInfo,'h3cEponBatchOperationMan':h3cEponBatchOperationMan,'h3cEponBatchOperationBySlotTable':h3cEponBatchOperationBySlotTable,'h3cEponBatchOperationBySlotEntry':h3cEponBatchOperationBySlotEntry,_A0:h3cEponBatchOperationBySlotIndex,'h3cEponBatchOperationBySlotType':h3cEponBatchOperationBySlotType,'h3cEponBatchOperationBySlot':h3cEponBatchOperationBySlot,'h3cEponBatchOperationBySlotResult':h3cEponBatchOperationBySlotResult,'h3cEponBatchOperationByOLTTable':h3cEponBatchOperationByOLTTable,'h3cEponBatchOperationByOLTEntry':h3cEponBatchOperationByOLTEntry,'h3cEponBatchOperationByOLTType':h3cEponBatchOperationByOLTType,'h3cEponBatchOperationByOLT':h3cEponBatchOperationByOLT,'h3cEponBatchOperationByOLTResult':h3cEponBatchOperationByOLTResult,'h3cOnuFirmwareUpdateByTypeTable':h3cOnuFirmwareUpdateByTypeTable,'h3cOnuFirmwareUpdateByTypeEntry':h3cOnuFirmwareUpdateByTypeEntry,_A3:h3cOnuUpdateByOnuTypeIndex,'h3cOnuUpdateByTypeOnuType':h3cOnuUpdateByTypeOnuType,'h3cOnuUpdateByTypeFileName':h3cOnuUpdateByTypeFileName,'h3cOnuUpdateByTypeRowStatus':h3cOnuUpdateByTypeRowStatus,'h3cEponErrorInfo':h3cEponErrorInfo,_i:h3cEponSoftwareErrorCode,_h:h3cOamVendorSpecificAlarmCode,_g:h3cEponOnuRegErrorMacAddr,_j:h3cOamEventLogType,_k:h3cOamEventLogLocation,_AA:h3cEponLoopbackPortIndex,_AB:h3cEponLoopbackPortDescr,_A8:h3cOltPortAlarmLlidMisFrames,_A4:h3cOltPortAlarmBer,_A6:h3cOltPortAlarmFer,_l:h3cEponOnuRegSilentMac,_AF:h3cEponOperationResult,_AI:h3cEponOnuLaserState,'h3cEponTrap':h3cEponTrap,'h3cEponTrapPrefix':h3cEponTrapPrefix,'h3cEponPortAlarmBerTrap':h3cEponPortAlarmBerTrap,'h3cEponPortAlarmFerTrap':h3cEponPortAlarmFerTrap,'h3cEponErrorLLIDFrameTrap':h3cEponErrorLLIDFrameTrap,'h3cEponLoopBackEnableTrap':h3cEponLoopBackEnableTrap,'h3cEponOnuRegistrationErrTrap':h3cEponOnuRegistrationErrTrap,'h3cEponOamDisconnectionTrap':h3cEponOamDisconnectionTrap,'h3cEponEncryptionKeyErrTrap':h3cEponEncryptionKeyErrTrap,'h3cEponRemoteStableTrap':h3cEponRemoteStableTrap,'h3cEponLocalStableTrap':h3cEponLocalStableTrap,'h3cEponOamVendorSpecificTrap':h3cEponOamVendorSpecificTrap,'h3cEponSoftwareErrTrap':h3cEponSoftwareErrTrap,'h3cEponPortAlarmBerRecoverTrap':h3cEponPortAlarmBerRecoverTrap,'h3cEponPortAlarmFerRecoverTrap':h3cEponPortAlarmFerRecoverTrap,'h3cEponErrorLLIDFrameRecoverTrap':h3cEponErrorLLIDFrameRecoverTrap,'h3cEponLoopBackEnableRecoverTrap':h3cEponLoopBackEnableRecoverTrap,'h3cEponOnuRegistrationErrRecoverTrap':h3cEponOnuRegistrationErrRecoverTrap,'h3cEponOamDisconnectionRecoverTrap':h3cEponOamDisconnectionRecoverTrap,'h3cEponEncryptionKeyErrRecoverTrap':h3cEponEncryptionKeyErrRecoverTrap,'h3cEponRemoteStableRecoverTrap':h3cEponRemoteStableRecoverTrap,'h3cEponLocalStableRecoverTrap':h3cEponLocalStableRecoverTrap,'h3cEponOamVendorSpecificRecoverTrap':h3cEponOamVendorSpecificRecoverTrap,'h3cEponSoftwareErrRecoverTrap':h3cEponSoftwareErrRecoverTrap,'h3cDot3OamThresholdRecoverEvent':h3cDot3OamThresholdRecoverEvent,'h3cDot3OamNonThresholdRecoverEvent':h3cDot3OamNonThresholdRecoverEvent,'h3cEponOnuRegExcessTrap':h3cEponOnuRegExcessTrap,'h3cEponOnuRegExcessRecoverTrap':h3cEponOnuRegExcessRecoverTrap,'h3cEponOnuPowerOffTrap':h3cEponOnuPowerOffTrap,'h3cEponOltSwitchoverTrap':h3cEponOltSwitchoverTrap,'h3cEponOltDFETrap':h3cEponOltDFETrap,'h3cEponOltDFERecoverTrap':h3cEponOltDFERecoverTrap,'h3cEponOnuSilenceTrap':h3cEponOnuSilenceTrap,'h3cEponOnuSilenceRecoverTrap':h3cEponOnuSilenceRecoverTrap,'h3cEponOnuUpdateResultTrap':h3cEponOnuUpdateResultTrap,'h3cEponOnuAutoBindTrap':h3cEponOnuAutoBindTrap,'h3cEponOnuPortStpStateTrap':h3cEponOnuPortStpStateTrap,'h3cEponOnuLaserFailedTrap':h3cEponOnuLaserFailedTrap,'h3cOnuSmlkSwitchoverTrap':h3cOnuSmlkSwitchoverTrap,'h3cEponStat':h3cEponStat,'h3cEponStatTable':h3cEponStatTable,'h3cEponStatEntry':h3cEponStatEntry,'h3cEponStatFER':h3cEponStatFER,'h3cEponStatBER':h3cEponStatBER})