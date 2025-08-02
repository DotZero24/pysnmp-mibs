_f='ciscoIetfDot11QosStatsGroup'
_e='ciscoIetfDot11QosQueueGroup'
_d='ciscoIetfDot11QosConfigGroup'
_c='cid11QosTransmittedFrames'
_b='cid11QosReceivedFragments'
_a='cid11QosFrameDuplicates'
_Z='cid11QosMutipleRetries'
_Y='cid11QosRetries'
_X='cid11QosFails'
_W='cid11QosTransmittedFragments'
_V='cid11QosDiscardedFrames'
_U='cid11QosReceivedRetries'
_T='cid11QosReceivedMPDUs'
_S='cid11QosIfDiscardedFragments'
_R='cid11QueuePeakSize'
_Q='cid11QueueSize'
_P='cid11QueuesAvailable'
_O='cid11QosOptionImplemented'
_N='cid11MSDULifetime'
_M='cid11TrafficPriority'
_L='cid11AIFS'
_K='cid11CWPFactor'
_J='cid11CWmax'
_I='cid11CWmin'
_H='cid11TrafficCategory'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='Unsigned32'
_C='read-only'
_B='CISCO-IETF-DOT11-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoIetfDot11QosMIB=ModuleIdentity((1,3,6,1,4,1,9,10,89))
if mibBuilder.loadTexts:ciscoIetfDot11QosMIB.setRevisions(('2002-03-28 00:00','2002-01-29 00:00'))
class Cid11QosTrafficCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('bestEffort',0),('background',1),('spare',2),('excellentEffort',3),('controlledLoad',4),('interactiveVideo',5),('interactiveVoice',6),('networkControl',7)))
_CiscoIetfDot11QosMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosMIBObjects=_CiscoIetfDot11QosMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,89,1))
_CiscoIetfDot11QosConfig_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosConfig=_CiscoIetfDot11QosConfig_ObjectIdentity((1,3,6,1,4,1,9,10,89,1,1))
_Cid11QosConfigTable_Object=MibTable
cid11QosConfigTable=_Cid11QosConfigTable_Object((1,3,6,1,4,1,9,10,89,1,1,1))
if mibBuilder.loadTexts:cid11QosConfigTable.setStatus(_A)
_Cid11QosConfigEntry_Object=MibTableRow
cid11QosConfigEntry=_Cid11QosConfigEntry_Object((1,3,6,1,4,1,9,10,89,1,1,1,1))
cid11QosConfigEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:cid11QosConfigEntry.setStatus(_A)
_Cid11TrafficCategory_Type=Cid11QosTrafficCategory
_Cid11TrafficCategory_Object=MibTableColumn
cid11TrafficCategory=_Cid11TrafficCategory_Object((1,3,6,1,4,1,9,10,89,1,1,1,1,1),_Cid11TrafficCategory_Type())
cid11TrafficCategory.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cid11TrafficCategory.setStatus(_A)
class _Cid11CWmin_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_Cid11CWmin_Type.__name__=_D
_Cid11CWmin_Object=MibTableColumn
cid11CWmin=_Cid11CWmin_Object((1,3,6,1,4,1,9,10,89,1,1,1,1,2),_Cid11CWmin_Type())
cid11CWmin.setMaxAccess(_G)
if mibBuilder.loadTexts:cid11CWmin.setStatus(_A)
class _Cid11CWmax_Type(Unsigned32):defaultValue=1023;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_Cid11CWmax_Type.__name__=_D
_Cid11CWmax_Object=MibTableColumn
cid11CWmax=_Cid11CWmax_Object((1,3,6,1,4,1,9,10,89,1,1,1,1,3),_Cid11CWmax_Type())
cid11CWmax.setMaxAccess(_G)
if mibBuilder.loadTexts:cid11CWmax.setStatus(_A)
class _Cid11CWPFactor_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Cid11CWPFactor_Type.__name__=_D
_Cid11CWPFactor_Object=MibTableColumn
cid11CWPFactor=_Cid11CWPFactor_Object((1,3,6,1,4,1,9,10,89,1,1,1,1,4),_Cid11CWPFactor_Type())
cid11CWPFactor.setMaxAccess(_G)
if mibBuilder.loadTexts:cid11CWPFactor.setStatus(_A)
class _Cid11AIFS_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_Cid11AIFS_Type.__name__=_D
_Cid11AIFS_Object=MibTableColumn
cid11AIFS=_Cid11AIFS_Object((1,3,6,1,4,1,9,10,89,1,1,1,1,5),_Cid11AIFS_Type())
cid11AIFS.setMaxAccess(_G)
if mibBuilder.loadTexts:cid11AIFS.setStatus(_A)
class _Cid11TrafficPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Cid11TrafficPriority_Type.__name__=_D
_Cid11TrafficPriority_Object=MibTableColumn
cid11TrafficPriority=_Cid11TrafficPriority_Object((1,3,6,1,4,1,9,10,89,1,1,1,1,6),_Cid11TrafficPriority_Type())
cid11TrafficPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:cid11TrafficPriority.setStatus(_A)
class _Cid11MSDULifetime_Type(Unsigned32):defaultValue=65535;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cid11MSDULifetime_Type.__name__=_D
_Cid11MSDULifetime_Object=MibTableColumn
cid11MSDULifetime=_Cid11MSDULifetime_Object((1,3,6,1,4,1,9,10,89,1,1,1,1,7),_Cid11MSDULifetime_Type())
cid11MSDULifetime.setMaxAccess(_G)
if mibBuilder.loadTexts:cid11MSDULifetime.setStatus(_A)
_Cid11QosSupportTable_Object=MibTable
cid11QosSupportTable=_Cid11QosSupportTable_Object((1,3,6,1,4,1,9,10,89,1,1,2))
if mibBuilder.loadTexts:cid11QosSupportTable.setStatus(_A)
_Cid11QosSupportEntry_Object=MibTableRow
cid11QosSupportEntry=_Cid11QosSupportEntry_Object((1,3,6,1,4,1,9,10,89,1,1,2,1))
cid11QosSupportEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cid11QosSupportEntry.setStatus(_A)
_Cid11QosOptionImplemented_Type=TruthValue
_Cid11QosOptionImplemented_Object=MibTableColumn
cid11QosOptionImplemented=_Cid11QosOptionImplemented_Object((1,3,6,1,4,1,9,10,89,1,1,2,1,1),_Cid11QosOptionImplemented_Type())
cid11QosOptionImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosOptionImplemented.setStatus(_A)
class _Cid11QueuesAvailable_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,8))
_Cid11QueuesAvailable_Type.__name__=_D
_Cid11QueuesAvailable_Object=MibTableColumn
cid11QueuesAvailable=_Cid11QueuesAvailable_Object((1,3,6,1,4,1,9,10,89,1,1,2,1,2),_Cid11QueuesAvailable_Type())
cid11QueuesAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QueuesAvailable.setStatus(_A)
_CiscoIetfDot11QosQueue_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosQueue=_CiscoIetfDot11QosQueue_ObjectIdentity((1,3,6,1,4,1,9,10,89,1,2))
_Cid11QueueTable_Object=MibTable
cid11QueueTable=_Cid11QueueTable_Object((1,3,6,1,4,1,9,10,89,1,2,1))
if mibBuilder.loadTexts:cid11QueueTable.setStatus(_A)
_Cid11QueueEntry_Object=MibTableRow
cid11QueueEntry=_Cid11QueueEntry_Object((1,3,6,1,4,1,9,10,89,1,2,1,1))
cid11QueueEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:cid11QueueEntry.setStatus(_A)
class _Cid11QueueSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_Cid11QueueSize_Type.__name__=_D
_Cid11QueueSize_Object=MibTableColumn
cid11QueueSize=_Cid11QueueSize_Object((1,3,6,1,4,1,9,10,89,1,2,1,1,1),_Cid11QueueSize_Type())
cid11QueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QueueSize.setStatus(_A)
_Cid11QueuePeakSize_Type=Counter32
_Cid11QueuePeakSize_Object=MibTableColumn
cid11QueuePeakSize=_Cid11QueuePeakSize_Object((1,3,6,1,4,1,9,10,89,1,2,1,1,2),_Cid11QueuePeakSize_Type())
cid11QueuePeakSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QueuePeakSize.setStatus(_A)
_CiscoIetfDot11QosStatistics_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosStatistics=_CiscoIetfDot11QosStatistics_ObjectIdentity((1,3,6,1,4,1,9,10,89,1,3))
_Cid11QosStatisticsTable_Object=MibTable
cid11QosStatisticsTable=_Cid11QosStatisticsTable_Object((1,3,6,1,4,1,9,10,89,1,3,1))
if mibBuilder.loadTexts:cid11QosStatisticsTable.setStatus(_A)
_Cid11QosStatisticsEntry_Object=MibTableRow
cid11QosStatisticsEntry=_Cid11QosStatisticsEntry_Object((1,3,6,1,4,1,9,10,89,1,3,1,1))
cid11QosStatisticsEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:cid11QosStatisticsEntry.setStatus(_A)
_Cid11QosReceivedMPDUs_Type=Counter32
_Cid11QosReceivedMPDUs_Object=MibTableColumn
cid11QosReceivedMPDUs=_Cid11QosReceivedMPDUs_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,1),_Cid11QosReceivedMPDUs_Type())
cid11QosReceivedMPDUs.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosReceivedMPDUs.setStatus(_A)
_Cid11QosReceivedRetries_Type=Counter32
_Cid11QosReceivedRetries_Object=MibTableColumn
cid11QosReceivedRetries=_Cid11QosReceivedRetries_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,2),_Cid11QosReceivedRetries_Type())
cid11QosReceivedRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosReceivedRetries.setStatus(_A)
_Cid11QosDiscardedFrames_Type=Counter32
_Cid11QosDiscardedFrames_Object=MibTableColumn
cid11QosDiscardedFrames=_Cid11QosDiscardedFrames_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,3),_Cid11QosDiscardedFrames_Type())
cid11QosDiscardedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosDiscardedFrames.setStatus(_A)
_Cid11QosTransmittedFragments_Type=Counter32
_Cid11QosTransmittedFragments_Object=MibTableColumn
cid11QosTransmittedFragments=_Cid11QosTransmittedFragments_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,4),_Cid11QosTransmittedFragments_Type())
cid11QosTransmittedFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosTransmittedFragments.setStatus(_A)
_Cid11QosFails_Type=Counter32
_Cid11QosFails_Object=MibTableColumn
cid11QosFails=_Cid11QosFails_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,5),_Cid11QosFails_Type())
cid11QosFails.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosFails.setStatus(_A)
_Cid11QosRetries_Type=Counter32
_Cid11QosRetries_Object=MibTableColumn
cid11QosRetries=_Cid11QosRetries_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,6),_Cid11QosRetries_Type())
cid11QosRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosRetries.setStatus(_A)
_Cid11QosMutipleRetries_Type=Counter32
_Cid11QosMutipleRetries_Object=MibTableColumn
cid11QosMutipleRetries=_Cid11QosMutipleRetries_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,7),_Cid11QosMutipleRetries_Type())
cid11QosMutipleRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosMutipleRetries.setStatus(_A)
_Cid11QosFrameDuplicates_Type=Counter32
_Cid11QosFrameDuplicates_Object=MibTableColumn
cid11QosFrameDuplicates=_Cid11QosFrameDuplicates_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,8),_Cid11QosFrameDuplicates_Type())
cid11QosFrameDuplicates.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosFrameDuplicates.setStatus(_A)
_Cid11QosReceivedFragments_Type=Counter32
_Cid11QosReceivedFragments_Object=MibTableColumn
cid11QosReceivedFragments=_Cid11QosReceivedFragments_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,9),_Cid11QosReceivedFragments_Type())
cid11QosReceivedFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosReceivedFragments.setStatus(_A)
_Cid11QosTransmittedFrames_Type=Counter32
_Cid11QosTransmittedFrames_Object=MibTableColumn
cid11QosTransmittedFrames=_Cid11QosTransmittedFrames_Object((1,3,6,1,4,1,9,10,89,1,3,1,1,10),_Cid11QosTransmittedFrames_Type())
cid11QosTransmittedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosTransmittedFrames.setStatus(_A)
_Cid11QosIfStatisticsTable_Object=MibTable
cid11QosIfStatisticsTable=_Cid11QosIfStatisticsTable_Object((1,3,6,1,4,1,9,10,89,1,3,2))
if mibBuilder.loadTexts:cid11QosIfStatisticsTable.setStatus(_A)
_Cid11QosIfStatisticsEntry_Object=MibTableRow
cid11QosIfStatisticsEntry=_Cid11QosIfStatisticsEntry_Object((1,3,6,1,4,1,9,10,89,1,3,2,1))
cid11QosIfStatisticsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cid11QosIfStatisticsEntry.setStatus(_A)
_Cid11QosIfDiscardedFragments_Type=Counter32
_Cid11QosIfDiscardedFragments_Object=MibTableColumn
cid11QosIfDiscardedFragments=_Cid11QosIfDiscardedFragments_Object((1,3,6,1,4,1,9,10,89,1,3,2,1,1),_Cid11QosIfDiscardedFragments_Type())
cid11QosIfDiscardedFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:cid11QosIfDiscardedFragments.setStatus(_A)
_CiscoIetfDot11QosMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosMIBConformance=_CiscoIetfDot11QosMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,89,2))
_CiscoIetfDot11QosMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosMIBCompliances=_CiscoIetfDot11QosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,89,2,1))
_CiscoIetfDot11QosMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIetfDot11QosMIBGroups=_CiscoIetfDot11QosMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,89,2,2))
ciscoIetfDot11QosConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,89,2,2,1))
ciscoIetfDot11QosConfigGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoIetfDot11QosConfigGroup.setStatus(_A)
ciscoIetfDot11QosQueueGroup=ObjectGroup((1,3,6,1,4,1,9,10,89,2,2,2))
ciscoIetfDot11QosQueueGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoIetfDot11QosQueueGroup.setStatus(_A)
ciscoIetfDot11QosStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,89,2,2,3))
ciscoIetfDot11QosStatsGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoIetfDot11QosStatsGroup.setStatus(_A)
ciscoIetfDot11QosMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,89,2,1,1))
ciscoIetfDot11QosMIBCompliance.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoIetfDot11QosMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Cid11QosTrafficCategory':Cid11QosTrafficCategory,'ciscoIetfDot11QosMIB':ciscoIetfDot11QosMIB,'ciscoIetfDot11QosMIBObjects':ciscoIetfDot11QosMIBObjects,'ciscoIetfDot11QosConfig':ciscoIetfDot11QosConfig,'cid11QosConfigTable':cid11QosConfigTable,'cid11QosConfigEntry':cid11QosConfigEntry,_H:cid11TrafficCategory,_I:cid11CWmin,_J:cid11CWmax,_K:cid11CWPFactor,_L:cid11AIFS,_M:cid11TrafficPriority,_N:cid11MSDULifetime,'cid11QosSupportTable':cid11QosSupportTable,'cid11QosSupportEntry':cid11QosSupportEntry,_O:cid11QosOptionImplemented,_P:cid11QueuesAvailable,'ciscoIetfDot11QosQueue':ciscoIetfDot11QosQueue,'cid11QueueTable':cid11QueueTable,'cid11QueueEntry':cid11QueueEntry,_Q:cid11QueueSize,_R:cid11QueuePeakSize,'ciscoIetfDot11QosStatistics':ciscoIetfDot11QosStatistics,'cid11QosStatisticsTable':cid11QosStatisticsTable,'cid11QosStatisticsEntry':cid11QosStatisticsEntry,_T:cid11QosReceivedMPDUs,_U:cid11QosReceivedRetries,_V:cid11QosDiscardedFrames,_W:cid11QosTransmittedFragments,_X:cid11QosFails,_Y:cid11QosRetries,_Z:cid11QosMutipleRetries,_a:cid11QosFrameDuplicates,_b:cid11QosReceivedFragments,_c:cid11QosTransmittedFrames,'cid11QosIfStatisticsTable':cid11QosIfStatisticsTable,'cid11QosIfStatisticsEntry':cid11QosIfStatisticsEntry,_S:cid11QosIfDiscardedFragments,'ciscoIetfDot11QosMIBConformance':ciscoIetfDot11QosMIBConformance,'ciscoIetfDot11QosMIBCompliances':ciscoIetfDot11QosMIBCompliances,'ciscoIetfDot11QosMIBCompliance':ciscoIetfDot11QosMIBCompliance,'ciscoIetfDot11QosMIBGroups':ciscoIetfDot11QosMIBGroups,_d:ciscoIetfDot11QosConfigGroup,_e:ciscoIetfDot11QosQueueGroup,_f:ciscoIetfDot11QosStatsGroup})