_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huawei,hwInternetProtocol,hwLocal=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huawei','hwInternetProtocol','hwLocal')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_RIp_ObjectIdentity=ObjectIdentity
rIp=_RIp_ObjectIdentity((1,3,6,1,4,1,43,45,1,1,3,1))
_IpTooShorts_Type=Counter32
_IpTooShorts_Object=MibScalar
ipTooShorts=_IpTooShorts_Object((1,3,6,1,4,1,43,45,1,1,3,1,1),_IpTooShorts_Type())
ipTooShorts.setMaxAccess(_A)
if mibBuilder.loadTexts:ipTooShorts.setStatus(_B)
_IpTooSmalls_Type=Counter32
_IpTooSmalls_Object=MibScalar
ipTooSmalls=_IpTooSmalls_Object((1,3,6,1,4,1,43,45,1,1,3,1,2),_IpTooSmalls_Type())
ipTooSmalls.setMaxAccess(_A)
if mibBuilder.loadTexts:ipTooSmalls.setStatus(_B)
_IpBadVersions_Type=Counter32
_IpBadVersions_Object=MibScalar
ipBadVersions=_IpBadVersions_Object((1,3,6,1,4,1,43,45,1,1,3,1,3),_IpBadVersions_Type())
ipBadVersions.setMaxAccess(_A)
if mibBuilder.loadTexts:ipBadVersions.setStatus(_B)
_IpBadChecksums_Type=Counter32
_IpBadChecksums_Object=MibScalar
ipBadChecksums=_IpBadChecksums_Object((1,3,6,1,4,1,43,45,1,1,3,1,4),_IpBadChecksums_Type())
ipBadChecksums.setMaxAccess(_A)
if mibBuilder.loadTexts:ipBadChecksums.setStatus(_B)
_IpBadLens_Type=Counter32
_IpBadLens_Object=MibScalar
ipBadLens=_IpBadLens_Object((1,3,6,1,4,1,43,45,1,1,3,1,5),_IpBadLens_Type())
ipBadLens.setMaxAccess(_A)
if mibBuilder.loadTexts:ipBadLens.setStatus(_B)
_IpBadHeadLens_Type=Counter32
_IpBadHeadLens_Object=MibScalar
ipBadHeadLens=_IpBadHeadLens_Object((1,3,6,1,4,1,43,45,1,1,3,1,6),_IpBadHeadLens_Type())
ipBadHeadLens.setMaxAccess(_A)
if mibBuilder.loadTexts:ipBadHeadLens.setStatus(_B)
_IpBadOptions_Type=Counter32
_IpBadOptions_Object=MibScalar
ipBadOptions=_IpBadOptions_Object((1,3,6,1,4,1,43,45,1,1,3,1,7),_IpBadOptions_Type())
ipBadOptions.setMaxAccess(_A)
if mibBuilder.loadTexts:ipBadOptions.setStatus(_B)
_IpFragDroppeds_Type=Counter32
_IpFragDroppeds_Object=MibScalar
ipFragDroppeds=_IpFragDroppeds_Object((1,3,6,1,4,1,43,45,1,1,3,1,8),_IpFragDroppeds_Type())
ipFragDroppeds.setMaxAccess(_A)
if mibBuilder.loadTexts:ipFragDroppeds.setStatus(_B)
_IpRawOuts_Type=Counter32
_IpRawOuts_Object=MibScalar
ipRawOuts=_IpRawOuts_Object((1,3,6,1,4,1,43,45,1,1,3,1,9),_IpRawOuts_Type())
ipRawOuts.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRawOuts.setStatus(_B)
_IpRouteBadRedirects_Type=Counter32
_IpRouteBadRedirects_Object=MibScalar
ipRouteBadRedirects=_IpRouteBadRedirects_Object((1,3,6,1,4,1,43,45,1,1,3,1,10),_IpRouteBadRedirects_Type())
ipRouteBadRedirects.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRouteBadRedirects.setStatus(_B)
_IpRouteDynamics_Type=Counter32
_IpRouteDynamics_Object=MibScalar
ipRouteDynamics=_IpRouteDynamics_Object((1,3,6,1,4,1,43,45,1,1,3,1,11),_IpRouteDynamics_Type())
ipRouteDynamics.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRouteDynamics.setStatus(_B)
_IpRouteNewGateways_Type=Counter32
_IpRouteNewGateways_Object=MibScalar
ipRouteNewGateways=_IpRouteNewGateways_Object((1,3,6,1,4,1,43,45,1,1,3,1,12),_IpRouteNewGateways_Type())
ipRouteNewGateways.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRouteNewGateways.setStatus(_B)
_IpRouteUnreachs_Type=Counter32
_IpRouteUnreachs_Object=MibScalar
ipRouteUnreachs=_IpRouteUnreachs_Object((1,3,6,1,4,1,43,45,1,1,3,1,13),_IpRouteUnreachs_Type())
ipRouteUnreachs.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRouteUnreachs.setStatus(_B)
_IpRouteWilds_Type=Counter32
_IpRouteWilds_Object=MibScalar
ipRouteWilds=_IpRouteWilds_Object((1,3,6,1,4,1,43,45,1,1,3,1,14),_IpRouteWilds_Type())
ipRouteWilds.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRouteWilds.setStatus(_B)
mibBuilder.exportSymbols('A3COM-HUAWEI-IP-MIB',**{'rIp':rIp,'ipTooShorts':ipTooShorts,'ipTooSmalls':ipTooSmalls,'ipBadVersions':ipBadVersions,'ipBadChecksums':ipBadChecksums,'ipBadLens':ipBadLens,'ipBadHeadLens':ipBadHeadLens,'ipBadOptions':ipBadOptions,'ipFragDroppeds':ipFragDroppeds,'ipRawOuts':ipRawOuts,'ipRouteBadRedirects':ipRouteBadRedirects,'ipRouteDynamics':ipRouteDynamics,'ipRouteNewGateways':ipRouteNewGateways,'ipRouteUnreachs':ipRouteUnreachs,'ipRouteWilds':ipRouteWilds})