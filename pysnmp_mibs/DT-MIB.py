_A2='hpSwitchDtSystemInfoGroup'
_A1='hpSwitchDtSystemRole'
_A0='hpSwitchDtSystemPeerOperRolePriority'
_z='hpSwitchDtSystemOperRolePriority'
_y='hpSwitchDtSystemAdminRolePriority'
_x='hpSwitchDtSystemDtLacpSystemID'
_w='hpSwitchDtSystemISCProtocolState'
_v='hpSwitchDtPeerKeepAlivePktsRecv'
_u='hpSwitchDtPeerKeepAlivePktsSent'
_t='hpSwitchDtIscMACAgedPktsRecv'
_s='hpSwitchDtIscMACAgedPktsSent'
_r='hpSwitchDtIscMACLearnPktsRecv'
_q='hpSwitchDtIscMACLearnPktsSent'
_p='hpSwitchDtIscHelloPktsRecv'
_o='hpSwitchDtIscHelloPktsSent'
_n='hpSwitchDtPeerKeepAliveHoldTime'
_m='hpSwitchDtPeerKeepAliveTimeout'
_l='hpSwitchDtPeerKeepAliveInterval'
_k='hpSwitchDtPeerKeepAliveDestUdpPort'
_j='hpSwitchDtPeerKeepAliveVlanId'
_i='hpSwitchDtPeerKeepAliveDestAddress'
_h='hpSwitchDtPeerKeepAliveDestAddressType'
_g='hpSwitchDtLacpPeerIfLacpStatus'
_f='hpSwitchDtLacpPeerIfLacpPartner'
_e='hpSwitchDtLacpPeerIfLacpPortStatus'
_d='hpSwitchDtLacpPeerIfTrunkGroup'
_c='hpSwitchDtLacpPeerIfLacpEnable'
_b='hpSwitchDtLacpPeerIfName'
_a='hpSwitchDtLacpLocalIfLacpOperKey'
_Z='hpSwitchDtLacpLocalIfLacpAdminKey'
_Y='hpSwitchDtLacpLocalIfLacpStatus'
_X='hpSwitchDtLacpLocalIfLacpPartner'
_W='hpSwitchDtLacpLocalIfLacpPortStatus'
_V='hpSwitchDtLacpLocalIfTrunkGroup'
_U='hpSwitchDtLacpLocalIfLacpEnable'
_T='hpSwitchDtLacpLocalIfName'
_S='hpSwitchRemoteISCPortIndex'
_R='hpSwitchISCPortIndex'
_Q='unknown'
_P='seconds'
_O='InetPortNumber'
_N='hpSwitchDtPeerKeepAliveStatsGroup'
_M='hpSwitchDtIscStatsGroup'
_L='hpSwitchDtPeerKeepAliveGroup'
_K='hpSwitchDtRemoteLacpGroup'
_J='hpSwitchDtLocalLacpGroup'
_I='hpSwitchDtIscGroup'
_H='hpSwitchDtLacpPeerIfIndex'
_G='hpSwitchDtLacpLocalIfIndex'
_F='Packets'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='DT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpSwitchDt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27))
if mibBuilder.loadTexts:hpSwitchDt.setRevisions(('2012-05-22 18:00','2011-08-09 00:00','2011-03-22 18:00','2007-10-27 18:00'))
_HpConfig_ObjectIdentity=ObjectIdentity
hpConfig=_HpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7))
_HpSwitchConfig_ObjectIdentity=ObjectIdentity
hpSwitchConfig=_HpSwitchConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1))
class _HpSwitchISCPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchISCPortIndex_Type.__name__=_D
_HpSwitchISCPortIndex_Object=MibScalar
hpSwitchISCPortIndex=_HpSwitchISCPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,1),_HpSwitchISCPortIndex_Type())
hpSwitchISCPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchISCPortIndex.setStatus(_B)
class _HpSwitchRemoteISCPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchRemoteISCPortIndex_Type.__name__=_D
_HpSwitchRemoteISCPortIndex_Object=MibScalar
hpSwitchRemoteISCPortIndex=_HpSwitchRemoteISCPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,2),_HpSwitchRemoteISCPortIndex_Type())
hpSwitchRemoteISCPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRemoteISCPortIndex.setStatus(_B)
_HpSwitchDtLacpStatus_ObjectIdentity=ObjectIdentity
hpSwitchDtLacpStatus=_HpSwitchDtLacpStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3))
_HpSwitchDtLacpStatusLocalTable_Object=MibTable
hpSwitchDtLacpStatusLocalTable=_HpSwitchDtLacpStatusLocalTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1))
if mibBuilder.loadTexts:hpSwitchDtLacpStatusLocalTable.setStatus(_B)
_HpSwitchDtLacpStatusLocalEntry_Object=MibTableRow
hpSwitchDtLacpStatusLocalEntry=_HpSwitchDtLacpStatusLocalEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1))
hpSwitchDtLacpStatusLocalEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:hpSwitchDtLacpStatusLocalEntry.setStatus(_B)
class _HpSwitchDtLacpLocalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchDtLacpLocalIfIndex_Type.__name__=_D
_HpSwitchDtLacpLocalIfIndex_Object=MibTableColumn
hpSwitchDtLacpLocalIfIndex=_HpSwitchDtLacpLocalIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,1),_HpSwitchDtLacpLocalIfIndex_Type())
hpSwitchDtLacpLocalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfIndex.setStatus(_B)
_HpSwitchDtLacpLocalIfName_Type=DisplayString
_HpSwitchDtLacpLocalIfName_Object=MibTableColumn
hpSwitchDtLacpLocalIfName=_HpSwitchDtLacpLocalIfName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,2),_HpSwitchDtLacpLocalIfName_Type())
hpSwitchDtLacpLocalIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfName.setStatus(_B)
_HpSwitchDtLacpLocalIfLacpEnable_Type=Integer32
_HpSwitchDtLacpLocalIfLacpEnable_Object=MibTableColumn
hpSwitchDtLacpLocalIfLacpEnable=_HpSwitchDtLacpLocalIfLacpEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,3),_HpSwitchDtLacpLocalIfLacpEnable_Type())
hpSwitchDtLacpLocalIfLacpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfLacpEnable.setStatus(_B)
_HpSwitchDtLacpLocalIfTrunkGroup_Type=Integer32
_HpSwitchDtLacpLocalIfTrunkGroup_Object=MibTableColumn
hpSwitchDtLacpLocalIfTrunkGroup=_HpSwitchDtLacpLocalIfTrunkGroup_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,4),_HpSwitchDtLacpLocalIfTrunkGroup_Type())
hpSwitchDtLacpLocalIfTrunkGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfTrunkGroup.setStatus(_B)
_HpSwitchDtLacpLocalIfLacpPortStatus_Type=Integer32
_HpSwitchDtLacpLocalIfLacpPortStatus_Object=MibTableColumn
hpSwitchDtLacpLocalIfLacpPortStatus=_HpSwitchDtLacpLocalIfLacpPortStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,5),_HpSwitchDtLacpLocalIfLacpPortStatus_Type())
hpSwitchDtLacpLocalIfLacpPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfLacpPortStatus.setStatus(_B)
_HpSwitchDtLacpLocalIfLacpPartner_Type=Integer32
_HpSwitchDtLacpLocalIfLacpPartner_Object=MibTableColumn
hpSwitchDtLacpLocalIfLacpPartner=_HpSwitchDtLacpLocalIfLacpPartner_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,6),_HpSwitchDtLacpLocalIfLacpPartner_Type())
hpSwitchDtLacpLocalIfLacpPartner.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfLacpPartner.setStatus(_B)
_HpSwitchDtLacpLocalIfLacpStatus_Type=Integer32
_HpSwitchDtLacpLocalIfLacpStatus_Object=MibTableColumn
hpSwitchDtLacpLocalIfLacpStatus=_HpSwitchDtLacpLocalIfLacpStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,7),_HpSwitchDtLacpLocalIfLacpStatus_Type())
hpSwitchDtLacpLocalIfLacpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfLacpStatus.setStatus(_B)
_HpSwitchDtLacpLocalIfLacpAdminKey_Type=Integer32
_HpSwitchDtLacpLocalIfLacpAdminKey_Object=MibTableColumn
hpSwitchDtLacpLocalIfLacpAdminKey=_HpSwitchDtLacpLocalIfLacpAdminKey_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,8),_HpSwitchDtLacpLocalIfLacpAdminKey_Type())
hpSwitchDtLacpLocalIfLacpAdminKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfLacpAdminKey.setStatus(_B)
_HpSwitchDtLacpLocalIfLacpOperKey_Type=Integer32
_HpSwitchDtLacpLocalIfLacpOperKey_Object=MibTableColumn
hpSwitchDtLacpLocalIfLacpOperKey=_HpSwitchDtLacpLocalIfLacpOperKey_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,1,1,9),_HpSwitchDtLacpLocalIfLacpOperKey_Type())
hpSwitchDtLacpLocalIfLacpOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpLocalIfLacpOperKey.setStatus(_B)
_HpSwitchDtLacpStatusPeerTable_Object=MibTable
hpSwitchDtLacpStatusPeerTable=_HpSwitchDtLacpStatusPeerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2))
if mibBuilder.loadTexts:hpSwitchDtLacpStatusPeerTable.setStatus(_B)
_HpSwitchDtLacpStatusPeerEntry_Object=MibTableRow
hpSwitchDtLacpStatusPeerEntry=_HpSwitchDtLacpStatusPeerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1))
hpSwitchDtLacpStatusPeerEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:hpSwitchDtLacpStatusPeerEntry.setStatus(_B)
class _HpSwitchDtLacpPeerIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchDtLacpPeerIfIndex_Type.__name__=_D
_HpSwitchDtLacpPeerIfIndex_Object=MibTableColumn
hpSwitchDtLacpPeerIfIndex=_HpSwitchDtLacpPeerIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1,1),_HpSwitchDtLacpPeerIfIndex_Type())
hpSwitchDtLacpPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpPeerIfIndex.setStatus(_B)
_HpSwitchDtLacpPeerIfName_Type=DisplayString
_HpSwitchDtLacpPeerIfName_Object=MibTableColumn
hpSwitchDtLacpPeerIfName=_HpSwitchDtLacpPeerIfName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1,2),_HpSwitchDtLacpPeerIfName_Type())
hpSwitchDtLacpPeerIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpPeerIfName.setStatus(_B)
_HpSwitchDtLacpPeerIfLacpEnable_Type=Integer32
_HpSwitchDtLacpPeerIfLacpEnable_Object=MibTableColumn
hpSwitchDtLacpPeerIfLacpEnable=_HpSwitchDtLacpPeerIfLacpEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1,3),_HpSwitchDtLacpPeerIfLacpEnable_Type())
hpSwitchDtLacpPeerIfLacpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpPeerIfLacpEnable.setStatus(_B)
_HpSwitchDtLacpPeerIfTrunkGroup_Type=Integer32
_HpSwitchDtLacpPeerIfTrunkGroup_Object=MibTableColumn
hpSwitchDtLacpPeerIfTrunkGroup=_HpSwitchDtLacpPeerIfTrunkGroup_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1,4),_HpSwitchDtLacpPeerIfTrunkGroup_Type())
hpSwitchDtLacpPeerIfTrunkGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpPeerIfTrunkGroup.setStatus(_B)
_HpSwitchDtLacpPeerIfLacpPortStatus_Type=Integer32
_HpSwitchDtLacpPeerIfLacpPortStatus_Object=MibTableColumn
hpSwitchDtLacpPeerIfLacpPortStatus=_HpSwitchDtLacpPeerIfLacpPortStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1,5),_HpSwitchDtLacpPeerIfLacpPortStatus_Type())
hpSwitchDtLacpPeerIfLacpPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpPeerIfLacpPortStatus.setStatus(_B)
_HpSwitchDtLacpPeerIfLacpPartner_Type=Integer32
_HpSwitchDtLacpPeerIfLacpPartner_Object=MibTableColumn
hpSwitchDtLacpPeerIfLacpPartner=_HpSwitchDtLacpPeerIfLacpPartner_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1,6),_HpSwitchDtLacpPeerIfLacpPartner_Type())
hpSwitchDtLacpPeerIfLacpPartner.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpPeerIfLacpPartner.setStatus(_B)
_HpSwitchDtLacpPeerIfLacpStatus_Type=Integer32
_HpSwitchDtLacpPeerIfLacpStatus_Object=MibTableColumn
hpSwitchDtLacpPeerIfLacpStatus=_HpSwitchDtLacpPeerIfLacpStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,3,2,1,7),_HpSwitchDtLacpPeerIfLacpStatus_Type())
hpSwitchDtLacpPeerIfLacpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtLacpPeerIfLacpStatus.setStatus(_B)
_HpSwitchDtConfig_ObjectIdentity=ObjectIdentity
hpSwitchDtConfig=_HpSwitchDtConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4))
_HpSwitchDtPeerKeepAliveConfig_ObjectIdentity=ObjectIdentity
hpSwitchDtPeerKeepAliveConfig=_HpSwitchDtPeerKeepAliveConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1))
_HpSwitchDtPeerKeepAliveDestAddressType_Type=InetAddressType
_HpSwitchDtPeerKeepAliveDestAddressType_Object=MibScalar
hpSwitchDtPeerKeepAliveDestAddressType=_HpSwitchDtPeerKeepAliveDestAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1,1),_HpSwitchDtPeerKeepAliveDestAddressType_Type())
hpSwitchDtPeerKeepAliveDestAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveDestAddressType.setStatus(_B)
_HpSwitchDtPeerKeepAliveDestAddress_Type=InetAddress
_HpSwitchDtPeerKeepAliveDestAddress_Object=MibScalar
hpSwitchDtPeerKeepAliveDestAddress=_HpSwitchDtPeerKeepAliveDestAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1,2),_HpSwitchDtPeerKeepAliveDestAddress_Type())
hpSwitchDtPeerKeepAliveDestAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveDestAddress.setStatus(_B)
class _HpSwitchDtPeerKeepAliveVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_HpSwitchDtPeerKeepAliveVlanId_Type.__name__=_D
_HpSwitchDtPeerKeepAliveVlanId_Object=MibScalar
hpSwitchDtPeerKeepAliveVlanId=_HpSwitchDtPeerKeepAliveVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1,3),_HpSwitchDtPeerKeepAliveVlanId_Type())
hpSwitchDtPeerKeepAliveVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveVlanId.setStatus(_B)
class _HpSwitchDtPeerKeepAliveDestUdpPort_Type(InetPortNumber):defaultValue=1024
_HpSwitchDtPeerKeepAliveDestUdpPort_Type.__name__=_O
_HpSwitchDtPeerKeepAliveDestUdpPort_Object=MibScalar
hpSwitchDtPeerKeepAliveDestUdpPort=_HpSwitchDtPeerKeepAliveDestUdpPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1,4),_HpSwitchDtPeerKeepAliveDestUdpPort_Type())
hpSwitchDtPeerKeepAliveDestUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveDestUdpPort.setStatus(_B)
class _HpSwitchDtPeerKeepAliveInterval_Type(Integer32):defaultValue=1000
_HpSwitchDtPeerKeepAliveInterval_Type.__name__=_D
_HpSwitchDtPeerKeepAliveInterval_Object=MibScalar
hpSwitchDtPeerKeepAliveInterval=_HpSwitchDtPeerKeepAliveInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1,5),_HpSwitchDtPeerKeepAliveInterval_Type())
hpSwitchDtPeerKeepAliveInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveInterval.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveInterval.setUnits('milliseconds')
class _HpSwitchDtPeerKeepAliveTimeout_Type(Integer32):defaultValue=5
_HpSwitchDtPeerKeepAliveTimeout_Type.__name__=_D
_HpSwitchDtPeerKeepAliveTimeout_Object=MibScalar
hpSwitchDtPeerKeepAliveTimeout=_HpSwitchDtPeerKeepAliveTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1,6),_HpSwitchDtPeerKeepAliveTimeout_Type())
hpSwitchDtPeerKeepAliveTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveTimeout.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveTimeout.setUnits(_P)
class _HpSwitchDtPeerKeepAliveHoldTime_Type(Integer32):defaultValue=3
_HpSwitchDtPeerKeepAliveHoldTime_Type.__name__=_D
_HpSwitchDtPeerKeepAliveHoldTime_Object=MibScalar
hpSwitchDtPeerKeepAliveHoldTime=_HpSwitchDtPeerKeepAliveHoldTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,4,1,7),_HpSwitchDtPeerKeepAliveHoldTime_Type())
hpSwitchDtPeerKeepAliveHoldTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveHoldTime.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveHoldTime.setUnits(_P)
_HpSwitchDtStats_ObjectIdentity=ObjectIdentity
hpSwitchDtStats=_HpSwitchDtStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5))
_HpSwitchDtIscProtocolStats_ObjectIdentity=ObjectIdentity
hpSwitchDtIscProtocolStats=_HpSwitchDtIscProtocolStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,1))
_HpSwitchDtIscHelloPktsSent_Type=Counter32
_HpSwitchDtIscHelloPktsSent_Object=MibScalar
hpSwitchDtIscHelloPktsSent=_HpSwitchDtIscHelloPktsSent_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,1,1),_HpSwitchDtIscHelloPktsSent_Type())
hpSwitchDtIscHelloPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtIscHelloPktsSent.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtIscHelloPktsSent.setUnits(_F)
_HpSwitchDtIscHelloPktsRecv_Type=Counter32
_HpSwitchDtIscHelloPktsRecv_Object=MibScalar
hpSwitchDtIscHelloPktsRecv=_HpSwitchDtIscHelloPktsRecv_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,1,2),_HpSwitchDtIscHelloPktsRecv_Type())
hpSwitchDtIscHelloPktsRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtIscHelloPktsRecv.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtIscHelloPktsRecv.setUnits(_F)
_HpSwitchDtIscMACLearnPktsSent_Type=Counter32
_HpSwitchDtIscMACLearnPktsSent_Object=MibScalar
hpSwitchDtIscMACLearnPktsSent=_HpSwitchDtIscMACLearnPktsSent_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,1,3),_HpSwitchDtIscMACLearnPktsSent_Type())
hpSwitchDtIscMACLearnPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtIscMACLearnPktsSent.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtIscMACLearnPktsSent.setUnits(_F)
_HpSwitchDtIscMACLearnPktsRecv_Type=Counter32
_HpSwitchDtIscMACLearnPktsRecv_Object=MibScalar
hpSwitchDtIscMACLearnPktsRecv=_HpSwitchDtIscMACLearnPktsRecv_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,1,4),_HpSwitchDtIscMACLearnPktsRecv_Type())
hpSwitchDtIscMACLearnPktsRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtIscMACLearnPktsRecv.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtIscMACLearnPktsRecv.setUnits(_F)
_HpSwitchDtIscMACAgedPktsSent_Type=Counter32
_HpSwitchDtIscMACAgedPktsSent_Object=MibScalar
hpSwitchDtIscMACAgedPktsSent=_HpSwitchDtIscMACAgedPktsSent_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,1,5),_HpSwitchDtIscMACAgedPktsSent_Type())
hpSwitchDtIscMACAgedPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtIscMACAgedPktsSent.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtIscMACAgedPktsSent.setUnits(_F)
_HpSwitchDtIscMACAgedPktsRecv_Type=Counter32
_HpSwitchDtIscMACAgedPktsRecv_Object=MibScalar
hpSwitchDtIscMACAgedPktsRecv=_HpSwitchDtIscMACAgedPktsRecv_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,1,6),_HpSwitchDtIscMACAgedPktsRecv_Type())
hpSwitchDtIscMACAgedPktsRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtIscMACAgedPktsRecv.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtIscMACAgedPktsRecv.setUnits(_F)
_HpSwitchDtPeerKeepAliveStats_ObjectIdentity=ObjectIdentity
hpSwitchDtPeerKeepAliveStats=_HpSwitchDtPeerKeepAliveStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,2))
_HpSwitchDtPeerKeepAlivePktsSent_Type=Counter32
_HpSwitchDtPeerKeepAlivePktsSent_Object=MibScalar
hpSwitchDtPeerKeepAlivePktsSent=_HpSwitchDtPeerKeepAlivePktsSent_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,2,1),_HpSwitchDtPeerKeepAlivePktsSent_Type())
hpSwitchDtPeerKeepAlivePktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAlivePktsSent.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAlivePktsSent.setUnits(_F)
_HpSwitchDtPeerKeepAlivePktsRecv_Type=Counter32
_HpSwitchDtPeerKeepAlivePktsRecv_Object=MibScalar
hpSwitchDtPeerKeepAlivePktsRecv=_HpSwitchDtPeerKeepAlivePktsRecv_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,5,2,2),_HpSwitchDtPeerKeepAlivePktsRecv_Type())
hpSwitchDtPeerKeepAlivePktsRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAlivePktsRecv.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAlivePktsRecv.setUnits(_F)
_HpSwitchDtSystemInfo_ObjectIdentity=ObjectIdentity
hpSwitchDtSystemInfo=_HpSwitchDtSystemInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,6))
class _HpSwitchDtSystemISCProtocolState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('inSync',2),('outOfSync',3)))
_HpSwitchDtSystemISCProtocolState_Type.__name__=_D
_HpSwitchDtSystemISCProtocolState_Object=MibScalar
hpSwitchDtSystemISCProtocolState=_HpSwitchDtSystemISCProtocolState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,6,1),_HpSwitchDtSystemISCProtocolState_Type())
hpSwitchDtSystemISCProtocolState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtSystemISCProtocolState.setStatus(_B)
_HpSwitchDtSystemDtLacpSystemID_Type=MacAddress
_HpSwitchDtSystemDtLacpSystemID_Object=MibScalar
hpSwitchDtSystemDtLacpSystemID=_HpSwitchDtSystemDtLacpSystemID_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,6,2),_HpSwitchDtSystemDtLacpSystemID_Type())
hpSwitchDtSystemDtLacpSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtSystemDtLacpSystemID.setStatus(_B)
class _HpSwitchDtSystemAdminRolePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchDtSystemAdminRolePriority_Type.__name__=_D
_HpSwitchDtSystemAdminRolePriority_Object=MibScalar
hpSwitchDtSystemAdminRolePriority=_HpSwitchDtSystemAdminRolePriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,6,3),_HpSwitchDtSystemAdminRolePriority_Type())
hpSwitchDtSystemAdminRolePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchDtSystemAdminRolePriority.setStatus(_B)
class _HpSwitchDtSystemOperRolePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchDtSystemOperRolePriority_Type.__name__=_D
_HpSwitchDtSystemOperRolePriority_Object=MibScalar
hpSwitchDtSystemOperRolePriority=_HpSwitchDtSystemOperRolePriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,6,4),_HpSwitchDtSystemOperRolePriority_Type())
hpSwitchDtSystemOperRolePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtSystemOperRolePriority.setStatus(_B)
class _HpSwitchDtSystemPeerOperRolePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchDtSystemPeerOperRolePriority_Type.__name__=_D
_HpSwitchDtSystemPeerOperRolePriority_Object=MibScalar
hpSwitchDtSystemPeerOperRolePriority=_HpSwitchDtSystemPeerOperRolePriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,6,5),_HpSwitchDtSystemPeerOperRolePriority_Type())
hpSwitchDtSystemPeerOperRolePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtSystemPeerOperRolePriority.setStatus(_B)
class _HpSwitchDtSystemRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('primary',2),('secondary',3)))
_HpSwitchDtSystemRole_Type.__name__=_D
_HpSwitchDtSystemRole_Object=MibScalar
hpSwitchDtSystemRole=_HpSwitchDtSystemRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,6,6),_HpSwitchDtSystemRole_Type())
hpSwitchDtSystemRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDtSystemRole.setStatus(_B)
_HpSwitchDtConformance_ObjectIdentity=ObjectIdentity
hpSwitchDtConformance=_HpSwitchDtConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256))
_HpSwitchDtCompliances_ObjectIdentity=ObjectIdentity
hpSwitchDtCompliances=_HpSwitchDtCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,1))
_HpSwitchDtGroups_ObjectIdentity=ObjectIdentity
hpSwitchDtGroups=_HpSwitchDtGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2))
hpSwitchDtIscGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2,1))
hpSwitchDtIscGroup.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:hpSwitchDtIscGroup.setStatus(_B)
hpSwitchDtLocalLacpGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2,2))
hpSwitchDtLocalLacpGroup.setObjects(*((_A,_G),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpSwitchDtLocalLacpGroup.setStatus(_B)
hpSwitchDtRemoteLacpGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2,3))
hpSwitchDtRemoteLacpGroup.setObjects(*((_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:hpSwitchDtRemoteLacpGroup.setStatus(_B)
hpSwitchDtPeerKeepAliveGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2,4))
hpSwitchDtPeerKeepAliveGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveGroup.setStatus(_B)
hpSwitchDtIscStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2,5))
hpSwitchDtIscStatsGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:hpSwitchDtIscStatsGroup.setStatus(_B)
hpSwitchDtPeerKeepAliveStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2,6))
hpSwitchDtPeerKeepAliveStatsGroup.setObjects(*((_A,_u),(_A,_v)))
if mibBuilder.loadTexts:hpSwitchDtPeerKeepAliveStatsGroup.setStatus(_B)
hpSwitchDtSystemInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,2,7))
hpSwitchDtSystemInfoGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:hpSwitchDtSystemInfoGroup.setStatus(_B)
hpSwitchDtCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,1,1))
hpSwitchDtCompliance.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpSwitchDtCompliance.setStatus('deprecated')
hpSwitchDtCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,27,256,1,2))
hpSwitchDtCompliance1.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_A2),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpSwitchDtCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpConfig':hpConfig,'hpSwitchConfig':hpSwitchConfig,'hpSwitchDt':hpSwitchDt,_R:hpSwitchISCPortIndex,_S:hpSwitchRemoteISCPortIndex,'hpSwitchDtLacpStatus':hpSwitchDtLacpStatus,'hpSwitchDtLacpStatusLocalTable':hpSwitchDtLacpStatusLocalTable,'hpSwitchDtLacpStatusLocalEntry':hpSwitchDtLacpStatusLocalEntry,_G:hpSwitchDtLacpLocalIfIndex,_T:hpSwitchDtLacpLocalIfName,_U:hpSwitchDtLacpLocalIfLacpEnable,_V:hpSwitchDtLacpLocalIfTrunkGroup,_W:hpSwitchDtLacpLocalIfLacpPortStatus,_X:hpSwitchDtLacpLocalIfLacpPartner,_Y:hpSwitchDtLacpLocalIfLacpStatus,_Z:hpSwitchDtLacpLocalIfLacpAdminKey,_a:hpSwitchDtLacpLocalIfLacpOperKey,'hpSwitchDtLacpStatusPeerTable':hpSwitchDtLacpStatusPeerTable,'hpSwitchDtLacpStatusPeerEntry':hpSwitchDtLacpStatusPeerEntry,_H:hpSwitchDtLacpPeerIfIndex,_b:hpSwitchDtLacpPeerIfName,_c:hpSwitchDtLacpPeerIfLacpEnable,_d:hpSwitchDtLacpPeerIfTrunkGroup,_e:hpSwitchDtLacpPeerIfLacpPortStatus,_f:hpSwitchDtLacpPeerIfLacpPartner,_g:hpSwitchDtLacpPeerIfLacpStatus,'hpSwitchDtConfig':hpSwitchDtConfig,'hpSwitchDtPeerKeepAliveConfig':hpSwitchDtPeerKeepAliveConfig,_h:hpSwitchDtPeerKeepAliveDestAddressType,_i:hpSwitchDtPeerKeepAliveDestAddress,_j:hpSwitchDtPeerKeepAliveVlanId,_k:hpSwitchDtPeerKeepAliveDestUdpPort,_l:hpSwitchDtPeerKeepAliveInterval,_m:hpSwitchDtPeerKeepAliveTimeout,_n:hpSwitchDtPeerKeepAliveHoldTime,'hpSwitchDtStats':hpSwitchDtStats,'hpSwitchDtIscProtocolStats':hpSwitchDtIscProtocolStats,_o:hpSwitchDtIscHelloPktsSent,_p:hpSwitchDtIscHelloPktsRecv,_q:hpSwitchDtIscMACLearnPktsSent,_r:hpSwitchDtIscMACLearnPktsRecv,_s:hpSwitchDtIscMACAgedPktsSent,_t:hpSwitchDtIscMACAgedPktsRecv,'hpSwitchDtPeerKeepAliveStats':hpSwitchDtPeerKeepAliveStats,_u:hpSwitchDtPeerKeepAlivePktsSent,_v:hpSwitchDtPeerKeepAlivePktsRecv,'hpSwitchDtSystemInfo':hpSwitchDtSystemInfo,_w:hpSwitchDtSystemISCProtocolState,_x:hpSwitchDtSystemDtLacpSystemID,_y:hpSwitchDtSystemAdminRolePriority,_z:hpSwitchDtSystemOperRolePriority,_A0:hpSwitchDtSystemPeerOperRolePriority,_A1:hpSwitchDtSystemRole,'hpSwitchDtConformance':hpSwitchDtConformance,'hpSwitchDtCompliances':hpSwitchDtCompliances,'hpSwitchDtCompliance':hpSwitchDtCompliance,'hpSwitchDtCompliance1':hpSwitchDtCompliance1,'hpSwitchDtGroups':hpSwitchDtGroups,_I:hpSwitchDtIscGroup,_J:hpSwitchDtLocalLacpGroup,_K:hpSwitchDtRemoteLacpGroup,_L:hpSwitchDtPeerKeepAliveGroup,_M:hpSwitchDtIscStatsGroup,_N:hpSwitchDtPeerKeepAliveStatsGroup,_A2:hpSwitchDtSystemInfoGroup})