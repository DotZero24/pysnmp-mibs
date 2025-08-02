_I='h3cDot11LICKeyIndex'
_H='h3cDot11LICAttrIndex'
_G='h3cDot11LICLicenseKeyIndex'
_F='TruthValue'
_E='OctetString'
_D='H3C-DOT11-LIC-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cDot11,=mibBuilder.importSymbols('H3C-DOT11-REF-MIB','h3cDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
h3cDot11LIC=ModuleIdentity((1,3,6,1,4,1,2011,10,2,75,14))
if mibBuilder.loadTexts:h3cDot11LIC.setRevisions(('2012-04-25 18:00',))
_H3cDot11LICConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11LICConfigGroup=_H3cDot11LICConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,14,1))
class _H3cDot11LICSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11LICSerialNumber_Type.__name__=_E
_H3cDot11LICSerialNumber_Object=MibScalar
h3cDot11LICSerialNumber=_H3cDot11LICSerialNumber_Object((1,3,6,1,4,1,2011,10,2,75,14,1,1),_H3cDot11LICSerialNumber_Type())
h3cDot11LICSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICSerialNumber.setStatus(_A)
class _H3cDot11LicApNumGroupSupport_Type(TruthValue):defaultValue=2
_H3cDot11LicApNumGroupSupport_Type.__name__=_F
_H3cDot11LicApNumGroupSupport_Object=MibScalar
h3cDot11LicApNumGroupSupport=_H3cDot11LicApNumGroupSupport_Object((1,3,6,1,4,1,2011,10,2,75,14,1,2),_H3cDot11LicApNumGroupSupport_Type())
h3cDot11LicApNumGroupSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LicApNumGroupSupport.setStatus(_A)
_H3cDot11LICApNumGroup_ObjectIdentity=ObjectIdentity
h3cDot11LICApNumGroup=_H3cDot11LICApNumGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,14,2))
_H3cDot11LICApNumAttrTable_ObjectIdentity=ObjectIdentity
h3cDot11LICApNumAttrTable=_H3cDot11LICApNumAttrTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,14,2,1))
_H3cDot11LICDefautAPNumPermit_Type=Integer32
_H3cDot11LICDefautAPNumPermit_Object=MibScalar
h3cDot11LICDefautAPNumPermit=_H3cDot11LICDefautAPNumPermit_Object((1,3,6,1,4,1,2011,10,2,75,14,2,1,1),_H3cDot11LICDefautAPNumPermit_Type())
h3cDot11LICDefautAPNumPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICDefautAPNumPermit.setStatus(_A)
_H3cDot11LICCurrentAPNumPermit_Type=Integer32
_H3cDot11LICCurrentAPNumPermit_Object=MibScalar
h3cDot11LICCurrentAPNumPermit=_H3cDot11LICCurrentAPNumPermit_Object((1,3,6,1,4,1,2011,10,2,75,14,2,1,2),_H3cDot11LICCurrentAPNumPermit_Type())
h3cDot11LICCurrentAPNumPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICCurrentAPNumPermit.setStatus(_A)
_H3cDot11LICMaxAPNumPermit_Type=Integer32
_H3cDot11LICMaxAPNumPermit_Object=MibScalar
h3cDot11LICMaxAPNumPermit=_H3cDot11LICMaxAPNumPermit_Object((1,3,6,1,4,1,2011,10,2,75,14,2,1,3),_H3cDot11LICMaxAPNumPermit_Type())
h3cDot11LICMaxAPNumPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICMaxAPNumPermit.setStatus(_A)
_H3cDot11LICApNumLicTable_Object=MibTable
h3cDot11LICApNumLicTable=_H3cDot11LICApNumLicTable_Object((1,3,6,1,4,1,2011,10,2,75,14,2,2))
if mibBuilder.loadTexts:h3cDot11LICApNumLicTable.setStatus(_A)
_H3cDot11LICApNumLicEntry_Object=MibTableRow
h3cDot11LICApNumLicEntry=_H3cDot11LICApNumLicEntry_Object((1,3,6,1,4,1,2011,10,2,75,14,2,2,1))
h3cDot11LICApNumLicEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:h3cDot11LICApNumLicEntry.setStatus(_A)
class _H3cDot11LICLicenseKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDot11LICLicenseKeyIndex_Type.__name__=_C
_H3cDot11LICLicenseKeyIndex_Object=MibTableColumn
h3cDot11LICLicenseKeyIndex=_H3cDot11LICLicenseKeyIndex_Object((1,3,6,1,4,1,2011,10,2,75,14,2,2,1,1),_H3cDot11LICLicenseKeyIndex_Type())
h3cDot11LICLicenseKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICLicenseKeyIndex.setStatus(_A)
_H3cDot11LICLicenseKey_Type=OctetString
_H3cDot11LICLicenseKey_Object=MibTableColumn
h3cDot11LICLicenseKey=_H3cDot11LICLicenseKey_Object((1,3,6,1,4,1,2011,10,2,75,14,2,2,1,2),_H3cDot11LICLicenseKey_Type())
h3cDot11LICLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICLicenseKey.setStatus(_A)
_H3cDot11LICActivationKey_Type=OctetString
_H3cDot11LICActivationKey_Object=MibTableColumn
h3cDot11LICActivationKey=_H3cDot11LICActivationKey_Object((1,3,6,1,4,1,2011,10,2,75,14,2,2,1,3),_H3cDot11LICActivationKey_Type())
h3cDot11LICActivationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICActivationKey.setStatus(_A)
_H3cDot11LICApNum_Type=Integer32
_H3cDot11LICApNum_Object=MibTableColumn
h3cDot11LICApNum=_H3cDot11LICApNum_Object((1,3,6,1,4,1,2011,10,2,75,14,2,2,1,4),_H3cDot11LICApNum_Type())
h3cDot11LICApNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICApNum.setStatus(_A)
_H3cDot11LICFeatureGroup_ObjectIdentity=ObjectIdentity
h3cDot11LICFeatureGroup=_H3cDot11LICFeatureGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,14,3))
_H3cDot11LICFeatureAttrTable_Object=MibTable
h3cDot11LICFeatureAttrTable=_H3cDot11LICFeatureAttrTable_Object((1,3,6,1,4,1,2011,10,2,75,14,3,1))
if mibBuilder.loadTexts:h3cDot11LICFeatureAttrTable.setStatus(_A)
_H3cDot11LICFeatureAttrEntry_Object=MibTableRow
h3cDot11LICFeatureAttrEntry=_H3cDot11LICFeatureAttrEntry_Object((1,3,6,1,4,1,2011,10,2,75,14,3,1,1))
h3cDot11LICFeatureAttrEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cDot11LICFeatureAttrEntry.setStatus(_A)
class _H3cDot11LICAttrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDot11LICAttrIndex_Type.__name__=_C
_H3cDot11LICAttrIndex_Object=MibTableColumn
h3cDot11LICAttrIndex=_H3cDot11LICAttrIndex_Object((1,3,6,1,4,1,2011,10,2,75,14,3,1,1,1),_H3cDot11LICAttrIndex_Type())
h3cDot11LICAttrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICAttrIndex.setStatus(_A)
_H3cDot11LICAttrTypeName_Type=OctetString
_H3cDot11LICAttrTypeName_Object=MibTableColumn
h3cDot11LICAttrTypeName=_H3cDot11LICAttrTypeName_Object((1,3,6,1,4,1,2011,10,2,75,14,3,1,1,2),_H3cDot11LICAttrTypeName_Type())
h3cDot11LICAttrTypeName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICAttrTypeName.setStatus(_A)
_H3cDot11LICAttrDefVal_Type=Integer32
_H3cDot11LICAttrDefVal_Object=MibTableColumn
h3cDot11LICAttrDefVal=_H3cDot11LICAttrDefVal_Object((1,3,6,1,4,1,2011,10,2,75,14,3,1,1,3),_H3cDot11LICAttrDefVal_Type())
h3cDot11LICAttrDefVal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICAttrDefVal.setStatus(_A)
_H3cDot11LICAttrMaxVal_Type=Integer32
_H3cDot11LICAttrMaxVal_Object=MibTableColumn
h3cDot11LICAttrMaxVal=_H3cDot11LICAttrMaxVal_Object((1,3,6,1,4,1,2011,10,2,75,14,3,1,1,4),_H3cDot11LICAttrMaxVal_Type())
h3cDot11LICAttrMaxVal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICAttrMaxVal.setStatus(_A)
_H3cDot11LICFeatureLicTable_Object=MibTable
h3cDot11LICFeatureLicTable=_H3cDot11LICFeatureLicTable_Object((1,3,6,1,4,1,2011,10,2,75,14,3,2))
if mibBuilder.loadTexts:h3cDot11LICFeatureLicTable.setStatus(_A)
_H3cDot11LICFeatureLicEntry_Object=MibTableRow
h3cDot11LICFeatureLicEntry=_H3cDot11LICFeatureLicEntry_Object((1,3,6,1,4,1,2011,10,2,75,14,3,2,1))
h3cDot11LICFeatureLicEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cDot11LICFeatureLicEntry.setStatus(_A)
class _H3cDot11LICKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDot11LICKeyIndex_Type.__name__=_C
_H3cDot11LICKeyIndex_Object=MibTableColumn
h3cDot11LICKeyIndex=_H3cDot11LICKeyIndex_Object((1,3,6,1,4,1,2011,10,2,75,14,3,2,1,1),_H3cDot11LICKeyIndex_Type())
h3cDot11LICKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICKeyIndex.setStatus(_A)
_H3cDot11LICTypeName_Type=OctetString
_H3cDot11LICTypeName_Object=MibTableColumn
h3cDot11LICTypeName=_H3cDot11LICTypeName_Object((1,3,6,1,4,1,2011,10,2,75,14,3,2,1,2),_H3cDot11LICTypeName_Type())
h3cDot11LICTypeName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICTypeName.setStatus(_A)
_H3cDot11LICKey_Type=OctetString
_H3cDot11LICKey_Object=MibTableColumn
h3cDot11LICKey=_H3cDot11LICKey_Object((1,3,6,1,4,1,2011,10,2,75,14,3,2,1,3),_H3cDot11LICKey_Type())
h3cDot11LICKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICKey.setStatus(_A)
_H3cDot11LICTimeLimit_Type=Integer32
_H3cDot11LICTimeLimit_Object=MibTableColumn
h3cDot11LICTimeLimit=_H3cDot11LICTimeLimit_Object((1,3,6,1,4,1,2011,10,2,75,14,3,2,1,4),_H3cDot11LICTimeLimit_Type())
h3cDot11LICTimeLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICTimeLimit.setStatus(_A)
_H3cDot11LICValue_Type=Integer32
_H3cDot11LICValue_Object=MibTableColumn
h3cDot11LICValue=_H3cDot11LICValue_Object((1,3,6,1,4,1,2011,10,2,75,14,3,2,1,5),_H3cDot11LICValue_Type())
h3cDot11LICValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LICValue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cDot11LIC':h3cDot11LIC,'h3cDot11LICConfigGroup':h3cDot11LICConfigGroup,'h3cDot11LICSerialNumber':h3cDot11LICSerialNumber,'h3cDot11LicApNumGroupSupport':h3cDot11LicApNumGroupSupport,'h3cDot11LICApNumGroup':h3cDot11LICApNumGroup,'h3cDot11LICApNumAttrTable':h3cDot11LICApNumAttrTable,'h3cDot11LICDefautAPNumPermit':h3cDot11LICDefautAPNumPermit,'h3cDot11LICCurrentAPNumPermit':h3cDot11LICCurrentAPNumPermit,'h3cDot11LICMaxAPNumPermit':h3cDot11LICMaxAPNumPermit,'h3cDot11LICApNumLicTable':h3cDot11LICApNumLicTable,'h3cDot11LICApNumLicEntry':h3cDot11LICApNumLicEntry,_G:h3cDot11LICLicenseKeyIndex,'h3cDot11LICLicenseKey':h3cDot11LICLicenseKey,'h3cDot11LICActivationKey':h3cDot11LICActivationKey,'h3cDot11LICApNum':h3cDot11LICApNum,'h3cDot11LICFeatureGroup':h3cDot11LICFeatureGroup,'h3cDot11LICFeatureAttrTable':h3cDot11LICFeatureAttrTable,'h3cDot11LICFeatureAttrEntry':h3cDot11LICFeatureAttrEntry,_H:h3cDot11LICAttrIndex,'h3cDot11LICAttrTypeName':h3cDot11LICAttrTypeName,'h3cDot11LICAttrDefVal':h3cDot11LICAttrDefVal,'h3cDot11LICAttrMaxVal':h3cDot11LICAttrMaxVal,'h3cDot11LICFeatureLicTable':h3cDot11LICFeatureLicTable,'h3cDot11LICFeatureLicEntry':h3cDot11LICFeatureLicEntry,_I:h3cDot11LICKeyIndex,'h3cDot11LICTypeName':h3cDot11LICTypeName,'h3cDot11LICKey':h3cDot11LICKey,'h3cDot11LICTimeLimit':h3cDot11LICTimeLimit,'h3cDot11LICValue':h3cDot11LICValue})