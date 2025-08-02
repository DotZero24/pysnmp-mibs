_Ae='h3cEponDeviceGroupEventLog'
_Ad='h3cEponDeviceGroupEvent'
_Ac='h3cEponDeviceGroupStat'
_Ab='h3cEponDeviceGroupRMadLTable'
_Aa='h3cEponDeviceGroupControl'
_AZ='h3cEponDeviceEventsLogEntryStatus'
_AY='h3cEponDeviceEventsLogType'
_AX='h3cEponDeviceEventsLogCounts'
_AW='h3cEponDeviceEventsLogLastTime'
_AV='h3cEponDeviceEventsLogFirstTime'
_AU='h3cEponDeviceEventsLogID'
_AT='h3cEponDeviceEventControl'
_AS='h3cEponDeviceOrganizationSpecificEventEnabled'
_AR='h3cEponDeviceErroredFrameSecondsSummaryEventEnabled'
_AQ='h3cEponDeviceErroredFramePeriodEventEnabled'
_AP='h3cEponDeviceErroredFrameEventEnabled'
_AO='h3cEponDeviceErroredSymbolPeriodEventEnabled'
_AN='h3cEponDeviceGlobalEventEnabled'
_AM='h3cEponDevicePowerVoltageEventIndicationEnabled'
_AL='h3cEponDeviceTemperatureEventIndicationEnabled'
_AK='h3cEponDeviceLocalLinkFaultAlarmEnabled'
_AJ='h3cEponDeviceCriticalEventEnabled'
_AI='h3cEponDeviceDyingGaspAlarmEnabled'
_AH='h3cEponDeviceSampleMinimum'
_AG='h3cEponDeviceStatDroppedFramesQueue7'
_AF='h3cEponDeviceStatDroppedFramesQueue6'
_AE='h3cEponDeviceStatDroppedFramesQueue5'
_AD='h3cEponDeviceStatDroppedFramesQueue4'
_AC='h3cEponDeviceStatDroppedFramesQueue3'
_AB='h3cEponDeviceStatDroppedFramesQueue2'
_AA='h3cEponDeviceStatDroppedFramesQueue1'
_A9='h3cEponDeviceStatDroppedFramesQueue0'
_A8='h3cEponDeviceStatRxFramesQueue7'
_A7='h3cEponDeviceStatRxFramesQueue6'
_A6='h3cEponDeviceStatRxFramesQueue5'
_A5='h3cEponDeviceStatRxFramesQueue4'
_A4='h3cEponDeviceStatRxFramesQueue3'
_A3='h3cEponDeviceStatRxFramesQueue2'
_A2='h3cEponDeviceStatRxFramesQueue1'
_A1='h3cEponDeviceStatRxFramesQueue0'
_A0='h3cEponDeviceStatTxFramesQueue7'
_z='h3cEponDeviceStatTxFramesQueue6'
_y='h3cEponDeviceStatTxFramesQueue5'
_x='h3cEponDeviceStatTxFramesQueue4'
_w='h3cEponDeviceStatTxFramesQueue3'
_v='h3cEponDeviceStatTxFramesQueue2'
_u='h3cEponDeviceStatTxFramesQueue1'
_t='h3cEponDeviceStatTxFramesQueue0'
_s='h3cEponDeviceRMadlEntryStatus'
_r='h3cEponDeviceRMadlAction'
_q='h3cEponDeviceRMadlType'
_p='h3cEponDeviceRMadlRemoteAddress'
_o='h3cEponDeviceRMadlLogID'
_n='h3cEponDeviceRMadlLLID'
_m='h3cEponDeviceRemoteMACAddressLLIDControl'
_l='h3cEponDeviceObjectReportThreshold'
_k='h3cEponDeviceObjectNumberOfLLIDs'
_j='h3cEponDeviceObjectPowerDown'
_i='h3cEponDeviceObjectDeviceReadyMode'
_h='h3cEponDeviceObjectOamMode'
_g='h3cEponDeviceObjectFecEnabled'
_f='h3cEponDeviceObjectModes'
_e='h3cEponDeviceObjectReset'
_d='not-accessible'
_c='h3cEponDeviceEventsLogIndex'
_b='h3cEponDeviceEventsLogName'
_a='useDefaultReporting'
_Z='resetLog'
_Y='h3cEponDeviceOrganizationSpecificEventState'
_X='h3cEponDeviceErroredFrameSecondsSummaryEventState'
_W='h3cEponDeviceErroredFramePeriodEventState'
_V='h3cEponDeviceErroredFrameEventState'
_U='h3cEponDeviceErroredSymbolPeriodEventState'
_T='h3cEponDeviceGlobalEventState'
_S='h3cEponDevicePowerVoltageEventIndicationState'
_R='h3cEponDeviceTemperatureEventIndicationState'
_Q='h3cEponDeviceLocalLinkFaultAlarmState'
_P='h3cEponDeviceCriticalEventState'
_O='h3cEponDeviceDyingGaspAlarmState'
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
_B='H3C-EPON-DEVICE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString',_K)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cEpon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cEpon')
ifIndex,=mibBuilder.importSymbols(_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso','mib-2','zeroDotZero')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
h3cEponDeviceMIB=ModuleIdentity((1,3,6,1,4,1,2011,10,2,42,4))
if mibBuilder.loadTexts:h3cEponDeviceMIB.setRevisions(('2004-09-21 00:00',))
_H3cEponDeviceObjectMIB_ObjectIdentity=ObjectIdentity
h3cEponDeviceObjectMIB=_H3cEponDeviceObjectMIB_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1))
_H3cEponDeviceObjects_ObjectIdentity=ObjectIdentity
h3cEponDeviceObjects=_H3cEponDeviceObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1,1))
_H3cEponDeviceControlObjects_ObjectIdentity=ObjectIdentity
h3cEponDeviceControlObjects=_H3cEponDeviceControlObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1,1,1))
_H3cEponDeviceControlTable_Object=MibTable
h3cEponDeviceControlTable=_H3cEponDeviceControlTable_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1))
if mibBuilder.loadTexts:h3cEponDeviceControlTable.setStatus(_A)
_H3cEponDeviceControlEntry_Object=MibTableRow
h3cEponDeviceControlEntry=_H3cEponDeviceControlEntry_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1))
h3cEponDeviceControlEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cEponDeviceControlEntry.setStatus(_A)
class _H3cEponDeviceObjectReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('reset',2)))
_H3cEponDeviceObjectReset_Type.__name__=_F
_H3cEponDeviceObjectReset_Object=MibTableColumn
h3cEponDeviceObjectReset=_H3cEponDeviceObjectReset_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,1),_H3cEponDeviceObjectReset_Type())
h3cEponDeviceObjectReset.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceObjectReset.setStatus(_A)
class _H3cEponDeviceObjectModes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('olt',1),('onu',2)))
_H3cEponDeviceObjectModes_Type.__name__=_F
_H3cEponDeviceObjectModes_Object=MibTableColumn
h3cEponDeviceObjectModes=_H3cEponDeviceObjectModes_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,2),_H3cEponDeviceObjectModes_Type())
h3cEponDeviceObjectModes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceObjectModes.setStatus(_A)
class _H3cEponDeviceObjectFecEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noFecEnabled',1),('fecTxEnabled',2),('fecRxEnabled',3),('fecTxRxEnabled',4)))
_H3cEponDeviceObjectFecEnabled_Type.__name__=_F
_H3cEponDeviceObjectFecEnabled_Object=MibTableColumn
h3cEponDeviceObjectFecEnabled=_H3cEponDeviceObjectFecEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,4),_H3cEponDeviceObjectFecEnabled_Type())
h3cEponDeviceObjectFecEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceObjectFecEnabled.setStatus(_A)
class _H3cEponDeviceObjectOamMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOam',1),('oamServer',2),('oamclient',3)))
_H3cEponDeviceObjectOamMode_Type.__name__=_F
_H3cEponDeviceObjectOamMode_Object=MibTableColumn
h3cEponDeviceObjectOamMode=_H3cEponDeviceObjectOamMode_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,5),_H3cEponDeviceObjectOamMode_Type())
h3cEponDeviceObjectOamMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceObjectOamMode.setStatus(_A)
class _H3cEponDeviceObjectDeviceReadyMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notReady',1),('inProcess',2),('ready',3)))
_H3cEponDeviceObjectDeviceReadyMode_Type.__name__=_F
_H3cEponDeviceObjectDeviceReadyMode_Object=MibTableColumn
h3cEponDeviceObjectDeviceReadyMode=_H3cEponDeviceObjectDeviceReadyMode_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,6),_H3cEponDeviceObjectDeviceReadyMode_Type())
h3cEponDeviceObjectDeviceReadyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceObjectDeviceReadyMode.setStatus(_A)
class _H3cEponDeviceObjectPowerDown_Type(TruthValue):defaultValue=2
_H3cEponDeviceObjectPowerDown_Type.__name__=_G
_H3cEponDeviceObjectPowerDown_Object=MibTableColumn
h3cEponDeviceObjectPowerDown=_H3cEponDeviceObjectPowerDown_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,7),_H3cEponDeviceObjectPowerDown_Type())
h3cEponDeviceObjectPowerDown.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceObjectPowerDown.setStatus(_A)
_H3cEponDeviceObjectNumberOfLLIDs_Type=Integer32
_H3cEponDeviceObjectNumberOfLLIDs_Object=MibTableColumn
h3cEponDeviceObjectNumberOfLLIDs=_H3cEponDeviceObjectNumberOfLLIDs_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,8),_H3cEponDeviceObjectNumberOfLLIDs_Type())
h3cEponDeviceObjectNumberOfLLIDs.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceObjectNumberOfLLIDs.setStatus(_A)
class _H3cEponDeviceObjectReportThreshold_Type(Integer32):defaultValue=0
_H3cEponDeviceObjectReportThreshold_Type.__name__=_F
_H3cEponDeviceObjectReportThreshold_Object=MibTableColumn
h3cEponDeviceObjectReportThreshold=_H3cEponDeviceObjectReportThreshold_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,9),_H3cEponDeviceObjectReportThreshold_Type())
h3cEponDeviceObjectReportThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceObjectReportThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceObjectReportThreshold.setUnits('TQ (16nsec)')
class _H3cEponDeviceRemoteMACAddressLLIDControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_Z,2),(_a,3)))
_H3cEponDeviceRemoteMACAddressLLIDControl_Type.__name__=_F
_H3cEponDeviceRemoteMACAddressLLIDControl_Object=MibTableColumn
h3cEponDeviceRemoteMACAddressLLIDControl=_H3cEponDeviceRemoteMACAddressLLIDControl_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,1,1,10),_H3cEponDeviceRemoteMACAddressLLIDControl_Type())
h3cEponDeviceRemoteMACAddressLLIDControl.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceRemoteMACAddressLLIDControl.setStatus(_A)
_H3cEponDeviceRemoteMACAddressLLIDTable_Object=MibTable
h3cEponDeviceRemoteMACAddressLLIDTable=_H3cEponDeviceRemoteMACAddressLLIDTable_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2))
if mibBuilder.loadTexts:h3cEponDeviceRemoteMACAddressLLIDTable.setStatus(_A)
_H3cEponDeviceRemoteMACAddressLLIDEntry_Object=MibTableRow
h3cEponDeviceRemoteMACAddressLLIDEntry=_H3cEponDeviceRemoteMACAddressLLIDEntry_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1))
h3cEponDeviceRemoteMACAddressLLIDEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cEponDeviceRemoteMACAddressLLIDEntry.setStatus(_A)
class _H3cEponDeviceRemoteMACAddressLLIDName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cEponDeviceRemoteMACAddressLLIDName_Type.__name__=_L
_H3cEponDeviceRemoteMACAddressLLIDName_Object=MibTableColumn
h3cEponDeviceRemoteMACAddressLLIDName=_H3cEponDeviceRemoteMACAddressLLIDName_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1,1),_H3cEponDeviceRemoteMACAddressLLIDName_Type())
h3cEponDeviceRemoteMACAddressLLIDName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceRemoteMACAddressLLIDName.setStatus(_A)
class _H3cEponDeviceRMadlLLID_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cEponDeviceRMadlLLID_Type.__name__=_M
_H3cEponDeviceRMadlLLID_Object=MibTableColumn
h3cEponDeviceRMadlLLID=_H3cEponDeviceRMadlLLID_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1,2),_H3cEponDeviceRMadlLLID_Type())
h3cEponDeviceRMadlLLID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceRMadlLLID.setStatus(_A)
class _H3cEponDeviceRMadlLogID_Type(ObjectIdentifier):defaultValue=0,0
_H3cEponDeviceRMadlLogID_Type.__name__=_K
_H3cEponDeviceRMadlLogID_Object=MibTableColumn
h3cEponDeviceRMadlLogID=_H3cEponDeviceRMadlLogID_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1,3),_H3cEponDeviceRMadlLogID_Type())
h3cEponDeviceRMadlLogID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceRMadlLogID.setStatus(_A)
_H3cEponDeviceRMadlRemoteAddress_Type=MacAddress
_H3cEponDeviceRMadlRemoteAddress_Object=MibTableColumn
h3cEponDeviceRMadlRemoteAddress=_H3cEponDeviceRMadlRemoteAddress_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1,4),_H3cEponDeviceRMadlRemoteAddress_Type())
h3cEponDeviceRMadlRemoteAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceRMadlRemoteAddress.setStatus(_A)
class _H3cEponDeviceRMadlType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notRegister',1),('registered',2)))
_H3cEponDeviceRMadlType_Type.__name__=_F
_H3cEponDeviceRMadlType_Object=MibTableColumn
h3cEponDeviceRMadlType=_H3cEponDeviceRMadlType_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1,5),_H3cEponDeviceRMadlType_Type())
h3cEponDeviceRMadlType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceRMadlType.setStatus(_A)
class _H3cEponDeviceRMadlAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('register',2),('deregister',3),('reregister',4)))
_H3cEponDeviceRMadlAction_Type.__name__=_F
_H3cEponDeviceRMadlAction_Object=MibTableColumn
h3cEponDeviceRMadlAction=_H3cEponDeviceRMadlAction_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1,6),_H3cEponDeviceRMadlAction_Type())
h3cEponDeviceRMadlAction.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceRMadlAction.setStatus(_A)
_H3cEponDeviceRMadlEntryStatus_Type=RowStatus
_H3cEponDeviceRMadlEntryStatus_Object=MibTableColumn
h3cEponDeviceRMadlEntryStatus=_H3cEponDeviceRMadlEntryStatus_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,1,2,1,7),_H3cEponDeviceRMadlEntryStatus_Type())
h3cEponDeviceRMadlEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceRMadlEntryStatus.setStatus(_A)
_H3cEponDeviceStatObjects_ObjectIdentity=ObjectIdentity
h3cEponDeviceStatObjects=_H3cEponDeviceStatObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1,1,2))
_H3cEponDeviceStatTable_Object=MibTable
h3cEponDeviceStatTable=_H3cEponDeviceStatTable_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1))
if mibBuilder.loadTexts:h3cEponDeviceStatTable.setStatus(_A)
_H3cEponDeviceStatEntry_Object=MibTableRow
h3cEponDeviceStatEntry=_H3cEponDeviceStatEntry_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1))
h3cEponDeviceStatEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cEponDeviceStatEntry.setStatus(_A)
_H3cEponDeviceStatTxFramesQueue0_Type=Counter32
_H3cEponDeviceStatTxFramesQueue0_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue0=_H3cEponDeviceStatTxFramesQueue0_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,1),_H3cEponDeviceStatTxFramesQueue0_Type())
h3cEponDeviceStatTxFramesQueue0.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue0.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue0.setUnits(_D)
_H3cEponDeviceStatTxFramesQueue1_Type=Counter32
_H3cEponDeviceStatTxFramesQueue1_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue1=_H3cEponDeviceStatTxFramesQueue1_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,2),_H3cEponDeviceStatTxFramesQueue1_Type())
h3cEponDeviceStatTxFramesQueue1.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue1.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue1.setUnits(_D)
_H3cEponDeviceStatTxFramesQueue2_Type=Counter32
_H3cEponDeviceStatTxFramesQueue2_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue2=_H3cEponDeviceStatTxFramesQueue2_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,3),_H3cEponDeviceStatTxFramesQueue2_Type())
h3cEponDeviceStatTxFramesQueue2.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue2.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue2.setUnits(_D)
_H3cEponDeviceStatTxFramesQueue3_Type=Counter32
_H3cEponDeviceStatTxFramesQueue3_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue3=_H3cEponDeviceStatTxFramesQueue3_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,4),_H3cEponDeviceStatTxFramesQueue3_Type())
h3cEponDeviceStatTxFramesQueue3.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue3.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue3.setUnits(_D)
_H3cEponDeviceStatTxFramesQueue4_Type=Counter32
_H3cEponDeviceStatTxFramesQueue4_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue4=_H3cEponDeviceStatTxFramesQueue4_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,5),_H3cEponDeviceStatTxFramesQueue4_Type())
h3cEponDeviceStatTxFramesQueue4.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue4.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue4.setUnits(_D)
_H3cEponDeviceStatTxFramesQueue5_Type=Counter32
_H3cEponDeviceStatTxFramesQueue5_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue5=_H3cEponDeviceStatTxFramesQueue5_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,6),_H3cEponDeviceStatTxFramesQueue5_Type())
h3cEponDeviceStatTxFramesQueue5.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue5.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue5.setUnits(_D)
_H3cEponDeviceStatTxFramesQueue6_Type=Counter32
_H3cEponDeviceStatTxFramesQueue6_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue6=_H3cEponDeviceStatTxFramesQueue6_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,7),_H3cEponDeviceStatTxFramesQueue6_Type())
h3cEponDeviceStatTxFramesQueue6.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue6.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue6.setUnits(_D)
_H3cEponDeviceStatTxFramesQueue7_Type=Counter32
_H3cEponDeviceStatTxFramesQueue7_Object=MibTableColumn
h3cEponDeviceStatTxFramesQueue7=_H3cEponDeviceStatTxFramesQueue7_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,8),_H3cEponDeviceStatTxFramesQueue7_Type())
h3cEponDeviceStatTxFramesQueue7.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue7.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatTxFramesQueue7.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue0_Type=Counter32
_H3cEponDeviceStatRxFramesQueue0_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue0=_H3cEponDeviceStatRxFramesQueue0_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,9),_H3cEponDeviceStatRxFramesQueue0_Type())
h3cEponDeviceStatRxFramesQueue0.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue0.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue0.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue1_Type=Counter32
_H3cEponDeviceStatRxFramesQueue1_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue1=_H3cEponDeviceStatRxFramesQueue1_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,10),_H3cEponDeviceStatRxFramesQueue1_Type())
h3cEponDeviceStatRxFramesQueue1.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue1.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue1.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue2_Type=Counter32
_H3cEponDeviceStatRxFramesQueue2_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue2=_H3cEponDeviceStatRxFramesQueue2_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,11),_H3cEponDeviceStatRxFramesQueue2_Type())
h3cEponDeviceStatRxFramesQueue2.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue2.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue2.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue3_Type=Counter32
_H3cEponDeviceStatRxFramesQueue3_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue3=_H3cEponDeviceStatRxFramesQueue3_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,12),_H3cEponDeviceStatRxFramesQueue3_Type())
h3cEponDeviceStatRxFramesQueue3.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue3.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue3.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue4_Type=Counter32
_H3cEponDeviceStatRxFramesQueue4_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue4=_H3cEponDeviceStatRxFramesQueue4_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,13),_H3cEponDeviceStatRxFramesQueue4_Type())
h3cEponDeviceStatRxFramesQueue4.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue4.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue4.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue5_Type=Counter32
_H3cEponDeviceStatRxFramesQueue5_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue5=_H3cEponDeviceStatRxFramesQueue5_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,14),_H3cEponDeviceStatRxFramesQueue5_Type())
h3cEponDeviceStatRxFramesQueue5.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue5.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue5.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue6_Type=Counter32
_H3cEponDeviceStatRxFramesQueue6_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue6=_H3cEponDeviceStatRxFramesQueue6_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,15),_H3cEponDeviceStatRxFramesQueue6_Type())
h3cEponDeviceStatRxFramesQueue6.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue6.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue6.setUnits(_D)
_H3cEponDeviceStatRxFramesQueue7_Type=Counter32
_H3cEponDeviceStatRxFramesQueue7_Object=MibTableColumn
h3cEponDeviceStatRxFramesQueue7=_H3cEponDeviceStatRxFramesQueue7_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,16),_H3cEponDeviceStatRxFramesQueue7_Type())
h3cEponDeviceStatRxFramesQueue7.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue7.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatRxFramesQueue7.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue0_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue0_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue0=_H3cEponDeviceStatDroppedFramesQueue0_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,17),_H3cEponDeviceStatDroppedFramesQueue0_Type())
h3cEponDeviceStatDroppedFramesQueue0.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue0.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue0.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue1_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue1_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue1=_H3cEponDeviceStatDroppedFramesQueue1_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,18),_H3cEponDeviceStatDroppedFramesQueue1_Type())
h3cEponDeviceStatDroppedFramesQueue1.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue1.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue1.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue2_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue2_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue2=_H3cEponDeviceStatDroppedFramesQueue2_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,19),_H3cEponDeviceStatDroppedFramesQueue2_Type())
h3cEponDeviceStatDroppedFramesQueue2.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue2.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue2.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue3_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue3_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue3=_H3cEponDeviceStatDroppedFramesQueue3_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,20),_H3cEponDeviceStatDroppedFramesQueue3_Type())
h3cEponDeviceStatDroppedFramesQueue3.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue3.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue3.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue4_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue4_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue4=_H3cEponDeviceStatDroppedFramesQueue4_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,21),_H3cEponDeviceStatDroppedFramesQueue4_Type())
h3cEponDeviceStatDroppedFramesQueue4.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue4.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue4.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue5_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue5_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue5=_H3cEponDeviceStatDroppedFramesQueue5_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,22),_H3cEponDeviceStatDroppedFramesQueue5_Type())
h3cEponDeviceStatDroppedFramesQueue5.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue5.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue5.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue6_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue6_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue6=_H3cEponDeviceStatDroppedFramesQueue6_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,23),_H3cEponDeviceStatDroppedFramesQueue6_Type())
h3cEponDeviceStatDroppedFramesQueue6.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue6.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue6.setUnits(_D)
_H3cEponDeviceStatDroppedFramesQueue7_Type=Counter32
_H3cEponDeviceStatDroppedFramesQueue7_Object=MibTableColumn
h3cEponDeviceStatDroppedFramesQueue7=_H3cEponDeviceStatDroppedFramesQueue7_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,2,1,1,24),_H3cEponDeviceStatDroppedFramesQueue7_Type())
h3cEponDeviceStatDroppedFramesQueue7.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue7.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceStatDroppedFramesQueue7.setUnits(_D)
_H3cEponDeviceEventObjects_ObjectIdentity=ObjectIdentity
h3cEponDeviceEventObjects=_H3cEponDeviceEventObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1,1,3))
_H3cEponDeviceEventObjectTable_Object=MibTable
h3cEponDeviceEventObjectTable=_H3cEponDeviceEventObjectTable_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1))
if mibBuilder.loadTexts:h3cEponDeviceEventObjectTable.setStatus(_A)
_H3cEponDeviceEventObjectEntry_Object=MibTableRow
h3cEponDeviceEventObjectEntry=_H3cEponDeviceEventObjectEntry_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1))
h3cEponDeviceEventObjectEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cEponDeviceEventObjectEntry.setStatus(_A)
class _H3cEponDeviceSampleMinimum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cEponDeviceSampleMinimum_Type.__name__=_F
_H3cEponDeviceSampleMinimum_Object=MibTableColumn
h3cEponDeviceSampleMinimum=_H3cEponDeviceSampleMinimum_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,1),_H3cEponDeviceSampleMinimum_Type())
h3cEponDeviceSampleMinimum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceSampleMinimum.setStatus(_A)
if mibBuilder.loadTexts:h3cEponDeviceSampleMinimum.setUnits('seconds')
_H3cEponDeviceDyingGaspAlarmState_Type=TruthValue
_H3cEponDeviceDyingGaspAlarmState_Object=MibTableColumn
h3cEponDeviceDyingGaspAlarmState=_H3cEponDeviceDyingGaspAlarmState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,2),_H3cEponDeviceDyingGaspAlarmState_Type())
h3cEponDeviceDyingGaspAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceDyingGaspAlarmState.setStatus(_A)
class _H3cEponDeviceDyingGaspAlarmEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceDyingGaspAlarmEnabled_Type.__name__=_G
_H3cEponDeviceDyingGaspAlarmEnabled_Object=MibTableColumn
h3cEponDeviceDyingGaspAlarmEnabled=_H3cEponDeviceDyingGaspAlarmEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,3),_H3cEponDeviceDyingGaspAlarmEnabled_Type())
h3cEponDeviceDyingGaspAlarmEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceDyingGaspAlarmEnabled.setStatus(_A)
_H3cEponDeviceCriticalEventState_Type=TruthValue
_H3cEponDeviceCriticalEventState_Object=MibTableColumn
h3cEponDeviceCriticalEventState=_H3cEponDeviceCriticalEventState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,4),_H3cEponDeviceCriticalEventState_Type())
h3cEponDeviceCriticalEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceCriticalEventState.setStatus(_A)
class _H3cEponDeviceCriticalEventEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceCriticalEventEnabled_Type.__name__=_G
_H3cEponDeviceCriticalEventEnabled_Object=MibTableColumn
h3cEponDeviceCriticalEventEnabled=_H3cEponDeviceCriticalEventEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,5),_H3cEponDeviceCriticalEventEnabled_Type())
h3cEponDeviceCriticalEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceCriticalEventEnabled.setStatus(_A)
_H3cEponDeviceLocalLinkFaultAlarmState_Type=TruthValue
_H3cEponDeviceLocalLinkFaultAlarmState_Object=MibTableColumn
h3cEponDeviceLocalLinkFaultAlarmState=_H3cEponDeviceLocalLinkFaultAlarmState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,6),_H3cEponDeviceLocalLinkFaultAlarmState_Type())
h3cEponDeviceLocalLinkFaultAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceLocalLinkFaultAlarmState.setStatus(_A)
class _H3cEponDeviceLocalLinkFaultAlarmEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceLocalLinkFaultAlarmEnabled_Type.__name__=_G
_H3cEponDeviceLocalLinkFaultAlarmEnabled_Object=MibTableColumn
h3cEponDeviceLocalLinkFaultAlarmEnabled=_H3cEponDeviceLocalLinkFaultAlarmEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,7),_H3cEponDeviceLocalLinkFaultAlarmEnabled_Type())
h3cEponDeviceLocalLinkFaultAlarmEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceLocalLinkFaultAlarmEnabled.setStatus(_A)
_H3cEponDeviceTemperatureEventIndicationState_Type=TruthValue
_H3cEponDeviceTemperatureEventIndicationState_Object=MibTableColumn
h3cEponDeviceTemperatureEventIndicationState=_H3cEponDeviceTemperatureEventIndicationState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,8),_H3cEponDeviceTemperatureEventIndicationState_Type())
h3cEponDeviceTemperatureEventIndicationState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceTemperatureEventIndicationState.setStatus(_A)
class _H3cEponDeviceTemperatureEventIndicationEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceTemperatureEventIndicationEnabled_Type.__name__=_G
_H3cEponDeviceTemperatureEventIndicationEnabled_Object=MibTableColumn
h3cEponDeviceTemperatureEventIndicationEnabled=_H3cEponDeviceTemperatureEventIndicationEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,9),_H3cEponDeviceTemperatureEventIndicationEnabled_Type())
h3cEponDeviceTemperatureEventIndicationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceTemperatureEventIndicationEnabled.setStatus(_A)
_H3cEponDevicePowerVoltageEventIndicationState_Type=TruthValue
_H3cEponDevicePowerVoltageEventIndicationState_Object=MibTableColumn
h3cEponDevicePowerVoltageEventIndicationState=_H3cEponDevicePowerVoltageEventIndicationState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,10),_H3cEponDevicePowerVoltageEventIndicationState_Type())
h3cEponDevicePowerVoltageEventIndicationState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDevicePowerVoltageEventIndicationState.setStatus(_A)
class _H3cEponDevicePowerVoltageEventIndicationEnabled_Type(TruthValue):defaultValue=2
_H3cEponDevicePowerVoltageEventIndicationEnabled_Type.__name__=_G
_H3cEponDevicePowerVoltageEventIndicationEnabled_Object=MibTableColumn
h3cEponDevicePowerVoltageEventIndicationEnabled=_H3cEponDevicePowerVoltageEventIndicationEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,11),_H3cEponDevicePowerVoltageEventIndicationEnabled_Type())
h3cEponDevicePowerVoltageEventIndicationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDevicePowerVoltageEventIndicationEnabled.setStatus(_A)
_H3cEponDeviceGlobalEventState_Type=TruthValue
_H3cEponDeviceGlobalEventState_Object=MibTableColumn
h3cEponDeviceGlobalEventState=_H3cEponDeviceGlobalEventState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,12),_H3cEponDeviceGlobalEventState_Type())
h3cEponDeviceGlobalEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceGlobalEventState.setStatus(_A)
class _H3cEponDeviceGlobalEventEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceGlobalEventEnabled_Type.__name__=_G
_H3cEponDeviceGlobalEventEnabled_Object=MibTableColumn
h3cEponDeviceGlobalEventEnabled=_H3cEponDeviceGlobalEventEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,13),_H3cEponDeviceGlobalEventEnabled_Type())
h3cEponDeviceGlobalEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceGlobalEventEnabled.setStatus(_A)
_H3cEponDeviceErroredSymbolPeriodEventState_Type=TruthValue
_H3cEponDeviceErroredSymbolPeriodEventState_Object=MibTableColumn
h3cEponDeviceErroredSymbolPeriodEventState=_H3cEponDeviceErroredSymbolPeriodEventState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,14),_H3cEponDeviceErroredSymbolPeriodEventState_Type())
h3cEponDeviceErroredSymbolPeriodEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceErroredSymbolPeriodEventState.setStatus(_A)
class _H3cEponDeviceErroredSymbolPeriodEventEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceErroredSymbolPeriodEventEnabled_Type.__name__=_G
_H3cEponDeviceErroredSymbolPeriodEventEnabled_Object=MibTableColumn
h3cEponDeviceErroredSymbolPeriodEventEnabled=_H3cEponDeviceErroredSymbolPeriodEventEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,15),_H3cEponDeviceErroredSymbolPeriodEventEnabled_Type())
h3cEponDeviceErroredSymbolPeriodEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceErroredSymbolPeriodEventEnabled.setStatus(_A)
_H3cEponDeviceErroredFrameEventState_Type=TruthValue
_H3cEponDeviceErroredFrameEventState_Object=MibTableColumn
h3cEponDeviceErroredFrameEventState=_H3cEponDeviceErroredFrameEventState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,16),_H3cEponDeviceErroredFrameEventState_Type())
h3cEponDeviceErroredFrameEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceErroredFrameEventState.setStatus(_A)
class _H3cEponDeviceErroredFrameEventEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceErroredFrameEventEnabled_Type.__name__=_G
_H3cEponDeviceErroredFrameEventEnabled_Object=MibTableColumn
h3cEponDeviceErroredFrameEventEnabled=_H3cEponDeviceErroredFrameEventEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,17),_H3cEponDeviceErroredFrameEventEnabled_Type())
h3cEponDeviceErroredFrameEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceErroredFrameEventEnabled.setStatus(_A)
_H3cEponDeviceErroredFramePeriodEventState_Type=TruthValue
_H3cEponDeviceErroredFramePeriodEventState_Object=MibTableColumn
h3cEponDeviceErroredFramePeriodEventState=_H3cEponDeviceErroredFramePeriodEventState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,18),_H3cEponDeviceErroredFramePeriodEventState_Type())
h3cEponDeviceErroredFramePeriodEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceErroredFramePeriodEventState.setStatus(_A)
class _H3cEponDeviceErroredFramePeriodEventEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceErroredFramePeriodEventEnabled_Type.__name__=_G
_H3cEponDeviceErroredFramePeriodEventEnabled_Object=MibTableColumn
h3cEponDeviceErroredFramePeriodEventEnabled=_H3cEponDeviceErroredFramePeriodEventEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,19),_H3cEponDeviceErroredFramePeriodEventEnabled_Type())
h3cEponDeviceErroredFramePeriodEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceErroredFramePeriodEventEnabled.setStatus(_A)
_H3cEponDeviceErroredFrameSecondsSummaryEventState_Type=TruthValue
_H3cEponDeviceErroredFrameSecondsSummaryEventState_Object=MibTableColumn
h3cEponDeviceErroredFrameSecondsSummaryEventState=_H3cEponDeviceErroredFrameSecondsSummaryEventState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,20),_H3cEponDeviceErroredFrameSecondsSummaryEventState_Type())
h3cEponDeviceErroredFrameSecondsSummaryEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceErroredFrameSecondsSummaryEventState.setStatus(_A)
class _H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Type.__name__=_G
_H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Object=MibTableColumn
h3cEponDeviceErroredFrameSecondsSummaryEventEnabled=_H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,21),_H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Type())
h3cEponDeviceErroredFrameSecondsSummaryEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceErroredFrameSecondsSummaryEventEnabled.setStatus(_A)
_H3cEponDeviceOrganizationSpecificEventState_Type=TruthValue
_H3cEponDeviceOrganizationSpecificEventState_Object=MibTableColumn
h3cEponDeviceOrganizationSpecificEventState=_H3cEponDeviceOrganizationSpecificEventState_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,22),_H3cEponDeviceOrganizationSpecificEventState_Type())
h3cEponDeviceOrganizationSpecificEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceOrganizationSpecificEventState.setStatus(_A)
class _H3cEponDeviceOrganizationSpecificEventEnabled_Type(TruthValue):defaultValue=2
_H3cEponDeviceOrganizationSpecificEventEnabled_Type.__name__=_G
_H3cEponDeviceOrganizationSpecificEventEnabled_Object=MibTableColumn
h3cEponDeviceOrganizationSpecificEventEnabled=_H3cEponDeviceOrganizationSpecificEventEnabled_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,23),_H3cEponDeviceOrganizationSpecificEventEnabled_Type())
h3cEponDeviceOrganizationSpecificEventEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceOrganizationSpecificEventEnabled.setStatus(_A)
class _H3cEponDeviceEventControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_Z,2),(_a,3)))
_H3cEponDeviceEventControl_Type.__name__=_F
_H3cEponDeviceEventControl_Object=MibTableColumn
h3cEponDeviceEventControl=_H3cEponDeviceEventControl_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,1,1,24),_H3cEponDeviceEventControl_Type())
h3cEponDeviceEventControl.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cEponDeviceEventControl.setStatus(_A)
_H3cEponDeviceEventsLogTable_Object=MibTable
h3cEponDeviceEventsLogTable=_H3cEponDeviceEventsLogTable_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2))
if mibBuilder.loadTexts:h3cEponDeviceEventsLogTable.setStatus(_A)
_H3cEponDeviceEventsLogEntry_Object=MibTableRow
h3cEponDeviceEventsLogEntry=_H3cEponDeviceEventsLogEntry_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1))
h3cEponDeviceEventsLogEntry.setIndexNames((0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:h3cEponDeviceEventsLogEntry.setStatus(_A)
class _H3cEponDeviceEventsLogName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cEponDeviceEventsLogName_Type.__name__=_L
_H3cEponDeviceEventsLogName_Object=MibTableColumn
h3cEponDeviceEventsLogName=_H3cEponDeviceEventsLogName_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,1),_H3cEponDeviceEventsLogName_Type())
h3cEponDeviceEventsLogName.setMaxAccess(_d)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogName.setStatus(_A)
class _H3cEponDeviceEventsLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cEponDeviceEventsLogIndex_Type.__name__=_M
_H3cEponDeviceEventsLogIndex_Object=MibTableColumn
h3cEponDeviceEventsLogIndex=_H3cEponDeviceEventsLogIndex_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,2),_H3cEponDeviceEventsLogIndex_Type())
h3cEponDeviceEventsLogIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogIndex.setStatus(_A)
class _H3cEponDeviceEventsLogID_Type(ObjectIdentifier):defaultValue=0,0
_H3cEponDeviceEventsLogID_Type.__name__=_K
_H3cEponDeviceEventsLogID_Object=MibTableColumn
h3cEponDeviceEventsLogID=_H3cEponDeviceEventsLogID_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,3),_H3cEponDeviceEventsLogID_Type())
h3cEponDeviceEventsLogID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogID.setStatus(_A)
_H3cEponDeviceEventsLogFirstTime_Type=DateAndTime
_H3cEponDeviceEventsLogFirstTime_Object=MibTableColumn
h3cEponDeviceEventsLogFirstTime=_H3cEponDeviceEventsLogFirstTime_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,4),_H3cEponDeviceEventsLogFirstTime_Type())
h3cEponDeviceEventsLogFirstTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogFirstTime.setStatus(_A)
_H3cEponDeviceEventsLogLastTime_Type=DateAndTime
_H3cEponDeviceEventsLogLastTime_Object=MibTableColumn
h3cEponDeviceEventsLogLastTime=_H3cEponDeviceEventsLogLastTime_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,5),_H3cEponDeviceEventsLogLastTime_Type())
h3cEponDeviceEventsLogLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogLastTime.setStatus(_A)
_H3cEponDeviceEventsLogCounts_Type=Counter32
_H3cEponDeviceEventsLogCounts_Object=MibTableColumn
h3cEponDeviceEventsLogCounts=_H3cEponDeviceEventsLogCounts_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,6),_H3cEponDeviceEventsLogCounts_Type())
h3cEponDeviceEventsLogCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogCounts.setStatus(_A)
class _H3cEponDeviceEventsLogType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11)))
_H3cEponDeviceEventsLogType_Type.__name__=_F
_H3cEponDeviceEventsLogType_Object=MibTableColumn
h3cEponDeviceEventsLogType=_H3cEponDeviceEventsLogType_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,7),_H3cEponDeviceEventsLogType_Type())
h3cEponDeviceEventsLogType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogType.setStatus(_A)
_H3cEponDeviceEventsLogEntryStatus_Type=RowStatus
_H3cEponDeviceEventsLogEntryStatus_Object=MibTableColumn
h3cEponDeviceEventsLogEntryStatus=_H3cEponDeviceEventsLogEntryStatus_Object((1,3,6,1,4,1,2011,10,2,42,4,1,1,3,2,1,8),_H3cEponDeviceEventsLogEntryStatus_Type())
h3cEponDeviceEventsLogEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cEponDeviceEventsLogEntryStatus.setStatus(_A)
_H3cEponDeviceConformance_ObjectIdentity=ObjectIdentity
h3cEponDeviceConformance=_H3cEponDeviceConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1,2))
_H3cEponDeviceGroups_ObjectIdentity=ObjectIdentity
h3cEponDeviceGroups=_H3cEponDeviceGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1,2,1))
_H3cEponDeviceCompliances_ObjectIdentity=ObjectIdentity
h3cEponDeviceCompliances=_H3cEponDeviceCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,4,1,2,2))
h3cEponDeviceGroupControl=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,4,1,2,1,1))
h3cEponDeviceGroupControl.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:h3cEponDeviceGroupControl.setStatus(_A)
h3cEponDeviceGroupRMadLTable=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,4,1,2,1,2))
h3cEponDeviceGroupRMadLTable.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:h3cEponDeviceGroupRMadLTable.setStatus(_A)
h3cEponDeviceGroupStat=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,4,1,2,1,3))
h3cEponDeviceGroupStat.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:h3cEponDeviceGroupStat.setStatus(_A)
h3cEponDeviceGroupEvent=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,4,1,2,1,4))
h3cEponDeviceGroupEvent.setObjects(*((_B,_AH),(_B,_O),(_B,_AI),(_B,_P),(_B,_AJ),(_B,_Q),(_B,_AK),(_B,_R),(_B,_AL),(_B,_S),(_B,_AM),(_B,_T),(_B,_AN),(_B,_U),(_B,_AO),(_B,_V),(_B,_AP),(_B,_W),(_B,_AQ),(_B,_X),(_B,_AR),(_B,_Y),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:h3cEponDeviceGroupEvent.setStatus(_A)
h3cEponDeviceGroupEventLog=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,4,1,2,1,5))
h3cEponDeviceGroupEventLog.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:h3cEponDeviceGroupEventLog.setStatus(_A)
h3cEponDeviceCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,42,4,1,2,2,1))
h3cEponDeviceCompliance.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:h3cEponDeviceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cEponDeviceMIB':h3cEponDeviceMIB,'h3cEponDeviceObjectMIB':h3cEponDeviceObjectMIB,'h3cEponDeviceObjects':h3cEponDeviceObjects,'h3cEponDeviceControlObjects':h3cEponDeviceControlObjects,'h3cEponDeviceControlTable':h3cEponDeviceControlTable,'h3cEponDeviceControlEntry':h3cEponDeviceControlEntry,_e:h3cEponDeviceObjectReset,_f:h3cEponDeviceObjectModes,_g:h3cEponDeviceObjectFecEnabled,_h:h3cEponDeviceObjectOamMode,_i:h3cEponDeviceObjectDeviceReadyMode,_j:h3cEponDeviceObjectPowerDown,_k:h3cEponDeviceObjectNumberOfLLIDs,_l:h3cEponDeviceObjectReportThreshold,_m:h3cEponDeviceRemoteMACAddressLLIDControl,'h3cEponDeviceRemoteMACAddressLLIDTable':h3cEponDeviceRemoteMACAddressLLIDTable,'h3cEponDeviceRemoteMACAddressLLIDEntry':h3cEponDeviceRemoteMACAddressLLIDEntry,'h3cEponDeviceRemoteMACAddressLLIDName':h3cEponDeviceRemoteMACAddressLLIDName,_n:h3cEponDeviceRMadlLLID,_o:h3cEponDeviceRMadlLogID,_p:h3cEponDeviceRMadlRemoteAddress,_q:h3cEponDeviceRMadlType,_r:h3cEponDeviceRMadlAction,_s:h3cEponDeviceRMadlEntryStatus,'h3cEponDeviceStatObjects':h3cEponDeviceStatObjects,'h3cEponDeviceStatTable':h3cEponDeviceStatTable,'h3cEponDeviceStatEntry':h3cEponDeviceStatEntry,_t:h3cEponDeviceStatTxFramesQueue0,_u:h3cEponDeviceStatTxFramesQueue1,_v:h3cEponDeviceStatTxFramesQueue2,_w:h3cEponDeviceStatTxFramesQueue3,_x:h3cEponDeviceStatTxFramesQueue4,_y:h3cEponDeviceStatTxFramesQueue5,_z:h3cEponDeviceStatTxFramesQueue6,_A0:h3cEponDeviceStatTxFramesQueue7,_A1:h3cEponDeviceStatRxFramesQueue0,_A2:h3cEponDeviceStatRxFramesQueue1,_A3:h3cEponDeviceStatRxFramesQueue2,_A4:h3cEponDeviceStatRxFramesQueue3,_A5:h3cEponDeviceStatRxFramesQueue4,_A6:h3cEponDeviceStatRxFramesQueue5,_A7:h3cEponDeviceStatRxFramesQueue6,_A8:h3cEponDeviceStatRxFramesQueue7,_A9:h3cEponDeviceStatDroppedFramesQueue0,_AA:h3cEponDeviceStatDroppedFramesQueue1,_AB:h3cEponDeviceStatDroppedFramesQueue2,_AC:h3cEponDeviceStatDroppedFramesQueue3,_AD:h3cEponDeviceStatDroppedFramesQueue4,_AE:h3cEponDeviceStatDroppedFramesQueue5,_AF:h3cEponDeviceStatDroppedFramesQueue6,_AG:h3cEponDeviceStatDroppedFramesQueue7,'h3cEponDeviceEventObjects':h3cEponDeviceEventObjects,'h3cEponDeviceEventObjectTable':h3cEponDeviceEventObjectTable,'h3cEponDeviceEventObjectEntry':h3cEponDeviceEventObjectEntry,_AH:h3cEponDeviceSampleMinimum,_O:h3cEponDeviceDyingGaspAlarmState,_AI:h3cEponDeviceDyingGaspAlarmEnabled,_P:h3cEponDeviceCriticalEventState,_AJ:h3cEponDeviceCriticalEventEnabled,_Q:h3cEponDeviceLocalLinkFaultAlarmState,_AK:h3cEponDeviceLocalLinkFaultAlarmEnabled,_R:h3cEponDeviceTemperatureEventIndicationState,_AL:h3cEponDeviceTemperatureEventIndicationEnabled,_S:h3cEponDevicePowerVoltageEventIndicationState,_AM:h3cEponDevicePowerVoltageEventIndicationEnabled,_T:h3cEponDeviceGlobalEventState,_AN:h3cEponDeviceGlobalEventEnabled,_U:h3cEponDeviceErroredSymbolPeriodEventState,_AO:h3cEponDeviceErroredSymbolPeriodEventEnabled,_V:h3cEponDeviceErroredFrameEventState,_AP:h3cEponDeviceErroredFrameEventEnabled,_W:h3cEponDeviceErroredFramePeriodEventState,_AQ:h3cEponDeviceErroredFramePeriodEventEnabled,_X:h3cEponDeviceErroredFrameSecondsSummaryEventState,_AR:h3cEponDeviceErroredFrameSecondsSummaryEventEnabled,_Y:h3cEponDeviceOrganizationSpecificEventState,_AS:h3cEponDeviceOrganizationSpecificEventEnabled,_AT:h3cEponDeviceEventControl,'h3cEponDeviceEventsLogTable':h3cEponDeviceEventsLogTable,'h3cEponDeviceEventsLogEntry':h3cEponDeviceEventsLogEntry,_b:h3cEponDeviceEventsLogName,_c:h3cEponDeviceEventsLogIndex,_AU:h3cEponDeviceEventsLogID,_AV:h3cEponDeviceEventsLogFirstTime,_AW:h3cEponDeviceEventsLogLastTime,_AX:h3cEponDeviceEventsLogCounts,_AY:h3cEponDeviceEventsLogType,_AZ:h3cEponDeviceEventsLogEntryStatus,'h3cEponDeviceConformance':h3cEponDeviceConformance,'h3cEponDeviceGroups':h3cEponDeviceGroups,_Aa:h3cEponDeviceGroupControl,_Ab:h3cEponDeviceGroupRMadLTable,_Ac:h3cEponDeviceGroupStat,_Ad:h3cEponDeviceGroupEvent,_Ae:h3cEponDeviceGroupEventLog,'h3cEponDeviceCompliances':h3cEponDeviceCompliances,'h3cEponDeviceCompliance':h3cEponDeviceCompliance})