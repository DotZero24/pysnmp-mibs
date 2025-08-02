_s='trustedHostID'
_r='dscpIndex'
_q='dot1pPortIndex'
_p='dot1xAuthConfigPortNumber'
_o='igsVlanId'
_n='igsVlanRouterPortListVlanId'
_m='igsVlanMcastFwdGroupAddress'
_l='igsVlanMcastFwdVlanIdMac'
_k='staticId'
_j='portTrunkMember'
_i='portTrunkId'
_h='tvlanPortPortId'
_g='tvlanId'
_f='configMirrorId'
_e='rate1000M-Full'
_d='rate100M-Full'
_c='rate100M-Half'
_b='rate10M-Full'
_a='rate10M-Half'
_Z='configPort'
_Y='upload'
_X='download'
_W='commTrapIndex'
_V='commGetIndex'
_U='commSetIndex'
_T='current'
_S='Unsigned32'
_R='createAndwait'
_Q='notready'
_P='highest'
_O='high'
_N='middle'
_M='low'
_L='not-accessible'
_K='noop'
_J='destroy'
_I='active'
_H='DisplayString'
_G='DES-1228-MIB'
_F='enabled'
_E='disabled'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
class OwnerString(DisplayString):0
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class PortList(TextualConvention,OctetString):status=_T;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class RowStatus(TextualConvention,Integer32):status=_T;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),(_J,6)))
_D_link_ObjectIdentity=ObjectIdentity
d_link=_D_link_ObjectIdentity((1,3,6,1,4,1,171))
_Dlink_products_ObjectIdentity=ObjectIdentity
dlink_products=_Dlink_products_ObjectIdentity((1,3,6,1,4,1,171,10))
_Dlink_DES12XXSeriesProd_ObjectIdentity=ObjectIdentity
dlink_DES12XXSeriesProd=_Dlink_DES12XXSeriesProd_ObjectIdentity((1,3,6,1,4,1,171,10,75))
_Des_1228a1_ObjectIdentity=ObjectIdentity
des_1228a1=_Des_1228a1_ObjectIdentity((1,3,6,1,4,1,171,10,75,2))
_CompanyCommGroup_ObjectIdentity=ObjectIdentity
companyCommGroup=_CompanyCommGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,1))
_CommSetTable_Object=MibTable
commSetTable=_CommSetTable_Object((1,3,6,1,4,1,171,10,75,2,1,1))
if mibBuilder.loadTexts:commSetTable.setStatus(_A)
_CommSetEntry_Object=MibTableRow
commSetEntry=_CommSetEntry_Object((1,3,6,1,4,1,171,10,75,2,1,1,1))
commSetEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:commSetEntry.setStatus(_A)
class _CommSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CommSetIndex_Type.__name__=_C
_CommSetIndex_Object=MibTableColumn
commSetIndex=_CommSetIndex_Object((1,3,6,1,4,1,171,10,75,2,1,1,1,1),_CommSetIndex_Type())
commSetIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:commSetIndex.setStatus(_A)
class _CommSetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CommSetName_Type.__name__=_H
_CommSetName_Object=MibTableColumn
commSetName=_CommSetName_Object((1,3,6,1,4,1,171,10,75,2,1,1,1,2),_CommSetName_Type())
commSetName.setMaxAccess(_B)
if mibBuilder.loadTexts:commSetName.setStatus(_A)
_CommSetStatus_Type=RowStatus
_CommSetStatus_Object=MibTableColumn
commSetStatus=_CommSetStatus_Object((1,3,6,1,4,1,171,10,75,2,1,1,1,3),_CommSetStatus_Type())
commSetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commSetStatus.setStatus(_A)
_CommGetTable_Object=MibTable
commGetTable=_CommGetTable_Object((1,3,6,1,4,1,171,10,75,2,1,2))
if mibBuilder.loadTexts:commGetTable.setStatus(_A)
_CommGetEntry_Object=MibTableRow
commGetEntry=_CommGetEntry_Object((1,3,6,1,4,1,171,10,75,2,1,2,1))
commGetEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:commGetEntry.setStatus(_A)
class _CommGetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CommGetIndex_Type.__name__=_C
_CommGetIndex_Object=MibTableColumn
commGetIndex=_CommGetIndex_Object((1,3,6,1,4,1,171,10,75,2,1,2,1,1),_CommGetIndex_Type())
commGetIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:commGetIndex.setStatus(_A)
class _CommGetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CommGetName_Type.__name__=_H
_CommGetName_Object=MibTableColumn
commGetName=_CommGetName_Object((1,3,6,1,4,1,171,10,75,2,1,2,1,2),_CommGetName_Type())
commGetName.setMaxAccess(_B)
if mibBuilder.loadTexts:commGetName.setStatus(_A)
_CommGetStatus_Type=RowStatus
_CommGetStatus_Object=MibTableColumn
commGetStatus=_CommGetStatus_Object((1,3,6,1,4,1,171,10,75,2,1,2,1,3),_CommGetStatus_Type())
commGetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commGetStatus.setStatus(_A)
_CommTrapTable_Object=MibTable
commTrapTable=_CommTrapTable_Object((1,3,6,1,4,1,171,10,75,2,1,3))
if mibBuilder.loadTexts:commTrapTable.setStatus(_A)
_CommTrapEntry_Object=MibTableRow
commTrapEntry=_CommTrapEntry_Object((1,3,6,1,4,1,171,10,75,2,1,3,1))
commTrapEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:commTrapEntry.setStatus(_A)
class _CommTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CommTrapIndex_Type.__name__=_C
_CommTrapIndex_Object=MibTableColumn
commTrapIndex=_CommTrapIndex_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,1),_CommTrapIndex_Type())
commTrapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:commTrapIndex.setStatus(_A)
class _CommTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CommTrapName_Type.__name__=_H
_CommTrapName_Object=MibTableColumn
commTrapName=_CommTrapName_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,2),_CommTrapName_Type())
commTrapName.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapName.setStatus(_A)
_CommTrapIpAddress_Type=IpAddress
_CommTrapIpAddress_Object=MibTableColumn
commTrapIpAddress=_CommTrapIpAddress_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,3),_CommTrapIpAddress_Type())
commTrapIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapIpAddress.setStatus(_A)
class _CommTrapSNMPBootup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_CommTrapSNMPBootup_Type.__name__=_C
_CommTrapSNMPBootup_Object=MibTableColumn
commTrapSNMPBootup=_CommTrapSNMPBootup_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,5),_CommTrapSNMPBootup_Type())
commTrapSNMPBootup.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapSNMPBootup.setStatus(_A)
class _CommTrapSNMPTPLinkUpDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_CommTrapSNMPTPLinkUpDown_Type.__name__=_C
_CommTrapSNMPTPLinkUpDown_Object=MibTableColumn
commTrapSNMPTPLinkUpDown=_CommTrapSNMPTPLinkUpDown_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,6),_CommTrapSNMPTPLinkUpDown_Type())
commTrapSNMPTPLinkUpDown.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapSNMPTPLinkUpDown.setStatus(_A)
class _CommTrapSNMPFiberLinkUpDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_CommTrapSNMPFiberLinkUpDown_Type.__name__=_C
_CommTrapSNMPFiberLinkUpDown_Object=MibTableColumn
commTrapSNMPFiberLinkUpDown=_CommTrapSNMPFiberLinkUpDown_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,7),_CommTrapSNMPFiberLinkUpDown_Type())
commTrapSNMPFiberLinkUpDown.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapSNMPFiberLinkUpDown.setStatus(_A)
class _CommTrapTrapAbnormalTPRXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_CommTrapTrapAbnormalTPRXError_Type.__name__=_C
_CommTrapTrapAbnormalTPRXError_Object=MibTableColumn
commTrapTrapAbnormalTPRXError=_CommTrapTrapAbnormalTPRXError_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,9),_CommTrapTrapAbnormalTPRXError_Type())
commTrapTrapAbnormalTPRXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalTPRXError.setStatus(_A)
class _CommTrapTrapAbnormalTPTXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_CommTrapTrapAbnormalTPTXError_Type.__name__=_C
_CommTrapTrapAbnormalTPTXError_Object=MibTableColumn
commTrapTrapAbnormalTPTXError=_CommTrapTrapAbnormalTPTXError_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,10),_CommTrapTrapAbnormalTPTXError_Type())
commTrapTrapAbnormalTPTXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalTPTXError.setStatus(_A)
class _CommTrapTrapAbnormalFiberRXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_CommTrapTrapAbnormalFiberRXError_Type.__name__=_C
_CommTrapTrapAbnormalFiberRXError_Object=MibTableColumn
commTrapTrapAbnormalFiberRXError=_CommTrapTrapAbnormalFiberRXError_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,11),_CommTrapTrapAbnormalFiberRXError_Type())
commTrapTrapAbnormalFiberRXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalFiberRXError.setStatus(_A)
class _CommTrapTrapAbnormalFiberTXError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_CommTrapTrapAbnormalFiberTXError_Type.__name__=_C
_CommTrapTrapAbnormalFiberTXError_Object=MibTableColumn
commTrapTrapAbnormalFiberTXError=_CommTrapTrapAbnormalFiberTXError_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,12),_CommTrapTrapAbnormalFiberTXError_Type())
commTrapTrapAbnormalFiberTXError.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapTrapAbnormalFiberTXError.setStatus(_A)
_CommTrapStatus_Type=RowStatus
_CommTrapStatus_Object=MibTableColumn
commTrapStatus=_CommTrapStatus_Object((1,3,6,1,4,1,171,10,75,2,1,3,1,13),_CommTrapStatus_Type())
commTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commTrapStatus.setStatus(_A)
_CompanyMiscGroup_ObjectIdentity=ObjectIdentity
companyMiscGroup=_CompanyMiscGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,3))
class _MiscReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_K,2)))
_MiscReset_Type.__name__=_C
_MiscReset_Object=MibScalar
miscReset=_MiscReset_Object((1,3,6,1,4,1,171,10,75,2,3,2),_MiscReset_Type())
miscReset.setMaxAccess(_B)
if mibBuilder.loadTexts:miscReset.setStatus(_A)
class _MiscStatisticsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_K,2)))
_MiscStatisticsReset_Type.__name__=_C
_MiscStatisticsReset_Object=MibScalar
miscStatisticsReset=_MiscStatisticsReset_Object((1,3,6,1,4,1,171,10,75,2,3,3),_MiscStatisticsReset_Type())
miscStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:miscStatisticsReset.setStatus(_A)
_CompanySpanGroup_ObjectIdentity=ObjectIdentity
companySpanGroup=_CompanySpanGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,4))
class _SpanOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SpanOnOff_Type.__name__=_C
_SpanOnOff_Object=MibScalar
spanOnOff=_SpanOnOff_Object((1,3,6,1,4,1,171,10,75,2,4,1),_SpanOnOff_Type())
spanOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:spanOnOff.setStatus(_A)
_CompanyConfigGroup_ObjectIdentity=ObjectIdentity
companyConfigGroup=_CompanyConfigGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,11))
class _ConfigVerSwPrimary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ConfigVerSwPrimary_Type.__name__=_H
_ConfigVerSwPrimary_Object=MibScalar
configVerSwPrimary=_ConfigVerSwPrimary_Object((1,3,6,1,4,1,171,10,75,2,11,1),_ConfigVerSwPrimary_Type())
configVerSwPrimary.setMaxAccess(_D)
if mibBuilder.loadTexts:configVerSwPrimary.setStatus(_A)
class _ConfigVerHwChipSet_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ConfigVerHwChipSet_Type.__name__=_H
_ConfigVerHwChipSet_Object=MibScalar
configVerHwChipSet=_ConfigVerHwChipSet_Object((1,3,6,1,4,1,171,10,75,2,11,2),_ConfigVerHwChipSet_Type())
configVerHwChipSet.setMaxAccess(_D)
if mibBuilder.loadTexts:configVerHwChipSet.setStatus(_A)
class _ConfigBootTftpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_ConfigBootTftpOperation_Type.__name__=_C
_ConfigBootTftpOperation_Object=MibScalar
configBootTftpOperation=_ConfigBootTftpOperation_Object((1,3,6,1,4,1,171,10,75,2,11,3),_ConfigBootTftpOperation_Type())
configBootTftpOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:configBootTftpOperation.setStatus(_A)
_ConfigBootTftpServerIp_Type=IpAddress
_ConfigBootTftpServerIp_Object=MibScalar
configBootTftpServerIp=_ConfigBootTftpServerIp_Object((1,3,6,1,4,1,171,10,75,2,11,4),_ConfigBootTftpServerIp_Type())
configBootTftpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:configBootTftpServerIp.setStatus(_A)
class _ConfigBootImageFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ConfigBootImageFileName_Type.__name__=_H
_ConfigBootImageFileName_Object=MibScalar
configBootImageFileName=_ConfigBootImageFileName_Object((1,3,6,1,4,1,171,10,75,2,11,5),_ConfigBootImageFileName_Type())
configBootImageFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:configBootImageFileName.setStatus(_A)
_ConfigPortTable_Object=MibTable
configPortTable=_ConfigPortTable_Object((1,3,6,1,4,1,171,10,75,2,11,6))
if mibBuilder.loadTexts:configPortTable.setStatus(_A)
_ConfigPortEntry_Object=MibTableRow
configPortEntry=_ConfigPortEntry_Object((1,3,6,1,4,1,171,10,75,2,11,6,1))
configPortEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:configPortEntry.setStatus(_A)
_ConfigPort_Type=Integer32
_ConfigPort_Object=MibTableColumn
configPort=_ConfigPort_Object((1,3,6,1,4,1,171,10,75,2,11,6,1,1),_ConfigPort_Type())
configPort.setMaxAccess(_D)
if mibBuilder.loadTexts:configPort.setStatus(_A)
class _ConfigPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disable',1),('auto',2),(_a,3),(_b,4),(_c,5),(_d,6),(_e,7)))
_ConfigPortSpeed_Type.__name__=_C
_ConfigPortSpeed_Object=MibTableColumn
configPortSpeed=_ConfigPortSpeed_Object((1,3,6,1,4,1,171,10,75,2,11,6,1,2),_ConfigPortSpeed_Type())
configPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortSpeed.setStatus(_A)
class _ConfigPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('down',1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6)))
_ConfigPortOperStatus_Type.__name__=_C
_ConfigPortOperStatus_Object=MibTableColumn
configPortOperStatus=_ConfigPortOperStatus_Object((1,3,6,1,4,1,171,10,75,2,11,6,1,3),_ConfigPortOperStatus_Type())
configPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:configPortOperStatus.setStatus(_A)
class _ConfigPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_ConfigPortPriority_Type.__name__=_C
_ConfigPortPriority_Object=MibTableColumn
configPortPriority=_ConfigPortPriority_Object((1,3,6,1,4,1,171,10,75,2,11,6,1,6),_ConfigPortPriority_Type())
configPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:configPortPriority.setStatus(_A)
class _ConfigVLANMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('modeTagBased',1))
_ConfigVLANMode_Type.__name__=_C
_ConfigVLANMode_Object=MibScalar
configVLANMode=_ConfigVLANMode_Object((1,3,6,1,4,1,171,10,75,2,11,7),_ConfigVLANMode_Type())
configVLANMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configVLANMode.setStatus(_A)
_ConfigMirrorTable_Object=MibTable
configMirrorTable=_ConfigMirrorTable_Object((1,3,6,1,4,1,171,10,75,2,11,8))
if mibBuilder.loadTexts:configMirrorTable.setStatus(_A)
_ConfigMirrorEntry_Object=MibTableRow
configMirrorEntry=_ConfigMirrorEntry_Object((1,3,6,1,4,1,171,10,75,2,11,8,1))
configMirrorEntry.setIndexNames((0,_G,_f))
if mibBuilder.loadTexts:configMirrorEntry.setStatus(_A)
class _ConfigMirrorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ConfigMirrorId_Type.__name__=_C
_ConfigMirrorId_Object=MibTableColumn
configMirrorId=_ConfigMirrorId_Object((1,3,6,1,4,1,171,10,75,2,11,8,1,1),_ConfigMirrorId_Type())
configMirrorId.setMaxAccess(_D)
if mibBuilder.loadTexts:configMirrorId.setStatus(_A)
_ConfigMirrorMon_Type=Integer32
_ConfigMirrorMon_Object=MibTableColumn
configMirrorMon=_ConfigMirrorMon_Object((1,3,6,1,4,1,171,10,75,2,11,8,1,2),_ConfigMirrorMon_Type())
configMirrorMon.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorMon.setStatus(_A)
_ConfigMirrorTXSrc_Type=PortList
_ConfigMirrorTXSrc_Object=MibTableColumn
configMirrorTXSrc=_ConfigMirrorTXSrc_Object((1,3,6,1,4,1,171,10,75,2,11,8,1,3),_ConfigMirrorTXSrc_Type())
configMirrorTXSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorTXSrc.setStatus(_A)
_ConfigMirrorRXSrc_Type=PortList
_ConfigMirrorRXSrc_Object=MibTableColumn
configMirrorRXSrc=_ConfigMirrorRXSrc_Object((1,3,6,1,4,1,171,10,75,2,11,8,1,4),_ConfigMirrorRXSrc_Type())
configMirrorRXSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorRXSrc.setStatus(_A)
_ConfigMirrorStatus_Type=RowStatus
_ConfigMirrorStatus_Object=MibTableColumn
configMirrorStatus=_ConfigMirrorStatus_Object((1,3,6,1,4,1,171,10,75,2,11,8,1,5),_ConfigMirrorStatus_Type())
configMirrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configMirrorStatus.setStatus(_A)
class _ConfigSNMPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_ConfigSNMPEnable_Type.__name__=_C
_ConfigSNMPEnable_Object=MibScalar
configSNMPEnable=_ConfigSNMPEnable_Object((1,3,6,1,4,1,171,10,75,2,11,9),_ConfigSNMPEnable_Type())
configSNMPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configSNMPEnable.setStatus(_A)
class _ConfigIpAssignmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('dhcp',2),('other',3)))
_ConfigIpAssignmentMode_Type.__name__=_C
_ConfigIpAssignmentMode_Object=MibScalar
configIpAssignmentMode=_ConfigIpAssignmentMode_Object((1,3,6,1,4,1,171,10,75,2,11,12),_ConfigIpAssignmentMode_Type())
configIpAssignmentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpAssignmentMode.setStatus(_A)
_ConfigPhysAddress_Type=MacAddress
_ConfigPhysAddress_Object=MibScalar
configPhysAddress=_ConfigPhysAddress_Object((1,3,6,1,4,1,171,10,75,2,11,13),_ConfigPhysAddress_Type())
configPhysAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:configPhysAddress.setStatus(_A)
class _ConfigPasswordAdmin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ConfigPasswordAdmin_Type.__name__=_H
_ConfigPasswordAdmin_Object=MibScalar
configPasswordAdmin=_ConfigPasswordAdmin_Object((1,3,6,1,4,1,171,10,75,2,11,15),_ConfigPasswordAdmin_Type())
configPasswordAdmin.setMaxAccess('write-only')
if mibBuilder.loadTexts:configPasswordAdmin.setStatus(_A)
_ConfigIpAddress_Type=IpAddress
_ConfigIpAddress_Object=MibScalar
configIpAddress=_ConfigIpAddress_Object((1,3,6,1,4,1,171,10,75,2,11,16),_ConfigIpAddress_Type())
configIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpAddress.setStatus(_A)
_ConfigNetMask_Type=IpAddress
_ConfigNetMask_Object=MibScalar
configNetMask=_ConfigNetMask_Object((1,3,6,1,4,1,171,10,75,2,11,17),_ConfigNetMask_Type())
configNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:configNetMask.setStatus(_A)
_ConfigGateway_Type=IpAddress
_ConfigGateway_Object=MibScalar
configGateway=_ConfigGateway_Object((1,3,6,1,4,1,171,10,75,2,11,18),_ConfigGateway_Type())
configGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:configGateway.setStatus(_A)
class _ConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('save',1),(_K,2)))
_ConfigSave_Type.__name__=_C
_ConfigSave_Object=MibScalar
configSave=_ConfigSave_Object((1,3,6,1,4,1,171,10,75,2,11,19),_ConfigSave_Type())
configSave.setMaxAccess(_B)
if mibBuilder.loadTexts:configSave.setStatus(_A)
class _ConfigRestoreDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restore',1),(_K,2)))
_ConfigRestoreDefaults_Type.__name__=_C
_ConfigRestoreDefaults_Object=MibScalar
configRestoreDefaults=_ConfigRestoreDefaults_Object((1,3,6,1,4,1,171,10,75,2,11,22),_ConfigRestoreDefaults_Type())
configRestoreDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:configRestoreDefaults.setStatus(_A)
_ConfigTftpServerIpAddress_Type=IpAddress
_ConfigTftpServerIpAddress_Object=MibScalar
configTftpServerIpAddress=_ConfigTftpServerIpAddress_Object((1,3,6,1,4,1,171,10,75,2,11,32),_ConfigTftpServerIpAddress_Type())
configTftpServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configTftpServerIpAddress.setStatus(_A)
class _ConfigTftpServerFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ConfigTftpServerFileName_Type.__name__=_H
_ConfigTftpServerFileName_Object=MibScalar
configTftpServerFileName=_ConfigTftpServerFileName_Object((1,3,6,1,4,1,171,10,75,2,11,33),_ConfigTftpServerFileName_Type())
configTftpServerFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:configTftpServerFileName.setStatus(_A)
class _ConfigTftpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_ConfigTftpOperation_Type.__name__=_C
_ConfigTftpOperation_Object=MibScalar
configTftpOperation=_ConfigTftpOperation_Object((1,3,6,1,4,1,171,10,75,2,11,34),_ConfigTftpOperation_Type())
configTftpOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:configTftpOperation.setStatus(_A)
class _ConfigSafeguardEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_ConfigSafeguardEnable_Type.__name__=_C
_ConfigSafeguardEnable_Object=MibScalar
configSafeguardEnable=_ConfigSafeguardEnable_Object((1,3,6,1,4,1,171,10,75,2,11,44),_ConfigSafeguardEnable_Type())
configSafeguardEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configSafeguardEnable.setStatus(_A)
_CompanyTVlanGroup_ObjectIdentity=ObjectIdentity
companyTVlanGroup=_CompanyTVlanGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,13))
_TvlanTable_Object=MibTable
tvlanTable=_TvlanTable_Object((1,3,6,1,4,1,171,10,75,2,13,1))
if mibBuilder.loadTexts:tvlanTable.setStatus(_A)
_TvlanEntry_Object=MibTableRow
tvlanEntry=_TvlanEntry_Object((1,3,6,1,4,1,171,10,75,2,13,1,1))
tvlanEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:tvlanEntry.setStatus(_A)
_TvlanId_Type=Integer32
_TvlanId_Object=MibTableColumn
tvlanId=_TvlanId_Object((1,3,6,1,4,1,171,10,75,2,13,1,1,1),_TvlanId_Type())
tvlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:tvlanId.setStatus(_A)
_TvlanName_Type=DisplayString
_TvlanName_Object=MibTableColumn
tvlanName=_TvlanName_Object((1,3,6,1,4,1,171,10,75,2,13,1,1,2),_TvlanName_Type())
tvlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanName.setStatus(_A)
_TvlanMember_Type=PortList
_TvlanMember_Object=MibTableColumn
tvlanMember=_TvlanMember_Object((1,3,6,1,4,1,171,10,75,2,13,1,1,3),_TvlanMember_Type())
tvlanMember.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanMember.setStatus(_A)
_TvlanUntaggedPorts_Type=PortList
_TvlanUntaggedPorts_Object=MibTableColumn
tvlanUntaggedPorts=_TvlanUntaggedPorts_Object((1,3,6,1,4,1,171,10,75,2,13,1,1,4),_TvlanUntaggedPorts_Type())
tvlanUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanUntaggedPorts.setStatus(_A)
class _TvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,6)));namedValues=NamedValues(*((_I,1),(_Q,3),(_R,5),(_J,6)))
_TvlanStatus_Type.__name__=_C
_TvlanStatus_Object=MibTableColumn
tvlanStatus=_TvlanStatus_Object((1,3,6,1,4,1,171,10,75,2,13,1,1,5),_TvlanStatus_Type())
tvlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanStatus.setStatus(_A)
class _TvlanManagementOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TvlanManagementOnOff_Type.__name__=_C
_TvlanManagementOnOff_Object=MibScalar
tvlanManagementOnOff=_TvlanManagementOnOff_Object((1,3,6,1,4,1,171,10,75,2,13,2),_TvlanManagementOnOff_Type())
tvlanManagementOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanManagementOnOff.setStatus(_A)
_TvlanManagementid_Type=Integer32
_TvlanManagementid_Object=MibScalar
tvlanManagementid=_TvlanManagementid_Object((1,3,6,1,4,1,171,10,75,2,13,3),_TvlanManagementid_Type())
tvlanManagementid.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanManagementid.setStatus(_A)
_TvlanPortTable_Object=MibTable
tvlanPortTable=_TvlanPortTable_Object((1,3,6,1,4,1,171,10,75,2,13,4))
if mibBuilder.loadTexts:tvlanPortTable.setStatus(_A)
_TvlanPortEntry_Object=MibTableRow
tvlanPortEntry=_TvlanPortEntry_Object((1,3,6,1,4,1,171,10,75,2,13,4,1))
tvlanPortEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:tvlanPortEntry.setStatus(_A)
_TvlanPortPortId_Type=Integer32
_TvlanPortPortId_Object=MibTableColumn
tvlanPortPortId=_TvlanPortPortId_Object((1,3,6,1,4,1,171,10,75,2,13,4,1,1),_TvlanPortPortId_Type())
tvlanPortPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tvlanPortPortId.setStatus(_A)
_TvlanPortVlanId_Type=Integer32
_TvlanPortVlanId_Object=MibTableColumn
tvlanPortVlanId=_TvlanPortVlanId_Object((1,3,6,1,4,1,171,10,75,2,13,4,1,2),_TvlanPortVlanId_Type())
tvlanPortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanPortVlanId.setStatus(_A)
class _TvlanAsyOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TvlanAsyOnOff_Type.__name__=_C
_TvlanAsyOnOff_Object=MibScalar
tvlanAsyOnOff=_TvlanAsyOnOff_Object((1,3,6,1,4,1,171,10,75,2,13,5),_TvlanAsyOnOff_Type())
tvlanAsyOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:tvlanAsyOnOff.setStatus(_A)
_CompanyPortTrunkGroup_ObjectIdentity=ObjectIdentity
companyPortTrunkGroup=_CompanyPortTrunkGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,14))
_PortTrunkTable_Object=MibTable
portTrunkTable=_PortTrunkTable_Object((1,3,6,1,4,1,171,10,75,2,14,1))
if mibBuilder.loadTexts:portTrunkTable.setStatus(_A)
_PortTrunkEntry_Object=MibTableRow
portTrunkEntry=_PortTrunkEntry_Object((1,3,6,1,4,1,171,10,75,2,14,1,1))
portTrunkEntry.setIndexNames((0,_G,_i),(0,_G,_j))
if mibBuilder.loadTexts:portTrunkEntry.setStatus(_A)
_PortTrunkId_Type=Integer32
_PortTrunkId_Object=MibTableColumn
portTrunkId=_PortTrunkId_Object((1,3,6,1,4,1,171,10,75,2,14,1,1,1),_PortTrunkId_Type())
portTrunkId.setMaxAccess(_D)
if mibBuilder.loadTexts:portTrunkId.setStatus(_A)
_PortTrunkName_Type=DisplayString
_PortTrunkName_Object=MibTableColumn
portTrunkName=_PortTrunkName_Object((1,3,6,1,4,1,171,10,75,2,14,1,1,2),_PortTrunkName_Type())
portTrunkName.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkName.setStatus(_A)
_PortTrunkMember_Type=PortList
_PortTrunkMember_Object=MibTableColumn
portTrunkMember=_PortTrunkMember_Object((1,3,6,1,4,1,171,10,75,2,14,1,1,3),_PortTrunkMember_Type())
portTrunkMember.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkMember.setStatus(_A)
_CompanyStaticGroup_ObjectIdentity=ObjectIdentity
companyStaticGroup=_CompanyStaticGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,21))
class _StaticOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_StaticOnOff_Type.__name__=_C
_StaticOnOff_Object=MibScalar
staticOnOff=_StaticOnOff_Object((1,3,6,1,4,1,171,10,75,2,21,1),_StaticOnOff_Type())
staticOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:staticOnOff.setStatus(_A)
_StaticAutoLearning_Type=PortList
_StaticAutoLearning_Object=MibScalar
staticAutoLearning=_StaticAutoLearning_Object((1,3,6,1,4,1,171,10,75,2,21,2),_StaticAutoLearning_Type())
staticAutoLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:staticAutoLearning.setStatus(_A)
_StaticTable_Object=MibTable
staticTable=_StaticTable_Object((1,3,6,1,4,1,171,10,75,2,21,3))
if mibBuilder.loadTexts:staticTable.setStatus(_A)
_StaticEntry_Object=MibTableRow
staticEntry=_StaticEntry_Object((1,3,6,1,4,1,171,10,75,2,21,3,1))
staticEntry.setIndexNames((0,_G,_k))
if mibBuilder.loadTexts:staticEntry.setStatus(_A)
_StaticId_Type=Integer32
_StaticId_Object=MibTableColumn
staticId=_StaticId_Object((1,3,6,1,4,1,171,10,75,2,21,3,1,1),_StaticId_Type())
staticId.setMaxAccess(_D)
if mibBuilder.loadTexts:staticId.setStatus(_A)
_StaticMac_Type=MacAddress
_StaticMac_Object=MibTableColumn
staticMac=_StaticMac_Object((1,3,6,1,4,1,171,10,75,2,21,3,1,2),_StaticMac_Type())
staticMac.setMaxAccess(_B)
if mibBuilder.loadTexts:staticMac.setStatus(_A)
_StaticPort_Type=Integer32
_StaticPort_Object=MibTableColumn
staticPort=_StaticPort_Object((1,3,6,1,4,1,171,10,75,2,21,3,1,3),_StaticPort_Type())
staticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:staticPort.setStatus(_A)
_StaticVlanID_Type=Integer32
_StaticVlanID_Object=MibTableColumn
staticVlanID=_StaticVlanID_Object((1,3,6,1,4,1,171,10,75,2,21,3,1,4),_StaticVlanID_Type())
staticVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:staticVlanID.setStatus(_A)
class _StaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,6)));namedValues=NamedValues(*((_I,1),(_Q,3),(_R,5),(_J,6)))
_StaticStatus_Type.__name__=_C
_StaticStatus_Object=MibTableColumn
staticStatus=_StaticStatus_Object((1,3,6,1,4,1,171,10,75,2,21,3,1,5),_StaticStatus_Type())
staticStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:staticStatus.setStatus(_A)
_CompanyIgsGroup_ObjectIdentity=ObjectIdentity
companyIgsGroup=_CompanyIgsGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,22))
_IgsSystem_ObjectIdentity=ObjectIdentity
igsSystem=_IgsSystem_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,22,1))
class _IgsStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IgsStatus_Type.__name__=_C
_IgsStatus_Object=MibScalar
igsStatus=_IgsStatus_Object((1,3,6,1,4,1,171,10,75,2,22,1,2),_IgsStatus_Type())
igsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igsStatus.setStatus(_A)
class _Igsv3Processing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_Igsv3Processing_Type.__name__=_C
_Igsv3Processing_Object=MibScalar
igsv3Processing=_Igsv3Processing_Object((1,3,6,1,4,1,171,10,75,2,22,1,3),_Igsv3Processing_Type())
igsv3Processing.setMaxAccess(_D)
if mibBuilder.loadTexts:igsv3Processing.setStatus(_A)
class _IgsRouterPortPurgeInterval_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_IgsRouterPortPurgeInterval_Type.__name__=_C
_IgsRouterPortPurgeInterval_Object=MibScalar
igsRouterPortPurgeInterval=_IgsRouterPortPurgeInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,4),_IgsRouterPortPurgeInterval_Type())
igsRouterPortPurgeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:igsRouterPortPurgeInterval.setStatus(_A)
class _IgsHostPortPurgeInterval_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(130,153025))
_IgsHostPortPurgeInterval_Type.__name__=_C
_IgsHostPortPurgeInterval_Object=MibScalar
igsHostPortPurgeInterval=_IgsHostPortPurgeInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,5),_IgsHostPortPurgeInterval_Type())
igsHostPortPurgeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:igsHostPortPurgeInterval.setStatus(_A)
class _IgsReportForwardInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_IgsReportForwardInterval_Type.__name__=_C
_IgsReportForwardInterval_Object=MibScalar
igsReportForwardInterval=_IgsReportForwardInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,6),_IgsReportForwardInterval_Type())
igsReportForwardInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:igsReportForwardInterval.setStatus(_A)
class _IgsLeaveProcessInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_IgsLeaveProcessInterval_Type.__name__=_C
_IgsLeaveProcessInterval_Object=MibScalar
igsLeaveProcessInterval=_IgsLeaveProcessInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,7),_IgsLeaveProcessInterval_Type())
igsLeaveProcessInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:igsLeaveProcessInterval.setStatus(_A)
class _IgsMcastEntryAgeingInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_IgsMcastEntryAgeingInterval_Type.__name__=_C
_IgsMcastEntryAgeingInterval_Object=MibScalar
igsMcastEntryAgeingInterval=_IgsMcastEntryAgeingInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,8),_IgsMcastEntryAgeingInterval_Type())
igsMcastEntryAgeingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:igsMcastEntryAgeingInterval.setStatus(_A)
class _IgsSharedSegmentAggregationInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IgsSharedSegmentAggregationInterval_Type.__name__=_C
_IgsSharedSegmentAggregationInterval_Object=MibScalar
igsSharedSegmentAggregationInterval=_IgsSharedSegmentAggregationInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,9),_IgsSharedSegmentAggregationInterval_Type())
igsSharedSegmentAggregationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:igsSharedSegmentAggregationInterval.setStatus(_A)
class _IgsGblReportFwdOnAllPorts_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allports',1),('rtrports',2)))
_IgsGblReportFwdOnAllPorts_Type.__name__=_C
_IgsGblReportFwdOnAllPorts_Object=MibScalar
igsGblReportFwdOnAllPorts=_IgsGblReportFwdOnAllPorts_Object((1,3,6,1,4,1,171,10,75,2,22,1,10),_IgsGblReportFwdOnAllPorts_Type())
igsGblReportFwdOnAllPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:igsGblReportFwdOnAllPorts.setStatus(_A)
class _IgsNextMcastFwdMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipbased',1),('macbased',2)))
_IgsNextMcastFwdMode_Type.__name__=_C
_IgsNextMcastFwdMode_Object=MibScalar
igsNextMcastFwdMode=_IgsNextMcastFwdMode_Object((1,3,6,1,4,1,171,10,75,2,22,1,13),_IgsNextMcastFwdMode_Type())
igsNextMcastFwdMode.setMaxAccess(_D)
if mibBuilder.loadTexts:igsNextMcastFwdMode.setStatus(_A)
class _IgsQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_IgsQueryInterval_Type.__name__=_C
_IgsQueryInterval_Object=MibScalar
igsQueryInterval=_IgsQueryInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,14),_IgsQueryInterval_Type())
igsQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:igsQueryInterval.setStatus(_A)
class _IgsQueryMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,25))
_IgsQueryMaxResponseTime_Type.__name__=_C
_IgsQueryMaxResponseTime_Object=MibScalar
igsQueryMaxResponseTime=_IgsQueryMaxResponseTime_Object((1,3,6,1,4,1,171,10,75,2,22,1,15),_IgsQueryMaxResponseTime_Type())
igsQueryMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:igsQueryMaxResponseTime.setStatus(_A)
class _IgsRobustnessValue_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,255))
_IgsRobustnessValue_Type.__name__=_C
_IgsRobustnessValue_Object=MibScalar
igsRobustnessValue=_IgsRobustnessValue_Object((1,3,6,1,4,1,171,10,75,2,22,1,16),_IgsRobustnessValue_Type())
igsRobustnessValue.setMaxAccess(_B)
if mibBuilder.loadTexts:igsRobustnessValue.setStatus(_A)
class _IgsLastMembQueryInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_IgsLastMembQueryInterval_Type.__name__=_C
_IgsLastMembQueryInterval_Object=MibScalar
igsLastMembQueryInterval=_IgsLastMembQueryInterval_Object((1,3,6,1,4,1,171,10,75,2,22,1,17),_IgsLastMembQueryInterval_Type())
igsLastMembQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:igsLastMembQueryInterval.setStatus(_A)
class _IgsQuerierStateOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IgsQuerierStateOnOff_Type.__name__=_C
_IgsQuerierStateOnOff_Object=MibScalar
igsQuerierStateOnOff=_IgsQuerierStateOnOff_Object((1,3,6,1,4,1,171,10,75,2,22,1,18),_IgsQuerierStateOnOff_Type())
igsQuerierStateOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:igsQuerierStateOnOff.setStatus(_A)
_IgsVlan_ObjectIdentity=ObjectIdentity
igsVlan=_IgsVlan_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,22,3))
_IgsVlanMcastFwdTable_Object=MibTable
igsVlanMcastFwdTable=_IgsVlanMcastFwdTable_Object((1,3,6,1,4,1,171,10,75,2,22,3,1))
if mibBuilder.loadTexts:igsVlanMcastFwdTable.setStatus(_A)
_IgsVlanMcastFwdEntry_Object=MibTableRow
igsVlanMcastFwdEntry=_IgsVlanMcastFwdEntry_Object((1,3,6,1,4,1,171,10,75,2,22,3,1,1))
igsVlanMcastFwdEntry.setIndexNames((0,_G,_l),(0,_G,_m))
if mibBuilder.loadTexts:igsVlanMcastFwdEntry.setStatus(_A)
class _IgsVlanMcastFwdVlanIdMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IgsVlanMcastFwdVlanIdMac_Type.__name__=_C
_IgsVlanMcastFwdVlanIdMac_Object=MibTableColumn
igsVlanMcastFwdVlanIdMac=_IgsVlanMcastFwdVlanIdMac_Object((1,3,6,1,4,1,171,10,75,2,22,3,1,1,1),_IgsVlanMcastFwdVlanIdMac_Type())
igsVlanMcastFwdVlanIdMac.setMaxAccess(_L)
if mibBuilder.loadTexts:igsVlanMcastFwdVlanIdMac.setStatus(_A)
_IgsVlanMcastFwdGroupAddress_Type=MacAddress
_IgsVlanMcastFwdGroupAddress_Object=MibTableColumn
igsVlanMcastFwdGroupAddress=_IgsVlanMcastFwdGroupAddress_Object((1,3,6,1,4,1,171,10,75,2,22,3,1,1,2),_IgsVlanMcastFwdGroupAddress_Type())
igsVlanMcastFwdGroupAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:igsVlanMcastFwdGroupAddress.setStatus(_A)
_IgsVlanMcastFwdPortListMac_Type=PortList
_IgsVlanMcastFwdPortListMac_Object=MibTableColumn
igsVlanMcastFwdPortListMac=_IgsVlanMcastFwdPortListMac_Object((1,3,6,1,4,1,171,10,75,2,22,3,1,1,3),_IgsVlanMcastFwdPortListMac_Type())
igsVlanMcastFwdPortListMac.setMaxAccess(_D)
if mibBuilder.loadTexts:igsVlanMcastFwdPortListMac.setStatus(_A)
_IgsVlanRouterPortListTable_Object=MibTable
igsVlanRouterPortListTable=_IgsVlanRouterPortListTable_Object((1,3,6,1,4,1,171,10,75,2,22,3,3))
if mibBuilder.loadTexts:igsVlanRouterPortListTable.setStatus(_A)
_IgsVlanRouterPortListEntry_Object=MibTableRow
igsVlanRouterPortListEntry=_IgsVlanRouterPortListEntry_Object((1,3,6,1,4,1,171,10,75,2,22,3,3,1))
igsVlanRouterPortListEntry.setIndexNames((0,_G,_n))
if mibBuilder.loadTexts:igsVlanRouterPortListEntry.setStatus(_A)
class _IgsVlanRouterPortListVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IgsVlanRouterPortListVlanId_Type.__name__=_C
_IgsVlanRouterPortListVlanId_Object=MibTableColumn
igsVlanRouterPortListVlanId=_IgsVlanRouterPortListVlanId_Object((1,3,6,1,4,1,171,10,75,2,22,3,3,1,1),_IgsVlanRouterPortListVlanId_Type())
igsVlanRouterPortListVlanId.setMaxAccess(_L)
if mibBuilder.loadTexts:igsVlanRouterPortListVlanId.setStatus(_A)
_IgsVlanRouterPortList_Type=PortList
_IgsVlanRouterPortList_Object=MibTableColumn
igsVlanRouterPortList=_IgsVlanRouterPortList_Object((1,3,6,1,4,1,171,10,75,2,22,3,3,1,2),_IgsVlanRouterPortList_Type())
igsVlanRouterPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:igsVlanRouterPortList.setStatus(_A)
_IgsVlanFilterTable_Object=MibTable
igsVlanFilterTable=_IgsVlanFilterTable_Object((1,3,6,1,4,1,171,10,75,2,22,3,4))
if mibBuilder.loadTexts:igsVlanFilterTable.setStatus(_A)
_IgsVlanFilterEntry_Object=MibTableRow
igsVlanFilterEntry=_IgsVlanFilterEntry_Object((1,3,6,1,4,1,171,10,75,2,22,3,4,1))
igsVlanFilterEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:igsVlanFilterEntry.setStatus(_A)
class _IgsVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IgsVlanId_Type.__name__=_C
_IgsVlanId_Object=MibTableColumn
igsVlanId=_IgsVlanId_Object((1,3,6,1,4,1,171,10,75,2,22,3,4,1,1),_IgsVlanId_Type())
igsVlanId.setMaxAccess(_L)
if mibBuilder.loadTexts:igsVlanId.setStatus(_A)
class _IgsVlanFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IgsVlanFilterStatus_Type.__name__=_C
_IgsVlanFilterStatus_Object=MibTableColumn
igsVlanFilterStatus=_IgsVlanFilterStatus_Object((1,3,6,1,4,1,171,10,75,2,22,3,4,1,2),_IgsVlanFilterStatus_Type())
igsVlanFilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igsVlanFilterStatus.setStatus(_A)
_CompanyDot1xGroup_ObjectIdentity=ObjectIdentity
companyDot1xGroup=_CompanyDot1xGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,23))
_Radius_ObjectIdentity=ObjectIdentity
radius=_Radius_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,23,1))
_RadiusServerAddress_Type=IpAddress
_RadiusServerAddress_Object=MibScalar
radiusServerAddress=_RadiusServerAddress_Object((1,3,6,1,4,1,171,10,75,2,23,1,1),_RadiusServerAddress_Type())
radiusServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServerAddress.setStatus(_A)
class _RadiusServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusServerPort_Type.__name__=_C
_RadiusServerPort_Object=MibScalar
radiusServerPort=_RadiusServerPort_Object((1,3,6,1,4,1,171,10,75,2,23,1,2),_RadiusServerPort_Type())
radiusServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServerPort.setStatus(_A)
_RadiusServerSharedSecret_Type=DisplayString
_RadiusServerSharedSecret_Object=MibScalar
radiusServerSharedSecret=_RadiusServerSharedSecret_Object((1,3,6,1,4,1,171,10,75,2,23,1,3),_RadiusServerSharedSecret_Type())
radiusServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServerSharedSecret.setStatus(_A)
_Dot1xAuth_ObjectIdentity=ObjectIdentity
dot1xAuth=_Dot1xAuth_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,23,2))
class _Dot1xAuthSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_Dot1xAuthSystemControl_Type.__name__=_C
_Dot1xAuthSystemControl_Object=MibScalar
dot1xAuthSystemControl=_Dot1xAuthSystemControl_Object((1,3,6,1,4,1,171,10,75,2,23,2,1),_Dot1xAuthSystemControl_Type())
dot1xAuthSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthSystemControl.setStatus(_A)
class _Dot1xAuthQuietPeriod_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1xAuthQuietPeriod_Type.__name__=_C
_Dot1xAuthQuietPeriod_Object=MibScalar
dot1xAuthQuietPeriod=_Dot1xAuthQuietPeriod_Object((1,3,6,1,4,1,171,10,75,2,23,2,2),_Dot1xAuthQuietPeriod_Type())
dot1xAuthQuietPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthQuietPeriod.setStatus(_A)
class _Dot1xAuthTxPeriod_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xAuthTxPeriod_Type.__name__=_C
_Dot1xAuthTxPeriod_Object=MibScalar
dot1xAuthTxPeriod=_Dot1xAuthTxPeriod_Object((1,3,6,1,4,1,171,10,75,2,23,2,3),_Dot1xAuthTxPeriod_Type())
dot1xAuthTxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthTxPeriod.setStatus(_A)
class _Dot1xAuthSuppTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xAuthSuppTimeout_Type.__name__=_C
_Dot1xAuthSuppTimeout_Object=MibScalar
dot1xAuthSuppTimeout=_Dot1xAuthSuppTimeout_Object((1,3,6,1,4,1,171,10,75,2,23,2,4),_Dot1xAuthSuppTimeout_Type())
dot1xAuthSuppTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthSuppTimeout.setStatus(_A)
class _Dot1xAuthServerTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xAuthServerTimeout_Type.__name__=_C
_Dot1xAuthServerTimeout_Object=MibScalar
dot1xAuthServerTimeout=_Dot1xAuthServerTimeout_Object((1,3,6,1,4,1,171,10,75,2,23,2,5),_Dot1xAuthServerTimeout_Type())
dot1xAuthServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthServerTimeout.setStatus(_A)
class _Dot1xAuthMaxReq_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Dot1xAuthMaxReq_Type.__name__=_C
_Dot1xAuthMaxReq_Object=MibScalar
dot1xAuthMaxReq=_Dot1xAuthMaxReq_Object((1,3,6,1,4,1,171,10,75,2,23,2,6),_Dot1xAuthMaxReq_Type())
dot1xAuthMaxReq.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthMaxReq.setStatus(_A)
class _Dot1xAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Dot1xAuthReAuthPeriod_Type.__name__=_S
_Dot1xAuthReAuthPeriod_Object=MibScalar
dot1xAuthReAuthPeriod=_Dot1xAuthReAuthPeriod_Object((1,3,6,1,4,1,171,10,75,2,23,2,7),_Dot1xAuthReAuthPeriod_Type())
dot1xAuthReAuthPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthReAuthPeriod.setStatus(_A)
class _Dot1xAuthReAuthEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_Dot1xAuthReAuthEnabled_Type.__name__=_C
_Dot1xAuthReAuthEnabled_Object=MibScalar
dot1xAuthReAuthEnabled=_Dot1xAuthReAuthEnabled_Object((1,3,6,1,4,1,171,10,75,2,23,2,8),_Dot1xAuthReAuthEnabled_Type())
dot1xAuthReAuthEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthReAuthEnabled.setStatus(_A)
_Dot1xAuthConfigPortTable_Object=MibTable
dot1xAuthConfigPortTable=_Dot1xAuthConfigPortTable_Object((1,3,6,1,4,1,171,10,75,2,23,2,9))
if mibBuilder.loadTexts:dot1xAuthConfigPortTable.setStatus(_A)
_Dot1xAuthConfigPortEntry_Object=MibTableRow
dot1xAuthConfigPortEntry=_Dot1xAuthConfigPortEntry_Object((1,3,6,1,4,1,171,10,75,2,23,2,9,1))
dot1xAuthConfigPortEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:dot1xAuthConfigPortEntry.setStatus(_A)
_Dot1xAuthConfigPortNumber_Type=Integer32
_Dot1xAuthConfigPortNumber_Object=MibTableColumn
dot1xAuthConfigPortNumber=_Dot1xAuthConfigPortNumber_Object((1,3,6,1,4,1,171,10,75,2,23,2,9,1,1),_Dot1xAuthConfigPortNumber_Type())
dot1xAuthConfigPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xAuthConfigPortNumber.setStatus(_A)
class _Dot1xAuthConfigPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_Dot1xAuthConfigPortControl_Type.__name__=_C
_Dot1xAuthConfigPortControl_Object=MibTableColumn
dot1xAuthConfigPortControl=_Dot1xAuthConfigPortControl_Object((1,3,6,1,4,1,171,10,75,2,23,2,9,1,2),_Dot1xAuthConfigPortControl_Type())
dot1xAuthConfigPortControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthConfigPortControl.setStatus(_A)
class _Dot1xAuthConfigPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('authnull',0),('authorized',1),('unauthorized',2)))
_Dot1xAuthConfigPortStatus_Type.__name__=_C
_Dot1xAuthConfigPortStatus_Object=MibTableColumn
dot1xAuthConfigPortStatus=_Dot1xAuthConfigPortStatus_Object((1,3,6,1,4,1,171,10,75,2,23,2,9,1,3),_Dot1xAuthConfigPortStatus_Type())
dot1xAuthConfigPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xAuthConfigPortStatus.setStatus(_A)
_Dot1xAuthConfigPortSessionTime_Type=TimeTicks
_Dot1xAuthConfigPortSessionTime_Object=MibTableColumn
dot1xAuthConfigPortSessionTime=_Dot1xAuthConfigPortSessionTime_Object((1,3,6,1,4,1,171,10,75,2,23,2,9,1,4),_Dot1xAuthConfigPortSessionTime_Type())
dot1xAuthConfigPortSessionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xAuthConfigPortSessionTime.setStatus(_A)
_Dot1xAuthConfigPortSessionUserName_Type=DisplayString
_Dot1xAuthConfigPortSessionUserName_Object=MibTableColumn
dot1xAuthConfigPortSessionUserName=_Dot1xAuthConfigPortSessionUserName_Object((1,3,6,1,4,1,171,10,75,2,23,2,9,1,5),_Dot1xAuthConfigPortSessionUserName_Type())
dot1xAuthConfigPortSessionUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xAuthConfigPortSessionUserName.setStatus(_A)
_CompanyQoSGroup_ObjectIdentity=ObjectIdentity
companyQoSGroup=_CompanyQoSGroup_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,26))
class _QosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1p',1),('dscp',2)))
_QosMode_Type.__name__=_C
_QosMode_Object=MibScalar
qosMode=_QosMode_Object((1,3,6,1,4,1,171,10,75,2,26,1),_QosMode_Type())
qosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:qosMode.setStatus(_A)
class _QueuingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strictPriority',1),('wrr',2)))
_QueuingMechanism_Type.__name__=_C
_QueuingMechanism_Object=MibScalar
queuingMechanism=_QueuingMechanism_Object((1,3,6,1,4,1,171,10,75,2,26,2),_QueuingMechanism_Type())
queuingMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:queuingMechanism.setStatus(_A)
_Dot1pPortTable_Object=MibTable
dot1pPortTable=_Dot1pPortTable_Object((1,3,6,1,4,1,171,10,75,2,26,3))
if mibBuilder.loadTexts:dot1pPortTable.setStatus(_A)
_Dot1pPortEntry_Object=MibTableRow
dot1pPortEntry=_Dot1pPortEntry_Object((1,3,6,1,4,1,171,10,75,2,26,3,1))
dot1pPortEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:dot1pPortEntry.setStatus(_A)
_Dot1pPortIndex_Type=Integer32
_Dot1pPortIndex_Object=MibTableColumn
dot1pPortIndex=_Dot1pPortIndex_Object((1,3,6,1,4,1,171,10,75,2,26,3,1,1),_Dot1pPortIndex_Type())
dot1pPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1pPortIndex.setStatus(_A)
class _Dot1pPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_Dot1pPortPriority_Type.__name__=_C
_Dot1pPortPriority_Object=MibTableColumn
dot1pPortPriority=_Dot1pPortPriority_Object((1,3,6,1,4,1,171,10,75,2,26,3,1,2),_Dot1pPortPriority_Type())
dot1pPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pPortPriority.setStatus(_A)
_DscpTable_Object=MibTable
dscpTable=_DscpTable_Object((1,3,6,1,4,1,171,10,75,2,26,4))
if mibBuilder.loadTexts:dscpTable.setStatus(_A)
_DscpEntry_Object=MibTableRow
dscpEntry=_DscpEntry_Object((1,3,6,1,4,1,171,10,75,2,26,4,1))
dscpEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:dscpEntry.setStatus(_A)
class _DscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_DscpIndex_Type.__name__=_C
_DscpIndex_Object=MibTableColumn
dscpIndex=_DscpIndex_Object((1,3,6,1,4,1,171,10,75,2,26,4,1,1),_DscpIndex_Type())
dscpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dscpIndex.setStatus(_A)
class _DscpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_DscpPriority_Type.__name__=_C
_DscpPriority_Object=MibTableColumn
dscpPriority=_DscpPriority_Object((1,3,6,1,4,1,171,10,75,2,26,4,1,2),_DscpPriority_Type())
dscpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:dscpPriority.setStatus(_A)
_CompanyTrafficMgmt_ObjectIdentity=ObjectIdentity
companyTrafficMgmt=_CompanyTrafficMgmt_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,27))
_BroadcastStormCtrlSettings_ObjectIdentity=ObjectIdentity
broadcastStormCtrlSettings=_BroadcastStormCtrlSettings_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,27,3))
class _BroadcastStormCtrlGlobalOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BroadcastStormCtrlGlobalOnOff_Type.__name__=_C
_BroadcastStormCtrlGlobalOnOff_Object=MibScalar
broadcastStormCtrlGlobalOnOff=_BroadcastStormCtrlGlobalOnOff_Object((1,3,6,1,4,1,171,10,75,2,27,3,1),_BroadcastStormCtrlGlobalOnOff_Type())
broadcastStormCtrlGlobalOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:broadcastStormCtrlGlobalOnOff.setStatus(_A)
class _BroadcastStormGlobalThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),('kBps-8',2),('kBps-16',3),('kBps-32',4),('kBps-64',5),('kBps-128',6),('kBps-256',7),('kBps-512',8),('kBps-1024',9),('kBps-2048',10),('kBps-4096',11)))
_BroadcastStormGlobalThreshold_Type.__name__=_C
_BroadcastStormGlobalThreshold_Object=MibScalar
broadcastStormGlobalThreshold=_BroadcastStormGlobalThreshold_Object((1,3,6,1,4,1,171,10,75,2,27,3,2),_BroadcastStormGlobalThreshold_Type())
broadcastStormGlobalThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:broadcastStormGlobalThreshold.setStatus(_A)
_CompanySecurity_ObjectIdentity=ObjectIdentity
companySecurity=_CompanySecurity_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,28))
_TrustedHostSettings_ObjectIdentity=ObjectIdentity
trustedHostSettings=_TrustedHostSettings_ObjectIdentity((1,3,6,1,4,1,171,10,75,2,28,1))
class _TrustedHostOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_TrustedHostOnOff_Type.__name__=_C
_TrustedHostOnOff_Object=MibScalar
trustedHostOnOff=_TrustedHostOnOff_Object((1,3,6,1,4,1,171,10,75,2,28,1,1),_TrustedHostOnOff_Type())
trustedHostOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:trustedHostOnOff.setStatus(_A)
_TrustedHostTable_Object=MibTable
trustedHostTable=_TrustedHostTable_Object((1,3,6,1,4,1,171,10,75,2,28,1,2))
if mibBuilder.loadTexts:trustedHostTable.setStatus(_A)
_TrustedHostEntry_Object=MibTableRow
trustedHostEntry=_TrustedHostEntry_Object((1,3,6,1,4,1,171,10,75,2,28,1,2,1))
trustedHostEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:trustedHostEntry.setStatus(_A)
_TrustedHostID_Type=Integer32
_TrustedHostID_Object=MibTableColumn
trustedHostID=_TrustedHostID_Object((1,3,6,1,4,1,171,10,75,2,28,1,2,1,1),_TrustedHostID_Type())
trustedHostID.setMaxAccess(_D)
if mibBuilder.loadTexts:trustedHostID.setStatus(_A)
_TrustedHostIpAddress_Type=IpAddress
_TrustedHostIpAddress_Object=MibTableColumn
trustedHostIpAddress=_TrustedHostIpAddress_Object((1,3,6,1,4,1,171,10,75,2,28,1,2,1,2),_TrustedHostIpAddress_Type())
trustedHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:trustedHostIpAddress.setStatus(_A)
_TrustedHostIpMask_Type=IpAddress
_TrustedHostIpMask_Object=MibTableColumn
trustedHostIpMask=_TrustedHostIpMask_Object((1,3,6,1,4,1,171,10,75,2,28,1,2,1,3),_TrustedHostIpMask_Type())
trustedHostIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:trustedHostIpMask.setStatus(_A)
class _TrustedHostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,6)));namedValues=NamedValues(*((_I,1),(_Q,3),(_R,5),(_J,6)))
_TrustedHostStatus_Type.__name__=_C
_TrustedHostStatus_Object=MibTableColumn
trustedHostStatus=_TrustedHostStatus_Object((1,3,6,1,4,1,171,10,75,2,28,1,2,1,4),_TrustedHostStatus_Type())
trustedHostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:trustedHostStatus.setStatus(_A)
swFiberInsert=NotificationType((1,3,6,1,4,1,171,10,75,2,0,1))
if mibBuilder.loadTexts:swFiberInsert.setStatus('')
swFiberRemove=NotificationType((1,3,6,1,4,1,171,10,75,2,0,2))
if mibBuilder.loadTexts:swFiberRemove.setStatus('')
swFiberAbnormalRXError=NotificationType((1,3,6,1,4,1,171,10,75,2,0,3))
if mibBuilder.loadTexts:swFiberAbnormalRXError.setStatus('')
swFiberAbnormalTXError=NotificationType((1,3,6,1,4,1,171,10,75,2,0,4))
if mibBuilder.loadTexts:swFiberAbnormalTXError.setStatus('')
swTPAbnormalRXError=NotificationType((1,3,6,1,4,1,171,10,75,2,0,5))
if mibBuilder.loadTexts:swTPAbnormalRXError.setStatus('')
swTPAbnormalTXError=NotificationType((1,3,6,1,4,1,171,10,75,2,0,6))
if mibBuilder.loadTexts:swTPAbnormalTXError.setStatus('')
mibBuilder.exportSymbols(_G,**{'OwnerString':OwnerString,'MacAddress':MacAddress,'PortList':PortList,'RowStatus':RowStatus,'d-link':d_link,'dlink-products':dlink_products,'dlink-DES12XXSeriesProd':dlink_DES12XXSeriesProd,'des-1228a1':des_1228a1,'swFiberInsert':swFiberInsert,'swFiberRemove':swFiberRemove,'swFiberAbnormalRXError':swFiberAbnormalRXError,'swFiberAbnormalTXError':swFiberAbnormalTXError,'swTPAbnormalRXError':swTPAbnormalRXError,'swTPAbnormalTXError':swTPAbnormalTXError,'companyCommGroup':companyCommGroup,'commSetTable':commSetTable,'commSetEntry':commSetEntry,_U:commSetIndex,'commSetName':commSetName,'commSetStatus':commSetStatus,'commGetTable':commGetTable,'commGetEntry':commGetEntry,_V:commGetIndex,'commGetName':commGetName,'commGetStatus':commGetStatus,'commTrapTable':commTrapTable,'commTrapEntry':commTrapEntry,_W:commTrapIndex,'commTrapName':commTrapName,'commTrapIpAddress':commTrapIpAddress,'commTrapSNMPBootup':commTrapSNMPBootup,'commTrapSNMPTPLinkUpDown':commTrapSNMPTPLinkUpDown,'commTrapSNMPFiberLinkUpDown':commTrapSNMPFiberLinkUpDown,'commTrapTrapAbnormalTPRXError':commTrapTrapAbnormalTPRXError,'commTrapTrapAbnormalTPTXError':commTrapTrapAbnormalTPTXError,'commTrapTrapAbnormalFiberRXError':commTrapTrapAbnormalFiberRXError,'commTrapTrapAbnormalFiberTXError':commTrapTrapAbnormalFiberTXError,'commTrapStatus':commTrapStatus,'companyMiscGroup':companyMiscGroup,'miscReset':miscReset,'miscStatisticsReset':miscStatisticsReset,'companySpanGroup':companySpanGroup,'spanOnOff':spanOnOff,'companyConfigGroup':companyConfigGroup,'configVerSwPrimary':configVerSwPrimary,'configVerHwChipSet':configVerHwChipSet,'configBootTftpOperation':configBootTftpOperation,'configBootTftpServerIp':configBootTftpServerIp,'configBootImageFileName':configBootImageFileName,'configPortTable':configPortTable,'configPortEntry':configPortEntry,_Z:configPort,'configPortSpeed':configPortSpeed,'configPortOperStatus':configPortOperStatus,'configPortPriority':configPortPriority,'configVLANMode':configVLANMode,'configMirrorTable':configMirrorTable,'configMirrorEntry':configMirrorEntry,_f:configMirrorId,'configMirrorMon':configMirrorMon,'configMirrorTXSrc':configMirrorTXSrc,'configMirrorRXSrc':configMirrorRXSrc,'configMirrorStatus':configMirrorStatus,'configSNMPEnable':configSNMPEnable,'configIpAssignmentMode':configIpAssignmentMode,'configPhysAddress':configPhysAddress,'configPasswordAdmin':configPasswordAdmin,'configIpAddress':configIpAddress,'configNetMask':configNetMask,'configGateway':configGateway,'configSave':configSave,'configRestoreDefaults':configRestoreDefaults,'configTftpServerIpAddress':configTftpServerIpAddress,'configTftpServerFileName':configTftpServerFileName,'configTftpOperation':configTftpOperation,'configSafeguardEnable':configSafeguardEnable,'companyTVlanGroup':companyTVlanGroup,'tvlanTable':tvlanTable,'tvlanEntry':tvlanEntry,_g:tvlanId,'tvlanName':tvlanName,'tvlanMember':tvlanMember,'tvlanUntaggedPorts':tvlanUntaggedPorts,'tvlanStatus':tvlanStatus,'tvlanManagementOnOff':tvlanManagementOnOff,'tvlanManagementid':tvlanManagementid,'tvlanPortTable':tvlanPortTable,'tvlanPortEntry':tvlanPortEntry,_h:tvlanPortPortId,'tvlanPortVlanId':tvlanPortVlanId,'tvlanAsyOnOff':tvlanAsyOnOff,'companyPortTrunkGroup':companyPortTrunkGroup,'portTrunkTable':portTrunkTable,'portTrunkEntry':portTrunkEntry,_i:portTrunkId,'portTrunkName':portTrunkName,_j:portTrunkMember,'companyStaticGroup':companyStaticGroup,'staticOnOff':staticOnOff,'staticAutoLearning':staticAutoLearning,'staticTable':staticTable,'staticEntry':staticEntry,_k:staticId,'staticMac':staticMac,'staticPort':staticPort,'staticVlanID':staticVlanID,'staticStatus':staticStatus,'companyIgsGroup':companyIgsGroup,'igsSystem':igsSystem,'igsStatus':igsStatus,'igsv3Processing':igsv3Processing,'igsRouterPortPurgeInterval':igsRouterPortPurgeInterval,'igsHostPortPurgeInterval':igsHostPortPurgeInterval,'igsReportForwardInterval':igsReportForwardInterval,'igsLeaveProcessInterval':igsLeaveProcessInterval,'igsMcastEntryAgeingInterval':igsMcastEntryAgeingInterval,'igsSharedSegmentAggregationInterval':igsSharedSegmentAggregationInterval,'igsGblReportFwdOnAllPorts':igsGblReportFwdOnAllPorts,'igsNextMcastFwdMode':igsNextMcastFwdMode,'igsQueryInterval':igsQueryInterval,'igsQueryMaxResponseTime':igsQueryMaxResponseTime,'igsRobustnessValue':igsRobustnessValue,'igsLastMembQueryInterval':igsLastMembQueryInterval,'igsQuerierStateOnOff':igsQuerierStateOnOff,'igsVlan':igsVlan,'igsVlanMcastFwdTable':igsVlanMcastFwdTable,'igsVlanMcastFwdEntry':igsVlanMcastFwdEntry,_l:igsVlanMcastFwdVlanIdMac,_m:igsVlanMcastFwdGroupAddress,'igsVlanMcastFwdPortListMac':igsVlanMcastFwdPortListMac,'igsVlanRouterPortListTable':igsVlanRouterPortListTable,'igsVlanRouterPortListEntry':igsVlanRouterPortListEntry,_n:igsVlanRouterPortListVlanId,'igsVlanRouterPortList':igsVlanRouterPortList,'igsVlanFilterTable':igsVlanFilterTable,'igsVlanFilterEntry':igsVlanFilterEntry,_o:igsVlanId,'igsVlanFilterStatus':igsVlanFilterStatus,'companyDot1xGroup':companyDot1xGroup,'radius':radius,'radiusServerAddress':radiusServerAddress,'radiusServerPort':radiusServerPort,'radiusServerSharedSecret':radiusServerSharedSecret,'dot1xAuth':dot1xAuth,'dot1xAuthSystemControl':dot1xAuthSystemControl,'dot1xAuthQuietPeriod':dot1xAuthQuietPeriod,'dot1xAuthTxPeriod':dot1xAuthTxPeriod,'dot1xAuthSuppTimeout':dot1xAuthSuppTimeout,'dot1xAuthServerTimeout':dot1xAuthServerTimeout,'dot1xAuthMaxReq':dot1xAuthMaxReq,'dot1xAuthReAuthPeriod':dot1xAuthReAuthPeriod,'dot1xAuthReAuthEnabled':dot1xAuthReAuthEnabled,'dot1xAuthConfigPortTable':dot1xAuthConfigPortTable,'dot1xAuthConfigPortEntry':dot1xAuthConfigPortEntry,_p:dot1xAuthConfigPortNumber,'dot1xAuthConfigPortControl':dot1xAuthConfigPortControl,'dot1xAuthConfigPortStatus':dot1xAuthConfigPortStatus,'dot1xAuthConfigPortSessionTime':dot1xAuthConfigPortSessionTime,'dot1xAuthConfigPortSessionUserName':dot1xAuthConfigPortSessionUserName,'companyQoSGroup':companyQoSGroup,'qosMode':qosMode,'queuingMechanism':queuingMechanism,'dot1pPortTable':dot1pPortTable,'dot1pPortEntry':dot1pPortEntry,_q:dot1pPortIndex,'dot1pPortPriority':dot1pPortPriority,'dscpTable':dscpTable,'dscpEntry':dscpEntry,_r:dscpIndex,'dscpPriority':dscpPriority,'companyTrafficMgmt':companyTrafficMgmt,'broadcastStormCtrlSettings':broadcastStormCtrlSettings,'broadcastStormCtrlGlobalOnOff':broadcastStormCtrlGlobalOnOff,'broadcastStormGlobalThreshold':broadcastStormGlobalThreshold,'companySecurity':companySecurity,'trustedHostSettings':trustedHostSettings,'trustedHostOnOff':trustedHostOnOff,'trustedHostTable':trustedHostTable,'trustedHostEntry':trustedHostEntry,_s:trustedHostID,'trustedHostIpAddress':trustedHostIpAddress,'trustedHostIpMask':trustedHostIpMask,'trustedHostStatus':trustedHostStatus})