_Z='ceAssetGroupRev2'
_Y='ceAssetEntityGroup'
_X='ceAssetGroupRev1'
_W='ceAssetGroup'
_V='read-write'
_U='entPhysicalIndex'
_T='ENTITY-MIB'
_S='ceAssetIsFRU'
_R='ceAssetTag'
_Q='ceAssetAlias'
_P='ceAssetSoftwareRevision'
_O='ceAssetSoftwareID'
_N='ceAssetFirmwareRevision'
_M='ceAssetFirmwareID'
_L='ceAssetHardwareRevision'
_K='ceAssetOrderablePartNumber'
_J='ceAssetSerialNumber'
_I='ceAssetOEMString'
_H='ceAssetCLEI'
_G='ceAssetMfgAssyRevision'
_F='ceAssetMfgAssyNumber'
_E='SnmpAdminString'
_D='current'
_C='read-only'
_B='deprecated'
_A='CISCO-ENTITY-ASSET-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_T,_U)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoEntityAssetMIB=ModuleIdentity((1,3,6,1,4,1,9,9,92))
if mibBuilder.loadTexts:ciscoEntityAssetMIB.setRevisions(('2003-09-18 00:00','2002-07-23 16:00','1999-06-02 16:00'))
_CiscoEntityAssetMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityAssetMIBObjects=_CiscoEntityAssetMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,92,1))
_CeAssetTable_Object=MibTable
ceAssetTable=_CeAssetTable_Object((1,3,6,1,4,1,9,9,92,1,1))
if mibBuilder.loadTexts:ceAssetTable.setStatus(_D)
_CeAssetEntry_Object=MibTableRow
ceAssetEntry=_CeAssetEntry_Object((1,3,6,1,4,1,9,9,92,1,1,1))
ceAssetEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:ceAssetEntry.setStatus(_D)
_CeAssetOEMString_Type=SnmpAdminString
_CeAssetOEMString_Object=MibTableColumn
ceAssetOEMString=_CeAssetOEMString_Object((1,3,6,1,4,1,9,9,92,1,1,1,1),_CeAssetOEMString_Type())
ceAssetOEMString.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetOEMString.setStatus(_B)
_CeAssetSerialNumber_Type=SnmpAdminString
_CeAssetSerialNumber_Object=MibTableColumn
ceAssetSerialNumber=_CeAssetSerialNumber_Object((1,3,6,1,4,1,9,9,92,1,1,1,2),_CeAssetSerialNumber_Type())
ceAssetSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetSerialNumber.setStatus(_B)
_CeAssetOrderablePartNumber_Type=SnmpAdminString
_CeAssetOrderablePartNumber_Object=MibTableColumn
ceAssetOrderablePartNumber=_CeAssetOrderablePartNumber_Object((1,3,6,1,4,1,9,9,92,1,1,1,3),_CeAssetOrderablePartNumber_Type())
ceAssetOrderablePartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetOrderablePartNumber.setStatus(_B)
_CeAssetHardwareRevision_Type=SnmpAdminString
_CeAssetHardwareRevision_Object=MibTableColumn
ceAssetHardwareRevision=_CeAssetHardwareRevision_Object((1,3,6,1,4,1,9,9,92,1,1,1,4),_CeAssetHardwareRevision_Type())
ceAssetHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetHardwareRevision.setStatus(_B)
_CeAssetMfgAssyNumber_Type=SnmpAdminString
_CeAssetMfgAssyNumber_Object=MibTableColumn
ceAssetMfgAssyNumber=_CeAssetMfgAssyNumber_Object((1,3,6,1,4,1,9,9,92,1,1,1,5),_CeAssetMfgAssyNumber_Type())
ceAssetMfgAssyNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetMfgAssyNumber.setStatus(_D)
_CeAssetMfgAssyRevision_Type=SnmpAdminString
_CeAssetMfgAssyRevision_Object=MibTableColumn
ceAssetMfgAssyRevision=_CeAssetMfgAssyRevision_Object((1,3,6,1,4,1,9,9,92,1,1,1,6),_CeAssetMfgAssyRevision_Type())
ceAssetMfgAssyRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetMfgAssyRevision.setStatus(_D)
_CeAssetFirmwareID_Type=SnmpAdminString
_CeAssetFirmwareID_Object=MibTableColumn
ceAssetFirmwareID=_CeAssetFirmwareID_Object((1,3,6,1,4,1,9,9,92,1,1,1,7),_CeAssetFirmwareID_Type())
ceAssetFirmwareID.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetFirmwareID.setStatus(_B)
_CeAssetFirmwareRevision_Type=SnmpAdminString
_CeAssetFirmwareRevision_Object=MibTableColumn
ceAssetFirmwareRevision=_CeAssetFirmwareRevision_Object((1,3,6,1,4,1,9,9,92,1,1,1,8),_CeAssetFirmwareRevision_Type())
ceAssetFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetFirmwareRevision.setStatus(_B)
_CeAssetSoftwareID_Type=SnmpAdminString
_CeAssetSoftwareID_Object=MibTableColumn
ceAssetSoftwareID=_CeAssetSoftwareID_Object((1,3,6,1,4,1,9,9,92,1,1,1,9),_CeAssetSoftwareID_Type())
ceAssetSoftwareID.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetSoftwareID.setStatus(_B)
_CeAssetSoftwareRevision_Type=SnmpAdminString
_CeAssetSoftwareRevision_Object=MibTableColumn
ceAssetSoftwareRevision=_CeAssetSoftwareRevision_Object((1,3,6,1,4,1,9,9,92,1,1,1,10),_CeAssetSoftwareRevision_Type())
ceAssetSoftwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetSoftwareRevision.setStatus(_B)
class _CeAssetCLEI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(10,10))
_CeAssetCLEI_Type.__name__=_E
_CeAssetCLEI_Object=MibTableColumn
ceAssetCLEI=_CeAssetCLEI_Object((1,3,6,1,4,1,9,9,92,1,1,1,11),_CeAssetCLEI_Type())
ceAssetCLEI.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetCLEI.setStatus(_D)
class _CeAssetAlias_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CeAssetAlias_Type.__name__=_E
_CeAssetAlias_Object=MibTableColumn
ceAssetAlias=_CeAssetAlias_Object((1,3,6,1,4,1,9,9,92,1,1,1,12),_CeAssetAlias_Type())
ceAssetAlias.setMaxAccess(_V)
if mibBuilder.loadTexts:ceAssetAlias.setStatus(_B)
class _CeAssetTag_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CeAssetTag_Type.__name__=_E
_CeAssetTag_Object=MibTableColumn
ceAssetTag=_CeAssetTag_Object((1,3,6,1,4,1,9,9,92,1,1,1,13),_CeAssetTag_Type())
ceAssetTag.setMaxAccess(_V)
if mibBuilder.loadTexts:ceAssetTag.setStatus(_B)
_CeAssetIsFRU_Type=TruthValue
_CeAssetIsFRU_Object=MibTableColumn
ceAssetIsFRU=_CeAssetIsFRU_Object((1,3,6,1,4,1,9,9,92,1,1,1,14),_CeAssetIsFRU_Type())
ceAssetIsFRU.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAssetIsFRU.setStatus(_B)
_CiscoEntityAssetMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoEntityAssetMIBNotificationsPrefix=_CiscoEntityAssetMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,92,2))
_CiscoEntityAssetMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoEntityAssetMIBNotifications=_CiscoEntityAssetMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,92,2,0))
_CiscoEntityAssetMIBConformance_ObjectIdentity=ObjectIdentity
ciscoEntityAssetMIBConformance=_CiscoEntityAssetMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,92,3))
_CiscoEntityAssetMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEntityAssetMIBCompliances=_CiscoEntityAssetMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,92,3,1))
_CiscoEntityAssetMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEntityAssetMIBGroups=_CiscoEntityAssetMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,92,3,2))
ceAssetGroup=ObjectGroup((1,3,6,1,4,1,9,9,92,3,2,1))
ceAssetGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_H),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ceAssetGroup.setStatus(_B)
ceAssetGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,92,3,2,2))
ceAssetGroupRev1.setObjects(*((_A,_I),(_A,_F),(_A,_G),(_A,_M),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:ceAssetGroupRev1.setStatus(_B)
ceAssetEntityGroup=ObjectGroup((1,3,6,1,4,1,9,9,92,3,2,3))
ceAssetEntityGroup.setObjects(*((_A,_K),(_A,_J),(_A,_L),(_A,_N),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ceAssetEntityGroup.setStatus(_B)
ceAssetGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,92,3,2,4))
ceAssetGroupRev2.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ceAssetGroupRev2.setStatus(_D)
ciscoEntityAssetMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,92,3,1,1))
ciscoEntityAssetMIBCompliance.setObjects((_A,_W))
if mibBuilder.loadTexts:ciscoEntityAssetMIBCompliance.setStatus(_B)
ciscoEntityAssetMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,92,3,1,2))
ciscoEntityAssetMIBComplianceRev1.setObjects(*((_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoEntityAssetMIBComplianceRev1.setStatus(_B)
ciscoEntityAssetMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,92,3,1,3))
ciscoEntityAssetMIBComplianceRev2.setObjects((_A,_Z))
if mibBuilder.loadTexts:ciscoEntityAssetMIBComplianceRev2.setStatus(_D)
mibBuilder.exportSymbols(_A,**{'ciscoEntityAssetMIB':ciscoEntityAssetMIB,'ciscoEntityAssetMIBObjects':ciscoEntityAssetMIBObjects,'ceAssetTable':ceAssetTable,'ceAssetEntry':ceAssetEntry,_I:ceAssetOEMString,_J:ceAssetSerialNumber,_K:ceAssetOrderablePartNumber,_L:ceAssetHardwareRevision,_F:ceAssetMfgAssyNumber,_G:ceAssetMfgAssyRevision,_M:ceAssetFirmwareID,_N:ceAssetFirmwareRevision,_O:ceAssetSoftwareID,_P:ceAssetSoftwareRevision,_H:ceAssetCLEI,_Q:ceAssetAlias,_R:ceAssetTag,_S:ceAssetIsFRU,'ciscoEntityAssetMIBNotificationsPrefix':ciscoEntityAssetMIBNotificationsPrefix,'ciscoEntityAssetMIBNotifications':ciscoEntityAssetMIBNotifications,'ciscoEntityAssetMIBConformance':ciscoEntityAssetMIBConformance,'ciscoEntityAssetMIBCompliances':ciscoEntityAssetMIBCompliances,'ciscoEntityAssetMIBCompliance':ciscoEntityAssetMIBCompliance,'ciscoEntityAssetMIBComplianceRev1':ciscoEntityAssetMIBComplianceRev1,'ciscoEntityAssetMIBComplianceRev2':ciscoEntityAssetMIBComplianceRev2,'ciscoEntityAssetMIBGroups':ciscoEntityAssetMIBGroups,_W:ceAssetGroup,_X:ceAssetGroupRev1,_Y:ceAssetEntityGroup,_Z:ceAssetGroupRev2})