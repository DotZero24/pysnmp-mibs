_Ab='ciscoSwitchStatsRewriteEngineStatsGroup'
_Aa='ciscoSwitchStatsInternalInstanceGroup'
_AZ='ciscoSwitchStatsInternalErrorGroup'
_AY='ciscoSwitchStatsInternalStatsGroup'
_AX='ciscoSwitchStatsTotalGroup'
_AW='ciscoSwitchStatsLayer3ExtGroup'
_AV='ciscoSwitchStatsLayer3Group'
_AU='ciscoSwitchStatsL3Group'
_AT='csstRewriteEngineTotalOverruns'
_AS='csstRewriteEngineDropPkts'
_AR='csstHwInternalErrorInstPorts'
_AQ='csstHwInternalErrorInstCount'
_AP='csstHwInternalErrorInstDescr'
_AO='csstHwInternalErrorLastCleared'
_AN='csstHwInternalErrorDeviceInfo'
_AM='csstHwInternalStatsRate'
_AL='csstHwInternalStatsDescr'
_AK='csstTotalAclDenyPkts'
_AJ='csstL3TotalAclRoutedPkts'
_AI='csstL3TotalNetflowSwitchedPkts'
_AH='deprecated'
_AG='csstL2TotalBridgedPkts'
_AF='csstVlanKnownBridgedNUcastOctets'
_AE='csstVlanKnownBridgedNUcastPkts'
_AD='csstVlanKnownBridgedUcastOctets'
_AC='csstVlanKnownBridgedUcastPkts'
_AB='csstConfigStatsIfOctets8'
_AA='csstConfigStatsIfPackets8'
_A9='csstConfigStatsIfOctets7'
_A8='csstConfigStatsIfPackets7'
_A7='csstConfigStatsIfOctets6'
_A6='csstConfigStatsIfPackets6'
_A5='csstConfigStatsIfOctets5'
_A4='csstConfigStatsIfPackets5'
_A3='csstConfigStatsIfOctets4'
_A2='csstConfigStatsIfPackets4'
_A1='csstConfigStatsIfOctets3'
_A0='csstConfigStatsIfPackets3'
_z='csstConfigStatsIfOctets2'
_y='csstConfigStatsIfPackets2'
_x='csstConfigStatsIfOctets1'
_w='csstConfigStatsIfPackets1'
_v='csstConfigStatsMap'
_u='csstConfigStatsMapSize'
_t='csstConfigStatsOptionDesc'
_s='csstRewriteEngineChannelIndex'
_r='csstHwInternalErrorInstErrorId'
_q='csstHwInternalErrorInstNum'
_p='csstHwInternalStatsIndex'
_o='csstHwInternalStatsType'
_n='csstHwInternalStatsDirection'
_m='csstHwInternalStatsInstanceNum'
_l='csstHwInternalStatsDeviceId'
_k='csstVlanIndex'
_j='csstConfigStatsOptionIndex'
_i='Unsigned32'
_h='ifIndex'
_g='IF-MIB'
_f='OctetString'
_e='ciscoSwitchStatsL2Group'
_d='ciscoSwitchStatsVlanGroup'
_c='ciscoSwitchStatsConfIfGroup'
_b='ciscoSwitchStatsConfMapGroup'
_a='ciscoSwitchStatsConfOptionGroup'
_Z='csstL3OutExceptionRedirectPkts'
_Y='csstL3InExceptionRedirectPkts'
_X='csstL3OutputNetflowSwitchedPkts'
_W='csstL3InputNetflowSwitchedPkts'
_V='csstL3OutputAclRoutedPkts'
_U='csstL3InputAclRoutedPkts'
_T='csstL3MulticastLeakPkts'
_S='csstL3Ipv6MulticastPkts'
_R='csstL3Ipv4MulticastPkts'
_Q='csstL3IgmpMldPkts'
_P='csstL3TotalMulticastPkts'
_O='csstL3FibSwitchedMplsPkts'
_N='csstL3FibSwitchedEoMplsPkts'
_M='csstL3FibSwitchedIpv6UcastPkts'
_L='csstL3FibSwitchedIpv4UcastPkts'
_K='csstHwInternalErrorCategory'
_J='csstHwInternalErrorDeviceId'
_I='Integer32'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='octets'
_E='not-accessible'
_D='packets'
_C='read-only'
_B='current'
_A='CISCO-SWITCH-STATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_f,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
ifIndex,=mibBuilder.importSymbols(_g,_h)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_i,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ciscoSwitchStatsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,652))
if mibBuilder.loadTexts:ciscoSwitchStatsMIB.setRevisions(('2013-01-30 00:00','2009-10-30 00:00'))
_CiscoSwitchStatsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSwitchStatsMIBNotifs=_CiscoSwitchStatsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,652,0))
_CiscoSwitchStatsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchStatsMIBObjects=_CiscoSwitchStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,652,1))
_CsstConfigurableStats_ObjectIdentity=ObjectIdentity
csstConfigurableStats=_CsstConfigurableStats_ObjectIdentity((1,3,6,1,4,1,9,9,652,1,1))
_CsstConfigStatsOptionTable_Object=MibTable
csstConfigStatsOptionTable=_CsstConfigStatsOptionTable_Object((1,3,6,1,4,1,9,9,652,1,1,1))
if mibBuilder.loadTexts:csstConfigStatsOptionTable.setStatus(_B)
_CsstConfigStatsOptionEntry_Object=MibTableRow
csstConfigStatsOptionEntry=_CsstConfigStatsOptionEntry_Object((1,3,6,1,4,1,9,9,652,1,1,1,1))
csstConfigStatsOptionEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:csstConfigStatsOptionEntry.setStatus(_B)
class _CsstConfigStatsOptionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CsstConfigStatsOptionIndex_Type.__name__=_i
_CsstConfigStatsOptionIndex_Object=MibTableColumn
csstConfigStatsOptionIndex=_CsstConfigStatsOptionIndex_Object((1,3,6,1,4,1,9,9,652,1,1,1,1,1),_CsstConfigStatsOptionIndex_Type())
csstConfigStatsOptionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:csstConfigStatsOptionIndex.setStatus(_B)
_CsstConfigStatsOptionDesc_Type=SnmpAdminString
_CsstConfigStatsOptionDesc_Object=MibTableColumn
csstConfigStatsOptionDesc=_CsstConfigStatsOptionDesc_Object((1,3,6,1,4,1,9,9,652,1,1,1,1,2),_CsstConfigStatsOptionDesc_Type())
csstConfigStatsOptionDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsOptionDesc.setStatus(_B)
_CsstConfigStatsMapSize_Type=Unsigned32
_CsstConfigStatsMapSize_Object=MibScalar
csstConfigStatsMapSize=_CsstConfigStatsMapSize_Object((1,3,6,1,4,1,9,9,652,1,1,2),_CsstConfigStatsMapSize_Type())
csstConfigStatsMapSize.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsMapSize.setStatus(_B)
class _CsstConfigStatsMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CsstConfigStatsMap_Type.__name__=_f
_CsstConfigStatsMap_Object=MibScalar
csstConfigStatsMap=_CsstConfigStatsMap_Object((1,3,6,1,4,1,9,9,652,1,1,3),_CsstConfigStatsMap_Type())
csstConfigStatsMap.setMaxAccess('read-write')
if mibBuilder.loadTexts:csstConfigStatsMap.setStatus(_B)
_CsstConfigStatsIfTable_Object=MibTable
csstConfigStatsIfTable=_CsstConfigStatsIfTable_Object((1,3,6,1,4,1,9,9,652,1,1,4))
if mibBuilder.loadTexts:csstConfigStatsIfTable.setStatus(_B)
_CsstConfigStatsIfEntry_Object=MibTableRow
csstConfigStatsIfEntry=_CsstConfigStatsIfEntry_Object((1,3,6,1,4,1,9,9,652,1,1,4,1))
csstConfigStatsIfEntry.setIndexNames((0,_g,_h))
if mibBuilder.loadTexts:csstConfigStatsIfEntry.setStatus(_B)
_CsstConfigStatsIfPackets1_Type=Counter64
_CsstConfigStatsIfPackets1_Object=MibTableColumn
csstConfigStatsIfPackets1=_CsstConfigStatsIfPackets1_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,1),_CsstConfigStatsIfPackets1_Type())
csstConfigStatsIfPackets1.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets1.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets1.setUnits(_D)
_CsstConfigStatsIfOctets1_Type=Counter64
_CsstConfigStatsIfOctets1_Object=MibTableColumn
csstConfigStatsIfOctets1=_CsstConfigStatsIfOctets1_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,2),_CsstConfigStatsIfOctets1_Type())
csstConfigStatsIfOctets1.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets1.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets1.setUnits(_F)
_CsstConfigStatsIfPackets2_Type=Counter64
_CsstConfigStatsIfPackets2_Object=MibTableColumn
csstConfigStatsIfPackets2=_CsstConfigStatsIfPackets2_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,3),_CsstConfigStatsIfPackets2_Type())
csstConfigStatsIfPackets2.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets2.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets2.setUnits(_D)
_CsstConfigStatsIfOctets2_Type=Counter64
_CsstConfigStatsIfOctets2_Object=MibTableColumn
csstConfigStatsIfOctets2=_CsstConfigStatsIfOctets2_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,4),_CsstConfigStatsIfOctets2_Type())
csstConfigStatsIfOctets2.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets2.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets2.setUnits(_F)
_CsstConfigStatsIfPackets3_Type=Counter64
_CsstConfigStatsIfPackets3_Object=MibTableColumn
csstConfigStatsIfPackets3=_CsstConfigStatsIfPackets3_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,5),_CsstConfigStatsIfPackets3_Type())
csstConfigStatsIfPackets3.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets3.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets3.setUnits(_D)
_CsstConfigStatsIfOctets3_Type=Counter64
_CsstConfigStatsIfOctets3_Object=MibTableColumn
csstConfigStatsIfOctets3=_CsstConfigStatsIfOctets3_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,6),_CsstConfigStatsIfOctets3_Type())
csstConfigStatsIfOctets3.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets3.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets3.setUnits(_F)
_CsstConfigStatsIfPackets4_Type=Counter64
_CsstConfigStatsIfPackets4_Object=MibTableColumn
csstConfigStatsIfPackets4=_CsstConfigStatsIfPackets4_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,7),_CsstConfigStatsIfPackets4_Type())
csstConfigStatsIfPackets4.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets4.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets4.setUnits(_D)
_CsstConfigStatsIfOctets4_Type=Counter64
_CsstConfigStatsIfOctets4_Object=MibTableColumn
csstConfigStatsIfOctets4=_CsstConfigStatsIfOctets4_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,8),_CsstConfigStatsIfOctets4_Type())
csstConfigStatsIfOctets4.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets4.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets4.setUnits(_F)
_CsstConfigStatsIfPackets5_Type=Counter64
_CsstConfigStatsIfPackets5_Object=MibTableColumn
csstConfigStatsIfPackets5=_CsstConfigStatsIfPackets5_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,9),_CsstConfigStatsIfPackets5_Type())
csstConfigStatsIfPackets5.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets5.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets5.setUnits(_D)
_CsstConfigStatsIfOctets5_Type=Counter64
_CsstConfigStatsIfOctets5_Object=MibTableColumn
csstConfigStatsIfOctets5=_CsstConfigStatsIfOctets5_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,10),_CsstConfigStatsIfOctets5_Type())
csstConfigStatsIfOctets5.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets5.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets5.setUnits(_F)
_CsstConfigStatsIfPackets6_Type=Counter64
_CsstConfigStatsIfPackets6_Object=MibTableColumn
csstConfigStatsIfPackets6=_CsstConfigStatsIfPackets6_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,11),_CsstConfigStatsIfPackets6_Type())
csstConfigStatsIfPackets6.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets6.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets6.setUnits(_D)
_CsstConfigStatsIfOctets6_Type=Counter64
_CsstConfigStatsIfOctets6_Object=MibTableColumn
csstConfigStatsIfOctets6=_CsstConfigStatsIfOctets6_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,12),_CsstConfigStatsIfOctets6_Type())
csstConfigStatsIfOctets6.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets6.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets6.setUnits(_F)
_CsstConfigStatsIfPackets7_Type=Counter64
_CsstConfigStatsIfPackets7_Object=MibTableColumn
csstConfigStatsIfPackets7=_CsstConfigStatsIfPackets7_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,13),_CsstConfigStatsIfPackets7_Type())
csstConfigStatsIfPackets7.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets7.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets7.setUnits(_D)
_CsstConfigStatsIfOctets7_Type=Counter64
_CsstConfigStatsIfOctets7_Object=MibTableColumn
csstConfigStatsIfOctets7=_CsstConfigStatsIfOctets7_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,14),_CsstConfigStatsIfOctets7_Type())
csstConfigStatsIfOctets7.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets7.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets7.setUnits(_F)
_CsstConfigStatsIfPackets8_Type=Counter64
_CsstConfigStatsIfPackets8_Object=MibTableColumn
csstConfigStatsIfPackets8=_CsstConfigStatsIfPackets8_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,15),_CsstConfigStatsIfPackets8_Type())
csstConfigStatsIfPackets8.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfPackets8.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfPackets8.setUnits(_D)
_CsstConfigStatsIfOctets8_Type=Counter64
_CsstConfigStatsIfOctets8_Object=MibTableColumn
csstConfigStatsIfOctets8=_CsstConfigStatsIfOctets8_Object((1,3,6,1,4,1,9,9,652,1,1,4,1,16),_CsstConfigStatsIfOctets8_Type())
csstConfigStatsIfOctets8.setMaxAccess(_C)
if mibBuilder.loadTexts:csstConfigStatsIfOctets8.setStatus(_B)
if mibBuilder.loadTexts:csstConfigStatsIfOctets8.setUnits(_F)
_CsstVlanStats_ObjectIdentity=ObjectIdentity
csstVlanStats=_CsstVlanStats_ObjectIdentity((1,3,6,1,4,1,9,9,652,1,2))
_CsstVlanStatsTable_Object=MibTable
csstVlanStatsTable=_CsstVlanStatsTable_Object((1,3,6,1,4,1,9,9,652,1,2,1))
if mibBuilder.loadTexts:csstVlanStatsTable.setStatus(_B)
_CsstVlanStatsEntry_Object=MibTableRow
csstVlanStatsEntry=_CsstVlanStatsEntry_Object((1,3,6,1,4,1,9,9,652,1,2,1,1))
csstVlanStatsEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:csstVlanStatsEntry.setStatus(_B)
_CsstVlanIndex_Type=VlanIndex
_CsstVlanIndex_Object=MibTableColumn
csstVlanIndex=_CsstVlanIndex_Object((1,3,6,1,4,1,9,9,652,1,2,1,1,1),_CsstVlanIndex_Type())
csstVlanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:csstVlanIndex.setStatus(_B)
_CsstVlanKnownBridgedUcastPkts_Type=Counter64
_CsstVlanKnownBridgedUcastPkts_Object=MibTableColumn
csstVlanKnownBridgedUcastPkts=_CsstVlanKnownBridgedUcastPkts_Object((1,3,6,1,4,1,9,9,652,1,2,1,1,2),_CsstVlanKnownBridgedUcastPkts_Type())
csstVlanKnownBridgedUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstVlanKnownBridgedUcastPkts.setStatus(_B)
if mibBuilder.loadTexts:csstVlanKnownBridgedUcastPkts.setUnits(_D)
_CsstVlanKnownBridgedUcastOctets_Type=Counter64
_CsstVlanKnownBridgedUcastOctets_Object=MibTableColumn
csstVlanKnownBridgedUcastOctets=_CsstVlanKnownBridgedUcastOctets_Object((1,3,6,1,4,1,9,9,652,1,2,1,1,3),_CsstVlanKnownBridgedUcastOctets_Type())
csstVlanKnownBridgedUcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:csstVlanKnownBridgedUcastOctets.setStatus(_B)
if mibBuilder.loadTexts:csstVlanKnownBridgedUcastOctets.setUnits(_F)
_CsstVlanKnownBridgedNUcastPkts_Type=Counter64
_CsstVlanKnownBridgedNUcastPkts_Object=MibTableColumn
csstVlanKnownBridgedNUcastPkts=_CsstVlanKnownBridgedNUcastPkts_Object((1,3,6,1,4,1,9,9,652,1,2,1,1,4),_CsstVlanKnownBridgedNUcastPkts_Type())
csstVlanKnownBridgedNUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstVlanKnownBridgedNUcastPkts.setStatus(_B)
if mibBuilder.loadTexts:csstVlanKnownBridgedNUcastPkts.setUnits(_D)
_CsstVlanKnownBridgedNUcastOctets_Type=Counter64
_CsstVlanKnownBridgedNUcastOctets_Object=MibTableColumn
csstVlanKnownBridgedNUcastOctets=_CsstVlanKnownBridgedNUcastOctets_Object((1,3,6,1,4,1,9,9,652,1,2,1,1,5),_CsstVlanKnownBridgedNUcastOctets_Type())
csstVlanKnownBridgedNUcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:csstVlanKnownBridgedNUcastOctets.setStatus(_B)
if mibBuilder.loadTexts:csstVlanKnownBridgedNUcastOctets.setUnits(_F)
_CsstSwitchTrafficStats_ObjectIdentity=ObjectIdentity
csstSwitchTrafficStats=_CsstSwitchTrafficStats_ObjectIdentity((1,3,6,1,4,1,9,9,652,1,3))
_CsstSwitchStatsTable_Object=MibTable
csstSwitchStatsTable=_CsstSwitchStatsTable_Object((1,3,6,1,4,1,9,9,652,1,3,1))
if mibBuilder.loadTexts:csstSwitchStatsTable.setStatus(_B)
_CsstSwitchStatsEntry_Object=MibTableRow
csstSwitchStatsEntry=_CsstSwitchStatsEntry_Object((1,3,6,1,4,1,9,9,652,1,3,1,1))
csstSwitchStatsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:csstSwitchStatsEntry.setStatus(_B)
_CsstL2TotalBridgedPkts_Type=Counter32
_CsstL2TotalBridgedPkts_Object=MibTableColumn
csstL2TotalBridgedPkts=_CsstL2TotalBridgedPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,1),_CsstL2TotalBridgedPkts_Type())
csstL2TotalBridgedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL2TotalBridgedPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL2TotalBridgedPkts.setUnits(_D)
_CsstL3FibSwitchedIpv4UcastPkts_Type=Counter32
_CsstL3FibSwitchedIpv4UcastPkts_Object=MibTableColumn
csstL3FibSwitchedIpv4UcastPkts=_CsstL3FibSwitchedIpv4UcastPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,2),_CsstL3FibSwitchedIpv4UcastPkts_Type())
csstL3FibSwitchedIpv4UcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3FibSwitchedIpv4UcastPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3FibSwitchedIpv4UcastPkts.setUnits(_D)
_CsstL3FibSwitchedIpv6UcastPkts_Type=Counter32
_CsstL3FibSwitchedIpv6UcastPkts_Object=MibTableColumn
csstL3FibSwitchedIpv6UcastPkts=_CsstL3FibSwitchedIpv6UcastPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,3),_CsstL3FibSwitchedIpv6UcastPkts_Type())
csstL3FibSwitchedIpv6UcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3FibSwitchedIpv6UcastPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3FibSwitchedIpv6UcastPkts.setUnits(_D)
_CsstL3FibSwitchedEoMplsPkts_Type=Counter32
_CsstL3FibSwitchedEoMplsPkts_Object=MibTableColumn
csstL3FibSwitchedEoMplsPkts=_CsstL3FibSwitchedEoMplsPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,4),_CsstL3FibSwitchedEoMplsPkts_Type())
csstL3FibSwitchedEoMplsPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3FibSwitchedEoMplsPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3FibSwitchedEoMplsPkts.setUnits(_D)
_CsstL3FibSwitchedMplsPkts_Type=Counter32
_CsstL3FibSwitchedMplsPkts_Object=MibTableColumn
csstL3FibSwitchedMplsPkts=_CsstL3FibSwitchedMplsPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,5),_CsstL3FibSwitchedMplsPkts_Type())
csstL3FibSwitchedMplsPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3FibSwitchedMplsPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3FibSwitchedMplsPkts.setUnits(_D)
_CsstL3TotalMulticastPkts_Type=Counter32
_CsstL3TotalMulticastPkts_Object=MibTableColumn
csstL3TotalMulticastPkts=_CsstL3TotalMulticastPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,6),_CsstL3TotalMulticastPkts_Type())
csstL3TotalMulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3TotalMulticastPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3TotalMulticastPkts.setUnits(_D)
_CsstL3IgmpMldPkts_Type=Counter32
_CsstL3IgmpMldPkts_Object=MibTableColumn
csstL3IgmpMldPkts=_CsstL3IgmpMldPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,7),_CsstL3IgmpMldPkts_Type())
csstL3IgmpMldPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3IgmpMldPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3IgmpMldPkts.setUnits(_D)
_CsstL3Ipv4MulticastPkts_Type=Counter32
_CsstL3Ipv4MulticastPkts_Object=MibTableColumn
csstL3Ipv4MulticastPkts=_CsstL3Ipv4MulticastPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,8),_CsstL3Ipv4MulticastPkts_Type())
csstL3Ipv4MulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3Ipv4MulticastPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3Ipv4MulticastPkts.setUnits(_D)
_CsstL3Ipv6MulticastPkts_Type=Counter32
_CsstL3Ipv6MulticastPkts_Object=MibTableColumn
csstL3Ipv6MulticastPkts=_CsstL3Ipv6MulticastPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,9),_CsstL3Ipv6MulticastPkts_Type())
csstL3Ipv6MulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3Ipv6MulticastPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3Ipv6MulticastPkts.setUnits(_D)
_CsstL3MulticastLeakPkts_Type=Counter32
_CsstL3MulticastLeakPkts_Object=MibTableColumn
csstL3MulticastLeakPkts=_CsstL3MulticastLeakPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,10),_CsstL3MulticastLeakPkts_Type())
csstL3MulticastLeakPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3MulticastLeakPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3MulticastLeakPkts.setUnits(_D)
_CsstL3InputAclRoutedPkts_Type=Counter32
_CsstL3InputAclRoutedPkts_Object=MibTableColumn
csstL3InputAclRoutedPkts=_CsstL3InputAclRoutedPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,11),_CsstL3InputAclRoutedPkts_Type())
csstL3InputAclRoutedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3InputAclRoutedPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3InputAclRoutedPkts.setUnits(_D)
_CsstL3OutputAclRoutedPkts_Type=Counter32
_CsstL3OutputAclRoutedPkts_Object=MibTableColumn
csstL3OutputAclRoutedPkts=_CsstL3OutputAclRoutedPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,12),_CsstL3OutputAclRoutedPkts_Type())
csstL3OutputAclRoutedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3OutputAclRoutedPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3OutputAclRoutedPkts.setUnits(_D)
_CsstL3InputNetflowSwitchedPkts_Type=Counter32
_CsstL3InputNetflowSwitchedPkts_Object=MibTableColumn
csstL3InputNetflowSwitchedPkts=_CsstL3InputNetflowSwitchedPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,13),_CsstL3InputNetflowSwitchedPkts_Type())
csstL3InputNetflowSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3InputNetflowSwitchedPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3InputNetflowSwitchedPkts.setUnits(_D)
_CsstL3OutputNetflowSwitchedPkts_Type=Counter32
_CsstL3OutputNetflowSwitchedPkts_Object=MibTableColumn
csstL3OutputNetflowSwitchedPkts=_CsstL3OutputNetflowSwitchedPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,14),_CsstL3OutputNetflowSwitchedPkts_Type())
csstL3OutputNetflowSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3OutputNetflowSwitchedPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3OutputNetflowSwitchedPkts.setUnits(_D)
_CsstL3InExceptionRedirectPkts_Type=Counter32
_CsstL3InExceptionRedirectPkts_Object=MibTableColumn
csstL3InExceptionRedirectPkts=_CsstL3InExceptionRedirectPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,15),_CsstL3InExceptionRedirectPkts_Type())
csstL3InExceptionRedirectPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3InExceptionRedirectPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3InExceptionRedirectPkts.setUnits(_D)
_CsstL3OutExceptionRedirectPkts_Type=Counter32
_CsstL3OutExceptionRedirectPkts_Object=MibTableColumn
csstL3OutExceptionRedirectPkts=_CsstL3OutExceptionRedirectPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,16),_CsstL3OutExceptionRedirectPkts_Type())
csstL3OutExceptionRedirectPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3OutExceptionRedirectPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3OutExceptionRedirectPkts.setUnits(_D)
_CsstL3TotalNetflowSwitchedPkts_Type=Counter32
_CsstL3TotalNetflowSwitchedPkts_Object=MibTableColumn
csstL3TotalNetflowSwitchedPkts=_CsstL3TotalNetflowSwitchedPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,17),_CsstL3TotalNetflowSwitchedPkts_Type())
csstL3TotalNetflowSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3TotalNetflowSwitchedPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3TotalNetflowSwitchedPkts.setUnits(_D)
_CsstL3TotalAclRoutedPkts_Type=Counter32
_CsstL3TotalAclRoutedPkts_Object=MibTableColumn
csstL3TotalAclRoutedPkts=_CsstL3TotalAclRoutedPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,18),_CsstL3TotalAclRoutedPkts_Type())
csstL3TotalAclRoutedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstL3TotalAclRoutedPkts.setStatus(_B)
if mibBuilder.loadTexts:csstL3TotalAclRoutedPkts.setUnits(_D)
_CsstTotalAclDenyPkts_Type=Counter32
_CsstTotalAclDenyPkts_Object=MibTableColumn
csstTotalAclDenyPkts=_CsstTotalAclDenyPkts_Object((1,3,6,1,4,1,9,9,652,1,3,1,1,19),_CsstTotalAclDenyPkts_Type())
csstTotalAclDenyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstTotalAclDenyPkts.setStatus(_B)
if mibBuilder.loadTexts:csstTotalAclDenyPkts.setUnits(_D)
_CsstHwInternalStats_ObjectIdentity=ObjectIdentity
csstHwInternalStats=_CsstHwInternalStats_ObjectIdentity((1,3,6,1,4,1,9,9,652,1,4))
_CsstHwInternalStatsTable_Object=MibTable
csstHwInternalStatsTable=_CsstHwInternalStatsTable_Object((1,3,6,1,4,1,9,9,652,1,4,1))
if mibBuilder.loadTexts:csstHwInternalStatsTable.setStatus(_B)
_CsstHwInternalStatsEntry_Object=MibTableRow
csstHwInternalStatsEntry=_CsstHwInternalStatsEntry_Object((1,3,6,1,4,1,9,9,652,1,4,1,1))
csstHwInternalStatsEntry.setIndexNames((0,_G,_H),(0,_A,_l),(0,_A,_m),(0,_A,_n),(0,_A,_o),(0,_A,_p))
if mibBuilder.loadTexts:csstHwInternalStatsEntry.setStatus(_B)
_CsstHwInternalStatsDeviceId_Type=Unsigned32
_CsstHwInternalStatsDeviceId_Object=MibTableColumn
csstHwInternalStatsDeviceId=_CsstHwInternalStatsDeviceId_Object((1,3,6,1,4,1,9,9,652,1,4,1,1,1),_CsstHwInternalStatsDeviceId_Type())
csstHwInternalStatsDeviceId.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalStatsDeviceId.setStatus(_B)
_CsstHwInternalStatsInstanceNum_Type=Unsigned32
_CsstHwInternalStatsInstanceNum_Object=MibTableColumn
csstHwInternalStatsInstanceNum=_CsstHwInternalStatsInstanceNum_Object((1,3,6,1,4,1,9,9,652,1,4,1,1,2),_CsstHwInternalStatsInstanceNum_Type())
csstHwInternalStatsInstanceNum.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalStatsInstanceNum.setStatus(_B)
class _CsstHwInternalStatsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ingressIn',1),('ingressOut',2),('egressIn',3),('egressOut',4)))
_CsstHwInternalStatsDirection_Type.__name__=_I
_CsstHwInternalStatsDirection_Object=MibTableColumn
csstHwInternalStatsDirection=_CsstHwInternalStatsDirection_Object((1,3,6,1,4,1,9,9,652,1,4,1,1,3),_CsstHwInternalStatsDirection_Type())
csstHwInternalStatsDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalStatsDirection.setStatus(_B)
class _CsstHwInternalStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('packetsPerSec',1),('bytesPerSec',2)))
_CsstHwInternalStatsType_Type.__name__=_I
_CsstHwInternalStatsType_Object=MibTableColumn
csstHwInternalStatsType=_CsstHwInternalStatsType_Object((1,3,6,1,4,1,9,9,652,1,4,1,1,4),_CsstHwInternalStatsType_Type())
csstHwInternalStatsType.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalStatsType.setStatus(_B)
_CsstHwInternalStatsIndex_Type=Unsigned32
_CsstHwInternalStatsIndex_Object=MibTableColumn
csstHwInternalStatsIndex=_CsstHwInternalStatsIndex_Object((1,3,6,1,4,1,9,9,652,1,4,1,1,5),_CsstHwInternalStatsIndex_Type())
csstHwInternalStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalStatsIndex.setStatus(_B)
_CsstHwInternalStatsDescr_Type=SnmpAdminString
_CsstHwInternalStatsDescr_Object=MibTableColumn
csstHwInternalStatsDescr=_CsstHwInternalStatsDescr_Object((1,3,6,1,4,1,9,9,652,1,4,1,1,6),_CsstHwInternalStatsDescr_Type())
csstHwInternalStatsDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:csstHwInternalStatsDescr.setStatus(_B)
_CsstHwInternalStatsRate_Type=Gauge32
_CsstHwInternalStatsRate_Object=MibTableColumn
csstHwInternalStatsRate=_CsstHwInternalStatsRate_Object((1,3,6,1,4,1,9,9,652,1,4,1,1,7),_CsstHwInternalStatsRate_Type())
csstHwInternalStatsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:csstHwInternalStatsRate.setStatus(_B)
_CsstHwInternalErrorTable_Object=MibTable
csstHwInternalErrorTable=_CsstHwInternalErrorTable_Object((1,3,6,1,4,1,9,9,652,1,4,2))
if mibBuilder.loadTexts:csstHwInternalErrorTable.setStatus(_B)
_CsstHwInternalErrorEntry_Object=MibTableRow
csstHwInternalErrorEntry=_CsstHwInternalErrorEntry_Object((1,3,6,1,4,1,9,9,652,1,4,2,1))
csstHwInternalErrorEntry.setIndexNames((0,_G,_H),(0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:csstHwInternalErrorEntry.setStatus(_B)
_CsstHwInternalErrorDeviceId_Type=Unsigned32
_CsstHwInternalErrorDeviceId_Object=MibTableColumn
csstHwInternalErrorDeviceId=_CsstHwInternalErrorDeviceId_Object((1,3,6,1,4,1,9,9,652,1,4,2,1,1),_CsstHwInternalErrorDeviceId_Type())
csstHwInternalErrorDeviceId.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalErrorDeviceId.setStatus(_B)
class _CsstHwInternalErrorCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('error',1),('congestion',2),('qos',3)))
_CsstHwInternalErrorCategory_Type.__name__=_I
_CsstHwInternalErrorCategory_Object=MibTableColumn
csstHwInternalErrorCategory=_CsstHwInternalErrorCategory_Object((1,3,6,1,4,1,9,9,652,1,4,2,1,2),_CsstHwInternalErrorCategory_Type())
csstHwInternalErrorCategory.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalErrorCategory.setStatus(_B)
_CsstHwInternalErrorDeviceInfo_Type=SnmpAdminString
_CsstHwInternalErrorDeviceInfo_Object=MibTableColumn
csstHwInternalErrorDeviceInfo=_CsstHwInternalErrorDeviceInfo_Object((1,3,6,1,4,1,9,9,652,1,4,2,1,3),_CsstHwInternalErrorDeviceInfo_Type())
csstHwInternalErrorDeviceInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:csstHwInternalErrorDeviceInfo.setStatus(_B)
_CsstHwInternalErrorLastCleared_Type=DateAndTime
_CsstHwInternalErrorLastCleared_Object=MibTableColumn
csstHwInternalErrorLastCleared=_CsstHwInternalErrorLastCleared_Object((1,3,6,1,4,1,9,9,652,1,4,2,1,4),_CsstHwInternalErrorLastCleared_Type())
csstHwInternalErrorLastCleared.setMaxAccess(_C)
if mibBuilder.loadTexts:csstHwInternalErrorLastCleared.setStatus(_B)
_CsstHwInternalErrorInstTable_Object=MibTable
csstHwInternalErrorInstTable=_CsstHwInternalErrorInstTable_Object((1,3,6,1,4,1,9,9,652,1,4,3))
if mibBuilder.loadTexts:csstHwInternalErrorInstTable.setStatus(_B)
_CsstHwInternalErrorInstEntry_Object=MibTableRow
csstHwInternalErrorInstEntry=_CsstHwInternalErrorInstEntry_Object((1,3,6,1,4,1,9,9,652,1,4,3,1))
csstHwInternalErrorInstEntry.setIndexNames((0,_G,_H),(0,_A,_J),(0,_A,_K),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:csstHwInternalErrorInstEntry.setStatus(_B)
_CsstHwInternalErrorInstNum_Type=Unsigned32
_CsstHwInternalErrorInstNum_Object=MibTableColumn
csstHwInternalErrorInstNum=_CsstHwInternalErrorInstNum_Object((1,3,6,1,4,1,9,9,652,1,4,3,1,1),_CsstHwInternalErrorInstNum_Type())
csstHwInternalErrorInstNum.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalErrorInstNum.setStatus(_B)
_CsstHwInternalErrorInstErrorId_Type=Unsigned32
_CsstHwInternalErrorInstErrorId_Object=MibTableColumn
csstHwInternalErrorInstErrorId=_CsstHwInternalErrorInstErrorId_Object((1,3,6,1,4,1,9,9,652,1,4,3,1,2),_CsstHwInternalErrorInstErrorId_Type())
csstHwInternalErrorInstErrorId.setMaxAccess(_E)
if mibBuilder.loadTexts:csstHwInternalErrorInstErrorId.setStatus(_B)
_CsstHwInternalErrorInstDescr_Type=SnmpAdminString
_CsstHwInternalErrorInstDescr_Object=MibTableColumn
csstHwInternalErrorInstDescr=_CsstHwInternalErrorInstDescr_Object((1,3,6,1,4,1,9,9,652,1,4,3,1,3),_CsstHwInternalErrorInstDescr_Type())
csstHwInternalErrorInstDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:csstHwInternalErrorInstDescr.setStatus(_B)
_CsstHwInternalErrorInstCount_Type=Counter64
_CsstHwInternalErrorInstCount_Object=MibTableColumn
csstHwInternalErrorInstCount=_CsstHwInternalErrorInstCount_Object((1,3,6,1,4,1,9,9,652,1,4,3,1,4),_CsstHwInternalErrorInstCount_Type())
csstHwInternalErrorInstCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csstHwInternalErrorInstCount.setStatus(_B)
_CsstHwInternalErrorInstPorts_Type=SnmpAdminString
_CsstHwInternalErrorInstPorts_Object=MibTableColumn
csstHwInternalErrorInstPorts=_CsstHwInternalErrorInstPorts_Object((1,3,6,1,4,1,9,9,652,1,4,3,1,5),_CsstHwInternalErrorInstPorts_Type())
csstHwInternalErrorInstPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstHwInternalErrorInstPorts.setStatus(_B)
_CsstRewriteEngineStats_ObjectIdentity=ObjectIdentity
csstRewriteEngineStats=_CsstRewriteEngineStats_ObjectIdentity((1,3,6,1,4,1,9,9,652,1,5))
_CsstRewriteEnginePktDropStatsTable_Object=MibTable
csstRewriteEnginePktDropStatsTable=_CsstRewriteEnginePktDropStatsTable_Object((1,3,6,1,4,1,9,9,652,1,5,1))
if mibBuilder.loadTexts:csstRewriteEnginePktDropStatsTable.setStatus(_B)
_CsstRewriteEnginePktDropStatsEntry_Object=MibTableRow
csstRewriteEnginePktDropStatsEntry=_CsstRewriteEnginePktDropStatsEntry_Object((1,3,6,1,4,1,9,9,652,1,5,1,1))
csstRewriteEnginePktDropStatsEntry.setIndexNames((0,_G,_H),(0,_A,_s))
if mibBuilder.loadTexts:csstRewriteEnginePktDropStatsEntry.setStatus(_B)
_CsstRewriteEngineChannelIndex_Type=Unsigned32
_CsstRewriteEngineChannelIndex_Object=MibTableColumn
csstRewriteEngineChannelIndex=_CsstRewriteEngineChannelIndex_Object((1,3,6,1,4,1,9,9,652,1,5,1,1,1),_CsstRewriteEngineChannelIndex_Type())
csstRewriteEngineChannelIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:csstRewriteEngineChannelIndex.setStatus(_B)
_CsstRewriteEngineDropPkts_Type=Counter64
_CsstRewriteEngineDropPkts_Object=MibTableColumn
csstRewriteEngineDropPkts=_CsstRewriteEngineDropPkts_Object((1,3,6,1,4,1,9,9,652,1,5,1,1,2),_CsstRewriteEngineDropPkts_Type())
csstRewriteEngineDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:csstRewriteEngineDropPkts.setStatus(_B)
if mibBuilder.loadTexts:csstRewriteEngineDropPkts.setUnits(_D)
_CsstRewriteEngineTotalOverruns_Type=Counter32
_CsstRewriteEngineTotalOverruns_Object=MibTableColumn
csstRewriteEngineTotalOverruns=_CsstRewriteEngineTotalOverruns_Object((1,3,6,1,4,1,9,9,652,1,5,1,1,3),_CsstRewriteEngineTotalOverruns_Type())
csstRewriteEngineTotalOverruns.setMaxAccess(_C)
if mibBuilder.loadTexts:csstRewriteEngineTotalOverruns.setStatus(_B)
_CiscoSwitchStatsMIBConform_ObjectIdentity=ObjectIdentity
ciscoSwitchStatsMIBConform=_CiscoSwitchStatsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,652,2))
_CsstSwitchStatsMIBCompliances_ObjectIdentity=ObjectIdentity
csstSwitchStatsMIBCompliances=_CsstSwitchStatsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,652,2,1))
_CsstSwitchStatsMIBGroups_ObjectIdentity=ObjectIdentity
csstSwitchStatsMIBGroups=_CsstSwitchStatsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,652,2,2))
ciscoSwitchStatsConfOptionGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,1))
ciscoSwitchStatsConfOptionGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:ciscoSwitchStatsConfOptionGroup.setStatus(_B)
ciscoSwitchStatsConfMapGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,2))
ciscoSwitchStatsConfMapGroup.setObjects(*((_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ciscoSwitchStatsConfMapGroup.setStatus(_B)
ciscoSwitchStatsConfIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,3))
ciscoSwitchStatsConfIfGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ciscoSwitchStatsConfIfGroup.setStatus(_B)
ciscoSwitchStatsVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,4))
ciscoSwitchStatsVlanGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:ciscoSwitchStatsVlanGroup.setStatus(_B)
ciscoSwitchStatsL2Group=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,5))
ciscoSwitchStatsL2Group.setObjects((_A,_AG))
if mibBuilder.loadTexts:ciscoSwitchStatsL2Group.setStatus(_B)
ciscoSwitchStatsL3Group=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,6))
ciscoSwitchStatsL3Group.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoSwitchStatsL3Group.setStatus(_AH)
ciscoSwitchStatsLayer3Group=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,7))
ciscoSwitchStatsLayer3Group.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoSwitchStatsLayer3Group.setStatus(_B)
ciscoSwitchStatsLayer3ExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,8))
ciscoSwitchStatsLayer3ExtGroup.setObjects((_A,_P))
if mibBuilder.loadTexts:ciscoSwitchStatsLayer3ExtGroup.setStatus(_B)
ciscoSwitchStatsTotalGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,9))
ciscoSwitchStatsTotalGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:ciscoSwitchStatsTotalGroup.setStatus(_B)
ciscoSwitchStatsInternalStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,10))
ciscoSwitchStatsInternalStatsGroup.setObjects(*((_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:ciscoSwitchStatsInternalStatsGroup.setStatus(_B)
ciscoSwitchStatsInternalErrorGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,11))
ciscoSwitchStatsInternalErrorGroup.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:ciscoSwitchStatsInternalErrorGroup.setStatus(_B)
ciscoSwitchStatsInternalInstanceGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,12))
ciscoSwitchStatsInternalInstanceGroup.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:ciscoSwitchStatsInternalInstanceGroup.setStatus(_B)
ciscoSwitchStatsRewriteEngineStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,652,2,2,13))
ciscoSwitchStatsRewriteEngineStatsGroup.setObjects(*((_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:ciscoSwitchStatsRewriteEngineStatsGroup.setStatus(_B)
csstSwitchStatsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,652,2,1,1))
csstSwitchStatsMIBCompliance.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_AU)))
if mibBuilder.loadTexts:csstSwitchStatsMIBCompliance.setStatus(_AH)
csstSwitchStatsMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,652,2,1,2))
csstSwitchStatsMIBCompliance2.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:csstSwitchStatsMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoSwitchStatsMIB':ciscoSwitchStatsMIB,'ciscoSwitchStatsMIBNotifs':ciscoSwitchStatsMIBNotifs,'ciscoSwitchStatsMIBObjects':ciscoSwitchStatsMIBObjects,'csstConfigurableStats':csstConfigurableStats,'csstConfigStatsOptionTable':csstConfigStatsOptionTable,'csstConfigStatsOptionEntry':csstConfigStatsOptionEntry,_j:csstConfigStatsOptionIndex,_t:csstConfigStatsOptionDesc,_u:csstConfigStatsMapSize,_v:csstConfigStatsMap,'csstConfigStatsIfTable':csstConfigStatsIfTable,'csstConfigStatsIfEntry':csstConfigStatsIfEntry,_w:csstConfigStatsIfPackets1,_x:csstConfigStatsIfOctets1,_y:csstConfigStatsIfPackets2,_z:csstConfigStatsIfOctets2,_A0:csstConfigStatsIfPackets3,_A1:csstConfigStatsIfOctets3,_A2:csstConfigStatsIfPackets4,_A3:csstConfigStatsIfOctets4,_A4:csstConfigStatsIfPackets5,_A5:csstConfigStatsIfOctets5,_A6:csstConfigStatsIfPackets6,_A7:csstConfigStatsIfOctets6,_A8:csstConfigStatsIfPackets7,_A9:csstConfigStatsIfOctets7,_AA:csstConfigStatsIfPackets8,_AB:csstConfigStatsIfOctets8,'csstVlanStats':csstVlanStats,'csstVlanStatsTable':csstVlanStatsTable,'csstVlanStatsEntry':csstVlanStatsEntry,_k:csstVlanIndex,_AC:csstVlanKnownBridgedUcastPkts,_AD:csstVlanKnownBridgedUcastOctets,_AE:csstVlanKnownBridgedNUcastPkts,_AF:csstVlanKnownBridgedNUcastOctets,'csstSwitchTrafficStats':csstSwitchTrafficStats,'csstSwitchStatsTable':csstSwitchStatsTable,'csstSwitchStatsEntry':csstSwitchStatsEntry,_AG:csstL2TotalBridgedPkts,_L:csstL3FibSwitchedIpv4UcastPkts,_M:csstL3FibSwitchedIpv6UcastPkts,_N:csstL3FibSwitchedEoMplsPkts,_O:csstL3FibSwitchedMplsPkts,_P:csstL3TotalMulticastPkts,_Q:csstL3IgmpMldPkts,_R:csstL3Ipv4MulticastPkts,_S:csstL3Ipv6MulticastPkts,_T:csstL3MulticastLeakPkts,_U:csstL3InputAclRoutedPkts,_V:csstL3OutputAclRoutedPkts,_W:csstL3InputNetflowSwitchedPkts,_X:csstL3OutputNetflowSwitchedPkts,_Y:csstL3InExceptionRedirectPkts,_Z:csstL3OutExceptionRedirectPkts,_AI:csstL3TotalNetflowSwitchedPkts,_AJ:csstL3TotalAclRoutedPkts,_AK:csstTotalAclDenyPkts,'csstHwInternalStats':csstHwInternalStats,'csstHwInternalStatsTable':csstHwInternalStatsTable,'csstHwInternalStatsEntry':csstHwInternalStatsEntry,_l:csstHwInternalStatsDeviceId,_m:csstHwInternalStatsInstanceNum,_n:csstHwInternalStatsDirection,_o:csstHwInternalStatsType,_p:csstHwInternalStatsIndex,_AL:csstHwInternalStatsDescr,_AM:csstHwInternalStatsRate,'csstHwInternalErrorTable':csstHwInternalErrorTable,'csstHwInternalErrorEntry':csstHwInternalErrorEntry,_J:csstHwInternalErrorDeviceId,_K:csstHwInternalErrorCategory,_AN:csstHwInternalErrorDeviceInfo,_AO:csstHwInternalErrorLastCleared,'csstHwInternalErrorInstTable':csstHwInternalErrorInstTable,'csstHwInternalErrorInstEntry':csstHwInternalErrorInstEntry,_q:csstHwInternalErrorInstNum,_r:csstHwInternalErrorInstErrorId,_AP:csstHwInternalErrorInstDescr,_AQ:csstHwInternalErrorInstCount,_AR:csstHwInternalErrorInstPorts,'csstRewriteEngineStats':csstRewriteEngineStats,'csstRewriteEnginePktDropStatsTable':csstRewriteEnginePktDropStatsTable,'csstRewriteEnginePktDropStatsEntry':csstRewriteEnginePktDropStatsEntry,_s:csstRewriteEngineChannelIndex,_AS:csstRewriteEngineDropPkts,_AT:csstRewriteEngineTotalOverruns,'ciscoSwitchStatsMIBConform':ciscoSwitchStatsMIBConform,'csstSwitchStatsMIBCompliances':csstSwitchStatsMIBCompliances,'csstSwitchStatsMIBCompliance':csstSwitchStatsMIBCompliance,'csstSwitchStatsMIBCompliance2':csstSwitchStatsMIBCompliance2,'csstSwitchStatsMIBGroups':csstSwitchStatsMIBGroups,_a:ciscoSwitchStatsConfOptionGroup,_b:ciscoSwitchStatsConfMapGroup,_c:ciscoSwitchStatsConfIfGroup,_d:ciscoSwitchStatsVlanGroup,_e:ciscoSwitchStatsL2Group,_AU:ciscoSwitchStatsL3Group,_AV:ciscoSwitchStatsLayer3Group,_AW:ciscoSwitchStatsLayer3ExtGroup,_AX:ciscoSwitchStatsTotalGroup,_AY:ciscoSwitchStatsInternalStatsGroup,_AZ:ciscoSwitchStatsInternalErrorGroup,_Aa:ciscoSwitchStatsInternalInstanceGroup,_Ab:ciscoSwitchStatsRewriteEngineStatsGroup})