_b='NotificationType'
_a='cpqRackNetConnectorFWRev'
_Z='agentSwitchCubeType'
_Y='agentSwitchCubeSparePartNumber'
_X='agentSwitchCubeSpareName'
_W='agentSNTPServer2IPAddr'
_V='agentSNTPServer1IPAddr'
_U='agentBscSwFileStatus'
_T='agentSwitchFanIndex'
_S='agentSwitchFanCondition'
_R='agentSwitchTempSensorThreshold'
_Q='agentSwitchTempSensorTempType'
_P='agentSwitchTempSensorIndex'
_O='agentSwitchTempSensorCurrent'
_N='agentSwitchTempSensorCondition'
_M='agentBscSwFileLoadType'
_L='agentBscSwFileAddr'
_K='agentBscSwFile'
_J='cpqRackNetConnectorSparePartNumber'
_I='cpqRackUid'
_H='cpqRackNetConnectorSerialNum'
_G='cpqRackNetConnectorName'
_F='cpqRackNetConnectorLocation'
_E='cpqRackName'
_D='cpqRackCommonEnclosureSerialNum'
_C='cpqRackCommonEnclosureName'
_B='COMPAQ-AGENT-MIB'
_A='CPQRACK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
agentBscSwFile,agentBscSwFileAddr,agentBscSwFileLoadType,agentBscSwFileStatus,agentSNTPServer1IPAddr,agentSNTPServer2IPAddr,agentSwitchCubeSpareName,agentSwitchCubeSparePartNumber,agentSwitchCubeType,agentSwitchFanCondition,agentSwitchFanIndex,agentSwitchPowerSupplyCondition,agentSwitchPowerSupplyCurPwrOutput,agentSwitchPowerSupplyExhaustTemp,agentSwitchPowerSupplyInputLineStatus,agentSwitchPowerSupplyIntakeTemp,agentSwitchPowerSupplyMaxPwrOutput,agentSwitchPowerSupplyStatus,agentSwitchTempSensorCondition,agentSwitchTempSensorCurrent,agentSwitchTempSensorIndex,agentSwitchTempSensorTempType,agentSwitchTempSensorThreshold=mibBuilder.importSymbols(_B,_K,_L,_M,_U,_V,_W,_X,_Y,_Z,_S,_T,'agentSwitchPowerSupplyCondition','agentSwitchPowerSupplyCurPwrOutput','agentSwitchPowerSupplyExhaustTemp','agentSwitchPowerSupplyInputLineStatus','agentSwitchPowerSupplyIntakeTemp','agentSwitchPowerSupplyMaxPwrOutput','agentSwitchPowerSupplyStatus',_N,_O,_P,_Q,_R)
compaq_common_mgmt,=mibBuilder.importSymbols('COMPAQ-ID-REC-MIB','compaq-common-mgmt')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
cpqRackCommonEnclosureName,cpqRackCommonEnclosureSerialNum,cpqRackName,cpqRackNetConnectorFWRev,cpqRackNetConnectorLocation,cpqRackNetConnectorName,cpqRackNetConnectorSerialNum,cpqRackNetConnectorSparePartNumber,cpqRackUid=mibBuilder.importSymbols(_A,_C,_D,_E,_a,_F,_G,_H,_J,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_b,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_b,'TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_EntityMIB_ObjectIdentity=ObjectIdentity
entityMIB=_EntityMIB_ObjectIdentity((1,3,6,1,2,1,47))
_EntityMIBTraps_ObjectIdentity=ObjectIdentity
entityMIBTraps=_EntityMIBTraps_ObjectIdentity((1,3,6,1,2,1,47,2))
_EntityMIBTrapPrefix_ObjectIdentity=ObjectIdentity
entityMIBTrapPrefix=_EntityMIBTrapPrefix_ObjectIdentity((1,3,6,1,2,1,47,2,0))
entConfigChange=NotificationType((1,3,6,1,2,1,47,2,0,0,1))
if mibBuilder.loadTexts:entConfigChange.setStatus('')
switchFirmwareTransferred=NotificationType((1,3,6,1,4,1,232,0,161001))
switchFirmwareTransferred.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_B,_L),(_B,_K),(_B,_M),(_A,_a)))
if mibBuilder.loadTexts:switchFirmwareTransferred.setStatus('')
switchConfigFileTransferred=NotificationType((1,3,6,1,4,1,232,0,161002))
switchConfigFileTransferred.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_B,_L),(_B,_K),(_B,_M)))
if mibBuilder.loadTexts:switchConfigFileTransferred.setStatus('')
switchTFTPTransferSucceeded=NotificationType((1,3,6,1,4,1,232,0,161003))
switchTFTPTransferSucceeded.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_B,_L),(_B,_K),(_B,_M)))
if mibBuilder.loadTexts:switchTFTPTransferSucceeded.setStatus('')
switchTFTPTransferFailed=NotificationType((1,3,6,1,4,1,232,0,161004))
switchTFTPTransferFailed.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_B,_L),(_B,_K),(_B,_M)))
if mibBuilder.loadTexts:switchTFTPTransferFailed.setStatus('')
switchFileInvalid=NotificationType((1,3,6,1,4,1,232,0,161005))
switchFileInvalid.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_B,_L),(_B,_K),(_B,_M),(_B,_U)))
if mibBuilder.loadTexts:switchFileInvalid.setStatus('')
switchFanFailed=NotificationType((1,3,6,1,4,1,232,0,161006))
switchFanFailed.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_A,_J),(_B,_T),(_B,_S)))
if mibBuilder.loadTexts:switchFanFailed.setStatus('')
switchFanOk=NotificationType((1,3,6,1,4,1,232,0,161007))
switchFanOk.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_A,_J),(_B,_T),(_B,_S)))
if mibBuilder.loadTexts:switchFanOk.setStatus('')
switchTempSensorDegraded=NotificationType((1,3,6,1,4,1,232,0,161008))
switchTempSensorDegraded.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_A,_J),(_B,_P),(_B,_O),(_B,_R),(_B,_N),(_B,_Q)))
if mibBuilder.loadTexts:switchTempSensorDegraded.setStatus('')
switchTempSensorFailed=NotificationType((1,3,6,1,4,1,232,0,161009))
switchTempSensorFailed.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_A,_J),(_B,_P),(_B,_O),(_B,_R),(_B,_N),(_B,_Q)))
if mibBuilder.loadTexts:switchTempSensorFailed.setStatus('')
switchTempSensorOk=NotificationType((1,3,6,1,4,1,232,0,161010))
switchTempSensorOk.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_A,_J),(_B,_P),(_B,_O),(_B,_R),(_B,_N),(_B,_Q)))
if mibBuilder.loadTexts:switchTempSensorOk.setStatus('')
switchPostSuccess=NotificationType((1,3,6,1,4,1,232,0,161011))
switchPostSuccess.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:switchPostSuccess.setStatus('')
switchLoginFailure=NotificationType((1,3,6,1,4,1,232,0,161012))
switchLoginFailure.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F)))
if mibBuilder.loadTexts:switchLoginFailure.setStatus('')
switchLocationChange=NotificationType((1,3,6,1,4,1,232,0,161013))
switchLocationChange.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F)))
if mibBuilder.loadTexts:switchLocationChange.setStatus('')
switchCubeTypeChange=NotificationType((1,3,6,1,4,1,232,0,161014))
switchCubeTypeChange.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_A,_J),(_B,_Z),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:switchCubeTypeChange.setStatus('')
switchSNTPServiceUnavailable=NotificationType((1,3,6,1,4,1,232,0,161015))
switchSNTPServiceUnavailable.setObjects(*((_A,_I),(_A,_D),(_A,_H),(_A,_E),(_A,_C),(_A,_G),(_A,_F),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:switchSNTPServiceUnavailable.setStatus('')
mibBuilder.exportSymbols('CPQ-TRAPS-MIB',**{'entityMIB':entityMIB,'entityMIBTraps':entityMIBTraps,'entityMIBTrapPrefix':entityMIBTrapPrefix,'entConfigChange':entConfigChange,'switchFirmwareTransferred':switchFirmwareTransferred,'switchConfigFileTransferred':switchConfigFileTransferred,'switchTFTPTransferSucceeded':switchTFTPTransferSucceeded,'switchTFTPTransferFailed':switchTFTPTransferFailed,'switchFileInvalid':switchFileInvalid,'switchFanFailed':switchFanFailed,'switchFanOk':switchFanOk,'switchTempSensorDegraded':switchTempSensorDegraded,'switchTempSensorFailed':switchTempSensorFailed,'switchTempSensorOk':switchTempSensorOk,'switchPostSuccess':switchPostSuccess,'switchLoginFailure':switchLoginFailure,'switchLocationChange':switchLocationChange,'switchCubeTypeChange':switchCubeTypeChange,'switchSNTPServiceUnavailable':switchSNTPServiceUnavailable})