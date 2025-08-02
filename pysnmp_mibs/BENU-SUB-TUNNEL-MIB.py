_J='bWagTunLowThreshold'
_I='bWagTunHighThreshold'
_H='bWagSubLowThreshold'
_G='bWagSubHighThreshold'
_F='read-only'
_E='bWagTunMaxNumOfTunnels'
_D='bWagSubMaxNumOfSubscribers'
_C='accessible-for-notify'
_B='BENU-SUB-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuWAG,=mibBuilder.importSymbols('BENU-WAG-MIB','benuWAG')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
benuWagSubTunMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,2))
if mibBuilder.loadTexts:benuWagSubTunMIB.setRevisions(('2015-11-13 00:00','2015-01-02 00:00','2012-12-12 00:00'))
_BWagSubTunnelMIBNotifications_ObjectIdentity=ObjectIdentity
bWagSubTunnelMIBNotifications=_BWagSubTunnelMIBNotifications_ObjectIdentity((1,3,6,1,4,1,39406,2,1,2,0))
if mibBuilder.loadTexts:bWagSubTunnelMIBNotifications.setStatus(_A)
_BWagSubMIBObjects_ObjectIdentity=ObjectIdentity
bWagSubMIBObjects=_BWagSubMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,2,1))
if mibBuilder.loadTexts:bWagSubMIBObjects.setStatus(_A)
_BWagSubMaxNumOfSubscribers_Type=Unsigned32
_BWagSubMaxNumOfSubscribers_Object=MibScalar
bWagSubMaxNumOfSubscribers=_BWagSubMaxNumOfSubscribers_Object((1,3,6,1,4,1,39406,2,1,2,1,1),_BWagSubMaxNumOfSubscribers_Type())
bWagSubMaxNumOfSubscribers.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagSubMaxNumOfSubscribers.setStatus(_A)
_BWagSubMIBNotifObjects_ObjectIdentity=ObjectIdentity
bWagSubMIBNotifObjects=_BWagSubMIBNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,2,2))
if mibBuilder.loadTexts:bWagSubMIBNotifObjects.setStatus(_A)
_BWagSubHighThreshold_Type=Unsigned32
_BWagSubHighThreshold_Object=MibScalar
bWagSubHighThreshold=_BWagSubHighThreshold_Object((1,3,6,1,4,1,39406,2,1,2,2,1),_BWagSubHighThreshold_Type())
bWagSubHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagSubHighThreshold.setStatus(_A)
_BWagSubLowThreshold_Type=Unsigned32
_BWagSubLowThreshold_Object=MibScalar
bWagSubLowThreshold=_BWagSubLowThreshold_Object((1,3,6,1,4,1,39406,2,1,2,2,2),_BWagSubLowThreshold_Type())
bWagSubLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagSubLowThreshold.setStatus(_A)
_BWagTunnelMIBObjects_ObjectIdentity=ObjectIdentity
bWagTunnelMIBObjects=_BWagTunnelMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,2,3))
if mibBuilder.loadTexts:bWagTunnelMIBObjects.setStatus(_A)
_BWagTunMaxNumOfTunnels_Type=Unsigned32
_BWagTunMaxNumOfTunnels_Object=MibScalar
bWagTunMaxNumOfTunnels=_BWagTunMaxNumOfTunnels_Object((1,3,6,1,4,1,39406,2,1,2,3,1),_BWagTunMaxNumOfTunnels_Type())
bWagTunMaxNumOfTunnels.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagTunMaxNumOfTunnels.setStatus(_A)
_BWagTunnelMIBNotifObjects_ObjectIdentity=ObjectIdentity
bWagTunnelMIBNotifObjects=_BWagTunnelMIBNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,2,4))
if mibBuilder.loadTexts:bWagTunnelMIBNotifObjects.setStatus(_A)
_BWagTunHighThreshold_Type=Unsigned32
_BWagTunHighThreshold_Object=MibScalar
bWagTunHighThreshold=_BWagTunHighThreshold_Object((1,3,6,1,4,1,39406,2,1,2,4,1),_BWagTunHighThreshold_Type())
bWagTunHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagTunHighThreshold.setStatus(_A)
_BWagTunLowThreshold_Type=Unsigned32
_BWagTunLowThreshold_Object=MibScalar
bWagTunLowThreshold=_BWagTunLowThreshold_Object((1,3,6,1,4,1,39406,2,1,2,4,2),_BWagTunLowThreshold_Type())
bWagTunLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagTunLowThreshold.setStatus(_A)
bWagSubHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,2,0,1))
bWagSubHighThresholdReached.setObjects(*((_B,_D),(_B,_G)))
if mibBuilder.loadTexts:bWagSubHighThresholdReached.setStatus(_A)
bWagSubLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,2,0,2))
bWagSubLowThresholdReached.setObjects(*((_B,_D),(_B,_H)))
if mibBuilder.loadTexts:bWagSubLowThresholdReached.setStatus(_A)
bWagTunHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,2,0,3))
bWagTunHighThresholdReached.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:bWagTunHighThresholdReached.setStatus(_A)
bWagTunLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,2,0,4))
bWagTunLowThresholdReached.setObjects(*((_B,_E),(_B,_J)))
if mibBuilder.loadTexts:bWagTunLowThresholdReached.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'benuWagSubTunMIB':benuWagSubTunMIB,'bWagSubTunnelMIBNotifications':bWagSubTunnelMIBNotifications,'bWagSubHighThresholdReached':bWagSubHighThresholdReached,'bWagSubLowThresholdReached':bWagSubLowThresholdReached,'bWagTunHighThresholdReached':bWagTunHighThresholdReached,'bWagTunLowThresholdReached':bWagTunLowThresholdReached,'bWagSubMIBObjects':bWagSubMIBObjects,_D:bWagSubMaxNumOfSubscribers,'bWagSubMIBNotifObjects':bWagSubMIBNotifObjects,_G:bWagSubHighThreshold,_H:bWagSubLowThreshold,'bWagTunnelMIBObjects':bWagTunnelMIBObjects,_E:bWagTunMaxNumOfTunnels,'bWagTunnelMIBNotifObjects':bWagTunnelMIBNotifObjects,_I:bWagTunHighThreshold,_J:bWagTunLowThreshold})