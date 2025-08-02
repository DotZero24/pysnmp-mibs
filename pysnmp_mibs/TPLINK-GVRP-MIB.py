_I='read-only'
_H='enable'
_G='disable'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkGvrpMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,20))
if mibBuilder.loadTexts:tplinkGvrpMIB.setRevisions(('2012-12-06 09:30',))
_TplinkGvrpMIBObjects_ObjectIdentity=ObjectIdentity
tplinkGvrpMIBObjects=_TplinkGvrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,20,1))
_TpGvrpGlobalConfig_ObjectIdentity=ObjectIdentity
tpGvrpGlobalConfig=_TpGvrpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,20,1,1))
class _TpGvrpGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpGvrpGlobalEnable_Type.__name__=_B
_TpGvrpGlobalEnable_Object=MibScalar
tpGvrpGlobalEnable=_TpGvrpGlobalEnable_Object((1,3,6,1,4,1,11863,6,20,1,1,1),_TpGvrpGlobalEnable_Type())
tpGvrpGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGvrpGlobalEnable.setStatus(_A)
_TpGvrpPortConfig_ObjectIdentity=ObjectIdentity
tpGvrpPortConfig=_TpGvrpPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,20,1,2))
_TpGvrpPortTable_Object=MibTable
tpGvrpPortTable=_TpGvrpPortTable_Object((1,3,6,1,4,1,11863,6,20,1,2,1))
if mibBuilder.loadTexts:tpGvrpPortTable.setStatus(_A)
_TpGvrpPortEntry_Object=MibTableRow
tpGvrpPortEntry=_TpGvrpPortEntry_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1))
tpGvrpPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tpGvrpPortEntry.setStatus(_A)
class _TpGvrpPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpGvrpPortNumber_Type.__name__=_D
_TpGvrpPortNumber_Object=MibTableColumn
tpGvrpPortNumber=_TpGvrpPortNumber_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1,1),_TpGvrpPortNumber_Type())
tpGvrpPortNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:tpGvrpPortNumber.setStatus(_A)
class _TpGvrpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpGvrpPortEnable_Type.__name__=_B
_TpGvrpPortEnable_Object=MibTableColumn
tpGvrpPortEnable=_TpGvrpPortEnable_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1,2),_TpGvrpPortEnable_Type())
tpGvrpPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGvrpPortEnable.setStatus(_A)
class _TpGvrpPortRegistration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('fixed',1),('forbidden',2)))
_TpGvrpPortRegistration_Type.__name__=_B
_TpGvrpPortRegistration_Object=MibTableColumn
tpGvrpPortRegistration=_TpGvrpPortRegistration_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1,3),_TpGvrpPortRegistration_Type())
tpGvrpPortRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGvrpPortRegistration.setStatus(_A)
class _TpGvrpLeaveAllTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,30000))
_TpGvrpLeaveAllTimer_Type.__name__=_B
_TpGvrpLeaveAllTimer_Object=MibTableColumn
tpGvrpLeaveAllTimer=_TpGvrpLeaveAllTimer_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1,4),_TpGvrpLeaveAllTimer_Type())
tpGvrpLeaveAllTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGvrpLeaveAllTimer.setStatus(_A)
class _TpGvrpJoinTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1000))
_TpGvrpJoinTimer_Type.__name__=_B
_TpGvrpJoinTimer_Object=MibTableColumn
tpGvrpJoinTimer=_TpGvrpJoinTimer_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1,5),_TpGvrpJoinTimer_Type())
tpGvrpJoinTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGvrpJoinTimer.setStatus(_A)
class _TpGvrpLeaveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3000))
_TpGvrpLeaveTimer_Type.__name__=_B
_TpGvrpLeaveTimer_Object=MibTableColumn
tpGvrpLeaveTimer=_TpGvrpLeaveTimer_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1,6),_TpGvrpLeaveTimer_Type())
tpGvrpLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGvrpLeaveTimer.setStatus(_A)
class _TpGvrpPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpGvrpPortLag_Type.__name__=_D
_TpGvrpPortLag_Object=MibTableColumn
tpGvrpPortLag=_TpGvrpPortLag_Object((1,3,6,1,4,1,11863,6,20,1,2,1,1,7),_TpGvrpPortLag_Type())
tpGvrpPortLag.setMaxAccess(_I)
if mibBuilder.loadTexts:tpGvrpPortLag.setStatus(_A)
_TplinkGvrpNotifications_ObjectIdentity=ObjectIdentity
tplinkGvrpNotifications=_TplinkGvrpNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,20,2))
mibBuilder.exportSymbols('TPLINK-GVRP-MIB',**{'tplinkGvrpMIB':tplinkGvrpMIB,'tplinkGvrpMIBObjects':tplinkGvrpMIBObjects,'tpGvrpGlobalConfig':tpGvrpGlobalConfig,'tpGvrpGlobalEnable':tpGvrpGlobalEnable,'tpGvrpPortConfig':tpGvrpPortConfig,'tpGvrpPortTable':tpGvrpPortTable,'tpGvrpPortEntry':tpGvrpPortEntry,'tpGvrpPortNumber':tpGvrpPortNumber,'tpGvrpPortEnable':tpGvrpPortEnable,'tpGvrpPortRegistration':tpGvrpPortRegistration,'tpGvrpLeaveAllTimer':tpGvrpLeaveAllTimer,'tpGvrpJoinTimer':tpGvrpJoinTimer,'tpGvrpLeaveTimer':tpGvrpLeaveTimer,'tpGvrpPortLag':tpGvrpPortLag,'tplinkGvrpNotifications':tplinkGvrpNotifications})