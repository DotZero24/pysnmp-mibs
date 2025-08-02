_W='ctTrunkFlowDiagnosticGroup'
_V='ctTrunkConfGroupV10'
_U='ctTrunkFlowDiagnosticInstalledFlows'
_T='ctTrunkMaxTrunks'
_S='ctTrunkLLAPRequirement'
_R='ctTrunkPortRemoteIfIndex'
_Q='ctTrunkIfIndex'
_P='ctTrunkConfigLoadBalance'
_O='ctTrunkConfigProtocol'
_N='ctTrunkConfigName'
_M='ctTrunkRowStatus'
_L='ctTrunkGlobalStatus'
_K='CTSmartTrunkLoadBalanceType'
_J='CTSmartTrunkProtocol'
_I='CTSmartTrunkName'
_H='Integer32'
_G='ctTrunkIndex'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='read-only'
_B='CTRON-SMARTTRUNK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctSmartTrunkBranch,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctSmartTrunkBranch')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ctSmartTrunk=ModuleIdentity((1,3,6,1,4,1,52,4,1,2,20,1))
class CTSmartTrunkProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noProtocol',1),('decHuntGroup',2)))
class CTSmartTrunkIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class CTSmartTrunkName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class CTSmartTrunkLoadBalanceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('balancingUnspecified',1),('roundRobin',2),('linkUtilization',3)))
_CtSmartTrunkConfig_ObjectIdentity=ObjectIdentity
ctSmartTrunkConfig=_CtSmartTrunkConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,20,1,1))
_CtTrunkGlobalStatus_Type=TruthValue
_CtTrunkGlobalStatus_Object=MibScalar
ctTrunkGlobalStatus=_CtTrunkGlobalStatus_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,1),_CtTrunkGlobalStatus_Type())
ctTrunkGlobalStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctTrunkGlobalStatus.setStatus(_A)
_CtTrunkConfigTable_Object=MibTable
ctTrunkConfigTable=_CtTrunkConfigTable_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3))
if mibBuilder.loadTexts:ctTrunkConfigTable.setStatus(_A)
_CtTrunkConfigEntry_Object=MibTableRow
ctTrunkConfigEntry=_CtTrunkConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3,1))
ctTrunkConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ctTrunkConfigEntry.setStatus(_A)
_CtTrunkIndex_Type=CTSmartTrunkIndex
_CtTrunkIndex_Object=MibTableColumn
ctTrunkIndex=_CtTrunkIndex_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3,1,1),_CtTrunkIndex_Type())
ctTrunkIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ctTrunkIndex.setStatus(_A)
class _CtTrunkConfigName_Type(CTSmartTrunkName):defaultValue=OctetString('')
_CtTrunkConfigName_Type.__name__=_I
_CtTrunkConfigName_Object=MibTableColumn
ctTrunkConfigName=_CtTrunkConfigName_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3,1,2),_CtTrunkConfigName_Type())
ctTrunkConfigName.setMaxAccess(_D)
if mibBuilder.loadTexts:ctTrunkConfigName.setStatus(_A)
class _CtTrunkConfigProtocol_Type(CTSmartTrunkProtocol):defaultValue=2
_CtTrunkConfigProtocol_Type.__name__=_J
_CtTrunkConfigProtocol_Object=MibTableColumn
ctTrunkConfigProtocol=_CtTrunkConfigProtocol_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3,1,3),_CtTrunkConfigProtocol_Type())
ctTrunkConfigProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ctTrunkConfigProtocol.setStatus(_A)
class _CtTrunkConfigLoadBalance_Type(CTSmartTrunkLoadBalanceType):defaultValue=1
_CtTrunkConfigLoadBalance_Type.__name__=_K
_CtTrunkConfigLoadBalance_Object=MibTableColumn
ctTrunkConfigLoadBalance=_CtTrunkConfigLoadBalance_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3,1,4),_CtTrunkConfigLoadBalance_Type())
ctTrunkConfigLoadBalance.setMaxAccess(_D)
if mibBuilder.loadTexts:ctTrunkConfigLoadBalance.setStatus(_A)
_CtTrunkIfIndex_Type=InterfaceIndex
_CtTrunkIfIndex_Object=MibTableColumn
ctTrunkIfIndex=_CtTrunkIfIndex_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3,1,5),_CtTrunkIfIndex_Type())
ctTrunkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTrunkIfIndex.setStatus(_A)
_CtTrunkRowStatus_Type=RowStatus
_CtTrunkRowStatus_Object=MibTableColumn
ctTrunkRowStatus=_CtTrunkRowStatus_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,3,1,6),_CtTrunkRowStatus_Type())
ctTrunkRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctTrunkRowStatus.setStatus(_A)
_CtTrunkConnectionTable_Object=MibTable
ctTrunkConnectionTable=_CtTrunkConnectionTable_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,4))
if mibBuilder.loadTexts:ctTrunkConnectionTable.setStatus(_A)
_CtTrunkConnectionEntry_Object=MibTableRow
ctTrunkConnectionEntry=_CtTrunkConnectionEntry_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,4,1))
ctTrunkConnectionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ctTrunkConnectionEntry.setStatus(_A)
_CtTrunkPortRemoteIfIndex_Type=InterfaceIndex
_CtTrunkPortRemoteIfIndex_Object=MibTableColumn
ctTrunkPortRemoteIfIndex=_CtTrunkPortRemoteIfIndex_Object((1,3,6,1,4,1,52,4,1,2,20,1,1,4,1,1),_CtTrunkPortRemoteIfIndex_Type())
ctTrunkPortRemoteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTrunkPortRemoteIfIndex.setStatus(_A)
_CtSmartTrunkDebug_ObjectIdentity=ObjectIdentity
ctSmartTrunkDebug=_CtSmartTrunkDebug_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,20,1,2))
class _CtTrunkLLAPRequirement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('required',1),('notRequired',2)))
_CtTrunkLLAPRequirement_Type.__name__=_H
_CtTrunkLLAPRequirement_Object=MibScalar
ctTrunkLLAPRequirement=_CtTrunkLLAPRequirement_Object((1,3,6,1,4,1,52,4,1,2,20,1,2,1),_CtTrunkLLAPRequirement_Type())
ctTrunkLLAPRequirement.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTrunkLLAPRequirement.setStatus(_A)
_CtTrunkMaxTrunks_Type=Integer32
_CtTrunkMaxTrunks_Object=MibScalar
ctTrunkMaxTrunks=_CtTrunkMaxTrunks_Object((1,3,6,1,4,1,52,4,1,2,20,1,2,2),_CtTrunkMaxTrunks_Type())
ctTrunkMaxTrunks.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTrunkMaxTrunks.setStatus(_A)
_CtTrunkFlowDiagnosticTable_Object=MibTable
ctTrunkFlowDiagnosticTable=_CtTrunkFlowDiagnosticTable_Object((1,3,6,1,4,1,52,4,1,2,20,1,2,4))
if mibBuilder.loadTexts:ctTrunkFlowDiagnosticTable.setStatus(_A)
_CtTrunkFlowDiagnosticEntry_Object=MibTableRow
ctTrunkFlowDiagnosticEntry=_CtTrunkFlowDiagnosticEntry_Object((1,3,6,1,4,1,52,4,1,2,20,1,2,4,1))
ctTrunkFlowDiagnosticEntry.setIndexNames((0,_B,_G),(0,_E,_F))
if mibBuilder.loadTexts:ctTrunkFlowDiagnosticEntry.setStatus(_A)
_CtTrunkFlowDiagnosticInstalledFlows_Type=Counter32
_CtTrunkFlowDiagnosticInstalledFlows_Object=MibTableColumn
ctTrunkFlowDiagnosticInstalledFlows=_CtTrunkFlowDiagnosticInstalledFlows_Object((1,3,6,1,4,1,52,4,1,2,20,1,2,4,1,1),_CtTrunkFlowDiagnosticInstalledFlows_Type())
ctTrunkFlowDiagnosticInstalledFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTrunkFlowDiagnosticInstalledFlows.setStatus(_A)
_CtTrunkConformance_ObjectIdentity=ObjectIdentity
ctTrunkConformance=_CtTrunkConformance_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,20,1,3))
_CtTrunkCompliances_ObjectIdentity=ObjectIdentity
ctTrunkCompliances=_CtTrunkCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,20,1,3,1))
_CtTrunkGroups_ObjectIdentity=ObjectIdentity
ctTrunkGroups=_CtTrunkGroups_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,20,1,3,2))
ctTrunkConfGroupV10=ObjectGroup((1,3,6,1,4,1,52,4,1,2,20,1,3,2,1))
ctTrunkConfGroupV10.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ctTrunkConfGroupV10.setStatus(_A)
ctTrunkFlowDiagnosticGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,20,1,3,2,2))
ctTrunkFlowDiagnosticGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:ctTrunkFlowDiagnosticGroup.setStatus(_A)
ctTrunkComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,20,1,3,1,1))
ctTrunkComplianceV10.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ctTrunkComplianceV10.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:CTSmartTrunkProtocol,'CTSmartTrunkIndex':CTSmartTrunkIndex,_I:CTSmartTrunkName,_K:CTSmartTrunkLoadBalanceType,'ctSmartTrunk':ctSmartTrunk,'ctSmartTrunkConfig':ctSmartTrunkConfig,_L:ctTrunkGlobalStatus,'ctTrunkConfigTable':ctTrunkConfigTable,'ctTrunkConfigEntry':ctTrunkConfigEntry,_G:ctTrunkIndex,_N:ctTrunkConfigName,_O:ctTrunkConfigProtocol,_P:ctTrunkConfigLoadBalance,_Q:ctTrunkIfIndex,_M:ctTrunkRowStatus,'ctTrunkConnectionTable':ctTrunkConnectionTable,'ctTrunkConnectionEntry':ctTrunkConnectionEntry,_R:ctTrunkPortRemoteIfIndex,'ctSmartTrunkDebug':ctSmartTrunkDebug,_S:ctTrunkLLAPRequirement,_T:ctTrunkMaxTrunks,'ctTrunkFlowDiagnosticTable':ctTrunkFlowDiagnosticTable,'ctTrunkFlowDiagnosticEntry':ctTrunkFlowDiagnosticEntry,_U:ctTrunkFlowDiagnosticInstalledFlows,'ctTrunkConformance':ctTrunkConformance,'ctTrunkCompliances':ctTrunkCompliances,'ctTrunkComplianceV10':ctTrunkComplianceV10,'ctTrunkGroups':ctTrunkGroups,_V:ctTrunkConfGroupV10,_W:ctTrunkFlowDiagnosticGroup})