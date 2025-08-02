if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ipAddressConfig,ipAddressStatus,mediatrixIpTelephonySignaling=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixIpTelephonySignaling')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_IpAddressStatusCorNet_ObjectIdentity=ObjectIdentity
ipAddressStatusCorNet=_IpAddressStatusCorNet_ObjectIdentity((1,3,6,1,4,1,4935,10,1,130))
_IpAddressConfigCorNet_ObjectIdentity=ObjectIdentity
ipAddressConfigCorNet=_IpAddressConfigCorNet_ObjectIdentity((1,3,6,1,4,1,4935,15,1,130))
_IpAddressConfigCorNetStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigCorNetStatic=_IpAddressConfigCorNetStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,130,10))
_CorNet_ObjectIdentity=ObjectIdentity
corNet=_CorNet_ObjectIdentity((1,3,6,1,4,1,4935,20,40))
if mibBuilder.loadTexts:corNet.setStatus('current')
mibBuilder.exportSymbols('MX-CORNET-MIB',**{'ipAddressStatusCorNet':ipAddressStatusCorNet,'ipAddressConfigCorNet':ipAddressConfigCorNet,'ipAddressConfigCorNetStatic':ipAddressConfigCorNetStatic,'corNet':corNet})