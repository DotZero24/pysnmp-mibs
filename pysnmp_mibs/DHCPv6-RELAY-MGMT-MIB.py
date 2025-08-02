_N='swDHCPv6LocalRelayVlanID'
_M='vendor1'
_L='default'
_K='swDHCPv6RelayServerAddr'
_J='swDHCPv6RelayServerAddrType'
_I='DisplayString'
_H='swDHCPv6RelayIfName'
_G='not-accessible'
_F='DHCPv6-RELAY-MGMT-MIB'
_E='disabled'
_D='enabled'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
swDHCPv6RelayMIB=ModuleIdentity((1,3,6,1,4,1,171,12,84))
_SwDHCPv6RelayMIBObjects_ObjectIdentity=ObjectIdentity
swDHCPv6RelayMIBObjects=_SwDHCPv6RelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,84,1))
class _SwDHCPv6RelayHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwDHCPv6RelayHopCount_Type.__name__=_B
_SwDHCPv6RelayHopCount_Object=MibScalar
swDHCPv6RelayHopCount=_SwDHCPv6RelayHopCount_Object((1,3,6,1,4,1,171,12,84,1,1),_SwDHCPv6RelayHopCount_Type())
swDHCPv6RelayHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayHopCount.setStatus(_A)
class _SwDHCPv6RelayGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6RelayGlobalState_Type.__name__=_B
_SwDHCPv6RelayGlobalState_Object=MibScalar
swDHCPv6RelayGlobalState=_SwDHCPv6RelayGlobalState_Object((1,3,6,1,4,1,171,12,84,1,2),_SwDHCPv6RelayGlobalState_Type())
swDHCPv6RelayGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayGlobalState.setStatus(_A)
_SwDHCPv6RelayCtrlTable_Object=MibTable
swDHCPv6RelayCtrlTable=_SwDHCPv6RelayCtrlTable_Object((1,3,6,1,4,1,171,12,84,1,3))
if mibBuilder.loadTexts:swDHCPv6RelayCtrlTable.setStatus(_A)
_SwDHCPv6RelayCtrlEntry_Object=MibTableRow
swDHCPv6RelayCtrlEntry=_SwDHCPv6RelayCtrlEntry_Object((1,3,6,1,4,1,171,12,84,1,3,1))
swDHCPv6RelayCtrlEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:swDHCPv6RelayCtrlEntry.setStatus(_A)
class _SwDHCPv6RelayIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwDHCPv6RelayIfName_Type.__name__=_I
_SwDHCPv6RelayIfName_Object=MibTableColumn
swDHCPv6RelayIfName=_SwDHCPv6RelayIfName_Object((1,3,6,1,4,1,171,12,84,1,3,1,1),_SwDHCPv6RelayIfName_Type())
swDHCPv6RelayIfName.setMaxAccess(_G)
if mibBuilder.loadTexts:swDHCPv6RelayIfName.setStatus(_A)
class _SwDHCPv6RelayCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6RelayCtrlState_Type.__name__=_B
_SwDHCPv6RelayCtrlState_Object=MibTableColumn
swDHCPv6RelayCtrlState=_SwDHCPv6RelayCtrlState_Object((1,3,6,1,4,1,171,12,84,1,3,1,2),_SwDHCPv6RelayCtrlState_Type())
swDHCPv6RelayCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayCtrlState.setStatus(_A)
_SwDHCPv6RelayServerTable_Object=MibTable
swDHCPv6RelayServerTable=_SwDHCPv6RelayServerTable_Object((1,3,6,1,4,1,171,12,84,1,4))
if mibBuilder.loadTexts:swDHCPv6RelayServerTable.setStatus(_A)
_SwDHCPv6RelayServerEntry_Object=MibTableRow
swDHCPv6RelayServerEntry=_SwDHCPv6RelayServerEntry_Object((1,3,6,1,4,1,171,12,84,1,4,1))
swDHCPv6RelayServerEntry.setIndexNames((0,_F,_H),(0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:swDHCPv6RelayServerEntry.setStatus(_A)
_SwDHCPv6RelayServerAddrType_Type=InetAddressType
_SwDHCPv6RelayServerAddrType_Object=MibTableColumn
swDHCPv6RelayServerAddrType=_SwDHCPv6RelayServerAddrType_Object((1,3,6,1,4,1,171,12,84,1,4,1,1),_SwDHCPv6RelayServerAddrType_Type())
swDHCPv6RelayServerAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:swDHCPv6RelayServerAddrType.setStatus(_A)
_SwDHCPv6RelayServerAddr_Type=InetAddress
_SwDHCPv6RelayServerAddr_Object=MibTableColumn
swDHCPv6RelayServerAddr=_SwDHCPv6RelayServerAddr_Object((1,3,6,1,4,1,171,12,84,1,4,1,2),_SwDHCPv6RelayServerAddr_Type())
swDHCPv6RelayServerAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:swDHCPv6RelayServerAddr.setStatus(_A)
_SwDHCPv6RelayServerRowStatus_Type=RowStatus
_SwDHCPv6RelayServerRowStatus_Object=MibTableColumn
swDHCPv6RelayServerRowStatus=_SwDHCPv6RelayServerRowStatus_Object((1,3,6,1,4,1,171,12,84,1,4,1,3),_SwDHCPv6RelayServerRowStatus_Type())
swDHCPv6RelayServerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:swDHCPv6RelayServerRowStatus.setStatus(_A)
_SwDHCPv6RelayOption37_ObjectIdentity=ObjectIdentity
swDHCPv6RelayOption37=_SwDHCPv6RelayOption37_ObjectIdentity((1,3,6,1,4,1,171,12,84,1,5))
class _SwDHCPv6RelayOption37State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6RelayOption37State_Type.__name__=_B
_SwDHCPv6RelayOption37State_Object=MibScalar
swDHCPv6RelayOption37State=_SwDHCPv6RelayOption37State_Object((1,3,6,1,4,1,171,12,84,1,5,1),_SwDHCPv6RelayOption37State_Type())
swDHCPv6RelayOption37State.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayOption37State.setStatus(_A)
class _SwDHCPv6RelayOption37CheckState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6RelayOption37CheckState_Type.__name__=_B
_SwDHCPv6RelayOption37CheckState_Object=MibScalar
swDHCPv6RelayOption37CheckState=_SwDHCPv6RelayOption37CheckState_Object((1,3,6,1,4,1,171,12,84,1,5,2),_SwDHCPv6RelayOption37CheckState_Type())
swDHCPv6RelayOption37CheckState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayOption37CheckState.setStatus(_A)
class _SwDHCPv6RelayOption37RemoteIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('cid-with-user-defined',2),('user-defined',3),(_M,4)))
_SwDHCPv6RelayOption37RemoteIDType_Type.__name__=_B
_SwDHCPv6RelayOption37RemoteIDType_Object=MibScalar
swDHCPv6RelayOption37RemoteIDType=_SwDHCPv6RelayOption37RemoteIDType_Object((1,3,6,1,4,1,171,12,84,1,5,3),_SwDHCPv6RelayOption37RemoteIDType_Type())
swDHCPv6RelayOption37RemoteIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayOption37RemoteIDType.setStatus(_A)
_SwDHCPv6RelayOption37UserDefined_Type=DisplayString
_SwDHCPv6RelayOption37UserDefined_Object=MibScalar
swDHCPv6RelayOption37UserDefined=_SwDHCPv6RelayOption37UserDefined_Object((1,3,6,1,4,1,171,12,84,1,5,4),_SwDHCPv6RelayOption37UserDefined_Type())
swDHCPv6RelayOption37UserDefined.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayOption37UserDefined.setStatus(_A)
_SwDHCPv6RelayOption18_ObjectIdentity=ObjectIdentity
swDHCPv6RelayOption18=_SwDHCPv6RelayOption18_ObjectIdentity((1,3,6,1,4,1,171,12,84,1,6))
class _SwDHCPv6RelayOption18State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6RelayOption18State_Type.__name__=_B
_SwDHCPv6RelayOption18State_Object=MibScalar
swDHCPv6RelayOption18State=_SwDHCPv6RelayOption18State_Object((1,3,6,1,4,1,171,12,84,1,6,1),_SwDHCPv6RelayOption18State_Type())
swDHCPv6RelayOption18State.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayOption18State.setStatus(_A)
class _SwDHCPv6RelayOption18CheckState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6RelayOption18CheckState_Type.__name__=_B
_SwDHCPv6RelayOption18CheckState_Object=MibScalar
swDHCPv6RelayOption18CheckState=_SwDHCPv6RelayOption18CheckState_Object((1,3,6,1,4,1,171,12,84,1,6,2),_SwDHCPv6RelayOption18CheckState_Type())
swDHCPv6RelayOption18CheckState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayOption18CheckState.setStatus(_A)
class _SwDHCPv6RelayOption18InterfaceIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('cid',2),(_M,3)))
_SwDHCPv6RelayOption18InterfaceIDType_Type.__name__=_B
_SwDHCPv6RelayOption18InterfaceIDType_Object=MibScalar
swDHCPv6RelayOption18InterfaceIDType=_SwDHCPv6RelayOption18InterfaceIDType_Object((1,3,6,1,4,1,171,12,84,1,6,3),_SwDHCPv6RelayOption18InterfaceIDType_Type())
swDHCPv6RelayOption18InterfaceIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6RelayOption18InterfaceIDType.setStatus(_A)
_SwDHCPv6LocalRelayMIBObjects_ObjectIdentity=ObjectIdentity
swDHCPv6LocalRelayMIBObjects=_SwDHCPv6LocalRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,84,2))
class _SwDHCPv6LocalRelayGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6LocalRelayGlobalState_Type.__name__=_B
_SwDHCPv6LocalRelayGlobalState_Object=MibScalar
swDHCPv6LocalRelayGlobalState=_SwDHCPv6LocalRelayGlobalState_Object((1,3,6,1,4,1,171,12,84,2,1),_SwDHCPv6LocalRelayGlobalState_Type())
swDHCPv6LocalRelayGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6LocalRelayGlobalState.setStatus(_A)
_SwDHCPv6LocalRelayVlanTable_Object=MibTable
swDHCPv6LocalRelayVlanTable=_SwDHCPv6LocalRelayVlanTable_Object((1,3,6,1,4,1,171,12,84,2,2))
if mibBuilder.loadTexts:swDHCPv6LocalRelayVlanTable.setStatus(_A)
_SwDHCPv6LocalRelayVlanEntry_Object=MibTableRow
swDHCPv6LocalRelayVlanEntry=_SwDHCPv6LocalRelayVlanEntry_Object((1,3,6,1,4,1,171,12,84,2,2,1))
swDHCPv6LocalRelayVlanEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:swDHCPv6LocalRelayVlanEntry.setStatus(_A)
_SwDHCPv6LocalRelayVlanID_Type=VlanId
_SwDHCPv6LocalRelayVlanID_Object=MibTableColumn
swDHCPv6LocalRelayVlanID=_SwDHCPv6LocalRelayVlanID_Object((1,3,6,1,4,1,171,12,84,2,2,1,1),_SwDHCPv6LocalRelayVlanID_Type())
swDHCPv6LocalRelayVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:swDHCPv6LocalRelayVlanID.setStatus(_A)
class _SwDHCPv6LocalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwDHCPv6LocalRelayState_Type.__name__=_B
_SwDHCPv6LocalRelayState_Object=MibTableColumn
swDHCPv6LocalRelayState=_SwDHCPv6LocalRelayState_Object((1,3,6,1,4,1,171,12,84,2,2,1,2),_SwDHCPv6LocalRelayState_Type())
swDHCPv6LocalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPv6LocalRelayState.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'swDHCPv6RelayMIB':swDHCPv6RelayMIB,'swDHCPv6RelayMIBObjects':swDHCPv6RelayMIBObjects,'swDHCPv6RelayHopCount':swDHCPv6RelayHopCount,'swDHCPv6RelayGlobalState':swDHCPv6RelayGlobalState,'swDHCPv6RelayCtrlTable':swDHCPv6RelayCtrlTable,'swDHCPv6RelayCtrlEntry':swDHCPv6RelayCtrlEntry,_H:swDHCPv6RelayIfName,'swDHCPv6RelayCtrlState':swDHCPv6RelayCtrlState,'swDHCPv6RelayServerTable':swDHCPv6RelayServerTable,'swDHCPv6RelayServerEntry':swDHCPv6RelayServerEntry,_J:swDHCPv6RelayServerAddrType,_K:swDHCPv6RelayServerAddr,'swDHCPv6RelayServerRowStatus':swDHCPv6RelayServerRowStatus,'swDHCPv6RelayOption37':swDHCPv6RelayOption37,'swDHCPv6RelayOption37State':swDHCPv6RelayOption37State,'swDHCPv6RelayOption37CheckState':swDHCPv6RelayOption37CheckState,'swDHCPv6RelayOption37RemoteIDType':swDHCPv6RelayOption37RemoteIDType,'swDHCPv6RelayOption37UserDefined':swDHCPv6RelayOption37UserDefined,'swDHCPv6RelayOption18':swDHCPv6RelayOption18,'swDHCPv6RelayOption18State':swDHCPv6RelayOption18State,'swDHCPv6RelayOption18CheckState':swDHCPv6RelayOption18CheckState,'swDHCPv6RelayOption18InterfaceIDType':swDHCPv6RelayOption18InterfaceIDType,'swDHCPv6LocalRelayMIBObjects':swDHCPv6LocalRelayMIBObjects,'swDHCPv6LocalRelayGlobalState':swDHCPv6LocalRelayGlobalState,'swDHCPv6LocalRelayVlanTable':swDHCPv6LocalRelayVlanTable,'swDHCPv6LocalRelayVlanEntry':swDHCPv6LocalRelayVlanEntry,_N:swDHCPv6LocalRelayVlanID,'swDHCPv6LocalRelayState':swDHCPv6LocalRelayState})