_J='jnxVplsBgpVEId'
_I='VPLS-BGP-DRAFT-01-MIB'
_H='jnxVplsPwBindIndex'
_G='StorageType'
_F='SnmpAdminString'
_E='jnxVplsConfigIndex'
_D='VPLS-GENERIC-DRAFT-01-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxExperiment,=mibBuilder.importSymbols('JUNIPER-SMI','jnxExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_G,'TextualConvention')
jnxVplsConfigIndex,jnxVplsPwBindIndex=mibBuilder.importSymbols(_D,_E,_H)
jnxVplsBgpDraft01MIB=ModuleIdentity((1,3,6,1,4,1,2636,5,10))
if mibBuilder.loadTexts:jnxVplsBgpDraft01MIB.setRevisions(('2006-12-06 12:00',))
_JnxVplsBgpObjects_ObjectIdentity=ObjectIdentity
jnxVplsBgpObjects=_JnxVplsBgpObjects_ObjectIdentity((1,3,6,1,4,1,2636,5,10,1))
_JnxVplsBgpConfigTable_Object=MibTable
jnxVplsBgpConfigTable=_JnxVplsBgpConfigTable_Object((1,3,6,1,4,1,2636,5,10,1,1))
if mibBuilder.loadTexts:jnxVplsBgpConfigTable.setStatus(_A)
_JnxVplsBgpConfigEntry_Object=MibTableRow
jnxVplsBgpConfigEntry=_JnxVplsBgpConfigEntry_Object((1,3,6,1,4,1,2636,5,10,1,1,1))
jnxVplsBgpConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:jnxVplsBgpConfigEntry.setStatus(_A)
class _JnxVplsBgpConfigVERangeSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JnxVplsBgpConfigVERangeSize_Type.__name__=_C
_JnxVplsBgpConfigVERangeSize_Object=MibTableColumn
jnxVplsBgpConfigVERangeSize=_JnxVplsBgpConfigVERangeSize_Object((1,3,6,1,4,1,2636,5,10,1,1,1,1),_JnxVplsBgpConfigVERangeSize_Type())
jnxVplsBgpConfigVERangeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVplsBgpConfigVERangeSize.setStatus(_A)
_JnxVplsBgpVETable_Object=MibTable
jnxVplsBgpVETable=_JnxVplsBgpVETable_Object((1,3,6,1,4,1,2636,5,10,1,2))
if mibBuilder.loadTexts:jnxVplsBgpVETable.setStatus(_A)
_JnxVplsBgpVEEntry_Object=MibTableRow
jnxVplsBgpVEEntry=_JnxVplsBgpVEEntry_Object((1,3,6,1,4,1,2636,5,10,1,2,1))
jnxVplsBgpVEEntry.setIndexNames((0,_D,_E),(0,_I,_J))
if mibBuilder.loadTexts:jnxVplsBgpVEEntry.setStatus(_A)
class _JnxVplsBgpVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxVplsBgpVEId_Type.__name__=_C
_JnxVplsBgpVEId_Object=MibTableColumn
jnxVplsBgpVEId=_JnxVplsBgpVEId_Object((1,3,6,1,4,1,2636,5,10,1,2,1,1),_JnxVplsBgpVEId_Type())
jnxVplsBgpVEId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:jnxVplsBgpVEId.setStatus(_A)
class _JnxVplsBgpVEName_Type(SnmpAdminString):defaultValue=OctetString('')
_JnxVplsBgpVEName_Type.__name__=_F
_JnxVplsBgpVEName_Object=MibTableColumn
jnxVplsBgpVEName=_JnxVplsBgpVEName_Object((1,3,6,1,4,1,2636,5,10,1,2,1,2),_JnxVplsBgpVEName_Type())
jnxVplsBgpVEName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVplsBgpVEName.setStatus(_A)
class _JnxVplsBgpVEPreference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JnxVplsBgpVEPreference_Type.__name__=_C
_JnxVplsBgpVEPreference_Object=MibTableColumn
jnxVplsBgpVEPreference=_JnxVplsBgpVEPreference_Object((1,3,6,1,4,1,2636,5,10,1,2,1,3),_JnxVplsBgpVEPreference_Type())
jnxVplsBgpVEPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVplsBgpVEPreference.setStatus(_A)
_JnxVplsBgpVERowStatus_Type=RowStatus
_JnxVplsBgpVERowStatus_Object=MibTableColumn
jnxVplsBgpVERowStatus=_JnxVplsBgpVERowStatus_Object((1,3,6,1,4,1,2636,5,10,1,2,1,5),_JnxVplsBgpVERowStatus_Type())
jnxVplsBgpVERowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVplsBgpVERowStatus.setStatus(_A)
class _JnxVplsBgpVEStorageType_Type(StorageType):defaultValue=2
_JnxVplsBgpVEStorageType_Type.__name__=_G
_JnxVplsBgpVEStorageType_Object=MibTableColumn
jnxVplsBgpVEStorageType=_JnxVplsBgpVEStorageType_Object((1,3,6,1,4,1,2636,5,10,1,2,1,6),_JnxVplsBgpVEStorageType_Type())
jnxVplsBgpVEStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVplsBgpVEStorageType.setStatus(_A)
_JnxVplsBgpPwBindTable_Object=MibTable
jnxVplsBgpPwBindTable=_JnxVplsBgpPwBindTable_Object((1,3,6,1,4,1,2636,5,10,1,3))
if mibBuilder.loadTexts:jnxVplsBgpPwBindTable.setStatus(_A)
_JnxVplsBgpPwBindEntry_Object=MibTableRow
jnxVplsBgpPwBindEntry=_JnxVplsBgpPwBindEntry_Object((1,3,6,1,4,1,2636,5,10,1,3,1))
jnxVplsBgpPwBindEntry.setIndexNames((0,_D,_E),(0,_D,_H))
if mibBuilder.loadTexts:jnxVplsBgpPwBindEntry.setStatus(_A)
class _JnxVplsBgpPwBindLocalVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxVplsBgpPwBindLocalVEId_Type.__name__=_C
_JnxVplsBgpPwBindLocalVEId_Object=MibTableColumn
jnxVplsBgpPwBindLocalVEId=_JnxVplsBgpPwBindLocalVEId_Object((1,3,6,1,4,1,2636,5,10,1,3,1,1),_JnxVplsBgpPwBindLocalVEId_Type())
jnxVplsBgpPwBindLocalVEId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVplsBgpPwBindLocalVEId.setStatus(_A)
class _JnxVplsBgpPwBindRemoteVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxVplsBgpPwBindRemoteVEId_Type.__name__=_C
_JnxVplsBgpPwBindRemoteVEId_Object=MibTableColumn
jnxVplsBgpPwBindRemoteVEId=_JnxVplsBgpPwBindRemoteVEId_Object((1,3,6,1,4,1,2636,5,10,1,3,1,2),_JnxVplsBgpPwBindRemoteVEId_Type())
jnxVplsBgpPwBindRemoteVEId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVplsBgpPwBindRemoteVEId.setStatus(_A)
_JnxVplsBgpConformance_ObjectIdentity=ObjectIdentity
jnxVplsBgpConformance=_JnxVplsBgpConformance_ObjectIdentity((1,3,6,1,4,1,2636,5,10,2))
mibBuilder.exportSymbols(_I,**{'jnxVplsBgpDraft01MIB':jnxVplsBgpDraft01MIB,'jnxVplsBgpObjects':jnxVplsBgpObjects,'jnxVplsBgpConfigTable':jnxVplsBgpConfigTable,'jnxVplsBgpConfigEntry':jnxVplsBgpConfigEntry,'jnxVplsBgpConfigVERangeSize':jnxVplsBgpConfigVERangeSize,'jnxVplsBgpVETable':jnxVplsBgpVETable,'jnxVplsBgpVEEntry':jnxVplsBgpVEEntry,_J:jnxVplsBgpVEId,'jnxVplsBgpVEName':jnxVplsBgpVEName,'jnxVplsBgpVEPreference':jnxVplsBgpVEPreference,'jnxVplsBgpVERowStatus':jnxVplsBgpVERowStatus,'jnxVplsBgpVEStorageType':jnxVplsBgpVEStorageType,'jnxVplsBgpPwBindTable':jnxVplsBgpPwBindTable,'jnxVplsBgpPwBindEntry':jnxVplsBgpPwBindEntry,'jnxVplsBgpPwBindLocalVEId':jnxVplsBgpPwBindLocalVEId,'jnxVplsBgpPwBindRemoteVEId':jnxVplsBgpPwBindRemoteVEId,'jnxVplsBgpConformance':jnxVplsBgpConformance})