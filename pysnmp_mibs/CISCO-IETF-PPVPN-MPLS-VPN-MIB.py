_G='cMplsVpnNotificationGroup'
_F='cMplsNumVrfRouteMaxThreshCleared'
_E='mplsVpnVrfPerfCurrNumRoutes'
_D='mplsVpnVrfConfHighRouteThreshold'
_C='CISCO-IETF-PPVPN-MPLS-VPN-MIB'
_B='current'
_A='MPLS-VPN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
mplsVpnVrfConfHighRouteThreshold,mplsVpnVrfPerfCurrNumRoutes=mibBuilder.importSymbols(_A,_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMplsVpnMIB=ModuleIdentity((1,3,6,1,4,1,9,10,999))
if mibBuilder.loadTexts:ciscoMplsVpnMIB.setRevisions(('2003-04-17 12:00',))
_CMplsVpnNotifs_ObjectIdentity=ObjectIdentity
cMplsVpnNotifs=_CMplsVpnNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,999,0))
_CMplsVpnObjects_ObjectIdentity=ObjectIdentity
cMplsVpnObjects=_CMplsVpnObjects_ObjectIdentity((1,3,6,1,4,1,9,10,999,1))
_CMplsVpnConform_ObjectIdentity=ObjectIdentity
cMplsVpnConform=_CMplsVpnConform_ObjectIdentity((1,3,6,1,4,1,9,10,999,2))
_CMplsVpnCompliances_ObjectIdentity=ObjectIdentity
cMplsVpnCompliances=_CMplsVpnCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,999,2,1))
_CMplsVpnGroups_ObjectIdentity=ObjectIdentity
cMplsVpnGroups=_CMplsVpnGroups_ObjectIdentity((1,3,6,1,4,1,9,10,999,2,2))
cMplsNumVrfRouteMaxThreshCleared=NotificationType((1,3,6,1,4,1,9,10,999,0,1))
cMplsNumVrfRouteMaxThreshCleared.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:cMplsNumVrfRouteMaxThreshCleared.setStatus(_B)
cMplsVpnNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,999,2,2,1))
cMplsVpnNotificationGroup.setObjects((_C,_F))
if mibBuilder.loadTexts:cMplsVpnNotificationGroup.setStatus(_B)
cMplsVpnCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,999,2,1,1))
cMplsVpnCompliance.setObjects((_C,_G))
if mibBuilder.loadTexts:cMplsVpnCompliance.setStatus(_B)
mibBuilder.exportSymbols(_C,**{'ciscoMplsVpnMIB':ciscoMplsVpnMIB,'cMplsVpnNotifs':cMplsVpnNotifs,_F:cMplsNumVrfRouteMaxThreshCleared,'cMplsVpnObjects':cMplsVpnObjects,'cMplsVpnConform':cMplsVpnConform,'cMplsVpnCompliances':cMplsVpnCompliances,'cMplsVpnCompliance':cMplsVpnCompliance,'cMplsVpnGroups':cMplsVpnGroups,_G:cMplsVpnNotificationGroup})