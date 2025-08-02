_f='alarmText'
_e='alarmLogInformation'
_d='oswDCPowerIndex'
_c='commonDeviceSlot'
_b='commonAgentTrapIndex'
_a='commonMulticastAddressIndex'
_Z='connected'
_Y='disconnected'
_X='watchdog'
_W='command'
_V='powerup'
_U='compromised'
_T='intact'
_S='detectionEnabledAndRegenerate'
_R='detectionEnabled'
_Q='detectionDisabled'
_P='alarmLogIndex'
_O='currentAlarmOID'
_N='discreteAlarmValue'
_M='discreteParameterOID'
_L='analogParameterOID'
_K='reset'
_J='commonNELogicalID'
_I='commonPhysAddress'
_H='OctetString'
_G='DisplayString'
_F='NSCRTV-HFCEMS-ANALOG-MIB'
_E='optional'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_NscrtvRoot_ObjectIdentity=ObjectIdentity
nscrtvRoot=_NscrtvRoot_ObjectIdentity((1,3,6,1,4,1,17409))
_NscrtvHFCemsTree_ObjectIdentity=ObjectIdentity
nscrtvHFCemsTree=_NscrtvHFCemsTree_ObjectIdentity((1,3,6,1,4,1,17409,1))
_PropertyIdent_ObjectIdentity=ObjectIdentity
propertyIdent=_PropertyIdent_ObjectIdentity((1,3,6,1,4,1,17409,1,1))
_AnalogPropertyTable_Object=MibTable
analogPropertyTable=_AnalogPropertyTable_Object((1,3,6,1,4,1,17409,1,1,1))
if mibBuilder.loadTexts:analogPropertyTable.setStatus(_A)
_AnalogPropertyEntry_Object=MibTableRow
analogPropertyEntry=_AnalogPropertyEntry_Object((1,3,6,1,4,1,17409,1,1,1,1))
analogPropertyEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:analogPropertyEntry.setStatus(_A)
_AnalogParameterOID_Type=ObjectIdentifier
_AnalogParameterOID_Object=MibTableColumn
analogParameterOID=_AnalogParameterOID_Object((1,3,6,1,4,1,17409,1,1,1,1,1),_AnalogParameterOID_Type())
analogParameterOID.setMaxAccess(_B)
if mibBuilder.loadTexts:analogParameterOID.setStatus(_A)
class _AlarmEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_AlarmEnable_Type.__name__=_H
_AlarmEnable_Object=MibTableColumn
alarmEnable=_AlarmEnable_Object((1,3,6,1,4,1,17409,1,1,1,1,2),_AlarmEnable_Type())
alarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmEnable.setStatus(_A)
class _AnalogAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('aasNominal',1),('aasHIHI',2),('aasHI',3),('aasLO',4),('aasLOLO',5)))
_AnalogAlarmState_Type.__name__=_C
_AnalogAlarmState_Object=MibTableColumn
analogAlarmState=_AnalogAlarmState_Object((1,3,6,1,4,1,17409,1,1,1,1,3),_AnalogAlarmState_Type())
analogAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:analogAlarmState.setStatus(_A)
_AnalogAlarmHIHI_Type=Integer32
_AnalogAlarmHIHI_Object=MibTableColumn
analogAlarmHIHI=_AnalogAlarmHIHI_Object((1,3,6,1,4,1,17409,1,1,1,1,4),_AnalogAlarmHIHI_Type())
analogAlarmHIHI.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmHIHI.setStatus(_A)
_AnalogAlarmHI_Type=Integer32
_AnalogAlarmHI_Object=MibTableColumn
analogAlarmHI=_AnalogAlarmHI_Object((1,3,6,1,4,1,17409,1,1,1,1,5),_AnalogAlarmHI_Type())
analogAlarmHI.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmHI.setStatus(_A)
_AnalogAlarmLO_Type=Integer32
_AnalogAlarmLO_Object=MibTableColumn
analogAlarmLO=_AnalogAlarmLO_Object((1,3,6,1,4,1,17409,1,1,1,1,6),_AnalogAlarmLO_Type())
analogAlarmLO.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmLO.setStatus(_A)
_AnalogAlarmLOLO_Type=Integer32
_AnalogAlarmLOLO_Object=MibTableColumn
analogAlarmLOLO=_AnalogAlarmLOLO_Object((1,3,6,1,4,1,17409,1,1,1,1,7),_AnalogAlarmLOLO_Type())
analogAlarmLOLO.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmLOLO.setStatus(_A)
_AnalogAlarmDeadband_Type=Integer32
_AnalogAlarmDeadband_Object=MibTableColumn
analogAlarmDeadband=_AnalogAlarmDeadband_Object((1,3,6,1,4,1,17409,1,1,1,1,8),_AnalogAlarmDeadband_Type())
analogAlarmDeadband.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmDeadband.setStatus(_A)
_DiscretePropertyTable_Object=MibTable
discretePropertyTable=_DiscretePropertyTable_Object((1,3,6,1,4,1,17409,1,1,2))
if mibBuilder.loadTexts:discretePropertyTable.setStatus(_A)
_DiscretePropertyEntry_Object=MibTableRow
discretePropertyEntry=_DiscretePropertyEntry_Object((1,3,6,1,4,1,17409,1,1,2,1))
discretePropertyEntry.setIndexNames((0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:discretePropertyEntry.setStatus(_A)
_DiscreteParameterOID_Type=ObjectIdentifier
_DiscreteParameterOID_Object=MibTableColumn
discreteParameterOID=_DiscreteParameterOID_Object((1,3,6,1,4,1,17409,1,1,2,1,1),_DiscreteParameterOID_Type())
discreteParameterOID.setMaxAccess(_B)
if mibBuilder.loadTexts:discreteParameterOID.setStatus(_A)
_DiscreteAlarmValue_Type=Integer32
_DiscreteAlarmValue_Object=MibTableColumn
discreteAlarmValue=_DiscreteAlarmValue_Object((1,3,6,1,4,1,17409,1,1,2,1,2),_DiscreteAlarmValue_Type())
discreteAlarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:discreteAlarmValue.setStatus(_A)
class _DiscreteAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('enableMajor',2),('enableMinor',3)))
_DiscreteAlarmEnable_Type.__name__=_C
_DiscreteAlarmEnable_Object=MibTableColumn
discreteAlarmEnable=_DiscreteAlarmEnable_Object((1,3,6,1,4,1,17409,1,1,2,1,3),_DiscreteAlarmEnable_Type())
discreteAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:discreteAlarmEnable.setStatus(_A)
class _DiscreteAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7)));namedValues=NamedValues(*(('dasNominal',1),('dasDiscreteMajor',6),('dasDiscreteMinor',7)))
_DiscreteAlarmState_Type.__name__=_C
_DiscreteAlarmState_Object=MibTableColumn
discreteAlarmState=_DiscreteAlarmState_Object((1,3,6,1,4,1,17409,1,1,2,1,4),_DiscreteAlarmState_Type())
discreteAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:discreteAlarmState.setStatus(_A)
_CurrentAlarmTable_Object=MibTable
currentAlarmTable=_CurrentAlarmTable_Object((1,3,6,1,4,1,17409,1,1,3))
if mibBuilder.loadTexts:currentAlarmTable.setStatus(_A)
_CurrentAlarmEntry_Object=MibTableRow
currentAlarmEntry=_CurrentAlarmEntry_Object((1,3,6,1,4,1,17409,1,1,3,1))
currentAlarmEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:currentAlarmEntry.setStatus(_A)
_CurrentAlarmOID_Type=ObjectIdentifier
_CurrentAlarmOID_Object=MibTableColumn
currentAlarmOID=_CurrentAlarmOID_Object((1,3,6,1,4,1,17409,1,1,3,1,1),_CurrentAlarmOID_Type())
currentAlarmOID.setMaxAccess(_B)
if mibBuilder.loadTexts:currentAlarmOID.setStatus(_A)
class _CurrentAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*(('caasHIHI',2),('caasHI',3),('caasLO',4),('caasLOLO',5),('caasDiscreteMajor',6),('caasDiscreteMinor',7)))
_CurrentAlarmState_Type.__name__=_C
_CurrentAlarmState_Object=MibTableColumn
currentAlarmState=_CurrentAlarmState_Object((1,3,6,1,4,1,17409,1,1,3,1,2),_CurrentAlarmState_Type())
currentAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:currentAlarmState.setStatus(_A)
_CurrentAlarmValue_Type=Integer32
_CurrentAlarmValue_Object=MibTableColumn
currentAlarmValue=_CurrentAlarmValue_Object((1,3,6,1,4,1,17409,1,1,3,1,3),_CurrentAlarmValue_Type())
currentAlarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:currentAlarmValue.setStatus(_A)
_AlarmsIdent_ObjectIdentity=ObjectIdentity
alarmsIdent=_AlarmsIdent_ObjectIdentity((1,3,6,1,4,1,17409,1,2))
_AlarmLogNumberOfEntries_Type=Integer32
_AlarmLogNumberOfEntries_Object=MibScalar
alarmLogNumberOfEntries=_AlarmLogNumberOfEntries_Object((1,3,6,1,4,1,17409,1,2,1),_AlarmLogNumberOfEntries_Type())
alarmLogNumberOfEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogNumberOfEntries.setStatus(_A)
_AlarmLogLastIndex_Type=Integer32
_AlarmLogLastIndex_Object=MibScalar
alarmLogLastIndex=_AlarmLogLastIndex_Object((1,3,6,1,4,1,17409,1,2,2),_AlarmLogLastIndex_Type())
alarmLogLastIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogLastIndex.setStatus(_A)
_AlarmLogTable_Object=MibTable
alarmLogTable=_AlarmLogTable_Object((1,3,6,1,4,1,17409,1,2,3))
if mibBuilder.loadTexts:alarmLogTable.setStatus(_A)
_AlarmLogEntry_Object=MibTableRow
alarmLogEntry=_AlarmLogEntry_Object((1,3,6,1,4,1,17409,1,2,3,1))
alarmLogEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:alarmLogEntry.setStatus(_A)
class _AlarmLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_AlarmLogIndex_Type.__name__=_C
_AlarmLogIndex_Object=MibTableColumn
alarmLogIndex=_AlarmLogIndex_Object((1,3,6,1,4,1,17409,1,2,3,1,1),_AlarmLogIndex_Type())
alarmLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogIndex.setStatus(_A)
class _AlarmLogInformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(17,255))
_AlarmLogInformation_Type.__name__=_H
_AlarmLogInformation_Object=MibTableColumn
alarmLogInformation=_AlarmLogInformation_Object((1,3,6,1,4,1,17409,1,2,3,1,2),_AlarmLogInformation_Type())
alarmLogInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogInformation.setStatus(_A)
_AlarmText_Type=DisplayString
_AlarmText_Object=MibScalar
alarmText=_AlarmText_Object((1,3,6,1,4,1,17409,1,2,4),_AlarmText_Type())
alarmText.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alarmText.setStatus(_E)
_CommonIdent_ObjectIdentity=ObjectIdentity
commonIdent=_CommonIdent_ObjectIdentity((1,3,6,1,4,1,17409,1,3))
_CommonAdminGroup_ObjectIdentity=ObjectIdentity
commonAdminGroup=_CommonAdminGroup_ObjectIdentity((1,3,6,1,4,1,17409,1,3,1))
class _CommonNELogicalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CommonNELogicalID_Type.__name__=_H
_CommonNELogicalID_Object=MibScalar
commonNELogicalID=_CommonNELogicalID_Object((1,3,6,1,4,1,17409,1,3,1,1),_CommonNELogicalID_Type())
commonNELogicalID.setMaxAccess(_D)
if mibBuilder.loadTexts:commonNELogicalID.setStatus(_A)
class _CommonNEVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonNEVendor_Type.__name__=_G
_CommonNEVendor_Object=MibScalar
commonNEVendor=_CommonNEVendor_Object((1,3,6,1,4,1,17409,1,3,1,2),_CommonNEVendor_Type())
commonNEVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNEVendor.setStatus(_A)
class _CommonNEModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonNEModelNumber_Type.__name__=_G
_CommonNEModelNumber_Object=MibScalar
commonNEModelNumber=_CommonNEModelNumber_Object((1,3,6,1,4,1,17409,1,3,1,3),_CommonNEModelNumber_Type())
commonNEModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNEModelNumber.setStatus(_A)
class _CommonNESerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonNESerialNumber_Type.__name__=_G
_CommonNESerialNumber_Object=MibScalar
commonNESerialNumber=_CommonNESerialNumber_Object((1,3,6,1,4,1,17409,1,3,1,4),_CommonNESerialNumber_Type())
commonNESerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNESerialNumber.setStatus(_A)
class _CommonNEVendorInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonNEVendorInfo_Type.__name__=_G
_CommonNEVendorInfo_Object=MibScalar
commonNEVendorInfo=_CommonNEVendorInfo_Object((1,3,6,1,4,1,17409,1,3,1,5),_CommonNEVendorInfo_Type())
commonNEVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNEVendorInfo.setStatus(_E)
class _CommonNEStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CommonNEStatus_Type.__name__=_H
_CommonNEStatus_Object=MibScalar
commonNEStatus=_CommonNEStatus_Object((1,3,6,1,4,1,17409,1,3,1,6),_CommonNEStatus_Type())
commonNEStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNEStatus.setStatus(_A)
class _CommonReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_CommonReset_Type.__name__=_C
_CommonReset_Object=MibScalar
commonReset=_CommonReset_Object((1,3,6,1,4,1,17409,1,3,1,7),_CommonReset_Type())
commonReset.setMaxAccess(_D)
if mibBuilder.loadTexts:commonReset.setStatus(_A)
class _CommonAlarmDetectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_CommonAlarmDetectionControl_Type.__name__=_C
_CommonAlarmDetectionControl_Object=MibScalar
commonAlarmDetectionControl=_CommonAlarmDetectionControl_Object((1,3,6,1,4,1,17409,1,3,1,8),_CommonAlarmDetectionControl_Type())
commonAlarmDetectionControl.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAlarmDetectionControl.setStatus(_A)
_CommonNetworkAddress_Type=IpAddress
_CommonNetworkAddress_Object=MibScalar
commonNetworkAddress=_CommonNetworkAddress_Object((1,3,6,1,4,1,17409,1,3,1,9),_CommonNetworkAddress_Type())
commonNetworkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:commonNetworkAddress.setStatus(_A)
_CommonCheckCode_Type=Integer32
_CommonCheckCode_Object=MibScalar
commonCheckCode=_CommonCheckCode_Object((1,3,6,1,4,1,17409,1,3,1,10),_CommonCheckCode_Type())
commonCheckCode.setMaxAccess(_D)
if mibBuilder.loadTexts:commonCheckCode.setStatus(_A)
class _CommonTrapCommunityString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CommonTrapCommunityString_Type.__name__=_H
_CommonTrapCommunityString_Object=MibScalar
commonTrapCommunityString=_CommonTrapCommunityString_Object((1,3,6,1,4,1,17409,1,3,1,11),_CommonTrapCommunityString_Type())
commonTrapCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:commonTrapCommunityString.setStatus(_A)
class _CommonTamperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_CommonTamperStatus_Type.__name__=_C
_CommonTamperStatus_Object=MibScalar
commonTamperStatus=_CommonTamperStatus_Object((1,3,6,1,4,1,17409,1,3,1,12),_CommonTamperStatus_Type())
commonTamperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonTamperStatus.setStatus(_E)
class _CommonInternalTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_CommonInternalTemperature_Type.__name__=_C
_CommonInternalTemperature_Object=MibScalar
commonInternalTemperature=_CommonInternalTemperature_Object((1,3,6,1,4,1,17409,1,3,1,13),_CommonInternalTemperature_Type())
commonInternalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:commonInternalTemperature.setStatus(_E)
_CommonTime_Type=Integer32
_CommonTime_Object=MibScalar
commonTime=_CommonTime_Object((1,3,6,1,4,1,17409,1,3,1,14),_CommonTime_Type())
commonTime.setMaxAccess(_D)
if mibBuilder.loadTexts:commonTime.setStatus(_E)
_CommonVarBindings_Type=Integer32
_CommonVarBindings_Object=MibScalar
commonVarBindings=_CommonVarBindings_Object((1,3,6,1,4,1,17409,1,3,1,15),_CommonVarBindings_Type())
commonVarBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:commonVarBindings.setStatus(_A)
class _CommonResetCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_V,2),(_W,3),(_X,4),('craft',5)))
_CommonResetCause_Type.__name__=_C
_CommonResetCause_Object=MibScalar
commonResetCause=_CommonResetCause_Object((1,3,6,1,4,1,17409,1,3,1,16),_CommonResetCause_Type())
commonResetCause.setMaxAccess(_B)
if mibBuilder.loadTexts:commonResetCause.setStatus(_A)
class _CommonCraftStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_CommonCraftStatus_Type.__name__=_C
_CommonCraftStatus_Object=MibScalar
commonCraftStatus=_CommonCraftStatus_Object((1,3,6,1,4,1,17409,1,3,1,17),_CommonCraftStatus_Type())
commonCraftStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonCraftStatus.setStatus(_A)
_CommonDeviceOID_Type=ObjectIdentifier
_CommonDeviceOID_Object=MibScalar
commonDeviceOID=_CommonDeviceOID_Object((1,3,6,1,4,1,17409,1,3,1,18),_CommonDeviceOID_Type())
commonDeviceOID.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceOID.setStatus(_E)
class _CommonDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_CommonDeviceId_Type.__name__=_H
_CommonDeviceId_Object=MibScalar
commonDeviceId=_CommonDeviceId_Object((1,3,6,1,4,1,17409,1,3,1,19),_CommonDeviceId_Type())
commonDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceId.setStatus(_E)
_CommonAdminUseRf_ObjectIdentity=ObjectIdentity
commonAdminUseRf=_CommonAdminUseRf_ObjectIdentity((1,3,6,1,4,1,17409,1,3,2))
_CommonMACGroup_ObjectIdentity=ObjectIdentity
commonMACGroup=_CommonMACGroup_ObjectIdentity((1,3,6,1,4,1,17409,1,3,2,1))
_CommonMacAddress_ObjectIdentity=ObjectIdentity
commonMacAddress=_CommonMacAddress_ObjectIdentity((1,3,6,1,4,1,17409,1,3,2,1,1))
_CommonPhysAddress_Type=OctetString
_CommonPhysAddress_Object=MibScalar
commonPhysAddress=_CommonPhysAddress_Object((1,3,6,1,4,1,17409,1,3,2,1,1,1),_CommonPhysAddress_Type())
commonPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:commonPhysAddress.setStatus(_A)
class _CommonMaxMulticastAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,255))
_CommonMaxMulticastAddresses_Type.__name__=_C
_CommonMaxMulticastAddresses_Object=MibScalar
commonMaxMulticastAddresses=_CommonMaxMulticastAddresses_Object((1,3,6,1,4,1,17409,1,3,2,1,1,2),_CommonMaxMulticastAddresses_Type())
commonMaxMulticastAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:commonMaxMulticastAddresses.setStatus(_A)
_CommonMulticastAddressTable_Object=MibTable
commonMulticastAddressTable=_CommonMulticastAddressTable_Object((1,3,6,1,4,1,17409,1,3,2,1,1,3))
if mibBuilder.loadTexts:commonMulticastAddressTable.setStatus(_A)
_CommonMulticastAddressEntry_Object=MibTableRow
commonMulticastAddressEntry=_CommonMulticastAddressEntry_Object((1,3,6,1,4,1,17409,1,3,2,1,1,3,1))
commonMulticastAddressEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:commonMulticastAddressEntry.setStatus(_A)
class _CommonMulticastAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CommonMulticastAddressIndex_Type.__name__=_C
_CommonMulticastAddressIndex_Object=MibTableColumn
commonMulticastAddressIndex=_CommonMulticastAddressIndex_Object((1,3,6,1,4,1,17409,1,3,2,1,1,3,1,1),_CommonMulticastAddressIndex_Type())
commonMulticastAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:commonMulticastAddressIndex.setStatus(_A)
class _CommonMulticastAddressNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CommonMulticastAddressNumber_Type.__name__=_H
_CommonMulticastAddressNumber_Object=MibTableColumn
commonMulticastAddressNumber=_CommonMulticastAddressNumber_Object((1,3,6,1,4,1,17409,1,3,2,1,1,3,1,2),_CommonMulticastAddressNumber_Type())
commonMulticastAddressNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:commonMulticastAddressNumber.setStatus(_A)
_CommonBackoffParams_ObjectIdentity=ObjectIdentity
commonBackoffParams=_CommonBackoffParams_ObjectIdentity((1,3,6,1,4,1,17409,1,3,2,1,2))
class _CommonBackoffPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_CommonBackoffPeriod_Type.__name__=_C
_CommonBackoffPeriod_Object=MibScalar
commonBackoffPeriod=_CommonBackoffPeriod_Object((1,3,6,1,4,1,17409,1,3,2,1,2,1),_CommonBackoffPeriod_Type())
commonBackoffPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:commonBackoffPeriod.setStatus(_A)
class _CommonACKTimeoutWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CommonACKTimeoutWindow_Type.__name__=_C
_CommonACKTimeoutWindow_Object=MibScalar
commonACKTimeoutWindow=_CommonACKTimeoutWindow_Object((1,3,6,1,4,1,17409,1,3,2,1,2,2),_CommonACKTimeoutWindow_Type())
commonACKTimeoutWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:commonACKTimeoutWindow.setStatus(_A)
class _CommonMaximumMACLayerRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CommonMaximumMACLayerRetries_Type.__name__=_C
_CommonMaximumMACLayerRetries_Object=MibScalar
commonMaximumMACLayerRetries=_CommonMaximumMACLayerRetries_Object((1,3,6,1,4,1,17409,1,3,2,1,2,3),_CommonMaximumMACLayerRetries_Type())
commonMaximumMACLayerRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:commonMaximumMACLayerRetries.setStatus(_A)
_CommonMaxPayloadSize_Type=Integer32
_CommonMaxPayloadSize_Object=MibScalar
commonMaxPayloadSize=_CommonMaxPayloadSize_Object((1,3,6,1,4,1,17409,1,3,2,1,2,4),_CommonMaxPayloadSize_Type())
commonMaxPayloadSize.setMaxAccess(_B)
if mibBuilder.loadTexts:commonMaxPayloadSize.setStatus(_A)
class _CommonBackoffMinimumExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CommonBackoffMinimumExponent_Type.__name__=_C
_CommonBackoffMinimumExponent_Object=MibScalar
commonBackoffMinimumExponent=_CommonBackoffMinimumExponent_Object((1,3,6,1,4,1,17409,1,3,2,1,2,5),_CommonBackoffMinimumExponent_Type())
commonBackoffMinimumExponent.setMaxAccess(_D)
if mibBuilder.loadTexts:commonBackoffMinimumExponent.setStatus(_A)
class _CommonBackoffMaximumExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CommonBackoffMaximumExponent_Type.__name__=_C
_CommonBackoffMaximumExponent_Object=MibScalar
commonBackoffMaximumExponent=_CommonBackoffMaximumExponent_Object((1,3,6,1,4,1,17409,1,3,2,1,2,6),_CommonBackoffMaximumExponent_Type())
commonBackoffMaximumExponent.setMaxAccess(_D)
if mibBuilder.loadTexts:commonBackoffMaximumExponent.setStatus(_A)
_CommonMacStats_ObjectIdentity=ObjectIdentity
commonMacStats=_CommonMacStats_ObjectIdentity((1,3,6,1,4,1,17409,1,3,2,1,3))
_CommonForwardPathLOSEvents_Type=Counter32
_CommonForwardPathLOSEvents_Object=MibScalar
commonForwardPathLOSEvents=_CommonForwardPathLOSEvents_Object((1,3,6,1,4,1,17409,1,3,2,1,3,1),_CommonForwardPathLOSEvents_Type())
commonForwardPathLOSEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:commonForwardPathLOSEvents.setStatus(_E)
_CommonForwardPathFramingErrors_Type=Counter32
_CommonForwardPathFramingErrors_Object=MibScalar
commonForwardPathFramingErrors=_CommonForwardPathFramingErrors_Object((1,3,6,1,4,1,17409,1,3,2,1,3,2),_CommonForwardPathFramingErrors_Type())
commonForwardPathFramingErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:commonForwardPathFramingErrors.setStatus(_E)
_CommonForwardPathCRCErrors_Type=Counter32
_CommonForwardPathCRCErrors_Object=MibScalar
commonForwardPathCRCErrors=_CommonForwardPathCRCErrors_Object((1,3,6,1,4,1,17409,1,3,2,1,3,3),_CommonForwardPathCRCErrors_Type())
commonForwardPathCRCErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:commonForwardPathCRCErrors.setStatus(_E)
_CommonInvalidMacCmds_Type=Counter32
_CommonInvalidMacCmds_Object=MibScalar
commonInvalidMacCmds=_CommonInvalidMacCmds_Object((1,3,6,1,4,1,17409,1,3,2,1,3,4),_CommonInvalidMacCmds_Type())
commonInvalidMacCmds.setMaxAccess(_D)
if mibBuilder.loadTexts:commonInvalidMacCmds.setStatus(_E)
_CommonBackwardPathCollisionTimes_Type=Counter32
_CommonBackwardPathCollisionTimes_Object=MibScalar
commonBackwardPathCollisionTimes=_CommonBackwardPathCollisionTimes_Object((1,3,6,1,4,1,17409,1,3,2,1,3,5),_CommonBackwardPathCollisionTimes_Type())
commonBackwardPathCollisionTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:commonBackwardPathCollisionTimes.setStatus(_E)
_CommonRfGroup_ObjectIdentity=ObjectIdentity
commonRfGroup=_CommonRfGroup_ObjectIdentity((1,3,6,1,4,1,17409,1,3,2,2))
class _CommonReturnPathFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CommonReturnPathFrequency_Type.__name__=_C
_CommonReturnPathFrequency_Object=MibScalar
commonReturnPathFrequency=_CommonReturnPathFrequency_Object((1,3,6,1,4,1,17409,1,3,2,2,1),_CommonReturnPathFrequency_Type())
commonReturnPathFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:commonReturnPathFrequency.setStatus(_A)
class _CommonForwardPathFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CommonForwardPathFrequency_Type.__name__=_C
_CommonForwardPathFrequency_Object=MibScalar
commonForwardPathFrequency=_CommonForwardPathFrequency_Object((1,3,6,1,4,1,17409,1,3,2,2,2),_CommonForwardPathFrequency_Type())
commonForwardPathFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:commonForwardPathFrequency.setStatus(_A)
class _CommonProvisionedReturnPowerLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CommonProvisionedReturnPowerLevel_Type.__name__=_C
_CommonProvisionedReturnPowerLevel_Object=MibScalar
commonProvisionedReturnPowerLevel=_CommonProvisionedReturnPowerLevel_Object((1,3,6,1,4,1,17409,1,3,2,2,3),_CommonProvisionedReturnPowerLevel_Type())
commonProvisionedReturnPowerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:commonProvisionedReturnPowerLevel.setStatus(_A)
class _CommonForwardPathReceiveLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CommonForwardPathReceiveLevel_Type.__name__=_C
_CommonForwardPathReceiveLevel_Object=MibScalar
commonForwardPathReceiveLevel=_CommonForwardPathReceiveLevel_Object((1,3,6,1,4,1,17409,1,3,2,2,4),_CommonForwardPathReceiveLevel_Type())
commonForwardPathReceiveLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:commonForwardPathReceiveLevel.setStatus(_E)
class _CommonMaxReturnPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CommonMaxReturnPower_Type.__name__=_C
_CommonMaxReturnPower_Object=MibScalar
commonMaxReturnPower=_CommonMaxReturnPower_Object((1,3,6,1,4,1,17409,1,3,2,2,5),_CommonMaxReturnPower_Type())
commonMaxReturnPower.setMaxAccess(_D)
if mibBuilder.loadTexts:commonMaxReturnPower.setStatus(_A)
_CommonAdminUseEthernet_ObjectIdentity=ObjectIdentity
commonAdminUseEthernet=_CommonAdminUseEthernet_ObjectIdentity((1,3,6,1,4,1,17409,1,3,3))
_CommonAgentGroup_ObjectIdentity=ObjectIdentity
commonAgentGroup=_CommonAgentGroup_ObjectIdentity((1,3,6,1,4,1,17409,1,3,3,1))
class _CommonAgentBootWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bootDefault',1),('bootBOOTP',2),('bootTFTP',3)))
_CommonAgentBootWay_Type.__name__=_C
_CommonAgentBootWay_Object=MibScalar
commonAgentBootWay=_CommonAgentBootWay_Object((1,3,6,1,4,1,17409,1,3,3,1,1),_CommonAgentBootWay_Type())
commonAgentBootWay.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentBootWay.setStatus(_A)
class _CommonAgentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_CommonAgentReset_Type.__name__=_C
_CommonAgentReset_Object=MibScalar
commonAgentReset=_CommonAgentReset_Object((1,3,6,1,4,1,17409,1,3,3,1,2),_CommonAgentReset_Type())
commonAgentReset.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentReset.setStatus(_A)
_CommonAgentMaxTraps_Type=Integer32
_CommonAgentMaxTraps_Object=MibScalar
commonAgentMaxTraps=_CommonAgentMaxTraps_Object((1,3,6,1,4,1,17409,1,3,3,1,3),_CommonAgentMaxTraps_Type())
commonAgentMaxTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentMaxTraps.setStatus(_A)
_CommonAgentTrapMinInterval_Type=Integer32
_CommonAgentTrapMinInterval_Object=MibScalar
commonAgentTrapMinInterval=_CommonAgentTrapMinInterval_Object((1,3,6,1,4,1,17409,1,3,3,1,4),_CommonAgentTrapMinInterval_Type())
commonAgentTrapMinInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentTrapMinInterval.setStatus(_A)
_CommonAgentTrapMaxInterval_Type=Integer32
_CommonAgentTrapMaxInterval_Object=MibScalar
commonAgentTrapMaxInterval=_CommonAgentTrapMaxInterval_Object((1,3,6,1,4,1,17409,1,3,3,1,5),_CommonAgentTrapMaxInterval_Type())
commonAgentTrapMaxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentTrapMaxInterval.setStatus(_A)
class _CommonTrapAck_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(17,255))
_CommonTrapAck_Type.__name__=_H
_CommonTrapAck_Object=MibScalar
commonTrapAck=_CommonTrapAck_Object((1,3,6,1,4,1,17409,1,3,3,1,6),_CommonTrapAck_Type())
commonTrapAck.setMaxAccess(_D)
if mibBuilder.loadTexts:commonTrapAck.setStatus(_E)
_CommonAgentTrapTable_Object=MibTable
commonAgentTrapTable=_CommonAgentTrapTable_Object((1,3,6,1,4,1,17409,1,3,3,1,7))
if mibBuilder.loadTexts:commonAgentTrapTable.setStatus(_A)
_CommonAgentTrapEntry_Object=MibTableRow
commonAgentTrapEntry=_CommonAgentTrapEntry_Object((1,3,6,1,4,1,17409,1,3,3,1,7,1))
commonAgentTrapEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:commonAgentTrapEntry.setStatus(_A)
_CommonAgentTrapIndex_Type=Integer32
_CommonAgentTrapIndex_Object=MibTableColumn
commonAgentTrapIndex=_CommonAgentTrapIndex_Object((1,3,6,1,4,1,17409,1,3,3,1,7,1,1),_CommonAgentTrapIndex_Type())
commonAgentTrapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:commonAgentTrapIndex.setStatus(_A)
_CommonAgentTrapIP_Type=IpAddress
_CommonAgentTrapIP_Object=MibTableColumn
commonAgentTrapIP=_CommonAgentTrapIP_Object((1,3,6,1,4,1,17409,1,3,3,1,7,1,2),_CommonAgentTrapIP_Type())
commonAgentTrapIP.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentTrapIP.setStatus(_A)
class _CommonAgentTrapCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CommonAgentTrapCommunity_Type.__name__=_G
_CommonAgentTrapCommunity_Object=MibTableColumn
commonAgentTrapCommunity=_CommonAgentTrapCommunity_Object((1,3,6,1,4,1,17409,1,3,3,1,7,1,3),_CommonAgentTrapCommunity_Type())
commonAgentTrapCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentTrapCommunity.setStatus(_A)
class _CommonAgentTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('commonAgentTrapEnable',1),('commonAgentTrapDisable',2)))
_CommonAgentTrapStatus_Type.__name__=_C
_CommonAgentTrapStatus_Object=MibTableColumn
commonAgentTrapStatus=_CommonAgentTrapStatus_Object((1,3,6,1,4,1,17409,1,3,3,1,7,1,4),_CommonAgentTrapStatus_Type())
commonAgentTrapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:commonAgentTrapStatus.setStatus(_A)
_CommonDeviceGroup_ObjectIdentity=ObjectIdentity
commonDeviceGroup=_CommonDeviceGroup_ObjectIdentity((1,3,6,1,4,1,17409,1,3,3,2))
_CommonDeviceNum_Type=Integer32
_CommonDeviceNum_Object=MibScalar
commonDeviceNum=_CommonDeviceNum_Object((1,3,6,1,4,1,17409,1,3,3,2,1),_CommonDeviceNum_Type())
commonDeviceNum.setMaxAccess(_D)
if mibBuilder.loadTexts:commonDeviceNum.setStatus(_A)
_CommonDeviceInfoTable_Object=MibTable
commonDeviceInfoTable=_CommonDeviceInfoTable_Object((1,3,6,1,4,1,17409,1,3,3,2,2))
if mibBuilder.loadTexts:commonDeviceInfoTable.setStatus(_A)
_CommonDeviceInfoEntry_Object=MibTableRow
commonDeviceInfoEntry=_CommonDeviceInfoEntry_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1))
commonDeviceInfoEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:commonDeviceInfoEntry.setStatus(_A)
_CommonDeviceSlot_Type=Integer32
_CommonDeviceSlot_Object=MibTableColumn
commonDeviceSlot=_CommonDeviceSlot_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,1),_CommonDeviceSlot_Type())
commonDeviceSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceSlot.setStatus(_A)
class _CommonDevicesID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CommonDevicesID_Type.__name__=_H
_CommonDevicesID_Object=MibTableColumn
commonDevicesID=_CommonDevicesID_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,2),_CommonDevicesID_Type())
commonDevicesID.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDevicesID.setStatus(_A)
class _CommonDeviceVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonDeviceVendor_Type.__name__=_G
_CommonDeviceVendor_Object=MibTableColumn
commonDeviceVendor=_CommonDeviceVendor_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,3),_CommonDeviceVendor_Type())
commonDeviceVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceVendor.setStatus(_A)
class _CommonDeviceModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonDeviceModelNumber_Type.__name__=_G
_CommonDeviceModelNumber_Object=MibTableColumn
commonDeviceModelNumber=_CommonDeviceModelNumber_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,4),_CommonDeviceModelNumber_Type())
commonDeviceModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceModelNumber.setStatus(_A)
class _CommonDeviceSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonDeviceSerialNumber_Type.__name__=_G
_CommonDeviceSerialNumber_Object=MibTableColumn
commonDeviceSerialNumber=_CommonDeviceSerialNumber_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,5),_CommonDeviceSerialNumber_Type())
commonDeviceSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceSerialNumber.setStatus(_A)
class _CommonDeviceVendorInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonDeviceVendorInfo_Type.__name__=_G
_CommonDeviceVendorInfo_Object=MibTableColumn
commonDeviceVendorInfo=_CommonDeviceVendorInfo_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,6),_CommonDeviceVendorInfo_Type())
commonDeviceVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceVendorInfo.setStatus(_E)
class _CommonDeviceStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CommonDeviceStatus_Type.__name__=_H
_CommonDeviceStatus_Object=MibTableColumn
commonDeviceStatus=_CommonDeviceStatus_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,7),_CommonDeviceStatus_Type())
commonDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceStatus.setStatus(_A)
class _CommonDeviceReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_CommonDeviceReset_Type.__name__=_C
_CommonDeviceReset_Object=MibTableColumn
commonDeviceReset=_CommonDeviceReset_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,8),_CommonDeviceReset_Type())
commonDeviceReset.setMaxAccess(_D)
if mibBuilder.loadTexts:commonDeviceReset.setStatus(_A)
class _CommonDeviceAlarmDetectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_CommonDeviceAlarmDetectionControl_Type.__name__=_C
_CommonDeviceAlarmDetectionControl_Object=MibTableColumn
commonDeviceAlarmDetectionControl=_CommonDeviceAlarmDetectionControl_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,9),_CommonDeviceAlarmDetectionControl_Type())
commonDeviceAlarmDetectionControl.setMaxAccess(_D)
if mibBuilder.loadTexts:commonDeviceAlarmDetectionControl.setStatus(_A)
_CommonDeviceMACAddress_Type=IpAddress
_CommonDeviceMACAddress_Object=MibTableColumn
commonDeviceMACAddress=_CommonDeviceMACAddress_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,10),_CommonDeviceMACAddress_Type())
commonDeviceMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceMACAddress.setStatus(_A)
class _CommonDeviceTamperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_CommonDeviceTamperStatus_Type.__name__=_C
_CommonDeviceTamperStatus_Object=MibTableColumn
commonDeviceTamperStatus=_CommonDeviceTamperStatus_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,11),_CommonDeviceTamperStatus_Type())
commonDeviceTamperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceTamperStatus.setStatus(_E)
class _CommonDeviceInternalTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_CommonDeviceInternalTemperature_Type.__name__=_C
_CommonDeviceInternalTemperature_Object=MibTableColumn
commonDeviceInternalTemperature=_CommonDeviceInternalTemperature_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,12),_CommonDeviceInternalTemperature_Type())
commonDeviceInternalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceInternalTemperature.setStatus(_E)
class _CommonDeviceResetCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_V,2),(_W,3),(_X,4),('craft',5)))
_CommonDeviceResetCause_Type.__name__=_C
_CommonDeviceResetCause_Object=MibTableColumn
commonDeviceResetCause=_CommonDeviceResetCause_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,13),_CommonDeviceResetCause_Type())
commonDeviceResetCause.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceResetCause.setStatus(_A)
class _CommonDeviceCraftStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_CommonDeviceCraftStatus_Type.__name__=_C
_CommonDeviceCraftStatus_Object=MibTableColumn
commonDeviceCraftStatus=_CommonDeviceCraftStatus_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,14),_CommonDeviceCraftStatus_Type())
commonDeviceCraftStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceCraftStatus.setStatus(_A)
_CommonDevicesOID_Type=ObjectIdentifier
_CommonDevicesOID_Object=MibTableColumn
commonDevicesOID=_CommonDevicesOID_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,15),_CommonDevicesOID_Type())
commonDevicesOID.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDevicesOID.setStatus(_A)
_CommonDeviceAcct_Type=Counter32
_CommonDeviceAcct_Object=MibTableColumn
commonDeviceAcct=_CommonDeviceAcct_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,16),_CommonDeviceAcct_Type())
commonDeviceAcct.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceAcct.setStatus(_E)
class _CommonDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonDeviceName_Type.__name__=_G
_CommonDeviceName_Object=MibTableColumn
commonDeviceName=_CommonDeviceName_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,17),_CommonDeviceName_Type())
commonDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceName.setStatus(_A)
class _CommonDeviceMFD_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_CommonDeviceMFD_Type.__name__=_G
_CommonDeviceMFD_Object=MibTableColumn
commonDeviceMFD=_CommonDeviceMFD_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,18),_CommonDeviceMFD_Type())
commonDeviceMFD.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceMFD.setStatus(_A)
class _CommonDeviceFW_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CommonDeviceFW_Type.__name__=_G
_CommonDeviceFW_Object=MibTableColumn
commonDeviceFW=_CommonDeviceFW_Object((1,3,6,1,4,1,17409,1,3,3,2,2,1,19),_CommonDeviceFW_Type())
commonDeviceFW.setMaxAccess(_B)
if mibBuilder.loadTexts:commonDeviceFW.setStatus(_A)
_OswIdent_ObjectIdentity=ObjectIdentity
oswIdent=_OswIdent_ObjectIdentity((1,3,6,1,4,1,17409,1,15))
_OswVendorOID_Type=ObjectIdentifier
_OswVendorOID_Object=MibScalar
oswVendorOID=_OswVendorOID_Object((1,3,6,1,4,1,17409,1,15,1),_OswVendorOID_Type())
oswVendorOID.setMaxAccess(_B)
if mibBuilder.loadTexts:oswVendorOID.setStatus(_E)
class _OswMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_OswMode_Type.__name__=_C
_OswMode_Object=MibScalar
oswMode=_OswMode_Object((1,3,6,1,4,1,17409,1,15,2),_OswMode_Type())
oswMode.setMaxAccess(_D)
if mibBuilder.loadTexts:oswMode.setStatus(_A)
class _OswSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OswSwitch_Type.__name__=_C
_OswSwitch_Object=MibScalar
oswSwitch=_OswSwitch_Object((1,3,6,1,4,1,17409,1,15,3),_OswSwitch_Type())
oswSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:oswSwitch.setStatus(_A)
_OswChannelTable_Object=MibTable
oswChannelTable=_OswChannelTable_Object((1,3,6,1,4,1,17409,1,15,4))
if mibBuilder.loadTexts:oswChannelTable.setStatus(_A)
_OswChannelEntry_Object=MibTableRow
oswChannelEntry=_OswChannelEntry_Object((1,3,6,1,4,1,17409,1,15,4,1))
oswChannelEntry.setIndexNames((0,_F,'oswIndex'))
if mibBuilder.loadTexts:oswChannelEntry.setStatus(_A)
_OswUnitTemp_Type=Integer32
_OswUnitTemp_Object=MibTableColumn
oswUnitTemp=_OswUnitTemp_Object((1,3,6,1,4,1,17409,1,15,4,1,1),_OswUnitTemp_Type())
oswUnitTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oswUnitTemp.setStatus(_A)
class _OswInputA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_OswInputA_Type.__name__=_C
_OswInputA_Object=MibTableColumn
oswInputA=_OswInputA_Object((1,3,6,1,4,1,17409,1,15,4,1,2),_OswInputA_Type())
oswInputA.setMaxAccess(_B)
if mibBuilder.loadTexts:oswInputA.setStatus(_A)
class _OswInputB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_OswInputB_Type.__name__=_C
_OswInputB_Object=MibTableColumn
oswInputB=_OswInputB_Object((1,3,6,1,4,1,17409,1,15,4,1,3),_OswInputB_Type())
oswInputB.setMaxAccess(_B)
if mibBuilder.loadTexts:oswInputB.setStatus(_A)
class _OswOutput1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OswOutput1_Type.__name__=_C
_OswOutput1_Object=MibTableColumn
oswOutput1=_OswOutput1_Object((1,3,6,1,4,1,17409,1,15,4,1,4),_OswOutput1_Type())
oswOutput1.setMaxAccess(_B)
if mibBuilder.loadTexts:oswOutput1.setStatus(_A)
class _OswOutput2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OswOutput2_Type.__name__=_C
_OswOutput2_Object=MibTableColumn
oswOutput2=_OswOutput2_Object((1,3,6,1,4,1,17409,1,15,4,1,5),_OswOutput2_Type())
oswOutput2.setMaxAccess(_B)
if mibBuilder.loadTexts:oswOutput2.setStatus(_A)
class _OswNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_OswNumberDCPowerSupply_Type.__name__=_C
_OswNumberDCPowerSupply_Object=MibScalar
oswNumberDCPowerSupply=_OswNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,15,5),_OswNumberDCPowerSupply_Type())
oswNumberDCPowerSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:oswNumberDCPowerSupply.setStatus(_A)
class _OswDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2),('aloneSupply',3)))
_OswDCPowerSupplyMode_Type.__name__=_C
_OswDCPowerSupplyMode_Object=MibScalar
oswDCPowerSupplyMode=_OswDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,15,6),_OswDCPowerSupplyMode_Type())
oswDCPowerSupplyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oswDCPowerSupplyMode.setStatus(_E)
_OswDCPowerTable_Object=MibTable
oswDCPowerTable=_OswDCPowerTable_Object((1,3,6,1,4,1,17409,1,15,7))
if mibBuilder.loadTexts:oswDCPowerTable.setStatus(_A)
_OswDCPowerEntry_Object=MibTableRow
oswDCPowerEntry=_OswDCPowerEntry_Object((1,3,6,1,4,1,17409,1,15,7,1))
oswDCPowerEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:oswDCPowerEntry.setStatus(_A)
_OswDCPowerIndex_Type=Integer32
_OswDCPowerIndex_Object=MibTableColumn
oswDCPowerIndex=_OswDCPowerIndex_Object((1,3,6,1,4,1,17409,1,15,7,1,1),_OswDCPowerIndex_Type())
oswDCPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oswDCPowerIndex.setStatus(_A)
class _OswDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OswDCPowerVoltage_Type.__name__=_C
_OswDCPowerVoltage_Object=MibTableColumn
oswDCPowerVoltage=_OswDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,15,7,1,2),_OswDCPowerVoltage_Type())
oswDCPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:oswDCPowerVoltage.setStatus(_A)
class _OswDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OswDCPowerCurrent_Type.__name__=_C
_OswDCPowerCurrent_Object=MibTableColumn
oswDCPowerCurrent=_OswDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,15,7,1,3),_OswDCPowerCurrent_Type())
oswDCPowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:oswDCPowerCurrent.setStatus(_A)
_OswDCPowerName_Type=DisplayString
_OswDCPowerName_Object=MibTableColumn
oswDCPowerName=_OswDCPowerName_Object((1,3,6,1,4,1,17409,1,15,7,1,4),_OswDCPowerName_Type())
oswDCPowerName.setMaxAccess(_B)
if mibBuilder.loadTexts:oswDCPowerName.setStatus(_A)
hfcColdStart=NotificationType((1,3,6,1,4,1,17409,1,0,0))
hfcColdStart.setObjects(*((_F,_I),(_F,_J)))
if mibBuilder.loadTexts:hfcColdStart.setStatus('')
hfcAlarmEvent=NotificationType((1,3,6,1,4,1,17409,1,0,1))
hfcAlarmEvent.setObjects(*((_F,_I),(_F,_J),(_F,_e),(_F,_f)))
if mibBuilder.loadTexts:hfcAlarmEvent.setStatus('')
hfcWarmStart=NotificationType((1,3,6,1,4,1,17409,1,0,2))
hfcWarmStart.setObjects(*((_F,_I),(_F,_J)))
if mibBuilder.loadTexts:hfcWarmStart.setStatus('')
mibBuilder.exportSymbols(_F,**{'nscrtvRoot':nscrtvRoot,'nscrtvHFCemsTree':nscrtvHFCemsTree,'hfcColdStart':hfcColdStart,'hfcAlarmEvent':hfcAlarmEvent,'hfcWarmStart':hfcWarmStart,'propertyIdent':propertyIdent,'analogPropertyTable':analogPropertyTable,'analogPropertyEntry':analogPropertyEntry,_L:analogParameterOID,'alarmEnable':alarmEnable,'analogAlarmState':analogAlarmState,'analogAlarmHIHI':analogAlarmHIHI,'analogAlarmHI':analogAlarmHI,'analogAlarmLO':analogAlarmLO,'analogAlarmLOLO':analogAlarmLOLO,'analogAlarmDeadband':analogAlarmDeadband,'discretePropertyTable':discretePropertyTable,'discretePropertyEntry':discretePropertyEntry,_M:discreteParameterOID,_N:discreteAlarmValue,'discreteAlarmEnable':discreteAlarmEnable,'discreteAlarmState':discreteAlarmState,'currentAlarmTable':currentAlarmTable,'currentAlarmEntry':currentAlarmEntry,_O:currentAlarmOID,'currentAlarmState':currentAlarmState,'currentAlarmValue':currentAlarmValue,'alarmsIdent':alarmsIdent,'alarmLogNumberOfEntries':alarmLogNumberOfEntries,'alarmLogLastIndex':alarmLogLastIndex,'alarmLogTable':alarmLogTable,'alarmLogEntry':alarmLogEntry,_P:alarmLogIndex,_e:alarmLogInformation,_f:alarmText,'commonIdent':commonIdent,'commonAdminGroup':commonAdminGroup,_J:commonNELogicalID,'commonNEVendor':commonNEVendor,'commonNEModelNumber':commonNEModelNumber,'commonNESerialNumber':commonNESerialNumber,'commonNEVendorInfo':commonNEVendorInfo,'commonNEStatus':commonNEStatus,'commonReset':commonReset,'commonAlarmDetectionControl':commonAlarmDetectionControl,'commonNetworkAddress':commonNetworkAddress,'commonCheckCode':commonCheckCode,'commonTrapCommunityString':commonTrapCommunityString,'commonTamperStatus':commonTamperStatus,'commonInternalTemperature':commonInternalTemperature,'commonTime':commonTime,'commonVarBindings':commonVarBindings,'commonResetCause':commonResetCause,'commonCraftStatus':commonCraftStatus,'commonDeviceOID':commonDeviceOID,'commonDeviceId':commonDeviceId,'commonAdminUseRf':commonAdminUseRf,'commonMACGroup':commonMACGroup,'commonMacAddress':commonMacAddress,_I:commonPhysAddress,'commonMaxMulticastAddresses':commonMaxMulticastAddresses,'commonMulticastAddressTable':commonMulticastAddressTable,'commonMulticastAddressEntry':commonMulticastAddressEntry,_a:commonMulticastAddressIndex,'commonMulticastAddressNumber':commonMulticastAddressNumber,'commonBackoffParams':commonBackoffParams,'commonBackoffPeriod':commonBackoffPeriod,'commonACKTimeoutWindow':commonACKTimeoutWindow,'commonMaximumMACLayerRetries':commonMaximumMACLayerRetries,'commonMaxPayloadSize':commonMaxPayloadSize,'commonBackoffMinimumExponent':commonBackoffMinimumExponent,'commonBackoffMaximumExponent':commonBackoffMaximumExponent,'commonMacStats':commonMacStats,'commonForwardPathLOSEvents':commonForwardPathLOSEvents,'commonForwardPathFramingErrors':commonForwardPathFramingErrors,'commonForwardPathCRCErrors':commonForwardPathCRCErrors,'commonInvalidMacCmds':commonInvalidMacCmds,'commonBackwardPathCollisionTimes':commonBackwardPathCollisionTimes,'commonRfGroup':commonRfGroup,'commonReturnPathFrequency':commonReturnPathFrequency,'commonForwardPathFrequency':commonForwardPathFrequency,'commonProvisionedReturnPowerLevel':commonProvisionedReturnPowerLevel,'commonForwardPathReceiveLevel':commonForwardPathReceiveLevel,'commonMaxReturnPower':commonMaxReturnPower,'commonAdminUseEthernet':commonAdminUseEthernet,'commonAgentGroup':commonAgentGroup,'commonAgentBootWay':commonAgentBootWay,'commonAgentReset':commonAgentReset,'commonAgentMaxTraps':commonAgentMaxTraps,'commonAgentTrapMinInterval':commonAgentTrapMinInterval,'commonAgentTrapMaxInterval':commonAgentTrapMaxInterval,'commonTrapAck':commonTrapAck,'commonAgentTrapTable':commonAgentTrapTable,'commonAgentTrapEntry':commonAgentTrapEntry,_b:commonAgentTrapIndex,'commonAgentTrapIP':commonAgentTrapIP,'commonAgentTrapCommunity':commonAgentTrapCommunity,'commonAgentTrapStatus':commonAgentTrapStatus,'commonDeviceGroup':commonDeviceGroup,'commonDeviceNum':commonDeviceNum,'commonDeviceInfoTable':commonDeviceInfoTable,'commonDeviceInfoEntry':commonDeviceInfoEntry,_c:commonDeviceSlot,'commonDevicesID':commonDevicesID,'commonDeviceVendor':commonDeviceVendor,'commonDeviceModelNumber':commonDeviceModelNumber,'commonDeviceSerialNumber':commonDeviceSerialNumber,'commonDeviceVendorInfo':commonDeviceVendorInfo,'commonDeviceStatus':commonDeviceStatus,'commonDeviceReset':commonDeviceReset,'commonDeviceAlarmDetectionControl':commonDeviceAlarmDetectionControl,'commonDeviceMACAddress':commonDeviceMACAddress,'commonDeviceTamperStatus':commonDeviceTamperStatus,'commonDeviceInternalTemperature':commonDeviceInternalTemperature,'commonDeviceResetCause':commonDeviceResetCause,'commonDeviceCraftStatus':commonDeviceCraftStatus,'commonDevicesOID':commonDevicesOID,'commonDeviceAcct':commonDeviceAcct,'commonDeviceName':commonDeviceName,'commonDeviceMFD':commonDeviceMFD,'commonDeviceFW':commonDeviceFW,'oswIdent':oswIdent,'oswVendorOID':oswVendorOID,'oswMode':oswMode,'oswSwitch':oswSwitch,'oswChannelTable':oswChannelTable,'oswChannelEntry':oswChannelEntry,'oswUnitTemp':oswUnitTemp,'oswInputA':oswInputA,'oswInputB':oswInputB,'oswOutput1':oswOutput1,'oswOutput2':oswOutput2,'oswNumberDCPowerSupply':oswNumberDCPowerSupply,'oswDCPowerSupplyMode':oswDCPowerSupplyMode,'oswDCPowerTable':oswDCPowerTable,'oswDCPowerEntry':oswDCPowerEntry,_d:oswDCPowerIndex,'oswDCPowerVoltage':oswDCPowerVoltage,'oswDCPowerCurrent':oswDCPowerCurrent,'oswDCPowerName':oswDCPowerName})