_L='EltHardwareLedUnitIdModeType'
_K='read-only'
_J='eltHardwareInterfaceIndex'
_I='eltHardwareSerdesTxConfigLaneNumber'
_H='eltHardwareSerdesTxConfigIfIndex'
_G='eltHardwareSerdesRxConfigLaneNumber'
_F='eltHardwareSerdesRxConfigIfIndex'
_E='TruthValue'
_D='ELTEX-MES-HARDWARE-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,eltMesHardwareMib=mibBuilder.importSymbols('ELTEX-MES','eltMes','eltMesHardwareMib')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
class EltHardwareLedUnitIdModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stack',1),('poe',2)))
class EltBreakoutMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('mode-4x10',2)))
_EltMesHardwareMibMIBObjects_ObjectIdentity=ObjectIdentity
eltMesHardwareMibMIBObjects=_EltMesHardwareMibMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,14,1))
_EltMesHardwareConfig_ObjectIdentity=ObjectIdentity
eltMesHardwareConfig=_EltMesHardwareConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,14,1,1))
_EltMesHardwareSerdesConfig_ObjectIdentity=ObjectIdentity
eltMesHardwareSerdesConfig=_EltMesHardwareSerdesConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,14,1,1,1))
_EltHardwareSerdesRxConfigTable_Object=MibTable
eltHardwareSerdesRxConfigTable=_EltHardwareSerdesRxConfigTable_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1))
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigTable.setStatus(_A)
_EltHardwareSerdesRxConfigEntry_Object=MibTableRow
eltHardwareSerdesRxConfigEntry=_EltHardwareSerdesRxConfigEntry_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1))
eltHardwareSerdesRxConfigEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigEntry.setStatus(_A)
_EltHardwareSerdesRxConfigIfIndex_Type=Integer32
_EltHardwareSerdesRxConfigIfIndex_Object=MibTableColumn
eltHardwareSerdesRxConfigIfIndex=_EltHardwareSerdesRxConfigIfIndex_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1,1),_EltHardwareSerdesRxConfigIfIndex_Type())
eltHardwareSerdesRxConfigIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigIfIndex.setStatus(_A)
_EltHardwareSerdesRxConfigLaneNumber_Type=Integer32
_EltHardwareSerdesRxConfigLaneNumber_Object=MibTableColumn
eltHardwareSerdesRxConfigLaneNumber=_EltHardwareSerdesRxConfigLaneNumber_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1,2),_EltHardwareSerdesRxConfigLaneNumber_Type())
eltHardwareSerdesRxConfigLaneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigLaneNumber.setStatus(_A)
class _EltHardwareSerdesRxConfigUserParamsEnable_Type(TruthValue):defaultValue=2
_EltHardwareSerdesRxConfigUserParamsEnable_Type.__name__=_E
_EltHardwareSerdesRxConfigUserParamsEnable_Object=MibTableColumn
eltHardwareSerdesRxConfigUserParamsEnable=_EltHardwareSerdesRxConfigUserParamsEnable_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1,3),_EltHardwareSerdesRxConfigUserParamsEnable_Type())
eltHardwareSerdesRxConfigUserParamsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigUserParamsEnable.setStatus(_A)
class _EltHardwareSerdesRxConfigSquelch_Type(Integer32):defaultValue=0
_EltHardwareSerdesRxConfigSquelch_Type.__name__=_C
_EltHardwareSerdesRxConfigSquelch_Object=MibTableColumn
eltHardwareSerdesRxConfigSquelch=_EltHardwareSerdesRxConfigSquelch_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1,4),_EltHardwareSerdesRxConfigSquelch_Type())
eltHardwareSerdesRxConfigSquelch.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigSquelch.setStatus(_A)
class _EltHardwareSerdesRxConfigFFEResistor_Type(Integer32):defaultValue=0
_EltHardwareSerdesRxConfigFFEResistor_Type.__name__=_C
_EltHardwareSerdesRxConfigFFEResistor_Object=MibTableColumn
eltHardwareSerdesRxConfigFFEResistor=_EltHardwareSerdesRxConfigFFEResistor_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1,5),_EltHardwareSerdesRxConfigFFEResistor_Type())
eltHardwareSerdesRxConfigFFEResistor.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigFFEResistor.setStatus(_A)
class _EltHardwareSerdesRxConfigFFECapacitor_Type(Integer32):defaultValue=0
_EltHardwareSerdesRxConfigFFECapacitor_Type.__name__=_C
_EltHardwareSerdesRxConfigFFECapacitor_Object=MibTableColumn
eltHardwareSerdesRxConfigFFECapacitor=_EltHardwareSerdesRxConfigFFECapacitor_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1,6),_EltHardwareSerdesRxConfigFFECapacitor_Type())
eltHardwareSerdesRxConfigFFECapacitor.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigFFECapacitor.setStatus(_A)
class _EltHardwareSerdesRxConfigAlign90_Type(Integer32):defaultValue=0
_EltHardwareSerdesRxConfigAlign90_Type.__name__=_C
_EltHardwareSerdesRxConfigAlign90_Object=MibTableColumn
eltHardwareSerdesRxConfigAlign90=_EltHardwareSerdesRxConfigAlign90_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,1,1,7),_EltHardwareSerdesRxConfigAlign90_Type())
eltHardwareSerdesRxConfigAlign90.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesRxConfigAlign90.setStatus(_A)
_EltHardwareSerdesTxConfigTable_Object=MibTable
eltHardwareSerdesTxConfigTable=_EltHardwareSerdesTxConfigTable_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2))
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigTable.setStatus(_A)
_EltHardwareSerdesTxConfigEntry_Object=MibTableRow
eltHardwareSerdesTxConfigEntry=_EltHardwareSerdesTxConfigEntry_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1))
eltHardwareSerdesTxConfigEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigEntry.setStatus(_A)
_EltHardwareSerdesTxConfigIfIndex_Type=Integer32
_EltHardwareSerdesTxConfigIfIndex_Object=MibTableColumn
eltHardwareSerdesTxConfigIfIndex=_EltHardwareSerdesTxConfigIfIndex_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,1),_EltHardwareSerdesTxConfigIfIndex_Type())
eltHardwareSerdesTxConfigIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigIfIndex.setStatus(_A)
_EltHardwareSerdesTxConfigLaneNumber_Type=Integer32
_EltHardwareSerdesTxConfigLaneNumber_Object=MibTableColumn
eltHardwareSerdesTxConfigLaneNumber=_EltHardwareSerdesTxConfigLaneNumber_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,2),_EltHardwareSerdesTxConfigLaneNumber_Type())
eltHardwareSerdesTxConfigLaneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigLaneNumber.setStatus(_A)
class _EltHardwareSerdesTxConfigUserParamsEnable_Type(TruthValue):defaultValue=2
_EltHardwareSerdesTxConfigUserParamsEnable_Type.__name__=_E
_EltHardwareSerdesTxConfigUserParamsEnable_Object=MibTableColumn
eltHardwareSerdesTxConfigUserParamsEnable=_EltHardwareSerdesTxConfigUserParamsEnable_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,3),_EltHardwareSerdesTxConfigUserParamsEnable_Type())
eltHardwareSerdesTxConfigUserParamsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigUserParamsEnable.setStatus(_A)
class _EltHardwareSerdesTxConfigAmplitude_Type(Integer32):defaultValue=0
_EltHardwareSerdesTxConfigAmplitude_Type.__name__=_C
_EltHardwareSerdesTxConfigAmplitude_Object=MibTableColumn
eltHardwareSerdesTxConfigAmplitude=_EltHardwareSerdesTxConfigAmplitude_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,4),_EltHardwareSerdesTxConfigAmplitude_Type())
eltHardwareSerdesTxConfigAmplitude.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigAmplitude.setStatus(_A)
class _EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Type(TruthValue):defaultValue=2
_EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Type.__name__=_E
_EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Object=MibTableColumn
eltHardwareSerdesTxConfigAmplitudeAdjustEnable=_EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,5),_EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Type())
eltHardwareSerdesTxConfigAmplitudeAdjustEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigAmplitudeAdjustEnable.setStatus(_A)
class _EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Type(Integer32):defaultValue=0
_EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Type.__name__=_C
_EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Object=MibTableColumn
eltHardwareSerdesTxConfigEmphasisAmplitudeGen0=_EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,6),_EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Type())
eltHardwareSerdesTxConfigEmphasisAmplitudeGen0.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigEmphasisAmplitudeGen0.setStatus(_A)
class _EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Type(Integer32):defaultValue=0
_EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Type.__name__=_C
_EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Object=MibTableColumn
eltHardwareSerdesTxConfigEmphasisAmplitudeGen1=_EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,7),_EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Type())
eltHardwareSerdesTxConfigEmphasisAmplitudeGen1.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigEmphasisAmplitudeGen1.setStatus(_A)
class _EltHardwareSerdesTxConfigAmplitudeShiftEnable_Type(TruthValue):defaultValue=2
_EltHardwareSerdesTxConfigAmplitudeShiftEnable_Type.__name__=_E
_EltHardwareSerdesTxConfigAmplitudeShiftEnable_Object=MibTableColumn
eltHardwareSerdesTxConfigAmplitudeShiftEnable=_EltHardwareSerdesTxConfigAmplitudeShiftEnable_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,2,1,8),_EltHardwareSerdesTxConfigAmplitudeShiftEnable_Type())
eltHardwareSerdesTxConfigAmplitudeShiftEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareSerdesTxConfigAmplitudeShiftEnable.setStatus(_A)
_EltHardwareInterfaceTable_Object=MibTable
eltHardwareInterfaceTable=_EltHardwareInterfaceTable_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,3))
if mibBuilder.loadTexts:eltHardwareInterfaceTable.setStatus(_A)
_EltHardwareInterfaceEntry_Object=MibTableRow
eltHardwareInterfaceEntry=_EltHardwareInterfaceEntry_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,3,1))
eltHardwareInterfaceEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:eltHardwareInterfaceEntry.setStatus(_A)
_EltHardwareInterfaceIndex_Type=InterfaceIndex
_EltHardwareInterfaceIndex_Object=MibTableColumn
eltHardwareInterfaceIndex=_EltHardwareInterfaceIndex_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,3,1,1),_EltHardwareInterfaceIndex_Type())
eltHardwareInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareInterfaceIndex.setStatus(_A)
_EltHardwareInterfaceBreakoutModeAfterReset_Type=EltBreakoutMode
_EltHardwareInterfaceBreakoutModeAfterReset_Object=MibTableColumn
eltHardwareInterfaceBreakoutModeAfterReset=_EltHardwareInterfaceBreakoutModeAfterReset_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,3,1,2),_EltHardwareInterfaceBreakoutModeAfterReset_Type())
eltHardwareInterfaceBreakoutModeAfterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareInterfaceBreakoutModeAfterReset.setStatus(_A)
_EltHardwareInterfaceBreakoutMode_Type=EltBreakoutMode
_EltHardwareInterfaceBreakoutMode_Object=MibTableColumn
eltHardwareInterfaceBreakoutMode=_EltHardwareInterfaceBreakoutMode_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,3,1,3),_EltHardwareInterfaceBreakoutMode_Type())
eltHardwareInterfaceBreakoutMode.setMaxAccess(_K)
if mibBuilder.loadTexts:eltHardwareInterfaceBreakoutMode.setStatus(_A)
_EltHardwareInterfaceBreakoutPortList_Type=PortList
_EltHardwareInterfaceBreakoutPortList_Object=MibTableColumn
eltHardwareInterfaceBreakoutPortList=_EltHardwareInterfaceBreakoutPortList_Object((1,3,6,1,4,1,35265,1,23,14,1,1,1,3,1,4),_EltHardwareInterfaceBreakoutPortList_Type())
eltHardwareInterfaceBreakoutPortList.setMaxAccess(_K)
if mibBuilder.loadTexts:eltHardwareInterfaceBreakoutPortList.setStatus(_A)
_EltMesHardwareLedConfig_ObjectIdentity=ObjectIdentity
eltMesHardwareLedConfig=_EltMesHardwareLedConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,14,1,1,2))
class _EltHardwareLedConfigUnitIdMode_Type(EltHardwareLedUnitIdModeType):defaultValue=1
_EltHardwareLedConfigUnitIdMode_Type.__name__=_L
_EltHardwareLedConfigUnitIdMode_Object=MibScalar
eltHardwareLedConfigUnitIdMode=_EltHardwareLedConfigUnitIdMode_Object((1,3,6,1,4,1,35265,1,23,14,1,1,2,1),_EltHardwareLedConfigUnitIdMode_Type())
eltHardwareLedConfigUnitIdMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltHardwareLedConfigUnitIdMode.setStatus(_A)
_EltMesHardwareStatus_ObjectIdentity=ObjectIdentity
eltMesHardwareStatus=_EltMesHardwareStatus_ObjectIdentity((1,3,6,1,4,1,35265,1,23,14,1,2))
_EltMesHardwareSerdesStatus_ObjectIdentity=ObjectIdentity
eltMesHardwareSerdesStatus=_EltMesHardwareSerdesStatus_ObjectIdentity((1,3,6,1,4,1,35265,1,23,14,1,2,1))
mibBuilder.exportSymbols(_D,**{_L:EltHardwareLedUnitIdModeType,'EltBreakoutMode':EltBreakoutMode,'eltMesHardwareMibMIBObjects':eltMesHardwareMibMIBObjects,'eltMesHardwareConfig':eltMesHardwareConfig,'eltMesHardwareSerdesConfig':eltMesHardwareSerdesConfig,'eltHardwareSerdesRxConfigTable':eltHardwareSerdesRxConfigTable,'eltHardwareSerdesRxConfigEntry':eltHardwareSerdesRxConfigEntry,_F:eltHardwareSerdesRxConfigIfIndex,_G:eltHardwareSerdesRxConfigLaneNumber,'eltHardwareSerdesRxConfigUserParamsEnable':eltHardwareSerdesRxConfigUserParamsEnable,'eltHardwareSerdesRxConfigSquelch':eltHardwareSerdesRxConfigSquelch,'eltHardwareSerdesRxConfigFFEResistor':eltHardwareSerdesRxConfigFFEResistor,'eltHardwareSerdesRxConfigFFECapacitor':eltHardwareSerdesRxConfigFFECapacitor,'eltHardwareSerdesRxConfigAlign90':eltHardwareSerdesRxConfigAlign90,'eltHardwareSerdesTxConfigTable':eltHardwareSerdesTxConfigTable,'eltHardwareSerdesTxConfigEntry':eltHardwareSerdesTxConfigEntry,_H:eltHardwareSerdesTxConfigIfIndex,_I:eltHardwareSerdesTxConfigLaneNumber,'eltHardwareSerdesTxConfigUserParamsEnable':eltHardwareSerdesTxConfigUserParamsEnable,'eltHardwareSerdesTxConfigAmplitude':eltHardwareSerdesTxConfigAmplitude,'eltHardwareSerdesTxConfigAmplitudeAdjustEnable':eltHardwareSerdesTxConfigAmplitudeAdjustEnable,'eltHardwareSerdesTxConfigEmphasisAmplitudeGen0':eltHardwareSerdesTxConfigEmphasisAmplitudeGen0,'eltHardwareSerdesTxConfigEmphasisAmplitudeGen1':eltHardwareSerdesTxConfigEmphasisAmplitudeGen1,'eltHardwareSerdesTxConfigAmplitudeShiftEnable':eltHardwareSerdesTxConfigAmplitudeShiftEnable,'eltHardwareInterfaceTable':eltHardwareInterfaceTable,'eltHardwareInterfaceEntry':eltHardwareInterfaceEntry,_J:eltHardwareInterfaceIndex,'eltHardwareInterfaceBreakoutModeAfterReset':eltHardwareInterfaceBreakoutModeAfterReset,'eltHardwareInterfaceBreakoutMode':eltHardwareInterfaceBreakoutMode,'eltHardwareInterfaceBreakoutPortList':eltHardwareInterfaceBreakoutPortList,'eltMesHardwareLedConfig':eltMesHardwareLedConfig,'eltHardwareLedConfigUnitIdMode':eltHardwareLedConfigUnitIdMode,'eltMesHardwareStatus':eltMesHardwareStatus,'eltMesHardwareSerdesStatus':eltMesHardwareSerdesStatus})