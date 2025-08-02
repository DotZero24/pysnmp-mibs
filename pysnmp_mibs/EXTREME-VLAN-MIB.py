_m='extremePvlanSubscriberVlanIfIndex'
_l='extremeVlanTranslationMemberVlanIfIndex'
_k='extremeVlanTranslationSuperVlanIfIndex'
_j='extremeVlanAggregationConfigSuperVlanIfIndex'
_i='extremeVlanAggregationSubVlanIfIndex'
_h='extremeVlanAggregationSuperVlanIfIndex'
_g='extremeStatsVlanNameIndex'
_f='extremeStatsPortIfIndex'
_e='extremeVlanStackLowerLayer'
_d='extremeVlanStackHigherLayer'
_c='extremeVlanProtocolBindingIfIndex'
_b='extremeVlanProtocolDefValue'
_a='extremeVlanProtocolDefDllEncapsType'
_Z='extremeVlanProtocolDefName'
_Y='extremeVlanProtocolVlanProtocolIndex'
_X='extremeVlanProtocolVlanIfIndex'
_W='llcSnapEthertype'
_V='ethertype'
_U='extremeVlanProtocolIdIndex'
_T='extremeVlanProtocolIndex'
_S='extremeVlanEncapsIfIndex'
_R='extremeVlanGlobalMappingIdentifier'
_Q='TruthValue'
_P='MacAddress'
_O='extremePvlanName'
_N='InterfaceIndexOrZero'
_M='extremeSlotNumber'
_L='EXTREME-SYSTEM-MIB'
_K='OctetString'
_J='not-accessible'
_I='read-write'
_H='extremeVlanIfIndex'
_G='deprecated'
_F='DisplayString'
_E='Integer32'
_D='EXTREME-VLAN-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','PortList','extremeAgent')
extremeSlotNumber,=mibBuilder.importSymbols(_L,_M)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_N)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,_P,'PhysAddress','RowStatus','TextualConvention',_Q)
extremeVlan=ModuleIdentity((1,3,6,1,4,1,1916,1,2))
class ExtremeVlanType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('vlanLayer2',1))
class ExtremeVlanEncapsType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlanEncaps8021q',1),('vlanEncapsNone',2)))
_ExtremeVlanGroup_ObjectIdentity=ObjectIdentity
extremeVlanGroup=_ExtremeVlanGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,1))
_ExtremeVlanGlobalMappingTable_Object=MibTable
extremeVlanGlobalMappingTable=_ExtremeVlanGlobalMappingTable_Object((1,3,6,1,4,1,1916,1,2,1,1))
if mibBuilder.loadTexts:extremeVlanGlobalMappingTable.setStatus(_G)
_ExtremeVlanGlobalMappingEntry_Object=MibTableRow
extremeVlanGlobalMappingEntry=_ExtremeVlanGlobalMappingEntry_Object((1,3,6,1,4,1,1916,1,2,1,1,1))
extremeVlanGlobalMappingEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:extremeVlanGlobalMappingEntry.setStatus(_A)
class _ExtremeVlanGlobalMappingIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeVlanGlobalMappingIdentifier_Type.__name__=_E
_ExtremeVlanGlobalMappingIdentifier_Object=MibTableColumn
extremeVlanGlobalMappingIdentifier=_ExtremeVlanGlobalMappingIdentifier_Object((1,3,6,1,4,1,1916,1,2,1,1,1,1),_ExtremeVlanGlobalMappingIdentifier_Type())
extremeVlanGlobalMappingIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanGlobalMappingIdentifier.setStatus(_A)
_ExtremeVlanGlobalMappingIfIndex_Type=Integer32
_ExtremeVlanGlobalMappingIfIndex_Object=MibTableColumn
extremeVlanGlobalMappingIfIndex=_ExtremeVlanGlobalMappingIfIndex_Object((1,3,6,1,4,1,1916,1,2,1,1,1,2),_ExtremeVlanGlobalMappingIfIndex_Type())
extremeVlanGlobalMappingIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanGlobalMappingIfIndex.setStatus(_A)
_ExtremeVlanIfTable_Object=MibTable
extremeVlanIfTable=_ExtremeVlanIfTable_Object((1,3,6,1,4,1,1916,1,2,1,2))
if mibBuilder.loadTexts:extremeVlanIfTable.setStatus(_A)
_ExtremeVlanIfEntry_Object=MibTableRow
extremeVlanIfEntry=_ExtremeVlanIfEntry_Object((1,3,6,1,4,1,1916,1,2,1,2,1))
extremeVlanIfEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:extremeVlanIfEntry.setStatus(_A)
_ExtremeVlanIfIndex_Type=Integer32
_ExtremeVlanIfIndex_Object=MibTableColumn
extremeVlanIfIndex=_ExtremeVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,1,2,1,1),_ExtremeVlanIfIndex_Type())
extremeVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIfIndex.setStatus(_A)
class _ExtremeVlanIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVlanIfDescr_Type.__name__=_F
_ExtremeVlanIfDescr_Object=MibTableColumn
extremeVlanIfDescr=_ExtremeVlanIfDescr_Object((1,3,6,1,4,1,1916,1,2,1,2,1,2),_ExtremeVlanIfDescr_Type())
extremeVlanIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIfDescr.setStatus(_A)
_ExtremeVlanIfType_Type=ExtremeVlanType
_ExtremeVlanIfType_Object=MibTableColumn
extremeVlanIfType=_ExtremeVlanIfType_Object((1,3,6,1,4,1,1916,1,2,1,2,1,3),_ExtremeVlanIfType_Type())
extremeVlanIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIfType.setStatus(_A)
class _ExtremeVlanIfGlobalIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeVlanIfGlobalIdentifier_Type.__name__=_E
_ExtremeVlanIfGlobalIdentifier_Object=MibTableColumn
extremeVlanIfGlobalIdentifier=_ExtremeVlanIfGlobalIdentifier_Object((1,3,6,1,4,1,1916,1,2,1,2,1,4),_ExtremeVlanIfGlobalIdentifier_Type())
extremeVlanIfGlobalIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIfGlobalIdentifier.setStatus(_G)
_ExtremeVlanIfStatus_Type=RowStatus
_ExtremeVlanIfStatus_Object=MibTableColumn
extremeVlanIfStatus=_ExtremeVlanIfStatus_Object((1,3,6,1,4,1,1916,1,2,1,2,1,6),_ExtremeVlanIfStatus_Type())
extremeVlanIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIfStatus.setStatus(_A)
_ExtremeVlanIfIgnoreStpFlag_Type=TruthValue
_ExtremeVlanIfIgnoreStpFlag_Object=MibTableColumn
extremeVlanIfIgnoreStpFlag=_ExtremeVlanIfIgnoreStpFlag_Object((1,3,6,1,4,1,1916,1,2,1,2,1,7),_ExtremeVlanIfIgnoreStpFlag_Type())
extremeVlanIfIgnoreStpFlag.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVlanIfIgnoreStpFlag.setStatus(_A)
_ExtremeVlanIfIgnoreBpduFlag_Type=TruthValue
_ExtremeVlanIfIgnoreBpduFlag_Object=MibTableColumn
extremeVlanIfIgnoreBpduFlag=_ExtremeVlanIfIgnoreBpduFlag_Object((1,3,6,1,4,1,1916,1,2,1,2,1,8),_ExtremeVlanIfIgnoreBpduFlag_Type())
extremeVlanIfIgnoreBpduFlag.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVlanIfIgnoreBpduFlag.setStatus(_A)
_ExtremeVlanIfLoopbackModeFlag_Type=TruthValue
_ExtremeVlanIfLoopbackModeFlag_Object=MibTableColumn
extremeVlanIfLoopbackModeFlag=_ExtremeVlanIfLoopbackModeFlag_Object((1,3,6,1,4,1,1916,1,2,1,2,1,9),_ExtremeVlanIfLoopbackModeFlag_Type())
extremeVlanIfLoopbackModeFlag.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVlanIfLoopbackModeFlag.setStatus(_A)
class _ExtremeVlanIfVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_ExtremeVlanIfVlanId_Type.__name__=_E
_ExtremeVlanIfVlanId_Object=MibTableColumn
extremeVlanIfVlanId=_ExtremeVlanIfVlanId_Object((1,3,6,1,4,1,1916,1,2,1,2,1,10),_ExtremeVlanIfVlanId_Type())
extremeVlanIfVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVlanIfVlanId.setStatus(_A)
_ExtremeVlanIfEncapsType_Type=ExtremeVlanEncapsType
_ExtremeVlanIfEncapsType_Object=MibTableColumn
extremeVlanIfEncapsType=_ExtremeVlanIfEncapsType_Object((1,3,6,1,4,1,1916,1,2,1,2,1,11),_ExtremeVlanIfEncapsType_Type())
extremeVlanIfEncapsType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIfEncapsType.setStatus(_A)
_ExtremeVlanIfAdminStatus_Type=TruthValue
_ExtremeVlanIfAdminStatus_Object=MibTableColumn
extremeVlanIfAdminStatus=_ExtremeVlanIfAdminStatus_Object((1,3,6,1,4,1,1916,1,2,1,2,1,12),_ExtremeVlanIfAdminStatus_Type())
extremeVlanIfAdminStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVlanIfAdminStatus.setStatus(_A)
_ExtremeVirtualGroup_ObjectIdentity=ObjectIdentity
extremeVirtualGroup=_ExtremeVirtualGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,2))
_ExtremeNextAvailableVirtIfIndex_Type=Integer32
_ExtremeNextAvailableVirtIfIndex_Object=MibScalar
extremeNextAvailableVirtIfIndex=_ExtremeNextAvailableVirtIfIndex_Object((1,3,6,1,4,1,1916,1,2,2,1),_ExtremeNextAvailableVirtIfIndex_Type())
extremeNextAvailableVirtIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeNextAvailableVirtIfIndex.setStatus(_A)
_ExtremeEncapsulationGroup_ObjectIdentity=ObjectIdentity
extremeEncapsulationGroup=_ExtremeEncapsulationGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,3))
_ExtremeVlanEncapsIfTable_Object=MibTable
extremeVlanEncapsIfTable=_ExtremeVlanEncapsIfTable_Object((1,3,6,1,4,1,1916,1,2,3,1))
if mibBuilder.loadTexts:extremeVlanEncapsIfTable.setStatus(_A)
_ExtremeVlanEncapsIfEntry_Object=MibTableRow
extremeVlanEncapsIfEntry=_ExtremeVlanEncapsIfEntry_Object((1,3,6,1,4,1,1916,1,2,3,1,1))
extremeVlanEncapsIfEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:extremeVlanEncapsIfEntry.setStatus(_A)
_ExtremeVlanEncapsIfIndex_Type=Integer32
_ExtremeVlanEncapsIfIndex_Object=MibTableColumn
extremeVlanEncapsIfIndex=_ExtremeVlanEncapsIfIndex_Object((1,3,6,1,4,1,1916,1,2,3,1,1,1),_ExtremeVlanEncapsIfIndex_Type())
extremeVlanEncapsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanEncapsIfIndex.setStatus(_A)
_ExtremeVlanEncapsIfType_Type=ExtremeVlanEncapsType
_ExtremeVlanEncapsIfType_Object=MibTableColumn
extremeVlanEncapsIfType=_ExtremeVlanEncapsIfType_Object((1,3,6,1,4,1,1916,1,2,3,1,1,2),_ExtremeVlanEncapsIfType_Type())
extremeVlanEncapsIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanEncapsIfType.setStatus(_A)
_ExtremeVlanEncapsIfTag_Type=Integer32
_ExtremeVlanEncapsIfTag_Object=MibTableColumn
extremeVlanEncapsIfTag=_ExtremeVlanEncapsIfTag_Object((1,3,6,1,4,1,1916,1,2,3,1,1,3),_ExtremeVlanEncapsIfTag_Type())
extremeVlanEncapsIfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanEncapsIfTag.setStatus(_A)
_ExtremeVlanEncapsIfStatus_Type=RowStatus
_ExtremeVlanEncapsIfStatus_Object=MibTableColumn
extremeVlanEncapsIfStatus=_ExtremeVlanEncapsIfStatus_Object((1,3,6,1,4,1,1916,1,2,3,1,1,4),_ExtremeVlanEncapsIfStatus_Type())
extremeVlanEncapsIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanEncapsIfStatus.setStatus(_A)
_ExtremeVlanIpGroup_ObjectIdentity=ObjectIdentity
extremeVlanIpGroup=_ExtremeVlanIpGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,4))
_ExtremeVlanIpTable_Object=MibTable
extremeVlanIpTable=_ExtremeVlanIpTable_Object((1,3,6,1,4,1,1916,1,2,4,1))
if mibBuilder.loadTexts:extremeVlanIpTable.setStatus(_A)
_ExtremeVlanIpEntry_Object=MibTableRow
extremeVlanIpEntry=_ExtremeVlanIpEntry_Object((1,3,6,1,4,1,1916,1,2,4,1,1))
extremeVlanIpEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:extremeVlanIpEntry.setStatus(_A)
_ExtremeVlanIpNetAddress_Type=IpAddress
_ExtremeVlanIpNetAddress_Object=MibTableColumn
extremeVlanIpNetAddress=_ExtremeVlanIpNetAddress_Object((1,3,6,1,4,1,1916,1,2,4,1,1,1),_ExtremeVlanIpNetAddress_Type())
extremeVlanIpNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIpNetAddress.setStatus(_A)
_ExtremeVlanIpNetMask_Type=IpAddress
_ExtremeVlanIpNetMask_Object=MibTableColumn
extremeVlanIpNetMask=_ExtremeVlanIpNetMask_Object((1,3,6,1,4,1,1916,1,2,4,1,1,2),_ExtremeVlanIpNetMask_Type())
extremeVlanIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIpNetMask.setStatus(_A)
_ExtremeVlanIpStatus_Type=RowStatus
_ExtremeVlanIpStatus_Object=MibTableColumn
extremeVlanIpStatus=_ExtremeVlanIpStatus_Object((1,3,6,1,4,1,1916,1,2,4,1,1,3),_ExtremeVlanIpStatus_Type())
extremeVlanIpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIpStatus.setStatus(_A)
_ExtremeVlanIpForwardingState_Type=TruthValue
_ExtremeVlanIpForwardingState_Object=MibTableColumn
extremeVlanIpForwardingState=_ExtremeVlanIpForwardingState_Object((1,3,6,1,4,1,1916,1,2,4,1,1,4),_ExtremeVlanIpForwardingState_Type())
extremeVlanIpForwardingState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanIpForwardingState.setStatus(_A)
_ExtremeProtocolGroup_ObjectIdentity=ObjectIdentity
extremeProtocolGroup=_ExtremeProtocolGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,5))
_ExtremeVlanProtocolTable_Object=MibTable
extremeVlanProtocolTable=_ExtremeVlanProtocolTable_Object((1,3,6,1,4,1,1916,1,2,5,1))
if mibBuilder.loadTexts:extremeVlanProtocolTable.setStatus(_A)
_ExtremeVlanProtocolEntry_Object=MibTableRow
extremeVlanProtocolEntry=_ExtremeVlanProtocolEntry_Object((1,3,6,1,4,1,1916,1,2,5,1,1))
extremeVlanProtocolEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:extremeVlanProtocolEntry.setStatus(_A)
class _ExtremeVlanProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeVlanProtocolIndex_Type.__name__=_E
_ExtremeVlanProtocolIndex_Object=MibTableColumn
extremeVlanProtocolIndex=_ExtremeVlanProtocolIndex_Object((1,3,6,1,4,1,1916,1,2,5,1,1,1),_ExtremeVlanProtocolIndex_Type())
extremeVlanProtocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolIndex.setStatus(_A)
class _ExtremeVlanProtocolIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ExtremeVlanProtocolIdIndex_Type.__name__=_E
_ExtremeVlanProtocolIdIndex_Object=MibTableColumn
extremeVlanProtocolIdIndex=_ExtremeVlanProtocolIdIndex_Object((1,3,6,1,4,1,1916,1,2,5,1,1,2),_ExtremeVlanProtocolIdIndex_Type())
extremeVlanProtocolIdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolIdIndex.setStatus(_A)
class _ExtremeVlanProtocolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeVlanProtocolName_Type.__name__=_F
_ExtremeVlanProtocolName_Object=MibTableColumn
extremeVlanProtocolName=_ExtremeVlanProtocolName_Object((1,3,6,1,4,1,1916,1,2,5,1,1,3),_ExtremeVlanProtocolName_Type())
extremeVlanProtocolName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolName.setStatus(_A)
class _ExtremeVlanProtocolDllEncapsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('any',1),(_V,2),('llc',3),(_W,4),('none',5)))
_ExtremeVlanProtocolDllEncapsType_Type.__name__=_E
_ExtremeVlanProtocolDllEncapsType_Object=MibTableColumn
extremeVlanProtocolDllEncapsType=_ExtremeVlanProtocolDllEncapsType_Object((1,3,6,1,4,1,1916,1,2,5,1,1,4),_ExtremeVlanProtocolDllEncapsType_Type())
extremeVlanProtocolDllEncapsType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolDllEncapsType.setStatus(_A)
class _ExtremeVlanProtocolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeVlanProtocolId_Type.__name__=_E
_ExtremeVlanProtocolId_Object=MibTableColumn
extremeVlanProtocolId=_ExtremeVlanProtocolId_Object((1,3,6,1,4,1,1916,1,2,5,1,1,5),_ExtremeVlanProtocolId_Type())
extremeVlanProtocolId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolId.setStatus(_A)
_ExtremeVlanProtocolStatus_Type=RowStatus
_ExtremeVlanProtocolStatus_Object=MibTableColumn
extremeVlanProtocolStatus=_ExtremeVlanProtocolStatus_Object((1,3,6,1,4,1,1916,1,2,5,1,1,6),_ExtremeVlanProtocolStatus_Type())
extremeVlanProtocolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolStatus.setStatus(_A)
class _ExtremeVlanProtocolDestAddress_Type(MacAddress):defaultHexValue='000000000000'
_ExtremeVlanProtocolDestAddress_Type.__name__=_P
_ExtremeVlanProtocolDestAddress_Object=MibTableColumn
extremeVlanProtocolDestAddress=_ExtremeVlanProtocolDestAddress_Object((1,3,6,1,4,1,1916,1,2,5,1,1,7),_ExtremeVlanProtocolDestAddress_Type())
extremeVlanProtocolDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolDestAddress.setStatus(_A)
class _ExtremeVlanProtocolDestAddressValid_Type(TruthValue):defaultValue=2
_ExtremeVlanProtocolDestAddressValid_Type.__name__=_Q
_ExtremeVlanProtocolDestAddressValid_Object=MibTableColumn
extremeVlanProtocolDestAddressValid=_ExtremeVlanProtocolDestAddressValid_Object((1,3,6,1,4,1,1916,1,2,5,1,1,8),_ExtremeVlanProtocolDestAddressValid_Type())
extremeVlanProtocolDestAddressValid.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolDestAddressValid.setStatus(_A)
class _ExtremeVlanProtocolUserFieldOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeVlanProtocolUserFieldOffset_Type.__name__=_E
_ExtremeVlanProtocolUserFieldOffset_Object=MibTableColumn
extremeVlanProtocolUserFieldOffset=_ExtremeVlanProtocolUserFieldOffset_Object((1,3,6,1,4,1,1916,1,2,5,1,1,9),_ExtremeVlanProtocolUserFieldOffset_Type())
extremeVlanProtocolUserFieldOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolUserFieldOffset.setStatus(_A)
class _ExtremeVlanProtocolUserFieldValue_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ExtremeVlanProtocolUserFieldValue_Type.__name__=_K
_ExtremeVlanProtocolUserFieldValue_Object=MibTableColumn
extremeVlanProtocolUserFieldValue=_ExtremeVlanProtocolUserFieldValue_Object((1,3,6,1,4,1,1916,1,2,5,1,1,10),_ExtremeVlanProtocolUserFieldValue_Type())
extremeVlanProtocolUserFieldValue.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolUserFieldValue.setStatus(_A)
class _ExtremeVlanProtocolUserFieldMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ExtremeVlanProtocolUserFieldMask_Type.__name__=_K
_ExtremeVlanProtocolUserFieldMask_Object=MibTableColumn
extremeVlanProtocolUserFieldMask=_ExtremeVlanProtocolUserFieldMask_Object((1,3,6,1,4,1,1916,1,2,5,1,1,11),_ExtremeVlanProtocolUserFieldMask_Type())
extremeVlanProtocolUserFieldMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolUserFieldMask.setStatus(_A)
_ExtremeVlanProtocolVlanTable_Object=MibTable
extremeVlanProtocolVlanTable=_ExtremeVlanProtocolVlanTable_Object((1,3,6,1,4,1,1916,1,2,5,2))
if mibBuilder.loadTexts:extremeVlanProtocolVlanTable.setStatus(_A)
_ExtremeVlanProtocolVlanEntry_Object=MibTableRow
extremeVlanProtocolVlanEntry=_ExtremeVlanProtocolVlanEntry_Object((1,3,6,1,4,1,1916,1,2,5,2,1))
extremeVlanProtocolVlanEntry.setIndexNames((0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:extremeVlanProtocolVlanEntry.setStatus(_A)
_ExtremeVlanProtocolVlanIfIndex_Type=Integer32
_ExtremeVlanProtocolVlanIfIndex_Object=MibTableColumn
extremeVlanProtocolVlanIfIndex=_ExtremeVlanProtocolVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,5,2,1,1),_ExtremeVlanProtocolVlanIfIndex_Type())
extremeVlanProtocolVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolVlanIfIndex.setStatus(_A)
_ExtremeVlanProtocolVlanProtocolIndex_Type=Integer32
_ExtremeVlanProtocolVlanProtocolIndex_Object=MibTableColumn
extremeVlanProtocolVlanProtocolIndex=_ExtremeVlanProtocolVlanProtocolIndex_Object((1,3,6,1,4,1,1916,1,2,5,2,1,2),_ExtremeVlanProtocolVlanProtocolIndex_Type())
extremeVlanProtocolVlanProtocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolVlanProtocolIndex.setStatus(_A)
_ExtremeVlanProtocolVlanStatus_Type=RowStatus
_ExtremeVlanProtocolVlanStatus_Object=MibTableColumn
extremeVlanProtocolVlanStatus=_ExtremeVlanProtocolVlanStatus_Object((1,3,6,1,4,1,1916,1,2,5,2,1,3),_ExtremeVlanProtocolVlanStatus_Type())
extremeVlanProtocolVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolVlanStatus.setStatus(_A)
_ExtremeVlanProtocolDefTable_Object=MibTable
extremeVlanProtocolDefTable=_ExtremeVlanProtocolDefTable_Object((1,3,6,1,4,1,1916,1,2,5,3))
if mibBuilder.loadTexts:extremeVlanProtocolDefTable.setStatus(_G)
_ExtremeVlanProtocolDefEntry_Object=MibTableRow
extremeVlanProtocolDefEntry=_ExtremeVlanProtocolDefEntry_Object((1,3,6,1,4,1,1916,1,2,5,3,1))
extremeVlanProtocolDefEntry.setIndexNames((0,_D,_Z),(0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:extremeVlanProtocolDefEntry.setStatus(_G)
class _ExtremeVlanProtocolDefName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeVlanProtocolDefName_Type.__name__=_F
_ExtremeVlanProtocolDefName_Object=MibTableColumn
extremeVlanProtocolDefName=_ExtremeVlanProtocolDefName_Object((1,3,6,1,4,1,1916,1,2,5,3,1,1),_ExtremeVlanProtocolDefName_Type())
extremeVlanProtocolDefName.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVlanProtocolDefName.setStatus(_G)
class _ExtremeVlanProtocolDefDllEncapsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('any',1),(_V,2),('llc',3),(_W,4),('none',5)))
_ExtremeVlanProtocolDefDllEncapsType_Type.__name__=_E
_ExtremeVlanProtocolDefDllEncapsType_Object=MibTableColumn
extremeVlanProtocolDefDllEncapsType=_ExtremeVlanProtocolDefDllEncapsType_Object((1,3,6,1,4,1,1916,1,2,5,3,1,2),_ExtremeVlanProtocolDefDllEncapsType_Type())
extremeVlanProtocolDefDllEncapsType.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVlanProtocolDefDllEncapsType.setStatus(_G)
class _ExtremeVlanProtocolDefValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeVlanProtocolDefValue_Type.__name__=_E
_ExtremeVlanProtocolDefValue_Object=MibTableColumn
extremeVlanProtocolDefValue=_ExtremeVlanProtocolDefValue_Object((1,3,6,1,4,1,1916,1,2,5,3,1,3),_ExtremeVlanProtocolDefValue_Type())
extremeVlanProtocolDefValue.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVlanProtocolDefValue.setStatus(_G)
_ExtremeVlanProtocolDefStatus_Type=RowStatus
_ExtremeVlanProtocolDefStatus_Object=MibTableColumn
extremeVlanProtocolDefStatus=_ExtremeVlanProtocolDefStatus_Object((1,3,6,1,4,1,1916,1,2,5,3,1,4),_ExtremeVlanProtocolDefStatus_Type())
extremeVlanProtocolDefStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanProtocolDefStatus.setStatus(_G)
_ExtremeVlanProtocolBindingTable_Object=MibTable
extremeVlanProtocolBindingTable=_ExtremeVlanProtocolBindingTable_Object((1,3,6,1,4,1,1916,1,2,5,4))
if mibBuilder.loadTexts:extremeVlanProtocolBindingTable.setStatus(_A)
_ExtremeVlanProtocolBindingEntry_Object=MibTableRow
extremeVlanProtocolBindingEntry=_ExtremeVlanProtocolBindingEntry_Object((1,3,6,1,4,1,1916,1,2,5,4,1))
extremeVlanProtocolBindingEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:extremeVlanProtocolBindingEntry.setStatus(_A)
_ExtremeVlanProtocolBindingIfIndex_Type=Integer32
_ExtremeVlanProtocolBindingIfIndex_Object=MibTableColumn
extremeVlanProtocolBindingIfIndex=_ExtremeVlanProtocolBindingIfIndex_Object((1,3,6,1,4,1,1916,1,2,5,4,1,1),_ExtremeVlanProtocolBindingIfIndex_Type())
extremeVlanProtocolBindingIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVlanProtocolBindingIfIndex.setStatus(_A)
class _ExtremeVlanProtocolBindingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeVlanProtocolBindingName_Type.__name__=_F
_ExtremeVlanProtocolBindingName_Object=MibTableColumn
extremeVlanProtocolBindingName=_ExtremeVlanProtocolBindingName_Object((1,3,6,1,4,1,1916,1,2,5,4,1,2),_ExtremeVlanProtocolBindingName_Type())
extremeVlanProtocolBindingName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanProtocolBindingName.setStatus(_A)
_ExtremeVlanProtocolBindingStatus_Type=RowStatus
_ExtremeVlanProtocolBindingStatus_Object=MibTableColumn
extremeVlanProtocolBindingStatus=_ExtremeVlanProtocolBindingStatus_Object((1,3,6,1,4,1,1916,1,2,5,4,1,3),_ExtremeVlanProtocolBindingStatus_Type())
extremeVlanProtocolBindingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanProtocolBindingStatus.setStatus(_A)
_ExtremeVlanOpaqueGroup_ObjectIdentity=ObjectIdentity
extremeVlanOpaqueGroup=_ExtremeVlanOpaqueGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,6))
_ExtremeVlanOpaqueTable_Object=MibTable
extremeVlanOpaqueTable=_ExtremeVlanOpaqueTable_Object((1,3,6,1,4,1,1916,1,2,6,1))
if mibBuilder.loadTexts:extremeVlanOpaqueTable.setStatus(_A)
_ExtremeVlanOpaqueEntry_Object=MibTableRow
extremeVlanOpaqueEntry=_ExtremeVlanOpaqueEntry_Object((1,3,6,1,4,1,1916,1,2,6,1,1))
extremeVlanOpaqueEntry.setIndexNames((0,_D,_H),(0,_L,_M))
if mibBuilder.loadTexts:extremeVlanOpaqueEntry.setStatus(_A)
_ExtremeVlanOpaqueTaggedPorts_Type=PortList
_ExtremeVlanOpaqueTaggedPorts_Object=MibTableColumn
extremeVlanOpaqueTaggedPorts=_ExtremeVlanOpaqueTaggedPorts_Object((1,3,6,1,4,1,1916,1,2,6,1,1,1),_ExtremeVlanOpaqueTaggedPorts_Type())
extremeVlanOpaqueTaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanOpaqueTaggedPorts.setStatus(_A)
_ExtremeVlanOpaqueUntaggedPorts_Type=PortList
_ExtremeVlanOpaqueUntaggedPorts_Object=MibTableColumn
extremeVlanOpaqueUntaggedPorts=_ExtremeVlanOpaqueUntaggedPorts_Object((1,3,6,1,4,1,1916,1,2,6,1,1,2),_ExtremeVlanOpaqueUntaggedPorts_Type())
extremeVlanOpaqueUntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanOpaqueUntaggedPorts.setStatus(_A)
_ExtremeVlanOpaqueTranslatedPorts_Type=PortList
_ExtremeVlanOpaqueTranslatedPorts_Object=MibTableColumn
extremeVlanOpaqueTranslatedPorts=_ExtremeVlanOpaqueTranslatedPorts_Object((1,3,6,1,4,1,1916,1,2,6,1,1,3),_ExtremeVlanOpaqueTranslatedPorts_Type())
extremeVlanOpaqueTranslatedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanOpaqueTranslatedPorts.setStatus(_A)
_ExtremeVlanOpaqueControlTable_Object=MibTable
extremeVlanOpaqueControlTable=_ExtremeVlanOpaqueControlTable_Object((1,3,6,1,4,1,1916,1,2,6,2))
if mibBuilder.loadTexts:extremeVlanOpaqueControlTable.setStatus(_A)
_ExtremeVlanOpaqueControlEntry_Object=MibTableRow
extremeVlanOpaqueControlEntry=_ExtremeVlanOpaqueControlEntry_Object((1,3,6,1,4,1,1916,1,2,6,2,1))
extremeVlanOpaqueControlEntry.setIndexNames((0,_D,_H),(0,_L,_M))
if mibBuilder.loadTexts:extremeVlanOpaqueControlEntry.setStatus(_A)
_ExtremeVlanOpaqueControlPorts_Type=PortList
_ExtremeVlanOpaqueControlPorts_Object=MibTableColumn
extremeVlanOpaqueControlPorts=_ExtremeVlanOpaqueControlPorts_Object((1,3,6,1,4,1,1916,1,2,6,2,1,1),_ExtremeVlanOpaqueControlPorts_Type())
extremeVlanOpaqueControlPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanOpaqueControlPorts.setStatus(_A)
class _ExtremeVlanOpaqueControlOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('addTagged',1),('addUntagged',2),('delete',3),('addTranslated',4)))
_ExtremeVlanOpaqueControlOperation_Type.__name__=_E
_ExtremeVlanOpaqueControlOperation_Object=MibTableColumn
extremeVlanOpaqueControlOperation=_ExtremeVlanOpaqueControlOperation_Object((1,3,6,1,4,1,1916,1,2,6,2,1,2),_ExtremeVlanOpaqueControlOperation_Type())
extremeVlanOpaqueControlOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanOpaqueControlOperation.setStatus(_A)
_ExtremeVlanOpaqueControlStatus_Type=RowStatus
_ExtremeVlanOpaqueControlStatus_Object=MibTableColumn
extremeVlanOpaqueControlStatus=_ExtremeVlanOpaqueControlStatus_Object((1,3,6,1,4,1,1916,1,2,6,2,1,3),_ExtremeVlanOpaqueControlStatus_Type())
extremeVlanOpaqueControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanOpaqueControlStatus.setStatus(_A)
_ExtremeVlanStackGroup_ObjectIdentity=ObjectIdentity
extremeVlanStackGroup=_ExtremeVlanStackGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,7))
_ExtremeVlanStackTable_Object=MibTable
extremeVlanStackTable=_ExtremeVlanStackTable_Object((1,3,6,1,4,1,1916,1,2,7,1))
if mibBuilder.loadTexts:extremeVlanStackTable.setStatus(_A)
_ExtremeVlanStackEntry_Object=MibTableRow
extremeVlanStackEntry=_ExtremeVlanStackEntry_Object((1,3,6,1,4,1,1916,1,2,7,1,1))
extremeVlanStackEntry.setIndexNames((0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:extremeVlanStackEntry.setStatus(_A)
_ExtremeVlanStackHigherLayer_Type=Integer32
_ExtremeVlanStackHigherLayer_Object=MibTableColumn
extremeVlanStackHigherLayer=_ExtremeVlanStackHigherLayer_Object((1,3,6,1,4,1,1916,1,2,7,1,1,1),_ExtremeVlanStackHigherLayer_Type())
extremeVlanStackHigherLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanStackHigherLayer.setStatus(_A)
_ExtremeVlanStackLowerLayer_Type=Integer32
_ExtremeVlanStackLowerLayer_Object=MibTableColumn
extremeVlanStackLowerLayer=_ExtremeVlanStackLowerLayer_Object((1,3,6,1,4,1,1916,1,2,7,1,1,2),_ExtremeVlanStackLowerLayer_Type())
extremeVlanStackLowerLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanStackLowerLayer.setStatus(_A)
_ExtremeVlanStatsGroup_ObjectIdentity=ObjectIdentity
extremeVlanStatsGroup=_ExtremeVlanStatsGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,8))
_ExtremeVlanL2StatsTable_Object=MibTable
extremeVlanL2StatsTable=_ExtremeVlanL2StatsTable_Object((1,3,6,1,4,1,1916,1,2,8,1))
if mibBuilder.loadTexts:extremeVlanL2StatsTable.setStatus(_A)
_ExtremeVlanL2StatsEntry_Object=MibTableRow
extremeVlanL2StatsEntry=_ExtremeVlanL2StatsEntry_Object((1,3,6,1,4,1,1916,1,2,8,1,1))
extremeVlanL2StatsEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:extremeVlanL2StatsEntry.setStatus(_A)
class _ExtremeVlanL2StatsIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVlanL2StatsIfDescr_Type.__name__=_F
_ExtremeVlanL2StatsIfDescr_Object=MibTableColumn
extremeVlanL2StatsIfDescr=_ExtremeVlanL2StatsIfDescr_Object((1,3,6,1,4,1,1916,1,2,8,1,1,1),_ExtremeVlanL2StatsIfDescr_Type())
extremeVlanL2StatsIfDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanL2StatsIfDescr.setStatus(_A)
_ExtremeVlanL2StatsPktsToCpu_Type=Counter64
_ExtremeVlanL2StatsPktsToCpu_Object=MibTableColumn
extremeVlanL2StatsPktsToCpu=_ExtremeVlanL2StatsPktsToCpu_Object((1,3,6,1,4,1,1916,1,2,8,1,1,2),_ExtremeVlanL2StatsPktsToCpu_Type())
extremeVlanL2StatsPktsToCpu.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanL2StatsPktsToCpu.setStatus(_A)
_ExtremeVlanL2StatsPktsLearnt_Type=Counter64
_ExtremeVlanL2StatsPktsLearnt_Object=MibTableColumn
extremeVlanL2StatsPktsLearnt=_ExtremeVlanL2StatsPktsLearnt_Object((1,3,6,1,4,1,1916,1,2,8,1,1,3),_ExtremeVlanL2StatsPktsLearnt_Type())
extremeVlanL2StatsPktsLearnt.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanL2StatsPktsLearnt.setStatus(_A)
_ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Type=Counter64
_ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Object=MibTableColumn
extremeVlanL2StatsIgmpCtrlPktsSnooped=_ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Object((1,3,6,1,4,1,1916,1,2,8,1,1,4),_ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Type())
extremeVlanL2StatsIgmpCtrlPktsSnooped.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanL2StatsIgmpCtrlPktsSnooped.setStatus(_A)
_ExtremeVlanL2StatsIgmpDataPktsSwitched_Type=Counter64
_ExtremeVlanL2StatsIgmpDataPktsSwitched_Object=MibTableColumn
extremeVlanL2StatsIgmpDataPktsSwitched=_ExtremeVlanL2StatsIgmpDataPktsSwitched_Object((1,3,6,1,4,1,1916,1,2,8,1,1,5),_ExtremeVlanL2StatsIgmpDataPktsSwitched_Type())
extremeVlanL2StatsIgmpDataPktsSwitched.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanL2StatsIgmpDataPktsSwitched.setStatus(_A)
_ExtremePortVlanStatsTable_Object=MibTable
extremePortVlanStatsTable=_ExtremePortVlanStatsTable_Object((1,3,6,1,4,1,1916,1,2,8,2))
if mibBuilder.loadTexts:extremePortVlanStatsTable.setStatus(_A)
_ExtremePortVlanStatsEntry_Object=MibTableRow
extremePortVlanStatsEntry=_ExtremePortVlanStatsEntry_Object((1,3,6,1,4,1,1916,1,2,8,2,1))
extremePortVlanStatsEntry.setIndexNames((0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:extremePortVlanStatsEntry.setStatus(_A)
_ExtremeStatsPortIfIndex_Type=Integer32
_ExtremeStatsPortIfIndex_Object=MibTableColumn
extremeStatsPortIfIndex=_ExtremeStatsPortIfIndex_Object((1,3,6,1,4,1,1916,1,2,8,2,1,1),_ExtremeStatsPortIfIndex_Type())
extremeStatsPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeStatsPortIfIndex.setStatus(_A)
class _ExtremeStatsVlanNameIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeStatsVlanNameIndex_Type.__name__=_F
_ExtremeStatsVlanNameIndex_Object=MibTableColumn
extremeStatsVlanNameIndex=_ExtremeStatsVlanNameIndex_Object((1,3,6,1,4,1,1916,1,2,8,2,1,2),_ExtremeStatsVlanNameIndex_Type())
extremeStatsVlanNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeStatsVlanNameIndex.setStatus(_A)
_ExtremePortVlanStatsCntrType_Type=Integer32
_ExtremePortVlanStatsCntrType_Object=MibTableColumn
extremePortVlanStatsCntrType=_ExtremePortVlanStatsCntrType_Object((1,3,6,1,4,1,1916,1,2,8,2,1,3),_ExtremePortVlanStatsCntrType_Type())
extremePortVlanStatsCntrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanStatsCntrType.setStatus(_A)
_ExtremePortVlanUnicastReceivedPacketsCounter_Type=Counter64
_ExtremePortVlanUnicastReceivedPacketsCounter_Object=MibTableColumn
extremePortVlanUnicastReceivedPacketsCounter=_ExtremePortVlanUnicastReceivedPacketsCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,4),_ExtremePortVlanUnicastReceivedPacketsCounter_Type())
extremePortVlanUnicastReceivedPacketsCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanUnicastReceivedPacketsCounter.setStatus(_A)
_ExtremePortVlanMulticastReceivedPacketsCounter_Type=Counter64
_ExtremePortVlanMulticastReceivedPacketsCounter_Object=MibTableColumn
extremePortVlanMulticastReceivedPacketsCounter=_ExtremePortVlanMulticastReceivedPacketsCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,5),_ExtremePortVlanMulticastReceivedPacketsCounter_Type())
extremePortVlanMulticastReceivedPacketsCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanMulticastReceivedPacketsCounter.setStatus(_A)
_ExtremePortVlanBroadcastReceivedPacketsCounter_Type=Counter64
_ExtremePortVlanBroadcastReceivedPacketsCounter_Object=MibTableColumn
extremePortVlanBroadcastReceivedPacketsCounter=_ExtremePortVlanBroadcastReceivedPacketsCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,6),_ExtremePortVlanBroadcastReceivedPacketsCounter_Type())
extremePortVlanBroadcastReceivedPacketsCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanBroadcastReceivedPacketsCounter.setStatus(_A)
_ExtremePortVlanTotalReceivedBytesCounter_Type=Counter64
_ExtremePortVlanTotalReceivedBytesCounter_Object=MibTableColumn
extremePortVlanTotalReceivedBytesCounter=_ExtremePortVlanTotalReceivedBytesCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,7),_ExtremePortVlanTotalReceivedBytesCounter_Type())
extremePortVlanTotalReceivedBytesCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanTotalReceivedBytesCounter.setStatus(_A)
_ExtremePortVlanTotalReceivedFramesCounter_Type=Counter64
_ExtremePortVlanTotalReceivedFramesCounter_Object=MibTableColumn
extremePortVlanTotalReceivedFramesCounter=_ExtremePortVlanTotalReceivedFramesCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,8),_ExtremePortVlanTotalReceivedFramesCounter_Type())
extremePortVlanTotalReceivedFramesCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanTotalReceivedFramesCounter.setStatus(_A)
_ExtremePortVlanUnicastTransmittedPacketsCounter_Type=Counter64
_ExtremePortVlanUnicastTransmittedPacketsCounter_Object=MibTableColumn
extremePortVlanUnicastTransmittedPacketsCounter=_ExtremePortVlanUnicastTransmittedPacketsCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,9),_ExtremePortVlanUnicastTransmittedPacketsCounter_Type())
extremePortVlanUnicastTransmittedPacketsCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanUnicastTransmittedPacketsCounter.setStatus(_A)
_ExtremePortVlanMulticastTransmittedPacketsCounter_Type=Counter64
_ExtremePortVlanMulticastTransmittedPacketsCounter_Object=MibTableColumn
extremePortVlanMulticastTransmittedPacketsCounter=_ExtremePortVlanMulticastTransmittedPacketsCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,10),_ExtremePortVlanMulticastTransmittedPacketsCounter_Type())
extremePortVlanMulticastTransmittedPacketsCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanMulticastTransmittedPacketsCounter.setStatus(_A)
_ExtremePortVlanBroadcastTransmittedPacketsCounter_Type=Counter64
_ExtremePortVlanBroadcastTransmittedPacketsCounter_Object=MibTableColumn
extremePortVlanBroadcastTransmittedPacketsCounter=_ExtremePortVlanBroadcastTransmittedPacketsCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,11),_ExtremePortVlanBroadcastTransmittedPacketsCounter_Type())
extremePortVlanBroadcastTransmittedPacketsCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanBroadcastTransmittedPacketsCounter.setStatus(_A)
_ExtremePortVlanTotalTransmittedBytesCounter_Type=Counter64
_ExtremePortVlanTotalTransmittedBytesCounter_Object=MibTableColumn
extremePortVlanTotalTransmittedBytesCounter=_ExtremePortVlanTotalTransmittedBytesCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,12),_ExtremePortVlanTotalTransmittedBytesCounter_Type())
extremePortVlanTotalTransmittedBytesCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanTotalTransmittedBytesCounter.setStatus(_A)
_ExtremePortVlanTotalTransmittedFramesCounter_Type=Counter64
_ExtremePortVlanTotalTransmittedFramesCounter_Object=MibTableColumn
extremePortVlanTotalTransmittedFramesCounter=_ExtremePortVlanTotalTransmittedFramesCounter_Object((1,3,6,1,4,1,1916,1,2,8,2,1,13),_ExtremePortVlanTotalTransmittedFramesCounter_Type())
extremePortVlanTotalTransmittedFramesCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePortVlanTotalTransmittedFramesCounter.setStatus(_A)
_ExtremePortConfigureVlanStatus_Type=RowStatus
_ExtremePortConfigureVlanStatus_Object=MibTableColumn
extremePortConfigureVlanStatus=_ExtremePortConfigureVlanStatus_Object((1,3,6,1,4,1,1916,1,2,8,2,1,14),_ExtremePortConfigureVlanStatus_Type())
extremePortConfigureVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortConfigureVlanStatus.setStatus(_A)
_ExtremeVlanAggregationGroup_ObjectIdentity=ObjectIdentity
extremeVlanAggregationGroup=_ExtremeVlanAggregationGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,9))
_ExtremeVlanAggregationTable_Object=MibTable
extremeVlanAggregationTable=_ExtremeVlanAggregationTable_Object((1,3,6,1,4,1,1916,1,2,9,1))
if mibBuilder.loadTexts:extremeVlanAggregationTable.setStatus(_A)
_ExtremeVlanAggregationEntry_Object=MibTableRow
extremeVlanAggregationEntry=_ExtremeVlanAggregationEntry_Object((1,3,6,1,4,1,1916,1,2,9,1,1))
extremeVlanAggregationEntry.setIndexNames((0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:extremeVlanAggregationEntry.setStatus(_A)
_ExtremeVlanAggregationSuperVlanIfIndex_Type=Integer32
_ExtremeVlanAggregationSuperVlanIfIndex_Object=MibTableColumn
extremeVlanAggregationSuperVlanIfIndex=_ExtremeVlanAggregationSuperVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,9,1,1,1),_ExtremeVlanAggregationSuperVlanIfIndex_Type())
extremeVlanAggregationSuperVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanAggregationSuperVlanIfIndex.setStatus(_A)
_ExtremeVlanAggregationSubVlanIfIndex_Type=Integer32
_ExtremeVlanAggregationSubVlanIfIndex_Object=MibTableColumn
extremeVlanAggregationSubVlanIfIndex=_ExtremeVlanAggregationSubVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,9,1,1,2),_ExtremeVlanAggregationSubVlanIfIndex_Type())
extremeVlanAggregationSubVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanAggregationSubVlanIfIndex.setStatus(_A)
_ExtremeVlanAggregationSubVlanStartIpNetAddress_Type=IpAddress
_ExtremeVlanAggregationSubVlanStartIpNetAddress_Object=MibTableColumn
extremeVlanAggregationSubVlanStartIpNetAddress=_ExtremeVlanAggregationSubVlanStartIpNetAddress_Object((1,3,6,1,4,1,1916,1,2,9,1,1,3),_ExtremeVlanAggregationSubVlanStartIpNetAddress_Type())
extremeVlanAggregationSubVlanStartIpNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanAggregationSubVlanStartIpNetAddress.setStatus(_A)
_ExtremeVlanAggregationSubVlanStartIpNetMask_Type=IpAddress
_ExtremeVlanAggregationSubVlanStartIpNetMask_Object=MibTableColumn
extremeVlanAggregationSubVlanStartIpNetMask=_ExtremeVlanAggregationSubVlanStartIpNetMask_Object((1,3,6,1,4,1,1916,1,2,9,1,1,4),_ExtremeVlanAggregationSubVlanStartIpNetMask_Type())
extremeVlanAggregationSubVlanStartIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanAggregationSubVlanStartIpNetMask.setStatus(_A)
_ExtremeVlanAggregationSubVlanEndIpNetAddress_Type=IpAddress
_ExtremeVlanAggregationSubVlanEndIpNetAddress_Object=MibTableColumn
extremeVlanAggregationSubVlanEndIpNetAddress=_ExtremeVlanAggregationSubVlanEndIpNetAddress_Object((1,3,6,1,4,1,1916,1,2,9,1,1,5),_ExtremeVlanAggregationSubVlanEndIpNetAddress_Type())
extremeVlanAggregationSubVlanEndIpNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanAggregationSubVlanEndIpNetAddress.setStatus(_A)
_ExtremeVlanAggregationSubVlanEndIpNetMask_Type=IpAddress
_ExtremeVlanAggregationSubVlanEndIpNetMask_Object=MibTableColumn
extremeVlanAggregationSubVlanEndIpNetMask=_ExtremeVlanAggregationSubVlanEndIpNetMask_Object((1,3,6,1,4,1,1916,1,2,9,1,1,6),_ExtremeVlanAggregationSubVlanEndIpNetMask_Type())
extremeVlanAggregationSubVlanEndIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanAggregationSubVlanEndIpNetMask.setStatus(_A)
_ExtremeVlanAggregationStatus_Type=RowStatus
_ExtremeVlanAggregationStatus_Object=MibTableColumn
extremeVlanAggregationStatus=_ExtremeVlanAggregationStatus_Object((1,3,6,1,4,1,1916,1,2,9,1,1,7),_ExtremeVlanAggregationStatus_Type())
extremeVlanAggregationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanAggregationStatus.setStatus(_A)
_ExtremeVlanAggregationConfigTable_Object=MibTable
extremeVlanAggregationConfigTable=_ExtremeVlanAggregationConfigTable_Object((1,3,6,1,4,1,1916,1,2,9,2))
if mibBuilder.loadTexts:extremeVlanAggregationConfigTable.setStatus(_A)
_ExtremeVlanAggregationConfigEntry_Object=MibTableRow
extremeVlanAggregationConfigEntry=_ExtremeVlanAggregationConfigEntry_Object((1,3,6,1,4,1,1916,1,2,9,2,1))
extremeVlanAggregationConfigEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:extremeVlanAggregationConfigEntry.setStatus(_A)
_ExtremeVlanAggregationConfigSuperVlanIfIndex_Type=Integer32
_ExtremeVlanAggregationConfigSuperVlanIfIndex_Object=MibTableColumn
extremeVlanAggregationConfigSuperVlanIfIndex=_ExtremeVlanAggregationConfigSuperVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,9,2,1,1),_ExtremeVlanAggregationConfigSuperVlanIfIndex_Type())
extremeVlanAggregationConfigSuperVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanAggregationConfigSuperVlanIfIndex.setStatus(_A)
_ExtremeVlanAggregationConfigSubVlanProxyEnable_Type=TruthValue
_ExtremeVlanAggregationConfigSubVlanProxyEnable_Object=MibTableColumn
extremeVlanAggregationConfigSubVlanProxyEnable=_ExtremeVlanAggregationConfigSubVlanProxyEnable_Object((1,3,6,1,4,1,1916,1,2,9,2,1,2),_ExtremeVlanAggregationConfigSubVlanProxyEnable_Type())
extremeVlanAggregationConfigSubVlanProxyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanAggregationConfigSubVlanProxyEnable.setStatus(_A)
_ExtremeVlanTranslationGroup_ObjectIdentity=ObjectIdentity
extremeVlanTranslationGroup=_ExtremeVlanTranslationGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,2,10))
_ExtremeVlanTranslationTable_Object=MibTable
extremeVlanTranslationTable=_ExtremeVlanTranslationTable_Object((1,3,6,1,4,1,1916,1,2,10,1))
if mibBuilder.loadTexts:extremeVlanTranslationTable.setStatus(_A)
_ExtremeVlanTranslationEntry_Object=MibTableRow
extremeVlanTranslationEntry=_ExtremeVlanTranslationEntry_Object((1,3,6,1,4,1,1916,1,2,10,1,1))
extremeVlanTranslationEntry.setIndexNames((0,_D,_k),(0,_D,_l))
if mibBuilder.loadTexts:extremeVlanTranslationEntry.setStatus(_A)
_ExtremeVlanTranslationSuperVlanIfIndex_Type=Integer32
_ExtremeVlanTranslationSuperVlanIfIndex_Object=MibTableColumn
extremeVlanTranslationSuperVlanIfIndex=_ExtremeVlanTranslationSuperVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,10,1,1,1),_ExtremeVlanTranslationSuperVlanIfIndex_Type())
extremeVlanTranslationSuperVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanTranslationSuperVlanIfIndex.setStatus(_A)
_ExtremeVlanTranslationMemberVlanIfIndex_Type=Integer32
_ExtremeVlanTranslationMemberVlanIfIndex_Object=MibTableColumn
extremeVlanTranslationMemberVlanIfIndex=_ExtremeVlanTranslationMemberVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,10,1,1,2),_ExtremeVlanTranslationMemberVlanIfIndex_Type())
extremeVlanTranslationMemberVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVlanTranslationMemberVlanIfIndex.setStatus(_A)
_ExtremeVlanTranslationStatus_Type=RowStatus
_ExtremeVlanTranslationStatus_Object=MibTableColumn
extremeVlanTranslationStatus=_ExtremeVlanTranslationStatus_Object((1,3,6,1,4,1,1916,1,2,10,1,1,3),_ExtremeVlanTranslationStatus_Type())
extremeVlanTranslationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeVlanTranslationStatus.setStatus(_A)
_ExtremePrivateVlan_ObjectIdentity=ObjectIdentity
extremePrivateVlan=_ExtremePrivateVlan_ObjectIdentity((1,3,6,1,4,1,1916,1,2,11))
_ExtremePvlanTable_Object=MibTable
extremePvlanTable=_ExtremePvlanTable_Object((1,3,6,1,4,1,1916,1,2,11,1))
if mibBuilder.loadTexts:extremePvlanTable.setStatus(_A)
_ExtremePvlanEntry_Object=MibTableRow
extremePvlanEntry=_ExtremePvlanEntry_Object((1,3,6,1,4,1,1916,1,2,11,1,1))
extremePvlanEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:extremePvlanEntry.setStatus(_A)
class _ExtremePvlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremePvlanName_Type.__name__=_F
_ExtremePvlanName_Object=MibTableColumn
extremePvlanName=_ExtremePvlanName_Object((1,3,6,1,4,1,1916,1,2,11,1,1,1),_ExtremePvlanName_Type())
extremePvlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanName.setStatus(_A)
class _ExtremePvlanVrName_Type(DisplayString):defaultValue=OctetString('VR-Default');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremePvlanVrName_Type.__name__=_F
_ExtremePvlanVrName_Object=MibTableColumn
extremePvlanVrName=_ExtremePvlanVrName_Object((1,3,6,1,4,1,1916,1,2,11,1,1,2),_ExtremePvlanVrName_Type())
extremePvlanVrName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanVrName.setStatus(_A)
class _ExtremePvlanNetworkVlanIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_ExtremePvlanNetworkVlanIfIndex_Type.__name__=_N
_ExtremePvlanNetworkVlanIfIndex_Object=MibTableColumn
extremePvlanNetworkVlanIfIndex=_ExtremePvlanNetworkVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,11,1,1,3),_ExtremePvlanNetworkVlanIfIndex_Type())
extremePvlanNetworkVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanNetworkVlanIfIndex.setStatus(_A)
_ExtremePvlanRowStatus_Type=RowStatus
_ExtremePvlanRowStatus_Object=MibTableColumn
extremePvlanRowStatus=_ExtremePvlanRowStatus_Object((1,3,6,1,4,1,1916,1,2,11,1,1,4),_ExtremePvlanRowStatus_Type())
extremePvlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanRowStatus.setStatus(_A)
_ExtremePvlanSubscriberTable_Object=MibTable
extremePvlanSubscriberTable=_ExtremePvlanSubscriberTable_Object((1,3,6,1,4,1,1916,1,2,11,2))
if mibBuilder.loadTexts:extremePvlanSubscriberTable.setStatus(_A)
_ExtremePvlanSubscriberEntry_Object=MibTableRow
extremePvlanSubscriberEntry=_ExtremePvlanSubscriberEntry_Object((1,3,6,1,4,1,1916,1,2,11,2,1))
extremePvlanSubscriberEntry.setIndexNames((0,_D,_O),(0,_D,_m))
if mibBuilder.loadTexts:extremePvlanSubscriberEntry.setStatus(_A)
_ExtremePvlanSubscriberVlanIfIndex_Type=InterfaceIndex
_ExtremePvlanSubscriberVlanIfIndex_Object=MibTableColumn
extremePvlanSubscriberVlanIfIndex=_ExtremePvlanSubscriberVlanIfIndex_Object((1,3,6,1,4,1,1916,1,2,11,2,1,1),_ExtremePvlanSubscriberVlanIfIndex_Type())
extremePvlanSubscriberVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanSubscriberVlanIfIndex.setStatus(_A)
class _ExtremePvlanSubscriberType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonIsolated',1),('isolated',2)))
_ExtremePvlanSubscriberType_Type.__name__=_E
_ExtremePvlanSubscriberType_Object=MibTableColumn
extremePvlanSubscriberType=_ExtremePvlanSubscriberType_Object((1,3,6,1,4,1,1916,1,2,11,2,1,2),_ExtremePvlanSubscriberType_Type())
extremePvlanSubscriberType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanSubscriberType.setStatus(_A)
class _ExtremePvlanSubscriberLoopBackPortIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_ExtremePvlanSubscriberLoopBackPortIfIndex_Type.__name__=_N
_ExtremePvlanSubscriberLoopBackPortIfIndex_Object=MibTableColumn
extremePvlanSubscriberLoopBackPortIfIndex=_ExtremePvlanSubscriberLoopBackPortIfIndex_Object((1,3,6,1,4,1,1916,1,2,11,2,1,3),_ExtremePvlanSubscriberLoopBackPortIfIndex_Type())
extremePvlanSubscriberLoopBackPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanSubscriberLoopBackPortIfIndex.setStatus(_A)
_ExtremePvlanSubscriberRowStatus_Type=RowStatus
_ExtremePvlanSubscriberRowStatus_Object=MibTableColumn
extremePvlanSubscriberRowStatus=_ExtremePvlanSubscriberRowStatus_Object((1,3,6,1,4,1,1916,1,2,11,2,1,4),_ExtremePvlanSubscriberRowStatus_Type())
extremePvlanSubscriberRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePvlanSubscriberRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ExtremeVlanType':ExtremeVlanType,'ExtremeVlanEncapsType':ExtremeVlanEncapsType,'extremeVlan':extremeVlan,'extremeVlanGroup':extremeVlanGroup,'extremeVlanGlobalMappingTable':extremeVlanGlobalMappingTable,'extremeVlanGlobalMappingEntry':extremeVlanGlobalMappingEntry,_R:extremeVlanGlobalMappingIdentifier,'extremeVlanGlobalMappingIfIndex':extremeVlanGlobalMappingIfIndex,'extremeVlanIfTable':extremeVlanIfTable,'extremeVlanIfEntry':extremeVlanIfEntry,_H:extremeVlanIfIndex,'extremeVlanIfDescr':extremeVlanIfDescr,'extremeVlanIfType':extremeVlanIfType,'extremeVlanIfGlobalIdentifier':extremeVlanIfGlobalIdentifier,'extremeVlanIfStatus':extremeVlanIfStatus,'extremeVlanIfIgnoreStpFlag':extremeVlanIfIgnoreStpFlag,'extremeVlanIfIgnoreBpduFlag':extremeVlanIfIgnoreBpduFlag,'extremeVlanIfLoopbackModeFlag':extremeVlanIfLoopbackModeFlag,'extremeVlanIfVlanId':extremeVlanIfVlanId,'extremeVlanIfEncapsType':extremeVlanIfEncapsType,'extremeVlanIfAdminStatus':extremeVlanIfAdminStatus,'extremeVirtualGroup':extremeVirtualGroup,'extremeNextAvailableVirtIfIndex':extremeNextAvailableVirtIfIndex,'extremeEncapsulationGroup':extremeEncapsulationGroup,'extremeVlanEncapsIfTable':extremeVlanEncapsIfTable,'extremeVlanEncapsIfEntry':extremeVlanEncapsIfEntry,_S:extremeVlanEncapsIfIndex,'extremeVlanEncapsIfType':extremeVlanEncapsIfType,'extremeVlanEncapsIfTag':extremeVlanEncapsIfTag,'extremeVlanEncapsIfStatus':extremeVlanEncapsIfStatus,'extremeVlanIpGroup':extremeVlanIpGroup,'extremeVlanIpTable':extremeVlanIpTable,'extremeVlanIpEntry':extremeVlanIpEntry,'extremeVlanIpNetAddress':extremeVlanIpNetAddress,'extremeVlanIpNetMask':extremeVlanIpNetMask,'extremeVlanIpStatus':extremeVlanIpStatus,'extremeVlanIpForwardingState':extremeVlanIpForwardingState,'extremeProtocolGroup':extremeProtocolGroup,'extremeVlanProtocolTable':extremeVlanProtocolTable,'extremeVlanProtocolEntry':extremeVlanProtocolEntry,_T:extremeVlanProtocolIndex,_U:extremeVlanProtocolIdIndex,'extremeVlanProtocolName':extremeVlanProtocolName,'extremeVlanProtocolDllEncapsType':extremeVlanProtocolDllEncapsType,'extremeVlanProtocolId':extremeVlanProtocolId,'extremeVlanProtocolStatus':extremeVlanProtocolStatus,'extremeVlanProtocolDestAddress':extremeVlanProtocolDestAddress,'extremeVlanProtocolDestAddressValid':extremeVlanProtocolDestAddressValid,'extremeVlanProtocolUserFieldOffset':extremeVlanProtocolUserFieldOffset,'extremeVlanProtocolUserFieldValue':extremeVlanProtocolUserFieldValue,'extremeVlanProtocolUserFieldMask':extremeVlanProtocolUserFieldMask,'extremeVlanProtocolVlanTable':extremeVlanProtocolVlanTable,'extremeVlanProtocolVlanEntry':extremeVlanProtocolVlanEntry,_X:extremeVlanProtocolVlanIfIndex,_Y:extremeVlanProtocolVlanProtocolIndex,'extremeVlanProtocolVlanStatus':extremeVlanProtocolVlanStatus,'extremeVlanProtocolDefTable':extremeVlanProtocolDefTable,'extremeVlanProtocolDefEntry':extremeVlanProtocolDefEntry,_Z:extremeVlanProtocolDefName,_a:extremeVlanProtocolDefDllEncapsType,_b:extremeVlanProtocolDefValue,'extremeVlanProtocolDefStatus':extremeVlanProtocolDefStatus,'extremeVlanProtocolBindingTable':extremeVlanProtocolBindingTable,'extremeVlanProtocolBindingEntry':extremeVlanProtocolBindingEntry,_c:extremeVlanProtocolBindingIfIndex,'extremeVlanProtocolBindingName':extremeVlanProtocolBindingName,'extremeVlanProtocolBindingStatus':extremeVlanProtocolBindingStatus,'extremeVlanOpaqueGroup':extremeVlanOpaqueGroup,'extremeVlanOpaqueTable':extremeVlanOpaqueTable,'extremeVlanOpaqueEntry':extremeVlanOpaqueEntry,'extremeVlanOpaqueTaggedPorts':extremeVlanOpaqueTaggedPorts,'extremeVlanOpaqueUntaggedPorts':extremeVlanOpaqueUntaggedPorts,'extremeVlanOpaqueTranslatedPorts':extremeVlanOpaqueTranslatedPorts,'extremeVlanOpaqueControlTable':extremeVlanOpaqueControlTable,'extremeVlanOpaqueControlEntry':extremeVlanOpaqueControlEntry,'extremeVlanOpaqueControlPorts':extremeVlanOpaqueControlPorts,'extremeVlanOpaqueControlOperation':extremeVlanOpaqueControlOperation,'extremeVlanOpaqueControlStatus':extremeVlanOpaqueControlStatus,'extremeVlanStackGroup':extremeVlanStackGroup,'extremeVlanStackTable':extremeVlanStackTable,'extremeVlanStackEntry':extremeVlanStackEntry,_d:extremeVlanStackHigherLayer,_e:extremeVlanStackLowerLayer,'extremeVlanStatsGroup':extremeVlanStatsGroup,'extremeVlanL2StatsTable':extremeVlanL2StatsTable,'extremeVlanL2StatsEntry':extremeVlanL2StatsEntry,'extremeVlanL2StatsIfDescr':extremeVlanL2StatsIfDescr,'extremeVlanL2StatsPktsToCpu':extremeVlanL2StatsPktsToCpu,'extremeVlanL2StatsPktsLearnt':extremeVlanL2StatsPktsLearnt,'extremeVlanL2StatsIgmpCtrlPktsSnooped':extremeVlanL2StatsIgmpCtrlPktsSnooped,'extremeVlanL2StatsIgmpDataPktsSwitched':extremeVlanL2StatsIgmpDataPktsSwitched,'extremePortVlanStatsTable':extremePortVlanStatsTable,'extremePortVlanStatsEntry':extremePortVlanStatsEntry,_f:extremeStatsPortIfIndex,_g:extremeStatsVlanNameIndex,'extremePortVlanStatsCntrType':extremePortVlanStatsCntrType,'extremePortVlanUnicastReceivedPacketsCounter':extremePortVlanUnicastReceivedPacketsCounter,'extremePortVlanMulticastReceivedPacketsCounter':extremePortVlanMulticastReceivedPacketsCounter,'extremePortVlanBroadcastReceivedPacketsCounter':extremePortVlanBroadcastReceivedPacketsCounter,'extremePortVlanTotalReceivedBytesCounter':extremePortVlanTotalReceivedBytesCounter,'extremePortVlanTotalReceivedFramesCounter':extremePortVlanTotalReceivedFramesCounter,'extremePortVlanUnicastTransmittedPacketsCounter':extremePortVlanUnicastTransmittedPacketsCounter,'extremePortVlanMulticastTransmittedPacketsCounter':extremePortVlanMulticastTransmittedPacketsCounter,'extremePortVlanBroadcastTransmittedPacketsCounter':extremePortVlanBroadcastTransmittedPacketsCounter,'extremePortVlanTotalTransmittedBytesCounter':extremePortVlanTotalTransmittedBytesCounter,'extremePortVlanTotalTransmittedFramesCounter':extremePortVlanTotalTransmittedFramesCounter,'extremePortConfigureVlanStatus':extremePortConfigureVlanStatus,'extremeVlanAggregationGroup':extremeVlanAggregationGroup,'extremeVlanAggregationTable':extremeVlanAggregationTable,'extremeVlanAggregationEntry':extremeVlanAggregationEntry,_h:extremeVlanAggregationSuperVlanIfIndex,_i:extremeVlanAggregationSubVlanIfIndex,'extremeVlanAggregationSubVlanStartIpNetAddress':extremeVlanAggregationSubVlanStartIpNetAddress,'extremeVlanAggregationSubVlanStartIpNetMask':extremeVlanAggregationSubVlanStartIpNetMask,'extremeVlanAggregationSubVlanEndIpNetAddress':extremeVlanAggregationSubVlanEndIpNetAddress,'extremeVlanAggregationSubVlanEndIpNetMask':extremeVlanAggregationSubVlanEndIpNetMask,'extremeVlanAggregationStatus':extremeVlanAggregationStatus,'extremeVlanAggregationConfigTable':extremeVlanAggregationConfigTable,'extremeVlanAggregationConfigEntry':extremeVlanAggregationConfigEntry,_j:extremeVlanAggregationConfigSuperVlanIfIndex,'extremeVlanAggregationConfigSubVlanProxyEnable':extremeVlanAggregationConfigSubVlanProxyEnable,'extremeVlanTranslationGroup':extremeVlanTranslationGroup,'extremeVlanTranslationTable':extremeVlanTranslationTable,'extremeVlanTranslationEntry':extremeVlanTranslationEntry,_k:extremeVlanTranslationSuperVlanIfIndex,_l:extremeVlanTranslationMemberVlanIfIndex,'extremeVlanTranslationStatus':extremeVlanTranslationStatus,'extremePrivateVlan':extremePrivateVlan,'extremePvlanTable':extremePvlanTable,'extremePvlanEntry':extremePvlanEntry,_O:extremePvlanName,'extremePvlanVrName':extremePvlanVrName,'extremePvlanNetworkVlanIfIndex':extremePvlanNetworkVlanIfIndex,'extremePvlanRowStatus':extremePvlanRowStatus,'extremePvlanSubscriberTable':extremePvlanSubscriberTable,'extremePvlanSubscriberEntry':extremePvlanSubscriberEntry,_m:extremePvlanSubscriberVlanIfIndex,'extremePvlanSubscriberType':extremePvlanSubscriberType,'extremePvlanSubscriberLoopBackPortIfIndex':extremePvlanSubscriberLoopBackPortIfIndex,'extremePvlanSubscriberRowStatus':extremePvlanSubscriberRowStatus})