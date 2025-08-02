_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
RtrStatus,=mibBuilder.importSymbols('FOUNDRY-SN-IP-MIB','RtrStatus')
fdryIpv6,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','fdryIpv6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fdryIpv6MIB=ModuleIdentity((1,3,6,1,4,1,1991,1,2,17,1))
if mibBuilder.loadTexts:fdryIpv6MIB.setRevisions(('2017-08-07 00:00','2010-05-06 00:00'))
_FdryIpv6GlobalObjects_ObjectIdentity=ObjectIdentity
fdryIpv6GlobalObjects=_FdryIpv6GlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,2,17,1,1))
_FdryIpv6LoadShare_Type=RtrStatus
_FdryIpv6LoadShare_Object=MibScalar
fdryIpv6LoadShare=_FdryIpv6LoadShare_Object((1,3,6,1,4,1,1991,1,2,17,1,1,1),_FdryIpv6LoadShare_Type())
fdryIpv6LoadShare.setMaxAccess(_A)
if mibBuilder.loadTexts:fdryIpv6LoadShare.setStatus(_B)
_FdryIpv6LoadShareNumOfPaths_Type=Unsigned32
_FdryIpv6LoadShareNumOfPaths_Object=MibScalar
fdryIpv6LoadShareNumOfPaths=_FdryIpv6LoadShareNumOfPaths_Object((1,3,6,1,4,1,1991,1,2,17,1,1,2),_FdryIpv6LoadShareNumOfPaths_Type())
fdryIpv6LoadShareNumOfPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:fdryIpv6LoadShareNumOfPaths.setStatus(_B)
mibBuilder.exportSymbols('FDRY-IPV6-IP-MIB',**{'fdryIpv6MIB':fdryIpv6MIB,'fdryIpv6GlobalObjects':fdryIpv6GlobalObjects,'fdryIpv6LoadShare':fdryIpv6LoadShare,'fdryIpv6LoadShareNumOfPaths':fdryIpv6LoadShareNumOfPaths})