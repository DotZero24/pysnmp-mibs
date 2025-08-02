_N='current'
_M='cfprFaultInstType'
_L='cfprFaultInstSeverity'
_K='cfprFaultInstOccur'
_J='cfprFaultInstLastTransition'
_I='cfprFaultInstInstanceId'
_H='cfprFaultInstId'
_G='cfprFaultInstDescr'
_F='cfprFaultInstCreated'
_E='cfprFaultInstCode'
_D='cfprFaultInstCause'
_C='cfprFaultInstAffectedObjectId'
_B='cfprFaultInstAffectedObjectDn'
_A='CISCO-FIREPOWER-FAULT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cfprFaultInstAffectedObjectDn,cfprFaultInstAffectedObjectId,cfprFaultInstCause,cfprFaultInstCode,cfprFaultInstCreated,cfprFaultInstDescr,cfprFaultInstId,cfprFaultInstInstanceId,cfprFaultInstLastTransition,cfprFaultInstOccur,cfprFaultInstSeverity,cfprFaultInstType=mibBuilder.importSymbols(_A,_B,_C,_D,_E,_F,_G,_H,_I,_J,_K,_L,_M)
ciscoFirepowerMIB,=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','ciscoFirepowerMIB')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoFirepowerMIBNotifs=ModuleIdentity((1,3,6,1,4,1,9,9,826,0))
if mibBuilder.loadTexts:ciscoFirepowerMIBNotifs.setRevisions(('2010-01-29 00:00',))
cfprFaultActiveNotif=NotificationType((1,3,6,1,4,1,9,9,826,0,1))
cfprFaultActiveNotif.setObjects(*((_A,_I),(_A,_G),(_A,_C),(_A,_B),(_A,_F),(_A,_J),(_A,_E),(_A,_M),(_A,_D),(_A,_L),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:cfprFaultActiveNotif.setStatus(_N)
cfprFaultClearNotif=NotificationType((1,3,6,1,4,1,9,9,826,0,2))
cfprFaultClearNotif.setObjects(*((_A,_I),(_A,_G),(_A,_C),(_A,_B),(_A,_F),(_A,_J),(_A,_E),(_A,_M),(_A,_D),(_A,_L),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:cfprFaultClearNotif.setStatus(_N)
mibBuilder.exportSymbols('CISCO-FIREPOWER-NOTIFS-MIB',**{'ciscoFirepowerMIBNotifs':ciscoFirepowerMIBNotifs,'cfprFaultActiveNotif':cfprFaultActiveNotif,'cfprFaultClearNotif':cfprFaultClearNotif})