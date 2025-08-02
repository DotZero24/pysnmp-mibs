_J='genMemUtilizationID'
_I='genCpuUtilizationHistorySampleIndex'
_H='enabled'
_G='disabled'
_F='genCpuIndex'
_E='read-write'
_D='UTILIZATION-MANAGEMENT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
avayaSystemStats,=mibBuilder.importSymbols('AVAYAGEN-MIB','avayaSystemStats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
genStats=ModuleIdentity((1,3,6,1,4,1,6889,2,1,11,1))
if mibBuilder.loadTexts:genStats.setRevisions(('2003-05-18 16:16',))
class MBytes(TextualConvention,Integer32):status=_A
_GenCpuUtilization_ObjectIdentity=ObjectIdentity
genCpuUtilization=_GenCpuUtilization_ObjectIdentity((1,3,6,1,4,1,6889,2,1,11,1,1))
_GenCpuUtilizationTable_Object=MibTable
genCpuUtilizationTable=_GenCpuUtilizationTable_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1))
if mibBuilder.loadTexts:genCpuUtilizationTable.setStatus(_A)
_GenCpuUtilizationEntry_Object=MibTableRow
genCpuUtilizationEntry=_GenCpuUtilizationEntry_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1,1))
genCpuUtilizationEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:genCpuUtilizationEntry.setStatus(_A)
_GenCpuIndex_Type=Integer32
_GenCpuIndex_Object=MibTableColumn
genCpuIndex=_GenCpuIndex_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1,1,1),_GenCpuIndex_Type())
genCpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:genCpuIndex.setStatus(_A)
class _GenCpuUtilizationEnableMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_GenCpuUtilizationEnableMonitoring_Type.__name__=_C
_GenCpuUtilizationEnableMonitoring_Object=MibTableColumn
genCpuUtilizationEnableMonitoring=_GenCpuUtilizationEnableMonitoring_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1,1,2),_GenCpuUtilizationEnableMonitoring_Type())
genCpuUtilizationEnableMonitoring.setMaxAccess(_E)
if mibBuilder.loadTexts:genCpuUtilizationEnableMonitoring.setStatus(_A)
class _GenCpuUtilizationEnableEventGeneration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_GenCpuUtilizationEnableEventGeneration_Type.__name__=_C
_GenCpuUtilizationEnableEventGeneration_Object=MibTableColumn
genCpuUtilizationEnableEventGeneration=_GenCpuUtilizationEnableEventGeneration_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1,1,3),_GenCpuUtilizationEnableEventGeneration_Type())
genCpuUtilizationEnableEventGeneration.setMaxAccess(_E)
if mibBuilder.loadTexts:genCpuUtilizationEnableEventGeneration.setStatus(_A)
class _GenCpuUtilizationHighThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,99))
_GenCpuUtilizationHighThreshold_Type.__name__=_C
_GenCpuUtilizationHighThreshold_Object=MibTableColumn
genCpuUtilizationHighThreshold=_GenCpuUtilizationHighThreshold_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1,1,4),_GenCpuUtilizationHighThreshold_Type())
genCpuUtilizationHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:genCpuUtilizationHighThreshold.setStatus(_A)
class _GenCpuAverageUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GenCpuAverageUtilization_Type.__name__=_C
_GenCpuAverageUtilization_Object=MibTableColumn
genCpuAverageUtilization=_GenCpuAverageUtilization_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1,1,5),_GenCpuAverageUtilization_Type())
genCpuAverageUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:genCpuAverageUtilization.setStatus(_A)
class _GenCpuCurrentUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GenCpuCurrentUtilization_Type.__name__=_C
_GenCpuCurrentUtilization_Object=MibTableColumn
genCpuCurrentUtilization=_GenCpuCurrentUtilization_Object((1,3,6,1,4,1,6889,2,1,11,1,1,1,1,6),_GenCpuCurrentUtilization_Type())
genCpuCurrentUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:genCpuCurrentUtilization.setStatus('obsolete')
_GenCpuUtilizationHistoryTable_Object=MibTable
genCpuUtilizationHistoryTable=_GenCpuUtilizationHistoryTable_Object((1,3,6,1,4,1,6889,2,1,11,1,1,2))
if mibBuilder.loadTexts:genCpuUtilizationHistoryTable.setStatus(_A)
_GenCpuUtilizationHistoryEntry_Object=MibTableRow
genCpuUtilizationHistoryEntry=_GenCpuUtilizationHistoryEntry_Object((1,3,6,1,4,1,6889,2,1,11,1,1,2,1))
genCpuUtilizationHistoryEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:genCpuUtilizationHistoryEntry.setStatus(_A)
_GenCpuUtilizationHistorySampleIndex_Type=Integer32
_GenCpuUtilizationHistorySampleIndex_Object=MibTableColumn
genCpuUtilizationHistorySampleIndex=_GenCpuUtilizationHistorySampleIndex_Object((1,3,6,1,4,1,6889,2,1,11,1,1,2,1,1),_GenCpuUtilizationHistorySampleIndex_Type())
genCpuUtilizationHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:genCpuUtilizationHistorySampleIndex.setStatus(_A)
_GenCpuHistoryUtilization_Type=Integer32
_GenCpuHistoryUtilization_Object=MibTableColumn
genCpuHistoryUtilization=_GenCpuHistoryUtilization_Object((1,3,6,1,4,1,6889,2,1,11,1,1,2,1,2),_GenCpuHistoryUtilization_Type())
genCpuHistoryUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:genCpuHistoryUtilization.setStatus(_A)
_GenMemUtilization_ObjectIdentity=ObjectIdentity
genMemUtilization=_GenMemUtilization_ObjectIdentity((1,3,6,1,4,1,6889,2,1,11,1,2))
_GenMemUtilizationTotalRAM_Type=MBytes
_GenMemUtilizationTotalRAM_Object=MibScalar
genMemUtilizationTotalRAM=_GenMemUtilizationTotalRAM_Object((1,3,6,1,4,1,6889,2,1,11,1,2,1),_GenMemUtilizationTotalRAM_Type())
genMemUtilizationTotalRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationTotalRAM.setStatus(_A)
_GenMemUtilizationOperationalImage_Type=MBytes
_GenMemUtilizationOperationalImage_Object=MibScalar
genMemUtilizationOperationalImage=_GenMemUtilizationOperationalImage_Object((1,3,6,1,4,1,6889,2,1,11,1,2,2),_GenMemUtilizationOperationalImage_Type())
genMemUtilizationOperationalImage.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationOperationalImage.setStatus(_A)
_GenMemUtilizationDynAllocMem_ObjectIdentity=ObjectIdentity
genMemUtilizationDynAllocMem=_GenMemUtilizationDynAllocMem_ObjectIdentity((1,3,6,1,4,1,6889,2,1,11,1,2,3))
_GenMemUtilizationDynAllocMemUsed_Type=MBytes
_GenMemUtilizationDynAllocMemUsed_Object=MibScalar
genMemUtilizationDynAllocMemUsed=_GenMemUtilizationDynAllocMemUsed_Object((1,3,6,1,4,1,6889,2,1,11,1,2,3,1),_GenMemUtilizationDynAllocMemUsed_Type())
genMemUtilizationDynAllocMemUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationDynAllocMemUsed.setStatus(_A)
_GenMemUtilizationDynAllocMemMaxUsed_Type=MBytes
_GenMemUtilizationDynAllocMemMaxUsed_Object=MibScalar
genMemUtilizationDynAllocMemMaxUsed=_GenMemUtilizationDynAllocMemMaxUsed_Object((1,3,6,1,4,1,6889,2,1,11,1,2,3,2),_GenMemUtilizationDynAllocMemMaxUsed_Type())
genMemUtilizationDynAllocMemMaxUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationDynAllocMemMaxUsed.setStatus(_A)
_GenMemUtilizationDynAllocMemAvailable_Type=MBytes
_GenMemUtilizationDynAllocMemAvailable_Object=MibScalar
genMemUtilizationDynAllocMemAvailable=_GenMemUtilizationDynAllocMemAvailable_Object((1,3,6,1,4,1,6889,2,1,11,1,2,3,3),_GenMemUtilizationDynAllocMemAvailable_Type())
genMemUtilizationDynAllocMemAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationDynAllocMemAvailable.setStatus(_A)
_GenMemUtilizationAllocationFailures_Type=MBytes
_GenMemUtilizationAllocationFailures_Object=MibScalar
genMemUtilizationAllocationFailures=_GenMemUtilizationAllocationFailures_Object((1,3,6,1,4,1,6889,2,1,11,1,2,4),_GenMemUtilizationAllocationFailures_Type())
genMemUtilizationAllocationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationAllocationFailures.setStatus(_A)
_GenMemUtilizationSysRAMTrap_ObjectIdentity=ObjectIdentity
genMemUtilizationSysRAMTrap=_GenMemUtilizationSysRAMTrap_ObjectIdentity((1,3,6,1,4,1,6889,2,1,11,1,2,5))
_GenMemUtilizationSysRAMNotificationHighWaterMark_Type=MBytes
_GenMemUtilizationSysRAMNotificationHighWaterMark_Object=MibScalar
genMemUtilizationSysRAMNotificationHighWaterMark=_GenMemUtilizationSysRAMNotificationHighWaterMark_Object((1,3,6,1,4,1,6889,2,1,11,1,2,5,1),_GenMemUtilizationSysRAMNotificationHighWaterMark_Type())
genMemUtilizationSysRAMNotificationHighWaterMark.setMaxAccess(_E)
if mibBuilder.loadTexts:genMemUtilizationSysRAMNotificationHighWaterMark.setStatus(_A)
_GenMemUtilizationTable_Object=MibTable
genMemUtilizationTable=_GenMemUtilizationTable_Object((1,3,6,1,4,1,6889,2,1,11,1,2,6))
if mibBuilder.loadTexts:genMemUtilizationTable.setStatus(_A)
_GenMemUtilizationEntry_Object=MibTableRow
genMemUtilizationEntry=_GenMemUtilizationEntry_Object((1,3,6,1,4,1,6889,2,1,11,1,2,6,1))
genMemUtilizationEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:genMemUtilizationEntry.setStatus(_A)
class _GenMemUtilizationID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_GenMemUtilizationID_Type.__name__=_C
_GenMemUtilizationID_Object=MibTableColumn
genMemUtilizationID=_GenMemUtilizationID_Object((1,3,6,1,4,1,6889,2,1,11,1,2,6,1,1),_GenMemUtilizationID_Type())
genMemUtilizationID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:genMemUtilizationID.setStatus(_A)
_GenMemUtilizationPhyRam_Type=MBytes
_GenMemUtilizationPhyRam_Object=MibTableColumn
genMemUtilizationPhyRam=_GenMemUtilizationPhyRam_Object((1,3,6,1,4,1,6889,2,1,11,1,2,6,1,2),_GenMemUtilizationPhyRam_Type())
genMemUtilizationPhyRam.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationPhyRam.setStatus(_A)
class _GenMemUtilizationPercentUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GenMemUtilizationPercentUsed_Type.__name__=_C
_GenMemUtilizationPercentUsed_Object=MibTableColumn
genMemUtilizationPercentUsed=_GenMemUtilizationPercentUsed_Object((1,3,6,1,4,1,6889,2,1,11,1,2,6,1,3),_GenMemUtilizationPercentUsed_Type())
genMemUtilizationPercentUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:genMemUtilizationPercentUsed.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MBytes':MBytes,'genStats':genStats,'genCpuUtilization':genCpuUtilization,'genCpuUtilizationTable':genCpuUtilizationTable,'genCpuUtilizationEntry':genCpuUtilizationEntry,_F:genCpuIndex,'genCpuUtilizationEnableMonitoring':genCpuUtilizationEnableMonitoring,'genCpuUtilizationEnableEventGeneration':genCpuUtilizationEnableEventGeneration,'genCpuUtilizationHighThreshold':genCpuUtilizationHighThreshold,'genCpuAverageUtilization':genCpuAverageUtilization,'genCpuCurrentUtilization':genCpuCurrentUtilization,'genCpuUtilizationHistoryTable':genCpuUtilizationHistoryTable,'genCpuUtilizationHistoryEntry':genCpuUtilizationHistoryEntry,_I:genCpuUtilizationHistorySampleIndex,'genCpuHistoryUtilization':genCpuHistoryUtilization,'genMemUtilization':genMemUtilization,'genMemUtilizationTotalRAM':genMemUtilizationTotalRAM,'genMemUtilizationOperationalImage':genMemUtilizationOperationalImage,'genMemUtilizationDynAllocMem':genMemUtilizationDynAllocMem,'genMemUtilizationDynAllocMemUsed':genMemUtilizationDynAllocMemUsed,'genMemUtilizationDynAllocMemMaxUsed':genMemUtilizationDynAllocMemMaxUsed,'genMemUtilizationDynAllocMemAvailable':genMemUtilizationDynAllocMemAvailable,'genMemUtilizationAllocationFailures':genMemUtilizationAllocationFailures,'genMemUtilizationSysRAMTrap':genMemUtilizationSysRAMTrap,'genMemUtilizationSysRAMNotificationHighWaterMark':genMemUtilizationSysRAMNotificationHighWaterMark,'genMemUtilizationTable':genMemUtilizationTable,'genMemUtilizationEntry':genMemUtilizationEntry,_J:genMemUtilizationID,'genMemUtilizationPhyRam':genMemUtilizationPhyRam,'genMemUtilizationPercentUsed':genMemUtilizationPercentUsed})