_R='wwpVoiceGatewaySipTimerLineId'
_Q='wwpVoiceGatewaySipLineId'
_P='wwpVoiceGatewayEndPointId'
_O='DisplayString'
_N='Unsigned32'
_M='disable'
_L='enable'
_K='seconds'
_J='read-create'
_I='none'
_H='WWP-VOICE-GATEWAY-MIB'
_G='TruthValue'
_F='milliseconds'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention',_G)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpVoiceGatewayMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,43))
if mibBuilder.loadTexts:wwpVoiceGatewayMIB.setRevisions(('2002-11-18 17:00',))
_WwpVoiceGatewayMIBObjects_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayMIBObjects=_WwpVoiceGatewayMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1))
_WwpVoiceGateway_ObjectIdentity=ObjectIdentity
wwpVoiceGateway=_WwpVoiceGateway_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1))
_WwpVoiceGatewayMGCP_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayMGCP=_WwpVoiceGatewayMGCP_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,1))
_WwpVoiceGatewayEndPointTable_Object=MibTable
wwpVoiceGatewayEndPointTable=_WwpVoiceGatewayEndPointTable_Object((1,3,6,1,4,1,6141,2,43,1,1,1,1))
if mibBuilder.loadTexts:wwpVoiceGatewayEndPointTable.setStatus(_A)
_WwpVoiceGatewayEndPointEntry_Object=MibTableRow
wwpVoiceGatewayEndPointEntry=_WwpVoiceGatewayEndPointEntry_Object((1,3,6,1,4,1,6141,2,43,1,1,1,1,1))
wwpVoiceGatewayEndPointEntry.setIndexNames((0,_H,_P))
if mibBuilder.loadTexts:wwpVoiceGatewayEndPointEntry.setStatus(_A)
class _WwpVoiceGatewayEndPointId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpVoiceGatewayEndPointId_Type.__name__=_C
_WwpVoiceGatewayEndPointId_Object=MibTableColumn
wwpVoiceGatewayEndPointId=_WwpVoiceGatewayEndPointId_Object((1,3,6,1,4,1,6141,2,43,1,1,1,1,1,1),_WwpVoiceGatewayEndPointId_Type())
wwpVoiceGatewayEndPointId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayEndPointId.setStatus(_A)
class _WwpVoiceGatewayEndpoint_Type(DisplayString):defaultValue=OctetString('')
_WwpVoiceGatewayEndpoint_Type.__name__=_O
_WwpVoiceGatewayEndpoint_Object=MibTableColumn
wwpVoiceGatewayEndpoint=_WwpVoiceGatewayEndpoint_Object((1,3,6,1,4,1,6141,2,43,1,1,1,1,1,2),_WwpVoiceGatewayEndpoint_Type())
wwpVoiceGatewayEndpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayEndpoint.setStatus(_A)
_WwpVoiceGatewayCallAgentAddr_Type=DisplayString
_WwpVoiceGatewayCallAgentAddr_Object=MibScalar
wwpVoiceGatewayCallAgentAddr=_WwpVoiceGatewayCallAgentAddr_Object((1,3,6,1,4,1,6141,2,43,1,1,1,2),_WwpVoiceGatewayCallAgentAddr_Type())
wwpVoiceGatewayCallAgentAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayCallAgentAddr.setStatus(_A)
class _WwpVoiceGatewayCallAgentUDPPort_Type(Integer32):defaultValue=2427;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_WwpVoiceGatewayCallAgentUDPPort_Type.__name__=_C
_WwpVoiceGatewayCallAgentUDPPort_Object=MibScalar
wwpVoiceGatewayCallAgentUDPPort=_WwpVoiceGatewayCallAgentUDPPort_Object((1,3,6,1,4,1,6141,2,43,1,1,1,3),_WwpVoiceGatewayCallAgentUDPPort_Type())
wwpVoiceGatewayCallAgentUDPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayCallAgentUDPPort.setStatus(_A)
class _WwpVoiceGatewayCallAgentProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ncs1',1),('rfc2705',2),('mgcp1Ncs1NoPackages',3)))
_WwpVoiceGatewayCallAgentProtocol_Type.__name__=_C
_WwpVoiceGatewayCallAgentProtocol_Object=MibScalar
wwpVoiceGatewayCallAgentProtocol=_WwpVoiceGatewayCallAgentProtocol_Object((1,3,6,1,4,1,6141,2,43,1,1,1,4),_WwpVoiceGatewayCallAgentProtocol_Type())
wwpVoiceGatewayCallAgentProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayCallAgentProtocol.setStatus(_A)
class _WwpVoiceGatewaySupportMessagePiggybacking_Type(TruthValue):defaultValue=1
_WwpVoiceGatewaySupportMessagePiggybacking_Type.__name__=_G
_WwpVoiceGatewaySupportMessagePiggybacking_Object=MibScalar
wwpVoiceGatewaySupportMessagePiggybacking=_WwpVoiceGatewaySupportMessagePiggybacking_Object((1,3,6,1,4,1,6141,2,43,1,1,1,5),_WwpVoiceGatewaySupportMessagePiggybacking_Type())
wwpVoiceGatewaySupportMessagePiggybacking.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySupportMessagePiggybacking.setStatus(_A)
class _WwpVoiceGatewayRsipKeepAliveEnable_Type(TruthValue):defaultValue=2
_WwpVoiceGatewayRsipKeepAliveEnable_Type.__name__=_G
_WwpVoiceGatewayRsipKeepAliveEnable_Object=MibScalar
wwpVoiceGatewayRsipKeepAliveEnable=_WwpVoiceGatewayRsipKeepAliveEnable_Object((1,3,6,1,4,1,6141,2,43,1,1,1,6),_WwpVoiceGatewayRsipKeepAliveEnable_Type())
wwpVoiceGatewayRsipKeepAliveEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayRsipKeepAliveEnable.setStatus(_A)
class _WwpVoiceGatewayRsipKeepAliveInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_WwpVoiceGatewayRsipKeepAliveInterval_Type.__name__=_C
_WwpVoiceGatewayRsipKeepAliveInterval_Object=MibScalar
wwpVoiceGatewayRsipKeepAliveInterval=_WwpVoiceGatewayRsipKeepAliveInterval_Object((1,3,6,1,4,1,6141,2,43,1,1,1,7),_WwpVoiceGatewayRsipKeepAliveInterval_Type())
wwpVoiceGatewayRsipKeepAliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayRsipKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceGatewayRsipKeepAliveInterval.setUnits(_K)
_WwpVoiceGatewayCountry_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayCountry=_WwpVoiceGatewayCountry_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,2))
class _WwpVoiceGatewayCountryCodes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('usa',1),('dubai',2),('holland',3),('newZealand',4),('uk',5),('sweden',6)))
_WwpVoiceGatewayCountryCodes_Type.__name__=_C
_WwpVoiceGatewayCountryCodes_Object=MibScalar
wwpVoiceGatewayCountryCodes=_WwpVoiceGatewayCountryCodes_Object((1,3,6,1,4,1,6141,2,43,1,1,2,1),_WwpVoiceGatewayCountryCodes_Type())
wwpVoiceGatewayCountryCodes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayCountryCodes.setStatus(_A)
_WwpVoiceGatewayCodec_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayCodec=_WwpVoiceGatewayCodec_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,3))
class _WwpVoiceGatewayComplexCodec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('g711',2),('g723',3),('g726',4),('g729',5)))
_WwpVoiceGatewayComplexCodec_Type.__name__=_C
_WwpVoiceGatewayComplexCodec_Object=MibScalar
wwpVoiceGatewayComplexCodec=_WwpVoiceGatewayComplexCodec_Object((1,3,6,1,4,1,6141,2,43,1,1,3,1),_WwpVoiceGatewayComplexCodec_Type())
wwpVoiceGatewayComplexCodec.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayComplexCodec.setStatus(_A)
class _WwpVoiceGatewaySilenceSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpVoiceGatewaySilenceSuppression_Type.__name__=_C
_WwpVoiceGatewaySilenceSuppression_Object=MibScalar
wwpVoiceGatewaySilenceSuppression=_WwpVoiceGatewaySilenceSuppression_Object((1,3,6,1,4,1,6141,2,43,1,1,3,2),_WwpVoiceGatewaySilenceSuppression_Type())
wwpVoiceGatewaySilenceSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySilenceSuppression.setStatus(_A)
class _WwpVoiceGatewayEchoCancellation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpVoiceGatewayEchoCancellation_Type.__name__=_C
_WwpVoiceGatewayEchoCancellation_Object=MibScalar
wwpVoiceGatewayEchoCancellation=_WwpVoiceGatewayEchoCancellation_Object((1,3,6,1,4,1,6141,2,43,1,1,3,3),_WwpVoiceGatewayEchoCancellation_Type())
wwpVoiceGatewayEchoCancellation.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayEchoCancellation.setStatus(_A)
_WwpVoiceGatewayPacketizationMinPeriod_Type=Integer32
_WwpVoiceGatewayPacketizationMinPeriod_Object=MibScalar
wwpVoiceGatewayPacketizationMinPeriod=_WwpVoiceGatewayPacketizationMinPeriod_Object((1,3,6,1,4,1,6141,2,43,1,1,3,4),_WwpVoiceGatewayPacketizationMinPeriod_Type())
wwpVoiceGatewayPacketizationMinPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayPacketizationMinPeriod.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceGatewayPacketizationMinPeriod.setUnits(_F)
_WwpVoiceGatewayPacketizationMaxPeriod_Type=Integer32
_WwpVoiceGatewayPacketizationMaxPeriod_Object=MibScalar
wwpVoiceGatewayPacketizationMaxPeriod=_WwpVoiceGatewayPacketizationMaxPeriod_Object((1,3,6,1,4,1,6141,2,43,1,1,3,5),_WwpVoiceGatewayPacketizationMaxPeriod_Type())
wwpVoiceGatewayPacketizationMaxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayPacketizationMaxPeriod.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceGatewayPacketizationMaxPeriod.setUnits(_F)
_WwpVoiceGatewayAudio_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayAudio=_WwpVoiceGatewayAudio_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,4))
class _WwpVoiceGatewayPayloadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(94,127))
_WwpVoiceGatewayPayloadType_Type.__name__=_C
_WwpVoiceGatewayPayloadType_Object=MibScalar
wwpVoiceGatewayPayloadType=_WwpVoiceGatewayPayloadType_Object((1,3,6,1,4,1,6141,2,43,1,1,4,1),_WwpVoiceGatewayPayloadType_Type())
wwpVoiceGatewayPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayPayloadType.setStatus(_A)
_WwpVoiceGatewaySendEventsViaRFC2833_Type=TruthValue
_WwpVoiceGatewaySendEventsViaRFC2833_Object=MibScalar
wwpVoiceGatewaySendEventsViaRFC2833=_WwpVoiceGatewaySendEventsViaRFC2833_Object((1,3,6,1,4,1,6141,2,43,1,1,4,2),_WwpVoiceGatewaySendEventsViaRFC2833_Type())
wwpVoiceGatewaySendEventsViaRFC2833.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySendEventsViaRFC2833.setStatus(_A)
_WwpVoiceGatewayDropVoicePktsDuringEvents_Type=TruthValue
_WwpVoiceGatewayDropVoicePktsDuringEvents_Object=MibScalar
wwpVoiceGatewayDropVoicePktsDuringEvents=_WwpVoiceGatewayDropVoicePktsDuringEvents_Object((1,3,6,1,4,1,6141,2,43,1,1,4,3),_WwpVoiceGatewayDropVoicePktsDuringEvents_Type())
wwpVoiceGatewayDropVoicePktsDuringEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayDropVoicePktsDuringEvents.setStatus(_A)
_WwpVoiceGatewaySquelchInbandDtmfAudio_Type=TruthValue
_WwpVoiceGatewaySquelchInbandDtmfAudio_Object=MibScalar
wwpVoiceGatewaySquelchInbandDtmfAudio=_WwpVoiceGatewaySquelchInbandDtmfAudio_Object((1,3,6,1,4,1,6141,2,43,1,1,4,4),_WwpVoiceGatewaySquelchInbandDtmfAudio_Type())
wwpVoiceGatewaySquelchInbandDtmfAudio.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySquelchInbandDtmfAudio.setStatus(_A)
_WwpVoiceGatewayStats_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayStats=_WwpVoiceGatewayStats_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,5))
_WwpVoiceGatewayPktsTx_Type=Counter32
_WwpVoiceGatewayPktsTx_Object=MibScalar
wwpVoiceGatewayPktsTx=_WwpVoiceGatewayPktsTx_Object((1,3,6,1,4,1,6141,2,43,1,1,5,1),_WwpVoiceGatewayPktsTx_Type())
wwpVoiceGatewayPktsTx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayPktsTx.setStatus(_A)
_WwpVoiceGatewayOctetsTx_Type=Counter32
_WwpVoiceGatewayOctetsTx_Object=MibScalar
wwpVoiceGatewayOctetsTx=_WwpVoiceGatewayOctetsTx_Object((1,3,6,1,4,1,6141,2,43,1,1,5,2),_WwpVoiceGatewayOctetsTx_Type())
wwpVoiceGatewayOctetsTx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayOctetsTx.setStatus(_A)
_WwpVoiceGatewayPktsRx_Type=Counter32
_WwpVoiceGatewayPktsRx_Object=MibScalar
wwpVoiceGatewayPktsRx=_WwpVoiceGatewayPktsRx_Object((1,3,6,1,4,1,6141,2,43,1,1,5,3),_WwpVoiceGatewayPktsRx_Type())
wwpVoiceGatewayPktsRx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayPktsRx.setStatus(_A)
_WwpVoiceGatewayOctetsRx_Type=Counter32
_WwpVoiceGatewayOctetsRx_Object=MibScalar
wwpVoiceGatewayOctetsRx=_WwpVoiceGatewayOctetsRx_Object((1,3,6,1,4,1,6141,2,43,1,1,5,4),_WwpVoiceGatewayOctetsRx_Type())
wwpVoiceGatewayOctetsRx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayOctetsRx.setStatus(_A)
_WwpVoiceGatewayPktsLost_Type=Counter32
_WwpVoiceGatewayPktsLost_Object=MibScalar
wwpVoiceGatewayPktsLost=_WwpVoiceGatewayPktsLost_Object((1,3,6,1,4,1,6141,2,43,1,1,5,5),_WwpVoiceGatewayPktsLost_Type())
wwpVoiceGatewayPktsLost.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayPktsLost.setStatus(_A)
_WwpVoiceGatewayIntervalJitter_Type=Integer32
_WwpVoiceGatewayIntervalJitter_Object=MibScalar
wwpVoiceGatewayIntervalJitter=_WwpVoiceGatewayIntervalJitter_Object((1,3,6,1,4,1,6141,2,43,1,1,5,6),_WwpVoiceGatewayIntervalJitter_Type())
wwpVoiceGatewayIntervalJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayIntervalJitter.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceGatewayIntervalJitter.setUnits(_F)
_WwpVoiceGatewayLatency_Type=Integer32
_WwpVoiceGatewayLatency_Object=MibScalar
wwpVoiceGatewayLatency=_WwpVoiceGatewayLatency_Object((1,3,6,1,4,1,6141,2,43,1,1,5,7),_WwpVoiceGatewayLatency_Type())
wwpVoiceGatewayLatency.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayLatency.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceGatewayLatency.setUnits(_F)
class _WwpVoiceGatewayResetStatCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('reset',1)))
_WwpVoiceGatewayResetStatCounters_Type.__name__=_C
_WwpVoiceGatewayResetStatCounters_Object=MibScalar
wwpVoiceGatewayResetStatCounters=_WwpVoiceGatewayResetStatCounters_Object((1,3,6,1,4,1,6141,2,43,1,1,5,8),_WwpVoiceGatewayResetStatCounters_Type())
wwpVoiceGatewayResetStatCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayResetStatCounters.setStatus(_A)
_WwpVoiceReset_ObjectIdentity=ObjectIdentity
wwpVoiceReset=_WwpVoiceReset_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,6))
class _WwpVoiceGatewayNumResets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpVoiceGatewayNumResets_Type.__name__=_N
_WwpVoiceGatewayNumResets_Object=MibScalar
wwpVoiceGatewayNumResets=_WwpVoiceGatewayNumResets_Object((1,3,6,1,4,1,6141,2,43,1,1,6,1),_WwpVoiceGatewayNumResets_Type())
wwpVoiceGatewayNumResets.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayNumResets.setStatus(_A)
class _WwpVoiceGatewayReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('reset',1),('resetDefault',2)))
_WwpVoiceGatewayReset_Type.__name__=_C
_WwpVoiceGatewayReset_Object=MibScalar
wwpVoiceGatewayReset=_WwpVoiceGatewayReset_Object((1,3,6,1,4,1,6141,2,43,1,1,6,2),_WwpVoiceGatewayReset_Type())
wwpVoiceGatewayReset.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayReset.setStatus(_A)
_WwpVoiceSec_ObjectIdentity=ObjectIdentity
wwpVoiceSec=_WwpVoiceSec_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,7))
class _WwpVoiceAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_WwpVoiceAccess_Type.__name__=_C
_WwpVoiceAccess_Object=MibScalar
wwpVoiceAccess=_WwpVoiceAccess_Object((1,3,6,1,4,1,6141,2,43,1,1,7,1),_WwpVoiceAccess_Type())
wwpVoiceAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceAccess.setStatus(_A)
class _WwpMgmtAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_WwpMgmtAccess_Type.__name__=_C
_WwpMgmtAccess_Object=MibScalar
wwpMgmtAccess=_WwpMgmtAccess_Object((1,3,6,1,4,1,6141,2,43,1,1,7,2),_WwpMgmtAccess_Type())
wwpMgmtAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpMgmtAccess.setStatus(_A)
_WwpVoiceGatewayConfigCallAgent_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigCallAgent=_WwpVoiceGatewayConfigCallAgent_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,8))
class _WwpVoiceCallAgentOtaModes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ifOtaRecv',1),('sendOta',2)))
_WwpVoiceCallAgentOtaModes_Type.__name__=_C
_WwpVoiceCallAgentOtaModes_Object=MibScalar
wwpVoiceCallAgentOtaModes=_WwpVoiceCallAgentOtaModes_Object((1,3,6,1,4,1,6141,2,43,1,1,8,1),_WwpVoiceCallAgentOtaModes_Type())
wwpVoiceCallAgentOtaModes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceCallAgentOtaModes.setStatus(_A)
class _WwpVoiceCallAgentEgressEvent_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sendIngressEgressNotif',1),('sendIngressNotif',2)))
_WwpVoiceCallAgentEgressEvent_Type.__name__=_C
_WwpVoiceCallAgentEgressEvent_Object=MibScalar
wwpVoiceCallAgentEgressEvent=_WwpVoiceCallAgentEgressEvent_Object((1,3,6,1,4,1,6141,2,43,1,1,8,2),_WwpVoiceCallAgentEgressEvent_Type())
wwpVoiceCallAgentEgressEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceCallAgentEgressEvent.setStatus(_A)
_WwpVoiceGatewayConfigPots_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigPots=_WwpVoiceGatewayConfigPots_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,9))
class _WwpVoiceCallAgentPotsLine_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable1PotLine',1),('enable2PotLine',2)))
_WwpVoiceCallAgentPotsLine_Type.__name__=_C
_WwpVoiceCallAgentPotsLine_Object=MibScalar
wwpVoiceCallAgentPotsLine=_WwpVoiceCallAgentPotsLine_Object((1,3,6,1,4,1,6141,2,43,1,1,9,1),_WwpVoiceCallAgentPotsLine_Type())
wwpVoiceCallAgentPotsLine.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceCallAgentPotsLine.setStatus(_A)
_WwpVoiceGatewayConfigFax_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigFax=_WwpVoiceGatewayConfigFax_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,10))
class _WwpVoiceAutonomousFaxState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpVoiceAutonomousFaxState_Type.__name__=_C
_WwpVoiceAutonomousFaxState_Object=MibScalar
wwpVoiceAutonomousFaxState=_WwpVoiceAutonomousFaxState_Object((1,3,6,1,4,1,6141,2,43,1,1,10,1),_WwpVoiceAutonomousFaxState_Type())
wwpVoiceAutonomousFaxState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceAutonomousFaxState.setStatus(_A)
_WwpVoiceGatewayConfigEndPoint_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigEndPoint=_WwpVoiceGatewayConfigEndPoint_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,11))
class _WwpVoiceEndPointName_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('ip',2),('mac',3),('hostName',4),('fqdn',5)))
_WwpVoiceEndPointName_Type.__name__=_C
_WwpVoiceEndPointName_Object=MibScalar
wwpVoiceEndPointName=_WwpVoiceEndPointName_Object((1,3,6,1,4,1,6141,2,43,1,1,11,1),_WwpVoiceEndPointName_Type())
wwpVoiceEndPointName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceEndPointName.setStatus(_A)
_WwpVoiceGatewayConfigNotifEntityCache_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigNotifEntityCache=_WwpVoiceGatewayConfigNotifEntityCache_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,12))
class _WwpVoiceNotifEntCache_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_WwpVoiceNotifEntCache_Type.__name__=_C
_WwpVoiceNotifEntCache_Object=MibScalar
wwpVoiceNotifEntCache=_WwpVoiceNotifEntCache_Object((1,3,6,1,4,1,6141,2,43,1,1,12,1),_WwpVoiceNotifEntCache_Type())
wwpVoiceNotifEntCache.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceNotifEntCache.setStatus(_A)
_WwpVoiceGatewayConfigJitterBuffer_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigJitterBuffer=_WwpVoiceGatewayConfigJitterBuffer_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,13))
class _WwpVoiceJitterOptionState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_L,1)))
_WwpVoiceJitterOptionState_Type.__name__=_C
_WwpVoiceJitterOptionState_Object=MibScalar
wwpVoiceJitterOptionState=_WwpVoiceJitterOptionState_Object((1,3,6,1,4,1,6141,2,43,1,1,13,1),_WwpVoiceJitterOptionState_Type())
wwpVoiceJitterOptionState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceJitterOptionState.setStatus(_A)
_WwpVoiceGatewayConfigJitterBufferMinPeriod_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigJitterBufferMinPeriod=_WwpVoiceGatewayConfigJitterBufferMinPeriod_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,14))
_WwpVoiceJitterBufferMinPeriod_Type=Integer32
_WwpVoiceJitterBufferMinPeriod_Object=MibScalar
wwpVoiceJitterBufferMinPeriod=_WwpVoiceJitterBufferMinPeriod_Object((1,3,6,1,4,1,6141,2,43,1,1,14,1),_WwpVoiceJitterBufferMinPeriod_Type())
wwpVoiceJitterBufferMinPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceJitterBufferMinPeriod.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceJitterBufferMinPeriod.setUnits(_F)
_WwpVoiceGatewayConfigJitterBufferMaxPeriod_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigJitterBufferMaxPeriod=_WwpVoiceGatewayConfigJitterBufferMaxPeriod_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,15))
_WwpVoiceJitterBufferMaxPeriod_Type=Integer32
_WwpVoiceJitterBufferMaxPeriod_Object=MibScalar
wwpVoiceJitterBufferMaxPeriod=_WwpVoiceJitterBufferMaxPeriod_Object((1,3,6,1,4,1,6141,2,43,1,1,15,1),_WwpVoiceJitterBufferMaxPeriod_Type())
wwpVoiceJitterBufferMaxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceJitterBufferMaxPeriod.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceJitterBufferMaxPeriod.setUnits(_F)
_WwpVoiceGatewayConfigJitterBufferTargetPeriod_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigJitterBufferTargetPeriod=_WwpVoiceGatewayConfigJitterBufferTargetPeriod_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,16))
_WwpVoiceJitterBufferTargetPeriod_Type=Integer32
_WwpVoiceJitterBufferTargetPeriod_Object=MibScalar
wwpVoiceJitterBufferTargetPeriod=_WwpVoiceJitterBufferTargetPeriod_Object((1,3,6,1,4,1,6141,2,43,1,1,16,1),_WwpVoiceJitterBufferTargetPeriod_Type())
wwpVoiceJitterBufferTargetPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceJitterBufferTargetPeriod.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceJitterBufferTargetPeriod.setUnits(_F)
_WwpVoiceGatewayConfigCodecOverride_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigCodecOverride=_WwpVoiceGatewayConfigCodecOverride_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,17))
class _WwpVoiceGatewayCodecOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('g711PCMU',1),('g711PCMA',2)))
_WwpVoiceGatewayCodecOverride_Type.__name__=_C
_WwpVoiceGatewayCodecOverride_Object=MibScalar
wwpVoiceGatewayCodecOverride=_WwpVoiceGatewayCodecOverride_Object((1,3,6,1,4,1,6141,2,43,1,1,17,1),_WwpVoiceGatewayCodecOverride_Type())
wwpVoiceGatewayCodecOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayCodecOverride.setStatus(_A)
_WwpVoiceGatewayConfigTestServerConnection_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigTestServerConnection=_WwpVoiceGatewayConfigTestServerConnection_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,18))
class _WwpVoiceGatewayTestServerConnection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_I,0))
_WwpVoiceGatewayTestServerConnection_Type.__name__=_C
_WwpVoiceGatewayTestServerConnection_Object=MibScalar
wwpVoiceGatewayTestServerConnection=_WwpVoiceGatewayTestServerConnection_Object((1,3,6,1,4,1,6141,2,43,1,1,18,1),_WwpVoiceGatewayTestServerConnection_Type())
wwpVoiceGatewayTestServerConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayTestServerConnection.setStatus(_A)
_WwpVoiceGatewayConfigLastServerResponseTime_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigLastServerResponseTime=_WwpVoiceGatewayConfigLastServerResponseTime_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,19))
class _WwpVoiceGatewayLastServerResponseTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpVoiceGatewayLastServerResponseTime_Type.__name__=_E
_WwpVoiceGatewayLastServerResponseTime_Object=MibScalar
wwpVoiceGatewayLastServerResponseTime=_WwpVoiceGatewayLastServerResponseTime_Object((1,3,6,1,4,1,6141,2,43,1,1,19,1),_WwpVoiceGatewayLastServerResponseTime_Type())
wwpVoiceGatewayLastServerResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewayLastServerResponseTime.setStatus(_A)
_WwpVoiceGatewaySIP_ObjectIdentity=ObjectIdentity
wwpVoiceGatewaySIP=_WwpVoiceGatewaySIP_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,20))
class _WwpVoiceGatewaySipSessionTimeoutPeriod_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_WwpVoiceGatewaySipSessionTimeoutPeriod_Type.__name__=_C
_WwpVoiceGatewaySipSessionTimeoutPeriod_Object=MibScalar
wwpVoiceGatewaySipSessionTimeoutPeriod=_WwpVoiceGatewaySipSessionTimeoutPeriod_Object((1,3,6,1,4,1,6141,2,43,1,1,20,1),_WwpVoiceGatewaySipSessionTimeoutPeriod_Type())
wwpVoiceGatewaySipSessionTimeoutPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipSessionTimeoutPeriod.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceGatewaySipSessionTimeoutPeriod.setUnits(_K)
class _WwpVoiceGatewaySipRegisterTimeoutPeriod_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_WwpVoiceGatewaySipRegisterTimeoutPeriod_Type.__name__=_C
_WwpVoiceGatewaySipRegisterTimeoutPeriod_Object=MibScalar
wwpVoiceGatewaySipRegisterTimeoutPeriod=_WwpVoiceGatewaySipRegisterTimeoutPeriod_Object((1,3,6,1,4,1,6141,2,43,1,1,20,2),_WwpVoiceGatewaySipRegisterTimeoutPeriod_Type())
wwpVoiceGatewaySipRegisterTimeoutPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipRegisterTimeoutPeriod.setStatus(_A)
if mibBuilder.loadTexts:wwpVoiceGatewaySipRegisterTimeoutPeriod.setUnits(_K)
class _WwpVoiceGatewaySipForceQuotesState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_L,1)))
_WwpVoiceGatewaySipForceQuotesState_Type.__name__=_C
_WwpVoiceGatewaySipForceQuotesState_Object=MibScalar
wwpVoiceGatewaySipForceQuotesState=_WwpVoiceGatewaySipForceQuotesState_Object((1,3,6,1,4,1,6141,2,43,1,1,20,3),_WwpVoiceGatewaySipForceQuotesState_Type())
wwpVoiceGatewaySipForceQuotesState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipForceQuotesState.setStatus(_A)
_WwpVoiceGatewaySipPhoneLineTable_Object=MibTable
wwpVoiceGatewaySipPhoneLineTable=_WwpVoiceGatewaySipPhoneLineTable_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4))
if mibBuilder.loadTexts:wwpVoiceGatewaySipPhoneLineTable.setStatus(_A)
_WwpVoiceGatewaySipPhoneLineEntry_Object=MibTableRow
wwpVoiceGatewaySipPhoneLineEntry=_WwpVoiceGatewaySipPhoneLineEntry_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4,1))
wwpVoiceGatewaySipPhoneLineEntry.setIndexNames((0,_H,_Q))
if mibBuilder.loadTexts:wwpVoiceGatewaySipPhoneLineEntry.setStatus(_A)
class _WwpVoiceGatewaySipLineId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpVoiceGatewaySipLineId_Type.__name__=_C
_WwpVoiceGatewaySipLineId_Object=MibTableColumn
wwpVoiceGatewaySipLineId=_WwpVoiceGatewaySipLineId_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4,1,1),_WwpVoiceGatewaySipLineId_Type())
wwpVoiceGatewaySipLineId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewaySipLineId.setStatus(_A)
class _WwpVoiceGatewaySipPhoneNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpVoiceGatewaySipPhoneNumber_Type.__name__=_E
_WwpVoiceGatewaySipPhoneNumber_Object=MibTableColumn
wwpVoiceGatewaySipPhoneNumber=_WwpVoiceGatewaySipPhoneNumber_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4,1,2),_WwpVoiceGatewaySipPhoneNumber_Type())
wwpVoiceGatewaySipPhoneNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpVoiceGatewaySipPhoneNumber.setStatus(_A)
class _WwpVoiceGatewaySipUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpVoiceGatewaySipUserName_Type.__name__=_E
_WwpVoiceGatewaySipUserName_Object=MibTableColumn
wwpVoiceGatewaySipUserName=_WwpVoiceGatewaySipUserName_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4,1,3),_WwpVoiceGatewaySipUserName_Type())
wwpVoiceGatewaySipUserName.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpVoiceGatewaySipUserName.setStatus(_A)
class _WwpVoiceGatewaySipUserDisplayName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpVoiceGatewaySipUserDisplayName_Type.__name__=_E
_WwpVoiceGatewaySipUserDisplayName_Object=MibTableColumn
wwpVoiceGatewaySipUserDisplayName=_WwpVoiceGatewaySipUserDisplayName_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4,1,4),_WwpVoiceGatewaySipUserDisplayName_Type())
wwpVoiceGatewaySipUserDisplayName.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpVoiceGatewaySipUserDisplayName.setStatus(_A)
class _WwpVoiceGatewaySipUserPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpVoiceGatewaySipUserPassword_Type.__name__=_E
_WwpVoiceGatewaySipUserPassword_Object=MibTableColumn
wwpVoiceGatewaySipUserPassword=_WwpVoiceGatewaySipUserPassword_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4,1,5),_WwpVoiceGatewaySipUserPassword_Type())
wwpVoiceGatewaySipUserPassword.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpVoiceGatewaySipUserPassword.setStatus(_A)
class _WwpVoiceGatewaySipDialPlan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpVoiceGatewaySipDialPlan_Type.__name__=_E
_WwpVoiceGatewaySipDialPlan_Object=MibTableColumn
wwpVoiceGatewaySipDialPlan=_WwpVoiceGatewaySipDialPlan_Object((1,3,6,1,4,1,6141,2,43,1,1,20,4,1,6),_WwpVoiceGatewaySipDialPlan_Type())
wwpVoiceGatewaySipDialPlan.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipDialPlan.setStatus(_A)
_WwpVoiceGatewaySipPhoneLineTimerTable_Object=MibTable
wwpVoiceGatewaySipPhoneLineTimerTable=_WwpVoiceGatewaySipPhoneLineTimerTable_Object((1,3,6,1,4,1,6141,2,43,1,1,20,5))
if mibBuilder.loadTexts:wwpVoiceGatewaySipPhoneLineTimerTable.setStatus(_A)
_WwpVoiceGatewaySipPhoneLineTimerEntry_Object=MibTableRow
wwpVoiceGatewaySipPhoneLineTimerEntry=_WwpVoiceGatewaySipPhoneLineTimerEntry_Object((1,3,6,1,4,1,6141,2,43,1,1,20,5,1))
wwpVoiceGatewaySipPhoneLineTimerEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:wwpVoiceGatewaySipPhoneLineTimerEntry.setStatus(_A)
class _WwpVoiceGatewaySipTimerLineId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpVoiceGatewaySipTimerLineId_Type.__name__=_C
_WwpVoiceGatewaySipTimerLineId_Object=MibTableColumn
wwpVoiceGatewaySipTimerLineId=_WwpVoiceGatewaySipTimerLineId_Object((1,3,6,1,4,1,6141,2,43,1,1,20,5,1,1),_WwpVoiceGatewaySipTimerLineId_Type())
wwpVoiceGatewaySipTimerLineId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVoiceGatewaySipTimerLineId.setStatus(_A)
class _WwpVoiceGatewaySipDialTimerLong_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_WwpVoiceGatewaySipDialTimerLong_Type.__name__=_C
_WwpVoiceGatewaySipDialTimerLong_Object=MibTableColumn
wwpVoiceGatewaySipDialTimerLong=_WwpVoiceGatewaySipDialTimerLong_Object((1,3,6,1,4,1,6141,2,43,1,1,20,5,1,2),_WwpVoiceGatewaySipDialTimerLong_Type())
wwpVoiceGatewaySipDialTimerLong.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipDialTimerLong.setStatus(_A)
_WwpVoiceGatewaySIPServers_ObjectIdentity=ObjectIdentity
wwpVoiceGatewaySIPServers=_WwpVoiceGatewaySIPServers_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,20,6))
_WwpVoiceGatewaySIPProxyServers_ObjectIdentity=ObjectIdentity
wwpVoiceGatewaySIPProxyServers=_WwpVoiceGatewaySIPProxyServers_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,20,6,1))
_WwpVoiceGatewaySipProxyAddr_Type=DisplayString
_WwpVoiceGatewaySipProxyAddr_Object=MibScalar
wwpVoiceGatewaySipProxyAddr=_WwpVoiceGatewaySipProxyAddr_Object((1,3,6,1,4,1,6141,2,43,1,1,20,6,1,1),_WwpVoiceGatewaySipProxyAddr_Type())
wwpVoiceGatewaySipProxyAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipProxyAddr.setStatus(_A)
class _WwpVoiceGatewaySipProxyPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_WwpVoiceGatewaySipProxyPort_Type.__name__=_C
_WwpVoiceGatewaySipProxyPort_Object=MibScalar
wwpVoiceGatewaySipProxyPort=_WwpVoiceGatewaySipProxyPort_Object((1,3,6,1,4,1,6141,2,43,1,1,20,6,1,2),_WwpVoiceGatewaySipProxyPort_Type())
wwpVoiceGatewaySipProxyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipProxyPort.setStatus(_A)
_WwpVoiceGatewaySIPRegistrarServers_ObjectIdentity=ObjectIdentity
wwpVoiceGatewaySIPRegistrarServers=_WwpVoiceGatewaySIPRegistrarServers_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,20,6,2))
_WwpVoiceGatewaySipRegistrarAddr_Type=DisplayString
_WwpVoiceGatewaySipRegistrarAddr_Object=MibScalar
wwpVoiceGatewaySipRegistrarAddr=_WwpVoiceGatewaySipRegistrarAddr_Object((1,3,6,1,4,1,6141,2,43,1,1,20,6,2,1),_WwpVoiceGatewaySipRegistrarAddr_Type())
wwpVoiceGatewaySipRegistrarAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipRegistrarAddr.setStatus(_A)
class _WwpVoiceGatewaySipRegistrarPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_WwpVoiceGatewaySipRegistrarPort_Type.__name__=_C
_WwpVoiceGatewaySipRegistrarPort_Object=MibScalar
wwpVoiceGatewaySipRegistrarPort=_WwpVoiceGatewaySipRegistrarPort_Object((1,3,6,1,4,1,6141,2,43,1,1,20,6,2,2),_WwpVoiceGatewaySipRegistrarPort_Type())
wwpVoiceGatewaySipRegistrarPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipRegistrarPort.setStatus(_A)
_WwpVoiceGatewaySIPLogServers_ObjectIdentity=ObjectIdentity
wwpVoiceGatewaySIPLogServers=_WwpVoiceGatewaySIPLogServers_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,20,6,3))
_WwpVoiceGatewaySipSyslogAddr_Type=DisplayString
_WwpVoiceGatewaySipSyslogAddr_Object=MibScalar
wwpVoiceGatewaySipSyslogAddr=_WwpVoiceGatewaySipSyslogAddr_Object((1,3,6,1,4,1,6141,2,43,1,1,20,6,3,1),_WwpVoiceGatewaySipSyslogAddr_Type())
wwpVoiceGatewaySipSyslogAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipSyslogAddr.setStatus(_A)
class _WwpVoiceGatewaySipSyslogPort_Type(Integer32):defaultValue=514;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpVoiceGatewaySipSyslogPort_Type.__name__=_C
_WwpVoiceGatewaySipSyslogPort_Object=MibScalar
wwpVoiceGatewaySipSyslogPort=_WwpVoiceGatewaySipSyslogPort_Object((1,3,6,1,4,1,6141,2,43,1,1,20,6,3,2),_WwpVoiceGatewaySipSyslogPort_Type())
wwpVoiceGatewaySipSyslogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipSyslogPort.setStatus(_A)
class _WwpVoiceGatewaySipSyslogLogLevel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WwpVoiceGatewaySipSyslogLogLevel_Type.__name__=_C
_WwpVoiceGatewaySipSyslogLogLevel_Object=MibScalar
wwpVoiceGatewaySipSyslogLogLevel=_WwpVoiceGatewaySipSyslogLogLevel_Object((1,3,6,1,4,1,6141,2,43,1,1,20,6,3,3),_WwpVoiceGatewaySipSyslogLogLevel_Type())
wwpVoiceGatewaySipSyslogLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySipSyslogLogLevel.setStatus(_A)
class _WwpVoiceGatewaySIPPreferredCodec_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('g711',1),('g729',2)))
_WwpVoiceGatewaySIPPreferredCodec_Type.__name__=_C
_WwpVoiceGatewaySIPPreferredCodec_Object=MibScalar
wwpVoiceGatewaySIPPreferredCodec=_WwpVoiceGatewaySIPPreferredCodec_Object((1,3,6,1,4,1,6141,2,43,1,1,20,7),_WwpVoiceGatewaySIPPreferredCodec_Type())
wwpVoiceGatewaySIPPreferredCodec.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySIPPreferredCodec.setStatus(_A)
class _WwpVoiceGatewaySIPDtmfEventHandling_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('audio',1),('info',2),('rfc2833',3)))
_WwpVoiceGatewaySIPDtmfEventHandling_Type.__name__=_C
_WwpVoiceGatewaySIPDtmfEventHandling_Object=MibScalar
wwpVoiceGatewaySIPDtmfEventHandling=_WwpVoiceGatewaySIPDtmfEventHandling_Object((1,3,6,1,4,1,6141,2,43,1,1,20,8),_WwpVoiceGatewaySIPDtmfEventHandling_Type())
wwpVoiceGatewaySIPDtmfEventHandling.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewaySIPDtmfEventHandling.setStatus(_A)
_WwpVoiceGatewaySIPCallFeatures_ObjectIdentity=ObjectIdentity
wwpVoiceGatewaySIPCallFeatures=_WwpVoiceGatewaySIPCallFeatures_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,20,9))
class _WwpVoiceGatewayHookFlashEnable_Type(TruthValue):defaultValue=1
_WwpVoiceGatewayHookFlashEnable_Type.__name__=_G
_WwpVoiceGatewayHookFlashEnable_Object=MibScalar
wwpVoiceGatewayHookFlashEnable=_WwpVoiceGatewayHookFlashEnable_Object((1,3,6,1,4,1,6141,2,43,1,1,20,9,1),_WwpVoiceGatewayHookFlashEnable_Type())
wwpVoiceGatewayHookFlashEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayHookFlashEnable.setStatus(_A)
_WwpVoiceGatewayConfigProtocolType_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigProtocolType=_WwpVoiceGatewayConfigProtocolType_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,21))
class _WwpVoiceGatewayProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgcp',1),('sip',2)))
_WwpVoiceGatewayProtocolType_Type.__name__=_C
_WwpVoiceGatewayProtocolType_Object=MibScalar
wwpVoiceGatewayProtocolType=_WwpVoiceGatewayProtocolType_Object((1,3,6,1,4,1,6141,2,43,1,1,21,1),_WwpVoiceGatewayProtocolType_Type())
wwpVoiceGatewayProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayProtocolType.setStatus(_A)
_WwpVoiceGatewayConfigProtocolEnable_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayConfigProtocolEnable=_WwpVoiceGatewayConfigProtocolEnable_ObjectIdentity((1,3,6,1,4,1,6141,2,43,1,1,22))
class _WwpVoiceGatewayProtocolEnable_Type(TruthValue):defaultValue=2
_WwpVoiceGatewayProtocolEnable_Type.__name__=_G
_WwpVoiceGatewayProtocolEnable_Object=MibScalar
wwpVoiceGatewayProtocolEnable=_WwpVoiceGatewayProtocolEnable_Object((1,3,6,1,4,1,6141,2,43,1,1,22,1),_WwpVoiceGatewayProtocolEnable_Type())
wwpVoiceGatewayProtocolEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoiceGatewayProtocolEnable.setStatus(_A)
_WwpVoiceGatewayMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayMIBNotificationPrefix=_WwpVoiceGatewayMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,43,2))
_WwpVoiceGatewayMIBNotifications_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayMIBNotifications=_WwpVoiceGatewayMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,43,2,0))
_WwpVoiceGatewayMIBConformance_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayMIBConformance=_WwpVoiceGatewayMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,43,3))
_WwpVoiceGatewayMIBCompliances_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayMIBCompliances=_WwpVoiceGatewayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,43,3,1))
_WwpVoiceGatewayMIBGroups_ObjectIdentity=ObjectIdentity
wwpVoiceGatewayMIBGroups=_WwpVoiceGatewayMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,43,3,2))
mibBuilder.exportSymbols(_H,**{'wwpVoiceGatewayMIB':wwpVoiceGatewayMIB,'wwpVoiceGatewayMIBObjects':wwpVoiceGatewayMIBObjects,'wwpVoiceGateway':wwpVoiceGateway,'wwpVoiceGatewayMGCP':wwpVoiceGatewayMGCP,'wwpVoiceGatewayEndPointTable':wwpVoiceGatewayEndPointTable,'wwpVoiceGatewayEndPointEntry':wwpVoiceGatewayEndPointEntry,_P:wwpVoiceGatewayEndPointId,'wwpVoiceGatewayEndpoint':wwpVoiceGatewayEndpoint,'wwpVoiceGatewayCallAgentAddr':wwpVoiceGatewayCallAgentAddr,'wwpVoiceGatewayCallAgentUDPPort':wwpVoiceGatewayCallAgentUDPPort,'wwpVoiceGatewayCallAgentProtocol':wwpVoiceGatewayCallAgentProtocol,'wwpVoiceGatewaySupportMessagePiggybacking':wwpVoiceGatewaySupportMessagePiggybacking,'wwpVoiceGatewayRsipKeepAliveEnable':wwpVoiceGatewayRsipKeepAliveEnable,'wwpVoiceGatewayRsipKeepAliveInterval':wwpVoiceGatewayRsipKeepAliveInterval,'wwpVoiceGatewayCountry':wwpVoiceGatewayCountry,'wwpVoiceGatewayCountryCodes':wwpVoiceGatewayCountryCodes,'wwpVoiceGatewayCodec':wwpVoiceGatewayCodec,'wwpVoiceGatewayComplexCodec':wwpVoiceGatewayComplexCodec,'wwpVoiceGatewaySilenceSuppression':wwpVoiceGatewaySilenceSuppression,'wwpVoiceGatewayEchoCancellation':wwpVoiceGatewayEchoCancellation,'wwpVoiceGatewayPacketizationMinPeriod':wwpVoiceGatewayPacketizationMinPeriod,'wwpVoiceGatewayPacketizationMaxPeriod':wwpVoiceGatewayPacketizationMaxPeriod,'wwpVoiceGatewayAudio':wwpVoiceGatewayAudio,'wwpVoiceGatewayPayloadType':wwpVoiceGatewayPayloadType,'wwpVoiceGatewaySendEventsViaRFC2833':wwpVoiceGatewaySendEventsViaRFC2833,'wwpVoiceGatewayDropVoicePktsDuringEvents':wwpVoiceGatewayDropVoicePktsDuringEvents,'wwpVoiceGatewaySquelchInbandDtmfAudio':wwpVoiceGatewaySquelchInbandDtmfAudio,'wwpVoiceGatewayStats':wwpVoiceGatewayStats,'wwpVoiceGatewayPktsTx':wwpVoiceGatewayPktsTx,'wwpVoiceGatewayOctetsTx':wwpVoiceGatewayOctetsTx,'wwpVoiceGatewayPktsRx':wwpVoiceGatewayPktsRx,'wwpVoiceGatewayOctetsRx':wwpVoiceGatewayOctetsRx,'wwpVoiceGatewayPktsLost':wwpVoiceGatewayPktsLost,'wwpVoiceGatewayIntervalJitter':wwpVoiceGatewayIntervalJitter,'wwpVoiceGatewayLatency':wwpVoiceGatewayLatency,'wwpVoiceGatewayResetStatCounters':wwpVoiceGatewayResetStatCounters,'wwpVoiceReset':wwpVoiceReset,'wwpVoiceGatewayNumResets':wwpVoiceGatewayNumResets,'wwpVoiceGatewayReset':wwpVoiceGatewayReset,'wwpVoiceSec':wwpVoiceSec,'wwpVoiceAccess':wwpVoiceAccess,'wwpMgmtAccess':wwpMgmtAccess,'wwpVoiceGatewayConfigCallAgent':wwpVoiceGatewayConfigCallAgent,'wwpVoiceCallAgentOtaModes':wwpVoiceCallAgentOtaModes,'wwpVoiceCallAgentEgressEvent':wwpVoiceCallAgentEgressEvent,'wwpVoiceGatewayConfigPots':wwpVoiceGatewayConfigPots,'wwpVoiceCallAgentPotsLine':wwpVoiceCallAgentPotsLine,'wwpVoiceGatewayConfigFax':wwpVoiceGatewayConfigFax,'wwpVoiceAutonomousFaxState':wwpVoiceAutonomousFaxState,'wwpVoiceGatewayConfigEndPoint':wwpVoiceGatewayConfigEndPoint,'wwpVoiceEndPointName':wwpVoiceEndPointName,'wwpVoiceGatewayConfigNotifEntityCache':wwpVoiceGatewayConfigNotifEntityCache,'wwpVoiceNotifEntCache':wwpVoiceNotifEntCache,'wwpVoiceGatewayConfigJitterBuffer':wwpVoiceGatewayConfigJitterBuffer,'wwpVoiceJitterOptionState':wwpVoiceJitterOptionState,'wwpVoiceGatewayConfigJitterBufferMinPeriod':wwpVoiceGatewayConfigJitterBufferMinPeriod,'wwpVoiceJitterBufferMinPeriod':wwpVoiceJitterBufferMinPeriod,'wwpVoiceGatewayConfigJitterBufferMaxPeriod':wwpVoiceGatewayConfigJitterBufferMaxPeriod,'wwpVoiceJitterBufferMaxPeriod':wwpVoiceJitterBufferMaxPeriod,'wwpVoiceGatewayConfigJitterBufferTargetPeriod':wwpVoiceGatewayConfigJitterBufferTargetPeriod,'wwpVoiceJitterBufferTargetPeriod':wwpVoiceJitterBufferTargetPeriod,'wwpVoiceGatewayConfigCodecOverride':wwpVoiceGatewayConfigCodecOverride,'wwpVoiceGatewayCodecOverride':wwpVoiceGatewayCodecOverride,'wwpVoiceGatewayConfigTestServerConnection':wwpVoiceGatewayConfigTestServerConnection,'wwpVoiceGatewayTestServerConnection':wwpVoiceGatewayTestServerConnection,'wwpVoiceGatewayConfigLastServerResponseTime':wwpVoiceGatewayConfigLastServerResponseTime,'wwpVoiceGatewayLastServerResponseTime':wwpVoiceGatewayLastServerResponseTime,'wwpVoiceGatewaySIP':wwpVoiceGatewaySIP,'wwpVoiceGatewaySipSessionTimeoutPeriod':wwpVoiceGatewaySipSessionTimeoutPeriod,'wwpVoiceGatewaySipRegisterTimeoutPeriod':wwpVoiceGatewaySipRegisterTimeoutPeriod,'wwpVoiceGatewaySipForceQuotesState':wwpVoiceGatewaySipForceQuotesState,'wwpVoiceGatewaySipPhoneLineTable':wwpVoiceGatewaySipPhoneLineTable,'wwpVoiceGatewaySipPhoneLineEntry':wwpVoiceGatewaySipPhoneLineEntry,_Q:wwpVoiceGatewaySipLineId,'wwpVoiceGatewaySipPhoneNumber':wwpVoiceGatewaySipPhoneNumber,'wwpVoiceGatewaySipUserName':wwpVoiceGatewaySipUserName,'wwpVoiceGatewaySipUserDisplayName':wwpVoiceGatewaySipUserDisplayName,'wwpVoiceGatewaySipUserPassword':wwpVoiceGatewaySipUserPassword,'wwpVoiceGatewaySipDialPlan':wwpVoiceGatewaySipDialPlan,'wwpVoiceGatewaySipPhoneLineTimerTable':wwpVoiceGatewaySipPhoneLineTimerTable,'wwpVoiceGatewaySipPhoneLineTimerEntry':wwpVoiceGatewaySipPhoneLineTimerEntry,_R:wwpVoiceGatewaySipTimerLineId,'wwpVoiceGatewaySipDialTimerLong':wwpVoiceGatewaySipDialTimerLong,'wwpVoiceGatewaySIPServers':wwpVoiceGatewaySIPServers,'wwpVoiceGatewaySIPProxyServers':wwpVoiceGatewaySIPProxyServers,'wwpVoiceGatewaySipProxyAddr':wwpVoiceGatewaySipProxyAddr,'wwpVoiceGatewaySipProxyPort':wwpVoiceGatewaySipProxyPort,'wwpVoiceGatewaySIPRegistrarServers':wwpVoiceGatewaySIPRegistrarServers,'wwpVoiceGatewaySipRegistrarAddr':wwpVoiceGatewaySipRegistrarAddr,'wwpVoiceGatewaySipRegistrarPort':wwpVoiceGatewaySipRegistrarPort,'wwpVoiceGatewaySIPLogServers':wwpVoiceGatewaySIPLogServers,'wwpVoiceGatewaySipSyslogAddr':wwpVoiceGatewaySipSyslogAddr,'wwpVoiceGatewaySipSyslogPort':wwpVoiceGatewaySipSyslogPort,'wwpVoiceGatewaySipSyslogLogLevel':wwpVoiceGatewaySipSyslogLogLevel,'wwpVoiceGatewaySIPPreferredCodec':wwpVoiceGatewaySIPPreferredCodec,'wwpVoiceGatewaySIPDtmfEventHandling':wwpVoiceGatewaySIPDtmfEventHandling,'wwpVoiceGatewaySIPCallFeatures':wwpVoiceGatewaySIPCallFeatures,'wwpVoiceGatewayHookFlashEnable':wwpVoiceGatewayHookFlashEnable,'wwpVoiceGatewayConfigProtocolType':wwpVoiceGatewayConfigProtocolType,'wwpVoiceGatewayProtocolType':wwpVoiceGatewayProtocolType,'wwpVoiceGatewayConfigProtocolEnable':wwpVoiceGatewayConfigProtocolEnable,'wwpVoiceGatewayProtocolEnable':wwpVoiceGatewayProtocolEnable,'wwpVoiceGatewayMIBNotificationPrefix':wwpVoiceGatewayMIBNotificationPrefix,'wwpVoiceGatewayMIBNotifications':wwpVoiceGatewayMIBNotifications,'wwpVoiceGatewayMIBConformance':wwpVoiceGatewayMIBConformance,'wwpVoiceGatewayMIBCompliances':wwpVoiceGatewayMIBCompliances,'wwpVoiceGatewayMIBGroups':wwpVoiceGatewayMIBGroups})