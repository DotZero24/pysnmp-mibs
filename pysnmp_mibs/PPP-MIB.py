_H='read-create'
_G='nnbundleId'
_F='BUNDLE-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nnbundleId,=mibBuilder.importSymbols(_F,_G)
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
nnpppMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,14))
if mibBuilder.loadTexts:nnpppMib.setRevisions(('1900-02-01 00:00',))
_NnpppTable_Object=MibTable
nnpppTable=_NnpppTable_Object((1,3,6,1,4,1,562,73,1,1,1,14,1))
if mibBuilder.loadTexts:nnpppTable.setStatus(_A)
_NnpppTableEntry_Object=MibTableRow
nnpppTableEntry=_NnpppTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1))
nnpppTableEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nnpppTableEntry.setStatus(_A)
class _NnpppMtu_Type(DisplayString):defaultValue=OctetString('64-1500-4096')
_NnpppMtu_Type.__name__=_E
_NnpppMtu_Object=MibTableColumn
nnpppMtu=_NnpppMtu_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,1),_NnpppMtu_Type())
nnpppMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:nnpppMtu.setStatus(_A)
class _NnpppMru_Type(DisplayString):defaultValue=OctetString('46-1500-4096')
_NnpppMru_Type.__name__=_E
_NnpppMru_Object=MibTableColumn
nnpppMru=_NnpppMru_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,2),_NnpppMru_Type())
nnpppMru.setMaxAccess(_C)
if mibBuilder.loadTexts:nnpppMru.setStatus(_A)
class _NnmlpppMrru_Type(DisplayString):defaultValue=OctetString('1500-1524-8192')
_NnmlpppMrru_Type.__name__=_E
_NnmlpppMrru_Object=MibTableColumn
nnmlpppMrru=_NnmlpppMrru_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,3),_NnmlpppMrru_Type())
nnmlpppMrru.setMaxAccess(_C)
if mibBuilder.loadTexts:nnmlpppMrru.setStatus(_A)
class _NnmlpppSeq_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_NnmlpppSeq_Type.__name__=_D
_NnmlpppSeq_Object=MibTableColumn
nnmlpppSeq=_NnmlpppSeq_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,4),_NnmlpppSeq_Type())
nnmlpppSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:nnmlpppSeq.setStatus(_A)
class _NnmlpppSegmentThreshold_Type(Integer32):defaultValue=512
_NnmlpppSegmentThreshold_Type.__name__=_D
_NnmlpppSegmentThreshold_Object=MibTableColumn
nnmlpppSegmentThreshold=_NnmlpppSegmentThreshold_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,5),_NnmlpppSegmentThreshold_Type())
nnmlpppSegmentThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:nnmlpppSegmentThreshold.setStatus(_A)
class _NnmlpppDiffDelay_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_NnmlpppDiffDelay_Type.__name__=_D
_NnmlpppDiffDelay_Object=MibTableColumn
nnmlpppDiffDelay=_NnmlpppDiffDelay_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,6),_NnmlpppDiffDelay_Type())
nnmlpppDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:nnmlpppDiffDelay.setStatus(_A)
_NnmlpppDiscriminator_Type=DisplayString
_NnmlpppDiscriminator_Object=MibTableColumn
nnmlpppDiscriminator=_NnmlpppDiscriminator_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,7),_NnmlpppDiscriminator_Type())
nnmlpppDiscriminator.setMaxAccess(_C)
if mibBuilder.loadTexts:nnmlpppDiscriminator.setStatus(_A)
_NnpppNegotiatePeerIpAddr_Type=IpAddress
_NnpppNegotiatePeerIpAddr_Object=MibTableColumn
nnpppNegotiatePeerIpAddr=_NnpppNegotiatePeerIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,8),_NnpppNegotiatePeerIpAddr_Type())
nnpppNegotiatePeerIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:nnpppNegotiatePeerIpAddr.setStatus(_A)
_NnpppSrcIpAddr_Type=IpAddress
_NnpppSrcIpAddr_Object=MibTableColumn
nnpppSrcIpAddr=_NnpppSrcIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,9),_NnpppSrcIpAddr_Type())
nnpppSrcIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:nnpppSrcIpAddr.setStatus(_A)
_NnpppPeerIpAddr_Type=IpAddress
_NnpppPeerIpAddr_Object=MibTableColumn
nnpppPeerIpAddr=_NnpppPeerIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,14,1,1,10),_NnpppPeerIpAddr_Type())
nnpppPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppPeerIpAddr.setStatus(_A)
_NnpppStatsTable_Object=MibTable
nnpppStatsTable=_NnpppStatsTable_Object((1,3,6,1,4,1,562,73,1,1,1,14,2))
if mibBuilder.loadTexts:nnpppStatsTable.setStatus(_A)
_NnpppStatsTableEntry_Object=MibTableRow
nnpppStatsTableEntry=_NnpppStatsTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1))
nnpppStatsTableEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nnpppStatsTableEntry.setStatus(_A)
_NnpppStatsBytesRxLastBootOrClear_Type=Counter32
_NnpppStatsBytesRxLastBootOrClear_Object=MibTableColumn
nnpppStatsBytesRxLastBootOrClear=_NnpppStatsBytesRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,1),_NnpppStatsBytesRxLastBootOrClear_Type())
nnpppStatsBytesRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsBytesRxLastBootOrClear.setStatus(_A)
_NnpppStatsBytesTxLastBootOrClear_Type=Counter32
_NnpppStatsBytesTxLastBootOrClear_Object=MibTableColumn
nnpppStatsBytesTxLastBootOrClear=_NnpppStatsBytesTxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,2),_NnpppStatsBytesTxLastBootOrClear_Type())
nnpppStatsBytesTxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsBytesTxLastBootOrClear.setStatus(_A)
_NnpppStatsPktsRxLastBootOrClear_Type=Counter32
_NnpppStatsPktsRxLastBootOrClear_Object=MibTableColumn
nnpppStatsPktsRxLastBootOrClear=_NnpppStatsPktsRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,3),_NnpppStatsPktsRxLastBootOrClear_Type())
nnpppStatsPktsRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsPktsRxLastBootOrClear.setStatus(_A)
_NnpppStatsPktsTxLastBootOrClear_Type=Counter32
_NnpppStatsPktsTxLastBootOrClear_Object=MibTableColumn
nnpppStatsPktsTxLastBootOrClear=_NnpppStatsPktsTxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,4),_NnpppStatsPktsTxLastBootOrClear_Type())
nnpppStatsPktsTxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsPktsTxLastBootOrClear.setStatus(_A)
_NnpppStatsErrPktsRxLastBootOrClear_Type=Counter32
_NnpppStatsErrPktsRxLastBootOrClear_Object=MibTableColumn
nnpppStatsErrPktsRxLastBootOrClear=_NnpppStatsErrPktsRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,5),_NnpppStatsErrPktsRxLastBootOrClear_Type())
nnpppStatsErrPktsRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsErrPktsRxLastBootOrClear.setStatus(_A)
_NnpppStatsUpDownStatesLastBootOrClear_Type=Counter32
_NnpppStatsUpDownStatesLastBootOrClear_Object=MibTableColumn
nnpppStatsUpDownStatesLastBootOrClear=_NnpppStatsUpDownStatesLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,6),_NnpppStatsUpDownStatesLastBootOrClear_Type())
nnpppStatsUpDownStatesLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsUpDownStatesLastBootOrClear.setStatus(_A)
_NnpppStatsBytesRxLastFiveMins_Type=Counter32
_NnpppStatsBytesRxLastFiveMins_Object=MibTableColumn
nnpppStatsBytesRxLastFiveMins=_NnpppStatsBytesRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,7),_NnpppStatsBytesRxLastFiveMins_Type())
nnpppStatsBytesRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsBytesRxLastFiveMins.setStatus(_A)
_NnpppStatsBytesTxLastFiveMins_Type=Counter32
_NnpppStatsBytesTxLastFiveMins_Object=MibTableColumn
nnpppStatsBytesTxLastFiveMins=_NnpppStatsBytesTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,8),_NnpppStatsBytesTxLastFiveMins_Type())
nnpppStatsBytesTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsBytesTxLastFiveMins.setStatus(_A)
_NnpppStatsPktsRxLastFiveMins_Type=Counter32
_NnpppStatsPktsRxLastFiveMins_Object=MibTableColumn
nnpppStatsPktsRxLastFiveMins=_NnpppStatsPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,9),_NnpppStatsPktsRxLastFiveMins_Type())
nnpppStatsPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsPktsRxLastFiveMins.setStatus(_A)
_NnpppStatsPktsTxLastFiveMins_Type=Counter32
_NnpppStatsPktsTxLastFiveMins_Object=MibTableColumn
nnpppStatsPktsTxLastFiveMins=_NnpppStatsPktsTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,10),_NnpppStatsPktsTxLastFiveMins_Type())
nnpppStatsPktsTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsPktsTxLastFiveMins.setStatus(_A)
_NnpppStatsErrPktsRxLastFiveMins_Type=Counter32
_NnpppStatsErrPktsRxLastFiveMins_Object=MibTableColumn
nnpppStatsErrPktsRxLastFiveMins=_NnpppStatsErrPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,11),_NnpppStatsErrPktsRxLastFiveMins_Type())
nnpppStatsErrPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsErrPktsRxLastFiveMins.setStatus(_A)
_NnpppStatsUpDownStatesLastFiveMins_Type=Counter32
_NnpppStatsUpDownStatesLastFiveMins_Object=MibTableColumn
nnpppStatsUpDownStatesLastFiveMins=_NnpppStatsUpDownStatesLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,14,2,1,12),_NnpppStatsUpDownStatesLastFiveMins_Type())
nnpppStatsUpDownStatesLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnpppStatsUpDownStatesLastFiveMins.setStatus(_A)
mibBuilder.exportSymbols('PPP-MIB',**{'nnpppMib':nnpppMib,'nnpppTable':nnpppTable,'nnpppTableEntry':nnpppTableEntry,'nnpppMtu':nnpppMtu,'nnpppMru':nnpppMru,'nnmlpppMrru':nnmlpppMrru,'nnmlpppSeq':nnmlpppSeq,'nnmlpppSegmentThreshold':nnmlpppSegmentThreshold,'nnmlpppDiffDelay':nnmlpppDiffDelay,'nnmlpppDiscriminator':nnmlpppDiscriminator,'nnpppNegotiatePeerIpAddr':nnpppNegotiatePeerIpAddr,'nnpppSrcIpAddr':nnpppSrcIpAddr,'nnpppPeerIpAddr':nnpppPeerIpAddr,'nnpppStatsTable':nnpppStatsTable,'nnpppStatsTableEntry':nnpppStatsTableEntry,'nnpppStatsBytesRxLastBootOrClear':nnpppStatsBytesRxLastBootOrClear,'nnpppStatsBytesTxLastBootOrClear':nnpppStatsBytesTxLastBootOrClear,'nnpppStatsPktsRxLastBootOrClear':nnpppStatsPktsRxLastBootOrClear,'nnpppStatsPktsTxLastBootOrClear':nnpppStatsPktsTxLastBootOrClear,'nnpppStatsErrPktsRxLastBootOrClear':nnpppStatsErrPktsRxLastBootOrClear,'nnpppStatsUpDownStatesLastBootOrClear':nnpppStatsUpDownStatesLastBootOrClear,'nnpppStatsBytesRxLastFiveMins':nnpppStatsBytesRxLastFiveMins,'nnpppStatsBytesTxLastFiveMins':nnpppStatsBytesTxLastFiveMins,'nnpppStatsPktsRxLastFiveMins':nnpppStatsPktsRxLastFiveMins,'nnpppStatsPktsTxLastFiveMins':nnpppStatsPktsTxLastFiveMins,'nnpppStatsErrPktsRxLastFiveMins':nnpppStatsErrPktsRxLastFiveMins,'nnpppStatsUpDownStatesLastFiveMins':nnpppStatsUpDownStatesLastFiveMins})