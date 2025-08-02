_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rl3sw2swTables=ModuleIdentity((1,3,6,1,4,1,4526,17,63))
if mibBuilder.loadTexts:rl3sw2swTables.setRevisions(('2007-01-02 00:00',))
class _Rl3sw2swTablesPollingInterval_Type(Integer32):defaultValue=3
_Rl3sw2swTablesPollingInterval_Type.__name__=_A
_Rl3sw2swTablesPollingInterval_Object=MibScalar
rl3sw2swTablesPollingInterval=_Rl3sw2swTablesPollingInterval_Object((1,3,6,1,4,1,4526,17,63,1),_Rl3sw2swTablesPollingInterval_Type())
rl3sw2swTablesPollingInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:rl3sw2swTablesPollingInterval.setStatus('current')
mibBuilder.exportSymbols('NETGEAR-RADLAN-3SW2SWTABLES-MIB',**{'rl3sw2swTables':rl3sw2swTables,'rl3sw2swTablesPollingInterval':rl3sw2swTablesPollingInterval})