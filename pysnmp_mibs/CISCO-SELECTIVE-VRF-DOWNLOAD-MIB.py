_e='csvdMIBNotificationGroup'
_d='csvdMIBNotificationEnableGroup'
_c='csvdMIBGroup'
_b='csvdEntityRoleChangeNotification'
_a='csvdEntityRoleChangeNotificationEnable'
_Z='csvdTableConvergedFlag'
_Y='csvdRemotePrefixCount'
_X='csvdLocalPrefixCount'
_W='csvdPrefixCount'
_V='csvdRoleHistoryRoleChangeTime'
_U='csvdRoleHistoryRole'
_T='csvdRoleHistoryLastIndex'
_S='csvdRoleHistorySize'
_R='csvdStateEntityRoleTransitions'
_Q='csvdStateEntityRoleLastChange'
_P='csvdCounterDiscontinuityTime'
_O='csvdOperEnable'
_N='csvdAdminEnable'
_M='csvdVrfName'
_L='csvdRoleHistoryIndex'
_K='csvdStateEntityRole'
_J='not-accessible'
_I='csvdStateAFI'
_H='read-write'
_G='TruthValue'
_F='Unsigned32'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-SELECTIVE-VRF-DOWNLOAD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
MplsL3VpnName,=mibBuilder.importSymbols('MPLS-L3VPN-STD-MIB','MplsL3VpnName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_G)
ciscoSelectiveVrfDownloadMIB=ModuleIdentity((1,3,6,1,4,1,9,9,775))
if mibBuilder.loadTexts:ciscoSelectiveVrfDownloadMIB.setRevisions(('2011-06-22 00:00',))
class SVDEntityRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('invalid',1),('standard',2),('core',3),('customer',4),('noInterest',5),('vpnOnlyCustomer',6)))
_CiscoSelectiveVrfDownloadMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSelectiveVrfDownloadMIBNotifs=_CiscoSelectiveVrfDownloadMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,775,0))
_CiscoSelectiveVrfDownloadMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSelectiveVrfDownloadMIBObjects=_CiscoSelectiveVrfDownloadMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,775,1))
class _CsvdAdminEnable_Type(TruthValue):defaultValue=1
_CsvdAdminEnable_Type.__name__=_G
_CsvdAdminEnable_Object=MibScalar
csvdAdminEnable=_CsvdAdminEnable_Object((1,3,6,1,4,1,9,9,775,1,1),_CsvdAdminEnable_Type())
csvdAdminEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:csvdAdminEnable.setStatus(_A)
_CsvdOperEnable_Type=TruthValue
_CsvdOperEnable_Object=MibScalar
csvdOperEnable=_CsvdOperEnable_Object((1,3,6,1,4,1,9,9,775,1,2),_CsvdOperEnable_Type())
csvdOperEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdOperEnable.setStatus(_A)
class _CsvdEntityRoleChangeNotificationEnable_Type(TruthValue):defaultValue=1
_CsvdEntityRoleChangeNotificationEnable_Type.__name__=_G
_CsvdEntityRoleChangeNotificationEnable_Object=MibScalar
csvdEntityRoleChangeNotificationEnable=_CsvdEntityRoleChangeNotificationEnable_Object((1,3,6,1,4,1,9,9,775,1,3),_CsvdEntityRoleChangeNotificationEnable_Type())
csvdEntityRoleChangeNotificationEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:csvdEntityRoleChangeNotificationEnable.setStatus(_A)
_CsvdCounterDiscontinuityTime_Type=TimeStamp
_CsvdCounterDiscontinuityTime_Object=MibScalar
csvdCounterDiscontinuityTime=_CsvdCounterDiscontinuityTime_Object((1,3,6,1,4,1,9,9,775,1,4),_CsvdCounterDiscontinuityTime_Type())
csvdCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdCounterDiscontinuityTime.setStatus(_A)
_CsvdStateTable_Object=MibTable
csvdStateTable=_CsvdStateTable_Object((1,3,6,1,4,1,9,9,775,1,5))
if mibBuilder.loadTexts:csvdStateTable.setStatus(_A)
_CsvdStateEntry_Object=MibTableRow
csvdStateEntry=_CsvdStateEntry_Object((1,3,6,1,4,1,9,9,775,1,5,1))
csvdStateEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:csvdStateEntry.setStatus(_A)
_CsvdStateAFI_Type=AddressFamilyNumbers
_CsvdStateAFI_Object=MibTableColumn
csvdStateAFI=_CsvdStateAFI_Object((1,3,6,1,4,1,9,9,775,1,5,1,1),_CsvdStateAFI_Type())
csvdStateAFI.setMaxAccess(_J)
if mibBuilder.loadTexts:csvdStateAFI.setStatus(_A)
_CsvdStateEntityRole_Type=SVDEntityRole
_CsvdStateEntityRole_Object=MibTableColumn
csvdStateEntityRole=_CsvdStateEntityRole_Object((1,3,6,1,4,1,9,9,775,1,5,1,2),_CsvdStateEntityRole_Type())
csvdStateEntityRole.setMaxAccess(_H)
if mibBuilder.loadTexts:csvdStateEntityRole.setStatus(_A)
_CsvdStateEntityRoleLastChange_Type=TimeStamp
_CsvdStateEntityRoleLastChange_Object=MibTableColumn
csvdStateEntityRoleLastChange=_CsvdStateEntityRoleLastChange_Object((1,3,6,1,4,1,9,9,775,1,5,1,3),_CsvdStateEntityRoleLastChange_Type())
csvdStateEntityRoleLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdStateEntityRoleLastChange.setStatus(_A)
_CsvdStateEntityRoleTransitions_Type=Counter32
_CsvdStateEntityRoleTransitions_Object=MibTableColumn
csvdStateEntityRoleTransitions=_CsvdStateEntityRoleTransitions_Object((1,3,6,1,4,1,9,9,775,1,5,1,4),_CsvdStateEntityRoleTransitions_Type())
csvdStateEntityRoleTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdStateEntityRoleTransitions.setStatus(_A)
_CsvdRoleHistory_ObjectIdentity=ObjectIdentity
csvdRoleHistory=_CsvdRoleHistory_ObjectIdentity((1,3,6,1,4,1,9,9,775,1,6))
class _CsvdRoleHistorySize_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CsvdRoleHistorySize_Type.__name__=_F
_CsvdRoleHistorySize_Object=MibScalar
csvdRoleHistorySize=_CsvdRoleHistorySize_Object((1,3,6,1,4,1,9,9,775,1,6,1),_CsvdRoleHistorySize_Type())
csvdRoleHistorySize.setMaxAccess(_H)
if mibBuilder.loadTexts:csvdRoleHistorySize.setStatus(_A)
class _CsvdRoleHistoryLastIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CsvdRoleHistoryLastIndex_Type.__name__=_F
_CsvdRoleHistoryLastIndex_Object=MibScalar
csvdRoleHistoryLastIndex=_CsvdRoleHistoryLastIndex_Object((1,3,6,1,4,1,9,9,775,1,6,2),_CsvdRoleHistoryLastIndex_Type())
csvdRoleHistoryLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdRoleHistoryLastIndex.setStatus(_A)
_CsvdRoleHistoryTable_Object=MibTable
csvdRoleHistoryTable=_CsvdRoleHistoryTable_Object((1,3,6,1,4,1,9,9,775,1,6,3))
if mibBuilder.loadTexts:csvdRoleHistoryTable.setStatus(_A)
_CsvdRoleHistoryEntry_Object=MibTableRow
csvdRoleHistoryEntry=_CsvdRoleHistoryEntry_Object((1,3,6,1,4,1,9,9,775,1,6,3,1))
csvdRoleHistoryEntry.setIndexNames((0,_D,_E),(0,_B,_I),(0,_B,_L))
if mibBuilder.loadTexts:csvdRoleHistoryEntry.setStatus(_A)
class _CsvdRoleHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CsvdRoleHistoryIndex_Type.__name__=_F
_CsvdRoleHistoryIndex_Object=MibTableColumn
csvdRoleHistoryIndex=_CsvdRoleHistoryIndex_Object((1,3,6,1,4,1,9,9,775,1,6,3,1,1),_CsvdRoleHistoryIndex_Type())
csvdRoleHistoryIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:csvdRoleHistoryIndex.setStatus(_A)
_CsvdRoleHistoryRole_Type=SVDEntityRole
_CsvdRoleHistoryRole_Object=MibTableColumn
csvdRoleHistoryRole=_CsvdRoleHistoryRole_Object((1,3,6,1,4,1,9,9,775,1,6,3,1,2),_CsvdRoleHistoryRole_Type())
csvdRoleHistoryRole.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdRoleHistoryRole.setStatus(_A)
_CsvdRoleHistoryRoleChangeTime_Type=TimeStamp
_CsvdRoleHistoryRoleChangeTime_Object=MibTableColumn
csvdRoleHistoryRoleChangeTime=_CsvdRoleHistoryRoleChangeTime_Object((1,3,6,1,4,1,9,9,775,1,6,3,1,3),_CsvdRoleHistoryRoleChangeTime_Type())
csvdRoleHistoryRoleChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdRoleHistoryRoleChangeTime.setStatus(_A)
_CsvdVrfTable_Object=MibTable
csvdVrfTable=_CsvdVrfTable_Object((1,3,6,1,4,1,9,9,775,1,7))
if mibBuilder.loadTexts:csvdVrfTable.setStatus(_A)
_CsvdVrfEntry_Object=MibTableRow
csvdVrfEntry=_CsvdVrfEntry_Object((1,3,6,1,4,1,9,9,775,1,7,1))
csvdVrfEntry.setIndexNames((0,_D,_E),(0,_B,_I),(0,_B,_M))
if mibBuilder.loadTexts:csvdVrfEntry.setStatus(_A)
_CsvdVrfName_Type=MplsL3VpnName
_CsvdVrfName_Object=MibTableColumn
csvdVrfName=_CsvdVrfName_Object((1,3,6,1,4,1,9,9,775,1,7,1,1),_CsvdVrfName_Type())
csvdVrfName.setMaxAccess(_J)
if mibBuilder.loadTexts:csvdVrfName.setStatus(_A)
_CsvdPrefixCount_Type=Gauge32
_CsvdPrefixCount_Object=MibTableColumn
csvdPrefixCount=_CsvdPrefixCount_Object((1,3,6,1,4,1,9,9,775,1,7,1,2),_CsvdPrefixCount_Type())
csvdPrefixCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdPrefixCount.setStatus(_A)
_CsvdLocalPrefixCount_Type=Gauge32
_CsvdLocalPrefixCount_Object=MibTableColumn
csvdLocalPrefixCount=_CsvdLocalPrefixCount_Object((1,3,6,1,4,1,9,9,775,1,7,1,3),_CsvdLocalPrefixCount_Type())
csvdLocalPrefixCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdLocalPrefixCount.setStatus(_A)
_CsvdRemotePrefixCount_Type=Gauge32
_CsvdRemotePrefixCount_Object=MibTableColumn
csvdRemotePrefixCount=_CsvdRemotePrefixCount_Object((1,3,6,1,4,1,9,9,775,1,7,1,4),_CsvdRemotePrefixCount_Type())
csvdRemotePrefixCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdRemotePrefixCount.setStatus(_A)
class _CsvdTableConvergedFlag_Type(TruthValue):defaultValue=2
_CsvdTableConvergedFlag_Type.__name__=_G
_CsvdTableConvergedFlag_Object=MibTableColumn
csvdTableConvergedFlag=_CsvdTableConvergedFlag_Object((1,3,6,1,4,1,9,9,775,1,7,1,5),_CsvdTableConvergedFlag_Type())
csvdTableConvergedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:csvdTableConvergedFlag.setStatus(_A)
_CiscoSelectiveVrfDownloadMIBConform_ObjectIdentity=ObjectIdentity
ciscoSelectiveVrfDownloadMIBConform=_CiscoSelectiveVrfDownloadMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,775,2))
_CsvdMIBCompliances_ObjectIdentity=ObjectIdentity
csvdMIBCompliances=_CsvdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,775,2,1))
_CsvdMIBGroups_ObjectIdentity=ObjectIdentity
csvdMIBGroups=_CsvdMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,775,2,2))
csvdMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,775,2,2,1))
csvdMIBGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_K),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:csvdMIBGroup.setStatus(_A)
csvdMIBNotificationEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,775,2,2,2))
csvdMIBNotificationEnableGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:csvdMIBNotificationEnableGroup.setStatus(_A)
csvdEntityRoleChangeNotification=NotificationType((1,3,6,1,4,1,9,9,775,0,1))
csvdEntityRoleChangeNotification.setObjects((_B,_K))
if mibBuilder.loadTexts:csvdEntityRoleChangeNotification.setStatus(_A)
csvdMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,775,2,2,3))
csvdMIBNotificationGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:csvdMIBNotificationGroup.setStatus(_A)
csvdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,775,2,1,1))
csvdMIBCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:csvdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SVDEntityRole':SVDEntityRole,'ciscoSelectiveVrfDownloadMIB':ciscoSelectiveVrfDownloadMIB,'ciscoSelectiveVrfDownloadMIBNotifs':ciscoSelectiveVrfDownloadMIBNotifs,_b:csvdEntityRoleChangeNotification,'ciscoSelectiveVrfDownloadMIBObjects':ciscoSelectiveVrfDownloadMIBObjects,_N:csvdAdminEnable,_O:csvdOperEnable,_a:csvdEntityRoleChangeNotificationEnable,_P:csvdCounterDiscontinuityTime,'csvdStateTable':csvdStateTable,'csvdStateEntry':csvdStateEntry,_I:csvdStateAFI,_K:csvdStateEntityRole,_Q:csvdStateEntityRoleLastChange,_R:csvdStateEntityRoleTransitions,'csvdRoleHistory':csvdRoleHistory,_S:csvdRoleHistorySize,_T:csvdRoleHistoryLastIndex,'csvdRoleHistoryTable':csvdRoleHistoryTable,'csvdRoleHistoryEntry':csvdRoleHistoryEntry,_L:csvdRoleHistoryIndex,_U:csvdRoleHistoryRole,_V:csvdRoleHistoryRoleChangeTime,'csvdVrfTable':csvdVrfTable,'csvdVrfEntry':csvdVrfEntry,_M:csvdVrfName,_W:csvdPrefixCount,_X:csvdLocalPrefixCount,_Y:csvdRemotePrefixCount,_Z:csvdTableConvergedFlag,'ciscoSelectiveVrfDownloadMIBConform':ciscoSelectiveVrfDownloadMIBConform,'csvdMIBCompliances':csvdMIBCompliances,'csvdMIBCompliance':csvdMIBCompliance,'csvdMIBGroups':csvdMIBGroups,_c:csvdMIBGroup,_d:csvdMIBNotificationEnableGroup,_e:csvdMIBNotificationGroup})