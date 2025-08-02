_J='licenseFeatureIndex'
_I='licenseStackId'
_H='licenseIndex'
_G='baseLicenseStackId'
_F='Integer32'
_E='not-accessible'
_D='read-write'
_C='AT-LICENSE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
license=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,22))
if mibBuilder.loadTexts:license.setRevisions(('2008-10-05 00:00',))
_BaseLicenseTable_Object=MibTable
baseLicenseTable=_BaseLicenseTable_Object((1,3,6,1,4,1,207,8,4,4,3,22,1))
if mibBuilder.loadTexts:baseLicenseTable.setStatus(_A)
_BaseLicenseEntry_Object=MibTableRow
baseLicenseEntry=_BaseLicenseEntry_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1))
baseLicenseEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:baseLicenseEntry.setStatus(_A)
_BaseLicenseStackId_Type=Integer32
_BaseLicenseStackId_Object=MibTableColumn
baseLicenseStackId=_BaseLicenseStackId_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1,1),_BaseLicenseStackId_Type())
baseLicenseStackId.setMaxAccess(_E)
if mibBuilder.loadTexts:baseLicenseStackId.setStatus(_A)
_BaseLicenseName_Type=DisplayString
_BaseLicenseName_Object=MibTableColumn
baseLicenseName=_BaseLicenseName_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1,2),_BaseLicenseName_Type())
baseLicenseName.setMaxAccess(_B)
if mibBuilder.loadTexts:baseLicenseName.setStatus(_A)
_BaseLicenseQuantity_Type=Integer32
_BaseLicenseQuantity_Object=MibTableColumn
baseLicenseQuantity=_BaseLicenseQuantity_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1,3),_BaseLicenseQuantity_Type())
baseLicenseQuantity.setMaxAccess(_B)
if mibBuilder.loadTexts:baseLicenseQuantity.setStatus(_A)
_BaseLicenseType_Type=DisplayString
_BaseLicenseType_Object=MibTableColumn
baseLicenseType=_BaseLicenseType_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1,4),_BaseLicenseType_Type())
baseLicenseType.setMaxAccess(_B)
if mibBuilder.loadTexts:baseLicenseType.setStatus(_A)
_BaseLicenseIssueDate_Type=DisplayString
_BaseLicenseIssueDate_Object=MibTableColumn
baseLicenseIssueDate=_BaseLicenseIssueDate_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1,5),_BaseLicenseIssueDate_Type())
baseLicenseIssueDate.setMaxAccess(_B)
if mibBuilder.loadTexts:baseLicenseIssueDate.setStatus(_A)
_BaseLicenseExpiryDate_Type=DisplayString
_BaseLicenseExpiryDate_Object=MibTableColumn
baseLicenseExpiryDate=_BaseLicenseExpiryDate_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1,6),_BaseLicenseExpiryDate_Type())
baseLicenseExpiryDate.setMaxAccess(_B)
if mibBuilder.loadTexts:baseLicenseExpiryDate.setStatus(_A)
_BaseLicenseFeatures_Type=OctetString
_BaseLicenseFeatures_Object=MibTableColumn
baseLicenseFeatures=_BaseLicenseFeatures_Object((1,3,6,1,4,1,207,8,4,4,3,22,1,1,7),_BaseLicenseFeatures_Type())
baseLicenseFeatures.setMaxAccess(_B)
if mibBuilder.loadTexts:baseLicenseFeatures.setStatus(_A)
_LicenseTable_Object=MibTable
licenseTable=_LicenseTable_Object((1,3,6,1,4,1,207,8,4,4,3,22,2))
if mibBuilder.loadTexts:licenseTable.setStatus(_A)
_LicenseEntry_Object=MibTableRow
licenseEntry=_LicenseEntry_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1))
licenseEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:licenseEntry.setStatus(_A)
_LicenseStackId_Type=Integer32
_LicenseStackId_Object=MibTableColumn
licenseStackId=_LicenseStackId_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,1),_LicenseStackId_Type())
licenseStackId.setMaxAccess(_E)
if mibBuilder.loadTexts:licenseStackId.setStatus(_A)
_LicenseIndex_Type=Integer32
_LicenseIndex_Object=MibTableColumn
licenseIndex=_LicenseIndex_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,2),_LicenseIndex_Type())
licenseIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:licenseIndex.setStatus(_A)
_LicenseName_Type=DisplayString
_LicenseName_Object=MibTableColumn
licenseName=_LicenseName_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,3),_LicenseName_Type())
licenseName.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseName.setStatus(_A)
_LicenseCustomer_Type=DisplayString
_LicenseCustomer_Object=MibTableColumn
licenseCustomer=_LicenseCustomer_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,4),_LicenseCustomer_Type())
licenseCustomer.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseCustomer.setStatus(_A)
_LicenseQuantity_Type=Integer32
_LicenseQuantity_Object=MibTableColumn
licenseQuantity=_LicenseQuantity_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,5),_LicenseQuantity_Type())
licenseQuantity.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseQuantity.setStatus(_A)
_LicenseType_Type=DisplayString
_LicenseType_Object=MibTableColumn
licenseType=_LicenseType_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,6),_LicenseType_Type())
licenseType.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseType.setStatus(_A)
_LicenseIssueDate_Type=DisplayString
_LicenseIssueDate_Object=MibTableColumn
licenseIssueDate=_LicenseIssueDate_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,7),_LicenseIssueDate_Type())
licenseIssueDate.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseIssueDate.setStatus(_A)
_LicenseExpiryDate_Type=DisplayString
_LicenseExpiryDate_Object=MibTableColumn
licenseExpiryDate=_LicenseExpiryDate_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,8),_LicenseExpiryDate_Type())
licenseExpiryDate.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseExpiryDate.setStatus(_A)
_LicenseFeatures_Type=OctetString
_LicenseFeatures_Object=MibTableColumn
licenseFeatures=_LicenseFeatures_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,9),_LicenseFeatures_Type())
licenseFeatures.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseFeatures.setStatus(_A)
_LicenseRowStatus_Type=RowStatus
_LicenseRowStatus_Object=MibTableColumn
licenseRowStatus=_LicenseRowStatus_Object((1,3,6,1,4,1,207,8,4,4,3,22,2,1,10),_LicenseRowStatus_Type())
licenseRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:licenseRowStatus.setStatus(_A)
_LicenseFeatureTable_Object=MibTable
licenseFeatureTable=_LicenseFeatureTable_Object((1,3,6,1,4,1,207,8,4,4,3,22,3))
if mibBuilder.loadTexts:licenseFeatureTable.setStatus(_A)
_LicenseFeatureEntry_Object=MibTableRow
licenseFeatureEntry=_LicenseFeatureEntry_Object((1,3,6,1,4,1,207,8,4,4,3,22,3,1))
licenseFeatureEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:licenseFeatureEntry.setStatus(_A)
_LicenseFeatureIndex_Type=Integer32
_LicenseFeatureIndex_Object=MibTableColumn
licenseFeatureIndex=_LicenseFeatureIndex_Object((1,3,6,1,4,1,207,8,4,4,3,22,3,1,1),_LicenseFeatureIndex_Type())
licenseFeatureIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:licenseFeatureIndex.setStatus(_A)
_LicenseFeatureName_Type=DisplayString
_LicenseFeatureName_Object=MibTableColumn
licenseFeatureName=_LicenseFeatureName_Object((1,3,6,1,4,1,207,8,4,4,3,22,3,1,2),_LicenseFeatureName_Type())
licenseFeatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseFeatureName.setStatus(_A)
_LicenseFeatureStkMembers_Type=OctetString
_LicenseFeatureStkMembers_Object=MibTableColumn
licenseFeatureStkMembers=_LicenseFeatureStkMembers_Object((1,3,6,1,4,1,207,8,4,4,3,22,3,1,3),_LicenseFeatureStkMembers_Type())
licenseFeatureStkMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseFeatureStkMembers.setStatus(_A)
_LicenseNew_ObjectIdentity=ObjectIdentity
licenseNew=_LicenseNew_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,22,4))
class _LicenseNewStackId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LicenseNewStackId_Type.__name__=_F
_LicenseNewStackId_Object=MibScalar
licenseNewStackId=_LicenseNewStackId_Object((1,3,6,1,4,1,207,8,4,4,3,22,4,1),_LicenseNewStackId_Type())
licenseNewStackId.setMaxAccess(_D)
if mibBuilder.loadTexts:licenseNewStackId.setStatus(_A)
_LicenseNewName_Type=DisplayString
_LicenseNewName_Object=MibScalar
licenseNewName=_LicenseNewName_Object((1,3,6,1,4,1,207,8,4,4,3,22,4,2),_LicenseNewName_Type())
licenseNewName.setMaxAccess(_D)
if mibBuilder.loadTexts:licenseNewName.setStatus(_A)
_LicenseNewKey_Type=DisplayString
_LicenseNewKey_Object=MibScalar
licenseNewKey=_LicenseNewKey_Object((1,3,6,1,4,1,207,8,4,4,3,22,4,3),_LicenseNewKey_Type())
licenseNewKey.setMaxAccess(_D)
if mibBuilder.loadTexts:licenseNewKey.setStatus(_A)
_LicenseNewInstall_Type=TruthValue
_LicenseNewInstall_Object=MibScalar
licenseNewInstall=_LicenseNewInstall_Object((1,3,6,1,4,1,207,8,4,4,3,22,4,4),_LicenseNewInstall_Type())
licenseNewInstall.setMaxAccess(_D)
if mibBuilder.loadTexts:licenseNewInstall.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'license':license,'baseLicenseTable':baseLicenseTable,'baseLicenseEntry':baseLicenseEntry,_G:baseLicenseStackId,'baseLicenseName':baseLicenseName,'baseLicenseQuantity':baseLicenseQuantity,'baseLicenseType':baseLicenseType,'baseLicenseIssueDate':baseLicenseIssueDate,'baseLicenseExpiryDate':baseLicenseExpiryDate,'baseLicenseFeatures':baseLicenseFeatures,'licenseTable':licenseTable,'licenseEntry':licenseEntry,_I:licenseStackId,_H:licenseIndex,'licenseName':licenseName,'licenseCustomer':licenseCustomer,'licenseQuantity':licenseQuantity,'licenseType':licenseType,'licenseIssueDate':licenseIssueDate,'licenseExpiryDate':licenseExpiryDate,'licenseFeatures':licenseFeatures,'licenseRowStatus':licenseRowStatus,'licenseFeatureTable':licenseFeatureTable,'licenseFeatureEntry':licenseFeatureEntry,_J:licenseFeatureIndex,'licenseFeatureName':licenseFeatureName,'licenseFeatureStkMembers':licenseFeatureStkMembers,'licenseNew':licenseNew,'licenseNewStackId':licenseNewStackId,'licenseNewName':licenseNewName,'licenseNewKey':licenseNewKey,'licenseNewInstall':licenseNewInstall})