_x='ciscoItpDsmrSmppNotificationsGroup'
_w='ciscoItpDsmrSmppGroup'
_v='ciscoItpDsmrSmppSessionState'
_u='cdsmrSmppDestRowStatus'
_t='cdsmrSmppDestRcvdResponses'
_s='cdsmrSmppDestSentResponses'
_r='cdsmrSmppDestRcvdRequests'
_q='cdsmrSmppDestSentRequests'
_p='cdsmrSmppDestProfileName'
_o='cdsmrSmppDestRemoteIpAddress'
_n='cdsmrSmppDestRemoteIpAddrType'
_m='cdsmrSmppDestSessionInitTimer'
_l='cdsmrSmppDestRemotePortNumber'
_k='cdsmrSmppDestSendWindow'
_j='cdsmrSmppDestResponseTimer'
_i='cdsmrSmppDestCallingParty'
_h='cdsmrSmppDestKeepaliveTimer'
_g='cdsmrSmppDestInactivityTimer'
_f='cdsmrSmppDestBindType'
_e='cdsmrSmppSessionRowStatus'
_d='cdsmrSmppSessionDynamicDest'
_c='cdsmrSmppSessionLocalIpAddress'
_b='cdsmrSmppSessionLocalIpAddrType'
_a='cdsmrSmppProfileRowStatus'
_Z='cdsmrSmppProfileSessionInitTimer'
_Y='cdsmrSmppProfileSendWindow'
_X='cdsmrSmppProfileResponseTimer'
_W='cdsmrSmppProfileCallingParty'
_V='cdsmrSmppProfileKeepaliveTimer'
_U='cdsmrSmppProfileInactivityTimer'
_T='cdsmrSmppProfileBindType'
_S='cdsmrSmppSessionStateNotifEnable'
_R='responses'
_Q='requests'
_P='cdsmrSmppDestName'
_O='cdsmrSmppProfileName'
_N='TruthValue'
_M='Integer32'
_L='cgspEventSequenceNumber'
_K='cgspCLLICode'
_J='cdsmrSmppDestState'
_I='cdsmrSmppSessionLocalPortNumber'
_H='not-accessible'
_G='cgspInstNetwork'
_F='read-only'
_E='CISCO-ITP-GSP-MIB'
_D='milliseconds'
_C='read-create'
_B='CISCO-ITP-DSMR-SMPP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cgspCLLICode,cgspEventSequenceNumber,cgspInstNetwork=mibBuilder.importSymbols(_E,_K,_L,_G)
CmlrName,=mibBuilder.importSymbols('CISCO-ITP-MLR-MIB','CmlrName')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
ciscoItpDsmrSmppMIB=ModuleIdentity((1,3,6,1,4,1,9,9,1301))
if mibBuilder.loadTexts:ciscoItpDsmrSmppMIB.setRevisions(('2005-05-18 00:00',))
class CdsmrSmppInactivityTimer(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1000,9000000))
class CdsmrSmppResponseTimer(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1000,10000))
class CdsmrSmppSendWindow(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,100))
class CdsmrSmppSessionInitTimer(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(500,120000))
class CdsmrSmppBindType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('any',2),('receiver',3),('transceiver',4),('transmitter',5)))
class CdsmrSmppKeepaliveTimer(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(500,120000))
_CiscoItpDsmrSmppMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoItpDsmrSmppMIBNotifs=_CiscoItpDsmrSmppMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,1301,0))
_CiscoItpDsmrSmppMIBObjects_ObjectIdentity=ObjectIdentity
ciscoItpDsmrSmppMIBObjects=_CiscoItpDsmrSmppMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,1301,1))
_CdsmrSmppScalars_ObjectIdentity=ObjectIdentity
cdsmrSmppScalars=_CdsmrSmppScalars_ObjectIdentity((1,3,6,1,4,1,9,9,1301,1,0))
class _CdsmrSmppSessionStateNotifEnable_Type(TruthValue):defaultValue=2
_CdsmrSmppSessionStateNotifEnable_Type.__name__=_N
_CdsmrSmppSessionStateNotifEnable_Object=MibScalar
cdsmrSmppSessionStateNotifEnable=_CdsmrSmppSessionStateNotifEnable_Object((1,3,6,1,4,1,9,9,1301,1,0,1),_CdsmrSmppSessionStateNotifEnable_Type())
cdsmrSmppSessionStateNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cdsmrSmppSessionStateNotifEnable.setStatus(_A)
_CdsmrSmppProfileTable_Object=MibTable
cdsmrSmppProfileTable=_CdsmrSmppProfileTable_Object((1,3,6,1,4,1,9,9,1301,1,2))
if mibBuilder.loadTexts:cdsmrSmppProfileTable.setStatus(_A)
_CdsmrSmppProfileTableEntry_Object=MibTableRow
cdsmrSmppProfileTableEntry=_CdsmrSmppProfileTableEntry_Object((1,3,6,1,4,1,9,9,1301,1,2,1))
cdsmrSmppProfileTableEntry.setIndexNames((0,_E,_G),(0,_B,_O))
if mibBuilder.loadTexts:cdsmrSmppProfileTableEntry.setStatus(_A)
_CdsmrSmppProfileName_Type=CmlrName
_CdsmrSmppProfileName_Object=MibTableColumn
cdsmrSmppProfileName=_CdsmrSmppProfileName_Object((1,3,6,1,4,1,9,9,1301,1,2,1,1),_CdsmrSmppProfileName_Type())
cdsmrSmppProfileName.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsmrSmppProfileName.setStatus(_A)
_CdsmrSmppProfileBindType_Type=CdsmrSmppBindType
_CdsmrSmppProfileBindType_Object=MibTableColumn
cdsmrSmppProfileBindType=_CdsmrSmppProfileBindType_Object((1,3,6,1,4,1,9,9,1301,1,2,1,2),_CdsmrSmppProfileBindType_Type())
cdsmrSmppProfileBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileBindType.setStatus(_A)
_CdsmrSmppProfileInactivityTimer_Type=CdsmrSmppInactivityTimer
_CdsmrSmppProfileInactivityTimer_Object=MibTableColumn
cdsmrSmppProfileInactivityTimer=_CdsmrSmppProfileInactivityTimer_Object((1,3,6,1,4,1,9,9,1301,1,2,1,3),_CdsmrSmppProfileInactivityTimer_Type())
cdsmrSmppProfileInactivityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileInactivityTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppProfileInactivityTimer.setUnits(_D)
_CdsmrSmppProfileKeepaliveTimer_Type=CdsmrSmppKeepaliveTimer
_CdsmrSmppProfileKeepaliveTimer_Object=MibTableColumn
cdsmrSmppProfileKeepaliveTimer=_CdsmrSmppProfileKeepaliveTimer_Object((1,3,6,1,4,1,9,9,1301,1,2,1,4),_CdsmrSmppProfileKeepaliveTimer_Type())
cdsmrSmppProfileKeepaliveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileKeepaliveTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppProfileKeepaliveTimer.setUnits(_D)
_CdsmrSmppProfileCallingParty_Type=TruthValue
_CdsmrSmppProfileCallingParty_Object=MibTableColumn
cdsmrSmppProfileCallingParty=_CdsmrSmppProfileCallingParty_Object((1,3,6,1,4,1,9,9,1301,1,2,1,5),_CdsmrSmppProfileCallingParty_Type())
cdsmrSmppProfileCallingParty.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileCallingParty.setStatus(_A)
_CdsmrSmppProfileResponseTimer_Type=CdsmrSmppResponseTimer
_CdsmrSmppProfileResponseTimer_Object=MibTableColumn
cdsmrSmppProfileResponseTimer=_CdsmrSmppProfileResponseTimer_Object((1,3,6,1,4,1,9,9,1301,1,2,1,6),_CdsmrSmppProfileResponseTimer_Type())
cdsmrSmppProfileResponseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileResponseTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppProfileResponseTimer.setUnits(_D)
_CdsmrSmppProfileSendWindow_Type=CdsmrSmppSendWindow
_CdsmrSmppProfileSendWindow_Object=MibTableColumn
cdsmrSmppProfileSendWindow=_CdsmrSmppProfileSendWindow_Object((1,3,6,1,4,1,9,9,1301,1,2,1,7),_CdsmrSmppProfileSendWindow_Type())
cdsmrSmppProfileSendWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileSendWindow.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppProfileSendWindow.setUnits('bytes')
_CdsmrSmppProfileSessionInitTimer_Type=CdsmrSmppSessionInitTimer
_CdsmrSmppProfileSessionInitTimer_Object=MibTableColumn
cdsmrSmppProfileSessionInitTimer=_CdsmrSmppProfileSessionInitTimer_Object((1,3,6,1,4,1,9,9,1301,1,2,1,8),_CdsmrSmppProfileSessionInitTimer_Type())
cdsmrSmppProfileSessionInitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileSessionInitTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppProfileSessionInitTimer.setUnits(_D)
_CdsmrSmppProfileRowStatus_Type=RowStatus
_CdsmrSmppProfileRowStatus_Object=MibTableColumn
cdsmrSmppProfileRowStatus=_CdsmrSmppProfileRowStatus_Object((1,3,6,1,4,1,9,9,1301,1,2,1,9),_CdsmrSmppProfileRowStatus_Type())
cdsmrSmppProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppProfileRowStatus.setStatus(_A)
_CdsmrSmppSessionTable_Object=MibTable
cdsmrSmppSessionTable=_CdsmrSmppSessionTable_Object((1,3,6,1,4,1,9,9,1301,1,3))
if mibBuilder.loadTexts:cdsmrSmppSessionTable.setStatus(_A)
_CdsmrSmppSessionTableEntry_Object=MibTableRow
cdsmrSmppSessionTableEntry=_CdsmrSmppSessionTableEntry_Object((1,3,6,1,4,1,9,9,1301,1,3,1))
cdsmrSmppSessionTableEntry.setIndexNames((0,_E,_G),(0,_B,_I))
if mibBuilder.loadTexts:cdsmrSmppSessionTableEntry.setStatus(_A)
_CdsmrSmppSessionLocalPortNumber_Type=InetPortNumber
_CdsmrSmppSessionLocalPortNumber_Object=MibTableColumn
cdsmrSmppSessionLocalPortNumber=_CdsmrSmppSessionLocalPortNumber_Object((1,3,6,1,4,1,9,9,1301,1,3,1,1),_CdsmrSmppSessionLocalPortNumber_Type())
cdsmrSmppSessionLocalPortNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsmrSmppSessionLocalPortNumber.setStatus(_A)
_CdsmrSmppSessionLocalIpAddrType_Type=InetAddressType
_CdsmrSmppSessionLocalIpAddrType_Object=MibTableColumn
cdsmrSmppSessionLocalIpAddrType=_CdsmrSmppSessionLocalIpAddrType_Object((1,3,6,1,4,1,9,9,1301,1,3,1,2),_CdsmrSmppSessionLocalIpAddrType_Type())
cdsmrSmppSessionLocalIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppSessionLocalIpAddrType.setStatus(_A)
_CdsmrSmppSessionLocalIpAddress_Type=InetAddress
_CdsmrSmppSessionLocalIpAddress_Object=MibTableColumn
cdsmrSmppSessionLocalIpAddress=_CdsmrSmppSessionLocalIpAddress_Object((1,3,6,1,4,1,9,9,1301,1,3,1,3),_CdsmrSmppSessionLocalIpAddress_Type())
cdsmrSmppSessionLocalIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppSessionLocalIpAddress.setStatus(_A)
_CdsmrSmppSessionDynamicDest_Type=TruthValue
_CdsmrSmppSessionDynamicDest_Object=MibTableColumn
cdsmrSmppSessionDynamicDest=_CdsmrSmppSessionDynamicDest_Object((1,3,6,1,4,1,9,9,1301,1,3,1,4),_CdsmrSmppSessionDynamicDest_Type())
cdsmrSmppSessionDynamicDest.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppSessionDynamicDest.setStatus(_A)
_CdsmrSmppSessionRowStatus_Type=RowStatus
_CdsmrSmppSessionRowStatus_Object=MibTableColumn
cdsmrSmppSessionRowStatus=_CdsmrSmppSessionRowStatus_Object((1,3,6,1,4,1,9,9,1301,1,3,1,5),_CdsmrSmppSessionRowStatus_Type())
cdsmrSmppSessionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppSessionRowStatus.setStatus(_A)
_CdsmrSmppDestTable_Object=MibTable
cdsmrSmppDestTable=_CdsmrSmppDestTable_Object((1,3,6,1,4,1,9,9,1301,1,4))
if mibBuilder.loadTexts:cdsmrSmppDestTable.setStatus(_A)
_CdsmrSmppDestTableEntry_Object=MibTableRow
cdsmrSmppDestTableEntry=_CdsmrSmppDestTableEntry_Object((1,3,6,1,4,1,9,9,1301,1,4,1))
cdsmrSmppDestTableEntry.setIndexNames((0,_E,_G),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:cdsmrSmppDestTableEntry.setStatus(_A)
_CdsmrSmppDestName_Type=CmlrName
_CdsmrSmppDestName_Object=MibTableColumn
cdsmrSmppDestName=_CdsmrSmppDestName_Object((1,3,6,1,4,1,9,9,1301,1,4,1,1),_CdsmrSmppDestName_Type())
cdsmrSmppDestName.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsmrSmppDestName.setStatus(_A)
_CdsmrSmppDestBindType_Type=CdsmrSmppBindType
_CdsmrSmppDestBindType_Object=MibTableColumn
cdsmrSmppDestBindType=_CdsmrSmppDestBindType_Object((1,3,6,1,4,1,9,9,1301,1,4,1,2),_CdsmrSmppDestBindType_Type())
cdsmrSmppDestBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestBindType.setStatus(_A)
_CdsmrSmppDestInactivityTimer_Type=CdsmrSmppInactivityTimer
_CdsmrSmppDestInactivityTimer_Object=MibTableColumn
cdsmrSmppDestInactivityTimer=_CdsmrSmppDestInactivityTimer_Object((1,3,6,1,4,1,9,9,1301,1,4,1,3),_CdsmrSmppDestInactivityTimer_Type())
cdsmrSmppDestInactivityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestInactivityTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestInactivityTimer.setUnits(_D)
_CdsmrSmppDestKeepaliveTimer_Type=CdsmrSmppKeepaliveTimer
_CdsmrSmppDestKeepaliveTimer_Object=MibTableColumn
cdsmrSmppDestKeepaliveTimer=_CdsmrSmppDestKeepaliveTimer_Object((1,3,6,1,4,1,9,9,1301,1,4,1,4),_CdsmrSmppDestKeepaliveTimer_Type())
cdsmrSmppDestKeepaliveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestKeepaliveTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestKeepaliveTimer.setUnits(_D)
_CdsmrSmppDestCallingParty_Type=TruthValue
_CdsmrSmppDestCallingParty_Object=MibTableColumn
cdsmrSmppDestCallingParty=_CdsmrSmppDestCallingParty_Object((1,3,6,1,4,1,9,9,1301,1,4,1,5),_CdsmrSmppDestCallingParty_Type())
cdsmrSmppDestCallingParty.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestCallingParty.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestCallingParty.setUnits(_D)
_CdsmrSmppDestResponseTimer_Type=CdsmrSmppResponseTimer
_CdsmrSmppDestResponseTimer_Object=MibTableColumn
cdsmrSmppDestResponseTimer=_CdsmrSmppDestResponseTimer_Object((1,3,6,1,4,1,9,9,1301,1,4,1,6),_CdsmrSmppDestResponseTimer_Type())
cdsmrSmppDestResponseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestResponseTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestResponseTimer.setUnits(_D)
_CdsmrSmppDestSendWindow_Type=CdsmrSmppSendWindow
_CdsmrSmppDestSendWindow_Object=MibTableColumn
cdsmrSmppDestSendWindow=_CdsmrSmppDestSendWindow_Object((1,3,6,1,4,1,9,9,1301,1,4,1,7),_CdsmrSmppDestSendWindow_Type())
cdsmrSmppDestSendWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestSendWindow.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestSendWindow.setUnits('bytes')
_CdsmrSmppDestSessionInitTimer_Type=CdsmrSmppSessionInitTimer
_CdsmrSmppDestSessionInitTimer_Object=MibTableColumn
cdsmrSmppDestSessionInitTimer=_CdsmrSmppDestSessionInitTimer_Object((1,3,6,1,4,1,9,9,1301,1,4,1,8),_CdsmrSmppDestSessionInitTimer_Type())
cdsmrSmppDestSessionInitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestSessionInitTimer.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestSessionInitTimer.setUnits(_D)
_CdsmrSmppDestRemotePortNumber_Type=InetPortNumber
_CdsmrSmppDestRemotePortNumber_Object=MibTableColumn
cdsmrSmppDestRemotePortNumber=_CdsmrSmppDestRemotePortNumber_Object((1,3,6,1,4,1,9,9,1301,1,4,1,9),_CdsmrSmppDestRemotePortNumber_Type())
cdsmrSmppDestRemotePortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestRemotePortNumber.setStatus(_A)
_CdsmrSmppDestRemoteIpAddrType_Type=InetAddressType
_CdsmrSmppDestRemoteIpAddrType_Object=MibTableColumn
cdsmrSmppDestRemoteIpAddrType=_CdsmrSmppDestRemoteIpAddrType_Object((1,3,6,1,4,1,9,9,1301,1,4,1,10),_CdsmrSmppDestRemoteIpAddrType_Type())
cdsmrSmppDestRemoteIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestRemoteIpAddrType.setStatus(_A)
_CdsmrSmppDestRemoteIpAddress_Type=InetAddress
_CdsmrSmppDestRemoteIpAddress_Object=MibTableColumn
cdsmrSmppDestRemoteIpAddress=_CdsmrSmppDestRemoteIpAddress_Object((1,3,6,1,4,1,9,9,1301,1,4,1,11),_CdsmrSmppDestRemoteIpAddress_Type())
cdsmrSmppDestRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestRemoteIpAddress.setStatus(_A)
_CdsmrSmppDestProfileName_Type=CmlrName
_CdsmrSmppDestProfileName_Object=MibTableColumn
cdsmrSmppDestProfileName=_CdsmrSmppDestProfileName_Object((1,3,6,1,4,1,9,9,1301,1,4,1,12),_CdsmrSmppDestProfileName_Type())
cdsmrSmppDestProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestProfileName.setStatus(_A)
class _CdsmrSmppDestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('open',3)))
_CdsmrSmppDestState_Type.__name__=_M
_CdsmrSmppDestState_Object=MibTableColumn
cdsmrSmppDestState=_CdsmrSmppDestState_Object((1,3,6,1,4,1,9,9,1301,1,4,1,13),_CdsmrSmppDestState_Type())
cdsmrSmppDestState.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrSmppDestState.setStatus(_A)
_CdsmrSmppDestSentRequests_Type=Counter32
_CdsmrSmppDestSentRequests_Object=MibTableColumn
cdsmrSmppDestSentRequests=_CdsmrSmppDestSentRequests_Object((1,3,6,1,4,1,9,9,1301,1,4,1,14),_CdsmrSmppDestSentRequests_Type())
cdsmrSmppDestSentRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrSmppDestSentRequests.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestSentRequests.setUnits(_Q)
_CdsmrSmppDestRcvdRequests_Type=Counter32
_CdsmrSmppDestRcvdRequests_Object=MibTableColumn
cdsmrSmppDestRcvdRequests=_CdsmrSmppDestRcvdRequests_Object((1,3,6,1,4,1,9,9,1301,1,4,1,15),_CdsmrSmppDestRcvdRequests_Type())
cdsmrSmppDestRcvdRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrSmppDestRcvdRequests.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestRcvdRequests.setUnits(_Q)
_CdsmrSmppDestSentResponses_Type=Counter32
_CdsmrSmppDestSentResponses_Object=MibTableColumn
cdsmrSmppDestSentResponses=_CdsmrSmppDestSentResponses_Object((1,3,6,1,4,1,9,9,1301,1,4,1,16),_CdsmrSmppDestSentResponses_Type())
cdsmrSmppDestSentResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrSmppDestSentResponses.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestSentResponses.setUnits(_R)
_CdsmrSmppDestRcvdResponses_Type=Counter32
_CdsmrSmppDestRcvdResponses_Object=MibTableColumn
cdsmrSmppDestRcvdResponses=_CdsmrSmppDestRcvdResponses_Object((1,3,6,1,4,1,9,9,1301,1,4,1,17),_CdsmrSmppDestRcvdResponses_Type())
cdsmrSmppDestRcvdResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:cdsmrSmppDestRcvdResponses.setStatus(_A)
if mibBuilder.loadTexts:cdsmrSmppDestRcvdResponses.setUnits(_R)
_CdsmrSmppDestRowStatus_Type=RowStatus
_CdsmrSmppDestRowStatus_Object=MibTableColumn
cdsmrSmppDestRowStatus=_CdsmrSmppDestRowStatus_Object((1,3,6,1,4,1,9,9,1301,1,4,1,18),_CdsmrSmppDestRowStatus_Type())
cdsmrSmppDestRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsmrSmppDestRowStatus.setStatus(_A)
_CiscoItpDsmrSmppMIBConform_ObjectIdentity=ObjectIdentity
ciscoItpDsmrSmppMIBConform=_CiscoItpDsmrSmppMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,1301,2))
_CiscoItpDsmrSmppMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoItpDsmrSmppMIBCompliances=_CiscoItpDsmrSmppMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,1301,2,1))
_CiscoItpDsmrSmppMIBGroups_ObjectIdentity=ObjectIdentity
ciscoItpDsmrSmppMIBGroups=_CiscoItpDsmrSmppMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,1301,2,2))
ciscoItpDsmrSmppGroup=ObjectGroup((1,3,6,1,4,1,9,9,1301,2,2,1))
ciscoItpDsmrSmppGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_J),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoItpDsmrSmppGroup.setStatus(_A)
ciscoItpDsmrSmppSessionState=NotificationType((1,3,6,1,4,1,9,9,1301,0,1))
ciscoItpDsmrSmppSessionState.setObjects(*((_E,_L),(_E,_K),(_B,_J)))
if mibBuilder.loadTexts:ciscoItpDsmrSmppSessionState.setStatus(_A)
ciscoItpDsmrSmppNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,1301,2,2,2))
ciscoItpDsmrSmppNotificationsGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:ciscoItpDsmrSmppNotificationsGroup.setStatus(_A)
ciscoItpDsmrSmppMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,1301,2,1,1))
ciscoItpDsmrSmppMIBCompliance.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoItpDsmrSmppMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CdsmrSmppInactivityTimer':CdsmrSmppInactivityTimer,'CdsmrSmppResponseTimer':CdsmrSmppResponseTimer,'CdsmrSmppSendWindow':CdsmrSmppSendWindow,'CdsmrSmppSessionInitTimer':CdsmrSmppSessionInitTimer,'CdsmrSmppBindType':CdsmrSmppBindType,'CdsmrSmppKeepaliveTimer':CdsmrSmppKeepaliveTimer,'ciscoItpDsmrSmppMIB':ciscoItpDsmrSmppMIB,'ciscoItpDsmrSmppMIBNotifs':ciscoItpDsmrSmppMIBNotifs,_v:ciscoItpDsmrSmppSessionState,'ciscoItpDsmrSmppMIBObjects':ciscoItpDsmrSmppMIBObjects,'cdsmrSmppScalars':cdsmrSmppScalars,_S:cdsmrSmppSessionStateNotifEnable,'cdsmrSmppProfileTable':cdsmrSmppProfileTable,'cdsmrSmppProfileTableEntry':cdsmrSmppProfileTableEntry,_O:cdsmrSmppProfileName,_T:cdsmrSmppProfileBindType,_U:cdsmrSmppProfileInactivityTimer,_V:cdsmrSmppProfileKeepaliveTimer,_W:cdsmrSmppProfileCallingParty,_X:cdsmrSmppProfileResponseTimer,_Y:cdsmrSmppProfileSendWindow,_Z:cdsmrSmppProfileSessionInitTimer,_a:cdsmrSmppProfileRowStatus,'cdsmrSmppSessionTable':cdsmrSmppSessionTable,'cdsmrSmppSessionTableEntry':cdsmrSmppSessionTableEntry,_I:cdsmrSmppSessionLocalPortNumber,_b:cdsmrSmppSessionLocalIpAddrType,_c:cdsmrSmppSessionLocalIpAddress,_d:cdsmrSmppSessionDynamicDest,_e:cdsmrSmppSessionRowStatus,'cdsmrSmppDestTable':cdsmrSmppDestTable,'cdsmrSmppDestTableEntry':cdsmrSmppDestTableEntry,_P:cdsmrSmppDestName,_f:cdsmrSmppDestBindType,_g:cdsmrSmppDestInactivityTimer,_h:cdsmrSmppDestKeepaliveTimer,_i:cdsmrSmppDestCallingParty,_j:cdsmrSmppDestResponseTimer,_k:cdsmrSmppDestSendWindow,_m:cdsmrSmppDestSessionInitTimer,_l:cdsmrSmppDestRemotePortNumber,_n:cdsmrSmppDestRemoteIpAddrType,_o:cdsmrSmppDestRemoteIpAddress,_p:cdsmrSmppDestProfileName,_J:cdsmrSmppDestState,_q:cdsmrSmppDestSentRequests,_r:cdsmrSmppDestRcvdRequests,_s:cdsmrSmppDestSentResponses,_t:cdsmrSmppDestRcvdResponses,_u:cdsmrSmppDestRowStatus,'ciscoItpDsmrSmppMIBConform':ciscoItpDsmrSmppMIBConform,'ciscoItpDsmrSmppMIBCompliances':ciscoItpDsmrSmppMIBCompliances,'ciscoItpDsmrSmppMIBCompliance':ciscoItpDsmrSmppMIBCompliance,'ciscoItpDsmrSmppMIBGroups':ciscoItpDsmrSmppMIBGroups,_w:ciscoItpDsmrSmppGroup,_x:ciscoItpDsmrSmppNotificationsGroup})