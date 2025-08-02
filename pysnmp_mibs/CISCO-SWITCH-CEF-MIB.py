_c='cscMplsStatsGroupExt'
_b='cscMplsStatsGroup'
_a='cscSwitchCefEomL2Group'
_Z='cscSwitchCefIpv6LinkLocalGroup'
_Y='cscSwitchCefIpv6GlobalStatsGroup'
_X='cscTotalStatsGroup'
_W='cscSwitchCefIpv6StatsGroup'
_V='cscSwitchCefIpv4StatsGroup'
_U='cscTotalRoutes'
_T='cscEomIpv6MulticastRoutes'
_S='cscEomIpv4MulticastRoutes'
_R='cscMplsVpnRoutes'
_Q='cscMplsRoutes'
_P='cscEomL2Routes'
_O='cscIpv6LinkLocalRoutes'
_N='cscIpv6GlobalRoutes'
_M='cscIpv6UnicastRoutes'
_L='cscIpv6MulticastRoutes'
_K='cscIpv6VrfRoutes'
_J='cscIpv6NonVrfRoutes'
_I='cscIpv4UnicastRoutes'
_H='cscIpv4MulticastRoutes'
_G='cscIpv4VrfRoutes'
_F='cscIpv4NonVrfRoutes'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-SWITCH-CEF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSwitchCefMIB=ModuleIdentity((1,3,6,1,4,1,9,9,790))
if mibBuilder.loadTexts:ciscoSwitchCefMIB.setRevisions(('2011-12-15 00:00',))
_CiscoSwitchCefMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSwitchCefMIBNotifs=_CiscoSwitchCefMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,790,0))
_CiscoSwitchCefMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchCefMIBObjects=_CiscoSwitchCefMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,790,1))
_CscStats_ObjectIdentity=ObjectIdentity
cscStats=_CscStats_ObjectIdentity((1,3,6,1,4,1,9,9,790,1,1))
_CscSwitchCefStatsTable_Object=MibTable
cscSwitchCefStatsTable=_CscSwitchCefStatsTable_Object((1,3,6,1,4,1,9,9,790,1,1,1))
if mibBuilder.loadTexts:cscSwitchCefStatsTable.setStatus(_A)
_CscSwitchCefStatsEntry_Object=MibTableRow
cscSwitchCefStatsEntry=_CscSwitchCefStatsEntry_Object((1,3,6,1,4,1,9,9,790,1,1,1,1))
cscSwitchCefStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cscSwitchCefStatsEntry.setStatus(_A)
_CscIpv4NonVrfRoutes_Type=Gauge32
_CscIpv4NonVrfRoutes_Object=MibTableColumn
cscIpv4NonVrfRoutes=_CscIpv4NonVrfRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,1),_CscIpv4NonVrfRoutes_Type())
cscIpv4NonVrfRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv4NonVrfRoutes.setStatus(_A)
_CscIpv4VrfRoutes_Type=Gauge32
_CscIpv4VrfRoutes_Object=MibTableColumn
cscIpv4VrfRoutes=_CscIpv4VrfRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,2),_CscIpv4VrfRoutes_Type())
cscIpv4VrfRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv4VrfRoutes.setStatus(_A)
_CscIpv4MulticastRoutes_Type=Gauge32
_CscIpv4MulticastRoutes_Object=MibTableColumn
cscIpv4MulticastRoutes=_CscIpv4MulticastRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,3),_CscIpv4MulticastRoutes_Type())
cscIpv4MulticastRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv4MulticastRoutes.setStatus(_A)
_CscIpv4UnicastRoutes_Type=Gauge32
_CscIpv4UnicastRoutes_Object=MibTableColumn
cscIpv4UnicastRoutes=_CscIpv4UnicastRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,4),_CscIpv4UnicastRoutes_Type())
cscIpv4UnicastRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv4UnicastRoutes.setStatus(_A)
_CscIpv6GlobalRoutes_Type=Gauge32
_CscIpv6GlobalRoutes_Object=MibTableColumn
cscIpv6GlobalRoutes=_CscIpv6GlobalRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,5),_CscIpv6GlobalRoutes_Type())
cscIpv6GlobalRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv6GlobalRoutes.setStatus(_A)
_CscIpv6NonVrfRoutes_Type=Gauge32
_CscIpv6NonVrfRoutes_Object=MibTableColumn
cscIpv6NonVrfRoutes=_CscIpv6NonVrfRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,6),_CscIpv6NonVrfRoutes_Type())
cscIpv6NonVrfRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv6NonVrfRoutes.setStatus(_A)
_CscIpv6VrfRoutes_Type=Gauge32
_CscIpv6VrfRoutes_Object=MibTableColumn
cscIpv6VrfRoutes=_CscIpv6VrfRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,7),_CscIpv6VrfRoutes_Type())
cscIpv6VrfRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv6VrfRoutes.setStatus(_A)
_CscIpv6LinkLocalRoutes_Type=Gauge32
_CscIpv6LinkLocalRoutes_Object=MibTableColumn
cscIpv6LinkLocalRoutes=_CscIpv6LinkLocalRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,8),_CscIpv6LinkLocalRoutes_Type())
cscIpv6LinkLocalRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv6LinkLocalRoutes.setStatus(_A)
_CscIpv6MulticastRoutes_Type=Gauge32
_CscIpv6MulticastRoutes_Object=MibTableColumn
cscIpv6MulticastRoutes=_CscIpv6MulticastRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,9),_CscIpv6MulticastRoutes_Type())
cscIpv6MulticastRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv6MulticastRoutes.setStatus(_A)
_CscIpv6UnicastRoutes_Type=Gauge32
_CscIpv6UnicastRoutes_Object=MibTableColumn
cscIpv6UnicastRoutes=_CscIpv6UnicastRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,10),_CscIpv6UnicastRoutes_Type())
cscIpv6UnicastRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscIpv6UnicastRoutes.setStatus(_A)
_CscMplsRoutes_Type=Gauge32
_CscMplsRoutes_Object=MibTableColumn
cscMplsRoutes=_CscMplsRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,11),_CscMplsRoutes_Type())
cscMplsRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscMplsRoutes.setStatus(_A)
_CscMplsVpnRoutes_Type=Gauge32
_CscMplsVpnRoutes_Object=MibTableColumn
cscMplsVpnRoutes=_CscMplsVpnRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,12),_CscMplsVpnRoutes_Type())
cscMplsVpnRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscMplsVpnRoutes.setStatus(_A)
_CscEomL2Routes_Type=Gauge32
_CscEomL2Routes_Object=MibTableColumn
cscEomL2Routes=_CscEomL2Routes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,13),_CscEomL2Routes_Type())
cscEomL2Routes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscEomL2Routes.setStatus(_A)
_CscEomIpv4MulticastRoutes_Type=Gauge32
_CscEomIpv4MulticastRoutes_Object=MibTableColumn
cscEomIpv4MulticastRoutes=_CscEomIpv4MulticastRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,14),_CscEomIpv4MulticastRoutes_Type())
cscEomIpv4MulticastRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscEomIpv4MulticastRoutes.setStatus(_A)
_CscEomIpv6MulticastRoutes_Type=Gauge32
_CscEomIpv6MulticastRoutes_Object=MibTableColumn
cscEomIpv6MulticastRoutes=_CscEomIpv6MulticastRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,15),_CscEomIpv6MulticastRoutes_Type())
cscEomIpv6MulticastRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscEomIpv6MulticastRoutes.setStatus(_A)
_CscTotalRoutes_Type=Gauge32
_CscTotalRoutes_Object=MibTableColumn
cscTotalRoutes=_CscTotalRoutes_Object((1,3,6,1,4,1,9,9,790,1,1,1,1,16),_CscTotalRoutes_Type())
cscTotalRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTotalRoutes.setStatus(_A)
_CiscoSwitchCefMIBConform_ObjectIdentity=ObjectIdentity
ciscoSwitchCefMIBConform=_CiscoSwitchCefMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,790,2))
_CscSwitchCefMIBCompliances_ObjectIdentity=ObjectIdentity
cscSwitchCefMIBCompliances=_CscSwitchCefMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,790,2,1))
_CscSwitchCefMIBGroups_ObjectIdentity=ObjectIdentity
cscSwitchCefMIBGroups=_CscSwitchCefMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,790,2,2))
cscSwitchCefIpv4StatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,1))
cscSwitchCefIpv4StatsGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cscSwitchCefIpv4StatsGroup.setStatus(_A)
cscSwitchCefIpv6StatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,2))
cscSwitchCefIpv6StatsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cscSwitchCefIpv6StatsGroup.setStatus(_A)
cscSwitchCefIpv6GlobalStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,3))
cscSwitchCefIpv6GlobalStatsGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:cscSwitchCefIpv6GlobalStatsGroup.setStatus(_A)
cscSwitchCefIpv6LinkLocalGroup=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,4))
cscSwitchCefIpv6LinkLocalGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:cscSwitchCefIpv6LinkLocalGroup.setStatus(_A)
cscSwitchCefEomL2Group=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,5))
cscSwitchCefEomL2Group.setObjects((_B,_P))
if mibBuilder.loadTexts:cscSwitchCefEomL2Group.setStatus(_A)
cscMplsStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,6))
cscMplsStatsGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:cscMplsStatsGroup.setStatus(_A)
cscMplsStatsGroupExt=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,7))
cscMplsStatsGroupExt.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cscMplsStatsGroupExt.setStatus(_A)
cscTotalStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,790,2,2,8))
cscTotalStatsGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:cscTotalStatsGroup.setStatus(_A)
cscSwitchCefMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,790,2,1,1))
cscSwitchCefMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cscSwitchCefMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSwitchCefMIB':ciscoSwitchCefMIB,'ciscoSwitchCefMIBNotifs':ciscoSwitchCefMIBNotifs,'ciscoSwitchCefMIBObjects':ciscoSwitchCefMIBObjects,'cscStats':cscStats,'cscSwitchCefStatsTable':cscSwitchCefStatsTable,'cscSwitchCefStatsEntry':cscSwitchCefStatsEntry,_F:cscIpv4NonVrfRoutes,_G:cscIpv4VrfRoutes,_H:cscIpv4MulticastRoutes,_I:cscIpv4UnicastRoutes,_N:cscIpv6GlobalRoutes,_J:cscIpv6NonVrfRoutes,_K:cscIpv6VrfRoutes,_O:cscIpv6LinkLocalRoutes,_L:cscIpv6MulticastRoutes,_M:cscIpv6UnicastRoutes,_Q:cscMplsRoutes,_R:cscMplsVpnRoutes,_P:cscEomL2Routes,_S:cscEomIpv4MulticastRoutes,_T:cscEomIpv6MulticastRoutes,_U:cscTotalRoutes,'ciscoSwitchCefMIBConform':ciscoSwitchCefMIBConform,'cscSwitchCefMIBCompliances':cscSwitchCefMIBCompliances,'cscSwitchCefMIBCompliance':cscSwitchCefMIBCompliance,'cscSwitchCefMIBGroups':cscSwitchCefMIBGroups,_V:cscSwitchCefIpv4StatsGroup,_W:cscSwitchCefIpv6StatsGroup,_Y:cscSwitchCefIpv6GlobalStatsGroup,_Z:cscSwitchCefIpv6LinkLocalGroup,_a:cscSwitchCefEomL2Group,_b:cscMplsStatsGroup,_c:cscMplsStatsGroupExt,_X:cscTotalStatsGroup})