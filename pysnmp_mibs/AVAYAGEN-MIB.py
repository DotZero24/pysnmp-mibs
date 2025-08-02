if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
avaya=ModuleIdentity((1,3,6,1,4,1,6889))
if mibBuilder.loadTexts:avaya.setRevisions(('1905-05-09 09:00','1904-01-27 09:00','1902-08-15 09:00','1902-07-28 09:00','1901-08-09 17:00','1901-06-21 11:55','1900-10-15 10:45','1900-10-15 13:05'))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,6889,1))
_AvGatewayProducts_ObjectIdentity=ObjectIdentity
avGatewayProducts=_AvGatewayProducts_ObjectIdentity((1,3,6,1,4,1,6889,1,6))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,6889,2))
_Lsg_ObjectIdentity=ObjectIdentity
lsg=_Lsg_ObjectIdentity((1,3,6,1,4,1,6889,2,1))
_AvayaEISTopology_ObjectIdentity=ObjectIdentity
avayaEISTopology=_AvayaEISTopology_ObjectIdentity((1,3,6,1,4,1,6889,2,1,10))
_AvayaSystemStats_ObjectIdentity=ObjectIdentity
avayaSystemStats=_AvayaSystemStats_ObjectIdentity((1,3,6,1,4,1,6889,2,1,11))
_AvGatewayMibs_ObjectIdentity=ObjectIdentity
avGatewayMibs=_AvGatewayMibs_ObjectIdentity((1,3,6,1,4,1,6889,2,6))
mibBuilder.exportSymbols('AVAYAGEN-MIB',**{'avaya':avaya,'products':products,'avGatewayProducts':avGatewayProducts,'mibs':mibs,'lsg':lsg,'avayaEISTopology':avayaEISTopology,'avayaSystemStats':avayaSystemStats,'avGatewayMibs':avGatewayMibs})