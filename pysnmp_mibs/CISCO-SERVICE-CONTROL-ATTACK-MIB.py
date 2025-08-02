_u='cscaMIBNotifControlGroupRev1'
_t='cscaFilterObjectGroupRev1'
_s='cscaMIBNotificationGroupRev1'
_r='cscaMIBNotifControlGroup'
_q='cscaFilterObjectGroup'
_p='cscaMIBNotificationGroup'
_o='cscaGlobalAttackFilterChange'
_n='cscaGlobalAttackNotifsEnabled'
_m='cscaInfoDownStreamLastAttackFilteringTime'
_l='cscaInfoDownStreamAttackFilteringTime'
_k='cscaInfoUpStreamLastAttackFilteringTime'
_j='cscaInfoUpStreamAttackFilteringTime'
_i='cscaTypeIPsDetected'
_h='cscaTypeIsPortSpecific'
_g='cscaTypeProtocol'
_f='cscaTypeTotalNumSeconds'
_e='cscaTypeTotalNumFlows'
_d='cscaTypeTotalNumAttacks'
_c='cscaTypeCurrentNumAttacks'
_b='attacks'
_a='CscaAttackType'
_Z='cscaTypeIndex'
_Y='read-write'
_X='cscaMIBAttackInfoObjectGroup'
_W='cscaMIBAttackTypeObjectGroup'
_V='cscaFilterChange'
_U='cscaGlobalAttackType'
_T='cscaNotifsEnabled'
_S='cscaLastDiscontinuityTimeStamp'
_R='cscaTypeOriginatedByNetworkSide'
_Q='seconds'
_P='Integer32'
_O='entPhysicalName'
_N='entPhysicalIndex'
_M='deprecated'
_L='cscaAttackedPort'
_K='cscaDestinationAddress'
_J='cscaDestinationAddressType'
_I='cscaSourceAddress'
_H='cscaSourceAddressType'
_G='cscaType'
_F='cscaFilterStatus'
_E='ENTITY-MIB'
_D='accessible-for-notify'
_C='read-only'
_B='current'
_A='CISCO-SERVICE-CONTROL-ATTACK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_E,_N,_O)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TimeInterval','TimeStamp','TruthValue')
ciscoServiceControlAttackMIB=ModuleIdentity((1,3,6,1,4,1,9,9,693))
if mibBuilder.loadTexts:ciscoServiceControlAttackMIB.setRevisions(('2013-08-16 00:00','2009-05-05 00:00'))
class CscaAttackType(TextualConvention,Integer32):status=_B;displayHint='d'
_CiscoServiceControlAttackMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoServiceControlAttackMIBNotifs=_CiscoServiceControlAttackMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,693,0))
_CiscoServiceControlAttackMIBObjects_ObjectIdentity=ObjectIdentity
ciscoServiceControlAttackMIBObjects=_CiscoServiceControlAttackMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,693,1))
_CscaFilterMIBObjects_ObjectIdentity=ObjectIdentity
cscaFilterMIBObjects=_CscaFilterMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,693,1,1))
_CscaType_Type=CscaAttackType
_CscaType_Object=MibScalar
cscaType=_CscaType_Object((1,3,6,1,4,1,9,9,693,1,1,1),_CscaType_Type())
cscaType.setMaxAccess(_D)
if mibBuilder.loadTexts:cscaType.setStatus(_B)
_CscaSourceAddressType_Type=InetAddressType
_CscaSourceAddressType_Object=MibScalar
cscaSourceAddressType=_CscaSourceAddressType_Object((1,3,6,1,4,1,9,9,693,1,1,2),_CscaSourceAddressType_Type())
cscaSourceAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cscaSourceAddressType.setStatus(_B)
_CscaSourceAddress_Type=InetAddress
_CscaSourceAddress_Object=MibScalar
cscaSourceAddress=_CscaSourceAddress_Object((1,3,6,1,4,1,9,9,693,1,1,3),_CscaSourceAddress_Type())
cscaSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cscaSourceAddress.setStatus(_B)
_CscaDestinationAddressType_Type=InetAddressType
_CscaDestinationAddressType_Object=MibScalar
cscaDestinationAddressType=_CscaDestinationAddressType_Object((1,3,6,1,4,1,9,9,693,1,1,4),_CscaDestinationAddressType_Type())
cscaDestinationAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cscaDestinationAddressType.setStatus(_B)
_CscaDestinationAddress_Type=InetAddress
_CscaDestinationAddress_Object=MibScalar
cscaDestinationAddress=_CscaDestinationAddress_Object((1,3,6,1,4,1,9,9,693,1,1,5),_CscaDestinationAddress_Type())
cscaDestinationAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cscaDestinationAddress.setStatus(_B)
_CscaAttackedPort_Type=InetPortNumber
_CscaAttackedPort_Object=MibScalar
cscaAttackedPort=_CscaAttackedPort_Object((1,3,6,1,4,1,9,9,693,1,1,6),_CscaAttackedPort_Type())
cscaAttackedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cscaAttackedPort.setStatus(_B)
class _CscaFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activated',1),('deactivated',2)))
_CscaFilterStatus_Type.__name__=_P
_CscaFilterStatus_Object=MibScalar
cscaFilterStatus=_CscaFilterStatus_Object((1,3,6,1,4,1,9,9,693,1,1,7),_CscaFilterStatus_Type())
cscaFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cscaFilterStatus.setStatus(_B)
_CscaNotifsEnabled_Type=TruthValue
_CscaNotifsEnabled_Object=MibScalar
cscaNotifsEnabled=_CscaNotifsEnabled_Object((1,3,6,1,4,1,9,9,693,1,1,8),_CscaNotifsEnabled_Type())
cscaNotifsEnabled.setMaxAccess(_Y)
if mibBuilder.loadTexts:cscaNotifsEnabled.setStatus(_B)
_CscaLastDiscontinuityTimeStamp_Type=TimeStamp
_CscaLastDiscontinuityTimeStamp_Object=MibScalar
cscaLastDiscontinuityTimeStamp=_CscaLastDiscontinuityTimeStamp_Object((1,3,6,1,4,1,9,9,693,1,1,9),_CscaLastDiscontinuityTimeStamp_Type())
cscaLastDiscontinuityTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaLastDiscontinuityTimeStamp.setStatus(_B)
class _CscaGlobalAttackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('icmpAttack',1),('udpAttack',2),('udpFragmentAttack',3),('tcpSynAttack',4),('tcpRstAttack',5),('tcpFragmentAttack',6),('tcpNonSynAttack',7)))
_CscaGlobalAttackType_Type.__name__=_P
_CscaGlobalAttackType_Object=MibScalar
cscaGlobalAttackType=_CscaGlobalAttackType_Object((1,3,6,1,4,1,9,9,693,1,1,10),_CscaGlobalAttackType_Type())
cscaGlobalAttackType.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaGlobalAttackType.setStatus(_B)
_CscaGlobalAttackNotifsEnabled_Type=TruthValue
_CscaGlobalAttackNotifsEnabled_Object=MibScalar
cscaGlobalAttackNotifsEnabled=_CscaGlobalAttackNotifsEnabled_Object((1,3,6,1,4,1,9,9,693,1,1,11),_CscaGlobalAttackNotifsEnabled_Type())
cscaGlobalAttackNotifsEnabled.setMaxAccess(_Y)
if mibBuilder.loadTexts:cscaGlobalAttackNotifsEnabled.setStatus(_B)
_CscaTypeTable_Object=MibTable
cscaTypeTable=_CscaTypeTable_Object((1,3,6,1,4,1,9,9,693,1,2))
if mibBuilder.loadTexts:cscaTypeTable.setStatus(_B)
_CscaTypeEntry_Object=MibTableRow
cscaTypeEntry=_CscaTypeEntry_Object((1,3,6,1,4,1,9,9,693,1,2,1))
cscaTypeEntry.setIndexNames((0,_E,_N),(0,_A,_Z))
if mibBuilder.loadTexts:cscaTypeEntry.setStatus(_B)
class _CscaTypeIndex_Type(CscaAttackType):subtypeSpec=CscaAttackType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CscaTypeIndex_Type.__name__=_a
_CscaTypeIndex_Object=MibTableColumn
cscaTypeIndex=_CscaTypeIndex_Object((1,3,6,1,4,1,9,9,693,1,2,1,1),_CscaTypeIndex_Type())
cscaTypeIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cscaTypeIndex.setStatus(_B)
_CscaTypeCurrentNumAttacks_Type=Gauge32
_CscaTypeCurrentNumAttacks_Object=MibTableColumn
cscaTypeCurrentNumAttacks=_CscaTypeCurrentNumAttacks_Object((1,3,6,1,4,1,9,9,693,1,2,1,2),_CscaTypeCurrentNumAttacks_Type())
cscaTypeCurrentNumAttacks.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeCurrentNumAttacks.setStatus(_B)
if mibBuilder.loadTexts:cscaTypeCurrentNumAttacks.setUnits(_b)
_CscaTypeTotalNumAttacks_Type=Counter32
_CscaTypeTotalNumAttacks_Object=MibTableColumn
cscaTypeTotalNumAttacks=_CscaTypeTotalNumAttacks_Object((1,3,6,1,4,1,9,9,693,1,2,1,3),_CscaTypeTotalNumAttacks_Type())
cscaTypeTotalNumAttacks.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeTotalNumAttacks.setStatus(_B)
if mibBuilder.loadTexts:cscaTypeTotalNumAttacks.setUnits(_b)
_CscaTypeTotalNumFlows_Type=Counter64
_CscaTypeTotalNumFlows_Object=MibTableColumn
cscaTypeTotalNumFlows=_CscaTypeTotalNumFlows_Object((1,3,6,1,4,1,9,9,693,1,2,1,4),_CscaTypeTotalNumFlows_Type())
cscaTypeTotalNumFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeTotalNumFlows.setStatus(_B)
if mibBuilder.loadTexts:cscaTypeTotalNumFlows.setUnits('IP flows')
_CscaTypeTotalNumSeconds_Type=Counter32
_CscaTypeTotalNumSeconds_Object=MibTableColumn
cscaTypeTotalNumSeconds=_CscaTypeTotalNumSeconds_Object((1,3,6,1,4,1,9,9,693,1,2,1,5),_CscaTypeTotalNumSeconds_Type())
cscaTypeTotalNumSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeTotalNumSeconds.setStatus(_B)
if mibBuilder.loadTexts:cscaTypeTotalNumSeconds.setUnits(_Q)
_CscaTypeOriginatedByNetworkSide_Type=TruthValue
_CscaTypeOriginatedByNetworkSide_Object=MibTableColumn
cscaTypeOriginatedByNetworkSide=_CscaTypeOriginatedByNetworkSide_Object((1,3,6,1,4,1,9,9,693,1,2,1,6),_CscaTypeOriginatedByNetworkSide_Type())
cscaTypeOriginatedByNetworkSide.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeOriginatedByNetworkSide.setStatus(_B)
_CscaTypeProtocol_Type=Integer32
_CscaTypeProtocol_Object=MibTableColumn
cscaTypeProtocol=_CscaTypeProtocol_Object((1,3,6,1,4,1,9,9,693,1,2,1,7),_CscaTypeProtocol_Type())
cscaTypeProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeProtocol.setStatus(_B)
_CscaTypeIsPortSpecific_Type=TruthValue
_CscaTypeIsPortSpecific_Object=MibTableColumn
cscaTypeIsPortSpecific=_CscaTypeIsPortSpecific_Object((1,3,6,1,4,1,9,9,693,1,2,1,8),_CscaTypeIsPortSpecific_Type())
cscaTypeIsPortSpecific.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeIsPortSpecific.setStatus(_B)
_CscaTypeIPsDetected_Type=Integer32
_CscaTypeIPsDetected_Object=MibTableColumn
cscaTypeIPsDetected=_CscaTypeIPsDetected_Object((1,3,6,1,4,1,9,9,693,1,2,1,9),_CscaTypeIPsDetected_Type())
cscaTypeIPsDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaTypeIPsDetected.setStatus(_B)
_CscaInfoTable_Object=MibTable
cscaInfoTable=_CscaInfoTable_Object((1,3,6,1,4,1,9,9,693,1,3))
if mibBuilder.loadTexts:cscaInfoTable.setStatus(_B)
_CscaInfoEntry_Object=MibTableRow
cscaInfoEntry=_CscaInfoEntry_Object((1,3,6,1,4,1,9,9,693,1,3,1))
cscaInfoEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:cscaInfoEntry.setStatus(_B)
_CscaInfoUpStreamAttackFilteringTime_Type=Counter32
_CscaInfoUpStreamAttackFilteringTime_Object=MibTableColumn
cscaInfoUpStreamAttackFilteringTime=_CscaInfoUpStreamAttackFilteringTime_Object((1,3,6,1,4,1,9,9,693,1,3,1,1),_CscaInfoUpStreamAttackFilteringTime_Type())
cscaInfoUpStreamAttackFilteringTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaInfoUpStreamAttackFilteringTime.setStatus(_B)
if mibBuilder.loadTexts:cscaInfoUpStreamAttackFilteringTime.setUnits(_Q)
_CscaInfoUpStreamLastAttackFilteringTime_Type=TimeInterval
_CscaInfoUpStreamLastAttackFilteringTime_Object=MibTableColumn
cscaInfoUpStreamLastAttackFilteringTime=_CscaInfoUpStreamLastAttackFilteringTime_Object((1,3,6,1,4,1,9,9,693,1,3,1,2),_CscaInfoUpStreamLastAttackFilteringTime_Type())
cscaInfoUpStreamLastAttackFilteringTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaInfoUpStreamLastAttackFilteringTime.setStatus(_B)
_CscaInfoDownStreamAttackFilteringTime_Type=Counter32
_CscaInfoDownStreamAttackFilteringTime_Object=MibTableColumn
cscaInfoDownStreamAttackFilteringTime=_CscaInfoDownStreamAttackFilteringTime_Object((1,3,6,1,4,1,9,9,693,1,3,1,3),_CscaInfoDownStreamAttackFilteringTime_Type())
cscaInfoDownStreamAttackFilteringTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaInfoDownStreamAttackFilteringTime.setStatus(_B)
if mibBuilder.loadTexts:cscaInfoDownStreamAttackFilteringTime.setUnits(_Q)
_CscaInfoDownStreamLastAttackFilteringTime_Type=TimeInterval
_CscaInfoDownStreamLastAttackFilteringTime_Object=MibTableColumn
cscaInfoDownStreamLastAttackFilteringTime=_CscaInfoDownStreamLastAttackFilteringTime_Object((1,3,6,1,4,1,9,9,693,1,3,1,4),_CscaInfoDownStreamLastAttackFilteringTime_Type())
cscaInfoDownStreamLastAttackFilteringTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cscaInfoDownStreamLastAttackFilteringTime.setStatus(_B)
_CiscoServiceControlAttackMIBConform_ObjectIdentity=ObjectIdentity
ciscoServiceControlAttackMIBConform=_CiscoServiceControlAttackMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,693,2))
_CscaMIBCompliances_ObjectIdentity=ObjectIdentity
cscaMIBCompliances=_CscaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,693,2,1))
_CscaMIBGroups_ObjectIdentity=ObjectIdentity
cscaMIBGroups=_CscaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,693,2,2))
cscaMIBAttackTypeObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,693,2,2,1))
cscaMIBAttackTypeObjectGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_R),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:cscaMIBAttackTypeObjectGroup.setStatus(_B)
cscaMIBAttackInfoObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,693,2,2,2))
cscaMIBAttackInfoObjectGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:cscaMIBAttackInfoObjectGroup.setStatus(_B)
cscaFilterObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,693,2,2,4))
cscaFilterObjectGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_F),(_A,_S)))
if mibBuilder.loadTexts:cscaFilterObjectGroup.setStatus(_M)
cscaMIBNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,693,2,2,5))
cscaMIBNotifControlGroup.setObjects((_A,_T))
if mibBuilder.loadTexts:cscaMIBNotifControlGroup.setStatus(_M)
cscaFilterObjectGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,693,2,2,7))
cscaFilterObjectGroupRev1.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_F),(_A,_S),(_A,_U)))
if mibBuilder.loadTexts:cscaFilterObjectGroupRev1.setStatus(_B)
cscaMIBNotifControlGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,693,2,2,8))
cscaMIBNotifControlGroupRev1.setObjects(*((_A,_T),(_A,_n)))
if mibBuilder.loadTexts:cscaMIBNotifControlGroupRev1.setStatus(_B)
cscaFilterChange=NotificationType((1,3,6,1,4,1,9,9,693,0,1))
cscaFilterChange.setObjects(*((_E,_O),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_F)))
if mibBuilder.loadTexts:cscaFilterChange.setStatus(_B)
cscaGlobalAttackFilterChange=NotificationType((1,3,6,1,4,1,9,9,693,0,2))
cscaGlobalAttackFilterChange.setObjects(*((_E,_O),(_A,_U),(_A,_F),(_A,_R)))
if mibBuilder.loadTexts:cscaGlobalAttackFilterChange.setStatus(_B)
cscaMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,693,2,2,3))
cscaMIBNotificationGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:cscaMIBNotificationGroup.setStatus(_M)
cscaMIBNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,693,2,2,6))
cscaMIBNotificationGroupRev1.setObjects(*((_A,_V),(_A,_o)))
if mibBuilder.loadTexts:cscaMIBNotificationGroupRev1.setStatus(_B)
cscaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,693,2,1,1))
cscaMIBCompliance.setObjects(*((_A,_W),(_A,_p),(_A,_X),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:cscaMIBCompliance.setStatus(_M)
cscaMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,693,2,1,2))
cscaMIBComplianceRev1.setObjects(*((_A,_W),(_A,_s),(_A,_X),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cscaMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_a:CscaAttackType,'ciscoServiceControlAttackMIB':ciscoServiceControlAttackMIB,'ciscoServiceControlAttackMIBNotifs':ciscoServiceControlAttackMIBNotifs,_V:cscaFilterChange,_o:cscaGlobalAttackFilterChange,'ciscoServiceControlAttackMIBObjects':ciscoServiceControlAttackMIBObjects,'cscaFilterMIBObjects':cscaFilterMIBObjects,_G:cscaType,_H:cscaSourceAddressType,_I:cscaSourceAddress,_J:cscaDestinationAddressType,_K:cscaDestinationAddress,_L:cscaAttackedPort,_F:cscaFilterStatus,_T:cscaNotifsEnabled,_S:cscaLastDiscontinuityTimeStamp,_U:cscaGlobalAttackType,_n:cscaGlobalAttackNotifsEnabled,'cscaTypeTable':cscaTypeTable,'cscaTypeEntry':cscaTypeEntry,_Z:cscaTypeIndex,_c:cscaTypeCurrentNumAttacks,_d:cscaTypeTotalNumAttacks,_e:cscaTypeTotalNumFlows,_f:cscaTypeTotalNumSeconds,_R:cscaTypeOriginatedByNetworkSide,_g:cscaTypeProtocol,_h:cscaTypeIsPortSpecific,_i:cscaTypeIPsDetected,'cscaInfoTable':cscaInfoTable,'cscaInfoEntry':cscaInfoEntry,_j:cscaInfoUpStreamAttackFilteringTime,_k:cscaInfoUpStreamLastAttackFilteringTime,_l:cscaInfoDownStreamAttackFilteringTime,_m:cscaInfoDownStreamLastAttackFilteringTime,'ciscoServiceControlAttackMIBConform':ciscoServiceControlAttackMIBConform,'cscaMIBCompliances':cscaMIBCompliances,'cscaMIBCompliance':cscaMIBCompliance,'cscaMIBComplianceRev1':cscaMIBComplianceRev1,'cscaMIBGroups':cscaMIBGroups,_W:cscaMIBAttackTypeObjectGroup,_X:cscaMIBAttackInfoObjectGroup,_p:cscaMIBNotificationGroup,_q:cscaFilterObjectGroup,_r:cscaMIBNotifControlGroup,_s:cscaMIBNotificationGroupRev1,_t:cscaFilterObjectGroupRev1,_u:cscaMIBNotifControlGroupRev1})