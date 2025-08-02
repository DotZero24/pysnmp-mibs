_H='nmsipsourceBindingsIpAddress'
_G='nmsBindingsIpAddress'
_F='Integer32'
_E='FS-NMS-DHCP-SNOOPING-MIB'
_D='mandatory'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmslocal,=mibBuilder.importSymbols('FS-NMS-SMI','nmslocal')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
_Dhcpsnooping_ObjectIdentity=ObjectIdentity
dhcpsnooping=_Dhcpsnooping_ObjectIdentity((1,3,6,1,4,1,52642,2,233))
class _DhcpSnoopingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_DhcpSnoopingStatus_Type.__name__=_F
_DhcpSnoopingStatus_Object=MibScalar
dhcpSnoopingStatus=_DhcpSnoopingStatus_Object((1,3,6,1,4,1,52642,2,233,1),_DhcpSnoopingStatus_Type())
dhcpSnoopingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSnoopingStatus.setStatus(_D)
_NmsBindingsTable_Object=MibTable
nmsBindingsTable=_NmsBindingsTable_Object((1,3,6,1,4,1,52642,2,233,2))
if mibBuilder.loadTexts:nmsBindingsTable.setStatus(_A)
_NmsBindingsEntry_Object=MibTableRow
nmsBindingsEntry=_NmsBindingsEntry_Object((1,3,6,1,4,1,52642,2,233,2,1))
nmsBindingsEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:nmsBindingsEntry.setStatus(_A)
_NmsBindingsIpAddress_Type=InetAddress
_NmsBindingsIpAddress_Object=MibTableColumn
nmsBindingsIpAddress=_NmsBindingsIpAddress_Object((1,3,6,1,4,1,52642,2,233,2,1,1),_NmsBindingsIpAddress_Type())
nmsBindingsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsBindingsIpAddress.setStatus(_A)
_NmsBindingsMacAddress_Type=MacAddress
_NmsBindingsMacAddress_Object=MibTableColumn
nmsBindingsMacAddress=_NmsBindingsMacAddress_Object((1,3,6,1,4,1,52642,2,233,2,1,2),_NmsBindingsMacAddress_Type())
nmsBindingsMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsBindingsMacAddress.setStatus(_A)
_NmsBindingsVlan_Type=VlanIndex
_NmsBindingsVlan_Object=MibTableColumn
nmsBindingsVlan=_NmsBindingsVlan_Object((1,3,6,1,4,1,52642,2,233,2,1,3),_NmsBindingsVlan_Type())
nmsBindingsVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsBindingsVlan.setStatus(_A)
_NmsBindingsInterface_Type=InterfaceIndex
_NmsBindingsInterface_Object=MibTableColumn
nmsBindingsInterface=_NmsBindingsInterface_Object((1,3,6,1,4,1,52642,2,233,2,1,4),_NmsBindingsInterface_Type())
nmsBindingsInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsBindingsInterface.setStatus(_A)
_NmsBindingsLeasedTime_Type=Unsigned32
_NmsBindingsLeasedTime_Object=MibTableColumn
nmsBindingsLeasedTime=_NmsBindingsLeasedTime_Object((1,3,6,1,4,1,52642,2,233,2,1,5),_NmsBindingsLeasedTime_Type())
nmsBindingsLeasedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsBindingsLeasedTime.setStatus(_A)
if mibBuilder.loadTexts:nmsBindingsLeasedTime.setUnits('seconds')
_NmsBindingsType_Type=Unsigned32
_NmsBindingsType_Object=MibTableColumn
nmsBindingsType=_NmsBindingsType_Object((1,3,6,1,4,1,52642,2,233,2,1,6),_NmsBindingsType_Type())
nmsBindingsType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsBindingsType.setStatus(_A)
_NmsBindingsStatus_Type=Unsigned32
_NmsBindingsStatus_Object=MibTableColumn
nmsBindingsStatus=_NmsBindingsStatus_Object((1,3,6,1,4,1,52642,2,233,2,1,7),_NmsBindingsStatus_Type())
nmsBindingsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsBindingsStatus.setStatus(_A)
_NmsBindingsrowstatus_Type=RowStatus
_NmsBindingsrowstatus_Object=MibTableColumn
nmsBindingsrowstatus=_NmsBindingsrowstatus_Object((1,3,6,1,4,1,52642,2,233,2,1,8),_NmsBindingsrowstatus_Type())
nmsBindingsrowstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsBindingsrowstatus.setStatus(_D)
_NmsipsourceBindingsTable_Object=MibTable
nmsipsourceBindingsTable=_NmsipsourceBindingsTable_Object((1,3,6,1,4,1,52642,2,233,3))
if mibBuilder.loadTexts:nmsipsourceBindingsTable.setStatus(_A)
_NmsipsourceBindingsEntry_Object=MibTableRow
nmsipsourceBindingsEntry=_NmsipsourceBindingsEntry_Object((1,3,6,1,4,1,52642,2,233,3,1))
nmsipsourceBindingsEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:nmsipsourceBindingsEntry.setStatus(_A)
_NmsipsourceBindingsrowstatus_Type=RowStatus
_NmsipsourceBindingsrowstatus_Object=MibTableColumn
nmsipsourceBindingsrowstatus=_NmsipsourceBindingsrowstatus_Object((1,3,6,1,4,1,52642,2,233,3,1,1),_NmsipsourceBindingsrowstatus_Type())
nmsipsourceBindingsrowstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsipsourceBindingsrowstatus.setStatus(_D)
_NmsipsourceBindingsIpAddress_Type=InetAddress
_NmsipsourceBindingsIpAddress_Object=MibTableColumn
nmsipsourceBindingsIpAddress=_NmsipsourceBindingsIpAddress_Object((1,3,6,1,4,1,52642,2,233,3,1,2),_NmsipsourceBindingsIpAddress_Type())
nmsipsourceBindingsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsipsourceBindingsIpAddress.setStatus(_A)
_NmsipsourceBindingsMacAddress_Type=MacAddress
_NmsipsourceBindingsMacAddress_Object=MibTableColumn
nmsipsourceBindingsMacAddress=_NmsipsourceBindingsMacAddress_Object((1,3,6,1,4,1,52642,2,233,3,1,3),_NmsipsourceBindingsMacAddress_Type())
nmsipsourceBindingsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsipsourceBindingsMacAddress.setStatus(_A)
_NmsipsourceBindingsInterface_Type=InterfaceIndex
_NmsipsourceBindingsInterface_Object=MibTableColumn
nmsipsourceBindingsInterface=_NmsipsourceBindingsInterface_Object((1,3,6,1,4,1,52642,2,233,3,1,4),_NmsipsourceBindingsInterface_Type())
nmsipsourceBindingsInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsipsourceBindingsInterface.setStatus(_A)
_NmsipsourceBindingsVlanID_Type=VlanIndex
_NmsipsourceBindingsVlanID_Object=MibTableColumn
nmsipsourceBindingsVlanID=_NmsipsourceBindingsVlanID_Object((1,3,6,1,4,1,52642,2,233,3,1,5),_NmsipsourceBindingsVlanID_Type())
nmsipsourceBindingsVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsipsourceBindingsVlanID.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dhcpsnooping':dhcpsnooping,'dhcpSnoopingStatus':dhcpSnoopingStatus,'nmsBindingsTable':nmsBindingsTable,'nmsBindingsEntry':nmsBindingsEntry,_G:nmsBindingsIpAddress,'nmsBindingsMacAddress':nmsBindingsMacAddress,'nmsBindingsVlan':nmsBindingsVlan,'nmsBindingsInterface':nmsBindingsInterface,'nmsBindingsLeasedTime':nmsBindingsLeasedTime,'nmsBindingsType':nmsBindingsType,'nmsBindingsStatus':nmsBindingsStatus,'nmsBindingsrowstatus':nmsBindingsrowstatus,'nmsipsourceBindingsTable':nmsipsourceBindingsTable,'nmsipsourceBindingsEntry':nmsipsourceBindingsEntry,'nmsipsourceBindingsrowstatus':nmsipsourceBindingsrowstatus,_H:nmsipsourceBindingsIpAddress,'nmsipsourceBindingsMacAddress':nmsipsourceBindingsMacAddress,'nmsipsourceBindingsInterface':nmsipsourceBindingsInterface,'nmsipsourceBindingsVlanID':nmsipsourceBindingsVlanID})