_X='sechtor100ThermoBOperationalStatus'
_W='sechtor100ThermoAOperationalStatus'
_V='sechtor100ThermoBTemperature'
_U='sechtor100ThermoATemperature'
_T='sechtor100FanOperationalStatus'
_S='s100ThermoBOperationalStatus'
_R='s100ThermoAOperationalStatus'
_Q='s100ThermoBTemperature'
_P='s100ThermoATemperature'
_O='s100FanOperationalStatus'
_N='fanFailure'
_M='operational'
_L='zhoneSlotIndex'
_K='zhoneShelfIndex'
_J='Zhone'
_I='belowLowerThreshold'
_H='overUpperThreshold'
_G='withinOperationalRange'
_F='read-write'
_E='read-only'
_D='ZHONE-SECHTOR100-MIB'
_C='deprecated'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
sechtor100,zhoneModules,zhoneShelfIndex,zhoneSlotIndex=mibBuilder.importSymbols(_J,'sechtor100','zhoneModules',_K,_L)
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
zhoneSechtor100=ModuleIdentity((1,3,6,1,4,1,5504,6,19))
if mibBuilder.loadTexts:zhoneSechtor100.setRevisions(('2001-09-28 10:29','2000-12-27 11:17','2000-12-21 17:00'))
_Sechtor100Environment_ObjectIdentity=ObjectIdentity
sechtor100Environment=_Sechtor100Environment_ObjectIdentity((1,3,6,1,4,1,5504,2,4,1,1))
if mibBuilder.loadTexts:sechtor100Environment.setStatus(_C)
class _S100FanOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_S100FanOperationalStatus_Type.__name__=_A
_S100FanOperationalStatus_Object=MibScalar
s100FanOperationalStatus=_S100FanOperationalStatus_Object((1,3,6,1,4,1,5504,2,4,1,1,1),_S100FanOperationalStatus_Type())
s100FanOperationalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:s100FanOperationalStatus.setStatus(_C)
class _S100ThermoAUpperThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,80))
_S100ThermoAUpperThreshold_Type.__name__=_A
_S100ThermoAUpperThreshold_Object=MibScalar
s100ThermoAUpperThreshold=_S100ThermoAUpperThreshold_Object((1,3,6,1,4,1,5504,2,4,1,1,2),_S100ThermoAUpperThreshold_Type())
s100ThermoAUpperThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:s100ThermoAUpperThreshold.setStatus(_C)
class _S100ThermoBUpperThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,80))
_S100ThermoBUpperThreshold_Type.__name__=_A
_S100ThermoBUpperThreshold_Object=MibScalar
s100ThermoBUpperThreshold=_S100ThermoBUpperThreshold_Object((1,3,6,1,4,1,5504,2,4,1,1,3),_S100ThermoBUpperThreshold_Type())
s100ThermoBUpperThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:s100ThermoBUpperThreshold.setStatus(_C)
class _S10ThermoALowerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,5))
_S10ThermoALowerThreshold_Type.__name__=_A
_S10ThermoALowerThreshold_Object=MibScalar
s10ThermoALowerThreshold=_S10ThermoALowerThreshold_Object((1,3,6,1,4,1,5504,2,4,1,1,4),_S10ThermoALowerThreshold_Type())
s10ThermoALowerThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:s10ThermoALowerThreshold.setStatus(_C)
class _S100ThermoBLowerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,5))
_S100ThermoBLowerThreshold_Type.__name__=_A
_S100ThermoBLowerThreshold_Object=MibScalar
s100ThermoBLowerThreshold=_S100ThermoBLowerThreshold_Object((1,3,6,1,4,1,5504,2,4,1,1,5),_S100ThermoBLowerThreshold_Type())
s100ThermoBLowerThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:s100ThermoBLowerThreshold.setStatus(_C)
class _S100ThermoATemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-55,125))
_S100ThermoATemperature_Type.__name__=_A
_S100ThermoATemperature_Object=MibScalar
s100ThermoATemperature=_S100ThermoATemperature_Object((1,3,6,1,4,1,5504,2,4,1,1,6),_S100ThermoATemperature_Type())
s100ThermoATemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:s100ThermoATemperature.setStatus(_C)
class _S100ThermoBTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-55,125))
_S100ThermoBTemperature_Type.__name__=_A
_S100ThermoBTemperature_Object=MibScalar
s100ThermoBTemperature=_S100ThermoBTemperature_Object((1,3,6,1,4,1,5504,2,4,1,1,7),_S100ThermoBTemperature_Type())
s100ThermoBTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:s100ThermoBTemperature.setStatus(_C)
class _S100ThermoAOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_S100ThermoAOperationalStatus_Type.__name__=_A
_S100ThermoAOperationalStatus_Object=MibScalar
s100ThermoAOperationalStatus=_S100ThermoAOperationalStatus_Object((1,3,6,1,4,1,5504,2,4,1,1,8),_S100ThermoAOperationalStatus_Type())
s100ThermoAOperationalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:s100ThermoAOperationalStatus.setStatus(_C)
class _S100ThermoBOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_S100ThermoBOperationalStatus_Type.__name__=_A
_S100ThermoBOperationalStatus_Object=MibScalar
s100ThermoBOperationalStatus=_S100ThermoBOperationalStatus_Object((1,3,6,1,4,1,5504,2,4,1,1,9),_S100ThermoBOperationalStatus_Type())
s100ThermoBOperationalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:s100ThermoBOperationalStatus.setStatus(_C)
_Sechtor100Traps_ObjectIdentity=ObjectIdentity
sechtor100Traps=_Sechtor100Traps_ObjectIdentity((1,3,6,1,4,1,5504,2,4,1,2))
if mibBuilder.loadTexts:sechtor100Traps.setStatus(_B)
_Sechtor100TrapsPrefix_ObjectIdentity=ObjectIdentity
sechtor100TrapsPrefix=_Sechtor100TrapsPrefix_ObjectIdentity((1,3,6,1,4,1,5504,2,4,1,2,0))
if mibBuilder.loadTexts:sechtor100TrapsPrefix.setStatus(_B)
_Sechtor100ConfigTable_Object=MibTable
sechtor100ConfigTable=_Sechtor100ConfigTable_Object((1,3,6,1,4,1,5504,2,4,1,3))
if mibBuilder.loadTexts:sechtor100ConfigTable.setStatus(_B)
_Sechtor100ConfigEntry_Object=MibTableRow
sechtor100ConfigEntry=_Sechtor100ConfigEntry_Object((1,3,6,1,4,1,5504,2,4,1,3,1))
sechtor100ConfigEntry.setIndexNames((0,_J,_K),(0,_J,_L))
if mibBuilder.loadTexts:sechtor100ConfigEntry.setStatus(_B)
_Sechtor100PeerMacAddress_Type=MacAddress
_Sechtor100PeerMacAddress_Object=MibTableColumn
sechtor100PeerMacAddress=_Sechtor100PeerMacAddress_Object((1,3,6,1,4,1,5504,2,4,1,3,1,1),_Sechtor100PeerMacAddress_Type())
sechtor100PeerMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:sechtor100PeerMacAddress.setStatus(_B)
_Sechtor100RedundancyEnable_Type=TruthValue
_Sechtor100RedundancyEnable_Object=MibTableColumn
sechtor100RedundancyEnable=_Sechtor100RedundancyEnable_Object((1,3,6,1,4,1,5504,2,4,1,3,1,2),_Sechtor100RedundancyEnable_Type())
sechtor100RedundancyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:sechtor100RedundancyEnable.setStatus(_B)
class _Sechtor100FanOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_Sechtor100FanOperationalStatus_Type.__name__=_A
_Sechtor100FanOperationalStatus_Object=MibTableColumn
sechtor100FanOperationalStatus=_Sechtor100FanOperationalStatus_Object((1,3,6,1,4,1,5504,2,4,1,3,1,3),_Sechtor100FanOperationalStatus_Type())
sechtor100FanOperationalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sechtor100FanOperationalStatus.setStatus(_B)
class _Sechtor100ThermoAUpperThreshold_Type(Integer32):defaultValue=65;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,80))
_Sechtor100ThermoAUpperThreshold_Type.__name__=_A
_Sechtor100ThermoAUpperThreshold_Object=MibTableColumn
sechtor100ThermoAUpperThreshold=_Sechtor100ThermoAUpperThreshold_Object((1,3,6,1,4,1,5504,2,4,1,3,1,4),_Sechtor100ThermoAUpperThreshold_Type())
sechtor100ThermoAUpperThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:sechtor100ThermoAUpperThreshold.setStatus(_B)
class _Sechtor100ThermoBUpperThreshold_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,80))
_Sechtor100ThermoBUpperThreshold_Type.__name__=_A
_Sechtor100ThermoBUpperThreshold_Object=MibTableColumn
sechtor100ThermoBUpperThreshold=_Sechtor100ThermoBUpperThreshold_Object((1,3,6,1,4,1,5504,2,4,1,3,1,5),_Sechtor100ThermoBUpperThreshold_Type())
sechtor100ThermoBUpperThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:sechtor100ThermoBUpperThreshold.setStatus(_B)
class _Sechtor100ThermoALowerThreshold_Type(Integer32):defaultValue=-5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,5))
_Sechtor100ThermoALowerThreshold_Type.__name__=_A
_Sechtor100ThermoALowerThreshold_Object=MibTableColumn
sechtor100ThermoALowerThreshold=_Sechtor100ThermoALowerThreshold_Object((1,3,6,1,4,1,5504,2,4,1,3,1,6),_Sechtor100ThermoALowerThreshold_Type())
sechtor100ThermoALowerThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:sechtor100ThermoALowerThreshold.setStatus(_B)
class _Sechtor100ThermoBLowerThreshold_Type(Integer32):defaultValue=-5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,5))
_Sechtor100ThermoBLowerThreshold_Type.__name__=_A
_Sechtor100ThermoBLowerThreshold_Object=MibTableColumn
sechtor100ThermoBLowerThreshold=_Sechtor100ThermoBLowerThreshold_Object((1,3,6,1,4,1,5504,2,4,1,3,1,7),_Sechtor100ThermoBLowerThreshold_Type())
sechtor100ThermoBLowerThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:sechtor100ThermoBLowerThreshold.setStatus(_B)
class _Sechtor100ThermoATemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-55,125))
_Sechtor100ThermoATemperature_Type.__name__=_A
_Sechtor100ThermoATemperature_Object=MibTableColumn
sechtor100ThermoATemperature=_Sechtor100ThermoATemperature_Object((1,3,6,1,4,1,5504,2,4,1,3,1,8),_Sechtor100ThermoATemperature_Type())
sechtor100ThermoATemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:sechtor100ThermoATemperature.setStatus(_B)
class _Sechtor100ThermoBTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-55,125))
_Sechtor100ThermoBTemperature_Type.__name__=_A
_Sechtor100ThermoBTemperature_Object=MibTableColumn
sechtor100ThermoBTemperature=_Sechtor100ThermoBTemperature_Object((1,3,6,1,4,1,5504,2,4,1,3,1,9),_Sechtor100ThermoBTemperature_Type())
sechtor100ThermoBTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:sechtor100ThermoBTemperature.setStatus(_B)
class _Sechtor100ThermoAOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_Sechtor100ThermoAOperationalStatus_Type.__name__=_A
_Sechtor100ThermoAOperationalStatus_Object=MibTableColumn
sechtor100ThermoAOperationalStatus=_Sechtor100ThermoAOperationalStatus_Object((1,3,6,1,4,1,5504,2,4,1,3,1,10),_Sechtor100ThermoAOperationalStatus_Type())
sechtor100ThermoAOperationalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sechtor100ThermoAOperationalStatus.setStatus(_B)
class _Sechtor100ThermoBOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_Sechtor100ThermoBOperationalStatus_Type.__name__=_A
_Sechtor100ThermoBOperationalStatus_Object=MibTableColumn
sechtor100ThermoBOperationalStatus=_Sechtor100ThermoBOperationalStatus_Object((1,3,6,1,4,1,5504,2,4,1,3,1,11),_Sechtor100ThermoBOperationalStatus_Type())
sechtor100ThermoBOperationalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sechtor100ThermoBOperationalStatus.setStatus(_B)
_Sechtor100RowStatus_Type=ZhoneRowStatus
_Sechtor100RowStatus_Object=MibTableColumn
sechtor100RowStatus=_Sechtor100RowStatus_Object((1,3,6,1,4,1,5504,2,4,1,3,1,12),_Sechtor100RowStatus_Type())
sechtor100RowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:sechtor100RowStatus.setStatus(_B)
s100FanStatusChange=NotificationType((1,3,6,1,4,1,5504,2,4,1,2,0,1))
s100FanStatusChange.setObjects((_D,_O))
if mibBuilder.loadTexts:s100FanStatusChange.setStatus(_C)
s100ThermoStatusChange=NotificationType((1,3,6,1,4,1,5504,2,4,1,2,0,2))
s100ThermoStatusChange.setObjects(*((_D,_P),(_D,_Q),(_D,_R),(_D,_S)))
if mibBuilder.loadTexts:s100ThermoStatusChange.setStatus(_C)
sechtor100FanStatusChange=NotificationType((1,3,6,1,4,1,5504,2,4,1,2,0,3))
sechtor100FanStatusChange.setObjects((_D,_T))
if mibBuilder.loadTexts:sechtor100FanStatusChange.setStatus(_B)
sechtor100ThermoStatusChange=NotificationType((1,3,6,1,4,1,5504,2,4,1,2,0,4))
sechtor100ThermoStatusChange.setObjects(*((_D,_U),(_D,_V),(_D,_W),(_D,_X)))
if mibBuilder.loadTexts:sechtor100ThermoStatusChange.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'sechtor100Environment':sechtor100Environment,_O:s100FanOperationalStatus,'s100ThermoAUpperThreshold':s100ThermoAUpperThreshold,'s100ThermoBUpperThreshold':s100ThermoBUpperThreshold,'s10ThermoALowerThreshold':s10ThermoALowerThreshold,'s100ThermoBLowerThreshold':s100ThermoBLowerThreshold,_P:s100ThermoATemperature,_Q:s100ThermoBTemperature,_R:s100ThermoAOperationalStatus,_S:s100ThermoBOperationalStatus,'sechtor100Traps':sechtor100Traps,'sechtor100TrapsPrefix':sechtor100TrapsPrefix,'s100FanStatusChange':s100FanStatusChange,'s100ThermoStatusChange':s100ThermoStatusChange,'sechtor100FanStatusChange':sechtor100FanStatusChange,'sechtor100ThermoStatusChange':sechtor100ThermoStatusChange,'sechtor100ConfigTable':sechtor100ConfigTable,'sechtor100ConfigEntry':sechtor100ConfigEntry,'sechtor100PeerMacAddress':sechtor100PeerMacAddress,'sechtor100RedundancyEnable':sechtor100RedundancyEnable,_T:sechtor100FanOperationalStatus,'sechtor100ThermoAUpperThreshold':sechtor100ThermoAUpperThreshold,'sechtor100ThermoBUpperThreshold':sechtor100ThermoBUpperThreshold,'sechtor100ThermoALowerThreshold':sechtor100ThermoALowerThreshold,'sechtor100ThermoBLowerThreshold':sechtor100ThermoBLowerThreshold,_U:sechtor100ThermoATemperature,_V:sechtor100ThermoBTemperature,_W:sechtor100ThermoAOperationalStatus,_X:sechtor100ThermoBOperationalStatus,'sechtor100RowStatus':sechtor100RowStatus,'zhoneSechtor100':zhoneSechtor100})