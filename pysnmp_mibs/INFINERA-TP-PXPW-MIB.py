_P='pxmPwGroup'
_O='pxmPwAssociatedMPLSTunnel'
_N='pxmPwFlapActionClear'
_M='pxmPwSplitHorizonGroupID'
_L='pxmPwPmHistStatsEnable'
_K='pxmPwCreationType'
_J='pxmPwOutgoingLabel'
_I='pxmPwIncomingLabel'
_H='pxmPwSetupMode'
_G='pxmPwMTUSize'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-PXPW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,FloatTenths,InfnCreationType,InfnFlapActionClear,InfnPWSetupMode,InfnPmHistStatsControl=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnCreationType','InfnFlapActionClear','InfnPWSetupMode','InfnPmHistStatsControl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmPwMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,75))
if mibBuilder.loadTexts:pxmPwMIB.setRevisions(('2016-05-20 00:00',))
_PxmPwTable_Object=MibTable
pxmPwTable=_PxmPwTable_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1))
if mibBuilder.loadTexts:pxmPwTable.setStatus(_A)
_PxmPwEntry_Object=MibTableRow
pxmPwEntry=_PxmPwEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1))
pxmPwEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pxmPwEntry.setStatus(_A)
_PxmPwMTUSize_Type=Integer32
_PxmPwMTUSize_Object=MibTableColumn
pxmPwMTUSize=_PxmPwMTUSize_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,1),_PxmPwMTUSize_Type())
pxmPwMTUSize.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPwMTUSize.setStatus(_A)
_PxmPwSetupMode_Type=InfnPWSetupMode
_PxmPwSetupMode_Object=MibTableColumn
pxmPwSetupMode=_PxmPwSetupMode_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,2),_PxmPwSetupMode_Type())
pxmPwSetupMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmPwSetupMode.setStatus(_A)
_PxmPwIncomingLabel_Type=Integer32
_PxmPwIncomingLabel_Object=MibTableColumn
pxmPwIncomingLabel=_PxmPwIncomingLabel_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,3),_PxmPwIncomingLabel_Type())
pxmPwIncomingLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPwIncomingLabel.setStatus(_A)
_PxmPwOutgoingLabel_Type=Integer32
_PxmPwOutgoingLabel_Object=MibTableColumn
pxmPwOutgoingLabel=_PxmPwOutgoingLabel_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,4),_PxmPwOutgoingLabel_Type())
pxmPwOutgoingLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPwOutgoingLabel.setStatus(_A)
_PxmPwCreationType_Type=InfnCreationType
_PxmPwCreationType_Object=MibTableColumn
pxmPwCreationType=_PxmPwCreationType_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,5),_PxmPwCreationType_Type())
pxmPwCreationType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPwCreationType.setStatus(_A)
_PxmPwPmHistStatsEnable_Type=InfnPmHistStatsControl
_PxmPwPmHistStatsEnable_Object=MibTableColumn
pxmPwPmHistStatsEnable=_PxmPwPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,6),_PxmPwPmHistStatsEnable_Type())
pxmPwPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmPwPmHistStatsEnable.setStatus(_A)
_PxmPwSplitHorizonGroupID_Type=Integer32
_PxmPwSplitHorizonGroupID_Object=MibTableColumn
pxmPwSplitHorizonGroupID=_PxmPwSplitHorizonGroupID_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,7),_PxmPwSplitHorizonGroupID_Type())
pxmPwSplitHorizonGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPwSplitHorizonGroupID.setStatus(_A)
_PxmPwFlapActionClear_Type=InfnFlapActionClear
_PxmPwFlapActionClear_Object=MibTableColumn
pxmPwFlapActionClear=_PxmPwFlapActionClear_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,8),_PxmPwFlapActionClear_Type())
pxmPwFlapActionClear.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmPwFlapActionClear.setStatus(_A)
_PxmPwAssociatedMPLSTunnel_Type=DisplayString
_PxmPwAssociatedMPLSTunnel_Object=MibTableColumn
pxmPwAssociatedMPLSTunnel=_PxmPwAssociatedMPLSTunnel_Object((1,3,6,1,4,1,21296,2,2,2,2,75,1,1,9),_PxmPwAssociatedMPLSTunnel_Type())
pxmPwAssociatedMPLSTunnel.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmPwAssociatedMPLSTunnel.setStatus(_A)
_PxmPwConformance_ObjectIdentity=ObjectIdentity
pxmPwConformance=_PxmPwConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,75,3))
_PxmPwCompliances_ObjectIdentity=ObjectIdentity
pxmPwCompliances=_PxmPwCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,75,3,1))
_PxmPwGroups_ObjectIdentity=ObjectIdentity
pxmPwGroups=_PxmPwGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,75,3,2))
pxmPwGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,75,3,2,1))
pxmPwGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:pxmPwGroup.setStatus(_A)
pxmPwCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,75,3,1,1))
pxmPwCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:pxmPwCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmPwMIB':pxmPwMIB,'pxmPwTable':pxmPwTable,'pxmPwEntry':pxmPwEntry,_G:pxmPwMTUSize,_H:pxmPwSetupMode,_I:pxmPwIncomingLabel,_J:pxmPwOutgoingLabel,_K:pxmPwCreationType,_L:pxmPwPmHistStatsEnable,_M:pxmPwSplitHorizonGroupID,_N:pxmPwFlapActionClear,_O:pxmPwAssociatedMPLSTunnel,'pxmPwConformance':pxmPwConformance,'pxmPwCompliances':pxmPwCompliances,'pxmPwCompliance':pxmPwCompliance,'pxmPwGroups':pxmPwGroups,_P:pxmPwGroup})