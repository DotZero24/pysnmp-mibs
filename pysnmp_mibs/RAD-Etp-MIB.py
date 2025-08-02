_U='etpName'
_T='etpStatDirection'
_S='etpServiceIndex'
_R='etpPortIfIndex'
_Q='Unsigned32'
_P='alarmEventReason'
_O='alarmEventLogSourceName'
_N='alarmEventLogSeverity'
_M='alarmEventLogDescription'
_L='alarmEventLogDateAndTime'
_K='alarmEventLogAlarmOrEventId'
_J='ifAlias'
_I='IF-MIB'
_H='etpIdx'
_G='not-accessible'
_F='read-create'
_E='Integer32'
_D='RAD-Etp-MIB'
_C='RAD-GEN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifAlias=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
ethIf,=mibBuilder.importSymbols('RAD-EthIf-MIB','ethIf')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_C,_K,_L,_M,_N,_O,_P)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
etp=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,1,9))
_EtpEvents_ObjectIdentity=ObjectIdentity
etpEvents=_EtpEvents_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,9,0))
_EtpTable_Object=MibTable
etpTable=_EtpTable_Object((1,3,6,1,4,1,164,3,1,6,1,9,1))
if mibBuilder.loadTexts:etpTable.setStatus(_A)
_EtpEntry_Object=MibTableRow
etpEntry=_EtpEntry_Object((1,3,6,1,4,1,164,3,1,6,1,9,1,1))
etpEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:etpEntry.setStatus(_A)
class _EtpIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtpIdx_Type.__name__=_Q
_EtpIdx_Object=MibTableColumn
etpIdx=_EtpIdx_Object((1,3,6,1,4,1,164,3,1,6,1,9,1,1,1),_EtpIdx_Type())
etpIdx.setMaxAccess(_G)
if mibBuilder.loadTexts:etpIdx.setStatus(_A)
_EtpRowStatus_Type=RowStatus
_EtpRowStatus_Object=MibTableColumn
etpRowStatus=_EtpRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,9,1,1,2),_EtpRowStatus_Type())
etpRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etpRowStatus.setStatus(_A)
_EtpName_Type=SnmpAdminString
_EtpName_Object=MibTableColumn
etpName=_EtpName_Object((1,3,6,1,4,1,164,3,1,6,1,9,1,1,3),_EtpName_Type())
etpName.setMaxAccess(_F)
if mibBuilder.loadTexts:etpName.setStatus(_A)
class _EtpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_EtpOperStatus_Type.__name__=_E
_EtpOperStatus_Object=MibTableColumn
etpOperStatus=_EtpOperStatus_Object((1,3,6,1,4,1,164,3,1,6,1,9,1,1,4),_EtpOperStatus_Type())
etpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:etpOperStatus.setStatus(_A)
class _EtpClearStatCounters_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('on',3)))
_EtpClearStatCounters_Type.__name__=_E
_EtpClearStatCounters_Object=MibTableColumn
etpClearStatCounters=_EtpClearStatCounters_Object((1,3,6,1,4,1,164,3,1,6,1,9,1,1,5),_EtpClearStatCounters_Type())
etpClearStatCounters.setMaxAccess(_F)
if mibBuilder.loadTexts:etpClearStatCounters.setStatus(_A)
_EtpPortTable_Object=MibTable
etpPortTable=_EtpPortTable_Object((1,3,6,1,4,1,164,3,1,6,1,9,2))
if mibBuilder.loadTexts:etpPortTable.setStatus(_A)
_EtpPortEntry_Object=MibTableRow
etpPortEntry=_EtpPortEntry_Object((1,3,6,1,4,1,164,3,1,6,1,9,2,1))
etpPortEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:etpPortEntry.setStatus(_A)
_EtpPortIfIndex_Type=InterfaceIndex
_EtpPortIfIndex_Object=MibTableColumn
etpPortIfIndex=_EtpPortIfIndex_Object((1,3,6,1,4,1,164,3,1,6,1,9,2,1,1),_EtpPortIfIndex_Type())
etpPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:etpPortIfIndex.setStatus(_A)
_EtpPortRowStatus_Type=RowStatus
_EtpPortRowStatus_Object=MibTableColumn
etpPortRowStatus=_EtpPortRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,9,2,1,2),_EtpPortRowStatus_Type())
etpPortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etpPortRowStatus.setStatus(_A)
_EtpStatTable_Object=MibTable
etpStatTable=_EtpStatTable_Object((1,3,6,1,4,1,164,3,1,6,1,9,3))
if mibBuilder.loadTexts:etpStatTable.setStatus(_A)
_EtpStatEntry_Object=MibTableRow
etpStatEntry=_EtpStatEntry_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1))
etpStatEntry.setIndexNames((0,_D,_H),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:etpStatEntry.setStatus(_A)
_EtpServiceIndex_Type=Integer32
_EtpServiceIndex_Object=MibTableColumn
etpServiceIndex=_EtpServiceIndex_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,1),_EtpServiceIndex_Type())
etpServiceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:etpServiceIndex.setStatus(_A)
class _EtpStatDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('tx',1),('rx',2),('notApplicable',255)))
_EtpStatDirection_Type.__name__=_E
_EtpStatDirection_Object=MibTableColumn
etpStatDirection=_EtpStatDirection_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,2),_EtpStatDirection_Type())
etpStatDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:etpStatDirection.setStatus(_A)
_EtpForwardGreenPackets_Type=Counter32
_EtpForwardGreenPackets_Object=MibTableColumn
etpForwardGreenPackets=_EtpForwardGreenPackets_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,3),_EtpForwardGreenPackets_Type())
etpForwardGreenPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardGreenPackets.setStatus(_A)
_EtpForwardGreenPacketsOverflow_Type=Counter32
_EtpForwardGreenPacketsOverflow_Object=MibTableColumn
etpForwardGreenPacketsOverflow=_EtpForwardGreenPacketsOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,4),_EtpForwardGreenPacketsOverflow_Type())
etpForwardGreenPacketsOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardGreenPacketsOverflow.setStatus(_A)
_EtpForwardYellowPackets_Type=Counter32
_EtpForwardYellowPackets_Object=MibTableColumn
etpForwardYellowPackets=_EtpForwardYellowPackets_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,5),_EtpForwardYellowPackets_Type())
etpForwardYellowPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardYellowPackets.setStatus(_A)
_EtpForwardYellowPacketsOverflow_Type=Counter32
_EtpForwardYellowPacketsOverflow_Object=MibTableColumn
etpForwardYellowPacketsOverflow=_EtpForwardYellowPacketsOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,6),_EtpForwardYellowPacketsOverflow_Type())
etpForwardYellowPacketsOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardYellowPacketsOverflow.setStatus(_A)
_EtpDiscardGreenPackets_Type=Counter32
_EtpDiscardGreenPackets_Object=MibTableColumn
etpDiscardGreenPackets=_EtpDiscardGreenPackets_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,7),_EtpDiscardGreenPackets_Type())
etpDiscardGreenPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardGreenPackets.setStatus(_A)
_EtpDiscardGreenPacketsOverflow_Type=Counter32
_EtpDiscardGreenPacketsOverflow_Object=MibTableColumn
etpDiscardGreenPacketsOverflow=_EtpDiscardGreenPacketsOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,8),_EtpDiscardGreenPacketsOverflow_Type())
etpDiscardGreenPacketsOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardGreenPacketsOverflow.setStatus(_A)
_EtpDiscardYellowRedPackets_Type=Counter32
_EtpDiscardYellowRedPackets_Object=MibTableColumn
etpDiscardYellowRedPackets=_EtpDiscardYellowRedPackets_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,9),_EtpDiscardYellowRedPackets_Type())
etpDiscardYellowRedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardYellowRedPackets.setStatus(_A)
_EtpDiscardYellowRedPacketsOverflow_Type=Counter32
_EtpDiscardYellowRedPacketsOverflow_Object=MibTableColumn
etpDiscardYellowRedPacketsOverflow=_EtpDiscardYellowRedPacketsOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,10),_EtpDiscardYellowRedPacketsOverflow_Type())
etpDiscardYellowRedPacketsOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardYellowRedPacketsOverflow.setStatus(_A)
_EtpForwardGreenBytes_Type=Counter32
_EtpForwardGreenBytes_Object=MibTableColumn
etpForwardGreenBytes=_EtpForwardGreenBytes_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,11),_EtpForwardGreenBytes_Type())
etpForwardGreenBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardGreenBytes.setStatus(_A)
_EtpForwardGreenBytesOverflow_Type=Counter32
_EtpForwardGreenBytesOverflow_Object=MibTableColumn
etpForwardGreenBytesOverflow=_EtpForwardGreenBytesOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,12),_EtpForwardGreenBytesOverflow_Type())
etpForwardGreenBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardGreenBytesOverflow.setStatus(_A)
_EtpForwardYellowBytes_Type=Counter32
_EtpForwardYellowBytes_Object=MibTableColumn
etpForwardYellowBytes=_EtpForwardYellowBytes_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,13),_EtpForwardYellowBytes_Type())
etpForwardYellowBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardYellowBytes.setStatus(_A)
_EtpForwardYellowBytesOverflow_Type=Counter32
_EtpForwardYellowBytesOverflow_Object=MibTableColumn
etpForwardYellowBytesOverflow=_EtpForwardYellowBytesOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,14),_EtpForwardYellowBytesOverflow_Type())
etpForwardYellowBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpForwardYellowBytesOverflow.setStatus(_A)
_EtpDiscardGreenBytes_Type=Counter32
_EtpDiscardGreenBytes_Object=MibTableColumn
etpDiscardGreenBytes=_EtpDiscardGreenBytes_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,15),_EtpDiscardGreenBytes_Type())
etpDiscardGreenBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardGreenBytes.setStatus(_A)
_EtpDiscardGreenBytesOverflow_Type=Counter32
_EtpDiscardGreenBytesOverflow_Object=MibTableColumn
etpDiscardGreenBytesOverflow=_EtpDiscardGreenBytesOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,16),_EtpDiscardGreenBytesOverflow_Type())
etpDiscardGreenBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardGreenBytesOverflow.setStatus(_A)
_EtpDiscardYellowRedBytes_Type=Counter32
_EtpDiscardYellowRedBytes_Object=MibTableColumn
etpDiscardYellowRedBytes=_EtpDiscardYellowRedBytes_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,17),_EtpDiscardYellowRedBytes_Type())
etpDiscardYellowRedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardYellowRedBytes.setStatus(_A)
_EtpDiscardYellowRedBytesOverflow_Type=Counter32
_EtpDiscardYellowRedBytesOverflow_Object=MibTableColumn
etpDiscardYellowRedBytesOverflow=_EtpDiscardYellowRedBytesOverflow_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,18),_EtpDiscardYellowRedBytesOverflow_Type())
etpDiscardYellowRedBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:etpDiscardYellowRedBytesOverflow.setStatus(_A)
class _EtpStatClearCounters_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('on',3)))
_EtpStatClearCounters_Type.__name__=_E
_EtpStatClearCounters_Object=MibTableColumn
etpStatClearCounters=_EtpStatClearCounters_Object((1,3,6,1,4,1,164,3,1,6,1,9,3,1,19),_EtpStatClearCounters_Type())
etpStatClearCounters.setMaxAccess(_F)
if mibBuilder.loadTexts:etpStatClearCounters.setStatus(_A)
etpPortDown=NotificationType((1,3,6,1,4,1,164,3,1,6,1,9,0,1))
etpPortDown.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_I,_J),(_D,_U)))
if mibBuilder.loadTexts:etpPortDown.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'etp':etp,'etpEvents':etpEvents,'etpPortDown':etpPortDown,'etpTable':etpTable,'etpEntry':etpEntry,_H:etpIdx,'etpRowStatus':etpRowStatus,_U:etpName,'etpOperStatus':etpOperStatus,'etpClearStatCounters':etpClearStatCounters,'etpPortTable':etpPortTable,'etpPortEntry':etpPortEntry,_R:etpPortIfIndex,'etpPortRowStatus':etpPortRowStatus,'etpStatTable':etpStatTable,'etpStatEntry':etpStatEntry,_S:etpServiceIndex,_T:etpStatDirection,'etpForwardGreenPackets':etpForwardGreenPackets,'etpForwardGreenPacketsOverflow':etpForwardGreenPacketsOverflow,'etpForwardYellowPackets':etpForwardYellowPackets,'etpForwardYellowPacketsOverflow':etpForwardYellowPacketsOverflow,'etpDiscardGreenPackets':etpDiscardGreenPackets,'etpDiscardGreenPacketsOverflow':etpDiscardGreenPacketsOverflow,'etpDiscardYellowRedPackets':etpDiscardYellowRedPackets,'etpDiscardYellowRedPacketsOverflow':etpDiscardYellowRedPacketsOverflow,'etpForwardGreenBytes':etpForwardGreenBytes,'etpForwardGreenBytesOverflow':etpForwardGreenBytesOverflow,'etpForwardYellowBytes':etpForwardYellowBytes,'etpForwardYellowBytesOverflow':etpForwardYellowBytesOverflow,'etpDiscardGreenBytes':etpDiscardGreenBytes,'etpDiscardGreenBytesOverflow':etpDiscardGreenBytesOverflow,'etpDiscardYellowRedBytes':etpDiscardYellowRedBytes,'etpDiscardYellowRedBytesOverflow':etpDiscardYellowRedBytesOverflow,'etpStatClearCounters':etpStatClearCounters})