_F='trpzSysPowerSupplyDeviceOID'
_E='TRAPEZE-NETWORKS-SYSTEM-MIB'
_D='obsolete'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzSystemMib=ModuleIdentity((1,3,6,1,4,1,14525,4,8))
if mibBuilder.loadTexts:trpzSystemMib.setRevisions(('2007-08-14 00:12','2007-05-04 00:10','2007-03-14 00:07','2006-11-09 00:04','2006-06-06 00:03'))
class TrpzSysCpuLoad(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class TrpzSysMemoryAmount(TextualConvention,Unsigned32):status=_A
class TrpzSysPowerSupplyStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('unknown',2),('ac-failed',3),('dc-failed',4),('ac-ok-dc-ok',5)))
_TrpzSysObjects_ObjectIdentity=ObjectIdentity
trpzSysObjects=_TrpzSysObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,8,1))
_TrpzSysDataObjects_ObjectIdentity=ObjectIdentity
trpzSysDataObjects=_TrpzSysDataObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,8,1,1))
_TrpzSysCpuMemoryUsedBytes_Type=Unsigned32
_TrpzSysCpuMemoryUsedBytes_Object=MibScalar
trpzSysCpuMemoryUsedBytes=_TrpzSysCpuMemoryUsedBytes_Object((1,3,6,1,4,1,14525,4,8,1,1,1),_TrpzSysCpuMemoryUsedBytes_Type())
trpzSysCpuMemoryUsedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryUsedBytes.setStatus(_D)
_TrpzSysCpuMemoryTotalBytes_Type=Unsigned32
_TrpzSysCpuMemoryTotalBytes_Object=MibScalar
trpzSysCpuMemoryTotalBytes=_TrpzSysCpuMemoryTotalBytes_Object((1,3,6,1,4,1,14525,4,8,1,1,2),_TrpzSysCpuMemoryTotalBytes_Type())
trpzSysCpuMemoryTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryTotalBytes.setStatus(_D)
_TrpzSysFlashMemoryUsedBytes_Type=Unsigned32
_TrpzSysFlashMemoryUsedBytes_Object=MibScalar
trpzSysFlashMemoryUsedBytes=_TrpzSysFlashMemoryUsedBytes_Object((1,3,6,1,4,1,14525,4,8,1,1,3),_TrpzSysFlashMemoryUsedBytes_Type())
trpzSysFlashMemoryUsedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysFlashMemoryUsedBytes.setStatus(_A)
_TrpzSysFlashMemoryTotalBytes_Type=Unsigned32
_TrpzSysFlashMemoryTotalBytes_Object=MibScalar
trpzSysFlashMemoryTotalBytes=_TrpzSysFlashMemoryTotalBytes_Object((1,3,6,1,4,1,14525,4,8,1,1,4),_TrpzSysFlashMemoryTotalBytes_Type())
trpzSysFlashMemoryTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysFlashMemoryTotalBytes.setStatus(_A)
_TrpzSysCpuAverageLoad_Type=TrpzSysCpuLoad
_TrpzSysCpuAverageLoad_Object=MibScalar
trpzSysCpuAverageLoad=_TrpzSysCpuAverageLoad_Object((1,3,6,1,4,1,14525,4,8,1,1,5),_TrpzSysCpuAverageLoad_Type())
trpzSysCpuAverageLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuAverageLoad.setStatus(_A)
_TrpzSysCpuMemorySize_Type=TrpzSysMemoryAmount
_TrpzSysCpuMemorySize_Object=MibScalar
trpzSysCpuMemorySize=_TrpzSysCpuMemorySize_Object((1,3,6,1,4,1,14525,4,8,1,1,6),_TrpzSysCpuMemorySize_Type())
trpzSysCpuMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemorySize.setStatus(_A)
_TrpzSysCpuLoadDetail_ObjectIdentity=ObjectIdentity
trpzSysCpuLoadDetail=_TrpzSysCpuLoadDetail_ObjectIdentity((1,3,6,1,4,1,14525,4,8,1,1,11))
_TrpzSysCpuInstantLoad_Type=TrpzSysCpuLoad
_TrpzSysCpuInstantLoad_Object=MibScalar
trpzSysCpuInstantLoad=_TrpzSysCpuInstantLoad_Object((1,3,6,1,4,1,14525,4,8,1,1,11,1),_TrpzSysCpuInstantLoad_Type())
trpzSysCpuInstantLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuInstantLoad.setStatus(_A)
_TrpzSysCpuLastMinuteLoad_Type=TrpzSysCpuLoad
_TrpzSysCpuLastMinuteLoad_Object=MibScalar
trpzSysCpuLastMinuteLoad=_TrpzSysCpuLastMinuteLoad_Object((1,3,6,1,4,1,14525,4,8,1,1,11,2),_TrpzSysCpuLastMinuteLoad_Type())
trpzSysCpuLastMinuteLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuLastMinuteLoad.setStatus(_A)
_TrpzSysCpuLast5MinutesLoad_Type=TrpzSysCpuLoad
_TrpzSysCpuLast5MinutesLoad_Object=MibScalar
trpzSysCpuLast5MinutesLoad=_TrpzSysCpuLast5MinutesLoad_Object((1,3,6,1,4,1,14525,4,8,1,1,11,3),_TrpzSysCpuLast5MinutesLoad_Type())
trpzSysCpuLast5MinutesLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuLast5MinutesLoad.setStatus(_A)
_TrpzSysCpuLastHourLoad_Type=TrpzSysCpuLoad
_TrpzSysCpuLastHourLoad_Object=MibScalar
trpzSysCpuLastHourLoad=_TrpzSysCpuLastHourLoad_Object((1,3,6,1,4,1,14525,4,8,1,1,11,4),_TrpzSysCpuLastHourLoad_Type())
trpzSysCpuLastHourLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuLastHourLoad.setStatus(_A)
_TrpzSysCpuLastDayLoad_Type=TrpzSysCpuLoad
_TrpzSysCpuLastDayLoad_Object=MibScalar
trpzSysCpuLastDayLoad=_TrpzSysCpuLastDayLoad_Object((1,3,6,1,4,1,14525,4,8,1,1,11,5),_TrpzSysCpuLastDayLoad_Type())
trpzSysCpuLastDayLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuLastDayLoad.setStatus(_A)
_TrpzSysCpuLast3DaysLoad_Type=TrpzSysCpuLoad
_TrpzSysCpuLast3DaysLoad_Object=MibScalar
trpzSysCpuLast3DaysLoad=_TrpzSysCpuLast3DaysLoad_Object((1,3,6,1,4,1,14525,4,8,1,1,11,6),_TrpzSysCpuLast3DaysLoad_Type())
trpzSysCpuLast3DaysLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuLast3DaysLoad.setStatus(_A)
_TrpzSysCpuMemoryUsageDetail_ObjectIdentity=ObjectIdentity
trpzSysCpuMemoryUsageDetail=_TrpzSysCpuMemoryUsageDetail_ObjectIdentity((1,3,6,1,4,1,14525,4,8,1,1,12))
_TrpzSysCpuMemoryInstantUsage_Type=TrpzSysMemoryAmount
_TrpzSysCpuMemoryInstantUsage_Object=MibScalar
trpzSysCpuMemoryInstantUsage=_TrpzSysCpuMemoryInstantUsage_Object((1,3,6,1,4,1,14525,4,8,1,1,12,1),_TrpzSysCpuMemoryInstantUsage_Type())
trpzSysCpuMemoryInstantUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryInstantUsage.setStatus(_A)
_TrpzSysCpuMemoryLastMinuteUsage_Type=TrpzSysMemoryAmount
_TrpzSysCpuMemoryLastMinuteUsage_Object=MibScalar
trpzSysCpuMemoryLastMinuteUsage=_TrpzSysCpuMemoryLastMinuteUsage_Object((1,3,6,1,4,1,14525,4,8,1,1,12,2),_TrpzSysCpuMemoryLastMinuteUsage_Type())
trpzSysCpuMemoryLastMinuteUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryLastMinuteUsage.setStatus(_A)
_TrpzSysCpuMemoryLast5MinutesUsage_Type=TrpzSysMemoryAmount
_TrpzSysCpuMemoryLast5MinutesUsage_Object=MibScalar
trpzSysCpuMemoryLast5MinutesUsage=_TrpzSysCpuMemoryLast5MinutesUsage_Object((1,3,6,1,4,1,14525,4,8,1,1,12,3),_TrpzSysCpuMemoryLast5MinutesUsage_Type())
trpzSysCpuMemoryLast5MinutesUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryLast5MinutesUsage.setStatus(_A)
_TrpzSysCpuMemoryLastHourUsage_Type=TrpzSysMemoryAmount
_TrpzSysCpuMemoryLastHourUsage_Object=MibScalar
trpzSysCpuMemoryLastHourUsage=_TrpzSysCpuMemoryLastHourUsage_Object((1,3,6,1,4,1,14525,4,8,1,1,12,4),_TrpzSysCpuMemoryLastHourUsage_Type())
trpzSysCpuMemoryLastHourUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryLastHourUsage.setStatus(_A)
_TrpzSysCpuMemoryLastDayUsage_Type=TrpzSysMemoryAmount
_TrpzSysCpuMemoryLastDayUsage_Object=MibScalar
trpzSysCpuMemoryLastDayUsage=_TrpzSysCpuMemoryLastDayUsage_Object((1,3,6,1,4,1,14525,4,8,1,1,12,5),_TrpzSysCpuMemoryLastDayUsage_Type())
trpzSysCpuMemoryLastDayUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryLastDayUsage.setStatus(_A)
_TrpzSysCpuMemoryLast3DaysUsage_Type=TrpzSysMemoryAmount
_TrpzSysCpuMemoryLast3DaysUsage_Object=MibScalar
trpzSysCpuMemoryLast3DaysUsage=_TrpzSysCpuMemoryLast3DaysUsage_Object((1,3,6,1,4,1,14525,4,8,1,1,12,6),_TrpzSysCpuMemoryLast3DaysUsage_Type())
trpzSysCpuMemoryLast3DaysUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysCpuMemoryLast3DaysUsage.setStatus(_A)
_TrpzSysChassisComponents_ObjectIdentity=ObjectIdentity
trpzSysChassisComponents=_TrpzSysChassisComponents_ObjectIdentity((1,3,6,1,4,1,14525,4,8,1,1,13))
_TrpzSysChasCompPowerSupplies_ObjectIdentity=ObjectIdentity
trpzSysChasCompPowerSupplies=_TrpzSysChasCompPowerSupplies_ObjectIdentity((1,3,6,1,4,1,14525,4,8,1,1,13,1))
_TrpzSysNumPowerSuppliesSupported_Type=Unsigned32
_TrpzSysNumPowerSuppliesSupported_Object=MibScalar
trpzSysNumPowerSuppliesSupported=_TrpzSysNumPowerSuppliesSupported_Object((1,3,6,1,4,1,14525,4,8,1,1,13,1,1),_TrpzSysNumPowerSuppliesSupported_Type())
trpzSysNumPowerSuppliesSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysNumPowerSuppliesSupported.setStatus(_A)
_TrpzSysPowerSupplyTable_Object=MibTable
trpzSysPowerSupplyTable=_TrpzSysPowerSupplyTable_Object((1,3,6,1,4,1,14525,4,8,1,1,13,1,2))
if mibBuilder.loadTexts:trpzSysPowerSupplyTable.setStatus(_A)
_TrpzSysPowerSupplyEntry_Object=MibTableRow
trpzSysPowerSupplyEntry=_TrpzSysPowerSupplyEntry_Object((1,3,6,1,4,1,14525,4,8,1,1,13,1,2,1))
trpzSysPowerSupplyEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:trpzSysPowerSupplyEntry.setStatus(_A)
_TrpzSysPowerSupplyDeviceOID_Type=ObjectIdentifier
_TrpzSysPowerSupplyDeviceOID_Object=MibTableColumn
trpzSysPowerSupplyDeviceOID=_TrpzSysPowerSupplyDeviceOID_Object((1,3,6,1,4,1,14525,4,8,1,1,13,1,2,1,1),_TrpzSysPowerSupplyDeviceOID_Type())
trpzSysPowerSupplyDeviceOID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzSysPowerSupplyDeviceOID.setStatus(_A)
_TrpzSysPowerSupplyStatus_Type=TrpzSysPowerSupplyStatus
_TrpzSysPowerSupplyStatus_Object=MibTableColumn
trpzSysPowerSupplyStatus=_TrpzSysPowerSupplyStatus_Object((1,3,6,1,4,1,14525,4,8,1,1,13,1,2,1,2),_TrpzSysPowerSupplyStatus_Type())
trpzSysPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysPowerSupplyStatus.setStatus(_A)
class _TrpzSysPowerSupplyDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TrpzSysPowerSupplyDescr_Type.__name__=_C
_TrpzSysPowerSupplyDescr_Object=MibTableColumn
trpzSysPowerSupplyDescr=_TrpzSysPowerSupplyDescr_Object((1,3,6,1,4,1,14525,4,8,1,1,13,1,2,1,3),_TrpzSysPowerSupplyDescr_Type())
trpzSysPowerSupplyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSysPowerSupplyDescr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'TrpzSysCpuLoad':TrpzSysCpuLoad,'TrpzSysMemoryAmount':TrpzSysMemoryAmount,'TrpzSysPowerSupplyStatus':TrpzSysPowerSupplyStatus,'trpzSystemMib':trpzSystemMib,'trpzSysObjects':trpzSysObjects,'trpzSysDataObjects':trpzSysDataObjects,'trpzSysCpuMemoryUsedBytes':trpzSysCpuMemoryUsedBytes,'trpzSysCpuMemoryTotalBytes':trpzSysCpuMemoryTotalBytes,'trpzSysFlashMemoryUsedBytes':trpzSysFlashMemoryUsedBytes,'trpzSysFlashMemoryTotalBytes':trpzSysFlashMemoryTotalBytes,'trpzSysCpuAverageLoad':trpzSysCpuAverageLoad,'trpzSysCpuMemorySize':trpzSysCpuMemorySize,'trpzSysCpuLoadDetail':trpzSysCpuLoadDetail,'trpzSysCpuInstantLoad':trpzSysCpuInstantLoad,'trpzSysCpuLastMinuteLoad':trpzSysCpuLastMinuteLoad,'trpzSysCpuLast5MinutesLoad':trpzSysCpuLast5MinutesLoad,'trpzSysCpuLastHourLoad':trpzSysCpuLastHourLoad,'trpzSysCpuLastDayLoad':trpzSysCpuLastDayLoad,'trpzSysCpuLast3DaysLoad':trpzSysCpuLast3DaysLoad,'trpzSysCpuMemoryUsageDetail':trpzSysCpuMemoryUsageDetail,'trpzSysCpuMemoryInstantUsage':trpzSysCpuMemoryInstantUsage,'trpzSysCpuMemoryLastMinuteUsage':trpzSysCpuMemoryLastMinuteUsage,'trpzSysCpuMemoryLast5MinutesUsage':trpzSysCpuMemoryLast5MinutesUsage,'trpzSysCpuMemoryLastHourUsage':trpzSysCpuMemoryLastHourUsage,'trpzSysCpuMemoryLastDayUsage':trpzSysCpuMemoryLastDayUsage,'trpzSysCpuMemoryLast3DaysUsage':trpzSysCpuMemoryLast3DaysUsage,'trpzSysChassisComponents':trpzSysChassisComponents,'trpzSysChasCompPowerSupplies':trpzSysChasCompPowerSupplies,'trpzSysNumPowerSuppliesSupported':trpzSysNumPowerSuppliesSupported,'trpzSysPowerSupplyTable':trpzSysPowerSupplyTable,'trpzSysPowerSupplyEntry':trpzSysPowerSupplyEntry,_F:trpzSysPowerSupplyDeviceOID,'trpzSysPowerSupplyStatus':trpzSysPowerSupplyStatus,'trpzSysPowerSupplyDescr':trpzSysPowerSupplyDescr})