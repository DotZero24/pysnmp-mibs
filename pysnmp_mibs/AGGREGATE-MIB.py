_Y='aggrMibBasicGroup'
_X='aggrDataErrorRecord'
_W='aggrDataRecordCompressed'
_V='aggrDataRecord'
_U='aggrMOEntryStatus'
_T='aggrMOEntryStorageType'
_S='aggrMODescr'
_R='aggrMOInstance'
_Q='aggrCtlEntryStatus'
_P='aggrCtlEntryStorageType'
_O='aggrCtlEntryOwner'
_N='aggrCtlCompressionAlgorithm'
_M='aggrCtlMODescr'
_L='aggrCtlMOIndex'
_K='aggrMOEntryMOID'
_J='aggrMOEntryID'
_I='Integer32'
_H='read-only'
_G='not-accessible'
_F='aggrCtlEntryID'
_E='Unsigned32'
_D='SnmpAdminString'
_C='read-create'
_B='AGGREGATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OwnerString,=mibBuilder.importSymbols('RMON-MIB','OwnerString')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks',_E,'experimental','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
aggrMIB=ModuleIdentity((1,3,6,1,3,123))
if mibBuilder.loadTexts:aggrMIB.setRevisions(('2006-04-27 00:00',))
class AggrMOErrorStatus(TextualConvention,Opaque):status=_A;subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
class AggrMOValue(TextualConvention,Opaque):status=_A;subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
class AggrMOCompressedValue(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_AggrCtlTable_Object=MibTable
aggrCtlTable=_AggrCtlTable_Object((1,3,6,1,3,123,1))
if mibBuilder.loadTexts:aggrCtlTable.setStatus(_A)
_AggrCtlEntry_Object=MibTableRow
aggrCtlEntry=_AggrCtlEntry_Object((1,3,6,1,3,123,1,1))
aggrCtlEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:aggrCtlEntry.setStatus(_A)
class _AggrCtlEntryID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AggrCtlEntryID_Type.__name__=_D
_AggrCtlEntryID_Object=MibTableColumn
aggrCtlEntryID=_AggrCtlEntryID_Object((1,3,6,1,3,123,1,1,1),_AggrCtlEntryID_Type())
aggrCtlEntryID.setMaxAccess(_G)
if mibBuilder.loadTexts:aggrCtlEntryID.setStatus(_A)
class _AggrCtlMOIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AggrCtlMOIndex_Type.__name__=_E
_AggrCtlMOIndex_Object=MibTableColumn
aggrCtlMOIndex=_AggrCtlMOIndex_Object((1,3,6,1,3,123,1,1,2),_AggrCtlMOIndex_Type())
aggrCtlMOIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrCtlMOIndex.setStatus(_A)
class _AggrCtlMODescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AggrCtlMODescr_Type.__name__=_D
_AggrCtlMODescr_Object=MibTableColumn
aggrCtlMODescr=_AggrCtlMODescr_Object((1,3,6,1,3,123,1,1,3),_AggrCtlMODescr_Type())
aggrCtlMODescr.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrCtlMODescr.setStatus(_A)
class _AggrCtlCompressionAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('deflate',2)))
_AggrCtlCompressionAlgorithm_Type.__name__=_I
_AggrCtlCompressionAlgorithm_Object=MibTableColumn
aggrCtlCompressionAlgorithm=_AggrCtlCompressionAlgorithm_Object((1,3,6,1,3,123,1,1,4),_AggrCtlCompressionAlgorithm_Type())
aggrCtlCompressionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrCtlCompressionAlgorithm.setStatus(_A)
_AggrCtlEntryOwner_Type=OwnerString
_AggrCtlEntryOwner_Object=MibTableColumn
aggrCtlEntryOwner=_AggrCtlEntryOwner_Object((1,3,6,1,3,123,1,1,5),_AggrCtlEntryOwner_Type())
aggrCtlEntryOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrCtlEntryOwner.setStatus(_A)
_AggrCtlEntryStorageType_Type=StorageType
_AggrCtlEntryStorageType_Object=MibTableColumn
aggrCtlEntryStorageType=_AggrCtlEntryStorageType_Object((1,3,6,1,3,123,1,1,6),_AggrCtlEntryStorageType_Type())
aggrCtlEntryStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrCtlEntryStorageType.setStatus(_A)
_AggrCtlEntryStatus_Type=RowStatus
_AggrCtlEntryStatus_Object=MibTableColumn
aggrCtlEntryStatus=_AggrCtlEntryStatus_Object((1,3,6,1,3,123,1,1,7),_AggrCtlEntryStatus_Type())
aggrCtlEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrCtlEntryStatus.setStatus(_A)
_AggrMOTable_Object=MibTable
aggrMOTable=_AggrMOTable_Object((1,3,6,1,3,123,2))
if mibBuilder.loadTexts:aggrMOTable.setStatus(_A)
_AggrMOEntry_Object=MibTableRow
aggrMOEntry=_AggrMOEntry_Object((1,3,6,1,3,123,2,1))
aggrMOEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:aggrMOEntry.setStatus(_A)
class _AggrMOEntryID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AggrMOEntryID_Type.__name__=_E
_AggrMOEntryID_Object=MibTableColumn
aggrMOEntryID=_AggrMOEntryID_Object((1,3,6,1,3,123,2,1,1),_AggrMOEntryID_Type())
aggrMOEntryID.setMaxAccess(_G)
if mibBuilder.loadTexts:aggrMOEntryID.setStatus(_A)
class _AggrMOEntryMOID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AggrMOEntryMOID_Type.__name__=_E
_AggrMOEntryMOID_Object=MibTableColumn
aggrMOEntryMOID=_AggrMOEntryMOID_Object((1,3,6,1,3,123,2,1,2),_AggrMOEntryMOID_Type())
aggrMOEntryMOID.setMaxAccess(_G)
if mibBuilder.loadTexts:aggrMOEntryMOID.setStatus(_A)
_AggrMOInstance_Type=ObjectIdentifier
_AggrMOInstance_Object=MibTableColumn
aggrMOInstance=_AggrMOInstance_Object((1,3,6,1,3,123,2,1,3),_AggrMOInstance_Type())
aggrMOInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrMOInstance.setStatus(_A)
class _AggrMODescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AggrMODescr_Type.__name__=_D
_AggrMODescr_Object=MibTableColumn
aggrMODescr=_AggrMODescr_Object((1,3,6,1,3,123,2,1,4),_AggrMODescr_Type())
aggrMODescr.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrMODescr.setStatus(_A)
_AggrMOEntryStorageType_Type=StorageType
_AggrMOEntryStorageType_Object=MibTableColumn
aggrMOEntryStorageType=_AggrMOEntryStorageType_Object((1,3,6,1,3,123,2,1,5),_AggrMOEntryStorageType_Type())
aggrMOEntryStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrMOEntryStorageType.setStatus(_A)
_AggrMOEntryStatus_Type=RowStatus
_AggrMOEntryStatus_Object=MibTableColumn
aggrMOEntryStatus=_AggrMOEntryStatus_Object((1,3,6,1,3,123,2,1,6),_AggrMOEntryStatus_Type())
aggrMOEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aggrMOEntryStatus.setStatus(_A)
_AggrDataTable_Object=MibTable
aggrDataTable=_AggrDataTable_Object((1,3,6,1,3,123,3))
if mibBuilder.loadTexts:aggrDataTable.setStatus(_A)
_AggrDataEntry_Object=MibTableRow
aggrDataEntry=_AggrDataEntry_Object((1,3,6,1,3,123,3,1))
aggrDataEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:aggrDataEntry.setStatus(_A)
_AggrDataRecord_Type=AggrMOValue
_AggrDataRecord_Object=MibTableColumn
aggrDataRecord=_AggrDataRecord_Object((1,3,6,1,3,123,3,1,1),_AggrDataRecord_Type())
aggrDataRecord.setMaxAccess(_H)
if mibBuilder.loadTexts:aggrDataRecord.setStatus(_A)
_AggrDataRecordCompressed_Type=AggrMOCompressedValue
_AggrDataRecordCompressed_Object=MibTableColumn
aggrDataRecordCompressed=_AggrDataRecordCompressed_Object((1,3,6,1,3,123,3,1,2),_AggrDataRecordCompressed_Type())
aggrDataRecordCompressed.setMaxAccess(_H)
if mibBuilder.loadTexts:aggrDataRecordCompressed.setStatus(_A)
_AggrDataErrorRecord_Type=AggrMOErrorStatus
_AggrDataErrorRecord_Object=MibTableColumn
aggrDataErrorRecord=_AggrDataErrorRecord_Object((1,3,6,1,3,123,3,1,3),_AggrDataErrorRecord_Type())
aggrDataErrorRecord.setMaxAccess(_H)
if mibBuilder.loadTexts:aggrDataErrorRecord.setStatus(_A)
_AggrConformance_ObjectIdentity=ObjectIdentity
aggrConformance=_AggrConformance_ObjectIdentity((1,3,6,1,3,123,4))
_AggrGroups_ObjectIdentity=ObjectIdentity
aggrGroups=_AggrGroups_ObjectIdentity((1,3,6,1,3,123,4,1))
_AggrCompliances_ObjectIdentity=ObjectIdentity
aggrCompliances=_AggrCompliances_ObjectIdentity((1,3,6,1,3,123,4,2))
aggrMibBasicGroup=ObjectGroup((1,3,6,1,3,123,4,1,1))
aggrMibBasicGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:aggrMibBasicGroup.setStatus(_A)
aggrMibCompliance=ModuleCompliance((1,3,6,1,3,123,4,2,1))
aggrMibCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:aggrMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AggrMOErrorStatus':AggrMOErrorStatus,'AggrMOValue':AggrMOValue,'AggrMOCompressedValue':AggrMOCompressedValue,'aggrMIB':aggrMIB,'aggrCtlTable':aggrCtlTable,'aggrCtlEntry':aggrCtlEntry,_F:aggrCtlEntryID,_L:aggrCtlMOIndex,_M:aggrCtlMODescr,_N:aggrCtlCompressionAlgorithm,_O:aggrCtlEntryOwner,_P:aggrCtlEntryStorageType,_Q:aggrCtlEntryStatus,'aggrMOTable':aggrMOTable,'aggrMOEntry':aggrMOEntry,_J:aggrMOEntryID,_K:aggrMOEntryMOID,_R:aggrMOInstance,_S:aggrMODescr,_T:aggrMOEntryStorageType,_U:aggrMOEntryStatus,'aggrDataTable':aggrDataTable,'aggrDataEntry':aggrDataEntry,_V:aggrDataRecord,_W:aggrDataRecordCompressed,_X:aggrDataErrorRecord,'aggrConformance':aggrConformance,'aggrGroups':aggrGroups,_Y:aggrMibBasicGroup,'aggrCompliances':aggrCompliances,'aggrMibCompliance':aggrMibCompliance})