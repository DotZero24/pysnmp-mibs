_X='ciscoHmcMIBOperModeGroup'
_W='chmcOperModePortGrpIfIndexList'
_V='chmcOperModePortGrpOperMode'
_U='chmcOversubPortGrpClearBlkStatus'
_T='chmcOversubPortGrpOversubStatus'
_S='chmcOversubPortGrpIfIndexList'
_R='chmcOversubModOversubStatus'
_Q='chmcOversubModuleCapabilities'
_P='chmcOperModePortGrpIndex'
_O='disabled'
_N='enabled'
_M='not-accessible'
_L='chmcOversubPortGrpIndex'
_K='ciscoHmcMIBOversubPgClearBlkGrp'
_J='ciscoHmcMIBOversubBaseGroup'
_I='other'
_H='read-only'
_G='Unsigned32'
_F='read-write'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='Integer32'
_B='CISCO-HW-MODULE-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoInterfaceIndexList,=mibBuilder.importSymbols('CISCO-TC','CiscoInterfaceIndexList')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoHwModuleControlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,714))
if mibBuilder.loadTexts:ciscoHwModuleControlMIB.setRevisions(('2010-08-09 00:00','2009-11-12 00:00'))
_CiscoHwModuleControlMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoHwModuleControlMIBNotifs=_CiscoHwModuleControlMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,714,0))
_CiscoHwModuleControlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoHwModuleControlMIBObjects=_CiscoHwModuleControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,714,1))
_ChmcOversubscription_ObjectIdentity=ObjectIdentity
chmcOversubscription=_ChmcOversubscription_ObjectIdentity((1,3,6,1,4,1,9,9,714,1,1))
_ChmcOversubModuleTable_Object=MibTable
chmcOversubModuleTable=_ChmcOversubModuleTable_Object((1,3,6,1,4,1,9,9,714,1,1,1))
if mibBuilder.loadTexts:chmcOversubModuleTable.setStatus(_A)
_ChmcOversubModuleEntry_Object=MibTableRow
chmcOversubModuleEntry=_ChmcOversubModuleEntry_Object((1,3,6,1,4,1,9,9,714,1,1,1,1))
chmcOversubModuleEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:chmcOversubModuleEntry.setStatus(_A)
class _ChmcOversubModuleCapabilities_Type(Bits):namedValues=NamedValues(*(('oversubConfigModuleLevel',0),('oversubConfigPortGroupLevel',1),('clearblockConfigPortGroupLevel',2)))
_ChmcOversubModuleCapabilities_Type.__name__='Bits'
_ChmcOversubModuleCapabilities_Object=MibTableColumn
chmcOversubModuleCapabilities=_ChmcOversubModuleCapabilities_Object((1,3,6,1,4,1,9,9,714,1,1,1,1,1),_ChmcOversubModuleCapabilities_Type())
chmcOversubModuleCapabilities.setMaxAccess(_H)
if mibBuilder.loadTexts:chmcOversubModuleCapabilities.setStatus(_A)
class _ChmcOversubModOversubStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabledOnAllPortGroups',1),('disabledOnAllPortGroups',2),('portGroupSpecific',3)))
_ChmcOversubModOversubStatus_Type.__name__=_C
_ChmcOversubModOversubStatus_Object=MibTableColumn
chmcOversubModOversubStatus=_ChmcOversubModOversubStatus_Object((1,3,6,1,4,1,9,9,714,1,1,1,1,2),_ChmcOversubModOversubStatus_Type())
chmcOversubModOversubStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:chmcOversubModOversubStatus.setStatus(_A)
_ChmcOversubPortGroupTable_Object=MibTable
chmcOversubPortGroupTable=_ChmcOversubPortGroupTable_Object((1,3,6,1,4,1,9,9,714,1,1,2))
if mibBuilder.loadTexts:chmcOversubPortGroupTable.setStatus(_A)
_ChmcOversubPortGroupEntry_Object=MibTableRow
chmcOversubPortGroupEntry=_ChmcOversubPortGroupEntry_Object((1,3,6,1,4,1,9,9,714,1,1,2,1))
chmcOversubPortGroupEntry.setIndexNames((0,_D,_E),(0,_B,_L))
if mibBuilder.loadTexts:chmcOversubPortGroupEntry.setStatus(_A)
class _ChmcOversubPortGrpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ChmcOversubPortGrpIndex_Type.__name__=_G
_ChmcOversubPortGrpIndex_Object=MibTableColumn
chmcOversubPortGrpIndex=_ChmcOversubPortGrpIndex_Object((1,3,6,1,4,1,9,9,714,1,1,2,1,1),_ChmcOversubPortGrpIndex_Type())
chmcOversubPortGrpIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:chmcOversubPortGrpIndex.setStatus(_A)
_ChmcOversubPortGrpIfIndexList_Type=CiscoInterfaceIndexList
_ChmcOversubPortGrpIfIndexList_Object=MibTableColumn
chmcOversubPortGrpIfIndexList=_ChmcOversubPortGrpIfIndexList_Object((1,3,6,1,4,1,9,9,714,1,1,2,1,2),_ChmcOversubPortGrpIfIndexList_Type())
chmcOversubPortGrpIfIndexList.setMaxAccess(_H)
if mibBuilder.loadTexts:chmcOversubPortGrpIfIndexList.setStatus(_A)
class _ChmcOversubPortGrpOversubStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_N,2),(_O,3)))
_ChmcOversubPortGrpOversubStatus_Type.__name__=_C
_ChmcOversubPortGrpOversubStatus_Object=MibTableColumn
chmcOversubPortGrpOversubStatus=_ChmcOversubPortGrpOversubStatus_Object((1,3,6,1,4,1,9,9,714,1,1,2,1,3),_ChmcOversubPortGrpOversubStatus_Type())
chmcOversubPortGrpOversubStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:chmcOversubPortGrpOversubStatus.setStatus(_A)
class _ChmcOversubPortGrpClearBlkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_N,2),(_O,3)))
_ChmcOversubPortGrpClearBlkStatus_Type.__name__=_C
_ChmcOversubPortGrpClearBlkStatus_Object=MibTableColumn
chmcOversubPortGrpClearBlkStatus=_ChmcOversubPortGrpClearBlkStatus_Object((1,3,6,1,4,1,9,9,714,1,1,2,1,4),_ChmcOversubPortGrpClearBlkStatus_Type())
chmcOversubPortGrpClearBlkStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:chmcOversubPortGrpClearBlkStatus.setStatus(_A)
_ChmcOperationalMode_ObjectIdentity=ObjectIdentity
chmcOperationalMode=_ChmcOperationalMode_ObjectIdentity((1,3,6,1,4,1,9,9,714,1,2))
_ChmcOperModePortGroupTable_Object=MibTable
chmcOperModePortGroupTable=_ChmcOperModePortGroupTable_Object((1,3,6,1,4,1,9,9,714,1,2,1))
if mibBuilder.loadTexts:chmcOperModePortGroupTable.setStatus(_A)
_ChmcOperModePortGroupEntry_Object=MibTableRow
chmcOperModePortGroupEntry=_ChmcOperModePortGroupEntry_Object((1,3,6,1,4,1,9,9,714,1,2,1,1))
chmcOperModePortGroupEntry.setIndexNames((0,_D,_E),(0,_B,_P))
if mibBuilder.loadTexts:chmcOperModePortGroupEntry.setStatus(_A)
class _ChmcOperModePortGrpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ChmcOperModePortGrpIndex_Type.__name__=_G
_ChmcOperModePortGrpIndex_Object=MibTableColumn
chmcOperModePortGrpIndex=_ChmcOperModePortGrpIndex_Object((1,3,6,1,4,1,9,9,714,1,2,1,1,1),_ChmcOperModePortGrpIndex_Type())
chmcOperModePortGrpIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:chmcOperModePortGrpIndex.setStatus(_A)
class _ChmcOperModePortGrpOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('tenGigabitEthernet',2),('fortyGigabitEthernet',3)))
_ChmcOperModePortGrpOperMode_Type.__name__=_C
_ChmcOperModePortGrpOperMode_Object=MibTableColumn
chmcOperModePortGrpOperMode=_ChmcOperModePortGrpOperMode_Object((1,3,6,1,4,1,9,9,714,1,2,1,1,2),_ChmcOperModePortGrpOperMode_Type())
chmcOperModePortGrpOperMode.setMaxAccess(_F)
if mibBuilder.loadTexts:chmcOperModePortGrpOperMode.setStatus(_A)
_ChmcOperModePortGrpIfIndexList_Type=CiscoInterfaceIndexList
_ChmcOperModePortGrpIfIndexList_Object=MibTableColumn
chmcOperModePortGrpIfIndexList=_ChmcOperModePortGrpIfIndexList_Object((1,3,6,1,4,1,9,9,714,1,2,1,1,3),_ChmcOperModePortGrpIfIndexList_Type())
chmcOperModePortGrpIfIndexList.setMaxAccess(_H)
if mibBuilder.loadTexts:chmcOperModePortGrpIfIndexList.setStatus(_A)
_CiscoHwModuleControlMIBConform_ObjectIdentity=ObjectIdentity
ciscoHwModuleControlMIBConform=_CiscoHwModuleControlMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,714,2))
_ChmcHwModuleControlMIBCompliances_ObjectIdentity=ObjectIdentity
chmcHwModuleControlMIBCompliances=_ChmcHwModuleControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,714,2,1))
_ChmcHwModuleControlMIBGroups_ObjectIdentity=ObjectIdentity
chmcHwModuleControlMIBGroups=_ChmcHwModuleControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,714,2,2))
ciscoHmcMIBOversubBaseGroup=ObjectGroup((1,3,6,1,4,1,9,9,714,2,2,1))
ciscoHmcMIBOversubBaseGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoHmcMIBOversubBaseGroup.setStatus(_A)
ciscoHmcMIBOversubPgClearBlkGrp=ObjectGroup((1,3,6,1,4,1,9,9,714,2,2,2))
ciscoHmcMIBOversubPgClearBlkGrp.setObjects((_B,_U))
if mibBuilder.loadTexts:ciscoHmcMIBOversubPgClearBlkGrp.setStatus(_A)
ciscoHmcMIBOperModeGroup=ObjectGroup((1,3,6,1,4,1,9,9,714,2,2,3))
ciscoHmcMIBOperModeGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoHmcMIBOperModeGroup.setStatus(_A)
chmcHwModuleControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,714,2,1,1))
chmcHwModuleControlMIBCompliance.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:chmcHwModuleControlMIBCompliance.setStatus('deprecated')
chmcHwModuleControlMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,714,2,1,2))
chmcHwModuleControlMIBCompliance1.setObjects(*((_B,_J),(_B,_K),(_B,_X)))
if mibBuilder.loadTexts:chmcHwModuleControlMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoHwModuleControlMIB':ciscoHwModuleControlMIB,'ciscoHwModuleControlMIBNotifs':ciscoHwModuleControlMIBNotifs,'ciscoHwModuleControlMIBObjects':ciscoHwModuleControlMIBObjects,'chmcOversubscription':chmcOversubscription,'chmcOversubModuleTable':chmcOversubModuleTable,'chmcOversubModuleEntry':chmcOversubModuleEntry,_Q:chmcOversubModuleCapabilities,_R:chmcOversubModOversubStatus,'chmcOversubPortGroupTable':chmcOversubPortGroupTable,'chmcOversubPortGroupEntry':chmcOversubPortGroupEntry,_L:chmcOversubPortGrpIndex,_S:chmcOversubPortGrpIfIndexList,_T:chmcOversubPortGrpOversubStatus,_U:chmcOversubPortGrpClearBlkStatus,'chmcOperationalMode':chmcOperationalMode,'chmcOperModePortGroupTable':chmcOperModePortGroupTable,'chmcOperModePortGroupEntry':chmcOperModePortGroupEntry,_P:chmcOperModePortGrpIndex,_V:chmcOperModePortGrpOperMode,_W:chmcOperModePortGrpIfIndexList,'ciscoHwModuleControlMIBConform':ciscoHwModuleControlMIBConform,'chmcHwModuleControlMIBCompliances':chmcHwModuleControlMIBCompliances,'chmcHwModuleControlMIBCompliance':chmcHwModuleControlMIBCompliance,'chmcHwModuleControlMIBCompliance1':chmcHwModuleControlMIBCompliance1,'chmcHwModuleControlMIBGroups':chmcHwModuleControlMIBGroups,_J:ciscoHmcMIBOversubBaseGroup,_K:ciscoHmcMIBOversubPgClearBlkGrp,_X:ciscoHmcMIBOperModeGroup})