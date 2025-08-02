_AB='cwrComplianceRadioDuplexorGroup'
_AA='cwrComplianceRadioLEDGroup'
_A9='cwrComplianceRadioImageGroup'
_A8='cwrComplianceRadioRFGroup'
_A7='cwrDuplexorSerialNumber'
_A6='cwrDuplexorVendorName'
_A5='cwrDuplexorCLEICode'
_A4='cwrDuplexorReceivePassband'
_A3='cwrDuplexorHiPassbandRange'
_A2='cwrDuplexorLoPassbandRange'
_A1='cwrDuplexorCiscoPartNumber'
_A0='cwrLedCurrentColor'
_z='cwrLedMode'
_y='cwrLedHorizontalPosition'
_x='cwrLedVerticalPosition'
_w='cwrLedName'
_v='cwrImageOp'
_u='cwrImageTag'
_t='cwrImageVersion'
_s='cwrImageCapability2'
_r='cwrImageCapability1'
_q='cwrImageChipClass'
_p='cwrImageChipType'
_o='cwrImageSize'
_n='cwrImageState'
_m='cwrImageNameUrl'
_l='cwrIfSwRevision'
_k='cwrIfVendorId'
_j='cwrIfManfDate'
_i='cwrIfSerialNumber'
_h='cwrIfBoardRevision'
_g='cwrIfBoardPartNumberVersion'
_f='cwrIfBoardPartNumberBase'
_e='cwrIfBoardPartNumberClass'
_d='cwrIfAssemblyPartNumberVersion'
_c='cwrIfAssemblyPartNumberBase'
_b='cwrIfAssemblyPartNumberClass'
_a='cwrRfDuplexorIndex'
_Z='cwrRfVendorId'
_Y='cwrRfManfDate'
_X='cwrRfSerialNumber'
_W='cwrRfBoardRevision'
_V='cwrRfBoardPartNumberVersion'
_U='cwrRfBoardPartNumberBase'
_T='cwrRfBoardPartNumberClass'
_S='cwrRfAssemblyPartNumberVersion'
_R='cwrRfAssemblyPartNumberBase'
_Q='cwrRfAssemblyPartNumberClass'
_P='cwrRfSwRevision'
_O='cwrDuplexorIndex'
_N='cwrLedIndex'
_M='cwrImageIndex'
_L='cwrRfEntityIndex'
_K='entPhysicalIndex'
_J='ENTITY-MIB'
_I='DisplayString'
_H='not-accessible'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-WIRELESS-EXP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
entPhysicalIndex,=mibBuilder.importSymbols(_J,_K)
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'PhysAddress','TextualConvention')
ciscoWirelessExpMIB=ModuleIdentity((1,3,6,1,4,1,9,10,52))
if mibBuilder.loadTexts:ciscoWirelessExpMIB.setRevisions(('2005-12-27 10:03','1999-05-13 20:10'))
_CwrRadioExpMibObjects_ObjectIdentity=ObjectIdentity
cwrRadioExpMibObjects=_CwrRadioExpMibObjects_ObjectIdentity((1,3,6,1,4,1,9,10,52,1))
_CwrRadioFreqEntityGroup_ObjectIdentity=ObjectIdentity
cwrRadioFreqEntityGroup=_CwrRadioFreqEntityGroup_ObjectIdentity((1,3,6,1,4,1,9,10,52,1,1))
_CwrRfEntityTable_Object=MibTable
cwrRfEntityTable=_CwrRfEntityTable_Object((1,3,6,1,4,1,9,10,52,1,1,1))
if mibBuilder.loadTexts:cwrRfEntityTable.setStatus(_A)
_CwrRfEntityEntry_Object=MibTableRow
cwrRfEntityEntry=_CwrRfEntityEntry_Object((1,3,6,1,4,1,9,10,52,1,1,1,1))
cwrRfEntityEntry.setIndexNames((0,_F,_G),(0,_B,_L))
if mibBuilder.loadTexts:cwrRfEntityEntry.setStatus(_A)
class _CwrRfEntityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwrRfEntityIndex_Type.__name__=_D
_CwrRfEntityIndex_Object=MibTableColumn
cwrRfEntityIndex=_CwrRfEntityIndex_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,1),_CwrRfEntityIndex_Type())
cwrRfEntityIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cwrRfEntityIndex.setStatus(_A)
_CwrRfSwRevision_Type=Unsigned32
_CwrRfSwRevision_Object=MibTableColumn
cwrRfSwRevision=_CwrRfSwRevision_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,2),_CwrRfSwRevision_Type())
cwrRfSwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfSwRevision.setStatus(_A)
_CwrRfAssemblyPartNumberClass_Type=Unsigned32
_CwrRfAssemblyPartNumberClass_Object=MibTableColumn
cwrRfAssemblyPartNumberClass=_CwrRfAssemblyPartNumberClass_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,3),_CwrRfAssemblyPartNumberClass_Type())
cwrRfAssemblyPartNumberClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfAssemblyPartNumberClass.setStatus(_A)
_CwrRfAssemblyPartNumberBase_Type=Unsigned32
_CwrRfAssemblyPartNumberBase_Object=MibTableColumn
cwrRfAssemblyPartNumberBase=_CwrRfAssemblyPartNumberBase_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,4),_CwrRfAssemblyPartNumberBase_Type())
cwrRfAssemblyPartNumberBase.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfAssemblyPartNumberBase.setStatus(_A)
_CwrRfAssemblyPartNumberVersion_Type=Unsigned32
_CwrRfAssemblyPartNumberVersion_Object=MibTableColumn
cwrRfAssemblyPartNumberVersion=_CwrRfAssemblyPartNumberVersion_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,5),_CwrRfAssemblyPartNumberVersion_Type())
cwrRfAssemblyPartNumberVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfAssemblyPartNumberVersion.setStatus(_A)
_CwrRfBoardPartNumberClass_Type=Unsigned32
_CwrRfBoardPartNumberClass_Object=MibTableColumn
cwrRfBoardPartNumberClass=_CwrRfBoardPartNumberClass_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,6),_CwrRfBoardPartNumberClass_Type())
cwrRfBoardPartNumberClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfBoardPartNumberClass.setStatus(_A)
_CwrRfBoardPartNumberBase_Type=Unsigned32
_CwrRfBoardPartNumberBase_Object=MibTableColumn
cwrRfBoardPartNumberBase=_CwrRfBoardPartNumberBase_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,7),_CwrRfBoardPartNumberBase_Type())
cwrRfBoardPartNumberBase.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfBoardPartNumberBase.setStatus(_A)
_CwrRfBoardPartNumberVersion_Type=Unsigned32
_CwrRfBoardPartNumberVersion_Object=MibTableColumn
cwrRfBoardPartNumberVersion=_CwrRfBoardPartNumberVersion_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,8),_CwrRfBoardPartNumberVersion_Type())
cwrRfBoardPartNumberVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfBoardPartNumberVersion.setStatus(_A)
_CwrRfBoardRevision_Type=DisplayString
_CwrRfBoardRevision_Object=MibTableColumn
cwrRfBoardRevision=_CwrRfBoardRevision_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,9),_CwrRfBoardRevision_Type())
cwrRfBoardRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfBoardRevision.setStatus(_A)
_CwrRfSerialNumber_Type=DisplayString
_CwrRfSerialNumber_Object=MibTableColumn
cwrRfSerialNumber=_CwrRfSerialNumber_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,10),_CwrRfSerialNumber_Type())
cwrRfSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfSerialNumber.setStatus(_A)
_CwrRfManfDate_Type=DateAndTime
_CwrRfManfDate_Object=MibTableColumn
cwrRfManfDate=_CwrRfManfDate_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,11),_CwrRfManfDate_Type())
cwrRfManfDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfManfDate.setStatus(_A)
class _CwrRfVendorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CwrRfVendorId_Type.__name__=_D
_CwrRfVendorId_Object=MibTableColumn
cwrRfVendorId=_CwrRfVendorId_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,12),_CwrRfVendorId_Type())
cwrRfVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfVendorId.setStatus(_A)
class _CwrRfDuplexorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwrRfDuplexorIndex_Type.__name__=_D
_CwrRfDuplexorIndex_Object=MibTableColumn
cwrRfDuplexorIndex=_CwrRfDuplexorIndex_Object((1,3,6,1,4,1,9,10,52,1,1,1,1,13),_CwrRfDuplexorIndex_Type())
cwrRfDuplexorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrRfDuplexorIndex.setStatus(_A)
_CwrIntFreqEntityTable_Object=MibTable
cwrIntFreqEntityTable=_CwrIntFreqEntityTable_Object((1,3,6,1,4,1,9,10,52,1,1,2))
if mibBuilder.loadTexts:cwrIntFreqEntityTable.setStatus(_A)
_CwrIntFreqEntityEntry_Object=MibTableRow
cwrIntFreqEntityEntry=_CwrIntFreqEntityEntry_Object((1,3,6,1,4,1,9,10,52,1,1,2,1))
cwrIntFreqEntityEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cwrIntFreqEntityEntry.setStatus(_A)
_CwrIfAssemblyPartNumberClass_Type=Unsigned32
_CwrIfAssemblyPartNumberClass_Object=MibTableColumn
cwrIfAssemblyPartNumberClass=_CwrIfAssemblyPartNumberClass_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,1),_CwrIfAssemblyPartNumberClass_Type())
cwrIfAssemblyPartNumberClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfAssemblyPartNumberClass.setStatus(_A)
_CwrIfAssemblyPartNumberBase_Type=Unsigned32
_CwrIfAssemblyPartNumberBase_Object=MibTableColumn
cwrIfAssemblyPartNumberBase=_CwrIfAssemblyPartNumberBase_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,2),_CwrIfAssemblyPartNumberBase_Type())
cwrIfAssemblyPartNumberBase.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfAssemblyPartNumberBase.setStatus(_A)
_CwrIfAssemblyPartNumberVersion_Type=Unsigned32
_CwrIfAssemblyPartNumberVersion_Object=MibTableColumn
cwrIfAssemblyPartNumberVersion=_CwrIfAssemblyPartNumberVersion_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,3),_CwrIfAssemblyPartNumberVersion_Type())
cwrIfAssemblyPartNumberVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfAssemblyPartNumberVersion.setStatus(_A)
_CwrIfBoardPartNumberClass_Type=Unsigned32
_CwrIfBoardPartNumberClass_Object=MibTableColumn
cwrIfBoardPartNumberClass=_CwrIfBoardPartNumberClass_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,4),_CwrIfBoardPartNumberClass_Type())
cwrIfBoardPartNumberClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfBoardPartNumberClass.setStatus(_A)
_CwrIfBoardPartNumberBase_Type=Unsigned32
_CwrIfBoardPartNumberBase_Object=MibTableColumn
cwrIfBoardPartNumberBase=_CwrIfBoardPartNumberBase_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,5),_CwrIfBoardPartNumberBase_Type())
cwrIfBoardPartNumberBase.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfBoardPartNumberBase.setStatus(_A)
_CwrIfBoardPartNumberVersion_Type=Unsigned32
_CwrIfBoardPartNumberVersion_Object=MibTableColumn
cwrIfBoardPartNumberVersion=_CwrIfBoardPartNumberVersion_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,6),_CwrIfBoardPartNumberVersion_Type())
cwrIfBoardPartNumberVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfBoardPartNumberVersion.setStatus(_A)
_CwrIfBoardRevision_Type=DisplayString
_CwrIfBoardRevision_Object=MibTableColumn
cwrIfBoardRevision=_CwrIfBoardRevision_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,7),_CwrIfBoardRevision_Type())
cwrIfBoardRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfBoardRevision.setStatus(_A)
_CwrIfSerialNumber_Type=DisplayString
_CwrIfSerialNumber_Object=MibTableColumn
cwrIfSerialNumber=_CwrIfSerialNumber_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,8),_CwrIfSerialNumber_Type())
cwrIfSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfSerialNumber.setStatus(_A)
_CwrIfManfDate_Type=DateAndTime
_CwrIfManfDate_Object=MibTableColumn
cwrIfManfDate=_CwrIfManfDate_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,9),_CwrIfManfDate_Type())
cwrIfManfDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfManfDate.setStatus(_A)
class _CwrIfVendorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CwrIfVendorId_Type.__name__=_D
_CwrIfVendorId_Object=MibTableColumn
cwrIfVendorId=_CwrIfVendorId_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,10),_CwrIfVendorId_Type())
cwrIfVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfVendorId.setStatus(_A)
_CwrIfSwRevision_Type=Unsigned32
_CwrIfSwRevision_Object=MibTableColumn
cwrIfSwRevision=_CwrIfSwRevision_Object((1,3,6,1,4,1,9,10,52,1,1,2,1,11),_CwrIfSwRevision_Type())
cwrIfSwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrIfSwRevision.setStatus(_A)
_CwrRadioImageGroup_ObjectIdentity=ObjectIdentity
cwrRadioImageGroup=_CwrRadioImageGroup_ObjectIdentity((1,3,6,1,4,1,9,10,52,1,2))
_CwrImageTable_Object=MibTable
cwrImageTable=_CwrImageTable_Object((1,3,6,1,4,1,9,10,52,1,2,1))
if mibBuilder.loadTexts:cwrImageTable.setStatus(_A)
_CwrImageEntry_Object=MibTableRow
cwrImageEntry=_CwrImageEntry_Object((1,3,6,1,4,1,9,10,52,1,2,1,1))
cwrImageEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cwrImageEntry.setStatus(_A)
class _CwrImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwrImageIndex_Type.__name__=_D
_CwrImageIndex_Object=MibTableColumn
cwrImageIndex=_CwrImageIndex_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,1),_CwrImageIndex_Type())
cwrImageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cwrImageIndex.setStatus(_A)
class _CwrImageNameUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CwrImageNameUrl_Type.__name__=_I
_CwrImageNameUrl_Object=MibTableColumn
cwrImageNameUrl=_CwrImageNameUrl_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,2),_CwrImageNameUrl_Type())
cwrImageNameUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrImageNameUrl.setStatus(_A)
class _CwrImageState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('imageInvalid',1),('imageValid',2)))
_CwrImageState_Type.__name__=_D
_CwrImageState_Object=MibTableColumn
cwrImageState=_CwrImageState_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,3),_CwrImageState_Type())
cwrImageState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageState.setStatus(_A)
_CwrImageSize_Type=Unsigned32
_CwrImageSize_Object=MibTableColumn
cwrImageSize=_CwrImageSize_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,4),_CwrImageSize_Type())
cwrImageSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageSize.setStatus(_A)
_CwrImageChipClass_Type=Unsigned32
_CwrImageChipClass_Object=MibTableColumn
cwrImageChipClass=_CwrImageChipClass_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,5),_CwrImageChipClass_Type())
cwrImageChipClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageChipClass.setStatus(_A)
_CwrImageChipType_Type=Unsigned32
_CwrImageChipType_Object=MibTableColumn
cwrImageChipType=_CwrImageChipType_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,6),_CwrImageChipType_Type())
cwrImageChipType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageChipType.setStatus(_A)
_CwrImageCapability1_Type=Unsigned32
_CwrImageCapability1_Object=MibTableColumn
cwrImageCapability1=_CwrImageCapability1_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,7),_CwrImageCapability1_Type())
cwrImageCapability1.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageCapability1.setStatus(_A)
_CwrImageCapability2_Type=Unsigned32
_CwrImageCapability2_Object=MibTableColumn
cwrImageCapability2=_CwrImageCapability2_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,8),_CwrImageCapability2_Type())
cwrImageCapability2.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageCapability2.setStatus(_A)
_CwrImageVersion_Type=Unsigned32
_CwrImageVersion_Object=MibTableColumn
cwrImageVersion=_CwrImageVersion_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,9),_CwrImageVersion_Type())
cwrImageVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageVersion.setStatus(_A)
class _CwrImageTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CwrImageTag_Type.__name__=_I
_CwrImageTag_Object=MibTableColumn
cwrImageTag=_CwrImageTag_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,10),_CwrImageTag_Type())
cwrImageTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrImageTag.setStatus(_A)
class _CwrImageOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('nop',0),('add',1),('delete',2),('move',3)))
_CwrImageOp_Type.__name__=_D
_CwrImageOp_Object=MibTableColumn
cwrImageOp=_CwrImageOp_Object((1,3,6,1,4,1,9,10,52,1,2,1,1,11),_CwrImageOp_Type())
cwrImageOp.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrImageOp.setStatus(_A)
_CwrRadioLedGroup_ObjectIdentity=ObjectIdentity
cwrRadioLedGroup=_CwrRadioLedGroup_ObjectIdentity((1,3,6,1,4,1,9,10,52,1,3))
_CwrLedTable_Object=MibTable
cwrLedTable=_CwrLedTable_Object((1,3,6,1,4,1,9,10,52,1,3,1))
if mibBuilder.loadTexts:cwrLedTable.setStatus(_A)
_CwrLedEntry_Object=MibTableRow
cwrLedEntry=_CwrLedEntry_Object((1,3,6,1,4,1,9,10,52,1,3,1,1))
cwrLedEntry.setIndexNames((0,_J,_K),(0,_B,_N))
if mibBuilder.loadTexts:cwrLedEntry.setStatus(_A)
class _CwrLedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CwrLedIndex_Type.__name__=_D
_CwrLedIndex_Object=MibTableColumn
cwrLedIndex=_CwrLedIndex_Object((1,3,6,1,4,1,9,10,52,1,3,1,1,1),_CwrLedIndex_Type())
cwrLedIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cwrLedIndex.setStatus(_A)
_CwrLedName_Type=DisplayString
_CwrLedName_Object=MibTableColumn
cwrLedName=_CwrLedName_Object((1,3,6,1,4,1,9,10,52,1,3,1,1,2),_CwrLedName_Type())
cwrLedName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrLedName.setStatus(_A)
class _CwrLedVerticalPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CwrLedVerticalPosition_Type.__name__=_D
_CwrLedVerticalPosition_Object=MibTableColumn
cwrLedVerticalPosition=_CwrLedVerticalPosition_Object((1,3,6,1,4,1,9,10,52,1,3,1,1,3),_CwrLedVerticalPosition_Type())
cwrLedVerticalPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrLedVerticalPosition.setStatus(_A)
class _CwrLedHorizontalPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CwrLedHorizontalPosition_Type.__name__=_D
_CwrLedHorizontalPosition_Object=MibTableColumn
cwrLedHorizontalPosition=_CwrLedHorizontalPosition_Object((1,3,6,1,4,1,9,10,52,1,3,1,1,4),_CwrLedHorizontalPosition_Type())
cwrLedHorizontalPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrLedHorizontalPosition.setStatus(_A)
class _CwrLedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('automatic',1),('latched',2),('forceOff',3),('forceSolidGreen',4),('forceSolidYellow',5),('forceBlinkGreen',6),('forceBlinkYellow',7),('forceBlinkBoth',8)))
_CwrLedMode_Type.__name__=_D
_CwrLedMode_Object=MibTableColumn
cwrLedMode=_CwrLedMode_Object((1,3,6,1,4,1,9,10,52,1,3,1,1,5),_CwrLedMode_Type())
cwrLedMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrLedMode.setStatus(_A)
class _CwrLedCurrentColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('green',1),('yellow',2),('blinkGreen',3),('blinkYellow',4),('blinkGreenYellow',5),('off',6)))
_CwrLedCurrentColor_Type.__name__=_D
_CwrLedCurrentColor_Object=MibTableColumn
cwrLedCurrentColor=_CwrLedCurrentColor_Object((1,3,6,1,4,1,9,10,52,1,3,1,1,6),_CwrLedCurrentColor_Type())
cwrLedCurrentColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrLedCurrentColor.setStatus(_A)
_CwrRadioDuplexorGroup_ObjectIdentity=ObjectIdentity
cwrRadioDuplexorGroup=_CwrRadioDuplexorGroup_ObjectIdentity((1,3,6,1,4,1,9,10,52,1,4))
_CwrDuplexorTable_Object=MibTable
cwrDuplexorTable=_CwrDuplexorTable_Object((1,3,6,1,4,1,9,10,52,1,4,1))
if mibBuilder.loadTexts:cwrDuplexorTable.setStatus(_A)
_CwrDuplexorEntry_Object=MibTableRow
cwrDuplexorEntry=_CwrDuplexorEntry_Object((1,3,6,1,4,1,9,10,52,1,4,1,1))
cwrDuplexorEntry.setIndexNames((0,_F,_G),(0,_B,_O))
if mibBuilder.loadTexts:cwrDuplexorEntry.setStatus(_A)
class _CwrDuplexorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwrDuplexorIndex_Type.__name__=_D
_CwrDuplexorIndex_Object=MibTableColumn
cwrDuplexorIndex=_CwrDuplexorIndex_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,1),_CwrDuplexorIndex_Type())
cwrDuplexorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cwrDuplexorIndex.setStatus(_A)
_CwrDuplexorCiscoPartNumber_Type=DisplayString
_CwrDuplexorCiscoPartNumber_Object=MibTableColumn
cwrDuplexorCiscoPartNumber=_CwrDuplexorCiscoPartNumber_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,2),_CwrDuplexorCiscoPartNumber_Type())
cwrDuplexorCiscoPartNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrDuplexorCiscoPartNumber.setStatus(_A)
_CwrDuplexorLoPassbandRange_Type=DisplayString
_CwrDuplexorLoPassbandRange_Object=MibTableColumn
cwrDuplexorLoPassbandRange=_CwrDuplexorLoPassbandRange_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,3),_CwrDuplexorLoPassbandRange_Type())
cwrDuplexorLoPassbandRange.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrDuplexorLoPassbandRange.setStatus(_A)
_CwrDuplexorHiPassbandRange_Type=DisplayString
_CwrDuplexorHiPassbandRange_Object=MibTableColumn
cwrDuplexorHiPassbandRange=_CwrDuplexorHiPassbandRange_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,4),_CwrDuplexorHiPassbandRange_Type())
cwrDuplexorHiPassbandRange.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrDuplexorHiPassbandRange.setStatus(_A)
class _CwrDuplexorReceivePassband_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loPassband',1),('hiPassband',2)))
_CwrDuplexorReceivePassband_Type.__name__=_D
_CwrDuplexorReceivePassband_Object=MibTableColumn
cwrDuplexorReceivePassband=_CwrDuplexorReceivePassband_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,5),_CwrDuplexorReceivePassband_Type())
cwrDuplexorReceivePassband.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrDuplexorReceivePassband.setStatus(_A)
_CwrDuplexorCLEICode_Type=DisplayString
_CwrDuplexorCLEICode_Object=MibTableColumn
cwrDuplexorCLEICode=_CwrDuplexorCLEICode_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,6),_CwrDuplexorCLEICode_Type())
cwrDuplexorCLEICode.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrDuplexorCLEICode.setStatus(_A)
_CwrDuplexorVendorName_Type=DisplayString
_CwrDuplexorVendorName_Object=MibTableColumn
cwrDuplexorVendorName=_CwrDuplexorVendorName_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,7),_CwrDuplexorVendorName_Type())
cwrDuplexorVendorName.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrDuplexorVendorName.setStatus(_A)
_CwrDuplexorSerialNumber_Type=DisplayString
_CwrDuplexorSerialNumber_Object=MibTableColumn
cwrDuplexorSerialNumber=_CwrDuplexorSerialNumber_Object((1,3,6,1,4,1,9,10,52,1,4,1,1,8),_CwrDuplexorSerialNumber_Type())
cwrDuplexorSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrDuplexorSerialNumber.setStatus(_A)
_CwrRadioExpConformance_ObjectIdentity=ObjectIdentity
cwrRadioExpConformance=_CwrRadioExpConformance_ObjectIdentity((1,3,6,1,4,1,9,10,52,2))
_CwrRadioExpCompliances_ObjectIdentity=ObjectIdentity
cwrRadioExpCompliances=_CwrRadioExpCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,52,2,1))
_CwrRadioExpGroups_ObjectIdentity=ObjectIdentity
cwrRadioExpGroups=_CwrRadioExpGroups_ObjectIdentity((1,3,6,1,4,1,9,10,52,2,2))
cwrComplianceRadioRFGroup=ObjectGroup((1,3,6,1,4,1,9,10,52,2,2,1))
cwrComplianceRadioRFGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cwrComplianceRadioRFGroup.setStatus(_A)
cwrComplianceRadioImageGroup=ObjectGroup((1,3,6,1,4,1,9,10,52,2,2,2))
cwrComplianceRadioImageGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cwrComplianceRadioImageGroup.setStatus(_A)
cwrComplianceRadioLEDGroup=ObjectGroup((1,3,6,1,4,1,9,10,52,2,2,3))
cwrComplianceRadioLEDGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cwrComplianceRadioLEDGroup.setStatus(_A)
cwrComplianceRadioDuplexorGroup=ObjectGroup((1,3,6,1,4,1,9,10,52,2,2,4))
cwrComplianceRadioDuplexorGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:cwrComplianceRadioDuplexorGroup.setStatus(_A)
cwrRadioExpCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,52,2,1,1))
cwrRadioExpCompliance.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:cwrRadioExpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWirelessExpMIB':ciscoWirelessExpMIB,'cwrRadioExpMibObjects':cwrRadioExpMibObjects,'cwrRadioFreqEntityGroup':cwrRadioFreqEntityGroup,'cwrRfEntityTable':cwrRfEntityTable,'cwrRfEntityEntry':cwrRfEntityEntry,_L:cwrRfEntityIndex,_P:cwrRfSwRevision,_Q:cwrRfAssemblyPartNumberClass,_R:cwrRfAssemblyPartNumberBase,_S:cwrRfAssemblyPartNumberVersion,_T:cwrRfBoardPartNumberClass,_U:cwrRfBoardPartNumberBase,_V:cwrRfBoardPartNumberVersion,_W:cwrRfBoardRevision,_X:cwrRfSerialNumber,_Y:cwrRfManfDate,_Z:cwrRfVendorId,_a:cwrRfDuplexorIndex,'cwrIntFreqEntityTable':cwrIntFreqEntityTable,'cwrIntFreqEntityEntry':cwrIntFreqEntityEntry,_b:cwrIfAssemblyPartNumberClass,_c:cwrIfAssemblyPartNumberBase,_d:cwrIfAssemblyPartNumberVersion,_e:cwrIfBoardPartNumberClass,_f:cwrIfBoardPartNumberBase,_g:cwrIfBoardPartNumberVersion,_h:cwrIfBoardRevision,_i:cwrIfSerialNumber,_j:cwrIfManfDate,_k:cwrIfVendorId,_l:cwrIfSwRevision,'cwrRadioImageGroup':cwrRadioImageGroup,'cwrImageTable':cwrImageTable,'cwrImageEntry':cwrImageEntry,_M:cwrImageIndex,_m:cwrImageNameUrl,_n:cwrImageState,_o:cwrImageSize,_q:cwrImageChipClass,_p:cwrImageChipType,_r:cwrImageCapability1,_s:cwrImageCapability2,_t:cwrImageVersion,_u:cwrImageTag,_v:cwrImageOp,'cwrRadioLedGroup':cwrRadioLedGroup,'cwrLedTable':cwrLedTable,'cwrLedEntry':cwrLedEntry,_N:cwrLedIndex,_w:cwrLedName,_x:cwrLedVerticalPosition,_y:cwrLedHorizontalPosition,_z:cwrLedMode,_A0:cwrLedCurrentColor,'cwrRadioDuplexorGroup':cwrRadioDuplexorGroup,'cwrDuplexorTable':cwrDuplexorTable,'cwrDuplexorEntry':cwrDuplexorEntry,_O:cwrDuplexorIndex,_A1:cwrDuplexorCiscoPartNumber,_A2:cwrDuplexorLoPassbandRange,_A3:cwrDuplexorHiPassbandRange,_A4:cwrDuplexorReceivePassband,_A5:cwrDuplexorCLEICode,_A6:cwrDuplexorVendorName,_A7:cwrDuplexorSerialNumber,'cwrRadioExpConformance':cwrRadioExpConformance,'cwrRadioExpCompliances':cwrRadioExpCompliances,'cwrRadioExpCompliance':cwrRadioExpCompliance,'cwrRadioExpGroups':cwrRadioExpGroups,_A8:cwrComplianceRadioRFGroup,_A9:cwrComplianceRadioImageGroup,_AA:cwrComplianceRadioLEDGroup,_AB:cwrComplianceRadioDuplexorGroup})