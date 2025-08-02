_a='pxmAcGroup'
_Z='pxmAcFlapActionClear'
_Y='pxmAcSplitHorizonGroupID'
_X='pxmAcPmHistStatsEnable'
_W='pxmAcCreationType'
_V='pxmAcLoopbackBehavior'
_U='pxmAcLoopback'
_T='pxmAcIngressTrafficClass'
_S='pxmAcEgressRewriteInnerPriority'
_R='pxmAcEgressActionInnerPriority'
_Q='pxmAcEgressRewriteOuterPriority'
_P='pxmAcEgressActionOuterPriority'
_O='pxmAcEgressRewriteInnerVlanId'
_N='pxmAcEgressActionInnerVlan'
_M='pxmAcEgressRewriteOuterVlanId'
_L='pxmAcEgressActionOuterVlan'
_K='pxmAcIngressRewriteOuterVlanId'
_J='pxmAcIngressActionOuterVlan'
_I='pxmAcIngressMatchOuterPriority'
_H='pxmAcIngressMatchInnerVlanId'
_G='pxmAcIngressMatchOuterVlanId'
_F='pxmAcIngressMatchCriteria'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-PXMAC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnActionOnVlan,InfnCreationType,InfnEgressActionPriority,InfnFlapActionClear,InfnIngressMatchCriteria,InfnLoopback,InfnLoopbackBehavior,InfnPmHistStatsControl=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnActionOnVlan','InfnCreationType','InfnEgressActionPriority','InfnFlapActionClear','InfnIngressMatchCriteria','InfnLoopback','InfnLoopbackBehavior','InfnPmHistStatsControl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmAcMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,72))
if mibBuilder.loadTexts:pxmAcMIB.setRevisions(('2016-05-15 00:00',))
_PxmAcTable_Object=MibTable
pxmAcTable=_PxmAcTable_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1))
if mibBuilder.loadTexts:pxmAcTable.setStatus(_A)
_PxmAcEntry_Object=MibTableRow
pxmAcEntry=_PxmAcEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1))
pxmAcEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pxmAcEntry.setStatus(_A)
_PxmAcIngressMatchCriteria_Type=InfnIngressMatchCriteria
_PxmAcIngressMatchCriteria_Object=MibTableColumn
pxmAcIngressMatchCriteria=_PxmAcIngressMatchCriteria_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,1),_PxmAcIngressMatchCriteria_Type())
pxmAcIngressMatchCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcIngressMatchCriteria.setStatus(_A)
_PxmAcIngressMatchOuterVlanId_Type=DisplayString
_PxmAcIngressMatchOuterVlanId_Object=MibTableColumn
pxmAcIngressMatchOuterVlanId=_PxmAcIngressMatchOuterVlanId_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,2),_PxmAcIngressMatchOuterVlanId_Type())
pxmAcIngressMatchOuterVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcIngressMatchOuterVlanId.setStatus(_A)
_PxmAcIngressMatchInnerVlanId_Type=DisplayString
_PxmAcIngressMatchInnerVlanId_Object=MibTableColumn
pxmAcIngressMatchInnerVlanId=_PxmAcIngressMatchInnerVlanId_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,3),_PxmAcIngressMatchInnerVlanId_Type())
pxmAcIngressMatchInnerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcIngressMatchInnerVlanId.setStatus(_A)
_PxmAcIngressMatchOuterPriority_Type=DisplayString
_PxmAcIngressMatchOuterPriority_Object=MibTableColumn
pxmAcIngressMatchOuterPriority=_PxmAcIngressMatchOuterPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,4),_PxmAcIngressMatchOuterPriority_Type())
pxmAcIngressMatchOuterPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcIngressMatchOuterPriority.setStatus(_A)
_PxmAcIngressActionOuterVlan_Type=InfnActionOnVlan
_PxmAcIngressActionOuterVlan_Object=MibTableColumn
pxmAcIngressActionOuterVlan=_PxmAcIngressActionOuterVlan_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,5),_PxmAcIngressActionOuterVlan_Type())
pxmAcIngressActionOuterVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcIngressActionOuterVlan.setStatus(_A)
_PxmAcIngressRewriteOuterVlanId_Type=Integer32
_PxmAcIngressRewriteOuterVlanId_Object=MibTableColumn
pxmAcIngressRewriteOuterVlanId=_PxmAcIngressRewriteOuterVlanId_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,6),_PxmAcIngressRewriteOuterVlanId_Type())
pxmAcIngressRewriteOuterVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcIngressRewriteOuterVlanId.setStatus(_A)
_PxmAcEgressActionOuterVlan_Type=InfnActionOnVlan
_PxmAcEgressActionOuterVlan_Object=MibTableColumn
pxmAcEgressActionOuterVlan=_PxmAcEgressActionOuterVlan_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,7),_PxmAcEgressActionOuterVlan_Type())
pxmAcEgressActionOuterVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressActionOuterVlan.setStatus(_A)
_PxmAcEgressRewriteOuterVlanId_Type=Integer32
_PxmAcEgressRewriteOuterVlanId_Object=MibTableColumn
pxmAcEgressRewriteOuterVlanId=_PxmAcEgressRewriteOuterVlanId_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,8),_PxmAcEgressRewriteOuterVlanId_Type())
pxmAcEgressRewriteOuterVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressRewriteOuterVlanId.setStatus(_A)
_PxmAcEgressActionInnerVlan_Type=InfnActionOnVlan
_PxmAcEgressActionInnerVlan_Object=MibTableColumn
pxmAcEgressActionInnerVlan=_PxmAcEgressActionInnerVlan_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,9),_PxmAcEgressActionInnerVlan_Type())
pxmAcEgressActionInnerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressActionInnerVlan.setStatus(_A)
_PxmAcEgressRewriteInnerVlanId_Type=Integer32
_PxmAcEgressRewriteInnerVlanId_Object=MibTableColumn
pxmAcEgressRewriteInnerVlanId=_PxmAcEgressRewriteInnerVlanId_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,10),_PxmAcEgressRewriteInnerVlanId_Type())
pxmAcEgressRewriteInnerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressRewriteInnerVlanId.setStatus(_A)
_PxmAcEgressActionOuterPriority_Type=InfnEgressActionPriority
_PxmAcEgressActionOuterPriority_Object=MibTableColumn
pxmAcEgressActionOuterPriority=_PxmAcEgressActionOuterPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,11),_PxmAcEgressActionOuterPriority_Type())
pxmAcEgressActionOuterPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressActionOuterPriority.setStatus(_A)
_PxmAcEgressRewriteOuterPriority_Type=Integer32
_PxmAcEgressRewriteOuterPriority_Object=MibTableColumn
pxmAcEgressRewriteOuterPriority=_PxmAcEgressRewriteOuterPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,12),_PxmAcEgressRewriteOuterPriority_Type())
pxmAcEgressRewriteOuterPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressRewriteOuterPriority.setStatus(_A)
_PxmAcEgressActionInnerPriority_Type=InfnEgressActionPriority
_PxmAcEgressActionInnerPriority_Object=MibTableColumn
pxmAcEgressActionInnerPriority=_PxmAcEgressActionInnerPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,13),_PxmAcEgressActionInnerPriority_Type())
pxmAcEgressActionInnerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressActionInnerPriority.setStatus(_A)
_PxmAcEgressRewriteInnerPriority_Type=Integer32
_PxmAcEgressRewriteInnerPriority_Object=MibTableColumn
pxmAcEgressRewriteInnerPriority=_PxmAcEgressRewriteInnerPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,14),_PxmAcEgressRewriteInnerPriority_Type())
pxmAcEgressRewriteInnerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcEgressRewriteInnerPriority.setStatus(_A)
_PxmAcIngressTrafficClass_Type=Integer32
_PxmAcIngressTrafficClass_Object=MibTableColumn
pxmAcIngressTrafficClass=_PxmAcIngressTrafficClass_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,15),_PxmAcIngressTrafficClass_Type())
pxmAcIngressTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcIngressTrafficClass.setStatus(_A)
_PxmAcLoopback_Type=InfnLoopback
_PxmAcLoopback_Object=MibTableColumn
pxmAcLoopback=_PxmAcLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,16),_PxmAcLoopback_Type())
pxmAcLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcLoopback.setStatus(_A)
_PxmAcLoopbackBehavior_Type=InfnLoopbackBehavior
_PxmAcLoopbackBehavior_Object=MibTableColumn
pxmAcLoopbackBehavior=_PxmAcLoopbackBehavior_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,17),_PxmAcLoopbackBehavior_Type())
pxmAcLoopbackBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcLoopbackBehavior.setStatus(_A)
_PxmAcCreationType_Type=InfnCreationType
_PxmAcCreationType_Object=MibTableColumn
pxmAcCreationType=_PxmAcCreationType_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,18),_PxmAcCreationType_Type())
pxmAcCreationType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcCreationType.setStatus(_A)
_PxmAcPmHistStatsEnable_Type=InfnPmHistStatsControl
_PxmAcPmHistStatsEnable_Object=MibTableColumn
pxmAcPmHistStatsEnable=_PxmAcPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,19),_PxmAcPmHistStatsEnable_Type())
pxmAcPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcPmHistStatsEnable.setStatus(_A)
_PxmAcSplitHorizonGroupID_Type=Integer32
_PxmAcSplitHorizonGroupID_Object=MibTableColumn
pxmAcSplitHorizonGroupID=_PxmAcSplitHorizonGroupID_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,20),_PxmAcSplitHorizonGroupID_Type())
pxmAcSplitHorizonGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcSplitHorizonGroupID.setStatus(_A)
_PxmAcFlapActionClear_Type=InfnFlapActionClear
_PxmAcFlapActionClear_Object=MibTableColumn
pxmAcFlapActionClear=_PxmAcFlapActionClear_Object((1,3,6,1,4,1,21296,2,2,2,2,72,1,1,21),_PxmAcFlapActionClear_Type())
pxmAcFlapActionClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmAcFlapActionClear.setStatus(_A)
_PxmAcConformance_ObjectIdentity=ObjectIdentity
pxmAcConformance=_PxmAcConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,72,3))
_PxmAcCompliances_ObjectIdentity=ObjectIdentity
pxmAcCompliances=_PxmAcCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,72,3,1))
_PxmAcGroups_ObjectIdentity=ObjectIdentity
pxmAcGroups=_PxmAcGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,72,3,2))
pxmAcGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,72,3,2,1))
pxmAcGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pxmAcGroup.setStatus(_A)
pxmAcCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,72,3,1,1))
pxmAcCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:pxmAcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmAcMIB':pxmAcMIB,'pxmAcTable':pxmAcTable,'pxmAcEntry':pxmAcEntry,_F:pxmAcIngressMatchCriteria,_G:pxmAcIngressMatchOuterVlanId,_H:pxmAcIngressMatchInnerVlanId,_I:pxmAcIngressMatchOuterPriority,_J:pxmAcIngressActionOuterVlan,_K:pxmAcIngressRewriteOuterVlanId,_L:pxmAcEgressActionOuterVlan,_M:pxmAcEgressRewriteOuterVlanId,_N:pxmAcEgressActionInnerVlan,_O:pxmAcEgressRewriteInnerVlanId,_P:pxmAcEgressActionOuterPriority,_Q:pxmAcEgressRewriteOuterPriority,_R:pxmAcEgressActionInnerPriority,_S:pxmAcEgressRewriteInnerPriority,_T:pxmAcIngressTrafficClass,_U:pxmAcLoopback,_V:pxmAcLoopbackBehavior,_W:pxmAcCreationType,_X:pxmAcPmHistStatsEnable,_Y:pxmAcSplitHorizonGroupID,_Z:pxmAcFlapActionClear,'pxmAcConformance':pxmAcConformance,'pxmAcCompliances':pxmAcCompliances,'pxmAcCompliance':pxmAcCompliance,'pxmAcGroups':pxmAcGroups,_a:pxmAcGroup})