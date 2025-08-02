_M='rcIgmpSnoopStaticMulticastAddress'
_L='rcIgmpSnoopMrouterPort'
_K='rcIgmpSnoopMrouterVlan'
_J='EnableVar'
_I='dot1qStaticMulticastReceivePort'
_H='dot1qStaticMulticastAddress'
_G='not-accessible'
_F='Integer32'
_E='dot1qVlanIndex'
_D='SWITCH-IGMPSNOOP-MIB'
_C='Q-BRIDGE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1qStaticMulticastAddress,dot1qStaticMulticastReceivePort,dot1qVlanIndex=mibBuilder.importSymbols(_C,_H,_I,_E)
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,PortList,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_J,'PortList','Vlanset')
rcIgmpSnoop=ModuleIdentity((1,3,6,1,4,1,8886,6,1,11))
if mibBuilder.loadTexts:rcIgmpSnoop.setRevisions(('1904-12-20 00:00',))
class _RcIgmpSnoopEnable_Type(EnableVar):defaultValue=1
_RcIgmpSnoopEnable_Type.__name__=_J
_RcIgmpSnoopEnable_Object=MibScalar
rcIgmpSnoopEnable=_RcIgmpSnoopEnable_Object((1,3,6,1,4,1,8886,6,1,11,1),_RcIgmpSnoopEnable_Type())
rcIgmpSnoopEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopEnable.setStatus(_A)
_RcIgmpSnoopAlerts_Type=TruthValue
_RcIgmpSnoopAlerts_Object=MibScalar
rcIgmpSnoopAlerts=_RcIgmpSnoopAlerts_Object((1,3,6,1,4,1,8886,6,1,11,2),_RcIgmpSnoopAlerts_Type())
rcIgmpSnoopAlerts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopAlerts.setStatus(_A)
class _RcIgmpSnoopAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,3600))
_RcIgmpSnoopAging_Type.__name__=_F
_RcIgmpSnoopAging_Object=MibScalar
rcIgmpSnoopAging=_RcIgmpSnoopAging_Object((1,3,6,1,4,1,8886,6,1,11,3),_RcIgmpSnoopAging_Type())
rcIgmpSnoopAging.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopAging.setStatus(_A)
if mibBuilder.loadTexts:rcIgmpSnoopAging.setUnits('second')
_RcIgmpSnoopVlan_Type=Vlanset
_RcIgmpSnoopVlan_Object=MibScalar
rcIgmpSnoopVlan=_RcIgmpSnoopVlan_Object((1,3,6,1,4,1,8886,6,1,11,4),_RcIgmpSnoopVlan_Type())
rcIgmpSnoopVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopVlan.setStatus(_A)
_RcIgmpSnoopLeave_Type=Vlanset
_RcIgmpSnoopLeave_Object=MibScalar
rcIgmpSnoopLeave=_RcIgmpSnoopLeave_Object((1,3,6,1,4,1,8886,6,1,11,5),_RcIgmpSnoopLeave_Type())
rcIgmpSnoopLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopLeave.setStatus(_A)
_RcIgmpSnoopFilter_Type=TruthValue
_RcIgmpSnoopFilter_Object=MibScalar
rcIgmpSnoopFilter=_RcIgmpSnoopFilter_Object((1,3,6,1,4,1,8886,6,1,11,6),_RcIgmpSnoopFilter_Type())
rcIgmpSnoopFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopFilter.setStatus(_A)
_RcIgmpSnoopTable_Object=MibTable
rcIgmpSnoopTable=_RcIgmpSnoopTable_Object((1,3,6,1,4,1,8886,6,1,11,7))
if mibBuilder.loadTexts:rcIgmpSnoopTable.setStatus(_A)
_RcIgmpSnoopEntry_Object=MibTableRow
rcIgmpSnoopEntry=_RcIgmpSnoopEntry_Object((1,3,6,1,4,1,8886,6,1,11,7,1))
rcIgmpSnoopEntry.setIndexNames((0,_C,_E),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:rcIgmpSnoopEntry.setStatus(_A)
_RcIgmpSnoopEgressPorts_Type=PortList
_RcIgmpSnoopEgressPorts_Object=MibTableColumn
rcIgmpSnoopEgressPorts=_RcIgmpSnoopEgressPorts_Object((1,3,6,1,4,1,8886,6,1,11,7,1,1),_RcIgmpSnoopEgressPorts_Type())
rcIgmpSnoopEgressPorts.setMaxAccess('read-only')
if mibBuilder.loadTexts:rcIgmpSnoopEgressPorts.setStatus(_A)
_RcIgmpSnoopMrouterTable_Object=MibTable
rcIgmpSnoopMrouterTable=_RcIgmpSnoopMrouterTable_Object((1,3,6,1,4,1,8886,6,1,11,8))
if mibBuilder.loadTexts:rcIgmpSnoopMrouterTable.setStatus(_A)
_RcIgmpSnoopMrouterEntry_Object=MibTableRow
rcIgmpSnoopMrouterEntry=_RcIgmpSnoopMrouterEntry_Object((1,3,6,1,4,1,8886,6,1,11,8,1))
rcIgmpSnoopMrouterEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:rcIgmpSnoopMrouterEntry.setStatus(_A)
_RcIgmpSnoopMrouterVlan_Type=Integer32
_RcIgmpSnoopMrouterVlan_Object=MibTableColumn
rcIgmpSnoopMrouterVlan=_RcIgmpSnoopMrouterVlan_Object((1,3,6,1,4,1,8886,6,1,11,8,1,1),_RcIgmpSnoopMrouterVlan_Type())
rcIgmpSnoopMrouterVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:rcIgmpSnoopMrouterVlan.setStatus(_A)
_RcIgmpSnoopMrouterPort_Type=Integer32
_RcIgmpSnoopMrouterPort_Object=MibTableColumn
rcIgmpSnoopMrouterPort=_RcIgmpSnoopMrouterPort_Object((1,3,6,1,4,1,8886,6,1,11,8,1,2),_RcIgmpSnoopMrouterPort_Type())
rcIgmpSnoopMrouterPort.setMaxAccess(_G)
if mibBuilder.loadTexts:rcIgmpSnoopMrouterPort.setStatus(_A)
_RcIgmpSnoopMrouterStatus_Type=RowStatus
_RcIgmpSnoopMrouterStatus_Object=MibTableColumn
rcIgmpSnoopMrouterStatus=_RcIgmpSnoopMrouterStatus_Object((1,3,6,1,4,1,8886,6,1,11,8,1,3),_RcIgmpSnoopMrouterStatus_Type())
rcIgmpSnoopMrouterStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rcIgmpSnoopMrouterStatus.setStatus(_A)
_RcIgmpSnoopStaticMulticastTable_Object=MibTable
rcIgmpSnoopStaticMulticastTable=_RcIgmpSnoopStaticMulticastTable_Object((1,3,6,1,4,1,8886,6,1,11,9))
if mibBuilder.loadTexts:rcIgmpSnoopStaticMulticastTable.setStatus(_A)
_RcIgmpSnoopStaticMulticastEntry_Object=MibTableRow
rcIgmpSnoopStaticMulticastEntry=_RcIgmpSnoopStaticMulticastEntry_Object((1,3,6,1,4,1,8886,6,1,11,9,1))
rcIgmpSnoopStaticMulticastEntry.setIndexNames((0,_C,_E),(0,_D,_M))
if mibBuilder.loadTexts:rcIgmpSnoopStaticMulticastEntry.setStatus(_A)
_RcIgmpSnoopStaticMulticastAddress_Type=IpAddress
_RcIgmpSnoopStaticMulticastAddress_Object=MibTableColumn
rcIgmpSnoopStaticMulticastAddress=_RcIgmpSnoopStaticMulticastAddress_Object((1,3,6,1,4,1,8886,6,1,11,9,1,1),_RcIgmpSnoopStaticMulticastAddress_Type())
rcIgmpSnoopStaticMulticastAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rcIgmpSnoopStaticMulticastAddress.setStatus(_A)
_RcIgmpSnoopStaticMulticastStaticEgressPorts_Type=PortList
_RcIgmpSnoopStaticMulticastStaticEgressPorts_Object=MibTableColumn
rcIgmpSnoopStaticMulticastStaticEgressPorts=_RcIgmpSnoopStaticMulticastStaticEgressPorts_Object((1,3,6,1,4,1,8886,6,1,11,9,1,2),_RcIgmpSnoopStaticMulticastStaticEgressPorts_Type())
rcIgmpSnoopStaticMulticastStaticEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopStaticMulticastStaticEgressPorts.setStatus(_A)
class _RcIgmpSnoopStaticMulticastStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('permanent',3),('deleteOnReset',4),('deleteOnTimeout',5)))
_RcIgmpSnoopStaticMulticastStatus_Type.__name__=_F
_RcIgmpSnoopStaticMulticastStatus_Object=MibTableColumn
rcIgmpSnoopStaticMulticastStatus=_RcIgmpSnoopStaticMulticastStatus_Object((1,3,6,1,4,1,8886,6,1,11,9,1,3),_RcIgmpSnoopStaticMulticastStatus_Type())
rcIgmpSnoopStaticMulticastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIgmpSnoopStaticMulticastStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rcIgmpSnoop':rcIgmpSnoop,'rcIgmpSnoopEnable':rcIgmpSnoopEnable,'rcIgmpSnoopAlerts':rcIgmpSnoopAlerts,'rcIgmpSnoopAging':rcIgmpSnoopAging,'rcIgmpSnoopVlan':rcIgmpSnoopVlan,'rcIgmpSnoopLeave':rcIgmpSnoopLeave,'rcIgmpSnoopFilter':rcIgmpSnoopFilter,'rcIgmpSnoopTable':rcIgmpSnoopTable,'rcIgmpSnoopEntry':rcIgmpSnoopEntry,'rcIgmpSnoopEgressPorts':rcIgmpSnoopEgressPorts,'rcIgmpSnoopMrouterTable':rcIgmpSnoopMrouterTable,'rcIgmpSnoopMrouterEntry':rcIgmpSnoopMrouterEntry,_K:rcIgmpSnoopMrouterVlan,_L:rcIgmpSnoopMrouterPort,'rcIgmpSnoopMrouterStatus':rcIgmpSnoopMrouterStatus,'rcIgmpSnoopStaticMulticastTable':rcIgmpSnoopStaticMulticastTable,'rcIgmpSnoopStaticMulticastEntry':rcIgmpSnoopStaticMulticastEntry,_M:rcIgmpSnoopStaticMulticastAddress,'rcIgmpSnoopStaticMulticastStaticEgressPorts':rcIgmpSnoopStaticMulticastStaticEgressPorts,'rcIgmpSnoopStaticMulticastStatus':rcIgmpSnoopStaticMulticastStatus})