_R='slTestsTrapsLoopbackActive'
_Q='slTestsIfLoopType'
_P='slTestsIfLoopIfIndex'
_O='optApsConfigUserWorkingIndex'
_N='optApsConfigActiveConnectionRx'
_M='slEventVal'
_L='slEventUser'
_K='slEventType'
_J='slEventIfIndex'
_I='slAlarmType'
_H='slAlarmSeverity'
_G='slAlarmServiceAffect'
_F='slAlarmIfIndex'
_E='slAlarmActive'
_D='SL-OPT-APS-MIB'
_C='SL-TESTS-MIB'
_B='SL-EVENT-MIB'
_A='SL-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
slAlarmActive,slAlarmIfIndex,slAlarmServiceAffect,slAlarmSeverity,slAlarmType=mibBuilder.importSymbols(_A,_E,_F,_G,_H,_I)
slEventIfIndex,slEventType,slEventUser,slEventVal=mibBuilder.importSymbols(_B,_J,_K,_L,_M)
smartoptics,=mibBuilder.importSymbols('SL-NE-MIB','smartoptics')
optApsConfigActiveConnectionRx,optApsConfigUserWorkingIndex=mibBuilder.importSymbols(_D,_N,_O)
slTestsIfLoopIfIndex,slTestsIfLoopType,slTestsTrapsLoopbackActive=mibBuilder.importSymbols(_C,_P,_Q,_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
slAlarmTrapV1=NotificationType((1,3,6,1,4,1,4515,0,101))
slAlarmTrapV1.setObjects(*((_A,_F),(_A,_I),(_A,_H),(_A,_G),(_A,_E)))
if mibBuilder.loadTexts:slAlarmTrapV1.setStatus('')
optApsTrapSwitchoverV1=NotificationType((1,3,6,1,4,1,4515,0,102))
optApsTrapSwitchoverV1.setObjects(*((_D,_O),(_D,_N)))
if mibBuilder.loadTexts:optApsTrapSwitchoverV1.setStatus('')
slTestsTrapsLoopbackTableChangedV1=NotificationType((1,3,6,1,4,1,4515,0,103))
slTestsTrapsLoopbackTableChangedV1.setObjects(*((_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:slTestsTrapsLoopbackTableChangedV1.setStatus('')
slEventTrapV1=NotificationType((1,3,6,1,4,1,4515,0,104))
slEventTrapV1.setObjects(*((_B,_J),(_B,_K),(_B,_M),(_B,_L)))
if mibBuilder.loadTexts:slEventTrapV1.setStatus('')
mibBuilder.exportSymbols('SL-TRAP-OPT-MIB',**{'slAlarmTrapV1':slAlarmTrapV1,'optApsTrapSwitchoverV1':optApsTrapSwitchoverV1,'slTestsTrapsLoopbackTableChangedV1':slTestsTrapsLoopbackTableChangedV1,'slEventTrapV1':slEventTrapV1})