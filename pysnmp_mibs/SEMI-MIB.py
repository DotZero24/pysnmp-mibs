_AL='hpHttpMgDeviceSpecificGroup'
_AK='hpHttpMgExtendedNetCitizenTrapGroup'
_AJ='hpHttpMgExtendedNetCitizenGroup'
_AI='hpHttpMgEntityRelationshipGroup'
_AH='hpHttpMgClusterGroup'
_AG='hpHttpMgEnhancedNetCitizenTrapGroup'
_AF='hpHttpMgEnhancedNetCitizenGroup'
_AE='hpHttpMgBasicNetCitizenTrapGroup'
_AD='hpHttpMgBasicNetCitizenGroup'
_AC='hpHttpMgDeviceRemovedTrap'
_AB='hpHttpMgDeviceAddedTrap'
_AA='hpHttpMgNonRecoverableHealthTrap'
_A9='hpHttpMgCriticalHealthTrap'
_A8='hpHttpMgWarningHealthTrap'
_A7='hpHttpMgOKHealthTrap'
_A6='hpHttpMgUnknownHealthTrap'
_A5='hpHttpMgShutdown'
_A4='hpHttpMgHealthTrap'
_A3='hpHttpMgDeviceRelationshipType'
_A2='hpHttpMgDeviceRackPosition'
_A1='hpHttpMgDeviceRackId'
_A0='hpHttpMgDeviceLocation'
_z='hpHttpMgDeviceContactPagerNumber'
_y='hpHttpMgDeviceContactEmail'
_x='hpHttpMgDeviceContactPhone'
_w='hpHttpMgDeviceContactPerson'
_v='hpHttpMgDeviceAssetNumber'
_u='hpHttpMgDeviceROMVersion'
_t='hpHttpMgDeviceHWVersion'
_s='hpHttpMgDeviceVersion'
_r='hpHttpMgDeviceSerialNumber'
_q='hpHttpMgDeviceProductCaption'
_p='hpHttpMgDeviceProductName'
_o='hpHttpMgDeviceManufacturer'
_n='hpHttpMgDeviceHealth'
_m='hpHttpMgClusterName'
_l='hpHttpMgEntityNetInfoIPAddress'
_k='hpHttpMgEntityNetInfoURLLabel'
_j='hpHttpMgEntityNetInfoURL'
_i='hpHttpMgEntityNetInfoUniqueID'
_h='hpHttpMgEntityNetInfoRelationshipType'
_g='hpHttpMgEntityNetInfoSysObjID'
_f='hpHttpMgPhone'
_e='hpHttpMgAssetNumber'
_d='hpHttpMgSerialNumber'
_c='hpHttpMgROMVersion'
_b='hpHttpMgHWVersion'
_a='hpHttpMgVersion'
_Z='hpHttpMgProduct'
_Y='hpHttpMgManufacturer'
_X='hpHttpMgID'
_W='hpHttpMgMgmtSrvrURL'
_V='hpHttpMgDefaultURL'
_U='nonrecoverable'
_T='critical'
_S='warning'
_R='unknown'
_Q='hpHttpMgHealth'
_P='hpHttpMgEntityNetInfoIndex'
_O='hpHttpMgDefaultGroup'
_N='hpHttpMgDeviceSpecificFRU'
_M='hpHttpMgDeviceSpecificEventCode'
_L='Integer32'
_K='hpHttpMgDeviceManagementURLLabel'
_J='hpHttpMgDeviceManagementURL'
_I='hpHttpMgDeviceSysObjID'
_H='hpHttpMgDeviceGlobalUniqueID'
_G='hpHttpMgDeviceIndex'
_F='Utf8String'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='SEMI-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpHttpMgMod=ModuleIdentity((1,3,6,1,4,1,11,2,36,1))
if mibBuilder.loadTexts:hpHttpMgMod.setRevisions(('2000-10-16 00:00','2000-10-12 00:00','2000-10-04 00:00','2000-01-12 00:00','1999-03-17 00:00','1998-12-01 00:00','1997-06-26 00:00','1996-06-12 00:00'))
class Utf8String(TextualConvention,OctetString):status=_B;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_HpWebMgmt_ObjectIdentity=ObjectIdentity
hpWebMgmt=_HpWebMgmt_ObjectIdentity((1,3,6,1,4,1,11,2,36))
_HpHttpMgTraps_ObjectIdentity=ObjectIdentity
hpHttpMgTraps=_HpHttpMgTraps_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,0))
_HpHttpMgDeviceSpecificEventCode_Type=Utf8String
_HpHttpMgDeviceSpecificEventCode_Object=MibScalar
hpHttpMgDeviceSpecificEventCode=_HpHttpMgDeviceSpecificEventCode_Object((1,3,6,1,4,1,11,2,36,1,0,10),_HpHttpMgDeviceSpecificEventCode_Type())
hpHttpMgDeviceSpecificEventCode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceSpecificEventCode.setStatus(_B)
_HpHttpMgDeviceSpecificFRU_Type=Utf8String
_HpHttpMgDeviceSpecificFRU_Object=MibScalar
hpHttpMgDeviceSpecificFRU=_HpHttpMgDeviceSpecificFRU_Object((1,3,6,1,4,1,11,2,36,1,0,11),_HpHttpMgDeviceSpecificFRU_Type())
hpHttpMgDeviceSpecificFRU.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceSpecificFRU.setStatus(_B)
_HpHttpMgObjects_ObjectIdentity=ObjectIdentity
hpHttpMgObjects=_HpHttpMgObjects_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1))
_HpHttpMgDefaults_ObjectIdentity=ObjectIdentity
hpHttpMgDefaults=_HpHttpMgDefaults_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1,1))
_HpHttpMgDefaultURL_Type=Utf8String
_HpHttpMgDefaultURL_Object=MibScalar
hpHttpMgDefaultURL=_HpHttpMgDefaultURL_Object((1,3,6,1,4,1,11,2,36,1,1,1,1),_HpHttpMgDefaultURL_Type())
hpHttpMgDefaultURL.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDefaultURL.setStatus(_B)
_HpHttpMgNetCitizen_ObjectIdentity=ObjectIdentity
hpHttpMgNetCitizen=_HpHttpMgNetCitizen_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1,2))
_HpHttpMgMgmtSrvrURL_Type=Utf8String
_HpHttpMgMgmtSrvrURL_Object=MibScalar
hpHttpMgMgmtSrvrURL=_HpHttpMgMgmtSrvrURL_Object((1,3,6,1,4,1,11,2,36,1,1,2,1),_HpHttpMgMgmtSrvrURL_Type())
hpHttpMgMgmtSrvrURL.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgMgmtSrvrURL.setStatus(_D)
_HpHttpMgID_Type=Utf8String
_HpHttpMgID_Object=MibScalar
hpHttpMgID=_HpHttpMgID_Object((1,3,6,1,4,1,11,2,36,1,1,2,2),_HpHttpMgID_Type())
hpHttpMgID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgID.setStatus(_D)
class _HpHttpMgHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('information',2),('ok',3),(_S,4),(_T,5),(_U,6)))
_HpHttpMgHealth_Type.__name__=_L
_HpHttpMgHealth_Object=MibScalar
hpHttpMgHealth=_HpHttpMgHealth_Object((1,3,6,1,4,1,11,2,36,1,1,2,3),_HpHttpMgHealth_Type())
hpHttpMgHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgHealth.setStatus(_D)
_HpHttpMgManufacturer_Type=Utf8String
_HpHttpMgManufacturer_Object=MibScalar
hpHttpMgManufacturer=_HpHttpMgManufacturer_Object((1,3,6,1,4,1,11,2,36,1,1,2,4),_HpHttpMgManufacturer_Type())
hpHttpMgManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgManufacturer.setStatus(_D)
class _HpHttpMgProduct_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgProduct_Type.__name__=_F
_HpHttpMgProduct_Object=MibScalar
hpHttpMgProduct=_HpHttpMgProduct_Object((1,3,6,1,4,1,11,2,36,1,1,2,5),_HpHttpMgProduct_Type())
hpHttpMgProduct.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgProduct.setStatus(_D)
class _HpHttpMgVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgVersion_Type.__name__=_F
_HpHttpMgVersion_Object=MibScalar
hpHttpMgVersion=_HpHttpMgVersion_Object((1,3,6,1,4,1,11,2,36,1,1,2,6),_HpHttpMgVersion_Type())
hpHttpMgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgVersion.setStatus(_D)
class _HpHttpMgHWVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgHWVersion_Type.__name__=_F
_HpHttpMgHWVersion_Object=MibScalar
hpHttpMgHWVersion=_HpHttpMgHWVersion_Object((1,3,6,1,4,1,11,2,36,1,1,2,7),_HpHttpMgHWVersion_Type())
hpHttpMgHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgHWVersion.setStatus(_D)
class _HpHttpMgROMVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgROMVersion_Type.__name__=_F
_HpHttpMgROMVersion_Object=MibScalar
hpHttpMgROMVersion=_HpHttpMgROMVersion_Object((1,3,6,1,4,1,11,2,36,1,1,2,8),_HpHttpMgROMVersion_Type())
hpHttpMgROMVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgROMVersion.setStatus(_D)
class _HpHttpMgSerialNumber_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgSerialNumber_Type.__name__=_F
_HpHttpMgSerialNumber_Object=MibScalar
hpHttpMgSerialNumber=_HpHttpMgSerialNumber_Object((1,3,6,1,4,1,11,2,36,1,1,2,9),_HpHttpMgSerialNumber_Type())
hpHttpMgSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgSerialNumber.setStatus(_D)
class _HpHttpMgAssetNumber_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgAssetNumber_Type.__name__=_F
_HpHttpMgAssetNumber_Object=MibScalar
hpHttpMgAssetNumber=_HpHttpMgAssetNumber_Object((1,3,6,1,4,1,11,2,36,1,1,2,10),_HpHttpMgAssetNumber_Type())
hpHttpMgAssetNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgAssetNumber.setStatus(_D)
class _HpHttpMgPhone_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgPhone_Type.__name__=_F
_HpHttpMgPhone_Object=MibScalar
hpHttpMgPhone=_HpHttpMgPhone_Object((1,3,6,1,4,1,11,2,36,1,1,2,11),_HpHttpMgPhone_Type())
hpHttpMgPhone.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgPhone.setStatus(_D)
_HpHttpMgEntityNetInfo_ObjectIdentity=ObjectIdentity
hpHttpMgEntityNetInfo=_HpHttpMgEntityNetInfo_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1,3))
_HpHttpMgEntityNetInfoTable_Object=MibTable
hpHttpMgEntityNetInfoTable=_HpHttpMgEntityNetInfoTable_Object((1,3,6,1,4,1,11,2,36,1,1,3,1))
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoTable.setStatus(_B)
_HpHttpMgEntityNetInfoEntry_Object=MibTableRow
hpHttpMgEntityNetInfoEntry=_HpHttpMgEntityNetInfoEntry_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1))
hpHttpMgEntityNetInfoEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoEntry.setStatus(_B)
class _HpHttpMgEntityNetInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HpHttpMgEntityNetInfoIndex_Type.__name__=_L
_HpHttpMgEntityNetInfoIndex_Object=MibTableColumn
hpHttpMgEntityNetInfoIndex=_HpHttpMgEntityNetInfoIndex_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1,1),_HpHttpMgEntityNetInfoIndex_Type())
hpHttpMgEntityNetInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoIndex.setStatus(_B)
_HpHttpMgEntityNetInfoSysObjID_Type=Utf8String
_HpHttpMgEntityNetInfoSysObjID_Object=MibTableColumn
hpHttpMgEntityNetInfoSysObjID=_HpHttpMgEntityNetInfoSysObjID_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1,2),_HpHttpMgEntityNetInfoSysObjID_Type())
hpHttpMgEntityNetInfoSysObjID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoSysObjID.setStatus(_B)
class _HpHttpMgEntityNetInfoRelationshipType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('self',0),('containedEntity',1),('containingEntity',2),('externallyAttachedEntity',3),('indirectlyAttachedEntity',4),('clusterNode',5)))
_HpHttpMgEntityNetInfoRelationshipType_Type.__name__=_L
_HpHttpMgEntityNetInfoRelationshipType_Object=MibTableColumn
hpHttpMgEntityNetInfoRelationshipType=_HpHttpMgEntityNetInfoRelationshipType_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1,3),_HpHttpMgEntityNetInfoRelationshipType_Type())
hpHttpMgEntityNetInfoRelationshipType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoRelationshipType.setStatus(_B)
_HpHttpMgEntityNetInfoUniqueID_Type=Utf8String
_HpHttpMgEntityNetInfoUniqueID_Object=MibTableColumn
hpHttpMgEntityNetInfoUniqueID=_HpHttpMgEntityNetInfoUniqueID_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1,4),_HpHttpMgEntityNetInfoUniqueID_Type())
hpHttpMgEntityNetInfoUniqueID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoUniqueID.setStatus(_B)
_HpHttpMgEntityNetInfoURL_Type=Utf8String
_HpHttpMgEntityNetInfoURL_Object=MibTableColumn
hpHttpMgEntityNetInfoURL=_HpHttpMgEntityNetInfoURL_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1,5),_HpHttpMgEntityNetInfoURL_Type())
hpHttpMgEntityNetInfoURL.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoURL.setStatus(_B)
_HpHttpMgEntityNetInfoURLLabel_Type=Utf8String
_HpHttpMgEntityNetInfoURLLabel_Object=MibTableColumn
hpHttpMgEntityNetInfoURLLabel=_HpHttpMgEntityNetInfoURLLabel_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1,6),_HpHttpMgEntityNetInfoURLLabel_Type())
hpHttpMgEntityNetInfoURLLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoURLLabel.setStatus(_B)
_HpHttpMgEntityNetInfoIPAddress_Type=Utf8String
_HpHttpMgEntityNetInfoIPAddress_Object=MibTableColumn
hpHttpMgEntityNetInfoIPAddress=_HpHttpMgEntityNetInfoIPAddress_Object((1,3,6,1,4,1,11,2,36,1,1,3,1,1,7),_HpHttpMgEntityNetInfoIPAddress_Type())
hpHttpMgEntityNetInfoIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgEntityNetInfoIPAddress.setStatus(_B)
_HpHttpMgCluster_ObjectIdentity=ObjectIdentity
hpHttpMgCluster=_HpHttpMgCluster_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1,4))
_HpHttpMgClusterName_Type=Utf8String
_HpHttpMgClusterName_Object=MibScalar
hpHttpMgClusterName=_HpHttpMgClusterName_Object((1,3,6,1,4,1,11,2,36,1,1,4,1),_HpHttpMgClusterName_Type())
hpHttpMgClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgClusterName.setStatus(_B)
_HpHttpMgDeviceInfo_ObjectIdentity=ObjectIdentity
hpHttpMgDeviceInfo=_HpHttpMgDeviceInfo_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1,5))
_HpHttpMgDeviceTable_Object=MibTable
hpHttpMgDeviceTable=_HpHttpMgDeviceTable_Object((1,3,6,1,4,1,11,2,36,1,1,5,1))
if mibBuilder.loadTexts:hpHttpMgDeviceTable.setStatus(_B)
_HpHttpMgDeviceEntry_Object=MibTableRow
hpHttpMgDeviceEntry=_HpHttpMgDeviceEntry_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1))
hpHttpMgDeviceEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:hpHttpMgDeviceEntry.setStatus(_B)
class _HpHttpMgDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_HpHttpMgDeviceIndex_Type.__name__=_L
_HpHttpMgDeviceIndex_Object=MibTableColumn
hpHttpMgDeviceIndex=_HpHttpMgDeviceIndex_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,1),_HpHttpMgDeviceIndex_Type())
hpHttpMgDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceIndex.setStatus(_B)
_HpHttpMgDeviceGlobalUniqueID_Type=Utf8String
_HpHttpMgDeviceGlobalUniqueID_Object=MibTableColumn
hpHttpMgDeviceGlobalUniqueID=_HpHttpMgDeviceGlobalUniqueID_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,2),_HpHttpMgDeviceGlobalUniqueID_Type())
hpHttpMgDeviceGlobalUniqueID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceGlobalUniqueID.setStatus(_B)
class _HpHttpMgDeviceHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('unused',2),('ok',3),(_S,4),(_T,5),(_U,6)))
_HpHttpMgDeviceHealth_Type.__name__=_L
_HpHttpMgDeviceHealth_Object=MibTableColumn
hpHttpMgDeviceHealth=_HpHttpMgDeviceHealth_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,3),_HpHttpMgDeviceHealth_Type())
hpHttpMgDeviceHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceHealth.setStatus(_B)
_HpHttpMgDeviceSysObjID_Type=Utf8String
_HpHttpMgDeviceSysObjID_Object=MibTableColumn
hpHttpMgDeviceSysObjID=_HpHttpMgDeviceSysObjID_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,4),_HpHttpMgDeviceSysObjID_Type())
hpHttpMgDeviceSysObjID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceSysObjID.setStatus(_B)
_HpHttpMgDeviceManagementURL_Type=Utf8String
_HpHttpMgDeviceManagementURL_Object=MibTableColumn
hpHttpMgDeviceManagementURL=_HpHttpMgDeviceManagementURL_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,5),_HpHttpMgDeviceManagementURL_Type())
hpHttpMgDeviceManagementURL.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceManagementURL.setStatus(_B)
_HpHttpMgDeviceManagementURLLabel_Type=Utf8String
_HpHttpMgDeviceManagementURLLabel_Object=MibTableColumn
hpHttpMgDeviceManagementURLLabel=_HpHttpMgDeviceManagementURLLabel_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,6),_HpHttpMgDeviceManagementURLLabel_Type())
hpHttpMgDeviceManagementURLLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceManagementURLLabel.setStatus(_B)
_HpHttpMgDeviceManufacturer_Type=Utf8String
_HpHttpMgDeviceManufacturer_Object=MibTableColumn
hpHttpMgDeviceManufacturer=_HpHttpMgDeviceManufacturer_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,7),_HpHttpMgDeviceManufacturer_Type())
hpHttpMgDeviceManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceManufacturer.setStatus(_B)
_HpHttpMgDeviceProductName_Type=Utf8String
_HpHttpMgDeviceProductName_Object=MibTableColumn
hpHttpMgDeviceProductName=_HpHttpMgDeviceProductName_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,8),_HpHttpMgDeviceProductName_Type())
hpHttpMgDeviceProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceProductName.setStatus(_B)
_HpHttpMgDeviceProductCaption_Type=Utf8String
_HpHttpMgDeviceProductCaption_Object=MibTableColumn
hpHttpMgDeviceProductCaption=_HpHttpMgDeviceProductCaption_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,9),_HpHttpMgDeviceProductCaption_Type())
hpHttpMgDeviceProductCaption.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceProductCaption.setStatus(_B)
_HpHttpMgDeviceSerialNumber_Type=Utf8String
_HpHttpMgDeviceSerialNumber_Object=MibTableColumn
hpHttpMgDeviceSerialNumber=_HpHttpMgDeviceSerialNumber_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,10),_HpHttpMgDeviceSerialNumber_Type())
hpHttpMgDeviceSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceSerialNumber.setStatus(_B)
class _HpHttpMgDeviceVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgDeviceVersion_Type.__name__=_F
_HpHttpMgDeviceVersion_Object=MibTableColumn
hpHttpMgDeviceVersion=_HpHttpMgDeviceVersion_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,11),_HpHttpMgDeviceVersion_Type())
hpHttpMgDeviceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceVersion.setStatus(_B)
class _HpHttpMgDeviceHWVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgDeviceHWVersion_Type.__name__=_F
_HpHttpMgDeviceHWVersion_Object=MibTableColumn
hpHttpMgDeviceHWVersion=_HpHttpMgDeviceHWVersion_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,12),_HpHttpMgDeviceHWVersion_Type())
hpHttpMgDeviceHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceHWVersion.setStatus(_B)
class _HpHttpMgDeviceROMVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgDeviceROMVersion_Type.__name__=_F
_HpHttpMgDeviceROMVersion_Object=MibTableColumn
hpHttpMgDeviceROMVersion=_HpHttpMgDeviceROMVersion_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,13),_HpHttpMgDeviceROMVersion_Type())
hpHttpMgDeviceROMVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceROMVersion.setStatus(_B)
class _HpHttpMgDeviceAssetNumber_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgDeviceAssetNumber_Type.__name__=_F
_HpHttpMgDeviceAssetNumber_Object=MibTableColumn
hpHttpMgDeviceAssetNumber=_HpHttpMgDeviceAssetNumber_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,14),_HpHttpMgDeviceAssetNumber_Type())
hpHttpMgDeviceAssetNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceAssetNumber.setStatus(_B)
class _HpHttpMgDeviceContactPerson_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgDeviceContactPerson_Type.__name__=_F
_HpHttpMgDeviceContactPerson_Object=MibTableColumn
hpHttpMgDeviceContactPerson=_HpHttpMgDeviceContactPerson_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,15),_HpHttpMgDeviceContactPerson_Type())
hpHttpMgDeviceContactPerson.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceContactPerson.setStatus(_B)
class _HpHttpMgDeviceContactPhone_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgDeviceContactPhone_Type.__name__=_F
_HpHttpMgDeviceContactPhone_Object=MibTableColumn
hpHttpMgDeviceContactPhone=_HpHttpMgDeviceContactPhone_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,16),_HpHttpMgDeviceContactPhone_Type())
hpHttpMgDeviceContactPhone.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceContactPhone.setStatus(_B)
_HpHttpMgDeviceContactEmail_Type=Utf8String
_HpHttpMgDeviceContactEmail_Object=MibTableColumn
hpHttpMgDeviceContactEmail=_HpHttpMgDeviceContactEmail_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,17),_HpHttpMgDeviceContactEmail_Type())
hpHttpMgDeviceContactEmail.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceContactEmail.setStatus(_B)
class _HpHttpMgDeviceContactPagerNumber_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgDeviceContactPagerNumber_Type.__name__=_F
_HpHttpMgDeviceContactPagerNumber_Object=MibTableColumn
hpHttpMgDeviceContactPagerNumber=_HpHttpMgDeviceContactPagerNumber_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,18),_HpHttpMgDeviceContactPagerNumber_Type())
hpHttpMgDeviceContactPagerNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceContactPagerNumber.setStatus(_B)
_HpHttpMgDeviceLocation_Type=Utf8String
_HpHttpMgDeviceLocation_Object=MibTableColumn
hpHttpMgDeviceLocation=_HpHttpMgDeviceLocation_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,19),_HpHttpMgDeviceLocation_Type())
hpHttpMgDeviceLocation.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceLocation.setStatus(_B)
_HpHttpMgDeviceRackId_Type=Utf8String
_HpHttpMgDeviceRackId_Object=MibTableColumn
hpHttpMgDeviceRackId=_HpHttpMgDeviceRackId_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,20),_HpHttpMgDeviceRackId_Type())
hpHttpMgDeviceRackId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceRackId.setStatus(_B)
_HpHttpMgDeviceRackPosition_Type=Utf8String
_HpHttpMgDeviceRackPosition_Object=MibTableColumn
hpHttpMgDeviceRackPosition=_HpHttpMgDeviceRackPosition_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,21),_HpHttpMgDeviceRackPosition_Type())
hpHttpMgDeviceRackPosition.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDeviceRackPosition.setStatus(_B)
class _HpHttpMgDeviceRelationshipType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('host',1),('other',2)))
_HpHttpMgDeviceRelationshipType_Type.__name__=_L
_HpHttpMgDeviceRelationshipType_Object=MibTableColumn
hpHttpMgDeviceRelationshipType=_HpHttpMgDeviceRelationshipType_Object((1,3,6,1,4,1,11,2,36,1,1,5,1,1,22),_HpHttpMgDeviceRelationshipType_Type())
hpHttpMgDeviceRelationshipType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpHttpMgDeviceRelationshipType.setStatus(_B)
_HpHttpMgGroups_ObjectIdentity=ObjectIdentity
hpHttpMgGroups=_HpHttpMgGroups_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,2))
_HpHttpMgCompliances_ObjectIdentity=ObjectIdentity
hpHttpMgCompliances=_HpHttpMgCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,3))
hpHttpMgDefaultGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,1))
hpHttpMgDefaultGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:hpHttpMgDefaultGroup.setStatus(_B)
hpHttpMgBasicNetCitizenGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,2))
hpHttpMgBasicNetCitizenGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Q),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpHttpMgBasicNetCitizenGroup.setStatus(_D)
hpHttpMgExtendedNetCitizenGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,4))
hpHttpMgExtendedNetCitizenGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:hpHttpMgExtendedNetCitizenGroup.setStatus(_D)
hpHttpMgEntityRelationshipGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,6))
hpHttpMgEntityRelationshipGroup.setObjects(*((_A,_P),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:hpHttpMgEntityRelationshipGroup.setStatus(_B)
hpHttpMgClusterGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,7))
hpHttpMgClusterGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:hpHttpMgClusterGroup.setStatus(_B)
hpHttpMgEnhancedNetCitizenGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,8))
hpHttpMgEnhancedNetCitizenGroup.setObjects(*((_A,_G),(_A,_H),(_A,_n),(_A,_I),(_A,_J),(_A,_K),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:hpHttpMgEnhancedNetCitizenGroup.setStatus(_B)
hpHttpMgDeviceSpecificGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,10))
hpHttpMgDeviceSpecificGroup.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpHttpMgDeviceSpecificGroup.setStatus(_B)
hpHttpMgHealthTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,1))
hpHttpMgHealthTrap.setObjects((_A,_Q))
if mibBuilder.loadTexts:hpHttpMgHealthTrap.setStatus(_D)
hpHttpMgShutdown=NotificationType((1,3,6,1,4,1,11,2,36,1,0,2))
if mibBuilder.loadTexts:hpHttpMgShutdown.setStatus(_D)
hpHttpMgUnknownHealthTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,3))
hpHttpMgUnknownHealthTrap.setObjects(*((_A,_G),(_A,_I),(_A,_H),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpHttpMgUnknownHealthTrap.setStatus(_B)
hpHttpMgOKHealthTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,4))
hpHttpMgOKHealthTrap.setObjects(*((_A,_G),(_A,_I),(_A,_H),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpHttpMgOKHealthTrap.setStatus(_B)
hpHttpMgWarningHealthTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,5))
hpHttpMgWarningHealthTrap.setObjects(*((_A,_G),(_A,_I),(_A,_H),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpHttpMgWarningHealthTrap.setStatus(_B)
hpHttpMgCriticalHealthTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,6))
hpHttpMgCriticalHealthTrap.setObjects(*((_A,_G),(_A,_I),(_A,_H),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpHttpMgCriticalHealthTrap.setStatus(_B)
hpHttpMgNonRecoverableHealthTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,7))
hpHttpMgNonRecoverableHealthTrap.setObjects(*((_A,_G),(_A,_I),(_A,_H),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpHttpMgNonRecoverableHealthTrap.setStatus(_B)
hpHttpMgDeviceAddedTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,8))
hpHttpMgDeviceAddedTrap.setObjects(*((_A,_G),(_A,_I),(_A,_H),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpHttpMgDeviceAddedTrap.setStatus(_B)
hpHttpMgDeviceRemovedTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,9))
hpHttpMgDeviceRemovedTrap.setObjects(*((_A,_G),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:hpHttpMgDeviceRemovedTrap.setStatus(_B)
hpHttpMgBasicNetCitizenTrapGroup=NotificationGroup((1,3,6,1,4,1,11,2,36,1,2,3))
hpHttpMgBasicNetCitizenTrapGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:hpHttpMgBasicNetCitizenTrapGroup.setStatus(_D)
hpHttpMgExtendedNetCitizenTrapGroup=NotificationGroup((1,3,6,1,4,1,11,2,36,1,2,5))
hpHttpMgExtendedNetCitizenTrapGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:hpHttpMgExtendedNetCitizenTrapGroup.setStatus(_B)
hpHttpMgEnhancedNetCitizenTrapGroup=NotificationGroup((1,3,6,1,4,1,11,2,36,1,2,9))
hpHttpMgEnhancedNetCitizenTrapGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:hpHttpMgEnhancedNetCitizenTrapGroup.setStatus(_B)
hpHttpMgMinCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,1))
hpHttpMgMinCompliance.setObjects((_A,_O))
if mibBuilder.loadTexts:hpHttpMgMinCompliance.setStatus(_B)
hpHttpMgBasicNetCitizenCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,2))
hpHttpMgBasicNetCitizenCompliance.setObjects(*((_A,_O),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:hpHttpMgBasicNetCitizenCompliance.setStatus(_D)
hpHttpMgEnhancedNetCitizenCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,3))
hpHttpMgEnhancedNetCitizenCompliance.setObjects(*((_A,_O),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:hpHttpMgEnhancedNetCitizenCompliance.setStatus(_B)
hpHttpMgExtentedNetCitizenCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,4))
hpHttpMgExtentedNetCitizenCompliance.setObjects(*((_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:hpHttpMgExtentedNetCitizenCompliance.setStatus(_B)
hpHttpMgExtentedNetCitizenCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,5))
hpHttpMgExtentedNetCitizenCompliance1.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:hpHttpMgExtentedNetCitizenCompliance1.setStatus(_D)
hpHttpMgExtentedNetCitizenCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,6))
hpHttpMgExtentedNetCitizenCompliance2.setObjects((_A,_AL))
if mibBuilder.loadTexts:hpHttpMgExtentedNetCitizenCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_F:Utf8String,'hp':hp,'nm':nm,'hpWebMgmt':hpWebMgmt,'hpHttpMgMod':hpHttpMgMod,'hpHttpMgTraps':hpHttpMgTraps,_A4:hpHttpMgHealthTrap,_A5:hpHttpMgShutdown,_A6:hpHttpMgUnknownHealthTrap,_A7:hpHttpMgOKHealthTrap,_A8:hpHttpMgWarningHealthTrap,_A9:hpHttpMgCriticalHealthTrap,_AA:hpHttpMgNonRecoverableHealthTrap,_AB:hpHttpMgDeviceAddedTrap,_AC:hpHttpMgDeviceRemovedTrap,_M:hpHttpMgDeviceSpecificEventCode,_N:hpHttpMgDeviceSpecificFRU,'hpHttpMgObjects':hpHttpMgObjects,'hpHttpMgDefaults':hpHttpMgDefaults,_V:hpHttpMgDefaultURL,'hpHttpMgNetCitizen':hpHttpMgNetCitizen,_W:hpHttpMgMgmtSrvrURL,_X:hpHttpMgID,_Q:hpHttpMgHealth,_Y:hpHttpMgManufacturer,_Z:hpHttpMgProduct,_a:hpHttpMgVersion,_b:hpHttpMgHWVersion,_c:hpHttpMgROMVersion,_d:hpHttpMgSerialNumber,_e:hpHttpMgAssetNumber,_f:hpHttpMgPhone,'hpHttpMgEntityNetInfo':hpHttpMgEntityNetInfo,'hpHttpMgEntityNetInfoTable':hpHttpMgEntityNetInfoTable,'hpHttpMgEntityNetInfoEntry':hpHttpMgEntityNetInfoEntry,_P:hpHttpMgEntityNetInfoIndex,_g:hpHttpMgEntityNetInfoSysObjID,_h:hpHttpMgEntityNetInfoRelationshipType,_i:hpHttpMgEntityNetInfoUniqueID,_j:hpHttpMgEntityNetInfoURL,_k:hpHttpMgEntityNetInfoURLLabel,_l:hpHttpMgEntityNetInfoIPAddress,'hpHttpMgCluster':hpHttpMgCluster,_m:hpHttpMgClusterName,'hpHttpMgDeviceInfo':hpHttpMgDeviceInfo,'hpHttpMgDeviceTable':hpHttpMgDeviceTable,'hpHttpMgDeviceEntry':hpHttpMgDeviceEntry,_G:hpHttpMgDeviceIndex,_H:hpHttpMgDeviceGlobalUniqueID,_n:hpHttpMgDeviceHealth,_I:hpHttpMgDeviceSysObjID,_J:hpHttpMgDeviceManagementURL,_K:hpHttpMgDeviceManagementURLLabel,_o:hpHttpMgDeviceManufacturer,_p:hpHttpMgDeviceProductName,_q:hpHttpMgDeviceProductCaption,_r:hpHttpMgDeviceSerialNumber,_s:hpHttpMgDeviceVersion,_t:hpHttpMgDeviceHWVersion,_u:hpHttpMgDeviceROMVersion,_v:hpHttpMgDeviceAssetNumber,_w:hpHttpMgDeviceContactPerson,_x:hpHttpMgDeviceContactPhone,_y:hpHttpMgDeviceContactEmail,_z:hpHttpMgDeviceContactPagerNumber,_A0:hpHttpMgDeviceLocation,_A1:hpHttpMgDeviceRackId,_A2:hpHttpMgDeviceRackPosition,_A3:hpHttpMgDeviceRelationshipType,'hpHttpMgGroups':hpHttpMgGroups,_O:hpHttpMgDefaultGroup,_AD:hpHttpMgBasicNetCitizenGroup,_AE:hpHttpMgBasicNetCitizenTrapGroup,_AJ:hpHttpMgExtendedNetCitizenGroup,_AK:hpHttpMgExtendedNetCitizenTrapGroup,_AI:hpHttpMgEntityRelationshipGroup,_AH:hpHttpMgClusterGroup,_AF:hpHttpMgEnhancedNetCitizenGroup,_AG:hpHttpMgEnhancedNetCitizenTrapGroup,_AL:hpHttpMgDeviceSpecificGroup,'hpHttpMgCompliances':hpHttpMgCompliances,'hpHttpMgMinCompliance':hpHttpMgMinCompliance,'hpHttpMgBasicNetCitizenCompliance':hpHttpMgBasicNetCitizenCompliance,'hpHttpMgEnhancedNetCitizenCompliance':hpHttpMgEnhancedNetCitizenCompliance,'hpHttpMgExtentedNetCitizenCompliance':hpHttpMgExtentedNetCitizenCompliance,'hpHttpMgExtentedNetCitizenCompliance1':hpHttpMgExtentedNetCitizenCompliance1,'hpHttpMgExtentedNetCitizenCompliance2':hpHttpMgExtentedNetCitizenCompliance2})