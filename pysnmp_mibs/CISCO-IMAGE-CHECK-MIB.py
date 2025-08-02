_S='ciscoImgChkResultsGroup'
_R='ciscoImageCheckOpGroup'
_Q='ciscoImgChkInCompDescr'
_P='ciscoImgChkCapabilityReq'
_O='ciscoImgChkCapabilityName'
_N='ciscoImgChkFeatureName'
_M='ciscoImageCheckEntryStatus'
_L='ciscoImageCheckStatus'
_K='ciscoImageCheckImageName'
_J='ciscoImgChkCapabIndex'
_I='ciscoImgChkFeatureIndex'
_H='read-create'
_G='not-accessible'
_F='ciscoImageCheckSerialNum'
_E='read-only'
_D='SnmpAdminString'
_C='Integer32'
_B='CISCO-IMAGE-CHECK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoImageCheckMIB=ModuleIdentity((1,3,6,1,4,1,9,9,99990))
_CiscoImageCheckMIBObjects_ObjectIdentity=ObjectIdentity
ciscoImageCheckMIBObjects=_CiscoImageCheckMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,99990,1))
_CiscoImageCheck_ObjectIdentity=ObjectIdentity
ciscoImageCheck=_CiscoImageCheck_ObjectIdentity((1,3,6,1,4,1,9,9,99990,1,1))
_CiscoImageCheckOpTable_Object=MibTable
ciscoImageCheckOpTable=_CiscoImageCheckOpTable_Object((1,3,6,1,4,1,9,9,99990,1,1,1))
if mibBuilder.loadTexts:ciscoImageCheckOpTable.setStatus(_A)
_CiscoImageCheckOpEntry_Object=MibTableRow
ciscoImageCheckOpEntry=_CiscoImageCheckOpEntry_Object((1,3,6,1,4,1,9,9,99990,1,1,1,1))
ciscoImageCheckOpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciscoImageCheckOpEntry.setStatus(_A)
class _CiscoImageCheckSerialNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoImageCheckSerialNum_Type.__name__=_C
_CiscoImageCheckSerialNum_Object=MibTableColumn
ciscoImageCheckSerialNum=_CiscoImageCheckSerialNum_Object((1,3,6,1,4,1,9,9,99990,1,1,1,1,1),_CiscoImageCheckSerialNum_Type())
ciscoImageCheckSerialNum.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoImageCheckSerialNum.setStatus(_A)
class _CiscoImageCheckImageName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiscoImageCheckImageName_Type.__name__=_D
_CiscoImageCheckImageName_Object=MibTableColumn
ciscoImageCheckImageName=_CiscoImageCheckImageName_Object((1,3,6,1,4,1,9,9,99990,1,1,1,1,2),_CiscoImageCheckImageName_Type())
ciscoImageCheckImageName.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoImageCheckImageName.setStatus(_A)
class _CiscoImageCheckStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',1),('inProgress',2),('inCompatLoose',3),('inCompatStrict',4),('compatible',5),('noStandby',6),('pssErr',7),('extractFail',8),('fileParseErr',9),('getIncompatErr',10)))
_CiscoImageCheckStatus_Type.__name__=_C
_CiscoImageCheckStatus_Object=MibTableColumn
ciscoImageCheckStatus=_CiscoImageCheckStatus_Object((1,3,6,1,4,1,9,9,99990,1,1,1,1,3),_CiscoImageCheckStatus_Type())
ciscoImageCheckStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoImageCheckStatus.setStatus(_A)
_CiscoImageCheckEntryStatus_Type=RowStatus
_CiscoImageCheckEntryStatus_Object=MibTableColumn
ciscoImageCheckEntryStatus=_CiscoImageCheckEntryStatus_Object((1,3,6,1,4,1,9,9,99990,1,1,1,1,4),_CiscoImageCheckEntryStatus_Type())
ciscoImageCheckEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoImageCheckEntryStatus.setStatus(_A)
_CiscoImgChkResultsTable_Object=MibTable
ciscoImgChkResultsTable=_CiscoImgChkResultsTable_Object((1,3,6,1,4,1,9,9,99990,1,1,2))
if mibBuilder.loadTexts:ciscoImgChkResultsTable.setStatus(_A)
_CiscoImgChkResultsEntry_Object=MibTableRow
ciscoImgChkResultsEntry=_CiscoImgChkResultsEntry_Object((1,3,6,1,4,1,9,9,99990,1,1,2,1))
ciscoImgChkResultsEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:ciscoImgChkResultsEntry.setStatus(_A)
class _CiscoImgChkFeatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiscoImgChkFeatureIndex_Type.__name__=_C
_CiscoImgChkFeatureIndex_Object=MibTableColumn
ciscoImgChkFeatureIndex=_CiscoImgChkFeatureIndex_Object((1,3,6,1,4,1,9,9,99990,1,1,2,1,1),_CiscoImgChkFeatureIndex_Type())
ciscoImgChkFeatureIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoImgChkFeatureIndex.setStatus(_A)
class _CiscoImgChkCapabIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiscoImgChkCapabIndex_Type.__name__=_C
_CiscoImgChkCapabIndex_Object=MibTableColumn
ciscoImgChkCapabIndex=_CiscoImgChkCapabIndex_Object((1,3,6,1,4,1,9,9,99990,1,1,2,1,2),_CiscoImgChkCapabIndex_Type())
ciscoImgChkCapabIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoImgChkCapabIndex.setStatus(_A)
class _CiscoImgChkFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiscoImgChkFeatureName_Type.__name__=_D
_CiscoImgChkFeatureName_Object=MibTableColumn
ciscoImgChkFeatureName=_CiscoImgChkFeatureName_Object((1,3,6,1,4,1,9,9,99990,1,1,2,1,3),_CiscoImgChkFeatureName_Type())
ciscoImgChkFeatureName.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoImgChkFeatureName.setStatus(_A)
class _CiscoImgChkCapabilityName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CiscoImgChkCapabilityName_Type.__name__=_D
_CiscoImgChkCapabilityName_Object=MibTableColumn
ciscoImgChkCapabilityName=_CiscoImgChkCapabilityName_Object((1,3,6,1,4,1,9,9,99990,1,1,2,1,4),_CiscoImgChkCapabilityName_Type())
ciscoImgChkCapabilityName.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoImgChkCapabilityName.setStatus(_A)
class _CiscoImgChkCapabilityReq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('loose',2)))
_CiscoImgChkCapabilityReq_Type.__name__=_C
_CiscoImgChkCapabilityReq_Object=MibTableColumn
ciscoImgChkCapabilityReq=_CiscoImgChkCapabilityReq_Object((1,3,6,1,4,1,9,9,99990,1,1,2,1,5),_CiscoImgChkCapabilityReq_Type())
ciscoImgChkCapabilityReq.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoImgChkCapabilityReq.setStatus(_A)
class _CiscoImgChkInCompDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiscoImgChkInCompDescr_Type.__name__=_D
_CiscoImgChkInCompDescr_Object=MibTableColumn
ciscoImgChkInCompDescr=_CiscoImgChkInCompDescr_Object((1,3,6,1,4,1,9,9,99990,1,1,2,1,6),_CiscoImgChkInCompDescr_Type())
ciscoImgChkInCompDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoImgChkInCompDescr.setStatus(_A)
_CiscoImageCheckMIBConformance_ObjectIdentity=ObjectIdentity
ciscoImageCheckMIBConformance=_CiscoImageCheckMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,99990,2))
_CiscoImageCheckMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoImageCheckMIBCompliances=_CiscoImageCheckMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,99990,2,1))
_CiscoImageCheckMIBGroups_ObjectIdentity=ObjectIdentity
ciscoImageCheckMIBGroups=_CiscoImageCheckMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,99990,2,2))
ciscoImageCheckOpGroup=ObjectGroup((1,3,6,1,4,1,9,9,99990,2,2,1))
ciscoImageCheckOpGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoImageCheckOpGroup.setStatus(_A)
ciscoImgChkResultsGroup=ObjectGroup((1,3,6,1,4,1,9,9,99990,2,2,2))
ciscoImgChkResultsGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoImgChkResultsGroup.setStatus(_A)
ciscoImageCheckMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,99990,2,1,1))
ciscoImageCheckMIBCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoImageCheckMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoImageCheckMIB':ciscoImageCheckMIB,'ciscoImageCheckMIBObjects':ciscoImageCheckMIBObjects,'ciscoImageCheck':ciscoImageCheck,'ciscoImageCheckOpTable':ciscoImageCheckOpTable,'ciscoImageCheckOpEntry':ciscoImageCheckOpEntry,_F:ciscoImageCheckSerialNum,_K:ciscoImageCheckImageName,_L:ciscoImageCheckStatus,_M:ciscoImageCheckEntryStatus,'ciscoImgChkResultsTable':ciscoImgChkResultsTable,'ciscoImgChkResultsEntry':ciscoImgChkResultsEntry,_I:ciscoImgChkFeatureIndex,_J:ciscoImgChkCapabIndex,_N:ciscoImgChkFeatureName,_O:ciscoImgChkCapabilityName,_P:ciscoImgChkCapabilityReq,_Q:ciscoImgChkInCompDescr,'ciscoImageCheckMIBConformance':ciscoImageCheckMIBConformance,'ciscoImageCheckMIBCompliances':ciscoImageCheckMIBCompliances,'ciscoImageCheckMIBCompliance':ciscoImageCheckMIBCompliance,'ciscoImageCheckMIBGroups':ciscoImageCheckMIBGroups,_R:ciscoImageCheckOpGroup,_S:ciscoImgChkResultsGroup})