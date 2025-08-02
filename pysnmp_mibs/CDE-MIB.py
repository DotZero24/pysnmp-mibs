_E='NotificationType'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
TruthValue,rdwrConfigurationSync=mibBuilder.importSymbols('RADWARE-MIB','TruthValue','rdwrConfigurationSync')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_RdwrConfigurationSyncMonitor_ObjectIdentity=ObjectIdentity
rdwrConfigurationSyncMonitor=_RdwrConfigurationSyncMonitor_ObjectIdentity((1,3,6,1,4,1,89,35,1,161,1))
class _RdwrConfSyncState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('syncOff',1),('disconnected',2),('synchronizing',3),('inSync',4),('incompatible',5),('cannotSync',6),('pendingVRRPSwitch',7),('noMaster',8),('masterConnected',9),('outOfSync',10)))
_RdwrConfSyncState_Type.__name__=_D
_RdwrConfSyncState_Object=MibScalar
rdwrConfSyncState=_RdwrConfSyncState_Object((1,3,6,1,4,1,89,35,1,161,1,1),_RdwrConfSyncState_Type())
rdwrConfSyncState.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncState.setStatus(_A)
_RdwrConfSyncIP_Type=IpAddress
_RdwrConfSyncIP_Object=MibScalar
rdwrConfSyncIP=_RdwrConfSyncIP_Object((1,3,6,1,4,1,89,35,1,161,1,2),_RdwrConfSyncIP_Type())
rdwrConfSyncIP.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncIP.setStatus(_A)
_RdwrConfSyncPeerIP_Type=IpAddress
_RdwrConfSyncPeerIP_Object=MibScalar
rdwrConfSyncPeerIP=_RdwrConfSyncPeerIP_Object((1,3,6,1,4,1,89,35,1,161,1,3),_RdwrConfSyncPeerIP_Type())
rdwrConfSyncPeerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncPeerIP.setStatus(_A)
_RdwrConfSyncPeerBaseMac_Type=PhysAddress
_RdwrConfSyncPeerBaseMac_Object=MibScalar
rdwrConfSyncPeerBaseMac=_RdwrConfSyncPeerBaseMac_Object((1,3,6,1,4,1,89,35,1,161,1,4),_RdwrConfSyncPeerBaseMac_Type())
rdwrConfSyncPeerBaseMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncPeerBaseMac.setStatus(_A)
class _RdwrConfSyncIncompatibilityReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('compatible',1),('incompatibleHardware',2),('incompatibleInstalledMemorySize',3),('incompatibleLicense',4),('incompatibleSoftwareVersion',5),('incompatibleSlaveConfiguration',6),('unknown',7),('incompatibleAttackDb',8)))
_RdwrConfSyncIncompatibilityReason_Type.__name__=_D
_RdwrConfSyncIncompatibilityReason_Object=MibScalar
rdwrConfSyncIncompatibilityReason=_RdwrConfSyncIncompatibilityReason_Object((1,3,6,1,4,1,89,35,1,161,1,5),_RdwrConfSyncIncompatibilityReason_Type())
rdwrConfSyncIncompatibilityReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncIncompatibilityReason.setStatus(_A)
_RdwrConfSyncLastConfSyncTime_Type=Unsigned32
_RdwrConfSyncLastConfSyncTime_Object=MibScalar
rdwrConfSyncLastConfSyncTime=_RdwrConfSyncLastConfSyncTime_Object((1,3,6,1,4,1,89,35,1,161,1,6),_RdwrConfSyncLastConfSyncTime_Type())
rdwrConfSyncLastConfSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncLastConfSyncTime.setStatus(_A)
_RdwrConfSyncLastConfFullSyncTime_Type=Unsigned32
_RdwrConfSyncLastConfFullSyncTime_Object=MibScalar
rdwrConfSyncLastConfFullSyncTime=_RdwrConfSyncLastConfFullSyncTime_Object((1,3,6,1,4,1,89,35,1,161,1,7),_RdwrConfSyncLastConfFullSyncTime_Type())
rdwrConfSyncLastConfFullSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncLastConfFullSyncTime.setStatus(_A)
_RdwrConfSyncNumOfFullSyncOperations_Type=Integer32
_RdwrConfSyncNumOfFullSyncOperations_Object=MibScalar
rdwrConfSyncNumOfFullSyncOperations=_RdwrConfSyncNumOfFullSyncOperations_Object((1,3,6,1,4,1,89,35,1,161,1,8),_RdwrConfSyncNumOfFullSyncOperations_Type())
rdwrConfSyncNumOfFullSyncOperations.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncNumOfFullSyncOperations.setStatus(_A)
_RdwrConfSyncNumOfSyncOperations_Type=Integer32
_RdwrConfSyncNumOfSyncOperations_Object=MibScalar
rdwrConfSyncNumOfSyncOperations=_RdwrConfSyncNumOfSyncOperations_Object((1,3,6,1,4,1,89,35,1,161,1,9),_RdwrConfSyncNumOfSyncOperations_Type())
rdwrConfSyncNumOfSyncOperations.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncNumOfSyncOperations.setStatus(_A)
_RdwrConfSyncNumOfFailedSyncAttempts_Type=Integer32
_RdwrConfSyncNumOfFailedSyncAttempts_Object=MibScalar
rdwrConfSyncNumOfFailedSyncAttempts=_RdwrConfSyncNumOfFailedSyncAttempts_Object((1,3,6,1,4,1,89,35,1,161,1,10),_RdwrConfSyncNumOfFailedSyncAttempts_Type())
rdwrConfSyncNumOfFailedSyncAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncNumOfFailedSyncAttempts.setStatus(_A)
_RdwrConfSyncPeerConfigVersion_Type=Integer32
_RdwrConfSyncPeerConfigVersion_Object=MibScalar
rdwrConfSyncPeerConfigVersion=_RdwrConfSyncPeerConfigVersion_Object((1,3,6,1,4,1,89,35,1,161,1,11),_RdwrConfSyncPeerConfigVersion_Type())
rdwrConfSyncPeerConfigVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncPeerConfigVersion.setStatus(_A)
_RdwrConfSyncConfigTimestamp_Type=Unsigned32
_RdwrConfSyncConfigTimestamp_Object=MibScalar
rdwrConfSyncConfigTimestamp=_RdwrConfSyncConfigTimestamp_Object((1,3,6,1,4,1,89,35,1,161,1,12),_RdwrConfSyncConfigTimestamp_Type())
rdwrConfSyncConfigTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncConfigTimestamp.setStatus(_A)
class _RdwrConfSyncResetStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_RdwrConfSyncResetStatistics_Type.__name__=_D
_RdwrConfSyncResetStatistics_Object=MibScalar
rdwrConfSyncResetStatistics=_RdwrConfSyncResetStatistics_Object((1,3,6,1,4,1,89,35,1,161,1,13),_RdwrConfSyncResetStatistics_Type())
rdwrConfSyncResetStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncResetStatistics.setStatus(_A)
_RdwrConfSyncShouldReboot_Type=TruthValue
_RdwrConfSyncShouldReboot_Object=MibScalar
rdwrConfSyncShouldReboot=_RdwrConfSyncShouldReboot_Object((1,3,6,1,4,1,89,35,1,161,1,14),_RdwrConfSyncShouldReboot_Type())
rdwrConfSyncShouldReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncShouldReboot.setStatus(_A)
_RdwrConfSyncNumOfConnects_Type=Integer32
_RdwrConfSyncNumOfConnects_Object=MibScalar
rdwrConfSyncNumOfConnects=_RdwrConfSyncNumOfConnects_Object((1,3,6,1,4,1,89,35,1,161,1,15),_RdwrConfSyncNumOfConnects_Type())
rdwrConfSyncNumOfConnects.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncNumOfConnects.setStatus(_A)
_RdwrConfSyncNumOfDisconnects_Type=Integer32
_RdwrConfSyncNumOfDisconnects_Object=MibScalar
rdwrConfSyncNumOfDisconnects=_RdwrConfSyncNumOfDisconnects_Object((1,3,6,1,4,1,89,35,1,161,1,16),_RdwrConfSyncNumOfDisconnects_Type())
rdwrConfSyncNumOfDisconnects.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncNumOfDisconnects.setStatus(_A)
_RdwrConfSyncIPString_Type=OctetString
_RdwrConfSyncIPString_Object=MibScalar
rdwrConfSyncIPString=_RdwrConfSyncIPString_Object((1,3,6,1,4,1,89,35,1,161,1,18),_RdwrConfSyncIPString_Type())
rdwrConfSyncIPString.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncIPString.setStatus(_A)
_RdwrConfSyncPeerIPString_Type=OctetString
_RdwrConfSyncPeerIPString_Object=MibScalar
rdwrConfSyncPeerIPString=_RdwrConfSyncPeerIPString_Object((1,3,6,1,4,1,89,35,1,161,1,19),_RdwrConfSyncPeerIPString_Type())
rdwrConfSyncPeerIPString.setMaxAccess(_C)
if mibBuilder.loadTexts:rdwrConfSyncPeerIPString.setStatus(_A)
_RdwrConfigurationSyncConf_ObjectIdentity=ObjectIdentity
rdwrConfigurationSyncConf=_RdwrConfigurationSyncConf_ObjectIdentity((1,3,6,1,4,1,89,35,1,161,2))
class _RdwrConfSyncMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('disabled',3)))
_RdwrConfSyncMode_Type.__name__=_D
_RdwrConfSyncMode_Object=MibScalar
rdwrConfSyncMode=_RdwrConfSyncMode_Object((1,3,6,1,4,1,89,35,1,161,2,1),_RdwrConfSyncMode_Type())
rdwrConfSyncMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncMode.setStatus(_A)
class _RdwrConfSyncRetryTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_RdwrConfSyncRetryTimeout_Type.__name__=_D
_RdwrConfSyncRetryTimeout_Object=MibScalar
rdwrConfSyncRetryTimeout=_RdwrConfSyncRetryTimeout_Object((1,3,6,1,4,1,89,35,1,161,2,2),_RdwrConfSyncRetryTimeout_Type())
rdwrConfSyncRetryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncRetryTimeout.setStatus(_A)
class _RdwrConfSyncKeepAlivePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_RdwrConfSyncKeepAlivePeriod_Type.__name__=_D
_RdwrConfSyncKeepAlivePeriod_Object=MibScalar
rdwrConfSyncKeepAlivePeriod=_RdwrConfSyncKeepAlivePeriod_Object((1,3,6,1,4,1,89,35,1,161,2,3),_RdwrConfSyncKeepAlivePeriod_Type())
rdwrConfSyncKeepAlivePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncKeepAlivePeriod.setStatus(_A)
class _RdwrConfSyncRebootTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_RdwrConfSyncRebootTimeout_Type.__name__=_D
_RdwrConfSyncRebootTimeout_Object=MibScalar
rdwrConfSyncRebootTimeout=_RdwrConfSyncRebootTimeout_Object((1,3,6,1,4,1,89,35,1,161,2,4),_RdwrConfSyncRebootTimeout_Type())
rdwrConfSyncRebootTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncRebootTimeout.setStatus(_A)
class _RdwrConfSyncPeerDiscTrapDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_RdwrConfSyncPeerDiscTrapDelay_Type.__name__=_D
_RdwrConfSyncPeerDiscTrapDelay_Object=MibScalar
rdwrConfSyncPeerDiscTrapDelay=_RdwrConfSyncPeerDiscTrapDelay_Object((1,3,6,1,4,1,89,35,1,161,2,5),_RdwrConfSyncPeerDiscTrapDelay_Type())
rdwrConfSyncPeerDiscTrapDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncPeerDiscTrapDelay.setStatus(_A)
class _RdwrConfSyncPeerResponseTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_RdwrConfSyncPeerResponseTimeout_Type.__name__=_D
_RdwrConfSyncPeerResponseTimeout_Object=MibScalar
rdwrConfSyncPeerResponseTimeout=_RdwrConfSyncPeerResponseTimeout_Object((1,3,6,1,4,1,89,35,1,161,2,6),_RdwrConfSyncPeerResponseTimeout_Type())
rdwrConfSyncPeerResponseTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncPeerResponseTimeout.setStatus(_A)
class _RdwrConfSyncMasterActivityTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_RdwrConfSyncMasterActivityTimeout_Type.__name__=_D
_RdwrConfSyncMasterActivityTimeout_Object=MibScalar
rdwrConfSyncMasterActivityTimeout=_RdwrConfSyncMasterActivityTimeout_Object((1,3,6,1,4,1,89,35,1,161,2,7),_RdwrConfSyncMasterActivityTimeout_Type())
rdwrConfSyncMasterActivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncMasterActivityTimeout.setStatus(_A)
_RdwrConfSyncAllowRebootActiveDevice_Type=TruthValue
_RdwrConfSyncAllowRebootActiveDevice_Object=MibScalar
rdwrConfSyncAllowRebootActiveDevice=_RdwrConfSyncAllowRebootActiveDevice_Object((1,3,6,1,4,1,89,35,1,161,2,8),_RdwrConfSyncAllowRebootActiveDevice_Type())
rdwrConfSyncAllowRebootActiveDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncAllowRebootActiveDevice.setStatus(_A)
class _RdwrConfSyncRebootSlave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_RdwrConfSyncRebootSlave_Type.__name__=_D
_RdwrConfSyncRebootSlave_Object=MibScalar
rdwrConfSyncRebootSlave=_RdwrConfSyncRebootSlave_Object((1,3,6,1,4,1,89,35,1,161,2,9),_RdwrConfSyncRebootSlave_Type())
rdwrConfSyncRebootSlave.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncRebootSlave.setStatus(_A)
_RdwrConfSyncExcludeMgmtIP_Type=TruthValue
_RdwrConfSyncExcludeMgmtIP_Object=MibScalar
rdwrConfSyncExcludeMgmtIP=_RdwrConfSyncExcludeMgmtIP_Object((1,3,6,1,4,1,89,35,1,161,2,10),_RdwrConfSyncExcludeMgmtIP_Type())
rdwrConfSyncExcludeMgmtIP.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncExcludeMgmtIP.setStatus(_A)
_RdwrConfSyncExcludeMgmtCert_Type=TruthValue
_RdwrConfSyncExcludeMgmtCert_Object=MibScalar
rdwrConfSyncExcludeMgmtCert=_RdwrConfSyncExcludeMgmtCert_Object((1,3,6,1,4,1,89,35,1,161,2,11),_RdwrConfSyncExcludeMgmtCert_Type())
rdwrConfSyncExcludeMgmtCert.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncExcludeMgmtCert.setStatus(_A)
_RdwrConfSyncDiscoverMngIPOnly_Type=TruthValue
_RdwrConfSyncDiscoverMngIPOnly_Object=MibScalar
rdwrConfSyncDiscoverMngIPOnly=_RdwrConfSyncDiscoverMngIPOnly_Object((1,3,6,1,4,1,89,35,1,161,2,12),_RdwrConfSyncDiscoverMngIPOnly_Type())
rdwrConfSyncDiscoverMngIPOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncDiscoverMngIPOnly.setStatus('obsolete')
class _RdwrConfSyncFullSyncDelay_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_RdwrConfSyncFullSyncDelay_Type.__name__=_D
_RdwrConfSyncFullSyncDelay_Object=MibScalar
rdwrConfSyncFullSyncDelay=_RdwrConfSyncFullSyncDelay_Object((1,3,6,1,4,1,89,35,1,161,2,13),_RdwrConfSyncFullSyncDelay_Type())
rdwrConfSyncFullSyncDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncFullSyncDelay.setStatus(_A)
class _RdwrConfSyncFullSyncMaxDelay_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_RdwrConfSyncFullSyncMaxDelay_Type.__name__=_D
_RdwrConfSyncFullSyncMaxDelay_Object=MibScalar
rdwrConfSyncFullSyncMaxDelay=_RdwrConfSyncFullSyncMaxDelay_Object((1,3,6,1,4,1,89,35,1,161,2,14),_RdwrConfSyncFullSyncMaxDelay_Type())
rdwrConfSyncFullSyncMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncFullSyncMaxDelay.setStatus(_A)
_RdwrConfSyncCommunicationPassword_Type=OctetString
_RdwrConfSyncCommunicationPassword_Object=MibScalar
rdwrConfSyncCommunicationPassword=_RdwrConfSyncCommunicationPassword_Object((1,3,6,1,4,1,89,35,1,161,2,15),_RdwrConfSyncCommunicationPassword_Type())
rdwrConfSyncCommunicationPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncCommunicationPassword.setStatus(_A)
_RdwrConfSyncConnectionPreference_Type=OctetString
_RdwrConfSyncConnectionPreference_Object=MibScalar
rdwrConfSyncConnectionPreference=_RdwrConfSyncConnectionPreference_Object((1,3,6,1,4,1,89,35,1,161,2,16),_RdwrConfSyncConnectionPreference_Type())
rdwrConfSyncConnectionPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncConnectionPreference.setStatus(_A)
_RdwrConfSyncAlternateConnectionPreference_Type=OctetString
_RdwrConfSyncAlternateConnectionPreference_Object=MibScalar
rdwrConfSyncAlternateConnectionPreference=_RdwrConfSyncAlternateConnectionPreference_Object((1,3,6,1,4,1,89,35,1,161,2,17),_RdwrConfSyncAlternateConnectionPreference_Type())
rdwrConfSyncAlternateConnectionPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncAlternateConnectionPreference.setStatus(_A)
class _RdwrConfSyncReconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reconnect',1),('doNothing',2)))
_RdwrConfSyncReconnect_Type.__name__=_D
_RdwrConfSyncReconnect_Object=MibScalar
rdwrConfSyncReconnect=_RdwrConfSyncReconnect_Object((1,3,6,1,4,1,89,35,1,161,2,18),_RdwrConfSyncReconnect_Type())
rdwrConfSyncReconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:rdwrConfSyncReconnect.setStatus(_A)
mibBuilder.exportSymbols('CDE-MIB',**{'rdwrConfigurationSyncMonitor':rdwrConfigurationSyncMonitor,'rdwrConfSyncState':rdwrConfSyncState,'rdwrConfSyncIP':rdwrConfSyncIP,'rdwrConfSyncPeerIP':rdwrConfSyncPeerIP,'rdwrConfSyncPeerBaseMac':rdwrConfSyncPeerBaseMac,'rdwrConfSyncIncompatibilityReason':rdwrConfSyncIncompatibilityReason,'rdwrConfSyncLastConfSyncTime':rdwrConfSyncLastConfSyncTime,'rdwrConfSyncLastConfFullSyncTime':rdwrConfSyncLastConfFullSyncTime,'rdwrConfSyncNumOfFullSyncOperations':rdwrConfSyncNumOfFullSyncOperations,'rdwrConfSyncNumOfSyncOperations':rdwrConfSyncNumOfSyncOperations,'rdwrConfSyncNumOfFailedSyncAttempts':rdwrConfSyncNumOfFailedSyncAttempts,'rdwrConfSyncPeerConfigVersion':rdwrConfSyncPeerConfigVersion,'rdwrConfSyncConfigTimestamp':rdwrConfSyncConfigTimestamp,'rdwrConfSyncResetStatistics':rdwrConfSyncResetStatistics,'rdwrConfSyncShouldReboot':rdwrConfSyncShouldReboot,'rdwrConfSyncNumOfConnects':rdwrConfSyncNumOfConnects,'rdwrConfSyncNumOfDisconnects':rdwrConfSyncNumOfDisconnects,'rdwrConfSyncIPString':rdwrConfSyncIPString,'rdwrConfSyncPeerIPString':rdwrConfSyncPeerIPString,'rdwrConfigurationSyncConf':rdwrConfigurationSyncConf,'rdwrConfSyncMode':rdwrConfSyncMode,'rdwrConfSyncRetryTimeout':rdwrConfSyncRetryTimeout,'rdwrConfSyncKeepAlivePeriod':rdwrConfSyncKeepAlivePeriod,'rdwrConfSyncRebootTimeout':rdwrConfSyncRebootTimeout,'rdwrConfSyncPeerDiscTrapDelay':rdwrConfSyncPeerDiscTrapDelay,'rdwrConfSyncPeerResponseTimeout':rdwrConfSyncPeerResponseTimeout,'rdwrConfSyncMasterActivityTimeout':rdwrConfSyncMasterActivityTimeout,'rdwrConfSyncAllowRebootActiveDevice':rdwrConfSyncAllowRebootActiveDevice,'rdwrConfSyncRebootSlave':rdwrConfSyncRebootSlave,'rdwrConfSyncExcludeMgmtIP':rdwrConfSyncExcludeMgmtIP,'rdwrConfSyncExcludeMgmtCert':rdwrConfSyncExcludeMgmtCert,'rdwrConfSyncDiscoverMngIPOnly':rdwrConfSyncDiscoverMngIPOnly,'rdwrConfSyncFullSyncDelay':rdwrConfSyncFullSyncDelay,'rdwrConfSyncFullSyncMaxDelay':rdwrConfSyncFullSyncMaxDelay,'rdwrConfSyncCommunicationPassword':rdwrConfSyncCommunicationPassword,'rdwrConfSyncConnectionPreference':rdwrConfSyncConnectionPreference,'rdwrConfSyncAlternateConnectionPreference':rdwrConfSyncAlternateConnectionPreference,'rdwrConfSyncReconnect':rdwrConfSyncReconnect})