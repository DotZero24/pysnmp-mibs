_H='read-create'
_G='rcDhcpRelayServerIndex'
_F='DHCP-RELAY-MIB'
_E='read-write'
_D='Integer32'
_C='current'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
EnableVar,Vlanset=mibBuilder.importSymbols('SWITCH-TC','EnableVar','Vlanset')
rcDhcpRelay=ModuleIdentity((1,3,6,1,4,1,8886,6,1,13))
if mibBuilder.loadTexts:rcDhcpRelay.setRevisions(('2004-12-20 00:00',))
_RcDhcpRelayMibObjects_ObjectIdentity=ObjectIdentity
rcDhcpRelayMibObjects=_RcDhcpRelayMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,13,1))
_RcDhcpRelayGroup_ObjectIdentity=ObjectIdentity
rcDhcpRelayGroup=_RcDhcpRelayGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,13,1,1))
_RcDhcpRelayEnable_Type=EnableVar
_RcDhcpRelayEnable_Object=MibScalar
rcDhcpRelayEnable=_RcDhcpRelayEnable_Object((1,3,6,1,4,1,8886,6,1,13,1,1,1),_RcDhcpRelayEnable_Type())
rcDhcpRelayEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDhcpRelayEnable.setStatus(_C)
_RcDhcpRelayStartTime_Type=TimeTicks
_RcDhcpRelayStartTime_Object=MibScalar
rcDhcpRelayStartTime=_RcDhcpRelayStartTime_Object((1,3,6,1,4,1,8886,6,1,13,1,1,2),_RcDhcpRelayStartTime_Type())
rcDhcpRelayStartTime.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStartTime.setStatus(_B)
_RcDhcpRelayServerTable_Object=MibTable
rcDhcpRelayServerTable=_RcDhcpRelayServerTable_Object((1,3,6,1,4,1,8886,6,1,13,1,1,3))
if mibBuilder.loadTexts:rcDhcpRelayServerTable.setStatus(_C)
_RcDhcpRelayServerEntry_Object=MibTableRow
rcDhcpRelayServerEntry=_RcDhcpRelayServerEntry_Object((1,3,6,1,4,1,8886,6,1,13,1,1,3,1))
rcDhcpRelayServerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rcDhcpRelayServerEntry.setStatus(_C)
_RcDhcpRelayServerIndex_Type=Integer32
_RcDhcpRelayServerIndex_Object=MibTableColumn
rcDhcpRelayServerIndex=_RcDhcpRelayServerIndex_Object((1,3,6,1,4,1,8886,6,1,13,1,1,3,1,1),_RcDhcpRelayServerIndex_Type())
rcDhcpRelayServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcDhcpRelayServerIndex.setStatus(_C)
_RcDhcpRelayServerAddress_Type=IpAddress
_RcDhcpRelayServerAddress_Object=MibTableColumn
rcDhcpRelayServerAddress=_RcDhcpRelayServerAddress_Object((1,3,6,1,4,1,8886,6,1,13,1,1,3,1,2),_RcDhcpRelayServerAddress_Type())
rcDhcpRelayServerAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:rcDhcpRelayServerAddress.setStatus(_C)
_RcDhcpRelayServerRowStatus_Type=RowStatus
_RcDhcpRelayServerRowStatus_Object=MibTableColumn
rcDhcpRelayServerRowStatus=_RcDhcpRelayServerRowStatus_Object((1,3,6,1,4,1,8886,6,1,13,1,1,3,1,3),_RcDhcpRelayServerRowStatus_Type())
rcDhcpRelayServerRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:rcDhcpRelayServerRowStatus.setStatus(_C)
class _RcDhcpRelayServerNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcDhcpRelayServerNextIndex_Type.__name__=_D
_RcDhcpRelayServerNextIndex_Object=MibScalar
rcDhcpRelayServerNextIndex=_RcDhcpRelayServerNextIndex_Object((1,3,6,1,4,1,8886,6,1,13,1,1,4),_RcDhcpRelayServerNextIndex_Type())
rcDhcpRelayServerNextIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayServerNextIndex.setStatus(_C)
_RcDhcpRelayVlans_Type=Vlanset
_RcDhcpRelayVlans_Object=MibScalar
rcDhcpRelayVlans=_RcDhcpRelayVlans_Object((1,3,6,1,4,1,8886,6,1,13,1,1,5),_RcDhcpRelayVlans_Type())
rcDhcpRelayVlans.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDhcpRelayVlans.setStatus(_C)
_RcDhcpRelayStatistics_ObjectIdentity=ObjectIdentity
rcDhcpRelayStatistics=_RcDhcpRelayStatistics_ObjectIdentity((1,3,6,1,4,1,8886,6,1,13,1,2))
_RcDhcpRelayStatsBootps_Type=Counter32
_RcDhcpRelayStatsBootps_Object=MibScalar
rcDhcpRelayStatsBootps=_RcDhcpRelayStatsBootps_Object((1,3,6,1,4,1,8886,6,1,13,1,2,1),_RcDhcpRelayStatsBootps_Type())
rcDhcpRelayStatsBootps.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsBootps.setStatus(_B)
_RcDhcpRelayStatsDiscovers_Type=Counter32
_RcDhcpRelayStatsDiscovers_Object=MibScalar
rcDhcpRelayStatsDiscovers=_RcDhcpRelayStatsDiscovers_Object((1,3,6,1,4,1,8886,6,1,13,1,2,2),_RcDhcpRelayStatsDiscovers_Type())
rcDhcpRelayStatsDiscovers.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsDiscovers.setStatus(_B)
_RcDhcpRelayStatsRequests_Type=Counter32
_RcDhcpRelayStatsRequests_Object=MibScalar
rcDhcpRelayStatsRequests=_RcDhcpRelayStatsRequests_Object((1,3,6,1,4,1,8886,6,1,13,1,2,3),_RcDhcpRelayStatsRequests_Type())
rcDhcpRelayStatsRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsRequests.setStatus(_B)
_RcDhcpRelayStatsReleases_Type=Counter32
_RcDhcpRelayStatsReleases_Object=MibScalar
rcDhcpRelayStatsReleases=_RcDhcpRelayStatsReleases_Object((1,3,6,1,4,1,8886,6,1,13,1,2,4),_RcDhcpRelayStatsReleases_Type())
rcDhcpRelayStatsReleases.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsReleases.setStatus(_B)
_RcDhcpRelayStatsOffers_Type=Counter32
_RcDhcpRelayStatsOffers_Object=MibScalar
rcDhcpRelayStatsOffers=_RcDhcpRelayStatsOffers_Object((1,3,6,1,4,1,8886,6,1,13,1,2,5),_RcDhcpRelayStatsOffers_Type())
rcDhcpRelayStatsOffers.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsOffers.setStatus(_B)
_RcDhcpRelayStatsAcks_Type=Counter32
_RcDhcpRelayStatsAcks_Object=MibScalar
rcDhcpRelayStatsAcks=_RcDhcpRelayStatsAcks_Object((1,3,6,1,4,1,8886,6,1,13,1,2,6),_RcDhcpRelayStatsAcks_Type())
rcDhcpRelayStatsAcks.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsAcks.setStatus(_B)
_RcDhcpRelayStatsNacks_Type=Counter32
_RcDhcpRelayStatsNacks_Object=MibScalar
rcDhcpRelayStatsNacks=_RcDhcpRelayStatsNacks_Object((1,3,6,1,4,1,8886,6,1,13,1,2,7),_RcDhcpRelayStatsNacks_Type())
rcDhcpRelayStatsNacks.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsNacks.setStatus(_B)
_RcDhcpRelayStatsDeclines_Type=Counter32
_RcDhcpRelayStatsDeclines_Object=MibScalar
rcDhcpRelayStatsDeclines=_RcDhcpRelayStatsDeclines_Object((1,3,6,1,4,1,8886,6,1,13,1,2,8),_RcDhcpRelayStatsDeclines_Type())
rcDhcpRelayStatsDeclines.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsDeclines.setStatus(_B)
_RcDhcpRelayStatsInformations_Type=Counter32
_RcDhcpRelayStatsInformations_Object=MibScalar
rcDhcpRelayStatsInformations=_RcDhcpRelayStatsInformations_Object((1,3,6,1,4,1,8886,6,1,13,1,2,9),_RcDhcpRelayStatsInformations_Type())
rcDhcpRelayStatsInformations.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsInformations.setStatus(_B)
_RcDhcpRelayStatsUnknows_Type=Counter32
_RcDhcpRelayStatsUnknows_Object=MibScalar
rcDhcpRelayStatsUnknows=_RcDhcpRelayStatsUnknows_Object((1,3,6,1,4,1,8886,6,1,13,1,2,10),_RcDhcpRelayStatsUnknows_Type())
rcDhcpRelayStatsUnknows.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsUnknows.setStatus(_B)
_RcDhcpRelayStatsPackets_Type=Counter32
_RcDhcpRelayStatsPackets_Object=MibScalar
rcDhcpRelayStatsPackets=_RcDhcpRelayStatsPackets_Object((1,3,6,1,4,1,8886,6,1,13,1,2,11),_RcDhcpRelayStatsPackets_Type())
rcDhcpRelayStatsPackets.setMaxAccess(_A)
if mibBuilder.loadTexts:rcDhcpRelayStatsPackets.setStatus(_B)
mibBuilder.exportSymbols(_F,**{'rcDhcpRelay':rcDhcpRelay,'rcDhcpRelayMibObjects':rcDhcpRelayMibObjects,'rcDhcpRelayGroup':rcDhcpRelayGroup,'rcDhcpRelayEnable':rcDhcpRelayEnable,'rcDhcpRelayStartTime':rcDhcpRelayStartTime,'rcDhcpRelayServerTable':rcDhcpRelayServerTable,'rcDhcpRelayServerEntry':rcDhcpRelayServerEntry,_G:rcDhcpRelayServerIndex,'rcDhcpRelayServerAddress':rcDhcpRelayServerAddress,'rcDhcpRelayServerRowStatus':rcDhcpRelayServerRowStatus,'rcDhcpRelayServerNextIndex':rcDhcpRelayServerNextIndex,'rcDhcpRelayVlans':rcDhcpRelayVlans,'rcDhcpRelayStatistics':rcDhcpRelayStatistics,'rcDhcpRelayStatsBootps':rcDhcpRelayStatsBootps,'rcDhcpRelayStatsDiscovers':rcDhcpRelayStatsDiscovers,'rcDhcpRelayStatsRequests':rcDhcpRelayStatsRequests,'rcDhcpRelayStatsReleases':rcDhcpRelayStatsReleases,'rcDhcpRelayStatsOffers':rcDhcpRelayStatsOffers,'rcDhcpRelayStatsAcks':rcDhcpRelayStatsAcks,'rcDhcpRelayStatsNacks':rcDhcpRelayStatsNacks,'rcDhcpRelayStatsDeclines':rcDhcpRelayStatsDeclines,'rcDhcpRelayStatsInformations':rcDhcpRelayStatsInformations,'rcDhcpRelayStatsUnknows':rcDhcpRelayStatsUnknows,'rcDhcpRelayStatsPackets':rcDhcpRelayStatsPackets})