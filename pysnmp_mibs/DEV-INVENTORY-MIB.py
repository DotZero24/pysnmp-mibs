_AG='nbInvPSGroup'
_AF='nbInvFanGroup'
_AE='nbInvCPUGroup'
_AD='nbInvPortGroup'
_AC='nbInvSlotGroup'
_AB='nbInvShelfGroup'
_AA='nbInvIndexGroup'
_A9='nbInvPsDescr'
_A8='nbInvPsPartNumber'
_A7='nbInvPsSerialNumber'
_A6='nbInvPsType'
_A5='nbInvPsIndexId'
_A4='nbInvPsIndexTableNum'
_A3='nbInvFanDescr'
_A2='nbInvFanIndexId'
_A1='nbInvFanIndexTableNum'
_A0='nbInvCpuDescr'
_z='nbInvCpuSerial'
_y='nbInvCpuIndexId'
_x='nbInvCpuIndexTableNum'
_w='nbInvPortWavelength'
_v='nbInvPortAlias'
_u='nbInvPortVendorLotCode'
_t='nbInvPortVendorDate'
_s='nbInvPortVendorSN'
_r='nbInvPortVendorRev'
_q='nbInvPortVendorPN'
_p='nbInvPortVendorOUI'
_o='nbInvPortVendorName'
_n='nbInvPortConnector'
_m='nbInvPortIdentifier'
_l='nbInvPortIndexId'
_k='nbInvPortIndexTableNum'
_j='nbInvSlotSwFpgaRevision'
_i='nbInvSlotHwPartNumber'
_h='nbInvSlotHwSerialUnit'
_g='nbInvSlotHardwareVer'
_f='nbInvSlotIndexId'
_e='nbInvSlotIndexTableNum'
_d='nbInvShelfSwBuildTime'
_c='nbInvShelfSwRev'
_b='nbInvShelfHwPSNumber'
_a='nbInvShelfHwFanNumber'
_Z='nbInvShelfHwCpuNumber'
_Y='nbInvShelfHwBackPlaneSN'
_X='nbInvShelfHwSerialUnit'
_W='nbInvShelfHwVer'
_V='nbInvShelfIndexId'
_U='nbInvShelfIndexTableNum'
_T='nbInvOffsetVal'
_S='nbInvParentIndexId'
_R='nbInvIndexDesc'
_Q='nbInvIndexVal'
_P='nbInvIndexType'
_O='nbInvIndexesMaxNumber'
_N='nbInvPsIndex'
_M='nbInvFanIndex'
_L='nbInvCpuIndex'
_K='unknown'
_J='nbInvPortIndex'
_I='nbInvSlotIndex'
_H='nbInvShelfIndex'
_G='nbInvIndexId'
_F='not-accessible'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='DEV-INVENTORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
nbInvId=ModuleIdentity((1,3,6,1,4,1,629,1,50,19))
if mibBuilder.loadTexts:nbInvId.setRevisions(('2009-01-15 00:00',))
class InvIndexType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('shelf',1),('slot',2),('entity',3),('port',4),('cpuSlot',5),('fanSlot',6),('psSlot',7)))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbInvGenInfo_ObjectIdentity=ObjectIdentity
nbInvGenInfo=_NbInvGenInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1))
_NbInvDevIndexInfo_ObjectIdentity=ObjectIdentity
nbInvDevIndexInfo=_NbInvDevIndexInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,1))
_NbInvIndexesMaxNumber_Type=Integer32
_NbInvIndexesMaxNumber_Object=MibScalar
nbInvIndexesMaxNumber=_NbInvIndexesMaxNumber_Object((1,3,6,1,4,1,629,1,50,19,1,1,1),_NbInvIndexesMaxNumber_Type())
nbInvIndexesMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvIndexesMaxNumber.setStatus(_A)
_NbInvIndexesTable_Object=MibTable
nbInvIndexesTable=_NbInvIndexesTable_Object((1,3,6,1,4,1,629,1,50,19,1,1,5))
if mibBuilder.loadTexts:nbInvIndexesTable.setStatus(_A)
_NbInvIndexesEntry_Object=MibTableRow
nbInvIndexesEntry=_NbInvIndexesEntry_Object((1,3,6,1,4,1,629,1,50,19,1,1,5,1))
nbInvIndexesEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:nbInvIndexesEntry.setStatus(_A)
class _NbInvIndexId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvIndexId_Type.__name__=_D
_NbInvIndexId_Object=MibTableColumn
nbInvIndexId=_NbInvIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,1,5,1,1),_NbInvIndexId_Type())
nbInvIndexId.setMaxAccess(_F)
if mibBuilder.loadTexts:nbInvIndexId.setStatus(_A)
_NbInvIndexType_Type=InvIndexType
_NbInvIndexType_Object=MibTableColumn
nbInvIndexType=_NbInvIndexType_Object((1,3,6,1,4,1,629,1,50,19,1,1,5,1,2),_NbInvIndexType_Type())
nbInvIndexType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvIndexType.setStatus(_A)
class _NbInvIndexVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvIndexVal_Type.__name__=_D
_NbInvIndexVal_Object=MibTableColumn
nbInvIndexVal=_NbInvIndexVal_Object((1,3,6,1,4,1,629,1,50,19,1,1,5,1,3),_NbInvIndexVal_Type())
nbInvIndexVal.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvIndexVal.setStatus(_A)
_NbInvIndexDesc_Type=DisplayString
_NbInvIndexDesc_Object=MibTableColumn
nbInvIndexDesc=_NbInvIndexDesc_Object((1,3,6,1,4,1,629,1,50,19,1,1,5,1,4),_NbInvIndexDesc_Type())
nbInvIndexDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvIndexDesc.setStatus(_A)
class _NbInvParentIndexId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvParentIndexId_Type.__name__=_D
_NbInvParentIndexId_Object=MibTableColumn
nbInvParentIndexId=_NbInvParentIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,1,5,1,5),_NbInvParentIndexId_Type())
nbInvParentIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvParentIndexId.setStatus(_A)
class _NbInvOffsetVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvOffsetVal_Type.__name__=_D
_NbInvOffsetVal_Object=MibTableColumn
nbInvOffsetVal=_NbInvOffsetVal_Object((1,3,6,1,4,1,629,1,50,19,1,1,5,1,6),_NbInvOffsetVal_Type())
nbInvOffsetVal.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvOffsetVal.setStatus(_A)
_NbInvDevDetails_ObjectIdentity=ObjectIdentity
nbInvDevDetails=_NbInvDevDetails_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,2))
_NbInvShelfInfo_ObjectIdentity=ObjectIdentity
nbInvShelfInfo=_NbInvShelfInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,2,1))
_NbInvShelfIndexTableNum_Type=Integer32
_NbInvShelfIndexTableNum_Object=MibScalar
nbInvShelfIndexTableNum=_NbInvShelfIndexTableNum_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,1),_NbInvShelfIndexTableNum_Type())
nbInvShelfIndexTableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfIndexTableNum.setStatus(_A)
_NbInvShelfIndexId_Type=Integer32
_NbInvShelfIndexId_Object=MibScalar
nbInvShelfIndexId=_NbInvShelfIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,2),_NbInvShelfIndexId_Type())
nbInvShelfIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfIndexId.setStatus(_A)
_NbInvShelfTable_Object=MibTable
nbInvShelfTable=_NbInvShelfTable_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5))
if mibBuilder.loadTexts:nbInvShelfTable.setStatus(_A)
_NbInvShelfEntry_Object=MibTableRow
nbInvShelfEntry=_NbInvShelfEntry_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1))
nbInvShelfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:nbInvShelfEntry.setStatus(_A)
class _NbInvShelfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvShelfIndex_Type.__name__=_D
_NbInvShelfIndex_Object=MibTableColumn
nbInvShelfIndex=_NbInvShelfIndex_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,1),_NbInvShelfIndex_Type())
nbInvShelfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbInvShelfIndex.setStatus(_A)
class _NbInvShelfHwVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvShelfHwVer_Type.__name__=_D
_NbInvShelfHwVer_Object=MibTableColumn
nbInvShelfHwVer=_NbInvShelfHwVer_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,2),_NbInvShelfHwVer_Type())
nbInvShelfHwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfHwVer.setStatus(_A)
_NbInvShelfHwSerialUnit_Type=DisplayString
_NbInvShelfHwSerialUnit_Object=MibTableColumn
nbInvShelfHwSerialUnit=_NbInvShelfHwSerialUnit_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,3),_NbInvShelfHwSerialUnit_Type())
nbInvShelfHwSerialUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfHwSerialUnit.setStatus(_A)
_NbInvShelfHwBackPlaneSN_Type=DisplayString
_NbInvShelfHwBackPlaneSN_Object=MibTableColumn
nbInvShelfHwBackPlaneSN=_NbInvShelfHwBackPlaneSN_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,4),_NbInvShelfHwBackPlaneSN_Type())
nbInvShelfHwBackPlaneSN.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfHwBackPlaneSN.setStatus(_A)
class _NbInvShelfHwCpuNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvShelfHwCpuNumber_Type.__name__=_D
_NbInvShelfHwCpuNumber_Object=MibTableColumn
nbInvShelfHwCpuNumber=_NbInvShelfHwCpuNumber_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,6),_NbInvShelfHwCpuNumber_Type())
nbInvShelfHwCpuNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfHwCpuNumber.setStatus(_A)
class _NbInvShelfHwFanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvShelfHwFanNumber_Type.__name__=_D
_NbInvShelfHwFanNumber_Object=MibTableColumn
nbInvShelfHwFanNumber=_NbInvShelfHwFanNumber_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,7),_NbInvShelfHwFanNumber_Type())
nbInvShelfHwFanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfHwFanNumber.setStatus(_A)
class _NbInvShelfHwPSNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvShelfHwPSNumber_Type.__name__=_D
_NbInvShelfHwPSNumber_Object=MibTableColumn
nbInvShelfHwPSNumber=_NbInvShelfHwPSNumber_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,8),_NbInvShelfHwPSNumber_Type())
nbInvShelfHwPSNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfHwPSNumber.setStatus(_A)
_NbInvShelfSwRev_Type=DisplayString
_NbInvShelfSwRev_Object=MibTableColumn
nbInvShelfSwRev=_NbInvShelfSwRev_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,9),_NbInvShelfSwRev_Type())
nbInvShelfSwRev.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfSwRev.setStatus(_A)
_NbInvShelfSwBuildTime_Type=DisplayString
_NbInvShelfSwBuildTime_Object=MibTableColumn
nbInvShelfSwBuildTime=_NbInvShelfSwBuildTime_Object((1,3,6,1,4,1,629,1,50,19,1,2,1,5,1,10),_NbInvShelfSwBuildTime_Type())
nbInvShelfSwBuildTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvShelfSwBuildTime.setStatus(_A)
_NbInvSlotInfo_ObjectIdentity=ObjectIdentity
nbInvSlotInfo=_NbInvSlotInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,2,2))
_NbInvSlotIndexTableNum_Type=Integer32
_NbInvSlotIndexTableNum_Object=MibScalar
nbInvSlotIndexTableNum=_NbInvSlotIndexTableNum_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,1),_NbInvSlotIndexTableNum_Type())
nbInvSlotIndexTableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvSlotIndexTableNum.setStatus(_A)
_NbInvSlotIndexId_Type=Integer32
_NbInvSlotIndexId_Object=MibScalar
nbInvSlotIndexId=_NbInvSlotIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,2),_NbInvSlotIndexId_Type())
nbInvSlotIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvSlotIndexId.setStatus(_A)
_NbInvSlotTable_Object=MibTable
nbInvSlotTable=_NbInvSlotTable_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,5))
if mibBuilder.loadTexts:nbInvSlotTable.setStatus(_A)
_NbInvSlotEntry_Object=MibTableRow
nbInvSlotEntry=_NbInvSlotEntry_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,5,1))
nbInvSlotEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:nbInvSlotEntry.setStatus(_A)
class _NbInvSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvSlotIndex_Type.__name__=_D
_NbInvSlotIndex_Object=MibTableColumn
nbInvSlotIndex=_NbInvSlotIndex_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,5,1,1),_NbInvSlotIndex_Type())
nbInvSlotIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbInvSlotIndex.setStatus(_A)
class _NbInvSlotHardwareVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvSlotHardwareVer_Type.__name__=_D
_NbInvSlotHardwareVer_Object=MibTableColumn
nbInvSlotHardwareVer=_NbInvSlotHardwareVer_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,5,1,2),_NbInvSlotHardwareVer_Type())
nbInvSlotHardwareVer.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvSlotHardwareVer.setStatus(_A)
_NbInvSlotHwSerialUnit_Type=DisplayString
_NbInvSlotHwSerialUnit_Object=MibTableColumn
nbInvSlotHwSerialUnit=_NbInvSlotHwSerialUnit_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,5,1,3),_NbInvSlotHwSerialUnit_Type())
nbInvSlotHwSerialUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvSlotHwSerialUnit.setStatus(_A)
_NbInvSlotHwPartNumber_Type=DisplayString
_NbInvSlotHwPartNumber_Object=MibTableColumn
nbInvSlotHwPartNumber=_NbInvSlotHwPartNumber_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,5,1,4),_NbInvSlotHwPartNumber_Type())
nbInvSlotHwPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvSlotHwPartNumber.setStatus(_A)
_NbInvSlotSwFpgaRevision_Type=DisplayString
_NbInvSlotSwFpgaRevision_Object=MibTableColumn
nbInvSlotSwFpgaRevision=_NbInvSlotSwFpgaRevision_Object((1,3,6,1,4,1,629,1,50,19,1,2,2,5,1,5),_NbInvSlotSwFpgaRevision_Type())
nbInvSlotSwFpgaRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvSlotSwFpgaRevision.setStatus(_A)
_NbInvPortInfo_ObjectIdentity=ObjectIdentity
nbInvPortInfo=_NbInvPortInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,2,4))
_NbInvPortIndexTableNum_Type=Integer32
_NbInvPortIndexTableNum_Object=MibScalar
nbInvPortIndexTableNum=_NbInvPortIndexTableNum_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,1),_NbInvPortIndexTableNum_Type())
nbInvPortIndexTableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortIndexTableNum.setStatus(_A)
_NbInvPortIndexId_Type=Integer32
_NbInvPortIndexId_Object=MibScalar
nbInvPortIndexId=_NbInvPortIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,2),_NbInvPortIndexId_Type())
nbInvPortIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortIndexId.setStatus(_A)
_NbInvPortTable_Object=MibTable
nbInvPortTable=_NbInvPortTable_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5))
if mibBuilder.loadTexts:nbInvPortTable.setStatus(_A)
_NbInvPortEntry_Object=MibTableRow
nbInvPortEntry=_NbInvPortEntry_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1))
nbInvPortEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:nbInvPortEntry.setStatus(_A)
class _NbInvPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvPortIndex_Type.__name__=_D
_NbInvPortIndex_Object=MibTableColumn
nbInvPortIndex=_NbInvPortIndex_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,1),_NbInvPortIndex_Type())
nbInvPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbInvPortIndex.setStatus(_A)
class _NbInvPortIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_K,1),('combo',2),('gbic',3),('fixed',4),('sfp',5),('xbi300pin',6),('xenpak',7),('xfp',8),('xff',9),('xfpE',10),('xpak',11),('x2',12),('dsfp',13)))
_NbInvPortIdentifier_Type.__name__=_D
_NbInvPortIdentifier_Object=MibTableColumn
nbInvPortIdentifier=_NbInvPortIdentifier_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,2),_NbInvPortIdentifier_Type())
nbInvPortIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortIdentifier.setStatus(_A)
class _NbInvPortConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,34,35)));namedValues=NamedValues(*((_K,1),('other',2),('sc',3),('fcs1cc',4),('fcs2cc',5),('bnctnc',6),('fcch',7),('fiberJack',8),('lc',9),('mtrj',10),('mu',11),('sg',12),('opticalPigtail',13),('hssdcii',34),('copperPigtail',35)))
_NbInvPortConnector_Type.__name__=_D
_NbInvPortConnector_Object=MibTableColumn
nbInvPortConnector=_NbInvPortConnector_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,3),_NbInvPortConnector_Type())
nbInvPortConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortConnector.setStatus(_A)
class _NbInvPortVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbInvPortVendorName_Type.__name__=_E
_NbInvPortVendorName_Object=MibTableColumn
nbInvPortVendorName=_NbInvPortVendorName_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,4),_NbInvPortVendorName_Type())
nbInvPortVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortVendorName.setStatus(_A)
class _NbInvPortVendorOUI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_NbInvPortVendorOUI_Type.__name__=_E
_NbInvPortVendorOUI_Object=MibTableColumn
nbInvPortVendorOUI=_NbInvPortVendorOUI_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,5),_NbInvPortVendorOUI_Type())
nbInvPortVendorOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortVendorOUI.setStatus(_A)
class _NbInvPortVendorPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbInvPortVendorPN_Type.__name__=_E
_NbInvPortVendorPN_Object=MibTableColumn
nbInvPortVendorPN=_NbInvPortVendorPN_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,6),_NbInvPortVendorPN_Type())
nbInvPortVendorPN.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortVendorPN.setStatus(_A)
class _NbInvPortVendorRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_NbInvPortVendorRev_Type.__name__=_E
_NbInvPortVendorRev_Object=MibTableColumn
nbInvPortVendorRev=_NbInvPortVendorRev_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,7),_NbInvPortVendorRev_Type())
nbInvPortVendorRev.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortVendorRev.setStatus(_A)
class _NbInvPortVendorSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbInvPortVendorSN_Type.__name__=_E
_NbInvPortVendorSN_Object=MibTableColumn
nbInvPortVendorSN=_NbInvPortVendorSN_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,8),_NbInvPortVendorSN_Type())
nbInvPortVendorSN.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortVendorSN.setStatus(_A)
class _NbInvPortVendorDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbInvPortVendorDate_Type.__name__=_E
_NbInvPortVendorDate_Object=MibTableColumn
nbInvPortVendorDate=_NbInvPortVendorDate_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,9),_NbInvPortVendorDate_Type())
nbInvPortVendorDate.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortVendorDate.setStatus(_A)
class _NbInvPortVendorLotCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NbInvPortVendorLotCode_Type.__name__=_E
_NbInvPortVendorLotCode_Object=MibTableColumn
nbInvPortVendorLotCode=_NbInvPortVendorLotCode_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,10),_NbInvPortVendorLotCode_Type())
nbInvPortVendorLotCode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortVendorLotCode.setStatus(_A)
class _NbInvPortAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NbInvPortAlias_Type.__name__=_E
_NbInvPortAlias_Object=MibTableColumn
nbInvPortAlias=_NbInvPortAlias_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,11),_NbInvPortAlias_Type())
nbInvPortAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortAlias.setStatus(_A)
_NbInvPortWavelength_Type=Integer32
_NbInvPortWavelength_Object=MibTableColumn
nbInvPortWavelength=_NbInvPortWavelength_Object((1,3,6,1,4,1,629,1,50,19,1,2,4,5,1,12),_NbInvPortWavelength_Type())
nbInvPortWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPortWavelength.setStatus(_A)
if mibBuilder.loadTexts:nbInvPortWavelength.setUnits('0.01 Nano Meter(nm)')
_NbInvCpuInfo_ObjectIdentity=ObjectIdentity
nbInvCpuInfo=_NbInvCpuInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,2,5))
_NbInvCpuIndexTableNum_Type=Integer32
_NbInvCpuIndexTableNum_Object=MibScalar
nbInvCpuIndexTableNum=_NbInvCpuIndexTableNum_Object((1,3,6,1,4,1,629,1,50,19,1,2,5,1),_NbInvCpuIndexTableNum_Type())
nbInvCpuIndexTableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvCpuIndexTableNum.setStatus(_A)
_NbInvCpuIndexId_Type=Integer32
_NbInvCpuIndexId_Object=MibScalar
nbInvCpuIndexId=_NbInvCpuIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,2,5,2),_NbInvCpuIndexId_Type())
nbInvCpuIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvCpuIndexId.setStatus(_A)
_NbInvCpuTable_Object=MibTable
nbInvCpuTable=_NbInvCpuTable_Object((1,3,6,1,4,1,629,1,50,19,1,2,5,5))
if mibBuilder.loadTexts:nbInvCpuTable.setStatus(_A)
_NbInvCpuEntry_Object=MibTableRow
nbInvCpuEntry=_NbInvCpuEntry_Object((1,3,6,1,4,1,629,1,50,19,1,2,5,5,1))
nbInvCpuEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:nbInvCpuEntry.setStatus(_A)
class _NbInvCpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvCpuIndex_Type.__name__=_D
_NbInvCpuIndex_Object=MibTableColumn
nbInvCpuIndex=_NbInvCpuIndex_Object((1,3,6,1,4,1,629,1,50,19,1,2,5,5,1,1),_NbInvCpuIndex_Type())
nbInvCpuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbInvCpuIndex.setStatus(_A)
_NbInvCpuSerial_Type=DisplayString
_NbInvCpuSerial_Object=MibTableColumn
nbInvCpuSerial=_NbInvCpuSerial_Object((1,3,6,1,4,1,629,1,50,19,1,2,5,5,1,4),_NbInvCpuSerial_Type())
nbInvCpuSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvCpuSerial.setStatus(_A)
_NbInvCpuDescr_Type=DisplayString
_NbInvCpuDescr_Object=MibTableColumn
nbInvCpuDescr=_NbInvCpuDescr_Object((1,3,6,1,4,1,629,1,50,19,1,2,5,5,1,9),_NbInvCpuDescr_Type())
nbInvCpuDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvCpuDescr.setStatus(_A)
_NbInvFanInfo_ObjectIdentity=ObjectIdentity
nbInvFanInfo=_NbInvFanInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,2,6))
_NbInvFanIndexTableNum_Type=Integer32
_NbInvFanIndexTableNum_Object=MibScalar
nbInvFanIndexTableNum=_NbInvFanIndexTableNum_Object((1,3,6,1,4,1,629,1,50,19,1,2,6,1),_NbInvFanIndexTableNum_Type())
nbInvFanIndexTableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvFanIndexTableNum.setStatus(_A)
_NbInvFanIndexId_Type=Integer32
_NbInvFanIndexId_Object=MibScalar
nbInvFanIndexId=_NbInvFanIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,2,6,2),_NbInvFanIndexId_Type())
nbInvFanIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvFanIndexId.setStatus(_A)
_NbInvFanTable_Object=MibTable
nbInvFanTable=_NbInvFanTable_Object((1,3,6,1,4,1,629,1,50,19,1,2,6,5))
if mibBuilder.loadTexts:nbInvFanTable.setStatus(_A)
_NbInvFanEntry_Object=MibTableRow
nbInvFanEntry=_NbInvFanEntry_Object((1,3,6,1,4,1,629,1,50,19,1,2,6,5,1))
nbInvFanEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:nbInvFanEntry.setStatus(_A)
class _NbInvFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvFanIndex_Type.__name__=_D
_NbInvFanIndex_Object=MibTableColumn
nbInvFanIndex=_NbInvFanIndex_Object((1,3,6,1,4,1,629,1,50,19,1,2,6,5,1,1),_NbInvFanIndex_Type())
nbInvFanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbInvFanIndex.setStatus(_A)
_NbInvFanDescr_Type=DisplayString
_NbInvFanDescr_Object=MibTableColumn
nbInvFanDescr=_NbInvFanDescr_Object((1,3,6,1,4,1,629,1,50,19,1,2,6,5,1,2),_NbInvFanDescr_Type())
nbInvFanDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvFanDescr.setStatus(_A)
_NbInvPsInfo_ObjectIdentity=ObjectIdentity
nbInvPsInfo=_NbInvPsInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,1,2,7))
_NbInvPsIndexTableNum_Type=Integer32
_NbInvPsIndexTableNum_Object=MibScalar
nbInvPsIndexTableNum=_NbInvPsIndexTableNum_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,1),_NbInvPsIndexTableNum_Type())
nbInvPsIndexTableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPsIndexTableNum.setStatus(_A)
_NbInvPsIndexId_Type=Integer32
_NbInvPsIndexId_Object=MibScalar
nbInvPsIndexId=_NbInvPsIndexId_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,2),_NbInvPsIndexId_Type())
nbInvPsIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPsIndexId.setStatus(_A)
_NbInvPsTable_Object=MibTable
nbInvPsTable=_NbInvPsTable_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,5))
if mibBuilder.loadTexts:nbInvPsTable.setStatus(_A)
_NbInvPsEntry_Object=MibTableRow
nbInvPsEntry=_NbInvPsEntry_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,5,1))
nbInvPsEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:nbInvPsEntry.setStatus(_A)
class _NbInvPsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NbInvPsIndex_Type.__name__=_D
_NbInvPsIndex_Object=MibTableColumn
nbInvPsIndex=_NbInvPsIndex_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,5,1,1),_NbInvPsIndex_Type())
nbInvPsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbInvPsIndex.setStatus(_A)
class _NbInvPsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('dcType',2),('acType',3)))
_NbInvPsType_Type.__name__=_D
_NbInvPsType_Object=MibTableColumn
nbInvPsType=_NbInvPsType_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,5,1,2),_NbInvPsType_Type())
nbInvPsType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPsType.setStatus(_A)
_NbInvPsSerialNumber_Type=DisplayString
_NbInvPsSerialNumber_Object=MibTableColumn
nbInvPsSerialNumber=_NbInvPsSerialNumber_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,5,1,3),_NbInvPsSerialNumber_Type())
nbInvPsSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPsSerialNumber.setStatus(_A)
_NbInvPsPartNumber_Type=DisplayString
_NbInvPsPartNumber_Object=MibTableColumn
nbInvPsPartNumber=_NbInvPsPartNumber_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,5,1,4),_NbInvPsPartNumber_Type())
nbInvPsPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPsPartNumber.setStatus(_A)
_NbInvPsDescr_Type=DisplayString
_NbInvPsDescr_Object=MibTableColumn
nbInvPsDescr=_NbInvPsDescr_Object((1,3,6,1,4,1,629,1,50,19,1,2,7,5,1,5),_NbInvPsDescr_Type())
nbInvPsDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbInvPsDescr.setStatus(_A)
_NbInvConformance_ObjectIdentity=ObjectIdentity
nbInvConformance=_NbInvConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,101))
_NbInvMIBCompliances_ObjectIdentity=ObjectIdentity
nbInvMIBCompliances=_NbInvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,101,1))
_NbInvMIBGroups_ObjectIdentity=ObjectIdentity
nbInvMIBGroups=_NbInvMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,19,101,2))
nbInvIndexGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,19,101,2,1))
nbInvIndexGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:nbInvIndexGroup.setStatus(_A)
nbInvShelfGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,19,101,2,2))
nbInvShelfGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:nbInvShelfGroup.setStatus(_A)
nbInvSlotGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,19,101,2,3))
nbInvSlotGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:nbInvSlotGroup.setStatus(_A)
nbInvPortGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,19,101,2,5))
nbInvPortGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:nbInvPortGroup.setStatus(_A)
nbInvCPUGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,19,101,2,6))
nbInvCPUGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:nbInvCPUGroup.setStatus(_A)
nbInvFanGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,19,101,2,7))
nbInvFanGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:nbInvFanGroup.setStatus(_A)
nbInvPSGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,19,101,2,8))
nbInvPSGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:nbInvPSGroup.setStatus(_A)
nbInvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,19,101,1,1))
nbInvMIBCompliance.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:nbInvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'InvIndexType':InvIndexType,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbInvId':nbInvId,'nbInvGenInfo':nbInvGenInfo,'nbInvDevIndexInfo':nbInvDevIndexInfo,_O:nbInvIndexesMaxNumber,'nbInvIndexesTable':nbInvIndexesTable,'nbInvIndexesEntry':nbInvIndexesEntry,_G:nbInvIndexId,_P:nbInvIndexType,_Q:nbInvIndexVal,_R:nbInvIndexDesc,_S:nbInvParentIndexId,_T:nbInvOffsetVal,'nbInvDevDetails':nbInvDevDetails,'nbInvShelfInfo':nbInvShelfInfo,_U:nbInvShelfIndexTableNum,_V:nbInvShelfIndexId,'nbInvShelfTable':nbInvShelfTable,'nbInvShelfEntry':nbInvShelfEntry,_H:nbInvShelfIndex,_W:nbInvShelfHwVer,_X:nbInvShelfHwSerialUnit,_Y:nbInvShelfHwBackPlaneSN,_Z:nbInvShelfHwCpuNumber,_a:nbInvShelfHwFanNumber,_b:nbInvShelfHwPSNumber,_c:nbInvShelfSwRev,_d:nbInvShelfSwBuildTime,'nbInvSlotInfo':nbInvSlotInfo,_e:nbInvSlotIndexTableNum,_f:nbInvSlotIndexId,'nbInvSlotTable':nbInvSlotTable,'nbInvSlotEntry':nbInvSlotEntry,_I:nbInvSlotIndex,_g:nbInvSlotHardwareVer,_h:nbInvSlotHwSerialUnit,_i:nbInvSlotHwPartNumber,_j:nbInvSlotSwFpgaRevision,'nbInvPortInfo':nbInvPortInfo,_k:nbInvPortIndexTableNum,_l:nbInvPortIndexId,'nbInvPortTable':nbInvPortTable,'nbInvPortEntry':nbInvPortEntry,_J:nbInvPortIndex,_m:nbInvPortIdentifier,_n:nbInvPortConnector,_o:nbInvPortVendorName,_p:nbInvPortVendorOUI,_q:nbInvPortVendorPN,_r:nbInvPortVendorRev,_s:nbInvPortVendorSN,_t:nbInvPortVendorDate,_u:nbInvPortVendorLotCode,_v:nbInvPortAlias,_w:nbInvPortWavelength,'nbInvCpuInfo':nbInvCpuInfo,_x:nbInvCpuIndexTableNum,_y:nbInvCpuIndexId,'nbInvCpuTable':nbInvCpuTable,'nbInvCpuEntry':nbInvCpuEntry,_L:nbInvCpuIndex,_z:nbInvCpuSerial,_A0:nbInvCpuDescr,'nbInvFanInfo':nbInvFanInfo,_A1:nbInvFanIndexTableNum,_A2:nbInvFanIndexId,'nbInvFanTable':nbInvFanTable,'nbInvFanEntry':nbInvFanEntry,_M:nbInvFanIndex,_A3:nbInvFanDescr,'nbInvPsInfo':nbInvPsInfo,_A4:nbInvPsIndexTableNum,_A5:nbInvPsIndexId,'nbInvPsTable':nbInvPsTable,'nbInvPsEntry':nbInvPsEntry,_N:nbInvPsIndex,_A6:nbInvPsType,_A7:nbInvPsSerialNumber,_A8:nbInvPsPartNumber,_A9:nbInvPsDescr,'nbInvConformance':nbInvConformance,'nbInvMIBCompliances':nbInvMIBCompliances,'nbInvMIBCompliance':nbInvMIBCompliance,'nbInvMIBGroups':nbInvMIBGroups,_AA:nbInvIndexGroup,_AB:nbInvShelfGroup,_AC:nbInvSlotGroup,_AD:nbInvPortGroup,_AE:nbInvCPUGroup,_AF:nbInvFanGroup,_AG:nbInvPSGroup})