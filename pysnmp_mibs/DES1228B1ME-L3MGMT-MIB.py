_N='swL3Ipv6AddressCtrlPrefixLen'
_M='swL3Ipv6Address'
_L='swL3Ipv6AddressCtrlInterfaceName'
_K='swL3Ipv6CtrlInterfaceName'
_J='swL3IpCtrlInterfaceName'
_I='Unsigned32'
_H='disabled'
_G='enabled'
_F='Integer32'
_E='read-write'
_D='DisplayString'
_C='DES1228B1ME-L3MGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
des1228MEv2,=mibBuilder.importSymbols('SWPRIMGMT-DES1228ME-MIB','des1228MEv2')
swL3MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,116,2,3))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwL3DevMgmt_ObjectIdentity=ObjectIdentity
swL3DevMgmt=_SwL3DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,116,2,3,1))
_SwL3IpMgmt_ObjectIdentity=ObjectIdentity
swL3IpMgmt=_SwL3IpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,116,2,3,2))
_SwL3IpCtrlMgmt_ObjectIdentity=ObjectIdentity
swL3IpCtrlMgmt=_SwL3IpCtrlMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,116,2,3,2,1))
_SwL3IpCtrlTable_Object=MibTable
swL3IpCtrlTable=_SwL3IpCtrlTable_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3))
if mibBuilder.loadTexts:swL3IpCtrlTable.setStatus(_A)
_SwL3IpCtrlEntry_Object=MibTableRow
swL3IpCtrlEntry=_SwL3IpCtrlEntry_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3,1))
swL3IpCtrlEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:swL3IpCtrlEntry.setStatus(_A)
class _SwL3IpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3IpCtrlInterfaceName_Type.__name__=_D
_SwL3IpCtrlInterfaceName_Object=MibTableColumn
swL3IpCtrlInterfaceName=_SwL3IpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3,1,1),_SwL3IpCtrlInterfaceName_Type())
swL3IpCtrlInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlInterfaceName.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalAddress_Type=Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress=_SwL3IpCtrlIpv6LinkLocalAddress_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3,1,14),_SwL3IpCtrlIpv6LinkLocalAddress_Type())
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAddress.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type=Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen=_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3,1,15),_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type())
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus(_A)
class _SwL3IpCtrlIpv6LinkLocalAutoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_G,2),(_H,3)))
_SwL3IpCtrlIpv6LinkLocalAutoState_Type.__name__=_F
_SwL3IpCtrlIpv6LinkLocalAutoState_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAutoState=_SwL3IpCtrlIpv6LinkLocalAutoState_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3,1,17),_SwL3IpCtrlIpv6LinkLocalAutoState_Type())
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAutoState.setStatus(_A)
class _SwL3IpCtrlIpDhcpOption12State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwL3IpCtrlIpDhcpOption12State_Type.__name__=_F
_SwL3IpCtrlIpDhcpOption12State_Object=MibTableColumn
swL3IpCtrlIpDhcpOption12State=_SwL3IpCtrlIpDhcpOption12State_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3,1,22),_SwL3IpCtrlIpDhcpOption12State_Type())
swL3IpCtrlIpDhcpOption12State.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlIpDhcpOption12State.setStatus(_A)
class _SwL3IpCtrlIpDhcpOption12HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_SwL3IpCtrlIpDhcpOption12HostName_Type.__name__=_D
_SwL3IpCtrlIpDhcpOption12HostName_Object=MibTableColumn
swL3IpCtrlIpDhcpOption12HostName=_SwL3IpCtrlIpDhcpOption12HostName_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,3,1,23),_SwL3IpCtrlIpDhcpOption12HostName_Type())
swL3IpCtrlIpDhcpOption12HostName.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlIpDhcpOption12HostName.setStatus(_A)
_SwL3Ipv6CtrlTable_Object=MibTable
swL3Ipv6CtrlTable=_SwL3Ipv6CtrlTable_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,4))
if mibBuilder.loadTexts:swL3Ipv6CtrlTable.setStatus(_A)
_SwL3Ipv6CtrlEntry_Object=MibTableRow
swL3Ipv6CtrlEntry=_SwL3Ipv6CtrlEntry_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,4,1))
swL3Ipv6CtrlEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:swL3Ipv6CtrlEntry.setStatus(_A)
class _SwL3Ipv6CtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6CtrlInterfaceName_Type.__name__=_D
_SwL3Ipv6CtrlInterfaceName_Object=MibTableColumn
swL3Ipv6CtrlInterfaceName=_SwL3Ipv6CtrlInterfaceName_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,4,1,1),_SwL3Ipv6CtrlInterfaceName_Type())
swL3Ipv6CtrlInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlInterfaceName.setStatus(_A)
_SwL3Ipv6CtrlMaxReassmblySize_Type=Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object=MibTableColumn
swL3Ipv6CtrlMaxReassmblySize=_SwL3Ipv6CtrlMaxReassmblySize_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,4,1,2),_SwL3Ipv6CtrlMaxReassmblySize_Type())
swL3Ipv6CtrlMaxReassmblySize.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlMaxReassmblySize.setStatus(_A)
class _SwL3Ipv6CtrlNsRetransTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SwL3Ipv6CtrlNsRetransTimer_Type.__name__=_I
_SwL3Ipv6CtrlNsRetransTimer_Object=MibTableColumn
swL3Ipv6CtrlNsRetransTimer=_SwL3Ipv6CtrlNsRetransTimer_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,4,1,3),_SwL3Ipv6CtrlNsRetransTimer_Type())
swL3Ipv6CtrlNsRetransTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Ipv6CtrlNsRetransTimer.setStatus(_A)
_SwL3Ipv6AddressCtrlTable_Object=MibTable
swL3Ipv6AddressCtrlTable=_SwL3Ipv6AddressCtrlTable_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,5))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlTable.setStatus(_A)
_SwL3Ipv6AddressCtrlEntry_Object=MibTableRow
swL3Ipv6AddressCtrlEntry=_SwL3Ipv6AddressCtrlEntry_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,5,1))
swL3Ipv6AddressCtrlEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlEntry.setStatus(_A)
class _SwL3Ipv6AddressCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6AddressCtrlInterfaceName_Type.__name__=_D
_SwL3Ipv6AddressCtrlInterfaceName_Object=MibTableColumn
swL3Ipv6AddressCtrlInterfaceName=_SwL3Ipv6AddressCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,5,1,1),_SwL3Ipv6AddressCtrlInterfaceName_Type())
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlInterfaceName.setStatus(_A)
_SwL3Ipv6Address_Type=Ipv6Address
_SwL3Ipv6Address_Object=MibTableColumn
swL3Ipv6Address=_SwL3Ipv6Address_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,5,1,2),_SwL3Ipv6Address_Type())
swL3Ipv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6Address.setStatus(_A)
_SwL3Ipv6AddressCtrlPrefixLen_Type=Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object=MibTableColumn
swL3Ipv6AddressCtrlPrefixLen=_SwL3Ipv6AddressCtrlPrefixLen_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,5,1,3),_SwL3Ipv6AddressCtrlPrefixLen_Type())
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlPrefixLen.setStatus(_A)
_SwL3Ipv6AddressCtrlState_Type=RowStatus
_SwL3Ipv6AddressCtrlState_Object=MibTableColumn
swL3Ipv6AddressCtrlState=_SwL3Ipv6AddressCtrlState_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,5,1,8),_SwL3Ipv6AddressCtrlState_Type())
swL3Ipv6AddressCtrlState.setMaxAccess('read-create')
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlState.setStatus(_A)
class _SwL3IpCtrlAllIpIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_G,2),(_H,3)))
_SwL3IpCtrlAllIpIfState_Type.__name__=_F
_SwL3IpCtrlAllIpIfState_Object=MibScalar
swL3IpCtrlAllIpIfState=_SwL3IpCtrlAllIpIfState_Object((1,3,6,1,4,1,171,11,116,2,3,2,1,7),_SwL3IpCtrlAllIpIfState_Type())
swL3IpCtrlAllIpIfState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlAllIpIfState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Ipv6Address':Ipv6Address,'swL3MgmtMIB':swL3MgmtMIB,'swL3DevMgmt':swL3DevMgmt,'swL3IpMgmt':swL3IpMgmt,'swL3IpCtrlMgmt':swL3IpCtrlMgmt,'swL3IpCtrlTable':swL3IpCtrlTable,'swL3IpCtrlEntry':swL3IpCtrlEntry,_J:swL3IpCtrlInterfaceName,'swL3IpCtrlIpv6LinkLocalAddress':swL3IpCtrlIpv6LinkLocalAddress,'swL3IpCtrlIpv6LinkLocalPrefixLen':swL3IpCtrlIpv6LinkLocalPrefixLen,'swL3IpCtrlIpv6LinkLocalAutoState':swL3IpCtrlIpv6LinkLocalAutoState,'swL3IpCtrlIpDhcpOption12State':swL3IpCtrlIpDhcpOption12State,'swL3IpCtrlIpDhcpOption12HostName':swL3IpCtrlIpDhcpOption12HostName,'swL3Ipv6CtrlTable':swL3Ipv6CtrlTable,'swL3Ipv6CtrlEntry':swL3Ipv6CtrlEntry,_K:swL3Ipv6CtrlInterfaceName,'swL3Ipv6CtrlMaxReassmblySize':swL3Ipv6CtrlMaxReassmblySize,'swL3Ipv6CtrlNsRetransTimer':swL3Ipv6CtrlNsRetransTimer,'swL3Ipv6AddressCtrlTable':swL3Ipv6AddressCtrlTable,'swL3Ipv6AddressCtrlEntry':swL3Ipv6AddressCtrlEntry,_L:swL3Ipv6AddressCtrlInterfaceName,_M:swL3Ipv6Address,_N:swL3Ipv6AddressCtrlPrefixLen,'swL3Ipv6AddressCtrlState':swL3Ipv6AddressCtrlState,'swL3IpCtrlAllIpIfState':swL3IpCtrlAllIpIfState})