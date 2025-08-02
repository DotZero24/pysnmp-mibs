_AK='hpnicfOnuSmlkSecondPonStatus'
_AJ='hpnicfOnuSmlkFirstPonStatus'
_AI='hpnicfEponOnuLaserState'
_AH='hpnicfEponStpPortState'
_AG='hpnicfEponStpPortDescr'
_AF='hpnicfEponOperationResult'
_AE='hpnicfOnuUpdateFileName'
_AD='hpnicfOnuRegType'
_AC='hpnicfOnuUpdateResult'
_AB='hpnicfEponLoopbackPortDescr'
_AA='hpnicfEponLoopbackPortIndex'
_A9='hpnicfOltPortAlarmLlidMismatchThreshold'
_A8='hpnicfOltPortAlarmLlidMisFrames'
_A7='hpnicfOltPortAlarmFerThreshold'
_A6='hpnicfOltPortAlarmFer'
_A5='hpnicfOltPortAlarmBerThreshold'
_A4='hpnicfOltPortAlarmBer'
_A3='hpnicfOnuUpdateByOnuTypeIndex'
_A2='updateONU'
_A1='resetUnknown'
_A0='hpnicfEponBatchOperationBySlotIndex'
_z='absent'
_y='notExist'
_x='hpnicfOnuCosToLocalPrecedenceCosIndex'
_w='hpnicfOnuDbaReportQueueId'
_v='hpnicfEponOnuTypeIndex'
_u='hpnicfOnuMacIndex'
_t='hpnicfOltUsingOnuNum'
_s='hpnicfOnuSilentMacAddr'
_r='notSetFilename'
_q='fileNotExist'
_p='update'
_o='hpnicfEponMulticastVlanId'
_n='hpnicfEponOuiIndex'
_m='hpnicfOnuBindMacAddress'
_l='hpnicfEponOnuRegSilentMac'
_k='hpnicfOamEventLogLocation'
_j='hpnicfOamEventLogType'
_i='hpnicfEponSoftwareErrorCode'
_h='hpnicfOamVendorSpecificAlarmCode'
_g='hpnicfEponOnuRegErrorMacAddr'
_f='hpnicfOltPortAlarmFerDirect'
_e='hpnicfOltPortAlarmBerDirect'
_d='hpnicfOnuRS485SessionIndex'
_c='hpnicfOnuSmlkGroupID'
_b='hpnicfEponStpPortIndex'
_a='hpnicfOnuQueueId'
_Z='hpnicfOnuQueueDirection'
_Y='fail'
_X='DisplayString'
_W='hpnicfLswSlotIndex'
_V='hpnicfLswFrameIndex'
_U='null'
_T='down'
_S='hpnicfOnuRS485SerialIndex'
_R='other'
_Q='hpnicfEponSlotIndex'
_P='HPN-ICF-LSW-DEV-ADM-MIB'
_O='disable'
_N='enable'
_M='not-accessible'
_L='OctetString'
_K='read-create'
_J='accessible-for-notify'
_I='ifDescr'
_H='TruthValue'
_G='HPN-ICF-EPON-MIB'
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
hpnicfLswFrameIndex,hpnicfLswSlotIndex=mibBuilder.importSymbols(_P,_V,_W)
hpnicfEpon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfEpon')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_I,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_X,'MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
hpnicfEponMibObjects=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1))
_HpnicfEponSysMan_ObjectIdentity=ObjectIdentity
hpnicfEponSysMan=_HpnicfEponSysMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1))
class _HpnicfEponAutoAuthorize_Type(TruthValue):defaultValue=2
_HpnicfEponAutoAuthorize_Type.__name__=_H
_HpnicfEponAutoAuthorize_Object=MibScalar
hpnicfEponAutoAuthorize=_HpnicfEponAutoAuthorize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,1),_HpnicfEponAutoAuthorize_Type())
hpnicfEponAutoAuthorize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutoAuthorize.setStatus(_A)
_HpnicfEponMonitorCycle_Type=Integer32
_HpnicfEponMonitorCycle_Object=MibScalar
hpnicfEponMonitorCycle=_HpnicfEponMonitorCycle_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,2),_HpnicfEponMonitorCycle_Type())
hpnicfEponMonitorCycle.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponMonitorCycle.setStatus(_A)
class _HpnicfEponMsgTimeOut_Type(Integer32):defaultValue=600
_HpnicfEponMsgTimeOut_Type.__name__=_E
_HpnicfEponMsgTimeOut_Object=MibScalar
hpnicfEponMsgTimeOut=_HpnicfEponMsgTimeOut_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,3),_HpnicfEponMsgTimeOut_Type())
hpnicfEponMsgTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponMsgTimeOut.setStatus(_A)
class _HpnicfEponMsgLoseNum_Type(Integer32):defaultValue=20
_HpnicfEponMsgLoseNum_Type.__name__=_E
_HpnicfEponMsgLoseNum_Object=MibScalar
hpnicfEponMsgLoseNum=_HpnicfEponMsgLoseNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,4),_HpnicfEponMsgLoseNum_Type())
hpnicfEponMsgLoseNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponMsgLoseNum.setStatus(_A)
_HpnicfEponSysHasEPONBoard_Type=TruthValue
_HpnicfEponSysHasEPONBoard_Object=MibScalar
hpnicfEponSysHasEPONBoard=_HpnicfEponSysHasEPONBoard_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,5),_HpnicfEponSysHasEPONBoard_Type())
hpnicfEponSysHasEPONBoard.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponSysHasEPONBoard.setStatus(_A)
class _HpnicfEponMonitorCycleEnable_Type(TruthValue):defaultValue=1
_HpnicfEponMonitorCycleEnable_Type.__name__=_H
_HpnicfEponMonitorCycleEnable_Object=MibScalar
hpnicfEponMonitorCycleEnable=_HpnicfEponMonitorCycleEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,6),_HpnicfEponMonitorCycleEnable_Type())
hpnicfEponMonitorCycleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponMonitorCycleEnable.setStatus(_A)
class _HpnicfEponOltSoftwareErrAlmEnable_Type(TruthValue):defaultValue=1
_HpnicfEponOltSoftwareErrAlmEnable_Type.__name__=_H
_HpnicfEponOltSoftwareErrAlmEnable_Object=MibScalar
hpnicfEponOltSoftwareErrAlmEnable=_HpnicfEponOltSoftwareErrAlmEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,7),_HpnicfEponOltSoftwareErrAlmEnable_Type())
hpnicfEponOltSoftwareErrAlmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponOltSoftwareErrAlmEnable.setStatus(_A)
class _HpnicfEponPortLoopBackAlmEnable_Type(TruthValue):defaultValue=1
_HpnicfEponPortLoopBackAlmEnable_Type.__name__=_H
_HpnicfEponPortLoopBackAlmEnable_Object=MibScalar
hpnicfEponPortLoopBackAlmEnable=_HpnicfEponPortLoopBackAlmEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,8),_HpnicfEponPortLoopBackAlmEnable_Type())
hpnicfEponPortLoopBackAlmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponPortLoopBackAlmEnable.setStatus(_A)
_HpnicfEponMonitorCycleMinVal_Type=Integer32
_HpnicfEponMonitorCycleMinVal_Object=MibScalar
hpnicfEponMonitorCycleMinVal=_HpnicfEponMonitorCycleMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,9),_HpnicfEponMonitorCycleMinVal_Type())
hpnicfEponMonitorCycleMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponMonitorCycleMinVal.setStatus(_A)
_HpnicfEponMonitorCycleMaxVal_Type=Integer32
_HpnicfEponMonitorCycleMaxVal_Object=MibScalar
hpnicfEponMonitorCycleMaxVal=_HpnicfEponMonitorCycleMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,10),_HpnicfEponMonitorCycleMaxVal_Type())
hpnicfEponMonitorCycleMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponMonitorCycleMaxVal.setStatus(_A)
_HpnicfEponMsgTimeOutMinVal_Type=Integer32
_HpnicfEponMsgTimeOutMinVal_Object=MibScalar
hpnicfEponMsgTimeOutMinVal=_HpnicfEponMsgTimeOutMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,11),_HpnicfEponMsgTimeOutMinVal_Type())
hpnicfEponMsgTimeOutMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponMsgTimeOutMinVal.setStatus(_A)
_HpnicfEponMsgTimeOutMaxVal_Type=Integer32
_HpnicfEponMsgTimeOutMaxVal_Object=MibScalar
hpnicfEponMsgTimeOutMaxVal=_HpnicfEponMsgTimeOutMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,12),_HpnicfEponMsgTimeOutMaxVal_Type())
hpnicfEponMsgTimeOutMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponMsgTimeOutMaxVal.setStatus(_A)
_HpnicfEponMsgLoseNumMinVal_Type=Integer32
_HpnicfEponMsgLoseNumMinVal_Object=MibScalar
hpnicfEponMsgLoseNumMinVal=_HpnicfEponMsgLoseNumMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,13),_HpnicfEponMsgLoseNumMinVal_Type())
hpnicfEponMsgLoseNumMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponMsgLoseNumMinVal.setStatus(_A)
_HpnicfEponMsgLoseNumMaxVal_Type=Integer32
_HpnicfEponMsgLoseNumMaxVal_Object=MibScalar
hpnicfEponMsgLoseNumMaxVal=_HpnicfEponMsgLoseNumMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,14),_HpnicfEponMsgLoseNumMaxVal_Type())
hpnicfEponMsgLoseNumMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponMsgLoseNumMaxVal.setStatus(_A)
_HpnicfEponSysScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfEponSysScalarGroup=_HpnicfEponSysScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,15))
_HpnicfEponSysManTable_Object=MibTable
hpnicfEponSysManTable=_HpnicfEponSysManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16))
if mibBuilder.loadTexts:hpnicfEponSysManTable.setStatus(_A)
_HpnicfEponSysManEntry_Object=MibTableRow
hpnicfEponSysManEntry=_HpnicfEponSysManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1))
hpnicfEponSysManEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:hpnicfEponSysManEntry.setStatus(_A)
_HpnicfEponSlotIndex_Type=Integer32
_HpnicfEponSlotIndex_Object=MibTableColumn
hpnicfEponSlotIndex=_HpnicfEponSlotIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1,1),_HpnicfEponSlotIndex_Type())
hpnicfEponSlotIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfEponSlotIndex.setStatus(_A)
class _HpnicfEponModeSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cmode',1),('hmode',2)))
_HpnicfEponModeSwitch_Type.__name__=_E
_HpnicfEponModeSwitch_Object=MibTableColumn
hpnicfEponModeSwitch=_HpnicfEponModeSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1,2),_HpnicfEponModeSwitch_Type())
hpnicfEponModeSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponModeSwitch.setStatus(_A)
class _HpnicfEponAutomaticMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponAutomaticMode_Type.__name__=_E
_HpnicfEponAutomaticMode_Object=MibTableColumn
hpnicfEponAutomaticMode=_HpnicfEponAutomaticMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1,3),_HpnicfEponAutomaticMode_Type())
hpnicfEponAutomaticMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutomaticMode.setStatus(_A)
class _HpnicfEponOamDiscoveryTimeout_Type(Integer32):defaultValue=30
_HpnicfEponOamDiscoveryTimeout_Type.__name__=_E
_HpnicfEponOamDiscoveryTimeout_Object=MibTableColumn
hpnicfEponOamDiscoveryTimeout=_HpnicfEponOamDiscoveryTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1,4),_HpnicfEponOamDiscoveryTimeout_Type())
hpnicfEponOamDiscoveryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponOamDiscoveryTimeout.setStatus(_A)
class _HpnicfEponEncryptionNoReplyTimeOut_Type(Integer32):defaultValue=30
_HpnicfEponEncryptionNoReplyTimeOut_Type.__name__=_E
_HpnicfEponEncryptionNoReplyTimeOut_Object=MibTableColumn
hpnicfEponEncryptionNoReplyTimeOut=_HpnicfEponEncryptionNoReplyTimeOut_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1,5),_HpnicfEponEncryptionNoReplyTimeOut_Type())
hpnicfEponEncryptionNoReplyTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponEncryptionNoReplyTimeOut.setStatus(_A)
class _HpnicfEponEncryptionUpdateTime_Type(Integer32):defaultValue=10
_HpnicfEponEncryptionUpdateTime_Type.__name__=_E
_HpnicfEponEncryptionUpdateTime_Object=MibTableColumn
hpnicfEponEncryptionUpdateTime=_HpnicfEponEncryptionUpdateTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1,6),_HpnicfEponEncryptionUpdateTime_Type())
hpnicfEponEncryptionUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponEncryptionUpdateTime.setStatus(_A)
class _HpnicfEponAutoBindStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponAutoBindStatus_Type.__name__=_E
_HpnicfEponAutoBindStatus_Object=MibTableColumn
hpnicfEponAutoBindStatus=_HpnicfEponAutoBindStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,16,1,7),_HpnicfEponAutoBindStatus_Type())
hpnicfEponAutoBindStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutoBindStatus.setStatus(_A)
_HpnicfEponAutoUpdateTable_Object=MibTable
hpnicfEponAutoUpdateTable=_HpnicfEponAutoUpdateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,17))
if mibBuilder.loadTexts:hpnicfEponAutoUpdateTable.setStatus(_A)
_HpnicfEponAutoUpdateEntry_Object=MibTableRow
hpnicfEponAutoUpdateEntry=_HpnicfEponAutoUpdateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,17,1))
hpnicfEponAutoUpdateEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:hpnicfEponAutoUpdateEntry.setStatus(_A)
class _HpnicfEponAutoUpdateFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponAutoUpdateFileName_Type.__name__=_X
_HpnicfEponAutoUpdateFileName_Object=MibTableColumn
hpnicfEponAutoUpdateFileName=_HpnicfEponAutoUpdateFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,17,1,1),_HpnicfEponAutoUpdateFileName_Type())
hpnicfEponAutoUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutoUpdateFileName.setStatus(_A)
class _HpnicfEponAutoUpdateSchedStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponAutoUpdateSchedStatus_Type.__name__=_E
_HpnicfEponAutoUpdateSchedStatus_Object=MibTableColumn
hpnicfEponAutoUpdateSchedStatus=_HpnicfEponAutoUpdateSchedStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,17,1,2),_HpnicfEponAutoUpdateSchedStatus_Type())
hpnicfEponAutoUpdateSchedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutoUpdateSchedStatus.setStatus(_A)
class _HpnicfEponAutoUpdateSchedTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponAutoUpdateSchedTime_Type.__name__=_L
_HpnicfEponAutoUpdateSchedTime_Object=MibTableColumn
hpnicfEponAutoUpdateSchedTime=_HpnicfEponAutoUpdateSchedTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,17,1,3),_HpnicfEponAutoUpdateSchedTime_Type())
hpnicfEponAutoUpdateSchedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutoUpdateSchedTime.setStatus(_A)
class _HpnicfEponAutoUpdateSchedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('daily',1),('weekly',2),('comingdate',3)))
_HpnicfEponAutoUpdateSchedType_Type.__name__=_E
_HpnicfEponAutoUpdateSchedType_Object=MibTableColumn
hpnicfEponAutoUpdateSchedType=_HpnicfEponAutoUpdateSchedType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,17,1,4),_HpnicfEponAutoUpdateSchedType_Type())
hpnicfEponAutoUpdateSchedType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutoUpdateSchedType.setStatus(_A)
class _HpnicfEponAutoUpdateRealTimeStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponAutoUpdateRealTimeStatus_Type.__name__=_E
_HpnicfEponAutoUpdateRealTimeStatus_Object=MibTableColumn
hpnicfEponAutoUpdateRealTimeStatus=_HpnicfEponAutoUpdateRealTimeStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,17,1,5),_HpnicfEponAutoUpdateRealTimeStatus_Type())
hpnicfEponAutoUpdateRealTimeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponAutoUpdateRealTimeStatus.setStatus(_A)
_HpnicfEponOuiIndexNextTable_Object=MibTable
hpnicfEponOuiIndexNextTable=_HpnicfEponOuiIndexNextTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,18))
if mibBuilder.loadTexts:hpnicfEponOuiIndexNextTable.setStatus(_A)
_HpnicfEponOuiIndexNextEntry_Object=MibTableRow
hpnicfEponOuiIndexNextEntry=_HpnicfEponOuiIndexNextEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,18,1))
hpnicfEponOuiIndexNextEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:hpnicfEponOuiIndexNextEntry.setStatus(_A)
_HpnicfEponOuiIndexNext_Type=Integer32
_HpnicfEponOuiIndexNext_Object=MibTableColumn
hpnicfEponOuiIndexNext=_HpnicfEponOuiIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,18,1,1),_HpnicfEponOuiIndexNext_Type())
hpnicfEponOuiIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponOuiIndexNext.setStatus(_A)
_HpnicfEponOuiTable_Object=MibTable
hpnicfEponOuiTable=_HpnicfEponOuiTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,19))
if mibBuilder.loadTexts:hpnicfEponOuiTable.setStatus(_A)
_HpnicfEponOuiEntry_Object=MibTableRow
hpnicfEponOuiEntry=_HpnicfEponOuiEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,19,1))
hpnicfEponOuiEntry.setIndexNames((0,_G,_Q),(0,_G,_n))
if mibBuilder.loadTexts:hpnicfEponOuiEntry.setStatus(_A)
_HpnicfEponOuiIndex_Type=Integer32
_HpnicfEponOuiIndex_Object=MibTableColumn
hpnicfEponOuiIndex=_HpnicfEponOuiIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,19,1,1),_HpnicfEponOuiIndex_Type())
hpnicfEponOuiIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfEponOuiIndex.setStatus(_A)
class _HpnicfEponOuiValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_HpnicfEponOuiValue_Type.__name__=_L
_HpnicfEponOuiValue_Object=MibTableColumn
hpnicfEponOuiValue=_HpnicfEponOuiValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,19,1,2),_HpnicfEponOuiValue_Type())
hpnicfEponOuiValue.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponOuiValue.setStatus(_A)
class _HpnicfEponOamVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponOamVersion_Type.__name__=_L
_HpnicfEponOamVersion_Object=MibTableColumn
hpnicfEponOamVersion=_HpnicfEponOamVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,19,1,3),_HpnicfEponOamVersion_Type())
hpnicfEponOamVersion.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponOamVersion.setStatus(_A)
_HpnicfEponOuiRowStatus_Type=RowStatus
_HpnicfEponOuiRowStatus_Object=MibTableColumn
hpnicfEponOuiRowStatus=_HpnicfEponOuiRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,19,1,4),_HpnicfEponOuiRowStatus_Type())
hpnicfEponOuiRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponOuiRowStatus.setStatus(_A)
_HpnicfEponMulticastControlTable_Object=MibTable
hpnicfEponMulticastControlTable=_HpnicfEponMulticastControlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,20))
if mibBuilder.loadTexts:hpnicfEponMulticastControlTable.setStatus(_A)
_HpnicfEponMulticastControlEntry_Object=MibTableRow
hpnicfEponMulticastControlEntry=_HpnicfEponMulticastControlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,20,1))
hpnicfEponMulticastControlEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:hpnicfEponMulticastControlEntry.setStatus(_A)
_HpnicfEponMulticastVlanId_Type=Integer32
_HpnicfEponMulticastVlanId_Object=MibTableColumn
hpnicfEponMulticastVlanId=_HpnicfEponMulticastVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,20,1,1),_HpnicfEponMulticastVlanId_Type())
hpnicfEponMulticastVlanId.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfEponMulticastVlanId.setStatus(_A)
class _HpnicfEponMulticastAddressList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponMulticastAddressList_Type.__name__=_L
_HpnicfEponMulticastAddressList_Object=MibTableColumn
hpnicfEponMulticastAddressList=_HpnicfEponMulticastAddressList_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,20,1,2),_HpnicfEponMulticastAddressList_Type())
hpnicfEponMulticastAddressList.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponMulticastAddressList.setStatus(_A)
_HpnicfEponMulticastStatus_Type=RowStatus
_HpnicfEponMulticastStatus_Object=MibTableColumn
hpnicfEponMulticastStatus=_HpnicfEponMulticastStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,1,20,1,3),_HpnicfEponMulticastStatus_Type())
hpnicfEponMulticastStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponMulticastStatus.setStatus(_A)
_HpnicfEponFileName_ObjectIdentity=ObjectIdentity
hpnicfEponFileName=_HpnicfEponFileName_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,2))
class _HpnicfEponDbaUpdateFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfEponDbaUpdateFileName_Type.__name__=_L
_HpnicfEponDbaUpdateFileName_Object=MibScalar
hpnicfEponDbaUpdateFileName=_HpnicfEponDbaUpdateFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,2,1),_HpnicfEponDbaUpdateFileName_Type())
hpnicfEponDbaUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponDbaUpdateFileName.setStatus(_A)
class _HpnicfEponOnuUpdateFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfEponOnuUpdateFileName_Type.__name__=_L
_HpnicfEponOnuUpdateFileName_Object=MibScalar
hpnicfEponOnuUpdateFileName=_HpnicfEponOnuUpdateFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,2,2),_HpnicfEponOnuUpdateFileName_Type())
hpnicfEponOnuUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponOnuUpdateFileName.setStatus(_A)
_HpnicfEponOltMan_ObjectIdentity=ObjectIdentity
hpnicfEponOltMan=_HpnicfEponOltMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3))
_HpnicfOltSysManTable_Object=MibTable
hpnicfOltSysManTable=_HpnicfOltSysManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1))
if mibBuilder.loadTexts:hpnicfOltSysManTable.setStatus(_A)
_HpnicfOltSysManEntry_Object=MibTableRow
hpnicfOltSysManEntry=_HpnicfOltSysManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1))
hpnicfOltSysManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOltSysManEntry.setStatus(_A)
class _HpnicfOltLaserOnTime_Type(Integer32):defaultValue=96
_HpnicfOltLaserOnTime_Type.__name__=_E
_HpnicfOltLaserOnTime_Object=MibTableColumn
hpnicfOltLaserOnTime=_HpnicfOltLaserOnTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1,1),_HpnicfOltLaserOnTime_Type())
hpnicfOltLaserOnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltLaserOnTime.setStatus(_A)
class _HpnicfOltLaserOffTime_Type(Integer32):defaultValue=96
_HpnicfOltLaserOffTime_Type.__name__=_E
_HpnicfOltLaserOffTime_Object=MibTableColumn
hpnicfOltLaserOffTime=_HpnicfOltLaserOffTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1,2),_HpnicfOltLaserOffTime_Type())
hpnicfOltLaserOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltLaserOffTime.setStatus(_A)
class _HpnicfOltMultiCopyBrdCast_Type(TruthValue):defaultValue=2
_HpnicfOltMultiCopyBrdCast_Type.__name__=_H
_HpnicfOltMultiCopyBrdCast_Object=MibTableColumn
hpnicfOltMultiCopyBrdCast=_HpnicfOltMultiCopyBrdCast_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1,3),_HpnicfOltMultiCopyBrdCast_Type())
hpnicfOltMultiCopyBrdCast.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltMultiCopyBrdCast.setStatus(_A)
class _HpnicfOltEnableDiscardPacket_Type(TruthValue):defaultValue=2
_HpnicfOltEnableDiscardPacket_Type.__name__=_H
_HpnicfOltEnableDiscardPacket_Object=MibTableColumn
hpnicfOltEnableDiscardPacket=_HpnicfOltEnableDiscardPacket_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1,4),_HpnicfOltEnableDiscardPacket_Type())
hpnicfOltEnableDiscardPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltEnableDiscardPacket.setStatus(_A)
class _HpnicfOltSelfTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('selftest',1))
_HpnicfOltSelfTest_Type.__name__=_E
_HpnicfOltSelfTest_Object=MibTableColumn
hpnicfOltSelfTest=_HpnicfOltSelfTest_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1,5),_HpnicfOltSelfTest_Type())
hpnicfOltSelfTest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltSelfTest.setStatus(_A)
class _HpnicfOltSelfTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('ok',2),(_Y,3)))
_HpnicfOltSelfTestResult_Type.__name__=_E
_HpnicfOltSelfTestResult_Object=MibTableColumn
hpnicfOltSelfTestResult=_HpnicfOltSelfTestResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1,6),_HpnicfOltSelfTestResult_Type())
hpnicfOltSelfTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltSelfTestResult.setStatus(_A)
_HpnicfOltMaxRtt_Type=Unsigned32
_HpnicfOltMaxRtt_Object=MibTableColumn
hpnicfOltMaxRtt=_HpnicfOltMaxRtt_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,1,1,7),_HpnicfOltMaxRtt_Type())
hpnicfOltMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltMaxRtt.setStatus(_A)
_HpnicfOltInfoTable_Object=MibTable
hpnicfOltInfoTable=_HpnicfOltInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2))
if mibBuilder.loadTexts:hpnicfOltInfoTable.setStatus(_A)
_HpnicfOltInfoEntry_Object=MibTableRow
hpnicfOltInfoEntry=_HpnicfOltInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1))
hpnicfOltInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOltInfoEntry.setStatus(_A)
_HpnicfOltFirmMajorVersion_Type=OctetString
_HpnicfOltFirmMajorVersion_Object=MibTableColumn
hpnicfOltFirmMajorVersion=_HpnicfOltFirmMajorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,1),_HpnicfOltFirmMajorVersion_Type())
hpnicfOltFirmMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltFirmMajorVersion.setStatus(_A)
_HpnicfOltFirmMinorVersion_Type=OctetString
_HpnicfOltFirmMinorVersion_Object=MibTableColumn
hpnicfOltFirmMinorVersion=_HpnicfOltFirmMinorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,2),_HpnicfOltFirmMinorVersion_Type())
hpnicfOltFirmMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltFirmMinorVersion.setStatus(_A)
_HpnicfOltHardMajorVersion_Type=OctetString
_HpnicfOltHardMajorVersion_Object=MibTableColumn
hpnicfOltHardMajorVersion=_HpnicfOltHardMajorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,3),_HpnicfOltHardMajorVersion_Type())
hpnicfOltHardMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltHardMajorVersion.setStatus(_A)
_HpnicfOltHardMinorVersion_Type=OctetString
_HpnicfOltHardMinorVersion_Object=MibTableColumn
hpnicfOltHardMinorVersion=_HpnicfOltHardMinorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,4),_HpnicfOltHardMinorVersion_Type())
hpnicfOltHardMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltHardMinorVersion.setStatus(_A)
_HpnicfOltAgcLockTime_Type=Integer32
_HpnicfOltAgcLockTime_Object=MibTableColumn
hpnicfOltAgcLockTime=_HpnicfOltAgcLockTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,5),_HpnicfOltAgcLockTime_Type())
hpnicfOltAgcLockTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltAgcLockTime.setStatus(_A)
_HpnicfOltAgcCdrTime_Type=Integer32
_HpnicfOltAgcCdrTime_Object=MibTableColumn
hpnicfOltAgcCdrTime=_HpnicfOltAgcCdrTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,6),_HpnicfOltAgcCdrTime_Type())
hpnicfOltAgcCdrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltAgcCdrTime.setStatus(_A)
_HpnicfOltMacAddress_Type=MacAddress
_HpnicfOltMacAddress_Object=MibTableColumn
hpnicfOltMacAddress=_HpnicfOltMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,7),_HpnicfOltMacAddress_Type())
hpnicfOltMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltMacAddress.setStatus(_A)
class _HpnicfOltWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('open',2),('reset',3),('closed',4)))
_HpnicfOltWorkMode_Type.__name__=_E
_HpnicfOltWorkMode_Object=MibTableColumn
hpnicfOltWorkMode=_HpnicfOltWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,8),_HpnicfOltWorkMode_Type())
hpnicfOltWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltWorkMode.setStatus(_A)
_HpnicfOltOpticalPowerTx_Type=Integer32
_HpnicfOltOpticalPowerTx_Object=MibTableColumn
hpnicfOltOpticalPowerTx=_HpnicfOltOpticalPowerTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,9),_HpnicfOltOpticalPowerTx_Type())
hpnicfOltOpticalPowerTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltOpticalPowerTx.setStatus(_A)
_HpnicfOltOpticalPowerRx_Type=Integer32
_HpnicfOltOpticalPowerRx_Object=MibTableColumn
hpnicfOltOpticalPowerRx=_HpnicfOltOpticalPowerRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,2,1,10),_HpnicfOltOpticalPowerRx_Type())
hpnicfOltOpticalPowerRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltOpticalPowerRx.setStatus(_A)
_HpnicfOltDbaManTable_Object=MibTable
hpnicfOltDbaManTable=_HpnicfOltDbaManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3))
if mibBuilder.loadTexts:hpnicfOltDbaManTable.setStatus(_A)
_HpnicfOltDbaManEntry_Object=MibTableRow
hpnicfOltDbaManEntry=_HpnicfOltDbaManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1))
hpnicfOltDbaManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOltDbaManEntry.setStatus(_A)
class _HpnicfOltDbaEnabledType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_HpnicfOltDbaEnabledType_Type.__name__=_E
_HpnicfOltDbaEnabledType_Object=MibTableColumn
hpnicfOltDbaEnabledType=_HpnicfOltDbaEnabledType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1,1),_HpnicfOltDbaEnabledType_Type())
hpnicfOltDbaEnabledType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltDbaEnabledType.setStatus(_A)
class _HpnicfOltDbaDiscoveryLength_Type(Integer32):defaultValue=41500
_HpnicfOltDbaDiscoveryLength_Type.__name__=_E
_HpnicfOltDbaDiscoveryLength_Object=MibTableColumn
hpnicfOltDbaDiscoveryLength=_HpnicfOltDbaDiscoveryLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1,2),_HpnicfOltDbaDiscoveryLength_Type())
hpnicfOltDbaDiscoveryLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltDbaDiscoveryLength.setStatus(_A)
class _HpnicfOltDbaDiscovryFrequency_Type(Integer32):defaultValue=50
_HpnicfOltDbaDiscovryFrequency_Type.__name__=_E
_HpnicfOltDbaDiscovryFrequency_Object=MibTableColumn
hpnicfOltDbaDiscovryFrequency=_HpnicfOltDbaDiscovryFrequency_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1,3),_HpnicfOltDbaDiscovryFrequency_Type())
hpnicfOltDbaDiscovryFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltDbaDiscovryFrequency.setStatus(_A)
class _HpnicfOltDbaCycleLength_Type(Integer32):defaultValue=65535
_HpnicfOltDbaCycleLength_Type.__name__=_E
_HpnicfOltDbaCycleLength_Object=MibTableColumn
hpnicfOltDbaCycleLength=_HpnicfOltDbaCycleLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1,4),_HpnicfOltDbaCycleLength_Type())
hpnicfOltDbaCycleLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltDbaCycleLength.setStatus(_A)
_HpnicfOltDbaVersion_Type=OctetString
_HpnicfOltDbaVersion_Object=MibTableColumn
hpnicfOltDbaVersion=_HpnicfOltDbaVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1,5),_HpnicfOltDbaVersion_Type())
hpnicfOltDbaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaVersion.setStatus(_A)
class _HpnicfOltDbaUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_p,1))
_HpnicfOltDbaUpdate_Type.__name__=_E
_HpnicfOltDbaUpdate_Object=MibTableColumn
hpnicfOltDbaUpdate=_HpnicfOltDbaUpdate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1,6),_HpnicfOltDbaUpdate_Type())
hpnicfOltDbaUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltDbaUpdate.setStatus(_A)
class _HpnicfOltDbaUpdateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),('ok',2),(_Y,3),(_q,4),(_r,5)))
_HpnicfOltDbaUpdateResult_Type.__name__=_E
_HpnicfOltDbaUpdateResult_Object=MibTableColumn
hpnicfOltDbaUpdateResult=_HpnicfOltDbaUpdateResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,3,1,7),_HpnicfOltDbaUpdateResult_Type())
hpnicfOltDbaUpdateResult.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaUpdateResult.setStatus(_A)
_HpnicfOltPortAlarmThresholdTable_Object=MibTable
hpnicfOltPortAlarmThresholdTable=_HpnicfOltPortAlarmThresholdTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4))
if mibBuilder.loadTexts:hpnicfOltPortAlarmThresholdTable.setStatus(_A)
_HpnicfOltPortAlarmThresholdEntry_Object=MibTableRow
hpnicfOltPortAlarmThresholdEntry=_HpnicfOltPortAlarmThresholdEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1))
hpnicfOltPortAlarmThresholdEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOltPortAlarmThresholdEntry.setStatus(_A)
class _HpnicfOltPortAlarmBerEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmBerEnabled_Type.__name__=_H
_HpnicfOltPortAlarmBerEnabled_Object=MibTableColumn
hpnicfOltPortAlarmBerEnabled=_HpnicfOltPortAlarmBerEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,1),_HpnicfOltPortAlarmBerEnabled_Type())
hpnicfOltPortAlarmBerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmBerEnabled.setStatus(_A)
class _HpnicfOltPortAlarmBerDirect_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('berUplink',1),('berDownlink',2),('berAll',3)))
_HpnicfOltPortAlarmBerDirect_Type.__name__=_E
_HpnicfOltPortAlarmBerDirect_Object=MibTableColumn
hpnicfOltPortAlarmBerDirect=_HpnicfOltPortAlarmBerDirect_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,2),_HpnicfOltPortAlarmBerDirect_Type())
hpnicfOltPortAlarmBerDirect.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmBerDirect.setStatus(_A)
class _HpnicfOltPortAlarmBerThreshold_Type(Integer32):defaultValue=10
_HpnicfOltPortAlarmBerThreshold_Type.__name__=_E
_HpnicfOltPortAlarmBerThreshold_Object=MibTableColumn
hpnicfOltPortAlarmBerThreshold=_HpnicfOltPortAlarmBerThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,3),_HpnicfOltPortAlarmBerThreshold_Type())
hpnicfOltPortAlarmBerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmBerThreshold.setStatus(_A)
class _HpnicfOltPortAlarmFerEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmFerEnabled_Type.__name__=_H
_HpnicfOltPortAlarmFerEnabled_Object=MibTableColumn
hpnicfOltPortAlarmFerEnabled=_HpnicfOltPortAlarmFerEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,4),_HpnicfOltPortAlarmFerEnabled_Type())
hpnicfOltPortAlarmFerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmFerEnabled.setStatus(_A)
class _HpnicfOltPortAlarmFerDirect_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ferUplink',1),('ferDownlink',2),('ferAll',3)))
_HpnicfOltPortAlarmFerDirect_Type.__name__=_E
_HpnicfOltPortAlarmFerDirect_Object=MibTableColumn
hpnicfOltPortAlarmFerDirect=_HpnicfOltPortAlarmFerDirect_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,5),_HpnicfOltPortAlarmFerDirect_Type())
hpnicfOltPortAlarmFerDirect.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmFerDirect.setStatus(_A)
class _HpnicfOltPortAlarmFerThreshold_Type(Integer32):defaultValue=1
_HpnicfOltPortAlarmFerThreshold_Type.__name__=_E
_HpnicfOltPortAlarmFerThreshold_Object=MibTableColumn
hpnicfOltPortAlarmFerThreshold=_HpnicfOltPortAlarmFerThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,6),_HpnicfOltPortAlarmFerThreshold_Type())
hpnicfOltPortAlarmFerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmFerThreshold.setStatus(_A)
class _HpnicfOltPortAlarmLlidMismatchEnabled_Type(TruthValue):defaultValue=2
_HpnicfOltPortAlarmLlidMismatchEnabled_Type.__name__=_H
_HpnicfOltPortAlarmLlidMismatchEnabled_Object=MibTableColumn
hpnicfOltPortAlarmLlidMismatchEnabled=_HpnicfOltPortAlarmLlidMismatchEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,7),_HpnicfOltPortAlarmLlidMismatchEnabled_Type())
hpnicfOltPortAlarmLlidMismatchEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmLlidMismatchEnabled.setStatus(_A)
class _HpnicfOltPortAlarmLlidMismatchThreshold_Type(Integer32):defaultValue=5000
_HpnicfOltPortAlarmLlidMismatchThreshold_Type.__name__=_E
_HpnicfOltPortAlarmLlidMismatchThreshold_Object=MibTableColumn
hpnicfOltPortAlarmLlidMismatchThreshold=_HpnicfOltPortAlarmLlidMismatchThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,8),_HpnicfOltPortAlarmLlidMismatchThreshold_Type())
hpnicfOltPortAlarmLlidMismatchThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmLlidMismatchThreshold.setStatus(_A)
class _HpnicfOltPortAlarmRemoteStableEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmRemoteStableEnabled_Type.__name__=_H
_HpnicfOltPortAlarmRemoteStableEnabled_Object=MibTableColumn
hpnicfOltPortAlarmRemoteStableEnabled=_HpnicfOltPortAlarmRemoteStableEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,9),_HpnicfOltPortAlarmRemoteStableEnabled_Type())
hpnicfOltPortAlarmRemoteStableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmRemoteStableEnabled.setStatus(_A)
class _HpnicfOltPortAlarmLocalStableEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmLocalStableEnabled_Type.__name__=_H
_HpnicfOltPortAlarmLocalStableEnabled_Object=MibTableColumn
hpnicfOltPortAlarmLocalStableEnabled=_HpnicfOltPortAlarmLocalStableEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,10),_HpnicfOltPortAlarmLocalStableEnabled_Type())
hpnicfOltPortAlarmLocalStableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmLocalStableEnabled.setStatus(_A)
class _HpnicfOltPortAlarmRegistrationEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmRegistrationEnabled_Type.__name__=_H
_HpnicfOltPortAlarmRegistrationEnabled_Object=MibTableColumn
hpnicfOltPortAlarmRegistrationEnabled=_HpnicfOltPortAlarmRegistrationEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,11),_HpnicfOltPortAlarmRegistrationEnabled_Type())
hpnicfOltPortAlarmRegistrationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmRegistrationEnabled.setStatus(_A)
class _HpnicfOltPortAlarmOamDisconnectionEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmOamDisconnectionEnabled_Type.__name__=_H
_HpnicfOltPortAlarmOamDisconnectionEnabled_Object=MibTableColumn
hpnicfOltPortAlarmOamDisconnectionEnabled=_HpnicfOltPortAlarmOamDisconnectionEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,12),_HpnicfOltPortAlarmOamDisconnectionEnabled_Type())
hpnicfOltPortAlarmOamDisconnectionEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmOamDisconnectionEnabled.setStatus(_A)
class _HpnicfOltPortAlarmEncryptionKeyEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmEncryptionKeyEnabled_Type.__name__=_H
_HpnicfOltPortAlarmEncryptionKeyEnabled_Object=MibTableColumn
hpnicfOltPortAlarmEncryptionKeyEnabled=_HpnicfOltPortAlarmEncryptionKeyEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,13),_HpnicfOltPortAlarmEncryptionKeyEnabled_Type())
hpnicfOltPortAlarmEncryptionKeyEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmEncryptionKeyEnabled.setStatus(_A)
class _HpnicfOltPortAlarmVendorSpecificEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmVendorSpecificEnabled_Type.__name__=_H
_HpnicfOltPortAlarmVendorSpecificEnabled_Object=MibTableColumn
hpnicfOltPortAlarmVendorSpecificEnabled=_HpnicfOltPortAlarmVendorSpecificEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,14),_HpnicfOltPortAlarmVendorSpecificEnabled_Type())
hpnicfOltPortAlarmVendorSpecificEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmVendorSpecificEnabled.setStatus(_A)
class _HpnicfOltPortAlarmRegExcessEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmRegExcessEnabled_Type.__name__=_H
_HpnicfOltPortAlarmRegExcessEnabled_Object=MibTableColumn
hpnicfOltPortAlarmRegExcessEnabled=_HpnicfOltPortAlarmRegExcessEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,15),_HpnicfOltPortAlarmRegExcessEnabled_Type())
hpnicfOltPortAlarmRegExcessEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmRegExcessEnabled.setStatus(_A)
class _HpnicfOltPortAlarmDFEEnabled_Type(TruthValue):defaultValue=1
_HpnicfOltPortAlarmDFEEnabled_Type.__name__=_H
_HpnicfOltPortAlarmDFEEnabled_Object=MibTableColumn
hpnicfOltPortAlarmDFEEnabled=_HpnicfOltPortAlarmDFEEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,4,1,16),_HpnicfOltPortAlarmDFEEnabled_Type())
hpnicfOltPortAlarmDFEEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOltPortAlarmDFEEnabled.setStatus(_A)
_HpnicfOltLaserOnTimeMinVal_Type=Integer32
_HpnicfOltLaserOnTimeMinVal_Object=MibScalar
hpnicfOltLaserOnTimeMinVal=_HpnicfOltLaserOnTimeMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,5),_HpnicfOltLaserOnTimeMinVal_Type())
hpnicfOltLaserOnTimeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltLaserOnTimeMinVal.setStatus(_A)
_HpnicfOltLaserOnTimeMaxVal_Type=Integer32
_HpnicfOltLaserOnTimeMaxVal_Object=MibScalar
hpnicfOltLaserOnTimeMaxVal=_HpnicfOltLaserOnTimeMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,6),_HpnicfOltLaserOnTimeMaxVal_Type())
hpnicfOltLaserOnTimeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltLaserOnTimeMaxVal.setStatus(_A)
_HpnicfOltLaserOffTimeMinVal_Type=Integer32
_HpnicfOltLaserOffTimeMinVal_Object=MibScalar
hpnicfOltLaserOffTimeMinVal=_HpnicfOltLaserOffTimeMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,7),_HpnicfOltLaserOffTimeMinVal_Type())
hpnicfOltLaserOffTimeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltLaserOffTimeMinVal.setStatus(_A)
_HpnicfOltLaserOffTimeMaxVal_Type=Integer32
_HpnicfOltLaserOffTimeMaxVal_Object=MibScalar
hpnicfOltLaserOffTimeMaxVal=_HpnicfOltLaserOffTimeMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,8),_HpnicfOltLaserOffTimeMaxVal_Type())
hpnicfOltLaserOffTimeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltLaserOffTimeMaxVal.setStatus(_A)
_HpnicfOltDbaDiscoveryLengthMinVal_Type=Integer32
_HpnicfOltDbaDiscoveryLengthMinVal_Object=MibScalar
hpnicfOltDbaDiscoveryLengthMinVal=_HpnicfOltDbaDiscoveryLengthMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,9),_HpnicfOltDbaDiscoveryLengthMinVal_Type())
hpnicfOltDbaDiscoveryLengthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaDiscoveryLengthMinVal.setStatus(_A)
_HpnicfOltDbaDiscoveryLengthMaxVal_Type=Integer32
_HpnicfOltDbaDiscoveryLengthMaxVal_Object=MibScalar
hpnicfOltDbaDiscoveryLengthMaxVal=_HpnicfOltDbaDiscoveryLengthMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,10),_HpnicfOltDbaDiscoveryLengthMaxVal_Type())
hpnicfOltDbaDiscoveryLengthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaDiscoveryLengthMaxVal.setStatus(_A)
_HpnicfOltDbaDiscovryFrequencyMinVal_Type=Integer32
_HpnicfOltDbaDiscovryFrequencyMinVal_Object=MibScalar
hpnicfOltDbaDiscovryFrequencyMinVal=_HpnicfOltDbaDiscovryFrequencyMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,11),_HpnicfOltDbaDiscovryFrequencyMinVal_Type())
hpnicfOltDbaDiscovryFrequencyMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaDiscovryFrequencyMinVal.setStatus(_A)
_HpnicfOltDbaDiscovryFrequencyMaxVal_Type=Integer32
_HpnicfOltDbaDiscovryFrequencyMaxVal_Object=MibScalar
hpnicfOltDbaDiscovryFrequencyMaxVal=_HpnicfOltDbaDiscovryFrequencyMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,12),_HpnicfOltDbaDiscovryFrequencyMaxVal_Type())
hpnicfOltDbaDiscovryFrequencyMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaDiscovryFrequencyMaxVal.setStatus(_A)
_HpnicfOltDbaCycleLengthMinVal_Type=Integer32
_HpnicfOltDbaCycleLengthMinVal_Object=MibScalar
hpnicfOltDbaCycleLengthMinVal=_HpnicfOltDbaCycleLengthMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,13),_HpnicfOltDbaCycleLengthMinVal_Type())
hpnicfOltDbaCycleLengthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaCycleLengthMinVal.setStatus(_A)
_HpnicfOltDbaCycleLengthMaxVal_Type=Integer32
_HpnicfOltDbaCycleLengthMaxVal_Object=MibScalar
hpnicfOltDbaCycleLengthMaxVal=_HpnicfOltDbaCycleLengthMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,14),_HpnicfOltDbaCycleLengthMaxVal_Type())
hpnicfOltDbaCycleLengthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltDbaCycleLengthMaxVal.setStatus(_A)
_HpnicfOltPortAlarmLlidMisMinVal_Type=Integer32
_HpnicfOltPortAlarmLlidMisMinVal_Object=MibScalar
hpnicfOltPortAlarmLlidMisMinVal=_HpnicfOltPortAlarmLlidMisMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,15),_HpnicfOltPortAlarmLlidMisMinVal_Type())
hpnicfOltPortAlarmLlidMisMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltPortAlarmLlidMisMinVal.setStatus(_A)
_HpnicfOltPortAlarmLlidMisMaxVal_Type=Integer32
_HpnicfOltPortAlarmLlidMisMaxVal_Object=MibScalar
hpnicfOltPortAlarmLlidMisMaxVal=_HpnicfOltPortAlarmLlidMisMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,16),_HpnicfOltPortAlarmLlidMisMaxVal_Type())
hpnicfOltPortAlarmLlidMisMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltPortAlarmLlidMisMaxVal.setStatus(_A)
_HpnicfOltPortAlarmBerMinVal_Type=Integer32
_HpnicfOltPortAlarmBerMinVal_Object=MibScalar
hpnicfOltPortAlarmBerMinVal=_HpnicfOltPortAlarmBerMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,17),_HpnicfOltPortAlarmBerMinVal_Type())
hpnicfOltPortAlarmBerMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltPortAlarmBerMinVal.setStatus(_A)
_HpnicfOltPortAlarmBerMaxVal_Type=Integer32
_HpnicfOltPortAlarmBerMaxVal_Object=MibScalar
hpnicfOltPortAlarmBerMaxVal=_HpnicfOltPortAlarmBerMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,18),_HpnicfOltPortAlarmBerMaxVal_Type())
hpnicfOltPortAlarmBerMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltPortAlarmBerMaxVal.setStatus(_A)
_HpnicfOltPortAlarmFerMinVal_Type=Integer32
_HpnicfOltPortAlarmFerMinVal_Object=MibScalar
hpnicfOltPortAlarmFerMinVal=_HpnicfOltPortAlarmFerMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,19),_HpnicfOltPortAlarmFerMinVal_Type())
hpnicfOltPortAlarmFerMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltPortAlarmFerMinVal.setStatus(_A)
_HpnicfOltPortAlarmFerMaxVal_Type=Integer32
_HpnicfOltPortAlarmFerMaxVal_Object=MibScalar
hpnicfOltPortAlarmFerMaxVal=_HpnicfOltPortAlarmFerMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,20),_HpnicfOltPortAlarmFerMaxVal_Type())
hpnicfOltPortAlarmFerMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltPortAlarmFerMaxVal.setStatus(_A)
_HpnicfOnuSilentTable_Object=MibTable
hpnicfOnuSilentTable=_HpnicfOnuSilentTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,21))
if mibBuilder.loadTexts:hpnicfOnuSilentTable.setStatus(_A)
_HpnicfOnuSilentEntry_Object=MibTableRow
hpnicfOnuSilentEntry=_HpnicfOnuSilentEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,21,1))
hpnicfOnuSilentEntry.setIndexNames((0,_D,_F),(0,_G,_s))
if mibBuilder.loadTexts:hpnicfOnuSilentEntry.setStatus(_A)
_HpnicfOnuSilentMacAddr_Type=MacAddress
_HpnicfOnuSilentMacAddr_Object=MibTableColumn
hpnicfOnuSilentMacAddr=_HpnicfOnuSilentMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,21,1,1),_HpnicfOnuSilentMacAddr_Type())
hpnicfOnuSilentMacAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuSilentMacAddr.setStatus(_A)
_HpnicfOnuSilentTime_Type=Integer32
_HpnicfOnuSilentTime_Object=MibTableColumn
hpnicfOnuSilentTime=_HpnicfOnuSilentTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,21,1,2),_HpnicfOnuSilentTime_Type())
hpnicfOnuSilentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSilentTime.setStatus(_A)
_HpnicfOltUsingOnuTable_Object=MibTable
hpnicfOltUsingOnuTable=_HpnicfOltUsingOnuTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,22))
if mibBuilder.loadTexts:hpnicfOltUsingOnuTable.setStatus(_A)
_HpnicfOltUsingOnuEntry_Object=MibTableRow
hpnicfOltUsingOnuEntry=_HpnicfOltUsingOnuEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,22,1))
hpnicfOltUsingOnuEntry.setIndexNames((0,_D,_F),(0,_G,_t))
if mibBuilder.loadTexts:hpnicfOltUsingOnuEntry.setStatus(_A)
class _HpnicfOltUsingOnuNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfOltUsingOnuNum_Type.__name__=_E
_HpnicfOltUsingOnuNum_Object=MibTableColumn
hpnicfOltUsingOnuNum=_HpnicfOltUsingOnuNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,22,1,1),_HpnicfOltUsingOnuNum_Type())
hpnicfOltUsingOnuNum.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOltUsingOnuNum.setStatus(_A)
_HpnicfOltUsingOnuIfIndex_Type=Integer32
_HpnicfOltUsingOnuIfIndex_Object=MibTableColumn
hpnicfOltUsingOnuIfIndex=_HpnicfOltUsingOnuIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,22,1,2),_HpnicfOltUsingOnuIfIndex_Type())
hpnicfOltUsingOnuIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOltUsingOnuIfIndex.setStatus(_A)
_HpnicfOltUsingOnuRowStatus_Type=RowStatus
_HpnicfOltUsingOnuRowStatus_Object=MibTableColumn
hpnicfOltUsingOnuRowStatus=_HpnicfOltUsingOnuRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,3,22,1,3),_HpnicfOltUsingOnuRowStatus_Type())
hpnicfOltUsingOnuRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOltUsingOnuRowStatus.setStatus(_A)
_HpnicfEponOnuMan_ObjectIdentity=ObjectIdentity
hpnicfEponOnuMan=_HpnicfEponOnuMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5))
_HpnicfOnuSysManTable_Object=MibTable
hpnicfOnuSysManTable=_HpnicfOnuSysManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1))
if mibBuilder.loadTexts:hpnicfOnuSysManTable.setStatus(_A)
_HpnicfOnuSysManEntry_Object=MibTableRow
hpnicfOnuSysManEntry=_HpnicfOnuSysManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1))
hpnicfOnuSysManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuSysManEntry.setStatus(_A)
class _HpnicfOnuEncryptMan_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('downlink',2),('updownlink',3)))
_HpnicfOnuEncryptMan_Type.__name__=_E
_HpnicfOnuEncryptMan_Object=MibTableColumn
hpnicfOnuEncryptMan=_HpnicfOnuEncryptMan_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,1),_HpnicfOnuEncryptMan_Type())
hpnicfOnuEncryptMan.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuEncryptMan.setStatus(_A)
class _HpnicfOnuReAuthorize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reAuthorize',1))
_HpnicfOnuReAuthorize_Type.__name__=_E
_HpnicfOnuReAuthorize_Object=MibTableColumn
hpnicfOnuReAuthorize=_HpnicfOnuReAuthorize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,2),_HpnicfOnuReAuthorize_Type())
hpnicfOnuReAuthorize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuReAuthorize.setStatus(_A)
class _HpnicfOnuMulticastFilterStatus_Type(TruthValue):defaultValue=2
_HpnicfOnuMulticastFilterStatus_Type.__name__=_H
_HpnicfOnuMulticastFilterStatus_Object=MibTableColumn
hpnicfOnuMulticastFilterStatus=_HpnicfOnuMulticastFilterStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,3),_HpnicfOnuMulticastFilterStatus_Type())
hpnicfOnuMulticastFilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuMulticastFilterStatus.setStatus(_A)
class _HpnicfOnuDbaReportQueueSetNumber_Type(Integer32):defaultValue=2
_HpnicfOnuDbaReportQueueSetNumber_Type.__name__=_E
_HpnicfOnuDbaReportQueueSetNumber_Object=MibTableColumn
hpnicfOnuDbaReportQueueSetNumber=_HpnicfOnuDbaReportQueueSetNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,4),_HpnicfOnuDbaReportQueueSetNumber_Type())
hpnicfOnuDbaReportQueueSetNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDbaReportQueueSetNumber.setStatus(_A)
class _HpnicfOnuRemoteFecStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfOnuRemoteFecStatus_Type.__name__=_E
_HpnicfOnuRemoteFecStatus_Object=MibTableColumn
hpnicfOnuRemoteFecStatus=_HpnicfOnuRemoteFecStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,5),_HpnicfOnuRemoteFecStatus_Type())
hpnicfOnuRemoteFecStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuRemoteFecStatus.setStatus(_A)
class _HpnicfOnuPortBerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfOnuPortBerStatus_Type.__name__=_E
_HpnicfOnuPortBerStatus_Object=MibTableColumn
hpnicfOnuPortBerStatus=_HpnicfOnuPortBerStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,6),_HpnicfOnuPortBerStatus_Type())
hpnicfOnuPortBerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuPortBerStatus.setStatus(_A)
class _HpnicfOnuReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_HpnicfOnuReset_Type.__name__=_E
_HpnicfOnuReset_Object=MibTableColumn
hpnicfOnuReset=_HpnicfOnuReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,7),_HpnicfOnuReset_Type())
hpnicfOnuReset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuReset.setStatus(_A)
class _HpnicfOnuMulticastControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('igmpsnooping',1),('multicastcontrol',2)))
_HpnicfOnuMulticastControlMode_Type.__name__=_E
_HpnicfOnuMulticastControlMode_Object=MibTableColumn
hpnicfOnuMulticastControlMode=_HpnicfOnuMulticastControlMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,8),_HpnicfOnuMulticastControlMode_Type())
hpnicfOnuMulticastControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuMulticastControlMode.setStatus(_A)
_HpnicfOnuAccessVlan_Type=Integer32
_HpnicfOnuAccessVlan_Object=MibTableColumn
hpnicfOnuAccessVlan=_HpnicfOnuAccessVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,9),_HpnicfOnuAccessVlan_Type())
hpnicfOnuAccessVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuAccessVlan.setStatus(_A)
class _HpnicfOnuEncryptKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfOnuEncryptKey_Type.__name__=_X
_HpnicfOnuEncryptKey_Object=MibTableColumn
hpnicfOnuEncryptKey=_HpnicfOnuEncryptKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,10),_HpnicfOnuEncryptKey_Type())
hpnicfOnuEncryptKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuEncryptKey.setStatus(_A)
class _HpnicfOnuUniUpDownTrapStatus_Type(TruthValue):defaultValue=2
_HpnicfOnuUniUpDownTrapStatus_Type.__name__=_H
_HpnicfOnuUniUpDownTrapStatus_Object=MibTableColumn
hpnicfOnuUniUpDownTrapStatus=_HpnicfOnuUniUpDownTrapStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,11),_HpnicfOnuUniUpDownTrapStatus_Type())
hpnicfOnuUniUpDownTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuUniUpDownTrapStatus.setStatus(_A)
class _HpnicfOnuFecStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfOnuFecStatus_Type.__name__=_E
_HpnicfOnuFecStatus_Object=MibTableColumn
hpnicfOnuFecStatus=_HpnicfOnuFecStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,12),_HpnicfOnuFecStatus_Type())
hpnicfOnuFecStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuFecStatus.setStatus(_A)
_HpnicfOnuMcastCtrlHostAgingTime_Type=Integer32
_HpnicfOnuMcastCtrlHostAgingTime_Object=MibTableColumn
hpnicfOnuMcastCtrlHostAgingTime=_HpnicfOnuMcastCtrlHostAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,13),_HpnicfOnuMcastCtrlHostAgingTime_Type())
hpnicfOnuMcastCtrlHostAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuMcastCtrlHostAgingTime.setStatus(_A)
_HpnicfOnuMulticastFastLeaveEnable_Type=TruthValue
_HpnicfOnuMulticastFastLeaveEnable_Object=MibTableColumn
hpnicfOnuMulticastFastLeaveEnable=_HpnicfOnuMulticastFastLeaveEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,14),_HpnicfOnuMulticastFastLeaveEnable_Type())
hpnicfOnuMulticastFastLeaveEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuMulticastFastLeaveEnable.setStatus(_A)
_HpnicfOnuPortIsolateEnable_Type=TruthValue
_HpnicfOnuPortIsolateEnable_Object=MibTableColumn
hpnicfOnuPortIsolateEnable=_HpnicfOnuPortIsolateEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,1,1,15),_HpnicfOnuPortIsolateEnable_Type())
hpnicfOnuPortIsolateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuPortIsolateEnable.setStatus(_A)
_HpnicfOnuLinkTestTable_Object=MibTable
hpnicfOnuLinkTestTable=_HpnicfOnuLinkTestTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2))
if mibBuilder.loadTexts:hpnicfOnuLinkTestTable.setStatus(_A)
_HpnicfOnuLinkTestEntry_Object=MibTableRow
hpnicfOnuLinkTestEntry=_HpnicfOnuLinkTestEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1))
hpnicfOnuLinkTestEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuLinkTestEntry.setStatus(_A)
class _HpnicfOnuLinkTestFrameNum_Type(Integer32):defaultValue=20
_HpnicfOnuLinkTestFrameNum_Type.__name__=_E
_HpnicfOnuLinkTestFrameNum_Object=MibTableColumn
hpnicfOnuLinkTestFrameNum=_HpnicfOnuLinkTestFrameNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,1),_HpnicfOnuLinkTestFrameNum_Type())
hpnicfOnuLinkTestFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuLinkTestFrameNum.setStatus(_A)
class _HpnicfOnuLinkTestFrameSize_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1514))
_HpnicfOnuLinkTestFrameSize_Type.__name__=_E
_HpnicfOnuLinkTestFrameSize_Object=MibTableColumn
hpnicfOnuLinkTestFrameSize=_HpnicfOnuLinkTestFrameSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,2),_HpnicfOnuLinkTestFrameSize_Type())
hpnicfOnuLinkTestFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuLinkTestFrameSize.setStatus(_A)
class _HpnicfOnuLinkTestDelay_Type(TruthValue):defaultValue=1
_HpnicfOnuLinkTestDelay_Type.__name__=_H
_HpnicfOnuLinkTestDelay_Object=MibTableColumn
hpnicfOnuLinkTestDelay=_HpnicfOnuLinkTestDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,3),_HpnicfOnuLinkTestDelay_Type())
hpnicfOnuLinkTestDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuLinkTestDelay.setStatus(_A)
class _HpnicfOnuLinkTestVlanTag_Type(TruthValue):defaultValue=1
_HpnicfOnuLinkTestVlanTag_Type.__name__=_H
_HpnicfOnuLinkTestVlanTag_Object=MibTableColumn
hpnicfOnuLinkTestVlanTag=_HpnicfOnuLinkTestVlanTag_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,4),_HpnicfOnuLinkTestVlanTag_Type())
hpnicfOnuLinkTestVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuLinkTestVlanTag.setStatus(_A)
class _HpnicfOnuLinkTestVlanPriority_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfOnuLinkTestVlanPriority_Type.__name__=_E
_HpnicfOnuLinkTestVlanPriority_Object=MibTableColumn
hpnicfOnuLinkTestVlanPriority=_HpnicfOnuLinkTestVlanPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,5),_HpnicfOnuLinkTestVlanPriority_Type())
hpnicfOnuLinkTestVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuLinkTestVlanPriority.setStatus(_A)
class _HpnicfOnuLinkTestVlanTagID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfOnuLinkTestVlanTagID_Type.__name__=_E
_HpnicfOnuLinkTestVlanTagID_Object=MibTableColumn
hpnicfOnuLinkTestVlanTagID=_HpnicfOnuLinkTestVlanTagID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,6),_HpnicfOnuLinkTestVlanTagID_Type())
hpnicfOnuLinkTestVlanTagID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuLinkTestVlanTagID.setStatus(_A)
_HpnicfOnuLinkTestResultSentFrameNum_Type=Integer32
_HpnicfOnuLinkTestResultSentFrameNum_Object=MibTableColumn
hpnicfOnuLinkTestResultSentFrameNum=_HpnicfOnuLinkTestResultSentFrameNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,7),_HpnicfOnuLinkTestResultSentFrameNum_Type())
hpnicfOnuLinkTestResultSentFrameNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestResultSentFrameNum.setStatus(_A)
_HpnicfOnuLinkTestResultRetFrameNum_Type=Integer32
_HpnicfOnuLinkTestResultRetFrameNum_Object=MibTableColumn
hpnicfOnuLinkTestResultRetFrameNum=_HpnicfOnuLinkTestResultRetFrameNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,8),_HpnicfOnuLinkTestResultRetFrameNum_Type())
hpnicfOnuLinkTestResultRetFrameNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestResultRetFrameNum.setStatus(_A)
_HpnicfOnuLinkTestResultRetErrFrameNum_Type=Integer32
_HpnicfOnuLinkTestResultRetErrFrameNum_Object=MibTableColumn
hpnicfOnuLinkTestResultRetErrFrameNum=_HpnicfOnuLinkTestResultRetErrFrameNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,9),_HpnicfOnuLinkTestResultRetErrFrameNum_Type())
hpnicfOnuLinkTestResultRetErrFrameNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestResultRetErrFrameNum.setStatus(_A)
_HpnicfOnuLinkTestResultMinDelay_Type=Integer32
_HpnicfOnuLinkTestResultMinDelay_Object=MibTableColumn
hpnicfOnuLinkTestResultMinDelay=_HpnicfOnuLinkTestResultMinDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,10),_HpnicfOnuLinkTestResultMinDelay_Type())
hpnicfOnuLinkTestResultMinDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestResultMinDelay.setStatus(_A)
_HpnicfOnuLinkTestResultMeanDelay_Type=Integer32
_HpnicfOnuLinkTestResultMeanDelay_Object=MibTableColumn
hpnicfOnuLinkTestResultMeanDelay=_HpnicfOnuLinkTestResultMeanDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,11),_HpnicfOnuLinkTestResultMeanDelay_Type())
hpnicfOnuLinkTestResultMeanDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestResultMeanDelay.setStatus(_A)
_HpnicfOnuLinkTestResultMaxDelay_Type=Integer32
_HpnicfOnuLinkTestResultMaxDelay_Object=MibTableColumn
hpnicfOnuLinkTestResultMaxDelay=_HpnicfOnuLinkTestResultMaxDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,2,1,12),_HpnicfOnuLinkTestResultMaxDelay_Type())
hpnicfOnuLinkTestResultMaxDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestResultMaxDelay.setStatus(_A)
_HpnicfOnuBandWidthTable_Object=MibTable
hpnicfOnuBandWidthTable=_HpnicfOnuBandWidthTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3))
if mibBuilder.loadTexts:hpnicfOnuBandWidthTable.setStatus(_A)
_HpnicfOnuBandWidthEntry_Object=MibTableRow
hpnicfOnuBandWidthEntry=_HpnicfOnuBandWidthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1))
hpnicfOnuBandWidthEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuBandWidthEntry.setStatus(_A)
class _HpnicfOnuDownStreamBandWidthPolicy_Type(TruthValue):defaultValue=2
_HpnicfOnuDownStreamBandWidthPolicy_Type.__name__=_H
_HpnicfOnuDownStreamBandWidthPolicy_Object=MibTableColumn
hpnicfOnuDownStreamBandWidthPolicy=_HpnicfOnuDownStreamBandWidthPolicy_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,1),_HpnicfOnuDownStreamBandWidthPolicy_Type())
hpnicfOnuDownStreamBandWidthPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDownStreamBandWidthPolicy.setStatus(_A)
class _HpnicfOnuDownStreamMaxBandWidth_Type(Integer32):defaultValue=1000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_HpnicfOnuDownStreamMaxBandWidth_Type.__name__=_E
_HpnicfOnuDownStreamMaxBandWidth_Object=MibTableColumn
hpnicfOnuDownStreamMaxBandWidth=_HpnicfOnuDownStreamMaxBandWidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,2),_HpnicfOnuDownStreamMaxBandWidth_Type())
hpnicfOnuDownStreamMaxBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDownStreamMaxBandWidth.setStatus(_A)
class _HpnicfOnuDownStreamMaxBurstSize_Type(Integer32):defaultValue=8388480;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388480))
_HpnicfOnuDownStreamMaxBurstSize_Type.__name__=_E
_HpnicfOnuDownStreamMaxBurstSize_Object=MibTableColumn
hpnicfOnuDownStreamMaxBurstSize=_HpnicfOnuDownStreamMaxBurstSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,3),_HpnicfOnuDownStreamMaxBurstSize_Type())
hpnicfOnuDownStreamMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDownStreamMaxBurstSize.setStatus(_A)
class _HpnicfOnuDownStreamHighPriorityFirst_Type(TruthValue):defaultValue=2
_HpnicfOnuDownStreamHighPriorityFirst_Type.__name__=_H
_HpnicfOnuDownStreamHighPriorityFirst_Object=MibTableColumn
hpnicfOnuDownStreamHighPriorityFirst=_HpnicfOnuDownStreamHighPriorityFirst_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,4),_HpnicfOnuDownStreamHighPriorityFirst_Type())
hpnicfOnuDownStreamHighPriorityFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDownStreamHighPriorityFirst.setStatus(_A)
class _HpnicfOnuDownStreamShortFrameFirst_Type(TruthValue):defaultValue=2
_HpnicfOnuDownStreamShortFrameFirst_Type.__name__=_H
_HpnicfOnuDownStreamShortFrameFirst_Object=MibTableColumn
hpnicfOnuDownStreamShortFrameFirst=_HpnicfOnuDownStreamShortFrameFirst_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,5),_HpnicfOnuDownStreamShortFrameFirst_Type())
hpnicfOnuDownStreamShortFrameFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDownStreamShortFrameFirst.setStatus(_A)
class _HpnicfOnuP2PBandWidthPolicy_Type(TruthValue):defaultValue=2
_HpnicfOnuP2PBandWidthPolicy_Type.__name__=_H
_HpnicfOnuP2PBandWidthPolicy_Object=MibTableColumn
hpnicfOnuP2PBandWidthPolicy=_HpnicfOnuP2PBandWidthPolicy_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,6),_HpnicfOnuP2PBandWidthPolicy_Type())
hpnicfOnuP2PBandWidthPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuP2PBandWidthPolicy.setStatus(_A)
class _HpnicfOnuP2PMaxBandWidth_Type(Integer32):defaultValue=1000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_HpnicfOnuP2PMaxBandWidth_Type.__name__=_E
_HpnicfOnuP2PMaxBandWidth_Object=MibTableColumn
hpnicfOnuP2PMaxBandWidth=_HpnicfOnuP2PMaxBandWidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,7),_HpnicfOnuP2PMaxBandWidth_Type())
hpnicfOnuP2PMaxBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuP2PMaxBandWidth.setStatus(_A)
class _HpnicfOnuP2PMaxBurstSize_Type(Integer32):defaultValue=8388480;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388480))
_HpnicfOnuP2PMaxBurstSize_Type.__name__=_E
_HpnicfOnuP2PMaxBurstSize_Object=MibTableColumn
hpnicfOnuP2PMaxBurstSize=_HpnicfOnuP2PMaxBurstSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,8),_HpnicfOnuP2PMaxBurstSize_Type())
hpnicfOnuP2PMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuP2PMaxBurstSize.setStatus(_A)
class _HpnicfOnuP2PHighPriorityFirst_Type(TruthValue):defaultValue=2
_HpnicfOnuP2PHighPriorityFirst_Type.__name__=_H
_HpnicfOnuP2PHighPriorityFirst_Object=MibTableColumn
hpnicfOnuP2PHighPriorityFirst=_HpnicfOnuP2PHighPriorityFirst_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,9),_HpnicfOnuP2PHighPriorityFirst_Type())
hpnicfOnuP2PHighPriorityFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuP2PHighPriorityFirst.setStatus(_A)
class _HpnicfOnuP2PShortFrameFirst_Type(TruthValue):defaultValue=2
_HpnicfOnuP2PShortFrameFirst_Type.__name__=_H
_HpnicfOnuP2PShortFrameFirst_Object=MibTableColumn
hpnicfOnuP2PShortFrameFirst=_HpnicfOnuP2PShortFrameFirst_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,3,1,10),_HpnicfOnuP2PShortFrameFirst_Type())
hpnicfOnuP2PShortFrameFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuP2PShortFrameFirst.setStatus(_A)
_HpnicfOnuSlaManTable_Object=MibTable
hpnicfOnuSlaManTable=_HpnicfOnuSlaManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4))
if mibBuilder.loadTexts:hpnicfOnuSlaManTable.setStatus(_A)
_HpnicfOnuSlaManEntry_Object=MibTableRow
hpnicfOnuSlaManEntry=_HpnicfOnuSlaManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1))
hpnicfOnuSlaManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuSlaManEntry.setStatus(_A)
_HpnicfOnuSlaMaxBandWidth_Type=Integer32
_HpnicfOnuSlaMaxBandWidth_Object=MibTableColumn
hpnicfOnuSlaMaxBandWidth=_HpnicfOnuSlaMaxBandWidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1,1),_HpnicfOnuSlaMaxBandWidth_Type())
hpnicfOnuSlaMaxBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuSlaMaxBandWidth.setStatus(_A)
_HpnicfOnuSlaMinBandWidth_Type=Integer32
_HpnicfOnuSlaMinBandWidth_Object=MibTableColumn
hpnicfOnuSlaMinBandWidth=_HpnicfOnuSlaMinBandWidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1,2),_HpnicfOnuSlaMinBandWidth_Type())
hpnicfOnuSlaMinBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuSlaMinBandWidth.setStatus(_A)
_HpnicfOnuSlaBandWidthStepVal_Type=Integer32
_HpnicfOnuSlaBandWidthStepVal_Object=MibTableColumn
hpnicfOnuSlaBandWidthStepVal=_HpnicfOnuSlaBandWidthStepVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1,3),_HpnicfOnuSlaBandWidthStepVal_Type())
hpnicfOnuSlaBandWidthStepVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSlaBandWidthStepVal.setStatus(_A)
class _HpnicfOnuSlaDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_HpnicfOnuSlaDelay_Type.__name__=_E
_HpnicfOnuSlaDelay_Object=MibTableColumn
hpnicfOnuSlaDelay=_HpnicfOnuSlaDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1,4),_HpnicfOnuSlaDelay_Type())
hpnicfOnuSlaDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuSlaDelay.setStatus(_A)
_HpnicfOnuSlaFixedBandWidth_Type=Integer32
_HpnicfOnuSlaFixedBandWidth_Object=MibTableColumn
hpnicfOnuSlaFixedBandWidth=_HpnicfOnuSlaFixedBandWidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1,5),_HpnicfOnuSlaFixedBandWidth_Type())
hpnicfOnuSlaFixedBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuSlaFixedBandWidth.setStatus(_A)
class _HpnicfOnuSlaPriorityClass_Type(Integer32):defaultValue=0
_HpnicfOnuSlaPriorityClass_Type.__name__=_E
_HpnicfOnuSlaPriorityClass_Object=MibTableColumn
hpnicfOnuSlaPriorityClass=_HpnicfOnuSlaPriorityClass_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1,6),_HpnicfOnuSlaPriorityClass_Type())
hpnicfOnuSlaPriorityClass.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuSlaPriorityClass.setStatus(_A)
_HpnicfOnuSlaFixedPacketSize_Type=Integer32
_HpnicfOnuSlaFixedPacketSize_Object=MibTableColumn
hpnicfOnuSlaFixedPacketSize=_HpnicfOnuSlaFixedPacketSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,4,1,7),_HpnicfOnuSlaFixedPacketSize_Type())
hpnicfOnuSlaFixedPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuSlaFixedPacketSize.setStatus(_A)
_HpnicfOnuInfoTable_Object=MibTable
hpnicfOnuInfoTable=_HpnicfOnuInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5))
if mibBuilder.loadTexts:hpnicfOnuInfoTable.setStatus(_A)
_HpnicfOnuInfoEntry_Object=MibTableRow
hpnicfOnuInfoEntry=_HpnicfOnuInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1))
hpnicfOnuInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuInfoEntry.setStatus(_A)
_HpnicfOnuHardMajorVersion_Type=OctetString
_HpnicfOnuHardMajorVersion_Object=MibTableColumn
hpnicfOnuHardMajorVersion=_HpnicfOnuHardMajorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,1),_HpnicfOnuHardMajorVersion_Type())
hpnicfOnuHardMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuHardMajorVersion.setStatus(_A)
_HpnicfOnuHardMinorVersion_Type=OctetString
_HpnicfOnuHardMinorVersion_Object=MibTableColumn
hpnicfOnuHardMinorVersion=_HpnicfOnuHardMinorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,2),_HpnicfOnuHardMinorVersion_Type())
hpnicfOnuHardMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuHardMinorVersion.setStatus(_A)
_HpnicfOnuSoftwareVersion_Type=OctetString
_HpnicfOnuSoftwareVersion_Object=MibTableColumn
hpnicfOnuSoftwareVersion=_HpnicfOnuSoftwareVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,3),_HpnicfOnuSoftwareVersion_Type())
hpnicfOnuSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSoftwareVersion.setStatus(_A)
class _HpnicfOnuUniMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('mii',2),('gmii',3),('tbi',4)))
_HpnicfOnuUniMacType_Type.__name__=_E
_HpnicfOnuUniMacType_Object=MibTableColumn
hpnicfOnuUniMacType=_HpnicfOnuUniMacType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,4),_HpnicfOnuUniMacType_Type())
hpnicfOnuUniMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuUniMacType.setStatus(_A)
_HpnicfOnuLaserOnTime_Type=Integer32
_HpnicfOnuLaserOnTime_Object=MibTableColumn
hpnicfOnuLaserOnTime=_HpnicfOnuLaserOnTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,5),_HpnicfOnuLaserOnTime_Type())
hpnicfOnuLaserOnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLaserOnTime.setStatus(_A)
_HpnicfOnuLaserOffTime_Type=Integer32
_HpnicfOnuLaserOffTime_Object=MibTableColumn
hpnicfOnuLaserOffTime=_HpnicfOnuLaserOffTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,6),_HpnicfOnuLaserOffTime_Type())
hpnicfOnuLaserOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLaserOffTime.setStatus(_A)
class _HpnicfOnuGrantFifoDep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255),ValueRangeConstraint(2147483647,2147483647))
_HpnicfOnuGrantFifoDep_Type.__name__=_E
_HpnicfOnuGrantFifoDep_Object=MibTableColumn
hpnicfOnuGrantFifoDep=_HpnicfOnuGrantFifoDep_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,7),_HpnicfOnuGrantFifoDep_Type())
hpnicfOnuGrantFifoDep.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuGrantFifoDep.setStatus(_A)
class _HpnicfOnuWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('on',2),('pending',3),('off',4)))
_HpnicfOnuWorkMode_Type.__name__=_E
_HpnicfOnuWorkMode_Object=MibTableColumn
hpnicfOnuWorkMode=_HpnicfOnuWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,8),_HpnicfOnuWorkMode_Type())
hpnicfOnuWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuWorkMode.setStatus(_A)
_HpnicfOnuPCBVersion_Type=OctetString
_HpnicfOnuPCBVersion_Object=MibTableColumn
hpnicfOnuPCBVersion=_HpnicfOnuPCBVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,9),_HpnicfOnuPCBVersion_Type())
hpnicfOnuPCBVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPCBVersion.setStatus(_A)
_HpnicfOnuRtt_Type=Unsigned32
_HpnicfOnuRtt_Object=MibTableColumn
hpnicfOnuRtt=_HpnicfOnuRtt_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,10),_HpnicfOnuRtt_Type())
hpnicfOnuRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRtt.setStatus(_A)
_HpnicfOnuEEPROMVersion_Type=OctetString
_HpnicfOnuEEPROMVersion_Object=MibTableColumn
hpnicfOnuEEPROMVersion=_HpnicfOnuEEPROMVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,11),_HpnicfOnuEEPROMVersion_Type())
hpnicfOnuEEPROMVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuEEPROMVersion.setStatus(_A)
_HpnicfOnuRegType_Type=OctetString
_HpnicfOnuRegType_Object=MibTableColumn
hpnicfOnuRegType=_HpnicfOnuRegType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,12),_HpnicfOnuRegType_Type())
hpnicfOnuRegType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRegType.setStatus(_A)
_HpnicfOnuHostType_Type=OctetString
_HpnicfOnuHostType_Object=MibTableColumn
hpnicfOnuHostType=_HpnicfOnuHostType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,13),_HpnicfOnuHostType_Type())
hpnicfOnuHostType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuHostType.setStatus(_A)
_HpnicfOnuDistance_Type=Integer32
_HpnicfOnuDistance_Object=MibTableColumn
hpnicfOnuDistance=_HpnicfOnuDistance_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,14),_HpnicfOnuDistance_Type())
hpnicfOnuDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuDistance.setStatus(_A)
_HpnicfOnuLlid_Type=Integer32
_HpnicfOnuLlid_Object=MibTableColumn
hpnicfOnuLlid=_HpnicfOnuLlid_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,15),_HpnicfOnuLlid_Type())
hpnicfOnuLlid.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLlid.setStatus(_A)
_HpnicfOnuVendorId_Type=OctetString
_HpnicfOnuVendorId_Object=MibTableColumn
hpnicfOnuVendorId=_HpnicfOnuVendorId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,16),_HpnicfOnuVendorId_Type())
hpnicfOnuVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuVendorId.setStatus(_A)
_HpnicfOnuFirmwareVersion_Type=OctetString
_HpnicfOnuFirmwareVersion_Object=MibTableColumn
hpnicfOnuFirmwareVersion=_HpnicfOnuFirmwareVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,17),_HpnicfOnuFirmwareVersion_Type())
hpnicfOnuFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuFirmwareVersion.setStatus(_A)
_HpnicfOnuOpticalPowerReceivedByOlt_Type=Integer32
_HpnicfOnuOpticalPowerReceivedByOlt_Object=MibTableColumn
hpnicfOnuOpticalPowerReceivedByOlt=_HpnicfOnuOpticalPowerReceivedByOlt_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,5,1,18),_HpnicfOnuOpticalPowerReceivedByOlt_Type())
hpnicfOnuOpticalPowerReceivedByOlt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuOpticalPowerReceivedByOlt.setStatus(_A)
_HpnicfOnuMacAddrInfoTable_Object=MibTable
hpnicfOnuMacAddrInfoTable=_HpnicfOnuMacAddrInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,6))
if mibBuilder.loadTexts:hpnicfOnuMacAddrInfoTable.setStatus(_A)
_HpnicfOnuMacAddrInfoEntry_Object=MibTableRow
hpnicfOnuMacAddrInfoEntry=_HpnicfOnuMacAddrInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,6,1))
hpnicfOnuMacAddrInfoEntry.setIndexNames((0,_D,_F),(0,_G,_u))
if mibBuilder.loadTexts:hpnicfOnuMacAddrInfoEntry.setStatus(_A)
_HpnicfOnuMacIndex_Type=Integer32
_HpnicfOnuMacIndex_Object=MibTableColumn
hpnicfOnuMacIndex=_HpnicfOnuMacIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,6,1,1),_HpnicfOnuMacIndex_Type())
hpnicfOnuMacIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuMacIndex.setStatus(_A)
class _HpnicfOnuMacAddrFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bound',1),('registered',2),('run',3),('regIncorrect',4)))
_HpnicfOnuMacAddrFlag_Type.__name__=_E
_HpnicfOnuMacAddrFlag_Object=MibTableColumn
hpnicfOnuMacAddrFlag=_HpnicfOnuMacAddrFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,6,1,2),_HpnicfOnuMacAddrFlag_Type())
hpnicfOnuMacAddrFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuMacAddrFlag.setStatus(_A)
_HpnicfOnuMacAddress_Type=MacAddress
_HpnicfOnuMacAddress_Object=MibTableColumn
hpnicfOnuMacAddress=_HpnicfOnuMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,6,1,3),_HpnicfOnuMacAddress_Type())
hpnicfOnuMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuMacAddress.setStatus(_A)
_HpnicfOnuBindMacAddrTable_Object=MibTable
hpnicfOnuBindMacAddrTable=_HpnicfOnuBindMacAddrTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,7))
if mibBuilder.loadTexts:hpnicfOnuBindMacAddrTable.setStatus(_A)
_HpnicfOnuBindMacAddrEntry_Object=MibTableRow
hpnicfOnuBindMacAddrEntry=_HpnicfOnuBindMacAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,7,1))
hpnicfOnuBindMacAddrEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuBindMacAddrEntry.setStatus(_A)
_HpnicfOnuBindMacAddress_Type=MacAddress
_HpnicfOnuBindMacAddress_Object=MibTableColumn
hpnicfOnuBindMacAddress=_HpnicfOnuBindMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,7,1,1),_HpnicfOnuBindMacAddress_Type())
hpnicfOnuBindMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuBindMacAddress.setStatus(_A)
_HpnicfOnuBindType_Type=Integer32
_HpnicfOnuBindType_Object=MibTableColumn
hpnicfOnuBindType=_HpnicfOnuBindType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,7,1,2),_HpnicfOnuBindType_Type())
hpnicfOnuBindType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuBindType.setStatus(_A)
_HpnicfOnuFirmwareUpdateTable_Object=MibTable
hpnicfOnuFirmwareUpdateTable=_HpnicfOnuFirmwareUpdateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,8))
if mibBuilder.loadTexts:hpnicfOnuFirmwareUpdateTable.setStatus(_A)
_HpnicfOnuFirmwareUpdateEntry_Object=MibTableRow
hpnicfOnuFirmwareUpdateEntry=_HpnicfOnuFirmwareUpdateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,8,1))
hpnicfOnuFirmwareUpdateEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuFirmwareUpdateEntry.setStatus(_A)
class _HpnicfOnuUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_p,1))
_HpnicfOnuUpdate_Type.__name__=_E
_HpnicfOnuUpdate_Object=MibTableColumn
hpnicfOnuUpdate=_HpnicfOnuUpdate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,8,1,1),_HpnicfOnuUpdate_Type())
hpnicfOnuUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuUpdate.setStatus(_A)
class _HpnicfOnuUpdateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('updating',1),('ok',2),(_Y,3),(_q,4),(_r,5),('fileNotMatchONU',6),('timeout',7),('otherError',8)))
_HpnicfOnuUpdateResult_Type.__name__=_E
_HpnicfOnuUpdateResult_Object=MibTableColumn
hpnicfOnuUpdateResult=_HpnicfOnuUpdateResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,8,1,2),_HpnicfOnuUpdateResult_Type())
hpnicfOnuUpdateResult.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuUpdateResult.setStatus(_A)
class _HpnicfOnuUpdateFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfOnuUpdateFileName_Type.__name__=_L
_HpnicfOnuUpdateFileName_Object=MibTableColumn
hpnicfOnuUpdateFileName=_HpnicfOnuUpdateFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,8,1,3),_HpnicfOnuUpdateFileName_Type())
hpnicfOnuUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuUpdateFileName.setStatus(_A)
_HpnicfOnuLinkTestFrameNumMinVal_Type=Integer32
_HpnicfOnuLinkTestFrameNumMinVal_Object=MibScalar
hpnicfOnuLinkTestFrameNumMinVal=_HpnicfOnuLinkTestFrameNumMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,9),_HpnicfOnuLinkTestFrameNumMinVal_Type())
hpnicfOnuLinkTestFrameNumMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestFrameNumMinVal.setStatus(_A)
_HpnicfOnuLinkTestFrameNumMaxVal_Type=Integer32
_HpnicfOnuLinkTestFrameNumMaxVal_Object=MibScalar
hpnicfOnuLinkTestFrameNumMaxVal=_HpnicfOnuLinkTestFrameNumMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,10),_HpnicfOnuLinkTestFrameNumMaxVal_Type())
hpnicfOnuLinkTestFrameNumMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuLinkTestFrameNumMaxVal.setStatus(_A)
_HpnicfOnuSlaMaxBandWidthMinVal_Type=Integer32
_HpnicfOnuSlaMaxBandWidthMinVal_Object=MibScalar
hpnicfOnuSlaMaxBandWidthMinVal=_HpnicfOnuSlaMaxBandWidthMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,11),_HpnicfOnuSlaMaxBandWidthMinVal_Type())
hpnicfOnuSlaMaxBandWidthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSlaMaxBandWidthMinVal.setStatus(_A)
_HpnicfOnuSlaMaxBandWidthMaxVal_Type=Integer32
_HpnicfOnuSlaMaxBandWidthMaxVal_Object=MibScalar
hpnicfOnuSlaMaxBandWidthMaxVal=_HpnicfOnuSlaMaxBandWidthMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,12),_HpnicfOnuSlaMaxBandWidthMaxVal_Type())
hpnicfOnuSlaMaxBandWidthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSlaMaxBandWidthMaxVal.setStatus(_A)
_HpnicfOnuSlaMinBandWidthMinVal_Type=Integer32
_HpnicfOnuSlaMinBandWidthMinVal_Object=MibScalar
hpnicfOnuSlaMinBandWidthMinVal=_HpnicfOnuSlaMinBandWidthMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,13),_HpnicfOnuSlaMinBandWidthMinVal_Type())
hpnicfOnuSlaMinBandWidthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSlaMinBandWidthMinVal.setStatus(_A)
_HpnicfOnuSlaMinBandWidthMaxVal_Type=Integer32
_HpnicfOnuSlaMinBandWidthMaxVal_Object=MibScalar
hpnicfOnuSlaMinBandWidthMaxVal=_HpnicfOnuSlaMinBandWidthMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,14),_HpnicfOnuSlaMinBandWidthMaxVal_Type())
hpnicfOnuSlaMinBandWidthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSlaMinBandWidthMaxVal.setStatus(_A)
_HpnicfEponOnuTypeManTable_Object=MibTable
hpnicfEponOnuTypeManTable=_HpnicfEponOnuTypeManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,15))
if mibBuilder.loadTexts:hpnicfEponOnuTypeManTable.setStatus(_A)
_HpnicfEponOnuTypeManEntry_Object=MibTableRow
hpnicfEponOnuTypeManEntry=_HpnicfEponOnuTypeManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,15,1))
hpnicfEponOnuTypeManEntry.setIndexNames((0,_G,_v))
if mibBuilder.loadTexts:hpnicfEponOnuTypeManEntry.setStatus(_A)
_HpnicfEponOnuTypeIndex_Type=Integer32
_HpnicfEponOnuTypeIndex_Object=MibTableColumn
hpnicfEponOnuTypeIndex=_HpnicfEponOnuTypeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,15,1,1),_HpnicfEponOnuTypeIndex_Type())
hpnicfEponOnuTypeIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfEponOnuTypeIndex.setStatus(_A)
_HpnicfEponOnuTypeDescr_Type=OctetString
_HpnicfEponOnuTypeDescr_Object=MibTableColumn
hpnicfEponOnuTypeDescr=_HpnicfEponOnuTypeDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,15,1,2),_HpnicfEponOnuTypeDescr_Type())
hpnicfEponOnuTypeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponOnuTypeDescr.setStatus(_A)
_HpnicfOnuPacketManTable_Object=MibTable
hpnicfOnuPacketManTable=_HpnicfOnuPacketManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,16))
if mibBuilder.loadTexts:hpnicfOnuPacketManTable.setStatus(_A)
_HpnicfOnuPacketManEntry_Object=MibTableRow
hpnicfOnuPacketManEntry=_HpnicfOnuPacketManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,16,1))
hpnicfOnuPacketManEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuPacketManEntry.setStatus(_A)
class _HpnicfOnuPriorityTrust_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dscp',1),('ipprecedence',2),('cos',3)))
_HpnicfOnuPriorityTrust_Type.__name__=_E
_HpnicfOnuPriorityTrust_Object=MibTableColumn
hpnicfOnuPriorityTrust=_HpnicfOnuPriorityTrust_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,16,1,1),_HpnicfOnuPriorityTrust_Type())
hpnicfOnuPriorityTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuPriorityTrust.setStatus(_A)
class _HpnicfOnuQueueScheduler_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('spq',1),('wfq',2)))
_HpnicfOnuQueueScheduler_Type.__name__=_E
_HpnicfOnuQueueScheduler_Object=MibTableColumn
hpnicfOnuQueueScheduler=_HpnicfOnuQueueScheduler_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,16,1,2),_HpnicfOnuQueueScheduler_Type())
hpnicfOnuQueueScheduler.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuQueueScheduler.setStatus(_A)
_HpnicfOnuProtocolTable_Object=MibTable
hpnicfOnuProtocolTable=_HpnicfOnuProtocolTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17))
if mibBuilder.loadTexts:hpnicfOnuProtocolTable.setStatus(_A)
_HpnicfOnuProtocolEntry_Object=MibTableRow
hpnicfOnuProtocolEntry=_HpnicfOnuProtocolEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1))
hpnicfOnuProtocolEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuProtocolEntry.setStatus(_A)
class _HpnicfOnuStpStatus_Type(TruthValue):defaultValue=1
_HpnicfOnuStpStatus_Type.__name__=_H
_HpnicfOnuStpStatus_Object=MibTableColumn
hpnicfOnuStpStatus=_HpnicfOnuStpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,1),_HpnicfOnuStpStatus_Type())
hpnicfOnuStpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuStpStatus.setStatus(_A)
class _HpnicfOnuIgmpSnoopingStatus_Type(TruthValue):defaultValue=1
_HpnicfOnuIgmpSnoopingStatus_Type.__name__=_H
_HpnicfOnuIgmpSnoopingStatus_Object=MibTableColumn
hpnicfOnuIgmpSnoopingStatus=_HpnicfOnuIgmpSnoopingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,2),_HpnicfOnuIgmpSnoopingStatus_Type())
hpnicfOnuIgmpSnoopingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIgmpSnoopingStatus.setStatus(_A)
class _HpnicfOnuDhcpsnoopingOption82_Type(TruthValue):defaultValue=2
_HpnicfOnuDhcpsnoopingOption82_Type.__name__=_H
_HpnicfOnuDhcpsnoopingOption82_Object=MibTableColumn
hpnicfOnuDhcpsnoopingOption82=_HpnicfOnuDhcpsnoopingOption82_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,3),_HpnicfOnuDhcpsnoopingOption82_Type())
hpnicfOnuDhcpsnoopingOption82.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDhcpsnoopingOption82.setStatus(_A)
class _HpnicfOnuDhcpsnooping_Type(TruthValue):defaultValue=2
_HpnicfOnuDhcpsnooping_Type.__name__=_H
_HpnicfOnuDhcpsnooping_Object=MibTableColumn
hpnicfOnuDhcpsnooping=_HpnicfOnuDhcpsnooping_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,4),_HpnicfOnuDhcpsnooping_Type())
hpnicfOnuDhcpsnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDhcpsnooping.setStatus(_A)
class _HpnicfOnuPppoe_Type(TruthValue):defaultValue=2
_HpnicfOnuPppoe_Type.__name__=_H
_HpnicfOnuPppoe_Object=MibTableColumn
hpnicfOnuPppoe=_HpnicfOnuPppoe_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,5),_HpnicfOnuPppoe_Type())
hpnicfOnuPppoe.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuPppoe.setStatus(_A)
_HpnicfOnuIgmpSnoopingHostAgingT_Type=Integer32
_HpnicfOnuIgmpSnoopingHostAgingT_Object=MibTableColumn
hpnicfOnuIgmpSnoopingHostAgingT=_HpnicfOnuIgmpSnoopingHostAgingT_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,6),_HpnicfOnuIgmpSnoopingHostAgingT_Type())
hpnicfOnuIgmpSnoopingHostAgingT.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIgmpSnoopingHostAgingT.setStatus(_A)
_HpnicfOnuIgmpSnoopingMaxRespT_Type=Integer32
_HpnicfOnuIgmpSnoopingMaxRespT_Object=MibTableColumn
hpnicfOnuIgmpSnoopingMaxRespT=_HpnicfOnuIgmpSnoopingMaxRespT_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,7),_HpnicfOnuIgmpSnoopingMaxRespT_Type())
hpnicfOnuIgmpSnoopingMaxRespT.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIgmpSnoopingMaxRespT.setStatus(_A)
_HpnicfOnuIgmpSnoopingRouterAgingT_Type=Integer32
_HpnicfOnuIgmpSnoopingRouterAgingT_Object=MibTableColumn
hpnicfOnuIgmpSnoopingRouterAgingT=_HpnicfOnuIgmpSnoopingRouterAgingT_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,8),_HpnicfOnuIgmpSnoopingRouterAgingT_Type())
hpnicfOnuIgmpSnoopingRouterAgingT.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIgmpSnoopingRouterAgingT.setStatus(_A)
class _HpnicfOnuIgmpSnoopingAggReportS_Type(TruthValue):defaultValue=2
_HpnicfOnuIgmpSnoopingAggReportS_Type.__name__=_H
_HpnicfOnuIgmpSnoopingAggReportS_Object=MibTableColumn
hpnicfOnuIgmpSnoopingAggReportS=_HpnicfOnuIgmpSnoopingAggReportS_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,9),_HpnicfOnuIgmpSnoopingAggReportS_Type())
hpnicfOnuIgmpSnoopingAggReportS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIgmpSnoopingAggReportS.setStatus(_A)
class _HpnicfOnuIgmpSnoopingAggLeaveS_Type(TruthValue):defaultValue=1
_HpnicfOnuIgmpSnoopingAggLeaveS_Type.__name__=_H
_HpnicfOnuIgmpSnoopingAggLeaveS_Object=MibTableColumn
hpnicfOnuIgmpSnoopingAggLeaveS=_HpnicfOnuIgmpSnoopingAggLeaveS_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,17,1,10),_HpnicfOnuIgmpSnoopingAggLeaveS_Type())
hpnicfOnuIgmpSnoopingAggLeaveS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIgmpSnoopingAggLeaveS.setStatus(_A)
_HpnicfOnuDot1xTable_Object=MibTable
hpnicfOnuDot1xTable=_HpnicfOnuDot1xTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,18))
if mibBuilder.loadTexts:hpnicfOnuDot1xTable.setStatus(_A)
_HpnicfOnuDot1xEntry_Object=MibTableRow
hpnicfOnuDot1xEntry=_HpnicfOnuDot1xEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,18,1))
hpnicfOnuDot1xEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuDot1xEntry.setStatus(_A)
_HpnicfOnuDot1xAccount_Type=OctetString
_HpnicfOnuDot1xAccount_Object=MibTableColumn
hpnicfOnuDot1xAccount=_HpnicfOnuDot1xAccount_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,18,1,1),_HpnicfOnuDot1xAccount_Type())
hpnicfOnuDot1xAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDot1xAccount.setStatus(_A)
_HpnicfOnuDot1xPassword_Type=OctetString
_HpnicfOnuDot1xPassword_Object=MibTableColumn
hpnicfOnuDot1xPassword=_HpnicfOnuDot1xPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,18,1,2),_HpnicfOnuDot1xPassword_Type())
hpnicfOnuDot1xPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDot1xPassword.setStatus(_A)
_HpnicfOnuPriorityQueueTable_Object=MibTable
hpnicfOnuPriorityQueueTable=_HpnicfOnuPriorityQueueTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,19))
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueTable.setStatus(_A)
_HpnicfOnuPriorityQueueEntry_Object=MibTableRow
hpnicfOnuPriorityQueueEntry=_HpnicfOnuPriorityQueueEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,19,1))
hpnicfOnuPriorityQueueEntry.setIndexNames((0,_D,_F),(0,_G,_Z),(0,_G,_a))
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueEntry.setStatus(_A)
class _HpnicfOnuQueueDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_HpnicfOnuQueueDirection_Type.__name__=_E
_HpnicfOnuQueueDirection_Object=MibTableColumn
hpnicfOnuQueueDirection=_HpnicfOnuQueueDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,19,1,1),_HpnicfOnuQueueDirection_Type())
hpnicfOnuQueueDirection.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuQueueDirection.setStatus(_A)
class _HpnicfOnuQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfOnuQueueId_Type.__name__=_E
_HpnicfOnuQueueId_Object=MibTableColumn
hpnicfOnuQueueId=_HpnicfOnuQueueId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,19,1,2),_HpnicfOnuQueueId_Type())
hpnicfOnuQueueId.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuQueueId.setStatus(_A)
_HpnicfOnuQueueSize_Type=Integer32
_HpnicfOnuQueueSize_Object=MibTableColumn
hpnicfOnuQueueSize=_HpnicfOnuQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,19,1,3),_HpnicfOnuQueueSize_Type())
hpnicfOnuQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuQueueSize.setStatus(_A)
_HpnicfOnuCountTable_Object=MibTable
hpnicfOnuCountTable=_HpnicfOnuCountTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,20))
if mibBuilder.loadTexts:hpnicfOnuCountTable.setStatus(_A)
_HpnicfOnuCountEntry_Object=MibTableRow
hpnicfOnuCountEntry=_HpnicfOnuCountEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,20,1))
hpnicfOnuCountEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuCountEntry.setStatus(_A)
_HpnicfOnuInCRCErrPkts_Type=Counter64
_HpnicfOnuInCRCErrPkts_Object=MibTableColumn
hpnicfOnuInCRCErrPkts=_HpnicfOnuInCRCErrPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,20,1,1),_HpnicfOnuInCRCErrPkts_Type())
hpnicfOnuInCRCErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuInCRCErrPkts.setStatus(_A)
_HpnicfOnuOutDroppedFrames_Type=Counter64
_HpnicfOnuOutDroppedFrames_Object=MibTableColumn
hpnicfOnuOutDroppedFrames=_HpnicfOnuOutDroppedFrames_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,20,1,2),_HpnicfOnuOutDroppedFrames_Type())
hpnicfOnuOutDroppedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuOutDroppedFrames.setStatus(_A)
_HpnicfEponOnuScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfEponOnuScalarGroup=_HpnicfEponOnuScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21))
_HpnicfOnuPriorityQueueSizeMinVal_Type=Integer32
_HpnicfOnuPriorityQueueSizeMinVal_Object=MibScalar
hpnicfOnuPriorityQueueSizeMinVal=_HpnicfOnuPriorityQueueSizeMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21,1),_HpnicfOnuPriorityQueueSizeMinVal_Type())
hpnicfOnuPriorityQueueSizeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueSizeMinVal.setStatus(_A)
_HpnicfOnuPriorityQueueSizeMaxVal_Type=Integer32
_HpnicfOnuPriorityQueueSizeMaxVal_Object=MibScalar
hpnicfOnuPriorityQueueSizeMaxVal=_HpnicfOnuPriorityQueueSizeMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21,2),_HpnicfOnuPriorityQueueSizeMaxVal_Type())
hpnicfOnuPriorityQueueSizeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueSizeMaxVal.setStatus(_A)
_HpnicfOnuPriorityQueueBandwidthMinVal_Type=Integer32
_HpnicfOnuPriorityQueueBandwidthMinVal_Object=MibScalar
hpnicfOnuPriorityQueueBandwidthMinVal=_HpnicfOnuPriorityQueueBandwidthMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21,3),_HpnicfOnuPriorityQueueBandwidthMinVal_Type())
hpnicfOnuPriorityQueueBandwidthMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueBandwidthMinVal.setStatus(_A)
_HpnicfOnuPriorityQueueBandwidthMaxVal_Type=Integer32
_HpnicfOnuPriorityQueueBandwidthMaxVal_Object=MibScalar
hpnicfOnuPriorityQueueBandwidthMaxVal=_HpnicfOnuPriorityQueueBandwidthMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21,4),_HpnicfOnuPriorityQueueBandwidthMaxVal_Type())
hpnicfOnuPriorityQueueBandwidthMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueBandwidthMaxVal.setStatus(_A)
_HpnicfOnuPriorityQueueBurstsizeMinVal_Type=Integer32
_HpnicfOnuPriorityQueueBurstsizeMinVal_Object=MibScalar
hpnicfOnuPriorityQueueBurstsizeMinVal=_HpnicfOnuPriorityQueueBurstsizeMinVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21,5),_HpnicfOnuPriorityQueueBurstsizeMinVal_Type())
hpnicfOnuPriorityQueueBurstsizeMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueBurstsizeMinVal.setStatus(_A)
_HpnicfOnuPriorityQueueBurstsizeMaxVal_Type=Integer32
_HpnicfOnuPriorityQueueBurstsizeMaxVal_Object=MibScalar
hpnicfOnuPriorityQueueBurstsizeMaxVal=_HpnicfOnuPriorityQueueBurstsizeMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21,6),_HpnicfOnuPriorityQueueBurstsizeMaxVal_Type())
hpnicfOnuPriorityQueueBurstsizeMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPriorityQueueBurstsizeMaxVal.setStatus(_A)
_HpnicfOnuUpdateByTypeNextIndex_Type=Integer32
_HpnicfOnuUpdateByTypeNextIndex_Object=MibScalar
hpnicfOnuUpdateByTypeNextIndex=_HpnicfOnuUpdateByTypeNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,21,7),_HpnicfOnuUpdateByTypeNextIndex_Type())
hpnicfOnuUpdateByTypeNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuUpdateByTypeNextIndex.setStatus(_A)
_HpnicfOnuQueueBandwidthTable_Object=MibTable
hpnicfOnuQueueBandwidthTable=_HpnicfOnuQueueBandwidthTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,22))
if mibBuilder.loadTexts:hpnicfOnuQueueBandwidthTable.setStatus(_A)
_HpnicfOnuQueueBandwidthEntry_Object=MibTableRow
hpnicfOnuQueueBandwidthEntry=_HpnicfOnuQueueBandwidthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,22,1))
hpnicfOnuQueueBandwidthEntry.setIndexNames((0,_D,_F),(0,_G,_Z),(0,_G,_a))
if mibBuilder.loadTexts:hpnicfOnuQueueBandwidthEntry.setStatus(_A)
_HpnicfOnuQueueMaxBandwidth_Type=Integer32
_HpnicfOnuQueueMaxBandwidth_Object=MibTableColumn
hpnicfOnuQueueMaxBandwidth=_HpnicfOnuQueueMaxBandwidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,22,1,1),_HpnicfOnuQueueMaxBandwidth_Type())
hpnicfOnuQueueMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuQueueMaxBandwidth.setStatus(_A)
_HpnicfOnuQueueMaxBurstsize_Type=Integer32
_HpnicfOnuQueueMaxBurstsize_Object=MibTableColumn
hpnicfOnuQueueMaxBurstsize=_HpnicfOnuQueueMaxBurstsize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,22,1,2),_HpnicfOnuQueueMaxBurstsize_Type())
hpnicfOnuQueueMaxBurstsize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuQueueMaxBurstsize.setStatus(_A)
_HpnicfOnuQueuePolicyStatus_Type=TruthValue
_HpnicfOnuQueuePolicyStatus_Object=MibTableColumn
hpnicfOnuQueuePolicyStatus=_HpnicfOnuQueuePolicyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,22,1,3),_HpnicfOnuQueuePolicyStatus_Type())
hpnicfOnuQueuePolicyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuQueuePolicyStatus.setStatus(_A)
_HpnicfOnuIpAddressTable_Object=MibTable
hpnicfOnuIpAddressTable=_HpnicfOnuIpAddressTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23))
if mibBuilder.loadTexts:hpnicfOnuIpAddressTable.setStatus(_A)
_HpnicfOnuIpAddressEntry_Object=MibTableRow
hpnicfOnuIpAddressEntry=_HpnicfOnuIpAddressEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23,1))
hpnicfOnuIpAddressEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuIpAddressEntry.setStatus(_A)
_HpnicfOnuIpAddress_Type=IpAddress
_HpnicfOnuIpAddress_Object=MibTableColumn
hpnicfOnuIpAddress=_HpnicfOnuIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23,1,1),_HpnicfOnuIpAddress_Type())
hpnicfOnuIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIpAddress.setStatus(_A)
_HpnicfOnuIpAddressMask_Type=IpAddress
_HpnicfOnuIpAddressMask_Object=MibTableColumn
hpnicfOnuIpAddressMask=_HpnicfOnuIpAddressMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23,1,2),_HpnicfOnuIpAddressMask_Type())
hpnicfOnuIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIpAddressMask.setStatus(_A)
_HpnicfOnuIpAddressGateway_Type=IpAddress
_HpnicfOnuIpAddressGateway_Object=MibTableColumn
hpnicfOnuIpAddressGateway=_HpnicfOnuIpAddressGateway_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23,1,3),_HpnicfOnuIpAddressGateway_Type())
hpnicfOnuIpAddressGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuIpAddressGateway.setStatus(_A)
_HpnicfOnuDhcpallocate_Type=TruthValue
_HpnicfOnuDhcpallocate_Object=MibTableColumn
hpnicfOnuDhcpallocate=_HpnicfOnuDhcpallocate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23,1,4),_HpnicfOnuDhcpallocate_Type())
hpnicfOnuDhcpallocate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDhcpallocate.setStatus(_A)
_HpnicfOnuManageVID_Type=Integer32
_HpnicfOnuManageVID_Object=MibTableColumn
hpnicfOnuManageVID=_HpnicfOnuManageVID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23,1,5),_HpnicfOnuManageVID_Type())
hpnicfOnuManageVID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuManageVID.setStatus(_A)
_HpnicfOnuManageVlanIntfS_Type=TruthValue
_HpnicfOnuManageVlanIntfS_Object=MibTableColumn
hpnicfOnuManageVlanIntfS=_HpnicfOnuManageVlanIntfS_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,23,1,6),_HpnicfOnuManageVlanIntfS_Type())
hpnicfOnuManageVlanIntfS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuManageVlanIntfS.setStatus(_A)
_HpnicfOnuChipSetInfoTable_Object=MibTable
hpnicfOnuChipSetInfoTable=_HpnicfOnuChipSetInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,24))
if mibBuilder.loadTexts:hpnicfOnuChipSetInfoTable.setStatus(_A)
_HpnicfOnuChipSetInfoEntry_Object=MibTableRow
hpnicfOnuChipSetInfoEntry=_HpnicfOnuChipSetInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,24,1))
hpnicfOnuChipSetInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuChipSetInfoEntry.setStatus(_A)
class _HpnicfOnuChipSetVendorId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfOnuChipSetVendorId_Type.__name__=_L
_HpnicfOnuChipSetVendorId_Object=MibTableColumn
hpnicfOnuChipSetVendorId=_HpnicfOnuChipSetVendorId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,24,1,1),_HpnicfOnuChipSetVendorId_Type())
hpnicfOnuChipSetVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuChipSetVendorId.setStatus(_A)
class _HpnicfOnuChipSetModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfOnuChipSetModel_Type.__name__=_L
_HpnicfOnuChipSetModel_Object=MibTableColumn
hpnicfOnuChipSetModel=_HpnicfOnuChipSetModel_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,24,1,2),_HpnicfOnuChipSetModel_Type())
hpnicfOnuChipSetModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuChipSetModel.setStatus(_A)
_HpnicfOnuChipSetRevision_Type=Integer32
_HpnicfOnuChipSetRevision_Object=MibTableColumn
hpnicfOnuChipSetRevision=_HpnicfOnuChipSetRevision_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,24,1,3),_HpnicfOnuChipSetRevision_Type())
hpnicfOnuChipSetRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuChipSetRevision.setStatus(_A)
_HpnicfOnuChipSetDesignDate_Type=DateAndTime
_HpnicfOnuChipSetDesignDate_Object=MibTableColumn
hpnicfOnuChipSetDesignDate=_HpnicfOnuChipSetDesignDate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,24,1,4),_HpnicfOnuChipSetDesignDate_Type())
hpnicfOnuChipSetDesignDate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuChipSetDesignDate.setStatus(_A)
_HpnicfOnuCapabilityTable_Object=MibTable
hpnicfOnuCapabilityTable=_HpnicfOnuCapabilityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25))
if mibBuilder.loadTexts:hpnicfOnuCapabilityTable.setStatus(_A)
_HpnicfOnuCapabilityEntry_Object=MibTableRow
hpnicfOnuCapabilityEntry=_HpnicfOnuCapabilityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1))
hpnicfOnuCapabilityEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuCapabilityEntry.setStatus(_A)
class _HpnicfOnuServiceSupported_Type(Bits):namedValues=NamedValues(*(('geinterfacesupport',0),('feinterfacesupport',1),('voipservicesupport',2),('tdmservicesupport',3)))
_HpnicfOnuServiceSupported_Type.__name__='Bits'
_HpnicfOnuServiceSupported_Object=MibTableColumn
hpnicfOnuServiceSupported=_HpnicfOnuServiceSupported_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,1),_HpnicfOnuServiceSupported_Type())
hpnicfOnuServiceSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuServiceSupported.setStatus(_A)
_HpnicfOnuGEPortNumber_Type=Integer32
_HpnicfOnuGEPortNumber_Object=MibTableColumn
hpnicfOnuGEPortNumber=_HpnicfOnuGEPortNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,2),_HpnicfOnuGEPortNumber_Type())
hpnicfOnuGEPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuGEPortNumber.setStatus(_A)
_HpnicfOnuFEPortNumber_Type=Integer32
_HpnicfOnuFEPortNumber_Object=MibTableColumn
hpnicfOnuFEPortNumber=_HpnicfOnuFEPortNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,3),_HpnicfOnuFEPortNumber_Type())
hpnicfOnuFEPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuFEPortNumber.setStatus(_A)
_HpnicfOnuPOTSPortNumber_Type=Integer32
_HpnicfOnuPOTSPortNumber_Object=MibTableColumn
hpnicfOnuPOTSPortNumber=_HpnicfOnuPOTSPortNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,4),_HpnicfOnuPOTSPortNumber_Type())
hpnicfOnuPOTSPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuPOTSPortNumber.setStatus(_A)
_HpnicfOnuE1PortsNumber_Type=Integer32
_HpnicfOnuE1PortsNumber_Object=MibTableColumn
hpnicfOnuE1PortsNumber=_HpnicfOnuE1PortsNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,5),_HpnicfOnuE1PortsNumber_Type())
hpnicfOnuE1PortsNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuE1PortsNumber.setStatus(_A)
_HpnicfOnuUpstreamQueueNumber_Type=Integer32
_HpnicfOnuUpstreamQueueNumber_Object=MibTableColumn
hpnicfOnuUpstreamQueueNumber=_HpnicfOnuUpstreamQueueNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,6),_HpnicfOnuUpstreamQueueNumber_Type())
hpnicfOnuUpstreamQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuUpstreamQueueNumber.setStatus(_A)
_HpnicfOnuMaxUpstreamQueuePerPort_Type=Integer32
_HpnicfOnuMaxUpstreamQueuePerPort_Object=MibTableColumn
hpnicfOnuMaxUpstreamQueuePerPort=_HpnicfOnuMaxUpstreamQueuePerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,7),_HpnicfOnuMaxUpstreamQueuePerPort_Type())
hpnicfOnuMaxUpstreamQueuePerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuMaxUpstreamQueuePerPort.setStatus(_A)
_HpnicfOnuDownstreamQueueNumber_Type=Integer32
_HpnicfOnuDownstreamQueueNumber_Object=MibTableColumn
hpnicfOnuDownstreamQueueNumber=_HpnicfOnuDownstreamQueueNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,8),_HpnicfOnuDownstreamQueueNumber_Type())
hpnicfOnuDownstreamQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuDownstreamQueueNumber.setStatus(_A)
_HpnicfOnuMaxDownstreamQueuePerPort_Type=Integer32
_HpnicfOnuMaxDownstreamQueuePerPort_Object=MibTableColumn
hpnicfOnuMaxDownstreamQueuePerPort=_HpnicfOnuMaxDownstreamQueuePerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,9),_HpnicfOnuMaxDownstreamQueuePerPort_Type())
hpnicfOnuMaxDownstreamQueuePerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuMaxDownstreamQueuePerPort.setStatus(_A)
_HpnicfOnuBatteryBackup_Type=TruthValue
_HpnicfOnuBatteryBackup_Object=MibTableColumn
hpnicfOnuBatteryBackup=_HpnicfOnuBatteryBackup_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,10),_HpnicfOnuBatteryBackup_Type())
hpnicfOnuBatteryBackup.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuBatteryBackup.setStatus(_A)
_HpnicfOnuIgspFastLeaveSupported_Type=TruthValue
_HpnicfOnuIgspFastLeaveSupported_Object=MibTableColumn
hpnicfOnuIgspFastLeaveSupported=_HpnicfOnuIgspFastLeaveSupported_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,11),_HpnicfOnuIgspFastLeaveSupported_Type())
hpnicfOnuIgspFastLeaveSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuIgspFastLeaveSupported.setStatus(_A)
_HpnicfOnuMCtrlFastLeaveSupported_Type=TruthValue
_HpnicfOnuMCtrlFastLeaveSupported_Object=MibTableColumn
hpnicfOnuMCtrlFastLeaveSupported=_HpnicfOnuMCtrlFastLeaveSupported_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,25,1,12),_HpnicfOnuMCtrlFastLeaveSupported_Type())
hpnicfOnuMCtrlFastLeaveSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuMCtrlFastLeaveSupported.setStatus(_A)
_HpnicfOnuDbaReportTable_Object=MibTable
hpnicfOnuDbaReportTable=_HpnicfOnuDbaReportTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,26))
if mibBuilder.loadTexts:hpnicfOnuDbaReportTable.setStatus(_A)
_HpnicfOnuDbaReportEntry_Object=MibTableRow
hpnicfOnuDbaReportEntry=_HpnicfOnuDbaReportEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,26,1))
hpnicfOnuDbaReportEntry.setIndexNames((0,_D,_F),(0,_G,_w))
if mibBuilder.loadTexts:hpnicfOnuDbaReportEntry.setStatus(_A)
_HpnicfOnuDbaReportQueueId_Type=Integer32
_HpnicfOnuDbaReportQueueId_Object=MibTableColumn
hpnicfOnuDbaReportQueueId=_HpnicfOnuDbaReportQueueId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,26,1,1),_HpnicfOnuDbaReportQueueId_Type())
hpnicfOnuDbaReportQueueId.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuDbaReportQueueId.setStatus(_A)
_HpnicfOnuDbaReportThreshold_Type=Integer32
_HpnicfOnuDbaReportThreshold_Object=MibTableColumn
hpnicfOnuDbaReportThreshold=_HpnicfOnuDbaReportThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,26,1,2),_HpnicfOnuDbaReportThreshold_Type())
hpnicfOnuDbaReportThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDbaReportThreshold.setStatus(_A)
class _HpnicfOnuDbaReportStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfOnuDbaReportStatus_Type.__name__=_E
_HpnicfOnuDbaReportStatus_Object=MibTableColumn
hpnicfOnuDbaReportStatus=_HpnicfOnuDbaReportStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,26,1,3),_HpnicfOnuDbaReportStatus_Type())
hpnicfOnuDbaReportStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuDbaReportStatus.setStatus(_A)
_HpnicfOnuCosToLocalPrecedenceTable_Object=MibTable
hpnicfOnuCosToLocalPrecedenceTable=_HpnicfOnuCosToLocalPrecedenceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,27))
if mibBuilder.loadTexts:hpnicfOnuCosToLocalPrecedenceTable.setStatus(_A)
_HpnicfOnuCosToLocalPrecedenceEntry_Object=MibTableRow
hpnicfOnuCosToLocalPrecedenceEntry=_HpnicfOnuCosToLocalPrecedenceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,27,1))
hpnicfOnuCosToLocalPrecedenceEntry.setIndexNames((0,_D,_F),(0,_G,_x))
if mibBuilder.loadTexts:hpnicfOnuCosToLocalPrecedenceEntry.setStatus(_A)
class _HpnicfOnuCosToLocalPrecedenceCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfOnuCosToLocalPrecedenceCosIndex_Type.__name__=_E
_HpnicfOnuCosToLocalPrecedenceCosIndex_Object=MibTableColumn
hpnicfOnuCosToLocalPrecedenceCosIndex=_HpnicfOnuCosToLocalPrecedenceCosIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,27,1,1),_HpnicfOnuCosToLocalPrecedenceCosIndex_Type())
hpnicfOnuCosToLocalPrecedenceCosIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuCosToLocalPrecedenceCosIndex.setStatus(_A)
class _HpnicfOnuCosToLocalPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfOnuCosToLocalPrecedenceValue_Type.__name__=_E
_HpnicfOnuCosToLocalPrecedenceValue_Object=MibTableColumn
hpnicfOnuCosToLocalPrecedenceValue=_HpnicfOnuCosToLocalPrecedenceValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,27,1,2),_HpnicfOnuCosToLocalPrecedenceValue_Type())
hpnicfOnuCosToLocalPrecedenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuCosToLocalPrecedenceValue.setStatus(_A)
_HpnicfEponOnuStpPortTable_Object=MibTable
hpnicfEponOnuStpPortTable=_HpnicfEponOnuStpPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,28))
if mibBuilder.loadTexts:hpnicfEponOnuStpPortTable.setStatus(_A)
_HpnicfEponOnuStpPortEntry_Object=MibTableRow
hpnicfEponOnuStpPortEntry=_HpnicfEponOnuStpPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,28,1))
hpnicfEponOnuStpPortEntry.setIndexNames((0,_D,_F),(0,_G,_b))
if mibBuilder.loadTexts:hpnicfEponOnuStpPortEntry.setStatus(_A)
class _HpnicfEponStpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,144))
_HpnicfEponStpPortIndex_Type.__name__=_E
_HpnicfEponStpPortIndex_Object=MibTableColumn
hpnicfEponStpPortIndex=_HpnicfEponStpPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,28,1,1),_HpnicfEponStpPortIndex_Type())
hpnicfEponStpPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponStpPortIndex.setStatus(_A)
_HpnicfEponStpPortDescr_Type=OctetString
_HpnicfEponStpPortDescr_Object=MibTableColumn
hpnicfEponStpPortDescr=_HpnicfEponStpPortDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,28,1,2),_HpnicfEponStpPortDescr_Type())
hpnicfEponStpPortDescr.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponStpPortDescr.setStatus(_A)
class _HpnicfEponStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('discarding',2),('learning',3),('forwarding',4)))
_HpnicfEponStpPortState_Type.__name__=_E
_HpnicfEponStpPortState_Object=MibTableColumn
hpnicfEponStpPortState=_HpnicfEponStpPortState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,28,1,3),_HpnicfEponStpPortState_Type())
hpnicfEponStpPortState.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponStpPortState.setStatus(_A)
_HpnicfOnuPhysicalTable_Object=MibTable
hpnicfOnuPhysicalTable=_HpnicfOnuPhysicalTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,29))
if mibBuilder.loadTexts:hpnicfOnuPhysicalTable.setStatus(_A)
_HpnicfOnuPhysicalEntry_Object=MibTableRow
hpnicfOnuPhysicalEntry=_HpnicfOnuPhysicalEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,29,1))
hpnicfOnuPhysicalEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfOnuPhysicalEntry.setStatus(_A)
_HpnicfOnuBridgeMac_Type=MacAddress
_HpnicfOnuBridgeMac_Object=MibTableColumn
hpnicfOnuBridgeMac=_HpnicfOnuBridgeMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,29,1,1),_HpnicfOnuBridgeMac_Type())
hpnicfOnuBridgeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuBridgeMac.setStatus(_A)
_HpnicfOnuFirstPonMac_Type=MacAddress
_HpnicfOnuFirstPonMac_Object=MibTableColumn
hpnicfOnuFirstPonMac=_HpnicfOnuFirstPonMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,29,1,2),_HpnicfOnuFirstPonMac_Type())
hpnicfOnuFirstPonMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuFirstPonMac.setStatus(_A)
class _HpnicfOnuFirstPonRegState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_y,1),(_z,2),('offline',3),('silent',4),(_T,5),('up',6)))
_HpnicfOnuFirstPonRegState_Type.__name__=_E
_HpnicfOnuFirstPonRegState_Object=MibTableColumn
hpnicfOnuFirstPonRegState=_HpnicfOnuFirstPonRegState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,29,1,3),_HpnicfOnuFirstPonRegState_Type())
hpnicfOnuFirstPonRegState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuFirstPonRegState.setStatus(_A)
_HpnicfOnuSecondPonMac_Type=MacAddress
_HpnicfOnuSecondPonMac_Object=MibTableColumn
hpnicfOnuSecondPonMac=_HpnicfOnuSecondPonMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,29,1,4),_HpnicfOnuSecondPonMac_Type())
hpnicfOnuSecondPonMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSecondPonMac.setStatus(_A)
class _HpnicfOnuSecondPonRegState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_y,1),(_z,2),('offline',3),('silent',4),(_T,5),('up',6)))
_HpnicfOnuSecondPonRegState_Type.__name__=_E
_HpnicfOnuSecondPonRegState_Object=MibTableColumn
hpnicfOnuSecondPonRegState=_HpnicfOnuSecondPonRegState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,29,1,5),_HpnicfOnuSecondPonRegState_Type())
hpnicfOnuSecondPonRegState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSecondPonRegState.setStatus(_A)
_HpnicfOnuSmlkTable_Object=MibTable
hpnicfOnuSmlkTable=_HpnicfOnuSmlkTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,30))
if mibBuilder.loadTexts:hpnicfOnuSmlkTable.setStatus(_A)
_HpnicfOnuSmlkEntry_Object=MibTableRow
hpnicfOnuSmlkEntry=_HpnicfOnuSmlkEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,30,1))
hpnicfOnuSmlkEntry.setIndexNames((0,_D,_F),(0,_G,_c))
if mibBuilder.loadTexts:hpnicfOnuSmlkEntry.setStatus(_A)
_HpnicfOnuSmlkGroupID_Type=Integer32
_HpnicfOnuSmlkGroupID_Object=MibTableColumn
hpnicfOnuSmlkGroupID=_HpnicfOnuSmlkGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,30,1,1),_HpnicfOnuSmlkGroupID_Type())
hpnicfOnuSmlkGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSmlkGroupID.setStatus(_A)
class _HpnicfOnuSmlkFirstPonRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),(_U,3)))
_HpnicfOnuSmlkFirstPonRole_Type.__name__=_E
_HpnicfOnuSmlkFirstPonRole_Object=MibTableColumn
hpnicfOnuSmlkFirstPonRole=_HpnicfOnuSmlkFirstPonRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,30,1,2),_HpnicfOnuSmlkFirstPonRole_Type())
hpnicfOnuSmlkFirstPonRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSmlkFirstPonRole.setStatus(_A)
class _HpnicfOnuSmlkFirstPonStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('standby',2),(_T,3),(_U,4)))
_HpnicfOnuSmlkFirstPonStatus_Type.__name__=_E
_HpnicfOnuSmlkFirstPonStatus_Object=MibTableColumn
hpnicfOnuSmlkFirstPonStatus=_HpnicfOnuSmlkFirstPonStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,30,1,3),_HpnicfOnuSmlkFirstPonStatus_Type())
hpnicfOnuSmlkFirstPonStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSmlkFirstPonStatus.setStatus(_A)
class _HpnicfOnuSmlkSecondPonRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),(_U,3)))
_HpnicfOnuSmlkSecondPonRole_Type.__name__=_E
_HpnicfOnuSmlkSecondPonRole_Object=MibTableColumn
hpnicfOnuSmlkSecondPonRole=_HpnicfOnuSmlkSecondPonRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,30,1,4),_HpnicfOnuSmlkSecondPonRole_Type())
hpnicfOnuSmlkSecondPonRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSmlkSecondPonRole.setStatus(_A)
class _HpnicfOnuSmlkSecondPonStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('standby',2),(_T,3),(_U,4)))
_HpnicfOnuSmlkSecondPonStatus_Type.__name__=_E
_HpnicfOnuSmlkSecondPonStatus_Object=MibTableColumn
hpnicfOnuSmlkSecondPonStatus=_HpnicfOnuSmlkSecondPonStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,30,1,5),_HpnicfOnuSmlkSecondPonStatus_Type())
hpnicfOnuSmlkSecondPonStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuSmlkSecondPonStatus.setStatus(_A)
_HpnicfOnuRS485PropertiesTable_Object=MibTable
hpnicfOnuRS485PropertiesTable=_HpnicfOnuRS485PropertiesTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31))
if mibBuilder.loadTexts:hpnicfOnuRS485PropertiesTable.setStatus(_A)
_HpnicfOnuRS485PropertiesEntry_Object=MibTableRow
hpnicfOnuRS485PropertiesEntry=_HpnicfOnuRS485PropertiesEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1))
hpnicfOnuRS485PropertiesEntry.setIndexNames((0,_D,_F),(0,_G,_S))
if mibBuilder.loadTexts:hpnicfOnuRS485PropertiesEntry.setStatus(_A)
class _HpnicfOnuRS485SerialIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfOnuRS485SerialIndex_Type.__name__=_E
_HpnicfOnuRS485SerialIndex_Object=MibTableColumn
hpnicfOnuRS485SerialIndex=_HpnicfOnuRS485SerialIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,1),_HpnicfOnuRS485SerialIndex_Type())
hpnicfOnuRS485SerialIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuRS485SerialIndex.setStatus(_A)
class _HpnicfOnuRS485BaudRate_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('baudRate300',1),('baudRate600',2),('baudRate1200',3),('baudRate2400',4),('baudRate4800',5),('baudRate9600',6),('baudRate19200',7),('baudRate38400',8),('baudRate57600',9),('baudRate115200',10)))
_HpnicfOnuRS485BaudRate_Type.__name__=_E
_HpnicfOnuRS485BaudRate_Object=MibTableColumn
hpnicfOnuRS485BaudRate=_HpnicfOnuRS485BaudRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,2),_HpnicfOnuRS485BaudRate_Type())
hpnicfOnuRS485BaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuRS485BaudRate.setStatus(_A)
class _HpnicfOnuRS485DataBits_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('five',1),('six',2),('seven',3),('eight',4)))
_HpnicfOnuRS485DataBits_Type.__name__=_E
_HpnicfOnuRS485DataBits_Object=MibTableColumn
hpnicfOnuRS485DataBits=_HpnicfOnuRS485DataBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,3),_HpnicfOnuRS485DataBits_Type())
hpnicfOnuRS485DataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuRS485DataBits.setStatus(_A)
if mibBuilder.loadTexts:hpnicfOnuRS485DataBits.setUnits('bit')
class _HpnicfOnuRS485Parity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3),('mark',4),('space',5)))
_HpnicfOnuRS485Parity_Type.__name__=_E
_HpnicfOnuRS485Parity_Object=MibTableColumn
hpnicfOnuRS485Parity=_HpnicfOnuRS485Parity_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,4),_HpnicfOnuRS485Parity_Type())
hpnicfOnuRS485Parity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuRS485Parity.setStatus(_A)
class _HpnicfOnuRS485StopBits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('one',1),('two',2),('oneAndHalf',3)))
_HpnicfOnuRS485StopBits_Type.__name__=_E
_HpnicfOnuRS485StopBits_Object=MibTableColumn
hpnicfOnuRS485StopBits=_HpnicfOnuRS485StopBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,5),_HpnicfOnuRS485StopBits_Type())
hpnicfOnuRS485StopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuRS485StopBits.setStatus(_A)
if mibBuilder.loadTexts:hpnicfOnuRS485StopBits.setUnits('bit')
class _HpnicfOnuRS485FlowControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('hardware',2),('xonOrxoff',3)))
_HpnicfOnuRS485FlowControl_Type.__name__=_E
_HpnicfOnuRS485FlowControl_Object=MibTableColumn
hpnicfOnuRS485FlowControl=_HpnicfOnuRS485FlowControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,6),_HpnicfOnuRS485FlowControl_Type())
hpnicfOnuRS485FlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuRS485FlowControl.setStatus(_A)
_HpnicfOnuRS485TXOctets_Type=Integer32
_HpnicfOnuRS485TXOctets_Object=MibTableColumn
hpnicfOnuRS485TXOctets=_HpnicfOnuRS485TXOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,7),_HpnicfOnuRS485TXOctets_Type())
hpnicfOnuRS485TXOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRS485TXOctets.setStatus(_A)
_HpnicfOnuRS485RXOctets_Type=Integer32
_HpnicfOnuRS485RXOctets_Object=MibTableColumn
hpnicfOnuRS485RXOctets=_HpnicfOnuRS485RXOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,8),_HpnicfOnuRS485RXOctets_Type())
hpnicfOnuRS485RXOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRS485RXOctets.setStatus(_A)
_HpnicfOnuRS485TXErrOctets_Type=Integer32
_HpnicfOnuRS485TXErrOctets_Object=MibTableColumn
hpnicfOnuRS485TXErrOctets=_HpnicfOnuRS485TXErrOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,9),_HpnicfOnuRS485TXErrOctets_Type())
hpnicfOnuRS485TXErrOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRS485TXErrOctets.setStatus(_A)
_HpnicfOnuRS485RXErrOctets_Type=Integer32
_HpnicfOnuRS485RXErrOctets_Object=MibTableColumn
hpnicfOnuRS485RXErrOctets=_HpnicfOnuRS485RXErrOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,10),_HpnicfOnuRS485RXErrOctets_Type())
hpnicfOnuRS485RXErrOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRS485RXErrOctets.setStatus(_A)
class _HpnicfOnuRS485ResetStatistics_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('counting',1),('clear',2)))
_HpnicfOnuRS485ResetStatistics_Type.__name__=_E
_HpnicfOnuRS485ResetStatistics_Object=MibTableColumn
hpnicfOnuRS485ResetStatistics=_HpnicfOnuRS485ResetStatistics_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,31,1,11),_HpnicfOnuRS485ResetStatistics_Type())
hpnicfOnuRS485ResetStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfOnuRS485ResetStatistics.setStatus(_A)
_HpnicfOnuRS485SessionSummaryTable_Object=MibTable
hpnicfOnuRS485SessionSummaryTable=_HpnicfOnuRS485SessionSummaryTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,32))
if mibBuilder.loadTexts:hpnicfOnuRS485SessionSummaryTable.setStatus(_A)
_HpnicfOnuRS485SessionSummaryEntry_Object=MibTableRow
hpnicfOnuRS485SessionSummaryEntry=_HpnicfOnuRS485SessionSummaryEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,32,1))
hpnicfOnuRS485SessionSummaryEntry.setIndexNames((0,_D,_F),(0,_G,_S))
if mibBuilder.loadTexts:hpnicfOnuRS485SessionSummaryEntry.setStatus(_A)
class _HpnicfOnuRS485SessionMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfOnuRS485SessionMaxNum_Type.__name__=_E
_HpnicfOnuRS485SessionMaxNum_Object=MibTableColumn
hpnicfOnuRS485SessionMaxNum=_HpnicfOnuRS485SessionMaxNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,32,1,1),_HpnicfOnuRS485SessionMaxNum_Type())
hpnicfOnuRS485SessionMaxNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionMaxNum.setStatus(_A)
class _HpnicfOnuRS485SessionNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_HpnicfOnuRS485SessionNextIndex_Type.__name__=_E
_HpnicfOnuRS485SessionNextIndex_Object=MibTableColumn
hpnicfOnuRS485SessionNextIndex=_HpnicfOnuRS485SessionNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,32,1,2),_HpnicfOnuRS485SessionNextIndex_Type())
hpnicfOnuRS485SessionNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionNextIndex.setStatus(_A)
_HpnicfOnuRS485SessionTable_Object=MibTable
hpnicfOnuRS485SessionTable=_HpnicfOnuRS485SessionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33))
if mibBuilder.loadTexts:hpnicfOnuRS485SessionTable.setStatus(_A)
_HpnicfOnuRS485SessionEntry_Object=MibTableRow
hpnicfOnuRS485SessionEntry=_HpnicfOnuRS485SessionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1))
hpnicfOnuRS485SessionEntry.setIndexNames((0,_D,_F),(0,_G,_S),(0,_G,_d))
if mibBuilder.loadTexts:hpnicfOnuRS485SessionEntry.setStatus(_A)
class _HpnicfOnuRS485SessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfOnuRS485SessionIndex_Type.__name__=_E
_HpnicfOnuRS485SessionIndex_Object=MibTableColumn
hpnicfOnuRS485SessionIndex=_HpnicfOnuRS485SessionIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1,1),_HpnicfOnuRS485SessionIndex_Type())
hpnicfOnuRS485SessionIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionIndex.setStatus(_A)
class _HpnicfOnuRS485SessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tcpClient',2),('tcpServer',3)))
_HpnicfOnuRS485SessionType_Type.__name__=_E
_HpnicfOnuRS485SessionType_Object=MibTableColumn
hpnicfOnuRS485SessionType=_HpnicfOnuRS485SessionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1,2),_HpnicfOnuRS485SessionType_Type())
hpnicfOnuRS485SessionType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionType.setStatus(_A)
_HpnicfOnuRS485SessionAddType_Type=InetAddressType
_HpnicfOnuRS485SessionAddType_Object=MibTableColumn
hpnicfOnuRS485SessionAddType=_HpnicfOnuRS485SessionAddType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1,3),_HpnicfOnuRS485SessionAddType_Type())
hpnicfOnuRS485SessionAddType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionAddType.setStatus(_A)
_HpnicfOnuRS485SessionRemoteIP_Type=InetAddress
_HpnicfOnuRS485SessionRemoteIP_Object=MibTableColumn
hpnicfOnuRS485SessionRemoteIP=_HpnicfOnuRS485SessionRemoteIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1,4),_HpnicfOnuRS485SessionRemoteIP_Type())
hpnicfOnuRS485SessionRemoteIP.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionRemoteIP.setStatus(_A)
class _HpnicfOnuRS485SessionRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_HpnicfOnuRS485SessionRemotePort_Type.__name__=_E
_HpnicfOnuRS485SessionRemotePort_Object=MibTableColumn
hpnicfOnuRS485SessionRemotePort=_HpnicfOnuRS485SessionRemotePort_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1,5),_HpnicfOnuRS485SessionRemotePort_Type())
hpnicfOnuRS485SessionRemotePort.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionRemotePort.setStatus(_A)
class _HpnicfOnuRS485SessionLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_HpnicfOnuRS485SessionLocalPort_Type.__name__=_E
_HpnicfOnuRS485SessionLocalPort_Object=MibTableColumn
hpnicfOnuRS485SessionLocalPort=_HpnicfOnuRS485SessionLocalPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1,6),_HpnicfOnuRS485SessionLocalPort_Type())
hpnicfOnuRS485SessionLocalPort.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionLocalPort.setStatus(_A)
_HpnicfOnuRS485SessionRowStatus_Type=RowStatus
_HpnicfOnuRS485SessionRowStatus_Object=MibTableColumn
hpnicfOnuRS485SessionRowStatus=_HpnicfOnuRS485SessionRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,33,1,7),_HpnicfOnuRS485SessionRowStatus_Type())
hpnicfOnuRS485SessionRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionRowStatus.setStatus(_A)
_HpnicfOnuRS485SessionErrInfoTable_Object=MibTable
hpnicfOnuRS485SessionErrInfoTable=_HpnicfOnuRS485SessionErrInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,34))
if mibBuilder.loadTexts:hpnicfOnuRS485SessionErrInfoTable.setStatus(_A)
_HpnicfOnuRS485SessionErrInfoEntry_Object=MibTableRow
hpnicfOnuRS485SessionErrInfoEntry=_HpnicfOnuRS485SessionErrInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,34,1))
hpnicfOnuRS485SessionErrInfoEntry.setIndexNames((0,_D,_F),(0,_G,_S),(0,_G,_d))
if mibBuilder.loadTexts:hpnicfOnuRS485SessionErrInfoEntry.setStatus(_A)
_HpnicfOnuRS485SessionErrInfo_Type=DisplayString
_HpnicfOnuRS485SessionErrInfo_Object=MibTableColumn
hpnicfOnuRS485SessionErrInfo=_HpnicfOnuRS485SessionErrInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,5,34,1,1),_HpnicfOnuRS485SessionErrInfo_Type())
hpnicfOnuRS485SessionErrInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfOnuRS485SessionErrInfo.setStatus(_A)
_HpnicfEponBatchOperationMan_ObjectIdentity=ObjectIdentity
hpnicfEponBatchOperationMan=_HpnicfEponBatchOperationMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6))
_HpnicfEponBatchOperationBySlotTable_Object=MibTable
hpnicfEponBatchOperationBySlotTable=_HpnicfEponBatchOperationBySlotTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,1))
if mibBuilder.loadTexts:hpnicfEponBatchOperationBySlotTable.setStatus(_A)
_HpnicfEponBatchOperationBySlotEntry_Object=MibTableRow
hpnicfEponBatchOperationBySlotEntry=_HpnicfEponBatchOperationBySlotEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,1,1))
hpnicfEponBatchOperationBySlotEntry.setIndexNames((0,_G,_A0))
if mibBuilder.loadTexts:hpnicfEponBatchOperationBySlotEntry.setStatus(_A)
_HpnicfEponBatchOperationBySlotIndex_Type=Integer32
_HpnicfEponBatchOperationBySlotIndex_Object=MibTableColumn
hpnicfEponBatchOperationBySlotIndex=_HpnicfEponBatchOperationBySlotIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,1,1,1),_HpnicfEponBatchOperationBySlotIndex_Type())
hpnicfEponBatchOperationBySlotIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfEponBatchOperationBySlotIndex.setStatus(_A)
class _HpnicfEponBatchOperationBySlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,9,10)));namedValues=NamedValues(*((_A1,1),('updateDba',9),(_A2,10)))
_HpnicfEponBatchOperationBySlotType_Type.__name__=_E
_HpnicfEponBatchOperationBySlotType_Object=MibTableColumn
hpnicfEponBatchOperationBySlotType=_HpnicfEponBatchOperationBySlotType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,1,1,2),_HpnicfEponBatchOperationBySlotType_Type())
hpnicfEponBatchOperationBySlotType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponBatchOperationBySlotType.setStatus(_A)
class _HpnicfEponBatchOperationBySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('batOpBySlot',1))
_HpnicfEponBatchOperationBySlot_Type.__name__=_E
_HpnicfEponBatchOperationBySlot_Object=MibTableColumn
hpnicfEponBatchOperationBySlot=_HpnicfEponBatchOperationBySlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,1,1,3),_HpnicfEponBatchOperationBySlot_Type())
hpnicfEponBatchOperationBySlot.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponBatchOperationBySlot.setStatus(_A)
_HpnicfEponBatchOperationBySlotResult_Type=Integer32
_HpnicfEponBatchOperationBySlotResult_Object=MibTableColumn
hpnicfEponBatchOperationBySlotResult=_HpnicfEponBatchOperationBySlotResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,1,1,4),_HpnicfEponBatchOperationBySlotResult_Type())
hpnicfEponBatchOperationBySlotResult.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponBatchOperationBySlotResult.setStatus(_A)
_HpnicfEponBatchOperationByOLTTable_Object=MibTable
hpnicfEponBatchOperationByOLTTable=_HpnicfEponBatchOperationByOLTTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,2))
if mibBuilder.loadTexts:hpnicfEponBatchOperationByOLTTable.setStatus(_A)
_HpnicfEponBatchOperationByOLTEntry_Object=MibTableRow
hpnicfEponBatchOperationByOLTEntry=_HpnicfEponBatchOperationByOLTEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,2,1))
hpnicfEponBatchOperationByOLTEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfEponBatchOperationByOLTEntry.setStatus(_A)
class _HpnicfEponBatchOperationByOLTType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*((_A1,1),(_A2,5)))
_HpnicfEponBatchOperationByOLTType_Type.__name__=_E
_HpnicfEponBatchOperationByOLTType_Object=MibTableColumn
hpnicfEponBatchOperationByOLTType=_HpnicfEponBatchOperationByOLTType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,2,1,1),_HpnicfEponBatchOperationByOLTType_Type())
hpnicfEponBatchOperationByOLTType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponBatchOperationByOLTType.setStatus(_A)
class _HpnicfEponBatchOperationByOLT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('batOpByOlt',1))
_HpnicfEponBatchOperationByOLT_Type.__name__=_E
_HpnicfEponBatchOperationByOLT_Object=MibTableColumn
hpnicfEponBatchOperationByOLT=_HpnicfEponBatchOperationByOLT_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,2,1,2),_HpnicfEponBatchOperationByOLT_Type())
hpnicfEponBatchOperationByOLT.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponBatchOperationByOLT.setStatus(_A)
_HpnicfEponBatchOperationByOLTResult_Type=Integer32
_HpnicfEponBatchOperationByOLTResult_Object=MibTableColumn
hpnicfEponBatchOperationByOLTResult=_HpnicfEponBatchOperationByOLTResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,2,1,3),_HpnicfEponBatchOperationByOLTResult_Type())
hpnicfEponBatchOperationByOLTResult.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponBatchOperationByOLTResult.setStatus(_A)
_HpnicfOnuFirmwareUpdateByTypeTable_Object=MibTable
hpnicfOnuFirmwareUpdateByTypeTable=_HpnicfOnuFirmwareUpdateByTypeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,3))
if mibBuilder.loadTexts:hpnicfOnuFirmwareUpdateByTypeTable.setStatus(_A)
_HpnicfOnuFirmwareUpdateByTypeEntry_Object=MibTableRow
hpnicfOnuFirmwareUpdateByTypeEntry=_HpnicfOnuFirmwareUpdateByTypeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,3,1))
hpnicfOnuFirmwareUpdateByTypeEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:hpnicfOnuFirmwareUpdateByTypeEntry.setStatus(_A)
_HpnicfOnuUpdateByOnuTypeIndex_Type=Integer32
_HpnicfOnuUpdateByOnuTypeIndex_Object=MibTableColumn
hpnicfOnuUpdateByOnuTypeIndex=_HpnicfOnuUpdateByOnuTypeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,3,1,1),_HpnicfOnuUpdateByOnuTypeIndex_Type())
hpnicfOnuUpdateByOnuTypeIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfOnuUpdateByOnuTypeIndex.setStatus(_A)
class _HpnicfOnuUpdateByTypeOnuType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_HpnicfOnuUpdateByTypeOnuType_Type.__name__=_L
_HpnicfOnuUpdateByTypeOnuType_Object=MibTableColumn
hpnicfOnuUpdateByTypeOnuType=_HpnicfOnuUpdateByTypeOnuType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,3,1,2),_HpnicfOnuUpdateByTypeOnuType_Type())
hpnicfOnuUpdateByTypeOnuType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuUpdateByTypeOnuType.setStatus(_A)
class _HpnicfOnuUpdateByTypeFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfOnuUpdateByTypeFileName_Type.__name__=_L
_HpnicfOnuUpdateByTypeFileName_Object=MibTableColumn
hpnicfOnuUpdateByTypeFileName=_HpnicfOnuUpdateByTypeFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,3,1,3),_HpnicfOnuUpdateByTypeFileName_Type())
hpnicfOnuUpdateByTypeFileName.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuUpdateByTypeFileName.setStatus(_A)
_HpnicfOnuUpdateByTypeRowStatus_Type=RowStatus
_HpnicfOnuUpdateByTypeRowStatus_Object=MibTableColumn
hpnicfOnuUpdateByTypeRowStatus=_HpnicfOnuUpdateByTypeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,6,3,1,4),_HpnicfOnuUpdateByTypeRowStatus_Type())
hpnicfOnuUpdateByTypeRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfOnuUpdateByTypeRowStatus.setStatus(_A)
_HpnicfEponErrorInfo_ObjectIdentity=ObjectIdentity
hpnicfEponErrorInfo=_HpnicfEponErrorInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7))
_HpnicfEponSoftwareErrorCode_Type=Integer32
_HpnicfEponSoftwareErrorCode_Object=MibScalar
hpnicfEponSoftwareErrorCode=_HpnicfEponSoftwareErrorCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,1),_HpnicfEponSoftwareErrorCode_Type())
hpnicfEponSoftwareErrorCode.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponSoftwareErrorCode.setStatus(_A)
_HpnicfOamVendorSpecificAlarmCode_Type=Integer32
_HpnicfOamVendorSpecificAlarmCode_Object=MibScalar
hpnicfOamVendorSpecificAlarmCode=_HpnicfOamVendorSpecificAlarmCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,2),_HpnicfOamVendorSpecificAlarmCode_Type())
hpnicfOamVendorSpecificAlarmCode.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfOamVendorSpecificAlarmCode.setStatus(_A)
_HpnicfEponOnuRegErrorMacAddr_Type=OctetString
_HpnicfEponOnuRegErrorMacAddr_Object=MibScalar
hpnicfEponOnuRegErrorMacAddr=_HpnicfEponOnuRegErrorMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,3),_HpnicfEponOnuRegErrorMacAddr_Type())
hpnicfEponOnuRegErrorMacAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponOnuRegErrorMacAddr.setStatus(_A)
_HpnicfOamEventLogType_Type=Unsigned32
_HpnicfOamEventLogType_Object=MibScalar
hpnicfOamEventLogType=_HpnicfOamEventLogType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,4),_HpnicfOamEventLogType_Type())
hpnicfOamEventLogType.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfOamEventLogType.setStatus(_A)
class _HpnicfOamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_HpnicfOamEventLogLocation_Type.__name__=_E
_HpnicfOamEventLogLocation_Object=MibScalar
hpnicfOamEventLogLocation=_HpnicfOamEventLogLocation_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,5),_HpnicfOamEventLogLocation_Type())
hpnicfOamEventLogLocation.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfOamEventLogLocation.setStatus(_A)
_HpnicfEponLoopbackPortIndex_Type=Integer32
_HpnicfEponLoopbackPortIndex_Object=MibScalar
hpnicfEponLoopbackPortIndex=_HpnicfEponLoopbackPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,6),_HpnicfEponLoopbackPortIndex_Type())
hpnicfEponLoopbackPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponLoopbackPortIndex.setStatus(_A)
class _HpnicfEponLoopbackPortDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponLoopbackPortDescr_Type.__name__=_L
_HpnicfEponLoopbackPortDescr_Object=MibScalar
hpnicfEponLoopbackPortDescr=_HpnicfEponLoopbackPortDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,7),_HpnicfEponLoopbackPortDescr_Type())
hpnicfEponLoopbackPortDescr.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponLoopbackPortDescr.setStatus(_A)
_HpnicfOltPortAlarmLlidMisFrames_Type=Unsigned32
_HpnicfOltPortAlarmLlidMisFrames_Object=MibScalar
hpnicfOltPortAlarmLlidMisFrames=_HpnicfOltPortAlarmLlidMisFrames_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,8),_HpnicfOltPortAlarmLlidMisFrames_Type())
hpnicfOltPortAlarmLlidMisFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfOltPortAlarmLlidMisFrames.setStatus(_A)
_HpnicfOltPortAlarmBer_Type=Unsigned32
_HpnicfOltPortAlarmBer_Object=MibScalar
hpnicfOltPortAlarmBer=_HpnicfOltPortAlarmBer_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,9),_HpnicfOltPortAlarmBer_Type())
hpnicfOltPortAlarmBer.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfOltPortAlarmBer.setStatus(_A)
_HpnicfOltPortAlarmFer_Type=Unsigned32
_HpnicfOltPortAlarmFer_Object=MibScalar
hpnicfOltPortAlarmFer=_HpnicfOltPortAlarmFer_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,10),_HpnicfOltPortAlarmFer_Type())
hpnicfOltPortAlarmFer.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfOltPortAlarmFer.setStatus(_A)
_HpnicfEponOnuRegSilentMac_Type=OctetString
_HpnicfEponOnuRegSilentMac_Object=MibScalar
hpnicfEponOnuRegSilentMac=_HpnicfEponOnuRegSilentMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,11),_HpnicfEponOnuRegSilentMac_Type())
hpnicfEponOnuRegSilentMac.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponOnuRegSilentMac.setStatus(_A)
class _HpnicfEponOperationResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponOperationResult_Type.__name__=_L
_HpnicfEponOperationResult_Object=MibScalar
hpnicfEponOperationResult=_HpnicfEponOperationResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,12),_HpnicfEponOperationResult_Type())
hpnicfEponOperationResult.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponOperationResult.setStatus(_A)
class _HpnicfEponOnuLaserState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('laserAlwaysOn',2),('signalDegradation',3),('endOfLife',4)))
_HpnicfEponOnuLaserState_Type.__name__=_E
_HpnicfEponOnuLaserState_Object=MibScalar
hpnicfEponOnuLaserState=_HpnicfEponOnuLaserState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,7,13),_HpnicfEponOnuLaserState_Type())
hpnicfEponOnuLaserState.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEponOnuLaserState.setStatus(_A)
_HpnicfEponTrap_ObjectIdentity=ObjectIdentity
hpnicfEponTrap=_HpnicfEponTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8))
_HpnicfEponTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfEponTrapPrefix=_HpnicfEponTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0))
_HpnicfEponStat_ObjectIdentity=ObjectIdentity
hpnicfEponStat=_HpnicfEponStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,1,9))
_HpnicfEponStatTable_Object=MibTable
hpnicfEponStatTable=_HpnicfEponStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,9,1))
if mibBuilder.loadTexts:hpnicfEponStatTable.setStatus(_A)
_HpnicfEponStatEntry_Object=MibTableRow
hpnicfEponStatEntry=_HpnicfEponStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,9,1,1))
hpnicfEponStatEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfEponStatEntry.setStatus(_A)
_HpnicfEponStatFER_Type=Counter64
_HpnicfEponStatFER_Object=MibTableColumn
hpnicfEponStatFER=_HpnicfEponStatFER_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,9,1,1,1),_HpnicfEponStatFER_Type())
hpnicfEponStatFER.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponStatFER.setStatus(_A)
_HpnicfEponStatBER_Type=Counter64
_HpnicfEponStatBER_Object=MibTableColumn
hpnicfEponStatBER=_HpnicfEponStatBER_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,1,9,1,1,2),_HpnicfEponStatBER_Type())
hpnicfEponStatBER.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponStatBER.setStatus(_A)
hpnicfEponPortAlarmBerTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,1))
hpnicfEponPortAlarmBerTrap.setObjects(*((_D,_F),(_D,_I),(_G,_e),(_G,_A4),(_G,_A5)))
if mibBuilder.loadTexts:hpnicfEponPortAlarmBerTrap.setStatus(_A)
hpnicfEponPortAlarmFerTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,2))
hpnicfEponPortAlarmFerTrap.setObjects(*((_D,_F),(_D,_I),(_G,_f),(_G,_A6),(_G,_A7)))
if mibBuilder.loadTexts:hpnicfEponPortAlarmFerTrap.setStatus(_A)
hpnicfEponErrorLLIDFrameTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,3))
hpnicfEponErrorLLIDFrameTrap.setObjects(*((_D,_F),(_D,_I),(_G,_A8),(_G,_A9)))
if mibBuilder.loadTexts:hpnicfEponErrorLLIDFrameTrap.setStatus(_A)
hpnicfEponLoopBackEnableTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,4))
hpnicfEponLoopBackEnableTrap.setObjects(*((_D,_F),(_D,_I),(_G,_AA),(_G,_AB)))
if mibBuilder.loadTexts:hpnicfEponLoopBackEnableTrap.setStatus(_A)
hpnicfEponOnuRegistrationErrTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,5))
hpnicfEponOnuRegistrationErrTrap.setObjects(*((_D,_F),(_D,_I),(_G,_g)))
if mibBuilder.loadTexts:hpnicfEponOnuRegistrationErrTrap.setStatus(_A)
hpnicfEponOamDisconnectionTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,6))
hpnicfEponOamDisconnectionTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOamDisconnectionTrap.setStatus(_A)
hpnicfEponEncryptionKeyErrTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,7))
hpnicfEponEncryptionKeyErrTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponEncryptionKeyErrTrap.setStatus(_A)
hpnicfEponRemoteStableTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,8))
hpnicfEponRemoteStableTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponRemoteStableTrap.setStatus(_A)
hpnicfEponLocalStableTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,9))
hpnicfEponLocalStableTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponLocalStableTrap.setStatus(_A)
hpnicfEponOamVendorSpecificTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,10))
hpnicfEponOamVendorSpecificTrap.setObjects(*((_D,_F),(_D,_I),(_G,_h)))
if mibBuilder.loadTexts:hpnicfEponOamVendorSpecificTrap.setStatus(_A)
hpnicfEponSoftwareErrTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,11))
hpnicfEponSoftwareErrTrap.setObjects(*((_P,_V),(_P,_W),(_G,_i)))
if mibBuilder.loadTexts:hpnicfEponSoftwareErrTrap.setStatus(_A)
hpnicfEponPortAlarmBerRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,12))
hpnicfEponPortAlarmBerRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_e)))
if mibBuilder.loadTexts:hpnicfEponPortAlarmBerRecoverTrap.setStatus(_A)
hpnicfEponPortAlarmFerRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,13))
hpnicfEponPortAlarmFerRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_f)))
if mibBuilder.loadTexts:hpnicfEponPortAlarmFerRecoverTrap.setStatus(_A)
hpnicfEponErrorLLIDFrameRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,14))
hpnicfEponErrorLLIDFrameRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponErrorLLIDFrameRecoverTrap.setStatus(_A)
hpnicfEponLoopBackEnableRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,15))
hpnicfEponLoopBackEnableRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponLoopBackEnableRecoverTrap.setStatus(_A)
hpnicfEponOnuRegistrationErrRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,16))
hpnicfEponOnuRegistrationErrRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_g)))
if mibBuilder.loadTexts:hpnicfEponOnuRegistrationErrRecoverTrap.setStatus(_A)
hpnicfEponOamDisconnectionRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,17))
hpnicfEponOamDisconnectionRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOamDisconnectionRecoverTrap.setStatus(_A)
hpnicfEponEncryptionKeyErrRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,18))
hpnicfEponEncryptionKeyErrRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponEncryptionKeyErrRecoverTrap.setStatus(_A)
hpnicfEponRemoteStableRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,19))
hpnicfEponRemoteStableRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponRemoteStableRecoverTrap.setStatus(_A)
hpnicfEponLocalStableRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,20))
hpnicfEponLocalStableRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponLocalStableRecoverTrap.setStatus(_A)
hpnicfEponOamVendorSpecificRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,21))
hpnicfEponOamVendorSpecificRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_h)))
if mibBuilder.loadTexts:hpnicfEponOamVendorSpecificRecoverTrap.setStatus(_A)
hpnicfEponSoftwareErrRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,22))
hpnicfEponSoftwareErrRecoverTrap.setObjects(*((_P,_V),(_P,_W),(_G,_i)))
if mibBuilder.loadTexts:hpnicfEponSoftwareErrRecoverTrap.setStatus(_A)
hpnicfDot3OamThresholdRecoverEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,23))
hpnicfDot3OamThresholdRecoverEvent.setObjects(*((_D,_F),(_G,_j),(_G,_k)))
if mibBuilder.loadTexts:hpnicfDot3OamThresholdRecoverEvent.setStatus(_A)
hpnicfDot3OamNonThresholdRecoverEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,24))
hpnicfDot3OamNonThresholdRecoverEvent.setObjects(*((_D,_F),(_G,_j),(_G,_k)))
if mibBuilder.loadTexts:hpnicfDot3OamNonThresholdRecoverEvent.setStatus(_A)
hpnicfEponOnuRegExcessTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,25))
hpnicfEponOnuRegExcessTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOnuRegExcessTrap.setStatus(_A)
hpnicfEponOnuRegExcessRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,26))
hpnicfEponOnuRegExcessRecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOnuRegExcessRecoverTrap.setStatus(_A)
hpnicfEponOnuPowerOffTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,27))
hpnicfEponOnuPowerOffTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOnuPowerOffTrap.setStatus(_A)
hpnicfEponOltSwitchoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,28))
hpnicfEponOltSwitchoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOltSwitchoverTrap.setStatus(_A)
hpnicfEponOltDFETrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,29))
hpnicfEponOltDFETrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOltDFETrap.setStatus(_A)
hpnicfEponOltDFERecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,30))
hpnicfEponOltDFERecoverTrap.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:hpnicfEponOltDFERecoverTrap.setStatus(_A)
hpnicfEponOnuSilenceTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,31))
hpnicfEponOnuSilenceTrap.setObjects(*((_D,_F),(_D,_I),(_G,_l)))
if mibBuilder.loadTexts:hpnicfEponOnuSilenceTrap.setStatus(_A)
hpnicfEponOnuSilenceRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,32))
hpnicfEponOnuSilenceRecoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_l)))
if mibBuilder.loadTexts:hpnicfEponOnuSilenceRecoverTrap.setStatus(_A)
hpnicfEponOnuUpdateResultTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,33))
hpnicfEponOnuUpdateResultTrap.setObjects(*((_D,_F),(_D,_I),(_G,_m),(_G,_AC),(_G,_AD),(_G,_AE)))
if mibBuilder.loadTexts:hpnicfEponOnuUpdateResultTrap.setStatus(_A)
hpnicfEponOnuAutoBindTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,34))
hpnicfEponOnuAutoBindTrap.setObjects(*((_D,_F),(_D,_I),(_G,_m),(_G,_AF)))
if mibBuilder.loadTexts:hpnicfEponOnuAutoBindTrap.setStatus(_A)
hpnicfEponOnuPortStpStateTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,35))
hpnicfEponOnuPortStpStateTrap.setObjects(*((_D,_F),(_D,_I),(_G,_b),(_G,_AG),(_G,_AH)))
if mibBuilder.loadTexts:hpnicfEponOnuPortStpStateTrap.setStatus(_A)
hpnicfEponOnuLaserFailedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,36))
hpnicfEponOnuLaserFailedTrap.setObjects(*((_D,_F),(_D,_I),(_G,_AI)))
if mibBuilder.loadTexts:hpnicfEponOnuLaserFailedTrap.setStatus(_A)
hpnicfOnuSmlkSwitchoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,1,8,0,37))
hpnicfOnuSmlkSwitchoverTrap.setObjects(*((_D,_F),(_D,_I),(_G,_c),(_G,_AJ),(_G,_AK)))
if mibBuilder.loadTexts:hpnicfOnuSmlkSwitchoverTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hpnicfEponMibObjects':hpnicfEponMibObjects,'hpnicfEponSysMan':hpnicfEponSysMan,'hpnicfEponAutoAuthorize':hpnicfEponAutoAuthorize,'hpnicfEponMonitorCycle':hpnicfEponMonitorCycle,'hpnicfEponMsgTimeOut':hpnicfEponMsgTimeOut,'hpnicfEponMsgLoseNum':hpnicfEponMsgLoseNum,'hpnicfEponSysHasEPONBoard':hpnicfEponSysHasEPONBoard,'hpnicfEponMonitorCycleEnable':hpnicfEponMonitorCycleEnable,'hpnicfEponOltSoftwareErrAlmEnable':hpnicfEponOltSoftwareErrAlmEnable,'hpnicfEponPortLoopBackAlmEnable':hpnicfEponPortLoopBackAlmEnable,'hpnicfEponMonitorCycleMinVal':hpnicfEponMonitorCycleMinVal,'hpnicfEponMonitorCycleMaxVal':hpnicfEponMonitorCycleMaxVal,'hpnicfEponMsgTimeOutMinVal':hpnicfEponMsgTimeOutMinVal,'hpnicfEponMsgTimeOutMaxVal':hpnicfEponMsgTimeOutMaxVal,'hpnicfEponMsgLoseNumMinVal':hpnicfEponMsgLoseNumMinVal,'hpnicfEponMsgLoseNumMaxVal':hpnicfEponMsgLoseNumMaxVal,'hpnicfEponSysScalarGroup':hpnicfEponSysScalarGroup,'hpnicfEponSysManTable':hpnicfEponSysManTable,'hpnicfEponSysManEntry':hpnicfEponSysManEntry,_Q:hpnicfEponSlotIndex,'hpnicfEponModeSwitch':hpnicfEponModeSwitch,'hpnicfEponAutomaticMode':hpnicfEponAutomaticMode,'hpnicfEponOamDiscoveryTimeout':hpnicfEponOamDiscoveryTimeout,'hpnicfEponEncryptionNoReplyTimeOut':hpnicfEponEncryptionNoReplyTimeOut,'hpnicfEponEncryptionUpdateTime':hpnicfEponEncryptionUpdateTime,'hpnicfEponAutoBindStatus':hpnicfEponAutoBindStatus,'hpnicfEponAutoUpdateTable':hpnicfEponAutoUpdateTable,'hpnicfEponAutoUpdateEntry':hpnicfEponAutoUpdateEntry,'hpnicfEponAutoUpdateFileName':hpnicfEponAutoUpdateFileName,'hpnicfEponAutoUpdateSchedStatus':hpnicfEponAutoUpdateSchedStatus,'hpnicfEponAutoUpdateSchedTime':hpnicfEponAutoUpdateSchedTime,'hpnicfEponAutoUpdateSchedType':hpnicfEponAutoUpdateSchedType,'hpnicfEponAutoUpdateRealTimeStatus':hpnicfEponAutoUpdateRealTimeStatus,'hpnicfEponOuiIndexNextTable':hpnicfEponOuiIndexNextTable,'hpnicfEponOuiIndexNextEntry':hpnicfEponOuiIndexNextEntry,'hpnicfEponOuiIndexNext':hpnicfEponOuiIndexNext,'hpnicfEponOuiTable':hpnicfEponOuiTable,'hpnicfEponOuiEntry':hpnicfEponOuiEntry,_n:hpnicfEponOuiIndex,'hpnicfEponOuiValue':hpnicfEponOuiValue,'hpnicfEponOamVersion':hpnicfEponOamVersion,'hpnicfEponOuiRowStatus':hpnicfEponOuiRowStatus,'hpnicfEponMulticastControlTable':hpnicfEponMulticastControlTable,'hpnicfEponMulticastControlEntry':hpnicfEponMulticastControlEntry,_o:hpnicfEponMulticastVlanId,'hpnicfEponMulticastAddressList':hpnicfEponMulticastAddressList,'hpnicfEponMulticastStatus':hpnicfEponMulticastStatus,'hpnicfEponFileName':hpnicfEponFileName,'hpnicfEponDbaUpdateFileName':hpnicfEponDbaUpdateFileName,'hpnicfEponOnuUpdateFileName':hpnicfEponOnuUpdateFileName,'hpnicfEponOltMan':hpnicfEponOltMan,'hpnicfOltSysManTable':hpnicfOltSysManTable,'hpnicfOltSysManEntry':hpnicfOltSysManEntry,'hpnicfOltLaserOnTime':hpnicfOltLaserOnTime,'hpnicfOltLaserOffTime':hpnicfOltLaserOffTime,'hpnicfOltMultiCopyBrdCast':hpnicfOltMultiCopyBrdCast,'hpnicfOltEnableDiscardPacket':hpnicfOltEnableDiscardPacket,'hpnicfOltSelfTest':hpnicfOltSelfTest,'hpnicfOltSelfTestResult':hpnicfOltSelfTestResult,'hpnicfOltMaxRtt':hpnicfOltMaxRtt,'hpnicfOltInfoTable':hpnicfOltInfoTable,'hpnicfOltInfoEntry':hpnicfOltInfoEntry,'hpnicfOltFirmMajorVersion':hpnicfOltFirmMajorVersion,'hpnicfOltFirmMinorVersion':hpnicfOltFirmMinorVersion,'hpnicfOltHardMajorVersion':hpnicfOltHardMajorVersion,'hpnicfOltHardMinorVersion':hpnicfOltHardMinorVersion,'hpnicfOltAgcLockTime':hpnicfOltAgcLockTime,'hpnicfOltAgcCdrTime':hpnicfOltAgcCdrTime,'hpnicfOltMacAddress':hpnicfOltMacAddress,'hpnicfOltWorkMode':hpnicfOltWorkMode,'hpnicfOltOpticalPowerTx':hpnicfOltOpticalPowerTx,'hpnicfOltOpticalPowerRx':hpnicfOltOpticalPowerRx,'hpnicfOltDbaManTable':hpnicfOltDbaManTable,'hpnicfOltDbaManEntry':hpnicfOltDbaManEntry,'hpnicfOltDbaEnabledType':hpnicfOltDbaEnabledType,'hpnicfOltDbaDiscoveryLength':hpnicfOltDbaDiscoveryLength,'hpnicfOltDbaDiscovryFrequency':hpnicfOltDbaDiscovryFrequency,'hpnicfOltDbaCycleLength':hpnicfOltDbaCycleLength,'hpnicfOltDbaVersion':hpnicfOltDbaVersion,'hpnicfOltDbaUpdate':hpnicfOltDbaUpdate,'hpnicfOltDbaUpdateResult':hpnicfOltDbaUpdateResult,'hpnicfOltPortAlarmThresholdTable':hpnicfOltPortAlarmThresholdTable,'hpnicfOltPortAlarmThresholdEntry':hpnicfOltPortAlarmThresholdEntry,'hpnicfOltPortAlarmBerEnabled':hpnicfOltPortAlarmBerEnabled,_e:hpnicfOltPortAlarmBerDirect,_A5:hpnicfOltPortAlarmBerThreshold,'hpnicfOltPortAlarmFerEnabled':hpnicfOltPortAlarmFerEnabled,_f:hpnicfOltPortAlarmFerDirect,_A7:hpnicfOltPortAlarmFerThreshold,'hpnicfOltPortAlarmLlidMismatchEnabled':hpnicfOltPortAlarmLlidMismatchEnabled,_A9:hpnicfOltPortAlarmLlidMismatchThreshold,'hpnicfOltPortAlarmRemoteStableEnabled':hpnicfOltPortAlarmRemoteStableEnabled,'hpnicfOltPortAlarmLocalStableEnabled':hpnicfOltPortAlarmLocalStableEnabled,'hpnicfOltPortAlarmRegistrationEnabled':hpnicfOltPortAlarmRegistrationEnabled,'hpnicfOltPortAlarmOamDisconnectionEnabled':hpnicfOltPortAlarmOamDisconnectionEnabled,'hpnicfOltPortAlarmEncryptionKeyEnabled':hpnicfOltPortAlarmEncryptionKeyEnabled,'hpnicfOltPortAlarmVendorSpecificEnabled':hpnicfOltPortAlarmVendorSpecificEnabled,'hpnicfOltPortAlarmRegExcessEnabled':hpnicfOltPortAlarmRegExcessEnabled,'hpnicfOltPortAlarmDFEEnabled':hpnicfOltPortAlarmDFEEnabled,'hpnicfOltLaserOnTimeMinVal':hpnicfOltLaserOnTimeMinVal,'hpnicfOltLaserOnTimeMaxVal':hpnicfOltLaserOnTimeMaxVal,'hpnicfOltLaserOffTimeMinVal':hpnicfOltLaserOffTimeMinVal,'hpnicfOltLaserOffTimeMaxVal':hpnicfOltLaserOffTimeMaxVal,'hpnicfOltDbaDiscoveryLengthMinVal':hpnicfOltDbaDiscoveryLengthMinVal,'hpnicfOltDbaDiscoveryLengthMaxVal':hpnicfOltDbaDiscoveryLengthMaxVal,'hpnicfOltDbaDiscovryFrequencyMinVal':hpnicfOltDbaDiscovryFrequencyMinVal,'hpnicfOltDbaDiscovryFrequencyMaxVal':hpnicfOltDbaDiscovryFrequencyMaxVal,'hpnicfOltDbaCycleLengthMinVal':hpnicfOltDbaCycleLengthMinVal,'hpnicfOltDbaCycleLengthMaxVal':hpnicfOltDbaCycleLengthMaxVal,'hpnicfOltPortAlarmLlidMisMinVal':hpnicfOltPortAlarmLlidMisMinVal,'hpnicfOltPortAlarmLlidMisMaxVal':hpnicfOltPortAlarmLlidMisMaxVal,'hpnicfOltPortAlarmBerMinVal':hpnicfOltPortAlarmBerMinVal,'hpnicfOltPortAlarmBerMaxVal':hpnicfOltPortAlarmBerMaxVal,'hpnicfOltPortAlarmFerMinVal':hpnicfOltPortAlarmFerMinVal,'hpnicfOltPortAlarmFerMaxVal':hpnicfOltPortAlarmFerMaxVal,'hpnicfOnuSilentTable':hpnicfOnuSilentTable,'hpnicfOnuSilentEntry':hpnicfOnuSilentEntry,_s:hpnicfOnuSilentMacAddr,'hpnicfOnuSilentTime':hpnicfOnuSilentTime,'hpnicfOltUsingOnuTable':hpnicfOltUsingOnuTable,'hpnicfOltUsingOnuEntry':hpnicfOltUsingOnuEntry,_t:hpnicfOltUsingOnuNum,'hpnicfOltUsingOnuIfIndex':hpnicfOltUsingOnuIfIndex,'hpnicfOltUsingOnuRowStatus':hpnicfOltUsingOnuRowStatus,'hpnicfEponOnuMan':hpnicfEponOnuMan,'hpnicfOnuSysManTable':hpnicfOnuSysManTable,'hpnicfOnuSysManEntry':hpnicfOnuSysManEntry,'hpnicfOnuEncryptMan':hpnicfOnuEncryptMan,'hpnicfOnuReAuthorize':hpnicfOnuReAuthorize,'hpnicfOnuMulticastFilterStatus':hpnicfOnuMulticastFilterStatus,'hpnicfOnuDbaReportQueueSetNumber':hpnicfOnuDbaReportQueueSetNumber,'hpnicfOnuRemoteFecStatus':hpnicfOnuRemoteFecStatus,'hpnicfOnuPortBerStatus':hpnicfOnuPortBerStatus,'hpnicfOnuReset':hpnicfOnuReset,'hpnicfOnuMulticastControlMode':hpnicfOnuMulticastControlMode,'hpnicfOnuAccessVlan':hpnicfOnuAccessVlan,'hpnicfOnuEncryptKey':hpnicfOnuEncryptKey,'hpnicfOnuUniUpDownTrapStatus':hpnicfOnuUniUpDownTrapStatus,'hpnicfOnuFecStatus':hpnicfOnuFecStatus,'hpnicfOnuMcastCtrlHostAgingTime':hpnicfOnuMcastCtrlHostAgingTime,'hpnicfOnuMulticastFastLeaveEnable':hpnicfOnuMulticastFastLeaveEnable,'hpnicfOnuPortIsolateEnable':hpnicfOnuPortIsolateEnable,'hpnicfOnuLinkTestTable':hpnicfOnuLinkTestTable,'hpnicfOnuLinkTestEntry':hpnicfOnuLinkTestEntry,'hpnicfOnuLinkTestFrameNum':hpnicfOnuLinkTestFrameNum,'hpnicfOnuLinkTestFrameSize':hpnicfOnuLinkTestFrameSize,'hpnicfOnuLinkTestDelay':hpnicfOnuLinkTestDelay,'hpnicfOnuLinkTestVlanTag':hpnicfOnuLinkTestVlanTag,'hpnicfOnuLinkTestVlanPriority':hpnicfOnuLinkTestVlanPriority,'hpnicfOnuLinkTestVlanTagID':hpnicfOnuLinkTestVlanTagID,'hpnicfOnuLinkTestResultSentFrameNum':hpnicfOnuLinkTestResultSentFrameNum,'hpnicfOnuLinkTestResultRetFrameNum':hpnicfOnuLinkTestResultRetFrameNum,'hpnicfOnuLinkTestResultRetErrFrameNum':hpnicfOnuLinkTestResultRetErrFrameNum,'hpnicfOnuLinkTestResultMinDelay':hpnicfOnuLinkTestResultMinDelay,'hpnicfOnuLinkTestResultMeanDelay':hpnicfOnuLinkTestResultMeanDelay,'hpnicfOnuLinkTestResultMaxDelay':hpnicfOnuLinkTestResultMaxDelay,'hpnicfOnuBandWidthTable':hpnicfOnuBandWidthTable,'hpnicfOnuBandWidthEntry':hpnicfOnuBandWidthEntry,'hpnicfOnuDownStreamBandWidthPolicy':hpnicfOnuDownStreamBandWidthPolicy,'hpnicfOnuDownStreamMaxBandWidth':hpnicfOnuDownStreamMaxBandWidth,'hpnicfOnuDownStreamMaxBurstSize':hpnicfOnuDownStreamMaxBurstSize,'hpnicfOnuDownStreamHighPriorityFirst':hpnicfOnuDownStreamHighPriorityFirst,'hpnicfOnuDownStreamShortFrameFirst':hpnicfOnuDownStreamShortFrameFirst,'hpnicfOnuP2PBandWidthPolicy':hpnicfOnuP2PBandWidthPolicy,'hpnicfOnuP2PMaxBandWidth':hpnicfOnuP2PMaxBandWidth,'hpnicfOnuP2PMaxBurstSize':hpnicfOnuP2PMaxBurstSize,'hpnicfOnuP2PHighPriorityFirst':hpnicfOnuP2PHighPriorityFirst,'hpnicfOnuP2PShortFrameFirst':hpnicfOnuP2PShortFrameFirst,'hpnicfOnuSlaManTable':hpnicfOnuSlaManTable,'hpnicfOnuSlaManEntry':hpnicfOnuSlaManEntry,'hpnicfOnuSlaMaxBandWidth':hpnicfOnuSlaMaxBandWidth,'hpnicfOnuSlaMinBandWidth':hpnicfOnuSlaMinBandWidth,'hpnicfOnuSlaBandWidthStepVal':hpnicfOnuSlaBandWidthStepVal,'hpnicfOnuSlaDelay':hpnicfOnuSlaDelay,'hpnicfOnuSlaFixedBandWidth':hpnicfOnuSlaFixedBandWidth,'hpnicfOnuSlaPriorityClass':hpnicfOnuSlaPriorityClass,'hpnicfOnuSlaFixedPacketSize':hpnicfOnuSlaFixedPacketSize,'hpnicfOnuInfoTable':hpnicfOnuInfoTable,'hpnicfOnuInfoEntry':hpnicfOnuInfoEntry,'hpnicfOnuHardMajorVersion':hpnicfOnuHardMajorVersion,'hpnicfOnuHardMinorVersion':hpnicfOnuHardMinorVersion,'hpnicfOnuSoftwareVersion':hpnicfOnuSoftwareVersion,'hpnicfOnuUniMacType':hpnicfOnuUniMacType,'hpnicfOnuLaserOnTime':hpnicfOnuLaserOnTime,'hpnicfOnuLaserOffTime':hpnicfOnuLaserOffTime,'hpnicfOnuGrantFifoDep':hpnicfOnuGrantFifoDep,'hpnicfOnuWorkMode':hpnicfOnuWorkMode,'hpnicfOnuPCBVersion':hpnicfOnuPCBVersion,'hpnicfOnuRtt':hpnicfOnuRtt,'hpnicfOnuEEPROMVersion':hpnicfOnuEEPROMVersion,_AD:hpnicfOnuRegType,'hpnicfOnuHostType':hpnicfOnuHostType,'hpnicfOnuDistance':hpnicfOnuDistance,'hpnicfOnuLlid':hpnicfOnuLlid,'hpnicfOnuVendorId':hpnicfOnuVendorId,'hpnicfOnuFirmwareVersion':hpnicfOnuFirmwareVersion,'hpnicfOnuOpticalPowerReceivedByOlt':hpnicfOnuOpticalPowerReceivedByOlt,'hpnicfOnuMacAddrInfoTable':hpnicfOnuMacAddrInfoTable,'hpnicfOnuMacAddrInfoEntry':hpnicfOnuMacAddrInfoEntry,_u:hpnicfOnuMacIndex,'hpnicfOnuMacAddrFlag':hpnicfOnuMacAddrFlag,'hpnicfOnuMacAddress':hpnicfOnuMacAddress,'hpnicfOnuBindMacAddrTable':hpnicfOnuBindMacAddrTable,'hpnicfOnuBindMacAddrEntry':hpnicfOnuBindMacAddrEntry,_m:hpnicfOnuBindMacAddress,'hpnicfOnuBindType':hpnicfOnuBindType,'hpnicfOnuFirmwareUpdateTable':hpnicfOnuFirmwareUpdateTable,'hpnicfOnuFirmwareUpdateEntry':hpnicfOnuFirmwareUpdateEntry,'hpnicfOnuUpdate':hpnicfOnuUpdate,_AC:hpnicfOnuUpdateResult,_AE:hpnicfOnuUpdateFileName,'hpnicfOnuLinkTestFrameNumMinVal':hpnicfOnuLinkTestFrameNumMinVal,'hpnicfOnuLinkTestFrameNumMaxVal':hpnicfOnuLinkTestFrameNumMaxVal,'hpnicfOnuSlaMaxBandWidthMinVal':hpnicfOnuSlaMaxBandWidthMinVal,'hpnicfOnuSlaMaxBandWidthMaxVal':hpnicfOnuSlaMaxBandWidthMaxVal,'hpnicfOnuSlaMinBandWidthMinVal':hpnicfOnuSlaMinBandWidthMinVal,'hpnicfOnuSlaMinBandWidthMaxVal':hpnicfOnuSlaMinBandWidthMaxVal,'hpnicfEponOnuTypeManTable':hpnicfEponOnuTypeManTable,'hpnicfEponOnuTypeManEntry':hpnicfEponOnuTypeManEntry,_v:hpnicfEponOnuTypeIndex,'hpnicfEponOnuTypeDescr':hpnicfEponOnuTypeDescr,'hpnicfOnuPacketManTable':hpnicfOnuPacketManTable,'hpnicfOnuPacketManEntry':hpnicfOnuPacketManEntry,'hpnicfOnuPriorityTrust':hpnicfOnuPriorityTrust,'hpnicfOnuQueueScheduler':hpnicfOnuQueueScheduler,'hpnicfOnuProtocolTable':hpnicfOnuProtocolTable,'hpnicfOnuProtocolEntry':hpnicfOnuProtocolEntry,'hpnicfOnuStpStatus':hpnicfOnuStpStatus,'hpnicfOnuIgmpSnoopingStatus':hpnicfOnuIgmpSnoopingStatus,'hpnicfOnuDhcpsnoopingOption82':hpnicfOnuDhcpsnoopingOption82,'hpnicfOnuDhcpsnooping':hpnicfOnuDhcpsnooping,'hpnicfOnuPppoe':hpnicfOnuPppoe,'hpnicfOnuIgmpSnoopingHostAgingT':hpnicfOnuIgmpSnoopingHostAgingT,'hpnicfOnuIgmpSnoopingMaxRespT':hpnicfOnuIgmpSnoopingMaxRespT,'hpnicfOnuIgmpSnoopingRouterAgingT':hpnicfOnuIgmpSnoopingRouterAgingT,'hpnicfOnuIgmpSnoopingAggReportS':hpnicfOnuIgmpSnoopingAggReportS,'hpnicfOnuIgmpSnoopingAggLeaveS':hpnicfOnuIgmpSnoopingAggLeaveS,'hpnicfOnuDot1xTable':hpnicfOnuDot1xTable,'hpnicfOnuDot1xEntry':hpnicfOnuDot1xEntry,'hpnicfOnuDot1xAccount':hpnicfOnuDot1xAccount,'hpnicfOnuDot1xPassword':hpnicfOnuDot1xPassword,'hpnicfOnuPriorityQueueTable':hpnicfOnuPriorityQueueTable,'hpnicfOnuPriorityQueueEntry':hpnicfOnuPriorityQueueEntry,_Z:hpnicfOnuQueueDirection,_a:hpnicfOnuQueueId,'hpnicfOnuQueueSize':hpnicfOnuQueueSize,'hpnicfOnuCountTable':hpnicfOnuCountTable,'hpnicfOnuCountEntry':hpnicfOnuCountEntry,'hpnicfOnuInCRCErrPkts':hpnicfOnuInCRCErrPkts,'hpnicfOnuOutDroppedFrames':hpnicfOnuOutDroppedFrames,'hpnicfEponOnuScalarGroup':hpnicfEponOnuScalarGroup,'hpnicfOnuPriorityQueueSizeMinVal':hpnicfOnuPriorityQueueSizeMinVal,'hpnicfOnuPriorityQueueSizeMaxVal':hpnicfOnuPriorityQueueSizeMaxVal,'hpnicfOnuPriorityQueueBandwidthMinVal':hpnicfOnuPriorityQueueBandwidthMinVal,'hpnicfOnuPriorityQueueBandwidthMaxVal':hpnicfOnuPriorityQueueBandwidthMaxVal,'hpnicfOnuPriorityQueueBurstsizeMinVal':hpnicfOnuPriorityQueueBurstsizeMinVal,'hpnicfOnuPriorityQueueBurstsizeMaxVal':hpnicfOnuPriorityQueueBurstsizeMaxVal,'hpnicfOnuUpdateByTypeNextIndex':hpnicfOnuUpdateByTypeNextIndex,'hpnicfOnuQueueBandwidthTable':hpnicfOnuQueueBandwidthTable,'hpnicfOnuQueueBandwidthEntry':hpnicfOnuQueueBandwidthEntry,'hpnicfOnuQueueMaxBandwidth':hpnicfOnuQueueMaxBandwidth,'hpnicfOnuQueueMaxBurstsize':hpnicfOnuQueueMaxBurstsize,'hpnicfOnuQueuePolicyStatus':hpnicfOnuQueuePolicyStatus,'hpnicfOnuIpAddressTable':hpnicfOnuIpAddressTable,'hpnicfOnuIpAddressEntry':hpnicfOnuIpAddressEntry,'hpnicfOnuIpAddress':hpnicfOnuIpAddress,'hpnicfOnuIpAddressMask':hpnicfOnuIpAddressMask,'hpnicfOnuIpAddressGateway':hpnicfOnuIpAddressGateway,'hpnicfOnuDhcpallocate':hpnicfOnuDhcpallocate,'hpnicfOnuManageVID':hpnicfOnuManageVID,'hpnicfOnuManageVlanIntfS':hpnicfOnuManageVlanIntfS,'hpnicfOnuChipSetInfoTable':hpnicfOnuChipSetInfoTable,'hpnicfOnuChipSetInfoEntry':hpnicfOnuChipSetInfoEntry,'hpnicfOnuChipSetVendorId':hpnicfOnuChipSetVendorId,'hpnicfOnuChipSetModel':hpnicfOnuChipSetModel,'hpnicfOnuChipSetRevision':hpnicfOnuChipSetRevision,'hpnicfOnuChipSetDesignDate':hpnicfOnuChipSetDesignDate,'hpnicfOnuCapabilityTable':hpnicfOnuCapabilityTable,'hpnicfOnuCapabilityEntry':hpnicfOnuCapabilityEntry,'hpnicfOnuServiceSupported':hpnicfOnuServiceSupported,'hpnicfOnuGEPortNumber':hpnicfOnuGEPortNumber,'hpnicfOnuFEPortNumber':hpnicfOnuFEPortNumber,'hpnicfOnuPOTSPortNumber':hpnicfOnuPOTSPortNumber,'hpnicfOnuE1PortsNumber':hpnicfOnuE1PortsNumber,'hpnicfOnuUpstreamQueueNumber':hpnicfOnuUpstreamQueueNumber,'hpnicfOnuMaxUpstreamQueuePerPort':hpnicfOnuMaxUpstreamQueuePerPort,'hpnicfOnuDownstreamQueueNumber':hpnicfOnuDownstreamQueueNumber,'hpnicfOnuMaxDownstreamQueuePerPort':hpnicfOnuMaxDownstreamQueuePerPort,'hpnicfOnuBatteryBackup':hpnicfOnuBatteryBackup,'hpnicfOnuIgspFastLeaveSupported':hpnicfOnuIgspFastLeaveSupported,'hpnicfOnuMCtrlFastLeaveSupported':hpnicfOnuMCtrlFastLeaveSupported,'hpnicfOnuDbaReportTable':hpnicfOnuDbaReportTable,'hpnicfOnuDbaReportEntry':hpnicfOnuDbaReportEntry,_w:hpnicfOnuDbaReportQueueId,'hpnicfOnuDbaReportThreshold':hpnicfOnuDbaReportThreshold,'hpnicfOnuDbaReportStatus':hpnicfOnuDbaReportStatus,'hpnicfOnuCosToLocalPrecedenceTable':hpnicfOnuCosToLocalPrecedenceTable,'hpnicfOnuCosToLocalPrecedenceEntry':hpnicfOnuCosToLocalPrecedenceEntry,_x:hpnicfOnuCosToLocalPrecedenceCosIndex,'hpnicfOnuCosToLocalPrecedenceValue':hpnicfOnuCosToLocalPrecedenceValue,'hpnicfEponOnuStpPortTable':hpnicfEponOnuStpPortTable,'hpnicfEponOnuStpPortEntry':hpnicfEponOnuStpPortEntry,_b:hpnicfEponStpPortIndex,_AG:hpnicfEponStpPortDescr,_AH:hpnicfEponStpPortState,'hpnicfOnuPhysicalTable':hpnicfOnuPhysicalTable,'hpnicfOnuPhysicalEntry':hpnicfOnuPhysicalEntry,'hpnicfOnuBridgeMac':hpnicfOnuBridgeMac,'hpnicfOnuFirstPonMac':hpnicfOnuFirstPonMac,'hpnicfOnuFirstPonRegState':hpnicfOnuFirstPonRegState,'hpnicfOnuSecondPonMac':hpnicfOnuSecondPonMac,'hpnicfOnuSecondPonRegState':hpnicfOnuSecondPonRegState,'hpnicfOnuSmlkTable':hpnicfOnuSmlkTable,'hpnicfOnuSmlkEntry':hpnicfOnuSmlkEntry,_c:hpnicfOnuSmlkGroupID,'hpnicfOnuSmlkFirstPonRole':hpnicfOnuSmlkFirstPonRole,_AJ:hpnicfOnuSmlkFirstPonStatus,'hpnicfOnuSmlkSecondPonRole':hpnicfOnuSmlkSecondPonRole,_AK:hpnicfOnuSmlkSecondPonStatus,'hpnicfOnuRS485PropertiesTable':hpnicfOnuRS485PropertiesTable,'hpnicfOnuRS485PropertiesEntry':hpnicfOnuRS485PropertiesEntry,_S:hpnicfOnuRS485SerialIndex,'hpnicfOnuRS485BaudRate':hpnicfOnuRS485BaudRate,'hpnicfOnuRS485DataBits':hpnicfOnuRS485DataBits,'hpnicfOnuRS485Parity':hpnicfOnuRS485Parity,'hpnicfOnuRS485StopBits':hpnicfOnuRS485StopBits,'hpnicfOnuRS485FlowControl':hpnicfOnuRS485FlowControl,'hpnicfOnuRS485TXOctets':hpnicfOnuRS485TXOctets,'hpnicfOnuRS485RXOctets':hpnicfOnuRS485RXOctets,'hpnicfOnuRS485TXErrOctets':hpnicfOnuRS485TXErrOctets,'hpnicfOnuRS485RXErrOctets':hpnicfOnuRS485RXErrOctets,'hpnicfOnuRS485ResetStatistics':hpnicfOnuRS485ResetStatistics,'hpnicfOnuRS485SessionSummaryTable':hpnicfOnuRS485SessionSummaryTable,'hpnicfOnuRS485SessionSummaryEntry':hpnicfOnuRS485SessionSummaryEntry,'hpnicfOnuRS485SessionMaxNum':hpnicfOnuRS485SessionMaxNum,'hpnicfOnuRS485SessionNextIndex':hpnicfOnuRS485SessionNextIndex,'hpnicfOnuRS485SessionTable':hpnicfOnuRS485SessionTable,'hpnicfOnuRS485SessionEntry':hpnicfOnuRS485SessionEntry,_d:hpnicfOnuRS485SessionIndex,'hpnicfOnuRS485SessionType':hpnicfOnuRS485SessionType,'hpnicfOnuRS485SessionAddType':hpnicfOnuRS485SessionAddType,'hpnicfOnuRS485SessionRemoteIP':hpnicfOnuRS485SessionRemoteIP,'hpnicfOnuRS485SessionRemotePort':hpnicfOnuRS485SessionRemotePort,'hpnicfOnuRS485SessionLocalPort':hpnicfOnuRS485SessionLocalPort,'hpnicfOnuRS485SessionRowStatus':hpnicfOnuRS485SessionRowStatus,'hpnicfOnuRS485SessionErrInfoTable':hpnicfOnuRS485SessionErrInfoTable,'hpnicfOnuRS485SessionErrInfoEntry':hpnicfOnuRS485SessionErrInfoEntry,'hpnicfOnuRS485SessionErrInfo':hpnicfOnuRS485SessionErrInfo,'hpnicfEponBatchOperationMan':hpnicfEponBatchOperationMan,'hpnicfEponBatchOperationBySlotTable':hpnicfEponBatchOperationBySlotTable,'hpnicfEponBatchOperationBySlotEntry':hpnicfEponBatchOperationBySlotEntry,_A0:hpnicfEponBatchOperationBySlotIndex,'hpnicfEponBatchOperationBySlotType':hpnicfEponBatchOperationBySlotType,'hpnicfEponBatchOperationBySlot':hpnicfEponBatchOperationBySlot,'hpnicfEponBatchOperationBySlotResult':hpnicfEponBatchOperationBySlotResult,'hpnicfEponBatchOperationByOLTTable':hpnicfEponBatchOperationByOLTTable,'hpnicfEponBatchOperationByOLTEntry':hpnicfEponBatchOperationByOLTEntry,'hpnicfEponBatchOperationByOLTType':hpnicfEponBatchOperationByOLTType,'hpnicfEponBatchOperationByOLT':hpnicfEponBatchOperationByOLT,'hpnicfEponBatchOperationByOLTResult':hpnicfEponBatchOperationByOLTResult,'hpnicfOnuFirmwareUpdateByTypeTable':hpnicfOnuFirmwareUpdateByTypeTable,'hpnicfOnuFirmwareUpdateByTypeEntry':hpnicfOnuFirmwareUpdateByTypeEntry,_A3:hpnicfOnuUpdateByOnuTypeIndex,'hpnicfOnuUpdateByTypeOnuType':hpnicfOnuUpdateByTypeOnuType,'hpnicfOnuUpdateByTypeFileName':hpnicfOnuUpdateByTypeFileName,'hpnicfOnuUpdateByTypeRowStatus':hpnicfOnuUpdateByTypeRowStatus,'hpnicfEponErrorInfo':hpnicfEponErrorInfo,_i:hpnicfEponSoftwareErrorCode,_h:hpnicfOamVendorSpecificAlarmCode,_g:hpnicfEponOnuRegErrorMacAddr,_j:hpnicfOamEventLogType,_k:hpnicfOamEventLogLocation,_AA:hpnicfEponLoopbackPortIndex,_AB:hpnicfEponLoopbackPortDescr,_A8:hpnicfOltPortAlarmLlidMisFrames,_A4:hpnicfOltPortAlarmBer,_A6:hpnicfOltPortAlarmFer,_l:hpnicfEponOnuRegSilentMac,_AF:hpnicfEponOperationResult,_AI:hpnicfEponOnuLaserState,'hpnicfEponTrap':hpnicfEponTrap,'hpnicfEponTrapPrefix':hpnicfEponTrapPrefix,'hpnicfEponPortAlarmBerTrap':hpnicfEponPortAlarmBerTrap,'hpnicfEponPortAlarmFerTrap':hpnicfEponPortAlarmFerTrap,'hpnicfEponErrorLLIDFrameTrap':hpnicfEponErrorLLIDFrameTrap,'hpnicfEponLoopBackEnableTrap':hpnicfEponLoopBackEnableTrap,'hpnicfEponOnuRegistrationErrTrap':hpnicfEponOnuRegistrationErrTrap,'hpnicfEponOamDisconnectionTrap':hpnicfEponOamDisconnectionTrap,'hpnicfEponEncryptionKeyErrTrap':hpnicfEponEncryptionKeyErrTrap,'hpnicfEponRemoteStableTrap':hpnicfEponRemoteStableTrap,'hpnicfEponLocalStableTrap':hpnicfEponLocalStableTrap,'hpnicfEponOamVendorSpecificTrap':hpnicfEponOamVendorSpecificTrap,'hpnicfEponSoftwareErrTrap':hpnicfEponSoftwareErrTrap,'hpnicfEponPortAlarmBerRecoverTrap':hpnicfEponPortAlarmBerRecoverTrap,'hpnicfEponPortAlarmFerRecoverTrap':hpnicfEponPortAlarmFerRecoverTrap,'hpnicfEponErrorLLIDFrameRecoverTrap':hpnicfEponErrorLLIDFrameRecoverTrap,'hpnicfEponLoopBackEnableRecoverTrap':hpnicfEponLoopBackEnableRecoverTrap,'hpnicfEponOnuRegistrationErrRecoverTrap':hpnicfEponOnuRegistrationErrRecoverTrap,'hpnicfEponOamDisconnectionRecoverTrap':hpnicfEponOamDisconnectionRecoverTrap,'hpnicfEponEncryptionKeyErrRecoverTrap':hpnicfEponEncryptionKeyErrRecoverTrap,'hpnicfEponRemoteStableRecoverTrap':hpnicfEponRemoteStableRecoverTrap,'hpnicfEponLocalStableRecoverTrap':hpnicfEponLocalStableRecoverTrap,'hpnicfEponOamVendorSpecificRecoverTrap':hpnicfEponOamVendorSpecificRecoverTrap,'hpnicfEponSoftwareErrRecoverTrap':hpnicfEponSoftwareErrRecoverTrap,'hpnicfDot3OamThresholdRecoverEvent':hpnicfDot3OamThresholdRecoverEvent,'hpnicfDot3OamNonThresholdRecoverEvent':hpnicfDot3OamNonThresholdRecoverEvent,'hpnicfEponOnuRegExcessTrap':hpnicfEponOnuRegExcessTrap,'hpnicfEponOnuRegExcessRecoverTrap':hpnicfEponOnuRegExcessRecoverTrap,'hpnicfEponOnuPowerOffTrap':hpnicfEponOnuPowerOffTrap,'hpnicfEponOltSwitchoverTrap':hpnicfEponOltSwitchoverTrap,'hpnicfEponOltDFETrap':hpnicfEponOltDFETrap,'hpnicfEponOltDFERecoverTrap':hpnicfEponOltDFERecoverTrap,'hpnicfEponOnuSilenceTrap':hpnicfEponOnuSilenceTrap,'hpnicfEponOnuSilenceRecoverTrap':hpnicfEponOnuSilenceRecoverTrap,'hpnicfEponOnuUpdateResultTrap':hpnicfEponOnuUpdateResultTrap,'hpnicfEponOnuAutoBindTrap':hpnicfEponOnuAutoBindTrap,'hpnicfEponOnuPortStpStateTrap':hpnicfEponOnuPortStpStateTrap,'hpnicfEponOnuLaserFailedTrap':hpnicfEponOnuLaserFailedTrap,'hpnicfOnuSmlkSwitchoverTrap':hpnicfOnuSmlkSwitchoverTrap,'hpnicfEponStat':hpnicfEponStat,'hpnicfEponStatTable':hpnicfEponStatTable,'hpnicfEponStatEntry':hpnicfEponStatEntry,'hpnicfEponStatFER':hpnicfEponStatFER,'hpnicfEponStatBER':hpnicfEponStatBER})