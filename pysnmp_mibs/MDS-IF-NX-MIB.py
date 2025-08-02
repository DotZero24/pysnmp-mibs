_AS='mIfNxStatusActChanGroup'
_AR='mIfNxStatusEndpointGroup'
_AQ='mIfNxStatusConnRemGroup'
_AP='mIfNxStatusGroup'
_AO='mIfNxStatusActChanAvgLqi'
_AN='mIfNxStatusActChanAvgRssi'
_AM='mIfNxStatusActChanFrequency'
_AL='mIfNxStatusEndpointStatsRxDrop'
_AK='mIfNxStatusEndpointStatsTxDrop'
_AJ='mIfNxStatusEndpointStatsRxError'
_AI='mIfNxStatusEndpointStatsTxError'
_AH='mIfNxStatusEndpointStatsRxBytes'
_AG='mIfNxStatusEndpointStatsRxPackets'
_AF='mIfNxStatusEndpointStatsTxBytes'
_AE='mIfNxStatusEndpointStatsTxPackets'
_AD='mIfNxStatusEndpointRemAddress'
_AC='mIfNxStatusEndpointTimeToLive'
_AB='mIfNxStatusEndpointIpAddress'
_AA='mIfNxStatusConnRemStatsDwnSnr'
_A9='mIfNxStatusConnRemStatsDwnLqi'
_A8='mIfNxStatusConnRemStatsDwnRssi'
_A7='mIfNxStatusConnRemStatsTemp'
_A6='mIfNxStatusConnRemStatsVersion'
_A5='mIfNxStatusConnRemStatsAlarmed'
_A4='mIfNxStatusConnRemStatsName'
_A3='mIfNxStatusConnRemStatsAllIp'
_A2='mIfNxStatusConnRemStatsGateway'
_A1='mIfNxStatusConnRemAvgSnr'
_A0='mIfNxStatusConnRemStatsRxDrop'
_z='mIfNxStatusConnRemStatsTxDrop'
_y='mIfNxStatusConnRemStatsRxError'
_x='mIfNxStatusConnRemStatsTxError'
_w='mIfNxStatusConnRemStatsRxBytes'
_v='mIfNxStatusConnRemStatsRxPackets'
_u='mIfNxStatusConnRemStatsTxBytes'
_t='mIfNxStatusConnRemStatsTxPackets'
_s='mIfNxStatusConnRemAvgLqi'
_r='mIfNxStatusConnRemAvgRssi'
_q='mIfNxStatusConnRemNicId'
_p='mIfNxStatusConnRemLinkStatus'
_o='mIfNxStatusConnRemTimeToLive'
_n='mIfNxStatusConnRemIpAddress'
_m='mIfNxActiveNic'
_l='mIfNxLastChan'
_k='mIfNxLastLqi'
_j='mIfNxLastRssi'
_i='mIfNxCurrentDeviceMode'
_h='mIfNxMacStatsSyncChange'
_g='mIfNxMacStatsSyncCheckError'
_f='mIfNxMacStatsRxSuccess'
_e='mIfNxMacStatsTxRetry'
_d='mIfNxMacStatsTxError'
_c='mIfNxMacStatsTxNoAssoc'
_b='mIfNxMacStatsTxNoSync'
_a='mIfNxMacStatsTxQueueFull'
_Z='mIfNxMacStatsTxFail'
_Y='mIfNxMacStatsTxSuccess'
_X='mIfNxApInfoAvgLqi'
_W='mIfNxApInfoAvgRssi'
_V='mIfNxApInfoConnectedTime'
_U='mIfNxApInfoIpAddress'
_T='mIfNxApInfoApAddress'
_S='mIfNxTemperature'
_R='mIfNxHardwareRevision'
_Q='mIfNxHardwareId'
_P='mIfNxFirmwareRevision'
_O='mIfNxSerialNumber'
_N='mIfNxAlarms'
_M='mIfNxCurrentModem'
_L='mIfNxInitStatus'
_K='mIfNxLinkStatus'
_J='initializing'
_I='Integer32'
_H='mIfNxStatusActChanChannel'
_G='mIfNxStatusEndpointAddress'
_F='mIfNxStatusConnRemAddress'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='MDS-IF-NX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
mdsInterfaces,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsInterfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
mdsIfNxMIB=ModuleIdentity((1,3,6,1,4,1,4130,10,2,3))
if mibBuilder.loadTexts:mdsIfNxMIB.setRevisions(('2018-05-16 00:00','2016-09-21 00:00','2015-08-21 00:00','2015-06-12 00:00','2015-03-27 00:00','2014-10-20 00:00','2014-05-13 00:00'))
class UnsignedByte(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class UnsignedShort(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class LinkStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),('scanning',1),('negotiating',2),('authenticating',3),('associated',4),('disassociated',5)))
class InitStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('off',0),(_J,1),('discovering',2),('reprogramming',3),('configuring',4),('complete',5),('error',6)))
class DeviceModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('remote',0),('accessPoint',1),('storeAndForward',2),('test',3)))
class ModemType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,10)));namedValues=NamedValues(*(('e125kbps',0),('e250kbps',1),('e500kbps',2),('e1000kbps',3),('e1000Wkbps',4),('e1250kbps',5),('auto',10)))
class AlarmFlags(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('temperature',0),('vswrFault',16),('notCalibrated',23)))
class FirmwareRevision(TextualConvention,OctetString):status=_A;displayHint='32a'
class InetIpAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_MIfNxMIBObjects_ObjectIdentity=ObjectIdentity
mIfNxMIBObjects=_MIfNxMIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,2,3,1))
_MIfNxConfig_ObjectIdentity=ObjectIdentity
mIfNxConfig=_MIfNxConfig_ObjectIdentity((1,3,6,1,4,1,4130,10,2,3,1,1))
_MIfNxStatus_ObjectIdentity=ObjectIdentity
mIfNxStatus=_MIfNxStatus_ObjectIdentity((1,3,6,1,4,1,4130,10,2,3,1,2))
_MIfNxStatusTable_Object=MibTable
mIfNxStatusTable=_MIfNxStatusTable_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1))
if mibBuilder.loadTexts:mIfNxStatusTable.setStatus(_A)
_MIfNxStatusEntry_Object=MibTableRow
mIfNxStatusEntry=_MIfNxStatusEntry_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1))
mIfNxStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mIfNxStatusEntry.setStatus(_A)
_MIfNxLinkStatus_Type=LinkStatus
_MIfNxLinkStatus_Object=MibTableColumn
mIfNxLinkStatus=_MIfNxLinkStatus_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,1),_MIfNxLinkStatus_Type())
mIfNxLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxLinkStatus.setStatus(_A)
_MIfNxInitStatus_Type=InitStatus
_MIfNxInitStatus_Object=MibTableColumn
mIfNxInitStatus=_MIfNxInitStatus_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,2),_MIfNxInitStatus_Type())
mIfNxInitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxInitStatus.setStatus(_A)
_MIfNxCurrentModem_Type=ModemType
_MIfNxCurrentModem_Object=MibTableColumn
mIfNxCurrentModem=_MIfNxCurrentModem_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,3),_MIfNxCurrentModem_Type())
mIfNxCurrentModem.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxCurrentModem.setStatus(_A)
_MIfNxAlarms_Type=AlarmFlags
_MIfNxAlarms_Object=MibTableColumn
mIfNxAlarms=_MIfNxAlarms_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,4),_MIfNxAlarms_Type())
mIfNxAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxAlarms.setStatus(_A)
_MIfNxSerialNumber_Type=Unsigned32
_MIfNxSerialNumber_Object=MibTableColumn
mIfNxSerialNumber=_MIfNxSerialNumber_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,5),_MIfNxSerialNumber_Type())
mIfNxSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxSerialNumber.setStatus(_A)
_MIfNxFirmwareRevision_Type=FirmwareRevision
_MIfNxFirmwareRevision_Object=MibTableColumn
mIfNxFirmwareRevision=_MIfNxFirmwareRevision_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,6),_MIfNxFirmwareRevision_Type())
mIfNxFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxFirmwareRevision.setStatus(_A)
_MIfNxHardwareId_Type=UnsignedByte
_MIfNxHardwareId_Object=MibTableColumn
mIfNxHardwareId=_MIfNxHardwareId_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,7),_MIfNxHardwareId_Type())
mIfNxHardwareId.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxHardwareId.setStatus(_A)
_MIfNxHardwareRevision_Type=UnsignedByte
_MIfNxHardwareRevision_Object=MibTableColumn
mIfNxHardwareRevision=_MIfNxHardwareRevision_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,8),_MIfNxHardwareRevision_Type())
mIfNxHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxHardwareRevision.setStatus(_A)
_MIfNxTemperature_Type=Integer32
_MIfNxTemperature_Object=MibTableColumn
mIfNxTemperature=_MIfNxTemperature_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,9),_MIfNxTemperature_Type())
mIfNxTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxTemperature.setStatus(_A)
_MIfNxApInfoApAddress_Type=MacAddress
_MIfNxApInfoApAddress_Object=MibTableColumn
mIfNxApInfoApAddress=_MIfNxApInfoApAddress_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,10),_MIfNxApInfoApAddress_Type())
mIfNxApInfoApAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxApInfoApAddress.setStatus(_A)
_MIfNxApInfoIpAddress_Type=InetIpAddress
_MIfNxApInfoIpAddress_Object=MibTableColumn
mIfNxApInfoIpAddress=_MIfNxApInfoIpAddress_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,11),_MIfNxApInfoIpAddress_Type())
mIfNxApInfoIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxApInfoIpAddress.setStatus(_A)
_MIfNxApInfoConnectedTime_Type=Integer32
_MIfNxApInfoConnectedTime_Object=MibTableColumn
mIfNxApInfoConnectedTime=_MIfNxApInfoConnectedTime_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,12),_MIfNxApInfoConnectedTime_Type())
mIfNxApInfoConnectedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxApInfoConnectedTime.setStatus(_A)
_MIfNxApInfoAvgRssi_Type=Integer32
_MIfNxApInfoAvgRssi_Object=MibTableColumn
mIfNxApInfoAvgRssi=_MIfNxApInfoAvgRssi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,13),_MIfNxApInfoAvgRssi_Type())
mIfNxApInfoAvgRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxApInfoAvgRssi.setStatus(_A)
_MIfNxApInfoAvgLqi_Type=Unsigned32
_MIfNxApInfoAvgLqi_Object=MibTableColumn
mIfNxApInfoAvgLqi=_MIfNxApInfoAvgLqi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,14),_MIfNxApInfoAvgLqi_Type())
mIfNxApInfoAvgLqi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxApInfoAvgLqi.setStatus(_A)
_MIfNxMacStatsTxSuccess_Type=Unsigned32
_MIfNxMacStatsTxSuccess_Object=MibTableColumn
mIfNxMacStatsTxSuccess=_MIfNxMacStatsTxSuccess_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,15),_MIfNxMacStatsTxSuccess_Type())
mIfNxMacStatsTxSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsTxSuccess.setStatus(_A)
_MIfNxMacStatsTxFail_Type=Unsigned32
_MIfNxMacStatsTxFail_Object=MibTableColumn
mIfNxMacStatsTxFail=_MIfNxMacStatsTxFail_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,16),_MIfNxMacStatsTxFail_Type())
mIfNxMacStatsTxFail.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsTxFail.setStatus(_A)
_MIfNxMacStatsTxQueueFull_Type=Unsigned32
_MIfNxMacStatsTxQueueFull_Object=MibTableColumn
mIfNxMacStatsTxQueueFull=_MIfNxMacStatsTxQueueFull_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,17),_MIfNxMacStatsTxQueueFull_Type())
mIfNxMacStatsTxQueueFull.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsTxQueueFull.setStatus(_A)
_MIfNxMacStatsTxNoSync_Type=Unsigned32
_MIfNxMacStatsTxNoSync_Object=MibTableColumn
mIfNxMacStatsTxNoSync=_MIfNxMacStatsTxNoSync_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,18),_MIfNxMacStatsTxNoSync_Type())
mIfNxMacStatsTxNoSync.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsTxNoSync.setStatus(_A)
_MIfNxMacStatsTxNoAssoc_Type=Unsigned32
_MIfNxMacStatsTxNoAssoc_Object=MibTableColumn
mIfNxMacStatsTxNoAssoc=_MIfNxMacStatsTxNoAssoc_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,19),_MIfNxMacStatsTxNoAssoc_Type())
mIfNxMacStatsTxNoAssoc.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsTxNoAssoc.setStatus(_A)
_MIfNxMacStatsTxError_Type=Unsigned32
_MIfNxMacStatsTxError_Object=MibTableColumn
mIfNxMacStatsTxError=_MIfNxMacStatsTxError_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,20),_MIfNxMacStatsTxError_Type())
mIfNxMacStatsTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsTxError.setStatus(_A)
_MIfNxMacStatsTxRetry_Type=Unsigned32
_MIfNxMacStatsTxRetry_Object=MibTableColumn
mIfNxMacStatsTxRetry=_MIfNxMacStatsTxRetry_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,21),_MIfNxMacStatsTxRetry_Type())
mIfNxMacStatsTxRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsTxRetry.setStatus(_A)
_MIfNxMacStatsRxSuccess_Type=Unsigned32
_MIfNxMacStatsRxSuccess_Object=MibTableColumn
mIfNxMacStatsRxSuccess=_MIfNxMacStatsRxSuccess_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,22),_MIfNxMacStatsRxSuccess_Type())
mIfNxMacStatsRxSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsRxSuccess.setStatus(_A)
_MIfNxMacStatsSyncCheckError_Type=Unsigned32
_MIfNxMacStatsSyncCheckError_Object=MibTableColumn
mIfNxMacStatsSyncCheckError=_MIfNxMacStatsSyncCheckError_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,23),_MIfNxMacStatsSyncCheckError_Type())
mIfNxMacStatsSyncCheckError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsSyncCheckError.setStatus(_A)
_MIfNxMacStatsSyncChange_Type=Unsigned32
_MIfNxMacStatsSyncChange_Object=MibTableColumn
mIfNxMacStatsSyncChange=_MIfNxMacStatsSyncChange_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,24),_MIfNxMacStatsSyncChange_Type())
mIfNxMacStatsSyncChange.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxMacStatsSyncChange.setStatus(_A)
_MIfNxCurrentDeviceMode_Type=DeviceModeType
_MIfNxCurrentDeviceMode_Object=MibTableColumn
mIfNxCurrentDeviceMode=_MIfNxCurrentDeviceMode_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,25),_MIfNxCurrentDeviceMode_Type())
mIfNxCurrentDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxCurrentDeviceMode.setStatus(_A)
_MIfNxLastRssi_Type=Integer32
_MIfNxLastRssi_Object=MibTableColumn
mIfNxLastRssi=_MIfNxLastRssi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,26),_MIfNxLastRssi_Type())
mIfNxLastRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxLastRssi.setStatus(_A)
_MIfNxLastLqi_Type=Unsigned32
_MIfNxLastLqi_Object=MibTableColumn
mIfNxLastLqi=_MIfNxLastLqi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,27),_MIfNxLastLqi_Type())
mIfNxLastLqi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxLastLqi.setStatus(_A)
_MIfNxLastChan_Type=Unsigned32
_MIfNxLastChan_Object=MibTableColumn
mIfNxLastChan=_MIfNxLastChan_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,28),_MIfNxLastChan_Type())
mIfNxLastChan.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxLastChan.setStatus(_A)
_MIfNxActiveNic_Type=TruthValue
_MIfNxActiveNic_Object=MibTableColumn
mIfNxActiveNic=_MIfNxActiveNic_Object((1,3,6,1,4,1,4130,10,2,3,1,2,1,1,29),_MIfNxActiveNic_Type())
mIfNxActiveNic.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxActiveNic.setStatus(_A)
_MIfNxStatusConnRemTable_Object=MibTable
mIfNxStatusConnRemTable=_MIfNxStatusConnRemTable_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2))
if mibBuilder.loadTexts:mIfNxStatusConnRemTable.setStatus(_A)
_MIfNxStatusConnRemEntry_Object=MibTableRow
mIfNxStatusConnRemEntry=_MIfNxStatusConnRemEntry_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1))
mIfNxStatusConnRemEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:mIfNxStatusConnRemEntry.setStatus(_A)
_MIfNxStatusConnRemAddress_Type=MacAddress
_MIfNxStatusConnRemAddress_Object=MibTableColumn
mIfNxStatusConnRemAddress=_MIfNxStatusConnRemAddress_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,1),_MIfNxStatusConnRemAddress_Type())
mIfNxStatusConnRemAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemAddress.setStatus(_A)
_MIfNxStatusConnRemIpAddress_Type=InetIpAddress
_MIfNxStatusConnRemIpAddress_Object=MibTableColumn
mIfNxStatusConnRemIpAddress=_MIfNxStatusConnRemIpAddress_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,2),_MIfNxStatusConnRemIpAddress_Type())
mIfNxStatusConnRemIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemIpAddress.setStatus(_A)
_MIfNxStatusConnRemTimeToLive_Type=Unsigned32
_MIfNxStatusConnRemTimeToLive_Object=MibTableColumn
mIfNxStatusConnRemTimeToLive=_MIfNxStatusConnRemTimeToLive_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,3),_MIfNxStatusConnRemTimeToLive_Type())
mIfNxStatusConnRemTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemTimeToLive.setStatus(_A)
_MIfNxStatusConnRemLinkStatus_Type=LinkStatus
_MIfNxStatusConnRemLinkStatus_Object=MibTableColumn
mIfNxStatusConnRemLinkStatus=_MIfNxStatusConnRemLinkStatus_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,4),_MIfNxStatusConnRemLinkStatus_Type())
mIfNxStatusConnRemLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemLinkStatus.setStatus(_A)
_MIfNxStatusConnRemNicId_Type=UnsignedShort
_MIfNxStatusConnRemNicId_Object=MibTableColumn
mIfNxStatusConnRemNicId=_MIfNxStatusConnRemNicId_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,5),_MIfNxStatusConnRemNicId_Type())
mIfNxStatusConnRemNicId.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemNicId.setStatus(_A)
_MIfNxStatusConnRemAvgRssi_Type=Integer32
_MIfNxStatusConnRemAvgRssi_Object=MibTableColumn
mIfNxStatusConnRemAvgRssi=_MIfNxStatusConnRemAvgRssi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,6),_MIfNxStatusConnRemAvgRssi_Type())
mIfNxStatusConnRemAvgRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemAvgRssi.setStatus(_A)
_MIfNxStatusConnRemAvgLqi_Type=Unsigned32
_MIfNxStatusConnRemAvgLqi_Object=MibTableColumn
mIfNxStatusConnRemAvgLqi=_MIfNxStatusConnRemAvgLqi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,7),_MIfNxStatusConnRemAvgLqi_Type())
mIfNxStatusConnRemAvgLqi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemAvgLqi.setStatus(_A)
_MIfNxStatusConnRemStatsTxPackets_Type=Unsigned32
_MIfNxStatusConnRemStatsTxPackets_Object=MibTableColumn
mIfNxStatusConnRemStatsTxPackets=_MIfNxStatusConnRemStatsTxPackets_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,8),_MIfNxStatusConnRemStatsTxPackets_Type())
mIfNxStatusConnRemStatsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsTxPackets.setStatus(_A)
_MIfNxStatusConnRemStatsTxBytes_Type=Unsigned32
_MIfNxStatusConnRemStatsTxBytes_Object=MibTableColumn
mIfNxStatusConnRemStatsTxBytes=_MIfNxStatusConnRemStatsTxBytes_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,9),_MIfNxStatusConnRemStatsTxBytes_Type())
mIfNxStatusConnRemStatsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsTxBytes.setStatus(_A)
_MIfNxStatusConnRemStatsRxPackets_Type=Unsigned32
_MIfNxStatusConnRemStatsRxPackets_Object=MibTableColumn
mIfNxStatusConnRemStatsRxPackets=_MIfNxStatusConnRemStatsRxPackets_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,10),_MIfNxStatusConnRemStatsRxPackets_Type())
mIfNxStatusConnRemStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsRxPackets.setStatus(_A)
_MIfNxStatusConnRemStatsRxBytes_Type=Unsigned32
_MIfNxStatusConnRemStatsRxBytes_Object=MibTableColumn
mIfNxStatusConnRemStatsRxBytes=_MIfNxStatusConnRemStatsRxBytes_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,11),_MIfNxStatusConnRemStatsRxBytes_Type())
mIfNxStatusConnRemStatsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsRxBytes.setStatus(_A)
_MIfNxStatusConnRemStatsTxError_Type=Unsigned32
_MIfNxStatusConnRemStatsTxError_Object=MibTableColumn
mIfNxStatusConnRemStatsTxError=_MIfNxStatusConnRemStatsTxError_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,12),_MIfNxStatusConnRemStatsTxError_Type())
mIfNxStatusConnRemStatsTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsTxError.setStatus(_A)
_MIfNxStatusConnRemStatsRxError_Type=Unsigned32
_MIfNxStatusConnRemStatsRxError_Object=MibTableColumn
mIfNxStatusConnRemStatsRxError=_MIfNxStatusConnRemStatsRxError_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,13),_MIfNxStatusConnRemStatsRxError_Type())
mIfNxStatusConnRemStatsRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsRxError.setStatus(_A)
_MIfNxStatusConnRemStatsTxDrop_Type=Unsigned32
_MIfNxStatusConnRemStatsTxDrop_Object=MibTableColumn
mIfNxStatusConnRemStatsTxDrop=_MIfNxStatusConnRemStatsTxDrop_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,14),_MIfNxStatusConnRemStatsTxDrop_Type())
mIfNxStatusConnRemStatsTxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsTxDrop.setStatus(_A)
_MIfNxStatusConnRemStatsRxDrop_Type=Unsigned32
_MIfNxStatusConnRemStatsRxDrop_Object=MibTableColumn
mIfNxStatusConnRemStatsRxDrop=_MIfNxStatusConnRemStatsRxDrop_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,15),_MIfNxStatusConnRemStatsRxDrop_Type())
mIfNxStatusConnRemStatsRxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsRxDrop.setStatus(_A)
_MIfNxStatusConnRemAvgSnr_Type=Unsigned32
_MIfNxStatusConnRemAvgSnr_Object=MibTableColumn
mIfNxStatusConnRemAvgSnr=_MIfNxStatusConnRemAvgSnr_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,16),_MIfNxStatusConnRemAvgSnr_Type())
mIfNxStatusConnRemAvgSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemAvgSnr.setStatus(_A)
_MIfNxStatusConnRemStatsGateway_Type=MacAddress
_MIfNxStatusConnRemStatsGateway_Object=MibTableColumn
mIfNxStatusConnRemStatsGateway=_MIfNxStatusConnRemStatsGateway_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,17),_MIfNxStatusConnRemStatsGateway_Type())
mIfNxStatusConnRemStatsGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsGateway.setStatus(_A)
_MIfNxStatusConnRemStatsAllIp_Type=OctetString
_MIfNxStatusConnRemStatsAllIp_Object=MibTableColumn
mIfNxStatusConnRemStatsAllIp=_MIfNxStatusConnRemStatsAllIp_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,18),_MIfNxStatusConnRemStatsAllIp_Type())
mIfNxStatusConnRemStatsAllIp.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsAllIp.setStatus(_A)
_MIfNxStatusConnRemStatsName_Type=OctetString
_MIfNxStatusConnRemStatsName_Object=MibTableColumn
mIfNxStatusConnRemStatsName=_MIfNxStatusConnRemStatsName_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,19),_MIfNxStatusConnRemStatsName_Type())
mIfNxStatusConnRemStatsName.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsName.setStatus(_A)
_MIfNxStatusConnRemStatsAlarmed_Type=TruthValue
_MIfNxStatusConnRemStatsAlarmed_Object=MibTableColumn
mIfNxStatusConnRemStatsAlarmed=_MIfNxStatusConnRemStatsAlarmed_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,20),_MIfNxStatusConnRemStatsAlarmed_Type())
mIfNxStatusConnRemStatsAlarmed.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsAlarmed.setStatus(_A)
_MIfNxStatusConnRemStatsVersion_Type=OctetString
_MIfNxStatusConnRemStatsVersion_Object=MibTableColumn
mIfNxStatusConnRemStatsVersion=_MIfNxStatusConnRemStatsVersion_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,21),_MIfNxStatusConnRemStatsVersion_Type())
mIfNxStatusConnRemStatsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsVersion.setStatus(_A)
class _MIfNxStatusConnRemStatsTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_MIfNxStatusConnRemStatsTemp_Type.__name__=_I
_MIfNxStatusConnRemStatsTemp_Object=MibTableColumn
mIfNxStatusConnRemStatsTemp=_MIfNxStatusConnRemStatsTemp_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,22),_MIfNxStatusConnRemStatsTemp_Type())
mIfNxStatusConnRemStatsTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsTemp.setStatus(_A)
_MIfNxStatusConnRemStatsDwnRssi_Type=Integer32
_MIfNxStatusConnRemStatsDwnRssi_Object=MibTableColumn
mIfNxStatusConnRemStatsDwnRssi=_MIfNxStatusConnRemStatsDwnRssi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,23),_MIfNxStatusConnRemStatsDwnRssi_Type())
mIfNxStatusConnRemStatsDwnRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsDwnRssi.setStatus(_A)
_MIfNxStatusConnRemStatsDwnLqi_Type=Unsigned32
_MIfNxStatusConnRemStatsDwnLqi_Object=MibTableColumn
mIfNxStatusConnRemStatsDwnLqi=_MIfNxStatusConnRemStatsDwnLqi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,24),_MIfNxStatusConnRemStatsDwnLqi_Type())
mIfNxStatusConnRemStatsDwnLqi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsDwnLqi.setStatus(_A)
_MIfNxStatusConnRemStatsDwnSnr_Type=Unsigned32
_MIfNxStatusConnRemStatsDwnSnr_Object=MibTableColumn
mIfNxStatusConnRemStatsDwnSnr=_MIfNxStatusConnRemStatsDwnSnr_Object((1,3,6,1,4,1,4130,10,2,3,1,2,2,1,25),_MIfNxStatusConnRemStatsDwnSnr_Type())
mIfNxStatusConnRemStatsDwnSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusConnRemStatsDwnSnr.setStatus(_A)
_MIfNxStatusEndpointTable_Object=MibTable
mIfNxStatusEndpointTable=_MIfNxStatusEndpointTable_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3))
if mibBuilder.loadTexts:mIfNxStatusEndpointTable.setStatus(_A)
_MIfNxStatusEndpointEntry_Object=MibTableRow
mIfNxStatusEndpointEntry=_MIfNxStatusEndpointEntry_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1))
mIfNxStatusEndpointEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:mIfNxStatusEndpointEntry.setStatus(_A)
_MIfNxStatusEndpointAddress_Type=MacAddress
_MIfNxStatusEndpointAddress_Object=MibTableColumn
mIfNxStatusEndpointAddress=_MIfNxStatusEndpointAddress_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,1),_MIfNxStatusEndpointAddress_Type())
mIfNxStatusEndpointAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointAddress.setStatus(_A)
_MIfNxStatusEndpointIpAddress_Type=InetIpAddress
_MIfNxStatusEndpointIpAddress_Object=MibTableColumn
mIfNxStatusEndpointIpAddress=_MIfNxStatusEndpointIpAddress_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,2),_MIfNxStatusEndpointIpAddress_Type())
mIfNxStatusEndpointIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointIpAddress.setStatus(_A)
_MIfNxStatusEndpointTimeToLive_Type=Unsigned32
_MIfNxStatusEndpointTimeToLive_Object=MibTableColumn
mIfNxStatusEndpointTimeToLive=_MIfNxStatusEndpointTimeToLive_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,3),_MIfNxStatusEndpointTimeToLive_Type())
mIfNxStatusEndpointTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointTimeToLive.setStatus(_A)
_MIfNxStatusEndpointRemAddress_Type=MacAddress
_MIfNxStatusEndpointRemAddress_Object=MibTableColumn
mIfNxStatusEndpointRemAddress=_MIfNxStatusEndpointRemAddress_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,4),_MIfNxStatusEndpointRemAddress_Type())
mIfNxStatusEndpointRemAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointRemAddress.setStatus(_A)
_MIfNxStatusEndpointStatsTxPackets_Type=Unsigned32
_MIfNxStatusEndpointStatsTxPackets_Object=MibTableColumn
mIfNxStatusEndpointStatsTxPackets=_MIfNxStatusEndpointStatsTxPackets_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,5),_MIfNxStatusEndpointStatsTxPackets_Type())
mIfNxStatusEndpointStatsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsTxPackets.setStatus(_A)
_MIfNxStatusEndpointStatsTxBytes_Type=Unsigned32
_MIfNxStatusEndpointStatsTxBytes_Object=MibTableColumn
mIfNxStatusEndpointStatsTxBytes=_MIfNxStatusEndpointStatsTxBytes_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,6),_MIfNxStatusEndpointStatsTxBytes_Type())
mIfNxStatusEndpointStatsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsTxBytes.setStatus(_A)
_MIfNxStatusEndpointStatsRxPackets_Type=Unsigned32
_MIfNxStatusEndpointStatsRxPackets_Object=MibTableColumn
mIfNxStatusEndpointStatsRxPackets=_MIfNxStatusEndpointStatsRxPackets_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,7),_MIfNxStatusEndpointStatsRxPackets_Type())
mIfNxStatusEndpointStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsRxPackets.setStatus(_A)
_MIfNxStatusEndpointStatsRxBytes_Type=Unsigned32
_MIfNxStatusEndpointStatsRxBytes_Object=MibTableColumn
mIfNxStatusEndpointStatsRxBytes=_MIfNxStatusEndpointStatsRxBytes_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,8),_MIfNxStatusEndpointStatsRxBytes_Type())
mIfNxStatusEndpointStatsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsRxBytes.setStatus(_A)
_MIfNxStatusEndpointStatsTxError_Type=Unsigned32
_MIfNxStatusEndpointStatsTxError_Object=MibTableColumn
mIfNxStatusEndpointStatsTxError=_MIfNxStatusEndpointStatsTxError_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,9),_MIfNxStatusEndpointStatsTxError_Type())
mIfNxStatusEndpointStatsTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsTxError.setStatus(_A)
_MIfNxStatusEndpointStatsRxError_Type=Unsigned32
_MIfNxStatusEndpointStatsRxError_Object=MibTableColumn
mIfNxStatusEndpointStatsRxError=_MIfNxStatusEndpointStatsRxError_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,10),_MIfNxStatusEndpointStatsRxError_Type())
mIfNxStatusEndpointStatsRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsRxError.setStatus(_A)
_MIfNxStatusEndpointStatsTxDrop_Type=Unsigned32
_MIfNxStatusEndpointStatsTxDrop_Object=MibTableColumn
mIfNxStatusEndpointStatsTxDrop=_MIfNxStatusEndpointStatsTxDrop_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,11),_MIfNxStatusEndpointStatsTxDrop_Type())
mIfNxStatusEndpointStatsTxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsTxDrop.setStatus(_A)
_MIfNxStatusEndpointStatsRxDrop_Type=Unsigned32
_MIfNxStatusEndpointStatsRxDrop_Object=MibTableColumn
mIfNxStatusEndpointStatsRxDrop=_MIfNxStatusEndpointStatsRxDrop_Object((1,3,6,1,4,1,4130,10,2,3,1,2,3,1,12),_MIfNxStatusEndpointStatsRxDrop_Type())
mIfNxStatusEndpointStatsRxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusEndpointStatsRxDrop.setStatus(_A)
_MIfNxStatusActChanTable_Object=MibTable
mIfNxStatusActChanTable=_MIfNxStatusActChanTable_Object((1,3,6,1,4,1,4130,10,2,3,1,2,4))
if mibBuilder.loadTexts:mIfNxStatusActChanTable.setStatus(_A)
_MIfNxStatusActChanEntry_Object=MibTableRow
mIfNxStatusActChanEntry=_MIfNxStatusActChanEntry_Object((1,3,6,1,4,1,4130,10,2,3,1,2,4,1))
mIfNxStatusActChanEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:mIfNxStatusActChanEntry.setStatus(_A)
_MIfNxStatusActChanChannel_Type=UnsignedByte
_MIfNxStatusActChanChannel_Object=MibTableColumn
mIfNxStatusActChanChannel=_MIfNxStatusActChanChannel_Object((1,3,6,1,4,1,4130,10,2,3,1,2,4,1,1),_MIfNxStatusActChanChannel_Type())
mIfNxStatusActChanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusActChanChannel.setStatus(_A)
_MIfNxStatusActChanFrequency_Type=OctetString
_MIfNxStatusActChanFrequency_Object=MibTableColumn
mIfNxStatusActChanFrequency=_MIfNxStatusActChanFrequency_Object((1,3,6,1,4,1,4130,10,2,3,1,2,4,1,2),_MIfNxStatusActChanFrequency_Type())
mIfNxStatusActChanFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusActChanFrequency.setStatus(_A)
_MIfNxStatusActChanAvgRssi_Type=Integer32
_MIfNxStatusActChanAvgRssi_Object=MibTableColumn
mIfNxStatusActChanAvgRssi=_MIfNxStatusActChanAvgRssi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,4,1,3),_MIfNxStatusActChanAvgRssi_Type())
mIfNxStatusActChanAvgRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusActChanAvgRssi.setStatus(_A)
_MIfNxStatusActChanAvgLqi_Type=Unsigned32
_MIfNxStatusActChanAvgLqi_Object=MibTableColumn
mIfNxStatusActChanAvgLqi=_MIfNxStatusActChanAvgLqi_Object((1,3,6,1,4,1,4130,10,2,3,1,2,4,1,4),_MIfNxStatusActChanAvgLqi_Type())
mIfNxStatusActChanAvgLqi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfNxStatusActChanAvgLqi.setStatus(_A)
_MdsIfNxMIBConformance_ObjectIdentity=ObjectIdentity
mdsIfNxMIBConformance=_MdsIfNxMIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,2,3,3))
_MdsIfNxMIBCompliances_ObjectIdentity=ObjectIdentity
mdsIfNxMIBCompliances=_MdsIfNxMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,2,3,3,1))
_MdsIfNxMIBGroups_ObjectIdentity=ObjectIdentity
mdsIfNxMIBGroups=_MdsIfNxMIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,2,3,3,2))
mIfNxStatusGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,3,3,2,1))
mIfNxStatusGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:mIfNxStatusGroup.setStatus(_A)
mIfNxStatusConnRemGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,3,3,2,2))
mIfNxStatusConnRemGroup.setObjects(*((_B,_F),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:mIfNxStatusConnRemGroup.setStatus(_A)
mIfNxStatusEndpointGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,3,3,2,3))
mIfNxStatusEndpointGroup.setObjects(*((_B,_G),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:mIfNxStatusEndpointGroup.setStatus(_A)
mIfNxStatusActChanGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,3,3,2,4))
mIfNxStatusActChanGroup.setObjects(*((_B,_H),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:mIfNxStatusActChanGroup.setStatus(_A)
mIfNxCompliance=ModuleCompliance((1,3,6,1,4,1,4130,10,2,3,3,1,1))
mIfNxCompliance.setObjects(*((_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:mIfNxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'UnsignedByte':UnsignedByte,'UnsignedShort':UnsignedShort,'LinkStatus':LinkStatus,'InitStatus':InitStatus,'DeviceModeType':DeviceModeType,'ModemType':ModemType,'AlarmFlags':AlarmFlags,'FirmwareRevision':FirmwareRevision,'InetIpAddress':InetIpAddress,'mdsIfNxMIB':mdsIfNxMIB,'mIfNxMIBObjects':mIfNxMIBObjects,'mIfNxConfig':mIfNxConfig,'mIfNxStatus':mIfNxStatus,'mIfNxStatusTable':mIfNxStatusTable,'mIfNxStatusEntry':mIfNxStatusEntry,_K:mIfNxLinkStatus,_L:mIfNxInitStatus,_M:mIfNxCurrentModem,_N:mIfNxAlarms,_O:mIfNxSerialNumber,_P:mIfNxFirmwareRevision,_Q:mIfNxHardwareId,_R:mIfNxHardwareRevision,_S:mIfNxTemperature,_T:mIfNxApInfoApAddress,_U:mIfNxApInfoIpAddress,_V:mIfNxApInfoConnectedTime,_W:mIfNxApInfoAvgRssi,_X:mIfNxApInfoAvgLqi,_Y:mIfNxMacStatsTxSuccess,_Z:mIfNxMacStatsTxFail,_a:mIfNxMacStatsTxQueueFull,_b:mIfNxMacStatsTxNoSync,_c:mIfNxMacStatsTxNoAssoc,_d:mIfNxMacStatsTxError,_e:mIfNxMacStatsTxRetry,_f:mIfNxMacStatsRxSuccess,_g:mIfNxMacStatsSyncCheckError,_h:mIfNxMacStatsSyncChange,_i:mIfNxCurrentDeviceMode,_j:mIfNxLastRssi,_k:mIfNxLastLqi,_l:mIfNxLastChan,_m:mIfNxActiveNic,'mIfNxStatusConnRemTable':mIfNxStatusConnRemTable,'mIfNxStatusConnRemEntry':mIfNxStatusConnRemEntry,_F:mIfNxStatusConnRemAddress,_n:mIfNxStatusConnRemIpAddress,_o:mIfNxStatusConnRemTimeToLive,_p:mIfNxStatusConnRemLinkStatus,_q:mIfNxStatusConnRemNicId,_r:mIfNxStatusConnRemAvgRssi,_s:mIfNxStatusConnRemAvgLqi,_t:mIfNxStatusConnRemStatsTxPackets,_u:mIfNxStatusConnRemStatsTxBytes,_v:mIfNxStatusConnRemStatsRxPackets,_w:mIfNxStatusConnRemStatsRxBytes,_x:mIfNxStatusConnRemStatsTxError,_y:mIfNxStatusConnRemStatsRxError,_z:mIfNxStatusConnRemStatsTxDrop,_A0:mIfNxStatusConnRemStatsRxDrop,_A1:mIfNxStatusConnRemAvgSnr,_A2:mIfNxStatusConnRemStatsGateway,_A3:mIfNxStatusConnRemStatsAllIp,_A4:mIfNxStatusConnRemStatsName,_A5:mIfNxStatusConnRemStatsAlarmed,_A6:mIfNxStatusConnRemStatsVersion,_A7:mIfNxStatusConnRemStatsTemp,_A8:mIfNxStatusConnRemStatsDwnRssi,_A9:mIfNxStatusConnRemStatsDwnLqi,_AA:mIfNxStatusConnRemStatsDwnSnr,'mIfNxStatusEndpointTable':mIfNxStatusEndpointTable,'mIfNxStatusEndpointEntry':mIfNxStatusEndpointEntry,_G:mIfNxStatusEndpointAddress,_AB:mIfNxStatusEndpointIpAddress,_AC:mIfNxStatusEndpointTimeToLive,_AD:mIfNxStatusEndpointRemAddress,_AE:mIfNxStatusEndpointStatsTxPackets,_AF:mIfNxStatusEndpointStatsTxBytes,_AG:mIfNxStatusEndpointStatsRxPackets,_AH:mIfNxStatusEndpointStatsRxBytes,_AI:mIfNxStatusEndpointStatsTxError,_AJ:mIfNxStatusEndpointStatsRxError,_AK:mIfNxStatusEndpointStatsTxDrop,_AL:mIfNxStatusEndpointStatsRxDrop,'mIfNxStatusActChanTable':mIfNxStatusActChanTable,'mIfNxStatusActChanEntry':mIfNxStatusActChanEntry,_H:mIfNxStatusActChanChannel,_AM:mIfNxStatusActChanFrequency,_AN:mIfNxStatusActChanAvgRssi,_AO:mIfNxStatusActChanAvgLqi,'mdsIfNxMIBConformance':mdsIfNxMIBConformance,'mdsIfNxMIBCompliances':mdsIfNxMIBCompliances,'mIfNxCompliance':mIfNxCompliance,'mdsIfNxMIBGroups':mdsIfNxMIBGroups,_AP:mIfNxStatusGroup,_AQ:mIfNxStatusConnRemGroup,_AR:mIfNxStatusEndpointGroup,_AS:mIfNxStatusActChanGroup})