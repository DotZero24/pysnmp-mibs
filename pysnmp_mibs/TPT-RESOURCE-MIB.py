_S='tptResourceNotifySubIdentifier'
_R='tptResourceNotifyTimeStamp'
_Q='tptResourceNotifyStateAfter'
_P='tptResourceNotifyStateBefore'
_O='tptResourceNotifyRangeMax'
_N='tptResourceNotifyRangeMin'
_M='tptResourceNotifyThresholdCrit'
_L='tptResourceNotifyThresholdMaj'
_K='tptResourceNotifyCurrentValue'
_J='tptResourceNotifyFSIndex'
_I='tptResourceNotifyIdentifier'
_H='tptResourceNotifyDeviceID'
_G='powerSupplyUnitIndex'
_F='resourceFSIndex'
_E='unknown'
_D='OctetString'
_C='TPT-RESOURCE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_resource=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,5))
if mibBuilder.loadTexts:tpt_resource.setRevisions(('2016-05-25 18:54',))
class ResourceIdentifier(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('filesystem',1),('hpCPU',2),('hpMemory',3),('chassisTemp',4),('fan',5),('powerSupply',6),('hardDisk',7),('i2cBus',8)))
class ResourceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('red',1),('yellow',2),('green',3)))
class PowerSupplyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('red',1),('green',2)))
class SnmpVersions(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('snmpv2',1),('snmpv3',2),('snmpv2-and-snmpv3',3)))
class EnabledOrNot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class FilesystemState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unformatted',0),('formatted',1),('mounted',2)))
class RemoteAuthType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('radius',1),('sms',2),('tacacs',3)))
_ResourceNumberOfFilesystems_Type=Unsigned32
_ResourceNumberOfFilesystems_Object=MibScalar
resourceNumberOfFilesystems=_ResourceNumberOfFilesystems_Object((1,3,6,1,4,1,10734,3,3,2,5,1),_ResourceNumberOfFilesystems_Type())
resourceNumberOfFilesystems.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNumberOfFilesystems.setStatus(_A)
_ResourceFSTable_Object=MibTable
resourceFSTable=_ResourceFSTable_Object((1,3,6,1,4,1,10734,3,3,2,5,2))
if mibBuilder.loadTexts:resourceFSTable.setStatus(_A)
_ResourceFSEntry_Object=MibTableRow
resourceFSEntry=_ResourceFSEntry_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1))
resourceFSEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:resourceFSEntry.setStatus(_A)
_ResourceFSInUseMB_Type=Integer32
_ResourceFSInUseMB_Object=MibTableColumn
resourceFSInUseMB=_ResourceFSInUseMB_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,1),_ResourceFSInUseMB_Type())
resourceFSInUseMB.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSInUseMB.setStatus(_A)
_ResourceFSThresholdMaj_Type=Integer32
_ResourceFSThresholdMaj_Object=MibTableColumn
resourceFSThresholdMaj=_ResourceFSThresholdMaj_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,2),_ResourceFSThresholdMaj_Type())
resourceFSThresholdMaj.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSThresholdMaj.setStatus(_A)
_ResourceFSThresholdCrit_Type=Integer32
_ResourceFSThresholdCrit_Object=MibTableColumn
resourceFSThresholdCrit=_ResourceFSThresholdCrit_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,3),_ResourceFSThresholdCrit_Type())
resourceFSThresholdCrit.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSThresholdCrit.setStatus(_A)
_ResourceFSRangeMin_Type=Integer32
_ResourceFSRangeMin_Object=MibTableColumn
resourceFSRangeMin=_ResourceFSRangeMin_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,4),_ResourceFSRangeMin_Type())
resourceFSRangeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSRangeMin.setStatus(_A)
_ResourceFSRangeMax_Type=Integer32
_ResourceFSRangeMax_Object=MibTableColumn
resourceFSRangeMax=_ResourceFSRangeMax_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,5),_ResourceFSRangeMax_Type())
resourceFSRangeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSRangeMax.setStatus(_A)
class _ResourceFSName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ResourceFSName_Type.__name__=_D
_ResourceFSName_Object=MibTableColumn
resourceFSName=_ResourceFSName_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,6),_ResourceFSName_Type())
resourceFSName.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSName.setStatus(_A)
_ResourceFSIndex_Type=Unsigned32
_ResourceFSIndex_Object=MibTableColumn
resourceFSIndex=_ResourceFSIndex_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,7),_ResourceFSIndex_Type())
resourceFSIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:resourceFSIndex.setStatus(_A)
_ResourceFSState_Type=FilesystemState
_ResourceFSState_Object=MibTableColumn
resourceFSState=_ResourceFSState_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,8),_ResourceFSState_Type())
resourceFSState.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSState.setStatus(_A)
_ResourceFSEncryption_Type=EnabledOrNot
_ResourceFSEncryption_Object=MibTableColumn
resourceFSEncryption=_ResourceFSEncryption_Object((1,3,6,1,4,1,10734,3,3,2,5,2,1,9),_ResourceFSEncryption_Type())
resourceFSEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceFSEncryption.setStatus(_A)
_ResourceHPMemoryObjs_ObjectIdentity=ObjectIdentity
resourceHPMemoryObjs=_ResourceHPMemoryObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,5,3))
if mibBuilder.loadTexts:resourceHPMemoryObjs.setStatus(_A)
_ResourceHPMemoryInUsePercent_Type=Integer32
_ResourceHPMemoryInUsePercent_Object=MibScalar
resourceHPMemoryInUsePercent=_ResourceHPMemoryInUsePercent_Object((1,3,6,1,4,1,10734,3,3,2,5,3,1),_ResourceHPMemoryInUsePercent_Type())
resourceHPMemoryInUsePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPMemoryInUsePercent.setStatus(_A)
_ResourceHPMemoryThresholdMaj_Type=Integer32
_ResourceHPMemoryThresholdMaj_Object=MibScalar
resourceHPMemoryThresholdMaj=_ResourceHPMemoryThresholdMaj_Object((1,3,6,1,4,1,10734,3,3,2,5,3,2),_ResourceHPMemoryThresholdMaj_Type())
resourceHPMemoryThresholdMaj.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPMemoryThresholdMaj.setStatus(_A)
_ResourceHPMemoryThresholdCrit_Type=Integer32
_ResourceHPMemoryThresholdCrit_Object=MibScalar
resourceHPMemoryThresholdCrit=_ResourceHPMemoryThresholdCrit_Object((1,3,6,1,4,1,10734,3,3,2,5,3,3),_ResourceHPMemoryThresholdCrit_Type())
resourceHPMemoryThresholdCrit.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPMemoryThresholdCrit.setStatus(_A)
_ResourceHPMemoryRangeMin_Type=Integer32
_ResourceHPMemoryRangeMin_Object=MibScalar
resourceHPMemoryRangeMin=_ResourceHPMemoryRangeMin_Object((1,3,6,1,4,1,10734,3,3,2,5,3,4),_ResourceHPMemoryRangeMin_Type())
resourceHPMemoryRangeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPMemoryRangeMin.setStatus(_A)
_ResourceHPMemoryRangeMax_Type=Integer32
_ResourceHPMemoryRangeMax_Object=MibScalar
resourceHPMemoryRangeMax=_ResourceHPMemoryRangeMax_Object((1,3,6,1,4,1,10734,3,3,2,5,3,5),_ResourceHPMemoryRangeMax_Type())
resourceHPMemoryRangeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPMemoryRangeMax.setStatus(_A)
_ResourceHPMemoryTotal_Type=Unsigned32
_ResourceHPMemoryTotal_Object=MibScalar
resourceHPMemoryTotal=_ResourceHPMemoryTotal_Object((1,3,6,1,4,1,10734,3,3,2,5,3,6),_ResourceHPMemoryTotal_Type())
resourceHPMemoryTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPMemoryTotal.setStatus(_A)
_ResourceHPCPUObjs_ObjectIdentity=ObjectIdentity
resourceHPCPUObjs=_ResourceHPCPUObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,5,4))
if mibBuilder.loadTexts:resourceHPCPUObjs.setStatus(_A)
_ResourceHPCPUBusyPercent_Type=Integer32
_ResourceHPCPUBusyPercent_Object=MibScalar
resourceHPCPUBusyPercent=_ResourceHPCPUBusyPercent_Object((1,3,6,1,4,1,10734,3,3,2,5,4,1),_ResourceHPCPUBusyPercent_Type())
resourceHPCPUBusyPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPCPUBusyPercent.setStatus(_A)
_ResourceHPCPUThresholdMaj_Type=Integer32
_ResourceHPCPUThresholdMaj_Object=MibScalar
resourceHPCPUThresholdMaj=_ResourceHPCPUThresholdMaj_Object((1,3,6,1,4,1,10734,3,3,2,5,4,2),_ResourceHPCPUThresholdMaj_Type())
resourceHPCPUThresholdMaj.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPCPUThresholdMaj.setStatus(_A)
_ResourceHPCPUThresholdCrit_Type=Integer32
_ResourceHPCPUThresholdCrit_Object=MibScalar
resourceHPCPUThresholdCrit=_ResourceHPCPUThresholdCrit_Object((1,3,6,1,4,1,10734,3,3,2,5,4,3),_ResourceHPCPUThresholdCrit_Type())
resourceHPCPUThresholdCrit.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPCPUThresholdCrit.setStatus(_A)
_ResourceHPCPURangeMin_Type=Integer32
_ResourceHPCPURangeMin_Object=MibScalar
resourceHPCPURangeMin=_ResourceHPCPURangeMin_Object((1,3,6,1,4,1,10734,3,3,2,5,4,4),_ResourceHPCPURangeMin_Type())
resourceHPCPURangeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPCPURangeMin.setStatus(_A)
_ResourceHPCPURangeMax_Type=Integer32
_ResourceHPCPURangeMax_Object=MibScalar
resourceHPCPURangeMax=_ResourceHPCPURangeMax_Object((1,3,6,1,4,1,10734,3,3,2,5,4,5),_ResourceHPCPURangeMax_Type())
resourceHPCPURangeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceHPCPURangeMax.setStatus(_A)
_ResourceNPCPUBusyPercentA_Type=Integer32
_ResourceNPCPUBusyPercentA_Object=MibScalar
resourceNPCPUBusyPercentA=_ResourceNPCPUBusyPercentA_Object((1,3,6,1,4,1,10734,3,3,2,5,4,6),_ResourceNPCPUBusyPercentA_Type())
resourceNPCPUBusyPercentA.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentA.setStatus(_A)
_ResourceNPCPUBusyPercentTier2A_Type=Integer32
_ResourceNPCPUBusyPercentTier2A_Object=MibScalar
resourceNPCPUBusyPercentTier2A=_ResourceNPCPUBusyPercentTier2A_Object((1,3,6,1,4,1,10734,3,3,2,5,4,7),_ResourceNPCPUBusyPercentTier2A_Type())
resourceNPCPUBusyPercentTier2A.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier2A.setStatus(_A)
_ResourceNPCPUBusyPercentTier3A_Type=Integer32
_ResourceNPCPUBusyPercentTier3A_Object=MibScalar
resourceNPCPUBusyPercentTier3A=_ResourceNPCPUBusyPercentTier3A_Object((1,3,6,1,4,1,10734,3,3,2,5,4,8),_ResourceNPCPUBusyPercentTier3A_Type())
resourceNPCPUBusyPercentTier3A.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier3A.setStatus(_A)
_ResourceNPCPUBusyPercentTier4A_Type=Integer32
_ResourceNPCPUBusyPercentTier4A_Object=MibScalar
resourceNPCPUBusyPercentTier4A=_ResourceNPCPUBusyPercentTier4A_Object((1,3,6,1,4,1,10734,3,3,2,5,4,9),_ResourceNPCPUBusyPercentTier4A_Type())
resourceNPCPUBusyPercentTier4A.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier4A.setStatus(_A)
_ResourceNPCPUBusyPercentB_Type=Integer32
_ResourceNPCPUBusyPercentB_Object=MibScalar
resourceNPCPUBusyPercentB=_ResourceNPCPUBusyPercentB_Object((1,3,6,1,4,1,10734,3,3,2,5,4,10),_ResourceNPCPUBusyPercentB_Type())
resourceNPCPUBusyPercentB.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentB.setStatus(_A)
_ResourceNPCPUBusyPercentTier2B_Type=Integer32
_ResourceNPCPUBusyPercentTier2B_Object=MibScalar
resourceNPCPUBusyPercentTier2B=_ResourceNPCPUBusyPercentTier2B_Object((1,3,6,1,4,1,10734,3,3,2,5,4,11),_ResourceNPCPUBusyPercentTier2B_Type())
resourceNPCPUBusyPercentTier2B.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier2B.setStatus(_A)
_ResourceNPCPUBusyPercentTier3B_Type=Integer32
_ResourceNPCPUBusyPercentTier3B_Object=MibScalar
resourceNPCPUBusyPercentTier3B=_ResourceNPCPUBusyPercentTier3B_Object((1,3,6,1,4,1,10734,3,3,2,5,4,12),_ResourceNPCPUBusyPercentTier3B_Type())
resourceNPCPUBusyPercentTier3B.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier3B.setStatus(_A)
_ResourceNPCPUBusyPercentTier4B_Type=Integer32
_ResourceNPCPUBusyPercentTier4B_Object=MibScalar
resourceNPCPUBusyPercentTier4B=_ResourceNPCPUBusyPercentTier4B_Object((1,3,6,1,4,1,10734,3,3,2,5,4,13),_ResourceNPCPUBusyPercentTier4B_Type())
resourceNPCPUBusyPercentTier4B.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier4B.setStatus(_A)
_ResourceNPCPUBusyPercentC_Type=Integer32
_ResourceNPCPUBusyPercentC_Object=MibScalar
resourceNPCPUBusyPercentC=_ResourceNPCPUBusyPercentC_Object((1,3,6,1,4,1,10734,3,3,2,5,4,14),_ResourceNPCPUBusyPercentC_Type())
resourceNPCPUBusyPercentC.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentC.setStatus(_A)
_ResourceNPCPUBusyPercentTier2C_Type=Integer32
_ResourceNPCPUBusyPercentTier2C_Object=MibScalar
resourceNPCPUBusyPercentTier2C=_ResourceNPCPUBusyPercentTier2C_Object((1,3,6,1,4,1,10734,3,3,2,5,4,15),_ResourceNPCPUBusyPercentTier2C_Type())
resourceNPCPUBusyPercentTier2C.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier2C.setStatus(_A)
_ResourceNPCPUBusyPercentTier3C_Type=Integer32
_ResourceNPCPUBusyPercentTier3C_Object=MibScalar
resourceNPCPUBusyPercentTier3C=_ResourceNPCPUBusyPercentTier3C_Object((1,3,6,1,4,1,10734,3,3,2,5,4,16),_ResourceNPCPUBusyPercentTier3C_Type())
resourceNPCPUBusyPercentTier3C.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier3C.setStatus(_A)
_ResourceNPCPUBusyPercentTier4C_Type=Integer32
_ResourceNPCPUBusyPercentTier4C_Object=MibScalar
resourceNPCPUBusyPercentTier4C=_ResourceNPCPUBusyPercentTier4C_Object((1,3,6,1,4,1,10734,3,3,2,5,4,17),_ResourceNPCPUBusyPercentTier4C_Type())
resourceNPCPUBusyPercentTier4C.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceNPCPUBusyPercentTier4C.setStatus(_A)
_ResourceChassisTempObjs_ObjectIdentity=ObjectIdentity
resourceChassisTempObjs=_ResourceChassisTempObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,5,5))
if mibBuilder.loadTexts:resourceChassisTempObjs.setStatus(_A)
_ResourceChassisTempDegreesC_Type=Integer32
_ResourceChassisTempDegreesC_Object=MibScalar
resourceChassisTempDegreesC=_ResourceChassisTempDegreesC_Object((1,3,6,1,4,1,10734,3,3,2,5,5,1),_ResourceChassisTempDegreesC_Type())
resourceChassisTempDegreesC.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceChassisTempDegreesC.setStatus(_A)
_ResourceChassisTempThresholdMaj_Type=Integer32
_ResourceChassisTempThresholdMaj_Object=MibScalar
resourceChassisTempThresholdMaj=_ResourceChassisTempThresholdMaj_Object((1,3,6,1,4,1,10734,3,3,2,5,5,2),_ResourceChassisTempThresholdMaj_Type())
resourceChassisTempThresholdMaj.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceChassisTempThresholdMaj.setStatus(_A)
_ResourceChassisTempThresholdCrit_Type=Integer32
_ResourceChassisTempThresholdCrit_Object=MibScalar
resourceChassisTempThresholdCrit=_ResourceChassisTempThresholdCrit_Object((1,3,6,1,4,1,10734,3,3,2,5,5,3),_ResourceChassisTempThresholdCrit_Type())
resourceChassisTempThresholdCrit.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceChassisTempThresholdCrit.setStatus(_A)
_ResourceChassisTempRangeMin_Type=Integer32
_ResourceChassisTempRangeMin_Object=MibScalar
resourceChassisTempRangeMin=_ResourceChassisTempRangeMin_Object((1,3,6,1,4,1,10734,3,3,2,5,5,4),_ResourceChassisTempRangeMin_Type())
resourceChassisTempRangeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceChassisTempRangeMin.setStatus(_A)
_ResourceChassisTempRangeMax_Type=Integer32
_ResourceChassisTempRangeMax_Object=MibScalar
resourceChassisTempRangeMax=_ResourceChassisTempRangeMax_Object((1,3,6,1,4,1,10734,3,3,2,5,5,5),_ResourceChassisTempRangeMax_Type())
resourceChassisTempRangeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceChassisTempRangeMax.setStatus(_A)
class _ResourceVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_ResourceVersion_Type.__name__=_D
_ResourceVersion_Object=MibScalar
resourceVersion=_ResourceVersion_Object((1,3,6,1,4,1,10734,3,3,2,5,6),_ResourceVersion_Type())
resourceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceVersion.setStatus(_A)
_ResourceLogCountObjs_ObjectIdentity=ObjectIdentity
resourceLogCountObjs=_ResourceLogCountObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,5,7))
if mibBuilder.loadTexts:resourceLogCountObjs.setStatus(_A)
_ResourceLogCountCritical_Type=Unsigned32
_ResourceLogCountCritical_Object=MibScalar
resourceLogCountCritical=_ResourceLogCountCritical_Object((1,3,6,1,4,1,10734,3,3,2,5,7,1),_ResourceLogCountCritical_Type())
resourceLogCountCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceLogCountCritical.setStatus(_A)
_ResourceLogCountError_Type=Unsigned32
_ResourceLogCountError_Object=MibScalar
resourceLogCountError=_ResourceLogCountError_Object((1,3,6,1,4,1,10734,3,3,2,5,7,2),_ResourceLogCountError_Type())
resourceLogCountError.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceLogCountError.setStatus(_A)
_ResourceLogCountWarning_Type=Unsigned32
_ResourceLogCountWarning_Object=MibScalar
resourceLogCountWarning=_ResourceLogCountWarning_Object((1,3,6,1,4,1,10734,3,3,2,5,7,3),_ResourceLogCountWarning_Type())
resourceLogCountWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceLogCountWarning.setStatus(_A)
_ResourceLogCountInfo_Type=Unsigned32
_ResourceLogCountInfo_Object=MibScalar
resourceLogCountInfo=_ResourceLogCountInfo_Object((1,3,6,1,4,1,10734,3,3,2,5,7,4),_ResourceLogCountInfo_Type())
resourceLogCountInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceLogCountInfo.setStatus(_A)
_ResourceMetricObjs_ObjectIdentity=ObjectIdentity
resourceMetricObjs=_ResourceMetricObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,5,8))
if mibBuilder.loadTexts:resourceMetricObjs.setStatus(_A)
_ResourceMetricFastpath_Type=Counter64
_ResourceMetricFastpath_Object=MibScalar
resourceMetricFastpath=_ResourceMetricFastpath_Object((1,3,6,1,4,1,10734,3,3,2,5,8,1),_ResourceMetricFastpath_Type())
resourceMetricFastpath.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceMetricFastpath.setStatus(_A)
_ResourceMetricSmartpath_Type=Counter64
_ResourceMetricSmartpath_Object=MibScalar
resourceMetricSmartpath=_ResourceMetricSmartpath_Object((1,3,6,1,4,1,10734,3,3,2,5,8,2),_ResourceMetricSmartpath_Type())
resourceMetricSmartpath.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceMetricSmartpath.setStatus(_A)
_ResourceMetricCongestion_Type=Counter64
_ResourceMetricCongestion_Object=MibScalar
resourceMetricCongestion=_ResourceMetricCongestion_Object((1,3,6,1,4,1,10734,3,3,2,5,8,3),_ResourceMetricCongestion_Type())
resourceMetricCongestion.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceMetricCongestion.setStatus(_A)
_ResourcePowerSupplyObjs_ObjectIdentity=ObjectIdentity
resourcePowerSupplyObjs=_ResourcePowerSupplyObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,5,9))
if mibBuilder.loadTexts:resourcePowerSupplyObjs.setStatus(_A)
_ResourcePowerSupplyStatus_Type=ResourceState
_ResourcePowerSupplyStatus_Object=MibScalar
resourcePowerSupplyStatus=_ResourcePowerSupplyStatus_Object((1,3,6,1,4,1,10734,3,3,2,5,9,1),_ResourcePowerSupplyStatus_Type())
resourcePowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:resourcePowerSupplyStatus.setStatus('deprecated')
_ResourcePowerSupplyQuantity_Type=Integer32
_ResourcePowerSupplyQuantity_Object=MibScalar
resourcePowerSupplyQuantity=_ResourcePowerSupplyQuantity_Object((1,3,6,1,4,1,10734,3,3,2,5,9,2),_ResourcePowerSupplyQuantity_Type())
resourcePowerSupplyQuantity.setMaxAccess(_B)
if mibBuilder.loadTexts:resourcePowerSupplyQuantity.setStatus(_A)
_ResourcePowerSupplyMonitoring_Type=Integer32
_ResourcePowerSupplyMonitoring_Object=MibScalar
resourcePowerSupplyMonitoring=_ResourcePowerSupplyMonitoring_Object((1,3,6,1,4,1,10734,3,3,2,5,9,3),_ResourcePowerSupplyMonitoring_Type())
resourcePowerSupplyMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:resourcePowerSupplyMonitoring.setStatus(_A)
_ResourcePowerSupplyTable_Object=MibTable
resourcePowerSupplyTable=_ResourcePowerSupplyTable_Object((1,3,6,1,4,1,10734,3,3,2,5,9,4))
if mibBuilder.loadTexts:resourcePowerSupplyTable.setStatus(_A)
_ResourcePowerSupplyEntry_Object=MibTableRow
resourcePowerSupplyEntry=_ResourcePowerSupplyEntry_Object((1,3,6,1,4,1,10734,3,3,2,5,9,4,1))
resourcePowerSupplyEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:resourcePowerSupplyEntry.setStatus(_A)
_PowerSupplyUnitIndex_Type=Integer32
_PowerSupplyUnitIndex_Object=MibTableColumn
powerSupplyUnitIndex=_PowerSupplyUnitIndex_Object((1,3,6,1,4,1,10734,3,3,2,5,9,4,1,1),_PowerSupplyUnitIndex_Type())
powerSupplyUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyUnitIndex.setStatus(_A)
_PowerSupplyStatus_Type=ResourceState
_PowerSupplyStatus_Object=MibTableColumn
powerSupplyStatus=_PowerSupplyStatus_Object((1,3,6,1,4,1,10734,3,3,2,5,9,4,1,2),_PowerSupplyStatus_Type())
powerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyStatus.setStatus(_A)
_ResourceDateTime_Type=Unsigned32
_ResourceDateTime_Object=MibScalar
resourceDateTime=_ResourceDateTime_Object((1,3,6,1,4,1,10734,3,3,2,5,10),_ResourceDateTime_Type())
resourceDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceDateTime.setStatus(_A)
_ResourceSnmpRunState_Type=SnmpVersions
_ResourceSnmpRunState_Object=MibScalar
resourceSnmpRunState=_ResourceSnmpRunState_Object((1,3,6,1,4,1,10734,3,3,2,5,11),_ResourceSnmpRunState_Type())
resourceSnmpRunState.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceSnmpRunState.setStatus(_A)
_ResourceSnmpConfig_Type=SnmpVersions
_ResourceSnmpConfig_Object=MibScalar
resourceSnmpConfig=_ResourceSnmpConfig_Object((1,3,6,1,4,1,10734,3,3,2,5,12),_ResourceSnmpConfig_Type())
resourceSnmpConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceSnmpConfig.setStatus(_A)
_ResourceRemoteAuthEnabled_Type=EnabledOrNot
_ResourceRemoteAuthEnabled_Object=MibScalar
resourceRemoteAuthEnabled=_ResourceRemoteAuthEnabled_Object((1,3,6,1,4,1,10734,3,3,2,5,13),_ResourceRemoteAuthEnabled_Type())
resourceRemoteAuthEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceRemoteAuthEnabled.setStatus(_A)
_ResourceRemoteAuthTimeout_Type=Integer32
_ResourceRemoteAuthTimeout_Object=MibScalar
resourceRemoteAuthTimeout=_ResourceRemoteAuthTimeout_Object((1,3,6,1,4,1,10734,3,3,2,5,14),_ResourceRemoteAuthTimeout_Type())
resourceRemoteAuthTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceRemoteAuthTimeout.setStatus(_A)
_ResourceRemoteAuthType_Type=RemoteAuthType
_ResourceRemoteAuthType_Object=MibScalar
resourceRemoteAuthType=_ResourceRemoteAuthType_Object((1,3,6,1,4,1,10734,3,3,2,5,15),_ResourceRemoteAuthType_Type())
resourceRemoteAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceRemoteAuthType.setStatus(_A)
class _TptResourceNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptResourceNotifyDeviceID_Type.__name__=_D
_TptResourceNotifyDeviceID_Object=MibScalar
tptResourceNotifyDeviceID=_TptResourceNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,61),_TptResourceNotifyDeviceID_Type())
tptResourceNotifyDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyDeviceID.setStatus(_A)
_TptResourceNotifyIdentifier_Type=ResourceIdentifier
_TptResourceNotifyIdentifier_Object=MibScalar
tptResourceNotifyIdentifier=_TptResourceNotifyIdentifier_Object((1,3,6,1,4,1,10734,3,3,3,1,62),_TptResourceNotifyIdentifier_Type())
tptResourceNotifyIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyIdentifier.setStatus(_A)
_TptResourceNotifyFSIndex_Type=Unsigned32
_TptResourceNotifyFSIndex_Object=MibScalar
tptResourceNotifyFSIndex=_TptResourceNotifyFSIndex_Object((1,3,6,1,4,1,10734,3,3,3,1,63),_TptResourceNotifyFSIndex_Type())
tptResourceNotifyFSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyFSIndex.setStatus(_A)
_TptResourceNotifyCurrentValue_Type=Integer32
_TptResourceNotifyCurrentValue_Object=MibScalar
tptResourceNotifyCurrentValue=_TptResourceNotifyCurrentValue_Object((1,3,6,1,4,1,10734,3,3,3,1,64),_TptResourceNotifyCurrentValue_Type())
tptResourceNotifyCurrentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyCurrentValue.setStatus(_A)
_TptResourceNotifyThresholdMaj_Type=Integer32
_TptResourceNotifyThresholdMaj_Object=MibScalar
tptResourceNotifyThresholdMaj=_TptResourceNotifyThresholdMaj_Object((1,3,6,1,4,1,10734,3,3,3,1,65),_TptResourceNotifyThresholdMaj_Type())
tptResourceNotifyThresholdMaj.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyThresholdMaj.setStatus(_A)
_TptResourceNotifyThresholdCrit_Type=Integer32
_TptResourceNotifyThresholdCrit_Object=MibScalar
tptResourceNotifyThresholdCrit=_TptResourceNotifyThresholdCrit_Object((1,3,6,1,4,1,10734,3,3,3,1,66),_TptResourceNotifyThresholdCrit_Type())
tptResourceNotifyThresholdCrit.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyThresholdCrit.setStatus(_A)
_TptResourceNotifyRangeMin_Type=Integer32
_TptResourceNotifyRangeMin_Object=MibScalar
tptResourceNotifyRangeMin=_TptResourceNotifyRangeMin_Object((1,3,6,1,4,1,10734,3,3,3,1,67),_TptResourceNotifyRangeMin_Type())
tptResourceNotifyRangeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyRangeMin.setStatus(_A)
_TptResourceNotifyRangeMax_Type=Integer32
_TptResourceNotifyRangeMax_Object=MibScalar
tptResourceNotifyRangeMax=_TptResourceNotifyRangeMax_Object((1,3,6,1,4,1,10734,3,3,3,1,68),_TptResourceNotifyRangeMax_Type())
tptResourceNotifyRangeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyRangeMax.setStatus(_A)
_TptResourceNotifyStateBefore_Type=ResourceState
_TptResourceNotifyStateBefore_Object=MibScalar
tptResourceNotifyStateBefore=_TptResourceNotifyStateBefore_Object((1,3,6,1,4,1,10734,3,3,3,1,69),_TptResourceNotifyStateBefore_Type())
tptResourceNotifyStateBefore.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyStateBefore.setStatus(_A)
_TptResourceNotifyStateAfter_Type=ResourceState
_TptResourceNotifyStateAfter_Object=MibScalar
tptResourceNotifyStateAfter=_TptResourceNotifyStateAfter_Object((1,3,6,1,4,1,10734,3,3,3,1,70),_TptResourceNotifyStateAfter_Type())
tptResourceNotifyStateAfter.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyStateAfter.setStatus(_A)
_TptResourceNotifyTimeStamp_Type=Unsigned32
_TptResourceNotifyTimeStamp_Object=MibScalar
tptResourceNotifyTimeStamp=_TptResourceNotifyTimeStamp_Object((1,3,6,1,4,1,10734,3,3,3,1,71),_TptResourceNotifyTimeStamp_Type())
tptResourceNotifyTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifyTimeStamp.setStatus(_A)
_TptResourceNotifySubIdentifier_Type=Integer32
_TptResourceNotifySubIdentifier_Object=MibScalar
tptResourceNotifySubIdentifier=_TptResourceNotifySubIdentifier_Object((1,3,6,1,4,1,10734,3,3,3,1,72),_TptResourceNotifySubIdentifier_Type())
tptResourceNotifySubIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:tptResourceNotifySubIdentifier.setStatus(_A)
tptResourceNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,14))
tptResourceNotify.setObjects(*((_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S)))
if mibBuilder.loadTexts:tptResourceNotify.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ResourceIdentifier':ResourceIdentifier,'ResourceState':ResourceState,'PowerSupplyState':PowerSupplyState,'SnmpVersions':SnmpVersions,'EnabledOrNot':EnabledOrNot,'FilesystemState':FilesystemState,'RemoteAuthType':RemoteAuthType,'tpt-resource':tpt_resource,'resourceNumberOfFilesystems':resourceNumberOfFilesystems,'resourceFSTable':resourceFSTable,'resourceFSEntry':resourceFSEntry,'resourceFSInUseMB':resourceFSInUseMB,'resourceFSThresholdMaj':resourceFSThresholdMaj,'resourceFSThresholdCrit':resourceFSThresholdCrit,'resourceFSRangeMin':resourceFSRangeMin,'resourceFSRangeMax':resourceFSRangeMax,'resourceFSName':resourceFSName,_F:resourceFSIndex,'resourceFSState':resourceFSState,'resourceFSEncryption':resourceFSEncryption,'resourceHPMemoryObjs':resourceHPMemoryObjs,'resourceHPMemoryInUsePercent':resourceHPMemoryInUsePercent,'resourceHPMemoryThresholdMaj':resourceHPMemoryThresholdMaj,'resourceHPMemoryThresholdCrit':resourceHPMemoryThresholdCrit,'resourceHPMemoryRangeMin':resourceHPMemoryRangeMin,'resourceHPMemoryRangeMax':resourceHPMemoryRangeMax,'resourceHPMemoryTotal':resourceHPMemoryTotal,'resourceHPCPUObjs':resourceHPCPUObjs,'resourceHPCPUBusyPercent':resourceHPCPUBusyPercent,'resourceHPCPUThresholdMaj':resourceHPCPUThresholdMaj,'resourceHPCPUThresholdCrit':resourceHPCPUThresholdCrit,'resourceHPCPURangeMin':resourceHPCPURangeMin,'resourceHPCPURangeMax':resourceHPCPURangeMax,'resourceNPCPUBusyPercentA':resourceNPCPUBusyPercentA,'resourceNPCPUBusyPercentTier2A':resourceNPCPUBusyPercentTier2A,'resourceNPCPUBusyPercentTier3A':resourceNPCPUBusyPercentTier3A,'resourceNPCPUBusyPercentTier4A':resourceNPCPUBusyPercentTier4A,'resourceNPCPUBusyPercentB':resourceNPCPUBusyPercentB,'resourceNPCPUBusyPercentTier2B':resourceNPCPUBusyPercentTier2B,'resourceNPCPUBusyPercentTier3B':resourceNPCPUBusyPercentTier3B,'resourceNPCPUBusyPercentTier4B':resourceNPCPUBusyPercentTier4B,'resourceNPCPUBusyPercentC':resourceNPCPUBusyPercentC,'resourceNPCPUBusyPercentTier2C':resourceNPCPUBusyPercentTier2C,'resourceNPCPUBusyPercentTier3C':resourceNPCPUBusyPercentTier3C,'resourceNPCPUBusyPercentTier4C':resourceNPCPUBusyPercentTier4C,'resourceChassisTempObjs':resourceChassisTempObjs,'resourceChassisTempDegreesC':resourceChassisTempDegreesC,'resourceChassisTempThresholdMaj':resourceChassisTempThresholdMaj,'resourceChassisTempThresholdCrit':resourceChassisTempThresholdCrit,'resourceChassisTempRangeMin':resourceChassisTempRangeMin,'resourceChassisTempRangeMax':resourceChassisTempRangeMax,'resourceVersion':resourceVersion,'resourceLogCountObjs':resourceLogCountObjs,'resourceLogCountCritical':resourceLogCountCritical,'resourceLogCountError':resourceLogCountError,'resourceLogCountWarning':resourceLogCountWarning,'resourceLogCountInfo':resourceLogCountInfo,'resourceMetricObjs':resourceMetricObjs,'resourceMetricFastpath':resourceMetricFastpath,'resourceMetricSmartpath':resourceMetricSmartpath,'resourceMetricCongestion':resourceMetricCongestion,'resourcePowerSupplyObjs':resourcePowerSupplyObjs,'resourcePowerSupplyStatus':resourcePowerSupplyStatus,'resourcePowerSupplyQuantity':resourcePowerSupplyQuantity,'resourcePowerSupplyMonitoring':resourcePowerSupplyMonitoring,'resourcePowerSupplyTable':resourcePowerSupplyTable,'resourcePowerSupplyEntry':resourcePowerSupplyEntry,_G:powerSupplyUnitIndex,'powerSupplyStatus':powerSupplyStatus,'resourceDateTime':resourceDateTime,'resourceSnmpRunState':resourceSnmpRunState,'resourceSnmpConfig':resourceSnmpConfig,'resourceRemoteAuthEnabled':resourceRemoteAuthEnabled,'resourceRemoteAuthTimeout':resourceRemoteAuthTimeout,'resourceRemoteAuthType':resourceRemoteAuthType,'tptResourceNotify':tptResourceNotify,_H:tptResourceNotifyDeviceID,_I:tptResourceNotifyIdentifier,_J:tptResourceNotifyFSIndex,_K:tptResourceNotifyCurrentValue,_L:tptResourceNotifyThresholdMaj,_M:tptResourceNotifyThresholdCrit,_N:tptResourceNotifyRangeMin,_O:tptResourceNotifyRangeMax,_P:tptResourceNotifyStateBefore,_Q:tptResourceNotifyStateAfter,_R:tptResourceNotifyTimeStamp,_S:tptResourceNotifySubIdentifier})