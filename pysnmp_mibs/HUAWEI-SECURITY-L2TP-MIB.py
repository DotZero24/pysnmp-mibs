_A5='hwL2tpTrapGroup'
_A4='hwL2tpTrapObjectGroup'
_A3='hwL2tpSessionTableGroup'
_A2='hwL2tpTunnelTableGroup'
_A1='hwL2tpGroupConfigTableGroup'
_A0='hwL2tpSessionStop'
_z='hwL2tpSessionStart'
_y='hwL2tpSessionSerialNumber'
_x='hwL2tpSessionCallType'
_w='hwL2tpSessionState'
_v='hwL2tpSessionUserOnlineTime'
_u='hwL2tpSessionUserName'
_t='hwL2tpSessionRemoteSID'
_s='hwL2tpSessionLocalSID'
_r='hwL2tpSessionTunnelID'
_q='hwL2tpLnsGroupRowStatus'
_p='hwL2tpTunnelSessionNum'
_o='hwL2tpTunnelRemotePort'
_n='hwL2tpTunnelRemoteIP'
_m='hwL2tpTunnelRemoteName'
_l='hwL2tpTunnelRemoteID'
_k='hwL2tpTunnelLocalID'
_j='hwL2tpGroupRowStatus'
_i='hwL2tpGroupVt'
_h='hwL2tpGroupForceLcp'
_g='hwL2tpGroupForceChap'
_f='hwL2tpGroupLnsIP5'
_e='hwL2tpGroupLnsIP4'
_d='hwL2tpGroupLnsIP3'
_c='hwL2tpGroupLnsIP2'
_b='hwL2tpGroupLnsIP1'
_a='hwL2tpGroupTimer'
_Z='hwL2tpGroupTimeout'
_Y='hwL2tpGroupRetransmit'
_X='hwL2tpGroupRemoteName'
_W='hwL2tpGroupName'
_V='hwL2tpGroupAvpHidden'
_U='hwL2tpGroupPassWord'
_T='hwL2tpGroupAuthentication'
_S='hwL2tpGroupFlag'
_R='hwL2tpTunnelNumber'
_Q='hwL2tpSessionIndex'
_P='hwL2tpTunnelIndex'
_O='hwL2tpGroupindex'
_N='not-accessible'
_M='TruthValue'
_L='hwL2tpTunnelStartTime'
_K='hwL2tpTunnelUserName'
_J='hwL2tpTunnelRemoteAddr'
_I='hwL2tpSessionindex'
_H='hwL2tpTunnelindex'
_G='OctetString'
_F='accessible-for-notify'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='current'
_A='HUAWEI-SECURITY-L2TP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval',_M)
hwL2tpMib=ModuleIdentity((1,3,6,1,4,1,2011,6,122,2))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_HuaweiUtility_ObjectIdentity=ObjectIdentity
huaweiUtility=_HuaweiUtility_ObjectIdentity((1,3,6,1,4,1,2011,6))
_HwSecurity_ObjectIdentity=ObjectIdentity
hwSecurity=_HwSecurity_ObjectIdentity((1,3,6,1,4,1,2011,6,122))
_HwL2tpMibObjects_ObjectIdentity=ObjectIdentity
hwL2tpMibObjects=_HwL2tpMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,6,122,2,1))
_HwL2tpEnableFlag_Type=TruthValue
_HwL2tpEnableFlag_Object=MibScalar
hwL2tpEnableFlag=_HwL2tpEnableFlag_Object((1,3,6,1,4,1,2011,6,122,2,1,1),_HwL2tpEnableFlag_Type())
hwL2tpEnableFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpEnableFlag.setStatus(_B)
_HwL2tpGroupConfigTable_Object=MibTable
hwL2tpGroupConfigTable=_HwL2tpGroupConfigTable_Object((1,3,6,1,4,1,2011,6,122,2,1,2))
if mibBuilder.loadTexts:hwL2tpGroupConfigTable.setStatus(_B)
_HwL2tpGroupConfigEntry_Object=MibTableRow
hwL2tpGroupConfigEntry=_HwL2tpGroupConfigEntry_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1))
hwL2tpGroupConfigEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:hwL2tpGroupConfigEntry.setStatus(_B)
class _HwL2tpGroupindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HwL2tpGroupindex_Type.__name__=_D
_HwL2tpGroupindex_Object=MibTableColumn
hwL2tpGroupindex=_HwL2tpGroupindex_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,1),_HwL2tpGroupindex_Type())
hwL2tpGroupindex.setMaxAccess(_N)
if mibBuilder.loadTexts:hwL2tpGroupindex.setStatus(_B)
class _HwL2tpTunnelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HwL2tpTunnelNumber_Type.__name__=_D
_HwL2tpTunnelNumber_Object=MibTableColumn
hwL2tpTunnelNumber=_HwL2tpTunnelNumber_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,2),_HwL2tpTunnelNumber_Type())
hwL2tpTunnelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpTunnelNumber.setStatus(_B)
class _HwL2tpGroupFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwL2tpGroupFlag_Type.__name__=_D
_HwL2tpGroupFlag_Object=MibTableColumn
hwL2tpGroupFlag=_HwL2tpGroupFlag_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,3),_HwL2tpGroupFlag_Type())
hwL2tpGroupFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpGroupFlag.setStatus(_B)
class _HwL2tpGroupAuthentication_Type(TruthValue):defaultValue=1
_HwL2tpGroupAuthentication_Type.__name__=_M
_HwL2tpGroupAuthentication_Object=MibTableColumn
hwL2tpGroupAuthentication=_HwL2tpGroupAuthentication_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,4),_HwL2tpGroupAuthentication_Type())
hwL2tpGroupAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupAuthentication.setStatus(_B)
class _HwL2tpGroupPassWord_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HwL2tpGroupPassWord_Type.__name__=_G
_HwL2tpGroupPassWord_Object=MibTableColumn
hwL2tpGroupPassWord=_HwL2tpGroupPassWord_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,5),_HwL2tpGroupPassWord_Type())
hwL2tpGroupPassWord.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupPassWord.setStatus(_B)
class _HwL2tpGroupAvpHidden_Type(TruthValue):defaultValue=2
_HwL2tpGroupAvpHidden_Type.__name__=_M
_HwL2tpGroupAvpHidden_Object=MibTableColumn
hwL2tpGroupAvpHidden=_HwL2tpGroupAvpHidden_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,6),_HwL2tpGroupAvpHidden_Type())
hwL2tpGroupAvpHidden.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupAvpHidden.setStatus(_B)
class _HwL2tpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_HwL2tpGroupName_Type.__name__=_G
_HwL2tpGroupName_Object=MibTableColumn
hwL2tpGroupName=_HwL2tpGroupName_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,7),_HwL2tpGroupName_Type())
hwL2tpGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupName.setStatus(_B)
class _HwL2tpGroupRemoteName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_HwL2tpGroupRemoteName_Type.__name__=_G
_HwL2tpGroupRemoteName_Object=MibTableColumn
hwL2tpGroupRemoteName=_HwL2tpGroupRemoteName_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,8),_HwL2tpGroupRemoteName_Type())
hwL2tpGroupRemoteName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupRemoteName.setStatus(_B)
class _HwL2tpGroupRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HwL2tpGroupRetransmit_Type.__name__=_D
_HwL2tpGroupRetransmit_Object=MibTableColumn
hwL2tpGroupRetransmit=_HwL2tpGroupRetransmit_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,9),_HwL2tpGroupRetransmit_Type())
hwL2tpGroupRetransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupRetransmit.setStatus(_B)
_HwL2tpGroupTimeout_Type=TimeInterval
_HwL2tpGroupTimeout_Object=MibTableColumn
hwL2tpGroupTimeout=_HwL2tpGroupTimeout_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,10),_HwL2tpGroupTimeout_Type())
hwL2tpGroupTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupTimeout.setStatus(_B)
_HwL2tpGroupTimer_Type=TimeInterval
_HwL2tpGroupTimer_Object=MibTableColumn
hwL2tpGroupTimer=_HwL2tpGroupTimer_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,11),_HwL2tpGroupTimer_Type())
hwL2tpGroupTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupTimer.setStatus(_B)
_HwL2tpGroupLnsIP1_Type=IpAddress
_HwL2tpGroupLnsIP1_Object=MibTableColumn
hwL2tpGroupLnsIP1=_HwL2tpGroupLnsIP1_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,12),_HwL2tpGroupLnsIP1_Type())
hwL2tpGroupLnsIP1.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupLnsIP1.setStatus(_B)
_HwL2tpGroupLnsIP2_Type=IpAddress
_HwL2tpGroupLnsIP2_Object=MibTableColumn
hwL2tpGroupLnsIP2=_HwL2tpGroupLnsIP2_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,13),_HwL2tpGroupLnsIP2_Type())
hwL2tpGroupLnsIP2.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupLnsIP2.setStatus(_B)
_HwL2tpGroupLnsIP3_Type=IpAddress
_HwL2tpGroupLnsIP3_Object=MibTableColumn
hwL2tpGroupLnsIP3=_HwL2tpGroupLnsIP3_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,14),_HwL2tpGroupLnsIP3_Type())
hwL2tpGroupLnsIP3.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupLnsIP3.setStatus(_B)
_HwL2tpGroupLnsIP4_Type=IpAddress
_HwL2tpGroupLnsIP4_Object=MibTableColumn
hwL2tpGroupLnsIP4=_HwL2tpGroupLnsIP4_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,15),_HwL2tpGroupLnsIP4_Type())
hwL2tpGroupLnsIP4.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupLnsIP4.setStatus(_B)
_HwL2tpGroupLnsIP5_Type=IpAddress
_HwL2tpGroupLnsIP5_Object=MibTableColumn
hwL2tpGroupLnsIP5=_HwL2tpGroupLnsIP5_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,16),_HwL2tpGroupLnsIP5_Type())
hwL2tpGroupLnsIP5.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupLnsIP5.setStatus(_B)
_HwL2tpGroupForceChap_Type=TruthValue
_HwL2tpGroupForceChap_Object=MibTableColumn
hwL2tpGroupForceChap=_HwL2tpGroupForceChap_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,17),_HwL2tpGroupForceChap_Type())
hwL2tpGroupForceChap.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupForceChap.setStatus(_B)
_HwL2tpGroupForceLcp_Type=TruthValue
_HwL2tpGroupForceLcp_Object=MibTableColumn
hwL2tpGroupForceLcp=_HwL2tpGroupForceLcp_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,18),_HwL2tpGroupForceLcp_Type())
hwL2tpGroupForceLcp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupForceLcp.setStatus(_B)
class _HwL2tpGroupVt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023),ValueRangeConstraint(65535,65535))
_HwL2tpGroupVt_Type.__name__=_D
_HwL2tpGroupVt_Object=MibTableColumn
hwL2tpGroupVt=_HwL2tpGroupVt_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,19),_HwL2tpGroupVt_Type())
hwL2tpGroupVt.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupVt.setStatus(_B)
_HwL2tpGroupRowStatus_Type=RowStatus
_HwL2tpGroupRowStatus_Object=MibTableColumn
hwL2tpGroupRowStatus=_HwL2tpGroupRowStatus_Object((1,3,6,1,4,1,2011,6,122,2,1,2,1,20),_HwL2tpGroupRowStatus_Type())
hwL2tpGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpGroupRowStatus.setStatus(_B)
_HwL2tpTunnelTable_Object=MibTable
hwL2tpTunnelTable=_HwL2tpTunnelTable_Object((1,3,6,1,4,1,2011,6,122,2,1,3))
if mibBuilder.loadTexts:hwL2tpTunnelTable.setStatus(_B)
_HwL2tpTunnelEntry_Object=MibTableRow
hwL2tpTunnelEntry=_HwL2tpTunnelEntry_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1))
hwL2tpTunnelEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:hwL2tpTunnelEntry.setStatus(_B)
class _HwL2tpTunnelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwL2tpTunnelIndex_Type.__name__=_D
_HwL2tpTunnelIndex_Object=MibTableColumn
hwL2tpTunnelIndex=_HwL2tpTunnelIndex_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,1),_HwL2tpTunnelIndex_Type())
hwL2tpTunnelIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:hwL2tpTunnelIndex.setStatus(_B)
class _HwL2tpTunnelLocalID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwL2tpTunnelLocalID_Type.__name__=_D
_HwL2tpTunnelLocalID_Object=MibTableColumn
hwL2tpTunnelLocalID=_HwL2tpTunnelLocalID_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,2),_HwL2tpTunnelLocalID_Type())
hwL2tpTunnelLocalID.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpTunnelLocalID.setStatus(_B)
class _HwL2tpTunnelRemoteID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwL2tpTunnelRemoteID_Type.__name__=_D
_HwL2tpTunnelRemoteID_Object=MibTableColumn
hwL2tpTunnelRemoteID=_HwL2tpTunnelRemoteID_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,3),_HwL2tpTunnelRemoteID_Type())
hwL2tpTunnelRemoteID.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpTunnelRemoteID.setStatus(_B)
_HwL2tpTunnelRemoteName_Type=OctetString
_HwL2tpTunnelRemoteName_Object=MibTableColumn
hwL2tpTunnelRemoteName=_HwL2tpTunnelRemoteName_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,4),_HwL2tpTunnelRemoteName_Type())
hwL2tpTunnelRemoteName.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpTunnelRemoteName.setStatus(_B)
_HwL2tpTunnelRemoteIP_Type=IpAddress
_HwL2tpTunnelRemoteIP_Object=MibTableColumn
hwL2tpTunnelRemoteIP=_HwL2tpTunnelRemoteIP_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,5),_HwL2tpTunnelRemoteIP_Type())
hwL2tpTunnelRemoteIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpTunnelRemoteIP.setStatus(_B)
class _HwL2tpTunnelRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwL2tpTunnelRemotePort_Type.__name__=_D
_HwL2tpTunnelRemotePort_Object=MibTableColumn
hwL2tpTunnelRemotePort=_HwL2tpTunnelRemotePort_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,6),_HwL2tpTunnelRemotePort_Type())
hwL2tpTunnelRemotePort.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpTunnelRemotePort.setStatus(_B)
class _HwL2tpTunnelSessionNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwL2tpTunnelSessionNum_Type.__name__=_D
_HwL2tpTunnelSessionNum_Object=MibTableColumn
hwL2tpTunnelSessionNum=_HwL2tpTunnelSessionNum_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,7),_HwL2tpTunnelSessionNum_Type())
hwL2tpTunnelSessionNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpTunnelSessionNum.setStatus(_B)
_HwL2tpLnsGroupRowStatus_Type=RowStatus
_HwL2tpLnsGroupRowStatus_Object=MibTableColumn
hwL2tpLnsGroupRowStatus=_HwL2tpLnsGroupRowStatus_Object((1,3,6,1,4,1,2011,6,122,2,1,3,1,8),_HwL2tpLnsGroupRowStatus_Type())
hwL2tpLnsGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwL2tpLnsGroupRowStatus.setStatus(_B)
_HwL2tpSessionTable_Object=MibTable
hwL2tpSessionTable=_HwL2tpSessionTable_Object((1,3,6,1,4,1,2011,6,122,2,1,4))
if mibBuilder.loadTexts:hwL2tpSessionTable.setStatus(_B)
_HwL2tpSessionEntry_Object=MibTableRow
hwL2tpSessionEntry=_HwL2tpSessionEntry_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1))
hwL2tpSessionEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:hwL2tpSessionEntry.setStatus(_B)
class _HwL2tpSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwL2tpSessionIndex_Type.__name__=_D
_HwL2tpSessionIndex_Object=MibTableColumn
hwL2tpSessionIndex=_HwL2tpSessionIndex_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,1),_HwL2tpSessionIndex_Type())
hwL2tpSessionIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:hwL2tpSessionIndex.setStatus(_B)
class _HwL2tpSessionTunnelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwL2tpSessionTunnelID_Type.__name__=_D
_HwL2tpSessionTunnelID_Object=MibTableColumn
hwL2tpSessionTunnelID=_HwL2tpSessionTunnelID_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,2),_HwL2tpSessionTunnelID_Type())
hwL2tpSessionTunnelID.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionTunnelID.setStatus(_B)
class _HwL2tpSessionLocalSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwL2tpSessionLocalSID_Type.__name__=_D
_HwL2tpSessionLocalSID_Object=MibTableColumn
hwL2tpSessionLocalSID=_HwL2tpSessionLocalSID_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,3),_HwL2tpSessionLocalSID_Type())
hwL2tpSessionLocalSID.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionLocalSID.setStatus(_B)
class _HwL2tpSessionRemoteSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwL2tpSessionRemoteSID_Type.__name__=_D
_HwL2tpSessionRemoteSID_Object=MibTableColumn
hwL2tpSessionRemoteSID=_HwL2tpSessionRemoteSID_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,4),_HwL2tpSessionRemoteSID_Type())
hwL2tpSessionRemoteSID.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionRemoteSID.setStatus(_B)
_HwL2tpSessionUserName_Type=OctetString
_HwL2tpSessionUserName_Object=MibTableColumn
hwL2tpSessionUserName=_HwL2tpSessionUserName_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,5),_HwL2tpSessionUserName_Type())
hwL2tpSessionUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionUserName.setStatus(_B)
_HwL2tpSessionUserOnlineTime_Type=DateAndTime
_HwL2tpSessionUserOnlineTime_Object=MibTableColumn
hwL2tpSessionUserOnlineTime=_HwL2tpSessionUserOnlineTime_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,6),_HwL2tpSessionUserOnlineTime_Type())
hwL2tpSessionUserOnlineTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionUserOnlineTime.setStatus(_B)
class _HwL2tpSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sessionIdle',1),('sessionConnecting',2),('sessionEstablished',3),('sessionDisconnecting',4)))
_HwL2tpSessionState_Type.__name__=_D
_HwL2tpSessionState_Object=MibTableColumn
hwL2tpSessionState=_HwL2tpSessionState_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,7),_HwL2tpSessionState_Type())
hwL2tpSessionState.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionState.setStatus(_B)
class _HwL2tpSessionCallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lacIncoming',1),('lnsIncoming',2),('lacOutgoing',3),('lnsOutgoing',4)))
_HwL2tpSessionCallType_Type.__name__=_D
_HwL2tpSessionCallType_Object=MibTableColumn
hwL2tpSessionCallType=_HwL2tpSessionCallType_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,8),_HwL2tpSessionCallType_Type())
hwL2tpSessionCallType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionCallType.setStatus(_B)
_HwL2tpSessionSerialNumber_Type=Unsigned32
_HwL2tpSessionSerialNumber_Object=MibTableColumn
hwL2tpSessionSerialNumber=_HwL2tpSessionSerialNumber_Object((1,3,6,1,4,1,2011,6,122,2,1,4,1,9),_HwL2tpSessionSerialNumber_Type())
hwL2tpSessionSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwL2tpSessionSerialNumber.setStatus(_B)
_HwL2tpTrapObject_ObjectIdentity=ObjectIdentity
hwL2tpTrapObject=_HwL2tpTrapObject_ObjectIdentity((1,3,6,1,4,1,2011,6,122,2,1,7))
class _HwL2tpTunnelindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwL2tpTunnelindex_Type.__name__=_D
_HwL2tpTunnelindex_Object=MibScalar
hwL2tpTunnelindex=_HwL2tpTunnelindex_Object((1,3,6,1,4,1,2011,6,122,2,1,7,1),_HwL2tpTunnelindex_Type())
hwL2tpTunnelindex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwL2tpTunnelindex.setStatus(_B)
class _HwL2tpSessionindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwL2tpSessionindex_Type.__name__=_D
_HwL2tpSessionindex_Object=MibScalar
hwL2tpSessionindex=_HwL2tpSessionindex_Object((1,3,6,1,4,1,2011,6,122,2,1,7,2),_HwL2tpSessionindex_Type())
hwL2tpSessionindex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwL2tpSessionindex.setStatus(_B)
_HwL2tpTunnelRemoteAddr_Type=IpAddress
_HwL2tpTunnelRemoteAddr_Object=MibScalar
hwL2tpTunnelRemoteAddr=_HwL2tpTunnelRemoteAddr_Object((1,3,6,1,4,1,2011,6,122,2,1,7,3),_HwL2tpTunnelRemoteAddr_Type())
hwL2tpTunnelRemoteAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hwL2tpTunnelRemoteAddr.setStatus(_B)
_HwL2tpTunnelUserName_Type=OctetString
_HwL2tpTunnelUserName_Object=MibScalar
hwL2tpTunnelUserName=_HwL2tpTunnelUserName_Object((1,3,6,1,4,1,2011,6,122,2,1,7,4),_HwL2tpTunnelUserName_Type())
hwL2tpTunnelUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:hwL2tpTunnelUserName.setStatus(_B)
_HwL2tpTunnelStartTime_Type=DateAndTime
_HwL2tpTunnelStartTime_Object=MibScalar
hwL2tpTunnelStartTime=_HwL2tpTunnelStartTime_Object((1,3,6,1,4,1,2011,6,122,2,1,7,5),_HwL2tpTunnelStartTime_Type())
hwL2tpTunnelStartTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwL2tpTunnelStartTime.setStatus(_B)
_HwL2tpTrap_ObjectIdentity=ObjectIdentity
hwL2tpTrap=_HwL2tpTrap_ObjectIdentity((1,3,6,1,4,1,2011,6,122,2,1,8))
_HwL2tpNotifications_ObjectIdentity=ObjectIdentity
hwL2tpNotifications=_HwL2tpNotifications_ObjectIdentity((1,3,6,1,4,1,2011,6,122,2,1,8,1))
_HwL2tpMibConformance_ObjectIdentity=ObjectIdentity
hwL2tpMibConformance=_HwL2tpMibConformance_ObjectIdentity((1,3,6,1,4,1,2011,6,122,2,1,10))
_HwL2tpMibGroups_ObjectIdentity=ObjectIdentity
hwL2tpMibGroups=_HwL2tpMibGroups_ObjectIdentity((1,3,6,1,4,1,2011,6,122,2,1,10,2))
hwL2tpGroupConfigTableGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,2,1,10,2,2))
hwL2tpGroupConfigTableGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:hwL2tpGroupConfigTableGroup.setStatus(_B)
hwL2tpTunnelTableGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,2,1,10,2,3))
hwL2tpTunnelTableGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:hwL2tpTunnelTableGroup.setStatus(_B)
hwL2tpSessionTableGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,2,1,10,2,4))
hwL2tpSessionTableGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:hwL2tpSessionTableGroup.setStatus(_B)
hwL2tpTrapObjectGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,2,1,10,2,5))
hwL2tpTrapObjectGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hwL2tpTrapObjectGroup.setStatus(_B)
hwL2tpSessionStart=NotificationType((1,3,6,1,4,1,2011,6,122,2,1,8,1,1))
hwL2tpSessionStart.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hwL2tpSessionStart.setStatus(_B)
hwL2tpSessionStop=NotificationType((1,3,6,1,4,1,2011,6,122,2,1,8,1,2))
hwL2tpSessionStop.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hwL2tpSessionStop.setStatus(_B)
hwL2tpTrapGroup=NotificationGroup((1,3,6,1,4,1,2011,6,122,2,1,10,2,6))
hwL2tpTrapGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:hwL2tpTrapGroup.setStatus(_B)
hwL2tpMibCompliances=ModuleCompliance((1,3,6,1,4,1,2011,6,122,2,1,10,1))
hwL2tpMibCompliances.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:hwL2tpMibCompliances.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'huawei':huawei,'huaweiUtility':huaweiUtility,'hwSecurity':hwSecurity,'hwL2tpMib':hwL2tpMib,'hwL2tpMibObjects':hwL2tpMibObjects,'hwL2tpEnableFlag':hwL2tpEnableFlag,'hwL2tpGroupConfigTable':hwL2tpGroupConfigTable,'hwL2tpGroupConfigEntry':hwL2tpGroupConfigEntry,_O:hwL2tpGroupindex,_R:hwL2tpTunnelNumber,_S:hwL2tpGroupFlag,_T:hwL2tpGroupAuthentication,_U:hwL2tpGroupPassWord,_V:hwL2tpGroupAvpHidden,_W:hwL2tpGroupName,_X:hwL2tpGroupRemoteName,_Y:hwL2tpGroupRetransmit,_Z:hwL2tpGroupTimeout,_a:hwL2tpGroupTimer,_b:hwL2tpGroupLnsIP1,_c:hwL2tpGroupLnsIP2,_d:hwL2tpGroupLnsIP3,_e:hwL2tpGroupLnsIP4,_f:hwL2tpGroupLnsIP5,_g:hwL2tpGroupForceChap,_h:hwL2tpGroupForceLcp,_i:hwL2tpGroupVt,_j:hwL2tpGroupRowStatus,'hwL2tpTunnelTable':hwL2tpTunnelTable,'hwL2tpTunnelEntry':hwL2tpTunnelEntry,_P:hwL2tpTunnelIndex,_k:hwL2tpTunnelLocalID,_l:hwL2tpTunnelRemoteID,_m:hwL2tpTunnelRemoteName,_n:hwL2tpTunnelRemoteIP,_o:hwL2tpTunnelRemotePort,_p:hwL2tpTunnelSessionNum,_q:hwL2tpLnsGroupRowStatus,'hwL2tpSessionTable':hwL2tpSessionTable,'hwL2tpSessionEntry':hwL2tpSessionEntry,_Q:hwL2tpSessionIndex,_r:hwL2tpSessionTunnelID,_s:hwL2tpSessionLocalSID,_t:hwL2tpSessionRemoteSID,_u:hwL2tpSessionUserName,_v:hwL2tpSessionUserOnlineTime,_w:hwL2tpSessionState,_x:hwL2tpSessionCallType,_y:hwL2tpSessionSerialNumber,'hwL2tpTrapObject':hwL2tpTrapObject,_H:hwL2tpTunnelindex,_I:hwL2tpSessionindex,_J:hwL2tpTunnelRemoteAddr,_K:hwL2tpTunnelUserName,_L:hwL2tpTunnelStartTime,'hwL2tpTrap':hwL2tpTrap,'hwL2tpNotifications':hwL2tpNotifications,_z:hwL2tpSessionStart,_A0:hwL2tpSessionStop,'hwL2tpMibConformance':hwL2tpMibConformance,'hwL2tpMibCompliances':hwL2tpMibCompliances,'hwL2tpMibGroups':hwL2tpMibGroups,_A1:hwL2tpGroupConfigTableGroup,_A2:hwL2tpTunnelTableGroup,_A3:hwL2tpSessionTableGroup,_A4:hwL2tpTrapObjectGroup,_A5:hwL2tpTrapGroup})