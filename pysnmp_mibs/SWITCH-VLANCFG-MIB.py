_K='rcVlanCfgStaticIndex'
_J='rcMgmtVlanIndex'
_I='rcVlanPriorityIndex'
_H='rcPortIndex'
_G='SWITCH-SYSTEM-MIB'
_F='not-accessible'
_E='SWITCH-VLANCFG-MIB'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rcPortIndex,=mibBuilder.importSymbols(_G,_H)
EnableVar,Vlanset=mibBuilder.importSymbols('SWITCH-TC','EnableVar','Vlanset')
rcVlanCfg=ModuleIdentity((1,3,6,1,4,1,8886,6,1,43))
_RcVlanCfgMibObjects_ObjectIdentity=ObjectIdentity
rcVlanCfgMibObjects=_RcVlanCfgMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,43,1))
_RcVlanCfgConfig_ObjectIdentity=ObjectIdentity
rcVlanCfgConfig=_RcVlanCfgConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,43,1,1))
class _RcVlanCfgSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transparent',1),('dot1q-vlan',2)))
_RcVlanCfgSwitchMode_Type.__name__=_B
_RcVlanCfgSwitchMode_Object=MibScalar
rcVlanCfgSwitchMode=_RcVlanCfgSwitchMode_Object((1,3,6,1,4,1,8886,6,1,43,1,1,1),_RcVlanCfgSwitchMode_Type())
rcVlanCfgSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcVlanCfgSwitchMode.setStatus(_A)
_RcVlanCfgPort_ObjectIdentity=ObjectIdentity
rcVlanCfgPort=_RcVlanCfgPort_ObjectIdentity((1,3,6,1,4,1,8886,6,1,43,1,2))
_RcVlanCfgPortTable_Object=MibTable
rcVlanCfgPortTable=_RcVlanCfgPortTable_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1))
if mibBuilder.loadTexts:rcVlanCfgPortTable.setStatus(_A)
_RcVlanCfgPortEntry_Object=MibTableRow
rcVlanCfgPortEntry=_RcVlanCfgPortEntry_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1))
rcVlanCfgPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:rcVlanCfgPortEntry.setStatus(_A)
class _RcPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('access',1),('trunk',2)))
_RcPortMode_Type.__name__=_B
_RcPortMode_Object=MibTableColumn
rcPortMode=_RcPortMode_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,1),_RcPortMode_Type())
rcPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortMode.setStatus(_A)
class _RcPortAccessVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcPortAccessVlanId_Type.__name__=_B
_RcPortAccessVlanId_Object=MibTableColumn
rcPortAccessVlanId=_RcPortAccessVlanId_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,2),_RcPortAccessVlanId_Type())
rcPortAccessVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortAccessVlanId.setStatus(_A)
_RcPortAccessPvidOverride_Type=EnableVar
_RcPortAccessPvidOverride_Object=MibTableColumn
rcPortAccessPvidOverride=_RcPortAccessPvidOverride_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,3),_RcPortAccessPvidOverride_Type())
rcPortAccessPvidOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortAccessPvidOverride.setStatus(_A)
_RcPortAccessEgressVlanList_Type=Vlanset
_RcPortAccessEgressVlanList_Object=MibTableColumn
rcPortAccessEgressVlanList=_RcPortAccessEgressVlanList_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,4),_RcPortAccessEgressVlanList_Type())
rcPortAccessEgressVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortAccessEgressVlanList.setStatus(_A)
class _RcPortTrunkVlanNative_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcPortTrunkVlanNative_Type.__name__=_B
_RcPortTrunkVlanNative_Object=MibTableColumn
rcPortTrunkVlanNative=_RcPortTrunkVlanNative_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,5),_RcPortTrunkVlanNative_Type())
rcPortTrunkVlanNative.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortTrunkVlanNative.setStatus(_A)
_RcPortTrunkAllowVlanList_Type=Vlanset
_RcPortTrunkAllowVlanList_Object=MibTableColumn
rcPortTrunkAllowVlanList=_RcPortTrunkAllowVlanList_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,6),_RcPortTrunkAllowVlanList_Type())
rcPortTrunkAllowVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortTrunkAllowVlanList.setStatus(_A)
_RcPortTrunkUntagVlanList_Type=Vlanset
_RcPortTrunkUntagVlanList_Object=MibTableColumn
rcPortTrunkUntagVlanList=_RcPortTrunkUntagVlanList_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,7),_RcPortTrunkUntagVlanList_Type())
rcPortTrunkUntagVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortTrunkUntagVlanList.setStatus(_A)
class _RcPortRejectFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('tagged',2),('untagged',3),('taggedAndUntagged',4)))
_RcPortRejectFrameType_Type.__name__=_B
_RcPortRejectFrameType_Object=MibTableColumn
rcPortRejectFrameType=_RcPortRejectFrameType_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,8),_RcPortRejectFrameType_Type())
rcPortRejectFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortRejectFrameType.setStatus(_A)
class _RcPortVlanMappingMissMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard',1),('forwarding',2)))
_RcPortVlanMappingMissMode_Type.__name__=_B
_RcPortVlanMappingMissMode_Object=MibTableColumn
rcPortVlanMappingMissMode=_RcPortVlanMappingMissMode_Object((1,3,6,1,4,1,8886,6,1,43,1,2,1,1,9),_RcPortVlanMappingMissMode_Type())
rcPortVlanMappingMissMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortVlanMappingMissMode.setStatus(_A)
_RcVlanCfgPriority_ObjectIdentity=ObjectIdentity
rcVlanCfgPriority=_RcVlanCfgPriority_ObjectIdentity((1,3,6,1,4,1,8886,6,1,43,1,3))
_RcVlanCfgPriorityTable_Object=MibTable
rcVlanCfgPriorityTable=_RcVlanCfgPriorityTable_Object((1,3,6,1,4,1,8886,6,1,43,1,3,2))
if mibBuilder.loadTexts:rcVlanCfgPriorityTable.setStatus(_A)
_RcVlanCfgPriorityEntry_Object=MibTableRow
rcVlanCfgPriorityEntry=_RcVlanCfgPriorityEntry_Object((1,3,6,1,4,1,8886,6,1,43,1,3,2,1))
rcVlanCfgPriorityEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:rcVlanCfgPriorityEntry.setStatus(_A)
class _RcVlanPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcVlanPriorityIndex_Type.__name__=_B
_RcVlanPriorityIndex_Object=MibTableColumn
rcVlanPriorityIndex=_RcVlanPriorityIndex_Object((1,3,6,1,4,1,8886,6,1,43,1,3,2,1,1),_RcVlanPriorityIndex_Type())
rcVlanPriorityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcVlanPriorityIndex.setStatus(_A)
class _RcVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_RcVlanPriority_Type.__name__=_B
_RcVlanPriority_Object=MibTableColumn
rcVlanPriority=_RcVlanPriority_Object((1,3,6,1,4,1,8886,6,1,43,1,3,2,1,2),_RcVlanPriority_Type())
rcVlanPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanPriority.setStatus(_A)
_RcVlanPriorityRowStatus_Type=RowStatus
_RcVlanPriorityRowStatus_Object=MibTableColumn
rcVlanPriorityRowStatus=_RcVlanPriorityRowStatus_Object((1,3,6,1,4,1,8886,6,1,43,1,3,2,1,3),_RcVlanPriorityRowStatus_Type())
rcVlanPriorityRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanPriorityRowStatus.setStatus(_A)
class _RcVlanFidVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcVlanFidVlan_Type.__name__=_B
_RcVlanFidVlan_Object=MibTableColumn
rcVlanFidVlan=_RcVlanFidVlan_Object((1,3,6,1,4,1,8886,6,1,43,1,3,2,1,4),_RcVlanFidVlan_Type())
rcVlanFidVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanFidVlan.setStatus(_A)
_RcVlanCfgMgmt_ObjectIdentity=ObjectIdentity
rcVlanCfgMgmt=_RcVlanCfgMgmt_ObjectIdentity((1,3,6,1,4,1,8886,6,1,43,1,4))
_RcMgmtVlanTable_Object=MibTable
rcMgmtVlanTable=_RcMgmtVlanTable_Object((1,3,6,1,4,1,8886,6,1,43,1,4,1))
if mibBuilder.loadTexts:rcMgmtVlanTable.setStatus(_A)
_RcMgmtVlanEntry_Object=MibTableRow
rcMgmtVlanEntry=_RcMgmtVlanEntry_Object((1,3,6,1,4,1,8886,6,1,43,1,4,1,1))
rcMgmtVlanEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:rcMgmtVlanEntry.setStatus(_A)
class _RcMgmtVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcMgmtVlanIndex_Type.__name__=_B
_RcMgmtVlanIndex_Object=MibTableColumn
rcMgmtVlanIndex=_RcMgmtVlanIndex_Object((1,3,6,1,4,1,8886,6,1,43,1,4,1,1,1),_RcMgmtVlanIndex_Type())
rcMgmtVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMgmtVlanIndex.setStatus(_A)
class _RcMgmtVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('termination',2)))
_RcMgmtVlanMode_Type.__name__=_B
_RcMgmtVlanMode_Object=MibTableColumn
rcMgmtVlanMode=_RcMgmtVlanMode_Object((1,3,6,1,4,1,8886,6,1,43,1,4,1,1,2),_RcMgmtVlanMode_Type())
rcMgmtVlanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcMgmtVlanMode.setStatus(_A)
_RcMgmtVlanRowStatus_Type=RowStatus
_RcMgmtVlanRowStatus_Object=MibTableColumn
rcMgmtVlanRowStatus=_RcMgmtVlanRowStatus_Object((1,3,6,1,4,1,8886,6,1,43,1,4,1,1,3),_RcMgmtVlanRowStatus_Type())
rcMgmtVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcMgmtVlanRowStatus.setStatus(_A)
_RcVlanCfgAttribute_ObjectIdentity=ObjectIdentity
rcVlanCfgAttribute=_RcVlanCfgAttribute_ObjectIdentity((1,3,6,1,4,1,8886,6,1,43,1,5))
_RcVlanCfgStaticTable_Object=MibTable
rcVlanCfgStaticTable=_RcVlanCfgStaticTable_Object((1,3,6,1,4,1,8886,6,1,43,1,5,1))
if mibBuilder.loadTexts:rcVlanCfgStaticTable.setStatus(_A)
_RcVlanCfgStaticEntry_Object=MibTableRow
rcVlanCfgStaticEntry=_RcVlanCfgStaticEntry_Object((1,3,6,1,4,1,8886,6,1,43,1,5,1,1))
rcVlanCfgStaticEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:rcVlanCfgStaticEntry.setStatus(_A)
class _RcVlanCfgStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcVlanCfgStaticIndex_Type.__name__=_B
_RcVlanCfgStaticIndex_Object=MibTableColumn
rcVlanCfgStaticIndex=_RcVlanCfgStaticIndex_Object((1,3,6,1,4,1,8886,6,1,43,1,5,1,1,1),_RcVlanCfgStaticIndex_Type())
rcVlanCfgStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcVlanCfgStaticIndex.setStatus(_A)
class _RcVlanCfgStaticBeCustomerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_RcVlanCfgStaticBeCustomerVlan_Type.__name__=_B
_RcVlanCfgStaticBeCustomerVlan_Object=MibTableColumn
rcVlanCfgStaticBeCustomerVlan=_RcVlanCfgStaticBeCustomerVlan_Object((1,3,6,1,4,1,8886,6,1,43,1,5,1,1,2),_RcVlanCfgStaticBeCustomerVlan_Type())
rcVlanCfgStaticBeCustomerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:rcVlanCfgStaticBeCustomerVlan.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rcVlanCfg':rcVlanCfg,'rcVlanCfgMibObjects':rcVlanCfgMibObjects,'rcVlanCfgConfig':rcVlanCfgConfig,'rcVlanCfgSwitchMode':rcVlanCfgSwitchMode,'rcVlanCfgPort':rcVlanCfgPort,'rcVlanCfgPortTable':rcVlanCfgPortTable,'rcVlanCfgPortEntry':rcVlanCfgPortEntry,'rcPortMode':rcPortMode,'rcPortAccessVlanId':rcPortAccessVlanId,'rcPortAccessPvidOverride':rcPortAccessPvidOverride,'rcPortAccessEgressVlanList':rcPortAccessEgressVlanList,'rcPortTrunkVlanNative':rcPortTrunkVlanNative,'rcPortTrunkAllowVlanList':rcPortTrunkAllowVlanList,'rcPortTrunkUntagVlanList':rcPortTrunkUntagVlanList,'rcPortRejectFrameType':rcPortRejectFrameType,'rcPortVlanMappingMissMode':rcPortVlanMappingMissMode,'rcVlanCfgPriority':rcVlanCfgPriority,'rcVlanCfgPriorityTable':rcVlanCfgPriorityTable,'rcVlanCfgPriorityEntry':rcVlanCfgPriorityEntry,_I:rcVlanPriorityIndex,'rcVlanPriority':rcVlanPriority,'rcVlanPriorityRowStatus':rcVlanPriorityRowStatus,'rcVlanFidVlan':rcVlanFidVlan,'rcVlanCfgMgmt':rcVlanCfgMgmt,'rcMgmtVlanTable':rcMgmtVlanTable,'rcMgmtVlanEntry':rcMgmtVlanEntry,_J:rcMgmtVlanIndex,'rcMgmtVlanMode':rcMgmtVlanMode,'rcMgmtVlanRowStatus':rcMgmtVlanRowStatus,'rcVlanCfgAttribute':rcVlanCfgAttribute,'rcVlanCfgStaticTable':rcVlanCfgStaticTable,'rcVlanCfgStaticEntry':rcVlanCfgStaticEntry,_K:rcVlanCfgStaticIndex,'rcVlanCfgStaticBeCustomerVlan':rcVlanCfgStaticBeCustomerVlan})