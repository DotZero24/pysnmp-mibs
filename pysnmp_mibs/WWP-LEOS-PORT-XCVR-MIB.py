_d='wwpLeosPortXcvrErrorType'
_c='wwpLeosPortXcvrEventType'
_b='voltageNeg5p2VCurrent'
_a='voltage1p8VCurrent'
_Z='voltage3p3VCurrent'
_Y='voltage5VCurrent'
_X='voltageNeg5p2V'
_W='voltage1p8V'
_V='voltage3p3V'
_U='voltage5V'
_T='laserWavelength'
_S='laserTemp'
_R='tECCurrentMa'
_Q='aPDBiasVoltage'
_P='loopback'
_O='OctetString'
_N='none'
_M='read-write'
_L='reserved'
_K='unknown'
_J='Unsigned32'
_I='enabled'
_H='disabled'
_G='dBm'
_F='uW'
_E='wwpLeosPortXcvrId'
_D='WWP-LEOS-PORT-XCVR-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosPortXcvrMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,4))
if mibBuilder.loadTexts:wwpLeosPortXcvrMIB.setRevisions(('2011-07-06 00:00','2011-05-24 00:00','2011-03-08 00:00','2010-02-01 00:00','2006-03-15 00:00','2001-04-03 17:00'))
_WwpLeosPortXcvrMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvrMIBObjects=_WwpLeosPortXcvrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,1))
_WwpLeosPortXcvr_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvr=_WwpLeosPortXcvr_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,1,1))
_WwpLeosPortXcvrTable_Object=MibTable
wwpLeosPortXcvrTable=_WwpLeosPortXcvrTable_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1))
if mibBuilder.loadTexts:wwpLeosPortXcvrTable.setStatus(_A)
_WwpLeosPortXcvrEntry_Object=MibTableRow
wwpLeosPortXcvrEntry=_WwpLeosPortXcvrEntry_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1))
wwpLeosPortXcvrEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrEntry.setStatus(_A)
class _WwpLeosPortXcvrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrId_Type.__name__=_C
_WwpLeosPortXcvrId_Object=MibTableColumn
wwpLeosPortXcvrId=_WwpLeosPortXcvrId_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,1),_WwpLeosPortXcvrId_Type())
wwpLeosPortXcvrId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrId.setStatus(_A)
class _WwpLeosPortXcvrOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),(_P,3),('notPresent',4),('faulted',5)))
_WwpLeosPortXcvrOperState_Type.__name__=_C
_WwpLeosPortXcvrOperState_Object=MibTableColumn
wwpLeosPortXcvrOperState=_WwpLeosPortXcvrOperState_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,2),_WwpLeosPortXcvrOperState_Type())
wwpLeosPortXcvrOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrOperState.setStatus(_A)
class _WwpLeosPortXcvrIdentiferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_K,1),('gbic',2),('solderedType',3),('sfp',4),(_L,5),('vendorSpecific',6),('xbi',7),('xenpak',8),('xfp',9),('xff',10),('xfpe',11),('xpak',12),('x2',13)))
_WwpLeosPortXcvrIdentiferType_Type.__name__=_C
_WwpLeosPortXcvrIdentiferType_Object=MibTableColumn
wwpLeosPortXcvrIdentiferType=_WwpLeosPortXcvrIdentiferType_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,3),_WwpLeosPortXcvrIdentiferType_Type())
wwpLeosPortXcvrIdentiferType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrIdentiferType.setStatus(_A)
class _WwpLeosPortXcvrExtIdentiferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('sfp-gbic',2)))
_WwpLeosPortXcvrExtIdentiferType_Type.__name__=_C
_WwpLeosPortXcvrExtIdentiferType_Object=MibTableColumn
wwpLeosPortXcvrExtIdentiferType=_WwpLeosPortXcvrExtIdentiferType_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,4),_WwpLeosPortXcvrExtIdentiferType_Type())
wwpLeosPortXcvrExtIdentiferType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrExtIdentiferType.setStatus(_A)
class _WwpLeosPortXcvrConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrConnectorType_Type.__name__=_C
_WwpLeosPortXcvrConnectorType_Object=MibTableColumn
wwpLeosPortXcvrConnectorType=_WwpLeosPortXcvrConnectorType_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,5),_WwpLeosPortXcvrConnectorType_Type())
wwpLeosPortXcvrConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrConnectorType.setStatus(_A)
class _WwpLeosPortXcvrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrType_Type.__name__=_C
_WwpLeosPortXcvrType_Object=MibTableColumn
wwpLeosPortXcvrType=_WwpLeosPortXcvrType_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,6),_WwpLeosPortXcvrType_Type())
wwpLeosPortXcvrType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrType.setStatus(_A)
_WwpLeosPortXcvrVendorName_Type=DisplayString
_WwpLeosPortXcvrVendorName_Object=MibTableColumn
wwpLeosPortXcvrVendorName=_WwpLeosPortXcvrVendorName_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,7),_WwpLeosPortXcvrVendorName_Type())
wwpLeosPortXcvrVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrVendorName.setStatus(_A)
class _WwpLeosPortXcvrVendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosPortXcvrVendorOUI_Type.__name__=_O
_WwpLeosPortXcvrVendorOUI_Object=MibTableColumn
wwpLeosPortXcvrVendorOUI=_WwpLeosPortXcvrVendorOUI_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,8),_WwpLeosPortXcvrVendorOUI_Type())
wwpLeosPortXcvrVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrVendorOUI.setStatus(_A)
_WwpLeosPortXcvrVendorPN_Type=DisplayString
_WwpLeosPortXcvrVendorPN_Object=MibTableColumn
wwpLeosPortXcvrVendorPN=_WwpLeosPortXcvrVendorPN_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,9),_WwpLeosPortXcvrVendorPN_Type())
wwpLeosPortXcvrVendorPN.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrVendorPN.setStatus(_A)
_WwpLeosPortXcvrRevNum_Type=DisplayString
_WwpLeosPortXcvrRevNum_Object=MibTableColumn
wwpLeosPortXcvrRevNum=_WwpLeosPortXcvrRevNum_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,10),_WwpLeosPortXcvrRevNum_Type())
wwpLeosPortXcvrRevNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrRevNum.setStatus(_A)
_WwpLeosPortXcvrSerialNum_Type=DisplayString
_WwpLeosPortXcvrSerialNum_Object=MibTableColumn
wwpLeosPortXcvrSerialNum=_WwpLeosPortXcvrSerialNum_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,11),_WwpLeosPortXcvrSerialNum_Type())
wwpLeosPortXcvrSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrSerialNum.setStatus(_A)
class _WwpLeosPortXcvrEncodingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrEncodingType_Type.__name__=_C
_WwpLeosPortXcvrEncodingType_Object=MibTableColumn
wwpLeosPortXcvrEncodingType=_WwpLeosPortXcvrEncodingType_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,12),_WwpLeosPortXcvrEncodingType_Type())
wwpLeosPortXcvrEncodingType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrEncodingType.setStatus(_A)
_WwpLeosPortXcvrMfgDate_Type=DisplayString
_WwpLeosPortXcvrMfgDate_Object=MibTableColumn
wwpLeosPortXcvrMfgDate=_WwpLeosPortXcvrMfgDate_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,13),_WwpLeosPortXcvrMfgDate_Type())
wwpLeosPortXcvrMfgDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrMfgDate.setStatus(_A)
class _WwpLeosPortXcvrComplianceVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WwpLeosPortXcvrComplianceVer_Type.__name__=_C
_WwpLeosPortXcvrComplianceVer_Object=MibTableColumn
wwpLeosPortXcvrComplianceVer=_WwpLeosPortXcvrComplianceVer_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,14),_WwpLeosPortXcvrComplianceVer_Type())
wwpLeosPortXcvrComplianceVer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrComplianceVer.setStatus(_A)
class _WwpLeosPortXcvrWaveLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrWaveLength_Type.__name__=_C
_WwpLeosPortXcvrWaveLength_Object=MibTableColumn
wwpLeosPortXcvrWaveLength=_WwpLeosPortXcvrWaveLength_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,15),_WwpLeosPortXcvrWaveLength_Type())
wwpLeosPortXcvrWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrWaveLength.setStatus(_A)
class _WwpLeosPortXcvrTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrTemperature_Type.__name__=_C
_WwpLeosPortXcvrTemperature_Object=MibTableColumn
wwpLeosPortXcvrTemperature=_WwpLeosPortXcvrTemperature_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,16),_WwpLeosPortXcvrTemperature_Type())
wwpLeosPortXcvrTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrTemperature.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrTemperature.setUnits('centigrade')
class _WwpLeosPortXcvrVcc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrVcc_Type.__name__=_C
_WwpLeosPortXcvrVcc_Object=MibTableColumn
wwpLeosPortXcvrVcc=_WwpLeosPortXcvrVcc_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,17),_WwpLeosPortXcvrVcc_Type())
wwpLeosPortXcvrVcc.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrVcc.setStatus(_A)
class _WwpLeosPortXcvrBias_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrBias_Type.__name__=_C
_WwpLeosPortXcvrBias_Object=MibTableColumn
wwpLeosPortXcvrBias=_WwpLeosPortXcvrBias_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,18),_WwpLeosPortXcvrBias_Type())
wwpLeosPortXcvrBias.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrBias.setStatus(_A)
class _WwpLeosPortXcvrRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrRxPower_Type.__name__=_C
_WwpLeosPortXcvrRxPower_Object=MibTableColumn
wwpLeosPortXcvrRxPower=_WwpLeosPortXcvrRxPower_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,19),_WwpLeosPortXcvrRxPower_Type())
wwpLeosPortXcvrRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrRxPower.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrRxPower.setUnits(_F)
class _WwpLeosPortXcvrTxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_WwpLeosPortXcvrTxState_Type.__name__=_C
_WwpLeosPortXcvrTxState_Object=MibTableColumn
wwpLeosPortXcvrTxState=_WwpLeosPortXcvrTxState_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,20),_WwpLeosPortXcvrTxState_Type())
wwpLeosPortXcvrTxState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrTxState.setStatus(_A)
class _WwpLeosPortXcvrTxFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fault',1),('noFault',2)))
_WwpLeosPortXcvrTxFaultStatus_Type.__name__=_C
_WwpLeosPortXcvrTxFaultStatus_Object=MibTableColumn
wwpLeosPortXcvrTxFaultStatus=_WwpLeosPortXcvrTxFaultStatus_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,21),_WwpLeosPortXcvrTxFaultStatus_Type())
wwpLeosPortXcvrTxFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrTxFaultStatus.setStatus(_A)
class _WwpLeosPortXcvrRxRateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_WwpLeosPortXcvrRxRateStatus_Type.__name__=_C
_WwpLeosPortXcvrRxRateStatus_Object=MibTableColumn
wwpLeosPortXcvrRxRateStatus=_WwpLeosPortXcvrRxRateStatus_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,22),_WwpLeosPortXcvrRxRateStatus_Type())
wwpLeosPortXcvrRxRateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrRxRateStatus.setStatus(_A)
class _WwpLeosPortXcvr9by125um_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvr9by125um_Type.__name__=_C
_WwpLeosPortXcvr9by125um_Object=MibTableColumn
wwpLeosPortXcvr9by125um=_WwpLeosPortXcvr9by125um_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,23),_WwpLeosPortXcvr9by125um_Type())
wwpLeosPortXcvr9by125um.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvr9by125um.setStatus(_A)
class _WwpLeosPortXcvr50by125um_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvr50by125um_Type.__name__=_C
_WwpLeosPortXcvr50by125um_Object=MibTableColumn
wwpLeosPortXcvr50by125um=_WwpLeosPortXcvr50by125um_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,24),_WwpLeosPortXcvr50by125um_Type())
wwpLeosPortXcvr50by125um.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvr50by125um.setStatus(_A)
class _WwpLeosPortXcvr62dot5by125um_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvr62dot5by125um_Type.__name__=_C
_WwpLeosPortXcvr62dot5by125um_Object=MibTableColumn
wwpLeosPortXcvr62dot5by125um=_WwpLeosPortXcvr62dot5by125um_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,25),_WwpLeosPortXcvr62dot5by125um_Type())
wwpLeosPortXcvr62dot5by125um.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvr62dot5by125um.setStatus(_A)
class _WwpLeosPortXcvrCu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrCu_Type.__name__=_C
_WwpLeosPortXcvrCu_Object=MibTableColumn
wwpLeosPortXcvrCu=_WwpLeosPortXcvrCu_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,26),_WwpLeosPortXcvrCu_Type())
wwpLeosPortXcvrCu.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrCu.setStatus(_A)
class _WwpLeosPortXcvrTxOutputPw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrTxOutputPw_Type.__name__=_C
_WwpLeosPortXcvrTxOutputPw_Object=MibTableColumn
wwpLeosPortXcvrTxOutputPw=_WwpLeosPortXcvrTxOutputPw_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,27),_WwpLeosPortXcvrTxOutputPw_Type())
wwpLeosPortXcvrTxOutputPw.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrTxOutputPw.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrTxOutputPw.setUnits(_F)
_WwpLeosPortXcvrLosState_Type=TruthValue
_WwpLeosPortXcvrLosState_Object=MibTableColumn
wwpLeosPortXcvrLosState=_WwpLeosPortXcvrLosState_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,28),_WwpLeosPortXcvrLosState_Type())
wwpLeosPortXcvrLosState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLosState.setStatus(_A)
_WwpLeosPortXcvrDiagSupported_Type=TruthValue
_WwpLeosPortXcvrDiagSupported_Object=MibTableColumn
wwpLeosPortXcvrDiagSupported=_WwpLeosPortXcvrDiagSupported_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,29),_WwpLeosPortXcvrDiagSupported_Type())
wwpLeosPortXcvrDiagSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrDiagSupported.setStatus(_A)
_WwpLeosPortXcvrEnhDiagAlarmSupported_Type=TruthValue
_WwpLeosPortXcvrEnhDiagAlarmSupported_Object=MibTableColumn
wwpLeosPortXcvrEnhDiagAlarmSupported=_WwpLeosPortXcvrEnhDiagAlarmSupported_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,30),_WwpLeosPortXcvrEnhDiagAlarmSupported_Type())
wwpLeosPortXcvrEnhDiagAlarmSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrEnhDiagAlarmSupported.setStatus(_A)
_WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Type=TruthValue
_WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Object=MibTableColumn
wwpLeosPortXcvrEnhDiagSoftTxDisableSupported=_WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,31),_WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Type())
wwpLeosPortXcvrEnhDiagSoftTxDisableSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrEnhDiagSoftTxDisableSupported.setStatus(_A)
_WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Type=TruthValue
_WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Object=MibTableColumn
wwpLeosPortXcvrEnhDiagSoftTxFaultSupported=_WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,32),_WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Type())
wwpLeosPortXcvrEnhDiagSoftTxFaultSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrEnhDiagSoftTxFaultSupported.setStatus(_A)
_WwpLeosPortXcvrEnhDiagRxLosSupported_Type=TruthValue
_WwpLeosPortXcvrEnhDiagRxLosSupported_Object=MibTableColumn
wwpLeosPortXcvrEnhDiagRxLosSupported=_WwpLeosPortXcvrEnhDiagRxLosSupported_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,33),_WwpLeosPortXcvrEnhDiagRxLosSupported_Type())
wwpLeosPortXcvrEnhDiagRxLosSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrEnhDiagRxLosSupported.setStatus(_A)
_WwpLeosPortXcvrHighTempAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrHighTempAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrHighTempAlarmThreshold=_WwpLeosPortXcvrHighTempAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,34),_WwpLeosPortXcvrHighTempAlarmThreshold_Type())
wwpLeosPortXcvrHighTempAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighTempAlarmThreshold.setStatus(_A)
_WwpLeosPortXcvrLowTempAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrLowTempAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrLowTempAlarmThreshold=_WwpLeosPortXcvrLowTempAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,35),_WwpLeosPortXcvrLowTempAlarmThreshold_Type())
wwpLeosPortXcvrLowTempAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowTempAlarmThreshold.setStatus(_A)
_WwpLeosPortXcvrHighVccAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrHighVccAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrHighVccAlarmThreshold=_WwpLeosPortXcvrHighVccAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,36),_WwpLeosPortXcvrHighVccAlarmThreshold_Type())
wwpLeosPortXcvrHighVccAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighVccAlarmThreshold.setStatus(_A)
_WwpLeosPortXcvrLowVccAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrLowVccAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrLowVccAlarmThreshold=_WwpLeosPortXcvrLowVccAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,37),_WwpLeosPortXcvrLowVccAlarmThreshold_Type())
wwpLeosPortXcvrLowVccAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowVccAlarmThreshold.setStatus(_A)
_WwpLeosPortXcvrHighBiasAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrHighBiasAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrHighBiasAlarmThreshold=_WwpLeosPortXcvrHighBiasAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,38),_WwpLeosPortXcvrHighBiasAlarmThreshold_Type())
wwpLeosPortXcvrHighBiasAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighBiasAlarmThreshold.setStatus(_A)
_WwpLeosPortXcvrLowBiasAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrLowBiasAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrLowBiasAlarmThreshold=_WwpLeosPortXcvrLowBiasAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,39),_WwpLeosPortXcvrLowBiasAlarmThreshold_Type())
wwpLeosPortXcvrLowBiasAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowBiasAlarmThreshold.setStatus(_A)
_WwpLeosPortXcvrHighTxPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrHighTxPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrHighTxPwAlarmThreshold=_WwpLeosPortXcvrHighTxPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,40),_WwpLeosPortXcvrHighTxPwAlarmThreshold_Type())
wwpLeosPortXcvrHighTxPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighTxPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighTxPwAlarmThreshold.setUnits(_F)
_WwpLeosPortXcvrLowTxPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrLowTxPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrLowTxPwAlarmThreshold=_WwpLeosPortXcvrLowTxPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,41),_WwpLeosPortXcvrLowTxPwAlarmThreshold_Type())
wwpLeosPortXcvrLowTxPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowTxPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowTxPwAlarmThreshold.setUnits(_F)
_WwpLeosPortXcvrHighRxPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrHighRxPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrHighRxPwAlarmThreshold=_WwpLeosPortXcvrHighRxPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,42),_WwpLeosPortXcvrHighRxPwAlarmThreshold_Type())
wwpLeosPortXcvrHighRxPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighRxPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighRxPwAlarmThreshold.setUnits(_F)
_WwpLeosPortXcvrLowRxPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrLowRxPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrLowRxPwAlarmThreshold=_WwpLeosPortXcvrLowRxPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,43),_WwpLeosPortXcvrLowRxPwAlarmThreshold_Type())
wwpLeosPortXcvrLowRxPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowRxPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowRxPwAlarmThreshold.setUnits(_F)
_WwpLeosPortXcvrEnhDiagRateSelectSupported_Type=TruthValue
_WwpLeosPortXcvrEnhDiagRateSelectSupported_Object=MibTableColumn
wwpLeosPortXcvrEnhDiagRateSelectSupported=_WwpLeosPortXcvrEnhDiagRateSelectSupported_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,44),_WwpLeosPortXcvrEnhDiagRateSelectSupported_Type())
wwpLeosPortXcvrEnhDiagRateSelectSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrEnhDiagRateSelectSupported.setStatus(_A)
class _WwpLeosPortXcvrAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_P,3)))
_WwpLeosPortXcvrAdminState_Type.__name__=_C
_WwpLeosPortXcvrAdminState_Object=MibTableColumn
wwpLeosPortXcvrAdminState=_WwpLeosPortXcvrAdminState_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,45),_WwpLeosPortXcvrAdminState_Type())
wwpLeosPortXcvrAdminState.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosPortXcvrAdminState.setStatus(_A)
class _WwpLeosPortXcvrXfpMinBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMinBitRate_Type.__name__=_C
_WwpLeosPortXcvrXfpMinBitRate_Object=MibTableColumn
wwpLeosPortXcvrXfpMinBitRate=_WwpLeosPortXcvrXfpMinBitRate_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,70),_WwpLeosPortXcvrXfpMinBitRate_Type())
wwpLeosPortXcvrXfpMinBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMinBitRate.setStatus(_A)
class _WwpLeosPortXcvrXfpMaxBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMaxBitRate_Type.__name__=_C
_WwpLeosPortXcvrXfpMaxBitRate_Object=MibTableColumn
wwpLeosPortXcvrXfpMaxBitRate=_WwpLeosPortXcvrXfpMaxBitRate_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,71),_WwpLeosPortXcvrXfpMaxBitRate_Type())
wwpLeosPortXcvrXfpMaxBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMaxBitRate.setStatus(_A)
class _WwpLeosPortXcvrXfpLinkLenSmf1km_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpLinkLenSmf1km_Type.__name__=_C
_WwpLeosPortXcvrXfpLinkLenSmf1km_Object=MibTableColumn
wwpLeosPortXcvrXfpLinkLenSmf1km=_WwpLeosPortXcvrXfpLinkLenSmf1km_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,72),_WwpLeosPortXcvrXfpLinkLenSmf1km_Type())
wwpLeosPortXcvrXfpLinkLenSmf1km.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLinkLenSmf1km.setStatus(_A)
class _WwpLeosPortXcvrXfpLinkLenE50u2m_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpLinkLenE50u2m_Type.__name__=_C
_WwpLeosPortXcvrXfpLinkLenE50u2m_Object=MibTableColumn
wwpLeosPortXcvrXfpLinkLenE50u2m=_WwpLeosPortXcvrXfpLinkLenE50u2m_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,73),_WwpLeosPortXcvrXfpLinkLenE50u2m_Type())
wwpLeosPortXcvrXfpLinkLenE50u2m.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLinkLenE50u2m.setStatus(_A)
class _WwpLeosPortXcvrXfpLinkLen50u1m_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpLinkLen50u1m_Type.__name__=_C
_WwpLeosPortXcvrXfpLinkLen50u1m_Object=MibTableColumn
wwpLeosPortXcvrXfpLinkLen50u1m=_WwpLeosPortXcvrXfpLinkLen50u1m_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,74),_WwpLeosPortXcvrXfpLinkLen50u1m_Type())
wwpLeosPortXcvrXfpLinkLen50u1m.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLinkLen50u1m.setStatus(_A)
class _WwpLeosPortXcvrXfpLinkLen62dot5u1m_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpLinkLen62dot5u1m_Type.__name__=_C
_WwpLeosPortXcvrXfpLinkLen62dot5u1m_Object=MibTableColumn
wwpLeosPortXcvrXfpLinkLen62dot5u1m=_WwpLeosPortXcvrXfpLinkLen62dot5u1m_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,75),_WwpLeosPortXcvrXfpLinkLen62dot5u1m_Type())
wwpLeosPortXcvrXfpLinkLen62dot5u1m.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLinkLen62dot5u1m.setStatus(_A)
class _WwpLeosPortXcvrXfpLinkLenCopper1m_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpLinkLenCopper1m_Type.__name__=_C
_WwpLeosPortXcvrXfpLinkLenCopper1m_Object=MibTableColumn
wwpLeosPortXcvrXfpLinkLenCopper1m=_WwpLeosPortXcvrXfpLinkLenCopper1m_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,76),_WwpLeosPortXcvrXfpLinkLenCopper1m_Type())
wwpLeosPortXcvrXfpLinkLenCopper1m.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLinkLenCopper1m.setStatus(_A)
class _WwpLeosPortXcvrXfpDevTech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('vcsel850nm',1),('vcsel1310nm',2),('vcsel1550nm',3),('fp1310nm',4),('dfb1310nm',5),('dfb1550nm',6),('eml1310nm',7),('eml1550nm',8),('copperOrOther',9),('tunable1550nm',10),(_L,11)))
_WwpLeosPortXcvrXfpDevTech_Type.__name__=_C
_WwpLeosPortXcvrXfpDevTech_Object=MibTableColumn
wwpLeosPortXcvrXfpDevTech=_WwpLeosPortXcvrXfpDevTech_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,77),_WwpLeosPortXcvrXfpDevTech_Type())
wwpLeosPortXcvrXfpDevTech.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpDevTech.setStatus(_A)
class _WwpLeosPortXcvrXfpTransmitterTech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpTransmitterTech_Type.__name__=_C
_WwpLeosPortXcvrXfpTransmitterTech_Object=MibTableColumn
wwpLeosPortXcvrXfpTransmitterTech=_WwpLeosPortXcvrXfpTransmitterTech_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,78),_WwpLeosPortXcvrXfpTransmitterTech_Type())
wwpLeosPortXcvrXfpTransmitterTech.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpTransmitterTech.setStatus(_A)
class _WwpLeosPortXcvrXfpCdrSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpCdrSupport_Type.__name__=_C
_WwpLeosPortXcvrXfpCdrSupport_Object=MibTableColumn
wwpLeosPortXcvrXfpCdrSupport=_WwpLeosPortXcvrXfpCdrSupport_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,79),_WwpLeosPortXcvrXfpCdrSupport_Type())
wwpLeosPortXcvrXfpCdrSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpCdrSupport.setStatus(_A)
class _WwpLeosPortXcvrXfpWaveLengthTol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpWaveLengthTol_Type.__name__=_C
_WwpLeosPortXcvrXfpWaveLengthTol_Object=MibTableColumn
wwpLeosPortXcvrXfpWaveLengthTol=_WwpLeosPortXcvrXfpWaveLengthTol_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,80),_WwpLeosPortXcvrXfpWaveLengthTol_Type())
wwpLeosPortXcvrXfpWaveLengthTol.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpWaveLengthTol.setStatus(_A)
class _WwpLeosPortXcvrXfpMaxCaseTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMaxCaseTemp_Type.__name__=_C
_WwpLeosPortXcvrXfpMaxCaseTemp_Object=MibTableColumn
wwpLeosPortXcvrXfpMaxCaseTemp=_WwpLeosPortXcvrXfpMaxCaseTemp_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,81),_WwpLeosPortXcvrXfpMaxCaseTemp_Type())
wwpLeosPortXcvrXfpMaxCaseTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMaxCaseTemp.setStatus(_A)
class _WwpLeosPortXcvrXfpMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMaxPower_Type.__name__=_C
_WwpLeosPortXcvrXfpMaxPower_Object=MibTableColumn
wwpLeosPortXcvrXfpMaxPower=_WwpLeosPortXcvrXfpMaxPower_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,82),_WwpLeosPortXcvrXfpMaxPower_Type())
wwpLeosPortXcvrXfpMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMaxPower.setStatus(_A)
class _WwpLeosPortXcvrXfpMax5vCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMax5vCurrent_Type.__name__=_C
_WwpLeosPortXcvrXfpMax5vCurrent_Object=MibTableColumn
wwpLeosPortXcvrXfpMax5vCurrent=_WwpLeosPortXcvrXfpMax5vCurrent_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,83),_WwpLeosPortXcvrXfpMax5vCurrent_Type())
wwpLeosPortXcvrXfpMax5vCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMax5vCurrent.setStatus(_A)
class _WwpLeosPortXcvrXfpMax3p3vCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMax3p3vCurrent_Type.__name__=_C
_WwpLeosPortXcvrXfpMax3p3vCurrent_Object=MibTableColumn
wwpLeosPortXcvrXfpMax3p3vCurrent=_WwpLeosPortXcvrXfpMax3p3vCurrent_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,84),_WwpLeosPortXcvrXfpMax3p3vCurrent_Type())
wwpLeosPortXcvrXfpMax3p3vCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMax3p3vCurrent.setStatus(_A)
class _WwpLeosPortXcvrXfpMax1p8vCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMax1p8vCurrent_Type.__name__=_C
_WwpLeosPortXcvrXfpMax1p8vCurrent_Object=MibTableColumn
wwpLeosPortXcvrXfpMax1p8vCurrent=_WwpLeosPortXcvrXfpMax1p8vCurrent_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,85),_WwpLeosPortXcvrXfpMax1p8vCurrent_Type())
wwpLeosPortXcvrXfpMax1p8vCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMax1p8vCurrent.setStatus(_A)
class _WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Type.__name__=_C
_WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Object=MibTableColumn
wwpLeosPortXcvrXfpMaxNeg5p2vCurrent=_WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,86),_WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Type())
wwpLeosPortXcvrXfpMaxNeg5p2vCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMaxNeg5p2vCurrent.setStatus(_A)
class _WwpLeosPortXcvrXfpDiagMonitorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpDiagMonitorType_Type.__name__=_C
_WwpLeosPortXcvrXfpDiagMonitorType_Object=MibTableColumn
wwpLeosPortXcvrXfpDiagMonitorType=_WwpLeosPortXcvrXfpDiagMonitorType_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,87),_WwpLeosPortXcvrXfpDiagMonitorType_Type())
wwpLeosPortXcvrXfpDiagMonitorType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpDiagMonitorType.setStatus(_A)
class _WwpLeosPortXcvrXfpEnhancedOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpEnhancedOptions_Type.__name__=_C
_WwpLeosPortXcvrXfpEnhancedOptions_Object=MibTableColumn
wwpLeosPortXcvrXfpEnhancedOptions=_WwpLeosPortXcvrXfpEnhancedOptions_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,88),_WwpLeosPortXcvrXfpEnhancedOptions_Type())
wwpLeosPortXcvrXfpEnhancedOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpEnhancedOptions.setStatus(_A)
class _WwpLeosPortXcvrXfpAuxMonitoringInput1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_N,1),(_Q,2),(_L,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_K,15)))
_WwpLeosPortXcvrXfpAuxMonitoringInput1_Type.__name__=_C
_WwpLeosPortXcvrXfpAuxMonitoringInput1_Object=MibTableColumn
wwpLeosPortXcvrXfpAuxMonitoringInput1=_WwpLeosPortXcvrXfpAuxMonitoringInput1_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,89),_WwpLeosPortXcvrXfpAuxMonitoringInput1_Type())
wwpLeosPortXcvrXfpAuxMonitoringInput1.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpAuxMonitoringInput1.setStatus(_A)
class _WwpLeosPortXcvrXfpAuxMonitoringInput2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_N,1),(_Q,2),(_L,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_K,15)))
_WwpLeosPortXcvrXfpAuxMonitoringInput2_Type.__name__=_C
_WwpLeosPortXcvrXfpAuxMonitoringInput2_Object=MibTableColumn
wwpLeosPortXcvrXfpAuxMonitoringInput2=_WwpLeosPortXcvrXfpAuxMonitoringInput2_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,90),_WwpLeosPortXcvrXfpAuxMonitoringInput2_Type())
wwpLeosPortXcvrXfpAuxMonitoringInput2.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpAuxMonitoringInput2.setStatus(_A)
class _WwpLeosPortXcvrAdminFrequency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwpLeosPortXcvrAdminFrequency_Type.__name__=_J
_WwpLeosPortXcvrAdminFrequency_Object=MibTableColumn
wwpLeosPortXcvrAdminFrequency=_WwpLeosPortXcvrAdminFrequency_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,91),_WwpLeosPortXcvrAdminFrequency_Type())
wwpLeosPortXcvrAdminFrequency.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosPortXcvrAdminFrequency.setStatus(_A)
class _WwpLeosPortXcvrXfpLaserFirstFrequency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwpLeosPortXcvrXfpLaserFirstFrequency_Type.__name__=_J
_WwpLeosPortXcvrXfpLaserFirstFrequency_Object=MibTableColumn
wwpLeosPortXcvrXfpLaserFirstFrequency=_WwpLeosPortXcvrXfpLaserFirstFrequency_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,92),_WwpLeosPortXcvrXfpLaserFirstFrequency_Type())
wwpLeosPortXcvrXfpLaserFirstFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLaserFirstFrequency.setStatus(_A)
class _WwpLeosPortXcvrXfpLaserLastFrquency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwpLeosPortXcvrXfpLaserLastFrquency_Type.__name__=_J
_WwpLeosPortXcvrXfpLaserLastFrquency_Object=MibTableColumn
wwpLeosPortXcvrXfpLaserLastFrquency=_WwpLeosPortXcvrXfpLaserLastFrquency_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,93),_WwpLeosPortXcvrXfpLaserLastFrquency_Type())
wwpLeosPortXcvrXfpLaserLastFrquency.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLaserLastFrquency.setStatus(_A)
class _WwpLeosPortXcvrXfpMaxGridScacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosPortXcvrXfpMaxGridScacing_Type.__name__=_C
_WwpLeosPortXcvrXfpMaxGridScacing_Object=MibTableColumn
wwpLeosPortXcvrXfpMaxGridScacing=_WwpLeosPortXcvrXfpMaxGridScacing_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,94),_WwpLeosPortXcvrXfpMaxGridScacing_Type())
wwpLeosPortXcvrXfpMaxGridScacing.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpMaxGridScacing.setStatus(_A)
class _WwpLeosPortXcvrXfpChannelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortXcvrXfpChannelNum_Type.__name__=_C
_WwpLeosPortXcvrXfpChannelNum_Object=MibTableColumn
wwpLeosPortXcvrXfpChannelNum=_WwpLeosPortXcvrXfpChannelNum_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,95),_WwpLeosPortXcvrXfpChannelNum_Type())
wwpLeosPortXcvrXfpChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpChannelNum.setStatus(_A)
class _WwpLeosPortXcvrXfpFrequencyError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_WwpLeosPortXcvrXfpFrequencyError_Type.__name__=_C
_WwpLeosPortXcvrXfpFrequencyError_Object=MibTableColumn
wwpLeosPortXcvrXfpFrequencyError=_WwpLeosPortXcvrXfpFrequencyError_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,96),_WwpLeosPortXcvrXfpFrequencyError_Type())
wwpLeosPortXcvrXfpFrequencyError.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpFrequencyError.setStatus(_A)
_WwpLeosPortXcvrAdminWavelength_Type=Unsigned32
_WwpLeosPortXcvrAdminWavelength_Object=MibTableColumn
wwpLeosPortXcvrAdminWavelength=_WwpLeosPortXcvrAdminWavelength_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,97),_WwpLeosPortXcvrAdminWavelength_Type())
wwpLeosPortXcvrAdminWavelength.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosPortXcvrAdminWavelength.setStatus(_A)
_WwpLeosPortXcvrAdminChannel_Type=Unsigned32
_WwpLeosPortXcvrAdminChannel_Object=MibTableColumn
wwpLeosPortXcvrAdminChannel=_WwpLeosPortXcvrAdminChannel_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,98),_WwpLeosPortXcvrAdminChannel_Type())
wwpLeosPortXcvrAdminChannel.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosPortXcvrAdminChannel.setStatus(_A)
_WwpLeosPortXcvrXfpLaserFirstWavelenth_Type=Unsigned32
_WwpLeosPortXcvrXfpLaserFirstWavelenth_Object=MibTableColumn
wwpLeosPortXcvrXfpLaserFirstWavelenth=_WwpLeosPortXcvrXfpLaserFirstWavelenth_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,99),_WwpLeosPortXcvrXfpLaserFirstWavelenth_Type())
wwpLeosPortXcvrXfpLaserFirstWavelenth.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLaserFirstWavelenth.setStatus(_A)
_WwpLeosPortXcvrXfpLaserLastWavelength_Type=Unsigned32
_WwpLeosPortXcvrXfpLaserLastWavelength_Object=MibTableColumn
wwpLeosPortXcvrXfpLaserLastWavelength=_WwpLeosPortXcvrXfpLaserLastWavelength_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,100),_WwpLeosPortXcvrXfpLaserLastWavelength_Type())
wwpLeosPortXcvrXfpLaserLastWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLaserLastWavelength.setStatus(_A)
_WwpLeosPortXcvrXfpLaserFirstChannel_Type=Unsigned32
_WwpLeosPortXcvrXfpLaserFirstChannel_Object=MibTableColumn
wwpLeosPortXcvrXfpLaserFirstChannel=_WwpLeosPortXcvrXfpLaserFirstChannel_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,101),_WwpLeosPortXcvrXfpLaserFirstChannel_Type())
wwpLeosPortXcvrXfpLaserFirstChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLaserFirstChannel.setStatus(_A)
_WwpLeosPortXcvrXfpLaserLastChannel_Type=Unsigned32
_WwpLeosPortXcvrXfpLaserLastChannel_Object=MibTableColumn
wwpLeosPortXcvrXfpLaserLastChannel=_WwpLeosPortXcvrXfpLaserLastChannel_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,102),_WwpLeosPortXcvrXfpLaserLastChannel_Type())
wwpLeosPortXcvrXfpLaserLastChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrXfpLaserLastChannel.setStatus(_A)
_WwpLeosPortXcvrOperFrequency_Type=Unsigned32
_WwpLeosPortXcvrOperFrequency_Object=MibTableColumn
wwpLeosPortXcvrOperFrequency=_WwpLeosPortXcvrOperFrequency_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,103),_WwpLeosPortXcvrOperFrequency_Type())
wwpLeosPortXcvrOperFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrOperFrequency.setStatus(_A)
_WwpLeosPortXcvrOperWavelength_Type=Unsigned32
_WwpLeosPortXcvrOperWavelength_Object=MibTableColumn
wwpLeosPortXcvrOperWavelength=_WwpLeosPortXcvrOperWavelength_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,104),_WwpLeosPortXcvrOperWavelength_Type())
wwpLeosPortXcvrOperWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrOperWavelength.setStatus(_A)
_WwpLeosPortXcvrRxDbmPower_Type=Integer32
_WwpLeosPortXcvrRxDbmPower_Object=MibTableColumn
wwpLeosPortXcvrRxDbmPower=_WwpLeosPortXcvrRxDbmPower_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,105),_WwpLeosPortXcvrRxDbmPower_Type())
wwpLeosPortXcvrRxDbmPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrRxDbmPower.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrRxDbmPower.setUnits(_G)
_WwpLeosPortXcvrTxDbmPower_Type=Integer32
_WwpLeosPortXcvrTxDbmPower_Object=MibTableColumn
wwpLeosPortXcvrTxDbmPower=_WwpLeosPortXcvrTxDbmPower_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,106),_WwpLeosPortXcvrTxDbmPower_Type())
wwpLeosPortXcvrTxDbmPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrTxDbmPower.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrTxDbmPower.setUnits(_G)
_WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrHighTxDbmPwAlarmThreshold=_WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,107),_WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Type())
wwpLeosPortXcvrHighTxDbmPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighTxDbmPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighTxDbmPwAlarmThreshold.setUnits(_G)
_WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrLowTxDbmPwAlarmThreshold=_WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,108),_WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Type())
wwpLeosPortXcvrLowTxDbmPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowTxDbmPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowTxDbmPwAlarmThreshold.setUnits(_G)
_WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrHighRxDbmPwAlarmThreshold=_WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,109),_WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Type())
wwpLeosPortXcvrHighRxDbmPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighRxDbmPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrHighRxDbmPwAlarmThreshold.setUnits(_G)
_WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Type=Integer32
_WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Object=MibTableColumn
wwpLeosPortXcvrLowRxDbmPwAlarmThreshold=_WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Object((1,3,6,1,4,1,6141,2,60,4,1,1,1,1,110),_WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Type())
wwpLeosPortXcvrLowRxDbmPwAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowRxDbmPwAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPortXcvrLowRxDbmPwAlarmThreshold.setUnits(_G)
_WwpLeosPortXcvrNotif_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvrNotif=_WwpLeosPortXcvrNotif_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,1,2))
class _WwpLeosPortXcvrEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inserted',1),('removed',2),(_I,3),(_H,4)))
_WwpLeosPortXcvrEventType_Type.__name__=_C
_WwpLeosPortXcvrEventType_Object=MibScalar
wwpLeosPortXcvrEventType=_WwpLeosPortXcvrEventType_Object((1,3,6,1,4,1,6141,2,60,4,1,2,1),_WwpLeosPortXcvrEventType_Type())
wwpLeosPortXcvrEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrEventType.setStatus(_A)
class _WwpLeosPortXcvrErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('chksumFailed',1),('opticalFault',2)))
_WwpLeosPortXcvrErrorType_Type.__name__=_C
_WwpLeosPortXcvrErrorType_Object=MibScalar
wwpLeosPortXcvrErrorType=_WwpLeosPortXcvrErrorType_Object((1,3,6,1,4,1,6141,2,60,4,1,2,2),_WwpLeosPortXcvrErrorType_Type())
wwpLeosPortXcvrErrorType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortXcvrErrorType.setStatus(_A)
_WwpLeosPortXcvrMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvrMIBNotificationPrefix=_WwpLeosPortXcvrMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,2))
_WwpLeosPortXcvrMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvrMIBNotifications=_WwpLeosPortXcvrMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,2,0))
_WwpLeosPortXcvrMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvrMIBConformance=_WwpLeosPortXcvrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,3))
_WwpLeosPortXcvrMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvrMIBCompliances=_WwpLeosPortXcvrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,3,1))
_WwpLeosPortXcvrMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosPortXcvrMIBGroups=_WwpLeosPortXcvrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,4,3,2))
wwpLeosPortXcvrLinkStateChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,4))
wwpLeosPortXcvrLinkStateChangeNotification.setObjects(*((_D,_E),(_D,_c)))
if mibBuilder.loadTexts:wwpLeosPortXcvrLinkStateChangeNotification.setStatus(_A)
wwpLeosPortXcvrErrorTypeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,5))
wwpLeosPortXcvrErrorTypeNotification.setObjects(*((_D,_E),(_D,_d)))
if mibBuilder.loadTexts:wwpLeosPortXcvrErrorTypeNotification.setStatus(_A)
wwpLeosPortXcvrTempHighNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,6))
wwpLeosPortXcvrTempHighNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTempHighNotification.setStatus(_A)
wwpLeosPortXcvrTempLowNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,7))
wwpLeosPortXcvrTempLowNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTempLowNotification.setStatus(_A)
wwpLeosPortXcvrTempNormalNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,8))
wwpLeosPortXcvrTempNormalNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTempNormalNotification.setStatus(_A)
wwpLeosPortXcvrVoltageHighNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,9))
wwpLeosPortXcvrVoltageHighNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrVoltageHighNotification.setStatus(_A)
wwpLeosPortXcvrVoltageLowNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,10))
wwpLeosPortXcvrVoltageLowNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrVoltageLowNotification.setStatus(_A)
wwpLeosPortXcvrVoltageNormalNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,11))
wwpLeosPortXcvrVoltageNormalNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrVoltageNormalNotification.setStatus(_A)
wwpLeosPortXcvrBiasHighNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,12))
wwpLeosPortXcvrBiasHighNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrBiasHighNotification.setStatus(_A)
wwpLeosPortXcvrBiasLowNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,13))
wwpLeosPortXcvrBiasLowNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrBiasLowNotification.setStatus(_A)
wwpLeosPortXcvrBiasNormalNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,14))
wwpLeosPortXcvrBiasNormalNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrBiasNormalNotification.setStatus(_A)
wwpLeosPortXcvrTxPowerHighNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,15))
wwpLeosPortXcvrTxPowerHighNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTxPowerHighNotification.setStatus(_A)
wwpLeosPortXcvrTxPowerLowNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,16))
wwpLeosPortXcvrTxPowerLowNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTxPowerLowNotification.setStatus(_A)
wwpLeosPortXcvrTxPowerNormalNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,17))
wwpLeosPortXcvrTxPowerNormalNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTxPowerNormalNotification.setStatus(_A)
wwpLeosPortXcvrRxPowerHighNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,18))
wwpLeosPortXcvrRxPowerHighNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrRxPowerHighNotification.setStatus(_A)
wwpLeosPortXcvrRxPowerLowNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,19))
wwpLeosPortXcvrRxPowerLowNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrRxPowerLowNotification.setStatus(_A)
wwpLeosPortXcvrRxPowerNormalNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,20))
wwpLeosPortXcvrRxPowerNormalNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrRxPowerNormalNotification.setStatus(_A)
wwpLeosPortXcvrSpeedInfoMissingNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,21))
wwpLeosPortXcvrSpeedInfoMissingNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrSpeedInfoMissingNotification.setStatus(_A)
wwpLeosPortXcvrBiasHighWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,22))
wwpLeosPortXcvrBiasHighWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrBiasHighWarningNotification.setStatus(_A)
wwpLeosPortXcvrBiasLowWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,23))
wwpLeosPortXcvrBiasLowWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrBiasLowWarningNotification.setStatus(_A)
wwpLeosPortXcvrTempHighWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,24))
wwpLeosPortXcvrTempHighWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTempHighWarningNotification.setStatus(_A)
wwpLeosPortXcvrTempLowWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,25))
wwpLeosPortXcvrTempLowWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTempLowWarningNotification.setStatus(_A)
wwpLeosPortXcvrVoltageHighWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,26))
wwpLeosPortXcvrVoltageHighWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrVoltageHighWarningNotification.setStatus(_A)
wwpLeosPortXcvrVoltageLowWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,27))
wwpLeosPortXcvrVoltageLowWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrVoltageLowWarningNotification.setStatus(_A)
wwpLeosPortXcvrTxPowerHighWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,28))
wwpLeosPortXcvrTxPowerHighWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTxPowerHighWarningNotification.setStatus(_A)
wwpLeosPortXcvrTxPowerLowWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,29))
wwpLeosPortXcvrTxPowerLowWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrTxPowerLowWarningNotification.setStatus(_A)
wwpLeosPortXcvrRxPowerHighWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,30))
wwpLeosPortXcvrRxPowerHighWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrRxPowerHighWarningNotification.setStatus(_A)
wwpLeosPortXcvrRxPowerLowWarningNotification=NotificationType((1,3,6,1,4,1,6141,2,60,4,2,0,31))
wwpLeosPortXcvrRxPowerLowWarningNotification.setObjects((_D,_E))
if mibBuilder.loadTexts:wwpLeosPortXcvrRxPowerLowWarningNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpLeosPortXcvrMIB':wwpLeosPortXcvrMIB,'wwpLeosPortXcvrMIBObjects':wwpLeosPortXcvrMIBObjects,'wwpLeosPortXcvr':wwpLeosPortXcvr,'wwpLeosPortXcvrTable':wwpLeosPortXcvrTable,'wwpLeosPortXcvrEntry':wwpLeosPortXcvrEntry,_E:wwpLeosPortXcvrId,'wwpLeosPortXcvrOperState':wwpLeosPortXcvrOperState,'wwpLeosPortXcvrIdentiferType':wwpLeosPortXcvrIdentiferType,'wwpLeosPortXcvrExtIdentiferType':wwpLeosPortXcvrExtIdentiferType,'wwpLeosPortXcvrConnectorType':wwpLeosPortXcvrConnectorType,'wwpLeosPortXcvrType':wwpLeosPortXcvrType,'wwpLeosPortXcvrVendorName':wwpLeosPortXcvrVendorName,'wwpLeosPortXcvrVendorOUI':wwpLeosPortXcvrVendorOUI,'wwpLeosPortXcvrVendorPN':wwpLeosPortXcvrVendorPN,'wwpLeosPortXcvrRevNum':wwpLeosPortXcvrRevNum,'wwpLeosPortXcvrSerialNum':wwpLeosPortXcvrSerialNum,'wwpLeosPortXcvrEncodingType':wwpLeosPortXcvrEncodingType,'wwpLeosPortXcvrMfgDate':wwpLeosPortXcvrMfgDate,'wwpLeosPortXcvrComplianceVer':wwpLeosPortXcvrComplianceVer,'wwpLeosPortXcvrWaveLength':wwpLeosPortXcvrWaveLength,'wwpLeosPortXcvrTemperature':wwpLeosPortXcvrTemperature,'wwpLeosPortXcvrVcc':wwpLeosPortXcvrVcc,'wwpLeosPortXcvrBias':wwpLeosPortXcvrBias,'wwpLeosPortXcvrRxPower':wwpLeosPortXcvrRxPower,'wwpLeosPortXcvrTxState':wwpLeosPortXcvrTxState,'wwpLeosPortXcvrTxFaultStatus':wwpLeosPortXcvrTxFaultStatus,'wwpLeosPortXcvrRxRateStatus':wwpLeosPortXcvrRxRateStatus,'wwpLeosPortXcvr9by125um':wwpLeosPortXcvr9by125um,'wwpLeosPortXcvr50by125um':wwpLeosPortXcvr50by125um,'wwpLeosPortXcvr62dot5by125um':wwpLeosPortXcvr62dot5by125um,'wwpLeosPortXcvrCu':wwpLeosPortXcvrCu,'wwpLeosPortXcvrTxOutputPw':wwpLeosPortXcvrTxOutputPw,'wwpLeosPortXcvrLosState':wwpLeosPortXcvrLosState,'wwpLeosPortXcvrDiagSupported':wwpLeosPortXcvrDiagSupported,'wwpLeosPortXcvrEnhDiagAlarmSupported':wwpLeosPortXcvrEnhDiagAlarmSupported,'wwpLeosPortXcvrEnhDiagSoftTxDisableSupported':wwpLeosPortXcvrEnhDiagSoftTxDisableSupported,'wwpLeosPortXcvrEnhDiagSoftTxFaultSupported':wwpLeosPortXcvrEnhDiagSoftTxFaultSupported,'wwpLeosPortXcvrEnhDiagRxLosSupported':wwpLeosPortXcvrEnhDiagRxLosSupported,'wwpLeosPortXcvrHighTempAlarmThreshold':wwpLeosPortXcvrHighTempAlarmThreshold,'wwpLeosPortXcvrLowTempAlarmThreshold':wwpLeosPortXcvrLowTempAlarmThreshold,'wwpLeosPortXcvrHighVccAlarmThreshold':wwpLeosPortXcvrHighVccAlarmThreshold,'wwpLeosPortXcvrLowVccAlarmThreshold':wwpLeosPortXcvrLowVccAlarmThreshold,'wwpLeosPortXcvrHighBiasAlarmThreshold':wwpLeosPortXcvrHighBiasAlarmThreshold,'wwpLeosPortXcvrLowBiasAlarmThreshold':wwpLeosPortXcvrLowBiasAlarmThreshold,'wwpLeosPortXcvrHighTxPwAlarmThreshold':wwpLeosPortXcvrHighTxPwAlarmThreshold,'wwpLeosPortXcvrLowTxPwAlarmThreshold':wwpLeosPortXcvrLowTxPwAlarmThreshold,'wwpLeosPortXcvrHighRxPwAlarmThreshold':wwpLeosPortXcvrHighRxPwAlarmThreshold,'wwpLeosPortXcvrLowRxPwAlarmThreshold':wwpLeosPortXcvrLowRxPwAlarmThreshold,'wwpLeosPortXcvrEnhDiagRateSelectSupported':wwpLeosPortXcvrEnhDiagRateSelectSupported,'wwpLeosPortXcvrAdminState':wwpLeosPortXcvrAdminState,'wwpLeosPortXcvrXfpMinBitRate':wwpLeosPortXcvrXfpMinBitRate,'wwpLeosPortXcvrXfpMaxBitRate':wwpLeosPortXcvrXfpMaxBitRate,'wwpLeosPortXcvrXfpLinkLenSmf1km':wwpLeosPortXcvrXfpLinkLenSmf1km,'wwpLeosPortXcvrXfpLinkLenE50u2m':wwpLeosPortXcvrXfpLinkLenE50u2m,'wwpLeosPortXcvrXfpLinkLen50u1m':wwpLeosPortXcvrXfpLinkLen50u1m,'wwpLeosPortXcvrXfpLinkLen62dot5u1m':wwpLeosPortXcvrXfpLinkLen62dot5u1m,'wwpLeosPortXcvrXfpLinkLenCopper1m':wwpLeosPortXcvrXfpLinkLenCopper1m,'wwpLeosPortXcvrXfpDevTech':wwpLeosPortXcvrXfpDevTech,'wwpLeosPortXcvrXfpTransmitterTech':wwpLeosPortXcvrXfpTransmitterTech,'wwpLeosPortXcvrXfpCdrSupport':wwpLeosPortXcvrXfpCdrSupport,'wwpLeosPortXcvrXfpWaveLengthTol':wwpLeosPortXcvrXfpWaveLengthTol,'wwpLeosPortXcvrXfpMaxCaseTemp':wwpLeosPortXcvrXfpMaxCaseTemp,'wwpLeosPortXcvrXfpMaxPower':wwpLeosPortXcvrXfpMaxPower,'wwpLeosPortXcvrXfpMax5vCurrent':wwpLeosPortXcvrXfpMax5vCurrent,'wwpLeosPortXcvrXfpMax3p3vCurrent':wwpLeosPortXcvrXfpMax3p3vCurrent,'wwpLeosPortXcvrXfpMax1p8vCurrent':wwpLeosPortXcvrXfpMax1p8vCurrent,'wwpLeosPortXcvrXfpMaxNeg5p2vCurrent':wwpLeosPortXcvrXfpMaxNeg5p2vCurrent,'wwpLeosPortXcvrXfpDiagMonitorType':wwpLeosPortXcvrXfpDiagMonitorType,'wwpLeosPortXcvrXfpEnhancedOptions':wwpLeosPortXcvrXfpEnhancedOptions,'wwpLeosPortXcvrXfpAuxMonitoringInput1':wwpLeosPortXcvrXfpAuxMonitoringInput1,'wwpLeosPortXcvrXfpAuxMonitoringInput2':wwpLeosPortXcvrXfpAuxMonitoringInput2,'wwpLeosPortXcvrAdminFrequency':wwpLeosPortXcvrAdminFrequency,'wwpLeosPortXcvrXfpLaserFirstFrequency':wwpLeosPortXcvrXfpLaserFirstFrequency,'wwpLeosPortXcvrXfpLaserLastFrquency':wwpLeosPortXcvrXfpLaserLastFrquency,'wwpLeosPortXcvrXfpMaxGridScacing':wwpLeosPortXcvrXfpMaxGridScacing,'wwpLeosPortXcvrXfpChannelNum':wwpLeosPortXcvrXfpChannelNum,'wwpLeosPortXcvrXfpFrequencyError':wwpLeosPortXcvrXfpFrequencyError,'wwpLeosPortXcvrAdminWavelength':wwpLeosPortXcvrAdminWavelength,'wwpLeosPortXcvrAdminChannel':wwpLeosPortXcvrAdminChannel,'wwpLeosPortXcvrXfpLaserFirstWavelenth':wwpLeosPortXcvrXfpLaserFirstWavelenth,'wwpLeosPortXcvrXfpLaserLastWavelength':wwpLeosPortXcvrXfpLaserLastWavelength,'wwpLeosPortXcvrXfpLaserFirstChannel':wwpLeosPortXcvrXfpLaserFirstChannel,'wwpLeosPortXcvrXfpLaserLastChannel':wwpLeosPortXcvrXfpLaserLastChannel,'wwpLeosPortXcvrOperFrequency':wwpLeosPortXcvrOperFrequency,'wwpLeosPortXcvrOperWavelength':wwpLeosPortXcvrOperWavelength,'wwpLeosPortXcvrRxDbmPower':wwpLeosPortXcvrRxDbmPower,'wwpLeosPortXcvrTxDbmPower':wwpLeosPortXcvrTxDbmPower,'wwpLeosPortXcvrHighTxDbmPwAlarmThreshold':wwpLeosPortXcvrHighTxDbmPwAlarmThreshold,'wwpLeosPortXcvrLowTxDbmPwAlarmThreshold':wwpLeosPortXcvrLowTxDbmPwAlarmThreshold,'wwpLeosPortXcvrHighRxDbmPwAlarmThreshold':wwpLeosPortXcvrHighRxDbmPwAlarmThreshold,'wwpLeosPortXcvrLowRxDbmPwAlarmThreshold':wwpLeosPortXcvrLowRxDbmPwAlarmThreshold,'wwpLeosPortXcvrNotif':wwpLeosPortXcvrNotif,_c:wwpLeosPortXcvrEventType,_d:wwpLeosPortXcvrErrorType,'wwpLeosPortXcvrMIBNotificationPrefix':wwpLeosPortXcvrMIBNotificationPrefix,'wwpLeosPortXcvrMIBNotifications':wwpLeosPortXcvrMIBNotifications,'wwpLeosPortXcvrLinkStateChangeNotification':wwpLeosPortXcvrLinkStateChangeNotification,'wwpLeosPortXcvrErrorTypeNotification':wwpLeosPortXcvrErrorTypeNotification,'wwpLeosPortXcvrTempHighNotification':wwpLeosPortXcvrTempHighNotification,'wwpLeosPortXcvrTempLowNotification':wwpLeosPortXcvrTempLowNotification,'wwpLeosPortXcvrTempNormalNotification':wwpLeosPortXcvrTempNormalNotification,'wwpLeosPortXcvrVoltageHighNotification':wwpLeosPortXcvrVoltageHighNotification,'wwpLeosPortXcvrVoltageLowNotification':wwpLeosPortXcvrVoltageLowNotification,'wwpLeosPortXcvrVoltageNormalNotification':wwpLeosPortXcvrVoltageNormalNotification,'wwpLeosPortXcvrBiasHighNotification':wwpLeosPortXcvrBiasHighNotification,'wwpLeosPortXcvrBiasLowNotification':wwpLeosPortXcvrBiasLowNotification,'wwpLeosPortXcvrBiasNormalNotification':wwpLeosPortXcvrBiasNormalNotification,'wwpLeosPortXcvrTxPowerHighNotification':wwpLeosPortXcvrTxPowerHighNotification,'wwpLeosPortXcvrTxPowerLowNotification':wwpLeosPortXcvrTxPowerLowNotification,'wwpLeosPortXcvrTxPowerNormalNotification':wwpLeosPortXcvrTxPowerNormalNotification,'wwpLeosPortXcvrRxPowerHighNotification':wwpLeosPortXcvrRxPowerHighNotification,'wwpLeosPortXcvrRxPowerLowNotification':wwpLeosPortXcvrRxPowerLowNotification,'wwpLeosPortXcvrRxPowerNormalNotification':wwpLeosPortXcvrRxPowerNormalNotification,'wwpLeosPortXcvrSpeedInfoMissingNotification':wwpLeosPortXcvrSpeedInfoMissingNotification,'wwpLeosPortXcvrBiasHighWarningNotification':wwpLeosPortXcvrBiasHighWarningNotification,'wwpLeosPortXcvrBiasLowWarningNotification':wwpLeosPortXcvrBiasLowWarningNotification,'wwpLeosPortXcvrTempHighWarningNotification':wwpLeosPortXcvrTempHighWarningNotification,'wwpLeosPortXcvrTempLowWarningNotification':wwpLeosPortXcvrTempLowWarningNotification,'wwpLeosPortXcvrVoltageHighWarningNotification':wwpLeosPortXcvrVoltageHighWarningNotification,'wwpLeosPortXcvrVoltageLowWarningNotification':wwpLeosPortXcvrVoltageLowWarningNotification,'wwpLeosPortXcvrTxPowerHighWarningNotification':wwpLeosPortXcvrTxPowerHighWarningNotification,'wwpLeosPortXcvrTxPowerLowWarningNotification':wwpLeosPortXcvrTxPowerLowWarningNotification,'wwpLeosPortXcvrRxPowerHighWarningNotification':wwpLeosPortXcvrRxPowerHighWarningNotification,'wwpLeosPortXcvrRxPowerLowWarningNotification':wwpLeosPortXcvrRxPowerLowWarningNotification,'wwpLeosPortXcvrMIBConformance':wwpLeosPortXcvrMIBConformance,'wwpLeosPortXcvrMIBCompliances':wwpLeosPortXcvrMIBCompliances,'wwpLeosPortXcvrMIBGroups':wwpLeosPortXcvrMIBGroups})