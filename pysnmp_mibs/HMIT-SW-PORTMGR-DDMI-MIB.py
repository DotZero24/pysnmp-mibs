_F='portDDMIIFindex'
_E='HMIT-SW-PORTMGR-DDMI-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITSwPortmgrMIB,=mibBuilder.importSymbols('HMIT-SW-PORT-MGR-MIB','hmITSwPortmgrMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention')
_PortDDMITable_Object=MibTable
portDDMITable=_PortDDMITable_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6))
if mibBuilder.loadTexts:portDDMITable.setStatus(_A)
_PortDDMIEntry_Object=MibTableRow
portDDMIEntry=_PortDDMIEntry_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1))
portDDMIEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:portDDMIEntry.setStatus(_A)
class _PortDDMIIFindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDDMIIFindex_Type.__name__=_D
_PortDDMIIFindex_Object=MibTableColumn
portDDMIIFindex=_PortDDMIIFindex_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,1),_PortDDMIIFindex_Type())
portDDMIIFindex.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIIFindex.setStatus(_A)
class _PortDDMIDeviceId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIDeviceId_Type.__name__=_C
_PortDDMIDeviceId_Object=MibTableColumn
portDDMIDeviceId=_PortDDMIDeviceId_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,2),_PortDDMIDeviceId_Type())
portDDMIDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIDeviceId.setStatus(_A)
class _PortDDMIConnector_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PortDDMIConnector_Type.__name__=_C
_PortDDMIConnector_Object=MibTableColumn
portDDMIConnector=_PortDDMIConnector_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,3),_PortDDMIConnector_Type())
portDDMIConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIConnector.setStatus(_A)
class _PortDDMIEncoding_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortDDMIEncoding_Type.__name__=_C
_PortDDMIEncoding_Object=MibTableColumn
portDDMIEncoding=_PortDDMIEncoding_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,4),_PortDDMIEncoding_Type())
portDDMIEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIEncoding.setStatus(_A)
class _PortDDMITransmitLen_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PortDDMITransmitLen_Type.__name__=_C
_PortDDMITransmitLen_Object=MibTableColumn
portDDMITransmitLen=_PortDDMITransmitLen_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,6),_PortDDMITransmitLen_Type())
portDDMITransmitLen.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITransmitLen.setStatus(_A)
_PortDDMIVendorOUI_Type=OctetString
_PortDDMIVendorOUI_Object=MibTableColumn
portDDMIVendorOUI=_PortDDMIVendorOUI_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,7),_PortDDMIVendorOUI_Type())
portDDMIVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVendorOUI.setStatus(_A)
class _PortDDMIVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIVendorName_Type.__name__=_C
_PortDDMIVendorName_Object=MibTableColumn
portDDMIVendorName=_PortDDMIVendorName_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,8),_PortDDMIVendorName_Type())
portDDMIVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVendorName.setStatus(_A)
class _PortDDMIPartName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIPartName_Type.__name__=_C
_PortDDMIPartName_Object=MibTableColumn
portDDMIPartName=_PortDDMIPartName_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,9),_PortDDMIPartName_Type())
portDDMIPartName.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIPartName.setStatus(_A)
class _PortDDMIRevisionNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PortDDMIRevisionNum_Type.__name__=_C
_PortDDMIRevisionNum_Object=MibTableColumn
portDDMIRevisionNum=_PortDDMIRevisionNum_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,10),_PortDDMIRevisionNum_Type())
portDDMIRevisionNum.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRevisionNum.setStatus(_A)
class _PortDDMILaserWaveLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDDMILaserWaveLen_Type.__name__=_D
_PortDDMILaserWaveLen_Object=MibTableColumn
portDDMILaserWaveLen=_PortDDMILaserWaveLen_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,11),_PortDDMILaserWaveLen_Type())
portDDMILaserWaveLen.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMILaserWaveLen.setStatus(_A)
class _PortDDMISerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMISerialNum_Type.__name__=_C
_PortDDMISerialNum_Object=MibTableColumn
portDDMISerialNum=_PortDDMISerialNum_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,12),_PortDDMISerialNum_Type())
portDDMISerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMISerialNum.setStatus(_A)
class _PortDDMIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDDMIClass_Type.__name__=_D
_PortDDMIClass_Object=MibTableColumn
portDDMIClass=_PortDDMIClass_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,13),_PortDDMIClass_Type())
portDDMIClass.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIClass.setStatus(_A)
class _PortDDMIProductDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_PortDDMIProductDate_Type.__name__=_C
_PortDDMIProductDate_Object=MibTableColumn
portDDMIProductDate=_PortDDMIProductDate_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,14),_PortDDMIProductDate_Type())
portDDMIProductDate.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIProductDate.setStatus(_A)
_PortDDMIVendorSpecific_Type=OctetString
_PortDDMIVendorSpecific_Object=MibTableColumn
portDDMIVendorSpecific=_PortDDMIVendorSpecific_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,15),_PortDDMIVendorSpecific_Type())
portDDMIVendorSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVendorSpecific.setStatus(_A)
class _PortDDMITmperature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITmperature_Type.__name__=_C
_PortDDMITmperature_Object=MibTableColumn
portDDMITmperature=_PortDDMITmperature_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,16),_PortDDMITmperature_Type())
portDDMITmperature.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITmperature.setStatus(_A)
class _PortDDMITempHighAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITempHighAlarmThreshold_Type.__name__=_C
_PortDDMITempHighAlarmThreshold_Object=MibTableColumn
portDDMITempHighAlarmThreshold=_PortDDMITempHighAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,17),_PortDDMITempHighAlarmThreshold_Type())
portDDMITempHighAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITempHighAlarmThreshold.setStatus(_A)
class _PortDDMITempLowAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITempLowAlarmThreshold_Type.__name__=_C
_PortDDMITempLowAlarmThreshold_Object=MibTableColumn
portDDMITempLowAlarmThreshold=_PortDDMITempLowAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,18),_PortDDMITempLowAlarmThreshold_Type())
portDDMITempLowAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITempLowAlarmThreshold.setStatus(_A)
class _PortDDMITempHighWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITempHighWarningThreshold_Type.__name__=_C
_PortDDMITempHighWarningThreshold_Object=MibTableColumn
portDDMITempHighWarningThreshold=_PortDDMITempHighWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,19),_PortDDMITempHighWarningThreshold_Type())
portDDMITempHighWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITempHighWarningThreshold.setStatus(_A)
class _PortDDMITempLowWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITempLowWarningThreshold_Type.__name__=_C
_PortDDMITempLowWarningThreshold_Object=MibTableColumn
portDDMITempLowWarningThreshold=_PortDDMITempLowWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,20),_PortDDMITempLowWarningThreshold_Type())
portDDMITempLowWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITempLowWarningThreshold.setStatus(_A)
class _PortDDMIVoltage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIVoltage_Type.__name__=_C
_PortDDMIVoltage_Object=MibTableColumn
portDDMIVoltage=_PortDDMIVoltage_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,21),_PortDDMIVoltage_Type())
portDDMIVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVoltage.setStatus(_A)
class _PortDDMIVolHighAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIVolHighAlarmThreshold_Type.__name__=_C
_PortDDMIVolHighAlarmThreshold_Object=MibTableColumn
portDDMIVolHighAlarmThreshold=_PortDDMIVolHighAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,22),_PortDDMIVolHighAlarmThreshold_Type())
portDDMIVolHighAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVolHighAlarmThreshold.setStatus(_A)
class _PortDDMIVolLowAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIVolLowAlarmThreshold_Type.__name__=_C
_PortDDMIVolLowAlarmThreshold_Object=MibTableColumn
portDDMIVolLowAlarmThreshold=_PortDDMIVolLowAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,23),_PortDDMIVolLowAlarmThreshold_Type())
portDDMIVolLowAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVolLowAlarmThreshold.setStatus(_A)
class _PortDDMIVolHighWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIVolHighWarningThreshold_Type.__name__=_C
_PortDDMIVolHighWarningThreshold_Object=MibTableColumn
portDDMIVolHighWarningThreshold=_PortDDMIVolHighWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,24),_PortDDMIVolHighWarningThreshold_Type())
portDDMIVolHighWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVolHighWarningThreshold.setStatus(_A)
class _PortDDMIVolLowWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIVolLowWarningThreshold_Type.__name__=_C
_PortDDMIVolLowWarningThreshold_Object=MibTableColumn
portDDMIVolLowWarningThreshold=_PortDDMIVolLowWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,25),_PortDDMIVolLowWarningThreshold_Type())
portDDMIVolLowWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIVolLowWarningThreshold.setStatus(_A)
class _PortDDMITxBias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBias_Type.__name__=_C
_PortDDMITxBias_Object=MibTableColumn
portDDMITxBias=_PortDDMITxBias_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,26),_PortDDMITxBias_Type())
portDDMITxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBias.setStatus(_A)
class _PortDDMITxBiasHighAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBiasHighAlarmThreshold_Type.__name__=_C
_PortDDMITxBiasHighAlarmThreshold_Object=MibTableColumn
portDDMITxBiasHighAlarmThreshold=_PortDDMITxBiasHighAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,27),_PortDDMITxBiasHighAlarmThreshold_Type())
portDDMITxBiasHighAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBiasHighAlarmThreshold.setStatus(_A)
class _PortDDMITxBiasLowAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBiasLowAlarmThreshold_Type.__name__=_C
_PortDDMITxBiasLowAlarmThreshold_Object=MibTableColumn
portDDMITxBiasLowAlarmThreshold=_PortDDMITxBiasLowAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,28),_PortDDMITxBiasLowAlarmThreshold_Type())
portDDMITxBiasLowAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBiasLowAlarmThreshold.setStatus(_A)
class _PortDDMITxBiasHighWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBiasHighWarningThreshold_Type.__name__=_C
_PortDDMITxBiasHighWarningThreshold_Object=MibTableColumn
portDDMITxBiasHighWarningThreshold=_PortDDMITxBiasHighWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,29),_PortDDMITxBiasHighWarningThreshold_Type())
portDDMITxBiasHighWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBiasHighWarningThreshold.setStatus(_A)
class _PortDDMITxBiasLowWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBiasLowWarningThreshold_Type.__name__=_C
_PortDDMITxBiasLowWarningThreshold_Object=MibTableColumn
portDDMITxBiasLowWarningThreshold=_PortDDMITxBiasLowWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,30),_PortDDMITxBiasLowWarningThreshold_Type())
portDDMITxBiasLowWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBiasLowWarningThreshold.setStatus(_A)
class _PortDDMITxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPower_Type.__name__=_C
_PortDDMITxPower_Object=MibTableColumn
portDDMITxPower=_PortDDMITxPower_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,31),_PortDDMITxPower_Type())
portDDMITxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPower.setStatus(_A)
class _PortDDMITxPowerHighAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPowerHighAlarmThreshold_Type.__name__=_C
_PortDDMITxPowerHighAlarmThreshold_Object=MibTableColumn
portDDMITxPowerHighAlarmThreshold=_PortDDMITxPowerHighAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,32),_PortDDMITxPowerHighAlarmThreshold_Type())
portDDMITxPowerHighAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPowerHighAlarmThreshold.setStatus(_A)
class _PortDDMITxPowerLowAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPowerLowAlarmThreshold_Type.__name__=_C
_PortDDMITxPowerLowAlarmThreshold_Object=MibTableColumn
portDDMITxPowerLowAlarmThreshold=_PortDDMITxPowerLowAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,33),_PortDDMITxPowerLowAlarmThreshold_Type())
portDDMITxPowerLowAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPowerLowAlarmThreshold.setStatus(_A)
class _PortDDMITxPowerHighWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPowerHighWarningThreshold_Type.__name__=_C
_PortDDMITxPowerHighWarningThreshold_Object=MibTableColumn
portDDMITxPowerHighWarningThreshold=_PortDDMITxPowerHighWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,34),_PortDDMITxPowerHighWarningThreshold_Type())
portDDMITxPowerHighWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPowerHighWarningThreshold.setStatus(_A)
class _PortDDMITxPowerLowWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPowerLowWarningThreshold_Type.__name__=_C
_PortDDMITxPowerLowWarningThreshold_Object=MibTableColumn
portDDMITxPowerLowWarningThreshold=_PortDDMITxPowerLowWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,35),_PortDDMITxPowerLowWarningThreshold_Type())
portDDMITxPowerLowWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPowerLowWarningThreshold.setStatus(_A)
class _PortDDMIRxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPower_Type.__name__=_C
_PortDDMIRxPower_Object=MibTableColumn
portDDMIRxPower=_PortDDMIRxPower_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,36),_PortDDMIRxPower_Type())
portDDMIRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPower.setStatus(_A)
class _PortDDMIRxPowerHighAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPowerHighAlarmThreshold_Type.__name__=_C
_PortDDMIRxPowerHighAlarmThreshold_Object=MibTableColumn
portDDMIRxPowerHighAlarmThreshold=_PortDDMIRxPowerHighAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,37),_PortDDMIRxPowerHighAlarmThreshold_Type())
portDDMIRxPowerHighAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPowerHighAlarmThreshold.setStatus(_A)
class _PortDDMIRxPowerLowAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPowerLowAlarmThreshold_Type.__name__=_C
_PortDDMIRxPowerLowAlarmThreshold_Object=MibTableColumn
portDDMIRxPowerLowAlarmThreshold=_PortDDMIRxPowerLowAlarmThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,38),_PortDDMIRxPowerLowAlarmThreshold_Type())
portDDMIRxPowerLowAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPowerLowAlarmThreshold.setStatus(_A)
class _PortDDMIRxPowerHighWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPowerHighWarningThreshold_Type.__name__=_C
_PortDDMIRxPowerHighWarningThreshold_Object=MibTableColumn
portDDMIRxPowerHighWarningThreshold=_PortDDMIRxPowerHighWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,39),_PortDDMIRxPowerHighWarningThreshold_Type())
portDDMIRxPowerHighWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPowerHighWarningThreshold.setStatus(_A)
class _PortDDMIRxPowerLowWarningThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPowerLowWarningThreshold_Type.__name__=_C
_PortDDMIRxPowerLowWarningThreshold_Object=MibTableColumn
portDDMIRxPowerLowWarningThreshold=_PortDDMIRxPowerLowWarningThreshold_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,40),_PortDDMIRxPowerLowWarningThreshold_Type())
portDDMIRxPowerLowWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPowerLowWarningThreshold.setStatus(_A)
_PortDDMIAlarmStatus_Type=OctetString
_PortDDMIAlarmStatus_Object=MibTableColumn
portDDMIAlarmStatus=_PortDDMIAlarmStatus_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,41),_PortDDMIAlarmStatus_Type())
portDDMIAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIAlarmStatus.setStatus(_A)
_PortDDMIWarningStatus_Type=OctetString
_PortDDMIWarningStatus_Object=MibTableColumn
portDDMIWarningStatus=_PortDDMIWarningStatus_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,42),_PortDDMIWarningStatus_Type())
portDDMIWarningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIWarningStatus.setStatus(_A)
class _PortDDMIIsMonotorImpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no_monitor',1),('has_monitor',2)))
_PortDDMIIsMonotorImpt_Type.__name__=_D
_PortDDMIIsMonotorImpt_Object=MibTableColumn
portDDMIIsMonotorImpt=_PortDDMIIsMonotorImpt_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,43),_PortDDMIIsMonotorImpt_Type())
portDDMIIsMonotorImpt.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIIsMonotorImpt.setStatus(_A)
class _PortDDMIResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('offline',2),('timeout',3),('error',4)))
_PortDDMIResult_Type.__name__=_D
_PortDDMIResult_Object=MibTableColumn
portDDMIResult=_PortDDMIResult_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,44),_PortDDMIResult_Type())
portDDMIResult.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIResult.setStatus(_A)
class _PortDDMITxBias2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBias2_Type.__name__=_C
_PortDDMITxBias2_Object=MibTableColumn
portDDMITxBias2=_PortDDMITxBias2_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,45),_PortDDMITxBias2_Type())
portDDMITxBias2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBias2.setStatus(_A)
class _PortDDMITxBias3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBias3_Type.__name__=_C
_PortDDMITxBias3_Object=MibTableColumn
portDDMITxBias3=_PortDDMITxBias3_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,46),_PortDDMITxBias3_Type())
portDDMITxBias3.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBias3.setStatus(_A)
class _PortDDMITxBias4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxBias4_Type.__name__=_C
_PortDDMITxBias4_Object=MibTableColumn
portDDMITxBias4=_PortDDMITxBias4_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,47),_PortDDMITxBias4_Type())
portDDMITxBias4.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxBias4.setStatus(_A)
class _PortDDMIRxPower2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPower2_Type.__name__=_C
_PortDDMIRxPower2_Object=MibTableColumn
portDDMIRxPower2=_PortDDMIRxPower2_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,48),_PortDDMIRxPower2_Type())
portDDMIRxPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPower2.setStatus(_A)
class _PortDDMIRxPower3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPower3_Type.__name__=_C
_PortDDMIRxPower3_Object=MibTableColumn
portDDMIRxPower3=_PortDDMIRxPower3_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,49),_PortDDMIRxPower3_Type())
portDDMIRxPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPower3.setStatus(_A)
class _PortDDMIRxPower4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMIRxPower4_Type.__name__=_C
_PortDDMIRxPower4_Object=MibTableColumn
portDDMIRxPower4=_PortDDMIRxPower4_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,50),_PortDDMIRxPower4_Type())
portDDMIRxPower4.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIRxPower4.setStatus(_A)
_PortDDMIAlarmStatus2_Type=OctetString
_PortDDMIAlarmStatus2_Object=MibTableColumn
portDDMIAlarmStatus2=_PortDDMIAlarmStatus2_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,51),_PortDDMIAlarmStatus2_Type())
portDDMIAlarmStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIAlarmStatus2.setStatus(_A)
_PortDDMIAlarmStatus3_Type=OctetString
_PortDDMIAlarmStatus3_Object=MibTableColumn
portDDMIAlarmStatus3=_PortDDMIAlarmStatus3_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,52),_PortDDMIAlarmStatus3_Type())
portDDMIAlarmStatus3.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIAlarmStatus3.setStatus(_A)
_PortDDMIAlarmStatus4_Type=OctetString
_PortDDMIAlarmStatus4_Object=MibTableColumn
portDDMIAlarmStatus4=_PortDDMIAlarmStatus4_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,53),_PortDDMIAlarmStatus4_Type())
portDDMIAlarmStatus4.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIAlarmStatus4.setStatus(_A)
_PortDDMIWarningStatus2_Type=OctetString
_PortDDMIWarningStatus2_Object=MibTableColumn
portDDMIWarningStatus2=_PortDDMIWarningStatus2_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,54),_PortDDMIWarningStatus2_Type())
portDDMIWarningStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIWarningStatus2.setStatus(_A)
_PortDDMIWarningStatus3_Type=OctetString
_PortDDMIWarningStatus3_Object=MibTableColumn
portDDMIWarningStatus3=_PortDDMIWarningStatus3_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,55),_PortDDMIWarningStatus3_Type())
portDDMIWarningStatus3.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIWarningStatus3.setStatus(_A)
_PortDDMIWarningStatus4_Type=OctetString
_PortDDMIWarningStatus4_Object=MibTableColumn
portDDMIWarningStatus4=_PortDDMIWarningStatus4_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,56),_PortDDMIWarningStatus4_Type())
portDDMIWarningStatus4.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMIWarningStatus4.setStatus(_A)
class _PortDDMITxPower2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPower2_Type.__name__=_C
_PortDDMITxPower2_Object=MibTableColumn
portDDMITxPower2=_PortDDMITxPower2_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,57),_PortDDMITxPower2_Type())
portDDMITxPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPower2.setStatus(_A)
class _PortDDMITxPower3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPower3_Type.__name__=_C
_PortDDMITxPower3_Object=MibTableColumn
portDDMITxPower3=_PortDDMITxPower3_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,58),_PortDDMITxPower3_Type())
portDDMITxPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPower3.setStatus(_A)
class _PortDDMITxPower4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortDDMITxPower4_Type.__name__=_C
_PortDDMITxPower4_Object=MibTableColumn
portDDMITxPower4=_PortDDMITxPower4_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,6,1,59),_PortDDMITxPower4_Type())
portDDMITxPower4.setMaxAccess(_B)
if mibBuilder.loadTexts:portDDMITxPower4.setStatus(_A)
_OpticalModuleExceptionTrap_ObjectIdentity=ObjectIdentity
opticalModuleExceptionTrap=_OpticalModuleExceptionTrap_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100))
opticalModuleTemperatureHighWarnTrap=NotificationType((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100,1))
if mibBuilder.loadTexts:opticalModuleTemperatureHighWarnTrap.setStatus(_A)
opticalModuleTemperatureLowWarnTrap=NotificationType((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100,2))
if mibBuilder.loadTexts:opticalModuleTemperatureLowWarnTrap.setStatus(_A)
opticalModuleTemperatureRecoverTrap=NotificationType((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100,3))
if mibBuilder.loadTexts:opticalModuleTemperatureRecoverTrap.setStatus(_A)
opticalModuleRxpowerLowWarnTrap=NotificationType((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100,4))
if mibBuilder.loadTexts:opticalModuleRxpowerLowWarnTrap.setStatus(_A)
opticalModuleRxpowerRecoverTrap=NotificationType((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100,6))
if mibBuilder.loadTexts:opticalModuleRxpowerRecoverTrap.setStatus(_A)
opticalModuleTxFaultWarnTrap=NotificationType((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100,7))
if mibBuilder.loadTexts:opticalModuleTxFaultWarnTrap.setStatus(_A)
opticalModuleTxFaultRecoverTrap=NotificationType((1,3,6,1,4,1,248,100,1,6,3,1,13,6,100,8))
if mibBuilder.loadTexts:opticalModuleTxFaultRecoverTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'portDDMITable':portDDMITable,'portDDMIEntry':portDDMIEntry,_F:portDDMIIFindex,'portDDMIDeviceId':portDDMIDeviceId,'portDDMIConnector':portDDMIConnector,'portDDMIEncoding':portDDMIEncoding,'portDDMITransmitLen':portDDMITransmitLen,'portDDMIVendorOUI':portDDMIVendorOUI,'portDDMIVendorName':portDDMIVendorName,'portDDMIPartName':portDDMIPartName,'portDDMIRevisionNum':portDDMIRevisionNum,'portDDMILaserWaveLen':portDDMILaserWaveLen,'portDDMISerialNum':portDDMISerialNum,'portDDMIClass':portDDMIClass,'portDDMIProductDate':portDDMIProductDate,'portDDMIVendorSpecific':portDDMIVendorSpecific,'portDDMITmperature':portDDMITmperature,'portDDMITempHighAlarmThreshold':portDDMITempHighAlarmThreshold,'portDDMITempLowAlarmThreshold':portDDMITempLowAlarmThreshold,'portDDMITempHighWarningThreshold':portDDMITempHighWarningThreshold,'portDDMITempLowWarningThreshold':portDDMITempLowWarningThreshold,'portDDMIVoltage':portDDMIVoltage,'portDDMIVolHighAlarmThreshold':portDDMIVolHighAlarmThreshold,'portDDMIVolLowAlarmThreshold':portDDMIVolLowAlarmThreshold,'portDDMIVolHighWarningThreshold':portDDMIVolHighWarningThreshold,'portDDMIVolLowWarningThreshold':portDDMIVolLowWarningThreshold,'portDDMITxBias':portDDMITxBias,'portDDMITxBiasHighAlarmThreshold':portDDMITxBiasHighAlarmThreshold,'portDDMITxBiasLowAlarmThreshold':portDDMITxBiasLowAlarmThreshold,'portDDMITxBiasHighWarningThreshold':portDDMITxBiasHighWarningThreshold,'portDDMITxBiasLowWarningThreshold':portDDMITxBiasLowWarningThreshold,'portDDMITxPower':portDDMITxPower,'portDDMITxPowerHighAlarmThreshold':portDDMITxPowerHighAlarmThreshold,'portDDMITxPowerLowAlarmThreshold':portDDMITxPowerLowAlarmThreshold,'portDDMITxPowerHighWarningThreshold':portDDMITxPowerHighWarningThreshold,'portDDMITxPowerLowWarningThreshold':portDDMITxPowerLowWarningThreshold,'portDDMIRxPower':portDDMIRxPower,'portDDMIRxPowerHighAlarmThreshold':portDDMIRxPowerHighAlarmThreshold,'portDDMIRxPowerLowAlarmThreshold':portDDMIRxPowerLowAlarmThreshold,'portDDMIRxPowerHighWarningThreshold':portDDMIRxPowerHighWarningThreshold,'portDDMIRxPowerLowWarningThreshold':portDDMIRxPowerLowWarningThreshold,'portDDMIAlarmStatus':portDDMIAlarmStatus,'portDDMIWarningStatus':portDDMIWarningStatus,'portDDMIIsMonotorImpt':portDDMIIsMonotorImpt,'portDDMIResult':portDDMIResult,'portDDMITxBias2':portDDMITxBias2,'portDDMITxBias3':portDDMITxBias3,'portDDMITxBias4':portDDMITxBias4,'portDDMIRxPower2':portDDMIRxPower2,'portDDMIRxPower3':portDDMIRxPower3,'portDDMIRxPower4':portDDMIRxPower4,'portDDMIAlarmStatus2':portDDMIAlarmStatus2,'portDDMIAlarmStatus3':portDDMIAlarmStatus3,'portDDMIAlarmStatus4':portDDMIAlarmStatus4,'portDDMIWarningStatus2':portDDMIWarningStatus2,'portDDMIWarningStatus3':portDDMIWarningStatus3,'portDDMIWarningStatus4':portDDMIWarningStatus4,'portDDMITxPower2':portDDMITxPower2,'portDDMITxPower3':portDDMITxPower3,'portDDMITxPower4':portDDMITxPower4,'opticalModuleExceptionTrap':opticalModuleExceptionTrap,'opticalModuleTemperatureHighWarnTrap':opticalModuleTemperatureHighWarnTrap,'opticalModuleTemperatureLowWarnTrap':opticalModuleTemperatureLowWarnTrap,'opticalModuleTemperatureRecoverTrap':opticalModuleTemperatureRecoverTrap,'opticalModuleRxpowerLowWarnTrap':opticalModuleRxpowerLowWarnTrap,'opticalModuleRxpowerRecoverTrap':opticalModuleRxpowerRecoverTrap,'opticalModuleTxFaultWarnTrap':opticalModuleTxFaultWarnTrap,'opticalModuleTxFaultRecoverTrap':opticalModuleTxFaultRecoverTrap})