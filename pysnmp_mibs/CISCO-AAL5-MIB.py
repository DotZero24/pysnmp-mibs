_V='ciscoAal5MIBHCGroup'
_U='deprecated'
_T='cAal5VccHCOutOctets'
_S='cAal5VccHCInOctets'
_R='cAal5VccHCOutPkts'
_Q='cAal5VccHCInPkts'
_P='cAal5VccOutDroppedOctets'
_O='cAal5VccInDroppedOctets'
_N='cAal5VccOutDroppedPkts'
_M='cAal5VccInDroppedPkts'
_L='cAal5VccOutOctets'
_K='cAal5VccInOctets'
_J='cAal5VccOutPkts'
_I='cAal5VccInPkts'
_H='cAal5VccEntry'
_G='ciscoAal5VcStatsExtMIBGroup'
_F='ciscoAal5MIBGroup'
_E='octets'
_D='packets'
_C='read-only'
_B='current'
_A='CISCO-AAL5-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aal5VccEntry,=mibBuilder.importSymbols('ATM-MIB','aal5VccEntry')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAal5MIB=ModuleIdentity((1,3,6,1,4,1,9,9,66))
if mibBuilder.loadTexts:ciscoAal5MIB.setRevisions(('2003-09-22 00:00','2002-10-17 00:00','1996-11-15 00:00'))
_CiscoAal5MIBObjects_ObjectIdentity=ObjectIdentity
ciscoAal5MIBObjects=_CiscoAal5MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,66,1))
_CAal5Connections_ObjectIdentity=ObjectIdentity
cAal5Connections=_CAal5Connections_ObjectIdentity((1,3,6,1,4,1,9,9,66,1,1))
_CAal5VccTable_Object=MibTable
cAal5VccTable=_CAal5VccTable_Object((1,3,6,1,4,1,9,9,66,1,1,1))
if mibBuilder.loadTexts:cAal5VccTable.setStatus(_B)
_CAal5VccEntry_Object=MibTableRow
cAal5VccEntry=_CAal5VccEntry_Object((1,3,6,1,4,1,9,9,66,1,1,1,1))
if mibBuilder.loadTexts:cAal5VccEntry.setStatus(_B)
_CAal5VccInPkts_Type=Counter32
_CAal5VccInPkts_Object=MibTableColumn
cAal5VccInPkts=_CAal5VccInPkts_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,1),_CAal5VccInPkts_Type())
cAal5VccInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInPkts.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccInPkts.setUnits(_D)
_CAal5VccOutPkts_Type=Counter32
_CAal5VccOutPkts_Object=MibTableColumn
cAal5VccOutPkts=_CAal5VccOutPkts_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,2),_CAal5VccOutPkts_Type())
cAal5VccOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutPkts.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccOutPkts.setUnits(_D)
_CAal5VccInOctets_Type=Counter32
_CAal5VccInOctets_Object=MibTableColumn
cAal5VccInOctets=_CAal5VccInOctets_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,3),_CAal5VccInOctets_Type())
cAal5VccInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInOctets.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccInOctets.setUnits(_E)
_CAal5VccOutOctets_Type=Counter32
_CAal5VccOutOctets_Object=MibTableColumn
cAal5VccOutOctets=_CAal5VccOutOctets_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,4),_CAal5VccOutOctets_Type())
cAal5VccOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutOctets.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccOutOctets.setUnits(_E)
_CAal5VccInDroppedPkts_Type=Counter32
_CAal5VccInDroppedPkts_Object=MibTableColumn
cAal5VccInDroppedPkts=_CAal5VccInDroppedPkts_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,5),_CAal5VccInDroppedPkts_Type())
cAal5VccInDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInDroppedPkts.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccInDroppedPkts.setUnits(_D)
_CAal5VccOutDroppedPkts_Type=Counter32
_CAal5VccOutDroppedPkts_Object=MibTableColumn
cAal5VccOutDroppedPkts=_CAal5VccOutDroppedPkts_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,6),_CAal5VccOutDroppedPkts_Type())
cAal5VccOutDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutDroppedPkts.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccOutDroppedPkts.setUnits(_D)
_CAal5VccInDroppedOctets_Type=Counter32
_CAal5VccInDroppedOctets_Object=MibTableColumn
cAal5VccInDroppedOctets=_CAal5VccInDroppedOctets_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,7),_CAal5VccInDroppedOctets_Type())
cAal5VccInDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccInDroppedOctets.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccInDroppedOctets.setUnits(_E)
_CAal5VccOutDroppedOctets_Type=Counter32
_CAal5VccOutDroppedOctets_Object=MibTableColumn
cAal5VccOutDroppedOctets=_CAal5VccOutDroppedOctets_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,8),_CAal5VccOutDroppedOctets_Type())
cAal5VccOutDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccOutDroppedOctets.setStatus(_B)
if mibBuilder.loadTexts:cAal5VccOutDroppedOctets.setUnits(_E)
_CAal5VccHCInPkts_Type=Counter64
_CAal5VccHCInPkts_Object=MibTableColumn
cAal5VccHCInPkts=_CAal5VccHCInPkts_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,9),_CAal5VccHCInPkts_Type())
cAal5VccHCInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccHCInPkts.setStatus(_B)
_CAal5VccHCOutPkts_Type=Counter64
_CAal5VccHCOutPkts_Object=MibTableColumn
cAal5VccHCOutPkts=_CAal5VccHCOutPkts_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,10),_CAal5VccHCOutPkts_Type())
cAal5VccHCOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccHCOutPkts.setStatus(_B)
_CAal5VccHCInOctets_Type=Counter64
_CAal5VccHCInOctets_Object=MibTableColumn
cAal5VccHCInOctets=_CAal5VccHCInOctets_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,11),_CAal5VccHCInOctets_Type())
cAal5VccHCInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccHCInOctets.setStatus(_B)
_CAal5VccHCOutOctets_Type=Counter64
_CAal5VccHCOutOctets_Object=MibTableColumn
cAal5VccHCOutOctets=_CAal5VccHCOutOctets_Object((1,3,6,1,4,1,9,9,66,1,1,1,1,12),_CAal5VccHCOutOctets_Type())
cAal5VccHCOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccHCOutOctets.setStatus(_B)
_CiscoAal5MIBConformance_ObjectIdentity=ObjectIdentity
ciscoAal5MIBConformance=_CiscoAal5MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,66,3))
_CiscoAal5MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAal5MIBCompliances=_CiscoAal5MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,66,3,1))
_CiscoAal5MIBGroups_ObjectIdentity=ObjectIdentity
ciscoAal5MIBGroups=_CiscoAal5MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,66,3,2))
aal5VccEntry.registerAugmentions((_A,_H))
cAal5VccEntry.setIndexNames(*aal5VccEntry.getIndexNames())
ciscoAal5MIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,66,3,2,1))
ciscoAal5MIBGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoAal5MIBGroup.setStatus(_B)
ciscoAal5VcStatsExtMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,66,3,2,2))
ciscoAal5VcStatsExtMIBGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoAal5VcStatsExtMIBGroup.setStatus(_B)
ciscoAal5MIBHCGroup=ObjectGroup((1,3,6,1,4,1,9,9,66,3,2,3))
ciscoAal5MIBHCGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoAal5MIBHCGroup.setStatus(_B)
ciscoAal5MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,66,3,1,1))
ciscoAal5MIBCompliance.setObjects((_A,_F))
if mibBuilder.loadTexts:ciscoAal5MIBCompliance.setStatus(_U)
ciscoAal5MIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,66,3,1,2))
ciscoAal5MIBComplianceRev1.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ciscoAal5MIBComplianceRev1.setStatus(_U)
ciscoAal5MIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,66,3,1,3))
ciscoAal5MIBComplianceRev2.setObjects(*((_A,_F),(_A,_G),(_A,_V)))
if mibBuilder.loadTexts:ciscoAal5MIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoAal5MIB':ciscoAal5MIB,'ciscoAal5MIBObjects':ciscoAal5MIBObjects,'cAal5Connections':cAal5Connections,'cAal5VccTable':cAal5VccTable,_H:cAal5VccEntry,_I:cAal5VccInPkts,_J:cAal5VccOutPkts,_K:cAal5VccInOctets,_L:cAal5VccOutOctets,_M:cAal5VccInDroppedPkts,_N:cAal5VccOutDroppedPkts,_O:cAal5VccInDroppedOctets,_P:cAal5VccOutDroppedOctets,_Q:cAal5VccHCInPkts,_R:cAal5VccHCOutPkts,_S:cAal5VccHCInOctets,_T:cAal5VccHCOutOctets,'ciscoAal5MIBConformance':ciscoAal5MIBConformance,'ciscoAal5MIBCompliances':ciscoAal5MIBCompliances,'ciscoAal5MIBCompliance':ciscoAal5MIBCompliance,'ciscoAal5MIBComplianceRev1':ciscoAal5MIBComplianceRev1,'ciscoAal5MIBComplianceRev2':ciscoAal5MIBComplianceRev2,'ciscoAal5MIBGroups':ciscoAal5MIBGroups,_F:ciscoAal5MIBGroup,_G:ciscoAal5VcStatsExtMIBGroup,_V:ciscoAal5MIBHCGroup})