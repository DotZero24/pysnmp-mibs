_k='metro1500TDMNumber'
_j='metro1500EthernetHubNumber'
_i='notAvailable'
_h='available'
_g='metro1500SwitchNumber'
_f='metro1500ConverterNumber'
_e='metro1500Converter'
_d='metro1500MainLogfileNumber'
_c='metro1500MainTrapsinkNumber'
_b='NotificationType'
_a='noError'
_Z='error'
_Y='noData'
_X='data'
_W='notEnabled'
_V='enabled'
_U='notInstalled'
_T='installed'
_S='metro1500FanNumber'
_R='metro1500PSNumber'
_Q='negative'
_P='positive'
_O='notLinked'
_N='linked'
_M='notPartitioned'
_L='partitioned'
_K='disable'
_J='enable'
_I='alwaysOff'
_H='alwaysOn'
_G='off'
_F='on'
_E='metro1500SlotNumber'
_D='Integer32'
_C='METRO1500-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_b,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_b,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Adva_ObjectIdentity=ObjectIdentity
adva=_Adva_ObjectIdentity((1,3,6,1,4,1,2544))
_AdvaProducts_ObjectIdentity=ObjectIdentity
advaProducts=_AdvaProducts_ObjectIdentity((1,3,6,1,4,1,2544,1))
_Metro1500_ObjectIdentity=ObjectIdentity
metro1500=_Metro1500_ObjectIdentity((1,3,6,1,4,1,2544,1,3))
_Metro1500Main_ObjectIdentity=ObjectIdentity
metro1500Main=_Metro1500Main_ObjectIdentity((1,3,6,1,4,1,2544,1,3,1))
_Metro1500Housing_ObjectIdentity=ObjectIdentity
metro1500Housing=_Metro1500Housing_ObjectIdentity((1,3,6,1,4,1,2544,1,3,1,1))
_Metro1500Manufacturer_Type=DisplayString
_Metro1500Manufacturer_Object=MibScalar
metro1500Manufacturer=_Metro1500Manufacturer_Object((1,3,6,1,4,1,2544,1,3,1,1,1),_Metro1500Manufacturer_Type())
metro1500Manufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500Manufacturer.setStatus(_A)
_Metro1500MainType_Type=DisplayString
_Metro1500MainType_Object=MibScalar
metro1500MainType=_Metro1500MainType_Object((1,3,6,1,4,1,2544,1,3,1,1,2),_Metro1500MainType_Type())
metro1500MainType.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainType.setStatus(_A)
_Metro1500MainSerialNumber_Type=DisplayString
_Metro1500MainSerialNumber_Object=MibScalar
metro1500MainSerialNumber=_Metro1500MainSerialNumber_Object((1,3,6,1,4,1,2544,1,3,1,1,3),_Metro1500MainSerialNumber_Type())
metro1500MainSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainSerialNumber.setStatus(_A)
_Metro1500MainHardwareVersion_Type=DisplayString
_Metro1500MainHardwareVersion_Object=MibScalar
metro1500MainHardwareVersion=_Metro1500MainHardwareVersion_Object((1,3,6,1,4,1,2544,1,3,1,1,4),_Metro1500MainHardwareVersion_Type())
metro1500MainHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainHardwareVersion.setStatus(_A)
_Metro1500MainSoftwareVersion_Type=DisplayString
_Metro1500MainSoftwareVersion_Object=MibScalar
metro1500MainSoftwareVersion=_Metro1500MainSoftwareVersion_Object((1,3,6,1,4,1,2544,1,3,1,1,5),_Metro1500MainSoftwareVersion_Type())
metro1500MainSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainSoftwareVersion.setStatus(_A)
_Metro1500MainBusMessages_Type=Integer32
_Metro1500MainBusMessages_Object=MibScalar
metro1500MainBusMessages=_Metro1500MainBusMessages_Object((1,3,6,1,4,1,2544,1,3,1,1,6),_Metro1500MainBusMessages_Type())
metro1500MainBusMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainBusMessages.setStatus(_A)
_Metro1500MainBusErrors_Type=Integer32
_Metro1500MainBusErrors_Object=MibScalar
metro1500MainBusErrors=_Metro1500MainBusErrors_Object((1,3,6,1,4,1,2544,1,3,1,1,7),_Metro1500MainBusErrors_Type())
metro1500MainBusErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainBusErrors.setStatus(_A)
class _Metro1500MainLastEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Metro1500MainLastEvent_Type.__name__=_D
_Metro1500MainLastEvent_Object=MibScalar
metro1500MainLastEvent=_Metro1500MainLastEvent_Object((1,3,6,1,4,1,2544,1,3,1,1,8),_Metro1500MainLastEvent_Type())
metro1500MainLastEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainLastEvent.setStatus(_A)
_Metro1500MainMotd_Type=DisplayString
_Metro1500MainMotd_Object=MibScalar
metro1500MainMotd=_Metro1500MainMotd_Object((1,3,6,1,4,1,2544,1,3,1,1,9),_Metro1500MainMotd_Type())
metro1500MainMotd.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainMotd.setStatus(_A)
_Metro1500MainTrapsinkTable_Object=MibTable
metro1500MainTrapsinkTable=_Metro1500MainTrapsinkTable_Object((1,3,6,1,4,1,2544,1,3,1,1,10))
if mibBuilder.loadTexts:metro1500MainTrapsinkTable.setStatus(_A)
_Metro1500MainTrapsinkEntry_Object=MibTableRow
metro1500MainTrapsinkEntry=_Metro1500MainTrapsinkEntry_Object((1,3,6,1,4,1,2544,1,3,1,1,10,1))
metro1500MainTrapsinkEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:metro1500MainTrapsinkEntry.setStatus(_A)
class _Metro1500MainTrapsinkNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Metro1500MainTrapsinkNumber_Type.__name__=_D
_Metro1500MainTrapsinkNumber_Object=MibTableColumn
metro1500MainTrapsinkNumber=_Metro1500MainTrapsinkNumber_Object((1,3,6,1,4,1,2544,1,3,1,1,10,1,1),_Metro1500MainTrapsinkNumber_Type())
metro1500MainTrapsinkNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainTrapsinkNumber.setStatus(_A)
_Metro1500MainTrapsinkAddress_Type=DisplayString
_Metro1500MainTrapsinkAddress_Object=MibTableColumn
metro1500MainTrapsinkAddress=_Metro1500MainTrapsinkAddress_Object((1,3,6,1,4,1,2544,1,3,1,1,10,1,2),_Metro1500MainTrapsinkAddress_Type())
metro1500MainTrapsinkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainTrapsinkAddress.setStatus(_A)
_Metro1500MainTrapsinkCommunity_Type=DisplayString
_Metro1500MainTrapsinkCommunity_Object=MibTableColumn
metro1500MainTrapsinkCommunity=_Metro1500MainTrapsinkCommunity_Object((1,3,6,1,4,1,2544,1,3,1,1,10,1,3),_Metro1500MainTrapsinkCommunity_Type())
metro1500MainTrapsinkCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainTrapsinkCommunity.setStatus(_A)
class _Metro1500MainTrapsinkPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Metro1500MainTrapsinkPriority_Type.__name__=_D
_Metro1500MainTrapsinkPriority_Object=MibTableColumn
metro1500MainTrapsinkPriority=_Metro1500MainTrapsinkPriority_Object((1,3,6,1,4,1,2544,1,3,1,1,10,1,4),_Metro1500MainTrapsinkPriority_Type())
metro1500MainTrapsinkPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainTrapsinkPriority.setStatus(_A)
_Metro1500MainLogfileTable_Object=MibTable
metro1500MainLogfileTable=_Metro1500MainLogfileTable_Object((1,3,6,1,4,1,2544,1,3,1,1,11))
if mibBuilder.loadTexts:metro1500MainLogfileTable.setStatus(_A)
_Metro1500MainLogfileEntry_Object=MibTableRow
metro1500MainLogfileEntry=_Metro1500MainLogfileEntry_Object((1,3,6,1,4,1,2544,1,3,1,1,11,1))
metro1500MainLogfileEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:metro1500MainLogfileEntry.setStatus(_A)
class _Metro1500MainLogfileNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Metro1500MainLogfileNumber_Type.__name__=_D
_Metro1500MainLogfileNumber_Object=MibTableColumn
metro1500MainLogfileNumber=_Metro1500MainLogfileNumber_Object((1,3,6,1,4,1,2544,1,3,1,1,11,1,1),_Metro1500MainLogfileNumber_Type())
metro1500MainLogfileNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainLogfileNumber.setStatus(_A)
_Metro1500MainLogfileName_Type=DisplayString
_Metro1500MainLogfileName_Object=MibTableColumn
metro1500MainLogfileName=_Metro1500MainLogfileName_Object((1,3,6,1,4,1,2544,1,3,1,1,11,1,2),_Metro1500MainLogfileName_Type())
metro1500MainLogfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainLogfileName.setStatus(_A)
_Metro1500MainLogfileSize_Type=Integer32
_Metro1500MainLogfileSize_Object=MibTableColumn
metro1500MainLogfileSize=_Metro1500MainLogfileSize_Object((1,3,6,1,4,1,2544,1,3,1,1,11,1,3),_Metro1500MainLogfileSize_Type())
metro1500MainLogfileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainLogfileSize.setStatus(_A)
class _Metro1500MainLogfilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Metro1500MainLogfilePriority_Type.__name__=_D
_Metro1500MainLogfilePriority_Object=MibTableColumn
metro1500MainLogfilePriority=_Metro1500MainLogfilePriority_Object((1,3,6,1,4,1,2544,1,3,1,1,11,1,4),_Metro1500MainLogfilePriority_Type())
metro1500MainLogfilePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500MainLogfilePriority.setStatus(_A)
_Metro1500SlotTable_Object=MibTable
metro1500SlotTable=_Metro1500SlotTable_Object((1,3,6,1,4,1,2544,1,3,1,2))
if mibBuilder.loadTexts:metro1500SlotTable.setStatus(_A)
_Metro1500SlotEntry_Object=MibTableRow
metro1500SlotEntry=_Metro1500SlotEntry_Object((1,3,6,1,4,1,2544,1,3,1,2,1))
metro1500SlotEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:metro1500SlotEntry.setStatus(_A)
class _Metro1500SlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,79))
_Metro1500SlotNumber_Type.__name__=_D
_Metro1500SlotNumber_Object=MibTableColumn
metro1500SlotNumber=_Metro1500SlotNumber_Object((1,3,6,1,4,1,2544,1,3,1,2,1,1),_Metro1500SlotNumber_Type())
metro1500SlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SlotNumber.setStatus(_A)
_Metro1500Type_Type=DisplayString
_Metro1500Type_Object=MibTableColumn
metro1500Type=_Metro1500Type_Object((1,3,6,1,4,1,2544,1,3,1,2,1,2),_Metro1500Type_Type())
metro1500Type.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500Type.setStatus(_A)
class _Metro1500SlotTypeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,7,10,32,33,39,64,255)));namedValues=NamedValues(*((_e,1),('metro1000Converter',2),('metro1000EthernetConverter',3),('metro1500-2-5GbConverter',5),('metro1500-TRL-Converter',7),('metro1500-4PortTDMCard',10),('nemi',32),('demi',33),('metro1500-EthernetHubCard',39),('switch',64),('other',255)))
_Metro1500SlotTypeNumber_Type.__name__=_D
_Metro1500SlotTypeNumber_Object=MibTableColumn
metro1500SlotTypeNumber=_Metro1500SlotTypeNumber_Object((1,3,6,1,4,1,2544,1,3,1,2,1,3),_Metro1500SlotTypeNumber_Type())
metro1500SlotTypeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SlotTypeNumber.setStatus(_A)
_Metro1500SerialNumber_Type=DisplayString
_Metro1500SerialNumber_Object=MibTableColumn
metro1500SerialNumber=_Metro1500SerialNumber_Object((1,3,6,1,4,1,2544,1,3,1,2,1,4),_Metro1500SerialNumber_Type())
metro1500SerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SerialNumber.setStatus(_A)
_Metro1500HardwareVersion_Type=DisplayString
_Metro1500HardwareVersion_Object=MibTableColumn
metro1500HardwareVersion=_Metro1500HardwareVersion_Object((1,3,6,1,4,1,2544,1,3,1,2,1,5),_Metro1500HardwareVersion_Type())
metro1500HardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500HardwareVersion.setStatus(_A)
_Metro1500SoftwareVersion_Type=DisplayString
_Metro1500SoftwareVersion_Object=MibTableColumn
metro1500SoftwareVersion=_Metro1500SoftwareVersion_Object((1,3,6,1,4,1,2544,1,3,1,2,1,6),_Metro1500SoftwareVersion_Type())
metro1500SoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SoftwareVersion.setStatus(_A)
_Metro1500Temperature_Type=Integer32
_Metro1500Temperature_Object=MibTableColumn
metro1500Temperature=_Metro1500Temperature_Object((1,3,6,1,4,1,2544,1,3,1,2,1,7),_Metro1500Temperature_Type())
metro1500Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500Temperature.setStatus(_A)
_Metro1500BoardVoltage_Type=Integer32
_Metro1500BoardVoltage_Object=MibTableColumn
metro1500BoardVoltage=_Metro1500BoardVoltage_Object((1,3,6,1,4,1,2544,1,3,1,2,1,8),_Metro1500BoardVoltage_Type())
metro1500BoardVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500BoardVoltage.setStatus(_A)
_Metro1500DetailInfo_Type=ObjectIdentifier
_Metro1500DetailInfo_Object=MibTableColumn
metro1500DetailInfo=_Metro1500DetailInfo_Object((1,3,6,1,4,1,2544,1,3,1,2,1,9),_Metro1500DetailInfo_Type())
metro1500DetailInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500DetailInfo.setStatus(_A)
class _Metro1500EPLDVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Metro1500EPLDVersion_Type.__name__=_D
_Metro1500EPLDVersion_Object=MibTableColumn
metro1500EPLDVersion=_Metro1500EPLDVersion_Object((1,3,6,1,4,1,2544,1,3,1,2,1,10),_Metro1500EPLDVersion_Type())
metro1500EPLDVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EPLDVersion.setStatus(_A)
_Metro1500PSTable_Object=MibTable
metro1500PSTable=_Metro1500PSTable_Object((1,3,6,1,4,1,2544,1,3,1,3))
if mibBuilder.loadTexts:metro1500PSTable.setStatus(_A)
_Metro1500PSEntry_Object=MibTableRow
metro1500PSEntry=_Metro1500PSEntry_Object((1,3,6,1,4,1,2544,1,3,1,3,1))
metro1500PSEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:metro1500PSEntry.setStatus(_A)
class _Metro1500PSNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Metro1500PSNumber_Type.__name__=_D
_Metro1500PSNumber_Object=MibTableColumn
metro1500PSNumber=_Metro1500PSNumber_Object((1,3,6,1,4,1,2544,1,3,1,3,1,1),_Metro1500PSNumber_Type())
metro1500PSNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500PSNumber.setStatus(_A)
class _Metro1500PSOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500PSOn_Type.__name__=_D
_Metro1500PSOn_Object=MibTableColumn
metro1500PSOn=_Metro1500PSOn_Object((1,3,6,1,4,1,2544,1,3,1,3,1,2),_Metro1500PSOn_Type())
metro1500PSOn.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500PSOn.setStatus(_A)
_Metro1500FanTable_Object=MibTable
metro1500FanTable=_Metro1500FanTable_Object((1,3,6,1,4,1,2544,1,3,1,4))
if mibBuilder.loadTexts:metro1500FanTable.setStatus(_A)
_Metro1500FanEntry_Object=MibTableRow
metro1500FanEntry=_Metro1500FanEntry_Object((1,3,6,1,4,1,2544,1,3,1,4,1))
metro1500FanEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:metro1500FanEntry.setStatus(_A)
class _Metro1500FanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Metro1500FanNumber_Type.__name__=_D
_Metro1500FanNumber_Object=MibTableColumn
metro1500FanNumber=_Metro1500FanNumber_Object((1,3,6,1,4,1,2544,1,3,1,4,1,1),_Metro1500FanNumber_Type())
metro1500FanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500FanNumber.setStatus(_A)
class _Metro1500FanOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500FanOn_Type.__name__=_D
_Metro1500FanOn_Object=MibTableColumn
metro1500FanOn=_Metro1500FanOn_Object((1,3,6,1,4,1,2544,1,3,1,4,1,2),_Metro1500FanOn_Type())
metro1500FanOn.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500FanOn.setStatus(_A)
_Metro1500Converter_ObjectIdentity=ObjectIdentity
metro1500Converter=_Metro1500Converter_ObjectIdentity((1,3,6,1,4,1,2544,1,3,5))
_Metro1500ConverterTable_Object=MibTable
metro1500ConverterTable=_Metro1500ConverterTable_Object((1,3,6,1,4,1,2544,1,3,5,1))
if mibBuilder.loadTexts:metro1500ConverterTable.setStatus(_A)
_Metro1500ConverterEntry_Object=MibTableRow
metro1500ConverterEntry=_Metro1500ConverterEntry_Object((1,3,6,1,4,1,2544,1,3,5,1,1))
metro1500ConverterEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:metro1500ConverterEntry.setStatus(_A)
class _Metro1500ConverterNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,79))
_Metro1500ConverterNumber_Type.__name__=_D
_Metro1500ConverterNumber_Object=MibTableColumn
metro1500ConverterNumber=_Metro1500ConverterNumber_Object((1,3,6,1,4,1,2544,1,3,5,1,1,1),_Metro1500ConverterNumber_Type())
metro1500ConverterNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500ConverterNumber.setStatus(_A)
class _Metro1500RxLoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500RxLoc_Type.__name__=_D
_Metro1500RxLoc_Object=MibTableColumn
metro1500RxLoc=_Metro1500RxLoc_Object((1,3,6,1,4,1,2544,1,3,5,1,1,2),_Metro1500RxLoc_Type())
metro1500RxLoc.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500RxLoc.setStatus(_A)
class _Metro1500TxLoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_Metro1500TxLoc_Type.__name__=_D
_Metro1500TxLoc_Object=MibTableColumn
metro1500TxLoc=_Metro1500TxLoc_Object((1,3,6,1,4,1,2544,1,3,5,1,1,3),_Metro1500TxLoc_Type())
metro1500TxLoc.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TxLoc.setStatus(_A)
class _Metro1500TxLocC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Metro1500TxLocC_Type.__name__=_D
_Metro1500TxLocC_Object=MibTableColumn
metro1500TxLocC=_Metro1500TxLocC_Object((1,3,6,1,4,1,2544,1,3,5,1,1,4),_Metro1500TxLocC_Type())
metro1500TxLocC.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TxLocC.setStatus(_A)
class _Metro1500TxLocTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_Metro1500TxLocTemp_Type.__name__=_D
_Metro1500TxLocTemp_Object=MibTableColumn
metro1500TxLocTemp=_Metro1500TxLocTemp_Object((1,3,6,1,4,1,2544,1,3,5,1,1,5),_Metro1500TxLocTemp_Type())
metro1500TxLocTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TxLocTemp.setStatus(_A)
class _Metro1500RxRem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500RxRem_Type.__name__=_D
_Metro1500RxRem_Object=MibTableColumn
metro1500RxRem=_Metro1500RxRem_Object((1,3,6,1,4,1,2544,1,3,5,1,1,6),_Metro1500RxRem_Type())
metro1500RxRem.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500RxRem.setStatus(_A)
class _Metro1500TxRem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_Metro1500TxRem_Type.__name__=_D
_Metro1500TxRem_Object=MibTableColumn
metro1500TxRem=_Metro1500TxRem_Object((1,3,6,1,4,1,2544,1,3,5,1,1,7),_Metro1500TxRem_Type())
metro1500TxRem.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TxRem.setStatus(_A)
class _Metro1500TxRemC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Metro1500TxRemC_Type.__name__=_D
_Metro1500TxRemC_Object=MibTableColumn
metro1500TxRemC=_Metro1500TxRemC_Object((1,3,6,1,4,1,2544,1,3,5,1,1,8),_Metro1500TxRemC_Type())
metro1500TxRemC.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TxRemC.setStatus(_A)
class _Metro1500TxRemTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_Metro1500TxRemTemp_Type.__name__=_D
_Metro1500TxRemTemp_Object=MibTableColumn
metro1500TxRemTemp=_Metro1500TxRemTemp_Object((1,3,6,1,4,1,2544,1,3,5,1,1,9),_Metro1500TxRemTemp_Type())
metro1500TxRemTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TxRemTemp.setStatus(_A)
class _Metro1500RxRem2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500RxRem2_Type.__name__=_D
_Metro1500RxRem2_Object=MibTableColumn
metro1500RxRem2=_Metro1500RxRem2_Object((1,3,6,1,4,1,2544,1,3,5,1,1,10),_Metro1500RxRem2_Type())
metro1500RxRem2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500RxRem2.setStatus(_A)
class _Metro1500ClockState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),('fail',3)))
_Metro1500ClockState_Type.__name__=_D
_Metro1500ClockState_Object=MibTableColumn
metro1500ClockState=_Metro1500ClockState_Object((1,3,6,1,4,1,2544,1,3,5,1,1,11),_Metro1500ClockState_Type())
metro1500ClockState.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500ClockState.setStatus(_A)
_Metro1500ClockFreq_Type=Integer32
_Metro1500ClockFreq_Object=MibTableColumn
metro1500ClockFreq=_Metro1500ClockFreq_Object((1,3,6,1,4,1,2544,1,3,5,1,1,12),_Metro1500ClockFreq_Type())
metro1500ClockFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500ClockFreq.setStatus(_A)
class _Metro1500LocLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500LocLoop_Type.__name__=_D
_Metro1500LocLoop_Object=MibTableColumn
metro1500LocLoop=_Metro1500LocLoop_Object((1,3,6,1,4,1,2544,1,3,5,1,1,13),_Metro1500LocLoop_Type())
metro1500LocLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500LocLoop.setStatus(_A)
class _Metro1500RemLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500RemLoop_Type.__name__=_D
_Metro1500RemLoop_Object=MibTableColumn
metro1500RemLoop=_Metro1500RemLoop_Object((1,3,6,1,4,1,2544,1,3,5,1,1,14),_Metro1500RemLoop_Type())
metro1500RemLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500RemLoop.setStatus(_A)
class _Metro1500ClockType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,7,9,11,21,22,31,32,41,42,51,52,61,62,71,72,75,76,81,82,255)));namedValues=NamedValues(*(('multiClockLSModule',1),('multiClockLS',2),('multiClockFCGbE',3),('multiClockOCxGbE',5),('multiClockOCxFC',7),('multiClockOCxGbEFC',9),('multiClockFCGbEOnBoard',11),('fixedClock125MbpsModule',21),('fixedClock125Mbps',22),('fixedClock155MbpsModule',31),('fixedClock155Mbps',32),('fixedClock200MbpsModule',41),('fixedClock200Mbps',42),('fixedClock266MbpsModule',51),('fixedClock266Mbps',52),('fixedClock622MbpsModule',61),('fixedClock622Mbps',62),('fixedClock1062MbpsModule',71),('fixedClock1062Mbps',72),('fixedClock1250MbpsModule',75),('fixedClock1250Mbps',76),('fixedClock2500MbpsModule',81),('fixedClock2500Mbps',82),('other',255)))
_Metro1500ClockType_Type.__name__=_D
_Metro1500ClockType_Object=MibTableColumn
metro1500ClockType=_Metro1500ClockType_Object((1,3,6,1,4,1,2544,1,3,5,1,1,15),_Metro1500ClockType_Type())
metro1500ClockType.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500ClockType.setStatus(_A)
_Metro1500Switch_ObjectIdentity=ObjectIdentity
metro1500Switch=_Metro1500Switch_ObjectIdentity((1,3,6,1,4,1,2544,1,3,10))
_Metro1500SwitchTable_Object=MibTable
metro1500SwitchTable=_Metro1500SwitchTable_Object((1,3,6,1,4,1,2544,1,3,10,1))
if mibBuilder.loadTexts:metro1500SwitchTable.setStatus(_A)
_Metro1500SwitchEntry_Object=MibTableRow
metro1500SwitchEntry=_Metro1500SwitchEntry_Object((1,3,6,1,4,1,2544,1,3,10,1,1))
metro1500SwitchEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:metro1500SwitchEntry.setStatus(_A)
class _Metro1500SwitchNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,79))
_Metro1500SwitchNumber_Type.__name__=_D
_Metro1500SwitchNumber_Object=MibTableColumn
metro1500SwitchNumber=_Metro1500SwitchNumber_Object((1,3,6,1,4,1,2544,1,3,10,1,1,1),_Metro1500SwitchNumber_Type())
metro1500SwitchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SwitchNumber.setStatus(_A)
class _Metro1500SwitchLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lineA',1),('lineB',2)))
_Metro1500SwitchLine_Type.__name__=_D
_Metro1500SwitchLine_Object=MibTableColumn
metro1500SwitchLine=_Metro1500SwitchLine_Object((1,3,6,1,4,1,2544,1,3,10,1,1,2),_Metro1500SwitchLine_Type())
metro1500SwitchLine.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SwitchLine.setStatus(_A)
class _Metro1500SwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('locked',2)))
_Metro1500SwitchMode_Type.__name__=_D
_Metro1500SwitchMode_Object=MibTableColumn
metro1500SwitchMode=_Metro1500SwitchMode_Object((1,3,6,1,4,1,2544,1,3,10,1,1,3),_Metro1500SwitchMode_Type())
metro1500SwitchMode.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SwitchMode.setStatus(_A)
class _Metro1500SwitchLaserOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500SwitchLaserOn_Type.__name__=_D
_Metro1500SwitchLaserOn_Object=MibTableColumn
metro1500SwitchLaserOn=_Metro1500SwitchLaserOn_Object((1,3,6,1,4,1,2544,1,3,10,1,1,4),_Metro1500SwitchLaserOn_Type())
metro1500SwitchLaserOn.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SwitchLaserOn.setStatus(_A)
class _Metro1500SwitchLineAavail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_Metro1500SwitchLineAavail_Type.__name__=_D
_Metro1500SwitchLineAavail_Object=MibTableColumn
metro1500SwitchLineAavail=_Metro1500SwitchLineAavail_Object((1,3,6,1,4,1,2544,1,3,10,1,1,5),_Metro1500SwitchLineAavail_Type())
metro1500SwitchLineAavail.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SwitchLineAavail.setStatus(_A)
class _Metro1500SwitchLineBavail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_Metro1500SwitchLineBavail_Type.__name__=_D
_Metro1500SwitchLineBavail_Object=MibTableColumn
metro1500SwitchLineBavail=_Metro1500SwitchLineBavail_Object((1,3,6,1,4,1,2544,1,3,10,1,1,6),_Metro1500SwitchLineBavail_Type())
metro1500SwitchLineBavail.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500SwitchLineBavail.setStatus(_A)
_Metro1500EthernetHub_ObjectIdentity=ObjectIdentity
metro1500EthernetHub=_Metro1500EthernetHub_ObjectIdentity((1,3,6,1,4,1,2544,1,3,14))
_Metro1500EthernetHubTable_Object=MibTable
metro1500EthernetHubTable=_Metro1500EthernetHubTable_Object((1,3,6,1,4,1,2544,1,3,14,1))
if mibBuilder.loadTexts:metro1500EthernetHubTable.setStatus(_A)
_Metro1500EthernetHubEntry_Object=MibTableRow
metro1500EthernetHubEntry=_Metro1500EthernetHubEntry_Object((1,3,6,1,4,1,2544,1,3,14,1,1))
metro1500EthernetHubEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:metro1500EthernetHubEntry.setStatus(_A)
class _Metro1500EthernetHubNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,79))
_Metro1500EthernetHubNumber_Type.__name__=_D
_Metro1500EthernetHubNumber_Object=MibTableColumn
metro1500EthernetHubNumber=_Metro1500EthernetHubNumber_Object((1,3,6,1,4,1,2544,1,3,14,1,1,1),_Metro1500EthernetHubNumber_Type())
metro1500EthernetHubNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubNumber.setStatus(_A)
class _Metro1500EthernetHubPortEnable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Metro1500EthernetHubPortEnable1_Type.__name__=_D
_Metro1500EthernetHubPortEnable1_Object=MibTableColumn
metro1500EthernetHubPortEnable1=_Metro1500EthernetHubPortEnable1_Object((1,3,6,1,4,1,2544,1,3,14,1,1,10),_Metro1500EthernetHubPortEnable1_Type())
metro1500EthernetHubPortEnable1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortEnable1.setStatus(_A)
class _Metro1500EthernetHubPortPartitionStatus1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_Metro1500EthernetHubPortPartitionStatus1_Type.__name__=_D
_Metro1500EthernetHubPortPartitionStatus1_Object=MibTableColumn
metro1500EthernetHubPortPartitionStatus1=_Metro1500EthernetHubPortPartitionStatus1_Object((1,3,6,1,4,1,2544,1,3,14,1,1,11),_Metro1500EthernetHubPortPartitionStatus1_Type())
metro1500EthernetHubPortPartitionStatus1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPartitionStatus1.setStatus(_A)
class _Metro1500EthernetHubPortLinkStatus1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Metro1500EthernetHubPortLinkStatus1_Type.__name__=_D
_Metro1500EthernetHubPortLinkStatus1_Object=MibTableColumn
metro1500EthernetHubPortLinkStatus1=_Metro1500EthernetHubPortLinkStatus1_Object((1,3,6,1,4,1,2544,1,3,14,1,1,12),_Metro1500EthernetHubPortLinkStatus1_Type())
metro1500EthernetHubPortLinkStatus1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortLinkStatus1.setStatus(_A)
class _Metro1500EthernetHubPortPolarity1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_Metro1500EthernetHubPortPolarity1_Type.__name__=_D
_Metro1500EthernetHubPortPolarity1_Object=MibTableColumn
metro1500EthernetHubPortPolarity1=_Metro1500EthernetHubPortPolarity1_Object((1,3,6,1,4,1,2544,1,3,14,1,1,13),_Metro1500EthernetHubPortPolarity1_Type())
metro1500EthernetHubPortPolarity1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPolarity1.setStatus(_A)
class _Metro1500EthernetHubPortEnable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Metro1500EthernetHubPortEnable2_Type.__name__=_D
_Metro1500EthernetHubPortEnable2_Object=MibTableColumn
metro1500EthernetHubPortEnable2=_Metro1500EthernetHubPortEnable2_Object((1,3,6,1,4,1,2544,1,3,14,1,1,20),_Metro1500EthernetHubPortEnable2_Type())
metro1500EthernetHubPortEnable2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortEnable2.setStatus(_A)
class _Metro1500EthernetHubPortPartitionStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_Metro1500EthernetHubPortPartitionStatus2_Type.__name__=_D
_Metro1500EthernetHubPortPartitionStatus2_Object=MibTableColumn
metro1500EthernetHubPortPartitionStatus2=_Metro1500EthernetHubPortPartitionStatus2_Object((1,3,6,1,4,1,2544,1,3,14,1,1,21),_Metro1500EthernetHubPortPartitionStatus2_Type())
metro1500EthernetHubPortPartitionStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPartitionStatus2.setStatus(_A)
class _Metro1500EthernetHubPortLinkStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Metro1500EthernetHubPortLinkStatus2_Type.__name__=_D
_Metro1500EthernetHubPortLinkStatus2_Object=MibTableColumn
metro1500EthernetHubPortLinkStatus2=_Metro1500EthernetHubPortLinkStatus2_Object((1,3,6,1,4,1,2544,1,3,14,1,1,22),_Metro1500EthernetHubPortLinkStatus2_Type())
metro1500EthernetHubPortLinkStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortLinkStatus2.setStatus(_A)
class _Metro1500EthernetHubPortPolarity2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_Metro1500EthernetHubPortPolarity2_Type.__name__=_D
_Metro1500EthernetHubPortPolarity2_Object=MibTableColumn
metro1500EthernetHubPortPolarity2=_Metro1500EthernetHubPortPolarity2_Object((1,3,6,1,4,1,2544,1,3,14,1,1,23),_Metro1500EthernetHubPortPolarity2_Type())
metro1500EthernetHubPortPolarity2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPolarity2.setStatus(_A)
class _Metro1500EthernetHubPortEnable3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Metro1500EthernetHubPortEnable3_Type.__name__=_D
_Metro1500EthernetHubPortEnable3_Object=MibTableColumn
metro1500EthernetHubPortEnable3=_Metro1500EthernetHubPortEnable3_Object((1,3,6,1,4,1,2544,1,3,14,1,1,30),_Metro1500EthernetHubPortEnable3_Type())
metro1500EthernetHubPortEnable3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortEnable3.setStatus(_A)
class _Metro1500EthernetHubPortPartitionStatus3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_Metro1500EthernetHubPortPartitionStatus3_Type.__name__=_D
_Metro1500EthernetHubPortPartitionStatus3_Object=MibTableColumn
metro1500EthernetHubPortPartitionStatus3=_Metro1500EthernetHubPortPartitionStatus3_Object((1,3,6,1,4,1,2544,1,3,14,1,1,31),_Metro1500EthernetHubPortPartitionStatus3_Type())
metro1500EthernetHubPortPartitionStatus3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPartitionStatus3.setStatus(_A)
class _Metro1500EthernetHubPortLinkStatus3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Metro1500EthernetHubPortLinkStatus3_Type.__name__=_D
_Metro1500EthernetHubPortLinkStatus3_Object=MibTableColumn
metro1500EthernetHubPortLinkStatus3=_Metro1500EthernetHubPortLinkStatus3_Object((1,3,6,1,4,1,2544,1,3,14,1,1,32),_Metro1500EthernetHubPortLinkStatus3_Type())
metro1500EthernetHubPortLinkStatus3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortLinkStatus3.setStatus(_A)
class _Metro1500EthernetHubPortPolarity3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_Metro1500EthernetHubPortPolarity3_Type.__name__=_D
_Metro1500EthernetHubPortPolarity3_Object=MibTableColumn
metro1500EthernetHubPortPolarity3=_Metro1500EthernetHubPortPolarity3_Object((1,3,6,1,4,1,2544,1,3,14,1,1,33),_Metro1500EthernetHubPortPolarity3_Type())
metro1500EthernetHubPortPolarity3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPolarity3.setStatus(_A)
class _Metro1500EthernetHubPortEnable4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Metro1500EthernetHubPortEnable4_Type.__name__=_D
_Metro1500EthernetHubPortEnable4_Object=MibTableColumn
metro1500EthernetHubPortEnable4=_Metro1500EthernetHubPortEnable4_Object((1,3,6,1,4,1,2544,1,3,14,1,1,40),_Metro1500EthernetHubPortEnable4_Type())
metro1500EthernetHubPortEnable4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortEnable4.setStatus(_A)
class _Metro1500EthernetHubPortPartitionStatus4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_Metro1500EthernetHubPortPartitionStatus4_Type.__name__=_D
_Metro1500EthernetHubPortPartitionStatus4_Object=MibTableColumn
metro1500EthernetHubPortPartitionStatus4=_Metro1500EthernetHubPortPartitionStatus4_Object((1,3,6,1,4,1,2544,1,3,14,1,1,41),_Metro1500EthernetHubPortPartitionStatus4_Type())
metro1500EthernetHubPortPartitionStatus4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPartitionStatus4.setStatus(_A)
class _Metro1500EthernetHubPortLinkStatus4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Metro1500EthernetHubPortLinkStatus4_Type.__name__=_D
_Metro1500EthernetHubPortLinkStatus4_Object=MibTableColumn
metro1500EthernetHubPortLinkStatus4=_Metro1500EthernetHubPortLinkStatus4_Object((1,3,6,1,4,1,2544,1,3,14,1,1,42),_Metro1500EthernetHubPortLinkStatus4_Type())
metro1500EthernetHubPortLinkStatus4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortLinkStatus4.setStatus(_A)
class _Metro1500EthernetHubPortPolarity4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_Metro1500EthernetHubPortPolarity4_Type.__name__=_D
_Metro1500EthernetHubPortPolarity4_Object=MibTableColumn
metro1500EthernetHubPortPolarity4=_Metro1500EthernetHubPortPolarity4_Object((1,3,6,1,4,1,2544,1,3,14,1,1,43),_Metro1500EthernetHubPortPolarity4_Type())
metro1500EthernetHubPortPolarity4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPolarity4.setStatus(_A)
class _Metro1500EthernetHubPortEnable5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Metro1500EthernetHubPortEnable5_Type.__name__=_D
_Metro1500EthernetHubPortEnable5_Object=MibTableColumn
metro1500EthernetHubPortEnable5=_Metro1500EthernetHubPortEnable5_Object((1,3,6,1,4,1,2544,1,3,14,1,1,50),_Metro1500EthernetHubPortEnable5_Type())
metro1500EthernetHubPortEnable5.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortEnable5.setStatus(_A)
class _Metro1500EthernetHubPortPartitionStatus5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_Metro1500EthernetHubPortPartitionStatus5_Type.__name__=_D
_Metro1500EthernetHubPortPartitionStatus5_Object=MibTableColumn
metro1500EthernetHubPortPartitionStatus5=_Metro1500EthernetHubPortPartitionStatus5_Object((1,3,6,1,4,1,2544,1,3,14,1,1,51),_Metro1500EthernetHubPortPartitionStatus5_Type())
metro1500EthernetHubPortPartitionStatus5.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPartitionStatus5.setStatus(_A)
class _Metro1500EthernetHubPortLinkStatus5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Metro1500EthernetHubPortLinkStatus5_Type.__name__=_D
_Metro1500EthernetHubPortLinkStatus5_Object=MibTableColumn
metro1500EthernetHubPortLinkStatus5=_Metro1500EthernetHubPortLinkStatus5_Object((1,3,6,1,4,1,2544,1,3,14,1,1,52),_Metro1500EthernetHubPortLinkStatus5_Type())
metro1500EthernetHubPortLinkStatus5.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortLinkStatus5.setStatus(_A)
class _Metro1500EthernetHubPortPolarity5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_Metro1500EthernetHubPortPolarity5_Type.__name__=_D
_Metro1500EthernetHubPortPolarity5_Object=MibTableColumn
metro1500EthernetHubPortPolarity5=_Metro1500EthernetHubPortPolarity5_Object((1,3,6,1,4,1,2544,1,3,14,1,1,53),_Metro1500EthernetHubPortPolarity5_Type())
metro1500EthernetHubPortPolarity5.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500EthernetHubPortPolarity5.setStatus(_A)
_Metro1500TDM_ObjectIdentity=ObjectIdentity
metro1500TDM=_Metro1500TDM_ObjectIdentity((1,3,6,1,4,1,2544,1,3,15))
_Metro1500TDMTable_Object=MibTable
metro1500TDMTable=_Metro1500TDMTable_Object((1,3,6,1,4,1,2544,1,3,15,1))
if mibBuilder.loadTexts:metro1500TDMTable.setStatus(_A)
_Metro1500TDMEntry_Object=MibTableRow
metro1500TDMEntry=_Metro1500TDMEntry_Object((1,3,6,1,4,1,2544,1,3,15,1,1))
metro1500TDMEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:metro1500TDMEntry.setStatus(_A)
class _Metro1500TDMNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,79))
_Metro1500TDMNumber_Type.__name__=_D
_Metro1500TDMNumber_Object=MibTableColumn
metro1500TDMNumber=_Metro1500TDMNumber_Object((1,3,6,1,4,1,2544,1,3,15,1,1,1),_Metro1500TDMNumber_Type())
metro1500TDMNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMNumber.setStatus(_A)
class _Metro1500TDMRxRem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500TDMRxRem_Type.__name__=_D
_Metro1500TDMRxRem_Object=MibTableColumn
metro1500TDMRxRem=_Metro1500TDMRxRem_Object((1,3,6,1,4,1,2544,1,3,15,1,1,4),_Metro1500TDMRxRem_Type())
metro1500TDMRxRem.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMRxRem.setStatus(_A)
class _Metro1500TDMRxSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync',1),('noSync',2)))
_Metro1500TDMRxSync_Type.__name__=_D
_Metro1500TDMRxSync_Object=MibTableColumn
metro1500TDMRxSync=_Metro1500TDMRxSync_Object((1,3,6,1,4,1,2544,1,3,15,1,1,5),_Metro1500TDMRxSync_Type())
metro1500TDMRxSync.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMRxSync.setStatus(_A)
class _Metro1500TDMTxRem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_Metro1500TDMTxRem_Type.__name__=_D
_Metro1500TDMTxRem_Object=MibTableColumn
metro1500TDMTxRem=_Metro1500TDMTxRem_Object((1,3,6,1,4,1,2544,1,3,15,1,1,6),_Metro1500TDMTxRem_Type())
metro1500TDMTxRem.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMTxRem.setStatus(_A)
class _Metro1500TDMTxRemC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Metro1500TDMTxRemC_Type.__name__=_D
_Metro1500TDMTxRemC_Object=MibTableColumn
metro1500TDMTxRemC=_Metro1500TDMTxRemC_Object((1,3,6,1,4,1,2544,1,3,15,1,1,7),_Metro1500TDMTxRemC_Type())
metro1500TDMTxRemC.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMTxRemC.setStatus(_A)
class _Metro1500TDMTxRemTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_Metro1500TDMTxRemTemp_Type.__name__=_D
_Metro1500TDMTxRemTemp_Object=MibTableColumn
metro1500TDMTxRemTemp=_Metro1500TDMTxRemTemp_Object((1,3,6,1,4,1,2544,1,3,15,1,1,8),_Metro1500TDMTxRemTemp_Type())
metro1500TDMTxRemTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMTxRemTemp.setStatus(_A)
class _Metro1500TDMLocLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500TDMLocLoop_Type.__name__=_D
_Metro1500TDMLocLoop_Object=MibTableColumn
metro1500TDMLocLoop=_Metro1500TDMLocLoop_Object((1,3,6,1,4,1,2544,1,3,15,1,1,9),_Metro1500TDMLocLoop_Type())
metro1500TDMLocLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocLoop.setStatus(_A)
class _Metro1500TDMLocModuleInst1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_Metro1500TDMLocModuleInst1_Type.__name__=_D
_Metro1500TDMLocModuleInst1_Object=MibTableColumn
metro1500TDMLocModuleInst1=_Metro1500TDMLocModuleInst1_Object((1,3,6,1,4,1,2544,1,3,15,1,1,20),_Metro1500TDMLocModuleInst1_Type())
metro1500TDMLocModuleInst1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleInst1.setStatus(_A)
class _Metro1500TDMLocModuleEnable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_Metro1500TDMLocModuleEnable1_Type.__name__=_D
_Metro1500TDMLocModuleEnable1_Object=MibTableColumn
metro1500TDMLocModuleEnable1=_Metro1500TDMLocModuleEnable1_Object((1,3,6,1,4,1,2544,1,3,15,1,1,21),_Metro1500TDMLocModuleEnable1_Type())
metro1500TDMLocModuleEnable1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleEnable1.setStatus(_A)
class _Metro1500TDMLocModuleRx1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500TDMLocModuleRx1_Type.__name__=_D
_Metro1500TDMLocModuleRx1_Object=MibTableColumn
metro1500TDMLocModuleRx1=_Metro1500TDMLocModuleRx1_Object((1,3,6,1,4,1,2544,1,3,15,1,1,22),_Metro1500TDMLocModuleRx1_Type())
metro1500TDMLocModuleRx1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRx1.setStatus(_A)
class _Metro1500TDMLocModuleTx1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_Metro1500TDMLocModuleTx1_Type.__name__=_D
_Metro1500TDMLocModuleTx1_Object=MibTableColumn
metro1500TDMLocModuleTx1=_Metro1500TDMLocModuleTx1_Object((1,3,6,1,4,1,2544,1,3,15,1,1,23),_Metro1500TDMLocModuleTx1_Type())
metro1500TDMLocModuleTx1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleTx1.setStatus(_A)
class _Metro1500TDMLocModuleRemoteData1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_Metro1500TDMLocModuleRemoteData1_Type.__name__=_D
_Metro1500TDMLocModuleRemoteData1_Object=MibTableColumn
metro1500TDMLocModuleRemoteData1=_Metro1500TDMLocModuleRemoteData1_Object((1,3,6,1,4,1,2544,1,3,15,1,1,24),_Metro1500TDMLocModuleRemoteData1_Type())
metro1500TDMLocModuleRemoteData1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRemoteData1.setStatus(_A)
_Metro1500TDMLocModuleClockFrequency1_Type=Integer32
_Metro1500TDMLocModuleClockFrequency1_Object=MibTableColumn
metro1500TDMLocModuleClockFrequency1=_Metro1500TDMLocModuleClockFrequency1_Object((1,3,6,1,4,1,2544,1,3,15,1,1,25),_Metro1500TDMLocModuleClockFrequency1_Type())
metro1500TDMLocModuleClockFrequency1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFrequency1.setStatus(_A)
class _Metro1500TDMLocModuleClockError1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_Metro1500TDMLocModuleClockError1_Type.__name__=_D
_Metro1500TDMLocModuleClockError1_Object=MibTableColumn
metro1500TDMLocModuleClockError1=_Metro1500TDMLocModuleClockError1_Object((1,3,6,1,4,1,2544,1,3,15,1,1,26),_Metro1500TDMLocModuleClockError1_Type())
metro1500TDMLocModuleClockError1.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockError1.setStatus(_A)
class _Metro1500TDMLocModuleInst2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_Metro1500TDMLocModuleInst2_Type.__name__=_D
_Metro1500TDMLocModuleInst2_Object=MibTableColumn
metro1500TDMLocModuleInst2=_Metro1500TDMLocModuleInst2_Object((1,3,6,1,4,1,2544,1,3,15,1,1,30),_Metro1500TDMLocModuleInst2_Type())
metro1500TDMLocModuleInst2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleInst2.setStatus(_A)
class _Metro1500TDMLocModuleEnable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_Metro1500TDMLocModuleEnable2_Type.__name__=_D
_Metro1500TDMLocModuleEnable2_Object=MibTableColumn
metro1500TDMLocModuleEnable2=_Metro1500TDMLocModuleEnable2_Object((1,3,6,1,4,1,2544,1,3,15,1,1,31),_Metro1500TDMLocModuleEnable2_Type())
metro1500TDMLocModuleEnable2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleEnable2.setStatus(_A)
class _Metro1500TDMLocModuleRx2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500TDMLocModuleRx2_Type.__name__=_D
_Metro1500TDMLocModuleRx2_Object=MibTableColumn
metro1500TDMLocModuleRx2=_Metro1500TDMLocModuleRx2_Object((1,3,6,1,4,1,2544,1,3,15,1,1,32),_Metro1500TDMLocModuleRx2_Type())
metro1500TDMLocModuleRx2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRx2.setStatus(_A)
class _Metro1500TDMLocModuleTx2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_Metro1500TDMLocModuleTx2_Type.__name__=_D
_Metro1500TDMLocModuleTx2_Object=MibTableColumn
metro1500TDMLocModuleTx2=_Metro1500TDMLocModuleTx2_Object((1,3,6,1,4,1,2544,1,3,15,1,1,33),_Metro1500TDMLocModuleTx2_Type())
metro1500TDMLocModuleTx2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleTx2.setStatus(_A)
class _Metro1500TDMLocModuleRemoteData2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_Metro1500TDMLocModuleRemoteData2_Type.__name__=_D
_Metro1500TDMLocModuleRemoteData2_Object=MibTableColumn
metro1500TDMLocModuleRemoteData2=_Metro1500TDMLocModuleRemoteData2_Object((1,3,6,1,4,1,2544,1,3,15,1,1,34),_Metro1500TDMLocModuleRemoteData2_Type())
metro1500TDMLocModuleRemoteData2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRemoteData2.setStatus(_A)
_Metro1500TDMLocModuleClockFrequency2_Type=Integer32
_Metro1500TDMLocModuleClockFrequency2_Object=MibTableColumn
metro1500TDMLocModuleClockFrequency2=_Metro1500TDMLocModuleClockFrequency2_Object((1,3,6,1,4,1,2544,1,3,15,1,1,35),_Metro1500TDMLocModuleClockFrequency2_Type())
metro1500TDMLocModuleClockFrequency2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFrequency2.setStatus(_A)
class _Metro1500TDMLocModuleClockError2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_Metro1500TDMLocModuleClockError2_Type.__name__=_D
_Metro1500TDMLocModuleClockError2_Object=MibTableColumn
metro1500TDMLocModuleClockError2=_Metro1500TDMLocModuleClockError2_Object((1,3,6,1,4,1,2544,1,3,15,1,1,36),_Metro1500TDMLocModuleClockError2_Type())
metro1500TDMLocModuleClockError2.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockError2.setStatus(_A)
class _Metro1500TDMLocModuleInst3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_Metro1500TDMLocModuleInst3_Type.__name__=_D
_Metro1500TDMLocModuleInst3_Object=MibTableColumn
metro1500TDMLocModuleInst3=_Metro1500TDMLocModuleInst3_Object((1,3,6,1,4,1,2544,1,3,15,1,1,40),_Metro1500TDMLocModuleInst3_Type())
metro1500TDMLocModuleInst3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleInst3.setStatus(_A)
class _Metro1500TDMLocModuleEnable3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_Metro1500TDMLocModuleEnable3_Type.__name__=_D
_Metro1500TDMLocModuleEnable3_Object=MibTableColumn
metro1500TDMLocModuleEnable3=_Metro1500TDMLocModuleEnable3_Object((1,3,6,1,4,1,2544,1,3,15,1,1,41),_Metro1500TDMLocModuleEnable3_Type())
metro1500TDMLocModuleEnable3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleEnable3.setStatus(_A)
class _Metro1500TDMLocModuleRx3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500TDMLocModuleRx3_Type.__name__=_D
_Metro1500TDMLocModuleRx3_Object=MibTableColumn
metro1500TDMLocModuleRx3=_Metro1500TDMLocModuleRx3_Object((1,3,6,1,4,1,2544,1,3,15,1,1,42),_Metro1500TDMLocModuleRx3_Type())
metro1500TDMLocModuleRx3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRx3.setStatus(_A)
class _Metro1500TDMLocModuleTx3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_Metro1500TDMLocModuleTx3_Type.__name__=_D
_Metro1500TDMLocModuleTx3_Object=MibTableColumn
metro1500TDMLocModuleTx3=_Metro1500TDMLocModuleTx3_Object((1,3,6,1,4,1,2544,1,3,15,1,1,43),_Metro1500TDMLocModuleTx3_Type())
metro1500TDMLocModuleTx3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleTx3.setStatus(_A)
class _Metro1500TDMLocModuleRemoteData3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_Metro1500TDMLocModuleRemoteData3_Type.__name__=_D
_Metro1500TDMLocModuleRemoteData3_Object=MibTableColumn
metro1500TDMLocModuleRemoteData3=_Metro1500TDMLocModuleRemoteData3_Object((1,3,6,1,4,1,2544,1,3,15,1,1,44),_Metro1500TDMLocModuleRemoteData3_Type())
metro1500TDMLocModuleRemoteData3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRemoteData3.setStatus(_A)
_Metro1500TDMLocModuleClockFrequency3_Type=Integer32
_Metro1500TDMLocModuleClockFrequency3_Object=MibTableColumn
metro1500TDMLocModuleClockFrequency3=_Metro1500TDMLocModuleClockFrequency3_Object((1,3,6,1,4,1,2544,1,3,15,1,1,45),_Metro1500TDMLocModuleClockFrequency3_Type())
metro1500TDMLocModuleClockFrequency3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFrequency3.setStatus(_A)
class _Metro1500TDMLocModuleClockError3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_Metro1500TDMLocModuleClockError3_Type.__name__=_D
_Metro1500TDMLocModuleClockError3_Object=MibTableColumn
metro1500TDMLocModuleClockError3=_Metro1500TDMLocModuleClockError3_Object((1,3,6,1,4,1,2544,1,3,15,1,1,46),_Metro1500TDMLocModuleClockError3_Type())
metro1500TDMLocModuleClockError3.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockError3.setStatus(_A)
class _Metro1500TDMLocModuleInst4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_Metro1500TDMLocModuleInst4_Type.__name__=_D
_Metro1500TDMLocModuleInst4_Object=MibTableColumn
metro1500TDMLocModuleInst4=_Metro1500TDMLocModuleInst4_Object((1,3,6,1,4,1,2544,1,3,15,1,1,50),_Metro1500TDMLocModuleInst4_Type())
metro1500TDMLocModuleInst4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleInst4.setStatus(_A)
class _Metro1500TDMLocModuleEnable4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_Metro1500TDMLocModuleEnable4_Type.__name__=_D
_Metro1500TDMLocModuleEnable4_Object=MibTableColumn
metro1500TDMLocModuleEnable4=_Metro1500TDMLocModuleEnable4_Object((1,3,6,1,4,1,2544,1,3,15,1,1,51),_Metro1500TDMLocModuleEnable4_Type())
metro1500TDMLocModuleEnable4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleEnable4.setStatus(_A)
class _Metro1500TDMLocModuleRx4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Metro1500TDMLocModuleRx4_Type.__name__=_D
_Metro1500TDMLocModuleRx4_Object=MibTableColumn
metro1500TDMLocModuleRx4=_Metro1500TDMLocModuleRx4_Object((1,3,6,1,4,1,2544,1,3,15,1,1,52),_Metro1500TDMLocModuleRx4_Type())
metro1500TDMLocModuleRx4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRx4.setStatus(_A)
class _Metro1500TDMLocModuleTx4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_Metro1500TDMLocModuleTx4_Type.__name__=_D
_Metro1500TDMLocModuleTx4_Object=MibTableColumn
metro1500TDMLocModuleTx4=_Metro1500TDMLocModuleTx4_Object((1,3,6,1,4,1,2544,1,3,15,1,1,53),_Metro1500TDMLocModuleTx4_Type())
metro1500TDMLocModuleTx4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleTx4.setStatus(_A)
class _Metro1500TDMLocModuleRemoteData4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_Metro1500TDMLocModuleRemoteData4_Type.__name__=_D
_Metro1500TDMLocModuleRemoteData4_Object=MibTableColumn
metro1500TDMLocModuleRemoteData4=_Metro1500TDMLocModuleRemoteData4_Object((1,3,6,1,4,1,2544,1,3,15,1,1,54),_Metro1500TDMLocModuleRemoteData4_Type())
metro1500TDMLocModuleRemoteData4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleRemoteData4.setStatus(_A)
_Metro1500TDMLocModuleClockFrequency4_Type=Integer32
_Metro1500TDMLocModuleClockFrequency4_Object=MibTableColumn
metro1500TDMLocModuleClockFrequency4=_Metro1500TDMLocModuleClockFrequency4_Object((1,3,6,1,4,1,2544,1,3,15,1,1,55),_Metro1500TDMLocModuleClockFrequency4_Type())
metro1500TDMLocModuleClockFrequency4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFrequency4.setStatus(_A)
class _Metro1500TDMLocModuleClockError4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_Metro1500TDMLocModuleClockError4_Type.__name__=_D
_Metro1500TDMLocModuleClockError4_Object=MibTableColumn
metro1500TDMLocModuleClockError4=_Metro1500TDMLocModuleClockError4_Object((1,3,6,1,4,1,2544,1,3,15,1,1,56),_Metro1500TDMLocModuleClockError4_Type())
metro1500TDMLocModuleClockError4.setMaxAccess(_B)
if mibBuilder.loadTexts:metro1500TDMLocModuleClockError4.setStatus(_A)
_Metro1500Trap_ObjectIdentity=ObjectIdentity
metro1500Trap=_Metro1500Trap_ObjectIdentity((1,3,6,1,4,1,2544,1,3,100))
metro1500HardwareAdded=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,1))
metro1500HardwareAdded.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500HardwareAdded.setStatus('')
metro1500HardwareDeleted=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,2))
metro1500HardwareDeleted.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500HardwareDeleted.setStatus('')
metro1500PSNotFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,3))
metro1500PSNotFail.setObjects((_C,_R))
if mibBuilder.loadTexts:metro1500PSNotFail.setStatus('')
metro1500PSFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,4))
metro1500PSFail.setObjects((_C,_R))
if mibBuilder.loadTexts:metro1500PSFail.setStatus('')
metro1500FanNotFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,5))
metro1500FanNotFail.setObjects((_C,_S))
if mibBuilder.loadTexts:metro1500FanNotFail.setStatus('')
metro1500FanFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,6))
metro1500FanFail.setObjects((_C,_S))
if mibBuilder.loadTexts:metro1500FanFail.setStatus('')
metro1500BusNotFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,7))
if mibBuilder.loadTexts:metro1500BusNotFail.setStatus('')
metro1500BusFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,8))
if mibBuilder.loadTexts:metro1500BusFail.setStatus('')
metro1500RxLocOn=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,20))
metro1500RxLocOn.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RxLocOn.setStatus('')
metro1500RxLocOff=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,21))
metro1500RxLocOff.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RxLocOff.setStatus('')
metro1500TxLocOn=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,22))
metro1500TxLocOn.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TxLocOn.setStatus('')
metro1500TxLocOff=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,23))
metro1500TxLocOff.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TxLocOff.setStatus('')
metro1500RxRemOn=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,24))
metro1500RxRemOn.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RxRemOn.setStatus('')
metro1500RxRemOff=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,25))
metro1500RxRemOff.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RxRemOff.setStatus('')
metro1500TxRemOn=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,26))
metro1500TxRemOn.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TxRemOn.setStatus('')
metro1500TxRemOff=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,27))
metro1500TxRemOff.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TxRemOff.setStatus('')
metro1500RxRem2On=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,28))
metro1500RxRem2On.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RxRem2On.setStatus('')
metro1500RxRem2Off=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,29))
metro1500RxRem2Off.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RxRem2Off.setStatus('')
metro1500TxRem2On=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,30))
metro1500TxRem2On.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TxRem2On.setStatus('')
metro1500TxRem2Off=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,31))
metro1500TxRem2Off.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TxRem2Off.setStatus('')
metro1500ClockNoFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,32))
metro1500ClockNoFail.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500ClockNoFail.setStatus('')
metro1500ClockFail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,33))
metro1500ClockFail.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500ClockFail.setStatus('')
metro1500ClockChangeFrequency=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,34))
metro1500ClockChangeFrequency.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500ClockChangeFrequency.setStatus('')
metro1500LocLoopOn=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,35))
metro1500LocLoopOn.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500LocLoopOn.setStatus('')
metro1500LocLoopOff=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,36))
metro1500LocLoopOff.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500LocLoopOff.setStatus('')
metro1500RemLoopOn=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,37))
metro1500RemLoopOn.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RemLoopOn.setStatus('')
metro1500RemLoopOff=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,38))
metro1500RemLoopOff.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500RemLoopOff.setStatus('')
metro1500switchReferenceLaserOn=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,40))
metro1500switchReferenceLaserOn.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchReferenceLaserOn.setStatus('')
metro1500switchReferenceLaserOff=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,41))
metro1500switchReferenceLaserOff.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchReferenceLaserOff.setStatus('')
metro1500switchToA=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,42))
metro1500switchToA.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchToA.setStatus('')
metro1500switchToB=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,43))
metro1500switchToB.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchToB.setStatus('')
metro1500switchAutomatic=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,44))
metro1500switchAutomatic.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchAutomatic.setStatus('')
metro1500switchLocked=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,45))
metro1500switchLocked.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchLocked.setStatus('')
metro1500switchLineAavail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,46))
metro1500switchLineAavail.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchLineAavail.setStatus('')
metro1500switchLineANotAvail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,47))
metro1500switchLineANotAvail.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchLineANotAvail.setStatus('')
metro1500switchLineBavail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,48))
metro1500switchLineBavail.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchLineBavail.setStatus('')
metro1500switchLineBNotAvail=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,49))
metro1500switchLineBNotAvail.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500switchLineBNotAvail.setStatus('')
metro1500repeatedMessage=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,50))
metro1500repeatedMessage.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500repeatedMessage.setStatus('')
metro1500INNCDown=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,51))
if mibBuilder.loadTexts:metro1500INNCDown.setStatus('')
metro1500INNCUp=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,52))
if mibBuilder.loadTexts:metro1500INNCUp.setStatus('')
metro1500EthernetHubPortEnable=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,60))
metro1500EthernetHubPortEnable.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500EthernetHubPortEnable.setStatus('')
metro1500EthernetHubPortDisable=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,61))
metro1500EthernetHubPortDisable.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500EthernetHubPortDisable.setStatus('')
metro1500EthernetHubPortPartitioned=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,62))
metro1500EthernetHubPortPartitioned.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500EthernetHubPortPartitioned.setStatus('')
metro1500EthernetHubPortNotPartitioned=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,63))
metro1500EthernetHubPortNotPartitioned.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500EthernetHubPortNotPartitioned.setStatus('')
metro1500EthernetHubPortLinkPulses=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,64))
metro1500EthernetHubPortLinkPulses.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500EthernetHubPortLinkPulses.setStatus('')
metro1500EthernetHubPortNoLinkPulses=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,65))
metro1500EthernetHubPortNoLinkPulses.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500EthernetHubPortNoLinkPulses.setStatus('')
metro1500TDMRemoteSyncLoss=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,70))
metro1500TDMRemoteSyncLoss.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMRemoteSyncLoss.setStatus('')
metro1500TDMRemoteSync=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,71))
metro1500TDMRemoteSync.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMRemoteSync.setStatus('')
metro1500TDMLocModuleEnabled1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,72))
metro1500TDMLocModuleEnabled1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleEnabled1.setStatus('')
metro1500TDMLocModuleDisable1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,73))
metro1500TDMLocModuleDisable1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleDisable1.setStatus('')
metro1500TDMLocModuleEnabled2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,74))
metro1500TDMLocModuleEnabled2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleEnabled2.setStatus('')
metro1500TDMLocModuleDisable2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,75))
metro1500TDMLocModuleDisable2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleDisable2.setStatus('')
metro1500TDMLocModuleEnabled3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,76))
metro1500TDMLocModuleEnabled3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleEnabled3.setStatus('')
metro1500TDMLocModuleDisable3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,77))
metro1500TDMLocModuleDisable3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleDisable3.setStatus('')
metro1500TDMLocModuleEnabled4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,78))
metro1500TDMLocModuleEnabled4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleEnabled4.setStatus('')
metro1500TDMLocModuleDisable4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,79))
metro1500TDMLocModuleDisable4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleDisable4.setStatus('')
metro1500TDMLocModuleRxOn1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,88))
metro1500TDMLocModuleRxOn1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOn1.setStatus('')
metro1500TDMLocModuleRxOff1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,89))
metro1500TDMLocModuleRxOff1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOff1.setStatus('')
metro1500TDMLocModuleRxOn2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,90))
metro1500TDMLocModuleRxOn2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOn2.setStatus('')
metro1500TDMLocModuleRxOff2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,91))
metro1500TDMLocModuleRxOff2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOff2.setStatus('')
metro1500TDMLocModuleRxOn3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,92))
metro1500TDMLocModuleRxOn3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOn3.setStatus('')
metro1500TDMLocModuleRxOff3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,93))
metro1500TDMLocModuleRxOff3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOff3.setStatus('')
metro1500TDMLocModuleRxOn4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,94))
metro1500TDMLocModuleRxOn4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOn4.setStatus('')
metro1500TDMLocModuleRxOff4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,95))
metro1500TDMLocModuleRxOff4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleRxOff4.setStatus('')
metro1500TDMLocModuleData1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,104))
metro1500TDMLocModuleData1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleData1.setStatus('')
metro1500TDMLocModuleNoData1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,105))
metro1500TDMLocModuleNoData1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleNoData1.setStatus('')
metro1500TDMLocModuleData2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,106))
metro1500TDMLocModuleData2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleData2.setStatus('')
metro1500TDMLocModuleNoData2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,107))
metro1500TDMLocModuleNoData2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleNoData2.setStatus('')
metro1500TDMLocModuleData3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,108))
metro1500TDMLocModuleData3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleData3.setStatus('')
metro1500TDMLocModuleNoData3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,109))
metro1500TDMLocModuleNoData3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleNoData3.setStatus('')
metro1500TDMLocModuleData4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,110))
metro1500TDMLocModuleData4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleData4.setStatus('')
metro1500TDMLocModuleNoData4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,111))
metro1500TDMLocModuleNoData4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleNoData4.setStatus('')
metro1500TDMLocModuleClockFail1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,120))
metro1500TDMLocModuleClockFail1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFail1.setStatus('')
metro1500TDMLocModuleClockNoFail1=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,121))
metro1500TDMLocModuleClockNoFail1.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockNoFail1.setStatus('')
metro1500TDMLocModuleClockFail2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,122))
metro1500TDMLocModuleClockFail2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFail2.setStatus('')
metro1500TDMLocModuleClockNoFail2=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,123))
metro1500TDMLocModuleClockNoFail2.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockNoFail2.setStatus('')
metro1500TDMLocModuleClockFail3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,124))
metro1500TDMLocModuleClockFail3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFail3.setStatus('')
metro1500TDMLocModuleClockNoFail3=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,125))
metro1500TDMLocModuleClockNoFail3.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockNoFail3.setStatus('')
metro1500TDMLocModuleClockFail4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,126))
metro1500TDMLocModuleClockFail4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockFail4.setStatus('')
metro1500TDMLocModuleClockNoFail4=NotificationType((1,3,6,1,4,1,2544,1,3,100,0,127))
metro1500TDMLocModuleClockNoFail4.setObjects((_C,_E))
if mibBuilder.loadTexts:metro1500TDMLocModuleClockNoFail4.setStatus('')
mibBuilder.exportSymbols(_C,**{'org':org,'dod':dod,'internet':internet,'private':private,'enterprises':enterprises,'adva':adva,'advaProducts':advaProducts,'metro1500':metro1500,'metro1500Main':metro1500Main,'metro1500Housing':metro1500Housing,'metro1500Manufacturer':metro1500Manufacturer,'metro1500MainType':metro1500MainType,'metro1500MainSerialNumber':metro1500MainSerialNumber,'metro1500MainHardwareVersion':metro1500MainHardwareVersion,'metro1500MainSoftwareVersion':metro1500MainSoftwareVersion,'metro1500MainBusMessages':metro1500MainBusMessages,'metro1500MainBusErrors':metro1500MainBusErrors,'metro1500MainLastEvent':metro1500MainLastEvent,'metro1500MainMotd':metro1500MainMotd,'metro1500MainTrapsinkTable':metro1500MainTrapsinkTable,'metro1500MainTrapsinkEntry':metro1500MainTrapsinkEntry,_c:metro1500MainTrapsinkNumber,'metro1500MainTrapsinkAddress':metro1500MainTrapsinkAddress,'metro1500MainTrapsinkCommunity':metro1500MainTrapsinkCommunity,'metro1500MainTrapsinkPriority':metro1500MainTrapsinkPriority,'metro1500MainLogfileTable':metro1500MainLogfileTable,'metro1500MainLogfileEntry':metro1500MainLogfileEntry,_d:metro1500MainLogfileNumber,'metro1500MainLogfileName':metro1500MainLogfileName,'metro1500MainLogfileSize':metro1500MainLogfileSize,'metro1500MainLogfilePriority':metro1500MainLogfilePriority,'metro1500SlotTable':metro1500SlotTable,'metro1500SlotEntry':metro1500SlotEntry,_E:metro1500SlotNumber,'metro1500Type':metro1500Type,'metro1500SlotTypeNumber':metro1500SlotTypeNumber,'metro1500SerialNumber':metro1500SerialNumber,'metro1500HardwareVersion':metro1500HardwareVersion,'metro1500SoftwareVersion':metro1500SoftwareVersion,'metro1500Temperature':metro1500Temperature,'metro1500BoardVoltage':metro1500BoardVoltage,'metro1500DetailInfo':metro1500DetailInfo,'metro1500EPLDVersion':metro1500EPLDVersion,'metro1500PSTable':metro1500PSTable,'metro1500PSEntry':metro1500PSEntry,_R:metro1500PSNumber,'metro1500PSOn':metro1500PSOn,'metro1500FanTable':metro1500FanTable,'metro1500FanEntry':metro1500FanEntry,_S:metro1500FanNumber,'metro1500FanOn':metro1500FanOn,_e:metro1500Converter,'metro1500ConverterTable':metro1500ConverterTable,'metro1500ConverterEntry':metro1500ConverterEntry,_f:metro1500ConverterNumber,'metro1500RxLoc':metro1500RxLoc,'metro1500TxLoc':metro1500TxLoc,'metro1500TxLocC':metro1500TxLocC,'metro1500TxLocTemp':metro1500TxLocTemp,'metro1500RxRem':metro1500RxRem,'metro1500TxRem':metro1500TxRem,'metro1500TxRemC':metro1500TxRemC,'metro1500TxRemTemp':metro1500TxRemTemp,'metro1500RxRem2':metro1500RxRem2,'metro1500ClockState':metro1500ClockState,'metro1500ClockFreq':metro1500ClockFreq,'metro1500LocLoop':metro1500LocLoop,'metro1500RemLoop':metro1500RemLoop,'metro1500ClockType':metro1500ClockType,'metro1500Switch':metro1500Switch,'metro1500SwitchTable':metro1500SwitchTable,'metro1500SwitchEntry':metro1500SwitchEntry,_g:metro1500SwitchNumber,'metro1500SwitchLine':metro1500SwitchLine,'metro1500SwitchMode':metro1500SwitchMode,'metro1500SwitchLaserOn':metro1500SwitchLaserOn,'metro1500SwitchLineAavail':metro1500SwitchLineAavail,'metro1500SwitchLineBavail':metro1500SwitchLineBavail,'metro1500EthernetHub':metro1500EthernetHub,'metro1500EthernetHubTable':metro1500EthernetHubTable,'metro1500EthernetHubEntry':metro1500EthernetHubEntry,_j:metro1500EthernetHubNumber,'metro1500EthernetHubPortEnable1':metro1500EthernetHubPortEnable1,'metro1500EthernetHubPortPartitionStatus1':metro1500EthernetHubPortPartitionStatus1,'metro1500EthernetHubPortLinkStatus1':metro1500EthernetHubPortLinkStatus1,'metro1500EthernetHubPortPolarity1':metro1500EthernetHubPortPolarity1,'metro1500EthernetHubPortEnable2':metro1500EthernetHubPortEnable2,'metro1500EthernetHubPortPartitionStatus2':metro1500EthernetHubPortPartitionStatus2,'metro1500EthernetHubPortLinkStatus2':metro1500EthernetHubPortLinkStatus2,'metro1500EthernetHubPortPolarity2':metro1500EthernetHubPortPolarity2,'metro1500EthernetHubPortEnable3':metro1500EthernetHubPortEnable3,'metro1500EthernetHubPortPartitionStatus3':metro1500EthernetHubPortPartitionStatus3,'metro1500EthernetHubPortLinkStatus3':metro1500EthernetHubPortLinkStatus3,'metro1500EthernetHubPortPolarity3':metro1500EthernetHubPortPolarity3,'metro1500EthernetHubPortEnable4':metro1500EthernetHubPortEnable4,'metro1500EthernetHubPortPartitionStatus4':metro1500EthernetHubPortPartitionStatus4,'metro1500EthernetHubPortLinkStatus4':metro1500EthernetHubPortLinkStatus4,'metro1500EthernetHubPortPolarity4':metro1500EthernetHubPortPolarity4,'metro1500EthernetHubPortEnable5':metro1500EthernetHubPortEnable5,'metro1500EthernetHubPortPartitionStatus5':metro1500EthernetHubPortPartitionStatus5,'metro1500EthernetHubPortLinkStatus5':metro1500EthernetHubPortLinkStatus5,'metro1500EthernetHubPortPolarity5':metro1500EthernetHubPortPolarity5,'metro1500TDM':metro1500TDM,'metro1500TDMTable':metro1500TDMTable,'metro1500TDMEntry':metro1500TDMEntry,_k:metro1500TDMNumber,'metro1500TDMRxRem':metro1500TDMRxRem,'metro1500TDMRxSync':metro1500TDMRxSync,'metro1500TDMTxRem':metro1500TDMTxRem,'metro1500TDMTxRemC':metro1500TDMTxRemC,'metro1500TDMTxRemTemp':metro1500TDMTxRemTemp,'metro1500TDMLocLoop':metro1500TDMLocLoop,'metro1500TDMLocModuleInst1':metro1500TDMLocModuleInst1,'metro1500TDMLocModuleEnable1':metro1500TDMLocModuleEnable1,'metro1500TDMLocModuleRx1':metro1500TDMLocModuleRx1,'metro1500TDMLocModuleTx1':metro1500TDMLocModuleTx1,'metro1500TDMLocModuleRemoteData1':metro1500TDMLocModuleRemoteData1,'metro1500TDMLocModuleClockFrequency1':metro1500TDMLocModuleClockFrequency1,'metro1500TDMLocModuleClockError1':metro1500TDMLocModuleClockError1,'metro1500TDMLocModuleInst2':metro1500TDMLocModuleInst2,'metro1500TDMLocModuleEnable2':metro1500TDMLocModuleEnable2,'metro1500TDMLocModuleRx2':metro1500TDMLocModuleRx2,'metro1500TDMLocModuleTx2':metro1500TDMLocModuleTx2,'metro1500TDMLocModuleRemoteData2':metro1500TDMLocModuleRemoteData2,'metro1500TDMLocModuleClockFrequency2':metro1500TDMLocModuleClockFrequency2,'metro1500TDMLocModuleClockError2':metro1500TDMLocModuleClockError2,'metro1500TDMLocModuleInst3':metro1500TDMLocModuleInst3,'metro1500TDMLocModuleEnable3':metro1500TDMLocModuleEnable3,'metro1500TDMLocModuleRx3':metro1500TDMLocModuleRx3,'metro1500TDMLocModuleTx3':metro1500TDMLocModuleTx3,'metro1500TDMLocModuleRemoteData3':metro1500TDMLocModuleRemoteData3,'metro1500TDMLocModuleClockFrequency3':metro1500TDMLocModuleClockFrequency3,'metro1500TDMLocModuleClockError3':metro1500TDMLocModuleClockError3,'metro1500TDMLocModuleInst4':metro1500TDMLocModuleInst4,'metro1500TDMLocModuleEnable4':metro1500TDMLocModuleEnable4,'metro1500TDMLocModuleRx4':metro1500TDMLocModuleRx4,'metro1500TDMLocModuleTx4':metro1500TDMLocModuleTx4,'metro1500TDMLocModuleRemoteData4':metro1500TDMLocModuleRemoteData4,'metro1500TDMLocModuleClockFrequency4':metro1500TDMLocModuleClockFrequency4,'metro1500TDMLocModuleClockError4':metro1500TDMLocModuleClockError4,'metro1500Trap':metro1500Trap,'metro1500HardwareAdded':metro1500HardwareAdded,'metro1500HardwareDeleted':metro1500HardwareDeleted,'metro1500PSNotFail':metro1500PSNotFail,'metro1500PSFail':metro1500PSFail,'metro1500FanNotFail':metro1500FanNotFail,'metro1500FanFail':metro1500FanFail,'metro1500BusNotFail':metro1500BusNotFail,'metro1500BusFail':metro1500BusFail,'metro1500RxLocOn':metro1500RxLocOn,'metro1500RxLocOff':metro1500RxLocOff,'metro1500TxLocOn':metro1500TxLocOn,'metro1500TxLocOff':metro1500TxLocOff,'metro1500RxRemOn':metro1500RxRemOn,'metro1500RxRemOff':metro1500RxRemOff,'metro1500TxRemOn':metro1500TxRemOn,'metro1500TxRemOff':metro1500TxRemOff,'metro1500RxRem2On':metro1500RxRem2On,'metro1500RxRem2Off':metro1500RxRem2Off,'metro1500TxRem2On':metro1500TxRem2On,'metro1500TxRem2Off':metro1500TxRem2Off,'metro1500ClockNoFail':metro1500ClockNoFail,'metro1500ClockFail':metro1500ClockFail,'metro1500ClockChangeFrequency':metro1500ClockChangeFrequency,'metro1500LocLoopOn':metro1500LocLoopOn,'metro1500LocLoopOff':metro1500LocLoopOff,'metro1500RemLoopOn':metro1500RemLoopOn,'metro1500RemLoopOff':metro1500RemLoopOff,'metro1500switchReferenceLaserOn':metro1500switchReferenceLaserOn,'metro1500switchReferenceLaserOff':metro1500switchReferenceLaserOff,'metro1500switchToA':metro1500switchToA,'metro1500switchToB':metro1500switchToB,'metro1500switchAutomatic':metro1500switchAutomatic,'metro1500switchLocked':metro1500switchLocked,'metro1500switchLineAavail':metro1500switchLineAavail,'metro1500switchLineANotAvail':metro1500switchLineANotAvail,'metro1500switchLineBavail':metro1500switchLineBavail,'metro1500switchLineBNotAvail':metro1500switchLineBNotAvail,'metro1500repeatedMessage':metro1500repeatedMessage,'metro1500INNCDown':metro1500INNCDown,'metro1500INNCUp':metro1500INNCUp,'metro1500EthernetHubPortEnable':metro1500EthernetHubPortEnable,'metro1500EthernetHubPortDisable':metro1500EthernetHubPortDisable,'metro1500EthernetHubPortPartitioned':metro1500EthernetHubPortPartitioned,'metro1500EthernetHubPortNotPartitioned':metro1500EthernetHubPortNotPartitioned,'metro1500EthernetHubPortLinkPulses':metro1500EthernetHubPortLinkPulses,'metro1500EthernetHubPortNoLinkPulses':metro1500EthernetHubPortNoLinkPulses,'metro1500TDMRemoteSyncLoss':metro1500TDMRemoteSyncLoss,'metro1500TDMRemoteSync':metro1500TDMRemoteSync,'metro1500TDMLocModuleEnabled1':metro1500TDMLocModuleEnabled1,'metro1500TDMLocModuleDisable1':metro1500TDMLocModuleDisable1,'metro1500TDMLocModuleEnabled2':metro1500TDMLocModuleEnabled2,'metro1500TDMLocModuleDisable2':metro1500TDMLocModuleDisable2,'metro1500TDMLocModuleEnabled3':metro1500TDMLocModuleEnabled3,'metro1500TDMLocModuleDisable3':metro1500TDMLocModuleDisable3,'metro1500TDMLocModuleEnabled4':metro1500TDMLocModuleEnabled4,'metro1500TDMLocModuleDisable4':metro1500TDMLocModuleDisable4,'metro1500TDMLocModuleRxOn1':metro1500TDMLocModuleRxOn1,'metro1500TDMLocModuleRxOff1':metro1500TDMLocModuleRxOff1,'metro1500TDMLocModuleRxOn2':metro1500TDMLocModuleRxOn2,'metro1500TDMLocModuleRxOff2':metro1500TDMLocModuleRxOff2,'metro1500TDMLocModuleRxOn3':metro1500TDMLocModuleRxOn3,'metro1500TDMLocModuleRxOff3':metro1500TDMLocModuleRxOff3,'metro1500TDMLocModuleRxOn4':metro1500TDMLocModuleRxOn4,'metro1500TDMLocModuleRxOff4':metro1500TDMLocModuleRxOff4,'metro1500TDMLocModuleData1':metro1500TDMLocModuleData1,'metro1500TDMLocModuleNoData1':metro1500TDMLocModuleNoData1,'metro1500TDMLocModuleData2':metro1500TDMLocModuleData2,'metro1500TDMLocModuleNoData2':metro1500TDMLocModuleNoData2,'metro1500TDMLocModuleData3':metro1500TDMLocModuleData3,'metro1500TDMLocModuleNoData3':metro1500TDMLocModuleNoData3,'metro1500TDMLocModuleData4':metro1500TDMLocModuleData4,'metro1500TDMLocModuleNoData4':metro1500TDMLocModuleNoData4,'metro1500TDMLocModuleClockFail1':metro1500TDMLocModuleClockFail1,'metro1500TDMLocModuleClockNoFail1':metro1500TDMLocModuleClockNoFail1,'metro1500TDMLocModuleClockFail2':metro1500TDMLocModuleClockFail2,'metro1500TDMLocModuleClockNoFail2':metro1500TDMLocModuleClockNoFail2,'metro1500TDMLocModuleClockFail3':metro1500TDMLocModuleClockFail3,'metro1500TDMLocModuleClockNoFail3':metro1500TDMLocModuleClockNoFail3,'metro1500TDMLocModuleClockFail4':metro1500TDMLocModuleClockFail4,'metro1500TDMLocModuleClockNoFail4':metro1500TDMLocModuleClockNoFail4})