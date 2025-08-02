_b='ciscoRptrMIBGlobalsGroup'
_a='ciscoRptrMIBPortGroupV11R01'
_Z='ciscoRptrMIBGroup'
_Y='ciscoRptrTrapAlgorithm'
_X='ciscoRptrPortIllegalAddrTotalCount'
_W='ciscoRptrPortLastIllegalAddrCount'
_V='ciscoRptrPortIllegalAddrLastHeard'
_U='ciscoRptrPortIllegalAddrFirstHeard'
_T='ciscoRptrPortIllegalAddrTrapEnabled'
_S='ciscoRptrPortIllegalAddrTrapAcked'
_R='obsolete'
_Q='ciscoRptrPortEntry'
_P='ciscoRptrPortAllowedSrcAddrStatus'
_O='ciscoRptrPortAllowedSrcAddr'
_N='ciscoRptrPortSrcAddrCtrl'
_M='ciscoRptrPortAutoPolarityCorrected'
_L='ciscoRptrPortAutoPolarityEnabled'
_K='ciscoRptrPortLinkTestFailed'
_J='ciscoRptrPortLinkTestEnabled'
_I='ciscoRptrPortMDIStatus'
_H='OctetString'
_G='ciscoRptrPortLastIllegalSrcAddr'
_F='TruthValue'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-REPEATER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
rptrPortEntry,=mibBuilder.importSymbols('SNMP-REPEATER-MIB','rptrPortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_F)
ciscoRptrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,22))
if mibBuilder.loadTexts:ciscoRptrMIB.setRevisions(('1995-12-05 00:00','1995-10-17 00:00','1995-03-09 00:00','1994-10-26 00:00'))
_CiscoRptrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRptrMIBObjects=_CiscoRptrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,22,1))
_CiscoRptrPortTable_Object=MibTable
ciscoRptrPortTable=_CiscoRptrPortTable_Object((1,3,6,1,4,1,9,9,22,1,1))
if mibBuilder.loadTexts:ciscoRptrPortTable.setStatus(_B)
_CiscoRptrPortEntry_Object=MibTableRow
ciscoRptrPortEntry=_CiscoRptrPortEntry_Object((1,3,6,1,4,1,9,9,22,1,1,1))
if mibBuilder.loadTexts:ciscoRptrPortEntry.setStatus(_B)
class _CiscoRptrPortMDIStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('crossover',2),('notSwitchable',3)))
_CiscoRptrPortMDIStatus_Type.__name__=_E
_CiscoRptrPortMDIStatus_Object=MibTableColumn
ciscoRptrPortMDIStatus=_CiscoRptrPortMDIStatus_Object((1,3,6,1,4,1,9,9,22,1,1,1,1),_CiscoRptrPortMDIStatus_Type())
ciscoRptrPortMDIStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortMDIStatus.setStatus(_B)
class _CiscoRptrPortLinkTestEnabled_Type(TruthValue):defaultValue=1
_CiscoRptrPortLinkTestEnabled_Type.__name__=_F
_CiscoRptrPortLinkTestEnabled_Object=MibTableColumn
ciscoRptrPortLinkTestEnabled=_CiscoRptrPortLinkTestEnabled_Object((1,3,6,1,4,1,9,9,22,1,1,1,2),_CiscoRptrPortLinkTestEnabled_Type())
ciscoRptrPortLinkTestEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoRptrPortLinkTestEnabled.setStatus(_B)
_CiscoRptrPortLinkTestFailed_Type=TruthValue
_CiscoRptrPortLinkTestFailed_Object=MibTableColumn
ciscoRptrPortLinkTestFailed=_CiscoRptrPortLinkTestFailed_Object((1,3,6,1,4,1,9,9,22,1,1,1,3),_CiscoRptrPortLinkTestFailed_Type())
ciscoRptrPortLinkTestFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortLinkTestFailed.setStatus(_B)
class _CiscoRptrPortAutoPolarityEnabled_Type(TruthValue):defaultValue=1
_CiscoRptrPortAutoPolarityEnabled_Type.__name__=_F
_CiscoRptrPortAutoPolarityEnabled_Object=MibTableColumn
ciscoRptrPortAutoPolarityEnabled=_CiscoRptrPortAutoPolarityEnabled_Object((1,3,6,1,4,1,9,9,22,1,1,1,4),_CiscoRptrPortAutoPolarityEnabled_Type())
ciscoRptrPortAutoPolarityEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoRptrPortAutoPolarityEnabled.setStatus(_B)
_CiscoRptrPortAutoPolarityCorrected_Type=TruthValue
_CiscoRptrPortAutoPolarityCorrected_Object=MibTableColumn
ciscoRptrPortAutoPolarityCorrected=_CiscoRptrPortAutoPolarityCorrected_Object((1,3,6,1,4,1,9,9,22,1,1,1,5),_CiscoRptrPortAutoPolarityCorrected_Type())
ciscoRptrPortAutoPolarityCorrected.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortAutoPolarityCorrected.setStatus(_B)
class _CiscoRptrPortSrcAddrCtrl_Type(TruthValue):defaultValue=2
_CiscoRptrPortSrcAddrCtrl_Type.__name__=_F
_CiscoRptrPortSrcAddrCtrl_Object=MibTableColumn
ciscoRptrPortSrcAddrCtrl=_CiscoRptrPortSrcAddrCtrl_Object((1,3,6,1,4,1,9,9,22,1,1,1,6),_CiscoRptrPortSrcAddrCtrl_Type())
ciscoRptrPortSrcAddrCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoRptrPortSrcAddrCtrl.setStatus(_B)
class _CiscoRptrPortAllowedSrcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_CiscoRptrPortAllowedSrcAddr_Type.__name__=_H
_CiscoRptrPortAllowedSrcAddr_Object=MibTableColumn
ciscoRptrPortAllowedSrcAddr=_CiscoRptrPortAllowedSrcAddr_Object((1,3,6,1,4,1,9,9,22,1,1,1,7),_CiscoRptrPortAllowedSrcAddr_Type())
ciscoRptrPortAllowedSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoRptrPortAllowedSrcAddr.setStatus(_B)
class _CiscoRptrPortAllowedSrcAddrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allowedSrcAddrConfig',1),('allowedSrcAddrLearn',2),('allowedSrcAddrUndefined',3)))
_CiscoRptrPortAllowedSrcAddrStatus_Type.__name__=_E
_CiscoRptrPortAllowedSrcAddrStatus_Object=MibTableColumn
ciscoRptrPortAllowedSrcAddrStatus=_CiscoRptrPortAllowedSrcAddrStatus_Object((1,3,6,1,4,1,9,9,22,1,1,1,8),_CiscoRptrPortAllowedSrcAddrStatus_Type())
ciscoRptrPortAllowedSrcAddrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortAllowedSrcAddrStatus.setStatus(_B)
class _CiscoRptrPortLastIllegalSrcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_CiscoRptrPortLastIllegalSrcAddr_Type.__name__=_H
_CiscoRptrPortLastIllegalSrcAddr_Object=MibTableColumn
ciscoRptrPortLastIllegalSrcAddr=_CiscoRptrPortLastIllegalSrcAddr_Object((1,3,6,1,4,1,9,9,22,1,1,1,9),_CiscoRptrPortLastIllegalSrcAddr_Type())
ciscoRptrPortLastIllegalSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortLastIllegalSrcAddr.setStatus(_B)
class _CiscoRptrPortIllegalAddrTrapAcked_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acked',1),('no-acked-sending',2),('no-acked-no-sending',3)))
_CiscoRptrPortIllegalAddrTrapAcked_Type.__name__=_E
_CiscoRptrPortIllegalAddrTrapAcked_Object=MibTableColumn
ciscoRptrPortIllegalAddrTrapAcked=_CiscoRptrPortIllegalAddrTrapAcked_Object((1,3,6,1,4,1,9,9,22,1,1,1,10),_CiscoRptrPortIllegalAddrTrapAcked_Type())
ciscoRptrPortIllegalAddrTrapAcked.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoRptrPortIllegalAddrTrapAcked.setStatus(_B)
class _CiscoRptrPortIllegalAddrTrapEnabled_Type(TruthValue):defaultValue=2
_CiscoRptrPortIllegalAddrTrapEnabled_Type.__name__=_F
_CiscoRptrPortIllegalAddrTrapEnabled_Object=MibTableColumn
ciscoRptrPortIllegalAddrTrapEnabled=_CiscoRptrPortIllegalAddrTrapEnabled_Object((1,3,6,1,4,1,9,9,22,1,1,1,11),_CiscoRptrPortIllegalAddrTrapEnabled_Type())
ciscoRptrPortIllegalAddrTrapEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoRptrPortIllegalAddrTrapEnabled.setStatus(_B)
_CiscoRptrPortIllegalAddrFirstHeard_Type=TimeStamp
_CiscoRptrPortIllegalAddrFirstHeard_Object=MibTableColumn
ciscoRptrPortIllegalAddrFirstHeard=_CiscoRptrPortIllegalAddrFirstHeard_Object((1,3,6,1,4,1,9,9,22,1,1,1,12),_CiscoRptrPortIllegalAddrFirstHeard_Type())
ciscoRptrPortIllegalAddrFirstHeard.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortIllegalAddrFirstHeard.setStatus(_B)
_CiscoRptrPortIllegalAddrLastHeard_Type=TimeStamp
_CiscoRptrPortIllegalAddrLastHeard_Object=MibTableColumn
ciscoRptrPortIllegalAddrLastHeard=_CiscoRptrPortIllegalAddrLastHeard_Object((1,3,6,1,4,1,9,9,22,1,1,1,13),_CiscoRptrPortIllegalAddrLastHeard_Type())
ciscoRptrPortIllegalAddrLastHeard.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortIllegalAddrLastHeard.setStatus(_B)
_CiscoRptrPortLastIllegalAddrCount_Type=Gauge32
_CiscoRptrPortLastIllegalAddrCount_Object=MibTableColumn
ciscoRptrPortLastIllegalAddrCount=_CiscoRptrPortLastIllegalAddrCount_Object((1,3,6,1,4,1,9,9,22,1,1,1,14),_CiscoRptrPortLastIllegalAddrCount_Type())
ciscoRptrPortLastIllegalAddrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortLastIllegalAddrCount.setStatus(_B)
_CiscoRptrPortIllegalAddrTotalCount_Type=Counter32
_CiscoRptrPortIllegalAddrTotalCount_Object=MibTableColumn
ciscoRptrPortIllegalAddrTotalCount=_CiscoRptrPortIllegalAddrTotalCount_Object((1,3,6,1,4,1,9,9,22,1,1,1,15),_CiscoRptrPortIllegalAddrTotalCount_Type())
ciscoRptrPortIllegalAddrTotalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoRptrPortIllegalAddrTotalCount.setStatus(_B)
_CiscoRptrMIBglobal_ObjectIdentity=ObjectIdentity
ciscoRptrMIBglobal=_CiscoRptrMIBglobal_ObjectIdentity((1,3,6,1,4,1,9,9,22,1,2))
class _CiscoRptrTrapAlgorithm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('once',1),('decay',2)))
_CiscoRptrTrapAlgorithm_Type.__name__=_E
_CiscoRptrTrapAlgorithm_Object=MibScalar
ciscoRptrTrapAlgorithm=_CiscoRptrTrapAlgorithm_Object((1,3,6,1,4,1,9,9,22,1,2,1),_CiscoRptrTrapAlgorithm_Type())
ciscoRptrTrapAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoRptrTrapAlgorithm.setStatus(_B)
_CiscoRptrMIBConformance_ObjectIdentity=ObjectIdentity
ciscoRptrMIBConformance=_CiscoRptrMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,22,2))
_CiscoRptrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoRptrMIBCompliances=_CiscoRptrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,22,2,1))
_CiscoRptrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoRptrMIBGroups=_CiscoRptrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,22,2,2))
_CiscoRptrMIBTrapPrefix_ObjectIdentity=ObjectIdentity
ciscoRptrMIBTrapPrefix=_CiscoRptrMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,22,3))
_CiscoRptrMIBTraps_ObjectIdentity=ObjectIdentity
ciscoRptrMIBTraps=_CiscoRptrMIBTraps_ObjectIdentity((1,3,6,1,4,1,9,9,22,3,0))
rptrPortEntry.registerAugmentions((_A,_Q))
ciscoRptrPortEntry.setIndexNames(*rptrPortEntry.getIndexNames())
ciscoRptrMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,22,2,2,1))
ciscoRptrMIBGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_G)))
if mibBuilder.loadTexts:ciscoRptrMIBGroup.setStatus(_R)
ciscoRptrMIBPortGroupV11R01=ObjectGroup((1,3,6,1,4,1,9,9,22,2,2,2))
ciscoRptrMIBPortGroupV11R01.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_G),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoRptrMIBPortGroupV11R01.setStatus(_B)
ciscoRptrMIBGlobalsGroup=ObjectGroup((1,3,6,1,4,1,9,9,22,2,2,3))
ciscoRptrMIBGlobalsGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:ciscoRptrMIBGlobalsGroup.setStatus(_B)
ciscoRptrIllegalSrcAddrTrap=NotificationType((1,3,6,1,4,1,9,9,22,3,0,1))
ciscoRptrIllegalSrcAddrTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:ciscoRptrIllegalSrcAddrTrap.setStatus(_B)
ciscoRptrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,22,2,1,1))
ciscoRptrMIBCompliance.setObjects((_A,_Z))
if mibBuilder.loadTexts:ciscoRptrMIBCompliance.setStatus(_R)
ciscoRptrMIBComplianceV11R01=ModuleCompliance((1,3,6,1,4,1,9,9,22,2,1,2))
ciscoRptrMIBComplianceV11R01.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ciscoRptrMIBComplianceV11R01.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoRptrMIB':ciscoRptrMIB,'ciscoRptrMIBObjects':ciscoRptrMIBObjects,'ciscoRptrPortTable':ciscoRptrPortTable,_Q:ciscoRptrPortEntry,_I:ciscoRptrPortMDIStatus,_J:ciscoRptrPortLinkTestEnabled,_K:ciscoRptrPortLinkTestFailed,_L:ciscoRptrPortAutoPolarityEnabled,_M:ciscoRptrPortAutoPolarityCorrected,_N:ciscoRptrPortSrcAddrCtrl,_O:ciscoRptrPortAllowedSrcAddr,_P:ciscoRptrPortAllowedSrcAddrStatus,_G:ciscoRptrPortLastIllegalSrcAddr,_S:ciscoRptrPortIllegalAddrTrapAcked,_T:ciscoRptrPortIllegalAddrTrapEnabled,_U:ciscoRptrPortIllegalAddrFirstHeard,_V:ciscoRptrPortIllegalAddrLastHeard,_W:ciscoRptrPortLastIllegalAddrCount,_X:ciscoRptrPortIllegalAddrTotalCount,'ciscoRptrMIBglobal':ciscoRptrMIBglobal,_Y:ciscoRptrTrapAlgorithm,'ciscoRptrMIBConformance':ciscoRptrMIBConformance,'ciscoRptrMIBCompliances':ciscoRptrMIBCompliances,'ciscoRptrMIBCompliance':ciscoRptrMIBCompliance,'ciscoRptrMIBComplianceV11R01':ciscoRptrMIBComplianceV11R01,'ciscoRptrMIBGroups':ciscoRptrMIBGroups,_Z:ciscoRptrMIBGroup,_a:ciscoRptrMIBPortGroupV11R01,_b:ciscoRptrMIBGlobalsGroup,'ciscoRptrMIBTrapPrefix':ciscoRptrMIBTrapPrefix,'ciscoRptrMIBTraps':ciscoRptrMIBTraps,'ciscoRptrIllegalSrcAddrTrap':ciscoRptrIllegalSrcAddrTrap})