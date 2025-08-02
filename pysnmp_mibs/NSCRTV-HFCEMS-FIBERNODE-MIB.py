_N='fnDCPowerIndex'
_M='fnABSwitchIndex'
_L='fnRFPortIndex'
_K='fnRFActiveIndex'
_J='fnOpticalReceiverIndex'
_I='fnReturnLaserIndex'
_H='off'
_G='none'
_F='NSCRTV-HFCEMS-FIBERNODE-MIB'
_E='read-write'
_D='optional'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fnIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','fnIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_FnVendorOID_Type=ObjectIdentifier
_FnVendorOID_Object=MibScalar
fnVendorOID=_FnVendorOID_Object((1,3,6,1,4,1,17409,1,10,1),_FnVendorOID_Type())
fnVendorOID.setMaxAccess(_A)
if mibBuilder.loadTexts:fnVendorOID.setStatus(_D)
class _FnNumberReturnLaser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_FnNumberReturnLaser_Type.__name__=_C
_FnNumberReturnLaser_Object=MibScalar
fnNumberReturnLaser=_FnNumberReturnLaser_Object((1,3,6,1,4,1,17409,1,10,2),_FnNumberReturnLaser_Type())
fnNumberReturnLaser.setMaxAccess(_E)
if mibBuilder.loadTexts:fnNumberReturnLaser.setStatus(_B)
_FnReturnLaserTable_Object=MibTable
fnReturnLaserTable=_FnReturnLaserTable_Object((1,3,6,1,4,1,17409,1,10,3))
if mibBuilder.loadTexts:fnReturnLaserTable.setStatus(_B)
_FnReturnLaserEntry_Object=MibTableRow
fnReturnLaserEntry=_FnReturnLaserEntry_Object((1,3,6,1,4,1,17409,1,10,3,1))
fnReturnLaserEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:fnReturnLaserEntry.setStatus(_B)
_FnReturnLaserIndex_Type=Integer32
_FnReturnLaserIndex_Object=MibTableColumn
fnReturnLaserIndex=_FnReturnLaserIndex_Object((1,3,6,1,4,1,17409,1,10,3,1,1),_FnReturnLaserIndex_Type())
fnReturnLaserIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:fnReturnLaserIndex.setStatus(_B)
class _FnReturnLaserCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnReturnLaserCurrent_Type.__name__=_C
_FnReturnLaserCurrent_Object=MibTableColumn
fnReturnLaserCurrent=_FnReturnLaserCurrent_Object((1,3,6,1,4,1,17409,1,10,3,1,2),_FnReturnLaserCurrent_Type())
fnReturnLaserCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:fnReturnLaserCurrent.setStatus(_D)
class _FnReturnLaserTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_FnReturnLaserTemp_Type.__name__=_C
_FnReturnLaserTemp_Object=MibTableColumn
fnReturnLaserTemp=_FnReturnLaserTemp_Object((1,3,6,1,4,1,17409,1,10,3,1,3),_FnReturnLaserTemp_Type())
fnReturnLaserTemp.setMaxAccess(_A)
if mibBuilder.loadTexts:fnReturnLaserTemp.setStatus(_D)
class _FnReturnLaserControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('on',2)))
_FnReturnLaserControl_Type.__name__=_C
_FnReturnLaserControl_Object=MibTableColumn
fnReturnLaserControl=_FnReturnLaserControl_Object((1,3,6,1,4,1,17409,1,10,3,1,4),_FnReturnLaserControl_Type())
fnReturnLaserControl.setMaxAccess(_E)
if mibBuilder.loadTexts:fnReturnLaserControl.setStatus(_D)
_FnReturnLaserType_Type=DisplayString
_FnReturnLaserType_Object=MibTableColumn
fnReturnLaserType=_FnReturnLaserType_Object((1,3,6,1,4,1,17409,1,10,3,1,5),_FnReturnLaserType_Type())
fnReturnLaserType.setMaxAccess(_A)
if mibBuilder.loadTexts:fnReturnLaserType.setStatus(_D)
_FnReturnLaserWavelength_Type=DisplayString
_FnReturnLaserWavelength_Object=MibTableColumn
fnReturnLaserWavelength=_FnReturnLaserWavelength_Object((1,3,6,1,4,1,17409,1,10,3,1,6),_FnReturnLaserWavelength_Type())
fnReturnLaserWavelength.setMaxAccess(_A)
if mibBuilder.loadTexts:fnReturnLaserWavelength.setStatus(_D)
class _FnReverseOpticalPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnReverseOpticalPower_Type.__name__=_C
_FnReverseOpticalPower_Object=MibTableColumn
fnReverseOpticalPower=_FnReverseOpticalPower_Object((1,3,6,1,4,1,17409,1,10,3,1,7),_FnReverseOpticalPower_Type())
fnReverseOpticalPower.setMaxAccess(_A)
if mibBuilder.loadTexts:fnReverseOpticalPower.setStatus(_B)
_FnReturnLaserRFActive_Type=Integer32
_FnReturnLaserRFActive_Object=MibTableColumn
fnReturnLaserRFActive=_FnReturnLaserRFActive_Object((1,3,6,1,4,1,17409,1,10,3,1,8),_FnReturnLaserRFActive_Type())
fnReturnLaserRFActive.setMaxAccess(_A)
if mibBuilder.loadTexts:fnReturnLaserRFActive.setStatus(_B)
class _FnNumberOpticalReceiver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_FnNumberOpticalReceiver_Type.__name__=_C
_FnNumberOpticalReceiver_Object=MibScalar
fnNumberOpticalReceiver=_FnNumberOpticalReceiver_Object((1,3,6,1,4,1,17409,1,10,4),_FnNumberOpticalReceiver_Type())
fnNumberOpticalReceiver.setMaxAccess(_A)
if mibBuilder.loadTexts:fnNumberOpticalReceiver.setStatus(_B)
_FnOpticalReceiverTable_Object=MibTable
fnOpticalReceiverTable=_FnOpticalReceiverTable_Object((1,3,6,1,4,1,17409,1,10,5))
if mibBuilder.loadTexts:fnOpticalReceiverTable.setStatus(_B)
_FnOpticalReceiverEntry_Object=MibTableRow
fnOpticalReceiverEntry=_FnOpticalReceiverEntry_Object((1,3,6,1,4,1,17409,1,10,5,1))
fnOpticalReceiverEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:fnOpticalReceiverEntry.setStatus(_B)
_FnOpticalReceiverIndex_Type=Integer32
_FnOpticalReceiverIndex_Object=MibTableColumn
fnOpticalReceiverIndex=_FnOpticalReceiverIndex_Object((1,3,6,1,4,1,17409,1,10,5,1,1),_FnOpticalReceiverIndex_Type())
fnOpticalReceiverIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:fnOpticalReceiverIndex.setStatus(_B)
class _FnOpticalReceiverPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnOpticalReceiverPower_Type.__name__=_C
_FnOpticalReceiverPower_Object=MibTableColumn
fnOpticalReceiverPower=_FnOpticalReceiverPower_Object((1,3,6,1,4,1,17409,1,10,5,1,2),_FnOpticalReceiverPower_Type())
fnOpticalReceiverPower.setMaxAccess(_A)
if mibBuilder.loadTexts:fnOpticalReceiverPower.setStatus(_B)
class _FnOpticalReceiverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('on',2)))
_FnOpticalReceiverState_Type.__name__=_C
_FnOpticalReceiverState_Object=MibTableColumn
fnOpticalReceiverState=_FnOpticalReceiverState_Object((1,3,6,1,4,1,17409,1,10,5,1,3),_FnOpticalReceiverState_Type())
fnOpticalReceiverState.setMaxAccess(_A)
if mibBuilder.loadTexts:fnOpticalReceiverState.setStatus(_D)
_FnOpticalReceiverRFActive_Type=Integer32
_FnOpticalReceiverRFActive_Object=MibTableColumn
fnOpticalReceiverRFActive=_FnOpticalReceiverRFActive_Object((1,3,6,1,4,1,17409,1,10,5,1,4),_FnOpticalReceiverRFActive_Type())
fnOpticalReceiverRFActive.setMaxAccess(_A)
if mibBuilder.loadTexts:fnOpticalReceiverRFActive.setStatus(_B)
class _FnOpticalAmpPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_FnOpticalAmpPresent_Type.__name__=_C
_FnOpticalAmpPresent_Object=MibScalar
fnOpticalAmpPresent=_FnOpticalAmpPresent_Object((1,3,6,1,4,1,17409,1,10,6),_FnOpticalAmpPresent_Type())
fnOpticalAmpPresent.setMaxAccess(_A)
if mibBuilder.loadTexts:fnOpticalAmpPresent.setStatus(_B)
class _FnNumberRFActives_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FnNumberRFActives_Type.__name__=_C
_FnNumberRFActives_Object=MibScalar
fnNumberRFActives=_FnNumberRFActives_Object((1,3,6,1,4,1,17409,1,10,7),_FnNumberRFActives_Type())
fnNumberRFActives.setMaxAccess(_A)
if mibBuilder.loadTexts:fnNumberRFActives.setStatus(_B)
_FnRFActiveTable_Object=MibTable
fnRFActiveTable=_FnRFActiveTable_Object((1,3,6,1,4,1,17409,1,10,8))
if mibBuilder.loadTexts:fnRFActiveTable.setStatus(_B)
_FnRFActiveEntry_Object=MibTableRow
fnRFActiveEntry=_FnRFActiveEntry_Object((1,3,6,1,4,1,17409,1,10,8,1))
fnRFActiveEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:fnRFActiveEntry.setStatus(_B)
_FnRFActiveIndex_Type=Integer32
_FnRFActiveIndex_Object=MibTableColumn
fnRFActiveIndex=_FnRFActiveIndex_Object((1,3,6,1,4,1,17409,1,10,8,1,1),_FnRFActiveIndex_Type())
fnRFActiveIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFActiveIndex.setStatus(_B)
class _FnRFActiveControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('alc',1),('asc',2),('agc',3),(_G,4)))
_FnRFActiveControlType_Type.__name__=_C
_FnRFActiveControlType_Object=MibTableColumn
fnRFActiveControlType=_FnRFActiveControlType_Object((1,3,6,1,4,1,17409,1,10,8,1,2),_FnRFActiveControlType_Type())
fnRFActiveControlType.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFActiveControlType.setStatus(_D)
class _FnRFActiveOutputLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_FnRFActiveOutputLevel_Type.__name__=_C
_FnRFActiveOutputLevel_Object=MibTableColumn
fnRFActiveOutputLevel=_FnRFActiveOutputLevel_Object((1,3,6,1,4,1,17409,1,10,8,1,3),_FnRFActiveOutputLevel_Type())
fnRFActiveOutputLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFActiveOutputLevel.setStatus(_D)
class _FnRFActiveCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnRFActiveCurrent_Type.__name__=_C
_FnRFActiveCurrent_Object=MibTableColumn
fnRFActiveCurrent=_FnRFActiveCurrent_Object((1,3,6,1,4,1,17409,1,10,8,1,4),_FnRFActiveCurrent_Type())
fnRFActiveCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFActiveCurrent.setStatus(_D)
_FnRFActiveControlLevel_Type=Integer32
_FnRFActiveControlLevel_Object=MibTableColumn
fnRFActiveControlLevel=_FnRFActiveControlLevel_Object((1,3,6,1,4,1,17409,1,10,8,1,5),_FnRFActiveControlLevel_Type())
fnRFActiveControlLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFActiveControlLevel.setStatus(_D)
class _FnNumberRFPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_FnNumberRFPort_Type.__name__=_C
_FnNumberRFPort_Object=MibScalar
fnNumberRFPort=_FnNumberRFPort_Object((1,3,6,1,4,1,17409,1,10,9),_FnNumberRFPort_Type())
fnNumberRFPort.setMaxAccess(_A)
if mibBuilder.loadTexts:fnNumberRFPort.setStatus(_B)
class _FnPortMasterAttenuationControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('low',2),('high',3)))
_FnPortMasterAttenuationControl_Type.__name__=_C
_FnPortMasterAttenuationControl_Object=MibScalar
fnPortMasterAttenuationControl=_FnPortMasterAttenuationControl_Object((1,3,6,1,4,1,17409,1,10,10),_FnPortMasterAttenuationControl_Type())
fnPortMasterAttenuationControl.setMaxAccess(_E)
if mibBuilder.loadTexts:fnPortMasterAttenuationControl.setStatus(_D)
_FnRFPortTable_Object=MibTable
fnRFPortTable=_FnRFPortTable_Object((1,3,6,1,4,1,17409,1,10,11))
if mibBuilder.loadTexts:fnRFPortTable.setStatus(_B)
_FnRFPortEntry_Object=MibTableRow
fnRFPortEntry=_FnRFPortEntry_Object((1,3,6,1,4,1,17409,1,10,11,1))
fnRFPortEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:fnRFPortEntry.setStatus(_B)
_FnRFPortIndex_Type=Integer32
_FnRFPortIndex_Object=MibTableColumn
fnRFPortIndex=_FnRFPortIndex_Object((1,3,6,1,4,1,17409,1,10,11,1,1),_FnRFPortIndex_Type())
fnRFPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFPortIndex.setStatus(_B)
class _FnRFPortControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('alc',1),('asc',2),('agc',3),(_G,4)))
_FnRFPortControlType_Type.__name__=_C
_FnRFPortControlType_Object=MibTableColumn
fnRFPortControlType=_FnRFPortControlType_Object((1,3,6,1,4,1,17409,1,10,11,1,2),_FnRFPortControlType_Type())
fnRFPortControlType.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFPortControlType.setStatus(_D)
_FnRFPortControlLevel_Type=Integer32
_FnRFPortControlLevel_Object=MibTableColumn
fnRFPortControlLevel=_FnRFPortControlLevel_Object((1,3,6,1,4,1,17409,1,10,11,1,3),_FnRFPortControlLevel_Type())
fnRFPortControlLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFPortControlLevel.setStatus(_D)
class _FnRFPortOutputRFLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_FnRFPortOutputRFLevel_Type.__name__=_C
_FnRFPortOutputRFLevel_Object=MibTableColumn
fnRFPortOutputRFLevel=_FnRFPortOutputRFLevel_Object((1,3,6,1,4,1,17409,1,10,11,1,4),_FnRFPortOutputRFLevel_Type())
fnRFPortOutputRFLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFPortOutputRFLevel.setStatus(_D)
_FnRFPortRFActive_Type=Integer32
_FnRFPortRFActive_Object=MibTableColumn
fnRFPortRFActive=_FnRFPortRFActive_Object((1,3,6,1,4,1,17409,1,10,11,1,5),_FnRFPortRFActive_Type())
fnRFPortRFActive.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFPortRFActive.setStatus(_B)
_FnRFPortName_Type=DisplayString
_FnRFPortName_Object=MibTableColumn
fnRFPortName=_FnRFPortName_Object((1,3,6,1,4,1,17409,1,10,11,1,6),_FnRFPortName_Type())
fnRFPortName.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFPortName.setStatus(_B)
class _FnRFPortReverseAttenuationControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('low',2),('high',3)))
_FnRFPortReverseAttenuationControl_Type.__name__=_C
_FnRFPortReverseAttenuationControl_Object=MibTableColumn
fnRFPortReverseAttenuationControl=_FnRFPortReverseAttenuationControl_Object((1,3,6,1,4,1,17409,1,10,11,1,7),_FnRFPortReverseAttenuationControl_Type())
fnRFPortReverseAttenuationControl.setMaxAccess(_E)
if mibBuilder.loadTexts:fnRFPortReverseAttenuationControl.setStatus(_D)
class _FnRFPortPowerFeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_H,2)))
_FnRFPortPowerFeedStatus_Type.__name__=_C
_FnRFPortPowerFeedStatus_Object=MibTableColumn
fnRFPortPowerFeedStatus=_FnRFPortPowerFeedStatus_Object((1,3,6,1,4,1,17409,1,10,11,1,8),_FnRFPortPowerFeedStatus_Type())
fnRFPortPowerFeedStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:fnRFPortPowerFeedStatus.setStatus(_D)
class _FnRFPortRFlevelatt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnRFPortRFlevelatt_Type.__name__=_C
_FnRFPortRFlevelatt_Object=MibTableColumn
fnRFPortRFlevelatt=_FnRFPortRFlevelatt_Object((1,3,6,1,4,1,17409,1,10,11,1,9),_FnRFPortRFlevelatt_Type())
fnRFPortRFlevelatt.setMaxAccess(_E)
if mibBuilder.loadTexts:fnRFPortRFlevelatt.setStatus(_D)
class _FnRFPortRFleveleq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnRFPortRFleveleq_Type.__name__=_C
_FnRFPortRFleveleq_Object=MibTableColumn
fnRFPortRFleveleq=_FnRFPortRFleveleq_Object((1,3,6,1,4,1,17409,1,10,11,1,10),_FnRFPortRFleveleq_Type())
fnRFPortRFleveleq.setMaxAccess(_E)
if mibBuilder.loadTexts:fnRFPortRFleveleq.setStatus(_D)
class _FnRFPortReverseatt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnRFPortReverseatt_Type.__name__=_C
_FnRFPortReverseatt_Object=MibTableColumn
fnRFPortReverseatt=_FnRFPortReverseatt_Object((1,3,6,1,4,1,17409,1,10,11,1,11),_FnRFPortReverseatt_Type())
fnRFPortReverseatt.setMaxAccess(_E)
if mibBuilder.loadTexts:fnRFPortReverseatt.setStatus(_D)
class _FnRFPortReverseeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnRFPortReverseeq_Type.__name__=_C
_FnRFPortReverseeq_Object=MibTableColumn
fnRFPortReverseeq=_FnRFPortReverseeq_Object((1,3,6,1,4,1,17409,1,10,11,1,12),_FnRFPortReverseeq_Type())
fnRFPortReverseeq.setMaxAccess(_E)
if mibBuilder.loadTexts:fnRFPortReverseeq.setStatus(_D)
class _FnNumberABSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_FnNumberABSwitch_Type.__name__=_C
_FnNumberABSwitch_Object=MibScalar
fnNumberABSwitch=_FnNumberABSwitch_Object((1,3,6,1,4,1,17409,1,10,12),_FnNumberABSwitch_Type())
fnNumberABSwitch.setMaxAccess(_A)
if mibBuilder.loadTexts:fnNumberABSwitch.setStatus(_B)
_FnABSwitchTable_Object=MibTable
fnABSwitchTable=_FnABSwitchTable_Object((1,3,6,1,4,1,17409,1,10,13))
if mibBuilder.loadTexts:fnABSwitchTable.setStatus(_B)
_FnABSwitchEntry_Object=MibTableRow
fnABSwitchEntry=_FnABSwitchEntry_Object((1,3,6,1,4,1,17409,1,10,13,1))
fnABSwitchEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:fnABSwitchEntry.setStatus(_B)
_FnABSwitchIndex_Type=Integer32
_FnABSwitchIndex_Object=MibTableColumn
fnABSwitchIndex=_FnABSwitchIndex_Object((1,3,6,1,4,1,17409,1,10,13,1,1),_FnABSwitchIndex_Type())
fnABSwitchIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:fnABSwitchIndex.setStatus(_B)
class _FnOpticalReceiverABSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pathA',1),('pathB',2)))
_FnOpticalReceiverABSwitchState_Type.__name__=_C
_FnOpticalReceiverABSwitchState_Object=MibTableColumn
fnOpticalReceiverABSwitchState=_FnOpticalReceiverABSwitchState_Object((1,3,6,1,4,1,17409,1,10,13,1,2),_FnOpticalReceiverABSwitchState_Type())
fnOpticalReceiverABSwitchState.setMaxAccess(_A)
if mibBuilder.loadTexts:fnOpticalReceiverABSwitchState.setStatus(_B)
class _FnOpticalReceiverABSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forcePathA',1),('forcePathB',2),('preferPathA',3),('preferPathB',4)))
_FnOpticalReceiverABSwitchControl_Type.__name__=_C
_FnOpticalReceiverABSwitchControl_Object=MibTableColumn
fnOpticalReceiverABSwitchControl=_FnOpticalReceiverABSwitchControl_Object((1,3,6,1,4,1,17409,1,10,13,1,3),_FnOpticalReceiverABSwitchControl_Type())
fnOpticalReceiverABSwitchControl.setMaxAccess(_E)
if mibBuilder.loadTexts:fnOpticalReceiverABSwitchControl.setStatus(_B)
class _FnLinePowerVoltage1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnLinePowerVoltage1_Type.__name__=_C
_FnLinePowerVoltage1_Object=MibScalar
fnLinePowerVoltage1=_FnLinePowerVoltage1_Object((1,3,6,1,4,1,17409,1,10,14),_FnLinePowerVoltage1_Type())
fnLinePowerVoltage1.setMaxAccess(_A)
if mibBuilder.loadTexts:fnLinePowerVoltage1.setStatus(_D)
class _FnLinePowerVoltage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnLinePowerVoltage2_Type.__name__=_C
_FnLinePowerVoltage2_Object=MibScalar
fnLinePowerVoltage2=_FnLinePowerVoltage2_Object((1,3,6,1,4,1,17409,1,10,15),_FnLinePowerVoltage2_Type())
fnLinePowerVoltage2.setMaxAccess(_A)
if mibBuilder.loadTexts:fnLinePowerVoltage2.setStatus(_D)
class _FnLinePowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnLinePowerCurrent_Type.__name__=_C
_FnLinePowerCurrent_Object=MibScalar
fnLinePowerCurrent=_FnLinePowerCurrent_Object((1,3,6,1,4,1,17409,1,10,16),_FnLinePowerCurrent_Type())
fnLinePowerCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:fnLinePowerCurrent.setStatus(_D)
class _FnNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_FnNumberDCPowerSupply_Type.__name__=_C
_FnNumberDCPowerSupply_Object=MibScalar
fnNumberDCPowerSupply=_FnNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,10,17),_FnNumberDCPowerSupply_Type())
fnNumberDCPowerSupply.setMaxAccess(_A)
if mibBuilder.loadTexts:fnNumberDCPowerSupply.setStatus(_B)
class _FnDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2)))
_FnDCPowerSupplyMode_Type.__name__=_C
_FnDCPowerSupplyMode_Object=MibScalar
fnDCPowerSupplyMode=_FnDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,10,18),_FnDCPowerSupplyMode_Type())
fnDCPowerSupplyMode.setMaxAccess(_A)
if mibBuilder.loadTexts:fnDCPowerSupplyMode.setStatus(_D)
_FnDCPowerTable_Object=MibTable
fnDCPowerTable=_FnDCPowerTable_Object((1,3,6,1,4,1,17409,1,10,19))
if mibBuilder.loadTexts:fnDCPowerTable.setStatus(_B)
_FnDCPowerEntry_Object=MibTableRow
fnDCPowerEntry=_FnDCPowerEntry_Object((1,3,6,1,4,1,17409,1,10,19,1))
fnDCPowerEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:fnDCPowerEntry.setStatus(_B)
_FnDCPowerIndex_Type=Integer32
_FnDCPowerIndex_Object=MibTableColumn
fnDCPowerIndex=_FnDCPowerIndex_Object((1,3,6,1,4,1,17409,1,10,19,1,1),_FnDCPowerIndex_Type())
fnDCPowerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:fnDCPowerIndex.setStatus(_B)
class _FnDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_FnDCPowerVoltage_Type.__name__=_C
_FnDCPowerVoltage_Object=MibTableColumn
fnDCPowerVoltage=_FnDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,10,19,1,2),_FnDCPowerVoltage_Type())
fnDCPowerVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:fnDCPowerVoltage.setStatus(_B)
class _FnDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnDCPowerCurrent_Type.__name__=_C
_FnDCPowerCurrent_Object=MibTableColumn
fnDCPowerCurrent=_FnDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,10,19,1,3),_FnDCPowerCurrent_Type())
fnDCPowerCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:fnDCPowerCurrent.setStatus(_D)
_FnDCPowerName_Type=DisplayString
_FnDCPowerName_Object=MibTableColumn
fnDCPowerName=_FnDCPowerName_Object((1,3,6,1,4,1,17409,1,10,19,1,4),_FnDCPowerName_Type())
fnDCPowerName.setMaxAccess(_A)
if mibBuilder.loadTexts:fnDCPowerName.setStatus(_B)
class _FnReturnRFPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_FnReturnRFPower_Type.__name__=_C
_FnReturnRFPower_Object=MibScalar
fnReturnRFPower=_FnReturnRFPower_Object((1,3,6,1,4,1,17409,1,10,26),_FnReturnRFPower_Type())
fnReturnRFPower.setMaxAccess(_E)
if mibBuilder.loadTexts:fnReturnRFPower.setStatus(_B)
mibBuilder.exportSymbols(_F,**{'fnVendorOID':fnVendorOID,'fnNumberReturnLaser':fnNumberReturnLaser,'fnReturnLaserTable':fnReturnLaserTable,'fnReturnLaserEntry':fnReturnLaserEntry,_I:fnReturnLaserIndex,'fnReturnLaserCurrent':fnReturnLaserCurrent,'fnReturnLaserTemp':fnReturnLaserTemp,'fnReturnLaserControl':fnReturnLaserControl,'fnReturnLaserType':fnReturnLaserType,'fnReturnLaserWavelength':fnReturnLaserWavelength,'fnReverseOpticalPower':fnReverseOpticalPower,'fnReturnLaserRFActive':fnReturnLaserRFActive,'fnNumberOpticalReceiver':fnNumberOpticalReceiver,'fnOpticalReceiverTable':fnOpticalReceiverTable,'fnOpticalReceiverEntry':fnOpticalReceiverEntry,_J:fnOpticalReceiverIndex,'fnOpticalReceiverPower':fnOpticalReceiverPower,'fnOpticalReceiverState':fnOpticalReceiverState,'fnOpticalReceiverRFActive':fnOpticalReceiverRFActive,'fnOpticalAmpPresent':fnOpticalAmpPresent,'fnNumberRFActives':fnNumberRFActives,'fnRFActiveTable':fnRFActiveTable,'fnRFActiveEntry':fnRFActiveEntry,_K:fnRFActiveIndex,'fnRFActiveControlType':fnRFActiveControlType,'fnRFActiveOutputLevel':fnRFActiveOutputLevel,'fnRFActiveCurrent':fnRFActiveCurrent,'fnRFActiveControlLevel':fnRFActiveControlLevel,'fnNumberRFPort':fnNumberRFPort,'fnPortMasterAttenuationControl':fnPortMasterAttenuationControl,'fnRFPortTable':fnRFPortTable,'fnRFPortEntry':fnRFPortEntry,_L:fnRFPortIndex,'fnRFPortControlType':fnRFPortControlType,'fnRFPortControlLevel':fnRFPortControlLevel,'fnRFPortOutputRFLevel':fnRFPortOutputRFLevel,'fnRFPortRFActive':fnRFPortRFActive,'fnRFPortName':fnRFPortName,'fnRFPortReverseAttenuationControl':fnRFPortReverseAttenuationControl,'fnRFPortPowerFeedStatus':fnRFPortPowerFeedStatus,'fnRFPortRFlevelatt':fnRFPortRFlevelatt,'fnRFPortRFleveleq':fnRFPortRFleveleq,'fnRFPortReverseatt':fnRFPortReverseatt,'fnRFPortReverseeq':fnRFPortReverseeq,'fnNumberABSwitch':fnNumberABSwitch,'fnABSwitchTable':fnABSwitchTable,'fnABSwitchEntry':fnABSwitchEntry,_M:fnABSwitchIndex,'fnOpticalReceiverABSwitchState':fnOpticalReceiverABSwitchState,'fnOpticalReceiverABSwitchControl':fnOpticalReceiverABSwitchControl,'fnLinePowerVoltage1':fnLinePowerVoltage1,'fnLinePowerVoltage2':fnLinePowerVoltage2,'fnLinePowerCurrent':fnLinePowerCurrent,'fnNumberDCPowerSupply':fnNumberDCPowerSupply,'fnDCPowerSupplyMode':fnDCPowerSupplyMode,'fnDCPowerTable':fnDCPowerTable,'fnDCPowerEntry':fnDCPowerEntry,_N:fnDCPowerIndex,'fnDCPowerVoltage':fnDCPowerVoltage,'fnDCPowerCurrent':fnDCPowerCurrent,'fnDCPowerName':fnDCPowerName,'fnReturnRFPower':fnReturnRFPower})