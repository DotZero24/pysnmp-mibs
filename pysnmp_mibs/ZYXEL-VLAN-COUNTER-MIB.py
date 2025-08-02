_G='zyVlanCounterInfoVid'
_F='read-write'
_E='not-accessible'
_D='zyVlanCounterVid'
_C='ZYXEL-VLAN-COUNTER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelVlanCounter=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,87))
_ZyxelVlanCounterSetup_ObjectIdentity=ObjectIdentity
zyxelVlanCounterSetup=_ZyxelVlanCounterSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,87,1))
_ZyxelVlanCounterTable_Object=MibTable
zyxelVlanCounterTable=_ZyxelVlanCounterTable_Object((1,3,6,1,4,1,890,1,15,3,87,1,1))
if mibBuilder.loadTexts:zyxelVlanCounterTable.setStatus(_A)
_ZyxelVlanCounterEntry_Object=MibTableRow
zyxelVlanCounterEntry=_ZyxelVlanCounterEntry_Object((1,3,6,1,4,1,890,1,15,3,87,1,1,1))
zyxelVlanCounterEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelVlanCounterEntry.setStatus(_A)
_ZyVlanCounterVid_Type=Integer32
_ZyVlanCounterVid_Object=MibTableColumn
zyVlanCounterVid=_ZyVlanCounterVid_Object((1,3,6,1,4,1,890,1,15,3,87,1,1,1,1),_ZyVlanCounterVid_Type())
zyVlanCounterVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyVlanCounterVid.setStatus(_A)
_ZyVlanCounterTimeout_Type=Unsigned32
_ZyVlanCounterTimeout_Object=MibTableColumn
zyVlanCounterTimeout=_ZyVlanCounterTimeout_Object((1,3,6,1,4,1,890,1,15,3,87,1,1,1,2),_ZyVlanCounterTimeout_Type())
zyVlanCounterTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:zyVlanCounterTimeout.setStatus(_A)
_ZyVlanCounterPorts_Type=PortList
_ZyVlanCounterPorts_Object=MibTableColumn
zyVlanCounterPorts=_ZyVlanCounterPorts_Object((1,3,6,1,4,1,890,1,15,3,87,1,1,1,3),_ZyVlanCounterPorts_Type())
zyVlanCounterPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:zyVlanCounterPorts.setStatus(_A)
_ZyVlanCounterRowStatus_Type=RowStatus
_ZyVlanCounterRowStatus_Object=MibTableColumn
zyVlanCounterRowStatus=_ZyVlanCounterRowStatus_Object((1,3,6,1,4,1,890,1,15,3,87,1,1,1,4),_ZyVlanCounterRowStatus_Type())
zyVlanCounterRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyVlanCounterRowStatus.setStatus(_A)
_ZyxelVlanCounterStatus_ObjectIdentity=ObjectIdentity
zyxelVlanCounterStatus=_ZyxelVlanCounterStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,87,2))
_ZyxelVlanCounterInfoTable_Object=MibTable
zyxelVlanCounterInfoTable=_ZyxelVlanCounterInfoTable_Object((1,3,6,1,4,1,890,1,15,3,87,2,1))
if mibBuilder.loadTexts:zyxelVlanCounterInfoTable.setStatus(_A)
_ZyxelVlanCounterInfoEntry_Object=MibTableRow
zyxelVlanCounterInfoEntry=_ZyxelVlanCounterInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1))
zyxelVlanCounterInfoEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:zyxelVlanCounterInfoEntry.setStatus(_A)
_ZyVlanCounterInfoVid_Type=Integer32
_ZyVlanCounterInfoVid_Object=MibTableColumn
zyVlanCounterInfoVid=_ZyVlanCounterInfoVid_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,1),_ZyVlanCounterInfoVid_Type())
zyVlanCounterInfoVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyVlanCounterInfoVid.setStatus(_A)
_ZyVlanCounterInfoHCOctets_Type=Counter64
_ZyVlanCounterInfoHCOctets_Object=MibTableColumn
zyVlanCounterInfoHCOctets=_ZyVlanCounterInfoHCOctets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,2),_ZyVlanCounterInfoHCOctets_Type())
zyVlanCounterInfoHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCOctets.setStatus(_A)
if mibBuilder.loadTexts:zyVlanCounterInfoHCOctets.setUnits('Octets')
_ZyVlanCounterInfoHCPackets_Type=Counter64
_ZyVlanCounterInfoHCPackets_Object=MibTableColumn
zyVlanCounterInfoHCPackets=_ZyVlanCounterInfoHCPackets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,3),_ZyVlanCounterInfoHCPackets_Type())
zyVlanCounterInfoHCPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCPackets.setStatus(_A)
_ZyVlanCounterInfoHCMulticastPackets_Type=Counter64
_ZyVlanCounterInfoHCMulticastPackets_Object=MibTableColumn
zyVlanCounterInfoHCMulticastPackets=_ZyVlanCounterInfoHCMulticastPackets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,4),_ZyVlanCounterInfoHCMulticastPackets_Type())
zyVlanCounterInfoHCMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCMulticastPackets.setStatus(_A)
_ZyVlanCounterInfoHCBroadcastPackets_Type=Counter64
_ZyVlanCounterInfoHCBroadcastPackets_Object=MibTableColumn
zyVlanCounterInfoHCBroadcastPackets=_ZyVlanCounterInfoHCBroadcastPackets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,5),_ZyVlanCounterInfoHCBroadcastPackets_Type())
zyVlanCounterInfoHCBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCBroadcastPackets.setStatus(_A)
_ZyVlanCounterInfoHCTaggedPackets_Type=Counter64
_ZyVlanCounterInfoHCTaggedPackets_Object=MibTableColumn
zyVlanCounterInfoHCTaggedPackets=_ZyVlanCounterInfoHCTaggedPackets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,6),_ZyVlanCounterInfoHCTaggedPackets_Type())
zyVlanCounterInfoHCTaggedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCTaggedPackets.setStatus(_A)
_ZyVlanCounterInfoHCPackets64Octets_Type=Counter64
_ZyVlanCounterInfoHCPackets64Octets_Object=MibTableColumn
zyVlanCounterInfoHCPackets64Octets=_ZyVlanCounterInfoHCPackets64Octets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,7),_ZyVlanCounterInfoHCPackets64Octets_Type())
zyVlanCounterInfoHCPackets64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCPackets64Octets.setStatus(_A)
_ZyVlanCounterInfoHCPackets65to127Octets_Type=Counter64
_ZyVlanCounterInfoHCPackets65to127Octets_Object=MibTableColumn
zyVlanCounterInfoHCPackets65to127Octets=_ZyVlanCounterInfoHCPackets65to127Octets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,8),_ZyVlanCounterInfoHCPackets65to127Octets_Type())
zyVlanCounterInfoHCPackets65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCPackets65to127Octets.setStatus(_A)
_ZyVlanCounterInfoHCPackets128to255Octets_Type=Counter64
_ZyVlanCounterInfoHCPackets128to255Octets_Object=MibTableColumn
zyVlanCounterInfoHCPackets128to255Octets=_ZyVlanCounterInfoHCPackets128to255Octets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,9),_ZyVlanCounterInfoHCPackets128to255Octets_Type())
zyVlanCounterInfoHCPackets128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCPackets128to255Octets.setStatus(_A)
_ZyVlanCounterInfoHCPackets256to511Octets_Type=Counter64
_ZyVlanCounterInfoHCPackets256to511Octets_Object=MibTableColumn
zyVlanCounterInfoHCPackets256to511Octets=_ZyVlanCounterInfoHCPackets256to511Octets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,10),_ZyVlanCounterInfoHCPackets256to511Octets_Type())
zyVlanCounterInfoHCPackets256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCPackets256to511Octets.setStatus(_A)
_ZyVlanCounterInfoHCPackets512to1023Octets_Type=Counter64
_ZyVlanCounterInfoHCPackets512to1023Octets_Object=MibTableColumn
zyVlanCounterInfoHCPackets512to1023Octets=_ZyVlanCounterInfoHCPackets512to1023Octets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,11),_ZyVlanCounterInfoHCPackets512to1023Octets_Type())
zyVlanCounterInfoHCPackets512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCPackets512to1023Octets.setStatus(_A)
_ZyVlanCounterInfoHCPackets1024to1518Octets_Type=Counter64
_ZyVlanCounterInfoHCPackets1024to1518Octets_Object=MibTableColumn
zyVlanCounterInfoHCPackets1024to1518Octets=_ZyVlanCounterInfoHCPackets1024to1518Octets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,12),_ZyVlanCounterInfoHCPackets1024to1518Octets_Type())
zyVlanCounterInfoHCPackets1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCPackets1024to1518Octets.setStatus(_A)
_ZyVlanCounterInfoHCOversizePackets_Type=Counter64
_ZyVlanCounterInfoHCOversizePackets_Object=MibTableColumn
zyVlanCounterInfoHCOversizePackets=_ZyVlanCounterInfoHCOversizePackets_Object((1,3,6,1,4,1,890,1,15,3,87,2,1,1,13),_ZyVlanCounterInfoHCOversizePackets_Type())
zyVlanCounterInfoHCOversizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanCounterInfoHCOversizePackets.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelVlanCounter':zyxelVlanCounter,'zyxelVlanCounterSetup':zyxelVlanCounterSetup,'zyxelVlanCounterTable':zyxelVlanCounterTable,'zyxelVlanCounterEntry':zyxelVlanCounterEntry,_D:zyVlanCounterVid,'zyVlanCounterTimeout':zyVlanCounterTimeout,'zyVlanCounterPorts':zyVlanCounterPorts,'zyVlanCounterRowStatus':zyVlanCounterRowStatus,'zyxelVlanCounterStatus':zyxelVlanCounterStatus,'zyxelVlanCounterInfoTable':zyxelVlanCounterInfoTable,'zyxelVlanCounterInfoEntry':zyxelVlanCounterInfoEntry,_G:zyVlanCounterInfoVid,'zyVlanCounterInfoHCOctets':zyVlanCounterInfoHCOctets,'zyVlanCounterInfoHCPackets':zyVlanCounterInfoHCPackets,'zyVlanCounterInfoHCMulticastPackets':zyVlanCounterInfoHCMulticastPackets,'zyVlanCounterInfoHCBroadcastPackets':zyVlanCounterInfoHCBroadcastPackets,'zyVlanCounterInfoHCTaggedPackets':zyVlanCounterInfoHCTaggedPackets,'zyVlanCounterInfoHCPackets64Octets':zyVlanCounterInfoHCPackets64Octets,'zyVlanCounterInfoHCPackets65to127Octets':zyVlanCounterInfoHCPackets65to127Octets,'zyVlanCounterInfoHCPackets128to255Octets':zyVlanCounterInfoHCPackets128to255Octets,'zyVlanCounterInfoHCPackets256to511Octets':zyVlanCounterInfoHCPackets256to511Octets,'zyVlanCounterInfoHCPackets512to1023Octets':zyVlanCounterInfoHCPackets512to1023Octets,'zyVlanCounterInfoHCPackets1024to1518Octets':zyVlanCounterInfoHCPackets1024to1518Octets,'zyVlanCounterInfoHCOversizePackets':zyVlanCounterInfoHCOversizePackets})