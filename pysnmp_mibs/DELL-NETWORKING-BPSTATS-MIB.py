_Z='bpCosStatsCOSNumber'
_Y='bpCosStatsPortIndex'
_X='bpCosStatsPortPipe'
_W='bpCosStatsStackUnitIndex'
_V='bpBufferStatsPortIndex'
_U='bpBufferStatsPortPipe'
_T='bpBufferStatsStackUnitIndex'
_S='bpPacketBufferPortPipe'
_R='bpPacketBufferStackUnitIndex'
_Q='bpIfStatsPortIndex'
_P='bpIfStatsPortPipe'
_O='bpIfStatsStackUnitIndex'
_N='bpDropsPortIndex'
_M='bpDropsPortPipe'
_L='bpDropsStackUnitIndex'
_K='read-write'
_J='bpLinkBundleLocalId'
_I='bpLinkBundleNpuUnit'
_H='bpLinkBundleSlot'
_G='bpLinkBundleType'
_F='accessible-for-notify'
_E='not-accessible'
_D='Integer32'
_C='DELL-NETWORKING-BPSTATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
dellNetBpStatsMib=ModuleIdentity((1,3,6,1,4,1,6027,3,24))
if mibBuilder.loadTexts:dellNetBpStatsMib.setRevisions(('2013-05-22 12:48',))
_DellNetBpStatsLinkBundleObjects_ObjectIdentity=ObjectIdentity
dellNetBpStatsLinkBundleObjects=_DellNetBpStatsLinkBundleObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,24,1))
_BpLinkBundleObjects_ObjectIdentity=ObjectIdentity
bpLinkBundleObjects=_BpLinkBundleObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,24,1,1))
class _BpLinkBundleRateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,299))
_BpLinkBundleRateInterval_Type.__name__=_D
_BpLinkBundleRateInterval_Object=MibScalar
bpLinkBundleRateInterval=_BpLinkBundleRateInterval_Object((1,3,6,1,4,1,6027,3,24,1,1,1),_BpLinkBundleRateInterval_Type())
bpLinkBundleRateInterval.setMaxAccess(_K)
if mibBuilder.loadTexts:bpLinkBundleRateInterval.setStatus(_A)
class _BpLinkBundleTriggerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,90))
_BpLinkBundleTriggerThreshold_Type.__name__=_D
_BpLinkBundleTriggerThreshold_Object=MibScalar
bpLinkBundleTriggerThreshold=_BpLinkBundleTriggerThreshold_Object((1,3,6,1,4,1,6027,3,24,1,1,2),_BpLinkBundleTriggerThreshold_Type())
bpLinkBundleTriggerThreshold.setMaxAccess(_K)
if mibBuilder.loadTexts:bpLinkBundleTriggerThreshold.setStatus(_A)
if mibBuilder.loadTexts:bpLinkBundleTriggerThreshold.setUnits('percent')
_DellNetBpStatsObjects_ObjectIdentity=ObjectIdentity
dellNetBpStatsObjects=_DellNetBpStatsObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,24,2))
_BpStatsObjects_ObjectIdentity=ObjectIdentity
bpStatsObjects=_BpStatsObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,24,2,1))
_BpDropsTable_Object=MibTable
bpDropsTable=_BpDropsTable_Object((1,3,6,1,4,1,6027,3,24,2,1,1))
if mibBuilder.loadTexts:bpDropsTable.setStatus(_A)
_BpDropsEntry_Object=MibTableRow
bpDropsEntry=_BpDropsEntry_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1))
bpDropsEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:bpDropsEntry.setStatus(_A)
class _BpDropsStackUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_BpDropsStackUnitIndex_Type.__name__=_D
_BpDropsStackUnitIndex_Object=MibTableColumn
bpDropsStackUnitIndex=_BpDropsStackUnitIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,1),_BpDropsStackUnitIndex_Type())
bpDropsStackUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpDropsStackUnitIndex.setStatus(_A)
class _BpDropsPortPipe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_BpDropsPortPipe_Type.__name__=_D
_BpDropsPortPipe_Object=MibTableColumn
bpDropsPortPipe=_BpDropsPortPipe_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,2),_BpDropsPortPipe_Type())
bpDropsPortPipe.setMaxAccess(_E)
if mibBuilder.loadTexts:bpDropsPortPipe.setStatus(_A)
class _BpDropsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_BpDropsPortIndex_Type.__name__=_D
_BpDropsPortIndex_Object=MibTableColumn
bpDropsPortIndex=_BpDropsPortIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,3),_BpDropsPortIndex_Type())
bpDropsPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpDropsPortIndex.setStatus(_A)
_BpDropsInDrops_Type=Counter64
_BpDropsInDrops_Object=MibTableColumn
bpDropsInDrops=_BpDropsInDrops_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,4),_BpDropsInDrops_Type())
bpDropsInDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsInDrops.setStatus(_A)
_BpDropsInUnKnownHgHdr_Type=Counter64
_BpDropsInUnKnownHgHdr_Object=MibTableColumn
bpDropsInUnKnownHgHdr=_BpDropsInUnKnownHgHdr_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,5),_BpDropsInUnKnownHgHdr_Type())
bpDropsInUnKnownHgHdr.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsInUnKnownHgHdr.setStatus(_A)
_BpDropsInUnKnownHgOpcode_Type=Counter64
_BpDropsInUnKnownHgOpcode_Object=MibTableColumn
bpDropsInUnKnownHgOpcode=_BpDropsInUnKnownHgOpcode_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,6),_BpDropsInUnKnownHgOpcode_Type())
bpDropsInUnKnownHgOpcode.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsInUnKnownHgOpcode.setStatus(_A)
_BpDropsInMTUExceeds_Type=Counter64
_BpDropsInMTUExceeds_Object=MibTableColumn
bpDropsInMTUExceeds=_BpDropsInMTUExceeds_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,7),_BpDropsInMTUExceeds_Type())
bpDropsInMTUExceeds.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsInMTUExceeds.setStatus(_A)
_BpDropsInMacDrops_Type=Counter64
_BpDropsInMacDrops_Object=MibTableColumn
bpDropsInMacDrops=_BpDropsInMacDrops_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,8),_BpDropsInMacDrops_Type())
bpDropsInMacDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsInMacDrops.setStatus(_A)
_BpDropsMMUHOLDrops_Type=Counter64
_BpDropsMMUHOLDrops_Object=MibTableColumn
bpDropsMMUHOLDrops=_BpDropsMMUHOLDrops_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,9),_BpDropsMMUHOLDrops_Type())
bpDropsMMUHOLDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsMMUHOLDrops.setStatus(_A)
_BpDropsEgMacDrops_Type=Counter64
_BpDropsEgMacDrops_Object=MibTableColumn
bpDropsEgMacDrops=_BpDropsEgMacDrops_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,10),_BpDropsEgMacDrops_Type())
bpDropsEgMacDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsEgMacDrops.setStatus(_A)
_BpDropsEgTxAgedCounter_Type=Counter64
_BpDropsEgTxAgedCounter_Object=MibTableColumn
bpDropsEgTxAgedCounter=_BpDropsEgTxAgedCounter_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,11),_BpDropsEgTxAgedCounter_Type())
bpDropsEgTxAgedCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsEgTxAgedCounter.setStatus(_A)
_BpDropsEgTxErrCounter_Type=Counter64
_BpDropsEgTxErrCounter_Object=MibTableColumn
bpDropsEgTxErrCounter=_BpDropsEgTxErrCounter_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,12),_BpDropsEgTxErrCounter_Type())
bpDropsEgTxErrCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsEgTxErrCounter.setStatus(_A)
_BpDropsEgTxMACUnderflow_Type=Counter64
_BpDropsEgTxMACUnderflow_Object=MibTableColumn
bpDropsEgTxMACUnderflow=_BpDropsEgTxMACUnderflow_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,13),_BpDropsEgTxMACUnderflow_Type())
bpDropsEgTxMACUnderflow.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsEgTxMACUnderflow.setStatus(_A)
_BpDropsEgTxErrPktCounter_Type=Counter64
_BpDropsEgTxErrPktCounter_Object=MibTableColumn
bpDropsEgTxErrPktCounter=_BpDropsEgTxErrPktCounter_Object((1,3,6,1,4,1,6027,3,24,2,1,1,1,14),_BpDropsEgTxErrPktCounter_Type())
bpDropsEgTxErrPktCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:bpDropsEgTxErrPktCounter.setStatus(_A)
_BpIfStatsTable_Object=MibTable
bpIfStatsTable=_BpIfStatsTable_Object((1,3,6,1,4,1,6027,3,24,2,1,2))
if mibBuilder.loadTexts:bpIfStatsTable.setStatus(_A)
_BpIfStatsEntry_Object=MibTableRow
bpIfStatsEntry=_BpIfStatsEntry_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1))
bpIfStatsEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:bpIfStatsEntry.setStatus(_A)
class _BpIfStatsStackUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_BpIfStatsStackUnitIndex_Type.__name__=_D
_BpIfStatsStackUnitIndex_Object=MibTableColumn
bpIfStatsStackUnitIndex=_BpIfStatsStackUnitIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,1),_BpIfStatsStackUnitIndex_Type())
bpIfStatsStackUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpIfStatsStackUnitIndex.setStatus(_A)
class _BpIfStatsPortPipe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_BpIfStatsPortPipe_Type.__name__=_D
_BpIfStatsPortPipe_Object=MibTableColumn
bpIfStatsPortPipe=_BpIfStatsPortPipe_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,2),_BpIfStatsPortPipe_Type())
bpIfStatsPortPipe.setMaxAccess(_E)
if mibBuilder.loadTexts:bpIfStatsPortPipe.setStatus(_A)
class _BpIfStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_BpIfStatsPortIndex_Type.__name__=_D
_BpIfStatsPortIndex_Object=MibTableColumn
bpIfStatsPortIndex=_BpIfStatsPortIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,3),_BpIfStatsPortIndex_Type())
bpIfStatsPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpIfStatsPortIndex.setStatus(_A)
_BpIfStatsIn64BytePkts_Type=Counter64
_BpIfStatsIn64BytePkts_Object=MibTableColumn
bpIfStatsIn64BytePkts=_BpIfStatsIn64BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,4),_BpIfStatsIn64BytePkts_Type())
bpIfStatsIn64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsIn64BytePkts.setStatus(_A)
_BpIfStatsIn65To127BytePkts_Type=Counter64
_BpIfStatsIn65To127BytePkts_Object=MibTableColumn
bpIfStatsIn65To127BytePkts=_BpIfStatsIn65To127BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,5),_BpIfStatsIn65To127BytePkts_Type())
bpIfStatsIn65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsIn65To127BytePkts.setStatus(_A)
_BpIfStatsIn128To255BytePkts_Type=Counter64
_BpIfStatsIn128To255BytePkts_Object=MibTableColumn
bpIfStatsIn128To255BytePkts=_BpIfStatsIn128To255BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,6),_BpIfStatsIn128To255BytePkts_Type())
bpIfStatsIn128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsIn128To255BytePkts.setStatus(_A)
_BpIfStatsIn256To511BytePkts_Type=Counter64
_BpIfStatsIn256To511BytePkts_Object=MibTableColumn
bpIfStatsIn256To511BytePkts=_BpIfStatsIn256To511BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,7),_BpIfStatsIn256To511BytePkts_Type())
bpIfStatsIn256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsIn256To511BytePkts.setStatus(_A)
_BpIfStatsIn512To1023BytePkts_Type=Counter64
_BpIfStatsIn512To1023BytePkts_Object=MibTableColumn
bpIfStatsIn512To1023BytePkts=_BpIfStatsIn512To1023BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,8),_BpIfStatsIn512To1023BytePkts_Type())
bpIfStatsIn512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsIn512To1023BytePkts.setStatus(_A)
_BpIfStatsInOver1023BytePkts_Type=Counter64
_BpIfStatsInOver1023BytePkts_Object=MibTableColumn
bpIfStatsInOver1023BytePkts=_BpIfStatsInOver1023BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,9),_BpIfStatsInOver1023BytePkts_Type())
bpIfStatsInOver1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsInOver1023BytePkts.setStatus(_A)
_BpIfStatsInThrottles_Type=Counter64
_BpIfStatsInThrottles_Object=MibTableColumn
bpIfStatsInThrottles=_BpIfStatsInThrottles_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,10),_BpIfStatsInThrottles_Type())
bpIfStatsInThrottles.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsInThrottles.setStatus(_A)
_BpIfStatsInRunts_Type=Counter64
_BpIfStatsInRunts_Object=MibTableColumn
bpIfStatsInRunts=_BpIfStatsInRunts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,11),_BpIfStatsInRunts_Type())
bpIfStatsInRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsInRunts.setStatus(_A)
_BpIfStatsInGiants_Type=Counter64
_BpIfStatsInGiants_Object=MibTableColumn
bpIfStatsInGiants=_BpIfStatsInGiants_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,12),_BpIfStatsInGiants_Type())
bpIfStatsInGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsInGiants.setStatus(_A)
_BpIfStatsInCRC_Type=Counter64
_BpIfStatsInCRC_Object=MibTableColumn
bpIfStatsInCRC=_BpIfStatsInCRC_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,13),_BpIfStatsInCRC_Type())
bpIfStatsInCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsInCRC.setStatus(_A)
_BpIfStatsInOverruns_Type=Counter64
_BpIfStatsInOverruns_Object=MibTableColumn
bpIfStatsInOverruns=_BpIfStatsInOverruns_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,14),_BpIfStatsInOverruns_Type())
bpIfStatsInOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsInOverruns.setStatus(_A)
_BpIfStatsOutUnderruns_Type=Counter64
_BpIfStatsOutUnderruns_Object=MibTableColumn
bpIfStatsOutUnderruns=_BpIfStatsOutUnderruns_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,15),_BpIfStatsOutUnderruns_Type())
bpIfStatsOutUnderruns.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOutUnderruns.setStatus(_A)
_BpIfStatsOutUnicasts_Type=Counter64
_BpIfStatsOutUnicasts_Object=MibTableColumn
bpIfStatsOutUnicasts=_BpIfStatsOutUnicasts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,16),_BpIfStatsOutUnicasts_Type())
bpIfStatsOutUnicasts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOutUnicasts.setStatus(_A)
_BpIfStatsOutCollisions_Type=Counter64
_BpIfStatsOutCollisions_Object=MibTableColumn
bpIfStatsOutCollisions=_BpIfStatsOutCollisions_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,17),_BpIfStatsOutCollisions_Type())
bpIfStatsOutCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOutCollisions.setStatus(_A)
_BpIfStatsOutWredDrops_Type=Counter64
_BpIfStatsOutWredDrops_Object=MibTableColumn
bpIfStatsOutWredDrops=_BpIfStatsOutWredDrops_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,18),_BpIfStatsOutWredDrops_Type())
bpIfStatsOutWredDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOutWredDrops.setStatus(_A)
_BpIfStatsOut64BytePkts_Type=Counter64
_BpIfStatsOut64BytePkts_Object=MibTableColumn
bpIfStatsOut64BytePkts=_BpIfStatsOut64BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,19),_BpIfStatsOut64BytePkts_Type())
bpIfStatsOut64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOut64BytePkts.setStatus(_A)
_BpIfStatsOut65To127BytePkts_Type=Counter64
_BpIfStatsOut65To127BytePkts_Object=MibTableColumn
bpIfStatsOut65To127BytePkts=_BpIfStatsOut65To127BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,20),_BpIfStatsOut65To127BytePkts_Type())
bpIfStatsOut65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOut65To127BytePkts.setStatus(_A)
_BpIfStatsOut128To255BytePkts_Type=Counter64
_BpIfStatsOut128To255BytePkts_Object=MibTableColumn
bpIfStatsOut128To255BytePkts=_BpIfStatsOut128To255BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,21),_BpIfStatsOut128To255BytePkts_Type())
bpIfStatsOut128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOut128To255BytePkts.setStatus(_A)
_BpIfStatsOut256To511BytePkts_Type=Counter64
_BpIfStatsOut256To511BytePkts_Object=MibTableColumn
bpIfStatsOut256To511BytePkts=_BpIfStatsOut256To511BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,22),_BpIfStatsOut256To511BytePkts_Type())
bpIfStatsOut256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOut256To511BytePkts.setStatus(_A)
_BpIfStatsOut512To1023BytePkts_Type=Counter64
_BpIfStatsOut512To1023BytePkts_Object=MibTableColumn
bpIfStatsOut512To1023BytePkts=_BpIfStatsOut512To1023BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,23),_BpIfStatsOut512To1023BytePkts_Type())
bpIfStatsOut512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOut512To1023BytePkts.setStatus(_A)
_BpIfStatsOutOver1023BytePkts_Type=Counter64
_BpIfStatsOutOver1023BytePkts_Object=MibTableColumn
bpIfStatsOutOver1023BytePkts=_BpIfStatsOutOver1023BytePkts_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,24),_BpIfStatsOutOver1023BytePkts_Type())
bpIfStatsOutOver1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOutOver1023BytePkts.setStatus(_A)
_BpIfStatsOutThrottles_Type=Counter64
_BpIfStatsOutThrottles_Object=MibTableColumn
bpIfStatsOutThrottles=_BpIfStatsOutThrottles_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,25),_BpIfStatsOutThrottles_Type())
bpIfStatsOutThrottles.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOutThrottles.setStatus(_A)
_BpIfStatsLastDiscontinuityTime_Type=TimeStamp
_BpIfStatsLastDiscontinuityTime_Object=MibTableColumn
bpIfStatsLastDiscontinuityTime=_BpIfStatsLastDiscontinuityTime_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,26),_BpIfStatsLastDiscontinuityTime_Type())
bpIfStatsLastDiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsLastDiscontinuityTime.setStatus(_A)
class _BpIfStatsInCentRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BpIfStatsInCentRate_Type.__name__=_D
_BpIfStatsInCentRate_Object=MibTableColumn
bpIfStatsInCentRate=_BpIfStatsInCentRate_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,27),_BpIfStatsInCentRate_Type())
bpIfStatsInCentRate.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsInCentRate.setStatus(_A)
class _BpIfStatsOutCentRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BpIfStatsOutCentRate_Type.__name__=_D
_BpIfStatsOutCentRate_Object=MibTableColumn
bpIfStatsOutCentRate=_BpIfStatsOutCentRate_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,28),_BpIfStatsOutCentRate_Type())
bpIfStatsOutCentRate.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsOutCentRate.setStatus(_A)
_BpIfStatsLastChange_Type=TimeStamp
_BpIfStatsLastChange_Object=MibTableColumn
bpIfStatsLastChange=_BpIfStatsLastChange_Object((1,3,6,1,4,1,6027,3,24,2,1,2,1,29),_BpIfStatsLastChange_Type())
bpIfStatsLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIfStatsLastChange.setStatus(_A)
_BpPacketBufferTable_Object=MibTable
bpPacketBufferTable=_BpPacketBufferTable_Object((1,3,6,1,4,1,6027,3,24,2,1,3))
if mibBuilder.loadTexts:bpPacketBufferTable.setStatus(_A)
_BpPacketBufferEntry_Object=MibTableRow
bpPacketBufferEntry=_BpPacketBufferEntry_Object((1,3,6,1,4,1,6027,3,24,2,1,3,1))
bpPacketBufferEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:bpPacketBufferEntry.setStatus(_A)
class _BpPacketBufferStackUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_BpPacketBufferStackUnitIndex_Type.__name__=_D
_BpPacketBufferStackUnitIndex_Object=MibTableColumn
bpPacketBufferStackUnitIndex=_BpPacketBufferStackUnitIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,3,1,1),_BpPacketBufferStackUnitIndex_Type())
bpPacketBufferStackUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpPacketBufferStackUnitIndex.setStatus(_A)
class _BpPacketBufferPortPipe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_BpPacketBufferPortPipe_Type.__name__=_D
_BpPacketBufferPortPipe_Object=MibTableColumn
bpPacketBufferPortPipe=_BpPacketBufferPortPipe_Object((1,3,6,1,4,1,6027,3,24,2,1,3,1,2),_BpPacketBufferPortPipe_Type())
bpPacketBufferPortPipe.setMaxAccess(_E)
if mibBuilder.loadTexts:bpPacketBufferPortPipe.setStatus(_A)
_BpPacketBufferTotalPacketBuffer_Type=Counter32
_BpPacketBufferTotalPacketBuffer_Object=MibTableColumn
bpPacketBufferTotalPacketBuffer=_BpPacketBufferTotalPacketBuffer_Object((1,3,6,1,4,1,6027,3,24,2,1,3,1,3),_BpPacketBufferTotalPacketBuffer_Type())
bpPacketBufferTotalPacketBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:bpPacketBufferTotalPacketBuffer.setStatus(_A)
_BpPacketBufferCurrentAvailBuffer_Type=Counter32
_BpPacketBufferCurrentAvailBuffer_Object=MibTableColumn
bpPacketBufferCurrentAvailBuffer=_BpPacketBufferCurrentAvailBuffer_Object((1,3,6,1,4,1,6027,3,24,2,1,3,1,4),_BpPacketBufferCurrentAvailBuffer_Type())
bpPacketBufferCurrentAvailBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:bpPacketBufferCurrentAvailBuffer.setStatus(_A)
_BpPacketBufferPacketBufferAlloc_Type=Counter32
_BpPacketBufferPacketBufferAlloc_Object=MibTableColumn
bpPacketBufferPacketBufferAlloc=_BpPacketBufferPacketBufferAlloc_Object((1,3,6,1,4,1,6027,3,24,2,1,3,1,5),_BpPacketBufferPacketBufferAlloc_Type())
bpPacketBufferPacketBufferAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:bpPacketBufferPacketBufferAlloc.setStatus(_A)
_BpBufferStatsTable_Object=MibTable
bpBufferStatsTable=_BpBufferStatsTable_Object((1,3,6,1,4,1,6027,3,24,2,1,4))
if mibBuilder.loadTexts:bpBufferStatsTable.setStatus(_A)
_BpBufferStatsEntry_Object=MibTableRow
bpBufferStatsEntry=_BpBufferStatsEntry_Object((1,3,6,1,4,1,6027,3,24,2,1,4,1))
bpBufferStatsEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:bpBufferStatsEntry.setStatus(_A)
class _BpBufferStatsStackUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_BpBufferStatsStackUnitIndex_Type.__name__=_D
_BpBufferStatsStackUnitIndex_Object=MibTableColumn
bpBufferStatsStackUnitIndex=_BpBufferStatsStackUnitIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,4,1,1),_BpBufferStatsStackUnitIndex_Type())
bpBufferStatsStackUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpBufferStatsStackUnitIndex.setStatus(_A)
class _BpBufferStatsPortPipe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_BpBufferStatsPortPipe_Type.__name__=_D
_BpBufferStatsPortPipe_Object=MibTableColumn
bpBufferStatsPortPipe=_BpBufferStatsPortPipe_Object((1,3,6,1,4,1,6027,3,24,2,1,4,1,2),_BpBufferStatsPortPipe_Type())
bpBufferStatsPortPipe.setMaxAccess(_E)
if mibBuilder.loadTexts:bpBufferStatsPortPipe.setStatus(_A)
class _BpBufferStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_BpBufferStatsPortIndex_Type.__name__=_D
_BpBufferStatsPortIndex_Object=MibTableColumn
bpBufferStatsPortIndex=_BpBufferStatsPortIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,4,1,3),_BpBufferStatsPortIndex_Type())
bpBufferStatsPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpBufferStatsPortIndex.setStatus(_A)
_BpBufferStatsCurrentUsagePerPort_Type=Counter32
_BpBufferStatsCurrentUsagePerPort_Object=MibTableColumn
bpBufferStatsCurrentUsagePerPort=_BpBufferStatsCurrentUsagePerPort_Object((1,3,6,1,4,1,6027,3,24,2,1,4,1,4),_BpBufferStatsCurrentUsagePerPort_Type())
bpBufferStatsCurrentUsagePerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bpBufferStatsCurrentUsagePerPort.setStatus(_A)
_BpBufferStatsDefaultPacketBuffAlloc_Type=Counter32
_BpBufferStatsDefaultPacketBuffAlloc_Object=MibTableColumn
bpBufferStatsDefaultPacketBuffAlloc=_BpBufferStatsDefaultPacketBuffAlloc_Object((1,3,6,1,4,1,6027,3,24,2,1,4,1,5),_BpBufferStatsDefaultPacketBuffAlloc_Type())
bpBufferStatsDefaultPacketBuffAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:bpBufferStatsDefaultPacketBuffAlloc.setStatus(_A)
_BpBufferStatsMaxLimitPerPort_Type=Counter32
_BpBufferStatsMaxLimitPerPort_Object=MibTableColumn
bpBufferStatsMaxLimitPerPort=_BpBufferStatsMaxLimitPerPort_Object((1,3,6,1,4,1,6027,3,24,2,1,4,1,6),_BpBufferStatsMaxLimitPerPort_Type())
bpBufferStatsMaxLimitPerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bpBufferStatsMaxLimitPerPort.setStatus(_A)
_BpCosStatsTable_Object=MibTable
bpCosStatsTable=_BpCosStatsTable_Object((1,3,6,1,4,1,6027,3,24,2,1,5))
if mibBuilder.loadTexts:bpCosStatsTable.setStatus(_A)
_BpCosStatsEntry_Object=MibTableRow
bpCosStatsEntry=_BpCosStatsEntry_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1))
bpCosStatsEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:bpCosStatsEntry.setStatus(_A)
class _BpCosStatsStackUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_BpCosStatsStackUnitIndex_Type.__name__=_D
_BpCosStatsStackUnitIndex_Object=MibTableColumn
bpCosStatsStackUnitIndex=_BpCosStatsStackUnitIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,1),_BpCosStatsStackUnitIndex_Type())
bpCosStatsStackUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpCosStatsStackUnitIndex.setStatus(_A)
class _BpCosStatsPortPipe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_BpCosStatsPortPipe_Type.__name__=_D
_BpCosStatsPortPipe_Object=MibTableColumn
bpCosStatsPortPipe=_BpCosStatsPortPipe_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,2),_BpCosStatsPortPipe_Type())
bpCosStatsPortPipe.setMaxAccess(_E)
if mibBuilder.loadTexts:bpCosStatsPortPipe.setStatus(_A)
class _BpCosStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_BpCosStatsPortIndex_Type.__name__=_D
_BpCosStatsPortIndex_Object=MibTableColumn
bpCosStatsPortIndex=_BpCosStatsPortIndex_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,3),_BpCosStatsPortIndex_Type())
bpCosStatsPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bpCosStatsPortIndex.setStatus(_A)
class _BpCosStatsCOSNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21))
_BpCosStatsCOSNumber_Type.__name__=_D
_BpCosStatsCOSNumber_Object=MibTableColumn
bpCosStatsCOSNumber=_BpCosStatsCOSNumber_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,4),_BpCosStatsCOSNumber_Type())
bpCosStatsCOSNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:bpCosStatsCOSNumber.setStatus(_A)
_BpCosStatsCurrentUsage_Type=Counter32
_BpCosStatsCurrentUsage_Object=MibTableColumn
bpCosStatsCurrentUsage=_BpCosStatsCurrentUsage_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,5),_BpCosStatsCurrentUsage_Type())
bpCosStatsCurrentUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:bpCosStatsCurrentUsage.setStatus(_A)
_BpCosStatsDefaultPacketBuffAlloc_Type=Counter32
_BpCosStatsDefaultPacketBuffAlloc_Object=MibTableColumn
bpCosStatsDefaultPacketBuffAlloc=_BpCosStatsDefaultPacketBuffAlloc_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,6),_BpCosStatsDefaultPacketBuffAlloc_Type())
bpCosStatsDefaultPacketBuffAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:bpCosStatsDefaultPacketBuffAlloc.setStatus(_A)
_BpCosStatsMaxLimit_Type=Counter32
_BpCosStatsMaxLimit_Object=MibTableColumn
bpCosStatsMaxLimit=_BpCosStatsMaxLimit_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,7),_BpCosStatsMaxLimit_Type())
bpCosStatsMaxLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bpCosStatsMaxLimit.setStatus(_A)
_BpCosStatsHOLDDrops_Type=Counter64
_BpCosStatsHOLDDrops_Object=MibTableColumn
bpCosStatsHOLDDrops=_BpCosStatsHOLDDrops_Object((1,3,6,1,4,1,6027,3,24,2,1,5,1,8),_BpCosStatsHOLDDrops_Type())
bpCosStatsHOLDDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:bpCosStatsHOLDDrops.setStatus(_A)
_DellNetBpStatsAlarms_ObjectIdentity=ObjectIdentity
dellNetBpStatsAlarms=_DellNetBpStatsAlarms_ObjectIdentity((1,3,6,1,4,1,6027,3,24,3))
_BpLinkBundleNotifications_ObjectIdentity=ObjectIdentity
bpLinkBundleNotifications=_BpLinkBundleNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,24,3,1))
_BpLinkBundleAlarmVariable_ObjectIdentity=ObjectIdentity
bpLinkBundleAlarmVariable=_BpLinkBundleAlarmVariable_ObjectIdentity((1,3,6,1,4,1,6027,3,24,3,2))
class _BpLinkBundleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unknown',1),('bpHgBundle',2)))
_BpLinkBundleType_Type.__name__=_D
_BpLinkBundleType_Object=MibScalar
bpLinkBundleType=_BpLinkBundleType_Object((1,3,6,1,4,1,6027,3,24,3,2,1),_BpLinkBundleType_Type())
bpLinkBundleType.setMaxAccess(_F)
if mibBuilder.loadTexts:bpLinkBundleType.setStatus(_A)
_BpLinkBundleSlot_Type=Integer32
_BpLinkBundleSlot_Object=MibScalar
bpLinkBundleSlot=_BpLinkBundleSlot_Object((1,3,6,1,4,1,6027,3,24,3,2,2),_BpLinkBundleSlot_Type())
bpLinkBundleSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:bpLinkBundleSlot.setStatus(_A)
_BpLinkBundleNpuUnit_Type=Integer32
_BpLinkBundleNpuUnit_Object=MibScalar
bpLinkBundleNpuUnit=_BpLinkBundleNpuUnit_Object((1,3,6,1,4,1,6027,3,24,3,2,3),_BpLinkBundleNpuUnit_Type())
bpLinkBundleNpuUnit.setMaxAccess(_F)
if mibBuilder.loadTexts:bpLinkBundleNpuUnit.setStatus(_A)
_BpLinkBundleLocalId_Type=Integer32
_BpLinkBundleLocalId_Object=MibScalar
bpLinkBundleLocalId=_BpLinkBundleLocalId_Object((1,3,6,1,4,1,6027,3,24,3,2,4),_BpLinkBundleLocalId_Type())
bpLinkBundleLocalId.setMaxAccess(_F)
if mibBuilder.loadTexts:bpLinkBundleLocalId.setStatus(_A)
bpLinkBundleImbalance=NotificationType((1,3,6,1,4,1,6027,3,24,3,1,1))
bpLinkBundleImbalance.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:bpLinkBundleImbalance.setStatus(_A)
bpLinkBundleImbalanceClear=NotificationType((1,3,6,1,4,1,6027,3,24,3,1,2))
bpLinkBundleImbalanceClear.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:bpLinkBundleImbalanceClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'dellNetBpStatsMib':dellNetBpStatsMib,'dellNetBpStatsLinkBundleObjects':dellNetBpStatsLinkBundleObjects,'bpLinkBundleObjects':bpLinkBundleObjects,'bpLinkBundleRateInterval':bpLinkBundleRateInterval,'bpLinkBundleTriggerThreshold':bpLinkBundleTriggerThreshold,'dellNetBpStatsObjects':dellNetBpStatsObjects,'bpStatsObjects':bpStatsObjects,'bpDropsTable':bpDropsTable,'bpDropsEntry':bpDropsEntry,_L:bpDropsStackUnitIndex,_M:bpDropsPortPipe,_N:bpDropsPortIndex,'bpDropsInDrops':bpDropsInDrops,'bpDropsInUnKnownHgHdr':bpDropsInUnKnownHgHdr,'bpDropsInUnKnownHgOpcode':bpDropsInUnKnownHgOpcode,'bpDropsInMTUExceeds':bpDropsInMTUExceeds,'bpDropsInMacDrops':bpDropsInMacDrops,'bpDropsMMUHOLDrops':bpDropsMMUHOLDrops,'bpDropsEgMacDrops':bpDropsEgMacDrops,'bpDropsEgTxAgedCounter':bpDropsEgTxAgedCounter,'bpDropsEgTxErrCounter':bpDropsEgTxErrCounter,'bpDropsEgTxMACUnderflow':bpDropsEgTxMACUnderflow,'bpDropsEgTxErrPktCounter':bpDropsEgTxErrPktCounter,'bpIfStatsTable':bpIfStatsTable,'bpIfStatsEntry':bpIfStatsEntry,_O:bpIfStatsStackUnitIndex,_P:bpIfStatsPortPipe,_Q:bpIfStatsPortIndex,'bpIfStatsIn64BytePkts':bpIfStatsIn64BytePkts,'bpIfStatsIn65To127BytePkts':bpIfStatsIn65To127BytePkts,'bpIfStatsIn128To255BytePkts':bpIfStatsIn128To255BytePkts,'bpIfStatsIn256To511BytePkts':bpIfStatsIn256To511BytePkts,'bpIfStatsIn512To1023BytePkts':bpIfStatsIn512To1023BytePkts,'bpIfStatsInOver1023BytePkts':bpIfStatsInOver1023BytePkts,'bpIfStatsInThrottles':bpIfStatsInThrottles,'bpIfStatsInRunts':bpIfStatsInRunts,'bpIfStatsInGiants':bpIfStatsInGiants,'bpIfStatsInCRC':bpIfStatsInCRC,'bpIfStatsInOverruns':bpIfStatsInOverruns,'bpIfStatsOutUnderruns':bpIfStatsOutUnderruns,'bpIfStatsOutUnicasts':bpIfStatsOutUnicasts,'bpIfStatsOutCollisions':bpIfStatsOutCollisions,'bpIfStatsOutWredDrops':bpIfStatsOutWredDrops,'bpIfStatsOut64BytePkts':bpIfStatsOut64BytePkts,'bpIfStatsOut65To127BytePkts':bpIfStatsOut65To127BytePkts,'bpIfStatsOut128To255BytePkts':bpIfStatsOut128To255BytePkts,'bpIfStatsOut256To511BytePkts':bpIfStatsOut256To511BytePkts,'bpIfStatsOut512To1023BytePkts':bpIfStatsOut512To1023BytePkts,'bpIfStatsOutOver1023BytePkts':bpIfStatsOutOver1023BytePkts,'bpIfStatsOutThrottles':bpIfStatsOutThrottles,'bpIfStatsLastDiscontinuityTime':bpIfStatsLastDiscontinuityTime,'bpIfStatsInCentRate':bpIfStatsInCentRate,'bpIfStatsOutCentRate':bpIfStatsOutCentRate,'bpIfStatsLastChange':bpIfStatsLastChange,'bpPacketBufferTable':bpPacketBufferTable,'bpPacketBufferEntry':bpPacketBufferEntry,_R:bpPacketBufferStackUnitIndex,_S:bpPacketBufferPortPipe,'bpPacketBufferTotalPacketBuffer':bpPacketBufferTotalPacketBuffer,'bpPacketBufferCurrentAvailBuffer':bpPacketBufferCurrentAvailBuffer,'bpPacketBufferPacketBufferAlloc':bpPacketBufferPacketBufferAlloc,'bpBufferStatsTable':bpBufferStatsTable,'bpBufferStatsEntry':bpBufferStatsEntry,_T:bpBufferStatsStackUnitIndex,_U:bpBufferStatsPortPipe,_V:bpBufferStatsPortIndex,'bpBufferStatsCurrentUsagePerPort':bpBufferStatsCurrentUsagePerPort,'bpBufferStatsDefaultPacketBuffAlloc':bpBufferStatsDefaultPacketBuffAlloc,'bpBufferStatsMaxLimitPerPort':bpBufferStatsMaxLimitPerPort,'bpCosStatsTable':bpCosStatsTable,'bpCosStatsEntry':bpCosStatsEntry,_W:bpCosStatsStackUnitIndex,_X:bpCosStatsPortPipe,_Y:bpCosStatsPortIndex,_Z:bpCosStatsCOSNumber,'bpCosStatsCurrentUsage':bpCosStatsCurrentUsage,'bpCosStatsDefaultPacketBuffAlloc':bpCosStatsDefaultPacketBuffAlloc,'bpCosStatsMaxLimit':bpCosStatsMaxLimit,'bpCosStatsHOLDDrops':bpCosStatsHOLDDrops,'dellNetBpStatsAlarms':dellNetBpStatsAlarms,'bpLinkBundleNotifications':bpLinkBundleNotifications,'bpLinkBundleImbalance':bpLinkBundleImbalance,'bpLinkBundleImbalanceClear':bpLinkBundleImbalanceClear,'bpLinkBundleAlarmVariable':bpLinkBundleAlarmVariable,_G:bpLinkBundleType,_H:bpLinkBundleSlot,_I:bpLinkBundleNpuUnit,_J:bpLinkBundleLocalId})