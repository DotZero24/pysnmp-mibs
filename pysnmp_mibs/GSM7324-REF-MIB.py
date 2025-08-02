if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gsm7324=ModuleIdentity((1,3,6,1,4,1,4526,1,7))
if mibBuilder.loadTexts:gsm7324.setRevisions(('2003-05-06 12:00',))
class AgentPortMask(TextualConvention,OctetString):status='current'
_Netgear_ObjectIdentity=ObjectIdentity
netgear=_Netgear_ObjectIdentity((1,3,6,1,4,1,4526))
_SnmpManagedSwitch_ObjectIdentity=ObjectIdentity
snmpManagedSwitch=_SnmpManagedSwitch_ObjectIdentity((1,3,6,1,4,1,4526,1))
mibBuilder.exportSymbols('GSM7324-REF-MIB',**{'AgentPortMask':AgentPortMask,'netgear':netgear,'snmpManagedSwitch':snmpManagedSwitch,'gsm7324':gsm7324})