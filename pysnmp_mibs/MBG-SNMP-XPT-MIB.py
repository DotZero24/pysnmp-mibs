_A2='mbgXPTTrapsGroup'
_A1='mbgXPTObjectsGroup'
_A0='mbgGPSTrapTestNotification'
_z='mbgGPSTrapPowerSupplyOK'
_y='mbgGPSTrapPowerSupplyFailure'
_x='mbgGPSTrapMasterclockSwitchover'
_w='mbgGPSTrapLeapSecondAnnounced'
_v='mbgGPSTrapLANXPTBoot'
_u='mbgGPSTrapAntennaReconnect'
_t='mbgGPSTrapAntennaFaulty'
_s='mbgGPSTrapReceiverNotSync'
_r='mbgGPSTrapReceiverNotResponding'
_q='mbgGPSNavSolved'
_p='mbgGPSTrapWarmBoot'
_o='mbgGPSTrapColdBoot'
_n='mbgSCUPSU2Status'
_m='mbgSCUPSU1Status'
_l='mbgSCUPSUStatus'
_k='mbgSCUACOMode'
_j='mbgSCUSelectedInputVal'
_i='mbgSCUSelectedInput'
_h='mbgSCUDisableOutputs'
_g='mbgSCUTimelimitError'
_f='mbgSCUTimeSync2'
_e='mbgSCUTimeSync1'
_d='mbgSCUMasterselectVal'
_c='mbgSCUMasterselect'
_b='mbgSCUMasterVal'
_a='mbgSCUMaster'
_Z='mbgSCUTypeVal'
_Y='mbgSCUType'
_X='mbgGPSRef2GpsSatellitesInView'
_W='mbgGPSRef2GpsSatellitesGood'
_V='mbgGPSRef2GpsSatellites'
_U='mbgGPSRef2GpsPosition'
_T='mbgGPSRef2GpsStateVal'
_S='mbgGPSRef2GpsState'
_R='mbgGPSRefclock2ModeVal'
_Q='mbgGPSRefclock2Mode'
_P='mbgGPSRefclock2TypeVal'
_O='mbgGPSRefclock2Type'
_N='mbgGPSRef1GpsSatellitesInView'
_M='mbgGPSRef1GpsSatellitesGood'
_L='mbgGPSRef1GpsSatellites'
_K='mbgGPSRef1GpsPosition'
_J='mbgGPSRef1GpsStateVal'
_I='mbgGPSRef1GpsState'
_H='mbgGPSRefclock1ModeVal'
_G='mbgGPSRefclock1Mode'
_F='mbgGPSRefclock1TypeVal'
_E='mbgGPSRefclock1Type'
_D='Integer32'
_C='read-only'
_B='MBG-SNMP-XPT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mbgSnmpRoot,=mibBuilder.importSymbols('MBG-SNMP-ROOT-MIB','mbgSnmpRoot')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mbgXPT=ModuleIdentity((1,3,6,1,4,1,5597,10))
if mibBuilder.loadTexts:mbgXPT.setRevisions(('2012-01-25 00:00','2006-01-20 00:00'))
_MbgGPSRefclock1_ObjectIdentity=ObjectIdentity
mbgGPSRefclock1=_MbgGPSRefclock1_ObjectIdentity((1,3,6,1,4,1,5597,10,2))
_MbgGPSRefclock1Type_Type=DisplayString
_MbgGPSRefclock1Type_Object=MibScalar
mbgGPSRefclock1Type=_MbgGPSRefclock1Type_Object((1,3,6,1,4,1,5597,10,2,1),_MbgGPSRefclock1Type_Type())
mbgGPSRefclock1Type.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock1Type.setStatus(_A)
class _MbgGPSRefclock1TypeVal_Type(Integer32):defaultValue=0
_MbgGPSRefclock1TypeVal_Type.__name__=_D
_MbgGPSRefclock1TypeVal_Object=MibScalar
mbgGPSRefclock1TypeVal=_MbgGPSRefclock1TypeVal_Object((1,3,6,1,4,1,5597,10,2,2),_MbgGPSRefclock1TypeVal_Type())
mbgGPSRefclock1TypeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock1TypeVal.setStatus(_A)
_MbgGPSRefclock1Mode_Type=DisplayString
_MbgGPSRefclock1Mode_Object=MibScalar
mbgGPSRefclock1Mode=_MbgGPSRefclock1Mode_Object((1,3,6,1,4,1,5597,10,2,3),_MbgGPSRefclock1Mode_Type())
mbgGPSRefclock1Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock1Mode.setStatus(_A)
class _MbgGPSRefclock1ModeVal_Type(Integer32):defaultValue=0
_MbgGPSRefclock1ModeVal_Type.__name__=_D
_MbgGPSRefclock1ModeVal_Object=MibScalar
mbgGPSRefclock1ModeVal=_MbgGPSRefclock1ModeVal_Object((1,3,6,1,4,1,5597,10,2,4),_MbgGPSRefclock1ModeVal_Type())
mbgGPSRefclock1ModeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock1ModeVal.setStatus(_A)
_MbgGPSRef1GpsState_Type=DisplayString
_MbgGPSRef1GpsState_Object=MibScalar
mbgGPSRef1GpsState=_MbgGPSRef1GpsState_Object((1,3,6,1,4,1,5597,10,2,5),_MbgGPSRef1GpsState_Type())
mbgGPSRef1GpsState.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef1GpsState.setStatus(_A)
class _MbgGPSRef1GpsStateVal_Type(Integer32):defaultValue=0
_MbgGPSRef1GpsStateVal_Type.__name__=_D
_MbgGPSRef1GpsStateVal_Object=MibScalar
mbgGPSRef1GpsStateVal=_MbgGPSRef1GpsStateVal_Object((1,3,6,1,4,1,5597,10,2,6),_MbgGPSRef1GpsStateVal_Type())
mbgGPSRef1GpsStateVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef1GpsStateVal.setStatus(_A)
_MbgGPSRef1GpsPosition_Type=DisplayString
_MbgGPSRef1GpsPosition_Object=MibScalar
mbgGPSRef1GpsPosition=_MbgGPSRef1GpsPosition_Object((1,3,6,1,4,1,5597,10,2,7),_MbgGPSRef1GpsPosition_Type())
mbgGPSRef1GpsPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef1GpsPosition.setStatus(_A)
_MbgGPSRef1GpsSatellites_Type=DisplayString
_MbgGPSRef1GpsSatellites_Object=MibScalar
mbgGPSRef1GpsSatellites=_MbgGPSRef1GpsSatellites_Object((1,3,6,1,4,1,5597,10,2,8),_MbgGPSRef1GpsSatellites_Type())
mbgGPSRef1GpsSatellites.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef1GpsSatellites.setStatus(_A)
_MbgGPSRef1GpsSatellitesGood_Type=Integer32
_MbgGPSRef1GpsSatellitesGood_Object=MibScalar
mbgGPSRef1GpsSatellitesGood=_MbgGPSRef1GpsSatellitesGood_Object((1,3,6,1,4,1,5597,10,2,9),_MbgGPSRef1GpsSatellitesGood_Type())
mbgGPSRef1GpsSatellitesGood.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef1GpsSatellitesGood.setStatus(_A)
_MbgGPSRef1GpsSatellitesInView_Type=Integer32
_MbgGPSRef1GpsSatellitesInView_Object=MibScalar
mbgGPSRef1GpsSatellitesInView=_MbgGPSRef1GpsSatellitesInView_Object((1,3,6,1,4,1,5597,10,2,10),_MbgGPSRef1GpsSatellitesInView_Type())
mbgGPSRef1GpsSatellitesInView.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef1GpsSatellitesInView.setStatus(_A)
_MbgGPSRefclock2_ObjectIdentity=ObjectIdentity
mbgGPSRefclock2=_MbgGPSRefclock2_ObjectIdentity((1,3,6,1,4,1,5597,10,3))
_MbgGPSRefclock2Type_Type=DisplayString
_MbgGPSRefclock2Type_Object=MibScalar
mbgGPSRefclock2Type=_MbgGPSRefclock2Type_Object((1,3,6,1,4,1,5597,10,3,1),_MbgGPSRefclock2Type_Type())
mbgGPSRefclock2Type.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock2Type.setStatus(_A)
class _MbgGPSRefclock2TypeVal_Type(Integer32):defaultValue=0
_MbgGPSRefclock2TypeVal_Type.__name__=_D
_MbgGPSRefclock2TypeVal_Object=MibScalar
mbgGPSRefclock2TypeVal=_MbgGPSRefclock2TypeVal_Object((1,3,6,1,4,1,5597,10,3,2),_MbgGPSRefclock2TypeVal_Type())
mbgGPSRefclock2TypeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock2TypeVal.setStatus(_A)
_MbgGPSRefclock2Mode_Type=DisplayString
_MbgGPSRefclock2Mode_Object=MibScalar
mbgGPSRefclock2Mode=_MbgGPSRefclock2Mode_Object((1,3,6,1,4,1,5597,10,3,3),_MbgGPSRefclock2Mode_Type())
mbgGPSRefclock2Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock2Mode.setStatus(_A)
class _MbgGPSRefclock2ModeVal_Type(Integer32):defaultValue=0
_MbgGPSRefclock2ModeVal_Type.__name__=_D
_MbgGPSRefclock2ModeVal_Object=MibScalar
mbgGPSRefclock2ModeVal=_MbgGPSRefclock2ModeVal_Object((1,3,6,1,4,1,5597,10,3,4),_MbgGPSRefclock2ModeVal_Type())
mbgGPSRefclock2ModeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRefclock2ModeVal.setStatus(_A)
_MbgGPSRef2GpsState_Type=DisplayString
_MbgGPSRef2GpsState_Object=MibScalar
mbgGPSRef2GpsState=_MbgGPSRef2GpsState_Object((1,3,6,1,4,1,5597,10,3,5),_MbgGPSRef2GpsState_Type())
mbgGPSRef2GpsState.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef2GpsState.setStatus(_A)
class _MbgGPSRef2GpsStateVal_Type(Integer32):defaultValue=0
_MbgGPSRef2GpsStateVal_Type.__name__=_D
_MbgGPSRef2GpsStateVal_Object=MibScalar
mbgGPSRef2GpsStateVal=_MbgGPSRef2GpsStateVal_Object((1,3,6,1,4,1,5597,10,3,6),_MbgGPSRef2GpsStateVal_Type())
mbgGPSRef2GpsStateVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef2GpsStateVal.setStatus(_A)
_MbgGPSRef2GpsPosition_Type=DisplayString
_MbgGPSRef2GpsPosition_Object=MibScalar
mbgGPSRef2GpsPosition=_MbgGPSRef2GpsPosition_Object((1,3,6,1,4,1,5597,10,3,7),_MbgGPSRef2GpsPosition_Type())
mbgGPSRef2GpsPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef2GpsPosition.setStatus(_A)
_MbgGPSRef2GpsSatellites_Type=DisplayString
_MbgGPSRef2GpsSatellites_Object=MibScalar
mbgGPSRef2GpsSatellites=_MbgGPSRef2GpsSatellites_Object((1,3,6,1,4,1,5597,10,3,8),_MbgGPSRef2GpsSatellites_Type())
mbgGPSRef2GpsSatellites.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef2GpsSatellites.setStatus(_A)
_MbgGPSRef2GpsSatellitesGood_Type=Integer32
_MbgGPSRef2GpsSatellitesGood_Object=MibScalar
mbgGPSRef2GpsSatellitesGood=_MbgGPSRef2GpsSatellitesGood_Object((1,3,6,1,4,1,5597,10,3,9),_MbgGPSRef2GpsSatellitesGood_Type())
mbgGPSRef2GpsSatellitesGood.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef2GpsSatellitesGood.setStatus(_A)
_MbgGPSRef2GpsSatellitesInView_Type=Integer32
_MbgGPSRef2GpsSatellitesInView_Object=MibScalar
mbgGPSRef2GpsSatellitesInView=_MbgGPSRef2GpsSatellitesInView_Object((1,3,6,1,4,1,5597,10,3,10),_MbgGPSRef2GpsSatellitesInView_Type())
mbgGPSRef2GpsSatellitesInView.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSRef2GpsSatellitesInView.setStatus(_A)
_MbgSCU_ObjectIdentity=ObjectIdentity
mbgSCU=_MbgSCU_ObjectIdentity((1,3,6,1,4,1,5597,10,4))
_MbgSCUType_Type=DisplayString
_MbgSCUType_Object=MibScalar
mbgSCUType=_MbgSCUType_Object((1,3,6,1,4,1,5597,10,4,1),_MbgSCUType_Type())
mbgSCUType.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUType.setStatus(_A)
class _MbgSCUTypeVal_Type(Integer32):defaultValue=0
_MbgSCUTypeVal_Type.__name__=_D
_MbgSCUTypeVal_Object=MibScalar
mbgSCUTypeVal=_MbgSCUTypeVal_Object((1,3,6,1,4,1,5597,10,4,2),_MbgSCUTypeVal_Type())
mbgSCUTypeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUTypeVal.setStatus(_A)
_MbgSCUMaster_Type=DisplayString
_MbgSCUMaster_Object=MibScalar
mbgSCUMaster=_MbgSCUMaster_Object((1,3,6,1,4,1,5597,10,4,3),_MbgSCUMaster_Type())
mbgSCUMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUMaster.setStatus(_A)
class _MbgSCUMasterVal_Type(Integer32):defaultValue=0
_MbgSCUMasterVal_Type.__name__=_D
_MbgSCUMasterVal_Object=MibScalar
mbgSCUMasterVal=_MbgSCUMasterVal_Object((1,3,6,1,4,1,5597,10,4,4),_MbgSCUMasterVal_Type())
mbgSCUMasterVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUMasterVal.setStatus(_A)
_MbgSCUMasterselect_Type=DisplayString
_MbgSCUMasterselect_Object=MibScalar
mbgSCUMasterselect=_MbgSCUMasterselect_Object((1,3,6,1,4,1,5597,10,4,5),_MbgSCUMasterselect_Type())
mbgSCUMasterselect.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUMasterselect.setStatus(_A)
class _MbgSCUMasterselectVal_Type(Integer32):defaultValue=0
_MbgSCUMasterselectVal_Type.__name__=_D
_MbgSCUMasterselectVal_Object=MibScalar
mbgSCUMasterselectVal=_MbgSCUMasterselectVal_Object((1,3,6,1,4,1,5597,10,4,6),_MbgSCUMasterselectVal_Type())
mbgSCUMasterselectVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUMasterselectVal.setStatus(_A)
_MbgSCUTimeSync1_Type=Integer32
_MbgSCUTimeSync1_Object=MibScalar
mbgSCUTimeSync1=_MbgSCUTimeSync1_Object((1,3,6,1,4,1,5597,10,4,7),_MbgSCUTimeSync1_Type())
mbgSCUTimeSync1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUTimeSync1.setStatus(_A)
_MbgSCUTimeSync2_Type=Integer32
_MbgSCUTimeSync2_Object=MibScalar
mbgSCUTimeSync2=_MbgSCUTimeSync2_Object((1,3,6,1,4,1,5597,10,4,8),_MbgSCUTimeSync2_Type())
mbgSCUTimeSync2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUTimeSync2.setStatus(_A)
_MbgSCUTimelimitError_Type=Integer32
_MbgSCUTimelimitError_Object=MibScalar
mbgSCUTimelimitError=_MbgSCUTimelimitError_Object((1,3,6,1,4,1,5597,10,4,9),_MbgSCUTimelimitError_Type())
mbgSCUTimelimitError.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUTimelimitError.setStatus(_A)
_MbgSCUDisableOutputs_Type=Integer32
_MbgSCUDisableOutputs_Object=MibScalar
mbgSCUDisableOutputs=_MbgSCUDisableOutputs_Object((1,3,6,1,4,1,5597,10,4,10),_MbgSCUDisableOutputs_Type())
mbgSCUDisableOutputs.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUDisableOutputs.setStatus(_A)
_MbgSCUSelectedInput_Type=DisplayString
_MbgSCUSelectedInput_Object=MibScalar
mbgSCUSelectedInput=_MbgSCUSelectedInput_Object((1,3,6,1,4,1,5597,10,4,11),_MbgSCUSelectedInput_Type())
mbgSCUSelectedInput.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSelectedInput.setStatus(_A)
_MbgSCUSelectedInputVal_Type=Integer32
_MbgSCUSelectedInputVal_Object=MibScalar
mbgSCUSelectedInputVal=_MbgSCUSelectedInputVal_Object((1,3,6,1,4,1,5597,10,4,12),_MbgSCUSelectedInputVal_Type())
mbgSCUSelectedInputVal.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSelectedInputVal.setStatus(_A)
_MbgSCUACOMode_Type=Integer32
_MbgSCUACOMode_Object=MibScalar
mbgSCUACOMode=_MbgSCUACOMode_Object((1,3,6,1,4,1,5597,10,4,13),_MbgSCUACOMode_Type())
mbgSCUACOMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUACOMode.setStatus(_A)
_MbgSCUPSUStatus_Type=DisplayString
_MbgSCUPSUStatus_Object=MibScalar
mbgSCUPSUStatus=_MbgSCUPSUStatus_Object((1,3,6,1,4,1,5597,10,4,14),_MbgSCUPSUStatus_Type())
mbgSCUPSUStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUPSUStatus.setStatus(_A)
_MbgSCUPSU1Status_Type=Integer32
_MbgSCUPSU1Status_Object=MibScalar
mbgSCUPSU1Status=_MbgSCUPSU1Status_Object((1,3,6,1,4,1,5597,10,4,15),_MbgSCUPSU1Status_Type())
mbgSCUPSU1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUPSU1Status.setStatus(_A)
_MbgSCUPSU2Status_Type=Integer32
_MbgSCUPSU2Status_Object=MibScalar
mbgSCUPSU2Status=_MbgSCUPSU2Status_Object((1,3,6,1,4,1,5597,10,4,16),_MbgSCUPSU2Status_Type())
mbgSCUPSU2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUPSU2Status.setStatus(_A)
_MbgXPTTraps_ObjectIdentity=ObjectIdentity
mbgXPTTraps=_MbgXPTTraps_ObjectIdentity((1,3,6,1,4,1,5597,10,5))
_MbgXPTConformance_ObjectIdentity=ObjectIdentity
mbgXPTConformance=_MbgXPTConformance_ObjectIdentity((1,3,6,1,4,1,5597,10,90))
_MbgXPTCompliances_ObjectIdentity=ObjectIdentity
mbgXPTCompliances=_MbgXPTCompliances_ObjectIdentity((1,3,6,1,4,1,5597,10,90,1))
_MbgXPTGroups_ObjectIdentity=ObjectIdentity
mbgXPTGroups=_MbgXPTGroups_ObjectIdentity((1,3,6,1,4,1,5597,10,90,2))
mbgXPTObjectsGroup=ObjectGroup((1,3,6,1,4,1,5597,10,90,2,1))
mbgXPTObjectsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:mbgXPTObjectsGroup.setStatus(_A)
mbgGPSTrapColdBoot=NotificationType((1,3,6,1,4,1,5597,10,5,1))
if mibBuilder.loadTexts:mbgGPSTrapColdBoot.setStatus(_A)
mbgGPSTrapWarmBoot=NotificationType((1,3,6,1,4,1,5597,10,5,2))
if mibBuilder.loadTexts:mbgGPSTrapWarmBoot.setStatus(_A)
mbgGPSNavSolved=NotificationType((1,3,6,1,4,1,5597,10,5,3))
if mibBuilder.loadTexts:mbgGPSNavSolved.setStatus(_A)
mbgGPSTrapReceiverNotResponding=NotificationType((1,3,6,1,4,1,5597,10,5,4))
if mibBuilder.loadTexts:mbgGPSTrapReceiverNotResponding.setStatus(_A)
mbgGPSTrapReceiverNotSync=NotificationType((1,3,6,1,4,1,5597,10,5,5))
if mibBuilder.loadTexts:mbgGPSTrapReceiverNotSync.setStatus(_A)
mbgGPSTrapAntennaFaulty=NotificationType((1,3,6,1,4,1,5597,10,5,6))
if mibBuilder.loadTexts:mbgGPSTrapAntennaFaulty.setStatus(_A)
mbgGPSTrapAntennaReconnect=NotificationType((1,3,6,1,4,1,5597,10,5,7))
if mibBuilder.loadTexts:mbgGPSTrapAntennaReconnect.setStatus(_A)
mbgGPSTrapLANXPTBoot=NotificationType((1,3,6,1,4,1,5597,10,5,8))
if mibBuilder.loadTexts:mbgGPSTrapLANXPTBoot.setStatus(_A)
mbgGPSTrapLeapSecondAnnounced=NotificationType((1,3,6,1,4,1,5597,10,5,9))
if mibBuilder.loadTexts:mbgGPSTrapLeapSecondAnnounced.setStatus(_A)
mbgGPSTrapMasterclockSwitchover=NotificationType((1,3,6,1,4,1,5597,10,5,10))
if mibBuilder.loadTexts:mbgGPSTrapMasterclockSwitchover.setStatus(_A)
mbgGPSTrapPowerSupplyFailure=NotificationType((1,3,6,1,4,1,5597,10,5,11))
if mibBuilder.loadTexts:mbgGPSTrapPowerSupplyFailure.setStatus(_A)
mbgGPSTrapPowerSupplyOK=NotificationType((1,3,6,1,4,1,5597,10,5,12))
if mibBuilder.loadTexts:mbgGPSTrapPowerSupplyOK.setStatus(_A)
mbgGPSTrapTestNotification=NotificationType((1,3,6,1,4,1,5597,10,5,99))
if mibBuilder.loadTexts:mbgGPSTrapTestNotification.setStatus(_A)
mbgXPTTrapsGroup=NotificationGroup((1,3,6,1,4,1,5597,10,90,2,2))
mbgXPTTrapsGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:mbgXPTTrapsGroup.setStatus(_A)
mbgXPTCompliance=ModuleCompliance((1,3,6,1,4,1,5597,10,90,1,1))
mbgXPTCompliance.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:mbgXPTCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mbgXPT':mbgXPT,'mbgGPSRefclock1':mbgGPSRefclock1,_E:mbgGPSRefclock1Type,_F:mbgGPSRefclock1TypeVal,_G:mbgGPSRefclock1Mode,_H:mbgGPSRefclock1ModeVal,_I:mbgGPSRef1GpsState,_J:mbgGPSRef1GpsStateVal,_K:mbgGPSRef1GpsPosition,_L:mbgGPSRef1GpsSatellites,_M:mbgGPSRef1GpsSatellitesGood,_N:mbgGPSRef1GpsSatellitesInView,'mbgGPSRefclock2':mbgGPSRefclock2,_O:mbgGPSRefclock2Type,_P:mbgGPSRefclock2TypeVal,_Q:mbgGPSRefclock2Mode,_R:mbgGPSRefclock2ModeVal,_S:mbgGPSRef2GpsState,_T:mbgGPSRef2GpsStateVal,_U:mbgGPSRef2GpsPosition,_V:mbgGPSRef2GpsSatellites,_W:mbgGPSRef2GpsSatellitesGood,_X:mbgGPSRef2GpsSatellitesInView,'mbgSCU':mbgSCU,_Y:mbgSCUType,_Z:mbgSCUTypeVal,_a:mbgSCUMaster,_b:mbgSCUMasterVal,_c:mbgSCUMasterselect,_d:mbgSCUMasterselectVal,_e:mbgSCUTimeSync1,_f:mbgSCUTimeSync2,_g:mbgSCUTimelimitError,_h:mbgSCUDisableOutputs,_i:mbgSCUSelectedInput,_j:mbgSCUSelectedInputVal,_k:mbgSCUACOMode,_l:mbgSCUPSUStatus,_m:mbgSCUPSU1Status,_n:mbgSCUPSU2Status,'mbgXPTTraps':mbgXPTTraps,_o:mbgGPSTrapColdBoot,_p:mbgGPSTrapWarmBoot,_q:mbgGPSNavSolved,_r:mbgGPSTrapReceiverNotResponding,_s:mbgGPSTrapReceiverNotSync,_t:mbgGPSTrapAntennaFaulty,_u:mbgGPSTrapAntennaReconnect,_v:mbgGPSTrapLANXPTBoot,_w:mbgGPSTrapLeapSecondAnnounced,_x:mbgGPSTrapMasterclockSwitchover,_y:mbgGPSTrapPowerSupplyFailure,_z:mbgGPSTrapPowerSupplyOK,_A0:mbgGPSTrapTestNotification,'mbgXPTConformance':mbgXPTConformance,'mbgXPTCompliances':mbgXPTCompliances,'mbgXPTCompliance':mbgXPTCompliance,'mbgXPTGroups':mbgXPTGroups,_A1:mbgXPTObjectsGroup,_A2:mbgXPTTrapsGroup})