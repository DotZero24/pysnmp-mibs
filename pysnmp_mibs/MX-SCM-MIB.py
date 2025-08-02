_K='servicesConfigName'
_J='serviceCommandsName'
_I='manual'
_H='servicesInfoName'
_G='OctetString'
_F='noOp'
_E='MX-SCM-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap','MxEnableState','MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
scmMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,400))
_ScmMIBObjects_ObjectIdentity=ObjectIdentity
scmMIBObjects=_ScmMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,400,1))
_ServicesInfoTable_Object=MibTable
servicesInfoTable=_ServicesInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100))
if mibBuilder.loadTexts:servicesInfoTable.setStatus(_A)
_ServicesInfoEntry_Object=MibTableRow
servicesInfoEntry=_ServicesInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100,1))
servicesInfoEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:servicesInfoEntry.setStatus(_A)
_ServicesInfoName_Type=OctetString
_ServicesInfoName_Object=MibTableColumn
servicesInfoName=_ServicesInfoName_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100,1,100),_ServicesInfoName_Type())
servicesInfoName.setMaxAccess(_C)
if mibBuilder.loadTexts:servicesInfoName.setStatus(_A)
_ServicesInfoId_Type=Unsigned32
_ServicesInfoId_Object=MibTableColumn
servicesInfoId=_ServicesInfoId_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100,1,200),_ServicesInfoId_Type())
servicesInfoId.setMaxAccess(_C)
if mibBuilder.loadTexts:servicesInfoId.setStatus(_A)
class _ServicesInfoClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('system',100),('user',200)))
_ServicesInfoClass_Type.__name__=_B
_ServicesInfoClass_Object=MibTableColumn
servicesInfoClass=_ServicesInfoClass_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100,1,400),_ServicesInfoClass_Type())
servicesInfoClass.setMaxAccess(_C)
if mibBuilder.loadTexts:servicesInfoClass.setStatus(_A)
class _ServicesInfoStartupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('auto',100),(_I,200)))
_ServicesInfoStartupType_Type.__name__=_B
_ServicesInfoStartupType_Object=MibTableColumn
servicesInfoStartupType=_ServicesInfoStartupType_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100,1,500),_ServicesInfoStartupType_Type())
servicesInfoStartupType.setMaxAccess(_C)
if mibBuilder.loadTexts:servicesInfoStartupType.setStatus(_A)
class _ServicesInfoExecState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,65000)));namedValues=NamedValues(*(('started',100),('starting',200),('stopped',300),('stopping',400),('notResponding',65000)))
_ServicesInfoExecState_Type.__name__=_B
_ServicesInfoExecState_Object=MibTableColumn
servicesInfoExecState=_ServicesInfoExecState_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100,1,600),_ServicesInfoExecState_Type())
servicesInfoExecState.setMaxAccess(_C)
if mibBuilder.loadTexts:servicesInfoExecState.setStatus(_A)
class _ServicesInfoComment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ServicesInfoComment_Type.__name__=_G
_ServicesInfoComment_Object=MibTableColumn
servicesInfoComment=_ServicesInfoComment_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,100,1,700),_ServicesInfoComment_Type())
servicesInfoComment.setMaxAccess(_C)
if mibBuilder.loadTexts:servicesInfoComment.setStatus(_A)
_ServiceCommandsTable_Object=MibTable
serviceCommandsTable=_ServiceCommandsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,200))
if mibBuilder.loadTexts:serviceCommandsTable.setStatus(_A)
_ServiceCommandsEntry_Object=MibTableRow
serviceCommandsEntry=_ServiceCommandsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,200,1))
serviceCommandsEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:serviceCommandsEntry.setStatus(_A)
_ServiceCommandsName_Type=OctetString
_ServiceCommandsName_Object=MibTableColumn
serviceCommandsName=_ServiceCommandsName_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,200,1,100),_ServiceCommandsName_Type())
serviceCommandsName.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceCommandsName.setStatus(_A)
class _ServiceCommandsRestart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('restart',10)))
_ServiceCommandsRestart_Type.__name__=_B
_ServiceCommandsRestart_Object=MibTableColumn
serviceCommandsRestart=_ServiceCommandsRestart_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,200,1,200),_ServiceCommandsRestart_Type())
serviceCommandsRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:serviceCommandsRestart.setStatus(_A)
class _ServiceCommandsStop_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('stop',10)))
_ServiceCommandsStop_Type.__name__=_B
_ServiceCommandsStop_Object=MibTableColumn
serviceCommandsStop=_ServiceCommandsStop_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,200,1,300),_ServiceCommandsStop_Type())
serviceCommandsStop.setMaxAccess(_D)
if mibBuilder.loadTexts:serviceCommandsStop.setStatus(_A)
class _ServiceCommandsStart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('start',10)))
_ServiceCommandsStart_Type.__name__=_B
_ServiceCommandsStart_Object=MibTableColumn
serviceCommandsStart=_ServiceCommandsStart_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,200,1,400),_ServiceCommandsStart_Type())
serviceCommandsStart.setMaxAccess(_D)
if mibBuilder.loadTexts:serviceCommandsStart.setStatus(_A)
_ServicesConfigTable_Object=MibTable
servicesConfigTable=_ServicesConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,400))
if mibBuilder.loadTexts:servicesConfigTable.setStatus(_A)
_ServicesConfigEntry_Object=MibTableRow
servicesConfigEntry=_ServicesConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,400,1))
servicesConfigEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:servicesConfigEntry.setStatus(_A)
_ServicesConfigName_Type=OctetString
_ServicesConfigName_Object=MibTableColumn
servicesConfigName=_ServicesConfigName_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,400,1,100),_ServicesConfigName_Type())
servicesConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:servicesConfigName.setStatus(_A)
class _ServicesConfigStartupType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('auto',100),(_I,200)))
_ServicesConfigStartupType_Type.__name__=_B
_ServicesConfigStartupType_Object=MibTableColumn
servicesConfigStartupType=_ServicesConfigStartupType_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,400,1,200),_ServicesConfigStartupType_Type())
servicesConfigStartupType.setMaxAccess(_D)
if mibBuilder.loadTexts:servicesConfigStartupType.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,400,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,400,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,400,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'scmMIB':scmMIB,'scmMIBObjects':scmMIBObjects,'servicesInfoTable':servicesInfoTable,'servicesInfoEntry':servicesInfoEntry,_H:servicesInfoName,'servicesInfoId':servicesInfoId,'servicesInfoClass':servicesInfoClass,'servicesInfoStartupType':servicesInfoStartupType,'servicesInfoExecState':servicesInfoExecState,'servicesInfoComment':servicesInfoComment,'serviceCommandsTable':serviceCommandsTable,'serviceCommandsEntry':serviceCommandsEntry,_J:serviceCommandsName,'serviceCommandsRestart':serviceCommandsRestart,'serviceCommandsStop':serviceCommandsStop,'serviceCommandsStart':serviceCommandsStart,'servicesConfigTable':servicesConfigTable,'servicesConfigEntry':servicesConfigEntry,_K:servicesConfigName,'servicesConfigStartupType':servicesConfigStartupType,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})