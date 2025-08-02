_D='Integer32'
_C='DisplayString'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ahProduct,=mibBuilder.importSymbols('AH-SMI-MIB','ahProduct')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
ahSystem=ModuleIdentity((1,3,6,1,4,1,26928,1,2))
class _AhSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AhSystemName_Type.__name__=_C
_AhSystemName_Object=MibScalar
ahSystemName=_AhSystemName_Object((1,3,6,1,4,1,26928,1,2,1),_AhSystemName_Type())
ahSystemName.setMaxAccess(_A)
if mibBuilder.loadTexts:ahSystemName.setStatus(_B)
class _AhSystemDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AhSystemDescription_Type.__name__=_C
_AhSystemDescription_Object=MibScalar
ahSystemDescription=_AhSystemDescription_Object((1,3,6,1,4,1,26928,1,2,2),_AhSystemDescription_Type())
ahSystemDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:ahSystemDescription.setStatus(_B)
class _AhCpuUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AhCpuUtilization_Type.__name__=_D
_AhCpuUtilization_Object=MibScalar
ahCpuUtilization=_AhCpuUtilization_Object((1,3,6,1,4,1,26928,1,2,3),_AhCpuUtilization_Type())
ahCpuUtilization.setMaxAccess(_A)
if mibBuilder.loadTexts:ahCpuUtilization.setStatus(_B)
class _AhMemUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AhMemUtilization_Type.__name__=_D
_AhMemUtilization_Object=MibScalar
ahMemUtilization=_AhMemUtilization_Object((1,3,6,1,4,1,26928,1,2,4),_AhMemUtilization_Type())
ahMemUtilization.setMaxAccess(_A)
if mibBuilder.loadTexts:ahMemUtilization.setStatus(_B)
class _AhSystemSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AhSystemSerial_Type.__name__=_C
_AhSystemSerial_Object=MibScalar
ahSystemSerial=_AhSystemSerial_Object((1,3,6,1,4,1,26928,1,2,5),_AhSystemSerial_Type())
ahSystemSerial.setMaxAccess(_A)
if mibBuilder.loadTexts:ahSystemSerial.setStatus(_B)
class _AhDeviceMode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AhDeviceMode_Type.__name__=_C
_AhDeviceMode_Object=MibScalar
ahDeviceMode=_AhDeviceMode_Object((1,3,6,1,4,1,26928,1,2,6),_AhDeviceMode_Type())
ahDeviceMode.setMaxAccess(_A)
if mibBuilder.loadTexts:ahDeviceMode.setStatus(_B)
class _AhUpTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AhUpTime_Type.__name__=_C
_AhUpTime_Object=MibScalar
ahUpTime=_AhUpTime_Object((1,3,6,1,4,1,26928,1,2,7),_AhUpTime_Type())
ahUpTime.setMaxAccess(_A)
if mibBuilder.loadTexts:ahUpTime.setStatus(_B)
class _AhHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AhHwVersion_Type.__name__=_C
_AhHwVersion_Object=MibScalar
ahHwVersion=_AhHwVersion_Object((1,3,6,1,4,1,26928,1,2,8),_AhHwVersion_Type())
ahHwVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:ahHwVersion.setStatus(_B)
class _AhClientCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_AhClientCount_Type.__name__=_D
_AhClientCount_Object=MibScalar
ahClientCount=_AhClientCount_Object((1,3,6,1,4,1,26928,1,2,9),_AhClientCount_Type())
ahClientCount.setMaxAccess(_A)
if mibBuilder.loadTexts:ahClientCount.setStatus(_B)
class _AhEnvirmentTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AhEnvirmentTemp_Type.__name__=_D
_AhEnvirmentTemp_Object=MibScalar
ahEnvirmentTemp=_AhEnvirmentTemp_Object((1,3,6,1,4,1,26928,1,2,10),_AhEnvirmentTemp_Type())
ahEnvirmentTemp.setMaxAccess(_A)
if mibBuilder.loadTexts:ahEnvirmentTemp.setStatus(_B)
class _AhEnvirmentFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_AhEnvirmentFan_Type.__name__=_D
_AhEnvirmentFan_Object=MibScalar
ahEnvirmentFan=_AhEnvirmentFan_Object((1,3,6,1,4,1,26928,1,2,11),_AhEnvirmentFan_Type())
ahEnvirmentFan.setMaxAccess(_A)
if mibBuilder.loadTexts:ahEnvirmentFan.setStatus(_B)
class _AhFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AhFirmwareVersion_Type.__name__=_C
_AhFirmwareVersion_Object=MibScalar
ahFirmwareVersion=_AhFirmwareVersion_Object((1,3,6,1,4,1,26928,1,2,12),_AhFirmwareVersion_Type())
ahFirmwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:ahFirmwareVersion.setStatus(_B)
mibBuilder.exportSymbols('AH-SYSTEM-MIB',**{'ahSystem':ahSystem,'ahSystemName':ahSystemName,'ahSystemDescription':ahSystemDescription,'ahCpuUtilization':ahCpuUtilization,'ahMemUtilization':ahMemUtilization,'ahSystemSerial':ahSystemSerial,'ahDeviceMode':ahDeviceMode,'ahUpTime':ahUpTime,'ahHwVersion':ahHwVersion,'ahClientCount':ahClientCount,'ahEnvirmentTemp':ahEnvirmentTemp,'ahEnvirmentFan':ahEnvirmentFan,'ahFirmwareVersion':ahFirmwareVersion})