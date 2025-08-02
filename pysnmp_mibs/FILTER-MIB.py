_N='swFilterDetectedport'
_M='swFilterDetectedIP'
_L='accessible-for-notify'
_K='swFilterDhcpPortIndex'
_J='read-create'
_I='swFilterDhcpClientMac'
_H='swFilterDhcpServerIP'
_G='read-only'
_F='disabled'
_E='enabled'
_D='read-write'
_C='FILTER-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swFilterMIB=ModuleIdentity((1,3,6,1,4,1,171,12,37))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwFilterDhcp_ObjectIdentity=ObjectIdentity
swFilterDhcp=_SwFilterDhcp_ObjectIdentity((1,3,6,1,4,1,171,12,37,1))
_SwFilterDhcpPermitTable_Object=MibTable
swFilterDhcpPermitTable=_SwFilterDhcpPermitTable_Object((1,3,6,1,4,1,171,12,37,1,1))
if mibBuilder.loadTexts:swFilterDhcpPermitTable.setStatus(_A)
_SwFilterDhcpPermitEntry_Object=MibTableRow
swFilterDhcpPermitEntry=_SwFilterDhcpPermitEntry_Object((1,3,6,1,4,1,171,12,37,1,1,1))
swFilterDhcpPermitEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:swFilterDhcpPermitEntry.setStatus(_A)
_SwFilterDhcpServerIP_Type=IpAddress
_SwFilterDhcpServerIP_Object=MibTableColumn
swFilterDhcpServerIP=_SwFilterDhcpServerIP_Object((1,3,6,1,4,1,171,12,37,1,1,1,1),_SwFilterDhcpServerIP_Type())
swFilterDhcpServerIP.setMaxAccess(_G)
if mibBuilder.loadTexts:swFilterDhcpServerIP.setStatus(_A)
_SwFilterDhcpClientMac_Type=MacAddress
_SwFilterDhcpClientMac_Object=MibTableColumn
swFilterDhcpClientMac=_SwFilterDhcpClientMac_Object((1,3,6,1,4,1,171,12,37,1,1,1,2),_SwFilterDhcpClientMac_Type())
swFilterDhcpClientMac.setMaxAccess(_G)
if mibBuilder.loadTexts:swFilterDhcpClientMac.setStatus(_A)
_SwFilterDhcpPorts_Type=PortList
_SwFilterDhcpPorts_Object=MibTableColumn
swFilterDhcpPorts=_SwFilterDhcpPorts_Object((1,3,6,1,4,1,171,12,37,1,1,1,3),_SwFilterDhcpPorts_Type())
swFilterDhcpPorts.setMaxAccess(_J)
if mibBuilder.loadTexts:swFilterDhcpPorts.setStatus(_A)
_SwFilterDhcpStatus_Type=RowStatus
_SwFilterDhcpStatus_Object=MibTableColumn
swFilterDhcpStatus=_SwFilterDhcpStatus_Object((1,3,6,1,4,1,171,12,37,1,1,1,4),_SwFilterDhcpStatus_Type())
swFilterDhcpStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swFilterDhcpStatus.setStatus(_A)
_SwFilterDhcpPortTable_Object=MibTable
swFilterDhcpPortTable=_SwFilterDhcpPortTable_Object((1,3,6,1,4,1,171,12,37,1,2))
if mibBuilder.loadTexts:swFilterDhcpPortTable.setStatus(_A)
_SwFilterDhcpPortEntry_Object=MibTableRow
swFilterDhcpPortEntry=_SwFilterDhcpPortEntry_Object((1,3,6,1,4,1,171,12,37,1,2,1))
swFilterDhcpPortEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:swFilterDhcpPortEntry.setStatus(_A)
class _SwFilterDhcpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwFilterDhcpPortIndex_Type.__name__=_B
_SwFilterDhcpPortIndex_Object=MibTableColumn
swFilterDhcpPortIndex=_SwFilterDhcpPortIndex_Object((1,3,6,1,4,1,171,12,37,1,2,1,1),_SwFilterDhcpPortIndex_Type())
swFilterDhcpPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:swFilterDhcpPortIndex.setStatus(_A)
class _SwFilterDhcpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwFilterDhcpPortState_Type.__name__=_B
_SwFilterDhcpPortState_Object=MibTableColumn
swFilterDhcpPortState=_SwFilterDhcpPortState_Object((1,3,6,1,4,1,171,12,37,1,2,1,2),_SwFilterDhcpPortState_Type())
swFilterDhcpPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swFilterDhcpPortState.setStatus(_A)
class _SwFilterDhcpServerIllegalSerLogSuppressDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('duration-1min',1),('duration-5min',2),('duration-30min',3)))
_SwFilterDhcpServerIllegalSerLogSuppressDuration_Type.__name__=_B
_SwFilterDhcpServerIllegalSerLogSuppressDuration_Object=MibScalar
swFilterDhcpServerIllegalSerLogSuppressDuration=_SwFilterDhcpServerIllegalSerLogSuppressDuration_Object((1,3,6,1,4,1,171,12,37,1,3),_SwFilterDhcpServerIllegalSerLogSuppressDuration_Type())
swFilterDhcpServerIllegalSerLogSuppressDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:swFilterDhcpServerIllegalSerLogSuppressDuration.setStatus(_A)
class _SwFilterDhcpServerTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwFilterDhcpServerTrapLogState_Type.__name__=_B
_SwFilterDhcpServerTrapLogState_Object=MibScalar
swFilterDhcpServerTrapLogState=_SwFilterDhcpServerTrapLogState_Object((1,3,6,1,4,1,171,12,37,1,4),_SwFilterDhcpServerTrapLogState_Type())
swFilterDhcpServerTrapLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swFilterDhcpServerTrapLogState.setStatus(_A)
class _SwFilterDhcpServerTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwFilterDhcpServerTrapState_Type.__name__=_B
_SwFilterDhcpServerTrapState_Object=MibScalar
swFilterDhcpServerTrapState=_SwFilterDhcpServerTrapState_Object((1,3,6,1,4,1,171,12,37,1,5),_SwFilterDhcpServerTrapState_Type())
swFilterDhcpServerTrapState.setMaxAccess(_D)
if mibBuilder.loadTexts:swFilterDhcpServerTrapState.setStatus(_A)
class _SwFilterDhcpServerLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwFilterDhcpServerLogState_Type.__name__=_B
_SwFilterDhcpServerLogState_Object=MibScalar
swFilterDhcpServerLogState=_SwFilterDhcpServerLogState_Object((1,3,6,1,4,1,171,12,37,1,6),_SwFilterDhcpServerLogState_Type())
swFilterDhcpServerLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swFilterDhcpServerLogState.setStatus(_A)
_SwFilterNotify_ObjectIdentity=ObjectIdentity
swFilterNotify=_SwFilterNotify_ObjectIdentity((1,3,6,1,4,1,171,12,37,100))
_SwFilterNotifyPrefix_ObjectIdentity=ObjectIdentity
swFilterNotifyPrefix=_SwFilterNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,37,100,0))
_SwFilterNotificationBindings_ObjectIdentity=ObjectIdentity
swFilterNotificationBindings=_SwFilterNotificationBindings_ObjectIdentity((1,3,6,1,4,1,171,12,37,100,2))
_SwFilterDetectedIP_Type=IpAddress
_SwFilterDetectedIP_Object=MibScalar
swFilterDetectedIP=_SwFilterDetectedIP_Object((1,3,6,1,4,1,171,12,37,100,2,1),_SwFilterDetectedIP_Type())
swFilterDetectedIP.setMaxAccess(_L)
if mibBuilder.loadTexts:swFilterDetectedIP.setStatus(_A)
_SwFilterDetectedport_Type=Integer32
_SwFilterDetectedport_Object=MibScalar
swFilterDetectedport=_SwFilterDetectedport_Object((1,3,6,1,4,1,171,12,37,100,2,2),_SwFilterDetectedport_Type())
swFilterDetectedport.setMaxAccess(_L)
if mibBuilder.loadTexts:swFilterDetectedport.setStatus(_A)
swFilterDetectedTrap=NotificationType((1,3,6,1,4,1,171,12,37,100,0,1))
swFilterDetectedTrap.setObjects(*((_C,_M),(_C,_N)))
if mibBuilder.loadTexts:swFilterDetectedTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PortList':PortList,'swFilterMIB':swFilterMIB,'swFilterDhcp':swFilterDhcp,'swFilterDhcpPermitTable':swFilterDhcpPermitTable,'swFilterDhcpPermitEntry':swFilterDhcpPermitEntry,_H:swFilterDhcpServerIP,_I:swFilterDhcpClientMac,'swFilterDhcpPorts':swFilterDhcpPorts,'swFilterDhcpStatus':swFilterDhcpStatus,'swFilterDhcpPortTable':swFilterDhcpPortTable,'swFilterDhcpPortEntry':swFilterDhcpPortEntry,_K:swFilterDhcpPortIndex,'swFilterDhcpPortState':swFilterDhcpPortState,'swFilterDhcpServerIllegalSerLogSuppressDuration':swFilterDhcpServerIllegalSerLogSuppressDuration,'swFilterDhcpServerTrapLogState':swFilterDhcpServerTrapLogState,'swFilterDhcpServerTrapState':swFilterDhcpServerTrapState,'swFilterDhcpServerLogState':swFilterDhcpServerLogState,'swFilterNotify':swFilterNotify,'swFilterNotifyPrefix':swFilterNotifyPrefix,'swFilterDetectedTrap':swFilterDetectedTrap,'swFilterNotificationBindings':swFilterNotificationBindings,_M:swFilterDetectedIP,_N:swFilterDetectedport})