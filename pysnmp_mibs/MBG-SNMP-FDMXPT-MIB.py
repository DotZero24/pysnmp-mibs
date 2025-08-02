_b='mbgFDMTrapsGroup'
_a='mbgFDMObjectsGroup'
_Z='mbgFDMNormalOperation'
_Y='mbgFDMXPTReboot'
_X='mbgFDMTrapFreqLimitExceeded'
_W='mbgFDMTrapA2Overflow'
_V='mbgFDMTrapA1Overflow'
_U='mbgFDMTrapTimeDeviationOverflow'
_T='mbgFDMTrapNoPowerline'
_S='mbgFDMTrapNoPPS'
_R='mbgFDMTrapNo10Mhz'
_Q='mbgFDMTrapNoTimeString'
_P='mbgFDMTrapInternalError'
_O='mbgFDMErrorStatus'
_N='mbgFDMTimeDevVal'
_M='mbgFDMTimeDev'
_L='mbgFDMFreqDevVal'
_K='mbgFDMFreqDev'
_J='mbgFDMPLTime'
_I='mbgFDMRefTime'
_H='mbgFDMFrequencyVal'
_G='mbgFDMFrequency'
_F='mbgFDMModeVal'
_E='mbgFDMMode'
_D='Integer32'
_C='read-only'
_B='MBG-SNMP-FDMXPT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mbgSnmpRoot,=mibBuilder.importSymbols('MBG-SNMP-ROOT-MIB','mbgSnmpRoot')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mbgFDM=ModuleIdentity((1,3,6,1,4,1,5597,15))
if mibBuilder.loadTexts:mbgFDM.setRevisions(('2012-01-25 00:00','2006-01-20 00:00'))
_MbgFDMData_ObjectIdentity=ObjectIdentity
mbgFDMData=_MbgFDMData_ObjectIdentity((1,3,6,1,4,1,5597,15,2))
_MbgFDMMode_Type=DisplayString
_MbgFDMMode_Object=MibScalar
mbgFDMMode=_MbgFDMMode_Object((1,3,6,1,4,1,5597,15,2,1),_MbgFDMMode_Type())
mbgFDMMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMMode.setStatus(_A)
class _MbgFDMModeVal_Type(Integer32):defaultValue=0
_MbgFDMModeVal_Type.__name__=_D
_MbgFDMModeVal_Object=MibScalar
mbgFDMModeVal=_MbgFDMModeVal_Object((1,3,6,1,4,1,5597,15,2,2),_MbgFDMModeVal_Type())
mbgFDMModeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMModeVal.setStatus(_A)
_MbgFDMFrequency_Type=DisplayString
_MbgFDMFrequency_Object=MibScalar
mbgFDMFrequency=_MbgFDMFrequency_Object((1,3,6,1,4,1,5597,15,2,3),_MbgFDMFrequency_Type())
mbgFDMFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMFrequency.setStatus(_A)
class _MbgFDMFrequencyVal_Type(Integer32):defaultValue=0
_MbgFDMFrequencyVal_Type.__name__=_D
_MbgFDMFrequencyVal_Object=MibScalar
mbgFDMFrequencyVal=_MbgFDMFrequencyVal_Object((1,3,6,1,4,1,5597,15,2,4),_MbgFDMFrequencyVal_Type())
mbgFDMFrequencyVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMFrequencyVal.setStatus(_A)
_MbgFDMRefTime_Type=DisplayString
_MbgFDMRefTime_Object=MibScalar
mbgFDMRefTime=_MbgFDMRefTime_Object((1,3,6,1,4,1,5597,15,2,5),_MbgFDMRefTime_Type())
mbgFDMRefTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMRefTime.setStatus(_A)
_MbgFDMPLTime_Type=DisplayString
_MbgFDMPLTime_Object=MibScalar
mbgFDMPLTime=_MbgFDMPLTime_Object((1,3,6,1,4,1,5597,15,2,6),_MbgFDMPLTime_Type())
mbgFDMPLTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMPLTime.setStatus(_A)
_MbgFDMFreqDev_Type=DisplayString
_MbgFDMFreqDev_Object=MibScalar
mbgFDMFreqDev=_MbgFDMFreqDev_Object((1,3,6,1,4,1,5597,15,2,7),_MbgFDMFreqDev_Type())
mbgFDMFreqDev.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMFreqDev.setStatus(_A)
class _MbgFDMFreqDevVal_Type(Integer32):defaultValue=0
_MbgFDMFreqDevVal_Type.__name__=_D
_MbgFDMFreqDevVal_Object=MibScalar
mbgFDMFreqDevVal=_MbgFDMFreqDevVal_Object((1,3,6,1,4,1,5597,15,2,8),_MbgFDMFreqDevVal_Type())
mbgFDMFreqDevVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMFreqDevVal.setStatus(_A)
_MbgFDMTimeDev_Type=DisplayString
_MbgFDMTimeDev_Object=MibScalar
mbgFDMTimeDev=_MbgFDMTimeDev_Object((1,3,6,1,4,1,5597,15,2,9),_MbgFDMTimeDev_Type())
mbgFDMTimeDev.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMTimeDev.setStatus(_A)
class _MbgFDMTimeDevVal_Type(Integer32):defaultValue=0
_MbgFDMTimeDevVal_Type.__name__=_D
_MbgFDMTimeDevVal_Object=MibScalar
mbgFDMTimeDevVal=_MbgFDMTimeDevVal_Object((1,3,6,1,4,1,5597,15,2,10),_MbgFDMTimeDevVal_Type())
mbgFDMTimeDevVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMTimeDevVal.setStatus(_A)
_MbgFDMErrorStatus_Type=DisplayString
_MbgFDMErrorStatus_Object=MibScalar
mbgFDMErrorStatus=_MbgFDMErrorStatus_Object((1,3,6,1,4,1,5597,15,2,11),_MbgFDMErrorStatus_Type())
mbgFDMErrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgFDMErrorStatus.setStatus(_A)
_MbgFDMTraps_ObjectIdentity=ObjectIdentity
mbgFDMTraps=_MbgFDMTraps_ObjectIdentity((1,3,6,1,4,1,5597,15,3))
_MbgFDMConformance_ObjectIdentity=ObjectIdentity
mbgFDMConformance=_MbgFDMConformance_ObjectIdentity((1,3,6,1,4,1,5597,15,90))
_MbgFDMCompliances_ObjectIdentity=ObjectIdentity
mbgFDMCompliances=_MbgFDMCompliances_ObjectIdentity((1,3,6,1,4,1,5597,15,90,1))
_MbgFDMGroups_ObjectIdentity=ObjectIdentity
mbgFDMGroups=_MbgFDMGroups_ObjectIdentity((1,3,6,1,4,1,5597,15,90,2))
mbgFDMObjectsGroup=ObjectGroup((1,3,6,1,4,1,5597,15,90,2,1))
mbgFDMObjectsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:mbgFDMObjectsGroup.setStatus(_A)
mbgFDMTrapInternalError=NotificationType((1,3,6,1,4,1,5597,15,3,1))
if mibBuilder.loadTexts:mbgFDMTrapInternalError.setStatus(_A)
mbgFDMTrapNoTimeString=NotificationType((1,3,6,1,4,1,5597,15,3,2))
if mibBuilder.loadTexts:mbgFDMTrapNoTimeString.setStatus(_A)
mbgFDMTrapNo10Mhz=NotificationType((1,3,6,1,4,1,5597,15,3,3))
if mibBuilder.loadTexts:mbgFDMTrapNo10Mhz.setStatus(_A)
mbgFDMTrapNoPPS=NotificationType((1,3,6,1,4,1,5597,15,3,4))
if mibBuilder.loadTexts:mbgFDMTrapNoPPS.setStatus(_A)
mbgFDMTrapNoPowerline=NotificationType((1,3,6,1,4,1,5597,15,3,5))
if mibBuilder.loadTexts:mbgFDMTrapNoPowerline.setStatus(_A)
mbgFDMTrapTimeDeviationOverflow=NotificationType((1,3,6,1,4,1,5597,15,3,6))
if mibBuilder.loadTexts:mbgFDMTrapTimeDeviationOverflow.setStatus(_A)
mbgFDMTrapA1Overflow=NotificationType((1,3,6,1,4,1,5597,15,3,7))
if mibBuilder.loadTexts:mbgFDMTrapA1Overflow.setStatus(_A)
mbgFDMTrapA2Overflow=NotificationType((1,3,6,1,4,1,5597,15,3,8))
if mibBuilder.loadTexts:mbgFDMTrapA2Overflow.setStatus(_A)
mbgFDMTrapFreqLimitExceeded=NotificationType((1,3,6,1,4,1,5597,15,3,9))
if mibBuilder.loadTexts:mbgFDMTrapFreqLimitExceeded.setStatus(_A)
mbgFDMXPTReboot=NotificationType((1,3,6,1,4,1,5597,15,3,10))
if mibBuilder.loadTexts:mbgFDMXPTReboot.setStatus(_A)
mbgFDMNormalOperation=NotificationType((1,3,6,1,4,1,5597,15,3,99))
if mibBuilder.loadTexts:mbgFDMNormalOperation.setStatus(_A)
mbgFDMTrapsGroup=NotificationGroup((1,3,6,1,4,1,5597,15,90,2,2))
mbgFDMTrapsGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:mbgFDMTrapsGroup.setStatus(_A)
mbgFDMCompliance=ModuleCompliance((1,3,6,1,4,1,5597,15,90,1,1))
mbgFDMCompliance.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:mbgFDMCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mbgFDM':mbgFDM,'mbgFDMData':mbgFDMData,_E:mbgFDMMode,_F:mbgFDMModeVal,_G:mbgFDMFrequency,_H:mbgFDMFrequencyVal,_I:mbgFDMRefTime,_J:mbgFDMPLTime,_K:mbgFDMFreqDev,_L:mbgFDMFreqDevVal,_M:mbgFDMTimeDev,_N:mbgFDMTimeDevVal,_O:mbgFDMErrorStatus,'mbgFDMTraps':mbgFDMTraps,_P:mbgFDMTrapInternalError,_Q:mbgFDMTrapNoTimeString,_R:mbgFDMTrapNo10Mhz,_S:mbgFDMTrapNoPPS,_T:mbgFDMTrapNoPowerline,_U:mbgFDMTrapTimeDeviationOverflow,_V:mbgFDMTrapA1Overflow,_W:mbgFDMTrapA2Overflow,_X:mbgFDMTrapFreqLimitExceeded,_Y:mbgFDMXPTReboot,_Z:mbgFDMNormalOperation,'mbgFDMConformance':mbgFDMConformance,'mbgFDMCompliances':mbgFDMCompliances,'mbgFDMCompliance':mbgFDMCompliance,'mbgFDMGroups':mbgFDMGroups,_a:mbgFDMObjectsGroup,_b:mbgFDMTrapsGroup})