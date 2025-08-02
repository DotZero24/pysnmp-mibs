_b='etsysLicenseKeyPhysicalConfigGroup'
_a='etsysLicenseKeyConfigurationGroup'
_Z='etsysLicenseKeyPhysicalExpiration'
_Y='etsysLicenseKeyPhysicalLastModified'
_X='etsysLicenseKeyPhysicalStatusText'
_W='etsysLicenseKeyPhysicalStatus'
_V='etsysLicenseKeyPhysicalString'
_U='etsysLicenseKeyPhysicalDescription'
_T='etsysLicenseKeyPhysicalIdentifier'
_S='etsysLicenseKeyExpiration'
_R='etsysLicenseKeyLastModified'
_Q='etsysLicenseKeyStatusText'
_P='etsysLicenseKeyStatus'
_O='etsysLicenseKeyString'
_N='etsysLicenseKeyDescription'
_M='etsysLicenseKeyIdentifier'
_L='etsysLicenseKeyPhysicalIndex'
_K='read-write'
_J='not-accessible'
_I='etsysLicenseKeyIndex'
_H='SnmpAdminString'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='OctetString'
_D='read-only'
_C='obsolete'
_B='current'
_A='ENTERASYS-LICENSE-KEY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
etsysLicenseKeyMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,54))
if mibBuilder.loadTexts:etsysLicenseKeyMIB.setRevisions(('2009-09-02 18:59','2004-11-03 19:52','2004-08-30 14:52','2004-08-17 16:35'))
class LicenseKeyStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('active',2),('invalid',3),('expired',4),('restricted',5),('uninitialized',6),('validNotActive',7)))
_EtsysLicenseKeyObjects_ObjectIdentity=ObjectIdentity
etsysLicenseKeyObjects=_EtsysLicenseKeyObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,54,1))
_EtsysLicenseKeyConfiguration_ObjectIdentity=ObjectIdentity
etsysLicenseKeyConfiguration=_EtsysLicenseKeyConfiguration_ObjectIdentity((1,3,6,1,4,1,5624,1,2,54,1,1))
_EtsysLicenseKeyTable_Object=MibTable
etsysLicenseKeyTable=_EtsysLicenseKeyTable_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1))
if mibBuilder.loadTexts:etsysLicenseKeyTable.setStatus(_C)
_EtsysLicenseKeyEntry_Object=MibTableRow
etsysLicenseKeyEntry=_EtsysLicenseKeyEntry_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1))
etsysLicenseKeyEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:etsysLicenseKeyEntry.setStatus(_C)
_EtsysLicenseKeyIndex_Type=Unsigned32
_EtsysLicenseKeyIndex_Object=MibTableColumn
etsysLicenseKeyIndex=_EtsysLicenseKeyIndex_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,1),_EtsysLicenseKeyIndex_Type())
etsysLicenseKeyIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:etsysLicenseKeyIndex.setStatus(_C)
_EtsysLicenseKeyIdentifier_Type=ObjectIdentifier
_EtsysLicenseKeyIdentifier_Object=MibTableColumn
etsysLicenseKeyIdentifier=_EtsysLicenseKeyIdentifier_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,2),_EtsysLicenseKeyIdentifier_Type())
etsysLicenseKeyIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyIdentifier.setStatus(_C)
_EtsysLicenseKeyDescription_Type=SnmpAdminString
_EtsysLicenseKeyDescription_Object=MibTableColumn
etsysLicenseKeyDescription=_EtsysLicenseKeyDescription_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,3),_EtsysLicenseKeyDescription_Type())
etsysLicenseKeyDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyDescription.setStatus(_C)
class _EtsysLicenseKeyString_Type(SnmpAdminString):defaultValue=OctetString('')
_EtsysLicenseKeyString_Type.__name__=_H
_EtsysLicenseKeyString_Object=MibTableColumn
etsysLicenseKeyString=_EtsysLicenseKeyString_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,4),_EtsysLicenseKeyString_Type())
etsysLicenseKeyString.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysLicenseKeyString.setStatus(_C)
_EtsysLicenseKeyStatus_Type=LicenseKeyStatus
_EtsysLicenseKeyStatus_Object=MibTableColumn
etsysLicenseKeyStatus=_EtsysLicenseKeyStatus_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,5),_EtsysLicenseKeyStatus_Type())
etsysLicenseKeyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyStatus.setStatus(_C)
_EtsysLicenseKeyStatusText_Type=SnmpAdminString
_EtsysLicenseKeyStatusText_Object=MibTableColumn
etsysLicenseKeyStatusText=_EtsysLicenseKeyStatusText_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,6),_EtsysLicenseKeyStatusText_Type())
etsysLicenseKeyStatusText.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyStatusText.setStatus(_C)
_EtsysLicenseKeyLastModified_Type=DateAndTime
_EtsysLicenseKeyLastModified_Object=MibTableColumn
etsysLicenseKeyLastModified=_EtsysLicenseKeyLastModified_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,7),_EtsysLicenseKeyLastModified_Type())
etsysLicenseKeyLastModified.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyLastModified.setStatus(_C)
_EtsysLicenseKeyExpiration_Type=DateAndTime
_EtsysLicenseKeyExpiration_Object=MibTableColumn
etsysLicenseKeyExpiration=_EtsysLicenseKeyExpiration_Object((1,3,6,1,4,1,5624,1,2,54,1,1,1,1,8),_EtsysLicenseKeyExpiration_Type())
etsysLicenseKeyExpiration.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyExpiration.setStatus(_C)
_EtsysLicenseKeyPhysicalTable_Object=MibTable
etsysLicenseKeyPhysicalTable=_EtsysLicenseKeyPhysicalTable_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2))
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalTable.setStatus(_B)
_EtsysLicenseKeyPhysicalEntry_Object=MibTableRow
etsysLicenseKeyPhysicalEntry=_EtsysLicenseKeyPhysicalEntry_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1))
etsysLicenseKeyPhysicalEntry.setIndexNames((0,_F,_G),(0,_A,_L))
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalEntry.setStatus(_B)
_EtsysLicenseKeyPhysicalIndex_Type=Unsigned32
_EtsysLicenseKeyPhysicalIndex_Object=MibTableColumn
etsysLicenseKeyPhysicalIndex=_EtsysLicenseKeyPhysicalIndex_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,1),_EtsysLicenseKeyPhysicalIndex_Type())
etsysLicenseKeyPhysicalIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalIndex.setStatus(_B)
_EtsysLicenseKeyPhysicalIdentifier_Type=ObjectIdentifier
_EtsysLicenseKeyPhysicalIdentifier_Object=MibTableColumn
etsysLicenseKeyPhysicalIdentifier=_EtsysLicenseKeyPhysicalIdentifier_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,2),_EtsysLicenseKeyPhysicalIdentifier_Type())
etsysLicenseKeyPhysicalIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalIdentifier.setStatus(_B)
_EtsysLicenseKeyPhysicalDescription_Type=SnmpAdminString
_EtsysLicenseKeyPhysicalDescription_Object=MibTableColumn
etsysLicenseKeyPhysicalDescription=_EtsysLicenseKeyPhysicalDescription_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,3),_EtsysLicenseKeyPhysicalDescription_Type())
etsysLicenseKeyPhysicalDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalDescription.setStatus(_B)
class _EtsysLicenseKeyPhysicalString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_EtsysLicenseKeyPhysicalString_Type.__name__=_E
_EtsysLicenseKeyPhysicalString_Object=MibTableColumn
etsysLicenseKeyPhysicalString=_EtsysLicenseKeyPhysicalString_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,4),_EtsysLicenseKeyPhysicalString_Type())
etsysLicenseKeyPhysicalString.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalString.setStatus(_B)
_EtsysLicenseKeyPhysicalStatus_Type=LicenseKeyStatus
_EtsysLicenseKeyPhysicalStatus_Object=MibTableColumn
etsysLicenseKeyPhysicalStatus=_EtsysLicenseKeyPhysicalStatus_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,5),_EtsysLicenseKeyPhysicalStatus_Type())
etsysLicenseKeyPhysicalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalStatus.setStatus(_B)
_EtsysLicenseKeyPhysicalStatusText_Type=SnmpAdminString
_EtsysLicenseKeyPhysicalStatusText_Object=MibTableColumn
etsysLicenseKeyPhysicalStatusText=_EtsysLicenseKeyPhysicalStatusText_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,6),_EtsysLicenseKeyPhysicalStatusText_Type())
etsysLicenseKeyPhysicalStatusText.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalStatusText.setStatus(_B)
_EtsysLicenseKeyPhysicalLastModified_Type=DateAndTime
_EtsysLicenseKeyPhysicalLastModified_Object=MibTableColumn
etsysLicenseKeyPhysicalLastModified=_EtsysLicenseKeyPhysicalLastModified_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,7),_EtsysLicenseKeyPhysicalLastModified_Type())
etsysLicenseKeyPhysicalLastModified.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalLastModified.setStatus(_B)
_EtsysLicenseKeyPhysicalExpiration_Type=DateAndTime
_EtsysLicenseKeyPhysicalExpiration_Object=MibTableColumn
etsysLicenseKeyPhysicalExpiration=_EtsysLicenseKeyPhysicalExpiration_Object((1,3,6,1,4,1,5624,1,2,54,1,1,2,1,8),_EtsysLicenseKeyPhysicalExpiration_Type())
etsysLicenseKeyPhysicalExpiration.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalExpiration.setStatus(_B)
_EtsysLicenseKeyConformance_ObjectIdentity=ObjectIdentity
etsysLicenseKeyConformance=_EtsysLicenseKeyConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,54,2))
_EtsysLicenseKeyGroups_ObjectIdentity=ObjectIdentity
etsysLicenseKeyGroups=_EtsysLicenseKeyGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,54,2,1))
_EtsysLicenseKeyCompliances_ObjectIdentity=ObjectIdentity
etsysLicenseKeyCompliances=_EtsysLicenseKeyCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,54,2,2))
etsysLicenseKeyConfigurationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,54,2,1,1))
etsysLicenseKeyConfigurationGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:etsysLicenseKeyConfigurationGroup.setStatus(_C)
etsysLicenseKeyPhysicalConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,54,2,1,2))
etsysLicenseKeyPhysicalConfigGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:etsysLicenseKeyPhysicalConfigGroup.setStatus(_B)
etsysLicenseKeyCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,54,2,2,1))
etsysLicenseKeyCompliance.setObjects((_A,_a))
if mibBuilder.loadTexts:etsysLicenseKeyCompliance.setStatus(_C)
etsysLicenseKeyCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,54,2,2,2))
etsysLicenseKeyCompliance2.setObjects((_A,_b))
if mibBuilder.loadTexts:etsysLicenseKeyCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'LicenseKeyStatus':LicenseKeyStatus,'etsysLicenseKeyMIB':etsysLicenseKeyMIB,'etsysLicenseKeyObjects':etsysLicenseKeyObjects,'etsysLicenseKeyConfiguration':etsysLicenseKeyConfiguration,'etsysLicenseKeyTable':etsysLicenseKeyTable,'etsysLicenseKeyEntry':etsysLicenseKeyEntry,_I:etsysLicenseKeyIndex,_M:etsysLicenseKeyIdentifier,_N:etsysLicenseKeyDescription,_O:etsysLicenseKeyString,_P:etsysLicenseKeyStatus,_Q:etsysLicenseKeyStatusText,_R:etsysLicenseKeyLastModified,_S:etsysLicenseKeyExpiration,'etsysLicenseKeyPhysicalTable':etsysLicenseKeyPhysicalTable,'etsysLicenseKeyPhysicalEntry':etsysLicenseKeyPhysicalEntry,_L:etsysLicenseKeyPhysicalIndex,_T:etsysLicenseKeyPhysicalIdentifier,_U:etsysLicenseKeyPhysicalDescription,_V:etsysLicenseKeyPhysicalString,_W:etsysLicenseKeyPhysicalStatus,_X:etsysLicenseKeyPhysicalStatusText,_Y:etsysLicenseKeyPhysicalLastModified,_Z:etsysLicenseKeyPhysicalExpiration,'etsysLicenseKeyConformance':etsysLicenseKeyConformance,'etsysLicenseKeyGroups':etsysLicenseKeyGroups,_a:etsysLicenseKeyConfigurationGroup,_b:etsysLicenseKeyPhysicalConfigGroup,'etsysLicenseKeyCompliances':etsysLicenseKeyCompliances,'etsysLicenseKeyCompliance':etsysLicenseKeyCompliance,'etsysLicenseKeyCompliance2':etsysLicenseKeyCompliance2})