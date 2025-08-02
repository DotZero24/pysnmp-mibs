_C='bluecoatSgFailoverMessage'
_B='BLUECOAT-SG-FAILOVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bluecoatSGFailoverMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,13))
if mibBuilder.loadTexts:bluecoatSGFailoverMIB.setRevisions(('2011-12-20 03:00',))
class FailoverMessageString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BluecoatSgFailoverMIBObjects_ObjectIdentity=ObjectIdentity
bluecoatSgFailoverMIBObjects=_BluecoatSgFailoverMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,13,1))
_BluecoatSgFailoverValues_ObjectIdentity=ObjectIdentity
bluecoatSgFailoverValues=_BluecoatSgFailoverValues_ObjectIdentity((1,3,6,1,4,1,3417,2,13,1,1))
_BluecoatSgFailoverMessage_Type=FailoverMessageString
_BluecoatSgFailoverMessage_Object=MibScalar
bluecoatSgFailoverMessage=_BluecoatSgFailoverMessage_Object((1,3,6,1,4,1,3417,2,13,1,1,1),_BluecoatSgFailoverMessage_Type())
bluecoatSgFailoverMessage.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:bluecoatSgFailoverMessage.setStatus(_A)
_BluecoatSgFailoverMIBNotifications_ObjectIdentity=ObjectIdentity
bluecoatSgFailoverMIBNotifications=_BluecoatSgFailoverMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,13,2))
_BluecoatSgFailoverMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
bluecoatSgFailoverMIBNotificationsPrefix=_BluecoatSgFailoverMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,13,2,0))
bluecoatSgFailoverTrap=NotificationType((1,3,6,1,4,1,3417,2,13,2,0,1))
bluecoatSgFailoverTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:bluecoatSgFailoverTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FailoverMessageString':FailoverMessageString,'bluecoatSGFailoverMIB':bluecoatSGFailoverMIB,'bluecoatSgFailoverMIBObjects':bluecoatSgFailoverMIBObjects,'bluecoatSgFailoverValues':bluecoatSgFailoverValues,_C:bluecoatSgFailoverMessage,'bluecoatSgFailoverMIBNotifications':bluecoatSgFailoverMIBNotifications,'bluecoatSgFailoverMIBNotificationsPrefix':bluecoatSgFailoverMIBNotificationsPrefix,'bluecoatSgFailoverTrap':bluecoatSgFailoverTrap})