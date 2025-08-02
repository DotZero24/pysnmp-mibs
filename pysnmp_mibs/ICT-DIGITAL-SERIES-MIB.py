_D='NotificationType'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_IctPower_ObjectIdentity=ObjectIdentity
ictPower=_IctPower_ObjectIdentity((1,3,6,1,4,1,39145))
_DigitalSeries_ObjectIdentity=ObjectIdentity
digitalSeries=_DigitalSeries_ObjectIdentity((1,3,6,1,4,1,39145,11))
_DeviceModel_Type=DisplayString
_DeviceModel_Object=MibScalar
deviceModel=_DeviceModel_Object((1,3,6,1,4,1,39145,11,1),_DeviceModel_Type())
deviceModel.setMaxAccess(_A)
if mibBuilder.loadTexts:deviceModel.setStatus(_B)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,39145,11,2),_DeviceName_Type())
deviceName.setMaxAccess(_A)
if mibBuilder.loadTexts:deviceName.setStatus(_B)
class _DeviceHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_DeviceHardware_Type.__name__=_C
_DeviceHardware_Object=MibScalar
deviceHardware=_DeviceHardware_Object((1,3,6,1,4,1,39145,11,3),_DeviceHardware_Type())
deviceHardware.setMaxAccess(_A)
if mibBuilder.loadTexts:deviceHardware.setStatus(_B)
_DeviceFirmware_Type=DisplayString
_DeviceFirmware_Object=MibScalar
deviceFirmware=_DeviceFirmware_Object((1,3,6,1,4,1,39145,11,4),_DeviceFirmware_Type())
deviceFirmware.setMaxAccess(_A)
if mibBuilder.loadTexts:deviceFirmware.setStatus(_B)
_DeviceMacAddress_Type=DisplayString
_DeviceMacAddress_Object=MibScalar
deviceMacAddress=_DeviceMacAddress_Object((1,3,6,1,4,1,39145,11,5),_DeviceMacAddress_Type())
deviceMacAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:deviceMacAddress.setStatus(_B)
_InputVoltage_Type=DisplayString
_InputVoltage_Object=MibScalar
inputVoltage=_InputVoltage_Object((1,3,6,1,4,1,39145,11,6),_InputVoltage_Type())
inputVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:inputVoltage.setStatus(_B)
_OutputVoltage_Type=DisplayString
_OutputVoltage_Object=MibScalar
outputVoltage=_OutputVoltage_Object((1,3,6,1,4,1,39145,11,7),_OutputVoltage_Type())
outputVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:outputVoltage.setStatus(_B)
_OutputCurrent_Type=DisplayString
_OutputCurrent_Object=MibScalar
outputCurrent=_OutputCurrent_Object((1,3,6,1,4,1,39145,11,8),_OutputCurrent_Type())
outputCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:outputCurrent.setStatus(_B)
class _OutputEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ENABLED',1),('DISABLED',2)))
_OutputEnable_Type.__name__=_C
_OutputEnable_Object=MibScalar
outputEnable=_OutputEnable_Object((1,3,6,1,4,1,39145,11,9),_OutputEnable_Type())
outputEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:outputEnable.setStatus(_B)
mibBuilder.exportSymbols('ICT-DIGITAL-SERIES-MIB',**{'ictPower':ictPower,'digitalSeries':digitalSeries,'deviceModel':deviceModel,'deviceName':deviceName,'deviceHardware':deviceHardware,'deviceFirmware':deviceFirmware,'deviceMacAddress':deviceMacAddress,'inputVoltage':inputVoltage,'outputVoltage':outputVoltage,'outputCurrent':outputCurrent,'outputEnable':outputEnable})