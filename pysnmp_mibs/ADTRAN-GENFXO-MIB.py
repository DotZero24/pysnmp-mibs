_R='enabled'
_Q='adGenFxoInterfaceFxsIndex'
_P='ADTRAN-GENFXO-MIB'
_O='ringGround'
_N='inactive'
_M='active'
_L='milliseconds'
_K='DisplayString'
_J='disable'
_I='disabled'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='0.1dB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenFxo,adGenFxoID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenFxo','adGenFxoID')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndexOrZero',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention','TruthValue')
adGenFxoIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,38,1))
if mibBuilder.loadTexts:adGenFxoIdentity.setRevisions(('2018-04-04 00:00','2014-06-12 00:00','2012-08-22 00:00','2011-09-12 00:00','2011-02-08 00:00'))
class AdGenFxoInterfaceFxsLocation(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_AdGenFxoProvisioning_ObjectIdentity=ObjectIdentity
adGenFxoProvisioning=_AdGenFxoProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,1))
_AdGenFxoDeviceProv_ObjectIdentity=ObjectIdentity
adGenFxoDeviceProv=_AdGenFxoDeviceProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,1,1))
_AdGenFxoInterfaceProv_ObjectIdentity=ObjectIdentity
adGenFxoInterfaceProv=_AdGenFxoInterfaceProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,1,2))
_AdGenFxoInterfaceProvTable_Object=MibTable
adGenFxoInterfaceProvTable=_AdGenFxoInterfaceProvTable_Object((1,3,6,1,4,1,664,5,70,38,1,2,1))
if mibBuilder.loadTexts:adGenFxoInterfaceProvTable.setStatus(_A)
_AdGenFxoInterfaceProvEntry_Object=MibTableRow
adGenFxoInterfaceProvEntry=_AdGenFxoInterfaceProvEntry_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1))
adGenFxoInterfaceProvEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenFxoInterfaceProvEntry.setStatus(_A)
_AdGenFxoInterfaceLastErrorString_Type=DisplayString
_AdGenFxoInterfaceLastErrorString_Object=MibTableColumn
adGenFxoInterfaceLastErrorString=_AdGenFxoInterfaceLastErrorString_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,1),_AdGenFxoInterfaceLastErrorString_Type())
adGenFxoInterfaceLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoInterfaceLastErrorString.setStatus(_A)
class _AdGenFxoInterfaceSignalingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loopStart',1),('groundStart',2),('tr08sp',3),('tr08uvg',4)))
_AdGenFxoInterfaceSignalingMode_Type.__name__=_C
_AdGenFxoInterfaceSignalingMode_Object=MibTableColumn
adGenFxoInterfaceSignalingMode=_AdGenFxoInterfaceSignalingMode_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,2),_AdGenFxoInterfaceSignalingMode_Type())
adGenFxoInterfaceSignalingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceSignalingMode.setStatus(_A)
_AdGenFxoInterfaceTxGain_Type=Integer32
_AdGenFxoInterfaceTxGain_Object=MibTableColumn
adGenFxoInterfaceTxGain=_AdGenFxoInterfaceTxGain_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,3),_AdGenFxoInterfaceTxGain_Type())
adGenFxoInterfaceTxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceTxGain.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceTxGain.setUnits(_E)
_AdGenFxoInterfaceMinTxGain_Type=Integer32
_AdGenFxoInterfaceMinTxGain_Object=MibTableColumn
adGenFxoInterfaceMinTxGain=_AdGenFxoInterfaceMinTxGain_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,4),_AdGenFxoInterfaceMinTxGain_Type())
adGenFxoInterfaceMinTxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoInterfaceMinTxGain.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceMinTxGain.setUnits(_E)
_AdGenFxoInterfaceMaxTxGain_Type=Integer32
_AdGenFxoInterfaceMaxTxGain_Object=MibTableColumn
adGenFxoInterfaceMaxTxGain=_AdGenFxoInterfaceMaxTxGain_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,5),_AdGenFxoInterfaceMaxTxGain_Type())
adGenFxoInterfaceMaxTxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoInterfaceMaxTxGain.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceMaxTxGain.setUnits(_E)
_AdGenFxoInterfaceRxGain_Type=Integer32
_AdGenFxoInterfaceRxGain_Object=MibTableColumn
adGenFxoInterfaceRxGain=_AdGenFxoInterfaceRxGain_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,6),_AdGenFxoInterfaceRxGain_Type())
adGenFxoInterfaceRxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceRxGain.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceRxGain.setUnits(_E)
_AdGenFxoInterfaceMinRxGain_Type=Integer32
_AdGenFxoInterfaceMinRxGain_Object=MibTableColumn
adGenFxoInterfaceMinRxGain=_AdGenFxoInterfaceMinRxGain_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,7),_AdGenFxoInterfaceMinRxGain_Type())
adGenFxoInterfaceMinRxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoInterfaceMinRxGain.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceMinRxGain.setUnits(_E)
_AdGenFxoInterfaceMaxRxGain_Type=Integer32
_AdGenFxoInterfaceMaxRxGain_Object=MibTableColumn
adGenFxoInterfaceMaxRxGain=_AdGenFxoInterfaceMaxRxGain_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,8),_AdGenFxoInterfaceMaxRxGain_Type())
adGenFxoInterfaceMaxRxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoInterfaceMaxRxGain.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceMaxRxGain.setUnits(_E)
class _AdGenFxoInterfaceImpedance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('z600r',1),('z900z',2),('z1',3),('z2',4),('z3',5),('z4',6),('z5',7),('z6',8),('z7',9),('z8',10),('z9',11),('z10',12)))
_AdGenFxoInterfaceImpedance_Type.__name__=_C
_AdGenFxoInterfaceImpedance_Object=MibTableColumn
adGenFxoInterfaceImpedance=_AdGenFxoInterfaceImpedance_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,9),_AdGenFxoInterfaceImpedance_Type())
adGenFxoInterfaceImpedance.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceImpedance.setStatus(_A)
class _AdGenFxoInterfaceCWCIdAckGenDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AdGenFxoInterfaceCWCIdAckGenDelay_Type.__name__=_H
_AdGenFxoInterfaceCWCIdAckGenDelay_Object=MibTableColumn
adGenFxoInterfaceCWCIdAckGenDelay=_AdGenFxoInterfaceCWCIdAckGenDelay_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,10),_AdGenFxoInterfaceCWCIdAckGenDelay_Type())
adGenFxoInterfaceCWCIdAckGenDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceCWCIdAckGenDelay.setStatus(_A)
class _AdGenFxoInterfaceCWCIdAckGenEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_J,2)))
_AdGenFxoInterfaceCWCIdAckGenEnable_Type.__name__=_C
_AdGenFxoInterfaceCWCIdAckGenEnable_Object=MibTableColumn
adGenFxoInterfaceCWCIdAckGenEnable=_AdGenFxoInterfaceCWCIdAckGenEnable_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,11),_AdGenFxoInterfaceCWCIdAckGenEnable_Type())
adGenFxoInterfaceCWCIdAckGenEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceCWCIdAckGenEnable.setStatus(_A)
_AdGenFxoInterfaceTargetFxsLocation_Type=AdGenFxoInterfaceFxsLocation
_AdGenFxoInterfaceTargetFxsLocation_Object=MibTableColumn
adGenFxoInterfaceTargetFxsLocation=_AdGenFxoInterfaceTargetFxsLocation_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,12),_AdGenFxoInterfaceTargetFxsLocation_Type())
adGenFxoInterfaceTargetFxsLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceTargetFxsLocation.setStatus(_A)
class _AdGenFxoInterfaceRingTripMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('forced',2),('delayed',3)))
_AdGenFxoInterfaceRingTripMode_Type.__name__=_C
_AdGenFxoInterfaceRingTripMode_Object=MibTableColumn
adGenFxoInterfaceRingTripMode=_AdGenFxoInterfaceRingTripMode_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,13),_AdGenFxoInterfaceRingTripMode_Type())
adGenFxoInterfaceRingTripMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceRingTripMode.setStatus(_A)
class _AdGenFxoInterfaceRingTripDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,300))
_AdGenFxoInterfaceRingTripDuration_Type.__name__=_H
_AdGenFxoInterfaceRingTripDuration_Object=MibTableColumn
adGenFxoInterfaceRingTripDuration=_AdGenFxoInterfaceRingTripDuration_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,14),_AdGenFxoInterfaceRingTripDuration_Type())
adGenFxoInterfaceRingTripDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceRingTripDuration.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceRingTripDuration.setUnits(_L)
class _AdGenFxoInterfaceRingTripMuteInterval_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_AdGenFxoInterfaceRingTripMuteInterval_Type.__name__=_H
_AdGenFxoInterfaceRingTripMuteInterval_Object=MibTableColumn
adGenFxoInterfaceRingTripMuteInterval=_AdGenFxoInterfaceRingTripMuteInterval_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,15),_AdGenFxoInterfaceRingTripMuteInterval_Type())
adGenFxoInterfaceRingTripMuteInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInterfaceRingTripMuteInterval.setStatus(_A)
if mibBuilder.loadTexts:adGenFxoInterfaceRingTripMuteInterval.setUnits(_L)
class _AdGenFxoCircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenFxoCircuitIdentifier_Type.__name__=_K
_AdGenFxoCircuitIdentifier_Object=MibTableColumn
adGenFxoCircuitIdentifier=_AdGenFxoCircuitIdentifier_Object((1,3,6,1,4,1,664,5,70,38,1,2,1,1,16),_AdGenFxoCircuitIdentifier_Type())
adGenFxoCircuitIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoCircuitIdentifier.setStatus(_A)
_AdGenFxoStatus_ObjectIdentity=ObjectIdentity
adGenFxoStatus=_AdGenFxoStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,2))
_AdGenFxoDeviceStatus_ObjectIdentity=ObjectIdentity
adGenFxoDeviceStatus=_AdGenFxoDeviceStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,2,1))
_AdGenFxoInterfaceStatus_ObjectIdentity=ObjectIdentity
adGenFxoInterfaceStatus=_AdGenFxoInterfaceStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,2,2))
_AdGenFxoInterfaceStatusTable_Object=MibTable
adGenFxoInterfaceStatusTable=_AdGenFxoInterfaceStatusTable_Object((1,3,6,1,4,1,664,5,70,38,2,2,1))
if mibBuilder.loadTexts:adGenFxoInterfaceStatusTable.setStatus(_A)
_AdGenFxoInterfaceStatusEntry_Object=MibTableRow
adGenFxoInterfaceStatusEntry=_AdGenFxoInterfaceStatusEntry_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1))
adGenFxoInterfaceStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenFxoInterfaceStatusEntry.setStatus(_A)
class _AdGenFxoPortActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_I,3)))
_AdGenFxoPortActive_Type.__name__=_C
_AdGenFxoPortActive_Object=MibTableColumn
adGenFxoPortActive=_AdGenFxoPortActive_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,1),_AdGenFxoPortActive_Type())
adGenFxoPortActive.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoPortActive.setStatus(_A)
class _AdGenFxoLoopFeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('open',1),('closed',2),(_O,3)))
_AdGenFxoLoopFeed_Type.__name__=_C
_AdGenFxoLoopFeed_Object=MibTableColumn
adGenFxoLoopFeed=_AdGenFxoLoopFeed_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,2),_AdGenFxoLoopFeed_Type())
adGenFxoLoopFeed.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoLoopFeed.setStatus(_A)
class _AdGenFxoLoopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('lcf',1),('rlcf',2),('noBatt',3),('tipOpen',4),('ringing',5)))
_AdGenFxoLoopState_Type.__name__=_C
_AdGenFxoLoopState_Object=MibTableColumn
adGenFxoLoopState=_AdGenFxoLoopState_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,3),_AdGenFxoLoopState_Type())
adGenFxoLoopState.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoLoopState.setStatus(_A)
class _AdGenFxoTestActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_I,3)))
_AdGenFxoTestActive_Type.__name__=_C
_AdGenFxoTestActive_Object=MibTableColumn
adGenFxoTestActive=_AdGenFxoTestActive_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,4),_AdGenFxoTestActive_Type())
adGenFxoTestActive.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoTestActive.setStatus(_A)
_AdGenFxoRxVoicePackets_Type=Unsigned32
_AdGenFxoRxVoicePackets_Object=MibTableColumn
adGenFxoRxVoicePackets=_AdGenFxoRxVoicePackets_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,5),_AdGenFxoRxVoicePackets_Type())
adGenFxoRxVoicePackets.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoRxVoicePackets.setStatus(_A)
_AdGenFxoRxControlPackets_Type=Unsigned32
_AdGenFxoRxControlPackets_Object=MibTableColumn
adGenFxoRxControlPackets=_AdGenFxoRxControlPackets_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,6),_AdGenFxoRxControlPackets_Type())
adGenFxoRxControlPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoRxControlPackets.setStatus(_A)
_AdGenFxoTxVoicePackets_Type=Unsigned32
_AdGenFxoTxVoicePackets_Object=MibTableColumn
adGenFxoTxVoicePackets=_AdGenFxoTxVoicePackets_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,7),_AdGenFxoTxVoicePackets_Type())
adGenFxoTxVoicePackets.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoTxVoicePackets.setStatus(_A)
_AdGenFxoTxControlPackets_Type=Unsigned32
_AdGenFxoTxControlPackets_Object=MibTableColumn
adGenFxoTxControlPackets=_AdGenFxoTxControlPackets_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,8),_AdGenFxoTxControlPackets_Type())
adGenFxoTxControlPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoTxControlPackets.setStatus(_A)
class _AdGenFxoClearPortCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_AdGenFxoClearPortCounters_Type.__name__=_C
_AdGenFxoClearPortCounters_Object=MibTableColumn
adGenFxoClearPortCounters=_AdGenFxoClearPortCounters_Object((1,3,6,1,4,1,664,5,70,38,2,2,1,1,9),_AdGenFxoClearPortCounters_Type())
adGenFxoClearPortCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoClearPortCounters.setStatus(_A)
_AdGenFxoFindFxsMap_ObjectIdentity=ObjectIdentity
adGenFxoFindFxsMap=_AdGenFxoFindFxsMap_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,2,3))
_AdGenFxoFindFxsMapTable_Object=MibTable
adGenFxoFindFxsMapTable=_AdGenFxoFindFxsMapTable_Object((1,3,6,1,4,1,664,5,70,38,2,3,1))
if mibBuilder.loadTexts:adGenFxoFindFxsMapTable.setStatus(_A)
_AdGenFxoFindFxsMapEntry_Object=MibTableRow
adGenFxoFindFxsMapEntry=_AdGenFxoFindFxsMapEntry_Object((1,3,6,1,4,1,664,5,70,38,2,3,1,1))
adGenFxoFindFxsMapEntry.setIndexNames((0,_F,_G),(1,_P,_Q))
if mibBuilder.loadTexts:adGenFxoFindFxsMapEntry.setStatus(_A)
_AdGenFxoInterfaceFxsIndex_Type=AdGenFxoInterfaceFxsLocation
_AdGenFxoInterfaceFxsIndex_Object=MibTableColumn
adGenFxoInterfaceFxsIndex=_AdGenFxoInterfaceFxsIndex_Object((1,3,6,1,4,1,664,5,70,38,2,3,1,1,1),_AdGenFxoInterfaceFxsIndex_Type())
adGenFxoInterfaceFxsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenFxoInterfaceFxsIndex.setStatus(_A)
_AdGenFxoInterfaceFound_Type=InterfaceIndexOrZero
_AdGenFxoInterfaceFound_Object=MibTableColumn
adGenFxoInterfaceFound=_AdGenFxoInterfaceFound_Object((1,3,6,1,4,1,664,5,70,38,2,3,1,1,2),_AdGenFxoInterfaceFound_Type())
adGenFxoInterfaceFound.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFxoInterfaceFound.setStatus(_A)
_AdGenFxoTest_ObjectIdentity=ObjectIdentity
adGenFxoTest=_AdGenFxoTest_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,3))
_AdGenFxoDeviceTests_ObjectIdentity=ObjectIdentity
adGenFxoDeviceTests=_AdGenFxoDeviceTests_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,3,1))
_AdGenFxoInterfaceTests_ObjectIdentity=ObjectIdentity
adGenFxoInterfaceTests=_AdGenFxoInterfaceTests_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,3,2))
_AdGenFxoInterfaceTestsTable_Object=MibTable
adGenFxoInterfaceTestsTable=_AdGenFxoInterfaceTestsTable_Object((1,3,6,1,4,1,664,5,70,38,3,2,1))
if mibBuilder.loadTexts:adGenFxoInterfaceTestsTable.setStatus(_A)
_AdGenFxoInterfaceTestsEntry_Object=MibTableRow
adGenFxoInterfaceTestsEntry=_AdGenFxoInterfaceTestsEntry_Object((1,3,6,1,4,1,664,5,70,38,3,2,1,1))
adGenFxoInterfaceTestsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenFxoInterfaceTestsEntry.setStatus(_A)
class _AdGenFxoPortClearTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_AdGenFxoPortClearTest_Type.__name__=_C
_AdGenFxoPortClearTest_Object=MibTableColumn
adGenFxoPortClearTest=_AdGenFxoPortClearTest_Object((1,3,6,1,4,1,664,5,70,38,3,2,1,1,1),_AdGenFxoPortClearTest_Type())
adGenFxoPortClearTest.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoPortClearTest.setStatus(_A)
class _AdGenFxo1004HzToneTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('near',1),('far',2),(_J,3)))
_AdGenFxo1004HzToneTest_Type.__name__=_C
_AdGenFxo1004HzToneTest_Object=MibTableColumn
adGenFxo1004HzToneTest=_AdGenFxo1004HzToneTest_Object((1,3,6,1,4,1,664,5,70,38,3,2,1,1,2),_AdGenFxo1004HzToneTest_Type())
adGenFxo1004HzToneTest.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxo1004HzToneTest.setStatus(_A)
class _AdGenFxoLoopStateTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('open',2),('close',3),(_O,4)))
_AdGenFxoLoopStateTest_Type.__name__=_C
_AdGenFxoLoopStateTest_Object=MibTableColumn
adGenFxoLoopStateTest=_AdGenFxoLoopStateTest_Object((1,3,6,1,4,1,664,5,70,38,3,2,1,1,3),_AdGenFxoLoopStateTest_Type())
adGenFxoLoopStateTest.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoLoopStateTest.setStatus(_A)
class _AdGenFxoInwardLoopbackTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_I,2)))
_AdGenFxoInwardLoopbackTest_Type.__name__=_C
_AdGenFxoInwardLoopbackTest_Object=MibTableColumn
adGenFxoInwardLoopbackTest=_AdGenFxoInwardLoopbackTest_Object((1,3,6,1,4,1,664,5,70,38,3,2,1,1,4),_AdGenFxoInwardLoopbackTest_Type())
adGenFxoInwardLoopbackTest.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoInwardLoopbackTest.setStatus(_A)
class _AdGenFxoOutwardLoopbackTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_I,2)))
_AdGenFxoOutwardLoopbackTest_Type.__name__=_C
_AdGenFxoOutwardLoopbackTest_Object=MibTableColumn
adGenFxoOutwardLoopbackTest=_AdGenFxoOutwardLoopbackTest_Object((1,3,6,1,4,1,664,5,70,38,3,2,1,1,5),_AdGenFxoOutwardLoopbackTest_Type())
adGenFxoOutwardLoopbackTest.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFxoOutwardLoopbackTest.setStatus(_A)
_AdGenFxoAlarms_ObjectIdentity=ObjectIdentity
adGenFxoAlarms=_AdGenFxoAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,70,38,4))
mibBuilder.exportSymbols(_P,**{'AdGenFxoInterfaceFxsLocation':AdGenFxoInterfaceFxsLocation,'adGenFxoProvisioning':adGenFxoProvisioning,'adGenFxoDeviceProv':adGenFxoDeviceProv,'adGenFxoInterfaceProv':adGenFxoInterfaceProv,'adGenFxoInterfaceProvTable':adGenFxoInterfaceProvTable,'adGenFxoInterfaceProvEntry':adGenFxoInterfaceProvEntry,'adGenFxoInterfaceLastErrorString':adGenFxoInterfaceLastErrorString,'adGenFxoInterfaceSignalingMode':adGenFxoInterfaceSignalingMode,'adGenFxoInterfaceTxGain':adGenFxoInterfaceTxGain,'adGenFxoInterfaceMinTxGain':adGenFxoInterfaceMinTxGain,'adGenFxoInterfaceMaxTxGain':adGenFxoInterfaceMaxTxGain,'adGenFxoInterfaceRxGain':adGenFxoInterfaceRxGain,'adGenFxoInterfaceMinRxGain':adGenFxoInterfaceMinRxGain,'adGenFxoInterfaceMaxRxGain':adGenFxoInterfaceMaxRxGain,'adGenFxoInterfaceImpedance':adGenFxoInterfaceImpedance,'adGenFxoInterfaceCWCIdAckGenDelay':adGenFxoInterfaceCWCIdAckGenDelay,'adGenFxoInterfaceCWCIdAckGenEnable':adGenFxoInterfaceCWCIdAckGenEnable,'adGenFxoInterfaceTargetFxsLocation':adGenFxoInterfaceTargetFxsLocation,'adGenFxoInterfaceRingTripMode':adGenFxoInterfaceRingTripMode,'adGenFxoInterfaceRingTripDuration':adGenFxoInterfaceRingTripDuration,'adGenFxoInterfaceRingTripMuteInterval':adGenFxoInterfaceRingTripMuteInterval,'adGenFxoCircuitIdentifier':adGenFxoCircuitIdentifier,'adGenFxoStatus':adGenFxoStatus,'adGenFxoDeviceStatus':adGenFxoDeviceStatus,'adGenFxoInterfaceStatus':adGenFxoInterfaceStatus,'adGenFxoInterfaceStatusTable':adGenFxoInterfaceStatusTable,'adGenFxoInterfaceStatusEntry':adGenFxoInterfaceStatusEntry,'adGenFxoPortActive':adGenFxoPortActive,'adGenFxoLoopFeed':adGenFxoLoopFeed,'adGenFxoLoopState':adGenFxoLoopState,'adGenFxoTestActive':adGenFxoTestActive,'adGenFxoRxVoicePackets':adGenFxoRxVoicePackets,'adGenFxoRxControlPackets':adGenFxoRxControlPackets,'adGenFxoTxVoicePackets':adGenFxoTxVoicePackets,'adGenFxoTxControlPackets':adGenFxoTxControlPackets,'adGenFxoClearPortCounters':adGenFxoClearPortCounters,'adGenFxoFindFxsMap':adGenFxoFindFxsMap,'adGenFxoFindFxsMapTable':adGenFxoFindFxsMapTable,'adGenFxoFindFxsMapEntry':adGenFxoFindFxsMapEntry,_Q:adGenFxoInterfaceFxsIndex,'adGenFxoInterfaceFound':adGenFxoInterfaceFound,'adGenFxoTest':adGenFxoTest,'adGenFxoDeviceTests':adGenFxoDeviceTests,'adGenFxoInterfaceTests':adGenFxoInterfaceTests,'adGenFxoInterfaceTestsTable':adGenFxoInterfaceTestsTable,'adGenFxoInterfaceTestsEntry':adGenFxoInterfaceTestsEntry,'adGenFxoPortClearTest':adGenFxoPortClearTest,'adGenFxo1004HzToneTest':adGenFxo1004HzToneTest,'adGenFxoLoopStateTest':adGenFxoLoopStateTest,'adGenFxoInwardLoopbackTest':adGenFxoInwardLoopbackTest,'adGenFxoOutwardLoopbackTest':adGenFxoOutwardLoopbackTest,'adGenFxoAlarms':adGenFxoAlarms,'adGenFxoIdentity':adGenFxoIdentity})