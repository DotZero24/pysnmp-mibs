_Z='portTrunkMember'
_Y='portTrunkId'
_X='tvlanPortPortId'
_W='tvlanId'
_V='configMirrorId'
_U='rate100M-Full'
_T='rate100M-Half'
_S='rate10M-Full'
_R='rate10M-Half'
_Q='configPort'
_P='commTrapIndex'
_O='commGetIndex'
_N='commSetIndex'
_M='destroy'
_L='createAndGo'
_K='active'
_J='current'
_I='noop'
_H='DisplayString'
_G='DES-1526-MIB'
_F='enabled'
_E='read-only'
_D='disabled'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
class OwnerString(DisplayString):0
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class PortList(TextualConvention,OctetString):status=_J;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class RowStatus(TextualConvention,Integer32):status=_J;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('notInService',2),('notReady',3),(_L,4),('createAndWait',5),(_M,6)))
_D_link_ObjectIdentity=ObjectIdentity
d_link=_D_link_ObjectIdentity((1,3,6,1,4,1,171))
_Dlink_products_ObjectIdentity=ObjectIdentity
dlink_products=_Dlink_products_ObjectIdentity((1,3,6,1,4,1,171,10))
_Dlink_DES1526SeriesProd_ObjectIdentity=ObjectIdentity
dlink_DES1526SeriesProd=_Dlink_DES1526SeriesProd_ObjectIdentity((1,3,6,1,4,1,171,10,60))
_DES_1526_ObjectIdentity=ObjectIdentity
DES_1526=_DES_1526_ObjectIdentity((1,3,6,1,4,1,171,10,60,1))
_CompanyCommGroup_ObjectIdentity=ObjectIdentity
companyCommGroup=_CompanyCommGroup_ObjectIdentity((1,3,6,1,4,1,171,10,60,1,1))
_CommSetTable_Object=MibTable
commSetTable=_CommSetTable_Object((1,3,6,1,4,1,171,10,60,1,1,1))
if mibBuilder.loadTexts:commSetTable.setStatus(_A)
_CommSetEntry_Object=MibTableRow
commSetEntry=_CommSetEntry_Object((1,3,6,1,4,1,171,10,60,1,1,1,1))
commSetEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:commSetEntry.setStatus(_A)
class _CommSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CommSetIndex_Type.__name__=_C
_CommSetIndex_Object=MibTableColumn
commSetIndex=_CommSetIndex_Object((1,3,6,1,4,1,171,10,60,1,1,1,1,1),_CommSetIndex_Type())
commSetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:commSetIndex.setStatus(_A)
class _CommSetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CommSetName_Type.__name__=_H
_CommSetName_Object=MibTableColumn
commSetName=_CommSetName_Object((1,3,6,1,4,1,171,10,60,1,1,1,1,2),_CommSetName_Type())
commSetName.setMaxAccess(_B)
if mibBuilder.loadTexts:commSetName.setStatus(_A)
_CommSetStatus_Type=RowStatus
_CommSetStatus_Object=MibTableColumn
commSetStatus=_CommSetStatus_Object((1,3,6,1,4,1,171,10,60,1,1,1,1,3),_CommSetStatus_Type())
commSetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commSetStatus.setStatus(_A)
_CommGetTable_Object=MibTable
commGetTable=_CommGetTable_Object((1,3,6,1,4,1,171,10,60,1,1,2))
if mibBuilder.loadTexts:commGetTable.setStatus(_A)
_CommGetEntry_Object=MibTableRow
commGetEntry=_CommGetEntry_Object((1,3,6,1,4,1,171,10,60,1,1,2,1))
commGetEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:commGetEntry.setStatus(_A)
class _CommGetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CommGetIndex_Type.__name__=_C
_CommGetIndex_Object=MibTableColumn
commGetIndex=_CommGetIndex_Object((1,3,6,1,4,1,171,10,60,1,1,2,1,1),_CommGetIndex_Type())
commGetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:commGetIndex.setStatus(_A)
class _CommGetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CommGetName_Type.__name__=_H
_CommGetName_Object=MibTableColumn
commGetName=_CommGetName_Object((1,3,6,1,4,1,171,10,60,1,1,2,1,2),_CommGetName_Type())
commGetName.setMaxAccess(_B)
if mibBuilder.loadTexts:commGetName.setStatus(_A)
_CommGetStatus_Type=RowStatus
_CommGetStatus_Object=MibTableColumn
commGetStatus=_CommGetStatus_Object((1,3,6,1,4,1,171,10,60,1,1,2,1,3),_CommGetStatus_Type())
commGetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commGetStatus.setStatus(_A)
_CommTrapTable_Object=MibTable
commTrapTable=_CommTrapTable_Object((1,3,6,1,4,1,171,10,60,1,1,3))
if mibBuilder.loadTexts:commTrapTable.setStatus(_A)
_CommTrapEntry_Object=MibTableRow
commTrapEntry=_CommTrapEntry_Object((1,3,6,1,4,1,171,10,60,1,1,3,1))
commTrapEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:commTrapEntry.setStatus(_A)
class _CommTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CommTrapIndex_Type.__name__=_C
_CommTrapIndex_Object=MibTableColumn
commTrapIndex=_CommTrapIndex_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,1),_CommTrapIndex_Type())
commTrapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:commTrapIndex.setStatus(_A)
class _CommTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CommTrapName_Type.__name__=_H
_CommTrapName_Object=MibTableColumn
commTrapName=_CommTrapName_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,2),_CommTrapName_Type())
commTrapName.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapName.setStatus(_A)
_CommTrapIpAddress_Type=IpAddress
_CommTrapIpAddress_Object=MibTableColumn
commTrapIpAddress=_CommTrapIpAddress_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,3),_CommTrapIpAddress_Type())
commTrapIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapIpAddress.setStatus(_A)
_CommTrapVlanId_Type=Integer32
_CommTrapVlanId_Object=MibTableColumn
commTrapVlanId=_CommTrapVlanId_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,4),_CommTrapVlanId_Type())
commTrapVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapVlanId.setStatus(_A)
class _CommTrapSNMPBootup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapSNMPBootup_Type.__name__=_C
_CommTrapSNMPBootup_Object=MibTableColumn
commTrapSNMPBootup=_CommTrapSNMPBootup_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,5),_CommTrapSNMPBootup_Type())
commTrapSNMPBootup.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapSNMPBootup.setStatus(_A)
class _CommTrapSNMPTPLinkUpDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapSNMPTPLinkUpDown_Type.__name__=_C
_CommTrapSNMPTPLinkUpDown_Object=MibTableColumn
commTrapSNMPTPLinkUpDown=_CommTrapSNMPTPLinkUpDown_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,6),_CommTrapSNMPTPLinkUpDown_Type())
commTrapSNMPTPLinkUpDown.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapSNMPTPLinkUpDown.setStatus(_A)
class _CommTrapSNMPFiberLinkUpDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapSNMPFiberLinkUpDown_Type.__name__=_C
_CommTrapSNMPFiberLinkUpDown_Object=MibTableColumn
commTrapSNMPFiberLinkUpDown=_CommTrapSNMPFiberLinkUpDown_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,7),_CommTrapSNMPFiberLinkUpDown_Type())
commTrapSNMPFiberLinkUpDown.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapSNMPFiberLinkUpDown.setStatus(_A)
class _CommTrapTrapAbnormalTPRXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapTrapAbnormalTPRXError_Type.__name__=_C
_CommTrapTrapAbnormalTPRXError_Object=MibTableColumn
commTrapTrapAbnormalTPRXError=_CommTrapTrapAbnormalTPRXError_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,9),_CommTrapTrapAbnormalTPRXError_Type())
commTrapTrapAbnormalTPRXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalTPRXError.setStatus(_A)
class _CommTrapTrapAbnormalTPTXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapTrapAbnormalTPTXError_Type.__name__=_C
_CommTrapTrapAbnormalTPTXError_Object=MibTableColumn
commTrapTrapAbnormalTPTXError=_CommTrapTrapAbnormalTPTXError_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,10),_CommTrapTrapAbnormalTPTXError_Type())
commTrapTrapAbnormalTPTXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalTPTXError.setStatus(_A)
class _CommTrapTrapAbnormalFiberRXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapTrapAbnormalFiberRXError_Type.__name__=_C
_CommTrapTrapAbnormalFiberRXError_Object=MibTableColumn
commTrapTrapAbnormalFiberRXError=_CommTrapTrapAbnormalFiberRXError_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,11),_CommTrapTrapAbnormalFiberRXError_Type())
commTrapTrapAbnormalFiberRXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalFiberRXError.setStatus(_A)
class _CommTrapTrapAbnormalFiberTXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapTrapAbnormalFiberTXError_Type.__name__=_C
_CommTrapTrapAbnormalFiberTXError_Object=MibTableColumn
commTrapTrapAbnormalFiberTXError=_CommTrapTrapAbnormalFiberTXError_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,12),_CommTrapTrapAbnormalFiberTXError_Type())
commTrapTrapAbnormalFiberTXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalFiberTXError.setStatus(_A)
class _CommTrapTrapPOEPowerFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapTrapPOEPowerFail_Type.__name__=_C
_CommTrapTrapPOEPowerFail_Object=MibTableColumn
commTrapTrapPOEPowerFail=_CommTrapTrapPOEPowerFail_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,13),_CommTrapTrapPOEPowerFail_Type())
commTrapTrapPOEPowerFail.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapPOEPowerFail.setStatus(_A)
class _CommTrapTrapPOEPortOvercurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapTrapPOEPortOvercurrent_Type.__name__=_C
_CommTrapTrapPOEPortOvercurrent_Object=MibTableColumn
commTrapTrapPOEPortOvercurrent=_CommTrapTrapPOEPortOvercurrent_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,14),_CommTrapTrapPOEPortOvercurrent_Type())
commTrapTrapPOEPortOvercurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapPOEPortOvercurrent.setStatus(_A)
class _CommTrapTrapPOEPortShort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_CommTrapTrapPOEPortShort_Type.__name__=_C
_CommTrapTrapPOEPortShort_Object=MibTableColumn
commTrapTrapPOEPortShort=_CommTrapTrapPOEPortShort_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,15),_CommTrapTrapPOEPortShort_Type())
commTrapTrapPOEPortShort.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapPOEPortShort.setStatus(_A)
_CommTrapStatus_Type=RowStatus
_CommTrapStatus_Object=MibTableColumn
commTrapStatus=_CommTrapStatus_Object((1,3,6,1,4,1,171,10,60,1,1,3,1,16),_CommTrapStatus_Type())
commTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapStatus.setStatus(_A)
_CompanyMiscGroup_ObjectIdentity=ObjectIdentity
companyMiscGroup=_CompanyMiscGroup_ObjectIdentity((1,3,6,1,4,1,171,10,60,1,3))
class _MiscStatisticsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_I,2)))
_MiscStatisticsReset_Type.__name__=_C
_MiscStatisticsReset_Object=MibScalar
miscStatisticsReset=_MiscStatisticsReset_Object((1,3,6,1,4,1,171,10,60,1,3,3),_MiscStatisticsReset_Type())
miscStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:miscStatisticsReset.setStatus(_A)
_CompanyConfigGroup_ObjectIdentity=ObjectIdentity
companyConfigGroup=_CompanyConfigGroup_ObjectIdentity((1,3,6,1,4,1,171,10,60,1,11))
class _ConfigVerSwPrimary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ConfigVerSwPrimary_Type.__name__=_H
_ConfigVerSwPrimary_Object=MibScalar
configVerSwPrimary=_ConfigVerSwPrimary_Object((1,3,6,1,4,1,171,10,60,1,11,1),_ConfigVerSwPrimary_Type())
configVerSwPrimary.setMaxAccess(_E)
if mibBuilder.loadTexts:configVerSwPrimary.setStatus(_A)
class _ConfigVerHwChipSet_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ConfigVerHwChipSet_Type.__name__=_H
_ConfigVerHwChipSet_Object=MibScalar
configVerHwChipSet=_ConfigVerHwChipSet_Object((1,3,6,1,4,1,171,10,60,1,11,2),_ConfigVerHwChipSet_Type())
configVerHwChipSet.setMaxAccess(_E)
if mibBuilder.loadTexts:configVerHwChipSet.setStatus(_A)
_ConfigPortTable_Object=MibTable
configPortTable=_ConfigPortTable_Object((1,3,6,1,4,1,171,10,60,1,11,6))
if mibBuilder.loadTexts:configPortTable.setStatus(_A)
_ConfigPortEntry_Object=MibTableRow
configPortEntry=_ConfigPortEntry_Object((1,3,6,1,4,1,171,10,60,1,11,6,1))
configPortEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:configPortEntry.setStatus(_A)
_ConfigPort_Type=Integer32
_ConfigPort_Object=MibTableColumn
configPort=_ConfigPort_Object((1,3,6,1,4,1,171,10,60,1,11,6,1,1),_ConfigPort_Type())
configPort.setMaxAccess(_E)
if mibBuilder.loadTexts:configPort.setStatus(_A)
class _ConfigPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disable',1),('auto',2),(_R,3),(_S,4),(_T,5),(_U,6)))
_ConfigPortSpeed_Type.__name__=_C
_ConfigPortSpeed_Object=MibTableColumn
configPortSpeed=_ConfigPortSpeed_Object((1,3,6,1,4,1,171,10,60,1,11,6,1,2),_ConfigPortSpeed_Type())
configPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortSpeed.setStatus(_A)
class _ConfigPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('down',1),(_R,2),(_S,3),(_T,4),(_U,5),('rate1G-Half',6),('rate1G-Full',7)))
_ConfigPortOperStatus_Type.__name__=_C
_ConfigPortOperStatus_Object=MibTableColumn
configPortOperStatus=_ConfigPortOperStatus_Object((1,3,6,1,4,1,171,10,60,1,11,6,1,3),_ConfigPortOperStatus_Type())
configPortOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:configPortOperStatus.setStatus(_A)
class _ConfigPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_ConfigPortFlowControl_Type.__name__=_C
_ConfigPortFlowControl_Object=MibTableColumn
configPortFlowControl=_ConfigPortFlowControl_Object((1,3,6,1,4,1,171,10,60,1,11,6,1,4),_ConfigPortFlowControl_Type())
configPortFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortFlowControl.setStatus(_A)
class _ConfigPortFlowControlOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_ConfigPortFlowControlOper_Type.__name__=_C
_ConfigPortFlowControlOper_Object=MibTableColumn
configPortFlowControlOper=_ConfigPortFlowControlOper_Object((1,3,6,1,4,1,171,10,60,1,11,6,1,5),_ConfigPortFlowControlOper_Type())
configPortFlowControlOper.setMaxAccess(_E)
if mibBuilder.loadTexts:configPortFlowControlOper.setStatus(_A)
class _ConfigPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('high',2)))
_ConfigPortPriority_Type.__name__=_C
_ConfigPortPriority_Object=MibTableColumn
configPortPriority=_ConfigPortPriority_Object((1,3,6,1,4,1,171,10,60,1,11,6,1,6),_ConfigPortPriority_Type())
configPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortPriority.setStatus(_A)
_ConfigMirrorTable_Object=MibTable
configMirrorTable=_ConfigMirrorTable_Object((1,3,6,1,4,1,171,10,60,1,11,8))
if mibBuilder.loadTexts:configMirrorTable.setStatus(_A)
_ConfigMirrorEntry_Object=MibTableRow
configMirrorEntry=_ConfigMirrorEntry_Object((1,3,6,1,4,1,171,10,60,1,11,8,1))
configMirrorEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:configMirrorEntry.setStatus(_A)
class _ConfigMirrorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ConfigMirrorId_Type.__name__=_C
_ConfigMirrorId_Object=MibTableColumn
configMirrorId=_ConfigMirrorId_Object((1,3,6,1,4,1,171,10,60,1,11,8,1,1),_ConfigMirrorId_Type())
configMirrorId.setMaxAccess(_E)
if mibBuilder.loadTexts:configMirrorId.setStatus(_A)
class _ConfigMirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('Rx',1),('Tx',2),('both',3)))
_ConfigMirrorMode_Type.__name__=_C
_ConfigMirrorMode_Object=MibTableColumn
configMirrorMode=_ConfigMirrorMode_Object((1,3,6,1,4,1,171,10,60,1,11,8,1,2),_ConfigMirrorMode_Type())
configMirrorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorMode.setStatus(_A)
_ConfigMirrorMon_Type=Integer32
_ConfigMirrorMon_Object=MibTableColumn
configMirrorMon=_ConfigMirrorMon_Object((1,3,6,1,4,1,171,10,60,1,11,8,1,3),_ConfigMirrorMon_Type())
configMirrorMon.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorMon.setStatus(_A)
_ConfigMirrorSrc_Type=PortList
_ConfigMirrorSrc_Object=MibTableColumn
configMirrorSrc=_ConfigMirrorSrc_Object((1,3,6,1,4,1,171,10,60,1,11,8,1,4),_ConfigMirrorSrc_Type())
configMirrorSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorSrc.setStatus(_A)
_ConfigMirrorStatus_Type=RowStatus
_ConfigMirrorStatus_Object=MibTableColumn
configMirrorStatus=_ConfigMirrorStatus_Object((1,3,6,1,4,1,171,10,60,1,11,8,1,5),_ConfigMirrorStatus_Type())
configMirrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorStatus.setStatus(_A)
class _ConfigSNMPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_ConfigSNMPEnable_Type.__name__=_C
_ConfigSNMPEnable_Object=MibScalar
configSNMPEnable=_ConfigSNMPEnable_Object((1,3,6,1,4,1,171,10,60,1,11,9),_ConfigSNMPEnable_Type())
configSNMPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configSNMPEnable.setStatus(_A)
class _ConfigIpAssignmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('dhcp',2),('other',3)))
_ConfigIpAssignmentMode_Type.__name__=_C
_ConfigIpAssignmentMode_Object=MibScalar
configIpAssignmentMode=_ConfigIpAssignmentMode_Object((1,3,6,1,4,1,171,10,60,1,11,12),_ConfigIpAssignmentMode_Type())
configIpAssignmentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpAssignmentMode.setStatus(_A)
_ConfigPhysAddress_Type=MacAddress
_ConfigPhysAddress_Object=MibScalar
configPhysAddress=_ConfigPhysAddress_Object((1,3,6,1,4,1,171,10,60,1,11,13),_ConfigPhysAddress_Type())
configPhysAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:configPhysAddress.setStatus(_A)
class _ConfigPasswordAdmin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ConfigPasswordAdmin_Type.__name__=_H
_ConfigPasswordAdmin_Object=MibScalar
configPasswordAdmin=_ConfigPasswordAdmin_Object((1,3,6,1,4,1,171,10,60,1,11,15),_ConfigPasswordAdmin_Type())
configPasswordAdmin.setMaxAccess('write-only')
if mibBuilder.loadTexts:configPasswordAdmin.setStatus(_A)
_ConfigIpAddress_Type=IpAddress
_ConfigIpAddress_Object=MibScalar
configIpAddress=_ConfigIpAddress_Object((1,3,6,1,4,1,171,10,60,1,11,16),_ConfigIpAddress_Type())
configIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpAddress.setStatus(_A)
_ConfigNetMask_Type=IpAddress
_ConfigNetMask_Object=MibScalar
configNetMask=_ConfigNetMask_Object((1,3,6,1,4,1,171,10,60,1,11,17),_ConfigNetMask_Type())
configNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:configNetMask.setStatus(_A)
_ConfigGateway_Type=IpAddress
_ConfigGateway_Object=MibScalar
configGateway=_ConfigGateway_Object((1,3,6,1,4,1,171,10,60,1,11,18),_ConfigGateway_Type())
configGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:configGateway.setStatus(_A)
class _ConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('save',1),(_I,2)))
_ConfigSave_Type.__name__=_C
_ConfigSave_Object=MibScalar
configSave=_ConfigSave_Object((1,3,6,1,4,1,171,10,60,1,11,19),_ConfigSave_Type())
configSave.setMaxAccess(_B)
if mibBuilder.loadTexts:configSave.setStatus(_A)
class _ConfigRestoreDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restore',1),(_I,2)))
_ConfigRestoreDefaults_Type.__name__=_C
_ConfigRestoreDefaults_Object=MibScalar
configRestoreDefaults=_ConfigRestoreDefaults_Object((1,3,6,1,4,1,171,10,60,1,11,22),_ConfigRestoreDefaults_Type())
configRestoreDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:configRestoreDefaults.setStatus(_A)
_CompanyTVlanGroup_ObjectIdentity=ObjectIdentity
companyTVlanGroup=_CompanyTVlanGroup_ObjectIdentity((1,3,6,1,4,1,171,10,60,1,13))
_TvlanTable_Object=MibTable
tvlanTable=_TvlanTable_Object((1,3,6,1,4,1,171,10,60,1,13,1))
if mibBuilder.loadTexts:tvlanTable.setStatus(_A)
_TvlanEntry_Object=MibTableRow
tvlanEntry=_TvlanEntry_Object((1,3,6,1,4,1,171,10,60,1,13,1,1))
tvlanEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:tvlanEntry.setStatus(_A)
_TvlanId_Type=Integer32
_TvlanId_Object=MibTableColumn
tvlanId=_TvlanId_Object((1,3,6,1,4,1,171,10,60,1,13,1,1,1),_TvlanId_Type())
tvlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:tvlanId.setStatus(_A)
_TvlanMember_Type=PortList
_TvlanMember_Object=MibTableColumn
tvlanMember=_TvlanMember_Object((1,3,6,1,4,1,171,10,60,1,13,1,1,3),_TvlanMember_Type())
tvlanMember.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanMember.setStatus(_A)
_TvlanUntaggedPorts_Type=PortList
_TvlanUntaggedPorts_Object=MibTableColumn
tvlanUntaggedPorts=_TvlanUntaggedPorts_Object((1,3,6,1,4,1,171,10,60,1,13,1,1,4),_TvlanUntaggedPorts_Type())
tvlanUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanUntaggedPorts.setStatus(_A)
class _TvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_K,1),(_L,4),(_M,6)))
_TvlanStatus_Type.__name__=_C
_TvlanStatus_Object=MibTableColumn
tvlanStatus=_TvlanStatus_Object((1,3,6,1,4,1,171,10,60,1,13,1,1,5),_TvlanStatus_Type())
tvlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanStatus.setStatus(_A)
_TvlanPortTable_Object=MibTable
tvlanPortTable=_TvlanPortTable_Object((1,3,6,1,4,1,171,10,60,1,13,2))
if mibBuilder.loadTexts:tvlanPortTable.setStatus(_A)
_TvlanPortEntry_Object=MibTableRow
tvlanPortEntry=_TvlanPortEntry_Object((1,3,6,1,4,1,171,10,60,1,13,2,1))
tvlanPortEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:tvlanPortEntry.setStatus(_A)
_TvlanPortPortId_Type=Integer32
_TvlanPortPortId_Object=MibTableColumn
tvlanPortPortId=_TvlanPortPortId_Object((1,3,6,1,4,1,171,10,60,1,13,2,1,1),_TvlanPortPortId_Type())
tvlanPortPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:tvlanPortPortId.setStatus(_A)
_TvlanPortVlanId_Type=Integer32
_TvlanPortVlanId_Object=MibTableColumn
tvlanPortVlanId=_TvlanPortVlanId_Object((1,3,6,1,4,1,171,10,60,1,13,2,1,2),_TvlanPortVlanId_Type())
tvlanPortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanPortVlanId.setStatus(_A)
_CompanyPortTrunkGroup_ObjectIdentity=ObjectIdentity
companyPortTrunkGroup=_CompanyPortTrunkGroup_ObjectIdentity((1,3,6,1,4,1,171,10,60,1,14))
_PortTrunkTable_Object=MibTable
portTrunkTable=_PortTrunkTable_Object((1,3,6,1,4,1,171,10,60,1,14,1))
if mibBuilder.loadTexts:portTrunkTable.setStatus(_A)
_PortTrunkEntry_Object=MibTableRow
portTrunkEntry=_PortTrunkEntry_Object((1,3,6,1,4,1,171,10,60,1,14,1,1))
portTrunkEntry.setIndexNames((0,_G,_Y),(0,_G,_Z))
if mibBuilder.loadTexts:portTrunkEntry.setStatus(_A)
_PortTrunkId_Type=Integer32
_PortTrunkId_Object=MibTableColumn
portTrunkId=_PortTrunkId_Object((1,3,6,1,4,1,171,10,60,1,14,1,1,1),_PortTrunkId_Type())
portTrunkId.setMaxAccess(_E)
if mibBuilder.loadTexts:portTrunkId.setStatus(_A)
_PortTrunkMember_Type=PortList
_PortTrunkMember_Object=MibTableColumn
portTrunkMember=_PortTrunkMember_Object((1,3,6,1,4,1,171,10,60,1,14,1,1,2),_PortTrunkMember_Type())
portTrunkMember.setMaxAccess(_E)
if mibBuilder.loadTexts:portTrunkMember.setStatus(_A)
_PortTrunkMemberValue_Type=PortList
_PortTrunkMemberValue_Object=MibTableColumn
portTrunkMemberValue=_PortTrunkMemberValue_Object((1,3,6,1,4,1,171,10,60,1,14,1,1,3),_PortTrunkMemberValue_Type())
portTrunkMemberValue.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkMemberValue.setStatus(_A)
class _PortTrunkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_D,2)))
_PortTrunkEnable_Type.__name__=_C
_PortTrunkEnable_Object=MibTableColumn
portTrunkEnable=_PortTrunkEnable_Object((1,3,6,1,4,1,171,10,60,1,14,1,1,4),_PortTrunkEnable_Type())
portTrunkEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkEnable.setStatus(_A)
swFiberInsert=NotificationType((1,3,6,1,4,1,171,10,60,1,0,1))
if mibBuilder.loadTexts:swFiberInsert.setStatus('')
swFiberRemove=NotificationType((1,3,6,1,4,1,171,10,60,1,0,2))
if mibBuilder.loadTexts:swFiberRemove.setStatus('')
swFiberAbnormalRXError=NotificationType((1,3,6,1,4,1,171,10,60,1,0,3))
if mibBuilder.loadTexts:swFiberAbnormalRXError.setStatus('')
swFiberAbnormalTXError=NotificationType((1,3,6,1,4,1,171,10,60,1,0,4))
if mibBuilder.loadTexts:swFiberAbnormalTXError.setStatus('')
swTPAbnormalRXError=NotificationType((1,3,6,1,4,1,171,10,60,1,0,5))
if mibBuilder.loadTexts:swTPAbnormalRXError.setStatus('')
swTPAbnormalTXError=NotificationType((1,3,6,1,4,1,171,10,60,1,0,6))
if mibBuilder.loadTexts:swTPAbnormalTXError.setStatus('')
mibBuilder.exportSymbols(_G,**{'OwnerString':OwnerString,'MacAddress':MacAddress,'PortList':PortList,'RowStatus':RowStatus,'d-link':d_link,'dlink-products':dlink_products,'dlink-DES1526SeriesProd':dlink_DES1526SeriesProd,'DES-1526':DES_1526,'swFiberInsert':swFiberInsert,'swFiberRemove':swFiberRemove,'swFiberAbnormalRXError':swFiberAbnormalRXError,'swFiberAbnormalTXError':swFiberAbnormalTXError,'swTPAbnormalRXError':swTPAbnormalRXError,'swTPAbnormalTXError':swTPAbnormalTXError,'companyCommGroup':companyCommGroup,'commSetTable':commSetTable,'commSetEntry':commSetEntry,_N:commSetIndex,'commSetName':commSetName,'commSetStatus':commSetStatus,'commGetTable':commGetTable,'commGetEntry':commGetEntry,_O:commGetIndex,'commGetName':commGetName,'commGetStatus':commGetStatus,'commTrapTable':commTrapTable,'commTrapEntry':commTrapEntry,_P:commTrapIndex,'commTrapName':commTrapName,'commTrapIpAddress':commTrapIpAddress,'commTrapVlanId':commTrapVlanId,'commTrapSNMPBootup':commTrapSNMPBootup,'commTrapSNMPTPLinkUpDown':commTrapSNMPTPLinkUpDown,'commTrapSNMPFiberLinkUpDown':commTrapSNMPFiberLinkUpDown,'commTrapTrapAbnormalTPRXError':commTrapTrapAbnormalTPRXError,'commTrapTrapAbnormalTPTXError':commTrapTrapAbnormalTPTXError,'commTrapTrapAbnormalFiberRXError':commTrapTrapAbnormalFiberRXError,'commTrapTrapAbnormalFiberTXError':commTrapTrapAbnormalFiberTXError,'commTrapTrapPOEPowerFail':commTrapTrapPOEPowerFail,'commTrapTrapPOEPortOvercurrent':commTrapTrapPOEPortOvercurrent,'commTrapTrapPOEPortShort':commTrapTrapPOEPortShort,'commTrapStatus':commTrapStatus,'companyMiscGroup':companyMiscGroup,'miscStatisticsReset':miscStatisticsReset,'companyConfigGroup':companyConfigGroup,'configVerSwPrimary':configVerSwPrimary,'configVerHwChipSet':configVerHwChipSet,'configPortTable':configPortTable,'configPortEntry':configPortEntry,_Q:configPort,'configPortSpeed':configPortSpeed,'configPortOperStatus':configPortOperStatus,'configPortFlowControl':configPortFlowControl,'configPortFlowControlOper':configPortFlowControlOper,'configPortPriority':configPortPriority,'configMirrorTable':configMirrorTable,'configMirrorEntry':configMirrorEntry,_V:configMirrorId,'configMirrorMode':configMirrorMode,'configMirrorMon':configMirrorMon,'configMirrorSrc':configMirrorSrc,'configMirrorStatus':configMirrorStatus,'configSNMPEnable':configSNMPEnable,'configIpAssignmentMode':configIpAssignmentMode,'configPhysAddress':configPhysAddress,'configPasswordAdmin':configPasswordAdmin,'configIpAddress':configIpAddress,'configNetMask':configNetMask,'configGateway':configGateway,'configSave':configSave,'configRestoreDefaults':configRestoreDefaults,'companyTVlanGroup':companyTVlanGroup,'tvlanTable':tvlanTable,'tvlanEntry':tvlanEntry,_W:tvlanId,'tvlanMember':tvlanMember,'tvlanUntaggedPorts':tvlanUntaggedPorts,'tvlanStatus':tvlanStatus,'tvlanPortTable':tvlanPortTable,'tvlanPortEntry':tvlanPortEntry,_X:tvlanPortPortId,'tvlanPortVlanId':tvlanPortVlanId,'companyPortTrunkGroup':companyPortTrunkGroup,'portTrunkTable':portTrunkTable,'portTrunkEntry':portTrunkEntry,_Y:portTrunkId,_Z:portTrunkMember,'portTrunkMemberValue':portTrunkMemberValue,'portTrunkEnable':portTrunkEnable})