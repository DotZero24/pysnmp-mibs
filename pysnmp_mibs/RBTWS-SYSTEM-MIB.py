_F='rbtwsSysPowerSupplyDeviceOID'
_E='RBTWS-SYSTEM-MIB'
_D='obsolete'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbtwsMibs,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
rbtwsSystemMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,4,8))
if mibBuilder.loadTexts:rbtwsSystemMib.setRevisions(('2007-08-14 00:12','2007-05-04 00:10','2007-03-14 00:07','2006-11-09 00:04','2006-06-06 00:03'))
class RbtwsSysCpuLoad(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class RbtwsSysMemoryAmount(TextualConvention,Unsigned32):status=_A
class RbtwsSysPowerSupplyStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('unknown',2),('ac-failed',3),('dc-failed',4),('ac-ok-dc-ok',5)))
_RbtwsSysObjects_ObjectIdentity=ObjectIdentity
rbtwsSysObjects=_RbtwsSysObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,8,1))
_RbtwsSysDataObjects_ObjectIdentity=ObjectIdentity
rbtwsSysDataObjects=_RbtwsSysDataObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,8,1,1))
_RbtwsSysCpuMemoryUsedBytes_Type=Unsigned32
_RbtwsSysCpuMemoryUsedBytes_Object=MibScalar
rbtwsSysCpuMemoryUsedBytes=_RbtwsSysCpuMemoryUsedBytes_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,1),_RbtwsSysCpuMemoryUsedBytes_Type())
rbtwsSysCpuMemoryUsedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryUsedBytes.setStatus(_D)
_RbtwsSysCpuMemoryTotalBytes_Type=Unsigned32
_RbtwsSysCpuMemoryTotalBytes_Object=MibScalar
rbtwsSysCpuMemoryTotalBytes=_RbtwsSysCpuMemoryTotalBytes_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,2),_RbtwsSysCpuMemoryTotalBytes_Type())
rbtwsSysCpuMemoryTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryTotalBytes.setStatus(_D)
_RbtwsSysFlashMemoryUsedBytes_Type=Unsigned32
_RbtwsSysFlashMemoryUsedBytes_Object=MibScalar
rbtwsSysFlashMemoryUsedBytes=_RbtwsSysFlashMemoryUsedBytes_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,3),_RbtwsSysFlashMemoryUsedBytes_Type())
rbtwsSysFlashMemoryUsedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysFlashMemoryUsedBytes.setStatus(_A)
_RbtwsSysFlashMemoryTotalBytes_Type=Unsigned32
_RbtwsSysFlashMemoryTotalBytes_Object=MibScalar
rbtwsSysFlashMemoryTotalBytes=_RbtwsSysFlashMemoryTotalBytes_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,4),_RbtwsSysFlashMemoryTotalBytes_Type())
rbtwsSysFlashMemoryTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysFlashMemoryTotalBytes.setStatus(_A)
_RbtwsSysCpuAverageLoad_Type=RbtwsSysCpuLoad
_RbtwsSysCpuAverageLoad_Object=MibScalar
rbtwsSysCpuAverageLoad=_RbtwsSysCpuAverageLoad_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,5),_RbtwsSysCpuAverageLoad_Type())
rbtwsSysCpuAverageLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuAverageLoad.setStatus(_A)
_RbtwsSysCpuMemorySize_Type=RbtwsSysMemoryAmount
_RbtwsSysCpuMemorySize_Object=MibScalar
rbtwsSysCpuMemorySize=_RbtwsSysCpuMemorySize_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,6),_RbtwsSysCpuMemorySize_Type())
rbtwsSysCpuMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemorySize.setStatus(_A)
_RbtwsSysCpuLoadDetail_ObjectIdentity=ObjectIdentity
rbtwsSysCpuLoadDetail=_RbtwsSysCpuLoadDetail_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,8,1,1,11))
_RbtwsSysCpuInstantLoad_Type=RbtwsSysCpuLoad
_RbtwsSysCpuInstantLoad_Object=MibScalar
rbtwsSysCpuInstantLoad=_RbtwsSysCpuInstantLoad_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,11,1),_RbtwsSysCpuInstantLoad_Type())
rbtwsSysCpuInstantLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuInstantLoad.setStatus(_A)
_RbtwsSysCpuLastMinuteLoad_Type=RbtwsSysCpuLoad
_RbtwsSysCpuLastMinuteLoad_Object=MibScalar
rbtwsSysCpuLastMinuteLoad=_RbtwsSysCpuLastMinuteLoad_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,11,2),_RbtwsSysCpuLastMinuteLoad_Type())
rbtwsSysCpuLastMinuteLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuLastMinuteLoad.setStatus(_A)
_RbtwsSysCpuLast5MinutesLoad_Type=RbtwsSysCpuLoad
_RbtwsSysCpuLast5MinutesLoad_Object=MibScalar
rbtwsSysCpuLast5MinutesLoad=_RbtwsSysCpuLast5MinutesLoad_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,11,3),_RbtwsSysCpuLast5MinutesLoad_Type())
rbtwsSysCpuLast5MinutesLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuLast5MinutesLoad.setStatus(_A)
_RbtwsSysCpuLastHourLoad_Type=RbtwsSysCpuLoad
_RbtwsSysCpuLastHourLoad_Object=MibScalar
rbtwsSysCpuLastHourLoad=_RbtwsSysCpuLastHourLoad_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,11,4),_RbtwsSysCpuLastHourLoad_Type())
rbtwsSysCpuLastHourLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuLastHourLoad.setStatus(_A)
_RbtwsSysCpuLastDayLoad_Type=RbtwsSysCpuLoad
_RbtwsSysCpuLastDayLoad_Object=MibScalar
rbtwsSysCpuLastDayLoad=_RbtwsSysCpuLastDayLoad_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,11,5),_RbtwsSysCpuLastDayLoad_Type())
rbtwsSysCpuLastDayLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuLastDayLoad.setStatus(_A)
_RbtwsSysCpuLast3DaysLoad_Type=RbtwsSysCpuLoad
_RbtwsSysCpuLast3DaysLoad_Object=MibScalar
rbtwsSysCpuLast3DaysLoad=_RbtwsSysCpuLast3DaysLoad_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,11,6),_RbtwsSysCpuLast3DaysLoad_Type())
rbtwsSysCpuLast3DaysLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuLast3DaysLoad.setStatus(_A)
_RbtwsSysCpuMemoryUsageDetail_ObjectIdentity=ObjectIdentity
rbtwsSysCpuMemoryUsageDetail=_RbtwsSysCpuMemoryUsageDetail_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,8,1,1,12))
_RbtwsSysCpuMemoryInstantUsage_Type=RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryInstantUsage_Object=MibScalar
rbtwsSysCpuMemoryInstantUsage=_RbtwsSysCpuMemoryInstantUsage_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,12,1),_RbtwsSysCpuMemoryInstantUsage_Type())
rbtwsSysCpuMemoryInstantUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryInstantUsage.setStatus(_A)
_RbtwsSysCpuMemoryLastMinuteUsage_Type=RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLastMinuteUsage_Object=MibScalar
rbtwsSysCpuMemoryLastMinuteUsage=_RbtwsSysCpuMemoryLastMinuteUsage_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,12,2),_RbtwsSysCpuMemoryLastMinuteUsage_Type())
rbtwsSysCpuMemoryLastMinuteUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryLastMinuteUsage.setStatus(_A)
_RbtwsSysCpuMemoryLast5MinutesUsage_Type=RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLast5MinutesUsage_Object=MibScalar
rbtwsSysCpuMemoryLast5MinutesUsage=_RbtwsSysCpuMemoryLast5MinutesUsage_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,12,3),_RbtwsSysCpuMemoryLast5MinutesUsage_Type())
rbtwsSysCpuMemoryLast5MinutesUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryLast5MinutesUsage.setStatus(_A)
_RbtwsSysCpuMemoryLastHourUsage_Type=RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLastHourUsage_Object=MibScalar
rbtwsSysCpuMemoryLastHourUsage=_RbtwsSysCpuMemoryLastHourUsage_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,12,4),_RbtwsSysCpuMemoryLastHourUsage_Type())
rbtwsSysCpuMemoryLastHourUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryLastHourUsage.setStatus(_A)
_RbtwsSysCpuMemoryLastDayUsage_Type=RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLastDayUsage_Object=MibScalar
rbtwsSysCpuMemoryLastDayUsage=_RbtwsSysCpuMemoryLastDayUsage_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,12,5),_RbtwsSysCpuMemoryLastDayUsage_Type())
rbtwsSysCpuMemoryLastDayUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryLastDayUsage.setStatus(_A)
_RbtwsSysCpuMemoryLast3DaysUsage_Type=RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLast3DaysUsage_Object=MibScalar
rbtwsSysCpuMemoryLast3DaysUsage=_RbtwsSysCpuMemoryLast3DaysUsage_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,12,6),_RbtwsSysCpuMemoryLast3DaysUsage_Type())
rbtwsSysCpuMemoryLast3DaysUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysCpuMemoryLast3DaysUsage.setStatus(_A)
_RbtwsSysChassisComponents_ObjectIdentity=ObjectIdentity
rbtwsSysChassisComponents=_RbtwsSysChassisComponents_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13))
_RbtwsSysChasCompPowerSupplies_ObjectIdentity=ObjectIdentity
rbtwsSysChasCompPowerSupplies=_RbtwsSysChasCompPowerSupplies_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13,1))
_RbtwsSysNumPowerSuppliesSupported_Type=Unsigned32
_RbtwsSysNumPowerSuppliesSupported_Object=MibScalar
rbtwsSysNumPowerSuppliesSupported=_RbtwsSysNumPowerSuppliesSupported_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13,1,1),_RbtwsSysNumPowerSuppliesSupported_Type())
rbtwsSysNumPowerSuppliesSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysNumPowerSuppliesSupported.setStatus(_A)
_RbtwsSysPowerSupplyTable_Object=MibTable
rbtwsSysPowerSupplyTable=_RbtwsSysPowerSupplyTable_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13,1,2))
if mibBuilder.loadTexts:rbtwsSysPowerSupplyTable.setStatus(_A)
_RbtwsSysPowerSupplyEntry_Object=MibTableRow
rbtwsSysPowerSupplyEntry=_RbtwsSysPowerSupplyEntry_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13,1,2,1))
rbtwsSysPowerSupplyEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rbtwsSysPowerSupplyEntry.setStatus(_A)
_RbtwsSysPowerSupplyDeviceOID_Type=ObjectIdentifier
_RbtwsSysPowerSupplyDeviceOID_Object=MibTableColumn
rbtwsSysPowerSupplyDeviceOID=_RbtwsSysPowerSupplyDeviceOID_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13,1,2,1,1),_RbtwsSysPowerSupplyDeviceOID_Type())
rbtwsSysPowerSupplyDeviceOID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbtwsSysPowerSupplyDeviceOID.setStatus(_A)
_RbtwsSysPowerSupplyStatus_Type=RbtwsSysPowerSupplyStatus
_RbtwsSysPowerSupplyStatus_Object=MibTableColumn
rbtwsSysPowerSupplyStatus=_RbtwsSysPowerSupplyStatus_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13,1,2,1,2),_RbtwsSysPowerSupplyStatus_Type())
rbtwsSysPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysPowerSupplyStatus.setStatus(_A)
class _RbtwsSysPowerSupplyDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsSysPowerSupplyDescr_Type.__name__=_C
_RbtwsSysPowerSupplyDescr_Object=MibTableColumn
rbtwsSysPowerSupplyDescr=_RbtwsSysPowerSupplyDescr_Object((1,3,6,1,4,1,52,4,15,1,4,8,1,1,13,1,2,1,3),_RbtwsSysPowerSupplyDescr_Type())
rbtwsSysPowerSupplyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSysPowerSupplyDescr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RbtwsSysCpuLoad':RbtwsSysCpuLoad,'RbtwsSysMemoryAmount':RbtwsSysMemoryAmount,'RbtwsSysPowerSupplyStatus':RbtwsSysPowerSupplyStatus,'rbtwsSystemMib':rbtwsSystemMib,'rbtwsSysObjects':rbtwsSysObjects,'rbtwsSysDataObjects':rbtwsSysDataObjects,'rbtwsSysCpuMemoryUsedBytes':rbtwsSysCpuMemoryUsedBytes,'rbtwsSysCpuMemoryTotalBytes':rbtwsSysCpuMemoryTotalBytes,'rbtwsSysFlashMemoryUsedBytes':rbtwsSysFlashMemoryUsedBytes,'rbtwsSysFlashMemoryTotalBytes':rbtwsSysFlashMemoryTotalBytes,'rbtwsSysCpuAverageLoad':rbtwsSysCpuAverageLoad,'rbtwsSysCpuMemorySize':rbtwsSysCpuMemorySize,'rbtwsSysCpuLoadDetail':rbtwsSysCpuLoadDetail,'rbtwsSysCpuInstantLoad':rbtwsSysCpuInstantLoad,'rbtwsSysCpuLastMinuteLoad':rbtwsSysCpuLastMinuteLoad,'rbtwsSysCpuLast5MinutesLoad':rbtwsSysCpuLast5MinutesLoad,'rbtwsSysCpuLastHourLoad':rbtwsSysCpuLastHourLoad,'rbtwsSysCpuLastDayLoad':rbtwsSysCpuLastDayLoad,'rbtwsSysCpuLast3DaysLoad':rbtwsSysCpuLast3DaysLoad,'rbtwsSysCpuMemoryUsageDetail':rbtwsSysCpuMemoryUsageDetail,'rbtwsSysCpuMemoryInstantUsage':rbtwsSysCpuMemoryInstantUsage,'rbtwsSysCpuMemoryLastMinuteUsage':rbtwsSysCpuMemoryLastMinuteUsage,'rbtwsSysCpuMemoryLast5MinutesUsage':rbtwsSysCpuMemoryLast5MinutesUsage,'rbtwsSysCpuMemoryLastHourUsage':rbtwsSysCpuMemoryLastHourUsage,'rbtwsSysCpuMemoryLastDayUsage':rbtwsSysCpuMemoryLastDayUsage,'rbtwsSysCpuMemoryLast3DaysUsage':rbtwsSysCpuMemoryLast3DaysUsage,'rbtwsSysChassisComponents':rbtwsSysChassisComponents,'rbtwsSysChasCompPowerSupplies':rbtwsSysChasCompPowerSupplies,'rbtwsSysNumPowerSuppliesSupported':rbtwsSysNumPowerSuppliesSupported,'rbtwsSysPowerSupplyTable':rbtwsSysPowerSupplyTable,'rbtwsSysPowerSupplyEntry':rbtwsSysPowerSupplyEntry,_F:rbtwsSysPowerSupplyDeviceOID,'rbtwsSysPowerSupplyStatus':rbtwsSysPowerSupplyStatus,'rbtwsSysPowerSupplyDescr':rbtwsSysPowerSupplyDescr})