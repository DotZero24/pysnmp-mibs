_D='mwLicenseTemplateTableIndex'
_C='MERU-CONFIG-LICENSE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlLicenseType,MwlSofwControllerType=mibBuilder.importSymbols('MERU-TC','MwlLicenseType','MwlSofwControllerType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigLicense=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,11))
_MwLicenseTemplateTable_Object=MibTable
mwLicenseTemplateTable=_MwLicenseTemplateTable_Object((1,3,6,1,4,1,15983,1,1,4,11,1))
if mibBuilder.loadTexts:mwLicenseTemplateTable.setStatus(_A)
_MwLicenseTemplateEntry_Object=MibTableRow
mwLicenseTemplateEntry=_MwLicenseTemplateEntry_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1))
mwLicenseTemplateEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mwLicenseTemplateEntry.setStatus(_A)
_MwLicenseTemplateTableIndex_Type=Integer32
_MwLicenseTemplateTableIndex_Object=MibTableColumn
mwLicenseTemplateTableIndex=_MwLicenseTemplateTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1,1),_MwLicenseTemplateTableIndex_Type())
mwLicenseTemplateTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mwLicenseTemplateTableIndex.setStatus(_A)
_MwLicenseTemplateExpiryDate_Type=DateAndTime
_MwLicenseTemplateExpiryDate_Object=MibTableColumn
mwLicenseTemplateExpiryDate=_MwLicenseTemplateExpiryDate_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1,2),_MwLicenseTemplateExpiryDate_Type())
mwLicenseTemplateExpiryDate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLicenseTemplateExpiryDate.setStatus(_A)
_MwLicenseTemplateFeatureName_Type=DisplayString
_MwLicenseTemplateFeatureName_Object=MibTableColumn
mwLicenseTemplateFeatureName=_MwLicenseTemplateFeatureName_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1,3),_MwLicenseTemplateFeatureName_Type())
mwLicenseTemplateFeatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLicenseTemplateFeatureName.setStatus(_A)
_MwLicenseTemplateLicenseType_Type=MwlLicenseType
_MwLicenseTemplateLicenseType_Object=MibTableColumn
mwLicenseTemplateLicenseType=_MwLicenseTemplateLicenseType_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1,4),_MwLicenseTemplateLicenseType_Type())
mwLicenseTemplateLicenseType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLicenseTemplateLicenseType.setStatus(_A)
_MwLicenseTemplateNumOfLicenses_Type=Unsigned32
_MwLicenseTemplateNumOfLicenses_Object=MibTableColumn
mwLicenseTemplateNumOfLicenses=_MwLicenseTemplateNumOfLicenses_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1,5),_MwLicenseTemplateNumOfLicenses_Type())
mwLicenseTemplateNumOfLicenses.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLicenseTemplateNumOfLicenses.setStatus(_A)
_MwLicenseTemplateControllerType_Type=MwlSofwControllerType
_MwLicenseTemplateControllerType_Object=MibTableColumn
mwLicenseTemplateControllerType=_MwLicenseTemplateControllerType_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1,6),_MwLicenseTemplateControllerType_Type())
mwLicenseTemplateControllerType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLicenseTemplateControllerType.setStatus(_A)
_MwLicenseTemplateLicensesInUsed_Type=Unsigned32
_MwLicenseTemplateLicensesInUsed_Object=MibTableColumn
mwLicenseTemplateLicensesInUsed=_MwLicenseTemplateLicensesInUsed_Object((1,3,6,1,4,1,15983,1,1,4,11,1,1,7),_MwLicenseTemplateLicensesInUsed_Type())
mwLicenseTemplateLicensesInUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLicenseTemplateLicensesInUsed.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mwConfigLicense':mwConfigLicense,'mwLicenseTemplateTable':mwLicenseTemplateTable,'mwLicenseTemplateEntry':mwLicenseTemplateEntry,_D:mwLicenseTemplateTableIndex,'mwLicenseTemplateExpiryDate':mwLicenseTemplateExpiryDate,'mwLicenseTemplateFeatureName':mwLicenseTemplateFeatureName,'mwLicenseTemplateLicenseType':mwLicenseTemplateLicenseType,'mwLicenseTemplateNumOfLicenses':mwLicenseTemplateNumOfLicenses,'mwLicenseTemplateControllerType':mwLicenseTemplateControllerType,'mwLicenseTemplateLicensesInUsed':mwLicenseTemplateLicensesInUsed})