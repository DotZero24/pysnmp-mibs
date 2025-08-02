_h='ceImageTagMIBGroup'
_g='ceImageInstallableMIBGroup'
_f='ceImageLocationMIBGroup'
_e='ceImageTagRowStatus'
_d='ceImageTagDate'
_c='ceImageTagListofInstIndex'
_b='ceImageInstallableRowStatus'
_a='ceImageInstallableDate'
_Z='ceImageInstallableRevisionVerNum'
_Y='ceImageInstallableMinorVerNumber'
_X='ceImageInstallableMajorVerNumber'
_W='ceImageInstallableStatus'
_V='ceImageInstallableName'
_U='ceImageInstallableType'
_T='ceImageLocationRunningStatus'
_S='ceImageLocation'
_R='ceImageDescription'
_Q='ceImageMedia'
_P='ceImageVersion'
_O='ceImageFeature'
_N='ceImageFamily'
_M='ceImageName'
_L='ceImageTagName'
_K='ceImageInstallableIndex'
_J='ceImageIndex'
_I='ciscoEnhancedImageMIBGroup'
_H='ceImageLocationIndex'
_G='not-accessible'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-create'
_C='read-only'
_B='CISCO-ENHANCED-IMAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CeImageInstallableStatus,CeImageInstallableType=mibBuilder.importSymbols('CISCO-IMAGE-TC','CeImageInstallableStatus','CeImageInstallableType')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_E,'PhysicalIndex',_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoEnhancedImageMIB=ModuleIdentity((1,3,6,1,4,1,9,9,249))
if mibBuilder.loadTexts:ciscoEnhancedImageMIB.setRevisions(('2005-01-06 00:00','2002-02-28 00:00'))
class MediaType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ram',1),('rom',2),('other',3)))
_CiscoEnhancedImageMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEnhancedImageMIBObjects=_CiscoEnhancedImageMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,249,1))
_CeImage_ObjectIdentity=ObjectIdentity
ceImage=_CeImage_ObjectIdentity((1,3,6,1,4,1,9,9,249,1,1))
_CeImageTable_Object=MibTable
ceImageTable=_CeImageTable_Object((1,3,6,1,4,1,9,9,249,1,1,1))
if mibBuilder.loadTexts:ceImageTable.setStatus(_A)
_CeImageEntry_Object=MibTableRow
ceImageEntry=_CeImageEntry_Object((1,3,6,1,4,1,9,9,249,1,1,1,1))
ceImageEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ceImageEntry.setStatus(_A)
_CeImageIndex_Type=PhysicalIndex
_CeImageIndex_Object=MibTableColumn
ceImageIndex=_CeImageIndex_Object((1,3,6,1,4,1,9,9,249,1,1,1,1,1),_CeImageIndex_Type())
ceImageIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ceImageIndex.setStatus(_A)
_CeImageName_Type=SnmpAdminString
_CeImageName_Object=MibTableColumn
ceImageName=_CeImageName_Object((1,3,6,1,4,1,9,9,249,1,1,1,1,2),_CeImageName_Type())
ceImageName.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageName.setStatus(_A)
_CeImageFamily_Type=SnmpAdminString
_CeImageFamily_Object=MibTableColumn
ceImageFamily=_CeImageFamily_Object((1,3,6,1,4,1,9,9,249,1,1,1,1,3),_CeImageFamily_Type())
ceImageFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageFamily.setStatus(_A)
_CeImageFeature_Type=SnmpAdminString
_CeImageFeature_Object=MibTableColumn
ceImageFeature=_CeImageFeature_Object((1,3,6,1,4,1,9,9,249,1,1,1,1,4),_CeImageFeature_Type())
ceImageFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageFeature.setStatus(_A)
_CeImageVersion_Type=SnmpAdminString
_CeImageVersion_Object=MibTableColumn
ceImageVersion=_CeImageVersion_Object((1,3,6,1,4,1,9,9,249,1,1,1,1,5),_CeImageVersion_Type())
ceImageVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageVersion.setStatus(_A)
_CeImageMedia_Type=MediaType
_CeImageMedia_Object=MibTableColumn
ceImageMedia=_CeImageMedia_Object((1,3,6,1,4,1,9,9,249,1,1,1,1,6),_CeImageMedia_Type())
ceImageMedia.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageMedia.setStatus(_A)
_CeImageDescription_Type=SnmpAdminString
_CeImageDescription_Object=MibTableColumn
ceImageDescription=_CeImageDescription_Object((1,3,6,1,4,1,9,9,249,1,1,1,1,7),_CeImageDescription_Type())
ceImageDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageDescription.setStatus(_A)
_CeImageInstallable_ObjectIdentity=ObjectIdentity
ceImageInstallable=_CeImageInstallable_ObjectIdentity((1,3,6,1,4,1,9,9,249,1,2))
_CeImageLocationTable_Object=MibTable
ceImageLocationTable=_CeImageLocationTable_Object((1,3,6,1,4,1,9,9,249,1,2,1))
if mibBuilder.loadTexts:ceImageLocationTable.setStatus(_A)
_CeImageLocationEntry_Object=MibTableRow
ceImageLocationEntry=_CeImageLocationEntry_Object((1,3,6,1,4,1,9,9,249,1,2,1,1))
ceImageLocationEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:ceImageLocationEntry.setStatus(_A)
_CeImageLocationIndex_Type=Unsigned32
_CeImageLocationIndex_Object=MibTableColumn
ceImageLocationIndex=_CeImageLocationIndex_Object((1,3,6,1,4,1,9,9,249,1,2,1,1,1),_CeImageLocationIndex_Type())
ceImageLocationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ceImageLocationIndex.setStatus(_A)
_CeImageLocation_Type=SnmpAdminString
_CeImageLocation_Object=MibTableColumn
ceImageLocation=_CeImageLocation_Object((1,3,6,1,4,1,9,9,249,1,2,1,1,2),_CeImageLocation_Type())
ceImageLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageLocation.setStatus(_A)
_CeImageLocationRunningStatus_Type=TruthValue
_CeImageLocationRunningStatus_Object=MibTableColumn
ceImageLocationRunningStatus=_CeImageLocationRunningStatus_Object((1,3,6,1,4,1,9,9,249,1,2,1,1,3),_CeImageLocationRunningStatus_Type())
ceImageLocationRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageLocationRunningStatus.setStatus(_A)
_CeImageInstallableTable_Object=MibTable
ceImageInstallableTable=_CeImageInstallableTable_Object((1,3,6,1,4,1,9,9,249,1,2,2))
if mibBuilder.loadTexts:ceImageInstallableTable.setStatus(_A)
_CeImageInstallableEntry_Object=MibTableRow
ceImageInstallableEntry=_CeImageInstallableEntry_Object((1,3,6,1,4,1,9,9,249,1,2,2,1))
ceImageInstallableEntry.setIndexNames((0,_E,_F),(0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:ceImageInstallableEntry.setStatus(_A)
_CeImageInstallableIndex_Type=Unsigned32
_CeImageInstallableIndex_Object=MibTableColumn
ceImageInstallableIndex=_CeImageInstallableIndex_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,1),_CeImageInstallableIndex_Type())
ceImageInstallableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ceImageInstallableIndex.setStatus(_A)
_CeImageInstallableType_Type=CeImageInstallableType
_CeImageInstallableType_Object=MibTableColumn
ceImageInstallableType=_CeImageInstallableType_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,2),_CeImageInstallableType_Type())
ceImageInstallableType.setMaxAccess(_D)
if mibBuilder.loadTexts:ceImageInstallableType.setStatus(_A)
_CeImageInstallableName_Type=SnmpAdminString
_CeImageInstallableName_Object=MibTableColumn
ceImageInstallableName=_CeImageInstallableName_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,3),_CeImageInstallableName_Type())
ceImageInstallableName.setMaxAccess(_D)
if mibBuilder.loadTexts:ceImageInstallableName.setStatus(_A)
_CeImageInstallableStatus_Type=CeImageInstallableStatus
_CeImageInstallableStatus_Object=MibTableColumn
ceImageInstallableStatus=_CeImageInstallableStatus_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,4),_CeImageInstallableStatus_Type())
ceImageInstallableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ceImageInstallableStatus.setStatus(_A)
_CeImageInstallableMajorVerNumber_Type=Unsigned32
_CeImageInstallableMajorVerNumber_Object=MibTableColumn
ceImageInstallableMajorVerNumber=_CeImageInstallableMajorVerNumber_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,5),_CeImageInstallableMajorVerNumber_Type())
ceImageInstallableMajorVerNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageInstallableMajorVerNumber.setStatus(_A)
_CeImageInstallableMinorVerNumber_Type=Unsigned32
_CeImageInstallableMinorVerNumber_Object=MibTableColumn
ceImageInstallableMinorVerNumber=_CeImageInstallableMinorVerNumber_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,6),_CeImageInstallableMinorVerNumber_Type())
ceImageInstallableMinorVerNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageInstallableMinorVerNumber.setStatus(_A)
_CeImageInstallableRevisionVerNum_Type=SnmpAdminString
_CeImageInstallableRevisionVerNum_Object=MibTableColumn
ceImageInstallableRevisionVerNum=_CeImageInstallableRevisionVerNum_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,7),_CeImageInstallableRevisionVerNum_Type())
ceImageInstallableRevisionVerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageInstallableRevisionVerNum.setStatus(_A)
_CeImageInstallableDate_Type=DateAndTime
_CeImageInstallableDate_Object=MibTableColumn
ceImageInstallableDate=_CeImageInstallableDate_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,8),_CeImageInstallableDate_Type())
ceImageInstallableDate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageInstallableDate.setStatus(_A)
_CeImageInstallableRowStatus_Type=RowStatus
_CeImageInstallableRowStatus_Object=MibTableColumn
ceImageInstallableRowStatus=_CeImageInstallableRowStatus_Object((1,3,6,1,4,1,9,9,249,1,2,2,1,9),_CeImageInstallableRowStatus_Type())
ceImageInstallableRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ceImageInstallableRowStatus.setStatus(_A)
_CeImageTags_ObjectIdentity=ObjectIdentity
ceImageTags=_CeImageTags_ObjectIdentity((1,3,6,1,4,1,9,9,249,1,3))
_CeImageTagTable_Object=MibTable
ceImageTagTable=_CeImageTagTable_Object((1,3,6,1,4,1,9,9,249,1,3,1))
if mibBuilder.loadTexts:ceImageTagTable.setStatus(_A)
_CeImageTagEntry_Object=MibTableRow
ceImageTagEntry=_CeImageTagEntry_Object((1,3,6,1,4,1,9,9,249,1,3,1,1))
ceImageTagEntry.setIndexNames((0,_E,_F),(0,_B,_H),(0,_B,_L))
if mibBuilder.loadTexts:ceImageTagEntry.setStatus(_A)
_CeImageTagName_Type=SnmpAdminString
_CeImageTagName_Object=MibTableColumn
ceImageTagName=_CeImageTagName_Object((1,3,6,1,4,1,9,9,249,1,3,1,1,1),_CeImageTagName_Type())
ceImageTagName.setMaxAccess(_G)
if mibBuilder.loadTexts:ceImageTagName.setStatus(_A)
_CeImageTagListofInstIndex_Type=SnmpAdminString
_CeImageTagListofInstIndex_Object=MibTableColumn
ceImageTagListofInstIndex=_CeImageTagListofInstIndex_Object((1,3,6,1,4,1,9,9,249,1,3,1,1,2),_CeImageTagListofInstIndex_Type())
ceImageTagListofInstIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageTagListofInstIndex.setStatus(_A)
_CeImageTagDate_Type=DateAndTime
_CeImageTagDate_Object=MibTableColumn
ceImageTagDate=_CeImageTagDate_Object((1,3,6,1,4,1,9,9,249,1,3,1,1,3),_CeImageTagDate_Type())
ceImageTagDate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceImageTagDate.setStatus(_A)
_CeImageTagRowStatus_Type=RowStatus
_CeImageTagRowStatus_Object=MibTableColumn
ceImageTagRowStatus=_CeImageTagRowStatus_Object((1,3,6,1,4,1,9,9,249,1,3,1,1,4),_CeImageTagRowStatus_Type())
ceImageTagRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ceImageTagRowStatus.setStatus(_A)
_CiscoEnhancedImageMIBConformance_ObjectIdentity=ObjectIdentity
ciscoEnhancedImageMIBConformance=_CiscoEnhancedImageMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,249,3))
_CiscoEnhancedImageMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEnhancedImageMIBCompliances=_CiscoEnhancedImageMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,249,3,1))
_CiscoEnhancedImageMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEnhancedImageMIBGroups=_CiscoEnhancedImageMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,249,3,2))
ciscoEnhancedImageMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,249,3,2,1))
ciscoEnhancedImageMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoEnhancedImageMIBGroup.setStatus(_A)
ceImageLocationMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,249,3,2,2))
ceImageLocationMIBGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ceImageLocationMIBGroup.setStatus(_A)
ceImageInstallableMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,249,3,2,3))
ceImageInstallableMIBGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ceImageInstallableMIBGroup.setStatus(_A)
ceImageTagMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,249,3,2,4))
ceImageTagMIBGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ceImageTagMIBGroup.setStatus(_A)
ciscoEnhancedImageMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,249,3,1,1))
ciscoEnhancedImageMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:ciscoEnhancedImageMIBCompliance.setStatus('deprecated')
ceImageMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,249,3,1,2))
ceImageMIBComplianceRev1.setObjects(*((_B,_I),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ceImageMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MediaType':MediaType,'ciscoEnhancedImageMIB':ciscoEnhancedImageMIB,'ciscoEnhancedImageMIBObjects':ciscoEnhancedImageMIBObjects,'ceImage':ceImage,'ceImageTable':ceImageTable,'ceImageEntry':ceImageEntry,_J:ceImageIndex,_M:ceImageName,_N:ceImageFamily,_O:ceImageFeature,_P:ceImageVersion,_Q:ceImageMedia,_R:ceImageDescription,'ceImageInstallable':ceImageInstallable,'ceImageLocationTable':ceImageLocationTable,'ceImageLocationEntry':ceImageLocationEntry,_H:ceImageLocationIndex,_S:ceImageLocation,_T:ceImageLocationRunningStatus,'ceImageInstallableTable':ceImageInstallableTable,'ceImageInstallableEntry':ceImageInstallableEntry,_K:ceImageInstallableIndex,_U:ceImageInstallableType,_V:ceImageInstallableName,_W:ceImageInstallableStatus,_X:ceImageInstallableMajorVerNumber,_Y:ceImageInstallableMinorVerNumber,_Z:ceImageInstallableRevisionVerNum,_a:ceImageInstallableDate,_b:ceImageInstallableRowStatus,'ceImageTags':ceImageTags,'ceImageTagTable':ceImageTagTable,'ceImageTagEntry':ceImageTagEntry,_L:ceImageTagName,_c:ceImageTagListofInstIndex,_d:ceImageTagDate,_e:ceImageTagRowStatus,'ciscoEnhancedImageMIBConformance':ciscoEnhancedImageMIBConformance,'ciscoEnhancedImageMIBCompliances':ciscoEnhancedImageMIBCompliances,'ciscoEnhancedImageMIBCompliance':ciscoEnhancedImageMIBCompliance,'ceImageMIBComplianceRev1':ceImageMIBComplianceRev1,'ciscoEnhancedImageMIBGroups':ciscoEnhancedImageMIBGroups,_I:ciscoEnhancedImageMIBGroup,_f:ceImageLocationMIBGroup,_g:ceImageInstallableMIBGroup,_h:ceImageTagMIBGroup})