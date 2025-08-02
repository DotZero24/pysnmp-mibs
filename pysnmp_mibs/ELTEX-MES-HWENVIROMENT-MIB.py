_F='eltEnvMonFanStatusEntry'
_E='eltEnvMonBatteryStatusIndex'
_D='read-only'
_C='ELTEX-MES-HWENVIROMENT-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
RlEnvMonState,rlEnvMonFanStatusEntry=mibBuilder.importSymbols('RADLAN-HWENVIROMENT','RlEnvMonState','rlEnvMonFanStatusEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesEnv=ModuleIdentity((1,3,6,1,4,1,35265,1,23,11))
if mibBuilder.loadTexts:eltMesEnv.setRevisions(('2018-07-27 00:00','2017-10-11 00:00','2015-06-11 00:00'))
_EltEnvMonBatteryStatusTable_Object=MibTable
eltEnvMonBatteryStatusTable=_EltEnvMonBatteryStatusTable_Object((1,3,6,1,4,1,35265,1,23,11,1))
if mibBuilder.loadTexts:eltEnvMonBatteryStatusTable.setStatus(_A)
_EltEnvMonBatteryStatusEntry_Object=MibTableRow
eltEnvMonBatteryStatusEntry=_EltEnvMonBatteryStatusEntry_Object((1,3,6,1,4,1,35265,1,23,11,1,1))
eltEnvMonBatteryStatusEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:eltEnvMonBatteryStatusEntry.setStatus(_A)
_EltEnvMonBatteryStatusIndex_Type=Integer32
_EltEnvMonBatteryStatusIndex_Object=MibTableColumn
eltEnvMonBatteryStatusIndex=_EltEnvMonBatteryStatusIndex_Object((1,3,6,1,4,1,35265,1,23,11,1,1,1),_EltEnvMonBatteryStatusIndex_Type())
eltEnvMonBatteryStatusIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltEnvMonBatteryStatusIndex.setStatus(_A)
_EltEnvMonBatteryState_Type=RlEnvMonState
_EltEnvMonBatteryState_Object=MibTableColumn
eltEnvMonBatteryState=_EltEnvMonBatteryState_Object((1,3,6,1,4,1,35265,1,23,11,1,1,2),_EltEnvMonBatteryState_Type())
eltEnvMonBatteryState.setMaxAccess(_D)
if mibBuilder.loadTexts:eltEnvMonBatteryState.setStatus(_A)
class _EltEnvMonBatteryStatusCharge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100),ValueRangeConstraint(255,255))
_EltEnvMonBatteryStatusCharge_Type.__name__=_B
_EltEnvMonBatteryStatusCharge_Object=MibTableColumn
eltEnvMonBatteryStatusCharge=_EltEnvMonBatteryStatusCharge_Object((1,3,6,1,4,1,35265,1,23,11,1,1,3),_EltEnvMonBatteryStatusCharge_Type())
eltEnvMonBatteryStatusCharge.setMaxAccess(_D)
if mibBuilder.loadTexts:eltEnvMonBatteryStatusCharge.setStatus(_A)
class _EltEnvResetButtonMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('enable',0),('disable',1),('reset-only',2)))
_EltEnvResetButtonMode_Type.__name__=_B
_EltEnvResetButtonMode_Object=MibScalar
eltEnvResetButtonMode=_EltEnvResetButtonMode_Object((1,3,6,1,4,1,35265,1,23,11,2),_EltEnvResetButtonMode_Type())
eltEnvResetButtonMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltEnvResetButtonMode.setStatus(_A)
_EltEnvMonFanStatusTable_Object=MibTable
eltEnvMonFanStatusTable=_EltEnvMonFanStatusTable_Object((1,3,6,1,4,1,35265,1,23,11,3))
if mibBuilder.loadTexts:eltEnvMonFanStatusTable.setStatus(_A)
_EltEnvMonFanStatusEntry_Object=MibTableRow
eltEnvMonFanStatusEntry=_EltEnvMonFanStatusEntry_Object((1,3,6,1,4,1,35265,1,23,11,3,1))
if mibBuilder.loadTexts:eltEnvMonFanStatusEntry.setStatus(_A)
_EltEnvMonFanSpeed_Type=Integer32
_EltEnvMonFanSpeed_Object=MibTableColumn
eltEnvMonFanSpeed=_EltEnvMonFanSpeed_Object((1,3,6,1,4,1,35265,1,23,11,3,1,1),_EltEnvMonFanSpeed_Type())
eltEnvMonFanSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:eltEnvMonFanSpeed.setStatus(_A)
rlEnvMonFanStatusEntry.registerAugmentions((_C,_F))
eltEnvMonFanStatusEntry.setIndexNames(*rlEnvMonFanStatusEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'eltMesEnv':eltMesEnv,'eltEnvMonBatteryStatusTable':eltEnvMonBatteryStatusTable,'eltEnvMonBatteryStatusEntry':eltEnvMonBatteryStatusEntry,_E:eltEnvMonBatteryStatusIndex,'eltEnvMonBatteryState':eltEnvMonBatteryState,'eltEnvMonBatteryStatusCharge':eltEnvMonBatteryStatusCharge,'eltEnvResetButtonMode':eltEnvResetButtonMode,'eltEnvMonFanStatusTable':eltEnvMonFanStatusTable,_F:eltEnvMonFanStatusEntry,'eltEnvMonFanSpeed':eltEnvMonFanSpeed})