_X='lookupResultsAddress'
_W='lookupResultsAddressType'
_V='lookupCtlRowStatus'
_U='lookupCtlRc'
_T='lookupCtlTime'
_S='lookupCtlTargetAddress'
_R='lookupCtlTargetAddressType'
_Q='lookupCtlOperStatus'
_P='lookupPurgeTime'
_O='lookupMaxConcurrentRequests'
_N='lookupResultsIndex'
_M='read-write'
_L='Integer32'
_K='InetAddressType'
_J='lookupGroup'
_I='read-create'
_H='not-accessible'
_G='lookupCtlOperationName'
_F='lookupCtlOwnerIndex'
_E='SnmpAdminString'
_D='Unsigned32'
_C='read-only'
_B='DISMAN-NSLOOKUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
lookupMIB=ModuleIdentity((1,3,6,1,2,1,82))
if mibBuilder.loadTexts:lookupMIB.setRevisions(('2006-06-13 00:00','2000-09-21 00:00'))
_LookupObjects_ObjectIdentity=ObjectIdentity
lookupObjects=_LookupObjects_ObjectIdentity((1,3,6,1,2,1,82,1))
class _LookupMaxConcurrentRequests_Type(Unsigned32):defaultValue=10
_LookupMaxConcurrentRequests_Type.__name__=_D
_LookupMaxConcurrentRequests_Object=MibScalar
lookupMaxConcurrentRequests=_LookupMaxConcurrentRequests_Object((1,3,6,1,2,1,82,1,1),_LookupMaxConcurrentRequests_Type())
lookupMaxConcurrentRequests.setMaxAccess(_M)
if mibBuilder.loadTexts:lookupMaxConcurrentRequests.setStatus(_A)
if mibBuilder.loadTexts:lookupMaxConcurrentRequests.setUnits('requests')
class _LookupPurgeTime_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_LookupPurgeTime_Type.__name__=_D
_LookupPurgeTime_Object=MibScalar
lookupPurgeTime=_LookupPurgeTime_Object((1,3,6,1,2,1,82,1,2),_LookupPurgeTime_Type())
lookupPurgeTime.setMaxAccess(_M)
if mibBuilder.loadTexts:lookupPurgeTime.setStatus(_A)
if mibBuilder.loadTexts:lookupPurgeTime.setUnits('seconds')
_LookupCtlTable_Object=MibTable
lookupCtlTable=_LookupCtlTable_Object((1,3,6,1,2,1,82,1,3))
if mibBuilder.loadTexts:lookupCtlTable.setStatus(_A)
_LookupCtlEntry_Object=MibTableRow
lookupCtlEntry=_LookupCtlEntry_Object((1,3,6,1,2,1,82,1,3,1))
lookupCtlEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:lookupCtlEntry.setStatus(_A)
class _LookupCtlOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LookupCtlOwnerIndex_Type.__name__=_E
_LookupCtlOwnerIndex_Object=MibTableColumn
lookupCtlOwnerIndex=_LookupCtlOwnerIndex_Object((1,3,6,1,2,1,82,1,3,1,1),_LookupCtlOwnerIndex_Type())
lookupCtlOwnerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lookupCtlOwnerIndex.setStatus(_A)
class _LookupCtlOperationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LookupCtlOperationName_Type.__name__=_E
_LookupCtlOperationName_Object=MibTableColumn
lookupCtlOperationName=_LookupCtlOperationName_Object((1,3,6,1,2,1,82,1,3,1,2),_LookupCtlOperationName_Type())
lookupCtlOperationName.setMaxAccess(_H)
if mibBuilder.loadTexts:lookupCtlOperationName.setStatus(_A)
class _LookupCtlTargetAddressType_Type(InetAddressType):defaultValue=0
_LookupCtlTargetAddressType_Type.__name__=_K
_LookupCtlTargetAddressType_Object=MibTableColumn
lookupCtlTargetAddressType=_LookupCtlTargetAddressType_Object((1,3,6,1,2,1,82,1,3,1,3),_LookupCtlTargetAddressType_Type())
lookupCtlTargetAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:lookupCtlTargetAddressType.setStatus(_A)
_LookupCtlTargetAddress_Type=InetAddress
_LookupCtlTargetAddress_Object=MibTableColumn
lookupCtlTargetAddress=_LookupCtlTargetAddress_Object((1,3,6,1,2,1,82,1,3,1,4),_LookupCtlTargetAddress_Type())
lookupCtlTargetAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:lookupCtlTargetAddress.setStatus(_A)
class _LookupCtlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('notStarted',2),('completed',3)))
_LookupCtlOperStatus_Type.__name__=_L
_LookupCtlOperStatus_Object=MibTableColumn
lookupCtlOperStatus=_LookupCtlOperStatus_Object((1,3,6,1,2,1,82,1,3,1,5),_LookupCtlOperStatus_Type())
lookupCtlOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lookupCtlOperStatus.setStatus(_A)
_LookupCtlTime_Type=Unsigned32
_LookupCtlTime_Object=MibTableColumn
lookupCtlTime=_LookupCtlTime_Object((1,3,6,1,2,1,82,1,3,1,6),_LookupCtlTime_Type())
lookupCtlTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lookupCtlTime.setStatus(_A)
if mibBuilder.loadTexts:lookupCtlTime.setUnits('milliseconds')
_LookupCtlRc_Type=Integer32
_LookupCtlRc_Object=MibTableColumn
lookupCtlRc=_LookupCtlRc_Object((1,3,6,1,2,1,82,1,3,1,7),_LookupCtlRc_Type())
lookupCtlRc.setMaxAccess(_C)
if mibBuilder.loadTexts:lookupCtlRc.setStatus(_A)
_LookupCtlRowStatus_Type=RowStatus
_LookupCtlRowStatus_Object=MibTableColumn
lookupCtlRowStatus=_LookupCtlRowStatus_Object((1,3,6,1,2,1,82,1,3,1,8),_LookupCtlRowStatus_Type())
lookupCtlRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:lookupCtlRowStatus.setStatus(_A)
_LookupResultsTable_Object=MibTable
lookupResultsTable=_LookupResultsTable_Object((1,3,6,1,2,1,82,1,4))
if mibBuilder.loadTexts:lookupResultsTable.setStatus(_A)
_LookupResultsEntry_Object=MibTableRow
lookupResultsEntry=_LookupResultsEntry_Object((1,3,6,1,2,1,82,1,4,1))
lookupResultsEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_N))
if mibBuilder.loadTexts:lookupResultsEntry.setStatus(_A)
class _LookupResultsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_LookupResultsIndex_Type.__name__=_D
_LookupResultsIndex_Object=MibTableColumn
lookupResultsIndex=_LookupResultsIndex_Object((1,3,6,1,2,1,82,1,4,1,1),_LookupResultsIndex_Type())
lookupResultsIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lookupResultsIndex.setStatus(_A)
_LookupResultsAddressType_Type=InetAddressType
_LookupResultsAddressType_Object=MibTableColumn
lookupResultsAddressType=_LookupResultsAddressType_Object((1,3,6,1,2,1,82,1,4,1,2),_LookupResultsAddressType_Type())
lookupResultsAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:lookupResultsAddressType.setStatus(_A)
_LookupResultsAddress_Type=InetAddress
_LookupResultsAddress_Object=MibTableColumn
lookupResultsAddress=_LookupResultsAddress_Object((1,3,6,1,2,1,82,1,4,1,3),_LookupResultsAddress_Type())
lookupResultsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lookupResultsAddress.setStatus(_A)
_LookupConformance_ObjectIdentity=ObjectIdentity
lookupConformance=_LookupConformance_ObjectIdentity((1,3,6,1,2,1,82,2))
_LookupCompliances_ObjectIdentity=ObjectIdentity
lookupCompliances=_LookupCompliances_ObjectIdentity((1,3,6,1,2,1,82,2,1))
_LookupGroups_ObjectIdentity=ObjectIdentity
lookupGroups=_LookupGroups_ObjectIdentity((1,3,6,1,2,1,82,2,2))
lookupGroup=ObjectGroup((1,3,6,1,2,1,82,2,2,1))
lookupGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:lookupGroup.setStatus(_A)
lookupCompliance=ModuleCompliance((1,3,6,1,2,1,82,2,1,1))
lookupCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:lookupCompliance.setStatus(_A)
lookupMinimumCompliance=ModuleCompliance((1,3,6,1,2,1,82,2,1,2))
lookupMinimumCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:lookupMinimumCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lookupMIB':lookupMIB,'lookupObjects':lookupObjects,_O:lookupMaxConcurrentRequests,_P:lookupPurgeTime,'lookupCtlTable':lookupCtlTable,'lookupCtlEntry':lookupCtlEntry,_F:lookupCtlOwnerIndex,_G:lookupCtlOperationName,_R:lookupCtlTargetAddressType,_S:lookupCtlTargetAddress,_Q:lookupCtlOperStatus,_T:lookupCtlTime,_U:lookupCtlRc,_V:lookupCtlRowStatus,'lookupResultsTable':lookupResultsTable,'lookupResultsEntry':lookupResultsEntry,_N:lookupResultsIndex,_W:lookupResultsAddressType,_X:lookupResultsAddress,'lookupConformance':lookupConformance,'lookupCompliances':lookupCompliances,'lookupCompliance':lookupCompliance,'lookupMinimumCompliance':lookupMinimumCompliance,'lookupGroups':lookupGroups,_J:lookupGroup})