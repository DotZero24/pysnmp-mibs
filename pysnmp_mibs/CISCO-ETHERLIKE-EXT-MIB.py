_P='ciscoEtherExtSubIfGroup'
_O='ceeSubInterfaceCount'
_N='ceeDot3PauseExtOperMode'
_M='ceeDot3PauseExtAdminMode'
_L='read-only'
_K='rxDesired'
_J='txDesired'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='dot3StatsIndex'
_E='EtherLike-MIB'
_D='ciscoEtherExtPauseGroup'
_C='Bits'
_B='CISCO-ETHERLIKE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
dot3StatsIndex,=mibBuilder.importSymbols(_E,_F)
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_C,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoEtherExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,645))
if mibBuilder.loadTexts:ciscoEtherExtMIB.setRevisions(('2010-06-04 00:00','2008-10-15 00:00','2008-01-09 00:00'))
_CiscoEtherExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEtherExtMIBNotifs=_CiscoEtherExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,645,0))
_CiscoEtherExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEtherExtMIBObjects=_CiscoEtherExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,645,1))
_CeeDot3PauseExt_ObjectIdentity=ObjectIdentity
ceeDot3PauseExt=_CeeDot3PauseExt_ObjectIdentity((1,3,6,1,4,1,9,9,645,1,1))
_CeeDot3PauseExtTable_Object=MibTable
ceeDot3PauseExtTable=_CeeDot3PauseExtTable_Object((1,3,6,1,4,1,9,9,645,1,1,1))
if mibBuilder.loadTexts:ceeDot3PauseExtTable.setStatus(_A)
_CeeDot3PauseExtEntry_Object=MibTableRow
ceeDot3PauseExtEntry=_CeeDot3PauseExtEntry_Object((1,3,6,1,4,1,9,9,645,1,1,1,1))
ceeDot3PauseExtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ceeDot3PauseExtEntry.setStatus(_A)
class _CeeDot3PauseExtAdminMode_Type(Bits):namedValues=NamedValues(*((_J,0),(_K,1)))
_CeeDot3PauseExtAdminMode_Type.__name__=_C
_CeeDot3PauseExtAdminMode_Object=MibTableColumn
ceeDot3PauseExtAdminMode=_CeeDot3PauseExtAdminMode_Object((1,3,6,1,4,1,9,9,645,1,1,1,1,1),_CeeDot3PauseExtAdminMode_Type())
ceeDot3PauseExtAdminMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:ceeDot3PauseExtAdminMode.setStatus(_A)
class _CeeDot3PauseExtOperMode_Type(Bits):namedValues=NamedValues(*(('txDisagree',0),('rxDisagree',1),(_J,2),(_K,3)))
_CeeDot3PauseExtOperMode_Type.__name__=_C
_CeeDot3PauseExtOperMode_Object=MibTableColumn
ceeDot3PauseExtOperMode=_CeeDot3PauseExtOperMode_Object((1,3,6,1,4,1,9,9,645,1,1,1,1,2),_CeeDot3PauseExtOperMode_Type())
ceeDot3PauseExtOperMode.setMaxAccess(_L)
if mibBuilder.loadTexts:ceeDot3PauseExtOperMode.setStatus(_A)
_CeeSubIf_ObjectIdentity=ObjectIdentity
ceeSubIf=_CeeSubIf_ObjectIdentity((1,3,6,1,4,1,9,9,645,1,2))
_CeeSubInterfaceTable_Object=MibTable
ceeSubInterfaceTable=_CeeSubInterfaceTable_Object((1,3,6,1,4,1,9,9,645,1,2,1))
if mibBuilder.loadTexts:ceeSubInterfaceTable.setStatus(_A)
_CeeSubInterfaceEntry_Object=MibTableRow
ceeSubInterfaceEntry=_CeeSubInterfaceEntry_Object((1,3,6,1,4,1,9,9,645,1,2,1,1))
ceeSubInterfaceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ceeSubInterfaceEntry.setStatus(_A)
class _CeeSubInterfaceCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CeeSubInterfaceCount_Type.__name__=_I
_CeeSubInterfaceCount_Object=MibTableColumn
ceeSubInterfaceCount=_CeeSubInterfaceCount_Object((1,3,6,1,4,1,9,9,645,1,2,1,1,1),_CeeSubInterfaceCount_Type())
ceeSubInterfaceCount.setMaxAccess(_L)
if mibBuilder.loadTexts:ceeSubInterfaceCount.setStatus(_A)
if mibBuilder.loadTexts:ceeSubInterfaceCount.setUnits('subifs')
_CiscoEtherExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoEtherExtMIBConform=_CiscoEtherExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,645,2))
_CeeEtherExtMIBCompliances_ObjectIdentity=ObjectIdentity
ceeEtherExtMIBCompliances=_CeeEtherExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,645,2,1))
_CeeEtherExtMIBGroups_ObjectIdentity=ObjectIdentity
ceeEtherExtMIBGroups=_CeeEtherExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,645,2,2))
ciscoEtherExtPauseGroup=ObjectGroup((1,3,6,1,4,1,9,9,645,2,2,1))
ciscoEtherExtPauseGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoEtherExtPauseGroup.setStatus(_A)
ciscoEtherExtSubIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,645,2,2,2))
ciscoEtherExtSubIfGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoEtherExtSubIfGroup.setStatus(_A)
ceeEtherExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,645,2,1,1))
ceeEtherExtMIBCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:ceeEtherExtMIBCompliance.setStatus('deprecated')
ceeEtherExtMIBComplianceR01=ModuleCompliance((1,3,6,1,4,1,9,9,645,2,1,2))
ceeEtherExtMIBComplianceR01.setObjects(*((_B,_D),(_B,_P)))
if mibBuilder.loadTexts:ceeEtherExtMIBComplianceR01.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoEtherExtMIB':ciscoEtherExtMIB,'ciscoEtherExtMIBNotifs':ciscoEtherExtMIBNotifs,'ciscoEtherExtMIBObjects':ciscoEtherExtMIBObjects,'ceeDot3PauseExt':ceeDot3PauseExt,'ceeDot3PauseExtTable':ceeDot3PauseExtTable,'ceeDot3PauseExtEntry':ceeDot3PauseExtEntry,_M:ceeDot3PauseExtAdminMode,_N:ceeDot3PauseExtOperMode,'ceeSubIf':ceeSubIf,'ceeSubInterfaceTable':ceeSubInterfaceTable,'ceeSubInterfaceEntry':ceeSubInterfaceEntry,_O:ceeSubInterfaceCount,'ciscoEtherExtMIBConform':ciscoEtherExtMIBConform,'ceeEtherExtMIBCompliances':ceeEtherExtMIBCompliances,'ceeEtherExtMIBCompliance':ceeEtherExtMIBCompliance,'ceeEtherExtMIBComplianceR01':ceeEtherExtMIBComplianceR01,'ceeEtherExtMIBGroups':ceeEtherExtMIBGroups,_D:ciscoEtherExtPauseGroup,_P:ciscoEtherExtSubIfGroup})