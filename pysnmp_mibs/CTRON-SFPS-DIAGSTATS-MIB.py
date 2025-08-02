_F='sfpsFloodCountersSource'
_E='CTRON-SFPS-DIAGSTATS-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsFloodCounters,sfpsFloodCountersReset,sfpsIsolatedSwitch,sfpsResetNVRAM=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsFloodCounters','sfpsFloodCountersReset','sfpsIsolatedSwitch','sfpsResetNVRAM')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsFloodCountersTable_Object=MibTable
sfpsFloodCountersTable=_SfpsFloodCountersTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1))
if mibBuilder.loadTexts:sfpsFloodCountersTable.setStatus(_A)
_SfpsFloodCountersEntry_Object=MibTableRow
sfpsFloodCountersEntry=_SfpsFloodCountersEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1))
sfpsFloodCountersEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sfpsFloodCountersEntry.setStatus(_A)
_SfpsFloodCountersSource_Type=SfpsAddress
_SfpsFloodCountersSource_Object=MibTableColumn
sfpsFloodCountersSource=_SfpsFloodCountersSource_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1,1),_SfpsFloodCountersSource_Type())
sfpsFloodCountersSource.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersSource.setStatus(_A)
_SfpsFloodCountersNumFloods_Type=Integer32
_SfpsFloodCountersNumFloods_Object=MibTableColumn
sfpsFloodCountersNumFloods=_SfpsFloodCountersNumFloods_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1,2),_SfpsFloodCountersNumFloods_Type())
sfpsFloodCountersNumFloods.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersNumFloods.setStatus(_A)
_SfpsFloodCountersLastSeqNum_Type=Integer32
_SfpsFloodCountersLastSeqNum_Object=MibTableColumn
sfpsFloodCountersLastSeqNum=_SfpsFloodCountersLastSeqNum_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1,3),_SfpsFloodCountersLastSeqNum_Type())
sfpsFloodCountersLastSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersLastSeqNum.setStatus(_A)
_SfpsFloodCountersNumDrops_Type=Integer32
_SfpsFloodCountersNumDrops_Object=MibTableColumn
sfpsFloodCountersNumDrops=_SfpsFloodCountersNumDrops_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1,4),_SfpsFloodCountersNumDrops_Type())
sfpsFloodCountersNumDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersNumDrops.setStatus(_A)
_SfpsFloodCountersLastDropTime_Type=TimeTicks
_SfpsFloodCountersLastDropTime_Object=MibTableColumn
sfpsFloodCountersLastDropTime=_SfpsFloodCountersLastDropTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1,5),_SfpsFloodCountersLastDropTime_Type())
sfpsFloodCountersLastDropTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersLastDropTime.setStatus(_A)
_SfpsFloodCountersMaxDrops_Type=Integer32
_SfpsFloodCountersMaxDrops_Object=MibTableColumn
sfpsFloodCountersMaxDrops=_SfpsFloodCountersMaxDrops_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1,6),_SfpsFloodCountersMaxDrops_Type())
sfpsFloodCountersMaxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersMaxDrops.setStatus(_A)
_SfpsFloodCountersMaxDropsTime_Type=TimeTicks
_SfpsFloodCountersMaxDropsTime_Object=MibTableColumn
sfpsFloodCountersMaxDropsTime=_SfpsFloodCountersMaxDropsTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,1,1,1,7),_SfpsFloodCountersMaxDropsTime_Type())
sfpsFloodCountersMaxDropsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersMaxDropsTime.setStatus(_A)
_SfpsFloodCountersResetReset_Type=Integer32
_SfpsFloodCountersResetReset_Object=MibScalar
sfpsFloodCountersResetReset=_SfpsFloodCountersResetReset_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,2,1),_SfpsFloodCountersResetReset_Type())
sfpsFloodCountersResetReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsFloodCountersResetReset.setStatus(_A)
_SfpsFloodCountersTotalDropped_Type=Integer32
_SfpsFloodCountersTotalDropped_Object=MibScalar
sfpsFloodCountersTotalDropped=_SfpsFloodCountersTotalDropped_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,2,2),_SfpsFloodCountersTotalDropped_Type())
sfpsFloodCountersTotalDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersTotalDropped.setStatus(_A)
_SfpsFloodCountersTotalRunts_Type=Integer32
_SfpsFloodCountersTotalRunts_Object=MibScalar
sfpsFloodCountersTotalRunts=_SfpsFloodCountersTotalRunts_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,2,3),_SfpsFloodCountersTotalRunts_Type())
sfpsFloodCountersTotalRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersTotalRunts.setStatus(_A)
_SfpsFloodCountersTotalSelfOrig_Type=Integer32
_SfpsFloodCountersTotalSelfOrig_Object=MibScalar
sfpsFloodCountersTotalSelfOrig=_SfpsFloodCountersTotalSelfOrig_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,2,4),_SfpsFloodCountersTotalSelfOrig_Type())
sfpsFloodCountersTotalSelfOrig.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersTotalSelfOrig.setStatus(_A)
_SfpsFloodCountersNonNetPort_Type=Integer32
_SfpsFloodCountersNonNetPort_Object=MibScalar
sfpsFloodCountersNonNetPort=_SfpsFloodCountersNonNetPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,2,5),_SfpsFloodCountersNonNetPort_Type())
sfpsFloodCountersNonNetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFloodCountersNonNetPort.setStatus(_A)
class _SfpsIsolatedSwitchIsolatedSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('yes',1))
_SfpsIsolatedSwitchIsolatedSwitch_Type.__name__=_D
_SfpsIsolatedSwitchIsolatedSwitch_Object=MibScalar
sfpsIsolatedSwitchIsolatedSwitch=_SfpsIsolatedSwitchIsolatedSwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,5,1),_SfpsIsolatedSwitchIsolatedSwitch_Type())
sfpsIsolatedSwitchIsolatedSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIsolatedSwitchIsolatedSwitch.setStatus(_A)
_SfpsIsolatedSwitchResetCounters_Type=Integer32
_SfpsIsolatedSwitchResetCounters_Object=MibScalar
sfpsIsolatedSwitchResetCounters=_SfpsIsolatedSwitchResetCounters_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,5,2),_SfpsIsolatedSwitchResetCounters_Type())
sfpsIsolatedSwitchResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsIsolatedSwitchResetCounters.setStatus(_A)
_SfpsIsolatedSwitchINBDropped_Type=Integer32
_SfpsIsolatedSwitchINBDropped_Object=MibScalar
sfpsIsolatedSwitchINBDropped=_SfpsIsolatedSwitchINBDropped_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,5,3),_SfpsIsolatedSwitchINBDropped_Type())
sfpsIsolatedSwitchINBDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIsolatedSwitchINBDropped.setStatus(_A)
_SfpsIsolatedSwitchINBNotSent_Type=Integer32
_SfpsIsolatedSwitchINBNotSent_Object=MibScalar
sfpsIsolatedSwitchINBNotSent=_SfpsIsolatedSwitchINBNotSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,2,5,4),_SfpsIsolatedSwitchINBNotSent_Type())
sfpsIsolatedSwitchINBNotSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIsolatedSwitchINBNotSent.setStatus(_A)
_SfpsResetNVRAMPercentNvramAvailable_Type=Integer32
_SfpsResetNVRAMPercentNvramAvailable_Object=MibScalar
sfpsResetNVRAMPercentNvramAvailable=_SfpsResetNVRAMPercentNvramAvailable_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,3,1),_SfpsResetNVRAMPercentNvramAvailable_Type())
sfpsResetNVRAMPercentNvramAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResetNVRAMPercentNvramAvailable.setStatus(_A)
_SfpsResetNVRAMTotalNVRAM_Type=Integer32
_SfpsResetNVRAMTotalNVRAM_Object=MibScalar
sfpsResetNVRAMTotalNVRAM=_SfpsResetNVRAMTotalNVRAM_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,3,2),_SfpsResetNVRAMTotalNVRAM_Type())
sfpsResetNVRAMTotalNVRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResetNVRAMTotalNVRAM.setStatus(_A)
_SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Type=Integer32
_SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Object=MibScalar
sfpsResetNVRAMOnetoResetNvramAndRestoreIP=_SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,3,3),_SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Type())
sfpsResetNVRAMOnetoResetNvramAndRestoreIP.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResetNVRAMOnetoResetNvramAndRestoreIP.setStatus(_A)
_SfpsResetNVRAMDelayTimer_Type=Integer32
_SfpsResetNVRAMDelayTimer_Object=MibScalar
sfpsResetNVRAMDelayTimer=_SfpsResetNVRAMDelayTimer_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,3,4),_SfpsResetNVRAMDelayTimer_Type())
sfpsResetNVRAMDelayTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResetNVRAMDelayTimer.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'SfpsAddress':SfpsAddress,'sfpsFloodCountersTable':sfpsFloodCountersTable,'sfpsFloodCountersEntry':sfpsFloodCountersEntry,_F:sfpsFloodCountersSource,'sfpsFloodCountersNumFloods':sfpsFloodCountersNumFloods,'sfpsFloodCountersLastSeqNum':sfpsFloodCountersLastSeqNum,'sfpsFloodCountersNumDrops':sfpsFloodCountersNumDrops,'sfpsFloodCountersLastDropTime':sfpsFloodCountersLastDropTime,'sfpsFloodCountersMaxDrops':sfpsFloodCountersMaxDrops,'sfpsFloodCountersMaxDropsTime':sfpsFloodCountersMaxDropsTime,'sfpsFloodCountersResetReset':sfpsFloodCountersResetReset,'sfpsFloodCountersTotalDropped':sfpsFloodCountersTotalDropped,'sfpsFloodCountersTotalRunts':sfpsFloodCountersTotalRunts,'sfpsFloodCountersTotalSelfOrig':sfpsFloodCountersTotalSelfOrig,'sfpsFloodCountersNonNetPort':sfpsFloodCountersNonNetPort,'sfpsIsolatedSwitchIsolatedSwitch':sfpsIsolatedSwitchIsolatedSwitch,'sfpsIsolatedSwitchResetCounters':sfpsIsolatedSwitchResetCounters,'sfpsIsolatedSwitchINBDropped':sfpsIsolatedSwitchINBDropped,'sfpsIsolatedSwitchINBNotSent':sfpsIsolatedSwitchINBNotSent,'sfpsResetNVRAMPercentNvramAvailable':sfpsResetNVRAMPercentNvramAvailable,'sfpsResetNVRAMTotalNVRAM':sfpsResetNVRAMTotalNVRAM,'sfpsResetNVRAMOnetoResetNvramAndRestoreIP':sfpsResetNVRAMOnetoResetNvramAndRestoreIP,'sfpsResetNVRAMDelayTimer':sfpsResetNVRAMDelayTimer})