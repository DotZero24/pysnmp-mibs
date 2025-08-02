_F='eltCpuTasksUtilStatisticsTaskIndex'
_E='ELTEX-MES-CPU-TASKS-UTIL-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesCpuTasksUtilMIB,=mibBuilder.importSymbols('ELTEX-MES-MNG-MIB','eltMesCpuTasksUtilMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
_EltMesCpuTasksUtilObjects_ObjectIdentity=ObjectIdentity
eltMesCpuTasksUtilObjects=_EltMesCpuTasksUtilObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,9,1))
_EltMesCpuTasksUtilConfig_ObjectIdentity=ObjectIdentity
eltMesCpuTasksUtilConfig=_EltMesCpuTasksUtilConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,9,1,1))
class _EltCpuTasksUtilEnable_Type(TruthValue):defaultValue=1
_EltCpuTasksUtilEnable_Type.__name__=_D
_EltCpuTasksUtilEnable_Object=MibScalar
eltCpuTasksUtilEnable=_EltCpuTasksUtilEnable_Object((1,3,6,1,4,1,35265,1,23,1,9,1,1,1),_EltCpuTasksUtilEnable_Type())
eltCpuTasksUtilEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltCpuTasksUtilEnable.setStatus(_A)
_EltMesCpuTasksUtilStatistics_ObjectIdentity=ObjectIdentity
eltMesCpuTasksUtilStatistics=_EltMesCpuTasksUtilStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,9,1,2))
_EltCpuTasksUtilStatisticsTable_Object=MibTable
eltCpuTasksUtilStatisticsTable=_EltCpuTasksUtilStatisticsTable_Object((1,3,6,1,4,1,35265,1,23,1,9,1,2,1))
if mibBuilder.loadTexts:eltCpuTasksUtilStatisticsTable.setStatus(_A)
_EltCpuTasksUtilStatisticsEntry_Object=MibTableRow
eltCpuTasksUtilStatisticsEntry=_EltCpuTasksUtilStatisticsEntry_Object((1,3,6,1,4,1,35265,1,23,1,9,1,2,1,1))
eltCpuTasksUtilStatisticsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eltCpuTasksUtilStatisticsEntry.setStatus(_A)
_EltCpuTasksUtilStatisticsTaskIndex_Type=Integer32
_EltCpuTasksUtilStatisticsTaskIndex_Object=MibTableColumn
eltCpuTasksUtilStatisticsTaskIndex=_EltCpuTasksUtilStatisticsTaskIndex_Object((1,3,6,1,4,1,35265,1,23,1,9,1,2,1,1,1),_EltCpuTasksUtilStatisticsTaskIndex_Type())
eltCpuTasksUtilStatisticsTaskIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCpuTasksUtilStatisticsTaskIndex.setStatus(_A)
_EltCpuTasksUtilStatisticsTaskName_Type=DisplayString
_EltCpuTasksUtilStatisticsTaskName_Object=MibTableColumn
eltCpuTasksUtilStatisticsTaskName=_EltCpuTasksUtilStatisticsTaskName_Object((1,3,6,1,4,1,35265,1,23,1,9,1,2,1,1,2),_EltCpuTasksUtilStatisticsTaskName_Type())
eltCpuTasksUtilStatisticsTaskName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCpuTasksUtilStatisticsTaskName.setStatus(_A)
class _EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,101))
_EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Type.__name__=_C
_EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Object=MibTableColumn
eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds=_EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Object((1,3,6,1,4,1,35265,1,23,1,9,1,2,1,1,3),_EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Type())
eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds.setStatus(_A)
class _EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,101))
_EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Type.__name__=_C
_EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Object=MibTableColumn
eltCpuTasksUtilStatisticsUtilizationDuringLastMinute=_EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Object((1,3,6,1,4,1,35265,1,23,1,9,1,2,1,1,4),_EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Type())
eltCpuTasksUtilStatisticsUtilizationDuringLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCpuTasksUtilStatisticsUtilizationDuringLastMinute.setStatus(_A)
class _EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,101))
_EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Type.__name__=_C
_EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Object=MibTableColumn
eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes=_EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Object((1,3,6,1,4,1,35265,1,23,1,9,1,2,1,1,5),_EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Type())
eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'eltMesCpuTasksUtilObjects':eltMesCpuTasksUtilObjects,'eltMesCpuTasksUtilConfig':eltMesCpuTasksUtilConfig,'eltCpuTasksUtilEnable':eltCpuTasksUtilEnable,'eltMesCpuTasksUtilStatistics':eltMesCpuTasksUtilStatistics,'eltCpuTasksUtilStatisticsTable':eltCpuTasksUtilStatisticsTable,'eltCpuTasksUtilStatisticsEntry':eltCpuTasksUtilStatisticsEntry,_F:eltCpuTasksUtilStatisticsTaskIndex,'eltCpuTasksUtilStatisticsTaskName':eltCpuTasksUtilStatisticsTaskName,'eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds':eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds,'eltCpuTasksUtilStatisticsUtilizationDuringLastMinute':eltCpuTasksUtilStatisticsUtilizationDuringLastMinute,'eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes':eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes})