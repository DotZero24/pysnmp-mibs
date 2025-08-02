_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
smIpMIB=ModuleIdentity((1,3,6,1,4,1,29601,100,1,10))
_SmIpGlobal_ObjectIdentity=ObjectIdentity
smIpGlobal=_SmIpGlobal_ObjectIdentity((1,3,6,1,4,1,29601,100,1,10,1))
class _SmIpForwardingStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SmIpForwardingStatus_Type.__name__=_A
_SmIpForwardingStatus_Object=MibScalar
smIpForwardingStatus=_SmIpForwardingStatus_Object((1,3,6,1,4,1,29601,100,1,10,1,1),_SmIpForwardingStatus_Type())
smIpForwardingStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:smIpForwardingStatus.setStatus('current')
mibBuilder.exportSymbols('SIAE-IP-MIB',**{'smIpMIB':smIpMIB,'smIpGlobal':smIpGlobal,'smIpForwardingStatus':smIpForwardingStatus})