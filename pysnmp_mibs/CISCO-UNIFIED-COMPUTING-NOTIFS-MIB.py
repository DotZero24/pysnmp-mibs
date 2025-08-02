_N='current'
_M='cucsFaultType'
_L='cucsFaultSeverity'
_K='cucsFaultProbableCause'
_J='cucsFaultOccur'
_I='cucsFaultLastModificationTime'
_H='cucsFaultIndex'
_G='cucsFaultId'
_F='cucsFaultDescription'
_E='cucsFaultCreationTime'
_D='cucsFaultCode'
_C='cucsFaultAffectedObjectId'
_B='cucsFaultAffectedObjectDn'
_A='CISCO-UNIFIED-COMPUTING-FAULT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cucsFaultAffectedObjectDn,cucsFaultAffectedObjectId,cucsFaultCode,cucsFaultCreationTime,cucsFaultDescription,cucsFaultId,cucsFaultIndex,cucsFaultLastModificationTime,cucsFaultOccur,cucsFaultProbableCause,cucsFaultSeverity,cucsFaultType=mibBuilder.importSymbols(_A,_B,_C,_D,_E,_F,_G,_H,_I,_J,_K,_L,_M)
ciscoUnifiedComputingMIB,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','ciscoUnifiedComputingMIB','ciscoUnifiedComputingMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoUnifiedComputingMIBNotifs=ModuleIdentity((1,3,6,1,4,1,9,9,719,0))
if mibBuilder.loadTexts:ciscoUnifiedComputingMIBNotifs.setRevisions(('2010-01-29 00:00',))
cucsFaultActiveNotif=NotificationType((1,3,6,1,4,1,9,9,719,0,1))
cucsFaultActiveNotif.setObjects(*((_A,_H),(_A,_F),(_A,_C),(_A,_B),(_A,_E),(_A,_I),(_A,_D),(_A,_M),(_A,_K),(_A,_L),(_A,_J),(_A,_G)))
if mibBuilder.loadTexts:cucsFaultActiveNotif.setStatus(_N)
cucsFaultClearNotif=NotificationType((1,3,6,1,4,1,9,9,719,0,2))
cucsFaultClearNotif.setObjects(*((_A,_H),(_A,_F),(_A,_C),(_A,_B),(_A,_E),(_A,_I),(_A,_D),(_A,_M),(_A,_K),(_A,_L),(_A,_J),(_A,_G)))
if mibBuilder.loadTexts:cucsFaultClearNotif.setStatus(_N)
mibBuilder.exportSymbols('CISCO-UNIFIED-COMPUTING-NOTIFS-MIB',**{'ciscoUnifiedComputingMIBNotifs':ciscoUnifiedComputingMIBNotifs,'cucsFaultActiveNotif':cucsFaultActiveNotif,'cucsFaultClearNotif':cucsFaultClearNotif})