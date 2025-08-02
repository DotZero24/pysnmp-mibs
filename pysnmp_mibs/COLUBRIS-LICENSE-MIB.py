_K='colubrisLicenseMIBGroup'
_J='coLicenseFeatureRemainingDays'
_I='coLicenseFeatureEndingDate'
_H='coLicenseFeatureState'
_G='coLicenseFeatureName'
_F='coLicenseFeatureIndex'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='COLUBRIS-LICENSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisLicenseMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,29))
_ColubrisLicenseMIBObjects_ObjectIdentity=ObjectIdentity
colubrisLicenseMIBObjects=_ColubrisLicenseMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,29,1))
_CoLicenseGroup_ObjectIdentity=ObjectIdentity
coLicenseGroup=_CoLicenseGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,29,1,1))
_CoLicenseFeatureTable_Object=MibTable
coLicenseFeatureTable=_CoLicenseFeatureTable_Object((1,3,6,1,4,1,8744,5,29,1,1,1))
if mibBuilder.loadTexts:coLicenseFeatureTable.setStatus(_A)
_CoLicenseFeatureEntry_Object=MibTableRow
coLicenseFeatureEntry=_CoLicenseFeatureEntry_Object((1,3,6,1,4,1,8744,5,29,1,1,1,1))
coLicenseFeatureEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:coLicenseFeatureEntry.setStatus(_A)
class _CoLicenseFeatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoLicenseFeatureIndex_Type.__name__=_C
_CoLicenseFeatureIndex_Object=MibTableColumn
coLicenseFeatureIndex=_CoLicenseFeatureIndex_Object((1,3,6,1,4,1,8744,5,29,1,1,1,1,1),_CoLicenseFeatureIndex_Type())
coLicenseFeatureIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coLicenseFeatureIndex.setStatus(_A)
_CoLicenseFeatureName_Type=DisplayString
_CoLicenseFeatureName_Object=MibTableColumn
coLicenseFeatureName=_CoLicenseFeatureName_Object((1,3,6,1,4,1,8744,5,29,1,1,1,1,2),_CoLicenseFeatureName_Type())
coLicenseFeatureName.setMaxAccess(_D)
if mibBuilder.loadTexts:coLicenseFeatureName.setStatus(_A)
class _CoLicenseFeatureState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CoLicenseFeatureState_Type.__name__=_C
_CoLicenseFeatureState_Object=MibTableColumn
coLicenseFeatureState=_CoLicenseFeatureState_Object((1,3,6,1,4,1,8744,5,29,1,1,1,1,3),_CoLicenseFeatureState_Type())
coLicenseFeatureState.setMaxAccess(_D)
if mibBuilder.loadTexts:coLicenseFeatureState.setStatus(_A)
class _CoLicenseFeatureEndingDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_CoLicenseFeatureEndingDate_Type.__name__=_E
_CoLicenseFeatureEndingDate_Object=MibTableColumn
coLicenseFeatureEndingDate=_CoLicenseFeatureEndingDate_Object((1,3,6,1,4,1,8744,5,29,1,1,1,1,4),_CoLicenseFeatureEndingDate_Type())
coLicenseFeatureEndingDate.setMaxAccess(_D)
if mibBuilder.loadTexts:coLicenseFeatureEndingDate.setStatus(_A)
class _CoLicenseFeatureRemainingDays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_CoLicenseFeatureRemainingDays_Type.__name__=_C
_CoLicenseFeatureRemainingDays_Object=MibTableColumn
coLicenseFeatureRemainingDays=_CoLicenseFeatureRemainingDays_Object((1,3,6,1,4,1,8744,5,29,1,1,1,1,5),_CoLicenseFeatureRemainingDays_Type())
coLicenseFeatureRemainingDays.setMaxAccess(_D)
if mibBuilder.loadTexts:coLicenseFeatureRemainingDays.setStatus(_A)
_ColubrisLicenseMIBConformance_ObjectIdentity=ObjectIdentity
colubrisLicenseMIBConformance=_ColubrisLicenseMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,29,2))
_ColubrisLicenseMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisLicenseMIBCompliances=_ColubrisLicenseMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,29,2,1))
_ColubrisLicenseMIBGroups_ObjectIdentity=ObjectIdentity
colubrisLicenseMIBGroups=_ColubrisLicenseMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,29,2,2))
colubrisLicenseMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,29,2,2,1))
colubrisLicenseMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:colubrisLicenseMIBGroup.setStatus(_A)
colubrisLicenseMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,29,2,1,1))
colubrisLicenseMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:colubrisLicenseMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisLicenseMIB':colubrisLicenseMIB,'colubrisLicenseMIBObjects':colubrisLicenseMIBObjects,'coLicenseGroup':coLicenseGroup,'coLicenseFeatureTable':coLicenseFeatureTable,'coLicenseFeatureEntry':coLicenseFeatureEntry,_F:coLicenseFeatureIndex,_G:coLicenseFeatureName,_H:coLicenseFeatureState,_I:coLicenseFeatureEndingDate,_J:coLicenseFeatureRemainingDays,'colubrisLicenseMIBConformance':colubrisLicenseMIBConformance,'colubrisLicenseMIBCompliances':colubrisLicenseMIBCompliances,'colubrisLicenseMIBCompliance':colubrisLicenseMIBCompliance,'colubrisLicenseMIBGroups':colubrisLicenseMIBGroups,_K:colubrisLicenseMIBGroup})