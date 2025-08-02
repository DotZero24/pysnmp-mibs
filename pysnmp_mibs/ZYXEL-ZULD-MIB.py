_H='ifIndex'
_G='IF-MIB'
_F='dot1dBasePort'
_E='BRIDGE-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_E,_F)
ifIndex,=mibBuilder.importSymbols(_G,_H)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelZuld=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,110))
_ZyxelZuldSetup_ObjectIdentity=ObjectIdentity
zyxelZuldSetup=_ZyxelZuldSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,110,1))
_ZyZuldState_Type=EnabledStatus
_ZyZuldState_Object=MibScalar
zyZuldState=_ZyZuldState_Object((1,3,6,1,4,1,890,1,15,3,110,1,1),_ZyZuldState_Type())
zyZuldState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyZuldState.setStatus(_A)
_ZyxelZuldPortTable_Object=MibTable
zyxelZuldPortTable=_ZyxelZuldPortTable_Object((1,3,6,1,4,1,890,1,15,3,110,1,2))
if mibBuilder.loadTexts:zyxelZuldPortTable.setStatus(_A)
_ZyxelZuldPortEntry_Object=MibTableRow
zyxelZuldPortEntry=_ZyxelZuldPortEntry_Object((1,3,6,1,4,1,890,1,15,3,110,1,2,1))
zyxelZuldPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelZuldPortEntry.setStatus(_A)
_ZyZuldPortState_Type=EnabledStatus
_ZyZuldPortState_Object=MibTableColumn
zyZuldPortState=_ZyZuldPortState_Object((1,3,6,1,4,1,890,1,15,3,110,1,2,1,1),_ZyZuldPortState_Type())
zyZuldPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyZuldPortState.setStatus(_A)
class _ZyZuldPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('aggressive',2)))
_ZyZuldPortMode_Type.__name__=_B
_ZyZuldPortMode_Object=MibTableColumn
zyZuldPortMode=_ZyZuldPortMode_Object((1,3,6,1,4,1,890,1,15,3,110,1,2,1,2),_ZyZuldPortMode_Type())
zyZuldPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zyZuldPortMode.setStatus(_A)
class _ZyZuldPortProbeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,65534))
_ZyZuldPortProbeTime_Type.__name__=_B
_ZyZuldPortProbeTime_Object=MibTableColumn
zyZuldPortProbeTime=_ZyZuldPortProbeTime_Object((1,3,6,1,4,1,890,1,15,3,110,1,2,1,3),_ZyZuldPortProbeTime_Type())
zyZuldPortProbeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zyZuldPortProbeTime.setStatus(_A)
_ZyxelZuldStatus_ObjectIdentity=ObjectIdentity
zyxelZuldStatus=_ZyxelZuldStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,110,2))
_ZyxelZuldPortStatusTable_Object=MibTable
zyxelZuldPortStatusTable=_ZyxelZuldPortStatusTable_Object((1,3,6,1,4,1,890,1,15,3,110,2,1))
if mibBuilder.loadTexts:zyxelZuldPortStatusTable.setStatus(_A)
_ZyxelZuldPortStatusEntry_Object=MibTableRow
zyxelZuldPortStatusEntry=_ZyxelZuldPortStatusEntry_Object((1,3,6,1,4,1,890,1,15,3,110,2,1,1))
zyxelZuldPortStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelZuldPortStatusEntry.setStatus(_A)
class _ZyZuldPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('linkdwon',1),('probe',2),('unidirectional',3),('bidirectional',4),('shutdown',5)))
_ZyZuldPortLinkState_Type.__name__=_B
_ZyZuldPortLinkState_Object=MibTableColumn
zyZuldPortLinkState=_ZyZuldPortLinkState_Object((1,3,6,1,4,1,890,1,15,3,110,2,1,1,1),_ZyZuldPortLinkState_Type())
zyZuldPortLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyZuldPortLinkState.setStatus(_A)
_ZyZuldPortRemoteMACAddress_Type=MacAddress
_ZyZuldPortRemoteMACAddress_Object=MibTableColumn
zyZuldPortRemoteMACAddress=_ZyZuldPortRemoteMACAddress_Object((1,3,6,1,4,1,890,1,15,3,110,2,1,1,2),_ZyZuldPortRemoteMACAddress_Type())
zyZuldPortRemoteMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyZuldPortRemoteMACAddress.setStatus(_A)
_ZyZuldPortRemotePort_Type=Integer32
_ZyZuldPortRemotePort_Object=MibTableColumn
zyZuldPortRemotePort=_ZyZuldPortRemotePort_Object((1,3,6,1,4,1,890,1,15,3,110,2,1,1,3),_ZyZuldPortRemotePort_Type())
zyZuldPortRemotePort.setMaxAccess(_D)
if mibBuilder.loadTexts:zyZuldPortRemotePort.setStatus(_A)
_ZyZuldPortRemoteOperation_Type=EnabledStatus
_ZyZuldPortRemoteOperation_Object=MibTableColumn
zyZuldPortRemoteOperation=_ZyZuldPortRemoteOperation_Object((1,3,6,1,4,1,890,1,15,3,110,2,1,1,4),_ZyZuldPortRemoteOperation_Type())
zyZuldPortRemoteOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:zyZuldPortRemoteOperation.setStatus(_A)
_ZyxelZuldTrapNotifications_ObjectIdentity=ObjectIdentity
zyxelZuldTrapNotifications=_ZyxelZuldTrapNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,110,3))
zyZuldUnidirectionalDetected=NotificationType((1,3,6,1,4,1,890,1,15,3,110,3,1))
zyZuldUnidirectionalDetected.setObjects((_G,_H))
if mibBuilder.loadTexts:zyZuldUnidirectionalDetected.setStatus(_A)
zyZuldBidirectionalRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,110,3,2))
zyZuldBidirectionalRecovered.setObjects((_G,_H))
if mibBuilder.loadTexts:zyZuldBidirectionalRecovered.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-ZULD-MIB',**{'zyxelZuld':zyxelZuld,'zyxelZuldSetup':zyxelZuldSetup,'zyZuldState':zyZuldState,'zyxelZuldPortTable':zyxelZuldPortTable,'zyxelZuldPortEntry':zyxelZuldPortEntry,'zyZuldPortState':zyZuldPortState,'zyZuldPortMode':zyZuldPortMode,'zyZuldPortProbeTime':zyZuldPortProbeTime,'zyxelZuldStatus':zyxelZuldStatus,'zyxelZuldPortStatusTable':zyxelZuldPortStatusTable,'zyxelZuldPortStatusEntry':zyxelZuldPortStatusEntry,'zyZuldPortLinkState':zyZuldPortLinkState,'zyZuldPortRemoteMACAddress':zyZuldPortRemoteMACAddress,'zyZuldPortRemotePort':zyZuldPortRemotePort,'zyZuldPortRemoteOperation':zyZuldPortRemoteOperation,'zyxelZuldTrapNotifications':zyxelZuldTrapNotifications,'zyZuldUnidirectionalDetected':zyZuldUnidirectionalDetected,'zyZuldBidirectionalRecovered':zyZuldBidirectionalRecovered})