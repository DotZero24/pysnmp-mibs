_O='mimosaChannel'
_N='mimosaStream'
_M='mimosaChain'
_L='not-accessible'
_K='auto'
_J='MIMOSA-NETWORKS-BFIVE-MIB'
_I='dB'
_H='MHz'
_G='dBm'
_F='disabled'
_E='enabled'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
mimosaConformanceGroup,mimosaWireless=mibBuilder.importSymbols('MIMOSA-NETWORKS-BASE-MIB','mimosaConformanceGroup','mimosaWireless')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mimosaB5Module=ModuleIdentity((1,3,6,1,4,1,43356,2,4,1))
if mibBuilder.loadTexts:mimosaB5Module.setRevisions(('2017-04-28 00:00',))
class DecimalOne(TextualConvention,Integer32):status=_A;displayHint='d-1'
class DecimalTwo(TextualConvention,Integer32):status=_A;displayHint='d-2'
class DecimalFive(TextualConvention,Integer32):status=_A;displayHint='d-5'
_MimosaGeneral_ObjectIdentity=ObjectIdentity
mimosaGeneral=_MimosaGeneral_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,1))
class _MimosaDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaDeviceName_Type.__name__=_D
_MimosaDeviceName_Object=MibScalar
mimosaDeviceName=_MimosaDeviceName_Object((1,3,6,1,4,1,43356,2,1,2,1,1),_MimosaDeviceName_Type())
mimosaDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaDeviceName.setStatus(_A)
class _MimosaSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaSerialNumber_Type.__name__=_D
_MimosaSerialNumber_Object=MibScalar
mimosaSerialNumber=_MimosaSerialNumber_Object((1,3,6,1,4,1,43356,2,1,2,1,2),_MimosaSerialNumber_Type())
mimosaSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaSerialNumber.setStatus(_A)
class _MimosaFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaFirmwareVersion_Type.__name__=_D
_MimosaFirmwareVersion_Object=MibScalar
mimosaFirmwareVersion=_MimosaFirmwareVersion_Object((1,3,6,1,4,1,43356,2,1,2,1,3),_MimosaFirmwareVersion_Type())
mimosaFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaFirmwareVersion.setStatus(_A)
class _MimosaFirmwareBuildDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaFirmwareBuildDate_Type.__name__=_D
_MimosaFirmwareBuildDate_Object=MibScalar
mimosaFirmwareBuildDate=_MimosaFirmwareBuildDate_Object((1,3,6,1,4,1,43356,2,1,2,1,4),_MimosaFirmwareBuildDate_Type())
mimosaFirmwareBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaFirmwareBuildDate.setStatus(_A)
class _MimosaLastRebootTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaLastRebootTime_Type.__name__=_D
_MimosaLastRebootTime_Object=MibScalar
mimosaLastRebootTime=_MimosaLastRebootTime_Object((1,3,6,1,4,1,43356,2,1,2,1,5),_MimosaLastRebootTime_Type())
mimosaLastRebootTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLastRebootTime.setStatus(_A)
class _MimosaUnlockCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaUnlockCode_Type.__name__=_D
_MimosaUnlockCode_Object=MibScalar
mimosaUnlockCode=_MimosaUnlockCode_Object((1,3,6,1,4,1,43356,2,1,2,1,6),_MimosaUnlockCode_Type())
mimosaUnlockCode.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaUnlockCode.setStatus(_A)
class _MimosaLEDBrightness_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('low',2),('medium',3),('high',4)))
_MimosaLEDBrightness_Type.__name__=_C
_MimosaLEDBrightness_Object=MibScalar
mimosaLEDBrightness=_MimosaLEDBrightness_Object((1,3,6,1,4,1,43356,2,1,2,1,7),_MimosaLEDBrightness_Type())
mimosaLEDBrightness.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLEDBrightness.setStatus(_A)
_MimosaInternalTemp_Type=DecimalOne
_MimosaInternalTemp_Object=MibScalar
mimosaInternalTemp=_MimosaInternalTemp_Object((1,3,6,1,4,1,43356,2,1,2,1,8),_MimosaInternalTemp_Type())
mimosaInternalTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaInternalTemp.setStatus(_A)
if mibBuilder.loadTexts:mimosaInternalTemp.setUnits('C')
class _MimosaRegulatoryDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaRegulatoryDomain_Type.__name__=_D
_MimosaRegulatoryDomain_Object=MibScalar
mimosaRegulatoryDomain=_MimosaRegulatoryDomain_Object((1,3,6,1,4,1,43356,2,1,2,1,9),_MimosaRegulatoryDomain_Type())
mimosaRegulatoryDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRegulatoryDomain.setStatus(_A)
_MimosaLocInfo_ObjectIdentity=ObjectIdentity
mimosaLocInfo=_MimosaLocInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,2))
_MimosaLongitude_Type=DecimalFive
_MimosaLongitude_Object=MibScalar
mimosaLongitude=_MimosaLongitude_Object((1,3,6,1,4,1,43356,2,1,2,2,1),_MimosaLongitude_Type())
mimosaLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLongitude.setStatus(_A)
_MimosaLatitude_Type=DecimalFive
_MimosaLatitude_Object=MibScalar
mimosaLatitude=_MimosaLatitude_Object((1,3,6,1,4,1,43356,2,1,2,2,2),_MimosaLatitude_Type())
mimosaLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLatitude.setStatus(_A)
_MimosaAltitude_Type=Integer32
_MimosaAltitude_Object=MibScalar
mimosaAltitude=_MimosaAltitude_Object((1,3,6,1,4,1,43356,2,1,2,2,3),_MimosaAltitude_Type())
mimosaAltitude.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaAltitude.setStatus(_A)
if mibBuilder.loadTexts:mimosaAltitude.setUnits('meters')
_MimosaSatelliteSNR_Type=DecimalOne
_MimosaSatelliteSNR_Object=MibScalar
mimosaSatelliteSNR=_MimosaSatelliteSNR_Object((1,3,6,1,4,1,43356,2,1,2,2,4),_MimosaSatelliteSNR_Type())
mimosaSatelliteSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaSatelliteSNR.setStatus(_A)
if mibBuilder.loadTexts:mimosaSatelliteSNR.setUnits(_I)
class _MimosaSatelliteStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_MimosaSatelliteStrength_Type.__name__=_C
_MimosaSatelliteStrength_Object=MibScalar
mimosaSatelliteStrength=_MimosaSatelliteStrength_Object((1,3,6,1,4,1,43356,2,1,2,2,5),_MimosaSatelliteStrength_Type())
mimosaSatelliteStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaSatelliteStrength.setStatus(_A)
_MimosaGPSSatellites_Type=Integer32
_MimosaGPSSatellites_Object=MibScalar
mimosaGPSSatellites=_MimosaGPSSatellites_Object((1,3,6,1,4,1,43356,2,1,2,2,6),_MimosaGPSSatellites_Type())
mimosaGPSSatellites.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaGPSSatellites.setStatus(_A)
_MimosaGlonassSatellites_Type=Integer32
_MimosaGlonassSatellites_Object=MibScalar
mimosaGlonassSatellites=_MimosaGlonassSatellites_Object((1,3,6,1,4,1,43356,2,1,2,2,7),_MimosaGlonassSatellites_Type())
mimosaGlonassSatellites.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaGlonassSatellites.setStatus(_A)
_MimosaClockAccuracy_Type=DecimalTwo
_MimosaClockAccuracy_Object=MibScalar
mimosaClockAccuracy=_MimosaClockAccuracy_Object((1,3,6,1,4,1,43356,2,1,2,2,8),_MimosaClockAccuracy_Type())
mimosaClockAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaClockAccuracy.setStatus(_A)
if mibBuilder.loadTexts:mimosaClockAccuracy.setUnits('PPB')
_MimosaWanInfo_ObjectIdentity=ObjectIdentity
mimosaWanInfo=_MimosaWanInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,3))
class _MimosaWanSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaWanSsid_Type.__name__=_D
_MimosaWanSsid_Object=MibScalar
mimosaWanSsid=_MimosaWanSsid_Object((1,3,6,1,4,1,43356,2,1,2,3,1),_MimosaWanSsid_Type())
mimosaWanSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaWanSsid.setStatus(_A)
_MimosaWanMac_Type=PhysAddress
_MimosaWanMac_Object=MibScalar
mimosaWanMac=_MimosaWanMac_Object((1,3,6,1,4,1,43356,2,1,2,3,2),_MimosaWanMac_Type())
mimosaWanMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaWanMac.setStatus(_A)
class _MimosaWanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnected',2)))
_MimosaWanStatus_Type.__name__=_C
_MimosaWanStatus_Object=MibScalar
mimosaWanStatus=_MimosaWanStatus_Object((1,3,6,1,4,1,43356,2,1,2,3,3),_MimosaWanStatus_Type())
mimosaWanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaWanStatus.setStatus(_A)
_MimosaWanUpTime_Type=TimeTicks
_MimosaWanUpTime_Object=MibScalar
mimosaWanUpTime=_MimosaWanUpTime_Object((1,3,6,1,4,1,43356,2,1,2,3,4),_MimosaWanUpTime_Type())
mimosaWanUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaWanUpTime.setStatus(_A)
_MimosaTdmaInfo_ObjectIdentity=ObjectIdentity
mimosaTdmaInfo=_MimosaTdmaInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,4))
class _MimosaWirelessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('accessPoint',1),('station',2)))
_MimosaWirelessMode_Type.__name__=_C
_MimosaWirelessMode_Object=MibScalar
mimosaWirelessMode=_MimosaWirelessMode_Object((1,3,6,1,4,1,43356,2,1,2,4,1),_MimosaWirelessMode_Type())
mimosaWirelessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaWirelessMode.setStatus(_A)
class _MimosaWirelessProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tdma',1),('csma',2)))
_MimosaWirelessProtocol_Type.__name__=_C
_MimosaWirelessProtocol_Object=MibScalar
mimosaWirelessProtocol=_MimosaWirelessProtocol_Object((1,3,6,1,4,1,43356,2,1,2,4,2),_MimosaWirelessProtocol_Type())
mimosaWirelessProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaWirelessProtocol.setStatus(_A)
class _MimosaTDMAMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('a',1),('b',2)))
_MimosaTDMAMode_Type.__name__=_C
_MimosaTDMAMode_Object=MibScalar
mimosaTDMAMode=_MimosaTDMAMode_Object((1,3,6,1,4,1,43356,2,1,2,4,3),_MimosaTDMAMode_Type())
mimosaTDMAMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTDMAMode.setStatus(_A)
_MimosaTDMAWindow_Type=Integer32
_MimosaTDMAWindow_Object=MibScalar
mimosaTDMAWindow=_MimosaTDMAWindow_Object((1,3,6,1,4,1,43356,2,1,2,4,4),_MimosaTDMAWindow_Type())
mimosaTDMAWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTDMAWindow.setStatus(_A)
if mibBuilder.loadTexts:mimosaTDMAWindow.setUnits('ms')
class _MimosaTrafficSplit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('symmetric',1),('asymmetric',2),(_K,3)))
_MimosaTrafficSplit_Type.__name__=_C
_MimosaTrafficSplit_Object=MibScalar
mimosaTrafficSplit=_MimosaTrafficSplit_Object((1,3,6,1,4,1,43356,2,1,2,4,5),_MimosaTrafficSplit_Type())
mimosaTrafficSplit.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTrafficSplit.setStatus(_A)
_MimosaMgmtInfo_ObjectIdentity=ObjectIdentity
mimosaMgmtInfo=_MimosaMgmtInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,5))
class _MimosaNetworkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_K,3)))
_MimosaNetworkMode_Type.__name__=_C
_MimosaNetworkMode_Object=MibScalar
mimosaNetworkMode=_MimosaNetworkMode_Object((1,3,6,1,4,1,43356,2,1,2,5,1),_MimosaNetworkMode_Type())
mimosaNetworkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaNetworkMode.setStatus(_A)
class _MimosaRecoverySsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MimosaRecoverySsid_Type.__name__=_D
_MimosaRecoverySsid_Object=MibScalar
mimosaRecoverySsid=_MimosaRecoverySsid_Object((1,3,6,1,4,1,43356,2,1,2,5,2),_MimosaRecoverySsid_Type())
mimosaRecoverySsid.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRecoverySsid.setStatus(_A)
class _MimosaLocalSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MimosaLocalSsid_Type.__name__=_D
_MimosaLocalSsid_Object=MibScalar
mimosaLocalSsid=_MimosaLocalSsid_Object((1,3,6,1,4,1,43356,2,1,2,5,3),_MimosaLocalSsid_Type())
mimosaLocalSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLocalSsid.setStatus(_A)
_MimosaLocalChannel_Type=Integer32
_MimosaLocalChannel_Object=MibScalar
mimosaLocalChannel=_MimosaLocalChannel_Object((1,3,6,1,4,1,43356,2,1,2,5,4),_MimosaLocalChannel_Type())
mimosaLocalChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLocalChannel.setStatus(_A)
_MimosaConsoleTimeout_Type=Integer32
_MimosaConsoleTimeout_Object=MibScalar
mimosaConsoleTimeout=_MimosaConsoleTimeout_Object((1,3,6,1,4,1,43356,2,1,2,5,5),_MimosaConsoleTimeout_Type())
mimosaConsoleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaConsoleTimeout.setStatus(_A)
if mibBuilder.loadTexts:mimosaConsoleTimeout.setUnits('min')
_MimosaMaxClients_Type=Integer32
_MimosaMaxClients_Object=MibScalar
mimosaMaxClients=_MimosaMaxClients_Object((1,3,6,1,4,1,43356,2,1,2,5,6),_MimosaMaxClients_Type())
mimosaMaxClients.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaMaxClients.setStatus(_A)
_MimosaLocalMac_Type=PhysAddress
_MimosaLocalMac_Object=MibScalar
mimosaLocalMac=_MimosaLocalMac_Object((1,3,6,1,4,1,43356,2,1,2,5,7),_MimosaLocalMac_Type())
mimosaLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLocalMac.setStatus(_A)
_MimosaLocalIpAddr_Type=IpAddress
_MimosaLocalIpAddr_Object=MibScalar
mimosaLocalIpAddr=_MimosaLocalIpAddr_Object((1,3,6,1,4,1,43356,2,1,2,5,8),_MimosaLocalIpAddr_Type())
mimosaLocalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLocalIpAddr.setStatus(_A)
_MimosaLocalNetMask_Type=IpAddress
_MimosaLocalNetMask_Object=MibScalar
mimosaLocalNetMask=_MimosaLocalNetMask_Object((1,3,6,1,4,1,43356,2,1,2,5,9),_MimosaLocalNetMask_Type())
mimosaLocalNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLocalNetMask.setStatus(_A)
_MimosaLocalGateway_Type=IpAddress
_MimosaLocalGateway_Object=MibScalar
mimosaLocalGateway=_MimosaLocalGateway_Object((1,3,6,1,4,1,43356,2,1,2,5,10),_MimosaLocalGateway_Type())
mimosaLocalGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaLocalGateway.setStatus(_A)
class _MimosaFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MimosaFlowControl_Type.__name__=_C
_MimosaFlowControl_Object=MibScalar
mimosaFlowControl=_MimosaFlowControl_Object((1,3,6,1,4,1,43356,2,1,2,5,11),_MimosaFlowControl_Type())
mimosaFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaFlowControl.setStatus(_A)
_MimosaRfInfo_ObjectIdentity=ObjectIdentity
mimosaRfInfo=_MimosaRfInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,6))
_MimosaChainTable_Object=MibTable
mimosaChainTable=_MimosaChainTable_Object((1,3,6,1,4,1,43356,2,1,2,6,1))
if mibBuilder.loadTexts:mimosaChainTable.setStatus(_A)
_MimosaChainEntry_Object=MibTableRow
mimosaChainEntry=_MimosaChainEntry_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1))
mimosaChainEntry.setIndexNames((0,_J,_M))
if mibBuilder.loadTexts:mimosaChainEntry.setStatus(_A)
class _MimosaChain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MimosaChain_Type.__name__=_C
_MimosaChain_Object=MibTableColumn
mimosaChain=_MimosaChain_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1,1),_MimosaChain_Type())
mimosaChain.setMaxAccess(_L)
if mibBuilder.loadTexts:mimosaChain.setStatus(_A)
_MimosaTxPower_Type=DecimalOne
_MimosaTxPower_Object=MibTableColumn
mimosaTxPower=_MimosaTxPower_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1,2),_MimosaTxPower_Type())
mimosaTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTxPower.setStatus(_A)
if mibBuilder.loadTexts:mimosaTxPower.setUnits(_G)
_MimosaRxPower_Type=DecimalOne
_MimosaRxPower_Object=MibTableColumn
mimosaRxPower=_MimosaRxPower_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1,3),_MimosaRxPower_Type())
mimosaRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRxPower.setStatus(_A)
if mibBuilder.loadTexts:mimosaRxPower.setUnits(_G)
_MimosaRxNoise_Type=DecimalOne
_MimosaRxNoise_Object=MibTableColumn
mimosaRxNoise=_MimosaRxNoise_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1,4),_MimosaRxNoise_Type())
mimosaRxNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRxNoise.setStatus(_A)
if mibBuilder.loadTexts:mimosaRxNoise.setUnits(_G)
_MimosaSNR_Type=DecimalOne
_MimosaSNR_Object=MibTableColumn
mimosaSNR=_MimosaSNR_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1,5),_MimosaSNR_Type())
mimosaSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaSNR.setStatus(_A)
if mibBuilder.loadTexts:mimosaSNR.setUnits(_I)
_MimosaCenterFreq_Type=Integer32
_MimosaCenterFreq_Object=MibTableColumn
mimosaCenterFreq=_MimosaCenterFreq_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1,6),_MimosaCenterFreq_Type())
mimosaCenterFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaCenterFreq.setStatus(_A)
if mibBuilder.loadTexts:mimosaCenterFreq.setUnits(_H)
class _MimosaPolarization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('horizontal',1),('vertical',2)))
_MimosaPolarization_Type.__name__=_C
_MimosaPolarization_Object=MibTableColumn
mimosaPolarization=_MimosaPolarization_Object((1,3,6,1,4,1,43356,2,1,2,6,1,1,7),_MimosaPolarization_Type())
mimosaPolarization.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaPolarization.setStatus(_A)
_MimosaStreamTable_Object=MibTable
mimosaStreamTable=_MimosaStreamTable_Object((1,3,6,1,4,1,43356,2,1,2,6,2))
if mibBuilder.loadTexts:mimosaStreamTable.setStatus(_A)
_MimosaStreamEntry_Object=MibTableRow
mimosaStreamEntry=_MimosaStreamEntry_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1))
mimosaStreamEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:mimosaStreamEntry.setStatus(_A)
class _MimosaStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MimosaStream_Type.__name__=_C
_MimosaStream_Object=MibTableColumn
mimosaStream=_MimosaStream_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,1),_MimosaStream_Type())
mimosaStream.setMaxAccess(_L)
if mibBuilder.loadTexts:mimosaStream.setStatus(_A)
_MimosaTxPhy_Type=Integer32
_MimosaTxPhy_Object=MibTableColumn
mimosaTxPhy=_MimosaTxPhy_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,2),_MimosaTxPhy_Type())
mimosaTxPhy.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTxPhy.setStatus(_A)
if mibBuilder.loadTexts:mimosaTxPhy.setUnits('Mbps')
_MimosaTxMCS_Type=Integer32
_MimosaTxMCS_Object=MibTableColumn
mimosaTxMCS=_MimosaTxMCS_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,3),_MimosaTxMCS_Type())
mimosaTxMCS.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTxMCS.setStatus(_A)
_MimosaTxWidth_Type=Integer32
_MimosaTxWidth_Object=MibTableColumn
mimosaTxWidth=_MimosaTxWidth_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,4),_MimosaTxWidth_Type())
mimosaTxWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTxWidth.setStatus(_A)
if mibBuilder.loadTexts:mimosaTxWidth.setUnits(_H)
_MimosaRxPhy_Type=Integer32
_MimosaRxPhy_Object=MibTableColumn
mimosaRxPhy=_MimosaRxPhy_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,5),_MimosaRxPhy_Type())
mimosaRxPhy.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRxPhy.setStatus(_A)
if mibBuilder.loadTexts:mimosaRxPhy.setUnits('Mbps')
_MimosaRxMCS_Type=Integer32
_MimosaRxMCS_Object=MibTableColumn
mimosaRxMCS=_MimosaRxMCS_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,6),_MimosaRxMCS_Type())
mimosaRxMCS.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRxMCS.setStatus(_A)
_MimosaRxWidth_Type=Integer32
_MimosaRxWidth_Object=MibTableColumn
mimosaRxWidth=_MimosaRxWidth_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,7),_MimosaRxWidth_Type())
mimosaRxWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRxWidth.setStatus(_A)
if mibBuilder.loadTexts:mimosaRxWidth.setUnits(_H)
_MimosaRxEVM_Type=DecimalOne
_MimosaRxEVM_Object=MibTableColumn
mimosaRxEVM=_MimosaRxEVM_Object((1,3,6,1,4,1,43356,2,1,2,6,2,1,8),_MimosaRxEVM_Type())
mimosaRxEVM.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRxEVM.setStatus(_A)
if mibBuilder.loadTexts:mimosaRxEVM.setUnits(_I)
_MimosaChannelTable_Object=MibTable
mimosaChannelTable=_MimosaChannelTable_Object((1,3,6,1,4,1,43356,2,1,2,6,3))
if mibBuilder.loadTexts:mimosaChannelTable.setStatus(_A)
_MimosaChannelEntry_Object=MibTableRow
mimosaChannelEntry=_MimosaChannelEntry_Object((1,3,6,1,4,1,43356,2,1,2,6,3,1))
mimosaChannelEntry.setIndexNames((0,_J,_O))
if mibBuilder.loadTexts:mimosaChannelEntry.setStatus(_A)
class _MimosaChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MimosaChannel_Type.__name__=_C
_MimosaChannel_Object=MibTableColumn
mimosaChannel=_MimosaChannel_Object((1,3,6,1,4,1,43356,2,1,2,6,3,1,1),_MimosaChannel_Type())
mimosaChannel.setMaxAccess(_L)
if mibBuilder.loadTexts:mimosaChannel.setStatus(_A)
class _MimosaChannelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transmit',1),('receive',2),('bidirectional',3)))
_MimosaChannelMode_Type.__name__=_C
_MimosaChannelMode_Object=MibTableColumn
mimosaChannelMode=_MimosaChannelMode_Object((1,3,6,1,4,1,43356,2,1,2,6,3,1,2),_MimosaChannelMode_Type())
mimosaChannelMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaChannelMode.setStatus(_A)
_MimosaChannelWidth_Type=Integer32
_MimosaChannelWidth_Object=MibTableColumn
mimosaChannelWidth=_MimosaChannelWidth_Object((1,3,6,1,4,1,43356,2,1,2,6,3,1,3),_MimosaChannelWidth_Type())
mimosaChannelWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaChannelWidth.setStatus(_A)
if mibBuilder.loadTexts:mimosaChannelWidth.setUnits(_H)
_MimosaChannelTxPower_Type=Integer32
_MimosaChannelTxPower_Object=MibTableColumn
mimosaChannelTxPower=_MimosaChannelTxPower_Object((1,3,6,1,4,1,43356,2,1,2,6,3,1,4),_MimosaChannelTxPower_Type())
mimosaChannelTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaChannelTxPower.setStatus(_A)
if mibBuilder.loadTexts:mimosaChannelTxPower.setUnits(_G)
_MimosaChannelCenterFreq_Type=Integer32
_MimosaChannelCenterFreq_Object=MibTableColumn
mimosaChannelCenterFreq=_MimosaChannelCenterFreq_Object((1,3,6,1,4,1,43356,2,1,2,6,3,1,5),_MimosaChannelCenterFreq_Type())
mimosaChannelCenterFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaChannelCenterFreq.setStatus(_A)
if mibBuilder.loadTexts:mimosaChannelCenterFreq.setUnits(_H)
_MimosaAntennaGain_Type=Integer32
_MimosaAntennaGain_Object=MibScalar
mimosaAntennaGain=_MimosaAntennaGain_Object((1,3,6,1,4,1,43356,2,1,2,6,4),_MimosaAntennaGain_Type())
mimosaAntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaAntennaGain.setStatus(_A)
if mibBuilder.loadTexts:mimosaAntennaGain.setUnits('dBi')
_MimosaTotalTxPower_Type=DecimalOne
_MimosaTotalTxPower_Object=MibScalar
mimosaTotalTxPower=_MimosaTotalTxPower_Object((1,3,6,1,4,1,43356,2,1,2,6,5),_MimosaTotalTxPower_Type())
mimosaTotalTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTotalTxPower.setStatus(_A)
if mibBuilder.loadTexts:mimosaTotalTxPower.setUnits(_G)
_MimosaTotalRxPower_Type=DecimalOne
_MimosaTotalRxPower_Object=MibScalar
mimosaTotalRxPower=_MimosaTotalRxPower_Object((1,3,6,1,4,1,43356,2,1,2,6,6),_MimosaTotalRxPower_Type())
mimosaTotalRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTotalRxPower.setStatus(_A)
if mibBuilder.loadTexts:mimosaTotalRxPower.setUnits(_G)
_MimosaTargetSignalStrength_Type=Integer32
_MimosaTargetSignalStrength_Object=MibScalar
mimosaTargetSignalStrength=_MimosaTargetSignalStrength_Object((1,3,6,1,4,1,43356,2,1,2,6,7),_MimosaTargetSignalStrength_Type())
mimosaTargetSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaTargetSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:mimosaTargetSignalStrength.setUnits(_I)
_MimosaPerfInfo_ObjectIdentity=ObjectIdentity
mimosaPerfInfo=_MimosaPerfInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,7))
_MimosaPhyTxRate_Type=DecimalTwo
_MimosaPhyTxRate_Object=MibScalar
mimosaPhyTxRate=_MimosaPhyTxRate_Object((1,3,6,1,4,1,43356,2,1,2,7,1),_MimosaPhyTxRate_Type())
mimosaPhyTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaPhyTxRate.setStatus(_A)
if mibBuilder.loadTexts:mimosaPhyTxRate.setUnits('kbps')
_MimosaPhyRxRate_Type=DecimalTwo
_MimosaPhyRxRate_Object=MibScalar
mimosaPhyRxRate=_MimosaPhyRxRate_Object((1,3,6,1,4,1,43356,2,1,2,7,2),_MimosaPhyRxRate_Type())
mimosaPhyRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaPhyRxRate.setStatus(_A)
if mibBuilder.loadTexts:mimosaPhyRxRate.setUnits('kbps')
_MimosaPerTxRate_Type=DecimalTwo
_MimosaPerTxRate_Object=MibScalar
mimosaPerTxRate=_MimosaPerTxRate_Object((1,3,6,1,4,1,43356,2,1,2,7,3),_MimosaPerTxRate_Type())
mimosaPerTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaPerTxRate.setStatus(_A)
if mibBuilder.loadTexts:mimosaPerTxRate.setUnits('%')
_MimosaPerRxRate_Type=DecimalTwo
_MimosaPerRxRate_Object=MibScalar
mimosaPerRxRate=_MimosaPerRxRate_Object((1,3,6,1,4,1,43356,2,1,2,7,4),_MimosaPerRxRate_Type())
mimosaPerRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaPerRxRate.setStatus(_A)
_MimosaServices_ObjectIdentity=ObjectIdentity
mimosaServices=_MimosaServices_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,8))
class _MimosaHttpsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MimosaHttpsEnabled_Type.__name__=_C
_MimosaHttpsEnabled_Object=MibScalar
mimosaHttpsEnabled=_MimosaHttpsEnabled_Object((1,3,6,1,4,1,43356,2,1,2,8,1),_MimosaHttpsEnabled_Type())
mimosaHttpsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaHttpsEnabled.setStatus(_A)
class _MimosaMgmtVlanEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MimosaMgmtVlanEnabled_Type.__name__=_C
_MimosaMgmtVlanEnabled_Object=MibScalar
mimosaMgmtVlanEnabled=_MimosaMgmtVlanEnabled_Object((1,3,6,1,4,1,43356,2,1,2,8,2),_MimosaMgmtVlanEnabled_Type())
mimosaMgmtVlanEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaMgmtVlanEnabled.setStatus(_A)
class _MimosaMgmtCloudEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MimosaMgmtCloudEnabled_Type.__name__=_C
_MimosaMgmtCloudEnabled_Object=MibScalar
mimosaMgmtCloudEnabled=_MimosaMgmtCloudEnabled_Object((1,3,6,1,4,1,43356,2,1,2,8,3),_MimosaMgmtCloudEnabled_Type())
mimosaMgmtCloudEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaMgmtCloudEnabled.setStatus(_A)
class _MimosaRestMgmtEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MimosaRestMgmtEnabled_Type.__name__=_C
_MimosaRestMgmtEnabled_Object=MibScalar
mimosaRestMgmtEnabled=_MimosaRestMgmtEnabled_Object((1,3,6,1,4,1,43356,2,1,2,8,4),_MimosaRestMgmtEnabled_Type())
mimosaRestMgmtEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaRestMgmtEnabled.setStatus(_A)
class _MimosaPingWatchdogEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MimosaPingWatchdogEnabled_Type.__name__=_C
_MimosaPingWatchdogEnabled_Object=MibScalar
mimosaPingWatchdogEnabled=_MimosaPingWatchdogEnabled_Object((1,3,6,1,4,1,43356,2,1,2,8,5),_MimosaPingWatchdogEnabled_Type())
mimosaPingWatchdogEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaPingWatchdogEnabled.setStatus(_A)
class _MimosaSyslogEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MimosaSyslogEnabled_Type.__name__=_C
_MimosaSyslogEnabled_Object=MibScalar
mimosaSyslogEnabled=_MimosaSyslogEnabled_Object((1,3,6,1,4,1,43356,2,1,2,8,6),_MimosaSyslogEnabled_Type())
mimosaSyslogEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaSyslogEnabled.setStatus(_A)
class _MimosaNtpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('custom',1),('standard',2)))
_MimosaNtpMode_Type.__name__=_C
_MimosaNtpMode_Object=MibScalar
mimosaNtpMode=_MimosaNtpMode_Object((1,3,6,1,4,1,43356,2,1,2,8,7),_MimosaNtpMode_Type())
mimosaNtpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaNtpMode.setStatus(_A)
class _MimosaNtpServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaNtpServer_Type.__name__=_D
_MimosaNtpServer_Object=MibScalar
mimosaNtpServer=_MimosaNtpServer_Object((1,3,6,1,4,1,43356,2,1,2,8,8),_MimosaNtpServer_Type())
mimosaNtpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mimosaNtpServer.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'DecimalOne':DecimalOne,'DecimalTwo':DecimalTwo,'DecimalFive':DecimalFive,'mimosaGeneral':mimosaGeneral,'mimosaDeviceName':mimosaDeviceName,'mimosaSerialNumber':mimosaSerialNumber,'mimosaFirmwareVersion':mimosaFirmwareVersion,'mimosaFirmwareBuildDate':mimosaFirmwareBuildDate,'mimosaLastRebootTime':mimosaLastRebootTime,'mimosaUnlockCode':mimosaUnlockCode,'mimosaLEDBrightness':mimosaLEDBrightness,'mimosaInternalTemp':mimosaInternalTemp,'mimosaRegulatoryDomain':mimosaRegulatoryDomain,'mimosaLocInfo':mimosaLocInfo,'mimosaLongitude':mimosaLongitude,'mimosaLatitude':mimosaLatitude,'mimosaAltitude':mimosaAltitude,'mimosaSatelliteSNR':mimosaSatelliteSNR,'mimosaSatelliteStrength':mimosaSatelliteStrength,'mimosaGPSSatellites':mimosaGPSSatellites,'mimosaGlonassSatellites':mimosaGlonassSatellites,'mimosaClockAccuracy':mimosaClockAccuracy,'mimosaWanInfo':mimosaWanInfo,'mimosaWanSsid':mimosaWanSsid,'mimosaWanMac':mimosaWanMac,'mimosaWanStatus':mimosaWanStatus,'mimosaWanUpTime':mimosaWanUpTime,'mimosaTdmaInfo':mimosaTdmaInfo,'mimosaWirelessMode':mimosaWirelessMode,'mimosaWirelessProtocol':mimosaWirelessProtocol,'mimosaTDMAMode':mimosaTDMAMode,'mimosaTDMAWindow':mimosaTDMAWindow,'mimosaTrafficSplit':mimosaTrafficSplit,'mimosaMgmtInfo':mimosaMgmtInfo,'mimosaNetworkMode':mimosaNetworkMode,'mimosaRecoverySsid':mimosaRecoverySsid,'mimosaLocalSsid':mimosaLocalSsid,'mimosaLocalChannel':mimosaLocalChannel,'mimosaConsoleTimeout':mimosaConsoleTimeout,'mimosaMaxClients':mimosaMaxClients,'mimosaLocalMac':mimosaLocalMac,'mimosaLocalIpAddr':mimosaLocalIpAddr,'mimosaLocalNetMask':mimosaLocalNetMask,'mimosaLocalGateway':mimosaLocalGateway,'mimosaFlowControl':mimosaFlowControl,'mimosaRfInfo':mimosaRfInfo,'mimosaChainTable':mimosaChainTable,'mimosaChainEntry':mimosaChainEntry,_M:mimosaChain,'mimosaTxPower':mimosaTxPower,'mimosaRxPower':mimosaRxPower,'mimosaRxNoise':mimosaRxNoise,'mimosaSNR':mimosaSNR,'mimosaCenterFreq':mimosaCenterFreq,'mimosaPolarization':mimosaPolarization,'mimosaStreamTable':mimosaStreamTable,'mimosaStreamEntry':mimosaStreamEntry,_N:mimosaStream,'mimosaTxPhy':mimosaTxPhy,'mimosaTxMCS':mimosaTxMCS,'mimosaTxWidth':mimosaTxWidth,'mimosaRxPhy':mimosaRxPhy,'mimosaRxMCS':mimosaRxMCS,'mimosaRxWidth':mimosaRxWidth,'mimosaRxEVM':mimosaRxEVM,'mimosaChannelTable':mimosaChannelTable,'mimosaChannelEntry':mimosaChannelEntry,_O:mimosaChannel,'mimosaChannelMode':mimosaChannelMode,'mimosaChannelWidth':mimosaChannelWidth,'mimosaChannelTxPower':mimosaChannelTxPower,'mimosaChannelCenterFreq':mimosaChannelCenterFreq,'mimosaAntennaGain':mimosaAntennaGain,'mimosaTotalTxPower':mimosaTotalTxPower,'mimosaTotalRxPower':mimosaTotalRxPower,'mimosaTargetSignalStrength':mimosaTargetSignalStrength,'mimosaPerfInfo':mimosaPerfInfo,'mimosaPhyTxRate':mimosaPhyTxRate,'mimosaPhyRxRate':mimosaPhyRxRate,'mimosaPerTxRate':mimosaPerTxRate,'mimosaPerRxRate':mimosaPerRxRate,'mimosaServices':mimosaServices,'mimosaHttpsEnabled':mimosaHttpsEnabled,'mimosaMgmtVlanEnabled':mimosaMgmtVlanEnabled,'mimosaMgmtCloudEnabled':mimosaMgmtCloudEnabled,'mimosaRestMgmtEnabled':mimosaRestMgmtEnabled,'mimosaPingWatchdogEnabled':mimosaPingWatchdogEnabled,'mimosaSyslogEnabled':mimosaSyslogEnabled,'mimosaNtpMode':mimosaNtpMode,'mimosaNtpServer':mimosaNtpServer,'mimosaB5Module':mimosaB5Module})