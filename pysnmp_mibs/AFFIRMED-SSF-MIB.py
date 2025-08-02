_I='OctetString'
_H='read-only'
_G='affirmedSsfAlarmDetails'
_F='affirmedSsfAlarmSeverity'
_E='affirmedSsfAlarmResource'
_D='affirmedSsfAlarmDateTime'
_C='affirmedSsfAlarmSeqId'
_B='current'
_A='AFFIRMED-SSF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
affirmedSsf=ModuleIdentity((1,3,6,1,4,1,37963,7))
if mibBuilder.loadTexts:affirmedSsf.setRevisions(('2020-01-14 00:00','2019-07-16 00:00','2019-05-20 00:00','2019-04-15 00:00','2019-04-11 00:00','2019-01-15 00:00','2018-10-23 00:00','2018-09-26 00:00','2018-07-31 00:00','2018-04-30 00:00','2017-10-23 00:00'))
_AffirmedSsfTc_ObjectIdentity=ObjectIdentity
affirmedSsfTc=_AffirmedSsfTc_ObjectIdentity((1,3,6,1,4,1,37963,7,1))
_AffirmedSsfObjects_ObjectIdentity=ObjectIdentity
affirmedSsfObjects=_AffirmedSsfObjects_ObjectIdentity((1,3,6,1,4,1,37963,7,2))
_AffirmedSsfAlarmObjects_ObjectIdentity=ObjectIdentity
affirmedSsfAlarmObjects=_AffirmedSsfAlarmObjects_ObjectIdentity((1,3,6,1,4,1,37963,7,2,1))
_AffirmedSsfAlarmSeqId_Type=Integer32
_AffirmedSsfAlarmSeqId_Object=MibScalar
affirmedSsfAlarmSeqId=_AffirmedSsfAlarmSeqId_Object((1,3,6,1,4,1,37963,7,2,1,1),_AffirmedSsfAlarmSeqId_Type())
affirmedSsfAlarmSeqId.setMaxAccess(_H)
if mibBuilder.loadTexts:affirmedSsfAlarmSeqId.setStatus(_B)
class _AffirmedSsfAlarmDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AffirmedSsfAlarmDateTime_Type.__name__=_I
_AffirmedSsfAlarmDateTime_Object=MibScalar
affirmedSsfAlarmDateTime=_AffirmedSsfAlarmDateTime_Object((1,3,6,1,4,1,37963,7,2,1,2),_AffirmedSsfAlarmDateTime_Type())
affirmedSsfAlarmDateTime.setMaxAccess(_H)
if mibBuilder.loadTexts:affirmedSsfAlarmDateTime.setStatus(_B)
class _AffirmedSsfAlarmResource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AffirmedSsfAlarmResource_Type.__name__=_I
_AffirmedSsfAlarmResource_Object=MibScalar
affirmedSsfAlarmResource=_AffirmedSsfAlarmResource_Object((1,3,6,1,4,1,37963,7,2,1,3),_AffirmedSsfAlarmResource_Type())
affirmedSsfAlarmResource.setMaxAccess(_H)
if mibBuilder.loadTexts:affirmedSsfAlarmResource.setStatus(_B)
_AffirmedSsfAlarmSeverity_Type=ItuPerceivedSeverity
_AffirmedSsfAlarmSeverity_Object=MibScalar
affirmedSsfAlarmSeverity=_AffirmedSsfAlarmSeverity_Object((1,3,6,1,4,1,37963,7,2,1,4),_AffirmedSsfAlarmSeverity_Type())
affirmedSsfAlarmSeverity.setMaxAccess(_H)
if mibBuilder.loadTexts:affirmedSsfAlarmSeverity.setStatus(_B)
class _AffirmedSsfAlarmDetails_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AffirmedSsfAlarmDetails_Type.__name__=_I
_AffirmedSsfAlarmDetails_Object=MibScalar
affirmedSsfAlarmDetails=_AffirmedSsfAlarmDetails_Object((1,3,6,1,4,1,37963,7,2,1,5),_AffirmedSsfAlarmDetails_Type())
affirmedSsfAlarmDetails.setMaxAccess(_H)
if mibBuilder.loadTexts:affirmedSsfAlarmDetails.setStatus(_B)
_AffirmedSsfNotifications_ObjectIdentity=ObjectIdentity
affirmedSsfNotifications=_AffirmedSsfNotifications_ObjectIdentity((1,3,6,1,4,1,37963,7,3))
_AffirmedSsfTraps_ObjectIdentity=ObjectIdentity
affirmedSsfTraps=_AffirmedSsfTraps_ObjectIdentity((1,3,6,1,4,1,37963,7,3,1))
anSsfAlarmDnsServiceReachability=NotificationType((1,3,6,1,4,1,37963,7,3,1,1))
anSsfAlarmDnsServiceReachability.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmDnsServiceReachability.setStatus(_B)
anSsfAlarmGtpPathStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,2))
anSsfAlarmGtpPathStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmGtpPathStatus.setStatus(_B)
anSsfAlarmLdapPeerStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,3))
anSsfAlarmLdapPeerStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmLdapPeerStatus.setStatus(_B)
anSsfAlarmNetworkKeepaliveStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,4))
anSsfAlarmNetworkKeepaliveStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmNetworkKeepaliveStatus.setStatus(_B)
anSsfAlarmLdapDbStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,5))
anSsfAlarmLdapDbStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmLdapDbStatus.setStatus(_B)
anSsfAlarmOperState=NotificationType((1,3,6,1,4,1,37963,7,3,1,6))
anSsfAlarmOperState.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmOperState.setStatus(_B)
anSsfAlarmRestPeerStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,7))
anSsfAlarmRestPeerStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmRestPeerStatus.setStatus(_B)
anSsfAlarmRestDbStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,8))
anSsfAlarmRestDbStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmRestDbStatus.setStatus(_B)
anSsfAlarmPgwGxMapping=NotificationType((1,3,6,1,4,1,37963,7,3,1,9))
anSsfAlarmPgwGxMapping.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmPgwGxMapping.setStatus(_B)
anSsfAlarmDiameterPeerStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,10))
anSsfAlarmDiameterPeerStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmDiameterPeerStatus.setStatus(_B)
anSsfAlarmDiameterDbStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,11))
anSsfAlarmDiameterDbStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmDiameterDbStatus.setStatus(_B)
anSsfAlarmDnsNameError=NotificationType((1,3,6,1,4,1,37963,7,3,1,12))
anSsfAlarmDnsNameError.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmDnsNameError.setStatus(_B)
anSsfAlarmConfigSync=NotificationType((1,3,6,1,4,1,37963,7,3,1,13))
anSsfAlarmConfigSync.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmConfigSync.setStatus(_B)
anSsfAlarmLoginFailure=NotificationType((1,3,6,1,4,1,37963,7,3,1,14))
anSsfAlarmLoginFailure.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmLoginFailure.setStatus(_B)
anSsfAlarmFileSystem=NotificationType((1,3,6,1,4,1,37963,7,3,1,15))
anSsfAlarmFileSystem.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmFileSystem.setStatus(_B)
anSsfAlarmCpu=NotificationType((1,3,6,1,4,1,37963,7,3,1,16))
anSsfAlarmCpu.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmCpu.setStatus(_B)
anSsfAlarmMemory=NotificationType((1,3,6,1,4,1,37963,7,3,1,17))
anSsfAlarmMemory.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmMemory.setStatus(_B)
anSsfAlarmNetworkNextHopStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,18))
anSsfAlarmNetworkNextHopStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmNetworkNextHopStatus.setStatus(_B)
anSsfAlarmNetworkStaticRouteStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,19))
anSsfAlarmNetworkStaticRouteStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmNetworkStaticRouteStatus.setStatus(_B)
anSsfAlarmStatusSync=NotificationType((1,3,6,1,4,1,37963,7,3,1,20))
anSsfAlarmStatusSync.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmStatusSync.setStatus(_B)
anSsfAlarmGatewaySnmpStatus=NotificationType((1,3,6,1,4,1,37963,7,3,1,21))
anSsfAlarmGatewaySnmpStatus.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:anSsfAlarmGatewaySnmpStatus.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'affirmedSsf':affirmedSsf,'affirmedSsfTc':affirmedSsfTc,'affirmedSsfObjects':affirmedSsfObjects,'affirmedSsfAlarmObjects':affirmedSsfAlarmObjects,_C:affirmedSsfAlarmSeqId,_D:affirmedSsfAlarmDateTime,_E:affirmedSsfAlarmResource,_F:affirmedSsfAlarmSeverity,_G:affirmedSsfAlarmDetails,'affirmedSsfNotifications':affirmedSsfNotifications,'affirmedSsfTraps':affirmedSsfTraps,'anSsfAlarmDnsServiceReachability':anSsfAlarmDnsServiceReachability,'anSsfAlarmGtpPathStatus':anSsfAlarmGtpPathStatus,'anSsfAlarmLdapPeerStatus':anSsfAlarmLdapPeerStatus,'anSsfAlarmNetworkKeepaliveStatus':anSsfAlarmNetworkKeepaliveStatus,'anSsfAlarmLdapDbStatus':anSsfAlarmLdapDbStatus,'anSsfAlarmOperState':anSsfAlarmOperState,'anSsfAlarmRestPeerStatus':anSsfAlarmRestPeerStatus,'anSsfAlarmRestDbStatus':anSsfAlarmRestDbStatus,'anSsfAlarmPgwGxMapping':anSsfAlarmPgwGxMapping,'anSsfAlarmDiameterPeerStatus':anSsfAlarmDiameterPeerStatus,'anSsfAlarmDiameterDbStatus':anSsfAlarmDiameterDbStatus,'anSsfAlarmDnsNameError':anSsfAlarmDnsNameError,'anSsfAlarmConfigSync':anSsfAlarmConfigSync,'anSsfAlarmLoginFailure':anSsfAlarmLoginFailure,'anSsfAlarmFileSystem':anSsfAlarmFileSystem,'anSsfAlarmCpu':anSsfAlarmCpu,'anSsfAlarmMemory':anSsfAlarmMemory,'anSsfAlarmNetworkNextHopStatus':anSsfAlarmNetworkNextHopStatus,'anSsfAlarmNetworkStaticRouteStatus':anSsfAlarmNetworkStaticRouteStatus,'anSsfAlarmStatusSync':anSsfAlarmStatusSync,'anSsfAlarmGatewaySnmpStatus':anSsfAlarmGatewaySnmpStatus})