_I='hpnicfDot11LICKeyIndex'
_H='hpnicfDot11LICAttrIndex'
_G='hpnicfDot11LICLicenseKeyIndex'
_F='TruthValue'
_E='OctetString'
_D='HPN-ICF-DOT11-LIC-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfDot11,=mibBuilder.importSymbols('HPN-ICF-DOT11-REF-MIB','hpnicfDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
hpnicfDot11LIC=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,14))
if mibBuilder.loadTexts:hpnicfDot11LIC.setRevisions(('2012-04-25 18:00',))
_HpnicfDot11LICConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11LICConfigGroup=_HpnicfDot11LICConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,14,1))
class _HpnicfDot11LICSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11LICSerialNumber_Type.__name__=_E
_HpnicfDot11LICSerialNumber_Object=MibScalar
hpnicfDot11LICSerialNumber=_HpnicfDot11LICSerialNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,1,1),_HpnicfDot11LICSerialNumber_Type())
hpnicfDot11LICSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICSerialNumber.setStatus(_A)
class _HpnicfDot11LicApNumGroupSupport_Type(TruthValue):defaultValue=2
_HpnicfDot11LicApNumGroupSupport_Type.__name__=_F
_HpnicfDot11LicApNumGroupSupport_Object=MibScalar
hpnicfDot11LicApNumGroupSupport=_HpnicfDot11LicApNumGroupSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,1,2),_HpnicfDot11LicApNumGroupSupport_Type())
hpnicfDot11LicApNumGroupSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LicApNumGroupSupport.setStatus(_A)
_HpnicfDot11LICApNumGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11LICApNumGroup=_HpnicfDot11LICApNumGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2))
_HpnicfDot11LICApNumAttrTable_ObjectIdentity=ObjectIdentity
hpnicfDot11LICApNumAttrTable=_HpnicfDot11LICApNumAttrTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,1))
_HpnicfDot11LICDefautAPNumPermit_Type=Integer32
_HpnicfDot11LICDefautAPNumPermit_Object=MibScalar
hpnicfDot11LICDefautAPNumPermit=_HpnicfDot11LICDefautAPNumPermit_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,1,1),_HpnicfDot11LICDefautAPNumPermit_Type())
hpnicfDot11LICDefautAPNumPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICDefautAPNumPermit.setStatus(_A)
_HpnicfDot11LICCurrentAPNumPermit_Type=Integer32
_HpnicfDot11LICCurrentAPNumPermit_Object=MibScalar
hpnicfDot11LICCurrentAPNumPermit=_HpnicfDot11LICCurrentAPNumPermit_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,1,2),_HpnicfDot11LICCurrentAPNumPermit_Type())
hpnicfDot11LICCurrentAPNumPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICCurrentAPNumPermit.setStatus(_A)
_HpnicfDot11LICMaxAPNumPermit_Type=Integer32
_HpnicfDot11LICMaxAPNumPermit_Object=MibScalar
hpnicfDot11LICMaxAPNumPermit=_HpnicfDot11LICMaxAPNumPermit_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,1,3),_HpnicfDot11LICMaxAPNumPermit_Type())
hpnicfDot11LICMaxAPNumPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICMaxAPNumPermit.setStatus(_A)
_HpnicfDot11LICApNumLicTable_Object=MibTable
hpnicfDot11LICApNumLicTable=_HpnicfDot11LICApNumLicTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,2))
if mibBuilder.loadTexts:hpnicfDot11LICApNumLicTable.setStatus(_A)
_HpnicfDot11LICApNumLicEntry_Object=MibTableRow
hpnicfDot11LICApNumLicEntry=_HpnicfDot11LICApNumLicEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,2,1))
hpnicfDot11LICApNumLicEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfDot11LICApNumLicEntry.setStatus(_A)
class _HpnicfDot11LICLicenseKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11LICLicenseKeyIndex_Type.__name__=_C
_HpnicfDot11LICLicenseKeyIndex_Object=MibTableColumn
hpnicfDot11LICLicenseKeyIndex=_HpnicfDot11LICLicenseKeyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,2,1,1),_HpnicfDot11LICLicenseKeyIndex_Type())
hpnicfDot11LICLicenseKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICLicenseKeyIndex.setStatus(_A)
_HpnicfDot11LICLicenseKey_Type=OctetString
_HpnicfDot11LICLicenseKey_Object=MibTableColumn
hpnicfDot11LICLicenseKey=_HpnicfDot11LICLicenseKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,2,1,2),_HpnicfDot11LICLicenseKey_Type())
hpnicfDot11LICLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICLicenseKey.setStatus(_A)
_HpnicfDot11LICActivationKey_Type=OctetString
_HpnicfDot11LICActivationKey_Object=MibTableColumn
hpnicfDot11LICActivationKey=_HpnicfDot11LICActivationKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,2,1,3),_HpnicfDot11LICActivationKey_Type())
hpnicfDot11LICActivationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICActivationKey.setStatus(_A)
_HpnicfDot11LICApNum_Type=Integer32
_HpnicfDot11LICApNum_Object=MibTableColumn
hpnicfDot11LICApNum=_HpnicfDot11LICApNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,2,2,1,4),_HpnicfDot11LICApNum_Type())
hpnicfDot11LICApNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICApNum.setStatus(_A)
_HpnicfDot11LICFeatureGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11LICFeatureGroup=_HpnicfDot11LICFeatureGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3))
_HpnicfDot11LICFeatureAttrTable_Object=MibTable
hpnicfDot11LICFeatureAttrTable=_HpnicfDot11LICFeatureAttrTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,1))
if mibBuilder.loadTexts:hpnicfDot11LICFeatureAttrTable.setStatus(_A)
_HpnicfDot11LICFeatureAttrEntry_Object=MibTableRow
hpnicfDot11LICFeatureAttrEntry=_HpnicfDot11LICFeatureAttrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,1,1))
hpnicfDot11LICFeatureAttrEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnicfDot11LICFeatureAttrEntry.setStatus(_A)
class _HpnicfDot11LICAttrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11LICAttrIndex_Type.__name__=_C
_HpnicfDot11LICAttrIndex_Object=MibTableColumn
hpnicfDot11LICAttrIndex=_HpnicfDot11LICAttrIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,1,1,1),_HpnicfDot11LICAttrIndex_Type())
hpnicfDot11LICAttrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICAttrIndex.setStatus(_A)
_HpnicfDot11LICAttrTypeName_Type=OctetString
_HpnicfDot11LICAttrTypeName_Object=MibTableColumn
hpnicfDot11LICAttrTypeName=_HpnicfDot11LICAttrTypeName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,1,1,2),_HpnicfDot11LICAttrTypeName_Type())
hpnicfDot11LICAttrTypeName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICAttrTypeName.setStatus(_A)
_HpnicfDot11LICAttrDefVal_Type=Integer32
_HpnicfDot11LICAttrDefVal_Object=MibTableColumn
hpnicfDot11LICAttrDefVal=_HpnicfDot11LICAttrDefVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,1,1,3),_HpnicfDot11LICAttrDefVal_Type())
hpnicfDot11LICAttrDefVal.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICAttrDefVal.setStatus(_A)
_HpnicfDot11LICAttrMaxVal_Type=Integer32
_HpnicfDot11LICAttrMaxVal_Object=MibTableColumn
hpnicfDot11LICAttrMaxVal=_HpnicfDot11LICAttrMaxVal_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,1,1,4),_HpnicfDot11LICAttrMaxVal_Type())
hpnicfDot11LICAttrMaxVal.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICAttrMaxVal.setStatus(_A)
_HpnicfDot11LICFeatureLicTable_Object=MibTable
hpnicfDot11LICFeatureLicTable=_HpnicfDot11LICFeatureLicTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,2))
if mibBuilder.loadTexts:hpnicfDot11LICFeatureLicTable.setStatus(_A)
_HpnicfDot11LICFeatureLicEntry_Object=MibTableRow
hpnicfDot11LICFeatureLicEntry=_HpnicfDot11LICFeatureLicEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,2,1))
hpnicfDot11LICFeatureLicEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hpnicfDot11LICFeatureLicEntry.setStatus(_A)
class _HpnicfDot11LICKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11LICKeyIndex_Type.__name__=_C
_HpnicfDot11LICKeyIndex_Object=MibTableColumn
hpnicfDot11LICKeyIndex=_HpnicfDot11LICKeyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,2,1,1),_HpnicfDot11LICKeyIndex_Type())
hpnicfDot11LICKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICKeyIndex.setStatus(_A)
_HpnicfDot11LICTypeName_Type=OctetString
_HpnicfDot11LICTypeName_Object=MibTableColumn
hpnicfDot11LICTypeName=_HpnicfDot11LICTypeName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,2,1,2),_HpnicfDot11LICTypeName_Type())
hpnicfDot11LICTypeName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICTypeName.setStatus(_A)
_HpnicfDot11LICKey_Type=OctetString
_HpnicfDot11LICKey_Object=MibTableColumn
hpnicfDot11LICKey=_HpnicfDot11LICKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,2,1,3),_HpnicfDot11LICKey_Type())
hpnicfDot11LICKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICKey.setStatus(_A)
_HpnicfDot11LICTimeLimit_Type=Integer32
_HpnicfDot11LICTimeLimit_Object=MibTableColumn
hpnicfDot11LICTimeLimit=_HpnicfDot11LICTimeLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,2,1,4),_HpnicfDot11LICTimeLimit_Type())
hpnicfDot11LICTimeLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICTimeLimit.setStatus(_A)
_HpnicfDot11LICValue_Type=Integer32
_HpnicfDot11LICValue_Object=MibTableColumn
hpnicfDot11LICValue=_HpnicfDot11LICValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,14,3,2,1,5),_HpnicfDot11LICValue_Type())
hpnicfDot11LICValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LICValue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfDot11LIC':hpnicfDot11LIC,'hpnicfDot11LICConfigGroup':hpnicfDot11LICConfigGroup,'hpnicfDot11LICSerialNumber':hpnicfDot11LICSerialNumber,'hpnicfDot11LicApNumGroupSupport':hpnicfDot11LicApNumGroupSupport,'hpnicfDot11LICApNumGroup':hpnicfDot11LICApNumGroup,'hpnicfDot11LICApNumAttrTable':hpnicfDot11LICApNumAttrTable,'hpnicfDot11LICDefautAPNumPermit':hpnicfDot11LICDefautAPNumPermit,'hpnicfDot11LICCurrentAPNumPermit':hpnicfDot11LICCurrentAPNumPermit,'hpnicfDot11LICMaxAPNumPermit':hpnicfDot11LICMaxAPNumPermit,'hpnicfDot11LICApNumLicTable':hpnicfDot11LICApNumLicTable,'hpnicfDot11LICApNumLicEntry':hpnicfDot11LICApNumLicEntry,_G:hpnicfDot11LICLicenseKeyIndex,'hpnicfDot11LICLicenseKey':hpnicfDot11LICLicenseKey,'hpnicfDot11LICActivationKey':hpnicfDot11LICActivationKey,'hpnicfDot11LICApNum':hpnicfDot11LICApNum,'hpnicfDot11LICFeatureGroup':hpnicfDot11LICFeatureGroup,'hpnicfDot11LICFeatureAttrTable':hpnicfDot11LICFeatureAttrTable,'hpnicfDot11LICFeatureAttrEntry':hpnicfDot11LICFeatureAttrEntry,_H:hpnicfDot11LICAttrIndex,'hpnicfDot11LICAttrTypeName':hpnicfDot11LICAttrTypeName,'hpnicfDot11LICAttrDefVal':hpnicfDot11LICAttrDefVal,'hpnicfDot11LICAttrMaxVal':hpnicfDot11LICAttrMaxVal,'hpnicfDot11LICFeatureLicTable':hpnicfDot11LICFeatureLicTable,'hpnicfDot11LICFeatureLicEntry':hpnicfDot11LICFeatureLicEntry,_I:hpnicfDot11LICKeyIndex,'hpnicfDot11LICTypeName':hpnicfDot11LICTypeName,'hpnicfDot11LICKey':hpnicfDot11LICKey,'hpnicfDot11LICTimeLimit':hpnicfDot11LICTimeLimit,'hpnicfDot11LICValue':hpnicfDot11LICValue})