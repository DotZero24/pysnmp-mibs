_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelRouterSnmpTrapGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,7))
if mibBuilder.loadTexts:mitelRouterSnmpTrapGroup.setRevisions(('2003-03-24 10:50','2002-04-02 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
class _MitelSnmpTrapGlobal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MitelSnmpTrapGlobal_Type.__name__=_A
_MitelSnmpTrapGlobal_Object=MibScalar
mitelSnmpTrapGlobal=_MitelSnmpTrapGlobal_Object((1,3,6,1,4,1,1027,4,8,1,7,1),_MitelSnmpTrapGlobal_Type())
mitelSnmpTrapGlobal.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelSnmpTrapGlobal.setStatus(_C)
_MitelSnmpTrapControl_Type=Integer32
_MitelSnmpTrapControl_Object=MibScalar
mitelSnmpTrapControl=_MitelSnmpTrapControl_Object((1,3,6,1,4,1,1027,4,8,1,7,2),_MitelSnmpTrapControl_Type())
mitelSnmpTrapControl.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelSnmpTrapControl.setStatus(_C)
mibBuilder.exportSymbols('MITEL-TRAPGROUP-MIB',**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterSnmpTrapGroup':mitelRouterSnmpTrapGroup,'mitelSnmpTrapGlobal':mitelSnmpTrapGlobal,'mitelSnmpTrapControl':mitelSnmpTrapControl})