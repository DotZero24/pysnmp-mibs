_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','snSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snArpInfo=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,22))
_SnArpStats_ObjectIdentity=ObjectIdentity
snArpStats=_SnArpStats_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,22,1))
_SnArpStatsTotalReceived_Type=Counter32
_SnArpStatsTotalReceived_Object=MibScalar
snArpStatsTotalReceived=_SnArpStatsTotalReceived_Object((1,3,6,1,4,1,1991,1,1,3,22,1,1),_SnArpStatsTotalReceived_Type())
snArpStatsTotalReceived.setMaxAccess(_A)
if mibBuilder.loadTexts:snArpStatsTotalReceived.setStatus(_B)
_SnArpStatsRequestReceived_Type=Counter32
_SnArpStatsRequestReceived_Object=MibScalar
snArpStatsRequestReceived=_SnArpStatsRequestReceived_Object((1,3,6,1,4,1,1991,1,1,3,22,1,2),_SnArpStatsRequestReceived_Type())
snArpStatsRequestReceived.setMaxAccess(_A)
if mibBuilder.loadTexts:snArpStatsRequestReceived.setStatus(_B)
_SnArpStatsRequestSent_Type=Counter32
_SnArpStatsRequestSent_Object=MibScalar
snArpStatsRequestSent=_SnArpStatsRequestSent_Object((1,3,6,1,4,1,1991,1,1,3,22,1,3),_SnArpStatsRequestSent_Type())
snArpStatsRequestSent.setMaxAccess(_A)
if mibBuilder.loadTexts:snArpStatsRequestSent.setStatus(_B)
_SnArpStatsRepliesSent_Type=Counter32
_SnArpStatsRepliesSent_Object=MibScalar
snArpStatsRepliesSent=_SnArpStatsRepliesSent_Object((1,3,6,1,4,1,1991,1,1,3,22,1,4),_SnArpStatsRepliesSent_Type())
snArpStatsRepliesSent.setMaxAccess(_A)
if mibBuilder.loadTexts:snArpStatsRepliesSent.setStatus(_B)
_SnArpStatsPendingDrop_Type=Counter32
_SnArpStatsPendingDrop_Object=MibScalar
snArpStatsPendingDrop=_SnArpStatsPendingDrop_Object((1,3,6,1,4,1,1991,1,1,3,22,1,5),_SnArpStatsPendingDrop_Type())
snArpStatsPendingDrop.setMaxAccess(_A)
if mibBuilder.loadTexts:snArpStatsPendingDrop.setStatus(_B)
_SnArpStatsInvalidSource_Type=Counter32
_SnArpStatsInvalidSource_Object=MibScalar
snArpStatsInvalidSource=_SnArpStatsInvalidSource_Object((1,3,6,1,4,1,1991,1,1,3,22,1,6),_SnArpStatsInvalidSource_Type())
snArpStatsInvalidSource.setMaxAccess(_A)
if mibBuilder.loadTexts:snArpStatsInvalidSource.setStatus(_B)
_SnArpStatsInvalidDestination_Type=Counter32
_SnArpStatsInvalidDestination_Object=MibScalar
snArpStatsInvalidDestination=_SnArpStatsInvalidDestination_Object((1,3,6,1,4,1,1991,1,1,3,22,1,7),_SnArpStatsInvalidDestination_Type())
snArpStatsInvalidDestination.setMaxAccess(_A)
if mibBuilder.loadTexts:snArpStatsInvalidDestination.setStatus(_B)
mibBuilder.exportSymbols('FOUNDRY-SN-ARP-GROUP-MIB',**{'snArpInfo':snArpInfo,'snArpStats':snArpStats,'snArpStatsTotalReceived':snArpStatsTotalReceived,'snArpStatsRequestReceived':snArpStatsRequestReceived,'snArpStatsRequestSent':snArpStatsRequestSent,'snArpStatsRepliesSent':snArpStatsRepliesSent,'snArpStatsPendingDrop':snArpStatsPendingDrop,'snArpStatsInvalidSource':snArpStatsInvalidSource,'snArpStatsInvalidDestination':snArpStatsInvalidDestination})