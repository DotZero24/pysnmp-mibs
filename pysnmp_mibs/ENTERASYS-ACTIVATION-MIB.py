_O='etsysActivationBaseGroup'
_N='etsysActivationKeyRestrictions'
_M='etsysActivationKeyStatus'
_L='etsysActivationKeyType'
_K='etsysActivationKeyValue'
_J='etsysActivationLicenseString'
_I='etsysMaxActivationKeyRow'
_H='etsysActivationKeyFeature'
_G='not-accessible'
_F='read-create'
_E='etsysActivationKeyRow'
_D='read-only'
_C='Integer32'
_B='ENTERASYS-ACTIVATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
etsysActivationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,99999))
if mibBuilder.loadTexts:etsysActivationMIB.setRevisions(('2002-04-18 14:54',))
class EnterasysKeyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noKey',1),('unknownKeyType',2),('productKey',3),('demoKey',4)))
class EnterasysFeature(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1xAuthentication',1),('pointToMultipoint',2)))
_EtsysActivationObjects_ObjectIdentity=ObjectIdentity
etsysActivationObjects=_EtsysActivationObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99999,1))
_EtsysActivationBaseBranch_ObjectIdentity=ObjectIdentity
etsysActivationBaseBranch=_EtsysActivationBaseBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99999,1,1))
class _EtsysMaxActivationKeyRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysMaxActivationKeyRow_Type.__name__=_C
_EtsysMaxActivationKeyRow_Object=MibScalar
etsysMaxActivationKeyRow=_EtsysMaxActivationKeyRow_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,1),_EtsysMaxActivationKeyRow_Type())
etsysMaxActivationKeyRow.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMaxActivationKeyRow.setStatus(_A)
_EtsysActivationKeyTable_Object=MibTable
etsysActivationKeyTable=_EtsysActivationKeyTable_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,2))
if mibBuilder.loadTexts:etsysActivationKeyTable.setStatus(_A)
_EtsysActivationKeyEntry_Object=MibTableRow
etsysActivationKeyEntry=_EtsysActivationKeyEntry_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,2,1))
etsysActivationKeyEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:etsysActivationKeyEntry.setStatus(_A)
class _EtsysActivationKeyRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysActivationKeyRow_Type.__name__=_C
_EtsysActivationKeyRow_Object=MibTableColumn
etsysActivationKeyRow=_EtsysActivationKeyRow_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,2,1,1),_EtsysActivationKeyRow_Type())
etsysActivationKeyRow.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysActivationKeyRow.setStatus(_A)
_EtsysActivationLicenseString_Type=SnmpAdminString
_EtsysActivationLicenseString_Object=MibTableColumn
etsysActivationLicenseString=_EtsysActivationLicenseString_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,2,1,2),_EtsysActivationLicenseString_Type())
etsysActivationLicenseString.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysActivationLicenseString.setStatus(_A)
_EtsysActivationKeyValue_Type=SnmpAdminString
_EtsysActivationKeyValue_Object=MibTableColumn
etsysActivationKeyValue=_EtsysActivationKeyValue_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,2,1,3),_EtsysActivationKeyValue_Type())
etsysActivationKeyValue.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysActivationKeyValue.setStatus(_A)
_EtsysActivationKeyType_Type=EnterasysKeyType
_EtsysActivationKeyType_Object=MibTableColumn
etsysActivationKeyType=_EtsysActivationKeyType_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,2,1,4),_EtsysActivationKeyType_Type())
etsysActivationKeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysActivationKeyType.setStatus(_A)
_EtsysActivationKeyStatus_Type=RowStatus
_EtsysActivationKeyStatus_Object=MibTableColumn
etsysActivationKeyStatus=_EtsysActivationKeyStatus_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,2,1,5),_EtsysActivationKeyStatus_Type())
etsysActivationKeyStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysActivationKeyStatus.setStatus(_A)
_EtsysActivationKeyFeatureTable_Object=MibTable
etsysActivationKeyFeatureTable=_EtsysActivationKeyFeatureTable_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,3))
if mibBuilder.loadTexts:etsysActivationKeyFeatureTable.setStatus(_A)
_EtsysActivationKeyFeatureEntry_Object=MibTableRow
etsysActivationKeyFeatureEntry=_EtsysActivationKeyFeatureEntry_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,3,1))
etsysActivationKeyFeatureEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:etsysActivationKeyFeatureEntry.setStatus(_A)
_EtsysActivationKeyFeature_Type=EnterasysFeature
_EtsysActivationKeyFeature_Object=MibTableColumn
etsysActivationKeyFeature=_EtsysActivationKeyFeature_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,3,1,1),_EtsysActivationKeyFeature_Type())
etsysActivationKeyFeature.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysActivationKeyFeature.setStatus(_A)
_EtsysActivationKeyRestrictions_Type=SnmpAdminString
_EtsysActivationKeyRestrictions_Object=MibTableColumn
etsysActivationKeyRestrictions=_EtsysActivationKeyRestrictions_Object((1,3,6,1,4,1,5624,1,2,99999,1,1,3,1,2),_EtsysActivationKeyRestrictions_Type())
etsysActivationKeyRestrictions.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysActivationKeyRestrictions.setStatus(_A)
_EtsysActivationConformance_ObjectIdentity=ObjectIdentity
etsysActivationConformance=_EtsysActivationConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99999,2))
_EtsysActivationGroups_ObjectIdentity=ObjectIdentity
etsysActivationGroups=_EtsysActivationGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99999,2,1))
_EtsysActivationCompliances_ObjectIdentity=ObjectIdentity
etsysActivationCompliances=_EtsysActivationCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99999,2,2))
etsysActivationBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,99999,2,1,1))
etsysActivationBaseGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:etsysActivationBaseGroup.setStatus(_A)
etsysActivationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,99999,2,2,1))
etsysActivationCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:etsysActivationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EnterasysKeyType':EnterasysKeyType,'EnterasysFeature':EnterasysFeature,'etsysActivationMIB':etsysActivationMIB,'etsysActivationObjects':etsysActivationObjects,'etsysActivationBaseBranch':etsysActivationBaseBranch,_I:etsysMaxActivationKeyRow,'etsysActivationKeyTable':etsysActivationKeyTable,'etsysActivationKeyEntry':etsysActivationKeyEntry,_E:etsysActivationKeyRow,_J:etsysActivationLicenseString,_K:etsysActivationKeyValue,_L:etsysActivationKeyType,_M:etsysActivationKeyStatus,'etsysActivationKeyFeatureTable':etsysActivationKeyFeatureTable,'etsysActivationKeyFeatureEntry':etsysActivationKeyFeatureEntry,_H:etsysActivationKeyFeature,_N:etsysActivationKeyRestrictions,'etsysActivationConformance':etsysActivationConformance,'etsysActivationGroups':etsysActivationGroups,_O:etsysActivationBaseGroup,'etsysActivationCompliances':etsysActivationCompliances,'etsysActivationCompliance':etsysActivationCompliance})