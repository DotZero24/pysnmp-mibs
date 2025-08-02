_V='cienaWsServiceGroup'
_U='cwsServicePropertiesParentSvcDomainIdxReference'
_T='cwsServicePropertiesMacLearning'
_S='cwsServicePropertiesLinkStateForwarding'
_R='cwsServicePropertiesProtectionState'
_Q='cwsServicePropertiesMaxNumberOfPort'
_P='cwsServicePropertiesType'
_O='cwsServiceStateAdminState'
_N='cwsServiceIdDescription'
_M='cwsServiceIdName'
_L='cwsServiceIdServiceId'
_K='cwsServicePortMembersReferenceTableSnmpKey'
_J='cwsServiceStateTableSnmpKey'
_I='cwsServiceIdTableSnmpKey'
_H='cwsServicePropertiesTableSnmpKey'
_G='not-accessible'
_F='read-only'
_E='cwsServiceServicesServiceIndex'
_D='read-write'
_C='Integer32'
_B='CIENA-WS-SERVICE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
DescriptionString,EnabledDisabledEnum,PortId,ServiceDomainIdx,ServiceIdx=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','DescriptionString','EnabledDisabledEnum','PortId','ServiceDomainIdx','ServiceIdx')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaWsServiceMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,1))
if mibBuilder.loadTexts:cienaWsServiceMIB.setRevisions(('2017-07-18 00:00','2017-03-02 00:00','2016-12-12 00:00','2016-06-17 00:00','2015-02-25 00:00'))
class ServiceId(TextualConvention,Unsigned32):status=_A
class ServiceMaxPort(TextualConvention,Unsigned32):status=_A
class ServiceNameStr(TextualConvention,OctetString):status=_A;displayHint='64a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CienaWsServiceObjects_ObjectIdentity=ObjectIdentity
cienaWsServiceObjects=_CienaWsServiceObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,1,1))
_CienaWsServiceConformance_ObjectIdentity=ObjectIdentity
cienaWsServiceConformance=_CienaWsServiceConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,1,2))
_CienaWsServiceGroups_ObjectIdentity=ObjectIdentity
cienaWsServiceGroups=_CienaWsServiceGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,1,2,1))
_CienaWsServiceCompliances_ObjectIdentity=ObjectIdentity
cienaWsServiceCompliances=_CienaWsServiceCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,1,2,2))
_CwsServiceServicesTable_Object=MibTable
cwsServiceServicesTable=_CwsServiceServicesTable_Object((1,3,6,1,4,1,1271,3,4,1,3))
if mibBuilder.loadTexts:cwsServiceServicesTable.setStatus(_A)
_CwsServiceServicesEntry_Object=MibTableRow
cwsServiceServicesEntry=_CwsServiceServicesEntry_Object((1,3,6,1,4,1,1271,3,4,1,3,1))
cwsServiceServicesEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cwsServiceServicesEntry.setStatus(_A)
class _CwsServiceServicesServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceServicesServiceIndex_Type.__name__=_C
_CwsServiceServicesServiceIndex_Object=MibTableColumn
cwsServiceServicesServiceIndex=_CwsServiceServicesServiceIndex_Object((1,3,6,1,4,1,1271,3,4,1,3,1,1),_CwsServiceServicesServiceIndex_Type())
cwsServiceServicesServiceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsServiceServicesServiceIndex.setStatus(_A)
_CwsServiceIdTable_Object=MibTable
cwsServiceIdTable=_CwsServiceIdTable_Object((1,3,6,1,4,1,1271,3,4,1,4))
if mibBuilder.loadTexts:cwsServiceIdTable.setStatus(_A)
_CwsServiceIdEntry_Object=MibTableRow
cwsServiceIdEntry=_CwsServiceIdEntry_Object((1,3,6,1,4,1,1271,3,4,1,4,1))
cwsServiceIdEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:cwsServiceIdEntry.setStatus(_A)
class _CwsServiceIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceIdTableSnmpKey_Type.__name__=_C
_CwsServiceIdTableSnmpKey_Object=MibTableColumn
cwsServiceIdTableSnmpKey=_CwsServiceIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,1,4,1,1),_CwsServiceIdTableSnmpKey_Type())
cwsServiceIdTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsServiceIdTableSnmpKey.setStatus(_A)
_CwsServiceIdServiceId_Type=ServiceId
_CwsServiceIdServiceId_Object=MibTableColumn
cwsServiceIdServiceId=_CwsServiceIdServiceId_Object((1,3,6,1,4,1,1271,3,4,1,4,1,2),_CwsServiceIdServiceId_Type())
cwsServiceIdServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServiceIdServiceId.setStatus(_A)
_CwsServiceIdName_Type=ServiceNameStr
_CwsServiceIdName_Object=MibTableColumn
cwsServiceIdName=_CwsServiceIdName_Object((1,3,6,1,4,1,1271,3,4,1,4,1,3),_CwsServiceIdName_Type())
cwsServiceIdName.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServiceIdName.setStatus(_A)
_CwsServiceIdDescription_Type=DescriptionString
_CwsServiceIdDescription_Object=MibTableColumn
cwsServiceIdDescription=_CwsServiceIdDescription_Object((1,3,6,1,4,1,1271,3,4,1,4,1,4),_CwsServiceIdDescription_Type())
cwsServiceIdDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServiceIdDescription.setStatus(_A)
_CwsServiceStateTable_Object=MibTable
cwsServiceStateTable=_CwsServiceStateTable_Object((1,3,6,1,4,1,1271,3,4,1,5))
if mibBuilder.loadTexts:cwsServiceStateTable.setStatus(_A)
_CwsServiceStateEntry_Object=MibTableRow
cwsServiceStateEntry=_CwsServiceStateEntry_Object((1,3,6,1,4,1,1271,3,4,1,5,1))
cwsServiceStateEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:cwsServiceStateEntry.setStatus(_A)
class _CwsServiceStateTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceStateTableSnmpKey_Type.__name__=_C
_CwsServiceStateTableSnmpKey_Object=MibTableColumn
cwsServiceStateTableSnmpKey=_CwsServiceStateTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,1,5,1,1),_CwsServiceStateTableSnmpKey_Type())
cwsServiceStateTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsServiceStateTableSnmpKey.setStatus(_A)
_CwsServiceStateAdminState_Type=EnabledDisabledEnum
_CwsServiceStateAdminState_Object=MibTableColumn
cwsServiceStateAdminState=_CwsServiceStateAdminState_Object((1,3,6,1,4,1,1271,3,4,1,5,1,2),_CwsServiceStateAdminState_Type())
cwsServiceStateAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsServiceStateAdminState.setStatus(_A)
_CwsServicePropertiesTable_Object=MibTable
cwsServicePropertiesTable=_CwsServicePropertiesTable_Object((1,3,6,1,4,1,1271,3,4,1,6))
if mibBuilder.loadTexts:cwsServicePropertiesTable.setStatus(_A)
_CwsServicePropertiesEntry_Object=MibTableRow
cwsServicePropertiesEntry=_CwsServicePropertiesEntry_Object((1,3,6,1,4,1,1271,3,4,1,6,1))
cwsServicePropertiesEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cwsServicePropertiesEntry.setStatus(_A)
class _CwsServicePropertiesTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServicePropertiesTableSnmpKey_Type.__name__=_C
_CwsServicePropertiesTableSnmpKey_Object=MibTableColumn
cwsServicePropertiesTableSnmpKey=_CwsServicePropertiesTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,1,6,1,1),_CwsServicePropertiesTableSnmpKey_Type())
cwsServicePropertiesTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsServicePropertiesTableSnmpKey.setStatus(_A)
class _CwsServicePropertiesType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('epl',0),('evpl',1),('etree',2),('elan',3),('eepl',4)))
_CwsServicePropertiesType_Type.__name__=_C
_CwsServicePropertiesType_Object=MibTableColumn
cwsServicePropertiesType=_CwsServicePropertiesType_Object((1,3,6,1,4,1,1271,3,4,1,6,1,2),_CwsServicePropertiesType_Type())
cwsServicePropertiesType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServicePropertiesType.setStatus(_A)
_CwsServicePropertiesMaxNumberOfPort_Type=ServiceMaxPort
_CwsServicePropertiesMaxNumberOfPort_Object=MibTableColumn
cwsServicePropertiesMaxNumberOfPort=_CwsServicePropertiesMaxNumberOfPort_Object((1,3,6,1,4,1,1271,3,4,1,6,1,3),_CwsServicePropertiesMaxNumberOfPort_Type())
cwsServicePropertiesMaxNumberOfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsServicePropertiesMaxNumberOfPort.setStatus(_A)
class _CwsServicePropertiesProtectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('protected',0),('unprotected',1)))
_CwsServicePropertiesProtectionState_Type.__name__=_C
_CwsServicePropertiesProtectionState_Object=MibTableColumn
cwsServicePropertiesProtectionState=_CwsServicePropertiesProtectionState_Object((1,3,6,1,4,1,1271,3,4,1,6,1,4),_CwsServicePropertiesProtectionState_Type())
cwsServicePropertiesProtectionState.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServicePropertiesProtectionState.setStatus(_A)
_CwsServicePropertiesLinkStateForwarding_Type=EnabledDisabledEnum
_CwsServicePropertiesLinkStateForwarding_Object=MibTableColumn
cwsServicePropertiesLinkStateForwarding=_CwsServicePropertiesLinkStateForwarding_Object((1,3,6,1,4,1,1271,3,4,1,6,1,5),_CwsServicePropertiesLinkStateForwarding_Type())
cwsServicePropertiesLinkStateForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServicePropertiesLinkStateForwarding.setStatus(_A)
_CwsServicePropertiesMacLearning_Type=EnabledDisabledEnum
_CwsServicePropertiesMacLearning_Object=MibTableColumn
cwsServicePropertiesMacLearning=_CwsServicePropertiesMacLearning_Object((1,3,6,1,4,1,1271,3,4,1,6,1,6),_CwsServicePropertiesMacLearning_Type())
cwsServicePropertiesMacLearning.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServicePropertiesMacLearning.setStatus(_A)
_CwsServicePropertiesParentSvcDomainIdxReference_Type=ServiceDomainIdx
_CwsServicePropertiesParentSvcDomainIdxReference_Object=MibTableColumn
cwsServicePropertiesParentSvcDomainIdxReference=_CwsServicePropertiesParentSvcDomainIdxReference_Object((1,3,6,1,4,1,1271,3,4,1,6,1,7),_CwsServicePropertiesParentSvcDomainIdxReference_Type())
cwsServicePropertiesParentSvcDomainIdxReference.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsServicePropertiesParentSvcDomainIdxReference.setStatus(_A)
_CwsServicePortMembersReferenceTable_Object=MibTable
cwsServicePortMembersReferenceTable=_CwsServicePortMembersReferenceTable_Object((1,3,6,1,4,1,1271,3,4,1,7))
if mibBuilder.loadTexts:cwsServicePortMembersReferenceTable.setStatus(_A)
_CwsServicePortMembersReferenceEntry_Object=MibTableRow
cwsServicePortMembersReferenceEntry=_CwsServicePortMembersReferenceEntry_Object((1,3,6,1,4,1,1271,3,4,1,7,1))
cwsServicePortMembersReferenceEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:cwsServicePortMembersReferenceEntry.setStatus(_A)
class _CwsServicePortMembersReferenceTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServicePortMembersReferenceTableSnmpKey_Type.__name__=_C
_CwsServicePortMembersReferenceTableSnmpKey_Object=MibTableColumn
cwsServicePortMembersReferenceTableSnmpKey=_CwsServicePortMembersReferenceTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,1,7,1,1),_CwsServicePortMembersReferenceTableSnmpKey_Type())
cwsServicePortMembersReferenceTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsServicePortMembersReferenceTableSnmpKey.setStatus(_A)
_CwsServicePortMembersReference_Type=PortId
_CwsServicePortMembersReference_Object=MibTableColumn
cwsServicePortMembersReference=_CwsServicePortMembersReference_Object((1,3,6,1,4,1,1271,3,4,1,7,1,2),_CwsServicePortMembersReference_Type())
cwsServicePortMembersReference.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsServicePortMembersReference.setStatus(_A)
cienaWsServiceGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,1,2,1,1))
cienaWsServiceGroup.setObjects(*((_B,_E),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cienaWsServiceGroup.setStatus(_A)
cienaWsServiceCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,1,2,2,1))
cienaWsServiceCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:cienaWsServiceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ServiceId':ServiceId,'ServiceMaxPort':ServiceMaxPort,'ServiceNameStr':ServiceNameStr,'cienaWsServiceMIB':cienaWsServiceMIB,'cienaWsServiceObjects':cienaWsServiceObjects,'cienaWsServiceConformance':cienaWsServiceConformance,'cienaWsServiceGroups':cienaWsServiceGroups,_V:cienaWsServiceGroup,'cienaWsServiceCompliances':cienaWsServiceCompliances,'cienaWsServiceCompliance':cienaWsServiceCompliance,'cwsServiceServicesTable':cwsServiceServicesTable,'cwsServiceServicesEntry':cwsServiceServicesEntry,_E:cwsServiceServicesServiceIndex,'cwsServiceIdTable':cwsServiceIdTable,'cwsServiceIdEntry':cwsServiceIdEntry,_I:cwsServiceIdTableSnmpKey,_L:cwsServiceIdServiceId,_M:cwsServiceIdName,_N:cwsServiceIdDescription,'cwsServiceStateTable':cwsServiceStateTable,'cwsServiceStateEntry':cwsServiceStateEntry,_J:cwsServiceStateTableSnmpKey,_O:cwsServiceStateAdminState,'cwsServicePropertiesTable':cwsServicePropertiesTable,'cwsServicePropertiesEntry':cwsServicePropertiesEntry,_H:cwsServicePropertiesTableSnmpKey,_P:cwsServicePropertiesType,_Q:cwsServicePropertiesMaxNumberOfPort,_R:cwsServicePropertiesProtectionState,_S:cwsServicePropertiesLinkStateForwarding,_T:cwsServicePropertiesMacLearning,_U:cwsServicePropertiesParentSvcDomainIdxReference,'cwsServicePortMembersReferenceTable':cwsServicePortMembersReferenceTable,'cwsServicePortMembersReferenceEntry':cwsServicePortMembersReferenceEntry,_K:cwsServicePortMembersReferenceTableSnmpKey,'cwsServicePortMembersReference':cwsServicePortMembersReference})