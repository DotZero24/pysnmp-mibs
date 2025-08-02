_D='tptNgfwNotificationGroup'
_C='tptNgfwNotifySeverity'
_B='TPT-NGFW-REG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_products,tpt_reg=mibBuilder.importSymbols('TIPPINGPOINT-REG-MIB','tpt-products','tpt-reg')
tpt_ngfwMIBs=ModuleIdentity((1,3,6,1,4,1,10734,3,9))
if mibBuilder.loadTexts:tpt_ngfwMIBs.setRevisions(('2016-06-08 17:21','2016-05-25 18:54','2013-01-03 17:39'))
class Severity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('info',7),('debug',8)))
_Tpt_ngfw_family_ObjectIdentity=ObjectIdentity
tpt_ngfw_family=_Tpt_ngfw_family_ObjectIdentity((1,3,6,1,4,1,10734,1,9))
if mibBuilder.loadTexts:tpt_ngfw_family.setStatus(_A)
_Tpt_model_S1020F_ObjectIdentity=ObjectIdentity
tpt_model_S1020F=_Tpt_model_S1020F_ObjectIdentity((1,3,6,1,4,1,10734,1,9,1))
if mibBuilder.loadTexts:tpt_model_S1020F.setStatus(_A)
_Tpt_model_S1050F_ObjectIdentity=ObjectIdentity
tpt_model_S1050F=_Tpt_model_S1050F_ObjectIdentity((1,3,6,1,4,1,10734,1,9,2))
if mibBuilder.loadTexts:tpt_model_S1050F.setStatus(_A)
_Tpt_model_S3010F_ObjectIdentity=ObjectIdentity
tpt_model_S3010F=_Tpt_model_S3010F_ObjectIdentity((1,3,6,1,4,1,10734,1,9,3))
if mibBuilder.loadTexts:tpt_model_S3010F.setStatus(_A)
_Tpt_model_S3020F_ObjectIdentity=ObjectIdentity
tpt_model_S3020F=_Tpt_model_S3020F_ObjectIdentity((1,3,6,1,4,1,10734,1,9,4))
if mibBuilder.loadTexts:tpt_model_S3020F.setStatus(_A)
_Tpt_model_S8005F_ObjectIdentity=ObjectIdentity
tpt_model_S8005F=_Tpt_model_S8005F_ObjectIdentity((1,3,6,1,4,1,10734,1,9,5))
if mibBuilder.loadTexts:tpt_model_S8005F.setStatus(_A)
_Tpt_model_S8010F_ObjectIdentity=ObjectIdentity
tpt_model_S8010F=_Tpt_model_S8010F_ObjectIdentity((1,3,6,1,4,1,10734,1,9,6))
if mibBuilder.loadTexts:tpt_model_S8010F.setStatus(_A)
_Tpt_model_S8020F_ObjectIdentity=ObjectIdentity
tpt_model_S8020F=_Tpt_model_S8020F_ObjectIdentity((1,3,6,1,4,1,10734,1,9,7))
if mibBuilder.loadTexts:tpt_model_S8020F.setStatus(_A)
_Tpt_model_440T_NGFW_ObjectIdentity=ObjectIdentity
tpt_model_440T_NGFW=_Tpt_model_440T_NGFW_ObjectIdentity((1,3,6,1,4,1,10734,1,9,8))
if mibBuilder.loadTexts:tpt_model_440T_NGFW.setStatus(_A)
_Tpt_model_2200T_NGFW_ObjectIdentity=ObjectIdentity
tpt_model_2200T_NGFW=_Tpt_model_2200T_NGFW_ObjectIdentity((1,3,6,1,4,1,10734,1,9,9))
if mibBuilder.loadTexts:tpt_model_2200T_NGFW.setStatus(_A)
_Tpt_model_VTPS_Standard_NGFW_ObjectIdentity=ObjectIdentity
tpt_model_VTPS_Standard_NGFW=_Tpt_model_VTPS_Standard_NGFW_ObjectIdentity((1,3,6,1,4,1,10734,1,9,10))
if mibBuilder.loadTexts:tpt_model_VTPS_Standard_NGFW.setStatus(_A)
_Tpt_model_VTPS_Trial_NGFW_ObjectIdentity=ObjectIdentity
tpt_model_VTPS_Trial_NGFW=_Tpt_model_VTPS_Trial_NGFW_ObjectIdentity((1,3,6,1,4,1,10734,1,9,11))
if mibBuilder.loadTexts:tpt_model_VTPS_Trial_NGFW.setStatus(_A)
_Tpt_ngfw_conf_ObjectIdentity=ObjectIdentity
tpt_ngfw_conf=_Tpt_ngfw_conf_ObjectIdentity((1,3,6,1,4,1,10734,3,9,1))
if mibBuilder.loadTexts:tpt_ngfw_conf.setStatus(_A)
_Tpt_ngfw_groups_ObjectIdentity=ObjectIdentity
tpt_ngfw_groups=_Tpt_ngfw_groups_ObjectIdentity((1,3,6,1,4,1,10734,3,9,1,1))
if mibBuilder.loadTexts:tpt_ngfw_groups.setStatus(_A)
_Tpt_ngfw_compls_ObjectIdentity=ObjectIdentity
tpt_ngfw_compls=_Tpt_ngfw_compls_ObjectIdentity((1,3,6,1,4,1,10734,3,9,1,2))
if mibBuilder.loadTexts:tpt_ngfw_compls.setStatus(_A)
_Tpt_ngfw_objs_ObjectIdentity=ObjectIdentity
tpt_ngfw_objs=_Tpt_ngfw_objs_ObjectIdentity((1,3,6,1,4,1,10734,3,9,2))
if mibBuilder.loadTexts:tpt_ngfw_objs.setStatus(_A)
_Tpt_ngfw_events_ObjectIdentity=ObjectIdentity
tpt_ngfw_events=_Tpt_ngfw_events_ObjectIdentity((1,3,6,1,4,1,10734,3,9,3))
if mibBuilder.loadTexts:tpt_ngfw_events.setStatus(_A)
_Tpt_ngfw_eventsV2_ObjectIdentity=ObjectIdentity
tpt_ngfw_eventsV2=_Tpt_ngfw_eventsV2_ObjectIdentity((1,3,6,1,4,1,10734,3,9,3,0))
if mibBuilder.loadTexts:tpt_ngfw_eventsV2.setStatus(_A)
_Tpt_ngfw_params_ObjectIdentity=ObjectIdentity
tpt_ngfw_params=_Tpt_ngfw_params_ObjectIdentity((1,3,6,1,4,1,10734,3,9,3,1))
if mibBuilder.loadTexts:tpt_ngfw_params.setStatus(_A)
_TptNgfwNotifySeverity_Type=Severity
_TptNgfwNotifySeverity_Object=MibScalar
tptNgfwNotifySeverity=_TptNgfwNotifySeverity_Object((1,3,6,1,4,1,10734,3,9,3,1,79),_TptNgfwNotifySeverity_Type())
tptNgfwNotifySeverity.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:tptNgfwNotifySeverity.setStatus(_A)
tptNgfwNotificationGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,13))
tptNgfwNotificationGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:tptNgfwNotificationGroup.setStatus(_A)
tptNgfwCompl=ModuleCompliance((1,3,6,1,4,1,10734,3,9,1,2,6))
tptNgfwCompl.setObjects((_B,_D))
if mibBuilder.loadTexts:tptNgfwCompl.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Severity':Severity,'tpt-ngfw-family':tpt_ngfw_family,'tpt-model-S1020F':tpt_model_S1020F,'tpt-model-S1050F':tpt_model_S1050F,'tpt-model-S3010F':tpt_model_S3010F,'tpt-model-S3020F':tpt_model_S3020F,'tpt-model-S8005F':tpt_model_S8005F,'tpt-model-S8010F':tpt_model_S8010F,'tpt-model-S8020F':tpt_model_S8020F,'tpt-model-440T-NGFW':tpt_model_440T_NGFW,'tpt-model-2200T-NGFW':tpt_model_2200T_NGFW,'tpt-model-VTPS-Standard-NGFW':tpt_model_VTPS_Standard_NGFW,'tpt-model-VTPS-Trial-NGFW':tpt_model_VTPS_Trial_NGFW,'tpt-ngfwMIBs':tpt_ngfwMIBs,'tpt-ngfw-conf':tpt_ngfw_conf,'tpt-ngfw-groups':tpt_ngfw_groups,_D:tptNgfwNotificationGroup,'tpt-ngfw-compls':tpt_ngfw_compls,'tptNgfwCompl':tptNgfwCompl,'tpt-ngfw-objs':tpt_ngfw_objs,'tpt-ngfw-events':tpt_ngfw_events,'tpt-ngfw-eventsV2':tpt_ngfw_eventsV2,'tpt-ngfw-params':tpt_ngfw_params,_C:tptNgfwNotifySeverity})