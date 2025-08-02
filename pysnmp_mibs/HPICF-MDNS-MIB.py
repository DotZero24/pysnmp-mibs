_Y='hpicfMdnsProfileRuleGroup'
_X='hpicfMdnsProfileGroup'
_W='hpicfMdnsScalarGroup'
_V='hpicfMdnsProfileRuleRowStatus'
_U='hpicfMdnsProfileRuleAction'
_T='hpicfMdnsProfileRuleInstance'
_S='hpicfMdnsProfileRuleService'
_R='hpicfMdnsProfileVIDList'
_Q='hpicfMdnsProfileRowStatus'
_P='hpicfMdnsGatewayVIDList'
_O='hpicfMdnsDefaultFilterOutAction'
_N='hpicfMdnsDefaultFilterInAction'
_M='hpicfMdnsAdminState'
_L='hpicfMdnsProfileRuleIndex'
_K='not-accessible'
_J='DisplayString'
_I='hpicfMdnsProfileName'
_H='permit'
_G='deny'
_F='OctetString'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='HPICF-MDNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VidList,=mibBuilder.importSymbols('HP-ICF-FTRCO','VidList')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
hpicfMdns=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,124))
if mibBuilder.loadTexts:hpicfMdns.setRevisions(('2015-05-19 00:00',))
_HpicfMdnsNotifications_ObjectIdentity=ObjectIdentity
hpicfMdnsNotifications=_HpicfMdnsNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,124,0))
_HpicfMdnsObjects_ObjectIdentity=ObjectIdentity
hpicfMdnsObjects=_HpicfMdnsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,124,1))
class _HpicfMdnsAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfMdnsAdminState_Type.__name__=_C
_HpicfMdnsAdminState_Object=MibScalar
hpicfMdnsAdminState=_HpicfMdnsAdminState_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,1),_HpicfMdnsAdminState_Type())
hpicfMdnsAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMdnsAdminState.setStatus(_A)
class _HpicfMdnsDefaultFilterInAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpicfMdnsDefaultFilterInAction_Type.__name__=_C
_HpicfMdnsDefaultFilterInAction_Object=MibScalar
hpicfMdnsDefaultFilterInAction=_HpicfMdnsDefaultFilterInAction_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,2),_HpicfMdnsDefaultFilterInAction_Type())
hpicfMdnsDefaultFilterInAction.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMdnsDefaultFilterInAction.setStatus(_A)
class _HpicfMdnsDefaultFilterOutAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpicfMdnsDefaultFilterOutAction_Type.__name__=_C
_HpicfMdnsDefaultFilterOutAction_Object=MibScalar
hpicfMdnsDefaultFilterOutAction=_HpicfMdnsDefaultFilterOutAction_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,3),_HpicfMdnsDefaultFilterOutAction_Type())
hpicfMdnsDefaultFilterOutAction.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMdnsDefaultFilterOutAction.setStatus(_A)
_HpicfMdnsGatewayVIDList_Type=VidList
_HpicfMdnsGatewayVIDList_Object=MibScalar
hpicfMdnsGatewayVIDList=_HpicfMdnsGatewayVIDList_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,4),_HpicfMdnsGatewayVIDList_Type())
hpicfMdnsGatewayVIDList.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMdnsGatewayVIDList.setStatus(_A)
_HpicfMdnsProfileTable_Object=MibTable
hpicfMdnsProfileTable=_HpicfMdnsProfileTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,5))
if mibBuilder.loadTexts:hpicfMdnsProfileTable.setStatus(_A)
_HpicfMdnsProfileEntry_Object=MibTableRow
hpicfMdnsProfileEntry=_HpicfMdnsProfileEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,5,1))
hpicfMdnsProfileEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hpicfMdnsProfileEntry.setStatus(_A)
class _HpicfMdnsProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfMdnsProfileName_Type.__name__=_J
_HpicfMdnsProfileName_Object=MibTableColumn
hpicfMdnsProfileName=_HpicfMdnsProfileName_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,5,1,1),_HpicfMdnsProfileName_Type())
hpicfMdnsProfileName.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfMdnsProfileName.setStatus(_A)
_HpicfMdnsProfileRowStatus_Type=RowStatus
_HpicfMdnsProfileRowStatus_Object=MibTableColumn
hpicfMdnsProfileRowStatus=_HpicfMdnsProfileRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,5,1,2),_HpicfMdnsProfileRowStatus_Type())
hpicfMdnsProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMdnsProfileRowStatus.setStatus(_A)
_HpicfMdnsProfileVIDList_Type=VidList
_HpicfMdnsProfileVIDList_Object=MibTableColumn
hpicfMdnsProfileVIDList=_HpicfMdnsProfileVIDList_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,5,1,3),_HpicfMdnsProfileVIDList_Type())
hpicfMdnsProfileVIDList.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMdnsProfileVIDList.setStatus(_A)
_HpicfMdnsProfileRuleTable_Object=MibTable
hpicfMdnsProfileRuleTable=_HpicfMdnsProfileRuleTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,6))
if mibBuilder.loadTexts:hpicfMdnsProfileRuleTable.setStatus(_A)
_HpicfMdnsProfileRuleEntry_Object=MibTableRow
hpicfMdnsProfileRuleEntry=_HpicfMdnsProfileRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,6,1))
hpicfMdnsProfileRuleEntry.setIndexNames((0,_B,_I),(0,_B,_L))
if mibBuilder.loadTexts:hpicfMdnsProfileRuleEntry.setStatus(_A)
class _HpicfMdnsProfileRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_HpicfMdnsProfileRuleIndex_Type.__name__=_C
_HpicfMdnsProfileRuleIndex_Object=MibTableColumn
hpicfMdnsProfileRuleIndex=_HpicfMdnsProfileRuleIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,6,1,1),_HpicfMdnsProfileRuleIndex_Type())
hpicfMdnsProfileRuleIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfMdnsProfileRuleIndex.setStatus(_A)
class _HpicfMdnsProfileRuleService_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfMdnsProfileRuleService_Type.__name__=_F
_HpicfMdnsProfileRuleService_Object=MibTableColumn
hpicfMdnsProfileRuleService=_HpicfMdnsProfileRuleService_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,6,1,2),_HpicfMdnsProfileRuleService_Type())
hpicfMdnsProfileRuleService.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMdnsProfileRuleService.setStatus(_A)
class _HpicfMdnsProfileRuleInstance_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfMdnsProfileRuleInstance_Type.__name__=_F
_HpicfMdnsProfileRuleInstance_Object=MibTableColumn
hpicfMdnsProfileRuleInstance=_HpicfMdnsProfileRuleInstance_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,6,1,3),_HpicfMdnsProfileRuleInstance_Type())
hpicfMdnsProfileRuleInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMdnsProfileRuleInstance.setStatus(_A)
class _HpicfMdnsProfileRuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpicfMdnsProfileRuleAction_Type.__name__=_C
_HpicfMdnsProfileRuleAction_Object=MibTableColumn
hpicfMdnsProfileRuleAction=_HpicfMdnsProfileRuleAction_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,6,1,4),_HpicfMdnsProfileRuleAction_Type())
hpicfMdnsProfileRuleAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMdnsProfileRuleAction.setStatus(_A)
_HpicfMdnsProfileRuleRowStatus_Type=RowStatus
_HpicfMdnsProfileRuleRowStatus_Object=MibTableColumn
hpicfMdnsProfileRuleRowStatus=_HpicfMdnsProfileRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,124,1,6,1,5),_HpicfMdnsProfileRuleRowStatus_Type())
hpicfMdnsProfileRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMdnsProfileRuleRowStatus.setStatus(_A)
_HpicfMdnsConformance_ObjectIdentity=ObjectIdentity
hpicfMdnsConformance=_HpicfMdnsConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,124,2))
_HpicfMdnsCompliances_ObjectIdentity=ObjectIdentity
hpicfMdnsCompliances=_HpicfMdnsCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,124,2,1))
_HpicfMdnsGroups_ObjectIdentity=ObjectIdentity
hpicfMdnsGroups=_HpicfMdnsGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,124,2,2))
hpicfMdnsScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,124,2,2,1))
hpicfMdnsScalarGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpicfMdnsScalarGroup.setStatus(_A)
hpicfMdnsProfileGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,124,2,2,2))
hpicfMdnsProfileGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpicfMdnsProfileGroup.setStatus(_A)
hpicfMdnsProfileRuleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,124,2,2,3))
hpicfMdnsProfileRuleGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:hpicfMdnsProfileRuleGroup.setStatus(_A)
hpicfMdnsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,124,2,1,1))
hpicfMdnsCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hpicfMdnsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfMdns':hpicfMdns,'hpicfMdnsNotifications':hpicfMdnsNotifications,'hpicfMdnsObjects':hpicfMdnsObjects,_M:hpicfMdnsAdminState,_N:hpicfMdnsDefaultFilterInAction,_O:hpicfMdnsDefaultFilterOutAction,_P:hpicfMdnsGatewayVIDList,'hpicfMdnsProfileTable':hpicfMdnsProfileTable,'hpicfMdnsProfileEntry':hpicfMdnsProfileEntry,_I:hpicfMdnsProfileName,_Q:hpicfMdnsProfileRowStatus,_R:hpicfMdnsProfileVIDList,'hpicfMdnsProfileRuleTable':hpicfMdnsProfileRuleTable,'hpicfMdnsProfileRuleEntry':hpicfMdnsProfileRuleEntry,_L:hpicfMdnsProfileRuleIndex,_S:hpicfMdnsProfileRuleService,_T:hpicfMdnsProfileRuleInstance,_U:hpicfMdnsProfileRuleAction,_V:hpicfMdnsProfileRuleRowStatus,'hpicfMdnsConformance':hpicfMdnsConformance,'hpicfMdnsCompliances':hpicfMdnsCompliances,'hpicfMdnsCompliance':hpicfMdnsCompliance,'hpicfMdnsGroups':hpicfMdnsGroups,_W:hpicfMdnsScalarGroup,_X:hpicfMdnsProfileGroup,_Y:hpicfMdnsProfileRuleGroup})