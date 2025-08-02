_K='rulesIndex'
_J='listIndex'
_I='activeFilterPortConfigPortIndex'
_H='enabled'
_G='disabled'
_F='not-accessible'
_E='G6-ACL-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Acl_ObjectIdentity=ObjectIdentity
acl=_Acl_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,51))
class _AclEnableAclFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AclEnableAclFiltering_Type.__name__=_C
_AclEnableAclFiltering_Object=MibScalar
aclEnableAclFiltering=_AclEnableAclFiltering_Object((1,3,6,1,4,1,3181,10,6,3,51,1),_AclEnableAclFiltering_Type())
aclEnableAclFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:aclEnableAclFiltering.setStatus(_A)
_ActiveFilterPortConfigTable_Object=MibTable
activeFilterPortConfigTable=_ActiveFilterPortConfigTable_Object((1,3,6,1,4,1,3181,10,6,3,51,2))
if mibBuilder.loadTexts:activeFilterPortConfigTable.setStatus(_A)
_ActiveFilterPortConfigEntry_Object=MibTableRow
activeFilterPortConfigEntry=_ActiveFilterPortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,3,51,2,1))
activeFilterPortConfigEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:activeFilterPortConfigEntry.setStatus(_A)
class _ActiveFilterPortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ActiveFilterPortConfigPortIndex_Type.__name__=_C
_ActiveFilterPortConfigPortIndex_Object=MibTableColumn
activeFilterPortConfigPortIndex=_ActiveFilterPortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,3,51,2,1,1),_ActiveFilterPortConfigPortIndex_Type())
activeFilterPortConfigPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:activeFilterPortConfigPortIndex.setStatus(_A)
class _ActiveFilterPortConfigEnableAclFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ActiveFilterPortConfigEnableAclFiltering_Type.__name__=_C
_ActiveFilterPortConfigEnableAclFiltering_Object=MibTableColumn
activeFilterPortConfigEnableAclFiltering=_ActiveFilterPortConfigEnableAclFiltering_Object((1,3,6,1,4,1,3181,10,6,3,51,2,1,2),_ActiveFilterPortConfigEnableAclFiltering_Type())
activeFilterPortConfigEnableAclFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:activeFilterPortConfigEnableAclFiltering.setStatus(_A)
_ActiveFilterPortConfigAclListName_Type=DisplayString
_ActiveFilterPortConfigAclListName_Object=MibTableColumn
activeFilterPortConfigAclListName=_ActiveFilterPortConfigAclListName_Object((1,3,6,1,4,1,3181,10,6,3,51,2,1,3),_ActiveFilterPortConfigAclListName_Type())
activeFilterPortConfigAclListName.setMaxAccess(_B)
if mibBuilder.loadTexts:activeFilterPortConfigAclListName.setStatus(_A)
_ListTable_Object=MibTable
listTable=_ListTable_Object((1,3,6,1,4,1,3181,10,6,3,51,3))
if mibBuilder.loadTexts:listTable.setStatus(_A)
_ListEntry_Object=MibTableRow
listEntry=_ListEntry_Object((1,3,6,1,4,1,3181,10,6,3,51,3,1))
listEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:listEntry.setStatus(_A)
class _ListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ListIndex_Type.__name__=_C
_ListIndex_Object=MibTableColumn
listIndex=_ListIndex_Object((1,3,6,1,4,1,3181,10,6,3,51,3,1,1),_ListIndex_Type())
listIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:listIndex.setStatus(_A)
_ListName_Type=DisplayString
_ListName_Object=MibTableColumn
listName=_ListName_Object((1,3,6,1,4,1,3181,10,6,3,51,3,1,2),_ListName_Type())
listName.setMaxAccess(_B)
if mibBuilder.loadTexts:listName.setStatus(_A)
_ListDescription_Type=DisplayString
_ListDescription_Object=MibTableColumn
listDescription=_ListDescription_Object((1,3,6,1,4,1,3181,10,6,3,51,3,1,3),_ListDescription_Type())
listDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:listDescription.setStatus(_A)
_ListRules_Type=DisplayString
_ListRules_Object=MibTableColumn
listRules=_ListRules_Object((1,3,6,1,4,1,3181,10,6,3,51,3,1,4),_ListRules_Type())
listRules.setMaxAccess(_B)
if mibBuilder.loadTexts:listRules.setStatus(_A)
_RulesTable_Object=MibTable
rulesTable=_RulesTable_Object((1,3,6,1,4,1,3181,10,6,3,51,4))
if mibBuilder.loadTexts:rulesTable.setStatus(_A)
_RulesEntry_Object=MibTableRow
rulesEntry=_RulesEntry_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1))
rulesEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:rulesEntry.setStatus(_A)
class _RulesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_RulesIndex_Type.__name__=_C
_RulesIndex_Object=MibTableColumn
rulesIndex=_RulesIndex_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,1),_RulesIndex_Type())
rulesIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rulesIndex.setStatus(_A)
_RulesName_Type=DisplayString
_RulesName_Object=MibTableColumn
rulesName=_RulesName_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,2),_RulesName_Type())
rulesName.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesName.setStatus(_A)
_RulesDescription_Type=DisplayString
_RulesDescription_Object=MibTableColumn
rulesDescription=_RulesDescription_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,3),_RulesDescription_Type())
rulesDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesDescription.setStatus(_A)
class _RulesMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unused',0),('permit',1),('deny',2)))
_RulesMode_Type.__name__=_C
_RulesMode_Object=MibTableColumn
rulesMode=_RulesMode_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,4),_RulesMode_Type())
rulesMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesMode.setStatus(_A)
class _RulesEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RulesEtherType_Type.__name__=_C
_RulesEtherType_Object=MibTableColumn
rulesEtherType=_RulesEtherType_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,5),_RulesEtherType_Type())
rulesEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesEtherType.setStatus(_A)
class _RulesProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RulesProtocol_Type.__name__=_C
_RulesProtocol_Object=MibTableColumn
rulesProtocol=_RulesProtocol_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,6),_RulesProtocol_Type())
rulesProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesProtocol.setStatus(_A)
class _RulesVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RulesVlanId_Type.__name__=_C
_RulesVlanId_Object=MibTableColumn
rulesVlanId=_RulesVlanId_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,7),_RulesVlanId_Type())
rulesVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesVlanId.setStatus(_A)
_RulesSourceMac_Type=MacAddress
_RulesSourceMac_Object=MibTableColumn
rulesSourceMac=_RulesSourceMac_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,8),_RulesSourceMac_Type())
rulesSourceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesSourceMac.setStatus(_A)
class _RulesSourceIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RulesSourceIp_Type.__name__=_D
_RulesSourceIp_Object=MibTableColumn
rulesSourceIp=_RulesSourceIp_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,9),_RulesSourceIp_Type())
rulesSourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesSourceIp.setStatus(_A)
class _RulesSourceMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RulesSourceMask_Type.__name__=_D
_RulesSourceMask_Object=MibTableColumn
rulesSourceMask=_RulesSourceMask_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,10),_RulesSourceMask_Type())
rulesSourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesSourceMask.setStatus(_A)
class _RulesSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RulesSourcePort_Type.__name__=_C
_RulesSourcePort_Object=MibTableColumn
rulesSourcePort=_RulesSourcePort_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,11),_RulesSourcePort_Type())
rulesSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesSourcePort.setStatus(_A)
_RulesDestinationMac_Type=MacAddress
_RulesDestinationMac_Object=MibTableColumn
rulesDestinationMac=_RulesDestinationMac_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,12),_RulesDestinationMac_Type())
rulesDestinationMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesDestinationMac.setStatus(_A)
class _RulesDestinationIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RulesDestinationIp_Type.__name__=_D
_RulesDestinationIp_Object=MibTableColumn
rulesDestinationIp=_RulesDestinationIp_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,13),_RulesDestinationIp_Type())
rulesDestinationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesDestinationIp.setStatus(_A)
class _RulesDestinationMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RulesDestinationMask_Type.__name__=_D
_RulesDestinationMask_Object=MibTableColumn
rulesDestinationMask=_RulesDestinationMask_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,14),_RulesDestinationMask_Type())
rulesDestinationMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesDestinationMask.setStatus(_A)
class _RulesDestinationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RulesDestinationPort_Type.__name__=_C
_RulesDestinationPort_Object=MibTableColumn
rulesDestinationPort=_RulesDestinationPort_Object((1,3,6,1,4,1,3181,10,6,3,51,4,1,15),_RulesDestinationPort_Type())
rulesDestinationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rulesDestinationPort.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'management':management,'acl':acl,'aclEnableAclFiltering':aclEnableAclFiltering,'activeFilterPortConfigTable':activeFilterPortConfigTable,'activeFilterPortConfigEntry':activeFilterPortConfigEntry,_I:activeFilterPortConfigPortIndex,'activeFilterPortConfigEnableAclFiltering':activeFilterPortConfigEnableAclFiltering,'activeFilterPortConfigAclListName':activeFilterPortConfigAclListName,'listTable':listTable,'listEntry':listEntry,_J:listIndex,'listName':listName,'listDescription':listDescription,'listRules':listRules,'rulesTable':rulesTable,'rulesEntry':rulesEntry,_K:rulesIndex,'rulesName':rulesName,'rulesDescription':rulesDescription,'rulesMode':rulesMode,'rulesEtherType':rulesEtherType,'rulesProtocol':rulesProtocol,'rulesVlanId':rulesVlanId,'rulesSourceMac':rulesSourceMac,'rulesSourceIp':rulesSourceIp,'rulesSourceMask':rulesSourceMask,'rulesSourcePort':rulesSourcePort,'rulesDestinationMac':rulesDestinationMac,'rulesDestinationIp':rulesDestinationIp,'rulesDestinationMask':rulesDestinationMask,'rulesDestinationPort':rulesDestinationPort})