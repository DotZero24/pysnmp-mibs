_L='eltCpuRateLimiterValue'
_K='eltCpuRateStatisticsIndex'
_J='tcpSyn'
_I='mcRpfFailed'
_H='mcRouting'
_G='arpInspec'
_F='telnet'
_E='eltCpuRateLimiterIndex'
_D='Integer32'
_C='read-only'
_B='ELTEX-MES-SWITCH-RATE-LIMITER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesSwitchRateLimiterMIB,=mibBuilder.importSymbols('ELTEX-MES-MNG-MIB','eltMesSwitchRateLimiterMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class EltCpuRateLimiterTrafficType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('http',1),(_F,2),('ssh',3),('snmp',4),('ip',5),('linkLocal',6),('arp',7),(_G,8),('stpBpdu',9),('otherBpdu',10),('ipRouting',11),('ipOptions',12),('dhcpSnoop',13),('igmpSnoop',14),('mldSnoop',15),('sflow',16),('ace',17),('ipErrors',18),('other',19),('dhcpv6Snoop',20),('vrrp',21),(_H,22),(_I,23),(_J,24)))
class EltCpuRateStatisticsTrafficType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)));namedValues=NamedValues(*(('stack',1),('http',2),(_F,3),('ssh',4),('snmp',5),('ip',6),('arp',7),(_G,8),('stp',9),('ieee',10),('routeUnknown',11),('ipHopByHop',12),('mtuExceeded',13),('ipv4Multicast',14),('ipv6Multicast',15),('dhcpSnooping',16),('igmpSnooping',17),('mldSnooping',18),('ttlExceeded',19),('ipv4IllegalAddress',20),('ipv4HeaderError',21),('ipDaMismatch',22),('sflow',23),('logDenyAces',24),('dhcpv6Snooping',25),('vrrp',26),('logPermitAces',27),('ipv6HeaderError',28),(_H,29),(_I,30),(_J,31),('vpc',32)))
_EltMesSwitchRateLimiterObjects_ObjectIdentity=ObjectIdentity
eltMesSwitchRateLimiterObjects=_EltMesSwitchRateLimiterObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,773,1))
_EltMesCpuRateLimiterNotifications_ObjectIdentity=ObjectIdentity
eltMesCpuRateLimiterNotifications=_EltMesCpuRateLimiterNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,773,1,0))
_EltMesSwitchRateLimiterConfig_ObjectIdentity=ObjectIdentity
eltMesSwitchRateLimiterConfig=_EltMesSwitchRateLimiterConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,773,1,1))
_EltCpuRateLimiterTable_Object=MibTable
eltCpuRateLimiterTable=_EltCpuRateLimiterTable_Object((1,3,6,1,4,1,35265,1,23,1,773,1,1,1))
if mibBuilder.loadTexts:eltCpuRateLimiterTable.setStatus(_A)
_EltCpuRateLimiterEntry_Object=MibTableRow
eltCpuRateLimiterEntry=_EltCpuRateLimiterEntry_Object((1,3,6,1,4,1,35265,1,23,1,773,1,1,1,1))
eltCpuRateLimiterEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:eltCpuRateLimiterEntry.setStatus(_A)
_EltCpuRateLimiterIndex_Type=EltCpuRateLimiterTrafficType
_EltCpuRateLimiterIndex_Object=MibTableColumn
eltCpuRateLimiterIndex=_EltCpuRateLimiterIndex_Object((1,3,6,1,4,1,35265,1,23,1,773,1,1,1,1,1),_EltCpuRateLimiterIndex_Type())
eltCpuRateLimiterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCpuRateLimiterIndex.setStatus(_A)
class _EltCpuRateLimiterValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltCpuRateLimiterValue_Type.__name__=_D
_EltCpuRateLimiterValue_Object=MibTableColumn
eltCpuRateLimiterValue=_EltCpuRateLimiterValue_Object((1,3,6,1,4,1,35265,1,23,1,773,1,1,1,1,2),_EltCpuRateLimiterValue_Type())
eltCpuRateLimiterValue.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltCpuRateLimiterValue.setStatus(_A)
class _EltCpuRateDefaultLimiterValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltCpuRateDefaultLimiterValue_Type.__name__=_D
_EltCpuRateDefaultLimiterValue_Object=MibTableColumn
eltCpuRateDefaultLimiterValue=_EltCpuRateDefaultLimiterValue_Object((1,3,6,1,4,1,35265,1,23,1,773,1,1,1,1,3),_EltCpuRateDefaultLimiterValue_Type())
eltCpuRateDefaultLimiterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCpuRateDefaultLimiterValue.setStatus(_A)
_EltMesSwitchRateLimiterStatistics_ObjectIdentity=ObjectIdentity
eltMesSwitchRateLimiterStatistics=_EltMesSwitchRateLimiterStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,773,1,2))
_EltCpuRateStatisticsTable_Object=MibTable
eltCpuRateStatisticsTable=_EltCpuRateStatisticsTable_Object((1,3,6,1,4,1,35265,1,23,1,773,1,2,1))
if mibBuilder.loadTexts:eltCpuRateStatisticsTable.setStatus(_A)
_EltCpuRateStatisticsEntry_Object=MibTableRow
eltCpuRateStatisticsEntry=_EltCpuRateStatisticsEntry_Object((1,3,6,1,4,1,35265,1,23,1,773,1,2,1,1))
eltCpuRateStatisticsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:eltCpuRateStatisticsEntry.setStatus(_A)
_EltCpuRateStatisticsIndex_Type=EltCpuRateStatisticsTrafficType
_EltCpuRateStatisticsIndex_Object=MibTableColumn
eltCpuRateStatisticsIndex=_EltCpuRateStatisticsIndex_Object((1,3,6,1,4,1,35265,1,23,1,773,1,2,1,1,1),_EltCpuRateStatisticsIndex_Type())
eltCpuRateStatisticsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCpuRateStatisticsIndex.setStatus(_A)
_EltCpuRateStatisticsRate_Type=Gauge32
_EltCpuRateStatisticsRate_Object=MibTableColumn
eltCpuRateStatisticsRate=_EltCpuRateStatisticsRate_Object((1,3,6,1,4,1,35265,1,23,1,773,1,2,1,1,2),_EltCpuRateStatisticsRate_Type())
eltCpuRateStatisticsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCpuRateStatisticsRate.setStatus(_A)
_EltCpuRateStatisticsCounter_Type=Counter32
_EltCpuRateStatisticsCounter_Object=MibTableColumn
eltCpuRateStatisticsCounter=_EltCpuRateStatisticsCounter_Object((1,3,6,1,4,1,35265,1,23,1,773,1,2,1,1,3),_EltCpuRateStatisticsCounter_Type())
eltCpuRateStatisticsCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCpuRateStatisticsCounter.setStatus(_A)
eltCpuRateLimiterTrap=NotificationType((1,3,6,1,4,1,35265,1,23,1,773,1,0,1))
eltCpuRateLimiterTrap.setObjects(*((_B,_E),(_B,_L)))
if mibBuilder.loadTexts:eltCpuRateLimiterTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EltCpuRateLimiterTrafficType':EltCpuRateLimiterTrafficType,'EltCpuRateStatisticsTrafficType':EltCpuRateStatisticsTrafficType,'eltMesSwitchRateLimiterObjects':eltMesSwitchRateLimiterObjects,'eltMesCpuRateLimiterNotifications':eltMesCpuRateLimiterNotifications,'eltCpuRateLimiterTrap':eltCpuRateLimiterTrap,'eltMesSwitchRateLimiterConfig':eltMesSwitchRateLimiterConfig,'eltCpuRateLimiterTable':eltCpuRateLimiterTable,'eltCpuRateLimiterEntry':eltCpuRateLimiterEntry,_E:eltCpuRateLimiterIndex,_L:eltCpuRateLimiterValue,'eltCpuRateDefaultLimiterValue':eltCpuRateDefaultLimiterValue,'eltMesSwitchRateLimiterStatistics':eltMesSwitchRateLimiterStatistics,'eltCpuRateStatisticsTable':eltCpuRateStatisticsTable,'eltCpuRateStatisticsEntry':eltCpuRateStatisticsEntry,_K:eltCpuRateStatisticsIndex,'eltCpuRateStatisticsRate':eltCpuRateStatisticsRate,'eltCpuRateStatisticsCounter':eltCpuRateStatisticsCounter})