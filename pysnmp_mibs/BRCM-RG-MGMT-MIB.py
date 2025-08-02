_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
residentialGatewayMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,7))
if mibBuilder.loadTexts:residentialGatewayMgmt.setRevisions(('2007-02-05 00:00','2004-06-16 00:00','2003-03-31 00:00'))
_RgMgmtBase_ObjectIdentity=ObjectIdentity
rgMgmtBase=_RgMgmtBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,7,1))
class _RgOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('residentialGateway',2),('cableHome10',3),('cableHome11',4)))
_RgOperMode_Type.__name__=_C
_RgOperMode_Object=MibScalar
rgOperMode=_RgOperMode_Object((1,3,6,1,4,1,4413,2,2,2,1,7,1,1),_RgOperMode_Type())
rgOperMode.setMaxAccess(_A)
if mibBuilder.loadTexts:rgOperMode.setStatus(_B)
_RgRipEnabled_Type=TruthValue
_RgRipEnabled_Object=MibScalar
rgRipEnabled=_RgRipEnabled_Object((1,3,6,1,4,1,4413,2,2,2,1,7,1,2),_RgRipEnabled_Type())
rgRipEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:rgRipEnabled.setStatus(_B)
_RgVpnEnabled_Type=TruthValue
_RgVpnEnabled_Object=MibScalar
rgVpnEnabled=_RgVpnEnabled_Object((1,3,6,1,4,1,4413,2,2,2,1,7,1,3),_RgVpnEnabled_Type())
rgVpnEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:rgVpnEnabled.setStatus(_B)
mibBuilder.exportSymbols('BRCM-RG-MGMT-MIB',**{'residentialGatewayMgmt':residentialGatewayMgmt,'rgMgmtBase':rgMgmtBase,'rgOperMode':rgOperMode,'rgRipEnabled':rgRipEnabled,'rgVpnEnabled':rgVpnEnabled})