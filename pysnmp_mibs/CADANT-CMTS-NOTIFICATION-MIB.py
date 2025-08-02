_M='accessible-for-notify'
_L='ifOperStatus'
_K='ifIndex'
_J='ifDescr'
_I='ifAdminStatus'
_H='ipdrInfo'
_G='IF-MIB'
_F='securityInfo'
_E='CADANT-CMTS-NOTIFICATION-MIB'
_D='trapSeverity'
_C='trapCounter'
_B='current'
_A='CADANT-CMTS-EQUIPMENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
trapCounter,trapSeverity=mibBuilder.importSymbols(_A,_C,_D)
cadNotification,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadNotification')
ifAdminStatus,ifDescr,ifIndex,ifOperStatus=mibBuilder.importSymbols(_G,_I,_J,_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cadNotificationMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,6,1))
if mibBuilder.loadTexts:cadNotificationMib.setRevisions(('2015-09-14 00:00','2006-05-03 00:00','2005-09-28 00:00','2003-03-26 00:00','2002-07-24 00:00'))
_CadTrapMibObjects_ObjectIdentity=ObjectIdentity
cadTrapMibObjects=_CadTrapMibObjects_ObjectIdentity((1,3,6,1,4,1,4998,1,1,6,1,1))
_CadTraps_ObjectIdentity=ObjectIdentity
cadTraps=_CadTraps_ObjectIdentity((1,3,6,1,4,1,4998,1,1,6,1,1,0))
_CadTrapsInfo_ObjectIdentity=ObjectIdentity
cadTrapsInfo=_CadTrapsInfo_ObjectIdentity((1,3,6,1,4,1,4998,1,1,6,1,1,1))
_SecurityInfo_Type=DisplayString
_SecurityInfo_Object=MibScalar
securityInfo=_SecurityInfo_Object((1,3,6,1,4,1,4998,1,1,6,1,1,1,1),_SecurityInfo_Type())
securityInfo.setMaxAccess(_M)
if mibBuilder.loadTexts:securityInfo.setStatus(_B)
_IpdrInfo_Type=DisplayString
_IpdrInfo_Object=MibScalar
ipdrInfo=_IpdrInfo_Object((1,3,6,1,4,1,4998,1,1,6,1,1,1,2),_IpdrInfo_Type())
ipdrInfo.setMaxAccess(_M)
if mibBuilder.loadTexts:ipdrInfo.setStatus(_B)
aaaServerUnreachableTrap=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,1))
aaaServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_E,_F)))
if mibBuilder.loadTexts:aaaServerUnreachableTrap.setStatus(_B)
aaaServerGroupUnreachableTrap=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,2))
aaaServerGroupUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_E,_F)))
if mibBuilder.loadTexts:aaaServerGroupUnreachableTrap.setStatus(_B)
aaaServerAuthFailTrap=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,3))
aaaServerAuthFailTrap.setObjects(*((_A,_C),(_A,_D),(_E,_F)))
if mibBuilder.loadTexts:aaaServerAuthFailTrap.setStatus(_B)
secuLocalAuthFailTrap=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,4))
secuLocalAuthFailTrap.setObjects(*((_A,_C),(_A,_D),(_E,_F)))
if mibBuilder.loadTexts:secuLocalAuthFailTrap.setStatus(_B)
secuLineAuthFailTrap=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,5))
secuLineAuthFailTrap.setObjects(*((_A,_C),(_A,_D),(_E,_F)))
if mibBuilder.loadTexts:secuLineAuthFailTrap.setStatus(_B)
rip2AuthFailTrap=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,6))
rip2AuthFailTrap.setObjects(*((_A,_C),(_A,_D),(_E,_F)))
if mibBuilder.loadTexts:rip2AuthFailTrap.setStatus(_B)
cadIpdrNoPrimaryCollector=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,7))
cadIpdrNoPrimaryCollector.setObjects(*((_A,_C),(_A,_D),(_E,_H)))
if mibBuilder.loadTexts:cadIpdrNoPrimaryCollector.setStatus(_B)
cadIpdrStreamingDisabled=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,8))
cadIpdrStreamingDisabled.setObjects(*((_A,_C),(_A,_D),(_E,_H)))
if mibBuilder.loadTexts:cadIpdrStreamingDisabled.setStatus(_B)
cadIpdrReportCycleMissed=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,9))
cadIpdrReportCycleMissed.setObjects(*((_A,_C),(_A,_D),(_E,_H)))
if mibBuilder.loadTexts:cadIpdrReportCycleMissed.setStatus(_B)
cadLinkUp=NotificationType((1,3,6,1,4,1,4998,1,1,6,1,1,0,10))
cadLinkUp.setObjects(*((_G,_K),(_G,_I),(_G,_L),(_G,_J)))
if mibBuilder.loadTexts:cadLinkUp.setStatus(_B)
mibBuilder.exportSymbols(_E,**{'cadNotificationMib':cadNotificationMib,'cadTrapMibObjects':cadTrapMibObjects,'cadTraps':cadTraps,'aaaServerUnreachableTrap':aaaServerUnreachableTrap,'aaaServerGroupUnreachableTrap':aaaServerGroupUnreachableTrap,'aaaServerAuthFailTrap':aaaServerAuthFailTrap,'secuLocalAuthFailTrap':secuLocalAuthFailTrap,'secuLineAuthFailTrap':secuLineAuthFailTrap,'rip2AuthFailTrap':rip2AuthFailTrap,'cadIpdrNoPrimaryCollector':cadIpdrNoPrimaryCollector,'cadIpdrStreamingDisabled':cadIpdrStreamingDisabled,'cadIpdrReportCycleMissed':cadIpdrReportCycleMissed,'cadLinkUp':cadLinkUp,'cadTrapsInfo':cadTrapsInfo,_F:securityInfo,_H:ipdrInfo})