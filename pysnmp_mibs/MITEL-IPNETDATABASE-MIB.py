_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelRouterDatabaseVersion=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,8))
if mibBuilder.loadTexts:mitelRouterDatabaseVersion.setRevisions(('2003-03-24 09:26',))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelRouterDatabaseMajorVersion_Type=Integer32
_MitelRouterDatabaseMajorVersion_Object=MibScalar
mitelRouterDatabaseMajorVersion=_MitelRouterDatabaseMajorVersion_Object((1,3,6,1,4,1,1027,4,8,1,8,1),_MitelRouterDatabaseMajorVersion_Type())
mitelRouterDatabaseMajorVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:mitelRouterDatabaseMajorVersion.setStatus(_B)
_MitelRouterDatabaseMinorVersion_Type=Integer32
_MitelRouterDatabaseMinorVersion_Object=MibScalar
mitelRouterDatabaseMinorVersion=_MitelRouterDatabaseMinorVersion_Object((1,3,6,1,4,1,1027,4,8,1,8,2),_MitelRouterDatabaseMinorVersion_Type())
mitelRouterDatabaseMinorVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:mitelRouterDatabaseMinorVersion.setStatus(_B)
mibBuilder.exportSymbols('MITEL-IPNETDATABASE-MIB',**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterDatabaseVersion':mitelRouterDatabaseVersion,'mitelRouterDatabaseMajorVersion':mitelRouterDatabaseMajorVersion,'mitelRouterDatabaseMinorVersion':mitelRouterDatabaseMinorVersion})