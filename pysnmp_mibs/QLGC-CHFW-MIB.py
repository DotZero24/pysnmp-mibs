_R='qlgcChFwGroup'
_Q='qlgcChFwResetMethod'
_P='qlgcChFwDwldFileName'
_O='qlgcChFwDwldPathName'
_N='qlgcChFwDwldHostPort'
_M='qlgcChFwDwldHostAddr'
_L='qlgcChFwDwldHostAddrType'
_K='qlgcChFwOpRequest'
_J='qlgcChFwOpResult'
_I='obsolete'
_H='AutonomousType'
_G='InetPortNumber'
_F='InetAddressType'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='QLGC-CHFW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_F,_G)
qlogicMgmt,=mibBuilder.importSymbols('QLOGIC-SMI','qlogicMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','zeroDotZero')
AutonomousType,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,_E,'PhysAddress','TextualConvention')
qlgcChangeFirmwareModule=ModuleIdentity((1,3,6,1,4,1,3873,3,1))
if mibBuilder.loadTexts:qlgcChangeFirmwareModule.setRevisions(('2006-01-26 00:00','2005-08-24 00:00','2005-06-17 00:00'))
_QlgcChFwNotifications_ObjectIdentity=ObjectIdentity
qlgcChFwNotifications=_QlgcChFwNotifications_ObjectIdentity((1,3,6,1,4,1,3873,3,1,0))
_QlgcChFwObjects_ObjectIdentity=ObjectIdentity
qlgcChFwObjects=_QlgcChFwObjects_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1))
_QlgcChFwOpTypes_ObjectIdentity=ObjectIdentity
qlgcChFwOpTypes=_QlgcChFwOpTypes_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1))
_QlgcChFwOperDownload_ObjectIdentity=ObjectIdentity
qlgcChFwOperDownload=_QlgcChFwOperDownload_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,1))
if mibBuilder.loadTexts:qlgcChFwOperDownload.setStatus(_A)
_QlgcChFwDwldNoErr_ObjectIdentity=ObjectIdentity
qlgcChFwDwldNoErr=_QlgcChFwDwldNoErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,1,1))
if mibBuilder.loadTexts:qlgcChFwDwldNoErr.setStatus(_A)
_QlgcChFwDwldHostErr_ObjectIdentity=ObjectIdentity
qlgcChFwDwldHostErr=_QlgcChFwDwldHostErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,1,2))
if mibBuilder.loadTexts:qlgcChFwDwldHostErr.setStatus(_I)
_QlgcChFwDwldFileErr_ObjectIdentity=ObjectIdentity
qlgcChFwDwldFileErr=_QlgcChFwDwldFileErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,1,3))
if mibBuilder.loadTexts:qlgcChFwDwldFileErr.setStatus(_I)
_QlgcChFwDwldTftpErr_ObjectIdentity=ObjectIdentity
qlgcChFwDwldTftpErr=_QlgcChFwDwldTftpErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,1,4))
if mibBuilder.loadTexts:qlgcChFwDwldTftpErr.setStatus(_A)
_QlgcChFwOperInstall_ObjectIdentity=ObjectIdentity
qlgcChFwOperInstall=_QlgcChFwOperInstall_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,2))
if mibBuilder.loadTexts:qlgcChFwOperInstall.setStatus(_A)
_QlgcChFwInstallNoErr_ObjectIdentity=ObjectIdentity
qlgcChFwInstallNoErr=_QlgcChFwInstallNoErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,2,1))
if mibBuilder.loadTexts:qlgcChFwInstallNoErr.setStatus(_A)
_QlgcChFwInstallFileErr_ObjectIdentity=ObjectIdentity
qlgcChFwInstallFileErr=_QlgcChFwInstallFileErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,2,2))
if mibBuilder.loadTexts:qlgcChFwInstallFileErr.setStatus(_A)
_QlgcChFwInstallFileNoAdminErr_ObjectIdentity=ObjectIdentity
qlgcChFwInstallFileNoAdminErr=_QlgcChFwInstallFileNoAdminErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,2,3))
if mibBuilder.loadTexts:qlgcChFwInstallFileNoAdminErr.setStatus(_A)
_QlgcChFwOperReset_ObjectIdentity=ObjectIdentity
qlgcChFwOperReset=_QlgcChFwOperReset_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,3))
if mibBuilder.loadTexts:qlgcChFwOperReset.setStatus(_A)
_QlgcChFwResetNoErr_ObjectIdentity=ObjectIdentity
qlgcChFwResetNoErr=_QlgcChFwResetNoErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,3,1))
if mibBuilder.loadTexts:qlgcChFwResetNoErr.setStatus(_A)
_QlgcChFwResetErr_ObjectIdentity=ObjectIdentity
qlgcChFwResetErr=_QlgcChFwResetErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,3,2))
if mibBuilder.loadTexts:qlgcChFwResetErr.setStatus(_A)
_QlgcChFwResetNoAdminErr_ObjectIdentity=ObjectIdentity
qlgcChFwResetNoAdminErr=_QlgcChFwResetNoAdminErr_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,1,3,3))
if mibBuilder.loadTexts:qlgcChFwResetNoAdminErr.setStatus(_A)
_QlgcChFwOpControl_ObjectIdentity=ObjectIdentity
qlgcChFwOpControl=_QlgcChFwOpControl_ObjectIdentity((1,3,6,1,4,1,3873,3,1,1,2))
class _QlgcChFwOpResult_Type(AutonomousType):defaultValue=0,0
_QlgcChFwOpResult_Type.__name__=_H
_QlgcChFwOpResult_Object=MibScalar
qlgcChFwOpResult=_QlgcChFwOpResult_Object((1,3,6,1,4,1,3873,3,1,1,2,1),_QlgcChFwOpResult_Type())
qlgcChFwOpResult.setMaxAccess('read-only')
if mibBuilder.loadTexts:qlgcChFwOpResult.setStatus(_A)
class _QlgcChFwOpRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('downloadOnly',2),('installOnly',3),('resetOnly',4)))
_QlgcChFwOpRequest_Type.__name__=_D
_QlgcChFwOpRequest_Object=MibScalar
qlgcChFwOpRequest=_QlgcChFwOpRequest_Object((1,3,6,1,4,1,3873,3,1,1,2,2),_QlgcChFwOpRequest_Type())
qlgcChFwOpRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:qlgcChFwOpRequest.setStatus(_A)
class _QlgcChFwDwldHostAddrType_Type(InetAddressType):defaultValue=1
_QlgcChFwDwldHostAddrType_Type.__name__=_F
_QlgcChFwDwldHostAddrType_Object=MibScalar
qlgcChFwDwldHostAddrType=_QlgcChFwDwldHostAddrType_Object((1,3,6,1,4,1,3873,3,1,1,2,3),_QlgcChFwDwldHostAddrType_Type())
qlgcChFwDwldHostAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qlgcChFwDwldHostAddrType.setStatus(_A)
_QlgcChFwDwldHostAddr_Type=InetAddress
_QlgcChFwDwldHostAddr_Object=MibScalar
qlgcChFwDwldHostAddr=_QlgcChFwDwldHostAddr_Object((1,3,6,1,4,1,3873,3,1,1,2,4),_QlgcChFwDwldHostAddr_Type())
qlgcChFwDwldHostAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qlgcChFwDwldHostAddr.setStatus(_A)
class _QlgcChFwDwldHostPort_Type(InetPortNumber):defaultValue=69
_QlgcChFwDwldHostPort_Type.__name__=_G
_QlgcChFwDwldHostPort_Object=MibScalar
qlgcChFwDwldHostPort=_QlgcChFwDwldHostPort_Object((1,3,6,1,4,1,3873,3,1,1,2,5),_QlgcChFwDwldHostPort_Type())
qlgcChFwDwldHostPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qlgcChFwDwldHostPort.setStatus(_A)
class _QlgcChFwDwldPathName_Type(DisplayString):defaultValue=OctetString('/');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_QlgcChFwDwldPathName_Type.__name__=_E
_QlgcChFwDwldPathName_Object=MibScalar
qlgcChFwDwldPathName=_QlgcChFwDwldPathName_Object((1,3,6,1,4,1,3873,3,1,1,2,6),_QlgcChFwDwldPathName_Type())
qlgcChFwDwldPathName.setMaxAccess(_C)
if mibBuilder.loadTexts:qlgcChFwDwldPathName.setStatus(_A)
class _QlgcChFwDwldFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_QlgcChFwDwldFileName_Type.__name__=_E
_QlgcChFwDwldFileName_Object=MibScalar
qlgcChFwDwldFileName=_QlgcChFwDwldFileName_Object((1,3,6,1,4,1,3873,3,1,1,2,7),_QlgcChFwDwldFileName_Type())
qlgcChFwDwldFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:qlgcChFwDwldFileName.setStatus(_A)
class _QlgcChFwResetMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),('ndcla',2)))
_QlgcChFwResetMethod_Type.__name__=_D
_QlgcChFwResetMethod_Object=MibScalar
qlgcChFwResetMethod=_QlgcChFwResetMethod_Object((1,3,6,1,4,1,3873,3,1,1,2,8),_QlgcChFwResetMethod_Type())
qlgcChFwResetMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:qlgcChFwResetMethod.setStatus(_A)
_QlgcChFwConformance_ObjectIdentity=ObjectIdentity
qlgcChFwConformance=_QlgcChFwConformance_ObjectIdentity((1,3,6,1,4,1,3873,3,1,2))
_QlgcChFwGroups_ObjectIdentity=ObjectIdentity
qlgcChFwGroups=_QlgcChFwGroups_ObjectIdentity((1,3,6,1,4,1,3873,3,1,2,1))
_QlgcChFwCompliances_ObjectIdentity=ObjectIdentity
qlgcChFwCompliances=_QlgcChFwCompliances_ObjectIdentity((1,3,6,1,4,1,3873,3,1,2,2))
qlgcChFwGroup=ObjectGroup((1,3,6,1,4,1,3873,3,1,2,1,1))
qlgcChFwGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:qlgcChFwGroup.setStatus(_A)
qlgcChFwComplianceV1=ModuleCompliance((1,3,6,1,4,1,3873,3,1,2,2,1))
qlgcChFwComplianceV1.setObjects((_B,_R))
if mibBuilder.loadTexts:qlgcChFwComplianceV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qlgcChangeFirmwareModule':qlgcChangeFirmwareModule,'qlgcChFwNotifications':qlgcChFwNotifications,'qlgcChFwObjects':qlgcChFwObjects,'qlgcChFwOpTypes':qlgcChFwOpTypes,'qlgcChFwOperDownload':qlgcChFwOperDownload,'qlgcChFwDwldNoErr':qlgcChFwDwldNoErr,'qlgcChFwDwldHostErr':qlgcChFwDwldHostErr,'qlgcChFwDwldFileErr':qlgcChFwDwldFileErr,'qlgcChFwDwldTftpErr':qlgcChFwDwldTftpErr,'qlgcChFwOperInstall':qlgcChFwOperInstall,'qlgcChFwInstallNoErr':qlgcChFwInstallNoErr,'qlgcChFwInstallFileErr':qlgcChFwInstallFileErr,'qlgcChFwInstallFileNoAdminErr':qlgcChFwInstallFileNoAdminErr,'qlgcChFwOperReset':qlgcChFwOperReset,'qlgcChFwResetNoErr':qlgcChFwResetNoErr,'qlgcChFwResetErr':qlgcChFwResetErr,'qlgcChFwResetNoAdminErr':qlgcChFwResetNoAdminErr,'qlgcChFwOpControl':qlgcChFwOpControl,_J:qlgcChFwOpResult,_K:qlgcChFwOpRequest,_L:qlgcChFwDwldHostAddrType,_M:qlgcChFwDwldHostAddr,_N:qlgcChFwDwldHostPort,_O:qlgcChFwDwldPathName,_P:qlgcChFwDwldFileName,_Q:qlgcChFwResetMethod,'qlgcChFwConformance':qlgcChFwConformance,'qlgcChFwGroups':qlgcChFwGroups,_R:qlgcChFwGroup,'qlgcChFwCompliances':qlgcChFwCompliances,'qlgcChFwComplianceV1':qlgcChFwComplianceV1})