_y='ccaHCCPOffNotification'
_x='ccaHCCPOnNotification'
_w='ccaHCCPMemChanSwitchSnmpEnable'
_v='ccaHCCPMemChanSwitchPosition'
_u='ccaHCCPMemChanSwitchProtModule'
_t='ccaHCCPMemChanSwitchProtIpAddr'
_s='ccaHCCPMemChanSwitchProtIpAddrType'
_r='ccaHCCPMemChanSwitchModule'
_q='ccaHCCPMemChanSwitchIpAddress'
_p='ccaHCCPMemChanSwitchIpAddrType'
_o='ccaHCCPMemChanSwitchType'
_n='ccaHCCPMemberSwitchNow'
_m='ccaHCCPMemberIpAddress'
_l='ccaHCCPMemberIpAddrType'
_k='ccaHCCPGroupIfState'
_j='ccaHCCPGroupTrackIfDescr'
_i='ccaHCCPGroupIfOffTransitions'
_h='ccaHCCPGroupIfOnTransitions'
_g='ccaHCCPGroupIfTrackEnable'
_f='ccaHCCPGroupIfRevertTime'
_e='ccaHCCPGroupProtectIpAddress'
_d='ccaHCCPGroupProtectIpAddrType'
_c='ccaHCCPGroupRevertEnable'
_b='ccaHCCPGroupHoldTime'
_a='ccaHCCPGroupHelloTime'
_Z='ccaHCCPGroupAuthKeyChain'
_Y='ccaHCCPGroupAuthentication'
_X='ccaHCCPOnOffNotificationEnable'
_W='ccaHCCPVersion'
_V='ccaHCCPMemChanSwitchID'
_U='ccaHCCPGroupTrackIfID'
_T='milliseconds'
_S='others'
_R='TruthValue'
_Q='DisplayString'
_P='ccaHCCPNotificationGroup'
_O='ccaHCCPMemberGroup'
_N='ccaHCCPGroup'
_M='ccaHCCPMemberID'
_L='ccaHCCPMemberState'
_K='ccaHCCPGroupIfLastSwitchReason'
_J='ccaHCCPGroupIfStatus'
_I='read-write'
_H='not-accessible'
_G='ifIndex'
_F='IF-MIB'
_E='ccaHCCPGroupID'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-CABLE-AVAILABILITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_Q,'PhysAddress','TextualConvention',_R)
ciscoCableAvailabilityMIB=ModuleIdentity((1,3,6,1,4,1,9,9,242))
if mibBuilder.loadTexts:ciscoCableAvailabilityMIB.setRevisions(('2003-02-20 00:00','2001-11-25 00:00'))
_CiscoCableAvailabilityMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCableAvailabilityMIBObjects=_CiscoCableAvailabilityMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,242,1))
_CcaHCCPObjects_ObjectIdentity=ObjectIdentity
ccaHCCPObjects=_CcaHCCPObjects_ObjectIdentity((1,3,6,1,4,1,9,9,242,1,1))
class _CcaHCCPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('version1',2),('version2',3),('version3',4)))
_CcaHCCPVersion_Type.__name__=_D
_CcaHCCPVersion_Object=MibScalar
ccaHCCPVersion=_CcaHCCPVersion_Object((1,3,6,1,4,1,9,9,242,1,1,1),_CcaHCCPVersion_Type())
ccaHCCPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPVersion.setStatus(_B)
_CcaHCCPGroupTable_Object=MibTable
ccaHCCPGroupTable=_CcaHCCPGroupTable_Object((1,3,6,1,4,1,9,9,242,1,1,2))
if mibBuilder.loadTexts:ccaHCCPGroupTable.setStatus(_B)
_CcaHCCPGroupEntry_Object=MibTableRow
ccaHCCPGroupEntry=_CcaHCCPGroupEntry_Object((1,3,6,1,4,1,9,9,242,1,1,2,1))
ccaHCCPGroupEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:ccaHCCPGroupEntry.setStatus(_B)
class _CcaHCCPGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CcaHCCPGroupID_Type.__name__=_D
_CcaHCCPGroupID_Object=MibTableColumn
ccaHCCPGroupID=_CcaHCCPGroupID_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,1),_CcaHCCPGroupID_Type())
ccaHCCPGroupID.setMaxAccess(_H)
if mibBuilder.loadTexts:ccaHCCPGroupID.setStatus(_B)
class _CcaHCCPGroupAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('md5',2),('text',3)))
_CcaHCCPGroupAuthentication_Type.__name__=_D
_CcaHCCPGroupAuthentication_Object=MibTableColumn
ccaHCCPGroupAuthentication=_CcaHCCPGroupAuthentication_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,2),_CcaHCCPGroupAuthentication_Type())
ccaHCCPGroupAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupAuthentication.setStatus(_B)
_CcaHCCPGroupAuthKeyChain_Type=SnmpAdminString
_CcaHCCPGroupAuthKeyChain_Object=MibTableColumn
ccaHCCPGroupAuthKeyChain=_CcaHCCPGroupAuthKeyChain_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,3),_CcaHCCPGroupAuthKeyChain_Type())
ccaHCCPGroupAuthKeyChain.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupAuthKeyChain.setStatus(_B)
class _CcaHCCPGroupHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(333,5000))
_CcaHCCPGroupHelloTime_Type.__name__=_D
_CcaHCCPGroupHelloTime_Object=MibTableColumn
ccaHCCPGroupHelloTime=_CcaHCCPGroupHelloTime_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,4),_CcaHCCPGroupHelloTime_Type())
ccaHCCPGroupHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupHelloTime.setStatus(_B)
if mibBuilder.loadTexts:ccaHCCPGroupHelloTime.setUnits(_T)
class _CcaHCCPGroupHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,25000))
_CcaHCCPGroupHoldTime_Type.__name__=_D
_CcaHCCPGroupHoldTime_Object=MibTableColumn
ccaHCCPGroupHoldTime=_CcaHCCPGroupHoldTime_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,5),_CcaHCCPGroupHoldTime_Type())
ccaHCCPGroupHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupHoldTime.setStatus(_B)
if mibBuilder.loadTexts:ccaHCCPGroupHoldTime.setUnits(_T)
_CcaHCCPGroupRevertEnable_Type=TruthValue
_CcaHCCPGroupRevertEnable_Object=MibTableColumn
ccaHCCPGroupRevertEnable=_CcaHCCPGroupRevertEnable_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,6),_CcaHCCPGroupRevertEnable_Type())
ccaHCCPGroupRevertEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupRevertEnable.setStatus(_B)
_CcaHCCPGroupProtectIpAddrType_Type=InetAddressType
_CcaHCCPGroupProtectIpAddrType_Object=MibTableColumn
ccaHCCPGroupProtectIpAddrType=_CcaHCCPGroupProtectIpAddrType_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,7),_CcaHCCPGroupProtectIpAddrType_Type())
ccaHCCPGroupProtectIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupProtectIpAddrType.setStatus(_B)
_CcaHCCPGroupProtectIpAddress_Type=InetAddress
_CcaHCCPGroupProtectIpAddress_Object=MibTableColumn
ccaHCCPGroupProtectIpAddress=_CcaHCCPGroupProtectIpAddress_Object((1,3,6,1,4,1,9,9,242,1,1,2,1,8),_CcaHCCPGroupProtectIpAddress_Type())
ccaHCCPGroupProtectIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupProtectIpAddress.setStatus(_B)
_CcaHCCPGroupIfTable_Object=MibTable
ccaHCCPGroupIfTable=_CcaHCCPGroupIfTable_Object((1,3,6,1,4,1,9,9,242,1,1,3))
if mibBuilder.loadTexts:ccaHCCPGroupIfTable.setStatus(_B)
_CcaHCCPGroupIfEntry_Object=MibTableRow
ccaHCCPGroupIfEntry=_CcaHCCPGroupIfEntry_Object((1,3,6,1,4,1,9,9,242,1,1,3,1))
ccaHCCPGroupIfEntry.setIndexNames((0,_A,_E),(0,_F,_G))
if mibBuilder.loadTexts:ccaHCCPGroupIfEntry.setStatus(_B)
class _CcaHCCPGroupIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('protect',2),('working',3)))
_CcaHCCPGroupIfStatus_Type.__name__=_D
_CcaHCCPGroupIfStatus_Object=MibTableColumn
ccaHCCPGroupIfStatus=_CcaHCCPGroupIfStatus_Object((1,3,6,1,4,1,9,9,242,1,1,3,1,1),_CcaHCCPGroupIfStatus_Type())
ccaHCCPGroupIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupIfStatus.setStatus(_B)
class _CcaHCCPGroupIfRevertTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CcaHCCPGroupIfRevertTime_Type.__name__=_D
_CcaHCCPGroupIfRevertTime_Object=MibTableColumn
ccaHCCPGroupIfRevertTime=_CcaHCCPGroupIfRevertTime_Object((1,3,6,1,4,1,9,9,242,1,1,3,1,2),_CcaHCCPGroupIfRevertTime_Type())
ccaHCCPGroupIfRevertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupIfRevertTime.setStatus(_B)
_CcaHCCPGroupIfTrackEnable_Type=TruthValue
_CcaHCCPGroupIfTrackEnable_Object=MibTableColumn
ccaHCCPGroupIfTrackEnable=_CcaHCCPGroupIfTrackEnable_Object((1,3,6,1,4,1,9,9,242,1,1,3,1,3),_CcaHCCPGroupIfTrackEnable_Type())
ccaHCCPGroupIfTrackEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupIfTrackEnable.setStatus(_B)
class _CcaHCCPGroupIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('blocking',2)))
_CcaHCCPGroupIfState_Type.__name__=_D
_CcaHCCPGroupIfState_Object=MibTableColumn
ccaHCCPGroupIfState=_CcaHCCPGroupIfState_Object((1,3,6,1,4,1,9,9,242,1,1,3,1,4),_CcaHCCPGroupIfState_Type())
ccaHCCPGroupIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupIfState.setStatus(_B)
class _CcaHCCPGroupIfLastSwitchReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('holdTimeExpire',2),('hwIfDown',3),('failTest',4),('failLinkDown',5),('failBundleDown',6),('internal',7)))
_CcaHCCPGroupIfLastSwitchReason_Type.__name__=_D
_CcaHCCPGroupIfLastSwitchReason_Object=MibTableColumn
ccaHCCPGroupIfLastSwitchReason=_CcaHCCPGroupIfLastSwitchReason_Object((1,3,6,1,4,1,9,9,242,1,1,3,1,5),_CcaHCCPGroupIfLastSwitchReason_Type())
ccaHCCPGroupIfLastSwitchReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupIfLastSwitchReason.setStatus(_B)
_CcaHCCPGroupIfOnTransitions_Type=Counter32
_CcaHCCPGroupIfOnTransitions_Object=MibTableColumn
ccaHCCPGroupIfOnTransitions=_CcaHCCPGroupIfOnTransitions_Object((1,3,6,1,4,1,9,9,242,1,1,3,1,6),_CcaHCCPGroupIfOnTransitions_Type())
ccaHCCPGroupIfOnTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupIfOnTransitions.setStatus(_B)
_CcaHCCPGroupIfOffTransitions_Type=Counter32
_CcaHCCPGroupIfOffTransitions_Object=MibTableColumn
ccaHCCPGroupIfOffTransitions=_CcaHCCPGroupIfOffTransitions_Object((1,3,6,1,4,1,9,9,242,1,1,3,1,7),_CcaHCCPGroupIfOffTransitions_Type())
ccaHCCPGroupIfOffTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupIfOffTransitions.setStatus(_B)
_CcaHCCPGroupTrackInterfaceTable_Object=MibTable
ccaHCCPGroupTrackInterfaceTable=_CcaHCCPGroupTrackInterfaceTable_Object((1,3,6,1,4,1,9,9,242,1,1,4))
if mibBuilder.loadTexts:ccaHCCPGroupTrackInterfaceTable.setStatus(_B)
_CcaHCCPGroupTrackInterfaceEntry_Object=MibTableRow
ccaHCCPGroupTrackInterfaceEntry=_CcaHCCPGroupTrackInterfaceEntry_Object((1,3,6,1,4,1,9,9,242,1,1,4,1))
ccaHCCPGroupTrackInterfaceEntry.setIndexNames((0,_A,_E),(0,_F,_G),(0,_A,_U))
if mibBuilder.loadTexts:ccaHCCPGroupTrackInterfaceEntry.setStatus(_B)
class _CcaHCCPGroupTrackIfID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CcaHCCPGroupTrackIfID_Type.__name__=_D
_CcaHCCPGroupTrackIfID_Object=MibTableColumn
ccaHCCPGroupTrackIfID=_CcaHCCPGroupTrackIfID_Object((1,3,6,1,4,1,9,9,242,1,1,4,1,1),_CcaHCCPGroupTrackIfID_Type())
ccaHCCPGroupTrackIfID.setMaxAccess(_H)
if mibBuilder.loadTexts:ccaHCCPGroupTrackIfID.setStatus(_B)
class _CcaHCCPGroupTrackIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CcaHCCPGroupTrackIfDescr_Type.__name__=_Q
_CcaHCCPGroupTrackIfDescr_Object=MibTableColumn
ccaHCCPGroupTrackIfDescr=_CcaHCCPGroupTrackIfDescr_Object((1,3,6,1,4,1,9,9,242,1,1,4,1,2),_CcaHCCPGroupTrackIfDescr_Type())
ccaHCCPGroupTrackIfDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPGroupTrackIfDescr.setStatus(_B)
_CcaHCCPMemberTable_Object=MibTable
ccaHCCPMemberTable=_CcaHCCPMemberTable_Object((1,3,6,1,4,1,9,9,242,1,1,5))
if mibBuilder.loadTexts:ccaHCCPMemberTable.setStatus(_B)
_CcaHCCPMemberEntry_Object=MibTableRow
ccaHCCPMemberEntry=_CcaHCCPMemberEntry_Object((1,3,6,1,4,1,9,9,242,1,1,5,1))
ccaHCCPMemberEntry.setIndexNames((0,_A,_E),(0,_F,_G),(0,_A,_M))
if mibBuilder.loadTexts:ccaHCCPMemberEntry.setStatus(_B)
class _CcaHCCPMemberID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CcaHCCPMemberID_Type.__name__=_D
_CcaHCCPMemberID_Object=MibTableColumn
ccaHCCPMemberID=_CcaHCCPMemberID_Object((1,3,6,1,4,1,9,9,242,1,1,5,1,1),_CcaHCCPMemberID_Type())
ccaHCCPMemberID.setMaxAccess(_H)
if mibBuilder.loadTexts:ccaHCCPMemberID.setStatus(_B)
_CcaHCCPMemberIpAddrType_Type=InetAddressType
_CcaHCCPMemberIpAddrType_Object=MibTableColumn
ccaHCCPMemberIpAddrType=_CcaHCCPMemberIpAddrType_Object((1,3,6,1,4,1,9,9,242,1,1,5,1,2),_CcaHCCPMemberIpAddrType_Type())
ccaHCCPMemberIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemberIpAddrType.setStatus(_B)
_CcaHCCPMemberIpAddress_Type=InetAddress
_CcaHCCPMemberIpAddress_Object=MibTableColumn
ccaHCCPMemberIpAddress=_CcaHCCPMemberIpAddress_Object((1,3,6,1,4,1,9,9,242,1,1,5,1,3),_CcaHCCPMemberIpAddress_Type())
ccaHCCPMemberIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemberIpAddress.setStatus(_B)
class _CcaHCCPMemberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('standby',2),('nonFunctional',3)))
_CcaHCCPMemberState_Type.__name__=_D
_CcaHCCPMemberState_Object=MibTableColumn
ccaHCCPMemberState=_CcaHCCPMemberState_Object((1,3,6,1,4,1,9,9,242,1,1,5,1,4),_CcaHCCPMemberState_Type())
ccaHCCPMemberState.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemberState.setStatus(_B)
_CcaHCCPMemberSwitchNow_Type=TruthValue
_CcaHCCPMemberSwitchNow_Object=MibTableColumn
ccaHCCPMemberSwitchNow=_CcaHCCPMemberSwitchNow_Object((1,3,6,1,4,1,9,9,242,1,1,5,1,5),_CcaHCCPMemberSwitchNow_Type())
ccaHCCPMemberSwitchNow.setMaxAccess(_I)
if mibBuilder.loadTexts:ccaHCCPMemberSwitchNow.setStatus(_B)
_CcaHCCPMemChanSwitchTable_Object=MibTable
ccaHCCPMemChanSwitchTable=_CcaHCCPMemChanSwitchTable_Object((1,3,6,1,4,1,9,9,242,1,1,6))
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchTable.setStatus(_B)
_CcaHCCPMemChanSwitchEntry_Object=MibTableRow
ccaHCCPMemChanSwitchEntry=_CcaHCCPMemChanSwitchEntry_Object((1,3,6,1,4,1,9,9,242,1,1,6,1))
ccaHCCPMemChanSwitchEntry.setIndexNames((0,_A,_E),(0,_F,_G),(0,_A,_M),(0,_A,_V))
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchEntry.setStatus(_B)
class _CcaHCCPMemChanSwitchID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CcaHCCPMemChanSwitchID_Type.__name__=_D
_CcaHCCPMemChanSwitchID_Object=MibTableColumn
ccaHCCPMemChanSwitchID=_CcaHCCPMemChanSwitchID_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,1),_CcaHCCPMemChanSwitchID_Type())
ccaHCCPMemChanSwitchID.setMaxAccess(_H)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchID.setStatus(_B)
class _CcaHCCPMemChanSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('ucWavecom',2),('rfSwitchGrp',3),('rfSwitchModule',4)))
_CcaHCCPMemChanSwitchType_Type.__name__=_D
_CcaHCCPMemChanSwitchType_Object=MibTableColumn
ccaHCCPMemChanSwitchType=_CcaHCCPMemChanSwitchType_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,2),_CcaHCCPMemChanSwitchType_Type())
ccaHCCPMemChanSwitchType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchType.setStatus(_B)
_CcaHCCPMemChanSwitchIpAddrType_Type=InetAddressType
_CcaHCCPMemChanSwitchIpAddrType_Object=MibTableColumn
ccaHCCPMemChanSwitchIpAddrType=_CcaHCCPMemChanSwitchIpAddrType_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,3),_CcaHCCPMemChanSwitchIpAddrType_Type())
ccaHCCPMemChanSwitchIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchIpAddrType.setStatus(_B)
_CcaHCCPMemChanSwitchIpAddress_Type=InetAddress
_CcaHCCPMemChanSwitchIpAddress_Object=MibTableColumn
ccaHCCPMemChanSwitchIpAddress=_CcaHCCPMemChanSwitchIpAddress_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,4),_CcaHCCPMemChanSwitchIpAddress_Type())
ccaHCCPMemChanSwitchIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchIpAddress.setStatus(_B)
class _CcaHCCPMemChanSwitchModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CcaHCCPMemChanSwitchModule_Type.__name__=_D
_CcaHCCPMemChanSwitchModule_Object=MibTableColumn
ccaHCCPMemChanSwitchModule=_CcaHCCPMemChanSwitchModule_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,5),_CcaHCCPMemChanSwitchModule_Type())
ccaHCCPMemChanSwitchModule.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchModule.setStatus(_B)
_CcaHCCPMemChanSwitchProtIpAddrType_Type=InetAddressType
_CcaHCCPMemChanSwitchProtIpAddrType_Object=MibTableColumn
ccaHCCPMemChanSwitchProtIpAddrType=_CcaHCCPMemChanSwitchProtIpAddrType_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,6),_CcaHCCPMemChanSwitchProtIpAddrType_Type())
ccaHCCPMemChanSwitchProtIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchProtIpAddrType.setStatus(_B)
_CcaHCCPMemChanSwitchProtIpAddr_Type=InetAddress
_CcaHCCPMemChanSwitchProtIpAddr_Object=MibTableColumn
ccaHCCPMemChanSwitchProtIpAddr=_CcaHCCPMemChanSwitchProtIpAddr_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,7),_CcaHCCPMemChanSwitchProtIpAddr_Type())
ccaHCCPMemChanSwitchProtIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchProtIpAddr.setStatus(_B)
class _CcaHCCPMemChanSwitchProtModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CcaHCCPMemChanSwitchProtModule_Type.__name__=_D
_CcaHCCPMemChanSwitchProtModule_Object=MibTableColumn
ccaHCCPMemChanSwitchProtModule=_CcaHCCPMemChanSwitchProtModule_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,8),_CcaHCCPMemChanSwitchProtModule_Type())
ccaHCCPMemChanSwitchProtModule.setMaxAccess(_C)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchProtModule.setStatus(_B)
class _CcaHCCPMemChanSwitchPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CcaHCCPMemChanSwitchPosition_Type.__name__=_D
_CcaHCCPMemChanSwitchPosition_Object=MibTableColumn
ccaHCCPMemChanSwitchPosition=_CcaHCCPMemChanSwitchPosition_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,9),_CcaHCCPMemChanSwitchPosition_Type())
ccaHCCPMemChanSwitchPosition.setMaxAccess(_I)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchPosition.setStatus(_B)
_CcaHCCPMemChanSwitchSnmpEnable_Type=TruthValue
_CcaHCCPMemChanSwitchSnmpEnable_Object=MibTableColumn
ccaHCCPMemChanSwitchSnmpEnable=_CcaHCCPMemChanSwitchSnmpEnable_Object((1,3,6,1,4,1,9,9,242,1,1,6,1,10),_CcaHCCPMemChanSwitchSnmpEnable_Type())
ccaHCCPMemChanSwitchSnmpEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:ccaHCCPMemChanSwitchSnmpEnable.setStatus(_B)
class _CcaHCCPOnOffNotificationEnable_Type(TruthValue):defaultValue=2
_CcaHCCPOnOffNotificationEnable_Type.__name__=_R
_CcaHCCPOnOffNotificationEnable_Object=MibScalar
ccaHCCPOnOffNotificationEnable=_CcaHCCPOnOffNotificationEnable_Object((1,3,6,1,4,1,9,9,242,1,1,7),_CcaHCCPOnOffNotificationEnable_Type())
ccaHCCPOnOffNotificationEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:ccaHCCPOnOffNotificationEnable.setStatus(_B)
_CiscoCableAvailabilityMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoCableAvailabilityMIBNotificationsPrefix=_CiscoCableAvailabilityMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,242,2))
_CiscoCableAvailabilityMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoCableAvailabilityMIBNotifications=_CiscoCableAvailabilityMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,242,2,0))
_CiscoCableAvailabilityMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCableAvailabilityMIBConformance=_CiscoCableAvailabilityMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,242,3))
_CiscoCableAvailabilityMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCableAvailabilityMIBCompliances=_CiscoCableAvailabilityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,242,3,1))
_CiscoCableAvailabilityMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCableAvailabilityMIBGroups=_CiscoCableAvailabilityMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,242,3,2))
ccaHCCPGroup=ObjectGroup((1,3,6,1,4,1,9,9,242,3,2,1))
ccaHCCPGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_J),(_A,_K),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ccaHCCPGroup.setStatus(_B)
ccaHCCPMemberGroup=ObjectGroup((1,3,6,1,4,1,9,9,242,3,2,2))
ccaHCCPMemberGroup.setObjects(*((_A,_l),(_A,_m),(_A,_L),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ccaHCCPMemberGroup.setStatus(_B)
ccaHCCPOnNotification=NotificationType((1,3,6,1,4,1,9,9,242,2,0,1))
ccaHCCPOnNotification.setObjects(*((_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ccaHCCPOnNotification.setStatus(_B)
ccaHCCPOffNotification=NotificationType((1,3,6,1,4,1,9,9,242,2,0,2))
ccaHCCPOffNotification.setObjects(*((_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ccaHCCPOffNotification.setStatus(_B)
ccaHCCPNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,242,3,2,3))
ccaHCCPNotificationGroup.setObjects(*((_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ccaHCCPNotificationGroup.setStatus(_B)
ciscoCableAvailabilityCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,242,3,1,1))
ciscoCableAvailabilityCompliance.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoCableAvailabilityCompliance.setStatus('deprecated')
ciscoCableAvailabilityComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,242,3,1,2))
ciscoCableAvailabilityComplianceRev1.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoCableAvailabilityComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoCableAvailabilityMIB':ciscoCableAvailabilityMIB,'ciscoCableAvailabilityMIBObjects':ciscoCableAvailabilityMIBObjects,'ccaHCCPObjects':ccaHCCPObjects,_W:ccaHCCPVersion,'ccaHCCPGroupTable':ccaHCCPGroupTable,'ccaHCCPGroupEntry':ccaHCCPGroupEntry,_E:ccaHCCPGroupID,_Y:ccaHCCPGroupAuthentication,_Z:ccaHCCPGroupAuthKeyChain,_a:ccaHCCPGroupHelloTime,_b:ccaHCCPGroupHoldTime,_c:ccaHCCPGroupRevertEnable,_d:ccaHCCPGroupProtectIpAddrType,_e:ccaHCCPGroupProtectIpAddress,'ccaHCCPGroupIfTable':ccaHCCPGroupIfTable,'ccaHCCPGroupIfEntry':ccaHCCPGroupIfEntry,_J:ccaHCCPGroupIfStatus,_f:ccaHCCPGroupIfRevertTime,_g:ccaHCCPGroupIfTrackEnable,_k:ccaHCCPGroupIfState,_K:ccaHCCPGroupIfLastSwitchReason,_h:ccaHCCPGroupIfOnTransitions,_i:ccaHCCPGroupIfOffTransitions,'ccaHCCPGroupTrackInterfaceTable':ccaHCCPGroupTrackInterfaceTable,'ccaHCCPGroupTrackInterfaceEntry':ccaHCCPGroupTrackInterfaceEntry,_U:ccaHCCPGroupTrackIfID,_j:ccaHCCPGroupTrackIfDescr,'ccaHCCPMemberTable':ccaHCCPMemberTable,'ccaHCCPMemberEntry':ccaHCCPMemberEntry,_M:ccaHCCPMemberID,_l:ccaHCCPMemberIpAddrType,_m:ccaHCCPMemberIpAddress,_L:ccaHCCPMemberState,_n:ccaHCCPMemberSwitchNow,'ccaHCCPMemChanSwitchTable':ccaHCCPMemChanSwitchTable,'ccaHCCPMemChanSwitchEntry':ccaHCCPMemChanSwitchEntry,_V:ccaHCCPMemChanSwitchID,_o:ccaHCCPMemChanSwitchType,_p:ccaHCCPMemChanSwitchIpAddrType,_q:ccaHCCPMemChanSwitchIpAddress,_r:ccaHCCPMemChanSwitchModule,_s:ccaHCCPMemChanSwitchProtIpAddrType,_t:ccaHCCPMemChanSwitchProtIpAddr,_u:ccaHCCPMemChanSwitchProtModule,_v:ccaHCCPMemChanSwitchPosition,_w:ccaHCCPMemChanSwitchSnmpEnable,_X:ccaHCCPOnOffNotificationEnable,'ciscoCableAvailabilityMIBNotificationsPrefix':ciscoCableAvailabilityMIBNotificationsPrefix,'ciscoCableAvailabilityMIBNotifications':ciscoCableAvailabilityMIBNotifications,_x:ccaHCCPOnNotification,_y:ccaHCCPOffNotification,'ciscoCableAvailabilityMIBConformance':ciscoCableAvailabilityMIBConformance,'ciscoCableAvailabilityMIBCompliances':ciscoCableAvailabilityMIBCompliances,'ciscoCableAvailabilityCompliance':ciscoCableAvailabilityCompliance,'ciscoCableAvailabilityComplianceRev1':ciscoCableAvailabilityComplianceRev1,'ciscoCableAvailabilityMIBGroups':ciscoCableAvailabilityMIBGroups,_N:ccaHCCPGroup,_O:ccaHCCPMemberGroup,_P:ccaHCCPNotificationGroup})