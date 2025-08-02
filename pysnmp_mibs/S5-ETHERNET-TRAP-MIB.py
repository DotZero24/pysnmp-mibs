_Q='s5SbsMgmViolationType'
_P='s5SbsMgmViolationIpAddress'
_O='s5EnPortLinkStatus'
_N='s5EnRedPortRemoteOperStatus'
_M='s5EnRedPortRedundMode'
_L='s5EnRedPortOperStatus'
_K='s5EnRedPortCompanionPortNum'
_J='s5EnRedPortCompanionBrdNum'
_I='s5SbsViolationStatusMACAddress'
_H='s5SbsViolationStatusPortIndx'
_G='s5SbsViolationStatusBrdIndx'
_F='s5EnPortPartStatus'
_E='s5EnPortJabberStatus'
_D='S5-ETH-REDUNDANT-LINKS-MIB'
_C='S5-SWITCH-BAYSECURE-MIB'
_B='S5-ETHERNET-COMMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
s5EnRedPortCompanionBrdNum,s5EnRedPortCompanionPortNum,s5EnRedPortOperStatus,s5EnRedPortRedundMode,s5EnRedPortRemoteOperStatus=mibBuilder.importSymbols(_D,_J,_K,_L,_M,_N)
s5EnPortJabberStatus,s5EnPortLinkStatus,s5EnPortPartStatus=mibBuilder.importSymbols(_B,_E,_O,_F)
s5EthTrap,=mibBuilder.importSymbols('S5-ROOT-MIB','s5EthTrap')
s5SbsMgmViolationIpAddress,s5SbsMgmViolationType,s5SbsViolationStatusBrdIndx,s5SbsViolationStatusMACAddress,s5SbsViolationStatusPortIndx=mibBuilder.importSymbols(_C,_P,_Q,_G,_I,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
s5EthernetTrapMib=ModuleIdentity((1,3,6,1,4,1,45,1,6,2,1,0))
if mibBuilder.loadTexts:s5EthernetTrapMib.setRevisions(('2012-02-28 00:00','2009-07-29 00:00','2009-02-25 00:00','2004-07-20 00:00'))
s5EtrSbsMacTableFull=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,1))
if mibBuilder.loadTexts:s5EtrSbsMacTableFull.setStatus(_A)
s5EtrSbsMacTableClearedForPort=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,2))
s5EtrSbsMacTableClearedForPort.setObjects(*((_C,_G),(_C,_H)))
if mibBuilder.loadTexts:s5EtrSbsMacTableClearedForPort.setStatus(_A)
s5EtrSbsMacTableCleared=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,3))
if mibBuilder.loadTexts:s5EtrSbsMacTableCleared.setStatus(_A)
s5EtrSbsMacRemoved=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,4))
s5EtrSbsMacRemoved.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:s5EtrSbsMacRemoved.setStatus(_A)
s5EtrNewSbsMacAccessViolation=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,5))
s5EtrNewSbsMacAccessViolation.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:s5EtrNewSbsMacAccessViolation.setStatus(_A)
s5EtrNewMgmAccessViolation=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,6))
s5EtrNewMgmAccessViolation.setObjects(*((_C,_Q),(_C,_P)))
if mibBuilder.loadTexts:s5EtrNewMgmAccessViolation.setStatus(_A)
s5EtrNewPortManualPart=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,7))
s5EtrNewPortManualPart.setObjects(*((_B,_F),(_B,_E)))
if mibBuilder.loadTexts:s5EtrNewPortManualPart.setStatus(_A)
s5EtrNewPortAutoPart=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,8))
s5EtrNewPortAutoPart.setObjects(*((_B,_F),(_B,_E)))
if mibBuilder.loadTexts:s5EtrNewPortAutoPart.setStatus(_A)
s5EtrNewPortDteJabbering=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,9))
s5EtrNewPortDteJabbering.setObjects((_B,_E))
if mibBuilder.loadTexts:s5EtrNewPortDteJabbering.setStatus(_A)
s5EtrNewRedPortFailure=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,10))
s5EtrNewRedPortFailure.setObjects(*((_D,_L),(_D,_J),(_D,_K),(_B,_F),(_B,_O),(_B,_E)))
if mibBuilder.loadTexts:s5EtrNewRedPortFailure.setStatus(_A)
s5EtrNewRedBadRemCfgDetected=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,11))
s5EtrNewRedBadRemCfgDetected.setObjects(*((_D,_N),(_D,_M)))
if mibBuilder.loadTexts:s5EtrNewRedBadRemCfgDetected.setStatus(_A)
s5EtrMacAddressTablesThresholdReached=NotificationType((1,3,6,1,4,1,45,1,6,2,1,0,12))
if mibBuilder.loadTexts:s5EtrMacAddressTablesThresholdReached.setStatus(_A)
s5EtrPortAutoPart=NotificationType((1,3,6,1,4,1,45,1,6,2,1,1))
s5EtrPortAutoPart.setObjects(*((_B,_F),(_B,_E)))
if mibBuilder.loadTexts:s5EtrPortAutoPart.setStatus(_A)
s5EtrPortDteJabbering=NotificationType((1,3,6,1,4,1,45,1,6,2,1,2))
s5EtrPortDteJabbering.setObjects((_B,_E))
if mibBuilder.loadTexts:s5EtrPortDteJabbering.setStatus(_A)
s5EtrRedPortFailure=NotificationType((1,3,6,1,4,1,45,1,6,2,1,3))
s5EtrRedPortFailure.setObjects(*((_D,_L),(_D,_J),(_D,_K),(_B,_F),(_B,_O),(_B,_E)))
if mibBuilder.loadTexts:s5EtrRedPortFailure.setStatus(_A)
s5EtrRedBadRemCfgDetected=NotificationType((1,3,6,1,4,1,45,1,6,2,1,4))
s5EtrRedBadRemCfgDetected.setObjects(*((_D,_N),(_D,_M)))
if mibBuilder.loadTexts:s5EtrRedBadRemCfgDetected.setStatus(_A)
s5EtrSbsMacAccessViolation=NotificationType((1,3,6,1,4,1,45,1,6,2,1,5))
s5EtrSbsMacAccessViolation.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:s5EtrSbsMacAccessViolation.setStatus(_A)
s5EtrMgmAccessViolation=NotificationType((1,3,6,1,4,1,45,1,6,2,1,6))
s5EtrMgmAccessViolation.setObjects(*((_C,_Q),(_C,_P)))
if mibBuilder.loadTexts:s5EtrMgmAccessViolation.setStatus(_A)
s5EtrPortManualPart=NotificationType((1,3,6,1,4,1,45,1,6,2,1,7))
s5EtrPortManualPart.setObjects(*((_B,_F),(_B,_E)))
if mibBuilder.loadTexts:s5EtrPortManualPart.setStatus(_A)
mibBuilder.exportSymbols('S5-ETHERNET-TRAP-MIB',**{'s5EthernetTrapMib':s5EthernetTrapMib,'s5EtrSbsMacTableFull':s5EtrSbsMacTableFull,'s5EtrSbsMacTableClearedForPort':s5EtrSbsMacTableClearedForPort,'s5EtrSbsMacTableCleared':s5EtrSbsMacTableCleared,'s5EtrSbsMacRemoved':s5EtrSbsMacRemoved,'s5EtrNewSbsMacAccessViolation':s5EtrNewSbsMacAccessViolation,'s5EtrNewMgmAccessViolation':s5EtrNewMgmAccessViolation,'s5EtrNewPortManualPart':s5EtrNewPortManualPart,'s5EtrNewPortAutoPart':s5EtrNewPortAutoPart,'s5EtrNewPortDteJabbering':s5EtrNewPortDteJabbering,'s5EtrNewRedPortFailure':s5EtrNewRedPortFailure,'s5EtrNewRedBadRemCfgDetected':s5EtrNewRedBadRemCfgDetected,'s5EtrMacAddressTablesThresholdReached':s5EtrMacAddressTablesThresholdReached,'s5EtrPortAutoPart':s5EtrPortAutoPart,'s5EtrPortDteJabbering':s5EtrPortDteJabbering,'s5EtrRedPortFailure':s5EtrRedPortFailure,'s5EtrRedBadRemCfgDetected':s5EtrRedBadRemCfgDetected,'s5EtrSbsMacAccessViolation':s5EtrSbsMacAccessViolation,'s5EtrMgmAccessViolation':s5EtrMgmAccessViolation,'s5EtrPortManualPart':s5EtrPortManualPart})