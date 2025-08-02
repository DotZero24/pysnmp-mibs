_G='tpSysMonitorMemoryUnitNumber'
_F='tpSysMonitorCpuUnitNumber'
_E='TPLINK-SYSMONITOR-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSysMonitorMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,4))
_TplinkSysMonitorMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSysMonitorMIBObjects=_TplinkSysMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,4,1))
_TpSysMonitorCpu_ObjectIdentity=ObjectIdentity
tpSysMonitorCpu=_TpSysMonitorCpu_ObjectIdentity((1,3,6,1,4,1,11863,6,4,1,1))
_TpSysMonitorCpuTable_Object=MibTable
tpSysMonitorCpuTable=_TpSysMonitorCpuTable_Object((1,3,6,1,4,1,11863,6,4,1,1,1))
if mibBuilder.loadTexts:tpSysMonitorCpuTable.setStatus(_A)
_TpSysMonitorCpuEntry_Object=MibTableRow
tpSysMonitorCpuEntry=_TpSysMonitorCpuEntry_Object((1,3,6,1,4,1,11863,6,4,1,1,1,1))
tpSysMonitorCpuEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tpSysMonitorCpuEntry.setStatus(_A)
_TpSysMonitorCpuUnitNumber_Type=Integer32
_TpSysMonitorCpuUnitNumber_Object=MibTableColumn
tpSysMonitorCpuUnitNumber=_TpSysMonitorCpuUnitNumber_Object((1,3,6,1,4,1,11863,6,4,1,1,1,1,1),_TpSysMonitorCpuUnitNumber_Type())
tpSysMonitorCpuUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorCpuUnitNumber.setStatus(_A)
class _TpSysMonitorCpu5Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TpSysMonitorCpu5Seconds_Type.__name__=_C
_TpSysMonitorCpu5Seconds_Object=MibTableColumn
tpSysMonitorCpu5Seconds=_TpSysMonitorCpu5Seconds_Object((1,3,6,1,4,1,11863,6,4,1,1,1,1,2),_TpSysMonitorCpu5Seconds_Type())
tpSysMonitorCpu5Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorCpu5Seconds.setStatus(_A)
class _TpSysMonitorCpu1Minute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TpSysMonitorCpu1Minute_Type.__name__=_C
_TpSysMonitorCpu1Minute_Object=MibTableColumn
tpSysMonitorCpu1Minute=_TpSysMonitorCpu1Minute_Object((1,3,6,1,4,1,11863,6,4,1,1,1,1,3),_TpSysMonitorCpu1Minute_Type())
tpSysMonitorCpu1Minute.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorCpu1Minute.setStatus(_A)
class _TpSysMonitorCpu5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TpSysMonitorCpu5Minutes_Type.__name__=_C
_TpSysMonitorCpu5Minutes_Object=MibTableColumn
tpSysMonitorCpu5Minutes=_TpSysMonitorCpu5Minutes_Object((1,3,6,1,4,1,11863,6,4,1,1,1,1,4),_TpSysMonitorCpu5Minutes_Type())
tpSysMonitorCpu5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorCpu5Minutes.setStatus(_A)
_TpSysMonitorMemory_ObjectIdentity=ObjectIdentity
tpSysMonitorMemory=_TpSysMonitorMemory_ObjectIdentity((1,3,6,1,4,1,11863,6,4,1,2))
_TpSysMonitorMemoryTable_Object=MibTable
tpSysMonitorMemoryTable=_TpSysMonitorMemoryTable_Object((1,3,6,1,4,1,11863,6,4,1,2,1))
if mibBuilder.loadTexts:tpSysMonitorMemoryTable.setStatus(_A)
_TpSysMonitorMemoryEntry_Object=MibTableRow
tpSysMonitorMemoryEntry=_TpSysMonitorMemoryEntry_Object((1,3,6,1,4,1,11863,6,4,1,2,1,1))
tpSysMonitorMemoryEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:tpSysMonitorMemoryEntry.setStatus(_A)
_TpSysMonitorMemoryUnitNumber_Type=Integer32
_TpSysMonitorMemoryUnitNumber_Object=MibTableColumn
tpSysMonitorMemoryUnitNumber=_TpSysMonitorMemoryUnitNumber_Object((1,3,6,1,4,1,11863,6,4,1,2,1,1,1),_TpSysMonitorMemoryUnitNumber_Type())
tpSysMonitorMemoryUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorMemoryUnitNumber.setStatus(_A)
class _TpSysMonitorMemoryUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TpSysMonitorMemoryUtilization_Type.__name__=_C
_TpSysMonitorMemoryUtilization_Object=MibTableColumn
tpSysMonitorMemoryUtilization=_TpSysMonitorMemoryUtilization_Object((1,3,6,1,4,1,11863,6,4,1,2,1,1,2),_TpSysMonitorMemoryUtilization_Type())
tpSysMonitorMemoryUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorMemoryUtilization.setStatus(_A)
class _TpSysMonitorTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSysMonitorTemperature_Type.__name__=_D
_TpSysMonitorTemperature_Object=MibScalar
tpSysMonitorTemperature=_TpSysMonitorTemperature_Object((1,3,6,1,4,1,11863,6,4,1,3),_TpSysMonitorTemperature_Type())
tpSysMonitorTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorTemperature.setStatus(_A)
class _TpSysMonitorVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSysMonitorVoltage_Type.__name__=_D
_TpSysMonitorVoltage_Object=MibScalar
tpSysMonitorVoltage=_TpSysMonitorVoltage_Object((1,3,6,1,4,1,11863,6,4,1,4),_TpSysMonitorVoltage_Type())
tpSysMonitorVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysMonitorVoltage.setStatus(_A)
_TplinkSysMonitorNotifications_ObjectIdentity=ObjectIdentity
tplinkSysMonitorNotifications=_TplinkSysMonitorNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,4,2))
tpSysMonitorCpuOverLoading=NotificationType((1,3,6,1,4,1,11863,6,4,2,1))
if mibBuilder.loadTexts:tpSysMonitorCpuOverLoading.setStatus(_A)
tpSysMonitorMemoryOverLoading=NotificationType((1,3,6,1,4,1,11863,6,4,2,2))
if mibBuilder.loadTexts:tpSysMonitorMemoryOverLoading.setStatus(_A)
tpSysMonitorTemperatureOverLoading=NotificationType((1,3,6,1,4,1,11863,6,4,2,3))
if mibBuilder.loadTexts:tpSysMonitorTemperatureOverLoading.setStatus(_A)
tpSysMonitorVoltageOverLoading=NotificationType((1,3,6,1,4,1,11863,6,4,2,4))
if mibBuilder.loadTexts:tpSysMonitorVoltageOverLoading.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'tplinkSysMonitorMIB':tplinkSysMonitorMIB,'tplinkSysMonitorMIBObjects':tplinkSysMonitorMIBObjects,'tpSysMonitorCpu':tpSysMonitorCpu,'tpSysMonitorCpuTable':tpSysMonitorCpuTable,'tpSysMonitorCpuEntry':tpSysMonitorCpuEntry,_F:tpSysMonitorCpuUnitNumber,'tpSysMonitorCpu5Seconds':tpSysMonitorCpu5Seconds,'tpSysMonitorCpu1Minute':tpSysMonitorCpu1Minute,'tpSysMonitorCpu5Minutes':tpSysMonitorCpu5Minutes,'tpSysMonitorMemory':tpSysMonitorMemory,'tpSysMonitorMemoryTable':tpSysMonitorMemoryTable,'tpSysMonitorMemoryEntry':tpSysMonitorMemoryEntry,_G:tpSysMonitorMemoryUnitNumber,'tpSysMonitorMemoryUtilization':tpSysMonitorMemoryUtilization,'tpSysMonitorTemperature':tpSysMonitorTemperature,'tpSysMonitorVoltage':tpSysMonitorVoltage,'tplinkSysMonitorNotifications':tplinkSysMonitorNotifications,'tpSysMonitorCpuOverLoading':tpSysMonitorCpuOverLoading,'tpSysMonitorMemoryOverLoading':tpSysMonitorMemoryOverLoading,'tpSysMonitorTemperatureOverLoading':tpSysMonitorTemperatureOverLoading,'tpSysMonitorVoltageOverLoading':tpSysMonitorVoltageOverLoading})