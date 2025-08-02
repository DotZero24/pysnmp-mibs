_r='ciscoItpDsmrUcpNotificationsGroup'
_q='ciscoItpDsmrUcpGroup'
_p='ciscoItpDsmrUcpSessionState'
_o='cdsmrUcpDestRowStatus'
_n='cdsmrUcpDestRcvdResponses'
_m='cdsmrUcpDestSentResponses'
_l='cdsmrUcpDestRcvdRequests'
_k='cdsmrUcpDestSentRequests'
_j='cdsmrUcpDestProfileName'
_i='cdsmrUcpDestRemoteIpAddress'
_h='cdsmrUcpDestRemoteIpAddrType'
_g='cdsmrUcpDestRemotePortNumber'
_f='cdsmrUcpDestSessionInitTimer'
_e='cdsmrUcpDestSendWindow'
_d='cdsmrUcpDestResponseTimer'
_c='cdsmrUcpDestInactivityTimer'
_b='cdsmrUcpSessionRowStatus'
_a='cdsmrUcpSessionDynamicDest'
_Z='cdsmrUcpSessionLocalIpAddress'
_Y='cdsmrUcpSessionLocalIpAddrType'
_X='cdsmrUcpProfileRowStatus'
_W='cdsmrUcpProfileSessionInitTimer'
_V='cdsmrUcpProfileSendWindow'
_U='cdsmrUcpProfileResponseTimer'
_T='cdsmrUcpProfileInactivityTimer'
_S='cdsmrUcpSessionStateNotifEnabled'
_R='responses'
_Q='requests'
_P='cdsmrUcpDestName'
_O='cdsmrUcpProfileName'
_N='TruthValue'
_M='Integer32'
_L='cgspEventSequenceNumber'
_K='cgspCLLICode'
_J='cdsmrUcpDestState'
_I='cdsmrUcpSessionLocalPortNumber'
_H='not-accessible'
_G='cgspInstNetwork'
_F='read-only'
_E='milliseconds'
_D='CISCO-ITP-GSP-MIB'
_C='read-create'
_B='CISCO-ITP-DSMR-UCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cgspCLLICode,cgspEventSequenceNumber,cgspInstNetwork=mibBuilder.importSymbols(_D,_K,_L,_G)
CmlrName,=mibBuilder.importSymbols('CISCO-ITP-MLR-MIB','CmlrName')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
ciscoItpDsmrUcpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,1302))
if mibBuilder.loadTexts:ciscoItpDsmrUcpMIB.setRevisions(('2005-05-18 00:00',))
class CdsmrUcpInactivityTimer(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1000,9000000))
class CdsmrUcpResponseTimer(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1000,10000))
class CdsmrUcpSendWindow(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,100))
class CdsmrUcpSessionInitTimer(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(500,120000))
_CiscoItpDsmrUcpMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoItpDsmrUcpMIBNotifs=_CiscoItpDsmrUcpMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,1302,0))
_CiscoItpDsmrUcpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoItpDsmrUcpMIBObjects=_CiscoItpDsmrUcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,1302,1))
_CdsmrUcpScalars_ObjectIdentity=ObjectIdentity
cdsmrUcpScalars=_CdsmrUcpScalars_ObjectIdentity((1,3,6,1,4,1,9,9,1302,1,0))
class _CdsmrUcpSessionStateNotifEnabled_Type(TruthValue):defaultValue=2
_CdsmrUcpSessionStateNotifEnabled_Type.__name__=_N
_CdsmrUcpSessionStateNotifEnabled_Object=MibScalar
cdsmrUcpSessionStateNotifEnabled=_CdsmrUcpSessionStateNotifEnabled_Object((1,3,6,1,4,1,9,9,1302,1,0,1),_CdsmrUcpSessionStateNotifEnabled_Type())
cdsmrUcpSessionStateNotifEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:cdsmrUcpSessionStateNotifEnabled.setStatus(_A)
_CdsmrUcpProfileTable_Object=MibTable
cdsmrUcpProfileTable=_CdsmrUcpProfileTable_Object((1,3,6,1,4,1,9,9,1302,1,5))
if mibBuilder.loadTexts:cdsmrUcpProfileTable.setStatus(_A)
_CdsmrUcpProfileTableEntry_Object=MibTableRow
cdsmrUcpProfileTableEntry=_CdsmrUcpProfileTableEntry_Object((1,3,6,1,4,1,9,9,1302,1,5,1))
cdsmrUcpProfileTableEntry.setIndexNames((0,_D,_G),(0,_B,_O))
if mibBuilder.loadTexts:cdsmrUcpProfileTableEntry.setStatus(_A)
_CdsmrUcpProfileName_Type=CmlrName
_CdsmrUcpProfileName_Object=MibTableColumn
cdsmrUcpProfileName=_CdsmrUcpProfileName_Object((1,3,6,1,4,1,9,9,1302,1,5,1,1),_CdsmrUcpProfileName_Type())
cdsmrUcpProfileName.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsmrUcpProfileName.setStatus(_A)
_CdsmrUcpProfileInactivityTimer_Type=CdsmrUcpInactivityTimer
_CdsmrUcpProfileInactivityTimer_Object=MibTableColumn
cdsmrUcpProfileInactivityTimer=_CdsmrUcpProfileInactivityTimer_Object((1,3,6,1,4,1,9,9,1302,1,5,1,2),_CdsmrUcpProfileInactivityTimer_Type())
cdsmrUcpProfileInactivityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpProfileInactivityTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpProfileInactivityTimer.setUnits(_E)
_CdsmrUcpProfileResponseTimer_Type=CdsmrUcpResponseTimer
_CdsmrUcpProfileResponseTimer_Object=MibTableColumn
cdsmrUcpProfileResponseTimer=_CdsmrUcpProfileResponseTimer_Object((1,3,6,1,4,1,9,9,1302,1,5,1,3),_CdsmrUcpProfileResponseTimer_Type())
cdsmrUcpProfileResponseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpProfileResponseTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpProfileResponseTimer.setUnits(_E)
_CdsmrUcpProfileSendWindow_Type=CdsmrUcpSendWindow
_CdsmrUcpProfileSendWindow_Object=MibTableColumn
cdsmrUcpProfileSendWindow=_CdsmrUcpProfileSendWindow_Object((1,3,6,1,4,1,9,9,1302,1,5,1,7),_CdsmrUcpProfileSendWindow_Type())
cdsmrUcpProfileSendWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpProfileSendWindow.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpProfileSendWindow.setUnits('bytes')
_CdsmrUcpProfileSessionInitTimer_Type=CdsmrUcpSessionInitTimer
_CdsmrUcpProfileSessionInitTimer_Object=MibTableColumn
cdsmrUcpProfileSessionInitTimer=_CdsmrUcpProfileSessionInitTimer_Object((1,3,6,1,4,1,9,9,1302,1,5,1,8),_CdsmrUcpProfileSessionInitTimer_Type())
cdsmrUcpProfileSessionInitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpProfileSessionInitTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpProfileSessionInitTimer.setUnits(_E)
_CdsmrUcpProfileRowStatus_Type=RowStatus
_CdsmrUcpProfileRowStatus_Object=MibTableColumn
cdsmrUcpProfileRowStatus=_CdsmrUcpProfileRowStatus_Object((1,3,6,1,4,1,9,9,1302,1,5,1,9),_CdsmrUcpProfileRowStatus_Type())
cdsmrUcpProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpProfileRowStatus.setStatus(_A)
_CdsmrUcpSessionTable_Object=MibTable
cdsmrUcpSessionTable=_CdsmrUcpSessionTable_Object((1,3,6,1,4,1,9,9,1302,1,6))
if mibBuilder.loadTexts:cdsmrUcpSessionTable.setStatus(_A)
_CdsmrUcpSessionTableEntry_Object=MibTableRow
cdsmrUcpSessionTableEntry=_CdsmrUcpSessionTableEntry_Object((1,3,6,1,4,1,9,9,1302,1,6,1))
cdsmrUcpSessionTableEntry.setIndexNames((0,_D,_G),(0,_B,_I))
if mibBuilder.loadTexts:cdsmrUcpSessionTableEntry.setStatus(_A)
_CdsmrUcpSessionLocalPortNumber_Type=InetPortNumber
_CdsmrUcpSessionLocalPortNumber_Object=MibTableColumn
cdsmrUcpSessionLocalPortNumber=_CdsmrUcpSessionLocalPortNumber_Object((1,3,6,1,4,1,9,9,1302,1,6,1,1),_CdsmrUcpSessionLocalPortNumber_Type())
cdsmrUcpSessionLocalPortNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsmrUcpSessionLocalPortNumber.setStatus(_A)
_CdsmrUcpSessionLocalIpAddrType_Type=InetAddressType
_CdsmrUcpSessionLocalIpAddrType_Object=MibTableColumn
cdsmrUcpSessionLocalIpAddrType=_CdsmrUcpSessionLocalIpAddrType_Object((1,3,6,1,4,1,9,9,1302,1,6,1,2),_CdsmrUcpSessionLocalIpAddrType_Type())
cdsmrUcpSessionLocalIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpSessionLocalIpAddrType.setStatus(_A)
_CdsmrUcpSessionLocalIpAddress_Type=InetAddress
_CdsmrUcpSessionLocalIpAddress_Object=MibTableColumn
cdsmrUcpSessionLocalIpAddress=_CdsmrUcpSessionLocalIpAddress_Object((1,3,6,1,4,1,9,9,1302,1,6,1,3),_CdsmrUcpSessionLocalIpAddress_Type())
cdsmrUcpSessionLocalIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpSessionLocalIpAddress.setStatus(_A)
_CdsmrUcpSessionDynamicDest_Type=TruthValue
_CdsmrUcpSessionDynamicDest_Object=MibTableColumn
cdsmrUcpSessionDynamicDest=_CdsmrUcpSessionDynamicDest_Object((1,3,6,1,4,1,9,9,1302,1,6,1,4),_CdsmrUcpSessionDynamicDest_Type())
cdsmrUcpSessionDynamicDest.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpSessionDynamicDest.setStatus(_A)
_CdsmrUcpSessionRowStatus_Type=RowStatus
_CdsmrUcpSessionRowStatus_Object=MibTableColumn
cdsmrUcpSessionRowStatus=_CdsmrUcpSessionRowStatus_Object((1,3,6,1,4,1,9,9,1302,1,6,1,5),_CdsmrUcpSessionRowStatus_Type())
cdsmrUcpSessionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpSessionRowStatus.setStatus(_A)
_CdsmrUcpDestTable_Object=MibTable
cdsmrUcpDestTable=_CdsmrUcpDestTable_Object((1,3,6,1,4,1,9,9,1302,1,7))
if mibBuilder.loadTexts:cdsmrUcpDestTable.setStatus(_A)
_CdsmrUcpDestTableEntry_Object=MibTableRow
cdsmrUcpDestTableEntry=_CdsmrUcpDestTableEntry_Object((1,3,6,1,4,1,9,9,1302,1,7,1))
cdsmrUcpDestTableEntry.setIndexNames((0,_D,_G),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:cdsmrUcpDestTableEntry.setStatus(_A)
_CdsmrUcpDestName_Type=CmlrName
_CdsmrUcpDestName_Object=MibTableColumn
cdsmrUcpDestName=_CdsmrUcpDestName_Object((1,3,6,1,4,1,9,9,1302,1,7,1,1),_CdsmrUcpDestName_Type())
cdsmrUcpDestName.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsmrUcpDestName.setStatus(_A)
_CdsmrUcpDestInactivityTimer_Type=CdsmrUcpInactivityTimer
_CdsmrUcpDestInactivityTimer_Object=MibTableColumn
cdsmrUcpDestInactivityTimer=_CdsmrUcpDestInactivityTimer_Object((1,3,6,1,4,1,9,9,1302,1,7,1,2),_CdsmrUcpDestInactivityTimer_Type())
cdsmrUcpDestInactivityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestInactivityTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestInactivityTimer.setUnits(_E)
_CdsmrUcpDestResponseTimer_Type=CdsmrUcpResponseTimer
_CdsmrUcpDestResponseTimer_Object=MibTableColumn
cdsmrUcpDestResponseTimer=_CdsmrUcpDestResponseTimer_Object((1,3,6,1,4,1,9,9,1302,1,7,1,3),_CdsmrUcpDestResponseTimer_Type())
cdsmrUcpDestResponseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestResponseTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestResponseTimer.setUnits(_E)
_CdsmrUcpDestSendWindow_Type=CdsmrUcpSendWindow
_CdsmrUcpDestSendWindow_Object=MibTableColumn
cdsmrUcpDestSendWindow=_CdsmrUcpDestSendWindow_Object((1,3,6,1,4,1,9,9,1302,1,7,1,4),_CdsmrUcpDestSendWindow_Type())
cdsmrUcpDestSendWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestSendWindow.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestSendWindow.setUnits('bytes')
_CdsmrUcpDestSessionInitTimer_Type=CdsmrUcpSessionInitTimer
_CdsmrUcpDestSessionInitTimer_Object=MibTableColumn
cdsmrUcpDestSessionInitTimer=_CdsmrUcpDestSessionInitTimer_Object((1,3,6,1,4,1,9,9,1302,1,7,1,5),_CdsmrUcpDestSessionInitTimer_Type())
cdsmrUcpDestSessionInitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestSessionInitTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestSessionInitTimer.setUnits(_E)
_CdsmrUcpDestRemotePortNumber_Type=InetPortNumber
_CdsmrUcpDestRemotePortNumber_Object=MibTableColumn
cdsmrUcpDestRemotePortNumber=_CdsmrUcpDestRemotePortNumber_Object((1,3,6,1,4,1,9,9,1302,1,7,1,6),_CdsmrUcpDestRemotePortNumber_Type())
cdsmrUcpDestRemotePortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestRemotePortNumber.setStatus(_A)
_CdsmrUcpDestRemoteIpAddrType_Type=InetAddressType
_CdsmrUcpDestRemoteIpAddrType_Object=MibTableColumn
cdsmrUcpDestRemoteIpAddrType=_CdsmrUcpDestRemoteIpAddrType_Object((1,3,6,1,4,1,9,9,1302,1,7,1,7),_CdsmrUcpDestRemoteIpAddrType_Type())
cdsmrUcpDestRemoteIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestRemoteIpAddrType.setStatus(_A)
_CdsmrUcpDestRemoteIpAddress_Type=InetAddress
_CdsmrUcpDestRemoteIpAddress_Object=MibTableColumn
cdsmrUcpDestRemoteIpAddress=_CdsmrUcpDestRemoteIpAddress_Object((1,3,6,1,4,1,9,9,1302,1,7,1,8),_CdsmrUcpDestRemoteIpAddress_Type())
cdsmrUcpDestRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestRemoteIpAddress.setStatus(_A)
_CdsmrUcpDestProfileName_Type=CmlrName
_CdsmrUcpDestProfileName_Object=MibTableColumn
cdsmrUcpDestProfileName=_CdsmrUcpDestProfileName_Object((1,3,6,1,4,1,9,9,1302,1,7,1,9),_CdsmrUcpDestProfileName_Type())
cdsmrUcpDestProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestProfileName.setStatus(_A)
class _CdsmrUcpDestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('open',3)))
_CdsmrUcpDestState_Type.__name__=_M
_CdsmrUcpDestState_Object=MibTableColumn
cdsmrUcpDestState=_CdsmrUcpDestState_Object((1,3,6,1,4,1,9,9,1302,1,7,1,10),_CdsmrUcpDestState_Type())
cdsmrUcpDestState.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrUcpDestState.setStatus(_A)
_CdsmrUcpDestSentRequests_Type=Counter32
_CdsmrUcpDestSentRequests_Object=MibTableColumn
cdsmrUcpDestSentRequests=_CdsmrUcpDestSentRequests_Object((1,3,6,1,4,1,9,9,1302,1,7,1,11),_CdsmrUcpDestSentRequests_Type())
cdsmrUcpDestSentRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrUcpDestSentRequests.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestSentRequests.setUnits(_Q)
_CdsmrUcpDestRcvdRequests_Type=Counter32
_CdsmrUcpDestRcvdRequests_Object=MibTableColumn
cdsmrUcpDestRcvdRequests=_CdsmrUcpDestRcvdRequests_Object((1,3,6,1,4,1,9,9,1302,1,7,1,12),_CdsmrUcpDestRcvdRequests_Type())
cdsmrUcpDestRcvdRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrUcpDestRcvdRequests.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestRcvdRequests.setUnits(_Q)
_CdsmrUcpDestSentResponses_Type=Counter32
_CdsmrUcpDestSentResponses_Object=MibTableColumn
cdsmrUcpDestSentResponses=_CdsmrUcpDestSentResponses_Object((1,3,6,1,4,1,9,9,1302,1,7,1,13),_CdsmrUcpDestSentResponses_Type())
cdsmrUcpDestSentResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrUcpDestSentResponses.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestSentResponses.setUnits(_R)
_CdsmrUcpDestRcvdResponses_Type=Counter32
_CdsmrUcpDestRcvdResponses_Object=MibTableColumn
cdsmrUcpDestRcvdResponses=_CdsmrUcpDestRcvdResponses_Object((1,3,6,1,4,1,9,9,1302,1,7,1,14),_CdsmrUcpDestRcvdResponses_Type())
cdsmrUcpDestRcvdResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrUcpDestRcvdResponses.setStatus(_A)
if mibBuilder.loadTexts:cdsmrUcpDestRcvdResponses.setUnits(_R)
_CdsmrUcpDestRowStatus_Type=RowStatus
_CdsmrUcpDestRowStatus_Object=MibTableColumn
cdsmrUcpDestRowStatus=_CdsmrUcpDestRowStatus_Object((1,3,6,1,4,1,9,9,1302,1,7,1,15),_CdsmrUcpDestRowStatus_Type())
cdsmrUcpDestRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrUcpDestRowStatus.setStatus(_A)
_CiscoItpDsmrUcpMIBConform_ObjectIdentity=ObjectIdentity
ciscoItpDsmrUcpMIBConform=_CiscoItpDsmrUcpMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,1302,2))
_CiscoItpDsmrUcpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoItpDsmrUcpMIBCompliances=_CiscoItpDsmrUcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,1302,2,1))
_CiscoItpDsmrUcpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoItpDsmrUcpMIBGroups=_CiscoItpDsmrUcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,1302,2,2))
ciscoItpDsmrUcpGroup=ObjectGroup((1,3,6,1,4,1,9,9,1302,2,2,1))
ciscoItpDsmrUcpGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_J),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoItpDsmrUcpGroup.setStatus(_A)
ciscoItpDsmrUcpSessionState=NotificationType((1,3,6,1,4,1,9,9,1302,0,1))
ciscoItpDsmrUcpSessionState.setObjects(*((_D,_L),(_D,_K),(_B,_J)))
if mibBuilder.loadTexts:ciscoItpDsmrUcpSessionState.setStatus(_A)
ciscoItpDsmrUcpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,1302,2,2,2))
ciscoItpDsmrUcpNotificationsGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:ciscoItpDsmrUcpNotificationsGroup.setStatus(_A)
ciscoItpDsmrUcpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,1302,2,1,1))
ciscoItpDsmrUcpMIBCompliance.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:ciscoItpDsmrUcpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CdsmrUcpInactivityTimer':CdsmrUcpInactivityTimer,'CdsmrUcpResponseTimer':CdsmrUcpResponseTimer,'CdsmrUcpSendWindow':CdsmrUcpSendWindow,'CdsmrUcpSessionInitTimer':CdsmrUcpSessionInitTimer,'ciscoItpDsmrUcpMIB':ciscoItpDsmrUcpMIB,'ciscoItpDsmrUcpMIBNotifs':ciscoItpDsmrUcpMIBNotifs,_p:ciscoItpDsmrUcpSessionState,'ciscoItpDsmrUcpMIBObjects':ciscoItpDsmrUcpMIBObjects,'cdsmrUcpScalars':cdsmrUcpScalars,_S:cdsmrUcpSessionStateNotifEnabled,'cdsmrUcpProfileTable':cdsmrUcpProfileTable,'cdsmrUcpProfileTableEntry':cdsmrUcpProfileTableEntry,_O:cdsmrUcpProfileName,_T:cdsmrUcpProfileInactivityTimer,_U:cdsmrUcpProfileResponseTimer,_V:cdsmrUcpProfileSendWindow,_W:cdsmrUcpProfileSessionInitTimer,_X:cdsmrUcpProfileRowStatus,'cdsmrUcpSessionTable':cdsmrUcpSessionTable,'cdsmrUcpSessionTableEntry':cdsmrUcpSessionTableEntry,_I:cdsmrUcpSessionLocalPortNumber,_Y:cdsmrUcpSessionLocalIpAddrType,_Z:cdsmrUcpSessionLocalIpAddress,_a:cdsmrUcpSessionDynamicDest,_b:cdsmrUcpSessionRowStatus,'cdsmrUcpDestTable':cdsmrUcpDestTable,'cdsmrUcpDestTableEntry':cdsmrUcpDestTableEntry,_P:cdsmrUcpDestName,_c:cdsmrUcpDestInactivityTimer,_d:cdsmrUcpDestResponseTimer,_e:cdsmrUcpDestSendWindow,_f:cdsmrUcpDestSessionInitTimer,_g:cdsmrUcpDestRemotePortNumber,_h:cdsmrUcpDestRemoteIpAddrType,_i:cdsmrUcpDestRemoteIpAddress,_j:cdsmrUcpDestProfileName,_J:cdsmrUcpDestState,_k:cdsmrUcpDestSentRequests,_l:cdsmrUcpDestRcvdRequests,_m:cdsmrUcpDestSentResponses,_n:cdsmrUcpDestRcvdResponses,_o:cdsmrUcpDestRowStatus,'ciscoItpDsmrUcpMIBConform':ciscoItpDsmrUcpMIBConform,'ciscoItpDsmrUcpMIBCompliances':ciscoItpDsmrUcpMIBCompliances,'ciscoItpDsmrUcpMIBCompliance':ciscoItpDsmrUcpMIBCompliance,'ciscoItpDsmrUcpMIBGroups':ciscoItpDsmrUcpMIBGroups,_q:ciscoItpDsmrUcpGroup,_r:ciscoItpDsmrUcpNotificationsGroup})