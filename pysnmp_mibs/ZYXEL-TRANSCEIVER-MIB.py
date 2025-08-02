_K='not-accessible'
_J='zyTransceiverDdmiType'
_I='Integer32'
_H='dot1dBasePort'
_G='BRIDGE-MIB'
_F='zyTransceiverTrapOutOfRangeType'
_E='ifIndex'
_D='IF-MIB'
_C='ZYXEL-TRANSCEIVER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_G,_H)
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelTransceiver=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,84))
_ZyxelTransceiverStatus_ObjectIdentity=ObjectIdentity
zyxelTransceiverStatus=_ZyxelTransceiverStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,84,1))
_ZyxelTransceiverSerialTable_Object=MibTable
zyxelTransceiverSerialTable=_ZyxelTransceiverSerialTable_Object((1,3,6,1,4,1,890,1,15,3,84,1,1))
if mibBuilder.loadTexts:zyxelTransceiverSerialTable.setStatus(_A)
_ZyxelTransceiverSerialEntry_Object=MibTableRow
zyxelTransceiverSerialEntry=_ZyxelTransceiverSerialEntry_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1))
zyxelTransceiverSerialEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zyxelTransceiverSerialEntry.setStatus(_A)
class _ZyTransceiverSerialModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('okWithDdm',1),('okWithoutDdm',2),('nonoperational',3)))
_ZyTransceiverSerialModuleType_Type.__name__=_I
_ZyTransceiverSerialModuleType_Object=MibTableColumn
zyTransceiverSerialModuleType=_ZyTransceiverSerialModuleType_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1,1),_ZyTransceiverSerialModuleType_Type())
zyTransceiverSerialModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverSerialModuleType.setStatus(_A)
_ZyTransceiverSerialVendor_Type=DisplayString
_ZyTransceiverSerialVendor_Object=MibTableColumn
zyTransceiverSerialVendor=_ZyTransceiverSerialVendor_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1,2),_ZyTransceiverSerialVendor_Type())
zyTransceiverSerialVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverSerialVendor.setStatus(_A)
_ZyTransceiverSerialPartNumber_Type=DisplayString
_ZyTransceiverSerialPartNumber_Object=MibTableColumn
zyTransceiverSerialPartNumber=_ZyTransceiverSerialPartNumber_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1,3),_ZyTransceiverSerialPartNumber_Type())
zyTransceiverSerialPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverSerialPartNumber.setStatus(_A)
_ZyTransceiverSerialSerialNumber_Type=DisplayString
_ZyTransceiverSerialSerialNumber_Object=MibTableColumn
zyTransceiverSerialSerialNumber=_ZyTransceiverSerialSerialNumber_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1,4),_ZyTransceiverSerialSerialNumber_Type())
zyTransceiverSerialSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverSerialSerialNumber.setStatus(_A)
_ZyTransceiverSerialRevision_Type=DisplayString
_ZyTransceiverSerialRevision_Object=MibTableColumn
zyTransceiverSerialRevision=_ZyTransceiverSerialRevision_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1,5),_ZyTransceiverSerialRevision_Type())
zyTransceiverSerialRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverSerialRevision.setStatus(_A)
_ZyTransceiverSerialDateCode_Type=DisplayString
_ZyTransceiverSerialDateCode_Object=MibTableColumn
zyTransceiverSerialDateCode=_ZyTransceiverSerialDateCode_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1,6),_ZyTransceiverSerialDateCode_Type())
zyTransceiverSerialDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverSerialDateCode.setStatus(_A)
_ZyTransceiverSerialTransceiver_Type=DisplayString
_ZyTransceiverSerialTransceiver_Object=MibTableColumn
zyTransceiverSerialTransceiver=_ZyTransceiverSerialTransceiver_Object((1,3,6,1,4,1,890,1,15,3,84,1,1,1,7),_ZyTransceiverSerialTransceiver_Type())
zyTransceiverSerialTransceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverSerialTransceiver.setStatus(_A)
_ZyxelTransceiverDdmiTable_Object=MibTable
zyxelTransceiverDdmiTable=_ZyxelTransceiverDdmiTable_Object((1,3,6,1,4,1,890,1,15,3,84,1,2))
if mibBuilder.loadTexts:zyxelTransceiverDdmiTable.setStatus(_A)
_ZyxelTransceiverDdmiEntry_Object=MibTableRow
zyxelTransceiverDdmiEntry=_ZyxelTransceiverDdmiEntry_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1))
zyxelTransceiverDdmiEntry.setIndexNames((0,_G,_H),(0,_C,_J))
if mibBuilder.loadTexts:zyxelTransceiverDdmiEntry.setStatus(_A)
_ZyTransceiverDdmiType_Type=Integer32
_ZyTransceiverDdmiType_Object=MibTableColumn
zyTransceiverDdmiType=_ZyTransceiverDdmiType_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1,1),_ZyTransceiverDdmiType_Type())
zyTransceiverDdmiType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverDdmiType.setStatus(_A)
_ZyTransceiverDdmiAlarmMax_Type=Integer32
_ZyTransceiverDdmiAlarmMax_Object=MibTableColumn
zyTransceiverDdmiAlarmMax=_ZyTransceiverDdmiAlarmMax_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1,2),_ZyTransceiverDdmiAlarmMax_Type())
zyTransceiverDdmiAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverDdmiAlarmMax.setStatus(_A)
_ZyTransceiverDdmiAlarmMin_Type=Integer32
_ZyTransceiverDdmiAlarmMin_Object=MibTableColumn
zyTransceiverDdmiAlarmMin=_ZyTransceiverDdmiAlarmMin_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1,3),_ZyTransceiverDdmiAlarmMin_Type())
zyTransceiverDdmiAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverDdmiAlarmMin.setStatus(_A)
_ZyTransceiverDdmiWarnMax_Type=Integer32
_ZyTransceiverDdmiWarnMax_Object=MibTableColumn
zyTransceiverDdmiWarnMax=_ZyTransceiverDdmiWarnMax_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1,4),_ZyTransceiverDdmiWarnMax_Type())
zyTransceiverDdmiWarnMax.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverDdmiWarnMax.setStatus(_A)
_ZyTransceiverDdmiWarnMin_Type=Integer32
_ZyTransceiverDdmiWarnMin_Object=MibTableColumn
zyTransceiverDdmiWarnMin=_ZyTransceiverDdmiWarnMin_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1,5),_ZyTransceiverDdmiWarnMin_Type())
zyTransceiverDdmiWarnMin.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverDdmiWarnMin.setStatus(_A)
_ZyTransceiverDdmiCurrent_Type=Integer32
_ZyTransceiverDdmiCurrent_Object=MibTableColumn
zyTransceiverDdmiCurrent=_ZyTransceiverDdmiCurrent_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1,6),_ZyTransceiverDdmiCurrent_Type())
zyTransceiverDdmiCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverDdmiCurrent.setStatus(_A)
_ZyTransceiverDdmiDescription_Type=DisplayString
_ZyTransceiverDdmiDescription_Object=MibTableColumn
zyTransceiverDdmiDescription=_ZyTransceiverDdmiDescription_Object((1,3,6,1,4,1,890,1,15,3,84,1,2,1,7),_ZyTransceiverDdmiDescription_Type())
zyTransceiverDdmiDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTransceiverDdmiDescription.setStatus(_A)
_ZyxelTransceiverTrapInfoObject_ObjectIdentity=ObjectIdentity
zyxelTransceiverTrapInfoObject=_ZyxelTransceiverTrapInfoObject_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,84,2))
class _ZyTransceiverTrapOutOfRangeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('alarmHigh',0),('warnHigh',1),('alarmLow',2),('warnLow',3)))
_ZyTransceiverTrapOutOfRangeType_Type.__name__=_I
_ZyTransceiverTrapOutOfRangeType_Object=MibScalar
zyTransceiverTrapOutOfRangeType=_ZyTransceiverTrapOutOfRangeType_Object((1,3,6,1,4,1,890,1,15,3,84,2,1),_ZyTransceiverTrapOutOfRangeType_Type())
zyTransceiverTrapOutOfRangeType.setMaxAccess(_K)
if mibBuilder.loadTexts:zyTransceiverTrapOutOfRangeType.setStatus(_A)
_ZyTransceiverTrapOutOfRangeValue_Type=Integer32
_ZyTransceiverTrapOutOfRangeValue_Object=MibScalar
zyTransceiverTrapOutOfRangeValue=_ZyTransceiverTrapOutOfRangeValue_Object((1,3,6,1,4,1,890,1,15,3,84,2,2),_ZyTransceiverTrapOutOfRangeValue_Type())
zyTransceiverTrapOutOfRangeValue.setMaxAccess(_K)
if mibBuilder.loadTexts:zyTransceiverTrapOutOfRangeValue.setStatus(_A)
_ZyxelTransceiverNotifications_ObjectIdentity=ObjectIdentity
zyxelTransceiverNotifications=_ZyxelTransceiverNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,84,3))
zyTransceiverDdmiTemperatureOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,1))
zyTransceiverDdmiTemperatureOutOfRange.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiTemperatureOutOfRange.setStatus(_A)
zyTransceiverDdmiTxPowerOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,2))
zyTransceiverDdmiTxPowerOutOfRange.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiTxPowerOutOfRange.setStatus(_A)
zyTransceiverDdmiRxPowerOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,3))
zyTransceiverDdmiRxPowerOutOfRange.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiRxPowerOutOfRange.setStatus(_A)
zyTransceiverDdmiVoltageOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,4))
zyTransceiverDdmiVoltageOutOfRange.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiVoltageOutOfRange.setStatus(_A)
zyTransceiverDdmiTxBiasOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,5))
zyTransceiverDdmiTxBiasOutOfRange.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiTxBiasOutOfRange.setStatus(_A)
zyTransceiverDdmiTemperatureOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,6))
zyTransceiverDdmiTemperatureOutOfRangeRecovered.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiTemperatureOutOfRangeRecovered.setStatus(_A)
zyTransceiverDdmiTxPowerOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,7))
zyTransceiverDdmiTxPowerOutOfRangeRecovered.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiTxPowerOutOfRangeRecovered.setStatus(_A)
zyTransceiverDdmiRxPowerOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,8))
zyTransceiverDdmiRxPowerOutOfRangeRecovered.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiRxPowerOutOfRangeRecovered.setStatus(_A)
zyTransceiverDdmiVoltageOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,9))
zyTransceiverDdmiVoltageOutOfRangeRecovered.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiVoltageOutOfRangeRecovered.setStatus(_A)
zyTransceiverDdmiTxBiasOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,84,3,10))
zyTransceiverDdmiTxBiasOutOfRangeRecovered.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:zyTransceiverDdmiTxBiasOutOfRangeRecovered.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelTransceiver':zyxelTransceiver,'zyxelTransceiverStatus':zyxelTransceiverStatus,'zyxelTransceiverSerialTable':zyxelTransceiverSerialTable,'zyxelTransceiverSerialEntry':zyxelTransceiverSerialEntry,'zyTransceiverSerialModuleType':zyTransceiverSerialModuleType,'zyTransceiverSerialVendor':zyTransceiverSerialVendor,'zyTransceiverSerialPartNumber':zyTransceiverSerialPartNumber,'zyTransceiverSerialSerialNumber':zyTransceiverSerialSerialNumber,'zyTransceiverSerialRevision':zyTransceiverSerialRevision,'zyTransceiverSerialDateCode':zyTransceiverSerialDateCode,'zyTransceiverSerialTransceiver':zyTransceiverSerialTransceiver,'zyxelTransceiverDdmiTable':zyxelTransceiverDdmiTable,'zyxelTransceiverDdmiEntry':zyxelTransceiverDdmiEntry,_J:zyTransceiverDdmiType,'zyTransceiverDdmiAlarmMax':zyTransceiverDdmiAlarmMax,'zyTransceiverDdmiAlarmMin':zyTransceiverDdmiAlarmMin,'zyTransceiverDdmiWarnMax':zyTransceiverDdmiWarnMax,'zyTransceiverDdmiWarnMin':zyTransceiverDdmiWarnMin,'zyTransceiverDdmiCurrent':zyTransceiverDdmiCurrent,'zyTransceiverDdmiDescription':zyTransceiverDdmiDescription,'zyxelTransceiverTrapInfoObject':zyxelTransceiverTrapInfoObject,_F:zyTransceiverTrapOutOfRangeType,'zyTransceiverTrapOutOfRangeValue':zyTransceiverTrapOutOfRangeValue,'zyxelTransceiverNotifications':zyxelTransceiverNotifications,'zyTransceiverDdmiTemperatureOutOfRange':zyTransceiverDdmiTemperatureOutOfRange,'zyTransceiverDdmiTxPowerOutOfRange':zyTransceiverDdmiTxPowerOutOfRange,'zyTransceiverDdmiRxPowerOutOfRange':zyTransceiverDdmiRxPowerOutOfRange,'zyTransceiverDdmiVoltageOutOfRange':zyTransceiverDdmiVoltageOutOfRange,'zyTransceiverDdmiTxBiasOutOfRange':zyTransceiverDdmiTxBiasOutOfRange,'zyTransceiverDdmiTemperatureOutOfRangeRecovered':zyTransceiverDdmiTemperatureOutOfRangeRecovered,'zyTransceiverDdmiTxPowerOutOfRangeRecovered':zyTransceiverDdmiTxPowerOutOfRangeRecovered,'zyTransceiverDdmiRxPowerOutOfRangeRecovered':zyTransceiverDdmiRxPowerOutOfRangeRecovered,'zyTransceiverDdmiVoltageOutOfRangeRecovered':zyTransceiverDdmiVoltageOutOfRangeRecovered,'zyTransceiverDdmiTxBiasOutOfRangeRecovered':zyTransceiverDdmiTxBiasOutOfRangeRecovered})