_L='rcIpDhcpRelayInformationOptionTrustPortIfIndex'
_K='rcIpDhcpRelayTargetAddress'
_J='rcIpDhcpRelayTargetIfIndex'
_I='rcIpDhcpRelayIpInterfaceIfIndex'
_H='EnableVar'
_G='Integer32'
_F='not-accessible'
_E='IPDHCP-RELAY-MIB'
_D='read-write'
_C='current'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_H)
rcIpDhcpRelay=ModuleIdentity((1,3,6,1,4,1,8886,6,1,30))
if mibBuilder.loadTexts:rcIpDhcpRelay.setRevisions(('2007-10-15 00:00',))
_RcIpDhcpRelayConfig_ObjectIdentity=ObjectIdentity
rcIpDhcpRelayConfig=_RcIpDhcpRelayConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,30,1))
class _RcIpDhcpRelayEnable_Type(EnableVar):defaultValue=2
_RcIpDhcpRelayEnable_Type.__name__=_H
_RcIpDhcpRelayEnable_Object=MibScalar
rcIpDhcpRelayEnable=_RcIpDhcpRelayEnable_Object((1,3,6,1,4,1,8886,6,1,30,1,1),_RcIpDhcpRelayEnable_Type())
rcIpDhcpRelayEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpDhcpRelayEnable.setStatus(_C)
_RcIpDhcpRelayStartTime_Type=TimeTicks
_RcIpDhcpRelayStartTime_Object=MibScalar
rcIpDhcpRelayStartTime=_RcIpDhcpRelayStartTime_Object((1,3,6,1,4,1,8886,6,1,30,1,2),_RcIpDhcpRelayStartTime_Type())
rcIpDhcpRelayStartTime.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStartTime.setStatus(_B)
_RcIpDhcpRelayIpInterfaceTable_Object=MibTable
rcIpDhcpRelayIpInterfaceTable=_RcIpDhcpRelayIpInterfaceTable_Object((1,3,6,1,4,1,8886,6,1,30,1,3))
if mibBuilder.loadTexts:rcIpDhcpRelayIpInterfaceTable.setStatus(_C)
_RcIpDhcpRelayIpInterfaceEntry_Object=MibTableRow
rcIpDhcpRelayIpInterfaceEntry=_RcIpDhcpRelayIpInterfaceEntry_Object((1,3,6,1,4,1,8886,6,1,30,1,3,1))
rcIpDhcpRelayIpInterfaceEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:rcIpDhcpRelayIpInterfaceEntry.setStatus(_C)
_RcIpDhcpRelayIpInterfaceIfIndex_Type=Integer32
_RcIpDhcpRelayIpInterfaceIfIndex_Object=MibTableColumn
rcIpDhcpRelayIpInterfaceIfIndex=_RcIpDhcpRelayIpInterfaceIfIndex_Object((1,3,6,1,4,1,8886,6,1,30,1,3,1,1),_RcIpDhcpRelayIpInterfaceIfIndex_Type())
rcIpDhcpRelayIpInterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpRelayIpInterfaceIfIndex.setStatus(_C)
_RcIpDhcpRelayIpInterfaceEnable_Type=EnableVar
_RcIpDhcpRelayIpInterfaceEnable_Object=MibTableColumn
rcIpDhcpRelayIpInterfaceEnable=_RcIpDhcpRelayIpInterfaceEnable_Object((1,3,6,1,4,1,8886,6,1,30,1,3,1,2),_RcIpDhcpRelayIpInterfaceEnable_Type())
rcIpDhcpRelayIpInterfaceEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpDhcpRelayIpInterfaceEnable.setStatus(_C)
_RcIpDhcpRelayTargetTable_Object=MibTable
rcIpDhcpRelayTargetTable=_RcIpDhcpRelayTargetTable_Object((1,3,6,1,4,1,8886,6,1,30,1,4))
if mibBuilder.loadTexts:rcIpDhcpRelayTargetTable.setStatus(_C)
_RcIpDhcpRelayTargetEntry_Object=MibTableRow
rcIpDhcpRelayTargetEntry=_RcIpDhcpRelayTargetEntry_Object((1,3,6,1,4,1,8886,6,1,30,1,4,1))
rcIpDhcpRelayTargetEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:rcIpDhcpRelayTargetEntry.setStatus(_C)
_RcIpDhcpRelayTargetIfIndex_Type=Integer32
_RcIpDhcpRelayTargetIfIndex_Object=MibTableColumn
rcIpDhcpRelayTargetIfIndex=_RcIpDhcpRelayTargetIfIndex_Object((1,3,6,1,4,1,8886,6,1,30,1,4,1,1),_RcIpDhcpRelayTargetIfIndex_Type())
rcIpDhcpRelayTargetIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpRelayTargetIfIndex.setStatus(_C)
_RcIpDhcpRelayTargetAddress_Type=IpAddress
_RcIpDhcpRelayTargetAddress_Object=MibTableColumn
rcIpDhcpRelayTargetAddress=_RcIpDhcpRelayTargetAddress_Object((1,3,6,1,4,1,8886,6,1,30,1,4,1,2),_RcIpDhcpRelayTargetAddress_Type())
rcIpDhcpRelayTargetAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpRelayTargetAddress.setStatus(_C)
_RcIpDhcpRelayTargetRowStatus_Type=RowStatus
_RcIpDhcpRelayTargetRowStatus_Object=MibTableColumn
rcIpDhcpRelayTargetRowStatus=_RcIpDhcpRelayTargetRowStatus_Object((1,3,6,1,4,1,8886,6,1,30,1,4,1,3),_RcIpDhcpRelayTargetRowStatus_Type())
rcIpDhcpRelayTargetRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rcIpDhcpRelayTargetRowStatus.setStatus(_C)
_RcIpDhcpRelayInformationOptionGroup_ObjectIdentity=ObjectIdentity
rcIpDhcpRelayInformationOptionGroup=_RcIpDhcpRelayInformationOptionGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,30,2))
class _RcIpDhcpRelayInformationOption_Type(EnableVar):defaultValue=2
_RcIpDhcpRelayInformationOption_Type.__name__=_H
_RcIpDhcpRelayInformationOption_Object=MibScalar
rcIpDhcpRelayInformationOption=_RcIpDhcpRelayInformationOption_Object((1,3,6,1,4,1,8886,6,1,30,2,1),_RcIpDhcpRelayInformationOption_Type())
rcIpDhcpRelayInformationOption.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpDhcpRelayInformationOption.setStatus(_C)
class _RcIpDhcpRelayInformationPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),('replace',3)))
_RcIpDhcpRelayInformationPolicy_Type.__name__=_G
_RcIpDhcpRelayInformationPolicy_Object=MibScalar
rcIpDhcpRelayInformationPolicy=_RcIpDhcpRelayInformationPolicy_Object((1,3,6,1,4,1,8886,6,1,30,2,2),_RcIpDhcpRelayInformationPolicy_Type())
rcIpDhcpRelayInformationPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpDhcpRelayInformationPolicy.setStatus(_C)
_RcIpDhcpRelayInformationOptionTrustTable_Object=MibTable
rcIpDhcpRelayInformationOptionTrustTable=_RcIpDhcpRelayInformationOptionTrustTable_Object((1,3,6,1,4,1,8886,6,1,30,2,3))
if mibBuilder.loadTexts:rcIpDhcpRelayInformationOptionTrustTable.setStatus(_C)
_RcIpDhcpRelayInformationOptionTrustEntry_Object=MibTableRow
rcIpDhcpRelayInformationOptionTrustEntry=_RcIpDhcpRelayInformationOptionTrustEntry_Object((1,3,6,1,4,1,8886,6,1,30,2,3,1))
rcIpDhcpRelayInformationOptionTrustEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:rcIpDhcpRelayInformationOptionTrustEntry.setStatus(_C)
_RcIpDhcpRelayInformationOptionTrustPortIfIndex_Type=Integer32
_RcIpDhcpRelayInformationOptionTrustPortIfIndex_Object=MibTableColumn
rcIpDhcpRelayInformationOptionTrustPortIfIndex=_RcIpDhcpRelayInformationOptionTrustPortIfIndex_Object((1,3,6,1,4,1,8886,6,1,30,2,3,1,1),_RcIpDhcpRelayInformationOptionTrustPortIfIndex_Type())
rcIpDhcpRelayInformationOptionTrustPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpRelayInformationOptionTrustPortIfIndex.setStatus(_C)
class _RcIpDhcpRelayInformationOptionTrustState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trusted',1),('untrusted',2)))
_RcIpDhcpRelayInformationOptionTrustState_Type.__name__=_G
_RcIpDhcpRelayInformationOptionTrustState_Object=MibTableColumn
rcIpDhcpRelayInformationOptionTrustState=_RcIpDhcpRelayInformationOptionTrustState_Object((1,3,6,1,4,1,8886,6,1,30,2,3,1,2),_RcIpDhcpRelayInformationOptionTrustState_Type())
rcIpDhcpRelayInformationOptionTrustState.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpDhcpRelayInformationOptionTrustState.setStatus(_C)
_RcIpDhcpRelayStatistics_ObjectIdentity=ObjectIdentity
rcIpDhcpRelayStatistics=_RcIpDhcpRelayStatistics_ObjectIdentity((1,3,6,1,4,1,8886,6,1,30,3))
_RcIpDhcpRelayStatsBootpsRcv_Type=Counter32
_RcIpDhcpRelayStatsBootpsRcv_Object=MibScalar
rcIpDhcpRelayStatsBootpsRcv=_RcIpDhcpRelayStatsBootpsRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,1),_RcIpDhcpRelayStatsBootpsRcv_Type())
rcIpDhcpRelayStatsBootpsRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsBootpsRcv.setStatus(_B)
_RcIpDhcpRelayStatsBootpsSnd_Type=Counter32
_RcIpDhcpRelayStatsBootpsSnd_Object=MibScalar
rcIpDhcpRelayStatsBootpsSnd=_RcIpDhcpRelayStatsBootpsSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,2),_RcIpDhcpRelayStatsBootpsSnd_Type())
rcIpDhcpRelayStatsBootpsSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsBootpsSnd.setStatus(_B)
_RcIpDhcpRelayStatsDiscoversRcv_Type=Counter32
_RcIpDhcpRelayStatsDiscoversRcv_Object=MibScalar
rcIpDhcpRelayStatsDiscoversRcv=_RcIpDhcpRelayStatsDiscoversRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,3),_RcIpDhcpRelayStatsDiscoversRcv_Type())
rcIpDhcpRelayStatsDiscoversRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsDiscoversRcv.setStatus(_B)
_RcIpDhcpRelayStatsDiscoversSnd_Type=Counter32
_RcIpDhcpRelayStatsDiscoversSnd_Object=MibScalar
rcIpDhcpRelayStatsDiscoversSnd=_RcIpDhcpRelayStatsDiscoversSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,4),_RcIpDhcpRelayStatsDiscoversSnd_Type())
rcIpDhcpRelayStatsDiscoversSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsDiscoversSnd.setStatus(_B)
_RcIpDhcpRelayStatsRequestsRcv_Type=Counter32
_RcIpDhcpRelayStatsRequestsRcv_Object=MibScalar
rcIpDhcpRelayStatsRequestsRcv=_RcIpDhcpRelayStatsRequestsRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,5),_RcIpDhcpRelayStatsRequestsRcv_Type())
rcIpDhcpRelayStatsRequestsRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsRequestsRcv.setStatus(_B)
_RcIpDhcpRelayStatsRequestsSnd_Type=Counter32
_RcIpDhcpRelayStatsRequestsSnd_Object=MibScalar
rcIpDhcpRelayStatsRequestsSnd=_RcIpDhcpRelayStatsRequestsSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,6),_RcIpDhcpRelayStatsRequestsSnd_Type())
rcIpDhcpRelayStatsRequestsSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsRequestsSnd.setStatus(_B)
_RcIpDhcpRelayStatsReleasesRcv_Type=Counter32
_RcIpDhcpRelayStatsReleasesRcv_Object=MibScalar
rcIpDhcpRelayStatsReleasesRcv=_RcIpDhcpRelayStatsReleasesRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,7),_RcIpDhcpRelayStatsReleasesRcv_Type())
rcIpDhcpRelayStatsReleasesRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsReleasesRcv.setStatus(_B)
_RcIpDhcpRelayStatsReleasesSnd_Type=Counter32
_RcIpDhcpRelayStatsReleasesSnd_Object=MibScalar
rcIpDhcpRelayStatsReleasesSnd=_RcIpDhcpRelayStatsReleasesSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,8),_RcIpDhcpRelayStatsReleasesSnd_Type())
rcIpDhcpRelayStatsReleasesSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsReleasesSnd.setStatus(_B)
_RcIpDhcpRelayStatsOffersRcv_Type=Counter32
_RcIpDhcpRelayStatsOffersRcv_Object=MibScalar
rcIpDhcpRelayStatsOffersRcv=_RcIpDhcpRelayStatsOffersRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,9),_RcIpDhcpRelayStatsOffersRcv_Type())
rcIpDhcpRelayStatsOffersRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsOffersRcv.setStatus(_B)
_RcIpDhcpRelayStatsOffersSnd_Type=Counter32
_RcIpDhcpRelayStatsOffersSnd_Object=MibScalar
rcIpDhcpRelayStatsOffersSnd=_RcIpDhcpRelayStatsOffersSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,10),_RcIpDhcpRelayStatsOffersSnd_Type())
rcIpDhcpRelayStatsOffersSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsOffersSnd.setStatus(_B)
_RcIpDhcpRelayStatsAcksRcv_Type=Counter32
_RcIpDhcpRelayStatsAcksRcv_Object=MibScalar
rcIpDhcpRelayStatsAcksRcv=_RcIpDhcpRelayStatsAcksRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,11),_RcIpDhcpRelayStatsAcksRcv_Type())
rcIpDhcpRelayStatsAcksRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsAcksRcv.setStatus(_B)
_RcIpDhcpRelayStatsAcksSnd_Type=Counter32
_RcIpDhcpRelayStatsAcksSnd_Object=MibScalar
rcIpDhcpRelayStatsAcksSnd=_RcIpDhcpRelayStatsAcksSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,12),_RcIpDhcpRelayStatsAcksSnd_Type())
rcIpDhcpRelayStatsAcksSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsAcksSnd.setStatus(_B)
_RcIpDhcpRelayStatsNacksRcv_Type=Counter32
_RcIpDhcpRelayStatsNacksRcv_Object=MibScalar
rcIpDhcpRelayStatsNacksRcv=_RcIpDhcpRelayStatsNacksRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,13),_RcIpDhcpRelayStatsNacksRcv_Type())
rcIpDhcpRelayStatsNacksRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsNacksRcv.setStatus(_B)
_RcIpDhcpRelayStatsNacksSnd_Type=Counter32
_RcIpDhcpRelayStatsNacksSnd_Object=MibScalar
rcIpDhcpRelayStatsNacksSnd=_RcIpDhcpRelayStatsNacksSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,14),_RcIpDhcpRelayStatsNacksSnd_Type())
rcIpDhcpRelayStatsNacksSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsNacksSnd.setStatus(_B)
_RcIpDhcpRelayStatsDeclinesRcv_Type=Counter32
_RcIpDhcpRelayStatsDeclinesRcv_Object=MibScalar
rcIpDhcpRelayStatsDeclinesRcv=_RcIpDhcpRelayStatsDeclinesRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,15),_RcIpDhcpRelayStatsDeclinesRcv_Type())
rcIpDhcpRelayStatsDeclinesRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsDeclinesRcv.setStatus(_B)
_RcIpDhcpRelayStatsDeclinesSnd_Type=Counter32
_RcIpDhcpRelayStatsDeclinesSnd_Object=MibScalar
rcIpDhcpRelayStatsDeclinesSnd=_RcIpDhcpRelayStatsDeclinesSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,16),_RcIpDhcpRelayStatsDeclinesSnd_Type())
rcIpDhcpRelayStatsDeclinesSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsDeclinesSnd.setStatus(_B)
_RcIpDhcpRelayStatsInformationsRcv_Type=Counter32
_RcIpDhcpRelayStatsInformationsRcv_Object=MibScalar
rcIpDhcpRelayStatsInformationsRcv=_RcIpDhcpRelayStatsInformationsRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,17),_RcIpDhcpRelayStatsInformationsRcv_Type())
rcIpDhcpRelayStatsInformationsRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsInformationsRcv.setStatus(_B)
_RcIpDhcpRelayStatsInformationsSnd_Type=Counter32
_RcIpDhcpRelayStatsInformationsSnd_Object=MibScalar
rcIpDhcpRelayStatsInformationsSnd=_RcIpDhcpRelayStatsInformationsSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,18),_RcIpDhcpRelayStatsInformationsSnd_Type())
rcIpDhcpRelayStatsInformationsSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsInformationsSnd.setStatus(_B)
_RcIpDhcpRelayStatsUnknowns_Type=Counter32
_RcIpDhcpRelayStatsUnknowns_Object=MibScalar
rcIpDhcpRelayStatsUnknowns=_RcIpDhcpRelayStatsUnknowns_Object((1,3,6,1,4,1,8886,6,1,30,3,19),_RcIpDhcpRelayStatsUnknowns_Type())
rcIpDhcpRelayStatsUnknowns.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsUnknowns.setStatus(_B)
_RcIpDhcpRelayStatsPacketsRcv_Type=Counter32
_RcIpDhcpRelayStatsPacketsRcv_Object=MibScalar
rcIpDhcpRelayStatsPacketsRcv=_RcIpDhcpRelayStatsPacketsRcv_Object((1,3,6,1,4,1,8886,6,1,30,3,20),_RcIpDhcpRelayStatsPacketsRcv_Type())
rcIpDhcpRelayStatsPacketsRcv.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsPacketsRcv.setStatus(_B)
_RcIpDhcpRelayStatsPacketsSnd_Type=Counter32
_RcIpDhcpRelayStatsPacketsSnd_Object=MibScalar
rcIpDhcpRelayStatsPacketsSnd=_RcIpDhcpRelayStatsPacketsSnd_Object((1,3,6,1,4,1,8886,6,1,30,3,21),_RcIpDhcpRelayStatsPacketsSnd_Type())
rcIpDhcpRelayStatsPacketsSnd.setMaxAccess(_A)
if mibBuilder.loadTexts:rcIpDhcpRelayStatsPacketsSnd.setStatus(_B)
mibBuilder.exportSymbols(_E,**{'rcIpDhcpRelay':rcIpDhcpRelay,'rcIpDhcpRelayConfig':rcIpDhcpRelayConfig,'rcIpDhcpRelayEnable':rcIpDhcpRelayEnable,'rcIpDhcpRelayStartTime':rcIpDhcpRelayStartTime,'rcIpDhcpRelayIpInterfaceTable':rcIpDhcpRelayIpInterfaceTable,'rcIpDhcpRelayIpInterfaceEntry':rcIpDhcpRelayIpInterfaceEntry,_I:rcIpDhcpRelayIpInterfaceIfIndex,'rcIpDhcpRelayIpInterfaceEnable':rcIpDhcpRelayIpInterfaceEnable,'rcIpDhcpRelayTargetTable':rcIpDhcpRelayTargetTable,'rcIpDhcpRelayTargetEntry':rcIpDhcpRelayTargetEntry,_J:rcIpDhcpRelayTargetIfIndex,_K:rcIpDhcpRelayTargetAddress,'rcIpDhcpRelayTargetRowStatus':rcIpDhcpRelayTargetRowStatus,'rcIpDhcpRelayInformationOptionGroup':rcIpDhcpRelayInformationOptionGroup,'rcIpDhcpRelayInformationOption':rcIpDhcpRelayInformationOption,'rcIpDhcpRelayInformationPolicy':rcIpDhcpRelayInformationPolicy,'rcIpDhcpRelayInformationOptionTrustTable':rcIpDhcpRelayInformationOptionTrustTable,'rcIpDhcpRelayInformationOptionTrustEntry':rcIpDhcpRelayInformationOptionTrustEntry,_L:rcIpDhcpRelayInformationOptionTrustPortIfIndex,'rcIpDhcpRelayInformationOptionTrustState':rcIpDhcpRelayInformationOptionTrustState,'rcIpDhcpRelayStatistics':rcIpDhcpRelayStatistics,'rcIpDhcpRelayStatsBootpsRcv':rcIpDhcpRelayStatsBootpsRcv,'rcIpDhcpRelayStatsBootpsSnd':rcIpDhcpRelayStatsBootpsSnd,'rcIpDhcpRelayStatsDiscoversRcv':rcIpDhcpRelayStatsDiscoversRcv,'rcIpDhcpRelayStatsDiscoversSnd':rcIpDhcpRelayStatsDiscoversSnd,'rcIpDhcpRelayStatsRequestsRcv':rcIpDhcpRelayStatsRequestsRcv,'rcIpDhcpRelayStatsRequestsSnd':rcIpDhcpRelayStatsRequestsSnd,'rcIpDhcpRelayStatsReleasesRcv':rcIpDhcpRelayStatsReleasesRcv,'rcIpDhcpRelayStatsReleasesSnd':rcIpDhcpRelayStatsReleasesSnd,'rcIpDhcpRelayStatsOffersRcv':rcIpDhcpRelayStatsOffersRcv,'rcIpDhcpRelayStatsOffersSnd':rcIpDhcpRelayStatsOffersSnd,'rcIpDhcpRelayStatsAcksRcv':rcIpDhcpRelayStatsAcksRcv,'rcIpDhcpRelayStatsAcksSnd':rcIpDhcpRelayStatsAcksSnd,'rcIpDhcpRelayStatsNacksRcv':rcIpDhcpRelayStatsNacksRcv,'rcIpDhcpRelayStatsNacksSnd':rcIpDhcpRelayStatsNacksSnd,'rcIpDhcpRelayStatsDeclinesRcv':rcIpDhcpRelayStatsDeclinesRcv,'rcIpDhcpRelayStatsDeclinesSnd':rcIpDhcpRelayStatsDeclinesSnd,'rcIpDhcpRelayStatsInformationsRcv':rcIpDhcpRelayStatsInformationsRcv,'rcIpDhcpRelayStatsInformationsSnd':rcIpDhcpRelayStatsInformationsSnd,'rcIpDhcpRelayStatsUnknowns':rcIpDhcpRelayStatsUnknowns,'rcIpDhcpRelayStatsPacketsRcv':rcIpDhcpRelayStatsPacketsRcv,'rcIpDhcpRelayStatsPacketsSnd':rcIpDhcpRelayStatsPacketsSnd})