_T='ringswitchPortTestError'
_S='ringswitchPortAdapterStatus'
_R='ringswitchBaseExtFanSpeed'
_Q='ringswitchBasePSFanSpeed'
_P='ringswitchLANRingIndex'
_O='ringswitchLANRingGroup'
_N='invalid'
_M='ringswitchLANIndex'
_L='ringswitchLCDNum'
_K='same-ring'
_J='ringswitchPortNum'
_I='DisplayString'
_H='NotificationType'
_G='enable'
_F='disable'
_E='MADGERSW-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
class INTEGER48(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class LCDText(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(50,50));fixedLength=50
_Madge_ObjectIdentity=ObjectIdentity
madge=_Madge_ObjectIdentity((1,3,6,1,4,1,494))
_Ringswitch_ObjectIdentity=ObjectIdentity
ringswitch=_Ringswitch_ObjectIdentity((1,3,6,1,4,1,494,4))
_RingswitchBase_ObjectIdentity=ObjectIdentity
ringswitchBase=_RingswitchBase_ObjectIdentity((1,3,6,1,4,1,494,4,1))
_RingswitchBasePSFanSpeed_Type=Integer32
_RingswitchBasePSFanSpeed_Object=MibScalar
ringswitchBasePSFanSpeed=_RingswitchBasePSFanSpeed_Object((1,3,6,1,4,1,494,4,1,1),_RingswitchBasePSFanSpeed_Type())
ringswitchBasePSFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchBasePSFanSpeed.setStatus(_A)
_RingswitchBaseExtFanSpeed_Type=Integer32
_RingswitchBaseExtFanSpeed_Object=MibScalar
ringswitchBaseExtFanSpeed=_RingswitchBaseExtFanSpeed_Object((1,3,6,1,4,1,494,4,1,2),_RingswitchBaseExtFanSpeed_Type())
ringswitchBaseExtFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchBaseExtFanSpeed.setStatus(_A)
class _RingswitchBaseRipSapSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_RingswitchBaseRipSapSuppression_Type.__name__=_C
_RingswitchBaseRipSapSuppression_Object=MibScalar
ringswitchBaseRipSapSuppression=_RingswitchBaseRipSapSuppression_Object((1,3,6,1,4,1,494,4,1,3),_RingswitchBaseRipSapSuppression_Type())
ringswitchBaseRipSapSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchBaseRipSapSuppression.setStatus(_A)
class _RingswitchBaseAREConversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('enable-first',1),('enable-all',2),('enable-bcast-first',3),('enable-bcast-all',4),(_F,5)))
_RingswitchBaseAREConversion_Type.__name__=_C
_RingswitchBaseAREConversion_Object=MibScalar
ringswitchBaseAREConversion=_RingswitchBaseAREConversion_Object((1,3,6,1,4,1,494,4,1,4),_RingswitchBaseAREConversion_Type())
ringswitchBaseAREConversion.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchBaseAREConversion.setStatus(_A)
_RingswitchPort_ObjectIdentity=ObjectIdentity
ringswitchPort=_RingswitchPort_ObjectIdentity((1,3,6,1,4,1,494,4,2))
_RingswitchPortTable_Object=MibTable
ringswitchPortTable=_RingswitchPortTable_Object((1,3,6,1,4,1,494,4,2,1))
if mibBuilder.loadTexts:ringswitchPortTable.setStatus(_A)
_RingswitchPortEntry_Object=MibTableRow
ringswitchPortEntry=_RingswitchPortEntry_Object((1,3,6,1,4,1,494,4,2,1,1))
ringswitchPortEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:ringswitchPortEntry.setStatus(_A)
class _RingswitchPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RingswitchPortNum_Type.__name__=_C
_RingswitchPortNum_Object=MibTableColumn
ringswitchPortNum=_RingswitchPortNum_Object((1,3,6,1,4,1,494,4,2,1,1,1),_RingswitchPortNum_Type())
ringswitchPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortNum.setStatus(_A)
class _RingswitchPortRingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('single',2),('beaconing',3)))
_RingswitchPortRingStatus_Type.__name__=_C
_RingswitchPortRingStatus_Object=MibTableColumn
ringswitchPortRingStatus=_RingswitchPortRingStatus_Object((1,3,6,1,4,1,494,4,2,1,1,2),_RingswitchPortRingStatus_Type())
ringswitchPortRingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortRingStatus.setStatus(_A)
class _RingswitchPortAdapterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('open',1),('closed',2),('opening',3)))
_RingswitchPortAdapterStatus_Type.__name__=_C
_RingswitchPortAdapterStatus_Object=MibTableColumn
ringswitchPortAdapterStatus=_RingswitchPortAdapterStatus_Object((1,3,6,1,4,1,494,4,2,1,1,3),_RingswitchPortAdapterStatus_Type())
ringswitchPortAdapterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortAdapterStatus.setStatus(_A)
class _RingswitchPortMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tr-copper',1),('tr-fiber',2),('fddi-fiber',3)))
_RingswitchPortMediaType_Type.__name__=_C
_RingswitchPortMediaType_Object=MibTableColumn
ringswitchPortMediaType=_RingswitchPortMediaType_Object((1,3,6,1,4,1,494,4,2,1,1,4),_RingswitchPortMediaType_Type())
ringswitchPortMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortMediaType.setStatus(_A)
class _RingswitchPortIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('node',1),('concentrator',2)))
_RingswitchPortIfMode_Type.__name__=_C
_RingswitchPortIfMode_Object=MibTableColumn
ringswitchPortIfMode=_RingswitchPortIfMode_Object((1,3,6,1,4,1,494,4,2,1,1,5),_RingswitchPortIfMode_Type())
ringswitchPortIfMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchPortIfMode.setStatus(_A)
class _RingswitchPortRingSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('four',1),('sixteen',2),('hundred',3)))
_RingswitchPortRingSpeed_Type.__name__=_C
_RingswitchPortRingSpeed_Object=MibTableColumn
ringswitchPortRingSpeed=_RingswitchPortRingSpeed_Object((1,3,6,1,4,1,494,4,2,1,1,6),_RingswitchPortRingSpeed_Type())
ringswitchPortRingSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchPortRingSpeed.setStatus(_A)
class _RingswitchPortTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('disabled',1),('running',2),('failed',3),('ok',4),('unknown',5)))
_RingswitchPortTestState_Type.__name__=_C
_RingswitchPortTestState_Object=MibTableColumn
ringswitchPortTestState=_RingswitchPortTestState_Object((1,3,6,1,4,1,494,4,2,1,1,7),_RingswitchPortTestState_Type())
ringswitchPortTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortTestState.setStatus(_A)
class _RingswitchPortTestError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('no-error',1),(_K,2),('duplicate-ring',3),('fail-nb',4),('bad-rnum',5),('fail-b',6)))
_RingswitchPortTestError_Type.__name__=_C
_RingswitchPortTestError_Object=MibTableColumn
ringswitchPortTestError=_RingswitchPortTestError_Object((1,3,6,1,4,1,494,4,2,1,1,8),_RingswitchPortTestError_Type())
ringswitchPortTestError.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortTestError.setStatus(_A)
class _RingswitchPortTestPhase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('not-running',1),(_K,2),('routed',3),('broadcast',4),('success',5)))
_RingswitchPortTestPhase_Type.__name__=_C
_RingswitchPortTestPhase_Object=MibTableColumn
ringswitchPortTestPhase=_RingswitchPortTestPhase_Object((1,3,6,1,4,1,494,4,2,1,1,9),_RingswitchPortTestPhase_Type())
ringswitchPortTestPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortTestPhase.setStatus(_A)
_RingswitchPortSummary_Type=Integer32
_RingswitchPortSummary_Object=MibTableColumn
ringswitchPortSummary=_RingswitchPortSummary_Object((1,3,6,1,4,1,494,4,2,1,1,10),_RingswitchPortSummary_Type())
ringswitchPortSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortSummary.setStatus(_A)
_RingswitchPortAddress_Type=PhysAddress
_RingswitchPortAddress_Object=MibTableColumn
ringswitchPortAddress=_RingswitchPortAddress_Object((1,3,6,1,4,1,494,4,2,1,1,11),_RingswitchPortAddress_Type())
ringswitchPortAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortAddress.setStatus(_A)
_RingswitchPortLAA_Type=PhysAddress
_RingswitchPortLAA_Object=MibTableColumn
ringswitchPortLAA=_RingswitchPortLAA_Object((1,3,6,1,4,1,494,4,2,1,1,12),_RingswitchPortLAA_Type())
ringswitchPortLAA.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchPortLAA.setStatus(_A)
class _RingswitchPortStationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('anything',1),('workstations',2)))
_RingswitchPortStationType_Type.__name__=_C
_RingswitchPortStationType_Object=MibTableColumn
ringswitchPortStationType=_RingswitchPortStationType_Object((1,3,6,1,4,1,494,4,2,1,1,13),_RingswitchPortStationType_Type())
ringswitchPortStationType.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchPortStationType.setStatus(_A)
class _RingswitchPortRPSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_RingswitchPortRPSEnable_Type.__name__=_C
_RingswitchPortRPSEnable_Object=MibTableColumn
ringswitchPortRPSEnable=_RingswitchPortRPSEnable_Object((1,3,6,1,4,1,494,4,2,1,1,14),_RingswitchPortRPSEnable_Type())
ringswitchPortRPSEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchPortRPSEnable.setStatus(_A)
class _RingswitchPortCutThruEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_RingswitchPortCutThruEnable_Type.__name__=_C
_RingswitchPortCutThruEnable_Object=MibTableColumn
ringswitchPortCutThruEnable=_RingswitchPortCutThruEnable_Object((1,3,6,1,4,1,494,4,2,1,1,15),_RingswitchPortCutThruEnable_Type())
ringswitchPortCutThruEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchPortCutThruEnable.setStatus(_A)
_RingswitchPortInOctets_Type=INTEGER48
_RingswitchPortInOctets_Object=MibTableColumn
ringswitchPortInOctets=_RingswitchPortInOctets_Object((1,3,6,1,4,1,494,4,2,1,1,16),_RingswitchPortInOctets_Type())
ringswitchPortInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortInOctets.setStatus(_A)
_RingswitchPortOutOctets_Type=INTEGER48
_RingswitchPortOutOctets_Object=MibTableColumn
ringswitchPortOutOctets=_RingswitchPortOutOctets_Object((1,3,6,1,4,1,494,4,2,1,1,17),_RingswitchPortOutOctets_Type())
ringswitchPortOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortOutOctets.setStatus(_A)
_RingswitchPortSpecInFrames_Type=INTEGER48
_RingswitchPortSpecInFrames_Object=MibTableColumn
ringswitchPortSpecInFrames=_RingswitchPortSpecInFrames_Object((1,3,6,1,4,1,494,4,2,1,1,18),_RingswitchPortSpecInFrames_Type())
ringswitchPortSpecInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortSpecInFrames.setStatus(_A)
_RingswitchPortSpecOutFrames_Type=INTEGER48
_RingswitchPortSpecOutFrames_Object=MibTableColumn
ringswitchPortSpecOutFrames=_RingswitchPortSpecOutFrames_Object((1,3,6,1,4,1,494,4,2,1,1,19),_RingswitchPortSpecOutFrames_Type())
ringswitchPortSpecOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortSpecOutFrames.setStatus(_A)
_RingswitchPortApeInFrames_Type=INTEGER48
_RingswitchPortApeInFrames_Object=MibTableColumn
ringswitchPortApeInFrames=_RingswitchPortApeInFrames_Object((1,3,6,1,4,1,494,4,2,1,1,20),_RingswitchPortApeInFrames_Type())
ringswitchPortApeInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortApeInFrames.setStatus(_A)
_RingswitchPortApeOutFrames_Type=INTEGER48
_RingswitchPortApeOutFrames_Object=MibTableColumn
ringswitchPortApeOutFrames=_RingswitchPortApeOutFrames_Object((1,3,6,1,4,1,494,4,2,1,1,21),_RingswitchPortApeOutFrames_Type())
ringswitchPortApeOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortApeOutFrames.setStatus(_A)
_RingswitchPortSteInFrames_Type=INTEGER48
_RingswitchPortSteInFrames_Object=MibTableColumn
ringswitchPortSteInFrames=_RingswitchPortSteInFrames_Object((1,3,6,1,4,1,494,4,2,1,1,22),_RingswitchPortSteInFrames_Type())
ringswitchPortSteInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortSteInFrames.setStatus(_A)
_RingswitchPortSteOutFrames_Type=INTEGER48
_RingswitchPortSteOutFrames_Object=MibTableColumn
ringswitchPortSteOutFrames=_RingswitchPortSteOutFrames_Object((1,3,6,1,4,1,494,4,2,1,1,23),_RingswitchPortSteOutFrames_Type())
ringswitchPortSteOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchPortSteOutFrames.setStatus(_A)
_RingswitchSR_ObjectIdentity=ObjectIdentity
ringswitchSR=_RingswitchSR_ObjectIdentity((1,3,6,1,4,1,494,4,3))
class _RingswitchSRAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_RingswitchSRAdminState_Type.__name__=_C
_RingswitchSRAdminState_Object=MibScalar
ringswitchSRAdminState=_RingswitchSRAdminState_Object((1,3,6,1,4,1,494,4,3,1),_RingswitchSRAdminState_Type())
ringswitchSRAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchSRAdminState.setStatus(_A)
class _RingswitchSROperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_RingswitchSROperState_Type.__name__=_C
_RingswitchSROperState_Object=MibScalar
ringswitchSROperState=_RingswitchSROperState_Object((1,3,6,1,4,1,494,4,3,2),_RingswitchSROperState_Type())
ringswitchSROperState.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchSROperState.setStatus(_A)
_RingswitchLCD_ObjectIdentity=ObjectIdentity
ringswitchLCD=_RingswitchLCD_ObjectIdentity((1,3,6,1,4,1,494,4,4))
class _RingswitchLCDTotalDisplays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RingswitchLCDTotalDisplays_Type.__name__=_C
_RingswitchLCDTotalDisplays_Object=MibScalar
ringswitchLCDTotalDisplays=_RingswitchLCDTotalDisplays_Object((1,3,6,1,4,1,494,4,4,1),_RingswitchLCDTotalDisplays_Type())
ringswitchLCDTotalDisplays.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchLCDTotalDisplays.setStatus(_A)
class _RingswitchLCDCurrentDisplay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RingswitchLCDCurrentDisplay_Type.__name__=_C
_RingswitchLCDCurrentDisplay_Object=MibScalar
ringswitchLCDCurrentDisplay=_RingswitchLCDCurrentDisplay_Object((1,3,6,1,4,1,494,4,4,2),_RingswitchLCDCurrentDisplay_Type())
ringswitchLCDCurrentDisplay.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchLCDCurrentDisplay.setStatus(_A)
_RingswitchLCDCurrentMsgText_Type=LCDText
_RingswitchLCDCurrentMsgText_Object=MibScalar
ringswitchLCDCurrentMsgText=_RingswitchLCDCurrentMsgText_Object((1,3,6,1,4,1,494,4,4,3),_RingswitchLCDCurrentMsgText_Type())
ringswitchLCDCurrentMsgText.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchLCDCurrentMsgText.setStatus(_A)
_RingswitchLCDTable_Object=MibTable
ringswitchLCDTable=_RingswitchLCDTable_Object((1,3,6,1,4,1,494,4,4,4))
if mibBuilder.loadTexts:ringswitchLCDTable.setStatus(_A)
_RingswitchLCDTableEntry_Object=MibTableRow
ringswitchLCDTableEntry=_RingswitchLCDTableEntry_Object((1,3,6,1,4,1,494,4,4,4,1))
ringswitchLCDTableEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:ringswitchLCDTableEntry.setStatus(_A)
class _RingswitchLCDNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RingswitchLCDNum_Type.__name__=_C
_RingswitchLCDNum_Object=MibTableColumn
ringswitchLCDNum=_RingswitchLCDNum_Object((1,3,6,1,4,1,494,4,4,4,1,1),_RingswitchLCDNum_Type())
ringswitchLCDNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchLCDNum.setStatus(_A)
_RingswitchLCDMsgText_Type=LCDText
_RingswitchLCDMsgText_Object=MibTableColumn
ringswitchLCDMsgText=_RingswitchLCDMsgText_Object((1,3,6,1,4,1,494,4,4,4,1,2),_RingswitchLCDMsgText_Type())
ringswitchLCDMsgText.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchLCDMsgText.setStatus(_A)
_RingswitchLAN_ObjectIdentity=ObjectIdentity
ringswitchLAN=_RingswitchLAN_ObjectIdentity((1,3,6,1,4,1,494,4,5))
_RingswitchLANTable_Object=MibTable
ringswitchLANTable=_RingswitchLANTable_Object((1,3,6,1,4,1,494,4,5,1))
if mibBuilder.loadTexts:ringswitchLANTable.setStatus(_A)
_RingswitchLANEntry_Object=MibTableRow
ringswitchLANEntry=_RingswitchLANEntry_Object((1,3,6,1,4,1,494,4,5,1,1))
ringswitchLANEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:ringswitchLANEntry.setStatus(_A)
class _RingswitchLANIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RingswitchLANIndex_Type.__name__=_C
_RingswitchLANIndex_Object=MibTableColumn
ringswitchLANIndex=_RingswitchLANIndex_Object((1,3,6,1,4,1,494,4,5,1,1,1),_RingswitchLANIndex_Type())
ringswitchLANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchLANIndex.setStatus(_A)
_RingswitchLANName_Type=DisplayString
_RingswitchLANName_Object=MibTableColumn
ringswitchLANName=_RingswitchLANName_Object((1,3,6,1,4,1,494,4,5,1,1,2),_RingswitchLANName_Type())
ringswitchLANName.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchLANName.setStatus(_A)
class _RingswitchLANPermeable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('impermeable',1),('permeable',2)))
_RingswitchLANPermeable_Type.__name__=_C
_RingswitchLANPermeable_Object=MibTableColumn
ringswitchLANPermeable=_RingswitchLANPermeable_Object((1,3,6,1,4,1,494,4,5,1,1,3),_RingswitchLANPermeable_Type())
ringswitchLANPermeable.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchLANPermeable.setStatus(_A)
class _RingswitchLANStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_N,2)))
_RingswitchLANStatus_Type.__name__=_C
_RingswitchLANStatus_Object=MibTableColumn
ringswitchLANStatus=_RingswitchLANStatus_Object((1,3,6,1,4,1,494,4,5,1,1,4),_RingswitchLANStatus_Type())
ringswitchLANStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchLANStatus.setStatus(_A)
_RingswitchLANRingTable_Object=MibTable
ringswitchLANRingTable=_RingswitchLANRingTable_Object((1,3,6,1,4,1,494,4,5,2))
if mibBuilder.loadTexts:ringswitchLANRingTable.setStatus(_A)
_RingswitchLANRingEntry_Object=MibTableRow
ringswitchLANRingEntry=_RingswitchLANRingEntry_Object((1,3,6,1,4,1,494,4,5,2,1))
ringswitchLANRingEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:ringswitchLANRingEntry.setStatus(_A)
_RingswitchLANRingGroup_Type=Integer32
_RingswitchLANRingGroup_Object=MibTableColumn
ringswitchLANRingGroup=_RingswitchLANRingGroup_Object((1,3,6,1,4,1,494,4,5,2,1,1),_RingswitchLANRingGroup_Type())
ringswitchLANRingGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchLANRingGroup.setStatus(_A)
_RingswitchLANRingIndex_Type=Integer32
_RingswitchLANRingIndex_Object=MibTableColumn
ringswitchLANRingIndex=_RingswitchLANRingIndex_Object((1,3,6,1,4,1,494,4,5,2,1,2),_RingswitchLANRingIndex_Type())
ringswitchLANRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringswitchLANRingIndex.setStatus(_A)
_RingswitchLANRingNum_Type=Integer32
_RingswitchLANRingNum_Object=MibTableColumn
ringswitchLANRingNum=_RingswitchLANRingNum_Object((1,3,6,1,4,1,494,4,5,2,1,3),_RingswitchLANRingNum_Type())
ringswitchLANRingNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchLANRingNum.setStatus(_A)
class _RingswitchLANRingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_N,2)))
_RingswitchLANRingStatus_Type.__name__=_C
_RingswitchLANRingStatus_Object=MibTableColumn
ringswitchLANRingStatus=_RingswitchLANRingStatus_Object((1,3,6,1,4,1,494,4,5,2,1,4),_RingswitchLANRingStatus_Type())
ringswitchLANRingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ringswitchLANRingStatus.setStatus(_A)
fanPSSpeedFailed=NotificationType((1,3,6,1,4,1,494,4,0,1))
fanPSSpeedFailed.setObjects((_E,_Q))
if mibBuilder.loadTexts:fanPSSpeedFailed.setStatus('')
fanExtSpeedFailed=NotificationType((1,3,6,1,4,1,494,4,0,2))
fanExtSpeedFailed.setObjects((_E,_R))
if mibBuilder.loadTexts:fanExtSpeedFailed.setStatus('')
portFailed=NotificationType((1,3,6,1,4,1,494,4,0,3))
portFailed.setObjects((_E,_S))
if mibBuilder.loadTexts:portFailed.setStatus('')
brTestFailed=NotificationType((1,3,6,1,4,1,494,4,0,4))
brTestFailed.setObjects((_E,_T))
if mibBuilder.loadTexts:brTestFailed.setStatus('')
mibBuilder.exportSymbols(_E,**{_I:DisplayString,'INTEGER48':INTEGER48,'LCDText':LCDText,'madge':madge,'ringswitch':ringswitch,'fanPSSpeedFailed':fanPSSpeedFailed,'fanExtSpeedFailed':fanExtSpeedFailed,'portFailed':portFailed,'brTestFailed':brTestFailed,'ringswitchBase':ringswitchBase,_Q:ringswitchBasePSFanSpeed,_R:ringswitchBaseExtFanSpeed,'ringswitchBaseRipSapSuppression':ringswitchBaseRipSapSuppression,'ringswitchBaseAREConversion':ringswitchBaseAREConversion,'ringswitchPort':ringswitchPort,'ringswitchPortTable':ringswitchPortTable,'ringswitchPortEntry':ringswitchPortEntry,_J:ringswitchPortNum,'ringswitchPortRingStatus':ringswitchPortRingStatus,_S:ringswitchPortAdapterStatus,'ringswitchPortMediaType':ringswitchPortMediaType,'ringswitchPortIfMode':ringswitchPortIfMode,'ringswitchPortRingSpeed':ringswitchPortRingSpeed,'ringswitchPortTestState':ringswitchPortTestState,_T:ringswitchPortTestError,'ringswitchPortTestPhase':ringswitchPortTestPhase,'ringswitchPortSummary':ringswitchPortSummary,'ringswitchPortAddress':ringswitchPortAddress,'ringswitchPortLAA':ringswitchPortLAA,'ringswitchPortStationType':ringswitchPortStationType,'ringswitchPortRPSEnable':ringswitchPortRPSEnable,'ringswitchPortCutThruEnable':ringswitchPortCutThruEnable,'ringswitchPortInOctets':ringswitchPortInOctets,'ringswitchPortOutOctets':ringswitchPortOutOctets,'ringswitchPortSpecInFrames':ringswitchPortSpecInFrames,'ringswitchPortSpecOutFrames':ringswitchPortSpecOutFrames,'ringswitchPortApeInFrames':ringswitchPortApeInFrames,'ringswitchPortApeOutFrames':ringswitchPortApeOutFrames,'ringswitchPortSteInFrames':ringswitchPortSteInFrames,'ringswitchPortSteOutFrames':ringswitchPortSteOutFrames,'ringswitchSR':ringswitchSR,'ringswitchSRAdminState':ringswitchSRAdminState,'ringswitchSROperState':ringswitchSROperState,'ringswitchLCD':ringswitchLCD,'ringswitchLCDTotalDisplays':ringswitchLCDTotalDisplays,'ringswitchLCDCurrentDisplay':ringswitchLCDCurrentDisplay,'ringswitchLCDCurrentMsgText':ringswitchLCDCurrentMsgText,'ringswitchLCDTable':ringswitchLCDTable,'ringswitchLCDTableEntry':ringswitchLCDTableEntry,_L:ringswitchLCDNum,'ringswitchLCDMsgText':ringswitchLCDMsgText,'ringswitchLAN':ringswitchLAN,'ringswitchLANTable':ringswitchLANTable,'ringswitchLANEntry':ringswitchLANEntry,_M:ringswitchLANIndex,'ringswitchLANName':ringswitchLANName,'ringswitchLANPermeable':ringswitchLANPermeable,'ringswitchLANStatus':ringswitchLANStatus,'ringswitchLANRingTable':ringswitchLANRingTable,'ringswitchLANRingEntry':ringswitchLANRingEntry,_O:ringswitchLANRingGroup,_P:ringswitchLANRingIndex,'ringswitchLANRingNum':ringswitchLANRingNum,'ringswitchLANRingStatus':ringswitchLANRingStatus})