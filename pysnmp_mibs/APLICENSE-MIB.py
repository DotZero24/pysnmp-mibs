_j='apLicenseExpirationWarningNotification'
_i='apLicenseNotApproachingCapacityNotification'
_h='apLicenseApproachingCapacityNotification'
_g='apLicenseExpirationWarningDays'
_f='apLicenseExpirationWarningKey'
_e='apLicenseExpirationWarningSnmpIndex'
_d='apLicenseExpirationWarningAcliIndex'
_c='apLicenseDatabaseRegCap'
_b='apLicenseDatabaseRegFeature'
_a='apLicenseAuthFeature'
_Z='apLicenseSLBEndpointCap'
_Y='apLicenseIPsecTunCap'
_X='apLicenseIKEFeature'
_W='apLicensePACFeature'
_V='apLicenseHAFeature'
_U='apLicenseACCTFeature'
_T='apLicenseSAGFeature'
_S='apLicenseLPFeature'
_R='apLicenseACPFeature'
_Q='apLicenseQOSFeature'
_P='apLicenseIWFFeature'
_O='apLicenseH323Feature'
_N='apLicenseMGCPFeature'
_M='apLicenseSIPFeature'
_L='apLicenseExpireDate'
_K='apLicenseBeginDate'
_J='apLicenseInstallDate'
_I='apLicenseCapacity'
_H='apLicenseKey'
_G='apLicenseIndex'
_F='accessible-for-notify'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='APLICENSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
apLicenseModule=ModuleIdentity((1,3,6,1,4,1,9148,3,5))
if mibBuilder.loadTexts:apLicenseModule.setRevisions(('2012-07-16 00:00',))
_ApLicenseMIBObjects_ObjectIdentity=ObjectIdentity
apLicenseMIBObjects=_ApLicenseMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,5,1))
_ApLicenseTable_Object=MibTable
apLicenseTable=_ApLicenseTable_Object((1,3,6,1,4,1,9148,3,5,1,1))
if mibBuilder.loadTexts:apLicenseTable.setStatus(_A)
_ApLicenseEntry_Object=MibTableRow
apLicenseEntry=_ApLicenseEntry_Object((1,3,6,1,4,1,9148,3,5,1,1,1))
apLicenseEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:apLicenseEntry.setStatus(_A)
class _ApLicenseIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApLicenseIndex_Type.__name__=_E
_ApLicenseIndex_Object=MibTableColumn
apLicenseIndex=_ApLicenseIndex_Object((1,3,6,1,4,1,9148,3,5,1,1,1,1),_ApLicenseIndex_Type())
apLicenseIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:apLicenseIndex.setStatus(_A)
class _ApLicenseKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApLicenseKey_Type.__name__=_D
_ApLicenseKey_Object=MibTableColumn
apLicenseKey=_ApLicenseKey_Object((1,3,6,1,4,1,9148,3,5,1,1,1,2),_ApLicenseKey_Type())
apLicenseKey.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseKey.setStatus(_A)
_ApLicenseCapacity_Type=Unsigned32
_ApLicenseCapacity_Object=MibTableColumn
apLicenseCapacity=_ApLicenseCapacity_Object((1,3,6,1,4,1,9148,3,5,1,1,1,3),_ApLicenseCapacity_Type())
apLicenseCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseCapacity.setStatus(_A)
class _ApLicenseInstallDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApLicenseInstallDate_Type.__name__=_D
_ApLicenseInstallDate_Object=MibTableColumn
apLicenseInstallDate=_ApLicenseInstallDate_Object((1,3,6,1,4,1,9148,3,5,1,1,1,4),_ApLicenseInstallDate_Type())
apLicenseInstallDate.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseInstallDate.setStatus(_A)
class _ApLicenseBeginDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApLicenseBeginDate_Type.__name__=_D
_ApLicenseBeginDate_Object=MibTableColumn
apLicenseBeginDate=_ApLicenseBeginDate_Object((1,3,6,1,4,1,9148,3,5,1,1,1,5),_ApLicenseBeginDate_Type())
apLicenseBeginDate.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseBeginDate.setStatus(_A)
class _ApLicenseExpireDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApLicenseExpireDate_Type.__name__=_D
_ApLicenseExpireDate_Object=MibTableColumn
apLicenseExpireDate=_ApLicenseExpireDate_Object((1,3,6,1,4,1,9148,3,5,1,1,1,6),_ApLicenseExpireDate_Type())
apLicenseExpireDate.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseExpireDate.setStatus(_A)
_ApLicenseSIPFeature_Type=TruthValue
_ApLicenseSIPFeature_Object=MibTableColumn
apLicenseSIPFeature=_ApLicenseSIPFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,7),_ApLicenseSIPFeature_Type())
apLicenseSIPFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseSIPFeature.setStatus(_A)
_ApLicenseMGCPFeature_Type=TruthValue
_ApLicenseMGCPFeature_Object=MibTableColumn
apLicenseMGCPFeature=_ApLicenseMGCPFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,8),_ApLicenseMGCPFeature_Type())
apLicenseMGCPFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseMGCPFeature.setStatus(_A)
_ApLicenseH323Feature_Type=TruthValue
_ApLicenseH323Feature_Object=MibTableColumn
apLicenseH323Feature=_ApLicenseH323Feature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,9),_ApLicenseH323Feature_Type())
apLicenseH323Feature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseH323Feature.setStatus(_A)
_ApLicenseIWFFeature_Type=TruthValue
_ApLicenseIWFFeature_Object=MibTableColumn
apLicenseIWFFeature=_ApLicenseIWFFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,10),_ApLicenseIWFFeature_Type())
apLicenseIWFFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseIWFFeature.setStatus(_A)
_ApLicenseQOSFeature_Type=TruthValue
_ApLicenseQOSFeature_Object=MibTableColumn
apLicenseQOSFeature=_ApLicenseQOSFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,11),_ApLicenseQOSFeature_Type())
apLicenseQOSFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseQOSFeature.setStatus(_A)
_ApLicenseACPFeature_Type=TruthValue
_ApLicenseACPFeature_Object=MibTableColumn
apLicenseACPFeature=_ApLicenseACPFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,12),_ApLicenseACPFeature_Type())
apLicenseACPFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseACPFeature.setStatus(_A)
_ApLicenseLPFeature_Type=TruthValue
_ApLicenseLPFeature_Object=MibTableColumn
apLicenseLPFeature=_ApLicenseLPFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,13),_ApLicenseLPFeature_Type())
apLicenseLPFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseLPFeature.setStatus(_A)
_ApLicenseSAGFeature_Type=TruthValue
_ApLicenseSAGFeature_Object=MibTableColumn
apLicenseSAGFeature=_ApLicenseSAGFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,14),_ApLicenseSAGFeature_Type())
apLicenseSAGFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseSAGFeature.setStatus(_A)
_ApLicenseACCTFeature_Type=TruthValue
_ApLicenseACCTFeature_Object=MibTableColumn
apLicenseACCTFeature=_ApLicenseACCTFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,15),_ApLicenseACCTFeature_Type())
apLicenseACCTFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseACCTFeature.setStatus(_A)
_ApLicenseHAFeature_Type=TruthValue
_ApLicenseHAFeature_Object=MibTableColumn
apLicenseHAFeature=_ApLicenseHAFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,16),_ApLicenseHAFeature_Type())
apLicenseHAFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseHAFeature.setStatus(_A)
_ApLicensePACFeature_Type=TruthValue
_ApLicensePACFeature_Object=MibTableColumn
apLicensePACFeature=_ApLicensePACFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,17),_ApLicensePACFeature_Type())
apLicensePACFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicensePACFeature.setStatus(_A)
_ApLicenseIKEFeature_Type=TruthValue
_ApLicenseIKEFeature_Object=MibTableColumn
apLicenseIKEFeature=_ApLicenseIKEFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,18),_ApLicenseIKEFeature_Type())
apLicenseIKEFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseIKEFeature.setStatus(_A)
_ApLicenseIPsecTunCap_Type=Unsigned32
_ApLicenseIPsecTunCap_Object=MibTableColumn
apLicenseIPsecTunCap=_ApLicenseIPsecTunCap_Object((1,3,6,1,4,1,9148,3,5,1,1,1,19),_ApLicenseIPsecTunCap_Type())
apLicenseIPsecTunCap.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseIPsecTunCap.setStatus(_A)
_ApLicenseAuthFeature_Type=TruthValue
_ApLicenseAuthFeature_Object=MibTableColumn
apLicenseAuthFeature=_ApLicenseAuthFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,20),_ApLicenseAuthFeature_Type())
apLicenseAuthFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseAuthFeature.setStatus(_A)
_ApLicenseDatabaseRegFeature_Type=TruthValue
_ApLicenseDatabaseRegFeature_Object=MibTableColumn
apLicenseDatabaseRegFeature=_ApLicenseDatabaseRegFeature_Object((1,3,6,1,4,1,9148,3,5,1,1,1,21),_ApLicenseDatabaseRegFeature_Type())
apLicenseDatabaseRegFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseDatabaseRegFeature.setStatus(_A)
_ApLicenseDatabaseRegCap_Type=Unsigned32
_ApLicenseDatabaseRegCap_Object=MibTableColumn
apLicenseDatabaseRegCap=_ApLicenseDatabaseRegCap_Object((1,3,6,1,4,1,9148,3,5,1,1,1,22),_ApLicenseDatabaseRegCap_Type())
apLicenseDatabaseRegCap.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseDatabaseRegCap.setStatus(_A)
_ApLicenseSLBEndpointCap_Type=Unsigned32
_ApLicenseSLBEndpointCap_Object=MibTableColumn
apLicenseSLBEndpointCap=_ApLicenseSLBEndpointCap_Object((1,3,6,1,4,1,9148,3,5,1,1,1,23),_ApLicenseSLBEndpointCap_Type())
apLicenseSLBEndpointCap.setMaxAccess(_C)
if mibBuilder.loadTexts:apLicenseSLBEndpointCap.setStatus(_A)
_ApLicenseNotificationObjects_ObjectIdentity=ObjectIdentity
apLicenseNotificationObjects=_ApLicenseNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,5,2))
class _ApLicenseExpirationWarningAcliIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApLicenseExpirationWarningAcliIndex_Type.__name__=_E
_ApLicenseExpirationWarningAcliIndex_Object=MibScalar
apLicenseExpirationWarningAcliIndex=_ApLicenseExpirationWarningAcliIndex_Object((1,3,6,1,4,1,9148,3,5,2,1),_ApLicenseExpirationWarningAcliIndex_Type())
apLicenseExpirationWarningAcliIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:apLicenseExpirationWarningAcliIndex.setStatus(_A)
class _ApLicenseExpirationWarningSnmpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApLicenseExpirationWarningSnmpIndex_Type.__name__=_E
_ApLicenseExpirationWarningSnmpIndex_Object=MibScalar
apLicenseExpirationWarningSnmpIndex=_ApLicenseExpirationWarningSnmpIndex_Object((1,3,6,1,4,1,9148,3,5,2,2),_ApLicenseExpirationWarningSnmpIndex_Type())
apLicenseExpirationWarningSnmpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:apLicenseExpirationWarningSnmpIndex.setStatus(_A)
class _ApLicenseExpirationWarningKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApLicenseExpirationWarningKey_Type.__name__=_D
_ApLicenseExpirationWarningKey_Object=MibScalar
apLicenseExpirationWarningKey=_ApLicenseExpirationWarningKey_Object((1,3,6,1,4,1,9148,3,5,2,3),_ApLicenseExpirationWarningKey_Type())
apLicenseExpirationWarningKey.setMaxAccess(_F)
if mibBuilder.loadTexts:apLicenseExpirationWarningKey.setStatus(_A)
_ApLicenseExpirationWarningDays_Type=Unsigned32
_ApLicenseExpirationWarningDays_Object=MibScalar
apLicenseExpirationWarningDays=_ApLicenseExpirationWarningDays_Object((1,3,6,1,4,1,9148,3,5,2,4),_ApLicenseExpirationWarningDays_Type())
apLicenseExpirationWarningDays.setMaxAccess(_F)
if mibBuilder.loadTexts:apLicenseExpirationWarningDays.setStatus(_A)
_ApLicenseNotificationPrefix_ObjectIdentity=ObjectIdentity
apLicenseNotificationPrefix=_ApLicenseNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,5,3))
_ApLicenseNotifications_ObjectIdentity=ObjectIdentity
apLicenseNotifications=_ApLicenseNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,5,3,0))
_ApLicenseConformance_ObjectIdentity=ObjectIdentity
apLicenseConformance=_ApLicenseConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,5,4))
_ApLicenseCompliances_ObjectIdentity=ObjectIdentity
apLicenseCompliances=_ApLicenseCompliances_ObjectIdentity((1,3,6,1,4,1,9148,3,5,4,1))
_ApLicenseGroups_ObjectIdentity=ObjectIdentity
apLicenseGroups=_ApLicenseGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,5,4,2))
_ApLicenseNotificationsGroups_ObjectIdentity=ObjectIdentity
apLicenseNotificationsGroups=_ApLicenseNotificationsGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,5,4,3))
apLicenseObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,5,4,2,1))
apLicenseObjectsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:apLicenseObjectsGroup.setStatus(_A)
apLicenseDatabaseRegGroup=ObjectGroup((1,3,6,1,4,1,9148,3,5,4,2,2))
apLicenseDatabaseRegGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:apLicenseDatabaseRegGroup.setStatus(_A)
apLicenseApproachingCapacityNotification=NotificationType((1,3,6,1,4,1,9148,3,5,3,0,1))
if mibBuilder.loadTexts:apLicenseApproachingCapacityNotification.setStatus(_A)
apLicenseNotApproachingCapacityNotification=NotificationType((1,3,6,1,4,1,9148,3,5,3,0,2))
if mibBuilder.loadTexts:apLicenseNotApproachingCapacityNotification.setStatus(_A)
apLicenseExpirationWarningNotification=NotificationType((1,3,6,1,4,1,9148,3,5,3,0,3))
apLicenseExpirationWarningNotification.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:apLicenseExpirationWarningNotification.setStatus(_A)
apLicenseNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,5,4,3,1))
apLicenseNotificationsGroup.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:apLicenseNotificationsGroup.setStatus(_A)
apLicenseExpirationNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,5,4,3,2))
apLicenseExpirationNotificationsGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:apLicenseExpirationNotificationsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'apLicenseModule':apLicenseModule,'apLicenseMIBObjects':apLicenseMIBObjects,'apLicenseTable':apLicenseTable,'apLicenseEntry':apLicenseEntry,_G:apLicenseIndex,_H:apLicenseKey,_I:apLicenseCapacity,_J:apLicenseInstallDate,_K:apLicenseBeginDate,_L:apLicenseExpireDate,_M:apLicenseSIPFeature,_N:apLicenseMGCPFeature,_O:apLicenseH323Feature,_P:apLicenseIWFFeature,_Q:apLicenseQOSFeature,_R:apLicenseACPFeature,_S:apLicenseLPFeature,_T:apLicenseSAGFeature,_U:apLicenseACCTFeature,_V:apLicenseHAFeature,_W:apLicensePACFeature,_X:apLicenseIKEFeature,_Y:apLicenseIPsecTunCap,_a:apLicenseAuthFeature,_b:apLicenseDatabaseRegFeature,_c:apLicenseDatabaseRegCap,_Z:apLicenseSLBEndpointCap,'apLicenseNotificationObjects':apLicenseNotificationObjects,_d:apLicenseExpirationWarningAcliIndex,_e:apLicenseExpirationWarningSnmpIndex,_f:apLicenseExpirationWarningKey,_g:apLicenseExpirationWarningDays,'apLicenseNotificationPrefix':apLicenseNotificationPrefix,'apLicenseNotifications':apLicenseNotifications,_h:apLicenseApproachingCapacityNotification,_i:apLicenseNotApproachingCapacityNotification,_j:apLicenseExpirationWarningNotification,'apLicenseConformance':apLicenseConformance,'apLicenseCompliances':apLicenseCompliances,'apLicenseGroups':apLicenseGroups,'apLicenseObjectsGroup':apLicenseObjectsGroup,'apLicenseDatabaseRegGroup':apLicenseDatabaseRegGroup,'apLicenseNotificationsGroups':apLicenseNotificationsGroups,'apLicenseNotificationsGroup':apLicenseNotificationsGroup,'apLicenseExpirationNotificationsGroup':apLicenseExpirationNotificationsGroup})