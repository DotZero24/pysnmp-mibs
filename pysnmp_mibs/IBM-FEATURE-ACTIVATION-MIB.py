_Z='ibmFeatureActivationNotifGroup'
_Y='ibmFeatureActivationBaseGroup'
_X='ibmFodActivationChangeAlert'
_W='ibmFodStatus'
_V='ibmFodFileUri'
_U='ibmFodAction'
_T='keyInProcessOfValidation'
_S='keyUseLimitExceeded'
_R='keyExpired'
_Q='keyFeatureRequiresBMCReboot'
_P='keyFeatureRequiresHostReboot'
_O='keyFeatureActive'
_N='keyValidElsewhere'
_M='keyInvalid'
_L='keyValid'
_K='OctetString'
_J='ibmFodKeyUpdateData'
_I='ibmFodKeyNewStatus'
_H='ibmFodKeyOldStatus'
_G='ibmFodKeyChangeTime'
_F='ibmFodIndex'
_E='read-write'
_D='accessible-for-notify'
_C='Integer32'
_B='current'
_A='IBM-FEATURE-ACTIVATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ibmFeatureActivationMIB=ModuleIdentity((1,3,6,1,4,1,2,5,31))
if mibBuilder.loadTexts:ibmFeatureActivationMIB.setRevisions(('2011-03-30 07:33','2011-02-02 19:49','2010-12-08 18:33'))
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmArchitecture_ObjectIdentity=ObjectIdentity
ibmArchitecture=_IbmArchitecture_ObjectIdentity((1,3,6,1,4,1,2,5))
_IbmFodNotifications_ObjectIdentity=ObjectIdentity
ibmFodNotifications=_IbmFodNotifications_ObjectIdentity((1,3,6,1,4,1,2,5,31,0))
_IbmFodObjects_ObjectIdentity=ObjectIdentity
ibmFodObjects=_IbmFodObjects_ObjectIdentity((1,3,6,1,4,1,2,5,31,1))
class _IbmFodAction_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('installActivationKey',1),('uninstallActivationKey',2),('exportActivationKey',3),('inventoryInstalledActivationKeys',4)))
_IbmFodAction_Type.__name__=_C
_IbmFodAction_Object=MibScalar
ibmFodAction=_IbmFodAction_Object((1,3,6,1,4,1,2,5,31,1,1),_IbmFodAction_Type())
ibmFodAction.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmFodAction.setStatus(_B)
class _IbmFodIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IbmFodIndex_Type.__name__=_C
_IbmFodIndex_Object=MibScalar
ibmFodIndex=_IbmFodIndex_Object((1,3,6,1,4,1,2,5,31,1,2),_IbmFodIndex_Type())
ibmFodIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmFodIndex.setStatus(_B)
class _IbmFodFileUri_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_IbmFodFileUri_Type.__name__=_K
_IbmFodFileUri_Object=MibScalar
ibmFodFileUri=_IbmFodFileUri_Object((1,3,6,1,4,1,2,5,31,1,3),_IbmFodFileUri_Type())
ibmFodFileUri.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmFodFileUri.setStatus(_B)
class _IbmFodStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('success',1),('rebootRequired',2),('versionMismatch',3),('corruptKeyFile',4),('invalideKeyFileTarget',5),('keyFileNotPresent',6),('communicationFailure',7),('keyStoreFull',8),('ftpServerFull',9),('userAuthenticationFailed',10),('invalidIndex',11),('protocolNotSupported',12),('preRequisiteKeyActionRequired',13),('actionIncompleteDeviceBusy',14),('fileAlreadyExists',15),('permissionProblem',16)))
_IbmFodStatus_Type.__name__=_C
_IbmFodStatus_Object=MibScalar
ibmFodStatus=_IbmFodStatus_Object((1,3,6,1,4,1,2,5,31,1,4),_IbmFodStatus_Type())
ibmFodStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:ibmFodStatus.setStatus(_B)
_IbmFodKeyChangeTime_Type=DateAndTime
_IbmFodKeyChangeTime_Object=MibScalar
ibmFodKeyChangeTime=_IbmFodKeyChangeTime_Object((1,3,6,1,4,1,2,5,31,1,5),_IbmFodKeyChangeTime_Type())
ibmFodKeyChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ibmFodKeyChangeTime.setStatus(_B)
class _IbmFodKeyOldStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('noPreviousStatus',1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8),(_S,9),(_T,10)))
_IbmFodKeyOldStatus_Type.__name__=_C
_IbmFodKeyOldStatus_Object=MibScalar
ibmFodKeyOldStatus=_IbmFodKeyOldStatus_Object((1,3,6,1,4,1,2,5,31,1,6),_IbmFodKeyOldStatus_Type())
ibmFodKeyOldStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ibmFodKeyOldStatus.setStatus(_B)
class _IbmFodKeyNewStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('keyRemoved',1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8),(_S,9),(_T,10),('keyReplaced',11)))
_IbmFodKeyNewStatus_Type.__name__=_C
_IbmFodKeyNewStatus_Object=MibScalar
ibmFodKeyNewStatus=_IbmFodKeyNewStatus_Object((1,3,6,1,4,1,2,5,31,1,7),_IbmFodKeyNewStatus_Type())
ibmFodKeyNewStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ibmFodKeyNewStatus.setStatus(_B)
_IbmFodKeyUpdateData_Type=DisplayString
_IbmFodKeyUpdateData_Object=MibScalar
ibmFodKeyUpdateData=_IbmFodKeyUpdateData_Object((1,3,6,1,4,1,2,5,31,1,8),_IbmFodKeyUpdateData_Type())
ibmFodKeyUpdateData.setMaxAccess(_D)
if mibBuilder.loadTexts:ibmFodKeyUpdateData.setStatus(_B)
_IbmFodConformance_ObjectIdentity=ObjectIdentity
ibmFodConformance=_IbmFodConformance_ObjectIdentity((1,3,6,1,4,1,2,5,31,2))
_IbmFeatureActivationCompliances_ObjectIdentity=ObjectIdentity
ibmFeatureActivationCompliances=_IbmFeatureActivationCompliances_ObjectIdentity((1,3,6,1,4,1,2,5,31,2,1))
_IbmFeatureActivationGroups_ObjectIdentity=ObjectIdentity
ibmFeatureActivationGroups=_IbmFeatureActivationGroups_ObjectIdentity((1,3,6,1,4,1,2,5,31,2,2))
ibmFeatureActivationBaseGroup=ObjectGroup((1,3,6,1,4,1,2,5,31,2,2,1))
ibmFeatureActivationBaseGroup.setObjects(*((_A,_U),(_A,_F),(_A,_V),(_A,_W),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ibmFeatureActivationBaseGroup.setStatus(_B)
ibmFodActivationChangeAlert=NotificationType((1,3,6,1,4,1,2,5,31,0,1))
ibmFodActivationChangeAlert.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ibmFodActivationChangeAlert.setStatus(_B)
ibmFeatureActivationNotifGroup=NotificationGroup((1,3,6,1,4,1,2,5,31,2,2,2))
ibmFeatureActivationNotifGroup.setObjects((_A,_X))
if mibBuilder.loadTexts:ibmFeatureActivationNotifGroup.setStatus(_B)
ibmFeatureActivationCompliance=ModuleCompliance((1,3,6,1,4,1,2,5,31,2,1,1))
ibmFeatureActivationCompliance.setObjects(*((_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ibmFeatureActivationCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ibm':ibm,'ibmArchitecture':ibmArchitecture,'ibmFeatureActivationMIB':ibmFeatureActivationMIB,'ibmFodNotifications':ibmFodNotifications,_X:ibmFodActivationChangeAlert,'ibmFodObjects':ibmFodObjects,_U:ibmFodAction,_F:ibmFodIndex,_V:ibmFodFileUri,_W:ibmFodStatus,_G:ibmFodKeyChangeTime,_H:ibmFodKeyOldStatus,_I:ibmFodKeyNewStatus,_J:ibmFodKeyUpdateData,'ibmFodConformance':ibmFodConformance,'ibmFeatureActivationCompliances':ibmFeatureActivationCompliances,'ibmFeatureActivationCompliance':ibmFeatureActivationCompliance,'ibmFeatureActivationGroups':ibmFeatureActivationGroups,_Y:ibmFeatureActivationBaseGroup,_Z:ibmFeatureActivationNotifGroup})