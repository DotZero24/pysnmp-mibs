_Z='osResourceOptGroup'
_Y='osResourceMandatoryGroup'
_X='osResourceTxSdmaUsers'
_W='osResourceTxSdmaInterval'
_V='osResourceTxSdmaMode'
_U='osResourceMacEntriesFree'
_T='osResourceMacEntriesUsed'
_S='osResourceMacEntriesTotal'
_R='osResourcePolicerEntriesFree'
_Q='osResourcePolicerEntriesUsed'
_P='osResourcePolicerEntriesTotal'
_O='osResourceTcamRulesFreeOptional'
_N='osResourceTcamRulesFreeGuaranteed'
_M='osResourceTcamRulesUsed'
_L='osResourceTcamRulesGuaranteed'
_K='osResourceTcamRulesSize'
_J='osResourceTxSdmaId'
_I='osResourcePolicerType'
_H='ingressAcl'
_G='osResourceTcamId'
_F='osResourcesSupport'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='OS-RESOURCES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osResources=ModuleIdentity((1,3,6,1,4,1,6926,2,41))
if mibBuilder.loadTexts:osResources.setRevisions(('2019-12-11 00:00',))
_OsResourcesGen_ObjectIdentity=ObjectIdentity
osResourcesGen=_OsResourcesGen_ObjectIdentity((1,3,6,1,4,1,6926,2,41,1))
class _OsResourcesSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsResourcesSupport_Type.__name__=_D
_OsResourcesSupport_Object=MibScalar
osResourcesSupport=_OsResourcesSupport_Object((1,3,6,1,4,1,6926,2,41,1,1),_OsResourcesSupport_Type())
osResourcesSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourcesSupport.setStatus(_A)
_OsResourcesTables_ObjectIdentity=ObjectIdentity
osResourcesTables=_OsResourcesTables_ObjectIdentity((1,3,6,1,4,1,6926,2,41,2))
_OsResourceTcamTable_Object=MibTable
osResourceTcamTable=_OsResourceTcamTable_Object((1,3,6,1,4,1,6926,2,41,2,1))
if mibBuilder.loadTexts:osResourceTcamTable.setStatus(_A)
_OsResourceTcamEntry_Object=MibTableRow
osResourceTcamEntry=_OsResourceTcamEntry_Object((1,3,6,1,4,1,6926,2,41,2,1,1))
osResourceTcamEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:osResourceTcamEntry.setStatus(_A)
class _OsResourceTcamId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('tunneling',1),('ingressOam',2),(_H,3),('egressAclOam',4),('ingressBfd',5)))
_OsResourceTcamId_Type.__name__=_D
_OsResourceTcamId_Object=MibTableColumn
osResourceTcamId=_OsResourceTcamId_Object((1,3,6,1,4,1,6926,2,41,2,1,1,1),_OsResourceTcamId_Type())
osResourceTcamId.setMaxAccess(_E)
if mibBuilder.loadTexts:osResourceTcamId.setStatus(_A)
_OsResourceTcamRulesSize_Type=Unsigned32
_OsResourceTcamRulesSize_Object=MibTableColumn
osResourceTcamRulesSize=_OsResourceTcamRulesSize_Object((1,3,6,1,4,1,6926,2,41,2,1,1,3),_OsResourceTcamRulesSize_Type())
osResourceTcamRulesSize.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTcamRulesSize.setStatus(_A)
_OsResourceTcamRulesGuaranteed_Type=Unsigned32
_OsResourceTcamRulesGuaranteed_Object=MibTableColumn
osResourceTcamRulesGuaranteed=_OsResourceTcamRulesGuaranteed_Object((1,3,6,1,4,1,6926,2,41,2,1,1,4),_OsResourceTcamRulesGuaranteed_Type())
osResourceTcamRulesGuaranteed.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTcamRulesGuaranteed.setStatus(_A)
_OsResourceTcamRulesUsed_Type=Unsigned32
_OsResourceTcamRulesUsed_Object=MibTableColumn
osResourceTcamRulesUsed=_OsResourceTcamRulesUsed_Object((1,3,6,1,4,1,6926,2,41,2,1,1,5),_OsResourceTcamRulesUsed_Type())
osResourceTcamRulesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTcamRulesUsed.setStatus(_A)
_OsResourceTcamRulesFreeGuaranteed_Type=Unsigned32
_OsResourceTcamRulesFreeGuaranteed_Object=MibTableColumn
osResourceTcamRulesFreeGuaranteed=_OsResourceTcamRulesFreeGuaranteed_Object((1,3,6,1,4,1,6926,2,41,2,1,1,6),_OsResourceTcamRulesFreeGuaranteed_Type())
osResourceTcamRulesFreeGuaranteed.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTcamRulesFreeGuaranteed.setStatus(_A)
_OsResourceTcamRulesFreeOptional_Type=Unsigned32
_OsResourceTcamRulesFreeOptional_Object=MibTableColumn
osResourceTcamRulesFreeOptional=_OsResourceTcamRulesFreeOptional_Object((1,3,6,1,4,1,6926,2,41,2,1,1,7),_OsResourceTcamRulesFreeOptional_Type())
osResourceTcamRulesFreeOptional.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTcamRulesFreeOptional.setStatus(_A)
_OsResourcePolicerTable_Object=MibTable
osResourcePolicerTable=_OsResourcePolicerTable_Object((1,3,6,1,4,1,6926,2,41,2,2))
if mibBuilder.loadTexts:osResourcePolicerTable.setStatus(_A)
_OsResourcePolicerEntry_Object=MibTableRow
osResourcePolicerEntry=_OsResourcePolicerEntry_Object((1,3,6,1,4,1,6926,2,41,2,2,1))
osResourcePolicerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:osResourcePolicerEntry.setStatus(_A)
class _OsResourcePolicerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('egressAcl',2)))
_OsResourcePolicerType_Type.__name__=_D
_OsResourcePolicerType_Object=MibTableColumn
osResourcePolicerType=_OsResourcePolicerType_Object((1,3,6,1,4,1,6926,2,41,2,2,1,1),_OsResourcePolicerType_Type())
osResourcePolicerType.setMaxAccess(_E)
if mibBuilder.loadTexts:osResourcePolicerType.setStatus(_A)
_OsResourcePolicerEntriesTotal_Type=Unsigned32
_OsResourcePolicerEntriesTotal_Object=MibTableColumn
osResourcePolicerEntriesTotal=_OsResourcePolicerEntriesTotal_Object((1,3,6,1,4,1,6926,2,41,2,2,1,3),_OsResourcePolicerEntriesTotal_Type())
osResourcePolicerEntriesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourcePolicerEntriesTotal.setStatus(_A)
_OsResourcePolicerEntriesUsed_Type=Unsigned32
_OsResourcePolicerEntriesUsed_Object=MibTableColumn
osResourcePolicerEntriesUsed=_OsResourcePolicerEntriesUsed_Object((1,3,6,1,4,1,6926,2,41,2,2,1,4),_OsResourcePolicerEntriesUsed_Type())
osResourcePolicerEntriesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourcePolicerEntriesUsed.setStatus(_A)
_OsResourcePolicerEntriesFree_Type=Unsigned32
_OsResourcePolicerEntriesFree_Object=MibTableColumn
osResourcePolicerEntriesFree=_OsResourcePolicerEntriesFree_Object((1,3,6,1,4,1,6926,2,41,2,2,1,5),_OsResourcePolicerEntriesFree_Type())
osResourcePolicerEntriesFree.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourcePolicerEntriesFree.setStatus(_A)
_OsResourceTxSdmaTable_Object=MibTable
osResourceTxSdmaTable=_OsResourceTxSdmaTable_Object((1,3,6,1,4,1,6926,2,41,2,3))
if mibBuilder.loadTexts:osResourceTxSdmaTable.setStatus(_A)
_OsResourceTxSdmaEntry_Object=MibTableRow
osResourceTxSdmaEntry=_OsResourceTxSdmaEntry_Object((1,3,6,1,4,1,6926,2,41,2,3,1))
osResourceTxSdmaEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osResourceTxSdmaEntry.setStatus(_A)
_OsResourceTxSdmaId_Type=Unsigned32
_OsResourceTxSdmaId_Object=MibTableColumn
osResourceTxSdmaId=_OsResourceTxSdmaId_Object((1,3,6,1,4,1,6926,2,41,2,3,1,1),_OsResourceTxSdmaId_Type())
osResourceTxSdmaId.setMaxAccess(_E)
if mibBuilder.loadTexts:osResourceTxSdmaId.setStatus(_A)
class _OsResourceTxSdmaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('free',1),('periodic',2),('rate',3)))
_OsResourceTxSdmaMode_Type.__name__=_D
_OsResourceTxSdmaMode_Object=MibTableColumn
osResourceTxSdmaMode=_OsResourceTxSdmaMode_Object((1,3,6,1,4,1,6926,2,41,2,3,1,2),_OsResourceTxSdmaMode_Type())
osResourceTxSdmaMode.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTxSdmaMode.setStatus(_A)
_OsResourceTxSdmaInterval_Type=Unsigned32
_OsResourceTxSdmaInterval_Object=MibTableColumn
osResourceTxSdmaInterval=_OsResourceTxSdmaInterval_Object((1,3,6,1,4,1,6926,2,41,2,3,1,3),_OsResourceTxSdmaInterval_Type())
osResourceTxSdmaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTxSdmaInterval.setStatus(_A)
_OsResourceTxSdmaUsers_Type=Unsigned32
_OsResourceTxSdmaUsers_Object=MibTableColumn
osResourceTxSdmaUsers=_OsResourceTxSdmaUsers_Object((1,3,6,1,4,1,6926,2,41,2,3,1,4),_OsResourceTxSdmaUsers_Type())
osResourceTxSdmaUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceTxSdmaUsers.setStatus(_A)
_OsResourcesMac_ObjectIdentity=ObjectIdentity
osResourcesMac=_OsResourcesMac_ObjectIdentity((1,3,6,1,4,1,6926,2,41,3))
_OsResourceMacEntriesTotal_Type=Unsigned32
_OsResourceMacEntriesTotal_Object=MibScalar
osResourceMacEntriesTotal=_OsResourceMacEntriesTotal_Object((1,3,6,1,4,1,6926,2,41,3,1),_OsResourceMacEntriesTotal_Type())
osResourceMacEntriesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceMacEntriesTotal.setStatus(_A)
_OsResourceMacEntriesUsed_Type=Unsigned32
_OsResourceMacEntriesUsed_Object=MibScalar
osResourceMacEntriesUsed=_OsResourceMacEntriesUsed_Object((1,3,6,1,4,1,6926,2,41,3,2),_OsResourceMacEntriesUsed_Type())
osResourceMacEntriesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceMacEntriesUsed.setStatus(_A)
_OsResourceMacEntriesFree_Type=Unsigned32
_OsResourceMacEntriesFree_Object=MibScalar
osResourceMacEntriesFree=_OsResourceMacEntriesFree_Object((1,3,6,1,4,1,6926,2,41,3,3),_OsResourceMacEntriesFree_Type())
osResourceMacEntriesFree.setMaxAccess(_C)
if mibBuilder.loadTexts:osResourceMacEntriesFree.setStatus(_A)
_OsResourcesConformance_ObjectIdentity=ObjectIdentity
osResourcesConformance=_OsResourcesConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,41,100))
_OsResourcesMIBCompliances_ObjectIdentity=ObjectIdentity
osResourcesMIBCompliances=_OsResourcesMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,41,100,1))
_OsResourcesMIBGroups_ObjectIdentity=ObjectIdentity
osResourcesMIBGroups=_OsResourcesMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,41,100,2))
osResourceMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,41,100,2,1))
osResourceMandatoryGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:osResourceMandatoryGroup.setStatus(_A)
osResourceOptGroup=ObjectGroup((1,3,6,1,4,1,6926,2,41,100,2,2))
osResourceOptGroup.setObjects(*((_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:osResourceOptGroup.setStatus(_A)
osResourceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,41,100,1,1))
osResourceMIBCompliance.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:osResourceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osResources':osResources,'osResourcesGen':osResourcesGen,_F:osResourcesSupport,'osResourcesTables':osResourcesTables,'osResourceTcamTable':osResourceTcamTable,'osResourceTcamEntry':osResourceTcamEntry,_G:osResourceTcamId,_K:osResourceTcamRulesSize,_L:osResourceTcamRulesGuaranteed,_M:osResourceTcamRulesUsed,_N:osResourceTcamRulesFreeGuaranteed,_O:osResourceTcamRulesFreeOptional,'osResourcePolicerTable':osResourcePolicerTable,'osResourcePolicerEntry':osResourcePolicerEntry,_I:osResourcePolicerType,_P:osResourcePolicerEntriesTotal,_Q:osResourcePolicerEntriesUsed,_R:osResourcePolicerEntriesFree,'osResourceTxSdmaTable':osResourceTxSdmaTable,'osResourceTxSdmaEntry':osResourceTxSdmaEntry,_J:osResourceTxSdmaId,_V:osResourceTxSdmaMode,_W:osResourceTxSdmaInterval,_X:osResourceTxSdmaUsers,'osResourcesMac':osResourcesMac,_S:osResourceMacEntriesTotal,_T:osResourceMacEntriesUsed,_U:osResourceMacEntriesFree,'osResourcesConformance':osResourcesConformance,'osResourcesMIBCompliances':osResourcesMIBCompliances,'osResourceMIBCompliance':osResourceMIBCompliance,'osResourcesMIBGroups':osResourcesMIBGroups,_Y:osResourceMandatoryGroup,_Z:osResourceOptGroup})