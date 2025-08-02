_I='altigaDnsStatsGroup'
_H='alDnsStatsMiscFailures'
_G='alDnsStatsUnreachableServerFailures'
_F='alDnsStatsTimeoutFailures'
_E='alDnsStatsSuccessfulResponses'
_D='alDnsStatsAttemptedQueries'
_C='read-only'
_B='ALTIGA-DNS-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alDnsMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alDnsMibModule')
alDnsGroup,alStatsDns=mibBuilder.importSymbols('ALTIGA-MIB','alDnsGroup','alStatsDns')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaDnsStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,23,2))
if mibBuilder.loadTexts:altigaDnsStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaDnsStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaDnsStatsMibConformance=_AltigaDnsStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,23,2,1))
_AltigaDnsStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaDnsStatsMibCompliances=_AltigaDnsStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,23,2,1,1))
_AlStatsDnsResolverGlobal_ObjectIdentity=ObjectIdentity
alStatsDnsResolverGlobal=_AlStatsDnsResolverGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,18,1))
_AlDnsStatsAttemptedQueries_Type=Gauge32
_AlDnsStatsAttemptedQueries_Object=MibScalar
alDnsStatsAttemptedQueries=_AlDnsStatsAttemptedQueries_Object((1,3,6,1,4,1,3076,2,1,2,18,1,1),_AlDnsStatsAttemptedQueries_Type())
alDnsStatsAttemptedQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:alDnsStatsAttemptedQueries.setStatus(_A)
_AlDnsStatsSuccessfulResponses_Type=Gauge32
_AlDnsStatsSuccessfulResponses_Object=MibScalar
alDnsStatsSuccessfulResponses=_AlDnsStatsSuccessfulResponses_Object((1,3,6,1,4,1,3076,2,1,2,18,1,2),_AlDnsStatsSuccessfulResponses_Type())
alDnsStatsSuccessfulResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:alDnsStatsSuccessfulResponses.setStatus(_A)
_AlDnsStatsTimeoutFailures_Type=Gauge32
_AlDnsStatsTimeoutFailures_Object=MibScalar
alDnsStatsTimeoutFailures=_AlDnsStatsTimeoutFailures_Object((1,3,6,1,4,1,3076,2,1,2,18,1,3),_AlDnsStatsTimeoutFailures_Type())
alDnsStatsTimeoutFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:alDnsStatsTimeoutFailures.setStatus(_A)
_AlDnsStatsUnreachableServerFailures_Type=Gauge32
_AlDnsStatsUnreachableServerFailures_Object=MibScalar
alDnsStatsUnreachableServerFailures=_AlDnsStatsUnreachableServerFailures_Object((1,3,6,1,4,1,3076,2,1,2,18,1,4),_AlDnsStatsUnreachableServerFailures_Type())
alDnsStatsUnreachableServerFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:alDnsStatsUnreachableServerFailures.setStatus(_A)
_AlDnsStatsMiscFailures_Type=Gauge32
_AlDnsStatsMiscFailures_Object=MibScalar
alDnsStatsMiscFailures=_AlDnsStatsMiscFailures_Object((1,3,6,1,4,1,3076,2,1,2,18,1,5),_AlDnsStatsMiscFailures_Type())
alDnsStatsMiscFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:alDnsStatsMiscFailures.setStatus(_A)
altigaDnsStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,18,2))
altigaDnsStatsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:altigaDnsStatsGroup.setStatus(_A)
altigaDnsStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,23,2,1,1,1))
altigaDnsStatsMibCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:altigaDnsStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaDnsStatsMibModule':altigaDnsStatsMibModule,'altigaDnsStatsMibConformance':altigaDnsStatsMibConformance,'altigaDnsStatsMibCompliances':altigaDnsStatsMibCompliances,'altigaDnsStatsMibCompliance':altigaDnsStatsMibCompliance,_I:altigaDnsStatsGroup,'alStatsDnsResolverGlobal':alStatsDnsResolverGlobal,_D:alDnsStatsAttemptedQueries,_E:alDnsStatsSuccessfulResponses,_F:alDnsStatsTimeoutFailures,_G:alDnsStatsUnreachableServerFailures,_H:alDnsStatsMiscFailures})