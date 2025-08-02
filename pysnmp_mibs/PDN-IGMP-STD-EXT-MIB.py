_a='pdnIgmpStdExtGeneralConfigGroupV2'
_Z='pdnIgmpStdExtGeneralConfigGroup'
_Y='pdnIgmpGeneralQueryInterval'
_X='deprecated'
_W='pdnIgmpCacheStatsIgmpLeavesOut'
_V='pdnIgmpCacheStatsIgmpLeavesIn'
_U='pdnIgmpCacheStatsIgmpReportsOut'
_T='pdnIgmpCacheStatsIgmpReportsIn'
_S='pdnIgmpCacheStatsIgmpQueriesOut'
_R='pdnIgmpCacheStatsIgmpQueriesIn'
_Q='pdnIgmpCacheStatsMulticastPktsOut'
_P='pdnIgmpCacheStatsMulticastPktsIn'
_O='pdnIgmpInterfaceLeaveJoinForwardingDelay'
_N='pdnIgmpInterfaceLeaveDelay'
_M='pdnIgmpInterfaceSnoopEnableDisable'
_L='pdnIgmpCacheExtEntry'
_K='pdnIgmpInterfaceExtEntry'
_J='tenths of a second'
_I='pdnIgmpStdExtStatsGroup'
_H='pdnIgmpStdExtConfigGroup'
_G='pdnIgmpSnoopingSelection'
_F='SwitchState'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='current'
_A='PDN-IGMP-STD-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
igmpCacheEntry,igmpInterfaceEntry=mibBuilder.importSymbols('IGMP-STD-MIB','igmpCacheEntry','igmpInterfaceEntry')
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
SwitchState,=mibBuilder.importSymbols('PDN-TC',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnIgmpStdExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,47))
if mibBuilder.loadTexts:pdnIgmpStdExtMIB.setRevisions(('2004-08-17 00:00','2004-01-08 00:00','2003-05-06 00:00','2003-05-01 00:00'))
_PdnIgmpStdExtNotifications_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtNotifications=_PdnIgmpStdExtNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,0))
_PdnIgmpStdExtObjects_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtObjects=_PdnIgmpStdExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,1))
_PdnIgmpInterfaceExtTable_Object=MibTable
pdnIgmpInterfaceExtTable=_PdnIgmpInterfaceExtTable_Object((1,3,6,1,4,1,1795,2,24,2,47,1,1))
if mibBuilder.loadTexts:pdnIgmpInterfaceExtTable.setStatus(_B)
_PdnIgmpInterfaceExtEntry_Object=MibTableRow
pdnIgmpInterfaceExtEntry=_PdnIgmpInterfaceExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,47,1,1,1))
if mibBuilder.loadTexts:pdnIgmpInterfaceExtEntry.setStatus(_B)
class _PdnIgmpInterfaceSnoopEnableDisable_Type(SwitchState):defaultValue=2
_PdnIgmpInterfaceSnoopEnableDisable_Type.__name__=_F
_PdnIgmpInterfaceSnoopEnableDisable_Object=MibTableColumn
pdnIgmpInterfaceSnoopEnableDisable=_PdnIgmpInterfaceSnoopEnableDisable_Object((1,3,6,1,4,1,1795,2,24,2,47,1,1,1,1),_PdnIgmpInterfaceSnoopEnableDisable_Type())
pdnIgmpInterfaceSnoopEnableDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnIgmpInterfaceSnoopEnableDisable.setStatus(_B)
class _PdnIgmpInterfaceLeaveDelay_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PdnIgmpInterfaceLeaveDelay_Type.__name__=_E
_PdnIgmpInterfaceLeaveDelay_Object=MibTableColumn
pdnIgmpInterfaceLeaveDelay=_PdnIgmpInterfaceLeaveDelay_Object((1,3,6,1,4,1,1795,2,24,2,47,1,1,1,2),_PdnIgmpInterfaceLeaveDelay_Type())
pdnIgmpInterfaceLeaveDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnIgmpInterfaceLeaveDelay.setStatus(_B)
if mibBuilder.loadTexts:pdnIgmpInterfaceLeaveDelay.setUnits(_J)
class _PdnIgmpInterfaceLeaveJoinForwardingDelay_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PdnIgmpInterfaceLeaveJoinForwardingDelay_Type.__name__=_E
_PdnIgmpInterfaceLeaveJoinForwardingDelay_Object=MibTableColumn
pdnIgmpInterfaceLeaveJoinForwardingDelay=_PdnIgmpInterfaceLeaveJoinForwardingDelay_Object((1,3,6,1,4,1,1795,2,24,2,47,1,1,1,3),_PdnIgmpInterfaceLeaveJoinForwardingDelay_Type())
pdnIgmpInterfaceLeaveJoinForwardingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnIgmpInterfaceLeaveJoinForwardingDelay.setStatus(_B)
if mibBuilder.loadTexts:pdnIgmpInterfaceLeaveJoinForwardingDelay.setUnits(_J)
_PdnIgmpCacheExtTable_Object=MibTable
pdnIgmpCacheExtTable=_PdnIgmpCacheExtTable_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2))
if mibBuilder.loadTexts:pdnIgmpCacheExtTable.setStatus(_B)
_PdnIgmpCacheExtEntry_Object=MibTableRow
pdnIgmpCacheExtEntry=_PdnIgmpCacheExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1))
if mibBuilder.loadTexts:pdnIgmpCacheExtEntry.setStatus(_B)
_PdnIgmpCacheStatsMulticastPktsIn_Type=Counter32
_PdnIgmpCacheStatsMulticastPktsIn_Object=MibTableColumn
pdnIgmpCacheStatsMulticastPktsIn=_PdnIgmpCacheStatsMulticastPktsIn_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,1),_PdnIgmpCacheStatsMulticastPktsIn_Type())
pdnIgmpCacheStatsMulticastPktsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsMulticastPktsIn.setStatus(_B)
_PdnIgmpCacheStatsMulticastPktsOut_Type=Counter32
_PdnIgmpCacheStatsMulticastPktsOut_Object=MibTableColumn
pdnIgmpCacheStatsMulticastPktsOut=_PdnIgmpCacheStatsMulticastPktsOut_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,2),_PdnIgmpCacheStatsMulticastPktsOut_Type())
pdnIgmpCacheStatsMulticastPktsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsMulticastPktsOut.setStatus(_B)
_PdnIgmpCacheStatsIgmpQueriesIn_Type=Counter32
_PdnIgmpCacheStatsIgmpQueriesIn_Object=MibTableColumn
pdnIgmpCacheStatsIgmpQueriesIn=_PdnIgmpCacheStatsIgmpQueriesIn_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,3),_PdnIgmpCacheStatsIgmpQueriesIn_Type())
pdnIgmpCacheStatsIgmpQueriesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsIgmpQueriesIn.setStatus(_B)
_PdnIgmpCacheStatsIgmpQueriesOut_Type=Counter32
_PdnIgmpCacheStatsIgmpQueriesOut_Object=MibTableColumn
pdnIgmpCacheStatsIgmpQueriesOut=_PdnIgmpCacheStatsIgmpQueriesOut_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,4),_PdnIgmpCacheStatsIgmpQueriesOut_Type())
pdnIgmpCacheStatsIgmpQueriesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsIgmpQueriesOut.setStatus(_B)
_PdnIgmpCacheStatsIgmpReportsIn_Type=Counter32
_PdnIgmpCacheStatsIgmpReportsIn_Object=MibTableColumn
pdnIgmpCacheStatsIgmpReportsIn=_PdnIgmpCacheStatsIgmpReportsIn_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,5),_PdnIgmpCacheStatsIgmpReportsIn_Type())
pdnIgmpCacheStatsIgmpReportsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsIgmpReportsIn.setStatus(_B)
_PdnIgmpCacheStatsIgmpReportsOut_Type=Counter32
_PdnIgmpCacheStatsIgmpReportsOut_Object=MibTableColumn
pdnIgmpCacheStatsIgmpReportsOut=_PdnIgmpCacheStatsIgmpReportsOut_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,6),_PdnIgmpCacheStatsIgmpReportsOut_Type())
pdnIgmpCacheStatsIgmpReportsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsIgmpReportsOut.setStatus(_B)
_PdnIgmpCacheStatsIgmpLeavesIn_Type=Counter32
_PdnIgmpCacheStatsIgmpLeavesIn_Object=MibTableColumn
pdnIgmpCacheStatsIgmpLeavesIn=_PdnIgmpCacheStatsIgmpLeavesIn_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,7),_PdnIgmpCacheStatsIgmpLeavesIn_Type())
pdnIgmpCacheStatsIgmpLeavesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsIgmpLeavesIn.setStatus(_B)
_PdnIgmpCacheStatsIgmpLeavesOut_Type=Counter32
_PdnIgmpCacheStatsIgmpLeavesOut_Object=MibTableColumn
pdnIgmpCacheStatsIgmpLeavesOut=_PdnIgmpCacheStatsIgmpLeavesOut_Object((1,3,6,1,4,1,1795,2,24,2,47,1,2,1,8),_PdnIgmpCacheStatsIgmpLeavesOut_Type())
pdnIgmpCacheStatsIgmpLeavesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIgmpCacheStatsIgmpLeavesOut.setStatus(_B)
class _PdnIgmpSnoopingSelection_Type(SwitchState):defaultValue=2
_PdnIgmpSnoopingSelection_Type.__name__=_F
_PdnIgmpSnoopingSelection_Object=MibScalar
pdnIgmpSnoopingSelection=_PdnIgmpSnoopingSelection_Object((1,3,6,1,4,1,1795,2,24,2,47,1,3),_PdnIgmpSnoopingSelection_Type())
pdnIgmpSnoopingSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnIgmpSnoopingSelection.setStatus(_B)
class _PdnIgmpGeneralQueryInterval_Type(Unsigned32):defaultValue=125
_PdnIgmpGeneralQueryInterval_Type.__name__=_E
_PdnIgmpGeneralQueryInterval_Object=MibScalar
pdnIgmpGeneralQueryInterval=_PdnIgmpGeneralQueryInterval_Object((1,3,6,1,4,1,1795,2,24,2,47,1,4),_PdnIgmpGeneralQueryInterval_Type())
pdnIgmpGeneralQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnIgmpGeneralQueryInterval.setStatus(_B)
if mibBuilder.loadTexts:pdnIgmpGeneralQueryInterval.setUnits('seconds')
_PdnIgmpStdExtAFNs_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtAFNs=_PdnIgmpStdExtAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,2))
_PdnIgmpStdExtConformance_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtConformance=_PdnIgmpStdExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,3))
_PdnIgmpStdExtCompliances_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtCompliances=_PdnIgmpStdExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,3,1))
_PdnIgmpStdExtGroups_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtGroups=_PdnIgmpStdExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,3,2))
_PdnIgmpStdExtObjGroups_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtObjGroups=_PdnIgmpStdExtObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,3,2,1))
_PdnIgmpStdExtAfnGroups_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtAfnGroups=_PdnIgmpStdExtAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,3,2,2))
_PdnIgmpStdExtNtfyGroups_ObjectIdentity=ObjectIdentity
pdnIgmpStdExtNtfyGroups=_PdnIgmpStdExtNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,47,3,2,3))
igmpInterfaceEntry.registerAugmentions((_A,_K))
pdnIgmpInterfaceExtEntry.setIndexNames(*igmpInterfaceEntry.getIndexNames())
igmpCacheEntry.registerAugmentions((_A,_L))
pdnIgmpCacheExtEntry.setIndexNames(*igmpCacheEntry.getIndexNames())
pdnIgmpStdExtConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,47,3,2,1,1))
pdnIgmpStdExtConfigGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:pdnIgmpStdExtConfigGroup.setStatus(_B)
pdnIgmpStdExtStatsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,47,3,2,1,2))
pdnIgmpStdExtStatsGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:pdnIgmpStdExtStatsGroup.setStatus(_B)
pdnIgmpStdExtGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,47,3,2,1,3))
pdnIgmpStdExtGeneralConfigGroup.setObjects((_A,_G))
if mibBuilder.loadTexts:pdnIgmpStdExtGeneralConfigGroup.setStatus(_X)
pdnIgmpStdExtGeneralConfigGroupV2=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,47,3,2,1,4))
pdnIgmpStdExtGeneralConfigGroupV2.setObjects(*((_A,_G),(_A,_Y)))
if mibBuilder.loadTexts:pdnIgmpStdExtGeneralConfigGroupV2.setStatus(_B)
pdnIgmpStdExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,47,3,1,1))
pdnIgmpStdExtMIBCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_Z)))
if mibBuilder.loadTexts:pdnIgmpStdExtMIBCompliance.setStatus(_X)
pdnIgmpStdExtMIBComplianceV2=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,47,3,1,2))
pdnIgmpStdExtMIBComplianceV2.setObjects(*((_A,_H),(_A,_I),(_A,_a)))
if mibBuilder.loadTexts:pdnIgmpStdExtMIBComplianceV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pdnIgmpStdExtMIB':pdnIgmpStdExtMIB,'pdnIgmpStdExtNotifications':pdnIgmpStdExtNotifications,'pdnIgmpStdExtObjects':pdnIgmpStdExtObjects,'pdnIgmpInterfaceExtTable':pdnIgmpInterfaceExtTable,_K:pdnIgmpInterfaceExtEntry,_M:pdnIgmpInterfaceSnoopEnableDisable,_N:pdnIgmpInterfaceLeaveDelay,_O:pdnIgmpInterfaceLeaveJoinForwardingDelay,'pdnIgmpCacheExtTable':pdnIgmpCacheExtTable,_L:pdnIgmpCacheExtEntry,_P:pdnIgmpCacheStatsMulticastPktsIn,_Q:pdnIgmpCacheStatsMulticastPktsOut,_R:pdnIgmpCacheStatsIgmpQueriesIn,_S:pdnIgmpCacheStatsIgmpQueriesOut,_T:pdnIgmpCacheStatsIgmpReportsIn,_U:pdnIgmpCacheStatsIgmpReportsOut,_V:pdnIgmpCacheStatsIgmpLeavesIn,_W:pdnIgmpCacheStatsIgmpLeavesOut,_G:pdnIgmpSnoopingSelection,_Y:pdnIgmpGeneralQueryInterval,'pdnIgmpStdExtAFNs':pdnIgmpStdExtAFNs,'pdnIgmpStdExtConformance':pdnIgmpStdExtConformance,'pdnIgmpStdExtCompliances':pdnIgmpStdExtCompliances,'pdnIgmpStdExtMIBCompliance':pdnIgmpStdExtMIBCompliance,'pdnIgmpStdExtMIBComplianceV2':pdnIgmpStdExtMIBComplianceV2,'pdnIgmpStdExtGroups':pdnIgmpStdExtGroups,'pdnIgmpStdExtObjGroups':pdnIgmpStdExtObjGroups,_H:pdnIgmpStdExtConfigGroup,_I:pdnIgmpStdExtStatsGroup,_Z:pdnIgmpStdExtGeneralConfigGroup,_a:pdnIgmpStdExtGeneralConfigGroupV2,'pdnIgmpStdExtAfnGroups':pdnIgmpStdExtAfnGroups,'pdnIgmpStdExtNtfyGroups':pdnIgmpStdExtNtfyGroups})