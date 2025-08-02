_Ae='hpnicfEponDeviceGroupEventLog'
_Ad='hpnicfEponDeviceGroupEvent'
_Ac='hpnicfEponDeviceGroupStat'
_Ab='hpnicfEponDeviceGroupRMadLTable'
_Aa='hpnicfEponDeviceGroupControl'
_AZ='hpnicfEponDeviceEventsLogEntryStatus'
_AY='hpnicfEponDeviceEventsLogType'
_AX='hpnicfEponDeviceEventsLogCounts'
_AW='hpnicfEponDeviceEventsLogLastTime'
_AV='hpnicfEponDeviceEventsLogFirstTime'
_AU='hpnicfEponDeviceEventsLogID'
_AT='hpnicfEponDeviceEventControl'
_AS='hpnicfEponDeviceOrganizationSpecificEventEnabled'
_AR='hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled'
_AQ='hpnicfEponDeviceErroredFramePeriodEventEnabled'
_AP='hpnicfEponDeviceErroredFrameEventEnabled'
_AO='hpnicfEponDeviceErroredSymbolPeriodEventEnabled'
_AN='hpnicfEponDeviceGlobalEventEnabled'
_AM='hpnicfEponDevicePowerVoltageEventIndicationEnabled'
_AL='hpnicfEponDeviceTemperatureEventIndicationEnabled'
_AK='hpnicfEponDeviceLocalLinkFaultAlarmEnabled'
_AJ='hpnicfEponDeviceCriticalEventEnabled'
_AI='hpnicfEponDeviceDyingGaspAlarmEnabled'
_AH='hpnicfEponDeviceSampleMinimum'
_AG='hpnicfEponDeviceStatDroppedFramesQueue7'
_AF='hpnicfEponDeviceStatDroppedFramesQueue6'
_AE='hpnicfEponDeviceStatDroppedFramesQueue5'
_AD='hpnicfEponDeviceStatDroppedFramesQueue4'
_AC='hpnicfEponDeviceStatDroppedFramesQueue3'
_AB='hpnicfEponDeviceStatDroppedFramesQueue2'
_AA='hpnicfEponDeviceStatDroppedFramesQueue1'
_A9='hpnicfEponDeviceStatDroppedFramesQueue0'
_A8='hpnicfEponDeviceStatRxFramesQueue7'
_A7='hpnicfEponDeviceStatRxFramesQueue6'
_A6='hpnicfEponDeviceStatRxFramesQueue5'
_A5='hpnicfEponDeviceStatRxFramesQueue4'
_A4='hpnicfEponDeviceStatRxFramesQueue3'
_A3='hpnicfEponDeviceStatRxFramesQueue2'
_A2='hpnicfEponDeviceStatRxFramesQueue1'
_A1='hpnicfEponDeviceStatRxFramesQueue0'
_A0='hpnicfEponDeviceStatTxFramesQueue7'
_z='hpnicfEponDeviceStatTxFramesQueue6'
_y='hpnicfEponDeviceStatTxFramesQueue5'
_x='hpnicfEponDeviceStatTxFramesQueue4'
_w='hpnicfEponDeviceStatTxFramesQueue3'
_v='hpnicfEponDeviceStatTxFramesQueue2'
_u='hpnicfEponDeviceStatTxFramesQueue1'
_t='hpnicfEponDeviceStatTxFramesQueue0'
_s='hpnicfEponDeviceRMadlEntryStatus'
_r='hpnicfEponDeviceRMadlAction'
_q='hpnicfEponDeviceRMadlType'
_p='hpnicfEponDeviceRMadlRemoteAddress'
_o='hpnicfEponDeviceRMadlLogID'
_n='hpnicfEponDeviceRMadlLLID'
_m='hpnicfEponDeviceRemoteMACAddressLLIDControl'
_l='hpnicfEponDeviceObjectReportThreshold'
_k='hpnicfEponDeviceObjectNumberOfLLIDs'
_j='hpnicfEponDeviceObjectPowerDown'
_i='hpnicfEponDeviceObjectDeviceReadyMode'
_h='hpnicfEponDeviceObjectOamMode'
_g='hpnicfEponDeviceObjectFecEnabled'
_f='hpnicfEponDeviceObjectModes'
_e='hpnicfEponDeviceObjectReset'
_d='not-accessible'
_c='hpnicfEponDeviceEventsLogIndex'
_b='hpnicfEponDeviceEventsLogName'
_a='useDefaultReporting'
_Z='resetLog'
_Y='hpnicfEponDeviceOrganizationSpecificEventState'
_X='hpnicfEponDeviceErroredFrameSecondsSummaryEventState'
_W='hpnicfEponDeviceErroredFramePeriodEventState'
_V='hpnicfEponDeviceErroredFrameEventState'
_U='hpnicfEponDeviceErroredSymbolPeriodEventState'
_T='hpnicfEponDeviceGlobalEventState'
_S='hpnicfEponDevicePowerVoltageEventIndicationState'
_R='hpnicfEponDeviceTemperatureEventIndicationState'
_Q='hpnicfEponDeviceLocalLinkFaultAlarmState'
_P='hpnicfEponDeviceCriticalEventState'
_O='hpnicfEponDeviceDyingGaspAlarmState'
_N='none'
_M='Unsigned32'
_L='SnmpAdminString'
_K='ObjectIdentifier'
_J='ifIndex'
_I='IF-MIB'
_H='read-create'
_G='TruthValue'
_F='Integer32'
_E='read-write'
_D='frames'
_C='read-only'
_B='HPN-ICF-EPON-DEVICE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString',_K)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfEpon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfEpon')
ifIndex,=mibBuilder.importSymbols(_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso','mib-2','zeroDotZero')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
hpnicfEponDeviceMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4))
if mibBuilder.loadTexts:hpnicfEponDeviceMIB.setRevisions(('2004-09-21 00:00',))
_HpnicfEponDeviceObjectMIB_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceObjectMIB=_HpnicfEponDeviceObjectMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1))
_HpnicfEponDeviceObjects_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceObjects=_HpnicfEponDeviceObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1))
_HpnicfEponDeviceControlObjects_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceControlObjects=_HpnicfEponDeviceControlObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1))
_HpnicfEponDeviceControlTable_Object=MibTable
hpnicfEponDeviceControlTable=_HpnicfEponDeviceControlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1))
if mibBuilder.loadTexts:hpnicfEponDeviceControlTable.setStatus(_A)
_HpnicfEponDeviceControlEntry_Object=MibTableRow
hpnicfEponDeviceControlEntry=_HpnicfEponDeviceControlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1))
hpnicfEponDeviceControlEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfEponDeviceControlEntry.setStatus(_A)
class _HpnicfEponDeviceObjectReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('reset',2)))
_HpnicfEponDeviceObjectReset_Type.__name__=_F
_HpnicfEponDeviceObjectReset_Object=MibTableColumn
hpnicfEponDeviceObjectReset=_HpnicfEponDeviceObjectReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,1),_HpnicfEponDeviceObjectReset_Type())
hpnicfEponDeviceObjectReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectReset.setStatus(_A)
class _HpnicfEponDeviceObjectModes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('olt',1),('onu',2)))
_HpnicfEponDeviceObjectModes_Type.__name__=_F
_HpnicfEponDeviceObjectModes_Object=MibTableColumn
hpnicfEponDeviceObjectModes=_HpnicfEponDeviceObjectModes_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,2),_HpnicfEponDeviceObjectModes_Type())
hpnicfEponDeviceObjectModes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectModes.setStatus(_A)
class _HpnicfEponDeviceObjectFecEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noFecEnabled',1),('fecTxEnabled',2),('fecRxEnabled',3),('fecTxRxEnabled',4)))
_HpnicfEponDeviceObjectFecEnabled_Type.__name__=_F
_HpnicfEponDeviceObjectFecEnabled_Object=MibTableColumn
hpnicfEponDeviceObjectFecEnabled=_HpnicfEponDeviceObjectFecEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,4),_HpnicfEponDeviceObjectFecEnabled_Type())
hpnicfEponDeviceObjectFecEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectFecEnabled.setStatus(_A)
class _HpnicfEponDeviceObjectOamMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOam',1),('oamServer',2),('oamclient',3)))
_HpnicfEponDeviceObjectOamMode_Type.__name__=_F
_HpnicfEponDeviceObjectOamMode_Object=MibTableColumn
hpnicfEponDeviceObjectOamMode=_HpnicfEponDeviceObjectOamMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,5),_HpnicfEponDeviceObjectOamMode_Type())
hpnicfEponDeviceObjectOamMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectOamMode.setStatus(_A)
class _HpnicfEponDeviceObjectDeviceReadyMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notReady',1),('inProcess',2),('ready',3)))
_HpnicfEponDeviceObjectDeviceReadyMode_Type.__name__=_F
_HpnicfEponDeviceObjectDeviceReadyMode_Object=MibTableColumn
hpnicfEponDeviceObjectDeviceReadyMode=_HpnicfEponDeviceObjectDeviceReadyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,6),_HpnicfEponDeviceObjectDeviceReadyMode_Type())
hpnicfEponDeviceObjectDeviceReadyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectDeviceReadyMode.setStatus(_A)
class _HpnicfEponDeviceObjectPowerDown_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceObjectPowerDown_Type.__name__=_G
_HpnicfEponDeviceObjectPowerDown_Object=MibTableColumn
hpnicfEponDeviceObjectPowerDown=_HpnicfEponDeviceObjectPowerDown_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,7),_HpnicfEponDeviceObjectPowerDown_Type())
hpnicfEponDeviceObjectPowerDown.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectPowerDown.setStatus(_A)
_HpnicfEponDeviceObjectNumberOfLLIDs_Type=Integer32
_HpnicfEponDeviceObjectNumberOfLLIDs_Object=MibTableColumn
hpnicfEponDeviceObjectNumberOfLLIDs=_HpnicfEponDeviceObjectNumberOfLLIDs_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,8),_HpnicfEponDeviceObjectNumberOfLLIDs_Type())
hpnicfEponDeviceObjectNumberOfLLIDs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectNumberOfLLIDs.setStatus(_A)
class _HpnicfEponDeviceObjectReportThreshold_Type(Integer32):defaultValue=0
_HpnicfEponDeviceObjectReportThreshold_Type.__name__=_F
_HpnicfEponDeviceObjectReportThreshold_Object=MibTableColumn
hpnicfEponDeviceObjectReportThreshold=_HpnicfEponDeviceObjectReportThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,9),_HpnicfEponDeviceObjectReportThreshold_Type())
hpnicfEponDeviceObjectReportThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectReportThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceObjectReportThreshold.setUnits('TQ (16nsec)')
class _HpnicfEponDeviceRemoteMACAddressLLIDControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_Z,2),(_a,3)))
_HpnicfEponDeviceRemoteMACAddressLLIDControl_Type.__name__=_F
_HpnicfEponDeviceRemoteMACAddressLLIDControl_Object=MibTableColumn
hpnicfEponDeviceRemoteMACAddressLLIDControl=_HpnicfEponDeviceRemoteMACAddressLLIDControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,1,1,10),_HpnicfEponDeviceRemoteMACAddressLLIDControl_Type())
hpnicfEponDeviceRemoteMACAddressLLIDControl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceRemoteMACAddressLLIDControl.setStatus(_A)
_HpnicfEponDeviceRemoteMACAddressLLIDTable_Object=MibTable
hpnicfEponDeviceRemoteMACAddressLLIDTable=_HpnicfEponDeviceRemoteMACAddressLLIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2))
if mibBuilder.loadTexts:hpnicfEponDeviceRemoteMACAddressLLIDTable.setStatus(_A)
_HpnicfEponDeviceRemoteMACAddressLLIDEntry_Object=MibTableRow
hpnicfEponDeviceRemoteMACAddressLLIDEntry=_HpnicfEponDeviceRemoteMACAddressLLIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1))
hpnicfEponDeviceRemoteMACAddressLLIDEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfEponDeviceRemoteMACAddressLLIDEntry.setStatus(_A)
class _HpnicfEponDeviceRemoteMACAddressLLIDName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfEponDeviceRemoteMACAddressLLIDName_Type.__name__=_L
_HpnicfEponDeviceRemoteMACAddressLLIDName_Object=MibTableColumn
hpnicfEponDeviceRemoteMACAddressLLIDName=_HpnicfEponDeviceRemoteMACAddressLLIDName_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1,1),_HpnicfEponDeviceRemoteMACAddressLLIDName_Type())
hpnicfEponDeviceRemoteMACAddressLLIDName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceRemoteMACAddressLLIDName.setStatus(_A)
class _HpnicfEponDeviceRMadlLLID_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfEponDeviceRMadlLLID_Type.__name__=_M
_HpnicfEponDeviceRMadlLLID_Object=MibTableColumn
hpnicfEponDeviceRMadlLLID=_HpnicfEponDeviceRMadlLLID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1,2),_HpnicfEponDeviceRMadlLLID_Type())
hpnicfEponDeviceRMadlLLID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceRMadlLLID.setStatus(_A)
class _HpnicfEponDeviceRMadlLogID_Type(ObjectIdentifier):defaultValue=0,0
_HpnicfEponDeviceRMadlLogID_Type.__name__=_K
_HpnicfEponDeviceRMadlLogID_Object=MibTableColumn
hpnicfEponDeviceRMadlLogID=_HpnicfEponDeviceRMadlLogID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1,3),_HpnicfEponDeviceRMadlLogID_Type())
hpnicfEponDeviceRMadlLogID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceRMadlLogID.setStatus(_A)
_HpnicfEponDeviceRMadlRemoteAddress_Type=MacAddress
_HpnicfEponDeviceRMadlRemoteAddress_Object=MibTableColumn
hpnicfEponDeviceRMadlRemoteAddress=_HpnicfEponDeviceRMadlRemoteAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1,4),_HpnicfEponDeviceRMadlRemoteAddress_Type())
hpnicfEponDeviceRMadlRemoteAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceRMadlRemoteAddress.setStatus(_A)
class _HpnicfEponDeviceRMadlType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notRegister',1),('registered',2)))
_HpnicfEponDeviceRMadlType_Type.__name__=_F
_HpnicfEponDeviceRMadlType_Object=MibTableColumn
hpnicfEponDeviceRMadlType=_HpnicfEponDeviceRMadlType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1,5),_HpnicfEponDeviceRMadlType_Type())
hpnicfEponDeviceRMadlType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceRMadlType.setStatus(_A)
class _HpnicfEponDeviceRMadlAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('register',2),('deregister',3),('reregister',4)))
_HpnicfEponDeviceRMadlAction_Type.__name__=_F
_HpnicfEponDeviceRMadlAction_Object=MibTableColumn
hpnicfEponDeviceRMadlAction=_HpnicfEponDeviceRMadlAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1,6),_HpnicfEponDeviceRMadlAction_Type())
hpnicfEponDeviceRMadlAction.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceRMadlAction.setStatus(_A)
_HpnicfEponDeviceRMadlEntryStatus_Type=RowStatus
_HpnicfEponDeviceRMadlEntryStatus_Object=MibTableColumn
hpnicfEponDeviceRMadlEntryStatus=_HpnicfEponDeviceRMadlEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,1,2,1,7),_HpnicfEponDeviceRMadlEntryStatus_Type())
hpnicfEponDeviceRMadlEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceRMadlEntryStatus.setStatus(_A)
_HpnicfEponDeviceStatObjects_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceStatObjects=_HpnicfEponDeviceStatObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2))
_HpnicfEponDeviceStatTable_Object=MibTable
hpnicfEponDeviceStatTable=_HpnicfEponDeviceStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1))
if mibBuilder.loadTexts:hpnicfEponDeviceStatTable.setStatus(_A)
_HpnicfEponDeviceStatEntry_Object=MibTableRow
hpnicfEponDeviceStatEntry=_HpnicfEponDeviceStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1))
hpnicfEponDeviceStatEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfEponDeviceStatEntry.setStatus(_A)
_HpnicfEponDeviceStatTxFramesQueue0_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue0_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue0=_HpnicfEponDeviceStatTxFramesQueue0_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,1),_HpnicfEponDeviceStatTxFramesQueue0_Type())
hpnicfEponDeviceStatTxFramesQueue0.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue0.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue0.setUnits(_D)
_HpnicfEponDeviceStatTxFramesQueue1_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue1_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue1=_HpnicfEponDeviceStatTxFramesQueue1_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,2),_HpnicfEponDeviceStatTxFramesQueue1_Type())
hpnicfEponDeviceStatTxFramesQueue1.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue1.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue1.setUnits(_D)
_HpnicfEponDeviceStatTxFramesQueue2_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue2_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue2=_HpnicfEponDeviceStatTxFramesQueue2_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,3),_HpnicfEponDeviceStatTxFramesQueue2_Type())
hpnicfEponDeviceStatTxFramesQueue2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue2.setUnits(_D)
_HpnicfEponDeviceStatTxFramesQueue3_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue3_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue3=_HpnicfEponDeviceStatTxFramesQueue3_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,4),_HpnicfEponDeviceStatTxFramesQueue3_Type())
hpnicfEponDeviceStatTxFramesQueue3.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue3.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue3.setUnits(_D)
_HpnicfEponDeviceStatTxFramesQueue4_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue4_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue4=_HpnicfEponDeviceStatTxFramesQueue4_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,5),_HpnicfEponDeviceStatTxFramesQueue4_Type())
hpnicfEponDeviceStatTxFramesQueue4.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue4.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue4.setUnits(_D)
_HpnicfEponDeviceStatTxFramesQueue5_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue5_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue5=_HpnicfEponDeviceStatTxFramesQueue5_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,6),_HpnicfEponDeviceStatTxFramesQueue5_Type())
hpnicfEponDeviceStatTxFramesQueue5.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue5.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue5.setUnits(_D)
_HpnicfEponDeviceStatTxFramesQueue6_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue6_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue6=_HpnicfEponDeviceStatTxFramesQueue6_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,7),_HpnicfEponDeviceStatTxFramesQueue6_Type())
hpnicfEponDeviceStatTxFramesQueue6.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue6.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue6.setUnits(_D)
_HpnicfEponDeviceStatTxFramesQueue7_Type=Counter32
_HpnicfEponDeviceStatTxFramesQueue7_Object=MibTableColumn
hpnicfEponDeviceStatTxFramesQueue7=_HpnicfEponDeviceStatTxFramesQueue7_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,8),_HpnicfEponDeviceStatTxFramesQueue7_Type())
hpnicfEponDeviceStatTxFramesQueue7.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue7.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatTxFramesQueue7.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue0_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue0_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue0=_HpnicfEponDeviceStatRxFramesQueue0_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,9),_HpnicfEponDeviceStatRxFramesQueue0_Type())
hpnicfEponDeviceStatRxFramesQueue0.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue0.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue0.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue1_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue1_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue1=_HpnicfEponDeviceStatRxFramesQueue1_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,10),_HpnicfEponDeviceStatRxFramesQueue1_Type())
hpnicfEponDeviceStatRxFramesQueue1.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue1.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue1.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue2_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue2_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue2=_HpnicfEponDeviceStatRxFramesQueue2_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,11),_HpnicfEponDeviceStatRxFramesQueue2_Type())
hpnicfEponDeviceStatRxFramesQueue2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue2.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue3_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue3_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue3=_HpnicfEponDeviceStatRxFramesQueue3_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,12),_HpnicfEponDeviceStatRxFramesQueue3_Type())
hpnicfEponDeviceStatRxFramesQueue3.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue3.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue3.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue4_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue4_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue4=_HpnicfEponDeviceStatRxFramesQueue4_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,13),_HpnicfEponDeviceStatRxFramesQueue4_Type())
hpnicfEponDeviceStatRxFramesQueue4.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue4.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue4.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue5_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue5_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue5=_HpnicfEponDeviceStatRxFramesQueue5_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,14),_HpnicfEponDeviceStatRxFramesQueue5_Type())
hpnicfEponDeviceStatRxFramesQueue5.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue5.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue5.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue6_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue6_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue6=_HpnicfEponDeviceStatRxFramesQueue6_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,15),_HpnicfEponDeviceStatRxFramesQueue6_Type())
hpnicfEponDeviceStatRxFramesQueue6.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue6.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue6.setUnits(_D)
_HpnicfEponDeviceStatRxFramesQueue7_Type=Counter32
_HpnicfEponDeviceStatRxFramesQueue7_Object=MibTableColumn
hpnicfEponDeviceStatRxFramesQueue7=_HpnicfEponDeviceStatRxFramesQueue7_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,16),_HpnicfEponDeviceStatRxFramesQueue7_Type())
hpnicfEponDeviceStatRxFramesQueue7.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue7.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatRxFramesQueue7.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue0_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue0_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue0=_HpnicfEponDeviceStatDroppedFramesQueue0_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,17),_HpnicfEponDeviceStatDroppedFramesQueue0_Type())
hpnicfEponDeviceStatDroppedFramesQueue0.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue0.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue0.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue1_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue1_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue1=_HpnicfEponDeviceStatDroppedFramesQueue1_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,18),_HpnicfEponDeviceStatDroppedFramesQueue1_Type())
hpnicfEponDeviceStatDroppedFramesQueue1.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue1.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue1.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue2_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue2_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue2=_HpnicfEponDeviceStatDroppedFramesQueue2_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,19),_HpnicfEponDeviceStatDroppedFramesQueue2_Type())
hpnicfEponDeviceStatDroppedFramesQueue2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue2.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue3_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue3_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue3=_HpnicfEponDeviceStatDroppedFramesQueue3_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,20),_HpnicfEponDeviceStatDroppedFramesQueue3_Type())
hpnicfEponDeviceStatDroppedFramesQueue3.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue3.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue3.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue4_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue4_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue4=_HpnicfEponDeviceStatDroppedFramesQueue4_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,21),_HpnicfEponDeviceStatDroppedFramesQueue4_Type())
hpnicfEponDeviceStatDroppedFramesQueue4.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue4.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue4.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue5_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue5_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue5=_HpnicfEponDeviceStatDroppedFramesQueue5_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,22),_HpnicfEponDeviceStatDroppedFramesQueue5_Type())
hpnicfEponDeviceStatDroppedFramesQueue5.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue5.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue5.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue6_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue6_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue6=_HpnicfEponDeviceStatDroppedFramesQueue6_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,23),_HpnicfEponDeviceStatDroppedFramesQueue6_Type())
hpnicfEponDeviceStatDroppedFramesQueue6.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue6.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue6.setUnits(_D)
_HpnicfEponDeviceStatDroppedFramesQueue7_Type=Counter32
_HpnicfEponDeviceStatDroppedFramesQueue7_Object=MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue7=_HpnicfEponDeviceStatDroppedFramesQueue7_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,2,1,1,24),_HpnicfEponDeviceStatDroppedFramesQueue7_Type())
hpnicfEponDeviceStatDroppedFramesQueue7.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue7.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceStatDroppedFramesQueue7.setUnits(_D)
_HpnicfEponDeviceEventObjects_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceEventObjects=_HpnicfEponDeviceEventObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3))
_HpnicfEponDeviceEventObjectTable_Object=MibTable
hpnicfEponDeviceEventObjectTable=_HpnicfEponDeviceEventObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1))
if mibBuilder.loadTexts:hpnicfEponDeviceEventObjectTable.setStatus(_A)
_HpnicfEponDeviceEventObjectEntry_Object=MibTableRow
hpnicfEponDeviceEventObjectEntry=_HpnicfEponDeviceEventObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1))
hpnicfEponDeviceEventObjectEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfEponDeviceEventObjectEntry.setStatus(_A)
class _HpnicfEponDeviceSampleMinimum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfEponDeviceSampleMinimum_Type.__name__=_F
_HpnicfEponDeviceSampleMinimum_Object=MibTableColumn
hpnicfEponDeviceSampleMinimum=_HpnicfEponDeviceSampleMinimum_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,1),_HpnicfEponDeviceSampleMinimum_Type())
hpnicfEponDeviceSampleMinimum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceSampleMinimum.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEponDeviceSampleMinimum.setUnits('seconds')
_HpnicfEponDeviceDyingGaspAlarmState_Type=TruthValue
_HpnicfEponDeviceDyingGaspAlarmState_Object=MibTableColumn
hpnicfEponDeviceDyingGaspAlarmState=_HpnicfEponDeviceDyingGaspAlarmState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,2),_HpnicfEponDeviceDyingGaspAlarmState_Type())
hpnicfEponDeviceDyingGaspAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceDyingGaspAlarmState.setStatus(_A)
class _HpnicfEponDeviceDyingGaspAlarmEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceDyingGaspAlarmEnabled_Type.__name__=_G
_HpnicfEponDeviceDyingGaspAlarmEnabled_Object=MibTableColumn
hpnicfEponDeviceDyingGaspAlarmEnabled=_HpnicfEponDeviceDyingGaspAlarmEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,3),_HpnicfEponDeviceDyingGaspAlarmEnabled_Type())
hpnicfEponDeviceDyingGaspAlarmEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceDyingGaspAlarmEnabled.setStatus(_A)
_HpnicfEponDeviceCriticalEventState_Type=TruthValue
_HpnicfEponDeviceCriticalEventState_Object=MibTableColumn
hpnicfEponDeviceCriticalEventState=_HpnicfEponDeviceCriticalEventState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,4),_HpnicfEponDeviceCriticalEventState_Type())
hpnicfEponDeviceCriticalEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceCriticalEventState.setStatus(_A)
class _HpnicfEponDeviceCriticalEventEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceCriticalEventEnabled_Type.__name__=_G
_HpnicfEponDeviceCriticalEventEnabled_Object=MibTableColumn
hpnicfEponDeviceCriticalEventEnabled=_HpnicfEponDeviceCriticalEventEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,5),_HpnicfEponDeviceCriticalEventEnabled_Type())
hpnicfEponDeviceCriticalEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceCriticalEventEnabled.setStatus(_A)
_HpnicfEponDeviceLocalLinkFaultAlarmState_Type=TruthValue
_HpnicfEponDeviceLocalLinkFaultAlarmState_Object=MibTableColumn
hpnicfEponDeviceLocalLinkFaultAlarmState=_HpnicfEponDeviceLocalLinkFaultAlarmState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,6),_HpnicfEponDeviceLocalLinkFaultAlarmState_Type())
hpnicfEponDeviceLocalLinkFaultAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceLocalLinkFaultAlarmState.setStatus(_A)
class _HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Type.__name__=_G
_HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Object=MibTableColumn
hpnicfEponDeviceLocalLinkFaultAlarmEnabled=_HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,7),_HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Type())
hpnicfEponDeviceLocalLinkFaultAlarmEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceLocalLinkFaultAlarmEnabled.setStatus(_A)
_HpnicfEponDeviceTemperatureEventIndicationState_Type=TruthValue
_HpnicfEponDeviceTemperatureEventIndicationState_Object=MibTableColumn
hpnicfEponDeviceTemperatureEventIndicationState=_HpnicfEponDeviceTemperatureEventIndicationState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,8),_HpnicfEponDeviceTemperatureEventIndicationState_Type())
hpnicfEponDeviceTemperatureEventIndicationState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceTemperatureEventIndicationState.setStatus(_A)
class _HpnicfEponDeviceTemperatureEventIndicationEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceTemperatureEventIndicationEnabled_Type.__name__=_G
_HpnicfEponDeviceTemperatureEventIndicationEnabled_Object=MibTableColumn
hpnicfEponDeviceTemperatureEventIndicationEnabled=_HpnicfEponDeviceTemperatureEventIndicationEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,9),_HpnicfEponDeviceTemperatureEventIndicationEnabled_Type())
hpnicfEponDeviceTemperatureEventIndicationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceTemperatureEventIndicationEnabled.setStatus(_A)
_HpnicfEponDevicePowerVoltageEventIndicationState_Type=TruthValue
_HpnicfEponDevicePowerVoltageEventIndicationState_Object=MibTableColumn
hpnicfEponDevicePowerVoltageEventIndicationState=_HpnicfEponDevicePowerVoltageEventIndicationState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,10),_HpnicfEponDevicePowerVoltageEventIndicationState_Type())
hpnicfEponDevicePowerVoltageEventIndicationState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDevicePowerVoltageEventIndicationState.setStatus(_A)
class _HpnicfEponDevicePowerVoltageEventIndicationEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDevicePowerVoltageEventIndicationEnabled_Type.__name__=_G
_HpnicfEponDevicePowerVoltageEventIndicationEnabled_Object=MibTableColumn
hpnicfEponDevicePowerVoltageEventIndicationEnabled=_HpnicfEponDevicePowerVoltageEventIndicationEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,11),_HpnicfEponDevicePowerVoltageEventIndicationEnabled_Type())
hpnicfEponDevicePowerVoltageEventIndicationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDevicePowerVoltageEventIndicationEnabled.setStatus(_A)
_HpnicfEponDeviceGlobalEventState_Type=TruthValue
_HpnicfEponDeviceGlobalEventState_Object=MibTableColumn
hpnicfEponDeviceGlobalEventState=_HpnicfEponDeviceGlobalEventState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,12),_HpnicfEponDeviceGlobalEventState_Type())
hpnicfEponDeviceGlobalEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceGlobalEventState.setStatus(_A)
class _HpnicfEponDeviceGlobalEventEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceGlobalEventEnabled_Type.__name__=_G
_HpnicfEponDeviceGlobalEventEnabled_Object=MibTableColumn
hpnicfEponDeviceGlobalEventEnabled=_HpnicfEponDeviceGlobalEventEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,13),_HpnicfEponDeviceGlobalEventEnabled_Type())
hpnicfEponDeviceGlobalEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceGlobalEventEnabled.setStatus(_A)
_HpnicfEponDeviceErroredSymbolPeriodEventState_Type=TruthValue
_HpnicfEponDeviceErroredSymbolPeriodEventState_Object=MibTableColumn
hpnicfEponDeviceErroredSymbolPeriodEventState=_HpnicfEponDeviceErroredSymbolPeriodEventState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,14),_HpnicfEponDeviceErroredSymbolPeriodEventState_Type())
hpnicfEponDeviceErroredSymbolPeriodEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredSymbolPeriodEventState.setStatus(_A)
class _HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Type.__name__=_G
_HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Object=MibTableColumn
hpnicfEponDeviceErroredSymbolPeriodEventEnabled=_HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,15),_HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Type())
hpnicfEponDeviceErroredSymbolPeriodEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredSymbolPeriodEventEnabled.setStatus(_A)
_HpnicfEponDeviceErroredFrameEventState_Type=TruthValue
_HpnicfEponDeviceErroredFrameEventState_Object=MibTableColumn
hpnicfEponDeviceErroredFrameEventState=_HpnicfEponDeviceErroredFrameEventState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,16),_HpnicfEponDeviceErroredFrameEventState_Type())
hpnicfEponDeviceErroredFrameEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredFrameEventState.setStatus(_A)
class _HpnicfEponDeviceErroredFrameEventEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceErroredFrameEventEnabled_Type.__name__=_G
_HpnicfEponDeviceErroredFrameEventEnabled_Object=MibTableColumn
hpnicfEponDeviceErroredFrameEventEnabled=_HpnicfEponDeviceErroredFrameEventEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,17),_HpnicfEponDeviceErroredFrameEventEnabled_Type())
hpnicfEponDeviceErroredFrameEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredFrameEventEnabled.setStatus(_A)
_HpnicfEponDeviceErroredFramePeriodEventState_Type=TruthValue
_HpnicfEponDeviceErroredFramePeriodEventState_Object=MibTableColumn
hpnicfEponDeviceErroredFramePeriodEventState=_HpnicfEponDeviceErroredFramePeriodEventState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,18),_HpnicfEponDeviceErroredFramePeriodEventState_Type())
hpnicfEponDeviceErroredFramePeriodEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredFramePeriodEventState.setStatus(_A)
class _HpnicfEponDeviceErroredFramePeriodEventEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceErroredFramePeriodEventEnabled_Type.__name__=_G
_HpnicfEponDeviceErroredFramePeriodEventEnabled_Object=MibTableColumn
hpnicfEponDeviceErroredFramePeriodEventEnabled=_HpnicfEponDeviceErroredFramePeriodEventEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,19),_HpnicfEponDeviceErroredFramePeriodEventEnabled_Type())
hpnicfEponDeviceErroredFramePeriodEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredFramePeriodEventEnabled.setStatus(_A)
_HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Type=TruthValue
_HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Object=MibTableColumn
hpnicfEponDeviceErroredFrameSecondsSummaryEventState=_HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,20),_HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Type())
hpnicfEponDeviceErroredFrameSecondsSummaryEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredFrameSecondsSummaryEventState.setStatus(_A)
class _HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Type.__name__=_G
_HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Object=MibTableColumn
hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled=_HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,21),_HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Type())
hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled.setStatus(_A)
_HpnicfEponDeviceOrganizationSpecificEventState_Type=TruthValue
_HpnicfEponDeviceOrganizationSpecificEventState_Object=MibTableColumn
hpnicfEponDeviceOrganizationSpecificEventState=_HpnicfEponDeviceOrganizationSpecificEventState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,22),_HpnicfEponDeviceOrganizationSpecificEventState_Type())
hpnicfEponDeviceOrganizationSpecificEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceOrganizationSpecificEventState.setStatus(_A)
class _HpnicfEponDeviceOrganizationSpecificEventEnabled_Type(TruthValue):defaultValue=2
_HpnicfEponDeviceOrganizationSpecificEventEnabled_Type.__name__=_G
_HpnicfEponDeviceOrganizationSpecificEventEnabled_Object=MibTableColumn
hpnicfEponDeviceOrganizationSpecificEventEnabled=_HpnicfEponDeviceOrganizationSpecificEventEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,23),_HpnicfEponDeviceOrganizationSpecificEventEnabled_Type())
hpnicfEponDeviceOrganizationSpecificEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceOrganizationSpecificEventEnabled.setStatus(_A)
class _HpnicfEponDeviceEventControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_Z,2),(_a,3)))
_HpnicfEponDeviceEventControl_Type.__name__=_F
_HpnicfEponDeviceEventControl_Object=MibTableColumn
hpnicfEponDeviceEventControl=_HpnicfEponDeviceEventControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,1,1,24),_HpnicfEponDeviceEventControl_Type())
hpnicfEponDeviceEventControl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfEponDeviceEventControl.setStatus(_A)
_HpnicfEponDeviceEventsLogTable_Object=MibTable
hpnicfEponDeviceEventsLogTable=_HpnicfEponDeviceEventsLogTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2))
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogTable.setStatus(_A)
_HpnicfEponDeviceEventsLogEntry_Object=MibTableRow
hpnicfEponDeviceEventsLogEntry=_HpnicfEponDeviceEventsLogEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1))
hpnicfEponDeviceEventsLogEntry.setIndexNames((0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogEntry.setStatus(_A)
class _HpnicfEponDeviceEventsLogName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfEponDeviceEventsLogName_Type.__name__=_L
_HpnicfEponDeviceEventsLogName_Object=MibTableColumn
hpnicfEponDeviceEventsLogName=_HpnicfEponDeviceEventsLogName_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,1),_HpnicfEponDeviceEventsLogName_Type())
hpnicfEponDeviceEventsLogName.setMaxAccess(_d)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogName.setStatus(_A)
class _HpnicfEponDeviceEventsLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfEponDeviceEventsLogIndex_Type.__name__=_M
_HpnicfEponDeviceEventsLogIndex_Object=MibTableColumn
hpnicfEponDeviceEventsLogIndex=_HpnicfEponDeviceEventsLogIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,2),_HpnicfEponDeviceEventsLogIndex_Type())
hpnicfEponDeviceEventsLogIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogIndex.setStatus(_A)
class _HpnicfEponDeviceEventsLogID_Type(ObjectIdentifier):defaultValue=0,0
_HpnicfEponDeviceEventsLogID_Type.__name__=_K
_HpnicfEponDeviceEventsLogID_Object=MibTableColumn
hpnicfEponDeviceEventsLogID=_HpnicfEponDeviceEventsLogID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,3),_HpnicfEponDeviceEventsLogID_Type())
hpnicfEponDeviceEventsLogID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogID.setStatus(_A)
_HpnicfEponDeviceEventsLogFirstTime_Type=DateAndTime
_HpnicfEponDeviceEventsLogFirstTime_Object=MibTableColumn
hpnicfEponDeviceEventsLogFirstTime=_HpnicfEponDeviceEventsLogFirstTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,4),_HpnicfEponDeviceEventsLogFirstTime_Type())
hpnicfEponDeviceEventsLogFirstTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogFirstTime.setStatus(_A)
_HpnicfEponDeviceEventsLogLastTime_Type=DateAndTime
_HpnicfEponDeviceEventsLogLastTime_Object=MibTableColumn
hpnicfEponDeviceEventsLogLastTime=_HpnicfEponDeviceEventsLogLastTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,5),_HpnicfEponDeviceEventsLogLastTime_Type())
hpnicfEponDeviceEventsLogLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogLastTime.setStatus(_A)
_HpnicfEponDeviceEventsLogCounts_Type=Counter32
_HpnicfEponDeviceEventsLogCounts_Object=MibTableColumn
hpnicfEponDeviceEventsLogCounts=_HpnicfEponDeviceEventsLogCounts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,6),_HpnicfEponDeviceEventsLogCounts_Type())
hpnicfEponDeviceEventsLogCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogCounts.setStatus(_A)
class _HpnicfEponDeviceEventsLogType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11)))
_HpnicfEponDeviceEventsLogType_Type.__name__=_F
_HpnicfEponDeviceEventsLogType_Object=MibTableColumn
hpnicfEponDeviceEventsLogType=_HpnicfEponDeviceEventsLogType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,7),_HpnicfEponDeviceEventsLogType_Type())
hpnicfEponDeviceEventsLogType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogType.setStatus(_A)
_HpnicfEponDeviceEventsLogEntryStatus_Type=RowStatus
_HpnicfEponDeviceEventsLogEntryStatus_Object=MibTableColumn
hpnicfEponDeviceEventsLogEntryStatus=_HpnicfEponDeviceEventsLogEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,1,3,2,1,8),_HpnicfEponDeviceEventsLogEntryStatus_Type())
hpnicfEponDeviceEventsLogEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfEponDeviceEventsLogEntryStatus.setStatus(_A)
_HpnicfEponDeviceConformance_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceConformance=_HpnicfEponDeviceConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2))
_HpnicfEponDeviceGroups_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceGroups=_HpnicfEponDeviceGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,1))
_HpnicfEponDeviceCompliances_ObjectIdentity=ObjectIdentity
hpnicfEponDeviceCompliances=_HpnicfEponDeviceCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,2))
hpnicfEponDeviceGroupControl=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,1,1))
hpnicfEponDeviceGroupControl.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:hpnicfEponDeviceGroupControl.setStatus(_A)
hpnicfEponDeviceGroupRMadLTable=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,1,2))
hpnicfEponDeviceGroupRMadLTable.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:hpnicfEponDeviceGroupRMadLTable.setStatus(_A)
hpnicfEponDeviceGroupStat=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,1,3))
hpnicfEponDeviceGroupStat.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:hpnicfEponDeviceGroupStat.setStatus(_A)
hpnicfEponDeviceGroupEvent=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,1,4))
hpnicfEponDeviceGroupEvent.setObjects(*((_B,_AH),(_B,_O),(_B,_AI),(_B,_P),(_B,_AJ),(_B,_Q),(_B,_AK),(_B,_R),(_B,_AL),(_B,_S),(_B,_AM),(_B,_T),(_B,_AN),(_B,_U),(_B,_AO),(_B,_V),(_B,_AP),(_B,_W),(_B,_AQ),(_B,_X),(_B,_AR),(_B,_Y),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:hpnicfEponDeviceGroupEvent.setStatus(_A)
hpnicfEponDeviceGroupEventLog=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,1,5))
hpnicfEponDeviceGroupEventLog.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:hpnicfEponDeviceGroupEventLog.setStatus(_A)
hpnicfEponDeviceCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,42,4,1,2,2,1))
hpnicfEponDeviceCompliance.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:hpnicfEponDeviceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfEponDeviceMIB':hpnicfEponDeviceMIB,'hpnicfEponDeviceObjectMIB':hpnicfEponDeviceObjectMIB,'hpnicfEponDeviceObjects':hpnicfEponDeviceObjects,'hpnicfEponDeviceControlObjects':hpnicfEponDeviceControlObjects,'hpnicfEponDeviceControlTable':hpnicfEponDeviceControlTable,'hpnicfEponDeviceControlEntry':hpnicfEponDeviceControlEntry,_e:hpnicfEponDeviceObjectReset,_f:hpnicfEponDeviceObjectModes,_g:hpnicfEponDeviceObjectFecEnabled,_h:hpnicfEponDeviceObjectOamMode,_i:hpnicfEponDeviceObjectDeviceReadyMode,_j:hpnicfEponDeviceObjectPowerDown,_k:hpnicfEponDeviceObjectNumberOfLLIDs,_l:hpnicfEponDeviceObjectReportThreshold,_m:hpnicfEponDeviceRemoteMACAddressLLIDControl,'hpnicfEponDeviceRemoteMACAddressLLIDTable':hpnicfEponDeviceRemoteMACAddressLLIDTable,'hpnicfEponDeviceRemoteMACAddressLLIDEntry':hpnicfEponDeviceRemoteMACAddressLLIDEntry,'hpnicfEponDeviceRemoteMACAddressLLIDName':hpnicfEponDeviceRemoteMACAddressLLIDName,_n:hpnicfEponDeviceRMadlLLID,_o:hpnicfEponDeviceRMadlLogID,_p:hpnicfEponDeviceRMadlRemoteAddress,_q:hpnicfEponDeviceRMadlType,_r:hpnicfEponDeviceRMadlAction,_s:hpnicfEponDeviceRMadlEntryStatus,'hpnicfEponDeviceStatObjects':hpnicfEponDeviceStatObjects,'hpnicfEponDeviceStatTable':hpnicfEponDeviceStatTable,'hpnicfEponDeviceStatEntry':hpnicfEponDeviceStatEntry,_t:hpnicfEponDeviceStatTxFramesQueue0,_u:hpnicfEponDeviceStatTxFramesQueue1,_v:hpnicfEponDeviceStatTxFramesQueue2,_w:hpnicfEponDeviceStatTxFramesQueue3,_x:hpnicfEponDeviceStatTxFramesQueue4,_y:hpnicfEponDeviceStatTxFramesQueue5,_z:hpnicfEponDeviceStatTxFramesQueue6,_A0:hpnicfEponDeviceStatTxFramesQueue7,_A1:hpnicfEponDeviceStatRxFramesQueue0,_A2:hpnicfEponDeviceStatRxFramesQueue1,_A3:hpnicfEponDeviceStatRxFramesQueue2,_A4:hpnicfEponDeviceStatRxFramesQueue3,_A5:hpnicfEponDeviceStatRxFramesQueue4,_A6:hpnicfEponDeviceStatRxFramesQueue5,_A7:hpnicfEponDeviceStatRxFramesQueue6,_A8:hpnicfEponDeviceStatRxFramesQueue7,_A9:hpnicfEponDeviceStatDroppedFramesQueue0,_AA:hpnicfEponDeviceStatDroppedFramesQueue1,_AB:hpnicfEponDeviceStatDroppedFramesQueue2,_AC:hpnicfEponDeviceStatDroppedFramesQueue3,_AD:hpnicfEponDeviceStatDroppedFramesQueue4,_AE:hpnicfEponDeviceStatDroppedFramesQueue5,_AF:hpnicfEponDeviceStatDroppedFramesQueue6,_AG:hpnicfEponDeviceStatDroppedFramesQueue7,'hpnicfEponDeviceEventObjects':hpnicfEponDeviceEventObjects,'hpnicfEponDeviceEventObjectTable':hpnicfEponDeviceEventObjectTable,'hpnicfEponDeviceEventObjectEntry':hpnicfEponDeviceEventObjectEntry,_AH:hpnicfEponDeviceSampleMinimum,_O:hpnicfEponDeviceDyingGaspAlarmState,_AI:hpnicfEponDeviceDyingGaspAlarmEnabled,_P:hpnicfEponDeviceCriticalEventState,_AJ:hpnicfEponDeviceCriticalEventEnabled,_Q:hpnicfEponDeviceLocalLinkFaultAlarmState,_AK:hpnicfEponDeviceLocalLinkFaultAlarmEnabled,_R:hpnicfEponDeviceTemperatureEventIndicationState,_AL:hpnicfEponDeviceTemperatureEventIndicationEnabled,_S:hpnicfEponDevicePowerVoltageEventIndicationState,_AM:hpnicfEponDevicePowerVoltageEventIndicationEnabled,_T:hpnicfEponDeviceGlobalEventState,_AN:hpnicfEponDeviceGlobalEventEnabled,_U:hpnicfEponDeviceErroredSymbolPeriodEventState,_AO:hpnicfEponDeviceErroredSymbolPeriodEventEnabled,_V:hpnicfEponDeviceErroredFrameEventState,_AP:hpnicfEponDeviceErroredFrameEventEnabled,_W:hpnicfEponDeviceErroredFramePeriodEventState,_AQ:hpnicfEponDeviceErroredFramePeriodEventEnabled,_X:hpnicfEponDeviceErroredFrameSecondsSummaryEventState,_AR:hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled,_Y:hpnicfEponDeviceOrganizationSpecificEventState,_AS:hpnicfEponDeviceOrganizationSpecificEventEnabled,_AT:hpnicfEponDeviceEventControl,'hpnicfEponDeviceEventsLogTable':hpnicfEponDeviceEventsLogTable,'hpnicfEponDeviceEventsLogEntry':hpnicfEponDeviceEventsLogEntry,_b:hpnicfEponDeviceEventsLogName,_c:hpnicfEponDeviceEventsLogIndex,_AU:hpnicfEponDeviceEventsLogID,_AV:hpnicfEponDeviceEventsLogFirstTime,_AW:hpnicfEponDeviceEventsLogLastTime,_AX:hpnicfEponDeviceEventsLogCounts,_AY:hpnicfEponDeviceEventsLogType,_AZ:hpnicfEponDeviceEventsLogEntryStatus,'hpnicfEponDeviceConformance':hpnicfEponDeviceConformance,'hpnicfEponDeviceGroups':hpnicfEponDeviceGroups,_Aa:hpnicfEponDeviceGroupControl,_Ab:hpnicfEponDeviceGroupRMadLTable,_Ac:hpnicfEponDeviceGroupStat,_Ad:hpnicfEponDeviceGroupEvent,_Ae:hpnicfEponDeviceGroupEventLog,'hpnicfEponDeviceCompliances':hpnicfEponDeviceCompliances,'hpnicfEponDeviceCompliance':hpnicfEponDeviceCompliance})