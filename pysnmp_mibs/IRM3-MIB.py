_Y='faulted'
_X='attached'
_W='detached'
_V='obsolete'
_U='notUsed'
_T='active'
_S='linkSignalActive'
_R='linkSignalInactive'
_Q='faultDetected'
_P='noFaultDetected'
_O='notOperational'
_N='operational'
_M='trapsOn'
_L='trapsOff'
_K='lockOn'
_J='lockOff'
_I='deprecated'
_H='on'
_G='off'
_F='enable'
_E='disable'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
repeaterRev1,repeaterRev2,subSysMMAC=mibBuilder.importSymbols('IRM-OIDS','repeaterRev1','repeaterRev2','subSysMMAC')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,1))
class _DeviceMMACType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('unknown',1),('mMAC8',2),('mMAC5',3),('mMAC3',4),('mINIMMAC',5),('mRXI',6),('m3Shunt',7),('m5Shunt',8),('m8FNB',9),('nonFNB',10),('mMAC3Shunting',11),('mMAC5Shunting',12),('mMAC8Shunting',13),('m8Shunting',14)))
_DeviceMMACType_Type.__name__=_D
_DeviceMMACType_Object=MibScalar
deviceMMACType=_DeviceMMACType_Object((1,3,6,1,4,1,52,1,2,1,1,2),_DeviceMMACType_Type())
deviceMMACType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMMACType.setStatus(_A)
_DeviceSlots_Type=Integer32
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
devicePortsOn.setMaxAccess(_B)
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
if mibBuilder.loadTexts:deviceTotalErrors.setStatus(_A)
_DeviceTransmitColls_Type=Counter32
_DeviceTransmitColls_Object=MibScalar
deviceTransmitColls=_DeviceTransmitColls_Object((1,3,6,1,4,1,52,1,2,1,1,9),_DeviceTransmitColls_Type())
deviceTransmitColls.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTransmitColls.setStatus(_A)
_DeviceRecColls_Type=Counter32
_DeviceRecColls_Object=MibScalar
deviceRecColls=_DeviceRecColls_Object((1,3,6,1,4,1,52,1,2,1,1,10),_DeviceRecColls_Type())
deviceRecColls.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRecColls.setStatus(_A)
_DeviceAlignErrs_Type=Counter32
_DeviceAlignErrs_Object=MibScalar
deviceAlignErrs=_DeviceAlignErrs_Object((1,3,6,1,4,1,52,1,2,1,1,11),_DeviceAlignErrs_Type())
deviceAlignErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceAlignErrs.setStatus(_A)
_DeviceCRCErrs_Type=Counter32
_DeviceCRCErrs_Object=MibScalar
deviceCRCErrs=_DeviceCRCErrs_Object((1,3,6,1,4,1,52,1,2,1,1,12),_DeviceCRCErrs_Type())
deviceCRCErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceCRCErrs.setStatus(_A)
_DeviceRunts_Type=Counter32
_DeviceRunts_Object=MibScalar
deviceRunts=_DeviceRunts_Object((1,3,6,1,4,1,52,1,2,1,1,13),_DeviceRunts_Type())
deviceRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRunts.setStatus(_A)
_DeviceOOWColls_Type=Counter32
_DeviceOOWColls_Object=MibScalar
deviceOOWColls=_DeviceOOWColls_Object((1,3,6,1,4,1,52,1,2,1,1,14),_DeviceOOWColls_Type())
deviceOOWColls.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOOWColls.setStatus(_A)
_DeviceNoResources_Type=Counter32
_DeviceNoResources_Object=MibScalar
deviceNoResources=_DeviceNoResources_Object((1,3,6,1,4,1,52,1,2,1,1,15),_DeviceNoResources_Type())
deviceNoResources.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceNoResources.setStatus(_A)
_DeviceRecBytes_Type=Counter32
_DeviceRecBytes_Object=MibScalar
deviceRecBytes=_DeviceRecBytes_Object((1,3,6,1,4,1,52,1,2,1,1,16),_DeviceRecBytes_Type())
deviceRecBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRecBytes.setStatus(_A)
_DeviceGiantFrames_Type=Counter32
_DeviceGiantFrames_Object=MibScalar
deviceGiantFrames=_DeviceGiantFrames_Object((1,3,6,1,4,1,52,1,2,1,1,17),_DeviceGiantFrames_Type())
deviceGiantFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceGiantFrames.setStatus(_A)
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
if mibBuilder.loadTexts:deviceRedundantCts.setStatus(_A)
_DeviceDiscover_Type=Integer32
_DeviceDiscover_Object=MibScalar
deviceDiscover=_DeviceDiscover_Object((1,3,6,1,4,1,52,1,2,1,1,21),_DeviceDiscover_Type())
deviceDiscover.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceDiscover.setStatus(_I)
_DeviceTimeBase_Type=Integer32
_DeviceTimeBase_Object=MibScalar
deviceTimeBase=_DeviceTimeBase_Object((1,3,6,1,4,1,52,1,2,1,1,24),_DeviceTimeBase_Type())
deviceTimeBase.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceTimeBase.setStatus(_A)
_DeviceResetRedundancy_Type=Integer32
_DeviceResetRedundancy_Object=MibScalar
deviceResetRedundancy=_DeviceResetRedundancy_Object((1,3,6,1,4,1,52,1,2,1,1,25),_DeviceResetRedundancy_Type())
deviceResetRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceResetRedundancy.setStatus(_A)
_DeviceSrcAddrAgingTime_Type=Integer32
_DeviceSrcAddrAgingTime_Object=MibScalar
deviceSrcAddrAgingTime=_DeviceSrcAddrAgingTime_Object((1,3,6,1,4,1,52,1,2,1,1,26),_DeviceSrcAddrAgingTime_Type())
deviceSrcAddrAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSrcAddrAgingTime.setStatus(_A)
class _DeviceSrcAddrTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_DeviceSrcAddrTraps_Type.__name__=_D
_DeviceSrcAddrTraps_Object=MibScalar
deviceSrcAddrTraps=_DeviceSrcAddrTraps_Object((1,3,6,1,4,1,52,1,2,1,1,27),_DeviceSrcAddrTraps_Type())
deviceSrcAddrTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSrcAddrTraps.setStatus(_A)
class _DeviceSrcAddrLocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_DeviceSrcAddrLocked_Type.__name__=_D
_DeviceSrcAddrLocked_Object=MibScalar
deviceSrcAddrLocked=_DeviceSrcAddrLocked_Object((1,3,6,1,4,1,52,1,2,1,1,28),_DeviceSrcAddrLocked_Type())
deviceSrcAddrLocked.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSrcAddrLocked.setStatus(_A)
_DeviceEtherOccupiedSlots_Type=Integer32
_DeviceEtherOccupiedSlots_Object=MibScalar
deviceEtherOccupiedSlots=_DeviceEtherOccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,29),_DeviceEtherOccupiedSlots_Type())
deviceEtherOccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceEtherOccupiedSlots.setStatus(_A)
_DeviceTROccupiedSlots_Type=Integer32
_DeviceTROccupiedSlots_Object=MibScalar
deviceTROccupiedSlots=_DeviceTROccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,30),_DeviceTROccupiedSlots_Type())
deviceTROccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTROccupiedSlots.setStatus(_A)
_DeviceFDDIOccupiedSlots_Type=Integer32
_DeviceFDDIOccupiedSlots_Object=MibScalar
deviceFDDIOccupiedSlots=_DeviceFDDIOccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,31),_DeviceFDDIOccupiedSlots_Type())
deviceFDDIOccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceFDDIOccupiedSlots.setStatus(_A)
_DeviceRestoreDefaults_Type=Integer32
_DeviceRestoreDefaults_Object=MibScalar
deviceRestoreDefaults=_DeviceRestoreDefaults_Object((1,3,6,1,4,1,52,1,2,1,1,32),_DeviceRestoreDefaults_Type())
deviceRestoreDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceRestoreDefaults.setStatus(_A)
_DeviceActiveUsers_Type=Integer32
_DeviceActiveUsers_Object=MibScalar
deviceActiveUsers=_DeviceActiveUsers_Object((1,3,6,1,4,1,52,1,2,1,1,33),_DeviceActiveUsers_Type())
deviceActiveUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceActiveUsers.setStatus(_A)
_DeviceOSIFrames_Type=Counter32
_DeviceOSIFrames_Object=MibScalar
deviceOSIFrames=_DeviceOSIFrames_Object((1,3,6,1,4,1,52,1,2,1,1,34),_DeviceOSIFrames_Type())
deviceOSIFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOSIFrames.setStatus(_A)
_DeviceNovellFrames_Type=Counter32
_DeviceNovellFrames_Object=MibScalar
deviceNovellFrames=_DeviceNovellFrames_Object((1,3,6,1,4,1,52,1,2,1,1,35),_DeviceNovellFrames_Type())
deviceNovellFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceNovellFrames.setStatus(_A)
_DeviceBanyanFrames_Type=Counter32
_DeviceBanyanFrames_Object=MibScalar
deviceBanyanFrames=_DeviceBanyanFrames_Object((1,3,6,1,4,1,52,1,2,1,1,36),_DeviceBanyanFrames_Type())
deviceBanyanFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceBanyanFrames.setStatus(_A)
_DeviceDECNetFrames_Type=Counter32
_DeviceDECNetFrames_Object=MibScalar
deviceDECNetFrames=_DeviceDECNetFrames_Object((1,3,6,1,4,1,52,1,2,1,1,37),_DeviceDECNetFrames_Type())
deviceDECNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDECNetFrames.setStatus(_A)
_DeviceXNSFrames_Type=Counter32
_DeviceXNSFrames_Object=MibScalar
deviceXNSFrames=_DeviceXNSFrames_Object((1,3,6,1,4,1,52,1,2,1,1,38),_DeviceXNSFrames_Type())
deviceXNSFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceXNSFrames.setStatus(_A)
_DeviceIPFrames_Type=Counter32
_DeviceIPFrames_Object=MibScalar
deviceIPFrames=_DeviceIPFrames_Object((1,3,6,1,4,1,52,1,2,1,1,39),_DeviceIPFrames_Type())
deviceIPFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceIPFrames.setStatus(_A)
_DeviceCtronFrames_Type=Counter32
_DeviceCtronFrames_Object=MibScalar
deviceCtronFrames=_DeviceCtronFrames_Object((1,3,6,1,4,1,52,1,2,1,1,40),_DeviceCtronFrames_Type())
deviceCtronFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceCtronFrames.setStatus(_A)
_DeviceAppletalkFrames_Type=Counter32
_DeviceAppletalkFrames_Object=MibScalar
deviceAppletalkFrames=_DeviceAppletalkFrames_Object((1,3,6,1,4,1,52,1,2,1,1,41),_DeviceAppletalkFrames_Type())
deviceAppletalkFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceAppletalkFrames.setStatus(_A)
_DeviceOtherFrames_Type=Counter32
_DeviceOtherFrames_Object=MibScalar
deviceOtherFrames=_DeviceOtherFrames_Object((1,3,6,1,4,1,52,1,2,1,1,42),_DeviceOtherFrames_Type())
deviceOtherFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOtherFrames.setStatus(_A)
_Device64To127Frames_Type=Counter32
_Device64To127Frames_Object=MibScalar
device64To127Frames=_Device64To127Frames_Object((1,3,6,1,4,1,52,1,2,1,1,43),_Device64To127Frames_Type())
device64To127Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:device64To127Frames.setStatus(_A)
_Device128To255Frames_Type=Counter32
_Device128To255Frames_Object=MibScalar
device128To255Frames=_Device128To255Frames_Object((1,3,6,1,4,1,52,1,2,1,1,44),_Device128To255Frames_Type())
device128To255Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:device128To255Frames.setStatus(_A)
_Device256To511Frames_Type=Counter32
_Device256To511Frames_Object=MibScalar
device256To511Frames=_Device256To511Frames_Object((1,3,6,1,4,1,52,1,2,1,1,45),_Device256To511Frames_Type())
device256To511Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:device256To511Frames.setStatus(_A)
_Device512To1023Frames_Type=Counter32
_Device512To1023Frames_Object=MibScalar
device512To1023Frames=_Device512To1023Frames_Object((1,3,6,1,4,1,52,1,2,1,1,46),_Device512To1023Frames_Type())
device512To1023Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:device512To1023Frames.setStatus(_A)
_Device1024To1518Frames_Type=Counter32
_Device1024To1518Frames_Object=MibScalar
device1024To1518Frames=_Device1024To1518Frames_Object((1,3,6,1,4,1,52,1,2,1,1,47),_Device1024To1518Frames_Type())
device1024To1518Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:device1024To1518Frames.setStatus(_A)
_DeviceBroadPkts_Type=Counter32
_DeviceBroadPkts_Object=MibScalar
deviceBroadPkts=_DeviceBroadPkts_Object((1,3,6,1,4,1,52,1,2,1,1,48),_DeviceBroadPkts_Type())
deviceBroadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceBroadPkts.setStatus(_A)
_DeviceMultPkts_Type=Counter32
_DeviceMultPkts_Object=MibScalar
deviceMultPkts=_DeviceMultPkts_Object((1,3,6,1,4,1,52,1,2,1,1,49),_DeviceMultPkts_Type())
deviceMultPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMultPkts.setStatus(_A)
_DeviceThdPartyOccupiedSlots_Type=Integer32
_DeviceThdPartyOccupiedSlots_Object=MibScalar
deviceThdPartyOccupiedSlots=_DeviceThdPartyOccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,51),_DeviceThdPartyOccupiedSlots_Type())
deviceThdPartyOccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceThdPartyOccupiedSlots.setStatus(_A)
_DeviceImimOccupiedSlots_Type=Integer32
_DeviceImimOccupiedSlots_Object=MibScalar
deviceImimOccupiedSlots=_DeviceImimOccupiedSlots_Object((1,3,6,1,4,1,52,1,2,1,1,52),_DeviceImimOccupiedSlots_Type())
deviceImimOccupiedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceImimOccupiedSlots.setStatus(_A)
class _DeviceLinkTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_DeviceLinkTraps_Type.__name__=_D
_DeviceLinkTraps_Object=MibScalar
deviceLinkTraps=_DeviceLinkTraps_Object((1,3,6,1,4,1,52,1,2,1,1,54),_DeviceLinkTraps_Type())
deviceLinkTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLinkTraps.setStatus(_A)
class _CtIPDefaultFrameType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethernet',1),('snap8022',2)))
_CtIPDefaultFrameType_Type.__name__=_D
_CtIPDefaultFrameType_Object=MibScalar
ctIPDefaultFrameType=_CtIPDefaultFrameType_Object((1,3,6,1,4,1,52,1,2,1,1,56),_CtIPDefaultFrameType_Type())
ctIPDefaultFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctIPDefaultFrameType.setStatus(_A)
class _DeviceSrcAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipHash',1),('decHash',2)))
_DeviceSrcAddrType_Type.__name__=_D
_DeviceSrcAddrType_Object=MibScalar
deviceSrcAddrType=_DeviceSrcAddrType_Object((1,3,6,1,4,1,52,1,2,1,1,57),_DeviceSrcAddrType_Type())
deviceSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSrcAddrType.setStatus(_A)
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
_RedundancyPollInterval_Type=Integer32
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
_RedundancyRetryCount_Type=Integer32
_RedundancyRetryCount_Object=MibScalar
redundancyRetryCount=_RedundancyRetryCount_Object((1,3,6,1,4,1,52,1,2,1,8,5),_RedundancyRetryCount_Type())
redundancyRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyRetryCount.setStatus(_A)
_RedundancyNumBPs_Type=Integer32
_RedundancyNumBPs_Object=MibScalar
redundancyNumBPs=_RedundancyNumBPs_Object((1,3,6,1,4,1,52,1,2,1,8,6),_RedundancyNumBPs_Type())
redundancyNumBPs.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyNumBPs.setStatus(_A)
_RedundancyCircuitBoard_Type=Integer32
_RedundancyCircuitBoard_Object=MibScalar
redundancyCircuitBoard=_RedundancyCircuitBoard_Object((1,3,6,1,4,1,52,1,2,1,8,7),_RedundancyCircuitBoard_Type())
redundancyCircuitBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyCircuitBoard.setStatus(_A)
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
_RedundancyCircuitMACAddrAdd_Type=IpAddress
_RedundancyCircuitMACAddrAdd_Object=MibScalar
redundancyCircuitMACAddrAdd=_RedundancyCircuitMACAddrAdd_Object((1,3,6,1,4,1,52,1,2,1,8,11),_RedundancyCircuitMACAddrAdd_Type())
redundancyCircuitMACAddrAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyCircuitMACAddrAdd.setStatus(_A)
_RedundancyCircuitMACAddrDel_Type=IpAddress
_RedundancyCircuitMACAddrDel_Object=MibScalar
redundancyCircuitMACAddrDel=_RedundancyCircuitMACAddrDel_Object((1,3,6,1,4,1,52,1,2,1,8,12),_RedundancyCircuitMACAddrDel_Type())
redundancyCircuitMACAddrDel.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyCircuitMACAddrDel.setStatus(_A)
_RedundancyCircuitMACAddrDisp_Type=IpAddress
_RedundancyCircuitMACAddrDisp_Object=MibScalar
redundancyCircuitMACAddrDisp=_RedundancyCircuitMACAddrDisp_Object((1,3,6,1,4,1,52,1,2,1,8,13),_RedundancyCircuitMACAddrDisp_Type())
redundancyCircuitMACAddrDisp.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyCircuitMACAddrDisp.setStatus(_A)
class _RedundancyCircuitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
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
class _DevTrafficEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DevTrafficEnable_Type.__name__=_D
_DevTrafficEnable_Object=MibScalar
devTrafficEnable=_DevTrafficEnable_Object((1,3,6,1,4,1,52,1,2,1,9,1,1,1),_DevTrafficEnable_Type())
devTrafficEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:devTrafficEnable.setStatus(_A)
_DevTrafficThreshold_Type=Integer32
_DevTrafficThreshold_Object=MibScalar
devTrafficThreshold=_DevTrafficThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,1,1,2),_DevTrafficThreshold_Type())
devTrafficThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:devTrafficThreshold.setStatus(_A)
_DevColls_ObjectIdentity=ObjectIdentity
devColls=_DevColls_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1,2))
class _DevCollsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DevCollsEnable_Type.__name__=_D
_DevCollsEnable_Object=MibScalar
devCollsEnable=_DevCollsEnable_Object((1,3,6,1,4,1,52,1,2,1,9,1,2,1),_DevCollsEnable_Type())
devCollsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:devCollsEnable.setStatus(_A)
class _DevCollsThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_DevCollsThreshold_Type.__name__=_D
_DevCollsThreshold_Object=MibScalar
devCollsThreshold=_DevCollsThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,1,2,2),_DevCollsThreshold_Type())
devCollsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:devCollsThreshold.setStatus(_A)
_DevError_ObjectIdentity=ObjectIdentity
devError=_DevError_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1,3))
class _DevErrorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DevErrorEnable_Type.__name__=_D
_DevErrorEnable_Object=MibScalar
devErrorEnable=_DevErrorEnable_Object((1,3,6,1,4,1,52,1,2,1,9,1,3,1),_DevErrorEnable_Type())
devErrorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:devErrorEnable.setStatus(_A)
_DevErrorThreshold_Type=Integer32
_DevErrorThreshold_Object=MibScalar
devErrorThreshold=_DevErrorThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,1,3,2),_DevErrorThreshold_Type())
devErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:devErrorThreshold.setStatus(_A)
_DevErrorSource_Type=Integer32
_DevErrorSource_Object=MibScalar
devErrorSource=_DevErrorSource_Object((1,3,6,1,4,1,52,1,2,1,9,1,3,3),_DevErrorSource_Type())
devErrorSource.setMaxAccess(_C)
if mibBuilder.loadTexts:devErrorSource.setStatus(_A)
_DevBroad_ObjectIdentity=ObjectIdentity
devBroad=_DevBroad_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,1,4))
class _DevBroadEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
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
class _BdTrafficEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BdTrafficEnable_Type.__name__=_D
_BdTrafficEnable_Object=MibScalar
bdTrafficEnable=_BdTrafficEnable_Object((1,3,6,1,4,1,52,1,2,1,9,2,1,1),_BdTrafficEnable_Type())
bdTrafficEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdTrafficEnable.setStatus(_A)
_BdTrafficThreshold_Type=Integer32
_BdTrafficThreshold_Object=MibScalar
bdTrafficThreshold=_BdTrafficThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,2,1,2),_BdTrafficThreshold_Type())
bdTrafficThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdTrafficThreshold.setStatus(_A)
class _BdTrafficBdDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BdTrafficBdDisable_Type.__name__=_D
_BdTrafficBdDisable_Object=MibScalar
bdTrafficBdDisable=_BdTrafficBdDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,1,3),_BdTrafficBdDisable_Type())
bdTrafficBdDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdTrafficBdDisable.setStatus(_A)
_BdColls_ObjectIdentity=ObjectIdentity
bdColls=_BdColls_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2,2))
class _BdCollsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BdCollsEnable_Type.__name__=_D
_BdCollsEnable_Object=MibScalar
bdCollsEnable=_BdCollsEnable_Object((1,3,6,1,4,1,52,1,2,1,9,2,2,1),_BdCollsEnable_Type())
bdCollsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdCollsEnable.setStatus(_A)
class _BdCollsThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_BdCollsThreshold_Type.__name__=_D
_BdCollsThreshold_Object=MibScalar
bdCollsThreshold=_BdCollsThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,2,2,2),_BdCollsThreshold_Type())
bdCollsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdCollsThreshold.setStatus(_A)
class _BdCollsBdDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BdCollsBdDisable_Type.__name__=_D
_BdCollsBdDisable_Object=MibScalar
bdCollsBdDisable=_BdCollsBdDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,2,3),_BdCollsBdDisable_Type())
bdCollsBdDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdCollsBdDisable.setStatus(_A)
_BdError_ObjectIdentity=ObjectIdentity
bdError=_BdError_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2,3))
class _BdErrorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BdErrorEnable_Type.__name__=_D
_BdErrorEnable_Object=MibScalar
bdErrorEnable=_BdErrorEnable_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,1),_BdErrorEnable_Type())
bdErrorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorEnable.setStatus(_A)
_BdErrorThreshold_Type=Integer32
_BdErrorThreshold_Object=MibScalar
bdErrorThreshold=_BdErrorThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,2),_BdErrorThreshold_Type())
bdErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorThreshold.setStatus(_A)
_BdErrorSource_Type=Integer32
_BdErrorSource_Object=MibScalar
bdErrorSource=_BdErrorSource_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,3),_BdErrorSource_Type())
bdErrorSource.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorSource.setStatus(_A)
class _BdErrorBdDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BdErrorBdDisable_Type.__name__=_D
_BdErrorBdDisable_Object=MibScalar
bdErrorBdDisable=_BdErrorBdDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,3,4),_BdErrorBdDisable_Type())
bdErrorBdDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdErrorBdDisable.setStatus(_A)
_BdBroad_ObjectIdentity=ObjectIdentity
bdBroad=_BdBroad_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,2,4))
class _BdBroadEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
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
class _BdBroadDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BdBroadDisable_Type.__name__=_D
_BdBroadDisable_Object=MibScalar
bdBroadDisable=_BdBroadDisable_Object((1,3,6,1,4,1,52,1,2,1,9,2,4,3),_BdBroadDisable_Type())
bdBroadDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:bdBroadDisable.setStatus(_A)
_PortAlrm_ObjectIdentity=ObjectIdentity
portAlrm=_PortAlrm_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3))
_PortTraffic_ObjectIdentity=ObjectIdentity
portTraffic=_PortTraffic_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,1))
class _PortTrafficEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortTrafficEnable_Type.__name__=_D
_PortTrafficEnable_Object=MibScalar
portTrafficEnable=_PortTrafficEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,1,1),_PortTrafficEnable_Type())
portTrafficEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portTrafficEnable.setStatus(_A)
_PortTrafficThreshold_Type=Integer32
_PortTrafficThreshold_Object=MibScalar
portTrafficThreshold=_PortTrafficThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,1,2),_PortTrafficThreshold_Type())
portTrafficThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portTrafficThreshold.setStatus(_A)
class _PortTrafficPortDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortTrafficPortDisable_Type.__name__=_D
_PortTrafficPortDisable_Object=MibScalar
portTrafficPortDisable=_PortTrafficPortDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,1,3),_PortTrafficPortDisable_Type())
portTrafficPortDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portTrafficPortDisable.setStatus(_A)
_PortColls_ObjectIdentity=ObjectIdentity
portColls=_PortColls_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,2))
class _PortCollsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortCollsEnable_Type.__name__=_D
_PortCollsEnable_Object=MibScalar
portCollsEnable=_PortCollsEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,2,1),_PortCollsEnable_Type())
portCollsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portCollsEnable.setStatus(_A)
class _PortCollsThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_PortCollsThreshold_Type.__name__=_D
_PortCollsThreshold_Object=MibScalar
portCollsThreshold=_PortCollsThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,2,2),_PortCollsThreshold_Type())
portCollsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portCollsThreshold.setStatus(_A)
class _PortCollsPortDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortCollsPortDisable_Type.__name__=_D
_PortCollsPortDisable_Object=MibScalar
portCollsPortDisable=_PortCollsPortDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,2,3),_PortCollsPortDisable_Type())
portCollsPortDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portCollsPortDisable.setStatus(_A)
_PortError_ObjectIdentity=ObjectIdentity
portError=_PortError_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,3))
class _PortErrorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortErrorEnable_Type.__name__=_D
_PortErrorEnable_Object=MibScalar
portErrorEnable=_PortErrorEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,1),_PortErrorEnable_Type())
portErrorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorEnable.setStatus(_A)
_PortErrorThreshold_Type=Integer32
_PortErrorThreshold_Object=MibScalar
portErrorThreshold=_PortErrorThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,2),_PortErrorThreshold_Type())
portErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorThreshold.setStatus(_A)
_PortErrorSource_Type=Integer32
_PortErrorSource_Object=MibScalar
portErrorSource=_PortErrorSource_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,3),_PortErrorSource_Type())
portErrorSource.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorSource.setStatus(_A)
class _PortErrorPortDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortErrorPortDisable_Type.__name__=_D
_PortErrorPortDisable_Object=MibScalar
portErrorPortDisable=_PortErrorPortDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,3,4),_PortErrorPortDisable_Type())
portErrorPortDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorPortDisable.setStatus(_A)
_PortBroad_ObjectIdentity=ObjectIdentity
portBroad=_PortBroad_ObjectIdentity((1,3,6,1,4,1,52,1,2,1,9,3,4))
class _PortBroadEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortBroadEnable_Type.__name__=_D
_PortBroadEnable_Object=MibScalar
portBroadEnable=_PortBroadEnable_Object((1,3,6,1,4,1,52,1,2,1,9,3,4,1),_PortBroadEnable_Type())
portBroadEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portBroadEnable.setStatus(_A)
_PortBroadThreshold_Type=Integer32
_PortBroadThreshold_Object=MibScalar
portBroadThreshold=_PortBroadThreshold_Object((1,3,6,1,4,1,52,1,2,1,9,3,4,2),_PortBroadThreshold_Type())
portBroadThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portBroadThreshold.setStatus(_A)
class _PortBroadDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortBroadDisable_Type.__name__=_D
_PortBroadDisable_Object=MibScalar
portBroadDisable=_PortBroadDisable_Object((1,3,6,1,4,1,52,1,2,1,9,3,4,3),_PortBroadDisable_Type())
portBroadDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:portBroadDisable.setStatus(_A)
_DeviceR2_ObjectIdentity=ObjectIdentity
deviceR2=_DeviceR2_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,1))
_TokenRingD_ObjectIdentity=ObjectIdentity
tokenRingD=_TokenRingD_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,1,3))
_DeviceTRPortsOn_Type=Integer32
_DeviceTRPortsOn_Object=MibScalar
deviceTRPortsOn=_DeviceTRPortsOn_Object((1,3,6,1,4,1,52,1,2,2,1,3,1),_DeviceTRPortsOn_Type())
deviceTRPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRPortsOn.setStatus(_A)
_DeviceTRPorts_Type=Integer32
_DeviceTRPorts_Object=MibScalar
deviceTRPorts=_DeviceTRPorts_Object((1,3,6,1,4,1,52,1,2,2,1,3,2),_DeviceTRPorts_Type())
deviceTRPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRPorts.setStatus(_A)
_DeviceTRRingPortsOn_Type=Integer32
_DeviceTRRingPortsOn_Object=MibScalar
deviceTRRingPortsOn=_DeviceTRRingPortsOn_Object((1,3,6,1,4,1,52,1,2,2,1,3,3),_DeviceTRRingPortsOn_Type())
deviceTRRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRRingPortsOn.setStatus(_A)
_DeviceTRRingPorts_Type=Integer32
_DeviceTRRingPorts_Object=MibScalar
deviceTRRingPorts=_DeviceTRRingPorts_Object((1,3,6,1,4,1,52,1,2,2,1,3,4),_DeviceTRRingPorts_Type())
deviceTRRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRRingPorts.setStatus(_A)
_DeviceTRLans_Type=Integer32
_DeviceTRLans_Object=MibScalar
deviceTRLans=_DeviceTRLans_Object((1,3,6,1,4,1,52,1,2,2,1,3,5),_DeviceTRLans_Type())
deviceTRLans.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRLans.setStatus(_A)
_DeviceTRBoards_Type=Integer32
_DeviceTRBoards_Object=MibScalar
deviceTRBoards=_DeviceTRBoards_Object((1,3,6,1,4,1,52,1,2,2,1,3,6),_DeviceTRBoards_Type())
deviceTRBoards.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRBoards.setStatus(_A)
_DeviceTRBoardMap_Type=Integer32
_DeviceTRBoardMap_Object=MibScalar
deviceTRBoardMap=_DeviceTRBoardMap_Object((1,3,6,1,4,1,52,1,2,2,1,3,7),_DeviceTRBoardMap_Type())
deviceTRBoardMap.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTRBoardMap.setStatus(_A)
_NetworkR2_ObjectIdentity=ObjectIdentity
networkR2=_NetworkR2_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,2))
_BoardR2_ObjectIdentity=ObjectIdentity
boardR2=_BoardR2_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3))
_CommonB_ObjectIdentity=ObjectIdentity
commonB=_CommonB_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3,1))
_BoardIndex_Type=Integer32
_BoardIndex_Object=MibScalar
boardIndex=_BoardIndex_Object((1,3,6,1,4,1,52,1,2,2,3,1,1),_BoardIndex_Type())
boardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boardIndex.setStatus(_A)
_BoardName_Type=DisplayString
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
class _BoardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_BoardStatus_Type.__name__=_D
_BoardStatus_Object=MibScalar
boardStatus=_BoardStatus_Object((1,3,6,1,4,1,52,1,2,2,3,1,5),_BoardStatus_Type())
boardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:boardStatus.setStatus(_I)
_BoardPortsOn_Type=Integer32
_BoardPortsOn_Object=MibScalar
boardPortsOn=_BoardPortsOn_Object((1,3,6,1,4,1,52,1,2,2,3,1,6),_BoardPortsOn_Type())
boardPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPortsOn.setStatus(_A)
class _BoardOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_BoardOper_Type.__name__=_D
_BoardOper_Object=MibScalar
boardOper=_BoardOper_Object((1,3,6,1,4,1,52,1,2,2,3,1,7),_BoardOper_Type())
boardOper.setMaxAccess(_B)
if mibBuilder.loadTexts:boardOper.setStatus(_I)
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
_BoardErrorPkts_Type=Counter32
_BoardErrorPkts_Object=MibScalar
boardErrorPkts=_BoardErrorPkts_Object((1,3,6,1,4,1,52,1,2,2,3,2,2),_BoardErrorPkts_Type())
boardErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardErrorPkts.setStatus(_A)
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
_BoardAlignErrs_Type=Counter32
_BoardAlignErrs_Object=MibScalar
boardAlignErrs=_BoardAlignErrs_Object((1,3,6,1,4,1,52,1,2,2,3,2,5),_BoardAlignErrs_Type())
boardAlignErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:boardAlignErrs.setStatus(_A)
_BoardCRCErrs_Type=Counter32
_BoardCRCErrs_Object=MibScalar
boardCRCErrs=_BoardCRCErrs_Object((1,3,6,1,4,1,52,1,2,2,3,2,6),_BoardCRCErrs_Type())
boardCRCErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:boardCRCErrs.setStatus(_A)
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
_BoardOSIFrames_Type=Counter32
_BoardOSIFrames_Object=MibScalar
boardOSIFrames=_BoardOSIFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,12),_BoardOSIFrames_Type())
boardOSIFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardOSIFrames.setStatus(_A)
_BoardNovellFrames_Type=Counter32
_BoardNovellFrames_Object=MibScalar
boardNovellFrames=_BoardNovellFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,13),_BoardNovellFrames_Type())
boardNovellFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardNovellFrames.setStatus(_A)
_BoardBanyanFrames_Type=Counter32
_BoardBanyanFrames_Object=MibScalar
boardBanyanFrames=_BoardBanyanFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,14),_BoardBanyanFrames_Type())
boardBanyanFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardBanyanFrames.setStatus(_A)
_BoardDECNetFrames_Type=Counter32
_BoardDECNetFrames_Object=MibScalar
boardDECNetFrames=_BoardDECNetFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,15),_BoardDECNetFrames_Type())
boardDECNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardDECNetFrames.setStatus(_A)
_BoardXNSFrames_Type=Counter32
_BoardXNSFrames_Object=MibScalar
boardXNSFrames=_BoardXNSFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,16),_BoardXNSFrames_Type())
boardXNSFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardXNSFrames.setStatus(_A)
_BoardIPFrames_Type=Counter32
_BoardIPFrames_Object=MibScalar
boardIPFrames=_BoardIPFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,17),_BoardIPFrames_Type())
boardIPFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardIPFrames.setStatus(_A)
_BoardCtronFrames_Type=Counter32
_BoardCtronFrames_Object=MibScalar
boardCtronFrames=_BoardCtronFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,18),_BoardCtronFrames_Type())
boardCtronFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardCtronFrames.setStatus(_A)
_BoardAppletalkFrames_Type=Counter32
_BoardAppletalkFrames_Object=MibScalar
boardAppletalkFrames=_BoardAppletalkFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,19),_BoardAppletalkFrames_Type())
boardAppletalkFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardAppletalkFrames.setStatus(_A)
_BoardOtherFrames_Type=Counter32
_BoardOtherFrames_Object=MibScalar
boardOtherFrames=_BoardOtherFrames_Object((1,3,6,1,4,1,52,1,2,2,3,2,20),_BoardOtherFrames_Type())
boardOtherFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:boardOtherFrames.setStatus(_A)
_Board64To127Frames_Type=Counter32
_Board64To127Frames_Object=MibScalar
board64To127Frames=_Board64To127Frames_Object((1,3,6,1,4,1,52,1,2,2,3,2,21),_Board64To127Frames_Type())
board64To127Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:board64To127Frames.setStatus(_A)
_Board128To255Frames_Type=Counter32
_Board128To255Frames_Object=MibScalar
board128To255Frames=_Board128To255Frames_Object((1,3,6,1,4,1,52,1,2,2,3,2,22),_Board128To255Frames_Type())
board128To255Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:board128To255Frames.setStatus(_A)
_Board256To511Frames_Type=Counter32
_Board256To511Frames_Object=MibScalar
board256To511Frames=_Board256To511Frames_Object((1,3,6,1,4,1,52,1,2,2,3,2,23),_Board256To511Frames_Type())
board256To511Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:board256To511Frames.setStatus(_A)
_Board512To1023Frames_Type=Counter32
_Board512To1023Frames_Object=MibScalar
board512To1023Frames=_Board512To1023Frames_Object((1,3,6,1,4,1,52,1,2,2,3,2,24),_Board512To1023Frames_Type())
board512To1023Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:board512To1023Frames.setStatus(_A)
_Board1024To1518Frames_Type=Counter32
_Board1024To1518Frames_Object=MibScalar
board1024To1518Frames=_Board1024To1518Frames_Object((1,3,6,1,4,1,52,1,2,2,3,2,25),_Board1024To1518Frames_Type())
board1024To1518Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:board1024To1518Frames.setStatus(_A)
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
class _BoardSrcAddrLocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BoardSrcAddrLocked_Type.__name__=_D
_BoardSrcAddrLocked_Object=MibScalar
boardSrcAddrLocked=_BoardSrcAddrLocked_Object((1,3,6,1,4,1,52,1,2,2,3,2,31),_BoardSrcAddrLocked_Type())
boardSrcAddrLocked.setMaxAccess(_C)
if mibBuilder.loadTexts:boardSrcAddrLocked.setStatus(_A)
_TokenRingB_ObjectIdentity=ObjectIdentity
tokenRingB=_TokenRingB_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3,3))
_BoardTotalRingPorts_Type=Integer32
_BoardTotalRingPorts_Object=MibScalar
boardTotalRingPorts=_BoardTotalRingPorts_Object((1,3,6,1,4,1,52,1,2,2,3,3,1),_BoardTotalRingPorts_Type())
boardTotalRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalRingPorts.setStatus(_A)
_BoardTotalStationPorts_Type=Integer32
_BoardTotalStationPorts_Object=MibScalar
boardTotalStationPorts=_BoardTotalStationPorts_Object((1,3,6,1,4,1,52,1,2,2,3,3,2),_BoardTotalStationPorts_Type())
boardTotalStationPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalStationPorts.setStatus(_A)
class _BoardModeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgmtMode',1),('autoMOde',2)))
_BoardModeStatus_Type.__name__=_D
_BoardModeStatus_Object=MibScalar
boardModeStatus=_BoardModeStatus_Object((1,3,6,1,4,1,52,1,2,2,3,3,3),_BoardModeStatus_Type())
boardModeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:boardModeStatus.setStatus(_A)
_BoardTotalRingPortsOn_Type=Integer32
_BoardTotalRingPortsOn_Object=MibScalar
boardTotalRingPortsOn=_BoardTotalRingPortsOn_Object((1,3,6,1,4,1,52,1,2,2,3,3,4),_BoardTotalRingPortsOn_Type())
boardTotalRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalRingPortsOn.setStatus(_A)
_BoardTotalStationPortsOn_Type=Integer32
_BoardTotalStationPortsOn_Object=MibScalar
boardTotalStationPortsOn=_BoardTotalStationPortsOn_Object((1,3,6,1,4,1,52,1,2,2,3,3,5),_BoardTotalStationPortsOn_Type())
boardTotalStationPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:boardTotalStationPortsOn.setStatus(_A)
class _BoardSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,16)));namedValues=NamedValues(*(('fourMHz',4),('sixteenMhz',16)))
_BoardSpeed_Type.__name__=_D
_BoardSpeed_Object=MibScalar
boardSpeed=_BoardSpeed_Object((1,3,6,1,4,1,52,1,2,2,3,3,6),_BoardSpeed_Type())
boardSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:boardSpeed.setStatus(_A)
class _RingSpeedFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_RingSpeedFault_Type.__name__=_D
_RingSpeedFault_Object=MibScalar
ringSpeedFault=_RingSpeedFault_Object((1,3,6,1,4,1,52,1,2,2,3,3,7),_RingSpeedFault_Type())
ringSpeedFault.setMaxAccess(_B)
if mibBuilder.loadTexts:ringSpeedFault.setStatus(_A)
_BoardSpeedFaultPort_Type=Integer32
_BoardSpeedFaultPort_Object=MibScalar
boardSpeedFaultPort=_BoardSpeedFaultPort_Object((1,3,6,1,4,1,52,1,2,2,3,3,8),_BoardSpeedFaultPort_Type())
boardSpeedFaultPort.setMaxAccess(_B)
if mibBuilder.loadTexts:boardSpeedFaultPort.setStatus(_A)
_BoardFirstRingPort_Type=Integer32
_BoardFirstRingPort_Object=MibScalar
boardFirstRingPort=_BoardFirstRingPort_Object((1,3,6,1,4,1,52,1,2,2,3,3,9),_BoardFirstRingPort_Type())
boardFirstRingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:boardFirstRingPort.setStatus(_A)
class _BoardBypassRingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('illegal',3)))
_BoardBypassRingPortState_Type.__name__=_D
_BoardBypassRingPortState_Object=MibScalar
boardBypassRingPortState=_BoardBypassRingPortState_Object((1,3,6,1,4,1,52,1,2,2,3,3,10),_BoardBypassRingPortState_Type())
boardBypassRingPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:boardBypassRingPortState.setStatus(_A)
_FDDIB_ObjectIdentity=ObjectIdentity
fDDIB=_FDDIB_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,3,4))
_PortR2_ObjectIdentity=ObjectIdentity
portR2=_PortR2_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4))
_CommonP_ObjectIdentity=ObjectIdentity
commonP=_CommonP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,1))
_PortIndex_Type=Integer32
_PortIndex_Object=MibScalar
portIndex=_PortIndex_Object((1,3,6,1,4,1,52,1,2,2,4,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('bnc',1),('aui',2),('tp',3),('tenbt',4),('fot',5),('laser',6),('stp',7),('utp',8),('fo',9),('otherMedia',10)))
_PortMediaType_Type.__name__=_D
_PortMediaType_Object=MibScalar
portMediaType=_PortMediaType_Object((1,3,6,1,4,1,52,1,2,2,4,1,2),_PortMediaType_Type())
portMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:portMediaType.setStatus(_A)
class _PortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PortAdminState_Type.__name__=_D
_PortAdminState_Object=MibScalar
portAdminState=_PortAdminState_Object((1,3,6,1,4,1,52,1,2,2,4,1,3),_PortAdminState_Type())
portAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:portAdminState.setStatus(_A)
_PortSourceAddr_Type=OctetString
_PortSourceAddr_Object=MibScalar
portSourceAddr=_PortSourceAddr_Object((1,3,6,1,4,1,52,1,2,2,4,1,4),_PortSourceAddr_Type())
portSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:portSourceAddr.setStatus(_A)
class _PortOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_N,2)))
_PortOper_Type.__name__=_D
_PortOper_Object=MibScalar
portOper=_PortOper_Object((1,3,6,1,4,1,52,1,2,2,4,1,5),_PortOper_Type())
portOper.setMaxAccess(_B)
if mibBuilder.loadTexts:portOper.setStatus(_A)
_PortActiveUsers_Type=Integer32
_PortActiveUsers_Object=MibScalar
portActiveUsers=_PortActiveUsers_Object((1,3,6,1,4,1,52,1,2,2,4,1,6),_PortActiveUsers_Type())
portActiveUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:portActiveUsers.setStatus(_A)
_PortName_Type=DisplayString
_PortName_Object=MibScalar
portName=_PortName_Object((1,3,6,1,4,1,52,1,2,2,4,1,7),_PortName_Type())
portName.setMaxAccess(_C)
if mibBuilder.loadTexts:portName.setStatus(_A)
_EthernetP_ObjectIdentity=ObjectIdentity
ethernetP=_EthernetP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,2))
class _PortTopologyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stations',1),('trunk',2)))
_PortTopologyType_Type.__name__=_D
_PortTopologyType_Object=MibScalar
portTopologyType=_PortTopologyType_Object((1,3,6,1,4,1,52,1,2,2,4,2,1),_PortTopologyType_Type())
portTopologyType.setMaxAccess(_B)
if mibBuilder.loadTexts:portTopologyType.setStatus(_A)
class _PortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),('linkSignalNotSupported',3)))
_PortLinkStatus_Type.__name__=_D
_PortLinkStatus_Object=MibScalar
portLinkStatus=_PortLinkStatus_Object((1,3,6,1,4,1,52,1,2,2,4,2,2),_PortLinkStatus_Type())
portLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portLinkStatus.setStatus(_A)
class _PortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('segmented',2)))
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
_PortErrorPkts_Type=Counter32
_PortErrorPkts_Object=MibScalar
portErrorPkts=_PortErrorPkts_Object((1,3,6,1,4,1,52,1,2,2,4,2,5),_PortErrorPkts_Type())
portErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portErrorPkts.setStatus(_A)
_PortXmitColls_Type=Counter32
_PortXmitColls_Object=MibScalar
portXmitColls=_PortXmitColls_Object((1,3,6,1,4,1,52,1,2,2,4,2,6),_PortXmitColls_Type())
portXmitColls.setMaxAccess(_B)
if mibBuilder.loadTexts:portXmitColls.setStatus(_A)
_PortRecColls_Type=Counter32
_PortRecColls_Object=MibScalar
portRecColls=_PortRecColls_Object((1,3,6,1,4,1,52,1,2,2,4,2,7),_PortRecColls_Type())
portRecColls.setMaxAccess(_B)
if mibBuilder.loadTexts:portRecColls.setStatus(_A)
_PortAlignErrs_Type=Counter32
_PortAlignErrs_Object=MibScalar
portAlignErrs=_PortAlignErrs_Object((1,3,6,1,4,1,52,1,2,2,4,2,8),_PortAlignErrs_Type())
portAlignErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:portAlignErrs.setStatus(_A)
_PortCRCErrs_Type=Counter32
_PortCRCErrs_Object=MibScalar
portCRCErrs=_PortCRCErrs_Object((1,3,6,1,4,1,52,1,2,2,4,2,9),_PortCRCErrs_Type())
portCRCErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:portCRCErrs.setStatus(_A)
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
_PortNoResorces_Type=Counter32
_PortNoResorces_Object=MibScalar
portNoResorces=_PortNoResorces_Object((1,3,6,1,4,1,52,1,2,2,4,2,12),_PortNoResorces_Type())
portNoResorces.setMaxAccess(_B)
if mibBuilder.loadTexts:portNoResorces.setStatus(_A)
_PortRecBytes_Type=Counter32
_PortRecBytes_Object=MibScalar
portRecBytes=_PortRecBytes_Object((1,3,6,1,4,1,52,1,2,2,4,2,13),_PortRecBytes_Type())
portRecBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:portRecBytes.setStatus(_A)
_PortGiants_Type=Counter32
_PortGiants_Object=MibScalar
portGiants=_PortGiants_Object((1,3,6,1,4,1,52,1,2,2,4,2,14),_PortGiants_Type())
portGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:portGiants.setStatus(_A)
_PortRedundCrt_Type=Integer32
_PortRedundCrt_Object=MibScalar
portRedundCrt=_PortRedundCrt_Object((1,3,6,1,4,1,52,1,2,2,4,2,15),_PortRedundCrt_Type())
portRedundCrt.setMaxAccess(_C)
if mibBuilder.loadTexts:portRedundCrt.setStatus(_A)
class _PortRedundType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('primary',2),('backup',3)))
_PortRedundType_Type.__name__=_D
_PortRedundType_Object=MibScalar
portRedundType=_PortRedundType_Object((1,3,6,1,4,1,52,1,2,2,4,2,16),_PortRedundType_Type())
portRedundType.setMaxAccess(_C)
if mibBuilder.loadTexts:portRedundType.setStatus(_A)
class _PortRedundStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_T,2),('inactive',3)))
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
_PortOSIFrames_Type=Counter32
_PortOSIFrames_Object=MibScalar
portOSIFrames=_PortOSIFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,19),_PortOSIFrames_Type())
portOSIFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portOSIFrames.setStatus(_A)
_PortNovellFrames_Type=Counter32
_PortNovellFrames_Object=MibScalar
portNovellFrames=_PortNovellFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,20),_PortNovellFrames_Type())
portNovellFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portNovellFrames.setStatus(_A)
_PortBanyanFrames_Type=Counter32
_PortBanyanFrames_Object=MibScalar
portBanyanFrames=_PortBanyanFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,21),_PortBanyanFrames_Type())
portBanyanFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portBanyanFrames.setStatus(_A)
_PortDECNetFrames_Type=Counter32
_PortDECNetFrames_Object=MibScalar
portDECNetFrames=_PortDECNetFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,22),_PortDECNetFrames_Type())
portDECNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portDECNetFrames.setStatus(_A)
_PortXNSFrames_Type=Counter32
_PortXNSFrames_Object=MibScalar
portXNSFrames=_PortXNSFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,23),_PortXNSFrames_Type())
portXNSFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portXNSFrames.setStatus(_A)
_PortIPFrames_Type=Counter32
_PortIPFrames_Object=MibScalar
portIPFrames=_PortIPFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,24),_PortIPFrames_Type())
portIPFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portIPFrames.setStatus(_A)
_PortCtronFrames_Type=Counter32
_PortCtronFrames_Object=MibScalar
portCtronFrames=_PortCtronFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,25),_PortCtronFrames_Type())
portCtronFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portCtronFrames.setStatus(_A)
_PortAppletalkFrames_Type=Counter32
_PortAppletalkFrames_Object=MibScalar
portAppletalkFrames=_PortAppletalkFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,26),_PortAppletalkFrames_Type())
portAppletalkFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portAppletalkFrames.setStatus(_A)
_PortOtherFrames_Type=Counter32
_PortOtherFrames_Object=MibScalar
portOtherFrames=_PortOtherFrames_Object((1,3,6,1,4,1,52,1,2,2,4,2,27),_PortOtherFrames_Type())
portOtherFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:portOtherFrames.setStatus(_A)
_Port64To127Frames_Type=Counter32
_Port64To127Frames_Object=MibScalar
port64To127Frames=_Port64To127Frames_Object((1,3,6,1,4,1,52,1,2,2,4,2,28),_Port64To127Frames_Type())
port64To127Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:port64To127Frames.setStatus(_A)
_Port128To255Frames_Type=Counter32
_Port128To255Frames_Object=MibScalar
port128To255Frames=_Port128To255Frames_Object((1,3,6,1,4,1,52,1,2,2,4,2,29),_Port128To255Frames_Type())
port128To255Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:port128To255Frames.setStatus(_A)
_Port256To511Frames_Type=Counter32
_Port256To511Frames_Object=MibScalar
port256To511Frames=_Port256To511Frames_Object((1,3,6,1,4,1,52,1,2,2,4,2,30),_Port256To511Frames_Type())
port256To511Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:port256To511Frames.setStatus(_A)
_Port512To1023Frames_Type=Counter32
_Port512To1023Frames_Object=MibScalar
port512To1023Frames=_Port512To1023Frames_Object((1,3,6,1,4,1,52,1,2,2,4,2,31),_Port512To1023Frames_Type())
port512To1023Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:port512To1023Frames.setStatus(_A)
_Port1024To1518Frames_Type=Counter32
_Port1024To1518Frames_Object=MibScalar
port1024To1518Frames=_Port1024To1518Frames_Object((1,3,6,1,4,1,52,1,2,2,4,2,32),_Port1024To1518Frames_Type())
port1024To1518Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:port1024To1518Frames.setStatus(_A)
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
class _PortSrcAddrLocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_PortSrcAddrLocked_Type.__name__=_D
_PortSrcAddrLocked_Object=MibScalar
portSrcAddrLocked=_PortSrcAddrLocked_Object((1,3,6,1,4,1,52,1,2,2,4,2,38),_PortSrcAddrLocked_Type())
portSrcAddrLocked.setMaxAccess(_C)
if mibBuilder.loadTexts:portSrcAddrLocked.setStatus(_A)
_TokenRingP_ObjectIdentity=ObjectIdentity
tokenRingP=_TokenRingP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3))
_StationP_ObjectIdentity=ObjectIdentity
stationP=_StationP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3,1))
class _StationPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_StationPortLinkStatus_Type.__name__=_D
_StationPortLinkStatus_Object=MibScalar
stationPortLinkStatus=_StationPortLinkStatus_Object((1,3,6,1,4,1,52,1,2,2,4,3,1,1),_StationPortLinkStatus_Type())
stationPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:stationPortLinkStatus.setStatus(_A)
_StationPortLinkStateTime_Type=Integer32
_StationPortLinkStateTime_Object=MibScalar
stationPortLinkStateTime=_StationPortLinkStateTime_Object((1,3,6,1,4,1,52,1,2,2,4,3,1,2),_StationPortLinkStateTime_Type())
stationPortLinkStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:stationPortLinkStateTime.setStatus(_A)
_RingP_ObjectIdentity=ObjectIdentity
ringP=_RingP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3,2))
class _RingPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RingPortLinkStatus_Type.__name__=_D
_RingPortLinkStatus_Object=MibScalar
ringPortLinkStatus=_RingPortLinkStatus_Object((1,3,6,1,4,1,52,1,2,2,4,3,2,1),_RingPortLinkStatus_Type())
ringPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ringPortLinkStatus.setStatus(_V)
_RingPortLinkStateTime_Type=Integer32
_RingPortLinkStateTime_Object=MibScalar
ringPortLinkStateTime=_RingPortLinkStateTime_Object((1,3,6,1,4,1,52,1,2,2,4,3,2,2),_RingPortLinkStateTime_Type())
ringPortLinkStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ringPortLinkStateTime.setStatus(_V)
_RingPort2_ObjectIdentity=ObjectIdentity
ringPort2=_RingPort2_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3,3))
_CommonRP_ObjectIdentity=ObjectIdentity
commonRP=_CommonRP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3,3,1))
class _CommonRPcapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonAutowrap',1),('autowrap',2),('selectable',3)))
_CommonRPcapabilities_Type.__name__=_D
_CommonRPcapabilities_Object=MibScalar
commonRPcapabilities=_CommonRPcapabilities_Object((1,3,6,1,4,1,52,1,2,2,4,3,3,1,1),_CommonRPcapabilities_Type())
commonRPcapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:commonRPcapabilities.setStatus(_A)
_AutowrapRP_ObjectIdentity=ObjectIdentity
autowrapRP=_AutowrapRP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,3,3,2))
class _AutowrapRPFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('faultUndetectable',1),(_P,2),(_Q,3)))
_AutowrapRPFaultStatus_Type.__name__=_D
_AutowrapRPFaultStatus_Object=MibScalar
autowrapRPFaultStatus=_AutowrapRPFaultStatus_Object((1,3,6,1,4,1,52,1,2,2,4,3,3,2,1),_AutowrapRPFaultStatus_Type())
autowrapRPFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:autowrapRPFaultStatus.setStatus(_A)
_AutowrapRPFaultStateTime_Type=Integer32
_AutowrapRPFaultStateTime_Object=MibScalar
autowrapRPFaultStateTime=_AutowrapRPFaultStateTime_Object((1,3,6,1,4,1,52,1,2,2,4,3,3,2,2),_AutowrapRPFaultStateTime_Type())
autowrapRPFaultStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:autowrapRPFaultStateTime.setStatus(_A)
class _AutowrapRPSelectedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unselectable',1),('stp',2),('fo',3)))
_AutowrapRPSelectedType_Type.__name__=_D
_AutowrapRPSelectedType_Object=MibScalar
autowrapRPSelectedType=_AutowrapRPSelectedType_Object((1,3,6,1,4,1,52,1,2,2,4,3,3,2,3),_AutowrapRPSelectedType_Type())
autowrapRPSelectedType.setMaxAccess(_C)
if mibBuilder.loadTexts:autowrapRPSelectedType.setStatus(_A)
class _AutowrapRPPhantomCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noPhantomAvailable',1),('activatePhantom',2),('deactivatePhantom',3)))
_AutowrapRPPhantomCurrent_Type.__name__=_D
_AutowrapRPPhantomCurrent_Object=MibScalar
autowrapRPPhantomCurrent=_AutowrapRPPhantomCurrent_Object((1,3,6,1,4,1,52,1,2,2,4,3,3,2,4),_AutowrapRPPhantomCurrent_Type())
autowrapRPPhantomCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:autowrapRPPhantomCurrent.setStatus(_A)
_FDDIP_ObjectIdentity=ObjectIdentity
fDDIP=_FDDIP_ObjectIdentity((1,3,6,1,4,1,52,1,2,2,4,4))
_FNB_ObjectIdentity=ObjectIdentity
fNB=_FNB_ObjectIdentity((1,3,6,1,4,1,52,1,6,1,1))
class _ConnectedLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_ConnectedLeft_Type.__name__=_D
_ConnectedLeft_Object=MibScalar
connectedLeft=_ConnectedLeft_Object((1,3,6,1,4,1,52,1,6,1,1,1),_ConnectedLeft_Type())
connectedLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:connectedLeft.setStatus(_A)
class _ConnectedRight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_ConnectedRight_Type.__name__=_D
_ConnectedRight_Object=MibScalar
connectedRight=_ConnectedRight_Object((1,3,6,1,4,1,52,1,6,1,1,2),_ConnectedRight_Type())
connectedRight.setMaxAccess(_C)
if mibBuilder.loadTexts:connectedRight.setStatus(_A)
class _BoardBypassState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BoardBypassState_Type.__name__=_D
_BoardBypassState_Object=MibScalar
boardBypassState=_BoardBypassState_Object((1,3,6,1,4,1,52,1,6,1,1,3),_BoardBypassState_Type())
boardBypassState.setMaxAccess(_C)
if mibBuilder.loadTexts:boardBypassState.setStatus(_A)
mibBuilder.exportSymbols('IRM3-MIB',**{'device':device,'deviceMMACType':deviceMMACType,'deviceSlots':deviceSlots,'deviceOccupiedSlots':deviceOccupiedSlots,'devicePortsOn':devicePortsOn,'deviceTotalPorts':deviceTotalPorts,'deviceTotalPkts':deviceTotalPkts,'deviceTotalErrors':deviceTotalErrors,'deviceTransmitColls':deviceTransmitColls,'deviceRecColls':deviceRecColls,'deviceAlignErrs':deviceAlignErrs,'deviceCRCErrs':deviceCRCErrs,'deviceRunts':deviceRunts,'deviceOOWColls':deviceOOWColls,'deviceNoResources':deviceNoResources,'deviceRecBytes':deviceRecBytes,'deviceGiantFrames':deviceGiantFrames,'deviceRestart':deviceRestart,'deviceResetCounters':deviceResetCounters,'deviceRedundantCts':deviceRedundantCts,'deviceDiscover':deviceDiscover,'deviceTimeBase':deviceTimeBase,'deviceResetRedundancy':deviceResetRedundancy,'deviceSrcAddrAgingTime':deviceSrcAddrAgingTime,'deviceSrcAddrTraps':deviceSrcAddrTraps,'deviceSrcAddrLocked':deviceSrcAddrLocked,'deviceEtherOccupiedSlots':deviceEtherOccupiedSlots,'deviceTROccupiedSlots':deviceTROccupiedSlots,'deviceFDDIOccupiedSlots':deviceFDDIOccupiedSlots,'deviceRestoreDefaults':deviceRestoreDefaults,'deviceActiveUsers':deviceActiveUsers,'deviceOSIFrames':deviceOSIFrames,'deviceNovellFrames':deviceNovellFrames,'deviceBanyanFrames':deviceBanyanFrames,'deviceDECNetFrames':deviceDECNetFrames,'deviceXNSFrames':deviceXNSFrames,'deviceIPFrames':deviceIPFrames,'deviceCtronFrames':deviceCtronFrames,'deviceAppletalkFrames':deviceAppletalkFrames,'deviceOtherFrames':deviceOtherFrames,'device64To127Frames':device64To127Frames,'device128To255Frames':device128To255Frames,'device256To511Frames':device256To511Frames,'device512To1023Frames':device512To1023Frames,'device1024To1518Frames':device1024To1518Frames,'deviceBroadPkts':deviceBroadPkts,'deviceMultPkts':deviceMultPkts,'deviceThdPartyOccupiedSlots':deviceThdPartyOccupiedSlots,'deviceImimOccupiedSlots':deviceImimOccupiedSlots,'deviceLinkTraps':deviceLinkTraps,'ctIPDefaultFrameType':ctIPDefaultFrameType,'deviceSrcAddrType':deviceSrcAddrType,'board':board,'port':port,'sourceAddr':sourceAddr,'sourceAddrBoard':sourceAddrBoard,'sourceAddrPort':sourceAddrPort,'redundancy':redundancy,'redundancyPollInterval':redundancyPollInterval,'redundancyTestTod':redundancyTestTod,'redundancyPerformTest':redundancyPerformTest,'redundancyCircuitName':redundancyCircuitName,'redundancyRetryCount':redundancyRetryCount,'redundancyNumBPs':redundancyNumBPs,'redundancyCircuitBoard':redundancyCircuitBoard,'redundancyCircuitPort':redundancyCircuitPort,'redundancyCircuitTypes':redundancyCircuitTypes,'redundancyCircuitNumAddr':redundancyCircuitNumAddr,'redundancyCircuitMACAddrAdd':redundancyCircuitMACAddrAdd,'redundancyCircuitMACAddrDel':redundancyCircuitMACAddrDel,'redundancyCircuitMACAddrDisp':redundancyCircuitMACAddrDisp,'redundancyCircuitEnable':redundancyCircuitEnable,'redundancyCircuitReset':redundancyCircuitReset,'alarm':alarm,'devAlrm':devAlrm,'devTraffic':devTraffic,'devTrafficEnable':devTrafficEnable,'devTrafficThreshold':devTrafficThreshold,'devColls':devColls,'devCollsEnable':devCollsEnable,'devCollsThreshold':devCollsThreshold,'devError':devError,'devErrorEnable':devErrorEnable,'devErrorThreshold':devErrorThreshold,'devErrorSource':devErrorSource,'devBroad':devBroad,'devBroadEnable':devBroadEnable,'devBroadThreshold':devBroadThreshold,'bdAlrm':bdAlrm,'bdTraffic':bdTraffic,'bdTrafficEnable':bdTrafficEnable,'bdTrafficThreshold':bdTrafficThreshold,'bdTrafficBdDisable':bdTrafficBdDisable,'bdColls':bdColls,'bdCollsEnable':bdCollsEnable,'bdCollsThreshold':bdCollsThreshold,'bdCollsBdDisable':bdCollsBdDisable,'bdError':bdError,'bdErrorEnable':bdErrorEnable,'bdErrorThreshold':bdErrorThreshold,'bdErrorSource':bdErrorSource,'bdErrorBdDisable':bdErrorBdDisable,'bdBroad':bdBroad,'bdBroadEnable':bdBroadEnable,'bdBroadThreshold':bdBroadThreshold,'bdBroadDisable':bdBroadDisable,'portAlrm':portAlrm,'portTraffic':portTraffic,'portTrafficEnable':portTrafficEnable,'portTrafficThreshold':portTrafficThreshold,'portTrafficPortDisable':portTrafficPortDisable,'portColls':portColls,'portCollsEnable':portCollsEnable,'portCollsThreshold':portCollsThreshold,'portCollsPortDisable':portCollsPortDisable,'portError':portError,'portErrorEnable':portErrorEnable,'portErrorThreshold':portErrorThreshold,'portErrorSource':portErrorSource,'portErrorPortDisable':portErrorPortDisable,'portBroad':portBroad,'portBroadEnable':portBroadEnable,'portBroadThreshold':portBroadThreshold,'portBroadDisable':portBroadDisable,'deviceR2':deviceR2,'tokenRingD':tokenRingD,'deviceTRPortsOn':deviceTRPortsOn,'deviceTRPorts':deviceTRPorts,'deviceTRRingPortsOn':deviceTRRingPortsOn,'deviceTRRingPorts':deviceTRRingPorts,'deviceTRLans':deviceTRLans,'deviceTRBoards':deviceTRBoards,'deviceTRBoardMap':deviceTRBoardMap,'networkR2':networkR2,'boardR2':boardR2,'commonB':commonB,'boardIndex':boardIndex,'boardName':boardName,'boardType':boardType,'boardTotalPorts':boardTotalPorts,'boardStatus':boardStatus,'boardPortsOn':boardPortsOn,'boardOper':boardOper,'boardActiveUsers':boardActiveUsers,'ethernetB':ethernetB,'boardTotalPkts':boardTotalPkts,'boardErrorPkts':boardErrorPkts,'boardTransColls':boardTransColls,'boardRecColls':boardRecColls,'boardAlignErrs':boardAlignErrs,'boardCRCErrs':boardCRCErrs,'boardRunts':boardRunts,'boardOOWColls':boardOOWColls,'boardNoResources':boardNoResources,'boardRecBytes':boardRecBytes,'boardGiants':boardGiants,'boardOSIFrames':boardOSIFrames,'boardNovellFrames':boardNovellFrames,'boardBanyanFrames':boardBanyanFrames,'boardDECNetFrames':boardDECNetFrames,'boardXNSFrames':boardXNSFrames,'boardIPFrames':boardIPFrames,'boardCtronFrames':boardCtronFrames,'boardAppletalkFrames':boardAppletalkFrames,'boardOtherFrames':boardOtherFrames,'board64To127Frames':board64To127Frames,'board128To255Frames':board128To255Frames,'board256To511Frames':board256To511Frames,'board512To1023Frames':board512To1023Frames,'board1024To1518Frames':board1024To1518Frames,'boardBroadPkts':boardBroadPkts,'boardMultPkts':boardMultPkts,'boardSrcAddrLocked':boardSrcAddrLocked,'tokenRingB':tokenRingB,'boardTotalRingPorts':boardTotalRingPorts,'boardTotalStationPorts':boardTotalStationPorts,'boardModeStatus':boardModeStatus,'boardTotalRingPortsOn':boardTotalRingPortsOn,'boardTotalStationPortsOn':boardTotalStationPortsOn,'boardSpeed':boardSpeed,'ringSpeedFault':ringSpeedFault,'boardSpeedFaultPort':boardSpeedFaultPort,'boardFirstRingPort':boardFirstRingPort,'boardBypassRingPortState':boardBypassRingPortState,'fDDIB':fDDIB,'portR2':portR2,'commonP':commonP,'portIndex':portIndex,'portMediaType':portMediaType,'portAdminState':portAdminState,'portSourceAddr':portSourceAddr,'portOper':portOper,'portActiveUsers':portActiveUsers,'portName':portName,'ethernetP':ethernetP,'portTopologyType':portTopologyType,'portLinkStatus':portLinkStatus,'portStatus':portStatus,'portTotalPkts':portTotalPkts,'portErrorPkts':portErrorPkts,'portXmitColls':portXmitColls,'portRecColls':portRecColls,'portAlignErrs':portAlignErrs,'portCRCErrs':portCRCErrs,'portRunts':portRunts,'portOOWColls':portOOWColls,'portNoResorces':portNoResorces,'portRecBytes':portRecBytes,'portGiants':portGiants,'portRedundCrt':portRedundCrt,'portRedundType':portRedundType,'portRedundStatus':portRedundStatus,'portForceTrunkType':portForceTrunkType,'portOSIFrames':portOSIFrames,'portNovellFrames':portNovellFrames,'portBanyanFrames':portBanyanFrames,'portDECNetFrames':portDECNetFrames,'portXNSFrames':portXNSFrames,'portIPFrames':portIPFrames,'portCtronFrames':portCtronFrames,'portAppletalkFrames':portAppletalkFrames,'portOtherFrames':portOtherFrames,'port64To127Frames':port64To127Frames,'port128To255Frames':port128To255Frames,'port256To511Frames':port256To511Frames,'port512To1023Frames':port512To1023Frames,'port1024To1518Frames':port1024To1518Frames,'portBroadPkts':portBroadPkts,'portMultPkts':portMultPkts,'portSrcAddrLocked':portSrcAddrLocked,'tokenRingP':tokenRingP,'stationP':stationP,'stationPortLinkStatus':stationPortLinkStatus,'stationPortLinkStateTime':stationPortLinkStateTime,'ringP':ringP,'ringPortLinkStatus':ringPortLinkStatus,'ringPortLinkStateTime':ringPortLinkStateTime,'ringPort2':ringPort2,'commonRP':commonRP,'commonRPcapabilities':commonRPcapabilities,'autowrapRP':autowrapRP,'autowrapRPFaultStatus':autowrapRPFaultStatus,'autowrapRPFaultStateTime':autowrapRPFaultStateTime,'autowrapRPSelectedType':autowrapRPSelectedType,'autowrapRPPhantomCurrent':autowrapRPPhantomCurrent,'fDDIP':fDDIP,'fNB':fNB,'connectedLeft':connectedLeft,'connectedRight':connectedRight,'boardBypassState':boardBypassState})