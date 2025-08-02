_I='deprecated'
_H='read-write'
_G='accessible-for-notify'
_F='DisplayString'
_E='fsMplsPwNotifStatusStr'
_D='fsMplsPwIndex'
_C='TruthValue'
_B='current'
_A='SUPERMICRO-MPLS-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PwIndexType,=mibBuilder.importSymbols('PW-TC-STD-MIB','PwIndexType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention',_C)
fsMplsNotificationMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,13,10))
if mibBuilder.loadTexts:fsMplsNotificationMIB.setRevisions(('2012-09-05 00:00',))
_FsMplsNotifications_ObjectIdentity=ObjectIdentity
fsMplsNotifications=_FsMplsNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,10,0))
class _FsMplsPwNotifStatusStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_FsMplsPwNotifStatusStr_Type.__name__=_F
_FsMplsPwNotifStatusStr_Object=MibScalar
fsMplsPwNotifStatusStr=_FsMplsPwNotifStatusStr_Object((1,3,6,1,4,1,10876,101,1,13,10,0,1),_FsMplsPwNotifStatusStr_Type())
fsMplsPwNotifStatusStr.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMplsPwNotifStatusStr.setStatus(_B)
_FsMplsPwIndex_Type=PwIndexType
_FsMplsPwIndex_Object=MibScalar
fsMplsPwIndex=_FsMplsPwIndex_Object((1,3,6,1,4,1,10876,101,1,13,10,0,2),_FsMplsPwIndex_Type())
fsMplsPwIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMplsPwIndex.setStatus(_B)
_FsMplsNotifConfig_ObjectIdentity=ObjectIdentity
fsMplsNotifConfig=_FsMplsNotifConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,10,1))
class _FsMplsPwStatusNotifEnable_Type(TruthValue):defaultValue=2
_FsMplsPwStatusNotifEnable_Type.__name__=_C
_FsMplsPwStatusNotifEnable_Object=MibScalar
fsMplsPwStatusNotifEnable=_FsMplsPwStatusNotifEnable_Object((1,3,6,1,4,1,10876,101,1,13,10,1,1),_FsMplsPwStatusNotifEnable_Type())
fsMplsPwStatusNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMplsPwStatusNotifEnable.setStatus(_B)
class _FsMplsPwOAMStatusNotifEnable_Type(TruthValue):defaultValue=2
_FsMplsPwOAMStatusNotifEnable_Type.__name__=_C
_FsMplsPwOAMStatusNotifEnable_Object=MibScalar
fsMplsPwOAMStatusNotifEnable=_FsMplsPwOAMStatusNotifEnable_Object((1,3,6,1,4,1,10876,101,1,13,10,1,2),_FsMplsPwOAMStatusNotifEnable_Type())
fsMplsPwOAMStatusNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMplsPwOAMStatusNotifEnable.setStatus(_I)
fsMplsPwOamStatus=NotificationType((1,3,6,1,4,1,10876,101,1,13,10,0,3))
fsMplsPwOamStatus.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:fsMplsPwOamStatus.setStatus(_I)
fsMplsPwStatus=NotificationType((1,3,6,1,4,1,10876,101,1,13,10,0,4))
fsMplsPwStatus.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:fsMplsPwStatus.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsMplsNotificationMIB':fsMplsNotificationMIB,'fsMplsNotifications':fsMplsNotifications,_E:fsMplsPwNotifStatusStr,_D:fsMplsPwIndex,'fsMplsPwOamStatus':fsMplsPwOamStatus,'fsMplsPwStatus':fsMplsPwStatus,'fsMplsNotifConfig':fsMplsNotifConfig,'fsMplsPwStatusNotifEnable':fsMplsPwStatusNotifEnable,'fsMplsPwOAMStatusNotifEnable':fsMplsPwOAMStatusNotifEnable})