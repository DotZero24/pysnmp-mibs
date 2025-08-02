_w='arubaWiredVsfv2NotificationsGroup'
_v='arubaWiredVsfv2PortTableGroup'
_u='arubaWiredVsfv2LinkTableGroup'
_t='arubaWiredVsfv2MemberTableGroup'
_s='arubaWiredVsfv2StatusScalarGroup'
_r='arubaWiredVsfv2ConfigScalarGroup'
_q='arubaWiredVsfv2FragmentStatusChange'
_p='arubaWiredVsfv2MemberStatusChange'
_o='arubaWiredVsfv2PortPeerProductType'
_n='arubaWiredVsfv2PortPeerSysMac'
_m='arubaWiredVsfv2PortPeerInterface'
_l='arubaWiredVsfv2PortStatusStr'
_k='arubaWiredVsfv2PortOperStatus'
_j='arubaWiredVsfv2LinkPortList'
_i='arubaWiredVsfv2LinkPeerLinkId'
_h='arubaWiredVsfv2LinkPeerMemberId'
_g='arubaWiredVsfv2LinkOperStatus'
_f='arubaWiredVsfv2MemberEntPhysicalIndex'
_e='arubaWiredVsfv2MemberCurrentUsage'
_d='arubaWiredVsfv2MemberTotalMemory'
_c='arubaWiredVsfv2MemberBootRomVersion'
_b='arubaWiredVsfv2MemberBootTime'
_a='arubaWiredVsfv2MemberMemoryUtil'
_Z='arubaWiredVsfv2MemberCpuUtil'
_Y='arubaWiredVsfv2MemberBootImage'
_X='arubaWiredVsfv2MemberSerialNum'
_W='arubaWiredVsfv2MemberProductName'
_V='arubaWiredVsfv2MemberMacAddr'
_U='arubaWiredVsfv2MemberPartNumber'
_T='arubaWiredVsfv2SplitDetectConfigured'
_S='arubaWiredVsfv2Secondary'
_R='arubaWiredVsfv2DomainId'
_Q='arubaWiredVsfv2StackMacAddr'
_P='arubaWiredVsfv2TrapEnable'
_O='arubaWiredVsfv2Topology'
_N='not-accessible'
_M='arubaWiredVsfv2LinkId'
_L='arubaWiredVsfv2LinkMemberId'
_K='read-write'
_J='arubaWiredVsfv2MemberStatus'
_I='arubaWiredVsfv2MemberRole'
_H='arubaWiredVsfv2OperStatus'
_G='arubaWiredVsfv2PortIfIndex'
_F='arubaWiredVsfv2MemberIndex'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='ARUBAWIRED-VSFv2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention','TruthValue')
arubaWiredVsfv2MIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,15))
if mibBuilder.loadTexts:arubaWiredVsfv2MIB.setRevisions(('2023-05-16 00:00','2022-03-03 00:00','2021-11-21 00:00','2020-11-18 00:00','2020-09-09 00:00','2020-07-13 00:00'))
_ArubaWiredVsfv2Notifications_ObjectIdentity=ObjectIdentity
arubaWiredVsfv2Notifications=_ArubaWiredVsfv2Notifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,15,0))
_ArubaWiredVsfv2Objects_ObjectIdentity=ObjectIdentity
arubaWiredVsfv2Objects=_ArubaWiredVsfv2Objects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,15,1))
_ArubaWiredVsfv2Config_ObjectIdentity=ObjectIdentity
arubaWiredVsfv2Config=_ArubaWiredVsfv2Config_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,15,1,0))
_ArubaWiredVsfv2TrapEnable_Type=TruthValue
_ArubaWiredVsfv2TrapEnable_Object=MibScalar
arubaWiredVsfv2TrapEnable=_ArubaWiredVsfv2TrapEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,0,1),_ArubaWiredVsfv2TrapEnable_Type())
arubaWiredVsfv2TrapEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:arubaWiredVsfv2TrapEnable.setStatus(_B)
class _ArubaWiredVsfv2SplitDetectConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('mgmt',2)))
_ArubaWiredVsfv2SplitDetectConfigured_Type.__name__=_D
_ArubaWiredVsfv2SplitDetectConfigured_Object=MibScalar
arubaWiredVsfv2SplitDetectConfigured=_ArubaWiredVsfv2SplitDetectConfigured_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,0,2),_ArubaWiredVsfv2SplitDetectConfigured_Type())
arubaWiredVsfv2SplitDetectConfigured.setMaxAccess(_K)
if mibBuilder.loadTexts:arubaWiredVsfv2SplitDetectConfigured.setStatus(_B)
_ArubaWiredVsfv2Status_ObjectIdentity=ObjectIdentity
arubaWiredVsfv2Status=_ArubaWiredVsfv2Status_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,15,1,1))
_ArubaWiredVsfv2OperStatus_Type=DisplayString
_ArubaWiredVsfv2OperStatus_Object=MibScalar
arubaWiredVsfv2OperStatus=_ArubaWiredVsfv2OperStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,1,1),_ArubaWiredVsfv2OperStatus_Type())
arubaWiredVsfv2OperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2OperStatus.setStatus(_B)
_ArubaWiredVsfv2Topology_Type=DisplayString
_ArubaWiredVsfv2Topology_Object=MibScalar
arubaWiredVsfv2Topology=_ArubaWiredVsfv2Topology_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,1,2),_ArubaWiredVsfv2Topology_Type())
arubaWiredVsfv2Topology.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2Topology.setStatus(_B)
_ArubaWiredVsfv2StackMacAddr_Type=MacAddress
_ArubaWiredVsfv2StackMacAddr_Object=MibScalar
arubaWiredVsfv2StackMacAddr=_ArubaWiredVsfv2StackMacAddr_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,1,3),_ArubaWiredVsfv2StackMacAddr_Type())
arubaWiredVsfv2StackMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2StackMacAddr.setStatus(_B)
class _ArubaWiredVsfv2DomainId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,37))
_ArubaWiredVsfv2DomainId_Type.__name__=_E
_ArubaWiredVsfv2DomainId_Object=MibScalar
arubaWiredVsfv2DomainId=_ArubaWiredVsfv2DomainId_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,1,4),_ArubaWiredVsfv2DomainId_Type())
arubaWiredVsfv2DomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2DomainId.setStatus(_B)
class _ArubaWiredVsfv2Secondary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ArubaWiredVsfv2Secondary_Type.__name__=_E
_ArubaWiredVsfv2Secondary_Object=MibScalar
arubaWiredVsfv2Secondary=_ArubaWiredVsfv2Secondary_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,1,5),_ArubaWiredVsfv2Secondary_Type())
arubaWiredVsfv2Secondary.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2Secondary.setStatus(_B)
_ArubaWiredVsfv2MemberTable_Object=MibTable
arubaWiredVsfv2MemberTable=_ArubaWiredVsfv2MemberTable_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2))
if mibBuilder.loadTexts:arubaWiredVsfv2MemberTable.setStatus(_B)
_ArubaWiredVsfv2MemberEntry_Object=MibTableRow
arubaWiredVsfv2MemberEntry=_ArubaWiredVsfv2MemberEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1))
arubaWiredVsfv2MemberEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:arubaWiredVsfv2MemberEntry.setStatus(_B)
class _ArubaWiredVsfv2MemberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2MemberIndex_Type.__name__=_D
_ArubaWiredVsfv2MemberIndex_Object=MibTableColumn
arubaWiredVsfv2MemberIndex=_ArubaWiredVsfv2MemberIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,1),_ArubaWiredVsfv2MemberIndex_Type())
arubaWiredVsfv2MemberIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberIndex.setStatus(_B)
class _ArubaWiredVsfv2MemberRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArubaWiredVsfv2MemberRole_Type.__name__=_E
_ArubaWiredVsfv2MemberRole_Object=MibTableColumn
arubaWiredVsfv2MemberRole=_ArubaWiredVsfv2MemberRole_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,2),_ArubaWiredVsfv2MemberRole_Type())
arubaWiredVsfv2MemberRole.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberRole.setStatus(_B)
class _ArubaWiredVsfv2MemberStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArubaWiredVsfv2MemberStatus_Type.__name__=_E
_ArubaWiredVsfv2MemberStatus_Object=MibTableColumn
arubaWiredVsfv2MemberStatus=_ArubaWiredVsfv2MemberStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,3),_ArubaWiredVsfv2MemberStatus_Type())
arubaWiredVsfv2MemberStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberStatus.setStatus(_B)
class _ArubaWiredVsfv2MemberPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArubaWiredVsfv2MemberPartNumber_Type.__name__=_E
_ArubaWiredVsfv2MemberPartNumber_Object=MibTableColumn
arubaWiredVsfv2MemberPartNumber=_ArubaWiredVsfv2MemberPartNumber_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,4),_ArubaWiredVsfv2MemberPartNumber_Type())
arubaWiredVsfv2MemberPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberPartNumber.setStatus(_B)
_ArubaWiredVsfv2MemberMacAddr_Type=MacAddress
_ArubaWiredVsfv2MemberMacAddr_Object=MibTableColumn
arubaWiredVsfv2MemberMacAddr=_ArubaWiredVsfv2MemberMacAddr_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,5),_ArubaWiredVsfv2MemberMacAddr_Type())
arubaWiredVsfv2MemberMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberMacAddr.setStatus(_B)
_ArubaWiredVsfv2MemberProductName_Type=DisplayString
_ArubaWiredVsfv2MemberProductName_Object=MibTableColumn
arubaWiredVsfv2MemberProductName=_ArubaWiredVsfv2MemberProductName_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,6),_ArubaWiredVsfv2MemberProductName_Type())
arubaWiredVsfv2MemberProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberProductName.setStatus(_B)
class _ArubaWiredVsfv2MemberSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArubaWiredVsfv2MemberSerialNum_Type.__name__=_E
_ArubaWiredVsfv2MemberSerialNum_Object=MibTableColumn
arubaWiredVsfv2MemberSerialNum=_ArubaWiredVsfv2MemberSerialNum_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,7),_ArubaWiredVsfv2MemberSerialNum_Type())
arubaWiredVsfv2MemberSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberSerialNum.setStatus(_B)
class _ArubaWiredVsfv2MemberBootImage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArubaWiredVsfv2MemberBootImage_Type.__name__=_E
_ArubaWiredVsfv2MemberBootImage_Object=MibTableColumn
arubaWiredVsfv2MemberBootImage=_ArubaWiredVsfv2MemberBootImage_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,8),_ArubaWiredVsfv2MemberBootImage_Type())
arubaWiredVsfv2MemberBootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberBootImage.setStatus(_B)
class _ArubaWiredVsfv2MemberCpuUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArubaWiredVsfv2MemberCpuUtil_Type.__name__=_D
_ArubaWiredVsfv2MemberCpuUtil_Object=MibTableColumn
arubaWiredVsfv2MemberCpuUtil=_ArubaWiredVsfv2MemberCpuUtil_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,9),_ArubaWiredVsfv2MemberCpuUtil_Type())
arubaWiredVsfv2MemberCpuUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberCpuUtil.setStatus(_B)
class _ArubaWiredVsfv2MemberMemoryUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArubaWiredVsfv2MemberMemoryUtil_Type.__name__=_D
_ArubaWiredVsfv2MemberMemoryUtil_Object=MibTableColumn
arubaWiredVsfv2MemberMemoryUtil=_ArubaWiredVsfv2MemberMemoryUtil_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,10),_ArubaWiredVsfv2MemberMemoryUtil_Type())
arubaWiredVsfv2MemberMemoryUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberMemoryUtil.setStatus(_B)
_ArubaWiredVsfv2MemberBootTime_Type=TimeTicks
_ArubaWiredVsfv2MemberBootTime_Object=MibTableColumn
arubaWiredVsfv2MemberBootTime=_ArubaWiredVsfv2MemberBootTime_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,11),_ArubaWiredVsfv2MemberBootTime_Type())
arubaWiredVsfv2MemberBootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberBootTime.setStatus(_B)
class _ArubaWiredVsfv2MemberBootRomVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArubaWiredVsfv2MemberBootRomVersion_Type.__name__=_E
_ArubaWiredVsfv2MemberBootRomVersion_Object=MibTableColumn
arubaWiredVsfv2MemberBootRomVersion=_ArubaWiredVsfv2MemberBootRomVersion_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,12),_ArubaWiredVsfv2MemberBootRomVersion_Type())
arubaWiredVsfv2MemberBootRomVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberBootRomVersion.setStatus(_B)
class _ArubaWiredVsfv2MemberTotalMemory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2MemberTotalMemory_Type.__name__=_D
_ArubaWiredVsfv2MemberTotalMemory_Object=MibTableColumn
arubaWiredVsfv2MemberTotalMemory=_ArubaWiredVsfv2MemberTotalMemory_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,13),_ArubaWiredVsfv2MemberTotalMemory_Type())
arubaWiredVsfv2MemberTotalMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberTotalMemory.setStatus(_B)
class _ArubaWiredVsfv2MemberCurrentUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2MemberCurrentUsage_Type.__name__=_D
_ArubaWiredVsfv2MemberCurrentUsage_Object=MibTableColumn
arubaWiredVsfv2MemberCurrentUsage=_ArubaWiredVsfv2MemberCurrentUsage_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,14),_ArubaWiredVsfv2MemberCurrentUsage_Type())
arubaWiredVsfv2MemberCurrentUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberCurrentUsage.setStatus(_B)
class _ArubaWiredVsfv2MemberEntPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredVsfv2MemberEntPhysicalIndex_Type.__name__=_D
_ArubaWiredVsfv2MemberEntPhysicalIndex_Object=MibTableColumn
arubaWiredVsfv2MemberEntPhysicalIndex=_ArubaWiredVsfv2MemberEntPhysicalIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,2,1,15),_ArubaWiredVsfv2MemberEntPhysicalIndex_Type())
arubaWiredVsfv2MemberEntPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2MemberEntPhysicalIndex.setStatus(_B)
_ArubaWiredVsfv2LinkTable_Object=MibTable
arubaWiredVsfv2LinkTable=_ArubaWiredVsfv2LinkTable_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3))
if mibBuilder.loadTexts:arubaWiredVsfv2LinkTable.setStatus(_B)
_ArubaWiredVsfv2LinkEntry_Object=MibTableRow
arubaWiredVsfv2LinkEntry=_ArubaWiredVsfv2LinkEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3,1))
arubaWiredVsfv2LinkEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:arubaWiredVsfv2LinkEntry.setStatus(_B)
class _ArubaWiredVsfv2LinkMemberId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2LinkMemberId_Type.__name__=_D
_ArubaWiredVsfv2LinkMemberId_Object=MibTableColumn
arubaWiredVsfv2LinkMemberId=_ArubaWiredVsfv2LinkMemberId_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3,1,1),_ArubaWiredVsfv2LinkMemberId_Type())
arubaWiredVsfv2LinkMemberId.setMaxAccess(_N)
if mibBuilder.loadTexts:arubaWiredVsfv2LinkMemberId.setStatus(_B)
class _ArubaWiredVsfv2LinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2LinkId_Type.__name__=_D
_ArubaWiredVsfv2LinkId_Object=MibTableColumn
arubaWiredVsfv2LinkId=_ArubaWiredVsfv2LinkId_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3,1,2),_ArubaWiredVsfv2LinkId_Type())
arubaWiredVsfv2LinkId.setMaxAccess(_N)
if mibBuilder.loadTexts:arubaWiredVsfv2LinkId.setStatus(_B)
_ArubaWiredVsfv2LinkOperStatus_Type=DisplayString
_ArubaWiredVsfv2LinkOperStatus_Object=MibTableColumn
arubaWiredVsfv2LinkOperStatus=_ArubaWiredVsfv2LinkOperStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3,1,3),_ArubaWiredVsfv2LinkOperStatus_Type())
arubaWiredVsfv2LinkOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2LinkOperStatus.setStatus(_B)
class _ArubaWiredVsfv2LinkPeerMemberId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2LinkPeerMemberId_Type.__name__=_D
_ArubaWiredVsfv2LinkPeerMemberId_Object=MibTableColumn
arubaWiredVsfv2LinkPeerMemberId=_ArubaWiredVsfv2LinkPeerMemberId_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3,1,4),_ArubaWiredVsfv2LinkPeerMemberId_Type())
arubaWiredVsfv2LinkPeerMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2LinkPeerMemberId.setStatus(_B)
class _ArubaWiredVsfv2LinkPeerLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2LinkPeerLinkId_Type.__name__=_D
_ArubaWiredVsfv2LinkPeerLinkId_Object=MibTableColumn
arubaWiredVsfv2LinkPeerLinkId=_ArubaWiredVsfv2LinkPeerLinkId_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3,1,5),_ArubaWiredVsfv2LinkPeerLinkId_Type())
arubaWiredVsfv2LinkPeerLinkId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2LinkPeerLinkId.setStatus(_B)
_ArubaWiredVsfv2LinkPortList_Type=PortList
_ArubaWiredVsfv2LinkPortList_Object=MibTableColumn
arubaWiredVsfv2LinkPortList=_ArubaWiredVsfv2LinkPortList_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,3,1,6),_ArubaWiredVsfv2LinkPortList_Type())
arubaWiredVsfv2LinkPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2LinkPortList.setStatus(_B)
_ArubaWiredVsfv2PortTable_Object=MibTable
arubaWiredVsfv2PortTable=_ArubaWiredVsfv2PortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4))
if mibBuilder.loadTexts:arubaWiredVsfv2PortTable.setStatus(_B)
_ArubaWiredVsfv2PortEntry_Object=MibTableRow
arubaWiredVsfv2PortEntry=_ArubaWiredVsfv2PortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4,1))
arubaWiredVsfv2PortEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:arubaWiredVsfv2PortEntry.setStatus(_B)
class _ArubaWiredVsfv2PortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredVsfv2PortIfIndex_Type.__name__=_D
_ArubaWiredVsfv2PortIfIndex_Object=MibTableColumn
arubaWiredVsfv2PortIfIndex=_ArubaWiredVsfv2PortIfIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4,1,1),_ArubaWiredVsfv2PortIfIndex_Type())
arubaWiredVsfv2PortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2PortIfIndex.setStatus(_B)
class _ArubaWiredVsfv2PortOperStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArubaWiredVsfv2PortOperStatus_Type.__name__=_E
_ArubaWiredVsfv2PortOperStatus_Object=MibTableColumn
arubaWiredVsfv2PortOperStatus=_ArubaWiredVsfv2PortOperStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4,1,2),_ArubaWiredVsfv2PortOperStatus_Type())
arubaWiredVsfv2PortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2PortOperStatus.setStatus(_B)
class _ArubaWiredVsfv2PortStatusStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArubaWiredVsfv2PortStatusStr_Type.__name__=_E
_ArubaWiredVsfv2PortStatusStr_Object=MibTableColumn
arubaWiredVsfv2PortStatusStr=_ArubaWiredVsfv2PortStatusStr_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4,1,3),_ArubaWiredVsfv2PortStatusStr_Type())
arubaWiredVsfv2PortStatusStr.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2PortStatusStr.setStatus(_B)
_ArubaWiredVsfv2PortPeerInterface_Type=PortList
_ArubaWiredVsfv2PortPeerInterface_Object=MibTableColumn
arubaWiredVsfv2PortPeerInterface=_ArubaWiredVsfv2PortPeerInterface_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4,1,4),_ArubaWiredVsfv2PortPeerInterface_Type())
arubaWiredVsfv2PortPeerInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2PortPeerInterface.setStatus(_B)
_ArubaWiredVsfv2PortPeerSysMac_Type=MacAddress
_ArubaWiredVsfv2PortPeerSysMac_Object=MibTableColumn
arubaWiredVsfv2PortPeerSysMac=_ArubaWiredVsfv2PortPeerSysMac_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4,1,5),_ArubaWiredVsfv2PortPeerSysMac_Type())
arubaWiredVsfv2PortPeerSysMac.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2PortPeerSysMac.setStatus(_B)
class _ArubaWiredVsfv2PortPeerProductType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ArubaWiredVsfv2PortPeerProductType_Type.__name__=_E
_ArubaWiredVsfv2PortPeerProductType_Object=MibTableColumn
arubaWiredVsfv2PortPeerProductType=_ArubaWiredVsfv2PortPeerProductType_Object((1,3,6,1,4,1,47196,4,1,1,3,15,1,4,1,6),_ArubaWiredVsfv2PortPeerProductType_Type())
arubaWiredVsfv2PortPeerProductType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredVsfv2PortPeerProductType.setStatus(_B)
_ArubaWiredVsfv2Conformance_ObjectIdentity=ObjectIdentity
arubaWiredVsfv2Conformance=_ArubaWiredVsfv2Conformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,15,2))
_ArubaWiredVsfv2Compliances_ObjectIdentity=ObjectIdentity
arubaWiredVsfv2Compliances=_ArubaWiredVsfv2Compliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,15,2,1))
_ArubaWiredVsfv2Groups_ObjectIdentity=ObjectIdentity
arubaWiredVsfv2Groups=_ArubaWiredVsfv2Groups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,15,2,2))
arubaWiredVsfv2ConfigScalarGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,15,2,2,1))
arubaWiredVsfv2ConfigScalarGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:arubaWiredVsfv2ConfigScalarGroup.setStatus(_B)
arubaWiredVsfv2StatusScalarGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,15,2,2,2))
arubaWiredVsfv2StatusScalarGroup.setObjects(*((_A,_H),(_A,_T)))
if mibBuilder.loadTexts:arubaWiredVsfv2StatusScalarGroup.setStatus(_B)
arubaWiredVsfv2MemberTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,15,2,2,3))
arubaWiredVsfv2MemberTableGroup.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:arubaWiredVsfv2MemberTableGroup.setStatus(_B)
arubaWiredVsfv2LinkTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,15,2,2,4))
arubaWiredVsfv2LinkTableGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:arubaWiredVsfv2LinkTableGroup.setStatus(_B)
arubaWiredVsfv2PortTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,15,2,2,5))
arubaWiredVsfv2PortTableGroup.setObjects(*((_A,_G),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:arubaWiredVsfv2PortTableGroup.setStatus(_B)
arubaWiredVsfv2MemberStatusChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,15,0,1))
arubaWiredVsfv2MemberStatusChange.setObjects(*((_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:arubaWiredVsfv2MemberStatusChange.setStatus(_B)
arubaWiredVsfv2FragmentStatusChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,15,0,2))
arubaWiredVsfv2FragmentStatusChange.setObjects(*((_A,_F),(_A,_H)))
if mibBuilder.loadTexts:arubaWiredVsfv2FragmentStatusChange.setStatus(_B)
arubaWiredVsfv2NotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,15,2,2,6))
arubaWiredVsfv2NotificationsGroup.setObjects(*((_A,_p),(_A,_q)))
if mibBuilder.loadTexts:arubaWiredVsfv2NotificationsGroup.setStatus(_B)
arubaWiredVsfv2MibCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,15,2,1,1))
arubaWiredVsfv2MibCompliance.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:arubaWiredVsfv2MibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'arubaWiredVsfv2MIB':arubaWiredVsfv2MIB,'arubaWiredVsfv2Notifications':arubaWiredVsfv2Notifications,_p:arubaWiredVsfv2MemberStatusChange,_q:arubaWiredVsfv2FragmentStatusChange,'arubaWiredVsfv2Objects':arubaWiredVsfv2Objects,'arubaWiredVsfv2Config':arubaWiredVsfv2Config,_P:arubaWiredVsfv2TrapEnable,_T:arubaWiredVsfv2SplitDetectConfigured,'arubaWiredVsfv2Status':arubaWiredVsfv2Status,_H:arubaWiredVsfv2OperStatus,_O:arubaWiredVsfv2Topology,_Q:arubaWiredVsfv2StackMacAddr,_R:arubaWiredVsfv2DomainId,_S:arubaWiredVsfv2Secondary,'arubaWiredVsfv2MemberTable':arubaWiredVsfv2MemberTable,'arubaWiredVsfv2MemberEntry':arubaWiredVsfv2MemberEntry,_F:arubaWiredVsfv2MemberIndex,_I:arubaWiredVsfv2MemberRole,_J:arubaWiredVsfv2MemberStatus,_U:arubaWiredVsfv2MemberPartNumber,_V:arubaWiredVsfv2MemberMacAddr,_W:arubaWiredVsfv2MemberProductName,_X:arubaWiredVsfv2MemberSerialNum,_Y:arubaWiredVsfv2MemberBootImage,_Z:arubaWiredVsfv2MemberCpuUtil,_a:arubaWiredVsfv2MemberMemoryUtil,_b:arubaWiredVsfv2MemberBootTime,_c:arubaWiredVsfv2MemberBootRomVersion,_d:arubaWiredVsfv2MemberTotalMemory,_e:arubaWiredVsfv2MemberCurrentUsage,_f:arubaWiredVsfv2MemberEntPhysicalIndex,'arubaWiredVsfv2LinkTable':arubaWiredVsfv2LinkTable,'arubaWiredVsfv2LinkEntry':arubaWiredVsfv2LinkEntry,_L:arubaWiredVsfv2LinkMemberId,_M:arubaWiredVsfv2LinkId,_g:arubaWiredVsfv2LinkOperStatus,_h:arubaWiredVsfv2LinkPeerMemberId,_i:arubaWiredVsfv2LinkPeerLinkId,_j:arubaWiredVsfv2LinkPortList,'arubaWiredVsfv2PortTable':arubaWiredVsfv2PortTable,'arubaWiredVsfv2PortEntry':arubaWiredVsfv2PortEntry,_G:arubaWiredVsfv2PortIfIndex,_k:arubaWiredVsfv2PortOperStatus,_l:arubaWiredVsfv2PortStatusStr,_m:arubaWiredVsfv2PortPeerInterface,_n:arubaWiredVsfv2PortPeerSysMac,_o:arubaWiredVsfv2PortPeerProductType,'arubaWiredVsfv2Conformance':arubaWiredVsfv2Conformance,'arubaWiredVsfv2Compliances':arubaWiredVsfv2Compliances,'arubaWiredVsfv2MibCompliance':arubaWiredVsfv2MibCompliance,'arubaWiredVsfv2Groups':arubaWiredVsfv2Groups,_r:arubaWiredVsfv2ConfigScalarGroup,_s:arubaWiredVsfv2StatusScalarGroup,_t:arubaWiredVsfv2MemberTableGroup,_u:arubaWiredVsfv2LinkTableGroup,_v:arubaWiredVsfv2PortTableGroup,_w:arubaWiredVsfv2NotificationsGroup})