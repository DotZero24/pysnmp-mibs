_Z='ctPriClassifyBaseGroup'
_Y='ctPriClassifyTableLastChange'
_X='ctPriClassifyPorts'
_W='ctPriClassifyTOSValue'
_V='ctPriClassifyTOSStatus'
_U='ctPriClassifyRowInfo'
_T='ctPriClassifyRowStatus'
_S='ctPriClassifyIngressList'
_R='ctPriClassifyNumEntries'
_Q='ctPriClassifyMaxEntries'
_P='ctPriClassifyStatus'
_O='ctPriClassifyAbility'
_N='read-create'
_M='PortList'
_L='ctPriClassifyDataMask'
_K='ctPriClassifyDataVal'
_J='ctPriClassifyDataMeaning'
_I='ctPriClassifyPriority'
_H='disable'
_G='enable'
_F='read-write'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='CTRON-PRIORITY-CLASSIFY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctPriorityExt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctPriorityExt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ctPriClassify=ModuleIdentity((1,3,6,1,4,1,52,4,1,2,14,6))
class CtPriClassifyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('etherType',1),('llcDsapSsap',2),('ipTypeOfService',3),('ipProtocolType',4),('ipxClassOfService',5),('ipxPacketType',6),('ipAddressSource',7),('ipAddressDestination',8),('ipAddressBilateral',9),('ipxNetworkSource',10),('ipxNetworkDestination',11),('ipxNetworkBilateral',12),('ipUdpPortSource',13),('ipUdpPortDestination',14),('ipUdpPortBilateral',15),('ipTcpPortSource',16),('ipTcpPortDestination',17),('ipTcpPortBilateral',18),('ipxSocketSource',19),('ipxSocketDestination',20),('ipxSocketBilateral',21),('macAddressSource',22),('macAddressDestination',23),('macAddressBilateral',24),('ipFragments',25)))
class PortList(TextualConvention,OctetString):status=_A
_CtPriClassifyObjects_ObjectIdentity=ObjectIdentity
ctPriClassifyObjects=_CtPriClassifyObjects_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,6,1))
class _CtPriClassifyStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtPriClassifyStatus_Type.__name__=_C
_CtPriClassifyStatus_Object=MibScalar
ctPriClassifyStatus=_CtPriClassifyStatus_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,1),_CtPriClassifyStatus_Type())
ctPriClassifyStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ctPriClassifyStatus.setStatus(_A)
_CtPriClassifyMaxEntries_Type=Unsigned32
_CtPriClassifyMaxEntries_Object=MibScalar
ctPriClassifyMaxEntries=_CtPriClassifyMaxEntries_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,2),_CtPriClassifyMaxEntries_Type())
ctPriClassifyMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:ctPriClassifyMaxEntries.setStatus(_A)
_CtPriClassifyNumEntries_Type=Unsigned32
_CtPriClassifyNumEntries_Object=MibScalar
ctPriClassifyNumEntries=_CtPriClassifyNumEntries_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,3),_CtPriClassifyNumEntries_Type())
ctPriClassifyNumEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:ctPriClassifyNumEntries.setStatus(_A)
_CtPriClassifyTable_Object=MibTable
ctPriClassifyTable=_CtPriClassifyTable_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4))
if mibBuilder.loadTexts:ctPriClassifyTable.setStatus(_A)
_CtPriClassifyEntry_Object=MibTableRow
ctPriClassifyEntry=_CtPriClassifyEntry_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1))
ctPriClassifyEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:ctPriClassifyEntry.setStatus(_A)
class _CtPriClassifyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CtPriClassifyPriority_Type.__name__=_C
_CtPriClassifyPriority_Object=MibTableColumn
ctPriClassifyPriority=_CtPriClassifyPriority_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,1),_CtPriClassifyPriority_Type())
ctPriClassifyPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriClassifyPriority.setStatus(_A)
_CtPriClassifyDataMeaning_Type=CtPriClassifyType
_CtPriClassifyDataMeaning_Object=MibTableColumn
ctPriClassifyDataMeaning=_CtPriClassifyDataMeaning_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,2),_CtPriClassifyDataMeaning_Type())
ctPriClassifyDataMeaning.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriClassifyDataMeaning.setStatus(_A)
_CtPriClassifyDataVal_Type=Unsigned32
_CtPriClassifyDataVal_Object=MibTableColumn
ctPriClassifyDataVal=_CtPriClassifyDataVal_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,3),_CtPriClassifyDataVal_Type())
ctPriClassifyDataVal.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriClassifyDataVal.setStatus(_A)
_CtPriClassifyDataMask_Type=Unsigned32
_CtPriClassifyDataMask_Object=MibTableColumn
ctPriClassifyDataMask=_CtPriClassifyDataMask_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,4),_CtPriClassifyDataMask_Type())
ctPriClassifyDataMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriClassifyDataMask.setStatus(_A)
class _CtPriClassifyIngressList_Type(PortList):defaultHexValue='0000'
_CtPriClassifyIngressList_Type.__name__=_M
_CtPriClassifyIngressList_Object=MibTableColumn
ctPriClassifyIngressList=_CtPriClassifyIngressList_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,5),_CtPriClassifyIngressList_Type())
ctPriClassifyIngressList.setMaxAccess(_N)
if mibBuilder.loadTexts:ctPriClassifyIngressList.setStatus(_A)
_CtPriClassifyRowStatus_Type=RowStatus
_CtPriClassifyRowStatus_Object=MibTableColumn
ctPriClassifyRowStatus=_CtPriClassifyRowStatus_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,6),_CtPriClassifyRowStatus_Type())
ctPriClassifyRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:ctPriClassifyRowStatus.setStatus(_A)
_CtPriClassifyRowInfo_Type=DisplayString
_CtPriClassifyRowInfo_Object=MibTableColumn
ctPriClassifyRowInfo=_CtPriClassifyRowInfo_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,7),_CtPriClassifyRowInfo_Type())
ctPriClassifyRowInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:ctPriClassifyRowInfo.setStatus(_A)
class _CtPriClassifyTOSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtPriClassifyTOSStatus_Type.__name__=_C
_CtPriClassifyTOSStatus_Object=MibTableColumn
ctPriClassifyTOSStatus=_CtPriClassifyTOSStatus_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,8),_CtPriClassifyTOSStatus_Type())
ctPriClassifyTOSStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ctPriClassifyTOSStatus.setStatus(_A)
class _CtPriClassifyTOSValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CtPriClassifyTOSValue_Type.__name__=_C
_CtPriClassifyTOSValue_Object=MibTableColumn
ctPriClassifyTOSValue=_CtPriClassifyTOSValue_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,4,1,9),_CtPriClassifyTOSValue_Type())
ctPriClassifyTOSValue.setMaxAccess(_F)
if mibBuilder.loadTexts:ctPriClassifyTOSValue.setStatus(_A)
_CtPriClassifyAbilityTable_Object=MibTable
ctPriClassifyAbilityTable=_CtPriClassifyAbilityTable_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,5))
if mibBuilder.loadTexts:ctPriClassifyAbilityTable.setStatus(_A)
_CtPriClassifyAbilityEntry_Object=MibTableRow
ctPriClassifyAbilityEntry=_CtPriClassifyAbilityEntry_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,5,1))
ctPriClassifyAbilityEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ctPriClassifyAbilityEntry.setStatus(_A)
_CtPriClassifyAbility_Type=CtPriClassifyType
_CtPriClassifyAbility_Object=MibTableColumn
ctPriClassifyAbility=_CtPriClassifyAbility_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,5,1,1),_CtPriClassifyAbility_Type())
ctPriClassifyAbility.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriClassifyAbility.setStatus(_A)
_CtPriClassifyPorts_Type=PortList
_CtPriClassifyPorts_Object=MibTableColumn
ctPriClassifyPorts=_CtPriClassifyPorts_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,5,1,2),_CtPriClassifyPorts_Type())
ctPriClassifyPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:ctPriClassifyPorts.setStatus(_A)
_CtPriClassifyTableLastChange_Type=TimeTicks
_CtPriClassifyTableLastChange_Object=MibScalar
ctPriClassifyTableLastChange=_CtPriClassifyTableLastChange_Object((1,3,6,1,4,1,52,4,1,2,14,6,1,6),_CtPriClassifyTableLastChange_Type())
ctPriClassifyTableLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:ctPriClassifyTableLastChange.setStatus(_A)
_CtPriClassifyConformance_ObjectIdentity=ObjectIdentity
ctPriClassifyConformance=_CtPriClassifyConformance_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,6,2))
_CtPriClassifyGroups_ObjectIdentity=ObjectIdentity
ctPriClassifyGroups=_CtPriClassifyGroups_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,6,2,1))
_CtPriClassifyCompliances_ObjectIdentity=ObjectIdentity
ctPriClassifyCompliances=_CtPriClassifyCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,6,2,2))
ctPriClassifyBaseGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,14,6,2,1,1))
ctPriClassifyBaseGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ctPriClassifyBaseGroup.setStatus(_A)
ctPriClassifyCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,14,6,2,2,1))
ctPriClassifyCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:ctPriClassifyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CtPriClassifyType':CtPriClassifyType,_M:PortList,'ctPriClassify':ctPriClassify,'ctPriClassifyObjects':ctPriClassifyObjects,_P:ctPriClassifyStatus,_Q:ctPriClassifyMaxEntries,_R:ctPriClassifyNumEntries,'ctPriClassifyTable':ctPriClassifyTable,'ctPriClassifyEntry':ctPriClassifyEntry,_I:ctPriClassifyPriority,_J:ctPriClassifyDataMeaning,_K:ctPriClassifyDataVal,_L:ctPriClassifyDataMask,_S:ctPriClassifyIngressList,_T:ctPriClassifyRowStatus,_U:ctPriClassifyRowInfo,_V:ctPriClassifyTOSStatus,_W:ctPriClassifyTOSValue,'ctPriClassifyAbilityTable':ctPriClassifyAbilityTable,'ctPriClassifyAbilityEntry':ctPriClassifyAbilityEntry,_O:ctPriClassifyAbility,_X:ctPriClassifyPorts,_Y:ctPriClassifyTableLastChange,'ctPriClassifyConformance':ctPriClassifyConformance,'ctPriClassifyGroups':ctPriClassifyGroups,_Z:ctPriClassifyBaseGroup,'ctPriClassifyCompliances':ctPriClassifyCompliances,'ctPriClassifyCompliance':ctPriClassifyCompliance})