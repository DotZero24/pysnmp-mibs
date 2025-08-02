_AP='ciscoCsgNotifGroup'
_AO='ciscoCsgNotifEnableGroup'
_AN='ciscoUserDbGroup'
_AM='ciscoQuotaMgrGroup'
_AL='ciscoAgentGroup'
_AK='ciscoUserGroup'
_AJ='ciscoCsgQuotaMgrLostRecordEvent'
_AI='ciscoCsgAgentLostRecordEvent'
_AH='ciscoCsgUserDbStateChange'
_AG='ciscoCsgQuotaMgrStateChange'
_AF='ciscoCsgAgentStateChange'
_AE='csgDatabaseNotifsEnabled'
_AD='csgQuotaNotifsEnabled'
_AC='csgAgentNotifsEnabled'
_AB='csgQuotaMgrRowStatus'
_AA='csgQuotaMgrLostRecordTimer'
_A9='csgQuotaMgrPriority'
_A8='csgQuotaMgrUserGroupName'
_A7='csgAgentRowStatus'
_A6='csgAgentLostRecordTimer'
_A5='csgAgentPriority'
_A4='csgAgentAcctName'
_A3='csgUserDbRowStatus'
_A2='csgUserRowStatus'
_A1='csgUserLRUSteals'
_A0='csgUserHighWater'
_z='csgUserCurrEntries'
_y='csgUserMaxEntries'
_x='csgQuotaMgrPort'
_w='csgQuotaMgrIpAddr'
_v='csgQuotaMgrIpAddrType'
_u='suspended'
_t='nawait'
_s='echowait'
_r='standby'
_q='csgAgentPort'
_p='csgAgentIpAddr'
_o='csgAgentIpAddrType'
_n='csgUserDbPort'
_m='csgUserDbIpAddr'
_l='csgUserDbIpAddrType'
_k='CsgUserTableUpperBound'
_j='csgUserDbReqErrors'
_i='csgUserDbReqTimeouts'
_h='csgUserDbReqResent'
_g='csgUserDbUidsReturned'
_f='csgUserDbRequests'
_e='csgUserDbState'
_d='failed'
_c='active'
_b='csgUserGroupName'
_a='TimeInterval'
_Z='Unsigned32'
_Y='csgQuotaMgrRetransmit'
_X='csgQuotaMgrBadRecord'
_W='csgQuotaMgrHighWater'
_V='csgQuotaMgrOutstanding'
_U='csgQuotaMgrFailAck'
_T='csgQuotaMgrTotalSent'
_S='csgQuotaMgrLostRecords'
_R='csgQuotaMgrState'
_Q='csgAgentRetransmit'
_P='csgAgentBadRecord'
_O='csgAgentHighWater'
_N='csgAgentOutstanding'
_M='csgAgentFailAck'
_L='csgAgentTotalSent'
_K='csgAgentLostRecords'
_J='csgAgentState'
_I='TruthValue'
_H='Integer32'
_G='csgUserCardId'
_F='read-write'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='current'
_A='CISCO-CSG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Z,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_a,_I)
ciscoCsgMIB=ModuleIdentity((1,3,6,1,4,1,9,9,331))
if mibBuilder.loadTexts:ciscoCsgMIB.setRevisions(('2003-02-20 00:00',))
class CsgSlotNumber(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class CsgEntityName(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
class CsgServerPriority(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
class CsgUserTableUpperBound(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CiscoCsgMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCsgMIBNotifs=_CiscoCsgMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,331,0))
_CiscoCsgMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCsgMIBObjects=_CiscoCsgMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,331,1))
_CsgScalars_ObjectIdentity=ObjectIdentity
csgScalars=_CsgScalars_ObjectIdentity((1,3,6,1,4,1,9,9,331,1,1))
class _CsgAgentLostRecordTimer_Type(TimeInterval):defaultValue=60
_CsgAgentLostRecordTimer_Type.__name__=_a
_CsgAgentLostRecordTimer_Object=MibScalar
csgAgentLostRecordTimer=_CsgAgentLostRecordTimer_Object((1,3,6,1,4,1,9,9,331,1,1,1),_CsgAgentLostRecordTimer_Type())
csgAgentLostRecordTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:csgAgentLostRecordTimer.setStatus(_B)
class _CsgQuotaMgrLostRecordTimer_Type(TimeInterval):defaultValue=60
_CsgQuotaMgrLostRecordTimer_Type.__name__=_a
_CsgQuotaMgrLostRecordTimer_Object=MibScalar
csgQuotaMgrLostRecordTimer=_CsgQuotaMgrLostRecordTimer_Object((1,3,6,1,4,1,9,9,331,1,1,2),_CsgQuotaMgrLostRecordTimer_Type())
csgQuotaMgrLostRecordTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:csgQuotaMgrLostRecordTimer.setStatus(_B)
_CsgUserStats_ObjectIdentity=ObjectIdentity
csgUserStats=_CsgUserStats_ObjectIdentity((1,3,6,1,4,1,9,9,331,1,2))
_CsgUserTable_Object=MibTable
csgUserTable=_CsgUserTable_Object((1,3,6,1,4,1,9,9,331,1,2,1))
if mibBuilder.loadTexts:csgUserTable.setStatus(_B)
_CsgUserTableEntry_Object=MibTableRow
csgUserTableEntry=_CsgUserTableEntry_Object((1,3,6,1,4,1,9,9,331,1,2,1,1))
csgUserTableEntry.setIndexNames((0,_A,_G),(0,_A,_b))
if mibBuilder.loadTexts:csgUserTableEntry.setStatus(_B)
_CsgUserCardId_Type=CsgSlotNumber
_CsgUserCardId_Object=MibTableColumn
csgUserCardId=_CsgUserCardId_Object((1,3,6,1,4,1,9,9,331,1,2,1,1,1),_CsgUserCardId_Type())
csgUserCardId.setMaxAccess(_D)
if mibBuilder.loadTexts:csgUserCardId.setStatus(_B)
_CsgUserGroupName_Type=CsgEntityName
_CsgUserGroupName_Object=MibTableColumn
csgUserGroupName=_CsgUserGroupName_Object((1,3,6,1,4,1,9,9,331,1,2,1,1,2),_CsgUserGroupName_Type())
csgUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:csgUserGroupName.setStatus(_B)
_CsgUserMaxEntries_Type=CsgUserTableUpperBound
_CsgUserMaxEntries_Object=MibTableColumn
csgUserMaxEntries=_CsgUserMaxEntries_Object((1,3,6,1,4,1,9,9,331,1,2,1,1,3),_CsgUserMaxEntries_Type())
csgUserMaxEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:csgUserMaxEntries.setStatus(_B)
_CsgUserCurrEntries_Type=Gauge32
_CsgUserCurrEntries_Object=MibTableColumn
csgUserCurrEntries=_CsgUserCurrEntries_Object((1,3,6,1,4,1,9,9,331,1,2,1,1,4),_CsgUserCurrEntries_Type())
csgUserCurrEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserCurrEntries.setStatus(_B)
class _CsgUserHighWater_Type(CsgUserTableUpperBound):defaultValue=0
_CsgUserHighWater_Type.__name__=_k
_CsgUserHighWater_Object=MibTableColumn
csgUserHighWater=_CsgUserHighWater_Object((1,3,6,1,4,1,9,9,331,1,2,1,1,5),_CsgUserHighWater_Type())
csgUserHighWater.setMaxAccess(_E)
if mibBuilder.loadTexts:csgUserHighWater.setStatus(_B)
_CsgUserLRUSteals_Type=Counter32
_CsgUserLRUSteals_Object=MibTableColumn
csgUserLRUSteals=_CsgUserLRUSteals_Object((1,3,6,1,4,1,9,9,331,1,2,1,1,6),_CsgUserLRUSteals_Type())
csgUserLRUSteals.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserLRUSteals.setStatus(_B)
_CsgUserRowStatus_Type=RowStatus
_CsgUserRowStatus_Object=MibTableColumn
csgUserRowStatus=_CsgUserRowStatus_Object((1,3,6,1,4,1,9,9,331,1,2,1,1,7),_CsgUserRowStatus_Type())
csgUserRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:csgUserRowStatus.setStatus(_B)
_CsgUserDataBaseStats_ObjectIdentity=ObjectIdentity
csgUserDataBaseStats=_CsgUserDataBaseStats_ObjectIdentity((1,3,6,1,4,1,9,9,331,1,3))
_CsgUserDbTable_Object=MibTable
csgUserDbTable=_CsgUserDbTable_Object((1,3,6,1,4,1,9,9,331,1,3,1))
if mibBuilder.loadTexts:csgUserDbTable.setStatus(_B)
_CsgUserDbTableEntry_Object=MibTableRow
csgUserDbTableEntry=_CsgUserDbTableEntry_Object((1,3,6,1,4,1,9,9,331,1,3,1,1))
csgUserDbTableEntry.setIndexNames((0,_A,_G),(0,_A,_b),(0,_A,_l),(0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:csgUserDbTableEntry.setStatus(_B)
_CsgUserDbIpAddrType_Type=InetAddressType
_CsgUserDbIpAddrType_Object=MibTableColumn
csgUserDbIpAddrType=_CsgUserDbIpAddrType_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,1),_CsgUserDbIpAddrType_Type())
csgUserDbIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:csgUserDbIpAddrType.setStatus(_B)
_CsgUserDbIpAddr_Type=InetAddress
_CsgUserDbIpAddr_Object=MibTableColumn
csgUserDbIpAddr=_CsgUserDbIpAddr_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,2),_CsgUserDbIpAddr_Type())
csgUserDbIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:csgUserDbIpAddr.setStatus(_B)
_CsgUserDbPort_Type=InetPortNumber
_CsgUserDbPort_Object=MibTableColumn
csgUserDbPort=_CsgUserDbPort_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,3),_CsgUserDbPort_Type())
csgUserDbPort.setMaxAccess(_D)
if mibBuilder.loadTexts:csgUserDbPort.setStatus(_B)
class _CsgUserDbState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reset',1),(_c,2),(_d,3)))
_CsgUserDbState_Type.__name__=_H
_CsgUserDbState_Object=MibTableColumn
csgUserDbState=_CsgUserDbState_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,4),_CsgUserDbState_Type())
csgUserDbState.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserDbState.setStatus(_B)
_CsgUserDbRequests_Type=Counter64
_CsgUserDbRequests_Object=MibTableColumn
csgUserDbRequests=_CsgUserDbRequests_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,5),_CsgUserDbRequests_Type())
csgUserDbRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserDbRequests.setStatus(_B)
_CsgUserDbUidsReturned_Type=Counter64
_CsgUserDbUidsReturned_Object=MibTableColumn
csgUserDbUidsReturned=_CsgUserDbUidsReturned_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,6),_CsgUserDbUidsReturned_Type())
csgUserDbUidsReturned.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserDbUidsReturned.setStatus(_B)
_CsgUserDbReqResent_Type=Counter32
_CsgUserDbReqResent_Object=MibTableColumn
csgUserDbReqResent=_CsgUserDbReqResent_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,7),_CsgUserDbReqResent_Type())
csgUserDbReqResent.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserDbReqResent.setStatus(_B)
_CsgUserDbReqTimeouts_Type=Counter32
_CsgUserDbReqTimeouts_Object=MibTableColumn
csgUserDbReqTimeouts=_CsgUserDbReqTimeouts_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,8),_CsgUserDbReqTimeouts_Type())
csgUserDbReqTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserDbReqTimeouts.setStatus(_B)
_CsgUserDbReqErrors_Type=Counter32
_CsgUserDbReqErrors_Object=MibTableColumn
csgUserDbReqErrors=_CsgUserDbReqErrors_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,9),_CsgUserDbReqErrors_Type())
csgUserDbReqErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:csgUserDbReqErrors.setStatus(_B)
_CsgUserDbRowStatus_Type=RowStatus
_CsgUserDbRowStatus_Object=MibTableColumn
csgUserDbRowStatus=_CsgUserDbRowStatus_Object((1,3,6,1,4,1,9,9,331,1,3,1,1,10),_CsgUserDbRowStatus_Type())
csgUserDbRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:csgUserDbRowStatus.setStatus(_B)
_CsgAgentStats_ObjectIdentity=ObjectIdentity
csgAgentStats=_CsgAgentStats_ObjectIdentity((1,3,6,1,4,1,9,9,331,1,4))
_CsgAgentTable_Object=MibTable
csgAgentTable=_CsgAgentTable_Object((1,3,6,1,4,1,9,9,331,1,4,1))
if mibBuilder.loadTexts:csgAgentTable.setStatus(_B)
_CsgAgentTableEntry_Object=MibTableRow
csgAgentTableEntry=_CsgAgentTableEntry_Object((1,3,6,1,4,1,9,9,331,1,4,1,1))
csgAgentTableEntry.setIndexNames((0,_A,_G),(0,_A,_o),(0,_A,_p),(0,_A,_q))
if mibBuilder.loadTexts:csgAgentTableEntry.setStatus(_B)
_CsgAgentIpAddrType_Type=InetAddressType
_CsgAgentIpAddrType_Object=MibTableColumn
csgAgentIpAddrType=_CsgAgentIpAddrType_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,1),_CsgAgentIpAddrType_Type())
csgAgentIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:csgAgentIpAddrType.setStatus(_B)
_CsgAgentIpAddr_Type=InetAddress
_CsgAgentIpAddr_Object=MibTableColumn
csgAgentIpAddr=_CsgAgentIpAddr_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,2),_CsgAgentIpAddr_Type())
csgAgentIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:csgAgentIpAddr.setStatus(_B)
_CsgAgentPort_Type=InetPortNumber
_CsgAgentPort_Object=MibTableColumn
csgAgentPort=_CsgAgentPort_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,3),_CsgAgentPort_Type())
csgAgentPort.setMaxAccess(_D)
if mibBuilder.loadTexts:csgAgentPort.setStatus(_B)
_CsgAgentAcctName_Type=CsgEntityName
_CsgAgentAcctName_Object=MibTableColumn
csgAgentAcctName=_CsgAgentAcctName_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,4),_CsgAgentAcctName_Type())
csgAgentAcctName.setMaxAccess(_E)
if mibBuilder.loadTexts:csgAgentAcctName.setStatus(_B)
_CsgAgentPriority_Type=CsgServerPriority
_CsgAgentPriority_Object=MibTableColumn
csgAgentPriority=_CsgAgentPriority_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,5),_CsgAgentPriority_Type())
csgAgentPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:csgAgentPriority.setStatus(_B)
class _CsgAgentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_r,1),(_d,2),(_c,3),(_s,4),(_t,5),(_u,6)))
_CsgAgentState_Type.__name__=_H
_CsgAgentState_Object=MibTableColumn
csgAgentState=_CsgAgentState_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,6),_CsgAgentState_Type())
csgAgentState.setMaxAccess(_C)
if mibBuilder.loadTexts:csgAgentState.setStatus(_B)
_CsgAgentLostRecords_Type=Counter32
_CsgAgentLostRecords_Object=MibTableColumn
csgAgentLostRecords=_CsgAgentLostRecords_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,7),_CsgAgentLostRecords_Type())
csgAgentLostRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:csgAgentLostRecords.setStatus(_B)
_CsgAgentTotalSent_Type=Counter64
_CsgAgentTotalSent_Object=MibTableColumn
csgAgentTotalSent=_CsgAgentTotalSent_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,8),_CsgAgentTotalSent_Type())
csgAgentTotalSent.setMaxAccess(_C)
if mibBuilder.loadTexts:csgAgentTotalSent.setStatus(_B)
_CsgAgentFailAck_Type=Counter32
_CsgAgentFailAck_Object=MibTableColumn
csgAgentFailAck=_CsgAgentFailAck_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,9),_CsgAgentFailAck_Type())
csgAgentFailAck.setMaxAccess(_C)
if mibBuilder.loadTexts:csgAgentFailAck.setStatus(_B)
_CsgAgentOutstanding_Type=Gauge32
_CsgAgentOutstanding_Object=MibTableColumn
csgAgentOutstanding=_CsgAgentOutstanding_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,10),_CsgAgentOutstanding_Type())
csgAgentOutstanding.setMaxAccess(_C)
if mibBuilder.loadTexts:csgAgentOutstanding.setStatus(_B)
class _CsgAgentHighWater_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CsgAgentHighWater_Type.__name__=_Z
_CsgAgentHighWater_Object=MibTableColumn
csgAgentHighWater=_CsgAgentHighWater_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,11),_CsgAgentHighWater_Type())
csgAgentHighWater.setMaxAccess(_E)
if mibBuilder.loadTexts:csgAgentHighWater.setStatus(_B)
_CsgAgentBadRecord_Type=Counter32
_CsgAgentBadRecord_Object=MibTableColumn
csgAgentBadRecord=_CsgAgentBadRecord_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,12),_CsgAgentBadRecord_Type())
csgAgentBadRecord.setMaxAccess(_C)
if mibBuilder.loadTexts:csgAgentBadRecord.setStatus(_B)
_CsgAgentRetransmit_Type=Counter32
_CsgAgentRetransmit_Object=MibTableColumn
csgAgentRetransmit=_CsgAgentRetransmit_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,13),_CsgAgentRetransmit_Type())
csgAgentRetransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:csgAgentRetransmit.setStatus(_B)
_CsgAgentRowStatus_Type=RowStatus
_CsgAgentRowStatus_Object=MibTableColumn
csgAgentRowStatus=_CsgAgentRowStatus_Object((1,3,6,1,4,1,9,9,331,1,4,1,1,14),_CsgAgentRowStatus_Type())
csgAgentRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:csgAgentRowStatus.setStatus(_B)
_CsgQuotaMgrStats_ObjectIdentity=ObjectIdentity
csgQuotaMgrStats=_CsgQuotaMgrStats_ObjectIdentity((1,3,6,1,4,1,9,9,331,1,5))
_CsgQuotaMgrTable_Object=MibTable
csgQuotaMgrTable=_CsgQuotaMgrTable_Object((1,3,6,1,4,1,9,9,331,1,5,1))
if mibBuilder.loadTexts:csgQuotaMgrTable.setStatus(_B)
_CsgQuotaMgrTableEntry_Object=MibTableRow
csgQuotaMgrTableEntry=_CsgQuotaMgrTableEntry_Object((1,3,6,1,4,1,9,9,331,1,5,1,1))
csgQuotaMgrTableEntry.setIndexNames((0,_A,_G),(0,_A,_v),(0,_A,_w),(0,_A,_x))
if mibBuilder.loadTexts:csgQuotaMgrTableEntry.setStatus(_B)
_CsgQuotaMgrIpAddrType_Type=InetAddressType
_CsgQuotaMgrIpAddrType_Object=MibTableColumn
csgQuotaMgrIpAddrType=_CsgQuotaMgrIpAddrType_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,1),_CsgQuotaMgrIpAddrType_Type())
csgQuotaMgrIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:csgQuotaMgrIpAddrType.setStatus(_B)
_CsgQuotaMgrIpAddr_Type=InetAddress
_CsgQuotaMgrIpAddr_Object=MibTableColumn
csgQuotaMgrIpAddr=_CsgQuotaMgrIpAddr_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,2),_CsgQuotaMgrIpAddr_Type())
csgQuotaMgrIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:csgQuotaMgrIpAddr.setStatus(_B)
_CsgQuotaMgrPort_Type=InetPortNumber
_CsgQuotaMgrPort_Object=MibTableColumn
csgQuotaMgrPort=_CsgQuotaMgrPort_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,3),_CsgQuotaMgrPort_Type())
csgQuotaMgrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:csgQuotaMgrPort.setStatus(_B)
_CsgQuotaMgrUserGroupName_Type=CsgEntityName
_CsgQuotaMgrUserGroupName_Object=MibTableColumn
csgQuotaMgrUserGroupName=_CsgQuotaMgrUserGroupName_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,4),_CsgQuotaMgrUserGroupName_Type())
csgQuotaMgrUserGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrUserGroupName.setStatus(_B)
_CsgQuotaMgrPriority_Type=CsgServerPriority
_CsgQuotaMgrPriority_Object=MibTableColumn
csgQuotaMgrPriority=_CsgQuotaMgrPriority_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,5),_CsgQuotaMgrPriority_Type())
csgQuotaMgrPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:csgQuotaMgrPriority.setStatus(_B)
class _CsgQuotaMgrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_r,1),(_d,2),(_c,3),(_s,4),(_t,5),(_u,6)))
_CsgQuotaMgrState_Type.__name__=_H
_CsgQuotaMgrState_Object=MibTableColumn
csgQuotaMgrState=_CsgQuotaMgrState_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,6),_CsgQuotaMgrState_Type())
csgQuotaMgrState.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrState.setStatus(_B)
_CsgQuotaMgrLostRecords_Type=Counter32
_CsgQuotaMgrLostRecords_Object=MibTableColumn
csgQuotaMgrLostRecords=_CsgQuotaMgrLostRecords_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,7),_CsgQuotaMgrLostRecords_Type())
csgQuotaMgrLostRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrLostRecords.setStatus(_B)
_CsgQuotaMgrTotalSent_Type=Counter64
_CsgQuotaMgrTotalSent_Object=MibTableColumn
csgQuotaMgrTotalSent=_CsgQuotaMgrTotalSent_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,8),_CsgQuotaMgrTotalSent_Type())
csgQuotaMgrTotalSent.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrTotalSent.setStatus(_B)
_CsgQuotaMgrFailAck_Type=Counter32
_CsgQuotaMgrFailAck_Object=MibTableColumn
csgQuotaMgrFailAck=_CsgQuotaMgrFailAck_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,9),_CsgQuotaMgrFailAck_Type())
csgQuotaMgrFailAck.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrFailAck.setStatus(_B)
_CsgQuotaMgrOutstanding_Type=Gauge32
_CsgQuotaMgrOutstanding_Object=MibTableColumn
csgQuotaMgrOutstanding=_CsgQuotaMgrOutstanding_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,10),_CsgQuotaMgrOutstanding_Type())
csgQuotaMgrOutstanding.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrOutstanding.setStatus(_B)
class _CsgQuotaMgrHighWater_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CsgQuotaMgrHighWater_Type.__name__=_Z
_CsgQuotaMgrHighWater_Object=MibTableColumn
csgQuotaMgrHighWater=_CsgQuotaMgrHighWater_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,11),_CsgQuotaMgrHighWater_Type())
csgQuotaMgrHighWater.setMaxAccess(_E)
if mibBuilder.loadTexts:csgQuotaMgrHighWater.setStatus(_B)
_CsgQuotaMgrBadRecord_Type=Counter32
_CsgQuotaMgrBadRecord_Object=MibTableColumn
csgQuotaMgrBadRecord=_CsgQuotaMgrBadRecord_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,12),_CsgQuotaMgrBadRecord_Type())
csgQuotaMgrBadRecord.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrBadRecord.setStatus(_B)
_CsgQuotaMgrRetransmit_Type=Counter32
_CsgQuotaMgrRetransmit_Object=MibTableColumn
csgQuotaMgrRetransmit=_CsgQuotaMgrRetransmit_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,13),_CsgQuotaMgrRetransmit_Type())
csgQuotaMgrRetransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:csgQuotaMgrRetransmit.setStatus(_B)
_CsgQuotaMgrRowStatus_Type=RowStatus
_CsgQuotaMgrRowStatus_Object=MibTableColumn
csgQuotaMgrRowStatus=_CsgQuotaMgrRowStatus_Object((1,3,6,1,4,1,9,9,331,1,5,1,1,14),_CsgQuotaMgrRowStatus_Type())
csgQuotaMgrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:csgQuotaMgrRowStatus.setStatus(_B)
_CsgNotifsEnable_ObjectIdentity=ObjectIdentity
csgNotifsEnable=_CsgNotifsEnable_ObjectIdentity((1,3,6,1,4,1,9,9,331,1,6))
class _CsgAgentNotifsEnabled_Type(TruthValue):defaultValue=2
_CsgAgentNotifsEnabled_Type.__name__=_I
_CsgAgentNotifsEnabled_Object=MibScalar
csgAgentNotifsEnabled=_CsgAgentNotifsEnabled_Object((1,3,6,1,4,1,9,9,331,1,6,1),_CsgAgentNotifsEnabled_Type())
csgAgentNotifsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:csgAgentNotifsEnabled.setStatus(_B)
class _CsgQuotaNotifsEnabled_Type(TruthValue):defaultValue=2
_CsgQuotaNotifsEnabled_Type.__name__=_I
_CsgQuotaNotifsEnabled_Object=MibScalar
csgQuotaNotifsEnabled=_CsgQuotaNotifsEnabled_Object((1,3,6,1,4,1,9,9,331,1,6,2),_CsgQuotaNotifsEnabled_Type())
csgQuotaNotifsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:csgQuotaNotifsEnabled.setStatus(_B)
class _CsgDatabaseNotifsEnabled_Type(TruthValue):defaultValue=2
_CsgDatabaseNotifsEnabled_Type.__name__=_I
_CsgDatabaseNotifsEnabled_Object=MibScalar
csgDatabaseNotifsEnabled=_CsgDatabaseNotifsEnabled_Object((1,3,6,1,4,1,9,9,331,1,6,3),_CsgDatabaseNotifsEnabled_Type())
csgDatabaseNotifsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:csgDatabaseNotifsEnabled.setStatus(_B)
_CiscoCsgMIBConform_ObjectIdentity=ObjectIdentity
ciscoCsgMIBConform=_CiscoCsgMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,331,2))
_CiscoCsgMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCsgMIBCompliances=_CiscoCsgMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,331,2,1))
_CiscoCsgMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCsgMIBGroups=_CiscoCsgMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,331,2,2))
ciscoUserGroup=ObjectGroup((1,3,6,1,4,1,9,9,331,2,2,1))
ciscoUserGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ciscoUserGroup.setStatus(_B)
ciscoUserDbGroup=ObjectGroup((1,3,6,1,4,1,9,9,331,2,2,2))
ciscoUserDbGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_A3)))
if mibBuilder.loadTexts:ciscoUserDbGroup.setStatus(_B)
ciscoAgentGroup=ObjectGroup((1,3,6,1,4,1,9,9,331,2,2,3))
ciscoAgentGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:ciscoAgentGroup.setStatus(_B)
ciscoQuotaMgrGroup=ObjectGroup((1,3,6,1,4,1,9,9,331,2,2,4))
ciscoQuotaMgrGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ciscoQuotaMgrGroup.setStatus(_B)
ciscoCsgNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,331,2,2,5))
ciscoCsgNotifEnableGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoCsgNotifEnableGroup.setStatus(_B)
ciscoCsgAgentStateChange=NotificationType((1,3,6,1,4,1,9,9,331,0,1))
ciscoCsgAgentStateChange.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoCsgAgentStateChange.setStatus(_B)
ciscoCsgQuotaMgrStateChange=NotificationType((1,3,6,1,4,1,9,9,331,0,2))
ciscoCsgQuotaMgrStateChange.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoCsgQuotaMgrStateChange.setStatus(_B)
ciscoCsgUserDbStateChange=NotificationType((1,3,6,1,4,1,9,9,331,0,3))
ciscoCsgUserDbStateChange.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoCsgUserDbStateChange.setStatus(_B)
ciscoCsgAgentLostRecordEvent=NotificationType((1,3,6,1,4,1,9,9,331,0,4))
ciscoCsgAgentLostRecordEvent.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoCsgAgentLostRecordEvent.setStatus(_B)
ciscoCsgQuotaMgrLostRecordEvent=NotificationType((1,3,6,1,4,1,9,9,331,0,5))
ciscoCsgQuotaMgrLostRecordEvent.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoCsgQuotaMgrLostRecordEvent.setStatus(_B)
ciscoCsgNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,331,2,2,6))
ciscoCsgNotifGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:ciscoCsgNotifGroup.setStatus(_B)
ciscoCsgMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,331,2,1,1))
ciscoCsgMIBCompliance.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:ciscoCsgMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CsgSlotNumber':CsgSlotNumber,'CsgEntityName':CsgEntityName,'CsgServerPriority':CsgServerPriority,_k:CsgUserTableUpperBound,'ciscoCsgMIB':ciscoCsgMIB,'ciscoCsgMIBNotifs':ciscoCsgMIBNotifs,_AF:ciscoCsgAgentStateChange,_AG:ciscoCsgQuotaMgrStateChange,_AH:ciscoCsgUserDbStateChange,_AI:ciscoCsgAgentLostRecordEvent,_AJ:ciscoCsgQuotaMgrLostRecordEvent,'ciscoCsgMIBObjects':ciscoCsgMIBObjects,'csgScalars':csgScalars,_A6:csgAgentLostRecordTimer,_AA:csgQuotaMgrLostRecordTimer,'csgUserStats':csgUserStats,'csgUserTable':csgUserTable,'csgUserTableEntry':csgUserTableEntry,_G:csgUserCardId,_b:csgUserGroupName,_y:csgUserMaxEntries,_z:csgUserCurrEntries,_A0:csgUserHighWater,_A1:csgUserLRUSteals,_A2:csgUserRowStatus,'csgUserDataBaseStats':csgUserDataBaseStats,'csgUserDbTable':csgUserDbTable,'csgUserDbTableEntry':csgUserDbTableEntry,_l:csgUserDbIpAddrType,_m:csgUserDbIpAddr,_n:csgUserDbPort,_e:csgUserDbState,_f:csgUserDbRequests,_g:csgUserDbUidsReturned,_h:csgUserDbReqResent,_i:csgUserDbReqTimeouts,_j:csgUserDbReqErrors,_A3:csgUserDbRowStatus,'csgAgentStats':csgAgentStats,'csgAgentTable':csgAgentTable,'csgAgentTableEntry':csgAgentTableEntry,_o:csgAgentIpAddrType,_p:csgAgentIpAddr,_q:csgAgentPort,_A4:csgAgentAcctName,_A5:csgAgentPriority,_J:csgAgentState,_K:csgAgentLostRecords,_L:csgAgentTotalSent,_M:csgAgentFailAck,_N:csgAgentOutstanding,_O:csgAgentHighWater,_P:csgAgentBadRecord,_Q:csgAgentRetransmit,_A7:csgAgentRowStatus,'csgQuotaMgrStats':csgQuotaMgrStats,'csgQuotaMgrTable':csgQuotaMgrTable,'csgQuotaMgrTableEntry':csgQuotaMgrTableEntry,_v:csgQuotaMgrIpAddrType,_w:csgQuotaMgrIpAddr,_x:csgQuotaMgrPort,_A8:csgQuotaMgrUserGroupName,_A9:csgQuotaMgrPriority,_R:csgQuotaMgrState,_S:csgQuotaMgrLostRecords,_T:csgQuotaMgrTotalSent,_U:csgQuotaMgrFailAck,_V:csgQuotaMgrOutstanding,_W:csgQuotaMgrHighWater,_X:csgQuotaMgrBadRecord,_Y:csgQuotaMgrRetransmit,_AB:csgQuotaMgrRowStatus,'csgNotifsEnable':csgNotifsEnable,_AC:csgAgentNotifsEnabled,_AD:csgQuotaNotifsEnabled,_AE:csgDatabaseNotifsEnabled,'ciscoCsgMIBConform':ciscoCsgMIBConform,'ciscoCsgMIBCompliances':ciscoCsgMIBCompliances,'ciscoCsgMIBCompliance':ciscoCsgMIBCompliance,'ciscoCsgMIBGroups':ciscoCsgMIBGroups,_AK:ciscoUserGroup,_AN:ciscoUserDbGroup,_AL:ciscoAgentGroup,_AM:ciscoQuotaMgrGroup,_AO:ciscoCsgNotifEnableGroup,_AP:ciscoCsgNotifGroup})