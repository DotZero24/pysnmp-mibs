_L='currentlyAuthorizedMacsIndex'
_K='multicast'
_J='learned'
_I='invalid'
_H='unused'
_G='not-accessible'
_F='macTableIndex'
_E='G6-MAC-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Mac_ObjectIdentity=ObjectIdentity
mac=_Mac_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,86))
_MacFilterPort_Type=DisplayString
_MacFilterPort_Object=MibScalar
macFilterPort=_MacFilterPort_Object((1,3,6,1,4,1,3181,10,6,1,86,1),_MacFilterPort_Type())
macFilterPort.setMaxAccess(_D)
if mibBuilder.loadTexts:macFilterPort.setStatus(_A)
_MacFilterUserPorts_Type=DisplayString
_MacFilterUserPorts_Object=MibScalar
macFilterUserPorts=_MacFilterUserPorts_Object((1,3,6,1,4,1,3181,10,6,1,86,2),_MacFilterUserPorts_Type())
macFilterUserPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:macFilterUserPorts.setStatus(_A)
_MacFilterVlan_Type=DisplayString
_MacFilterVlan_Object=MibScalar
macFilterVlan=_MacFilterVlan_Object((1,3,6,1,4,1,3181,10,6,1,86,3),_MacFilterVlan_Type())
macFilterVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:macFilterVlan.setStatus(_A)
_MacFilterMac_Type=DisplayString
_MacFilterMac_Object=MibScalar
macFilterMac=_MacFilterMac_Object((1,3,6,1,4,1,3181,10,6,1,86,4),_MacFilterMac_Type())
macFilterMac.setMaxAccess(_D)
if mibBuilder.loadTexts:macFilterMac.setStatus(_A)
_MacFilterCustom_Type=DisplayString
_MacFilterCustom_Object=MibScalar
macFilterCustom=_MacFilterCustom_Object((1,3,6,1,4,1,3181,10,6,1,86,5),_MacFilterCustom_Type())
macFilterCustom.setMaxAccess(_D)
if mibBuilder.loadTexts:macFilterCustom.setStatus(_A)
_MacFilterMulticastVlan_Type=DisplayString
_MacFilterMulticastVlan_Object=MibScalar
macFilterMulticastVlan=_MacFilterMulticastVlan_Object((1,3,6,1,4,1,3181,10,6,1,86,6),_MacFilterMulticastVlan_Type())
macFilterMulticastVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:macFilterMulticastVlan.setStatus(_A)
_MacFilterMulticastPort_Type=DisplayString
_MacFilterMulticastPort_Object=MibScalar
macFilterMulticastPort=_MacFilterMulticastPort_Object((1,3,6,1,4,1,3181,10,6,1,86,7),_MacFilterMulticastPort_Type())
macFilterMulticastPort.setMaxAccess(_D)
if mibBuilder.loadTexts:macFilterMulticastPort.setStatus(_A)
_MacClearLearnedMacTable_Type=DisplayString
_MacClearLearnedMacTable_Object=MibScalar
macClearLearnedMacTable=_MacClearLearnedMacTable_Object((1,3,6,1,4,1,3181,10,6,1,86,8),_MacClearLearnedMacTable_Type())
macClearLearnedMacTable.setMaxAccess(_D)
if mibBuilder.loadTexts:macClearLearnedMacTable.setStatus(_A)
_MacClearMacTableForVlan_Type=DisplayString
_MacClearMacTableForVlan_Object=MibScalar
macClearMacTableForVlan=_MacClearMacTableForVlan_Object((1,3,6,1,4,1,3181,10,6,1,86,9),_MacClearMacTableForVlan_Type())
macClearMacTableForVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:macClearMacTableForVlan.setStatus(_A)
class _MacHideMacsOnLinkPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_MacHideMacsOnLinkPorts_Type.__name__=_B
_MacHideMacsOnLinkPorts_Object=MibScalar
macHideMacsOnLinkPorts=_MacHideMacsOnLinkPorts_Object((1,3,6,1,4,1,3181,10,6,1,86,10),_MacHideMacsOnLinkPorts_Type())
macHideMacsOnLinkPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:macHideMacsOnLinkPorts.setStatus(_A)
class _MacGlobalAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MacGlobalAgingTime_Type.__name__=_B
_MacGlobalAgingTime_Object=MibScalar
macGlobalAgingTime=_MacGlobalAgingTime_Object((1,3,6,1,4,1,3181,10,6,1,86,11),_MacGlobalAgingTime_Type())
macGlobalAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:macGlobalAgingTime.setStatus(_A)
class _MacNumberOfEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MacNumberOfEntries_Type.__name__=_B
_MacNumberOfEntries_Object=MibScalar
macNumberOfEntries=_MacNumberOfEntries_Object((1,3,6,1,4,1,3181,10,6,1,86,100),_MacNumberOfEntries_Type())
macNumberOfEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:macNumberOfEntries.setStatus(_A)
class _MacNumberOfIgmpEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MacNumberOfIgmpEntries_Type.__name__=_B
_MacNumberOfIgmpEntries_Object=MibScalar
macNumberOfIgmpEntries=_MacNumberOfIgmpEntries_Object((1,3,6,1,4,1,3181,10,6,1,86,101),_MacNumberOfIgmpEntries_Type())
macNumberOfIgmpEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:macNumberOfIgmpEntries.setStatus(_A)
class _MacUsedAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MacUsedAgingTime_Type.__name__=_B
_MacUsedAgingTime_Object=MibScalar
macUsedAgingTime=_MacUsedAgingTime_Object((1,3,6,1,4,1,3181,10,6,1,86,102),_MacUsedAgingTime_Type())
macUsedAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:macUsedAgingTime.setStatus(_A)
class _MacNumberOfHiddenEntires_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MacNumberOfHiddenEntires_Type.__name__=_B
_MacNumberOfHiddenEntires_Object=MibScalar
macNumberOfHiddenEntires=_MacNumberOfHiddenEntires_Object((1,3,6,1,4,1,3181,10,6,1,86,103),_MacNumberOfHiddenEntires_Type())
macNumberOfHiddenEntires.setMaxAccess(_C)
if mibBuilder.loadTexts:macNumberOfHiddenEntires.setStatus(_A)
_MacTableTable_Object=MibTable
macTableTable=_MacTableTable_Object((1,3,6,1,4,1,3181,10,6,1,86,104))
if mibBuilder.loadTexts:macTableTable.setStatus(_A)
_MacTableEntry_Object=MibTableRow
macTableEntry=_MacTableEntry_Object((1,3,6,1,4,1,3181,10,6,1,86,104,1))
macTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:macTableEntry.setStatus(_A)
class _MacTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_MacTableIndex_Type.__name__=_B
_MacTableIndex_Object=MibTableColumn
macTableIndex=_MacTableIndex_Object((1,3,6,1,4,1,3181,10,6,1,86,104,1,1),_MacTableIndex_Type())
macTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:macTableIndex.setStatus(_A)
_MacTableMac_Type=MacAddress
_MacTableMac_Object=MibTableColumn
macTableMac=_MacTableMac_Object((1,3,6,1,4,1,3181,10,6,1,86,104,1,2),_MacTableMac_Type())
macTableMac.setMaxAccess(_C)
if mibBuilder.loadTexts:macTableMac.setStatus(_A)
class _MacTablePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MacTablePort_Type.__name__=_B
_MacTablePort_Object=MibTableColumn
macTablePort=_MacTablePort_Object((1,3,6,1,4,1,3181,10,6,1,86,104,1,3),_MacTablePort_Type())
macTablePort.setMaxAccess(_C)
if mibBuilder.loadTexts:macTablePort.setStatus(_A)
class _MacTableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),('other',1),(_I,2),(_J,3),('self',4),('pacc',5),(_K,6)))
_MacTableState_Type.__name__=_B
_MacTableState_Object=MibTableColumn
macTableState=_MacTableState_Object((1,3,6,1,4,1,3181,10,6,1,86,104,1,4),_MacTableState_Type())
macTableState.setMaxAccess(_C)
if mibBuilder.loadTexts:macTableState.setStatus(_A)
class _MacTableVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MacTableVlan_Type.__name__=_B
_MacTableVlan_Object=MibTableColumn
macTableVlan=_MacTableVlan_Object((1,3,6,1,4,1,3181,10,6,1,86,104,1,5),_MacTableVlan_Type())
macTableVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:macTableVlan.setStatus(_A)
_CurrentlyAuthorizedMacsTable_Object=MibTable
currentlyAuthorizedMacsTable=_CurrentlyAuthorizedMacsTable_Object((1,3,6,1,4,1,3181,10,6,1,86,105))
if mibBuilder.loadTexts:currentlyAuthorizedMacsTable.setStatus(_A)
_CurrentlyAuthorizedMacsEntry_Object=MibTableRow
currentlyAuthorizedMacsEntry=_CurrentlyAuthorizedMacsEntry_Object((1,3,6,1,4,1,3181,10,6,1,86,105,1))
currentlyAuthorizedMacsEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:currentlyAuthorizedMacsEntry.setStatus(_A)
class _CurrentlyAuthorizedMacsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CurrentlyAuthorizedMacsIndex_Type.__name__=_B
_CurrentlyAuthorizedMacsIndex_Object=MibTableColumn
currentlyAuthorizedMacsIndex=_CurrentlyAuthorizedMacsIndex_Object((1,3,6,1,4,1,3181,10,6,1,86,105,1,1),_CurrentlyAuthorizedMacsIndex_Type())
currentlyAuthorizedMacsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:currentlyAuthorizedMacsIndex.setStatus(_A)
_CurrentlyAuthorizedMacsMac_Type=MacAddress
_CurrentlyAuthorizedMacsMac_Object=MibTableColumn
currentlyAuthorizedMacsMac=_CurrentlyAuthorizedMacsMac_Object((1,3,6,1,4,1,3181,10,6,1,86,105,1,2),_CurrentlyAuthorizedMacsMac_Type())
currentlyAuthorizedMacsMac.setMaxAccess(_C)
if mibBuilder.loadTexts:currentlyAuthorizedMacsMac.setStatus(_A)
class _CurrentlyAuthorizedMacsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CurrentlyAuthorizedMacsPort_Type.__name__=_B
_CurrentlyAuthorizedMacsPort_Object=MibTableColumn
currentlyAuthorizedMacsPort=_CurrentlyAuthorizedMacsPort_Object((1,3,6,1,4,1,3181,10,6,1,86,105,1,3),_CurrentlyAuthorizedMacsPort_Type())
currentlyAuthorizedMacsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:currentlyAuthorizedMacsPort.setStatus(_A)
class _CurrentlyAuthorizedMacsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),('other',1),(_I,2),(_J,3),('self',4),('pacc',5),(_K,6)))
_CurrentlyAuthorizedMacsState_Type.__name__=_B
_CurrentlyAuthorizedMacsState_Object=MibTableColumn
currentlyAuthorizedMacsState=_CurrentlyAuthorizedMacsState_Object((1,3,6,1,4,1,3181,10,6,1,86,105,1,4),_CurrentlyAuthorizedMacsState_Type())
currentlyAuthorizedMacsState.setMaxAccess(_C)
if mibBuilder.loadTexts:currentlyAuthorizedMacsState.setStatus(_A)
class _CurrentlyAuthorizedMacsVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CurrentlyAuthorizedMacsVlan_Type.__name__=_B
_CurrentlyAuthorizedMacsVlan_Object=MibTableColumn
currentlyAuthorizedMacsVlan=_CurrentlyAuthorizedMacsVlan_Object((1,3,6,1,4,1,3181,10,6,1,86,105,1,5),_CurrentlyAuthorizedMacsVlan_Type())
currentlyAuthorizedMacsVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:currentlyAuthorizedMacsVlan.setStatus(_A)
class _CurrentlyAuthorizedMacsDatabase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CurrentlyAuthorizedMacsDatabase_Type.__name__=_B
_CurrentlyAuthorizedMacsDatabase_Object=MibTableColumn
currentlyAuthorizedMacsDatabase=_CurrentlyAuthorizedMacsDatabase_Object((1,3,6,1,4,1,3181,10,6,1,86,105,1,6),_CurrentlyAuthorizedMacsDatabase_Type())
currentlyAuthorizedMacsDatabase.setMaxAccess(_C)
if mibBuilder.loadTexts:currentlyAuthorizedMacsDatabase.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'device':device,'mac':mac,'macFilterPort':macFilterPort,'macFilterUserPorts':macFilterUserPorts,'macFilterVlan':macFilterVlan,'macFilterMac':macFilterMac,'macFilterCustom':macFilterCustom,'macFilterMulticastVlan':macFilterMulticastVlan,'macFilterMulticastPort':macFilterMulticastPort,'macClearLearnedMacTable':macClearLearnedMacTable,'macClearMacTableForVlan':macClearMacTableForVlan,'macHideMacsOnLinkPorts':macHideMacsOnLinkPorts,'macGlobalAgingTime':macGlobalAgingTime,'macNumberOfEntries':macNumberOfEntries,'macNumberOfIgmpEntries':macNumberOfIgmpEntries,'macUsedAgingTime':macUsedAgingTime,'macNumberOfHiddenEntires':macNumberOfHiddenEntires,'macTableTable':macTableTable,'macTableEntry':macTableEntry,_F:macTableIndex,'macTableMac':macTableMac,'macTablePort':macTablePort,'macTableState':macTableState,'macTableVlan':macTableVlan,'currentlyAuthorizedMacsTable':currentlyAuthorizedMacsTable,'currentlyAuthorizedMacsEntry':currentlyAuthorizedMacsEntry,_L:currentlyAuthorizedMacsIndex,'currentlyAuthorizedMacsMac':currentlyAuthorizedMacsMac,'currentlyAuthorizedMacsPort':currentlyAuthorizedMacsPort,'currentlyAuthorizedMacsState':currentlyAuthorizedMacsState,'currentlyAuthorizedMacsVlan':currentlyAuthorizedMacsVlan,'currentlyAuthorizedMacsDatabase':currentlyAuthorizedMacsDatabase})