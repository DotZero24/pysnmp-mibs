_E='clabDNSGroup'
_D='clabDnsIpv6QueryForDualMode'
_C='TruthValue'
_B='CLAB-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabCommonMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabCommonMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
clabDNSMib=ModuleIdentity((1,3,6,1,4,1,4491,4,5))
if mibBuilder.loadTexts:clabDNSMib.setRevisions(('2016-02-24 00:00',))
_ClabDNSNotifications_ObjectIdentity=ObjectIdentity
clabDNSNotifications=_ClabDNSNotifications_ObjectIdentity((1,3,6,1,4,1,4491,4,5,0))
_ClabDNSObjects_ObjectIdentity=ObjectIdentity
clabDNSObjects=_ClabDNSObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,5,1))
class _ClabDnsIpv6QueryForDualMode_Type(TruthValue):defaultValue=2
_ClabDnsIpv6QueryForDualMode_Type.__name__=_C
_ClabDnsIpv6QueryForDualMode_Object=MibScalar
clabDnsIpv6QueryForDualMode=_ClabDnsIpv6QueryForDualMode_Object((1,3,6,1,4,1,4491,4,5,1,1),_ClabDnsIpv6QueryForDualMode_Type())
clabDnsIpv6QueryForDualMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:clabDnsIpv6QueryForDualMode.setStatus(_A)
_ClabDNSMibConformance_ObjectIdentity=ObjectIdentity
clabDNSMibConformance=_ClabDNSMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,4,5,2))
_ClabDNSMibCompliances_ObjectIdentity=ObjectIdentity
clabDNSMibCompliances=_ClabDNSMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,4,5,2,1))
_ClabDNSMibGroups_ObjectIdentity=ObjectIdentity
clabDNSMibGroups=_ClabDNSMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,4,5,2,2))
clabDNSGroup=ObjectGroup((1,3,6,1,4,1,4491,4,5,2,2,1))
clabDNSGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:clabDNSGroup.setStatus(_A)
clabDNSCompliance=ModuleCompliance((1,3,6,1,4,1,4491,4,5,2,1,1))
clabDNSCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:clabDNSCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'clabDNSMib':clabDNSMib,'clabDNSNotifications':clabDNSNotifications,'clabDNSObjects':clabDNSObjects,_D:clabDnsIpv6QueryForDualMode,'clabDNSMibConformance':clabDNSMibConformance,'clabDNSMibCompliances':clabDNSMibCompliances,'clabDNSCompliance':clabDNSCompliance,'clabDNSMibGroups':clabDNSMibGroups,_E:clabDNSGroup})