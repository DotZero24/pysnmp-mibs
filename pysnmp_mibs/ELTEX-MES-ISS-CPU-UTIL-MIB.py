_F='eltMesIssCpuUtilTaskStatIndex'
_E='ELTEX-MES-ISS-CPU-UTIL-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
eltMesIssCpuUtilMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,6))
if mibBuilder.loadTexts:eltMesIssCpuUtilMIB.setRevisions(('2018-12-26 00:00',))
_EltMesIssCpuUtilObjects_ObjectIdentity=ObjectIdentity
eltMesIssCpuUtilObjects=_EltMesIssCpuUtilObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,6,1))
_EltMesIssCpuUtilGlobal_ObjectIdentity=ObjectIdentity
eltMesIssCpuUtilGlobal=_EltMesIssCpuUtilGlobal_ObjectIdentity((1,3,6,1,4,1,35265,1,139,6,1,1))
_EltMesIssCpuUtilGlobalConfig_ObjectIdentity=ObjectIdentity
eltMesIssCpuUtilGlobalConfig=_EltMesIssCpuUtilGlobalConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,6,1,1,1))
class _EltMesIssCpuUtilEnable_Type(TruthValue):defaultValue=1
_EltMesIssCpuUtilEnable_Type.__name__=_D
_EltMesIssCpuUtilEnable_Object=MibScalar
eltMesIssCpuUtilEnable=_EltMesIssCpuUtilEnable_Object((1,3,6,1,4,1,35265,1,139,6,1,1,1,1),_EltMesIssCpuUtilEnable_Type())
eltMesIssCpuUtilEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilEnable.setStatus(_A)
_EltMesIssCpuUtilGlobalStat_ObjectIdentity=ObjectIdentity
eltMesIssCpuUtilGlobalStat=_EltMesIssCpuUtilGlobalStat_ObjectIdentity((1,3,6,1,4,1,35265,1,139,6,1,1,2))
class _EltMesIssCpuUtilLast5Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EltMesIssCpuUtilLast5Seconds_Type.__name__=_C
_EltMesIssCpuUtilLast5Seconds_Object=MibScalar
eltMesIssCpuUtilLast5Seconds=_EltMesIssCpuUtilLast5Seconds_Object((1,3,6,1,4,1,35265,1,139,6,1,1,2,1),_EltMesIssCpuUtilLast5Seconds_Type())
eltMesIssCpuUtilLast5Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilLast5Seconds.setStatus(_A)
class _EltMesIssCpuUtilLastMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EltMesIssCpuUtilLastMinute_Type.__name__=_C
_EltMesIssCpuUtilLastMinute_Object=MibScalar
eltMesIssCpuUtilLastMinute=_EltMesIssCpuUtilLastMinute_Object((1,3,6,1,4,1,35265,1,139,6,1,1,2,2),_EltMesIssCpuUtilLastMinute_Type())
eltMesIssCpuUtilLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilLastMinute.setStatus(_A)
class _EltMesIssCpuUtilLast5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EltMesIssCpuUtilLast5Minutes_Type.__name__=_C
_EltMesIssCpuUtilLast5Minutes_Object=MibScalar
eltMesIssCpuUtilLast5Minutes=_EltMesIssCpuUtilLast5Minutes_Object((1,3,6,1,4,1,35265,1,139,6,1,1,2,3),_EltMesIssCpuUtilLast5Minutes_Type())
eltMesIssCpuUtilLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilLast5Minutes.setStatus(_A)
_EltMesIssCpuUtilTask_ObjectIdentity=ObjectIdentity
eltMesIssCpuUtilTask=_EltMesIssCpuUtilTask_ObjectIdentity((1,3,6,1,4,1,35265,1,139,6,1,2))
_EltMesIssCpuUtilTaskConfig_ObjectIdentity=ObjectIdentity
eltMesIssCpuUtilTaskConfig=_EltMesIssCpuUtilTaskConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,6,1,2,1))
class _EltMesIssCpuUtilTaskEnable_Type(TruthValue):defaultValue=1
_EltMesIssCpuUtilTaskEnable_Type.__name__=_D
_EltMesIssCpuUtilTaskEnable_Object=MibScalar
eltMesIssCpuUtilTaskEnable=_EltMesIssCpuUtilTaskEnable_Object((1,3,6,1,4,1,35265,1,139,6,1,2,1,1),_EltMesIssCpuUtilTaskEnable_Type())
eltMesIssCpuUtilTaskEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskEnable.setStatus(_A)
_EltMesIssCpuUtilTaskStat_ObjectIdentity=ObjectIdentity
eltMesIssCpuUtilTaskStat=_EltMesIssCpuUtilTaskStat_ObjectIdentity((1,3,6,1,4,1,35265,1,139,6,1,2,2))
_EltMesIssCpuUtilTaskStatTable_Object=MibTable
eltMesIssCpuUtilTaskStatTable=_EltMesIssCpuUtilTaskStatTable_Object((1,3,6,1,4,1,35265,1,139,6,1,2,2,1))
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskStatTable.setStatus(_A)
_EltMesIssCpuUtilTaskStatEntry_Object=MibTableRow
eltMesIssCpuUtilTaskStatEntry=_EltMesIssCpuUtilTaskStatEntry_Object((1,3,6,1,4,1,35265,1,139,6,1,2,2,1,1))
eltMesIssCpuUtilTaskStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskStatEntry.setStatus(_A)
_EltMesIssCpuUtilTaskStatIndex_Type=Integer32
_EltMesIssCpuUtilTaskStatIndex_Object=MibTableColumn
eltMesIssCpuUtilTaskStatIndex=_EltMesIssCpuUtilTaskStatIndex_Object((1,3,6,1,4,1,35265,1,139,6,1,2,2,1,1,1),_EltMesIssCpuUtilTaskStatIndex_Type())
eltMesIssCpuUtilTaskStatIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskStatIndex.setStatus(_A)
_EltMesIssCpuUtilTaskStatName_Type=DisplayString
_EltMesIssCpuUtilTaskStatName_Object=MibTableColumn
eltMesIssCpuUtilTaskStatName=_EltMesIssCpuUtilTaskStatName_Object((1,3,6,1,4,1,35265,1,139,6,1,2,2,1,1,2),_EltMesIssCpuUtilTaskStatName_Type())
eltMesIssCpuUtilTaskStatName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskStatName.setStatus(_A)
class _EltMesIssCpuUtilTaskStatLast5Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EltMesIssCpuUtilTaskStatLast5Seconds_Type.__name__=_C
_EltMesIssCpuUtilTaskStatLast5Seconds_Object=MibTableColumn
eltMesIssCpuUtilTaskStatLast5Seconds=_EltMesIssCpuUtilTaskStatLast5Seconds_Object((1,3,6,1,4,1,35265,1,139,6,1,2,2,1,1,3),_EltMesIssCpuUtilTaskStatLast5Seconds_Type())
eltMesIssCpuUtilTaskStatLast5Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskStatLast5Seconds.setStatus(_A)
class _EltMesIssCpuUtilTaskStatLastMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EltMesIssCpuUtilTaskStatLastMinute_Type.__name__=_C
_EltMesIssCpuUtilTaskStatLastMinute_Object=MibTableColumn
eltMesIssCpuUtilTaskStatLastMinute=_EltMesIssCpuUtilTaskStatLastMinute_Object((1,3,6,1,4,1,35265,1,139,6,1,2,2,1,1,4),_EltMesIssCpuUtilTaskStatLastMinute_Type())
eltMesIssCpuUtilTaskStatLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskStatLastMinute.setStatus(_A)
class _EltMesIssCpuUtilTaskStatLast5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EltMesIssCpuUtilTaskStatLast5Minutes_Type.__name__=_C
_EltMesIssCpuUtilTaskStatLast5Minutes_Object=MibTableColumn
eltMesIssCpuUtilTaskStatLast5Minutes=_EltMesIssCpuUtilTaskStatLast5Minutes_Object((1,3,6,1,4,1,35265,1,139,6,1,2,2,1,1,5),_EltMesIssCpuUtilTaskStatLast5Minutes_Type())
eltMesIssCpuUtilTaskStatLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssCpuUtilTaskStatLast5Minutes.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'eltMesIssCpuUtilMIB':eltMesIssCpuUtilMIB,'eltMesIssCpuUtilObjects':eltMesIssCpuUtilObjects,'eltMesIssCpuUtilGlobal':eltMesIssCpuUtilGlobal,'eltMesIssCpuUtilGlobalConfig':eltMesIssCpuUtilGlobalConfig,'eltMesIssCpuUtilEnable':eltMesIssCpuUtilEnable,'eltMesIssCpuUtilGlobalStat':eltMesIssCpuUtilGlobalStat,'eltMesIssCpuUtilLast5Seconds':eltMesIssCpuUtilLast5Seconds,'eltMesIssCpuUtilLastMinute':eltMesIssCpuUtilLastMinute,'eltMesIssCpuUtilLast5Minutes':eltMesIssCpuUtilLast5Minutes,'eltMesIssCpuUtilTask':eltMesIssCpuUtilTask,'eltMesIssCpuUtilTaskConfig':eltMesIssCpuUtilTaskConfig,'eltMesIssCpuUtilTaskEnable':eltMesIssCpuUtilTaskEnable,'eltMesIssCpuUtilTaskStat':eltMesIssCpuUtilTaskStat,'eltMesIssCpuUtilTaskStatTable':eltMesIssCpuUtilTaskStatTable,'eltMesIssCpuUtilTaskStatEntry':eltMesIssCpuUtilTaskStatEntry,_F:eltMesIssCpuUtilTaskStatIndex,'eltMesIssCpuUtilTaskStatName':eltMesIssCpuUtilTaskStatName,'eltMesIssCpuUtilTaskStatLast5Seconds':eltMesIssCpuUtilTaskStatLast5Seconds,'eltMesIssCpuUtilTaskStatLastMinute':eltMesIssCpuUtilTaskStatLastMinute,'eltMesIssCpuUtilTaskStatLast5Minutes':eltMesIssCpuUtilTaskStatLast5Minutes})