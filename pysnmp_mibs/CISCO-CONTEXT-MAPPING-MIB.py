_Y='cContextMappingLicenseGroupDataGroup'
_X='cContextMappingLicenseGroupRowStatus'
_W='cContextMappingLicenseGroupName'
_V='cContextMappingBridgeInstRowStatus'
_U='cContextMappingBridgeInstStorageType'
_T='cContextMappingBridgeInstName'
_S='cContextMappingBridgeDomainRowStatus'
_R='cContextMappingBridgeDomainStorageType'
_Q='cContextMappingBridgeDomainIdentifier'
_P='cContextMappingRowStatus'
_O='cContextMappingStorageType'
_N='cContextMappingProtoInstName'
_M='cContextMappingTopologyName'
_L='cContextMappingVrfName'
_K='cContextMappingBridgeInstanceDataGroup'
_J='deprecated'
_I='cContextMappingLicenseGroupStorageType'
_H='cContextMappingBridgeDomainDataGroup'
_G='cContextMappingDataGroup'
_F='cContextMappingVacmContextName'
_E='StorageType'
_D='SnmpAdminString'
_C='read-create'
_B='current'
_A='CISCO-CONTEXT-MAPPING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoBridgeDomain,=mibBuilder.importSymbols('CISCO-TC','CiscoBridgeDomain')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_E,'TextualConvention')
ciscoContextMappingMIB=ModuleIdentity((1,3,6,1,4,1,9,9,468))
if mibBuilder.loadTexts:ciscoContextMappingMIB.setRevisions(('2008-11-22 00:00','2008-05-30 00:00','2008-02-01 00:00','2005-03-17 00:00'))
_CContextMappingMIBObjects_ObjectIdentity=ObjectIdentity
cContextMappingMIBObjects=_CContextMappingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,468,1))
_CContextMappingTable_Object=MibTable
cContextMappingTable=_CContextMappingTable_Object((1,3,6,1,4,1,9,9,468,1,1))
if mibBuilder.loadTexts:cContextMappingTable.setStatus(_B)
_CContextMappingEntry_Object=MibTableRow
cContextMappingEntry=_CContextMappingEntry_Object((1,3,6,1,4,1,9,9,468,1,1,1))
cContextMappingEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cContextMappingEntry.setStatus(_B)
class _CContextMappingVacmContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CContextMappingVacmContextName_Type.__name__=_D
_CContextMappingVacmContextName_Object=MibTableColumn
cContextMappingVacmContextName=_CContextMappingVacmContextName_Object((1,3,6,1,4,1,9,9,468,1,1,1,1),_CContextMappingVacmContextName_Type())
cContextMappingVacmContextName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cContextMappingVacmContextName.setStatus(_B)
class _CContextMappingVrfName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CContextMappingVrfName_Type.__name__=_D
_CContextMappingVrfName_Object=MibTableColumn
cContextMappingVrfName=_CContextMappingVrfName_Object((1,3,6,1,4,1,9,9,468,1,1,1,2),_CContextMappingVrfName_Type())
cContextMappingVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingVrfName.setStatus(_B)
class _CContextMappingTopologyName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CContextMappingTopologyName_Type.__name__=_D
_CContextMappingTopologyName_Object=MibTableColumn
cContextMappingTopologyName=_CContextMappingTopologyName_Object((1,3,6,1,4,1,9,9,468,1,1,1,3),_CContextMappingTopologyName_Type())
cContextMappingTopologyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingTopologyName.setStatus(_B)
class _CContextMappingProtoInstName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CContextMappingProtoInstName_Type.__name__=_D
_CContextMappingProtoInstName_Object=MibTableColumn
cContextMappingProtoInstName=_CContextMappingProtoInstName_Object((1,3,6,1,4,1,9,9,468,1,1,1,4),_CContextMappingProtoInstName_Type())
cContextMappingProtoInstName.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingProtoInstName.setStatus(_B)
class _CContextMappingStorageType_Type(StorageType):defaultValue=3
_CContextMappingStorageType_Type.__name__=_E
_CContextMappingStorageType_Object=MibTableColumn
cContextMappingStorageType=_CContextMappingStorageType_Object((1,3,6,1,4,1,9,9,468,1,1,1,5),_CContextMappingStorageType_Type())
cContextMappingStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingStorageType.setStatus(_B)
_CContextMappingRowStatus_Type=RowStatus
_CContextMappingRowStatus_Object=MibTableColumn
cContextMappingRowStatus=_CContextMappingRowStatus_Object((1,3,6,1,4,1,9,9,468,1,1,1,6),_CContextMappingRowStatus_Type())
cContextMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingRowStatus.setStatus(_B)
_CContextMappingBridgeDomainTable_Object=MibTable
cContextMappingBridgeDomainTable=_CContextMappingBridgeDomainTable_Object((1,3,6,1,4,1,9,9,468,1,2))
if mibBuilder.loadTexts:cContextMappingBridgeDomainTable.setStatus(_B)
_CContextMappingBridgeDomainEntry_Object=MibTableRow
cContextMappingBridgeDomainEntry=_CContextMappingBridgeDomainEntry_Object((1,3,6,1,4,1,9,9,468,1,2,1))
cContextMappingBridgeDomainEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cContextMappingBridgeDomainEntry.setStatus(_B)
_CContextMappingBridgeDomainIdentifier_Type=CiscoBridgeDomain
_CContextMappingBridgeDomainIdentifier_Object=MibTableColumn
cContextMappingBridgeDomainIdentifier=_CContextMappingBridgeDomainIdentifier_Object((1,3,6,1,4,1,9,9,468,1,2,1,1),_CContextMappingBridgeDomainIdentifier_Type())
cContextMappingBridgeDomainIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingBridgeDomainIdentifier.setStatus(_B)
class _CContextMappingBridgeDomainStorageType_Type(StorageType):defaultValue=3
_CContextMappingBridgeDomainStorageType_Type.__name__=_E
_CContextMappingBridgeDomainStorageType_Object=MibTableColumn
cContextMappingBridgeDomainStorageType=_CContextMappingBridgeDomainStorageType_Object((1,3,6,1,4,1,9,9,468,1,2,1,2),_CContextMappingBridgeDomainStorageType_Type())
cContextMappingBridgeDomainStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingBridgeDomainStorageType.setStatus(_B)
_CContextMappingBridgeDomainRowStatus_Type=RowStatus
_CContextMappingBridgeDomainRowStatus_Object=MibTableColumn
cContextMappingBridgeDomainRowStatus=_CContextMappingBridgeDomainRowStatus_Object((1,3,6,1,4,1,9,9,468,1,2,1,3),_CContextMappingBridgeDomainRowStatus_Type())
cContextMappingBridgeDomainRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingBridgeDomainRowStatus.setStatus(_B)
_CContextMappingBridgeInstanceTable_Object=MibTable
cContextMappingBridgeInstanceTable=_CContextMappingBridgeInstanceTable_Object((1,3,6,1,4,1,9,9,468,1,3))
if mibBuilder.loadTexts:cContextMappingBridgeInstanceTable.setStatus(_B)
_CContextMappingBridgeInstanceEntry_Object=MibTableRow
cContextMappingBridgeInstanceEntry=_CContextMappingBridgeInstanceEntry_Object((1,3,6,1,4,1,9,9,468,1,3,1))
cContextMappingBridgeInstanceEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cContextMappingBridgeInstanceEntry.setStatus(_B)
_CContextMappingBridgeInstName_Type=SnmpAdminString
_CContextMappingBridgeInstName_Object=MibTableColumn
cContextMappingBridgeInstName=_CContextMappingBridgeInstName_Object((1,3,6,1,4,1,9,9,468,1,3,1,1),_CContextMappingBridgeInstName_Type())
cContextMappingBridgeInstName.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingBridgeInstName.setStatus(_B)
class _CContextMappingBridgeInstStorageType_Type(StorageType):defaultValue=3
_CContextMappingBridgeInstStorageType_Type.__name__=_E
_CContextMappingBridgeInstStorageType_Object=MibTableColumn
cContextMappingBridgeInstStorageType=_CContextMappingBridgeInstStorageType_Object((1,3,6,1,4,1,9,9,468,1,3,1,2),_CContextMappingBridgeInstStorageType_Type())
cContextMappingBridgeInstStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingBridgeInstStorageType.setStatus(_B)
_CContextMappingBridgeInstRowStatus_Type=RowStatus
_CContextMappingBridgeInstRowStatus_Object=MibTableColumn
cContextMappingBridgeInstRowStatus=_CContextMappingBridgeInstRowStatus_Object((1,3,6,1,4,1,9,9,468,1,3,1,3),_CContextMappingBridgeInstRowStatus_Type())
cContextMappingBridgeInstRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingBridgeInstRowStatus.setStatus(_B)
_CContextMappingLicenseGroupTable_Object=MibTable
cContextMappingLicenseGroupTable=_CContextMappingLicenseGroupTable_Object((1,3,6,1,4,1,9,9,468,1,4))
if mibBuilder.loadTexts:cContextMappingLicenseGroupTable.setStatus(_B)
_CContextMappingLicenseGroupEntry_Object=MibTableRow
cContextMappingLicenseGroupEntry=_CContextMappingLicenseGroupEntry_Object((1,3,6,1,4,1,9,9,468,1,4,1))
cContextMappingLicenseGroupEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cContextMappingLicenseGroupEntry.setStatus(_B)
class _CContextMappingLicenseGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CContextMappingLicenseGroupName_Type.__name__=_D
_CContextMappingLicenseGroupName_Object=MibTableColumn
cContextMappingLicenseGroupName=_CContextMappingLicenseGroupName_Object((1,3,6,1,4,1,9,9,468,1,4,1,1),_CContextMappingLicenseGroupName_Type())
cContextMappingLicenseGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingLicenseGroupName.setStatus(_B)
class _CContextMappingLicenseGroupStorageType_Type(StorageType):defaultValue=3
_CContextMappingLicenseGroupStorageType_Type.__name__=_E
_CContextMappingLicenseGroupStorageType_Object=MibTableColumn
cContextMappingLicenseGroupStorageType=_CContextMappingLicenseGroupStorageType_Object((1,3,6,1,4,1,9,9,468,1,4,1,2),_CContextMappingLicenseGroupStorageType_Type())
cContextMappingLicenseGroupStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingLicenseGroupStorageType.setStatus(_B)
_CContextMappingLicenseGroupRowStatus_Type=RowStatus
_CContextMappingLicenseGroupRowStatus_Object=MibTableColumn
cContextMappingLicenseGroupRowStatus=_CContextMappingLicenseGroupRowStatus_Object((1,3,6,1,4,1,9,9,468,1,4,1,3),_CContextMappingLicenseGroupRowStatus_Type())
cContextMappingLicenseGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cContextMappingLicenseGroupRowStatus.setStatus(_B)
_CContextMappingMIBConformance_ObjectIdentity=ObjectIdentity
cContextMappingMIBConformance=_CContextMappingMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,468,2))
_CContextMappingMIBCompliances_ObjectIdentity=ObjectIdentity
cContextMappingMIBCompliances=_CContextMappingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,468,2,1))
_CContextMappingMIBGroups_ObjectIdentity=ObjectIdentity
cContextMappingMIBGroups=_CContextMappingMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,468,2,2))
cContextMappingDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,468,2,2,1))
cContextMappingDataGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cContextMappingDataGroup.setStatus(_B)
cContextMappingBridgeDomainDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,468,2,2,2))
cContextMappingBridgeDomainDataGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cContextMappingBridgeDomainDataGroup.setStatus(_B)
cContextMappingBridgeInstanceDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,468,2,2,3))
cContextMappingBridgeInstanceDataGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:cContextMappingBridgeInstanceDataGroup.setStatus(_B)
cContextMappingLicenseGroupDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,468,2,2,4))
cContextMappingLicenseGroupDataGroup.setObjects(*((_A,_W),(_A,_I),(_A,_I),(_A,_X)))
if mibBuilder.loadTexts:cContextMappingLicenseGroupDataGroup.setStatus(_B)
cContextMappingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,468,2,1,1))
cContextMappingMIBCompliance.setObjects((_A,_G))
if mibBuilder.loadTexts:cContextMappingMIBCompliance.setStatus(_J)
cContextMappingMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,468,2,1,2))
cContextMappingMIBComplianceRev1.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cContextMappingMIBComplianceRev1.setStatus(_J)
cContextMappingMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,468,2,1,3))
cContextMappingMIBComplianceRev2.setObjects(*((_A,_G),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:cContextMappingMIBComplianceRev2.setStatus(_J)
cContextMappingMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,468,2,1,4))
cContextMappingMIBComplianceRev3.setObjects(*((_A,_G),(_A,_H),(_A,_K),(_A,_Y)))
if mibBuilder.loadTexts:cContextMappingMIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoContextMappingMIB':ciscoContextMappingMIB,'cContextMappingMIBObjects':cContextMappingMIBObjects,'cContextMappingTable':cContextMappingTable,'cContextMappingEntry':cContextMappingEntry,_F:cContextMappingVacmContextName,_L:cContextMappingVrfName,_M:cContextMappingTopologyName,_N:cContextMappingProtoInstName,_O:cContextMappingStorageType,_P:cContextMappingRowStatus,'cContextMappingBridgeDomainTable':cContextMappingBridgeDomainTable,'cContextMappingBridgeDomainEntry':cContextMappingBridgeDomainEntry,_Q:cContextMappingBridgeDomainIdentifier,_R:cContextMappingBridgeDomainStorageType,_S:cContextMappingBridgeDomainRowStatus,'cContextMappingBridgeInstanceTable':cContextMappingBridgeInstanceTable,'cContextMappingBridgeInstanceEntry':cContextMappingBridgeInstanceEntry,_T:cContextMappingBridgeInstName,_U:cContextMappingBridgeInstStorageType,_V:cContextMappingBridgeInstRowStatus,'cContextMappingLicenseGroupTable':cContextMappingLicenseGroupTable,'cContextMappingLicenseGroupEntry':cContextMappingLicenseGroupEntry,_W:cContextMappingLicenseGroupName,_I:cContextMappingLicenseGroupStorageType,_X:cContextMappingLicenseGroupRowStatus,'cContextMappingMIBConformance':cContextMappingMIBConformance,'cContextMappingMIBCompliances':cContextMappingMIBCompliances,'cContextMappingMIBCompliance':cContextMappingMIBCompliance,'cContextMappingMIBComplianceRev1':cContextMappingMIBComplianceRev1,'cContextMappingMIBComplianceRev2':cContextMappingMIBComplianceRev2,'cContextMappingMIBComplianceRev3':cContextMappingMIBComplianceRev3,'cContextMappingMIBGroups':cContextMappingMIBGroups,_G:cContextMappingDataGroup,_H:cContextMappingBridgeDomainDataGroup,_K:cContextMappingBridgeInstanceDataGroup,_Y:cContextMappingLicenseGroupDataGroup})