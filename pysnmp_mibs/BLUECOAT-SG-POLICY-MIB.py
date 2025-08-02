_C='devicePolicyMessage'
_B='BLUECOAT-SG-POLICY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
devicePolicyMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,6))
if mibBuilder.loadTexts:devicePolicyMIB.setRevisions(('2007-11-05 03:00','2002-08-28 03:00'))
class PolicyMessageString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevicePolicyMIBObjects_ObjectIdentity=ObjectIdentity
devicePolicyMIBObjects=_DevicePolicyMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,6,1))
_DevicePolicyValues_ObjectIdentity=ObjectIdentity
devicePolicyValues=_DevicePolicyValues_ObjectIdentity((1,3,6,1,4,1,3417,2,6,1,1))
_DevicePolicyMessage_Type=PolicyMessageString
_DevicePolicyMessage_Object=MibScalar
devicePolicyMessage=_DevicePolicyMessage_Object((1,3,6,1,4,1,3417,2,6,1,1,1),_DevicePolicyMessage_Type())
devicePolicyMessage.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:devicePolicyMessage.setStatus(_A)
_DevicePolicyMIBNotifications_ObjectIdentity=ObjectIdentity
devicePolicyMIBNotifications=_DevicePolicyMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,6,2))
_DevicePolicyMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
devicePolicyMIBNotificationsPrefix=_DevicePolicyMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,6,2,0))
devicePolicyTrap=NotificationType((1,3,6,1,4,1,3417,2,6,2,0,1))
devicePolicyTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:devicePolicyTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PolicyMessageString':PolicyMessageString,'devicePolicyMIB':devicePolicyMIB,'devicePolicyMIBObjects':devicePolicyMIBObjects,'devicePolicyValues':devicePolicyValues,_C:devicePolicyMessage,'devicePolicyMIBNotifications':devicePolicyMIBNotifications,'devicePolicyMIBNotificationsPrefix':devicePolicyMIBNotificationsPrefix,'devicePolicyTrap':devicePolicyTrap})