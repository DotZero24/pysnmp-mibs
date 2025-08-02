_G='current'
_F='rldot1dStpTrapVrblifIndex'
_E='rndErrorSeverity'
_D='rndErrorDesc'
_C='rldot1dStpTrapVrblVID'
_B='RADLAN-BRIDGEMIBOBJECTS-MIB'
_A='RADLAN-DEVICEPARAMS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
rldot1dStpTrapVrblVID,rldot1dStpTrapVrblifIndex=mibBuilder.importSymbols(_B,_C,_F)
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_A,_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesNotifications=ModuleIdentity((1,3,6,1,4,1,35265,1,23,0))
if mibBuilder.loadTexts:eltMesNotifications.setRevisions(('2012-07-13 00:00',))
eltdot1dStpTopologyChange=NotificationType((1,3,6,1,4,1,35265,1,23,0,7))
eltdot1dStpTopologyChange.setObjects(*((_A,_D),(_A,_E),(_B,_F),(_B,_C)))
if mibBuilder.loadTexts:eltdot1dStpTopologyChange.setStatus(_G)
eltdot1dStpRootBridgeChange=NotificationType((1,3,6,1,4,1,35265,1,23,0,8))
eltdot1dStpRootBridgeChange.setObjects(*((_A,_D),(_A,_E),(_B,_F),(_B,_C)))
if mibBuilder.loadTexts:eltdot1dStpRootBridgeChange.setStatus(_G)
eltdot1dStpTcProtectionThresholdReached=NotificationType((1,3,6,1,4,1,35265,1,23,0,9))
eltdot1dStpTcProtectionThresholdReached.setObjects(*((_A,_D),(_A,_E),(_B,_C)))
if mibBuilder.loadTexts:eltdot1dStpTcProtectionThresholdReached.setStatus(_G)
mibBuilder.exportSymbols('ELTEX-MES-TRAPS-MIB',**{'eltMesNotifications':eltMesNotifications,'eltdot1dStpTopologyChange':eltdot1dStpTopologyChange,'eltdot1dStpRootBridgeChange':eltdot1dStpRootBridgeChange,'eltdot1dStpTcProtectionThresholdReached':eltdot1dStpTcProtectionThresholdReached})