_o='ctQBridgePortVlanEgressGroup2'
_n='ctQBridgeVlanGvrpGroup'
_m='ctQBridgeTpFdbTableExtGroup'
_l='ctQBridgePortVlanEgressGroup'
_k='ctQBridgeVlanCurrentForbidGroup'
_j='ctQBridgePortGroup'
_i='ctDot1qPortVlanStaticEgressType'
_h='ctDot1qVlanGvrpRestrictedStatus'
_g='ctDot1qTpFdbRemoveAddress'
_f='ctDot1qPortReplaceTCI'
_e='ctDot1qVlanForbidEgressPorts'
_d='ctDot1qPortDiscardTagged'
_c='ctDot1qVlanDynamicEgressStatus'
_b='ctDot1qVlanCurrentEntryExt'
_a='ctDot1qPortVlanEntry'
_Z='ctDot1qVlanGvrpRestrictedIndex'
_Y='forbidden'
_X='untagged'
_W='tagged'
_V='not-accessible'
_U='ctDot1qVlanDynamicEgressIndex'
_T='TruthValue'
_S='dot1qTpFdbAddress'
_R='dot1qFdbId'
_Q='ctQBridgePortReplaceTCIGroup'
_P='ctQBridgePortGroup2'
_O='ctDot1qPortVlanEgressType'
_N='ctDot1qPortVlanEgressStatus'
_M='ctDot1qPortDefaultForwardMode'
_L='dot1qVlanIndex'
_K='dot1dBasePort'
_J='BRIDGE-MIB'
_I='ctQBridgeVlanGroup'
_H='read-only'
_G='deprecated'
_F='Integer32'
_E='Q-BRIDGE-MIB'
_D='EnabledStatus'
_C='read-write'
_B='CTRON-Q-BRIDGE-MIB-EXT'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,dot1dBasePortEntry=mibBuilder.importSymbols(_J,_K,'dot1dBasePortEntry')
ctVlanExt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctVlanExt')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
PortList,VlanIndex,dot1qFdbId,dot1qTpFdbAddress,dot1qVlanCurrentEntry,dot1qVlanIndex=mibBuilder.importSymbols(_E,'PortList','VlanIndex',_R,_S,'dot1qVlanCurrentEntry',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_T)
ctQBridgeMibExt=ModuleIdentity((1,3,6,1,4,1,52,4,1,2,16,7))
if mibBuilder.loadTexts:ctQBridgeMibExt.setRevisions(('2012-02-14 14:42','2012-01-09 13:49','2010-06-30 18:25','2007-02-16 17:44','2005-01-21 17:17','2004-06-04 12:41','2003-12-15 20:53','2002-07-26 20:45','2002-07-19 14:12','2001-04-16 18:16','2001-01-10 13:29','1999-10-06 08:12'))
_CtQBridgeMIBObjects_ObjectIdentity=ObjectIdentity
ctQBridgeMIBObjects=_CtQBridgeMIBObjects_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,7,1))
_CtDot1qPortVlanExtTable_Object=MibTable
ctDot1qPortVlanExtTable=_CtDot1qPortVlanExtTable_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,1))
if mibBuilder.loadTexts:ctDot1qPortVlanExtTable.setStatus(_A)
_CtDot1qPortVlanEntry_Object=MibTableRow
ctDot1qPortVlanEntry=_CtDot1qPortVlanEntry_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,1,1))
if mibBuilder.loadTexts:ctDot1qPortVlanEntry.setStatus(_A)
class _CtDot1qPortDefaultForwardMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forwardNoFrames',1),('forwardAllFramesAsTagged',2),('forwardAllFramesAsUntagged',3)))
_CtDot1qPortDefaultForwardMode_Type.__name__=_F
_CtDot1qPortDefaultForwardMode_Object=MibTableColumn
ctDot1qPortDefaultForwardMode=_CtDot1qPortDefaultForwardMode_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,1,1,1),_CtDot1qPortDefaultForwardMode_Type())
ctDot1qPortDefaultForwardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDot1qPortDefaultForwardMode.setStatus(_A)
class _CtDot1qPortDiscardTagged_Type(EnabledStatus):defaultValue=2
_CtDot1qPortDiscardTagged_Type.__name__=_D
_CtDot1qPortDiscardTagged_Object=MibTableColumn
ctDot1qPortDiscardTagged=_CtDot1qPortDiscardTagged_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,1,1,2),_CtDot1qPortDiscardTagged_Type())
ctDot1qPortDiscardTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDot1qPortDiscardTagged.setStatus(_A)
class _CtDot1qPortReplaceTCI_Type(EnabledStatus):defaultValue=2
_CtDot1qPortReplaceTCI_Type.__name__=_D
_CtDot1qPortReplaceTCI_Object=MibTableColumn
ctDot1qPortReplaceTCI=_CtDot1qPortReplaceTCI_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,1,1,3),_CtDot1qPortReplaceTCI_Type())
ctDot1qPortReplaceTCI.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDot1qPortReplaceTCI.setStatus(_A)
_CtDot1qVlanDynamicEgressTable_Object=MibTable
ctDot1qVlanDynamicEgressTable=_CtDot1qVlanDynamicEgressTable_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,2))
if mibBuilder.loadTexts:ctDot1qVlanDynamicEgressTable.setStatus(_A)
_CtDot1qVlanDynamicEgressEntry_Object=MibTableRow
ctDot1qVlanDynamicEgressEntry=_CtDot1qVlanDynamicEgressEntry_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,2,1))
ctDot1qVlanDynamicEgressEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:ctDot1qVlanDynamicEgressEntry.setStatus(_A)
_CtDot1qVlanDynamicEgressIndex_Type=VlanIndex
_CtDot1qVlanDynamicEgressIndex_Object=MibTableColumn
ctDot1qVlanDynamicEgressIndex=_CtDot1qVlanDynamicEgressIndex_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,2,1,1),_CtDot1qVlanDynamicEgressIndex_Type())
ctDot1qVlanDynamicEgressIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:ctDot1qVlanDynamicEgressIndex.setStatus(_A)
class _CtDot1qVlanDynamicEgressStatus_Type(EnabledStatus):defaultValue=2
_CtDot1qVlanDynamicEgressStatus_Type.__name__=_D
_CtDot1qVlanDynamicEgressStatus_Object=MibTableColumn
ctDot1qVlanDynamicEgressStatus=_CtDot1qVlanDynamicEgressStatus_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,2,1,2),_CtDot1qVlanDynamicEgressStatus_Type())
ctDot1qVlanDynamicEgressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDot1qVlanDynamicEgressStatus.setStatus(_A)
_CtDot1qVlanCurrentExtTable_Object=MibTable
ctDot1qVlanCurrentExtTable=_CtDot1qVlanCurrentExtTable_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,3))
if mibBuilder.loadTexts:ctDot1qVlanCurrentExtTable.setStatus(_A)
_CtDot1qVlanCurrentEntryExt_Object=MibTableRow
ctDot1qVlanCurrentEntryExt=_CtDot1qVlanCurrentEntryExt_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,3,1))
if mibBuilder.loadTexts:ctDot1qVlanCurrentEntryExt.setStatus(_A)
_CtDot1qVlanForbidEgressPorts_Type=PortList
_CtDot1qVlanForbidEgressPorts_Object=MibTableColumn
ctDot1qVlanForbidEgressPorts=_CtDot1qVlanForbidEgressPorts_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,3,1,1),_CtDot1qVlanForbidEgressPorts_Type())
ctDot1qVlanForbidEgressPorts.setMaxAccess(_H)
if mibBuilder.loadTexts:ctDot1qVlanForbidEgressPorts.setStatus(_A)
_CtDot1qPortVlanEgressTable_Object=MibTable
ctDot1qPortVlanEgressTable=_CtDot1qPortVlanEgressTable_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,4))
if mibBuilder.loadTexts:ctDot1qPortVlanEgressTable.setStatus(_A)
_CtDot1qPortVlanEgressEntry_Object=MibTableRow
ctDot1qPortVlanEgressEntry=_CtDot1qPortVlanEgressEntry_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,4,1))
ctDot1qPortVlanEgressEntry.setIndexNames((0,_J,_K),(0,_E,_L))
if mibBuilder.loadTexts:ctDot1qPortVlanEgressEntry.setStatus(_A)
class _CtDot1qPortVlanEgressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('static',2),('gvrp',3),('ctDynamicEgress',4),('etsysPolicyProfile',5),('ctPortDefFwdMode',6),('rfc3580VlanTunnelAttribute',7),('mvrp',8)))
_CtDot1qPortVlanEgressStatus_Type.__name__=_F
_CtDot1qPortVlanEgressStatus_Object=MibTableColumn
ctDot1qPortVlanEgressStatus=_CtDot1qPortVlanEgressStatus_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,4,1,1),_CtDot1qPortVlanEgressStatus_Type())
ctDot1qPortVlanEgressStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ctDot1qPortVlanEgressStatus.setStatus(_A)
class _CtDot1qPortVlanEgressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_CtDot1qPortVlanEgressType_Type.__name__=_F
_CtDot1qPortVlanEgressType_Object=MibTableColumn
ctDot1qPortVlanEgressType=_CtDot1qPortVlanEgressType_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,4,1,2),_CtDot1qPortVlanEgressType_Type())
ctDot1qPortVlanEgressType.setMaxAccess(_H)
if mibBuilder.loadTexts:ctDot1qPortVlanEgressType.setStatus(_A)
_CtDot1qTpFdbExtTable_Object=MibTable
ctDot1qTpFdbExtTable=_CtDot1qTpFdbExtTable_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,5))
if mibBuilder.loadTexts:ctDot1qTpFdbExtTable.setStatus(_A)
_CtDot1qTpFdbExtEntry_Object=MibTableRow
ctDot1qTpFdbExtEntry=_CtDot1qTpFdbExtEntry_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,5,1))
ctDot1qTpFdbExtEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:ctDot1qTpFdbExtEntry.setStatus(_A)
class _CtDot1qTpFdbRemoveAddress_Type(TruthValue):defaultValue=2
_CtDot1qTpFdbRemoveAddress_Type.__name__=_T
_CtDot1qTpFdbRemoveAddress_Object=MibTableColumn
ctDot1qTpFdbRemoveAddress=_CtDot1qTpFdbRemoveAddress_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,5,1,1),_CtDot1qTpFdbRemoveAddress_Type())
ctDot1qTpFdbRemoveAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDot1qTpFdbRemoveAddress.setStatus(_A)
_CtDot1qVlanGvrpRestrictedTable_Object=MibTable
ctDot1qVlanGvrpRestrictedTable=_CtDot1qVlanGvrpRestrictedTable_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,6))
if mibBuilder.loadTexts:ctDot1qVlanGvrpRestrictedTable.setStatus(_A)
_CtDot1qVlanGvrpRestrictedEntry_Object=MibTableRow
ctDot1qVlanGvrpRestrictedEntry=_CtDot1qVlanGvrpRestrictedEntry_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,6,1))
ctDot1qVlanGvrpRestrictedEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:ctDot1qVlanGvrpRestrictedEntry.setStatus(_A)
_CtDot1qVlanGvrpRestrictedIndex_Type=VlanIndex
_CtDot1qVlanGvrpRestrictedIndex_Object=MibTableColumn
ctDot1qVlanGvrpRestrictedIndex=_CtDot1qVlanGvrpRestrictedIndex_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,6,1,1),_CtDot1qVlanGvrpRestrictedIndex_Type())
ctDot1qVlanGvrpRestrictedIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:ctDot1qVlanGvrpRestrictedIndex.setStatus(_A)
class _CtDot1qVlanGvrpRestrictedStatus_Type(EnabledStatus):defaultValue=2
_CtDot1qVlanGvrpRestrictedStatus_Type.__name__=_D
_CtDot1qVlanGvrpRestrictedStatus_Object=MibTableColumn
ctDot1qVlanGvrpRestrictedStatus=_CtDot1qVlanGvrpRestrictedStatus_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,6,1,2),_CtDot1qVlanGvrpRestrictedStatus_Type())
ctDot1qVlanGvrpRestrictedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDot1qVlanGvrpRestrictedStatus.setStatus(_A)
_CtDot1qPortVlanStaticEgressTable_Object=MibTable
ctDot1qPortVlanStaticEgressTable=_CtDot1qPortVlanStaticEgressTable_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,7))
if mibBuilder.loadTexts:ctDot1qPortVlanStaticEgressTable.setStatus(_A)
_CtDot1qPortVlanStaticEgressEntry_Object=MibTableRow
ctDot1qPortVlanStaticEgressEntry=_CtDot1qPortVlanStaticEgressEntry_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,7,1))
ctDot1qPortVlanStaticEgressEntry.setIndexNames((0,_J,_K),(0,_E,_L))
if mibBuilder.loadTexts:ctDot1qPortVlanStaticEgressEntry.setStatus(_A)
class _CtDot1qPortVlanStaticEgressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_CtDot1qPortVlanStaticEgressType_Type.__name__=_F
_CtDot1qPortVlanStaticEgressType_Object=MibTableColumn
ctDot1qPortVlanStaticEgressType=_CtDot1qPortVlanStaticEgressType_Object((1,3,6,1,4,1,52,4,1,2,16,7,1,7,1,1),_CtDot1qPortVlanStaticEgressType_Type())
ctDot1qPortVlanStaticEgressType.setMaxAccess(_H)
if mibBuilder.loadTexts:ctDot1qPortVlanStaticEgressType.setStatus(_A)
_CtQBridgeConformance_ObjectIdentity=ObjectIdentity
ctQBridgeConformance=_CtQBridgeConformance_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,7,2))
_CtQBridgeGroups_ObjectIdentity=ObjectIdentity
ctQBridgeGroups=_CtQBridgeGroups_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,7,2,1))
_CtQBridgeCompliances_ObjectIdentity=ObjectIdentity
ctQBridgeCompliances=_CtQBridgeCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,7,2,2))
dot1dBasePortEntry.registerAugmentions((_B,_a))
ctDot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1qVlanCurrentEntry.registerAugmentions((_B,_b))
ctDot1qVlanCurrentEntryExt.setIndexNames(*dot1qVlanCurrentEntry.getIndexNames())
ctQBridgePortGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,1))
ctQBridgePortGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:ctQBridgePortGroup.setStatus(_G)
ctQBridgeVlanGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,2))
ctQBridgeVlanGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:ctQBridgeVlanGroup.setStatus(_A)
ctQBridgePortGroup2=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,3))
ctQBridgePortGroup2.setObjects(*((_B,_M),(_B,_d)))
if mibBuilder.loadTexts:ctQBridgePortGroup2.setStatus(_A)
ctQBridgeVlanCurrentForbidGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,4))
ctQBridgeVlanCurrentForbidGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:ctQBridgeVlanCurrentForbidGroup.setStatus(_A)
ctQBridgePortReplaceTCIGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,5))
ctQBridgePortReplaceTCIGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:ctQBridgePortReplaceTCIGroup.setStatus(_A)
ctQBridgePortVlanEgressGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,6))
ctQBridgePortVlanEgressGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ctQBridgePortVlanEgressGroup.setStatus(_G)
ctQBridgeTpFdbTableExtGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,7))
ctQBridgeTpFdbTableExtGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:ctQBridgeTpFdbTableExtGroup.setStatus(_A)
ctQBridgeVlanGvrpGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,8))
ctQBridgeVlanGvrpGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:ctQBridgeVlanGvrpGroup.setStatus(_A)
ctQBridgePortVlanEgressGroup2=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,7,2,1,9))
ctQBridgePortVlanEgressGroup2.setObjects(*((_B,_N),(_B,_O),(_B,_i)))
if mibBuilder.loadTexts:ctQBridgePortVlanEgressGroup2.setStatus(_A)
ctDot1qVlan=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,7,2,2,1))
ctDot1qVlan.setObjects(*((_B,_j),(_B,_I)))
if mibBuilder.loadTexts:ctDot1qVlan.setStatus(_G)
ctDot1qVlan2=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,7,2,2,2))
ctDot1qVlan2.setObjects(*((_B,_I),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ctDot1qVlan2.setStatus(_G)
ctDot1qVlanCurentCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,7,2,2,3))
ctDot1qVlanCurentCompliance.setObjects((_B,_k))
if mibBuilder.loadTexts:ctDot1qVlanCurentCompliance.setStatus(_A)
ctDot1qPortVlanEgressCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,7,2,2,4))
ctDot1qPortVlanEgressCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:ctDot1qPortVlanEgressCompliance.setStatus(_G)
ctDot1qTpFdbTableExtCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,7,2,2,5))
ctDot1qTpFdbTableExtCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:ctDot1qTpFdbTableExtCompliance.setStatus(_A)
ctDot1qVlan3=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,7,2,2,6))
ctDot1qVlan3.setObjects(*((_B,_I),(_B,_P),(_B,_Q),(_B,_n)))
if mibBuilder.loadTexts:ctDot1qVlan3.setStatus(_A)
ctDot1qPortVlanEgressCompliance2=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,7,2,2,7))
ctDot1qPortVlanEgressCompliance2.setObjects((_B,_o))
if mibBuilder.loadTexts:ctDot1qPortVlanEgressCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ctQBridgeMibExt':ctQBridgeMibExt,'ctQBridgeMIBObjects':ctQBridgeMIBObjects,'ctDot1qPortVlanExtTable':ctDot1qPortVlanExtTable,_a:ctDot1qPortVlanEntry,_M:ctDot1qPortDefaultForwardMode,_d:ctDot1qPortDiscardTagged,_f:ctDot1qPortReplaceTCI,'ctDot1qVlanDynamicEgressTable':ctDot1qVlanDynamicEgressTable,'ctDot1qVlanDynamicEgressEntry':ctDot1qVlanDynamicEgressEntry,_U:ctDot1qVlanDynamicEgressIndex,_c:ctDot1qVlanDynamicEgressStatus,'ctDot1qVlanCurrentExtTable':ctDot1qVlanCurrentExtTable,_b:ctDot1qVlanCurrentEntryExt,_e:ctDot1qVlanForbidEgressPorts,'ctDot1qPortVlanEgressTable':ctDot1qPortVlanEgressTable,'ctDot1qPortVlanEgressEntry':ctDot1qPortVlanEgressEntry,_N:ctDot1qPortVlanEgressStatus,_O:ctDot1qPortVlanEgressType,'ctDot1qTpFdbExtTable':ctDot1qTpFdbExtTable,'ctDot1qTpFdbExtEntry':ctDot1qTpFdbExtEntry,_g:ctDot1qTpFdbRemoveAddress,'ctDot1qVlanGvrpRestrictedTable':ctDot1qVlanGvrpRestrictedTable,'ctDot1qVlanGvrpRestrictedEntry':ctDot1qVlanGvrpRestrictedEntry,_Z:ctDot1qVlanGvrpRestrictedIndex,_h:ctDot1qVlanGvrpRestrictedStatus,'ctDot1qPortVlanStaticEgressTable':ctDot1qPortVlanStaticEgressTable,'ctDot1qPortVlanStaticEgressEntry':ctDot1qPortVlanStaticEgressEntry,_i:ctDot1qPortVlanStaticEgressType,'ctQBridgeConformance':ctQBridgeConformance,'ctQBridgeGroups':ctQBridgeGroups,_j:ctQBridgePortGroup,_I:ctQBridgeVlanGroup,_P:ctQBridgePortGroup2,_k:ctQBridgeVlanCurrentForbidGroup,_Q:ctQBridgePortReplaceTCIGroup,_l:ctQBridgePortVlanEgressGroup,_m:ctQBridgeTpFdbTableExtGroup,_n:ctQBridgeVlanGvrpGroup,_o:ctQBridgePortVlanEgressGroup2,'ctQBridgeCompliances':ctQBridgeCompliances,'ctDot1qVlan':ctDot1qVlan,'ctDot1qVlan2':ctDot1qVlan2,'ctDot1qVlanCurentCompliance':ctDot1qVlanCurentCompliance,'ctDot1qPortVlanEgressCompliance':ctDot1qPortVlanEgressCompliance,'ctDot1qTpFdbTableExtCompliance':ctDot1qTpFdbTableExtCompliance,'ctDot1qVlan3':ctDot1qVlan3,'ctDot1qPortVlanEgressCompliance2':ctDot1qPortVlanEgressCompliance2})