_g='slTestsTrapsLoopbackActive'
_f='slTestsIfLoopType'
_e='slTestsIfLoopIfIndex'
_d='optApsConfigUserWorkingIndex'
_c='optApsConfigActiveConnectionRx'
_b='slGenEventVal'
_a='slGenEventUser'
_Z='slGenEventType'
_Y='slGenEventIfIndex'
_X='slEventVal'
_W='slEventUser'
_V='slEventType'
_U='slEventInventoryType'
_T='slEventInventorySerial'
_S='slEventInventoryPartnum'
_R='slEventInventoryIfIndex'
_Q='slEventInventoryAction'
_P='slEventIfIndex'
_O='edfaStatus'
_N='edfaOperControlMode'
_M='slAlarmType'
_L='slAlarmSeverity'
_K='slAlarmServiceAffect'
_J='slAlarmIfIndex'
_I='slAlarmActive'
_H='tftpStatus'
_G='RAD-MIB'
_F='SL-OPT-APS-MIB'
_E='edfaIfIndex'
_D='SL-TESTS-MIB'
_C='SL-EDFA-MIB'
_B='SL-ALARM-MIB'
_A='SL-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
tftpStatus,=mibBuilder.importSymbols(_G,_H)
slAlarmActive,slAlarmIfIndex,slAlarmServiceAffect,slAlarmSeverity,slAlarmType=mibBuilder.importSymbols(_B,_I,_J,_K,_L,_M)
edfaIfIndex,edfaOperControlMode,edfaStatus=mibBuilder.importSymbols(_C,_E,_N,_O)
slEventIfIndex,slEventInventoryAction,slEventInventoryIfIndex,slEventInventoryPartnum,slEventInventorySerial,slEventInventoryType,slEventType,slEventUser,slEventVal,slGenEventIfIndex,slGenEventType,slGenEventUser,slGenEventVal=mibBuilder.importSymbols(_A,_P,_Q,_R,_S,_T,_U,_V,_W,_X,_Y,_Z,_a,_b)
smartoptics,=mibBuilder.importSymbols('SL-NE-MIB','smartoptics')
optApsConfigActiveConnectionRx,optApsConfigUserWorkingIndex=mibBuilder.importSymbols(_F,_c,_d)
slTestsIfLoopIfIndex,slTestsIfLoopType,slTestsTrapsLoopbackActive=mibBuilder.importSymbols(_D,_e,_f,_g)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
slAlarmTrapV1=NotificationType((1,3,6,1,4,1,4515,0,101))
slAlarmTrapV1.setObjects(*((_B,_J),(_B,_M),(_B,_L),(_B,_K),(_B,_I)))
if mibBuilder.loadTexts:slAlarmTrapV1.setStatus('')
slTestsTrapsLoopbackTableChangedV1=NotificationType((1,3,6,1,4,1,4515,0,122))
slTestsTrapsLoopbackTableChangedV1.setObjects(*((_D,_e),(_D,_f),(_D,_g)))
if mibBuilder.loadTexts:slTestsTrapsLoopbackTableChangedV1.setStatus('')
edfaStatusChangeV1=NotificationType((1,3,6,1,4,1,4515,0,128))
edfaStatusChangeV1.setObjects(*((_C,_E),(_C,_O)))
if mibBuilder.loadTexts:edfaStatusChangeV1.setStatus('')
edfaControlModeChangeV1=NotificationType((1,3,6,1,4,1,4515,0,129))
edfaControlModeChangeV1.setObjects(*((_C,_E),(_C,_N)))
if mibBuilder.loadTexts:edfaControlModeChangeV1.setStatus('')
optApsTrapSwitchoverV1=NotificationType((1,3,6,1,4,1,4515,0,130))
optApsTrapSwitchoverV1.setObjects(*((_F,_d),(_F,_c)))
if mibBuilder.loadTexts:optApsTrapSwitchoverV1.setStatus('')
slEventTrapV1=NotificationType((1,3,6,1,4,1,4515,0,131))
slEventTrapV1.setObjects(*((_A,_P),(_A,_V),(_A,_X),(_A,_W)))
if mibBuilder.loadTexts:slEventTrapV1.setStatus('')
tftpStatusChangeTrapV1=NotificationType((1,3,6,1,4,1,4515,0,132))
tftpStatusChangeTrapV1.setObjects((_G,_H))
if mibBuilder.loadTexts:tftpStatusChangeTrapV1.setStatus('')
slEventInventoryTrapV1=NotificationType((1,3,6,1,4,1,4515,0,133))
slEventInventoryTrapV1.setObjects(*((_A,_R),(_A,_Q),(_A,_U),(_A,_T),(_A,_S)))
if mibBuilder.loadTexts:slEventInventoryTrapV1.setStatus('')
slGenEventTrapV1=NotificationType((1,3,6,1,4,1,4515,0,134))
slGenEventTrapV1.setObjects(*((_A,_Y),(_A,_Z),(_A,_b),(_A,_a)))
if mibBuilder.loadTexts:slGenEventTrapV1.setStatus('')
mibBuilder.exportSymbols('SL-TRAP-MIB',**{'slAlarmTrapV1':slAlarmTrapV1,'slTestsTrapsLoopbackTableChangedV1':slTestsTrapsLoopbackTableChangedV1,'edfaStatusChangeV1':edfaStatusChangeV1,'edfaControlModeChangeV1':edfaControlModeChangeV1,'optApsTrapSwitchoverV1':optApsTrapSwitchoverV1,'slEventTrapV1':slEventTrapV1,'tftpStatusChangeTrapV1':tftpStatusChangeTrapV1,'slEventInventoryTrapV1':slEventInventoryTrapV1,'slGenEventTrapV1':slGenEventTrapV1})