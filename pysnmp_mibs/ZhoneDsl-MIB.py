_O='zhoneDslPerfDataEntry'
_N='zhoneHdsl2StatusEntry'
_M='zhoneDslAlarmProfileName'
_L='not-accessible'
_K='zhoneHdsl2ConfigProfileName'
_J='read-write'
_I='ifIndex'
_H='IF-MIB'
_G='OctetString'
_F='ZhoneDsl-MIB'
_E='seconds'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','VariablePointer')
zhoneDsl,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneDsl','zhoneModules')
ZhoneAdminString,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString','ZhoneRowStatus')
zhoneDsl_MIB=ModuleIdentity((1,3,6,1,4,1,5504,6,3))
if mibBuilder.loadTexts:zhoneDsl_MIB.setRevisions(('2000-04-26 17:53',))
_ZhoneDslLineTable_Object=MibTable
zhoneDslLineTable=_ZhoneDslLineTable_Object((1,3,6,1,4,1,5504,5,4,1))
if mibBuilder.loadTexts:zhoneDslLineTable.setStatus(_A)
_ZhoneDslLineEntry_Object=MibTableRow
zhoneDslLineEntry=_ZhoneDslLineEntry_Object((1,3,6,1,4,1,5504,5,4,1,1))
zhoneDslLineEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zhoneDslLineEntry.setStatus(_A)
class _ZhoneDslLineType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,96)));namedValues=NamedValues(*(('hdsl',1),('hdsl2',2),('shdsl',3),('sdsl',96)))
_ZhoneDslLineType_Type.__name__=_C
_ZhoneDslLineType_Object=MibTableColumn
zhoneDslLineType=_ZhoneDslLineType_Object((1,3,6,1,4,1,5504,5,4,1,1,1),_ZhoneDslLineType_Type())
zhoneDslLineType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDslLineType.setStatus(_A)
class _ZhoneDslLineCapabilities_Type(Bits):namedValues=NamedValues(*(('hdsl',1),('hdsl2',2),('shdsl',4),('sdsl',8)))
_ZhoneDslLineCapabilities_Type.__name__='Bits'
_ZhoneDslLineCapabilities_Object=MibTableColumn
zhoneDslLineCapabilities=_ZhoneDslLineCapabilities_Object((1,3,6,1,4,1,5504,5,4,1,1,2),_ZhoneDslLineCapabilities_Type())
zhoneDslLineCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslLineCapabilities.setStatus(_A)
class _ZhoneDslLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('down',1),('downloading',2),('activated',3),('training',4),('up',5)))
_ZhoneDslLineStatus_Type.__name__=_C
_ZhoneDslLineStatus_Object=MibTableColumn
zhoneDslLineStatus=_ZhoneDslLineStatus_Object((1,3,6,1,4,1,5504,5,4,1,1,3),_ZhoneDslLineStatus_Type())
zhoneDslLineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslLineStatus.setStatus(_A)
_ZhoneDslUpLineRate_Type=Gauge32
_ZhoneDslUpLineRate_Object=MibTableColumn
zhoneDslUpLineRate=_ZhoneDslUpLineRate_Object((1,3,6,1,4,1,5504,5,4,1,1,4),_ZhoneDslUpLineRate_Type())
zhoneDslUpLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslUpLineRate.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslUpLineRate.setUnits('bps')
_ZhoneDslDownLineRate_Type=Gauge32
_ZhoneDslDownLineRate_Object=MibTableColumn
zhoneDslDownLineRate=_ZhoneDslDownLineRate_Object((1,3,6,1,4,1,5504,5,4,1,1,5),_ZhoneDslDownLineRate_Type())
zhoneDslDownLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslDownLineRate.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslDownLineRate.setUnits('bps')
_ZhoneDslLineConfigProfile_Type=ZhoneAdminString
_ZhoneDslLineConfigProfile_Object=MibTableColumn
zhoneDslLineConfigProfile=_ZhoneDslLineConfigProfile_Object((1,3,6,1,4,1,5504,5,4,1,1,6),_ZhoneDslLineConfigProfile_Type())
zhoneDslLineConfigProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDslLineConfigProfile.setStatus(_A)
_ZhoneDslLineAlarmProfile_Type=ZhoneAdminString
_ZhoneDslLineAlarmProfile_Object=MibTableColumn
zhoneDslLineAlarmProfile=_ZhoneDslLineAlarmProfile_Object((1,3,6,1,4,1,5504,5,4,1,1,7),_ZhoneDslLineAlarmProfile_Type())
zhoneDslLineAlarmProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDslLineAlarmProfile.setStatus(_A)
_ZhoneDslLineRowStatus_Type=ZhoneRowStatus
_ZhoneDslLineRowStatus_Object=MibTableColumn
zhoneDslLineRowStatus=_ZhoneDslLineRowStatus_Object((1,3,6,1,4,1,5504,5,4,1,1,8),_ZhoneDslLineRowStatus_Type())
zhoneDslLineRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zhoneDslLineRowStatus.setStatus(_A)
_ZhoneHdsl2ConfigProfileTable_Object=MibTable
zhoneHdsl2ConfigProfileTable=_ZhoneHdsl2ConfigProfileTable_Object((1,3,6,1,4,1,5504,5,4,3))
if mibBuilder.loadTexts:zhoneHdsl2ConfigProfileTable.setStatus(_A)
_ZhoneHdsl2ConfigProfileEntry_Object=MibTableRow
zhoneHdsl2ConfigProfileEntry=_ZhoneHdsl2ConfigProfileEntry_Object((1,3,6,1,4,1,5504,5,4,3,1))
zhoneHdsl2ConfigProfileEntry.setIndexNames((1,_F,_K))
if mibBuilder.loadTexts:zhoneHdsl2ConfigProfileEntry.setStatus(_A)
_ZhoneHdsl2ConfigProfileName_Type=ZhoneAdminString
_ZhoneHdsl2ConfigProfileName_Object=MibTableColumn
zhoneHdsl2ConfigProfileName=_ZhoneHdsl2ConfigProfileName_Object((1,3,6,1,4,1,5504,5,4,3,1,1),_ZhoneHdsl2ConfigProfileName_Type())
zhoneHdsl2ConfigProfileName.setMaxAccess(_L)
if mibBuilder.loadTexts:zhoneHdsl2ConfigProfileName.setStatus(_A)
class _ZhoneHdsl2ConfigUnitMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('co',1),('cpe',2)))
_ZhoneHdsl2ConfigUnitMode_Type.__name__=_C
_ZhoneHdsl2ConfigUnitMode_Object=MibTableColumn
zhoneHdsl2ConfigUnitMode=_ZhoneHdsl2ConfigUnitMode_Object((1,3,6,1,4,1,5504,5,4,3,1,2),_ZhoneHdsl2ConfigUnitMode_Type())
zhoneHdsl2ConfigUnitMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneHdsl2ConfigUnitMode.setStatus(_A)
class _ZhoneHdsl2ConfigTransmitPowerbackoffMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('backoff-disable',1),('backoff-enable',2),('no-change-backoff',3)))
_ZhoneHdsl2ConfigTransmitPowerbackoffMode_Type.__name__=_C
_ZhoneHdsl2ConfigTransmitPowerbackoffMode_Object=MibTableColumn
zhoneHdsl2ConfigTransmitPowerbackoffMode=_ZhoneHdsl2ConfigTransmitPowerbackoffMode_Object((1,3,6,1,4,1,5504,5,4,3,1,3),_ZhoneHdsl2ConfigTransmitPowerbackoffMode_Type())
zhoneHdsl2ConfigTransmitPowerbackoffMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneHdsl2ConfigTransmitPowerbackoffMode.setStatus(_A)
class _ZhoneHdsl2ConfigDecoderCoeffA_Type(Integer32):defaultValue=970752
_ZhoneHdsl2ConfigDecoderCoeffA_Type.__name__=_C
_ZhoneHdsl2ConfigDecoderCoeffA_Object=MibTableColumn
zhoneHdsl2ConfigDecoderCoeffA=_ZhoneHdsl2ConfigDecoderCoeffA_Object((1,3,6,1,4,1,5504,5,4,3,1,4),_ZhoneHdsl2ConfigDecoderCoeffA_Type())
zhoneHdsl2ConfigDecoderCoeffA.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneHdsl2ConfigDecoderCoeffA.setStatus(_A)
class _ZhoneHdsl2ConfigDecoderCoeffB_Type(Integer32):defaultValue=970752
_ZhoneHdsl2ConfigDecoderCoeffB_Type.__name__=_C
_ZhoneHdsl2ConfigDecoderCoeffB_Object=MibTableColumn
zhoneHdsl2ConfigDecoderCoeffB=_ZhoneHdsl2ConfigDecoderCoeffB_Object((1,3,6,1,4,1,5504,5,4,3,1,5),_ZhoneHdsl2ConfigDecoderCoeffB_Type())
zhoneHdsl2ConfigDecoderCoeffB.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneHdsl2ConfigDecoderCoeffB.setStatus(_A)
class _ZhoneHdsl2ConfigFrameSyncWord_Type(Integer32):defaultValue=45
_ZhoneHdsl2ConfigFrameSyncWord_Type.__name__=_C
_ZhoneHdsl2ConfigFrameSyncWord_Object=MibTableColumn
zhoneHdsl2ConfigFrameSyncWord=_ZhoneHdsl2ConfigFrameSyncWord_Object((1,3,6,1,4,1,5504,5,4,3,1,6),_ZhoneHdsl2ConfigFrameSyncWord_Type())
zhoneHdsl2ConfigFrameSyncWord.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneHdsl2ConfigFrameSyncWord.setStatus(_A)
class _ZhoneHdsl2ConfigStuffBits_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZhoneHdsl2ConfigStuffBits_Type.__name__=_C
_ZhoneHdsl2ConfigStuffBits_Object=MibTableColumn
zhoneHdsl2ConfigStuffBits=_ZhoneHdsl2ConfigStuffBits_Object((1,3,6,1,4,1,5504,5,4,3,1,7),_ZhoneHdsl2ConfigStuffBits_Type())
zhoneHdsl2ConfigStuffBits.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneHdsl2ConfigStuffBits.setStatus(_A)
_ZhoneHdsl2ConfigRowStatus_Type=ZhoneRowStatus
_ZhoneHdsl2ConfigRowStatus_Object=MibTableColumn
zhoneHdsl2ConfigRowStatus=_ZhoneHdsl2ConfigRowStatus_Object((1,3,6,1,4,1,5504,5,4,3,1,8),_ZhoneHdsl2ConfigRowStatus_Type())
zhoneHdsl2ConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneHdsl2ConfigRowStatus.setStatus(_A)
_ZhoneHdsl2StatusTable_Object=MibTable
zhoneHdsl2StatusTable=_ZhoneHdsl2StatusTable_Object((1,3,6,1,4,1,5504,5,4,4))
if mibBuilder.loadTexts:zhoneHdsl2StatusTable.setStatus(_A)
_ZhoneHdsl2StatusEntry_Object=MibTableRow
zhoneHdsl2StatusEntry=_ZhoneHdsl2StatusEntry_Object((1,3,6,1,4,1,5504,5,4,4,1))
if mibBuilder.loadTexts:zhoneHdsl2StatusEntry.setStatus(_A)
class _ZhoneHdsl2DriftAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('rx-clk-alarm',1),('tx-clk-alarm',2),('tx-rx-clk-alarm',3),('no-drift-alarm',4),('not-applicable',5)))
_ZhoneHdsl2DriftAlarm_Type.__name__=_C
_ZhoneHdsl2DriftAlarm_Object=MibTableColumn
zhoneHdsl2DriftAlarm=_ZhoneHdsl2DriftAlarm_Object((1,3,6,1,4,1,5504,5,4,4,1,1),_ZhoneHdsl2DriftAlarm_Type())
zhoneHdsl2DriftAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2DriftAlarm.setStatus(_A)
class _ZhoneHdsl2FramerIBStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_ZhoneHdsl2FramerIBStatus_Type.__name__=_G
_ZhoneHdsl2FramerIBStatus_Object=MibTableColumn
zhoneHdsl2FramerIBStatus=_ZhoneHdsl2FramerIBStatus_Object((1,3,6,1,4,1,5504,5,4,4,1,2),_ZhoneHdsl2FramerIBStatus_Type())
zhoneHdsl2FramerIBStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2FramerIBStatus.setStatus(_A)
_ZhoneHdsl2LocalPSDMaskStatus_Type=Integer32
_ZhoneHdsl2LocalPSDMaskStatus_Object=MibTableColumn
zhoneHdsl2LocalPSDMaskStatus=_ZhoneHdsl2LocalPSDMaskStatus_Object((1,3,6,1,4,1,5504,5,4,4,1,3),_ZhoneHdsl2LocalPSDMaskStatus_Type())
zhoneHdsl2LocalPSDMaskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2LocalPSDMaskStatus.setStatus(_A)
_ZhoneHdsl2LoopAttenuation_Type=Integer32
_ZhoneHdsl2LoopAttenuation_Object=MibTableColumn
zhoneHdsl2LoopAttenuation=_ZhoneHdsl2LoopAttenuation_Object((1,3,6,1,4,1,5504,5,4,4,1,4),_ZhoneHdsl2LoopAttenuation_Type())
zhoneHdsl2LoopAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2LoopAttenuation.setStatus(_A)
if mibBuilder.loadTexts:zhoneHdsl2LoopAttenuation.setUnits('tenth DB')
class _ZhoneHdsl2LossWordStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no-lossw-defect',1),('lossw-defect',2)))
_ZhoneHdsl2LossWordStatus_Type.__name__=_C
_ZhoneHdsl2LossWordStatus_Object=MibTableColumn
zhoneHdsl2LossWordStatus=_ZhoneHdsl2LossWordStatus_Object((1,3,6,1,4,1,5504,5,4,4,1,5),_ZhoneHdsl2LossWordStatus_Type())
zhoneHdsl2LossWordStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2LossWordStatus.setStatus(_A)
_ZhoneHdsl2RmtPSDMaskStatus_Type=Integer32
_ZhoneHdsl2RmtPSDMaskStatus_Object=MibTableColumn
zhoneHdsl2RmtPSDMaskStatus=_ZhoneHdsl2RmtPSDMaskStatus_Object((1,3,6,1,4,1,5504,5,4,4,1,6),_ZhoneHdsl2RmtPSDMaskStatus_Type())
zhoneHdsl2RmtPSDMaskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2RmtPSDMaskStatus.setStatus(_A)
_ZhoneHdsl2RmtCountryCode_Type=Integer32
_ZhoneHdsl2RmtCountryCode_Object=MibTableColumn
zhoneHdsl2RmtCountryCode=_ZhoneHdsl2RmtCountryCode_Object((1,3,6,1,4,1,5504,5,4,4,1,7),_ZhoneHdsl2RmtCountryCode_Type())
zhoneHdsl2RmtCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2RmtCountryCode.setStatus(_A)
_ZhoneHdsl2RmtVersion_Type=Integer32
_ZhoneHdsl2RmtVersion_Object=MibTableColumn
zhoneHdsl2RmtVersion=_ZhoneHdsl2RmtVersion_Object((1,3,6,1,4,1,5504,5,4,4,1,8),_ZhoneHdsl2RmtVersion_Type())
zhoneHdsl2RmtVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2RmtVersion.setStatus(_A)
_ZhoneHdsl2RmtProviderCode_Type=Integer32
_ZhoneHdsl2RmtProviderCode_Object=MibTableColumn
zhoneHdsl2RmtProviderCode=_ZhoneHdsl2RmtProviderCode_Object((1,3,6,1,4,1,5504,5,4,4,1,9),_ZhoneHdsl2RmtProviderCode_Type())
zhoneHdsl2RmtProviderCode.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2RmtProviderCode.setStatus(_A)
class _ZhoneHdsl2RmtVendorData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZhoneHdsl2RmtVendorData_Type.__name__=_G
_ZhoneHdsl2RmtVendorData_Object=MibTableColumn
zhoneHdsl2RmtVendorData=_ZhoneHdsl2RmtVendorData_Object((1,3,6,1,4,1,5504,5,4,4,1,10),_ZhoneHdsl2RmtVendorData_Type())
zhoneHdsl2RmtVendorData.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2RmtVendorData.setStatus(_A)
_ZhoneHdsl2RmtTxEncoderA_Type=Integer32
_ZhoneHdsl2RmtTxEncoderA_Object=MibTableColumn
zhoneHdsl2RmtTxEncoderA=_ZhoneHdsl2RmtTxEncoderA_Object((1,3,6,1,4,1,5504,5,4,4,1,11),_ZhoneHdsl2RmtTxEncoderA_Type())
zhoneHdsl2RmtTxEncoderA.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2RmtTxEncoderA.setStatus(_A)
_ZhoneHdsl2RmtTxEncoderB_Type=Integer32
_ZhoneHdsl2RmtTxEncoderB_Object=MibTableColumn
zhoneHdsl2RmtTxEncoderB=_ZhoneHdsl2RmtTxEncoderB_Object((1,3,6,1,4,1,5504,5,4,4,1,12),_ZhoneHdsl2RmtTxEncoderB_Type())
zhoneHdsl2RmtTxEncoderB.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2RmtTxEncoderB.setStatus(_A)
class _ZhoneHdsl2TipRingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('reverse',2)))
_ZhoneHdsl2TipRingStatus_Type.__name__=_C
_ZhoneHdsl2TipRingStatus_Object=MibTableColumn
zhoneHdsl2TipRingStatus=_ZhoneHdsl2TipRingStatus_Object((1,3,6,1,4,1,5504,5,4,4,1,13),_ZhoneHdsl2TipRingStatus_Type())
zhoneHdsl2TipRingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2TipRingStatus.setStatus(_A)
_ZhoneHdsl2FrameSyncWord_Type=Integer32
_ZhoneHdsl2FrameSyncWord_Object=MibTableColumn
zhoneHdsl2FrameSyncWord=_ZhoneHdsl2FrameSyncWord_Object((1,3,6,1,4,1,5504,5,4,4,1,14),_ZhoneHdsl2FrameSyncWord_Type())
zhoneHdsl2FrameSyncWord.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2FrameSyncWord.setStatus(_A)
_ZhoneHdsl2StuffBits_Type=Integer32
_ZhoneHdsl2StuffBits_Object=MibTableColumn
zhoneHdsl2StuffBits=_ZhoneHdsl2StuffBits_Object((1,3,6,1,4,1,5504,5,4,4,1,15),_ZhoneHdsl2StuffBits_Type())
zhoneHdsl2StuffBits.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneHdsl2StuffBits.setStatus(_A)
_ZhoneDslPerfDataTable_Object=MibTable
zhoneDslPerfDataTable=_ZhoneDslPerfDataTable_Object((1,3,6,1,4,1,5504,5,4,5))
if mibBuilder.loadTexts:zhoneDslPerfDataTable.setStatus(_A)
_ZhoneDslPerfDataEntry_Object=MibTableRow
zhoneDslPerfDataEntry=_ZhoneDslPerfDataEntry_Object((1,3,6,1,4,1,5504,5,4,5,1))
if mibBuilder.loadTexts:zhoneDslPerfDataEntry.setStatus(_A)
_ZhoneDslPerfLofs_Type=Counter32
_ZhoneDslPerfLofs_Object=MibTableColumn
zhoneDslPerfLofs=_ZhoneDslPerfLofs_Object((1,3,6,1,4,1,5504,5,4,5,1,1),_ZhoneDslPerfLofs_Type())
zhoneDslPerfLofs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfLofs.setStatus(_A)
_ZhoneDslPerfLoss_Type=Counter32
_ZhoneDslPerfLoss_Object=MibTableColumn
zhoneDslPerfLoss=_ZhoneDslPerfLoss_Object((1,3,6,1,4,1,5504,5,4,5,1,2),_ZhoneDslPerfLoss_Type())
zhoneDslPerfLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfLoss.setStatus(_A)
_ZhoneDslPerfLols_Type=Counter32
_ZhoneDslPerfLols_Object=MibTableColumn
zhoneDslPerfLols=_ZhoneDslPerfLols_Object((1,3,6,1,4,1,5504,5,4,5,1,3),_ZhoneDslPerfLols_Type())
zhoneDslPerfLols.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfLols.setStatus(_A)
_ZhoneDslPerfInits_Type=Counter32
_ZhoneDslPerfInits_Object=MibTableColumn
zhoneDslPerfInits=_ZhoneDslPerfInits_Object((1,3,6,1,4,1,5504,5,4,5,1,4),_ZhoneDslPerfInits_Type())
zhoneDslPerfInits.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfInits.setStatus(_A)
_ZhoneDslPerfCur15MinTimeElapsed_Type=Gauge32
_ZhoneDslPerfCur15MinTimeElapsed_Object=MibTableColumn
zhoneDslPerfCur15MinTimeElapsed=_ZhoneDslPerfCur15MinTimeElapsed_Object((1,3,6,1,4,1,5504,5,4,5,1,5),_ZhoneDslPerfCur15MinTimeElapsed_Type())
zhoneDslPerfCur15MinTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinTimeElapsed.setUnits(_E)
_ZhoneDslPerfCur15MinLofs_Type=Gauge32
_ZhoneDslPerfCur15MinLofs_Object=MibTableColumn
zhoneDslPerfCur15MinLofs=_ZhoneDslPerfCur15MinLofs_Object((1,3,6,1,4,1,5504,5,4,5,1,6),_ZhoneDslPerfCur15MinLofs_Type())
zhoneDslPerfCur15MinLofs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinLofs.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinLofs.setUnits(_E)
_ZhoneDslPerfCur15MinLoss_Type=Gauge32
_ZhoneDslPerfCur15MinLoss_Object=MibTableColumn
zhoneDslPerfCur15MinLoss=_ZhoneDslPerfCur15MinLoss_Object((1,3,6,1,4,1,5504,5,4,5,1,7),_ZhoneDslPerfCur15MinLoss_Type())
zhoneDslPerfCur15MinLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinLoss.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinLoss.setUnits(_E)
_ZhoneDslPerfCur15MinLols_Type=Gauge32
_ZhoneDslPerfCur15MinLols_Object=MibTableColumn
zhoneDslPerfCur15MinLols=_ZhoneDslPerfCur15MinLols_Object((1,3,6,1,4,1,5504,5,4,5,1,8),_ZhoneDslPerfCur15MinLols_Type())
zhoneDslPerfCur15MinLols.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinLols.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinLols.setUnits(_E)
_ZhoneDslPerfCur15MinInits_Type=Counter32
_ZhoneDslPerfCur15MinInits_Object=MibTableColumn
zhoneDslPerfCur15MinInits=_ZhoneDslPerfCur15MinInits_Object((1,3,6,1,4,1,5504,5,4,5,1,9),_ZhoneDslPerfCur15MinInits_Type())
zhoneDslPerfCur15MinInits.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDslPerfCur15MinInits.setStatus(_A)
_ZhoneDslAlarmProfileTable_Object=MibTable
zhoneDslAlarmProfileTable=_ZhoneDslAlarmProfileTable_Object((1,3,6,1,4,1,5504,5,4,6))
if mibBuilder.loadTexts:zhoneDslAlarmProfileTable.setStatus(_A)
_ZhoneDslAlarmProfileEntry_Object=MibTableRow
zhoneDslAlarmProfileEntry=_ZhoneDslAlarmProfileEntry_Object((1,3,6,1,4,1,5504,5,4,6,1))
zhoneDslAlarmProfileEntry.setIndexNames((1,_F,_M))
if mibBuilder.loadTexts:zhoneDslAlarmProfileEntry.setStatus(_A)
_ZhoneDslAlarmProfileName_Type=ZhoneAdminString
_ZhoneDslAlarmProfileName_Object=MibTableColumn
zhoneDslAlarmProfileName=_ZhoneDslAlarmProfileName_Object((1,3,6,1,4,1,5504,5,4,6,1,1),_ZhoneDslAlarmProfileName_Type())
zhoneDslAlarmProfileName.setMaxAccess(_L)
if mibBuilder.loadTexts:zhoneDslAlarmProfileName.setStatus(_A)
class _ZhoneDslThreshold15MinLoss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_ZhoneDslThreshold15MinLoss_Type.__name__=_C
_ZhoneDslThreshold15MinLoss_Object=MibTableColumn
zhoneDslThreshold15MinLoss=_ZhoneDslThreshold15MinLoss_Object((1,3,6,1,4,1,5504,5,4,6,1,2),_ZhoneDslThreshold15MinLoss_Type())
zhoneDslThreshold15MinLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDslThreshold15MinLoss.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslThreshold15MinLoss.setUnits(_E)
class _ZhoneDslThreshold15MinLols_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_ZhoneDslThreshold15MinLols_Type.__name__=_C
_ZhoneDslThreshold15MinLols_Object=MibTableColumn
zhoneDslThreshold15MinLols=_ZhoneDslThreshold15MinLols_Object((1,3,6,1,4,1,5504,5,4,6,1,3),_ZhoneDslThreshold15MinLols_Type())
zhoneDslThreshold15MinLols.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDslThreshold15MinLols.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslThreshold15MinLols.setUnits(_E)
class _ZhoneDslThreshold15MinLofs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_ZhoneDslThreshold15MinLofs_Type.__name__=_C
_ZhoneDslThreshold15MinLofs_Object=MibTableColumn
zhoneDslThreshold15MinLofs=_ZhoneDslThreshold15MinLofs_Object((1,3,6,1,4,1,5504,5,4,6,1,4),_ZhoneDslThreshold15MinLofs_Type())
zhoneDslThreshold15MinLofs.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDslThreshold15MinLofs.setStatus(_A)
if mibBuilder.loadTexts:zhoneDslThreshold15MinLofs.setUnits(_E)
_ZhoneDslAlarmProfileRowStatus_Type=ZhoneAdminString
_ZhoneDslAlarmProfileRowStatus_Object=MibTableColumn
zhoneDslAlarmProfileRowStatus=_ZhoneDslAlarmProfileRowStatus_Object((1,3,6,1,4,1,5504,5,4,6,1,5),_ZhoneDslAlarmProfileRowStatus_Type())
zhoneDslAlarmProfileRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zhoneDslAlarmProfileRowStatus.setStatus(_A)
ifIndex.registerAugmentions((_F,_N))
zhoneHdsl2StatusEntry.setIndexNames(*ifIndex.getIndexNames())
zhoneDslLineEntry.registerAugmentions((_F,_O))
zhoneDslPerfDataEntry.setIndexNames(*zhoneDslLineEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'zhoneDslLineTable':zhoneDslLineTable,'zhoneDslLineEntry':zhoneDslLineEntry,'zhoneDslLineType':zhoneDslLineType,'zhoneDslLineCapabilities':zhoneDslLineCapabilities,'zhoneDslLineStatus':zhoneDslLineStatus,'zhoneDslUpLineRate':zhoneDslUpLineRate,'zhoneDslDownLineRate':zhoneDslDownLineRate,'zhoneDslLineConfigProfile':zhoneDslLineConfigProfile,'zhoneDslLineAlarmProfile':zhoneDslLineAlarmProfile,'zhoneDslLineRowStatus':zhoneDslLineRowStatus,'zhoneHdsl2ConfigProfileTable':zhoneHdsl2ConfigProfileTable,'zhoneHdsl2ConfigProfileEntry':zhoneHdsl2ConfigProfileEntry,_K:zhoneHdsl2ConfigProfileName,'zhoneHdsl2ConfigUnitMode':zhoneHdsl2ConfigUnitMode,'zhoneHdsl2ConfigTransmitPowerbackoffMode':zhoneHdsl2ConfigTransmitPowerbackoffMode,'zhoneHdsl2ConfigDecoderCoeffA':zhoneHdsl2ConfigDecoderCoeffA,'zhoneHdsl2ConfigDecoderCoeffB':zhoneHdsl2ConfigDecoderCoeffB,'zhoneHdsl2ConfigFrameSyncWord':zhoneHdsl2ConfigFrameSyncWord,'zhoneHdsl2ConfigStuffBits':zhoneHdsl2ConfigStuffBits,'zhoneHdsl2ConfigRowStatus':zhoneHdsl2ConfigRowStatus,'zhoneHdsl2StatusTable':zhoneHdsl2StatusTable,_N:zhoneHdsl2StatusEntry,'zhoneHdsl2DriftAlarm':zhoneHdsl2DriftAlarm,'zhoneHdsl2FramerIBStatus':zhoneHdsl2FramerIBStatus,'zhoneHdsl2LocalPSDMaskStatus':zhoneHdsl2LocalPSDMaskStatus,'zhoneHdsl2LoopAttenuation':zhoneHdsl2LoopAttenuation,'zhoneHdsl2LossWordStatus':zhoneHdsl2LossWordStatus,'zhoneHdsl2RmtPSDMaskStatus':zhoneHdsl2RmtPSDMaskStatus,'zhoneHdsl2RmtCountryCode':zhoneHdsl2RmtCountryCode,'zhoneHdsl2RmtVersion':zhoneHdsl2RmtVersion,'zhoneHdsl2RmtProviderCode':zhoneHdsl2RmtProviderCode,'zhoneHdsl2RmtVendorData':zhoneHdsl2RmtVendorData,'zhoneHdsl2RmtTxEncoderA':zhoneHdsl2RmtTxEncoderA,'zhoneHdsl2RmtTxEncoderB':zhoneHdsl2RmtTxEncoderB,'zhoneHdsl2TipRingStatus':zhoneHdsl2TipRingStatus,'zhoneHdsl2FrameSyncWord':zhoneHdsl2FrameSyncWord,'zhoneHdsl2StuffBits':zhoneHdsl2StuffBits,'zhoneDslPerfDataTable':zhoneDslPerfDataTable,_O:zhoneDslPerfDataEntry,'zhoneDslPerfLofs':zhoneDslPerfLofs,'zhoneDslPerfLoss':zhoneDslPerfLoss,'zhoneDslPerfLols':zhoneDslPerfLols,'zhoneDslPerfInits':zhoneDslPerfInits,'zhoneDslPerfCur15MinTimeElapsed':zhoneDslPerfCur15MinTimeElapsed,'zhoneDslPerfCur15MinLofs':zhoneDslPerfCur15MinLofs,'zhoneDslPerfCur15MinLoss':zhoneDslPerfCur15MinLoss,'zhoneDslPerfCur15MinLols':zhoneDslPerfCur15MinLols,'zhoneDslPerfCur15MinInits':zhoneDslPerfCur15MinInits,'zhoneDslAlarmProfileTable':zhoneDslAlarmProfileTable,'zhoneDslAlarmProfileEntry':zhoneDslAlarmProfileEntry,_M:zhoneDslAlarmProfileName,'zhoneDslThreshold15MinLoss':zhoneDslThreshold15MinLoss,'zhoneDslThreshold15MinLols':zhoneDslThreshold15MinLols,'zhoneDslThreshold15MinLofs':zhoneDslThreshold15MinLofs,'zhoneDslAlarmProfileRowStatus':zhoneDslAlarmProfileRowStatus,'zhoneDsl-MIB':zhoneDsl_MIB})