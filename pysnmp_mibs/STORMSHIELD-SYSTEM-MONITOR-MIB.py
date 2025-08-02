_L='snsFanIndex'
_K='snsBypassIndex'
_J='snsCpuIndex'
_I='snsPowerSupplyIndex'
_H='snsDiskEntryIndex'
_G='Unsigned32'
_F='not-accessible'
_E='DisplayString'
_D='STORMSHIELD-SYSTEM-MONITOR-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TruthValue')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsSystemMonitor=ModuleIdentity((1,3,6,1,4,1,11256,1,10))
if mibBuilder.loadTexts:snsSystemMonitor.setRevisions(('2017-02-20 00:00',))
class _SnsDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsDate_Type.__name__=_E
_SnsDate_Object=MibScalar
snsDate=_SnsDate_Object((1,3,6,1,4,1,11256,1,10,1),_SnsDate_Type())
snsDate.setMaxAccess(_B)
if mibBuilder.loadTexts:snsDate.setStatus(_A)
class _SnsUptime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsUptime_Type.__name__=_E
_SnsUptime_Object=MibScalar
snsUptime=_SnsUptime_Object((1,3,6,1,4,1,11256,1,10,2),_SnsUptime_Type())
snsUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsUptime.setStatus(_A)
class _SnsMem_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsMem_Type.__name__=_E
_SnsMem_Object=MibScalar
snsMem=_SnsMem_Object((1,3,6,1,4,1,11256,1,10,3),_SnsMem_Type())
snsMem.setMaxAccess(_B)
if mibBuilder.loadTexts:snsMem.setStatus(_A)
class _SnsStatTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsStatTime_Type.__name__=_E
_SnsStatTime_Object=MibScalar
snsStatTime=_SnsStatTime_Object((1,3,6,1,4,1,11256,1,10,4),_SnsStatTime_Type())
snsStatTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsStatTime.setStatus(_A)
_SnsDiskTable_Object=MibTable
snsDiskTable=_SnsDiskTable_Object((1,3,6,1,4,1,11256,1,10,5))
if mibBuilder.loadTexts:snsDiskTable.setStatus(_A)
_SnsDiskEntry_Object=MibTableRow
snsDiskEntry=_SnsDiskEntry_Object((1,3,6,1,4,1,11256,1,10,5,1))
snsDiskEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:snsDiskEntry.setStatus(_A)
class _SnsDiskEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsDiskEntryIndex_Type.__name__=_C
_SnsDiskEntryIndex_Object=MibTableColumn
snsDiskEntryIndex=_SnsDiskEntryIndex_Object((1,3,6,1,4,1,11256,1,10,5,1,1),_SnsDiskEntryIndex_Type())
snsDiskEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsDiskEntryIndex.setStatus(_A)
_SnsDiskEntryDiskName_Type=DisplayString
_SnsDiskEntryDiskName_Object=MibTableColumn
snsDiskEntryDiskName=_SnsDiskEntryDiskName_Object((1,3,6,1,4,1,11256,1,10,5,1,2),_SnsDiskEntryDiskName_Type())
snsDiskEntryDiskName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsDiskEntryDiskName.setStatus(_A)
_SnsDiskEntrySmartResult_Type=DisplayString
_SnsDiskEntrySmartResult_Object=MibTableColumn
snsDiskEntrySmartResult=_SnsDiskEntrySmartResult_Object((1,3,6,1,4,1,11256,1,10,5,1,3),_SnsDiskEntrySmartResult_Type())
snsDiskEntrySmartResult.setMaxAccess(_B)
if mibBuilder.loadTexts:snsDiskEntrySmartResult.setStatus(_A)
class _SnsDiskEntryIsRaid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SnsDiskEntryIsRaid_Type.__name__=_C
_SnsDiskEntryIsRaid_Object=MibTableColumn
snsDiskEntryIsRaid=_SnsDiskEntryIsRaid_Object((1,3,6,1,4,1,11256,1,10,5,1,4),_SnsDiskEntryIsRaid_Type())
snsDiskEntryIsRaid.setMaxAccess(_B)
if mibBuilder.loadTexts:snsDiskEntryIsRaid.setStatus(_A)
_SnsDiskEntryRaidStatus_Type=DisplayString
_SnsDiskEntryRaidStatus_Object=MibTableColumn
snsDiskEntryRaidStatus=_SnsDiskEntryRaidStatus_Object((1,3,6,1,4,1,11256,1,10,5,1,5),_SnsDiskEntryRaidStatus_Type())
snsDiskEntryRaidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snsDiskEntryRaidStatus.setStatus(_A)
_SnsDiskEntryPosition_Type=DisplayString
_SnsDiskEntryPosition_Object=MibTableColumn
snsDiskEntryPosition=_SnsDiskEntryPosition_Object((1,3,6,1,4,1,11256,1,10,5,1,6),_SnsDiskEntryPosition_Type())
snsDiskEntryPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:snsDiskEntryPosition.setStatus(_A)
_SnsPowerSupplyTable_Object=MibTable
snsPowerSupplyTable=_SnsPowerSupplyTable_Object((1,3,6,1,4,1,11256,1,10,6))
if mibBuilder.loadTexts:snsPowerSupplyTable.setStatus(_A)
_SnsPowerSupplyEntry_Object=MibTableRow
snsPowerSupplyEntry=_SnsPowerSupplyEntry_Object((1,3,6,1,4,1,11256,1,10,6,1))
snsPowerSupplyEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:snsPowerSupplyEntry.setStatus(_A)
class _SnsPowerSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsPowerSupplyIndex_Type.__name__=_C
_SnsPowerSupplyIndex_Object=MibTableColumn
snsPowerSupplyIndex=_SnsPowerSupplyIndex_Object((1,3,6,1,4,1,11256,1,10,6,1,1),_SnsPowerSupplyIndex_Type())
snsPowerSupplyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsPowerSupplyIndex.setStatus(_A)
_SnsPowerSupplyPowered_Type=TruthValue
_SnsPowerSupplyPowered_Object=MibTableColumn
snsPowerSupplyPowered=_SnsPowerSupplyPowered_Object((1,3,6,1,4,1,11256,1,10,6,1,2),_SnsPowerSupplyPowered_Type())
snsPowerSupplyPowered.setMaxAccess(_B)
if mibBuilder.loadTexts:snsPowerSupplyPowered.setStatus(_A)
_SnsCpuTable_Object=MibTable
snsCpuTable=_SnsCpuTable_Object((1,3,6,1,4,1,11256,1,10,7))
if mibBuilder.loadTexts:snsCpuTable.setStatus(_A)
_SnsCpuEntry_Object=MibTableRow
snsCpuEntry=_SnsCpuEntry_Object((1,3,6,1,4,1,11256,1,10,7,1))
snsCpuEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:snsCpuEntry.setStatus(_A)
class _SnsCpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsCpuIndex_Type.__name__=_C
_SnsCpuIndex_Object=MibTableColumn
snsCpuIndex=_SnsCpuIndex_Object((1,3,6,1,4,1,11256,1,10,7,1,1),_SnsCpuIndex_Type())
snsCpuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsCpuIndex.setStatus(_A)
_SnsCpuTemp_Type=Integer32
_SnsCpuTemp_Object=MibTableColumn
snsCpuTemp=_SnsCpuTemp_Object((1,3,6,1,4,1,11256,1,10,7,1,2),_SnsCpuTemp_Type())
snsCpuTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:snsCpuTemp.setStatus(_A)
_SnsBypassTable_Object=MibTable
snsBypassTable=_SnsBypassTable_Object((1,3,6,1,4,1,11256,1,10,8))
if mibBuilder.loadTexts:snsBypassTable.setStatus(_A)
_SnsBypassEntry_Object=MibTableRow
snsBypassEntry=_SnsBypassEntry_Object((1,3,6,1,4,1,11256,1,10,8,1))
snsBypassEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:snsBypassEntry.setStatus(_A)
class _SnsBypassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsBypassIndex_Type.__name__=_C
_SnsBypassIndex_Object=MibTableColumn
snsBypassIndex=_SnsBypassIndex_Object((1,3,6,1,4,1,11256,1,10,8,1,1),_SnsBypassIndex_Type())
snsBypassIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsBypassIndex.setStatus(_A)
class _SnsBypassI2CAddress_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SnsBypassI2CAddress_Type.__name__=_G
_SnsBypassI2CAddress_Object=MibTableColumn
snsBypassI2CAddress=_SnsBypassI2CAddress_Object((1,3,6,1,4,1,11256,1,10,8,1,2),_SnsBypassI2CAddress_Type())
snsBypassI2CAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snsBypassI2CAddress.setStatus(_A)
_SnsBypassSystemOff_Type=TruthValue
_SnsBypassSystemOff_Object=MibTableColumn
snsBypassSystemOff=_SnsBypassSystemOff_Object((1,3,6,1,4,1,11256,1,10,8,1,3),_SnsBypassSystemOff_Type())
snsBypassSystemOff.setMaxAccess(_B)
if mibBuilder.loadTexts:snsBypassSystemOff.setStatus(_A)
_SnsBypassJustOn_Type=TruthValue
_SnsBypassJustOn_Object=MibTableColumn
snsBypassJustOn=_SnsBypassJustOn_Object((1,3,6,1,4,1,11256,1,10,8,1,4),_SnsBypassJustOn_Type())
snsBypassJustOn.setMaxAccess(_B)
if mibBuilder.loadTexts:snsBypassJustOn.setStatus(_A)
_SnsBypassRunTime_Type=TruthValue
_SnsBypassRunTime_Object=MibTableColumn
snsBypassRunTime=_SnsBypassRunTime_Object((1,3,6,1,4,1,11256,1,10,8,1,5),_SnsBypassRunTime_Type())
snsBypassRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsBypassRunTime.setStatus(_A)
_SnsBypassWatchdog_Type=TruthValue
_SnsBypassWatchdog_Object=MibTableColumn
snsBypassWatchdog=_SnsBypassWatchdog_Object((1,3,6,1,4,1,11256,1,10,8,1,6),_SnsBypassWatchdog_Type())
snsBypassWatchdog.setMaxAccess(_B)
if mibBuilder.loadTexts:snsBypassWatchdog.setStatus(_A)
_SnsFanTable_Object=MibTable
snsFanTable=_SnsFanTable_Object((1,3,6,1,4,1,11256,1,10,9))
if mibBuilder.loadTexts:snsFanTable.setStatus(_A)
_SnsFanEntry_Object=MibTableRow
snsFanEntry=_SnsFanEntry_Object((1,3,6,1,4,1,11256,1,10,9,1))
snsFanEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:snsFanEntry.setStatus(_A)
class _SnsFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsFanIndex_Type.__name__=_C
_SnsFanIndex_Object=MibTableColumn
snsFanIndex=_SnsFanIndex_Object((1,3,6,1,4,1,11256,1,10,9,1,1),_SnsFanIndex_Type())
snsFanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsFanIndex.setStatus(_A)
_SnsFanName_Type=DisplayString
_SnsFanName_Object=MibTableColumn
snsFanName=_SnsFanName_Object((1,3,6,1,4,1,11256,1,10,9,1,2),_SnsFanName_Type())
snsFanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsFanName.setStatus(_A)
_SnsFanStatus_Type=DisplayString
_SnsFanStatus_Object=MibTableColumn
snsFanStatus=_SnsFanStatus_Object((1,3,6,1,4,1,11256,1,10,9,1,3),_SnsFanStatus_Type())
snsFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snsFanStatus.setStatus(_A)
class _SnsFanRpm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SnsFanRpm_Type.__name__=_G
_SnsFanRpm_Object=MibTableColumn
snsFanRpm=_SnsFanRpm_Object((1,3,6,1,4,1,11256,1,10,9,1,4),_SnsFanRpm_Type())
snsFanRpm.setMaxAccess(_B)
if mibBuilder.loadTexts:snsFanRpm.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsSystemMonitor':snsSystemMonitor,'snsDate':snsDate,'snsUptime':snsUptime,'snsMem':snsMem,'snsStatTime':snsStatTime,'snsDiskTable':snsDiskTable,'snsDiskEntry':snsDiskEntry,_H:snsDiskEntryIndex,'snsDiskEntryDiskName':snsDiskEntryDiskName,'snsDiskEntrySmartResult':snsDiskEntrySmartResult,'snsDiskEntryIsRaid':snsDiskEntryIsRaid,'snsDiskEntryRaidStatus':snsDiskEntryRaidStatus,'snsDiskEntryPosition':snsDiskEntryPosition,'snsPowerSupplyTable':snsPowerSupplyTable,'snsPowerSupplyEntry':snsPowerSupplyEntry,_I:snsPowerSupplyIndex,'snsPowerSupplyPowered':snsPowerSupplyPowered,'snsCpuTable':snsCpuTable,'snsCpuEntry':snsCpuEntry,_J:snsCpuIndex,'snsCpuTemp':snsCpuTemp,'snsBypassTable':snsBypassTable,'snsBypassEntry':snsBypassEntry,_K:snsBypassIndex,'snsBypassI2CAddress':snsBypassI2CAddress,'snsBypassSystemOff':snsBypassSystemOff,'snsBypassJustOn':snsBypassJustOn,'snsBypassRunTime':snsBypassRunTime,'snsBypassWatchdog':snsBypassWatchdog,'snsFanTable':snsFanTable,'snsFanEntry':snsFanEntry,_L:snsFanIndex,'snsFanName':snsFanName,'snsFanStatus':snsFanStatus,'snsFanRpm':snsFanRpm})