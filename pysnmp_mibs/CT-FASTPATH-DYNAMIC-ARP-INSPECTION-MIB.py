_M='ctAgentDaiVlanStatsIndex'
_L='not-accessible'
_K='ctAgentDaiVlanIndex'
_J='DisplayString'
_I='Integer32'
_H='ifIndex'
_G='IF-MIB'
_F='CT-FASTPATH-DYNAMIC-ARP-INSPECTION-MIB'
_E='Unsigned32'
_D='TruthValue'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDynamicArpInspectionExpMib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDynamicArpInspectionExpMib')
ifIndex,=mibBuilder.importSymbols(_G,_H)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention',_D)
ctFastPathDynamicArpInspectionMIB=ModuleIdentity((1,3,6,1,4,1,52,4,2,36,1))
_CtAgentDaiConfigGroup_ObjectIdentity=ObjectIdentity
ctAgentDaiConfigGroup=_CtAgentDaiConfigGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,36,1,1))
class _CtAgentDaiSrcMacValidate_Type(TruthValue):defaultValue=2
_CtAgentDaiSrcMacValidate_Type.__name__=_D
_CtAgentDaiSrcMacValidate_Object=MibScalar
ctAgentDaiSrcMacValidate=_CtAgentDaiSrcMacValidate_Object((1,3,6,1,4,1,52,4,2,36,1,1,1),_CtAgentDaiSrcMacValidate_Type())
ctAgentDaiSrcMacValidate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiSrcMacValidate.setStatus(_A)
class _CtAgentDaiDstMacValidate_Type(TruthValue):defaultValue=2
_CtAgentDaiDstMacValidate_Type.__name__=_D
_CtAgentDaiDstMacValidate_Object=MibScalar
ctAgentDaiDstMacValidate=_CtAgentDaiDstMacValidate_Object((1,3,6,1,4,1,52,4,2,36,1,1,2),_CtAgentDaiDstMacValidate_Type())
ctAgentDaiDstMacValidate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiDstMacValidate.setStatus(_A)
class _CtAgentDaiIPValidate_Type(TruthValue):defaultValue=2
_CtAgentDaiIPValidate_Type.__name__=_D
_CtAgentDaiIPValidate_Object=MibScalar
ctAgentDaiIPValidate=_CtAgentDaiIPValidate_Object((1,3,6,1,4,1,52,4,2,36,1,1,3),_CtAgentDaiIPValidate_Type())
ctAgentDaiIPValidate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiIPValidate.setStatus(_A)
_CtAgentDaiVlanConfigTable_Object=MibTable
ctAgentDaiVlanConfigTable=_CtAgentDaiVlanConfigTable_Object((1,3,6,1,4,1,52,4,2,36,1,1,4))
if mibBuilder.loadTexts:ctAgentDaiVlanConfigTable.setStatus(_A)
_CtAgentDaiVlanConfigEntry_Object=MibTableRow
ctAgentDaiVlanConfigEntry=_CtAgentDaiVlanConfigEntry_Object((1,3,6,1,4,1,52,4,2,36,1,1,4,1))
ctAgentDaiVlanConfigEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:ctAgentDaiVlanConfigEntry.setStatus(_A)
_CtAgentDaiVlanIndex_Type=VlanIndex
_CtAgentDaiVlanIndex_Object=MibTableColumn
ctAgentDaiVlanIndex=_CtAgentDaiVlanIndex_Object((1,3,6,1,4,1,52,4,2,36,1,1,4,1,1),_CtAgentDaiVlanIndex_Type())
ctAgentDaiVlanIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:ctAgentDaiVlanIndex.setStatus(_A)
class _CtAgentDaiVlanDynArpInspEnable_Type(TruthValue):defaultValue=2
_CtAgentDaiVlanDynArpInspEnable_Type.__name__=_D
_CtAgentDaiVlanDynArpInspEnable_Object=MibTableColumn
ctAgentDaiVlanDynArpInspEnable=_CtAgentDaiVlanDynArpInspEnable_Object((1,3,6,1,4,1,52,4,2,36,1,1,4,1,2),_CtAgentDaiVlanDynArpInspEnable_Type())
ctAgentDaiVlanDynArpInspEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiVlanDynArpInspEnable.setStatus(_A)
class _CtAgentDaiVlanLoggingEnable_Type(TruthValue):defaultValue=1
_CtAgentDaiVlanLoggingEnable_Type.__name__=_D
_CtAgentDaiVlanLoggingEnable_Object=MibTableColumn
ctAgentDaiVlanLoggingEnable=_CtAgentDaiVlanLoggingEnable_Object((1,3,6,1,4,1,52,4,2,36,1,1,4,1,3),_CtAgentDaiVlanLoggingEnable_Type())
ctAgentDaiVlanLoggingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiVlanLoggingEnable.setStatus(_A)
class _CtAgentDaiVlanArpAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CtAgentDaiVlanArpAclName_Type.__name__=_J
_CtAgentDaiVlanArpAclName_Object=MibTableColumn
ctAgentDaiVlanArpAclName=_CtAgentDaiVlanArpAclName_Object((1,3,6,1,4,1,52,4,2,36,1,1,4,1,4),_CtAgentDaiVlanArpAclName_Type())
ctAgentDaiVlanArpAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiVlanArpAclName.setStatus(_A)
class _CtAgentDaiVlanArpAclStaticFlag_Type(TruthValue):defaultValue=2
_CtAgentDaiVlanArpAclStaticFlag_Type.__name__=_D
_CtAgentDaiVlanArpAclStaticFlag_Object=MibTableColumn
ctAgentDaiVlanArpAclStaticFlag=_CtAgentDaiVlanArpAclStaticFlag_Object((1,3,6,1,4,1,52,4,2,36,1,1,4,1,5),_CtAgentDaiVlanArpAclStaticFlag_Type())
ctAgentDaiVlanArpAclStaticFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiVlanArpAclStaticFlag.setStatus(_A)
class _CtAagentDaiStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
_CtAagentDaiStatsReset_Type.__name__=_I
_CtAagentDaiStatsReset_Object=MibScalar
ctAagentDaiStatsReset=_CtAagentDaiStatsReset_Object((1,3,6,1,4,1,52,4,2,36,1,1,5),_CtAagentDaiStatsReset_Type())
ctAagentDaiStatsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAagentDaiStatsReset.setStatus(_A)
_CtAgentDaiVlanStatsTable_Object=MibTable
ctAgentDaiVlanStatsTable=_CtAgentDaiVlanStatsTable_Object((1,3,6,1,4,1,52,4,2,36,1,1,6))
if mibBuilder.loadTexts:ctAgentDaiVlanStatsTable.setStatus(_A)
_CtAgentDaiVlanStatsEntry_Object=MibTableRow
ctAgentDaiVlanStatsEntry=_CtAgentDaiVlanStatsEntry_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1))
ctAgentDaiVlanStatsEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:ctAgentDaiVlanStatsEntry.setStatus(_A)
_CtAgentDaiVlanStatsIndex_Type=VlanIndex
_CtAgentDaiVlanStatsIndex_Object=MibTableColumn
ctAgentDaiVlanStatsIndex=_CtAgentDaiVlanStatsIndex_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,1),_CtAgentDaiVlanStatsIndex_Type())
ctAgentDaiVlanStatsIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:ctAgentDaiVlanStatsIndex.setStatus(_A)
_CtAgentDaiVlanPktsForwarded_Type=Counter32
_CtAgentDaiVlanPktsForwarded_Object=MibTableColumn
ctAgentDaiVlanPktsForwarded=_CtAgentDaiVlanPktsForwarded_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,2),_CtAgentDaiVlanPktsForwarded_Type())
ctAgentDaiVlanPktsForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanPktsForwarded.setStatus(_A)
_CtAgentDaiVlanPktsDropped_Type=Counter32
_CtAgentDaiVlanPktsDropped_Object=MibTableColumn
ctAgentDaiVlanPktsDropped=_CtAgentDaiVlanPktsDropped_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,3),_CtAgentDaiVlanPktsDropped_Type())
ctAgentDaiVlanPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanPktsDropped.setStatus(_A)
_CtAgentDaiVlanDhcpDrops_Type=Counter32
_CtAgentDaiVlanDhcpDrops_Object=MibTableColumn
ctAgentDaiVlanDhcpDrops=_CtAgentDaiVlanDhcpDrops_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,4),_CtAgentDaiVlanDhcpDrops_Type())
ctAgentDaiVlanDhcpDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanDhcpDrops.setStatus(_A)
_CtAgentDaiVlanDhcpPermits_Type=Counter32
_CtAgentDaiVlanDhcpPermits_Object=MibTableColumn
ctAgentDaiVlanDhcpPermits=_CtAgentDaiVlanDhcpPermits_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,5),_CtAgentDaiVlanDhcpPermits_Type())
ctAgentDaiVlanDhcpPermits.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanDhcpPermits.setStatus(_A)
_CtAgentDaiVlanAclDrops_Type=Counter32
_CtAgentDaiVlanAclDrops_Object=MibTableColumn
ctAgentDaiVlanAclDrops=_CtAgentDaiVlanAclDrops_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,6),_CtAgentDaiVlanAclDrops_Type())
ctAgentDaiVlanAclDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanAclDrops.setStatus(_A)
_CtAgentDaiVlanAclPermits_Type=Counter32
_CtAgentDaiVlanAclPermits_Object=MibTableColumn
ctAgentDaiVlanAclPermits=_CtAgentDaiVlanAclPermits_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,7),_CtAgentDaiVlanAclPermits_Type())
ctAgentDaiVlanAclPermits.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanAclPermits.setStatus(_A)
_CtAgentDaiVlanSrcMacFailures_Type=Counter32
_CtAgentDaiVlanSrcMacFailures_Object=MibTableColumn
ctAgentDaiVlanSrcMacFailures=_CtAgentDaiVlanSrcMacFailures_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,8),_CtAgentDaiVlanSrcMacFailures_Type())
ctAgentDaiVlanSrcMacFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanSrcMacFailures.setStatus(_A)
_CtAgentDaiVlanDstMacFailures_Type=Counter32
_CtAgentDaiVlanDstMacFailures_Object=MibTableColumn
ctAgentDaiVlanDstMacFailures=_CtAgentDaiVlanDstMacFailures_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,9),_CtAgentDaiVlanDstMacFailures_Type())
ctAgentDaiVlanDstMacFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanDstMacFailures.setStatus(_A)
_CtAgentDaiVlanIpValidFailures_Type=Counter32
_CtAgentDaiVlanIpValidFailures_Object=MibTableColumn
ctAgentDaiVlanIpValidFailures=_CtAgentDaiVlanIpValidFailures_Object((1,3,6,1,4,1,52,4,2,36,1,1,6,1,10),_CtAgentDaiVlanIpValidFailures_Type())
ctAgentDaiVlanIpValidFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDaiVlanIpValidFailures.setStatus(_A)
_CtAgentDaiIfConfigTable_Object=MibTable
ctAgentDaiIfConfigTable=_CtAgentDaiIfConfigTable_Object((1,3,6,1,4,1,52,4,2,36,1,1,7))
if mibBuilder.loadTexts:ctAgentDaiIfConfigTable.setStatus(_A)
_CtAgentDaiIfConfigEntry_Object=MibTableRow
ctAgentDaiIfConfigEntry=_CtAgentDaiIfConfigEntry_Object((1,3,6,1,4,1,52,4,2,36,1,1,7,1))
ctAgentDaiIfConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ctAgentDaiIfConfigEntry.setStatus(_A)
class _CtAgentDaiIfTrustEnable_Type(TruthValue):defaultValue=2
_CtAgentDaiIfTrustEnable_Type.__name__=_D
_CtAgentDaiIfTrustEnable_Object=MibTableColumn
ctAgentDaiIfTrustEnable=_CtAgentDaiIfTrustEnable_Object((1,3,6,1,4,1,52,4,2,36,1,1,7,1,1),_CtAgentDaiIfTrustEnable_Type())
ctAgentDaiIfTrustEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiIfTrustEnable.setStatus(_A)
class _CtAgentDaiIfRateLimit_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_CtAgentDaiIfRateLimit_Type.__name__=_E
_CtAgentDaiIfRateLimit_Object=MibTableColumn
ctAgentDaiIfRateLimit=_CtAgentDaiIfRateLimit_Object((1,3,6,1,4,1,52,4,2,36,1,1,7,1,2),_CtAgentDaiIfRateLimit_Type())
ctAgentDaiIfRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiIfRateLimit.setStatus(_A)
if mibBuilder.loadTexts:ctAgentDaiIfRateLimit.setUnits('packets per second')
class _CtAgentDaiIfBurstInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CtAgentDaiIfBurstInterval_Type.__name__=_E
_CtAgentDaiIfBurstInterval_Object=MibTableColumn
ctAgentDaiIfBurstInterval=_CtAgentDaiIfBurstInterval_Object((1,3,6,1,4,1,52,4,2,36,1,1,7,1,3),_CtAgentDaiIfBurstInterval_Type())
ctAgentDaiIfBurstInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDaiIfBurstInterval.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ctFastPathDynamicArpInspectionMIB':ctFastPathDynamicArpInspectionMIB,'ctAgentDaiConfigGroup':ctAgentDaiConfigGroup,'ctAgentDaiSrcMacValidate':ctAgentDaiSrcMacValidate,'ctAgentDaiDstMacValidate':ctAgentDaiDstMacValidate,'ctAgentDaiIPValidate':ctAgentDaiIPValidate,'ctAgentDaiVlanConfigTable':ctAgentDaiVlanConfigTable,'ctAgentDaiVlanConfigEntry':ctAgentDaiVlanConfigEntry,_K:ctAgentDaiVlanIndex,'ctAgentDaiVlanDynArpInspEnable':ctAgentDaiVlanDynArpInspEnable,'ctAgentDaiVlanLoggingEnable':ctAgentDaiVlanLoggingEnable,'ctAgentDaiVlanArpAclName':ctAgentDaiVlanArpAclName,'ctAgentDaiVlanArpAclStaticFlag':ctAgentDaiVlanArpAclStaticFlag,'ctAagentDaiStatsReset':ctAagentDaiStatsReset,'ctAgentDaiVlanStatsTable':ctAgentDaiVlanStatsTable,'ctAgentDaiVlanStatsEntry':ctAgentDaiVlanStatsEntry,_M:ctAgentDaiVlanStatsIndex,'ctAgentDaiVlanPktsForwarded':ctAgentDaiVlanPktsForwarded,'ctAgentDaiVlanPktsDropped':ctAgentDaiVlanPktsDropped,'ctAgentDaiVlanDhcpDrops':ctAgentDaiVlanDhcpDrops,'ctAgentDaiVlanDhcpPermits':ctAgentDaiVlanDhcpPermits,'ctAgentDaiVlanAclDrops':ctAgentDaiVlanAclDrops,'ctAgentDaiVlanAclPermits':ctAgentDaiVlanAclPermits,'ctAgentDaiVlanSrcMacFailures':ctAgentDaiVlanSrcMacFailures,'ctAgentDaiVlanDstMacFailures':ctAgentDaiVlanDstMacFailures,'ctAgentDaiVlanIpValidFailures':ctAgentDaiVlanIpValidFailures,'ctAgentDaiIfConfigTable':ctAgentDaiIfConfigTable,'ctAgentDaiIfConfigEntry':ctAgentDaiIfConfigEntry,'ctAgentDaiIfTrustEnable':ctAgentDaiIfTrustEnable,'ctAgentDaiIfRateLimit':ctAgentDaiIfRateLimit,'ctAgentDaiIfBurstInterval':ctAgentDaiIfBurstInterval})