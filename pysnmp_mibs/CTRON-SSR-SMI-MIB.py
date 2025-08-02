_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ssr=ModuleIdentity((1,3,6,1,4,1,52,2501))
if mibBuilder.loadTexts:ssr.setRevisions(('2000-07-15 00:00',))
_SsrMibs_ObjectIdentity=ObjectIdentity
ssrMibs=_SsrMibs_ObjectIdentity((1,3,6,1,4,1,52,2501,1))
if mibBuilder.loadTexts:ssrMibs.setStatus(_A)
_SsrTraps_ObjectIdentity=ObjectIdentity
ssrTraps=_SsrTraps_ObjectIdentity((1,3,6,1,4,1,52,2501,10))
if mibBuilder.loadTexts:ssrTraps.setStatus(_A)
mibBuilder.exportSymbols('CTRON-SSR-SMI-MIB',**{'ssr':ssr,'ssrMibs':ssrMibs,'ssrTraps':ssrTraps})