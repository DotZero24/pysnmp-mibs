_AH='ciscoTsTCActivePorts'
_AG='ciscoTsTCStatus'
_AF='ciscoTsPortStatsCfgLoss'
_AE='ciscoTsPortCfgActualForwardingMode'
_AD='ciscoTsStackSwitchPwrSupplyStatus'
_AC='ciscoTsStackSwitchTemperature'
_AB='ciscoTsProStackMatrixStatus'
_AA='ciscoTsNumSwitches'
_A9='ciscoTsTrunkProtocolFilterPort'
_A8='ciscoTsDupAddrFilterStationAddress'
_A7='ciscoTsDupAddrFilterSwitchNumber'
_A6='ciscoTsMACSourceFilterType'
_A5='ciscoTsMACSourceFilterStationAddress'
_A4='ciscoTsMACSourceFilterSwitchNumber'
_A3='ciscoTsMACDestFilterType'
_A2='ciscoTsMACDestFilterStationAddress'
_A1='ciscoTsMACDestFilterSwitchNumber'
_A0='ciscoTsProtocolFilterPort'
_z='ciscoTsTCNumber'
_y='ciscoTsTCSwitchNumber'
_x='ciscoTsPassiveProbeIndex'
_w='ciscoTsPortStatsNumber'
_v='blocking'
_u='forwarding'
_t='passive-probe'
_s='fdx-Station'
_r='fdx-Port'
_q='hdx-Station'
_p='hdx-Port'
_o='cutthru'
_n='storeandforward'
_m='disabled'
_l='enabled'
_k='ciscoTsModNumber'
_j='ciscoTsModSwitchNumber'
_i='ciscoTsStackSwitchBIAddr'
_h='ciscoTsTrapRcvrIndex'
_g='warmReset'
_f='coldReset'
_e='ringStationMacAddress'
_d='ringStationIfIndex'
_c='NotificationType'
_b='ifName'
_a='IF-MIB'
_Z='ciscoTsTCPorts'
_Y='invalid'
_X='valid'
_W='TOKEN-RING-RMON-MIB'
_V='ciscoTsProtocolClassFilterIndex'
_U='ciscoTsTrBRFInfoTrBRFNumber'
_T='other'
_S='ciscoTsTrCRFInfoTrCRFNumber'
_R='auto'
_Q='disable'
_P='enable'
_O='none'
_N='ciscoTsPortCfgNumber'
_M='running'
_L='ciscoTsStackSwitchNumber'
_K='DisplayString'
_J='unknown'
_I='OctetString'
_H='sysName'
_G='sysLocation'
_F='SNMPv2-MIB'
_E='CISCO-TS-STACK-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Timeout,=mibBuilder.importSymbols('BRIDGE-MIB','Timeout')
cisco,workgroup=mibBuilder.importSymbols('CISCO-SMI','cisco','workgroup')
ifName,=mibBuilder.importSymbols(_a,_b)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,sysName=mibBuilder.importSymbols(_F,_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_c,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_c,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
ringStationIfIndex,ringStationMacAddress=mibBuilder.importSymbols(_W,_d,_e)
class MacAddr(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TsStack_ObjectIdentity=ObjectIdentity
tsStack=_TsStack_ObjectIdentity((1,3,6,1,4,1,9,5,32))
_CiscoTsMain_ObjectIdentity=ObjectIdentity
ciscoTsMain=_CiscoTsMain_ObjectIdentity((1,3,6,1,4,1,9,5,32,1))
_CiscoTsConfig_ObjectIdentity=ObjectIdentity
ciscoTsConfig=_CiscoTsConfig_ObjectIdentity((1,3,6,1,4,1,9,5,32,1,1))
_CiscoTsIpAddr_Type=IpAddress
_CiscoTsIpAddr_Object=MibScalar
ciscoTsIpAddr=_CiscoTsIpAddr_Object((1,3,6,1,4,1,9,5,32,1,1,1),_CiscoTsIpAddr_Type())
ciscoTsIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsIpAddr.setStatus(_A)
_CiscoTsNetMask_Type=IpAddress
_CiscoTsNetMask_Object=MibScalar
ciscoTsNetMask=_CiscoTsNetMask_Object((1,3,6,1,4,1,9,5,32,1,1,2),_CiscoTsNetMask_Type())
ciscoTsNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsNetMask.setStatus(_A)
_CiscoTsDefaultGateway_Type=IpAddress
_CiscoTsDefaultGateway_Object=MibScalar
ciscoTsDefaultGateway=_CiscoTsDefaultGateway_Object((1,3,6,1,4,1,9,5,32,1,1,3),_CiscoTsDefaultGateway_Type())
ciscoTsDefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsDefaultGateway.setStatus(_A)
class _CiscoTsSysCurTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CiscoTsSysCurTime_Type.__name__=_K
_CiscoTsSysCurTime_Object=MibScalar
ciscoTsSysCurTime=_CiscoTsSysCurTime_Object((1,3,6,1,4,1,9,5,32,1,1,4),_CiscoTsSysCurTime_Type())
ciscoTsSysCurTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsSysCurTime.setStatus(_A)
class _CiscoTsConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stand-alone',1),('back-to-back',2),('prostack-matrix',3)))
_CiscoTsConfiguration_Type.__name__=_C
_CiscoTsConfiguration_Object=MibScalar
ciscoTsConfiguration=_CiscoTsConfiguration_Object((1,3,6,1,4,1,9,5,32,1,1,5),_CiscoTsConfiguration_Type())
ciscoTsConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsConfiguration.setStatus(_A)
_CiscoTsNumSwitches_Type=Integer32
_CiscoTsNumSwitches_Object=MibScalar
ciscoTsNumSwitches=_CiscoTsNumSwitches_Object((1,3,6,1,4,1,9,5,32,1,1,6),_CiscoTsNumSwitches_Type())
ciscoTsNumSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsNumSwitches.setStatus(_A)
class _CiscoTsStackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('updating',2)))
_CiscoTsStackStatus_Type.__name__=_C
_CiscoTsStackStatus_Object=MibScalar
ciscoTsStackStatus=_CiscoTsStackStatus_Object((1,3,6,1,4,1,9,5,32,1,1,7),_CiscoTsStackStatus_Type())
ciscoTsStackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackStatus.setStatus(_A)
_CiscoTsTftpServer_Type=IpAddress
_CiscoTsTftpServer_Object=MibScalar
ciscoTsTftpServer=_CiscoTsTftpServer_Object((1,3,6,1,4,1,9,5,32,1,1,8),_CiscoTsTftpServer_Type())
ciscoTsTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTftpServer.setStatus(_A)
class _CiscoTsTftpServerTrBRF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CiscoTsTftpServerTrBRF_Type.__name__=_C
_CiscoTsTftpServerTrBRF_Object=MibScalar
ciscoTsTftpServerTrBRF=_CiscoTsTftpServerTrBRF_Object((1,3,6,1,4,1,9,5,32,1,1,9),_CiscoTsTftpServerTrBRF_Type())
ciscoTsTftpServerTrBRF.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTftpServerTrBRF.setStatus(_A)
class _CiscoTsTftpFileLoc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CiscoTsTftpFileLoc_Type.__name__=_K
_CiscoTsTftpFileLoc_Object=MibScalar
ciscoTsTftpFileLoc=_CiscoTsTftpFileLoc_Object((1,3,6,1,4,1,9,5,32,1,1,10),_CiscoTsTftpFileLoc_Type())
ciscoTsTftpFileLoc.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTftpFileLoc.setStatus(_A)
class _CiscoTsTftpDownload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_CiscoTsTftpDownload_Type.__name__=_C
_CiscoTsTftpDownload_Object=MibScalar
ciscoTsTftpDownload=_CiscoTsTftpDownload_Object((1,3,6,1,4,1,9,5,32,1,1,11),_CiscoTsTftpDownload_Type())
ciscoTsTftpDownload.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTftpDownload.setStatus(_A)
class _CiscoTsTftpDownloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('writing',1),('complete',2),(_T,3)))
_CiscoTsTftpDownloadStatus_Type.__name__=_C
_CiscoTsTftpDownloadStatus_Object=MibScalar
ciscoTsTftpDownloadStatus=_CiscoTsTftpDownloadStatus_Object((1,3,6,1,4,1,9,5,32,1,1,12),_CiscoTsTftpDownloadStatus_Type())
ciscoTsTftpDownloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTftpDownloadStatus.setStatus(_A)
class _CiscoTsProStackMatrixStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primary',1),('secondary',2),(_O,3),('failed',4)))
_CiscoTsProStackMatrixStatus_Type.__name__=_C
_CiscoTsProStackMatrixStatus_Object=MibScalar
ciscoTsProStackMatrixStatus=_CiscoTsProStackMatrixStatus_Object((1,3,6,1,4,1,9,5,32,1,1,13),_CiscoTsProStackMatrixStatus_Type())
ciscoTsProStackMatrixStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsProStackMatrixStatus.setStatus(_A)
_CiscoTsNumMatrixModules_Type=Integer32
_CiscoTsNumMatrixModules_Object=MibScalar
ciscoTsNumMatrixModules=_CiscoTsNumMatrixModules_Object((1,3,6,1,4,1,9,5,32,1,1,14),_CiscoTsNumMatrixModules_Type())
ciscoTsNumMatrixModules.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsNumMatrixModules.setStatus(_A)
class _CiscoTsStackReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_f,2),(_g,3)))
_CiscoTsStackReset_Type.__name__=_C
_CiscoTsStackReset_Object=MibScalar
ciscoTsStackReset=_CiscoTsStackReset_Object((1,3,6,1,4,1,9,5,32,1,1,15),_CiscoTsStackReset_Type())
ciscoTsStackReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackReset.setStatus(_A)
class _CiscoTsStackRMONStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CiscoTsStackRMONStatistics_Type.__name__=_C
_CiscoTsStackRMONStatistics_Object=MibScalar
ciscoTsStackRMONStatistics=_CiscoTsStackRMONStatistics_Object((1,3,6,1,4,1,9,5,32,1,1,16),_CiscoTsStackRMONStatistics_Type())
ciscoTsStackRMONStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackRMONStatistics.setStatus(_A)
_CiscoTsTrapRcvrTable_Object=MibTable
ciscoTsTrapRcvrTable=_CiscoTsTrapRcvrTable_Object((1,3,6,1,4,1,9,5,32,1,1,25))
if mibBuilder.loadTexts:ciscoTsTrapRcvrTable.setStatus(_A)
_CiscoTsTrapRcvrEntry_Object=MibTableRow
ciscoTsTrapRcvrEntry=_CiscoTsTrapRcvrEntry_Object((1,3,6,1,4,1,9,5,32,1,1,25,1))
ciscoTsTrapRcvrEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:ciscoTsTrapRcvrEntry.setStatus(_A)
class _CiscoTsTrapRcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiscoTsTrapRcvrIndex_Type.__name__=_C
_CiscoTsTrapRcvrIndex_Object=MibTableColumn
ciscoTsTrapRcvrIndex=_CiscoTsTrapRcvrIndex_Object((1,3,6,1,4,1,9,5,32,1,1,25,1,1),_CiscoTsTrapRcvrIndex_Type())
ciscoTsTrapRcvrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTrapRcvrIndex.setStatus(_A)
class _CiscoTsTrapRcvrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),(_X,2),(_Y,3),('create',4)))
_CiscoTsTrapRcvrStatus_Type.__name__=_C
_CiscoTsTrapRcvrStatus_Object=MibTableColumn
ciscoTsTrapRcvrStatus=_CiscoTsTrapRcvrStatus_Object((1,3,6,1,4,1,9,5,32,1,1,25,1,2),_CiscoTsTrapRcvrStatus_Type())
ciscoTsTrapRcvrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrapRcvrStatus.setStatus(_A)
_CiscoTsTrapRcvrIpAddress_Type=IpAddress
_CiscoTsTrapRcvrIpAddress_Object=MibTableColumn
ciscoTsTrapRcvrIpAddress=_CiscoTsTrapRcvrIpAddress_Object((1,3,6,1,4,1,9,5,32,1,1,25,1,3),_CiscoTsTrapRcvrIpAddress_Type())
ciscoTsTrapRcvrIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrapRcvrIpAddress.setStatus(_A)
class _CiscoTsTrapRcvrComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CiscoTsTrapRcvrComm_Type.__name__=_K
_CiscoTsTrapRcvrComm_Object=MibTableColumn
ciscoTsTrapRcvrComm=_CiscoTsTrapRcvrComm_Object((1,3,6,1,4,1,9,5,32,1,1,25,1,4),_CiscoTsTrapRcvrComm_Type())
ciscoTsTrapRcvrComm.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrapRcvrComm.setStatus(_A)
class _CiscoTsTrapRcvrTrBRFs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CiscoTsTrapRcvrTrBRFs_Type.__name__=_I
_CiscoTsTrapRcvrTrBRFs_Object=MibTableColumn
ciscoTsTrapRcvrTrBRFs=_CiscoTsTrapRcvrTrBRFs_Object((1,3,6,1,4,1,9,5,32,1,1,25,1,5),_CiscoTsTrapRcvrTrBRFs_Type())
ciscoTsTrapRcvrTrBRFs.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrapRcvrTrBRFs.setStatus(_A)
_CiscoTsStack_ObjectIdentity=ObjectIdentity
ciscoTsStack=_CiscoTsStack_ObjectIdentity((1,3,6,1,4,1,9,5,32,2))
_CiscoTsStackTable_Object=MibTable
ciscoTsStackTable=_CiscoTsStackTable_Object((1,3,6,1,4,1,9,5,32,2,1))
if mibBuilder.loadTexts:ciscoTsStackTable.setStatus(_A)
_CiscoTsStackEntry_Object=MibTableRow
ciscoTsStackEntry=_CiscoTsStackEntry_Object((1,3,6,1,4,1,9,5,32,2,1,1))
ciscoTsStackEntry.setIndexNames((0,_E,_L),(0,_E,_i))
if mibBuilder.loadTexts:ciscoTsStackEntry.setStatus(_A)
class _CiscoTsStackSwitchNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsStackSwitchNumber_Type.__name__=_C
_CiscoTsStackSwitchNumber_Object=MibTableColumn
ciscoTsStackSwitchNumber=_CiscoTsStackSwitchNumber_Object((1,3,6,1,4,1,9,5,32,2,1,1,1),_CiscoTsStackSwitchNumber_Type())
ciscoTsStackSwitchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchNumber.setStatus(_A)
_CiscoTsStackSwitchBIAddr_Type=MacAddr
_CiscoTsStackSwitchBIAddr_Object=MibTableColumn
ciscoTsStackSwitchBIAddr=_CiscoTsStackSwitchBIAddr_Object((1,3,6,1,4,1,9,5,32,2,1,1,2),_CiscoTsStackSwitchBIAddr_Type())
ciscoTsStackSwitchBIAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchBIAddr.setStatus(_A)
_CiscoTsStackSwitchLAAddr_Type=MacAddr
_CiscoTsStackSwitchLAAddr_Object=MibTableColumn
ciscoTsStackSwitchLAAddr=_CiscoTsStackSwitchLAAddr_Object((1,3,6,1,4,1,9,5,32,2,1,1,3),_CiscoTsStackSwitchLAAddr_Type())
ciscoTsStackSwitchLAAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchLAAddr.setStatus(_A)
class _CiscoTsStackSwitchFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CiscoTsStackSwitchFwVersion_Type.__name__=_K
_CiscoTsStackSwitchFwVersion_Object=MibTableColumn
ciscoTsStackSwitchFwVersion=_CiscoTsStackSwitchFwVersion_Object((1,3,6,1,4,1,9,5,32,2,1,1,4),_CiscoTsStackSwitchFwVersion_Type())
ciscoTsStackSwitchFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchFwVersion.setStatus(_A)
class _CiscoTsStackSwitchHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CiscoTsStackSwitchHwVersion_Type.__name__=_K
_CiscoTsStackSwitchHwVersion_Object=MibTableColumn
ciscoTsStackSwitchHwVersion=_CiscoTsStackSwitchHwVersion_Object((1,3,6,1,4,1,9,5,32,2,1,1,5),_CiscoTsStackSwitchHwVersion_Type())
ciscoTsStackSwitchHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchHwVersion.setStatus(_A)
_CiscoTsStackSwitchUptime_Type=TimeTicks
_CiscoTsStackSwitchUptime_Object=MibTableColumn
ciscoTsStackSwitchUptime=_CiscoTsStackSwitchUptime_Object((1,3,6,1,4,1,9,5,32,2,1,1,6),_CiscoTsStackSwitchUptime_Type())
ciscoTsStackSwitchUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchUptime.setStatus(_A)
class _CiscoTsStackSwitchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_f,2),(_g,3)))
_CiscoTsStackSwitchStatus_Type.__name__=_C
_CiscoTsStackSwitchStatus_Object=MibTableColumn
ciscoTsStackSwitchStatus=_CiscoTsStackSwitchStatus_Object((1,3,6,1,4,1,9,5,32,2,1,1,7),_CiscoTsStackSwitchStatus_Type())
ciscoTsStackSwitchStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchStatus.setStatus(_A)
_CiscoTsStackSwitchTemperature_Type=Integer32
_CiscoTsStackSwitchTemperature_Object=MibTableColumn
ciscoTsStackSwitchTemperature=_CiscoTsStackSwitchTemperature_Object((1,3,6,1,4,1,9,5,32,2,1,1,8),_CiscoTsStackSwitchTemperature_Type())
ciscoTsStackSwitchTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchTemperature.setStatus(_A)
class _CiscoTsStackSwitchMemory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CiscoTsStackSwitchMemory_Type.__name__=_C
_CiscoTsStackSwitchMemory_Object=MibTableColumn
ciscoTsStackSwitchMemory=_CiscoTsStackSwitchMemory_Object((1,3,6,1,4,1,9,5,32,2,1,1,9),_CiscoTsStackSwitchMemory_Type())
ciscoTsStackSwitchMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchMemory.setStatus(_A)
class _CiscoTsStackSwitchSPANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CiscoTsStackSwitchSPANPort_Type.__name__=_C
_CiscoTsStackSwitchSPANPort_Object=MibTableColumn
ciscoTsStackSwitchSPANPort=_CiscoTsStackSwitchSPANPort_Object((1,3,6,1,4,1,9,5,32,2,1,1,10),_CiscoTsStackSwitchSPANPort_Type())
ciscoTsStackSwitchSPANPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchSPANPort.setStatus(_A)
class _CiscoTsStackSwitchSPANMonitoredPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CiscoTsStackSwitchSPANMonitoredPort_Type.__name__=_C
_CiscoTsStackSwitchSPANMonitoredPort_Object=MibTableColumn
ciscoTsStackSwitchSPANMonitoredPort=_CiscoTsStackSwitchSPANMonitoredPort_Object((1,3,6,1,4,1,9,5,32,2,1,1,11),_CiscoTsStackSwitchSPANMonitoredPort_Type())
ciscoTsStackSwitchSPANMonitoredPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchSPANMonitoredPort.setStatus(_A)
class _CiscoTsStackSwitchFeatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standard',1),('enhanced',2),(_J,3)))
_CiscoTsStackSwitchFeatureStatus_Type.__name__=_C
_CiscoTsStackSwitchFeatureStatus_Object=MibTableColumn
ciscoTsStackSwitchFeatureStatus=_CiscoTsStackSwitchFeatureStatus_Object((1,3,6,1,4,1,9,5,32,2,1,1,12),_CiscoTsStackSwitchFeatureStatus_Type())
ciscoTsStackSwitchFeatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchFeatureStatus.setStatus(_A)
_CiscoTsStackSwitchFeatureKey_Type=Integer32
_CiscoTsStackSwitchFeatureKey_Object=MibTableColumn
ciscoTsStackSwitchFeatureKey=_CiscoTsStackSwitchFeatureKey_Object((1,3,6,1,4,1,9,5,32,2,1,1,13),_CiscoTsStackSwitchFeatureKey_Type())
ciscoTsStackSwitchFeatureKey.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchFeatureKey.setStatus(_A)
class _CiscoTsStackSwitchPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoTsStackSwitchPorts_Type.__name__=_I
_CiscoTsStackSwitchPorts_Object=MibTableColumn
ciscoTsStackSwitchPorts=_CiscoTsStackSwitchPorts_Object((1,3,6,1,4,1,9,5,32,2,1,1,14),_CiscoTsStackSwitchPorts_Type())
ciscoTsStackSwitchPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchPorts.setStatus(_A)
class _CiscoTsStackSwitchAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_CiscoTsStackSwitchAgingTime_Type.__name__=_C
_CiscoTsStackSwitchAgingTime_Object=MibTableColumn
ciscoTsStackSwitchAgingTime=_CiscoTsStackSwitchAgingTime_Object((1,3,6,1,4,1,9,5,32,2,1,1,15),_CiscoTsStackSwitchAgingTime_Type())
ciscoTsStackSwitchAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchAgingTime.setStatus(_A)
class _CiscoTsStackSwitchAgingLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_CiscoTsStackSwitchAgingLevel_Type.__name__=_C
_CiscoTsStackSwitchAgingLevel_Object=MibTableColumn
ciscoTsStackSwitchAgingLevel=_CiscoTsStackSwitchAgingLevel_Object((1,3,6,1,4,1,9,5,32,2,1,1,16),_CiscoTsStackSwitchAgingLevel_Type())
ciscoTsStackSwitchAgingLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchAgingLevel.setStatus(_A)
_CiscoTsStackSwitchXmitFrames_Type=Counter32
_CiscoTsStackSwitchXmitFrames_Object=MibTableColumn
ciscoTsStackSwitchXmitFrames=_CiscoTsStackSwitchXmitFrames_Object((1,3,6,1,4,1,9,5,32,2,1,1,18),_CiscoTsStackSwitchXmitFrames_Type())
ciscoTsStackSwitchXmitFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchXmitFrames.setStatus(_A)
_CiscoTsStackSwitchRcvdFrames_Type=Counter32
_CiscoTsStackSwitchRcvdFrames_Object=MibTableColumn
ciscoTsStackSwitchRcvdFrames=_CiscoTsStackSwitchRcvdFrames_Object((1,3,6,1,4,1,9,5,32,2,1,1,19),_CiscoTsStackSwitchRcvdFrames_Type())
ciscoTsStackSwitchRcvdFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchRcvdFrames.setStatus(_A)
_CiscoTsStackSwitchRcvdErrFrames_Type=Counter32
_CiscoTsStackSwitchRcvdErrFrames_Object=MibTableColumn
ciscoTsStackSwitchRcvdErrFrames=_CiscoTsStackSwitchRcvdErrFrames_Object((1,3,6,1,4,1,9,5,32,2,1,1,20),_CiscoTsStackSwitchRcvdErrFrames_Type())
ciscoTsStackSwitchRcvdErrFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchRcvdErrFrames.setStatus(_A)
_CiscoTsStackSwitchLostFrames_Type=Counter32
_CiscoTsStackSwitchLostFrames_Object=MibTableColumn
ciscoTsStackSwitchLostFrames=_CiscoTsStackSwitchLostFrames_Object((1,3,6,1,4,1,9,5,32,2,1,1,21),_CiscoTsStackSwitchLostFrames_Type())
ciscoTsStackSwitchLostFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchLostFrames.setStatus(_A)
_CiscoTsStackSwitchPendingSendRqsts_Type=Counter32
_CiscoTsStackSwitchPendingSendRqsts_Object=MibTableColumn
ciscoTsStackSwitchPendingSendRqsts=_CiscoTsStackSwitchPendingSendRqsts_Object((1,3,6,1,4,1,9,5,32,2,1,1,22),_CiscoTsStackSwitchPendingSendRqsts_Type())
ciscoTsStackSwitchPendingSendRqsts.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchPendingSendRqsts.setStatus(_A)
_CiscoTsStackSwitchXmitErrFrames_Type=Counter32
_CiscoTsStackSwitchXmitErrFrames_Object=MibTableColumn
ciscoTsStackSwitchXmitErrFrames=_CiscoTsStackSwitchXmitErrFrames_Object((1,3,6,1,4,1,9,5,32,2,1,1,23),_CiscoTsStackSwitchXmitErrFrames_Type())
ciscoTsStackSwitchXmitErrFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchXmitErrFrames.setStatus(_A)
_CiscoTsStackSwitchCurrActStations_Type=Counter32
_CiscoTsStackSwitchCurrActStations_Object=MibTableColumn
ciscoTsStackSwitchCurrActStations=_CiscoTsStackSwitchCurrActStations_Object((1,3,6,1,4,1,9,5,32,2,1,1,24),_CiscoTsStackSwitchCurrActStations_Type())
ciscoTsStackSwitchCurrActStations.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchCurrActStations.setStatus(_A)
_CiscoTsStackSwitchLargestNumStations_Type=Counter32
_CiscoTsStackSwitchLargestNumStations_Object=MibTableColumn
ciscoTsStackSwitchLargestNumStations=_CiscoTsStackSwitchLargestNumStations_Object((1,3,6,1,4,1,9,5,32,2,1,1,25),_CiscoTsStackSwitchLargestNumStations_Type())
ciscoTsStackSwitchLargestNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchLargestNumStations.setStatus(_A)
_CiscoTsStackSwitchMaxAddressChain_Type=Gauge32
_CiscoTsStackSwitchMaxAddressChain_Object=MibTableColumn
ciscoTsStackSwitchMaxAddressChain=_CiscoTsStackSwitchMaxAddressChain_Object((1,3,6,1,4,1,9,5,32,2,1,1,26),_CiscoTsStackSwitchMaxAddressChain_Type())
ciscoTsStackSwitchMaxAddressChain.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchMaxAddressChain.setStatus(_A)
_CiscoTsStackSwitchAddressTblFulls_Type=Counter32
_CiscoTsStackSwitchAddressTblFulls_Object=MibTableColumn
ciscoTsStackSwitchAddressTblFulls=_CiscoTsStackSwitchAddressTblFulls_Object((1,3,6,1,4,1,9,5,32,2,1,1,27),_CiscoTsStackSwitchAddressTblFulls_Type())
ciscoTsStackSwitchAddressTblFulls.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchAddressTblFulls.setStatus(_A)
_CiscoTsStackSwitchId_Type=ObjectIdentifier
_CiscoTsStackSwitchId_Object=MibTableColumn
ciscoTsStackSwitchId=_CiscoTsStackSwitchId_Object((1,3,6,1,4,1,9,5,32,2,1,1,28),_CiscoTsStackSwitchId_Type())
ciscoTsStackSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchId.setStatus(_A)
class _CiscoTsStackSwitchSPANMonitoredTrCRFs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CiscoTsStackSwitchSPANMonitoredTrCRFs_Type.__name__=_I
_CiscoTsStackSwitchSPANMonitoredTrCRFs_Object=MibTableColumn
ciscoTsStackSwitchSPANMonitoredTrCRFs=_CiscoTsStackSwitchSPANMonitoredTrCRFs_Object((1,3,6,1,4,1,9,5,32,2,1,1,29),_CiscoTsStackSwitchSPANMonitoredTrCRFs_Type())
ciscoTsStackSwitchSPANMonitoredTrCRFs.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsStackSwitchSPANMonitoredTrCRFs.setStatus(_A)
class _CiscoTsStackSwitchPwrSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('internal-only',2),('internal-no-backup',3),('internal-backup-will-reset',4),('external-no-backup',5),('external-backup-no-reset',6)))
_CiscoTsStackSwitchPwrSupplyStatus_Type.__name__=_C
_CiscoTsStackSwitchPwrSupplyStatus_Object=MibTableColumn
ciscoTsStackSwitchPwrSupplyStatus=_CiscoTsStackSwitchPwrSupplyStatus_Object((1,3,6,1,4,1,9,5,32,2,1,1,30),_CiscoTsStackSwitchPwrSupplyStatus_Type())
ciscoTsStackSwitchPwrSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsStackSwitchPwrSupplyStatus.setStatus(_A)
_CiscoTsModule_ObjectIdentity=ObjectIdentity
ciscoTsModule=_CiscoTsModule_ObjectIdentity((1,3,6,1,4,1,9,5,32,3))
_CiscoTsModTable_Object=MibTable
ciscoTsModTable=_CiscoTsModTable_Object((1,3,6,1,4,1,9,5,32,3,1))
if mibBuilder.loadTexts:ciscoTsModTable.setStatus(_A)
_CiscoTsModEntry_Object=MibTableRow
ciscoTsModEntry=_CiscoTsModEntry_Object((1,3,6,1,4,1,9,5,32,3,1,1))
ciscoTsModEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:ciscoTsModEntry.setStatus(_A)
class _CiscoTsModSwitchNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsModSwitchNumber_Type.__name__=_C
_CiscoTsModSwitchNumber_Object=MibTableColumn
ciscoTsModSwitchNumber=_CiscoTsModSwitchNumber_Object((1,3,6,1,4,1,9,5,32,3,1,1,1),_CiscoTsModSwitchNumber_Type())
ciscoTsModSwitchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModSwitchNumber.setStatus(_A)
class _CiscoTsModNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CiscoTsModNumber_Type.__name__=_C
_CiscoTsModNumber_Object=MibTableColumn
ciscoTsModNumber=_CiscoTsModNumber_Object((1,3,6,1,4,1,9,5,32,3,1,1,2),_CiscoTsModNumber_Type())
ciscoTsModNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModNumber.setStatus(_A)
class _CiscoTsModState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nomodule',1),(_M,2),('faulty',3)))
_CiscoTsModState_Type.__name__=_C
_CiscoTsModState_Object=MibTableColumn
ciscoTsModState=_CiscoTsModState_Object((1,3,6,1,4,1,9,5,32,3,1,1,3),_CiscoTsModState_Type())
ciscoTsModState.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModState.setStatus(_A)
class _CiscoTsModType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,8,9,10,11)));namedValues=NamedValues(*(('system',1),('proStack',2),('proPort4TR',3),('proPort4Fiber',4),('proPortISL-FX',5),('proPortISL-TX',6),('proPortATM155Fiber',8),('proPortATM155UTP',9),(_J,10),(_O,11)))
_CiscoTsModType_Type.__name__=_C
_CiscoTsModType_Object=MibTableColumn
ciscoTsModType=_CiscoTsModType_Object((1,3,6,1,4,1,9,5,32,3,1,1,4),_CiscoTsModType_Type())
ciscoTsModType.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModType.setStatus(_A)
_CiscoTsModRevision_Type=DisplayString
_CiscoTsModRevision_Object=MibTableColumn
ciscoTsModRevision=_CiscoTsModRevision_Object((1,3,6,1,4,1,9,5,32,3,1,1,5),_CiscoTsModRevision_Type())
ciscoTsModRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModRevision.setStatus(_A)
_CiscoTsModFwVer_Type=DisplayString
_CiscoTsModFwVer_Object=MibTableColumn
ciscoTsModFwVer=_CiscoTsModFwVer_Object((1,3,6,1,4,1,9,5,32,3,1,1,6),_CiscoTsModFwVer_Type())
ciscoTsModFwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModFwVer.setStatus(_A)
_CiscoTsModNumPorts_Type=Integer32
_CiscoTsModNumPorts_Object=MibTableColumn
ciscoTsModNumPorts=_CiscoTsModNumPorts_Object((1,3,6,1,4,1,9,5,32,3,1,1,7),_CiscoTsModNumPorts_Type())
ciscoTsModNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModNumPorts.setStatus(_A)
_CiscoTsModUptime_Type=TimeTicks
_CiscoTsModUptime_Object=MibTableColumn
ciscoTsModUptime=_CiscoTsModUptime_Object((1,3,6,1,4,1,9,5,32,3,1,1,8),_CiscoTsModUptime_Type())
ciscoTsModUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsModUptime.setStatus(_A)
_CiscoTsPort_ObjectIdentity=ObjectIdentity
ciscoTsPort=_CiscoTsPort_ObjectIdentity((1,3,6,1,4,1,9,5,32,4))
_CiscoTsPortCfgTable_Object=MibTable
ciscoTsPortCfgTable=_CiscoTsPortCfgTable_Object((1,3,6,1,4,1,9,5,32,4,1))
if mibBuilder.loadTexts:ciscoTsPortCfgTable.setStatus(_A)
_CiscoTsPortCfgEntry_Object=MibTableRow
ciscoTsPortCfgEntry=_CiscoTsPortCfgEntry_Object((1,3,6,1,4,1,9,5,32,4,1,1))
ciscoTsPortCfgEntry.setIndexNames((0,_E,_L),(0,_E,_N))
if mibBuilder.loadTexts:ciscoTsPortCfgEntry.setStatus(_A)
class _CiscoTsPortCfgNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiscoTsPortCfgNumber_Type.__name__=_C
_CiscoTsPortCfgNumber_Object=MibTableColumn
ciscoTsPortCfgNumber=_CiscoTsPortCfgNumber_Object((1,3,6,1,4,1,9,5,32,4,1,1,1),_CiscoTsPortCfgNumber_Type())
ciscoTsPortCfgNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortCfgNumber.setStatus(_A)
class _CiscoTsPortCfgModNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CiscoTsPortCfgModNumber_Type.__name__=_C
_CiscoTsPortCfgModNumber_Object=MibTableColumn
ciscoTsPortCfgModNumber=_CiscoTsPortCfgModNumber_Object((1,3,6,1,4,1,9,5,32,4,1,1,2),_CiscoTsPortCfgModNumber_Type())
ciscoTsPortCfgModNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortCfgModNumber.setStatus(_A)
_CiscoTsPortCfgIfIndex_Type=Integer32
_CiscoTsPortCfgIfIndex_Object=MibTableColumn
ciscoTsPortCfgIfIndex=_CiscoTsPortCfgIfIndex_Object((1,3,6,1,4,1,9,5,32,4,1,1,3),_CiscoTsPortCfgIfIndex_Type())
ciscoTsPortCfgIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortCfgIfIndex.setStatus(_A)
class _CiscoTsPortCfgResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_M,2),('reset',3)))
_CiscoTsPortCfgResetStats_Type.__name__=_C
_CiscoTsPortCfgResetStats_Object=MibTableColumn
ciscoTsPortCfgResetStats=_CiscoTsPortCfgResetStats_Object((1,3,6,1,4,1,9,5,32,4,1,1,4),_CiscoTsPortCfgResetStats_Type())
ciscoTsPortCfgResetStats.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgResetStats.setStatus(_A)
class _CiscoTsPortCfgResetAddrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_M,2),('reset',3)))
_CiscoTsPortCfgResetAddrs_Type.__name__=_C
_CiscoTsPortCfgResetAddrs_Object=MibTableColumn
ciscoTsPortCfgResetAddrs=_CiscoTsPortCfgResetAddrs_Object((1,3,6,1,4,1,9,5,32,4,1,1,5),_CiscoTsPortCfgResetAddrs_Type())
ciscoTsPortCfgResetAddrs.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgResetAddrs.setStatus(_A)
class _CiscoTsPortCfgAddrAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_CiscoTsPortCfgAddrAgingTime_Type.__name__=_C
_CiscoTsPortCfgAddrAgingTime_Object=MibTableColumn
ciscoTsPortCfgAddrAgingTime=_CiscoTsPortCfgAddrAgingTime_Object((1,3,6,1,4,1,9,5,32,4,1,1,6),_CiscoTsPortCfgAddrAgingTime_Type())
ciscoTsPortCfgAddrAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgAddrAgingTime.setStatus(_A)
class _CiscoTsPortCfgDemandAgingLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_CiscoTsPortCfgDemandAgingLevel_Type.__name__=_C
_CiscoTsPortCfgDemandAgingLevel_Object=MibTableColumn
ciscoTsPortCfgDemandAgingLevel=_CiscoTsPortCfgDemandAgingLevel_Object((1,3,6,1,4,1,9,5,32,4,1,1,7),_CiscoTsPortCfgDemandAgingLevel_Type())
ciscoTsPortCfgDemandAgingLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgDemandAgingLevel.setStatus(_A)
class _CiscoTsPortCfgErrLoThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CiscoTsPortCfgErrLoThreshold_Type.__name__=_C
_CiscoTsPortCfgErrLoThreshold_Object=MibTableColumn
ciscoTsPortCfgErrLoThreshold=_CiscoTsPortCfgErrLoThreshold_Object((1,3,6,1,4,1,9,5,32,4,1,1,8),_CiscoTsPortCfgErrLoThreshold_Type())
ciscoTsPortCfgErrLoThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgErrLoThreshold.setStatus(_A)
class _CiscoTsPortCfgErrHiThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CiscoTsPortCfgErrHiThreshold_Type.__name__=_C
_CiscoTsPortCfgErrHiThreshold_Object=MibTableColumn
ciscoTsPortCfgErrHiThreshold=_CiscoTsPortCfgErrHiThreshold_Object((1,3,6,1,4,1,9,5,32,4,1,1,9),_CiscoTsPortCfgErrHiThreshold_Type())
ciscoTsPortCfgErrHiThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgErrHiThreshold.setStatus(_A)
class _CiscoTsPortCfgErrSampling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CiscoTsPortCfgErrSampling_Type.__name__=_C
_CiscoTsPortCfgErrSampling_Object=MibTableColumn
ciscoTsPortCfgErrSampling=_CiscoTsPortCfgErrSampling_Object((1,3,6,1,4,1,9,5,32,4,1,1,10),_CiscoTsPortCfgErrSampling_Type())
ciscoTsPortCfgErrSampling.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgErrSampling.setStatus(_A)
_CiscoTsPortCfgMaxTransmitUnit_Type=Integer32
_CiscoTsPortCfgMaxTransmitUnit_Object=MibTableColumn
ciscoTsPortCfgMaxTransmitUnit=_CiscoTsPortCfgMaxTransmitUnit_Object((1,3,6,1,4,1,9,5,32,4,1,1,11),_CiscoTsPortCfgMaxTransmitUnit_Type())
ciscoTsPortCfgMaxTransmitUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgMaxTransmitUnit.setStatus(_A)
class _CiscoTsPortCfgMaxExplorerRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,5000))
_CiscoTsPortCfgMaxExplorerRate_Type.__name__=_C
_CiscoTsPortCfgMaxExplorerRate_Object=MibTableColumn
ciscoTsPortCfgMaxExplorerRate=_CiscoTsPortCfgMaxExplorerRate_Object((1,3,6,1,4,1,9,5,32,4,1,1,12),_CiscoTsPortCfgMaxExplorerRate_Type())
ciscoTsPortCfgMaxExplorerRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgMaxExplorerRate.setStatus(_A)
class _CiscoTsPortCfgSetACbits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_CiscoTsPortCfgSetACbits_Type.__name__=_C
_CiscoTsPortCfgSetACbits_Object=MibTableColumn
ciscoTsPortCfgSetACbits=_CiscoTsPortCfgSetACbits_Object((1,3,6,1,4,1,9,5,32,4,1,1,13),_CiscoTsPortCfgSetACbits_Type())
ciscoTsPortCfgSetACbits.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgSetACbits.setStatus(_A)
class _CiscoTsPortCfgEarlyTokenRlse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_CiscoTsPortCfgEarlyTokenRlse_Type.__name__=_C
_CiscoTsPortCfgEarlyTokenRlse_Object=MibTableColumn
ciscoTsPortCfgEarlyTokenRlse=_CiscoTsPortCfgEarlyTokenRlse_Object((1,3,6,1,4,1,9,5,32,4,1,1,14),_CiscoTsPortCfgEarlyTokenRlse_Type())
ciscoTsPortCfgEarlyTokenRlse.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgEarlyTokenRlse.setStatus(_A)
class _CiscoTsPortCfgForwardingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_n,2),(_o,3),(_J,4)))
_CiscoTsPortCfgForwardingMode_Type.__name__=_C
_CiscoTsPortCfgForwardingMode_Object=MibTableColumn
ciscoTsPortCfgForwardingMode=_CiscoTsPortCfgForwardingMode_Object((1,3,6,1,4,1,9,5,32,4,1,1,15),_CiscoTsPortCfgForwardingMode_Type())
ciscoTsPortCfgForwardingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgForwardingMode.setStatus(_A)
class _CiscoTsPortCfgActualForwardingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_o,2),(_J,3)))
_CiscoTsPortCfgActualForwardingMode_Type.__name__=_C
_CiscoTsPortCfgActualForwardingMode_Object=MibTableColumn
ciscoTsPortCfgActualForwardingMode=_CiscoTsPortCfgActualForwardingMode_Object((1,3,6,1,4,1,9,5,32,4,1,1,16),_CiscoTsPortCfgActualForwardingMode_Type())
ciscoTsPortCfgActualForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortCfgActualForwardingMode.setStatus(_A)
class _CiscoTsPortCfgPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,1),(_p,2),(_q,3),(_r,4),(_s,5),('ri-ro',6),(_t,7),(_J,8)))
_CiscoTsPortCfgPortMode_Type.__name__=_C
_CiscoTsPortCfgPortMode_Object=MibTableColumn
ciscoTsPortCfgPortMode=_CiscoTsPortCfgPortMode_Object((1,3,6,1,4,1,9,5,32,4,1,1,17),_CiscoTsPortCfgPortMode_Type())
ciscoTsPortCfgPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgPortMode.setStatus(_A)
class _CiscoTsPortCfgActualPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),('ri-ro',5),(_t,6),(_J,7)))
_CiscoTsPortCfgActualPortMode_Type.__name__=_C
_CiscoTsPortCfgActualPortMode_Object=MibTableColumn
ciscoTsPortCfgActualPortMode=_CiscoTsPortCfgActualPortMode_Object((1,3,6,1,4,1,9,5,32,4,1,1,18),_CiscoTsPortCfgActualPortMode_Type())
ciscoTsPortCfgActualPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortCfgActualPortMode.setStatus(_A)
class _CiscoTsPortCfgPriorityThres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CiscoTsPortCfgPriorityThres_Type.__name__=_C
_CiscoTsPortCfgPriorityThres_Object=MibTableColumn
ciscoTsPortCfgPriorityThres=_CiscoTsPortCfgPriorityThres_Object((1,3,6,1,4,1,9,5,32,4,1,1,19),_CiscoTsPortCfgPriorityThres_Type())
ciscoTsPortCfgPriorityThres.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgPriorityThres.setStatus(_A)
class _CiscoTsPortCfgMinXmitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_CiscoTsPortCfgMinXmitPriority_Type.__name__=_C
_CiscoTsPortCfgMinXmitPriority_Object=MibTableColumn
ciscoTsPortCfgMinXmitPriority=_CiscoTsPortCfgMinXmitPriority_Object((1,3,6,1,4,1,9,5,32,4,1,1,20),_CiscoTsPortCfgMinXmitPriority_Type())
ciscoTsPortCfgMinXmitPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgMinXmitPriority.setStatus(_A)
class _CiscoTsPortCfgCfgLossThres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoTsPortCfgCfgLossThres_Type.__name__=_C
_CiscoTsPortCfgCfgLossThres_Object=MibTableColumn
ciscoTsPortCfgCfgLossThres=_CiscoTsPortCfgCfgLossThres_Object((1,3,6,1,4,1,9,5,32,4,1,1,21),_CiscoTsPortCfgCfgLossThres_Type())
ciscoTsPortCfgCfgLossThres.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgCfgLossThres.setStatus(_A)
class _CiscoTsPortCfgCfgLossInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CiscoTsPortCfgCfgLossInterval_Type.__name__=_C
_CiscoTsPortCfgCfgLossInterval_Object=MibTableColumn
ciscoTsPortCfgCfgLossInterval=_CiscoTsPortCfgCfgLossInterval_Object((1,3,6,1,4,1,9,5,32,4,1,1,22),_CiscoTsPortCfgCfgLossInterval_Type())
ciscoTsPortCfgCfgLossInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgCfgLossInterval.setStatus(_A)
class _CiscoTsPortCfgBcastSuppresion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CiscoTsPortCfgBcastSuppresion_Type.__name__=_C
_CiscoTsPortCfgBcastSuppresion_Object=MibTableColumn
ciscoTsPortCfgBcastSuppresion=_CiscoTsPortCfgBcastSuppresion_Object((1,3,6,1,4,1,9,5,32,4,1,1,23),_CiscoTsPortCfgBcastSuppresion_Type())
ciscoTsPortCfgBcastSuppresion.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgBcastSuppresion.setStatus(_A)
class _CiscoTsPortCfgCDPTimeToLive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoTsPortCfgCDPTimeToLive_Type.__name__=_C
_CiscoTsPortCfgCDPTimeToLive_Object=MibTableColumn
ciscoTsPortCfgCDPTimeToLive=_CiscoTsPortCfgCDPTimeToLive_Object((1,3,6,1,4,1,9,5,32,4,1,1,24),_CiscoTsPortCfgCDPTimeToLive_Type())
ciscoTsPortCfgCDPTimeToLive.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgCDPTimeToLive.setStatus(_A)
class _CiscoTsPortCfgSpanningTreeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_u,2),(_v,3),(_J,4)))
_CiscoTsPortCfgSpanningTreeMode_Type.__name__=_C
_CiscoTsPortCfgSpanningTreeMode_Object=MibTableColumn
ciscoTsPortCfgSpanningTreeMode=_CiscoTsPortCfgSpanningTreeMode_Object((1,3,6,1,4,1,9,5,32,4,1,1,25),_CiscoTsPortCfgSpanningTreeMode_Type())
ciscoTsPortCfgSpanningTreeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgSpanningTreeMode.setStatus(_A)
class _CiscoTsPortCfgSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('secure-src-addrs',2),('secure-dest-addrs',3),('secure-src-and-dest-addrs',4)))
_CiscoTsPortCfgSecurityMode_Type.__name__=_C
_CiscoTsPortCfgSecurityMode_Object=MibTableColumn
ciscoTsPortCfgSecurityMode=_CiscoTsPortCfgSecurityMode_Object((1,3,6,1,4,1,9,5,32,4,1,1,26),_CiscoTsPortCfgSecurityMode_Type())
ciscoTsPortCfgSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgSecurityMode.setStatus(_A)
class _CiscoTsPortCfgSoftErrThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CiscoTsPortCfgSoftErrThreshold_Type.__name__=_C
_CiscoTsPortCfgSoftErrThreshold_Object=MibTableColumn
ciscoTsPortCfgSoftErrThreshold=_CiscoTsPortCfgSoftErrThreshold_Object((1,3,6,1,4,1,9,5,32,4,1,1,27),_CiscoTsPortCfgSoftErrThreshold_Type())
ciscoTsPortCfgSoftErrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgSoftErrThreshold.setStatus(_A)
class _CiscoTsPortCfgSoftErrReportInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoTsPortCfgSoftErrReportInterval_Type.__name__=_C
_CiscoTsPortCfgSoftErrReportInterval_Object=MibTableColumn
ciscoTsPortCfgSoftErrReportInterval=_CiscoTsPortCfgSoftErrReportInterval_Object((1,3,6,1,4,1,9,5,32,4,1,1,28),_CiscoTsPortCfgSoftErrReportInterval_Type())
ciscoTsPortCfgSoftErrReportInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgSoftErrReportInterval.setStatus(_A)
class _CiscoTsPortCfgSoftErrorMonitoring_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CiscoTsPortCfgSoftErrorMonitoring_Type.__name__=_C
_CiscoTsPortCfgSoftErrorMonitoring_Object=MibTableColumn
ciscoTsPortCfgSoftErrorMonitoring=_CiscoTsPortCfgSoftErrorMonitoring_Object((1,3,6,1,4,1,9,5,32,4,1,1,29),_CiscoTsPortCfgSoftErrorMonitoring_Type())
ciscoTsPortCfgSoftErrorMonitoring.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPortCfgSoftErrorMonitoring.setStatus(_A)
_CiscoTsPortStatsTable_Object=MibTable
ciscoTsPortStatsTable=_CiscoTsPortStatsTable_Object((1,3,6,1,4,1,9,5,32,4,2))
if mibBuilder.loadTexts:ciscoTsPortStatsTable.setStatus(_A)
_CiscoTsPortStatsEntry_Object=MibTableRow
ciscoTsPortStatsEntry=_CiscoTsPortStatsEntry_Object((1,3,6,1,4,1,9,5,32,4,2,1))
ciscoTsPortStatsEntry.setIndexNames((0,_E,_L),(0,_E,_w))
if mibBuilder.loadTexts:ciscoTsPortStatsEntry.setStatus(_A)
class _CiscoTsPortStatsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiscoTsPortStatsNumber_Type.__name__=_C
_CiscoTsPortStatsNumber_Object=MibTableColumn
ciscoTsPortStatsNumber=_CiscoTsPortStatsNumber_Object((1,3,6,1,4,1,9,5,32,4,2,1,1),_CiscoTsPortStatsNumber_Type())
ciscoTsPortStatsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsNumber.setStatus(_A)
class _CiscoTsPortStatsModNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CiscoTsPortStatsModNumber_Type.__name__=_C
_CiscoTsPortStatsModNumber_Object=MibTableColumn
ciscoTsPortStatsModNumber=_CiscoTsPortStatsModNumber_Object((1,3,6,1,4,1,9,5,32,4,2,1,2),_CiscoTsPortStatsModNumber_Type())
ciscoTsPortStatsModNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsModNumber.setStatus(_A)
_CiscoTsPortStatsIfIndex_Type=Integer32
_CiscoTsPortStatsIfIndex_Object=MibTableColumn
ciscoTsPortStatsIfIndex=_CiscoTsPortStatsIfIndex_Object((1,3,6,1,4,1,9,5,32,4,2,1,3),_CiscoTsPortStatsIfIndex_Type())
ciscoTsPortStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsIfIndex.setStatus(_A)
_CiscoTsPortStatsRcvLocalFrames_Type=Counter32
_CiscoTsPortStatsRcvLocalFrames_Object=MibTableColumn
ciscoTsPortStatsRcvLocalFrames=_CiscoTsPortStatsRcvLocalFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,4),_CiscoTsPortStatsRcvLocalFrames_Type())
ciscoTsPortStatsRcvLocalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsRcvLocalFrames.setStatus(_A)
_CiscoTsPortStatsForwardedFrames_Type=Counter32
_CiscoTsPortStatsForwardedFrames_Object=MibTableColumn
ciscoTsPortStatsForwardedFrames=_CiscoTsPortStatsForwardedFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,5),_CiscoTsPortStatsForwardedFrames_Type())
ciscoTsPortStatsForwardedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsForwardedFrames.setStatus(_A)
_CiscoTsPortStatsStations_Type=Counter32
_CiscoTsPortStatsStations_Object=MibTableColumn
ciscoTsPortStatsStations=_CiscoTsPortStatsStations_Object((1,3,6,1,4,1,9,5,32,4,2,1,6),_CiscoTsPortStatsStations_Type())
ciscoTsPortStatsStations.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsStations.setStatus(_A)
_CiscoTsPortStatsSWHandledFrames_Type=Counter32
_CiscoTsPortStatsSWHandledFrames_Object=MibTableColumn
ciscoTsPortStatsSWHandledFrames=_CiscoTsPortStatsSWHandledFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,7),_CiscoTsPortStatsSWHandledFrames_Type())
ciscoTsPortStatsSWHandledFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsSWHandledFrames.setStatus(_A)
_CiscoTsPortStatsLocalStations_Type=Counter32
_CiscoTsPortStatsLocalStations_Object=MibTableColumn
ciscoTsPortStatsLocalStations=_CiscoTsPortStatsLocalStations_Object((1,3,6,1,4,1,9,5,32,4,2,1,8),_CiscoTsPortStatsLocalStations_Type())
ciscoTsPortStatsLocalStations.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsLocalStations.setStatus(_A)
_CiscoTsPortStatsRemoteStations_Type=Counter32
_CiscoTsPortStatsRemoteStations_Object=MibTableColumn
ciscoTsPortStatsRemoteStations=_CiscoTsPortStatsRemoteStations_Object((1,3,6,1,4,1,9,5,32,4,2,1,9),_CiscoTsPortStatsRemoteStations_Type())
ciscoTsPortStatsRemoteStations.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsRemoteStations.setStatus(_A)
_CiscoTsPortStatsUnknownStaFrames_Type=Counter32
_CiscoTsPortStatsUnknownStaFrames_Object=MibTableColumn
ciscoTsPortStatsUnknownStaFrames=_CiscoTsPortStatsUnknownStaFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,10),_CiscoTsPortStatsUnknownStaFrames_Type())
ciscoTsPortStatsUnknownStaFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsUnknownStaFrames.setStatus(_A)
_CiscoTsPortStatsResetTimer_Type=TimeTicks
_CiscoTsPortStatsResetTimer_Object=MibTableColumn
ciscoTsPortStatsResetTimer=_CiscoTsPortStatsResetTimer_Object((1,3,6,1,4,1,9,5,32,4,2,1,11),_CiscoTsPortStatsResetTimer_Type())
ciscoTsPortStatsResetTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsResetTimer.setStatus(_A)
_CiscoTsPortStatsInFrames_Type=Counter32
_CiscoTsPortStatsInFrames_Object=MibTableColumn
ciscoTsPortStatsInFrames=_CiscoTsPortStatsInFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,12),_CiscoTsPortStatsInFrames_Type())
ciscoTsPortStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsInFrames.setStatus(_A)
_CiscoTsPortStatsOutFrames_Type=Counter32
_CiscoTsPortStatsOutFrames_Object=MibTableColumn
ciscoTsPortStatsOutFrames=_CiscoTsPortStatsOutFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,13),_CiscoTsPortStatsOutFrames_Type())
ciscoTsPortStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsOutFrames.setStatus(_A)
_CiscoTsPortStatsLongFrames_Type=Counter32
_CiscoTsPortStatsLongFrames_Object=MibTableColumn
ciscoTsPortStatsLongFrames=_CiscoTsPortStatsLongFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,14),_CiscoTsPortStatsLongFrames_Type())
ciscoTsPortStatsLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsLongFrames.setStatus(_A)
_CiscoTsPortStatsShortFrames_Type=Counter32
_CiscoTsPortStatsShortFrames_Object=MibTableColumn
ciscoTsPortStatsShortFrames=_CiscoTsPortStatsShortFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,15),_CiscoTsPortStatsShortFrames_Type())
ciscoTsPortStatsShortFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsShortFrames.setStatus(_A)
_CiscoTsPortStatsInBufOverflows_Type=Counter32
_CiscoTsPortStatsInBufOverflows_Object=MibTableColumn
ciscoTsPortStatsInBufOverflows=_CiscoTsPortStatsInBufOverflows_Object((1,3,6,1,4,1,9,5,32,4,2,1,16),_CiscoTsPortStatsInBufOverflows_Type())
ciscoTsPortStatsInBufOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsInBufOverflows.setStatus(_A)
_CiscoTsPortStatsOutBufOverflows_Type=Counter32
_CiscoTsPortStatsOutBufOverflows_Object=MibTableColumn
ciscoTsPortStatsOutBufOverflows=_CiscoTsPortStatsOutBufOverflows_Object((1,3,6,1,4,1,9,5,32,4,2,1,17),_CiscoTsPortStatsOutBufOverflows_Type())
ciscoTsPortStatsOutBufOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsOutBufOverflows.setStatus(_A)
_CiscoTsPortStatsRcvBcasts_Type=Counter32
_CiscoTsPortStatsRcvBcasts_Object=MibTableColumn
ciscoTsPortStatsRcvBcasts=_CiscoTsPortStatsRcvBcasts_Object((1,3,6,1,4,1,9,5,32,4,2,1,18),_CiscoTsPortStatsRcvBcasts_Type())
ciscoTsPortStatsRcvBcasts.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsRcvBcasts.setStatus(_A)
_CiscoTsPortStatsRcvMcasts_Type=Counter32
_CiscoTsPortStatsRcvMcasts_Object=MibTableColumn
ciscoTsPortStatsRcvMcasts=_CiscoTsPortStatsRcvMcasts_Object((1,3,6,1,4,1,9,5,32,4,2,1,19),_CiscoTsPortStatsRcvMcasts_Type())
ciscoTsPortStatsRcvMcasts.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsRcvMcasts.setStatus(_A)
_CiscoTsPortStatsSwitchedFrames_Type=Counter32
_CiscoTsPortStatsSwitchedFrames_Object=MibTableColumn
ciscoTsPortStatsSwitchedFrames=_CiscoTsPortStatsSwitchedFrames_Object((1,3,6,1,4,1,9,5,32,4,2,1,20),_CiscoTsPortStatsSwitchedFrames_Type())
ciscoTsPortStatsSwitchedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsSwitchedFrames.setStatus(_A)
_CiscoTsPortStatsPktsInErrors_Type=Counter32
_CiscoTsPortStatsPktsInErrors_Object=MibTableColumn
ciscoTsPortStatsPktsInErrors=_CiscoTsPortStatsPktsInErrors_Object((1,3,6,1,4,1,9,5,32,4,2,1,21),_CiscoTsPortStatsPktsInErrors_Type())
ciscoTsPortStatsPktsInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsPktsInErrors.setStatus(_A)
_CiscoTsPortStatsAddrChainOverflows_Type=Counter32
_CiscoTsPortStatsAddrChainOverflows_Object=MibTableColumn
ciscoTsPortStatsAddrChainOverflows=_CiscoTsPortStatsAddrChainOverflows_Object((1,3,6,1,4,1,9,5,32,4,2,1,22),_CiscoTsPortStatsAddrChainOverflows_Type())
ciscoTsPortStatsAddrChainOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsAddrChainOverflows.setStatus(_A)
_CiscoTsPortStatsTableOverflows_Type=Counter32
_CiscoTsPortStatsTableOverflows_Object=MibTableColumn
ciscoTsPortStatsTableOverflows=_CiscoTsPortStatsTableOverflows_Object((1,3,6,1,4,1,9,5,32,4,2,1,23),_CiscoTsPortStatsTableOverflows_Type())
ciscoTsPortStatsTableOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsTableOverflows.setStatus(_A)
_CiscoTsPortStatsCfgLoss_Type=Integer32
_CiscoTsPortStatsCfgLoss_Object=MibTableColumn
ciscoTsPortStatsCfgLoss=_CiscoTsPortStatsCfgLoss_Object((1,3,6,1,4,1,9,5,32,4,2,1,24),_CiscoTsPortStatsCfgLoss_Type())
ciscoTsPortStatsCfgLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsCfgLoss.setStatus(_A)
class _CiscoTsPortStatsCfgLossRC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wire-fault',1),('lobe-test-fail',2),('tkp-mac-frame-rcv-in-txi-mode',3),('heart-beat-fail',4),('txi-new-station',5),('txi-protocol-error',6),('no-cfg-loss',7)))
_CiscoTsPortStatsCfgLossRC_Type.__name__=_C
_CiscoTsPortStatsCfgLossRC_Object=MibTableColumn
ciscoTsPortStatsCfgLossRC=_CiscoTsPortStatsCfgLossRC_Object((1,3,6,1,4,1,9,5,32,4,2,1,25),_CiscoTsPortStatsCfgLossRC_Type())
ciscoTsPortStatsCfgLossRC.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsCfgLossRC.setStatus(_A)
class _CiscoTsPortStatsTrCRF_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CiscoTsPortStatsTrCRF_Type.__name__=_I
_CiscoTsPortStatsTrCRF_Object=MibTableColumn
ciscoTsPortStatsTrCRF=_CiscoTsPortStatsTrCRF_Object((1,3,6,1,4,1,9,5,32,4,2,1,26),_CiscoTsPortStatsTrCRF_Type())
ciscoTsPortStatsTrCRF.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsTrCRF.setStatus(_A)
class _CiscoTsPortStatsAutoDisableRC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('not-disabled',1),(_J,2),('speed-error',3),('remove-received',4),('disabled-by-DRiP',5)))
_CiscoTsPortStatsAutoDisableRC_Type.__name__=_C
_CiscoTsPortStatsAutoDisableRC_Object=MibTableColumn
ciscoTsPortStatsAutoDisableRC=_CiscoTsPortStatsAutoDisableRC_Object((1,3,6,1,4,1,9,5,32,4,2,1,27),_CiscoTsPortStatsAutoDisableRC_Type())
ciscoTsPortStatsAutoDisableRC.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPortStatsAutoDisableRC.setStatus(_A)
_CiscoTsProbe_ObjectIdentity=ObjectIdentity
ciscoTsProbe=_CiscoTsProbe_ObjectIdentity((1,3,6,1,4,1,9,5,32,5))
_CiscoTsPassiveProbeTable_Object=MibTable
ciscoTsPassiveProbeTable=_CiscoTsPassiveProbeTable_Object((1,3,6,1,4,1,9,5,32,5,1))
if mibBuilder.loadTexts:ciscoTsPassiveProbeTable.setStatus(_A)
_CiscoTsPassiveProbeEntry_Object=MibTableRow
ciscoTsPassiveProbeEntry=_CiscoTsPassiveProbeEntry_Object((1,3,6,1,4,1,9,5,32,5,1,1))
ciscoTsPassiveProbeEntry.setIndexNames((0,_E,_L),(0,_E,_x))
if mibBuilder.loadTexts:ciscoTsPassiveProbeEntry.setStatus(_A)
class _CiscoTsPassiveProbeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CiscoTsPassiveProbeIndex_Type.__name__=_C
_CiscoTsPassiveProbeIndex_Object=MibTableColumn
ciscoTsPassiveProbeIndex=_CiscoTsPassiveProbeIndex_Object((1,3,6,1,4,1,9,5,32,5,1,1,1),_CiscoTsPassiveProbeIndex_Type())
ciscoTsPassiveProbeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPassiveProbeIndex.setStatus(_A)
class _CiscoTsPassiveProbePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_CiscoTsPassiveProbePort_Type.__name__=_C
_CiscoTsPassiveProbePort_Object=MibTableColumn
ciscoTsPassiveProbePort=_CiscoTsPassiveProbePort_Object((1,3,6,1,4,1,9,5,32,5,1,1,2),_CiscoTsPassiveProbePort_Type())
ciscoTsPassiveProbePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPassiveProbePort.setStatus(_A)
class _CiscoTsPassiveProbeMonitoredPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_CiscoTsPassiveProbeMonitoredPort_Type.__name__=_C
_CiscoTsPassiveProbeMonitoredPort_Object=MibTableColumn
ciscoTsPassiveProbeMonitoredPort=_CiscoTsPassiveProbeMonitoredPort_Object((1,3,6,1,4,1,9,5,32,5,1,1,3),_CiscoTsPassiveProbeMonitoredPort_Type())
ciscoTsPassiveProbeMonitoredPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsPassiveProbeMonitoredPort.setStatus(_A)
class _CiscoTsPassiveProbeDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('transmit',1),('receive',2),('both',3),(_J,4)))
_CiscoTsPassiveProbeDirection_Type.__name__=_C
_CiscoTsPassiveProbeDirection_Object=MibTableColumn
ciscoTsPassiveProbeDirection=_CiscoTsPassiveProbeDirection_Object((1,3,6,1,4,1,9,5,32,5,1,1,4),_CiscoTsPassiveProbeDirection_Type())
ciscoTsPassiveProbeDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsPassiveProbeDirection.setStatus(_A)
_CiscoTsVLANS_ObjectIdentity=ObjectIdentity
ciscoTsVLANS=_CiscoTsVLANS_ObjectIdentity((1,3,6,1,4,1,9,5,32,6))
_CiscoTsTrCRFInfoTable_Object=MibTable
ciscoTsTrCRFInfoTable=_CiscoTsTrCRFInfoTable_Object((1,3,6,1,4,1,9,5,32,6,1))
if mibBuilder.loadTexts:ciscoTsTrCRFInfoTable.setStatus(_A)
_CiscoTsTrCRFInfoEntry_Object=MibTableRow
ciscoTsTrCRFInfoEntry=_CiscoTsTrCRFInfoEntry_Object((1,3,6,1,4,1,9,5,32,6,1,1))
ciscoTsTrCRFInfoEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:ciscoTsTrCRFInfoEntry.setStatus(_A)
class _CiscoTsTrCRFInfoTrCRFNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CiscoTsTrCRFInfoTrCRFNumber_Type.__name__=_C
_CiscoTsTrCRFInfoTrCRFNumber_Object=MibTableColumn
ciscoTsTrCRFInfoTrCRFNumber=_CiscoTsTrCRFInfoTrCRFNumber_Object((1,3,6,1,4,1,9,5,32,6,1,1,1),_CiscoTsTrCRFInfoTrCRFNumber_Type())
ciscoTsTrCRFInfoTrCRFNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTrCRFInfoTrCRFNumber.setStatus(_A)
class _CiscoTsTrCRFInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiscoTsTrCRFInfoName_Type.__name__=_K
_CiscoTsTrCRFInfoName_Object=MibTableColumn
ciscoTsTrCRFInfoName=_CiscoTsTrCRFInfoName_Object((1,3,6,1,4,1,9,5,32,6,1,1,2),_CiscoTsTrCRFInfoName_Type())
ciscoTsTrCRFInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTrCRFInfoName.setStatus(_A)
class _CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('cisco',2),('ieee',3),(_R,4)))
_CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Type.__name__=_C
_CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Object=MibTableColumn
ciscoTsTrCRFInfoSpanningTreeProtoSpecification=_CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Object((1,3,6,1,4,1,9,5,32,6,1,1,3),_CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Type())
ciscoTsTrCRFInfoSpanningTreeProtoSpecification.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrCRFInfoSpanningTreeProtoSpecification.setStatus(_A)
_CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Type=Timeout
_CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Object=MibTableColumn
ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay=_CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Object((1,3,6,1,4,1,9,5,32,6,1,1,4),_CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Type())
ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay.setStatus(_A)
_CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Type=Timeout
_CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Object=MibTableColumn
ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime=_CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Object((1,3,6,1,4,1,9,5,32,6,1,1,5),_CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Type())
ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime.setStatus(_A)
_CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Type=Timeout
_CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Object=MibTableColumn
ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge=_CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Object((1,3,6,1,4,1,9,5,32,6,1,1,6),_CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Type())
ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge.setStatus(_A)
class _CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_u,2),(_v,3)))
_CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Type.__name__=_C
_CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Object=MibTableColumn
ciscoTsTrCRFInfoSpanningTreeInternalPortMode=_CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Object((1,3,6,1,4,1,9,5,32,6,1,1,7),_CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Type())
ciscoTsTrCRFInfoSpanningTreeInternalPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrCRFInfoSpanningTreeInternalPortMode.setStatus(_A)
_CiscoTsTrBRFInfoTable_Object=MibTable
ciscoTsTrBRFInfoTable=_CiscoTsTrBRFInfoTable_Object((1,3,6,1,4,1,9,5,32,6,2))
if mibBuilder.loadTexts:ciscoTsTrBRFInfoTable.setStatus(_A)
_CiscoTsTrBRFInfoEntry_Object=MibTableRow
ciscoTsTrBRFInfoEntry=_CiscoTsTrBRFInfoEntry_Object((1,3,6,1,4,1,9,5,32,6,2,1))
ciscoTsTrBRFInfoEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:ciscoTsTrBRFInfoEntry.setStatus(_A)
class _CiscoTsTrBRFInfoTrBRFNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CiscoTsTrBRFInfoTrBRFNumber_Type.__name__=_C
_CiscoTsTrBRFInfoTrBRFNumber_Object=MibTableColumn
ciscoTsTrBRFInfoTrBRFNumber=_CiscoTsTrBRFInfoTrBRFNumber_Object((1,3,6,1,4,1,9,5,32,6,2,1,1),_CiscoTsTrBRFInfoTrBRFNumber_Type())
ciscoTsTrBRFInfoTrBRFNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoTrBRFNumber.setStatus(_A)
class _CiscoTsTrBRFInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiscoTsTrBRFInfoName_Type.__name__=_K
_CiscoTsTrBRFInfoName_Object=MibTableColumn
ciscoTsTrBRFInfoName=_CiscoTsTrBRFInfoName_Object((1,3,6,1,4,1,9,5,32,6,2,1,2),_CiscoTsTrBRFInfoName_Type())
ciscoTsTrBRFInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoName.setStatus(_A)
class _CiscoTsTrBRFInfoIpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip-disabled',1),('bootp-when-needed',2),('bootp-always',3)))
_CiscoTsTrBRFInfoIpState_Type.__name__=_C
_CiscoTsTrBRFInfoIpState_Object=MibTableColumn
ciscoTsTrBRFInfoIpState=_CiscoTsTrBRFInfoIpState_Object((1,3,6,1,4,1,9,5,32,6,2,1,3),_CiscoTsTrBRFInfoIpState_Type())
ciscoTsTrBRFInfoIpState.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoIpState.setStatus(_A)
_CiscoTsTrBRFInfoIpAddress_Type=IpAddress
_CiscoTsTrBRFInfoIpAddress_Object=MibTableColumn
ciscoTsTrBRFInfoIpAddress=_CiscoTsTrBRFInfoIpAddress_Object((1,3,6,1,4,1,9,5,32,6,2,1,4),_CiscoTsTrBRFInfoIpAddress_Type())
ciscoTsTrBRFInfoIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoIpAddress.setStatus(_A)
_CiscoTsTrBRFInfoIpSubnetMask_Type=IpAddress
_CiscoTsTrBRFInfoIpSubnetMask_Object=MibTableColumn
ciscoTsTrBRFInfoIpSubnetMask=_CiscoTsTrBRFInfoIpSubnetMask_Object((1,3,6,1,4,1,9,5,32,6,2,1,5),_CiscoTsTrBRFInfoIpSubnetMask_Type())
ciscoTsTrBRFInfoIpSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoIpSubnetMask.setStatus(_A)
_CiscoTsTrBRFInfoIpDefaultGateway_Type=IpAddress
_CiscoTsTrBRFInfoIpDefaultGateway_Object=MibTableColumn
ciscoTsTrBRFInfoIpDefaultGateway=_CiscoTsTrBRFInfoIpDefaultGateway_Object((1,3,6,1,4,1,9,5,32,6,2,1,6),_CiscoTsTrBRFInfoIpDefaultGateway_Type())
ciscoTsTrBRFInfoIpDefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoIpDefaultGateway.setStatus(_A)
class _CiscoTsTrBRFInfoStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CiscoTsTrBRFInfoStpMode_Type.__name__=_C
_CiscoTsTrBRFInfoStpMode_Object=MibTableColumn
ciscoTsTrBRFInfoStpMode=_CiscoTsTrBRFInfoStpMode_Object((1,3,6,1,4,1,9,5,32,6,2,1,7),_CiscoTsTrBRFInfoStpMode_Type())
ciscoTsTrBRFInfoStpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoStpMode.setStatus(_A)
class _CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Type.__name__=_C
_CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Object=MibTableColumn
ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr=_CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Object((1,3,6,1,4,1,9,5,32,6,2,1,8),_CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Type())
ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr.setStatus(_A)
class _CiscoTsTransitedConfiguredTrCRFs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CiscoTsTransitedConfiguredTrCRFs_Type.__name__=_I
_CiscoTsTransitedConfiguredTrCRFs_Object=MibScalar
ciscoTsTransitedConfiguredTrCRFs=_CiscoTsTransitedConfiguredTrCRFs_Object((1,3,6,1,4,1,9,5,32,6,3),_CiscoTsTransitedConfiguredTrCRFs_Type())
ciscoTsTransitedConfiguredTrCRFs.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTransitedConfiguredTrCRFs.setStatus(_A)
class _CiscoTsTransitedTrCRFs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CiscoTsTransitedTrCRFs_Type.__name__=_I
_CiscoTsTransitedTrCRFs_Object=MibScalar
ciscoTsTransitedTrCRFs=_CiscoTsTransitedTrCRFs_Object((1,3,6,1,4,1,9,5,32,6,4),_CiscoTsTransitedTrCRFs_Type())
ciscoTsTransitedTrCRFs.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTransitedTrCRFs.setStatus(_A)
class _CiscoTsTransitedConfiguredTrBRFs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CiscoTsTransitedConfiguredTrBRFs_Type.__name__=_I
_CiscoTsTransitedConfiguredTrBRFs_Object=MibScalar
ciscoTsTransitedConfiguredTrBRFs=_CiscoTsTransitedConfiguredTrBRFs_Object((1,3,6,1,4,1,9,5,32,6,5),_CiscoTsTransitedConfiguredTrBRFs_Type())
ciscoTsTransitedConfiguredTrBRFs.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTransitedConfiguredTrBRFs.setStatus(_A)
class _CiscoTsTransitedTrBRFs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CiscoTsTransitedTrBRFs_Type.__name__=_I
_CiscoTsTransitedTrBRFs_Object=MibScalar
ciscoTsTransitedTrBRFs=_CiscoTsTransitedTrBRFs_Object((1,3,6,1,4,1,9,5,32,6,6),_CiscoTsTransitedTrBRFs_Type())
ciscoTsTransitedTrBRFs.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTransitedTrBRFs.setStatus(_A)
_CiscoTsTChannel_ObjectIdentity=ObjectIdentity
ciscoTsTChannel=_CiscoTsTChannel_ObjectIdentity((1,3,6,1,4,1,9,5,32,7))
_CiscoTsTCTable_Object=MibTable
ciscoTsTCTable=_CiscoTsTCTable_Object((1,3,6,1,4,1,9,5,32,7,1))
if mibBuilder.loadTexts:ciscoTsTCTable.setStatus(_A)
_CiscoTsTCEntry_Object=MibTableRow
ciscoTsTCEntry=_CiscoTsTCEntry_Object((1,3,6,1,4,1,9,5,32,7,1,1))
ciscoTsTCEntry.setIndexNames((0,_E,_y),(0,_E,_z))
if mibBuilder.loadTexts:ciscoTsTCEntry.setStatus(_A)
class _CiscoTsTCSwitchNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsTCSwitchNumber_Type.__name__=_C
_CiscoTsTCSwitchNumber_Object=MibTableColumn
ciscoTsTCSwitchNumber=_CiscoTsTCSwitchNumber_Object((1,3,6,1,4,1,9,5,32,7,1,1,1),_CiscoTsTCSwitchNumber_Type())
ciscoTsTCSwitchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTCSwitchNumber.setStatus(_A)
class _CiscoTsTCNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsTCNumber_Type.__name__=_C
_CiscoTsTCNumber_Object=MibTableColumn
ciscoTsTCNumber=_CiscoTsTCNumber_Object((1,3,6,1,4,1,9,5,32,7,1,1,2),_CiscoTsTCNumber_Type())
ciscoTsTCNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTCNumber.setStatus(_A)
class _CiscoTsTCPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoTsTCPorts_Type.__name__=_I
_CiscoTsTCPorts_Object=MibTableColumn
ciscoTsTCPorts=_CiscoTsTCPorts_Object((1,3,6,1,4,1,9,5,32,7,1,1,3),_CiscoTsTCPorts_Type())
ciscoTsTCPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTCPorts.setStatus(_A)
class _CiscoTsTCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('reduced',3)))
_CiscoTsTCStatus_Type.__name__=_C
_CiscoTsTCStatus_Object=MibTableColumn
ciscoTsTCStatus=_CiscoTsTCStatus_Object((1,3,6,1,4,1,9,5,32,7,1,1,4),_CiscoTsTCStatus_Type())
ciscoTsTCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTCStatus.setStatus(_A)
class _CiscoTsTCActivePorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoTsTCActivePorts_Type.__name__=_I
_CiscoTsTCActivePorts_Object=MibTableColumn
ciscoTsTCActivePorts=_CiscoTsTCActivePorts_Object((1,3,6,1,4,1,9,5,32,7,1,1,5),_CiscoTsTCActivePorts_Type())
ciscoTsTCActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTCActivePorts.setStatus(_A)
_CiscoTsFilter_ObjectIdentity=ObjectIdentity
ciscoTsFilter=_CiscoTsFilter_ObjectIdentity((1,3,6,1,4,1,9,5,32,8))
_CiscoTsProtocolClassFilterTable_Object=MibTable
ciscoTsProtocolClassFilterTable=_CiscoTsProtocolClassFilterTable_Object((1,3,6,1,4,1,9,5,32,8,1))
if mibBuilder.loadTexts:ciscoTsProtocolClassFilterTable.setStatus(_A)
_CiscoTsProtocolClassFilterEntry_Object=MibTableRow
ciscoTsProtocolClassFilterEntry=_CiscoTsProtocolClassFilterEntry_Object((1,3,6,1,4,1,9,5,32,8,1,1))
ciscoTsProtocolClassFilterEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:ciscoTsProtocolClassFilterEntry.setStatus(_A)
class _CiscoTsProtocolClassFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CiscoTsProtocolClassFilterIndex_Type.__name__=_C
_CiscoTsProtocolClassFilterIndex_Object=MibTableColumn
ciscoTsProtocolClassFilterIndex=_CiscoTsProtocolClassFilterIndex_Object((1,3,6,1,4,1,9,5,32,8,1,1,1),_CiscoTsProtocolClassFilterIndex_Type())
ciscoTsProtocolClassFilterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsProtocolClassFilterIndex.setStatus(_A)
_CiscoTsProtocolClassFilterEtype_Type=OctetString
_CiscoTsProtocolClassFilterEtype_Object=MibTableColumn
ciscoTsProtocolClassFilterEtype=_CiscoTsProtocolClassFilterEtype_Object((1,3,6,1,4,1,9,5,32,8,1,1,2),_CiscoTsProtocolClassFilterEtype_Type())
ciscoTsProtocolClassFilterEtype.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsProtocolClassFilterEtype.setStatus(_A)
_CiscoTsProtocolClassFilterDSAPs_Type=OctetString
_CiscoTsProtocolClassFilterDSAPs_Object=MibTableColumn
ciscoTsProtocolClassFilterDSAPs=_CiscoTsProtocolClassFilterDSAPs_Object((1,3,6,1,4,1,9,5,32,8,1,1,3),_CiscoTsProtocolClassFilterDSAPs_Type())
ciscoTsProtocolClassFilterDSAPs.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsProtocolClassFilterDSAPs.setStatus(_A)
_CiscoTsProtocolFilterTable_Object=MibTable
ciscoTsProtocolFilterTable=_CiscoTsProtocolFilterTable_Object((1,3,6,1,4,1,9,5,32,8,2))
if mibBuilder.loadTexts:ciscoTsProtocolFilterTable.setStatus(_A)
_CiscoTsProtocolFilterEntry_Object=MibTableRow
ciscoTsProtocolFilterEntry=_CiscoTsProtocolFilterEntry_Object((1,3,6,1,4,1,9,5,32,8,2,1))
ciscoTsProtocolFilterEntry.setIndexNames((0,_E,_L),(0,_E,_A0),(0,_E,_V))
if mibBuilder.loadTexts:ciscoTsProtocolFilterEntry.setStatus(_A)
class _CiscoTsProtocolFilterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiscoTsProtocolFilterPort_Type.__name__=_C
_CiscoTsProtocolFilterPort_Object=MibTableColumn
ciscoTsProtocolFilterPort=_CiscoTsProtocolFilterPort_Object((1,3,6,1,4,1,9,5,32,8,2,1,1),_CiscoTsProtocolFilterPort_Type())
ciscoTsProtocolFilterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsProtocolFilterPort.setStatus(_A)
class _CiscoTsProtocolFilterBlockingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('sr',2),('nsr',3),(_O,4)))
_CiscoTsProtocolFilterBlockingMode_Type.__name__=_C
_CiscoTsProtocolFilterBlockingMode_Object=MibTableColumn
ciscoTsProtocolFilterBlockingMode=_CiscoTsProtocolFilterBlockingMode_Object((1,3,6,1,4,1,9,5,32,8,2,1,2),_CiscoTsProtocolFilterBlockingMode_Type())
ciscoTsProtocolFilterBlockingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsProtocolFilterBlockingMode.setStatus(_A)
class _CiscoTsProtocolFilterTranspMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CiscoTsProtocolFilterTranspMode_Type.__name__=_C
_CiscoTsProtocolFilterTranspMode_Object=MibTableColumn
ciscoTsProtocolFilterTranspMode=_CiscoTsProtocolFilterTranspMode_Object((1,3,6,1,4,1,9,5,32,8,2,1,3),_CiscoTsProtocolFilterTranspMode_Type())
ciscoTsProtocolFilterTranspMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsProtocolFilterTranspMode.setStatus(_A)
_CiscoTsMACDestFilterTable_Object=MibTable
ciscoTsMACDestFilterTable=_CiscoTsMACDestFilterTable_Object((1,3,6,1,4,1,9,5,32,8,3))
if mibBuilder.loadTexts:ciscoTsMACDestFilterTable.setStatus(_A)
_CiscoTsMACDestFilterEntry_Object=MibTableRow
ciscoTsMACDestFilterEntry=_CiscoTsMACDestFilterEntry_Object((1,3,6,1,4,1,9,5,32,8,3,1))
ciscoTsMACDestFilterEntry.setIndexNames((0,_E,_A1),(0,_E,_A2),(0,_E,_A3))
if mibBuilder.loadTexts:ciscoTsMACDestFilterEntry.setStatus(_A)
class _CiscoTsMACDestFilterSwitchNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsMACDestFilterSwitchNumber_Type.__name__=_C
_CiscoTsMACDestFilterSwitchNumber_Object=MibTableColumn
ciscoTsMACDestFilterSwitchNumber=_CiscoTsMACDestFilterSwitchNumber_Object((1,3,6,1,4,1,9,5,32,8,3,1,1),_CiscoTsMACDestFilterSwitchNumber_Type())
ciscoTsMACDestFilterSwitchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsMACDestFilterSwitchNumber.setStatus(_A)
_CiscoTsMACDestFilterStationAddress_Type=MacAddr
_CiscoTsMACDestFilterStationAddress_Object=MibTableColumn
ciscoTsMACDestFilterStationAddress=_CiscoTsMACDestFilterStationAddress_Object((1,3,6,1,4,1,9,5,32,8,3,1,2),_CiscoTsMACDestFilterStationAddress_Type())
ciscoTsMACDestFilterStationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsMACDestFilterStationAddress.setStatus(_A)
class _CiscoTsMACDestFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('block-dest',1),('allow-dest',2),('limited-multicast',3),('force-dest',4)))
_CiscoTsMACDestFilterType_Type.__name__=_C
_CiscoTsMACDestFilterType_Object=MibTableColumn
ciscoTsMACDestFilterType=_CiscoTsMACDestFilterType_Object((1,3,6,1,4,1,9,5,32,8,3,1,3),_CiscoTsMACDestFilterType_Type())
ciscoTsMACDestFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACDestFilterType.setStatus(_A)
class _CiscoTsMACDestFilterPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoTsMACDestFilterPorts_Type.__name__=_I
_CiscoTsMACDestFilterPorts_Object=MibTableColumn
ciscoTsMACDestFilterPorts=_CiscoTsMACDestFilterPorts_Object((1,3,6,1,4,1,9,5,32,8,3,1,4),_CiscoTsMACDestFilterPorts_Type())
ciscoTsMACDestFilterPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACDestFilterPorts.setStatus(_A)
class _CiscoTsMACDestFilterExitMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoTsMACDestFilterExitMask_Type.__name__=_I
_CiscoTsMACDestFilterExitMask_Object=MibTableColumn
ciscoTsMACDestFilterExitMask=_CiscoTsMACDestFilterExitMask_Object((1,3,6,1,4,1,9,5,32,8,3,1,5),_CiscoTsMACDestFilterExitMask_Type())
ciscoTsMACDestFilterExitMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACDestFilterExitMask.setStatus(_A)
class _CiscoTsMACDestFilterRemoteBox_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsMACDestFilterRemoteBox_Type.__name__=_C
_CiscoTsMACDestFilterRemoteBox_Object=MibTableColumn
ciscoTsMACDestFilterRemoteBox=_CiscoTsMACDestFilterRemoteBox_Object((1,3,6,1,4,1,9,5,32,8,3,1,6),_CiscoTsMACDestFilterRemoteBox_Type())
ciscoTsMACDestFilterRemoteBox.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACDestFilterRemoteBox.setStatus(_A)
class _CiscoTsMACDestFilterRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiscoTsMACDestFilterRemotePort_Type.__name__=_C
_CiscoTsMACDestFilterRemotePort_Object=MibTableColumn
ciscoTsMACDestFilterRemotePort=_CiscoTsMACDestFilterRemotePort_Object((1,3,6,1,4,1,9,5,32,8,3,1,7),_CiscoTsMACDestFilterRemotePort_Type())
ciscoTsMACDestFilterRemotePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACDestFilterRemotePort.setStatus(_A)
class _CiscoTsMACDestFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_CiscoTsMACDestFilterStatus_Type.__name__=_C
_CiscoTsMACDestFilterStatus_Object=MibTableColumn
ciscoTsMACDestFilterStatus=_CiscoTsMACDestFilterStatus_Object((1,3,6,1,4,1,9,5,32,8,3,1,8),_CiscoTsMACDestFilterStatus_Type())
ciscoTsMACDestFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACDestFilterStatus.setStatus(_A)
_CiscoTsMACSourceFilterTable_Object=MibTable
ciscoTsMACSourceFilterTable=_CiscoTsMACSourceFilterTable_Object((1,3,6,1,4,1,9,5,32,8,4))
if mibBuilder.loadTexts:ciscoTsMACSourceFilterTable.setStatus(_A)
_CiscoTsMACSourceFilterEntry_Object=MibTableRow
ciscoTsMACSourceFilterEntry=_CiscoTsMACSourceFilterEntry_Object((1,3,6,1,4,1,9,5,32,8,4,1))
ciscoTsMACSourceFilterEntry.setIndexNames((0,_E,_A4),(0,_E,_A5),(0,_E,_A6))
if mibBuilder.loadTexts:ciscoTsMACSourceFilterEntry.setStatus(_A)
class _CiscoTsMACSourceFilterSwitchNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsMACSourceFilterSwitchNumber_Type.__name__=_C
_CiscoTsMACSourceFilterSwitchNumber_Object=MibTableColumn
ciscoTsMACSourceFilterSwitchNumber=_CiscoTsMACSourceFilterSwitchNumber_Object((1,3,6,1,4,1,9,5,32,8,4,1,1),_CiscoTsMACSourceFilterSwitchNumber_Type())
ciscoTsMACSourceFilterSwitchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsMACSourceFilterSwitchNumber.setStatus(_A)
_CiscoTsMACSourceFilterStationAddress_Type=MacAddr
_CiscoTsMACSourceFilterStationAddress_Object=MibTableColumn
ciscoTsMACSourceFilterStationAddress=_CiscoTsMACSourceFilterStationAddress_Object((1,3,6,1,4,1,9,5,32,8,4,1,2),_CiscoTsMACSourceFilterStationAddress_Type())
ciscoTsMACSourceFilterStationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsMACSourceFilterStationAddress.setStatus(_A)
class _CiscoTsMACSourceFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('block-source',1),('allow-source',2)))
_CiscoTsMACSourceFilterType_Type.__name__=_C
_CiscoTsMACSourceFilterType_Object=MibTableColumn
ciscoTsMACSourceFilterType=_CiscoTsMACSourceFilterType_Object((1,3,6,1,4,1,9,5,32,8,4,1,3),_CiscoTsMACSourceFilterType_Type())
ciscoTsMACSourceFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACSourceFilterType.setStatus(_A)
class _CiscoTsMACSourceFilterPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoTsMACSourceFilterPorts_Type.__name__=_I
_CiscoTsMACSourceFilterPorts_Object=MibTableColumn
ciscoTsMACSourceFilterPorts=_CiscoTsMACSourceFilterPorts_Object((1,3,6,1,4,1,9,5,32,8,4,1,4),_CiscoTsMACSourceFilterPorts_Type())
ciscoTsMACSourceFilterPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACSourceFilterPorts.setStatus(_A)
class _CiscoTsMACSourceFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_CiscoTsMACSourceFilterStatus_Type.__name__=_C
_CiscoTsMACSourceFilterStatus_Object=MibTableColumn
ciscoTsMACSourceFilterStatus=_CiscoTsMACSourceFilterStatus_Object((1,3,6,1,4,1,9,5,32,8,4,1,5),_CiscoTsMACSourceFilterStatus_Type())
ciscoTsMACSourceFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsMACSourceFilterStatus.setStatus(_A)
_CiscoTsDupAddrFilterTable_Object=MibTable
ciscoTsDupAddrFilterTable=_CiscoTsDupAddrFilterTable_Object((1,3,6,1,4,1,9,5,32,8,5))
if mibBuilder.loadTexts:ciscoTsDupAddrFilterTable.setStatus(_A)
_CiscoTsDupAddrFilterEntry_Object=MibTableRow
ciscoTsDupAddrFilterEntry=_CiscoTsDupAddrFilterEntry_Object((1,3,6,1,4,1,9,5,32,8,5,1))
ciscoTsDupAddrFilterEntry.setIndexNames((0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:ciscoTsDupAddrFilterEntry.setStatus(_A)
class _CiscoTsDupAddrFilterSwitchNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiscoTsDupAddrFilterSwitchNumber_Type.__name__=_C
_CiscoTsDupAddrFilterSwitchNumber_Object=MibTableColumn
ciscoTsDupAddrFilterSwitchNumber=_CiscoTsDupAddrFilterSwitchNumber_Object((1,3,6,1,4,1,9,5,32,8,5,1,1),_CiscoTsDupAddrFilterSwitchNumber_Type())
ciscoTsDupAddrFilterSwitchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsDupAddrFilterSwitchNumber.setStatus(_A)
_CiscoTsDupAddrFilterStationAddress_Type=MacAddr
_CiscoTsDupAddrFilterStationAddress_Object=MibTableColumn
ciscoTsDupAddrFilterStationAddress=_CiscoTsDupAddrFilterStationAddress_Object((1,3,6,1,4,1,9,5,32,8,5,1,2),_CiscoTsDupAddrFilterStationAddress_Type())
ciscoTsDupAddrFilterStationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsDupAddrFilterStationAddress.setStatus(_A)
class _CiscoTsDupAddrFilterPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoTsDupAddrFilterPorts_Type.__name__=_I
_CiscoTsDupAddrFilterPorts_Object=MibTableColumn
ciscoTsDupAddrFilterPorts=_CiscoTsDupAddrFilterPorts_Object((1,3,6,1,4,1,9,5,32,8,5,1,3),_CiscoTsDupAddrFilterPorts_Type())
ciscoTsDupAddrFilterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsDupAddrFilterPorts.setStatus(_A)
_CiscoTsTrunkProtocolFilterTable_Object=MibTable
ciscoTsTrunkProtocolFilterTable=_CiscoTsTrunkProtocolFilterTable_Object((1,3,6,1,4,1,9,5,32,8,6))
if mibBuilder.loadTexts:ciscoTsTrunkProtocolFilterTable.setStatus(_A)
_CiscoTsTrunkProtocolFilterEntry_Object=MibTableRow
ciscoTsTrunkProtocolFilterEntry=_CiscoTsTrunkProtocolFilterEntry_Object((1,3,6,1,4,1,9,5,32,8,6,1))
ciscoTsTrunkProtocolFilterEntry.setIndexNames((0,_E,_L),(0,_E,_A9),(0,_E,_S),(0,_E,_V))
if mibBuilder.loadTexts:ciscoTsTrunkProtocolFilterEntry.setStatus(_A)
class _CiscoTsTrunkProtocolFilterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiscoTsTrunkProtocolFilterPort_Type.__name__=_C
_CiscoTsTrunkProtocolFilterPort_Object=MibTableColumn
ciscoTsTrunkProtocolFilterPort=_CiscoTsTrunkProtocolFilterPort_Object((1,3,6,1,4,1,9,5,32,8,6,1,1),_CiscoTsTrunkProtocolFilterPort_Type())
ciscoTsTrunkProtocolFilterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoTsTrunkProtocolFilterPort.setStatus(_A)
class _CiscoTsTrunkProtocolFilterBlockingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('sr',2),('nsr',3),(_O,4)))
_CiscoTsTrunkProtocolFilterBlockingMode_Type.__name__=_C
_CiscoTsTrunkProtocolFilterBlockingMode_Object=MibTableColumn
ciscoTsTrunkProtocolFilterBlockingMode=_CiscoTsTrunkProtocolFilterBlockingMode_Object((1,3,6,1,4,1,9,5,32,8,6,1,2),_CiscoTsTrunkProtocolFilterBlockingMode_Type())
ciscoTsTrunkProtocolFilterBlockingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrunkProtocolFilterBlockingMode.setStatus(_A)
class _CiscoTsTrunkProtocolFilterTranspMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CiscoTsTrunkProtocolFilterTranspMode_Type.__name__=_C
_CiscoTsTrunkProtocolFilterTranspMode_Object=MibTableColumn
ciscoTsTrunkProtocolFilterTranspMode=_CiscoTsTrunkProtocolFilterTranspMode_Object((1,3,6,1,4,1,9,5,32,8,6,1,3),_CiscoTsTrunkProtocolFilterTranspMode_Type())
ciscoTsTrunkProtocolFilterTranspMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoTsTrunkProtocolFilterTranspMode.setStatus(_A)
_CiscoTsUplinkMIBs_ObjectIdentity=ObjectIdentity
ciscoTsUplinkMIBs=_CiscoTsUplinkMIBs_ObjectIdentity((1,3,6,1,4,1,9,5,32,9))
ciscoTsStackCfgChange=NotificationType((1,3,6,1,4,1,9,5,32,1,1,0,1))
ciscoTsStackCfgChange.setObjects(*((_F,_H),(_F,_G),(_E,_AA)))
if mibBuilder.loadTexts:ciscoTsStackCfgChange.setStatus('')
ciscoTsStackProStackMatrixChange=NotificationType((1,3,6,1,4,1,9,5,32,1,1,0,2))
ciscoTsStackProStackMatrixChange.setObjects(*((_F,_H),(_F,_G),(_E,_AB)))
if mibBuilder.loadTexts:ciscoTsStackProStackMatrixChange.setStatus('')
ciscoTsStackTempChange=NotificationType((1,3,6,1,4,1,9,5,32,2,0,3))
ciscoTsStackTempChange.setObjects(*((_F,_H),(_F,_G),(_E,_AC)))
if mibBuilder.loadTexts:ciscoTsStackTempChange.setStatus('')
ciscoTsStackPwrStatusChange=NotificationType((1,3,6,1,4,1,9,5,32,2,0,4))
ciscoTsStackPwrStatusChange.setObjects(*((_F,_H),(_F,_G),(_E,_AD)))
if mibBuilder.loadTexts:ciscoTsStackPwrStatusChange.setStatus('')
ciscoTsPortStrNFwdEntry=NotificationType((1,3,6,1,4,1,9,5,32,4,0,1))
ciscoTsPortStrNFwdEntry.setObjects(*((_F,_H),(_F,_G),(_E,_AE)))
if mibBuilder.loadTexts:ciscoTsPortStrNFwdEntry.setStatus('')
ciscoTsPortCfgLossTrap=NotificationType((1,3,6,1,4,1,9,5,32,4,0,2))
ciscoTsPortCfgLossTrap.setObjects(*((_F,_H),(_F,_G),(_E,_AF)))
if mibBuilder.loadTexts:ciscoTsPortCfgLossTrap.setStatus('')
ciscoTsBeaconStart=NotificationType((1,3,6,1,4,1,9,5,32,4,0,3))
ciscoTsBeaconStart.setObjects(*((_F,_H),(_F,_G),(_E,_N)))
if mibBuilder.loadTexts:ciscoTsBeaconStart.setStatus('')
ciscoTsBeaconEnd=NotificationType((1,3,6,1,4,1,9,5,32,4,0,4))
ciscoTsBeaconEnd.setObjects(*((_F,_H),(_F,_G),(_E,_N)))
if mibBuilder.loadTexts:ciscoTsBeaconEnd.setStatus('')
ciscoTsDuplicateMACAddr=NotificationType((1,3,6,1,4,1,9,5,32,4,0,5))
ciscoTsDuplicateMACAddr.setObjects(*((_F,_H),(_F,_G),(_E,_N)))
if mibBuilder.loadTexts:ciscoTsDuplicateMACAddr.setStatus('')
ciscoTsPortSoftErrExceededTrap=NotificationType((1,3,6,1,4,1,9,5,32,4,0,6))
ciscoTsPortSoftErrExceededTrap.setObjects(*((_F,_H),(_F,_G),(_E,_L),(_E,_N),(_W,_d),(_W,_e),(_a,_b)))
if mibBuilder.loadTexts:ciscoTsPortSoftErrExceededTrap.setStatus('')
ciscoTsTrCRFNewRoot=NotificationType((1,3,6,1,4,1,9,5,32,6,0,1))
ciscoTsTrCRFNewRoot.setObjects(*((_F,_H),(_F,_G),(_E,_S)))
if mibBuilder.loadTexts:ciscoTsTrCRFNewRoot.setStatus('')
ciscoTsTrCRFTopologyChange=NotificationType((1,3,6,1,4,1,9,5,32,6,0,2))
ciscoTsTrCRFTopologyChange.setObjects(*((_F,_H),(_F,_G),(_E,_S)))
if mibBuilder.loadTexts:ciscoTsTrCRFTopologyChange.setStatus('')
ciscoTsTrBRFNewRoot=NotificationType((1,3,6,1,4,1,9,5,32,6,0,3))
ciscoTsTrBRFNewRoot.setObjects(*((_F,_H),(_F,_G),(_E,_U)))
if mibBuilder.loadTexts:ciscoTsTrBRFNewRoot.setStatus('')
ciscoTsTrBRFTopologyChange=NotificationType((1,3,6,1,4,1,9,5,32,6,0,4))
ciscoTsTrBRFTopologyChange.setObjects(*((_F,_H),(_F,_G),(_E,_U)))
if mibBuilder.loadTexts:ciscoTsTrBRFTopologyChange.setStatus('')
ciscoTsTokenChannelFailed=NotificationType((1,3,6,1,4,1,9,5,32,7,0,1))
ciscoTsTokenChannelFailed.setObjects(*((_F,_H),(_F,_G),(_E,_Z)))
if mibBuilder.loadTexts:ciscoTsTokenChannelFailed.setStatus('')
ciscoTsTokenChannelStatus=NotificationType((1,3,6,1,4,1,9,5,32,7,0,2))
ciscoTsTokenChannelStatus.setObjects(*((_F,_H),(_F,_G),(_E,_AG),(_E,_Z),(_E,_AH)))
if mibBuilder.loadTexts:ciscoTsTokenChannelStatus.setStatus('')
mibBuilder.exportSymbols(_E,**{'MacAddr':MacAddr,'tsStack':tsStack,'ciscoTsMain':ciscoTsMain,'ciscoTsConfig':ciscoTsConfig,'ciscoTsStackCfgChange':ciscoTsStackCfgChange,'ciscoTsStackProStackMatrixChange':ciscoTsStackProStackMatrixChange,'ciscoTsIpAddr':ciscoTsIpAddr,'ciscoTsNetMask':ciscoTsNetMask,'ciscoTsDefaultGateway':ciscoTsDefaultGateway,'ciscoTsSysCurTime':ciscoTsSysCurTime,'ciscoTsConfiguration':ciscoTsConfiguration,_AA:ciscoTsNumSwitches,'ciscoTsStackStatus':ciscoTsStackStatus,'ciscoTsTftpServer':ciscoTsTftpServer,'ciscoTsTftpServerTrBRF':ciscoTsTftpServerTrBRF,'ciscoTsTftpFileLoc':ciscoTsTftpFileLoc,'ciscoTsTftpDownload':ciscoTsTftpDownload,'ciscoTsTftpDownloadStatus':ciscoTsTftpDownloadStatus,_AB:ciscoTsProStackMatrixStatus,'ciscoTsNumMatrixModules':ciscoTsNumMatrixModules,'ciscoTsStackReset':ciscoTsStackReset,'ciscoTsStackRMONStatistics':ciscoTsStackRMONStatistics,'ciscoTsTrapRcvrTable':ciscoTsTrapRcvrTable,'ciscoTsTrapRcvrEntry':ciscoTsTrapRcvrEntry,_h:ciscoTsTrapRcvrIndex,'ciscoTsTrapRcvrStatus':ciscoTsTrapRcvrStatus,'ciscoTsTrapRcvrIpAddress':ciscoTsTrapRcvrIpAddress,'ciscoTsTrapRcvrComm':ciscoTsTrapRcvrComm,'ciscoTsTrapRcvrTrBRFs':ciscoTsTrapRcvrTrBRFs,'ciscoTsStack':ciscoTsStack,'ciscoTsStackTempChange':ciscoTsStackTempChange,'ciscoTsStackPwrStatusChange':ciscoTsStackPwrStatusChange,'ciscoTsStackTable':ciscoTsStackTable,'ciscoTsStackEntry':ciscoTsStackEntry,_L:ciscoTsStackSwitchNumber,_i:ciscoTsStackSwitchBIAddr,'ciscoTsStackSwitchLAAddr':ciscoTsStackSwitchLAAddr,'ciscoTsStackSwitchFwVersion':ciscoTsStackSwitchFwVersion,'ciscoTsStackSwitchHwVersion':ciscoTsStackSwitchHwVersion,'ciscoTsStackSwitchUptime':ciscoTsStackSwitchUptime,'ciscoTsStackSwitchStatus':ciscoTsStackSwitchStatus,_AC:ciscoTsStackSwitchTemperature,'ciscoTsStackSwitchMemory':ciscoTsStackSwitchMemory,'ciscoTsStackSwitchSPANPort':ciscoTsStackSwitchSPANPort,'ciscoTsStackSwitchSPANMonitoredPort':ciscoTsStackSwitchSPANMonitoredPort,'ciscoTsStackSwitchFeatureStatus':ciscoTsStackSwitchFeatureStatus,'ciscoTsStackSwitchFeatureKey':ciscoTsStackSwitchFeatureKey,'ciscoTsStackSwitchPorts':ciscoTsStackSwitchPorts,'ciscoTsStackSwitchAgingTime':ciscoTsStackSwitchAgingTime,'ciscoTsStackSwitchAgingLevel':ciscoTsStackSwitchAgingLevel,'ciscoTsStackSwitchXmitFrames':ciscoTsStackSwitchXmitFrames,'ciscoTsStackSwitchRcvdFrames':ciscoTsStackSwitchRcvdFrames,'ciscoTsStackSwitchRcvdErrFrames':ciscoTsStackSwitchRcvdErrFrames,'ciscoTsStackSwitchLostFrames':ciscoTsStackSwitchLostFrames,'ciscoTsStackSwitchPendingSendRqsts':ciscoTsStackSwitchPendingSendRqsts,'ciscoTsStackSwitchXmitErrFrames':ciscoTsStackSwitchXmitErrFrames,'ciscoTsStackSwitchCurrActStations':ciscoTsStackSwitchCurrActStations,'ciscoTsStackSwitchLargestNumStations':ciscoTsStackSwitchLargestNumStations,'ciscoTsStackSwitchMaxAddressChain':ciscoTsStackSwitchMaxAddressChain,'ciscoTsStackSwitchAddressTblFulls':ciscoTsStackSwitchAddressTblFulls,'ciscoTsStackSwitchId':ciscoTsStackSwitchId,'ciscoTsStackSwitchSPANMonitoredTrCRFs':ciscoTsStackSwitchSPANMonitoredTrCRFs,_AD:ciscoTsStackSwitchPwrSupplyStatus,'ciscoTsModule':ciscoTsModule,'ciscoTsModTable':ciscoTsModTable,'ciscoTsModEntry':ciscoTsModEntry,_j:ciscoTsModSwitchNumber,_k:ciscoTsModNumber,'ciscoTsModState':ciscoTsModState,'ciscoTsModType':ciscoTsModType,'ciscoTsModRevision':ciscoTsModRevision,'ciscoTsModFwVer':ciscoTsModFwVer,'ciscoTsModNumPorts':ciscoTsModNumPorts,'ciscoTsModUptime':ciscoTsModUptime,'ciscoTsPort':ciscoTsPort,'ciscoTsPortStrNFwdEntry':ciscoTsPortStrNFwdEntry,'ciscoTsPortCfgLossTrap':ciscoTsPortCfgLossTrap,'ciscoTsBeaconStart':ciscoTsBeaconStart,'ciscoTsBeaconEnd':ciscoTsBeaconEnd,'ciscoTsDuplicateMACAddr':ciscoTsDuplicateMACAddr,'ciscoTsPortSoftErrExceededTrap':ciscoTsPortSoftErrExceededTrap,'ciscoTsPortCfgTable':ciscoTsPortCfgTable,'ciscoTsPortCfgEntry':ciscoTsPortCfgEntry,_N:ciscoTsPortCfgNumber,'ciscoTsPortCfgModNumber':ciscoTsPortCfgModNumber,'ciscoTsPortCfgIfIndex':ciscoTsPortCfgIfIndex,'ciscoTsPortCfgResetStats':ciscoTsPortCfgResetStats,'ciscoTsPortCfgResetAddrs':ciscoTsPortCfgResetAddrs,'ciscoTsPortCfgAddrAgingTime':ciscoTsPortCfgAddrAgingTime,'ciscoTsPortCfgDemandAgingLevel':ciscoTsPortCfgDemandAgingLevel,'ciscoTsPortCfgErrLoThreshold':ciscoTsPortCfgErrLoThreshold,'ciscoTsPortCfgErrHiThreshold':ciscoTsPortCfgErrHiThreshold,'ciscoTsPortCfgErrSampling':ciscoTsPortCfgErrSampling,'ciscoTsPortCfgMaxTransmitUnit':ciscoTsPortCfgMaxTransmitUnit,'ciscoTsPortCfgMaxExplorerRate':ciscoTsPortCfgMaxExplorerRate,'ciscoTsPortCfgSetACbits':ciscoTsPortCfgSetACbits,'ciscoTsPortCfgEarlyTokenRlse':ciscoTsPortCfgEarlyTokenRlse,'ciscoTsPortCfgForwardingMode':ciscoTsPortCfgForwardingMode,_AE:ciscoTsPortCfgActualForwardingMode,'ciscoTsPortCfgPortMode':ciscoTsPortCfgPortMode,'ciscoTsPortCfgActualPortMode':ciscoTsPortCfgActualPortMode,'ciscoTsPortCfgPriorityThres':ciscoTsPortCfgPriorityThres,'ciscoTsPortCfgMinXmitPriority':ciscoTsPortCfgMinXmitPriority,'ciscoTsPortCfgCfgLossThres':ciscoTsPortCfgCfgLossThres,'ciscoTsPortCfgCfgLossInterval':ciscoTsPortCfgCfgLossInterval,'ciscoTsPortCfgBcastSuppresion':ciscoTsPortCfgBcastSuppresion,'ciscoTsPortCfgCDPTimeToLive':ciscoTsPortCfgCDPTimeToLive,'ciscoTsPortCfgSpanningTreeMode':ciscoTsPortCfgSpanningTreeMode,'ciscoTsPortCfgSecurityMode':ciscoTsPortCfgSecurityMode,'ciscoTsPortCfgSoftErrThreshold':ciscoTsPortCfgSoftErrThreshold,'ciscoTsPortCfgSoftErrReportInterval':ciscoTsPortCfgSoftErrReportInterval,'ciscoTsPortCfgSoftErrorMonitoring':ciscoTsPortCfgSoftErrorMonitoring,'ciscoTsPortStatsTable':ciscoTsPortStatsTable,'ciscoTsPortStatsEntry':ciscoTsPortStatsEntry,_w:ciscoTsPortStatsNumber,'ciscoTsPortStatsModNumber':ciscoTsPortStatsModNumber,'ciscoTsPortStatsIfIndex':ciscoTsPortStatsIfIndex,'ciscoTsPortStatsRcvLocalFrames':ciscoTsPortStatsRcvLocalFrames,'ciscoTsPortStatsForwardedFrames':ciscoTsPortStatsForwardedFrames,'ciscoTsPortStatsStations':ciscoTsPortStatsStations,'ciscoTsPortStatsSWHandledFrames':ciscoTsPortStatsSWHandledFrames,'ciscoTsPortStatsLocalStations':ciscoTsPortStatsLocalStations,'ciscoTsPortStatsRemoteStations':ciscoTsPortStatsRemoteStations,'ciscoTsPortStatsUnknownStaFrames':ciscoTsPortStatsUnknownStaFrames,'ciscoTsPortStatsResetTimer':ciscoTsPortStatsResetTimer,'ciscoTsPortStatsInFrames':ciscoTsPortStatsInFrames,'ciscoTsPortStatsOutFrames':ciscoTsPortStatsOutFrames,'ciscoTsPortStatsLongFrames':ciscoTsPortStatsLongFrames,'ciscoTsPortStatsShortFrames':ciscoTsPortStatsShortFrames,'ciscoTsPortStatsInBufOverflows':ciscoTsPortStatsInBufOverflows,'ciscoTsPortStatsOutBufOverflows':ciscoTsPortStatsOutBufOverflows,'ciscoTsPortStatsRcvBcasts':ciscoTsPortStatsRcvBcasts,'ciscoTsPortStatsRcvMcasts':ciscoTsPortStatsRcvMcasts,'ciscoTsPortStatsSwitchedFrames':ciscoTsPortStatsSwitchedFrames,'ciscoTsPortStatsPktsInErrors':ciscoTsPortStatsPktsInErrors,'ciscoTsPortStatsAddrChainOverflows':ciscoTsPortStatsAddrChainOverflows,'ciscoTsPortStatsTableOverflows':ciscoTsPortStatsTableOverflows,_AF:ciscoTsPortStatsCfgLoss,'ciscoTsPortStatsCfgLossRC':ciscoTsPortStatsCfgLossRC,'ciscoTsPortStatsTrCRF':ciscoTsPortStatsTrCRF,'ciscoTsPortStatsAutoDisableRC':ciscoTsPortStatsAutoDisableRC,'ciscoTsProbe':ciscoTsProbe,'ciscoTsPassiveProbeTable':ciscoTsPassiveProbeTable,'ciscoTsPassiveProbeEntry':ciscoTsPassiveProbeEntry,_x:ciscoTsPassiveProbeIndex,'ciscoTsPassiveProbePort':ciscoTsPassiveProbePort,'ciscoTsPassiveProbeMonitoredPort':ciscoTsPassiveProbeMonitoredPort,'ciscoTsPassiveProbeDirection':ciscoTsPassiveProbeDirection,'ciscoTsVLANS':ciscoTsVLANS,'ciscoTsTrCRFNewRoot':ciscoTsTrCRFNewRoot,'ciscoTsTrCRFTopologyChange':ciscoTsTrCRFTopologyChange,'ciscoTsTrBRFNewRoot':ciscoTsTrBRFNewRoot,'ciscoTsTrBRFTopologyChange':ciscoTsTrBRFTopologyChange,'ciscoTsTrCRFInfoTable':ciscoTsTrCRFInfoTable,'ciscoTsTrCRFInfoEntry':ciscoTsTrCRFInfoEntry,_S:ciscoTsTrCRFInfoTrCRFNumber,'ciscoTsTrCRFInfoName':ciscoTsTrCRFInfoName,'ciscoTsTrCRFInfoSpanningTreeProtoSpecification':ciscoTsTrCRFInfoSpanningTreeProtoSpecification,'ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay':ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay,'ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime':ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime,'ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge':ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge,'ciscoTsTrCRFInfoSpanningTreeInternalPortMode':ciscoTsTrCRFInfoSpanningTreeInternalPortMode,'ciscoTsTrBRFInfoTable':ciscoTsTrBRFInfoTable,'ciscoTsTrBRFInfoEntry':ciscoTsTrBRFInfoEntry,_U:ciscoTsTrBRFInfoTrBRFNumber,'ciscoTsTrBRFInfoName':ciscoTsTrBRFInfoName,'ciscoTsTrBRFInfoIpState':ciscoTsTrBRFInfoIpState,'ciscoTsTrBRFInfoIpAddress':ciscoTsTrBRFInfoIpAddress,'ciscoTsTrBRFInfoIpSubnetMask':ciscoTsTrBRFInfoIpSubnetMask,'ciscoTsTrBRFInfoIpDefaultGateway':ciscoTsTrBRFInfoIpDefaultGateway,'ciscoTsTrBRFInfoStpMode':ciscoTsTrBRFInfoStpMode,'ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr':ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr,'ciscoTsTransitedConfiguredTrCRFs':ciscoTsTransitedConfiguredTrCRFs,'ciscoTsTransitedTrCRFs':ciscoTsTransitedTrCRFs,'ciscoTsTransitedConfiguredTrBRFs':ciscoTsTransitedConfiguredTrBRFs,'ciscoTsTransitedTrBRFs':ciscoTsTransitedTrBRFs,'ciscoTsTChannel':ciscoTsTChannel,'ciscoTsTokenChannelFailed':ciscoTsTokenChannelFailed,'ciscoTsTokenChannelStatus':ciscoTsTokenChannelStatus,'ciscoTsTCTable':ciscoTsTCTable,'ciscoTsTCEntry':ciscoTsTCEntry,_y:ciscoTsTCSwitchNumber,_z:ciscoTsTCNumber,_Z:ciscoTsTCPorts,_AG:ciscoTsTCStatus,_AH:ciscoTsTCActivePorts,'ciscoTsFilter':ciscoTsFilter,'ciscoTsProtocolClassFilterTable':ciscoTsProtocolClassFilterTable,'ciscoTsProtocolClassFilterEntry':ciscoTsProtocolClassFilterEntry,_V:ciscoTsProtocolClassFilterIndex,'ciscoTsProtocolClassFilterEtype':ciscoTsProtocolClassFilterEtype,'ciscoTsProtocolClassFilterDSAPs':ciscoTsProtocolClassFilterDSAPs,'ciscoTsProtocolFilterTable':ciscoTsProtocolFilterTable,'ciscoTsProtocolFilterEntry':ciscoTsProtocolFilterEntry,_A0:ciscoTsProtocolFilterPort,'ciscoTsProtocolFilterBlockingMode':ciscoTsProtocolFilterBlockingMode,'ciscoTsProtocolFilterTranspMode':ciscoTsProtocolFilterTranspMode,'ciscoTsMACDestFilterTable':ciscoTsMACDestFilterTable,'ciscoTsMACDestFilterEntry':ciscoTsMACDestFilterEntry,_A1:ciscoTsMACDestFilterSwitchNumber,_A2:ciscoTsMACDestFilterStationAddress,_A3:ciscoTsMACDestFilterType,'ciscoTsMACDestFilterPorts':ciscoTsMACDestFilterPorts,'ciscoTsMACDestFilterExitMask':ciscoTsMACDestFilterExitMask,'ciscoTsMACDestFilterRemoteBox':ciscoTsMACDestFilterRemoteBox,'ciscoTsMACDestFilterRemotePort':ciscoTsMACDestFilterRemotePort,'ciscoTsMACDestFilterStatus':ciscoTsMACDestFilterStatus,'ciscoTsMACSourceFilterTable':ciscoTsMACSourceFilterTable,'ciscoTsMACSourceFilterEntry':ciscoTsMACSourceFilterEntry,_A4:ciscoTsMACSourceFilterSwitchNumber,_A5:ciscoTsMACSourceFilterStationAddress,_A6:ciscoTsMACSourceFilterType,'ciscoTsMACSourceFilterPorts':ciscoTsMACSourceFilterPorts,'ciscoTsMACSourceFilterStatus':ciscoTsMACSourceFilterStatus,'ciscoTsDupAddrFilterTable':ciscoTsDupAddrFilterTable,'ciscoTsDupAddrFilterEntry':ciscoTsDupAddrFilterEntry,_A7:ciscoTsDupAddrFilterSwitchNumber,_A8:ciscoTsDupAddrFilterStationAddress,'ciscoTsDupAddrFilterPorts':ciscoTsDupAddrFilterPorts,'ciscoTsTrunkProtocolFilterTable':ciscoTsTrunkProtocolFilterTable,'ciscoTsTrunkProtocolFilterEntry':ciscoTsTrunkProtocolFilterEntry,_A9:ciscoTsTrunkProtocolFilterPort,'ciscoTsTrunkProtocolFilterBlockingMode':ciscoTsTrunkProtocolFilterBlockingMode,'ciscoTsTrunkProtocolFilterTranspMode':ciscoTsTrunkProtocolFilterTranspMode,'ciscoTsUplinkMIBs':ciscoTsUplinkMIBs})