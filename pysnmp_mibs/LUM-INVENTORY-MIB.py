_AT='invInsRemGroup'
_AS='invGeneralGroupV5'
_AR='invGeneralGroupV3'
_AQ='invPhysGroupV2'
_AP='invGeneralGroup'
_AO='invNotificationPhysRemoved'
_AN='invNotificationPhysAdded'
_AM='invGeneralInsRemLastSeqNumber'
_AL='invGeneralInsRemTableSize'
_AK='invInsRemSeqNumber'
_AJ='invInsRemPartNumber'
_AI='invInsRemSerialNumber'
_AH='invInsRemClei'
_AG='invInsRemPhysicalLocation'
_AF='invInsRemEquipmentType'
_AE='invInsRemTimestamp'
_AD='invInsRemEvent'
_AC='invInsRemName'
_AB='invPhysAid'
_AA='invPhysClei'
_A9='invRelationEntityName2'
_A8='invRelationEntityIndex2'
_A7='invRelationType'
_A6='invRelationEntityName1'
_A5='invRelationEntityIndex1'
_A4='invEntityClass'
_A3='invEntityObject'
_A2='invEntityName'
_A1='invGeneralTestAndIncr'
_A0='invGeneralMibImplVersion'
_z='invGeneralMibSpecVersion'
_y='module'
_x='sensor'
_w='powerSupply'
_v='container'
_u='backplane'
_t='chassis'
_s='unknown'
_r='SnmpAdminString'
_q='invPhysGroupV4'
_p='invPhysGroup'
_o='invInsRemIndex'
_n='invRelationIndex'
_m='invEntityIndex'
_l='read-write'
_k='undefined'
_j='Integer32'
_i='inventoryGeneralMinimalGroupV1'
_h='invPhysGroupV5'
_g='invGeneralGroupV4'
_f='invGeneralRelationTableSize'
_e='invGeneralEntityTableSize'
_d='invGeneralPhysTableSize'
_c='invPhysSoftwareProduct'
_b='invGeneralGroupV2'
_a='invGeneralConfigLastChangeTime'
_Z='invPhysSoftwareRev'
_Y='invPhysGroupV3'
_X='invPhysVendorType'
_W='invGeneralLastChangeTime'
_V='DisplayString'
_U='invPhysIsFRU'
_T='invPhysModelName'
_S='invPhysMfgName'
_R='invPhysSerialNum'
_Q='invPhysProductDataRev'
_P='invPhysFirmwareRev'
_O='invPhysHardwareRev'
_N='invPhysName'
_M='invPhysParentRelPos'
_L='invPhysClass'
_K='invPhysContainedIn'
_J='invPhysDescr'
_I='Unsigned32'
_H='invPhysIndex'
_G='invRelationGroup'
_F='invEntityGroup'
_E='invEventGroup'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-INVENTORY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumInventoryMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumInventoryMIB','lumModules')
MgmtNameString,=mibBuilder.importSymbols('LUM-TC','MgmtNameString')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_r)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_j,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
AutonomousType,DateAndTime,DisplayString,PhysAddress,RowPointer,TextualConvention,TestAndIncr,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime',_V,'PhysAddress','RowPointer','TextualConvention','TestAndIncr','TruthValue')
lumInventoryMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,5))
if mibBuilder.loadTexts:lumInventoryMIBModule.setRevisions(('2017-06-15 00:00','2014-09-30 00:00','2005-09-14 00:00','2004-09-30 00:00','2002-03-08 00:00','2001-10-30 00:00','2001-07-17 00:00','2001-05-11 00:00','2001-05-10 00:00'))
class PhysicalClass(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_k,0),('other',1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6),('fan',7),(_x,8),(_y,9),('port',10),('stack',11)))
class EntityClass(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_k,0),('other',1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6),('fan',7),(_x,8),(_y,9),('port',10),('stack',11),('logical',12)))
class InsRemEventType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('insert',0),('remove',1)))
_LumInventoryConfs_ObjectIdentity=ObjectIdentity
lumInventoryConfs=_LumInventoryConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,3,1))
_LumInventoryGroups_ObjectIdentity=ObjectIdentity
lumInventoryGroups=_LumInventoryGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,3,1,1))
_LumInventoryCompl_ObjectIdentity=ObjectIdentity
lumInventoryCompl=_LumInventoryCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,3,1,2))
_LumInventoryMinimalGroups_ObjectIdentity=ObjectIdentity
lumInventoryMinimalGroups=_LumInventoryMinimalGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,3,1,3))
_LumInventoryMinimalCompl_ObjectIdentity=ObjectIdentity
lumInventoryMinimalCompl=_LumInventoryMinimalCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,3,1,4))
_LumInventoryMIBObjects_ObjectIdentity=ObjectIdentity
lumInventoryMIBObjects=_LumInventoryMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2))
_InvPhysical_ObjectIdentity=ObjectIdentity
invPhysical=_InvPhysical_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2,1))
_InvPhysTable_Object=MibTable
invPhysTable=_InvPhysTable_Object((1,3,6,1,4,1,8708,2,3,2,1,1))
if mibBuilder.loadTexts:invPhysTable.setStatus(_B)
_InvPhysEntry_Object=MibTableRow
invPhysEntry=_InvPhysEntry_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1))
invPhysEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:invPhysEntry.setStatus(_B)
class _InvPhysIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InvPhysIndex_Type.__name__=_I
_InvPhysIndex_Object=MibTableColumn
invPhysIndex=_InvPhysIndex_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,1),_InvPhysIndex_Type())
invPhysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysIndex.setStatus(_B)
_InvPhysDescr_Type=SnmpAdminString
_InvPhysDescr_Object=MibTableColumn
invPhysDescr=_InvPhysDescr_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,2),_InvPhysDescr_Type())
invPhysDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysDescr.setStatus(_B)
_InvPhysVendorType_Type=AutonomousType
_InvPhysVendorType_Object=MibTableColumn
invPhysVendorType=_InvPhysVendorType_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,3),_InvPhysVendorType_Type())
invPhysVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysVendorType.setStatus(_D)
class _InvPhysContainedIn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_InvPhysContainedIn_Type.__name__=_I
_InvPhysContainedIn_Object=MibTableColumn
invPhysContainedIn=_InvPhysContainedIn_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,4),_InvPhysContainedIn_Type())
invPhysContainedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysContainedIn.setStatus(_B)
_InvPhysClass_Type=PhysicalClass
_InvPhysClass_Object=MibTableColumn
invPhysClass=_InvPhysClass_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,5),_InvPhysClass_Type())
invPhysClass.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysClass.setStatus(_B)
class _InvPhysParentRelPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_InvPhysParentRelPos_Type.__name__=_j
_InvPhysParentRelPos_Object=MibTableColumn
invPhysParentRelPos=_InvPhysParentRelPos_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,6),_InvPhysParentRelPos_Type())
invPhysParentRelPos.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysParentRelPos.setStatus(_B)
_InvPhysName_Type=MgmtNameString
_InvPhysName_Object=MibTableColumn
invPhysName=_InvPhysName_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,7),_InvPhysName_Type())
invPhysName.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysName.setStatus(_B)
_InvPhysHardwareRev_Type=SnmpAdminString
_InvPhysHardwareRev_Object=MibTableColumn
invPhysHardwareRev=_InvPhysHardwareRev_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,8),_InvPhysHardwareRev_Type())
invPhysHardwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysHardwareRev.setStatus(_B)
_InvPhysFirmwareRev_Type=SnmpAdminString
_InvPhysFirmwareRev_Object=MibTableColumn
invPhysFirmwareRev=_InvPhysFirmwareRev_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,9),_InvPhysFirmwareRev_Type())
invPhysFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysFirmwareRev.setStatus(_B)
_InvPhysProductDataRev_Type=SnmpAdminString
_InvPhysProductDataRev_Object=MibTableColumn
invPhysProductDataRev=_InvPhysProductDataRev_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,10),_InvPhysProductDataRev_Type())
invPhysProductDataRev.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysProductDataRev.setStatus(_B)
class _InvPhysSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_InvPhysSerialNum_Type.__name__=_r
_InvPhysSerialNum_Object=MibTableColumn
invPhysSerialNum=_InvPhysSerialNum_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,11),_InvPhysSerialNum_Type())
invPhysSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysSerialNum.setStatus(_B)
_InvPhysMfgName_Type=SnmpAdminString
_InvPhysMfgName_Object=MibTableColumn
invPhysMfgName=_InvPhysMfgName_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,12),_InvPhysMfgName_Type())
invPhysMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysMfgName.setStatus(_B)
_InvPhysModelName_Type=SnmpAdminString
_InvPhysModelName_Object=MibTableColumn
invPhysModelName=_InvPhysModelName_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,13),_InvPhysModelName_Type())
invPhysModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysModelName.setStatus(_B)
_InvPhysIsFRU_Type=TruthValue
_InvPhysIsFRU_Object=MibTableColumn
invPhysIsFRU=_InvPhysIsFRU_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,14),_InvPhysIsFRU_Type())
invPhysIsFRU.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysIsFRU.setStatus(_B)
_InvPhysSoftwareRev_Type=SnmpAdminString
_InvPhysSoftwareRev_Object=MibTableColumn
invPhysSoftwareRev=_InvPhysSoftwareRev_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,15),_InvPhysSoftwareRev_Type())
invPhysSoftwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysSoftwareRev.setStatus(_B)
_InvPhysSoftwareProduct_Type=SnmpAdminString
_InvPhysSoftwareProduct_Object=MibTableColumn
invPhysSoftwareProduct=_InvPhysSoftwareProduct_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,16),_InvPhysSoftwareProduct_Type())
invPhysSoftwareProduct.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysSoftwareProduct.setStatus(_B)
class _InvPhysClei_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_InvPhysClei_Type.__name__=_V
_InvPhysClei_Object=MibTableColumn
invPhysClei=_InvPhysClei_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,17),_InvPhysClei_Type())
invPhysClei.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysClei.setStatus(_B)
_InvPhysAid_Type=DisplayString
_InvPhysAid_Object=MibTableColumn
invPhysAid=_InvPhysAid_Object((1,3,6,1,4,1,8708,2,3,2,1,1,1,18),_InvPhysAid_Type())
invPhysAid.setMaxAccess(_C)
if mibBuilder.loadTexts:invPhysAid.setStatus(_B)
_InvGeneral_ObjectIdentity=ObjectIdentity
invGeneral=_InvGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2,2))
_InvGeneralLastChangeTime_Type=DateAndTime
_InvGeneralLastChangeTime_Object=MibScalar
invGeneralLastChangeTime=_InvGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,3,2,2,1),_InvGeneralLastChangeTime_Type())
invGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:invGeneralLastChangeTime.setStatus(_B)
_InvGeneralTestAndIncr_Type=TestAndIncr
_InvGeneralTestAndIncr_Object=MibScalar
invGeneralTestAndIncr=_InvGeneralTestAndIncr_Object((1,3,6,1,4,1,8708,2,3,2,2,2),_InvGeneralTestAndIncr_Type())
invGeneralTestAndIncr.setMaxAccess(_l)
if mibBuilder.loadTexts:invGeneralTestAndIncr.setStatus(_B)
class _InvGeneralMibSpecVersion_Type(DisplayString):defaultValue=OctetString('')
_InvGeneralMibSpecVersion_Type.__name__=_V
_InvGeneralMibSpecVersion_Object=MibScalar
invGeneralMibSpecVersion=_InvGeneralMibSpecVersion_Object((1,3,6,1,4,1,8708,2,3,2,2,3),_InvGeneralMibSpecVersion_Type())
invGeneralMibSpecVersion.setMaxAccess(_l)
if mibBuilder.loadTexts:invGeneralMibSpecVersion.setStatus(_B)
class _InvGeneralMibImplVersion_Type(DisplayString):defaultValue=OctetString('')
_InvGeneralMibImplVersion_Type.__name__=_V
_InvGeneralMibImplVersion_Object=MibScalar
invGeneralMibImplVersion=_InvGeneralMibImplVersion_Object((1,3,6,1,4,1,8708,2,3,2,2,4),_InvGeneralMibImplVersion_Type())
invGeneralMibImplVersion.setMaxAccess(_l)
if mibBuilder.loadTexts:invGeneralMibImplVersion.setStatus(_B)
_InvGeneralConfigLastChangeTime_Type=DateAndTime
_InvGeneralConfigLastChangeTime_Object=MibScalar
invGeneralConfigLastChangeTime=_InvGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,3,2,2,5),_InvGeneralConfigLastChangeTime_Type())
invGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:invGeneralConfigLastChangeTime.setStatus(_B)
_InvGeneralPhysTableSize_Type=Unsigned32
_InvGeneralPhysTableSize_Object=MibScalar
invGeneralPhysTableSize=_InvGeneralPhysTableSize_Object((1,3,6,1,4,1,8708,2,3,2,2,6),_InvGeneralPhysTableSize_Type())
invGeneralPhysTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:invGeneralPhysTableSize.setStatus(_B)
_InvGeneralEntityTableSize_Type=Unsigned32
_InvGeneralEntityTableSize_Object=MibScalar
invGeneralEntityTableSize=_InvGeneralEntityTableSize_Object((1,3,6,1,4,1,8708,2,3,2,2,7),_InvGeneralEntityTableSize_Type())
invGeneralEntityTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:invGeneralEntityTableSize.setStatus(_B)
_InvGeneralRelationTableSize_Type=Unsigned32
_InvGeneralRelationTableSize_Object=MibScalar
invGeneralRelationTableSize=_InvGeneralRelationTableSize_Object((1,3,6,1,4,1,8708,2,3,2,2,8),_InvGeneralRelationTableSize_Type())
invGeneralRelationTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:invGeneralRelationTableSize.setStatus(_B)
_InvGeneralInsRemTableSize_Type=Unsigned32
_InvGeneralInsRemTableSize_Object=MibScalar
invGeneralInsRemTableSize=_InvGeneralInsRemTableSize_Object((1,3,6,1,4,1,8708,2,3,2,2,9),_InvGeneralInsRemTableSize_Type())
invGeneralInsRemTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:invGeneralInsRemTableSize.setStatus(_B)
_InvGeneralInsRemLastSeqNumber_Type=Counter32
_InvGeneralInsRemLastSeqNumber_Object=MibScalar
invGeneralInsRemLastSeqNumber=_InvGeneralInsRemLastSeqNumber_Object((1,3,6,1,4,1,8708,2,3,2,2,10),_InvGeneralInsRemLastSeqNumber_Type())
invGeneralInsRemLastSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:invGeneralInsRemLastSeqNumber.setStatus(_B)
_LumentisInvNotifications_ObjectIdentity=ObjectIdentity
lumentisInvNotifications=_LumentisInvNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2,3))
_InvNotifyPrefix_ObjectIdentity=ObjectIdentity
invNotifyPrefix=_InvNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2,3,0))
_InvEntities_ObjectIdentity=ObjectIdentity
invEntities=_InvEntities_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2,4))
_InvEntityTable_Object=MibTable
invEntityTable=_InvEntityTable_Object((1,3,6,1,4,1,8708,2,3,2,4,1))
if mibBuilder.loadTexts:invEntityTable.setStatus(_B)
_InvEntityEntry_Object=MibTableRow
invEntityEntry=_InvEntityEntry_Object((1,3,6,1,4,1,8708,2,3,2,4,1,1))
invEntityEntry.setIndexNames((0,_A,_m))
if mibBuilder.loadTexts:invEntityEntry.setStatus(_B)
class _InvEntityIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InvEntityIndex_Type.__name__=_I
_InvEntityIndex_Object=MibTableColumn
invEntityIndex=_InvEntityIndex_Object((1,3,6,1,4,1,8708,2,3,2,4,1,1,1),_InvEntityIndex_Type())
invEntityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:invEntityIndex.setStatus(_B)
_InvEntityName_Type=MgmtNameString
_InvEntityName_Object=MibTableColumn
invEntityName=_InvEntityName_Object((1,3,6,1,4,1,8708,2,3,2,4,1,1,2),_InvEntityName_Type())
invEntityName.setMaxAccess(_C)
if mibBuilder.loadTexts:invEntityName.setStatus(_B)
_InvEntityObject_Type=RowPointer
_InvEntityObject_Object=MibTableColumn
invEntityObject=_InvEntityObject_Object((1,3,6,1,4,1,8708,2,3,2,4,1,1,3),_InvEntityObject_Type())
invEntityObject.setMaxAccess(_C)
if mibBuilder.loadTexts:invEntityObject.setStatus(_B)
_InvEntityClass_Type=EntityClass
_InvEntityClass_Object=MibTableColumn
invEntityClass=_InvEntityClass_Object((1,3,6,1,4,1,8708,2,3,2,4,1,1,4),_InvEntityClass_Type())
invEntityClass.setMaxAccess(_C)
if mibBuilder.loadTexts:invEntityClass.setStatus(_B)
_InvRelations_ObjectIdentity=ObjectIdentity
invRelations=_InvRelations_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2,5))
_InvRelationTable_Object=MibTable
invRelationTable=_InvRelationTable_Object((1,3,6,1,4,1,8708,2,3,2,5,1))
if mibBuilder.loadTexts:invRelationTable.setStatus(_B)
_InvRelationEntry_Object=MibTableRow
invRelationEntry=_InvRelationEntry_Object((1,3,6,1,4,1,8708,2,3,2,5,1,1))
invRelationEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:invRelationEntry.setStatus(_B)
class _InvRelationIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InvRelationIndex_Type.__name__=_I
_InvRelationIndex_Object=MibTableColumn
invRelationIndex=_InvRelationIndex_Object((1,3,6,1,4,1,8708,2,3,2,5,1,1,1),_InvRelationIndex_Type())
invRelationIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:invRelationIndex.setStatus(_B)
class _InvRelationEntityIndex1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InvRelationEntityIndex1_Type.__name__=_I
_InvRelationEntityIndex1_Object=MibTableColumn
invRelationEntityIndex1=_InvRelationEntityIndex1_Object((1,3,6,1,4,1,8708,2,3,2,5,1,1,2),_InvRelationEntityIndex1_Type())
invRelationEntityIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:invRelationEntityIndex1.setStatus(_B)
_InvRelationEntityName1_Type=MgmtNameString
_InvRelationEntityName1_Object=MibTableColumn
invRelationEntityName1=_InvRelationEntityName1_Object((1,3,6,1,4,1,8708,2,3,2,5,1,1,3),_InvRelationEntityName1_Type())
invRelationEntityName1.setMaxAccess(_C)
if mibBuilder.loadTexts:invRelationEntityName1.setStatus(_B)
class _InvRelationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_k,0),('containedIn',1),('dependsOn',2)))
_InvRelationType_Type.__name__=_j
_InvRelationType_Object=MibTableColumn
invRelationType=_InvRelationType_Object((1,3,6,1,4,1,8708,2,3,2,5,1,1,4),_InvRelationType_Type())
invRelationType.setMaxAccess(_C)
if mibBuilder.loadTexts:invRelationType.setStatus(_B)
class _InvRelationEntityIndex2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InvRelationEntityIndex2_Type.__name__=_I
_InvRelationEntityIndex2_Object=MibTableColumn
invRelationEntityIndex2=_InvRelationEntityIndex2_Object((1,3,6,1,4,1,8708,2,3,2,5,1,1,5),_InvRelationEntityIndex2_Type())
invRelationEntityIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:invRelationEntityIndex2.setStatus(_B)
_InvRelationEntityName2_Type=MgmtNameString
_InvRelationEntityName2_Object=MibTableColumn
invRelationEntityName2=_InvRelationEntityName2_Object((1,3,6,1,4,1,8708,2,3,2,5,1,1,6),_InvRelationEntityName2_Type())
invRelationEntityName2.setMaxAccess(_C)
if mibBuilder.loadTexts:invRelationEntityName2.setStatus(_B)
_InvInsRemLog_ObjectIdentity=ObjectIdentity
invInsRemLog=_InvInsRemLog_ObjectIdentity((1,3,6,1,4,1,8708,2,3,2,6))
_InvInsRemTable_Object=MibTable
invInsRemTable=_InvInsRemTable_Object((1,3,6,1,4,1,8708,2,3,2,6,1))
if mibBuilder.loadTexts:invInsRemTable.setStatus(_B)
_InvInsRemEntry_Object=MibTableRow
invInsRemEntry=_InvInsRemEntry_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1))
invInsRemEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:invInsRemEntry.setStatus(_B)
class _InvInsRemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InvInsRemIndex_Type.__name__=_I
_InvInsRemIndex_Object=MibTableColumn
invInsRemIndex=_InvInsRemIndex_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,1),_InvInsRemIndex_Type())
invInsRemIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemIndex.setStatus(_B)
_InvInsRemName_Type=MgmtNameString
_InvInsRemName_Object=MibTableColumn
invInsRemName=_InvInsRemName_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,2),_InvInsRemName_Type())
invInsRemName.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemName.setStatus(_B)
_InvInsRemEvent_Type=InsRemEventType
_InvInsRemEvent_Object=MibTableColumn
invInsRemEvent=_InvInsRemEvent_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,3),_InvInsRemEvent_Type())
invInsRemEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemEvent.setStatus(_B)
_InvInsRemTimestamp_Type=DateAndTime
_InvInsRemTimestamp_Object=MibTableColumn
invInsRemTimestamp=_InvInsRemTimestamp_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,4),_InvInsRemTimestamp_Type())
invInsRemTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemTimestamp.setStatus(_B)
_InvInsRemEquipmentType_Type=PhysicalClass
_InvInsRemEquipmentType_Object=MibTableColumn
invInsRemEquipmentType=_InvInsRemEquipmentType_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,5),_InvInsRemEquipmentType_Type())
invInsRemEquipmentType.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemEquipmentType.setStatus(_B)
class _InvInsRemPhysicalLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InvInsRemPhysicalLocation_Type.__name__=_V
_InvInsRemPhysicalLocation_Object=MibTableColumn
invInsRemPhysicalLocation=_InvInsRemPhysicalLocation_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,6),_InvInsRemPhysicalLocation_Type())
invInsRemPhysicalLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemPhysicalLocation.setStatus(_B)
class _InvInsRemClei_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_InvInsRemClei_Type.__name__=_V
_InvInsRemClei_Object=MibTableColumn
invInsRemClei=_InvInsRemClei_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,7),_InvInsRemClei_Type())
invInsRemClei.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemClei.setStatus(_B)
class _InvInsRemSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_InvInsRemSerialNumber_Type.__name__=_V
_InvInsRemSerialNumber_Object=MibTableColumn
invInsRemSerialNumber=_InvInsRemSerialNumber_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,8),_InvInsRemSerialNumber_Type())
invInsRemSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemSerialNumber.setStatus(_B)
_InvInsRemPartNumber_Type=DisplayString
_InvInsRemPartNumber_Object=MibTableColumn
invInsRemPartNumber=_InvInsRemPartNumber_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,9),_InvInsRemPartNumber_Type())
invInsRemPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemPartNumber.setStatus(_B)
_InvInsRemSeqNumber_Type=Counter32
_InvInsRemSeqNumber_Object=MibTableColumn
invInsRemSeqNumber=_InvInsRemSeqNumber_Object((1,3,6,1,4,1,8708,2,3,2,6,1,1,10),_InvInsRemSeqNumber_Type())
invInsRemSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:invInsRemSeqNumber.setStatus(_B)
invPhysGroup=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,1))
invPhysGroup.setObjects(*((_A,_H),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:invPhysGroup.setStatus(_D)
invGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,2))
invGeneralGroup.setObjects(*((_A,_W),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:invGeneralGroup.setStatus(_D)
invGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,4))
invGeneralGroupV2.setObjects((_A,_W))
if mibBuilder.loadTexts:invGeneralGroupV2.setStatus(_D)
invPhysGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,5))
invPhysGroupV2.setObjects(*((_A,_H),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Z)))
if mibBuilder.loadTexts:invPhysGroupV2.setStatus(_D)
invPhysGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,6))
invPhysGroupV3.setObjects(*((_A,_H),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Z),(_A,_c)))
if mibBuilder.loadTexts:invPhysGroupV3.setStatus(_D)
invEntityGroup=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,7))
invEntityGroup.setObjects(*((_A,_m),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:invEntityGroup.setStatus(_B)
invRelationGroup=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,8))
invRelationGroup.setObjects(*((_A,_n),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:invRelationGroup.setStatus(_B)
invGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,9))
invGeneralGroupV3.setObjects(*((_A,_W),(_A,_a)))
if mibBuilder.loadTexts:invGeneralGroupV3.setStatus(_D)
invGeneralGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,10))
invGeneralGroupV4.setObjects(*((_A,_W),(_A,_a),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:invGeneralGroupV4.setStatus(_D)
invPhysGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,11))
invPhysGroupV4.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Z),(_A,_c)))
if mibBuilder.loadTexts:invPhysGroupV4.setStatus(_D)
invPhysGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,12))
invPhysGroupV5.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Z),(_A,_c),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:invPhysGroupV5.setStatus(_B)
invInsRemGroup=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,13))
invInsRemGroup.setObjects(*((_A,_o),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:invInsRemGroup.setStatus(_B)
invGeneralGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,1,14))
invGeneralGroupV5.setObjects(*((_A,_W),(_A,_a),(_A,_d),(_A,_e),(_A,_f),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:invGeneralGroupV5.setStatus(_B)
inventoryGeneralMinimalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,3,1,3,1))
inventoryGeneralMinimalGroupV1.setObjects(*((_A,_W),(_A,_a),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:inventoryGeneralMinimalGroupV1.setStatus(_B)
invNotificationPhysAdded=NotificationType((1,3,6,1,4,1,8708,2,3,2,3,0,1))
invNotificationPhysAdded.setObjects(*((_A,_H),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:invNotificationPhysAdded.setStatus(_B)
invNotificationPhysRemoved=NotificationType((1,3,6,1,4,1,8708,2,3,2,3,0,2))
invNotificationPhysRemoved.setObjects(*((_A,_H),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:invNotificationPhysRemoved.setStatus(_B)
invEventGroup=NotificationGroup((1,3,6,1,4,1,8708,2,3,1,1,3))
invEventGroup.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:invEventGroup.setStatus(_B)
lumInventoryBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,1))
lumInventoryBasicComplV1.setObjects(*((_A,_p),(_A,_AP),(_A,_E)))
if mibBuilder.loadTexts:lumInventoryBasicComplV1.setStatus(_D)
lumInventoryBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,2))
lumInventoryBasicComplV2.setObjects(*((_A,_b),(_A,_p),(_A,_E)))
if mibBuilder.loadTexts:lumInventoryBasicComplV2.setStatus(_D)
lumInventoryBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,3))
lumInventoryBasicComplV3.setObjects(*((_A,_b),(_A,_AQ),(_A,_E)))
if mibBuilder.loadTexts:lumInventoryBasicComplV3.setStatus(_D)
lumInventoryBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,4))
lumInventoryBasicComplV4.setObjects(*((_A,_b),(_A,_Y),(_A,_E)))
if mibBuilder.loadTexts:lumInventoryBasicComplV4.setStatus(_D)
lumInventoryBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,5))
lumInventoryBasicComplV5.setObjects(*((_A,_b),(_A,_Y),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryBasicComplV5.setStatus(_D)
lumInventoryBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,6))
lumInventoryBasicComplV6.setObjects(*((_A,_AR),(_A,_Y),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryBasicComplV6.setStatus(_D)
lumInventoryBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,7))
lumInventoryBasicComplV7.setObjects(*((_A,_g),(_A,_Y),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryBasicComplV7.setStatus(_D)
lumInventoryBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,8))
lumInventoryBasicComplV8.setObjects(*((_A,_g),(_A,_q),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryBasicComplV8.setStatus(_D)
lumInventoryBasicComplV9=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,9))
lumInventoryBasicComplV9.setObjects(*((_A,_g),(_A,_h),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryBasicComplV9.setStatus(_D)
lumInventoryBasicComplV10=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,2,10))
lumInventoryBasicComplV10.setObjects(*((_A,_AS),(_A,_h),(_A,_E),(_A,_F),(_A,_G),(_A,_AT)))
if mibBuilder.loadTexts:lumInventoryBasicComplV10.setStatus(_B)
lumInventoryMinimalComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,4,1))
lumInventoryMinimalComplV1.setObjects(*((_A,_i),(_A,_Y),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryMinimalComplV1.setStatus(_D)
lumInventoryMinimalComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,4,2))
lumInventoryMinimalComplV2.setObjects(*((_A,_i),(_A,_q),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryMinimalComplV2.setStatus(_D)
lumInventoryMinimalComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,3,1,4,3))
lumInventoryMinimalComplV3.setObjects(*((_A,_i),(_A,_h),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:lumInventoryMinimalComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PhysicalClass':PhysicalClass,'EntityClass':EntityClass,'InsRemEventType':InsRemEventType,'lumInventoryMIBModule':lumInventoryMIBModule,'lumInventoryConfs':lumInventoryConfs,'lumInventoryGroups':lumInventoryGroups,_p:invPhysGroup,_AP:invGeneralGroup,_E:invEventGroup,_b:invGeneralGroupV2,_AQ:invPhysGroupV2,_Y:invPhysGroupV3,_F:invEntityGroup,_G:invRelationGroup,_AR:invGeneralGroupV3,_g:invGeneralGroupV4,_q:invPhysGroupV4,_h:invPhysGroupV5,_AT:invInsRemGroup,_AS:invGeneralGroupV5,'lumInventoryCompl':lumInventoryCompl,'lumInventoryBasicComplV1':lumInventoryBasicComplV1,'lumInventoryBasicComplV2':lumInventoryBasicComplV2,'lumInventoryBasicComplV3':lumInventoryBasicComplV3,'lumInventoryBasicComplV4':lumInventoryBasicComplV4,'lumInventoryBasicComplV5':lumInventoryBasicComplV5,'lumInventoryBasicComplV6':lumInventoryBasicComplV6,'lumInventoryBasicComplV7':lumInventoryBasicComplV7,'lumInventoryBasicComplV8':lumInventoryBasicComplV8,'lumInventoryBasicComplV9':lumInventoryBasicComplV9,'lumInventoryBasicComplV10':lumInventoryBasicComplV10,'lumInventoryMinimalGroups':lumInventoryMinimalGroups,_i:inventoryGeneralMinimalGroupV1,'lumInventoryMinimalCompl':lumInventoryMinimalCompl,'lumInventoryMinimalComplV1':lumInventoryMinimalComplV1,'lumInventoryMinimalComplV2':lumInventoryMinimalComplV2,'lumInventoryMinimalComplV3':lumInventoryMinimalComplV3,'lumInventoryMIBObjects':lumInventoryMIBObjects,'invPhysical':invPhysical,'invPhysTable':invPhysTable,'invPhysEntry':invPhysEntry,_H:invPhysIndex,_J:invPhysDescr,_X:invPhysVendorType,_K:invPhysContainedIn,_L:invPhysClass,_M:invPhysParentRelPos,_N:invPhysName,_O:invPhysHardwareRev,_P:invPhysFirmwareRev,_Q:invPhysProductDataRev,_R:invPhysSerialNum,_S:invPhysMfgName,_T:invPhysModelName,_U:invPhysIsFRU,_Z:invPhysSoftwareRev,_c:invPhysSoftwareProduct,_AA:invPhysClei,_AB:invPhysAid,'invGeneral':invGeneral,_W:invGeneralLastChangeTime,_A1:invGeneralTestAndIncr,_z:invGeneralMibSpecVersion,_A0:invGeneralMibImplVersion,_a:invGeneralConfigLastChangeTime,_d:invGeneralPhysTableSize,_e:invGeneralEntityTableSize,_f:invGeneralRelationTableSize,_AL:invGeneralInsRemTableSize,_AM:invGeneralInsRemLastSeqNumber,'lumentisInvNotifications':lumentisInvNotifications,'invNotifyPrefix':invNotifyPrefix,_AN:invNotificationPhysAdded,_AO:invNotificationPhysRemoved,'invEntities':invEntities,'invEntityTable':invEntityTable,'invEntityEntry':invEntityEntry,_m:invEntityIndex,_A2:invEntityName,_A3:invEntityObject,_A4:invEntityClass,'invRelations':invRelations,'invRelationTable':invRelationTable,'invRelationEntry':invRelationEntry,_n:invRelationIndex,_A5:invRelationEntityIndex1,_A6:invRelationEntityName1,_A7:invRelationType,_A8:invRelationEntityIndex2,_A9:invRelationEntityName2,'invInsRemLog':invInsRemLog,'invInsRemTable':invInsRemTable,'invInsRemEntry':invInsRemEntry,_o:invInsRemIndex,_AC:invInsRemName,_AD:invInsRemEvent,_AE:invInsRemTimestamp,_AF:invInsRemEquipmentType,_AG:invInsRemPhysicalLocation,_AH:invInsRemClei,_AI:invInsRemSerialNumber,_AJ:invInsRemPartNumber,_AK:invInsRemSeqNumber})