_c='casaFlapListGroup'
_b='casaFlapCmFlapRowStatus'
_a='casaFlapCmLastFlapTime'
_Z='casaFlapCmFlapCounts'
_Y='casaFlapCmPowerAdjustments'
_X='casaFlapCmCRCCounts'
_W='casaFlapCmMisses'
_V='casaFlapCmHits'
_U='casaFlapCmInsertionFails'
_T='casaFlapCmDownstreamIfIndex'
_S='casaFlapCmUpstreamIfIndex'
_R='casaFlapListCheckInterval'
_Q='casaFlapListLastClearTime'
_P='casaFlapListClearAll'
_O='casaFlapListLastResetTime'
_N='casaFlapListResetAll'
_M='casaFlapListMaxSize'
_L='casaFlapListAging'
_K='casaFlapPowerAdjThreshold'
_J='casaFlapMissThreshold'
_I='casaFlapInsertionTime'
_H='casaFlapCmMacAddress'
_G='minutes'
_F='times'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='CASA-CABLE-FLAPLIST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
casa,=mibBuilder.importSymbols('CASA-MIB','casa')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
casaFlapListMib=ModuleIdentity((1,3,6,1,4,1,20858,10,11))
_CasaMgmt_ObjectIdentity=ObjectIdentity
casaMgmt=_CasaMgmt_ObjectIdentity((1,3,6,1,4,1,20858,10))
_CasaFlapListMIBObjects_ObjectIdentity=ObjectIdentity
casaFlapListMIBObjects=_CasaFlapListMIBObjects_ObjectIdentity((1,3,6,1,4,1,20858,10,11,1))
_CasaFlapListGlobal_ObjectIdentity=ObjectIdentity
casaFlapListGlobal=_CasaFlapListGlobal_ObjectIdentity((1,3,6,1,4,1,20858,10,11,1,1))
class _CasaFlapInsertionTime_Type(Unsigned32):defaultValue=60
_CasaFlapInsertionTime_Type.__name__=_E
_CasaFlapInsertionTime_Object=MibScalar
casaFlapInsertionTime=_CasaFlapInsertionTime_Object((1,3,6,1,4,1,20858,10,11,1,1,1),_CasaFlapInsertionTime_Type())
casaFlapInsertionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapInsertionTime.setStatus(_A)
if mibBuilder.loadTexts:casaFlapInsertionTime.setUnits('seconds')
class _CasaFlapMissThreshold_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_CasaFlapMissThreshold_Type.__name__=_E
_CasaFlapMissThreshold_Object=MibScalar
casaFlapMissThreshold=_CasaFlapMissThreshold_Object((1,3,6,1,4,1,20858,10,11,1,1,2),_CasaFlapMissThreshold_Type())
casaFlapMissThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapMissThreshold.setStatus(_A)
if mibBuilder.loadTexts:casaFlapMissThreshold.setUnits(_F)
class _CasaFlapPowerAdjThreshold_Type(Unsigned32):defaultValue=2
_CasaFlapPowerAdjThreshold_Type.__name__=_E
_CasaFlapPowerAdjThreshold_Object=MibScalar
casaFlapPowerAdjThreshold=_CasaFlapPowerAdjThreshold_Object((1,3,6,1,4,1,20858,10,11,1,1,3),_CasaFlapPowerAdjThreshold_Type())
casaFlapPowerAdjThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapPowerAdjThreshold.setStatus(_A)
if mibBuilder.loadTexts:casaFlapPowerAdjThreshold.setUnits('dB')
class _CasaFlapListAging_Type(Unsigned32):defaultValue=10080;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,86400))
_CasaFlapListAging_Type.__name__=_E
_CasaFlapListAging_Object=MibScalar
casaFlapListAging=_CasaFlapListAging_Object((1,3,6,1,4,1,20858,10,11,1,1,4),_CasaFlapListAging_Type())
casaFlapListAging.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapListAging.setStatus(_A)
if mibBuilder.loadTexts:casaFlapListAging.setUnits(_G)
class _CasaFlapListMaxSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CasaFlapListMaxSize_Type.__name__=_E
_CasaFlapListMaxSize_Object=MibScalar
casaFlapListMaxSize=_CasaFlapListMaxSize_Object((1,3,6,1,4,1,20858,10,11,1,1,5),_CasaFlapListMaxSize_Type())
casaFlapListMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapListMaxSize.setStatus(_A)
if mibBuilder.loadTexts:casaFlapListMaxSize.setUnits('entries')
_CasaFlapListResetAll_Type=TruthValue
_CasaFlapListResetAll_Object=MibScalar
casaFlapListResetAll=_CasaFlapListResetAll_Object((1,3,6,1,4,1,20858,10,11,1,1,6),_CasaFlapListResetAll_Type())
casaFlapListResetAll.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapListResetAll.setStatus(_A)
_CasaFlapListLastResetTime_Type=DateAndTime
_CasaFlapListLastResetTime_Object=MibScalar
casaFlapListLastResetTime=_CasaFlapListLastResetTime_Object((1,3,6,1,4,1,20858,10,11,1,1,7),_CasaFlapListLastResetTime_Type())
casaFlapListLastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapListLastResetTime.setStatus(_A)
_CasaFlapListClearAll_Type=TruthValue
_CasaFlapListClearAll_Object=MibScalar
casaFlapListClearAll=_CasaFlapListClearAll_Object((1,3,6,1,4,1,20858,10,11,1,1,8),_CasaFlapListClearAll_Type())
casaFlapListClearAll.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapListClearAll.setStatus(_A)
_CasaFlapListLastClearTime_Type=DateAndTime
_CasaFlapListLastClearTime_Object=MibScalar
casaFlapListLastClearTime=_CasaFlapListLastClearTime_Object((1,3,6,1,4,1,20858,10,11,1,1,9),_CasaFlapListLastClearTime_Type())
casaFlapListLastClearTime.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapListLastClearTime.setStatus(_A)
class _CasaFlapListCheckInterval_Type(Unsigned32):defaultValue=120
_CasaFlapListCheckInterval_Type.__name__=_E
_CasaFlapListCheckInterval_Object=MibScalar
casaFlapListCheckInterval=_CasaFlapListCheckInterval_Object((1,3,6,1,4,1,20858,10,11,1,1,10),_CasaFlapListCheckInterval_Type())
casaFlapListCheckInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapListCheckInterval.setStatus(_A)
if mibBuilder.loadTexts:casaFlapListCheckInterval.setUnits(_G)
_CasaFlapListTable_Object=MibTable
casaFlapListTable=_CasaFlapListTable_Object((1,3,6,1,4,1,20858,10,11,1,2))
if mibBuilder.loadTexts:casaFlapListTable.setStatus(_A)
_CasaFlapListEntry_Object=MibTableRow
casaFlapListEntry=_CasaFlapListEntry_Object((1,3,6,1,4,1,20858,10,11,1,2,1))
casaFlapListEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:casaFlapListEntry.setStatus(_A)
_CasaFlapCmMacAddress_Type=MacAddress
_CasaFlapCmMacAddress_Object=MibTableColumn
casaFlapCmMacAddress=_CasaFlapCmMacAddress_Object((1,3,6,1,4,1,20858,10,11,1,2,1,1),_CasaFlapCmMacAddress_Type())
casaFlapCmMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmMacAddress.setStatus(_A)
_CasaFlapCmUpstreamIfIndex_Type=Unsigned32
_CasaFlapCmUpstreamIfIndex_Object=MibTableColumn
casaFlapCmUpstreamIfIndex=_CasaFlapCmUpstreamIfIndex_Object((1,3,6,1,4,1,20858,10,11,1,2,1,2),_CasaFlapCmUpstreamIfIndex_Type())
casaFlapCmUpstreamIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmUpstreamIfIndex.setStatus(_A)
_CasaFlapCmDownstreamIfIndex_Type=Unsigned32
_CasaFlapCmDownstreamIfIndex_Object=MibTableColumn
casaFlapCmDownstreamIfIndex=_CasaFlapCmDownstreamIfIndex_Object((1,3,6,1,4,1,20858,10,11,1,2,1,3),_CasaFlapCmDownstreamIfIndex_Type())
casaFlapCmDownstreamIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmDownstreamIfIndex.setStatus(_A)
_CasaFlapCmInsertionFails_Type=Integer32
_CasaFlapCmInsertionFails_Object=MibTableColumn
casaFlapCmInsertionFails=_CasaFlapCmInsertionFails_Object((1,3,6,1,4,1,20858,10,11,1,2,1,4),_CasaFlapCmInsertionFails_Type())
casaFlapCmInsertionFails.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmInsertionFails.setStatus(_A)
if mibBuilder.loadTexts:casaFlapCmInsertionFails.setUnits(_F)
_CasaFlapCmHits_Type=Unsigned32
_CasaFlapCmHits_Object=MibTableColumn
casaFlapCmHits=_CasaFlapCmHits_Object((1,3,6,1,4,1,20858,10,11,1,2,1,5),_CasaFlapCmHits_Type())
casaFlapCmHits.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmHits.setStatus(_A)
if mibBuilder.loadTexts:casaFlapCmHits.setUnits(_F)
_CasaFlapCmMisses_Type=Unsigned32
_CasaFlapCmMisses_Object=MibTableColumn
casaFlapCmMisses=_CasaFlapCmMisses_Object((1,3,6,1,4,1,20858,10,11,1,2,1,6),_CasaFlapCmMisses_Type())
casaFlapCmMisses.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmMisses.setStatus(_A)
if mibBuilder.loadTexts:casaFlapCmMisses.setUnits(_F)
_CasaFlapCmCRCCounts_Type=Integer32
_CasaFlapCmCRCCounts_Object=MibTableColumn
casaFlapCmCRCCounts=_CasaFlapCmCRCCounts_Object((1,3,6,1,4,1,20858,10,11,1,2,1,7),_CasaFlapCmCRCCounts_Type())
casaFlapCmCRCCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmCRCCounts.setStatus(_A)
_CasaFlapCmPowerAdjustments_Type=Unsigned32
_CasaFlapCmPowerAdjustments_Object=MibTableColumn
casaFlapCmPowerAdjustments=_CasaFlapCmPowerAdjustments_Object((1,3,6,1,4,1,20858,10,11,1,2,1,8),_CasaFlapCmPowerAdjustments_Type())
casaFlapCmPowerAdjustments.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmPowerAdjustments.setStatus(_A)
_CasaFlapCmFlapCounts_Type=Integer32
_CasaFlapCmFlapCounts_Object=MibTableColumn
casaFlapCmFlapCounts=_CasaFlapCmFlapCounts_Object((1,3,6,1,4,1,20858,10,11,1,2,1,9),_CasaFlapCmFlapCounts_Type())
casaFlapCmFlapCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmFlapCounts.setStatus(_A)
_CasaFlapCmLastFlapTime_Type=DateAndTime
_CasaFlapCmLastFlapTime_Object=MibTableColumn
casaFlapCmLastFlapTime=_CasaFlapCmLastFlapTime_Object((1,3,6,1,4,1,20858,10,11,1,2,1,10),_CasaFlapCmLastFlapTime_Type())
casaFlapCmLastFlapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:casaFlapCmLastFlapTime.setStatus(_A)
_CasaFlapCmFlapRowStatus_Type=RowStatus
_CasaFlapCmFlapRowStatus_Object=MibTableColumn
casaFlapCmFlapRowStatus=_CasaFlapCmFlapRowStatus_Object((1,3,6,1,4,1,20858,10,11,1,2,1,11),_CasaFlapCmFlapRowStatus_Type())
casaFlapCmFlapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:casaFlapCmFlapRowStatus.setStatus(_A)
_CasaFlapListGroups_ObjectIdentity=ObjectIdentity
casaFlapListGroups=_CasaFlapListGroups_ObjectIdentity((1,3,6,1,4,1,20858,10,11,2))
_CasaFlapListCompliances_ObjectIdentity=ObjectIdentity
casaFlapListCompliances=_CasaFlapListCompliances_ObjectIdentity((1,3,6,1,4,1,20858,10,11,3))
casaFlapListGroup=ObjectGroup((1,3,6,1,4,1,20858,10,11,2,1))
casaFlapListGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:casaFlapListGroup.setStatus(_A)
casaFlapListCompliance=ModuleCompliance((1,3,6,1,4,1,20858,10,11,3,1))
casaFlapListCompliance.setObjects((_B,_c))
if mibBuilder.loadTexts:casaFlapListCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'casaMgmt':casaMgmt,'casaFlapListMib':casaFlapListMib,'casaFlapListMIBObjects':casaFlapListMIBObjects,'casaFlapListGlobal':casaFlapListGlobal,_I:casaFlapInsertionTime,_J:casaFlapMissThreshold,_K:casaFlapPowerAdjThreshold,_L:casaFlapListAging,_M:casaFlapListMaxSize,_N:casaFlapListResetAll,_O:casaFlapListLastResetTime,_P:casaFlapListClearAll,_Q:casaFlapListLastClearTime,_R:casaFlapListCheckInterval,'casaFlapListTable':casaFlapListTable,'casaFlapListEntry':casaFlapListEntry,_H:casaFlapCmMacAddress,_S:casaFlapCmUpstreamIfIndex,_T:casaFlapCmDownstreamIfIndex,_U:casaFlapCmInsertionFails,_V:casaFlapCmHits,_W:casaFlapCmMisses,_X:casaFlapCmCRCCounts,_Y:casaFlapCmPowerAdjustments,_Z:casaFlapCmFlapCounts,_a:casaFlapCmLastFlapTime,_b:casaFlapCmFlapRowStatus,'casaFlapListGroups':casaFlapListGroups,_c:casaFlapListGroup,'casaFlapListCompliances':casaFlapListCompliances,'casaFlapListCompliance':casaFlapListCompliance})