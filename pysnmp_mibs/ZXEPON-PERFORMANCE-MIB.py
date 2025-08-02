_V='zxAnEponIfXOltHistoryEntry'
_U='zxAnEponIfXHistoryEntry'
_T='zxAnEponIfXCurrentEntry'
_S='zxAnEponIfXOltEntry'
_R='zxAnEponIfXEntry'
_Q='read-create'
_P='zxAnEponDot3QueueIndexCurrent'
_O='read-write'
_N='unknown'
_M='octets'
_L='zxAnEponOnuLlid'
_K='ZXANEPON-ONUMGMT-MIB'
_J='Integer32'
_I='deprecated'
_H='Unsigned32'
_G='ZXEPON-PERFORMANCE-MIB'
_F='OctetString'
_E='ifIndex'
_D='IF-MIB'
_C='frames'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
EntryStatus,OwnerString=mibBuilder.importSymbols('RMON-MIB','EntryStatus','OwnerString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxAnEponMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnEponMib')
zxAnEponOnuLlid,=mibBuilder.importSymbols(_K,_L)
zxAnEponPm=ModuleIdentity((1,3,6,1,4,1,3902,1015,1010,1,9))
_ZxAnEponPmInfor_ObjectIdentity=ObjectIdentity
zxAnEponPmInfor=_ZxAnEponPmInfor_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,9,1))
_ZxAnEponOltVirtualIfBERStatisticTable_Object=MibTable
zxAnEponOltVirtualIfBERStatisticTable=_ZxAnEponOltVirtualIfBERStatisticTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,1))
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticTable.setStatus(_A)
_ZxAnEponOltVirtualIfBERStatisticEntry_Object=MibTableRow
zxAnEponOltVirtualIfBERStatisticEntry=_ZxAnEponOltVirtualIfBERStatisticEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,1,1))
zxAnEponOltVirtualIfBERStatisticEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticEntry.setStatus(_A)
class _ZxAnEponOltVirtualIfBERStatisticOnuBER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltVirtualIfBERStatisticOnuBER_Type.__name__=_F
_ZxAnEponOltVirtualIfBERStatisticOnuBER_Object=MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuBER=_ZxAnEponOltVirtualIfBERStatisticOnuBER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,1,1,1),_ZxAnEponOltVirtualIfBERStatisticOnuBER_Type())
zxAnEponOltVirtualIfBERStatisticOnuBER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticOnuBER.setStatus(_A)
class _ZxAnEponOltVirtualIfBERStatisticOnuFER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltVirtualIfBERStatisticOnuFER_Type.__name__=_F
_ZxAnEponOltVirtualIfBERStatisticOnuFER_Object=MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuFER=_ZxAnEponOltVirtualIfBERStatisticOnuFER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,1,1,2),_ZxAnEponOltVirtualIfBERStatisticOnuFER_Type())
zxAnEponOltVirtualIfBERStatisticOnuFER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticOnuFER.setStatus(_A)
_ZxAnEponOltPhyPortStatisticTable_Object=MibTable
zxAnEponOltPhyPortStatisticTable=_ZxAnEponOltPhyPortStatisticTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,2))
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticTable.setStatus(_A)
_ZxAnEponOltPhyPortStatisticEntry_Object=MibTableRow
zxAnEponOltPhyPortStatisticEntry=_ZxAnEponOltPhyPortStatisticEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,2,1))
zxAnEponOltPhyPortStatisticEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticEntry.setStatus(_A)
class _ZxAnEponOltPhyPortStatisticOltPonAverageBER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltPhyPortStatisticOltPonAverageBER_Type.__name__=_F
_ZxAnEponOltPhyPortStatisticOltPonAverageBER_Object=MibTableColumn
zxAnEponOltPhyPortStatisticOltPonAverageBER=_ZxAnEponOltPhyPortStatisticOltPonAverageBER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,2,1,1),_ZxAnEponOltPhyPortStatisticOltPonAverageBER_Type())
zxAnEponOltPhyPortStatisticOltPonAverageBER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticOltPonAverageBER.setStatus(_A)
class _ZxAnEponOltPhyPortStatisticOltSysAverageBER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltPhyPortStatisticOltSysAverageBER_Type.__name__=_F
_ZxAnEponOltPhyPortStatisticOltSysAverageBER_Object=MibTableColumn
zxAnEponOltPhyPortStatisticOltSysAverageBER=_ZxAnEponOltPhyPortStatisticOltSysAverageBER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,2,1,2),_ZxAnEponOltPhyPortStatisticOltSysAverageBER_Type())
zxAnEponOltPhyPortStatisticOltSysAverageBER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticOltSysAverageBER.setStatus(_A)
_ZxAnEponEtherStatsTable_Object=MibTable
zxAnEponEtherStatsTable=_ZxAnEponEtherStatsTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3))
if mibBuilder.loadTexts:zxAnEponEtherStatsTable.setStatus(_A)
_ZxAnEponEtherStatsEntry_Object=MibTableRow
zxAnEponEtherStatsEntry=_ZxAnEponEtherStatsEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1))
zxAnEponEtherStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponEtherStatsEntry.setStatus(_A)
_ZxAnEponEtherStatsDropEvents_Type=Counter32
_ZxAnEponEtherStatsDropEvents_Object=MibTableColumn
zxAnEponEtherStatsDropEvents=_ZxAnEponEtherStatsDropEvents_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,1),_ZxAnEponEtherStatsDropEvents_Type())
zxAnEponEtherStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsDropEvents.setStatus(_A)
_ZxAnEponEtherStatsOctets_Type=Counter32
_ZxAnEponEtherStatsOctets_Object=MibTableColumn
zxAnEponEtherStatsOctets=_ZxAnEponEtherStatsOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,2),_ZxAnEponEtherStatsOctets_Type())
zxAnEponEtherStatsOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsOctets.setStatus(_A)
_ZxAnEponEtherStatsPkts_Type=Counter32
_ZxAnEponEtherStatsPkts_Object=MibTableColumn
zxAnEponEtherStatsPkts=_ZxAnEponEtherStatsPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,3),_ZxAnEponEtherStatsPkts_Type())
zxAnEponEtherStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts.setStatus(_A)
_ZxAnEponEtherStatsBroadcastPkts_Type=Counter32
_ZxAnEponEtherStatsBroadcastPkts_Object=MibTableColumn
zxAnEponEtherStatsBroadcastPkts=_ZxAnEponEtherStatsBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,4),_ZxAnEponEtherStatsBroadcastPkts_Type())
zxAnEponEtherStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsBroadcastPkts.setStatus(_A)
_ZxAnEponEtherStatsMulticastPkts_Type=Counter32
_ZxAnEponEtherStatsMulticastPkts_Object=MibTableColumn
zxAnEponEtherStatsMulticastPkts=_ZxAnEponEtherStatsMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,5),_ZxAnEponEtherStatsMulticastPkts_Type())
zxAnEponEtherStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsMulticastPkts.setStatus(_A)
_ZxAnEponEtherStatsCRCAlignErrors_Type=Counter32
_ZxAnEponEtherStatsCRCAlignErrors_Object=MibTableColumn
zxAnEponEtherStatsCRCAlignErrors=_ZxAnEponEtherStatsCRCAlignErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,6),_ZxAnEponEtherStatsCRCAlignErrors_Type())
zxAnEponEtherStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsCRCAlignErrors.setStatus(_A)
_ZxAnEponEtherStatsUndersizePkts_Type=Counter32
_ZxAnEponEtherStatsUndersizePkts_Object=MibTableColumn
zxAnEponEtherStatsUndersizePkts=_ZxAnEponEtherStatsUndersizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,7),_ZxAnEponEtherStatsUndersizePkts_Type())
zxAnEponEtherStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsUndersizePkts.setStatus(_A)
_ZxAnEponEtherStatsOversizePkts_Type=Counter32
_ZxAnEponEtherStatsOversizePkts_Object=MibTableColumn
zxAnEponEtherStatsOversizePkts=_ZxAnEponEtherStatsOversizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,8),_ZxAnEponEtherStatsOversizePkts_Type())
zxAnEponEtherStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsOversizePkts.setStatus(_A)
_ZxAnEponEtherStatsFragments_Type=Counter32
_ZxAnEponEtherStatsFragments_Object=MibTableColumn
zxAnEponEtherStatsFragments=_ZxAnEponEtherStatsFragments_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,9),_ZxAnEponEtherStatsFragments_Type())
zxAnEponEtherStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsFragments.setStatus(_A)
_ZxAnEponEtherStatsJabbers_Type=Counter32
_ZxAnEponEtherStatsJabbers_Object=MibTableColumn
zxAnEponEtherStatsJabbers=_ZxAnEponEtherStatsJabbers_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,10),_ZxAnEponEtherStatsJabbers_Type())
zxAnEponEtherStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsJabbers.setStatus(_A)
_ZxAnEponEtherStatsCollisions_Type=Counter32
_ZxAnEponEtherStatsCollisions_Object=MibTableColumn
zxAnEponEtherStatsCollisions=_ZxAnEponEtherStatsCollisions_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,11),_ZxAnEponEtherStatsCollisions_Type())
zxAnEponEtherStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsCollisions.setStatus(_A)
_ZxAnEponEtherStatsPkts64Octets_Type=Counter32
_ZxAnEponEtherStatsPkts64Octets_Object=MibTableColumn
zxAnEponEtherStatsPkts64Octets=_ZxAnEponEtherStatsPkts64Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,12),_ZxAnEponEtherStatsPkts64Octets_Type())
zxAnEponEtherStatsPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts64Octets.setStatus(_A)
_ZxAnEponEtherStatsPkts65to127Octets_Type=Counter32
_ZxAnEponEtherStatsPkts65to127Octets_Object=MibTableColumn
zxAnEponEtherStatsPkts65to127Octets=_ZxAnEponEtherStatsPkts65to127Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,13),_ZxAnEponEtherStatsPkts65to127Octets_Type())
zxAnEponEtherStatsPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts65to127Octets.setStatus(_A)
_ZxAnEponEtherStatsPkts128to255Octets_Type=Counter32
_ZxAnEponEtherStatsPkts128to255Octets_Object=MibTableColumn
zxAnEponEtherStatsPkts128to255Octets=_ZxAnEponEtherStatsPkts128to255Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,14),_ZxAnEponEtherStatsPkts128to255Octets_Type())
zxAnEponEtherStatsPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts128to255Octets.setStatus(_A)
_ZxAnEponEtherStatsPkts256to511Octets_Type=Counter32
_ZxAnEponEtherStatsPkts256to511Octets_Object=MibTableColumn
zxAnEponEtherStatsPkts256to511Octets=_ZxAnEponEtherStatsPkts256to511Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,15),_ZxAnEponEtherStatsPkts256to511Octets_Type())
zxAnEponEtherStatsPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts256to511Octets.setStatus(_A)
_ZxAnEponEtherStatsPkts512to1023Octets_Type=Counter32
_ZxAnEponEtherStatsPkts512to1023Octets_Object=MibTableColumn
zxAnEponEtherStatsPkts512to1023Octets=_ZxAnEponEtherStatsPkts512to1023Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,16),_ZxAnEponEtherStatsPkts512to1023Octets_Type())
zxAnEponEtherStatsPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts512to1023Octets.setStatus(_A)
_ZxAnEponEtherStatsPkts1024to1518Octets_Type=Counter32
_ZxAnEponEtherStatsPkts1024to1518Octets_Object=MibTableColumn
zxAnEponEtherStatsPkts1024to1518Octets=_ZxAnEponEtherStatsPkts1024to1518Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,3,1,17),_ZxAnEponEtherStatsPkts1024to1518Octets_Type())
zxAnEponEtherStatsPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts1024to1518Octets.setStatus(_A)
_ZxAnEponIfTable_Object=MibTable
zxAnEponIfTable=_ZxAnEponIfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4))
if mibBuilder.loadTexts:zxAnEponIfTable.setStatus(_A)
_ZxAnEponIfEntry_Object=MibTableRow
zxAnEponIfEntry=_ZxAnEponIfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1))
zxAnEponIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponIfEntry.setStatus(_A)
_ZxAnEponIfInOctets_Type=Counter32
_ZxAnEponIfInOctets_Object=MibTableColumn
zxAnEponIfInOctets=_ZxAnEponIfInOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,1),_ZxAnEponIfInOctets_Type())
zxAnEponIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInOctets.setStatus(_A)
_ZxAnEponIfInUcastPkts_Type=Counter32
_ZxAnEponIfInUcastPkts_Object=MibTableColumn
zxAnEponIfInUcastPkts=_ZxAnEponIfInUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,2),_ZxAnEponIfInUcastPkts_Type())
zxAnEponIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInUcastPkts.setStatus(_A)
_ZxAnEponIfInNUcastPkts_Type=Counter32
_ZxAnEponIfInNUcastPkts_Object=MibTableColumn
zxAnEponIfInNUcastPkts=_ZxAnEponIfInNUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,3),_ZxAnEponIfInNUcastPkts_Type())
zxAnEponIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInNUcastPkts.setStatus(_I)
_ZxAnEponIfInDiscards_Type=Counter32
_ZxAnEponIfInDiscards_Object=MibTableColumn
zxAnEponIfInDiscards=_ZxAnEponIfInDiscards_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,4),_ZxAnEponIfInDiscards_Type())
zxAnEponIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInDiscards.setStatus(_A)
_ZxAnEponIfInErrors_Type=Counter32
_ZxAnEponIfInErrors_Object=MibTableColumn
zxAnEponIfInErrors=_ZxAnEponIfInErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,5),_ZxAnEponIfInErrors_Type())
zxAnEponIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInErrors.setStatus(_A)
_ZxAnEponIfInUnknownProtos_Type=Counter32
_ZxAnEponIfInUnknownProtos_Object=MibTableColumn
zxAnEponIfInUnknownProtos=_ZxAnEponIfInUnknownProtos_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,6),_ZxAnEponIfInUnknownProtos_Type())
zxAnEponIfInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInUnknownProtos.setStatus(_A)
_ZxAnEponIfOutOctets_Type=Counter32
_ZxAnEponIfOutOctets_Object=MibTableColumn
zxAnEponIfOutOctets=_ZxAnEponIfOutOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,7),_ZxAnEponIfOutOctets_Type())
zxAnEponIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutOctets.setStatus(_A)
_ZxAnEponIfOutUcastPkts_Type=Counter32
_ZxAnEponIfOutUcastPkts_Object=MibTableColumn
zxAnEponIfOutUcastPkts=_ZxAnEponIfOutUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,8),_ZxAnEponIfOutUcastPkts_Type())
zxAnEponIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutUcastPkts.setStatus(_A)
_ZxAnEponIfOutNUcastPkts_Type=Counter32
_ZxAnEponIfOutNUcastPkts_Object=MibTableColumn
zxAnEponIfOutNUcastPkts=_ZxAnEponIfOutNUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,9),_ZxAnEponIfOutNUcastPkts_Type())
zxAnEponIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutNUcastPkts.setStatus(_I)
_ZxAnEponIfOutDiscards_Type=Counter32
_ZxAnEponIfOutDiscards_Object=MibTableColumn
zxAnEponIfOutDiscards=_ZxAnEponIfOutDiscards_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,10),_ZxAnEponIfOutDiscards_Type())
zxAnEponIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutDiscards.setStatus(_A)
_ZxAnEponIfOutErrors_Type=Counter32
_ZxAnEponIfOutErrors_Object=MibTableColumn
zxAnEponIfOutErrors=_ZxAnEponIfOutErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,4,1,11),_ZxAnEponIfOutErrors_Type())
zxAnEponIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutErrors.setStatus(_A)
_ZxAnEponIfXTable_Object=MibTable
zxAnEponIfXTable=_ZxAnEponIfXTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5))
if mibBuilder.loadTexts:zxAnEponIfXTable.setStatus(_A)
_ZxAnEponIfXEntry_Object=MibTableRow
zxAnEponIfXEntry=_ZxAnEponIfXEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1))
if mibBuilder.loadTexts:zxAnEponIfXEntry.setStatus(_A)
_ZxAnEponIfInMulticastPkts_Type=Counter32
_ZxAnEponIfInMulticastPkts_Object=MibTableColumn
zxAnEponIfInMulticastPkts=_ZxAnEponIfInMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,1),_ZxAnEponIfInMulticastPkts_Type())
zxAnEponIfInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInMulticastPkts.setStatus(_A)
_ZxAnEponIfInBroadcastPkts_Type=Counter32
_ZxAnEponIfInBroadcastPkts_Object=MibTableColumn
zxAnEponIfInBroadcastPkts=_ZxAnEponIfInBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,2),_ZxAnEponIfInBroadcastPkts_Type())
zxAnEponIfInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInBroadcastPkts.setStatus(_A)
_ZxAnEponIfOutMulticastPkts_Type=Counter32
_ZxAnEponIfOutMulticastPkts_Object=MibTableColumn
zxAnEponIfOutMulticastPkts=_ZxAnEponIfOutMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,3),_ZxAnEponIfOutMulticastPkts_Type())
zxAnEponIfOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutMulticastPkts.setStatus(_A)
_ZxAnEponIfOutBroadcastPkts_Type=Counter32
_ZxAnEponIfOutBroadcastPkts_Object=MibTableColumn
zxAnEponIfOutBroadcastPkts=_ZxAnEponIfOutBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,4),_ZxAnEponIfOutBroadcastPkts_Type())
zxAnEponIfOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutBroadcastPkts.setStatus(_A)
_ZxAnEponIfHCInOctets_Type=Counter64
_ZxAnEponIfHCInOctets_Object=MibTableColumn
zxAnEponIfHCInOctets=_ZxAnEponIfHCInOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,5),_ZxAnEponIfHCInOctets_Type())
zxAnEponIfHCInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInOctets.setStatus(_A)
_ZxAnEponIfHCInUcastPkts_Type=Counter64
_ZxAnEponIfHCInUcastPkts_Object=MibTableColumn
zxAnEponIfHCInUcastPkts=_ZxAnEponIfHCInUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,6),_ZxAnEponIfHCInUcastPkts_Type())
zxAnEponIfHCInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInUcastPkts.setStatus(_A)
_ZxAnEponIfHCInMulticastPkts_Type=Counter64
_ZxAnEponIfHCInMulticastPkts_Object=MibTableColumn
zxAnEponIfHCInMulticastPkts=_ZxAnEponIfHCInMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,7),_ZxAnEponIfHCInMulticastPkts_Type())
zxAnEponIfHCInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInMulticastPkts.setStatus(_A)
_ZxAnEponIfHCInBroadcastPkts_Type=Counter64
_ZxAnEponIfHCInBroadcastPkts_Object=MibTableColumn
zxAnEponIfHCInBroadcastPkts=_ZxAnEponIfHCInBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,8),_ZxAnEponIfHCInBroadcastPkts_Type())
zxAnEponIfHCInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInBroadcastPkts.setStatus(_A)
_ZxAnEponIfHCOutOctets_Type=Counter64
_ZxAnEponIfHCOutOctets_Object=MibTableColumn
zxAnEponIfHCOutOctets=_ZxAnEponIfHCOutOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,9),_ZxAnEponIfHCOutOctets_Type())
zxAnEponIfHCOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutOctets.setStatus(_A)
_ZxAnEponIfHCOutUcastPkts_Type=Counter64
_ZxAnEponIfHCOutUcastPkts_Object=MibTableColumn
zxAnEponIfHCOutUcastPkts=_ZxAnEponIfHCOutUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,10),_ZxAnEponIfHCOutUcastPkts_Type())
zxAnEponIfHCOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutUcastPkts.setStatus(_A)
_ZxAnEponIfHCOutMulticastPkts_Type=Counter64
_ZxAnEponIfHCOutMulticastPkts_Object=MibTableColumn
zxAnEponIfHCOutMulticastPkts=_ZxAnEponIfHCOutMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,11),_ZxAnEponIfHCOutMulticastPkts_Type())
zxAnEponIfHCOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutMulticastPkts.setStatus(_A)
_ZxAnEponIfHCOutBroadcastPkts_Type=Counter64
_ZxAnEponIfHCOutBroadcastPkts_Object=MibTableColumn
zxAnEponIfHCOutBroadcastPkts=_ZxAnEponIfHCOutBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,5,1,12),_ZxAnEponIfHCOutBroadcastPkts_Type())
zxAnEponIfHCOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutBroadcastPkts.setStatus(_A)
_ZxAnEponDot3PauseTable_Object=MibTable
zxAnEponDot3PauseTable=_ZxAnEponDot3PauseTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,6))
if mibBuilder.loadTexts:zxAnEponDot3PauseTable.setStatus(_A)
_ZxAnEponDot3PauseEntry_Object=MibTableRow
zxAnEponDot3PauseEntry=_ZxAnEponDot3PauseEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,6,1))
zxAnEponDot3PauseEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3PauseEntry.setStatus(_A)
_ZxAnEponDot3InPauseFrames_Type=Counter32
_ZxAnEponDot3InPauseFrames_Object=MibTableColumn
zxAnEponDot3InPauseFrames=_ZxAnEponDot3InPauseFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,6,1,1),_ZxAnEponDot3InPauseFrames_Type())
zxAnEponDot3InPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3InPauseFrames.setStatus(_A)
_ZxAnEponDot3OutPauseFrames_Type=Counter32
_ZxAnEponDot3OutPauseFrames_Object=MibTableColumn
zxAnEponDot3OutPauseFrames=_ZxAnEponDot3OutPauseFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,6,1,2),_ZxAnEponDot3OutPauseFrames_Type())
zxAnEponDot3OutPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OutPauseFrames.setStatus(_A)
_ZxAnEponDot3HCInPauseFrames_Type=Counter64
_ZxAnEponDot3HCInPauseFrames_Object=MibTableColumn
zxAnEponDot3HCInPauseFrames=_ZxAnEponDot3HCInPauseFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,6,1,3),_ZxAnEponDot3HCInPauseFrames_Type())
zxAnEponDot3HCInPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCInPauseFrames.setStatus(_A)
_ZxAnEponDot3HCOutPauseFrames_Type=Counter64
_ZxAnEponDot3HCOutPauseFrames_Object=MibTableColumn
zxAnEponDot3HCOutPauseFrames=_ZxAnEponDot3HCOutPauseFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,6,1,4),_ZxAnEponDot3HCOutPauseFrames_Type())
zxAnEponDot3HCOutPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCOutPauseFrames.setStatus(_A)
_ZxAnEponDot3HCStatsTable_Object=MibTable
zxAnEponDot3HCStatsTable=_ZxAnEponDot3HCStatsTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7))
if mibBuilder.loadTexts:zxAnEponDot3HCStatsTable.setStatus(_A)
_ZxAnEponDot3HCStatsEntry_Object=MibTableRow
zxAnEponDot3HCStatsEntry=_ZxAnEponDot3HCStatsEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7,1))
zxAnEponDot3HCStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3HCStatsEntry.setStatus(_A)
_ZxAnEponDot3HCStatsAlignmentErrors_Type=Counter64
_ZxAnEponDot3HCStatsAlignmentErrors_Object=MibTableColumn
zxAnEponDot3HCStatsAlignmentErrors=_ZxAnEponDot3HCStatsAlignmentErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7,1,1),_ZxAnEponDot3HCStatsAlignmentErrors_Type())
zxAnEponDot3HCStatsAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsAlignmentErrors.setStatus(_A)
_ZxAnEponDot3HCStatsFCSErrors_Type=Counter64
_ZxAnEponDot3HCStatsFCSErrors_Object=MibTableColumn
zxAnEponDot3HCStatsFCSErrors=_ZxAnEponDot3HCStatsFCSErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7,1,2),_ZxAnEponDot3HCStatsFCSErrors_Type())
zxAnEponDot3HCStatsFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsFCSErrors.setStatus(_A)
_ZxAnEponDot3HCStatsInternalMacTransmitErrors_Type=Counter64
_ZxAnEponDot3HCStatsInternalMacTransmitErrors_Object=MibTableColumn
zxAnEponDot3HCStatsInternalMacTransmitErrors=_ZxAnEponDot3HCStatsInternalMacTransmitErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7,1,3),_ZxAnEponDot3HCStatsInternalMacTransmitErrors_Type())
zxAnEponDot3HCStatsInternalMacTransmitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsInternalMacTransmitErrors.setStatus(_A)
_ZxAnEponDot3HCStatsFrameTooLongs_Type=Counter64
_ZxAnEponDot3HCStatsFrameTooLongs_Object=MibTableColumn
zxAnEponDot3HCStatsFrameTooLongs=_ZxAnEponDot3HCStatsFrameTooLongs_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7,1,4),_ZxAnEponDot3HCStatsFrameTooLongs_Type())
zxAnEponDot3HCStatsFrameTooLongs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsFrameTooLongs.setStatus(_A)
_ZxAnEponDot3HCStatsInternalMacReceiveErrors_Type=Counter64
_ZxAnEponDot3HCStatsInternalMacReceiveErrors_Object=MibTableColumn
zxAnEponDot3HCStatsInternalMacReceiveErrors=_ZxAnEponDot3HCStatsInternalMacReceiveErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7,1,5),_ZxAnEponDot3HCStatsInternalMacReceiveErrors_Type())
zxAnEponDot3HCStatsInternalMacReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsInternalMacReceiveErrors.setStatus(_A)
_ZxAnEponDot3HCStatsSymbolErrors_Type=Counter64
_ZxAnEponDot3HCStatsSymbolErrors_Object=MibTableColumn
zxAnEponDot3HCStatsSymbolErrors=_ZxAnEponDot3HCStatsSymbolErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,7,1,6),_ZxAnEponDot3HCStatsSymbolErrors_Type())
zxAnEponDot3HCStatsSymbolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsSymbolErrors.setStatus(_A)
_ZxAnEponIfXOltTable_Object=MibTable
zxAnEponIfXOltTable=_ZxAnEponIfXOltTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8))
if mibBuilder.loadTexts:zxAnEponIfXOltTable.setStatus(_A)
_ZxAnEponIfXOltEntry_Object=MibTableRow
zxAnEponIfXOltEntry=_ZxAnEponIfXOltEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1))
if mibBuilder.loadTexts:zxAnEponIfXOltEntry.setStatus(_A)
_ZxAnEponIfOltInMulticastPkts_Type=Counter32
_ZxAnEponIfOltInMulticastPkts_Object=MibTableColumn
zxAnEponIfOltInMulticastPkts=_ZxAnEponIfOltInMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,1),_ZxAnEponIfOltInMulticastPkts_Type())
zxAnEponIfOltInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltInMulticastPkts.setStatus(_A)
_ZxAnEponIfOltInBroadcastPkts_Type=Counter32
_ZxAnEponIfOltInBroadcastPkts_Object=MibTableColumn
zxAnEponIfOltInBroadcastPkts=_ZxAnEponIfOltInBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,2),_ZxAnEponIfOltInBroadcastPkts_Type())
zxAnEponIfOltInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltInBroadcastPkts.setStatus(_A)
_ZxAnEponIfOltOutMulticastPkts_Type=Counter32
_ZxAnEponIfOltOutMulticastPkts_Object=MibTableColumn
zxAnEponIfOltOutMulticastPkts=_ZxAnEponIfOltOutMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,3),_ZxAnEponIfOltOutMulticastPkts_Type())
zxAnEponIfOltOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltOutMulticastPkts.setStatus(_A)
_ZxAnEponIfOltOutBroadcastPkts_Type=Counter32
_ZxAnEponIfOltOutBroadcastPkts_Object=MibTableColumn
zxAnEponIfOltOutBroadcastPkts=_ZxAnEponIfOltOutBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,4),_ZxAnEponIfOltOutBroadcastPkts_Type())
zxAnEponIfOltOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltOutBroadcastPkts.setStatus(_A)
_ZxAnEponIfOltHCInOctets_Type=Counter64
_ZxAnEponIfOltHCInOctets_Object=MibTableColumn
zxAnEponIfOltHCInOctets=_ZxAnEponIfOltHCInOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,5),_ZxAnEponIfOltHCInOctets_Type())
zxAnEponIfOltHCInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInOctets.setStatus(_A)
_ZxAnEponIfOltHCInUcastPkts_Type=Counter64
_ZxAnEponIfOltHCInUcastPkts_Object=MibTableColumn
zxAnEponIfOltHCInUcastPkts=_ZxAnEponIfOltHCInUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,6),_ZxAnEponIfOltHCInUcastPkts_Type())
zxAnEponIfOltHCInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInUcastPkts.setStatus(_A)
_ZxAnEponIfOltHCInMulticastPkts_Type=Counter64
_ZxAnEponIfOltHCInMulticastPkts_Object=MibTableColumn
zxAnEponIfOltHCInMulticastPkts=_ZxAnEponIfOltHCInMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,7),_ZxAnEponIfOltHCInMulticastPkts_Type())
zxAnEponIfOltHCInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInMulticastPkts.setStatus(_A)
_ZxAnEponIfOltHCInBroadcastPkts_Type=Counter64
_ZxAnEponIfOltHCInBroadcastPkts_Object=MibTableColumn
zxAnEponIfOltHCInBroadcastPkts=_ZxAnEponIfOltHCInBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,8),_ZxAnEponIfOltHCInBroadcastPkts_Type())
zxAnEponIfOltHCInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInBroadcastPkts.setStatus(_A)
_ZxAnEponIfOltHCOutOctets_Type=Counter64
_ZxAnEponIfOltHCOutOctets_Object=MibTableColumn
zxAnEponIfOltHCOutOctets=_ZxAnEponIfOltHCOutOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,9),_ZxAnEponIfOltHCOutOctets_Type())
zxAnEponIfOltHCOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutOctets.setStatus(_A)
_ZxAnEponIfOltHCOutUcastPkts_Type=Counter64
_ZxAnEponIfOltHCOutUcastPkts_Object=MibTableColumn
zxAnEponIfOltHCOutUcastPkts=_ZxAnEponIfOltHCOutUcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,10),_ZxAnEponIfOltHCOutUcastPkts_Type())
zxAnEponIfOltHCOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutUcastPkts.setStatus(_A)
_ZxAnEponIfOltHCOutMulticastPkts_Type=Counter64
_ZxAnEponIfOltHCOutMulticastPkts_Object=MibTableColumn
zxAnEponIfOltHCOutMulticastPkts=_ZxAnEponIfOltHCOutMulticastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,11),_ZxAnEponIfOltHCOutMulticastPkts_Type())
zxAnEponIfOltHCOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutMulticastPkts.setStatus(_A)
_ZxAnEponIfOltHCOutBroadcastPkts_Type=Counter64
_ZxAnEponIfOltHCOutBroadcastPkts_Object=MibTableColumn
zxAnEponIfOltHCOutBroadcastPkts=_ZxAnEponIfOltHCOutBroadcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,9,1,8,1,12),_ZxAnEponIfOltHCOutBroadcastPkts_Type())
zxAnEponIfOltHCOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutBroadcastPkts.setStatus(_A)
_ZxAnEponPmCurrent_ObjectIdentity=ObjectIdentity
zxAnEponPmCurrent=_ZxAnEponPmCurrent_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,9,2))
_ZxAnEponDot3MpcpStatCurrentTable_Object=MibTable
zxAnEponDot3MpcpStatCurrentTable=_ZxAnEponDot3MpcpStatCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1))
if mibBuilder.loadTexts:zxAnEponDot3MpcpStatCurrentTable.setStatus(_A)
_ZxAnEponDot3MpcpStatCurrentEntry_Object=MibTableRow
zxAnEponDot3MpcpStatCurrentEntry=_ZxAnEponDot3MpcpStatCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1))
zxAnEponDot3MpcpStatCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3MpcpStatCurrentEntry.setStatus(_A)
_ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Type=Counter64
_ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Object=MibTableColumn
zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent=_ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,1),_ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Type())
zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent.setUnits(_C)
_ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Type=Counter64
_ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Object=MibTableColumn
zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent=_ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,2),_ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Type())
zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent.setUnits(_C)
_ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Type=Counter32
_ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Object=MibTableColumn
zxAnEponDot3MpcpDiscoveryWindowsSentCurrent=_ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,3),_ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Type())
zxAnEponDot3MpcpDiscoveryWindowsSentCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpDiscoveryWindowsSentCurrent.setStatus(_A)
_ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Type=Counter32
_ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Object=MibTableColumn
zxAnEponDot3MpcpDiscoveryTimeoutCurrent=_ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,4),_ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Type())
zxAnEponDot3MpcpDiscoveryTimeoutCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpDiscoveryTimeoutCurrent.setStatus(_A)
_ZxAnEponDot3MpcpTxRegRequestCurrent_Type=Counter64
_ZxAnEponDot3MpcpTxRegRequestCurrent_Object=MibTableColumn
zxAnEponDot3MpcpTxRegRequestCurrent=_ZxAnEponDot3MpcpTxRegRequestCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,5),_ZxAnEponDot3MpcpTxRegRequestCurrent_Type())
zxAnEponDot3MpcpTxRegRequestCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxRegRequestCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxRegRequestCurrent.setUnits(_C)
_ZxAnEponDot3MpcpRxRegRequestCurrent_Type=Counter64
_ZxAnEponDot3MpcpRxRegRequestCurrent_Object=MibTableColumn
zxAnEponDot3MpcpRxRegRequestCurrent=_ZxAnEponDot3MpcpRxRegRequestCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,6),_ZxAnEponDot3MpcpRxRegRequestCurrent_Type())
zxAnEponDot3MpcpRxRegRequestCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxRegRequestCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxRegRequestCurrent.setUnits(_C)
_ZxAnEponDot3MpcpTxRegAckCurrent_Type=Counter64
_ZxAnEponDot3MpcpTxRegAckCurrent_Object=MibTableColumn
zxAnEponDot3MpcpTxRegAckCurrent=_ZxAnEponDot3MpcpTxRegAckCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,7),_ZxAnEponDot3MpcpTxRegAckCurrent_Type())
zxAnEponDot3MpcpTxRegAckCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxRegAckCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxRegAckCurrent.setUnits(_C)
_ZxAnEponDot3MpcpRxRegAckCurrent_Type=Counter64
_ZxAnEponDot3MpcpRxRegAckCurrent_Object=MibTableColumn
zxAnEponDot3MpcpRxRegAckCurrent=_ZxAnEponDot3MpcpRxRegAckCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,8),_ZxAnEponDot3MpcpRxRegAckCurrent_Type())
zxAnEponDot3MpcpRxRegAckCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxRegAckCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxRegAckCurrent.setUnits(_C)
_ZxAnEponDot3MpcpTxReportCurrent_Type=Counter64
_ZxAnEponDot3MpcpTxReportCurrent_Object=MibTableColumn
zxAnEponDot3MpcpTxReportCurrent=_ZxAnEponDot3MpcpTxReportCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,9),_ZxAnEponDot3MpcpTxReportCurrent_Type())
zxAnEponDot3MpcpTxReportCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxReportCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxReportCurrent.setUnits(_C)
_ZxAnEponDot3MpcpRxReportCurrent_Type=Counter64
_ZxAnEponDot3MpcpRxReportCurrent_Object=MibTableColumn
zxAnEponDot3MpcpRxReportCurrent=_ZxAnEponDot3MpcpRxReportCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,10),_ZxAnEponDot3MpcpRxReportCurrent_Type())
zxAnEponDot3MpcpRxReportCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxReportCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxReportCurrent.setUnits(_C)
_ZxAnEponDot3MpcpTxGateCurrent_Type=Counter64
_ZxAnEponDot3MpcpTxGateCurrent_Object=MibTableColumn
zxAnEponDot3MpcpTxGateCurrent=_ZxAnEponDot3MpcpTxGateCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,11),_ZxAnEponDot3MpcpTxGateCurrent_Type())
zxAnEponDot3MpcpTxGateCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxGateCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxGateCurrent.setUnits(_C)
_ZxAnEponDot3MpcpRxGateCurrent_Type=Counter64
_ZxAnEponDot3MpcpRxGateCurrent_Object=MibTableColumn
zxAnEponDot3MpcpRxGateCurrent=_ZxAnEponDot3MpcpRxGateCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,12),_ZxAnEponDot3MpcpRxGateCurrent_Type())
zxAnEponDot3MpcpRxGateCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxGateCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxGateCurrent.setUnits(_C)
_ZxAnEponDot3MpcpTxRegisterCurrent_Type=Counter64
_ZxAnEponDot3MpcpTxRegisterCurrent_Object=MibTableColumn
zxAnEponDot3MpcpTxRegisterCurrent=_ZxAnEponDot3MpcpTxRegisterCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,13),_ZxAnEponDot3MpcpTxRegisterCurrent_Type())
zxAnEponDot3MpcpTxRegisterCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxRegisterCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpTxRegisterCurrent.setUnits(_C)
_ZxAnEponDot3MpcpRxRegisterCurrent_Type=Counter64
_ZxAnEponDot3MpcpRxRegisterCurrent_Object=MibTableColumn
zxAnEponDot3MpcpRxRegisterCurrent=_ZxAnEponDot3MpcpRxRegisterCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,1,1,14),_ZxAnEponDot3MpcpRxRegisterCurrent_Type())
zxAnEponDot3MpcpRxRegisterCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxRegisterCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3MpcpRxRegisterCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationStatCurrentTable_Object=MibTable
zxAnEponDot3OmpEmulationStatCurrentTable=_ZxAnEponDot3OmpEmulationStatCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2))
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationStatCurrentTable.setStatus(_A)
_ZxAnEponDot3OmpEmulationStatCurrentEntry_Object=MibTableRow
zxAnEponDot3OmpEmulationStatCurrentEntry=_ZxAnEponDot3OmpEmulationStatCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1))
zxAnEponDot3OmpEmulationStatCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationStatCurrentEntry.setStatus(_A)
_ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationSLDErrorsCurrent=_ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,1),_ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Type())
zxAnEponDot3OmpEmulationSLDErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationSLDErrorsCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationSLDErrorsCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationCRC8ErrorsCurrent=_ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,2),_ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Type())
zxAnEponDot3OmpEmulationCRC8ErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationCRC8ErrorsCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationCRC8ErrorsCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationBadLLIDCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationBadLLIDCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationBadLLIDCurrent=_ZxAnEponDot3OmpEmulationBadLLIDCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,3),_ZxAnEponDot3OmpEmulationBadLLIDCurrent_Type())
zxAnEponDot3OmpEmulationBadLLIDCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationBadLLIDCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationBadLLIDCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationGoodLLIDCurrent=_ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,4),_ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Type())
zxAnEponDot3OmpEmulationGoodLLIDCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationGoodLLIDCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationGoodLLIDCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent=_ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,5),_ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Type())
zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent=_ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,6),_ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Type())
zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent=_ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,7),_ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Type())
zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent=_ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,8),_ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Type())
zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent=_ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,9),_ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Type())
zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent.setUnits(_C)
_ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Type=Counter64
_ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Object=MibTableColumn
zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent=_ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,2,1,10),_ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Type())
zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent.setUnits(_C)
_ZxAnEponDot3EponFecCurrentTable_Object=MibTable
zxAnEponDot3EponFecCurrentTable=_ZxAnEponDot3EponFecCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3))
if mibBuilder.loadTexts:zxAnEponDot3EponFecCurrentTable.setStatus(_A)
_ZxAnEponDot3EponFecCurrentEntry_Object=MibTableRow
zxAnEponDot3EponFecCurrentEntry=_ZxAnEponDot3EponFecCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3,1))
zxAnEponDot3EponFecCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3EponFecCurrentEntry.setStatus(_A)
_ZxAnEponDot3EponFecPCSCodingViolationCurrent_Type=Counter64
_ZxAnEponDot3EponFecPCSCodingViolationCurrent_Object=MibTableColumn
zxAnEponDot3EponFecPCSCodingViolationCurrent=_ZxAnEponDot3EponFecPCSCodingViolationCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3,1,1),_ZxAnEponDot3EponFecPCSCodingViolationCurrent_Type())
zxAnEponDot3EponFecPCSCodingViolationCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3EponFecPCSCodingViolationCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3EponFecPCSCodingViolationCurrent.setUnits(_M)
class _ZxAnEponDot3EponFecAbilityCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('unsupported',2),('supported',3)))
_ZxAnEponDot3EponFecAbilityCurrent_Type.__name__=_J
_ZxAnEponDot3EponFecAbilityCurrent_Object=MibTableColumn
zxAnEponDot3EponFecAbilityCurrent=_ZxAnEponDot3EponFecAbilityCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3,1,2),_ZxAnEponDot3EponFecAbilityCurrent_Type())
zxAnEponDot3EponFecAbilityCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3EponFecAbilityCurrent.setStatus(_A)
class _ZxAnEponDot3EponFecModeCurrent_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('disabled',2),('enabled',3)))
_ZxAnEponDot3EponFecModeCurrent_Type.__name__=_J
_ZxAnEponDot3EponFecModeCurrent_Object=MibTableColumn
zxAnEponDot3EponFecModeCurrent=_ZxAnEponDot3EponFecModeCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3,1,3),_ZxAnEponDot3EponFecModeCurrent_Type())
zxAnEponDot3EponFecModeCurrent.setMaxAccess(_O)
if mibBuilder.loadTexts:zxAnEponDot3EponFecModeCurrent.setStatus(_A)
_ZxAnEponDot3EponFecCorrectedBlocksCurrent_Type=Counter64
_ZxAnEponDot3EponFecCorrectedBlocksCurrent_Object=MibTableColumn
zxAnEponDot3EponFecCorrectedBlocksCurrent=_ZxAnEponDot3EponFecCorrectedBlocksCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3,1,4),_ZxAnEponDot3EponFecCorrectedBlocksCurrent_Type())
zxAnEponDot3EponFecCorrectedBlocksCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3EponFecCorrectedBlocksCurrent.setStatus(_A)
_ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Type=Counter64
_ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Object=MibTableColumn
zxAnEponDot3EponFecUncorrectableBlocksCurrent=_ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3,1,5),_ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Type())
zxAnEponDot3EponFecUncorrectableBlocksCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3EponFecUncorrectableBlocksCurrent.setStatus(_A)
_ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Type=Counter64
_ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Object=MibTableColumn
zxAnEponDot3EponFecBufferHeadCodingViolationCurrent=_ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,3,1,6),_ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Type())
zxAnEponDot3EponFecBufferHeadCodingViolationCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3EponFecBufferHeadCodingViolationCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3EponFecBufferHeadCodingViolationCurrent.setUnits(_M)
_ZxAnEponDot3ExtPkgQueueCurrentTable_Object=MibTable
zxAnEponDot3ExtPkgQueueCurrentTable=_ZxAnEponDot3ExtPkgQueueCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4))
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgQueueCurrentTable.setStatus(_A)
_ZxAnEponDot3ExtPkgQueueCurrentEntry_Object=MibTableRow
zxAnEponDot3ExtPkgQueueCurrentEntry=_ZxAnEponDot3ExtPkgQueueCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4,1))
zxAnEponDot3ExtPkgQueueCurrentEntry.setIndexNames((0,_D,_E),(0,_G,_P))
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgQueueCurrentEntry.setStatus(_A)
class _ZxAnEponDot3QueueIndexCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponDot3QueueIndexCurrent_Type.__name__=_H
_ZxAnEponDot3QueueIndexCurrent_Object=MibTableColumn
zxAnEponDot3QueueIndexCurrent=_ZxAnEponDot3QueueIndexCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4,1,1),_ZxAnEponDot3QueueIndexCurrent_Type())
zxAnEponDot3QueueIndexCurrent.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnEponDot3QueueIndexCurrent.setStatus(_A)
class _ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Type.__name__=_H
_ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Object=MibTableColumn
zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent=_ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4,1,2),_ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Type())
zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent.setMaxAccess(_O)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent.setStatus(_A)
class _ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Type.__name__=_H
_ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Object=MibTableColumn
zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent=_ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4,1,3),_ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Type())
zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent.setStatus(_A)
_ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Type=Counter64
_ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Object=MibTableColumn
zxAnEponDot3ExtPkgStatTxFramesQueueCurrent=_ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4,1,4),_ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Type())
zxAnEponDot3ExtPkgStatTxFramesQueueCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgStatTxFramesQueueCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgStatTxFramesQueueCurrent.setUnits(_C)
_ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Type=Counter64
_ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Object=MibTableColumn
zxAnEponDot3ExtPkgStatRxFramesQueueCurrent=_ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4,1,5),_ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Type())
zxAnEponDot3ExtPkgStatRxFramesQueueCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgStatRxFramesQueueCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgStatRxFramesQueueCurrent.setUnits(_C)
_ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Type=Counter64
_ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Object=MibTableColumn
zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent=_ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,4,1,6),_ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Type())
zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent.setUnits(_C)
_ZxAnEponDot3OamStatsCurrentTable_Object=MibTable
zxAnEponDot3OamStatsCurrentTable=_ZxAnEponDot3OamStatsCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5))
if mibBuilder.loadTexts:zxAnEponDot3OamStatsCurrentTable.setStatus(_A)
_ZxAnEponDot3OamStatsCurrentEntry_Object=MibTableRow
zxAnEponDot3OamStatsCurrentEntry=_ZxAnEponDot3OamStatsCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1))
zxAnEponDot3OamStatsCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3OamStatsCurrentEntry.setStatus(_A)
_ZxAnEponDot3OamInformationTxCurrent_Type=Counter32
_ZxAnEponDot3OamInformationTxCurrent_Object=MibTableColumn
zxAnEponDot3OamInformationTxCurrent=_ZxAnEponDot3OamInformationTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,1),_ZxAnEponDot3OamInformationTxCurrent_Type())
zxAnEponDot3OamInformationTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamInformationTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamInformationTxCurrent.setUnits(_C)
_ZxAnEponDot3OamInformationRxCurrent_Type=Counter32
_ZxAnEponDot3OamInformationRxCurrent_Object=MibTableColumn
zxAnEponDot3OamInformationRxCurrent=_ZxAnEponDot3OamInformationRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,2),_ZxAnEponDot3OamInformationRxCurrent_Type())
zxAnEponDot3OamInformationRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamInformationRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamInformationRxCurrent.setUnits(_C)
_ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Type=Counter32
_ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Object=MibTableColumn
zxAnEponDot3OamUniqueEventNotificationTxCurrent=_ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,3),_ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Type())
zxAnEponDot3OamUniqueEventNotificationTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamUniqueEventNotificationTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamUniqueEventNotificationTxCurrent.setUnits(_C)
_ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Type=Counter32
_ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Object=MibTableColumn
zxAnEponDot3OamUniqueEventNotificationRxCurrent=_ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,4),_ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Type())
zxAnEponDot3OamUniqueEventNotificationRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamUniqueEventNotificationRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamUniqueEventNotificationRxCurrent.setUnits(_C)
_ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Type=Counter32
_ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Object=MibTableColumn
zxAnEponDot3OamDuplicateEventNotificationTxCurrent=_ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,5),_ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Type())
zxAnEponDot3OamDuplicateEventNotificationTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamDuplicateEventNotificationTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamDuplicateEventNotificationTxCurrent.setUnits(_C)
_ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Type=Counter32
_ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Object=MibTableColumn
zxAnEponDot3OamDuplicateEventNotificationRxCurrent=_ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,6),_ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Type())
zxAnEponDot3OamDuplicateEventNotificationRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamDuplicateEventNotificationRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamDuplicateEventNotificationRxCurrent.setUnits(_C)
_ZxAnEponDot3OamLoopbackControlTxCurrent_Type=Counter32
_ZxAnEponDot3OamLoopbackControlTxCurrent_Object=MibTableColumn
zxAnEponDot3OamLoopbackControlTxCurrent=_ZxAnEponDot3OamLoopbackControlTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,7),_ZxAnEponDot3OamLoopbackControlTxCurrent_Type())
zxAnEponDot3OamLoopbackControlTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamLoopbackControlTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamLoopbackControlTxCurrent.setUnits(_C)
_ZxAnEponDot3OamLoopbackControlRxCurrent_Type=Counter32
_ZxAnEponDot3OamLoopbackControlRxCurrent_Object=MibTableColumn
zxAnEponDot3OamLoopbackControlRxCurrent=_ZxAnEponDot3OamLoopbackControlRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,8),_ZxAnEponDot3OamLoopbackControlRxCurrent_Type())
zxAnEponDot3OamLoopbackControlRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamLoopbackControlRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamLoopbackControlRxCurrent.setUnits(_C)
_ZxAnEponDot3OamVariableRequestTxCurrent_Type=Counter32
_ZxAnEponDot3OamVariableRequestTxCurrent_Object=MibTableColumn
zxAnEponDot3OamVariableRequestTxCurrent=_ZxAnEponDot3OamVariableRequestTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,9),_ZxAnEponDot3OamVariableRequestTxCurrent_Type())
zxAnEponDot3OamVariableRequestTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableRequestTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableRequestTxCurrent.setUnits(_C)
_ZxAnEponDot3OamVariableRequestRxCurrent_Type=Counter32
_ZxAnEponDot3OamVariableRequestRxCurrent_Object=MibTableColumn
zxAnEponDot3OamVariableRequestRxCurrent=_ZxAnEponDot3OamVariableRequestRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,10),_ZxAnEponDot3OamVariableRequestRxCurrent_Type())
zxAnEponDot3OamVariableRequestRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableRequestRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableRequestRxCurrent.setUnits(_C)
_ZxAnEponDot3OamVariableResponseTxCurrent_Type=Counter32
_ZxAnEponDot3OamVariableResponseTxCurrent_Object=MibTableColumn
zxAnEponDot3OamVariableResponseTxCurrent=_ZxAnEponDot3OamVariableResponseTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,11),_ZxAnEponDot3OamVariableResponseTxCurrent_Type())
zxAnEponDot3OamVariableResponseTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableResponseTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableResponseTxCurrent.setUnits(_C)
_ZxAnEponDot3OamVariableResponseRxCurrent_Type=Counter32
_ZxAnEponDot3OamVariableResponseRxCurrent_Object=MibTableColumn
zxAnEponDot3OamVariableResponseRxCurrent=_ZxAnEponDot3OamVariableResponseRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,12),_ZxAnEponDot3OamVariableResponseRxCurrent_Type())
zxAnEponDot3OamVariableResponseRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableResponseRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamVariableResponseRxCurrent.setUnits(_C)
_ZxAnEponDot3OamOrgSpecificTxCurrent_Type=Counter32
_ZxAnEponDot3OamOrgSpecificTxCurrent_Object=MibTableColumn
zxAnEponDot3OamOrgSpecificTxCurrent=_ZxAnEponDot3OamOrgSpecificTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,13),_ZxAnEponDot3OamOrgSpecificTxCurrent_Type())
zxAnEponDot3OamOrgSpecificTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamOrgSpecificTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamOrgSpecificTxCurrent.setUnits(_C)
_ZxAnEponDot3OamOrgSpecificRxCurrent_Type=Counter32
_ZxAnEponDot3OamOrgSpecificRxCurrent_Object=MibTableColumn
zxAnEponDot3OamOrgSpecificRxCurrent=_ZxAnEponDot3OamOrgSpecificRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,14),_ZxAnEponDot3OamOrgSpecificRxCurrent_Type())
zxAnEponDot3OamOrgSpecificRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamOrgSpecificRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamOrgSpecificRxCurrent.setUnits(_C)
_ZxAnEponDot3OamUnsupportedCodesTxCurrent_Type=Counter32
_ZxAnEponDot3OamUnsupportedCodesTxCurrent_Object=MibTableColumn
zxAnEponDot3OamUnsupportedCodesTxCurrent=_ZxAnEponDot3OamUnsupportedCodesTxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,15),_ZxAnEponDot3OamUnsupportedCodesTxCurrent_Type())
zxAnEponDot3OamUnsupportedCodesTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamUnsupportedCodesTxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamUnsupportedCodesTxCurrent.setUnits(_C)
_ZxAnEponDot3OamUnsupportedCodesRxCurrent_Type=Counter32
_ZxAnEponDot3OamUnsupportedCodesRxCurrent_Object=MibTableColumn
zxAnEponDot3OamUnsupportedCodesRxCurrent=_ZxAnEponDot3OamUnsupportedCodesRxCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,16),_ZxAnEponDot3OamUnsupportedCodesRxCurrent_Type())
zxAnEponDot3OamUnsupportedCodesRxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamUnsupportedCodesRxCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamUnsupportedCodesRxCurrent.setUnits(_C)
_ZxAnEponDot3OamFramesLostDueToOamCurrent_Type=Counter32
_ZxAnEponDot3OamFramesLostDueToOamCurrent_Object=MibTableColumn
zxAnEponDot3OamFramesLostDueToOamCurrent=_ZxAnEponDot3OamFramesLostDueToOamCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,5,1,17),_ZxAnEponDot3OamFramesLostDueToOamCurrent_Type())
zxAnEponDot3OamFramesLostDueToOamCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OamFramesLostDueToOamCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponDot3OamFramesLostDueToOamCurrent.setUnits(_C)
_ZxAnEponOltVirtualIfBERStatisticCurrentTable_Object=MibTable
zxAnEponOltVirtualIfBERStatisticCurrentTable=_ZxAnEponOltVirtualIfBERStatisticCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,6))
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticCurrentTable.setStatus(_A)
_ZxAnEponOltVirtualIfBERStatisticCurrentEntry_Object=MibTableRow
zxAnEponOltVirtualIfBERStatisticCurrentEntry=_ZxAnEponOltVirtualIfBERStatisticCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,6,1))
zxAnEponOltVirtualIfBERStatisticCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticCurrentEntry.setStatus(_A)
_ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Type=Counter32
_ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Object=MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuBERCurrent=_ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,6,1,1),_ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Type())
zxAnEponOltVirtualIfBERStatisticOnuBERCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticOnuBERCurrent.setStatus(_A)
_ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Type=Counter32
_ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Object=MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuFERCurrent=_ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,6,1,2),_ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Type())
zxAnEponOltVirtualIfBERStatisticOnuFERCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticOnuFERCurrent.setStatus(_A)
_ZxAnEponOltPhyPortStatisticCurrentTable_Object=MibTable
zxAnEponOltPhyPortStatisticCurrentTable=_ZxAnEponOltPhyPortStatisticCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,7))
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticCurrentTable.setStatus(_A)
_ZxAnEponOltPhyPortStatisticCurrentEntry_Object=MibTableRow
zxAnEponOltPhyPortStatisticCurrentEntry=_ZxAnEponOltPhyPortStatisticCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,7,1))
zxAnEponOltPhyPortStatisticCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticCurrentEntry.setStatus(_A)
_ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Type=Counter32
_ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Object=MibTableColumn
zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent=_ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,7,1,1),_ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Type())
zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent.setStatus(_A)
_ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Type=Counter32
_ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Object=MibTableColumn
zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent=_ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,7,1,2),_ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Type())
zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent.setStatus(_A)
_ZxAnEponEtherStatsCurrentTable_Object=MibTable
zxAnEponEtherStatsCurrentTable=_ZxAnEponEtherStatsCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8))
if mibBuilder.loadTexts:zxAnEponEtherStatsCurrentTable.setStatus(_A)
_ZxAnEponEtherStatsCurrentEntry_Object=MibTableRow
zxAnEponEtherStatsCurrentEntry=_ZxAnEponEtherStatsCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1))
zxAnEponEtherStatsCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponEtherStatsCurrentEntry.setStatus(_A)
_ZxAnEponEtherStatsDropEventsCurrent_Type=Counter32
_ZxAnEponEtherStatsDropEventsCurrent_Object=MibTableColumn
zxAnEponEtherStatsDropEventsCurrent=_ZxAnEponEtherStatsDropEventsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,1),_ZxAnEponEtherStatsDropEventsCurrent_Type())
zxAnEponEtherStatsDropEventsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsDropEventsCurrent.setStatus(_A)
_ZxAnEponEtherStatsOctetsCurrent_Type=Counter32
_ZxAnEponEtherStatsOctetsCurrent_Object=MibTableColumn
zxAnEponEtherStatsOctetsCurrent=_ZxAnEponEtherStatsOctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,2),_ZxAnEponEtherStatsOctetsCurrent_Type())
zxAnEponEtherStatsOctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsOctetsCurrent.setStatus(_A)
_ZxAnEponEtherStatsPktsCurrent_Type=Counter32
_ZxAnEponEtherStatsPktsCurrent_Object=MibTableColumn
zxAnEponEtherStatsPktsCurrent=_ZxAnEponEtherStatsPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,3),_ZxAnEponEtherStatsPktsCurrent_Type())
zxAnEponEtherStatsPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPktsCurrent.setStatus(_A)
_ZxAnEponEtherStatsBroadcastPktsCurrent_Type=Counter32
_ZxAnEponEtherStatsBroadcastPktsCurrent_Object=MibTableColumn
zxAnEponEtherStatsBroadcastPktsCurrent=_ZxAnEponEtherStatsBroadcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,4),_ZxAnEponEtherStatsBroadcastPktsCurrent_Type())
zxAnEponEtherStatsBroadcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsBroadcastPktsCurrent.setStatus(_A)
_ZxAnEponEtherStatsMulticastPktsCurrent_Type=Counter32
_ZxAnEponEtherStatsMulticastPktsCurrent_Object=MibTableColumn
zxAnEponEtherStatsMulticastPktsCurrent=_ZxAnEponEtherStatsMulticastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,5),_ZxAnEponEtherStatsMulticastPktsCurrent_Type())
zxAnEponEtherStatsMulticastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsMulticastPktsCurrent.setStatus(_A)
_ZxAnEponEtherStatsCRCAlignErrorsCurrent_Type=Counter32
_ZxAnEponEtherStatsCRCAlignErrorsCurrent_Object=MibTableColumn
zxAnEponEtherStatsCRCAlignErrorsCurrent=_ZxAnEponEtherStatsCRCAlignErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,6),_ZxAnEponEtherStatsCRCAlignErrorsCurrent_Type())
zxAnEponEtherStatsCRCAlignErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsCRCAlignErrorsCurrent.setStatus(_A)
_ZxAnEponEtherStatsUndersizePktsCurrent_Type=Counter32
_ZxAnEponEtherStatsUndersizePktsCurrent_Object=MibTableColumn
zxAnEponEtherStatsUndersizePktsCurrent=_ZxAnEponEtherStatsUndersizePktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,7),_ZxAnEponEtherStatsUndersizePktsCurrent_Type())
zxAnEponEtherStatsUndersizePktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsUndersizePktsCurrent.setStatus(_A)
_ZxAnEponEtherStatsOversizePktsCurrent_Type=Counter32
_ZxAnEponEtherStatsOversizePktsCurrent_Object=MibTableColumn
zxAnEponEtherStatsOversizePktsCurrent=_ZxAnEponEtherStatsOversizePktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,8),_ZxAnEponEtherStatsOversizePktsCurrent_Type())
zxAnEponEtherStatsOversizePktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsOversizePktsCurrent.setStatus(_A)
_ZxAnEponEtherStatsFragmentsCurrent_Type=Counter32
_ZxAnEponEtherStatsFragmentsCurrent_Object=MibTableColumn
zxAnEponEtherStatsFragmentsCurrent=_ZxAnEponEtherStatsFragmentsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,9),_ZxAnEponEtherStatsFragmentsCurrent_Type())
zxAnEponEtherStatsFragmentsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsFragmentsCurrent.setStatus(_A)
_ZxAnEponEtherStatsJabbersCurrent_Type=Counter32
_ZxAnEponEtherStatsJabbersCurrent_Object=MibTableColumn
zxAnEponEtherStatsJabbersCurrent=_ZxAnEponEtherStatsJabbersCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,10),_ZxAnEponEtherStatsJabbersCurrent_Type())
zxAnEponEtherStatsJabbersCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsJabbersCurrent.setStatus(_A)
_ZxAnEponEtherStatsCollisionsCurrent_Type=Counter32
_ZxAnEponEtherStatsCollisionsCurrent_Object=MibTableColumn
zxAnEponEtherStatsCollisionsCurrent=_ZxAnEponEtherStatsCollisionsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,11),_ZxAnEponEtherStatsCollisionsCurrent_Type())
zxAnEponEtherStatsCollisionsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsCollisionsCurrent.setStatus(_A)
_ZxAnEponEtherStatsPkts64OctetsCurrent_Type=Counter32
_ZxAnEponEtherStatsPkts64OctetsCurrent_Object=MibTableColumn
zxAnEponEtherStatsPkts64OctetsCurrent=_ZxAnEponEtherStatsPkts64OctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,12),_ZxAnEponEtherStatsPkts64OctetsCurrent_Type())
zxAnEponEtherStatsPkts64OctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts64OctetsCurrent.setStatus(_A)
_ZxAnEponEtherStatsPkts65to127OctetsCurrent_Type=Counter32
_ZxAnEponEtherStatsPkts65to127OctetsCurrent_Object=MibTableColumn
zxAnEponEtherStatsPkts65to127OctetsCurrent=_ZxAnEponEtherStatsPkts65to127OctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,13),_ZxAnEponEtherStatsPkts65to127OctetsCurrent_Type())
zxAnEponEtherStatsPkts65to127OctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts65to127OctetsCurrent.setStatus(_A)
_ZxAnEponEtherStatsPkts128to255OctetsCurrent_Type=Counter32
_ZxAnEponEtherStatsPkts128to255OctetsCurrent_Object=MibTableColumn
zxAnEponEtherStatsPkts128to255OctetsCurrent=_ZxAnEponEtherStatsPkts128to255OctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,14),_ZxAnEponEtherStatsPkts128to255OctetsCurrent_Type())
zxAnEponEtherStatsPkts128to255OctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts128to255OctetsCurrent.setStatus(_A)
_ZxAnEponEtherStatsPkts256to511OctetsCurrent_Type=Counter32
_ZxAnEponEtherStatsPkts256to511OctetsCurrent_Object=MibTableColumn
zxAnEponEtherStatsPkts256to511OctetsCurrent=_ZxAnEponEtherStatsPkts256to511OctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,15),_ZxAnEponEtherStatsPkts256to511OctetsCurrent_Type())
zxAnEponEtherStatsPkts256to511OctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts256to511OctetsCurrent.setStatus(_A)
_ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Type=Counter32
_ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Object=MibTableColumn
zxAnEponEtherStatsPkts512to1023OctetsCurrent=_ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,16),_ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Type())
zxAnEponEtherStatsPkts512to1023OctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts512to1023OctetsCurrent.setStatus(_A)
_ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Type=Counter32
_ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Object=MibTableColumn
zxAnEponEtherStatsPkts1024to1518OctetsCurrent=_ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,17),_ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Type())
zxAnEponEtherStatsPkts1024to1518OctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts1024to1518OctetsCurrent.setStatus(_A)
_ZxAnEponEtherStatsOwnerCurrent_Type=OwnerString
_ZxAnEponEtherStatsOwnerCurrent_Object=MibTableColumn
zxAnEponEtherStatsOwnerCurrent=_ZxAnEponEtherStatsOwnerCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,18),_ZxAnEponEtherStatsOwnerCurrent_Type())
zxAnEponEtherStatsOwnerCurrent.setMaxAccess(_Q)
if mibBuilder.loadTexts:zxAnEponEtherStatsOwnerCurrent.setStatus(_A)
_ZxAnEponEtherStatsStatusCurrent_Type=EntryStatus
_ZxAnEponEtherStatsStatusCurrent_Object=MibTableColumn
zxAnEponEtherStatsStatusCurrent=_ZxAnEponEtherStatsStatusCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,8,1,19),_ZxAnEponEtherStatsStatusCurrent_Type())
zxAnEponEtherStatsStatusCurrent.setMaxAccess(_Q)
if mibBuilder.loadTexts:zxAnEponEtherStatsStatusCurrent.setStatus(_A)
_ZxAnEponIfCurrentTable_Object=MibTable
zxAnEponIfCurrentTable=_ZxAnEponIfCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9))
if mibBuilder.loadTexts:zxAnEponIfCurrentTable.setStatus(_A)
_ZxAnEponIfCurrentEntry_Object=MibTableRow
zxAnEponIfCurrentEntry=_ZxAnEponIfCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1))
zxAnEponIfCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponIfCurrentEntry.setStatus(_A)
_ZxAnEponIfInOctetsCurrent_Type=Counter32
_ZxAnEponIfInOctetsCurrent_Object=MibTableColumn
zxAnEponIfInOctetsCurrent=_ZxAnEponIfInOctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,1),_ZxAnEponIfInOctetsCurrent_Type())
zxAnEponIfInOctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInOctetsCurrent.setStatus(_A)
_ZxAnEponIfInUcastPktsCurrent_Type=Counter32
_ZxAnEponIfInUcastPktsCurrent_Object=MibTableColumn
zxAnEponIfInUcastPktsCurrent=_ZxAnEponIfInUcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,2),_ZxAnEponIfInUcastPktsCurrent_Type())
zxAnEponIfInUcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInUcastPktsCurrent.setStatus(_A)
_ZxAnEponIfInNUcastPktsCurrent_Type=Counter32
_ZxAnEponIfInNUcastPktsCurrent_Object=MibTableColumn
zxAnEponIfInNUcastPktsCurrent=_ZxAnEponIfInNUcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,3),_ZxAnEponIfInNUcastPktsCurrent_Type())
zxAnEponIfInNUcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInNUcastPktsCurrent.setStatus(_I)
_ZxAnEponIfInDiscardsCurrent_Type=Counter32
_ZxAnEponIfInDiscardsCurrent_Object=MibTableColumn
zxAnEponIfInDiscardsCurrent=_ZxAnEponIfInDiscardsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,4),_ZxAnEponIfInDiscardsCurrent_Type())
zxAnEponIfInDiscardsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInDiscardsCurrent.setStatus(_A)
_ZxAnEponIfInErrorsCurrent_Type=Counter32
_ZxAnEponIfInErrorsCurrent_Object=MibTableColumn
zxAnEponIfInErrorsCurrent=_ZxAnEponIfInErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,5),_ZxAnEponIfInErrorsCurrent_Type())
zxAnEponIfInErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInErrorsCurrent.setStatus(_A)
_ZxAnEponIfInUnknownProtosCurrent_Type=Counter32
_ZxAnEponIfInUnknownProtosCurrent_Object=MibTableColumn
zxAnEponIfInUnknownProtosCurrent=_ZxAnEponIfInUnknownProtosCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,6),_ZxAnEponIfInUnknownProtosCurrent_Type())
zxAnEponIfInUnknownProtosCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInUnknownProtosCurrent.setStatus(_A)
_ZxAnEponIfOutOctetsCurrent_Type=Counter32
_ZxAnEponIfOutOctetsCurrent_Object=MibTableColumn
zxAnEponIfOutOctetsCurrent=_ZxAnEponIfOutOctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,7),_ZxAnEponIfOutOctetsCurrent_Type())
zxAnEponIfOutOctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutOctetsCurrent.setStatus(_A)
_ZxAnEponIfOutUcastPktsCurrent_Type=Counter32
_ZxAnEponIfOutUcastPktsCurrent_Object=MibTableColumn
zxAnEponIfOutUcastPktsCurrent=_ZxAnEponIfOutUcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,8),_ZxAnEponIfOutUcastPktsCurrent_Type())
zxAnEponIfOutUcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutUcastPktsCurrent.setStatus(_A)
_ZxAnEponIfOutNUcastPktsCurrent_Type=Counter32
_ZxAnEponIfOutNUcastPktsCurrent_Object=MibTableColumn
zxAnEponIfOutNUcastPktsCurrent=_ZxAnEponIfOutNUcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,9),_ZxAnEponIfOutNUcastPktsCurrent_Type())
zxAnEponIfOutNUcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutNUcastPktsCurrent.setStatus(_I)
_ZxAnEponIfOutDiscardsCurrent_Type=Counter32
_ZxAnEponIfOutDiscardsCurrent_Object=MibTableColumn
zxAnEponIfOutDiscardsCurrent=_ZxAnEponIfOutDiscardsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,10),_ZxAnEponIfOutDiscardsCurrent_Type())
zxAnEponIfOutDiscardsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutDiscardsCurrent.setStatus(_A)
_ZxAnEponIfOutErrorsCurrent_Type=Counter32
_ZxAnEponIfOutErrorsCurrent_Object=MibTableColumn
zxAnEponIfOutErrorsCurrent=_ZxAnEponIfOutErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,9,1,11),_ZxAnEponIfOutErrorsCurrent_Type())
zxAnEponIfOutErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutErrorsCurrent.setStatus(_A)
_ZxAnEponIfXCurrentTable_Object=MibTable
zxAnEponIfXCurrentTable=_ZxAnEponIfXCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10))
if mibBuilder.loadTexts:zxAnEponIfXCurrentTable.setStatus(_A)
_ZxAnEponIfXCurrentEntry_Object=MibTableRow
zxAnEponIfXCurrentEntry=_ZxAnEponIfXCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1))
if mibBuilder.loadTexts:zxAnEponIfXCurrentEntry.setStatus(_A)
_ZxAnEponIfInMulticastPktsCurrent_Type=Counter32
_ZxAnEponIfInMulticastPktsCurrent_Object=MibTableColumn
zxAnEponIfInMulticastPktsCurrent=_ZxAnEponIfInMulticastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,1),_ZxAnEponIfInMulticastPktsCurrent_Type())
zxAnEponIfInMulticastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInMulticastPktsCurrent.setStatus(_A)
_ZxAnEponIfInBroadcastPktsCurrent_Type=Counter32
_ZxAnEponIfInBroadcastPktsCurrent_Object=MibTableColumn
zxAnEponIfInBroadcastPktsCurrent=_ZxAnEponIfInBroadcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,2),_ZxAnEponIfInBroadcastPktsCurrent_Type())
zxAnEponIfInBroadcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInBroadcastPktsCurrent.setStatus(_A)
_ZxAnEponIfOutMulticastPktsCurrent_Type=Counter32
_ZxAnEponIfOutMulticastPktsCurrent_Object=MibTableColumn
zxAnEponIfOutMulticastPktsCurrent=_ZxAnEponIfOutMulticastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,3),_ZxAnEponIfOutMulticastPktsCurrent_Type())
zxAnEponIfOutMulticastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutMulticastPktsCurrent.setStatus(_A)
_ZxAnEponIfOutBroadcastPktsCurrent_Type=Counter32
_ZxAnEponIfOutBroadcastPktsCurrent_Object=MibTableColumn
zxAnEponIfOutBroadcastPktsCurrent=_ZxAnEponIfOutBroadcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,4),_ZxAnEponIfOutBroadcastPktsCurrent_Type())
zxAnEponIfOutBroadcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutBroadcastPktsCurrent.setStatus(_A)
_ZxAnEponIfHCInOctetsCurrent_Type=Counter64
_ZxAnEponIfHCInOctetsCurrent_Object=MibTableColumn
zxAnEponIfHCInOctetsCurrent=_ZxAnEponIfHCInOctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,5),_ZxAnEponIfHCInOctetsCurrent_Type())
zxAnEponIfHCInOctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInOctetsCurrent.setStatus(_A)
_ZxAnEponIfHCInUcastPktsCurrent_Type=Counter64
_ZxAnEponIfHCInUcastPktsCurrent_Object=MibTableColumn
zxAnEponIfHCInUcastPktsCurrent=_ZxAnEponIfHCInUcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,6),_ZxAnEponIfHCInUcastPktsCurrent_Type())
zxAnEponIfHCInUcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInUcastPktsCurrent.setStatus(_A)
_ZxAnEponIfHCInMulticastPktsCurrent_Type=Counter64
_ZxAnEponIfHCInMulticastPktsCurrent_Object=MibTableColumn
zxAnEponIfHCInMulticastPktsCurrent=_ZxAnEponIfHCInMulticastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,7),_ZxAnEponIfHCInMulticastPktsCurrent_Type())
zxAnEponIfHCInMulticastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInMulticastPktsCurrent.setStatus(_A)
_ZxAnEponIfHCInBroadcastPktsCurrent_Type=Counter64
_ZxAnEponIfHCInBroadcastPktsCurrent_Object=MibTableColumn
zxAnEponIfHCInBroadcastPktsCurrent=_ZxAnEponIfHCInBroadcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,8),_ZxAnEponIfHCInBroadcastPktsCurrent_Type())
zxAnEponIfHCInBroadcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInBroadcastPktsCurrent.setStatus(_A)
_ZxAnEponIfHCOutOctetsCurrent_Type=Counter64
_ZxAnEponIfHCOutOctetsCurrent_Object=MibTableColumn
zxAnEponIfHCOutOctetsCurrent=_ZxAnEponIfHCOutOctetsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,9),_ZxAnEponIfHCOutOctetsCurrent_Type())
zxAnEponIfHCOutOctetsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutOctetsCurrent.setStatus(_A)
_ZxAnEponIfHCOutUcastPktsCurrent_Type=Counter64
_ZxAnEponIfHCOutUcastPktsCurrent_Object=MibTableColumn
zxAnEponIfHCOutUcastPktsCurrent=_ZxAnEponIfHCOutUcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,10),_ZxAnEponIfHCOutUcastPktsCurrent_Type())
zxAnEponIfHCOutUcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutUcastPktsCurrent.setStatus(_A)
_ZxAnEponIfHCOutMulticastPktsCurrent_Type=Counter64
_ZxAnEponIfHCOutMulticastPktsCurrent_Object=MibTableColumn
zxAnEponIfHCOutMulticastPktsCurrent=_ZxAnEponIfHCOutMulticastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,11),_ZxAnEponIfHCOutMulticastPktsCurrent_Type())
zxAnEponIfHCOutMulticastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutMulticastPktsCurrent.setStatus(_A)
_ZxAnEponIfHCOutBroadcastPktsCurrent_Type=Counter64
_ZxAnEponIfHCOutBroadcastPktsCurrent_Object=MibTableColumn
zxAnEponIfHCOutBroadcastPktsCurrent=_ZxAnEponIfHCOutBroadcastPktsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,10,1,12),_ZxAnEponIfHCOutBroadcastPktsCurrent_Type())
zxAnEponIfHCOutBroadcastPktsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutBroadcastPktsCurrent.setStatus(_A)
_ZxAnEponDot3PauseCurrentTable_Object=MibTable
zxAnEponDot3PauseCurrentTable=_ZxAnEponDot3PauseCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,11))
if mibBuilder.loadTexts:zxAnEponDot3PauseCurrentTable.setStatus(_A)
_ZxAnEponDot3PauseCurrentEntry_Object=MibTableRow
zxAnEponDot3PauseCurrentEntry=_ZxAnEponDot3PauseCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,11,1))
zxAnEponDot3PauseCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3PauseCurrentEntry.setStatus(_A)
_ZxAnEponDot3InPauseFramesCurrent_Type=Counter32
_ZxAnEponDot3InPauseFramesCurrent_Object=MibTableColumn
zxAnEponDot3InPauseFramesCurrent=_ZxAnEponDot3InPauseFramesCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,11,1,1),_ZxAnEponDot3InPauseFramesCurrent_Type())
zxAnEponDot3InPauseFramesCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3InPauseFramesCurrent.setStatus(_A)
_ZxAnEponDot3OutPauseFramesCurrent_Type=Counter32
_ZxAnEponDot3OutPauseFramesCurrent_Object=MibTableColumn
zxAnEponDot3OutPauseFramesCurrent=_ZxAnEponDot3OutPauseFramesCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,11,1,2),_ZxAnEponDot3OutPauseFramesCurrent_Type())
zxAnEponDot3OutPauseFramesCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3OutPauseFramesCurrent.setStatus(_A)
_ZxAnEponDot3HCInPauseFramesCurrent_Type=Counter64
_ZxAnEponDot3HCInPauseFramesCurrent_Object=MibTableColumn
zxAnEponDot3HCInPauseFramesCurrent=_ZxAnEponDot3HCInPauseFramesCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,11,1,3),_ZxAnEponDot3HCInPauseFramesCurrent_Type())
zxAnEponDot3HCInPauseFramesCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCInPauseFramesCurrent.setStatus(_A)
_ZxAnEponDot3HCOutPauseFramesCurrent_Type=Counter64
_ZxAnEponDot3HCOutPauseFramesCurrent_Object=MibTableColumn
zxAnEponDot3HCOutPauseFramesCurrent=_ZxAnEponDot3HCOutPauseFramesCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,11,1,4),_ZxAnEponDot3HCOutPauseFramesCurrent_Type())
zxAnEponDot3HCOutPauseFramesCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCOutPauseFramesCurrent.setStatus(_A)
_ZxAnEponDot3HCStatsCurrentTable_Object=MibTable
zxAnEponDot3HCStatsCurrentTable=_ZxAnEponDot3HCStatsCurrentTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12))
if mibBuilder.loadTexts:zxAnEponDot3HCStatsCurrentTable.setStatus(_A)
_ZxAnEponDot3HCStatsCurrentEntry_Object=MibTableRow
zxAnEponDot3HCStatsCurrentEntry=_ZxAnEponDot3HCStatsCurrentEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12,1))
zxAnEponDot3HCStatsCurrentEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponDot3HCStatsCurrentEntry.setStatus(_A)
_ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Type=Counter64
_ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Object=MibTableColumn
zxAnEponDot3HCStatsAlignmentErrorsCurrent=_ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12,1,1),_ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Type())
zxAnEponDot3HCStatsAlignmentErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsAlignmentErrorsCurrent.setStatus(_A)
_ZxAnEponDot3HCStatsFCSErrorsCurrent_Type=Counter64
_ZxAnEponDot3HCStatsFCSErrorsCurrent_Object=MibTableColumn
zxAnEponDot3HCStatsFCSErrorsCurrent=_ZxAnEponDot3HCStatsFCSErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12,1,2),_ZxAnEponDot3HCStatsFCSErrorsCurrent_Type())
zxAnEponDot3HCStatsFCSErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsFCSErrorsCurrent.setStatus(_A)
_ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Type=Counter64
_ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Object=MibTableColumn
zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent=_ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12,1,3),_ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Type())
zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent.setStatus(_A)
_ZxAnEponDot3HCStatsFrameTooLongsCurrent_Type=Counter64
_ZxAnEponDot3HCStatsFrameTooLongsCurrent_Object=MibTableColumn
zxAnEponDot3HCStatsFrameTooLongsCurrent=_ZxAnEponDot3HCStatsFrameTooLongsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12,1,4),_ZxAnEponDot3HCStatsFrameTooLongsCurrent_Type())
zxAnEponDot3HCStatsFrameTooLongsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsFrameTooLongsCurrent.setStatus(_A)
_ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Type=Counter64
_ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Object=MibTableColumn
zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent=_ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12,1,5),_ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Type())
zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent.setStatus(_A)
_ZxAnEponDot3HCStatsSymbolErrorsCurrent_Type=Counter64
_ZxAnEponDot3HCStatsSymbolErrorsCurrent_Object=MibTableColumn
zxAnEponDot3HCStatsSymbolErrorsCurrent=_ZxAnEponDot3HCStatsSymbolErrorsCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,12,1,6),_ZxAnEponDot3HCStatsSymbolErrorsCurrent_Type())
zxAnEponDot3HCStatsSymbolErrorsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponDot3HCStatsSymbolErrorsCurrent.setStatus(_A)
_ZxAnEponOnuLlidStatTable_Object=MibTable
zxAnEponOnuLlidStatTable=_ZxAnEponOnuLlidStatTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13))
if mibBuilder.loadTexts:zxAnEponOnuLlidStatTable.setStatus(_A)
_ZxAnEponOnuLlidStatEntry_Object=MibTableRow
zxAnEponOnuLlidStatEntry=_ZxAnEponOnuLlidStatEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1))
zxAnEponOnuLlidStatEntry.setIndexNames((0,_D,_E),(0,_K,_L))
if mibBuilder.loadTexts:zxAnEponOnuLlidStatEntry.setStatus(_A)
_ZxAnEponOnuLlidRxFrames_Type=Counter64
_ZxAnEponOnuLlidRxFrames_Object=MibTableColumn
zxAnEponOnuLlidRxFrames=_ZxAnEponOnuLlidRxFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,1),_ZxAnEponOnuLlidRxFrames_Type())
zxAnEponOnuLlidRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidRxFrames.setStatus(_A)
_ZxAnEponOnuLlidRxOctets_Type=Counter64
_ZxAnEponOnuLlidRxOctets_Object=MibTableColumn
zxAnEponOnuLlidRxOctets=_ZxAnEponOnuLlidRxOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,2),_ZxAnEponOnuLlidRxOctets_Type())
zxAnEponOnuLlidRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidRxOctets.setStatus(_A)
_ZxAnEponOnuLlidRxMulticastFrames_Type=Counter64
_ZxAnEponOnuLlidRxMulticastFrames_Object=MibTableColumn
zxAnEponOnuLlidRxMulticastFrames=_ZxAnEponOnuLlidRxMulticastFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,3),_ZxAnEponOnuLlidRxMulticastFrames_Type())
zxAnEponOnuLlidRxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidRxMulticastFrames.setStatus(_A)
_ZxAnEponOnuLlidRxBroadcastFrames_Type=Counter64
_ZxAnEponOnuLlidRxBroadcastFrames_Object=MibTableColumn
zxAnEponOnuLlidRxBroadcastFrames=_ZxAnEponOnuLlidRxBroadcastFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,4),_ZxAnEponOnuLlidRxBroadcastFrames_Type())
zxAnEponOnuLlidRxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidRxBroadcastFrames.setStatus(_A)
_ZxAnEponOnuLlidTxFrames_Type=Counter64
_ZxAnEponOnuLlidTxFrames_Object=MibTableColumn
zxAnEponOnuLlidTxFrames=_ZxAnEponOnuLlidTxFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,5),_ZxAnEponOnuLlidTxFrames_Type())
zxAnEponOnuLlidTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidTxFrames.setStatus(_A)
_ZxAnEponOnuLlidTxOctets_Type=Counter64
_ZxAnEponOnuLlidTxOctets_Object=MibTableColumn
zxAnEponOnuLlidTxOctets=_ZxAnEponOnuLlidTxOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,6),_ZxAnEponOnuLlidTxOctets_Type())
zxAnEponOnuLlidTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidTxOctets.setStatus(_A)
_ZxAnEponOnuLlidTxMulticastFrames_Type=Counter64
_ZxAnEponOnuLlidTxMulticastFrames_Object=MibTableColumn
zxAnEponOnuLlidTxMulticastFrames=_ZxAnEponOnuLlidTxMulticastFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,7),_ZxAnEponOnuLlidTxMulticastFrames_Type())
zxAnEponOnuLlidTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidTxMulticastFrames.setStatus(_A)
_ZxAnEponOnuLlidTxBroadcastFrames_Type=Counter64
_ZxAnEponOnuLlidTxBroadcastFrames_Object=MibTableColumn
zxAnEponOnuLlidTxBroadcastFrames=_ZxAnEponOnuLlidTxBroadcastFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,8),_ZxAnEponOnuLlidTxBroadcastFrames_Type())
zxAnEponOnuLlidTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidTxBroadcastFrames.setStatus(_A)
_ZxAnEponOnuLlidCrcErrors_Type=Counter64
_ZxAnEponOnuLlidCrcErrors_Object=MibTableColumn
zxAnEponOnuLlidCrcErrors=_ZxAnEponOnuLlidCrcErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,9),_ZxAnEponOnuLlidCrcErrors_Type())
zxAnEponOnuLlidCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidCrcErrors.setStatus(_A)
_ZxAnEponOnuLlidFecCrctedBlocks_Type=Counter64
_ZxAnEponOnuLlidFecCrctedBlocks_Object=MibTableColumn
zxAnEponOnuLlidFecCrctedBlocks=_ZxAnEponOnuLlidFecCrctedBlocks_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,10),_ZxAnEponOnuLlidFecCrctedBlocks_Type())
zxAnEponOnuLlidFecCrctedBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidFecCrctedBlocks.setStatus(_A)
_ZxAnEponOnuLlidFecUncrctedBlocks_Type=Counter64
_ZxAnEponOnuLlidFecUncrctedBlocks_Object=MibTableColumn
zxAnEponOnuLlidFecUncrctedBlocks=_ZxAnEponOnuLlidFecUncrctedBlocks_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,11),_ZxAnEponOnuLlidFecUncrctedBlocks_Type())
zxAnEponOnuLlidFecUncrctedBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidFecUncrctedBlocks.setStatus(_A)
_ZxAnEponOnuLlidMpcpRxGateFrames_Type=Counter64
_ZxAnEponOnuLlidMpcpRxGateFrames_Object=MibTableColumn
zxAnEponOnuLlidMpcpRxGateFrames=_ZxAnEponOnuLlidMpcpRxGateFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,12),_ZxAnEponOnuLlidMpcpRxGateFrames_Type())
zxAnEponOnuLlidMpcpRxGateFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidMpcpRxGateFrames.setStatus(_A)
_ZxAnEponOnuLlidMpcpRxCtrlFrames_Type=Counter64
_ZxAnEponOnuLlidMpcpRxCtrlFrames_Object=MibTableColumn
zxAnEponOnuLlidMpcpRxCtrlFrames=_ZxAnEponOnuLlidMpcpRxCtrlFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,13),_ZxAnEponOnuLlidMpcpRxCtrlFrames_Type())
zxAnEponOnuLlidMpcpRxCtrlFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidMpcpRxCtrlFrames.setStatus(_A)
_ZxAnEponOnuLlidMpcpRxRegFrames_Type=Counter64
_ZxAnEponOnuLlidMpcpRxRegFrames_Object=MibTableColumn
zxAnEponOnuLlidMpcpRxRegFrames=_ZxAnEponOnuLlidMpcpRxRegFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,14),_ZxAnEponOnuLlidMpcpRxRegFrames_Type())
zxAnEponOnuLlidMpcpRxRegFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidMpcpRxRegFrames.setStatus(_A)
_ZxAnEponOnuLlidMpcpTxCtrlFrames_Type=Counter64
_ZxAnEponOnuLlidMpcpTxCtrlFrames_Object=MibTableColumn
zxAnEponOnuLlidMpcpTxCtrlFrames=_ZxAnEponOnuLlidMpcpTxCtrlFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,15),_ZxAnEponOnuLlidMpcpTxCtrlFrames_Type())
zxAnEponOnuLlidMpcpTxCtrlFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidMpcpTxCtrlFrames.setStatus(_A)
_ZxAnEponOnuLlidMpcpTxReqFrames_Type=Counter64
_ZxAnEponOnuLlidMpcpTxReqFrames_Object=MibTableColumn
zxAnEponOnuLlidMpcpTxReqFrames=_ZxAnEponOnuLlidMpcpTxReqFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,16),_ZxAnEponOnuLlidMpcpTxReqFrames_Type())
zxAnEponOnuLlidMpcpTxReqFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidMpcpTxReqFrames.setStatus(_A)
_ZxAnEponOnuLlidMpcpTxRepFrames_Type=Counter64
_ZxAnEponOnuLlidMpcpTxRepFrames_Object=MibTableColumn
zxAnEponOnuLlidMpcpTxRepFrames=_ZxAnEponOnuLlidMpcpTxRepFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,9,2,13,1,17),_ZxAnEponOnuLlidMpcpTxRepFrames_Type())
zxAnEponOnuLlidMpcpTxRepFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuLlidMpcpTxRepFrames.setStatus(_A)
_ZxAnEponPmHistory_ObjectIdentity=ObjectIdentity
zxAnEponPmHistory=_ZxAnEponPmHistory_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,9,3))
_ZxAnEponOltVirtualIfBERStatisticHistoryTable_Object=MibTable
zxAnEponOltVirtualIfBERStatisticHistoryTable=_ZxAnEponOltVirtualIfBERStatisticHistoryTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,1))
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticHistoryTable.setStatus(_A)
_ZxAnEponOltVirtualIfBERStatisticHistoryEntry_Object=MibTableRow
zxAnEponOltVirtualIfBERStatisticHistoryEntry=_ZxAnEponOltVirtualIfBERStatisticHistoryEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,1,1))
zxAnEponOltVirtualIfBERStatisticHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticHistoryEntry.setStatus(_A)
class _ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Type.__name__=_F
_ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Object=MibTableColumn
zxAnEponOltVirtualIfBERStatisticHistoryOnuBER=_ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,1,1,1),_ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Type())
zxAnEponOltVirtualIfBERStatisticHistoryOnuBER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticHistoryOnuBER.setStatus(_A)
class _ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Type.__name__=_F
_ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Object=MibTableColumn
zxAnEponOltVirtualIfBERStatisticHistoryOnuFER=_ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,1,1,2),_ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Type())
zxAnEponOltVirtualIfBERStatisticHistoryOnuFER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltVirtualIfBERStatisticHistoryOnuFER.setStatus(_A)
_ZxAnEponOltPhyPortStatisticHistoryTable_Object=MibTable
zxAnEponOltPhyPortStatisticHistoryTable=_ZxAnEponOltPhyPortStatisticHistoryTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,2))
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticHistoryTable.setStatus(_A)
_ZxAnEponOltPhyPortStatisticHistoryEntry_Object=MibTableRow
zxAnEponOltPhyPortStatisticHistoryEntry=_ZxAnEponOltPhyPortStatisticHistoryEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,2,1))
zxAnEponOltPhyPortStatisticHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticHistoryEntry.setStatus(_A)
class _ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Type.__name__=_F
_ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Object=MibTableColumn
zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER=_ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,2,1,1),_ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Type())
zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER.setStatus(_A)
class _ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Type.__name__=_F
_ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Object=MibTableColumn
zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER=_ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,2,1,2),_ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Type())
zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER.setStatus(_A)
_ZxAnEponEtherStatsHistoryTable_Object=MibTable
zxAnEponEtherStatsHistoryTable=_ZxAnEponEtherStatsHistoryTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3))
if mibBuilder.loadTexts:zxAnEponEtherStatsHistoryTable.setStatus(_A)
_ZxAnEponEtherStatsHistoryEntry_Object=MibTableRow
zxAnEponEtherStatsHistoryEntry=_ZxAnEponEtherStatsHistoryEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1))
zxAnEponEtherStatsHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnEponEtherStatsHistoryEntry.setStatus(_A)
_ZxAnEponEtherStatsDropEventsHistory_Type=Counter32
_ZxAnEponEtherStatsDropEventsHistory_Object=MibTableColumn
zxAnEponEtherStatsDropEventsHistory=_ZxAnEponEtherStatsDropEventsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,1),_ZxAnEponEtherStatsDropEventsHistory_Type())
zxAnEponEtherStatsDropEventsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsDropEventsHistory.setStatus(_A)
_ZxAnEponEtherStatsOctetsHistory_Type=Counter32
_ZxAnEponEtherStatsOctetsHistory_Object=MibTableColumn
zxAnEponEtherStatsOctetsHistory=_ZxAnEponEtherStatsOctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,2),_ZxAnEponEtherStatsOctetsHistory_Type())
zxAnEponEtherStatsOctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsOctetsHistory.setStatus(_A)
_ZxAnEponEtherStatsPktsHistory_Type=Counter32
_ZxAnEponEtherStatsPktsHistory_Object=MibTableColumn
zxAnEponEtherStatsPktsHistory=_ZxAnEponEtherStatsPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,3),_ZxAnEponEtherStatsPktsHistory_Type())
zxAnEponEtherStatsPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPktsHistory.setStatus(_A)
_ZxAnEponEtherStatsBroadcastPktsHistory_Type=Counter32
_ZxAnEponEtherStatsBroadcastPktsHistory_Object=MibTableColumn
zxAnEponEtherStatsBroadcastPktsHistory=_ZxAnEponEtherStatsBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,4),_ZxAnEponEtherStatsBroadcastPktsHistory_Type())
zxAnEponEtherStatsBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsBroadcastPktsHistory.setStatus(_A)
_ZxAnEponEtherStatsMulticastPktsHistory_Type=Counter32
_ZxAnEponEtherStatsMulticastPktsHistory_Object=MibTableColumn
zxAnEponEtherStatsMulticastPktsHistory=_ZxAnEponEtherStatsMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,5),_ZxAnEponEtherStatsMulticastPktsHistory_Type())
zxAnEponEtherStatsMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsMulticastPktsHistory.setStatus(_A)
_ZxAnEponEtherStatsCRCAlignErrorsHistory_Type=Counter32
_ZxAnEponEtherStatsCRCAlignErrorsHistory_Object=MibTableColumn
zxAnEponEtherStatsCRCAlignErrorsHistory=_ZxAnEponEtherStatsCRCAlignErrorsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,6),_ZxAnEponEtherStatsCRCAlignErrorsHistory_Type())
zxAnEponEtherStatsCRCAlignErrorsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsCRCAlignErrorsHistory.setStatus(_A)
_ZxAnEponEtherStatsUndersizePktsHistory_Type=Counter32
_ZxAnEponEtherStatsUndersizePktsHistory_Object=MibTableColumn
zxAnEponEtherStatsUndersizePktsHistory=_ZxAnEponEtherStatsUndersizePktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,7),_ZxAnEponEtherStatsUndersizePktsHistory_Type())
zxAnEponEtherStatsUndersizePktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsUndersizePktsHistory.setStatus(_A)
_ZxAnEponEtherStatsOversizePktsHistory_Type=Counter32
_ZxAnEponEtherStatsOversizePktsHistory_Object=MibTableColumn
zxAnEponEtherStatsOversizePktsHistory=_ZxAnEponEtherStatsOversizePktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,8),_ZxAnEponEtherStatsOversizePktsHistory_Type())
zxAnEponEtherStatsOversizePktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsOversizePktsHistory.setStatus(_A)
_ZxAnEponEtherStatsFragmentsHistory_Type=Counter32
_ZxAnEponEtherStatsFragmentsHistory_Object=MibTableColumn
zxAnEponEtherStatsFragmentsHistory=_ZxAnEponEtherStatsFragmentsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,9),_ZxAnEponEtherStatsFragmentsHistory_Type())
zxAnEponEtherStatsFragmentsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsFragmentsHistory.setStatus(_A)
_ZxAnEponEtherStatsJabbersHistory_Type=Counter32
_ZxAnEponEtherStatsJabbersHistory_Object=MibTableColumn
zxAnEponEtherStatsJabbersHistory=_ZxAnEponEtherStatsJabbersHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,10),_ZxAnEponEtherStatsJabbersHistory_Type())
zxAnEponEtherStatsJabbersHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsJabbersHistory.setStatus(_A)
_ZxAnEponEtherStatsCollisionsHistory_Type=Counter32
_ZxAnEponEtherStatsCollisionsHistory_Object=MibTableColumn
zxAnEponEtherStatsCollisionsHistory=_ZxAnEponEtherStatsCollisionsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,11),_ZxAnEponEtherStatsCollisionsHistory_Type())
zxAnEponEtherStatsCollisionsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsCollisionsHistory.setStatus(_A)
_ZxAnEponEtherStatsPkts64OctetsHistory_Type=Counter32
_ZxAnEponEtherStatsPkts64OctetsHistory_Object=MibTableColumn
zxAnEponEtherStatsPkts64OctetsHistory=_ZxAnEponEtherStatsPkts64OctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,12),_ZxAnEponEtherStatsPkts64OctetsHistory_Type())
zxAnEponEtherStatsPkts64OctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts64OctetsHistory.setStatus(_A)
_ZxAnEponEtherStatsPkts65to127OctetsHistory_Type=Counter32
_ZxAnEponEtherStatsPkts65to127OctetsHistory_Object=MibTableColumn
zxAnEponEtherStatsPkts65to127OctetsHistory=_ZxAnEponEtherStatsPkts65to127OctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,13),_ZxAnEponEtherStatsPkts65to127OctetsHistory_Type())
zxAnEponEtherStatsPkts65to127OctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts65to127OctetsHistory.setStatus(_A)
_ZxAnEponEtherStatsPkts128to255OctetsHistory_Type=Counter32
_ZxAnEponEtherStatsPkts128to255OctetsHistory_Object=MibTableColumn
zxAnEponEtherStatsPkts128to255OctetsHistory=_ZxAnEponEtherStatsPkts128to255OctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,14),_ZxAnEponEtherStatsPkts128to255OctetsHistory_Type())
zxAnEponEtherStatsPkts128to255OctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts128to255OctetsHistory.setStatus(_A)
_ZxAnEponEtherStatsPkts256to511OctetsHistory_Type=Counter32
_ZxAnEponEtherStatsPkts256to511OctetsHistory_Object=MibTableColumn
zxAnEponEtherStatsPkts256to511OctetsHistory=_ZxAnEponEtherStatsPkts256to511OctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,15),_ZxAnEponEtherStatsPkts256to511OctetsHistory_Type())
zxAnEponEtherStatsPkts256to511OctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts256to511OctetsHistory.setStatus(_A)
_ZxAnEponEtherStatsPkts512to1023OctetsHistory_Type=Counter32
_ZxAnEponEtherStatsPkts512to1023OctetsHistory_Object=MibTableColumn
zxAnEponEtherStatsPkts512to1023OctetsHistory=_ZxAnEponEtherStatsPkts512to1023OctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,16),_ZxAnEponEtherStatsPkts512to1023OctetsHistory_Type())
zxAnEponEtherStatsPkts512to1023OctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts512to1023OctetsHistory.setStatus(_A)
_ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Type=Counter32
_ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Object=MibTableColumn
zxAnEponEtherStatsPkts1024to1518OctetsHistory=_ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,3,1,17),_ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Type())
zxAnEponEtherStatsPkts1024to1518OctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponEtherStatsPkts1024to1518OctetsHistory.setStatus(_A)
_ZxAnEponIfXHistoryTable_Object=MibTable
zxAnEponIfXHistoryTable=_ZxAnEponIfXHistoryTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4))
if mibBuilder.loadTexts:zxAnEponIfXHistoryTable.setStatus(_A)
_ZxAnEponIfXHistoryEntry_Object=MibTableRow
zxAnEponIfXHistoryEntry=_ZxAnEponIfXHistoryEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1))
if mibBuilder.loadTexts:zxAnEponIfXHistoryEntry.setStatus(_A)
_ZxAnEponIfInMulticastPktsHistory_Type=Counter32
_ZxAnEponIfInMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfInMulticastPktsHistory=_ZxAnEponIfInMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,1),_ZxAnEponIfInMulticastPktsHistory_Type())
zxAnEponIfInMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfInBroadcastPktsHistory_Type=Counter32
_ZxAnEponIfInBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfInBroadcastPktsHistory=_ZxAnEponIfInBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,2),_ZxAnEponIfInBroadcastPktsHistory_Type())
zxAnEponIfInBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfInBroadcastPktsHistory.setStatus(_A)
_ZxAnEponIfOutMulticastPktsHistory_Type=Counter32
_ZxAnEponIfOutMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfOutMulticastPktsHistory=_ZxAnEponIfOutMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,3),_ZxAnEponIfOutMulticastPktsHistory_Type())
zxAnEponIfOutMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfOutBroadcastPktsHistory_Type=Counter32
_ZxAnEponIfOutBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfOutBroadcastPktsHistory=_ZxAnEponIfOutBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,4),_ZxAnEponIfOutBroadcastPktsHistory_Type())
zxAnEponIfOutBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOutBroadcastPktsHistory.setStatus(_A)
_ZxAnEponIfHCInOctetsHistory_Type=Counter64
_ZxAnEponIfHCInOctetsHistory_Object=MibTableColumn
zxAnEponIfHCInOctetsHistory=_ZxAnEponIfHCInOctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,5),_ZxAnEponIfHCInOctetsHistory_Type())
zxAnEponIfHCInOctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInOctetsHistory.setStatus(_A)
_ZxAnEponIfHCInUcastPktsHistory_Type=Counter64
_ZxAnEponIfHCInUcastPktsHistory_Object=MibTableColumn
zxAnEponIfHCInUcastPktsHistory=_ZxAnEponIfHCInUcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,6),_ZxAnEponIfHCInUcastPktsHistory_Type())
zxAnEponIfHCInUcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInUcastPktsHistory.setStatus(_A)
_ZxAnEponIfHCInMulticastPktsHistory_Type=Counter64
_ZxAnEponIfHCInMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfHCInMulticastPktsHistory=_ZxAnEponIfHCInMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,7),_ZxAnEponIfHCInMulticastPktsHistory_Type())
zxAnEponIfHCInMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfHCInBroadcastPktsHistory_Type=Counter64
_ZxAnEponIfHCInBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfHCInBroadcastPktsHistory=_ZxAnEponIfHCInBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,8),_ZxAnEponIfHCInBroadcastPktsHistory_Type())
zxAnEponIfHCInBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCInBroadcastPktsHistory.setStatus(_A)
_ZxAnEponIfHCOutOctetsHistory_Type=Counter64
_ZxAnEponIfHCOutOctetsHistory_Object=MibTableColumn
zxAnEponIfHCOutOctetsHistory=_ZxAnEponIfHCOutOctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,9),_ZxAnEponIfHCOutOctetsHistory_Type())
zxAnEponIfHCOutOctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutOctetsHistory.setStatus(_A)
_ZxAnEponIfHCOutUcastPktsHistory_Type=Counter64
_ZxAnEponIfHCOutUcastPktsHistory_Object=MibTableColumn
zxAnEponIfHCOutUcastPktsHistory=_ZxAnEponIfHCOutUcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,10),_ZxAnEponIfHCOutUcastPktsHistory_Type())
zxAnEponIfHCOutUcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutUcastPktsHistory.setStatus(_A)
_ZxAnEponIfHCOutMulticastPktsHistory_Type=Counter64
_ZxAnEponIfHCOutMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfHCOutMulticastPktsHistory=_ZxAnEponIfHCOutMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,11),_ZxAnEponIfHCOutMulticastPktsHistory_Type())
zxAnEponIfHCOutMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfHCOutBroadcastPktsHistory_Type=Counter64
_ZxAnEponIfHCOutBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfHCOutBroadcastPktsHistory=_ZxAnEponIfHCOutBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,4,1,12),_ZxAnEponIfHCOutBroadcastPktsHistory_Type())
zxAnEponIfHCOutBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfHCOutBroadcastPktsHistory.setStatus(_A)
_ZxAnEponIfXOltHistoryTable_Object=MibTable
zxAnEponIfXOltHistoryTable=_ZxAnEponIfXOltHistoryTable_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5))
if mibBuilder.loadTexts:zxAnEponIfXOltHistoryTable.setStatus(_A)
_ZxAnEponIfXOltHistoryEntry_Object=MibTableRow
zxAnEponIfXOltHistoryEntry=_ZxAnEponIfXOltHistoryEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1))
if mibBuilder.loadTexts:zxAnEponIfXOltHistoryEntry.setStatus(_A)
_ZxAnEponIfOltInMulticastPktsHistory_Type=Counter32
_ZxAnEponIfOltInMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfOltInMulticastPktsHistory=_ZxAnEponIfOltInMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,1),_ZxAnEponIfOltInMulticastPktsHistory_Type())
zxAnEponIfOltInMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltInMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfOltInBroadcastPktsHistory_Type=Counter32
_ZxAnEponIfOltInBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfOltInBroadcastPktsHistory=_ZxAnEponIfOltInBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,2),_ZxAnEponIfOltInBroadcastPktsHistory_Type())
zxAnEponIfOltInBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltInBroadcastPktsHistory.setStatus(_A)
_ZxAnEponIfOltOutMulticastPktsHistory_Type=Counter32
_ZxAnEponIfOltOutMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfOltOutMulticastPktsHistory=_ZxAnEponIfOltOutMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,3),_ZxAnEponIfOltOutMulticastPktsHistory_Type())
zxAnEponIfOltOutMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltOutMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfOltOutBroadcastPktsHistory_Type=Counter32
_ZxAnEponIfOltOutBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfOltOutBroadcastPktsHistory=_ZxAnEponIfOltOutBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,4),_ZxAnEponIfOltOutBroadcastPktsHistory_Type())
zxAnEponIfOltOutBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltOutBroadcastPktsHistory.setStatus(_A)
_ZxAnEponIfOltHCInOctetsHistory_Type=Counter64
_ZxAnEponIfOltHCInOctetsHistory_Object=MibTableColumn
zxAnEponIfOltHCInOctetsHistory=_ZxAnEponIfOltHCInOctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,5),_ZxAnEponIfOltHCInOctetsHistory_Type())
zxAnEponIfOltHCInOctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInOctetsHistory.setStatus(_A)
_ZxAnEponIfOltHCInUcastPktsHistory_Type=Counter64
_ZxAnEponIfOltHCInUcastPktsHistory_Object=MibTableColumn
zxAnEponIfOltHCInUcastPktsHistory=_ZxAnEponIfOltHCInUcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,6),_ZxAnEponIfOltHCInUcastPktsHistory_Type())
zxAnEponIfOltHCInUcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInUcastPktsHistory.setStatus(_A)
_ZxAnEponIfOltHCInMulticastPktsHistory_Type=Counter64
_ZxAnEponIfOltHCInMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfOltHCInMulticastPktsHistory=_ZxAnEponIfOltHCInMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,7),_ZxAnEponIfOltHCInMulticastPktsHistory_Type())
zxAnEponIfOltHCInMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfOltHCInBroadcastPktsHistory_Type=Counter64
_ZxAnEponIfOltHCInBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfOltHCInBroadcastPktsHistory=_ZxAnEponIfOltHCInBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,8),_ZxAnEponIfOltHCInBroadcastPktsHistory_Type())
zxAnEponIfOltHCInBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCInBroadcastPktsHistory.setStatus(_A)
_ZxAnEponIfOltHCOutOctetsHistory_Type=Counter64
_ZxAnEponIfOltHCOutOctetsHistory_Object=MibTableColumn
zxAnEponIfOltHCOutOctetsHistory=_ZxAnEponIfOltHCOutOctetsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,9),_ZxAnEponIfOltHCOutOctetsHistory_Type())
zxAnEponIfOltHCOutOctetsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutOctetsHistory.setStatus(_A)
_ZxAnEponIfOltHCOutUcastPktsHistory_Type=Counter64
_ZxAnEponIfOltHCOutUcastPktsHistory_Object=MibTableColumn
zxAnEponIfOltHCOutUcastPktsHistory=_ZxAnEponIfOltHCOutUcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,10),_ZxAnEponIfOltHCOutUcastPktsHistory_Type())
zxAnEponIfOltHCOutUcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutUcastPktsHistory.setStatus(_A)
_ZxAnEponIfOltHCOutMulticastPktsHistory_Type=Counter64
_ZxAnEponIfOltHCOutMulticastPktsHistory_Object=MibTableColumn
zxAnEponIfOltHCOutMulticastPktsHistory=_ZxAnEponIfOltHCOutMulticastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,11),_ZxAnEponIfOltHCOutMulticastPktsHistory_Type())
zxAnEponIfOltHCOutMulticastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutMulticastPktsHistory.setStatus(_A)
_ZxAnEponIfOltHCOutBroadcastPktsHistory_Type=Counter64
_ZxAnEponIfOltHCOutBroadcastPktsHistory_Object=MibTableColumn
zxAnEponIfOltHCOutBroadcastPktsHistory=_ZxAnEponIfOltHCOutBroadcastPktsHistory_Object((1,3,6,1,4,1,3902,1015,1010,1,9,3,5,1,12),_ZxAnEponIfOltHCOutBroadcastPktsHistory_Type())
zxAnEponIfOltHCOutBroadcastPktsHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIfOltHCOutBroadcastPktsHistory.setStatus(_A)
zxAnEponIfEntry.registerAugmentions((_G,_R))
zxAnEponIfXEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())
zxAnEponIfEntry.registerAugmentions((_G,_S))
zxAnEponIfXOltEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())
zxAnEponIfCurrentEntry.registerAugmentions((_G,_T))
zxAnEponIfXCurrentEntry.setIndexNames(*zxAnEponIfCurrentEntry.getIndexNames())
zxAnEponIfEntry.registerAugmentions((_G,_U))
zxAnEponIfXHistoryEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())
zxAnEponIfEntry.registerAugmentions((_G,_V))
zxAnEponIfXOltHistoryEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{'zxAnEponPm':zxAnEponPm,'zxAnEponPmInfor':zxAnEponPmInfor,'zxAnEponOltVirtualIfBERStatisticTable':zxAnEponOltVirtualIfBERStatisticTable,'zxAnEponOltVirtualIfBERStatisticEntry':zxAnEponOltVirtualIfBERStatisticEntry,'zxAnEponOltVirtualIfBERStatisticOnuBER':zxAnEponOltVirtualIfBERStatisticOnuBER,'zxAnEponOltVirtualIfBERStatisticOnuFER':zxAnEponOltVirtualIfBERStatisticOnuFER,'zxAnEponOltPhyPortStatisticTable':zxAnEponOltPhyPortStatisticTable,'zxAnEponOltPhyPortStatisticEntry':zxAnEponOltPhyPortStatisticEntry,'zxAnEponOltPhyPortStatisticOltPonAverageBER':zxAnEponOltPhyPortStatisticOltPonAverageBER,'zxAnEponOltPhyPortStatisticOltSysAverageBER':zxAnEponOltPhyPortStatisticOltSysAverageBER,'zxAnEponEtherStatsTable':zxAnEponEtherStatsTable,'zxAnEponEtherStatsEntry':zxAnEponEtherStatsEntry,'zxAnEponEtherStatsDropEvents':zxAnEponEtherStatsDropEvents,'zxAnEponEtherStatsOctets':zxAnEponEtherStatsOctets,'zxAnEponEtherStatsPkts':zxAnEponEtherStatsPkts,'zxAnEponEtherStatsBroadcastPkts':zxAnEponEtherStatsBroadcastPkts,'zxAnEponEtherStatsMulticastPkts':zxAnEponEtherStatsMulticastPkts,'zxAnEponEtherStatsCRCAlignErrors':zxAnEponEtherStatsCRCAlignErrors,'zxAnEponEtherStatsUndersizePkts':zxAnEponEtherStatsUndersizePkts,'zxAnEponEtherStatsOversizePkts':zxAnEponEtherStatsOversizePkts,'zxAnEponEtherStatsFragments':zxAnEponEtherStatsFragments,'zxAnEponEtherStatsJabbers':zxAnEponEtherStatsJabbers,'zxAnEponEtherStatsCollisions':zxAnEponEtherStatsCollisions,'zxAnEponEtherStatsPkts64Octets':zxAnEponEtherStatsPkts64Octets,'zxAnEponEtherStatsPkts65to127Octets':zxAnEponEtherStatsPkts65to127Octets,'zxAnEponEtherStatsPkts128to255Octets':zxAnEponEtherStatsPkts128to255Octets,'zxAnEponEtherStatsPkts256to511Octets':zxAnEponEtherStatsPkts256to511Octets,'zxAnEponEtherStatsPkts512to1023Octets':zxAnEponEtherStatsPkts512to1023Octets,'zxAnEponEtherStatsPkts1024to1518Octets':zxAnEponEtherStatsPkts1024to1518Octets,'zxAnEponIfTable':zxAnEponIfTable,'zxAnEponIfEntry':zxAnEponIfEntry,'zxAnEponIfInOctets':zxAnEponIfInOctets,'zxAnEponIfInUcastPkts':zxAnEponIfInUcastPkts,'zxAnEponIfInNUcastPkts':zxAnEponIfInNUcastPkts,'zxAnEponIfInDiscards':zxAnEponIfInDiscards,'zxAnEponIfInErrors':zxAnEponIfInErrors,'zxAnEponIfInUnknownProtos':zxAnEponIfInUnknownProtos,'zxAnEponIfOutOctets':zxAnEponIfOutOctets,'zxAnEponIfOutUcastPkts':zxAnEponIfOutUcastPkts,'zxAnEponIfOutNUcastPkts':zxAnEponIfOutNUcastPkts,'zxAnEponIfOutDiscards':zxAnEponIfOutDiscards,'zxAnEponIfOutErrors':zxAnEponIfOutErrors,'zxAnEponIfXTable':zxAnEponIfXTable,_R:zxAnEponIfXEntry,'zxAnEponIfInMulticastPkts':zxAnEponIfInMulticastPkts,'zxAnEponIfInBroadcastPkts':zxAnEponIfInBroadcastPkts,'zxAnEponIfOutMulticastPkts':zxAnEponIfOutMulticastPkts,'zxAnEponIfOutBroadcastPkts':zxAnEponIfOutBroadcastPkts,'zxAnEponIfHCInOctets':zxAnEponIfHCInOctets,'zxAnEponIfHCInUcastPkts':zxAnEponIfHCInUcastPkts,'zxAnEponIfHCInMulticastPkts':zxAnEponIfHCInMulticastPkts,'zxAnEponIfHCInBroadcastPkts':zxAnEponIfHCInBroadcastPkts,'zxAnEponIfHCOutOctets':zxAnEponIfHCOutOctets,'zxAnEponIfHCOutUcastPkts':zxAnEponIfHCOutUcastPkts,'zxAnEponIfHCOutMulticastPkts':zxAnEponIfHCOutMulticastPkts,'zxAnEponIfHCOutBroadcastPkts':zxAnEponIfHCOutBroadcastPkts,'zxAnEponDot3PauseTable':zxAnEponDot3PauseTable,'zxAnEponDot3PauseEntry':zxAnEponDot3PauseEntry,'zxAnEponDot3InPauseFrames':zxAnEponDot3InPauseFrames,'zxAnEponDot3OutPauseFrames':zxAnEponDot3OutPauseFrames,'zxAnEponDot3HCInPauseFrames':zxAnEponDot3HCInPauseFrames,'zxAnEponDot3HCOutPauseFrames':zxAnEponDot3HCOutPauseFrames,'zxAnEponDot3HCStatsTable':zxAnEponDot3HCStatsTable,'zxAnEponDot3HCStatsEntry':zxAnEponDot3HCStatsEntry,'zxAnEponDot3HCStatsAlignmentErrors':zxAnEponDot3HCStatsAlignmentErrors,'zxAnEponDot3HCStatsFCSErrors':zxAnEponDot3HCStatsFCSErrors,'zxAnEponDot3HCStatsInternalMacTransmitErrors':zxAnEponDot3HCStatsInternalMacTransmitErrors,'zxAnEponDot3HCStatsFrameTooLongs':zxAnEponDot3HCStatsFrameTooLongs,'zxAnEponDot3HCStatsInternalMacReceiveErrors':zxAnEponDot3HCStatsInternalMacReceiveErrors,'zxAnEponDot3HCStatsSymbolErrors':zxAnEponDot3HCStatsSymbolErrors,'zxAnEponIfXOltTable':zxAnEponIfXOltTable,_S:zxAnEponIfXOltEntry,'zxAnEponIfOltInMulticastPkts':zxAnEponIfOltInMulticastPkts,'zxAnEponIfOltInBroadcastPkts':zxAnEponIfOltInBroadcastPkts,'zxAnEponIfOltOutMulticastPkts':zxAnEponIfOltOutMulticastPkts,'zxAnEponIfOltOutBroadcastPkts':zxAnEponIfOltOutBroadcastPkts,'zxAnEponIfOltHCInOctets':zxAnEponIfOltHCInOctets,'zxAnEponIfOltHCInUcastPkts':zxAnEponIfOltHCInUcastPkts,'zxAnEponIfOltHCInMulticastPkts':zxAnEponIfOltHCInMulticastPkts,'zxAnEponIfOltHCInBroadcastPkts':zxAnEponIfOltHCInBroadcastPkts,'zxAnEponIfOltHCOutOctets':zxAnEponIfOltHCOutOctets,'zxAnEponIfOltHCOutUcastPkts':zxAnEponIfOltHCOutUcastPkts,'zxAnEponIfOltHCOutMulticastPkts':zxAnEponIfOltHCOutMulticastPkts,'zxAnEponIfOltHCOutBroadcastPkts':zxAnEponIfOltHCOutBroadcastPkts,'zxAnEponPmCurrent':zxAnEponPmCurrent,'zxAnEponDot3MpcpStatCurrentTable':zxAnEponDot3MpcpStatCurrentTable,'zxAnEponDot3MpcpStatCurrentEntry':zxAnEponDot3MpcpStatCurrentEntry,'zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent':zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent,'zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent':zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent,'zxAnEponDot3MpcpDiscoveryWindowsSentCurrent':zxAnEponDot3MpcpDiscoveryWindowsSentCurrent,'zxAnEponDot3MpcpDiscoveryTimeoutCurrent':zxAnEponDot3MpcpDiscoveryTimeoutCurrent,'zxAnEponDot3MpcpTxRegRequestCurrent':zxAnEponDot3MpcpTxRegRequestCurrent,'zxAnEponDot3MpcpRxRegRequestCurrent':zxAnEponDot3MpcpRxRegRequestCurrent,'zxAnEponDot3MpcpTxRegAckCurrent':zxAnEponDot3MpcpTxRegAckCurrent,'zxAnEponDot3MpcpRxRegAckCurrent':zxAnEponDot3MpcpRxRegAckCurrent,'zxAnEponDot3MpcpTxReportCurrent':zxAnEponDot3MpcpTxReportCurrent,'zxAnEponDot3MpcpRxReportCurrent':zxAnEponDot3MpcpRxReportCurrent,'zxAnEponDot3MpcpTxGateCurrent':zxAnEponDot3MpcpTxGateCurrent,'zxAnEponDot3MpcpRxGateCurrent':zxAnEponDot3MpcpRxGateCurrent,'zxAnEponDot3MpcpTxRegisterCurrent':zxAnEponDot3MpcpTxRegisterCurrent,'zxAnEponDot3MpcpRxRegisterCurrent':zxAnEponDot3MpcpRxRegisterCurrent,'zxAnEponDot3OmpEmulationStatCurrentTable':zxAnEponDot3OmpEmulationStatCurrentTable,'zxAnEponDot3OmpEmulationStatCurrentEntry':zxAnEponDot3OmpEmulationStatCurrentEntry,'zxAnEponDot3OmpEmulationSLDErrorsCurrent':zxAnEponDot3OmpEmulationSLDErrorsCurrent,'zxAnEponDot3OmpEmulationCRC8ErrorsCurrent':zxAnEponDot3OmpEmulationCRC8ErrorsCurrent,'zxAnEponDot3OmpEmulationBadLLIDCurrent':zxAnEponDot3OmpEmulationBadLLIDCurrent,'zxAnEponDot3OmpEmulationGoodLLIDCurrent':zxAnEponDot3OmpEmulationGoodLLIDCurrent,'zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent':zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent,'zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent':zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent,'zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent':zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent,'zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent':zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent,'zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent':zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent,'zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent':zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent,'zxAnEponDot3EponFecCurrentTable':zxAnEponDot3EponFecCurrentTable,'zxAnEponDot3EponFecCurrentEntry':zxAnEponDot3EponFecCurrentEntry,'zxAnEponDot3EponFecPCSCodingViolationCurrent':zxAnEponDot3EponFecPCSCodingViolationCurrent,'zxAnEponDot3EponFecAbilityCurrent':zxAnEponDot3EponFecAbilityCurrent,'zxAnEponDot3EponFecModeCurrent':zxAnEponDot3EponFecModeCurrent,'zxAnEponDot3EponFecCorrectedBlocksCurrent':zxAnEponDot3EponFecCorrectedBlocksCurrent,'zxAnEponDot3EponFecUncorrectableBlocksCurrent':zxAnEponDot3EponFecUncorrectableBlocksCurrent,'zxAnEponDot3EponFecBufferHeadCodingViolationCurrent':zxAnEponDot3EponFecBufferHeadCodingViolationCurrent,'zxAnEponDot3ExtPkgQueueCurrentTable':zxAnEponDot3ExtPkgQueueCurrentTable,'zxAnEponDot3ExtPkgQueueCurrentEntry':zxAnEponDot3ExtPkgQueueCurrentEntry,_P:zxAnEponDot3QueueIndexCurrent,'zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent':zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent,'zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent':zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent,'zxAnEponDot3ExtPkgStatTxFramesQueueCurrent':zxAnEponDot3ExtPkgStatTxFramesQueueCurrent,'zxAnEponDot3ExtPkgStatRxFramesQueueCurrent':zxAnEponDot3ExtPkgStatRxFramesQueueCurrent,'zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent':zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent,'zxAnEponDot3OamStatsCurrentTable':zxAnEponDot3OamStatsCurrentTable,'zxAnEponDot3OamStatsCurrentEntry':zxAnEponDot3OamStatsCurrentEntry,'zxAnEponDot3OamInformationTxCurrent':zxAnEponDot3OamInformationTxCurrent,'zxAnEponDot3OamInformationRxCurrent':zxAnEponDot3OamInformationRxCurrent,'zxAnEponDot3OamUniqueEventNotificationTxCurrent':zxAnEponDot3OamUniqueEventNotificationTxCurrent,'zxAnEponDot3OamUniqueEventNotificationRxCurrent':zxAnEponDot3OamUniqueEventNotificationRxCurrent,'zxAnEponDot3OamDuplicateEventNotificationTxCurrent':zxAnEponDot3OamDuplicateEventNotificationTxCurrent,'zxAnEponDot3OamDuplicateEventNotificationRxCurrent':zxAnEponDot3OamDuplicateEventNotificationRxCurrent,'zxAnEponDot3OamLoopbackControlTxCurrent':zxAnEponDot3OamLoopbackControlTxCurrent,'zxAnEponDot3OamLoopbackControlRxCurrent':zxAnEponDot3OamLoopbackControlRxCurrent,'zxAnEponDot3OamVariableRequestTxCurrent':zxAnEponDot3OamVariableRequestTxCurrent,'zxAnEponDot3OamVariableRequestRxCurrent':zxAnEponDot3OamVariableRequestRxCurrent,'zxAnEponDot3OamVariableResponseTxCurrent':zxAnEponDot3OamVariableResponseTxCurrent,'zxAnEponDot3OamVariableResponseRxCurrent':zxAnEponDot3OamVariableResponseRxCurrent,'zxAnEponDot3OamOrgSpecificTxCurrent':zxAnEponDot3OamOrgSpecificTxCurrent,'zxAnEponDot3OamOrgSpecificRxCurrent':zxAnEponDot3OamOrgSpecificRxCurrent,'zxAnEponDot3OamUnsupportedCodesTxCurrent':zxAnEponDot3OamUnsupportedCodesTxCurrent,'zxAnEponDot3OamUnsupportedCodesRxCurrent':zxAnEponDot3OamUnsupportedCodesRxCurrent,'zxAnEponDot3OamFramesLostDueToOamCurrent':zxAnEponDot3OamFramesLostDueToOamCurrent,'zxAnEponOltVirtualIfBERStatisticCurrentTable':zxAnEponOltVirtualIfBERStatisticCurrentTable,'zxAnEponOltVirtualIfBERStatisticCurrentEntry':zxAnEponOltVirtualIfBERStatisticCurrentEntry,'zxAnEponOltVirtualIfBERStatisticOnuBERCurrent':zxAnEponOltVirtualIfBERStatisticOnuBERCurrent,'zxAnEponOltVirtualIfBERStatisticOnuFERCurrent':zxAnEponOltVirtualIfBERStatisticOnuFERCurrent,'zxAnEponOltPhyPortStatisticCurrentTable':zxAnEponOltPhyPortStatisticCurrentTable,'zxAnEponOltPhyPortStatisticCurrentEntry':zxAnEponOltPhyPortStatisticCurrentEntry,'zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent':zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent,'zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent':zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent,'zxAnEponEtherStatsCurrentTable':zxAnEponEtherStatsCurrentTable,'zxAnEponEtherStatsCurrentEntry':zxAnEponEtherStatsCurrentEntry,'zxAnEponEtherStatsDropEventsCurrent':zxAnEponEtherStatsDropEventsCurrent,'zxAnEponEtherStatsOctetsCurrent':zxAnEponEtherStatsOctetsCurrent,'zxAnEponEtherStatsPktsCurrent':zxAnEponEtherStatsPktsCurrent,'zxAnEponEtherStatsBroadcastPktsCurrent':zxAnEponEtherStatsBroadcastPktsCurrent,'zxAnEponEtherStatsMulticastPktsCurrent':zxAnEponEtherStatsMulticastPktsCurrent,'zxAnEponEtherStatsCRCAlignErrorsCurrent':zxAnEponEtherStatsCRCAlignErrorsCurrent,'zxAnEponEtherStatsUndersizePktsCurrent':zxAnEponEtherStatsUndersizePktsCurrent,'zxAnEponEtherStatsOversizePktsCurrent':zxAnEponEtherStatsOversizePktsCurrent,'zxAnEponEtherStatsFragmentsCurrent':zxAnEponEtherStatsFragmentsCurrent,'zxAnEponEtherStatsJabbersCurrent':zxAnEponEtherStatsJabbersCurrent,'zxAnEponEtherStatsCollisionsCurrent':zxAnEponEtherStatsCollisionsCurrent,'zxAnEponEtherStatsPkts64OctetsCurrent':zxAnEponEtherStatsPkts64OctetsCurrent,'zxAnEponEtherStatsPkts65to127OctetsCurrent':zxAnEponEtherStatsPkts65to127OctetsCurrent,'zxAnEponEtherStatsPkts128to255OctetsCurrent':zxAnEponEtherStatsPkts128to255OctetsCurrent,'zxAnEponEtherStatsPkts256to511OctetsCurrent':zxAnEponEtherStatsPkts256to511OctetsCurrent,'zxAnEponEtherStatsPkts512to1023OctetsCurrent':zxAnEponEtherStatsPkts512to1023OctetsCurrent,'zxAnEponEtherStatsPkts1024to1518OctetsCurrent':zxAnEponEtherStatsPkts1024to1518OctetsCurrent,'zxAnEponEtherStatsOwnerCurrent':zxAnEponEtherStatsOwnerCurrent,'zxAnEponEtherStatsStatusCurrent':zxAnEponEtherStatsStatusCurrent,'zxAnEponIfCurrentTable':zxAnEponIfCurrentTable,'zxAnEponIfCurrentEntry':zxAnEponIfCurrentEntry,'zxAnEponIfInOctetsCurrent':zxAnEponIfInOctetsCurrent,'zxAnEponIfInUcastPktsCurrent':zxAnEponIfInUcastPktsCurrent,'zxAnEponIfInNUcastPktsCurrent':zxAnEponIfInNUcastPktsCurrent,'zxAnEponIfInDiscardsCurrent':zxAnEponIfInDiscardsCurrent,'zxAnEponIfInErrorsCurrent':zxAnEponIfInErrorsCurrent,'zxAnEponIfInUnknownProtosCurrent':zxAnEponIfInUnknownProtosCurrent,'zxAnEponIfOutOctetsCurrent':zxAnEponIfOutOctetsCurrent,'zxAnEponIfOutUcastPktsCurrent':zxAnEponIfOutUcastPktsCurrent,'zxAnEponIfOutNUcastPktsCurrent':zxAnEponIfOutNUcastPktsCurrent,'zxAnEponIfOutDiscardsCurrent':zxAnEponIfOutDiscardsCurrent,'zxAnEponIfOutErrorsCurrent':zxAnEponIfOutErrorsCurrent,'zxAnEponIfXCurrentTable':zxAnEponIfXCurrentTable,_T:zxAnEponIfXCurrentEntry,'zxAnEponIfInMulticastPktsCurrent':zxAnEponIfInMulticastPktsCurrent,'zxAnEponIfInBroadcastPktsCurrent':zxAnEponIfInBroadcastPktsCurrent,'zxAnEponIfOutMulticastPktsCurrent':zxAnEponIfOutMulticastPktsCurrent,'zxAnEponIfOutBroadcastPktsCurrent':zxAnEponIfOutBroadcastPktsCurrent,'zxAnEponIfHCInOctetsCurrent':zxAnEponIfHCInOctetsCurrent,'zxAnEponIfHCInUcastPktsCurrent':zxAnEponIfHCInUcastPktsCurrent,'zxAnEponIfHCInMulticastPktsCurrent':zxAnEponIfHCInMulticastPktsCurrent,'zxAnEponIfHCInBroadcastPktsCurrent':zxAnEponIfHCInBroadcastPktsCurrent,'zxAnEponIfHCOutOctetsCurrent':zxAnEponIfHCOutOctetsCurrent,'zxAnEponIfHCOutUcastPktsCurrent':zxAnEponIfHCOutUcastPktsCurrent,'zxAnEponIfHCOutMulticastPktsCurrent':zxAnEponIfHCOutMulticastPktsCurrent,'zxAnEponIfHCOutBroadcastPktsCurrent':zxAnEponIfHCOutBroadcastPktsCurrent,'zxAnEponDot3PauseCurrentTable':zxAnEponDot3PauseCurrentTable,'zxAnEponDot3PauseCurrentEntry':zxAnEponDot3PauseCurrentEntry,'zxAnEponDot3InPauseFramesCurrent':zxAnEponDot3InPauseFramesCurrent,'zxAnEponDot3OutPauseFramesCurrent':zxAnEponDot3OutPauseFramesCurrent,'zxAnEponDot3HCInPauseFramesCurrent':zxAnEponDot3HCInPauseFramesCurrent,'zxAnEponDot3HCOutPauseFramesCurrent':zxAnEponDot3HCOutPauseFramesCurrent,'zxAnEponDot3HCStatsCurrentTable':zxAnEponDot3HCStatsCurrentTable,'zxAnEponDot3HCStatsCurrentEntry':zxAnEponDot3HCStatsCurrentEntry,'zxAnEponDot3HCStatsAlignmentErrorsCurrent':zxAnEponDot3HCStatsAlignmentErrorsCurrent,'zxAnEponDot3HCStatsFCSErrorsCurrent':zxAnEponDot3HCStatsFCSErrorsCurrent,'zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent':zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent,'zxAnEponDot3HCStatsFrameTooLongsCurrent':zxAnEponDot3HCStatsFrameTooLongsCurrent,'zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent':zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent,'zxAnEponDot3HCStatsSymbolErrorsCurrent':zxAnEponDot3HCStatsSymbolErrorsCurrent,'zxAnEponOnuLlidStatTable':zxAnEponOnuLlidStatTable,'zxAnEponOnuLlidStatEntry':zxAnEponOnuLlidStatEntry,'zxAnEponOnuLlidRxFrames':zxAnEponOnuLlidRxFrames,'zxAnEponOnuLlidRxOctets':zxAnEponOnuLlidRxOctets,'zxAnEponOnuLlidRxMulticastFrames':zxAnEponOnuLlidRxMulticastFrames,'zxAnEponOnuLlidRxBroadcastFrames':zxAnEponOnuLlidRxBroadcastFrames,'zxAnEponOnuLlidTxFrames':zxAnEponOnuLlidTxFrames,'zxAnEponOnuLlidTxOctets':zxAnEponOnuLlidTxOctets,'zxAnEponOnuLlidTxMulticastFrames':zxAnEponOnuLlidTxMulticastFrames,'zxAnEponOnuLlidTxBroadcastFrames':zxAnEponOnuLlidTxBroadcastFrames,'zxAnEponOnuLlidCrcErrors':zxAnEponOnuLlidCrcErrors,'zxAnEponOnuLlidFecCrctedBlocks':zxAnEponOnuLlidFecCrctedBlocks,'zxAnEponOnuLlidFecUncrctedBlocks':zxAnEponOnuLlidFecUncrctedBlocks,'zxAnEponOnuLlidMpcpRxGateFrames':zxAnEponOnuLlidMpcpRxGateFrames,'zxAnEponOnuLlidMpcpRxCtrlFrames':zxAnEponOnuLlidMpcpRxCtrlFrames,'zxAnEponOnuLlidMpcpRxRegFrames':zxAnEponOnuLlidMpcpRxRegFrames,'zxAnEponOnuLlidMpcpTxCtrlFrames':zxAnEponOnuLlidMpcpTxCtrlFrames,'zxAnEponOnuLlidMpcpTxReqFrames':zxAnEponOnuLlidMpcpTxReqFrames,'zxAnEponOnuLlidMpcpTxRepFrames':zxAnEponOnuLlidMpcpTxRepFrames,'zxAnEponPmHistory':zxAnEponPmHistory,'zxAnEponOltVirtualIfBERStatisticHistoryTable':zxAnEponOltVirtualIfBERStatisticHistoryTable,'zxAnEponOltVirtualIfBERStatisticHistoryEntry':zxAnEponOltVirtualIfBERStatisticHistoryEntry,'zxAnEponOltVirtualIfBERStatisticHistoryOnuBER':zxAnEponOltVirtualIfBERStatisticHistoryOnuBER,'zxAnEponOltVirtualIfBERStatisticHistoryOnuFER':zxAnEponOltVirtualIfBERStatisticHistoryOnuFER,'zxAnEponOltPhyPortStatisticHistoryTable':zxAnEponOltPhyPortStatisticHistoryTable,'zxAnEponOltPhyPortStatisticHistoryEntry':zxAnEponOltPhyPortStatisticHistoryEntry,'zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER':zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER,'zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER':zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER,'zxAnEponEtherStatsHistoryTable':zxAnEponEtherStatsHistoryTable,'zxAnEponEtherStatsHistoryEntry':zxAnEponEtherStatsHistoryEntry,'zxAnEponEtherStatsDropEventsHistory':zxAnEponEtherStatsDropEventsHistory,'zxAnEponEtherStatsOctetsHistory':zxAnEponEtherStatsOctetsHistory,'zxAnEponEtherStatsPktsHistory':zxAnEponEtherStatsPktsHistory,'zxAnEponEtherStatsBroadcastPktsHistory':zxAnEponEtherStatsBroadcastPktsHistory,'zxAnEponEtherStatsMulticastPktsHistory':zxAnEponEtherStatsMulticastPktsHistory,'zxAnEponEtherStatsCRCAlignErrorsHistory':zxAnEponEtherStatsCRCAlignErrorsHistory,'zxAnEponEtherStatsUndersizePktsHistory':zxAnEponEtherStatsUndersizePktsHistory,'zxAnEponEtherStatsOversizePktsHistory':zxAnEponEtherStatsOversizePktsHistory,'zxAnEponEtherStatsFragmentsHistory':zxAnEponEtherStatsFragmentsHistory,'zxAnEponEtherStatsJabbersHistory':zxAnEponEtherStatsJabbersHistory,'zxAnEponEtherStatsCollisionsHistory':zxAnEponEtherStatsCollisionsHistory,'zxAnEponEtherStatsPkts64OctetsHistory':zxAnEponEtherStatsPkts64OctetsHistory,'zxAnEponEtherStatsPkts65to127OctetsHistory':zxAnEponEtherStatsPkts65to127OctetsHistory,'zxAnEponEtherStatsPkts128to255OctetsHistory':zxAnEponEtherStatsPkts128to255OctetsHistory,'zxAnEponEtherStatsPkts256to511OctetsHistory':zxAnEponEtherStatsPkts256to511OctetsHistory,'zxAnEponEtherStatsPkts512to1023OctetsHistory':zxAnEponEtherStatsPkts512to1023OctetsHistory,'zxAnEponEtherStatsPkts1024to1518OctetsHistory':zxAnEponEtherStatsPkts1024to1518OctetsHistory,'zxAnEponIfXHistoryTable':zxAnEponIfXHistoryTable,_U:zxAnEponIfXHistoryEntry,'zxAnEponIfInMulticastPktsHistory':zxAnEponIfInMulticastPktsHistory,'zxAnEponIfInBroadcastPktsHistory':zxAnEponIfInBroadcastPktsHistory,'zxAnEponIfOutMulticastPktsHistory':zxAnEponIfOutMulticastPktsHistory,'zxAnEponIfOutBroadcastPktsHistory':zxAnEponIfOutBroadcastPktsHistory,'zxAnEponIfHCInOctetsHistory':zxAnEponIfHCInOctetsHistory,'zxAnEponIfHCInUcastPktsHistory':zxAnEponIfHCInUcastPktsHistory,'zxAnEponIfHCInMulticastPktsHistory':zxAnEponIfHCInMulticastPktsHistory,'zxAnEponIfHCInBroadcastPktsHistory':zxAnEponIfHCInBroadcastPktsHistory,'zxAnEponIfHCOutOctetsHistory':zxAnEponIfHCOutOctetsHistory,'zxAnEponIfHCOutUcastPktsHistory':zxAnEponIfHCOutUcastPktsHistory,'zxAnEponIfHCOutMulticastPktsHistory':zxAnEponIfHCOutMulticastPktsHistory,'zxAnEponIfHCOutBroadcastPktsHistory':zxAnEponIfHCOutBroadcastPktsHistory,'zxAnEponIfXOltHistoryTable':zxAnEponIfXOltHistoryTable,_V:zxAnEponIfXOltHistoryEntry,'zxAnEponIfOltInMulticastPktsHistory':zxAnEponIfOltInMulticastPktsHistory,'zxAnEponIfOltInBroadcastPktsHistory':zxAnEponIfOltInBroadcastPktsHistory,'zxAnEponIfOltOutMulticastPktsHistory':zxAnEponIfOltOutMulticastPktsHistory,'zxAnEponIfOltOutBroadcastPktsHistory':zxAnEponIfOltOutBroadcastPktsHistory,'zxAnEponIfOltHCInOctetsHistory':zxAnEponIfOltHCInOctetsHistory,'zxAnEponIfOltHCInUcastPktsHistory':zxAnEponIfOltHCInUcastPktsHistory,'zxAnEponIfOltHCInMulticastPktsHistory':zxAnEponIfOltHCInMulticastPktsHistory,'zxAnEponIfOltHCInBroadcastPktsHistory':zxAnEponIfOltHCInBroadcastPktsHistory,'zxAnEponIfOltHCOutOctetsHistory':zxAnEponIfOltHCOutOctetsHistory,'zxAnEponIfOltHCOutUcastPktsHistory':zxAnEponIfOltHCOutUcastPktsHistory,'zxAnEponIfOltHCOutMulticastPktsHistory':zxAnEponIfOltHCOutMulticastPktsHistory,'zxAnEponIfOltHCOutBroadcastPktsHistory':zxAnEponIfOltHCOutBroadcastPktsHistory})