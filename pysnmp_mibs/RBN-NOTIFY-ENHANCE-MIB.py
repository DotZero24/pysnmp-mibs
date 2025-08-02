_t='rbnNotifyEnhanceMIBObjectGroup'
_s='rbnNEdsx3LineStatusChange'
_r='rbnNEdsx1LineStatusChange'
_q='rbnNElinkUp'
_p='rbnNElinkDown'
_o='rbnNECardAlarm'
_n='rbnNEentConfigChange'
_m='rbnNEGroupName'
_l='Integer32'
_k='rbnDsx3AlarmSeverity'
_j='rbnDsx3AlarmServiceAffecting'
_i='rbnDsx1AlarmSeverity'
_h='rbnDsx1AlarmServiceAffecting'
_g='rbnCardAlarmType'
_f='rbnCardAlarmSeverity'
_e='rbnCardAlarmServiceAffecting'
_d='rbnCardAlarmProbableCause'
_c='rbnCardAlarmId'
_b='rbnCardAlarmDescription'
_a='rbnCardAlarmDateAndTime'
_Z='dsx3LineStatusLastChange'
_Y='dsx3LineStatus'
_X='dsx1LineStatusLastChange'
_W='dsx1LineStatus'
_V='rbnNECardOp'
_U='rbnNESlot'
_T='DisplayString'
_S='RBN-DS3-MIB'
_R='RBN-DS1-MIB'
_Q='ifSpeed'
_P='ifOperStatus'
_O='ifIndex'
_N='ifHighSpeed'
_M='ifAdminStatus'
_L='DS3-MIB'
_K='DS1-MIB'
_J='rbnNotifyEnhanceMIBNotificationGroup'
_I='rbnNECardName'
_H='accessible-for-notify'
_G='rbnNECircuitId'
_F='sysName'
_E='SNMPv2-MIB'
_D='RBN-CARDMON-MIB'
_C='IF-MIB'
_B='current'
_A='RBN-NOTIFY-ENHANCE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx1LineStatus,dsx1LineStatusLastChange=mibBuilder.importSymbols(_K,_W,_X)
dsx3LineStatus,dsx3LineStatusLastChange=mibBuilder.importSymbols(_L,_Y,_Z)
ifAdminStatus,ifHighSpeed,ifIndex,ifOperStatus,ifSpeed=mibBuilder.importSymbols(_C,_M,_N,_O,_P,_Q)
rbnCardAlarmDateAndTime,rbnCardAlarmDescription,rbnCardAlarmId,rbnCardAlarmProbableCause,rbnCardAlarmServiceAffecting,rbnCardAlarmSeverity,rbnCardAlarmType=mibBuilder.importSymbols(_D,_a,_b,_c,_d,_e,_f,_g)
rbnDsx1AlarmServiceAffecting,rbnDsx1AlarmSeverity=mibBuilder.importSymbols(_R,_h,_i)
rbnDsx3AlarmServiceAffecting,rbnDsx3AlarmSeverity=mibBuilder.importSymbols(_S,_j,_k)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnSlot,=mibBuilder.importSymbols('RBN-TC','RbnSlot')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_l,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_T,'PhysAddress','TextualConvention')
rbnNotifyEnhanceMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,36))
if mibBuilder.loadTexts:rbnNotifyEnhanceMIB.setRevisions(('2009-03-23 17:00','2005-05-09 00:00'))
_RbnNotifyEnhanceMIBNotifications_ObjectIdentity=ObjectIdentity
rbnNotifyEnhanceMIBNotifications=_RbnNotifyEnhanceMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,36,0))
_RbnNotifyEnhanceMIBObjects_ObjectIdentity=ObjectIdentity
rbnNotifyEnhanceMIBObjects=_RbnNotifyEnhanceMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,36,1))
_RbnNEGeneral_ObjectIdentity=ObjectIdentity
rbnNEGeneral=_RbnNEGeneral_ObjectIdentity((1,3,6,1,4,1,2352,2,36,1,1))
_RbnNESlot_Type=RbnSlot
_RbnNESlot_Object=MibScalar
rbnNESlot=_RbnNESlot_Object((1,3,6,1,4,1,2352,2,36,1,1,1),_RbnNESlot_Type())
rbnNESlot.setMaxAccess(_H)
if mibBuilder.loadTexts:rbnNESlot.setStatus(_B)
class _RbnNECardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbnNECardName_Type.__name__=_T
_RbnNECardName_Object=MibScalar
rbnNECardName=_RbnNECardName_Object((1,3,6,1,4,1,2352,2,36,1,1,2),_RbnNECardName_Type())
rbnNECardName.setMaxAccess(_H)
if mibBuilder.loadTexts:rbnNECardName.setStatus(_B)
class _RbnNECardOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('insert',1),('remove',2),('other',3)))
_RbnNECardOp_Type.__name__=_l
_RbnNECardOp_Object=MibScalar
rbnNECardOp=_RbnNECardOp_Object((1,3,6,1,4,1,2352,2,36,1,1,3),_RbnNECardOp_Type())
rbnNECardOp.setMaxAccess(_H)
if mibBuilder.loadTexts:rbnNECardOp.setStatus(_B)
class _RbnNECircuitId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbnNECircuitId_Type.__name__=_T
_RbnNECircuitId_Object=MibScalar
rbnNECircuitId=_RbnNECircuitId_Object((1,3,6,1,4,1,2352,2,36,1,1,4),_RbnNECircuitId_Type())
rbnNECircuitId.setMaxAccess(_H)
if mibBuilder.loadTexts:rbnNECircuitId.setStatus(_B)
_RbnNEGroupName_Type=SnmpAdminString
_RbnNEGroupName_Object=MibScalar
rbnNEGroupName=_RbnNEGroupName_Object((1,3,6,1,4,1,2352,2,36,1,1,5),_RbnNEGroupName_Type())
rbnNEGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:rbnNEGroupName.setStatus(_B)
_RbnNotifyEnhanceMIBConformance_ObjectIdentity=ObjectIdentity
rbnNotifyEnhanceMIBConformance=_RbnNotifyEnhanceMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,36,2))
_RbnNotifyEnhanceMIBGroups_ObjectIdentity=ObjectIdentity
rbnNotifyEnhanceMIBGroups=_RbnNotifyEnhanceMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,36,2,1))
_RbnNotifyEnhanceMIBCompliances_ObjectIdentity=ObjectIdentity
rbnNotifyEnhanceMIBCompliances=_RbnNotifyEnhanceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,36,2,2))
rbnNotifyEnhanceMIBObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,36,2,1,1))
rbnNotifyEnhanceMIBObjectGroup.setObjects(*((_A,_U),(_A,_I),(_A,_V),(_A,_G),(_A,_m)))
if mibBuilder.loadTexts:rbnNotifyEnhanceMIBObjectGroup.setStatus(_B)
rbnNEentConfigChange=NotificationType((1,3,6,1,4,1,2352,2,36,0,1))
rbnNEentConfigChange.setObjects(*((_A,_U),(_A,_I),(_A,_V),(_E,_F)))
if mibBuilder.loadTexts:rbnNEentConfigChange.setStatus(_B)
rbnNECardAlarm=NotificationType((1,3,6,1,4,1,2352,2,36,0,2))
rbnNECardAlarm.setObjects(*((_D,_c),(_D,_g),(_D,_a),(_D,_b),(_D,_d),(_D,_f),(_D,_e),(_A,_I),(_E,_F)))
if mibBuilder.loadTexts:rbnNECardAlarm.setStatus(_B)
rbnNElinkDown=NotificationType((1,3,6,1,4,1,2352,2,36,0,3))
rbnNElinkDown.setObjects(*((_C,_O),(_C,_M),(_C,_P),(_C,_Q),(_C,_N),(_A,_G),(_E,_F)))
if mibBuilder.loadTexts:rbnNElinkDown.setStatus(_B)
rbnNElinkUp=NotificationType((1,3,6,1,4,1,2352,2,36,0,4))
rbnNElinkUp.setObjects(*((_C,_O),(_C,_M),(_C,_P),(_C,_Q),(_C,_N),(_A,_G),(_E,_F)))
if mibBuilder.loadTexts:rbnNElinkUp.setStatus(_B)
rbnNEdsx1LineStatusChange=NotificationType((1,3,6,1,4,1,2352,2,36,0,5))
rbnNEdsx1LineStatusChange.setObjects(*((_K,_W),(_K,_X),(_R,_i),(_R,_h),(_A,_G),(_E,_F)))
if mibBuilder.loadTexts:rbnNEdsx1LineStatusChange.setStatus(_B)
rbnNEdsx3LineStatusChange=NotificationType((1,3,6,1,4,1,2352,2,36,0,6))
rbnNEdsx3LineStatusChange.setObjects(*((_L,_Y),(_L,_Z),(_S,_k),(_S,_j),(_A,_G),(_E,_F)))
if mibBuilder.loadTexts:rbnNEdsx3LineStatusChange.setStatus(_B)
rbnNotifyEnhanceMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,2352,2,36,2,1,2))
rbnNotifyEnhanceMIBNotificationGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:rbnNotifyEnhanceMIBNotificationGroup.setStatus(_B)
rbnNotifyEnhanceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,36,2,2,1))
rbnNotifyEnhanceMIBCompliance.setObjects((_A,_J))
if mibBuilder.loadTexts:rbnNotifyEnhanceMIBCompliance.setStatus('deprecated')
rbnNotifyEnhanceMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,36,2,2,2))
rbnNotifyEnhanceMIBCompliance2.setObjects(*((_A,_t),(_A,_J),(_A,_J)))
if mibBuilder.loadTexts:rbnNotifyEnhanceMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnNotifyEnhanceMIB':rbnNotifyEnhanceMIB,'rbnNotifyEnhanceMIBNotifications':rbnNotifyEnhanceMIBNotifications,_n:rbnNEentConfigChange,_o:rbnNECardAlarm,_p:rbnNElinkDown,_q:rbnNElinkUp,_r:rbnNEdsx1LineStatusChange,_s:rbnNEdsx3LineStatusChange,'rbnNotifyEnhanceMIBObjects':rbnNotifyEnhanceMIBObjects,'rbnNEGeneral':rbnNEGeneral,_U:rbnNESlot,_I:rbnNECardName,_V:rbnNECardOp,_G:rbnNECircuitId,_m:rbnNEGroupName,'rbnNotifyEnhanceMIBConformance':rbnNotifyEnhanceMIBConformance,'rbnNotifyEnhanceMIBGroups':rbnNotifyEnhanceMIBGroups,_t:rbnNotifyEnhanceMIBObjectGroup,_J:rbnNotifyEnhanceMIBNotificationGroup,'rbnNotifyEnhanceMIBCompliances':rbnNotifyEnhanceMIBCompliances,'rbnNotifyEnhanceMIBCompliance':rbnNotifyEnhanceMIBCompliance,'rbnNotifyEnhanceMIBCompliance2':rbnNotifyEnhanceMIBCompliance2})