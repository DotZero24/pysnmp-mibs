_L='commonMulticastAddressIndex'
_K='NotificationType'
_J='commonLogicalID'
_I='commonPhysAddress'
_H='DisplayString'
_G='OctetString'
_F='SCTE-HMS-COMMON-MIB'
_E='optional'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonIdent,=mibBuilder.importSymbols('SCTE-HMS-ROOTS','commonIdent')
scteHmsTree,=mibBuilder.importSymbols('SCTE-ROOT','scteHmsTree')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_CommonAdminGroup_ObjectIdentity=ObjectIdentity
commonAdminGroup=_CommonAdminGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,3,1))
class _CommonLogicalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CommonLogicalID_Type.__name__=_G
_CommonLogicalID_Object=MibScalar
commonLogicalID=_CommonLogicalID_Object((1,3,6,1,4,1,5591,1,3,1,1),_CommonLogicalID_Type())
commonLogicalID.setMaxAccess(_D)
if mibBuilder.loadTexts:commonLogicalID.setStatus(_A)
class _CommonVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonVendor_Type.__name__=_H
_CommonVendor_Object=MibScalar
commonVendor=_CommonVendor_Object((1,3,6,1,4,1,5591,1,3,1,2),_CommonVendor_Type())
commonVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:commonVendor.setStatus(_A)
class _CommonModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonModelNumber_Type.__name__=_H
_CommonModelNumber_Object=MibScalar
commonModelNumber=_CommonModelNumber_Object((1,3,6,1,4,1,5591,1,3,1,3),_CommonModelNumber_Type())
commonModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:commonModelNumber.setStatus(_A)
class _CommonSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonSerialNumber_Type.__name__=_H
_CommonSerialNumber_Object=MibScalar
commonSerialNumber=_CommonSerialNumber_Object((1,3,6,1,4,1,5591,1,3,1,4),_CommonSerialNumber_Type())
commonSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:commonSerialNumber.setStatus(_A)
class _CommonVendorInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonVendorInfo_Type.__name__=_H
_CommonVendorInfo_Object=MibScalar
commonVendorInfo=_CommonVendorInfo_Object((1,3,6,1,4,1,5591,1,3,1,5),_CommonVendorInfo_Type())
commonVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:commonVendorInfo.setStatus(_E)
class _CommonNEStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CommonNEStatus_Type.__name__=_G
_CommonNEStatus_Object=MibScalar
commonNEStatus=_CommonNEStatus_Object((1,3,6,1,4,1,5591,1,3,1,6),_CommonNEStatus_Type())
commonNEStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNEStatus.setStatus(_A)
class _CommonReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_CommonReset_Type.__name__=_C
_CommonReset_Object=MibScalar
commonReset=_CommonReset_Object((1,3,6,1,4,1,5591,1,3,1,7),_CommonReset_Type())
commonReset.setMaxAccess(_D)
if mibBuilder.loadTexts:commonReset.setStatus(_A)
class _CommonAlarmDetectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('detectionDisabled',1),('detectionEnabled',2),('detectionEnabledAndRegenerate',3)))
_CommonAlarmDetectionControl_Type.__name__=_C
_CommonAlarmDetectionControl_Object=MibScalar
commonAlarmDetectionControl=_CommonAlarmDetectionControl_Object((1,3,6,1,4,1,5591,1,3,1,8),_CommonAlarmDetectionControl_Type())
commonAlarmDetectionControl.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAlarmDetectionControl.setStatus(_A)
_CommonNetworkAddress_Type=IpAddress
_CommonNetworkAddress_Object=MibScalar
commonNetworkAddress=_CommonNetworkAddress_Object((1,3,6,1,4,1,5591,1,3,1,9),_CommonNetworkAddress_Type())
commonNetworkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNetworkAddress.setStatus(_A)
_CommonCheckCode_Type=Integer32
_CommonCheckCode_Object=MibScalar
commonCheckCode=_CommonCheckCode_Object((1,3,6,1,4,1,5591,1,3,1,10),_CommonCheckCode_Type())
commonCheckCode.setMaxAccess(_D)
if mibBuilder.loadTexts:commonCheckCode.setStatus(_A)
class _CommonTrapCommunityString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CommonTrapCommunityString_Type.__name__=_G
_CommonTrapCommunityString_Object=MibScalar
commonTrapCommunityString=_CommonTrapCommunityString_Object((1,3,6,1,4,1,5591,1,3,1,11),_CommonTrapCommunityString_Type())
commonTrapCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:commonTrapCommunityString.setStatus(_A)
class _CommonTamperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('intact',1),('compromised',2)))
_CommonTamperStatus_Type.__name__=_C
_CommonTamperStatus_Object=MibScalar
commonTamperStatus=_CommonTamperStatus_Object((1,3,6,1,4,1,5591,1,3,1,12),_CommonTamperStatus_Type())
commonTamperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonTamperStatus.setStatus(_E)
class _CommonInternalTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,130))
_CommonInternalTemperature_Type.__name__=_C
_CommonInternalTemperature_Object=MibScalar
commonInternalTemperature=_CommonInternalTemperature_Object((1,3,6,1,4,1,5591,1,3,1,13),_CommonInternalTemperature_Type())
commonInternalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:commonInternalTemperature.setStatus(_E)
_CommonTime_Type=Integer32
_CommonTime_Object=MibScalar
commonTime=_CommonTime_Object((1,3,6,1,4,1,5591,1,3,1,14),_CommonTime_Type())
commonTime.setMaxAccess(_B)
if mibBuilder.loadTexts:commonTime.setStatus(_E)
_CommonVarBindings_Type=Integer32
_CommonVarBindings_Object=MibScalar
commonVarBindings=_CommonVarBindings_Object((1,3,6,1,4,1,5591,1,3,1,15),_CommonVarBindings_Type())
commonVarBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:commonVarBindings.setStatus(_A)
class _CommonResetCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('powerup',2),('command',3),('watchdog',4),('craft',5)))
_CommonResetCause_Type.__name__=_C
_CommonResetCause_Object=MibScalar
commonResetCause=_CommonResetCause_Object((1,3,6,1,4,1,5591,1,3,1,16),_CommonResetCause_Type())
commonResetCause.setMaxAccess(_B)
if mibBuilder.loadTexts:commonResetCause.setStatus(_A)
class _CommonCraftStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disconnected',1),('connected',2)))
_CommonCraftStatus_Type.__name__=_C
_CommonCraftStatus_Object=MibScalar
commonCraftStatus=_CommonCraftStatus_Object((1,3,6,1,4,1,5591,1,3,1,17),_CommonCraftStatus_Type())
commonCraftStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonCraftStatus.setStatus(_A)
_CommonMACGroup_ObjectIdentity=ObjectIdentity
commonMACGroup=_CommonMACGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,3,2))
class _CommonBackoffPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_CommonBackoffPeriod_Type.__name__=_C
_CommonBackoffPeriod_Object=MibScalar
commonBackoffPeriod=_CommonBackoffPeriod_Object((1,3,6,1,4,1,5591,1,3,2,1),_CommonBackoffPeriod_Type())
commonBackoffPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:commonBackoffPeriod.setStatus(_A)
class _CommonACKTimeoutWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CommonACKTimeoutWindow_Type.__name__=_C
_CommonACKTimeoutWindow_Object=MibScalar
commonACKTimeoutWindow=_CommonACKTimeoutWindow_Object((1,3,6,1,4,1,5591,1,3,2,2),_CommonACKTimeoutWindow_Type())
commonACKTimeoutWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:commonACKTimeoutWindow.setStatus(_A)
class _CommonMaximumMACLayerRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CommonMaximumMACLayerRetries_Type.__name__=_C
_CommonMaximumMACLayerRetries_Object=MibScalar
commonMaximumMACLayerRetries=_CommonMaximumMACLayerRetries_Object((1,3,6,1,4,1,5591,1,3,2,3),_CommonMaximumMACLayerRetries_Type())
commonMaximumMACLayerRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:commonMaximumMACLayerRetries.setStatus(_A)
_CommonMaxPayloadSize_Type=Integer32
_CommonMaxPayloadSize_Object=MibScalar
commonMaxPayloadSize=_CommonMaxPayloadSize_Object((1,3,6,1,4,1,5591,1,3,2,4),_CommonMaxPayloadSize_Type())
commonMaxPayloadSize.setMaxAccess(_B)
if mibBuilder.loadTexts:commonMaxPayloadSize.setStatus(_A)
class _CommonBackoffMinimumExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CommonBackoffMinimumExponent_Type.__name__=_C
_CommonBackoffMinimumExponent_Object=MibScalar
commonBackoffMinimumExponent=_CommonBackoffMinimumExponent_Object((1,3,6,1,4,1,5591,1,3,2,5),_CommonBackoffMinimumExponent_Type())
commonBackoffMinimumExponent.setMaxAccess(_D)
if mibBuilder.loadTexts:commonBackoffMinimumExponent.setStatus(_A)
class _CommonBackoffMaximumExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CommonBackoffMaximumExponent_Type.__name__=_C
_CommonBackoffMaximumExponent_Object=MibScalar
commonBackoffMaximumExponent=_CommonBackoffMaximumExponent_Object((1,3,6,1,4,1,5591,1,3,2,6),_CommonBackoffMaximumExponent_Type())
commonBackoffMaximumExponent.setMaxAccess(_D)
if mibBuilder.loadTexts:commonBackoffMaximumExponent.setStatus(_A)
_CommonPhysAddress_Type=OctetString
_CommonPhysAddress_Object=MibScalar
commonPhysAddress=_CommonPhysAddress_Object((1,3,6,1,4,1,5591,1,3,2,7),_CommonPhysAddress_Type())
commonPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:commonPhysAddress.setStatus(_A)
_CommonMulticastGroup_ObjectIdentity=ObjectIdentity
commonMulticastGroup=_CommonMulticastGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,3,3))
class _CommonMaxMulticastAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,255))
_CommonMaxMulticastAddresses_Type.__name__=_C
_CommonMaxMulticastAddresses_Object=MibScalar
commonMaxMulticastAddresses=_CommonMaxMulticastAddresses_Object((1,3,6,1,4,1,5591,1,3,3,1),_CommonMaxMulticastAddresses_Type())
commonMaxMulticastAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:commonMaxMulticastAddresses.setStatus(_A)
_CommonMulticastAddressTable_Object=MibTable
commonMulticastAddressTable=_CommonMulticastAddressTable_Object((1,3,6,1,4,1,5591,1,3,3,2))
if mibBuilder.loadTexts:commonMulticastAddressTable.setStatus(_A)
_CommonMulticastAddressEntry_Object=MibTableRow
commonMulticastAddressEntry=_CommonMulticastAddressEntry_Object((1,3,6,1,4,1,5591,1,3,3,2,1))
commonMulticastAddressEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:commonMulticastAddressEntry.setStatus(_A)
class _CommonMulticastAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CommonMulticastAddressIndex_Type.__name__=_C
_CommonMulticastAddressIndex_Object=MibTableColumn
commonMulticastAddressIndex=_CommonMulticastAddressIndex_Object((1,3,6,1,4,1,5591,1,3,3,2,1,1),_CommonMulticastAddressIndex_Type())
commonMulticastAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:commonMulticastAddressIndex.setStatus(_A)
class _CommonMulticastAddressNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CommonMulticastAddressNumber_Type.__name__=_G
_CommonMulticastAddressNumber_Object=MibTableColumn
commonMulticastAddressNumber=_CommonMulticastAddressNumber_Object((1,3,6,1,4,1,5591,1,3,3,2,1,2),_CommonMulticastAddressNumber_Type())
commonMulticastAddressNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:commonMulticastAddressNumber.setStatus(_A)
_CommonStatsGroup_ObjectIdentity=ObjectIdentity
commonStatsGroup=_CommonStatsGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,3,4))
_CommonMacStats_ObjectIdentity=ObjectIdentity
commonMacStats=_CommonMacStats_ObjectIdentity((1,3,6,1,4,1,5591,1,3,4,1))
_CommonForwardPathLOSEvents_Type=Counter32
_CommonForwardPathLOSEvents_Object=MibScalar
commonForwardPathLOSEvents=_CommonForwardPathLOSEvents_Object((1,3,6,1,4,1,5591,1,3,4,1,1),_CommonForwardPathLOSEvents_Type())
commonForwardPathLOSEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:commonForwardPathLOSEvents.setStatus(_E)
_CommonForwardPathFramingErrors_Type=Counter32
_CommonForwardPathFramingErrors_Object=MibScalar
commonForwardPathFramingErrors=_CommonForwardPathFramingErrors_Object((1,3,6,1,4,1,5591,1,3,4,1,2),_CommonForwardPathFramingErrors_Type())
commonForwardPathFramingErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:commonForwardPathFramingErrors.setStatus(_E)
_CommonForwardPathCRCErrors_Type=Counter32
_CommonForwardPathCRCErrors_Object=MibScalar
commonForwardPathCRCErrors=_CommonForwardPathCRCErrors_Object((1,3,6,1,4,1,5591,1,3,4,1,3),_CommonForwardPathCRCErrors_Type())
commonForwardPathCRCErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:commonForwardPathCRCErrors.setStatus(_E)
_CommonInvalidMacCmds_Type=Counter32
_CommonInvalidMacCmds_Object=MibScalar
commonInvalidMacCmds=_CommonInvalidMacCmds_Object((1,3,6,1,4,1,5591,1,3,4,1,4),_CommonInvalidMacCmds_Type())
commonInvalidMacCmds.setMaxAccess(_D)
if mibBuilder.loadTexts:commonInvalidMacCmds.setStatus(_E)
_CommonRfGroup_ObjectIdentity=ObjectIdentity
commonRfGroup=_CommonRfGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,3,5))
class _CommonReturnPathFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CommonReturnPathFrequency_Type.__name__=_C
_CommonReturnPathFrequency_Object=MibScalar
commonReturnPathFrequency=_CommonReturnPathFrequency_Object((1,3,6,1,4,1,5591,1,3,5,1),_CommonReturnPathFrequency_Type())
commonReturnPathFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:commonReturnPathFrequency.setStatus(_A)
class _CommonForwardPathFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CommonForwardPathFrequency_Type.__name__=_C
_CommonForwardPathFrequency_Object=MibScalar
commonForwardPathFrequency=_CommonForwardPathFrequency_Object((1,3,6,1,4,1,5591,1,3,5,2),_CommonForwardPathFrequency_Type())
commonForwardPathFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:commonForwardPathFrequency.setStatus(_A)
_CommonProvisionedReturnPowerLevel_Type=Integer32
_CommonProvisionedReturnPowerLevel_Object=MibScalar
commonProvisionedReturnPowerLevel=_CommonProvisionedReturnPowerLevel_Object((1,3,6,1,4,1,5591,1,3,5,3),_CommonProvisionedReturnPowerLevel_Type())
commonProvisionedReturnPowerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:commonProvisionedReturnPowerLevel.setStatus(_A)
class _CommonForwardPathReceiveLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,1000))
_CommonForwardPathReceiveLevel_Type.__name__=_C
_CommonForwardPathReceiveLevel_Object=MibScalar
commonForwardPathReceiveLevel=_CommonForwardPathReceiveLevel_Object((1,3,6,1,4,1,5591,1,3,5,4),_CommonForwardPathReceiveLevel_Type())
commonForwardPathReceiveLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:commonForwardPathReceiveLevel.setStatus(_E)
class _CommonMaxReturnPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,600))
_CommonMaxReturnPower_Type.__name__=_C
_CommonMaxReturnPower_Object=MibScalar
commonMaxReturnPower=_CommonMaxReturnPower_Object((1,3,6,1,4,1,5591,1,3,5,5),_CommonMaxReturnPower_Type())
commonMaxReturnPower.setMaxAccess(_D)
if mibBuilder.loadTexts:commonMaxReturnPower.setStatus(_A)
hmsColdStart=NotificationType((1,3,6,1,4,1,5591,1,0,0))
hmsColdStart.setObjects(*((_F,_I),(_F,_J)))
if mibBuilder.loadTexts:hmsColdStart.setStatus('')
hmsWarmStart=NotificationType((1,3,6,1,4,1,5591,1,0,2))
hmsWarmStart.setObjects(*((_F,_I),(_F,_J)))
if mibBuilder.loadTexts:hmsWarmStart.setStatus('')
mibBuilder.exportSymbols(_F,**{'hmsColdStart':hmsColdStart,'hmsWarmStart':hmsWarmStart,'commonAdminGroup':commonAdminGroup,_J:commonLogicalID,'commonVendor':commonVendor,'commonModelNumber':commonModelNumber,'commonSerialNumber':commonSerialNumber,'commonVendorInfo':commonVendorInfo,'commonNEStatus':commonNEStatus,'commonReset':commonReset,'commonAlarmDetectionControl':commonAlarmDetectionControl,'commonNetworkAddress':commonNetworkAddress,'commonCheckCode':commonCheckCode,'commonTrapCommunityString':commonTrapCommunityString,'commonTamperStatus':commonTamperStatus,'commonInternalTemperature':commonInternalTemperature,'commonTime':commonTime,'commonVarBindings':commonVarBindings,'commonResetCause':commonResetCause,'commonCraftStatus':commonCraftStatus,'commonMACGroup':commonMACGroup,'commonBackoffPeriod':commonBackoffPeriod,'commonACKTimeoutWindow':commonACKTimeoutWindow,'commonMaximumMACLayerRetries':commonMaximumMACLayerRetries,'commonMaxPayloadSize':commonMaxPayloadSize,'commonBackoffMinimumExponent':commonBackoffMinimumExponent,'commonBackoffMaximumExponent':commonBackoffMaximumExponent,_I:commonPhysAddress,'commonMulticastGroup':commonMulticastGroup,'commonMaxMulticastAddresses':commonMaxMulticastAddresses,'commonMulticastAddressTable':commonMulticastAddressTable,'commonMulticastAddressEntry':commonMulticastAddressEntry,_L:commonMulticastAddressIndex,'commonMulticastAddressNumber':commonMulticastAddressNumber,'commonStatsGroup':commonStatsGroup,'commonMacStats':commonMacStats,'commonForwardPathLOSEvents':commonForwardPathLOSEvents,'commonForwardPathFramingErrors':commonForwardPathFramingErrors,'commonForwardPathCRCErrors':commonForwardPathCRCErrors,'commonInvalidMacCmds':commonInvalidMacCmds,'commonRfGroup':commonRfGroup,'commonReturnPathFrequency':commonReturnPathFrequency,'commonForwardPathFrequency':commonForwardPathFrequency,'commonProvisionedReturnPowerLevel':commonProvisionedReturnPowerLevel,'commonForwardPathReceiveLevel':commonForwardPathReceiveLevel,'commonMaxReturnPower':commonMaxReturnPower})