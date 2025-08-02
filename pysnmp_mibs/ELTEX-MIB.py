if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
elt=ModuleIdentity((1,3,6,1,4,1,35265))
if mibBuilder.loadTexts:elt.setRevisions(('2012-12-18 00:00',))
class Percents(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class NetNumber(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class VlanPriority(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EltNotifications_ObjectIdentity=ObjectIdentity
eltNotifications=_EltNotifications_ObjectIdentity((1,3,6,1,4,1,35265,0))
if mibBuilder.loadTexts:eltNotifications.setStatus('current')
_EltMng_ObjectIdentity=ObjectIdentity
eltMng=_EltMng_ObjectIdentity((1,3,6,1,4,1,35265,1))
_EltDevParams_ObjectIdentity=ObjectIdentity
eltDevParams=_EltDevParams_ObjectIdentity((1,3,6,1,4,1,35265,2))
_EltCopy_ObjectIdentity=ObjectIdentity
eltCopy=_EltCopy_ObjectIdentity((1,3,6,1,4,1,35265,3))
_EltIpOspfMtu_ObjectIdentity=ObjectIdentity
eltIpOspfMtu=_EltIpOspfMtu_ObjectIdentity((1,3,6,1,4,1,35265,4))
_EltIpBfd_ObjectIdentity=ObjectIdentity
eltIpBfd=_EltIpBfd_ObjectIdentity((1,3,6,1,4,1,35265,6))
_EltIpUnnumbered_ObjectIdentity=ObjectIdentity
eltIpUnnumbered=_EltIpUnnumbered_ObjectIdentity((1,3,6,1,4,1,35265,7))
_EltDhcp_ObjectIdentity=ObjectIdentity
eltDhcp=_EltDhcp_ObjectIdentity((1,3,6,1,4,1,35265,8))
_EltLinkAgg_ObjectIdentity=ObjectIdentity
eltLinkAgg=_EltLinkAgg_ObjectIdentity((1,3,6,1,4,1,35265,9))
_EltQosTailDropMib_ObjectIdentity=ObjectIdentity
eltQosTailDropMib=_EltQosTailDropMib_ObjectIdentity((1,3,6,1,4,1,35265,12))
_EltTuning_ObjectIdentity=ObjectIdentity
eltTuning=_EltTuning_ObjectIdentity((1,3,6,1,4,1,35265,29))
_EltSwInterfaces_ObjectIdentity=ObjectIdentity
eltSwInterfaces=_EltSwInterfaces_ObjectIdentity((1,3,6,1,4,1,35265,43))
_EltIpMulticast_ObjectIdentity=ObjectIdentity
eltIpMulticast=_EltIpMulticast_ObjectIdentity((1,3,6,1,4,1,35265,46))
_EltPhdTransceiver_ObjectIdentity=ObjectIdentity
eltPhdTransceiver=_EltPhdTransceiver_ObjectIdentity((1,3,6,1,4,1,35265,53))
_EltMacMulticast_ObjectIdentity=ObjectIdentity
eltMacMulticast=_EltMacMulticast_ObjectIdentity((1,3,6,1,4,1,35265,55))
_EltStormCtrl_ObjectIdentity=ObjectIdentity
eltStormCtrl=_EltStormCtrl_ObjectIdentity((1,3,6,1,4,1,35265,77))
_EltRadius_ObjectIdentity=ObjectIdentity
eltRadius=_EltRadius_ObjectIdentity((1,3,6,1,4,1,35265,80))
_EltQosCliMib_ObjectIdentity=ObjectIdentity
eltQosCliMib=_EltQosCliMib_ObjectIdentity((1,3,6,1,4,1,35265,88))
_EltPhy_ObjectIdentity=ObjectIdentity
eltPhy=_EltPhy_ObjectIdentity((1,3,6,1,4,1,35265,90))
_IpSpec_ObjectIdentity=ObjectIdentity
ipSpec=_IpSpec_ObjectIdentity((1,3,6,1,4,1,35265,91))
_Eltdot1x_ObjectIdentity=ObjectIdentity
eltdot1x=_Eltdot1x_ObjectIdentity((1,3,6,1,4,1,35265,95))
_EltBridgeSecurity_ObjectIdentity=ObjectIdentity
eltBridgeSecurity=_EltBridgeSecurity_ObjectIdentity((1,3,6,1,4,1,35265,112))
_EltEndOfMibGroup_ObjectIdentity=ObjectIdentity
eltEndOfMibGroup=_EltEndOfMibGroup_ObjectIdentity((1,3,6,1,4,1,35265,1000))
mibBuilder.exportSymbols('ELTEX-MIB',**{'Percents':Percents,'NetNumber':NetNumber,'VlanPriority':VlanPriority,'elt':elt,'eltNotifications':eltNotifications,'eltMng':eltMng,'eltDevParams':eltDevParams,'eltCopy':eltCopy,'eltIpOspfMtu':eltIpOspfMtu,'eltIpBfd':eltIpBfd,'eltIpUnnumbered':eltIpUnnumbered,'eltDhcp':eltDhcp,'eltLinkAgg':eltLinkAgg,'eltQosTailDropMib':eltQosTailDropMib,'eltTuning':eltTuning,'eltSwInterfaces':eltSwInterfaces,'eltIpMulticast':eltIpMulticast,'eltPhdTransceiver':eltPhdTransceiver,'eltMacMulticast':eltMacMulticast,'eltStormCtrl':eltStormCtrl,'eltRadius':eltRadius,'eltQosCliMib':eltQosCliMib,'eltPhy':eltPhy,'ipSpec':ipSpec,'eltdot1x':eltdot1x,'eltBridgeSecurity':eltBridgeSecurity,'eltEndOfMibGroup':eltEndOfMibGroup})