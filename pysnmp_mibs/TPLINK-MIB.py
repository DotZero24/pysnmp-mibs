_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Tplink_ObjectIdentity=ObjectIdentity
tplink=_Tplink_ObjectIdentity((1,3,6,1,4,1,11863))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,11863,1))
_L2manageswitch_ObjectIdentity=ObjectIdentity
l2manageswitch=_L2manageswitch_ObjectIdentity((1,3,6,1,4,1,11863,1,1))
_L3manageswitch_ObjectIdentity=ObjectIdentity
l3manageswitch=_L3manageswitch_ObjectIdentity((1,3,6,1,4,1,11863,1,2))
_Router_ObjectIdentity=ObjectIdentity
router=_Router_ObjectIdentity((1,3,6,1,4,1,11863,2))
_Wireless_ObjectIdentity=ObjectIdentity
wireless=_Wireless_ObjectIdentity((1,3,6,1,4,1,11863,3))
_Adsl_ObjectIdentity=ObjectIdentity
adsl=_Adsl_ObjectIdentity((1,3,6,1,4,1,11863,4))
_TplinkProducts_ObjectIdentity=ObjectIdentity
tplinkProducts=_TplinkProducts_ObjectIdentity((1,3,6,1,4,1,11863,5))
if mibBuilder.loadTexts:tplinkProducts.setStatus(_A)
_TplinkMgmt_ObjectIdentity=ObjectIdentity
tplinkMgmt=_TplinkMgmt_ObjectIdentity((1,3,6,1,4,1,11863,6))
if mibBuilder.loadTexts:tplinkMgmt.setStatus(_A)
_Ap_ObjectIdentity=ObjectIdentity
ap=_Ap_ObjectIdentity((1,3,6,1,4,1,11863,10))
_Eap_ObjectIdentity=ObjectIdentity
eap=_Eap_ObjectIdentity((1,3,6,1,4,1,11863,10,1))
_SystemTools_ObjectIdentity=ObjectIdentity
systemTools=_SystemTools_ObjectIdentity((1,3,6,1,4,1,11863,10,1,2))
mibBuilder.exportSymbols('TPLINK-MIB',**{'tplink':tplink,'switch':switch,'l2manageswitch':l2manageswitch,'l3manageswitch':l3manageswitch,'router':router,'wireless':wireless,'adsl':adsl,'tplinkProducts':tplinkProducts,'tplinkMgmt':tplinkMgmt,'ap':ap,'eap':eap,'systemTools':systemTools})