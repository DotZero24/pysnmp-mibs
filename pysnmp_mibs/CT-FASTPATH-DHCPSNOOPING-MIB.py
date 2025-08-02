_M='ctAgentDynamicDsBindingMacAddr'
_L='ctAgentStaticDsBindingMacAddr'
_K='ctAgentDhcpSnoopingVlanIndex'
_J='Integer32'
_I='Unsigned32'
_H='CT-FASTPATH-DHCPSNOOPING-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='TruthValue'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDhcpSnoopingExpMib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDhcpSnoopingExpMib')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention',_D)
ctFastPathDHCPSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,52,4,2,35,1))
_CtAgentDhcpSnoopingConfigGroup_ObjectIdentity=ObjectIdentity
ctAgentDhcpSnoopingConfigGroup=_CtAgentDhcpSnoopingConfigGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,35,1,1))
class _CtAgentDhcpSnoopingAdminMode_Type(TruthValue):defaultValue=2
_CtAgentDhcpSnoopingAdminMode_Type.__name__=_D
_CtAgentDhcpSnoopingAdminMode_Object=MibScalar
ctAgentDhcpSnoopingAdminMode=_CtAgentDhcpSnoopingAdminMode_Object((1,3,6,1,4,1,52,4,2,35,1,1,1),_CtAgentDhcpSnoopingAdminMode_Type())
ctAgentDhcpSnoopingAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingAdminMode.setStatus(_A)
class _CtAgentDhcpSnoopingVerifyMac_Type(TruthValue):defaultValue=2
_CtAgentDhcpSnoopingVerifyMac_Type.__name__=_D
_CtAgentDhcpSnoopingVerifyMac_Object=MibScalar
ctAgentDhcpSnoopingVerifyMac=_CtAgentDhcpSnoopingVerifyMac_Object((1,3,6,1,4,1,52,4,2,35,1,1,2),_CtAgentDhcpSnoopingVerifyMac_Type())
ctAgentDhcpSnoopingVerifyMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingVerifyMac.setStatus(_A)
_CtAgentDhcpSnoopingVlanConfigTable_Object=MibTable
ctAgentDhcpSnoopingVlanConfigTable=_CtAgentDhcpSnoopingVlanConfigTable_Object((1,3,6,1,4,1,52,4,2,35,1,1,3))
if mibBuilder.loadTexts:ctAgentDhcpSnoopingVlanConfigTable.setStatus(_A)
_CtAgentDhcpSnoopingVlanConfigEntry_Object=MibTableRow
ctAgentDhcpSnoopingVlanConfigEntry=_CtAgentDhcpSnoopingVlanConfigEntry_Object((1,3,6,1,4,1,52,4,2,35,1,1,3,1))
ctAgentDhcpSnoopingVlanConfigEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:ctAgentDhcpSnoopingVlanConfigEntry.setStatus(_A)
_CtAgentDhcpSnoopingVlanIndex_Type=VlanIndex
_CtAgentDhcpSnoopingVlanIndex_Object=MibTableColumn
ctAgentDhcpSnoopingVlanIndex=_CtAgentDhcpSnoopingVlanIndex_Object((1,3,6,1,4,1,52,4,2,35,1,1,3,1,1),_CtAgentDhcpSnoopingVlanIndex_Type())
ctAgentDhcpSnoopingVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ctAgentDhcpSnoopingVlanIndex.setStatus(_A)
class _CtAgentDhcpSnoopingVlanEnable_Type(TruthValue):defaultValue=2
_CtAgentDhcpSnoopingVlanEnable_Type.__name__=_D
_CtAgentDhcpSnoopingVlanEnable_Object=MibTableColumn
ctAgentDhcpSnoopingVlanEnable=_CtAgentDhcpSnoopingVlanEnable_Object((1,3,6,1,4,1,52,4,2,35,1,1,3,1,2),_CtAgentDhcpSnoopingVlanEnable_Type())
ctAgentDhcpSnoopingVlanEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingVlanEnable.setStatus(_A)
_CtAgentDhcpSnoopingIfConfigTable_Object=MibTable
ctAgentDhcpSnoopingIfConfigTable=_CtAgentDhcpSnoopingIfConfigTable_Object((1,3,6,1,4,1,52,4,2,35,1,1,4))
if mibBuilder.loadTexts:ctAgentDhcpSnoopingIfConfigTable.setStatus(_A)
_CtAgentDhcpSnoopingIfConfigEntry_Object=MibTableRow
ctAgentDhcpSnoopingIfConfigEntry=_CtAgentDhcpSnoopingIfConfigEntry_Object((1,3,6,1,4,1,52,4,2,35,1,1,4,1))
ctAgentDhcpSnoopingIfConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctAgentDhcpSnoopingIfConfigEntry.setStatus(_A)
class _CtAgentDhcpSnoopingIfTrustEnable_Type(TruthValue):defaultValue=2
_CtAgentDhcpSnoopingIfTrustEnable_Type.__name__=_D
_CtAgentDhcpSnoopingIfTrustEnable_Object=MibTableColumn
ctAgentDhcpSnoopingIfTrustEnable=_CtAgentDhcpSnoopingIfTrustEnable_Object((1,3,6,1,4,1,52,4,2,35,1,1,4,1,1),_CtAgentDhcpSnoopingIfTrustEnable_Type())
ctAgentDhcpSnoopingIfTrustEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingIfTrustEnable.setStatus(_A)
class _CtAgentDhcpSnoopingIfLogEnable_Type(TruthValue):defaultValue=2
_CtAgentDhcpSnoopingIfLogEnable_Type.__name__=_D
_CtAgentDhcpSnoopingIfLogEnable_Object=MibTableColumn
ctAgentDhcpSnoopingIfLogEnable=_CtAgentDhcpSnoopingIfLogEnable_Object((1,3,6,1,4,1,52,4,2,35,1,1,4,1,2),_CtAgentDhcpSnoopingIfLogEnable_Type())
ctAgentDhcpSnoopingIfLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingIfLogEnable.setStatus(_A)
class _CtAgentDhcpSnoopingIfRateLimit_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_CtAgentDhcpSnoopingIfRateLimit_Type.__name__=_I
_CtAgentDhcpSnoopingIfRateLimit_Object=MibTableColumn
ctAgentDhcpSnoopingIfRateLimit=_CtAgentDhcpSnoopingIfRateLimit_Object((1,3,6,1,4,1,52,4,2,35,1,1,4,1,3),_CtAgentDhcpSnoopingIfRateLimit_Type())
ctAgentDhcpSnoopingIfRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingIfRateLimit.setStatus(_A)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingIfRateLimit.setUnits('packets per second')
class _CtAgentDhcpSnoopingIfBurstInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CtAgentDhcpSnoopingIfBurstInterval_Type.__name__=_I
_CtAgentDhcpSnoopingIfBurstInterval_Object=MibTableColumn
ctAgentDhcpSnoopingIfBurstInterval=_CtAgentDhcpSnoopingIfBurstInterval_Object((1,3,6,1,4,1,52,4,2,35,1,1,4,1,4),_CtAgentDhcpSnoopingIfBurstInterval_Type())
ctAgentDhcpSnoopingIfBurstInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingIfBurstInterval.setStatus(_A)
class _CtAgentDhcpSnoopingStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
_CtAgentDhcpSnoopingStatsReset_Type.__name__=_J
_CtAgentDhcpSnoopingStatsReset_Object=MibScalar
ctAgentDhcpSnoopingStatsReset=_CtAgentDhcpSnoopingStatsReset_Object((1,3,6,1,4,1,52,4,2,35,1,1,6),_CtAgentDhcpSnoopingStatsReset_Type())
ctAgentDhcpSnoopingStatsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingStatsReset.setStatus(_A)
_CtAgentDhcpSnoopingStatsTable_Object=MibTable
ctAgentDhcpSnoopingStatsTable=_CtAgentDhcpSnoopingStatsTable_Object((1,3,6,1,4,1,52,4,2,35,1,1,7))
if mibBuilder.loadTexts:ctAgentDhcpSnoopingStatsTable.setStatus(_A)
_CtAgentDhcpSnoopingStatsEntry_Object=MibTableRow
ctAgentDhcpSnoopingStatsEntry=_CtAgentDhcpSnoopingStatsEntry_Object((1,3,6,1,4,1,52,4,2,35,1,1,7,1))
ctAgentDhcpSnoopingStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctAgentDhcpSnoopingStatsEntry.setStatus(_A)
_CtAgentDhcpSnoopingMacVerifyFailures_Type=Counter32
_CtAgentDhcpSnoopingMacVerifyFailures_Object=MibTableColumn
ctAgentDhcpSnoopingMacVerifyFailures=_CtAgentDhcpSnoopingMacVerifyFailures_Object((1,3,6,1,4,1,52,4,2,35,1,1,7,1,1),_CtAgentDhcpSnoopingMacVerifyFailures_Type())
ctAgentDhcpSnoopingMacVerifyFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingMacVerifyFailures.setStatus(_A)
_CtAgentDhcpSnoopingInvalidClientMessages_Type=Counter32
_CtAgentDhcpSnoopingInvalidClientMessages_Object=MibTableColumn
ctAgentDhcpSnoopingInvalidClientMessages=_CtAgentDhcpSnoopingInvalidClientMessages_Object((1,3,6,1,4,1,52,4,2,35,1,1,7,1,2),_CtAgentDhcpSnoopingInvalidClientMessages_Type())
ctAgentDhcpSnoopingInvalidClientMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingInvalidClientMessages.setStatus(_A)
_CtAgentDhcpSnoopingInvalidServerMessages_Type=Counter32
_CtAgentDhcpSnoopingInvalidServerMessages_Object=MibTableColumn
ctAgentDhcpSnoopingInvalidServerMessages=_CtAgentDhcpSnoopingInvalidServerMessages_Object((1,3,6,1,4,1,52,4,2,35,1,1,7,1,3),_CtAgentDhcpSnoopingInvalidServerMessages_Type())
ctAgentDhcpSnoopingInvalidServerMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpSnoopingInvalidServerMessages.setStatus(_A)
_CtAgentStaticDsBindingTable_Object=MibTable
ctAgentStaticDsBindingTable=_CtAgentStaticDsBindingTable_Object((1,3,6,1,4,1,52,4,2,35,1,1,10))
if mibBuilder.loadTexts:ctAgentStaticDsBindingTable.setStatus(_A)
_CtAgentStaticDsBinding_Object=MibTableRow
ctAgentStaticDsBinding=_CtAgentStaticDsBinding_Object((1,3,6,1,4,1,52,4,2,35,1,1,10,1))
ctAgentStaticDsBinding.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:ctAgentStaticDsBinding.setStatus(_A)
_CtAgentStaticDsBindingIfIndex_Type=InterfaceIndex
_CtAgentStaticDsBindingIfIndex_Object=MibTableColumn
ctAgentStaticDsBindingIfIndex=_CtAgentStaticDsBindingIfIndex_Object((1,3,6,1,4,1,52,4,2,35,1,1,10,1,1),_CtAgentStaticDsBindingIfIndex_Type())
ctAgentStaticDsBindingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAgentStaticDsBindingIfIndex.setStatus(_A)
_CtAgentStaticDsBindingVlanId_Type=VlanIndex
_CtAgentStaticDsBindingVlanId_Object=MibTableColumn
ctAgentStaticDsBindingVlanId=_CtAgentStaticDsBindingVlanId_Object((1,3,6,1,4,1,52,4,2,35,1,1,10,1,2),_CtAgentStaticDsBindingVlanId_Type())
ctAgentStaticDsBindingVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAgentStaticDsBindingVlanId.setStatus(_A)
_CtAgentStaticDsBindingMacAddr_Type=MacAddress
_CtAgentStaticDsBindingMacAddr_Object=MibTableColumn
ctAgentStaticDsBindingMacAddr=_CtAgentStaticDsBindingMacAddr_Object((1,3,6,1,4,1,52,4,2,35,1,1,10,1,3),_CtAgentStaticDsBindingMacAddr_Type())
ctAgentStaticDsBindingMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAgentStaticDsBindingMacAddr.setStatus(_A)
_CtAgentStaticDsBindingIpAddr_Type=IpAddress
_CtAgentStaticDsBindingIpAddr_Object=MibTableColumn
ctAgentStaticDsBindingIpAddr=_CtAgentStaticDsBindingIpAddr_Object((1,3,6,1,4,1,52,4,2,35,1,1,10,1,4),_CtAgentStaticDsBindingIpAddr_Type())
ctAgentStaticDsBindingIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAgentStaticDsBindingIpAddr.setStatus(_A)
_CtAgentStaticDsBindingRowStatus_Type=RowStatus
_CtAgentStaticDsBindingRowStatus_Object=MibTableColumn
ctAgentStaticDsBindingRowStatus=_CtAgentStaticDsBindingRowStatus_Object((1,3,6,1,4,1,52,4,2,35,1,1,10,1,5),_CtAgentStaticDsBindingRowStatus_Type())
ctAgentStaticDsBindingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAgentStaticDsBindingRowStatus.setStatus(_A)
_CtAgentDynamicDsBindingTable_Object=MibTable
ctAgentDynamicDsBindingTable=_CtAgentDynamicDsBindingTable_Object((1,3,6,1,4,1,52,4,2,35,1,1,11))
if mibBuilder.loadTexts:ctAgentDynamicDsBindingTable.setStatus(_A)
_CtAgentDynamicDsBinding_Object=MibTableRow
ctAgentDynamicDsBinding=_CtAgentDynamicDsBinding_Object((1,3,6,1,4,1,52,4,2,35,1,1,11,11))
ctAgentDynamicDsBinding.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:ctAgentDynamicDsBinding.setStatus(_A)
_CtAgentDynamicDsBindingIfIndex_Type=InterfaceIndex
_CtAgentDynamicDsBindingIfIndex_Object=MibTableColumn
ctAgentDynamicDsBindingIfIndex=_CtAgentDynamicDsBindingIfIndex_Object((1,3,6,1,4,1,52,4,2,35,1,1,11,11,1),_CtAgentDynamicDsBindingIfIndex_Type())
ctAgentDynamicDsBindingIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDynamicDsBindingIfIndex.setStatus(_A)
_CtAgentDynamicDsBindingVlanId_Type=VlanIndex
_CtAgentDynamicDsBindingVlanId_Object=MibTableColumn
ctAgentDynamicDsBindingVlanId=_CtAgentDynamicDsBindingVlanId_Object((1,3,6,1,4,1,52,4,2,35,1,1,11,11,2),_CtAgentDynamicDsBindingVlanId_Type())
ctAgentDynamicDsBindingVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDynamicDsBindingVlanId.setStatus(_A)
_CtAgentDynamicDsBindingMacAddr_Type=MacAddress
_CtAgentDynamicDsBindingMacAddr_Object=MibTableColumn
ctAgentDynamicDsBindingMacAddr=_CtAgentDynamicDsBindingMacAddr_Object((1,3,6,1,4,1,52,4,2,35,1,1,11,11,3),_CtAgentDynamicDsBindingMacAddr_Type())
ctAgentDynamicDsBindingMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDynamicDsBindingMacAddr.setStatus(_A)
_CtAgentDynamicDsBindingIpAddr_Type=IpAddress
_CtAgentDynamicDsBindingIpAddr_Object=MibTableColumn
ctAgentDynamicDsBindingIpAddr=_CtAgentDynamicDsBindingIpAddr_Object((1,3,6,1,4,1,52,4,2,35,1,1,11,11,4),_CtAgentDynamicDsBindingIpAddr_Type())
ctAgentDynamicDsBindingIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDynamicDsBindingIpAddr.setStatus(_A)
ctDhcpSnoopingIntfErrorDisabledTrap=NotificationType((1,3,6,1,4,1,52,4,2,35,1,1,12))
ctDhcpSnoopingIntfErrorDisabledTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:ctDhcpSnoopingIntfErrorDisabledTrap.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'ctFastPathDHCPSnoopingMIB':ctFastPathDHCPSnoopingMIB,'ctAgentDhcpSnoopingConfigGroup':ctAgentDhcpSnoopingConfigGroup,'ctAgentDhcpSnoopingAdminMode':ctAgentDhcpSnoopingAdminMode,'ctAgentDhcpSnoopingVerifyMac':ctAgentDhcpSnoopingVerifyMac,'ctAgentDhcpSnoopingVlanConfigTable':ctAgentDhcpSnoopingVlanConfigTable,'ctAgentDhcpSnoopingVlanConfigEntry':ctAgentDhcpSnoopingVlanConfigEntry,_K:ctAgentDhcpSnoopingVlanIndex,'ctAgentDhcpSnoopingVlanEnable':ctAgentDhcpSnoopingVlanEnable,'ctAgentDhcpSnoopingIfConfigTable':ctAgentDhcpSnoopingIfConfigTable,'ctAgentDhcpSnoopingIfConfigEntry':ctAgentDhcpSnoopingIfConfigEntry,'ctAgentDhcpSnoopingIfTrustEnable':ctAgentDhcpSnoopingIfTrustEnable,'ctAgentDhcpSnoopingIfLogEnable':ctAgentDhcpSnoopingIfLogEnable,'ctAgentDhcpSnoopingIfRateLimit':ctAgentDhcpSnoopingIfRateLimit,'ctAgentDhcpSnoopingIfBurstInterval':ctAgentDhcpSnoopingIfBurstInterval,'ctAgentDhcpSnoopingStatsReset':ctAgentDhcpSnoopingStatsReset,'ctAgentDhcpSnoopingStatsTable':ctAgentDhcpSnoopingStatsTable,'ctAgentDhcpSnoopingStatsEntry':ctAgentDhcpSnoopingStatsEntry,'ctAgentDhcpSnoopingMacVerifyFailures':ctAgentDhcpSnoopingMacVerifyFailures,'ctAgentDhcpSnoopingInvalidClientMessages':ctAgentDhcpSnoopingInvalidClientMessages,'ctAgentDhcpSnoopingInvalidServerMessages':ctAgentDhcpSnoopingInvalidServerMessages,'ctAgentStaticDsBindingTable':ctAgentStaticDsBindingTable,'ctAgentStaticDsBinding':ctAgentStaticDsBinding,'ctAgentStaticDsBindingIfIndex':ctAgentStaticDsBindingIfIndex,'ctAgentStaticDsBindingVlanId':ctAgentStaticDsBindingVlanId,_L:ctAgentStaticDsBindingMacAddr,'ctAgentStaticDsBindingIpAddr':ctAgentStaticDsBindingIpAddr,'ctAgentStaticDsBindingRowStatus':ctAgentStaticDsBindingRowStatus,'ctAgentDynamicDsBindingTable':ctAgentDynamicDsBindingTable,'ctAgentDynamicDsBinding':ctAgentDynamicDsBinding,'ctAgentDynamicDsBindingIfIndex':ctAgentDynamicDsBindingIfIndex,'ctAgentDynamicDsBindingVlanId':ctAgentDynamicDsBindingVlanId,_M:ctAgentDynamicDsBindingMacAddr,'ctAgentDynamicDsBindingIpAddr':ctAgentDynamicDsBindingIpAddr,'ctDhcpSnoopingIntfErrorDisabledTrap':ctDhcpSnoopingIntfErrorDisabledTrap})