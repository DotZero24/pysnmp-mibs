_e='swDHCPLocalRelayOption82PortIndex'
_d='swDHCPLocalRelayVlanID'
_c='swDHCPRelayPortStateCtrlPortIndex'
_b='swDHCPRelayVlanCtrlServer'
_a='swDHCPRelayOption61ClientID'
_Z='swDHCPRelayOption61ClientType'
_Y='swDHCPRelayOption60RelayIp'
_X='swDHCPRelayOption60String'
_W='swDHCPRelayOption60DefRelayIp'
_V='swDHCPRelayOption82PerPortCircuitIdPortIndex'
_U='swDHCPRelayOption82PerPortRemoteIdPortIndex'
_T='vendor2'
_S='user-defined'
_R='default'
_Q='replace'
_P='swDHCPRelayCtrlInterfaceName'
_O='DisplayString'
_N='relay'
_M='swDHCPRelayCtrlServer'
_L='vendor3'
_K='drop'
_J='not-accessible'
_I='read-only'
_H='disabled'
_G='enabled'
_F='OctetString'
_E='DHCP-RELAY-MGMT-MIB'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swDHCPRelayMIB=ModuleIdentity((1,3,6,1,4,1,171,12,42))
_SwDHCPRelayCtrl_ObjectIdentity=ObjectIdentity
swDHCPRelayCtrl=_SwDHCPRelayCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,42,1))
class _SwDHCPRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPRelayState_Type.__name__=_B
_SwDHCPRelayState_Object=MibScalar
swDHCPRelayState=_SwDHCPRelayState_Object((1,3,6,1,4,1,171,12,42,1,1),_SwDHCPRelayState_Type())
swDHCPRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayState.setStatus(_A)
class _SwDHCPRelayHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SwDHCPRelayHopCount_Type.__name__=_B
_SwDHCPRelayHopCount_Object=MibScalar
swDHCPRelayHopCount=_SwDHCPRelayHopCount_Object((1,3,6,1,4,1,171,12,42,1,2),_SwDHCPRelayHopCount_Type())
swDHCPRelayHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayHopCount.setStatus(_A)
class _SwDHCPRelayTimeThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDHCPRelayTimeThreshold_Type.__name__=_B
_SwDHCPRelayTimeThreshold_Object=MibScalar
swDHCPRelayTimeThreshold=_SwDHCPRelayTimeThreshold_Object((1,3,6,1,4,1,171,12,42,1,3),_SwDHCPRelayTimeThreshold_Type())
swDHCPRelayTimeThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayTimeThreshold.setStatus(_A)
_SwDHCPRelayInfo_ObjectIdentity=ObjectIdentity
swDHCPRelayInfo=_SwDHCPRelayInfo_ObjectIdentity((1,3,6,1,4,1,171,12,42,2))
_SwDHCPRelayMgmt_ObjectIdentity=ObjectIdentity
swDHCPRelayMgmt=_SwDHCPRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,42,3))
_SwDHCPRelayCtrlTable_Object=MibTable
swDHCPRelayCtrlTable=_SwDHCPRelayCtrlTable_Object((1,3,6,1,4,1,171,12,42,3,1))
if mibBuilder.loadTexts:swDHCPRelayCtrlTable.setStatus(_A)
_SwDHCPRelayCtrlEntry_Object=MibTableRow
swDHCPRelayCtrlEntry=_SwDHCPRelayCtrlEntry_Object((1,3,6,1,4,1,171,12,42,3,1,1))
swDHCPRelayCtrlEntry.setIndexNames((0,_E,_P),(0,_E,_M))
if mibBuilder.loadTexts:swDHCPRelayCtrlEntry.setStatus(_A)
class _SwDHCPRelayCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwDHCPRelayCtrlInterfaceName_Type.__name__=_O
_SwDHCPRelayCtrlInterfaceName_Object=MibTableColumn
swDHCPRelayCtrlInterfaceName=_SwDHCPRelayCtrlInterfaceName_Object((1,3,6,1,4,1,171,12,42,3,1,1,1),_SwDHCPRelayCtrlInterfaceName_Type())
swDHCPRelayCtrlInterfaceName.setMaxAccess(_I)
if mibBuilder.loadTexts:swDHCPRelayCtrlInterfaceName.setStatus(_A)
_SwDHCPRelayCtrlServer_Type=IpAddress
_SwDHCPRelayCtrlServer_Object=MibTableColumn
swDHCPRelayCtrlServer=_SwDHCPRelayCtrlServer_Object((1,3,6,1,4,1,171,12,42,3,1,1,2),_SwDHCPRelayCtrlServer_Type())
swDHCPRelayCtrlServer.setMaxAccess(_I)
if mibBuilder.loadTexts:swDHCPRelayCtrlServer.setStatus(_A)
_SwDHCPRelayCtrlRowStatus_Type=RowStatus
_SwDHCPRelayCtrlRowStatus_Object=MibTableColumn
swDHCPRelayCtrlRowStatus=_SwDHCPRelayCtrlRowStatus_Object((1,3,6,1,4,1,171,12,42,3,1,1,3),_SwDHCPRelayCtrlRowStatus_Type())
swDHCPRelayCtrlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayCtrlRowStatus.setStatus(_A)
_SwDHCPRelayOption82_ObjectIdentity=ObjectIdentity
swDHCPRelayOption82=_SwDHCPRelayOption82_ObjectIdentity((1,3,6,1,4,1,171,12,42,3,2))
class _SwDHCPRelayOption82State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPRelayOption82State_Type.__name__=_B
_SwDHCPRelayOption82State_Object=MibScalar
swDHCPRelayOption82State=_SwDHCPRelayOption82State_Object((1,3,6,1,4,1,171,12,42,3,2,1),_SwDHCPRelayOption82State_Type())
swDHCPRelayOption82State.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82State.setStatus(_A)
class _SwDHCPRelayOption82CheckState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPRelayOption82CheckState_Type.__name__=_B
_SwDHCPRelayOption82CheckState_Object=MibScalar
swDHCPRelayOption82CheckState=_SwDHCPRelayOption82CheckState_Object((1,3,6,1,4,1,171,12,42,3,2,2),_SwDHCPRelayOption82CheckState_Type())
swDHCPRelayOption82CheckState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82CheckState.setStatus(_A)
class _SwDHCPRelayOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_K,2),('keep',3)))
_SwDHCPRelayOption82Policy_Type.__name__=_B
_SwDHCPRelayOption82Policy_Object=MibScalar
swDHCPRelayOption82Policy=_SwDHCPRelayOption82Policy_Object((1,3,6,1,4,1,171,12,42,3,2,3),_SwDHCPRelayOption82Policy_Type())
swDHCPRelayOption82Policy.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82Policy.setStatus(_A)
class _SwDHCPRelayOption82RemoteIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,4),(_L,5)))
_SwDHCPRelayOption82RemoteIDType_Type.__name__=_B
_SwDHCPRelayOption82RemoteIDType_Object=MibScalar
swDHCPRelayOption82RemoteIDType=_SwDHCPRelayOption82RemoteIDType_Object((1,3,6,1,4,1,171,12,42,3,2,4),_SwDHCPRelayOption82RemoteIDType_Type())
swDHCPRelayOption82RemoteIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82RemoteIDType.setStatus(_A)
_SwDHCPRelayOption82RemoteID_Type=DisplayString
_SwDHCPRelayOption82RemoteID_Object=MibScalar
swDHCPRelayOption82RemoteID=_SwDHCPRelayOption82RemoteID_Object((1,3,6,1,4,1,171,12,42,3,2,5),_SwDHCPRelayOption82RemoteID_Type())
swDHCPRelayOption82RemoteID.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82RemoteID.setStatus(_A)
class _SwDHCPRelayOption82CircuitIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,1),(_S,2),('vendor1',3),(_T,4),(_L,5),('vendor4',6),('vendor5',7),('vendor6',8)))
_SwDHCPRelayOption82CircuitIDType_Type.__name__=_B
_SwDHCPRelayOption82CircuitIDType_Object=MibScalar
swDHCPRelayOption82CircuitIDType=_SwDHCPRelayOption82CircuitIDType_Object((1,3,6,1,4,1,171,12,42,3,2,6),_SwDHCPRelayOption82CircuitIDType_Type())
swDHCPRelayOption82CircuitIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82CircuitIDType.setStatus(_A)
_SwDHCPRelayOption82CircuitID_Type=DisplayString
_SwDHCPRelayOption82CircuitID_Object=MibScalar
swDHCPRelayOption82CircuitID=_SwDHCPRelayOption82CircuitID_Object((1,3,6,1,4,1,171,12,42,3,2,7),_SwDHCPRelayOption82CircuitID_Type())
swDHCPRelayOption82CircuitID.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82CircuitID.setStatus(_A)
_SwDHCPRelayOption82PerPortRemoteIdTable_Object=MibTable
swDHCPRelayOption82PerPortRemoteIdTable=_SwDHCPRelayOption82PerPortRemoteIdTable_Object((1,3,6,1,4,1,171,12,42,3,2,8))
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortRemoteIdTable.setStatus(_A)
_SwDHCPRelayOption82PerPortRemoteIdEntry_Object=MibTableRow
swDHCPRelayOption82PerPortRemoteIdEntry=_SwDHCPRelayOption82PerPortRemoteIdEntry_Object((1,3,6,1,4,1,171,12,42,3,2,8,1))
swDHCPRelayOption82PerPortRemoteIdEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortRemoteIdEntry.setStatus(_A)
_SwDHCPRelayOption82PerPortRemoteIdPortIndex_Type=Integer32
_SwDHCPRelayOption82PerPortRemoteIdPortIndex_Object=MibTableColumn
swDHCPRelayOption82PerPortRemoteIdPortIndex=_SwDHCPRelayOption82PerPortRemoteIdPortIndex_Object((1,3,6,1,4,1,171,12,42,3,2,8,1,1),_SwDHCPRelayOption82PerPortRemoteIdPortIndex_Type())
swDHCPRelayOption82PerPortRemoteIdPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortRemoteIdPortIndex.setStatus(_A)
class _SwDHCPRelayOption82PerPortRemoteIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_L,5))
_SwDHCPRelayOption82PerPortRemoteIdType_Type.__name__=_B
_SwDHCPRelayOption82PerPortRemoteIdType_Object=MibTableColumn
swDHCPRelayOption82PerPortRemoteIdType=_SwDHCPRelayOption82PerPortRemoteIdType_Object((1,3,6,1,4,1,171,12,42,3,2,8,1,2),_SwDHCPRelayOption82PerPortRemoteIdType_Type())
swDHCPRelayOption82PerPortRemoteIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortRemoteIdType.setStatus(_A)
_SwDHCPRelayOption82PerPortRemoteIdValue_Type=DisplayString
_SwDHCPRelayOption82PerPortRemoteIdValue_Object=MibTableColumn
swDHCPRelayOption82PerPortRemoteIdValue=_SwDHCPRelayOption82PerPortRemoteIdValue_Object((1,3,6,1,4,1,171,12,42,3,2,8,1,3),_SwDHCPRelayOption82PerPortRemoteIdValue_Type())
swDHCPRelayOption82PerPortRemoteIdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortRemoteIdValue.setStatus(_A)
_SwDHCPRelayOption82PerPortCircuitIdTable_Object=MibTable
swDHCPRelayOption82PerPortCircuitIdTable=_SwDHCPRelayOption82PerPortCircuitIdTable_Object((1,3,6,1,4,1,171,12,42,3,2,9))
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortCircuitIdTable.setStatus(_A)
_SwDHCPRelayOption82PerPortCircuitIdEntry_Object=MibTableRow
swDHCPRelayOption82PerPortCircuitIdEntry=_SwDHCPRelayOption82PerPortCircuitIdEntry_Object((1,3,6,1,4,1,171,12,42,3,2,9,1))
swDHCPRelayOption82PerPortCircuitIdEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortCircuitIdEntry.setStatus(_A)
_SwDHCPRelayOption82PerPortCircuitIdPortIndex_Type=Integer32
_SwDHCPRelayOption82PerPortCircuitIdPortIndex_Object=MibTableColumn
swDHCPRelayOption82PerPortCircuitIdPortIndex=_SwDHCPRelayOption82PerPortCircuitIdPortIndex_Object((1,3,6,1,4,1,171,12,42,3,2,9,1,1),_SwDHCPRelayOption82PerPortCircuitIdPortIndex_Type())
swDHCPRelayOption82PerPortCircuitIdPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortCircuitIdPortIndex.setStatus(_A)
class _SwDHCPRelayOption82PerPortCircuitIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_L,5))
_SwDHCPRelayOption82PerPortCircuitIdType_Type.__name__=_B
_SwDHCPRelayOption82PerPortCircuitIdType_Object=MibTableColumn
swDHCPRelayOption82PerPortCircuitIdType=_SwDHCPRelayOption82PerPortCircuitIdType_Object((1,3,6,1,4,1,171,12,42,3,2,9,1,2),_SwDHCPRelayOption82PerPortCircuitIdType_Type())
swDHCPRelayOption82PerPortCircuitIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortCircuitIdType.setStatus(_A)
_SwDHCPRelayOption82PerPortCircuitIdValue_Type=DisplayString
_SwDHCPRelayOption82PerPortCircuitIdValue_Object=MibTableColumn
swDHCPRelayOption82PerPortCircuitIdValue=_SwDHCPRelayOption82PerPortCircuitIdValue_Object((1,3,6,1,4,1,171,12,42,3,2,9,1,3),_SwDHCPRelayOption82PerPortCircuitIdValue_Type())
swDHCPRelayOption82PerPortCircuitIdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption82PerPortCircuitIdValue.setStatus(_A)
_SwDHCPRelayOption60_ObjectIdentity=ObjectIdentity
swDHCPRelayOption60=_SwDHCPRelayOption60_ObjectIdentity((1,3,6,1,4,1,171,12,42,3,3))
class _SwDHCPRelayOption60State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPRelayOption60State_Type.__name__=_B
_SwDHCPRelayOption60State_Object=MibScalar
swDHCPRelayOption60State=_SwDHCPRelayOption60State_Object((1,3,6,1,4,1,171,12,42,3,3,1),_SwDHCPRelayOption60State_Type())
swDHCPRelayOption60State.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption60State.setStatus(_A)
class _SwDHCPRelayOption60DefMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_K,2)))
_SwDHCPRelayOption60DefMode_Type.__name__=_B
_SwDHCPRelayOption60DefMode_Object=MibScalar
swDHCPRelayOption60DefMode=_SwDHCPRelayOption60DefMode_Object((1,3,6,1,4,1,171,12,42,3,3,2),_SwDHCPRelayOption60DefMode_Type())
swDHCPRelayOption60DefMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption60DefMode.setStatus(_A)
_SwDHCPRelayOption60DefTable_Object=MibTable
swDHCPRelayOption60DefTable=_SwDHCPRelayOption60DefTable_Object((1,3,6,1,4,1,171,12,42,3,3,3))
if mibBuilder.loadTexts:swDHCPRelayOption60DefTable.setStatus(_A)
_SwDHCPRelayOption60DefEntry_Object=MibTableRow
swDHCPRelayOption60DefEntry=_SwDHCPRelayOption60DefEntry_Object((1,3,6,1,4,1,171,12,42,3,3,3,1))
swDHCPRelayOption60DefEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:swDHCPRelayOption60DefEntry.setStatus(_A)
_SwDHCPRelayOption60DefRelayIp_Type=IpAddress
_SwDHCPRelayOption60DefRelayIp_Object=MibTableColumn
swDHCPRelayOption60DefRelayIp=_SwDHCPRelayOption60DefRelayIp_Object((1,3,6,1,4,1,171,12,42,3,3,3,1,1),_SwDHCPRelayOption60DefRelayIp_Type())
swDHCPRelayOption60DefRelayIp.setMaxAccess(_I)
if mibBuilder.loadTexts:swDHCPRelayOption60DefRelayIp.setStatus(_A)
_SwDHCPRelayOption60DefRowStatus_Type=RowStatus
_SwDHCPRelayOption60DefRowStatus_Object=MibTableColumn
swDHCPRelayOption60DefRowStatus=_SwDHCPRelayOption60DefRowStatus_Object((1,3,6,1,4,1,171,12,42,3,3,3,1,2),_SwDHCPRelayOption60DefRowStatus_Type())
swDHCPRelayOption60DefRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayOption60DefRowStatus.setStatus(_A)
_SwDHCPRelayOption60Table_Object=MibTable
swDHCPRelayOption60Table=_SwDHCPRelayOption60Table_Object((1,3,6,1,4,1,171,12,42,3,3,4))
if mibBuilder.loadTexts:swDHCPRelayOption60Table.setStatus(_A)
_SwDHCPRelayOption60Entry_Object=MibTableRow
swDHCPRelayOption60Entry=_SwDHCPRelayOption60Entry_Object((1,3,6,1,4,1,171,12,42,3,3,4,1))
swDHCPRelayOption60Entry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:swDHCPRelayOption60Entry.setStatus(_A)
_SwDHCPRelayOption60String_Type=DisplayString
_SwDHCPRelayOption60String_Object=MibTableColumn
swDHCPRelayOption60String=_SwDHCPRelayOption60String_Object((1,3,6,1,4,1,171,12,42,3,3,4,1,1),_SwDHCPRelayOption60String_Type())
swDHCPRelayOption60String.setMaxAccess(_I)
if mibBuilder.loadTexts:swDHCPRelayOption60String.setStatus(_A)
_SwDHCPRelayOption60RelayIp_Type=IpAddress
_SwDHCPRelayOption60RelayIp_Object=MibTableColumn
swDHCPRelayOption60RelayIp=_SwDHCPRelayOption60RelayIp_Object((1,3,6,1,4,1,171,12,42,3,3,4,1,2),_SwDHCPRelayOption60RelayIp_Type())
swDHCPRelayOption60RelayIp.setMaxAccess(_I)
if mibBuilder.loadTexts:swDHCPRelayOption60RelayIp.setStatus(_A)
class _SwDHCPRelayOption60MatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exact',1),('partial',2)))
_SwDHCPRelayOption60MatchType_Type.__name__=_B
_SwDHCPRelayOption60MatchType_Object=MibTableColumn
swDHCPRelayOption60MatchType=_SwDHCPRelayOption60MatchType_Object((1,3,6,1,4,1,171,12,42,3,3,4,1,3),_SwDHCPRelayOption60MatchType_Type())
swDHCPRelayOption60MatchType.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayOption60MatchType.setStatus(_A)
_SwDHCPRelayOption60RowStatus_Type=RowStatus
_SwDHCPRelayOption60RowStatus_Object=MibTableColumn
swDHCPRelayOption60RowStatus=_SwDHCPRelayOption60RowStatus_Object((1,3,6,1,4,1,171,12,42,3,3,4,1,4),_SwDHCPRelayOption60RowStatus_Type())
swDHCPRelayOption60RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayOption60RowStatus.setStatus(_A)
_SwDHCPRelayOption61_ObjectIdentity=ObjectIdentity
swDHCPRelayOption61=_SwDHCPRelayOption61_ObjectIdentity((1,3,6,1,4,1,171,12,42,3,4))
class _SwDHCPRelayOption61State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPRelayOption61State_Type.__name__=_B
_SwDHCPRelayOption61State_Object=MibScalar
swDHCPRelayOption61State=_SwDHCPRelayOption61State_Object((1,3,6,1,4,1,171,12,42,3,4,1),_SwDHCPRelayOption61State_Type())
swDHCPRelayOption61State.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption61State.setStatus(_A)
class _SwDHCPRelayOption61DefMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_K,2)))
_SwDHCPRelayOption61DefMode_Type.__name__=_B
_SwDHCPRelayOption61DefMode_Object=MibScalar
swDHCPRelayOption61DefMode=_SwDHCPRelayOption61DefMode_Object((1,3,6,1,4,1,171,12,42,3,4,2),_SwDHCPRelayOption61DefMode_Type())
swDHCPRelayOption61DefMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption61DefMode.setStatus(_A)
_SwDHCPRelayOption61DefRelayIp_Type=IpAddress
_SwDHCPRelayOption61DefRelayIp_Object=MibScalar
swDHCPRelayOption61DefRelayIp=_SwDHCPRelayOption61DefRelayIp_Object((1,3,6,1,4,1,171,12,42,3,4,3),_SwDHCPRelayOption61DefRelayIp_Type())
swDHCPRelayOption61DefRelayIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayOption61DefRelayIp.setStatus(_A)
_SwDHCPRelayOption61Table_Object=MibTable
swDHCPRelayOption61Table=_SwDHCPRelayOption61Table_Object((1,3,6,1,4,1,171,12,42,3,4,4))
if mibBuilder.loadTexts:swDHCPRelayOption61Table.setStatus(_A)
_SwDHCPRelayOption61Entry_Object=MibTableRow
swDHCPRelayOption61Entry=_SwDHCPRelayOption61Entry_Object((1,3,6,1,4,1,171,12,42,3,4,4,1))
swDHCPRelayOption61Entry.setIndexNames((0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:swDHCPRelayOption61Entry.setStatus(_A)
class _SwDHCPRelayOption61ClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mac',1),('string',2)))
_SwDHCPRelayOption61ClientType_Type.__name__=_B
_SwDHCPRelayOption61ClientType_Object=MibTableColumn
swDHCPRelayOption61ClientType=_SwDHCPRelayOption61ClientType_Object((1,3,6,1,4,1,171,12,42,3,4,4,1,1),_SwDHCPRelayOption61ClientType_Type())
swDHCPRelayOption61ClientType.setMaxAccess(_I)
if mibBuilder.loadTexts:swDHCPRelayOption61ClientType.setStatus(_A)
_SwDHCPRelayOption61ClientID_Type=DisplayString
_SwDHCPRelayOption61ClientID_Object=MibTableColumn
swDHCPRelayOption61ClientID=_SwDHCPRelayOption61ClientID_Object((1,3,6,1,4,1,171,12,42,3,4,4,1,2),_SwDHCPRelayOption61ClientID_Type())
swDHCPRelayOption61ClientID.setMaxAccess(_I)
if mibBuilder.loadTexts:swDHCPRelayOption61ClientID.setStatus(_A)
class _SwDHCPRelayOption61Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_K,2)))
_SwDHCPRelayOption61Mode_Type.__name__=_B
_SwDHCPRelayOption61Mode_Object=MibTableColumn
swDHCPRelayOption61Mode=_SwDHCPRelayOption61Mode_Object((1,3,6,1,4,1,171,12,42,3,4,4,1,3),_SwDHCPRelayOption61Mode_Type())
swDHCPRelayOption61Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayOption61Mode.setStatus(_A)
_SwDHCPRelayOption61RelayIp_Type=IpAddress
_SwDHCPRelayOption61RelayIp_Object=MibTableColumn
swDHCPRelayOption61RelayIp=_SwDHCPRelayOption61RelayIp_Object((1,3,6,1,4,1,171,12,42,3,4,4,1,4),_SwDHCPRelayOption61RelayIp_Type())
swDHCPRelayOption61RelayIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayOption61RelayIp.setStatus(_A)
_SwDHCPRelayOption61RowStatus_Type=RowStatus
_SwDHCPRelayOption61RowStatus_Object=MibTableColumn
swDHCPRelayOption61RowStatus=_SwDHCPRelayOption61RowStatus_Object((1,3,6,1,4,1,171,12,42,3,4,4,1,5),_SwDHCPRelayOption61RowStatus_Type())
swDHCPRelayOption61RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayOption61RowStatus.setStatus(_A)
_SwDHCPRelayVlanCtrlTable_Object=MibTable
swDHCPRelayVlanCtrlTable=_SwDHCPRelayVlanCtrlTable_Object((1,3,6,1,4,1,171,12,42,3,5))
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlTable.setStatus(_A)
_SwDHCPRelayVlanCtrlEntry_Object=MibTableRow
swDHCPRelayVlanCtrlEntry=_SwDHCPRelayVlanCtrlEntry_Object((1,3,6,1,4,1,171,12,42,3,5,1))
swDHCPRelayVlanCtrlEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlEntry.setStatus(_A)
_SwDHCPRelayVlanCtrlServer_Type=IpAddress
_SwDHCPRelayVlanCtrlServer_Object=MibTableColumn
swDHCPRelayVlanCtrlServer=_SwDHCPRelayVlanCtrlServer_Object((1,3,6,1,4,1,171,12,42,3,5,1,1),_SwDHCPRelayVlanCtrlServer_Type())
swDHCPRelayVlanCtrlServer.setMaxAccess(_J)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlServer.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList1to64_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList1to64_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList1to64_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList1to64=_SwDHCPRelayVlanCtrlVlanRangeList1to64_Object((1,3,6,1,4,1,171,12,42,3,5,1,2),_SwDHCPRelayVlanCtrlVlanRangeList1to64_Type())
swDHCPRelayVlanCtrlVlanRangeList1to64.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList1to64.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList65to128_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList65to128_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList65to128_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList65to128=_SwDHCPRelayVlanCtrlVlanRangeList65to128_Object((1,3,6,1,4,1,171,12,42,3,5,1,3),_SwDHCPRelayVlanCtrlVlanRangeList65to128_Type())
swDHCPRelayVlanCtrlVlanRangeList65to128.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList65to128.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList129to192_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList129to192_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList129to192_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList129to192=_SwDHCPRelayVlanCtrlVlanRangeList129to192_Object((1,3,6,1,4,1,171,12,42,3,5,1,4),_SwDHCPRelayVlanCtrlVlanRangeList129to192_Type())
swDHCPRelayVlanCtrlVlanRangeList129to192.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList129to192.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList193to256_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList193to256_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList193to256_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList193to256=_SwDHCPRelayVlanCtrlVlanRangeList193to256_Object((1,3,6,1,4,1,171,12,42,3,5,1,5),_SwDHCPRelayVlanCtrlVlanRangeList193to256_Type())
swDHCPRelayVlanCtrlVlanRangeList193to256.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList193to256.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList257to320_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList257to320_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList257to320_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList257to320=_SwDHCPRelayVlanCtrlVlanRangeList257to320_Object((1,3,6,1,4,1,171,12,42,3,5,1,6),_SwDHCPRelayVlanCtrlVlanRangeList257to320_Type())
swDHCPRelayVlanCtrlVlanRangeList257to320.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList257to320.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList321to384_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList321to384_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList321to384_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList321to384=_SwDHCPRelayVlanCtrlVlanRangeList321to384_Object((1,3,6,1,4,1,171,12,42,3,5,1,7),_SwDHCPRelayVlanCtrlVlanRangeList321to384_Type())
swDHCPRelayVlanCtrlVlanRangeList321to384.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList321to384.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList385to448_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList385to448_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList385to448_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList385to448=_SwDHCPRelayVlanCtrlVlanRangeList385to448_Object((1,3,6,1,4,1,171,12,42,3,5,1,8),_SwDHCPRelayVlanCtrlVlanRangeList385to448_Type())
swDHCPRelayVlanCtrlVlanRangeList385to448.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList385to448.setStatus(_A)
class _SwDHCPRelayVlanCtrlVlanRangeList449to512_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwDHCPRelayVlanCtrlVlanRangeList449to512_Type.__name__=_F
_SwDHCPRelayVlanCtrlVlanRangeList449to512_Object=MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList449to512=_SwDHCPRelayVlanCtrlVlanRangeList449to512_Object((1,3,6,1,4,1,171,12,42,3,5,1,9),_SwDHCPRelayVlanCtrlVlanRangeList449to512_Type())
swDHCPRelayVlanCtrlVlanRangeList449to512.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlVlanRangeList449to512.setStatus(_A)
_SwDHCPRelayVlanCtrlRowStatus_Type=RowStatus
_SwDHCPRelayVlanCtrlRowStatus_Object=MibTableColumn
swDHCPRelayVlanCtrlRowStatus=_SwDHCPRelayVlanCtrlRowStatus_Object((1,3,6,1,4,1,171,12,42,3,5,1,10),_SwDHCPRelayVlanCtrlRowStatus_Type())
swDHCPRelayVlanCtrlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDHCPRelayVlanCtrlRowStatus.setStatus(_A)
_SwDHCPRelayPortStateCtrlTable_Object=MibTable
swDHCPRelayPortStateCtrlTable=_SwDHCPRelayPortStateCtrlTable_Object((1,3,6,1,4,1,171,12,42,3,6))
if mibBuilder.loadTexts:swDHCPRelayPortStateCtrlTable.setStatus(_A)
_SwDHCPRelayPortStateCtrlEntry_Object=MibTableRow
swDHCPRelayPortStateCtrlEntry=_SwDHCPRelayPortStateCtrlEntry_Object((1,3,6,1,4,1,171,12,42,3,6,1))
swDHCPRelayPortStateCtrlEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:swDHCPRelayPortStateCtrlEntry.setStatus(_A)
_SwDHCPRelayPortStateCtrlPortIndex_Type=Integer32
_SwDHCPRelayPortStateCtrlPortIndex_Object=MibTableColumn
swDHCPRelayPortStateCtrlPortIndex=_SwDHCPRelayPortStateCtrlPortIndex_Object((1,3,6,1,4,1,171,12,42,3,6,1,1),_SwDHCPRelayPortStateCtrlPortIndex_Type())
swDHCPRelayPortStateCtrlPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swDHCPRelayPortStateCtrlPortIndex.setStatus(_A)
class _SwDHCPRelayPortStateCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPRelayPortStateCtrlState_Type.__name__=_B
_SwDHCPRelayPortStateCtrlState_Object=MibTableColumn
swDHCPRelayPortStateCtrlState=_SwDHCPRelayPortStateCtrlState_Object((1,3,6,1,4,1,171,12,42,3,6,1,2),_SwDHCPRelayPortStateCtrlState_Type())
swDHCPRelayPortStateCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelayPortStateCtrlState.setStatus(_A)
_SwDHCPRelaySendArpByCidTable_Object=MibTable
swDHCPRelaySendArpByCidTable=_SwDHCPRelaySendArpByCidTable_Object((1,3,6,1,4,1,171,12,42,3,7))
if mibBuilder.loadTexts:swDHCPRelaySendArpByCidTable.setStatus(_A)
_SwDHCPRelaySendArpByCidEntry_Object=MibTableRow
swDHCPRelaySendArpByCidEntry=_SwDHCPRelaySendArpByCidEntry_Object((1,3,6,1,4,1,171,12,42,3,7,1))
swDHCPRelaySendArpByCidEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:swDHCPRelaySendArpByCidEntry.setStatus(_A)
class _SwDHCPRelaySendArpByCidInnerVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SwDHCPRelaySendArpByCidInnerVid_Type.__name__=_B
_SwDHCPRelaySendArpByCidInnerVid_Object=MibTableColumn
swDHCPRelaySendArpByCidInnerVid=_SwDHCPRelaySendArpByCidInnerVid_Object((1,3,6,1,4,1,171,12,42,3,7,1,1),_SwDHCPRelaySendArpByCidInnerVid_Type())
swDHCPRelaySendArpByCidInnerVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPRelaySendArpByCidInnerVid.setStatus(_A)
_SwDHCPLocalRelayMgmt_ObjectIdentity=ObjectIdentity
swDHCPLocalRelayMgmt=_SwDHCPLocalRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,42,4))
class _SwDHCPLocalRelayGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPLocalRelayGlobalState_Type.__name__=_B
_SwDHCPLocalRelayGlobalState_Object=MibScalar
swDHCPLocalRelayGlobalState=_SwDHCPLocalRelayGlobalState_Object((1,3,6,1,4,1,171,12,42,4,1),_SwDHCPLocalRelayGlobalState_Type())
swDHCPLocalRelayGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPLocalRelayGlobalState.setStatus(_A)
_SwDHCPLocalRelayVlanTable_Object=MibTable
swDHCPLocalRelayVlanTable=_SwDHCPLocalRelayVlanTable_Object((1,3,6,1,4,1,171,12,42,4,2))
if mibBuilder.loadTexts:swDHCPLocalRelayVlanTable.setStatus(_A)
_SwDHCPLocalRelayVlanEntry_Object=MibTableRow
swDHCPLocalRelayVlanEntry=_SwDHCPLocalRelayVlanEntry_Object((1,3,6,1,4,1,171,12,42,4,2,1))
swDHCPLocalRelayVlanEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:swDHCPLocalRelayVlanEntry.setStatus(_A)
_SwDHCPLocalRelayVlanID_Type=VlanId
_SwDHCPLocalRelayVlanID_Object=MibTableColumn
swDHCPLocalRelayVlanID=_SwDHCPLocalRelayVlanID_Object((1,3,6,1,4,1,171,12,42,4,2,1,1),_SwDHCPLocalRelayVlanID_Type())
swDHCPLocalRelayVlanID.setMaxAccess(_J)
if mibBuilder.loadTexts:swDHCPLocalRelayVlanID.setStatus(_A)
class _SwDHCPLocalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDHCPLocalRelayState_Type.__name__=_B
_SwDHCPLocalRelayState_Object=MibTableColumn
swDHCPLocalRelayState=_SwDHCPLocalRelayState_Object((1,3,6,1,4,1,171,12,42,4,2,1,2),_SwDHCPLocalRelayState_Type())
swDHCPLocalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPLocalRelayState.setStatus(_A)
_SwDHCPLocalRelayOption82Table_Object=MibTable
swDHCPLocalRelayOption82Table=_SwDHCPLocalRelayOption82Table_Object((1,3,6,1,4,1,171,12,42,4,3))
if mibBuilder.loadTexts:swDHCPLocalRelayOption82Table.setStatus(_A)
_SwDHCPLocalRelayOption82Entry_Object=MibTableRow
swDHCPLocalRelayOption82Entry=_SwDHCPLocalRelayOption82Entry_Object((1,3,6,1,4,1,171,12,42,4,3,1))
swDHCPLocalRelayOption82Entry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:swDHCPLocalRelayOption82Entry.setStatus(_A)
class _SwDHCPLocalRelayOption82PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDHCPLocalRelayOption82PortIndex_Type.__name__=_B
_SwDHCPLocalRelayOption82PortIndex_Object=MibTableColumn
swDHCPLocalRelayOption82PortIndex=_SwDHCPLocalRelayOption82PortIndex_Object((1,3,6,1,4,1,171,12,42,4,3,1,1),_SwDHCPLocalRelayOption82PortIndex_Type())
swDHCPLocalRelayOption82PortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swDHCPLocalRelayOption82PortIndex.setStatus(_A)
class _SwDHCPLocalRelayOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_K,2),('keep',3)))
_SwDHCPLocalRelayOption82Policy_Type.__name__=_B
_SwDHCPLocalRelayOption82Policy_Object=MibTableColumn
swDHCPLocalRelayOption82Policy=_SwDHCPLocalRelayOption82Policy_Object((1,3,6,1,4,1,171,12,42,4,3,1,2),_SwDHCPLocalRelayOption82Policy_Type())
swDHCPLocalRelayOption82Policy.setMaxAccess(_C)
if mibBuilder.loadTexts:swDHCPLocalRelayOption82Policy.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swDHCPRelayMIB':swDHCPRelayMIB,'swDHCPRelayCtrl':swDHCPRelayCtrl,'swDHCPRelayState':swDHCPRelayState,'swDHCPRelayHopCount':swDHCPRelayHopCount,'swDHCPRelayTimeThreshold':swDHCPRelayTimeThreshold,'swDHCPRelayInfo':swDHCPRelayInfo,'swDHCPRelayMgmt':swDHCPRelayMgmt,'swDHCPRelayCtrlTable':swDHCPRelayCtrlTable,'swDHCPRelayCtrlEntry':swDHCPRelayCtrlEntry,_P:swDHCPRelayCtrlInterfaceName,_M:swDHCPRelayCtrlServer,'swDHCPRelayCtrlRowStatus':swDHCPRelayCtrlRowStatus,'swDHCPRelayOption82':swDHCPRelayOption82,'swDHCPRelayOption82State':swDHCPRelayOption82State,'swDHCPRelayOption82CheckState':swDHCPRelayOption82CheckState,'swDHCPRelayOption82Policy':swDHCPRelayOption82Policy,'swDHCPRelayOption82RemoteIDType':swDHCPRelayOption82RemoteIDType,'swDHCPRelayOption82RemoteID':swDHCPRelayOption82RemoteID,'swDHCPRelayOption82CircuitIDType':swDHCPRelayOption82CircuitIDType,'swDHCPRelayOption82CircuitID':swDHCPRelayOption82CircuitID,'swDHCPRelayOption82PerPortRemoteIdTable':swDHCPRelayOption82PerPortRemoteIdTable,'swDHCPRelayOption82PerPortRemoteIdEntry':swDHCPRelayOption82PerPortRemoteIdEntry,_U:swDHCPRelayOption82PerPortRemoteIdPortIndex,'swDHCPRelayOption82PerPortRemoteIdType':swDHCPRelayOption82PerPortRemoteIdType,'swDHCPRelayOption82PerPortRemoteIdValue':swDHCPRelayOption82PerPortRemoteIdValue,'swDHCPRelayOption82PerPortCircuitIdTable':swDHCPRelayOption82PerPortCircuitIdTable,'swDHCPRelayOption82PerPortCircuitIdEntry':swDHCPRelayOption82PerPortCircuitIdEntry,_V:swDHCPRelayOption82PerPortCircuitIdPortIndex,'swDHCPRelayOption82PerPortCircuitIdType':swDHCPRelayOption82PerPortCircuitIdType,'swDHCPRelayOption82PerPortCircuitIdValue':swDHCPRelayOption82PerPortCircuitIdValue,'swDHCPRelayOption60':swDHCPRelayOption60,'swDHCPRelayOption60State':swDHCPRelayOption60State,'swDHCPRelayOption60DefMode':swDHCPRelayOption60DefMode,'swDHCPRelayOption60DefTable':swDHCPRelayOption60DefTable,'swDHCPRelayOption60DefEntry':swDHCPRelayOption60DefEntry,_W:swDHCPRelayOption60DefRelayIp,'swDHCPRelayOption60DefRowStatus':swDHCPRelayOption60DefRowStatus,'swDHCPRelayOption60Table':swDHCPRelayOption60Table,'swDHCPRelayOption60Entry':swDHCPRelayOption60Entry,_X:swDHCPRelayOption60String,_Y:swDHCPRelayOption60RelayIp,'swDHCPRelayOption60MatchType':swDHCPRelayOption60MatchType,'swDHCPRelayOption60RowStatus':swDHCPRelayOption60RowStatus,'swDHCPRelayOption61':swDHCPRelayOption61,'swDHCPRelayOption61State':swDHCPRelayOption61State,'swDHCPRelayOption61DefMode':swDHCPRelayOption61DefMode,'swDHCPRelayOption61DefRelayIp':swDHCPRelayOption61DefRelayIp,'swDHCPRelayOption61Table':swDHCPRelayOption61Table,'swDHCPRelayOption61Entry':swDHCPRelayOption61Entry,_Z:swDHCPRelayOption61ClientType,_a:swDHCPRelayOption61ClientID,'swDHCPRelayOption61Mode':swDHCPRelayOption61Mode,'swDHCPRelayOption61RelayIp':swDHCPRelayOption61RelayIp,'swDHCPRelayOption61RowStatus':swDHCPRelayOption61RowStatus,'swDHCPRelayVlanCtrlTable':swDHCPRelayVlanCtrlTable,'swDHCPRelayVlanCtrlEntry':swDHCPRelayVlanCtrlEntry,_b:swDHCPRelayVlanCtrlServer,'swDHCPRelayVlanCtrlVlanRangeList1to64':swDHCPRelayVlanCtrlVlanRangeList1to64,'swDHCPRelayVlanCtrlVlanRangeList65to128':swDHCPRelayVlanCtrlVlanRangeList65to128,'swDHCPRelayVlanCtrlVlanRangeList129to192':swDHCPRelayVlanCtrlVlanRangeList129to192,'swDHCPRelayVlanCtrlVlanRangeList193to256':swDHCPRelayVlanCtrlVlanRangeList193to256,'swDHCPRelayVlanCtrlVlanRangeList257to320':swDHCPRelayVlanCtrlVlanRangeList257to320,'swDHCPRelayVlanCtrlVlanRangeList321to384':swDHCPRelayVlanCtrlVlanRangeList321to384,'swDHCPRelayVlanCtrlVlanRangeList385to448':swDHCPRelayVlanCtrlVlanRangeList385to448,'swDHCPRelayVlanCtrlVlanRangeList449to512':swDHCPRelayVlanCtrlVlanRangeList449to512,'swDHCPRelayVlanCtrlRowStatus':swDHCPRelayVlanCtrlRowStatus,'swDHCPRelayPortStateCtrlTable':swDHCPRelayPortStateCtrlTable,'swDHCPRelayPortStateCtrlEntry':swDHCPRelayPortStateCtrlEntry,_c:swDHCPRelayPortStateCtrlPortIndex,'swDHCPRelayPortStateCtrlState':swDHCPRelayPortStateCtrlState,'swDHCPRelaySendArpByCidTable':swDHCPRelaySendArpByCidTable,'swDHCPRelaySendArpByCidEntry':swDHCPRelaySendArpByCidEntry,'swDHCPRelaySendArpByCidInnerVid':swDHCPRelaySendArpByCidInnerVid,'swDHCPLocalRelayMgmt':swDHCPLocalRelayMgmt,'swDHCPLocalRelayGlobalState':swDHCPLocalRelayGlobalState,'swDHCPLocalRelayVlanTable':swDHCPLocalRelayVlanTable,'swDHCPLocalRelayVlanEntry':swDHCPLocalRelayVlanEntry,_d:swDHCPLocalRelayVlanID,'swDHCPLocalRelayState':swDHCPLocalRelayState,'swDHCPLocalRelayOption82Table':swDHCPLocalRelayOption82Table,'swDHCPLocalRelayOption82Entry':swDHCPLocalRelayOption82Entry,_e:swDHCPLocalRelayOption82PortIndex,'swDHCPLocalRelayOption82Policy':swDHCPLocalRelayOption82Policy})