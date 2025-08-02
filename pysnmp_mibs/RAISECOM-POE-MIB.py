_K='rcMainPseModuleOverTemp'
_J='RAISECOM-POE-MIB'
_I='pethPsePortIndex'
_H='pethPsePortGroupIndex'
_G='pethMainPseGroupIndex'
_F='OctetString'
_E='POWER-ETHERNET-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
pethMainPseGroupIndex,pethPsePortGroupIndex,pethPsePortIndex=mibBuilder.importSymbols(_E,_G,_H,_I)
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcPoe=ModuleIdentity((1,3,6,1,4,1,8886,6,1,51))
if mibBuilder.loadTexts:rcPoe.setRevisions(('2007-11-02 00:00',))
_RcPsePortTable_Object=MibTable
rcPsePortTable=_RcPsePortTable_Object((1,3,6,1,4,1,8886,6,1,51,1))
if mibBuilder.loadTexts:rcPsePortTable.setStatus(_A)
_RcPsePortEntry_Object=MibTableRow
rcPsePortEntry=_RcPsePortEntry_Object((1,3,6,1,4,1,8886,6,1,51,1,1))
rcPsePortEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:rcPsePortEntry.setStatus(_A)
_RcPsePortPeakPower_Type=Unsigned32
_RcPsePortPeakPower_Object=MibTableColumn
rcPsePortPeakPower=_RcPsePortPeakPower_Object((1,3,6,1,4,1,8886,6,1,51,1,1,1),_RcPsePortPeakPower_Type())
rcPsePortPeakPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPsePortPeakPower.setStatus(_A)
_RcPsePortAveragePower_Type=Unsigned32
_RcPsePortAveragePower_Object=MibTableColumn
rcPsePortAveragePower=_RcPsePortAveragePower_Object((1,3,6,1,4,1,8886,6,1,51,1,1,2),_RcPsePortAveragePower_Type())
rcPsePortAveragePower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPsePortAveragePower.setStatus(_A)
_RcPsePortCurrentPower_Type=Unsigned32
_RcPsePortCurrentPower_Object=MibTableColumn
rcPsePortCurrentPower=_RcPsePortCurrentPower_Object((1,3,6,1,4,1,8886,6,1,51,1,1,3),_RcPsePortCurrentPower_Type())
rcPsePortCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPsePortCurrentPower.setStatus(_A)
_RcPsePortCurrentVoltage_Type=Unsigned32
_RcPsePortCurrentVoltage_Object=MibTableColumn
rcPsePortCurrentVoltage=_RcPsePortCurrentVoltage_Object((1,3,6,1,4,1,8886,6,1,51,1,1,4),_RcPsePortCurrentVoltage_Type())
rcPsePortCurrentVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPsePortCurrentVoltage.setStatus(_A)
_RcPsePortCurrent_Type=Unsigned32
_RcPsePortCurrent_Object=MibTableColumn
rcPsePortCurrent=_RcPsePortCurrent_Object((1,3,6,1,4,1,8886,6,1,51,1,1,5),_RcPsePortCurrent_Type())
rcPsePortCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPsePortCurrent.setStatus(_A)
_RcPsePortPowerLimit_Type=Unsigned32
_RcPsePortPowerLimit_Object=MibTableColumn
rcPsePortPowerLimit=_RcPsePortPowerLimit_Object((1,3,6,1,4,1,8886,6,1,51,1,1,6),_RcPsePortPowerLimit_Type())
rcPsePortPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPsePortPowerLimit.setStatus(_A)
class _RcPsePortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),('force-power',3)))
_RcPsePortOperStatus_Type.__name__=_D
_RcPsePortOperStatus_Object=MibTableColumn
rcPsePortOperStatus=_RcPsePortOperStatus_Object((1,3,6,1,4,1,8886,6,1,51,1,1,7),_RcPsePortOperStatus_Type())
rcPsePortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPsePortOperStatus.setStatus(_A)
_RcPsePortForcePower_Type=EnableVar
_RcPsePortForcePower_Object=MibTableColumn
rcPsePortForcePower=_RcPsePortForcePower_Object((1,3,6,1,4,1,8886,6,1,51,1,1,8),_RcPsePortForcePower_Type())
rcPsePortForcePower.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPsePortForcePower.setStatus(_A)
class _RcPsePortPoeProtectStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_RcPsePortPoeProtectStatus_Type.__name__=_F
_RcPsePortPoeProtectStatus_Object=MibTableColumn
rcPsePortPoeProtectStatus=_RcPsePortPoeProtectStatus_Object((1,3,6,1,4,1,8886,6,1,51,1,1,9),_RcPsePortPoeProtectStatus_Type())
rcPsePortPoeProtectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPsePortPoeProtectStatus.setStatus(_A)
_RcMainPseTable_Object=MibTable
rcMainPseTable=_RcMainPseTable_Object((1,3,6,1,4,1,8886,6,1,51,2))
if mibBuilder.loadTexts:rcMainPseTable.setStatus(_A)
_RcMainPseEntry_Object=MibTableRow
rcMainPseEntry=_RcMainPseEntry_Object((1,3,6,1,4,1,8886,6,1,51,2,1))
rcMainPseEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:rcMainPseEntry.setStatus(_A)
_RcMainPseAveragePower_Type=Unsigned32
_RcMainPseAveragePower_Object=MibTableColumn
rcMainPseAveragePower=_RcMainPseAveragePower_Object((1,3,6,1,4,1,8886,6,1,51,2,1,1),_RcMainPseAveragePower_Type())
rcMainPseAveragePower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMainPseAveragePower.setStatus(_A)
_RcMainPsePeakPower_Type=Unsigned32
_RcMainPsePeakPower_Object=MibTableColumn
rcMainPsePeakPower=_RcMainPsePeakPower_Object((1,3,6,1,4,1,8886,6,1,51,2,1,2),_RcMainPsePeakPower_Type())
rcMainPsePeakPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMainPsePeakPower.setStatus(_A)
_RcMainPseLegacyDetectionEnable_Type=EnableVar
_RcMainPseLegacyDetectionEnable_Object=MibTableColumn
rcMainPseLegacyDetectionEnable=_RcMainPseLegacyDetectionEnable_Object((1,3,6,1,4,1,8886,6,1,51,2,1,3),_RcMainPseLegacyDetectionEnable_Type())
rcMainPseLegacyDetectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMainPseLegacyDetectionEnable.setStatus(_A)
class _RcMainPseManageMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_RcMainPseManageMode_Type.__name__=_D
_RcMainPseManageMode_Object=MibTableColumn
rcMainPseManageMode=_RcMainPseManageMode_Object((1,3,6,1,4,1,8886,6,1,51,2,1,4),_RcMainPseManageMode_Type())
rcMainPseManageMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMainPseManageMode.setStatus(_A)
_RcMainPseTemperatureProtect_Type=EnableVar
_RcMainPseTemperatureProtect_Object=MibTableColumn
rcMainPseTemperatureProtect=_RcMainPseTemperatureProtect_Object((1,3,6,1,4,1,8886,6,1,51,2,1,5),_RcMainPseTemperatureProtect_Type())
rcMainPseTemperatureProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMainPseTemperatureProtect.setStatus(_A)
class _RcMainPseModuleOverTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('alarm',2)))
_RcMainPseModuleOverTemp_Type.__name__=_D
_RcMainPseModuleOverTemp_Object=MibTableColumn
rcMainPseModuleOverTemp=_RcMainPseModuleOverTemp_Object((1,3,6,1,4,1,8886,6,1,51,2,1,6),_RcMainPseModuleOverTemp_Type())
rcMainPseModuleOverTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMainPseModuleOverTemp.setStatus(_A)
_RcMainPseChipSupplyVoltage_Type=Unsigned32
_RcMainPseChipSupplyVoltage_Object=MibTableColumn
rcMainPseChipSupplyVoltage=_RcMainPseChipSupplyVoltage_Object((1,3,6,1,4,1,8886,6,1,51,2,1,7),_RcMainPseChipSupplyVoltage_Type())
rcMainPseChipSupplyVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMainPseChipSupplyVoltage.setStatus(_A)
class _RcMainPseMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('AF',1),('AT',2)))
_RcMainPseMode_Type.__name__=_D
_RcMainPseMode_Object=MibTableColumn
rcMainPseMode=_RcMainPseMode_Object((1,3,6,1,4,1,8886,6,1,51,2,1,8),_RcMainPseMode_Type())
rcMainPseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMainPseMode.setStatus(_A)
_RcMainPseHighInrushEnable_Type=EnableVar
_RcMainPseHighInrushEnable_Object=MibTableColumn
rcMainPseHighInrushEnable=_RcMainPseHighInrushEnable_Object((1,3,6,1,4,1,8886,6,1,51,2,1,9),_RcMainPseHighInrushEnable_Type())
rcMainPseHighInrushEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMainPseHighInrushEnable.setStatus(_A)
class _RcMainPseCurrentProtectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('class',1),('power',2)))
_RcMainPseCurrentProtectMode_Type.__name__=_D
_RcMainPseCurrentProtectMode_Object=MibTableColumn
rcMainPseCurrentProtectMode=_RcMainPseCurrentProtectMode_Object((1,3,6,1,4,1,8886,6,1,51,2,1,10),_RcMainPseCurrentProtectMode_Type())
rcMainPseCurrentProtectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMainPseCurrentProtectMode.setStatus(_A)
_RcPoeNotifications_ObjectIdentity=ObjectIdentity
rcPoeNotifications=_RcPoeNotifications_ObjectIdentity((1,3,6,1,4,1,8886,6,1,51,3))
rcMainPseOverTempreture=NotificationType((1,3,6,1,4,1,8886,6,1,51,3,1))
rcMainPseOverTempreture.setObjects((_J,_K))
if mibBuilder.loadTexts:rcMainPseOverTempreture.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'rcPoe':rcPoe,'rcPsePortTable':rcPsePortTable,'rcPsePortEntry':rcPsePortEntry,'rcPsePortPeakPower':rcPsePortPeakPower,'rcPsePortAveragePower':rcPsePortAveragePower,'rcPsePortCurrentPower':rcPsePortCurrentPower,'rcPsePortCurrentVoltage':rcPsePortCurrentVoltage,'rcPsePortCurrent':rcPsePortCurrent,'rcPsePortPowerLimit':rcPsePortPowerLimit,'rcPsePortOperStatus':rcPsePortOperStatus,'rcPsePortForcePower':rcPsePortForcePower,'rcPsePortPoeProtectStatus':rcPsePortPoeProtectStatus,'rcMainPseTable':rcMainPseTable,'rcMainPseEntry':rcMainPseEntry,'rcMainPseAveragePower':rcMainPseAveragePower,'rcMainPsePeakPower':rcMainPsePeakPower,'rcMainPseLegacyDetectionEnable':rcMainPseLegacyDetectionEnable,'rcMainPseManageMode':rcMainPseManageMode,'rcMainPseTemperatureProtect':rcMainPseTemperatureProtect,_K:rcMainPseModuleOverTemp,'rcMainPseChipSupplyVoltage':rcMainPseChipSupplyVoltage,'rcMainPseMode':rcMainPseMode,'rcMainPseHighInrushEnable':rcMainPseHighInrushEnable,'rcMainPseCurrentProtectMode':rcMainPseCurrentProtectMode,'rcPoeNotifications':rcPoeNotifications,'rcMainPseOverTempreture':rcMainPseOverTempreture})