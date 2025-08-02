_K='memorySlotId'
_J='cpuCoreCoreId'
_I='memoryChassisId'
_H='not-accessible'
_G='cpuSlotId'
_F='cpuChassisId'
_E='DMOS-SYSMON-MIB'
_D='Bytes'
_C='%'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
datacomDevicesMIBs,=mibBuilder.importSymbols('DATACOM-SMI','datacomDevicesMIBs')
Unsigned8,UnsignedPercent=mibBuilder.importSymbols('DMOS-TC-MIB','Unsigned8','UnsignedPercent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dmosSysmonMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,4))
if mibBuilder.loadTexts:dmosSysmonMIB.setRevisions(('2016-02-12 00:00',))
_Cpu_ObjectIdentity=ObjectIdentity
cpu=_Cpu_ObjectIdentity((1,3,6,1,4,1,3709,3,6,4,1))
_CpuChassisTable_Object=MibTable
cpuChassisTable=_CpuChassisTable_Object((1,3,6,1,4,1,3709,3,6,4,1,1))
if mibBuilder.loadTexts:cpuChassisTable.setStatus(_A)
_CpuChassisEntry_Object=MibTableRow
cpuChassisEntry=_CpuChassisEntry_Object((1,3,6,1,4,1,3709,3,6,4,1,1,1))
cpuChassisEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cpuChassisEntry.setStatus(_A)
_CpuChassisId_Type=Unsigned32
_CpuChassisId_Object=MibTableColumn
cpuChassisId=_CpuChassisId_Object((1,3,6,1,4,1,3709,3,6,4,1,1,1,1),_CpuChassisId_Type())
cpuChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuChassisId.setStatus(_A)
_CpuSlotTable_Object=MibTable
cpuSlotTable=_CpuSlotTable_Object((1,3,6,1,4,1,3709,3,6,4,1,2))
if mibBuilder.loadTexts:cpuSlotTable.setStatus(_A)
_CpuSlotEntry_Object=MibTableRow
cpuSlotEntry=_CpuSlotEntry_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1))
cpuSlotEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:cpuSlotEntry.setStatus(_A)
_CpuSlotId_Type=DisplayString
_CpuSlotId_Object=MibTableColumn
cpuSlotId=_CpuSlotId_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1,1),_CpuSlotId_Type())
cpuSlotId.setMaxAccess(_H)
if mibBuilder.loadTexts:cpuSlotId.setStatus(_A)
_CpuLoadFiveSecondsActive_Type=UnsignedPercent
_CpuLoadFiveSecondsActive_Object=MibTableColumn
cpuLoadFiveSecondsActive=_CpuLoadFiveSecondsActive_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1,2),_CpuLoadFiveSecondsActive_Type())
cpuLoadFiveSecondsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoadFiveSecondsActive.setStatus(_A)
if mibBuilder.loadTexts:cpuLoadFiveSecondsActive.setUnits(_C)
_CpuLoadFiveSecondsIdle_Type=UnsignedPercent
_CpuLoadFiveSecondsIdle_Object=MibTableColumn
cpuLoadFiveSecondsIdle=_CpuLoadFiveSecondsIdle_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1,3),_CpuLoadFiveSecondsIdle_Type())
cpuLoadFiveSecondsIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoadFiveSecondsIdle.setStatus(_A)
if mibBuilder.loadTexts:cpuLoadFiveSecondsIdle.setUnits(_C)
_CpuLoadOneMinuteActive_Type=UnsignedPercent
_CpuLoadOneMinuteActive_Object=MibTableColumn
cpuLoadOneMinuteActive=_CpuLoadOneMinuteActive_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1,4),_CpuLoadOneMinuteActive_Type())
cpuLoadOneMinuteActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoadOneMinuteActive.setStatus(_A)
if mibBuilder.loadTexts:cpuLoadOneMinuteActive.setUnits(_C)
_CpuLoadOneMinuteIdle_Type=UnsignedPercent
_CpuLoadOneMinuteIdle_Object=MibTableColumn
cpuLoadOneMinuteIdle=_CpuLoadOneMinuteIdle_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1,5),_CpuLoadOneMinuteIdle_Type())
cpuLoadOneMinuteIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoadOneMinuteIdle.setStatus(_A)
if mibBuilder.loadTexts:cpuLoadOneMinuteIdle.setUnits(_C)
_CpuLoadFiveMinutesActive_Type=UnsignedPercent
_CpuLoadFiveMinutesActive_Object=MibTableColumn
cpuLoadFiveMinutesActive=_CpuLoadFiveMinutesActive_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1,6),_CpuLoadFiveMinutesActive_Type())
cpuLoadFiveMinutesActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoadFiveMinutesActive.setStatus(_A)
if mibBuilder.loadTexts:cpuLoadFiveMinutesActive.setUnits(_C)
_CpuLoadFiveMinutesIdle_Type=UnsignedPercent
_CpuLoadFiveMinutesIdle_Object=MibTableColumn
cpuLoadFiveMinutesIdle=_CpuLoadFiveMinutesIdle_Object((1,3,6,1,4,1,3709,3,6,4,1,2,1,7),_CpuLoadFiveMinutesIdle_Type())
cpuLoadFiveMinutesIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoadFiveMinutesIdle.setStatus(_A)
if mibBuilder.loadTexts:cpuLoadFiveMinutesIdle.setUnits(_C)
_CpuCoreTable_Object=MibTable
cpuCoreTable=_CpuCoreTable_Object((1,3,6,1,4,1,3709,3,6,4,1,3))
if mibBuilder.loadTexts:cpuCoreTable.setStatus(_A)
_CpuCoreEntry_Object=MibTableRow
cpuCoreEntry=_CpuCoreEntry_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1))
cpuCoreEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_E,_J))
if mibBuilder.loadTexts:cpuCoreEntry.setStatus(_A)
_CpuCoreCoreId_Type=Unsigned8
_CpuCoreCoreId_Object=MibTableColumn
cpuCoreCoreId=_CpuCoreCoreId_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,1),_CpuCoreCoreId_Type())
cpuCoreCoreId.setMaxAccess(_H)
if mibBuilder.loadTexts:cpuCoreCoreId.setStatus(_A)
_CpuCoreFiveSecondsActive_Type=UnsignedPercent
_CpuCoreFiveSecondsActive_Object=MibTableColumn
cpuCoreFiveSecondsActive=_CpuCoreFiveSecondsActive_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,2),_CpuCoreFiveSecondsActive_Type())
cpuCoreFiveSecondsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsActive.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsActive.setUnits(_C)
_CpuCoreFiveSecondsUser_Type=UnsignedPercent
_CpuCoreFiveSecondsUser_Object=MibTableColumn
cpuCoreFiveSecondsUser=_CpuCoreFiveSecondsUser_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,3),_CpuCoreFiveSecondsUser_Type())
cpuCoreFiveSecondsUser.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsUser.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsUser.setUnits(_C)
_CpuCoreFiveSecondsSystem_Type=UnsignedPercent
_CpuCoreFiveSecondsSystem_Object=MibTableColumn
cpuCoreFiveSecondsSystem=_CpuCoreFiveSecondsSystem_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,4),_CpuCoreFiveSecondsSystem_Type())
cpuCoreFiveSecondsSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsSystem.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsSystem.setUnits(_C)
_CpuCoreFiveSecondsNice_Type=UnsignedPercent
_CpuCoreFiveSecondsNice_Object=MibTableColumn
cpuCoreFiveSecondsNice=_CpuCoreFiveSecondsNice_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,5),_CpuCoreFiveSecondsNice_Type())
cpuCoreFiveSecondsNice.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsNice.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsNice.setUnits(_C)
_CpuCoreFiveSecondsIdle_Type=UnsignedPercent
_CpuCoreFiveSecondsIdle_Object=MibTableColumn
cpuCoreFiveSecondsIdle=_CpuCoreFiveSecondsIdle_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,6),_CpuCoreFiveSecondsIdle_Type())
cpuCoreFiveSecondsIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsIdle.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsIdle.setUnits(_C)
_CpuCoreFiveSecondsWait_Type=UnsignedPercent
_CpuCoreFiveSecondsWait_Object=MibTableColumn
cpuCoreFiveSecondsWait=_CpuCoreFiveSecondsWait_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,7),_CpuCoreFiveSecondsWait_Type())
cpuCoreFiveSecondsWait.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsWait.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsWait.setUnits(_C)
_CpuCoreFiveSecondsInterrupt_Type=UnsignedPercent
_CpuCoreFiveSecondsInterrupt_Object=MibTableColumn
cpuCoreFiveSecondsInterrupt=_CpuCoreFiveSecondsInterrupt_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,8),_CpuCoreFiveSecondsInterrupt_Type())
cpuCoreFiveSecondsInterrupt.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsInterrupt.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsInterrupt.setUnits(_C)
_CpuCoreFiveSecondsSoftirq_Type=UnsignedPercent
_CpuCoreFiveSecondsSoftirq_Object=MibTableColumn
cpuCoreFiveSecondsSoftirq=_CpuCoreFiveSecondsSoftirq_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,9),_CpuCoreFiveSecondsSoftirq_Type())
cpuCoreFiveSecondsSoftirq.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveSecondsSoftirq.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveSecondsSoftirq.setUnits(_C)
_CpuCoreOneMinuteActive_Type=UnsignedPercent
_CpuCoreOneMinuteActive_Object=MibTableColumn
cpuCoreOneMinuteActive=_CpuCoreOneMinuteActive_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,10),_CpuCoreOneMinuteActive_Type())
cpuCoreOneMinuteActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteActive.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteActive.setUnits(_C)
_CpuCoreOneMinuteUser_Type=UnsignedPercent
_CpuCoreOneMinuteUser_Object=MibTableColumn
cpuCoreOneMinuteUser=_CpuCoreOneMinuteUser_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,11),_CpuCoreOneMinuteUser_Type())
cpuCoreOneMinuteUser.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteUser.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteUser.setUnits(_C)
_CpuCoreOneMinuteSystem_Type=UnsignedPercent
_CpuCoreOneMinuteSystem_Object=MibTableColumn
cpuCoreOneMinuteSystem=_CpuCoreOneMinuteSystem_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,12),_CpuCoreOneMinuteSystem_Type())
cpuCoreOneMinuteSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteSystem.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteSystem.setUnits(_C)
_CpuCoreOneMinuteNice_Type=UnsignedPercent
_CpuCoreOneMinuteNice_Object=MibTableColumn
cpuCoreOneMinuteNice=_CpuCoreOneMinuteNice_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,13),_CpuCoreOneMinuteNice_Type())
cpuCoreOneMinuteNice.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteNice.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteNice.setUnits(_C)
_CpuCoreOneMinuteIdle_Type=UnsignedPercent
_CpuCoreOneMinuteIdle_Object=MibTableColumn
cpuCoreOneMinuteIdle=_CpuCoreOneMinuteIdle_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,14),_CpuCoreOneMinuteIdle_Type())
cpuCoreOneMinuteIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteIdle.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteIdle.setUnits(_C)
_CpuCoreOneMinuteWait_Type=UnsignedPercent
_CpuCoreOneMinuteWait_Object=MibTableColumn
cpuCoreOneMinuteWait=_CpuCoreOneMinuteWait_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,15),_CpuCoreOneMinuteWait_Type())
cpuCoreOneMinuteWait.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteWait.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteWait.setUnits(_C)
_CpuCoreOneMinuteInterrupt_Type=UnsignedPercent
_CpuCoreOneMinuteInterrupt_Object=MibTableColumn
cpuCoreOneMinuteInterrupt=_CpuCoreOneMinuteInterrupt_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,16),_CpuCoreOneMinuteInterrupt_Type())
cpuCoreOneMinuteInterrupt.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteInterrupt.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteInterrupt.setUnits(_C)
_CpuCoreOneMinuteSoftirq_Type=UnsignedPercent
_CpuCoreOneMinuteSoftirq_Object=MibTableColumn
cpuCoreOneMinuteSoftirq=_CpuCoreOneMinuteSoftirq_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,17),_CpuCoreOneMinuteSoftirq_Type())
cpuCoreOneMinuteSoftirq.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreOneMinuteSoftirq.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreOneMinuteSoftirq.setUnits(_C)
_CpuCoreFiveMinutesActive_Type=UnsignedPercent
_CpuCoreFiveMinutesActive_Object=MibTableColumn
cpuCoreFiveMinutesActive=_CpuCoreFiveMinutesActive_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,18),_CpuCoreFiveMinutesActive_Type())
cpuCoreFiveMinutesActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesActive.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesActive.setUnits(_C)
_CpuCoreFiveMinutesUser_Type=UnsignedPercent
_CpuCoreFiveMinutesUser_Object=MibTableColumn
cpuCoreFiveMinutesUser=_CpuCoreFiveMinutesUser_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,19),_CpuCoreFiveMinutesUser_Type())
cpuCoreFiveMinutesUser.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesUser.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesUser.setUnits(_C)
_CpuCoreFiveMinutesSystem_Type=UnsignedPercent
_CpuCoreFiveMinutesSystem_Object=MibTableColumn
cpuCoreFiveMinutesSystem=_CpuCoreFiveMinutesSystem_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,20),_CpuCoreFiveMinutesSystem_Type())
cpuCoreFiveMinutesSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesSystem.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesSystem.setUnits(_C)
_CpuCoreFiveMinutesNice_Type=UnsignedPercent
_CpuCoreFiveMinutesNice_Object=MibTableColumn
cpuCoreFiveMinutesNice=_CpuCoreFiveMinutesNice_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,21),_CpuCoreFiveMinutesNice_Type())
cpuCoreFiveMinutesNice.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesNice.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesNice.setUnits(_C)
_CpuCoreFiveMinutesIdle_Type=UnsignedPercent
_CpuCoreFiveMinutesIdle_Object=MibTableColumn
cpuCoreFiveMinutesIdle=_CpuCoreFiveMinutesIdle_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,22),_CpuCoreFiveMinutesIdle_Type())
cpuCoreFiveMinutesIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesIdle.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesIdle.setUnits(_C)
_CpuCoreFiveMinutesWait_Type=UnsignedPercent
_CpuCoreFiveMinutesWait_Object=MibTableColumn
cpuCoreFiveMinutesWait=_CpuCoreFiveMinutesWait_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,23),_CpuCoreFiveMinutesWait_Type())
cpuCoreFiveMinutesWait.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesWait.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesWait.setUnits(_C)
_CpuCoreFiveMinutesInterrupt_Type=UnsignedPercent
_CpuCoreFiveMinutesInterrupt_Object=MibTableColumn
cpuCoreFiveMinutesInterrupt=_CpuCoreFiveMinutesInterrupt_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,24),_CpuCoreFiveMinutesInterrupt_Type())
cpuCoreFiveMinutesInterrupt.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesInterrupt.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesInterrupt.setUnits(_C)
_CpuCoreFiveMinutesSoftirq_Type=UnsignedPercent
_CpuCoreFiveMinutesSoftirq_Object=MibTableColumn
cpuCoreFiveMinutesSoftirq=_CpuCoreFiveMinutesSoftirq_Object((1,3,6,1,4,1,3709,3,6,4,1,3,1,25),_CpuCoreFiveMinutesSoftirq_Type())
cpuCoreFiveMinutesSoftirq.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreFiveMinutesSoftirq.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreFiveMinutesSoftirq.setUnits(_C)
_Memory_ObjectIdentity=ObjectIdentity
memory=_Memory_ObjectIdentity((1,3,6,1,4,1,3709,3,6,4,2))
_MemoryChassisTable_Object=MibTable
memoryChassisTable=_MemoryChassisTable_Object((1,3,6,1,4,1,3709,3,6,4,2,1))
if mibBuilder.loadTexts:memoryChassisTable.setStatus(_A)
_MemoryChassisEntry_Object=MibTableRow
memoryChassisEntry=_MemoryChassisEntry_Object((1,3,6,1,4,1,3709,3,6,4,2,1,1))
memoryChassisEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:memoryChassisEntry.setStatus(_A)
_MemoryChassisId_Type=Unsigned32
_MemoryChassisId_Object=MibTableColumn
memoryChassisId=_MemoryChassisId_Object((1,3,6,1,4,1,3709,3,6,4,2,1,1,1),_MemoryChassisId_Type())
memoryChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryChassisId.setStatus(_A)
_MemorySlotTable_Object=MibTable
memorySlotTable=_MemorySlotTable_Object((1,3,6,1,4,1,3709,3,6,4,2,2))
if mibBuilder.loadTexts:memorySlotTable.setStatus(_A)
_MemorySlotEntry_Object=MibTableRow
memorySlotEntry=_MemorySlotEntry_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1))
memorySlotEntry.setIndexNames((0,_E,_I),(0,_E,_K))
if mibBuilder.loadTexts:memorySlotEntry.setStatus(_A)
_MemorySlotId_Type=DisplayString
_MemorySlotId_Object=MibTableColumn
memorySlotId=_MemorySlotId_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,1),_MemorySlotId_Type())
memorySlotId.setMaxAccess(_H)
if mibBuilder.loadTexts:memorySlotId.setStatus(_A)
_MemoryFiveSecondsTotal_Type=Unsigned32
_MemoryFiveSecondsTotal_Object=MibTableColumn
memoryFiveSecondsTotal=_MemoryFiveSecondsTotal_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,2),_MemoryFiveSecondsTotal_Type())
memoryFiveSecondsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsTotal.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsTotal.setUnits(_D)
_MemoryFiveSecondsUsed_Type=Unsigned32
_MemoryFiveSecondsUsed_Object=MibTableColumn
memoryFiveSecondsUsed=_MemoryFiveSecondsUsed_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,3),_MemoryFiveSecondsUsed_Type())
memoryFiveSecondsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsUsed.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsUsed.setUnits(_D)
_MemoryFiveSecondsFree_Type=Unsigned32
_MemoryFiveSecondsFree_Object=MibTableColumn
memoryFiveSecondsFree=_MemoryFiveSecondsFree_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,4),_MemoryFiveSecondsFree_Type())
memoryFiveSecondsFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsFree.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsFree.setUnits(_D)
_MemoryFiveSecondsBuffered_Type=Unsigned32
_MemoryFiveSecondsBuffered_Object=MibTableColumn
memoryFiveSecondsBuffered=_MemoryFiveSecondsBuffered_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,5),_MemoryFiveSecondsBuffered_Type())
memoryFiveSecondsBuffered.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsBuffered.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsBuffered.setUnits(_D)
_MemoryFiveSecondsCached_Type=Unsigned32
_MemoryFiveSecondsCached_Object=MibTableColumn
memoryFiveSecondsCached=_MemoryFiveSecondsCached_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,6),_MemoryFiveSecondsCached_Type())
memoryFiveSecondsCached.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsCached.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsCached.setUnits(_D)
_MemoryFiveSecondsAvailable_Type=Unsigned32
_MemoryFiveSecondsAvailable_Object=MibTableColumn
memoryFiveSecondsAvailable=_MemoryFiveSecondsAvailable_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,7),_MemoryFiveSecondsAvailable_Type())
memoryFiveSecondsAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsAvailable.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsAvailable.setUnits(_D)
_MemoryFiveSecondsSlabRecl_Type=Unsigned32
_MemoryFiveSecondsSlabRecl_Object=MibTableColumn
memoryFiveSecondsSlabRecl=_MemoryFiveSecondsSlabRecl_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,8),_MemoryFiveSecondsSlabRecl_Type())
memoryFiveSecondsSlabRecl.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsSlabRecl.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsSlabRecl.setUnits(_D)
_MemoryFiveSecondsSlabUnrecl_Type=Unsigned32
_MemoryFiveSecondsSlabUnrecl_Object=MibTableColumn
memoryFiveSecondsSlabUnrecl=_MemoryFiveSecondsSlabUnrecl_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,9),_MemoryFiveSecondsSlabUnrecl_Type())
memoryFiveSecondsSlabUnrecl.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveSecondsSlabUnrecl.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveSecondsSlabUnrecl.setUnits(_D)
_MemoryFiveMinutesTotal_Type=Unsigned32
_MemoryFiveMinutesTotal_Object=MibTableColumn
memoryFiveMinutesTotal=_MemoryFiveMinutesTotal_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,10),_MemoryFiveMinutesTotal_Type())
memoryFiveMinutesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesTotal.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesTotal.setUnits(_D)
_MemoryFiveMinutesUsed_Type=Unsigned32
_MemoryFiveMinutesUsed_Object=MibTableColumn
memoryFiveMinutesUsed=_MemoryFiveMinutesUsed_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,11),_MemoryFiveMinutesUsed_Type())
memoryFiveMinutesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesUsed.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesUsed.setUnits(_D)
_MemoryFiveMinutesFree_Type=Unsigned32
_MemoryFiveMinutesFree_Object=MibTableColumn
memoryFiveMinutesFree=_MemoryFiveMinutesFree_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,12),_MemoryFiveMinutesFree_Type())
memoryFiveMinutesFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesFree.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesFree.setUnits(_D)
_MemoryFiveMinutesBuffered_Type=Unsigned32
_MemoryFiveMinutesBuffered_Object=MibTableColumn
memoryFiveMinutesBuffered=_MemoryFiveMinutesBuffered_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,13),_MemoryFiveMinutesBuffered_Type())
memoryFiveMinutesBuffered.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesBuffered.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesBuffered.setUnits(_D)
_MemoryFiveMinutesCached_Type=Unsigned32
_MemoryFiveMinutesCached_Object=MibTableColumn
memoryFiveMinutesCached=_MemoryFiveMinutesCached_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,14),_MemoryFiveMinutesCached_Type())
memoryFiveMinutesCached.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesCached.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesCached.setUnits(_D)
_MemoryFiveMinutesAvailable_Type=Unsigned32
_MemoryFiveMinutesAvailable_Object=MibTableColumn
memoryFiveMinutesAvailable=_MemoryFiveMinutesAvailable_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,15),_MemoryFiveMinutesAvailable_Type())
memoryFiveMinutesAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesAvailable.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesAvailable.setUnits(_D)
_MemoryFiveMinutesSlabRecl_Type=Unsigned32
_MemoryFiveMinutesSlabRecl_Object=MibTableColumn
memoryFiveMinutesSlabRecl=_MemoryFiveMinutesSlabRecl_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,16),_MemoryFiveMinutesSlabRecl_Type())
memoryFiveMinutesSlabRecl.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesSlabRecl.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesSlabRecl.setUnits(_D)
_MemoryFiveMinutesSlabUnrecl_Type=Unsigned32
_MemoryFiveMinutesSlabUnrecl_Object=MibTableColumn
memoryFiveMinutesSlabUnrecl=_MemoryFiveMinutesSlabUnrecl_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,17),_MemoryFiveMinutesSlabUnrecl_Type())
memoryFiveMinutesSlabUnrecl.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFiveMinutesSlabUnrecl.setStatus(_A)
if mibBuilder.loadTexts:memoryFiveMinutesSlabUnrecl.setUnits(_D)
_MemoryThirtyMinutesTotal_Type=Unsigned32
_MemoryThirtyMinutesTotal_Object=MibTableColumn
memoryThirtyMinutesTotal=_MemoryThirtyMinutesTotal_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,18),_MemoryThirtyMinutesTotal_Type())
memoryThirtyMinutesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesTotal.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesTotal.setUnits(_D)
_MemoryThirtyMinutesUsed_Type=Unsigned32
_MemoryThirtyMinutesUsed_Object=MibTableColumn
memoryThirtyMinutesUsed=_MemoryThirtyMinutesUsed_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,19),_MemoryThirtyMinutesUsed_Type())
memoryThirtyMinutesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesUsed.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesUsed.setUnits(_D)
_MemoryThirtyMinutesFree_Type=Unsigned32
_MemoryThirtyMinutesFree_Object=MibTableColumn
memoryThirtyMinutesFree=_MemoryThirtyMinutesFree_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,20),_MemoryThirtyMinutesFree_Type())
memoryThirtyMinutesFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesFree.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesFree.setUnits(_D)
_MemoryThirtyMinutesBuffered_Type=Unsigned32
_MemoryThirtyMinutesBuffered_Object=MibTableColumn
memoryThirtyMinutesBuffered=_MemoryThirtyMinutesBuffered_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,21),_MemoryThirtyMinutesBuffered_Type())
memoryThirtyMinutesBuffered.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesBuffered.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesBuffered.setUnits(_D)
_MemoryThirtyMinutesCached_Type=Unsigned32
_MemoryThirtyMinutesCached_Object=MibTableColumn
memoryThirtyMinutesCached=_MemoryThirtyMinutesCached_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,22),_MemoryThirtyMinutesCached_Type())
memoryThirtyMinutesCached.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesCached.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesCached.setUnits(_D)
_MemoryThirtyMinutesAvailable_Type=Unsigned32
_MemoryThirtyMinutesAvailable_Object=MibTableColumn
memoryThirtyMinutesAvailable=_MemoryThirtyMinutesAvailable_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,23),_MemoryThirtyMinutesAvailable_Type())
memoryThirtyMinutesAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesAvailable.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesAvailable.setUnits(_D)
_MemoryThirtyMinutesSlabRecl_Type=Unsigned32
_MemoryThirtyMinutesSlabRecl_Object=MibTableColumn
memoryThirtyMinutesSlabRecl=_MemoryThirtyMinutesSlabRecl_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,24),_MemoryThirtyMinutesSlabRecl_Type())
memoryThirtyMinutesSlabRecl.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesSlabRecl.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesSlabRecl.setUnits(_D)
_MemoryThirtyMinutesSlabUnrecl_Type=Unsigned32
_MemoryThirtyMinutesSlabUnrecl_Object=MibTableColumn
memoryThirtyMinutesSlabUnrecl=_MemoryThirtyMinutesSlabUnrecl_Object((1,3,6,1,4,1,3709,3,6,4,2,2,1,25),_MemoryThirtyMinutesSlabUnrecl_Type())
memoryThirtyMinutesSlabUnrecl.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryThirtyMinutesSlabUnrecl.setStatus(_A)
if mibBuilder.loadTexts:memoryThirtyMinutesSlabUnrecl.setUnits(_D)
mibBuilder.exportSymbols(_E,**{'dmosSysmonMIB':dmosSysmonMIB,'cpu':cpu,'cpuChassisTable':cpuChassisTable,'cpuChassisEntry':cpuChassisEntry,_F:cpuChassisId,'cpuSlotTable':cpuSlotTable,'cpuSlotEntry':cpuSlotEntry,_G:cpuSlotId,'cpuLoadFiveSecondsActive':cpuLoadFiveSecondsActive,'cpuLoadFiveSecondsIdle':cpuLoadFiveSecondsIdle,'cpuLoadOneMinuteActive':cpuLoadOneMinuteActive,'cpuLoadOneMinuteIdle':cpuLoadOneMinuteIdle,'cpuLoadFiveMinutesActive':cpuLoadFiveMinutesActive,'cpuLoadFiveMinutesIdle':cpuLoadFiveMinutesIdle,'cpuCoreTable':cpuCoreTable,'cpuCoreEntry':cpuCoreEntry,_J:cpuCoreCoreId,'cpuCoreFiveSecondsActive':cpuCoreFiveSecondsActive,'cpuCoreFiveSecondsUser':cpuCoreFiveSecondsUser,'cpuCoreFiveSecondsSystem':cpuCoreFiveSecondsSystem,'cpuCoreFiveSecondsNice':cpuCoreFiveSecondsNice,'cpuCoreFiveSecondsIdle':cpuCoreFiveSecondsIdle,'cpuCoreFiveSecondsWait':cpuCoreFiveSecondsWait,'cpuCoreFiveSecondsInterrupt':cpuCoreFiveSecondsInterrupt,'cpuCoreFiveSecondsSoftirq':cpuCoreFiveSecondsSoftirq,'cpuCoreOneMinuteActive':cpuCoreOneMinuteActive,'cpuCoreOneMinuteUser':cpuCoreOneMinuteUser,'cpuCoreOneMinuteSystem':cpuCoreOneMinuteSystem,'cpuCoreOneMinuteNice':cpuCoreOneMinuteNice,'cpuCoreOneMinuteIdle':cpuCoreOneMinuteIdle,'cpuCoreOneMinuteWait':cpuCoreOneMinuteWait,'cpuCoreOneMinuteInterrupt':cpuCoreOneMinuteInterrupt,'cpuCoreOneMinuteSoftirq':cpuCoreOneMinuteSoftirq,'cpuCoreFiveMinutesActive':cpuCoreFiveMinutesActive,'cpuCoreFiveMinutesUser':cpuCoreFiveMinutesUser,'cpuCoreFiveMinutesSystem':cpuCoreFiveMinutesSystem,'cpuCoreFiveMinutesNice':cpuCoreFiveMinutesNice,'cpuCoreFiveMinutesIdle':cpuCoreFiveMinutesIdle,'cpuCoreFiveMinutesWait':cpuCoreFiveMinutesWait,'cpuCoreFiveMinutesInterrupt':cpuCoreFiveMinutesInterrupt,'cpuCoreFiveMinutesSoftirq':cpuCoreFiveMinutesSoftirq,'memory':memory,'memoryChassisTable':memoryChassisTable,'memoryChassisEntry':memoryChassisEntry,_I:memoryChassisId,'memorySlotTable':memorySlotTable,'memorySlotEntry':memorySlotEntry,_K:memorySlotId,'memoryFiveSecondsTotal':memoryFiveSecondsTotal,'memoryFiveSecondsUsed':memoryFiveSecondsUsed,'memoryFiveSecondsFree':memoryFiveSecondsFree,'memoryFiveSecondsBuffered':memoryFiveSecondsBuffered,'memoryFiveSecondsCached':memoryFiveSecondsCached,'memoryFiveSecondsAvailable':memoryFiveSecondsAvailable,'memoryFiveSecondsSlabRecl':memoryFiveSecondsSlabRecl,'memoryFiveSecondsSlabUnrecl':memoryFiveSecondsSlabUnrecl,'memoryFiveMinutesTotal':memoryFiveMinutesTotal,'memoryFiveMinutesUsed':memoryFiveMinutesUsed,'memoryFiveMinutesFree':memoryFiveMinutesFree,'memoryFiveMinutesBuffered':memoryFiveMinutesBuffered,'memoryFiveMinutesCached':memoryFiveMinutesCached,'memoryFiveMinutesAvailable':memoryFiveMinutesAvailable,'memoryFiveMinutesSlabRecl':memoryFiveMinutesSlabRecl,'memoryFiveMinutesSlabUnrecl':memoryFiveMinutesSlabUnrecl,'memoryThirtyMinutesTotal':memoryThirtyMinutesTotal,'memoryThirtyMinutesUsed':memoryThirtyMinutesUsed,'memoryThirtyMinutesFree':memoryThirtyMinutesFree,'memoryThirtyMinutesBuffered':memoryThirtyMinutesBuffered,'memoryThirtyMinutesCached':memoryThirtyMinutesCached,'memoryThirtyMinutesAvailable':memoryThirtyMinutesAvailable,'memoryThirtyMinutesSlabRecl':memoryThirtyMinutesSlabRecl,'memoryThirtyMinutesSlabUnrecl':memoryThirtyMinutesSlabUnrecl})