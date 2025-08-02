_AO='halfduplex'
_AN='fullduplex'
_AM='dedicated'
_AL='nicNumber'
_AK='nvmeCtrlPresent'
_AJ='vietnamese'
_AI='ukrainian'
_AH='slovenian'
_AG='singhalese'
_AF='serbo-croatian'
_AE='kinyarwanda'
_AD='rhaeto-romance'
_AC='portuguese'
_AB='norwegian'
_AA='moldavian'
_A9='mongolian'
_A8='malayalam'
_A7='macedonian'
_A6='lithuanian'
_A5='cambodian'
_A4='greenlandic'
_A3='icelandic'
_A2='indonesian'
_A1='interlingue'
_A0='interlingua'
_z='armenian'
_y='hungarian'
_x='croatian'
_w='gujarati'
_v='guarani'
_u='galician'
_t='gaelic'
_s='frisian'
_r='french'
_q='faeroese'
_p='finnish'
_o='persian'
_n='basque'
_m='estonian'
_l='spanish'
_k='esperanto'
_j='english'
_i='bhutani'
_h='german'
_g='danish'
_f='corsican'
_e='catalan'
_d='breton'
_c='tibetan'
_b='bengali'
_a='bislama'
_Z='bihari'
_Y='bulgarian'
_X='byelorussian'
_W='bashkir'
_V='azerbaijani'
_U='aymara'
_T='assamese'
_S='arabic'
_R='amharic'
_Q='afrikaans'
_P='abkhazian'
_O='psuIndex'
_N='volNumber'
_M='hddNumber'
_L='controllerNumber'
_K='dimmNumber'
_J='cpuNumber'
_I='sensorNumber'
_H='enabled'
_G='disabled'
_F='read-write'
_E='ATEN-IPMI-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
aten=ModuleIdentity((1,3,6,1,4,1,21317))
if mibBuilder.loadTexts:aten.setRevisions(('2009-03-20 11:50',))
_Ipmi_ObjectIdentity=ObjectIdentity
ipmi=_Ipmi_ObjectIdentity((1,3,6,1,4,1,21317,1))
_Sel_Type=Integer32
_Sel_Object=MibScalar
sel=_Sel_Object((1,3,6,1,4,1,21317,1,2),_Sel_Type())
sel.setMaxAccess(_F)
if mibBuilder.loadTexts:sel.setStatus(_A)
_SensorTable_Object=MibTable
sensorTable=_SensorTable_Object((1,3,6,1,4,1,21317,1,3))
if mibBuilder.loadTexts:sensorTable.setStatus(_A)
_SensorEntry_Object=MibTableRow
sensorEntry=_SensorEntry_Object((1,3,6,1,4,1,21317,1,3,1))
sensorEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:sensorEntry.setStatus(_A)
class _SensorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SensorNumber_Type.__name__=_C
_SensorNumber_Object=MibTableColumn
sensorNumber=_SensorNumber_Object((1,3,6,1,4,1,21317,1,3,1,1),_SensorNumber_Type())
sensorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorNumber.setStatus(_A)
class _SensorReading_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SensorReading_Type.__name__=_D
_SensorReading_Object=MibTableColumn
sensorReading=_SensorReading_Object((1,3,6,1,4,1,21317,1,3,1,2),_SensorReading_Type())
sensorReading.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorReading.setStatus(_A)
_SensorPositiveHysteresis_Type=Integer32
_SensorPositiveHysteresis_Object=MibTableColumn
sensorPositiveHysteresis=_SensorPositiveHysteresis_Object((1,3,6,1,4,1,21317,1,3,1,3),_SensorPositiveHysteresis_Type())
sensorPositiveHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorPositiveHysteresis.setStatus(_A)
_SensorNegativeHysteresis_Type=Integer32
_SensorNegativeHysteresis_Object=MibTableColumn
sensorNegativeHysteresis=_SensorNegativeHysteresis_Object((1,3,6,1,4,1,21317,1,3,1,4),_SensorNegativeHysteresis_Type())
sensorNegativeHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorNegativeHysteresis.setStatus(_A)
class _LncThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_LncThreshold_Type.__name__=_D
_LncThreshold_Object=MibTableColumn
lncThreshold=_LncThreshold_Object((1,3,6,1,4,1,21317,1,3,1,5),_LncThreshold_Type())
lncThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:lncThreshold.setStatus(_A)
class _LcThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_LcThreshold_Type.__name__=_D
_LcThreshold_Object=MibTableColumn
lcThreshold=_LcThreshold_Object((1,3,6,1,4,1,21317,1,3,1,6),_LcThreshold_Type())
lcThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:lcThreshold.setStatus(_A)
class _LnrThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_LnrThreshold_Type.__name__=_D
_LnrThreshold_Object=MibTableColumn
lnrThreshold=_LnrThreshold_Object((1,3,6,1,4,1,21317,1,3,1,7),_LnrThreshold_Type())
lnrThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:lnrThreshold.setStatus(_A)
class _UncThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_UncThreshold_Type.__name__=_D
_UncThreshold_Object=MibTableColumn
uncThreshold=_UncThreshold_Object((1,3,6,1,4,1,21317,1,3,1,8),_UncThreshold_Type())
uncThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:uncThreshold.setStatus(_A)
class _UcThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_UcThreshold_Type.__name__=_D
_UcThreshold_Object=MibTableColumn
ucThreshold=_UcThreshold_Object((1,3,6,1,4,1,21317,1,3,1,9),_UcThreshold_Type())
ucThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:ucThreshold.setStatus(_A)
class _UnrThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_UnrThreshold_Type.__name__=_D
_UnrThreshold_Object=MibTableColumn
unrThreshold=_UnrThreshold_Object((1,3,6,1,4,1,21317,1,3,1,10),_UnrThreshold_Type())
unrThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:unrThreshold.setStatus(_A)
_EventAssertionEnable_Type=Integer32
_EventAssertionEnable_Object=MibTableColumn
eventAssertionEnable=_EventAssertionEnable_Object((1,3,6,1,4,1,21317,1,3,1,11),_EventAssertionEnable_Type())
eventAssertionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eventAssertionEnable.setStatus(_A)
_EventDeassertionEnable_Type=Integer32
_EventDeassertionEnable_Object=MibTableColumn
eventDeassertionEnable=_EventDeassertionEnable_Object((1,3,6,1,4,1,21317,1,3,1,12),_EventDeassertionEnable_Type())
eventDeassertionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eventDeassertionEnable.setStatus(_A)
class _SensorIDString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SensorIDString_Type.__name__=_D
_SensorIDString_Object=MibTableColumn
sensorIDString=_SensorIDString_Object((1,3,6,1,4,1,21317,1,3,1,13),_SensorIDString_Type())
sensorIDString.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorIDString.setStatus(_A)
class _PowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('poweroff',0),('poweron',1)))
_PowerStatus_Type.__name__=_C
_PowerStatus_Object=MibScalar
powerStatus=_PowerStatus_Object((1,3,6,1,4,1,21317,1,4),_PowerStatus_Type())
powerStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:powerStatus.setStatus(_A)
_Boardinfo_ObjectIdentity=ObjectIdentity
boardinfo=_Boardinfo_ObjectIdentity((1,3,6,1,4,1,21317,1,5))
class _BmcMajorVesion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BmcMajorVesion_Type.__name__=_C
_BmcMajorVesion_Object=MibScalar
bmcMajorVesion=_BmcMajorVesion_Object((1,3,6,1,4,1,21317,1,5,1),_BmcMajorVesion_Type())
bmcMajorVesion.setMaxAccess(_B)
if mibBuilder.loadTexts:bmcMajorVesion.setStatus(_A)
class _BmcMinorVesion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BmcMinorVesion_Type.__name__=_C
_BmcMinorVesion_Object=MibScalar
bmcMinorVesion=_BmcMinorVesion_Object((1,3,6,1,4,1,21317,1,5,2),_BmcMinorVesion_Type())
bmcMinorVesion.setMaxAccess(_B)
if mibBuilder.loadTexts:bmcMinorVesion.setStatus(_A)
class _BmcBuildDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_BmcBuildDate_Type.__name__=_D
_BmcBuildDate_Object=MibScalar
bmcBuildDate=_BmcBuildDate_Object((1,3,6,1,4,1,21317,1,5,3),_BmcBuildDate_Type())
bmcBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:bmcBuildDate.setStatus(_A)
class _BiosVesion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_BiosVesion_Type.__name__=_D
_BiosVesion_Object=MibScalar
biosVesion=_BiosVesion_Object((1,3,6,1,4,1,21317,1,5,4),_BiosVesion_Type())
biosVesion.setMaxAccess(_B)
if mibBuilder.loadTexts:biosVesion.setStatus(_A)
class _BiosBuildDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_BiosBuildDate_Type.__name__=_D
_BiosBuildDate_Object=MibScalar
biosBuildDate=_BiosBuildDate_Object((1,3,6,1,4,1,21317,1,5,5),_BiosBuildDate_Type())
biosBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:biosBuildDate.setStatus(_A)
class _HostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_HostName_Type.__name__=_D
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,21317,1,5,6),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
class _BmcBuildVesion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BmcBuildVesion_Type.__name__=_C
_BmcBuildVesion_Object=MibScalar
bmcBuildVesion=_BmcBuildVesion_Object((1,3,6,1,4,1,21317,1,5,7),_BmcBuildVesion_Type())
bmcBuildVesion.setMaxAccess(_B)
if mibBuilder.loadTexts:bmcBuildVesion.setStatus(_A)
_Hardwareinfo_ObjectIdentity=ObjectIdentity
hardwareinfo=_Hardwareinfo_ObjectIdentity((1,3,6,1,4,1,21317,1,6))
class _SerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SerialNumber_Type.__name__=_D
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,21317,1,6,1),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_CpuTable_Object=MibTable
cpuTable=_CpuTable_Object((1,3,6,1,4,1,21317,1,6,2))
if mibBuilder.loadTexts:cpuTable.setStatus(_A)
_CpuEntry_Object=MibTableRow
cpuEntry=_CpuEntry_Object((1,3,6,1,4,1,21317,1,6,2,1))
cpuEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:cpuEntry.setStatus(_A)
class _CpuNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CpuNumber_Type.__name__=_C
_CpuNumber_Object=MibTableColumn
cpuNumber=_CpuNumber_Object((1,3,6,1,4,1,21317,1,6,2,1,1),_CpuNumber_Type())
cpuNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuNumber.setStatus(_A)
class _Processor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_Processor_Type.__name__=_D
_Processor_Object=MibTableColumn
processor=_Processor_Object((1,3,6,1,4,1,21317,1,6,2,1,2),_Processor_Type())
processor.setMaxAccess(_B)
if mibBuilder.loadTexts:processor.setStatus(_A)
class _Speed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Speed_Type.__name__=_C
_Speed_Object=MibTableColumn
speed=_Speed_Object((1,3,6,1,4,1,21317,1,6,2,1,3),_Speed_Type())
speed.setMaxAccess(_B)
if mibBuilder.loadTexts:speed.setStatus(_A)
class _Core_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Core_Type.__name__=_C
_Core_Object=MibTableColumn
core=_Core_Object((1,3,6,1,4,1,21317,1,6,2,1,4),_Core_Type())
core.setMaxAccess(_B)
if mibBuilder.loadTexts:core.setStatus(_A)
class _CoreActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoreActive_Type.__name__=_C
_CoreActive_Object=MibTableColumn
coreActive=_CoreActive_Object((1,3,6,1,4,1,21317,1,6,2,1,5),_CoreActive_Type())
coreActive.setMaxAccess(_B)
if mibBuilder.loadTexts:coreActive.setStatus(_A)
class _Manufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_Manufacturer_Type.__name__=_D
_Manufacturer_Object=MibTableColumn
manufacturer=_Manufacturer_Object((1,3,6,1,4,1,21317,1,6,2,1,6),_Manufacturer_Type())
manufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:manufacturer.setStatus(_A)
_DimmTable_Object=MibTable
dimmTable=_DimmTable_Object((1,3,6,1,4,1,21317,1,6,3))
if mibBuilder.loadTexts:dimmTable.setStatus(_A)
_DimmEntry_Object=MibTableRow
dimmEntry=_DimmEntry_Object((1,3,6,1,4,1,21317,1,6,3,1))
dimmEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:dimmEntry.setStatus(_A)
class _DimmNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DimmNumber_Type.__name__=_C
_DimmNumber_Object=MibTableColumn
dimmNumber=_DimmNumber_Object((1,3,6,1,4,1,21317,1,6,3,1,1),_DimmNumber_Type())
dimmNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmNumber.setStatus(_A)
class _DimmLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_DimmLocation_Type.__name__=_D
_DimmLocation_Object=MibTableColumn
dimmLocation=_DimmLocation_Object((1,3,6,1,4,1,21317,1,6,3,1,2),_DimmLocation_Type())
dimmLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmLocation.setStatus(_A)
class _DimmMaxCapSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DimmMaxCapSpeed_Type.__name__=_C
_DimmMaxCapSpeed_Object=MibTableColumn
dimmMaxCapSpeed=_DimmMaxCapSpeed_Object((1,3,6,1,4,1,21317,1,6,3,1,3),_DimmMaxCapSpeed_Type())
dimmMaxCapSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmMaxCapSpeed.setStatus(_A)
class _DimmOpSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DimmOpSpeed_Type.__name__=_C
_DimmOpSpeed_Object=MibTableColumn
dimmOpSpeed=_DimmOpSpeed_Object((1,3,6,1,4,1,21317,1,6,3,1,4),_DimmOpSpeed_Type())
dimmOpSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmOpSpeed.setStatus(_A)
class _DimmSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DimmSize_Type.__name__=_C
_DimmSize_Object=MibTableColumn
dimmSize=_DimmSize_Object((1,3,6,1,4,1,21317,1,6,3,1,5),_DimmSize_Type())
dimmSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmSize.setStatus(_A)
class _DimmSerialNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_DimmSerialNo_Type.__name__=_D
_DimmSerialNo_Object=MibTableColumn
dimmSerialNo=_DimmSerialNo_Object((1,3,6,1,4,1,21317,1,6,3,1,6),_DimmSerialNo_Type())
dimmSerialNo.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmSerialNo.setStatus(_A)
class _DimmPartNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_DimmPartNo_Type.__name__=_D
_DimmPartNo_Object=MibTableColumn
dimmPartNo=_DimmPartNo_Object((1,3,6,1,4,1,21317,1,6,3,1,7),_DimmPartNo_Type())
dimmPartNo.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmPartNo.setStatus(_A)
class _DimmManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_DimmManufacturer_Type.__name__=_D
_DimmManufacturer_Object=MibTableColumn
dimmManufacturer=_DimmManufacturer_Object((1,3,6,1,4,1,21317,1,6,3,1,8),_DimmManufacturer_Type())
dimmManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:dimmManufacturer.setStatus(_A)
_Storage_ObjectIdentity=ObjectIdentity
storage=_Storage_ObjectIdentity((1,3,6,1,4,1,21317,1,7))
_ControllerTable_Object=MibTable
controllerTable=_ControllerTable_Object((1,3,6,1,4,1,21317,1,7,1))
if mibBuilder.loadTexts:controllerTable.setStatus(_A)
_ControllerEntry_Object=MibTableRow
controllerEntry=_ControllerEntry_Object((1,3,6,1,4,1,21317,1,7,1,1))
controllerEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:controllerEntry.setStatus(_A)
class _ControllerNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ControllerNumber_Type.__name__=_C
_ControllerNumber_Object=MibTableColumn
controllerNumber=_ControllerNumber_Object((1,3,6,1,4,1,21317,1,7,1,1,1),_ControllerNumber_Type())
controllerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:controllerNumber.setStatus(_A)
class _ControllerProductName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(96,96));fixedLength=96
_ControllerProductName_Type.__name__=_D
_ControllerProductName_Object=MibTableColumn
controllerProductName=_ControllerProductName_Object((1,3,6,1,4,1,21317,1,7,1,1,2),_ControllerProductName_Type())
controllerProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:controllerProductName.setStatus(_A)
class _Serial_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_Serial_Type.__name__=_D
_Serial_Object=MibTableColumn
serial=_Serial_Object((1,3,6,1,4,1,21317,1,7,1,1,3),_Serial_Type())
serial.setMaxAccess(_B)
if mibBuilder.loadTexts:serial.setStatus(_A)
class _Package_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(96,96));fixedLength=96
_Package_Type.__name__=_D
_Package_Object=MibTableColumn
package=_Package_Object((1,3,6,1,4,1,21317,1,7,1,1,4),_Package_Type())
package.setMaxAccess(_B)
if mibBuilder.loadTexts:package.setStatus(_A)
class _FwVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_FwVersion_Type.__name__=_D
_FwVersion_Object=MibTableColumn
fwVersion=_FwVersion_Object((1,3,6,1,4,1,21317,1,7,1,1,5),_FwVersion_Type())
fwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fwVersion.setStatus(_A)
class _BiosVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_BiosVersion_Type.__name__=_D
_BiosVersion_Object=MibTableColumn
biosVersion=_BiosVersion_Object((1,3,6,1,4,1,21317,1,7,1,1,6),_BiosVersion_Type())
biosVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:biosVersion.setStatus(_A)
class _BootBlockVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_BootBlockVersion_Type.__name__=_D
_BootBlockVersion_Object=MibTableColumn
bootBlockVersion=_BootBlockVersion_Object((1,3,6,1,4,1,21317,1,7,1,1,7),_BootBlockVersion_Type())
bootBlockVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bootBlockVersion.setStatus(_A)
class _BatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BatteryStatus_Type.__name__=_C
_BatteryStatus_Object=MibTableColumn
batteryStatus=_BatteryStatus_Object((1,3,6,1,4,1,21317,1,7,1,1,8),_BatteryStatus_Type())
batteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryStatus.setStatus(_A)
class _PcieLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PcieLocation_Type.__name__=_C
_PcieLocation_Object=MibTableColumn
pcieLocation=_PcieLocation_Object((1,3,6,1,4,1,21317,1,7,1,1,9),_PcieLocation_Type())
pcieLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:pcieLocation.setStatus(_A)
class _PcieSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PcieSlot_Type.__name__=_C
_PcieSlot_Object=MibTableColumn
pcieSlot=_PcieSlot_Object((1,3,6,1,4,1,21317,1,7,1,1,10),_PcieSlot_Type())
pcieSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:pcieSlot.setStatus(_A)
_PhyHddTable_Object=MibTable
phyHddTable=_PhyHddTable_Object((1,3,6,1,4,1,21317,1,7,2))
if mibBuilder.loadTexts:phyHddTable.setStatus(_A)
_HddEntry_Object=MibTableRow
hddEntry=_HddEntry_Object((1,3,6,1,4,1,21317,1,7,2,1))
hddEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:hddEntry.setStatus(_A)
class _HddNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HddNumber_Type.__name__=_C
_HddNumber_Object=MibTableColumn
hddNumber=_HddNumber_Object((1,3,6,1,4,1,21317,1,7,2,1,1),_HddNumber_Type())
hddNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hddNumber.setStatus(_A)
class _HddControllerNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HddControllerNumber_Type.__name__=_C
_HddControllerNumber_Object=MibTableColumn
hddControllerNumber=_HddControllerNumber_Object((1,3,6,1,4,1,21317,1,7,2,1,2),_HddControllerNumber_Type())
hddControllerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hddControllerNumber.setStatus(_A)
class _EnclosureNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EnclosureNumber_Type.__name__=_C
_EnclosureNumber_Object=MibTableColumn
enclosureNumber=_EnclosureNumber_Object((1,3,6,1,4,1,21317,1,7,2,1,3),_EnclosureNumber_Type())
enclosureNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureNumber.setStatus(_A)
class _Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Status_Type.__name__=_C
_Status_Object=MibTableColumn
status=_Status_Object((1,3,6,1,4,1,21317,1,7,2,1,4),_Status_Type())
status.setMaxAccess(_B)
if mibBuilder.loadTexts:status.setStatus(_A)
class _Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Temperature_Type.__name__=_C
_Temperature_Object=MibTableColumn
temperature=_Temperature_Object((1,3,6,1,4,1,21317,1,7,2,1,5),_Temperature_Type())
temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature.setStatus(_A)
class _Capacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Capacity_Type.__name__=_C
_Capacity_Object=MibTableColumn
capacity=_Capacity_Object((1,3,6,1,4,1,21317,1,7,2,1,6),_Capacity_Type())
capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:capacity.setStatus(_A)
class _Vendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Vendor_Type.__name__=_D
_Vendor_Object=MibTableColumn
vendor=_Vendor_Object((1,3,6,1,4,1,21317,1,7,2,1,7),_Vendor_Type())
vendor.setMaxAccess(_B)
if mibBuilder.loadTexts:vendor.setStatus(_A)
class _ModelName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ModelName_Type.__name__=_D
_ModelName_Object=MibTableColumn
modelName=_ModelName_Object((1,3,6,1,4,1,21317,1,7,2,1,8),_ModelName_Type())
modelName.setMaxAccess(_B)
if mibBuilder.loadTexts:modelName.setStatus(_A)
class _Revision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Revision_Type.__name__=_D
_Revision_Object=MibTableColumn
revision=_Revision_Object((1,3,6,1,4,1,21317,1,7,2,1,9),_Revision_Type())
revision.setMaxAccess(_B)
if mibBuilder.loadTexts:revision.setStatus(_A)
class _Sn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_Sn_Type.__name__=_D
_Sn_Object=MibTableColumn
sn=_Sn_Object((1,3,6,1,4,1,21317,1,7,2,1,10),_Sn_Type())
sn.setMaxAccess(_B)
if mibBuilder.loadTexts:sn.setStatus(_A)
class _LinkSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LinkSpeed_Type.__name__=_C
_LinkSpeed_Object=MibTableColumn
linkSpeed=_LinkSpeed_Object((1,3,6,1,4,1,21317,1,7,2,1,11),_LinkSpeed_Type())
linkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:linkSpeed.setStatus(_A)
class _FwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FwState_Type.__name__=_C
_FwState_Object=MibTableColumn
fwState=_FwState_Object((1,3,6,1,4,1,21317,1,7,2,1,12),_FwState_Type())
fwState.setMaxAccess(_B)
if mibBuilder.loadTexts:fwState.setStatus(_A)
class _OtherErrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OtherErrCount_Type.__name__=_C
_OtherErrCount_Object=MibTableColumn
otherErrCount=_OtherErrCount_Object((1,3,6,1,4,1,21317,1,7,2,1,13),_OtherErrCount_Type())
otherErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:otherErrCount.setStatus(_A)
class _PredictedFailCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PredictedFailCount_Type.__name__=_C
_PredictedFailCount_Object=MibTableColumn
predictedFailCount=_PredictedFailCount_Object((1,3,6,1,4,1,21317,1,7,2,1,14),_PredictedFailCount_Type())
predictedFailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:predictedFailCount.setStatus(_A)
class _MediaErrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MediaErrCount_Type.__name__=_C
_MediaErrCount_Object=MibTableColumn
mediaErrCount=_MediaErrCount_Object((1,3,6,1,4,1,21317,1,7,2,1,15),_MediaErrCount_Type())
mediaErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaErrCount.setStatus(_A)
_LogHddTable_Object=MibTable
logHddTable=_LogHddTable_Object((1,3,6,1,4,1,21317,1,7,3))
if mibBuilder.loadTexts:logHddTable.setStatus(_A)
_VolumeEntry_Object=MibTableRow
volumeEntry=_VolumeEntry_Object((1,3,6,1,4,1,21317,1,7,3,1))
volumeEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:volumeEntry.setStatus(_A)
class _VolNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VolNumber_Type.__name__=_C
_VolNumber_Object=MibTableColumn
volNumber=_VolNumber_Object((1,3,6,1,4,1,21317,1,7,3,1,1),_VolNumber_Type())
volNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:volNumber.setStatus(_A)
class _VolControllerNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VolControllerNumber_Type.__name__=_C
_VolControllerNumber_Object=MibTableColumn
volControllerNumber=_VolControllerNumber_Object((1,3,6,1,4,1,21317,1,7,3,1,2),_VolControllerNumber_Type())
volControllerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:volControllerNumber.setStatus(_A)
class _VolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VolStatus_Type.__name__=_C
_VolStatus_Object=MibTableColumn
volStatus=_VolStatus_Object((1,3,6,1,4,1,21317,1,7,3,1,3),_VolStatus_Type())
volStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:volStatus.setStatus(_A)
class _VolCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VolCapacity_Type.__name__=_C
_VolCapacity_Object=MibTableColumn
volCapacity=_VolCapacity_Object((1,3,6,1,4,1,21317,1,7,3,1,4),_VolCapacity_Type())
volCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:volCapacity.setStatus(_A)
class _PriRaidLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PriRaidLevel_Type.__name__=_C
_PriRaidLevel_Object=MibTableColumn
priRaidLevel=_PriRaidLevel_Object((1,3,6,1,4,1,21317,1,7,3,1,5),_PriRaidLevel_Type())
priRaidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:priRaidLevel.setStatus(_A)
class _RaidLevelQualifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RaidLevelQualifier_Type.__name__=_C
_RaidLevelQualifier_Object=MibTableColumn
raidLevelQualifier=_RaidLevelQualifier_Object((1,3,6,1,4,1,21317,1,7,3,1,6),_RaidLevelQualifier_Type())
raidLevelQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:raidLevelQualifier.setStatus(_A)
class _SecRaidLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SecRaidLevel_Type.__name__=_C
_SecRaidLevel_Object=MibTableColumn
secRaidLevel=_SecRaidLevel_Object((1,3,6,1,4,1,21317,1,7,3,1,7),_SecRaidLevel_Type())
secRaidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:secRaidLevel.setStatus(_A)
class _LdStripSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LdStripSize_Type.__name__=_C
_LdStripSize_Object=MibTableColumn
ldStripSize=_LdStripSize_Object((1,3,6,1,4,1,21317,1,7,3,1,8),_LdStripSize_Type())
ldStripSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ldStripSize.setStatus(_A)
class _NumDevices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NumDevices_Type.__name__=_C
_NumDevices_Object=MibTableColumn
numDevices=_NumDevices_Object((1,3,6,1,4,1,21317,1,7,3,1,9),_NumDevices_Type())
numDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:numDevices.setStatus(_A)
class _SpanDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SpanDepth_Type.__name__=_C
_SpanDepth_Object=MibTableColumn
spanDepth=_SpanDepth_Object((1,3,6,1,4,1,21317,1,7,3,1,10),_SpanDepth_Type())
spanDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:spanDepth.setStatus(_A)
class _State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_State_Type.__name__=_C
_State_Object=MibTableColumn
state=_State_Object((1,3,6,1,4,1,21317,1,7,3,1,11),_State_Type())
state.setMaxAccess(_B)
if mibBuilder.loadTexts:state.setStatus(_A)
class _VolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_VolName_Type.__name__=_D
_VolName_Object=MibTableColumn
volName=_VolName_Object((1,3,6,1,4,1,21317,1,7,3,1,12),_VolName_Type())
volName.setMaxAccess(_B)
if mibBuilder.loadTexts:volName.setStatus(_A)
class _ColdResetBMC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ColdResetBMC_Type.__name__=_C
_ColdResetBMC_Object=MibScalar
coldResetBMC=_ColdResetBMC_Object((1,3,6,1,4,1,21317,1,8),_ColdResetBMC_Type())
coldResetBMC.setMaxAccess(_F)
if mibBuilder.loadTexts:coldResetBMC.setStatus(_A)
_UserTable_Object=MibTable
userTable=_UserTable_Object((1,3,6,1,4,1,21317,1,9))
if mibBuilder.loadTexts:userTable.setStatus(_A)
_UserInfo_Object=MibTableRow
userInfo=_UserInfo_Object((1,3,6,1,4,1,21317,1,9,1))
userInfo.setIndexNames((0,_E,'id'))
if mibBuilder.loadTexts:userInfo.setStatus(_A)
class _Id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Id_Type.__name__=_C
_Id_Object=MibTableColumn
id=_Id_Object((1,3,6,1,4,1,21317,1,9,1,1),_Id_Type())
id.setMaxAccess(_B)
if mibBuilder.loadTexts:id.setStatus(_A)
class _Username_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Username_Type.__name__=_D
_Username_Object=MibTableColumn
username=_Username_Object((1,3,6,1,4,1,21317,1,9,1,2),_Username_Type())
username.setMaxAccess(_F)
if mibBuilder.loadTexts:username.setStatus(_A)
class _Password_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_Password_Type.__name__=_D
_Password_Object=MibTableColumn
password=_Password_Object((1,3,6,1,4,1,21317,1,9,1,3),_Password_Type())
password.setMaxAccess(_F)
if mibBuilder.loadTexts:password.setStatus(_A)
class _Privilege_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_Privilege_Type.__name__=_C
_Privilege_Object=MibTableColumn
privilege=_Privilege_Object((1,3,6,1,4,1,21317,1,9,1,4),_Privilege_Type())
privilege.setMaxAccess(_F)
if mibBuilder.loadTexts:privilege.setStatus(_A)
class _Uid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Uid_Type.__name__=_C
_Uid_Object=MibScalar
uid=_Uid_Object((1,3,6,1,4,1,21317,1,10),_Uid_Type())
uid.setMaxAccess(_F)
if mibBuilder.loadTexts:uid.setStatus(_A)
_AlertTable_Object=MibTable
alertTable=_AlertTable_Object((1,3,6,1,4,1,21317,1,11))
if mibBuilder.loadTexts:alertTable.setStatus(_A)
_AlertInfo_Object=MibTableRow
alertInfo=_AlertInfo_Object((1,3,6,1,4,1,21317,1,11,1))
alertInfo.setIndexNames((0,_E,'id'))
if mibBuilder.loadTexts:alertInfo.setStatus(_A)
class _AlertNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AlertNo_Type.__name__=_C
_AlertNo_Object=MibTableColumn
alertNo=_AlertNo_Object((1,3,6,1,4,1,21317,1,11,1,1),_AlertNo_Type())
alertNo.setMaxAccess(_B)
if mibBuilder.loadTexts:alertNo.setStatus(_A)
class _AlertLevel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(25,25));fixedLength=25
_AlertLevel_Type.__name__=_D
_AlertLevel_Object=MibTableColumn
alertLevel=_AlertLevel_Object((1,3,6,1,4,1,21317,1,11,1,2),_AlertLevel_Type())
alertLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:alertLevel.setStatus(_A)
class _DestinationAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(270,270));fixedLength=270
_DestinationAddress_Type.__name__=_D
_DestinationAddress_Object=MibTableColumn
destinationAddress=_DestinationAddress_Object((1,3,6,1,4,1,21317,1,11,1,3),_DestinationAddress_Type())
destinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:destinationAddress.setStatus(_A)
_Powerinfo_ObjectIdentity=ObjectIdentity
powerinfo=_Powerinfo_ObjectIdentity((1,3,6,1,4,1,21317,1,14))
class _PsuNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PsuNumber_Type.__name__=_C
_PsuNumber_Object=MibScalar
psuNumber=_PsuNumber_Object((1,3,6,1,4,1,21317,1,14,1),_PsuNumber_Type())
psuNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:psuNumber.setStatus(_A)
_PsuTable_Object=MibTable
psuTable=_PsuTable_Object((1,3,6,1,4,1,21317,1,14,2))
if mibBuilder.loadTexts:psuTable.setStatus(_A)
_PsuEntry_Object=MibTableRow
psuEntry=_PsuEntry_Object((1,3,6,1,4,1,21317,1,14,2,1))
psuEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:psuEntry.setStatus(_A)
class _PsuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PsuIndex_Type.__name__=_C
_PsuIndex_Object=MibTableColumn
psuIndex=_PsuIndex_Object((1,3,6,1,4,1,21317,1,14,2,1,1),_PsuIndex_Type())
psuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:psuIndex.setStatus(_A)
class _PsuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fail',0),('good',1)))
_PsuStatus_Type.__name__=_C
_PsuStatus_Object=MibTableColumn
psuStatus=_PsuStatus_Object((1,3,6,1,4,1,21317,1,14,2,1,2),_PsuStatus_Type())
psuStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:psuStatus.setStatus(_A)
class _InputVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_InputVoltage_Type.__name__=_D
_InputVoltage_Object=MibTableColumn
inputVoltage=_InputVoltage_Object((1,3,6,1,4,1,21317,1,14,2,1,3),_InputVoltage_Type())
inputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:inputVoltage.setStatus(_A)
class _InputCurrent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_InputCurrent_Type.__name__=_D
_InputCurrent_Object=MibTableColumn
inputCurrent=_InputCurrent_Object((1,3,6,1,4,1,21317,1,14,2,1,4),_InputCurrent_Type())
inputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:inputCurrent.setStatus(_A)
class _InputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048576))
_InputPower_Type.__name__=_C
_InputPower_Object=MibTableColumn
inputPower=_InputPower_Object((1,3,6,1,4,1,21317,1,14,2,1,5),_InputPower_Type())
inputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:inputPower.setStatus(_A)
class _OutputVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_OutputVoltage_Type.__name__=_D
_OutputVoltage_Object=MibTableColumn
outputVoltage=_OutputVoltage_Object((1,3,6,1,4,1,21317,1,14,2,1,6),_OutputVoltage_Type())
outputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:outputVoltage.setStatus(_A)
class _OutputCurrent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_OutputCurrent_Type.__name__=_D
_OutputCurrent_Object=MibTableColumn
outputCurrent=_OutputCurrent_Object((1,3,6,1,4,1,21317,1,14,2,1,7),_OutputCurrent_Type())
outputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:outputCurrent.setStatus(_A)
class _OutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048576))
_OutputPower_Type.__name__=_C
_OutputPower_Object=MibTableColumn
outputPower=_OutputPower_Object((1,3,6,1,4,1,21317,1,14,2,1,8),_OutputPower_Type())
outputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:outputPower.setStatus(_A)
class _Temperature1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Temperature1_Type.__name__=_C
_Temperature1_Object=MibTableColumn
temperature1=_Temperature1_Object((1,3,6,1,4,1,21317,1,14,2,1,9),_Temperature1_Type())
temperature1.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature1.setStatus(_A)
class _Temperature2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Temperature2_Type.__name__=_C
_Temperature2_Object=MibTableColumn
temperature2=_Temperature2_Object((1,3,6,1,4,1,21317,1,14,2,1,10),_Temperature2_Type())
temperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature2.setStatus(_A)
class _FanRPM1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanRPM1_Type.__name__=_C
_FanRPM1_Object=MibTableColumn
fanRPM1=_FanRPM1_Object((1,3,6,1,4,1,21317,1,14,2,1,11),_FanRPM1_Type())
fanRPM1.setMaxAccess(_B)
if mibBuilder.loadTexts:fanRPM1.setStatus(_A)
class _FanRPM2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanRPM2_Type.__name__=_C
_FanRPM2_Object=MibTableColumn
fanRPM2=_FanRPM2_Object((1,3,6,1,4,1,21317,1,14,2,1,12),_FanRPM2_Type())
fanRPM2.setMaxAccess(_B)
if mibBuilder.loadTexts:fanRPM2.setStatus(_A)
class _PsuSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_PsuSerialNumber_Type.__name__=_D
_PsuSerialNumber_Object=MibTableColumn
psuSerialNumber=_PsuSerialNumber_Object((1,3,6,1,4,1,21317,1,14,2,1,13),_PsuSerialNumber_Type())
psuSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:psuSerialNumber.setStatus(_A)
class _FanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('standard',0),('fullspeed',1),('optimal',2),('pue2optimal',3),('heavyIO',4)))
_FanMode_Type.__name__=_C
_FanMode_Object=MibScalar
fanMode=_FanMode_Object((1,3,6,1,4,1,21317,1,15),_FanMode_Type())
fanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fanMode.setStatus(_A)
_Fruinfo_ObjectIdentity=ObjectIdentity
fruinfo=_Fruinfo_ObjectIdentity((1,3,6,1,4,1,21317,1,16))
_Chassis_ObjectIdentity=ObjectIdentity
chassis=_Chassis_ObjectIdentity((1,3,6,1,4,1,21317,1,16,1))
_ChassisType_Type=Integer32
_ChassisType_Object=MibScalar
chassisType=_ChassisType_Object((1,3,6,1,4,1,21317,1,16,1,1),_ChassisType_Type())
chassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisType.setStatus(_A)
class _ChassisPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_ChassisPartNumber_Type.__name__=_D
_ChassisPartNumber_Object=MibScalar
chassisPartNumber=_ChassisPartNumber_Object((1,3,6,1,4,1,21317,1,16,1,2),_ChassisPartNumber_Type())
chassisPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPartNumber.setStatus(_A)
class _ChassisSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_ChassisSerialNumber_Type.__name__=_D
_ChassisSerialNumber_Object=MibScalar
chassisSerialNumber=_ChassisSerialNumber_Object((1,3,6,1,4,1,21317,1,16,1,3),_ChassisSerialNumber_Type())
chassisSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSerialNumber.setStatus(_A)
_Board_ObjectIdentity=ObjectIdentity
board=_Board_ObjectIdentity((1,3,6,1,4,1,21317,1,16,2))
class _BoardLanguage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136)));namedValues=NamedValues(*(('afar',1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),('czech',19),('welsh',20),(_g,21),(_h,22),(_i,23),('greek',24),(_j,25),(_k,26),(_l,27),(_m,28),(_n,29),(_o,30),(_p,31),('fiji',32),(_q,33),(_r,34),(_s,35),('irish',36),(_t,37),(_u,38),(_v,39),(_w,40),('hausa',41),('hindi',42),(_x,43),(_y,44),(_z,45),(_A0,46),(_A1,47),('inupiak',48),(_A2,49),(_A3,50),('italian',51),('hebrew',52),('japanese',53),('yiddish',54),('javanese',55),('georgian',56),('kazakh',57),(_A4,58),(_A5,59),('kannada',60),('korean',61),('kashmiri',62),('kurdish',63),('kirghiz',64),('latin',65),('lingala',66),('laothian',67),(_A6,68),('lettish',69),('malagasy',70),('maori',71),(_A7,72),(_A8,73),(_A9,74),(_AA,75),('marathi',76),('malay',77),('maltese',78),('burmese',79),('nauru',80),('nepali',81),('dutch',82),(_AB,83),('occitan',84),('oromo',85),('oriya',86),('punjabi',87),('polish',88),('pushto',89),(_AC,90),('quechua',91),(_AD,92),('kirundi',93),('romanian',94),('russian',95),(_AE,96),('sanskrit',97),('sindhi',98),('sangro',99),(_AF,100),(_AG,101),('slovak',102),(_AH,103),('samoan',104),('shona',105),('somali',106),('albanian',107),('serbian',108),('siswati',109),('sesotho',110),('sudanese',111),('swedish',112),('swahili',113),('tamil',114),('tegulu',115),('tajik',116),('thai',117),('tigrinya',118),('turkmen',119),('tagalog',120),('setswana',121),('tonga',122),('turkish',123),('tsonga',124),('tatar',125),('twi',126),(_AI,127),('urdu',128),('uzbek',129),(_AJ,130),('volapuk',131),('wolof',132),('xhosa',133),('yoruba',134),('chinese',135),('zulu',136)))
_BoardLanguage_Type.__name__=_C
_BoardLanguage_Object=MibScalar
boardLanguage=_BoardLanguage_Object((1,3,6,1,4,1,21317,1,16,2,1),_BoardLanguage_Type())
boardLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:boardLanguage.setStatus(_A)
class _BoardManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_BoardManufacturer_Type.__name__=_D
_BoardManufacturer_Object=MibScalar
boardManufacturer=_BoardManufacturer_Object((1,3,6,1,4,1,21317,1,16,2,2),_BoardManufacturer_Type())
boardManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:boardManufacturer.setStatus(_A)
class _BoardProductName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_BoardProductName_Type.__name__=_D
_BoardProductName_Object=MibScalar
boardProductName=_BoardProductName_Object((1,3,6,1,4,1,21317,1,16,2,3),_BoardProductName_Type())
boardProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:boardProductName.setStatus(_A)
class _BoardSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_BoardSerialNumber_Type.__name__=_D
_BoardSerialNumber_Object=MibScalar
boardSerialNumber=_BoardSerialNumber_Object((1,3,6,1,4,1,21317,1,16,2,4),_BoardSerialNumber_Type())
boardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:boardSerialNumber.setStatus(_A)
class _BoardPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_BoardPartNumber_Type.__name__=_D
_BoardPartNumber_Object=MibScalar
boardPartNumber=_BoardPartNumber_Object((1,3,6,1,4,1,21317,1,16,2,5),_BoardPartNumber_Type())
boardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPartNumber.setStatus(_A)
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,21317,1,16,3))
class _ProductLanguage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136)));namedValues=NamedValues(*(('afar',1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),('czech',19),('welsh',20),(_g,21),(_h,22),(_i,23),('greek',24),(_j,25),(_k,26),(_l,27),(_m,28),(_n,29),(_o,30),(_p,31),('fiji',32),(_q,33),(_r,34),(_s,35),('irish',36),(_t,37),(_u,38),(_v,39),(_w,40),('hausa',41),('hindi',42),(_x,43),(_y,44),(_z,45),(_A0,46),(_A1,47),('inupiak',48),(_A2,49),(_A3,50),('italian',51),('hebrew',52),('japanese',53),('yiddish',54),('javanese',55),('georgian',56),('kazakh',57),(_A4,58),(_A5,59),('kannada',60),('korean',61),('kashmiri',62),('kurdish',63),('kirghiz',64),('latin',65),('lingala',66),('laothian',67),(_A6,68),('lettish',69),('malagasy',70),('maori',71),(_A7,72),(_A8,73),(_A9,74),(_AA,75),('marathi',76),('malay',77),('maltese',78),('burmese',79),('nauru',80),('nepali',81),('dutch',82),(_AB,83),('occitan',84),('oromo',85),('oriya',86),('punjabi',87),('polish',88),('pushto',89),(_AC,90),('quechua',91),(_AD,92),('kirundi',93),('romanian',94),('russian',95),(_AE,96),('sanskrit',97),('sindhi',98),('sangro',99),(_AF,100),(_AG,101),('slovak',102),(_AH,103),('samoan',104),('shona',105),('somali',106),('albanian',107),('serbian',108),('siswati',109),('sesotho',110),('sudanese',111),('swedish',112),('swahili',113),('tamil',114),('tegulu',115),('tajik',116),('thai',117),('tigrinya',118),('turkmen',119),('tagalog',120),('setswana',121),('tonga',122),('turkish',123),('tsonga',124),('tatar',125),('twi',126),(_AI,127),('urdu',128),('uzbek',129),(_AJ,130),('volapuk',131),('wolof',132),('xhosa',133),('yoruba',134),('chinese',135),('zulu',136)))
_ProductLanguage_Type.__name__=_C
_ProductLanguage_Object=MibScalar
productLanguage=_ProductLanguage_Object((1,3,6,1,4,1,21317,1,16,3,1),_ProductLanguage_Type())
productLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:productLanguage.setStatus(_A)
class _ProductManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_ProductManufacturer_Type.__name__=_D
_ProductManufacturer_Object=MibScalar
productManufacturer=_ProductManufacturer_Object((1,3,6,1,4,1,21317,1,16,3,2),_ProductManufacturer_Type())
productManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:productManufacturer.setStatus(_A)
class _ProductName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_ProductName_Type.__name__=_D
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,21317,1,16,3,3),_ProductName_Type())
productName.setMaxAccess(_B)
if mibBuilder.loadTexts:productName.setStatus(_A)
class _ProductPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_ProductPartNumber_Type.__name__=_D
_ProductPartNumber_Object=MibScalar
productPartNumber=_ProductPartNumber_Object((1,3,6,1,4,1,21317,1,16,3,4),_ProductPartNumber_Type())
productPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:productPartNumber.setStatus(_A)
_ProductVersion_Type=Integer32
_ProductVersion_Object=MibScalar
productVersion=_ProductVersion_Object((1,3,6,1,4,1,21317,1,16,3,5),_ProductVersion_Type())
productVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:productVersion.setStatus(_A)
class _ProductSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_ProductSerialNumber_Type.__name__=_D
_ProductSerialNumber_Object=MibScalar
productSerialNumber=_ProductSerialNumber_Object((1,3,6,1,4,1,21317,1,16,3,6),_ProductSerialNumber_Type())
productSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:productSerialNumber.setStatus(_A)
class _ProductAssetTag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_ProductAssetTag_Type.__name__=_D
_ProductAssetTag_Object=MibScalar
productAssetTag=_ProductAssetTag_Object((1,3,6,1,4,1,21317,1,16,3,7),_ProductAssetTag_Type())
productAssetTag.setMaxAccess(_F)
if mibBuilder.loadTexts:productAssetTag.setStatus(_A)
_Ntpinfo_ObjectIdentity=ObjectIdentity
ntpinfo=_Ntpinfo_ObjectIdentity((1,3,6,1,4,1,21317,1,17))
class _TimeZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_TimeZone_Type.__name__=_D
_TimeZone_Object=MibScalar
timeZone=_TimeZone_Object((1,3,6,1,4,1,21317,1,17,1),_TimeZone_Type())
timeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:timeZone.setStatus(_A)
class _NtpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NtpEnable_Type.__name__=_C
_NtpEnable_Object=MibScalar
ntpEnable=_NtpEnable_Object((1,3,6,1,4,1,21317,1,17,2),_NtpEnable_Type())
ntpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpEnable.setStatus(_A)
class _PrimaryNTPServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(127,127));fixedLength=127
_PrimaryNTPServer_Type.__name__=_D
_PrimaryNTPServer_Object=MibScalar
primaryNTPServer=_PrimaryNTPServer_Object((1,3,6,1,4,1,21317,1,17,3),_PrimaryNTPServer_Type())
primaryNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryNTPServer.setStatus(_A)
class _SecondaryNTPServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(127,127));fixedLength=127
_SecondaryNTPServer_Type.__name__=_D
_SecondaryNTPServer_Object=MibScalar
secondaryNTPServer=_SecondaryNTPServer_Object((1,3,6,1,4,1,21317,1,17,4),_SecondaryNTPServer_Type())
secondaryNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:secondaryNTPServer.setStatus(_A)
class _Dst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Dst_Type.__name__=_C
_Dst_Object=MibScalar
dst=_Dst_Object((1,3,6,1,4,1,21317,1,17,5),_Dst_Type())
dst.setMaxAccess(_B)
if mibBuilder.loadTexts:dst.setStatus(_A)
_SelTable_Object=MibTable
selTable=_SelTable_Object((1,3,6,1,4,1,21317,1,18))
if mibBuilder.loadTexts:selTable.setStatus(_A)
_SelEntry_Object=MibTableRow
selEntry=_SelEntry_Object((1,3,6,1,4,1,21317,1,18,1))
selEntry.setIndexNames((0,_E,'selEid'))
if mibBuilder.loadTexts:selEntry.setStatus(_A)
class _SelEid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_SelEid_Type.__name__=_C
_SelEid_Object=MibTableColumn
selEid=_SelEid_Object((1,3,6,1,4,1,21317,1,18,1,1),_SelEid_Type())
selEid.setMaxAccess(_B)
if mibBuilder.loadTexts:selEid.setStatus(_A)
_SelTimeStamp_Type=DateAndTime
_SelTimeStamp_Object=MibTableColumn
selTimeStamp=_SelTimeStamp_Object((1,3,6,1,4,1,21317,1,18,1,2),_SelTimeStamp_Type())
selTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:selTimeStamp.setStatus(_A)
class _SelSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SelSensorName_Type.__name__=_D
_SelSensorName_Object=MibTableColumn
selSensorName=_SelSensorName_Object((1,3,6,1,4,1,21317,1,18,1,3),_SelSensorName_Type())
selSensorName.setMaxAccess(_B)
if mibBuilder.loadTexts:selSensorName.setStatus(_A)
class _SelSensorType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SelSensorType_Type.__name__=_D
_SelSensorType_Object=MibTableColumn
selSensorType=_SelSensorType_Object((1,3,6,1,4,1,21317,1,18,1,4),_SelSensorType_Type())
selSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:selSensorType.setStatus(_A)
class _SelDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_SelDescription_Type.__name__=_D
_SelDescription_Object=MibTableColumn
selDescription=_SelDescription_Object((1,3,6,1,4,1,21317,1,18,1,5),_SelDescription_Type())
selDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:selDescription.setStatus(_A)
class _SelRawData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_SelRawData_Type.__name__=_D
_SelRawData_Object=MibTableColumn
selRawData=_SelRawData_Object((1,3,6,1,4,1,21317,1,18,1,6),_SelRawData_Type())
selRawData.setMaxAccess(_B)
if mibBuilder.loadTexts:selRawData.setStatus(_A)
_Nvme_ObjectIdentity=ObjectIdentity
nvme=_Nvme_ObjectIdentity((1,3,6,1,4,1,21317,1,19))
_NvmeCtrlTbl_Object=MibTable
nvmeCtrlTbl=_NvmeCtrlTbl_Object((1,3,6,1,4,1,21317,1,19,1))
if mibBuilder.loadTexts:nvmeCtrlTbl.setStatus(_A)
_NvmeCtrlEntry_Object=MibTableRow
nvmeCtrlEntry=_NvmeCtrlEntry_Object((1,3,6,1,4,1,21317,1,19,1,1))
nvmeCtrlEntry.setIndexNames((0,_E,_AK))
if mibBuilder.loadTexts:nvmeCtrlEntry.setStatus(_A)
class _NvmeCtrlPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('absent',0),('present',1)))
_NvmeCtrlPresent_Type.__name__=_C
_NvmeCtrlPresent_Object=MibTableColumn
nvmeCtrlPresent=_NvmeCtrlPresent_Object((1,3,6,1,4,1,21317,1,19,1,1,1),_NvmeCtrlPresent_Type())
nvmeCtrlPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:nvmeCtrlPresent.setStatus(_A)
class _MaxTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_MaxTemp_Type.__name__=_C
_MaxTemp_Object=MibTableColumn
maxTemp=_MaxTemp_Object((1,3,6,1,4,1,21317,1,19,1,1,2),_MaxTemp_Type())
maxTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:maxTemp.setStatus(_A)
class _MaxSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_MaxSlotNum_Type.__name__=_C
_MaxSlotNum_Object=MibTableColumn
maxSlotNum=_MaxSlotNum_Object((1,3,6,1,4,1,21317,1,19,1,1,3),_MaxSlotNum_Type())
maxSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:maxSlotNum.setStatus(_A)
class _Onboard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_Onboard_Type.__name__=_C
_Onboard_Object=MibTableColumn
onboard=_Onboard_Object((1,3,6,1,4,1,21317,1,19,1,1,4),_Onboard_Type())
onboard.setMaxAccess(_B)
if mibBuilder.loadTexts:onboard.setStatus(_A)
class _DriverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_DriverIndex_Type.__name__=_C
_DriverIndex_Object=MibTableColumn
driverIndex=_DriverIndex_Object((1,3,6,1,4,1,21317,1,19,1,1,5),_DriverIndex_Type())
driverIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:driverIndex.setStatus(_A)
class _CpldVer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CpldVer_Type.__name__=_D
_CpldVer_Object=MibTableColumn
cpldVer=_CpldVer_Object((1,3,6,1,4,1,21317,1,19,1,1,6),_CpldVer_Type())
cpldVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cpldVer.setStatus(_A)
_NvmeDriveTbl_Object=MibTable
nvmeDriveTbl=_NvmeDriveTbl_Object((1,3,6,1,4,1,21317,1,19,2))
if mibBuilder.loadTexts:nvmeDriveTbl.setStatus(_A)
_NvmeDriveEntry_Object=MibTableRow
nvmeDriveEntry=_NvmeDriveEntry_Object((1,3,6,1,4,1,21317,1,19,2,1))
nvmeDriveEntry.setIndexNames((0,_E,'slotId'))
if mibBuilder.loadTexts:nvmeDriveEntry.setStatus(_A)
class _SlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_SlotId_Type.__name__=_C
_SlotId_Object=MibTableColumn
slotId=_SlotId_Object((1,3,6,1,4,1,21317,1,19,2,1,1),_SlotId_Type())
slotId.setMaxAccess(_B)
if mibBuilder.loadTexts:slotId.setStatus(_A)
class _GroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_GroupId_Type.__name__=_C
_GroupId_Object=MibTableColumn
groupId=_GroupId_Object((1,3,6,1,4,1,21317,1,19,2,1,2),_GroupId_Type())
groupId.setMaxAccess(_B)
if mibBuilder.loadTexts:groupId.setStatus(_A)
class _NvmeDrivePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('absent',0),('present',1)))
_NvmeDrivePresent_Type.__name__=_C
_NvmeDrivePresent_Object=MibTableColumn
nvmeDrivePresent=_NvmeDrivePresent_Object((1,3,6,1,4,1,21317,1,19,2,1,3),_NvmeDrivePresent_Type())
nvmeDrivePresent.setMaxAccess(_B)
if mibBuilder.loadTexts:nvmeDrivePresent.setStatus(_A)
class _Locate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dislocate',0),('locate',1)))
_Locate_Type.__name__=_C
_Locate_Object=MibTableColumn
locate=_Locate_Object((1,3,6,1,4,1,21317,1,19,2,1,4),_Locate_Type())
locate.setMaxAccess(_B)
if mibBuilder.loadTexts:locate.setStatus(_A)
class _Save2Remove_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-ready',0),('ready',1)))
_Save2Remove_Type.__name__=_C
_Save2Remove_Object=MibTableColumn
save2Remove=_Save2Remove_Object((1,3,6,1,4,1,21317,1,19,2,1,5),_Save2Remove_Type())
save2Remove.setMaxAccess(_B)
if mibBuilder.loadTexts:save2Remove.setStatus(_A)
class _VmdMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('vmd-off',0),('vmd-on',1)))
_VmdMode_Type.__name__=_C
_VmdMode_Object=MibTableColumn
vmdMode=_VmdMode_Object((1,3,6,1,4,1,21317,1,19,2,1,6),_VmdMode_Type())
vmdMode.setMaxAccess(_B)
if mibBuilder.loadTexts:vmdMode.setStatus(_A)
class _Temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_Temp_Type.__name__=_C
_Temp_Object=MibTableColumn
temp=_Temp_Object((1,3,6,1,4,1,21317,1,19,2,1,7),_Temp_Type())
temp.setMaxAccess(_B)
if mibBuilder.loadTexts:temp.setStatus(_A)
class _ClassCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ClassCode_Type.__name__=_D
_ClassCode_Object=MibTableColumn
classCode=_ClassCode_Object((1,3,6,1,4,1,21317,1,19,2,1,8),_ClassCode_Type())
classCode.setMaxAccess(_B)
if mibBuilder.loadTexts:classCode.setStatus(_A)
class _VendorID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_VendorID_Type.__name__=_D
_VendorID_Object=MibTableColumn
vendorID=_VendorID_Object((1,3,6,1,4,1,21317,1,19,2,1,9),_VendorID_Type())
vendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:vendorID.setStatus(_A)
class _SerialNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_SerialNum_Type.__name__=_D
_SerialNum_Object=MibTableColumn
serialNum=_SerialNum_Object((1,3,6,1,4,1,21317,1,19,2,1,10),_SerialNum_Type())
serialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNum.setStatus(_A)
class _ModelNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_ModelNum_Type.__name__=_D
_ModelNum_Object=MibTableColumn
modelNum=_ModelNum_Object((1,3,6,1,4,1,21317,1,19,2,1,11),_ModelNum_Type())
modelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:modelNum.setStatus(_A)
class _Port0MaxLinkSpd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Port0MaxLinkSpd_Type.__name__=_D
_Port0MaxLinkSpd_Object=MibTableColumn
port0MaxLinkSpd=_Port0MaxLinkSpd_Object((1,3,6,1,4,1,21317,1,19,2,1,12),_Port0MaxLinkSpd_Type())
port0MaxLinkSpd.setMaxAccess(_B)
if mibBuilder.loadTexts:port0MaxLinkSpd.setStatus(_A)
class _Port0MaxLinkWidth_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Port0MaxLinkWidth_Type.__name__=_D
_Port0MaxLinkWidth_Object=MibTableColumn
port0MaxLinkWidth=_Port0MaxLinkWidth_Object((1,3,6,1,4,1,21317,1,19,2,1,13),_Port0MaxLinkWidth_Type())
port0MaxLinkWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:port0MaxLinkWidth.setStatus(_A)
class _Port1MaxLinkSpd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Port1MaxLinkSpd_Type.__name__=_D
_Port1MaxLinkSpd_Object=MibTableColumn
port1MaxLinkSpd=_Port1MaxLinkSpd_Object((1,3,6,1,4,1,21317,1,19,2,1,14),_Port1MaxLinkSpd_Type())
port1MaxLinkSpd.setMaxAccess(_B)
if mibBuilder.loadTexts:port1MaxLinkSpd.setStatus(_A)
class _Port1MaxLinkWidth_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Port1MaxLinkWidth_Type.__name__=_D
_Port1MaxLinkWidth_Object=MibTableColumn
port1MaxLinkWidth=_Port1MaxLinkWidth_Object((1,3,6,1,4,1,21317,1,19,2,1,15),_Port1MaxLinkWidth_Type())
port1MaxLinkWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:port1MaxLinkWidth.setStatus(_A)
class _InitPowerRequirement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InitPowerRequirement_Type.__name__=_C
_InitPowerRequirement_Object=MibTableColumn
initPowerRequirement=_InitPowerRequirement_Object((1,3,6,1,4,1,21317,1,19,2,1,16),_InitPowerRequirement_Type())
initPowerRequirement.setMaxAccess(_B)
if mibBuilder.loadTexts:initPowerRequirement.setStatus(_A)
class _MaxPowerRequirement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MaxPowerRequirement_Type.__name__=_C
_MaxPowerRequirement_Object=MibTableColumn
maxPowerRequirement=_MaxPowerRequirement_Object((1,3,6,1,4,1,21317,1,19,2,1,17),_MaxPowerRequirement_Type())
maxPowerRequirement.setMaxAccess(_B)
if mibBuilder.loadTexts:maxPowerRequirement.setStatus(_A)
_NicTable_Object=MibTable
nicTable=_NicTable_Object((1,3,6,1,4,1,21317,1,20))
if mibBuilder.loadTexts:nicTable.setStatus(_A)
_NicEntry_Object=MibTableRow
nicEntry=_NicEntry_Object((1,3,6,1,4,1,21317,1,20,1))
nicEntry.setIndexNames((0,_E,_AL))
if mibBuilder.loadTexts:nicEntry.setStatus(_A)
class _NicNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_NicNumber_Type.__name__=_C
_NicNumber_Object=MibTableColumn
nicNumber=_NicNumber_Object((1,3,6,1,4,1,21317,1,20,1,1),_NicNumber_Type())
nicNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nicNumber.setStatus(_A)
class _NicName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_NicName_Type.__name__=_D
_NicName_Object=MibTableColumn
nicName=_NicName_Object((1,3,6,1,4,1,21317,1,20,1,2),_NicName_Type())
nicName.setMaxAccess(_B)
if mibBuilder.loadTexts:nicName.setStatus(_A)
class _NicMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(17,17));fixedLength=17
_NicMac_Type.__name__=_D
_NicMac_Object=MibTableColumn
nicMac=_NicMac_Object((1,3,6,1,4,1,21317,1,20,1,3),_NicMac_Type())
nicMac.setMaxAccess(_B)
if mibBuilder.loadTexts:nicMac.setStatus(_A)
_NicIpv4Addr_Type=IpAddress
_NicIpv4Addr_Object=MibTableColumn
nicIpv4Addr=_NicIpv4Addr_Object((1,3,6,1,4,1,21317,1,20,1,4),_NicIpv4Addr_Type())
nicIpv4Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:nicIpv4Addr.setStatus(_A)
class _NicIpv6Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(45,45));fixedLength=45
_NicIpv6Addr_Type.__name__=_D
_NicIpv6Addr_Object=MibTableColumn
nicIpv6Addr=_NicIpv6Addr_Object((1,3,6,1,4,1,21317,1,20,1,5),_NicIpv6Addr_Type())
nicIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:nicIpv6Addr.setStatus(_A)
class _NicGateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(45,45));fixedLength=45
_NicGateway_Type.__name__=_D
_NicGateway_Object=MibTableColumn
nicGateway=_NicGateway_Object((1,3,6,1,4,1,21317,1,20,1,6),_NicGateway_Type())
nicGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:nicGateway.setStatus(_A)
class _NicNetmask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(45,45));fixedLength=45
_NicNetmask_Type.__name__=_D
_NicNetmask_Object=MibTableColumn
nicNetmask=_NicNetmask_Object((1,3,6,1,4,1,21317,1,20,1,7),_NicNetmask_Type())
nicNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nicNetmask.setStatus(_A)
class _NicFqdn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_NicFqdn_Type.__name__=_D
_NicFqdn_Object=MibTableColumn
nicFqdn=_NicFqdn_Object((1,3,6,1,4,1,21317,1,20,1,8),_NicFqdn_Type())
nicFqdn.setMaxAccess(_B)
if mibBuilder.loadTexts:nicFqdn.setStatus(_A)
class _NicDns_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(91,91));fixedLength=91
_NicDns_Type.__name__=_D
_NicDns_Object=MibTableColumn
nicDns=_NicDns_Object((1,3,6,1,4,1,21317,1,20,1,9),_NicDns_Type())
nicDns.setMaxAccess(_B)
if mibBuilder.loadTexts:nicDns.setStatus(_A)
class _NicSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NicSpeed_Type.__name__=_C
_NicSpeed_Object=MibTableColumn
nicSpeed=_NicSpeed_Object((1,3,6,1,4,1,21317,1,20,1,10),_NicSpeed_Type())
nicSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:nicSpeed.setStatus(_A)
class _NicDescript_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_NicDescript_Type.__name__=_D
_NicDescript_Object=MibTableColumn
nicDescript=_NicDescript_Object((1,3,6,1,4,1,21317,1,20,1,11),_NicDescript_Type())
nicDescript.setMaxAccess(_B)
if mibBuilder.loadTexts:nicDescript.setStatus(_A)
class _NicStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_NicStatus_Type.__name__=_D
_NicStatus_Object=MibTableColumn
nicStatus=_NicStatus_Object((1,3,6,1,4,1,21317,1,20,1,12),_NicStatus_Type())
nicStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nicStatus.setStatus(_A)
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,21317,1,21))
_Ipv4DNSServer_Type=IpAddress
_Ipv4DNSServer_Object=MibScalar
ipv4DNSServer=_Ipv4DNSServer_Object((1,3,6,1,4,1,21317,1,21,1),_Ipv4DNSServer_Type())
ipv4DNSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4DNSServer.setStatus(_A)
_Ipv4Gateway_Type=IpAddress
_Ipv4Gateway_Object=MibScalar
ipv4Gateway=_Ipv4Gateway_Object((1,3,6,1,4,1,21317,1,21,2),_Ipv4Gateway_Type())
ipv4Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4Gateway.setStatus(_A)
class _Ipv6DNSServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(45,45));fixedLength=45
_Ipv6DNSServer_Type.__name__=_D
_Ipv6DNSServer_Object=MibScalar
ipv6DNSServer=_Ipv6DNSServer_Object((1,3,6,1,4,1,21317,1,21,3),_Ipv6DNSServer_Type())
ipv6DNSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6DNSServer.setStatus(_A)
class _Ipv6DUID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_Ipv6DUID_Type.__name__=_D
_Ipv6DUID_Object=MibScalar
ipv6DUID=_Ipv6DUID_Object((1,3,6,1,4,1,21317,1,21,4),_Ipv6DUID_Type())
ipv6DUID.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6DUID.setStatus(_A)
class _Dhcpv6State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('stateless',0),('stateful',1)))
_Dhcpv6State_Type.__name__=_C
_Dhcpv6State_Object=MibScalar
dhcpv6State=_Dhcpv6State_Object((1,3,6,1,4,1,21317,1,21,5),_Dhcpv6State_Type())
dhcpv6State.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpv6State.setStatus(_A)
class _Hostname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_Hostname_Type.__name__=_D
_Hostname_Object=MibScalar
hostname=_Hostname_Object((1,3,6,1,4,1,21317,1,21,6),_Hostname_Type())
hostname.setMaxAccess(_B)
if mibBuilder.loadTexts:hostname.setStatus(_A)
class _DhcpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_DhcpEnabled_Type.__name__=_C
_DhcpEnabled_Object=MibScalar
dhcpEnabled=_DhcpEnabled_Object((1,3,6,1,4,1,21317,1,21,7),_DhcpEnabled_Type())
dhcpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpEnabled.setStatus(_A)
class _VlanIDEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_VlanIDEnabled_Type.__name__=_C
_VlanIDEnabled_Object=MibScalar
vlanIDEnabled=_VlanIDEnabled_Object((1,3,6,1,4,1,21317,1,21,8),_VlanIDEnabled_Type())
vlanIDEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanIDEnabled.setStatus(_A)
class _VlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_VlanID_Type.__name__=_C
_VlanID_Object=MibScalar
vlanID=_VlanID_Object((1,3,6,1,4,1,21317,1,21,9),_VlanID_Type())
vlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanID.setStatus(_A)
class _LanInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_AM,0),('shared',1),('failover',2)))
_LanInterface_Type.__name__=_C
_LanInterface_Object=MibScalar
lanInterface=_LanInterface_Object((1,3,6,1,4,1,21317,1,21,10),_LanInterface_Type())
lanInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterface.setStatus(_A)
class _RmcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RmcpPort_Type.__name__=_C
_RmcpPort_Object=MibScalar
rmcpPort=_RmcpPort_Object((1,3,6,1,4,1,21317,1,21,11),_RmcpPort_Type())
rmcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rmcpPort.setStatus(_A)
class _ActiveLanInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_AM,0),('shared',1),('failover',2)))
_ActiveLanInterface_Type.__name__=_C
_ActiveLanInterface_Object=MibScalar
activeLanInterface=_ActiveLanInterface_Object((1,3,6,1,4,1,21317,1,21,12),_ActiveLanInterface_Type())
activeLanInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:activeLanInterface.setStatus(_A)
class _DedicatedLanDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),(_AN,1),(_AO,2)))
_DedicatedLanDuplex_Type.__name__=_C
_DedicatedLanDuplex_Object=MibScalar
dedicatedLanDuplex=_DedicatedLanDuplex_Object((1,3,6,1,4,1,21317,1,21,13),_DedicatedLanDuplex_Type())
dedicatedLanDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:dedicatedLanDuplex.setStatus(_A)
class _SharedLanDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),(_AN,1),(_AO,2)))
_SharedLanDuplex_Type.__name__=_C
_SharedLanDuplex_Object=MibScalar
sharedLanDuplex=_SharedLanDuplex_Object((1,3,6,1,4,1,21317,1,21,14),_SharedLanDuplex_Type())
sharedLanDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:sharedLanDuplex.setStatus(_A)
_Smtp_ObjectIdentity=ObjectIdentity
smtp=_Smtp_ObjectIdentity((1,3,6,1,4,1,21317,1,22))
class _SmtpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SmtpEnabled_Type.__name__=_C
_SmtpEnabled_Object=MibScalar
smtpEnabled=_SmtpEnabled_Object((1,3,6,1,4,1,21317,1,22,1),_SmtpEnabled_Type())
smtpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpEnabled.setStatus(_A)
class _SmtpServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_SmtpServer_Type.__name__=_D
_SmtpServer_Object=MibScalar
smtpServer=_SmtpServer_Object((1,3,6,1,4,1,21317,1,22,2),_SmtpServer_Type())
smtpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpServer.setStatus(_A)
class _SmtpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SmtpPort_Type.__name__=_C
_SmtpPort_Object=MibScalar
smtpPort=_SmtpPort_Object((1,3,6,1,4,1,21317,1,22,3),_SmtpPort_Type())
smtpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpPort.setStatus(_A)
class _SmtpUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_SmtpUsername_Type.__name__=_D
_SmtpUsername_Object=MibScalar
smtpUsername=_SmtpUsername_Object((1,3,6,1,4,1,21317,1,22,4),_SmtpUsername_Type())
smtpUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpUsername.setStatus(_A)
class _SmtpSenderEmail_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_SmtpSenderEmail_Type.__name__=_D
_SmtpSenderEmail_Object=MibScalar
smtpSenderEmail=_SmtpSenderEmail_Object((1,3,6,1,4,1,21317,1,22,5),_SmtpSenderEmail_Type())
smtpSenderEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpSenderEmail.setStatus(_A)
class _MouseMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absolute',1),('relative',2),('single',3)))
_MouseMode_Type.__name__=_C
_MouseMode_Object=MibScalar
mouseMode=_MouseMode_Object((1,3,6,1,4,1,21317,1,23),_MouseMode_Type())
mouseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mouseMode.setStatus(_A)
class _SysBootOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('none',0),('pxe',1),('hdd',2),('diags',3),('cdDvd',4),('biosSetup',5),('floppy',6),('usbKey',7),('usbHdd',8),('usbFloppy',9),('usbCD',10),('uefiUsbKey',11),('uefiCD',12),('uefiHdd',13),('uefiUsbHdd',14),('uefiUsbCD',15)))
_SysBootOrder_Type.__name__=_C
_SysBootOrder_Object=MibScalar
sysBootOrder=_SysBootOrder_Object((1,3,6,1,4,1,21317,1,24),_SysBootOrder_Type())
sysBootOrder.setMaxAccess(_F)
if mibBuilder.loadTexts:sysBootOrder.setStatus(_A)
guid=NotificationType((1,3,6,1,4,1,21317,1,30))
if mibBuilder.loadTexts:guid.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'aten':aten,'ipmi':ipmi,'sel':sel,'sensorTable':sensorTable,'sensorEntry':sensorEntry,_I:sensorNumber,'sensorReading':sensorReading,'sensorPositiveHysteresis':sensorPositiveHysteresis,'sensorNegativeHysteresis':sensorNegativeHysteresis,'lncThreshold':lncThreshold,'lcThreshold':lcThreshold,'lnrThreshold':lnrThreshold,'uncThreshold':uncThreshold,'ucThreshold':ucThreshold,'unrThreshold':unrThreshold,'eventAssertionEnable':eventAssertionEnable,'eventDeassertionEnable':eventDeassertionEnable,'sensorIDString':sensorIDString,'powerStatus':powerStatus,'boardinfo':boardinfo,'bmcMajorVesion':bmcMajorVesion,'bmcMinorVesion':bmcMinorVesion,'bmcBuildDate':bmcBuildDate,'biosVesion':biosVesion,'biosBuildDate':biosBuildDate,'hostName':hostName,'bmcBuildVesion':bmcBuildVesion,'hardwareinfo':hardwareinfo,'serialNumber':serialNumber,'cpuTable':cpuTable,'cpuEntry':cpuEntry,_J:cpuNumber,'processor':processor,'speed':speed,'core':core,'coreActive':coreActive,'manufacturer':manufacturer,'dimmTable':dimmTable,'dimmEntry':dimmEntry,_K:dimmNumber,'dimmLocation':dimmLocation,'dimmMaxCapSpeed':dimmMaxCapSpeed,'dimmOpSpeed':dimmOpSpeed,'dimmSize':dimmSize,'dimmSerialNo':dimmSerialNo,'dimmPartNo':dimmPartNo,'dimmManufacturer':dimmManufacturer,'storage':storage,'controllerTable':controllerTable,'controllerEntry':controllerEntry,_L:controllerNumber,'controllerProductName':controllerProductName,'serial':serial,'package':package,'fwVersion':fwVersion,'biosVersion':biosVersion,'bootBlockVersion':bootBlockVersion,'batteryStatus':batteryStatus,'pcieLocation':pcieLocation,'pcieSlot':pcieSlot,'phyHddTable':phyHddTable,'hddEntry':hddEntry,_M:hddNumber,'hddControllerNumber':hddControllerNumber,'enclosureNumber':enclosureNumber,'status':status,'temperature':temperature,'capacity':capacity,'vendor':vendor,'modelName':modelName,'revision':revision,'sn':sn,'linkSpeed':linkSpeed,'fwState':fwState,'otherErrCount':otherErrCount,'predictedFailCount':predictedFailCount,'mediaErrCount':mediaErrCount,'logHddTable':logHddTable,'volumeEntry':volumeEntry,_N:volNumber,'volControllerNumber':volControllerNumber,'volStatus':volStatus,'volCapacity':volCapacity,'priRaidLevel':priRaidLevel,'raidLevelQualifier':raidLevelQualifier,'secRaidLevel':secRaidLevel,'ldStripSize':ldStripSize,'numDevices':numDevices,'spanDepth':spanDepth,'state':state,'volName':volName,'coldResetBMC':coldResetBMC,'userTable':userTable,'userInfo':userInfo,'id':id,'username':username,'password':password,'privilege':privilege,'uid':uid,'alertTable':alertTable,'alertInfo':alertInfo,'alertNo':alertNo,'alertLevel':alertLevel,'destinationAddress':destinationAddress,'powerinfo':powerinfo,'psuNumber':psuNumber,'psuTable':psuTable,'psuEntry':psuEntry,_O:psuIndex,'psuStatus':psuStatus,'inputVoltage':inputVoltage,'inputCurrent':inputCurrent,'inputPower':inputPower,'outputVoltage':outputVoltage,'outputCurrent':outputCurrent,'outputPower':outputPower,'temperature1':temperature1,'temperature2':temperature2,'fanRPM1':fanRPM1,'fanRPM2':fanRPM2,'psuSerialNumber':psuSerialNumber,'fanMode':fanMode,'fruinfo':fruinfo,'chassis':chassis,'chassisType':chassisType,'chassisPartNumber':chassisPartNumber,'chassisSerialNumber':chassisSerialNumber,'board':board,'boardLanguage':boardLanguage,'boardManufacturer':boardManufacturer,'boardProductName':boardProductName,'boardSerialNumber':boardSerialNumber,'boardPartNumber':boardPartNumber,'product':product,'productLanguage':productLanguage,'productManufacturer':productManufacturer,'productName':productName,'productPartNumber':productPartNumber,'productVersion':productVersion,'productSerialNumber':productSerialNumber,'productAssetTag':productAssetTag,'ntpinfo':ntpinfo,'timeZone':timeZone,'ntpEnable':ntpEnable,'primaryNTPServer':primaryNTPServer,'secondaryNTPServer':secondaryNTPServer,'dst':dst,'selTable':selTable,'selEntry':selEntry,'selEid':selEid,'selTimeStamp':selTimeStamp,'selSensorName':selSensorName,'selSensorType':selSensorType,'selDescription':selDescription,'selRawData':selRawData,'nvme':nvme,'nvmeCtrlTbl':nvmeCtrlTbl,'nvmeCtrlEntry':nvmeCtrlEntry,_AK:nvmeCtrlPresent,'maxTemp':maxTemp,'maxSlotNum':maxSlotNum,'onboard':onboard,'driverIndex':driverIndex,'cpldVer':cpldVer,'nvmeDriveTbl':nvmeDriveTbl,'nvmeDriveEntry':nvmeDriveEntry,'slotId':slotId,'groupId':groupId,'nvmeDrivePresent':nvmeDrivePresent,'locate':locate,'save2Remove':save2Remove,'vmdMode':vmdMode,'temp':temp,'classCode':classCode,'vendorID':vendorID,'serialNum':serialNum,'modelNum':modelNum,'port0MaxLinkSpd':port0MaxLinkSpd,'port0MaxLinkWidth':port0MaxLinkWidth,'port1MaxLinkSpd':port1MaxLinkSpd,'port1MaxLinkWidth':port1MaxLinkWidth,'initPowerRequirement':initPowerRequirement,'maxPowerRequirement':maxPowerRequirement,'nicTable':nicTable,'nicEntry':nicEntry,_AL:nicNumber,'nicName':nicName,'nicMac':nicMac,'nicIpv4Addr':nicIpv4Addr,'nicIpv6Addr':nicIpv6Addr,'nicGateway':nicGateway,'nicNetmask':nicNetmask,'nicFqdn':nicFqdn,'nicDns':nicDns,'nicSpeed':nicSpeed,'nicDescript':nicDescript,'nicStatus':nicStatus,'network':network,'ipv4DNSServer':ipv4DNSServer,'ipv4Gateway':ipv4Gateway,'ipv6DNSServer':ipv6DNSServer,'ipv6DUID':ipv6DUID,'dhcpv6State':dhcpv6State,'hostname':hostname,'dhcpEnabled':dhcpEnabled,'vlanIDEnabled':vlanIDEnabled,'vlanID':vlanID,'lanInterface':lanInterface,'rmcpPort':rmcpPort,'activeLanInterface':activeLanInterface,'dedicatedLanDuplex':dedicatedLanDuplex,'sharedLanDuplex':sharedLanDuplex,'smtp':smtp,'smtpEnabled':smtpEnabled,'smtpServer':smtpServer,'smtpPort':smtpPort,'smtpUsername':smtpUsername,'smtpSenderEmail':smtpSenderEmail,'mouseMode':mouseMode,'sysBootOrder':sysBootOrder,'guid':guid})