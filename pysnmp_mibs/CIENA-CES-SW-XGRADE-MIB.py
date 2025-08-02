_J='cienaCesSwXgradeGracefulUpgrade'
_I='cienaCesSwXgradeStatus'
_H='cienaCesSwXgradeOp'
_G='cienaGlobalSeverity'
_F='cienaGlobalMacAddress'
_E='accessible-for-notify'
_D='Integer32'
_C='CIENA-GLOBAL-MIB'
_B='CIENA-CES-SW-XGRADE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_C,_F,_G)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaCesSwXgradeMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,13))
if mibBuilder.loadTexts:cienaCesSwXgradeMIB.setRevisions(('2017-06-07 00:00','2012-07-24 00:00','2010-05-10 00:00'))
_CienaCesSwXgradeMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesSwXgradeMIBObjects=_CienaCesSwXgradeMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,13,1))
_CienaCesSwXgrade_ObjectIdentity=ObjectIdentity
cienaCesSwXgrade=_CienaCesSwXgrade_ObjectIdentity((1,3,6,1,4,1,1271,2,1,13,1,1))
_CienaCesSwXgradeGracefulUpgrade_Type=TruthValue
_CienaCesSwXgradeGracefulUpgrade_Object=MibScalar
cienaCesSwXgradeGracefulUpgrade=_CienaCesSwXgradeGracefulUpgrade_Object((1,3,6,1,4,1,1271,2,1,13,1,1,1),_CienaCesSwXgradeGracefulUpgrade_Type())
cienaCesSwXgradeGracefulUpgrade.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesSwXgradeGracefulUpgrade.setStatus(_A)
class _CienaCesSwXgradeOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',0),('download',1),('install',2),('activate',3),('protect',4),('validate',5),('revert',6),('configure',7),('run',8),('remove',9)))
_CienaCesSwXgradeOp_Type.__name__=_D
_CienaCesSwXgradeOp_Object=MibScalar
cienaCesSwXgradeOp=_CienaCesSwXgradeOp_Object((1,3,6,1,4,1,1271,2,1,13,1,1,2),_CienaCesSwXgradeOp_Type())
cienaCesSwXgradeOp.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesSwXgradeOp.setStatus(_A)
class _CienaCesSwXgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('success',1),('failed',2),('unknown',3),('processing',4),('invalidCfgRule',5),('invalidFileName',6),('fileSystemError',7),('cannotResolveHostName',8),('tftpClientTimeout',9),('tftpServerError',10),('tftpBadTag',11),('tftpBadValue',12),('networkError',13),('platformTypeNotSupported',14),('swMgrBusy',15),('needBackupSw',16),('internalError',17),('fileNotExist',18),('missingAttribute',19),('invalidXgradeOp',20),('noDefaultTftpConfigured',21)))
_CienaCesSwXgradeStatus_Type.__name__=_D
_CienaCesSwXgradeStatus_Object=MibScalar
cienaCesSwXgradeStatus=_CienaCesSwXgradeStatus_Object((1,3,6,1,4,1,1271,2,1,13,1,1,3),_CienaCesSwXgradeStatus_Type())
cienaCesSwXgradeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesSwXgradeStatus.setStatus(_A)
_CienaCesSwXgradeMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesSwXgradeMIBConformance=_CienaCesSwXgradeMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,13,3))
_CienaCesSwXgradeMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesSwXgradeMIBCompliances=_CienaCesSwXgradeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,13,3,1))
_CienaCesSwXgradeMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesSwXgradeMIBGroups=_CienaCesSwXgradeMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,13,3,2))
_CienaCesSwXgradeMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesSwXgradeMIBNotificationPrefix=_CienaCesSwXgradeMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,13))
_CienaCesSwXgradeMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesSwXgradeMIBNotifications=_CienaCesSwXgradeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,13,0))
cienaCesSwXgradeCompletion=NotificationType((1,3,6,1,4,1,1271,2,2,13,0,1))
cienaCesSwXgradeCompletion.setObjects(*((_C,_G),(_C,_F),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cienaCesSwXgradeCompletion.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cienaCesSwXgradeMIB':cienaCesSwXgradeMIB,'cienaCesSwXgradeMIBObjects':cienaCesSwXgradeMIBObjects,'cienaCesSwXgrade':cienaCesSwXgrade,_J:cienaCesSwXgradeGracefulUpgrade,_H:cienaCesSwXgradeOp,_I:cienaCesSwXgradeStatus,'cienaCesSwXgradeMIBConformance':cienaCesSwXgradeMIBConformance,'cienaCesSwXgradeMIBCompliances':cienaCesSwXgradeMIBCompliances,'cienaCesSwXgradeMIBGroups':cienaCesSwXgradeMIBGroups,'cienaCesSwXgradeMIBNotificationPrefix':cienaCesSwXgradeMIBNotificationPrefix,'cienaCesSwXgradeMIBNotifications':cienaCesSwXgradeMIBNotifications,'cienaCesSwXgradeCompletion':cienaCesSwXgradeCompletion})