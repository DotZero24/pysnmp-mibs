_P='ciscoAal5ExtMIBGroup'
_O='cAal5VccOutDroppedCells'
_N='cAal5VccInDroppedCells'
_M='cAal5VccOutCells'
_L='cAal5VccInCells'
_K='cAal5VccOutDroppedOctets'
_J='cAal5VccInDroppedOctets'
_I='cAal5VccOutDroppedPkts'
_H='cAal5VccInDroppedPkts'
_G='cAal5ExtVccEntry'
_F='octets'
_E='packets'
_D='cells'
_C='read-only'
_B='CISCO-AAL5-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aal5VccEntry,=mibBuilder.importSymbols('ATM-MIB','aal5VccEntry')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAal5ExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9999))
if mibBuilder.loadTexts:ciscoAal5ExtMIB.setRevisions(('2001-11-05 00:00',))
_CiscoAal5ExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAal5ExtMIBObjects=_CiscoAal5ExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1))
_CAal5ExtConnections_ObjectIdentity=ObjectIdentity
cAal5ExtConnections=_CAal5ExtConnections_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1))
_CAal5ExtVccTable_Object=MibTable
cAal5ExtVccTable=_CAal5ExtVccTable_Object((1,3,6,1,4,1,9,9,9999,1,1,1))
if mibBuilder.loadTexts:cAal5ExtVccTable.setStatus(_A)
_CAal5ExtVccEntry_Object=MibTableRow
cAal5ExtVccEntry=_CAal5ExtVccEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1))
if mibBuilder.loadTexts:cAal5ExtVccEntry.setStatus(_A)
_CAal5VccInDroppedPkts_Type=Counter32
_CAal5VccInDroppedPkts_Object=MibTableColumn
cAal5VccInDroppedPkts=_CAal5VccInDroppedPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,1),_CAal5VccInDroppedPkts_Type())
cAal5VccInDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInDroppedPkts.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccInDroppedPkts.setUnits(_E)
_CAal5VccOutDroppedPkts_Type=Counter32
_CAal5VccOutDroppedPkts_Object=MibTableColumn
cAal5VccOutDroppedPkts=_CAal5VccOutDroppedPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,2),_CAal5VccOutDroppedPkts_Type())
cAal5VccOutDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutDroppedPkts.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccOutDroppedPkts.setUnits(_E)
_CAal5VccInDroppedOctets_Type=Counter32
_CAal5VccInDroppedOctets_Object=MibTableColumn
cAal5VccInDroppedOctets=_CAal5VccInDroppedOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,3),_CAal5VccInDroppedOctets_Type())
cAal5VccInDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInDroppedOctets.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccInDroppedOctets.setUnits(_F)
_CAal5VccOutDroppedOctets_Type=Counter32
_CAal5VccOutDroppedOctets_Object=MibTableColumn
cAal5VccOutDroppedOctets=_CAal5VccOutDroppedOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,4),_CAal5VccOutDroppedOctets_Type())
cAal5VccOutDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutDroppedOctets.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccOutDroppedOctets.setUnits(_F)
_CAal5VccInCells_Type=Counter32
_CAal5VccInCells_Object=MibTableColumn
cAal5VccInCells=_CAal5VccInCells_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,5),_CAal5VccInCells_Type())
cAal5VccInCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInCells.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccInCells.setUnits(_D)
_CAal5VccOutCells_Type=Counter32
_CAal5VccOutCells_Object=MibTableColumn
cAal5VccOutCells=_CAal5VccOutCells_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,6),_CAal5VccOutCells_Type())
cAal5VccOutCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutCells.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccOutCells.setUnits(_D)
_CAal5VccInDroppedCells_Type=Counter32
_CAal5VccInDroppedCells_Object=MibTableColumn
cAal5VccInDroppedCells=_CAal5VccInDroppedCells_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,7),_CAal5VccInDroppedCells_Type())
cAal5VccInDroppedCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInDroppedCells.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccInDroppedCells.setUnits(_D)
_CAal5VccOutDroppedCells_Type=Counter32
_CAal5VccOutDroppedCells_Object=MibTableColumn
cAal5VccOutDroppedCells=_CAal5VccOutDroppedCells_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,8),_CAal5VccOutDroppedCells_Type())
cAal5VccOutDroppedCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutDroppedCells.setStatus(_A)
if mibBuilder.loadTexts:cAal5VccOutDroppedCells.setUnits(_D)
_CiscoAAL5ExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAAL5ExtMIBConformance=_CiscoAAL5ExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2))
_CiscoAAL5ExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAAL5ExtMIBCompliances=_CiscoAAL5ExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,1))
_CiscoAAL5ExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAAL5ExtMIBGroups=_CiscoAAL5ExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,2))
aal5VccEntry.registerAugmentions((_B,_G))
cAal5ExtVccEntry.setIndexNames(*aal5VccEntry.getIndexNames())
ciscoAal5ExtMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,1))
ciscoAal5ExtMIBGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoAal5ExtMIBGroup.setStatus(_A)
ciscoAAL5ExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,9999,2,1,1))
ciscoAAL5ExtMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:ciscoAAL5ExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAal5ExtMIB':ciscoAal5ExtMIB,'ciscoAal5ExtMIBObjects':ciscoAal5ExtMIBObjects,'cAal5ExtConnections':cAal5ExtConnections,'cAal5ExtVccTable':cAal5ExtVccTable,_G:cAal5ExtVccEntry,_H:cAal5VccInDroppedPkts,_I:cAal5VccOutDroppedPkts,_J:cAal5VccInDroppedOctets,_K:cAal5VccOutDroppedOctets,_L:cAal5VccInCells,_M:cAal5VccOutCells,_N:cAal5VccInDroppedCells,_O:cAal5VccOutDroppedCells,'ciscoAAL5ExtMIBConformance':ciscoAAL5ExtMIBConformance,'ciscoAAL5ExtMIBCompliances':ciscoAAL5ExtMIBCompliances,'ciscoAAL5ExtMIBCompliance':ciscoAAL5ExtMIBCompliance,'ciscoAAL5ExtMIBGroups':ciscoAAL5ExtMIBGroups,_P:ciscoAal5ExtMIBGroup})