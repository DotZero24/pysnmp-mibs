_M='upmTimerName'
_L='upmProfileExecVars'
_K='upmPort'
_J='upmExecutionStatus'
_I='upmEventType'
_H='upmExecutionId'
_G='upmProfileName'
_F='Unsigned32'
_E='DisplayString'
_D='Integer32'
_C='accessible-for-notify'
_B='EXTREME-UPM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
extremeUpm=ModuleIdentity((1,3,6,1,4,1,1916,1,35))
_UpmNotificationTrap_ObjectIdentity=ObjectIdentity
upmNotificationTrap=_UpmNotificationTrap_ObjectIdentity((1,3,6,1,4,1,1916,1,35,1))
_UpmConfig_ObjectIdentity=ObjectIdentity
upmConfig=_UpmConfig_ObjectIdentity((1,3,6,1,4,1,1916,1,35,2))
class _UpmProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpmProfileName_Type.__name__=_E
_UpmProfileName_Object=MibScalar
upmProfileName=_UpmProfileName_Object((1,3,6,1,4,1,1916,1,35,2,1),_UpmProfileName_Type())
upmProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:upmProfileName.setStatus(_A)
class _UpmExecutionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967296))
_UpmExecutionId_Type.__name__=_F
_UpmExecutionId_Object=MibScalar
upmExecutionId=_UpmExecutionId_Object((1,3,6,1,4,1,1916,1,35,2,2),_UpmExecutionId_Type())
upmExecutionId.setMaxAccess(_C)
if mibBuilder.loadTexts:upmExecutionId.setStatus(_A)
class _UpmEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*(('devicedetect',1),('deviceundetect',2),('userauthenticated',3),('userunauthenticated',4),('upmTimer',5),('userrequest',7)))
_UpmEventType_Type.__name__=_D
_UpmEventType_Object=MibScalar
upmEventType=_UpmEventType_Object((1,3,6,1,4,1,1916,1,35,2,3),_UpmEventType_Type())
upmEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:upmEventType.setStatus(_A)
class _UpmExecutionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failure',2)))
_UpmExecutionStatus_Type.__name__=_D
_UpmExecutionStatus_Object=MibScalar
upmExecutionStatus=_UpmExecutionStatus_Object((1,3,6,1,4,1,1916,1,35,2,4),_UpmExecutionStatus_Type())
upmExecutionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:upmExecutionStatus.setStatus(_A)
class _UpmPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967296))
_UpmPort_Type.__name__=_D
_UpmPort_Object=MibScalar
upmPort=_UpmPort_Object((1,3,6,1,4,1,1916,1,35,2,5),_UpmPort_Type())
upmPort.setMaxAccess(_C)
if mibBuilder.loadTexts:upmPort.setStatus(_A)
class _UpmProfileExecVars_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpmProfileExecVars_Type.__name__=_E
_UpmProfileExecVars_Object=MibScalar
upmProfileExecVars=_UpmProfileExecVars_Object((1,3,6,1,4,1,1916,1,35,2,6),_UpmProfileExecVars_Type())
upmProfileExecVars.setMaxAccess(_C)
if mibBuilder.loadTexts:upmProfileExecVars.setStatus(_A)
class _UpmTimerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpmTimerName_Type.__name__=_E
_UpmTimerName_Object=MibScalar
upmTimerName=_UpmTimerName_Object((1,3,6,1,4,1,1916,1,35,2,7),_UpmTimerName_Type())
upmTimerName.setMaxAccess(_C)
if mibBuilder.loadTexts:upmTimerName.setStatus(_A)
upmProfileEventExecution=NotificationType((1,3,6,1,4,1,1916,1,35,1,1))
upmProfileEventExecution.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:upmProfileEventExecution.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeUpm':extremeUpm,'upmNotificationTrap':upmNotificationTrap,'upmProfileEventExecution':upmProfileEventExecution,'upmConfig':upmConfig,_G:upmProfileName,_H:upmExecutionId,_I:upmEventType,_J:upmExecutionStatus,_K:upmPort,_L:upmProfileExecVars,_M:upmTimerName})