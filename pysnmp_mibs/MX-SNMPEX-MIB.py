_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snmpMIBObjects,=mibBuilder.importSymbols('MX-SNMP-MIB','snmpMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snmpExMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,900,1,100))
if mibBuilder.loadTexts:snmpExMIB.setRevisions(('1904-11-15 00:00',))
_SnmpExMIBObjects_ObjectIdentity=ObjectIdentity
snmpExMIBObjects=_SnmpExMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,900,1,100,1))
_Access_ObjectIdentity=ObjectIdentity
access=_Access_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,900,1,100,1,100))
_LastResult_Type=OctetString
_LastResult_Object=MibScalar
lastResult=_LastResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,900,1,100,1,100,100),_LastResult_Type())
lastResult.setMaxAccess('read-only')
if mibBuilder.loadTexts:lastResult.setStatus(_A)
_Command_Type=OctetString
_Command_Object=MibScalar
command=_Command_Object((1,3,6,1,4,1,4935,1000,100,200,100,900,1,100,1,100,200),_Command_Type())
command.setMaxAccess('read-write')
if mibBuilder.loadTexts:command.setStatus(_A)
mibBuilder.exportSymbols('MX-SNMPEX-MIB',**{'snmpExMIB':snmpExMIB,'snmpExMIBObjects':snmpExMIBObjects,'access':access,'lastResult':lastResult,'command':command})