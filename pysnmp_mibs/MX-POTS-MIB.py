_X='fxoLinkStateId'
_W='fxoCustomBasicParametersId'
_V='fxoIncomingCallBehaviorId'
_U='fxoAnsweringDelayId'
_T='countryTone'
_S='fxsCallerIdId'
_R='fxsDistinctiveRingIndex'
_Q='fxsSpecificMessageWaitingIndicatorId'
_P='toneAndVisual'
_O='visual'
_N='fxsBypassId'
_M='country'
_L='lineId'
_K='MxDigitMap'
_J='disabled'
_I='disable'
_H='OctetString'
_G='MX-POTS-MIB'
_F='MxEnableState'
_E='read-only'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort',_K,_F,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
potsMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800))
_PotsMIBObjects_ObjectIdentity=ObjectIdentity
potsMIBObjects=_PotsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1))
_LineTable_Object=MibTable
lineTable=_LineTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,100))
if mibBuilder.loadTexts:lineTable.setStatus(_A)
_LineEntry_Object=MibTableRow
lineEntry=_LineEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,100,1))
lineEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:lineEntry.setStatus(_A)
_LineId_Type=OctetString
_LineId_Object=MibTableColumn
lineId=_LineId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,100,1,100),_LineId_Type())
lineId.setMaxAccess(_E)
if mibBuilder.loadTexts:lineId.setStatus(_A)
class _LineTypeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('fxs',100),('fxo',200)))
_LineTypeStatus_Type.__name__=_C
_LineTypeStatus_Object=MibTableColumn
lineTypeStatus=_LineTypeStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,100,1,200),_LineTypeStatus_Type())
lineTypeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lineTypeStatus.setStatus(_A)
class _LineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('idle',100),('inUse',200),(_J,300),('bypass',400),('down',500)))
_LineState_Type.__name__=_C
_LineState_Object=MibTableColumn
lineState=_LineState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,100,1,300),_LineState_Type())
lineState.setMaxAccess(_E)
if mibBuilder.loadTexts:lineState.setStatus(_A)
class _CallerIdCustomization_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_M,100),('etsiDtmf',200),('etsiFsk',300)))
_CallerIdCustomization_Type.__name__=_C
_CallerIdCustomization_Object=MibScalar
callerIdCustomization=_CallerIdCustomization_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,200),_CallerIdCustomization_Type())
callerIdCustomization.setMaxAccess(_B)
if mibBuilder.loadTexts:callerIdCustomization.setStatus(_A)
class _DtmfMapDigitDetection_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('whenPressed',100),('whenReleased',200)))
_DtmfMapDigitDetection_Type.__name__=_C
_DtmfMapDigitDetection_Object=MibScalar
dtmfMapDigitDetection=_DtmfMapDigitDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,300),_DtmfMapDigitDetection_Type())
dtmfMapDigitDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmfMapDigitDetection.setStatus(_A)
class _VocalUnitInformation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('none',100),('all',200)))
_VocalUnitInformation_Type.__name__=_C
_VocalUnitInformation_Object=MibScalar
vocalUnitInformation=_VocalUnitInformation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,400),_VocalUnitInformation_Type())
vocalUnitInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:vocalUnitInformation.setStatus(_A)
class _CallerIdTransmission_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700)));namedValues=NamedValues(*((_M,100),('firstRing',200),('ringPulse',300),('lineReversalRingPulse',400),('dtAs',500),('lineReversalDtAs',600),('noRingPulse',700)))
_CallerIdTransmission_Type.__name__=_C
_CallerIdTransmission_Object=MibScalar
callerIdTransmission=_CallerIdTransmission_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,500),_CallerIdTransmission_Type())
callerIdTransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:callerIdTransmission.setStatus(_A)
_FxsGroup_ObjectIdentity=ObjectIdentity
fxsGroup=_FxsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000))
class _FxsLineSupervisionMode_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('none',100),('dropOnDisconnect',200),('reversalOnIdle',300),('reversalOnEstablished',400)))
_FxsLineSupervisionMode_Type.__name__=_C
_FxsLineSupervisionMode_Object=MibScalar
fxsLineSupervisionMode=_FxsLineSupervisionMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,100),_FxsLineSupervisionMode_Type())
fxsLineSupervisionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsLineSupervisionMode.setStatus(_A)
class _FxsDisconnectDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_FxsDisconnectDelay_Type.__name__=_D
_FxsDisconnectDelay_Object=MibScalar
fxsDisconnectDelay=_FxsDisconnectDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,200),_FxsDisconnectDelay_Type())
fxsDisconnectDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsDisconnectDelay.setStatus(_A)
class _FxsInbandRingback_Type(MxEnableState):defaultValue=0
_FxsInbandRingback_Type.__name__=_F
_FxsInbandRingback_Object=MibScalar
fxsInbandRingback=_FxsInbandRingback_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,300),_FxsInbandRingback_Type())
fxsInbandRingback.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsInbandRingback.setStatus(_A)
class _FxsShutdownBehavior_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('disabledTone',100),('powerDrop',200)))
_FxsShutdownBehavior_Type.__name__=_C
_FxsShutdownBehavior_Object=MibScalar
fxsShutdownBehavior=_FxsShutdownBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,400),_FxsShutdownBehavior_Type())
fxsShutdownBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsShutdownBehavior.setStatus(_A)
class _FxsPowerDropOnDisconnectDuration_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_FxsPowerDropOnDisconnectDuration_Type.__name__=_D
_FxsPowerDropOnDisconnectDuration_Object=MibScalar
fxsPowerDropOnDisconnectDuration=_FxsPowerDropOnDisconnectDuration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,500),_FxsPowerDropOnDisconnectDuration_Type())
fxsPowerDropOnDisconnectDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsPowerDropOnDisconnectDuration.setStatus(_A)
class _FxsServiceActivation_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('flashHook',100),('flashHookAndDigit',200)))
_FxsServiceActivation_Type.__name__=_C
_FxsServiceActivation_Object=MibScalar
fxsServiceActivation=_FxsServiceActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,600),_FxsServiceActivation_Type())
fxsServiceActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsServiceActivation.setStatus(_A)
class _FxsCallerIdPrivateCallingPartyName_Type(OctetString):defaultValue=OctetString('Anonymous');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_FxsCallerIdPrivateCallingPartyName_Type.__name__=_H
_FxsCallerIdPrivateCallingPartyName_Object=MibScalar
fxsCallerIdPrivateCallingPartyName=_FxsCallerIdPrivateCallingPartyName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,700),_FxsCallerIdPrivateCallingPartyName_Type())
fxsCallerIdPrivateCallingPartyName.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsCallerIdPrivateCallingPartyName.setStatus(_A)
class _FxsSipMessageAlertingEnable_Type(MxEnableState):defaultValue=0
_FxsSipMessageAlertingEnable_Type.__name__=_F
_FxsSipMessageAlertingEnable_Object=MibScalar
fxsSipMessageAlertingEnable=_FxsSipMessageAlertingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,800),_FxsSipMessageAlertingEnable_Type())
fxsSipMessageAlertingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsSipMessageAlertingEnable.setStatus(_A)
_FxsCountryCustomizationGroup_ObjectIdentity=ObjectIdentity
fxsCountryCustomizationGroup=_FxsCountryCustomizationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10000))
class _FxsCountryCustomizationOverride_Type(MxEnableState):defaultValue=0
_FxsCountryCustomizationOverride_Type.__name__=_F
_FxsCountryCustomizationOverride_Object=MibScalar
fxsCountryCustomizationOverride=_FxsCountryCustomizationOverride_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10000,100),_FxsCountryCustomizationOverride_Type())
fxsCountryCustomizationOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsCountryCustomizationOverride.setStatus(_A)
class _FxsCountryCustomizationLoopCurrent_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,32))
_FxsCountryCustomizationLoopCurrent_Type.__name__=_D
_FxsCountryCustomizationLoopCurrent_Object=MibScalar
fxsCountryCustomizationLoopCurrent=_FxsCountryCustomizationLoopCurrent_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10000,200),_FxsCountryCustomizationLoopCurrent_Type())
fxsCountryCustomizationLoopCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsCountryCustomizationLoopCurrent.setStatus(_A)
class _FxsCountryCustomizationFlashHookDetectionRange_Type(OctetString):defaultValue=OctetString('100-1200');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,9))
_FxsCountryCustomizationFlashHookDetectionRange_Type.__name__=_H
_FxsCountryCustomizationFlashHookDetectionRange_Object=MibScalar
fxsCountryCustomizationFlashHookDetectionRange=_FxsCountryCustomizationFlashHookDetectionRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10000,300),_FxsCountryCustomizationFlashHookDetectionRange_Type())
fxsCountryCustomizationFlashHookDetectionRange.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsCountryCustomizationFlashHookDetectionRange.setStatus(_A)
_FxsBypassGroup_ObjectIdentity=ObjectIdentity
fxsBypassGroup=_FxsBypassGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10100))
_FxsBypassTable_Object=MibTable
fxsBypassTable=_FxsBypassTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10100,1000))
if mibBuilder.loadTexts:fxsBypassTable.setStatus(_A)
_FxsBypassEntry_Object=MibTableRow
fxsBypassEntry=_FxsBypassEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10100,1000,1))
fxsBypassEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:fxsBypassEntry.setStatus(_A)
_FxsBypassId_Type=OctetString
_FxsBypassId_Object=MibTableColumn
fxsBypassId=_FxsBypassId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10100,1000,1,100),_FxsBypassId_Type())
fxsBypassId.setMaxAccess(_E)
if mibBuilder.loadTexts:fxsBypassId.setStatus(_A)
class _FxsBypassActivation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('powerOff',100),('endpointDisabled',200),('onDemand',300)))
_FxsBypassActivation_Type.__name__=_C
_FxsBypassActivation_Object=MibTableColumn
fxsBypassActivation=_FxsBypassActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10100,1000,1,200),_FxsBypassActivation_Type())
fxsBypassActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsBypassActivation.setStatus(_A)
class _FxsBypassActivationDtmfMap_Type(MxDigitMap):defaultValue=OctetString('')
_FxsBypassActivationDtmfMap_Type.__name__=_K
_FxsBypassActivationDtmfMap_Object=MibTableColumn
fxsBypassActivationDtmfMap=_FxsBypassActivationDtmfMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10100,1000,1,300),_FxsBypassActivationDtmfMap_Type())
fxsBypassActivationDtmfMap.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsBypassActivationDtmfMap.setStatus(_A)
class _FxsBypassDeactivationTimeout_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FxsBypassDeactivationTimeout_Type.__name__=_D
_FxsBypassDeactivationTimeout_Object=MibTableColumn
fxsBypassDeactivationTimeout=_FxsBypassDeactivationTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10100,1000,1,400),_FxsBypassDeactivationTimeout_Type())
fxsBypassDeactivationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsBypassDeactivationTimeout.setStatus(_A)
_FxsMessageWaitingIndicatorGroup_ObjectIdentity=ObjectIdentity
fxsMessageWaitingIndicatorGroup=_FxsMessageWaitingIndicatorGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200))
class _FxsDefaultMessageWaitingIndicatorActivation_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_J,100),('tone',200),(_O,300),(_P,400)))
_FxsDefaultMessageWaitingIndicatorActivation_Type.__name__=_C
_FxsDefaultMessageWaitingIndicatorActivation_Object=MibScalar
fxsDefaultMessageWaitingIndicatorActivation=_FxsDefaultMessageWaitingIndicatorActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200,100),_FxsDefaultMessageWaitingIndicatorActivation_Type())
fxsDefaultMessageWaitingIndicatorActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsDefaultMessageWaitingIndicatorActivation.setStatus(_A)
class _FxsDefaultVisualMessageWaitingIndicatorType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('fsk',100),('fskAndVoltage',200)))
_FxsDefaultVisualMessageWaitingIndicatorType_Type.__name__=_C
_FxsDefaultVisualMessageWaitingIndicatorType_Object=MibScalar
fxsDefaultVisualMessageWaitingIndicatorType=_FxsDefaultVisualMessageWaitingIndicatorType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200,150),_FxsDefaultVisualMessageWaitingIndicatorType_Type())
fxsDefaultVisualMessageWaitingIndicatorType.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsDefaultVisualMessageWaitingIndicatorType.setStatus(_A)
_FxsSpecificMessageWaitingIndicatorTable_Object=MibTable
fxsSpecificMessageWaitingIndicatorTable=_FxsSpecificMessageWaitingIndicatorTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200,200))
if mibBuilder.loadTexts:fxsSpecificMessageWaitingIndicatorTable.setStatus(_A)
_FxsSpecificMessageWaitingIndicatorEntry_Object=MibTableRow
fxsSpecificMessageWaitingIndicatorEntry=_FxsSpecificMessageWaitingIndicatorEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200,200,1))
fxsSpecificMessageWaitingIndicatorEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:fxsSpecificMessageWaitingIndicatorEntry.setStatus(_A)
_FxsSpecificMessageWaitingIndicatorId_Type=OctetString
_FxsSpecificMessageWaitingIndicatorId_Object=MibTableColumn
fxsSpecificMessageWaitingIndicatorId=_FxsSpecificMessageWaitingIndicatorId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200,200,1,100),_FxsSpecificMessageWaitingIndicatorId_Type())
fxsSpecificMessageWaitingIndicatorId.setMaxAccess(_E)
if mibBuilder.loadTexts:fxsSpecificMessageWaitingIndicatorId.setStatus(_A)
class _FxsSpecificMessageWaitingIndicatorEnableConfig_Type(MxEnableState):defaultValue=0
_FxsSpecificMessageWaitingIndicatorEnableConfig_Type.__name__=_F
_FxsSpecificMessageWaitingIndicatorEnableConfig_Object=MibTableColumn
fxsSpecificMessageWaitingIndicatorEnableConfig=_FxsSpecificMessageWaitingIndicatorEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200,200,1,200),_FxsSpecificMessageWaitingIndicatorEnableConfig_Type())
fxsSpecificMessageWaitingIndicatorEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsSpecificMessageWaitingIndicatorEnableConfig.setStatus(_A)
class _FxsSpecificMessageWaitingIndicatorActivation_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_J,100),('tone',200),(_O,300),(_P,400)))
_FxsSpecificMessageWaitingIndicatorActivation_Type.__name__=_C
_FxsSpecificMessageWaitingIndicatorActivation_Object=MibTableColumn
fxsSpecificMessageWaitingIndicatorActivation=_FxsSpecificMessageWaitingIndicatorActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10200,200,1,300),_FxsSpecificMessageWaitingIndicatorActivation_Type())
fxsSpecificMessageWaitingIndicatorActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsSpecificMessageWaitingIndicatorActivation.setStatus(_A)
_FxsCallGroup_ObjectIdentity=ObjectIdentity
fxsCallGroup=_FxsCallGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10300))
class _FxsDefaultAutoCancelTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_FxsDefaultAutoCancelTimeout_Type.__name__=_D
_FxsDefaultAutoCancelTimeout_Object=MibScalar
fxsDefaultAutoCancelTimeout=_FxsDefaultAutoCancelTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10300,100),_FxsDefaultAutoCancelTimeout_Type())
fxsDefaultAutoCancelTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsDefaultAutoCancelTimeout.setStatus(_A)
_FxsEmergencyCallGroup_ObjectIdentity=ObjectIdentity
fxsEmergencyCallGroup=_FxsEmergencyCallGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10400))
class _FxsEmergencyCallOverride_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('noOverride',100),('noServices',200),('noDisconnect',300)))
_FxsEmergencyCallOverride_Type.__name__=_C
_FxsEmergencyCallOverride_Object=MibScalar
fxsEmergencyCallOverride=_FxsEmergencyCallOverride_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10400,100),_FxsEmergencyCallOverride_Type())
fxsEmergencyCallOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsEmergencyCallOverride.setStatus(_A)
class _FxsEmergencyRingTimeout_Type(Unsigned32):defaultValue=2000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180000))
_FxsEmergencyRingTimeout_Type.__name__=_D
_FxsEmergencyRingTimeout_Object=MibScalar
fxsEmergencyRingTimeout=_FxsEmergencyRingTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10400,200),_FxsEmergencyRingTimeout_Type())
fxsEmergencyRingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsEmergencyRingTimeout.setStatus(_A)
_FxsRingGroup_ObjectIdentity=ObjectIdentity
fxsRingGroup=_FxsRingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10500))
_FxsDistinctiveRingTable_Object=MibTable
fxsDistinctiveRingTable=_FxsDistinctiveRingTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10500,100))
if mibBuilder.loadTexts:fxsDistinctiveRingTable.setStatus(_A)
_FxsDistinctiveRingEntry_Object=MibTableRow
fxsDistinctiveRingEntry=_FxsDistinctiveRingEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10500,100,1))
fxsDistinctiveRingEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:fxsDistinctiveRingEntry.setStatus(_A)
class _FxsDistinctiveRingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FxsDistinctiveRingIndex_Type.__name__=_D
_FxsDistinctiveRingIndex_Object=MibTableColumn
fxsDistinctiveRingIndex=_FxsDistinctiveRingIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10500,100,1,100),_FxsDistinctiveRingIndex_Type())
fxsDistinctiveRingIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fxsDistinctiveRingIndex.setStatus(_A)
class _FxsDistinctiveRingRingId_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FxsDistinctiveRingRingId_Type.__name__=_H
_FxsDistinctiveRingRingId_Object=MibTableColumn
fxsDistinctiveRingRingId=_FxsDistinctiveRingRingId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10500,100,1,200),_FxsDistinctiveRingRingId_Type())
fxsDistinctiveRingRingId.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsDistinctiveRingRingId.setStatus(_A)
class _FxsDistinctiveRingPattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FxsDistinctiveRingPattern_Type.__name__=_H
_FxsDistinctiveRingPattern_Object=MibTableColumn
fxsDistinctiveRingPattern=_FxsDistinctiveRingPattern_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10500,100,1,300),_FxsDistinctiveRingPattern_Type())
fxsDistinctiveRingPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsDistinctiveRingPattern.setStatus(_A)
_FxsCallerIdGroup_ObjectIdentity=ObjectIdentity
fxsCallerIdGroup=_FxsCallerIdGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10600))
_FxsCallerIdTable_Object=MibTable
fxsCallerIdTable=_FxsCallerIdTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10600,100))
if mibBuilder.loadTexts:fxsCallerIdTable.setStatus(_A)
_FxsCallerIdEntry_Object=MibTableRow
fxsCallerIdEntry=_FxsCallerIdEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10600,100,1))
fxsCallerIdEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:fxsCallerIdEntry.setStatus(_A)
_FxsCallerIdId_Type=OctetString
_FxsCallerIdId_Object=MibTableColumn
fxsCallerIdId=_FxsCallerIdId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10600,100,1,150),_FxsCallerIdId_Type())
fxsCallerIdId.setMaxAccess(_E)
if mibBuilder.loadTexts:fxsCallerIdId.setStatus(_A)
class _FxsCallerIdActivation_Type(MxEnableState):defaultValue=1
_FxsCallerIdActivation_Type.__name__=_F
_FxsCallerIdActivation_Object=MibTableColumn
fxsCallerIdActivation=_FxsCallerIdActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,10600,100,1,300),_FxsCallerIdActivation_Type())
fxsCallerIdActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsCallerIdActivation.setStatus(_A)
_FxsInteropGroup_ObjectIdentity=ObjectIdentity
fxsInteropGroup=_FxsInteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,50000))
class _FxsInteropPlayLocalRingbackWhenNoMediaStream_Type(MxEnableState):defaultValue=0
_FxsInteropPlayLocalRingbackWhenNoMediaStream_Type.__name__=_F
_FxsInteropPlayLocalRingbackWhenNoMediaStream_Object=MibScalar
fxsInteropPlayLocalRingbackWhenNoMediaStream=_FxsInteropPlayLocalRingbackWhenNoMediaStream_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,10000,50000,100),_FxsInteropPlayLocalRingbackWhenNoMediaStream_Type())
fxsInteropPlayLocalRingbackWhenNoMediaStream.setMaxAccess(_B)
if mibBuilder.loadTexts:fxsInteropPlayLocalRingbackWhenNoMediaStream.setStatus(_A)
_FxoGroup_ObjectIdentity=ObjectIdentity
fxoGroup=_FxoGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000))
class _FxoPreDialDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_FxoPreDialDelay_Type.__name__=_D
_FxoPreDialDelay_Object=MibScalar
fxoPreDialDelay=_FxoPreDialDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,100),_FxoPreDialDelay_Type())
fxoPreDialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoPreDialDelay.setStatus(_A)
class _FxoDialToneDetectionMode_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_I,100),(_T,200)))
_FxoDialToneDetectionMode_Type.__name__=_C
_FxoDialToneDetectionMode_Object=MibScalar
fxoDialToneDetectionMode=_FxoDialToneDetectionMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,200),_FxoDialToneDetectionMode_Type())
fxoDialToneDetectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoDialToneDetectionMode.setStatus(_A)
class _FxoDialToneDetectionTimeout_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1300,10000))
_FxoDialToneDetectionTimeout_Type.__name__=_D
_FxoDialToneDetectionTimeout_Object=MibScalar
fxoDialToneDetectionTimeout=_FxoDialToneDetectionTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,300),_FxoDialToneDetectionTimeout_Type())
fxoDialToneDetectionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoDialToneDetectionTimeout.setStatus(_A)
_FxoAnsweringDelayTable_Object=MibTable
fxoAnsweringDelayTable=_FxoAnsweringDelayTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5000))
if mibBuilder.loadTexts:fxoAnsweringDelayTable.setStatus(_A)
_FxoAnsweringDelayEntry_Object=MibTableRow
fxoAnsweringDelayEntry=_FxoAnsweringDelayEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5000,1))
fxoAnsweringDelayEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:fxoAnsweringDelayEntry.setStatus(_A)
_FxoAnsweringDelayId_Type=OctetString
_FxoAnsweringDelayId_Object=MibTableColumn
fxoAnsweringDelayId=_FxoAnsweringDelayId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5000,1,100),_FxoAnsweringDelayId_Type())
fxoAnsweringDelayId.setMaxAccess(_E)
if mibBuilder.loadTexts:fxoAnsweringDelayId.setStatus(_A)
class _FxoAnsweringDelayWaitBeforeAnsweringDelay_Type(Unsigned32):defaultValue=8000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_FxoAnsweringDelayWaitBeforeAnsweringDelay_Type.__name__=_D
_FxoAnsweringDelayWaitBeforeAnsweringDelay_Object=MibTableColumn
fxoAnsweringDelayWaitBeforeAnsweringDelay=_FxoAnsweringDelayWaitBeforeAnsweringDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5000,1,200),_FxoAnsweringDelayWaitBeforeAnsweringDelay_Type())
fxoAnsweringDelayWaitBeforeAnsweringDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoAnsweringDelayWaitBeforeAnsweringDelay.setStatus(_A)
class _FxoAnsweringDelayAnsweringOnCallerIdDetection_Type(MxEnableState):defaultValue=1
_FxoAnsweringDelayAnsweringOnCallerIdDetection_Type.__name__=_F
_FxoAnsweringDelayAnsweringOnCallerIdDetection_Object=MibTableColumn
fxoAnsweringDelayAnsweringOnCallerIdDetection=_FxoAnsweringDelayAnsweringOnCallerIdDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5000,1,300),_FxoAnsweringDelayAnsweringOnCallerIdDetection_Type())
fxoAnsweringDelayAnsweringOnCallerIdDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoAnsweringDelayAnsweringOnCallerIdDetection.setStatus(_A)
class _FxoAnsweringDelayWaitForCalleeToAnswer_Type(MxEnableState):defaultValue=0
_FxoAnsweringDelayWaitForCalleeToAnswer_Type.__name__=_F
_FxoAnsweringDelayWaitForCalleeToAnswer_Object=MibTableColumn
fxoAnsweringDelayWaitForCalleeToAnswer=_FxoAnsweringDelayWaitForCalleeToAnswer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5000,1,400),_FxoAnsweringDelayWaitForCalleeToAnswer_Type())
fxoAnsweringDelayWaitForCalleeToAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoAnsweringDelayWaitForCalleeToAnswer.setStatus(_A)
_FxoIncomingCallBehaviorTable_Object=MibTable
fxoIncomingCallBehaviorTable=_FxoIncomingCallBehaviorTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5100))
if mibBuilder.loadTexts:fxoIncomingCallBehaviorTable.setStatus(_A)
_FxoIncomingCallBehaviorEntry_Object=MibTableRow
fxoIncomingCallBehaviorEntry=_FxoIncomingCallBehaviorEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5100,1))
fxoIncomingCallBehaviorEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:fxoIncomingCallBehaviorEntry.setStatus(_A)
_FxoIncomingCallBehaviorId_Type=OctetString
_FxoIncomingCallBehaviorId_Object=MibTableColumn
fxoIncomingCallBehaviorId=_FxoIncomingCallBehaviorId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5100,1,100),_FxoIncomingCallBehaviorId_Type())
fxoIncomingCallBehaviorId.setMaxAccess(_E)
if mibBuilder.loadTexts:fxoIncomingCallBehaviorId.setStatus(_A)
class _FxoIncomingCallBehaviorNotAllowedBehavior_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('doNotAnswer',100),('playCongestionTone',200)))
_FxoIncomingCallBehaviorNotAllowedBehavior_Type.__name__=_C
_FxoIncomingCallBehaviorNotAllowedBehavior_Object=MibTableColumn
fxoIncomingCallBehaviorNotAllowedBehavior=_FxoIncomingCallBehaviorNotAllowedBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5100,1,200),_FxoIncomingCallBehaviorNotAllowedBehavior_Type())
fxoIncomingCallBehaviorNotAllowedBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoIncomingCallBehaviorNotAllowedBehavior.setStatus(_A)
_FxoCustomBasicParametersTable_Object=MibTable
fxoCustomBasicParametersTable=_FxoCustomBasicParametersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5200))
if mibBuilder.loadTexts:fxoCustomBasicParametersTable.setStatus(_A)
_FxoCustomBasicParametersEntry_Object=MibTableRow
fxoCustomBasicParametersEntry=_FxoCustomBasicParametersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5200,1))
fxoCustomBasicParametersEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:fxoCustomBasicParametersEntry.setStatus(_A)
_FxoCustomBasicParametersId_Type=OctetString
_FxoCustomBasicParametersId_Object=MibTableColumn
fxoCustomBasicParametersId=_FxoCustomBasicParametersId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5200,1,100),_FxoCustomBasicParametersId_Type())
fxoCustomBasicParametersId.setMaxAccess(_E)
if mibBuilder.loadTexts:fxoCustomBasicParametersId.setStatus(_A)
class _FxoCustomBasicParametersOverrideDefaultCountryParameters_Type(MxEnableState):defaultValue=0
_FxoCustomBasicParametersOverrideDefaultCountryParameters_Type.__name__=_F
_FxoCustomBasicParametersOverrideDefaultCountryParameters_Object=MibTableColumn
fxoCustomBasicParametersOverrideDefaultCountryParameters=_FxoCustomBasicParametersOverrideDefaultCountryParameters_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5200,1,200),_FxoCustomBasicParametersOverrideDefaultCountryParameters_Type())
fxoCustomBasicParametersOverrideDefaultCountryParameters.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoCustomBasicParametersOverrideDefaultCountryParameters.setStatus(_A)
class _FxoCustomBasicParametersImpedance_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400)));namedValues=NamedValues(*(('i600',100),('i600LongLoop',200),('i900',300),('australia',400),('austria',500),('belgium',600),('brazil',700),('china',800),('czechRepublic',900),('denmark',1000),('finland',1100),('france',1200),('germany',1300),('greece',1400),('italy',1500),('japan',1600),('netherlands',1700),('newZealand',1800),('norway',1900),('russia',2000),('slovakia',2100),('spain',2200),('sweden',2300),('uK',2400)))
_FxoCustomBasicParametersImpedance_Type.__name__=_C
_FxoCustomBasicParametersImpedance_Object=MibTableColumn
fxoCustomBasicParametersImpedance=_FxoCustomBasicParametersImpedance_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5200,1,300),_FxoCustomBasicParametersImpedance_Type())
fxoCustomBasicParametersImpedance.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoCustomBasicParametersImpedance.setStatus(_A)
class _FxoCustomBasicParametersDigitalHybrid_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FxoCustomBasicParametersDigitalHybrid_Type.__name__=_H
_FxoCustomBasicParametersDigitalHybrid_Object=MibTableColumn
fxoCustomBasicParametersDigitalHybrid=_FxoCustomBasicParametersDigitalHybrid_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5200,1,400),_FxoCustomBasicParametersDigitalHybrid_Type())
fxoCustomBasicParametersDigitalHybrid.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoCustomBasicParametersDigitalHybrid.setStatus(_A)
class _FxoCustomBasicParametersReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('reset',10)))
_FxoCustomBasicParametersReset_Type.__name__=_C
_FxoCustomBasicParametersReset_Object=MibTableColumn
fxoCustomBasicParametersReset=_FxoCustomBasicParametersReset_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,5200,1,10000),_FxoCustomBasicParametersReset_Type())
fxoCustomBasicParametersReset.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoCustomBasicParametersReset.setStatus(_A)
_FxoLinkStateVerificationGroup_ObjectIdentity=ObjectIdentity
fxoLinkStateVerificationGroup=_FxoLinkStateVerificationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10100))
_FxoLinkStateTable_Object=MibTable
fxoLinkStateTable=_FxoLinkStateTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10100,100))
if mibBuilder.loadTexts:fxoLinkStateTable.setStatus(_A)
_FxoLinkStateEntry_Object=MibTableRow
fxoLinkStateEntry=_FxoLinkStateEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10100,100,1))
fxoLinkStateEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:fxoLinkStateEntry.setStatus(_A)
_FxoLinkStateId_Type=OctetString
_FxoLinkStateId_Object=MibTableColumn
fxoLinkStateId=_FxoLinkStateId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10100,100,1,100),_FxoLinkStateId_Type())
fxoLinkStateId.setMaxAccess(_E)
if mibBuilder.loadTexts:fxoLinkStateId.setStatus(_A)
class _FxoLinkStateLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('unknown',100),('up',200),('down',300)))
_FxoLinkStateLinkState_Type.__name__=_C
_FxoLinkStateLinkState_Object=MibTableColumn
fxoLinkStateLinkState=_FxoLinkStateLinkState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10100,100,1,200),_FxoLinkStateLinkState_Type())
fxoLinkStateLinkState.setMaxAccess(_E)
if mibBuilder.loadTexts:fxoLinkStateLinkState.setStatus(_A)
class _FxoLinkStateVerification_Type(MxEnableState):defaultValue=1
_FxoLinkStateVerification_Type.__name__=_F
_FxoLinkStateVerification_Object=MibScalar
fxoLinkStateVerification=_FxoLinkStateVerification_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10100,200),_FxoLinkStateVerification_Type())
fxoLinkStateVerification.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoLinkStateVerification.setStatus(_A)
class _FxoLinkStateVerificationTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_FxoLinkStateVerificationTimeout_Type.__name__=_D
_FxoLinkStateVerificationTimeout_Object=MibScalar
fxoLinkStateVerificationTimeout=_FxoLinkStateVerificationTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10100,300),_FxoLinkStateVerificationTimeout_Type())
fxoLinkStateVerificationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoLinkStateVerificationTimeout.setStatus(_A)
_FxoForceEndOfCallGroup_ObjectIdentity=ObjectIdentity
fxoForceEndOfCallGroup=_FxoForceEndOfCallGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200))
class _FxoFeocOnCallFailureEnable_Type(MxEnableState):defaultValue=1
_FxoFeocOnCallFailureEnable_Type.__name__=_F
_FxoFeocOnCallFailureEnable_Object=MibScalar
fxoFeocOnCallFailureEnable=_FxoFeocOnCallFailureEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,100),_FxoFeocOnCallFailureEnable_Type())
fxoFeocOnCallFailureEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocOnCallFailureEnable.setStatus(_A)
class _FxoFeocOnCallFailureTimeout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FxoFeocOnCallFailureTimeout_Type.__name__=_D
_FxoFeocOnCallFailureTimeout_Object=MibScalar
fxoFeocOnCallFailureTimeout=_FxoFeocOnCallFailureTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,200),_FxoFeocOnCallFailureTimeout_Type())
fxoFeocOnCallFailureTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocOnCallFailureTimeout.setStatus(_A)
class _FxoFeocOnSilenceDetectionMode_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,400)));namedValues=NamedValues(*((_I,100),('inbountAndOutboundSilent',400)))
_FxoFeocOnSilenceDetectionMode_Type.__name__=_C
_FxoFeocOnSilenceDetectionMode_Object=MibScalar
fxoFeocOnSilenceDetectionMode=_FxoFeocOnSilenceDetectionMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,300),_FxoFeocOnSilenceDetectionMode_Type())
fxoFeocOnSilenceDetectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocOnSilenceDetectionMode.setStatus(_A)
class _FxoFeocOnSilenceDetectionTimeout_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_FxoFeocOnSilenceDetectionTimeout_Type.__name__=_D
_FxoFeocOnSilenceDetectionTimeout_Object=MibScalar
fxoFeocOnSilenceDetectionTimeout=_FxoFeocOnSilenceDetectionTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,400),_FxoFeocOnSilenceDetectionTimeout_Type())
fxoFeocOnSilenceDetectionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocOnSilenceDetectionTimeout.setStatus(_A)
class _FxoFeocOnToneDetectionMode_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_I,100),(_T,200),('customTone',300)))
_FxoFeocOnToneDetectionMode_Type.__name__=_C
_FxoFeocOnToneDetectionMode_Object=MibScalar
fxoFeocOnToneDetectionMode=_FxoFeocOnToneDetectionMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,500),_FxoFeocOnToneDetectionMode_Type())
fxoFeocOnToneDetectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocOnToneDetectionMode.setStatus(_A)
_FxoForceEndOfCallToneCustomSettingsGroup_ObjectIdentity=ObjectIdentity
fxoForceEndOfCallToneCustomSettingsGroup=_FxoForceEndOfCallToneCustomSettingsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,10000))
class _FxoFeocToneCustomFrequency_Type(Unsigned32):defaultValue=440;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(350,620))
_FxoFeocToneCustomFrequency_Type.__name__=_D
_FxoFeocToneCustomFrequency_Object=MibScalar
fxoFeocToneCustomFrequency=_FxoFeocToneCustomFrequency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,10000,100),_FxoFeocToneCustomFrequency_Type())
fxoFeocToneCustomFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocToneCustomFrequency.setStatus(_A)
class _FxoFeocToneCustomCadence_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FxoFeocToneCustomCadence_Type.__name__=_H
_FxoFeocToneCustomCadence_Object=MibScalar
fxoFeocToneCustomCadence=_FxoFeocToneCustomCadence_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,10000,200),_FxoFeocToneCustomCadence_Type())
fxoFeocToneCustomCadence.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocToneCustomCadence.setStatus(_A)
class _FxoFeocToneCustomRepetition_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_FxoFeocToneCustomRepetition_Type.__name__=_D
_FxoFeocToneCustomRepetition_Object=MibScalar
fxoFeocToneCustomRepetition=_FxoFeocToneCustomRepetition_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,20000,10200,10000,300),_FxoFeocToneCustomRepetition_Type())
fxoFeocToneCustomRepetition.setMaxAccess(_B)
if mibBuilder.loadTexts:fxoFeocToneCustomRepetition.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*((_I,0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1800,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'potsMIB':potsMIB,'potsMIBObjects':potsMIBObjects,'lineTable':lineTable,'lineEntry':lineEntry,_L:lineId,'lineTypeStatus':lineTypeStatus,'lineState':lineState,'callerIdCustomization':callerIdCustomization,'dtmfMapDigitDetection':dtmfMapDigitDetection,'vocalUnitInformation':vocalUnitInformation,'callerIdTransmission':callerIdTransmission,'fxsGroup':fxsGroup,'fxsLineSupervisionMode':fxsLineSupervisionMode,'fxsDisconnectDelay':fxsDisconnectDelay,'fxsInbandRingback':fxsInbandRingback,'fxsShutdownBehavior':fxsShutdownBehavior,'fxsPowerDropOnDisconnectDuration':fxsPowerDropOnDisconnectDuration,'fxsServiceActivation':fxsServiceActivation,'fxsCallerIdPrivateCallingPartyName':fxsCallerIdPrivateCallingPartyName,'fxsSipMessageAlertingEnable':fxsSipMessageAlertingEnable,'fxsCountryCustomizationGroup':fxsCountryCustomizationGroup,'fxsCountryCustomizationOverride':fxsCountryCustomizationOverride,'fxsCountryCustomizationLoopCurrent':fxsCountryCustomizationLoopCurrent,'fxsCountryCustomizationFlashHookDetectionRange':fxsCountryCustomizationFlashHookDetectionRange,'fxsBypassGroup':fxsBypassGroup,'fxsBypassTable':fxsBypassTable,'fxsBypassEntry':fxsBypassEntry,_N:fxsBypassId,'fxsBypassActivation':fxsBypassActivation,'fxsBypassActivationDtmfMap':fxsBypassActivationDtmfMap,'fxsBypassDeactivationTimeout':fxsBypassDeactivationTimeout,'fxsMessageWaitingIndicatorGroup':fxsMessageWaitingIndicatorGroup,'fxsDefaultMessageWaitingIndicatorActivation':fxsDefaultMessageWaitingIndicatorActivation,'fxsDefaultVisualMessageWaitingIndicatorType':fxsDefaultVisualMessageWaitingIndicatorType,'fxsSpecificMessageWaitingIndicatorTable':fxsSpecificMessageWaitingIndicatorTable,'fxsSpecificMessageWaitingIndicatorEntry':fxsSpecificMessageWaitingIndicatorEntry,_Q:fxsSpecificMessageWaitingIndicatorId,'fxsSpecificMessageWaitingIndicatorEnableConfig':fxsSpecificMessageWaitingIndicatorEnableConfig,'fxsSpecificMessageWaitingIndicatorActivation':fxsSpecificMessageWaitingIndicatorActivation,'fxsCallGroup':fxsCallGroup,'fxsDefaultAutoCancelTimeout':fxsDefaultAutoCancelTimeout,'fxsEmergencyCallGroup':fxsEmergencyCallGroup,'fxsEmergencyCallOverride':fxsEmergencyCallOverride,'fxsEmergencyRingTimeout':fxsEmergencyRingTimeout,'fxsRingGroup':fxsRingGroup,'fxsDistinctiveRingTable':fxsDistinctiveRingTable,'fxsDistinctiveRingEntry':fxsDistinctiveRingEntry,_R:fxsDistinctiveRingIndex,'fxsDistinctiveRingRingId':fxsDistinctiveRingRingId,'fxsDistinctiveRingPattern':fxsDistinctiveRingPattern,'fxsCallerIdGroup':fxsCallerIdGroup,'fxsCallerIdTable':fxsCallerIdTable,'fxsCallerIdEntry':fxsCallerIdEntry,_S:fxsCallerIdId,'fxsCallerIdActivation':fxsCallerIdActivation,'fxsInteropGroup':fxsInteropGroup,'fxsInteropPlayLocalRingbackWhenNoMediaStream':fxsInteropPlayLocalRingbackWhenNoMediaStream,'fxoGroup':fxoGroup,'fxoPreDialDelay':fxoPreDialDelay,'fxoDialToneDetectionMode':fxoDialToneDetectionMode,'fxoDialToneDetectionTimeout':fxoDialToneDetectionTimeout,'fxoAnsweringDelayTable':fxoAnsweringDelayTable,'fxoAnsweringDelayEntry':fxoAnsweringDelayEntry,_U:fxoAnsweringDelayId,'fxoAnsweringDelayWaitBeforeAnsweringDelay':fxoAnsweringDelayWaitBeforeAnsweringDelay,'fxoAnsweringDelayAnsweringOnCallerIdDetection':fxoAnsweringDelayAnsweringOnCallerIdDetection,'fxoAnsweringDelayWaitForCalleeToAnswer':fxoAnsweringDelayWaitForCalleeToAnswer,'fxoIncomingCallBehaviorTable':fxoIncomingCallBehaviorTable,'fxoIncomingCallBehaviorEntry':fxoIncomingCallBehaviorEntry,_V:fxoIncomingCallBehaviorId,'fxoIncomingCallBehaviorNotAllowedBehavior':fxoIncomingCallBehaviorNotAllowedBehavior,'fxoCustomBasicParametersTable':fxoCustomBasicParametersTable,'fxoCustomBasicParametersEntry':fxoCustomBasicParametersEntry,_W:fxoCustomBasicParametersId,'fxoCustomBasicParametersOverrideDefaultCountryParameters':fxoCustomBasicParametersOverrideDefaultCountryParameters,'fxoCustomBasicParametersImpedance':fxoCustomBasicParametersImpedance,'fxoCustomBasicParametersDigitalHybrid':fxoCustomBasicParametersDigitalHybrid,'fxoCustomBasicParametersReset':fxoCustomBasicParametersReset,'fxoLinkStateVerificationGroup':fxoLinkStateVerificationGroup,'fxoLinkStateTable':fxoLinkStateTable,'fxoLinkStateEntry':fxoLinkStateEntry,_X:fxoLinkStateId,'fxoLinkStateLinkState':fxoLinkStateLinkState,'fxoLinkStateVerification':fxoLinkStateVerification,'fxoLinkStateVerificationTimeout':fxoLinkStateVerificationTimeout,'fxoForceEndOfCallGroup':fxoForceEndOfCallGroup,'fxoFeocOnCallFailureEnable':fxoFeocOnCallFailureEnable,'fxoFeocOnCallFailureTimeout':fxoFeocOnCallFailureTimeout,'fxoFeocOnSilenceDetectionMode':fxoFeocOnSilenceDetectionMode,'fxoFeocOnSilenceDetectionTimeout':fxoFeocOnSilenceDetectionTimeout,'fxoFeocOnToneDetectionMode':fxoFeocOnToneDetectionMode,'fxoForceEndOfCallToneCustomSettingsGroup':fxoForceEndOfCallToneCustomSettingsGroup,'fxoFeocToneCustomFrequency':fxoFeocToneCustomFrequency,'fxoFeocToneCustomCadence':fxoFeocToneCustomCadence,'fxoFeocToneCustomRepetition':fxoFeocToneCustomRepetition,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})