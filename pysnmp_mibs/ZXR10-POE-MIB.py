_M='portEntryPortIndex'
_L='portEntryGroupIndex'
_K='enable'
_J='disable'
_I='pseGroupIndex'
_H='DisplayString'
_G='read-write'
_F='not-accessible'
_E='ZXR10-POE-MIB'
_D='Watts'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10POE_ObjectIdentity=ObjectIdentity
zxr10POE=_Zxr10POE_ObjectIdentity((1,3,6,1,4,1,3902,3,319))
_PseTable_Object=MibTable
pseTable=_PseTable_Object((1,3,6,1,4,1,3902,3,319,1))
if mibBuilder.loadTexts:pseTable.setStatus(_A)
_PseEntry_Object=MibTableRow
pseEntry=_PseEntry_Object((1,3,6,1,4,1,3902,3,319,1,1))
pseEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:pseEntry.setStatus(_A)
class _PseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PseGroupIndex_Type.__name__=_C
_PseGroupIndex_Object=MibTableColumn
pseGroupIndex=_PseGroupIndex_Object((1,3,6,1,4,1,3902,3,319,1,1,1),_PseGroupIndex_Type())
pseGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pseGroupIndex.setStatus(_A)
class _OverTemperatureAutoRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_OverTemperatureAutoRecovery_Type.__name__=_C
_OverTemperatureAutoRecovery_Object=MibTableColumn
overTemperatureAutoRecovery=_OverTemperatureAutoRecovery_Object((1,3,6,1,4,1,3902,3,319,1,1,2),_OverTemperatureAutoRecovery_Type())
overTemperatureAutoRecovery.setMaxAccess(_G)
if mibBuilder.loadTexts:overTemperatureAutoRecovery.setStatus(_A)
_PsePeakPower_Type=DisplayString
_PsePeakPower_Object=MibTableColumn
psePeakPower=_PsePeakPower_Object((1,3,6,1,4,1,3902,3,319,1,1,3),_PsePeakPower_Type())
psePeakPower.setMaxAccess(_B)
if mibBuilder.loadTexts:psePeakPower.setStatus(_A)
if mibBuilder.loadTexts:psePeakPower.setUnits(_D)
_PsePeakPowerTime_Type=DisplayString
_PsePeakPowerTime_Object=MibTableColumn
psePeakPowerTime=_PsePeakPowerTime_Object((1,3,6,1,4,1,3902,3,319,1,1,4),_PsePeakPowerTime_Type())
psePeakPowerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:psePeakPowerTime.setStatus(_A)
_PseCurrentTemperature_Type=DisplayString
_PseCurrentTemperature_Object=MibTableColumn
pseCurrentTemperature=_PseCurrentTemperature_Object((1,3,6,1,4,1,3902,3,319,1,1,5),_PseCurrentTemperature_Type())
pseCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:pseCurrentTemperature.setStatus(_A)
_PseFirmwareVersion_Type=DisplayString
_PseFirmwareVersion_Object=MibTableColumn
pseFirmwareVersion=_PseFirmwareVersion_Object((1,3,6,1,4,1,3902,3,319,1,1,6),_PseFirmwareVersion_Type())
pseFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pseFirmwareVersion.setStatus(_A)
_PseCriticalPower_Type=DisplayString
_PseCriticalPower_Object=MibTableColumn
pseCriticalPower=_PseCriticalPower_Object((1,3,6,1,4,1,3902,3,319,1,1,7),_PseCriticalPower_Type())
pseCriticalPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pseCriticalPower.setStatus(_A)
if mibBuilder.loadTexts:pseCriticalPower.setUnits(_D)
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,3902,3,319,2))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,3902,3,319,2,1))
portEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
class _PortEntryGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortEntryGroupIndex_Type.__name__=_C
_PortEntryGroupIndex_Object=MibTableColumn
portEntryGroupIndex=_PortEntryGroupIndex_Object((1,3,6,1,4,1,3902,3,319,2,1,1),_PortEntryGroupIndex_Type())
portEntryGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:portEntryGroupIndex.setStatus(_A)
class _PortEntryPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortEntryPortIndex_Type.__name__=_C
_PortEntryPortIndex_Object=MibTableColumn
portEntryPortIndex=_PortEntryPortIndex_Object((1,3,6,1,4,1,3902,3,319,2,1,2),_PortEntryPortIndex_Type())
portEntryPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:portEntryPortIndex.setStatus(_A)
_InterfaceCurrentPower_Type=DisplayString
_InterfaceCurrentPower_Object=MibTableColumn
interfaceCurrentPower=_InterfaceCurrentPower_Object((1,3,6,1,4,1,3902,3,319,2,1,3),_InterfaceCurrentPower_Type())
interfaceCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceCurrentPower.setStatus(_A)
if mibBuilder.loadTexts:interfaceCurrentPower.setUnits(_D)
_InterfaceAvgPower_Type=DisplayString
_InterfaceAvgPower_Object=MibTableColumn
interfaceAvgPower=_InterfaceAvgPower_Object((1,3,6,1,4,1,3902,3,319,2,1,4),_InterfaceAvgPower_Type())
interfaceAvgPower.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceAvgPower.setStatus(_A)
if mibBuilder.loadTexts:interfaceAvgPower.setUnits(_D)
_InterfacePeakPower_Type=DisplayString
_InterfacePeakPower_Object=MibTableColumn
interfacePeakPower=_InterfacePeakPower_Object((1,3,6,1,4,1,3902,3,319,2,1,5),_InterfacePeakPower_Type())
interfacePeakPower.setMaxAccess(_B)
if mibBuilder.loadTexts:interfacePeakPower.setStatus(_A)
if mibBuilder.loadTexts:interfacePeakPower.setUnits(_D)
_InterfacepeakPowerTime_Type=DisplayString
_InterfacepeakPowerTime_Object=MibTableColumn
interfacepeakPowerTime=_InterfacepeakPowerTime_Object((1,3,6,1,4,1,3902,3,319,2,1,6),_InterfacepeakPowerTime_Type())
interfacepeakPowerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:interfacepeakPowerTime.setStatus(_A)
class _EnhancedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_J,1)))
_EnhancedMode_Type.__name__=_C
_EnhancedMode_Object=MibTableColumn
enhancedMode=_EnhancedMode_Object((1,3,6,1,4,1,3902,3,319,2,1,7),_EnhancedMode_Type())
enhancedMode.setMaxAccess(_G)
if mibBuilder.loadTexts:enhancedMode.setStatus(_A)
class _PdMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('fifteen-point-four',0),('four',1),('seven',2),('eighteen',3),('twenty-seven',4),('thirty',5)))
_PdMaxPower_Type.__name__=_C
_PdMaxPower_Object=MibTableColumn
pdMaxPower=_PdMaxPower_Object((1,3,6,1,4,1,3902,3,319,2,1,8),_PdMaxPower_Type())
pdMaxPower.setMaxAccess(_G)
if mibBuilder.loadTexts:pdMaxPower.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_H:DisplayString,'zte':zte,'zxr10':zxr10,'zxr10POE':zxr10POE,'pseTable':pseTable,'pseEntry':pseEntry,_I:pseGroupIndex,'overTemperatureAutoRecovery':overTemperatureAutoRecovery,'psePeakPower':psePeakPower,'psePeakPowerTime':psePeakPowerTime,'pseCurrentTemperature':pseCurrentTemperature,'pseFirmwareVersion':pseFirmwareVersion,'pseCriticalPower':pseCriticalPower,'portTable':portTable,'portEntry':portEntry,_L:portEntryGroupIndex,_M:portEntryPortIndex,'interfaceCurrentPower':interfaceCurrentPower,'interfaceAvgPower':interfaceAvgPower,'interfacePeakPower':interfacePeakPower,'interfacepeakPowerTime':interfacepeakPowerTime,'enhancedMode':enhancedMode,'pdMaxPower':pdMaxPower})