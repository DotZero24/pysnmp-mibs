_F='ntwsSysPowerSupplyDeviceOID'
_E='NTWS-SYSTEM-MIB'
_D='obsolete'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
ntwsSystemMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,8))
if mibBuilder.loadTexts:ntwsSystemMib.setRevisions(('2007-08-31 00:13','2007-08-14 00:12','2007-05-04 00:10','2007-03-14 00:07','2006-11-09 00:04','2006-06-06 00:03'))
class NtwsSysCpuLoad(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class NtwsSysMemoryAmount(TextualConvention,Unsigned32):status=_A
class NtwsSysPowerSupplyStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('unknown',2),('ac-failed',3),('dc-failed',4),('ac-ok-dc-ok',5)))
_NtwsSysObjects_ObjectIdentity=ObjectIdentity
ntwsSysObjects=_NtwsSysObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,8,1))
_NtwsSysDataObjects_ObjectIdentity=ObjectIdentity
ntwsSysDataObjects=_NtwsSysDataObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,8,1,1))
_NtwsSysCpuMemoryUsedBytes_Type=Unsigned32
_NtwsSysCpuMemoryUsedBytes_Object=MibScalar
ntwsSysCpuMemoryUsedBytes=_NtwsSysCpuMemoryUsedBytes_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,1),_NtwsSysCpuMemoryUsedBytes_Type())
ntwsSysCpuMemoryUsedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryUsedBytes.setStatus(_D)
_NtwsSysCpuMemoryTotalBytes_Type=Unsigned32
_NtwsSysCpuMemoryTotalBytes_Object=MibScalar
ntwsSysCpuMemoryTotalBytes=_NtwsSysCpuMemoryTotalBytes_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,2),_NtwsSysCpuMemoryTotalBytes_Type())
ntwsSysCpuMemoryTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryTotalBytes.setStatus(_D)
_NtwsSysFlashMemoryUsedBytes_Type=Unsigned32
_NtwsSysFlashMemoryUsedBytes_Object=MibScalar
ntwsSysFlashMemoryUsedBytes=_NtwsSysFlashMemoryUsedBytes_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,3),_NtwsSysFlashMemoryUsedBytes_Type())
ntwsSysFlashMemoryUsedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysFlashMemoryUsedBytes.setStatus(_A)
_NtwsSysFlashMemoryTotalBytes_Type=Unsigned32
_NtwsSysFlashMemoryTotalBytes_Object=MibScalar
ntwsSysFlashMemoryTotalBytes=_NtwsSysFlashMemoryTotalBytes_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,4),_NtwsSysFlashMemoryTotalBytes_Type())
ntwsSysFlashMemoryTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysFlashMemoryTotalBytes.setStatus(_A)
_NtwsSysCpuAverageLoad_Type=NtwsSysCpuLoad
_NtwsSysCpuAverageLoad_Object=MibScalar
ntwsSysCpuAverageLoad=_NtwsSysCpuAverageLoad_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,5),_NtwsSysCpuAverageLoad_Type())
ntwsSysCpuAverageLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuAverageLoad.setStatus(_A)
_NtwsSysCpuMemorySize_Type=NtwsSysMemoryAmount
_NtwsSysCpuMemorySize_Object=MibScalar
ntwsSysCpuMemorySize=_NtwsSysCpuMemorySize_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,6),_NtwsSysCpuMemorySize_Type())
ntwsSysCpuMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemorySize.setStatus(_A)
_NtwsSysCpuLoadDetail_ObjectIdentity=ObjectIdentity
ntwsSysCpuLoadDetail=_NtwsSysCpuLoadDetail_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,8,1,1,11))
_NtwsSysCpuInstantLoad_Type=NtwsSysCpuLoad
_NtwsSysCpuInstantLoad_Object=MibScalar
ntwsSysCpuInstantLoad=_NtwsSysCpuInstantLoad_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,11,1),_NtwsSysCpuInstantLoad_Type())
ntwsSysCpuInstantLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuInstantLoad.setStatus(_A)
_NtwsSysCpuLastMinuteLoad_Type=NtwsSysCpuLoad
_NtwsSysCpuLastMinuteLoad_Object=MibScalar
ntwsSysCpuLastMinuteLoad=_NtwsSysCpuLastMinuteLoad_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,11,2),_NtwsSysCpuLastMinuteLoad_Type())
ntwsSysCpuLastMinuteLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuLastMinuteLoad.setStatus(_A)
_NtwsSysCpuLast5MinutesLoad_Type=NtwsSysCpuLoad
_NtwsSysCpuLast5MinutesLoad_Object=MibScalar
ntwsSysCpuLast5MinutesLoad=_NtwsSysCpuLast5MinutesLoad_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,11,3),_NtwsSysCpuLast5MinutesLoad_Type())
ntwsSysCpuLast5MinutesLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuLast5MinutesLoad.setStatus(_A)
_NtwsSysCpuLastHourLoad_Type=NtwsSysCpuLoad
_NtwsSysCpuLastHourLoad_Object=MibScalar
ntwsSysCpuLastHourLoad=_NtwsSysCpuLastHourLoad_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,11,4),_NtwsSysCpuLastHourLoad_Type())
ntwsSysCpuLastHourLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuLastHourLoad.setStatus(_A)
_NtwsSysCpuLastDayLoad_Type=NtwsSysCpuLoad
_NtwsSysCpuLastDayLoad_Object=MibScalar
ntwsSysCpuLastDayLoad=_NtwsSysCpuLastDayLoad_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,11,5),_NtwsSysCpuLastDayLoad_Type())
ntwsSysCpuLastDayLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuLastDayLoad.setStatus(_A)
_NtwsSysCpuLast3DaysLoad_Type=NtwsSysCpuLoad
_NtwsSysCpuLast3DaysLoad_Object=MibScalar
ntwsSysCpuLast3DaysLoad=_NtwsSysCpuLast3DaysLoad_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,11,6),_NtwsSysCpuLast3DaysLoad_Type())
ntwsSysCpuLast3DaysLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuLast3DaysLoad.setStatus(_A)
_NtwsSysCpuMemoryUsageDetail_ObjectIdentity=ObjectIdentity
ntwsSysCpuMemoryUsageDetail=_NtwsSysCpuMemoryUsageDetail_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,8,1,1,12))
_NtwsSysCpuMemoryInstantUsage_Type=NtwsSysMemoryAmount
_NtwsSysCpuMemoryInstantUsage_Object=MibScalar
ntwsSysCpuMemoryInstantUsage=_NtwsSysCpuMemoryInstantUsage_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,12,1),_NtwsSysCpuMemoryInstantUsage_Type())
ntwsSysCpuMemoryInstantUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryInstantUsage.setStatus(_A)
_NtwsSysCpuMemoryLastMinuteUsage_Type=NtwsSysMemoryAmount
_NtwsSysCpuMemoryLastMinuteUsage_Object=MibScalar
ntwsSysCpuMemoryLastMinuteUsage=_NtwsSysCpuMemoryLastMinuteUsage_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,12,2),_NtwsSysCpuMemoryLastMinuteUsage_Type())
ntwsSysCpuMemoryLastMinuteUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryLastMinuteUsage.setStatus(_A)
_NtwsSysCpuMemoryLast5MinutesUsage_Type=NtwsSysMemoryAmount
_NtwsSysCpuMemoryLast5MinutesUsage_Object=MibScalar
ntwsSysCpuMemoryLast5MinutesUsage=_NtwsSysCpuMemoryLast5MinutesUsage_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,12,3),_NtwsSysCpuMemoryLast5MinutesUsage_Type())
ntwsSysCpuMemoryLast5MinutesUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryLast5MinutesUsage.setStatus(_A)
_NtwsSysCpuMemoryLastHourUsage_Type=NtwsSysMemoryAmount
_NtwsSysCpuMemoryLastHourUsage_Object=MibScalar
ntwsSysCpuMemoryLastHourUsage=_NtwsSysCpuMemoryLastHourUsage_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,12,4),_NtwsSysCpuMemoryLastHourUsage_Type())
ntwsSysCpuMemoryLastHourUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryLastHourUsage.setStatus(_A)
_NtwsSysCpuMemoryLastDayUsage_Type=NtwsSysMemoryAmount
_NtwsSysCpuMemoryLastDayUsage_Object=MibScalar
ntwsSysCpuMemoryLastDayUsage=_NtwsSysCpuMemoryLastDayUsage_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,12,5),_NtwsSysCpuMemoryLastDayUsage_Type())
ntwsSysCpuMemoryLastDayUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryLastDayUsage.setStatus(_A)
_NtwsSysCpuMemoryLast3DaysUsage_Type=NtwsSysMemoryAmount
_NtwsSysCpuMemoryLast3DaysUsage_Object=MibScalar
ntwsSysCpuMemoryLast3DaysUsage=_NtwsSysCpuMemoryLast3DaysUsage_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,12,6),_NtwsSysCpuMemoryLast3DaysUsage_Type())
ntwsSysCpuMemoryLast3DaysUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysCpuMemoryLast3DaysUsage.setStatus(_A)
_NtwsSysChassisComponents_ObjectIdentity=ObjectIdentity
ntwsSysChassisComponents=_NtwsSysChassisComponents_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,8,1,1,13))
_NtwsSysChasCompPowerSupplies_ObjectIdentity=ObjectIdentity
ntwsSysChasCompPowerSupplies=_NtwsSysChasCompPowerSupplies_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,8,1,1,13,1))
_NtwsSysNumPowerSuppliesSupported_Type=Unsigned32
_NtwsSysNumPowerSuppliesSupported_Object=MibScalar
ntwsSysNumPowerSuppliesSupported=_NtwsSysNumPowerSuppliesSupported_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,13,1,1),_NtwsSysNumPowerSuppliesSupported_Type())
ntwsSysNumPowerSuppliesSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysNumPowerSuppliesSupported.setStatus(_A)
_NtwsSysPowerSupplyTable_Object=MibTable
ntwsSysPowerSupplyTable=_NtwsSysPowerSupplyTable_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,13,1,2))
if mibBuilder.loadTexts:ntwsSysPowerSupplyTable.setStatus(_A)
_NtwsSysPowerSupplyEntry_Object=MibTableRow
ntwsSysPowerSupplyEntry=_NtwsSysPowerSupplyEntry_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,13,1,2,1))
ntwsSysPowerSupplyEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ntwsSysPowerSupplyEntry.setStatus(_A)
_NtwsSysPowerSupplyDeviceOID_Type=ObjectIdentifier
_NtwsSysPowerSupplyDeviceOID_Object=MibTableColumn
ntwsSysPowerSupplyDeviceOID=_NtwsSysPowerSupplyDeviceOID_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,13,1,2,1,1),_NtwsSysPowerSupplyDeviceOID_Type())
ntwsSysPowerSupplyDeviceOID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntwsSysPowerSupplyDeviceOID.setStatus(_A)
_NtwsSysPowerSupplyStatus_Type=NtwsSysPowerSupplyStatus
_NtwsSysPowerSupplyStatus_Object=MibTableColumn
ntwsSysPowerSupplyStatus=_NtwsSysPowerSupplyStatus_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,13,1,2,1,2),_NtwsSysPowerSupplyStatus_Type())
ntwsSysPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysPowerSupplyStatus.setStatus(_A)
class _NtwsSysPowerSupplyDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsSysPowerSupplyDescr_Type.__name__=_C
_NtwsSysPowerSupplyDescr_Object=MibTableColumn
ntwsSysPowerSupplyDescr=_NtwsSysPowerSupplyDescr_Object((1,3,6,1,4,1,45,6,1,4,8,1,1,13,1,2,1,3),_NtwsSysPowerSupplyDescr_Type())
ntwsSysPowerSupplyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSysPowerSupplyDescr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'NtwsSysCpuLoad':NtwsSysCpuLoad,'NtwsSysMemoryAmount':NtwsSysMemoryAmount,'NtwsSysPowerSupplyStatus':NtwsSysPowerSupplyStatus,'ntwsSystemMib':ntwsSystemMib,'ntwsSysObjects':ntwsSysObjects,'ntwsSysDataObjects':ntwsSysDataObjects,'ntwsSysCpuMemoryUsedBytes':ntwsSysCpuMemoryUsedBytes,'ntwsSysCpuMemoryTotalBytes':ntwsSysCpuMemoryTotalBytes,'ntwsSysFlashMemoryUsedBytes':ntwsSysFlashMemoryUsedBytes,'ntwsSysFlashMemoryTotalBytes':ntwsSysFlashMemoryTotalBytes,'ntwsSysCpuAverageLoad':ntwsSysCpuAverageLoad,'ntwsSysCpuMemorySize':ntwsSysCpuMemorySize,'ntwsSysCpuLoadDetail':ntwsSysCpuLoadDetail,'ntwsSysCpuInstantLoad':ntwsSysCpuInstantLoad,'ntwsSysCpuLastMinuteLoad':ntwsSysCpuLastMinuteLoad,'ntwsSysCpuLast5MinutesLoad':ntwsSysCpuLast5MinutesLoad,'ntwsSysCpuLastHourLoad':ntwsSysCpuLastHourLoad,'ntwsSysCpuLastDayLoad':ntwsSysCpuLastDayLoad,'ntwsSysCpuLast3DaysLoad':ntwsSysCpuLast3DaysLoad,'ntwsSysCpuMemoryUsageDetail':ntwsSysCpuMemoryUsageDetail,'ntwsSysCpuMemoryInstantUsage':ntwsSysCpuMemoryInstantUsage,'ntwsSysCpuMemoryLastMinuteUsage':ntwsSysCpuMemoryLastMinuteUsage,'ntwsSysCpuMemoryLast5MinutesUsage':ntwsSysCpuMemoryLast5MinutesUsage,'ntwsSysCpuMemoryLastHourUsage':ntwsSysCpuMemoryLastHourUsage,'ntwsSysCpuMemoryLastDayUsage':ntwsSysCpuMemoryLastDayUsage,'ntwsSysCpuMemoryLast3DaysUsage':ntwsSysCpuMemoryLast3DaysUsage,'ntwsSysChassisComponents':ntwsSysChassisComponents,'ntwsSysChasCompPowerSupplies':ntwsSysChasCompPowerSupplies,'ntwsSysNumPowerSuppliesSupported':ntwsSysNumPowerSuppliesSupported,'ntwsSysPowerSupplyTable':ntwsSysPowerSupplyTable,'ntwsSysPowerSupplyEntry':ntwsSysPowerSupplyEntry,_F:ntwsSysPowerSupplyDeviceOID,'ntwsSysPowerSupplyStatus':ntwsSysPowerSupplyStatus,'ntwsSysPowerSupplyDescr':ntwsSysPowerSupplyDescr})