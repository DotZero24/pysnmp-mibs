_X='ciscoWanAtmCosbAlarmMIBGroup1'
_W='ciscoWanAtmCosbAlarmMIBGroup'
_V='cwacHCIntCellDeparts'
_U='cwacHCIntCellDiscards'
_T='cwacHCIntCellArrivals'
_S='cwacHighIntCellDeparts'
_R='cwacHighIntCellDiscards'
_Q='cwacHighIntCellArrivals'
_P='deprecated'
_O='cwacIntervalNumber'
_N='not-accessible'
_M='cwacIntCellDeparts'
_L='cwacIntCellDiscards'
_K='cwacIntCellArrivals'
_J='cwacValidIntervals'
_I='cwacStatsAlarmStatus'
_H='cwacCosbCurrentCellsDiscThres'
_G='cwacCosbIndex'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-WAN-ATM-COSB-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanAtmCosbMIB=ModuleIdentity((1,3,6,1,4,1,351,150,16))
if mibBuilder.loadTexts:ciscoWanAtmCosbMIB.setRevisions(('2003-03-21 00:00','2002-06-10 00:00','2000-04-17 00:00'))
_CiscoWanAtmCosbMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanAtmCosbMIBObjects=_CiscoWanAtmCosbMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,16,1))
_CwacConfig_ObjectIdentity=ObjectIdentity
cwacConfig=_CwacConfig_ObjectIdentity((1,3,6,1,4,1,351,150,16,1,1))
_CwacStatistics_ObjectIdentity=ObjectIdentity
cwacStatistics=_CwacStatistics_ObjectIdentity((1,3,6,1,4,1,351,150,16,1,2))
_CwacStatsAlarmConfgTable_Object=MibTable
cwacStatsAlarmConfgTable=_CwacStatsAlarmConfgTable_Object((1,3,6,1,4,1,351,150,16,1,2,1))
if mibBuilder.loadTexts:cwacStatsAlarmConfgTable.setStatus(_B)
_CwacStatsAlarmConfgEntry_Object=MibTableRow
cwacStatsAlarmConfgEntry=_CwacStatsAlarmConfgEntry_Object((1,3,6,1,4,1,351,150,16,1,2,1,1))
cwacStatsAlarmConfgEntry.setIndexNames((0,_E,_F),(0,_A,_G))
if mibBuilder.loadTexts:cwacStatsAlarmConfgEntry.setStatus(_B)
class _CwacCosbIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CwacCosbIndex_Type.__name__=_D
_CwacCosbIndex_Object=MibTableColumn
cwacCosbIndex=_CwacCosbIndex_Object((1,3,6,1,4,1,351,150,16,1,2,1,1,1),_CwacCosbIndex_Type())
cwacCosbIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cwacCosbIndex.setStatus(_B)
class _CwacCosbCurrentCellsDiscThres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwacCosbCurrentCellsDiscThres_Type.__name__=_D
_CwacCosbCurrentCellsDiscThres_Object=MibTableColumn
cwacCosbCurrentCellsDiscThres=_CwacCosbCurrentCellsDiscThres_Object((1,3,6,1,4,1,351,150,16,1,2,1,1,2),_CwacCosbCurrentCellsDiscThres_Type())
cwacCosbCurrentCellsDiscThres.setMaxAccess('read-write')
if mibBuilder.loadTexts:cwacCosbCurrentCellsDiscThres.setStatus(_B)
class _CwacStatsAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwacStatsAlarmStatus_Type.__name__=_D
_CwacStatsAlarmStatus_Object=MibTableColumn
cwacStatsAlarmStatus=_CwacStatsAlarmStatus_Object((1,3,6,1,4,1,351,150,16,1,2,1,1,3),_CwacStatsAlarmStatus_Type())
cwacStatsAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacStatsAlarmStatus.setStatus(_B)
class _CwacValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_CwacValidIntervals_Type.__name__=_D
_CwacValidIntervals_Object=MibTableColumn
cwacValidIntervals=_CwacValidIntervals_Object((1,3,6,1,4,1,351,150,16,1,2,1,1,4),_CwacValidIntervals_Type())
cwacValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacValidIntervals.setStatus(_B)
_CwacIntervalTable_Object=MibTable
cwacIntervalTable=_CwacIntervalTable_Object((1,3,6,1,4,1,351,150,16,1,2,2))
if mibBuilder.loadTexts:cwacIntervalTable.setStatus(_B)
_CwacIntervalEntry_Object=MibTableRow
cwacIntervalEntry=_CwacIntervalEntry_Object((1,3,6,1,4,1,351,150,16,1,2,2,1))
cwacIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_G),(0,_A,_O))
if mibBuilder.loadTexts:cwacIntervalEntry.setStatus(_B)
class _CwacIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_CwacIntervalNumber_Type.__name__=_D
_CwacIntervalNumber_Object=MibTableColumn
cwacIntervalNumber=_CwacIntervalNumber_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,1),_CwacIntervalNumber_Type())
cwacIntervalNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:cwacIntervalNumber.setStatus(_B)
_CwacIntCellArrivals_Type=Counter32
_CwacIntCellArrivals_Object=MibTableColumn
cwacIntCellArrivals=_CwacIntCellArrivals_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,2),_CwacIntCellArrivals_Type())
cwacIntCellArrivals.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacIntCellArrivals.setStatus(_B)
_CwacIntCellDiscards_Type=Counter32
_CwacIntCellDiscards_Object=MibTableColumn
cwacIntCellDiscards=_CwacIntCellDiscards_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,3),_CwacIntCellDiscards_Type())
cwacIntCellDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacIntCellDiscards.setStatus(_B)
_CwacIntCellDeparts_Type=Counter32
_CwacIntCellDeparts_Object=MibTableColumn
cwacIntCellDeparts=_CwacIntCellDeparts_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,4),_CwacIntCellDeparts_Type())
cwacIntCellDeparts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacIntCellDeparts.setStatus(_B)
_CwacHighIntCellArrivals_Type=Counter32
_CwacHighIntCellArrivals_Object=MibTableColumn
cwacHighIntCellArrivals=_CwacHighIntCellArrivals_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,5),_CwacHighIntCellArrivals_Type())
cwacHighIntCellArrivals.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacHighIntCellArrivals.setStatus(_B)
_CwacHighIntCellDiscards_Type=Counter32
_CwacHighIntCellDiscards_Object=MibTableColumn
cwacHighIntCellDiscards=_CwacHighIntCellDiscards_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,6),_CwacHighIntCellDiscards_Type())
cwacHighIntCellDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacHighIntCellDiscards.setStatus(_B)
_CwacHighIntCellDeparts_Type=Counter32
_CwacHighIntCellDeparts_Object=MibTableColumn
cwacHighIntCellDeparts=_CwacHighIntCellDeparts_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,7),_CwacHighIntCellDeparts_Type())
cwacHighIntCellDeparts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacHighIntCellDeparts.setStatus(_B)
_CwacHCIntCellArrivals_Type=Counter64
_CwacHCIntCellArrivals_Object=MibTableColumn
cwacHCIntCellArrivals=_CwacHCIntCellArrivals_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,8),_CwacHCIntCellArrivals_Type())
cwacHCIntCellArrivals.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacHCIntCellArrivals.setStatus(_B)
_CwacHCIntCellDiscards_Type=Counter64
_CwacHCIntCellDiscards_Object=MibTableColumn
cwacHCIntCellDiscards=_CwacHCIntCellDiscards_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,9),_CwacHCIntCellDiscards_Type())
cwacHCIntCellDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacHCIntCellDiscards.setStatus(_B)
_CwacHCIntCellDeparts_Type=Counter64
_CwacHCIntCellDeparts_Object=MibTableColumn
cwacHCIntCellDeparts=_CwacHCIntCellDeparts_Object((1,3,6,1,4,1,351,150,16,1,2,2,1,10),_CwacHCIntCellDeparts_Type())
cwacHCIntCellDeparts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwacHCIntCellDeparts.setStatus(_B)
_CiscoWanAtmCosbMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanAtmCosbMIBConformance=_CiscoWanAtmCosbMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,16,2))
_CiscoWanAtmCosbMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanAtmCosbMIBCompliances=_CiscoWanAtmCosbMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,16,2,1))
_CiscoWanAtmCosbMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanAtmCosbMIBGroups=_CiscoWanAtmCosbMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,16,2,2))
ciscoWanAtmCosbAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,16,2,2,1))
ciscoWanAtmCosbAlarmMIBGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoWanAtmCosbAlarmMIBGroup.setStatus(_P)
ciscoWanAtmCosbAlarmMIBGroup1=ObjectGroup((1,3,6,1,4,1,351,150,16,2,2,2))
ciscoWanAtmCosbAlarmMIBGroup1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoWanAtmCosbAlarmMIBGroup1.setStatus(_B)
ciscoHCWanAtmCosbAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,16,2,2,3))
ciscoHCWanAtmCosbAlarmMIBGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoHCWanAtmCosbAlarmMIBGroup.setStatus(_B)
ciscoWanAtmCosbMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,16,2,1,1))
ciscoWanAtmCosbMIBCompliance.setObjects((_A,_W))
if mibBuilder.loadTexts:ciscoWanAtmCosbMIBCompliance.setStatus(_P)
ciscoWanAtmCosbMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,351,150,16,2,1,2))
ciscoWanAtmCosbMIBCompliance1.setObjects((_A,_X))
if mibBuilder.loadTexts:ciscoWanAtmCosbMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoWanAtmCosbMIB':ciscoWanAtmCosbMIB,'ciscoWanAtmCosbMIBObjects':ciscoWanAtmCosbMIBObjects,'cwacConfig':cwacConfig,'cwacStatistics':cwacStatistics,'cwacStatsAlarmConfgTable':cwacStatsAlarmConfgTable,'cwacStatsAlarmConfgEntry':cwacStatsAlarmConfgEntry,_G:cwacCosbIndex,_H:cwacCosbCurrentCellsDiscThres,_I:cwacStatsAlarmStatus,_J:cwacValidIntervals,'cwacIntervalTable':cwacIntervalTable,'cwacIntervalEntry':cwacIntervalEntry,_O:cwacIntervalNumber,_K:cwacIntCellArrivals,_L:cwacIntCellDiscards,_M:cwacIntCellDeparts,_Q:cwacHighIntCellArrivals,_R:cwacHighIntCellDiscards,_S:cwacHighIntCellDeparts,_T:cwacHCIntCellArrivals,_U:cwacHCIntCellDiscards,_V:cwacHCIntCellDeparts,'ciscoWanAtmCosbMIBConformance':ciscoWanAtmCosbMIBConformance,'ciscoWanAtmCosbMIBCompliances':ciscoWanAtmCosbMIBCompliances,'ciscoWanAtmCosbMIBCompliance':ciscoWanAtmCosbMIBCompliance,'ciscoWanAtmCosbMIBCompliance1':ciscoWanAtmCosbMIBCompliance1,'ciscoWanAtmCosbMIBGroups':ciscoWanAtmCosbMIBGroups,_W:ciscoWanAtmCosbAlarmMIBGroup,_X:ciscoWanAtmCosbAlarmMIBGroup1,'ciscoHCWanAtmCosbAlarmMIBGroup':ciscoHCWanAtmCosbAlarmMIBGroup})