_AO='mIfLwStatusEndpointGroup'
_AN='mIfLwStatusConnRemGroup'
_AM='mIfLwStatusGroup'
_AL='mIfLwStatusEndpointStatsRxDrop'
_AK='mIfLwStatusEndpointStatsTxDrop'
_AJ='mIfLwStatusEndpointStatsRxError'
_AI='mIfLwStatusEndpointStatsTxError'
_AH='mIfLwStatusEndpointStatsRxBytes'
_AG='mIfLwStatusEndpointStatsRxPackets'
_AF='mIfLwStatusEndpointStatsTxBytes'
_AE='mIfLwStatusEndpointStatsTxPackets'
_AD='mIfLwStatusEndpointRemAddress'
_AC='mIfLwStatusEndpointTimeToLive'
_AB='mIfLwStatusEndpointIpAddress'
_AA='mIfLwStatusConnRemStatsDwnMod'
_A9='mIfLwStatusConnRemStatsDwnSnr'
_A8='mIfLwStatusConnRemStatsDwnRssi'
_A7='mIfLwStatusConnRemStatsTemp'
_A6='mIfLwStatusConnRemStatsVersion'
_A5='mIfLwStatusConnRemStatsAlarmed'
_A4='mIfLwStatusConnRemStatsName'
_A3='mIfLwStatusConnRemStatsAllIp'
_A2='mIfLwStatusConnRemStatsGateway'
_A1='mIfLwStatusConnRemStatsRxDrop'
_A0='mIfLwStatusConnRemStatsTxDrop'
_z='mIfLwStatusConnRemStatsRxError'
_y='mIfLwStatusConnRemStatsTxError'
_x='mIfLwStatusConnRemStatsRxBytes'
_w='mIfLwStatusConnRemStatsRxPackets'
_v='mIfLwStatusConnRemStatsTxBytes'
_u='mIfLwStatusConnRemStatsTxPackets'
_t='mIfLwStatusConnRemMod'
_s='mIfLwStatusConnRemSnr'
_r='mIfLwStatusConnRemRssi'
_q='mIfLwStatusConnRemNicId'
_p='mIfLwStatusConnRemLinkStatus'
_o='mIfLwStatusConnRemTimeToLive'
_n='mIfLwStatusConnRemIpAddress'
_m='mIfLwActiveNic'
_l='mIfLwLastRate'
_k='mIfLwLastMod'
_j='mIfLwLastSnr'
_i='mIfLwLastRssi'
_h='mIfLwModemStatsRxError'
_g='mIfLwModemStatsRxSuccess'
_f='mIfLwModemStatsTxError'
_e='mIfLwModemStatsTxSuccess'
_d='mIfLwMacStatsRxError'
_c='mIfLwMacStatsRxSuccess'
_b='mIfLwMacStatsTxRetry'
_a='mIfLwMacStatsTxError'
_Z='mIfLwMacStatsTxQueueFull'
_Y='mIfLwMacStatsTxSuccess'
_X='mIfLwApInfoMod'
_W='mIfLwApInfoSnr'
_V='mIfLwApInfoRssi'
_U='mIfLwApInfoConnectedTime'
_T='mIfLwApInfoIpAddress'
_S='mIfLwApInfoApAddress'
_R='mIfLwTemperature'
_Q='mIfLwHardwareRevision'
_P='mIfLwHardwareId'
_O='mIfLwFirmwareRevision'
_N='mIfLwSerialNumber'
_M='mIfLwAlarms'
_L='mIfLwCurrentDeviceMode'
_K='mIfLwInitStatus'
_J='mIfLwLinkStatus'
_I='initializing'
_H='Integer32'
_G='mIfLwStatusEndpointAddress'
_F='mIfLwStatusConnRemAddress'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='MDS-IF-LW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
mdsInterfaces,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsInterfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
mdsIfLwMIB=ModuleIdentity((1,3,6,1,4,1,4130,10,2,6))
if mibBuilder.loadTexts:mdsIfLwMIB.setRevisions(('2018-09-13 00:00',))
class UnsignedByte(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class UnsignedShort(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class LinkStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),('scanning',1),('negotiating',2),('authenticating',3),('associated',4),('disassociated',5)))
class InitStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('off',0),(_I,1),('discovering',2),('reprogramming',3),('configuring',4),('complete',5),('error',6)))
class DeviceModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('remote',0),('accessPoint',1),('storeAndForward',2),('test',3)))
class ModulationModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('qpsk25',2),('qpsk50',3),('qpsk75',4),('qam16r50',5),('qam16r75',6)))
class AlarmFlags(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('temperature',0),('notCalibrated',23)))
class FirmwareRevision(TextualConvention,OctetString):status=_A;displayHint='32a'
class InetIpAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
class FrequencyType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class ChannelType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class FecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('adaptiveGain',1),('lowGain',2)))
class RateType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MIfLwMIBObjects_ObjectIdentity=ObjectIdentity
mIfLwMIBObjects=_MIfLwMIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,2,6,1))
_MIfLwConfig_ObjectIdentity=ObjectIdentity
mIfLwConfig=_MIfLwConfig_ObjectIdentity((1,3,6,1,4,1,4130,10,2,6,1,1))
_MIfLwStatus_ObjectIdentity=ObjectIdentity
mIfLwStatus=_MIfLwStatus_ObjectIdentity((1,3,6,1,4,1,4130,10,2,6,1,2))
_MIfLwStatusTable_Object=MibTable
mIfLwStatusTable=_MIfLwStatusTable_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1))
if mibBuilder.loadTexts:mIfLwStatusTable.setStatus(_A)
_MIfLwStatusEntry_Object=MibTableRow
mIfLwStatusEntry=_MIfLwStatusEntry_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1))
mIfLwStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mIfLwStatusEntry.setStatus(_A)
_MIfLwLinkStatus_Type=LinkStatus
_MIfLwLinkStatus_Object=MibTableColumn
mIfLwLinkStatus=_MIfLwLinkStatus_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,1),_MIfLwLinkStatus_Type())
mIfLwLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwLinkStatus.setStatus(_A)
_MIfLwInitStatus_Type=InitStatus
_MIfLwInitStatus_Object=MibTableColumn
mIfLwInitStatus=_MIfLwInitStatus_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,2),_MIfLwInitStatus_Type())
mIfLwInitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwInitStatus.setStatus(_A)
_MIfLwCurrentDeviceMode_Type=DeviceModeType
_MIfLwCurrentDeviceMode_Object=MibTableColumn
mIfLwCurrentDeviceMode=_MIfLwCurrentDeviceMode_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,3),_MIfLwCurrentDeviceMode_Type())
mIfLwCurrentDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwCurrentDeviceMode.setStatus(_A)
_MIfLwAlarms_Type=AlarmFlags
_MIfLwAlarms_Object=MibTableColumn
mIfLwAlarms=_MIfLwAlarms_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,4),_MIfLwAlarms_Type())
mIfLwAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwAlarms.setStatus(_A)
_MIfLwSerialNumber_Type=Unsigned32
_MIfLwSerialNumber_Object=MibTableColumn
mIfLwSerialNumber=_MIfLwSerialNumber_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,5),_MIfLwSerialNumber_Type())
mIfLwSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwSerialNumber.setStatus(_A)
_MIfLwFirmwareRevision_Type=FirmwareRevision
_MIfLwFirmwareRevision_Object=MibTableColumn
mIfLwFirmwareRevision=_MIfLwFirmwareRevision_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,6),_MIfLwFirmwareRevision_Type())
mIfLwFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwFirmwareRevision.setStatus(_A)
_MIfLwHardwareId_Type=UnsignedByte
_MIfLwHardwareId_Object=MibTableColumn
mIfLwHardwareId=_MIfLwHardwareId_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,7),_MIfLwHardwareId_Type())
mIfLwHardwareId.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwHardwareId.setStatus(_A)
_MIfLwHardwareRevision_Type=UnsignedByte
_MIfLwHardwareRevision_Object=MibTableColumn
mIfLwHardwareRevision=_MIfLwHardwareRevision_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,8),_MIfLwHardwareRevision_Type())
mIfLwHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwHardwareRevision.setStatus(_A)
_MIfLwTemperature_Type=Integer32
_MIfLwTemperature_Object=MibTableColumn
mIfLwTemperature=_MIfLwTemperature_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,9),_MIfLwTemperature_Type())
mIfLwTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwTemperature.setStatus(_A)
_MIfLwApInfoApAddress_Type=MacAddress
_MIfLwApInfoApAddress_Object=MibTableColumn
mIfLwApInfoApAddress=_MIfLwApInfoApAddress_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,10),_MIfLwApInfoApAddress_Type())
mIfLwApInfoApAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwApInfoApAddress.setStatus(_A)
_MIfLwApInfoIpAddress_Type=InetIpAddress
_MIfLwApInfoIpAddress_Object=MibTableColumn
mIfLwApInfoIpAddress=_MIfLwApInfoIpAddress_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,11),_MIfLwApInfoIpAddress_Type())
mIfLwApInfoIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwApInfoIpAddress.setStatus(_A)
_MIfLwApInfoConnectedTime_Type=Integer32
_MIfLwApInfoConnectedTime_Object=MibTableColumn
mIfLwApInfoConnectedTime=_MIfLwApInfoConnectedTime_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,12),_MIfLwApInfoConnectedTime_Type())
mIfLwApInfoConnectedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwApInfoConnectedTime.setStatus(_A)
_MIfLwApInfoRssi_Type=Integer32
_MIfLwApInfoRssi_Object=MibTableColumn
mIfLwApInfoRssi=_MIfLwApInfoRssi_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,13),_MIfLwApInfoRssi_Type())
mIfLwApInfoRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwApInfoRssi.setStatus(_A)
_MIfLwApInfoSnr_Type=Unsigned32
_MIfLwApInfoSnr_Object=MibTableColumn
mIfLwApInfoSnr=_MIfLwApInfoSnr_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,14),_MIfLwApInfoSnr_Type())
mIfLwApInfoSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwApInfoSnr.setStatus(_A)
_MIfLwApInfoMod_Type=ModulationModeType
_MIfLwApInfoMod_Object=MibTableColumn
mIfLwApInfoMod=_MIfLwApInfoMod_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,15),_MIfLwApInfoMod_Type())
mIfLwApInfoMod.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwApInfoMod.setStatus(_A)
_MIfLwMacStatsTxSuccess_Type=Unsigned32
_MIfLwMacStatsTxSuccess_Object=MibTableColumn
mIfLwMacStatsTxSuccess=_MIfLwMacStatsTxSuccess_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,16),_MIfLwMacStatsTxSuccess_Type())
mIfLwMacStatsTxSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwMacStatsTxSuccess.setStatus(_A)
_MIfLwMacStatsTxQueueFull_Type=Unsigned32
_MIfLwMacStatsTxQueueFull_Object=MibTableColumn
mIfLwMacStatsTxQueueFull=_MIfLwMacStatsTxQueueFull_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,17),_MIfLwMacStatsTxQueueFull_Type())
mIfLwMacStatsTxQueueFull.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwMacStatsTxQueueFull.setStatus(_A)
_MIfLwMacStatsTxError_Type=Unsigned32
_MIfLwMacStatsTxError_Object=MibTableColumn
mIfLwMacStatsTxError=_MIfLwMacStatsTxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,18),_MIfLwMacStatsTxError_Type())
mIfLwMacStatsTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwMacStatsTxError.setStatus(_A)
_MIfLwMacStatsTxRetry_Type=Unsigned32
_MIfLwMacStatsTxRetry_Object=MibTableColumn
mIfLwMacStatsTxRetry=_MIfLwMacStatsTxRetry_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,19),_MIfLwMacStatsTxRetry_Type())
mIfLwMacStatsTxRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwMacStatsTxRetry.setStatus(_A)
_MIfLwMacStatsRxSuccess_Type=Unsigned32
_MIfLwMacStatsRxSuccess_Object=MibTableColumn
mIfLwMacStatsRxSuccess=_MIfLwMacStatsRxSuccess_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,20),_MIfLwMacStatsRxSuccess_Type())
mIfLwMacStatsRxSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwMacStatsRxSuccess.setStatus(_A)
_MIfLwMacStatsRxError_Type=Unsigned32
_MIfLwMacStatsRxError_Object=MibTableColumn
mIfLwMacStatsRxError=_MIfLwMacStatsRxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,21),_MIfLwMacStatsRxError_Type())
mIfLwMacStatsRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwMacStatsRxError.setStatus(_A)
_MIfLwModemStatsTxSuccess_Type=Unsigned32
_MIfLwModemStatsTxSuccess_Object=MibTableColumn
mIfLwModemStatsTxSuccess=_MIfLwModemStatsTxSuccess_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,22),_MIfLwModemStatsTxSuccess_Type())
mIfLwModemStatsTxSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwModemStatsTxSuccess.setStatus(_A)
_MIfLwModemStatsTxError_Type=Unsigned32
_MIfLwModemStatsTxError_Object=MibTableColumn
mIfLwModemStatsTxError=_MIfLwModemStatsTxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,23),_MIfLwModemStatsTxError_Type())
mIfLwModemStatsTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwModemStatsTxError.setStatus(_A)
_MIfLwModemStatsRxSuccess_Type=Unsigned32
_MIfLwModemStatsRxSuccess_Object=MibTableColumn
mIfLwModemStatsRxSuccess=_MIfLwModemStatsRxSuccess_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,24),_MIfLwModemStatsRxSuccess_Type())
mIfLwModemStatsRxSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwModemStatsRxSuccess.setStatus(_A)
_MIfLwModemStatsRxError_Type=Unsigned32
_MIfLwModemStatsRxError_Object=MibTableColumn
mIfLwModemStatsRxError=_MIfLwModemStatsRxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,25),_MIfLwModemStatsRxError_Type())
mIfLwModemStatsRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwModemStatsRxError.setStatus(_A)
_MIfLwLastRssi_Type=Integer32
_MIfLwLastRssi_Object=MibTableColumn
mIfLwLastRssi=_MIfLwLastRssi_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,26),_MIfLwLastRssi_Type())
mIfLwLastRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwLastRssi.setStatus(_A)
_MIfLwLastSnr_Type=Unsigned32
_MIfLwLastSnr_Object=MibTableColumn
mIfLwLastSnr=_MIfLwLastSnr_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,27),_MIfLwLastSnr_Type())
mIfLwLastSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwLastSnr.setStatus(_A)
_MIfLwLastMod_Type=ModulationModeType
_MIfLwLastMod_Object=MibTableColumn
mIfLwLastMod=_MIfLwLastMod_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,28),_MIfLwLastMod_Type())
mIfLwLastMod.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwLastMod.setStatus(_A)
_MIfLwLastRate_Type=RateType
_MIfLwLastRate_Object=MibTableColumn
mIfLwLastRate=_MIfLwLastRate_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,29),_MIfLwLastRate_Type())
mIfLwLastRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwLastRate.setStatus(_A)
_MIfLwActiveNic_Type=TruthValue
_MIfLwActiveNic_Object=MibTableColumn
mIfLwActiveNic=_MIfLwActiveNic_Object((1,3,6,1,4,1,4130,10,2,6,1,2,1,1,30),_MIfLwActiveNic_Type())
mIfLwActiveNic.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwActiveNic.setStatus(_A)
_MIfLwStatusConnRemTable_Object=MibTable
mIfLwStatusConnRemTable=_MIfLwStatusConnRemTable_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2))
if mibBuilder.loadTexts:mIfLwStatusConnRemTable.setStatus(_A)
_MIfLwStatusConnRemEntry_Object=MibTableRow
mIfLwStatusConnRemEntry=_MIfLwStatusConnRemEntry_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1))
mIfLwStatusConnRemEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:mIfLwStatusConnRemEntry.setStatus(_A)
_MIfLwStatusConnRemAddress_Type=MacAddress
_MIfLwStatusConnRemAddress_Object=MibTableColumn
mIfLwStatusConnRemAddress=_MIfLwStatusConnRemAddress_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,1),_MIfLwStatusConnRemAddress_Type())
mIfLwStatusConnRemAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemAddress.setStatus(_A)
_MIfLwStatusConnRemIpAddress_Type=InetIpAddress
_MIfLwStatusConnRemIpAddress_Object=MibTableColumn
mIfLwStatusConnRemIpAddress=_MIfLwStatusConnRemIpAddress_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,2),_MIfLwStatusConnRemIpAddress_Type())
mIfLwStatusConnRemIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemIpAddress.setStatus(_A)
_MIfLwStatusConnRemTimeToLive_Type=Unsigned32
_MIfLwStatusConnRemTimeToLive_Object=MibTableColumn
mIfLwStatusConnRemTimeToLive=_MIfLwStatusConnRemTimeToLive_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,3),_MIfLwStatusConnRemTimeToLive_Type())
mIfLwStatusConnRemTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemTimeToLive.setStatus(_A)
_MIfLwStatusConnRemLinkStatus_Type=LinkStatus
_MIfLwStatusConnRemLinkStatus_Object=MibTableColumn
mIfLwStatusConnRemLinkStatus=_MIfLwStatusConnRemLinkStatus_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,4),_MIfLwStatusConnRemLinkStatus_Type())
mIfLwStatusConnRemLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemLinkStatus.setStatus(_A)
_MIfLwStatusConnRemNicId_Type=UnsignedShort
_MIfLwStatusConnRemNicId_Object=MibTableColumn
mIfLwStatusConnRemNicId=_MIfLwStatusConnRemNicId_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,5),_MIfLwStatusConnRemNicId_Type())
mIfLwStatusConnRemNicId.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemNicId.setStatus(_A)
_MIfLwStatusConnRemRssi_Type=Integer32
_MIfLwStatusConnRemRssi_Object=MibTableColumn
mIfLwStatusConnRemRssi=_MIfLwStatusConnRemRssi_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,6),_MIfLwStatusConnRemRssi_Type())
mIfLwStatusConnRemRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemRssi.setStatus(_A)
_MIfLwStatusConnRemSnr_Type=Unsigned32
_MIfLwStatusConnRemSnr_Object=MibTableColumn
mIfLwStatusConnRemSnr=_MIfLwStatusConnRemSnr_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,7),_MIfLwStatusConnRemSnr_Type())
mIfLwStatusConnRemSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemSnr.setStatus(_A)
_MIfLwStatusConnRemMod_Type=ModulationModeType
_MIfLwStatusConnRemMod_Object=MibTableColumn
mIfLwStatusConnRemMod=_MIfLwStatusConnRemMod_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,8),_MIfLwStatusConnRemMod_Type())
mIfLwStatusConnRemMod.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemMod.setStatus(_A)
_MIfLwStatusConnRemStatsTxPackets_Type=Unsigned32
_MIfLwStatusConnRemStatsTxPackets_Object=MibTableColumn
mIfLwStatusConnRemStatsTxPackets=_MIfLwStatusConnRemStatsTxPackets_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,9),_MIfLwStatusConnRemStatsTxPackets_Type())
mIfLwStatusConnRemStatsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsTxPackets.setStatus(_A)
_MIfLwStatusConnRemStatsTxBytes_Type=Unsigned32
_MIfLwStatusConnRemStatsTxBytes_Object=MibTableColumn
mIfLwStatusConnRemStatsTxBytes=_MIfLwStatusConnRemStatsTxBytes_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,10),_MIfLwStatusConnRemStatsTxBytes_Type())
mIfLwStatusConnRemStatsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsTxBytes.setStatus(_A)
_MIfLwStatusConnRemStatsRxPackets_Type=Unsigned32
_MIfLwStatusConnRemStatsRxPackets_Object=MibTableColumn
mIfLwStatusConnRemStatsRxPackets=_MIfLwStatusConnRemStatsRxPackets_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,11),_MIfLwStatusConnRemStatsRxPackets_Type())
mIfLwStatusConnRemStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsRxPackets.setStatus(_A)
_MIfLwStatusConnRemStatsRxBytes_Type=Unsigned32
_MIfLwStatusConnRemStatsRxBytes_Object=MibTableColumn
mIfLwStatusConnRemStatsRxBytes=_MIfLwStatusConnRemStatsRxBytes_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,12),_MIfLwStatusConnRemStatsRxBytes_Type())
mIfLwStatusConnRemStatsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsRxBytes.setStatus(_A)
_MIfLwStatusConnRemStatsTxError_Type=Unsigned32
_MIfLwStatusConnRemStatsTxError_Object=MibTableColumn
mIfLwStatusConnRemStatsTxError=_MIfLwStatusConnRemStatsTxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,13),_MIfLwStatusConnRemStatsTxError_Type())
mIfLwStatusConnRemStatsTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsTxError.setStatus(_A)
_MIfLwStatusConnRemStatsRxError_Type=Unsigned32
_MIfLwStatusConnRemStatsRxError_Object=MibTableColumn
mIfLwStatusConnRemStatsRxError=_MIfLwStatusConnRemStatsRxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,14),_MIfLwStatusConnRemStatsRxError_Type())
mIfLwStatusConnRemStatsRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsRxError.setStatus(_A)
_MIfLwStatusConnRemStatsTxDrop_Type=Unsigned32
_MIfLwStatusConnRemStatsTxDrop_Object=MibTableColumn
mIfLwStatusConnRemStatsTxDrop=_MIfLwStatusConnRemStatsTxDrop_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,15),_MIfLwStatusConnRemStatsTxDrop_Type())
mIfLwStatusConnRemStatsTxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsTxDrop.setStatus(_A)
_MIfLwStatusConnRemStatsRxDrop_Type=Unsigned32
_MIfLwStatusConnRemStatsRxDrop_Object=MibTableColumn
mIfLwStatusConnRemStatsRxDrop=_MIfLwStatusConnRemStatsRxDrop_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,16),_MIfLwStatusConnRemStatsRxDrop_Type())
mIfLwStatusConnRemStatsRxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsRxDrop.setStatus(_A)
_MIfLwStatusConnRemStatsGateway_Type=MacAddress
_MIfLwStatusConnRemStatsGateway_Object=MibTableColumn
mIfLwStatusConnRemStatsGateway=_MIfLwStatusConnRemStatsGateway_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,17),_MIfLwStatusConnRemStatsGateway_Type())
mIfLwStatusConnRemStatsGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsGateway.setStatus(_A)
_MIfLwStatusConnRemStatsAllIp_Type=OctetString
_MIfLwStatusConnRemStatsAllIp_Object=MibTableColumn
mIfLwStatusConnRemStatsAllIp=_MIfLwStatusConnRemStatsAllIp_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,18),_MIfLwStatusConnRemStatsAllIp_Type())
mIfLwStatusConnRemStatsAllIp.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsAllIp.setStatus(_A)
_MIfLwStatusConnRemStatsName_Type=OctetString
_MIfLwStatusConnRemStatsName_Object=MibTableColumn
mIfLwStatusConnRemStatsName=_MIfLwStatusConnRemStatsName_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,19),_MIfLwStatusConnRemStatsName_Type())
mIfLwStatusConnRemStatsName.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsName.setStatus(_A)
_MIfLwStatusConnRemStatsAlarmed_Type=TruthValue
_MIfLwStatusConnRemStatsAlarmed_Object=MibTableColumn
mIfLwStatusConnRemStatsAlarmed=_MIfLwStatusConnRemStatsAlarmed_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,20),_MIfLwStatusConnRemStatsAlarmed_Type())
mIfLwStatusConnRemStatsAlarmed.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsAlarmed.setStatus(_A)
_MIfLwStatusConnRemStatsVersion_Type=OctetString
_MIfLwStatusConnRemStatsVersion_Object=MibTableColumn
mIfLwStatusConnRemStatsVersion=_MIfLwStatusConnRemStatsVersion_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,21),_MIfLwStatusConnRemStatsVersion_Type())
mIfLwStatusConnRemStatsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsVersion.setStatus(_A)
class _MIfLwStatusConnRemStatsTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_MIfLwStatusConnRemStatsTemp_Type.__name__=_H
_MIfLwStatusConnRemStatsTemp_Object=MibTableColumn
mIfLwStatusConnRemStatsTemp=_MIfLwStatusConnRemStatsTemp_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,22),_MIfLwStatusConnRemStatsTemp_Type())
mIfLwStatusConnRemStatsTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsTemp.setStatus(_A)
_MIfLwStatusConnRemStatsDwnRssi_Type=Integer32
_MIfLwStatusConnRemStatsDwnRssi_Object=MibTableColumn
mIfLwStatusConnRemStatsDwnRssi=_MIfLwStatusConnRemStatsDwnRssi_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,23),_MIfLwStatusConnRemStatsDwnRssi_Type())
mIfLwStatusConnRemStatsDwnRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsDwnRssi.setStatus(_A)
_MIfLwStatusConnRemStatsDwnSnr_Type=Unsigned32
_MIfLwStatusConnRemStatsDwnSnr_Object=MibTableColumn
mIfLwStatusConnRemStatsDwnSnr=_MIfLwStatusConnRemStatsDwnSnr_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,24),_MIfLwStatusConnRemStatsDwnSnr_Type())
mIfLwStatusConnRemStatsDwnSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsDwnSnr.setStatus(_A)
_MIfLwStatusConnRemStatsDwnMod_Type=ModulationModeType
_MIfLwStatusConnRemStatsDwnMod_Object=MibTableColumn
mIfLwStatusConnRemStatsDwnMod=_MIfLwStatusConnRemStatsDwnMod_Object((1,3,6,1,4,1,4130,10,2,6,1,2,2,1,25),_MIfLwStatusConnRemStatsDwnMod_Type())
mIfLwStatusConnRemStatsDwnMod.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusConnRemStatsDwnMod.setStatus(_A)
_MIfLwStatusEndpointTable_Object=MibTable
mIfLwStatusEndpointTable=_MIfLwStatusEndpointTable_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3))
if mibBuilder.loadTexts:mIfLwStatusEndpointTable.setStatus(_A)
_MIfLwStatusEndpointEntry_Object=MibTableRow
mIfLwStatusEndpointEntry=_MIfLwStatusEndpointEntry_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1))
mIfLwStatusEndpointEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:mIfLwStatusEndpointEntry.setStatus(_A)
_MIfLwStatusEndpointAddress_Type=MacAddress
_MIfLwStatusEndpointAddress_Object=MibTableColumn
mIfLwStatusEndpointAddress=_MIfLwStatusEndpointAddress_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,1),_MIfLwStatusEndpointAddress_Type())
mIfLwStatusEndpointAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointAddress.setStatus(_A)
_MIfLwStatusEndpointIpAddress_Type=InetIpAddress
_MIfLwStatusEndpointIpAddress_Object=MibTableColumn
mIfLwStatusEndpointIpAddress=_MIfLwStatusEndpointIpAddress_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,2),_MIfLwStatusEndpointIpAddress_Type())
mIfLwStatusEndpointIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointIpAddress.setStatus(_A)
_MIfLwStatusEndpointTimeToLive_Type=Unsigned32
_MIfLwStatusEndpointTimeToLive_Object=MibTableColumn
mIfLwStatusEndpointTimeToLive=_MIfLwStatusEndpointTimeToLive_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,3),_MIfLwStatusEndpointTimeToLive_Type())
mIfLwStatusEndpointTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointTimeToLive.setStatus(_A)
_MIfLwStatusEndpointRemAddress_Type=MacAddress
_MIfLwStatusEndpointRemAddress_Object=MibTableColumn
mIfLwStatusEndpointRemAddress=_MIfLwStatusEndpointRemAddress_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,4),_MIfLwStatusEndpointRemAddress_Type())
mIfLwStatusEndpointRemAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointRemAddress.setStatus(_A)
_MIfLwStatusEndpointStatsTxPackets_Type=Unsigned32
_MIfLwStatusEndpointStatsTxPackets_Object=MibTableColumn
mIfLwStatusEndpointStatsTxPackets=_MIfLwStatusEndpointStatsTxPackets_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,5),_MIfLwStatusEndpointStatsTxPackets_Type())
mIfLwStatusEndpointStatsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsTxPackets.setStatus(_A)
_MIfLwStatusEndpointStatsTxBytes_Type=Unsigned32
_MIfLwStatusEndpointStatsTxBytes_Object=MibTableColumn
mIfLwStatusEndpointStatsTxBytes=_MIfLwStatusEndpointStatsTxBytes_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,6),_MIfLwStatusEndpointStatsTxBytes_Type())
mIfLwStatusEndpointStatsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsTxBytes.setStatus(_A)
_MIfLwStatusEndpointStatsRxPackets_Type=Unsigned32
_MIfLwStatusEndpointStatsRxPackets_Object=MibTableColumn
mIfLwStatusEndpointStatsRxPackets=_MIfLwStatusEndpointStatsRxPackets_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,7),_MIfLwStatusEndpointStatsRxPackets_Type())
mIfLwStatusEndpointStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsRxPackets.setStatus(_A)
_MIfLwStatusEndpointStatsRxBytes_Type=Unsigned32
_MIfLwStatusEndpointStatsRxBytes_Object=MibTableColumn
mIfLwStatusEndpointStatsRxBytes=_MIfLwStatusEndpointStatsRxBytes_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,8),_MIfLwStatusEndpointStatsRxBytes_Type())
mIfLwStatusEndpointStatsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsRxBytes.setStatus(_A)
_MIfLwStatusEndpointStatsTxError_Type=Unsigned32
_MIfLwStatusEndpointStatsTxError_Object=MibTableColumn
mIfLwStatusEndpointStatsTxError=_MIfLwStatusEndpointStatsTxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,9),_MIfLwStatusEndpointStatsTxError_Type())
mIfLwStatusEndpointStatsTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsTxError.setStatus(_A)
_MIfLwStatusEndpointStatsRxError_Type=Unsigned32
_MIfLwStatusEndpointStatsRxError_Object=MibTableColumn
mIfLwStatusEndpointStatsRxError=_MIfLwStatusEndpointStatsRxError_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,10),_MIfLwStatusEndpointStatsRxError_Type())
mIfLwStatusEndpointStatsRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsRxError.setStatus(_A)
_MIfLwStatusEndpointStatsTxDrop_Type=Unsigned32
_MIfLwStatusEndpointStatsTxDrop_Object=MibTableColumn
mIfLwStatusEndpointStatsTxDrop=_MIfLwStatusEndpointStatsTxDrop_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,11),_MIfLwStatusEndpointStatsTxDrop_Type())
mIfLwStatusEndpointStatsTxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsTxDrop.setStatus(_A)
_MIfLwStatusEndpointStatsRxDrop_Type=Unsigned32
_MIfLwStatusEndpointStatsRxDrop_Object=MibTableColumn
mIfLwStatusEndpointStatsRxDrop=_MIfLwStatusEndpointStatsRxDrop_Object((1,3,6,1,4,1,4130,10,2,6,1,2,3,1,12),_MIfLwStatusEndpointStatsRxDrop_Type())
mIfLwStatusEndpointStatsRxDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfLwStatusEndpointStatsRxDrop.setStatus(_A)
_MdsIfLwMIBConformance_ObjectIdentity=ObjectIdentity
mdsIfLwMIBConformance=_MdsIfLwMIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,2,6,3))
_MdsIfLwMIBCompliances_ObjectIdentity=ObjectIdentity
mdsIfLwMIBCompliances=_MdsIfLwMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,2,6,3,1))
_MdsIfLwMIBGroups_ObjectIdentity=ObjectIdentity
mdsIfLwMIBGroups=_MdsIfLwMIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,2,6,3,2))
mIfLwStatusGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,6,3,2,1))
mIfLwStatusGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:mIfLwStatusGroup.setStatus(_A)
mIfLwStatusConnRemGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,6,3,2,2))
mIfLwStatusConnRemGroup.setObjects(*((_B,_F),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:mIfLwStatusConnRemGroup.setStatus(_A)
mIfLwStatusEndpointGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,6,3,2,3))
mIfLwStatusEndpointGroup.setObjects(*((_B,_G),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:mIfLwStatusEndpointGroup.setStatus(_A)
mIfLwCompliance=ModuleCompliance((1,3,6,1,4,1,4130,10,2,6,3,1,1))
mIfLwCompliance.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:mIfLwCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'UnsignedByte':UnsignedByte,'UnsignedShort':UnsignedShort,'LinkStatus':LinkStatus,'InitStatus':InitStatus,'DeviceModeType':DeviceModeType,'ModulationModeType':ModulationModeType,'AlarmFlags':AlarmFlags,'FirmwareRevision':FirmwareRevision,'InetIpAddress':InetIpAddress,'FrequencyType':FrequencyType,'ChannelType':ChannelType,'FecType':FecType,'RateType':RateType,'mdsIfLwMIB':mdsIfLwMIB,'mIfLwMIBObjects':mIfLwMIBObjects,'mIfLwConfig':mIfLwConfig,'mIfLwStatus':mIfLwStatus,'mIfLwStatusTable':mIfLwStatusTable,'mIfLwStatusEntry':mIfLwStatusEntry,_J:mIfLwLinkStatus,_K:mIfLwInitStatus,_L:mIfLwCurrentDeviceMode,_M:mIfLwAlarms,_N:mIfLwSerialNumber,_O:mIfLwFirmwareRevision,_P:mIfLwHardwareId,_Q:mIfLwHardwareRevision,_R:mIfLwTemperature,_S:mIfLwApInfoApAddress,_T:mIfLwApInfoIpAddress,_U:mIfLwApInfoConnectedTime,_V:mIfLwApInfoRssi,_W:mIfLwApInfoSnr,_X:mIfLwApInfoMod,_Y:mIfLwMacStatsTxSuccess,_Z:mIfLwMacStatsTxQueueFull,_a:mIfLwMacStatsTxError,_b:mIfLwMacStatsTxRetry,_c:mIfLwMacStatsRxSuccess,_d:mIfLwMacStatsRxError,_e:mIfLwModemStatsTxSuccess,_f:mIfLwModemStatsTxError,_g:mIfLwModemStatsRxSuccess,_h:mIfLwModemStatsRxError,_i:mIfLwLastRssi,_j:mIfLwLastSnr,_k:mIfLwLastMod,_l:mIfLwLastRate,_m:mIfLwActiveNic,'mIfLwStatusConnRemTable':mIfLwStatusConnRemTable,'mIfLwStatusConnRemEntry':mIfLwStatusConnRemEntry,_F:mIfLwStatusConnRemAddress,_n:mIfLwStatusConnRemIpAddress,_o:mIfLwStatusConnRemTimeToLive,_p:mIfLwStatusConnRemLinkStatus,_q:mIfLwStatusConnRemNicId,_r:mIfLwStatusConnRemRssi,_s:mIfLwStatusConnRemSnr,_t:mIfLwStatusConnRemMod,_u:mIfLwStatusConnRemStatsTxPackets,_v:mIfLwStatusConnRemStatsTxBytes,_w:mIfLwStatusConnRemStatsRxPackets,_x:mIfLwStatusConnRemStatsRxBytes,_y:mIfLwStatusConnRemStatsTxError,_z:mIfLwStatusConnRemStatsRxError,_A0:mIfLwStatusConnRemStatsTxDrop,_A1:mIfLwStatusConnRemStatsRxDrop,_A2:mIfLwStatusConnRemStatsGateway,_A3:mIfLwStatusConnRemStatsAllIp,_A4:mIfLwStatusConnRemStatsName,_A5:mIfLwStatusConnRemStatsAlarmed,_A6:mIfLwStatusConnRemStatsVersion,_A7:mIfLwStatusConnRemStatsTemp,_A8:mIfLwStatusConnRemStatsDwnRssi,_A9:mIfLwStatusConnRemStatsDwnSnr,_AA:mIfLwStatusConnRemStatsDwnMod,'mIfLwStatusEndpointTable':mIfLwStatusEndpointTable,'mIfLwStatusEndpointEntry':mIfLwStatusEndpointEntry,_G:mIfLwStatusEndpointAddress,_AB:mIfLwStatusEndpointIpAddress,_AC:mIfLwStatusEndpointTimeToLive,_AD:mIfLwStatusEndpointRemAddress,_AE:mIfLwStatusEndpointStatsTxPackets,_AF:mIfLwStatusEndpointStatsTxBytes,_AG:mIfLwStatusEndpointStatsRxPackets,_AH:mIfLwStatusEndpointStatsRxBytes,_AI:mIfLwStatusEndpointStatsTxError,_AJ:mIfLwStatusEndpointStatsRxError,_AK:mIfLwStatusEndpointStatsTxDrop,_AL:mIfLwStatusEndpointStatsRxDrop,'mdsIfLwMIBConformance':mdsIfLwMIBConformance,'mdsIfLwMIBCompliances':mdsIfLwMIBCompliances,'mIfLwCompliance':mIfLwCompliance,'mdsIfLwMIBGroups':mdsIfLwMIBGroups,_AM:mIfLwStatusGroup,_AN:mIfLwStatusConnRemGroup,_AO:mIfLwStatusEndpointGroup})