_R='cucsFaultsGroup'
_Q='cucsFaultsNotifGroup'
_P='cucsFaultClearNotif'
_O='cucsFaultActiveNotif'
_N='cucsFaultType'
_M='cucsFaultSeverity'
_L='cucsFaultProbableCause'
_K='cucsFaultOccur'
_J='cucsFaultLastModificationTime'
_I='cucsFaultDescription'
_H='cucsFaultCreationTime'
_G='cucsFaultCode'
_F='cucsFaultAffectedObjectId'
_E='cucsFaultAffectedObjectDn'
_D='CISCO-UNIFIED-COMPUTING-CONFORM-MIB'
_C='current'
_B='CISCO-UNIFIED-COMPUTING-NOTIFS-MIB'
_A='CISCO-UNIFIED-COMPUTING-FAULT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cucsFaultAffectedObjectDn,cucsFaultAffectedObjectId,cucsFaultCode,cucsFaultCreationTime,cucsFaultDescription,cucsFaultLastModificationTime,cucsFaultOccur,cucsFaultProbableCause,cucsFaultSeverity,cucsFaultType=mibBuilder.importSymbols(_A,_E,_F,_G,_H,_I,_J,_K,_L,_M,_N)
ciscoUnifiedComputingMIB,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','ciscoUnifiedComputingMIB','ciscoUnifiedComputingMIBObjects')
cucsFaultActiveNotif,cucsFaultClearNotif=mibBuilder.importSymbols(_B,_O,_P)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoUnifiedComputingMIBConform=ModuleIdentity((1,3,6,1,4,1,9,9,719,2))
if mibBuilder.loadTexts:ciscoUnifiedComputingMIBConform.setRevisions(('2010-01-29 00:00',))
_CucsFaultMIBConform_ObjectIdentity=ObjectIdentity
cucsFaultMIBConform=_CucsFaultMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,719,2,1))
_CucsFaultMIBCompliances_ObjectIdentity=ObjectIdentity
cucsFaultMIBCompliances=_CucsFaultMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,719,2,1,1))
_CucsFaultMIBGroups_ObjectIdentity=ObjectIdentity
cucsFaultMIBGroups=_CucsFaultMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,719,2,1,2))
cucsFaultsGroup=ObjectGroup((1,3,6,1,4,1,9,9,719,2,1,2,1))
cucsFaultsGroup.setObjects(*((_A,_I),(_A,_F),(_A,_E),(_A,_H),(_A,_J),(_A,_G),(_A,_N),(_A,_L),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:cucsFaultsGroup.setStatus(_C)
cucsFaultsNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,719,2,1,2,2))
cucsFaultsNotifGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cucsFaultsNotifGroup.setStatus(_C)
cucsFaultMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,719,2,1,1,1))
cucsFaultMIBCompliance.setObjects(*((_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:cucsFaultMIBCompliance.setStatus(_C)
mibBuilder.exportSymbols(_D,**{'ciscoUnifiedComputingMIBConform':ciscoUnifiedComputingMIBConform,'cucsFaultMIBConform':cucsFaultMIBConform,'cucsFaultMIBCompliances':cucsFaultMIBCompliances,'cucsFaultMIBCompliance':cucsFaultMIBCompliance,'cucsFaultMIBGroups':cucsFaultMIBGroups,_R:cucsFaultsGroup,_Q:cucsFaultsNotifGroup})