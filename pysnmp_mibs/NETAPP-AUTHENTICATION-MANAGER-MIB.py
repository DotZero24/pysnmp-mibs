_Z='agentAuthMgrClientAuthstatus'
_Y='agentAuthMgrClientAuthMethod'
_X='agentAuthMgrInterface'
_W='agentAuthMgrPortMethodIndex'
_V='agentAuthMgrAuthHistoryResultIfIndex'
_U='agentAuthMgrAuthHistoryResultIndex'
_T='agentAuthMgrAuthHistoryResultIfaceIndex'
_S='agentAuthMgrTimerIfIndex'
_R='read-create'
_Q='Unsigned32'
_P='agentAuthMgrPortIfaceIndex'
_O='agentAuthMgrClientMacAddress'
_N='methodIndex'
_M='agentAuthMgrIfIndex'
_L='disable'
_K='enable'
_J='undefined'
_I='not-accessible'
_H='read-write'
_G='captivePortal'
_F='mab'
_E='dot1x'
_D='Integer32'
_C='read-only'
_B='NETAPP-AUTHENTICATION-MANAGER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
fastPath,=mibBuilder.importSymbols('NETAPP-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
fastPathAuthMgr=ModuleIdentity((1,3,6,1,4,1,789,4413,1,1,61))
if mibBuilder.loadTexts:fastPathAuthMgr.setRevisions(('2012-12-28 00:00',))
_FastpathAuthMgrTraps_ObjectIdentity=ObjectIdentity
fastpathAuthMgrTraps=_FastpathAuthMgrTraps_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,0))
_AgentAuthMgrGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrGlobalConfigGroup=_AgentAuthMgrGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,1))
class _AgentAuthMgrAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AgentAuthMgrAdminMode_Type.__name__=_D
_AgentAuthMgrAdminMode_Object=MibScalar
agentAuthMgrAdminMode=_AgentAuthMgrAdminMode_Object((1,3,6,1,4,1,789,4413,1,1,61,1,1),_AgentAuthMgrAdminMode_Type())
agentAuthMgrAdminMode.setMaxAccess(_H)
if mibBuilder.loadTexts:agentAuthMgrAdminMode.setStatus(_A)
_AgentAuthMgrInterfaceConfigGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrInterfaceConfigGroup=_AgentAuthMgrInterfaceConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,2))
_AgentAuthMgrInterfaceConfigMethodTable_Object=MibTable
agentAuthMgrInterfaceConfigMethodTable=_AgentAuthMgrInterfaceConfigMethodTable_Object((1,3,6,1,4,1,789,4413,1,1,61,2,1))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigMethodTable.setStatus(_A)
_AgentAuthMgrInterfaceConfigMethodEntry_Object=MibTableRow
agentAuthMgrInterfaceConfigMethodEntry=_AgentAuthMgrInterfaceConfigMethodEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,2,1,1))
agentAuthMgrInterfaceConfigMethodEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigMethodEntry.setStatus(_A)
_AgentAuthMgrIfIndex_Type=InterfaceIndex
_AgentAuthMgrIfIndex_Object=MibTableColumn
agentAuthMgrIfIndex=_AgentAuthMgrIfIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,2,1,1,1),_AgentAuthMgrIfIndex_Type())
agentAuthMgrIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentAuthMgrIfIndex.setStatus(_A)
_MethodIndex_Type=Unsigned32
_MethodIndex_Object=MibTableColumn
methodIndex=_MethodIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,2,1,1,2),_MethodIndex_Type())
methodIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:methodIndex.setStatus(_A)
class _AgentAuthMgrMethodOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3)))
_AgentAuthMgrMethodOrder_Type.__name__=_D
_AgentAuthMgrMethodOrder_Object=MibTableColumn
agentAuthMgrMethodOrder=_AgentAuthMgrMethodOrder_Object((1,3,6,1,4,1,789,4413,1,1,61,2,1,1,3),_AgentAuthMgrMethodOrder_Type())
agentAuthMgrMethodOrder.setMaxAccess(_R)
if mibBuilder.loadTexts:agentAuthMgrMethodOrder.setStatus(_A)
class _AgentAuthMgrMethodPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3)))
_AgentAuthMgrMethodPriority_Type.__name__=_D
_AgentAuthMgrMethodPriority_Object=MibTableColumn
agentAuthMgrMethodPriority=_AgentAuthMgrMethodPriority_Object((1,3,6,1,4,1,789,4413,1,1,61,2,1,1,4),_AgentAuthMgrMethodPriority_Type())
agentAuthMgrMethodPriority.setMaxAccess(_R)
if mibBuilder.loadTexts:agentAuthMgrMethodPriority.setStatus(_A)
_AgentAuthMgrInterfaceConfigTimerTable_Object=MibTable
agentAuthMgrInterfaceConfigTimerTable=_AgentAuthMgrInterfaceConfigTimerTable_Object((1,3,6,1,4,1,789,4413,1,1,61,2,2))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigTimerTable.setStatus(_A)
_AgentAuthMgrInterfaceConfigTimerEntry_Object=MibTableRow
agentAuthMgrInterfaceConfigTimerEntry=_AgentAuthMgrInterfaceConfigTimerEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,2,2,1))
agentAuthMgrInterfaceConfigTimerEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigTimerEntry.setStatus(_A)
_AgentAuthMgrTimerIfIndex_Type=InterfaceIndex
_AgentAuthMgrTimerIfIndex_Object=MibTableColumn
agentAuthMgrTimerIfIndex=_AgentAuthMgrTimerIfIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,2,2,1,1),_AgentAuthMgrTimerIfIndex_Type())
agentAuthMgrTimerIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentAuthMgrTimerIfIndex.setStatus(_A)
class _AgentAuthMgrRestart_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentAuthMgrRestart_Type.__name__=_Q
_AgentAuthMgrRestart_Object=MibTableColumn
agentAuthMgrRestart=_AgentAuthMgrRestart_Object((1,3,6,1,4,1,789,4413,1,1,61,2,2,1,2),_AgentAuthMgrRestart_Type())
agentAuthMgrRestart.setMaxAccess(_H)
if mibBuilder.loadTexts:agentAuthMgrRestart.setStatus(_A)
_AgentAuthMgrInterfaceStatusGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrInterfaceStatusGroup=_AgentAuthMgrInterfaceStatusGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,3))
_AgentAuthMgrInterfaceStatusTable_Object=MibTable
agentAuthMgrInterfaceStatusTable=_AgentAuthMgrInterfaceStatusTable_Object((1,3,6,1,4,1,789,4413,1,1,61,3,1))
if mibBuilder.loadTexts:agentAuthMgrInterfaceStatusTable.setStatus(_A)
_AgentAuthMgrInterfaceStatusEntry_Object=MibTableRow
agentAuthMgrInterfaceStatusEntry=_AgentAuthMgrInterfaceStatusEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,3,1,1))
agentAuthMgrInterfaceStatusEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:agentAuthMgrInterfaceStatusEntry.setStatus(_A)
class _AgentAuthMgrStatusMethodOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3)))
_AgentAuthMgrStatusMethodOrder_Type.__name__=_D
_AgentAuthMgrStatusMethodOrder_Object=MibTableColumn
agentAuthMgrStatusMethodOrder=_AgentAuthMgrStatusMethodOrder_Object((1,3,6,1,4,1,789,4413,1,1,61,3,1,1,1),_AgentAuthMgrStatusMethodOrder_Type())
agentAuthMgrStatusMethodOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrStatusMethodOrder.setStatus(_A)
class _AgentAuthMgrStatusMethodPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3)))
_AgentAuthMgrStatusMethodPriority_Type.__name__=_D
_AgentAuthMgrStatusMethodPriority_Object=MibTableColumn
agentAuthMgrStatusMethodPriority=_AgentAuthMgrStatusMethodPriority_Object((1,3,6,1,4,1,789,4413,1,1,61,3,1,1,2),_AgentAuthMgrStatusMethodPriority_Type())
agentAuthMgrStatusMethodPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrStatusMethodPriority.setStatus(_A)
_AgentAuthMgrClientStatusGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrClientStatusGroup=_AgentAuthMgrClientStatusGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,4))
_AgentAuthMgrClientStatusTable_Object=MibTable
agentAuthMgrClientStatusTable=_AgentAuthMgrClientStatusTable_Object((1,3,6,1,4,1,789,4413,1,1,61,4,1))
if mibBuilder.loadTexts:agentAuthMgrClientStatusTable.setStatus(_A)
_AgentAuthMgrClientStatusEntry_Object=MibTableRow
agentAuthMgrClientStatusEntry=_AgentAuthMgrClientStatusEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,4,1,1))
agentAuthMgrClientStatusEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:agentAuthMgrClientStatusEntry.setStatus(_A)
_AgentAuthMgrClientMacAddress_Type=MacAddress
_AgentAuthMgrClientMacAddress_Object=MibTableColumn
agentAuthMgrClientMacAddress=_AgentAuthMgrClientMacAddress_Object((1,3,6,1,4,1,789,4413,1,1,61,4,1,1,1),_AgentAuthMgrClientMacAddress_Type())
agentAuthMgrClientMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrClientMacAddress.setStatus(_A)
_AgentAuthMgrLogicalPort_Type=Unsigned32
_AgentAuthMgrLogicalPort_Object=MibTableColumn
agentAuthMgrLogicalPort=_AgentAuthMgrLogicalPort_Object((1,3,6,1,4,1,789,4413,1,1,61,4,1,1,2),_AgentAuthMgrLogicalPort_Type())
agentAuthMgrLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrLogicalPort.setStatus(_A)
_AgentAuthMgrInterface_Type=Unsigned32
_AgentAuthMgrInterface_Object=MibTableColumn
agentAuthMgrInterface=_AgentAuthMgrInterface_Object((1,3,6,1,4,1,789,4413,1,1,61,4,1,1,3),_AgentAuthMgrInterface_Type())
agentAuthMgrInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrInterface.setStatus(_A)
class _AgentAuthMgrClientAuthstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2)))
_AgentAuthMgrClientAuthstatus_Type.__name__=_D
_AgentAuthMgrClientAuthstatus_Object=MibTableColumn
agentAuthMgrClientAuthstatus=_AgentAuthMgrClientAuthstatus_Object((1,3,6,1,4,1,789,4413,1,1,61,4,1,1,4),_AgentAuthMgrClientAuthstatus_Type())
agentAuthMgrClientAuthstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrClientAuthstatus.setStatus(_A)
class _AgentAuthMgrClientAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3)))
_AgentAuthMgrClientAuthMethod_Type.__name__=_D
_AgentAuthMgrClientAuthMethod_Object=MibTableColumn
agentAuthMgrClientAuthMethod=_AgentAuthMgrClientAuthMethod_Object((1,3,6,1,4,1,789,4413,1,1,61,4,1,1,5),_AgentAuthMgrClientAuthMethod_Type())
agentAuthMgrClientAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrClientAuthMethod.setStatus(_A)
_AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrAuthHistoryResultsGroup=_AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,5))
_AgentAuthMgrPortAuthHistoryResultTable_Object=MibTable
agentAuthMgrPortAuthHistoryResultTable=_AgentAuthMgrPortAuthHistoryResultTable_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultTable.setStatus(_A)
_AgentAuthMgrPortAuthHistoryResultEntry_Object=MibTableRow
agentAuthMgrPortAuthHistoryResultEntry=_AgentAuthMgrPortAuthHistoryResultEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1,1))
agentAuthMgrPortAuthHistoryResultEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultEntry.setStatus(_A)
_AgentAuthMgrAuthHistoryResultIfaceIndex_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultIfaceIndex_Object=MibTableColumn
agentAuthMgrAuthHistoryResultIfaceIndex=_AgentAuthMgrAuthHistoryResultIfaceIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1,1,1),_AgentAuthMgrAuthHistoryResultIfaceIndex_Type())
agentAuthMgrAuthHistoryResultIfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultIfaceIndex.setStatus(_A)
_AgentAuthMgrAuthHistoryResultIndex_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultIndex_Object=MibTableColumn
agentAuthMgrAuthHistoryResultIndex=_AgentAuthMgrAuthHistoryResultIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1,1,2),_AgentAuthMgrAuthHistoryResultIndex_Type())
agentAuthMgrAuthHistoryResultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultIndex.setStatus(_A)
_AgentAuthMgrAuthHistoryResultTimeStamp_Type=DateAndTime
_AgentAuthMgrAuthHistoryResultTimeStamp_Object=MibTableColumn
agentAuthMgrAuthHistoryResultTimeStamp=_AgentAuthMgrAuthHistoryResultTimeStamp_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1,1,3),_AgentAuthMgrAuthHistoryResultTimeStamp_Type())
agentAuthMgrAuthHistoryResultTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultTimeStamp.setStatus(_A)
_AgentAuthMgrAuthHistoryResultMacAddress_Type=MacAddress
_AgentAuthMgrAuthHistoryResultMacAddress_Object=MibTableColumn
agentAuthMgrAuthHistoryResultMacAddress=_AgentAuthMgrAuthHistoryResultMacAddress_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1,1,4),_AgentAuthMgrAuthHistoryResultMacAddress_Type())
agentAuthMgrAuthHistoryResultMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultMacAddress.setStatus(_A)
_AgentAuthMgrAuthHistoryResultAuthMethod_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultAuthMethod_Object=MibTableColumn
agentAuthMgrAuthHistoryResultAuthMethod=_AgentAuthMgrAuthHistoryResultAuthMethod_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1,1,5),_AgentAuthMgrAuthHistoryResultAuthMethod_Type())
agentAuthMgrAuthHistoryResultAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultAuthMethod.setStatus(_A)
class _AgentAuthMgrAuthHistoryResultAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failure',2)))
_AgentAuthMgrAuthHistoryResultAuthStatus_Type.__name__=_D
_AgentAuthMgrAuthHistoryResultAuthStatus_Object=MibTableColumn
agentAuthMgrAuthHistoryResultAuthStatus=_AgentAuthMgrAuthHistoryResultAuthStatus_Object((1,3,6,1,4,1,789,4413,1,1,61,5,1,1,6),_AgentAuthMgrAuthHistoryResultAuthStatus_Type())
agentAuthMgrAuthHistoryResultAuthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultAuthStatus.setStatus(_A)
_AgentAuthMgrPortAuthHistoryResultClearTable_Object=MibTable
agentAuthMgrPortAuthHistoryResultClearTable=_AgentAuthMgrPortAuthHistoryResultClearTable_Object((1,3,6,1,4,1,789,4413,1,1,61,5,3))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultClearTable.setStatus(_A)
_AgentAuthMgrPortAuthHistoryResultClearEntry_Object=MibTableRow
agentAuthMgrPortAuthHistoryResultClearEntry=_AgentAuthMgrPortAuthHistoryResultClearEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,5,3,1))
agentAuthMgrPortAuthHistoryResultClearEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultClearEntry.setStatus(_A)
_AgentAuthMgrAuthHistoryResultIfIndex_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultIfIndex_Object=MibTableColumn
agentAuthMgrAuthHistoryResultIfIndex=_AgentAuthMgrAuthHistoryResultIfIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,5,3,1,1),_AgentAuthMgrAuthHistoryResultIfIndex_Type())
agentAuthMgrAuthHistoryResultIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultIfIndex.setStatus(_A)
class _AgentAuthMgrPortAuthHistoryResultsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AgentAuthMgrPortAuthHistoryResultsClear_Type.__name__=_D
_AgentAuthMgrPortAuthHistoryResultsClear_Object=MibTableColumn
agentAuthMgrPortAuthHistoryResultsClear=_AgentAuthMgrPortAuthHistoryResultsClear_Object((1,3,6,1,4,1,789,4413,1,1,61,5,3,1,2),_AgentAuthMgrPortAuthHistoryResultsClear_Type())
agentAuthMgrPortAuthHistoryResultsClear.setMaxAccess(_H)
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultsClear.setStatus(_A)
_AgentAuthMgrAuthStatsGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrAuthStatsGroup=_AgentAuthMgrAuthStatsGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,6))
_AgentAuthMgrPortStatsTable_Object=MibTable
agentAuthMgrPortStatsTable=_AgentAuthMgrPortStatsTable_Object((1,3,6,1,4,1,789,4413,1,1,61,6,1))
if mibBuilder.loadTexts:agentAuthMgrPortStatsTable.setStatus(_A)
_AgentAuthMgrPortStatsEntry_Object=MibTableRow
agentAuthMgrPortStatsEntry=_AgentAuthMgrPortStatsEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,6,1,1))
agentAuthMgrPortStatsEntry.setIndexNames((0,_B,_P),(0,_B,_W))
if mibBuilder.loadTexts:agentAuthMgrPortStatsEntry.setStatus(_A)
_AgentAuthMgrPortIfaceIndex_Type=Unsigned32
_AgentAuthMgrPortIfaceIndex_Object=MibTableColumn
agentAuthMgrPortIfaceIndex=_AgentAuthMgrPortIfaceIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,6,1,1,1),_AgentAuthMgrPortIfaceIndex_Type())
agentAuthMgrPortIfaceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentAuthMgrPortIfaceIndex.setStatus(_A)
class _AgentAuthMgrPortMethodIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AgentAuthMgrPortMethodIndex_Type.__name__=_D
_AgentAuthMgrPortMethodIndex_Object=MibTableColumn
agentAuthMgrPortMethodIndex=_AgentAuthMgrPortMethodIndex_Object((1,3,6,1,4,1,789,4413,1,1,61,6,1,1,2),_AgentAuthMgrPortMethodIndex_Type())
agentAuthMgrPortMethodIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentAuthMgrPortMethodIndex.setStatus(_A)
_AgentAuthMgrPortStatsAttempts_Type=Unsigned32
_AgentAuthMgrPortStatsAttempts_Object=MibTableColumn
agentAuthMgrPortStatsAttempts=_AgentAuthMgrPortStatsAttempts_Object((1,3,6,1,4,1,789,4413,1,1,61,6,1,1,3),_AgentAuthMgrPortStatsAttempts_Type())
agentAuthMgrPortStatsAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrPortStatsAttempts.setStatus(_A)
_AgentAuthMgrPortStatsFailedAttempts_Type=Unsigned32
_AgentAuthMgrPortStatsFailedAttempts_Object=MibTableColumn
agentAuthMgrPortStatsFailedAttempts=_AgentAuthMgrPortStatsFailedAttempts_Object((1,3,6,1,4,1,789,4413,1,1,61,6,1,1,4),_AgentAuthMgrPortStatsFailedAttempts_Type())
agentAuthMgrPortStatsFailedAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:agentAuthMgrPortStatsFailedAttempts.setStatus(_A)
_AgentAuthMgrPortStatsClearTable_Object=MibTable
agentAuthMgrPortStatsClearTable=_AgentAuthMgrPortStatsClearTable_Object((1,3,6,1,4,1,789,4413,1,1,61,6,2))
if mibBuilder.loadTexts:agentAuthMgrPortStatsClearTable.setStatus(_A)
_AgentAuthMgrPortStatsClearEntry_Object=MibTableRow
agentAuthMgrPortStatsClearEntry=_AgentAuthMgrPortStatsClearEntry_Object((1,3,6,1,4,1,789,4413,1,1,61,6,2,1))
agentAuthMgrPortStatsClearEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:agentAuthMgrPortStatsClearEntry.setStatus(_A)
class _AgentAuthMgrPortStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AgentAuthMgrPortStatsClear_Type.__name__=_D
_AgentAuthMgrPortStatsClear_Object=MibTableColumn
agentAuthMgrPortStatsClear=_AgentAuthMgrPortStatsClear_Object((1,3,6,1,4,1,789,4413,1,1,61,6,2,1,2),_AgentAuthMgrPortStatsClear_Type())
agentAuthMgrPortStatsClear.setMaxAccess(_H)
if mibBuilder.loadTexts:agentAuthMgrPortStatsClear.setStatus(_A)
_AgentAuthMgrTrapsConfigGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrTrapsConfigGroup=_AgentAuthMgrTrapsConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,61,7))
class _AuthMgrTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AuthMgrTrapMode_Type.__name__=_D
_AuthMgrTrapMode_Object=MibScalar
authMgrTrapMode=_AuthMgrTrapMode_Object((1,3,6,1,4,1,789,4413,1,1,61,7,1),_AuthMgrTrapMode_Type())
authMgrTrapMode.setMaxAccess(_H)
if mibBuilder.loadTexts:authMgrTrapMode.setStatus(_A)
agentAuthMgrClientAuthStatusTrap=NotificationType((1,3,6,1,4,1,789,4413,1,1,61,0,1))
agentAuthMgrClientAuthStatusTrap.setObjects(*((_B,_X),(_B,_O),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:agentAuthMgrClientAuthStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fastPathAuthMgr':fastPathAuthMgr,'fastpathAuthMgrTraps':fastpathAuthMgrTraps,'agentAuthMgrClientAuthStatusTrap':agentAuthMgrClientAuthStatusTrap,'agentAuthMgrGlobalConfigGroup':agentAuthMgrGlobalConfigGroup,'agentAuthMgrAdminMode':agentAuthMgrAdminMode,'agentAuthMgrInterfaceConfigGroup':agentAuthMgrInterfaceConfigGroup,'agentAuthMgrInterfaceConfigMethodTable':agentAuthMgrInterfaceConfigMethodTable,'agentAuthMgrInterfaceConfigMethodEntry':agentAuthMgrInterfaceConfigMethodEntry,_M:agentAuthMgrIfIndex,_N:methodIndex,'agentAuthMgrMethodOrder':agentAuthMgrMethodOrder,'agentAuthMgrMethodPriority':agentAuthMgrMethodPriority,'agentAuthMgrInterfaceConfigTimerTable':agentAuthMgrInterfaceConfigTimerTable,'agentAuthMgrInterfaceConfigTimerEntry':agentAuthMgrInterfaceConfigTimerEntry,_S:agentAuthMgrTimerIfIndex,'agentAuthMgrRestart':agentAuthMgrRestart,'agentAuthMgrInterfaceStatusGroup':agentAuthMgrInterfaceStatusGroup,'agentAuthMgrInterfaceStatusTable':agentAuthMgrInterfaceStatusTable,'agentAuthMgrInterfaceStatusEntry':agentAuthMgrInterfaceStatusEntry,'agentAuthMgrStatusMethodOrder':agentAuthMgrStatusMethodOrder,'agentAuthMgrStatusMethodPriority':agentAuthMgrStatusMethodPriority,'agentAuthMgrClientStatusGroup':agentAuthMgrClientStatusGroup,'agentAuthMgrClientStatusTable':agentAuthMgrClientStatusTable,'agentAuthMgrClientStatusEntry':agentAuthMgrClientStatusEntry,_O:agentAuthMgrClientMacAddress,'agentAuthMgrLogicalPort':agentAuthMgrLogicalPort,_X:agentAuthMgrInterface,_Z:agentAuthMgrClientAuthstatus,_Y:agentAuthMgrClientAuthMethod,'agentAuthMgrAuthHistoryResultsGroup':agentAuthMgrAuthHistoryResultsGroup,'agentAuthMgrPortAuthHistoryResultTable':agentAuthMgrPortAuthHistoryResultTable,'agentAuthMgrPortAuthHistoryResultEntry':agentAuthMgrPortAuthHistoryResultEntry,_T:agentAuthMgrAuthHistoryResultIfaceIndex,_U:agentAuthMgrAuthHistoryResultIndex,'agentAuthMgrAuthHistoryResultTimeStamp':agentAuthMgrAuthHistoryResultTimeStamp,'agentAuthMgrAuthHistoryResultMacAddress':agentAuthMgrAuthHistoryResultMacAddress,'agentAuthMgrAuthHistoryResultAuthMethod':agentAuthMgrAuthHistoryResultAuthMethod,'agentAuthMgrAuthHistoryResultAuthStatus':agentAuthMgrAuthHistoryResultAuthStatus,'agentAuthMgrPortAuthHistoryResultClearTable':agentAuthMgrPortAuthHistoryResultClearTable,'agentAuthMgrPortAuthHistoryResultClearEntry':agentAuthMgrPortAuthHistoryResultClearEntry,_V:agentAuthMgrAuthHistoryResultIfIndex,'agentAuthMgrPortAuthHistoryResultsClear':agentAuthMgrPortAuthHistoryResultsClear,'agentAuthMgrAuthStatsGroup':agentAuthMgrAuthStatsGroup,'agentAuthMgrPortStatsTable':agentAuthMgrPortStatsTable,'agentAuthMgrPortStatsEntry':agentAuthMgrPortStatsEntry,_P:agentAuthMgrPortIfaceIndex,_W:agentAuthMgrPortMethodIndex,'agentAuthMgrPortStatsAttempts':agentAuthMgrPortStatsAttempts,'agentAuthMgrPortStatsFailedAttempts':agentAuthMgrPortStatsFailedAttempts,'agentAuthMgrPortStatsClearTable':agentAuthMgrPortStatsClearTable,'agentAuthMgrPortStatsClearEntry':agentAuthMgrPortStatsClearEntry,'agentAuthMgrPortStatsClear':agentAuthMgrPortStatsClear,'agentAuthMgrTrapsConfigGroup':agentAuthMgrTrapsConfigGroup,'authMgrTrapMode':authMgrTrapMode})