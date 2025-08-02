_G='micro-watts'
_F='cnTransceiverPortIfIndex'
_E='CAMBIUM-NETWORKS-TRANSCEIVER-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnTransceiverMib=ModuleIdentity((1,3,6,1,4,1,2076,81,18,1))
if mibBuilder.loadTexts:cnTransceiverMib.setRevisions(('2022-09-29 00:00','2018-12-18 00:00'))
_CnTransceiverNotifications_ObjectIdentity=ObjectIdentity
cnTransceiverNotifications=_CnTransceiverNotifications_ObjectIdentity((1,3,6,1,4,1,2076,81,18,1,0))
_CnTransceiverObjects_ObjectIdentity=ObjectIdentity
cnTransceiverObjects=_CnTransceiverObjects_ObjectIdentity((1,3,6,1,4,1,2076,81,18,1,1))
_CnTransceiverPortTable_Object=MibTable
cnTransceiverPortTable=_CnTransceiverPortTable_Object((1,3,6,1,4,1,2076,81,18,1,1,11))
if mibBuilder.loadTexts:cnTransceiverPortTable.setStatus(_A)
_CnTransceiverPortEntry_Object=MibTableRow
cnTransceiverPortEntry=_CnTransceiverPortEntry_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1))
cnTransceiverPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cnTransceiverPortEntry.setStatus(_A)
class _CnTransceiverPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CnTransceiverPortIfIndex_Type.__name__=_C
_CnTransceiverPortIfIndex_Object=MibTableColumn
cnTransceiverPortIfIndex=_CnTransceiverPortIfIndex_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,1),_CnTransceiverPortIfIndex_Type())
cnTransceiverPortIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnTransceiverPortIfIndex.setStatus(_A)
class _CnTransceiverTxEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CnTransceiverTxEnabled_Type.__name__=_C
_CnTransceiverTxEnabled_Object=MibTableColumn
cnTransceiverTxEnabled=_CnTransceiverTxEnabled_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,2),_CnTransceiverTxEnabled_Type())
cnTransceiverTxEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverTxEnabled.setStatus(_A)
class _CnTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('cn1000BASE-T',1),('cn1000BASE-CX',2),('cn1000BASE-LX',3),('cn1000BASE-SX',4),('cn10GBASE-SR',5),('cn10GBASE-LR',6),('cn10GBASE-ER',7),('cn10GBASE-LRM',8),('cn10GBASE-SW',9),('cn10GBASE-LW',10),('cn10GBASE-EW',11)))
_CnTransceiverType_Type.__name__=_C
_CnTransceiverType_Object=MibTableColumn
cnTransceiverType=_CnTransceiverType_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,3),_CnTransceiverType_Type())
cnTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverType.setStatus(_A)
class _CnTransceiverWavelength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CnTransceiverWavelength_Type.__name__=_C
_CnTransceiverWavelength_Object=MibTableColumn
cnTransceiverWavelength=_CnTransceiverWavelength_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,4),_CnTransceiverWavelength_Type())
cnTransceiverWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverWavelength.setStatus(_A)
class _CnTransceiverVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnTransceiverVendorName_Type.__name__=_D
_CnTransceiverVendorName_Object=MibTableColumn
cnTransceiverVendorName=_CnTransceiverVendorName_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,5),_CnTransceiverVendorName_Type())
cnTransceiverVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverVendorName.setStatus(_A)
class _CnTransceiverVendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnTransceiverVendorOUI_Type.__name__=_D
_CnTransceiverVendorOUI_Object=MibTableColumn
cnTransceiverVendorOUI=_CnTransceiverVendorOUI_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,6),_CnTransceiverVendorOUI_Type())
cnTransceiverVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverVendorOUI.setStatus(_A)
class _CnTransceiverVendorPartNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnTransceiverVendorPartNo_Type.__name__=_D
_CnTransceiverVendorPartNo_Object=MibTableColumn
cnTransceiverVendorPartNo=_CnTransceiverVendorPartNo_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,7),_CnTransceiverVendorPartNo_Type())
cnTransceiverVendorPartNo.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverVendorPartNo.setStatus(_A)
class _CnTransceiverVendorRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnTransceiverVendorRevision_Type.__name__=_D
_CnTransceiverVendorRevision_Object=MibTableColumn
cnTransceiverVendorRevision=_CnTransceiverVendorRevision_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,8),_CnTransceiverVendorRevision_Type())
cnTransceiverVendorRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverVendorRevision.setStatus(_A)
class _CnTransceiverVendorSerial_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnTransceiverVendorSerial_Type.__name__=_D
_CnTransceiverVendorSerial_Object=MibTableColumn
cnTransceiverVendorSerial=_CnTransceiverVendorSerial_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,9),_CnTransceiverVendorSerial_Type())
cnTransceiverVendorSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverVendorSerial.setStatus(_A)
class _CnTransceiverDateCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnTransceiverDateCode_Type.__name__=_D
_CnTransceiverDateCode_Object=MibTableColumn
cnTransceiverDateCode=_CnTransceiverDateCode_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,10),_CnTransceiverDateCode_Type())
cnTransceiverDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverDateCode.setStatus(_A)
class _CnTransceiverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_CnTransceiverTemperature_Type.__name__=_C
_CnTransceiverTemperature_Object=MibTableColumn
cnTransceiverTemperature=_CnTransceiverTemperature_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,11),_CnTransceiverTemperature_Type())
cnTransceiverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverTemperature.setStatus(_A)
if mibBuilder.loadTexts:cnTransceiverTemperature.setUnits('celsius')
class _CnTransceiverVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CnTransceiverVoltage_Type.__name__=_C
_CnTransceiverVoltage_Object=MibTableColumn
cnTransceiverVoltage=_CnTransceiverVoltage_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,12),_CnTransceiverVoltage_Type())
cnTransceiverVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverVoltage.setStatus(_A)
if mibBuilder.loadTexts:cnTransceiverVoltage.setUnits('milli-volts')
class _CnTransceiverTxBias_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CnTransceiverTxBias_Type.__name__=_C
_CnTransceiverTxBias_Object=MibTableColumn
cnTransceiverTxBias=_CnTransceiverTxBias_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,13),_CnTransceiverTxBias_Type())
cnTransceiverTxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverTxBias.setStatus(_A)
if mibBuilder.loadTexts:cnTransceiverTxBias.setUnits('micro-amps')
class _CnTransceiverTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CnTransceiverTxPower_Type.__name__=_C
_CnTransceiverTxPower_Object=MibTableColumn
cnTransceiverTxPower=_CnTransceiverTxPower_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,14),_CnTransceiverTxPower_Type())
cnTransceiverTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverTxPower.setStatus(_A)
if mibBuilder.loadTexts:cnTransceiverTxPower.setUnits(_G)
class _CnTransceiverRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CnTransceiverRxPower_Type.__name__=_C
_CnTransceiverRxPower_Object=MibTableColumn
cnTransceiverRxPower=_CnTransceiverRxPower_Object((1,3,6,1,4,1,2076,81,18,1,1,11,1,15),_CnTransceiverRxPower_Type())
cnTransceiverRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cnTransceiverRxPower.setStatus(_A)
if mibBuilder.loadTexts:cnTransceiverRxPower.setUnits(_G)
_CnTransceiverNotifyObjects_ObjectIdentity=ObjectIdentity
cnTransceiverNotifyObjects=_CnTransceiverNotifyObjects_ObjectIdentity((1,3,6,1,4,1,2076,81,18,1,2))
mibBuilder.exportSymbols(_E,**{'cnTransceiverMib':cnTransceiverMib,'cnTransceiverNotifications':cnTransceiverNotifications,'cnTransceiverObjects':cnTransceiverObjects,'cnTransceiverPortTable':cnTransceiverPortTable,'cnTransceiverPortEntry':cnTransceiverPortEntry,_F:cnTransceiverPortIfIndex,'cnTransceiverTxEnabled':cnTransceiverTxEnabled,'cnTransceiverType':cnTransceiverType,'cnTransceiverWavelength':cnTransceiverWavelength,'cnTransceiverVendorName':cnTransceiverVendorName,'cnTransceiverVendorOUI':cnTransceiverVendorOUI,'cnTransceiverVendorPartNo':cnTransceiverVendorPartNo,'cnTransceiverVendorRevision':cnTransceiverVendorRevision,'cnTransceiverVendorSerial':cnTransceiverVendorSerial,'cnTransceiverDateCode':cnTransceiverDateCode,'cnTransceiverTemperature':cnTransceiverTemperature,'cnTransceiverVoltage':cnTransceiverVoltage,'cnTransceiverTxBias':cnTransceiverTxBias,'cnTransceiverTxPower':cnTransceiverTxPower,'cnTransceiverRxPower':cnTransceiverRxPower,'cnTransceiverNotifyObjects':cnTransceiverNotifyObjects})