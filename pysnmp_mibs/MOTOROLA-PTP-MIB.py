_Q='current'
_P='mod-64qam-7-8'
_O='mod-64qam-3-4'
_N='mod-64qam-2-3'
_M='mod-16qam-3-4'
_L='mod-16qam-1-2'
_K='mod-qpsk-2-3'
_J='mod-qpsk-1-2'
_I='mod-bpsk-1-2'
_H='mod-acquisition'
_G='OctetString'
_F='receiveChannel'
_E='MOTOROLA-PTP-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Motorola_ObjectIdentity=ObjectIdentity
motorola=_Motorola_ObjectIdentity((1,3,6,1,4,1,17713))
_Ptp_ObjectIdentity=ObjectIdentity
ptp=_Ptp_ObjectIdentity((1,3,6,1,4,1,17713,1))
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,17713,1,5))
_IPAddress_Type=IpAddress
_IPAddress_Object=MibScalar
iPAddress=_IPAddress_Object((1,3,6,1,4,1,17713,1,5,1),_IPAddress_Type())
iPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:iPAddress.setStatus(_A)
_SubnetMask_Type=IpAddress
_SubnetMask_Object=MibScalar
subnetMask=_SubnetMask_Object((1,3,6,1,4,1,17713,1,5,2),_SubnetMask_Type())
subnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetMask.setStatus(_A)
_GatewayIPAddress_Type=IpAddress
_GatewayIPAddress_Object=MibScalar
gatewayIPAddress=_GatewayIPAddress_Object((1,3,6,1,4,1,17713,1,5,3),_GatewayIPAddress_Type())
gatewayIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayIPAddress.setStatus(_A)
class _TargetMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TargetMACAddress_Type.__name__=_G
_TargetMACAddress_Object=MibScalar
targetMACAddress=_TargetMACAddress_Object((1,3,6,1,4,1,17713,1,5,4),_TargetMACAddress_Type())
targetMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:targetMACAddress.setStatus(_A)
class _MasterSlaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('master',0),('slave',1)))
_MasterSlaveMode_Type.__name__=_C
_MasterSlaveMode_Object=MibScalar
masterSlaveMode=_MasterSlaveMode_Object((1,3,6,1,4,1,17713,1,5,5),_MasterSlaveMode_Type())
masterSlaveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:masterSlaveMode.setStatus(_A)
class _MaximumTransmitPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,25))
_MaximumTransmitPower_Type.__name__=_C
_MaximumTransmitPower_Object=MibScalar
maximumTransmitPower=_MaximumTransmitPower_Object((1,3,6,1,4,1,17713,1,5,6),_MaximumTransmitPower_Type())
maximumTransmitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:maximumTransmitPower.setStatus(_A)
_Licence_ObjectIdentity=ObjectIdentity
licence=_Licence_ObjectIdentity((1,3,6,1,4,1,17713,1,8))
class _RegionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_RegionCode_Type.__name__=_C
_RegionCode_Object=MibScalar
regionCode=_RegionCode_Object((1,3,6,1,4,1,17713,1,8,1),_RegionCode_Type())
regionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:regionCode.setStatus(_A)
class _ProductVariant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('motorola-ptp-xx400-full',2),('motorola-ptp-xx400-lite',3),('spare-1',4),('spare-2',5),('spare-3',6),('spare-4',7),('spare-5',8),('spare-6',9),('spare-7',10),('motorola-ptp-xx600-lite',11),('motorola-ptp-xx600-full',12)))
_ProductVariant_Type.__name__=_C
_ProductVariant_Object=MibScalar
productVariant=_ProductVariant_Object((1,3,6,1,4,1,17713,1,8,2),_ProductVariant_Type())
productVariant.setMaxAccess(_B)
if mibBuilder.loadTexts:productVariant.setStatus(_A)
class _ProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProductName_Type.__name__=_D
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,17713,1,8,3),_ProductName_Type())
productName.setMaxAccess(_B)
if mibBuilder.loadTexts:productName.setStatus(_A)
class _EthernetFibreSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_EthernetFibreSupport_Type.__name__=_C
_EthernetFibreSupport_Object=MibScalar
ethernetFibreSupport=_EthernetFibreSupport_Object((1,3,6,1,4,1,17713,1,8,4),_EthernetFibreSupport_Type())
ethernetFibreSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetFibreSupport.setStatus(_A)
class _FrequencyVariant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('freq-5800-mhz',0),('freq-5400-mhz',1),('freq-4900-mhz',2)))
_FrequencyVariant_Type.__name__=_C
_FrequencyVariant_Object=MibScalar
frequencyVariant=_FrequencyVariant_Object((1,3,6,1,4,1,17713,1,8,5),_FrequencyVariant_Type())
frequencyVariant.setMaxAccess(_B)
if mibBuilder.loadTexts:frequencyVariant.setStatus(_A)
_Mgmt_ObjectIdentity=ObjectIdentity
mgmt=_Mgmt_ObjectIdentity((1,3,6,1,4,1,17713,1,9))
class _TargetRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_TargetRange_Type.__name__=_C
_TargetRange_Object=MibScalar
targetRange=_TargetRange_Object((1,3,6,1,4,1,17713,1,9,1),_TargetRange_Type())
targetRange.setMaxAccess(_B)
if mibBuilder.loadTexts:targetRange.setStatus(_A)
class _RangingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('auto-0-5-km',0),('auto-0-40-km',1),('auto-0-100-km',2),('auto-0-200-km',3),('target-range',4)))
_RangingMode_Type.__name__=_C
_RangingMode_Object=MibScalar
rangingMode=_RangingMode_Object((1,3,6,1,4,1,17713,1,9,2),_RangingMode_Type())
rangingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rangingMode.setStatus(_A)
_PhyControl_ObjectIdentity=ObjectIdentity
phyControl=_PhyControl_ObjectIdentity((1,3,6,1,4,1,17713,1,10))
class _AsymmetricTDD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('symmetric-data-rate-1-to-1',0),('asymmetric-data-rate-2-to-1',1),('prohibited',2),('latency-optimised',3)))
_AsymmetricTDD_Type.__name__=_C
_AsymmetricTDD_Object=MibScalar
asymmetricTDD=_AsymmetricTDD_Object((1,3,6,1,4,1,17713,1,10,1),_AsymmetricTDD_Type())
asymmetricTDD.setMaxAccess(_B)
if mibBuilder.loadTexts:asymmetricTDD.setStatus(_A)
_PhyStatus_ObjectIdentity=ObjectIdentity
phyStatus=_PhyStatus_ObjectIdentity((1,3,6,1,4,1,17713,1,12))
_ReceivePower_Type=Integer32
_ReceivePower_Object=MibScalar
receivePower=_ReceivePower_Object((1,3,6,1,4,1,17713,1,12,1),_ReceivePower_Type())
receivePower.setMaxAccess(_B)
if mibBuilder.loadTexts:receivePower.setStatus(_A)
_VectorError_Type=Integer32
_VectorError_Object=MibScalar
vectorError=_VectorError_Object((1,3,6,1,4,1,17713,1,12,2),_VectorError_Type())
vectorError.setMaxAccess(_B)
if mibBuilder.loadTexts:vectorError.setStatus(_A)
_TransmitPower_Type=Integer32
_TransmitPower_Object=MibScalar
transmitPower=_TransmitPower_Object((1,3,6,1,4,1,17713,1,12,3),_TransmitPower_Type())
transmitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:transmitPower.setStatus(_A)
_Range_Type=Integer32
_Range_Object=MibScalar
range=_Range_Object((1,3,6,1,4,1,17713,1,12,4),_Range_Type())
range.setMaxAccess(_B)
if mibBuilder.loadTexts:range.setStatus(_A)
class _LinkLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_LinkLoss_Type.__name__=_C
_LinkLoss_Object=MibScalar
linkLoss=_LinkLoss_Object((1,3,6,1,4,1,17713,1,12,5),_LinkLoss_Type())
linkLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:linkLoss.setStatus(_A)
class _ReceiveChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21))
_ReceiveChannel_Type.__name__=_C
_ReceiveChannel_Object=MibScalar
receiveChannel=_ReceiveChannel_Object((1,3,6,1,4,1,17713,1,12,6),_ReceiveChannel_Type())
receiveChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:receiveChannel.setStatus(_A)
class _TransmitChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21))
_TransmitChannel_Type.__name__=_C
_TransmitChannel_Object=MibScalar
transmitChannel=_TransmitChannel_Object((1,3,6,1,4,1,17713,1,12,7),_TransmitChannel_Type())
transmitChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:transmitChannel.setStatus(_A)
class _ReceiveModulationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8)))
_ReceiveModulationMode_Type.__name__=_C
_ReceiveModulationMode_Object=MibScalar
receiveModulationMode=_ReceiveModulationMode_Object((1,3,6,1,4,1,17713,1,12,8),_ReceiveModulationMode_Type())
receiveModulationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:receiveModulationMode.setStatus(_A)
class _TransmitModulationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8)))
_TransmitModulationMode_Type.__name__=_C
_TransmitModulationMode_Object=MibScalar
transmitModulationMode=_TransmitModulationMode_Object((1,3,6,1,4,1,17713,1,12,9),_TransmitModulationMode_Type())
transmitModulationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:transmitModulationMode.setStatus(_A)
class _ReceiveFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5875))
_ReceiveFreq_Type.__name__=_C
_ReceiveFreq_Object=MibScalar
receiveFreq=_ReceiveFreq_Object((1,3,6,1,4,1,17713,1,12,11),_ReceiveFreq_Type())
receiveFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:receiveFreq.setStatus(_A)
class _TransmitFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5875))
_TransmitFreq_Type.__name__=_C
_TransmitFreq_Object=MibScalar
transmitFreq=_TransmitFreq_Object((1,3,6,1,4,1,17713,1,12,12),_TransmitFreq_Type())
transmitFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:transmitFreq.setStatus(_A)
_SignalStrengthRatio_Type=Integer32
_SignalStrengthRatio_Object=MibScalar
signalStrengthRatio=_SignalStrengthRatio_Object((1,3,6,1,4,1,17713,1,12,13),_SignalStrengthRatio_Type())
signalStrengthRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:signalStrengthRatio.setStatus(_A)
_Reset_ObjectIdentity=ObjectIdentity
reset=_Reset_ObjectIdentity((1,3,6,1,4,1,17713,1,18))
class _SystemReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('running',0),('console-reboot',1)))
_SystemReset_Type.__name__=_C
_SystemReset_Object=MibScalar
systemReset=_SystemReset_Object((1,3,6,1,4,1,17713,1,18,1),_SystemReset_Type())
systemReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:systemReset.setStatus(_A)
_Versions_ObjectIdentity=ObjectIdentity
versions=_Versions_ObjectIdentity((1,3,6,1,4,1,17713,1,19))
class _SoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SoftwareVersion_Type.__name__=_D
_SoftwareVersion_Object=MibScalar
softwareVersion=_SoftwareVersion_Object((1,3,6,1,4,1,17713,1,19,1),_SoftwareVersion_Type())
softwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareVersion.setStatus(_A)
class _HardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HardwareVersion_Type.__name__=_D
_HardwareVersion_Object=MibScalar
hardwareVersion=_HardwareVersion_Object((1,3,6,1,4,1,17713,1,19,2),_HardwareVersion_Type())
hardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwareVersion.setStatus(_A)
class _SecondarySoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SecondarySoftwareVersion_Type.__name__=_D
_SecondarySoftwareVersion_Object=MibScalar
secondarySoftwareVersion=_SecondarySoftwareVersion_Object((1,3,6,1,4,1,17713,1,19,3),_SecondarySoftwareVersion_Type())
secondarySoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:secondarySoftwareVersion.setStatus(_A)
class _BootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BootVersion_Type.__name__=_D
_BootVersion_Object=MibScalar
bootVersion=_BootVersion_Object((1,3,6,1,4,1,17713,1,19,4),_BootVersion_Type())
bootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bootVersion.setStatus(_A)
_PubStats_ObjectIdentity=ObjectIdentity
pubStats=_PubStats_ObjectIdentity((1,3,6,1,4,1,17713,1,20))
_ReceiveDataRate_Type=Integer32
_ReceiveDataRate_Object=MibScalar
receiveDataRate=_ReceiveDataRate_Object((1,3,6,1,4,1,17713,1,20,1),_ReceiveDataRate_Type())
receiveDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:receiveDataRate.setStatus(_A)
_TransmitDataRate_Type=Integer32
_TransmitDataRate_Object=MibScalar
transmitDataRate=_TransmitDataRate_Object((1,3,6,1,4,1,17713,1,20,2),_TransmitDataRate_Type())
transmitDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:transmitDataRate.setStatus(_A)
_AggregateDataRate_Type=Integer32
_AggregateDataRate_Object=MibScalar
aggregateDataRate=_AggregateDataRate_Object((1,3,6,1,4,1,17713,1,20,3),_AggregateDataRate_Type())
aggregateDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:aggregateDataRate.setStatus(_A)
_Encryption_ObjectIdentity=ObjectIdentity
encryption=_Encryption_ObjectIdentity((1,3,6,1,4,1,17713,1,22))
class _EncryptionAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('aes-rijndael',1),('aes-256-bit-rijndael',2)))
_EncryptionAlgorithm_Type.__name__=_C
_EncryptionAlgorithm_Object=MibScalar
encryptionAlgorithm=_EncryptionAlgorithm_Object((1,3,6,1,4,1,17713,1,22,1),_EncryptionAlgorithm_Type())
encryptionAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:encryptionAlgorithm.setStatus(_A)
_PtpTraps_ObjectIdentity=ObjectIdentity
ptpTraps=_PtpTraps_ObjectIdentity((1,3,6,1,4,1,17713,1,99))
_Ptmp_ObjectIdentity=ObjectIdentity
ptmp=_Ptmp_ObjectIdentity((1,3,6,1,4,1,17713,2))
dfsChannelChangeTrap=NotificationType((1,3,6,1,4,1,17713,1,99,1))
dfsChannelChangeTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:dfsChannelChangeTrap.setStatus(_Q)
dfsImpulsiveInterferenceDetectedTrap=NotificationType((1,3,6,1,4,1,17713,1,99,2))
dfsImpulsiveInterferenceDetectedTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:dfsImpulsiveInterferenceDetectedTrap.setStatus(_Q)
mibBuilder.exportSymbols(_E,**{'motorola':motorola,'ptp':ptp,'configuration':configuration,'iPAddress':iPAddress,'subnetMask':subnetMask,'gatewayIPAddress':gatewayIPAddress,'targetMACAddress':targetMACAddress,'masterSlaveMode':masterSlaveMode,'maximumTransmitPower':maximumTransmitPower,'licence':licence,'regionCode':regionCode,'productVariant':productVariant,'productName':productName,'ethernetFibreSupport':ethernetFibreSupport,'frequencyVariant':frequencyVariant,'mgmt':mgmt,'targetRange':targetRange,'rangingMode':rangingMode,'phyControl':phyControl,'asymmetricTDD':asymmetricTDD,'phyStatus':phyStatus,'receivePower':receivePower,'vectorError':vectorError,'transmitPower':transmitPower,'range':range,'linkLoss':linkLoss,_F:receiveChannel,'transmitChannel':transmitChannel,'receiveModulationMode':receiveModulationMode,'transmitModulationMode':transmitModulationMode,'receiveFreq':receiveFreq,'transmitFreq':transmitFreq,'signalStrengthRatio':signalStrengthRatio,'reset':reset,'systemReset':systemReset,'versions':versions,'softwareVersion':softwareVersion,'hardwareVersion':hardwareVersion,'secondarySoftwareVersion':secondarySoftwareVersion,'bootVersion':bootVersion,'pubStats':pubStats,'receiveDataRate':receiveDataRate,'transmitDataRate':transmitDataRate,'aggregateDataRate':aggregateDataRate,'encryption':encryption,'encryptionAlgorithm':encryptionAlgorithm,'ptpTraps':ptpTraps,'dfsChannelChangeTrap':dfsChannelChangeTrap,'dfsImpulsiveInterferenceDetectedTrap':dfsImpulsiveInterferenceDetectedTrap,'ptmp':ptmp})