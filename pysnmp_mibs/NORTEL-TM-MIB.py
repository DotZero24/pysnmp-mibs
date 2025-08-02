_H='cosIndex'
_G='queueGroupIndex'
_F='trafficMgmtIfIndex'
_E='not-accessible'
_D='Gauge32'
_C='NORTEL-TM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nortelGenericMIBs,=mibBuilder.importSymbols('NORTEL-GENERIC-MIB','nortelGenericMIBs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_D,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nnTMMIB=ModuleIdentity((1,3,6,1,4,1,562,29,3))
if mibBuilder.loadTexts:nnTMMIB.setRevisions(('2005-11-15 15:22','2008-07-30 10:12'))
class NnTMClassOfService(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,15)));namedValues=NamedValues(*(('cosStandard',0),('cosBronze',1),('cosSilver',2),('cosGold',3),('cosPlatinum',4),('cosPremium',5),('cosNetworkNT',6),('cosCritical',7),('cosNetworkNW',8),('cosUnknown',15)))
class NnTMQueueGroup(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('eQGRPUNKNOWN',0),('eQGRPNA',1),('eQGRP1',2),('eQGRP2',3)))
_NnTMObjects_ObjectIdentity=ObjectIdentity
nnTMObjects=_NnTMObjects_ObjectIdentity((1,3,6,1,4,1,562,29,3,1))
_NnTMStatsTable_Object=MibTable
nnTMStatsTable=_NnTMStatsTable_Object((1,3,6,1,4,1,562,29,3,1,1))
if mibBuilder.loadTexts:nnTMStatsTable.setStatus(_A)
_NnTMStatsEntry_Object=MibTableRow
nnTMStatsEntry=_NnTMStatsEntry_Object((1,3,6,1,4,1,562,29,3,1,1,1))
nnTMStatsEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:nnTMStatsEntry.setStatus(_A)
_TrafficMgmtIfIndex_Type=InterfaceIndex
_TrafficMgmtIfIndex_Object=MibTableColumn
trafficMgmtIfIndex=_TrafficMgmtIfIndex_Object((1,3,6,1,4,1,562,29,3,1,1,1,1),_TrafficMgmtIfIndex_Type())
trafficMgmtIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:trafficMgmtIfIndex.setStatus(_A)
_QueueGroupIndex_Type=NnTMQueueGroup
_QueueGroupIndex_Object=MibTableColumn
queueGroupIndex=_QueueGroupIndex_Object((1,3,6,1,4,1,562,29,3,1,1,1,2),_QueueGroupIndex_Type())
queueGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:queueGroupIndex.setStatus(_A)
_CosIndex_Type=NnTMClassOfService
_CosIndex_Object=MibTableColumn
cosIndex=_CosIndex_Object((1,3,6,1,4,1,562,29,3,1,1,1,3),_CosIndex_Type())
cosIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cosIndex.setStatus(_A)
_NnTMStatsInFrames_Type=Counter64
_NnTMStatsInFrames_Object=MibTableColumn
nnTMStatsInFrames=_NnTMStatsInFrames_Object((1,3,6,1,4,1,562,29,3,1,1,1,4),_NnTMStatsInFrames_Type())
nnTMStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsInFrames.setStatus(_A)
_NnTMStatsInOctets_Type=Counter64
_NnTMStatsInOctets_Object=MibTableColumn
nnTMStatsInOctets=_NnTMStatsInOctets_Object((1,3,6,1,4,1,562,29,3,1,1,1,5),_NnTMStatsInOctets_Type())
nnTMStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsInOctets.setStatus(_A)
_NnTMStatsInFramesDiscards_Type=Counter64
_NnTMStatsInFramesDiscards_Object=MibTableColumn
nnTMStatsInFramesDiscards=_NnTMStatsInFramesDiscards_Object((1,3,6,1,4,1,562,29,3,1,1,1,6),_NnTMStatsInFramesDiscards_Type())
nnTMStatsInFramesDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsInFramesDiscards.setStatus(_A)
_NnTMStatsInFramesDiscardsOctets_Type=Counter64
_NnTMStatsInFramesDiscardsOctets_Object=MibTableColumn
nnTMStatsInFramesDiscardsOctets=_NnTMStatsInFramesDiscardsOctets_Object((1,3,6,1,4,1,562,29,3,1,1,1,7),_NnTMStatsInFramesDiscardsOctets_Type())
nnTMStatsInFramesDiscardsOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsInFramesDiscardsOctets.setStatus(_A)
_NnTMStatsInFramesNonConforming_Type=Counter64
_NnTMStatsInFramesNonConforming_Object=MibTableColumn
nnTMStatsInFramesNonConforming=_NnTMStatsInFramesNonConforming_Object((1,3,6,1,4,1,562,29,3,1,1,1,8),_NnTMStatsInFramesNonConforming_Type())
nnTMStatsInFramesNonConforming.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsInFramesNonConforming.setStatus(_A)
_NnTMStatsOutFrames_Type=Counter64
_NnTMStatsOutFrames_Object=MibTableColumn
nnTMStatsOutFrames=_NnTMStatsOutFrames_Object((1,3,6,1,4,1,562,29,3,1,1,1,9),_NnTMStatsOutFrames_Type())
nnTMStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsOutFrames.setStatus(_A)
_NnTMStatsOutOctets_Type=Counter64
_NnTMStatsOutOctets_Object=MibTableColumn
nnTMStatsOutOctets=_NnTMStatsOutOctets_Object((1,3,6,1,4,1,562,29,3,1,1,1,10),_NnTMStatsOutOctets_Type())
nnTMStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsOutOctets.setStatus(_A)
_NnTMStatsOutFramesDiscards_Type=Counter64
_NnTMStatsOutFramesDiscards_Object=MibTableColumn
nnTMStatsOutFramesDiscards=_NnTMStatsOutFramesDiscards_Object((1,3,6,1,4,1,562,29,3,1,1,1,11),_NnTMStatsOutFramesDiscards_Type())
nnTMStatsOutFramesDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsOutFramesDiscards.setStatus(_A)
_NnTMStatsOutFramesDiscardsOctets_Type=Counter64
_NnTMStatsOutFramesDiscardsOctets_Object=MibTableColumn
nnTMStatsOutFramesDiscardsOctets=_NnTMStatsOutFramesDiscardsOctets_Object((1,3,6,1,4,1,562,29,3,1,1,1,12),_NnTMStatsOutFramesDiscardsOctets_Type())
nnTMStatsOutFramesDiscardsOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsOutFramesDiscardsOctets.setStatus(_A)
_NnTMStatsOutFramesConformingDiscards_Type=Counter64
_NnTMStatsOutFramesConformingDiscards_Object=MibTableColumn
nnTMStatsOutFramesConformingDiscards=_NnTMStatsOutFramesConformingDiscards_Object((1,3,6,1,4,1,562,29,3,1,1,1,13),_NnTMStatsOutFramesConformingDiscards_Type())
nnTMStatsOutFramesConformingDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsOutFramesConformingDiscards.setStatus(_A)
class _NnTMStatsTxQueueUtilization_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NnTMStatsTxQueueUtilization_Type.__name__=_D
_NnTMStatsTxQueueUtilization_Object=MibTableColumn
nnTMStatsTxQueueUtilization=_NnTMStatsTxQueueUtilization_Object((1,3,6,1,4,1,562,29,3,1,1,1,14),_NnTMStatsTxQueueUtilization_Type())
nnTMStatsTxQueueUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsTxQueueUtilization.setStatus(_A)
class _NnTMStatsTxQueueUtilizationMaxPeak_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NnTMStatsTxQueueUtilizationMaxPeak_Type.__name__=_D
_NnTMStatsTxQueueUtilizationMaxPeak_Object=MibTableColumn
nnTMStatsTxQueueUtilizationMaxPeak=_NnTMStatsTxQueueUtilizationMaxPeak_Object((1,3,6,1,4,1,562,29,3,1,1,1,15),_NnTMStatsTxQueueUtilizationMaxPeak_Type())
nnTMStatsTxQueueUtilizationMaxPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:nnTMStatsTxQueueUtilizationMaxPeak.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'NnTMClassOfService':NnTMClassOfService,'NnTMQueueGroup':NnTMQueueGroup,'nnTMMIB':nnTMMIB,'nnTMObjects':nnTMObjects,'nnTMStatsTable':nnTMStatsTable,'nnTMStatsEntry':nnTMStatsEntry,_F:trafficMgmtIfIndex,_G:queueGroupIndex,_H:cosIndex,'nnTMStatsInFrames':nnTMStatsInFrames,'nnTMStatsInOctets':nnTMStatsInOctets,'nnTMStatsInFramesDiscards':nnTMStatsInFramesDiscards,'nnTMStatsInFramesDiscardsOctets':nnTMStatsInFramesDiscardsOctets,'nnTMStatsInFramesNonConforming':nnTMStatsInFramesNonConforming,'nnTMStatsOutFrames':nnTMStatsOutFrames,'nnTMStatsOutOctets':nnTMStatsOutOctets,'nnTMStatsOutFramesDiscards':nnTMStatsOutFramesDiscards,'nnTMStatsOutFramesDiscardsOctets':nnTMStatsOutFramesDiscardsOctets,'nnTMStatsOutFramesConformingDiscards':nnTMStatsOutFramesConformingDiscards,'nnTMStatsTxQueueUtilization':nnTMStatsTxQueueUtilization,'nnTMStatsTxQueueUtilizationMaxPeak':nnTMStatsTxQueueUtilizationMaxPeak})