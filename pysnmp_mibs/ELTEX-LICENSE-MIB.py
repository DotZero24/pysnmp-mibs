_F='not-accessible'
_E='eltexLicenseFeatureName'
_D='eltexLicenseInfoId'
_C='ELTEX-LICENSE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
eltexLicenseMIB=ModuleIdentity((1,3,6,1,4,1,35265,49))
if mibBuilder.loadTexts:eltexLicenseMIB.setRevisions(('2018-07-31 00:00',))
class EltexLicenseStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('activeAfterReboot',2),('inactiveAfterReboot',3),('deviceMismatching',4)))
_EltexLicenseMIBObjects_ObjectIdentity=ObjectIdentity
eltexLicenseMIBObjects=_EltexLicenseMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,49,1))
_EltexLicenseGeneral_ObjectIdentity=ObjectIdentity
eltexLicenseGeneral=_EltexLicenseGeneral_ObjectIdentity((1,3,6,1,4,1,35265,49,1,1))
_EltexLicenseInformation_ObjectIdentity=ObjectIdentity
eltexLicenseInformation=_EltexLicenseInformation_ObjectIdentity((1,3,6,1,4,1,35265,49,1,2))
_EltexLicenseInfoTable_Object=MibTable
eltexLicenseInfoTable=_EltexLicenseInfoTable_Object((1,3,6,1,4,1,35265,49,1,2,1))
if mibBuilder.loadTexts:eltexLicenseInfoTable.setStatus(_A)
_EltexLicenseInfoEntry_Object=MibTableRow
eltexLicenseInfoEntry=_EltexLicenseInfoEntry_Object((1,3,6,1,4,1,35265,49,1,2,1,1))
eltexLicenseInfoEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltexLicenseInfoEntry.setStatus(_A)
_EltexLicenseInfoId_Type=Unsigned32
_EltexLicenseInfoId_Object=MibTableColumn
eltexLicenseInfoId=_EltexLicenseInfoId_Object((1,3,6,1,4,1,35265,49,1,2,1,1,1),_EltexLicenseInfoId_Type())
eltexLicenseInfoId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexLicenseInfoId.setStatus(_A)
_EltexLicenseInfoFileName_Type=DisplayString
_EltexLicenseInfoFileName_Object=MibTableColumn
eltexLicenseInfoFileName=_EltexLicenseInfoFileName_Object((1,3,6,1,4,1,35265,49,1,2,1,1,2),_EltexLicenseInfoFileName_Type())
eltexLicenseInfoFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseInfoFileName.setStatus(_A)
_EltexLicenseInfoVersion_Type=Unsigned32
_EltexLicenseInfoVersion_Object=MibTableColumn
eltexLicenseInfoVersion=_EltexLicenseInfoVersion_Object((1,3,6,1,4,1,35265,49,1,2,1,1,3),_EltexLicenseInfoVersion_Type())
eltexLicenseInfoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseInfoVersion.setStatus(_A)
_EltexLicenseInfoStatus_Type=EltexLicenseStatus
_EltexLicenseInfoStatus_Object=MibTableColumn
eltexLicenseInfoStatus=_EltexLicenseInfoStatus_Object((1,3,6,1,4,1,35265,49,1,2,1,1,4),_EltexLicenseInfoStatus_Type())
eltexLicenseInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseInfoStatus.setStatus(_A)
_EltexLicenseInfoSerialNumber_Type=DisplayString
_EltexLicenseInfoSerialNumber_Object=MibTableColumn
eltexLicenseInfoSerialNumber=_EltexLicenseInfoSerialNumber_Object((1,3,6,1,4,1,35265,49,1,2,1,1,5),_EltexLicenseInfoSerialNumber_Type())
eltexLicenseInfoSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseInfoSerialNumber.setStatus(_A)
_EltexLicenseInfoMacAddress_Type=MacAddress
_EltexLicenseInfoMacAddress_Object=MibTableColumn
eltexLicenseInfoMacAddress=_EltexLicenseInfoMacAddress_Object((1,3,6,1,4,1,35265,49,1,2,1,1,6),_EltexLicenseInfoMacAddress_Type())
eltexLicenseInfoMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseInfoMacAddress.setStatus(_A)
_EltexLicenseInfoVendorName_Type=DisplayString
_EltexLicenseInfoVendorName_Object=MibTableColumn
eltexLicenseInfoVendorName=_EltexLicenseInfoVendorName_Object((1,3,6,1,4,1,35265,49,1,2,1,1,7),_EltexLicenseInfoVendorName_Type())
eltexLicenseInfoVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseInfoVendorName.setStatus(_A)
_EltexLicenseInfoDeviceName_Type=DisplayString
_EltexLicenseInfoDeviceName_Object=MibTableColumn
eltexLicenseInfoDeviceName=_EltexLicenseInfoDeviceName_Object((1,3,6,1,4,1,35265,49,1,2,1,1,8),_EltexLicenseInfoDeviceName_Type())
eltexLicenseInfoDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseInfoDeviceName.setStatus(_A)
_EltexLicenseFeature_ObjectIdentity=ObjectIdentity
eltexLicenseFeature=_EltexLicenseFeature_ObjectIdentity((1,3,6,1,4,1,35265,49,1,3))
_EltexLicenseFeatureTable_Object=MibTable
eltexLicenseFeatureTable=_EltexLicenseFeatureTable_Object((1,3,6,1,4,1,35265,49,1,3,1))
if mibBuilder.loadTexts:eltexLicenseFeatureTable.setStatus(_A)
_EltexLicenseFeatureEntry_Object=MibTableRow
eltexLicenseFeatureEntry=_EltexLicenseFeatureEntry_Object((1,3,6,1,4,1,35265,49,1,3,1,1))
eltexLicenseFeatureEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:eltexLicenseFeatureEntry.setStatus(_A)
_EltexLicenseFeatureName_Type=DisplayString
_EltexLicenseFeatureName_Object=MibTableColumn
eltexLicenseFeatureName=_EltexLicenseFeatureName_Object((1,3,6,1,4,1,35265,49,1,3,1,1,1),_EltexLicenseFeatureName_Type())
eltexLicenseFeatureName.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexLicenseFeatureName.setStatus(_A)
_EltexLicenseFeatureActive_Type=TruthValue
_EltexLicenseFeatureActive_Object=MibTableColumn
eltexLicenseFeatureActive=_EltexLicenseFeatureActive_Object((1,3,6,1,4,1,35265,49,1,3,1,1,2),_EltexLicenseFeatureActive_Type())
eltexLicenseFeatureActive.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseFeatureActive.setStatus(_A)
_EltexLicenseFeatureCountable_Type=TruthValue
_EltexLicenseFeatureCountable_Object=MibTableColumn
eltexLicenseFeatureCountable=_EltexLicenseFeatureCountable_Object((1,3,6,1,4,1,35265,49,1,3,1,1,3),_EltexLicenseFeatureCountable_Type())
eltexLicenseFeatureCountable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseFeatureCountable.setStatus(_A)
_EltexLicenseFeatureLicensesInstalled_Type=Unsigned32
_EltexLicenseFeatureLicensesInstalled_Object=MibTableColumn
eltexLicenseFeatureLicensesInstalled=_EltexLicenseFeatureLicensesInstalled_Object((1,3,6,1,4,1,35265,49,1,3,1,1,4),_EltexLicenseFeatureLicensesInstalled_Type())
eltexLicenseFeatureLicensesInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseFeatureLicensesInstalled.setStatus(_A)
_EltexLicenseFeatureLicensesUsed_Type=Unsigned32
_EltexLicenseFeatureLicensesUsed_Object=MibTableColumn
eltexLicenseFeatureLicensesUsed=_EltexLicenseFeatureLicensesUsed_Object((1,3,6,1,4,1,35265,49,1,3,1,1,5),_EltexLicenseFeatureLicensesUsed_Type())
eltexLicenseFeatureLicensesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseFeatureLicensesUsed.setStatus(_A)
_EltexLicenseFeatureListTable_Object=MibTable
eltexLicenseFeatureListTable=_EltexLicenseFeatureListTable_Object((1,3,6,1,4,1,35265,49,1,3,2))
if mibBuilder.loadTexts:eltexLicenseFeatureListTable.setStatus(_A)
_EltexLicenseFeatureListEntry_Object=MibTableRow
eltexLicenseFeatureListEntry=_EltexLicenseFeatureListEntry_Object((1,3,6,1,4,1,35265,49,1,3,2,1))
eltexLicenseFeatureListEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:eltexLicenseFeatureListEntry.setStatus(_A)
_EltexLicenseFeatureListCount_Type=Unsigned32
_EltexLicenseFeatureListCount_Object=MibTableColumn
eltexLicenseFeatureListCount=_EltexLicenseFeatureListCount_Object((1,3,6,1,4,1,35265,49,1,3,2,1,1),_EltexLicenseFeatureListCount_Type())
eltexLicenseFeatureListCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexLicenseFeatureListCount.setStatus(_A)
_EltexLicenseMIBNotifications_ObjectIdentity=ObjectIdentity
eltexLicenseMIBNotifications=_EltexLicenseMIBNotifications_ObjectIdentity((1,3,6,1,4,1,35265,49,2))
_EltexLicenseMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltexLicenseMIBNotificationsPrefix=_EltexLicenseMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,49,2,0))
_EltexLicenseMIBConformance_ObjectIdentity=ObjectIdentity
eltexLicenseMIBConformance=_EltexLicenseMIBConformance_ObjectIdentity((1,3,6,1,4,1,35265,49,3))
mibBuilder.exportSymbols(_C,**{'EltexLicenseStatus':EltexLicenseStatus,'eltexLicenseMIB':eltexLicenseMIB,'eltexLicenseMIBObjects':eltexLicenseMIBObjects,'eltexLicenseGeneral':eltexLicenseGeneral,'eltexLicenseInformation':eltexLicenseInformation,'eltexLicenseInfoTable':eltexLicenseInfoTable,'eltexLicenseInfoEntry':eltexLicenseInfoEntry,_D:eltexLicenseInfoId,'eltexLicenseInfoFileName':eltexLicenseInfoFileName,'eltexLicenseInfoVersion':eltexLicenseInfoVersion,'eltexLicenseInfoStatus':eltexLicenseInfoStatus,'eltexLicenseInfoSerialNumber':eltexLicenseInfoSerialNumber,'eltexLicenseInfoMacAddress':eltexLicenseInfoMacAddress,'eltexLicenseInfoVendorName':eltexLicenseInfoVendorName,'eltexLicenseInfoDeviceName':eltexLicenseInfoDeviceName,'eltexLicenseFeature':eltexLicenseFeature,'eltexLicenseFeatureTable':eltexLicenseFeatureTable,'eltexLicenseFeatureEntry':eltexLicenseFeatureEntry,_E:eltexLicenseFeatureName,'eltexLicenseFeatureActive':eltexLicenseFeatureActive,'eltexLicenseFeatureCountable':eltexLicenseFeatureCountable,'eltexLicenseFeatureLicensesInstalled':eltexLicenseFeatureLicensesInstalled,'eltexLicenseFeatureLicensesUsed':eltexLicenseFeatureLicensesUsed,'eltexLicenseFeatureListTable':eltexLicenseFeatureListTable,'eltexLicenseFeatureListEntry':eltexLicenseFeatureListEntry,'eltexLicenseFeatureListCount':eltexLicenseFeatureListCount,'eltexLicenseMIBNotifications':eltexLicenseMIBNotifications,'eltexLicenseMIBNotificationsPrefix':eltexLicenseMIBNotificationsPrefix,'eltexLicenseMIBConformance':eltexLicenseMIBConformance})