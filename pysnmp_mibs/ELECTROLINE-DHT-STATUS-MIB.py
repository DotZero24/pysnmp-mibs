_O='dhtTrapAckValue'
_N='dhtFnOpticalReceiverIndex'
_M='dhtTrapAckAddressIndex'
_L='DisplayString'
_K='Integer32'
_J='cfgSleepVoltage'
_I='ELECTROLINE-DHT-CONFIG-MIB'
_H='mandatory'
_G='commonPhysAddress'
_F='commonLogicalID'
_E='ELECTROLINE-DHT-STATUS-MIB'
_D='SCTE-HMS-COMMON-MIB'
_C='deprecated'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cfgSleepVoltage,=mibBuilder.importSymbols(_I,_J)
dhtStatus,electrolineDHT=mibBuilder.importSymbols('ELECTROLINE-DHT-ROOT-MIB','dhtStatus','electrolineDHT')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
commonLogicalID,commonPhysAddress=mibBuilder.importSymbols(_D,_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention')
class TenthdBmV(TextualConvention,Integer32):status=_B;displayHint='d-1'
class TenthdB(TextualConvention,Integer32):status=_B;displayHint='d-1'
class HundredthsVolts(TextualConvention,Integer32):status=_B;displayHint='d-2';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DhtTrapAcknowledgeStatusTable_Object=MibTable
dhtTrapAcknowledgeStatusTable=_DhtTrapAcknowledgeStatusTable_Object((1,3,6,1,4,1,5802,1,3,1,2,3,1))
if mibBuilder.loadTexts:dhtTrapAcknowledgeStatusTable.setStatus(_B)
_DhtTrapAcknowledgeStatusEntry_Object=MibTableRow
dhtTrapAcknowledgeStatusEntry=_DhtTrapAcknowledgeStatusEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,3,1,1))
dhtTrapAcknowledgeStatusEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:dhtTrapAcknowledgeStatusEntry.setStatus(_B)
_DhtTrapAckAddressIndex_Type=Integer32
_DhtTrapAckAddressIndex_Object=MibTableColumn
dhtTrapAckAddressIndex=_DhtTrapAckAddressIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,3,1,1,1),_DhtTrapAckAddressIndex_Type())
dhtTrapAckAddressIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtTrapAckAddressIndex.setStatus(_B)
_DhtTrapAckValue_Type=Integer32
_DhtTrapAckValue_Object=MibTableColumn
dhtTrapAckValue=_DhtTrapAckValue_Object((1,3,6,1,4,1,5802,1,3,1,2,3,1,1,2),_DhtTrapAckValue_Type())
dhtTrapAckValue.setMaxAccess('read-write')
if mibBuilder.loadTexts:dhtTrapAckValue.setStatus(_B)
_DhtNetworkAddress_Type=IpAddress
_DhtNetworkAddress_Object=MibScalar
dhtNetworkAddress=_DhtNetworkAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,3,2),_DhtNetworkAddress_Type())
dhtNetworkAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtNetworkAddress.setStatus(_C)
_DhtHmsStatus_ObjectIdentity=ObjectIdentity
dhtHmsStatus=_DhtHmsStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,3,3))
_DhtHmsTibStatusInfo_ObjectIdentity=ObjectIdentity
dhtHmsTibStatusInfo=_DhtHmsTibStatusInfo_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,3,3,1))
_DhtHmsTibLineStatus_ObjectIdentity=ObjectIdentity
dhtHmsTibLineStatus=_DhtHmsTibLineStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,3,3,1,1))
_DhtHmsTibLineRxBytes_Type=Integer32
_DhtHmsTibLineRxBytes_Object=MibScalar
dhtHmsTibLineRxBytes=_DhtHmsTibLineRxBytes_Object((1,3,6,1,4,1,5802,1,3,1,2,3,3,1,1,1),_DhtHmsTibLineRxBytes_Type())
dhtHmsTibLineRxBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtHmsTibLineRxBytes.setStatus(_B)
_DhtHmsTibLineTxBytes_Type=Integer32
_DhtHmsTibLineTxBytes_Object=MibScalar
dhtHmsTibLineTxBytes=_DhtHmsTibLineTxBytes_Object((1,3,6,1,4,1,5802,1,3,1,2,3,3,1,1,2),_DhtHmsTibLineTxBytes_Type())
dhtHmsTibLineTxBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtHmsTibLineTxBytes.setStatus(_B)
_DhtHmsTibLineTxFifoError_Type=Integer32
_DhtHmsTibLineTxFifoError_Object=MibScalar
dhtHmsTibLineTxFifoError=_DhtHmsTibLineTxFifoError_Object((1,3,6,1,4,1,5802,1,3,1,2,3,3,1,1,3),_DhtHmsTibLineTxFifoError_Type())
dhtHmsTibLineTxFifoError.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtHmsTibLineTxFifoError.setStatus(_B)
_DhtHmsTibLineRxFifoError_Type=Integer32
_DhtHmsTibLineRxFifoError_Object=MibScalar
dhtHmsTibLineRxFifoError=_DhtHmsTibLineRxFifoError_Object((1,3,6,1,4,1,5802,1,3,1,2,3,3,1,1,4),_DhtHmsTibLineRxFifoError_Type())
dhtHmsTibLineRxFifoError.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtHmsTibLineRxFifoError.setStatus(_B)
_DhtHmsTibLineRxLineError_Type=Integer32
_DhtHmsTibLineRxLineError_Object=MibScalar
dhtHmsTibLineRxLineError=_DhtHmsTibLineRxLineError_Object((1,3,6,1,4,1,5802,1,3,1,2,3,3,1,1,5),_DhtHmsTibLineRxLineError_Type())
dhtHmsTibLineRxLineError.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtHmsTibLineRxLineError.setStatus(_B)
_DhtMonitoringNetworkAddress_Type=IpAddress
_DhtMonitoringNetworkAddress_Object=MibScalar
dhtMonitoringNetworkAddress=_DhtMonitoringNetworkAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,3,4),_DhtMonitoringNetworkAddress_Type())
dhtMonitoringNetworkAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtMonitoringNetworkAddress.setStatus(_C)
class _DhtInternalTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,130))
_DhtInternalTemperature_Type.__name__=_K
_DhtInternalTemperature_Object=MibScalar
dhtInternalTemperature=_DhtInternalTemperature_Object((1,3,6,1,4,1,5802,1,3,1,2,3,5),_DhtInternalTemperature_Type())
dhtInternalTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtInternalTemperature.setStatus(_C)
_DhtDlmStatus_ObjectIdentity=ObjectIdentity
dhtDlmStatus=_DhtDlmStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,3,6))
_DlmAcInputVoltage_Type=HundredthsVolts
_DlmAcInputVoltage_Object=MibScalar
dlmAcInputVoltage=_DlmAcInputVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,3,6,1),_DlmAcInputVoltage_Type())
dlmAcInputVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:dlmAcInputVoltage.setStatus(_B)
if mibBuilder.loadTexts:dlmAcInputVoltage.setUnits('Volts')
_DlmDhtInputVoltage_Type=HundredthsVolts
_DlmDhtInputVoltage_Object=MibScalar
dlmDhtInputVoltage=_DlmDhtInputVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,3,6,2),_DlmDhtInputVoltage_Type())
dlmDhtInputVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:dlmDhtInputVoltage.setStatus(_B)
if mibBuilder.loadTexts:dlmDhtInputVoltage.setUnits('Volts')
_DlmRxPowerLevel_Type=TenthdBmV
_DlmRxPowerLevel_Object=MibScalar
dlmRxPowerLevel=_DlmRxPowerLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,3,6,3),_DlmRxPowerLevel_Type())
dlmRxPowerLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:dlmRxPowerLevel.setStatus(_B)
if mibBuilder.loadTexts:dlmRxPowerLevel.setUnits('dBmV')
_DlmTxPowerLevel_Type=TenthdBmV
_DlmTxPowerLevel_Object=MibScalar
dlmTxPowerLevel=_DlmTxPowerLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,3,6,4),_DlmTxPowerLevel_Type())
dlmTxPowerLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:dlmTxPowerLevel.setStatus(_B)
if mibBuilder.loadTexts:dlmTxPowerLevel.setUnits('dBmV')
_DlmRxAttenuatorPad_Type=TenthdB
_DlmRxAttenuatorPad_Object=MibScalar
dlmRxAttenuatorPad=_DlmRxAttenuatorPad_Object((1,3,6,1,4,1,5802,1,3,1,2,3,6,5),_DlmRxAttenuatorPad_Type())
dlmRxAttenuatorPad.setMaxAccess(_A)
if mibBuilder.loadTexts:dlmRxAttenuatorPad.setStatus(_B)
if mibBuilder.loadTexts:dlmRxAttenuatorPad.setUnits('dB')
_DlmTxAttenuatorPad_Type=TenthdB
_DlmTxAttenuatorPad_Object=MibScalar
dlmTxAttenuatorPad=_DlmTxAttenuatorPad_Object((1,3,6,1,4,1,5802,1,3,1,2,3,6,6),_DlmTxAttenuatorPad_Type())
dlmTxAttenuatorPad.setMaxAccess(_A)
if mibBuilder.loadTexts:dlmTxAttenuatorPad.setStatus(_B)
if mibBuilder.loadTexts:dlmTxAttenuatorPad.setUnits('dB')
_FiberNodeStatus_ObjectIdentity=ObjectIdentity
fiberNodeStatus=_FiberNodeStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,3,7))
_DhtFnOpticalReceiverTable_Object=MibTable
dhtFnOpticalReceiverTable=_DhtFnOpticalReceiverTable_Object((1,3,6,1,4,1,5802,1,3,1,2,3,7,1))
if mibBuilder.loadTexts:dhtFnOpticalReceiverTable.setStatus(_H)
_DhtFnOpticalReceiverEntry_Object=MibTableRow
dhtFnOpticalReceiverEntry=_DhtFnOpticalReceiverEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,3,7,1,1))
dhtFnOpticalReceiverEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:dhtFnOpticalReceiverEntry.setStatus(_H)
_DhtFnOpticalReceiverIndex_Type=Integer32
_DhtFnOpticalReceiverIndex_Object=MibTableColumn
dhtFnOpticalReceiverIndex=_DhtFnOpticalReceiverIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,3,7,1,1,1),_DhtFnOpticalReceiverIndex_Type())
dhtFnOpticalReceiverIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtFnOpticalReceiverIndex.setStatus(_H)
class _DhtFnOpticalReceiverType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DhtFnOpticalReceiverType_Type.__name__=_L
_DhtFnOpticalReceiverType_Object=MibTableColumn
dhtFnOpticalReceiverType=_DhtFnOpticalReceiverType_Object((1,3,6,1,4,1,5802,1,3,1,2,3,7,1,1,2),_DhtFnOpticalReceiverType_Type())
dhtFnOpticalReceiverType.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtFnOpticalReceiverType.setStatus('optional')
_DhtInetNetworkAddressType_Type=InetAddressType
_DhtInetNetworkAddressType_Object=MibScalar
dhtInetNetworkAddressType=_DhtInetNetworkAddressType_Object((1,3,6,1,4,1,5802,1,3,1,2,3,8),_DhtInetNetworkAddressType_Type())
dhtInetNetworkAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtInetNetworkAddressType.setStatus(_C)
_DhtInetNetworkAddress_Type=InetAddress
_DhtInetNetworkAddress_Object=MibScalar
dhtInetNetworkAddress=_DhtInetNetworkAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,3,9),_DhtInetNetworkAddress_Type())
dhtInetNetworkAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtInetNetworkAddress.setStatus(_C)
_DhtInetMonitoringNetworkAddressType_Type=InetAddressType
_DhtInetMonitoringNetworkAddressType_Object=MibScalar
dhtInetMonitoringNetworkAddressType=_DhtInetMonitoringNetworkAddressType_Object((1,3,6,1,4,1,5802,1,3,1,2,3,10),_DhtInetMonitoringNetworkAddressType_Type())
dhtInetMonitoringNetworkAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtInetMonitoringNetworkAddressType.setStatus(_C)
_DhtInetMonitoringNetworkAddress_Type=InetAddress
_DhtInetMonitoringNetworkAddress_Object=MibScalar
dhtInetMonitoringNetworkAddress=_DhtInetMonitoringNetworkAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,3,11),_DhtInetMonitoringNetworkAddress_Type())
dhtInetMonitoringNetworkAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:dhtInetMonitoringNetworkAddress.setStatus(_C)
dhtSleepModeEvent=NotificationType((1,3,6,1,4,1,5802,1,3,1,2,0,10))
dhtSleepModeEvent.setObjects(*((_D,_G),(_D,_F),(_I,_J)))
if mibBuilder.loadTexts:dhtSleepModeEvent.setStatus('')
dhtAlarmAssuranceEvent=NotificationType((1,3,6,1,4,1,5802,1,3,1,2,0,11))
dhtAlarmAssuranceEvent.setObjects(*((_D,_G),(_D,_F),(_E,_O)))
if mibBuilder.loadTexts:dhtAlarmAssuranceEvent.setStatus('')
mibBuilder.exportSymbols(_E,**{'TenthdBmV':TenthdBmV,'TenthdB':TenthdB,'HundredthsVolts':HundredthsVolts,'dhtSleepModeEvent':dhtSleepModeEvent,'dhtAlarmAssuranceEvent':dhtAlarmAssuranceEvent,'dhtTrapAcknowledgeStatusTable':dhtTrapAcknowledgeStatusTable,'dhtTrapAcknowledgeStatusEntry':dhtTrapAcknowledgeStatusEntry,_M:dhtTrapAckAddressIndex,_O:dhtTrapAckValue,'dhtNetworkAddress':dhtNetworkAddress,'dhtHmsStatus':dhtHmsStatus,'dhtHmsTibStatusInfo':dhtHmsTibStatusInfo,'dhtHmsTibLineStatus':dhtHmsTibLineStatus,'dhtHmsTibLineRxBytes':dhtHmsTibLineRxBytes,'dhtHmsTibLineTxBytes':dhtHmsTibLineTxBytes,'dhtHmsTibLineTxFifoError':dhtHmsTibLineTxFifoError,'dhtHmsTibLineRxFifoError':dhtHmsTibLineRxFifoError,'dhtHmsTibLineRxLineError':dhtHmsTibLineRxLineError,'dhtMonitoringNetworkAddress':dhtMonitoringNetworkAddress,'dhtInternalTemperature':dhtInternalTemperature,'dhtDlmStatus':dhtDlmStatus,'dlmAcInputVoltage':dlmAcInputVoltage,'dlmDhtInputVoltage':dlmDhtInputVoltage,'dlmRxPowerLevel':dlmRxPowerLevel,'dlmTxPowerLevel':dlmTxPowerLevel,'dlmRxAttenuatorPad':dlmRxAttenuatorPad,'dlmTxAttenuatorPad':dlmTxAttenuatorPad,'fiberNodeStatus':fiberNodeStatus,'dhtFnOpticalReceiverTable':dhtFnOpticalReceiverTable,'dhtFnOpticalReceiverEntry':dhtFnOpticalReceiverEntry,_N:dhtFnOpticalReceiverIndex,'dhtFnOpticalReceiverType':dhtFnOpticalReceiverType,'dhtInetNetworkAddressType':dhtInetNetworkAddressType,'dhtInetNetworkAddress':dhtInetNetworkAddress,'dhtInetMonitoringNetworkAddressType':dhtInetMonitoringNetworkAddressType,'dhtInetMonitoringNetworkAddress':dhtInetMonitoringNetworkAddress})