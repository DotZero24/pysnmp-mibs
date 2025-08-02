_T='ciscoL2DevMonRadioConfigGroup'
_S='cl2DevMonSwitchover'
_R='cl2DevMonActiveLocalRadioIndex'
_Q='cl2DevMonActiveRadioMacType'
_P='cl2DevMonActiveRowStatus'
_O='cl2DevMonNotifEnabled'
_N='cl2DevMonInStandbyMode'
_M='seconds'
_L='cl2DevMonActiveMacAddress'
_K='read-write'
_J='Integer32'
_I='ciscoL2DevMonNotificationGroup'
_H='ciscoL2DevMonConfigGroup'
_G='cl2DevMonActivePollingTimeOut'
_F='cl2DevMonActivePollingFrequency'
_E='TruthValue'
_D='Unsigned32'
_C='read-create'
_B='current'
_A='CISCO-L2-DEV-MONITORING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
ciscoL2DevMonMIB=ModuleIdentity((1,3,6,1,4,1,9,9,271))
if mibBuilder.loadTexts:ciscoL2DevMonMIB.setRevisions(('2003-07-22 00:00','2001-09-27 00:00'))
_CiscoL2DevMonMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoL2DevMonMIBNotifications=_CiscoL2DevMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,271,0))
_CiscoL2DevMonMIBObjects_ObjectIdentity=ObjectIdentity
ciscoL2DevMonMIBObjects=_CiscoL2DevMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,271,1))
_Cl2DevMonConfig_ObjectIdentity=ObjectIdentity
cl2DevMonConfig=_Cl2DevMonConfig_ObjectIdentity((1,3,6,1,4,1,9,9,271,1,1))
class _Cl2DevMonInStandbyMode_Type(TruthValue):defaultValue=2
_Cl2DevMonInStandbyMode_Type.__name__=_E
_Cl2DevMonInStandbyMode_Object=MibScalar
cl2DevMonInStandbyMode=_Cl2DevMonInStandbyMode_Object((1,3,6,1,4,1,9,9,271,1,1,1),_Cl2DevMonInStandbyMode_Type())
cl2DevMonInStandbyMode.setMaxAccess(_K)
if mibBuilder.loadTexts:cl2DevMonInStandbyMode.setStatus(_B)
class _Cl2DevMonNotifEnabled_Type(TruthValue):defaultValue=2
_Cl2DevMonNotifEnabled_Type.__name__=_E
_Cl2DevMonNotifEnabled_Object=MibScalar
cl2DevMonNotifEnabled=_Cl2DevMonNotifEnabled_Object((1,3,6,1,4,1,9,9,271,1,1,2),_Cl2DevMonNotifEnabled_Type())
cl2DevMonNotifEnabled.setMaxAccess(_K)
if mibBuilder.loadTexts:cl2DevMonNotifEnabled.setStatus(_B)
_Cl2DevMonActiveTable_Object=MibTable
cl2DevMonActiveTable=_Cl2DevMonActiveTable_Object((1,3,6,1,4,1,9,9,271,1,1,3))
if mibBuilder.loadTexts:cl2DevMonActiveTable.setStatus(_B)
_Cl2DevMonActiveEntry_Object=MibTableRow
cl2DevMonActiveEntry=_Cl2DevMonActiveEntry_Object((1,3,6,1,4,1,9,9,271,1,1,3,1))
cl2DevMonActiveEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:cl2DevMonActiveEntry.setStatus(_B)
_Cl2DevMonActiveMacAddress_Type=MacAddress
_Cl2DevMonActiveMacAddress_Object=MibTableColumn
cl2DevMonActiveMacAddress=_Cl2DevMonActiveMacAddress_Object((1,3,6,1,4,1,9,9,271,1,1,3,1,1),_Cl2DevMonActiveMacAddress_Type())
cl2DevMonActiveMacAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cl2DevMonActiveMacAddress.setStatus(_B)
class _Cl2DevMonActivePollingFrequency_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_Cl2DevMonActivePollingFrequency_Type.__name__=_D
_Cl2DevMonActivePollingFrequency_Object=MibTableColumn
cl2DevMonActivePollingFrequency=_Cl2DevMonActivePollingFrequency_Object((1,3,6,1,4,1,9,9,271,1,1,3,1,2),_Cl2DevMonActivePollingFrequency_Type())
cl2DevMonActivePollingFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2DevMonActivePollingFrequency.setStatus(_B)
if mibBuilder.loadTexts:cl2DevMonActivePollingFrequency.setUnits(_M)
class _Cl2DevMonActivePollingTimeOut_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_Cl2DevMonActivePollingTimeOut_Type.__name__=_D
_Cl2DevMonActivePollingTimeOut_Object=MibTableColumn
cl2DevMonActivePollingTimeOut=_Cl2DevMonActivePollingTimeOut_Object((1,3,6,1,4,1,9,9,271,1,1,3,1,3),_Cl2DevMonActivePollingTimeOut_Type())
cl2DevMonActivePollingTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2DevMonActivePollingTimeOut.setStatus(_B)
if mibBuilder.loadTexts:cl2DevMonActivePollingTimeOut.setUnits(_M)
_Cl2DevMonActiveRowStatus_Type=RowStatus
_Cl2DevMonActiveRowStatus_Object=MibTableColumn
cl2DevMonActiveRowStatus=_Cl2DevMonActiveRowStatus_Object((1,3,6,1,4,1,9,9,271,1,1,3,1,4),_Cl2DevMonActiveRowStatus_Type())
cl2DevMonActiveRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2DevMonActiveRowStatus.setStatus(_B)
class _Cl2DevMonActiveRadioMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ieee802dot11a',1),('ieee802dot11b',2),('ieee802dot11g',3)))
_Cl2DevMonActiveRadioMacType_Type.__name__=_J
_Cl2DevMonActiveRadioMacType_Object=MibTableColumn
cl2DevMonActiveRadioMacType=_Cl2DevMonActiveRadioMacType_Object((1,3,6,1,4,1,9,9,271,1,1,3,1,5),_Cl2DevMonActiveRadioMacType_Type())
cl2DevMonActiveRadioMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2DevMonActiveRadioMacType.setStatus(_B)
_Cl2DevMonActiveLocalRadioIndex_Type=InterfaceIndex
_Cl2DevMonActiveLocalRadioIndex_Object=MibTableColumn
cl2DevMonActiveLocalRadioIndex=_Cl2DevMonActiveLocalRadioIndex_Object((1,3,6,1,4,1,9,9,271,1,1,3,1,6),_Cl2DevMonActiveLocalRadioIndex_Type())
cl2DevMonActiveLocalRadioIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2DevMonActiveLocalRadioIndex.setStatus(_B)
_CiscoL2DevMonMIBConformance_ObjectIdentity=ObjectIdentity
ciscoL2DevMonMIBConformance=_CiscoL2DevMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,271,2))
_CiscoL2DevMonMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoL2DevMonMIBCompliances=_CiscoL2DevMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,271,2,1))
_CiscoL2DevMonMIBGroups_ObjectIdentity=ObjectIdentity
ciscoL2DevMonMIBGroups=_CiscoL2DevMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,271,2,2))
ciscoL2DevMonConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,271,2,2,1))
ciscoL2DevMonConfigGroup.setObjects(*((_A,_N),(_A,_O),(_A,_F),(_A,_G),(_A,_P)))
if mibBuilder.loadTexts:ciscoL2DevMonConfigGroup.setStatus(_B)
ciscoL2DevMonRadioConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,271,2,2,3))
ciscoL2DevMonRadioConfigGroup.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoL2DevMonRadioConfigGroup.setStatus(_B)
cl2DevMonSwitchover=NotificationType((1,3,6,1,4,1,9,9,271,0,1))
cl2DevMonSwitchover.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cl2DevMonSwitchover.setStatus(_B)
ciscoL2DevMonNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,271,2,2,2))
ciscoL2DevMonNotificationGroup.setObjects((_A,_S))
if mibBuilder.loadTexts:ciscoL2DevMonNotificationGroup.setStatus(_B)
ciscoL2DevMonCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,271,2,1,1))
ciscoL2DevMonCompliance.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ciscoL2DevMonCompliance.setStatus('deprecated')
ciscoL2DevMonComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,271,2,1,2))
ciscoL2DevMonComplianceRev1.setObjects(*((_A,_H),(_A,_I),(_A,_T)))
if mibBuilder.loadTexts:ciscoL2DevMonComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoL2DevMonMIB':ciscoL2DevMonMIB,'ciscoL2DevMonMIBNotifications':ciscoL2DevMonMIBNotifications,_S:cl2DevMonSwitchover,'ciscoL2DevMonMIBObjects':ciscoL2DevMonMIBObjects,'cl2DevMonConfig':cl2DevMonConfig,_N:cl2DevMonInStandbyMode,_O:cl2DevMonNotifEnabled,'cl2DevMonActiveTable':cl2DevMonActiveTable,'cl2DevMonActiveEntry':cl2DevMonActiveEntry,_L:cl2DevMonActiveMacAddress,_F:cl2DevMonActivePollingFrequency,_G:cl2DevMonActivePollingTimeOut,_P:cl2DevMonActiveRowStatus,_Q:cl2DevMonActiveRadioMacType,_R:cl2DevMonActiveLocalRadioIndex,'ciscoL2DevMonMIBConformance':ciscoL2DevMonMIBConformance,'ciscoL2DevMonMIBCompliances':ciscoL2DevMonMIBCompliances,'ciscoL2DevMonCompliance':ciscoL2DevMonCompliance,'ciscoL2DevMonComplianceRev1':ciscoL2DevMonComplianceRev1,'ciscoL2DevMonMIBGroups':ciscoL2DevMonMIBGroups,_H:ciscoL2DevMonConfigGroup,_I:ciscoL2DevMonNotificationGroup,_T:ciscoL2DevMonRadioConfigGroup})