_A1='facTrapsConformanceGroup'
_A0='facSystemConformanceGroup'
_z='facTrapRaidStatusChange'
_y='facTrapHASyncActivityLow'
_x='facTrapHAStatusChange'
_w='facTrapUserLockout'
_v='facTrapAuthFailureThreshold'
_u='facTrapAuthEventsThreshold'
_t='facTrapRadiusNasThreshold'
_s='facTrapAuthGroupThreshold'
_r='facTrapAuthUsersThreshold'
_q='facFssoUserRemaining'
_p='facFssoUserCount'
_o='facRadiusProxyOutTotal'
_n='facRadiusProxyInTotal'
_m='facAuthFailuresTotal'
_l='facAuthEventsTotal'
_k='facLdapFailures5Mins'
_j='facLdapFailuresTotal'
_i='facLdapLogins5Mins'
_h='facLdapLoginsTotal'
_g='facRadiusAccounting5Mins'
_f='facRadiusAccountingTotal'
_e='facRadiusFailures5Mins'
_d='facRadiusFailuresTotal'
_c='facRadiusLogins5Mins'
_b='facRadiusLoginsTotal'
_a='facUserCertificateCount'
_Z='facRadiusNasCount'
_Y='facFortiTokenRemaining'
_X='facFortiTokenCount'
_W='facAuthGroupCount'
_V='facAuthUserCount'
_U='facSysLogDiskUsage'
_T='facSysMemUsage'
_S='facSysCpuUsage'
_R='facSysVersion'
_Q='facSysModel'
_P='Integer32'
_O='facRaidStatus'
_N='facHaCurrentStatus'
_M='facAuthFailures5Mins'
_L='facAuthEvents5Mins'
_K='facRadiusNasRemaining'
_J='facAuthGroupRemaining'
_I='facAuthUsersRemaining'
_H='sysName'
_G='SNMPv2-MIB'
_F='fnGenTrapMsg'
_E='FORTINET-CORE-MIB'
_D='facSysSerial'
_C='read-only'
_B='current'
_A='FORTINET-FORTIAUTHENTICATOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FnIndex,fnGenTrapMsg,fortinet=mibBuilder.importSymbols(_E,'FnIndex',_F,'fortinet')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fnFortiAuthenticatorMib=ModuleIdentity((1,3,6,1,4,1,12356,113))
if mibBuilder.loadTexts:fnFortiAuthenticatorMib.setRevisions(('2020-04-16 00:00','2019-01-17 00:00','2015-06-08 00:00','2012-11-05 00:00'))
class FacHaState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*(('unknownOrDetermining',1),('clusterPrimary',2),('clusterSecondary',3),('standalonePrimary',4),('loadBalancer',5),('disabled',255)))
_FacTraps_ObjectIdentity=ObjectIdentity
facTraps=_FacTraps_ObjectIdentity((1,3,6,1,4,1,12356,113,0))
_FacSystem_ObjectIdentity=ObjectIdentity
facSystem=_FacSystem_ObjectIdentity((1,3,6,1,4,1,12356,113,1))
_FacSysModel_Type=DisplayString
_FacSysModel_Object=MibScalar
facSysModel=_FacSysModel_Object((1,3,6,1,4,1,12356,113,1,1),_FacSysModel_Type())
facSysModel.setMaxAccess(_C)
if mibBuilder.loadTexts:facSysModel.setStatus(_B)
_FacSysSerial_Type=DisplayString
_FacSysSerial_Object=MibScalar
facSysSerial=_FacSysSerial_Object((1,3,6,1,4,1,12356,113,1,2),_FacSysSerial_Type())
facSysSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:facSysSerial.setStatus(_B)
_FacSysVersion_Type=DisplayString
_FacSysVersion_Object=MibScalar
facSysVersion=_FacSysVersion_Object((1,3,6,1,4,1,12356,113,1,3),_FacSysVersion_Type())
facSysVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:facSysVersion.setStatus(_B)
_FacSysCpuUsage_Type=Gauge32
_FacSysCpuUsage_Object=MibScalar
facSysCpuUsage=_FacSysCpuUsage_Object((1,3,6,1,4,1,12356,113,1,4),_FacSysCpuUsage_Type())
facSysCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:facSysCpuUsage.setStatus(_B)
_FacSysMemUsage_Type=Gauge32
_FacSysMemUsage_Object=MibScalar
facSysMemUsage=_FacSysMemUsage_Object((1,3,6,1,4,1,12356,113,1,5),_FacSysMemUsage_Type())
facSysMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:facSysMemUsage.setStatus(_B)
_FacSysLogDiskUsage_Type=Gauge32
_FacSysLogDiskUsage_Object=MibScalar
facSysLogDiskUsage=_FacSysLogDiskUsage_Object((1,3,6,1,4,1,12356,113,1,6),_FacSysLogDiskUsage_Type())
facSysLogDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:facSysLogDiskUsage.setStatus(_B)
_FacHa_ObjectIdentity=ObjectIdentity
facHa=_FacHa_ObjectIdentity((1,3,6,1,4,1,12356,113,1,201))
_FacHaCurrentStatus_Type=FacHaState
_FacHaCurrentStatus_Object=MibScalar
facHaCurrentStatus=_FacHaCurrentStatus_Object((1,3,6,1,4,1,12356,113,1,201,1),_FacHaCurrentStatus_Type())
facHaCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:facHaCurrentStatus.setStatus(_B)
_FacAuth_ObjectIdentity=ObjectIdentity
facAuth=_FacAuth_ObjectIdentity((1,3,6,1,4,1,12356,113,1,202))
_FacAuthUserCount_Type=FnIndex
_FacAuthUserCount_Object=MibScalar
facAuthUserCount=_FacAuthUserCount_Object((1,3,6,1,4,1,12356,113,1,202,1),_FacAuthUserCount_Type())
facAuthUserCount.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthUserCount.setStatus(_B)
_FacAuthGroupCount_Type=FnIndex
_FacAuthGroupCount_Object=MibScalar
facAuthGroupCount=_FacAuthGroupCount_Object((1,3,6,1,4,1,12356,113,1,202,2),_FacAuthGroupCount_Type())
facAuthGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthGroupCount.setStatus(_B)
_FacFortiTokenCount_Type=FnIndex
_FacFortiTokenCount_Object=MibScalar
facFortiTokenCount=_FacFortiTokenCount_Object((1,3,6,1,4,1,12356,113,1,202,3),_FacFortiTokenCount_Type())
facFortiTokenCount.setMaxAccess(_C)
if mibBuilder.loadTexts:facFortiTokenCount.setStatus(_B)
_FacAuthUsersRemaining_Type=FnIndex
_FacAuthUsersRemaining_Object=MibScalar
facAuthUsersRemaining=_FacAuthUsersRemaining_Object((1,3,6,1,4,1,12356,113,1,202,4),_FacAuthUsersRemaining_Type())
facAuthUsersRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthUsersRemaining.setStatus(_B)
_FacAuthGroupRemaining_Type=FnIndex
_FacAuthGroupRemaining_Object=MibScalar
facAuthGroupRemaining=_FacAuthGroupRemaining_Object((1,3,6,1,4,1,12356,113,1,202,5),_FacAuthGroupRemaining_Type())
facAuthGroupRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthGroupRemaining.setStatus(_B)
_FacFortiTokenRemaining_Type=FnIndex
_FacFortiTokenRemaining_Object=MibScalar
facFortiTokenRemaining=_FacFortiTokenRemaining_Object((1,3,6,1,4,1,12356,113,1,202,6),_FacFortiTokenRemaining_Type())
facFortiTokenRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:facFortiTokenRemaining.setStatus(_B)
_FacRadiusNasCount_Type=FnIndex
_FacRadiusNasCount_Object=MibScalar
facRadiusNasCount=_FacRadiusNasCount_Object((1,3,6,1,4,1,12356,113,1,202,7),_FacRadiusNasCount_Type())
facRadiusNasCount.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusNasCount.setStatus(_B)
_FacRadiusNasRemaining_Type=FnIndex
_FacRadiusNasRemaining_Object=MibScalar
facRadiusNasRemaining=_FacRadiusNasRemaining_Object((1,3,6,1,4,1,12356,113,1,202,8),_FacRadiusNasRemaining_Type())
facRadiusNasRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusNasRemaining.setStatus(_B)
_FacUserCertificateCount_Type=FnIndex
_FacUserCertificateCount_Object=MibScalar
facUserCertificateCount=_FacUserCertificateCount_Object((1,3,6,1,4,1,12356,113,1,202,9),_FacUserCertificateCount_Type())
facUserCertificateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:facUserCertificateCount.setStatus(_B)
_FacRadiusLoginsTotal_Type=FnIndex
_FacRadiusLoginsTotal_Object=MibScalar
facRadiusLoginsTotal=_FacRadiusLoginsTotal_Object((1,3,6,1,4,1,12356,113,1,202,10),_FacRadiusLoginsTotal_Type())
facRadiusLoginsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusLoginsTotal.setStatus(_B)
_FacRadiusLogins5Mins_Type=FnIndex
_FacRadiusLogins5Mins_Object=MibScalar
facRadiusLogins5Mins=_FacRadiusLogins5Mins_Object((1,3,6,1,4,1,12356,113,1,202,11),_FacRadiusLogins5Mins_Type())
facRadiusLogins5Mins.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusLogins5Mins.setStatus(_B)
_FacRadiusFailuresTotal_Type=FnIndex
_FacRadiusFailuresTotal_Object=MibScalar
facRadiusFailuresTotal=_FacRadiusFailuresTotal_Object((1,3,6,1,4,1,12356,113,1,202,12),_FacRadiusFailuresTotal_Type())
facRadiusFailuresTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusFailuresTotal.setStatus(_B)
_FacRadiusFailures5Mins_Type=FnIndex
_FacRadiusFailures5Mins_Object=MibScalar
facRadiusFailures5Mins=_FacRadiusFailures5Mins_Object((1,3,6,1,4,1,12356,113,1,202,13),_FacRadiusFailures5Mins_Type())
facRadiusFailures5Mins.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusFailures5Mins.setStatus(_B)
_FacRadiusAccountingTotal_Type=FnIndex
_FacRadiusAccountingTotal_Object=MibScalar
facRadiusAccountingTotal=_FacRadiusAccountingTotal_Object((1,3,6,1,4,1,12356,113,1,202,14),_FacRadiusAccountingTotal_Type())
facRadiusAccountingTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusAccountingTotal.setStatus(_B)
_FacRadiusAccounting5Mins_Type=FnIndex
_FacRadiusAccounting5Mins_Object=MibScalar
facRadiusAccounting5Mins=_FacRadiusAccounting5Mins_Object((1,3,6,1,4,1,12356,113,1,202,15),_FacRadiusAccounting5Mins_Type())
facRadiusAccounting5Mins.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusAccounting5Mins.setStatus(_B)
_FacLdapLoginsTotal_Type=FnIndex
_FacLdapLoginsTotal_Object=MibScalar
facLdapLoginsTotal=_FacLdapLoginsTotal_Object((1,3,6,1,4,1,12356,113,1,202,16),_FacLdapLoginsTotal_Type())
facLdapLoginsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facLdapLoginsTotal.setStatus(_B)
_FacLdapLogins5Mins_Type=FnIndex
_FacLdapLogins5Mins_Object=MibScalar
facLdapLogins5Mins=_FacLdapLogins5Mins_Object((1,3,6,1,4,1,12356,113,1,202,17),_FacLdapLogins5Mins_Type())
facLdapLogins5Mins.setMaxAccess(_C)
if mibBuilder.loadTexts:facLdapLogins5Mins.setStatus(_B)
_FacLdapFailuresTotal_Type=FnIndex
_FacLdapFailuresTotal_Object=MibScalar
facLdapFailuresTotal=_FacLdapFailuresTotal_Object((1,3,6,1,4,1,12356,113,1,202,18),_FacLdapFailuresTotal_Type())
facLdapFailuresTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facLdapFailuresTotal.setStatus(_B)
_FacLdapFailures5Mins_Type=FnIndex
_FacLdapFailures5Mins_Object=MibScalar
facLdapFailures5Mins=_FacLdapFailures5Mins_Object((1,3,6,1,4,1,12356,113,1,202,19),_FacLdapFailures5Mins_Type())
facLdapFailures5Mins.setMaxAccess(_C)
if mibBuilder.loadTexts:facLdapFailures5Mins.setStatus(_B)
_FacAuthEventsTotal_Type=FnIndex
_FacAuthEventsTotal_Object=MibScalar
facAuthEventsTotal=_FacAuthEventsTotal_Object((1,3,6,1,4,1,12356,113,1,202,20),_FacAuthEventsTotal_Type())
facAuthEventsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthEventsTotal.setStatus(_B)
_FacAuthEvents5Mins_Type=FnIndex
_FacAuthEvents5Mins_Object=MibScalar
facAuthEvents5Mins=_FacAuthEvents5Mins_Object((1,3,6,1,4,1,12356,113,1,202,21),_FacAuthEvents5Mins_Type())
facAuthEvents5Mins.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthEvents5Mins.setStatus(_B)
_FacAuthFailuresTotal_Type=FnIndex
_FacAuthFailuresTotal_Object=MibScalar
facAuthFailuresTotal=_FacAuthFailuresTotal_Object((1,3,6,1,4,1,12356,113,1,202,22),_FacAuthFailuresTotal_Type())
facAuthFailuresTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthFailuresTotal.setStatus(_B)
_FacAuthFailures5Mins_Type=FnIndex
_FacAuthFailures5Mins_Object=MibScalar
facAuthFailures5Mins=_FacAuthFailures5Mins_Object((1,3,6,1,4,1,12356,113,1,202,23),_FacAuthFailures5Mins_Type())
facAuthFailures5Mins.setMaxAccess(_C)
if mibBuilder.loadTexts:facAuthFailures5Mins.setStatus(_B)
_FacRadiusProxyInTotal_Type=FnIndex
_FacRadiusProxyInTotal_Object=MibScalar
facRadiusProxyInTotal=_FacRadiusProxyInTotal_Object((1,3,6,1,4,1,12356,113,1,202,24),_FacRadiusProxyInTotal_Type())
facRadiusProxyInTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusProxyInTotal.setStatus(_B)
_FacRadiusProxyOutTotal_Type=FnIndex
_FacRadiusProxyOutTotal_Object=MibScalar
facRadiusProxyOutTotal=_FacRadiusProxyOutTotal_Object((1,3,6,1,4,1,12356,113,1,202,25),_FacRadiusProxyOutTotal_Type())
facRadiusProxyOutTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:facRadiusProxyOutTotal.setStatus(_B)
_FacFssoUserCount_Type=FnIndex
_FacFssoUserCount_Object=MibScalar
facFssoUserCount=_FacFssoUserCount_Object((1,3,6,1,4,1,12356,113,1,202,26),_FacFssoUserCount_Type())
facFssoUserCount.setMaxAccess(_C)
if mibBuilder.loadTexts:facFssoUserCount.setStatus(_B)
_FacFssoUserRemaining_Type=FnIndex
_FacFssoUserRemaining_Object=MibScalar
facFssoUserRemaining=_FacFssoUserRemaining_Object((1,3,6,1,4,1,12356,113,1,202,27),_FacFssoUserRemaining_Type())
facFssoUserRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:facFssoUserRemaining.setStatus(_B)
class _FacRaidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('none',0),('ok',1),('degraded',2),('failed',3),('initializing',4),('verifying',5),('rebuilding',6)))
_FacRaidStatus_Type.__name__=_P
_FacRaidStatus_Object=MibScalar
facRaidStatus=_FacRaidStatus_Object((1,3,6,1,4,1,12356,113,1,202,28),_FacRaidStatus_Type())
facRaidStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:facRaidStatus.setStatus(_B)
_FacModel_ObjectIdentity=ObjectIdentity
facModel=_FacModel_ObjectIdentity((1,3,6,1,4,1,12356,113,100))
_Facvm_ObjectIdentity=ObjectIdentity
facvm=_Facvm_ObjectIdentity((1,3,6,1,4,1,12356,113,100,101))
_Facvmhv_ObjectIdentity=ObjectIdentity
facvmhv=_Facvmhv_ObjectIdentity((1,3,6,1,4,1,12356,113,100,102))
_Facvmxen_ObjectIdentity=ObjectIdentity
facvmxen=_Facvmxen_ObjectIdentity((1,3,6,1,4,1,12356,113,100,103))
_Facvmkvm_ObjectIdentity=ObjectIdentity
facvmkvm=_Facvmkvm_ObjectIdentity((1,3,6,1,4,1,12356,113,100,104))
_Facdocker_ObjectIdentity=ObjectIdentity
facdocker=_Facdocker_ObjectIdentity((1,3,6,1,4,1,12356,113,100,105))
_Fac2hd_ObjectIdentity=ObjectIdentity
fac2hd=_Fac2hd_ObjectIdentity((1,3,6,1,4,1,12356,113,100,204))
_Fac2he_ObjectIdentity=ObjectIdentity
fac2he=_Fac2he_ObjectIdentity((1,3,6,1,4,1,12356,113,100,205))
_Fac4hc_ObjectIdentity=ObjectIdentity
fac4hc=_Fac4hc_ObjectIdentity((1,3,6,1,4,1,12356,113,100,303))
_Fac4he_ObjectIdentity=ObjectIdentity
fac4he=_Fac4he_ObjectIdentity((1,3,6,1,4,1,12356,113,100,305))
_Fac1kc_ObjectIdentity=ObjectIdentity
fac1kc=_Fac1kc_ObjectIdentity((1,3,6,1,4,1,12356,113,100,403))
_Fac1kd_ObjectIdentity=ObjectIdentity
fac1kd=_Fac1kd_ObjectIdentity((1,3,6,1,4,1,12356,113,100,404))
_Fac2ke_ObjectIdentity=ObjectIdentity
fac2ke=_Fac2ke_ObjectIdentity((1,3,6,1,4,1,12356,113,100,505))
_Fac3kd_ObjectIdentity=ObjectIdentity
fac3kd=_Fac3kd_ObjectIdentity((1,3,6,1,4,1,12356,113,100,604))
_Fac3ke_ObjectIdentity=ObjectIdentity
fac3ke=_Fac3ke_ObjectIdentity((1,3,6,1,4,1,12356,113,100,605))
_Fac3hf_ObjectIdentity=ObjectIdentity
fac3hf=_Fac3hf_ObjectIdentity((1,3,6,1,4,1,12356,113,100,706))
_Fac8hf_ObjectIdentity=ObjectIdentity
fac8hf=_Fac8hf_ObjectIdentity((1,3,6,1,4,1,12356,113,100,806))
_FacMIBConformance_ObjectIdentity=ObjectIdentity
facMIBConformance=_FacMIBConformance_ObjectIdentity((1,3,6,1,4,1,12356,113,600))
facSystemConformanceGroup=ObjectGroup((1,3,6,1,4,1,12356,113,600,1))
facSystemConformanceGroup.setObjects(*((_A,_Q),(_A,_D),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_I),(_A,_J),(_A,_Y),(_A,_Z),(_A,_K),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_L),(_A,_m),(_A,_M),(_A,_N),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_O)))
if mibBuilder.loadTexts:facSystemConformanceGroup.setStatus(_B)
facTrapAuthUsersThreshold=NotificationType((1,3,6,1,4,1,12356,113,0,100))
facTrapAuthUsersThreshold.setObjects(*((_A,_D),(_A,_I)))
if mibBuilder.loadTexts:facTrapAuthUsersThreshold.setStatus(_B)
facTrapAuthGroupThreshold=NotificationType((1,3,6,1,4,1,12356,113,0,101))
facTrapAuthGroupThreshold.setObjects(*((_A,_D),(_A,_J)))
if mibBuilder.loadTexts:facTrapAuthGroupThreshold.setStatus(_B)
facTrapRadiusNasThreshold=NotificationType((1,3,6,1,4,1,12356,113,0,102))
facTrapRadiusNasThreshold.setObjects(*((_A,_D),(_A,_K)))
if mibBuilder.loadTexts:facTrapRadiusNasThreshold.setStatus(_B)
facTrapAuthEventsThreshold=NotificationType((1,3,6,1,4,1,12356,113,0,103))
facTrapAuthEventsThreshold.setObjects(*((_A,_D),(_A,_L)))
if mibBuilder.loadTexts:facTrapAuthEventsThreshold.setStatus(_B)
facTrapAuthFailureThreshold=NotificationType((1,3,6,1,4,1,12356,113,0,104))
facTrapAuthFailureThreshold.setObjects(*((_A,_D),(_A,_M)))
if mibBuilder.loadTexts:facTrapAuthFailureThreshold.setStatus(_B)
facTrapUserLockout=NotificationType((1,3,6,1,4,1,12356,113,0,105))
facTrapUserLockout.setObjects(*((_A,_D),(_G,_H),(_E,_F)))
if mibBuilder.loadTexts:facTrapUserLockout.setStatus(_B)
facTrapHAStatusChange=NotificationType((1,3,6,1,4,1,12356,113,0,106))
facTrapHAStatusChange.setObjects(*((_A,_D),(_G,_H),(_A,_N),(_E,_F)))
if mibBuilder.loadTexts:facTrapHAStatusChange.setStatus(_B)
facTrapHASyncActivityLow=NotificationType((1,3,6,1,4,1,12356,113,0,107))
facTrapHASyncActivityLow.setObjects(*((_A,_D),(_G,_H),(_E,_F)))
if mibBuilder.loadTexts:facTrapHASyncActivityLow.setStatus(_B)
facTrapRaidStatusChange=NotificationType((1,3,6,1,4,1,12356,113,0,108))
facTrapRaidStatusChange.setObjects(*((_A,_D),(_A,_O)))
if mibBuilder.loadTexts:facTrapRaidStatusChange.setStatus(_B)
facTrapsConformanceGroup=NotificationGroup((1,3,6,1,4,1,12356,113,600,2))
facTrapsConformanceGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:facTrapsConformanceGroup.setStatus(_B)
facMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,113,600,100))
facMIBCompliance.setObjects(*((_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:facMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FacHaState':FacHaState,'fnFortiAuthenticatorMib':fnFortiAuthenticatorMib,'facTraps':facTraps,_r:facTrapAuthUsersThreshold,_s:facTrapAuthGroupThreshold,_t:facTrapRadiusNasThreshold,_u:facTrapAuthEventsThreshold,_v:facTrapAuthFailureThreshold,_w:facTrapUserLockout,_x:facTrapHAStatusChange,_y:facTrapHASyncActivityLow,_z:facTrapRaidStatusChange,'facSystem':facSystem,_Q:facSysModel,_D:facSysSerial,_R:facSysVersion,_S:facSysCpuUsage,_T:facSysMemUsage,_U:facSysLogDiskUsage,'facHa':facHa,_N:facHaCurrentStatus,'facAuth':facAuth,_V:facAuthUserCount,_W:facAuthGroupCount,_X:facFortiTokenCount,_I:facAuthUsersRemaining,_J:facAuthGroupRemaining,_Y:facFortiTokenRemaining,_Z:facRadiusNasCount,_K:facRadiusNasRemaining,_a:facUserCertificateCount,_b:facRadiusLoginsTotal,_c:facRadiusLogins5Mins,_d:facRadiusFailuresTotal,_e:facRadiusFailures5Mins,_f:facRadiusAccountingTotal,_g:facRadiusAccounting5Mins,_h:facLdapLoginsTotal,_i:facLdapLogins5Mins,_j:facLdapFailuresTotal,_k:facLdapFailures5Mins,_l:facAuthEventsTotal,_L:facAuthEvents5Mins,_m:facAuthFailuresTotal,_M:facAuthFailures5Mins,_n:facRadiusProxyInTotal,_o:facRadiusProxyOutTotal,_p:facFssoUserCount,_q:facFssoUserRemaining,_O:facRaidStatus,'facModel':facModel,'facvm':facvm,'facvmhv':facvmhv,'facvmxen':facvmxen,'facvmkvm':facvmkvm,'facdocker':facdocker,'fac2hd':fac2hd,'fac2he':fac2he,'fac4hc':fac4hc,'fac4he':fac4he,'fac1kc':fac1kc,'fac1kd':fac1kd,'fac2ke':fac2ke,'fac3kd':fac3kd,'fac3ke':fac3ke,'fac3hf':fac3hf,'fac8hf':fac8hf,'facMIBConformance':facMIBConformance,_A0:facSystemConformanceGroup,_A1:facTrapsConformanceGroup,'facMIBCompliance':facMIBCompliance})