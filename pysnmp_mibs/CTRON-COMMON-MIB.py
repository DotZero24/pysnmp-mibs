_X='normalOperation'
_W='fPRedundAddrId'
_V='powerSupplyNum'
_U='fnbPortConnectPortIndex'
_T='fnbPortConnectBoardIndex'
_S='connectA'
_R='connectC'
_Q='connectB'
_P='fnbCSMACDIndex'
_O='faulted'
_N='attached'
_M='detached'
_L='fnbTRIndex'
_K='infoNotAvailable'
_J='enable'
_I='disable'
_H='DisplayString'
_G='other'
_F='CTRON-COMMON-MIB'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonRev1,dl,subSysDevice,subSysMMAC,ups=mibBuilder.importSymbols('IRM-OIDS','commonRev1','dl','subSysDevice','subSysMMAC','ups')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
class _DeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,176,177,178,179,180,185,187,190,65569,65570,65571,65572)));namedValues=NamedValues(*((_G,1),('iRM2',176),('iRBM',177),('iRM3',178),('tRMBM-R',179),('tRMBM-S',180),('emm-E',185),('tRMM',187),('trmMim',190),('mrxi24',65569),('mrxi22',65570),('mrxi34',65571),('mrxi38',65572)))
_DeviceType_Type.__name__=_D
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,52,1,1,1,1),_DeviceType_Type())
deviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,52,1,1,1,2),_DeviceName_Type())
deviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
_DeviceIPAddress_Type=IpAddress
_DeviceIPAddress_Object=MibScalar
deviceIPAddress=_DeviceIPAddress_Object((1,3,6,1,4,1,52,1,1,1,3),_DeviceIPAddress_Type())
deviceIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceIPAddress.setStatus(_A)
class _DeviceTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_DeviceTime_Type.__name__=_H
_DeviceTime_Object=MibScalar
deviceTime=_DeviceTime_Object((1,3,6,1,4,1,52,1,1,1,4),_DeviceTime_Type())
deviceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceTime.setStatus(_A)
class _DeviceDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_DeviceDate_Type.__name__=_H
_DeviceDate_Object=MibScalar
deviceDate=_DeviceDate_Object((1,3,6,1,4,1,52,1,1,1,5),_DeviceDate_Type())
deviceDate.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceDate.setStatus(_A)
_Fnb2_ObjectIdentity=ObjectIdentity
fnb2=_Fnb2_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,2))
_FnbTR_ObjectIdentity=ObjectIdentity
fnbTR=_FnbTR_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,2,1))
_FnbTRTable_Object=MibTable
fnbTRTable=_FnbTRTable_Object((1,3,6,1,4,1,52,1,6,1,2,1,1))
if mibBuilder.loadTexts:fnbTRTable.setStatus(_A)
_FnbTREntry_Object=MibTableRow
fnbTREntry=_FnbTREntry_Object((1,3,6,1,4,1,52,1,6,1,2,1,1,1))
fnbTREntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:fnbTREntry.setStatus(_A)
_FnbTRIndex_Type=Integer32
_FnbTRIndex_Object=MibTableColumn
fnbTRIndex=_FnbTRIndex_Object((1,3,6,1,4,1,52,1,6,1,2,1,1,1,1),_FnbTRIndex_Type())
fnbTRIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnbTRIndex.setStatus(_A)
class _FnbConnectLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_FnbConnectLeft_Type.__name__=_D
_FnbConnectLeft_Object=MibTableColumn
fnbConnectLeft=_FnbConnectLeft_Object((1,3,6,1,4,1,52,1,6,1,2,1,1,1,2),_FnbConnectLeft_Type())
fnbConnectLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbConnectLeft.setStatus(_A)
class _FnbConnectRight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_FnbConnectRight_Type.__name__=_D
_FnbConnectRight_Object=MibTableColumn
fnbConnectRight=_FnbConnectRight_Object((1,3,6,1,4,1,52,1,6,1,2,1,1,1,3),_FnbConnectRight_Type())
fnbConnectRight.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbConnectRight.setStatus(_A)
class _FnbBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_FnbBypass_Type.__name__=_D
_FnbBypass_Object=MibTableColumn
fnbBypass=_FnbBypass_Object((1,3,6,1,4,1,52,1,6,1,2,1,1,1,4),_FnbBypass_Type())
fnbBypass.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbBypass.setStatus(_A)
class _FnbRPBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('disabled',2),('enabled',3)))
_FnbRPBypass_Type.__name__=_D
_FnbRPBypass_Object=MibTableColumn
fnbRPBypass=_FnbRPBypass_Object((1,3,6,1,4,1,52,1,6,1,2,1,1,1,5),_FnbRPBypass_Type())
fnbRPBypass.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbRPBypass.setStatus(_A)
_FnbCSMACD_ObjectIdentity=ObjectIdentity
fnbCSMACD=_FnbCSMACD_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,2,2))
_FnbCSMACDTable_Object=MibTable
fnbCSMACDTable=_FnbCSMACDTable_Object((1,3,6,1,4,1,52,1,6,1,2,2,1))
if mibBuilder.loadTexts:fnbCSMACDTable.setStatus(_A)
_FnbCSMACDEntry_Object=MibTableRow
fnbCSMACDEntry=_FnbCSMACDEntry_Object((1,3,6,1,4,1,52,1,6,1,2,2,1,1))
fnbCSMACDEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:fnbCSMACDEntry.setStatus(_A)
_FnbCSMACDIndex_Type=Integer32
_FnbCSMACDIndex_Object=MibTableColumn
fnbCSMACDIndex=_FnbCSMACDIndex_Object((1,3,6,1,4,1,52,1,6,1,2,2,1,1,1),_FnbCSMACDIndex_Type())
fnbCSMACDIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbCSMACDIndex.setStatus(_A)
class _FnbConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_Q,1),(_R,2),('disconnect',3),(_S,4),('subnetB',5),('subnetC',6),('multiChannel',7),('frontPanel',8)))
_FnbConnect_Type.__name__=_D
_FnbConnect_Object=MibTableColumn
fnbConnect=_FnbConnect_Object((1,3,6,1,4,1,52,1,6,1,2,2,1,1,2),_FnbConnect_Type())
fnbConnect.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbConnect.setStatus(_A)
_FnbPortChanges_Type=Counter32
_FnbPortChanges_Object=MibTableColumn
fnbPortChanges=_FnbPortChanges_Object((1,3,6,1,4,1,52,1,6,1,2,2,1,1,3),_FnbPortChanges_Type())
fnbPortChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fnbPortChanges.setStatus(_A)
_FnbPortConnect_ObjectIdentity=ObjectIdentity
fnbPortConnect=_FnbPortConnect_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,2,3))
_FnbPortConnectTable_Object=MibTable
fnbPortConnectTable=_FnbPortConnectTable_Object((1,3,6,1,4,1,52,1,6,1,2,3,1))
if mibBuilder.loadTexts:fnbPortConnectTable.setStatus(_A)
_FnbPortConnectEntry_Object=MibTableRow
fnbPortConnectEntry=_FnbPortConnectEntry_Object((1,3,6,1,4,1,52,1,6,1,2,3,1,1))
fnbPortConnectEntry.setIndexNames((0,_F,_T),(0,_F,_U))
if mibBuilder.loadTexts:fnbPortConnectEntry.setStatus(_A)
_FnbPortConnectBoardIndex_Type=Integer32
_FnbPortConnectBoardIndex_Object=MibTableColumn
fnbPortConnectBoardIndex=_FnbPortConnectBoardIndex_Object((1,3,6,1,4,1,52,1,6,1,2,3,1,1,1),_FnbPortConnectBoardIndex_Type())
fnbPortConnectBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnbPortConnectBoardIndex.setStatus(_A)
_FnbPortConnectPortIndex_Type=Integer32
_FnbPortConnectPortIndex_Object=MibTableColumn
fnbPortConnectPortIndex=_FnbPortConnectPortIndex_Object((1,3,6,1,4,1,52,1,6,1,2,3,1,1,2),_FnbPortConnectPortIndex_Type())
fnbPortConnectPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnbPortConnectPortIndex.setStatus(_A)
class _FnbPortConnectPortAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_Q,2),(_R,3)))
_FnbPortConnectPortAssignment_Type.__name__=_D
_FnbPortConnectPortAssignment_Object=MibTableColumn
fnbPortConnectPortAssignment=_FnbPortConnectPortAssignment_Object((1,3,6,1,4,1,52,1,6,1,2,3,1,1,3),_FnbPortConnectPortAssignment_Type())
fnbPortConnectPortAssignment.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbPortConnectPortAssignment.setStatus(_A)
_FnbPortConnectCompID_Type=Integer32
_FnbPortConnectCompID_Object=MibTableColumn
fnbPortConnectCompID=_FnbPortConnectCompID_Object((1,3,6,1,4,1,52,1,6,1,2,3,1,1,4),_FnbPortConnectCompID_Type())
fnbPortConnectCompID.setMaxAccess(_B)
if mibBuilder.loadTexts:fnbPortConnectCompID.setStatus(_A)
_FnbPortConnectionChanges_Type=Counter32
_FnbPortConnectionChanges_Object=MibScalar
fnbPortConnectionChanges=_FnbPortConnectionChanges_Object((1,3,6,1,4,1,52,1,6,1,2,3,2),_FnbPortConnectionChanges_Type())
fnbPortConnectionChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fnbPortConnectionChanges.setStatus(_A)
_Chassis_ObjectIdentity=ObjectIdentity
chassis=_Chassis_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,3))
_ChassisHWRev_Type=Integer32
_ChassisHWRev_Object=MibScalar
chassisHWRev=_ChassisHWRev_Object((1,3,6,1,4,1,52,1,6,1,3,1),_ChassisHWRev_Type())
chassisHWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisHWRev.setStatus(_A)
class _ChassisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,1),('mMAC8FNB',2),('mMAC5FNB',3),('mMAC3FNB',4),('mINIMMAC',5),('mRXI',6),('m3FNB',7),('m5FNB',8),('m8FNB',9),('nonFNB',10),('mMAC3FNBS',11),('mMAC5FNBS',12),('mMAC8FNBS',13),('m8FNBS',14)))
_ChassisType_Type.__name__=_D
_ChassisType_Object=MibScalar
chassisType=_ChassisType_Object((1,3,6,1,4,1,52,1,6,1,3,2),_ChassisType_Type())
chassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisType.setStatus(_A)
_ChassisSlots_Type=Integer32
_ChassisSlots_Object=MibScalar
chassisSlots=_ChassisSlots_Object((1,3,6,1,4,1,52,1,6,1,3,3),_ChassisSlots_Type())
chassisSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlots.setStatus(_A)
class _ChassisFNB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absent',1),('present',2)))
_ChassisFNB_Type.__name__=_D
_ChassisFNB_Object=MibScalar
chassisFNB=_ChassisFNB_Object((1,3,6,1,4,1,52,1,6,1,3,4),_ChassisFNB_Type())
chassisFNB.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisFNB.setStatus(_A)
class _ChassisAlarmEna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ChassisAlarmEna_Type.__name__=_D
_ChassisAlarmEna_Object=MibScalar
chassisAlarmEna=_ChassisAlarmEna_Object((1,3,6,1,4,1,52,1,6,1,3,5),_ChassisAlarmEna_Type())
chassisAlarmEna.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisAlarmEna.setStatus(_A)
class _ChassisAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chassisNoFaultCondition',1),('chassisFaultCondition',2)))
_ChassisAlarmState_Type.__name__=_D
_ChassisAlarmState_Object=MibScalar
chassisAlarmState=_ChassisAlarmState_Object((1,3,6,1,4,1,52,1,6,1,3,6),_ChassisAlarmState_Type())
chassisAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisAlarmState.setStatus(_A)
_Environment_ObjectIdentity=ObjectIdentity
environment=_Environment_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,4))
_PowerTable_Object=MibTable
powerTable=_PowerTable_Object((1,3,6,1,4,1,52,1,6,1,4,1))
if mibBuilder.loadTexts:powerTable.setStatus(_A)
_PowerEntry_Object=MibTableRow
powerEntry=_PowerEntry_Object((1,3,6,1,4,1,52,1,6,1,4,1,1))
powerEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:powerEntry.setStatus(_A)
_PowerSupplyNum_Type=Integer32
_PowerSupplyNum_Object=MibTableColumn
powerSupplyNum=_PowerSupplyNum_Object((1,3,6,1,4,1,52,1,6,1,4,1,1,1),_PowerSupplyNum_Type())
powerSupplyNum.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyNum.setStatus(_A)
class _PowerSupplyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('notInstalled',2),('installedAndOperating',3),('installedAndNotOperating',4)))
_PowerSupplyState_Type.__name__=_D
_PowerSupplyState_Object=MibTableColumn
powerSupplyState=_PowerSupplyState_Object((1,3,6,1,4,1,52,1,6,1,4,1,1,2),_PowerSupplyState_Type())
powerSupplyState.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyState.setStatus(_A)
_PowerSupplyId_Type=ObjectIdentifier
_PowerSupplyId_Object=MibTableColumn
powerSupplyId=_PowerSupplyId_Object((1,3,6,1,4,1,52,1,6,1,4,1,1,3),_PowerSupplyId_Type())
powerSupplyId.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyId.setStatus(_A)
class _PowerSupplyRedun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('redundancyAvail',1),('redundancyNotAvail',2),(_K,3)))
_PowerSupplyRedun_Type.__name__=_D
_PowerSupplyRedun_Object=MibTableColumn
powerSupplyRedun=_PowerSupplyRedun_Object((1,3,6,1,4,1,52,1,6,1,4,1,1,4),_PowerSupplyRedun_Type())
powerSupplyRedun.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyRedun.setStatus(_A)
class _PowerSupplyRemoteDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3)))
_PowerSupplyRemoteDisable_Type.__name__=_D
_PowerSupplyRemoteDisable_Object=MibTableColumn
powerSupplyRemoteDisable=_PowerSupplyRemoteDisable_Object((1,3,6,1,4,1,52,1,6,1,4,1,1,5),_PowerSupplyRemoteDisable_Type())
powerSupplyRemoteDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:powerSupplyRemoteDisable.setStatus(_A)
_NB55_ObjectIdentity=ObjectIdentity
nB55=_NB55_ObjectIdentity((1,3,6,1,4,1,52,1,6,2,3))
_NB55HWAddress_Type=PhysAddress
_NB55HWAddress_Object=MibScalar
nB55HWAddress=_NB55HWAddress_Object((1,3,6,1,4,1,52,1,6,2,3,1),_NB55HWAddress_Type())
nB55HWAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nB55HWAddress.setStatus(_A)
_NB55HWRev_Type=Integer32
_NB55HWRev_Object=MibScalar
nB55HWRev=_NB55HWRev_Object((1,3,6,1,4,1,52,1,6,2,3,2),_NB55HWRev_Type())
nB55HWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nB55HWRev.setStatus(_A)
class _NB55FWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NB55FWRev_Type.__name__=_E
_NB55FWRev_Object=MibScalar
nB55FWRev=_NB55FWRev_Object((1,3,6,1,4,1,52,1,6,2,3,3),_NB55FWRev_Type())
nB55FWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nB55FWRev.setStatus(_A)
_MRXI_ObjectIdentity=ObjectIdentity
mRXI=_MRXI_ObjectIdentity((1,3,6,1,4,1,52,1,6,2,6))
_MRXIHWAddress_Type=PhysAddress
_MRXIHWAddress_Object=MibScalar
mRXIHWAddress=_MRXIHWAddress_Object((1,3,6,1,4,1,52,1,6,2,6,1),_MRXIHWAddress_Type())
mRXIHWAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mRXIHWAddress.setStatus(_A)
_MRXIHWRev_Type=Integer32
_MRXIHWRev_Object=MibScalar
mRXIHWRev=_MRXIHWRev_Object((1,3,6,1,4,1,52,1,6,2,6,2),_MRXIHWRev_Type())
mRXIHWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:mRXIHWRev.setStatus(_A)
class _MRXIFWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MRXIFWRev_Type.__name__=_E
_MRXIFWRev_Object=MibScalar
mRXIFWRev=_MRXIFWRev_Object((1,3,6,1,4,1,52,1,6,2,6,3),_MRXIFWRev_Type())
mRXIFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:mRXIFWRev.setStatus(_A)
_IRM3_ObjectIdentity=ObjectIdentity
iRM3=_IRM3_ObjectIdentity((1,3,6,1,4,1,52,1,6,2,7))
_IRM3HWAddress_Type=PhysAddress
_IRM3HWAddress_Object=MibScalar
iRM3HWAddress=_IRM3HWAddress_Object((1,3,6,1,4,1,52,1,6,2,7,1),_IRM3HWAddress_Type())
iRM3HWAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:iRM3HWAddress.setStatus(_A)
_IRM3HWRev_Type=Integer32
_IRM3HWRev_Object=MibScalar
iRM3HWRev=_IRM3HWRev_Object((1,3,6,1,4,1,52,1,6,2,7,2),_IRM3HWRev_Type())
iRM3HWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:iRM3HWRev.setStatus(_A)
class _IRM3FWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IRM3FWRev_Type.__name__=_E
_IRM3FWRev_Object=MibScalar
iRM3FWRev=_IRM3FWRev_Object((1,3,6,1,4,1,52,1,6,2,7,3),_IRM3FWRev_Type())
iRM3FWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:iRM3FWRev.setStatus(_A)
class _IRM3PortAssoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6)));namedValues=NamedValues(*(('aoffFrp',5),('arpFoff',6)))
_IRM3PortAssoc_Type.__name__=_D
_IRM3PortAssoc_Object=MibScalar
iRM3PortAssoc=_IRM3PortAssoc_Object((1,3,6,1,4,1,52,1,6,2,7,4),_IRM3PortAssoc_Type())
iRM3PortAssoc.setMaxAccess(_C)
if mibBuilder.loadTexts:iRM3PortAssoc.setStatus(_A)
class _IRM3BPSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_IRM3BPSupport_Type.__name__=_D
_IRM3BPSupport_Object=MibScalar
iRM3BPSupport=_IRM3BPSupport_Object((1,3,6,1,4,1,52,1,6,2,7,5),_IRM3BPSupport_Type())
iRM3BPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:iRM3BPSupport.setStatus(_A)
_TRMM_ObjectIdentity=ObjectIdentity
tRMM=_TRMM_ObjectIdentity((1,3,6,1,4,1,52,1,6,2,8))
_TRMMHWAddress_Type=PhysAddress
_TRMMHWAddress_Object=MibScalar
tRMMHWAddress=_TRMMHWAddress_Object((1,3,6,1,4,1,52,1,6,2,8,1),_TRMMHWAddress_Type())
tRMMHWAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tRMMHWAddress.setStatus(_A)
_TRMMHWRev_Type=Integer32
_TRMMHWRev_Object=MibScalar
tRMMHWRev=_TRMMHWRev_Object((1,3,6,1,4,1,52,1,6,2,8,2),_TRMMHWRev_Type())
tRMMHWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:tRMMHWRev.setStatus(_A)
class _TRMMFWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_TRMMFWRev_Type.__name__=_E
_TRMMFWRev_Object=MibScalar
tRMMFWRev=_TRMMFWRev_Object((1,3,6,1,4,1,52,1,6,2,8,3),_TRMMFWRev_Type())
tRMMFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:tRMMFWRev.setStatus(_A)
_EMME_ObjectIdentity=ObjectIdentity
eMME=_EMME_ObjectIdentity((1,3,6,1,4,1,52,1,6,2,9))
_EMMEHWAddress_Type=PhysAddress
_EMMEHWAddress_Object=MibScalar
eMMEHWAddress=_EMMEHWAddress_Object((1,3,6,1,4,1,52,1,6,2,9,1),_EMMEHWAddress_Type())
eMMEHWAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eMMEHWAddress.setStatus(_A)
_EMMEHWRev_Type=Integer32
_EMMEHWRev_Object=MibScalar
eMMEHWRev=_EMMEHWRev_Object((1,3,6,1,4,1,52,1,6,2,9,2),_EMMEHWRev_Type())
eMMEHWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eMMEHWRev.setStatus(_A)
class _EMMEFWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_EMMEFWRev_Type.__name__=_E
_EMMEFWRev_Object=MibScalar
eMMEFWRev=_EMMEFWRev_Object((1,3,6,1,4,1,52,1,6,2,9,3),_EMMEFWRev_Type())
eMMEFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eMMEFWRev.setStatus(_A)
_EMMEBoardMap_Type=Integer32
_EMMEBoardMap_Object=MibScalar
eMMEBoardMap=_EMMEBoardMap_Object((1,3,6,1,4,1,52,1,6,2,9,4),_EMMEBoardMap_Type())
eMMEBoardMap.setMaxAccess(_B)
if mibBuilder.loadTexts:eMMEBoardMap.setStatus(_A)
_FPRedundancy_ObjectIdentity=ObjectIdentity
fPRedundancy=_FPRedundancy_ObjectIdentity((1,3,6,1,4,1,52,1,6,2,10))
_FPRedund_ObjectIdentity=ObjectIdentity
fPRedund=_FPRedund_ObjectIdentity((1,3,6,1,4,1,52,1,6,2,10,1))
class _FPRedundReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('reset',2)))
_FPRedundReset_Type.__name__=_D
_FPRedundReset_Object=MibScalar
fPRedundReset=_FPRedundReset_Object((1,3,6,1,4,1,52,1,6,2,10,1,1),_FPRedundReset_Type())
fPRedundReset.setMaxAccess(_C)
if mibBuilder.loadTexts:fPRedundReset.setStatus(_A)
_FPRedundPollInterval_Type=Integer32
_FPRedundPollInterval_Object=MibScalar
fPRedundPollInterval=_FPRedundPollInterval_Object((1,3,6,1,4,1,52,1,6,2,10,1,2),_FPRedundPollInterval_Type())
fPRedundPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fPRedundPollInterval.setStatus(_A)
_FPRedundRetrys_Type=Integer32
_FPRedundRetrys_Object=MibScalar
fPRedundRetrys=_FPRedundRetrys_Object((1,3,6,1,4,1,52,1,6,2,10,1,3),_FPRedundRetrys_Type())
fPRedundRetrys.setMaxAccess(_C)
if mibBuilder.loadTexts:fPRedundRetrys.setStatus(_A)
_FPRedundNumAddr_Type=Integer32
_FPRedundNumAddr_Object=MibScalar
fPRedundNumAddr=_FPRedundNumAddr_Object((1,3,6,1,4,1,52,1,6,2,10,1,4),_FPRedundNumAddr_Type())
fPRedundNumAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fPRedundNumAddr.setStatus(_A)
_FPRedundAddAddr_Type=IpAddress
_FPRedundAddAddr_Object=MibScalar
fPRedundAddAddr=_FPRedundAddAddr_Object((1,3,6,1,4,1,52,1,6,2,10,1,5),_FPRedundAddAddr_Type())
fPRedundAddAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fPRedundAddAddr.setStatus(_A)
_FPRedundDelAddr_Type=IpAddress
_FPRedundDelAddr_Object=MibScalar
fPRedundDelAddr=_FPRedundDelAddr_Object((1,3,6,1,4,1,52,1,6,2,10,1,6),_FPRedundDelAddr_Type())
fPRedundDelAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fPRedundDelAddr.setStatus(_A)
_FPRedundActivePort_Type=Integer32
_FPRedundActivePort_Object=MibScalar
fPRedundActivePort=_FPRedundActivePort_Object((1,3,6,1,4,1,52,1,6,2,10,1,7),_FPRedundActivePort_Type())
fPRedundActivePort.setMaxAccess(_C)
if mibBuilder.loadTexts:fPRedundActivePort.setStatus(_A)
class _FPRedundEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FPRedundEnable_Type.__name__=_D
_FPRedundEnable_Object=MibScalar
fPRedundEnable=_FPRedundEnable_Object((1,3,6,1,4,1,52,1,6,2,10,1,8),_FPRedundEnable_Type())
fPRedundEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fPRedundEnable.setStatus(_A)
_FPRedundAddrTable_Object=MibTable
fPRedundAddrTable=_FPRedundAddrTable_Object((1,3,6,1,4,1,52,1,6,2,10,2))
if mibBuilder.loadTexts:fPRedundAddrTable.setStatus(_A)
_FPRedundAddrEntry_Object=MibTableRow
fPRedundAddrEntry=_FPRedundAddrEntry_Object((1,3,6,1,4,1,52,1,6,2,10,2,1))
fPRedundAddrEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:fPRedundAddrEntry.setStatus(_A)
_FPRedundAddrId_Type=Integer32
_FPRedundAddrId_Object=MibTableColumn
fPRedundAddrId=_FPRedundAddrId_Object((1,3,6,1,4,1,52,1,6,2,10,2,1,1),_FPRedundAddrId_Type())
fPRedundAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:fPRedundAddrId.setStatus(_A)
_FPRedundAddrIPAddr_Type=IpAddress
_FPRedundAddrIPAddr_Object=MibTableColumn
fPRedundAddrIPAddr=_FPRedundAddrIPAddr_Object((1,3,6,1,4,1,52,1,6,2,10,2,1,2),_FPRedundAddrIPAddr_Type())
fPRedundAddrIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fPRedundAddrIPAddr.setStatus(_A)
_UpsVersion_ObjectIdentity=ObjectIdentity
upsVersion=_UpsVersion_ObjectIdentity((1,3,6,1,4,1,52,1,6,3,1))
_UpsRevision_ObjectIdentity=ObjectIdentity
upsRevision=_UpsRevision_ObjectIdentity((1,3,6,1,4,1,52,1,6,3,1,1))
class _UpsID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,257,258,259,260,261,262)));namedValues=NamedValues(*((_G,1),('aPCModel370',257),('aPCModel400',258),('aPCModel600',259),('aPCModel900',260),('aPCModel1250',261),('aPCModel2000',262)))
_UpsID_Type.__name__=_D
_UpsID_Object=MibScalar
upsID=_UpsID_Object((1,3,6,1,4,1,52,1,6,3,1,1,1),_UpsID_Type())
upsID.setMaxAccess(_C)
if mibBuilder.loadTexts:upsID.setStatus(_A)
_UpsUpTime_Type=Integer32
_UpsUpTime_Object=MibScalar
upsUpTime=_UpsUpTime_Object((1,3,6,1,4,1,52,1,6,3,1,1,2),_UpsUpTime_Type())
upsUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsUpTime.setStatus(_A)
_UpsDisable_Type=Integer32
_UpsDisable_Object=MibScalar
upsDisable=_UpsDisable_Object((1,3,6,1,4,1,52,1,6,3,1,1,3),_UpsDisable_Type())
upsDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDisable.setStatus('deprecated')
_UpsDisconnect_Type=Integer32
_UpsDisconnect_Object=MibScalar
upsDisconnect=_UpsDisconnect_Object((1,3,6,1,4,1,52,1,6,3,1,1,4),_UpsDisconnect_Type())
upsDisconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDisconnect.setStatus(_A)
class _UpsTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unitOK',1),('unitFailed',2),('badBattery',3),('noRecentTest',4),('underTest',5)))
_UpsTest_Type.__name__=_D
_UpsTest_Object=MibScalar
upsTest=_UpsTest_Object((1,3,6,1,4,1,52,1,6,3,1,1,5),_UpsTest_Type())
upsTest.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTest.setStatus(_A)
_UpsBatteryCapacity_Type=Integer32
_UpsBatteryCapacity_Object=MibScalar
upsBatteryCapacity=_UpsBatteryCapacity_Object((1,3,6,1,4,1,52,1,6,3,1,1,6),_UpsBatteryCapacity_Type())
upsBatteryCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryCapacity.setStatus(_A)
_UpsACLineVoltsIn_Type=Integer32
_UpsACLineVoltsIn_Object=MibScalar
upsACLineVoltsIn=_UpsACLineVoltsIn_Object((1,3,6,1,4,1,52,1,6,3,1,1,7),_UpsACLineVoltsIn_Type())
upsACLineVoltsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:upsACLineVoltsIn.setStatus(_A)
_UpsBatteryVoltsOut_Type=Integer32
_UpsBatteryVoltsOut_Object=MibScalar
upsBatteryVoltsOut=_UpsBatteryVoltsOut_Object((1,3,6,1,4,1,52,1,6,3,1,1,8),_UpsBatteryVoltsOut_Type())
upsBatteryVoltsOut.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryVoltsOut.setStatus(_A)
_DlForceOnBoot_Type=Integer32
_DlForceOnBoot_Object=MibScalar
dlForceOnBoot=_DlForceOnBoot_Object((1,3,6,1,4,1,52,1,6,4,1),_DlForceOnBoot_Type())
dlForceOnBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:dlForceOnBoot.setStatus(_A)
_DlCommitRAMToFlash_Type=Integer32
_DlCommitRAMToFlash_Object=MibScalar
dlCommitRAMToFlash=_DlCommitRAMToFlash_Object((1,3,6,1,4,1,52,1,6,4,2),_DlCommitRAMToFlash_Type())
dlCommitRAMToFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:dlCommitRAMToFlash.setStatus(_A)
_DlInitiateColdBoot_Type=Integer32
_DlInitiateColdBoot_Object=MibScalar
dlInitiateColdBoot=_DlInitiateColdBoot_Object((1,3,6,1,4,1,52,1,6,4,3),_DlInitiateColdBoot_Type())
dlInitiateColdBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:dlInitiateColdBoot.setStatus(_A)
_DlTFTPRequestHost_Type=IpAddress
_DlTFTPRequestHost_Object=MibScalar
dlTFTPRequestHost=_DlTFTPRequestHost_Object((1,3,6,1,4,1,52,1,6,4,4),_DlTFTPRequestHost_Type())
dlTFTPRequestHost.setMaxAccess(_C)
if mibBuilder.loadTexts:dlTFTPRequestHost.setStatus(_A)
_DlTFTPRequest_Type=DisplayString
_DlTFTPRequest_Object=MibScalar
dlTFTPRequest=_DlTFTPRequest_Object((1,3,6,1,4,1,52,1,6,4,5),_DlTFTPRequest_Type())
dlTFTPRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:dlTFTPRequest.setStatus(_A)
_DlLastImageFilename_Type=DisplayString
_DlLastImageFilename_Object=MibScalar
dlLastImageFilename=_DlLastImageFilename_Object((1,3,6,1,4,1,52,1,6,4,6),_DlLastImageFilename_Type())
dlLastImageFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:dlLastImageFilename.setStatus(_A)
_DlLastServerIPAddress_Type=IpAddress
_DlLastServerIPAddress_Object=MibScalar
dlLastServerIPAddress=_DlLastServerIPAddress_Object((1,3,6,1,4,1,52,1,6,4,7),_DlLastServerIPAddress_Type())
dlLastServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dlLastServerIPAddress.setStatus(_A)
_DlFlashSize_Type=Integer32
_DlFlashSize_Object=MibScalar
dlFlashSize=_DlFlashSize_Object((1,3,6,1,4,1,52,1,6,4,8),_DlFlashSize_Type())
dlFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dlFlashSize.setStatus(_A)
_DlFlashCount_Type=Integer32
_DlFlashCount_Object=MibScalar
dlFlashCount=_DlFlashCount_Object((1,3,6,1,4,1,52,1,6,4,9),_DlFlashCount_Type())
dlFlashCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dlFlashCount.setStatus(_A)
_DlFirmwareBase_Type=Integer32
_DlFirmwareBase_Object=MibScalar
dlFirmwareBase=_DlFirmwareBase_Object((1,3,6,1,4,1,52,1,6,4,10),_DlFirmwareBase_Type())
dlFirmwareBase.setMaxAccess(_B)
if mibBuilder.loadTexts:dlFirmwareBase.setStatus(_A)
_DlFirmwareTop_Type=Integer32
_DlFirmwareTop_Object=MibScalar
dlFirmwareTop=_DlFirmwareTop_Object((1,3,6,1,4,1,52,1,6,4,11),_DlFirmwareTop_Type())
dlFirmwareTop.setMaxAccess(_B)
if mibBuilder.loadTexts:dlFirmwareTop.setStatus(_A)
_DlFirmwareStart_Type=Integer32
_DlFirmwareStart_Object=MibScalar
dlFirmwareStart=_DlFirmwareStart_Object((1,3,6,1,4,1,52,1,6,4,12),_DlFirmwareStart_Type())
dlFirmwareStart.setMaxAccess(_B)
if mibBuilder.loadTexts:dlFirmwareStart.setStatus(_A)
class _DlBootRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_DlBootRev_Type.__name__=_E
_DlBootRev_Object=MibScalar
dlBootRev=_DlBootRev_Object((1,3,6,1,4,1,52,1,6,4,13),_DlBootRev_Type())
dlBootRev.setMaxAccess(_B)
if mibBuilder.loadTexts:dlBootRev.setStatus(_A)
_DlForceBootp_Type=Integer32
_DlForceBootp_Object=MibScalar
dlForceBootp=_DlForceBootp_Object((1,3,6,1,4,1,52,1,6,4,14),_DlForceBootp_Type())
dlForceBootp.setMaxAccess(_C)
if mibBuilder.loadTexts:dlForceBootp.setStatus(_A)
_DlServerName_Type=OctetString
_DlServerName_Object=MibScalar
dlServerName=_DlServerName_Object((1,3,6,1,4,1,52,1,6,4,15),_DlServerName_Type())
dlServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlServerName.setStatus(_A)
class _DlOnLineDownLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),('forceDownLoad',2),('forceDownLoadReset',3)))
_DlOnLineDownLoad_Type.__name__=_D
_DlOnLineDownLoad_Object=MibScalar
dlOnLineDownLoad=_DlOnLineDownLoad_Object((1,3,6,1,4,1,52,1,6,4,16),_DlOnLineDownLoad_Type())
dlOnLineDownLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:dlOnLineDownLoad.setStatus(_A)
class _DlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('unknown',2),(_X,3),('downLoadActive',4),('downLoadCompleteError',5)))
_DlOperStatus_Type.__name__=_D
_DlOperStatus_Object=MibScalar
dlOperStatus=_DlOperStatus_Object((1,3,6,1,4,1,52,1,6,4,17),_DlOperStatus_Type())
dlOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dlOperStatus.setStatus(_A)
_DlNetAddress_Type=IpAddress
_DlNetAddress_Object=MibScalar
dlNetAddress=_DlNetAddress_Object((1,3,6,1,4,1,52,1,6,4,18),_DlNetAddress_Type())
dlNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dlNetAddress.setStatus(_A)
class _DlFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DlFileName_Type.__name__=_E
_DlFileName_Object=MibScalar
dlFileName=_DlFileName_Object((1,3,6,1,4,1,52,1,6,4,19),_DlFileName_Type())
dlFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlFileName.setStatus(_A)
_DlErrorString_Type=DisplayString
_DlErrorString_Object=MibScalar
dlErrorString=_DlErrorString_Object((1,3,6,1,4,1,52,1,6,4,20),_DlErrorString_Type())
dlErrorString.setMaxAccess(_B)
if mibBuilder.loadTexts:dlErrorString.setStatus(_A)
_DlTftpServerGatewayIPAddress_Type=IpAddress
_DlTftpServerGatewayIPAddress_Object=MibScalar
dlTftpServerGatewayIPAddress=_DlTftpServerGatewayIPAddress_Object((1,3,6,1,4,1,52,1,6,4,21),_DlTftpServerGatewayIPAddress_Type())
dlTftpServerGatewayIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dlTftpServerGatewayIPAddress.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'deviceType':deviceType,'deviceName':deviceName,'deviceIPAddress':deviceIPAddress,'deviceTime':deviceTime,'deviceDate':deviceDate,'fnb2':fnb2,'fnbTR':fnbTR,'fnbTRTable':fnbTRTable,'fnbTREntry':fnbTREntry,_L:fnbTRIndex,'fnbConnectLeft':fnbConnectLeft,'fnbConnectRight':fnbConnectRight,'fnbBypass':fnbBypass,'fnbRPBypass':fnbRPBypass,'fnbCSMACD':fnbCSMACD,'fnbCSMACDTable':fnbCSMACDTable,'fnbCSMACDEntry':fnbCSMACDEntry,_P:fnbCSMACDIndex,'fnbConnect':fnbConnect,'fnbPortChanges':fnbPortChanges,'fnbPortConnect':fnbPortConnect,'fnbPortConnectTable':fnbPortConnectTable,'fnbPortConnectEntry':fnbPortConnectEntry,_T:fnbPortConnectBoardIndex,_U:fnbPortConnectPortIndex,'fnbPortConnectPortAssignment':fnbPortConnectPortAssignment,'fnbPortConnectCompID':fnbPortConnectCompID,'fnbPortConnectionChanges':fnbPortConnectionChanges,'chassis':chassis,'chassisHWRev':chassisHWRev,'chassisType':chassisType,'chassisSlots':chassisSlots,'chassisFNB':chassisFNB,'chassisAlarmEna':chassisAlarmEna,'chassisAlarmState':chassisAlarmState,'environment':environment,'powerTable':powerTable,'powerEntry':powerEntry,_V:powerSupplyNum,'powerSupplyState':powerSupplyState,'powerSupplyId':powerSupplyId,'powerSupplyRedun':powerSupplyRedun,'powerSupplyRemoteDisable':powerSupplyRemoteDisable,'nB55':nB55,'nB55HWAddress':nB55HWAddress,'nB55HWRev':nB55HWRev,'nB55FWRev':nB55FWRev,'mRXI':mRXI,'mRXIHWAddress':mRXIHWAddress,'mRXIHWRev':mRXIHWRev,'mRXIFWRev':mRXIFWRev,'iRM3':iRM3,'iRM3HWAddress':iRM3HWAddress,'iRM3HWRev':iRM3HWRev,'iRM3FWRev':iRM3FWRev,'iRM3PortAssoc':iRM3PortAssoc,'iRM3BPSupport':iRM3BPSupport,'tRMM':tRMM,'tRMMHWAddress':tRMMHWAddress,'tRMMHWRev':tRMMHWRev,'tRMMFWRev':tRMMFWRev,'eMME':eMME,'eMMEHWAddress':eMMEHWAddress,'eMMEHWRev':eMMEHWRev,'eMMEFWRev':eMMEFWRev,'eMMEBoardMap':eMMEBoardMap,'fPRedundancy':fPRedundancy,'fPRedund':fPRedund,'fPRedundReset':fPRedundReset,'fPRedundPollInterval':fPRedundPollInterval,'fPRedundRetrys':fPRedundRetrys,'fPRedundNumAddr':fPRedundNumAddr,'fPRedundAddAddr':fPRedundAddAddr,'fPRedundDelAddr':fPRedundDelAddr,'fPRedundActivePort':fPRedundActivePort,'fPRedundEnable':fPRedundEnable,'fPRedundAddrTable':fPRedundAddrTable,'fPRedundAddrEntry':fPRedundAddrEntry,_W:fPRedundAddrId,'fPRedundAddrIPAddr':fPRedundAddrIPAddr,'upsVersion':upsVersion,'upsRevision':upsRevision,'upsID':upsID,'upsUpTime':upsUpTime,'upsDisable':upsDisable,'upsDisconnect':upsDisconnect,'upsTest':upsTest,'upsBatteryCapacity':upsBatteryCapacity,'upsACLineVoltsIn':upsACLineVoltsIn,'upsBatteryVoltsOut':upsBatteryVoltsOut,'dlForceOnBoot':dlForceOnBoot,'dlCommitRAMToFlash':dlCommitRAMToFlash,'dlInitiateColdBoot':dlInitiateColdBoot,'dlTFTPRequestHost':dlTFTPRequestHost,'dlTFTPRequest':dlTFTPRequest,'dlLastImageFilename':dlLastImageFilename,'dlLastServerIPAddress':dlLastServerIPAddress,'dlFlashSize':dlFlashSize,'dlFlashCount':dlFlashCount,'dlFirmwareBase':dlFirmwareBase,'dlFirmwareTop':dlFirmwareTop,'dlFirmwareStart':dlFirmwareStart,'dlBootRev':dlBootRev,'dlForceBootp':dlForceBootp,'dlServerName':dlServerName,'dlOnLineDownLoad':dlOnLineDownLoad,'dlOperStatus':dlOperStatus,'dlNetAddress':dlNetAddress,'dlFileName':dlFileName,'dlErrorString':dlErrorString,'dlTftpServerGatewayIPAddress':dlTftpServerGatewayIPAddress})