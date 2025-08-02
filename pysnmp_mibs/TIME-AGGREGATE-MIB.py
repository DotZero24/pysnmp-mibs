_S='tAggrMibBasicGroup'
_R='tAggrDataErrorRecord'
_Q='tAggrDataRecordCompressed'
_P='tAggrDataRecord'
_O='tAggrCtlEntryStatus'
_N='tAggrCtlEntryStorageType'
_M='tAggrCtlEntryOwner'
_L='tAggrCtlCompressionAlgorithm'
_K='tAggrCtlSamples'
_J='tAggrCtlInterval'
_I='tAggrCtlAgMODescr'
_H='tAggrCtlMOInstance'
_G='Integer32'
_F='read-only'
_E='tAggrCtlEntryID'
_D='SnmpAdminString'
_C='read-create'
_B='TIME-AGGREGATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OwnerString,=mibBuilder.importSymbols('RMON-MIB','OwnerString')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
tAggrMIB=ModuleIdentity((1,3,6,1,3,124))
if mibBuilder.loadTexts:tAggrMIB.setRevisions(('2006-04-27 00:00',))
class TAggrMOErrorStatus(TextualConvention,Opaque):status=_A;subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
class TimeAggrMOValue(TextualConvention,Opaque):status=_A;subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
class CompressedTimeAggrMOValue(TextualConvention,Opaque):status=_A;subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_TAggrCtlTable_Object=MibTable
tAggrCtlTable=_TAggrCtlTable_Object((1,3,6,1,3,124,1))
if mibBuilder.loadTexts:tAggrCtlTable.setStatus(_A)
_TAggrCtlEntry_Object=MibTableRow
tAggrCtlEntry=_TAggrCtlEntry_Object((1,3,6,1,3,124,1,1))
tAggrCtlEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:tAggrCtlEntry.setStatus(_A)
class _TAggrCtlEntryID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TAggrCtlEntryID_Type.__name__=_D
_TAggrCtlEntryID_Object=MibTableColumn
tAggrCtlEntryID=_TAggrCtlEntryID_Object((1,3,6,1,3,124,1,1,1),_TAggrCtlEntryID_Type())
tAggrCtlEntryID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tAggrCtlEntryID.setStatus(_A)
_TAggrCtlMOInstance_Type=ObjectIdentifier
_TAggrCtlMOInstance_Object=MibTableColumn
tAggrCtlMOInstance=_TAggrCtlMOInstance_Object((1,3,6,1,3,124,1,1,2),_TAggrCtlMOInstance_Type())
tAggrCtlMOInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlMOInstance.setStatus(_A)
class _TAggrCtlAgMODescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TAggrCtlAgMODescr_Type.__name__=_D
_TAggrCtlAgMODescr_Object=MibTableColumn
tAggrCtlAgMODescr=_TAggrCtlAgMODescr_Object((1,3,6,1,3,124,1,1,3),_TAggrCtlAgMODescr_Type())
tAggrCtlAgMODescr.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlAgMODescr.setStatus(_A)
_TAggrCtlInterval_Type=Integer32
_TAggrCtlInterval_Object=MibTableColumn
tAggrCtlInterval=_TAggrCtlInterval_Object((1,3,6,1,3,124,1,1,4),_TAggrCtlInterval_Type())
tAggrCtlInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlInterval.setStatus(_A)
if mibBuilder.loadTexts:tAggrCtlInterval.setUnits('micro seconds')
_TAggrCtlSamples_Type=Integer32
_TAggrCtlSamples_Object=MibTableColumn
tAggrCtlSamples=_TAggrCtlSamples_Object((1,3,6,1,3,124,1,1,5),_TAggrCtlSamples_Type())
tAggrCtlSamples.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlSamples.setStatus(_A)
class _TAggrCtlCompressionAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('deflate',2)))
_TAggrCtlCompressionAlgorithm_Type.__name__=_G
_TAggrCtlCompressionAlgorithm_Object=MibTableColumn
tAggrCtlCompressionAlgorithm=_TAggrCtlCompressionAlgorithm_Object((1,3,6,1,3,124,1,1,6),_TAggrCtlCompressionAlgorithm_Type())
tAggrCtlCompressionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlCompressionAlgorithm.setStatus(_A)
_TAggrCtlEntryOwner_Type=OwnerString
_TAggrCtlEntryOwner_Object=MibTableColumn
tAggrCtlEntryOwner=_TAggrCtlEntryOwner_Object((1,3,6,1,3,124,1,1,7),_TAggrCtlEntryOwner_Type())
tAggrCtlEntryOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlEntryOwner.setStatus(_A)
_TAggrCtlEntryStorageType_Type=StorageType
_TAggrCtlEntryStorageType_Object=MibTableColumn
tAggrCtlEntryStorageType=_TAggrCtlEntryStorageType_Object((1,3,6,1,3,124,1,1,8),_TAggrCtlEntryStorageType_Type())
tAggrCtlEntryStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlEntryStorageType.setStatus(_A)
_TAggrCtlEntryStatus_Type=RowStatus
_TAggrCtlEntryStatus_Object=MibTableColumn
tAggrCtlEntryStatus=_TAggrCtlEntryStatus_Object((1,3,6,1,3,124,1,1,9),_TAggrCtlEntryStatus_Type())
tAggrCtlEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tAggrCtlEntryStatus.setStatus(_A)
_TAggrDataTable_Object=MibTable
tAggrDataTable=_TAggrDataTable_Object((1,3,6,1,3,124,2))
if mibBuilder.loadTexts:tAggrDataTable.setStatus(_A)
_TAggrDataEntry_Object=MibTableRow
tAggrDataEntry=_TAggrDataEntry_Object((1,3,6,1,3,124,2,1))
tAggrDataEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:tAggrDataEntry.setStatus(_A)
_TAggrDataRecord_Type=TimeAggrMOValue
_TAggrDataRecord_Object=MibTableColumn
tAggrDataRecord=_TAggrDataRecord_Object((1,3,6,1,3,124,2,1,1),_TAggrDataRecord_Type())
tAggrDataRecord.setMaxAccess(_F)
if mibBuilder.loadTexts:tAggrDataRecord.setStatus(_A)
_TAggrDataRecordCompressed_Type=CompressedTimeAggrMOValue
_TAggrDataRecordCompressed_Object=MibTableColumn
tAggrDataRecordCompressed=_TAggrDataRecordCompressed_Object((1,3,6,1,3,124,2,1,2),_TAggrDataRecordCompressed_Type())
tAggrDataRecordCompressed.setMaxAccess(_F)
if mibBuilder.loadTexts:tAggrDataRecordCompressed.setStatus(_A)
_TAggrDataErrorRecord_Type=TAggrMOErrorStatus
_TAggrDataErrorRecord_Object=MibTableColumn
tAggrDataErrorRecord=_TAggrDataErrorRecord_Object((1,3,6,1,3,124,2,1,3),_TAggrDataErrorRecord_Type())
tAggrDataErrorRecord.setMaxAccess(_F)
if mibBuilder.loadTexts:tAggrDataErrorRecord.setStatus(_A)
_TAggrConformance_ObjectIdentity=ObjectIdentity
tAggrConformance=_TAggrConformance_ObjectIdentity((1,3,6,1,3,124,3))
_TAggrGroups_ObjectIdentity=ObjectIdentity
tAggrGroups=_TAggrGroups_ObjectIdentity((1,3,6,1,3,124,3,1))
_TAggrCompliances_ObjectIdentity=ObjectIdentity
tAggrCompliances=_TAggrCompliances_ObjectIdentity((1,3,6,1,3,124,3,2))
tAggrMibBasicGroup=ObjectGroup((1,3,6,1,3,124,3,1,1))
tAggrMibBasicGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:tAggrMibBasicGroup.setStatus(_A)
tAggrMibCompliance=ModuleCompliance((1,3,6,1,3,124,3,2,1))
tAggrMibCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:tAggrMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TAggrMOErrorStatus':TAggrMOErrorStatus,'TimeAggrMOValue':TimeAggrMOValue,'CompressedTimeAggrMOValue':CompressedTimeAggrMOValue,'tAggrMIB':tAggrMIB,'tAggrCtlTable':tAggrCtlTable,'tAggrCtlEntry':tAggrCtlEntry,_E:tAggrCtlEntryID,_H:tAggrCtlMOInstance,_I:tAggrCtlAgMODescr,_J:tAggrCtlInterval,_K:tAggrCtlSamples,_L:tAggrCtlCompressionAlgorithm,_M:tAggrCtlEntryOwner,_N:tAggrCtlEntryStorageType,_O:tAggrCtlEntryStatus,'tAggrDataTable':tAggrDataTable,'tAggrDataEntry':tAggrDataEntry,_P:tAggrDataRecord,_Q:tAggrDataRecordCompressed,_R:tAggrDataErrorRecord,'tAggrConformance':tAggrConformance,'tAggrGroups':tAggrGroups,_S:tAggrMibBasicGroup,'tAggrCompliances':tAggrCompliances,'tAggrMibCompliance':tAggrMibCompliance})