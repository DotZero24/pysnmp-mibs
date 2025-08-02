_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsu,=mibBuilder.importSymbols('ANIROOT-MIB','bsu')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aniBsuBridge=ModuleIdentity((1,3,6,1,4,1,4325,3,5))
class _AniBsuSuBridgeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),('not-applicable',3)))
_AniBsuSuBridgeEnable_Type.__name__=_A
_AniBsuSuBridgeEnable_Object=MibScalar
aniBsuSuBridgeEnable=_AniBsuSuBridgeEnable_Object((1,3,6,1,4,1,4325,3,5,1),_AniBsuSuBridgeEnable_Type())
aniBsuSuBridgeEnable.setMaxAccess('read-only')
if mibBuilder.loadTexts:aniBsuSuBridgeEnable.setStatus('current')
mibBuilder.exportSymbols('BSU-BRGCLUSTER-MIB',**{'aniBsuBridge':aniBsuBridge,'aniBsuSuBridgeEnable':aniBsuSuBridgeEnable})