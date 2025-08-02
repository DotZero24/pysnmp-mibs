_P='hqosHQosInterface'
_O='hqosHQosFlowClassName'
_N='hqosPriorityFlowClass'
_M='hqosShapingProfileName'
_L='hqosWfqProfileName'
_K='hqosWredColor'
_J='notconfig'
_I='hqosHQosPolicyName'
_H='hqosPriorityProfileName'
_G='hqosWredProfileName'
_F='hqosFlowClassName'
_E='HQOS-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
zxr10switch,=mibBuilder.importSymbols('ZXR10-SMI','zxr10switch')
_Hqos_ObjectIdentity=ObjectIdentity
hqos=_Hqos_ObjectIdentity((1,3,6,1,4,1,3902,3,102,16))
_HqosFlowClassTable_Object=MibTable
hqosFlowClassTable=_HqosFlowClassTable_Object((1,3,6,1,4,1,3902,3,102,16,1))
if mibBuilder.loadTexts:hqosFlowClassTable.setStatus(_A)
_HqosFlowClassEntry_Object=MibTableRow
hqosFlowClassEntry=_HqosFlowClassEntry_Object((1,3,6,1,4,1,3902,3,102,16,1,1))
hqosFlowClassEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hqosFlowClassEntry.setStatus(_A)
class _HqosFlowClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosFlowClassName_Type.__name__=_C
_HqosFlowClassName_Object=MibTableColumn
hqosFlowClassName=_HqosFlowClassName_Object((1,3,6,1,4,1,3902,3,102,16,1,1,1),_HqosFlowClassName_Type())
hqosFlowClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosFlowClassName.setStatus(_A)
_HqosFlowMatchTable_Object=MibTable
hqosFlowMatchTable=_HqosFlowMatchTable_Object((1,3,6,1,4,1,3902,3,102,16,2))
if mibBuilder.loadTexts:hqosFlowMatchTable.setStatus(_A)
_HqosFlowMatchEntry_Object=MibTableRow
hqosFlowMatchEntry=_HqosFlowMatchEntry_Object((1,3,6,1,4,1,3902,3,102,16,2,1))
hqosFlowMatchEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hqosFlowMatchEntry.setStatus(_A)
class _HqosMatchFlowclass_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosMatchFlowclass_Type.__name__=_C
_HqosMatchFlowclass_Object=MibTableColumn
hqosMatchFlowclass=_HqosMatchFlowclass_Object((1,3,6,1,4,1,3902,3,102,16,2,1,1),_HqosMatchFlowclass_Type())
hqosMatchFlowclass.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchFlowclass.setStatus(_A)
class _HqosMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,5,6,7)));namedValues=NamedValues(*(('unvalid',0),('acl',1),('vlan',3),('phb',5),('svlan',6),('cvlan',7)))
_HqosMatchType_Type.__name__=_D
_HqosMatchType_Object=MibTableColumn
hqosMatchType=_HqosMatchType_Object((1,3,6,1,4,1,3902,3,102,16,2,1,2),_HqosMatchType_Type())
hqosMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchType.setStatus(_A)
_HqosMatchAclNo_Type=Integer32
_HqosMatchAclNo_Object=MibTableColumn
hqosMatchAclNo=_HqosMatchAclNo_Object((1,3,6,1,4,1,3902,3,102,16,2,1,3),_HqosMatchAclNo_Type())
hqosMatchAclNo.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchAclNo.setStatus(_A)
_HqosMatchRuleNo_Type=Integer32
_HqosMatchRuleNo_Object=MibTableColumn
hqosMatchRuleNo=_HqosMatchRuleNo_Object((1,3,6,1,4,1,3902,3,102,16,2,1,4),_HqosMatchRuleNo_Type())
hqosMatchRuleNo.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchRuleNo.setStatus(_A)
class _HqosMatchVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HqosMatchVlanID_Type.__name__=_D
_HqosMatchVlanID_Object=MibTableColumn
hqosMatchVlanID=_HqosMatchVlanID_Object((1,3,6,1,4,1,3902,3,102,16,2,1,5),_HqosMatchVlanID_Type())
hqosMatchVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchVlanID.setStatus(_A)
class _HqosMatchPhb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('be',0),('af1',1),('af2',2),('af3',3),('af4',4),('ef',5),('cs6',6),('cs7',7),(_J,8)))
_HqosMatchPhb_Type.__name__=_D
_HqosMatchPhb_Object=MibTableColumn
hqosMatchPhb=_HqosMatchPhb_Object((1,3,6,1,4,1,3902,3,102,16,2,1,6),_HqosMatchPhb_Type())
hqosMatchPhb.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchPhb.setStatus(_A)
class _HqosMatchSvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HqosMatchSvlan_Type.__name__=_D
_HqosMatchSvlan_Object=MibTableColumn
hqosMatchSvlan=_HqosMatchSvlan_Object((1,3,6,1,4,1,3902,3,102,16,2,1,7),_HqosMatchSvlan_Type())
hqosMatchSvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchSvlan.setStatus(_A)
class _HqosMatchCvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HqosMatchCvlan_Type.__name__=_D
_HqosMatchCvlan_Object=MibTableColumn
hqosMatchCvlan=_HqosMatchCvlan_Object((1,3,6,1,4,1,3902,3,102,16,2,1,8),_HqosMatchCvlan_Type())
hqosMatchCvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosMatchCvlan.setStatus(_A)
_HqosWredTable_Object=MibTable
hqosWredTable=_HqosWredTable_Object((1,3,6,1,4,1,3902,3,102,16,3))
if mibBuilder.loadTexts:hqosWredTable.setStatus(_A)
_HqosWredEntry_Object=MibTableRow
hqosWredEntry=_HqosWredEntry_Object((1,3,6,1,4,1,3902,3,102,16,3,1))
hqosWredEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hqosWredEntry.setStatus(_A)
class _HqosWredProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosWredProfileName_Type.__name__=_C
_HqosWredProfileName_Object=MibTableColumn
hqosWredProfileName=_HqosWredProfileName_Object((1,3,6,1,4,1,3902,3,102,16,3,1,1),_HqosWredProfileName_Type())
hqosWredProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWredProfileName.setStatus(_A)
class _HqosWredLevelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_HqosWredLevelID_Type.__name__=_D
_HqosWredLevelID_Object=MibTableColumn
hqosWredLevelID=_HqosWredLevelID_Object((1,3,6,1,4,1,3902,3,102,16,3,1,2),_HqosWredLevelID_Type())
hqosWredLevelID.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWredLevelID.setStatus(_A)
_HqosWredColorTable_Object=MibTable
hqosWredColorTable=_HqosWredColorTable_Object((1,3,6,1,4,1,3902,3,102,16,4))
if mibBuilder.loadTexts:hqosWredColorTable.setStatus(_A)
_HqosWredColorEntry_Object=MibTableRow
hqosWredColorEntry=_HqosWredColorEntry_Object((1,3,6,1,4,1,3902,3,102,16,4,1))
hqosWredColorEntry.setIndexNames((0,_E,_G),(0,_E,_K))
if mibBuilder.loadTexts:hqosWredColorEntry.setStatus(_A)
class _HqosWredColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('red',1),('yellow',2),('green',3),(_J,4)))
_HqosWredColor_Type.__name__=_D
_HqosWredColor_Object=MibTableColumn
hqosWredColor=_HqosWredColor_Object((1,3,6,1,4,1,3902,3,102,16,4,1,1),_HqosWredColor_Type())
hqosWredColor.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWredColor.setStatus(_A)
class _HqosWredMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_HqosWredMin_Type.__name__=_D
_HqosWredMin_Object=MibTableColumn
hqosWredMin=_HqosWredMin_Object((1,3,6,1,4,1,3902,3,102,16,4,1,2),_HqosWredMin_Type())
hqosWredMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWredMin.setStatus(_A)
class _HqosWredMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_HqosWredMax_Type.__name__=_D
_HqosWredMax_Object=MibTableColumn
hqosWredMax=_HqosWredMax_Object((1,3,6,1,4,1,3902,3,102,16,4,1,3),_HqosWredMax_Type())
hqosWredMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWredMax.setStatus(_A)
class _HqosWredPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HqosWredPercent_Type.__name__=_D
_HqosWredPercent_Object=MibTableColumn
hqosWredPercent=_HqosWredPercent_Object((1,3,6,1,4,1,3902,3,102,16,4,1,4),_HqosWredPercent_Type())
hqosWredPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWredPercent.setStatus(_A)
_HqosWfqTable_Object=MibTable
hqosWfqTable=_HqosWfqTable_Object((1,3,6,1,4,1,3902,3,102,16,5))
if mibBuilder.loadTexts:hqosWfqTable.setStatus(_A)
_HqosWfqEntry_Object=MibTableRow
hqosWfqEntry=_HqosWfqEntry_Object((1,3,6,1,4,1,3902,3,102,16,5,1))
hqosWfqEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hqosWfqEntry.setStatus(_A)
class _HqosWfqProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosWfqProfileName_Type.__name__=_C
_HqosWfqProfileName_Object=MibTableColumn
hqosWfqProfileName=_HqosWfqProfileName_Object((1,3,6,1,4,1,3902,3,102,16,5,1,1),_HqosWfqProfileName_Type())
hqosWfqProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWfqProfileName.setStatus(_A)
class _HqosWfqLevelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_HqosWfqLevelID_Type.__name__=_D
_HqosWfqLevelID_Object=MibTableColumn
hqosWfqLevelID=_HqosWfqLevelID_Object((1,3,6,1,4,1,3902,3,102,16,5,1,2),_HqosWfqLevelID_Type())
hqosWfqLevelID.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWfqLevelID.setStatus(_A)
class _HqosWfqWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HqosWfqWeight_Type.__name__=_D
_HqosWfqWeight_Object=MibTableColumn
hqosWfqWeight=_HqosWfqWeight_Object((1,3,6,1,4,1,3902,3,102,16,5,1,3),_HqosWfqWeight_Type())
hqosWfqWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosWfqWeight.setStatus(_A)
_HqosShapingTable_Object=MibTable
hqosShapingTable=_HqosShapingTable_Object((1,3,6,1,4,1,3902,3,102,16,6))
if mibBuilder.loadTexts:hqosShapingTable.setStatus(_A)
_HqosShapingEntry_Object=MibTableRow
hqosShapingEntry=_HqosShapingEntry_Object((1,3,6,1,4,1,3902,3,102,16,6,1))
hqosShapingEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:hqosShapingEntry.setStatus(_A)
class _HqosShapingProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosShapingProfileName_Type.__name__=_C
_HqosShapingProfileName_Object=MibTableColumn
hqosShapingProfileName=_HqosShapingProfileName_Object((1,3,6,1,4,1,3902,3,102,16,6,1,1),_HqosShapingProfileName_Type())
hqosShapingProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosShapingProfileName.setStatus(_A)
class _HqosShapingLevelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_HqosShapingLevelID_Type.__name__=_D
_HqosShapingLevelID_Object=MibTableColumn
hqosShapingLevelID=_HqosShapingLevelID_Object((1,3,6,1,4,1,3902,3,102,16,6,1,2),_HqosShapingLevelID_Type())
hqosShapingLevelID.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosShapingLevelID.setStatus(_A)
class _HqosShapingCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,10000000))
_HqosShapingCir_Type.__name__=_D
_HqosShapingCir_Object=MibTableColumn
hqosShapingCir=_HqosShapingCir_Object((1,3,6,1,4,1,3902,3,102,16,6,1,3),_HqosShapingCir_Type())
hqosShapingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosShapingCir.setStatus(_A)
class _HqosShapingCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,16711680))
_HqosShapingCbs_Type.__name__=_D
_HqosShapingCbs_Object=MibTableColumn
hqosShapingCbs=_HqosShapingCbs_Object((1,3,6,1,4,1,3902,3,102,16,6,1,4),_HqosShapingCbs_Type())
hqosShapingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosShapingCbs.setStatus(_A)
class _HqosShapingPir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,10000000))
_HqosShapingPir_Type.__name__=_D
_HqosShapingPir_Object=MibTableColumn
hqosShapingPir=_HqosShapingPir_Object((1,3,6,1,4,1,3902,3,102,16,6,1,5),_HqosShapingPir_Type())
hqosShapingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosShapingPir.setStatus(_A)
class _HqosShapingPbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,16711680))
_HqosShapingPbs_Type.__name__=_D
_HqosShapingPbs_Object=MibTableColumn
hqosShapingPbs=_HqosShapingPbs_Object((1,3,6,1,4,1,3902,3,102,16,6,1,6),_HqosShapingPbs_Type())
hqosShapingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosShapingPbs.setStatus(_A)
_HqosPriorityTable_Object=MibTable
hqosPriorityTable=_HqosPriorityTable_Object((1,3,6,1,4,1,3902,3,102,16,7))
if mibBuilder.loadTexts:hqosPriorityTable.setStatus(_A)
_HqosPriorityEntry_Object=MibTableRow
hqosPriorityEntry=_HqosPriorityEntry_Object((1,3,6,1,4,1,3902,3,102,16,7,1))
hqosPriorityEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hqosPriorityEntry.setStatus(_A)
class _HqosPriorityProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosPriorityProfileName_Type.__name__=_C
_HqosPriorityProfileName_Object=MibTableColumn
hqosPriorityProfileName=_HqosPriorityProfileName_Object((1,3,6,1,4,1,3902,3,102,16,7,1,1),_HqosPriorityProfileName_Type())
hqosPriorityProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosPriorityProfileName.setStatus(_A)
_HqosPriorityFlowTable_Object=MibTable
hqosPriorityFlowTable=_HqosPriorityFlowTable_Object((1,3,6,1,4,1,3902,3,102,16,8))
if mibBuilder.loadTexts:hqosPriorityFlowTable.setStatus(_A)
_HqosPriorityFlowEntry_Object=MibTableRow
hqosPriorityFlowEntry=_HqosPriorityFlowEntry_Object((1,3,6,1,4,1,3902,3,102,16,8,1))
hqosPriorityFlowEntry.setIndexNames((0,_E,_H),(0,_E,_N))
if mibBuilder.loadTexts:hqosPriorityFlowEntry.setStatus(_A)
class _HqosPriorityFlowClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('be',0),('af1',1),('af2',2),('af3',3),('af4',4),('ef',5),('cs6',6),('cs7',7)))
_HqosPriorityFlowClass_Type.__name__=_D
_HqosPriorityFlowClass_Object=MibTableColumn
hqosPriorityFlowClass=_HqosPriorityFlowClass_Object((1,3,6,1,4,1,3902,3,102,16,8,1,1),_HqosPriorityFlowClass_Type())
hqosPriorityFlowClass.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosPriorityFlowClass.setStatus(_A)
class _HqosPriorityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('single',0),('dual',1)))
_HqosPriorityMode_Type.__name__=_D
_HqosPriorityMode_Object=MibTableColumn
hqosPriorityMode=_HqosPriorityMode_Object((1,3,6,1,4,1,3902,3,102,16,8,1,2),_HqosPriorityMode_Type())
hqosPriorityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosPriorityMode.setStatus(_A)
class _HqosPriorityGreen_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosPriorityGreen_Type.__name__=_C
_HqosPriorityGreen_Object=MibTableColumn
hqosPriorityGreen=_HqosPriorityGreen_Object((1,3,6,1,4,1,3902,3,102,16,8,1,3),_HqosPriorityGreen_Type())
hqosPriorityGreen.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosPriorityGreen.setStatus(_A)
class _HqosPriorityYellow_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosPriorityYellow_Type.__name__=_C
_HqosPriorityYellow_Object=MibTableColumn
hqosPriorityYellow=_HqosPriorityYellow_Object((1,3,6,1,4,1,3902,3,102,16,8,1,4),_HqosPriorityYellow_Type())
hqosPriorityYellow.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosPriorityYellow.setStatus(_A)
_HqosHQosTable_Object=MibTable
hqosHQosTable=_HqosHQosTable_Object((1,3,6,1,4,1,3902,3,102,16,9))
if mibBuilder.loadTexts:hqosHQosTable.setStatus(_A)
_HqosHQosEntry_Object=MibTableRow
hqosHQosEntry=_HqosHQosEntry_Object((1,3,6,1,4,1,3902,3,102,16,9,1))
hqosHQosEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hqosHQosEntry.setStatus(_A)
class _HqosHQosPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosPolicyName_Type.__name__=_C
_HqosHQosPolicyName_Object=MibTableColumn
hqosHQosPolicyName=_HqosHQosPolicyName_Object((1,3,6,1,4,1,3902,3,102,16,9,1,1),_HqosHQosPolicyName_Type())
hqosHQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosPolicyName.setStatus(_A)
class _HqosHQosLevelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_HqosHQosLevelID_Type.__name__=_D
_HqosHQosLevelID_Object=MibTableColumn
hqosHQosLevelID=_HqosHQosLevelID_Object((1,3,6,1,4,1,3902,3,102,16,9,1,2),_HqosHQosLevelID_Type())
hqosHQosLevelID.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosLevelID.setStatus(_A)
class _HqosHQosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('svlan',2)))
_HqosHQosMode_Type.__name__=_D
_HqosHQosMode_Object=MibTableColumn
hqosHQosMode=_HqosHQosMode_Object((1,3,6,1,4,1,3902,3,102,16,9,1,3),_HqosHQosMode_Type())
hqosHQosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosMode.setStatus(_A)
class _HqosHQosDiscripString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,200))
_HqosHQosDiscripString_Type.__name__=_C
_HqosHQosDiscripString_Object=MibTableColumn
hqosHQosDiscripString=_HqosHQosDiscripString_Object((1,3,6,1,4,1,3902,3,102,16,9,1,4),_HqosHQosDiscripString_Type())
hqosHQosDiscripString.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosDiscripString.setStatus(_A)
_HqosHQosFlowTable_Object=MibTable
hqosHQosFlowTable=_HqosHQosFlowTable_Object((1,3,6,1,4,1,3902,3,102,16,10))
if mibBuilder.loadTexts:hqosHQosFlowTable.setStatus(_A)
_HqosHQosFlowEntry_Object=MibTableRow
hqosHQosFlowEntry=_HqosHQosFlowEntry_Object((1,3,6,1,4,1,3902,3,102,16,10,1))
hqosHQosFlowEntry.setIndexNames((0,_E,_I),(0,_E,_O))
if mibBuilder.loadTexts:hqosHQosFlowEntry.setStatus(_A)
class _HqosHQosFlowClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosFlowClassName_Type.__name__=_C
_HqosHQosFlowClassName_Object=MibTableColumn
hqosHQosFlowClassName=_HqosHQosFlowClassName_Object((1,3,6,1,4,1,3902,3,102,16,10,1,1),_HqosHQosFlowClassName_Type())
hqosHQosFlowClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosFlowClassName.setStatus(_A)
class _HqosHQosFlowPriority_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosFlowPriority_Type.__name__=_C
_HqosHQosFlowPriority_Object=MibTableColumn
hqosHQosFlowPriority=_HqosHQosFlowPriority_Object((1,3,6,1,4,1,3902,3,102,16,10,1,2),_HqosHQosFlowPriority_Type())
hqosHQosFlowPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosFlowPriority.setStatus(_A)
class _HqosHQosFlowWredProfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosFlowWredProfName_Type.__name__=_C
_HqosHQosFlowWredProfName_Object=MibTableColumn
hqosHQosFlowWredProfName=_HqosHQosFlowWredProfName_Object((1,3,6,1,4,1,3902,3,102,16,10,1,3),_HqosHQosFlowWredProfName_Type())
hqosHQosFlowWredProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosFlowWredProfName.setStatus(_A)
class _HqosHQosFlowWfqProfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosFlowWfqProfName_Type.__name__=_C
_HqosHQosFlowWfqProfName_Object=MibTableColumn
hqosHQosFlowWfqProfName=_HqosHQosFlowWfqProfName_Object((1,3,6,1,4,1,3902,3,102,16,10,1,4),_HqosHQosFlowWfqProfName_Type())
hqosHQosFlowWfqProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosFlowWfqProfName.setStatus(_A)
class _HqosHQosFlowShapingProfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosFlowShapingProfName_Type.__name__=_C
_HqosHQosFlowShapingProfName_Object=MibTableColumn
hqosHQosFlowShapingProfName=_HqosHQosFlowShapingProfName_Object((1,3,6,1,4,1,3902,3,102,16,10,1,5),_HqosHQosFlowShapingProfName_Type())
hqosHQosFlowShapingProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosFlowShapingProfName.setStatus(_A)
class _HqosHQosFlowPriorityProfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosFlowPriorityProfName_Type.__name__=_C
_HqosHQosFlowPriorityProfName_Object=MibTableColumn
hqosHQosFlowPriorityProfName=_HqosHQosFlowPriorityProfName_Object((1,3,6,1,4,1,3902,3,102,16,10,1,6),_HqosHQosFlowPriorityProfName_Type())
hqosHQosFlowPriorityProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosFlowPriorityProfName.setStatus(_A)
class _HqosHQosSubPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosSubPolicyName_Type.__name__=_C
_HqosHQosSubPolicyName_Object=MibTableColumn
hqosHQosSubPolicyName=_HqosHQosSubPolicyName_Object((1,3,6,1,4,1,3902,3,102,16,10,1,7),_HqosHQosSubPolicyName_Type())
hqosHQosSubPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosSubPolicyName.setStatus(_A)
_HqosHQosInterfaceTable_Object=MibTable
hqosHQosInterfaceTable=_HqosHQosInterfaceTable_Object((1,3,6,1,4,1,3902,3,102,16,11))
if mibBuilder.loadTexts:hqosHQosInterfaceTable.setStatus(_A)
_HqosHQosInterfaceEntry_Object=MibTableRow
hqosHQosInterfaceEntry=_HqosHQosInterfaceEntry_Object((1,3,6,1,4,1,3902,3,102,16,11,1))
hqosHQosInterfaceEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hqosHQosInterfaceEntry.setStatus(_A)
class _HqosHQosInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosInterface_Type.__name__=_C
_HqosHQosInterface_Object=MibTableColumn
hqosHQosInterface=_HqosHQosInterface_Object((1,3,6,1,4,1,3902,3,102,16,11,1,1),_HqosHQosInterface_Type())
hqosHQosInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosInterface.setStatus(_A)
class _HqosHQosPolicyNameIN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosPolicyNameIN_Type.__name__=_C
_HqosHQosPolicyNameIN_Object=MibTableColumn
hqosHQosPolicyNameIN=_HqosHQosPolicyNameIN_Object((1,3,6,1,4,1,3902,3,102,16,11,1,2),_HqosHQosPolicyNameIN_Type())
hqosHQosPolicyNameIN.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosPolicyNameIN.setStatus(_A)
class _HqosInterfaceShapingIN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosInterfaceShapingIN_Type.__name__=_C
_HqosInterfaceShapingIN_Object=MibTableColumn
hqosInterfaceShapingIN=_HqosInterfaceShapingIN_Object((1,3,6,1,4,1,3902,3,102,16,11,1,3),_HqosInterfaceShapingIN_Type())
hqosInterfaceShapingIN.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosInterfaceShapingIN.setStatus(_A)
class _HqosHQosPolicyNameOUT_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosHQosPolicyNameOUT_Type.__name__=_C
_HqosHQosPolicyNameOUT_Object=MibTableColumn
hqosHQosPolicyNameOUT=_HqosHQosPolicyNameOUT_Object((1,3,6,1,4,1,3902,3,102,16,11,1,4),_HqosHQosPolicyNameOUT_Type())
hqosHQosPolicyNameOUT.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosHQosPolicyNameOUT.setStatus(_A)
class _HqosInterfaceShapingOUT_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HqosInterfaceShapingOUT_Type.__name__=_C
_HqosInterfaceShapingOUT_Object=MibTableColumn
hqosInterfaceShapingOUT=_HqosInterfaceShapingOUT_Object((1,3,6,1,4,1,3902,3,102,16,11,1,5),_HqosInterfaceShapingOUT_Type())
hqosInterfaceShapingOUT.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosInterfaceShapingOUT.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hqos':hqos,'hqosFlowClassTable':hqosFlowClassTable,'hqosFlowClassEntry':hqosFlowClassEntry,_F:hqosFlowClassName,'hqosFlowMatchTable':hqosFlowMatchTable,'hqosFlowMatchEntry':hqosFlowMatchEntry,'hqosMatchFlowclass':hqosMatchFlowclass,'hqosMatchType':hqosMatchType,'hqosMatchAclNo':hqosMatchAclNo,'hqosMatchRuleNo':hqosMatchRuleNo,'hqosMatchVlanID':hqosMatchVlanID,'hqosMatchPhb':hqosMatchPhb,'hqosMatchSvlan':hqosMatchSvlan,'hqosMatchCvlan':hqosMatchCvlan,'hqosWredTable':hqosWredTable,'hqosWredEntry':hqosWredEntry,_G:hqosWredProfileName,'hqosWredLevelID':hqosWredLevelID,'hqosWredColorTable':hqosWredColorTable,'hqosWredColorEntry':hqosWredColorEntry,_K:hqosWredColor,'hqosWredMin':hqosWredMin,'hqosWredMax':hqosWredMax,'hqosWredPercent':hqosWredPercent,'hqosWfqTable':hqosWfqTable,'hqosWfqEntry':hqosWfqEntry,_L:hqosWfqProfileName,'hqosWfqLevelID':hqosWfqLevelID,'hqosWfqWeight':hqosWfqWeight,'hqosShapingTable':hqosShapingTable,'hqosShapingEntry':hqosShapingEntry,_M:hqosShapingProfileName,'hqosShapingLevelID':hqosShapingLevelID,'hqosShapingCir':hqosShapingCir,'hqosShapingCbs':hqosShapingCbs,'hqosShapingPir':hqosShapingPir,'hqosShapingPbs':hqosShapingPbs,'hqosPriorityTable':hqosPriorityTable,'hqosPriorityEntry':hqosPriorityEntry,_H:hqosPriorityProfileName,'hqosPriorityFlowTable':hqosPriorityFlowTable,'hqosPriorityFlowEntry':hqosPriorityFlowEntry,_N:hqosPriorityFlowClass,'hqosPriorityMode':hqosPriorityMode,'hqosPriorityGreen':hqosPriorityGreen,'hqosPriorityYellow':hqosPriorityYellow,'hqosHQosTable':hqosHQosTable,'hqosHQosEntry':hqosHQosEntry,_I:hqosHQosPolicyName,'hqosHQosLevelID':hqosHQosLevelID,'hqosHQosMode':hqosHQosMode,'hqosHQosDiscripString':hqosHQosDiscripString,'hqosHQosFlowTable':hqosHQosFlowTable,'hqosHQosFlowEntry':hqosHQosFlowEntry,_O:hqosHQosFlowClassName,'hqosHQosFlowPriority':hqosHQosFlowPriority,'hqosHQosFlowWredProfName':hqosHQosFlowWredProfName,'hqosHQosFlowWfqProfName':hqosHQosFlowWfqProfName,'hqosHQosFlowShapingProfName':hqosHQosFlowShapingProfName,'hqosHQosFlowPriorityProfName':hqosHQosFlowPriorityProfName,'hqosHQosSubPolicyName':hqosHQosSubPolicyName,'hqosHQosInterfaceTable':hqosHQosInterfaceTable,'hqosHQosInterfaceEntry':hqosHQosInterfaceEntry,_P:hqosHQosInterface,'hqosHQosPolicyNameIN':hqosHQosPolicyNameIN,'hqosInterfaceShapingIN':hqosInterfaceShapingIN,'hqosHQosPolicyNameOUT':hqosHQosPolicyNameOUT,'hqosInterfaceShapingOUT':hqosInterfaceShapingOUT})