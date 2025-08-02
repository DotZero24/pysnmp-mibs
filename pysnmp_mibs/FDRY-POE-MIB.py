_I='snAgentPoeUnitIndex'
_H='snAgentPoeModuleNumber'
_G='deprecated'
_F='snAgentPoePortNumber'
_E='FDRY-POE-MIB'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snAgentSys,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','snAgentSys')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snAgentPoe=ModuleIdentity((1,3,6,1,4,1,1991,1,1,2,14))
if mibBuilder.loadTexts:snAgentPoe.setRevisions(('2009-09-30 00:00','2009-04-03 00:00','2017-08-07 00:00'))
_SnAgentPoeGbl_ObjectIdentity=ObjectIdentity
snAgentPoeGbl=_SnAgentPoeGbl_ObjectIdentity((1,3,6,1,4,1,1991,1,1,2,14,1))
_SnAgentPoeGblPowerCapacityTotal_Type=Unsigned32
_SnAgentPoeGblPowerCapacityTotal_Object=MibScalar
snAgentPoeGblPowerCapacityTotal=_SnAgentPoeGblPowerCapacityTotal_Object((1,3,6,1,4,1,1991,1,1,2,14,1,1),_SnAgentPoeGblPowerCapacityTotal_Type())
snAgentPoeGblPowerCapacityTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeGblPowerCapacityTotal.setStatus(_A)
_SnAgentPoeGblPowerCapacityFree_Type=Unsigned32
_SnAgentPoeGblPowerCapacityFree_Object=MibScalar
snAgentPoeGblPowerCapacityFree=_SnAgentPoeGblPowerCapacityFree_Object((1,3,6,1,4,1,1991,1,1,2,14,1,2),_SnAgentPoeGblPowerCapacityFree_Type())
snAgentPoeGblPowerCapacityFree.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeGblPowerCapacityFree.setStatus(_A)
_SnAgentPoeGblPowerAllocationsRequestsHonored_Type=Unsigned32
_SnAgentPoeGblPowerAllocationsRequestsHonored_Object=MibScalar
snAgentPoeGblPowerAllocationsRequestsHonored=_SnAgentPoeGblPowerAllocationsRequestsHonored_Object((1,3,6,1,4,1,1991,1,1,2,14,1,3),_SnAgentPoeGblPowerAllocationsRequestsHonored_Type())
snAgentPoeGblPowerAllocationsRequestsHonored.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeGblPowerAllocationsRequestsHonored.setStatus(_A)
_SnAgentPoePort_ObjectIdentity=ObjectIdentity
snAgentPoePort=_SnAgentPoePort_ObjectIdentity((1,3,6,1,4,1,1991,1,1,2,14,2))
_SnAgentPoePortTable_Object=MibTable
snAgentPoePortTable=_SnAgentPoePortTable_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2))
if mibBuilder.loadTexts:snAgentPoePortTable.setStatus(_A)
_SnAgentPoePortEntry_Object=MibTableRow
snAgentPoePortEntry=_SnAgentPoePortEntry_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1))
snAgentPoePortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:snAgentPoePortEntry.setStatus(_A)
_SnAgentPoePortNumber_Type=InterfaceIndex
_SnAgentPoePortNumber_Object=MibTableColumn
snAgentPoePortNumber=_SnAgentPoePortNumber_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,1),_SnAgentPoePortNumber_Type())
snAgentPoePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortNumber.setStatus(_A)
class _SnAgentPoePortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('disable',2),('enable',3),('enableLegacyDevice',4)))
_SnAgentPoePortControl_Type.__name__=_C
_SnAgentPoePortControl_Object=MibTableColumn
snAgentPoePortControl=_SnAgentPoePortControl_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,2),_SnAgentPoePortControl_Type())
snAgentPoePortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgentPoePortControl.setStatus(_A)
_SnAgentPoePortWattage_Type=Integer32
_SnAgentPoePortWattage_Object=MibTableColumn
snAgentPoePortWattage=_SnAgentPoePortWattage_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,3),_SnAgentPoePortWattage_Type())
snAgentPoePortWattage.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgentPoePortWattage.setStatus(_A)
_SnAgentPoePortClass_Type=Integer32
_SnAgentPoePortClass_Object=MibTableColumn
snAgentPoePortClass=_SnAgentPoePortClass_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,4),_SnAgentPoePortClass_Type())
snAgentPoePortClass.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgentPoePortClass.setStatus(_A)
class _SnAgentPoePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('invalid',0),('critical',1),('high',2),('low',3),('medium',4),('other',5)))
_SnAgentPoePortPriority_Type.__name__=_C
_SnAgentPoePortPriority_Object=MibTableColumn
snAgentPoePortPriority=_SnAgentPoePortPriority_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,5),_SnAgentPoePortPriority_Type())
snAgentPoePortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgentPoePortPriority.setStatus(_A)
_SnAgentPoePortConsumed_Type=Integer32
_SnAgentPoePortConsumed_Object=MibTableColumn
snAgentPoePortConsumed=_SnAgentPoePortConsumed_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,6),_SnAgentPoePortConsumed_Type())
snAgentPoePortConsumed.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortConsumed.setStatus(_A)
_SnAgentPoePortType_Type=DisplayString
_SnAgentPoePortType_Object=MibTableColumn
snAgentPoePortType=_SnAgentPoePortType_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,7),_SnAgentPoePortType_Type())
snAgentPoePortType.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortType.setStatus(_A)
_SnAgentPoePortPDClass_Type=Integer32
_SnAgentPoePortPDClass_Object=MibTableColumn
snAgentPoePortPDClass=_SnAgentPoePortPDClass_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,8),_SnAgentPoePortPDClass_Type())
snAgentPoePortPDClass.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortPDClass.setStatus(_A)
_SnAgentPoePortPDClassB_Type=Integer32
_SnAgentPoePortPDClassB_Object=MibTableColumn
snAgentPoePortPDClassB=_SnAgentPoePortPDClassB_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,9),_SnAgentPoePortPDClassB_Type())
snAgentPoePortPDClassB.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortPDClassB.setStatus(_A)
_SnAgentPoePortlldpReqPwr_Type=Integer32
_SnAgentPoePortlldpReqPwr_Object=MibTableColumn
snAgentPoePortlldpReqPwr=_SnAgentPoePortlldpReqPwr_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,10),_SnAgentPoePortlldpReqPwr_Type())
snAgentPoePortlldpReqPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortlldpReqPwr.setStatus(_A)
_SnAgentPoePortlldpReqPwrA_Type=Integer32
_SnAgentPoePortlldpReqPwrA_Object=MibTableColumn
snAgentPoePortlldpReqPwrA=_SnAgentPoePortlldpReqPwrA_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,11),_SnAgentPoePortlldpReqPwrA_Type())
snAgentPoePortlldpReqPwrA.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortlldpReqPwrA.setStatus(_G)
_SnAgentPoePortlldpReqPwrB_Type=Integer32
_SnAgentPoePortlldpReqPwrB_Object=MibTableColumn
snAgentPoePortlldpReqPwrB=_SnAgentPoePortlldpReqPwrB_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,12),_SnAgentPoePortlldpReqPwrB_Type())
snAgentPoePortlldpReqPwrB.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortlldpReqPwrB.setStatus(_G)
class _SnAgentPoePortCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('others',0),('twoPairPse',1),('fourPairPse',2)))
_SnAgentPoePortCapability_Type.__name__=_C
_SnAgentPoePortCapability_Object=MibTableColumn
snAgentPoePortCapability=_SnAgentPoePortCapability_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,13),_SnAgentPoePortCapability_Type())
snAgentPoePortCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortCapability.setStatus(_A)
_SnAgentPoePortMax2PairPwr_Type=Integer32
_SnAgentPoePortMax2PairPwr_Object=MibTableColumn
snAgentPoePortMax2PairPwr=_SnAgentPoePortMax2PairPwr_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,14),_SnAgentPoePortMax2PairPwr_Type())
snAgentPoePortMax2PairPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortMax2PairPwr.setStatus(_A)
_SnAgentPoePortMax4PairPwr_Type=Integer32
_SnAgentPoePortMax4PairPwr_Object=MibTableColumn
snAgentPoePortMax4PairPwr=_SnAgentPoePortMax4PairPwr_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,15),_SnAgentPoePortMax4PairPwr_Type())
snAgentPoePortMax4PairPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortMax4PairPwr.setStatus(_A)
class _SnAgentPoePortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('overdrive',1)))
_SnAgentPoePortMode_Type.__name__=_C
_SnAgentPoePortMode_Object=MibTableColumn
snAgentPoePortMode=_SnAgentPoePortMode_Object((1,3,6,1,4,1,1991,1,1,2,14,2,2,1,16),_SnAgentPoePortMode_Type())
snAgentPoePortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePortMode.setStatus(_A)
_SnAgentPoeModule_ObjectIdentity=ObjectIdentity
snAgentPoeModule=_SnAgentPoeModule_ObjectIdentity((1,3,6,1,4,1,1991,1,1,2,14,3))
_SnAgentPoeModuleTable_Object=MibTable
snAgentPoeModuleTable=_SnAgentPoeModuleTable_Object((1,3,6,1,4,1,1991,1,1,2,14,3,1))
if mibBuilder.loadTexts:snAgentPoeModuleTable.setStatus(_A)
_SnAgentPoeModuleEntry_Object=MibTableRow
snAgentPoeModuleEntry=_SnAgentPoeModuleEntry_Object((1,3,6,1,4,1,1991,1,1,2,14,3,1,1))
snAgentPoeModuleEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:snAgentPoeModuleEntry.setStatus(_A)
_SnAgentPoeModuleNumber_Type=Unsigned32
_SnAgentPoeModuleNumber_Object=MibTableColumn
snAgentPoeModuleNumber=_SnAgentPoeModuleNumber_Object((1,3,6,1,4,1,1991,1,1,2,14,3,1,1,1),_SnAgentPoeModuleNumber_Type())
snAgentPoeModuleNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeModuleNumber.setStatus(_A)
_SnAgentPoeModuleBudget_Type=Unsigned32
_SnAgentPoeModuleBudget_Object=MibTableColumn
snAgentPoeModuleBudget=_SnAgentPoeModuleBudget_Object((1,3,6,1,4,1,1991,1,1,2,14,3,1,1,2),_SnAgentPoeModuleBudget_Type())
snAgentPoeModuleBudget.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgentPoeModuleBudget.setStatus(_A)
class _SnAgentPoeModuleMaxPDTypeSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ieee802dot3af',0),('ieee802dot3at',1)))
_SnAgentPoeModuleMaxPDTypeSupport_Type.__name__=_C
_SnAgentPoeModuleMaxPDTypeSupport_Object=MibTableColumn
snAgentPoeModuleMaxPDTypeSupport=_SnAgentPoeModuleMaxPDTypeSupport_Object((1,3,6,1,4,1,1991,1,1,2,14,3,1,1,3),_SnAgentPoeModuleMaxPDTypeSupport_Type())
snAgentPoeModuleMaxPDTypeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeModuleMaxPDTypeSupport.setStatus(_A)
_SnAgentPoeUnit_ObjectIdentity=ObjectIdentity
snAgentPoeUnit=_SnAgentPoeUnit_ObjectIdentity((1,3,6,1,4,1,1991,1,1,2,14,4))
_SnAgentPoeUnitTable_Object=MibTable
snAgentPoeUnitTable=_SnAgentPoeUnitTable_Object((1,3,6,1,4,1,1991,1,1,2,14,4,1))
if mibBuilder.loadTexts:snAgentPoeUnitTable.setStatus(_A)
_SnAgentPoeUnitEntry_Object=MibTableRow
snAgentPoeUnitEntry=_SnAgentPoeUnitEntry_Object((1,3,6,1,4,1,1991,1,1,2,14,4,1,1))
snAgentPoeUnitEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:snAgentPoeUnitEntry.setStatus(_A)
_SnAgentPoeUnitIndex_Type=Unsigned32
_SnAgentPoeUnitIndex_Object=MibTableColumn
snAgentPoeUnitIndex=_SnAgentPoeUnitIndex_Object((1,3,6,1,4,1,1991,1,1,2,14,4,1,1,1),_SnAgentPoeUnitIndex_Type())
snAgentPoeUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeUnitIndex.setStatus(_A)
_SnAgentPoeUnitPowerCapacityTotal_Type=Unsigned32
_SnAgentPoeUnitPowerCapacityTotal_Object=MibTableColumn
snAgentPoeUnitPowerCapacityTotal=_SnAgentPoeUnitPowerCapacityTotal_Object((1,3,6,1,4,1,1991,1,1,2,14,4,1,1,2),_SnAgentPoeUnitPowerCapacityTotal_Type())
snAgentPoeUnitPowerCapacityTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeUnitPowerCapacityTotal.setStatus(_A)
_SnAgentPoeUnitPowerCapacityFree_Type=Unsigned32
_SnAgentPoeUnitPowerCapacityFree_Object=MibTableColumn
snAgentPoeUnitPowerCapacityFree=_SnAgentPoeUnitPowerCapacityFree_Object((1,3,6,1,4,1,1991,1,1,2,14,4,1,1,3),_SnAgentPoeUnitPowerCapacityFree_Type())
snAgentPoeUnitPowerCapacityFree.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeUnitPowerCapacityFree.setStatus(_A)
_SnAgentPoeUnitPowerAllocationsRequestsHonored_Type=Unsigned32
_SnAgentPoeUnitPowerAllocationsRequestsHonored_Object=MibTableColumn
snAgentPoeUnitPowerAllocationsRequestsHonored=_SnAgentPoeUnitPowerAllocationsRequestsHonored_Object((1,3,6,1,4,1,1991,1,1,2,14,4,1,1,4),_SnAgentPoeUnitPowerAllocationsRequestsHonored_Type())
snAgentPoeUnitPowerAllocationsRequestsHonored.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoeUnitPowerAllocationsRequestsHonored.setStatus(_A)
class _SnAgentPoePwrAllocationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('static',1),('dynamic',2)))
_SnAgentPoePwrAllocationType_Type.__name__=_C
_SnAgentPoePwrAllocationType_Object=MibTableColumn
snAgentPoePwrAllocationType=_SnAgentPoePwrAllocationType_Object((1,3,6,1,4,1,1991,1,1,2,14,4,1,1,5),_SnAgentPoePwrAllocationType_Type())
snAgentPoePwrAllocationType.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgentPoePwrAllocationType.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'snAgentPoe':snAgentPoe,'snAgentPoeGbl':snAgentPoeGbl,'snAgentPoeGblPowerCapacityTotal':snAgentPoeGblPowerCapacityTotal,'snAgentPoeGblPowerCapacityFree':snAgentPoeGblPowerCapacityFree,'snAgentPoeGblPowerAllocationsRequestsHonored':snAgentPoeGblPowerAllocationsRequestsHonored,'snAgentPoePort':snAgentPoePort,'snAgentPoePortTable':snAgentPoePortTable,'snAgentPoePortEntry':snAgentPoePortEntry,_F:snAgentPoePortNumber,'snAgentPoePortControl':snAgentPoePortControl,'snAgentPoePortWattage':snAgentPoePortWattage,'snAgentPoePortClass':snAgentPoePortClass,'snAgentPoePortPriority':snAgentPoePortPriority,'snAgentPoePortConsumed':snAgentPoePortConsumed,'snAgentPoePortType':snAgentPoePortType,'snAgentPoePortPDClass':snAgentPoePortPDClass,'snAgentPoePortPDClassB':snAgentPoePortPDClassB,'snAgentPoePortlldpReqPwr':snAgentPoePortlldpReqPwr,'snAgentPoePortlldpReqPwrA':snAgentPoePortlldpReqPwrA,'snAgentPoePortlldpReqPwrB':snAgentPoePortlldpReqPwrB,'snAgentPoePortCapability':snAgentPoePortCapability,'snAgentPoePortMax2PairPwr':snAgentPoePortMax2PairPwr,'snAgentPoePortMax4PairPwr':snAgentPoePortMax4PairPwr,'snAgentPoePortMode':snAgentPoePortMode,'snAgentPoeModule':snAgentPoeModule,'snAgentPoeModuleTable':snAgentPoeModuleTable,'snAgentPoeModuleEntry':snAgentPoeModuleEntry,_H:snAgentPoeModuleNumber,'snAgentPoeModuleBudget':snAgentPoeModuleBudget,'snAgentPoeModuleMaxPDTypeSupport':snAgentPoeModuleMaxPDTypeSupport,'snAgentPoeUnit':snAgentPoeUnit,'snAgentPoeUnitTable':snAgentPoeUnitTable,'snAgentPoeUnitEntry':snAgentPoeUnitEntry,_I:snAgentPoeUnitIndex,'snAgentPoeUnitPowerCapacityTotal':snAgentPoeUnitPowerCapacityTotal,'snAgentPoeUnitPowerCapacityFree':snAgentPoeUnitPowerCapacityFree,'snAgentPoeUnitPowerAllocationsRequestsHonored':snAgentPoeUnitPowerAllocationsRequestsHonored,'snAgentPoePwrAllocationType':snAgentPoePwrAllocationType})