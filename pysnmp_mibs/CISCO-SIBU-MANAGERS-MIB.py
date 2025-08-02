_b='ciscoSibuManagersSnmpTrapManagerGroup'
_a='ciscoSibuManagersSnmpSetManagerGroup'
_Z='ciscoSibuManagersWebConsoleGroup'
_Y='ciscoSibuManagersCLIConsoleGroup'
_X='ciscoSibuManagersIpConfigGroup'
_W='cmSnmpTrapManagerRowStatus'
_V='cmSnmpTrapManagerCommunity'
_U='cmSnmpSetManagerRowStatus'
_T='cmConsoleWebHttpPort'
_S='cmConsoleWebAdminState'
_R='cmConsoleCLISilentTime'
_Q='cmConsoleCLIPasswordMaxAttempts'
_P='cmConsoleCLIInactiveTimeout'
_O='cmIpConfigDefaultGateway'
_N='cmIpConfigSubnetMask'
_M='cmIpConfigAddress'
_L='cmIpConfigMethod'
_K='cmSnmpTrapManagerAddr'
_J='not-accessible'
_I='cmSnmpSetManagerAddr'
_H='DisplayString'
_G='read-create'
_F='00000000'
_E='IpAddress'
_D='Integer32'
_C='read-write'
_B='CISCO-SIBU-MANAGERS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_E,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
ciscoSibuManagersMIB=ModuleIdentity((1,3,6,1,4,1,9,10,46))
if mibBuilder.loadTexts:ciscoSibuManagersMIB.setRevisions(('1998-10-23 00:00',))
_CiscoSibuManagersMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSibuManagersMIBObjects=_CiscoSibuManagersMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,46,1))
_CmIpConfig_ObjectIdentity=ObjectIdentity
cmIpConfig=_CmIpConfig_ObjectIdentity((1,3,6,1,4,1,9,10,46,1,1))
class _CmIpConfigMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('bootp',2)))
_CmIpConfigMethod_Type.__name__=_D
_CmIpConfigMethod_Object=MibScalar
cmIpConfigMethod=_CmIpConfigMethod_Object((1,3,6,1,4,1,9,10,46,1,1,1),_CmIpConfigMethod_Type())
cmIpConfigMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:cmIpConfigMethod.setStatus(_A)
class _CmIpConfigAddress_Type(IpAddress):defaultHexValue=_F
_CmIpConfigAddress_Type.__name__=_E
_CmIpConfigAddress_Object=MibScalar
cmIpConfigAddress=_CmIpConfigAddress_Object((1,3,6,1,4,1,9,10,46,1,1,2),_CmIpConfigAddress_Type())
cmIpConfigAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmIpConfigAddress.setStatus(_A)
class _CmIpConfigSubnetMask_Type(IpAddress):defaultHexValue=_F
_CmIpConfigSubnetMask_Type.__name__=_E
_CmIpConfigSubnetMask_Object=MibScalar
cmIpConfigSubnetMask=_CmIpConfigSubnetMask_Object((1,3,6,1,4,1,9,10,46,1,1,3),_CmIpConfigSubnetMask_Type())
cmIpConfigSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmIpConfigSubnetMask.setStatus(_A)
class _CmIpConfigDefaultGateway_Type(IpAddress):defaultHexValue=_F
_CmIpConfigDefaultGateway_Type.__name__=_E
_CmIpConfigDefaultGateway_Object=MibScalar
cmIpConfigDefaultGateway=_CmIpConfigDefaultGateway_Object((1,3,6,1,4,1,9,10,46,1,1,4),_CmIpConfigDefaultGateway_Type())
cmIpConfigDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:cmIpConfigDefaultGateway.setStatus(_A)
_CmConsoleConfig_ObjectIdentity=ObjectIdentity
cmConsoleConfig=_CmConsoleConfig_ObjectIdentity((1,3,6,1,4,1,9,10,46,1,2))
class _CmConsoleCLIInactiveTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,65500))
_CmConsoleCLIInactiveTimeout_Type.__name__=_D
_CmConsoleCLIInactiveTimeout_Object=MibScalar
cmConsoleCLIInactiveTimeout=_CmConsoleCLIInactiveTimeout_Object((1,3,6,1,4,1,9,10,46,1,2,1),_CmConsoleCLIInactiveTimeout_Type())
cmConsoleCLIInactiveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cmConsoleCLIInactiveTimeout.setStatus(_A)
if mibBuilder.loadTexts:cmConsoleCLIInactiveTimeout.setUnits('seconds')
class _CmConsoleCLIPasswordMaxAttempts_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_CmConsoleCLIPasswordMaxAttempts_Type.__name__=_D
_CmConsoleCLIPasswordMaxAttempts_Object=MibScalar
cmConsoleCLIPasswordMaxAttempts=_CmConsoleCLIPasswordMaxAttempts_Object((1,3,6,1,4,1,9,10,46,1,2,2),_CmConsoleCLIPasswordMaxAttempts_Type())
cmConsoleCLIPasswordMaxAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmConsoleCLIPasswordMaxAttempts.setStatus(_A)
if mibBuilder.loadTexts:cmConsoleCLIPasswordMaxAttempts.setUnits('attempts')
class _CmConsoleCLISilentTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_CmConsoleCLISilentTime_Type.__name__=_D
_CmConsoleCLISilentTime_Object=MibScalar
cmConsoleCLISilentTime=_CmConsoleCLISilentTime_Object((1,3,6,1,4,1,9,10,46,1,2,3),_CmConsoleCLISilentTime_Type())
cmConsoleCLISilentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmConsoleCLISilentTime.setStatus(_A)
class _CmConsoleWebAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CmConsoleWebAdminState_Type.__name__=_D
_CmConsoleWebAdminState_Object=MibScalar
cmConsoleWebAdminState=_CmConsoleWebAdminState_Object((1,3,6,1,4,1,9,10,46,1,2,4),_CmConsoleWebAdminState_Type())
cmConsoleWebAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmConsoleWebAdminState.setStatus(_A)
class _CmConsoleWebHttpPort_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CmConsoleWebHttpPort_Type.__name__=_D
_CmConsoleWebHttpPort_Object=MibScalar
cmConsoleWebHttpPort=_CmConsoleWebHttpPort_Object((1,3,6,1,4,1,9,10,46,1,2,5),_CmConsoleWebHttpPort_Type())
cmConsoleWebHttpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmConsoleWebHttpPort.setStatus(_A)
_CmSnmpSetManager_ObjectIdentity=ObjectIdentity
cmSnmpSetManager=_CmSnmpSetManager_ObjectIdentity((1,3,6,1,4,1,9,10,46,1,3))
_CmSnmpSetManagerTable_Object=MibTable
cmSnmpSetManagerTable=_CmSnmpSetManagerTable_Object((1,3,6,1,4,1,9,10,46,1,3,1))
if mibBuilder.loadTexts:cmSnmpSetManagerTable.setStatus(_A)
_CmSnmpSetManagerEntry_Object=MibTableRow
cmSnmpSetManagerEntry=_CmSnmpSetManagerEntry_Object((1,3,6,1,4,1,9,10,46,1,3,1,1))
cmSnmpSetManagerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cmSnmpSetManagerEntry.setStatus(_A)
_CmSnmpSetManagerAddr_Type=IpAddress
_CmSnmpSetManagerAddr_Object=MibTableColumn
cmSnmpSetManagerAddr=_CmSnmpSetManagerAddr_Object((1,3,6,1,4,1,9,10,46,1,3,1,1,1),_CmSnmpSetManagerAddr_Type())
cmSnmpSetManagerAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:cmSnmpSetManagerAddr.setStatus(_A)
_CmSnmpSetManagerRowStatus_Type=RowStatus
_CmSnmpSetManagerRowStatus_Object=MibTableColumn
cmSnmpSetManagerRowStatus=_CmSnmpSetManagerRowStatus_Object((1,3,6,1,4,1,9,10,46,1,3,1,1,2),_CmSnmpSetManagerRowStatus_Type())
cmSnmpSetManagerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmSnmpSetManagerRowStatus.setStatus(_A)
_CmSnmpTrapManager_ObjectIdentity=ObjectIdentity
cmSnmpTrapManager=_CmSnmpTrapManager_ObjectIdentity((1,3,6,1,4,1,9,10,46,1,4))
_CmSnmpTrapManagerTable_Object=MibTable
cmSnmpTrapManagerTable=_CmSnmpTrapManagerTable_Object((1,3,6,1,4,1,9,10,46,1,4,1))
if mibBuilder.loadTexts:cmSnmpTrapManagerTable.setStatus(_A)
_CmSnmpTrapManagerEntry_Object=MibTableRow
cmSnmpTrapManagerEntry=_CmSnmpTrapManagerEntry_Object((1,3,6,1,4,1,9,10,46,1,4,1,1))
cmSnmpTrapManagerEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cmSnmpTrapManagerEntry.setStatus(_A)
_CmSnmpTrapManagerAddr_Type=IpAddress
_CmSnmpTrapManagerAddr_Object=MibTableColumn
cmSnmpTrapManagerAddr=_CmSnmpTrapManagerAddr_Object((1,3,6,1,4,1,9,10,46,1,4,1,1,1),_CmSnmpTrapManagerAddr_Type())
cmSnmpTrapManagerAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:cmSnmpTrapManagerAddr.setStatus(_A)
class _CmSnmpTrapManagerCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmSnmpTrapManagerCommunity_Type.__name__=_H
_CmSnmpTrapManagerCommunity_Object=MibTableColumn
cmSnmpTrapManagerCommunity=_CmSnmpTrapManagerCommunity_Object((1,3,6,1,4,1,9,10,46,1,4,1,1,2),_CmSnmpTrapManagerCommunity_Type())
cmSnmpTrapManagerCommunity.setMaxAccess(_G)
if mibBuilder.loadTexts:cmSnmpTrapManagerCommunity.setStatus(_A)
_CmSnmpTrapManagerRowStatus_Type=RowStatus
_CmSnmpTrapManagerRowStatus_Object=MibTableColumn
cmSnmpTrapManagerRowStatus=_CmSnmpTrapManagerRowStatus_Object((1,3,6,1,4,1,9,10,46,1,4,1,1,3),_CmSnmpTrapManagerRowStatus_Type())
cmSnmpTrapManagerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmSnmpTrapManagerRowStatus.setStatus(_A)
_CiscoSibuManagersNotifications_ObjectIdentity=ObjectIdentity
ciscoSibuManagersNotifications=_CiscoSibuManagersNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,46,2))
_CiscoSibuManagersNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoSibuManagersNotificationsPrefix=_CiscoSibuManagersNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,46,2,0))
_CiscoSibuManagersMIBComformance_ObjectIdentity=ObjectIdentity
ciscoSibuManagersMIBComformance=_CiscoSibuManagersMIBComformance_ObjectIdentity((1,3,6,1,4,1,9,10,46,3))
_CiscoSibuManagersMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSibuManagersMIBCompliances=_CiscoSibuManagersMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,46,3,1))
_CiscoSibuManagersMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSibuManagersMIBGroups=_CiscoSibuManagersMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,46,3,2))
ciscoSibuManagersIpConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,46,3,2,1))
ciscoSibuManagersIpConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoSibuManagersIpConfigGroup.setStatus(_A)
ciscoSibuManagersCLIConsoleGroup=ObjectGroup((1,3,6,1,4,1,9,10,46,3,2,2))
ciscoSibuManagersCLIConsoleGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoSibuManagersCLIConsoleGroup.setStatus(_A)
ciscoSibuManagersWebConsoleGroup=ObjectGroup((1,3,6,1,4,1,9,10,46,3,2,3))
ciscoSibuManagersWebConsoleGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoSibuManagersWebConsoleGroup.setStatus(_A)
ciscoSibuManagersSnmpSetManagerGroup=ObjectGroup((1,3,6,1,4,1,9,10,46,3,2,4))
ciscoSibuManagersSnmpSetManagerGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:ciscoSibuManagersSnmpSetManagerGroup.setStatus(_A)
ciscoSibuManagersSnmpTrapManagerGroup=ObjectGroup((1,3,6,1,4,1,9,10,46,3,2,5))
ciscoSibuManagersSnmpTrapManagerGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoSibuManagersSnmpTrapManagerGroup.setStatus(_A)
ciscoSibuManagersConsoleLogonIntruder=NotificationType((1,3,6,1,4,1,9,10,46,2,0,1))
if mibBuilder.loadTexts:ciscoSibuManagersConsoleLogonIntruder.setStatus(_A)
ciscoSibuManagersCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,46,3,1,1))
ciscoSibuManagersCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ciscoSibuManagersCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSibuManagersMIB':ciscoSibuManagersMIB,'ciscoSibuManagersMIBObjects':ciscoSibuManagersMIBObjects,'cmIpConfig':cmIpConfig,_L:cmIpConfigMethod,_M:cmIpConfigAddress,_N:cmIpConfigSubnetMask,_O:cmIpConfigDefaultGateway,'cmConsoleConfig':cmConsoleConfig,_P:cmConsoleCLIInactiveTimeout,_Q:cmConsoleCLIPasswordMaxAttempts,_R:cmConsoleCLISilentTime,_S:cmConsoleWebAdminState,_T:cmConsoleWebHttpPort,'cmSnmpSetManager':cmSnmpSetManager,'cmSnmpSetManagerTable':cmSnmpSetManagerTable,'cmSnmpSetManagerEntry':cmSnmpSetManagerEntry,_I:cmSnmpSetManagerAddr,_U:cmSnmpSetManagerRowStatus,'cmSnmpTrapManager':cmSnmpTrapManager,'cmSnmpTrapManagerTable':cmSnmpTrapManagerTable,'cmSnmpTrapManagerEntry':cmSnmpTrapManagerEntry,_K:cmSnmpTrapManagerAddr,_V:cmSnmpTrapManagerCommunity,_W:cmSnmpTrapManagerRowStatus,'ciscoSibuManagersNotifications':ciscoSibuManagersNotifications,'ciscoSibuManagersNotificationsPrefix':ciscoSibuManagersNotificationsPrefix,'ciscoSibuManagersConsoleLogonIntruder':ciscoSibuManagersConsoleLogonIntruder,'ciscoSibuManagersMIBComformance':ciscoSibuManagersMIBComformance,'ciscoSibuManagersMIBCompliances':ciscoSibuManagersMIBCompliances,'ciscoSibuManagersCompliance':ciscoSibuManagersCompliance,'ciscoSibuManagersMIBGroups':ciscoSibuManagersMIBGroups,_X:ciscoSibuManagersIpConfigGroup,_Y:ciscoSibuManagersCLIConsoleGroup,_Z:ciscoSibuManagersWebConsoleGroup,_a:ciscoSibuManagersSnmpSetManagerGroup,_b:ciscoSibuManagersSnmpTrapManagerGroup})