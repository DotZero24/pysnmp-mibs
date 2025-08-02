_G='rlStackHybridUnitId'
_F='RADLAN-HYBRID-STACK-MIB'
_E='Integer32'
_D='OctetString'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
rlStack,=mibBuilder.importSymbols('RADLAN-STACK-MIB','rlStack')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
class StackMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('standalone',1),('native',2),('basic-hybrid',3),('advanced-hybrid',4),('advanced-hybrid-XG',5)))
class PortsPair(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pair-s1s2',1),('pair-s3s4',2),('pair-s1s25G',3),('pair-s1s2Xg',4),('pair-lionXg',5),('pair-s1s2-xg1xg2-Xg',6)))
class HybridStackPortSpeed(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('port-speed-1G',1),('port-speed-5G',2),('port-speed-10G',3),('port-speed-auto',4),('port-speed-down',5)))
class HybridStackDeviceMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mode-L2',1),('mode-L3',2)))
class UnitModuleType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unit-ros_sku1',1),('unit-ros_sku2',2),('unit-ros_sku3',3)))
_RlStackHybridTable_Object=MibTable
rlStackHybridTable=_RlStackHybridTable_Object((1,3,6,1,4,1,89,107,5))
if mibBuilder.loadTexts:rlStackHybridTable.setStatus(_A)
_RlStackHybridEntry_Object=MibTableRow
rlStackHybridEntry=_RlStackHybridEntry_Object((1,3,6,1,4,1,89,107,5,1))
rlStackHybridEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rlStackHybridEntry.setStatus(_A)
class _RlStackHybridUnitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlStackHybridUnitId_Type.__name__=_E
_RlStackHybridUnitId_Object=MibTableColumn
rlStackHybridUnitId=_RlStackHybridUnitId_Object((1,3,6,1,4,1,89,107,5,1,1),_RlStackHybridUnitId_Type())
rlStackHybridUnitId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlStackHybridUnitId.setStatus(_A)
_RlStackHybridStackMode_Type=StackMode
_RlStackHybridStackMode_Object=MibTableColumn
rlStackHybridStackMode=_RlStackHybridStackMode_Object((1,3,6,1,4,1,89,107,5,1,2),_RlStackHybridStackMode_Type())
rlStackHybridStackMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridStackMode.setStatus(_A)
_RlStackHybridPortsPair_Type=PortsPair
_RlStackHybridPortsPair_Object=MibTableColumn
rlStackHybridPortsPair=_RlStackHybridPortsPair_Object((1,3,6,1,4,1,89,107,5,1,3),_RlStackHybridPortsPair_Type())
rlStackHybridPortsPair.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridPortsPair.setStatus(_A)
_RlStackHybridPortNo1speedDeprecated_Type=HybridStackPortSpeed
_RlStackHybridPortNo1speedDeprecated_Object=MibTableColumn
rlStackHybridPortNo1speedDeprecated=_RlStackHybridPortNo1speedDeprecated_Object((1,3,6,1,4,1,89,107,5,1,4),_RlStackHybridPortNo1speedDeprecated_Type())
rlStackHybridPortNo1speedDeprecated.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridPortNo1speedDeprecated.setStatus(_A)
_RlStackHybridPortNo2speedDeprecated_Type=HybridStackPortSpeed
_RlStackHybridPortNo2speedDeprecated_Object=MibTableColumn
rlStackHybridPortNo2speedDeprecated=_RlStackHybridPortNo2speedDeprecated_Object((1,3,6,1,4,1,89,107,5,1,5),_RlStackHybridPortNo2speedDeprecated_Type())
rlStackHybridPortNo2speedDeprecated.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridPortNo2speedDeprecated.setStatus(_A)
class _RlStackHybridUnitIdAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RlStackHybridUnitIdAfterReset_Type.__name__=_E
_RlStackHybridUnitIdAfterReset_Object=MibTableColumn
rlStackHybridUnitIdAfterReset=_RlStackHybridUnitIdAfterReset_Object((1,3,6,1,4,1,89,107,5,1,6),_RlStackHybridUnitIdAfterReset_Type())
rlStackHybridUnitIdAfterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridUnitIdAfterReset.setStatus(_A)
_RlStackHybridStackModeAfterReset_Type=StackMode
_RlStackHybridStackModeAfterReset_Object=MibTableColumn
rlStackHybridStackModeAfterReset=_RlStackHybridStackModeAfterReset_Object((1,3,6,1,4,1,89,107,5,1,7),_RlStackHybridStackModeAfterReset_Type())
rlStackHybridStackModeAfterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridStackModeAfterReset.setStatus(_A)
_RlStackHybridPortsPairAfterReset_Type=PortsPair
_RlStackHybridPortsPairAfterReset_Object=MibTableColumn
rlStackHybridPortsPairAfterReset=_RlStackHybridPortsPairAfterReset_Object((1,3,6,1,4,1,89,107,5,1,8),_RlStackHybridPortsPairAfterReset_Type())
rlStackHybridPortsPairAfterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridPortsPairAfterReset.setStatus(_A)
_RlStackHybridPortNo1speedAfterResetDeprecated_Type=HybridStackPortSpeed
_RlStackHybridPortNo1speedAfterResetDeprecated_Object=MibTableColumn
rlStackHybridPortNo1speedAfterResetDeprecated=_RlStackHybridPortNo1speedAfterResetDeprecated_Object((1,3,6,1,4,1,89,107,5,1,9),_RlStackHybridPortNo1speedAfterResetDeprecated_Type())
rlStackHybridPortNo1speedAfterResetDeprecated.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridPortNo1speedAfterResetDeprecated.setStatus(_A)
_RlStackHybridPortNo2speedAfterResetDeprecated_Type=HybridStackPortSpeed
_RlStackHybridPortNo2speedAfterResetDeprecated_Object=MibTableColumn
rlStackHybridPortNo2speedAfterResetDeprecated=_RlStackHybridPortNo2speedAfterResetDeprecated_Object((1,3,6,1,4,1,89,107,5,1,10),_RlStackHybridPortNo2speedAfterResetDeprecated_Type())
rlStackHybridPortNo2speedAfterResetDeprecated.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridPortNo2speedAfterResetDeprecated.setStatus(_A)
_RlStackHybridDeleteStartupAfterResetDeprecated_Type=TruthValue
_RlStackHybridDeleteStartupAfterResetDeprecated_Object=MibTableColumn
rlStackHybridDeleteStartupAfterResetDeprecated=_RlStackHybridDeleteStartupAfterResetDeprecated_Object((1,3,6,1,4,1,89,107,5,1,11),_RlStackHybridDeleteStartupAfterResetDeprecated_Type())
rlStackHybridDeleteStartupAfterResetDeprecated.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridDeleteStartupAfterResetDeprecated.setStatus(_A)
_RlStackHybridDeviceModeAfterReset_Type=HybridStackDeviceMode
_RlStackHybridDeviceModeAfterReset_Object=MibTableColumn
rlStackHybridDeviceModeAfterReset=_RlStackHybridDeviceModeAfterReset_Object((1,3,6,1,4,1,89,107,5,1,12),_RlStackHybridDeviceModeAfterReset_Type())
rlStackHybridDeviceModeAfterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridDeviceModeAfterReset.setStatus(_A)
_RlStackHybridXgPortNo1NumDeprecated_Type=Integer32
_RlStackHybridXgPortNo1NumDeprecated_Object=MibTableColumn
rlStackHybridXgPortNo1NumDeprecated=_RlStackHybridXgPortNo1NumDeprecated_Object((1,3,6,1,4,1,89,107,5,1,13),_RlStackHybridXgPortNo1NumDeprecated_Type())
rlStackHybridXgPortNo1NumDeprecated.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridXgPortNo1NumDeprecated.setStatus(_A)
_RlStackHybridXgPortNo1NumAfterResetDeprecated_Type=Integer32
_RlStackHybridXgPortNo1NumAfterResetDeprecated_Object=MibTableColumn
rlStackHybridXgPortNo1NumAfterResetDeprecated=_RlStackHybridXgPortNo1NumAfterResetDeprecated_Object((1,3,6,1,4,1,89,107,5,1,14),_RlStackHybridXgPortNo1NumAfterResetDeprecated_Type())
rlStackHybridXgPortNo1NumAfterResetDeprecated.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridXgPortNo1NumAfterResetDeprecated.setStatus(_A)
_RlStackHybridXgPortNo2NumDeprecated_Type=Integer32
_RlStackHybridXgPortNo2NumDeprecated_Object=MibTableColumn
rlStackHybridXgPortNo2NumDeprecated=_RlStackHybridXgPortNo2NumDeprecated_Object((1,3,6,1,4,1,89,107,5,1,15),_RlStackHybridXgPortNo2NumDeprecated_Type())
rlStackHybridXgPortNo2NumDeprecated.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridXgPortNo2NumDeprecated.setStatus(_A)
_RlStackHybridXgPortNo2NumAfterResetDeprecated_Type=Integer32
_RlStackHybridXgPortNo2NumAfterResetDeprecated_Object=MibTableColumn
rlStackHybridXgPortNo2NumAfterResetDeprecated=_RlStackHybridXgPortNo2NumAfterResetDeprecated_Object((1,3,6,1,4,1,89,107,5,1,16),_RlStackHybridXgPortNo2NumAfterResetDeprecated_Type())
rlStackHybridXgPortNo2NumAfterResetDeprecated.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridXgPortNo2NumAfterResetDeprecated.setStatus(_A)
_RlStackHybridPortSpeed_Type=HybridStackPortSpeed
_RlStackHybridPortSpeed_Object=MibTableColumn
rlStackHybridPortSpeed=_RlStackHybridPortSpeed_Object((1,3,6,1,4,1,89,107,5,1,17),_RlStackHybridPortSpeed_Type())
rlStackHybridPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridPortSpeed.setStatus(_A)
_RlStackHybridPortSpeedAfterReset_Type=HybridStackPortSpeed
_RlStackHybridPortSpeedAfterReset_Object=MibTableColumn
rlStackHybridPortSpeedAfterReset=_RlStackHybridPortSpeedAfterReset_Object((1,3,6,1,4,1,89,107,5,1,18),_RlStackHybridPortSpeedAfterReset_Type())
rlStackHybridPortSpeedAfterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridPortSpeedAfterReset.setStatus(_A)
class _RlStackHybridXgPortList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,16))
_RlStackHybridXgPortList_Type.__name__=_D
_RlStackHybridXgPortList_Object=MibTableColumn
rlStackHybridXgPortList=_RlStackHybridXgPortList_Object((1,3,6,1,4,1,89,107,5,1,19),_RlStackHybridXgPortList_Type())
rlStackHybridXgPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridXgPortList.setStatus(_A)
class _RlStackHybridXgPortListAfterReset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,16))
_RlStackHybridXgPortListAfterReset_Type.__name__=_D
_RlStackHybridXgPortListAfterReset_Object=MibTableColumn
rlStackHybridXgPortListAfterReset=_RlStackHybridXgPortListAfterReset_Object((1,3,6,1,4,1,89,107,5,1,20),_RlStackHybridXgPortListAfterReset_Type())
rlStackHybridXgPortListAfterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridXgPortListAfterReset.setStatus(_A)
_RlStackHybridUnitModuleType_Type=UnitModuleType
_RlStackHybridUnitModuleType_Object=MibTableColumn
rlStackHybridUnitModuleType=_RlStackHybridUnitModuleType_Object((1,3,6,1,4,1,89,107,5,1,21),_RlStackHybridUnitModuleType_Type())
rlStackHybridUnitModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStackHybridUnitModuleType.setStatus(_A)
_RlStackHybridMibVersion_Type=Integer32
_RlStackHybridMibVersion_Object=MibTableColumn
rlStackHybridMibVersion=_RlStackHybridMibVersion_Object((1,3,6,1,4,1,89,107,5,1,22),_RlStackHybridMibVersion_Type())
rlStackHybridMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlStackHybridMibVersion.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'StackMode':StackMode,'PortsPair':PortsPair,'HybridStackPortSpeed':HybridStackPortSpeed,'HybridStackDeviceMode':HybridStackDeviceMode,'UnitModuleType':UnitModuleType,'rlStackHybridTable':rlStackHybridTable,'rlStackHybridEntry':rlStackHybridEntry,_G:rlStackHybridUnitId,'rlStackHybridStackMode':rlStackHybridStackMode,'rlStackHybridPortsPair':rlStackHybridPortsPair,'rlStackHybridPortNo1speedDeprecated':rlStackHybridPortNo1speedDeprecated,'rlStackHybridPortNo2speedDeprecated':rlStackHybridPortNo2speedDeprecated,'rlStackHybridUnitIdAfterReset':rlStackHybridUnitIdAfterReset,'rlStackHybridStackModeAfterReset':rlStackHybridStackModeAfterReset,'rlStackHybridPortsPairAfterReset':rlStackHybridPortsPairAfterReset,'rlStackHybridPortNo1speedAfterResetDeprecated':rlStackHybridPortNo1speedAfterResetDeprecated,'rlStackHybridPortNo2speedAfterResetDeprecated':rlStackHybridPortNo2speedAfterResetDeprecated,'rlStackHybridDeleteStartupAfterResetDeprecated':rlStackHybridDeleteStartupAfterResetDeprecated,'rlStackHybridDeviceModeAfterReset':rlStackHybridDeviceModeAfterReset,'rlStackHybridXgPortNo1NumDeprecated':rlStackHybridXgPortNo1NumDeprecated,'rlStackHybridXgPortNo1NumAfterResetDeprecated':rlStackHybridXgPortNo1NumAfterResetDeprecated,'rlStackHybridXgPortNo2NumDeprecated':rlStackHybridXgPortNo2NumDeprecated,'rlStackHybridXgPortNo2NumAfterResetDeprecated':rlStackHybridXgPortNo2NumAfterResetDeprecated,'rlStackHybridPortSpeed':rlStackHybridPortSpeed,'rlStackHybridPortSpeedAfterReset':rlStackHybridPortSpeedAfterReset,'rlStackHybridXgPortList':rlStackHybridXgPortList,'rlStackHybridXgPortListAfterReset':rlStackHybridXgPortListAfterReset,'rlStackHybridUnitModuleType':rlStackHybridUnitModuleType,'rlStackHybridMibVersion':rlStackHybridMibVersion})