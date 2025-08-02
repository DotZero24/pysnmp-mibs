_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eap,=mibBuilder.importSymbols('TPLINK-MIB','eap')
clientStatis=ModuleIdentity((1,3,6,1,4,1,11863,10,1,1))
if mibBuilder.loadTexts:clientStatis.setRevisions(('2016-10-17 00:00',))
class _ClientCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_ClientCount_Type.__name__=_A
_ClientCount_Object=MibScalar
clientCount=_ClientCount_Object((1,3,6,1,4,1,11863,10,1,1,1),_ClientCount_Type())
clientCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:clientCount.setStatus('current')
_ClientTable_ObjectIdentity=ObjectIdentity
clientTable=_ClientTable_ObjectIdentity((1,3,6,1,4,1,11863,10,1,1,2))
mibBuilder.exportSymbols('EAP-CLIENT-MIB',**{'clientStatis':clientStatis,'clientCount':clientCount,'clientTable':clientTable})