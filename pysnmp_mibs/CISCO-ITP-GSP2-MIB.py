_AC='ciscoGsp2ContextGroup'
_AB='cgsp2ContextNetworkName'
_AA='cgsp2ContextAspName'
_A9='cgsp2ContextAsName'
_A8='cgsp2ContextSlc'
_A7='cgsp2ContextLinksetName'
_A6='cgsp2ContextType'
_A5='cgsp2LocalPeerProcessorNumber'
_A4='cgsp2OperRedundancy'
_A3='cgsp2OperMtp3Offload'
_A2='cgsp2Mtp3ErrorsCount'
_A1='cgsp2Mtp3ErrorsDescription'
_A0='cgsp2LpIpAddressRowStatus'
_z='cgsp2LpIpAddress'
_y='cgsp2LpIpAddressType'
_x='cgsp2LocalPeerRowStatus'
_w='cgsp2LocalPeerSlotNumber'
_v='cgsp2QosRowStatus'
_u='cgsp2QosAclId'
_t='cgsp2QosIpDscp'
_s='cgsp2QosPrecedenceValue'
_r='cgsp2QosType'
_q='cgsp2EventPcTimestamp'
_p='cgsp2EventPcText'
_o='cgsp2EventAspTimestamp'
_n='cgsp2EventAspText'
_m='cgsp2EventAsTimestamp'
_l='cgsp2EventAsText'
_k='cgsp2EventMtp3Timestamp'
_j='cgsp2EventMtp3Text'
_i='cgsp2EventMaxEntriesAllowed'
_h='cgsp2EventMaxEntries'
_g='cgsp2EventDroppedEvents'
_f='cgsp2EventLoggedEvents'
_e='cgsp2ContextIdentifier'
_d='cgsp2Mtp3ErrorsType'
_c='cgsp2LpIpAddressNumber'
_b='cgsp2QosClass'
_a='cgsp2EventPcIndex'
_Z='cgsp2EventPc'
_Y='cgsp2EventMtp3Index'
_X='cgsp2EventAspIndex'
_W='cgsp2EventAspName'
_V='cgsp2EventAsIndex'
_U='cgsp2EventAsName'
_T='cgsp2EventType'
_S='CItpTcAclId'
_R='ciscoGsp2LocalPeerGroupSup1'
_Q='cgsp2LocalPeerPort'
_P='ciscoGsp2OperationGroup'
_O='deprecated'
_N='ciscoGsp2Mtp3ErrorsGroup'
_M='ciscoGsp2LocalPeerGroup'
_L='Unsigned32'
_K='ciscoGsp2QosGroup'
_J='ciscoGsp2EventsGroup'
_I='SnmpAdminString'
_H='cgspInstNetwork'
_G='CISCO-ITP-GSP-MIB'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='CISCO-ITP-GSP2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cgspInstNetwork,=mibBuilder.importSymbols(_G,_H)
CItpTcAclId,CItpTcLinkSLC,CItpTcLinksetId,CItpTcNetworkName,CItpTcPointCode,CItpTcXuaName=mibBuilder.importSymbols('CISCO-ITP-TC-MIB',_S,'CItpTcLinkSLC','CItpTcLinksetId','CItpTcNetworkName','CItpTcPointCode','CItpTcXuaName')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoGsp2MIB=ModuleIdentity((1,3,6,1,4,1,9,9,332))
if mibBuilder.loadTexts:ciscoGsp2MIB.setRevisions(('2008-07-09 00:00','2007-12-18 00:00','2004-05-26 00:00','2003-08-07 00:00','2003-03-03 00:00'))
class Cgsp2TcQosClass(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class Cgsp2EventIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class CItpTcContextId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CItpTcContextType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,6)));namedValues=NamedValues(*(('unknown',0),('cs7link',1),('asp',6)))
_CiscoGsp2MIBNotifs_ObjectIdentity=ObjectIdentity
ciscoGsp2MIBNotifs=_CiscoGsp2MIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,332,0))
_CiscoGsp2MIBObjects_ObjectIdentity=ObjectIdentity
ciscoGsp2MIBObjects=_CiscoGsp2MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,332,1))
_Cgsp2Events_ObjectIdentity=ObjectIdentity
cgsp2Events=_Cgsp2Events_ObjectIdentity((1,3,6,1,4,1,9,9,332,1,1))
_Cgsp2EventTable_Object=MibTable
cgsp2EventTable=_Cgsp2EventTable_Object((1,3,6,1,4,1,9,9,332,1,1,1))
if mibBuilder.loadTexts:cgsp2EventTable.setStatus(_A)
_Cgsp2EventTableEntry_Object=MibTableRow
cgsp2EventTableEntry=_Cgsp2EventTableEntry_Object((1,3,6,1,4,1,9,9,332,1,1,1,1))
cgsp2EventTableEntry.setIndexNames((0,_G,_H),(0,_B,_T))
if mibBuilder.loadTexts:cgsp2EventTableEntry.setStatus(_A)
class _Cgsp2EventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('as',1),('asp',2),('mtp3',3),('pc',4)))
_Cgsp2EventType_Type.__name__=_E
_Cgsp2EventType_Object=MibTableColumn
cgsp2EventType=_Cgsp2EventType_Object((1,3,6,1,4,1,9,9,332,1,1,1,1,1),_Cgsp2EventType_Type())
cgsp2EventType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventType.setStatus(_A)
_Cgsp2EventLoggedEvents_Type=Counter32
_Cgsp2EventLoggedEvents_Object=MibTableColumn
cgsp2EventLoggedEvents=_Cgsp2EventLoggedEvents_Object((1,3,6,1,4,1,9,9,332,1,1,1,1,2),_Cgsp2EventLoggedEvents_Type())
cgsp2EventLoggedEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventLoggedEvents.setStatus(_A)
_Cgsp2EventDroppedEvents_Type=Counter32
_Cgsp2EventDroppedEvents_Object=MibTableColumn
cgsp2EventDroppedEvents=_Cgsp2EventDroppedEvents_Object((1,3,6,1,4,1,9,9,332,1,1,1,1,3),_Cgsp2EventDroppedEvents_Type())
cgsp2EventDroppedEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventDroppedEvents.setStatus(_A)
class _Cgsp2EventMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cgsp2EventMaxEntries_Type.__name__=_L
_Cgsp2EventMaxEntries_Object=MibTableColumn
cgsp2EventMaxEntries=_Cgsp2EventMaxEntries_Object((1,3,6,1,4,1,9,9,332,1,1,1,1,4),_Cgsp2EventMaxEntries_Type())
cgsp2EventMaxEntries.setMaxAccess('read-write')
if mibBuilder.loadTexts:cgsp2EventMaxEntries.setStatus(_A)
class _Cgsp2EventMaxEntriesAllowed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cgsp2EventMaxEntriesAllowed_Type.__name__=_L
_Cgsp2EventMaxEntriesAllowed_Object=MibTableColumn
cgsp2EventMaxEntriesAllowed=_Cgsp2EventMaxEntriesAllowed_Object((1,3,6,1,4,1,9,9,332,1,1,1,1,5),_Cgsp2EventMaxEntriesAllowed_Type())
cgsp2EventMaxEntriesAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventMaxEntriesAllowed.setStatus(_A)
_Cgsp2EventAsTable_Object=MibTable
cgsp2EventAsTable=_Cgsp2EventAsTable_Object((1,3,6,1,4,1,9,9,332,1,1,2))
if mibBuilder.loadTexts:cgsp2EventAsTable.setStatus(_A)
_Cgsp2EventAsTableEntry_Object=MibTableRow
cgsp2EventAsTableEntry=_Cgsp2EventAsTableEntry_Object((1,3,6,1,4,1,9,9,332,1,1,2,1))
cgsp2EventAsTableEntry.setIndexNames((0,_G,_H),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:cgsp2EventAsTableEntry.setStatus(_A)
_Cgsp2EventAsName_Type=CItpTcXuaName
_Cgsp2EventAsName_Object=MibTableColumn
cgsp2EventAsName=_Cgsp2EventAsName_Object((1,3,6,1,4,1,9,9,332,1,1,2,1,1),_Cgsp2EventAsName_Type())
cgsp2EventAsName.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventAsName.setStatus(_A)
_Cgsp2EventAsIndex_Type=Cgsp2EventIndex
_Cgsp2EventAsIndex_Object=MibTableColumn
cgsp2EventAsIndex=_Cgsp2EventAsIndex_Object((1,3,6,1,4,1,9,9,332,1,1,2,1,2),_Cgsp2EventAsIndex_Type())
cgsp2EventAsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventAsIndex.setStatus(_A)
class _Cgsp2EventAsText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cgsp2EventAsText_Type.__name__=_I
_Cgsp2EventAsText_Object=MibTableColumn
cgsp2EventAsText=_Cgsp2EventAsText_Object((1,3,6,1,4,1,9,9,332,1,1,2,1,3),_Cgsp2EventAsText_Type())
cgsp2EventAsText.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventAsText.setStatus(_A)
_Cgsp2EventAsTimestamp_Type=TimeStamp
_Cgsp2EventAsTimestamp_Object=MibTableColumn
cgsp2EventAsTimestamp=_Cgsp2EventAsTimestamp_Object((1,3,6,1,4,1,9,9,332,1,1,2,1,4),_Cgsp2EventAsTimestamp_Type())
cgsp2EventAsTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventAsTimestamp.setStatus(_A)
_Cgsp2EventAspTable_Object=MibTable
cgsp2EventAspTable=_Cgsp2EventAspTable_Object((1,3,6,1,4,1,9,9,332,1,1,3))
if mibBuilder.loadTexts:cgsp2EventAspTable.setStatus(_A)
_Cgsp2EventAspTableEntry_Object=MibTableRow
cgsp2EventAspTableEntry=_Cgsp2EventAspTableEntry_Object((1,3,6,1,4,1,9,9,332,1,1,3,1))
cgsp2EventAspTableEntry.setIndexNames((0,_G,_H),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:cgsp2EventAspTableEntry.setStatus(_A)
_Cgsp2EventAspName_Type=CItpTcXuaName
_Cgsp2EventAspName_Object=MibTableColumn
cgsp2EventAspName=_Cgsp2EventAspName_Object((1,3,6,1,4,1,9,9,332,1,1,3,1,1),_Cgsp2EventAspName_Type())
cgsp2EventAspName.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventAspName.setStatus(_A)
_Cgsp2EventAspIndex_Type=Cgsp2EventIndex
_Cgsp2EventAspIndex_Object=MibTableColumn
cgsp2EventAspIndex=_Cgsp2EventAspIndex_Object((1,3,6,1,4,1,9,9,332,1,1,3,1,2),_Cgsp2EventAspIndex_Type())
cgsp2EventAspIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventAspIndex.setStatus(_A)
class _Cgsp2EventAspText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cgsp2EventAspText_Type.__name__=_I
_Cgsp2EventAspText_Object=MibTableColumn
cgsp2EventAspText=_Cgsp2EventAspText_Object((1,3,6,1,4,1,9,9,332,1,1,3,1,3),_Cgsp2EventAspText_Type())
cgsp2EventAspText.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventAspText.setStatus(_A)
_Cgsp2EventAspTimestamp_Type=TimeStamp
_Cgsp2EventAspTimestamp_Object=MibTableColumn
cgsp2EventAspTimestamp=_Cgsp2EventAspTimestamp_Object((1,3,6,1,4,1,9,9,332,1,1,3,1,4),_Cgsp2EventAspTimestamp_Type())
cgsp2EventAspTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventAspTimestamp.setStatus(_A)
_Cgsp2EventMtp3Table_Object=MibTable
cgsp2EventMtp3Table=_Cgsp2EventMtp3Table_Object((1,3,6,1,4,1,9,9,332,1,1,4))
if mibBuilder.loadTexts:cgsp2EventMtp3Table.setStatus(_A)
_Cgsp2EventMtp3TableEntry_Object=MibTableRow
cgsp2EventMtp3TableEntry=_Cgsp2EventMtp3TableEntry_Object((1,3,6,1,4,1,9,9,332,1,1,4,1))
cgsp2EventMtp3TableEntry.setIndexNames((0,_G,_H),(0,_B,_Y))
if mibBuilder.loadTexts:cgsp2EventMtp3TableEntry.setStatus(_A)
_Cgsp2EventMtp3Index_Type=Cgsp2EventIndex
_Cgsp2EventMtp3Index_Object=MibTableColumn
cgsp2EventMtp3Index=_Cgsp2EventMtp3Index_Object((1,3,6,1,4,1,9,9,332,1,1,4,1,1),_Cgsp2EventMtp3Index_Type())
cgsp2EventMtp3Index.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventMtp3Index.setStatus(_A)
class _Cgsp2EventMtp3Text_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cgsp2EventMtp3Text_Type.__name__=_I
_Cgsp2EventMtp3Text_Object=MibTableColumn
cgsp2EventMtp3Text=_Cgsp2EventMtp3Text_Object((1,3,6,1,4,1,9,9,332,1,1,4,1,2),_Cgsp2EventMtp3Text_Type())
cgsp2EventMtp3Text.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventMtp3Text.setStatus(_A)
_Cgsp2EventMtp3Timestamp_Type=TimeStamp
_Cgsp2EventMtp3Timestamp_Object=MibTableColumn
cgsp2EventMtp3Timestamp=_Cgsp2EventMtp3Timestamp_Object((1,3,6,1,4,1,9,9,332,1,1,4,1,3),_Cgsp2EventMtp3Timestamp_Type())
cgsp2EventMtp3Timestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventMtp3Timestamp.setStatus(_A)
_Cgsp2EventPcTable_Object=MibTable
cgsp2EventPcTable=_Cgsp2EventPcTable_Object((1,3,6,1,4,1,9,9,332,1,1,5))
if mibBuilder.loadTexts:cgsp2EventPcTable.setStatus(_A)
_Cgsp2EventPcTableEntry_Object=MibTableRow
cgsp2EventPcTableEntry=_Cgsp2EventPcTableEntry_Object((1,3,6,1,4,1,9,9,332,1,1,5,1))
cgsp2EventPcTableEntry.setIndexNames((0,_G,_H),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:cgsp2EventPcTableEntry.setStatus(_A)
_Cgsp2EventPc_Type=CItpTcPointCode
_Cgsp2EventPc_Object=MibTableColumn
cgsp2EventPc=_Cgsp2EventPc_Object((1,3,6,1,4,1,9,9,332,1,1,5,1,1),_Cgsp2EventPc_Type())
cgsp2EventPc.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventPc.setStatus(_A)
_Cgsp2EventPcIndex_Type=Cgsp2EventIndex
_Cgsp2EventPcIndex_Object=MibTableColumn
cgsp2EventPcIndex=_Cgsp2EventPcIndex_Object((1,3,6,1,4,1,9,9,332,1,1,5,1,2),_Cgsp2EventPcIndex_Type())
cgsp2EventPcIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2EventPcIndex.setStatus(_A)
class _Cgsp2EventPcText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cgsp2EventPcText_Type.__name__=_I
_Cgsp2EventPcText_Object=MibTableColumn
cgsp2EventPcText=_Cgsp2EventPcText_Object((1,3,6,1,4,1,9,9,332,1,1,5,1,3),_Cgsp2EventPcText_Type())
cgsp2EventPcText.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventPcText.setStatus(_A)
_Cgsp2EventPcTimestamp_Type=TimeStamp
_Cgsp2EventPcTimestamp_Object=MibTableColumn
cgsp2EventPcTimestamp=_Cgsp2EventPcTimestamp_Object((1,3,6,1,4,1,9,9,332,1,1,5,1,4),_Cgsp2EventPcTimestamp_Type())
cgsp2EventPcTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2EventPcTimestamp.setStatus(_A)
_Cgsp2Qos_ObjectIdentity=ObjectIdentity
cgsp2Qos=_Cgsp2Qos_ObjectIdentity((1,3,6,1,4,1,9,9,332,1,2))
_Cgsp2QosTable_Object=MibTable
cgsp2QosTable=_Cgsp2QosTable_Object((1,3,6,1,4,1,9,9,332,1,2,1))
if mibBuilder.loadTexts:cgsp2QosTable.setStatus(_A)
_Cgsp2QosTableEntry_Object=MibTableRow
cgsp2QosTableEntry=_Cgsp2QosTableEntry_Object((1,3,6,1,4,1,9,9,332,1,2,1,1))
cgsp2QosTableEntry.setIndexNames((0,_G,_H),(0,_B,_b))
if mibBuilder.loadTexts:cgsp2QosTableEntry.setStatus(_A)
_Cgsp2QosClass_Type=Cgsp2TcQosClass
_Cgsp2QosClass_Object=MibTableColumn
cgsp2QosClass=_Cgsp2QosClass_Object((1,3,6,1,4,1,9,9,332,1,2,1,1,1),_Cgsp2QosClass_Type())
cgsp2QosClass.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2QosClass.setStatus(_A)
class _Cgsp2QosType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipPrecedence',1),('ipDscp',2)))
_Cgsp2QosType_Type.__name__=_E
_Cgsp2QosType_Object=MibTableColumn
cgsp2QosType=_Cgsp2QosType_Object((1,3,6,1,4,1,9,9,332,1,2,1,1,2),_Cgsp2QosType_Type())
cgsp2QosType.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2QosType.setStatus(_A)
class _Cgsp2QosPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_Cgsp2QosPrecedenceValue_Type.__name__=_E
_Cgsp2QosPrecedenceValue_Object=MibTableColumn
cgsp2QosPrecedenceValue=_Cgsp2QosPrecedenceValue_Object((1,3,6,1,4,1,9,9,332,1,2,1,1,3),_Cgsp2QosPrecedenceValue_Type())
cgsp2QosPrecedenceValue.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2QosPrecedenceValue.setStatus(_A)
class _Cgsp2QosIpDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_Cgsp2QosIpDscp_Type.__name__=_E
_Cgsp2QosIpDscp_Object=MibTableColumn
cgsp2QosIpDscp=_Cgsp2QosIpDscp_Object((1,3,6,1,4,1,9,9,332,1,2,1,1,4),_Cgsp2QosIpDscp_Type())
cgsp2QosIpDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2QosIpDscp.setStatus(_A)
class _Cgsp2QosAclId_Type(CItpTcAclId):defaultValue=0
_Cgsp2QosAclId_Type.__name__=_S
_Cgsp2QosAclId_Object=MibTableColumn
cgsp2QosAclId=_Cgsp2QosAclId_Object((1,3,6,1,4,1,9,9,332,1,2,1,1,5),_Cgsp2QosAclId_Type())
cgsp2QosAclId.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2QosAclId.setStatus(_A)
_Cgsp2QosRowStatus_Type=RowStatus
_Cgsp2QosRowStatus_Object=MibTableColumn
cgsp2QosRowStatus=_Cgsp2QosRowStatus_Object((1,3,6,1,4,1,9,9,332,1,2,1,1,6),_Cgsp2QosRowStatus_Type())
cgsp2QosRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2QosRowStatus.setStatus(_A)
_Cgsp2LocalPeer_ObjectIdentity=ObjectIdentity
cgsp2LocalPeer=_Cgsp2LocalPeer_ObjectIdentity((1,3,6,1,4,1,9,9,332,1,3))
_Cgsp2LocalPeerTable_Object=MibTable
cgsp2LocalPeerTable=_Cgsp2LocalPeerTable_Object((1,3,6,1,4,1,9,9,332,1,3,1))
if mibBuilder.loadTexts:cgsp2LocalPeerTable.setStatus(_A)
_Cgsp2LocalPeerTableEntry_Object=MibTableRow
cgsp2LocalPeerTableEntry=_Cgsp2LocalPeerTableEntry_Object((1,3,6,1,4,1,9,9,332,1,3,1,1))
cgsp2LocalPeerTableEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cgsp2LocalPeerTableEntry.setStatus(_A)
_Cgsp2LocalPeerPort_Type=InetPortNumber
_Cgsp2LocalPeerPort_Object=MibTableColumn
cgsp2LocalPeerPort=_Cgsp2LocalPeerPort_Object((1,3,6,1,4,1,9,9,332,1,3,1,1,1),_Cgsp2LocalPeerPort_Type())
cgsp2LocalPeerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2LocalPeerPort.setStatus(_A)
class _Cgsp2LocalPeerSlotNumber_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,32767))
_Cgsp2LocalPeerSlotNumber_Type.__name__=_E
_Cgsp2LocalPeerSlotNumber_Object=MibTableColumn
cgsp2LocalPeerSlotNumber=_Cgsp2LocalPeerSlotNumber_Object((1,3,6,1,4,1,9,9,332,1,3,1,1,2),_Cgsp2LocalPeerSlotNumber_Type())
cgsp2LocalPeerSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2LocalPeerSlotNumber.setStatus(_A)
_Cgsp2LocalPeerRowStatus_Type=RowStatus
_Cgsp2LocalPeerRowStatus_Object=MibTableColumn
cgsp2LocalPeerRowStatus=_Cgsp2LocalPeerRowStatus_Object((1,3,6,1,4,1,9,9,332,1,3,1,1,3),_Cgsp2LocalPeerRowStatus_Type())
cgsp2LocalPeerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2LocalPeerRowStatus.setStatus(_A)
class _Cgsp2LocalPeerProcessorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Cgsp2LocalPeerProcessorNumber_Type.__name__=_E
_Cgsp2LocalPeerProcessorNumber_Object=MibTableColumn
cgsp2LocalPeerProcessorNumber=_Cgsp2LocalPeerProcessorNumber_Object((1,3,6,1,4,1,9,9,332,1,3,1,1,4),_Cgsp2LocalPeerProcessorNumber_Type())
cgsp2LocalPeerProcessorNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2LocalPeerProcessorNumber.setStatus(_A)
_Cgsp2LpIpAddrTable_Object=MibTable
cgsp2LpIpAddrTable=_Cgsp2LpIpAddrTable_Object((1,3,6,1,4,1,9,9,332,1,3,2))
if mibBuilder.loadTexts:cgsp2LpIpAddrTable.setStatus(_A)
_Cgsp2LpIpAddrTableEntry_Object=MibTableRow
cgsp2LpIpAddrTableEntry=_Cgsp2LpIpAddrTableEntry_Object((1,3,6,1,4,1,9,9,332,1,3,2,1))
cgsp2LpIpAddrTableEntry.setIndexNames((0,_B,_Q),(0,_B,_c))
if mibBuilder.loadTexts:cgsp2LpIpAddrTableEntry.setStatus(_A)
class _Cgsp2LpIpAddressNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Cgsp2LpIpAddressNumber_Type.__name__=_L
_Cgsp2LpIpAddressNumber_Object=MibTableColumn
cgsp2LpIpAddressNumber=_Cgsp2LpIpAddressNumber_Object((1,3,6,1,4,1,9,9,332,1,3,2,1,1),_Cgsp2LpIpAddressNumber_Type())
cgsp2LpIpAddressNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2LpIpAddressNumber.setStatus(_A)
_Cgsp2LpIpAddressType_Type=InetAddressType
_Cgsp2LpIpAddressType_Object=MibTableColumn
cgsp2LpIpAddressType=_Cgsp2LpIpAddressType_Object((1,3,6,1,4,1,9,9,332,1,3,2,1,2),_Cgsp2LpIpAddressType_Type())
cgsp2LpIpAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2LpIpAddressType.setStatus(_A)
_Cgsp2LpIpAddress_Type=InetAddress
_Cgsp2LpIpAddress_Object=MibTableColumn
cgsp2LpIpAddress=_Cgsp2LpIpAddress_Object((1,3,6,1,4,1,9,9,332,1,3,2,1,3),_Cgsp2LpIpAddress_Type())
cgsp2LpIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2LpIpAddress.setStatus(_A)
_Cgsp2LpIpAddressRowStatus_Type=RowStatus
_Cgsp2LpIpAddressRowStatus_Object=MibTableColumn
cgsp2LpIpAddressRowStatus=_Cgsp2LpIpAddressRowStatus_Object((1,3,6,1,4,1,9,9,332,1,3,2,1,4),_Cgsp2LpIpAddressRowStatus_Type())
cgsp2LpIpAddressRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cgsp2LpIpAddressRowStatus.setStatus(_A)
_Cgsp2Mtp3Errors_ObjectIdentity=ObjectIdentity
cgsp2Mtp3Errors=_Cgsp2Mtp3Errors_ObjectIdentity((1,3,6,1,4,1,9,9,332,1,4))
_Cgsp2Mtp3ErrorsTable_Object=MibTable
cgsp2Mtp3ErrorsTable=_Cgsp2Mtp3ErrorsTable_Object((1,3,6,1,4,1,9,9,332,1,4,1))
if mibBuilder.loadTexts:cgsp2Mtp3ErrorsTable.setStatus(_A)
_Cgsp2Mtp3ErrorsTableEntry_Object=MibTableRow
cgsp2Mtp3ErrorsTableEntry=_Cgsp2Mtp3ErrorsTableEntry_Object((1,3,6,1,4,1,9,9,332,1,4,1,1))
cgsp2Mtp3ErrorsTableEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:cgsp2Mtp3ErrorsTableEntry.setStatus(_A)
class _Cgsp2Mtp3ErrorsType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cgsp2Mtp3ErrorsType_Type.__name__=_L
_Cgsp2Mtp3ErrorsType_Object=MibTableColumn
cgsp2Mtp3ErrorsType=_Cgsp2Mtp3ErrorsType_Object((1,3,6,1,4,1,9,9,332,1,4,1,1,1),_Cgsp2Mtp3ErrorsType_Type())
cgsp2Mtp3ErrorsType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2Mtp3ErrorsType.setStatus(_A)
class _Cgsp2Mtp3ErrorsDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cgsp2Mtp3ErrorsDescription_Type.__name__=_I
_Cgsp2Mtp3ErrorsDescription_Object=MibTableColumn
cgsp2Mtp3ErrorsDescription=_Cgsp2Mtp3ErrorsDescription_Object((1,3,6,1,4,1,9,9,332,1,4,1,1,2),_Cgsp2Mtp3ErrorsDescription_Type())
cgsp2Mtp3ErrorsDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2Mtp3ErrorsDescription.setStatus(_A)
_Cgsp2Mtp3ErrorsCount_Type=Counter64
_Cgsp2Mtp3ErrorsCount_Object=MibTableColumn
cgsp2Mtp3ErrorsCount=_Cgsp2Mtp3ErrorsCount_Object((1,3,6,1,4,1,9,9,332,1,4,1,1,3),_Cgsp2Mtp3ErrorsCount_Type())
cgsp2Mtp3ErrorsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2Mtp3ErrorsCount.setStatus(_A)
_Cgsp2Operation_ObjectIdentity=ObjectIdentity
cgsp2Operation=_Cgsp2Operation_ObjectIdentity((1,3,6,1,4,1,9,9,332,1,5))
class _Cgsp2OperMtp3Offload_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),('offload',2)))
_Cgsp2OperMtp3Offload_Type.__name__=_E
_Cgsp2OperMtp3Offload_Object=MibScalar
cgsp2OperMtp3Offload=_Cgsp2OperMtp3Offload_Object((1,3,6,1,4,1,9,9,332,1,5,1),_Cgsp2OperMtp3Offload_Type())
cgsp2OperMtp3Offload.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2OperMtp3Offload.setStatus(_A)
class _Cgsp2OperRedundancy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('local',2),('distributed',3)))
_Cgsp2OperRedundancy_Type.__name__=_E
_Cgsp2OperRedundancy_Object=MibScalar
cgsp2OperRedundancy=_Cgsp2OperRedundancy_Object((1,3,6,1,4,1,9,9,332,1,5,2),_Cgsp2OperRedundancy_Type())
cgsp2OperRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2OperRedundancy.setStatus(_A)
_Cgsp2Context_ObjectIdentity=ObjectIdentity
cgsp2Context=_Cgsp2Context_ObjectIdentity((1,3,6,1,4,1,9,9,332,1,6))
_Cgsp2ContextTable_Object=MibTable
cgsp2ContextTable=_Cgsp2ContextTable_Object((1,3,6,1,4,1,9,9,332,1,6,1))
if mibBuilder.loadTexts:cgsp2ContextTable.setStatus(_A)
_Cgsp2ContextEntry_Object=MibTableRow
cgsp2ContextEntry=_Cgsp2ContextEntry_Object((1,3,6,1,4,1,9,9,332,1,6,1,1))
cgsp2ContextEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:cgsp2ContextEntry.setStatus(_A)
_Cgsp2ContextIdentifier_Type=CItpTcContextId
_Cgsp2ContextIdentifier_Object=MibTableColumn
cgsp2ContextIdentifier=_Cgsp2ContextIdentifier_Object((1,3,6,1,4,1,9,9,332,1,6,1,1,1),_Cgsp2ContextIdentifier_Type())
cgsp2ContextIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsp2ContextIdentifier.setStatus(_A)
_Cgsp2ContextType_Type=CItpTcContextType
_Cgsp2ContextType_Object=MibTableColumn
cgsp2ContextType=_Cgsp2ContextType_Object((1,3,6,1,4,1,9,9,332,1,6,1,1,2),_Cgsp2ContextType_Type())
cgsp2ContextType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2ContextType.setStatus(_A)
_Cgsp2ContextLinksetName_Type=CItpTcLinksetId
_Cgsp2ContextLinksetName_Object=MibTableColumn
cgsp2ContextLinksetName=_Cgsp2ContextLinksetName_Object((1,3,6,1,4,1,9,9,332,1,6,1,1,3),_Cgsp2ContextLinksetName_Type())
cgsp2ContextLinksetName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2ContextLinksetName.setStatus(_A)
_Cgsp2ContextSlc_Type=CItpTcLinkSLC
_Cgsp2ContextSlc_Object=MibTableColumn
cgsp2ContextSlc=_Cgsp2ContextSlc_Object((1,3,6,1,4,1,9,9,332,1,6,1,1,4),_Cgsp2ContextSlc_Type())
cgsp2ContextSlc.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2ContextSlc.setStatus(_A)
_Cgsp2ContextAsName_Type=CItpTcXuaName
_Cgsp2ContextAsName_Object=MibTableColumn
cgsp2ContextAsName=_Cgsp2ContextAsName_Object((1,3,6,1,4,1,9,9,332,1,6,1,1,5),_Cgsp2ContextAsName_Type())
cgsp2ContextAsName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2ContextAsName.setStatus(_A)
_Cgsp2ContextAspName_Type=CItpTcXuaName
_Cgsp2ContextAspName_Object=MibTableColumn
cgsp2ContextAspName=_Cgsp2ContextAspName_Object((1,3,6,1,4,1,9,9,332,1,6,1,1,6),_Cgsp2ContextAspName_Type())
cgsp2ContextAspName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2ContextAspName.setStatus(_A)
_Cgsp2ContextNetworkName_Type=CItpTcNetworkName
_Cgsp2ContextNetworkName_Object=MibTableColumn
cgsp2ContextNetworkName=_Cgsp2ContextNetworkName_Object((1,3,6,1,4,1,9,9,332,1,6,1,1,7),_Cgsp2ContextNetworkName_Type())
cgsp2ContextNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsp2ContextNetworkName.setStatus(_A)
_CiscoGsp2MIBConform_ObjectIdentity=ObjectIdentity
ciscoGsp2MIBConform=_CiscoGsp2MIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,332,2))
_CiscoGsp2MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGsp2MIBCompliances=_CiscoGsp2MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,332,2,1))
_CiscoGsp2MIBGroups_ObjectIdentity=ObjectIdentity
ciscoGsp2MIBGroups=_CiscoGsp2MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,332,2,2))
ciscoGsp2EventsGroup=ObjectGroup((1,3,6,1,4,1,9,9,332,2,2,1))
ciscoGsp2EventsGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoGsp2EventsGroup.setStatus(_A)
ciscoGsp2QosGroup=ObjectGroup((1,3,6,1,4,1,9,9,332,2,2,2))
ciscoGsp2QosGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ciscoGsp2QosGroup.setStatus(_A)
ciscoGsp2LocalPeerGroup=ObjectGroup((1,3,6,1,4,1,9,9,332,2,2,3))
ciscoGsp2LocalPeerGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ciscoGsp2LocalPeerGroup.setStatus(_A)
ciscoGsp2Mtp3ErrorsGroup=ObjectGroup((1,3,6,1,4,1,9,9,332,2,2,4))
ciscoGsp2Mtp3ErrorsGroup.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ciscoGsp2Mtp3ErrorsGroup.setStatus(_A)
ciscoGsp2OperationGroup=ObjectGroup((1,3,6,1,4,1,9,9,332,2,2,5))
ciscoGsp2OperationGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoGsp2OperationGroup.setStatus(_A)
ciscoGsp2LocalPeerGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,332,2,2,6))
ciscoGsp2LocalPeerGroupSup1.setObjects((_B,_A5))
if mibBuilder.loadTexts:ciscoGsp2LocalPeerGroupSup1.setStatus(_A)
ciscoGsp2ContextGroup=ObjectGroup((1,3,6,1,4,1,9,9,332,2,2,7))
ciscoGsp2ContextGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ciscoGsp2ContextGroup.setStatus(_A)
ciscoGsp2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,332,2,1,1))
ciscoGsp2MIBCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_M)))
if mibBuilder.loadTexts:ciscoGsp2MIBCompliance.setStatus(_O)
ciscoGsp2MIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,332,2,1,2))
ciscoGsp2MIBComplianceRev1.setObjects(*((_B,_J),(_B,_K),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoGsp2MIBComplianceRev1.setStatus(_O)
ciscoGsp2MIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,332,2,1,3))
ciscoGsp2MIBComplianceRev2.setObjects(*((_B,_J),(_B,_K),(_B,_M),(_B,_N),(_B,_P)))
if mibBuilder.loadTexts:ciscoGsp2MIBComplianceRev2.setStatus(_O)
ciscoGsp2MIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,332,2,1,4))
ciscoGsp2MIBComplianceRev3.setObjects(*((_B,_J),(_B,_K),(_B,_N),(_B,_P),(_B,_R)))
if mibBuilder.loadTexts:ciscoGsp2MIBComplianceRev3.setStatus(_O)
ciscoGsp2MIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,332,2,1,5))
ciscoGsp2MIBComplianceRev4.setObjects(*((_B,_J),(_B,_K),(_B,_M),(_B,_N),(_B,_P),(_B,_R),(_B,_AC)))
if mibBuilder.loadTexts:ciscoGsp2MIBComplianceRev4.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Cgsp2TcQosClass':Cgsp2TcQosClass,'Cgsp2EventIndex':Cgsp2EventIndex,'CItpTcContextId':CItpTcContextId,'CItpTcContextType':CItpTcContextType,'ciscoGsp2MIB':ciscoGsp2MIB,'ciscoGsp2MIBNotifs':ciscoGsp2MIBNotifs,'ciscoGsp2MIBObjects':ciscoGsp2MIBObjects,'cgsp2Events':cgsp2Events,'cgsp2EventTable':cgsp2EventTable,'cgsp2EventTableEntry':cgsp2EventTableEntry,_T:cgsp2EventType,_f:cgsp2EventLoggedEvents,_g:cgsp2EventDroppedEvents,_h:cgsp2EventMaxEntries,_i:cgsp2EventMaxEntriesAllowed,'cgsp2EventAsTable':cgsp2EventAsTable,'cgsp2EventAsTableEntry':cgsp2EventAsTableEntry,_U:cgsp2EventAsName,_V:cgsp2EventAsIndex,_l:cgsp2EventAsText,_m:cgsp2EventAsTimestamp,'cgsp2EventAspTable':cgsp2EventAspTable,'cgsp2EventAspTableEntry':cgsp2EventAspTableEntry,_W:cgsp2EventAspName,_X:cgsp2EventAspIndex,_n:cgsp2EventAspText,_o:cgsp2EventAspTimestamp,'cgsp2EventMtp3Table':cgsp2EventMtp3Table,'cgsp2EventMtp3TableEntry':cgsp2EventMtp3TableEntry,_Y:cgsp2EventMtp3Index,_j:cgsp2EventMtp3Text,_k:cgsp2EventMtp3Timestamp,'cgsp2EventPcTable':cgsp2EventPcTable,'cgsp2EventPcTableEntry':cgsp2EventPcTableEntry,_Z:cgsp2EventPc,_a:cgsp2EventPcIndex,_p:cgsp2EventPcText,_q:cgsp2EventPcTimestamp,'cgsp2Qos':cgsp2Qos,'cgsp2QosTable':cgsp2QosTable,'cgsp2QosTableEntry':cgsp2QosTableEntry,_b:cgsp2QosClass,_r:cgsp2QosType,_s:cgsp2QosPrecedenceValue,_t:cgsp2QosIpDscp,_u:cgsp2QosAclId,_v:cgsp2QosRowStatus,'cgsp2LocalPeer':cgsp2LocalPeer,'cgsp2LocalPeerTable':cgsp2LocalPeerTable,'cgsp2LocalPeerTableEntry':cgsp2LocalPeerTableEntry,_Q:cgsp2LocalPeerPort,_w:cgsp2LocalPeerSlotNumber,_x:cgsp2LocalPeerRowStatus,_A5:cgsp2LocalPeerProcessorNumber,'cgsp2LpIpAddrTable':cgsp2LpIpAddrTable,'cgsp2LpIpAddrTableEntry':cgsp2LpIpAddrTableEntry,_c:cgsp2LpIpAddressNumber,_y:cgsp2LpIpAddressType,_z:cgsp2LpIpAddress,_A0:cgsp2LpIpAddressRowStatus,'cgsp2Mtp3Errors':cgsp2Mtp3Errors,'cgsp2Mtp3ErrorsTable':cgsp2Mtp3ErrorsTable,'cgsp2Mtp3ErrorsTableEntry':cgsp2Mtp3ErrorsTableEntry,_d:cgsp2Mtp3ErrorsType,_A1:cgsp2Mtp3ErrorsDescription,_A2:cgsp2Mtp3ErrorsCount,'cgsp2Operation':cgsp2Operation,_A3:cgsp2OperMtp3Offload,_A4:cgsp2OperRedundancy,'cgsp2Context':cgsp2Context,'cgsp2ContextTable':cgsp2ContextTable,'cgsp2ContextEntry':cgsp2ContextEntry,_e:cgsp2ContextIdentifier,_A6:cgsp2ContextType,_A7:cgsp2ContextLinksetName,_A8:cgsp2ContextSlc,_A9:cgsp2ContextAsName,_AA:cgsp2ContextAspName,_AB:cgsp2ContextNetworkName,'ciscoGsp2MIBConform':ciscoGsp2MIBConform,'ciscoGsp2MIBCompliances':ciscoGsp2MIBCompliances,'ciscoGsp2MIBCompliance':ciscoGsp2MIBCompliance,'ciscoGsp2MIBComplianceRev1':ciscoGsp2MIBComplianceRev1,'ciscoGsp2MIBComplianceRev2':ciscoGsp2MIBComplianceRev2,'ciscoGsp2MIBComplianceRev3':ciscoGsp2MIBComplianceRev3,'ciscoGsp2MIBComplianceRev4':ciscoGsp2MIBComplianceRev4,'ciscoGsp2MIBGroups':ciscoGsp2MIBGroups,_J:ciscoGsp2EventsGroup,_K:ciscoGsp2QosGroup,_M:ciscoGsp2LocalPeerGroup,_N:ciscoGsp2Mtp3ErrorsGroup,_P:ciscoGsp2OperationGroup,_R:ciscoGsp2LocalPeerGroupSup1,_AC:ciscoGsp2ContextGroup})