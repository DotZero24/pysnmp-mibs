_y='whiteRabbit'
_x='enabled'
_w='uncalibrated'
_v='passive'
_u='preMaster'
_t='listening'
_s='faulty'
_r='initializing'
_q='wrsPtpInstanceOnPortIndex'
_p='wrsPtpInstancePortIndex'
_o='wrsPstatsHCIndex'
_n='disable'
_m='enable'
_l='wrsPortStatusIndex'
_k='l1Sync'
_j='obsolete'
_i='unknown'
_h='wrsPtpDataIndex'
_g='wrsPstatsIndex'
_f='locked'
_e='startMain'
_d='grandmaster'
_c='wrsDiskIndex'
_b='fileNotFound'
_a='remote'
_Z='dhcpError'
_Y='statusFileMissing'
_X='downloadError'
_W='local'
_V='unknownStatus'
_U='none'
_T='failed'
_S='slave'
_R='master'
_Q='firstRead'
_P='OctetString'
_O='not-accessible'
_N='bug'
_M='WR-SWITCH-MIB'
_L='errorMinor'
_K='disabled'
_J='warning'
_I='warningNA'
_H='ok'
_G='error'
_F='DisplayString'
_E='deprecated'
_D='na'
_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
wrSwitchMIB=ModuleIdentity((1,3,6,1,4,1,96,100))
if mibBuilder.loadTexts:wrSwitchMIB.setRevisions(('2023-03-26 00:00','2021-08-31 00:00','2020-05-22 00:00','2018-07-18 14:00','2016-02-17 16:00','2015-08-12 12:00'))
_Cern_ObjectIdentity=ObjectIdentity
cern=_Cern_ObjectIdentity((1,3,6,1,4,1,96))
_WrsScalar_ObjectIdentity=ObjectIdentity
wrsScalar=_WrsScalar_ObjectIdentity((1,3,6,1,4,1,96,100,1))
_WrsScalarOne_Type=Integer32
_WrsScalarOne_Object=MibScalar
wrsScalarOne=_WrsScalarOne_Object((1,3,6,1,4,1,96,100,1,1),_WrsScalarOne_Type())
wrsScalarOne.setMaxAccess('read-write')
if mibBuilder.loadTexts:wrsScalarOne.setStatus(_B)
_WrsStatus_ObjectIdentity=ObjectIdentity
wrsStatus=_WrsStatus_ObjectIdentity((1,3,6,1,4,1,96,100,6))
_WrsGeneralStatusGroup_ObjectIdentity=ObjectIdentity
wrsGeneralStatusGroup=_WrsGeneralStatusGroup_ObjectIdentity((1,3,6,1,4,1,96,100,6,1))
class _WrsMainSystemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4),(_N,5)))
_WrsMainSystemStatus_Type.__name__=_C
_WrsMainSystemStatus_Object=MibScalar
wrsMainSystemStatus=_WrsMainSystemStatus_Object((1,3,6,1,4,1,96,100,6,1,1),_WrsMainSystemStatus_Type())
wrsMainSystemStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsMainSystemStatus.setStatus(_B)
class _WrsOSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4),(_N,5)))
_WrsOSStatus_Type.__name__=_C
_WrsOSStatus_Object=MibScalar
wrsOSStatus=_WrsOSStatus_Object((1,3,6,1,4,1,96,100,6,1,2),_WrsOSStatus_Type())
wrsOSStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsOSStatus.setStatus(_B)
class _WrsTimingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4),(_N,5)))
_WrsTimingStatus_Type.__name__=_C
_WrsTimingStatus_Object=MibScalar
wrsTimingStatus=_WrsTimingStatus_Object((1,3,6,1,4,1,96,100,6,1,3),_WrsTimingStatus_Type())
wrsTimingStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTimingStatus.setStatus(_B)
class _WrsNetworkingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4),(_N,5)))
_WrsNetworkingStatus_Type.__name__=_C
_WrsNetworkingStatus_Object=MibScalar
wrsNetworkingStatus=_WrsNetworkingStatus_Object((1,3,6,1,4,1,96,100,6,1,4),_WrsNetworkingStatus_Type())
wrsNetworkingStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsNetworkingStatus.setStatus(_B)
_WrsDetailedStatusesGroup_ObjectIdentity=ObjectIdentity
wrsDetailedStatusesGroup=_WrsDetailedStatusesGroup_ObjectIdentity((1,3,6,1,4,1,96,100,6,2))
_WrsOSStatusGroup_ObjectIdentity=ObjectIdentity
wrsOSStatusGroup=_WrsOSStatusGroup_ObjectIdentity((1,3,6,1,4,1,96,100,6,2,1))
class _WrsBootSuccessful_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4),(_N,5)))
_WrsBootSuccessful_Type.__name__=_C
_WrsBootSuccessful_Object=MibScalar
wrsBootSuccessful=_WrsBootSuccessful_Object((1,3,6,1,4,1,96,100,6,2,1,1),_WrsBootSuccessful_Type())
wrsBootSuccessful.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootSuccessful.setStatus(_B)
class _WrsTemperatureWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('thresholdNotSet',1),('temperatureOK',2),('temperatureTooHigh',3)))
_WrsTemperatureWarning_Type.__name__=_C
_WrsTemperatureWarning_Object=MibScalar
wrsTemperatureWarning=_WrsTemperatureWarning_Object((1,3,6,1,4,1,96,100,6,2,1,2),_WrsTemperatureWarning_Type())
wrsTemperatureWarning.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTemperatureWarning.setStatus(_B)
class _WrsMemoryFreeLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4)))
_WrsMemoryFreeLow_Type.__name__=_C
_WrsMemoryFreeLow_Object=MibScalar
wrsMemoryFreeLow=_WrsMemoryFreeLow_Object((1,3,6,1,4,1,96,100,6,2,1,3),_WrsMemoryFreeLow_Type())
wrsMemoryFreeLow.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsMemoryFreeLow.setStatus(_B)
class _WrsCpuLoadHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3)))
_WrsCpuLoadHigh_Type.__name__=_C
_WrsCpuLoadHigh_Object=MibScalar
wrsCpuLoadHigh=_WrsCpuLoadHigh_Object((1,3,6,1,4,1,96,100,6,2,1,4),_WrsCpuLoadHigh_Type())
wrsCpuLoadHigh.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsCpuLoadHigh.setStatus(_B)
class _WrsDiskSpaceLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4)))
_WrsDiskSpaceLow_Type.__name__=_C
_WrsDiskSpaceLow_Object=MibScalar
wrsDiskSpaceLow=_WrsDiskSpaceLow_Object((1,3,6,1,4,1,96,100,6,2,1,5),_WrsDiskSpaceLow_Type())
wrsDiskSpaceLow.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDiskSpaceLow.setStatus(_B)
_WrsTimingStatusGroup_ObjectIdentity=ObjectIdentity
wrsTimingStatusGroup=_WrsTimingStatusGroup_ObjectIdentity((1,3,6,1,4,1,96,100,6,2,2))
class _WrsPTPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,6)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_Q,6)))
_WrsPTPStatus_Type.__name__=_C
_WrsPTPStatus_Object=MibScalar
wrsPTPStatus=_WrsPTPStatus_Object((1,3,6,1,4,1,96,100,6,2,2,1),_WrsPTPStatus_Type())
wrsPTPStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPTPStatus.setStatus(_B)
class _WrsSoftPLLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4),(_N,5)))
_WrsSoftPLLStatus_Type.__name__=_C
_WrsSoftPLLStatus_Object=MibScalar
wrsSoftPLLStatus=_WrsSoftPLLStatus_Object((1,3,6,1,4,1,96,100,6,2,2,2),_WrsSoftPLLStatus_Type())
wrsSoftPLLStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSoftPLLStatus.setStatus(_B)
class _WrsSlaveLinksStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_I,4)))
_WrsSlaveLinksStatus_Type.__name__=_C
_WrsSlaveLinksStatus_Object=MibScalar
wrsSlaveLinksStatus=_WrsSlaveLinksStatus_Object((1,3,6,1,4,1,96,100,6,2,2,3),_WrsSlaveLinksStatus_Type())
wrsSlaveLinksStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSlaveLinksStatus.setStatus(_B)
class _WrsPTPFramesFlowing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_I,4),(_Q,6)))
_WrsPTPFramesFlowing_Type.__name__=_C
_WrsPTPFramesFlowing_Object=MibScalar
wrsPTPFramesFlowing=_WrsPTPFramesFlowing_Object((1,3,6,1,4,1,96,100,6,2,2,4),_WrsPTPFramesFlowing_Type())
wrsPTPFramesFlowing.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPTPFramesFlowing.setStatus(_B)
class _WrsSystemClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4)))
_WrsSystemClockStatus_Type.__name__=_C
_WrsSystemClockStatus_Object=MibScalar
wrsSystemClockStatus=_WrsSystemClockStatus_Object((1,3,6,1,4,1,96,100,6,2,2,5),_WrsSystemClockStatus_Type())
wrsSystemClockStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSystemClockStatus.setStatus(_B)
_WrsNetworkingStatusGroup_ObjectIdentity=ObjectIdentity
wrsNetworkingStatusGroup=_WrsNetworkingStatusGroup_ObjectIdentity((1,3,6,1,4,1,96,100,6,2,3))
class _WrsSFPsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_J,3),(_I,4),(_N,5)))
_WrsSFPsStatus_Type.__name__=_C
_WrsSFPsStatus_Object=MibScalar
wrsSFPsStatus=_WrsSFPsStatus_Object((1,3,6,1,4,1,96,100,6,2,3,1),_WrsSFPsStatus_Type())
wrsSFPsStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSFPsStatus.setStatus(_B)
class _WrsEndpointStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,6)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_Q,6)))
_WrsEndpointStatus_Type.__name__=_C
_WrsEndpointStatus_Object=MibScalar
wrsEndpointStatus=_WrsEndpointStatus_Object((1,3,6,1,4,1,96,100,6,2,3,2),_WrsEndpointStatus_Type())
wrsEndpointStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsEndpointStatus.setStatus(_B)
class _WrsSwcoreStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,6)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_Q,6)))
_WrsSwcoreStatus_Type.__name__=_C
_WrsSwcoreStatus_Object=MibScalar
wrsSwcoreStatus=_WrsSwcoreStatus_Object((1,3,6,1,4,1,96,100,6,2,3,3),_WrsSwcoreStatus_Type())
wrsSwcoreStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSwcoreStatus.setStatus(_B)
class _WrsRTUStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,6)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_Q,6)))
_WrsRTUStatus_Type.__name__=_C
_WrsRTUStatus_Object=MibScalar
wrsRTUStatus=_WrsRTUStatus_Object((1,3,6,1,4,1,96,100,6,2,3,4),_WrsRTUStatus_Type())
wrsRTUStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsRTUStatus.setStatus(_B)
_WrsVersionGroup_ObjectIdentity=ObjectIdentity
wrsVersionGroup=_WrsVersionGroup_ObjectIdentity((1,3,6,1,4,1,96,100,6,3))
class _WrsVersionSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionSwVersion_Type.__name__=_F
_WrsVersionSwVersion_Object=MibScalar
wrsVersionSwVersion=_WrsVersionSwVersion_Object((1,3,6,1,4,1,96,100,6,3,1),_WrsVersionSwVersion_Type())
wrsVersionSwVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionSwVersion.setStatus(_B)
class _WrsVersionSwBuildBy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionSwBuildBy_Type.__name__=_F
_WrsVersionSwBuildBy_Object=MibScalar
wrsVersionSwBuildBy=_WrsVersionSwBuildBy_Object((1,3,6,1,4,1,96,100,6,3,2),_WrsVersionSwBuildBy_Type())
wrsVersionSwBuildBy.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionSwBuildBy.setStatus(_B)
class _WrsVersionSwBuildDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionSwBuildDate_Type.__name__=_F
_WrsVersionSwBuildDate_Object=MibScalar
wrsVersionSwBuildDate=_WrsVersionSwBuildDate_Object((1,3,6,1,4,1,96,100,6,3,3),_WrsVersionSwBuildDate_Type())
wrsVersionSwBuildDate.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionSwBuildDate.setStatus(_B)
class _WrsVersionBackplaneVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionBackplaneVersion_Type.__name__=_F
_WrsVersionBackplaneVersion_Object=MibScalar
wrsVersionBackplaneVersion=_WrsVersionBackplaneVersion_Object((1,3,6,1,4,1,96,100,6,3,4),_WrsVersionBackplaneVersion_Type())
wrsVersionBackplaneVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionBackplaneVersion.setStatus(_B)
class _WrsVersionFpgaType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionFpgaType_Type.__name__=_F
_WrsVersionFpgaType_Object=MibScalar
wrsVersionFpgaType=_WrsVersionFpgaType_Object((1,3,6,1,4,1,96,100,6,3,5),_WrsVersionFpgaType_Type())
wrsVersionFpgaType.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionFpgaType.setStatus(_B)
class _WrsVersionManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionManufacturer_Type.__name__=_F
_WrsVersionManufacturer_Object=MibScalar
wrsVersionManufacturer=_WrsVersionManufacturer_Object((1,3,6,1,4,1,96,100,6,3,6),_WrsVersionManufacturer_Type())
wrsVersionManufacturer.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionManufacturer.setStatus(_B)
class _WrsVersionSwitchSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionSwitchSerialNumber_Type.__name__=_F
_WrsVersionSwitchSerialNumber_Object=MibScalar
wrsVersionSwitchSerialNumber=_WrsVersionSwitchSerialNumber_Object((1,3,6,1,4,1,96,100,6,3,7),_WrsVersionSwitchSerialNumber_Type())
wrsVersionSwitchSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionSwitchSerialNumber.setStatus(_B)
class _WrsVersionScbVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionScbVersion_Type.__name__=_F
_WrsVersionScbVersion_Object=MibScalar
wrsVersionScbVersion=_WrsVersionScbVersion_Object((1,3,6,1,4,1,96,100,6,3,8),_WrsVersionScbVersion_Type())
wrsVersionScbVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionScbVersion.setStatus(_B)
class _WrsVersionGwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionGwVersion_Type.__name__=_F
_WrsVersionGwVersion_Object=MibScalar
wrsVersionGwVersion=_WrsVersionGwVersion_Object((1,3,6,1,4,1,96,100,6,3,9),_WrsVersionGwVersion_Type())
wrsVersionGwVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionGwVersion.setStatus(_B)
class _WrsVersionGwBuild_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionGwBuild_Type.__name__=_F
_WrsVersionGwBuild_Object=MibScalar
wrsVersionGwBuild=_WrsVersionGwBuild_Object((1,3,6,1,4,1,96,100,6,3,10),_WrsVersionGwBuild_Type())
wrsVersionGwBuild.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionGwBuild.setStatus(_B)
class _WrsVersionSwitchHdlCommitId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionSwitchHdlCommitId_Type.__name__=_F
_WrsVersionSwitchHdlCommitId_Object=MibScalar
wrsVersionSwitchHdlCommitId=_WrsVersionSwitchHdlCommitId_Object((1,3,6,1,4,1,96,100,6,3,11),_WrsVersionSwitchHdlCommitId_Type())
wrsVersionSwitchHdlCommitId.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionSwitchHdlCommitId.setStatus(_B)
class _WrsVersionGeneralCoresCommitId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionGeneralCoresCommitId_Type.__name__=_F
_WrsVersionGeneralCoresCommitId_Object=MibScalar
wrsVersionGeneralCoresCommitId=_WrsVersionGeneralCoresCommitId_Object((1,3,6,1,4,1,96,100,6,3,12),_WrsVersionGeneralCoresCommitId_Type())
wrsVersionGeneralCoresCommitId.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionGeneralCoresCommitId.setStatus(_B)
class _WrsVersionWrCoresCommitId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionWrCoresCommitId_Type.__name__=_F
_WrsVersionWrCoresCommitId_Object=MibScalar
wrsVersionWrCoresCommitId=_WrsVersionWrCoresCommitId_Object((1,3,6,1,4,1,96,100,6,3,13),_WrsVersionWrCoresCommitId_Type())
wrsVersionWrCoresCommitId.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionWrCoresCommitId.setStatus(_B)
class _WrsVersionLastUpdateDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsVersionLastUpdateDate_Type.__name__=_F
_WrsVersionLastUpdateDate_Object=MibScalar
wrsVersionLastUpdateDate=_WrsVersionLastUpdateDate_Object((1,3,6,1,4,1,96,100,6,3,14),_WrsVersionLastUpdateDate_Type())
wrsVersionLastUpdateDate.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionLastUpdateDate.setStatus(_B)
_WrsVersionFeatures_Type=DisplayString
_WrsVersionFeatures_Object=MibScalar
wrsVersionFeatures=_WrsVersionFeatures_Object((1,3,6,1,4,1,96,100,6,3,15),_WrsVersionFeatures_Type())
wrsVersionFeatures.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVersionFeatures.setStatus(_B)
_WrsExpertStatus_ObjectIdentity=ObjectIdentity
wrsExpertStatus=_WrsExpertStatus_ObjectIdentity((1,3,6,1,4,1,96,100,7))
_WrsOperationStatus_ObjectIdentity=ObjectIdentity
wrsOperationStatus=_WrsOperationStatus_ObjectIdentity((1,3,6,1,4,1,96,100,7,1))
_WrsCurrentTimeGroup_ObjectIdentity=ObjectIdentity
wrsCurrentTimeGroup=_WrsCurrentTimeGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,1,1))
_WrsDateTAI_Type=Counter64
_WrsDateTAI_Object=MibScalar
wrsDateTAI=_WrsDateTAI_Object((1,3,6,1,4,1,96,100,7,1,1,1),_WrsDateTAI_Type())
wrsDateTAI.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDateTAI.setStatus(_B)
class _WrsDateTAIString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsDateTAIString_Type.__name__=_F
_WrsDateTAIString_Object=MibScalar
wrsDateTAIString=_WrsDateTAIString_Object((1,3,6,1,4,1,96,100,7,1,1,2),_WrsDateTAIString_Type())
wrsDateTAIString.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDateTAIString.setStatus(_B)
class _WrsSystemClockStatusDetails_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_D,0),(_H,1),('thresholdExceeded',2),('ntpError',3),(_G,4),('ioError',5),(_V,6)))
_WrsSystemClockStatusDetails_Type.__name__=_C
_WrsSystemClockStatusDetails_Object=MibScalar
wrsSystemClockStatusDetails=_WrsSystemClockStatusDetails_Object((1,3,6,1,4,1,96,100,7,1,1,3),_WrsSystemClockStatusDetails_Type())
wrsSystemClockStatusDetails.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSystemClockStatusDetails.setStatus(_B)
_WrsSystemClockDrift_Type=Integer32
_WrsSystemClockDrift_Object=MibScalar
wrsSystemClockDrift=_WrsSystemClockDrift_Object((1,3,6,1,4,1,96,100,7,1,1,4),_WrsSystemClockDrift_Type())
wrsSystemClockDrift.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSystemClockDrift.setStatus(_B)
_WrsSystemClockDriftThreshold_Type=Integer32
_WrsSystemClockDriftThreshold_Object=MibScalar
wrsSystemClockDriftThreshold=_WrsSystemClockDriftThreshold_Object((1,3,6,1,4,1,96,100,7,1,1,5),_WrsSystemClockDriftThreshold_Type())
wrsSystemClockDriftThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSystemClockDriftThreshold.setStatus(_B)
_WrsSystemClockCheckInterval_Type=Integer32
_WrsSystemClockCheckInterval_Object=MibScalar
wrsSystemClockCheckInterval=_WrsSystemClockCheckInterval_Object((1,3,6,1,4,1,96,100,7,1,1,6),_WrsSystemClockCheckInterval_Type())
wrsSystemClockCheckInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSystemClockCheckInterval.setStatus(_B)
class _WrsSystemClockCheckIntervalUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_G,1),('minutes',2),('hours',3),('days',4)))
_WrsSystemClockCheckIntervalUnit_Type.__name__=_C
_WrsSystemClockCheckIntervalUnit_Object=MibScalar
wrsSystemClockCheckIntervalUnit=_WrsSystemClockCheckIntervalUnit_Object((1,3,6,1,4,1,96,100,7,1,1,7),_WrsSystemClockCheckIntervalUnit_Type())
wrsSystemClockCheckIntervalUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSystemClockCheckIntervalUnit.setStatus(_B)
class _WrsLeapSecSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_G,1),(_L,2),(_W,3),('tryRemote',4),('forceRemote',5)))
_WrsLeapSecSource_Type.__name__=_C
_WrsLeapSecSource_Object=MibScalar
wrsLeapSecSource=_WrsLeapSecSource_Object((1,3,6,1,4,1,96,100,7,1,1,8),_WrsLeapSecSource_Type())
wrsLeapSecSource.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsLeapSecSource.setStatus(_B)
class _WrsLeapSecStatusDetails_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,0),(_H,1),(_Y,2),(_V,3),('leapSecFileExpired',4),('internalErrorDetected',5),('taiReadError',6),('leaSecInserted',7),('leapSecDeleted',8)))
_WrsLeapSecStatusDetails_Type.__name__=_C
_WrsLeapSecStatusDetails_Object=MibScalar
wrsLeapSecStatusDetails=_WrsLeapSecStatusDetails_Object((1,3,6,1,4,1,96,100,7,1,1,9),_WrsLeapSecStatusDetails_Type())
wrsLeapSecStatusDetails.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsLeapSecStatusDetails.setStatus(_B)
class _WrsLeapSecSourceStatusDetails_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,0),(_H,1),(_Y,2),(_V,3),('updated',4),(_Z,5),('invalidUrl',6),('invalidFile',7),(_X,8)))
_WrsLeapSecSourceStatusDetails_Type.__name__=_C
_WrsLeapSecSourceStatusDetails_Object=MibScalar
wrsLeapSecSourceStatusDetails=_WrsLeapSecSourceStatusDetails_Object((1,3,6,1,4,1,96,100,7,1,1,10),_WrsLeapSecSourceStatusDetails_Type())
wrsLeapSecSourceStatusDetails.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsLeapSecSourceStatusDetails.setStatus(_B)
class _WrsLeapSecSourceURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WrsLeapSecSourceURL_Type.__name__=_F
_WrsLeapSecSourceURL_Object=MibScalar
wrsLeapSecSourceURL=_WrsLeapSecSourceURL_Object((1,3,6,1,4,1,96,100,7,1,1,11),_WrsLeapSecSourceURL_Type())
wrsLeapSecSourceURL.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsLeapSecSourceURL.setStatus(_B)
_WrsSystemClockDriftUs_Type=Integer32
_WrsSystemClockDriftUs_Object=MibScalar
wrsSystemClockDriftUs=_WrsSystemClockDriftUs_Object((1,3,6,1,4,1,96,100,7,1,1,12),_WrsSystemClockDriftUs_Type())
wrsSystemClockDriftUs.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSystemClockDriftUs.setStatus(_B)
_WrsBootStatusGroup_ObjectIdentity=ObjectIdentity
wrsBootStatusGroup=_WrsBootStatusGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,1,2))
_WrsBootCnt_Type=Counter32
_WrsBootCnt_Object=MibScalar
wrsBootCnt=_WrsBootCnt_Object((1,3,6,1,4,1,96,100,7,1,2,1),_WrsBootCnt_Type())
wrsBootCnt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootCnt.setStatus(_B)
_WrsRebootCnt_Type=Counter32
_WrsRebootCnt_Object=MibScalar
wrsRebootCnt=_WrsRebootCnt_Object((1,3,6,1,4,1,96,100,7,1,2,2),_WrsRebootCnt_Type())
wrsRebootCnt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsRebootCnt.setStatus(_B)
class _WrsRestartReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,0),(_G,1),('generalReset',2),('wakeUpReset',3),('watchdogReset',4),('softwareReset',5),('userReset',6),('restartByMonit',7)))
_WrsRestartReason_Type.__name__=_C
_WrsRestartReason_Object=MibScalar
wrsRestartReason=_WrsRestartReason_Object((1,3,6,1,4,1,96,100,7,1,2,3),_WrsRestartReason_Type())
wrsRestartReason.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsRestartReason.setStatus(_B)
class _WrsFaultIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WrsFaultIP_Type.__name__=_P
_WrsFaultIP_Object=MibScalar
wrsFaultIP=_WrsFaultIP_Object((1,3,6,1,4,1,96,100,7,1,2,4),_WrsFaultIP_Type())
wrsFaultIP.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsFaultIP.setStatus(_B)
class _WrsFaultLR_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WrsFaultLR_Type.__name__=_P
_WrsFaultLR_Object=MibScalar
wrsFaultLR=_WrsFaultLR_Object((1,3,6,1,4,1,96,100,7,1,2,5),_WrsFaultLR_Type())
wrsFaultLR.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsFaultLR.setStatus(_B)
class _WrsConfigSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_D,0),(_G,1),(_L,2),(_W,3),(_a,4),('tryDhcp',5),('forceDhcp',6)))
_WrsConfigSource_Type.__name__=_C
_WrsConfigSource_Object=MibScalar
wrsConfigSource=_WrsConfigSource_Object((1,3,6,1,4,1,96,100,7,1,2,6),_WrsConfigSource_Type())
wrsConfigSource.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsConfigSource.setStatus(_B)
class _WrsConfigSourceUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WrsConfigSourceUrl_Type.__name__=_F
_WrsConfigSourceUrl_Object=MibScalar
wrsConfigSourceUrl=_WrsConfigSourceUrl_Object((1,3,6,1,4,1,96,100,7,1,2,7),_WrsConfigSourceUrl_Type())
wrsConfigSourceUrl.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsConfigSourceUrl.setStatus(_B)
class _WrsRestartReasonMonit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsRestartReasonMonit_Type.__name__=_F
_WrsRestartReasonMonit_Object=MibScalar
wrsRestartReasonMonit=_WrsRestartReasonMonit_Object((1,3,6,1,4,1,96,100,7,1,2,8),_WrsRestartReasonMonit_Type())
wrsRestartReasonMonit.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsRestartReasonMonit.setStatus(_B)
class _WrsBootConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_X,3),('checkError',4),(_L,5),(_Z,6)))
_WrsBootConfigStatus_Type.__name__=_C
_WrsBootConfigStatus_Object=MibScalar
wrsBootConfigStatus=_WrsBootConfigStatus_Object((1,3,6,1,4,1,96,100,7,1,2,9),_WrsBootConfigStatus_Type())
wrsBootConfigStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootConfigStatus.setStatus(_B)
class _WrsBootHwinfoReadout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_L,3),(_J,4)))
_WrsBootHwinfoReadout_Type.__name__=_C
_WrsBootHwinfoReadout_Object=MibScalar
wrsBootHwinfoReadout=_WrsBootHwinfoReadout_Object((1,3,6,1,4,1,96,100,7,1,2,10),_WrsBootHwinfoReadout_Type())
wrsBootHwinfoReadout.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootHwinfoReadout.setStatus(_B)
class _WrsBootLoadFPGA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_L,3),(_b,4)))
_WrsBootLoadFPGA_Type.__name__=_C
_WrsBootLoadFPGA_Object=MibScalar
wrsBootLoadFPGA=_WrsBootLoadFPGA_Object((1,3,6,1,4,1,96,100,7,1,2,11),_WrsBootLoadFPGA_Type())
wrsBootLoadFPGA.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootLoadFPGA.setStatus(_B)
class _WrsBootLoadLM32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_L,3),(_b,4)))
_WrsBootLoadLM32_Type.__name__=_C
_WrsBootLoadLM32_Object=MibScalar
wrsBootLoadLM32=_WrsBootLoadLM32_Object((1,3,6,1,4,1,96,100,7,1,2,12),_WrsBootLoadLM32_Type())
wrsBootLoadLM32.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootLoadLM32.setStatus(_B)
class _WrsBootKernelModulesMissing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('allKernelModulesPresent',0))
_WrsBootKernelModulesMissing_Type.__name__=_C
_WrsBootKernelModulesMissing_Object=MibScalar
wrsBootKernelModulesMissing=_WrsBootKernelModulesMissing_Object((1,3,6,1,4,1,96,100,7,1,2,13),_WrsBootKernelModulesMissing_Type())
wrsBootKernelModulesMissing.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootKernelModulesMissing.setStatus(_B)
class _WrsBootUserspaceDaemonsMissing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('allDaemonsPresent',0))
_WrsBootUserspaceDaemonsMissing_Type.__name__=_C
_WrsBootUserspaceDaemonsMissing_Object=MibScalar
wrsBootUserspaceDaemonsMissing=_WrsBootUserspaceDaemonsMissing_Object((1,3,6,1,4,1,96,100,7,1,2,14),_WrsBootUserspaceDaemonsMissing_Type())
wrsBootUserspaceDaemonsMissing.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsBootUserspaceDaemonsMissing.setStatus(_B)
_WrsGwWatchdogTimeouts_Type=Counter32
_WrsGwWatchdogTimeouts_Object=MibScalar
wrsGwWatchdogTimeouts=_WrsGwWatchdogTimeouts_Object((1,3,6,1,4,1,96,100,7,1,2,15),_WrsGwWatchdogTimeouts_Type())
wrsGwWatchdogTimeouts.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsGwWatchdogTimeouts.setStatus(_B)
class _WrsFwUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_H,1),('checksumError',2)))
_WrsFwUpdateStatus_Type.__name__=_C
_WrsFwUpdateStatus_Object=MibScalar
wrsFwUpdateStatus=_WrsFwUpdateStatus_Object((1,3,6,1,4,1,96,100,7,1,2,16),_WrsFwUpdateStatus_Type())
wrsFwUpdateStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsFwUpdateStatus.setStatus(_B)
class _WrsCustomBootScriptSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_G,1),(_L,2),(_W,3),(_a,4),(_K,5)))
_WrsCustomBootScriptSource_Type.__name__=_C
_WrsCustomBootScriptSource_Object=MibScalar
wrsCustomBootScriptSource=_WrsCustomBootScriptSource_Object((1,3,6,1,4,1,96,100,7,1,2,17),_WrsCustomBootScriptSource_Type())
wrsCustomBootScriptSource.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsCustomBootScriptSource.setStatus(_B)
class _WrsCustomBootScriptSourceUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WrsCustomBootScriptSourceUrl_Type.__name__=_F
_WrsCustomBootScriptSourceUrl_Object=MibScalar
wrsCustomBootScriptSourceUrl=_WrsCustomBootScriptSourceUrl_Object((1,3,6,1,4,1,96,100,7,1,2,18),_WrsCustomBootScriptSourceUrl_Type())
wrsCustomBootScriptSourceUrl.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsCustomBootScriptSourceUrl.setStatus(_B)
class _WrsCustomBootScriptStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,0),(_H,1),(_T,2),('wrongSrc',3),(_X,4),(_K,5),(_G,6),(_L,7)))
_WrsCustomBootScriptStatus_Type.__name__=_C
_WrsCustomBootScriptStatus_Object=MibScalar
wrsCustomBootScriptStatus=_WrsCustomBootScriptStatus_Object((1,3,6,1,4,1,96,100,7,1,2,19),_WrsCustomBootScriptStatus_Type())
wrsCustomBootScriptStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsCustomBootScriptStatus.setStatus(_B)
class _WrsAuxClkSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_T,2),(_K,3),(_G,4),(_L,5)))
_WrsAuxClkSetStatus_Type.__name__=_C
_WrsAuxClkSetStatus_Object=MibScalar
wrsAuxClkSetStatus=_WrsAuxClkSetStatus_Object((1,3,6,1,4,1,96,100,7,1,2,20),_WrsAuxClkSetStatus_Type())
wrsAuxClkSetStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsAuxClkSetStatus.setStatus(_B)
class _WrsThrottlingSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_T,2),(_K,3),(_G,4),(_L,5)))
_WrsThrottlingSetStatus_Type.__name__=_C
_WrsThrottlingSetStatus_Object=MibScalar
wrsThrottlingSetStatus=_WrsThrottlingSetStatus_Object((1,3,6,1,4,1,96,100,7,1,2,21),_WrsThrottlingSetStatus_Type())
wrsThrottlingSetStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsThrottlingSetStatus.setStatus(_B)
class _WrsVlansSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_H,1),(_T,2),(_K,3),(_G,4),(_L,5)))
_WrsVlansSetStatus_Type.__name__=_C
_WrsVlansSetStatus_Object=MibScalar
wrsVlansSetStatus=_WrsVlansSetStatus_Object((1,3,6,1,4,1,96,100,7,1,2,22),_WrsVlansSetStatus_Type())
wrsVlansSetStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsVlansSetStatus.setStatus(_B)
_WrsTemperatureGroup_ObjectIdentity=ObjectIdentity
wrsTemperatureGroup=_WrsTemperatureGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,1,3))
_WrsTempFPGA_Type=Integer32
_WrsTempFPGA_Object=MibScalar
wrsTempFPGA=_WrsTempFPGA_Object((1,3,6,1,4,1,96,100,7,1,3,1),_WrsTempFPGA_Type())
wrsTempFPGA.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempFPGA.setStatus(_B)
_WrsTempPLL_Type=Integer32
_WrsTempPLL_Object=MibScalar
wrsTempPLL=_WrsTempPLL_Object((1,3,6,1,4,1,96,100,7,1,3,2),_WrsTempPLL_Type())
wrsTempPLL.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempPLL.setStatus(_B)
_WrsTempPSL_Type=Integer32
_WrsTempPSL_Object=MibScalar
wrsTempPSL=_WrsTempPSL_Object((1,3,6,1,4,1,96,100,7,1,3,3),_WrsTempPSL_Type())
wrsTempPSL.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempPSL.setStatus(_B)
_WrsTempPSR_Type=Integer32
_WrsTempPSR_Object=MibScalar
wrsTempPSR=_WrsTempPSR_Object((1,3,6,1,4,1,96,100,7,1,3,4),_WrsTempPSR_Type())
wrsTempPSR.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempPSR.setStatus(_B)
_WrsTempThresholdFPGA_Type=Integer32
_WrsTempThresholdFPGA_Object=MibScalar
wrsTempThresholdFPGA=_WrsTempThresholdFPGA_Object((1,3,6,1,4,1,96,100,7,1,3,5),_WrsTempThresholdFPGA_Type())
wrsTempThresholdFPGA.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempThresholdFPGA.setStatus(_B)
_WrsTempThresholdPLL_Type=Integer32
_WrsTempThresholdPLL_Object=MibScalar
wrsTempThresholdPLL=_WrsTempThresholdPLL_Object((1,3,6,1,4,1,96,100,7,1,3,6),_WrsTempThresholdPLL_Type())
wrsTempThresholdPLL.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempThresholdPLL.setStatus(_B)
_WrsTempThresholdPSL_Type=Integer32
_WrsTempThresholdPSL_Object=MibScalar
wrsTempThresholdPSL=_WrsTempThresholdPSL_Object((1,3,6,1,4,1,96,100,7,1,3,7),_WrsTempThresholdPSL_Type())
wrsTempThresholdPSL.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempThresholdPSL.setStatus(_B)
_WrsTempThresholdPSR_Type=Integer32
_WrsTempThresholdPSR_Object=MibScalar
wrsTempThresholdPSR=_WrsTempThresholdPSR_Object((1,3,6,1,4,1,96,100,7,1,3,8),_WrsTempThresholdPSR_Type())
wrsTempThresholdPSR.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsTempThresholdPSR.setStatus(_B)
_WrsMemoryGroup_ObjectIdentity=ObjectIdentity
wrsMemoryGroup=_WrsMemoryGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,1,4))
_WrsMemoryTotal_Type=Integer32
_WrsMemoryTotal_Object=MibScalar
wrsMemoryTotal=_WrsMemoryTotal_Object((1,3,6,1,4,1,96,100,7,1,4,1),_WrsMemoryTotal_Type())
wrsMemoryTotal.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsMemoryTotal.setStatus(_B)
_WrsMemoryUsed_Type=Integer32
_WrsMemoryUsed_Object=MibScalar
wrsMemoryUsed=_WrsMemoryUsed_Object((1,3,6,1,4,1,96,100,7,1,4,2),_WrsMemoryUsed_Type())
wrsMemoryUsed.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsMemoryUsed.setStatus(_B)
_WrsMemoryUsedPerc_Type=Integer32
_WrsMemoryUsedPerc_Object=MibScalar
wrsMemoryUsedPerc=_WrsMemoryUsedPerc_Object((1,3,6,1,4,1,96,100,7,1,4,3),_WrsMemoryUsedPerc_Type())
wrsMemoryUsedPerc.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsMemoryUsedPerc.setStatus(_B)
_WrsMemoryFree_Type=Integer32
_WrsMemoryFree_Object=MibScalar
wrsMemoryFree=_WrsMemoryFree_Object((1,3,6,1,4,1,96,100,7,1,4,4),_WrsMemoryFree_Type())
wrsMemoryFree.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsMemoryFree.setStatus(_B)
_WrsCpuLoadGroup_ObjectIdentity=ObjectIdentity
wrsCpuLoadGroup=_WrsCpuLoadGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,1,5))
_WrsCPULoadAvg1min_Type=Integer32
_WrsCPULoadAvg1min_Object=MibScalar
wrsCPULoadAvg1min=_WrsCPULoadAvg1min_Object((1,3,6,1,4,1,96,100,7,1,5,1),_WrsCPULoadAvg1min_Type())
wrsCPULoadAvg1min.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsCPULoadAvg1min.setStatus(_B)
_WrsCPULoadAvg5min_Type=Integer32
_WrsCPULoadAvg5min_Object=MibScalar
wrsCPULoadAvg5min=_WrsCPULoadAvg5min_Object((1,3,6,1,4,1,96,100,7,1,5,2),_WrsCPULoadAvg5min_Type())
wrsCPULoadAvg5min.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsCPULoadAvg5min.setStatus(_B)
_WrsCPULoadAvg15min_Type=Integer32
_WrsCPULoadAvg15min_Object=MibScalar
wrsCPULoadAvg15min=_WrsCPULoadAvg15min_Object((1,3,6,1,4,1,96,100,7,1,5,3),_WrsCPULoadAvg15min_Type())
wrsCPULoadAvg15min.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsCPULoadAvg15min.setStatus(_B)
_WrsDiskTable_Object=MibTable
wrsDiskTable=_WrsDiskTable_Object((1,3,6,1,4,1,96,100,7,1,6))
if mibBuilder.loadTexts:wrsDiskTable.setStatus(_B)
_WrsDiskEntry_Object=MibTableRow
wrsDiskEntry=_WrsDiskEntry_Object((1,3,6,1,4,1,96,100,7,1,6,1))
wrsDiskEntry.setIndexNames((0,_M,_c))
if mibBuilder.loadTexts:wrsDiskEntry.setStatus(_B)
_WrsDiskIndex_Type=Unsigned32
_WrsDiskIndex_Object=MibTableColumn
wrsDiskIndex=_WrsDiskIndex_Object((1,3,6,1,4,1,96,100,7,1,6,1,1),_WrsDiskIndex_Type())
wrsDiskIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:wrsDiskIndex.setStatus(_B)
class _WrsDiskMountPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsDiskMountPath_Type.__name__=_F
_WrsDiskMountPath_Object=MibTableColumn
wrsDiskMountPath=_WrsDiskMountPath_Object((1,3,6,1,4,1,96,100,7,1,6,1,2),_WrsDiskMountPath_Type())
wrsDiskMountPath.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDiskMountPath.setStatus(_B)
_WrsDiskSize_Type=Integer32
_WrsDiskSize_Object=MibTableColumn
wrsDiskSize=_WrsDiskSize_Object((1,3,6,1,4,1,96,100,7,1,6,1,3),_WrsDiskSize_Type())
wrsDiskSize.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDiskSize.setStatus(_B)
_WrsDiskUsed_Type=Integer32
_WrsDiskUsed_Object=MibTableColumn
wrsDiskUsed=_WrsDiskUsed_Object((1,3,6,1,4,1,96,100,7,1,6,1,4),_WrsDiskUsed_Type())
wrsDiskUsed.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDiskUsed.setStatus(_B)
_WrsDiskFree_Type=Integer32
_WrsDiskFree_Object=MibTableColumn
wrsDiskFree=_WrsDiskFree_Object((1,3,6,1,4,1,96,100,7,1,6,1,5),_WrsDiskFree_Type())
wrsDiskFree.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDiskFree.setStatus(_B)
_WrsDiskUseRate_Type=Integer32
_WrsDiskUseRate_Object=MibTableColumn
wrsDiskUseRate=_WrsDiskUseRate_Object((1,3,6,1,4,1,96,100,7,1,6,1,6),_WrsDiskUseRate_Type())
wrsDiskUseRate.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDiskUseRate.setStatus(_B)
class _WrsDiskFilesystem_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WrsDiskFilesystem_Type.__name__=_F
_WrsDiskFilesystem_Object=MibTableColumn
wrsDiskFilesystem=_WrsDiskFilesystem_Object((1,3,6,1,4,1,96,100,7,1,6,1,7),_WrsDiskFilesystem_Type())
wrsDiskFilesystem.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsDiskFilesystem.setStatus(_B)
_WrsStartCntGroup_ObjectIdentity=ObjectIdentity
wrsStartCntGroup=_WrsStartCntGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,2))
_WrsStartCntHAL_Type=Counter32
_WrsStartCntHAL_Object=MibScalar
wrsStartCntHAL=_WrsStartCntHAL_Object((1,3,6,1,4,1,96,100,7,2,1),_WrsStartCntHAL_Type())
wrsStartCntHAL.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntHAL.setStatus(_B)
_WrsStartCntPTP_Type=Counter32
_WrsStartCntPTP_Object=MibScalar
wrsStartCntPTP=_WrsStartCntPTP_Object((1,3,6,1,4,1,96,100,7,2,2),_WrsStartCntPTP_Type())
wrsStartCntPTP.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntPTP.setStatus(_B)
_WrsStartCntRTUd_Type=Counter32
_WrsStartCntRTUd_Object=MibScalar
wrsStartCntRTUd=_WrsStartCntRTUd_Object((1,3,6,1,4,1,96,100,7,2,3),_WrsStartCntRTUd_Type())
wrsStartCntRTUd.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntRTUd.setStatus(_B)
_WrsStartCntSshd_Type=Counter32
_WrsStartCntSshd_Object=MibScalar
wrsStartCntSshd=_WrsStartCntSshd_Object((1,3,6,1,4,1,96,100,7,2,4),_WrsStartCntSshd_Type())
wrsStartCntSshd.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntSshd.setStatus(_B)
_WrsStartCntHttpd_Type=Counter32
_WrsStartCntHttpd_Object=MibScalar
wrsStartCntHttpd=_WrsStartCntHttpd_Object((1,3,6,1,4,1,96,100,7,2,5),_WrsStartCntHttpd_Type())
wrsStartCntHttpd.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntHttpd.setStatus(_B)
_WrsStartCntSnmpd_Type=Counter32
_WrsStartCntSnmpd_Object=MibScalar
wrsStartCntSnmpd=_WrsStartCntSnmpd_Object((1,3,6,1,4,1,96,100,7,2,6),_WrsStartCntSnmpd_Type())
wrsStartCntSnmpd.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntSnmpd.setStatus(_B)
_WrsStartCntSyslogd_Type=Counter32
_WrsStartCntSyslogd_Object=MibScalar
wrsStartCntSyslogd=_WrsStartCntSyslogd_Object((1,3,6,1,4,1,96,100,7,2,7),_WrsStartCntSyslogd_Type())
wrsStartCntSyslogd.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntSyslogd.setStatus(_B)
_WrsStartCntWrsWatchdog_Type=Counter32
_WrsStartCntWrsWatchdog_Object=MibScalar
wrsStartCntWrsWatchdog=_WrsStartCntWrsWatchdog_Object((1,3,6,1,4,1,96,100,7,2,8),_WrsStartCntWrsWatchdog_Type())
wrsStartCntWrsWatchdog.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntWrsWatchdog.setStatus(_B)
_WrsStartCntLldpd_Type=Counter32
_WrsStartCntLldpd_Object=MibScalar
wrsStartCntLldpd=_WrsStartCntLldpd_Object((1,3,6,1,4,1,96,100,7,2,9),_WrsStartCntLldpd_Type())
wrsStartCntLldpd.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntLldpd.setStatus(_B)
_WrsStartCntLdap_Type=Counter32
_WrsStartCntLdap_Object=MibScalar
wrsStartCntLdap=_WrsStartCntLdap_Object((1,3,6,1,4,1,96,100,7,2,10),_WrsStartCntLdap_Type())
wrsStartCntLdap.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntLdap.setStatus(_B)
_WrsStartCntRvlan_Type=Counter32
_WrsStartCntRvlan_Object=MibScalar
wrsStartCntRvlan=_WrsStartCntRvlan_Object((1,3,6,1,4,1,96,100,7,2,11),_WrsStartCntRvlan_Type())
wrsStartCntRvlan.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsStartCntRvlan.setStatus(_B)
_WrsSpllState_ObjectIdentity=ObjectIdentity
wrsSpllState=_WrsSpllState_ObjectIdentity((1,3,6,1,4,1,96,100,7,3))
_WrsSpllVersionGroup_ObjectIdentity=ObjectIdentity
wrsSpllVersionGroup=_WrsSpllVersionGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,3,1))
class _WrsSpllVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsSpllVersion_Type.__name__=_F
_WrsSpllVersion_Object=MibScalar
wrsSpllVersion=_WrsSpllVersion_Object((1,3,6,1,4,1,96,100,7,3,1,1),_WrsSpllVersion_Type())
wrsSpllVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllVersion.setStatus(_B)
class _WrsSpllBuildDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsSpllBuildDate_Type.__name__=_F
_WrsSpllBuildDate_Object=MibScalar
wrsSpllBuildDate=_WrsSpllBuildDate_Object((1,3,6,1,4,1,96,100,7,3,1,2),_WrsSpllBuildDate_Type())
wrsSpllBuildDate.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllBuildDate.setStatus(_B)
class _WrsSpllBuildBy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsSpllBuildBy_Type.__name__=_F
_WrsSpllBuildBy_Object=MibScalar
wrsSpllBuildBy=_WrsSpllBuildBy_Object((1,3,6,1,4,1,96,100,7,3,1,3),_WrsSpllBuildBy_Type())
wrsSpllBuildBy.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllBuildBy.setStatus(_B)
_WrsSpllStatusGroup_ObjectIdentity=ObjectIdentity
wrsSpllStatusGroup=_WrsSpllStatusGroup_ObjectIdentity((1,3,6,1,4,1,96,100,7,3,2))
class _WrsSpllMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_d,1),(_R,2),(_S,3),(_K,4)))
_WrsSpllMode_Type.__name__=_C
_WrsSpllMode_Object=MibScalar
wrsSpllMode=_WrsSpllMode_Object((1,3,6,1,4,1,96,100,7,3,2,1),_WrsSpllMode_Type())
wrsSpllMode.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllMode.setStatus(_B)
_WrsSpllIrqCnt_Type=Counter32
_WrsSpllIrqCnt_Object=MibScalar
wrsSpllIrqCnt=_WrsSpllIrqCnt_Object((1,3,6,1,4,1,96,100,7,3,2,2),_WrsSpllIrqCnt_Type())
wrsSpllIrqCnt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllIrqCnt.setStatus(_B)
class _WrsSpllSeqState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('startExt',1),('waitExt',2),('startHelper',3),('waitHelper',4),(_e,5),('waitMain',6),(_K,7),('ready',8),('clearDacs',9),('waitClearDacs',10)))
_WrsSpllSeqState_Type.__name__=_C
_WrsSpllSeqState_Object=MibScalar
wrsSpllSeqState=_WrsSpllSeqState_Object((1,3,6,1,4,1,96,100,7,3,2,3),_WrsSpllSeqState_Type())
wrsSpllSeqState.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllSeqState.setStatus(_B)
class _WrsSpllAlignState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('extOff',0),('start',1),('initCsync',2),('waitCsync',3),('waitSample',4),('compensateDelay',5),(_f,6),('startAlignment',7),(_e,8),('waitClkIn',9),('waitPlock',10)))
_WrsSpllAlignState_Type.__name__=_C
_WrsSpllAlignState_Object=MibScalar
wrsSpllAlignState=_WrsSpllAlignState_Object((1,3,6,1,4,1,96,100,7,3,2,4),_WrsSpllAlignState_Type())
wrsSpllAlignState.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllAlignState.setStatus(_B)
_WrsSpllHlock_Type=Counter32
_WrsSpllHlock_Object=MibScalar
wrsSpllHlock=_WrsSpllHlock_Object((1,3,6,1,4,1,96,100,7,3,2,5),_WrsSpllHlock_Type())
wrsSpllHlock.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllHlock.setStatus(_B)
_WrsSpllMlock_Type=Counter32
_WrsSpllMlock_Object=MibScalar
wrsSpllMlock=_WrsSpllMlock_Object((1,3,6,1,4,1,96,100,7,3,2,6),_WrsSpllMlock_Type())
wrsSpllMlock.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllMlock.setStatus(_B)
_WrsSpllHY_Type=Integer32
_WrsSpllHY_Object=MibScalar
wrsSpllHY=_WrsSpllHY_Object((1,3,6,1,4,1,96,100,7,3,2,7),_WrsSpllHY_Type())
wrsSpllHY.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllHY.setStatus(_B)
_WrsSpllMY_Type=Integer32
_WrsSpllMY_Object=MibScalar
wrsSpllMY=_WrsSpllMY_Object((1,3,6,1,4,1,96,100,7,3,2,8),_WrsSpllMY_Type())
wrsSpllMY.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllMY.setStatus(_B)
_WrsSpllDelCnt_Type=Counter32
_WrsSpllDelCnt_Object=MibScalar
wrsSpllDelCnt=_WrsSpllDelCnt_Object((1,3,6,1,4,1,96,100,7,3,2,9),_WrsSpllDelCnt_Type())
wrsSpllDelCnt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsSpllDelCnt.setStatus(_B)
_WrsPstatsTable_Object=MibTable
wrsPstatsTable=_WrsPstatsTable_Object((1,3,6,1,4,1,96,100,7,4))
if mibBuilder.loadTexts:wrsPstatsTable.setStatus(_E)
_WrsPstatsEntry_Object=MibTableRow
wrsPstatsEntry=_WrsPstatsEntry_Object((1,3,6,1,4,1,96,100,7,4,1))
wrsPstatsEntry.setIndexNames((0,_M,_g))
if mibBuilder.loadTexts:wrsPstatsEntry.setStatus(_E)
_WrsPstatsIndex_Type=Unsigned32
_WrsPstatsIndex_Object=MibTableColumn
wrsPstatsIndex=_WrsPstatsIndex_Object((1,3,6,1,4,1,96,100,7,4,1,1),_WrsPstatsIndex_Type())
wrsPstatsIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:wrsPstatsIndex.setStatus(_E)
class _WrsPstatsPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_WrsPstatsPortName_Type.__name__=_F
_WrsPstatsPortName_Object=MibTableColumn
wrsPstatsPortName=_WrsPstatsPortName_Object((1,3,6,1,4,1,96,100,7,4,1,2),_WrsPstatsPortName_Type())
wrsPstatsPortName.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsPortName.setStatus(_E)
_WrsPstatsTXUnderrun_Type=Counter32
_WrsPstatsTXUnderrun_Object=MibTableColumn
wrsPstatsTXUnderrun=_WrsPstatsTXUnderrun_Object((1,3,6,1,4,1,96,100,7,4,1,3),_WrsPstatsTXUnderrun_Type())
wrsPstatsTXUnderrun.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsTXUnderrun.setStatus(_E)
_WrsPstatsRXOverrun_Type=Counter32
_WrsPstatsRXOverrun_Object=MibTableColumn
wrsPstatsRXOverrun=_WrsPstatsRXOverrun_Object((1,3,6,1,4,1,96,100,7,4,1,4),_WrsPstatsRXOverrun_Type())
wrsPstatsRXOverrun.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXOverrun.setStatus(_E)
_WrsPstatsRXInvalidCode_Type=Counter32
_WrsPstatsRXInvalidCode_Object=MibTableColumn
wrsPstatsRXInvalidCode=_WrsPstatsRXInvalidCode_Object((1,3,6,1,4,1,96,100,7,4,1,5),_WrsPstatsRXInvalidCode_Type())
wrsPstatsRXInvalidCode.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXInvalidCode.setStatus(_E)
_WrsPstatsRXSyncLost_Type=Counter32
_WrsPstatsRXSyncLost_Object=MibTableColumn
wrsPstatsRXSyncLost=_WrsPstatsRXSyncLost_Object((1,3,6,1,4,1,96,100,7,4,1,6),_WrsPstatsRXSyncLost_Type())
wrsPstatsRXSyncLost.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXSyncLost.setStatus(_E)
_WrsPstatsRXPauseFrames_Type=Counter32
_WrsPstatsRXPauseFrames_Object=MibTableColumn
wrsPstatsRXPauseFrames=_WrsPstatsRXPauseFrames_Object((1,3,6,1,4,1,96,100,7,4,1,7),_WrsPstatsRXPauseFrames_Type())
wrsPstatsRXPauseFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPauseFrames.setStatus(_E)
_WrsPstatsRXPfilterDropped_Type=Counter32
_WrsPstatsRXPfilterDropped_Object=MibTableColumn
wrsPstatsRXPfilterDropped=_WrsPstatsRXPfilterDropped_Object((1,3,6,1,4,1,96,100,7,4,1,8),_WrsPstatsRXPfilterDropped_Type())
wrsPstatsRXPfilterDropped.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPfilterDropped.setStatus(_E)
_WrsPstatsRXPCSErrors_Type=Counter32
_WrsPstatsRXPCSErrors_Object=MibTableColumn
wrsPstatsRXPCSErrors=_WrsPstatsRXPCSErrors_Object((1,3,6,1,4,1,96,100,7,4,1,9),_WrsPstatsRXPCSErrors_Type())
wrsPstatsRXPCSErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPCSErrors.setStatus(_E)
_WrsPstatsRXGiantFrames_Type=Counter32
_WrsPstatsRXGiantFrames_Object=MibTableColumn
wrsPstatsRXGiantFrames=_WrsPstatsRXGiantFrames_Object((1,3,6,1,4,1,96,100,7,4,1,10),_WrsPstatsRXGiantFrames_Type())
wrsPstatsRXGiantFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXGiantFrames.setStatus(_E)
_WrsPstatsRXRuntFrames_Type=Counter32
_WrsPstatsRXRuntFrames_Object=MibTableColumn
wrsPstatsRXRuntFrames=_WrsPstatsRXRuntFrames_Object((1,3,6,1,4,1,96,100,7,4,1,11),_WrsPstatsRXRuntFrames_Type())
wrsPstatsRXRuntFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXRuntFrames.setStatus(_E)
_WrsPstatsRXCRCErrors_Type=Counter32
_WrsPstatsRXCRCErrors_Object=MibTableColumn
wrsPstatsRXCRCErrors=_WrsPstatsRXCRCErrors_Object((1,3,6,1,4,1,96,100,7,4,1,12),_WrsPstatsRXCRCErrors_Type())
wrsPstatsRXCRCErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXCRCErrors.setStatus(_E)
_WrsPstatsRXPclass0_Type=Counter32
_WrsPstatsRXPclass0_Object=MibTableColumn
wrsPstatsRXPclass0=_WrsPstatsRXPclass0_Object((1,3,6,1,4,1,96,100,7,4,1,13),_WrsPstatsRXPclass0_Type())
wrsPstatsRXPclass0.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass0.setStatus(_E)
_WrsPstatsRXPclass1_Type=Counter32
_WrsPstatsRXPclass1_Object=MibTableColumn
wrsPstatsRXPclass1=_WrsPstatsRXPclass1_Object((1,3,6,1,4,1,96,100,7,4,1,14),_WrsPstatsRXPclass1_Type())
wrsPstatsRXPclass1.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass1.setStatus(_E)
_WrsPstatsRXPclass2_Type=Counter32
_WrsPstatsRXPclass2_Object=MibTableColumn
wrsPstatsRXPclass2=_WrsPstatsRXPclass2_Object((1,3,6,1,4,1,96,100,7,4,1,15),_WrsPstatsRXPclass2_Type())
wrsPstatsRXPclass2.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass2.setStatus(_E)
_WrsPstatsRXPclass3_Type=Counter32
_WrsPstatsRXPclass3_Object=MibTableColumn
wrsPstatsRXPclass3=_WrsPstatsRXPclass3_Object((1,3,6,1,4,1,96,100,7,4,1,16),_WrsPstatsRXPclass3_Type())
wrsPstatsRXPclass3.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass3.setStatus(_E)
_WrsPstatsRXPclass4_Type=Counter32
_WrsPstatsRXPclass4_Object=MibTableColumn
wrsPstatsRXPclass4=_WrsPstatsRXPclass4_Object((1,3,6,1,4,1,96,100,7,4,1,17),_WrsPstatsRXPclass4_Type())
wrsPstatsRXPclass4.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass4.setStatus(_E)
_WrsPstatsRXPclass5_Type=Counter32
_WrsPstatsRXPclass5_Object=MibTableColumn
wrsPstatsRXPclass5=_WrsPstatsRXPclass5_Object((1,3,6,1,4,1,96,100,7,4,1,18),_WrsPstatsRXPclass5_Type())
wrsPstatsRXPclass5.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass5.setStatus(_E)
_WrsPstatsRXPclass6_Type=Counter32
_WrsPstatsRXPclass6_Object=MibTableColumn
wrsPstatsRXPclass6=_WrsPstatsRXPclass6_Object((1,3,6,1,4,1,96,100,7,4,1,19),_WrsPstatsRXPclass6_Type())
wrsPstatsRXPclass6.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass6.setStatus(_E)
_WrsPstatsRXPclass7_Type=Counter32
_WrsPstatsRXPclass7_Object=MibTableColumn
wrsPstatsRXPclass7=_WrsPstatsRXPclass7_Object((1,3,6,1,4,1,96,100,7,4,1,20),_WrsPstatsRXPclass7_Type())
wrsPstatsRXPclass7.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPclass7.setStatus(_E)
_WrsPstatsTXFrames_Type=Counter32
_WrsPstatsTXFrames_Object=MibTableColumn
wrsPstatsTXFrames=_WrsPstatsTXFrames_Object((1,3,6,1,4,1,96,100,7,4,1,21),_WrsPstatsTXFrames_Type())
wrsPstatsTXFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsTXFrames.setStatus(_E)
_WrsPstatsRXFrames_Type=Counter32
_WrsPstatsRXFrames_Object=MibTableColumn
wrsPstatsRXFrames=_WrsPstatsRXFrames_Object((1,3,6,1,4,1,96,100,7,4,1,22),_WrsPstatsRXFrames_Type())
wrsPstatsRXFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXFrames.setStatus(_E)
_WrsPstatsRXDropRTUFull_Type=Counter32
_WrsPstatsRXDropRTUFull_Object=MibTableColumn
wrsPstatsRXDropRTUFull=_WrsPstatsRXDropRTUFull_Object((1,3,6,1,4,1,96,100,7,4,1,23),_WrsPstatsRXDropRTUFull_Type())
wrsPstatsRXDropRTUFull.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXDropRTUFull.setStatus(_E)
_WrsPstatsRXPrio0_Type=Counter32
_WrsPstatsRXPrio0_Object=MibTableColumn
wrsPstatsRXPrio0=_WrsPstatsRXPrio0_Object((1,3,6,1,4,1,96,100,7,4,1,24),_WrsPstatsRXPrio0_Type())
wrsPstatsRXPrio0.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio0.setStatus(_E)
_WrsPstatsRXPrio1_Type=Counter32
_WrsPstatsRXPrio1_Object=MibTableColumn
wrsPstatsRXPrio1=_WrsPstatsRXPrio1_Object((1,3,6,1,4,1,96,100,7,4,1,25),_WrsPstatsRXPrio1_Type())
wrsPstatsRXPrio1.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio1.setStatus(_E)
_WrsPstatsRXPrio2_Type=Counter32
_WrsPstatsRXPrio2_Object=MibTableColumn
wrsPstatsRXPrio2=_WrsPstatsRXPrio2_Object((1,3,6,1,4,1,96,100,7,4,1,26),_WrsPstatsRXPrio2_Type())
wrsPstatsRXPrio2.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio2.setStatus(_E)
_WrsPstatsRXPrio3_Type=Counter32
_WrsPstatsRXPrio3_Object=MibTableColumn
wrsPstatsRXPrio3=_WrsPstatsRXPrio3_Object((1,3,6,1,4,1,96,100,7,4,1,27),_WrsPstatsRXPrio3_Type())
wrsPstatsRXPrio3.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio3.setStatus(_E)
_WrsPstatsRXPrio4_Type=Counter32
_WrsPstatsRXPrio4_Object=MibTableColumn
wrsPstatsRXPrio4=_WrsPstatsRXPrio4_Object((1,3,6,1,4,1,96,100,7,4,1,28),_WrsPstatsRXPrio4_Type())
wrsPstatsRXPrio4.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio4.setStatus(_E)
_WrsPstatsRXPrio5_Type=Counter32
_WrsPstatsRXPrio5_Object=MibTableColumn
wrsPstatsRXPrio5=_WrsPstatsRXPrio5_Object((1,3,6,1,4,1,96,100,7,4,1,29),_WrsPstatsRXPrio5_Type())
wrsPstatsRXPrio5.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio5.setStatus(_E)
_WrsPstatsRXPrio6_Type=Counter32
_WrsPstatsRXPrio6_Object=MibTableColumn
wrsPstatsRXPrio6=_WrsPstatsRXPrio6_Object((1,3,6,1,4,1,96,100,7,4,1,30),_WrsPstatsRXPrio6_Type())
wrsPstatsRXPrio6.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio6.setStatus(_E)
_WrsPstatsRXPrio7_Type=Counter32
_WrsPstatsRXPrio7_Object=MibTableColumn
wrsPstatsRXPrio7=_WrsPstatsRXPrio7_Object((1,3,6,1,4,1,96,100,7,4,1,31),_WrsPstatsRXPrio7_Type())
wrsPstatsRXPrio7.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRXPrio7.setStatus(_E)
_WrsPstatsRTUValid_Type=Counter32
_WrsPstatsRTUValid_Object=MibTableColumn
wrsPstatsRTUValid=_WrsPstatsRTUValid_Object((1,3,6,1,4,1,96,100,7,4,1,32),_WrsPstatsRTUValid_Type())
wrsPstatsRTUValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRTUValid.setStatus(_E)
_WrsPstatsRTUResponses_Type=Counter32
_WrsPstatsRTUResponses_Object=MibTableColumn
wrsPstatsRTUResponses=_WrsPstatsRTUResponses_Object((1,3,6,1,4,1,96,100,7,4,1,33),_WrsPstatsRTUResponses_Type())
wrsPstatsRTUResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRTUResponses.setStatus(_E)
_WrsPstatsRTUDropped_Type=Counter32
_WrsPstatsRTUDropped_Object=MibTableColumn
wrsPstatsRTUDropped=_WrsPstatsRTUDropped_Object((1,3,6,1,4,1,96,100,7,4,1,34),_WrsPstatsRTUDropped_Type())
wrsPstatsRTUDropped.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsRTUDropped.setStatus(_E)
_WrsPstatsFastMatchPriority_Type=Counter32
_WrsPstatsFastMatchPriority_Object=MibTableColumn
wrsPstatsFastMatchPriority=_WrsPstatsFastMatchPriority_Object((1,3,6,1,4,1,96,100,7,4,1,35),_WrsPstatsFastMatchPriority_Type())
wrsPstatsFastMatchPriority.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsFastMatchPriority.setStatus(_E)
_WrsPstatsFastMatchFastForward_Type=Counter32
_WrsPstatsFastMatchFastForward_Object=MibTableColumn
wrsPstatsFastMatchFastForward=_WrsPstatsFastMatchFastForward_Object((1,3,6,1,4,1,96,100,7,4,1,36),_WrsPstatsFastMatchFastForward_Type())
wrsPstatsFastMatchFastForward.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsFastMatchFastForward.setStatus(_E)
_WrsPstatsFastMatchNonForward_Type=Counter32
_WrsPstatsFastMatchNonForward_Object=MibTableColumn
wrsPstatsFastMatchNonForward=_WrsPstatsFastMatchNonForward_Object((1,3,6,1,4,1,96,100,7,4,1,37),_WrsPstatsFastMatchNonForward_Type())
wrsPstatsFastMatchNonForward.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsFastMatchNonForward.setStatus(_E)
_WrsPstatsFastMatchRespValid_Type=Counter32
_WrsPstatsFastMatchRespValid_Object=MibTableColumn
wrsPstatsFastMatchRespValid=_WrsPstatsFastMatchRespValid_Object((1,3,6,1,4,1,96,100,7,4,1,38),_WrsPstatsFastMatchRespValid_Type())
wrsPstatsFastMatchRespValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsFastMatchRespValid.setStatus(_E)
_WrsPstatsFullMatchRespValid_Type=Counter32
_WrsPstatsFullMatchRespValid_Object=MibTableColumn
wrsPstatsFullMatchRespValid=_WrsPstatsFullMatchRespValid_Object((1,3,6,1,4,1,96,100,7,4,1,39),_WrsPstatsFullMatchRespValid_Type())
wrsPstatsFullMatchRespValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsFullMatchRespValid.setStatus(_E)
_WrsPstatsForwarded_Type=Counter32
_WrsPstatsForwarded_Object=MibTableColumn
wrsPstatsForwarded=_WrsPstatsForwarded_Object((1,3,6,1,4,1,96,100,7,4,1,40),_WrsPstatsForwarded_Type())
wrsPstatsForwarded.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsForwarded.setStatus(_E)
_WrsPstatsTRURespValid_Type=Counter32
_WrsPstatsTRURespValid_Object=MibTableColumn
wrsPstatsTRURespValid=_WrsPstatsTRURespValid_Object((1,3,6,1,4,1,96,100,7,4,1,41),_WrsPstatsTRURespValid_Type())
wrsPstatsTRURespValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsTRURespValid.setStatus(_E)
_WrsPtpDataTable_Object=MibTable
wrsPtpDataTable=_WrsPtpDataTable_Object((1,3,6,1,4,1,96,100,7,5))
if mibBuilder.loadTexts:wrsPtpDataTable.setStatus(_B)
_WrsPtpDataEntry_Object=MibTableRow
wrsPtpDataEntry=_WrsPtpDataEntry_Object((1,3,6,1,4,1,96,100,7,5,1))
wrsPtpDataEntry.setIndexNames((0,_M,_h))
if mibBuilder.loadTexts:wrsPtpDataEntry.setStatus(_B)
_WrsPtpDataIndex_Type=Unsigned32
_WrsPtpDataIndex_Object=MibTableColumn
wrsPtpDataIndex=_WrsPtpDataIndex_Object((1,3,6,1,4,1,96,100,7,5,1,1),_WrsPtpDataIndex_Type())
wrsPtpDataIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:wrsPtpDataIndex.setStatus(_B)
class _WrsPtpPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_WrsPtpPortName_Type.__name__=_F
_WrsPtpPortName_Object=MibTableColumn
wrsPtpPortName=_WrsPtpPortName_Object((1,3,6,1,4,1,96,100,7,5,1,2),_WrsPtpPortName_Type())
wrsPtpPortName.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpPortName.setStatus(_B)
class _WrsPtpGrandmasterID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_WrsPtpGrandmasterID_Type.__name__=_P
_WrsPtpGrandmasterID_Object=MibTableColumn
wrsPtpGrandmasterID=_WrsPtpGrandmasterID_Object((1,3,6,1,4,1,96,100,7,5,1,3),_WrsPtpGrandmasterID_Type())
wrsPtpGrandmasterID.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpGrandmasterID.setStatus(_B)
class _WrsPtpOwnID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_WrsPtpOwnID_Type.__name__=_P
_WrsPtpOwnID_Object=MibTableColumn
wrsPtpOwnID=_WrsPtpOwnID_Object((1,3,6,1,4,1,96,100,7,5,1,4),_WrsPtpOwnID_Type())
wrsPtpOwnID.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpOwnID.setStatus(_B)
class _WrsPtpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_i,0),(_d,1),(_R,2),(_S,3)))
_WrsPtpMode_Type.__name__=_C
_WrsPtpMode_Object=MibTableColumn
wrsPtpMode=_WrsPtpMode_Object((1,3,6,1,4,1,96,100,7,5,1,5),_WrsPtpMode_Type())
wrsPtpMode.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpMode.setStatus(_j)
class _WrsPtpServoState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsPtpServoState_Type.__name__=_F
_WrsPtpServoState_Object=MibTableColumn
wrsPtpServoState=_WrsPtpServoState_Object((1,3,6,1,4,1,96,100,7,5,1,6),_WrsPtpServoState_Type())
wrsPtpServoState.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpServoState.setStatus(_B)
class _WrsPtpServoStateN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,99)));namedValues=NamedValues(*(('uninitialized',0),('syncNsec',1),('syncSec',2),('syncPhase',3),('trackPhase',4),('waitOffsetStable',5),('standardPTP',99)))
_WrsPtpServoStateN_Type.__name__=_C
_WrsPtpServoStateN_Object=MibTableColumn
wrsPtpServoStateN=_WrsPtpServoStateN_Object((1,3,6,1,4,1,96,100,7,5,1,7),_WrsPtpServoStateN_Type())
wrsPtpServoStateN.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpServoStateN.setStatus(_B)
class _WrsPtpPhaseTracking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('notTracking',1),('tracking',2)))
_WrsPtpPhaseTracking_Type.__name__=_C
_WrsPtpPhaseTracking_Object=MibTableColumn
wrsPtpPhaseTracking=_WrsPtpPhaseTracking_Object((1,3,6,1,4,1,96,100,7,5,1,8),_WrsPtpPhaseTracking_Type())
wrsPtpPhaseTracking.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpPhaseTracking.setStatus(_B)
class _WrsPtpSyncSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsPtpSyncSource_Type.__name__=_F
_WrsPtpSyncSource_Object=MibTableColumn
wrsPtpSyncSource=_WrsPtpSyncSource_Object((1,3,6,1,4,1,96,100,7,5,1,9),_WrsPtpSyncSource_Type())
wrsPtpSyncSource.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpSyncSource.setStatus(_B)
_WrsPtpClockOffsetPs_Type=Counter64
_WrsPtpClockOffsetPs_Object=MibTableColumn
wrsPtpClockOffsetPs=_WrsPtpClockOffsetPs_Object((1,3,6,1,4,1,96,100,7,5,1,10),_WrsPtpClockOffsetPs_Type())
wrsPtpClockOffsetPs.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpClockOffsetPs.setStatus(_B)
_WrsPtpClockOffsetPsHR_Type=Integer32
_WrsPtpClockOffsetPsHR_Object=MibTableColumn
wrsPtpClockOffsetPsHR=_WrsPtpClockOffsetPsHR_Object((1,3,6,1,4,1,96,100,7,5,1,11),_WrsPtpClockOffsetPsHR_Type())
wrsPtpClockOffsetPsHR.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpClockOffsetPsHR.setStatus(_B)
_WrsPtpSkew_Type=Integer32
_WrsPtpSkew_Object=MibTableColumn
wrsPtpSkew=_WrsPtpSkew_Object((1,3,6,1,4,1,96,100,7,5,1,12),_WrsPtpSkew_Type())
wrsPtpSkew.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpSkew.setStatus(_B)
_WrsPtpRTT_Type=Counter64
_WrsPtpRTT_Object=MibTableColumn
wrsPtpRTT=_WrsPtpRTT_Object((1,3,6,1,4,1,96,100,7,5,1,13),_WrsPtpRTT_Type())
wrsPtpRTT.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpRTT.setStatus(_B)
_WrsPtpLinkLength_Type=Unsigned32
_WrsPtpLinkLength_Object=MibTableColumn
wrsPtpLinkLength=_WrsPtpLinkLength_Object((1,3,6,1,4,1,96,100,7,5,1,14),_WrsPtpLinkLength_Type())
wrsPtpLinkLength.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpLinkLength.setStatus(_B)
_WrsPtpServoUpdates_Type=Counter32
_WrsPtpServoUpdates_Object=MibTableColumn
wrsPtpServoUpdates=_WrsPtpServoUpdates_Object((1,3,6,1,4,1,96,100,7,5,1,15),_WrsPtpServoUpdates_Type())
wrsPtpServoUpdates.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpServoUpdates.setStatus(_B)
_WrsPtpDeltaTxM_Type=Integer32
_WrsPtpDeltaTxM_Object=MibTableColumn
wrsPtpDeltaTxM=_WrsPtpDeltaTxM_Object((1,3,6,1,4,1,96,100,7,5,1,16),_WrsPtpDeltaTxM_Type())
wrsPtpDeltaTxM.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpDeltaTxM.setStatus(_B)
_WrsPtpDeltaRxM_Type=Integer32
_WrsPtpDeltaRxM_Object=MibTableColumn
wrsPtpDeltaRxM=_WrsPtpDeltaRxM_Object((1,3,6,1,4,1,96,100,7,5,1,17),_WrsPtpDeltaRxM_Type())
wrsPtpDeltaRxM.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpDeltaRxM.setStatus(_B)
_WrsPtpDeltaTxS_Type=Integer32
_WrsPtpDeltaTxS_Object=MibTableColumn
wrsPtpDeltaTxS=_WrsPtpDeltaTxS_Object((1,3,6,1,4,1,96,100,7,5,1,18),_WrsPtpDeltaTxS_Type())
wrsPtpDeltaTxS.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpDeltaTxS.setStatus(_B)
_WrsPtpDeltaRxS_Type=Integer32
_WrsPtpDeltaRxS_Object=MibTableColumn
wrsPtpDeltaRxS=_WrsPtpDeltaRxS_Object((1,3,6,1,4,1,96,100,7,5,1,19),_WrsPtpDeltaRxS_Type())
wrsPtpDeltaRxS.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpDeltaRxS.setStatus(_B)
_WrsPtpServoStateErrCnt_Type=Counter32
_WrsPtpServoStateErrCnt_Object=MibTableColumn
wrsPtpServoStateErrCnt=_WrsPtpServoStateErrCnt_Object((1,3,6,1,4,1,96,100,7,5,1,20),_WrsPtpServoStateErrCnt_Type())
wrsPtpServoStateErrCnt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpServoStateErrCnt.setStatus(_B)
_WrsPtpClockOffsetErrCnt_Type=Counter32
_WrsPtpClockOffsetErrCnt_Object=MibTableColumn
wrsPtpClockOffsetErrCnt=_WrsPtpClockOffsetErrCnt_Object((1,3,6,1,4,1,96,100,7,5,1,21),_WrsPtpClockOffsetErrCnt_Type())
wrsPtpClockOffsetErrCnt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpClockOffsetErrCnt.setStatus(_B)
_WrsPtpRTTErrCnt_Type=Counter32
_WrsPtpRTTErrCnt_Object=MibTableColumn
wrsPtpRTTErrCnt=_WrsPtpRTTErrCnt_Object((1,3,6,1,4,1,96,100,7,5,1,22),_WrsPtpRTTErrCnt_Type())
wrsPtpRTTErrCnt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpRTTErrCnt.setStatus(_B)
_WrsPtpServoUpdateTime_Type=Counter64
_WrsPtpServoUpdateTime_Object=MibTableColumn
wrsPtpServoUpdateTime=_WrsPtpServoUpdateTime_Object((1,3,6,1,4,1,96,100,7,5,1,23),_WrsPtpServoUpdateTime_Type())
wrsPtpServoUpdateTime.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpServoUpdateTime.setStatus(_B)
class _WrsPtpServoExt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_U,1),('wr',2),(_k,3)))
_WrsPtpServoExt_Type.__name__=_C
_WrsPtpServoExt_Object=MibTableColumn
wrsPtpServoExt=_WrsPtpServoExt_Object((1,3,6,1,4,1,96,100,7,5,1,24),_WrsPtpServoExt_Type())
wrsPtpServoExt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpServoExt.setStatus(_B)
_WrsPortStatusTable_Object=MibTable
wrsPortStatusTable=_WrsPortStatusTable_Object((1,3,6,1,4,1,96,100,7,6))
if mibBuilder.loadTexts:wrsPortStatusTable.setStatus(_B)
_WrsPortStatusEntry_Object=MibTableRow
wrsPortStatusEntry=_WrsPortStatusEntry_Object((1,3,6,1,4,1,96,100,7,6,1))
wrsPortStatusEntry.setIndexNames((0,_M,_l))
if mibBuilder.loadTexts:wrsPortStatusEntry.setStatus(_B)
_WrsPortStatusIndex_Type=Unsigned32
_WrsPortStatusIndex_Object=MibTableColumn
wrsPortStatusIndex=_WrsPortStatusIndex_Object((1,3,6,1,4,1,96,100,7,6,1,1),_WrsPortStatusIndex_Type())
wrsPortStatusIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:wrsPortStatusIndex.setStatus(_B)
class _WrsPortStatusPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_WrsPortStatusPortName_Type.__name__=_F
_WrsPortStatusPortName_Object=MibTableColumn
wrsPortStatusPortName=_WrsPortStatusPortName_Object((1,3,6,1,4,1,96,100,7,6,1,2),_WrsPortStatusPortName_Type())
wrsPortStatusPortName.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusPortName.setStatus(_B)
class _WrsPortStatusLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('down',1),('up',2)))
_WrsPortStatusLink_Type.__name__=_C
_WrsPortStatusLink_Object=MibTableColumn
wrsPortStatusLink=_WrsPortStatusLink_Object((1,3,6,1,4,1,96,100,7,6,1,3),_WrsPortStatusLink_Type())
wrsPortStatusLink.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusLink.setStatus(_B)
class _WrsPortStatusConfiguredMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_i,0),(_R,1),(_S,2),('nonWr',3),('auto',4),(_U,5)))
_WrsPortStatusConfiguredMode_Type.__name__=_C
_WrsPortStatusConfiguredMode_Object=MibTableColumn
wrsPortStatusConfiguredMode=_WrsPortStatusConfiguredMode_Object((1,3,6,1,4,1,96,100,7,6,1,4),_WrsPortStatusConfiguredMode_Type())
wrsPortStatusConfiguredMode.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusConfiguredMode.setStatus(_B)
class _WrsPortStatusLocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('notLocked',1),(_f,2)))
_WrsPortStatusLocked_Type.__name__=_C
_WrsPortStatusLocked_Object=MibTableColumn
wrsPortStatusLocked=_WrsPortStatusLocked_Object((1,3,6,1,4,1,96,100,7,6,1,5),_WrsPortStatusLocked_Type())
wrsPortStatusLocked.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusLocked.setStatus(_B)
class _WrsPortStatusPeer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_WrsPortStatusPeer_Type.__name__=_P
_WrsPortStatusPeer_Object=MibTableColumn
wrsPortStatusPeer=_WrsPortStatusPeer_Object((1,3,6,1,4,1,96,100,7,6,1,6),_WrsPortStatusPeer_Type())
wrsPortStatusPeer.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusPeer.setStatus(_j)
class _WrsPortStatusSfpVN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsPortStatusSfpVN_Type.__name__=_F
_WrsPortStatusSfpVN_Object=MibTableColumn
wrsPortStatusSfpVN=_WrsPortStatusSfpVN_Object((1,3,6,1,4,1,96,100,7,6,1,7),_WrsPortStatusSfpVN_Type())
wrsPortStatusSfpVN.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpVN.setStatus(_B)
class _WrsPortStatusSfpPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsPortStatusSfpPN_Type.__name__=_F
_WrsPortStatusSfpPN_Object=MibTableColumn
wrsPortStatusSfpPN=_WrsPortStatusSfpPN_Object((1,3,6,1,4,1,96,100,7,6,1,8),_WrsPortStatusSfpPN_Type())
wrsPortStatusSfpPN.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpPN.setStatus(_B)
class _WrsPortStatusSfpVS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WrsPortStatusSfpVS_Type.__name__=_F
_WrsPortStatusSfpVS_Object=MibTableColumn
wrsPortStatusSfpVS=_WrsPortStatusSfpVS_Object((1,3,6,1,4,1,96,100,7,6,1,9),_WrsPortStatusSfpVS_Type())
wrsPortStatusSfpVS.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpVS.setStatus(_B)
class _WrsPortStatusSfpInDB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('notInDataBase',1),('inDataBase',2)))
_WrsPortStatusSfpInDB_Type.__name__=_C
_WrsPortStatusSfpInDB_Object=MibTableColumn
wrsPortStatusSfpInDB=_WrsPortStatusSfpInDB_Object((1,3,6,1,4,1,96,100,7,6,1,10),_WrsPortStatusSfpInDB_Type())
wrsPortStatusSfpInDB.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpInDB.setStatus(_B)
class _WrsPortStatusSfpGbE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('linkNotGbE',1),('linkGbE',2)))
_WrsPortStatusSfpGbE_Type.__name__=_C
_WrsPortStatusSfpGbE_Object=MibTableColumn
wrsPortStatusSfpGbE=_WrsPortStatusSfpGbE_Object((1,3,6,1,4,1,96,100,7,6,1,11),_WrsPortStatusSfpGbE_Type())
wrsPortStatusSfpGbE.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpGbE.setStatus(_B)
class _WrsPortStatusSfpError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('sfpOk',1),('sfpError',2),('portDown',3)))
_WrsPortStatusSfpError_Type.__name__=_C
_WrsPortStatusSfpError_Object=MibTableColumn
wrsPortStatusSfpError=_WrsPortStatusSfpError_Object((1,3,6,1,4,1,96,100,7,6,1,12),_WrsPortStatusSfpError_Type())
wrsPortStatusSfpError.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpError.setStatus(_B)
_WrsPortStatusPtpTxFrames_Type=Counter32
_WrsPortStatusPtpTxFrames_Object=MibTableColumn
wrsPortStatusPtpTxFrames=_WrsPortStatusPtpTxFrames_Object((1,3,6,1,4,1,96,100,7,6,1,13),_WrsPortStatusPtpTxFrames_Type())
wrsPortStatusPtpTxFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusPtpTxFrames.setStatus(_B)
_WrsPortStatusPtpRxFrames_Type=Counter32
_WrsPortStatusPtpRxFrames_Object=MibTableColumn
wrsPortStatusPtpRxFrames=_WrsPortStatusPtpRxFrames_Object((1,3,6,1,4,1,96,100,7,6,1,14),_WrsPortStatusPtpRxFrames_Type())
wrsPortStatusPtpRxFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusPtpRxFrames.setStatus(_B)
class _WrsPortStatusMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_m,1),(_n,2)))
_WrsPortStatusMonitor_Type.__name__=_C
_WrsPortStatusMonitor_Object=MibTableColumn
wrsPortStatusMonitor=_WrsPortStatusMonitor_Object((1,3,6,1,4,1,96,100,7,6,1,15),_WrsPortStatusMonitor_Type())
wrsPortStatusMonitor.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusMonitor.setStatus(_B)
class _WrsPortStatusSfpDom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_m,1),(_n,2),('domNotSupported',3)))
_WrsPortStatusSfpDom_Type.__name__=_C
_WrsPortStatusSfpDom_Object=MibTableColumn
wrsPortStatusSfpDom=_WrsPortStatusSfpDom_Object((1,3,6,1,4,1,96,100,7,6,1,16),_WrsPortStatusSfpDom_Type())
wrsPortStatusSfpDom.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpDom.setStatus(_B)
_WrsPortStatusSfpTemp_Type=Integer32
_WrsPortStatusSfpTemp_Object=MibTableColumn
wrsPortStatusSfpTemp=_WrsPortStatusSfpTemp_Object((1,3,6,1,4,1,96,100,7,6,1,17),_WrsPortStatusSfpTemp_Type())
wrsPortStatusSfpTemp.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpTemp.setStatus(_B)
_WrsPortStatusSfpVcc_Type=Integer32
_WrsPortStatusSfpVcc_Object=MibTableColumn
wrsPortStatusSfpVcc=_WrsPortStatusSfpVcc_Object((1,3,6,1,4,1,96,100,7,6,1,18),_WrsPortStatusSfpVcc_Type())
wrsPortStatusSfpVcc.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpVcc.setStatus(_B)
_WrsPortStatusSfpTxBias_Type=Integer32
_WrsPortStatusSfpTxBias_Object=MibTableColumn
wrsPortStatusSfpTxBias=_WrsPortStatusSfpTxBias_Object((1,3,6,1,4,1,96,100,7,6,1,19),_WrsPortStatusSfpTxBias_Type())
wrsPortStatusSfpTxBias.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpTxBias.setStatus(_B)
_WrsPortStatusSfpTxPower_Type=Integer32
_WrsPortStatusSfpTxPower_Object=MibTableColumn
wrsPortStatusSfpTxPower=_WrsPortStatusSfpTxPower_Object((1,3,6,1,4,1,96,100,7,6,1,20),_WrsPortStatusSfpTxPower_Type())
wrsPortStatusSfpTxPower.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpTxPower.setStatus(_B)
_WrsPortStatusSfpRxPower_Type=Integer32
_WrsPortStatusSfpRxPower_Object=MibTableColumn
wrsPortStatusSfpRxPower=_WrsPortStatusSfpRxPower_Object((1,3,6,1,4,1,96,100,7,6,1,21),_WrsPortStatusSfpRxPower_Type())
wrsPortStatusSfpRxPower.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusSfpRxPower.setStatus(_B)
_WrsPortStatusT24p_Type=Integer32
_WrsPortStatusT24p_Object=MibTableColumn
wrsPortStatusT24p=_WrsPortStatusT24p_Object((1,3,6,1,4,1,96,100,7,6,1,22),_WrsPortStatusT24p_Type())
wrsPortStatusT24p.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusT24p.setStatus(_B)
class _WrsPortStatusT24pValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('readFromConfig',1)))
_WrsPortStatusT24pValid_Type.__name__=_C
_WrsPortStatusT24pValid_Object=MibTableColumn
wrsPortStatusT24pValid=_WrsPortStatusT24pValid_Object((1,3,6,1,4,1,96,100,7,6,1,23),_WrsPortStatusT24pValid_Type())
wrsPortStatusT24pValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPortStatusT24pValid.setStatus(_B)
_WrsPstatsHCTable_Object=MibTable
wrsPstatsHCTable=_WrsPstatsHCTable_Object((1,3,6,1,4,1,96,100,7,7))
if mibBuilder.loadTexts:wrsPstatsHCTable.setStatus(_B)
_WrsPstatsHCEntry_Object=MibTableRow
wrsPstatsHCEntry=_WrsPstatsHCEntry_Object((1,3,6,1,4,1,96,100,7,7,1))
wrsPstatsHCEntry.setIndexNames((0,_M,_o))
if mibBuilder.loadTexts:wrsPstatsHCEntry.setStatus(_B)
_WrsPstatsHCIndex_Type=Unsigned32
_WrsPstatsHCIndex_Object=MibTableColumn
wrsPstatsHCIndex=_WrsPstatsHCIndex_Object((1,3,6,1,4,1,96,100,7,7,1,1),_WrsPstatsHCIndex_Type())
wrsPstatsHCIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:wrsPstatsHCIndex.setStatus(_B)
class _WrsPstatsHCPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_WrsPstatsHCPortName_Type.__name__=_F
_WrsPstatsHCPortName_Object=MibTableColumn
wrsPstatsHCPortName=_WrsPstatsHCPortName_Object((1,3,6,1,4,1,96,100,7,7,1,2),_WrsPstatsHCPortName_Type())
wrsPstatsHCPortName.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCPortName.setStatus(_B)
_WrsPstatsHCTXUnderrun_Type=Counter64
_WrsPstatsHCTXUnderrun_Object=MibTableColumn
wrsPstatsHCTXUnderrun=_WrsPstatsHCTXUnderrun_Object((1,3,6,1,4,1,96,100,7,7,1,3),_WrsPstatsHCTXUnderrun_Type())
wrsPstatsHCTXUnderrun.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCTXUnderrun.setStatus(_B)
_WrsPstatsHCRXOverrun_Type=Counter64
_WrsPstatsHCRXOverrun_Object=MibTableColumn
wrsPstatsHCRXOverrun=_WrsPstatsHCRXOverrun_Object((1,3,6,1,4,1,96,100,7,7,1,4),_WrsPstatsHCRXOverrun_Type())
wrsPstatsHCRXOverrun.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXOverrun.setStatus(_B)
_WrsPstatsHCRXInvalidCode_Type=Counter64
_WrsPstatsHCRXInvalidCode_Object=MibTableColumn
wrsPstatsHCRXInvalidCode=_WrsPstatsHCRXInvalidCode_Object((1,3,6,1,4,1,96,100,7,7,1,5),_WrsPstatsHCRXInvalidCode_Type())
wrsPstatsHCRXInvalidCode.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXInvalidCode.setStatus(_B)
_WrsPstatsHCRXSyncLost_Type=Counter64
_WrsPstatsHCRXSyncLost_Object=MibTableColumn
wrsPstatsHCRXSyncLost=_WrsPstatsHCRXSyncLost_Object((1,3,6,1,4,1,96,100,7,7,1,6),_WrsPstatsHCRXSyncLost_Type())
wrsPstatsHCRXSyncLost.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXSyncLost.setStatus(_B)
_WrsPstatsHCRXPauseFrames_Type=Counter64
_WrsPstatsHCRXPauseFrames_Object=MibTableColumn
wrsPstatsHCRXPauseFrames=_WrsPstatsHCRXPauseFrames_Object((1,3,6,1,4,1,96,100,7,7,1,7),_WrsPstatsHCRXPauseFrames_Type())
wrsPstatsHCRXPauseFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPauseFrames.setStatus(_B)
_WrsPstatsHCRXPfilterDropped_Type=Counter64
_WrsPstatsHCRXPfilterDropped_Object=MibTableColumn
wrsPstatsHCRXPfilterDropped=_WrsPstatsHCRXPfilterDropped_Object((1,3,6,1,4,1,96,100,7,7,1,8),_WrsPstatsHCRXPfilterDropped_Type())
wrsPstatsHCRXPfilterDropped.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPfilterDropped.setStatus(_B)
_WrsPstatsHCRXPCSErrors_Type=Counter64
_WrsPstatsHCRXPCSErrors_Object=MibTableColumn
wrsPstatsHCRXPCSErrors=_WrsPstatsHCRXPCSErrors_Object((1,3,6,1,4,1,96,100,7,7,1,9),_WrsPstatsHCRXPCSErrors_Type())
wrsPstatsHCRXPCSErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPCSErrors.setStatus(_B)
_WrsPstatsHCRXGiantFrames_Type=Counter64
_WrsPstatsHCRXGiantFrames_Object=MibTableColumn
wrsPstatsHCRXGiantFrames=_WrsPstatsHCRXGiantFrames_Object((1,3,6,1,4,1,96,100,7,7,1,10),_WrsPstatsHCRXGiantFrames_Type())
wrsPstatsHCRXGiantFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXGiantFrames.setStatus(_B)
_WrsPstatsHCRXRuntFrames_Type=Counter64
_WrsPstatsHCRXRuntFrames_Object=MibTableColumn
wrsPstatsHCRXRuntFrames=_WrsPstatsHCRXRuntFrames_Object((1,3,6,1,4,1,96,100,7,7,1,11),_WrsPstatsHCRXRuntFrames_Type())
wrsPstatsHCRXRuntFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXRuntFrames.setStatus(_B)
_WrsPstatsHCRXCRCErrors_Type=Counter64
_WrsPstatsHCRXCRCErrors_Object=MibTableColumn
wrsPstatsHCRXCRCErrors=_WrsPstatsHCRXCRCErrors_Object((1,3,6,1,4,1,96,100,7,7,1,12),_WrsPstatsHCRXCRCErrors_Type())
wrsPstatsHCRXCRCErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXCRCErrors.setStatus(_B)
_WrsPstatsHCRXPclass0_Type=Counter64
_WrsPstatsHCRXPclass0_Object=MibTableColumn
wrsPstatsHCRXPclass0=_WrsPstatsHCRXPclass0_Object((1,3,6,1,4,1,96,100,7,7,1,13),_WrsPstatsHCRXPclass0_Type())
wrsPstatsHCRXPclass0.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass0.setStatus(_B)
_WrsPstatsHCRXPclass1_Type=Counter64
_WrsPstatsHCRXPclass1_Object=MibTableColumn
wrsPstatsHCRXPclass1=_WrsPstatsHCRXPclass1_Object((1,3,6,1,4,1,96,100,7,7,1,14),_WrsPstatsHCRXPclass1_Type())
wrsPstatsHCRXPclass1.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass1.setStatus(_B)
_WrsPstatsHCRXPclass2_Type=Counter64
_WrsPstatsHCRXPclass2_Object=MibTableColumn
wrsPstatsHCRXPclass2=_WrsPstatsHCRXPclass2_Object((1,3,6,1,4,1,96,100,7,7,1,15),_WrsPstatsHCRXPclass2_Type())
wrsPstatsHCRXPclass2.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass2.setStatus(_B)
_WrsPstatsHCRXPclass3_Type=Counter64
_WrsPstatsHCRXPclass3_Object=MibTableColumn
wrsPstatsHCRXPclass3=_WrsPstatsHCRXPclass3_Object((1,3,6,1,4,1,96,100,7,7,1,16),_WrsPstatsHCRXPclass3_Type())
wrsPstatsHCRXPclass3.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass3.setStatus(_B)
_WrsPstatsHCRXPclass4_Type=Counter64
_WrsPstatsHCRXPclass4_Object=MibTableColumn
wrsPstatsHCRXPclass4=_WrsPstatsHCRXPclass4_Object((1,3,6,1,4,1,96,100,7,7,1,17),_WrsPstatsHCRXPclass4_Type())
wrsPstatsHCRXPclass4.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass4.setStatus(_B)
_WrsPstatsHCRXPclass5_Type=Counter64
_WrsPstatsHCRXPclass5_Object=MibTableColumn
wrsPstatsHCRXPclass5=_WrsPstatsHCRXPclass5_Object((1,3,6,1,4,1,96,100,7,7,1,18),_WrsPstatsHCRXPclass5_Type())
wrsPstatsHCRXPclass5.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass5.setStatus(_B)
_WrsPstatsHCRXPclass6_Type=Counter64
_WrsPstatsHCRXPclass6_Object=MibTableColumn
wrsPstatsHCRXPclass6=_WrsPstatsHCRXPclass6_Object((1,3,6,1,4,1,96,100,7,7,1,19),_WrsPstatsHCRXPclass6_Type())
wrsPstatsHCRXPclass6.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass6.setStatus(_B)
_WrsPstatsHCRXPclass7_Type=Counter64
_WrsPstatsHCRXPclass7_Object=MibTableColumn
wrsPstatsHCRXPclass7=_WrsPstatsHCRXPclass7_Object((1,3,6,1,4,1,96,100,7,7,1,20),_WrsPstatsHCRXPclass7_Type())
wrsPstatsHCRXPclass7.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPclass7.setStatus(_B)
_WrsPstatsHCTXFrames_Type=Counter64
_WrsPstatsHCTXFrames_Object=MibTableColumn
wrsPstatsHCTXFrames=_WrsPstatsHCTXFrames_Object((1,3,6,1,4,1,96,100,7,7,1,21),_WrsPstatsHCTXFrames_Type())
wrsPstatsHCTXFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCTXFrames.setStatus(_B)
_WrsPstatsHCRXFrames_Type=Counter64
_WrsPstatsHCRXFrames_Object=MibTableColumn
wrsPstatsHCRXFrames=_WrsPstatsHCRXFrames_Object((1,3,6,1,4,1,96,100,7,7,1,22),_WrsPstatsHCRXFrames_Type())
wrsPstatsHCRXFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXFrames.setStatus(_B)
_WrsPstatsHCRXDropRTUFull_Type=Counter64
_WrsPstatsHCRXDropRTUFull_Object=MibTableColumn
wrsPstatsHCRXDropRTUFull=_WrsPstatsHCRXDropRTUFull_Object((1,3,6,1,4,1,96,100,7,7,1,23),_WrsPstatsHCRXDropRTUFull_Type())
wrsPstatsHCRXDropRTUFull.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXDropRTUFull.setStatus(_B)
_WrsPstatsHCRXPrio0_Type=Counter64
_WrsPstatsHCRXPrio0_Object=MibTableColumn
wrsPstatsHCRXPrio0=_WrsPstatsHCRXPrio0_Object((1,3,6,1,4,1,96,100,7,7,1,24),_WrsPstatsHCRXPrio0_Type())
wrsPstatsHCRXPrio0.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio0.setStatus(_B)
_WrsPstatsHCRXPrio1_Type=Counter64
_WrsPstatsHCRXPrio1_Object=MibTableColumn
wrsPstatsHCRXPrio1=_WrsPstatsHCRXPrio1_Object((1,3,6,1,4,1,96,100,7,7,1,25),_WrsPstatsHCRXPrio1_Type())
wrsPstatsHCRXPrio1.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio1.setStatus(_B)
_WrsPstatsHCRXPrio2_Type=Counter64
_WrsPstatsHCRXPrio2_Object=MibTableColumn
wrsPstatsHCRXPrio2=_WrsPstatsHCRXPrio2_Object((1,3,6,1,4,1,96,100,7,7,1,26),_WrsPstatsHCRXPrio2_Type())
wrsPstatsHCRXPrio2.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio2.setStatus(_B)
_WrsPstatsHCRXPrio3_Type=Counter64
_WrsPstatsHCRXPrio3_Object=MibTableColumn
wrsPstatsHCRXPrio3=_WrsPstatsHCRXPrio3_Object((1,3,6,1,4,1,96,100,7,7,1,27),_WrsPstatsHCRXPrio3_Type())
wrsPstatsHCRXPrio3.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio3.setStatus(_B)
_WrsPstatsHCRXPrio4_Type=Counter64
_WrsPstatsHCRXPrio4_Object=MibTableColumn
wrsPstatsHCRXPrio4=_WrsPstatsHCRXPrio4_Object((1,3,6,1,4,1,96,100,7,7,1,28),_WrsPstatsHCRXPrio4_Type())
wrsPstatsHCRXPrio4.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio4.setStatus(_B)
_WrsPstatsHCRXPrio5_Type=Counter64
_WrsPstatsHCRXPrio5_Object=MibTableColumn
wrsPstatsHCRXPrio5=_WrsPstatsHCRXPrio5_Object((1,3,6,1,4,1,96,100,7,7,1,29),_WrsPstatsHCRXPrio5_Type())
wrsPstatsHCRXPrio5.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio5.setStatus(_B)
_WrsPstatsHCRXPrio6_Type=Counter64
_WrsPstatsHCRXPrio6_Object=MibTableColumn
wrsPstatsHCRXPrio6=_WrsPstatsHCRXPrio6_Object((1,3,6,1,4,1,96,100,7,7,1,30),_WrsPstatsHCRXPrio6_Type())
wrsPstatsHCRXPrio6.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio6.setStatus(_B)
_WrsPstatsHCRXPrio7_Type=Counter64
_WrsPstatsHCRXPrio7_Object=MibTableColumn
wrsPstatsHCRXPrio7=_WrsPstatsHCRXPrio7_Object((1,3,6,1,4,1,96,100,7,7,1,31),_WrsPstatsHCRXPrio7_Type())
wrsPstatsHCRXPrio7.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRXPrio7.setStatus(_B)
_WrsPstatsHCRTUValid_Type=Counter64
_WrsPstatsHCRTUValid_Object=MibTableColumn
wrsPstatsHCRTUValid=_WrsPstatsHCRTUValid_Object((1,3,6,1,4,1,96,100,7,7,1,32),_WrsPstatsHCRTUValid_Type())
wrsPstatsHCRTUValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRTUValid.setStatus(_B)
_WrsPstatsHCRTUResponses_Type=Counter64
_WrsPstatsHCRTUResponses_Object=MibTableColumn
wrsPstatsHCRTUResponses=_WrsPstatsHCRTUResponses_Object((1,3,6,1,4,1,96,100,7,7,1,33),_WrsPstatsHCRTUResponses_Type())
wrsPstatsHCRTUResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRTUResponses.setStatus(_B)
_WrsPstatsHCRTUDropped_Type=Counter64
_WrsPstatsHCRTUDropped_Object=MibTableColumn
wrsPstatsHCRTUDropped=_WrsPstatsHCRTUDropped_Object((1,3,6,1,4,1,96,100,7,7,1,34),_WrsPstatsHCRTUDropped_Type())
wrsPstatsHCRTUDropped.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCRTUDropped.setStatus(_B)
_WrsPstatsHCFastMatchPriority_Type=Counter64
_WrsPstatsHCFastMatchPriority_Object=MibTableColumn
wrsPstatsHCFastMatchPriority=_WrsPstatsHCFastMatchPriority_Object((1,3,6,1,4,1,96,100,7,7,1,35),_WrsPstatsHCFastMatchPriority_Type())
wrsPstatsHCFastMatchPriority.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCFastMatchPriority.setStatus(_B)
_WrsPstatsHCFastMatchFastForward_Type=Counter64
_WrsPstatsHCFastMatchFastForward_Object=MibTableColumn
wrsPstatsHCFastMatchFastForward=_WrsPstatsHCFastMatchFastForward_Object((1,3,6,1,4,1,96,100,7,7,1,36),_WrsPstatsHCFastMatchFastForward_Type())
wrsPstatsHCFastMatchFastForward.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCFastMatchFastForward.setStatus(_B)
_WrsPstatsHCFastMatchNonForward_Type=Counter64
_WrsPstatsHCFastMatchNonForward_Object=MibTableColumn
wrsPstatsHCFastMatchNonForward=_WrsPstatsHCFastMatchNonForward_Object((1,3,6,1,4,1,96,100,7,7,1,37),_WrsPstatsHCFastMatchNonForward_Type())
wrsPstatsHCFastMatchNonForward.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCFastMatchNonForward.setStatus(_B)
_WrsPstatsHCFastMatchRespValid_Type=Counter64
_WrsPstatsHCFastMatchRespValid_Object=MibTableColumn
wrsPstatsHCFastMatchRespValid=_WrsPstatsHCFastMatchRespValid_Object((1,3,6,1,4,1,96,100,7,7,1,38),_WrsPstatsHCFastMatchRespValid_Type())
wrsPstatsHCFastMatchRespValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCFastMatchRespValid.setStatus(_B)
_WrsPstatsHCFullMatchRespValid_Type=Counter64
_WrsPstatsHCFullMatchRespValid_Object=MibTableColumn
wrsPstatsHCFullMatchRespValid=_WrsPstatsHCFullMatchRespValid_Object((1,3,6,1,4,1,96,100,7,7,1,39),_WrsPstatsHCFullMatchRespValid_Type())
wrsPstatsHCFullMatchRespValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCFullMatchRespValid.setStatus(_B)
_WrsPstatsHCForwarded_Type=Counter64
_WrsPstatsHCForwarded_Object=MibTableColumn
wrsPstatsHCForwarded=_WrsPstatsHCForwarded_Object((1,3,6,1,4,1,96,100,7,7,1,40),_WrsPstatsHCForwarded_Type())
wrsPstatsHCForwarded.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCForwarded.setStatus(_B)
_WrsPstatsHCTRURespValid_Type=Counter64
_WrsPstatsHCTRURespValid_Object=MibTableColumn
wrsPstatsHCTRURespValid=_WrsPstatsHCTRURespValid_Object((1,3,6,1,4,1,96,100,7,7,1,41),_WrsPstatsHCTRURespValid_Type())
wrsPstatsHCTRURespValid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCTRURespValid.setStatus(_B)
_WrsPstatsHCNICTXFrames_Type=Counter64
_WrsPstatsHCNICTXFrames_Object=MibTableColumn
wrsPstatsHCNICTXFrames=_WrsPstatsHCNICTXFrames_Object((1,3,6,1,4,1,96,100,7,7,1,42),_WrsPstatsHCNICTXFrames_Type())
wrsPstatsHCNICTXFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPstatsHCNICTXFrames.setStatus(_B)
_WrsPtpInstanceTable_Object=MibTable
wrsPtpInstanceTable=_WrsPtpInstanceTable_Object((1,3,6,1,4,1,96,100,7,8))
if mibBuilder.loadTexts:wrsPtpInstanceTable.setStatus(_B)
_WrsPtpInstanceEntry_Object=MibTableRow
wrsPtpInstanceEntry=_WrsPtpInstanceEntry_Object((1,3,6,1,4,1,96,100,7,8,1))
wrsPtpInstanceEntry.setIndexNames((0,_M,_p),(0,_M,_q))
if mibBuilder.loadTexts:wrsPtpInstanceEntry.setStatus(_B)
_WrsPtpInstancePortIndex_Type=Unsigned32
_WrsPtpInstancePortIndex_Object=MibTableColumn
wrsPtpInstancePortIndex=_WrsPtpInstancePortIndex_Object((1,3,6,1,4,1,96,100,7,8,1,1),_WrsPtpInstancePortIndex_Type())
wrsPtpInstancePortIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:wrsPtpInstancePortIndex.setStatus(_B)
_WrsPtpInstanceOnPortIndex_Type=Unsigned32
_WrsPtpInstanceOnPortIndex_Object=MibTableColumn
wrsPtpInstanceOnPortIndex=_WrsPtpInstanceOnPortIndex_Object((1,3,6,1,4,1,96,100,7,8,1,2),_WrsPtpInstanceOnPortIndex_Type())
wrsPtpInstanceOnPortIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:wrsPtpInstanceOnPortIndex.setStatus(_B)
class _WrsPtpInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_WrsPtpInstanceName_Type.__name__=_F
_WrsPtpInstanceName_Object=MibTableColumn
wrsPtpInstanceName=_WrsPtpInstanceName_Object((1,3,6,1,4,1,96,100,7,8,1,3),_WrsPtpInstanceName_Type())
wrsPtpInstanceName.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceName.setStatus(_B)
_WrsPtpInstancePort_Type=Integer32
_WrsPtpInstancePort_Object=MibTableColumn
wrsPtpInstancePort=_WrsPtpInstancePort_Object((1,3,6,1,4,1,96,100,7,8,1,4),_WrsPtpInstancePort_Type())
wrsPtpInstancePort.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstancePort.setStatus(_B)
_WrsPtpInstancePortInstance_Type=Integer32
_WrsPtpInstancePortInstance_Object=MibTableColumn
wrsPtpInstancePortInstance=_WrsPtpInstancePortInstance_Object((1,3,6,1,4,1,96,100,7,8,1,5),_WrsPtpInstancePortInstance_Type())
wrsPtpInstancePortInstance.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstancePortInstance.setStatus(_B)
class _WrsPtpInstancePortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_WrsPtpInstancePortName_Type.__name__=_F
_WrsPtpInstancePortName_Object=MibTableColumn
wrsPtpInstancePortName=_WrsPtpInstancePortName_Object((1,3,6,1,4,1,96,100,7,8,1,6),_WrsPtpInstancePortName_Type())
wrsPtpInstancePortName.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstancePortName.setStatus(_B)
class _WrsPtpInstanceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,0),(_r,1),(_s,2),(_K,3),(_t,4),(_u,5),(_R,6),(_v,7),(_w,8),(_S,9)))
_WrsPtpInstanceState_Type.__name__=_C
_WrsPtpInstanceState_Object=MibTableColumn
wrsPtpInstanceState=_WrsPtpInstanceState_Object((1,3,6,1,4,1,96,100,7,8,1,7),_WrsPtpInstanceState_Type())
wrsPtpInstanceState.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceState.setStatus(_B)
class _WrsPtpInstanceMasterOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_K,1),(_x,2)))
_WrsPtpInstanceMasterOnly_Type.__name__=_C
_WrsPtpInstanceMasterOnly_Object=MibTableColumn
wrsPtpInstanceMasterOnly=_WrsPtpInstanceMasterOnly_Object((1,3,6,1,4,1,96,100,7,8,1,8),_WrsPtpInstanceMasterOnly_Type())
wrsPtpInstanceMasterOnly.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceMasterOnly.setStatus(_B)
class _WrsPtpInstanceExtPortCfgDesSt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,0),(_r,1),(_s,2),(_K,3),(_t,4),(_u,5),(_R,6),(_v,7),(_w,8),(_S,9)))
_WrsPtpInstanceExtPortCfgDesSt_Type.__name__=_C
_WrsPtpInstanceExtPortCfgDesSt_Object=MibTableColumn
wrsPtpInstanceExtPortCfgDesSt=_WrsPtpInstanceExtPortCfgDesSt_Object((1,3,6,1,4,1,96,100,7,8,1,9),_WrsPtpInstanceExtPortCfgDesSt_Type())
wrsPtpInstanceExtPortCfgDesSt.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceExtPortCfgDesSt.setStatus(_B)
class _WrsPtpInstanceMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,254)));namedValues=NamedValues(*((_D,0),('e2e',1),('p2p',2),('commonP2P',3),('special',4),('noMechanism',254)))
_WrsPtpInstanceMechanism_Type.__name__=_C
_WrsPtpInstanceMechanism_Object=MibTableColumn
wrsPtpInstanceMechanism=_WrsPtpInstanceMechanism_Object((1,3,6,1,4,1,96,100,7,8,1,10),_WrsPtpInstanceMechanism_Type())
wrsPtpInstanceMechanism.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceMechanism.setStatus(_B)
class _WrsPtpInstanceProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('defaultPTP',1),(_y,2),('highAccuracy',3),('custom',4)))
_WrsPtpInstanceProfile_Type.__name__=_C
_WrsPtpInstanceProfile_Object=MibTableColumn
wrsPtpInstanceProfile=_WrsPtpInstanceProfile_Object((1,3,6,1,4,1,96,100,7,8,1,11),_WrsPtpInstanceProfile_Type())
wrsPtpInstanceProfile.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceProfile.setStatus(_B)
class _WrsPtpInstanceExtension_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_U,1),(_y,2),(_k,3)))
_WrsPtpInstanceExtension_Type.__name__=_C
_WrsPtpInstanceExtension_Object=MibTableColumn
wrsPtpInstanceExtension=_WrsPtpInstanceExtension_Object((1,3,6,1,4,1,96,100,7,8,1,12),_WrsPtpInstanceExtension_Type())
wrsPtpInstanceExtension.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceExtension.setStatus(_B)
class _WrsPtpInstanceAsymEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_K,1),(_x,2)))
_WrsPtpInstanceAsymEnabled_Type.__name__=_C
_WrsPtpInstanceAsymEnabled_Object=MibTableColumn
wrsPtpInstanceAsymEnabled=_WrsPtpInstanceAsymEnabled_Object((1,3,6,1,4,1,96,100,7,8,1,13),_WrsPtpInstanceAsymEnabled_Type())
wrsPtpInstanceAsymEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceAsymEnabled.setStatus(_B)
_WrsPtpInstanceAsymConstAsymPS_Type=Counter64
_WrsPtpInstanceAsymConstAsymPS_Object=MibTableColumn
wrsPtpInstanceAsymConstAsymPS=_WrsPtpInstanceAsymConstAsymPS_Object((1,3,6,1,4,1,96,100,7,8,1,14),_WrsPtpInstanceAsymConstAsymPS_Type())
wrsPtpInstanceAsymConstAsymPS.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceAsymConstAsymPS.setStatus(_B)
_WrsPtpInstanceAsymScDelayCoef_Type=Counter64
_WrsPtpInstanceAsymScDelayCoef_Object=MibTableColumn
wrsPtpInstanceAsymScDelayCoef=_WrsPtpInstanceAsymScDelayCoef_Object((1,3,6,1,4,1,96,100,7,8,1,15),_WrsPtpInstanceAsymScDelayCoef_Type())
wrsPtpInstanceAsymScDelayCoef.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceAsymScDelayCoef.setStatus(_B)
class _WrsPtpInstanceAsymScDelayCoefHR_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WrsPtpInstanceAsymScDelayCoefHR_Type.__name__=_F
_WrsPtpInstanceAsymScDelayCoefHR_Object=MibTableColumn
wrsPtpInstanceAsymScDelayCoefHR=_WrsPtpInstanceAsymScDelayCoefHR_Object((1,3,6,1,4,1,96,100,7,8,1,16),_WrsPtpInstanceAsymScDelayCoefHR_Type())
wrsPtpInstanceAsymScDelayCoefHR.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceAsymScDelayCoefHR.setStatus(_B)
_WrsPtpInstanceTSCorrEgressLatPS_Type=Counter64
_WrsPtpInstanceTSCorrEgressLatPS_Object=MibTableColumn
wrsPtpInstanceTSCorrEgressLatPS=_WrsPtpInstanceTSCorrEgressLatPS_Object((1,3,6,1,4,1,96,100,7,8,1,17),_WrsPtpInstanceTSCorrEgressLatPS_Type())
wrsPtpInstanceTSCorrEgressLatPS.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceTSCorrEgressLatPS.setStatus(_B)
_WrsPtpInstanceTSCorrIngLatPS_Type=Counter64
_WrsPtpInstanceTSCorrIngLatPS_Object=MibTableColumn
wrsPtpInstanceTSCorrIngLatPS=_WrsPtpInstanceTSCorrIngLatPS_Object((1,3,6,1,4,1,96,100,7,8,1,18),_WrsPtpInstanceTSCorrIngLatPS_Type())
wrsPtpInstanceTSCorrIngLatPS.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceTSCorrIngLatPS.setStatus(_B)
_WrsPtpInstanceTSCorrSemistLatPS_Type=Counter64
_WrsPtpInstanceTSCorrSemistLatPS_Object=MibTableColumn
wrsPtpInstanceTSCorrSemistLatPS=_WrsPtpInstanceTSCorrSemistLatPS_Object((1,3,6,1,4,1,96,100,7,8,1,19),_WrsPtpInstanceTSCorrSemistLatPS_Type())
wrsPtpInstanceTSCorrSemistLatPS.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceTSCorrSemistLatPS.setStatus(_B)
class _WrsPtpInstanceProtoDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),(_U,1),('pWaitMsg',2),('pDetection',3),('pDetected',4),('pFailure',5)))
_WrsPtpInstanceProtoDetectState_Type.__name__=_C
_WrsPtpInstanceProtoDetectState_Object=MibTableColumn
wrsPtpInstanceProtoDetectState=_WrsPtpInstanceProtoDetectState_Object((1,3,6,1,4,1,96,100,7,8,1,20),_WrsPtpInstanceProtoDetectState_Type())
wrsPtpInstanceProtoDetectState.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceProtoDetectState.setStatus(_B)
class _WrsPtpInstanceExtState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_K,1),('active',2),('ptp',3)))
_WrsPtpInstanceExtState_Type.__name__=_C
_WrsPtpInstanceExtState_Object=MibTableColumn
wrsPtpInstanceExtState=_WrsPtpInstanceExtState_Object((1,3,6,1,4,1,96,100,7,8,1,21),_WrsPtpInstanceExtState_Type())
wrsPtpInstanceExtState.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceExtState.setStatus(_B)
_WrsPtpInstancePeerMac_Type=PhysAddress
_WrsPtpInstancePeerMac_Object=MibTableColumn
wrsPtpInstancePeerMac=_WrsPtpInstancePeerMac_Object((1,3,6,1,4,1,96,100,7,8,1,22),_WrsPtpInstancePeerMac_Type())
wrsPtpInstancePeerMac.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstancePeerMac.setStatus(_B)
_WrsPtpInstancePeerVid_Type=Integer32
_WrsPtpInstancePeerVid_Object=MibTableColumn
wrsPtpInstancePeerVid=_WrsPtpInstancePeerVid_Object((1,3,6,1,4,1,96,100,7,8,1,23),_WrsPtpInstancePeerVid_Type())
wrsPtpInstancePeerVid.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstancePeerVid.setStatus(_B)
_WrsPtpInstanceVlanNum_Type=Integer32
_WrsPtpInstanceVlanNum_Object=MibTableColumn
wrsPtpInstanceVlanNum=_WrsPtpInstanceVlanNum_Object((1,3,6,1,4,1,96,100,7,8,1,24),_WrsPtpInstanceVlanNum_Type())
wrsPtpInstanceVlanNum.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceVlanNum.setStatus(_B)
class _WrsPtpInstanceVlanListStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_WrsPtpInstanceVlanListStr_Type.__name__=_F
_WrsPtpInstanceVlanListStr_Object=MibTableColumn
wrsPtpInstanceVlanListStr=_WrsPtpInstanceVlanListStr_Object((1,3,6,1,4,1,96,100,7,8,1,25),_WrsPtpInstanceVlanListStr_Type())
wrsPtpInstanceVlanListStr.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceVlanListStr.setStatus(_B)
class _WrsPtpInstanceStatusError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_H,1),(_G,2),(_I,3)))
_WrsPtpInstanceStatusError_Type.__name__=_C
_WrsPtpInstanceStatusError_Object=MibTableColumn
wrsPtpInstanceStatusError=_WrsPtpInstanceStatusError_Object((1,3,6,1,4,1,96,100,7,8,1,26),_WrsPtpInstanceStatusError_Type())
wrsPtpInstanceStatusError.setMaxAccess(_A)
if mibBuilder.loadTexts:wrsPtpInstanceStatusError.setStatus(_B)
_WrsId_ObjectIdentity=ObjectIdentity
wrsId=_WrsId_ObjectIdentity((1,3,6,1,4,1,96,100,1000))
_WrsIdUnkn_ObjectIdentity=ObjectIdentity
wrsIdUnkn=_WrsIdUnkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,1))
_WrsIdUnknUnkn_ObjectIdentity=ObjectIdentity
wrsIdUnknUnkn=_WrsIdUnknUnkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,1,1))
_WrsIdOther_ObjectIdentity=ObjectIdentity
wrsIdOther=_WrsIdOther_ObjectIdentity((1,3,6,1,4,1,96,100,1000,2))
_WrsId3_ObjectIdentity=ObjectIdentity
wrsId3=_WrsId3_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3))
_WrsId3Unkn_ObjectIdentity=ObjectIdentity
wrsId3Unkn=_WrsId3Unkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,1))
_WrsId3UnknUnkn_ObjectIdentity=ObjectIdentity
wrsId3UnknUnkn=_WrsId3UnknUnkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,1,1))
_WrsId3Unkn3_ObjectIdentity=ObjectIdentity
wrsId3Unkn3=_WrsId3Unkn3_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,1,3))
_WrsId3Unkn4_ObjectIdentity=ObjectIdentity
wrsId3Unkn4=_WrsId3Unkn4_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,1,4))
_WrsId3UnknFL_ObjectIdentity=ObjectIdentity
wrsId3UnknFL=_WrsId3UnknFL_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,1,5))
_WrsId3Ssol_ObjectIdentity=ObjectIdentity
wrsId3Ssol=_WrsId3Ssol_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,2))
_WrsId3SsolUnkn_ObjectIdentity=ObjectIdentity
wrsId3SsolUnkn=_WrsId3SsolUnkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,2,1))
_WrsId3Ssol3_ObjectIdentity=ObjectIdentity
wrsId3Ssol3=_WrsId3Ssol3_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,2,3))
_WrsId3Ssol4_ObjectIdentity=ObjectIdentity
wrsId3Ssol4=_WrsId3Ssol4_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,2,4))
_WrsId3Cti_ObjectIdentity=ObjectIdentity
wrsId3Cti=_WrsId3Cti_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,3))
_WrsId3CtiUnkn_ObjectIdentity=ObjectIdentity
wrsId3CtiUnkn=_WrsId3CtiUnkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,3,1))
_WrsId3Cti3_ObjectIdentity=ObjectIdentity
wrsId3Cti3=_WrsId3Cti3_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,3,3))
_WrsId3Cti4_ObjectIdentity=ObjectIdentity
wrsId3Cti4=_WrsId3Cti4_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,3,4))
_WrsId3St_ObjectIdentity=ObjectIdentity
wrsId3St=_WrsId3St_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,4))
_WrsId3StUnkn_ObjectIdentity=ObjectIdentity
wrsId3StUnkn=_WrsId3StUnkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,4,1))
_WrsId3St3_ObjectIdentity=ObjectIdentity
wrsId3St3=_WrsId3St3_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,4,3))
_WrsId3St4_ObjectIdentity=ObjectIdentity
wrsId3St4=_WrsId3St4_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,4,4))
_WrsId3StFL_ObjectIdentity=ObjectIdentity
wrsId3StFL=_WrsId3StFL_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,4,5))
_WrsId3Opnt_ObjectIdentity=ObjectIdentity
wrsId3Opnt=_WrsId3Opnt_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,5))
_WrsId3OpntUnkn_ObjectIdentity=ObjectIdentity
wrsId3OpntUnkn=_WrsId3OpntUnkn_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,5,1))
_WrsId3Opnt3_ObjectIdentity=ObjectIdentity
wrsId3Opnt3=_WrsId3Opnt3_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,5,3))
_WrsId3Opnt4_ObjectIdentity=ObjectIdentity
wrsId3Opnt4=_WrsId3Opnt4_ObjectIdentity((1,3,6,1,4,1,96,100,1000,3,5,4))
mibBuilder.exportSymbols(_M,**{'cern':cern,'wrSwitchMIB':wrSwitchMIB,'wrsScalar':wrsScalar,'wrsScalarOne':wrsScalarOne,'wrsStatus':wrsStatus,'wrsGeneralStatusGroup':wrsGeneralStatusGroup,'wrsMainSystemStatus':wrsMainSystemStatus,'wrsOSStatus':wrsOSStatus,'wrsTimingStatus':wrsTimingStatus,'wrsNetworkingStatus':wrsNetworkingStatus,'wrsDetailedStatusesGroup':wrsDetailedStatusesGroup,'wrsOSStatusGroup':wrsOSStatusGroup,'wrsBootSuccessful':wrsBootSuccessful,'wrsTemperatureWarning':wrsTemperatureWarning,'wrsMemoryFreeLow':wrsMemoryFreeLow,'wrsCpuLoadHigh':wrsCpuLoadHigh,'wrsDiskSpaceLow':wrsDiskSpaceLow,'wrsTimingStatusGroup':wrsTimingStatusGroup,'wrsPTPStatus':wrsPTPStatus,'wrsSoftPLLStatus':wrsSoftPLLStatus,'wrsSlaveLinksStatus':wrsSlaveLinksStatus,'wrsPTPFramesFlowing':wrsPTPFramesFlowing,'wrsSystemClockStatus':wrsSystemClockStatus,'wrsNetworkingStatusGroup':wrsNetworkingStatusGroup,'wrsSFPsStatus':wrsSFPsStatus,'wrsEndpointStatus':wrsEndpointStatus,'wrsSwcoreStatus':wrsSwcoreStatus,'wrsRTUStatus':wrsRTUStatus,'wrsVersionGroup':wrsVersionGroup,'wrsVersionSwVersion':wrsVersionSwVersion,'wrsVersionSwBuildBy':wrsVersionSwBuildBy,'wrsVersionSwBuildDate':wrsVersionSwBuildDate,'wrsVersionBackplaneVersion':wrsVersionBackplaneVersion,'wrsVersionFpgaType':wrsVersionFpgaType,'wrsVersionManufacturer':wrsVersionManufacturer,'wrsVersionSwitchSerialNumber':wrsVersionSwitchSerialNumber,'wrsVersionScbVersion':wrsVersionScbVersion,'wrsVersionGwVersion':wrsVersionGwVersion,'wrsVersionGwBuild':wrsVersionGwBuild,'wrsVersionSwitchHdlCommitId':wrsVersionSwitchHdlCommitId,'wrsVersionGeneralCoresCommitId':wrsVersionGeneralCoresCommitId,'wrsVersionWrCoresCommitId':wrsVersionWrCoresCommitId,'wrsVersionLastUpdateDate':wrsVersionLastUpdateDate,'wrsVersionFeatures':wrsVersionFeatures,'wrsExpertStatus':wrsExpertStatus,'wrsOperationStatus':wrsOperationStatus,'wrsCurrentTimeGroup':wrsCurrentTimeGroup,'wrsDateTAI':wrsDateTAI,'wrsDateTAIString':wrsDateTAIString,'wrsSystemClockStatusDetails':wrsSystemClockStatusDetails,'wrsSystemClockDrift':wrsSystemClockDrift,'wrsSystemClockDriftThreshold':wrsSystemClockDriftThreshold,'wrsSystemClockCheckInterval':wrsSystemClockCheckInterval,'wrsSystemClockCheckIntervalUnit':wrsSystemClockCheckIntervalUnit,'wrsLeapSecSource':wrsLeapSecSource,'wrsLeapSecStatusDetails':wrsLeapSecStatusDetails,'wrsLeapSecSourceStatusDetails':wrsLeapSecSourceStatusDetails,'wrsLeapSecSourceURL':wrsLeapSecSourceURL,'wrsSystemClockDriftUs':wrsSystemClockDriftUs,'wrsBootStatusGroup':wrsBootStatusGroup,'wrsBootCnt':wrsBootCnt,'wrsRebootCnt':wrsRebootCnt,'wrsRestartReason':wrsRestartReason,'wrsFaultIP':wrsFaultIP,'wrsFaultLR':wrsFaultLR,'wrsConfigSource':wrsConfigSource,'wrsConfigSourceUrl':wrsConfigSourceUrl,'wrsRestartReasonMonit':wrsRestartReasonMonit,'wrsBootConfigStatus':wrsBootConfigStatus,'wrsBootHwinfoReadout':wrsBootHwinfoReadout,'wrsBootLoadFPGA':wrsBootLoadFPGA,'wrsBootLoadLM32':wrsBootLoadLM32,'wrsBootKernelModulesMissing':wrsBootKernelModulesMissing,'wrsBootUserspaceDaemonsMissing':wrsBootUserspaceDaemonsMissing,'wrsGwWatchdogTimeouts':wrsGwWatchdogTimeouts,'wrsFwUpdateStatus':wrsFwUpdateStatus,'wrsCustomBootScriptSource':wrsCustomBootScriptSource,'wrsCustomBootScriptSourceUrl':wrsCustomBootScriptSourceUrl,'wrsCustomBootScriptStatus':wrsCustomBootScriptStatus,'wrsAuxClkSetStatus':wrsAuxClkSetStatus,'wrsThrottlingSetStatus':wrsThrottlingSetStatus,'wrsVlansSetStatus':wrsVlansSetStatus,'wrsTemperatureGroup':wrsTemperatureGroup,'wrsTempFPGA':wrsTempFPGA,'wrsTempPLL':wrsTempPLL,'wrsTempPSL':wrsTempPSL,'wrsTempPSR':wrsTempPSR,'wrsTempThresholdFPGA':wrsTempThresholdFPGA,'wrsTempThresholdPLL':wrsTempThresholdPLL,'wrsTempThresholdPSL':wrsTempThresholdPSL,'wrsTempThresholdPSR':wrsTempThresholdPSR,'wrsMemoryGroup':wrsMemoryGroup,'wrsMemoryTotal':wrsMemoryTotal,'wrsMemoryUsed':wrsMemoryUsed,'wrsMemoryUsedPerc':wrsMemoryUsedPerc,'wrsMemoryFree':wrsMemoryFree,'wrsCpuLoadGroup':wrsCpuLoadGroup,'wrsCPULoadAvg1min':wrsCPULoadAvg1min,'wrsCPULoadAvg5min':wrsCPULoadAvg5min,'wrsCPULoadAvg15min':wrsCPULoadAvg15min,'wrsDiskTable':wrsDiskTable,'wrsDiskEntry':wrsDiskEntry,_c:wrsDiskIndex,'wrsDiskMountPath':wrsDiskMountPath,'wrsDiskSize':wrsDiskSize,'wrsDiskUsed':wrsDiskUsed,'wrsDiskFree':wrsDiskFree,'wrsDiskUseRate':wrsDiskUseRate,'wrsDiskFilesystem':wrsDiskFilesystem,'wrsStartCntGroup':wrsStartCntGroup,'wrsStartCntHAL':wrsStartCntHAL,'wrsStartCntPTP':wrsStartCntPTP,'wrsStartCntRTUd':wrsStartCntRTUd,'wrsStartCntSshd':wrsStartCntSshd,'wrsStartCntHttpd':wrsStartCntHttpd,'wrsStartCntSnmpd':wrsStartCntSnmpd,'wrsStartCntSyslogd':wrsStartCntSyslogd,'wrsStartCntWrsWatchdog':wrsStartCntWrsWatchdog,'wrsStartCntLldpd':wrsStartCntLldpd,'wrsStartCntLdap':wrsStartCntLdap,'wrsStartCntRvlan':wrsStartCntRvlan,'wrsSpllState':wrsSpllState,'wrsSpllVersionGroup':wrsSpllVersionGroup,'wrsSpllVersion':wrsSpllVersion,'wrsSpllBuildDate':wrsSpllBuildDate,'wrsSpllBuildBy':wrsSpllBuildBy,'wrsSpllStatusGroup':wrsSpllStatusGroup,'wrsSpllMode':wrsSpllMode,'wrsSpllIrqCnt':wrsSpllIrqCnt,'wrsSpllSeqState':wrsSpllSeqState,'wrsSpllAlignState':wrsSpllAlignState,'wrsSpllHlock':wrsSpllHlock,'wrsSpllMlock':wrsSpllMlock,'wrsSpllHY':wrsSpllHY,'wrsSpllMY':wrsSpllMY,'wrsSpllDelCnt':wrsSpllDelCnt,'wrsPstatsTable':wrsPstatsTable,'wrsPstatsEntry':wrsPstatsEntry,_g:wrsPstatsIndex,'wrsPstatsPortName':wrsPstatsPortName,'wrsPstatsTXUnderrun':wrsPstatsTXUnderrun,'wrsPstatsRXOverrun':wrsPstatsRXOverrun,'wrsPstatsRXInvalidCode':wrsPstatsRXInvalidCode,'wrsPstatsRXSyncLost':wrsPstatsRXSyncLost,'wrsPstatsRXPauseFrames':wrsPstatsRXPauseFrames,'wrsPstatsRXPfilterDropped':wrsPstatsRXPfilterDropped,'wrsPstatsRXPCSErrors':wrsPstatsRXPCSErrors,'wrsPstatsRXGiantFrames':wrsPstatsRXGiantFrames,'wrsPstatsRXRuntFrames':wrsPstatsRXRuntFrames,'wrsPstatsRXCRCErrors':wrsPstatsRXCRCErrors,'wrsPstatsRXPclass0':wrsPstatsRXPclass0,'wrsPstatsRXPclass1':wrsPstatsRXPclass1,'wrsPstatsRXPclass2':wrsPstatsRXPclass2,'wrsPstatsRXPclass3':wrsPstatsRXPclass3,'wrsPstatsRXPclass4':wrsPstatsRXPclass4,'wrsPstatsRXPclass5':wrsPstatsRXPclass5,'wrsPstatsRXPclass6':wrsPstatsRXPclass6,'wrsPstatsRXPclass7':wrsPstatsRXPclass7,'wrsPstatsTXFrames':wrsPstatsTXFrames,'wrsPstatsRXFrames':wrsPstatsRXFrames,'wrsPstatsRXDropRTUFull':wrsPstatsRXDropRTUFull,'wrsPstatsRXPrio0':wrsPstatsRXPrio0,'wrsPstatsRXPrio1':wrsPstatsRXPrio1,'wrsPstatsRXPrio2':wrsPstatsRXPrio2,'wrsPstatsRXPrio3':wrsPstatsRXPrio3,'wrsPstatsRXPrio4':wrsPstatsRXPrio4,'wrsPstatsRXPrio5':wrsPstatsRXPrio5,'wrsPstatsRXPrio6':wrsPstatsRXPrio6,'wrsPstatsRXPrio7':wrsPstatsRXPrio7,'wrsPstatsRTUValid':wrsPstatsRTUValid,'wrsPstatsRTUResponses':wrsPstatsRTUResponses,'wrsPstatsRTUDropped':wrsPstatsRTUDropped,'wrsPstatsFastMatchPriority':wrsPstatsFastMatchPriority,'wrsPstatsFastMatchFastForward':wrsPstatsFastMatchFastForward,'wrsPstatsFastMatchNonForward':wrsPstatsFastMatchNonForward,'wrsPstatsFastMatchRespValid':wrsPstatsFastMatchRespValid,'wrsPstatsFullMatchRespValid':wrsPstatsFullMatchRespValid,'wrsPstatsForwarded':wrsPstatsForwarded,'wrsPstatsTRURespValid':wrsPstatsTRURespValid,'wrsPtpDataTable':wrsPtpDataTable,'wrsPtpDataEntry':wrsPtpDataEntry,_h:wrsPtpDataIndex,'wrsPtpPortName':wrsPtpPortName,'wrsPtpGrandmasterID':wrsPtpGrandmasterID,'wrsPtpOwnID':wrsPtpOwnID,'wrsPtpMode':wrsPtpMode,'wrsPtpServoState':wrsPtpServoState,'wrsPtpServoStateN':wrsPtpServoStateN,'wrsPtpPhaseTracking':wrsPtpPhaseTracking,'wrsPtpSyncSource':wrsPtpSyncSource,'wrsPtpClockOffsetPs':wrsPtpClockOffsetPs,'wrsPtpClockOffsetPsHR':wrsPtpClockOffsetPsHR,'wrsPtpSkew':wrsPtpSkew,'wrsPtpRTT':wrsPtpRTT,'wrsPtpLinkLength':wrsPtpLinkLength,'wrsPtpServoUpdates':wrsPtpServoUpdates,'wrsPtpDeltaTxM':wrsPtpDeltaTxM,'wrsPtpDeltaRxM':wrsPtpDeltaRxM,'wrsPtpDeltaTxS':wrsPtpDeltaTxS,'wrsPtpDeltaRxS':wrsPtpDeltaRxS,'wrsPtpServoStateErrCnt':wrsPtpServoStateErrCnt,'wrsPtpClockOffsetErrCnt':wrsPtpClockOffsetErrCnt,'wrsPtpRTTErrCnt':wrsPtpRTTErrCnt,'wrsPtpServoUpdateTime':wrsPtpServoUpdateTime,'wrsPtpServoExt':wrsPtpServoExt,'wrsPortStatusTable':wrsPortStatusTable,'wrsPortStatusEntry':wrsPortStatusEntry,_l:wrsPortStatusIndex,'wrsPortStatusPortName':wrsPortStatusPortName,'wrsPortStatusLink':wrsPortStatusLink,'wrsPortStatusConfiguredMode':wrsPortStatusConfiguredMode,'wrsPortStatusLocked':wrsPortStatusLocked,'wrsPortStatusPeer':wrsPortStatusPeer,'wrsPortStatusSfpVN':wrsPortStatusSfpVN,'wrsPortStatusSfpPN':wrsPortStatusSfpPN,'wrsPortStatusSfpVS':wrsPortStatusSfpVS,'wrsPortStatusSfpInDB':wrsPortStatusSfpInDB,'wrsPortStatusSfpGbE':wrsPortStatusSfpGbE,'wrsPortStatusSfpError':wrsPortStatusSfpError,'wrsPortStatusPtpTxFrames':wrsPortStatusPtpTxFrames,'wrsPortStatusPtpRxFrames':wrsPortStatusPtpRxFrames,'wrsPortStatusMonitor':wrsPortStatusMonitor,'wrsPortStatusSfpDom':wrsPortStatusSfpDom,'wrsPortStatusSfpTemp':wrsPortStatusSfpTemp,'wrsPortStatusSfpVcc':wrsPortStatusSfpVcc,'wrsPortStatusSfpTxBias':wrsPortStatusSfpTxBias,'wrsPortStatusSfpTxPower':wrsPortStatusSfpTxPower,'wrsPortStatusSfpRxPower':wrsPortStatusSfpRxPower,'wrsPortStatusT24p':wrsPortStatusT24p,'wrsPortStatusT24pValid':wrsPortStatusT24pValid,'wrsPstatsHCTable':wrsPstatsHCTable,'wrsPstatsHCEntry':wrsPstatsHCEntry,_o:wrsPstatsHCIndex,'wrsPstatsHCPortName':wrsPstatsHCPortName,'wrsPstatsHCTXUnderrun':wrsPstatsHCTXUnderrun,'wrsPstatsHCRXOverrun':wrsPstatsHCRXOverrun,'wrsPstatsHCRXInvalidCode':wrsPstatsHCRXInvalidCode,'wrsPstatsHCRXSyncLost':wrsPstatsHCRXSyncLost,'wrsPstatsHCRXPauseFrames':wrsPstatsHCRXPauseFrames,'wrsPstatsHCRXPfilterDropped':wrsPstatsHCRXPfilterDropped,'wrsPstatsHCRXPCSErrors':wrsPstatsHCRXPCSErrors,'wrsPstatsHCRXGiantFrames':wrsPstatsHCRXGiantFrames,'wrsPstatsHCRXRuntFrames':wrsPstatsHCRXRuntFrames,'wrsPstatsHCRXCRCErrors':wrsPstatsHCRXCRCErrors,'wrsPstatsHCRXPclass0':wrsPstatsHCRXPclass0,'wrsPstatsHCRXPclass1':wrsPstatsHCRXPclass1,'wrsPstatsHCRXPclass2':wrsPstatsHCRXPclass2,'wrsPstatsHCRXPclass3':wrsPstatsHCRXPclass3,'wrsPstatsHCRXPclass4':wrsPstatsHCRXPclass4,'wrsPstatsHCRXPclass5':wrsPstatsHCRXPclass5,'wrsPstatsHCRXPclass6':wrsPstatsHCRXPclass6,'wrsPstatsHCRXPclass7':wrsPstatsHCRXPclass7,'wrsPstatsHCTXFrames':wrsPstatsHCTXFrames,'wrsPstatsHCRXFrames':wrsPstatsHCRXFrames,'wrsPstatsHCRXDropRTUFull':wrsPstatsHCRXDropRTUFull,'wrsPstatsHCRXPrio0':wrsPstatsHCRXPrio0,'wrsPstatsHCRXPrio1':wrsPstatsHCRXPrio1,'wrsPstatsHCRXPrio2':wrsPstatsHCRXPrio2,'wrsPstatsHCRXPrio3':wrsPstatsHCRXPrio3,'wrsPstatsHCRXPrio4':wrsPstatsHCRXPrio4,'wrsPstatsHCRXPrio5':wrsPstatsHCRXPrio5,'wrsPstatsHCRXPrio6':wrsPstatsHCRXPrio6,'wrsPstatsHCRXPrio7':wrsPstatsHCRXPrio7,'wrsPstatsHCRTUValid':wrsPstatsHCRTUValid,'wrsPstatsHCRTUResponses':wrsPstatsHCRTUResponses,'wrsPstatsHCRTUDropped':wrsPstatsHCRTUDropped,'wrsPstatsHCFastMatchPriority':wrsPstatsHCFastMatchPriority,'wrsPstatsHCFastMatchFastForward':wrsPstatsHCFastMatchFastForward,'wrsPstatsHCFastMatchNonForward':wrsPstatsHCFastMatchNonForward,'wrsPstatsHCFastMatchRespValid':wrsPstatsHCFastMatchRespValid,'wrsPstatsHCFullMatchRespValid':wrsPstatsHCFullMatchRespValid,'wrsPstatsHCForwarded':wrsPstatsHCForwarded,'wrsPstatsHCTRURespValid':wrsPstatsHCTRURespValid,'wrsPstatsHCNICTXFrames':wrsPstatsHCNICTXFrames,'wrsPtpInstanceTable':wrsPtpInstanceTable,'wrsPtpInstanceEntry':wrsPtpInstanceEntry,_p:wrsPtpInstancePortIndex,_q:wrsPtpInstanceOnPortIndex,'wrsPtpInstanceName':wrsPtpInstanceName,'wrsPtpInstancePort':wrsPtpInstancePort,'wrsPtpInstancePortInstance':wrsPtpInstancePortInstance,'wrsPtpInstancePortName':wrsPtpInstancePortName,'wrsPtpInstanceState':wrsPtpInstanceState,'wrsPtpInstanceMasterOnly':wrsPtpInstanceMasterOnly,'wrsPtpInstanceExtPortCfgDesSt':wrsPtpInstanceExtPortCfgDesSt,'wrsPtpInstanceMechanism':wrsPtpInstanceMechanism,'wrsPtpInstanceProfile':wrsPtpInstanceProfile,'wrsPtpInstanceExtension':wrsPtpInstanceExtension,'wrsPtpInstanceAsymEnabled':wrsPtpInstanceAsymEnabled,'wrsPtpInstanceAsymConstAsymPS':wrsPtpInstanceAsymConstAsymPS,'wrsPtpInstanceAsymScDelayCoef':wrsPtpInstanceAsymScDelayCoef,'wrsPtpInstanceAsymScDelayCoefHR':wrsPtpInstanceAsymScDelayCoefHR,'wrsPtpInstanceTSCorrEgressLatPS':wrsPtpInstanceTSCorrEgressLatPS,'wrsPtpInstanceTSCorrIngLatPS':wrsPtpInstanceTSCorrIngLatPS,'wrsPtpInstanceTSCorrSemistLatPS':wrsPtpInstanceTSCorrSemistLatPS,'wrsPtpInstanceProtoDetectState':wrsPtpInstanceProtoDetectState,'wrsPtpInstanceExtState':wrsPtpInstanceExtState,'wrsPtpInstancePeerMac':wrsPtpInstancePeerMac,'wrsPtpInstancePeerVid':wrsPtpInstancePeerVid,'wrsPtpInstanceVlanNum':wrsPtpInstanceVlanNum,'wrsPtpInstanceVlanListStr':wrsPtpInstanceVlanListStr,'wrsPtpInstanceStatusError':wrsPtpInstanceStatusError,'wrsId':wrsId,'wrsIdUnkn':wrsIdUnkn,'wrsIdUnknUnkn':wrsIdUnknUnkn,'wrsIdOther':wrsIdOther,'wrsId3':wrsId3,'wrsId3Unkn':wrsId3Unkn,'wrsId3UnknUnkn':wrsId3UnknUnkn,'wrsId3Unkn3':wrsId3Unkn3,'wrsId3Unkn4':wrsId3Unkn4,'wrsId3UnknFL':wrsId3UnknFL,'wrsId3Ssol':wrsId3Ssol,'wrsId3SsolUnkn':wrsId3SsolUnkn,'wrsId3Ssol3':wrsId3Ssol3,'wrsId3Ssol4':wrsId3Ssol4,'wrsId3Cti':wrsId3Cti,'wrsId3CtiUnkn':wrsId3CtiUnkn,'wrsId3Cti3':wrsId3Cti3,'wrsId3Cti4':wrsId3Cti4,'wrsId3St':wrsId3St,'wrsId3StUnkn':wrsId3StUnkn,'wrsId3St3':wrsId3St3,'wrsId3St4':wrsId3St4,'wrsId3StFL':wrsId3StFL,'wrsId3Opnt':wrsId3Opnt,'wrsId3OpntUnkn':wrsId3OpntUnkn,'wrsId3Opnt3':wrsId3Opnt3,'wrsId3Opnt4':wrsId3Opnt4})