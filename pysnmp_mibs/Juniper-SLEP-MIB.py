_T='juniSlepGroup2'
_S='juniSlepGroup'
_R='juniSlepDownWhenLooped'
_Q='obsolete'
_P='juniSlepIfStatsIndex'
_O='not-accessible'
_N='juniSlepIfIndex'
_M='Integer32'
_L='JuniEnable'
_K='juniSlepLinkStatusBadFCSs'
_J='juniSlepLinkStatusTooLongPackets'
_I='juniSlepKeepAliveFailures'
_H='juniSlepIfRowStatus'
_G='juniSlepIfLowerIfIndex'
_F='juniSlepKeepAliveTimer'
_E='juniSlepNextIfIndex'
_D='read-create'
_C='read-only'
_B='current'
_A='Juniper-SLEP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,JuniNextIfIndex=mibBuilder.importSymbols('Juniper-TC',_L,'JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
juniSlepMIBS=ModuleIdentity((1,3,6,1,4,1,4874,2,2,15))
if mibBuilder.loadTexts:juniSlepMIBS.setRevisions(('2002-09-16 21:44','2001-04-03 19:10','2000-01-03 00:00'))
_JuniSlepObjects_ObjectIdentity=ObjectIdentity
juniSlepObjects=_JuniSlepObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,15,1))
_JuniSlepIfLayer_ObjectIdentity=ObjectIdentity
juniSlepIfLayer=_JuniSlepIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,15,1,1))
_JuniSlepNextIfIndex_Type=JuniNextIfIndex
_JuniSlepNextIfIndex_Object=MibScalar
juniSlepNextIfIndex=_JuniSlepNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,15,1,1,1),_JuniSlepNextIfIndex_Type())
juniSlepNextIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSlepNextIfIndex.setStatus(_B)
_JuniSlepIfTable_Object=MibTable
juniSlepIfTable=_JuniSlepIfTable_Object((1,3,6,1,4,1,4874,2,2,15,1,1,2))
if mibBuilder.loadTexts:juniSlepIfTable.setStatus(_B)
_JuniSlepIfEntry_Object=MibTableRow
juniSlepIfEntry=_JuniSlepIfEntry_Object((1,3,6,1,4,1,4874,2,2,15,1,1,2,1))
juniSlepIfEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:juniSlepIfEntry.setStatus(_B)
_JuniSlepIfIndex_Type=InterfaceIndex
_JuniSlepIfIndex_Object=MibTableColumn
juniSlepIfIndex=_JuniSlepIfIndex_Object((1,3,6,1,4,1,4874,2,2,15,1,1,2,1,1),_JuniSlepIfIndex_Type())
juniSlepIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:juniSlepIfIndex.setStatus(_B)
class _JuniSlepKeepAliveTimer_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6553))
_JuniSlepKeepAliveTimer_Type.__name__=_M
_JuniSlepKeepAliveTimer_Object=MibTableColumn
juniSlepKeepAliveTimer=_JuniSlepKeepAliveTimer_Object((1,3,6,1,4,1,4874,2,2,15,1,1,2,1,2),_JuniSlepKeepAliveTimer_Type())
juniSlepKeepAliveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSlepKeepAliveTimer.setStatus(_B)
if mibBuilder.loadTexts:juniSlepKeepAliveTimer.setUnits('seconds')
_JuniSlepIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniSlepIfLowerIfIndex_Object=MibTableColumn
juniSlepIfLowerIfIndex=_JuniSlepIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,15,1,1,2,1,3),_JuniSlepIfLowerIfIndex_Type())
juniSlepIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSlepIfLowerIfIndex.setStatus(_B)
_JuniSlepIfRowStatus_Type=RowStatus
_JuniSlepIfRowStatus_Object=MibTableColumn
juniSlepIfRowStatus=_JuniSlepIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,15,1,1,2,1,4),_JuniSlepIfRowStatus_Type())
juniSlepIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSlepIfRowStatus.setStatus(_B)
class _JuniSlepDownWhenLooped_Type(JuniEnable):defaultValue=0
_JuniSlepDownWhenLooped_Type.__name__=_L
_JuniSlepDownWhenLooped_Object=MibTableColumn
juniSlepDownWhenLooped=_JuniSlepDownWhenLooped_Object((1,3,6,1,4,1,4874,2,2,15,1,1,2,1,5),_JuniSlepDownWhenLooped_Type())
juniSlepDownWhenLooped.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSlepDownWhenLooped.setStatus(_B)
_JuniSlepIfStatisticsTable_Object=MibTable
juniSlepIfStatisticsTable=_JuniSlepIfStatisticsTable_Object((1,3,6,1,4,1,4874,2,2,15,1,1,3))
if mibBuilder.loadTexts:juniSlepIfStatisticsTable.setStatus(_B)
_JuniSlepIfStatisticsEntry_Object=MibTableRow
juniSlepIfStatisticsEntry=_JuniSlepIfStatisticsEntry_Object((1,3,6,1,4,1,4874,2,2,15,1,1,3,1))
juniSlepIfStatisticsEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:juniSlepIfStatisticsEntry.setStatus(_B)
_JuniSlepIfStatsIndex_Type=InterfaceIndex
_JuniSlepIfStatsIndex_Object=MibTableColumn
juniSlepIfStatsIndex=_JuniSlepIfStatsIndex_Object((1,3,6,1,4,1,4874,2,2,15,1,1,3,1,1),_JuniSlepIfStatsIndex_Type())
juniSlepIfStatsIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:juniSlepIfStatsIndex.setStatus(_B)
_JuniSlepKeepAliveFailures_Type=Counter32
_JuniSlepKeepAliveFailures_Object=MibTableColumn
juniSlepKeepAliveFailures=_JuniSlepKeepAliveFailures_Object((1,3,6,1,4,1,4874,2,2,15,1,1,3,1,2),_JuniSlepKeepAliveFailures_Type())
juniSlepKeepAliveFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSlepKeepAliveFailures.setStatus(_B)
_JuniSlepLinkStatusTooLongPackets_Type=Counter32
_JuniSlepLinkStatusTooLongPackets_Object=MibTableColumn
juniSlepLinkStatusTooLongPackets=_JuniSlepLinkStatusTooLongPackets_Object((1,3,6,1,4,1,4874,2,2,15,1,1,3,1,3),_JuniSlepLinkStatusTooLongPackets_Type())
juniSlepLinkStatusTooLongPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSlepLinkStatusTooLongPackets.setStatus(_B)
_JuniSlepLinkStatusBadFCSs_Type=Counter32
_JuniSlepLinkStatusBadFCSs_Object=MibTableColumn
juniSlepLinkStatusBadFCSs=_JuniSlepLinkStatusBadFCSs_Object((1,3,6,1,4,1,4874,2,2,15,1,1,3,1,4),_JuniSlepLinkStatusBadFCSs_Type())
juniSlepLinkStatusBadFCSs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSlepLinkStatusBadFCSs.setStatus(_B)
_JuniSlepConformance_ObjectIdentity=ObjectIdentity
juniSlepConformance=_JuniSlepConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,15,4))
_JuniSlepCompliances_ObjectIdentity=ObjectIdentity
juniSlepCompliances=_JuniSlepCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,15,4,1))
_JuniSlepGroups_ObjectIdentity=ObjectIdentity
juniSlepGroups=_JuniSlepGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,15,4,2))
juniSlepGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,15,4,2,1))
juniSlepGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniSlepGroup.setStatus(_Q)
juniSlepGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,15,4,2,2))
juniSlepGroup2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniSlepGroup2.setStatus(_B)
juniSlepCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,15,4,1,1))
juniSlepCompliance.setObjects((_A,_S))
if mibBuilder.loadTexts:juniSlepCompliance.setStatus(_Q)
juniSlepCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,15,4,1,2))
juniSlepCompliance2.setObjects((_A,_T))
if mibBuilder.loadTexts:juniSlepCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniSlepMIBS':juniSlepMIBS,'juniSlepObjects':juniSlepObjects,'juniSlepIfLayer':juniSlepIfLayer,_E:juniSlepNextIfIndex,'juniSlepIfTable':juniSlepIfTable,'juniSlepIfEntry':juniSlepIfEntry,_N:juniSlepIfIndex,_F:juniSlepKeepAliveTimer,_G:juniSlepIfLowerIfIndex,_H:juniSlepIfRowStatus,_R:juniSlepDownWhenLooped,'juniSlepIfStatisticsTable':juniSlepIfStatisticsTable,'juniSlepIfStatisticsEntry':juniSlepIfStatisticsEntry,_P:juniSlepIfStatsIndex,_I:juniSlepKeepAliveFailures,_J:juniSlepLinkStatusTooLongPackets,_K:juniSlepLinkStatusBadFCSs,'juniSlepConformance':juniSlepConformance,'juniSlepCompliances':juniSlepCompliances,'juniSlepCompliance':juniSlepCompliance,'juniSlepCompliance2':juniSlepCompliance2,'juniSlepGroups':juniSlepGroups,_S:juniSlepGroup,_T:juniSlepGroup2})