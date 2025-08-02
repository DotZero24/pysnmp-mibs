_A9='cpqWcrmWaterCoolUnitStatus'
_A8='cpqWcrmWaterCoolUnitText'
_A7='cpqWcrmInternalStatus'
_A6='cpqWcrmInternalText'
_A5='waterCoolUnitSensorValue'
_A4='waterCoolUnitMsgStatus'
_A3='waterCoolUnitMsgText'
_A2='internalSensorValue'
_A1='internalMsgStatus'
_A0='internalMsgText'
_z='trapIndex'
_y='cpqWcrmTimerIndex'
_x='waterCoolUnitOutputIndex'
_w='waterCoolUnitSensorIndex'
_v='manual'
_u='enRemote'
_t='disRemote'
_s='unlockDelay'
_r='unlock'
_q='internalOutputIndex'
_p='internalSensorIndex'
_o='lowPower'
_n='detected'
_m='timeout'
_l='unitIO'
_k='unitWcrm'
_j='failed'
_i='NotificationType'
_h='enabled'
_g='disabled'
_f='waterCoolUnitMsgIndex'
_e='alarm'
_d='internalMsgIndex'
_c='overflow'
_b='failure'
_a='reset'
_Z='configChanged'
_Y='setOn'
_X='setOff'
_W='tooHigh'
_V='tooLow'
_U='lost'
_T='error'
_S='warning'
_R='cpqWcrmURL'
_Q='changed'
_P='sysName'
_O='sysLocation'
_N='sysContact'
_M='on'
_L='ok'
_K='off'
_J='enable'
_I='disable'
_H='notAvail'
_G='DisplayString'
_F='SNMPv2-MIB'
_E='CPQWCRM-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysContact,sysLocation,sysName=mibBuilder.importSymbols(_F,_N,_O,_P)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_i,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_i,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_CpqWcrm_ObjectIdentity=ObjectIdentity
cpqWcrm=_CpqWcrm_ObjectIdentity((1,3,6,1,4,1,232,167))
_CpqWcrmMibRev_ObjectIdentity=ObjectIdentity
cpqWcrmMibRev=_CpqWcrmMibRev_ObjectIdentity((1,3,6,1,4,1,232,167,1))
class _CpqWcrmMibMajRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqWcrmMibMajRev_Type.__name__=_B
_CpqWcrmMibMajRev_Object=MibScalar
cpqWcrmMibMajRev=_CpqWcrmMibMajRev_Object((1,3,6,1,4,1,232,167,1,1),_CpqWcrmMibMajRev_Type())
cpqWcrmMibMajRev.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmMibMajRev.setStatus(_A)
class _CpqWcrmMibMinRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqWcrmMibMinRev_Type.__name__=_B
_CpqWcrmMibMinRev_Object=MibScalar
cpqWcrmMibMinRev=_CpqWcrmMibMinRev_Object((1,3,6,1,4,1,232,167,1,2),_CpqWcrmMibMinRev_Type())
cpqWcrmMibMinRev.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmMibMinRev.setStatus(_A)
class _CpqWcrmMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_L,2),('degraded',3),(_j,4),(_Z,5)))
_CpqWcrmMibCondition_Type.__name__=_B
_CpqWcrmMibCondition_Object=MibScalar
cpqWcrmMibCondition=_CpqWcrmMibCondition_Object((1,3,6,1,4,1,232,167,1,3),_CpqWcrmMibCondition_Type())
cpqWcrmMibCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmMibCondition.setStatus(_A)
_CpqWcrmStatus_ObjectIdentity=ObjectIdentity
cpqWcrmStatus=_CpqWcrmStatus_ObjectIdentity((1,3,6,1,4,1,232,167,2))
class _CpqWcrmStatusDeviceEnvironmentalController_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_L,2)))
_CpqWcrmStatusDeviceEnvironmentalController_Type.__name__=_B
_CpqWcrmStatusDeviceEnvironmentalController_Object=MibScalar
cpqWcrmStatusDeviceEnvironmentalController=_CpqWcrmStatusDeviceEnvironmentalController_Object((1,3,6,1,4,1,232,167,2,1),_CpqWcrmStatusDeviceEnvironmentalController_Type())
cpqWcrmStatusDeviceEnvironmentalController.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmStatusDeviceEnvironmentalController.setStatus(_A)
_CpqWcrmUnitsConnected_Type=Integer32
_CpqWcrmUnitsConnected_Object=MibScalar
cpqWcrmUnitsConnected=_CpqWcrmUnitsConnected_Object((1,3,6,1,4,1,232,167,2,2),_CpqWcrmUnitsConnected_Type())
cpqWcrmUnitsConnected.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmUnitsConnected.setStatus(_A)
_CpqWcrmStatusSensorInternal_ObjectIdentity=ObjectIdentity
cpqWcrmStatusSensorInternal=_CpqWcrmStatusSensorInternal_ObjectIdentity((1,3,6,1,4,1,232,167,2,3))
class _CpqWcrmInternalTypeOfDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_k,2),(_l,3)))
_CpqWcrmInternalTypeOfDevice_Type.__name__=_B
_CpqWcrmInternalTypeOfDevice_Object=MibScalar
cpqWcrmInternalTypeOfDevice=_CpqWcrmInternalTypeOfDevice_Object((1,3,6,1,4,1,232,167,2,3,1),_CpqWcrmInternalTypeOfDevice_Type())
cpqWcrmInternalTypeOfDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmInternalTypeOfDevice.setStatus(_A)
class _CpqWcrmInternalText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CpqWcrmInternalText_Type.__name__=_G
_CpqWcrmInternalText_Object=MibScalar
cpqWcrmInternalText=_CpqWcrmInternalText_Object((1,3,6,1,4,1,232,167,2,3,2),_CpqWcrmInternalText_Type())
cpqWcrmInternalText.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmInternalText.setStatus(_A)
_CpqWcrmInternalSerial_Type=Integer32
_CpqWcrmInternalSerial_Object=MibScalar
cpqWcrmInternalSerial=_CpqWcrmInternalSerial_Object((1,3,6,1,4,1,232,167,2,3,3),_CpqWcrmInternalSerial_Type())
cpqWcrmInternalSerial.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmInternalSerial.setStatus(_A)
class _CpqWcrmInternalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_T,2),(_Q,3),(_a,4),(_m,5),(_n,6),(_H,7),(_o,8)))
_CpqWcrmInternalStatus_Type.__name__=_B
_CpqWcrmInternalStatus_Object=MibScalar
cpqWcrmInternalStatus=_CpqWcrmInternalStatus_Object((1,3,6,1,4,1,232,167,2,3,4),_CpqWcrmInternalStatus_Type())
cpqWcrmInternalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmInternalStatus.setStatus(_A)
_CpqWcrmStatusInternalSensors_ObjectIdentity=ObjectIdentity
cpqWcrmStatusInternalSensors=_CpqWcrmStatusInternalSensors_ObjectIdentity((1,3,6,1,4,1,232,167,2,3,5))
_CpqWcrmInternalNumberOfSensors_Type=Integer32
_CpqWcrmInternalNumberOfSensors_Object=MibScalar
cpqWcrmInternalNumberOfSensors=_CpqWcrmInternalNumberOfSensors_Object((1,3,6,1,4,1,232,167,2,3,5,1),_CpqWcrmInternalNumberOfSensors_Type())
cpqWcrmInternalNumberOfSensors.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmInternalNumberOfSensors.setStatus(_A)
_CpqWcrmInternalSensorTable_Object=MibTable
cpqWcrmInternalSensorTable=_CpqWcrmInternalSensorTable_Object((1,3,6,1,4,1,232,167,2,3,5,2))
if mibBuilder.loadTexts:cpqWcrmInternalSensorTable.setStatus(_A)
_CpqWcrmInternalSensorEntry_Object=MibTableRow
cpqWcrmInternalSensorEntry=_CpqWcrmInternalSensorEntry_Object((1,3,6,1,4,1,232,167,2,3,5,2,1))
cpqWcrmInternalSensorEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:cpqWcrmInternalSensorEntry.setStatus(_A)
class _InternalSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_InternalSensorIndex_Type.__name__=_B
_InternalSensorIndex_Object=MibTableColumn
internalSensorIndex=_InternalSensorIndex_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,1),_InternalSensorIndex_Type())
internalSensorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:internalSensorIndex.setStatus(_A)
class _InternalSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,19,20)));namedValues=NamedValues(*((_H,1),(_b,2),(_c,3),('access',4),('vibration',5),('motion',6),('smoke',7),('airFlow',8),('type6',9),('temperature',10),('current4to20',11),('humidity',12),('userNO',13),('userNC',14),('voltOK',17),('voltage',18),('fanOK',19),('leakage',20)))
_InternalSensorType_Type.__name__=_B
_InternalSensorType_Object=MibTableColumn
internalSensorType=_InternalSensorType_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,2),_InternalSensorType_Type())
internalSensorType.setMaxAccess(_D)
if mibBuilder.loadTexts:internalSensorType.setStatus(_A)
class _InternalSensorText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_InternalSensorText_Type.__name__=_G
_InternalSensorText_Object=MibTableColumn
internalSensorText=_InternalSensorText_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,3),_InternalSensorText_Type())
internalSensorText.setMaxAccess(_C)
if mibBuilder.loadTexts:internalSensorText.setStatus(_A)
class _InternalSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),(_U,2),(_Q,3),(_L,4),(_K,5),(_M,6),(_S,7),(_V,8),(_W,9)))
_InternalSensorStatus_Type.__name__=_B
_InternalSensorStatus_Object=MibTableColumn
internalSensorStatus=_InternalSensorStatus_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,4),_InternalSensorStatus_Type())
internalSensorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:internalSensorStatus.setStatus(_A)
_InternalSensorValue_Type=Integer32
_InternalSensorValue_Object=MibTableColumn
internalSensorValue=_InternalSensorValue_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,5),_InternalSensorValue_Type())
internalSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:internalSensorValue.setStatus(_A)
_InternalSensorSetHigh_Type=Integer32
_InternalSensorSetHigh_Object=MibTableColumn
internalSensorSetHigh=_InternalSensorSetHigh_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,6),_InternalSensorSetHigh_Type())
internalSensorSetHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:internalSensorSetHigh.setStatus(_A)
_InternalSensorSetLow_Type=Integer32
_InternalSensorSetLow_Object=MibTableColumn
internalSensorSetLow=_InternalSensorSetLow_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,7),_InternalSensorSetLow_Type())
internalSensorSetLow.setMaxAccess(_C)
if mibBuilder.loadTexts:internalSensorSetLow.setStatus(_A)
_InternalSensorSetWarn_Type=Integer32
_InternalSensorSetWarn_Object=MibTableColumn
internalSensorSetWarn=_InternalSensorSetWarn_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,8),_InternalSensorSetWarn_Type())
internalSensorSetWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:internalSensorSetWarn.setStatus(_A)
_InternalSensorValueScale_Type=Integer32
_InternalSensorValueScale_Object=MibTableColumn
internalSensorValueScale=_InternalSensorValueScale_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,9),_InternalSensorValueScale_Type())
internalSensorValueScale.setMaxAccess(_D)
if mibBuilder.loadTexts:internalSensorValueScale.setStatus(_A)
_InternalSensorScaledValue_Type=Integer32
_InternalSensorScaledValue_Object=MibTableColumn
internalSensorScaledValue=_InternalSensorScaledValue_Object((1,3,6,1,4,1,232,167,2,3,5,2,1,10),_InternalSensorScaledValue_Type())
internalSensorScaledValue.setMaxAccess(_D)
if mibBuilder.loadTexts:internalSensorScaledValue.setStatus(_A)
_CpqWcrmStatusInternalOutputs_ObjectIdentity=ObjectIdentity
cpqWcrmStatusInternalOutputs=_CpqWcrmStatusInternalOutputs_ObjectIdentity((1,3,6,1,4,1,232,167,2,3,6))
_CpqWcrmInternalNumberOfOutputs_Type=Integer32
_CpqWcrmInternalNumberOfOutputs_Object=MibScalar
cpqWcrmInternalNumberOfOutputs=_CpqWcrmInternalNumberOfOutputs_Object((1,3,6,1,4,1,232,167,2,3,6,1),_CpqWcrmInternalNumberOfOutputs_Type())
cpqWcrmInternalNumberOfOutputs.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmInternalNumberOfOutputs.setStatus(_A)
_CpqWcrmInternalOutputTable_Object=MibTable
cpqWcrmInternalOutputTable=_CpqWcrmInternalOutputTable_Object((1,3,6,1,4,1,232,167,2,3,6,2))
if mibBuilder.loadTexts:cpqWcrmInternalOutputTable.setStatus(_A)
_CpqWcrmInternalOutputEntry_Object=MibTableRow
cpqWcrmInternalOutputEntry=_CpqWcrmInternalOutputEntry_Object((1,3,6,1,4,1,232,167,2,3,6,2,1))
cpqWcrmInternalOutputEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:cpqWcrmInternalOutputEntry.setStatus(_A)
class _InternalOutputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_InternalOutputIndex_Type.__name__=_B
_InternalOutputIndex_Object=MibTableColumn
internalOutputIndex=_InternalOutputIndex_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,1),_InternalOutputIndex_Type())
internalOutputIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:internalOutputIndex.setStatus(_A)
class _InternalOutputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_b,2),(_c,3),('universalOut',4),('powerOut',5)))
_InternalOutputType_Type.__name__=_B
_InternalOutputType_Object=MibTableColumn
internalOutputType=_InternalOutputType_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,2),_InternalOutputType_Type())
internalOutputType.setMaxAccess(_D)
if mibBuilder.loadTexts:internalOutputType.setStatus(_A)
class _InternalOutputText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_InternalOutputText_Type.__name__=_G
_InternalOutputText_Object=MibTableColumn
internalOutputText=_InternalOutputText_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,3),_InternalOutputText_Type())
internalOutputText.setMaxAccess(_C)
if mibBuilder.loadTexts:internalOutputText.setStatus(_A)
class _InternalOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,1),(_U,2),(_Q,3),(_L,4),(_K,5),(_M,6),(_X,7),(_Y,8)))
_InternalOutputStatus_Type.__name__=_B
_InternalOutputStatus_Object=MibTableColumn
internalOutputStatus=_InternalOutputStatus_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,4),_InternalOutputStatus_Type())
internalOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:internalOutputStatus.setStatus(_A)
_InternalOutputValue_Type=Integer32
_InternalOutputValue_Object=MibTableColumn
internalOutputValue=_InternalOutputValue_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,5),_InternalOutputValue_Type())
internalOutputValue.setMaxAccess(_C)
if mibBuilder.loadTexts:internalOutputValue.setStatus(_A)
class _InternalOutputSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_M,2),('lock',3),(_r,4),(_s,5)))
_InternalOutputSet_Type.__name__=_B
_InternalOutputSet_Object=MibTableColumn
internalOutputSet=_InternalOutputSet_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,6),_InternalOutputSet_Type())
internalOutputSet.setMaxAccess(_C)
if mibBuilder.loadTexts:internalOutputSet.setStatus(_A)
class _InternalOutputConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),(_u,2)))
_InternalOutputConfig_Type.__name__=_B
_InternalOutputConfig_Object=MibTableColumn
internalOutputConfig=_InternalOutputConfig_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,7),_InternalOutputConfig_Type())
internalOutputConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:internalOutputConfig.setStatus(_A)
_InternalOutputDelay_Type=Integer32
_InternalOutputDelay_Object=MibTableColumn
internalOutputDelay=_InternalOutputDelay_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,8),_InternalOutputDelay_Type())
internalOutputDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:internalOutputDelay.setStatus(_A)
class _InternalOutputTimeoutAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stay',1),(_K,2),(_M,3)))
_InternalOutputTimeoutAction_Type.__name__=_B
_InternalOutputTimeoutAction_Object=MibTableColumn
internalOutputTimeoutAction=_InternalOutputTimeoutAction_Object((1,3,6,1,4,1,232,167,2,3,6,2,1,9),_InternalOutputTimeoutAction_Type())
internalOutputTimeoutAction.setMaxAccess(_C)
if mibBuilder.loadTexts:internalOutputTimeoutAction.setStatus(_A)
_CpqWcrmStatusInternalMsg_ObjectIdentity=ObjectIdentity
cpqWcrmStatusInternalMsg=_CpqWcrmStatusInternalMsg_ObjectIdentity((1,3,6,1,4,1,232,167,2,3,7))
_CpqWcrmInternalNumberOfMsgs_Type=Integer32
_CpqWcrmInternalNumberOfMsgs_Object=MibScalar
cpqWcrmInternalNumberOfMsgs=_CpqWcrmInternalNumberOfMsgs_Object((1,3,6,1,4,1,232,167,2,3,7,1),_CpqWcrmInternalNumberOfMsgs_Type())
cpqWcrmInternalNumberOfMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmInternalNumberOfMsgs.setStatus(_A)
_CpqWcrmInternalMsgTable_Object=MibTable
cpqWcrmInternalMsgTable=_CpqWcrmInternalMsgTable_Object((1,3,6,1,4,1,232,167,2,3,7,2))
if mibBuilder.loadTexts:cpqWcrmInternalMsgTable.setStatus(_A)
_CpqWcrmInternalMsgEntry_Object=MibTableRow
cpqWcrmInternalMsgEntry=_CpqWcrmInternalMsgEntry_Object((1,3,6,1,4,1,232,167,2,3,7,2,1))
cpqWcrmInternalMsgEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:cpqWcrmInternalMsgEntry.setStatus(_A)
class _InternalMsgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_InternalMsgIndex_Type.__name__=_B
_InternalMsgIndex_Object=MibTableColumn
internalMsgIndex=_InternalMsgIndex_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,1),_InternalMsgIndex_Type())
internalMsgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:internalMsgIndex.setStatus(_A)
class _InternalMsgText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_InternalMsgText_Type.__name__=_G
_InternalMsgText_Object=MibTableColumn
internalMsgText=_InternalMsgText_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,2),_InternalMsgText_Type())
internalMsgText.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgText.setStatus(_A)
class _InternalMsgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),(_Z,2),(_T,3),(_L,4),(_e,5),(_S,6),(_V,7),(_W,8),(_X,9),(_Y,10)))
_InternalMsgStatus_Type.__name__=_B
_InternalMsgStatus_Object=MibTableColumn
internalMsgStatus=_InternalMsgStatus_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,3),_InternalMsgStatus_Type())
internalMsgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:internalMsgStatus.setStatus(_A)
class _InternalMsgRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_InternalMsgRelay_Type.__name__=_B
_InternalMsgRelay_Object=MibTableColumn
internalMsgRelay=_InternalMsgRelay_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,4),_InternalMsgRelay_Type())
internalMsgRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgRelay.setStatus(_A)
class _InternalMsgBeeper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_InternalMsgBeeper_Type.__name__=_B
_InternalMsgBeeper_Object=MibTableColumn
internalMsgBeeper=_InternalMsgBeeper_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,5),_InternalMsgBeeper_Type())
internalMsgBeeper.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgBeeper.setStatus(_A)
class _InternalMsgTrap1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_InternalMsgTrap1_Type.__name__=_B
_InternalMsgTrap1_Object=MibTableColumn
internalMsgTrap1=_InternalMsgTrap1_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,6),_InternalMsgTrap1_Type())
internalMsgTrap1.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgTrap1.setStatus(_A)
class _InternalMsgTrap2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_InternalMsgTrap2_Type.__name__=_B
_InternalMsgTrap2_Object=MibTableColumn
internalMsgTrap2=_InternalMsgTrap2_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,7),_InternalMsgTrap2_Type())
internalMsgTrap2.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgTrap2.setStatus(_A)
class _InternalMsgTrap3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_InternalMsgTrap3_Type.__name__=_B
_InternalMsgTrap3_Object=MibTableColumn
internalMsgTrap3=_InternalMsgTrap3_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,8),_InternalMsgTrap3_Type())
internalMsgTrap3.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgTrap3.setStatus(_A)
class _InternalMsgTrap4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_InternalMsgTrap4_Type.__name__=_B
_InternalMsgTrap4_Object=MibTableColumn
internalMsgTrap4=_InternalMsgTrap4_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,9),_InternalMsgTrap4_Type())
internalMsgTrap4.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgTrap4.setStatus(_A)
class _InternalMsgReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_v,2)))
_InternalMsgReset_Type.__name__=_B
_InternalMsgReset_Object=MibTableColumn
internalMsgReset=_InternalMsgReset_Object((1,3,6,1,4,1,232,167,2,3,7,2,1,10),_InternalMsgReset_Type())
internalMsgReset.setMaxAccess(_C)
if mibBuilder.loadTexts:internalMsgReset.setStatus(_A)
_CpqWcrmStatusSensorWaterCoolUnit_ObjectIdentity=ObjectIdentity
cpqWcrmStatusSensorWaterCoolUnit=_CpqWcrmStatusSensorWaterCoolUnit_ObjectIdentity((1,3,6,1,4,1,232,167,2,4))
class _CpqWcrmWaterCoolUnitTypeOfDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_k,2),(_l,3)))
_CpqWcrmWaterCoolUnitTypeOfDevice_Type.__name__=_B
_CpqWcrmWaterCoolUnitTypeOfDevice_Object=MibScalar
cpqWcrmWaterCoolUnitTypeOfDevice=_CpqWcrmWaterCoolUnitTypeOfDevice_Object((1,3,6,1,4,1,232,167,2,4,1),_CpqWcrmWaterCoolUnitTypeOfDevice_Type())
cpqWcrmWaterCoolUnitTypeOfDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitTypeOfDevice.setStatus(_A)
class _CpqWcrmWaterCoolUnitText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CpqWcrmWaterCoolUnitText_Type.__name__=_G
_CpqWcrmWaterCoolUnitText_Object=MibScalar
cpqWcrmWaterCoolUnitText=_CpqWcrmWaterCoolUnitText_Object((1,3,6,1,4,1,232,167,2,4,2),_CpqWcrmWaterCoolUnitText_Type())
cpqWcrmWaterCoolUnitText.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitText.setStatus(_A)
_CpqWcrmWaterCoolUnitSerial_Type=Integer32
_CpqWcrmWaterCoolUnitSerial_Object=MibScalar
cpqWcrmWaterCoolUnitSerial=_CpqWcrmWaterCoolUnitSerial_Object((1,3,6,1,4,1,232,167,2,4,3),_CpqWcrmWaterCoolUnitSerial_Type())
cpqWcrmWaterCoolUnitSerial.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitSerial.setStatus(_A)
class _CpqWcrmWaterCoolUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_T,2),(_Q,3),(_a,4),(_m,5),(_n,6),(_H,7),(_o,8)))
_CpqWcrmWaterCoolUnitStatus_Type.__name__=_B
_CpqWcrmWaterCoolUnitStatus_Object=MibScalar
cpqWcrmWaterCoolUnitStatus=_CpqWcrmWaterCoolUnitStatus_Object((1,3,6,1,4,1,232,167,2,4,4),_CpqWcrmWaterCoolUnitStatus_Type())
cpqWcrmWaterCoolUnitStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitStatus.setStatus(_A)
_CpqWcrmStatusWaterCoolUnitSensors_ObjectIdentity=ObjectIdentity
cpqWcrmStatusWaterCoolUnitSensors=_CpqWcrmStatusWaterCoolUnitSensors_ObjectIdentity((1,3,6,1,4,1,232,167,2,4,5))
_CpqWcrmWaterCoolUnitNumberOfSensors_Type=Integer32
_CpqWcrmWaterCoolUnitNumberOfSensors_Object=MibScalar
cpqWcrmWaterCoolUnitNumberOfSensors=_CpqWcrmWaterCoolUnitNumberOfSensors_Object((1,3,6,1,4,1,232,167,2,4,5,1),_CpqWcrmWaterCoolUnitNumberOfSensors_Type())
cpqWcrmWaterCoolUnitNumberOfSensors.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitNumberOfSensors.setStatus(_A)
_CpqWcrmWaterCoolUnitSensorTable_Object=MibTable
cpqWcrmWaterCoolUnitSensorTable=_CpqWcrmWaterCoolUnitSensorTable_Object((1,3,6,1,4,1,232,167,2,4,5,2))
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitSensorTable.setStatus(_A)
_CpqWcrmWaterCoolUnitSensorEntry_Object=MibTableRow
cpqWcrmWaterCoolUnitSensorEntry=_CpqWcrmWaterCoolUnitSensorEntry_Object((1,3,6,1,4,1,232,167,2,4,5,2,1))
cpqWcrmWaterCoolUnitSensorEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitSensorEntry.setStatus(_A)
class _WaterCoolUnitSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WaterCoolUnitSensorIndex_Type.__name__=_B
_WaterCoolUnitSensorIndex_Object=MibTableColumn
waterCoolUnitSensorIndex=_WaterCoolUnitSensorIndex_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,1),_WaterCoolUnitSensorIndex_Type())
waterCoolUnitSensorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitSensorIndex.setStatus(_A)
class _WaterCoolUnitSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65)));namedValues=NamedValues(*(('tempIn',4),('tempOut',5),('heatFlow',6),(_e,7),(_S,8),('rpmFan1',9),('rpmFan2',10),('rpmFan3',11),('fanSpeed',12),('tempIn1',13),('tempOut1',14),('tempIn2',15),('tempOut2',16),('tempIn3',17),('tempOut3',18),('tempWaterIn',19),('tempWaterOut',20),('waterFlow',21),('valve',22),('status',23),('condensateDuration',24),('condensateCycles',25),('rpmFan4',26),('rpmFan5',27),('rpmFan6',28),('transfSwitch',29),('valveActValue',30),('dewPointValue',31),('foundFans',32),('isolationValveInlet',33),('isolationValveFacility',34),('isolationValveInfrastructure',35),('controlValveFacility',36),('controlValveInfrastructure',37),('tempIn4',38),('tempIn5',39),('tempIn6',40),('waterPressureSupply',41),('waterPressureReturn',42),('airDiffPressure1',43),('airDiffPressure2',44),('acInput1',45),('acInput2',46),('frontDoor',47),('rearDoor',48),('leakMidLevel',49),('leakOverflow1',50),('leakOverflow2',51),('condensate',52),('dewPointValue2',53),('humidityValue',54),('humidityValue2',55),('pump',56),('tempeValue1',57),('tempeValue2',58),('dewPointAverage',59),('percentFan1',60),('percentFan2',61),('percentFan3',62),('percentFan4',63),('percentFan5',64),('percentFan6',65)))
_WaterCoolUnitSensorType_Type.__name__=_B
_WaterCoolUnitSensorType_Object=MibTableColumn
waterCoolUnitSensorType=_WaterCoolUnitSensorType_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,2),_WaterCoolUnitSensorType_Type())
waterCoolUnitSensorType.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitSensorType.setStatus(_A)
class _WaterCoolUnitSensorText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_WaterCoolUnitSensorText_Type.__name__=_G
_WaterCoolUnitSensorText_Object=MibTableColumn
waterCoolUnitSensorText=_WaterCoolUnitSensorText_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,3),_WaterCoolUnitSensorText_Type())
waterCoolUnitSensorText.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitSensorText.setStatus(_A)
class _WaterCoolUnitSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),(_U,2),(_Q,3),(_L,4),(_K,5),(_M,6),(_S,7),(_V,8),(_W,9)))
_WaterCoolUnitSensorStatus_Type.__name__=_B
_WaterCoolUnitSensorStatus_Object=MibTableColumn
waterCoolUnitSensorStatus=_WaterCoolUnitSensorStatus_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,4),_WaterCoolUnitSensorStatus_Type())
waterCoolUnitSensorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitSensorStatus.setStatus(_A)
_WaterCoolUnitSensorValue_Type=Integer32
_WaterCoolUnitSensorValue_Object=MibTableColumn
waterCoolUnitSensorValue=_WaterCoolUnitSensorValue_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,5),_WaterCoolUnitSensorValue_Type())
waterCoolUnitSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitSensorValue.setStatus(_A)
_WaterCoolUnitSensorSetHigh_Type=Integer32
_WaterCoolUnitSensorSetHigh_Object=MibTableColumn
waterCoolUnitSensorSetHigh=_WaterCoolUnitSensorSetHigh_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,6),_WaterCoolUnitSensorSetHigh_Type())
waterCoolUnitSensorSetHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitSensorSetHigh.setStatus(_A)
_WaterCoolUnitSensorSetLow_Type=Integer32
_WaterCoolUnitSensorSetLow_Object=MibTableColumn
waterCoolUnitSensorSetLow=_WaterCoolUnitSensorSetLow_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,7),_WaterCoolUnitSensorSetLow_Type())
waterCoolUnitSensorSetLow.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitSensorSetLow.setStatus(_A)
_WaterCoolUnitSensorSetWarn_Type=Integer32
_WaterCoolUnitSensorSetWarn_Object=MibTableColumn
waterCoolUnitSensorSetWarn=_WaterCoolUnitSensorSetWarn_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,8),_WaterCoolUnitSensorSetWarn_Type())
waterCoolUnitSensorSetWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitSensorSetWarn.setStatus(_A)
_WaterCoolUnitSensorValueScale_Type=Integer32
_WaterCoolUnitSensorValueScale_Object=MibTableColumn
waterCoolUnitSensorValueScale=_WaterCoolUnitSensorValueScale_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,9),_WaterCoolUnitSensorValueScale_Type())
waterCoolUnitSensorValueScale.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitSensorValueScale.setStatus(_A)
_WaterCoolUnitSensorScaledValue_Type=Integer32
_WaterCoolUnitSensorScaledValue_Object=MibTableColumn
waterCoolUnitSensorScaledValue=_WaterCoolUnitSensorScaledValue_Object((1,3,6,1,4,1,232,167,2,4,5,2,1,10),_WaterCoolUnitSensorScaledValue_Type())
waterCoolUnitSensorScaledValue.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitSensorScaledValue.setStatus(_A)
_CpqWcrmStatusWaterCoolUnitOutputs_ObjectIdentity=ObjectIdentity
cpqWcrmStatusWaterCoolUnitOutputs=_CpqWcrmStatusWaterCoolUnitOutputs_ObjectIdentity((1,3,6,1,4,1,232,167,2,4,6))
_CpqWcrmWaterCoolUnitNumberOfOutputs_Type=Integer32
_CpqWcrmWaterCoolUnitNumberOfOutputs_Object=MibScalar
cpqWcrmWaterCoolUnitNumberOfOutputs=_CpqWcrmWaterCoolUnitNumberOfOutputs_Object((1,3,6,1,4,1,232,167,2,4,6,1),_CpqWcrmWaterCoolUnitNumberOfOutputs_Type())
cpqWcrmWaterCoolUnitNumberOfOutputs.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitNumberOfOutputs.setStatus(_A)
_CpqWcrmWaterCoolUnitOutputTable_Object=MibTable
cpqWcrmWaterCoolUnitOutputTable=_CpqWcrmWaterCoolUnitOutputTable_Object((1,3,6,1,4,1,232,167,2,4,6,2))
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitOutputTable.setStatus(_A)
_CpqWcrmWaterCoolUnitOutputEntry_Object=MibTableRow
cpqWcrmWaterCoolUnitOutputEntry=_CpqWcrmWaterCoolUnitOutputEntry_Object((1,3,6,1,4,1,232,167,2,4,6,2,1))
cpqWcrmWaterCoolUnitOutputEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitOutputEntry.setStatus(_A)
class _WaterCoolUnitOutputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WaterCoolUnitOutputIndex_Type.__name__=_B
_WaterCoolUnitOutputIndex_Object=MibTableColumn
waterCoolUnitOutputIndex=_WaterCoolUnitOutputIndex_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,1),_WaterCoolUnitOutputIndex_Type())
waterCoolUnitOutputIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitOutputIndex.setStatus(_A)
class _WaterCoolUnitOutputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43)));namedValues=NamedValues(*((_H,1),(_b,2),(_c,3),('setpoint',4),('hysteresis',5),('command',6),('controlMode',7),('fanSpeedMin',8),('dTmin',9),('dTmax',10),('cpWatert',11),('setHeatload',12),('setEdoFlow',13),('setEdoHeat',14),('setCondCycles',15),('setCondRun',16),('doorControl',17),('pidContrKP',18),('pidContrKI',19),('pidContrKD',20),('pidSampleTime',21),('installedFans',22),('offsetCW',23),('offsetHW',24),('valveControlMode',25),('isolationValveInletManual',26),('isolationValveFacilityManual',27),('isolationValveInfrastructureManual',28),('controlValveFacilityManual',29),('controlValveInfrastructureManual',30),('fanControlMode',31),('fan1Manual',32),('fan2Manual',33),('fan3Manual',34),('fan4Manual',35),('setpointAirDifPressure',36),('pidContrKPFan',37),('pidContrKIFan',38),('pidContrKDFan',39),('pidSampleTimeFan',40),('dewpointOffset',41),('maxItAirTemperature',42),('dewpointControlMode',43)))
_WaterCoolUnitOutputType_Type.__name__=_B
_WaterCoolUnitOutputType_Object=MibTableColumn
waterCoolUnitOutputType=_WaterCoolUnitOutputType_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,2),_WaterCoolUnitOutputType_Type())
waterCoolUnitOutputType.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitOutputType.setStatus(_A)
class _WaterCoolUnitOutputText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_WaterCoolUnitOutputText_Type.__name__=_G
_WaterCoolUnitOutputText_Object=MibTableColumn
waterCoolUnitOutputText=_WaterCoolUnitOutputText_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,3),_WaterCoolUnitOutputText_Type())
waterCoolUnitOutputText.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitOutputText.setStatus(_A)
class _WaterCoolUnitOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,1),(_U,2),(_Q,3),(_L,4),(_K,5),(_M,6),(_X,7),(_Y,8)))
_WaterCoolUnitOutputStatus_Type.__name__=_B
_WaterCoolUnitOutputStatus_Object=MibTableColumn
waterCoolUnitOutputStatus=_WaterCoolUnitOutputStatus_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,4),_WaterCoolUnitOutputStatus_Type())
waterCoolUnitOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitOutputStatus.setStatus(_A)
_WaterCoolUnitOutputValue_Type=Integer32
_WaterCoolUnitOutputValue_Object=MibTableColumn
waterCoolUnitOutputValue=_WaterCoolUnitOutputValue_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,5),_WaterCoolUnitOutputValue_Type())
waterCoolUnitOutputValue.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitOutputValue.setStatus(_A)
class _WaterCoolUnitOutputSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_M,2),('lock',3),(_r,4),(_s,5)))
_WaterCoolUnitOutputSet_Type.__name__=_B
_WaterCoolUnitOutputSet_Object=MibTableColumn
waterCoolUnitOutputSet=_WaterCoolUnitOutputSet_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,6),_WaterCoolUnitOutputSet_Type())
waterCoolUnitOutputSet.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitOutputSet.setStatus(_A)
class _WaterCoolUnitOutputConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),(_u,2)))
_WaterCoolUnitOutputConfig_Type.__name__=_B
_WaterCoolUnitOutputConfig_Object=MibTableColumn
waterCoolUnitOutputConfig=_WaterCoolUnitOutputConfig_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,7),_WaterCoolUnitOutputConfig_Type())
waterCoolUnitOutputConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitOutputConfig.setStatus(_A)
_WaterCoolUnitOutputDelay_Type=Integer32
_WaterCoolUnitOutputDelay_Object=MibTableColumn
waterCoolUnitOutputDelay=_WaterCoolUnitOutputDelay_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,8),_WaterCoolUnitOutputDelay_Type())
waterCoolUnitOutputDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitOutputDelay.setStatus(_A)
class _WaterCoolUnitOutputTimeoutAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stay',1),(_K,2),(_M,3)))
_WaterCoolUnitOutputTimeoutAction_Type.__name__=_B
_WaterCoolUnitOutputTimeoutAction_Object=MibTableColumn
waterCoolUnitOutputTimeoutAction=_WaterCoolUnitOutputTimeoutAction_Object((1,3,6,1,4,1,232,167,2,4,6,2,1,9),_WaterCoolUnitOutputTimeoutAction_Type())
waterCoolUnitOutputTimeoutAction.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitOutputTimeoutAction.setStatus(_A)
_CpqWcrmStatusWaterCoolUnitMsg_ObjectIdentity=ObjectIdentity
cpqWcrmStatusWaterCoolUnitMsg=_CpqWcrmStatusWaterCoolUnitMsg_ObjectIdentity((1,3,6,1,4,1,232,167,2,4,7))
_CpqWcrmWaterCoolUnitNumberOfMsgs_Type=Integer32
_CpqWcrmWaterCoolUnitNumberOfMsgs_Object=MibScalar
cpqWcrmWaterCoolUnitNumberOfMsgs=_CpqWcrmWaterCoolUnitNumberOfMsgs_Object((1,3,6,1,4,1,232,167,2,4,7,1),_CpqWcrmWaterCoolUnitNumberOfMsgs_Type())
cpqWcrmWaterCoolUnitNumberOfMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitNumberOfMsgs.setStatus(_A)
_CpqWcrmWaterCoolUnitMsgTable_Object=MibTable
cpqWcrmWaterCoolUnitMsgTable=_CpqWcrmWaterCoolUnitMsgTable_Object((1,3,6,1,4,1,232,167,2,4,7,2))
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitMsgTable.setStatus(_A)
_CpqWcrmWaterCoolUnitMsgEntry_Object=MibTableRow
cpqWcrmWaterCoolUnitMsgEntry=_CpqWcrmWaterCoolUnitMsgEntry_Object((1,3,6,1,4,1,232,167,2,4,7,2,1))
cpqWcrmWaterCoolUnitMsgEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:cpqWcrmWaterCoolUnitMsgEntry.setStatus(_A)
class _WaterCoolUnitMsgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WaterCoolUnitMsgIndex_Type.__name__=_B
_WaterCoolUnitMsgIndex_Object=MibTableColumn
waterCoolUnitMsgIndex=_WaterCoolUnitMsgIndex_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,1),_WaterCoolUnitMsgIndex_Type())
waterCoolUnitMsgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitMsgIndex.setStatus(_A)
class _WaterCoolUnitMsgText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_WaterCoolUnitMsgText_Type.__name__=_G
_WaterCoolUnitMsgText_Object=MibTableColumn
waterCoolUnitMsgText=_WaterCoolUnitMsgText_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,2),_WaterCoolUnitMsgText_Type())
waterCoolUnitMsgText.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgText.setStatus(_A)
class _WaterCoolUnitMsgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),(_Z,2),(_T,3),(_L,4),(_e,5),(_S,6),(_V,7),(_W,8),(_X,9),(_Y,10)))
_WaterCoolUnitMsgStatus_Type.__name__=_B
_WaterCoolUnitMsgStatus_Object=MibTableColumn
waterCoolUnitMsgStatus=_WaterCoolUnitMsgStatus_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,3),_WaterCoolUnitMsgStatus_Type())
waterCoolUnitMsgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:waterCoolUnitMsgStatus.setStatus(_A)
class _WaterCoolUnitMsgRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WaterCoolUnitMsgRelay_Type.__name__=_B
_WaterCoolUnitMsgRelay_Object=MibTableColumn
waterCoolUnitMsgRelay=_WaterCoolUnitMsgRelay_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,4),_WaterCoolUnitMsgRelay_Type())
waterCoolUnitMsgRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgRelay.setStatus(_A)
class _WaterCoolUnitMsgBeeper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WaterCoolUnitMsgBeeper_Type.__name__=_B
_WaterCoolUnitMsgBeeper_Object=MibTableColumn
waterCoolUnitMsgBeeper=_WaterCoolUnitMsgBeeper_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,5),_WaterCoolUnitMsgBeeper_Type())
waterCoolUnitMsgBeeper.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgBeeper.setStatus(_A)
class _WaterCoolUnitMsgTrap1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WaterCoolUnitMsgTrap1_Type.__name__=_B
_WaterCoolUnitMsgTrap1_Object=MibTableColumn
waterCoolUnitMsgTrap1=_WaterCoolUnitMsgTrap1_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,6),_WaterCoolUnitMsgTrap1_Type())
waterCoolUnitMsgTrap1.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgTrap1.setStatus(_A)
class _WaterCoolUnitMsgTrap2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WaterCoolUnitMsgTrap2_Type.__name__=_B
_WaterCoolUnitMsgTrap2_Object=MibTableColumn
waterCoolUnitMsgTrap2=_WaterCoolUnitMsgTrap2_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,7),_WaterCoolUnitMsgTrap2_Type())
waterCoolUnitMsgTrap2.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgTrap2.setStatus(_A)
class _WaterCoolUnitMsgTrap3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WaterCoolUnitMsgTrap3_Type.__name__=_B
_WaterCoolUnitMsgTrap3_Object=MibTableColumn
waterCoolUnitMsgTrap3=_WaterCoolUnitMsgTrap3_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,8),_WaterCoolUnitMsgTrap3_Type())
waterCoolUnitMsgTrap3.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgTrap3.setStatus(_A)
class _WaterCoolUnitMsgTrap4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WaterCoolUnitMsgTrap4_Type.__name__=_B
_WaterCoolUnitMsgTrap4_Object=MibTableColumn
waterCoolUnitMsgTrap4=_WaterCoolUnitMsgTrap4_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,9),_WaterCoolUnitMsgTrap4_Type())
waterCoolUnitMsgTrap4.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgTrap4.setStatus(_A)
class _WaterCoolUnitMsgReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_v,2)))
_WaterCoolUnitMsgReset_Type.__name__=_B
_WaterCoolUnitMsgReset_Object=MibTableColumn
waterCoolUnitMsgReset=_WaterCoolUnitMsgReset_Object((1,3,6,1,4,1,232,167,2,4,7,2,1,10),_WaterCoolUnitMsgReset_Type())
waterCoolUnitMsgReset.setMaxAccess(_C)
if mibBuilder.loadTexts:waterCoolUnitMsgReset.setStatus(_A)
class _CpqWcrmURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqWcrmURL_Type.__name__=_G
_CpqWcrmURL_Object=MibScalar
cpqWcrmURL=_CpqWcrmURL_Object((1,3,6,1,4,1,232,167,2,7),_CpqWcrmURL_Type())
cpqWcrmURL.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmURL.setStatus(_A)
_CpqWcrmSetup_ObjectIdentity=ObjectIdentity
cpqWcrmSetup=_CpqWcrmSetup_ObjectIdentity((1,3,6,1,4,1,232,167,3))
_CpqWcrmSetupGeneral_ObjectIdentity=ObjectIdentity
cpqWcrmSetupGeneral=_CpqWcrmSetupGeneral_ObjectIdentity((1,3,6,1,4,1,232,167,3,1))
class _CpqWcrmSetTempUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('celsius',1),('fahrenheit',2)))
_CpqWcrmSetTempUnit_Type.__name__=_B
_CpqWcrmSetTempUnit_Object=MibScalar
cpqWcrmSetTempUnit=_CpqWcrmSetTempUnit_Object((1,3,6,1,4,1,232,167,3,1,1),_CpqWcrmSetTempUnit_Type())
cpqWcrmSetTempUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmSetTempUnit.setStatus(_A)
class _CpqWcrmSetBeeper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_CpqWcrmSetBeeper_Type.__name__=_B
_CpqWcrmSetBeeper_Object=MibScalar
cpqWcrmSetBeeper=_CpqWcrmSetBeeper_Object((1,3,6,1,4,1,232,167,3,1,2),_CpqWcrmSetBeeper_Type())
cpqWcrmSetBeeper.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmSetBeeper.setStatus(_A)
class _CpqWcrmResetRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_CpqWcrmResetRelay_Type.__name__=_B
_CpqWcrmResetRelay_Object=MibScalar
cpqWcrmResetRelay=_CpqWcrmResetRelay_Object((1,3,6,1,4,1,232,167,3,1,3),_CpqWcrmResetRelay_Type())
cpqWcrmResetRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmResetRelay.setStatus(_A)
class _CpqWcrmLogicRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('closeAtAlarm',1),('openAtAlarm',2),(_K,3)))
_CpqWcrmLogicRelay_Type.__name__=_B
_CpqWcrmLogicRelay_Object=MibScalar
cpqWcrmLogicRelay=_CpqWcrmLogicRelay_Object((1,3,6,1,4,1,232,167,3,1,4),_CpqWcrmLogicRelay_Type())
cpqWcrmLogicRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmLogicRelay.setStatus(_A)
class _CpqWcrmWebAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('viewOnly',1),('fullAccess',2),(_K,3)))
_CpqWcrmWebAccess_Type.__name__=_B
_CpqWcrmWebAccess_Object=MibScalar
cpqWcrmWebAccess=_CpqWcrmWebAccess_Object((1,3,6,1,4,1,232,167,3,1,5),_CpqWcrmWebAccess_Type())
cpqWcrmWebAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmWebAccess.setStatus(_A)
class _CpqWcrmSetupDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CpqWcrmSetupDate_Type.__name__=_G
_CpqWcrmSetupDate_Object=MibScalar
cpqWcrmSetupDate=_CpqWcrmSetupDate_Object((1,3,6,1,4,1,232,167,3,1,6),_CpqWcrmSetupDate_Type())
cpqWcrmSetupDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmSetupDate.setStatus(_A)
class _CpqWcrmSetupTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqWcrmSetupTime_Type.__name__=_G
_CpqWcrmSetupTime_Object=MibScalar
cpqWcrmSetupTime=_CpqWcrmSetupTime_Object((1,3,6,1,4,1,232,167,3,1,7),_CpqWcrmSetupTime_Type())
cpqWcrmSetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmSetupTime.setStatus(_A)
_CpqWcrmTimerTable1_ObjectIdentity=ObjectIdentity
cpqWcrmTimerTable1=_CpqWcrmTimerTable1_ObjectIdentity((1,3,6,1,4,1,232,167,3,1,8))
_CpqWcrmTimerNumber_Type=Integer32
_CpqWcrmTimerNumber_Object=MibScalar
cpqWcrmTimerNumber=_CpqWcrmTimerNumber_Object((1,3,6,1,4,1,232,167,3,1,8,1),_CpqWcrmTimerNumber_Type())
cpqWcrmTimerNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmTimerNumber.setStatus(_A)
_CpqWcrmTimerTable_Object=MibTable
cpqWcrmTimerTable=_CpqWcrmTimerTable_Object((1,3,6,1,4,1,232,167,3,1,8,2))
if mibBuilder.loadTexts:cpqWcrmTimerTable.setStatus(_A)
_CpqWcrmTimerEntry_Object=MibTableRow
cpqWcrmTimerEntry=_CpqWcrmTimerEntry_Object((1,3,6,1,4,1,232,167,3,1,8,2,1))
cpqWcrmTimerEntry.setIndexNames((0,_E,_y))
if mibBuilder.loadTexts:cpqWcrmTimerEntry.setStatus(_A)
class _CpqWcrmTimerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqWcrmTimerIndex_Type.__name__=_B
_CpqWcrmTimerIndex_Object=MibTableColumn
cpqWcrmTimerIndex=_CpqWcrmTimerIndex_Object((1,3,6,1,4,1,232,167,3,1,8,2,1,1),_CpqWcrmTimerIndex_Type())
cpqWcrmTimerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmTimerIndex.setStatus(_A)
class _CpqWcrmTimerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('switchedOff',1),('switchedOn',2),('noTime',3)))
_CpqWcrmTimerStatus_Type.__name__=_B
_CpqWcrmTimerStatus_Object=MibTableColumn
cpqWcrmTimerStatus=_CpqWcrmTimerStatus_Object((1,3,6,1,4,1,232,167,3,1,8,2,1,2),_CpqWcrmTimerStatus_Type())
cpqWcrmTimerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmTimerStatus.setStatus(_A)
class _CpqWcrmTimerDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7),('sat-sun',8),('mon-fri',9),('mon-sun',10)))
_CpqWcrmTimerDayOfWeek_Type.__name__=_B
_CpqWcrmTimerDayOfWeek_Object=MibTableColumn
cpqWcrmTimerDayOfWeek=_CpqWcrmTimerDayOfWeek_Object((1,3,6,1,4,1,232,167,3,1,8,2,1,3),_CpqWcrmTimerDayOfWeek_Type())
cpqWcrmTimerDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmTimerDayOfWeek.setStatus(_A)
class _CpqWcrmTimeOn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqWcrmTimeOn_Type.__name__=_G
_CpqWcrmTimeOn_Object=MibTableColumn
cpqWcrmTimeOn=_CpqWcrmTimeOn_Object((1,3,6,1,4,1,232,167,3,1,8,2,1,4),_CpqWcrmTimeOn_Type())
cpqWcrmTimeOn.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmTimeOn.setStatus(_A)
class _CpqWcrmTimeOff_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqWcrmTimeOff_Type.__name__=_G
_CpqWcrmTimeOff_Object=MibTableColumn
cpqWcrmTimeOff=_CpqWcrmTimeOff_Object((1,3,6,1,4,1,232,167,3,1,8,2,1,5),_CpqWcrmTimeOff_Type())
cpqWcrmTimeOff.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmTimeOff.setStatus(_A)
class _CpqWcrmTimeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_CpqWcrmTimeControl_Type.__name__=_B
_CpqWcrmTimeControl_Object=MibTableColumn
cpqWcrmTimeControl=_CpqWcrmTimeControl_Object((1,3,6,1,4,1,232,167,3,1,8,2,1,6),_CpqWcrmTimeControl_Type())
cpqWcrmTimeControl.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmTimeControl.setStatus(_A)
class _CpqWcrmTimerFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('disTrapRec1',1),('disTrapRec2',2),('disTrapRec3',3),('disTrapRec4',4),('schedule1',5),('schedule2',6),('schedule3',7),('schedule4',8)))
_CpqWcrmTimerFunction_Type.__name__=_B
_CpqWcrmTimerFunction_Object=MibTableColumn
cpqWcrmTimerFunction=_CpqWcrmTimerFunction_Object((1,3,6,1,4,1,232,167,3,1,8,2,1,7),_CpqWcrmTimerFunction_Type())
cpqWcrmTimerFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmTimerFunction.setStatus(_A)
class _CpqWcrmSetFlowUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('literMin',1),('gallonMin',2)))
_CpqWcrmSetFlowUnit_Type.__name__=_B
_CpqWcrmSetFlowUnit_Object=MibScalar
cpqWcrmSetFlowUnit=_CpqWcrmSetFlowUnit_Object((1,3,6,1,4,1,232,167,3,1,9),_CpqWcrmSetFlowUnit_Type())
cpqWcrmSetFlowUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmSetFlowUnit.setStatus(_A)
_CpqWcrmTrapControl_ObjectIdentity=ObjectIdentity
cpqWcrmTrapControl=_CpqWcrmTrapControl_ObjectIdentity((1,3,6,1,4,1,232,167,4))
_CpqWcrmTraps_ObjectIdentity=ObjectIdentity
cpqWcrmTraps=_CpqWcrmTraps_ObjectIdentity((1,3,6,1,4,1,232,167,4,7))
_CpqWcrmTraptableNumber_Type=Integer32
_CpqWcrmTraptableNumber_Object=MibScalar
cpqWcrmTraptableNumber=_CpqWcrmTraptableNumber_Object((1,3,6,1,4,1,232,167,4,7,1),_CpqWcrmTraptableNumber_Type())
cpqWcrmTraptableNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqWcrmTraptableNumber.setStatus(_A)
_CpqWcrmTrapTableTable_Object=MibTable
cpqWcrmTrapTableTable=_CpqWcrmTrapTableTable_Object((1,3,6,1,4,1,232,167,4,7,2))
if mibBuilder.loadTexts:cpqWcrmTrapTableTable.setStatus(_A)
_CpqWcrmTrapTableEntry_Object=MibTableRow
cpqWcrmTrapTableEntry=_CpqWcrmTrapTableEntry_Object((1,3,6,1,4,1,232,167,4,7,2,1))
cpqWcrmTrapTableEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:cpqWcrmTrapTableEntry.setStatus(_A)
class _TrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TrapIndex_Type.__name__=_B
_TrapIndex_Object=MibTableColumn
trapIndex=_TrapIndex_Object((1,3,6,1,4,1,232,167,4,7,2,1,1),_TrapIndex_Type())
trapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:trapIndex.setStatus(_A)
class _TrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_TrapStatus_Type.__name__=_B
_TrapStatus_Object=MibTableColumn
trapStatus=_TrapStatus_Object((1,3,6,1,4,1,232,167,4,7,2,1,2),_TrapStatus_Type())
trapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:trapStatus.setStatus(_A)
class _TrapIPaddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_TrapIPaddress_Type.__name__=_G
_TrapIPaddress_Object=MibTableColumn
trapIPaddress=_TrapIPaddress_Object((1,3,6,1,4,1,232,167,4,7,2,1,3),_TrapIPaddress_Type())
trapIPaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trapIPaddress.setStatus(_A)
class _TrapIPV4V6address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TrapIPV4V6address_Type.__name__=_G
_TrapIPV4V6address_Object=MibTableColumn
trapIPV4V6address=_TrapIPV4V6address_Object((1,3,6,1,4,1,232,167,4,7,2,1,4),_TrapIPV4V6address_Type())
trapIPV4V6address.setMaxAccess(_C)
if mibBuilder.loadTexts:trapIPV4V6address.setStatus(_A)
_CpqWcrmControl_ObjectIdentity=ObjectIdentity
cpqWcrmControl=_CpqWcrmControl_ObjectIdentity((1,3,6,1,4,1,232,167,5))
class _CpqWcrmResetUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),(_a,2)))
_CpqWcrmResetUnit_Type.__name__=_B
_CpqWcrmResetUnit_Object=MibScalar
cpqWcrmResetUnit=_CpqWcrmResetUnit_Object((1,3,6,1,4,1,232,167,5,1),_CpqWcrmResetUnit_Type())
cpqWcrmResetUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqWcrmResetUnit.setStatus(_A)
alarmSensorInternal=NotificationType((1,3,6,1,4,1,232,167,0,1))
alarmSensorInternal.setObjects(*((_F,_N),(_F,_P),(_F,_O),(_E,_d),(_E,_A0),(_E,_A1),(_E,_A2),(_E,_R)))
if mibBuilder.loadTexts:alarmSensorInternal.setStatus('')
alarmSensorWaterCoolUnit=NotificationType((1,3,6,1,4,1,232,167,0,2))
alarmSensorWaterCoolUnit.setObjects(*((_F,_N),(_F,_P),(_F,_O),(_E,_f),(_E,_A3),(_E,_A4),(_E,_A5),(_E,_R)))
if mibBuilder.loadTexts:alarmSensorWaterCoolUnit.setStatus('')
alarmInternal=NotificationType((1,3,6,1,4,1,232,167,0,5))
alarmInternal.setObjects(*((_F,_N),(_F,_P),(_F,_O),(_E,_A6),(_E,_A7),(_E,_R)))
if mibBuilder.loadTexts:alarmInternal.setStatus('')
alarmWaterCoolUnit=NotificationType((1,3,6,1,4,1,232,167,0,6))
alarmWaterCoolUnit.setObjects(*((_F,_N),(_F,_P),(_F,_O),(_E,_A8),(_E,_A9),(_E,_R)))
if mibBuilder.loadTexts:alarmWaterCoolUnit.setStatus('')
testTrap=NotificationType((1,3,6,1,4,1,232,167,0,10))
testTrap.setObjects(*((_F,_N),(_F,_P),(_F,_O),(_E,_R)))
if mibBuilder.loadTexts:testTrap.setStatus('')
mibBuilder.exportSymbols(_E,**{'cpqWcrm':cpqWcrm,'alarmSensorInternal':alarmSensorInternal,'alarmSensorWaterCoolUnit':alarmSensorWaterCoolUnit,'alarmInternal':alarmInternal,'alarmWaterCoolUnit':alarmWaterCoolUnit,'testTrap':testTrap,'cpqWcrmMibRev':cpqWcrmMibRev,'cpqWcrmMibMajRev':cpqWcrmMibMajRev,'cpqWcrmMibMinRev':cpqWcrmMibMinRev,'cpqWcrmMibCondition':cpqWcrmMibCondition,'cpqWcrmStatus':cpqWcrmStatus,'cpqWcrmStatusDeviceEnvironmentalController':cpqWcrmStatusDeviceEnvironmentalController,'cpqWcrmUnitsConnected':cpqWcrmUnitsConnected,'cpqWcrmStatusSensorInternal':cpqWcrmStatusSensorInternal,'cpqWcrmInternalTypeOfDevice':cpqWcrmInternalTypeOfDevice,_A6:cpqWcrmInternalText,'cpqWcrmInternalSerial':cpqWcrmInternalSerial,_A7:cpqWcrmInternalStatus,'cpqWcrmStatusInternalSensors':cpqWcrmStatusInternalSensors,'cpqWcrmInternalNumberOfSensors':cpqWcrmInternalNumberOfSensors,'cpqWcrmInternalSensorTable':cpqWcrmInternalSensorTable,'cpqWcrmInternalSensorEntry':cpqWcrmInternalSensorEntry,_p:internalSensorIndex,'internalSensorType':internalSensorType,'internalSensorText':internalSensorText,'internalSensorStatus':internalSensorStatus,_A2:internalSensorValue,'internalSensorSetHigh':internalSensorSetHigh,'internalSensorSetLow':internalSensorSetLow,'internalSensorSetWarn':internalSensorSetWarn,'internalSensorValueScale':internalSensorValueScale,'internalSensorScaledValue':internalSensorScaledValue,'cpqWcrmStatusInternalOutputs':cpqWcrmStatusInternalOutputs,'cpqWcrmInternalNumberOfOutputs':cpqWcrmInternalNumberOfOutputs,'cpqWcrmInternalOutputTable':cpqWcrmInternalOutputTable,'cpqWcrmInternalOutputEntry':cpqWcrmInternalOutputEntry,_q:internalOutputIndex,'internalOutputType':internalOutputType,'internalOutputText':internalOutputText,'internalOutputStatus':internalOutputStatus,'internalOutputValue':internalOutputValue,'internalOutputSet':internalOutputSet,'internalOutputConfig':internalOutputConfig,'internalOutputDelay':internalOutputDelay,'internalOutputTimeoutAction':internalOutputTimeoutAction,'cpqWcrmStatusInternalMsg':cpqWcrmStatusInternalMsg,'cpqWcrmInternalNumberOfMsgs':cpqWcrmInternalNumberOfMsgs,'cpqWcrmInternalMsgTable':cpqWcrmInternalMsgTable,'cpqWcrmInternalMsgEntry':cpqWcrmInternalMsgEntry,_d:internalMsgIndex,_A0:internalMsgText,_A1:internalMsgStatus,'internalMsgRelay':internalMsgRelay,'internalMsgBeeper':internalMsgBeeper,'internalMsgTrap1':internalMsgTrap1,'internalMsgTrap2':internalMsgTrap2,'internalMsgTrap3':internalMsgTrap3,'internalMsgTrap4':internalMsgTrap4,'internalMsgReset':internalMsgReset,'cpqWcrmStatusSensorWaterCoolUnit':cpqWcrmStatusSensorWaterCoolUnit,'cpqWcrmWaterCoolUnitTypeOfDevice':cpqWcrmWaterCoolUnitTypeOfDevice,_A8:cpqWcrmWaterCoolUnitText,'cpqWcrmWaterCoolUnitSerial':cpqWcrmWaterCoolUnitSerial,_A9:cpqWcrmWaterCoolUnitStatus,'cpqWcrmStatusWaterCoolUnitSensors':cpqWcrmStatusWaterCoolUnitSensors,'cpqWcrmWaterCoolUnitNumberOfSensors':cpqWcrmWaterCoolUnitNumberOfSensors,'cpqWcrmWaterCoolUnitSensorTable':cpqWcrmWaterCoolUnitSensorTable,'cpqWcrmWaterCoolUnitSensorEntry':cpqWcrmWaterCoolUnitSensorEntry,_w:waterCoolUnitSensorIndex,'waterCoolUnitSensorType':waterCoolUnitSensorType,'waterCoolUnitSensorText':waterCoolUnitSensorText,'waterCoolUnitSensorStatus':waterCoolUnitSensorStatus,_A5:waterCoolUnitSensorValue,'waterCoolUnitSensorSetHigh':waterCoolUnitSensorSetHigh,'waterCoolUnitSensorSetLow':waterCoolUnitSensorSetLow,'waterCoolUnitSensorSetWarn':waterCoolUnitSensorSetWarn,'waterCoolUnitSensorValueScale':waterCoolUnitSensorValueScale,'waterCoolUnitSensorScaledValue':waterCoolUnitSensorScaledValue,'cpqWcrmStatusWaterCoolUnitOutputs':cpqWcrmStatusWaterCoolUnitOutputs,'cpqWcrmWaterCoolUnitNumberOfOutputs':cpqWcrmWaterCoolUnitNumberOfOutputs,'cpqWcrmWaterCoolUnitOutputTable':cpqWcrmWaterCoolUnitOutputTable,'cpqWcrmWaterCoolUnitOutputEntry':cpqWcrmWaterCoolUnitOutputEntry,_x:waterCoolUnitOutputIndex,'waterCoolUnitOutputType':waterCoolUnitOutputType,'waterCoolUnitOutputText':waterCoolUnitOutputText,'waterCoolUnitOutputStatus':waterCoolUnitOutputStatus,'waterCoolUnitOutputValue':waterCoolUnitOutputValue,'waterCoolUnitOutputSet':waterCoolUnitOutputSet,'waterCoolUnitOutputConfig':waterCoolUnitOutputConfig,'waterCoolUnitOutputDelay':waterCoolUnitOutputDelay,'waterCoolUnitOutputTimeoutAction':waterCoolUnitOutputTimeoutAction,'cpqWcrmStatusWaterCoolUnitMsg':cpqWcrmStatusWaterCoolUnitMsg,'cpqWcrmWaterCoolUnitNumberOfMsgs':cpqWcrmWaterCoolUnitNumberOfMsgs,'cpqWcrmWaterCoolUnitMsgTable':cpqWcrmWaterCoolUnitMsgTable,'cpqWcrmWaterCoolUnitMsgEntry':cpqWcrmWaterCoolUnitMsgEntry,_f:waterCoolUnitMsgIndex,_A3:waterCoolUnitMsgText,_A4:waterCoolUnitMsgStatus,'waterCoolUnitMsgRelay':waterCoolUnitMsgRelay,'waterCoolUnitMsgBeeper':waterCoolUnitMsgBeeper,'waterCoolUnitMsgTrap1':waterCoolUnitMsgTrap1,'waterCoolUnitMsgTrap2':waterCoolUnitMsgTrap2,'waterCoolUnitMsgTrap3':waterCoolUnitMsgTrap3,'waterCoolUnitMsgTrap4':waterCoolUnitMsgTrap4,'waterCoolUnitMsgReset':waterCoolUnitMsgReset,_R:cpqWcrmURL,'cpqWcrmSetup':cpqWcrmSetup,'cpqWcrmSetupGeneral':cpqWcrmSetupGeneral,'cpqWcrmSetTempUnit':cpqWcrmSetTempUnit,'cpqWcrmSetBeeper':cpqWcrmSetBeeper,'cpqWcrmResetRelay':cpqWcrmResetRelay,'cpqWcrmLogicRelay':cpqWcrmLogicRelay,'cpqWcrmWebAccess':cpqWcrmWebAccess,'cpqWcrmSetupDate':cpqWcrmSetupDate,'cpqWcrmSetupTime':cpqWcrmSetupTime,'cpqWcrmTimerTable1':cpqWcrmTimerTable1,'cpqWcrmTimerNumber':cpqWcrmTimerNumber,'cpqWcrmTimerTable':cpqWcrmTimerTable,'cpqWcrmTimerEntry':cpqWcrmTimerEntry,_y:cpqWcrmTimerIndex,'cpqWcrmTimerStatus':cpqWcrmTimerStatus,'cpqWcrmTimerDayOfWeek':cpqWcrmTimerDayOfWeek,'cpqWcrmTimeOn':cpqWcrmTimeOn,'cpqWcrmTimeOff':cpqWcrmTimeOff,'cpqWcrmTimeControl':cpqWcrmTimeControl,'cpqWcrmTimerFunction':cpqWcrmTimerFunction,'cpqWcrmSetFlowUnit':cpqWcrmSetFlowUnit,'cpqWcrmTrapControl':cpqWcrmTrapControl,'cpqWcrmTraps':cpqWcrmTraps,'cpqWcrmTraptableNumber':cpqWcrmTraptableNumber,'cpqWcrmTrapTableTable':cpqWcrmTrapTableTable,'cpqWcrmTrapTableEntry':cpqWcrmTrapTableEntry,_z:trapIndex,'trapStatus':trapStatus,'trapIPaddress':trapIPaddress,'trapIPV4V6address':trapIPV4V6address,'cpqWcrmControl':cpqWcrmControl,'cpqWcrmResetUnit':cpqWcrmResetUnit})