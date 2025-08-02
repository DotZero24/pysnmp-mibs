_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlIpProxyType,MwlOnOffSwitch=mibBuilder.importSymbols('MERU-TC','MwlIpProxyType','MwlOnOffSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwSupportedFeatures=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,14))
_MwSupport_ObjectIdentity=ObjectIdentity
mwSupport=_MwSupport_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,14,1))
_MwSupportChannelDomainCheck_Type=MwlOnOffSwitch
_MwSupportChannelDomainCheck_Object=MibScalar
mwSupportChannelDomainCheck=_MwSupportChannelDomainCheck_Object((1,3,6,1,4,1,15983,1,1,4,14,1,1),_MwSupportChannelDomainCheck_Type())
mwSupportChannelDomainCheck.setMaxAccess(_A)
if mibBuilder.loadTexts:mwSupportChannelDomainCheck.setStatus(_B)
_MwSupportLicensingMgmt_Type=MwlOnOffSwitch
_MwSupportLicensingMgmt_Object=MibScalar
mwSupportLicensingMgmt=_MwSupportLicensingMgmt_Object((1,3,6,1,4,1,15983,1,1,4,14,1,2),_MwSupportLicensingMgmt_Type())
mwSupportLicensingMgmt.setMaxAccess(_A)
if mibBuilder.loadTexts:mwSupportLicensingMgmt.setStatus(_B)
_MwSupportSipProxy_Type=MwlIpProxyType
_MwSupportSipProxy_Object=MibScalar
mwSupportSipProxy=_MwSupportSipProxy_Object((1,3,6,1,4,1,15983,1,1,4,14,1,3),_MwSupportSipProxy_Type())
mwSupportSipProxy.setMaxAccess(_A)
if mibBuilder.loadTexts:mwSupportSipProxy.setStatus(_B)
mibBuilder.exportSymbols('MERU-SUPPORTED-FEATURES-MIB',**{'mwSupportedFeatures':mwSupportedFeatures,'mwSupport':mwSupport,'mwSupportChannelDomainCheck':mwSupportChannelDomainCheck,'mwSupportLicensingMgmt':mwSupportLicensingMgmt,'mwSupportSipProxy':mwSupportSipProxy})