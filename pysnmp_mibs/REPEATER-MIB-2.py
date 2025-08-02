_O='notUsed'
_N='active'
_M='linkSignalActive'
_L='linkSignalInactive'
_K='trapson'
_J='trapsoff'
_I='OctetString'
_H='deprecated'
_G='enable'
_F='disable'
_E='optional'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonRev1,product,repeaterRev1,repeaterRev2,subSysMMAC,sysChassis,sysRepeaters=mibBuilder.importSymbols('IRM-OIDS','commonRev1','product','repeaterRev1','repeaterRev2','subSysMMAC','sysChassis','sysRepeaters')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_DeviceType_Type=Integer32
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,52,1,1,1,1),_DeviceType_Type())
deviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
_DeviceName_Type=OctetString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,52,1,1,1,2),_DeviceName_Type())
deviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
_DeviceIPAddress_Type=IpAddress
_DeviceIPAddress_Object=MibScalar
deviceIPAddress=_DeviceIPAddress_Object((1,3,6,1,4,1,52,1,1,1,3),_DeviceIPAddress_Type())
deviceIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceIPAddress.setStatus(_A)
class _CurrentTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CurrentTime_Type.__name__=_I
_CurrentTime_Object=MibScalar
currentTime=_CurrentTime_Object((1,3,6,1,4,1,52,1,1,1,4),_CurrentTime_Type())
currentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:currentTime.setStatus(_E)
class _CurrentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CurrentDate_Type.__name__=_I
_CurrentDate_Object=MibScalar
currentDate=_CurrentDate_Object((1,3,6,1,4,1,52,1,1,1,5),_CurrentDate_Type())
currentDate.setMaxAccess(_C)
if mibBuilder.loadTexts:currentDate.setStatus(_E)
_MACAddress_Type=OctetString
_MACAddress_Object=MibScalar
mACAddress=_MACAddress_Object((1,3,6,1,4,1,52,1,1,1,6),_MACAddress_Type())
mACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mACAddress.setStatus(_A)
_SoidIRMSNMP_ObjectIdentity=ObjectIdentity
soidIRMSNMP=_SoidIRMSNMP_ObjectIdentity((1,3,6,1,4,1,52,1,1,2,2,1))
_SoidIRBM_ObjectIdentity=ObjectIdentity
soidIRBM=_SoidIRBM_ObjectIdentity((1,3,6,1,4,1,52,1,1,2,2,2))
_SoidIRM2_ObjectIdentity=ObjectIdentity
soidIRM2=_SoidIRM2_ObjectIdentity((1,3,6,1,4,1,52,1,1,2,2,3))
_SoidMINIMMAC_ObjectIdentity=ObjectIdentity
soidMINIMMAC=_SoidMINIMMAC_ObjectIdentity((1,3,6,1,4,1,52,1,1,2,3,1))
_SoidMRXI_ObjectIdentity=ObjectIdentity
soidMRXI=_SoidMRXI_ObjectIdentity((1,3,6,1,4,1,52,1,1,2,3,2))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,1))
class _DeviceMMACType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('mMAC3',1),('mMAC5',2),('minimmac',3),('mrxi1',4),('mrxi2',5),('mMACm8Shunt',6),('mMACm3Shunt',7),('mMACm5Shunt',8),('mMAC8FNBShunt',9),('mMAC3FNBShunt',10),('mMAC5FNBShunt',11),('mMACm8FNB',12)))
_DeviceMMACType_Type.__name__=_D
_DeviceMMACType_Object=MibScalar
deviceMMACType=_DeviceMMACType_Object((1,3,6,1,4,1,52,1,2,1,1,2),_DeviceMMACType_Type())
deviceMMACType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMMACType.setStatus(_A)
class _DeviceSlots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,8)));namedValues=NamedValues(*(('mMAC3',3),('mMAC5',5),('mMAC8',8)))
_DeviceSlots_Type.__name__=_D
_DeviceSlots_Object=MibScalar
deviceSlots=_DeviceSlots_Object((1,3,6,1,4,1,52,1,2,1,1,3),_DeviceSlots_Type())
deviceSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSlots.setStatus(_A)
_DeviceOccupiedSlots_Type=Integer32
_DeviceOccupiedSlots_Object=MibScalar
deviceOccupiedSlots=_DeviceOccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,4),_DeviceOccupiedSlots_Type())
deviceOccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOccupiedSlots.setStatus(_A)
_DevicePortsOn_Type=Integer32
_DevicePortsOn_Object=MibScalar
devicePortsOn=_DevicePortsOn_Object((1,3,6,1,4,1,52,1,2,1,1,5),_DevicePortsOn_Type())
devicePortsOn.setMaxAccess(_C)
if mibBuilder.loadTexts:devicePortsOn.setStatus(_A)
_DeviceTotalPorts_Type=Integer32
_DeviceTotalPorts_Object=MibScalar
deviceTotalPorts=_DeviceTotalPorts_Object((1,3,6,1,4,1,52,1,2,1,1,6),_DeviceTotalPorts_Type())
deviceTotalPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTotalPorts.setStatus(_A)
_DeviceTotalPkts_Type=Counter32
_DeviceTotalPkts_Object=MibScalar
deviceTotalPkts=_DeviceTotalPkts_Object((1,3,6,1,4,1,52,1,2,1,1,7),_DeviceTotalPkts_Type())
deviceTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTotalPkts.setStatus(_A)
_DeviceTotalErrors_Type=Counter32
_DeviceTotalErrors_Object=MibScalar
deviceTotalErrors=_DeviceTotalErrors_Object((1,3,6,1,4,1,52,1,2,1,1,8),_DeviceTotalErrors_Type())
deviceTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTotalErrors.setStatus(_E)
_DeviceTransmitColls_Type=Counter32
_DeviceTransmitColls_Object=MibScalar
deviceTransmitColls=_DeviceTransmitColls_Object((1,3,6,1,4,1,52,1,2,1,1,9),_DeviceTransmitColls_Type())
deviceTransmitColls.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTransmitColls.setStatus(_E)
_DeviceRecColls_Type=Counter32
_DeviceRecColls_Object=MibScalar
deviceRecColls=_DeviceRecColls_Object((1,3,6,1,4,1,52,1,2,1,1,10),_DeviceRecColls_Type())
deviceRecColls.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRecColls.setStatus(_E)
_DeviceAligns_Type=Counter32
_DeviceAligns_Object=MibScalar
deviceAligns=_DeviceAligns_Object((1,3,6,1,4,1,52,1,2,1,1,11),_DeviceAligns_Type())
deviceAligns.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceAligns.setStatus(_E)
_DeviceCRCs_Type=Counter32
_DeviceCRCs_Object=MibScalar
deviceCRCs=_DeviceCRCs_Object((1,3,6,1,4,1,52,1,2,1,1,12),_DeviceCRCs_Type())
deviceCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceCRCs.setStatus(_E)
_DeviceRunts_Type=Counter32
_DeviceRunts_Object=MibScalar
deviceRunts=_DeviceRunts_Object((1,3,6,1,4,1,52,1,2,1,1,13),_DeviceRunts_Type())
deviceRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRunts.setStatus(_E)
_DeviceOOWColls_Type=Counter32
_DeviceOOWColls_Object=MibScalar
deviceOOWColls=_DeviceOOWColls_Object((1,3,6,1,4,1,52,1,2,1,1,14),_DeviceOOWColls_Type())
deviceOOWColls.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOOWColls.setStatus(_E)
_DeviceNoResources_Type=Counter32
_DeviceNoResources_Object=MibScalar
deviceNoResources=_DeviceNoResources_Object((1,3,6,1,4,1,52,1,2,1,1,15),_DeviceNoResources_Type())
deviceNoResources.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceNoResources.setStatus(_E)
_DeviceRecBytes_Type=Counter32
_DeviceRecBytes_Object=MibScalar
deviceRecBytes=_DeviceRecBytes_Object((1,3,6,1,4,1,52,1,2,1,1,16),_DeviceRecBytes_Type())
deviceRecBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRecBytes.setStatus(_E)
_DeviceGiantFrames_Type=Counter32
_DeviceGiantFrames_Object=MibScalar
deviceGiantFrames=_DeviceGiantFrames_Object((1,3,6,1,4,1,52,1,2,1,1,17),_DeviceGiantFrames_Type())
deviceGiantFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceGiantFrames.setStatus(_E)
_DeviceRestart_Type=Integer32
_DeviceRestart_Object=MibScalar
deviceRestart=_DeviceRestart_Object((1,3,6,1,4,1,52,1,2,1,1,18),_DeviceRestart_Type())
deviceRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceRestart.setStatus(_A)
_DeviceResetCounters_Type=Integer32
_DeviceResetCounters_Object=MibScalar
deviceResetCounters=_DeviceResetCounters_Object((1,3,6,1,4,1,52,1,2,1,1,19),_DeviceResetCounters_Type())
deviceResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceResetCounters.setStatus(_A)
_DeviceRedundantCts_Type=Integer32
_DeviceRedundantCts_Object=MibScalar
deviceRedundantCts=_DeviceRedundantCts_Object((1,3,6,1,4,1,52,1,2,1,1,20),_DeviceRedundantCts_Type())
deviceRedundantCts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRedundantCts.setStatus(_E)
class _DeviceTimeBase_Type(Integer32):defaultValue=10
_DeviceTimeBase_Type.__name__=_D
_DeviceTimeBase_Object=MibScalar
deviceTimeBase=_DeviceTimeBase_Object((1,3,6,1,4,1,52,1,2,1,1,24),_DeviceTimeBase_Type())
deviceTimeBase.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceTimeBase.setStatus(_E)
_DeviceResetRedundancy_Type=Integer32
_DeviceResetRedundancy_Object=MibScalar
deviceResetRedundancy=_DeviceResetRedundancy_Object((1,3,6,1,4,1,52,1,2,1,1,25),_DeviceResetRedundancy_Type())
deviceResetRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceResetRedundancy.setStatus(_E)
class _DeviceSrcAddrAgingTime_Type(Integer32):defaultValue=60
_DeviceSrcAddrAgingTime_Type.__name__=_D
_DeviceSrcAddrAgingTime_Object=MibScalar
deviceSrcAddrAgingTime=_DeviceSrcAddrAgingTime_Object((1,3,6,1,4,1,52,1,2,1,1,26),_DeviceSrcAddrAgingTime_Type())
deviceSrcAddrAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSrcAddrAgingTime.setStatus(_E)
class _DeviceSrcAddrTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_DeviceSrcAddrTraps_Type.__name__=_D
_DeviceSrcAddrTraps_Object=MibScalar
deviceSrcAddrTraps=_DeviceSrcAddrTraps_Object((1,3,6,1,4,1,52,1,2,1,1,27),_DeviceSrcAddrTraps_Type())
deviceSrcAddrTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSrcAddrTraps.setStatus(_E)
class _DeviceSrcAddrLocked_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lockoff',1),('lockon',2)))
_DeviceSrcAddrLocked_Type.__name__=_D
_DeviceSrcAddrLocked_Object=MibScalar
deviceSrcAddrLocked=_DeviceSrcAddrLocked_Object((1,3,6,1,4,1,52,1,2,1,1,28),_DeviceSrcAddrLocked_Type())
deviceSrcAddrLocked.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSrcAddrLocked.setStatus(_E)
_DeviceEnetBoardMap_Type=Integer32
_DeviceEnetBoardMap_Object=MibScalar
deviceEnetBoardMap=_DeviceEnetBoardMap_Object((1,3,6,1,4,1,52,1,2,1,1,29),_DeviceEnetBoardMap_Type())
deviceEnetBoardMap.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceEnetBoardMap.setStatus(_A)
_DeviceTokenRingBoardMap_Type=Integer32
_DeviceTokenRingBoardMap_Object=MibScalar
deviceTokenRingBoardMap=_DeviceTokenRingBoardMap_Object((1,3,6,1,4,1,52,1,2,1,1,30),_DeviceTokenRingBoardMap_Type())
deviceTokenRingBoardMap.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTokenRingBoardMap.setStatus(_A)
_DeviceFDDIBoardMap_Type=Integer32
_DeviceFDDIBoardMap_Object=MibScalar
deviceFDDIBoardMap=_DeviceFDDIBoardMap_Object((1,3,6,1,4,1,52,1,2,1,1,31),_DeviceFDDIBoardMap_Type())
deviceFDDIBoardMap.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceFDDIBoardMap.setStatus(_A)
_DeviceRestoreDefaults_Type=Integer32
_DeviceRestoreDefaults_Object=MibScalar
deviceRestoreDefaults=_DeviceRestoreDefaults_Object((1,3,6,1,4,1,52,1,2,1,1,32),_DeviceRestoreDefaults_Type())
deviceRestoreDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceRestoreDefaults.setStatus(_E)
_DeviceActiveUsers_Type=Integer32
_DeviceActiveUsers_Object=MibScalar
deviceActiveUsers=_DeviceActiveUsers_Object((1,3,6,1,4,1,52,1,2,1,1,33),_DeviceActiveUsers_Type())
deviceActiveUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceActiveUsers.setStatus(_E)
_DeviceBroadPkts_Type=Counter32
_DeviceBroadPkts_Object=MibScalar
deviceBroadPkts=_DeviceBroadPkts_Object((1,3,6,1,4,1,52,1,2,1,1,48),_DeviceBroadPkts_Type())
deviceBroadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceBroadPkts.setStatus(_E)
_DeviceMultPkts_Type=Counter32
_DeviceMultPkts_Object=MibScalar
deviceMultPkts=_DeviceMultPkts_Object((1,3,6,1,4,1,52,1,2,1,1,49),_DeviceMultPkts_Type())
deviceMultPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMultPkts.setStatus(_E)
_DeviceThdPartyOccupiedSlots_Type=Integer32
_DeviceThdPartyOccupiedSlots_Object=MibScalar
deviceThdPartyOccupiedSlots=_DeviceThdPartyOccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,51),_DeviceThdPartyOccupiedSlots_Type())
deviceThdPartyOccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceThdPartyOccupiedSlots.setStatus(_E)
_DeviceImimOccupiedSlots_Type=Integer32
_DeviceImimOccupiedSlots_Object=MibScalar
deviceImimOccupiedSlots=_DeviceImimOccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,52),_DeviceImimOccupiedSlots_Type())
deviceImimOccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceImimOccupiedSlots.setStatus(_E)
class _DeviceLinkTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_DeviceLinkTraps_Type.__name__=_D
_DeviceLinkTraps_Object=MibScalar
deviceLinkTraps=_DeviceLinkTraps_Object((1,3,6,1,4,1,52,1,2,1,1,54),_DeviceLinkTraps_Type())
deviceLinkTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLinkTraps.setStatus(_E)
class _DeviceSegTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_DeviceSegTraps_Type.__name__=_D
_DeviceSegTraps_Object=MibScalar
deviceSegTraps=_DeviceSegTraps_Object((1,3,6,1,4,1,52,1,2,1,1,55),_DeviceSegTraps_Type())
deviceSegTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSegTraps.setStatus(_E)
class _CtIPDefaultFrameType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethernet',1),('snap8022',2)))
_CtIPDefaultFrameType_Type.__name__=_D
_CtIPDefaultFrameType_Object=MibScalar
ctIPDefaultFrameType=_CtIPDefaultFrameType_Object((1,3,6,1,4,1,52,1,2,1,1,56),_CtIPDefaultFrameType_Type())
ctIPDefaultFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctIPDefaultFrameType.setStatus(_A)
_Board_ObjectIdentity=ObjectIdentity
board=_Board_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,2))
_Port_ObjectIdentity=ObjectIdentity
port=_Port_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,3))
_SourceAddr_ObjectIdentity=ObjectIdentity
sourceAddr=_SourceAddr_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,7))
_SourceAddrBoard_Type=Integer32
_SourceAddrBoard_Object=MibScalar
sourceAddrBoard=_SourceAddrBoard_Object((1,3,6,1,4,1,52,1,2,1,7,1),_SourceAddrBoard_Type())
sourceAddrBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceAddrBoard.setStatus(_A)
_SourceAddrPort_Type=Integer32
_SourceAddrPort_Object=MibScalar
sourceAddrPort=_SourceAddrPort_Object((1,3,6,1,4,1,52,1,2,1,7,2),_SourceAddrPort_Type())
sourceAddrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceAddrPort.setStatus(_A)
_Redundancy_ObjectIdentity=ObjectIdentity
redundancy=_Redundancy_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,8))
class _RedundancyPollInterval_Type(Integer32):defaultValue=3
_RedundancyPollInterval_Type.__name__=_D
_RedundancyPollInterval_Object=MibScalar
redundancyPollInterval=_RedundancyPollInterval_Object((1,3,6,1,4,1,52,1,2,1,8,1),_RedundancyPollInterval_Type())
redundancyPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyPollInterval.setStatus(_A)
_RedundancyTestTod_Type=OctetString
_RedundancyTestTod_Object=MibScalar
redundancyTestTod=_RedundancyTestTod_Object((1,3,6,1,4,1,52,1,2,1,8,2),_RedundancyTestTod_Type())
redundancyTestTod.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyTestTod.setStatus(_A)
class _RedundancyPerformTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('performTest',1))
_RedundancyPerformTest_Type.__name__=_D
_RedundancyPerformTest_Object=MibScalar
redundancyPerformTest=_RedundancyPerformTest_Object((1,3,6,1,4,1,52,1,2,1,8,3),_RedundancyPerformTest_Type())
redundancyPerformTest.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyPerformTest.setStatus(_A)
_RedundancyCircuitName_Type=OctetString
_RedundancyCircuitName_Object=MibScalar
redundancyCircuitName=_RedundancyCircuitName_Object((1,3,6,1,4,1,52,1,2,1,8,4),_RedundancyCircuitName_Type())
redundancyCircuitName.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyCircuitName.setStatus(_A)
class _RedundancyRetryCount_Type(Integer32):defaultValue=0
_RedundancyRetryCount_Type.__name__=_D
_RedundancyRetryCount_Object=MibScalar
redundancyRetryCount=_RedundancyRetryCount_Object((1,3,6,1,4,1,52,1,2,1,8,5),_RedundancyRetryCount_Type())
redundancyRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyRetryCount.setStatus(_A)
_RedundancyNumBPs_Type=Integer32
_RedundancyNumBPs_Object=MibScalar
redundancyNumBPs=_RedundancyNumBPs_Object((1,3,6,1,4,1,52,1,2,1,8,6),_RedundancyNumBPs_Type())
redundancyNumBPs.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyNumBPs.setStatus(_A)
_RedundancyCircuitBoards_Type=Integer32
_RedundancyCircuitBoards_Object=MibScalar
redundancyCircuitBoards=_RedundancyCircuitBoards_Object((1,3,6,1,4,1,52,1,2,1,8,7),_RedundancyCircuitBoards_Type())
redundancyCircuitBoards.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyCircuitBoards.setStatus(_A)
_RedundancyCircuitPort_Type=Integer32
_RedundancyCircuitPort_Object=MibScalar
redundancyCircuitPort=_RedundancyCircuitPort_Object((1,3,6,1,4,1,52,1,2,1,8,8),_RedundancyCircuitPort_Type())
redundancyCircuitPort.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyCircuitPort.setStatus(_A)
_RedundancyCircuitTypes_Type=Integer32
_RedundancyCircuitTypes_Object=MibScalar
redundancyCircuitTypes=_RedundancyCircuitTypes_Object((1,3,6,1,4,1,52,1,2,1,8,9),_RedundancyCircuitTypes_Type())
redundancyCircuitTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyCircuitTypes.setStatus(_A)
_RedundancyCircuitNumAddr_Type=Integer32
_RedundancyCircuitNumAddr_Object=MibScalar
redundancyCircuitNumAddr=_RedundancyCircuitNumAddr_Object((1,3,6,1,4,1,52,1,2,1,8,10),_RedundancyCircuitNumAddr_Type())
redundancyCircuitNumAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyCircuitNumAddr.setStatus(_A)
_RedundancyCircuitMACAddrAdd_Type=OctetString
_RedundancyCircuitMACAddrAdd_Object=MibScalar
redundancyCircuitMACAddrAdd=_RedundancyCircuitMACAddrAdd_Object((1,3,6,1,4,1,52,1,2,1,8,11),_RedundancyCircuitMACAddrAdd_Type())
redundancyCircuitMACAddrAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyCircuitMACAddrAdd.setStatus(_A)
_RedundancyCircuitMACAddrDel_Type=OctetString
_RedundancyCircuitMACAddrDel_Object=MibScalar
redundancyCircuitMACAddrDel=_RedundancyCircuitMACAddrDel_Object((1,3,6,1,4,1,52,1,2,1,8,12),_RedundancyCircuitMACAddrDel_Type())
redundancyCircuitMACAddrDel.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyCircuitMACAddrDel.setStatus(_A)
_RedundancyCircuitMACAddrDisp_Type=OctetString
_RedundancyCircuitMACAddrDisp_Object=MibScalar
redundancyCircuitMACAddrDisp=_RedundancyCircuitMACAddrDisp_Object((1,3,6,1,4,1,52,1,2,1,8,13),_RedundancyCircuitMACAddrDisp_Type())
redundancyCircuitMACAddrDisp.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyCircuitMACAddrDisp.setStatus(_A)
class _RedundancyCircuitEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RedundancyCircuitEnable_Type.__name__=_D
_RedundancyCircuitEnable_Object=MibScalar
redundancyCircuitEnable=_RedundancyCircuitEnable_Object((1,3,6,1,4,1,52,1,2,1,8,14),_RedundancyCircuitEnable_Type())
redundancyCircuitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyCircuitEnable.setStatus(_A)
class _RedundancyCircuitReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_RedundancyCircuitReset_Type.__name__=_D
_RedundancyCircuitReset_Object=MibScalar
redundancyCircuitReset=_RedundancyCircuitReset_Object((1,3,6,1,4,1,52,1,2,1,8,15),_RedundancyCircuitReset_Type())
redundancyCircuitReset.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyCircuitReset.setStatus(_A)
_Alarm_ObjectIdentity=ObjectIdentity
alarm=_Alarm_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9))
_DevAlrm_ObjectIdentity=ObjectIdentity
devAlrm=_DevAlrm_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1))
_DevTraffic_ObjectIdentity=ObjectIdentity
devTraffic=_DevTraffic_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1,1))
class _DevTrafficEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DevTrafficEnable_Type.__name__=_D
_DevTrafficEnable_Object=MibScalar
devTrafficEnable=_DevTrafficEnable_Object((1,3,6,1,4,1,52,1,2,1,9,1,1,1),_DevTrafficEnable_Type())
devTrafficEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:devTrafficEnable.setStatus(_A)
class _DevTrafficThreshold_Type(Integer32):defaultValue=1000
_DevTrafficThreshold_Type.__name__=_D
_DevTrafficThreshold_Object=MibScalar
devTrafficThreshold=_DevTrafficThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,1,1,2),_DevTrafficThreshold_Type())
devTrafficThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:devTrafficThreshold.setStatus(_A)
_DevColls_ObjectIdentity=ObjectIdentity
devColls=_DevColls_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1,2))
class _DevCollsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DevCollsEnable_Type.__name__=_D
_DevCollsEnable_Object=MibScalar
devCollsEnable=_DevCollsEnable_Object((1,3,6,1,4,1,52,1,2,1,9,1,2,1),_DevCollsEnable_Type())
devCollsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:devCollsEnable.setStatus(_A)
_DevCollsThreshold_Type=Integer32
_DevCollsThreshold_Object=MibScalar
devCollsThreshold=_DevCollsThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,1,2,2),_DevCollsThreshold_Type())
devCollsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:devCollsThreshold.setStatus(_A)
_DevError_ObjectIdentity=ObjectIdentity
devError=_DevError_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1,3))
class _DevErrorEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DevErrorEnable_Type.__name__=_D
_DevErrorEnable_Object=MibScalar
devErrorEnable=_DevErrorEnable_Object((1,3,6,1,4,1,52,1,2,1,9,1,3,1),_DevErrorEnable_Type())
devErrorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:devErrorEnable.setStatus(_A)
class _DevErrorThreshold_Type(Integer32):defaultValue=10
_DevErrorThreshold_Type.__name__=_D
_DevErrorThreshold_Object=MibScalar
devErrorThreshold=_DevErrorThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,1,3,2),_DevErrorThreshold_Type())
devErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:devErrorThreshold.setStatus(_A)
class _DevErrorSource_Type(Integer32):defaultValue=63
_DevErrorSource_Type.__name__=_D
_DevErrorSource_Object=MibScalar
devErrorSource=_DevErrorSource_Object((1,3,6,1,4,1,52,1,2,1,9,1,3,3),_DevErrorSource_Type())
devErrorSource.setMaxAccess(_C)
if mibBuilder.loadTexts:devErrorSource.setStatus(_A)
_DevBroad_ObjectIdentity=ObjectIdentity
devBroad=_DevBroad_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1,4))
class _DevBroadEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DevBroadEnable_Type.__name__=_D
_DevBroadEnable_Object=MibScalar
devBroadEnable=_DevBroadEnable_Object((1,3,6,1,4,1,52,1,2,1,9,1,4,1),_DevBroadEnable_Type())
devBroadEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:devBroadEnable.setStatus(_A)
_DevBroadThreshold_Type=Integer32
_DevBroadThreshold_Object=MibScalar
devBroadThreshold=_DevBroadThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,1,4,2),_DevBroadThreshold_Type())
devBroadThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:devBroadThreshold.setStatus(_A)
_BdAlrm_ObjectIdentity=ObjectIdentity
bdAlrm=_BdAlrm_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2))
_BdTraffic_ObjectIdentity=ObjectIdentity
bdTraffic=_BdTraffic_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2,1))
class _BdTrafficEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdTrafficEnable_Type.__name__=_D
_BdTrafficEnable_Object=MibScalar
bdTrafficEnable=_BdTrafficEnable_Object((1,3,6,1,4,1,52,1,2,1,9,2,1,1),_BdTrafficEnable_Type())
bdTrafficEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdTrafficEnable.setStatus(_A)
class _BdTrafficThreshold_Type(Integer32):defaultValue=100
_BdTrafficThreshold_Type.__name__=_D
_BdTrafficThreshold_Object=MibScalar
bdTrafficThreshold=_BdTrafficThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,2,1,2),_BdTrafficThreshold_Type())
bdTrafficThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdTrafficThreshold.setStatus(_A)
class _BdTrafficBdDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdTrafficBdDisable_Type.__name__=_D
_BdTrafficBdDisable_Object=MibScalar
bdTrafficBdDisable=_BdTrafficBdDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,1,3),_BdTrafficBdDisable_Type())
bdTrafficBdDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdTrafficBdDisable.setStatus(_A)
_BdColls_ObjectIdentity=ObjectIdentity
bdColls=_BdColls_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2,2))
class _BdCollsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdCollsEnable_Type.__name__=_D
_BdCollsEnable_Object=MibScalar
bdCollsEnable=_BdCollsEnable_Object((1,3,6,1,4,1,52,1,2,1,9,2,2,1),_BdCollsEnable_Type())
bdCollsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdCollsEnable.setStatus(_A)
class _BdCollsThreshold_Type(Integer32):defaultValue=1
_BdCollsThreshold_Type.__name__=_D
_BdCollsThreshold_Object=MibScalar
bdCollsThreshold=_BdCollsThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,2,2,2),_BdCollsThreshold_Type())
bdCollsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdCollsThreshold.setStatus(_A)
class _BdCollsBdDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdCollsBdDisable_Type.__name__=_D
_BdCollsBdDisable_Object=MibScalar
bdCollsBdDisable=_BdCollsBdDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,2,3),_BdCollsBdDisable_Type())
bdCollsBdDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdCollsBdDisable.setStatus(_A)
_BdError_ObjectIdentity=ObjectIdentity
bdError=_BdError_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2,3))
class _BdErrorEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdErrorEnable_Type.__name__=_D
_BdErrorEnable_Object=MibScalar
bdErrorEnable=_BdErrorEnable_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,1),_BdErrorEnable_Type())
bdErrorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorEnable.setStatus(_A)
class _BdErrorThreshold_Type(Integer32):defaultValue=10
_BdErrorThreshold_Type.__name__=_D
_BdErrorThreshold_Object=MibScalar
bdErrorThreshold=_BdErrorThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,2),_BdErrorThreshold_Type())
bdErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorThreshold.setStatus(_A)
class _BdErrorSource_Type(Integer32):defaultValue=63
_BdErrorSource_Type.__name__=_D
_BdErrorSource_Object=MibScalar
bdErrorSource=_BdErrorSource_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,3),_BdErrorSource_Type())
bdErrorSource.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorSource.setStatus(_A)
class _BdErrorBdDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdErrorBdDisable_Type.__name__=_D
_BdErrorBdDisable_Object=MibScalar
bdErrorBdDisable=_BdErrorBdDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,4),_BdErrorBdDisable_Type())
bdErrorBdDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorBdDisable.setStatus(_A)
_BdBroad_ObjectIdentity=ObjectIdentity
bdBroad=_BdBroad_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2,4))
class _BdBroadEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdBroadEnable_Type.__name__=_D
_BdBroadEnable_Object=MibScalar
bdBroadEnable=_BdBroadEnable_Object((1,3,6,1,4,1,52,1,2,1,9,2,4,1),_BdBroadEnable_Type())
bdBroadEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdBroadEnable.setStatus(_A)
_BdBroadThreshold_Type=Integer32
_BdBroadThreshold_Object=MibScalar
bdBroadThreshold=_BdBroadThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,2,4,2),_BdBroadThreshold_Type())
bdBroadThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdBroadThreshold.setStatus(_A)
class _BdBroadDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BdBroadDisable_Type.__name__=_D
_BdBroadDisable_Object=MibScalar
bdBroadDisable=_BdBroadDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,4,3),_BdBroadDisable_Type())
bdBroadDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdBroadDisable.setStatus(_A)
_PortAlrm_ObjectIdentity=ObjectIdentity
portAlrm=_PortAlrm_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3))
_PortTraffic_ObjectIdentity=ObjectIdentity
portTraffic=_PortTraffic_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,1))
class _PortTrafficEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortTrafficEnable_Type.__name__=_D
_PortTrafficEnable_Object=MibScalar
portTrafficEnable=_PortTrafficEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,1,1),_PortTrafficEnable_Type())
portTrafficEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portTrafficEnable.setStatus(_A)
class _PortTrafficThreshold_Type(Integer32):defaultValue=100
_PortTrafficThreshold_Type.__name__=_D
_PortTrafficThreshold_Object=MibScalar
portTrafficThreshold=_PortTrafficThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,1,2),_PortTrafficThreshold_Type())
portTrafficThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portTrafficThreshold.setStatus(_A)
class _PortTrafficPortDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortTrafficPortDisable_Type.__name__=_D
_PortTrafficPortDisable_Object=MibScalar
portTrafficPortDisable=_PortTrafficPortDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,1,3),_PortTrafficPortDisable_Type())
portTrafficPortDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portTrafficPortDisable.setStatus(_A)
_PortColls_ObjectIdentity=ObjectIdentity
portColls=_PortColls_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,2))
class _PortCollsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortCollsEnable_Type.__name__=_D
_PortCollsEnable_Object=MibScalar
portCollsEnable=_PortCollsEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,2,1),_PortCollsEnable_Type())
portCollsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portCollsEnable.setStatus(_A)
class _PortCollsThreshold_Type(Integer32):defaultValue=1
_PortCollsThreshold_Type.__name__=_D
_PortCollsThreshold_Object=MibScalar
portCollsThreshold=_PortCollsThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,2,2),_PortCollsThreshold_Type())
portCollsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portCollsThreshold.setStatus(_A)
class _PortCollsPortDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortCollsPortDisable_Type.__name__=_D
_PortCollsPortDisable_Object=MibScalar
portCollsPortDisable=_PortCollsPortDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,2,3),_PortCollsPortDisable_Type())
portCollsPortDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portCollsPortDisable.setStatus(_A)
_PortError_ObjectIdentity=ObjectIdentity
portError=_PortError_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,3))
class _PortErrorEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortErrorEnable_Type.__name__=_D
_PortErrorEnable_Object=MibScalar
portErrorEnable=_PortErrorEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,1),_PortErrorEnable_Type())
portErrorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorEnable.setStatus(_A)
class _PortErrorThreshold_Type(Integer32):defaultValue=10
_PortErrorThreshold_Type.__name__=_D
_PortErrorThreshold_Object=MibScalar
portErrorThreshold=_PortErrorThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,2),_PortErrorThreshold_Type())
portErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorThreshold.setStatus(_A)
class _PortErrorSource_Type(Integer32):defaultValue=63
_PortErrorSource_Type.__name__=_D
_PortErrorSource_Object=MibScalar
portErrorSource=_PortErrorSource_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,3),_PortErrorSource_Type())
portErrorSource.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorSource.setStatus(_A)
class _PortErrorPortDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortErrorPortDisable_Type.__name__=_D
_PortErrorPortDisable_Object=MibScalar
portErrorPortDisable=_PortErrorPortDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,4),_PortErrorPortDisable_Type())
portErrorPortDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorPortDisable.setStatus(_A)
_PortBroad_ObjectIdentity=ObjectIdentity
portBroad=_PortBroad_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,4))
class _PortBroadEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBroadEnable_Type.__name__=_D
_PortBroadEnable_Object=MibScalar
portBroadEnable=_PortBroadEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,4,1),_PortBroadEnable_Type())
portBroadEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portBroadEnable.setStatus(_A)
_PortBroadThreshold_Type=Counter32
_PortBroadThreshold_Object=MibScalar
portBroadThreshold=_PortBroadThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,4,2),_PortBroadThreshold_Type())
portBroadThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portBroadThreshold.setStatus(_A)
class _PortBroadDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBroadDisable_Type.__name__=_D
_PortBroadDisable_Object=MibScalar
portBroadDisable=_PortBroadDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,4,3),_PortBroadDisable_Type())
portBroadDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portBroadDisable.setStatus(_A)
_Rr2device_ObjectIdentity=ObjectIdentity
rr2device=_Rr2device_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,1))
_CommonD_ObjectIdentity=ObjectIdentity
commonD=_CommonD_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,1,1))
_EthernetD_ObjectIdentity=ObjectIdentity
ethernetD=_EthernetD_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,1,2))
_TokenRingD_ObjectIdentity=ObjectIdentity
tokenRingD=_TokenRingD_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,1,3))
_DeviceTRTokenRingPortsOn_Type=Integer32
_DeviceTRTokenRingPortsOn_Object=MibScalar
deviceTRTokenRingPortsOn=_DeviceTRTokenRingPortsOn_Object((1,3,6,1,4,1,52,1,2,2,1,3,1),_DeviceTRTokenRingPortsOn_Type())
deviceTRTokenRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRTokenRingPortsOn.setStatus(_H)
_DeviceTRTotalTokenRingPorts_Type=Integer32
_DeviceTRTotalTokenRingPorts_Object=MibScalar
deviceTRTotalTokenRingPorts=_DeviceTRTotalTokenRingPorts_Object((1,3,6,1,4,1,52,1,2,2,1,3,2),_DeviceTRTotalTokenRingPorts_Type())
deviceTRTotalTokenRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRTotalTokenRingPorts.setStatus(_H)
_DeviceTRTotalTokenRingRingPortsOn_Type=Integer32
_DeviceTRTotalTokenRingRingPortsOn_Object=MibScalar
deviceTRTotalTokenRingRingPortsOn=_DeviceTRTotalTokenRingRingPortsOn_Object((1,3,6,1,4,1,52,1,2,2,1,3,3),_DeviceTRTotalTokenRingRingPortsOn_Type())
deviceTRTotalTokenRingRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRTotalTokenRingRingPortsOn.setStatus(_H)
_DeviceTRTotalTokenRingRingPorts_Type=Integer32
_DeviceTRTotalTokenRingRingPorts_Object=MibScalar
deviceTRTotalTokenRingRingPorts=_DeviceTRTotalTokenRingRingPorts_Object((1,3,6,1,4,1,52,1,2,2,1,3,4),_DeviceTRTotalTokenRingRingPorts_Type())
deviceTRTotalTokenRingRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRTotalTokenRingRingPorts.setStatus(_H)
_DeviceTRTotalTokenRingRings_Type=Integer32
_DeviceTRTotalTokenRingRings_Object=MibScalar
deviceTRTotalTokenRingRings=_DeviceTRTotalTokenRingRings_Object((1,3,6,1,4,1,52,1,2,2,1,3,5),_DeviceTRTotalTokenRingRings_Type())
deviceTRTotalTokenRingRings.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRTotalTokenRingRings.setStatus(_H)
_DeviceTRTotalTokenRingBoards_Type=Integer32
_DeviceTRTotalTokenRingBoards_Object=MibScalar
deviceTRTotalTokenRingBoards=_DeviceTRTotalTokenRingBoards_Object((1,3,6,1,4,1,52,1,2,2,1,3,6),_DeviceTRTotalTokenRingBoards_Type())
deviceTRTotalTokenRingBoards.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRTotalTokenRingBoards.setStatus(_H)
_DeviceTRTokenRingBoardMap_Type=Integer32
_DeviceTRTokenRingBoardMap_Object=MibScalar
deviceTRTokenRingBoardMap=_DeviceTRTokenRingBoardMap_Object((1,3,6,1,4,1,52,1,2,2,1,3,7),_DeviceTRTokenRingBoardMap_Type())
deviceTRTokenRingBoardMap.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRTokenRingBoardMap.setStatus(_H)
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,2))
_Rr2board_ObjectIdentity=ObjectIdentity
rr2board=_Rr2board_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3))
_CommonB_ObjectIdentity=ObjectIdentity
commonB=_CommonB_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3,1))
_BoardIndex_Type=Integer32
_BoardIndex_Object=MibScalar
boardIndex=_BoardIndex_Object((1,3,6,1,4,1,52,1,2,2,3,1,1),_BoardIndex_Type())
boardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boardIndex.setStatus(_A)
_BoardName_Type=OctetString
_BoardName_Object=MibScalar
boardName=_BoardName_Object((1,3,6,1,4,1,52,1,2,2,3,1,2),_BoardName_Type())
boardName.setMaxAccess(_C)
if mibBuilder.loadTexts:boardName.setStatus(_A)
_BoardType_Type=Integer32
_BoardType_Object=MibScalar
boardType=_BoardType_Object((1,3,6,1,4,1,52,1,2,2,3,1,3),_BoardType_Type())
boardType.setMaxAccess(_B)
if mibBuilder.loadTexts:boardType.setStatus(_A)
_BoardTotalPorts_Type=Integer32
_BoardTotalPorts_Object=MibScalar
boardTotalPorts=_BoardTotalPorts_Object((1,3,6,1,4,1,52,1,2,2,3,1,4),_BoardTotalPorts_Type())
boardTotalPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalPorts.setStatus(_A)
_BoardPortsOn_Type=Integer32
_BoardPortsOn_Object=MibScalar
boardPortsOn=_BoardPortsOn_Object((1,3,6,1,4,1,52,1,2,2,3,1,6),_BoardPortsOn_Type())
boardPortsOn.setMaxAccess(_C)
if mibBuilder.loadTexts:boardPortsOn.setStatus(_A)
_BoardActiveUsers_Type=Integer32
_BoardActiveUsers_Object=MibScalar
boardActiveUsers=_BoardActiveUsers_Object((1,3,6,1,4,1,52,1,2,2,3,1,8),_BoardActiveUsers_Type())
boardActiveUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:boardActiveUsers.setStatus(_A)
_EthernetB_ObjectIdentity=ObjectIdentity
ethernetB=_EthernetB_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3,2))
_BoardTotalPkts_Type=Counter32
_BoardTotalPkts_Object=MibScalar
boardTotalPkts=_BoardTotalPkts_Object((1,3,6,1,4,1,52,1,2,2,3,2,1),_BoardTotalPkts_Type())
boardTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalPkts.setStatus(_A)
_BoardTotalErrors_Type=Counter32
_BoardTotalErrors_Object=MibScalar
boardTotalErrors=_BoardTotalErrors_Object((1,3,6,1,4,1,52,1,2,2,3,2,2),_BoardTotalErrors_Type())
boardTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalErrors.setStatus(_A)
_BoardTransColls_Type=Counter32
_BoardTransColls_Object=MibScalar
boardTransColls=_BoardTransColls_Object((1,3,6,1,4,1,52,1,2,2,3,2,3),_BoardTransColls_Type())
boardTransColls.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTransColls.setStatus(_A)
_BoardRecColls_Type=Counter32
_BoardRecColls_Object=MibScalar
boardRecColls=_BoardRecColls_Object((1,3,6,1,4,1,52,1,2,2,3,2,4),_BoardRecColls_Type())
boardRecColls.setMaxAccess(_B)
if mibBuilder.loadTexts:boardRecColls.setStatus(_A)
_BoardAligns_Type=Counter32
_BoardAligns_Object=MibScalar
boardAligns=_BoardAligns_Object((1,3,6,1,4,1,52,1,2,2,3,2,5),_BoardAligns_Type())
boardAligns.setMaxAccess(_B)
if mibBuilder.loadTexts:boardAligns.setStatus(_A)
_BoardCRCs_Type=Counter32
_BoardCRCs_Object=MibScalar
boardCRCs=_BoardCRCs_Object((1,3,6,1,4,1,52,1,2,2,3,2,6),_BoardCRCs_Type())
boardCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:boardCRCs.setStatus(_A)
_BoardRunts_Type=Counter32
_BoardRunts_Object=MibScalar
boardRunts=_BoardRunts_Object((1,3,6,1,4,1,52,1,2,2,3,2,7),_BoardRunts_Type())
boardRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardRunts.setStatus(_A)
_BoardOOWColls_Type=Counter32
_BoardOOWColls_Object=MibScalar
boardOOWColls=_BoardOOWColls_Object((1,3,6,1,4,1,52,1,2,2,3,2,8),_BoardOOWColls_Type())
boardOOWColls.setMaxAccess(_B)
if mibBuilder.loadTexts:boardOOWColls.setStatus(_A)
_BoardNoResources_Type=Counter32
_BoardNoResources_Object=MibScalar
boardNoResources=_BoardNoResources_Object((1,3,6,1,4,1,52,1,2,2,3,2,9),_BoardNoResources_Type())
boardNoResources.setMaxAccess(_B)
if mibBuilder.loadTexts:boardNoResources.setStatus(_A)
_BoardRecBytes_Type=Counter32
_BoardRecBytes_Object=MibScalar
boardRecBytes=_BoardRecBytes_Object((1,3,6,1,4,1,52,1,2,2,3,2,10),_BoardRecBytes_Type())
boardRecBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:boardRecBytes.setStatus(_A)
_BoardGiants_Type=Counter32
_BoardGiants_Object=MibScalar
boardGiants=_BoardGiants_Object((1,3,6,1,4,1,52,1,2,2,3,2,11),_BoardGiants_Type())
boardGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:boardGiants.setStatus(_A)
_BoardBroadPkts_Type=Counter32
_BoardBroadPkts_Object=MibScalar
boardBroadPkts=_BoardBroadPkts_Object((1,3,6,1,4,1,52,1,2,2,3,2,26),_BoardBroadPkts_Type())
boardBroadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardBroadPkts.setStatus(_A)
_BoardMultPkts_Type=Counter32
_BoardMultPkts_Object=MibScalar
boardMultPkts=_BoardMultPkts_Object((1,3,6,1,4,1,52,1,2,2,3,2,27),_BoardMultPkts_Type())
boardMultPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardMultPkts.setStatus(_A)
_TokenRingB_ObjectIdentity=ObjectIdentity
tokenRingB=_TokenRingB_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3,3))
_BoardTotalRingPorts_Type=Integer32
_BoardTotalRingPorts_Object=MibScalar
boardTotalRingPorts=_BoardTotalRingPorts_Object((1,3,6,1,4,1,52,1,2,2,3,3,1),_BoardTotalRingPorts_Type())
boardTotalRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalRingPorts.setStatus(_H)
_BoardTotalStationPorts_Type=Integer32
_BoardTotalStationPorts_Object=MibScalar
boardTotalStationPorts=_BoardTotalStationPorts_Object((1,3,6,1,4,1,52,1,2,2,3,3,2),_BoardTotalStationPorts_Type())
boardTotalStationPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalStationPorts.setStatus(_H)
class _BoardModeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('management',1),('auto',2)))
_BoardModeStatus_Type.__name__=_D
_BoardModeStatus_Object=MibScalar
boardModeStatus=_BoardModeStatus_Object((1,3,6,1,4,1,52,1,2,2,3,3,3),_BoardModeStatus_Type())
boardModeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:boardModeStatus.setStatus(_H)
_BoardTotalRingPortsOn_Type=Integer32
_BoardTotalRingPortsOn_Object=MibScalar
boardTotalRingPortsOn=_BoardTotalRingPortsOn_Object((1,3,6,1,4,1,52,1,2,2,3,3,4),_BoardTotalRingPortsOn_Type())
boardTotalRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalRingPortsOn.setStatus(_H)
_BoardTotalStationPortsOn_Type=Integer32
_BoardTotalStationPortsOn_Object=MibScalar
boardTotalStationPortsOn=_BoardTotalStationPortsOn_Object((1,3,6,1,4,1,52,1,2,2,3,3,5),_BoardTotalStationPortsOn_Type())
boardTotalStationPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalStationPortsOn.setStatus(_H)
class _BoardSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,16)));namedValues=NamedValues(*(('fourMhz',4),('sixteenMhz',16)))
_BoardSpeed_Type.__name__=_D
_BoardSpeed_Object=MibScalar
boardSpeed=_BoardSpeed_Object((1,3,6,1,4,1,52,1,2,2,3,3,6),_BoardSpeed_Type())
boardSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:boardSpeed.setStatus(_H)
class _BoardRingSpeedFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noFaultDetected',1),('faultDetected',2)))
_BoardRingSpeedFault_Type.__name__=_D
_BoardRingSpeedFault_Object=MibScalar
boardRingSpeedFault=_BoardRingSpeedFault_Object((1,3,6,1,4,1,52,1,2,2,3,3,7),_BoardRingSpeedFault_Type())
boardRingSpeedFault.setMaxAccess(_B)
if mibBuilder.loadTexts:boardRingSpeedFault.setStatus(_H)
_BoardFirstRingPort_Type=Integer32
_BoardFirstRingPort_Object=MibScalar
boardFirstRingPort=_BoardFirstRingPort_Object((1,3,6,1,4,1,52,1,2,2,3,3,9),_BoardFirstRingPort_Type())
boardFirstRingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:boardFirstRingPort.setStatus(_H)
_FddiB_ObjectIdentity=ObjectIdentity
fddiB=_FddiB_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3,4))
_Rr2port_ObjectIdentity=ObjectIdentity
rr2port=_Rr2port_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4))
_CommonP_ObjectIdentity=ObjectIdentity
commonP=_CommonP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,1))
_PortIndex_Type=Integer32
_PortIndex_Object=MibScalar
portIndex=_PortIndex_Object((1,3,6,1,4,1,52,1,2,2,4,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
_PortMediaType_Type=Integer32
_PortMediaType_Object=MibScalar
portMediaType=_PortMediaType_Object((1,3,6,1,4,1,52,1,2,2,4,1,2),_PortMediaType_Type())
portMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:portMediaType.setStatus(_A)
class _PortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_PortAdminState_Type.__name__=_D
_PortAdminState_Object=MibScalar
portAdminState=_PortAdminState_Object((1,3,6,1,4,1,52,1,2,2,4,1,3),_PortAdminState_Type())
portAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:portAdminState.setStatus(_A)
_PortSourceAddr_Type=OctetString
_PortSourceAddr_Object=MibScalar
portSourceAddr=_PortSourceAddr_Object((1,3,6,1,4,1,52,1,2,2,4,1,4),_PortSourceAddr_Type())
portSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:portSourceAddr.setStatus(_E)
_PortActiveUsers_Type=Integer32
_PortActiveUsers_Object=MibScalar
portActiveUsers=_PortActiveUsers_Object((1,3,6,1,4,1,52,1,2,2,4,1,6),_PortActiveUsers_Type())
portActiveUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:portActiveUsers.setStatus(_E)
_EthernetP_ObjectIdentity=ObjectIdentity
ethernetP=_EthernetP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,2))
class _PortTopologyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('station',1),('trunk',2)))
_PortTopologyType_Type.__name__=_D
_PortTopologyType_Object=MibScalar
portTopologyType=_PortTopologyType_Object((1,3,6,1,4,1,52,1,2,2,4,2,1),_PortTopologyType_Type())
portTopologyType.setMaxAccess(_B)
if mibBuilder.loadTexts:portTopologyType.setStatus(_A)
class _PortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('linkSignalNotSupported',3)))
_PortLinkStatus_Type.__name__=_D
_PortLinkStatus_Object=MibScalar
portLinkStatus=_PortLinkStatus_Object((1,3,6,1,4,1,52,1,2,2,4,2,2),_PortLinkStatus_Type())
portLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portLinkStatus.setStatus(_A)
class _PortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('segmented',2)))
_PortStatus_Type.__name__=_D
_PortStatus_Object=MibScalar
portStatus=_PortStatus_Object((1,3,6,1,4,1,52,1,2,2,4,2,3),_PortStatus_Type())
portStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatus.setStatus(_A)
_PortTotalPkts_Type=Counter32
_PortTotalPkts_Object=MibScalar
portTotalPkts=_PortTotalPkts_Object((1,3,6,1,4,1,52,1,2,2,4,2,4),_PortTotalPkts_Type())
portTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portTotalPkts.setStatus(_A)
_PortTotalErrors_Type=Counter32
_PortTotalErrors_Object=MibScalar
portTotalErrors=_PortTotalErrors_Object((1,3,6,1,4,1,52,1,2,2,4,2,5),_PortTotalErrors_Type())
portTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:portTotalErrors.setStatus(_A)
_PortTransmitColls_Type=Counter32
_PortTransmitColls_Object=MibScalar
portTransmitColls=_PortTransmitColls_Object((1,3,6,1,4,1,52,1,2,2,4,2,6),_PortTransmitColls_Type())
portTransmitColls.setMaxAccess(_B)
if mibBuilder.loadTexts:portTransmitColls.setStatus(_A)
_PortRecColls_Type=Counter32
_PortRecColls_Object=MibScalar
portRecColls=_PortRecColls_Object((1,3,6,1,4,1,52,1,2,2,4,2,7),_PortRecColls_Type())
portRecColls.setMaxAccess(_B)
if mibBuilder.loadTexts:portRecColls.setStatus(_A)
_PortAligns_Type=Counter32
_PortAligns_Object=MibScalar
portAligns=_PortAligns_Object((1,3,6,1,4,1,52,1,2,2,4,2,8),_PortAligns_Type())
portAligns.setMaxAccess(_B)
if mibBuilder.loadTexts:portAligns.setStatus(_A)
_PortCRCs_Type=Counter32
_PortCRCs_Object=MibScalar
portCRCs=_PortCRCs_Object((1,3,6,1,4,1,52,1,2,2,4,2,9),_PortCRCs_Type())
portCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:portCRCs.setStatus(_A)
_PortRunts_Type=Counter32
_PortRunts_Object=MibScalar
portRunts=_PortRunts_Object((1,3,6,1,4,1,52,1,2,2,4,2,10),_PortRunts_Type())
portRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:portRunts.setStatus(_A)
_PortOOWColls_Type=Counter32
_PortOOWColls_Object=MibScalar
portOOWColls=_PortOOWColls_Object((1,3,6,1,4,1,52,1,2,2,4,2,11),_PortOOWColls_Type())
portOOWColls.setMaxAccess(_B)
if mibBuilder.loadTexts:portOOWColls.setStatus(_A)
_PortNoResources_Type=Counter32
_PortNoResources_Object=MibScalar
portNoResources=_PortNoResources_Object((1,3,6,1,4,1,52,1,2,2,4,2,12),_PortNoResources_Type())
portNoResources.setMaxAccess(_B)
if mibBuilder.loadTexts:portNoResources.setStatus(_A)
_PortRecBytes_Type=Counter32
_PortRecBytes_Object=MibScalar
portRecBytes=_PortRecBytes_Object((1,3,6,1,4,1,52,1,2,2,4,2,13),_PortRecBytes_Type())
portRecBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:portRecBytes.setStatus(_A)
_PortGiantFrames_Type=Counter32
_PortGiantFrames_Object=MibScalar
portGiantFrames=_PortGiantFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,14),_PortGiantFrames_Type())
portGiantFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portGiantFrames.setStatus(_A)
_PortRedundCrt_Type=Integer32
_PortRedundCrt_Object=MibScalar
portRedundCrt=_PortRedundCrt_Object((1,3,6,1,4,1,52,1,2,2,4,2,15),_PortRedundCrt_Type())
portRedundCrt.setMaxAccess(_C)
if mibBuilder.loadTexts:portRedundCrt.setStatus(_A)
class _PortRedundType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_O,1),('primary',3),('backup',4)))
_PortRedundType_Type.__name__=_D
_PortRedundType_Object=MibScalar
portRedundType=_PortRedundType_Object((1,3,6,1,4,1,52,1,2,2,4,2,16),_PortRedundType_Type())
portRedundType.setMaxAccess(_C)
if mibBuilder.loadTexts:portRedundType.setStatus(_A)
class _PortRedundStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_N,2),('inactive',3)))
_PortRedundStatus_Type.__name__=_D
_PortRedundStatus_Object=MibScalar
portRedundStatus=_PortRedundStatus_Object((1,3,6,1,4,1,52,1,2,2,4,2,17),_PortRedundStatus_Type())
portRedundStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portRedundStatus.setStatus(_A)
class _PortForceTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notForced',1),('forced',2)))
_PortForceTrunkType_Type.__name__=_D
_PortForceTrunkType_Object=MibScalar
portForceTrunkType=_PortForceTrunkType_Object((1,3,6,1,4,1,52,1,2,2,4,2,18),_PortForceTrunkType_Type())
portForceTrunkType.setMaxAccess(_C)
if mibBuilder.loadTexts:portForceTrunkType.setStatus(_A)
_PortBroadPkts_Type=Counter32
_PortBroadPkts_Object=MibScalar
portBroadPkts=_PortBroadPkts_Object((1,3,6,1,4,1,52,1,2,2,4,2,33),_PortBroadPkts_Type())
portBroadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portBroadPkts.setStatus(_A)
_PortMultPkts_Type=Counter32
_PortMultPkts_Object=MibScalar
portMultPkts=_PortMultPkts_Object((1,3,6,1,4,1,52,1,2,2,4,2,34),_PortMultPkts_Type())
portMultPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portMultPkts.setStatus(_A)
_TokenRingP_ObjectIdentity=ObjectIdentity
tokenRingP=_TokenRingP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3))
_StationP_ObjectIdentity=ObjectIdentity
stationP=_StationP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3,1))
class _StationPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_StationPortLinkStatus_Type.__name__=_D
_StationPortLinkStatus_Object=MibScalar
stationPortLinkStatus=_StationPortLinkStatus_Object((1,3,6,1,4,1,52,1,2,2,4,3,1,1),_StationPortLinkStatus_Type())
stationPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:stationPortLinkStatus.setStatus(_H)
_StationPortLinkStateTime_Type=Integer32
_StationPortLinkStateTime_Object=MibScalar
stationPortLinkStateTime=_StationPortLinkStateTime_Object((1,3,6,1,4,1,52,1,2,2,4,3,1,2),_StationPortLinkStateTime_Type())
stationPortLinkStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:stationPortLinkStateTime.setStatus(_H)
_RingP_ObjectIdentity=ObjectIdentity
ringP=_RingP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3,2))
_FddiP_ObjectIdentity=ObjectIdentity
fddiP=_FddiP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,4))
_RepeaterTables_ObjectIdentity=ObjectIdentity
repeaterTables=_RepeaterTables_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,5))
_ProductRev1_ObjectIdentity=ObjectIdentity
productRev1=_ProductRev1_ObjectIdentity((1,3,6,1,4,1,52,1,5,1))
_Target_ObjectIdentity=ObjectIdentity
target=_Target_ObjectIdentity((1,3,6,1,4,1,52,1,5,1,1))
_TargetRevision_Type=Integer32
_TargetRevision_Object=MibScalar
targetRevision=_TargetRevision_Object((1,3,6,1,4,1,52,1,5,1,1,1),_TargetRevision_Type())
targetRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:targetRevision.setStatus(_A)
_TargetPortAssociation_Type=Integer32
_TargetPortAssociation_Object=MibScalar
targetPortAssociation=_TargetPortAssociation_Object((1,3,6,1,4,1,52,1,5,1,1,2),_TargetPortAssociation_Type())
targetPortAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:targetPortAssociation.setStatus(_A)
_Fnb_ObjectIdentity=ObjectIdentity
fnb=_Fnb_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,1))
_FnbConnectedLeft_Type=Integer32
_FnbConnectedLeft_Object=MibScalar
fnbConnectedLeft=_FnbConnectedLeft_Object((1,3,6,1,4,1,52,1,6,1,1,1),_FnbConnectedLeft_Type())
fnbConnectedLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbConnectedLeft.setStatus(_A)
_FnbConnectedRight_Type=Integer32
_FnbConnectedRight_Object=MibScalar
fnbConnectedRight=_FnbConnectedRight_Object((1,3,6,1,4,1,52,1,6,1,1,2),_FnbConnectedRight_Type())
fnbConnectedRight.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbConnectedRight.setStatus(_A)
_FnbBoardBypassState_Type=Integer32
_FnbBoardBypassState_Object=MibScalar
fnbBoardBypassState=_FnbBoardBypassState_Object((1,3,6,1,4,1,52,1,6,1,1,3),_FnbBoardBypassState_Type())
fnbBoardBypassState.setMaxAccess(_C)
if mibBuilder.loadTexts:fnbBoardBypassState.setStatus(_A)
_AudibleAlarm_ObjectIdentity=ObjectIdentity
audibleAlarm=_AudibleAlarm_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,2))
class _AudibleAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AudibleAlarmEnable_Type.__name__=_D
_AudibleAlarmEnable_Object=MibScalar
audibleAlarmEnable=_AudibleAlarmEnable_Object((1,3,6,1,4,1,52,1,6,1,2,1),_AudibleAlarmEnable_Type())
audibleAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:audibleAlarmEnable.setStatus(_A)
class _AudibleAlarmOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AudibleAlarmOff_Type.__name__=_D
_AudibleAlarmOff_Object=MibScalar
audibleAlarmOff=_AudibleAlarmOff_Object((1,3,6,1,4,1,52,1,6,1,2,2),_AudibleAlarmOff_Type())
audibleAlarmOff.setMaxAccess(_C)
if mibBuilder.loadTexts:audibleAlarmOff.setStatus(_A)
mibBuilder.exportSymbols('REPEATER-MIB-2',**{'deviceType':deviceType,'deviceName':deviceName,'deviceIPAddress':deviceIPAddress,'currentTime':currentTime,'currentDate':currentDate,'mACAddress':mACAddress,'soidIRMSNMP':soidIRMSNMP,'soidIRBM':soidIRBM,'soidIRM2':soidIRM2,'soidMINIMMAC':soidMINIMMAC,'soidMRXI':soidMRXI,'device':device,'deviceMMACType':deviceMMACType,'deviceSlots':deviceSlots,'deviceOccupiedSlots':deviceOccupiedSlots,'devicePortsOn':devicePortsOn,'deviceTotalPorts':deviceTotalPorts,'deviceTotalPkts':deviceTotalPkts,'deviceTotalErrors':deviceTotalErrors,'deviceTransmitColls':deviceTransmitColls,'deviceRecColls':deviceRecColls,'deviceAligns':deviceAligns,'deviceCRCs':deviceCRCs,'deviceRunts':deviceRunts,'deviceOOWColls':deviceOOWColls,'deviceNoResources':deviceNoResources,'deviceRecBytes':deviceRecBytes,'deviceGiantFrames':deviceGiantFrames,'deviceRestart':deviceRestart,'deviceResetCounters':deviceResetCounters,'deviceRedundantCts':deviceRedundantCts,'deviceTimeBase':deviceTimeBase,'deviceResetRedundancy':deviceResetRedundancy,'deviceSrcAddrAgingTime':deviceSrcAddrAgingTime,'deviceSrcAddrTraps':deviceSrcAddrTraps,'deviceSrcAddrLocked':deviceSrcAddrLocked,'deviceEnetBoardMap':deviceEnetBoardMap,'deviceTokenRingBoardMap':deviceTokenRingBoardMap,'deviceFDDIBoardMap':deviceFDDIBoardMap,'deviceRestoreDefaults':deviceRestoreDefaults,'deviceActiveUsers':deviceActiveUsers,'deviceBroadPkts':deviceBroadPkts,'deviceMultPkts':deviceMultPkts,'deviceThdPartyOccupiedSlots':deviceThdPartyOccupiedSlots,'deviceImimOccupiedSlots':deviceImimOccupiedSlots,'deviceLinkTraps':deviceLinkTraps,'deviceSegTraps':deviceSegTraps,'ctIPDefaultFrameType':ctIPDefaultFrameType,'board':board,'port':port,'sourceAddr':sourceAddr,'sourceAddrBoard':sourceAddrBoard,'sourceAddrPort':sourceAddrPort,'redundancy':redundancy,'redundancyPollInterval':redundancyPollInterval,'redundancyTestTod':redundancyTestTod,'redundancyPerformTest':redundancyPerformTest,'redundancyCircuitName':redundancyCircuitName,'redundancyRetryCount':redundancyRetryCount,'redundancyNumBPs':redundancyNumBPs,'redundancyCircuitBoards':redundancyCircuitBoards,'redundancyCircuitPort':redundancyCircuitPort,'redundancyCircuitTypes':redundancyCircuitTypes,'redundancyCircuitNumAddr':redundancyCircuitNumAddr,'redundancyCircuitMACAddrAdd':redundancyCircuitMACAddrAdd,'redundancyCircuitMACAddrDel':redundancyCircuitMACAddrDel,'redundancyCircuitMACAddrDisp':redundancyCircuitMACAddrDisp,'redundancyCircuitEnable':redundancyCircuitEnable,'redundancyCircuitReset':redundancyCircuitReset,'alarm':alarm,'devAlrm':devAlrm,'devTraffic':devTraffic,'devTrafficEnable':devTrafficEnable,'devTrafficThreshold':devTrafficThreshold,'devColls':devColls,'devCollsEnable':devCollsEnable,'devCollsThreshold':devCollsThreshold,'devError':devError,'devErrorEnable':devErrorEnable,'devErrorThreshold':devErrorThreshold,'devErrorSource':devErrorSource,'devBroad':devBroad,'devBroadEnable':devBroadEnable,'devBroadThreshold':devBroadThreshold,'bdAlrm':bdAlrm,'bdTraffic':bdTraffic,'bdTrafficEnable':bdTrafficEnable,'bdTrafficThreshold':bdTrafficThreshold,'bdTrafficBdDisable':bdTrafficBdDisable,'bdColls':bdColls,'bdCollsEnable':bdCollsEnable,'bdCollsThreshold':bdCollsThreshold,'bdCollsBdDisable':bdCollsBdDisable,'bdError':bdError,'bdErrorEnable':bdErrorEnable,'bdErrorThreshold':bdErrorThreshold,'bdErrorSource':bdErrorSource,'bdErrorBdDisable':bdErrorBdDisable,'bdBroad':bdBroad,'bdBroadEnable':bdBroadEnable,'bdBroadThreshold':bdBroadThreshold,'bdBroadDisable':bdBroadDisable,'portAlrm':portAlrm,'portTraffic':portTraffic,'portTrafficEnable':portTrafficEnable,'portTrafficThreshold':portTrafficThreshold,'portTrafficPortDisable':portTrafficPortDisable,'portColls':portColls,'portCollsEnable':portCollsEnable,'portCollsThreshold':portCollsThreshold,'portCollsPortDisable':portCollsPortDisable,'portError':portError,'portErrorEnable':portErrorEnable,'portErrorThreshold':portErrorThreshold,'portErrorSource':portErrorSource,'portErrorPortDisable':portErrorPortDisable,'portBroad':portBroad,'portBroadEnable':portBroadEnable,'portBroadThreshold':portBroadThreshold,'portBroadDisable':portBroadDisable,'rr2device':rr2device,'commonD':commonD,'ethernetD':ethernetD,'tokenRingD':tokenRingD,'deviceTRTokenRingPortsOn':deviceTRTokenRingPortsOn,'deviceTRTotalTokenRingPorts':deviceTRTotalTokenRingPorts,'deviceTRTotalTokenRingRingPortsOn':deviceTRTotalTokenRingRingPortsOn,'deviceTRTotalTokenRingRingPorts':deviceTRTotalTokenRingRingPorts,'deviceTRTotalTokenRingRings':deviceTRTotalTokenRingRings,'deviceTRTotalTokenRingBoards':deviceTRTotalTokenRingBoards,'deviceTRTokenRingBoardMap':deviceTRTokenRingBoardMap,'network':network,'rr2board':rr2board,'commonB':commonB,'boardIndex':boardIndex,'boardName':boardName,'boardType':boardType,'boardTotalPorts':boardTotalPorts,'boardPortsOn':boardPortsOn,'boardActiveUsers':boardActiveUsers,'ethernetB':ethernetB,'boardTotalPkts':boardTotalPkts,'boardTotalErrors':boardTotalErrors,'boardTransColls':boardTransColls,'boardRecColls':boardRecColls,'boardAligns':boardAligns,'boardCRCs':boardCRCs,'boardRunts':boardRunts,'boardOOWColls':boardOOWColls,'boardNoResources':boardNoResources,'boardRecBytes':boardRecBytes,'boardGiants':boardGiants,'boardBroadPkts':boardBroadPkts,'boardMultPkts':boardMultPkts,'tokenRingB':tokenRingB,'boardTotalRingPorts':boardTotalRingPorts,'boardTotalStationPorts':boardTotalStationPorts,'boardModeStatus':boardModeStatus,'boardTotalRingPortsOn':boardTotalRingPortsOn,'boardTotalStationPortsOn':boardTotalStationPortsOn,'boardSpeed':boardSpeed,'boardRingSpeedFault':boardRingSpeedFault,'boardFirstRingPort':boardFirstRingPort,'fddiB':fddiB,'rr2port':rr2port,'commonP':commonP,'portIndex':portIndex,'portMediaType':portMediaType,'portAdminState':portAdminState,'portSourceAddr':portSourceAddr,'portActiveUsers':portActiveUsers,'ethernetP':ethernetP,'portTopologyType':portTopologyType,'portLinkStatus':portLinkStatus,'portStatus':portStatus,'portTotalPkts':portTotalPkts,'portTotalErrors':portTotalErrors,'portTransmitColls':portTransmitColls,'portRecColls':portRecColls,'portAligns':portAligns,'portCRCs':portCRCs,'portRunts':portRunts,'portOOWColls':portOOWColls,'portNoResources':portNoResources,'portRecBytes':portRecBytes,'portGiantFrames':portGiantFrames,'portRedundCrt':portRedundCrt,'portRedundType':portRedundType,'portRedundStatus':portRedundStatus,'portForceTrunkType':portForceTrunkType,'portBroadPkts':portBroadPkts,'portMultPkts':portMultPkts,'tokenRingP':tokenRingP,'stationP':stationP,'stationPortLinkStatus':stationPortLinkStatus,'stationPortLinkStateTime':stationPortLinkStateTime,'ringP':ringP,'fddiP':fddiP,'repeaterTables':repeaterTables,'productRev1':productRev1,'target':target,'targetRevision':targetRevision,'targetPortAssociation':targetPortAssociation,'fnb':fnb,'fnbConnectedLeft':fnbConnectedLeft,'fnbConnectedRight':fnbConnectedRight,'fnbBoardBypassState':fnbBoardBypassState,'audibleAlarm':audibleAlarm,'audibleAlarmEnable':audibleAlarmEnable,'audibleAlarmOff':audibleAlarmOff})