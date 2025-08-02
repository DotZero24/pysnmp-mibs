_K='aristaFIBStatsGroup'
_J='aristaFIBStatsTotalRoutesForPrefixLen'
_I='aristaFIBStatsTotalRoutesForRouteType'
_H='aristaFIBStatsTotalRoutes'
_G='aristaFIBStatsPrefixLen'
_F='aristaFIBStatsRouteType'
_E='read-only'
_D='not-accessible'
_C='aristaFIBStatsAF'
_B='ARISTA-FIB-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
InetAddressPrefixLength,InetVersion=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressPrefixLength','InetVersion')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaFIBStatsMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,23))
if mibBuilder.loadTexts:aristaFIBStatsMIB.setRevisions(('2017-05-19 00:00',))
class RouteType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,9,13,14,200,201,202,203,204,205)));namedValues=NamedValues(*(('other',1),('connected',2),('static',3),('rip',8),('isIs',9),('ospf',13),('bgp',14),('ospfv3',200),('staticNonPersistent',201),('staticNexthopGroup',202),('attached',203),('vcs',204),('internal',205)))
_AristaFIBStatsMibObjects_ObjectIdentity=ObjectIdentity
aristaFIBStatsMibObjects=_AristaFIBStatsMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,23,1))
_AristaFIBStatsSummaryTable_Object=MibTable
aristaFIBStatsSummaryTable=_AristaFIBStatsSummaryTable_Object((1,3,6,1,4,1,30065,3,23,1,1))
if mibBuilder.loadTexts:aristaFIBStatsSummaryTable.setStatus(_A)
_AristaFIBStatsSummaryEntry_Object=MibTableRow
aristaFIBStatsSummaryEntry=_AristaFIBStatsSummaryEntry_Object((1,3,6,1,4,1,30065,3,23,1,1,1))
aristaFIBStatsSummaryEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:aristaFIBStatsSummaryEntry.setStatus(_A)
_AristaFIBStatsAF_Type=InetVersion
_AristaFIBStatsAF_Object=MibTableColumn
aristaFIBStatsAF=_AristaFIBStatsAF_Object((1,3,6,1,4,1,30065,3,23,1,1,1,1),_AristaFIBStatsAF_Type())
aristaFIBStatsAF.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaFIBStatsAF.setStatus(_A)
_AristaFIBStatsTotalRoutes_Type=Gauge32
_AristaFIBStatsTotalRoutes_Object=MibTableColumn
aristaFIBStatsTotalRoutes=_AristaFIBStatsTotalRoutes_Object((1,3,6,1,4,1,30065,3,23,1,1,1,2),_AristaFIBStatsTotalRoutes_Type())
aristaFIBStatsTotalRoutes.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaFIBStatsTotalRoutes.setStatus(_A)
_AristaFIBStatsByRouteTypeTable_Object=MibTable
aristaFIBStatsByRouteTypeTable=_AristaFIBStatsByRouteTypeTable_Object((1,3,6,1,4,1,30065,3,23,1,2))
if mibBuilder.loadTexts:aristaFIBStatsByRouteTypeTable.setStatus(_A)
_AristaFIBStatsByRouteTypeEntry_Object=MibTableRow
aristaFIBStatsByRouteTypeEntry=_AristaFIBStatsByRouteTypeEntry_Object((1,3,6,1,4,1,30065,3,23,1,2,1))
aristaFIBStatsByRouteTypeEntry.setIndexNames((0,_B,_C),(0,_B,_F))
if mibBuilder.loadTexts:aristaFIBStatsByRouteTypeEntry.setStatus(_A)
_AristaFIBStatsRouteType_Type=RouteType
_AristaFIBStatsRouteType_Object=MibTableColumn
aristaFIBStatsRouteType=_AristaFIBStatsRouteType_Object((1,3,6,1,4,1,30065,3,23,1,2,1,1),_AristaFIBStatsRouteType_Type())
aristaFIBStatsRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaFIBStatsRouteType.setStatus(_A)
_AristaFIBStatsTotalRoutesForRouteType_Type=Gauge32
_AristaFIBStatsTotalRoutesForRouteType_Object=MibTableColumn
aristaFIBStatsTotalRoutesForRouteType=_AristaFIBStatsTotalRoutesForRouteType_Object((1,3,6,1,4,1,30065,3,23,1,2,1,2),_AristaFIBStatsTotalRoutesForRouteType_Type())
aristaFIBStatsTotalRoutesForRouteType.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaFIBStatsTotalRoutesForRouteType.setStatus(_A)
_AristaFIBStatsByPrefixLenTable_Object=MibTable
aristaFIBStatsByPrefixLenTable=_AristaFIBStatsByPrefixLenTable_Object((1,3,6,1,4,1,30065,3,23,1,3))
if mibBuilder.loadTexts:aristaFIBStatsByPrefixLenTable.setStatus(_A)
_AristaFIBStatsByPrefixLenEntry_Object=MibTableRow
aristaFIBStatsByPrefixLenEntry=_AristaFIBStatsByPrefixLenEntry_Object((1,3,6,1,4,1,30065,3,23,1,3,1))
aristaFIBStatsByPrefixLenEntry.setIndexNames((0,_B,_C),(0,_B,_G))
if mibBuilder.loadTexts:aristaFIBStatsByPrefixLenEntry.setStatus(_A)
_AristaFIBStatsPrefixLen_Type=InetAddressPrefixLength
_AristaFIBStatsPrefixLen_Object=MibTableColumn
aristaFIBStatsPrefixLen=_AristaFIBStatsPrefixLen_Object((1,3,6,1,4,1,30065,3,23,1,3,1,1),_AristaFIBStatsPrefixLen_Type())
aristaFIBStatsPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaFIBStatsPrefixLen.setStatus(_A)
_AristaFIBStatsTotalRoutesForPrefixLen_Type=Gauge32
_AristaFIBStatsTotalRoutesForPrefixLen_Object=MibTableColumn
aristaFIBStatsTotalRoutesForPrefixLen=_AristaFIBStatsTotalRoutesForPrefixLen_Object((1,3,6,1,4,1,30065,3,23,1,3,1,2),_AristaFIBStatsTotalRoutesForPrefixLen_Type())
aristaFIBStatsTotalRoutesForPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaFIBStatsTotalRoutesForPrefixLen.setStatus(_A)
_AristaFIBStatsMibConformance_ObjectIdentity=ObjectIdentity
aristaFIBStatsMibConformance=_AristaFIBStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,23,2))
_AristaFIBStatsMibCompliances_ObjectIdentity=ObjectIdentity
aristaFIBStatsMibCompliances=_AristaFIBStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,23,2,1))
_AristaFIBStatsMibGroups_ObjectIdentity=ObjectIdentity
aristaFIBStatsMibGroups=_AristaFIBStatsMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,23,2,2))
aristaFIBStatsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,23,2,2,1))
aristaFIBStatsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:aristaFIBStatsGroup.setStatus(_A)
aristaFIBStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,23,2,1,1))
aristaFIBStatsMibCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:aristaFIBStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RouteType':RouteType,'aristaFIBStatsMIB':aristaFIBStatsMIB,'aristaFIBStatsMibObjects':aristaFIBStatsMibObjects,'aristaFIBStatsSummaryTable':aristaFIBStatsSummaryTable,'aristaFIBStatsSummaryEntry':aristaFIBStatsSummaryEntry,_C:aristaFIBStatsAF,_H:aristaFIBStatsTotalRoutes,'aristaFIBStatsByRouteTypeTable':aristaFIBStatsByRouteTypeTable,'aristaFIBStatsByRouteTypeEntry':aristaFIBStatsByRouteTypeEntry,_F:aristaFIBStatsRouteType,_I:aristaFIBStatsTotalRoutesForRouteType,'aristaFIBStatsByPrefixLenTable':aristaFIBStatsByPrefixLenTable,'aristaFIBStatsByPrefixLenEntry':aristaFIBStatsByPrefixLenEntry,_G:aristaFIBStatsPrefixLen,_J:aristaFIBStatsTotalRoutesForPrefixLen,'aristaFIBStatsMibConformance':aristaFIBStatsMibConformance,'aristaFIBStatsMibCompliances':aristaFIBStatsMibCompliances,'aristaFIBStatsMibCompliance':aristaFIBStatsMibCompliance,'aristaFIBStatsMibGroups':aristaFIBStatsMibGroups,_K:aristaFIBStatsGroup})