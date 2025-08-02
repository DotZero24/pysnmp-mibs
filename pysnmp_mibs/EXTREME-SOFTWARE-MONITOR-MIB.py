_T='trialPeriod'
_S='extremeServiceLicenseType'
_R='extremeServiceLicenseExpiryDate'
_Q='extremeMemoryMonitorProcessName'
_P='extremeMemoryMonitorSlotId'
_O='extremeMemoryMonitorSystemSlotId'
_N='extremeCpuMonitorSystemSlotId'
_M='not-accessible'
_L='noOfDaysLeft'
_K='imageDescription'
_J='extremeCpuMonitorThreshold'
_I='extremeCpuMonitorCurrentUtilization'
_H='extremeCpuMonitorProcessName'
_G='extremeCpuMonitorSlotId'
_F='accessible-for-notify'
_E='Integer32'
_D='DisplayString'
_C='EXTREME-SOFTWARE-MONITOR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','PortList','extremeAgent')
extremeImageDescription,=mibBuilder.importSymbols('EXTREME-SYSTEM-MIB','extremeImageDescription')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
extremeSwMonitor=ModuleIdentity((1,3,6,1,4,1,1916,1,32))
_ExtremeSwMonitorCpu_ObjectIdentity=ObjectIdentity
extremeSwMonitorCpu=_ExtremeSwMonitorCpu_ObjectIdentity((1,3,6,1,4,1,1916,1,32,1))
class _ExtremeCpuMonitorInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_ExtremeCpuMonitorInterval_Type.__name__=_E
_ExtremeCpuMonitorInterval_Object=MibScalar
extremeCpuMonitorInterval=_ExtremeCpuMonitorInterval_Object((1,3,6,1,4,1,1916,1,32,1,1),_ExtremeCpuMonitorInterval_Type())
extremeCpuMonitorInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorInterval.setStatus(_A)
class _ExtremeCpuMonitorTotalUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ExtremeCpuMonitorTotalUtilization_Type.__name__=_E
_ExtremeCpuMonitorTotalUtilization_Object=MibScalar
extremeCpuMonitorTotalUtilization=_ExtremeCpuMonitorTotalUtilization_Object((1,3,6,1,4,1,1916,1,32,1,2),_ExtremeCpuMonitorTotalUtilization_Type())
extremeCpuMonitorTotalUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorTotalUtilization.setStatus(_A)
_ExtremeCpuMonitorTable_Object=MibTable
extremeCpuMonitorTable=_ExtremeCpuMonitorTable_Object((1,3,6,1,4,1,1916,1,32,1,3))
if mibBuilder.loadTexts:extremeCpuMonitorTable.setStatus(_A)
_ExtremeCpuMonitorEntry_Object=MibTableRow
extremeCpuMonitorEntry=_ExtremeCpuMonitorEntry_Object((1,3,6,1,4,1,1916,1,32,1,3,1))
extremeCpuMonitorEntry.setIndexNames((0,_C,_G),(1,_C,_H))
if mibBuilder.loadTexts:extremeCpuMonitorEntry.setStatus(_A)
_ExtremeCpuMonitorSlotId_Type=Unsigned32
_ExtremeCpuMonitorSlotId_Object=MibTableColumn
extremeCpuMonitorSlotId=_ExtremeCpuMonitorSlotId_Object((1,3,6,1,4,1,1916,1,32,1,3,1,1),_ExtremeCpuMonitorSlotId_Type())
extremeCpuMonitorSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSlotId.setStatus(_A)
class _ExtremeCpuMonitorProcessName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ExtremeCpuMonitorProcessName_Type.__name__=_D
_ExtremeCpuMonitorProcessName_Object=MibTableColumn
extremeCpuMonitorProcessName=_ExtremeCpuMonitorProcessName_Object((1,3,6,1,4,1,1916,1,32,1,3,1,2),_ExtremeCpuMonitorProcessName_Type())
extremeCpuMonitorProcessName.setMaxAccess(_M)
if mibBuilder.loadTexts:extremeCpuMonitorProcessName.setStatus(_A)
_ExtremeCpuMonitorProcessId_Type=Unsigned32
_ExtremeCpuMonitorProcessId_Object=MibTableColumn
extremeCpuMonitorProcessId=_ExtremeCpuMonitorProcessId_Object((1,3,6,1,4,1,1916,1,32,1,3,1,3),_ExtremeCpuMonitorProcessId_Type())
extremeCpuMonitorProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorProcessId.setStatus(_A)
_ExtremeCpuMonitorProcessState_Type=DisplayString
_ExtremeCpuMonitorProcessState_Object=MibTableColumn
extremeCpuMonitorProcessState=_ExtremeCpuMonitorProcessState_Object((1,3,6,1,4,1,1916,1,32,1,3,1,4),_ExtremeCpuMonitorProcessState_Type())
extremeCpuMonitorProcessState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorProcessState.setStatus(_A)
_ExtremeCpuMonitorUtilization5secs_Type=DisplayString
_ExtremeCpuMonitorUtilization5secs_Object=MibTableColumn
extremeCpuMonitorUtilization5secs=_ExtremeCpuMonitorUtilization5secs_Object((1,3,6,1,4,1,1916,1,32,1,3,1,5),_ExtremeCpuMonitorUtilization5secs_Type())
extremeCpuMonitorUtilization5secs.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUtilization5secs.setStatus(_A)
_ExtremeCpuMonitorUtilization10secs_Type=DisplayString
_ExtremeCpuMonitorUtilization10secs_Object=MibTableColumn
extremeCpuMonitorUtilization10secs=_ExtremeCpuMonitorUtilization10secs_Object((1,3,6,1,4,1,1916,1,32,1,3,1,6),_ExtremeCpuMonitorUtilization10secs_Type())
extremeCpuMonitorUtilization10secs.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUtilization10secs.setStatus(_A)
_ExtremeCpuMonitorUtilization30secs_Type=DisplayString
_ExtremeCpuMonitorUtilization30secs_Object=MibTableColumn
extremeCpuMonitorUtilization30secs=_ExtremeCpuMonitorUtilization30secs_Object((1,3,6,1,4,1,1916,1,32,1,3,1,7),_ExtremeCpuMonitorUtilization30secs_Type())
extremeCpuMonitorUtilization30secs.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUtilization30secs.setStatus(_A)
_ExtremeCpuMonitorUtilization1min_Type=DisplayString
_ExtremeCpuMonitorUtilization1min_Object=MibTableColumn
extremeCpuMonitorUtilization1min=_ExtremeCpuMonitorUtilization1min_Object((1,3,6,1,4,1,1916,1,32,1,3,1,8),_ExtremeCpuMonitorUtilization1min_Type())
extremeCpuMonitorUtilization1min.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUtilization1min.setStatus(_A)
_ExtremeCpuMonitorUtilization5mins_Type=DisplayString
_ExtremeCpuMonitorUtilization5mins_Object=MibTableColumn
extremeCpuMonitorUtilization5mins=_ExtremeCpuMonitorUtilization5mins_Object((1,3,6,1,4,1,1916,1,32,1,3,1,9),_ExtremeCpuMonitorUtilization5mins_Type())
extremeCpuMonitorUtilization5mins.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUtilization5mins.setStatus(_A)
_ExtremeCpuMonitorUtilization30mins_Type=DisplayString
_ExtremeCpuMonitorUtilization30mins_Object=MibTableColumn
extremeCpuMonitorUtilization30mins=_ExtremeCpuMonitorUtilization30mins_Object((1,3,6,1,4,1,1916,1,32,1,3,1,10),_ExtremeCpuMonitorUtilization30mins_Type())
extremeCpuMonitorUtilization30mins.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUtilization30mins.setStatus(_A)
_ExtremeCpuMonitorUtilization1hour_Type=DisplayString
_ExtremeCpuMonitorUtilization1hour_Object=MibTableColumn
extremeCpuMonitorUtilization1hour=_ExtremeCpuMonitorUtilization1hour_Object((1,3,6,1,4,1,1916,1,32,1,3,1,11),_ExtremeCpuMonitorUtilization1hour_Type())
extremeCpuMonitorUtilization1hour.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUtilization1hour.setStatus(_A)
_ExtremeCpuMonitorMaxUtilization_Type=DisplayString
_ExtremeCpuMonitorMaxUtilization_Object=MibTableColumn
extremeCpuMonitorMaxUtilization=_ExtremeCpuMonitorMaxUtilization_Object((1,3,6,1,4,1,1916,1,32,1,3,1,12),_ExtremeCpuMonitorMaxUtilization_Type())
extremeCpuMonitorMaxUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorMaxUtilization.setStatus(_A)
_ExtremeCpuMonitorUserTime_Type=DisplayString
_ExtremeCpuMonitorUserTime_Object=MibTableColumn
extremeCpuMonitorUserTime=_ExtremeCpuMonitorUserTime_Object((1,3,6,1,4,1,1916,1,32,1,3,1,13),_ExtremeCpuMonitorUserTime_Type())
extremeCpuMonitorUserTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorUserTime.setStatus(_A)
_ExtremeCpuMonitorSystemTime_Type=DisplayString
_ExtremeCpuMonitorSystemTime_Object=MibTableColumn
extremeCpuMonitorSystemTime=_ExtremeCpuMonitorSystemTime_Object((1,3,6,1,4,1,1916,1,32,1,3,1,14),_ExtremeCpuMonitorSystemTime_Type())
extremeCpuMonitorSystemTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemTime.setStatus(_A)
_ExtremeCpuMonitorSystemTable_Object=MibTable
extremeCpuMonitorSystemTable=_ExtremeCpuMonitorSystemTable_Object((1,3,6,1,4,1,1916,1,32,1,4))
if mibBuilder.loadTexts:extremeCpuMonitorSystemTable.setStatus(_A)
_ExtremeCpuMonitorSystemEntry_Object=MibTableRow
extremeCpuMonitorSystemEntry=_ExtremeCpuMonitorSystemEntry_Object((1,3,6,1,4,1,1916,1,32,1,4,1))
extremeCpuMonitorSystemEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:extremeCpuMonitorSystemEntry.setStatus(_A)
_ExtremeCpuMonitorSystemSlotId_Type=Unsigned32
_ExtremeCpuMonitorSystemSlotId_Object=MibTableColumn
extremeCpuMonitorSystemSlotId=_ExtremeCpuMonitorSystemSlotId_Object((1,3,6,1,4,1,1916,1,32,1,4,1,1),_ExtremeCpuMonitorSystemSlotId_Type())
extremeCpuMonitorSystemSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemSlotId.setStatus(_A)
_ExtremeCpuMonitorSystemUtilization5secs_Type=DisplayString
_ExtremeCpuMonitorSystemUtilization5secs_Object=MibTableColumn
extremeCpuMonitorSystemUtilization5secs=_ExtremeCpuMonitorSystemUtilization5secs_Object((1,3,6,1,4,1,1916,1,32,1,4,1,5),_ExtremeCpuMonitorSystemUtilization5secs_Type())
extremeCpuMonitorSystemUtilization5secs.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemUtilization5secs.setStatus(_A)
_ExtremeCpuMonitorSystemUtilization10secs_Type=DisplayString
_ExtremeCpuMonitorSystemUtilization10secs_Object=MibTableColumn
extremeCpuMonitorSystemUtilization10secs=_ExtremeCpuMonitorSystemUtilization10secs_Object((1,3,6,1,4,1,1916,1,32,1,4,1,6),_ExtremeCpuMonitorSystemUtilization10secs_Type())
extremeCpuMonitorSystemUtilization10secs.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemUtilization10secs.setStatus(_A)
_ExtremeCpuMonitorSystemUtilization30secs_Type=DisplayString
_ExtremeCpuMonitorSystemUtilization30secs_Object=MibTableColumn
extremeCpuMonitorSystemUtilization30secs=_ExtremeCpuMonitorSystemUtilization30secs_Object((1,3,6,1,4,1,1916,1,32,1,4,1,7),_ExtremeCpuMonitorSystemUtilization30secs_Type())
extremeCpuMonitorSystemUtilization30secs.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemUtilization30secs.setStatus(_A)
_ExtremeCpuMonitorSystemUtilization1min_Type=DisplayString
_ExtremeCpuMonitorSystemUtilization1min_Object=MibTableColumn
extremeCpuMonitorSystemUtilization1min=_ExtremeCpuMonitorSystemUtilization1min_Object((1,3,6,1,4,1,1916,1,32,1,4,1,8),_ExtremeCpuMonitorSystemUtilization1min_Type())
extremeCpuMonitorSystemUtilization1min.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemUtilization1min.setStatus(_A)
_ExtremeCpuMonitorSystemUtilization5mins_Type=DisplayString
_ExtremeCpuMonitorSystemUtilization5mins_Object=MibTableColumn
extremeCpuMonitorSystemUtilization5mins=_ExtremeCpuMonitorSystemUtilization5mins_Object((1,3,6,1,4,1,1916,1,32,1,4,1,9),_ExtremeCpuMonitorSystemUtilization5mins_Type())
extremeCpuMonitorSystemUtilization5mins.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemUtilization5mins.setStatus(_A)
_ExtremeCpuMonitorSystemUtilization30mins_Type=DisplayString
_ExtremeCpuMonitorSystemUtilization30mins_Object=MibTableColumn
extremeCpuMonitorSystemUtilization30mins=_ExtremeCpuMonitorSystemUtilization30mins_Object((1,3,6,1,4,1,1916,1,32,1,4,1,10),_ExtremeCpuMonitorSystemUtilization30mins_Type())
extremeCpuMonitorSystemUtilization30mins.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemUtilization30mins.setStatus(_A)
_ExtremeCpuMonitorSystemUtilization1hour_Type=DisplayString
_ExtremeCpuMonitorSystemUtilization1hour_Object=MibTableColumn
extremeCpuMonitorSystemUtilization1hour=_ExtremeCpuMonitorSystemUtilization1hour_Object((1,3,6,1,4,1,1916,1,32,1,4,1,11),_ExtremeCpuMonitorSystemUtilization1hour_Type())
extremeCpuMonitorSystemUtilization1hour.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemUtilization1hour.setStatus(_A)
_ExtremeCpuMonitorSystemMaxUtilization_Type=DisplayString
_ExtremeCpuMonitorSystemMaxUtilization_Object=MibTableColumn
extremeCpuMonitorSystemMaxUtilization=_ExtremeCpuMonitorSystemMaxUtilization_Object((1,3,6,1,4,1,1916,1,32,1,4,1,12),_ExtremeCpuMonitorSystemMaxUtilization_Type())
extremeCpuMonitorSystemMaxUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuMonitorSystemMaxUtilization.setStatus(_A)
class _ExtremeCpuMonitorThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ExtremeCpuMonitorThreshold_Type.__name__=_E
_ExtremeCpuMonitorThreshold_Object=MibScalar
extremeCpuMonitorThreshold=_ExtremeCpuMonitorThreshold_Object((1,3,6,1,4,1,1916,1,32,1,5),_ExtremeCpuMonitorThreshold_Type())
extremeCpuMonitorThreshold.setMaxAccess('read-write')
if mibBuilder.loadTexts:extremeCpuMonitorThreshold.setStatus(_A)
_ExtremeCpuMonitorCurrentUtilization_Type=DisplayString
_ExtremeCpuMonitorCurrentUtilization_Object=MibScalar
extremeCpuMonitorCurrentUtilization=_ExtremeCpuMonitorCurrentUtilization_Object((1,3,6,1,4,1,1916,1,32,1,6),_ExtremeCpuMonitorCurrentUtilization_Type())
extremeCpuMonitorCurrentUtilization.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeCpuMonitorCurrentUtilization.setStatus(_A)
_ExtremeSwMonitorMemory_ObjectIdentity=ObjectIdentity
extremeSwMonitorMemory=_ExtremeSwMonitorMemory_ObjectIdentity((1,3,6,1,4,1,1916,1,32,2))
_ExtremeMemoryMonitorSystemTable_Object=MibTable
extremeMemoryMonitorSystemTable=_ExtremeMemoryMonitorSystemTable_Object((1,3,6,1,4,1,1916,1,32,2,2))
if mibBuilder.loadTexts:extremeMemoryMonitorSystemTable.setStatus(_A)
_ExtremeMemoryMonitorSystemEntry_Object=MibTableRow
extremeMemoryMonitorSystemEntry=_ExtremeMemoryMonitorSystemEntry_Object((1,3,6,1,4,1,1916,1,32,2,2,1))
extremeMemoryMonitorSystemEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:extremeMemoryMonitorSystemEntry.setStatus(_A)
_ExtremeMemoryMonitorSystemSlotId_Type=Unsigned32
_ExtremeMemoryMonitorSystemSlotId_Object=MibTableColumn
extremeMemoryMonitorSystemSlotId=_ExtremeMemoryMonitorSystemSlotId_Object((1,3,6,1,4,1,1916,1,32,2,2,1,1),_ExtremeMemoryMonitorSystemSlotId_Type())
extremeMemoryMonitorSystemSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorSystemSlotId.setStatus(_A)
class _ExtremeMemoryMonitorSystemTotal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ExtremeMemoryMonitorSystemTotal_Type.__name__=_D
_ExtremeMemoryMonitorSystemTotal_Object=MibTableColumn
extremeMemoryMonitorSystemTotal=_ExtremeMemoryMonitorSystemTotal_Object((1,3,6,1,4,1,1916,1,32,2,2,1,2),_ExtremeMemoryMonitorSystemTotal_Type())
extremeMemoryMonitorSystemTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorSystemTotal.setStatus(_A)
class _ExtremeMemoryMonitorSystemFree_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ExtremeMemoryMonitorSystemFree_Type.__name__=_D
_ExtremeMemoryMonitorSystemFree_Object=MibTableColumn
extremeMemoryMonitorSystemFree=_ExtremeMemoryMonitorSystemFree_Object((1,3,6,1,4,1,1916,1,32,2,2,1,3),_ExtremeMemoryMonitorSystemFree_Type())
extremeMemoryMonitorSystemFree.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorSystemFree.setStatus(_A)
class _ExtremeMemoryMonitorSystemUsage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ExtremeMemoryMonitorSystemUsage_Type.__name__=_D
_ExtremeMemoryMonitorSystemUsage_Object=MibTableColumn
extremeMemoryMonitorSystemUsage=_ExtremeMemoryMonitorSystemUsage_Object((1,3,6,1,4,1,1916,1,32,2,2,1,4),_ExtremeMemoryMonitorSystemUsage_Type())
extremeMemoryMonitorSystemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorSystemUsage.setStatus(_A)
class _ExtremeMemoryMonitorUserUsage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ExtremeMemoryMonitorUserUsage_Type.__name__=_D
_ExtremeMemoryMonitorUserUsage_Object=MibTableColumn
extremeMemoryMonitorUserUsage=_ExtremeMemoryMonitorUserUsage_Object((1,3,6,1,4,1,1916,1,32,2,2,1,5),_ExtremeMemoryMonitorUserUsage_Type())
extremeMemoryMonitorUserUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorUserUsage.setStatus(_A)
_ExtremeMemoryMonitorTable_Object=MibTable
extremeMemoryMonitorTable=_ExtremeMemoryMonitorTable_Object((1,3,6,1,4,1,1916,1,32,2,3))
if mibBuilder.loadTexts:extremeMemoryMonitorTable.setStatus(_A)
_ExtremeMemoryMonitorEntry_Object=MibTableRow
extremeMemoryMonitorEntry=_ExtremeMemoryMonitorEntry_Object((1,3,6,1,4,1,1916,1,32,2,3,1))
extremeMemoryMonitorEntry.setIndexNames((0,_C,_P),(1,_C,_Q))
if mibBuilder.loadTexts:extremeMemoryMonitorEntry.setStatus(_A)
_ExtremeMemoryMonitorSlotId_Type=Unsigned32
_ExtremeMemoryMonitorSlotId_Object=MibTableColumn
extremeMemoryMonitorSlotId=_ExtremeMemoryMonitorSlotId_Object((1,3,6,1,4,1,1916,1,32,2,3,1,1),_ExtremeMemoryMonitorSlotId_Type())
extremeMemoryMonitorSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorSlotId.setStatus(_A)
class _ExtremeMemoryMonitorProcessName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ExtremeMemoryMonitorProcessName_Type.__name__=_D
_ExtremeMemoryMonitorProcessName_Object=MibTableColumn
extremeMemoryMonitorProcessName=_ExtremeMemoryMonitorProcessName_Object((1,3,6,1,4,1,1916,1,32,2,3,1,2),_ExtremeMemoryMonitorProcessName_Type())
extremeMemoryMonitorProcessName.setMaxAccess(_M)
if mibBuilder.loadTexts:extremeMemoryMonitorProcessName.setStatus(_A)
_ExtremeMemoryMonitorUsage_Type=Unsigned32
_ExtremeMemoryMonitorUsage_Object=MibTableColumn
extremeMemoryMonitorUsage=_ExtremeMemoryMonitorUsage_Object((1,3,6,1,4,1,1916,1,32,2,3,1,3),_ExtremeMemoryMonitorUsage_Type())
extremeMemoryMonitorUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorUsage.setStatus(_A)
_ExtremeMemoryMonitorLimit_Type=Unsigned32
_ExtremeMemoryMonitorLimit_Object=MibTableColumn
extremeMemoryMonitorLimit=_ExtremeMemoryMonitorLimit_Object((1,3,6,1,4,1,1916,1,32,2,3,1,4),_ExtremeMemoryMonitorLimit_Type())
extremeMemoryMonitorLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorLimit.setStatus(_A)
class _ExtremeMemoryMonitorZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ExtremeMemoryMonitorZone_Type.__name__=_D
_ExtremeMemoryMonitorZone_Object=MibTableColumn
extremeMemoryMonitorZone=_ExtremeMemoryMonitorZone_Object((1,3,6,1,4,1,1916,1,32,2,3,1,5),_ExtremeMemoryMonitorZone_Type())
extremeMemoryMonitorZone.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorZone.setStatus(_A)
_ExtremeMemoryMonitorGreenZoneCount_Type=Unsigned32
_ExtremeMemoryMonitorGreenZoneCount_Object=MibTableColumn
extremeMemoryMonitorGreenZoneCount=_ExtremeMemoryMonitorGreenZoneCount_Object((1,3,6,1,4,1,1916,1,32,2,3,1,6),_ExtremeMemoryMonitorGreenZoneCount_Type())
extremeMemoryMonitorGreenZoneCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorGreenZoneCount.setStatus(_A)
_ExtremeMemoryMonitorYellowZoneCount_Type=Unsigned32
_ExtremeMemoryMonitorYellowZoneCount_Object=MibTableColumn
extremeMemoryMonitorYellowZoneCount=_ExtremeMemoryMonitorYellowZoneCount_Object((1,3,6,1,4,1,1916,1,32,2,3,1,7),_ExtremeMemoryMonitorYellowZoneCount_Type())
extremeMemoryMonitorYellowZoneCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorYellowZoneCount.setStatus(_A)
_ExtremeMemoryMonitorOrangeZoneCount_Type=Unsigned32
_ExtremeMemoryMonitorOrangeZoneCount_Object=MibTableColumn
extremeMemoryMonitorOrangeZoneCount=_ExtremeMemoryMonitorOrangeZoneCount_Object((1,3,6,1,4,1,1916,1,32,2,3,1,8),_ExtremeMemoryMonitorOrangeZoneCount_Type())
extremeMemoryMonitorOrangeZoneCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorOrangeZoneCount.setStatus(_A)
_ExtremeMemoryMonitorRedZoneCount_Type=Unsigned32
_ExtremeMemoryMonitorRedZoneCount_Object=MibTableColumn
extremeMemoryMonitorRedZoneCount=_ExtremeMemoryMonitorRedZoneCount_Object((1,3,6,1,4,1,1916,1,32,2,3,1,9),_ExtremeMemoryMonitorRedZoneCount_Type())
extremeMemoryMonitorRedZoneCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorRedZoneCount.setStatus(_A)
_ExtremeMemoryMonitorGreenZoneThreshold_Type=Unsigned32
_ExtremeMemoryMonitorGreenZoneThreshold_Object=MibTableColumn
extremeMemoryMonitorGreenZoneThreshold=_ExtremeMemoryMonitorGreenZoneThreshold_Object((1,3,6,1,4,1,1916,1,32,2,3,1,10),_ExtremeMemoryMonitorGreenZoneThreshold_Type())
extremeMemoryMonitorGreenZoneThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorGreenZoneThreshold.setStatus(_A)
_ExtremeMemoryMonitorYellowZoneThreshold_Type=Unsigned32
_ExtremeMemoryMonitorYellowZoneThreshold_Object=MibTableColumn
extremeMemoryMonitorYellowZoneThreshold=_ExtremeMemoryMonitorYellowZoneThreshold_Object((1,3,6,1,4,1,1916,1,32,2,3,1,11),_ExtremeMemoryMonitorYellowZoneThreshold_Type())
extremeMemoryMonitorYellowZoneThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorYellowZoneThreshold.setStatus(_A)
_ExtremeMemoryMonitorOrangeZoneThreshold_Type=Unsigned32
_ExtremeMemoryMonitorOrangeZoneThreshold_Object=MibTableColumn
extremeMemoryMonitorOrangeZoneThreshold=_ExtremeMemoryMonitorOrangeZoneThreshold_Object((1,3,6,1,4,1,1916,1,32,2,3,1,12),_ExtremeMemoryMonitorOrangeZoneThreshold_Type())
extremeMemoryMonitorOrangeZoneThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorOrangeZoneThreshold.setStatus(_A)
_ExtremeMemoryMonitorRedZoneThreshold_Type=Unsigned32
_ExtremeMemoryMonitorRedZoneThreshold_Object=MibTableColumn
extremeMemoryMonitorRedZoneThreshold=_ExtremeMemoryMonitorRedZoneThreshold_Object((1,3,6,1,4,1,1916,1,32,2,3,1,13),_ExtremeMemoryMonitorRedZoneThreshold_Type())
extremeMemoryMonitorRedZoneThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMemoryMonitorRedZoneThreshold.setStatus(_A)
_ExtremeSwMonitorNotifications_ObjectIdentity=ObjectIdentity
extremeSwMonitorNotifications=_ExtremeSwMonitorNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,32,3))
_ExtremeSwMonitorNotificationsPrefix_ObjectIdentity=ObjectIdentity
extremeSwMonitorNotificationsPrefix=_ExtremeSwMonitorNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,32,3,0))
_ExtremeServiceLicense_ObjectIdentity=ObjectIdentity
extremeServiceLicense=_ExtremeServiceLicense_ObjectIdentity((1,3,6,1,4,1,1916,1,32,4))
_ExtremeServiceLicenseExpiryDate_Type=DisplayString
_ExtremeServiceLicenseExpiryDate_Object=MibScalar
extremeServiceLicenseExpiryDate=_ExtremeServiceLicenseExpiryDate_Object((1,3,6,1,4,1,1916,1,32,4,1),_ExtremeServiceLicenseExpiryDate_Type())
extremeServiceLicenseExpiryDate.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeServiceLicenseExpiryDate.setStatus(_A)
_ExtremeServiceLicenseType_Type=DisplayString
_ExtremeServiceLicenseType_Object=MibScalar
extremeServiceLicenseType=_ExtremeServiceLicenseType_Object((1,3,6,1,4,1,1916,1,32,4,2),_ExtremeServiceLicenseType_Type())
extremeServiceLicenseType.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeServiceLicenseType.setStatus(_A)
_ImageDescription_Type=DisplayString
_ImageDescription_Object=MibScalar
imageDescription=_ImageDescription_Object((1,3,6,1,4,1,1916,1,32,4,3),_ImageDescription_Type())
imageDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:imageDescription.setStatus(_A)
class _NoOfDaysLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_NoOfDaysLeft_Type.__name__=_E
_NoOfDaysLeft_Object=MibScalar
noOfDaysLeft=_NoOfDaysLeft_Object((1,3,6,1,4,1,1916,1,32,4,4),_NoOfDaysLeft_Type())
noOfDaysLeft.setMaxAccess(_F)
if mibBuilder.loadTexts:noOfDaysLeft.setStatus(_A)
_ExtremeTrialLicense_ObjectIdentity=ObjectIdentity
extremeTrialLicense=_ExtremeTrialLicense_ObjectIdentity((1,3,6,1,4,1,1916,1,32,5))
class _TrialPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_TrialPeriod_Type.__name__=_E
_TrialPeriod_Object=MibScalar
trialPeriod=_TrialPeriod_Object((1,3,6,1,4,1,1916,1,32,5,1),_TrialPeriod_Type())
trialPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:trialPeriod.setStatus(_A)
extremeSwMonitorCpuUtilization=NotificationType((1,3,6,1,4,1,1916,1,32,3,0,1))
extremeSwMonitorCpuUtilization.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:extremeSwMonitorCpuUtilization.setStatus(_A)
extremeServiceLicenseExpiration=NotificationType((1,3,6,1,4,1,1916,1,32,3,0,2))
extremeServiceLicenseExpiration.setObjects(*((_C,_R),(_C,_S),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:extremeServiceLicenseExpiration.setStatus(_A)
extremeTrialLicenseExpiration=NotificationType((1,3,6,1,4,1,1916,1,32,3,0,3))
extremeTrialLicenseExpiration.setObjects(*((_C,_T),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:extremeTrialLicenseExpiration.setStatus(_A)
extremeSwMonitorCpuUtilizationNormal=NotificationType((1,3,6,1,4,1,1916,1,32,3,0,4))
extremeSwMonitorCpuUtilizationNormal.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:extremeSwMonitorCpuUtilizationNormal.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'extremeSwMonitor':extremeSwMonitor,'extremeSwMonitorCpu':extremeSwMonitorCpu,'extremeCpuMonitorInterval':extremeCpuMonitorInterval,'extremeCpuMonitorTotalUtilization':extremeCpuMonitorTotalUtilization,'extremeCpuMonitorTable':extremeCpuMonitorTable,'extremeCpuMonitorEntry':extremeCpuMonitorEntry,_G:extremeCpuMonitorSlotId,_H:extremeCpuMonitorProcessName,'extremeCpuMonitorProcessId':extremeCpuMonitorProcessId,'extremeCpuMonitorProcessState':extremeCpuMonitorProcessState,'extremeCpuMonitorUtilization5secs':extremeCpuMonitorUtilization5secs,'extremeCpuMonitorUtilization10secs':extremeCpuMonitorUtilization10secs,'extremeCpuMonitorUtilization30secs':extremeCpuMonitorUtilization30secs,'extremeCpuMonitorUtilization1min':extremeCpuMonitorUtilization1min,'extremeCpuMonitorUtilization5mins':extremeCpuMonitorUtilization5mins,'extremeCpuMonitorUtilization30mins':extremeCpuMonitorUtilization30mins,'extremeCpuMonitorUtilization1hour':extremeCpuMonitorUtilization1hour,'extremeCpuMonitorMaxUtilization':extremeCpuMonitorMaxUtilization,'extremeCpuMonitorUserTime':extremeCpuMonitorUserTime,'extremeCpuMonitorSystemTime':extremeCpuMonitorSystemTime,'extremeCpuMonitorSystemTable':extremeCpuMonitorSystemTable,'extremeCpuMonitorSystemEntry':extremeCpuMonitorSystemEntry,_N:extremeCpuMonitorSystemSlotId,'extremeCpuMonitorSystemUtilization5secs':extremeCpuMonitorSystemUtilization5secs,'extremeCpuMonitorSystemUtilization10secs':extremeCpuMonitorSystemUtilization10secs,'extremeCpuMonitorSystemUtilization30secs':extremeCpuMonitorSystemUtilization30secs,'extremeCpuMonitorSystemUtilization1min':extremeCpuMonitorSystemUtilization1min,'extremeCpuMonitorSystemUtilization5mins':extremeCpuMonitorSystemUtilization5mins,'extremeCpuMonitorSystemUtilization30mins':extremeCpuMonitorSystemUtilization30mins,'extremeCpuMonitorSystemUtilization1hour':extremeCpuMonitorSystemUtilization1hour,'extremeCpuMonitorSystemMaxUtilization':extremeCpuMonitorSystemMaxUtilization,_J:extremeCpuMonitorThreshold,_I:extremeCpuMonitorCurrentUtilization,'extremeSwMonitorMemory':extremeSwMonitorMemory,'extremeMemoryMonitorSystemTable':extremeMemoryMonitorSystemTable,'extremeMemoryMonitorSystemEntry':extremeMemoryMonitorSystemEntry,_O:extremeMemoryMonitorSystemSlotId,'extremeMemoryMonitorSystemTotal':extremeMemoryMonitorSystemTotal,'extremeMemoryMonitorSystemFree':extremeMemoryMonitorSystemFree,'extremeMemoryMonitorSystemUsage':extremeMemoryMonitorSystemUsage,'extremeMemoryMonitorUserUsage':extremeMemoryMonitorUserUsage,'extremeMemoryMonitorTable':extremeMemoryMonitorTable,'extremeMemoryMonitorEntry':extremeMemoryMonitorEntry,_P:extremeMemoryMonitorSlotId,_Q:extremeMemoryMonitorProcessName,'extremeMemoryMonitorUsage':extremeMemoryMonitorUsage,'extremeMemoryMonitorLimit':extremeMemoryMonitorLimit,'extremeMemoryMonitorZone':extremeMemoryMonitorZone,'extremeMemoryMonitorGreenZoneCount':extremeMemoryMonitorGreenZoneCount,'extremeMemoryMonitorYellowZoneCount':extremeMemoryMonitorYellowZoneCount,'extremeMemoryMonitorOrangeZoneCount':extremeMemoryMonitorOrangeZoneCount,'extremeMemoryMonitorRedZoneCount':extremeMemoryMonitorRedZoneCount,'extremeMemoryMonitorGreenZoneThreshold':extremeMemoryMonitorGreenZoneThreshold,'extremeMemoryMonitorYellowZoneThreshold':extremeMemoryMonitorYellowZoneThreshold,'extremeMemoryMonitorOrangeZoneThreshold':extremeMemoryMonitorOrangeZoneThreshold,'extremeMemoryMonitorRedZoneThreshold':extremeMemoryMonitorRedZoneThreshold,'extremeSwMonitorNotifications':extremeSwMonitorNotifications,'extremeSwMonitorNotificationsPrefix':extremeSwMonitorNotificationsPrefix,'extremeSwMonitorCpuUtilization':extremeSwMonitorCpuUtilization,'extremeServiceLicenseExpiration':extremeServiceLicenseExpiration,'extremeTrialLicenseExpiration':extremeTrialLicenseExpiration,'extremeSwMonitorCpuUtilizationNormal':extremeSwMonitorCpuUtilizationNormal,'extremeServiceLicense':extremeServiceLicense,_R:extremeServiceLicenseExpiryDate,_S:extremeServiceLicenseType,_K:imageDescription,_L:noOfDaysLeft,'extremeTrialLicense':extremeTrialLicense,_T:trialPeriod})