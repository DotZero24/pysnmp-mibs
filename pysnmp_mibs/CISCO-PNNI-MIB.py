_j='ciscoPnniRouteOptimizationGroup'
_i='ciscoPnniBasicGroup'
_h='ciscoPnniIfRouteOptimEndMinute'
_g='ciscoPnniIfRouteOptimEndHour'
_f='ciscoPnniIfRouteOptimStartMinute'
_e='ciscoPnniIfRouteOptimStartHour'
_d='ciscoPnniIfRouteOptimInterval'
_c='ciscoPnniIfRouteOptimization'
_b='ciscoPnniRouteOptimizationThreshold'
_a='ciscoPnniRouteAddrForwardingE164Address'
_Z='ciscoPnniPrecedenceValue'
_Y='ciscoPnniIfLinkSelection'
_X='ciscoPnniNodeScopeMappingMode'
_W='ciscoPnniNodeName'
_V='ciscoPnniNodePtseRequest'
_U='ciscoPnniNodeRedistributeStatic'
_T='ciscoPnniNodeAutoSummary'
_S='ciscoPnniMaxAdminWeightPercentage'
_R='ciscoPnniAdminWeightMode'
_Q='ciscoPnniResourceMgmtPollInterval'
_P='ciscoPnniBackgroundInsignificantThreshold'
_O='ciscoPnniBackgroundPollInterval'
_N='ciscoPnniBackgroundRoutes'
_M='ciscoPnniRouteAddrEntry'
_L='ciscoPnniIfEntry'
_K='ciscoPnniNodeEntry'
_J='E164Address'
_I='ciscoPnniPrecedenceAddressType'
_H='seconds'
_G='minutes'
_F='TruthValue'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='CISCO-PNNI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
pnniIfEntry,pnniNodeEntry,pnniRouteAddrEntry=mibBuilder.importSymbols('PNNI-MIB','pnniIfEntry','pnniNodeEntry','pnniRouteAddrEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
ciscoPnniMIB=ModuleIdentity((1,3,6,1,4,1,9,9,65))
if mibBuilder.loadTexts:ciscoPnniMIB.setRevisions(('1996-10-28 00:00',))
class E164Address(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
_CiscoPnniMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPnniMIBObjects=_CiscoPnniMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,65,1))
_CiscoPnniBase_ObjectIdentity=ObjectIdentity
ciscoPnniBase=_CiscoPnniBase_ObjectIdentity((1,3,6,1,4,1,9,9,65,1,1))
class _CiscoPnniBackgroundRoutes_Type(TruthValue):defaultValue=2
_CiscoPnniBackgroundRoutes_Type.__name__=_F
_CiscoPnniBackgroundRoutes_Object=MibScalar
ciscoPnniBackgroundRoutes=_CiscoPnniBackgroundRoutes_Object((1,3,6,1,4,1,9,9,65,1,1,1),_CiscoPnniBackgroundRoutes_Type())
ciscoPnniBackgroundRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniBackgroundRoutes.setStatus(_A)
class _CiscoPnniBackgroundPollInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CiscoPnniBackgroundPollInterval_Type.__name__=_C
_CiscoPnniBackgroundPollInterval_Object=MibScalar
ciscoPnniBackgroundPollInterval=_CiscoPnniBackgroundPollInterval_Object((1,3,6,1,4,1,9,9,65,1,1,2),_CiscoPnniBackgroundPollInterval_Type())
ciscoPnniBackgroundPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniBackgroundPollInterval.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniBackgroundPollInterval.setUnits(_H)
class _CiscoPnniBackgroundInsignificantThreshold_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoPnniBackgroundInsignificantThreshold_Type.__name__=_C
_CiscoPnniBackgroundInsignificantThreshold_Object=MibScalar
ciscoPnniBackgroundInsignificantThreshold=_CiscoPnniBackgroundInsignificantThreshold_Object((1,3,6,1,4,1,9,9,65,1,1,3),_CiscoPnniBackgroundInsignificantThreshold_Type())
ciscoPnniBackgroundInsignificantThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniBackgroundInsignificantThreshold.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniBackgroundInsignificantThreshold.setUnits('changes')
class _CiscoPnniResourceMgmtPollInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CiscoPnniResourceMgmtPollInterval_Type.__name__=_C
_CiscoPnniResourceMgmtPollInterval_Object=MibScalar
ciscoPnniResourceMgmtPollInterval=_CiscoPnniResourceMgmtPollInterval_Object((1,3,6,1,4,1,9,9,65,1,1,4),_CiscoPnniResourceMgmtPollInterval_Type())
ciscoPnniResourceMgmtPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniResourceMgmtPollInterval.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniResourceMgmtPollInterval.setUnits(_H)
class _CiscoPnniAdminWeightMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uniform',1),('linespeed',2)))
_CiscoPnniAdminWeightMode_Type.__name__=_C
_CiscoPnniAdminWeightMode_Object=MibScalar
ciscoPnniAdminWeightMode=_CiscoPnniAdminWeightMode_Object((1,3,6,1,4,1,9,9,65,1,1,5),_CiscoPnniAdminWeightMode_Type())
ciscoPnniAdminWeightMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniAdminWeightMode.setStatus(_A)
class _CiscoPnniMaxAdminWeightPercentage_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(100,2000))
_CiscoPnniMaxAdminWeightPercentage_Type.__name__=_C
_CiscoPnniMaxAdminWeightPercentage_Object=MibScalar
ciscoPnniMaxAdminWeightPercentage=_CiscoPnniMaxAdminWeightPercentage_Object((1,3,6,1,4,1,9,9,65,1,1,6),_CiscoPnniMaxAdminWeightPercentage_Type())
ciscoPnniMaxAdminWeightPercentage.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniMaxAdminWeightPercentage.setStatus(_A)
class _CiscoPnniRouteOptimizationThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,100))
_CiscoPnniRouteOptimizationThreshold_Type.__name__=_C
_CiscoPnniRouteOptimizationThreshold_Object=MibScalar
ciscoPnniRouteOptimizationThreshold=_CiscoPnniRouteOptimizationThreshold_Object((1,3,6,1,4,1,9,9,65,1,1,7),_CiscoPnniRouteOptimizationThreshold_Type())
ciscoPnniRouteOptimizationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniRouteOptimizationThreshold.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniRouteOptimizationThreshold.setUnits('percent')
_CiscoPnniNode_ObjectIdentity=ObjectIdentity
ciscoPnniNode=_CiscoPnniNode_ObjectIdentity((1,3,6,1,4,1,9,9,65,1,2))
_CiscoPnniNodeTable_Object=MibTable
ciscoPnniNodeTable=_CiscoPnniNodeTable_Object((1,3,6,1,4,1,9,9,65,1,2,1))
if mibBuilder.loadTexts:ciscoPnniNodeTable.setStatus(_A)
_CiscoPnniNodeEntry_Object=MibTableRow
ciscoPnniNodeEntry=_CiscoPnniNodeEntry_Object((1,3,6,1,4,1,9,9,65,1,2,1,1))
if mibBuilder.loadTexts:ciscoPnniNodeEntry.setStatus(_A)
class _CiscoPnniNodeAutoSummary_Type(TruthValue):defaultValue=1
_CiscoPnniNodeAutoSummary_Type.__name__=_F
_CiscoPnniNodeAutoSummary_Object=MibTableColumn
ciscoPnniNodeAutoSummary=_CiscoPnniNodeAutoSummary_Object((1,3,6,1,4,1,9,9,65,1,2,1,1,1),_CiscoPnniNodeAutoSummary_Type())
ciscoPnniNodeAutoSummary.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPnniNodeAutoSummary.setStatus(_A)
class _CiscoPnniNodeRedistributeStatic_Type(TruthValue):defaultValue=1
_CiscoPnniNodeRedistributeStatic_Type.__name__=_F
_CiscoPnniNodeRedistributeStatic_Object=MibTableColumn
ciscoPnniNodeRedistributeStatic=_CiscoPnniNodeRedistributeStatic_Object((1,3,6,1,4,1,9,9,65,1,2,1,1,2),_CiscoPnniNodeRedistributeStatic_Type())
ciscoPnniNodeRedistributeStatic.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPnniNodeRedistributeStatic.setStatus(_A)
class _CiscoPnniNodePtseRequest_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CiscoPnniNodePtseRequest_Type.__name__=_C
_CiscoPnniNodePtseRequest_Object=MibTableColumn
ciscoPnniNodePtseRequest=_CiscoPnniNodePtseRequest_Object((1,3,6,1,4,1,9,9,65,1,2,1,1,3),_CiscoPnniNodePtseRequest_Type())
ciscoPnniNodePtseRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPnniNodePtseRequest.setStatus(_A)
_CiscoPnniNodeName_Type=DisplayString
_CiscoPnniNodeName_Object=MibTableColumn
ciscoPnniNodeName=_CiscoPnniNodeName_Object((1,3,6,1,4,1,9,9,65,1,2,1,1,4),_CiscoPnniNodeName_Type())
ciscoPnniNodeName.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPnniNodeName.setStatus(_A)
class _CiscoPnniNodeScopeMappingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('manual',2)))
_CiscoPnniNodeScopeMappingMode_Type.__name__=_C
_CiscoPnniNodeScopeMappingMode_Object=MibTableColumn
ciscoPnniNodeScopeMappingMode=_CiscoPnniNodeScopeMappingMode_Object((1,3,6,1,4,1,9,9,65,1,2,1,1,5),_CiscoPnniNodeScopeMappingMode_Type())
ciscoPnniNodeScopeMappingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPnniNodeScopeMappingMode.setStatus(_A)
_CiscoPnniInterface_ObjectIdentity=ObjectIdentity
ciscoPnniInterface=_CiscoPnniInterface_ObjectIdentity((1,3,6,1,4,1,9,9,65,1,3))
_CiscoPnniIfTable_Object=MibTable
ciscoPnniIfTable=_CiscoPnniIfTable_Object((1,3,6,1,4,1,9,9,65,1,3,1))
if mibBuilder.loadTexts:ciscoPnniIfTable.setStatus(_A)
_CiscoPnniIfEntry_Object=MibTableRow
ciscoPnniIfEntry=_CiscoPnniIfEntry_Object((1,3,6,1,4,1,9,9,65,1,3,1,1))
if mibBuilder.loadTexts:ciscoPnniIfEntry.setStatus(_A)
class _CiscoPnniIfLinkSelection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adminWeightMinimize',1),('blockingMinimize',2),('transmitSpeedMaximize',3),('loadBalance',4)))
_CiscoPnniIfLinkSelection_Type.__name__=_C
_CiscoPnniIfLinkSelection_Object=MibTableColumn
ciscoPnniIfLinkSelection=_CiscoPnniIfLinkSelection_Object((1,3,6,1,4,1,9,9,65,1,3,1,1,1),_CiscoPnniIfLinkSelection_Type())
ciscoPnniIfLinkSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniIfLinkSelection.setStatus(_A)
class _CiscoPnniIfRouteOptimization_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disable',1),('soft',2),('switched',3),('switchedAndSoft',4)))
_CiscoPnniIfRouteOptimization_Type.__name__=_C
_CiscoPnniIfRouteOptimization_Object=MibTableColumn
ciscoPnniIfRouteOptimization=_CiscoPnniIfRouteOptimization_Object((1,3,6,1,4,1,9,9,65,1,3,1,1,2),_CiscoPnniIfRouteOptimization_Type())
ciscoPnniIfRouteOptimization.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimization.setStatus(_A)
class _CiscoPnniIfRouteOptimInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_CiscoPnniIfRouteOptimInterval_Type.__name__=_C
_CiscoPnniIfRouteOptimInterval_Object=MibTableColumn
ciscoPnniIfRouteOptimInterval=_CiscoPnniIfRouteOptimInterval_Object((1,3,6,1,4,1,9,9,65,1,3,1,1,3),_CiscoPnniIfRouteOptimInterval_Type())
ciscoPnniIfRouteOptimInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimInterval.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimInterval.setUnits(_G)
class _CiscoPnniIfRouteOptimStartHour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_CiscoPnniIfRouteOptimStartHour_Type.__name__=_C
_CiscoPnniIfRouteOptimStartHour_Object=MibTableColumn
ciscoPnniIfRouteOptimStartHour=_CiscoPnniIfRouteOptimStartHour_Object((1,3,6,1,4,1,9,9,65,1,3,1,1,4),_CiscoPnniIfRouteOptimStartHour_Type())
ciscoPnniIfRouteOptimStartHour.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimStartHour.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimStartHour.setUnits('hour')
class _CiscoPnniIfRouteOptimStartMinute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_CiscoPnniIfRouteOptimStartMinute_Type.__name__=_C
_CiscoPnniIfRouteOptimStartMinute_Object=MibTableColumn
ciscoPnniIfRouteOptimStartMinute=_CiscoPnniIfRouteOptimStartMinute_Object((1,3,6,1,4,1,9,9,65,1,3,1,1,5),_CiscoPnniIfRouteOptimStartMinute_Type())
ciscoPnniIfRouteOptimStartMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimStartMinute.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimStartMinute.setUnits(_G)
class _CiscoPnniIfRouteOptimEndHour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_CiscoPnniIfRouteOptimEndHour_Type.__name__=_C
_CiscoPnniIfRouteOptimEndHour_Object=MibTableColumn
ciscoPnniIfRouteOptimEndHour=_CiscoPnniIfRouteOptimEndHour_Object((1,3,6,1,4,1,9,9,65,1,3,1,1,6),_CiscoPnniIfRouteOptimEndHour_Type())
ciscoPnniIfRouteOptimEndHour.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimEndHour.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimEndHour.setUnits('hour')
class _CiscoPnniIfRouteOptimEndMinute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_CiscoPnniIfRouteOptimEndMinute_Type.__name__=_C
_CiscoPnniIfRouteOptimEndMinute_Object=MibTableColumn
ciscoPnniIfRouteOptimEndMinute=_CiscoPnniIfRouteOptimEndMinute_Object((1,3,6,1,4,1,9,9,65,1,3,1,1,7),_CiscoPnniIfRouteOptimEndMinute_Type())
ciscoPnniIfRouteOptimEndMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimEndMinute.setStatus(_A)
if mibBuilder.loadTexts:ciscoPnniIfRouteOptimEndMinute.setUnits(_G)
_CiscoPnniPrecedence_ObjectIdentity=ObjectIdentity
ciscoPnniPrecedence=_CiscoPnniPrecedence_ObjectIdentity((1,3,6,1,4,1,9,9,65,1,4))
_CiscoPnniPrecedenceTable_Object=MibTable
ciscoPnniPrecedenceTable=_CiscoPnniPrecedenceTable_Object((1,3,6,1,4,1,9,9,65,1,4,1))
if mibBuilder.loadTexts:ciscoPnniPrecedenceTable.setStatus(_A)
_CiscoPnniPrecedenceEntry_Object=MibTableRow
ciscoPnniPrecedenceEntry=_CiscoPnniPrecedenceEntry_Object((1,3,6,1,4,1,9,9,65,1,4,1,1))
ciscoPnniPrecedenceEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ciscoPnniPrecedenceEntry.setStatus(_A)
class _CiscoPnniPrecedenceAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('staticLocalInternalWithMetrics',1),('staticLocalExterior',2),('staticLocalExteriorWithMetrics',3),('pnniRemoteInternal',4),('pnniRemoteInternalWithMetrics',5),('pnniRemoteExterior',6),('pnniRemoteExteriorWithMetrics',7)))
_CiscoPnniPrecedenceAddressType_Type.__name__=_C
_CiscoPnniPrecedenceAddressType_Object=MibTableColumn
ciscoPnniPrecedenceAddressType=_CiscoPnniPrecedenceAddressType_Object((1,3,6,1,4,1,9,9,65,1,4,1,1,1),_CiscoPnniPrecedenceAddressType_Type())
ciscoPnniPrecedenceAddressType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoPnniPrecedenceAddressType.setStatus(_A)
class _CiscoPnniPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_CiscoPnniPrecedenceValue_Type.__name__=_C
_CiscoPnniPrecedenceValue_Object=MibTableColumn
ciscoPnniPrecedenceValue=_CiscoPnniPrecedenceValue_Object((1,3,6,1,4,1,9,9,65,1,4,1,1,2),_CiscoPnniPrecedenceValue_Type())
ciscoPnniPrecedenceValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoPnniPrecedenceValue.setStatus(_A)
_CiscoPnniRouteAddr_ObjectIdentity=ObjectIdentity
ciscoPnniRouteAddr=_CiscoPnniRouteAddr_ObjectIdentity((1,3,6,1,4,1,9,9,65,1,5))
_CiscoPnniRouteAddrTable_Object=MibTable
ciscoPnniRouteAddrTable=_CiscoPnniRouteAddrTable_Object((1,3,6,1,4,1,9,9,65,1,5,1))
if mibBuilder.loadTexts:ciscoPnniRouteAddrTable.setStatus(_A)
_CiscoPnniRouteAddrEntry_Object=MibTableRow
ciscoPnniRouteAddrEntry=_CiscoPnniRouteAddrEntry_Object((1,3,6,1,4,1,9,9,65,1,5,1,1))
if mibBuilder.loadTexts:ciscoPnniRouteAddrEntry.setStatus(_A)
class _CiscoPnniRouteAddrForwardingE164Address_Type(E164Address):defaultHexValue=''
_CiscoPnniRouteAddrForwardingE164Address_Type.__name__=_J
_CiscoPnniRouteAddrForwardingE164Address_Object=MibTableColumn
ciscoPnniRouteAddrForwardingE164Address=_CiscoPnniRouteAddrForwardingE164Address_Object((1,3,6,1,4,1,9,9,65,1,5,1,1,1),_CiscoPnniRouteAddrForwardingE164Address_Type())
ciscoPnniRouteAddrForwardingE164Address.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPnniRouteAddrForwardingE164Address.setStatus(_A)
_CiscoPnniMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPnniMIBConformance=_CiscoPnniMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,65,3))
_CiscoPnniMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPnniMIBCompliances=_CiscoPnniMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,65,3,1))
_CiscoPnniMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPnniMIBGroups=_CiscoPnniMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,65,3,2))
pnniNodeEntry.registerAugmentions((_B,_K))
ciscoPnniNodeEntry.setIndexNames(*pnniNodeEntry.getIndexNames())
pnniIfEntry.registerAugmentions((_B,_L))
ciscoPnniIfEntry.setIndexNames(*pnniIfEntry.getIndexNames())
pnniRouteAddrEntry.registerAugmentions((_B,_M))
ciscoPnniRouteAddrEntry.setIndexNames(*pnniRouteAddrEntry.getIndexNames())
ciscoPnniBasicGroup=ObjectGroup((1,3,6,1,4,1,9,9,65,3,2,1))
ciscoPnniBasicGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoPnniBasicGroup.setStatus(_A)
ciscoPnniRouteOptimizationGroup=ObjectGroup((1,3,6,1,4,1,9,9,65,3,2,2))
ciscoPnniRouteOptimizationGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ciscoPnniRouteOptimizationGroup.setStatus(_A)
ciscoPnniMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,65,3,1,1))
ciscoPnniMIBCompliance.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ciscoPnniMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:E164Address,'ciscoPnniMIB':ciscoPnniMIB,'ciscoPnniMIBObjects':ciscoPnniMIBObjects,'ciscoPnniBase':ciscoPnniBase,_N:ciscoPnniBackgroundRoutes,_O:ciscoPnniBackgroundPollInterval,_P:ciscoPnniBackgroundInsignificantThreshold,_Q:ciscoPnniResourceMgmtPollInterval,_R:ciscoPnniAdminWeightMode,_S:ciscoPnniMaxAdminWeightPercentage,_b:ciscoPnniRouteOptimizationThreshold,'ciscoPnniNode':ciscoPnniNode,'ciscoPnniNodeTable':ciscoPnniNodeTable,_K:ciscoPnniNodeEntry,_T:ciscoPnniNodeAutoSummary,_U:ciscoPnniNodeRedistributeStatic,_V:ciscoPnniNodePtseRequest,_W:ciscoPnniNodeName,_X:ciscoPnniNodeScopeMappingMode,'ciscoPnniInterface':ciscoPnniInterface,'ciscoPnniIfTable':ciscoPnniIfTable,_L:ciscoPnniIfEntry,_Y:ciscoPnniIfLinkSelection,_c:ciscoPnniIfRouteOptimization,_d:ciscoPnniIfRouteOptimInterval,_e:ciscoPnniIfRouteOptimStartHour,_f:ciscoPnniIfRouteOptimStartMinute,_g:ciscoPnniIfRouteOptimEndHour,_h:ciscoPnniIfRouteOptimEndMinute,'ciscoPnniPrecedence':ciscoPnniPrecedence,'ciscoPnniPrecedenceTable':ciscoPnniPrecedenceTable,'ciscoPnniPrecedenceEntry':ciscoPnniPrecedenceEntry,_I:ciscoPnniPrecedenceAddressType,_Z:ciscoPnniPrecedenceValue,'ciscoPnniRouteAddr':ciscoPnniRouteAddr,'ciscoPnniRouteAddrTable':ciscoPnniRouteAddrTable,_M:ciscoPnniRouteAddrEntry,_a:ciscoPnniRouteAddrForwardingE164Address,'ciscoPnniMIBConformance':ciscoPnniMIBConformance,'ciscoPnniMIBCompliances':ciscoPnniMIBCompliances,'ciscoPnniMIBCompliance':ciscoPnniMIBCompliance,'ciscoPnniMIBGroups':ciscoPnniMIBGroups,_i:ciscoPnniBasicGroup,_j:ciscoPnniRouteOptimizationGroup})