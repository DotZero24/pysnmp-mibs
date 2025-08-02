_Q='ciscoMpoaExtMpsInterfaceMappingGroup'
_P='ciscoMpoaExtMpcInterfaceMappingGroup'
_O='ciscoMpoaExtShorcutVCCMIBGroup'
_N='cMpsInterfaceMappingRowStatus'
_M='cMpsInterfaceMappingIndex'
_L='cMpcInterfaceMappingRowStatus'
_K='cMpcInterfaceMappingIndex'
_J='cmpcDestAtmAddr'
_I='not-accessible'
_H='cmpcSCVci'
_G='cmpcSCVpi'
_F='mpsIndex'
_E='mpcIndex'
_D='read-create'
_C='MPOA-MIB'
_B='CISCO-MPOA-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmAddress,=mibBuilder.importSymbols('ATM-FORUM-TC-MIB','AtmAddress')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VciInteger,VpiInteger=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB','VciInteger','VpiInteger')
mpcIndex,mpsIndex=mibBuilder.importSymbols(_C,_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoMpoaExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,99999))
if mibBuilder.loadTexts:ciscoMpoaExtMIB.setRevisions(('2000-01-10 12:30',))
_CiscoMpoaExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMpoaExtMIBObjects=_CiscoMpoaExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,99999,1))
_CMpcExtShortcutVCC_ObjectIdentity=ObjectIdentity
cMpcExtShortcutVCC=_CMpcExtShortcutVCC_ObjectIdentity((1,3,6,1,4,1,9,9,99999,1,1))
_CMpcExtShortcutVCCTable_Object=MibTable
cMpcExtShortcutVCCTable=_CMpcExtShortcutVCCTable_Object((1,3,6,1,4,1,9,9,99999,1,1,1))
if mibBuilder.loadTexts:cMpcExtShortcutVCCTable.setStatus(_A)
_CMpcExtShortcutVCCEntry_Object=MibTableRow
cMpcExtShortcutVCCEntry=_CMpcExtShortcutVCCEntry_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1))
cMpcExtShortcutVCCEntry.setIndexNames((0,_C,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cMpcExtShortcutVCCEntry.setStatus(_A)
_CmpcSCVpi_Type=VpiInteger
_CmpcSCVpi_Object=MibTableColumn
cmpcSCVpi=_CmpcSCVpi_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,1),_CmpcSCVpi_Type())
cmpcSCVpi.setMaxAccess(_I)
if mibBuilder.loadTexts:cmpcSCVpi.setStatus(_A)
_CmpcSCVci_Type=VciInteger
_CmpcSCVci_Object=MibTableColumn
cmpcSCVci=_CmpcSCVci_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,2),_CmpcSCVci_Type())
cmpcSCVci.setMaxAccess(_I)
if mibBuilder.loadTexts:cmpcSCVci.setStatus(_A)
_CmpcDestAtmAddr_Type=AtmAddress
_CmpcDestAtmAddr_Object=MibTableColumn
cmpcDestAtmAddr=_CmpcDestAtmAddr_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,3),_CmpcDestAtmAddr_Type())
cmpcDestAtmAddr.setMaxAccess('read-only')
if mibBuilder.loadTexts:cmpcDestAtmAddr.setStatus(_A)
_CMpcInterface_ObjectIdentity=ObjectIdentity
cMpcInterface=_CMpcInterface_ObjectIdentity((1,3,6,1,4,1,9,9,99999,1,2))
_CMpcInterfaceMappingTable_Object=MibTable
cMpcInterfaceMappingTable=_CMpcInterfaceMappingTable_Object((1,3,6,1,4,1,9,9,99999,1,2,1))
if mibBuilder.loadTexts:cMpcInterfaceMappingTable.setStatus(_A)
_CMpcInterfaceMappingEntry_Object=MibTableRow
cMpcInterfaceMappingEntry=_CMpcInterfaceMappingEntry_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1))
cMpcInterfaceMappingEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cMpcInterfaceMappingEntry.setStatus(_A)
_CMpcInterfaceMappingIndex_Type=InterfaceIndex
_CMpcInterfaceMappingIndex_Object=MibTableColumn
cMpcInterfaceMappingIndex=_CMpcInterfaceMappingIndex_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1,1),_CMpcInterfaceMappingIndex_Type())
cMpcInterfaceMappingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cMpcInterfaceMappingIndex.setStatus(_A)
_CMpcInterfaceMappingRowStatus_Type=RowStatus
_CMpcInterfaceMappingRowStatus_Object=MibTableColumn
cMpcInterfaceMappingRowStatus=_CMpcInterfaceMappingRowStatus_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1,2),_CMpcInterfaceMappingRowStatus_Type())
cMpcInterfaceMappingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cMpcInterfaceMappingRowStatus.setStatus(_A)
_CMpsInterface_ObjectIdentity=ObjectIdentity
cMpsInterface=_CMpsInterface_ObjectIdentity((1,3,6,1,4,1,9,9,99999,1,3))
_CMpsInterfaceMappingTable_Object=MibTable
cMpsInterfaceMappingTable=_CMpsInterfaceMappingTable_Object((1,3,6,1,4,1,9,9,99999,1,3,1))
if mibBuilder.loadTexts:cMpsInterfaceMappingTable.setStatus(_A)
_CMpsInterfaceMappingEntry_Object=MibTableRow
cMpsInterfaceMappingEntry=_CMpsInterfaceMappingEntry_Object((1,3,6,1,4,1,9,9,99999,1,3,1,1))
cMpsInterfaceMappingEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cMpsInterfaceMappingEntry.setStatus(_A)
_CMpsInterfaceMappingIndex_Type=InterfaceIndex
_CMpsInterfaceMappingIndex_Object=MibTableColumn
cMpsInterfaceMappingIndex=_CMpsInterfaceMappingIndex_Object((1,3,6,1,4,1,9,9,99999,1,3,1,1,1),_CMpsInterfaceMappingIndex_Type())
cMpsInterfaceMappingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cMpsInterfaceMappingIndex.setStatus(_A)
_CMpsInterfaceMappingRowStatus_Type=RowStatus
_CMpsInterfaceMappingRowStatus_Object=MibTableColumn
cMpsInterfaceMappingRowStatus=_CMpsInterfaceMappingRowStatus_Object((1,3,6,1,4,1,9,9,99999,1,3,1,1,2),_CMpsInterfaceMappingRowStatus_Type())
cMpsInterfaceMappingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cMpsInterfaceMappingRowStatus.setStatus(_A)
_CiscoMpoaExtMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoMpoaExtMIBNotificationPrefix=_CiscoMpoaExtMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,99999,2))
_CiscoMpoaExtMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoMpoaExtMIBNotifications=_CiscoMpoaExtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,99999,2,0))
_CiscoMpoaExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoMpoaExtMIBConformance=_CiscoMpoaExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,99999,3))
_CiscoMpoaExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoMpoaExtMIBCompliances=_CiscoMpoaExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,99999,3,1))
_CiscoMpoaExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoMpoaExtMIBGroups=_CiscoMpoaExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,99999,3,2))
ciscoMpoaExtShorcutVCCMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,99999,3,2,1))
ciscoMpoaExtShorcutVCCMIBGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoMpoaExtShorcutVCCMIBGroup.setStatus(_A)
ciscoMpoaExtMpcInterfaceMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,99999,3,2,2))
ciscoMpoaExtMpcInterfaceMappingGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoMpoaExtMpcInterfaceMappingGroup.setStatus(_A)
ciscoMpoaExtMpsInterfaceMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,99999,3,2,3))
ciscoMpoaExtMpsInterfaceMappingGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoMpoaExtMpsInterfaceMappingGroup.setStatus(_A)
ciscoMpoaExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,99999,3,1,1))
ciscoMpoaExtMIBCompliance.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoMpoaExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoMpoaExtMIB':ciscoMpoaExtMIB,'ciscoMpoaExtMIBObjects':ciscoMpoaExtMIBObjects,'cMpcExtShortcutVCC':cMpcExtShortcutVCC,'cMpcExtShortcutVCCTable':cMpcExtShortcutVCCTable,'cMpcExtShortcutVCCEntry':cMpcExtShortcutVCCEntry,_G:cmpcSCVpi,_H:cmpcSCVci,_J:cmpcDestAtmAddr,'cMpcInterface':cMpcInterface,'cMpcInterfaceMappingTable':cMpcInterfaceMappingTable,'cMpcInterfaceMappingEntry':cMpcInterfaceMappingEntry,_K:cMpcInterfaceMappingIndex,_L:cMpcInterfaceMappingRowStatus,'cMpsInterface':cMpsInterface,'cMpsInterfaceMappingTable':cMpsInterfaceMappingTable,'cMpsInterfaceMappingEntry':cMpsInterfaceMappingEntry,_M:cMpsInterfaceMappingIndex,_N:cMpsInterfaceMappingRowStatus,'ciscoMpoaExtMIBNotificationPrefix':ciscoMpoaExtMIBNotificationPrefix,'ciscoMpoaExtMIBNotifications':ciscoMpoaExtMIBNotifications,'ciscoMpoaExtMIBConformance':ciscoMpoaExtMIBConformance,'ciscoMpoaExtMIBCompliances':ciscoMpoaExtMIBCompliances,'ciscoMpoaExtMIBCompliance':ciscoMpoaExtMIBCompliance,'ciscoMpoaExtMIBGroups':ciscoMpoaExtMIBGroups,_O:ciscoMpoaExtShorcutVCCMIBGroup,_P:ciscoMpoaExtMpcInterfaceMappingGroup,_Q:ciscoMpoaExtMpsInterfaceMappingGroup})