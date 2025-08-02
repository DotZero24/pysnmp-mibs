_A8='irIpAddress'
_A7='irTextString'
_A6='irPowerStatus'
_A5='irPowerIndex'
_A4='irEnetPortLinkStatus'
_A3='irEnetPortIndex'
_A2='ipmiThresholdType'
_A1='ipmiThresholdSensorName'
_A0='ipmiThresholdDirection'
_z='ipmiThresholdAssert'
_y='irHdamPowerStatus'
_x='irHdamPowerPortIndex'
_w='irHdamPowerIndex'
_v='irUserName'
_u='irSysTempThresholdLow'
_t='irSysTempThresholdHigh'
_s='ipmiDiscreteSensorName'
_r='ipmiDiscreteOffset'
_q='irHdamPortIndex'
_p='irAnalogThresholdLowAlarmCount'
_o='irAnalogThresholdHighAlarmCount'
_n='irAlarmTrapSeverity'
_m='irAlarmSlotIndex'
_l='irAlarmPortIndex'
_k='irAlarmPointIndex'
_j='irAlarmName'
_i='irAlarmDescription'
_h='irAlarmCount'
_g='irAlarmContactState'
_f='irTempThresholdLow'
_e='irTempThresholdHigh'
_d='irLdAlarmTrapSeverity'
_c='irLdAlarmPortIndex'
_b='irLdAlarmPointIndex'
_a='irLdAlarmName'
_Z='irLdAlarmDescription'
_Y='irLdAlarmCount'
_X='irLdAlarmContactState'
_W='irHumidityThresholdLow'
_V='irHumidityThresholdHigh'
_U='accessible-for-notify'
_T='irSysTempHysteresis'
_S='irSysCurrentTemp'
_R='irAnalogThresholdSeverity'
_Q='irAnalogSlotIndex'
_P='irAnalogPortIndex'
_O='irAnalogPointIndex'
_N='irAnalogName'
_M='irAnalogDescription'
_L='irAnalogCalValue'
_K='irTempValue'
_J='irTempTrapSeverity'
_I='irHumidityValue'
_H='irHumidityTrapSeverity'
_G='irTimeStamp'
_F='MRV-IR-TRAP-MIB'
_E='irCharPortIndex'
_D='MRV-IR-SYSTEM-MIB'
_C='current'
_B='MRV-IR-CHAR-MIB'
_A='MRV-IR-HDAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
irCharPortIndex,irHumidityThresholdHigh,irHumidityThresholdLow,irHumidityTrapSeverity,irHumidityValue,irLdAlarmContactState,irLdAlarmCount,irLdAlarmDescription,irLdAlarmName,irLdAlarmPointIndex,irLdAlarmPortIndex,irLdAlarmTrapSeverity,irTempThresholdHigh,irTempThresholdLow,irTempTrapSeverity,irTempValue=mibBuilder.importSymbols(_B,_E,_V,_W,_H,_I,_X,_Y,_Z,_a,_b,_c,_d,_e,_f,_J,_K)
irAlarmContactState,irAlarmCount,irAlarmDescription,irAlarmName,irAlarmPointIndex,irAlarmPortIndex,irAlarmSlotIndex,irAlarmTrapSeverity,irAnalogCalValue,irAnalogDescription,irAnalogName,irAnalogPointIndex,irAnalogPortIndex,irAnalogSlotIndex,irAnalogThresholdHighAlarmCount,irAnalogThresholdLowAlarmCount,irAnalogThresholdSeverity,irHdamPortIndex,irHdamPowerIndex,irHdamPowerPortIndex,irHdamPowerStatus=mibBuilder.importSymbols(_A,_g,_h,_i,_j,_k,_l,_m,_n,_L,_M,_N,_O,_P,_Q,_o,_p,_R,_q,_w,_x,_y)
ipmiDiscreteOffset,ipmiDiscreteSensorName,ipmiThresholdAssert,ipmiThresholdDirection,ipmiThresholdSensorName,ipmiThresholdType,irEnetPortIndex,irEnetPortLinkStatus,irPowerIndex,irPowerStatus,irSysCurrentTemp,irSysTempHysteresis,irSysTempThresholdHigh,irSysTempThresholdLow,mrvLx=mibBuilder.importSymbols(_D,_r,_s,_z,_A0,_A1,_A2,_A3,_A4,_A5,_A6,_S,_T,_t,_u,'mrvLx')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
irTrapMib=ModuleIdentity((1,3,6,1,4,1,33,100,3))
_IrTrapObjects_ObjectIdentity=ObjectIdentity
irTrapObjects=_IrTrapObjects_ObjectIdentity((1,3,6,1,4,1,33,100,3,1))
_IrTextString_Type=DisplayString
_IrTextString_Object=MibScalar
irTextString=_IrTextString_Object((1,3,6,1,4,1,33,100,3,1,1),_IrTextString_Type())
irTextString.setMaxAccess(_U)
if mibBuilder.loadTexts:irTextString.setStatus(_C)
_IrTimeStamp_Type=DisplayString
_IrTimeStamp_Object=MibScalar
irTimeStamp=_IrTimeStamp_Object((1,3,6,1,4,1,33,100,3,1,2),_IrTimeStamp_Type())
irTimeStamp.setMaxAccess(_U)
if mibBuilder.loadTexts:irTimeStamp.setStatus(_C)
_IrUserName_Type=DisplayString
_IrUserName_Object=MibScalar
irUserName=_IrUserName_Object((1,3,6,1,4,1,33,100,3,1,3),_IrUserName_Type())
irUserName.setMaxAccess(_U)
if mibBuilder.loadTexts:irUserName.setStatus(_C)
_IrIpAddress_Type=DisplayString
_IrIpAddress_Object=MibScalar
irIpAddress=_IrIpAddress_Object((1,3,6,1,4,1,33,100,3,1,4),_IrIpAddress_Type())
irIpAddress.setMaxAccess(_U)
if mibBuilder.loadTexts:irIpAddress.setStatus(_C)
_IrTraps_ObjectIdentity=ObjectIdentity
irTraps=_IrTraps_ObjectIdentity((1,3,6,1,4,1,33,100,3,2))
irNotifyEvent=NotificationType((1,3,6,1,4,1,33,100,3,2,1))
irNotifyEvent.setObjects((_F,_A7))
if mibBuilder.loadTexts:irNotifyEvent.setStatus(_C)
irTempHighTholdAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,2))
irTempHighTholdAlarmRaised.setObjects(*((_B,_E),(_B,_K),(_B,_e),(_B,_J)))
if mibBuilder.loadTexts:irTempHighTholdAlarmRaised.setStatus(_C)
irTempHighTholdAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,3))
irTempHighTholdAlarmCleared.setObjects(*((_B,_E),(_B,_K),(_B,_e),(_B,_J)))
if mibBuilder.loadTexts:irTempHighTholdAlarmCleared.setStatus(_C)
irTempLowTholdAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,4))
irTempLowTholdAlarmRaised.setObjects(*((_B,_E),(_B,_K),(_B,_f),(_B,_J)))
if mibBuilder.loadTexts:irTempLowTholdAlarmRaised.setStatus(_C)
irTempLowTholdAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,5))
irTempLowTholdAlarmCleared.setObjects(*((_B,_E),(_B,_K),(_B,_f),(_B,_J)))
if mibBuilder.loadTexts:irTempLowTholdAlarmCleared.setStatus(_C)
irHumidityHighTholdAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,6))
irHumidityHighTholdAlarmRaised.setObjects(*((_B,_E),(_B,_I),(_B,_V),(_B,_H)))
if mibBuilder.loadTexts:irHumidityHighTholdAlarmRaised.setStatus(_C)
irHumidityHighTholdAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,7))
irHumidityHighTholdAlarmCleared.setObjects(*((_B,_E),(_B,_I),(_B,_V),(_B,_H)))
if mibBuilder.loadTexts:irHumidityHighTholdAlarmCleared.setStatus(_C)
irHumidityLowTholdAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,8))
irHumidityLowTholdAlarmRaised.setObjects(*((_B,_E),(_B,_I),(_B,_W),(_B,_H)))
if mibBuilder.loadTexts:irHumidityLowTholdAlarmRaised.setStatus(_C)
irHumidityLowTholdAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,9))
irHumidityLowTholdAlarmCleared.setObjects(*((_B,_E),(_B,_I),(_B,_W),(_B,_H)))
if mibBuilder.loadTexts:irHumidityLowTholdAlarmCleared.setStatus(_C)
irClusterSyncStarted=NotificationType((1,3,6,1,4,1,33,100,3,2,10))
irClusterSyncStarted.setObjects((_F,_G))
if mibBuilder.loadTexts:irClusterSyncStarted.setStatus(_C)
irClusterSyncCompleted=NotificationType((1,3,6,1,4,1,33,100,3,2,11))
irClusterSyncCompleted.setObjects((_F,_G))
if mibBuilder.loadTexts:irClusterSyncCompleted.setStatus(_C)
irClusterSoftwareUpdateStarted=NotificationType((1,3,6,1,4,1,33,100,3,2,12))
irClusterSoftwareUpdateStarted.setObjects((_F,_G))
if mibBuilder.loadTexts:irClusterSoftwareUpdateStarted.setStatus(_C)
irClusterSoftwareUpdateCompleted=NotificationType((1,3,6,1,4,1,33,100,3,2,13))
irClusterSoftwareUpdateCompleted.setObjects((_F,_G))
if mibBuilder.loadTexts:irClusterSoftwareUpdateCompleted.setStatus(_C)
irClusterBootloaderUpdateStarted=NotificationType((1,3,6,1,4,1,33,100,3,2,14))
irClusterBootloaderUpdateStarted.setObjects((_F,_G))
if mibBuilder.loadTexts:irClusterBootloaderUpdateStarted.setStatus(_C)
irClusterBootloaderUpdateCompleted=NotificationType((1,3,6,1,4,1,33,100,3,2,15))
irClusterBootloaderUpdateCompleted.setObjects((_F,_G))
if mibBuilder.loadTexts:irClusterBootloaderUpdateCompleted.setStatus(_C)
irPowerSupplyStatusChanged=NotificationType((1,3,6,1,4,1,33,100,3,2,16))
irPowerSupplyStatusChanged.setObjects(*((_D,_A5),(_D,_A6)))
if mibBuilder.loadTexts:irPowerSupplyStatusChanged.setStatus(_C)
irLoginFailed=NotificationType((1,3,6,1,4,1,33,100,3,2,17))
irLoginFailed.setObjects(*((_F,_v),(_F,_A8),(_B,_E)))
if mibBuilder.loadTexts:irLoginFailed.setStatus(_C)
irHdamAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,18))
irHdamAlarmRaised.setObjects(*((_A,_l),(_A,_m),(_A,_k),(_A,_j),(_A,_g),(_A,_n),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:irHdamAlarmRaised.setStatus(_C)
irHdamAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,19))
irHdamAlarmCleared.setObjects(*((_A,_l),(_A,_m),(_A,_k),(_A,_j),(_A,_g),(_A,_n),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:irHdamAlarmCleared.setStatus(_C)
irHdamContactLost=NotificationType((1,3,6,1,4,1,33,100,3,2,20))
irHdamContactLost.setObjects((_A,_q))
if mibBuilder.loadTexts:irHdamContactLost.setStatus(_C)
irHdamContactRegained=NotificationType((1,3,6,1,4,1,33,100,3,2,21))
irHdamContactRegained.setObjects((_A,_q))
if mibBuilder.loadTexts:irHdamContactRegained.setStatus(_C)
irHdamPowerStatusChanged=NotificationType((1,3,6,1,4,1,33,100,3,2,22))
irHdamPowerStatusChanged.setObjects(*((_A,_x),(_A,_w),(_A,_y)))
if mibBuilder.loadTexts:irHdamPowerStatusChanged.setStatus(_C)
irOnBoardLowTempExceeded=NotificationType((1,3,6,1,4,1,33,100,3,2,24))
irOnBoardLowTempExceeded.setObjects(*((_D,_S),(_D,_u),(_D,_T)))
if mibBuilder.loadTexts:irOnBoardLowTempExceeded.setStatus(_C)
irOnBoardLowTempCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,25))
irOnBoardLowTempCleared.setObjects(*((_D,_S),(_D,_u),(_D,_T)))
if mibBuilder.loadTexts:irOnBoardLowTempCleared.setStatus(_C)
irOnBoardHighTempExceeded=NotificationType((1,3,6,1,4,1,33,100,3,2,26))
irOnBoardHighTempExceeded.setObjects(*((_D,_S),(_D,_t),(_D,_T)))
if mibBuilder.loadTexts:irOnBoardHighTempExceeded.setStatus(_C)
irOnBoardHighTempCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,27))
irOnBoardHighTempCleared.setObjects(*((_D,_S),(_D,_t),(_D,_T)))
if mibBuilder.loadTexts:irOnBoardHighTempCleared.setStatus(_C)
irAdminLoginFailed=NotificationType((1,3,6,1,4,1,33,100,3,2,28))
irAdminLoginFailed.setObjects(*((_F,_v),(_B,_E)))
if mibBuilder.loadTexts:irAdminLoginFailed.setStatus(_C)
irEnetPortBondLinkStatusChanged=NotificationType((1,3,6,1,4,1,33,100,3,2,29))
irEnetPortBondLinkStatusChanged.setObjects(*((_D,_A3),(_D,_A4)))
if mibBuilder.loadTexts:irEnetPortBondLinkStatusChanged.setStatus(_C)
irHdamAnalogHighAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,30))
irHdamAnalogHighAlarmRaised.setObjects(*((_A,_P),(_A,_Q),(_A,_O),(_A,_N),(_A,_M),(_A,_L),(_A,_R),(_A,_o)))
if mibBuilder.loadTexts:irHdamAnalogHighAlarmRaised.setStatus(_C)
irHdamAnalogHighAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,31))
irHdamAnalogHighAlarmCleared.setObjects(*((_A,_P),(_A,_Q),(_A,_O),(_A,_N),(_A,_M),(_A,_L),(_A,_R),(_A,_o)))
if mibBuilder.loadTexts:irHdamAnalogHighAlarmCleared.setStatus(_C)
irHdamAnalogLowAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,32))
irHdamAnalogLowAlarmRaised.setObjects(*((_A,_P),(_A,_Q),(_A,_O),(_A,_N),(_A,_M),(_A,_L),(_A,_R),(_A,_p)))
if mibBuilder.loadTexts:irHdamAnalogLowAlarmRaised.setStatus(_C)
irHdamAnalogLowAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,33))
irHdamAnalogLowAlarmCleared.setObjects(*((_A,_P),(_A,_Q),(_A,_O),(_A,_N),(_A,_M),(_A,_L),(_A,_R),(_A,_p)))
if mibBuilder.loadTexts:irHdamAnalogLowAlarmCleared.setStatus(_C)
irLdamAlarmRaised=NotificationType((1,3,6,1,4,1,33,100,3,2,34))
irLdamAlarmRaised.setObjects(*((_B,_c),(_B,_b),(_B,_a),(_B,_Z),(_B,_X),(_B,_d),(_B,_Y)))
if mibBuilder.loadTexts:irLdamAlarmRaised.setStatus(_C)
irLdamAlarmCleared=NotificationType((1,3,6,1,4,1,33,100,3,2,35))
irLdamAlarmCleared.setObjects(*((_B,_c),(_B,_b),(_B,_a),(_B,_Z),(_B,_X),(_B,_d),(_B,_Y)))
if mibBuilder.loadTexts:irLdamAlarmCleared.setStatus(_C)
irIpmiDiscreteDeassertEvent=NotificationType((1,3,6,1,4,1,33,100,3,2,36))
irIpmiDiscreteDeassertEvent.setObjects(*((_D,_r),(_D,_s)))
if mibBuilder.loadTexts:irIpmiDiscreteDeassertEvent.setStatus(_C)
irIpmiDiscreteAssertEvent=NotificationType((1,3,6,1,4,1,33,100,3,2,37))
irIpmiDiscreteAssertEvent.setObjects(*((_D,_r),(_D,_s)))
if mibBuilder.loadTexts:irIpmiDiscreteAssertEvent.setStatus(_C)
irIpmiThresholdEvent=NotificationType((1,3,6,1,4,1,33,100,3,2,38))
irIpmiThresholdEvent.setObjects(*((_D,_A2),(_D,_A1),(_D,_A0),(_D,_z)))
if mibBuilder.loadTexts:irIpmiThresholdEvent.setStatus(_C)
mibBuilder.exportSymbols(_F,**{'irTrapMib':irTrapMib,'irTrapObjects':irTrapObjects,_A7:irTextString,_G:irTimeStamp,_v:irUserName,_A8:irIpAddress,'irTraps':irTraps,'irNotifyEvent':irNotifyEvent,'irTempHighTholdAlarmRaised':irTempHighTholdAlarmRaised,'irTempHighTholdAlarmCleared':irTempHighTholdAlarmCleared,'irTempLowTholdAlarmRaised':irTempLowTholdAlarmRaised,'irTempLowTholdAlarmCleared':irTempLowTholdAlarmCleared,'irHumidityHighTholdAlarmRaised':irHumidityHighTholdAlarmRaised,'irHumidityHighTholdAlarmCleared':irHumidityHighTholdAlarmCleared,'irHumidityLowTholdAlarmRaised':irHumidityLowTholdAlarmRaised,'irHumidityLowTholdAlarmCleared':irHumidityLowTholdAlarmCleared,'irClusterSyncStarted':irClusterSyncStarted,'irClusterSyncCompleted':irClusterSyncCompleted,'irClusterSoftwareUpdateStarted':irClusterSoftwareUpdateStarted,'irClusterSoftwareUpdateCompleted':irClusterSoftwareUpdateCompleted,'irClusterBootloaderUpdateStarted':irClusterBootloaderUpdateStarted,'irClusterBootloaderUpdateCompleted':irClusterBootloaderUpdateCompleted,'irPowerSupplyStatusChanged':irPowerSupplyStatusChanged,'irLoginFailed':irLoginFailed,'irHdamAlarmRaised':irHdamAlarmRaised,'irHdamAlarmCleared':irHdamAlarmCleared,'irHdamContactLost':irHdamContactLost,'irHdamContactRegained':irHdamContactRegained,'irHdamPowerStatusChanged':irHdamPowerStatusChanged,'irOnBoardLowTempExceeded':irOnBoardLowTempExceeded,'irOnBoardLowTempCleared':irOnBoardLowTempCleared,'irOnBoardHighTempExceeded':irOnBoardHighTempExceeded,'irOnBoardHighTempCleared':irOnBoardHighTempCleared,'irAdminLoginFailed':irAdminLoginFailed,'irEnetPortBondLinkStatusChanged':irEnetPortBondLinkStatusChanged,'irHdamAnalogHighAlarmRaised':irHdamAnalogHighAlarmRaised,'irHdamAnalogHighAlarmCleared':irHdamAnalogHighAlarmCleared,'irHdamAnalogLowAlarmRaised':irHdamAnalogLowAlarmRaised,'irHdamAnalogLowAlarmCleared':irHdamAnalogLowAlarmCleared,'irLdamAlarmRaised':irLdamAlarmRaised,'irLdamAlarmCleared':irLdamAlarmCleared,'irIpmiDiscreteDeassertEvent':irIpmiDiscreteDeassertEvent,'irIpmiDiscreteAssertEvent':irIpmiDiscreteAssertEvent,'irIpmiThresholdEvent':irIpmiThresholdEvent})