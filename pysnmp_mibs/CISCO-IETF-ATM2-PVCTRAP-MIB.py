_U='atmSwitchServcHostGroup'
_T='atmPreviouslyFailedPVclTimeStamp'
_S='atmCurrentlyFailingPVclTimeStamp'
_R='atmPreviouslyFailedPVclInterval'
_Q='atmIntfPvcNotificationInterval'
_P='atmIntfPvcFailuresTrapEnable'
_O='atmInterfaceExtEntry'
_N='seconds'
_M='TruthValue'
_L='atmVclVpi'
_K='atmVclVci'
_J='atmIntfCurrentlyFailingPVcls'
_I='atmIntfPvcFailures'
_H='read-write'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='ATM-MIB'
_C='read-only'
_B='CISCO-IETF-ATM2-PVCTRAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmInterfaceConfEntry,atmVclVci,atmVclVpi=mibBuilder.importSymbols(_D,'atmInterfaceConfEntry',_K,_L)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_M)
ciscoIetfAtm2PvctrapMIB=ModuleIdentity((1,3,6,1,4,1,9,10,29))
_Atm2MIBObjects_ObjectIdentity=ObjectIdentity
atm2MIBObjects=_Atm2MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,29,1))
_AtmInterfaceExtTable_Object=MibTable
atmInterfaceExtTable=_AtmInterfaceExtTable_Object((1,3,6,1,4,1,9,10,29,1,14))
if mibBuilder.loadTexts:atmInterfaceExtTable.setStatus(_A)
_AtmInterfaceExtEntry_Object=MibTableRow
atmInterfaceExtEntry=_AtmInterfaceExtEntry_Object((1,3,6,1,4,1,9,10,29,1,14,1))
if mibBuilder.loadTexts:atmInterfaceExtEntry.setStatus(_A)
_AtmIntfPvcFailures_Type=Counter32
_AtmIntfPvcFailures_Object=MibTableColumn
atmIntfPvcFailures=_AtmIntfPvcFailures_Object((1,3,6,1,4,1,9,10,29,1,14,1,20),_AtmIntfPvcFailures_Type())
atmIntfPvcFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:atmIntfPvcFailures.setStatus(_A)
_AtmIntfCurrentlyFailingPVcls_Type=Gauge32
_AtmIntfCurrentlyFailingPVcls_Object=MibTableColumn
atmIntfCurrentlyFailingPVcls=_AtmIntfCurrentlyFailingPVcls_Object((1,3,6,1,4,1,9,10,29,1,14,1,22),_AtmIntfCurrentlyFailingPVcls_Type())
atmIntfCurrentlyFailingPVcls.setMaxAccess(_C)
if mibBuilder.loadTexts:atmIntfCurrentlyFailingPVcls.setStatus(_A)
class _AtmIntfPvcFailuresTrapEnable_Type(TruthValue):defaultValue=2
_AtmIntfPvcFailuresTrapEnable_Type.__name__=_M
_AtmIntfPvcFailuresTrapEnable_Object=MibTableColumn
atmIntfPvcFailuresTrapEnable=_AtmIntfPvcFailuresTrapEnable_Object((1,3,6,1,4,1,9,10,29,1,14,1,23),_AtmIntfPvcFailuresTrapEnable_Type())
atmIntfPvcFailuresTrapEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:atmIntfPvcFailuresTrapEnable.setStatus(_A)
class _AtmIntfPvcNotificationInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_AtmIntfPvcNotificationInterval_Type.__name__=_G
_AtmIntfPvcNotificationInterval_Object=MibTableColumn
atmIntfPvcNotificationInterval=_AtmIntfPvcNotificationInterval_Object((1,3,6,1,4,1,9,10,29,1,14,1,24),_AtmIntfPvcNotificationInterval_Type())
atmIntfPvcNotificationInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:atmIntfPvcNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:atmIntfPvcNotificationInterval.setUnits(_N)
class _AtmPreviouslyFailedPVclInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_AtmPreviouslyFailedPVclInterval_Type.__name__=_G
_AtmPreviouslyFailedPVclInterval_Object=MibTableColumn
atmPreviouslyFailedPVclInterval=_AtmPreviouslyFailedPVclInterval_Object((1,3,6,1,4,1,9,10,29,1,14,1,25),_AtmPreviouslyFailedPVclInterval_Type())
atmPreviouslyFailedPVclInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:atmPreviouslyFailedPVclInterval.setStatus(_A)
if mibBuilder.loadTexts:atmPreviouslyFailedPVclInterval.setUnits(_N)
_AtmCurrentlyFailingPVclTable_Object=MibTable
atmCurrentlyFailingPVclTable=_AtmCurrentlyFailingPVclTable_Object((1,3,6,1,4,1,9,10,29,1,21))
if mibBuilder.loadTexts:atmCurrentlyFailingPVclTable.setStatus(_A)
_AtmCurrentlyFailingPVclEntry_Object=MibTableRow
atmCurrentlyFailingPVclEntry=_AtmCurrentlyFailingPVclEntry_Object((1,3,6,1,4,1,9,10,29,1,21,1))
atmCurrentlyFailingPVclEntry.setIndexNames((0,_E,_F),(0,_D,_L),(0,_D,_K))
if mibBuilder.loadTexts:atmCurrentlyFailingPVclEntry.setStatus(_A)
_AtmCurrentlyFailingPVclTimeStamp_Type=TimeStamp
_AtmCurrentlyFailingPVclTimeStamp_Object=MibTableColumn
atmCurrentlyFailingPVclTimeStamp=_AtmCurrentlyFailingPVclTimeStamp_Object((1,3,6,1,4,1,9,10,29,1,21,1,1),_AtmCurrentlyFailingPVclTimeStamp_Type())
atmCurrentlyFailingPVclTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:atmCurrentlyFailingPVclTimeStamp.setStatus(_A)
_AtmPreviouslyFailedPVclTimeStamp_Type=TimeStamp
_AtmPreviouslyFailedPVclTimeStamp_Object=MibTableColumn
atmPreviouslyFailedPVclTimeStamp=_AtmPreviouslyFailedPVclTimeStamp_Object((1,3,6,1,4,1,9,10,29,1,21,1,2),_AtmPreviouslyFailedPVclTimeStamp_Type())
atmPreviouslyFailedPVclTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:atmPreviouslyFailedPVclTimeStamp.setStatus(_A)
_Atm2MIBTraps_ObjectIdentity=ObjectIdentity
atm2MIBTraps=_Atm2MIBTraps_ObjectIdentity((1,3,6,1,4,1,9,10,29,2))
_AtmPvcTraps_ObjectIdentity=ObjectIdentity
atmPvcTraps=_AtmPvcTraps_ObjectIdentity((1,3,6,1,4,1,9,10,29,2,1))
_AtmPvcTrapsPrefix_ObjectIdentity=ObjectIdentity
atmPvcTrapsPrefix=_AtmPvcTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,29,2,1,0))
_Atm2MIBConformance_ObjectIdentity=ObjectIdentity
atm2MIBConformance=_Atm2MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,29,3))
_Atm2MIBGroups_ObjectIdentity=ObjectIdentity
atm2MIBGroups=_Atm2MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,29,3,1))
_Atm2MIBCompliances_ObjectIdentity=ObjectIdentity
atm2MIBCompliances=_Atm2MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,29,3,2))
atmInterfaceConfEntry.registerAugmentions((_B,_O))
atmInterfaceExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmSwitchServcHostGroup=ObjectGroup((1,3,6,1,4,1,9,10,29,3,1,1))
atmSwitchServcHostGroup.setObjects(*((_B,_I),(_B,_J),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:atmSwitchServcHostGroup.setStatus(_A)
atmIntfPvcFailuresTrap=NotificationType((1,3,6,1,4,1,9,10,29,2,1,0,1))
atmIntfPvcFailuresTrap.setObjects(*((_E,_F),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:atmIntfPvcFailuresTrap.setStatus(_A)
atm2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,29,3,2,1))
atm2MIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:atm2MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIetfAtm2PvctrapMIB':ciscoIetfAtm2PvctrapMIB,'atm2MIBObjects':atm2MIBObjects,'atmInterfaceExtTable':atmInterfaceExtTable,_O:atmInterfaceExtEntry,_I:atmIntfPvcFailures,_J:atmIntfCurrentlyFailingPVcls,_P:atmIntfPvcFailuresTrapEnable,_Q:atmIntfPvcNotificationInterval,_R:atmPreviouslyFailedPVclInterval,'atmCurrentlyFailingPVclTable':atmCurrentlyFailingPVclTable,'atmCurrentlyFailingPVclEntry':atmCurrentlyFailingPVclEntry,_S:atmCurrentlyFailingPVclTimeStamp,_T:atmPreviouslyFailedPVclTimeStamp,'atm2MIBTraps':atm2MIBTraps,'atmPvcTraps':atmPvcTraps,'atmPvcTrapsPrefix':atmPvcTrapsPrefix,'atmIntfPvcFailuresTrap':atmIntfPvcFailuresTrap,'atm2MIBConformance':atm2MIBConformance,'atm2MIBGroups':atm2MIBGroups,_U:atmSwitchServcHostGroup,'atm2MIBCompliances':atm2MIBCompliances,'atm2MIBCompliance':atm2MIBCompliance})