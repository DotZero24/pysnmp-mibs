_y='natRsvdPortTrigInfoAppIndex'
_x='natPolicyAclName'
_w='natPolicyId'
_v='natPolicyType'
_u='natPortTrigInfoProtocol'
_t='natPortTrigInfoOutBoundPortRange'
_s='natPortTrigInfoInBoundPortRange'
_r='natIKESessionInitCookie'
_q='natIKESessionOutsideIp'
_p='natIKESessionLocalIp'
_o='natIKESessionInterfaceNum'
_n='natIPSecPendingSPIOutside'
_m='natIPSecPendingSPIInside'
_l='natIPSecPendingOutsideIp'
_k='natIPSecPendingLocalIp'
_j='natIPSecPendingInterfaceNum'
_i='natIPSecSessionSPIOutside'
_h='natIPSecSessionSPIInside'
_g='natIPSecSessionOutsideIp'
_f='natIPSecSessionLocalIp'
_e='natIPSecSessionInterfaceNum'
_d='natIfInterfaceNumber'
_c='natStaticNaptProtocolNumber'
_b='natStaticNaptEndLocalPort'
_a='natStaticNaptStartLocalPort'
_Z='natStaticNaptLocalIp'
_Y='natStaticNaptInterfaceNum'
_X='natStaticLocalIp'
_W='natStaticInterfaceNum'
_V='natLocalAddressLocalIp'
_U='natLocalAddressInterfaceNumber'
_T='natGlobalAddressTranslatedLocalIp'
_S='natGlobalAddressInterfaceNum'
_R='natDynamicTransOutsidePort'
_Q='natDynamicTransOutsideIp'
_P='natDynamicTransLocalPort'
_O='natDynamicTransLocalIp'
_N='natDynamicTransInterfaceNum'
_M='TimeStamp'
_L='any'
_K='udp'
_J='tcp'
_I='OctetString'
_H='Status'
_G='DisplayString'
_F='read-only'
_E='read-write'
_D='Integer32'
_C='not-accessible'
_B='FutureNat-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_M)
futureNatMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,14))
if mibBuilder.loadTexts:futureNatMIB.setRevisions(('2012-09-05 00:00',))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Nat_ObjectIdentity=ObjectIdentity
nat=_Nat_ObjectIdentity((1,3,6,1,4,1,10876,101,1,14,1))
_NatStatInfo_ObjectIdentity=ObjectIdentity
natStatInfo=_NatStatInfo_ObjectIdentity((1,3,6,1,4,1,10876,101,1,14,1,1))
class _NatEnable_Type(Status):defaultValue=1
_NatEnable_Type.__name__=_H
_NatEnable_Object=MibScalar
natEnable=_NatEnable_Object((1,3,6,1,4,1,10876,101,1,14,1,1,1),_NatEnable_Type())
natEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:natEnable.setStatus(_A)
class _NatTypicalNumberOfEntries_Type(Integer32):defaultValue=9000
_NatTypicalNumberOfEntries_Type.__name__=_D
_NatTypicalNumberOfEntries_Object=MibScalar
natTypicalNumberOfEntries=_NatTypicalNumberOfEntries_Object((1,3,6,1,4,1,10876,101,1,14,1,1,2),_NatTypicalNumberOfEntries_Type())
natTypicalNumberOfEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:natTypicalNumberOfEntries.setStatus(_A)
class _NatTranslatedLocalPortStart_Type(Integer32):defaultValue=6001
_NatTranslatedLocalPortStart_Type.__name__=_D
_NatTranslatedLocalPortStart_Object=MibScalar
natTranslatedLocalPortStart=_NatTranslatedLocalPortStart_Object((1,3,6,1,4,1,10876,101,1,14,1,1,3),_NatTranslatedLocalPortStart_Type())
natTranslatedLocalPortStart.setMaxAccess(_E)
if mibBuilder.loadTexts:natTranslatedLocalPortStart.setStatus(_A)
class _NatIdleTimeOut_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_NatIdleTimeOut_Type.__name__=_D
_NatIdleTimeOut_Object=MibScalar
natIdleTimeOut=_NatIdleTimeOut_Object((1,3,6,1,4,1,10876,101,1,14,1,1,4),_NatIdleTimeOut_Type())
natIdleTimeOut.setMaxAccess(_E)
if mibBuilder.loadTexts:natIdleTimeOut.setStatus(_A)
class _NatTcpTimeOut_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,86400))
_NatTcpTimeOut_Type.__name__=_D
_NatTcpTimeOut_Object=MibScalar
natTcpTimeOut=_NatTcpTimeOut_Object((1,3,6,1,4,1,10876,101,1,14,1,1,5),_NatTcpTimeOut_Type())
natTcpTimeOut.setMaxAccess(_E)
if mibBuilder.loadTexts:natTcpTimeOut.setStatus(_A)
class _NatUdpTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,86400))
_NatUdpTimeOut_Type.__name__=_D
_NatUdpTimeOut_Object=MibScalar
natUdpTimeOut=_NatUdpTimeOut_Object((1,3,6,1,4,1,10876,101,1,14,1,1,6),_NatUdpTimeOut_Type())
natUdpTimeOut.setMaxAccess(_E)
if mibBuilder.loadTexts:natUdpTimeOut.setStatus(_A)
class _NatTrcFlag_Type(Integer32):defaultValue=0
_NatTrcFlag_Type.__name__=_D
_NatTrcFlag_Object=MibScalar
natTrcFlag=_NatTrcFlag_Object((1,3,6,1,4,1,10876,101,1,14,1,1,7),_NatTrcFlag_Type())
natTrcFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:natTrcFlag.setStatus(_A)
_NatStatDynamicAllocFailureCount_Type=Counter32
_NatStatDynamicAllocFailureCount_Object=MibScalar
natStatDynamicAllocFailureCount=_NatStatDynamicAllocFailureCount_Object((1,3,6,1,4,1,10876,101,1,14,1,1,8),_NatStatDynamicAllocFailureCount_Type())
natStatDynamicAllocFailureCount.setMaxAccess(_F)
if mibBuilder.loadTexts:natStatDynamicAllocFailureCount.setStatus(_A)
_NatStatTotalNumberOfTranslations_Type=Counter32
_NatStatTotalNumberOfTranslations_Object=MibScalar
natStatTotalNumberOfTranslations=_NatStatTotalNumberOfTranslations_Object((1,3,6,1,4,1,10876,101,1,14,1,1,9),_NatStatTotalNumberOfTranslations_Type())
natStatTotalNumberOfTranslations.setMaxAccess(_F)
if mibBuilder.loadTexts:natStatTotalNumberOfTranslations.setStatus(_A)
_NatStatTotalNumberOfActiveSessions_Type=Counter32
_NatStatTotalNumberOfActiveSessions_Object=MibScalar
natStatTotalNumberOfActiveSessions=_NatStatTotalNumberOfActiveSessions_Object((1,3,6,1,4,1,10876,101,1,14,1,1,10),_NatStatTotalNumberOfActiveSessions_Type())
natStatTotalNumberOfActiveSessions.setMaxAccess(_F)
if mibBuilder.loadTexts:natStatTotalNumberOfActiveSessions.setStatus(_A)
_NatStatTotalNumberOfPktsDropped_Type=Counter32
_NatStatTotalNumberOfPktsDropped_Object=MibScalar
natStatTotalNumberOfPktsDropped=_NatStatTotalNumberOfPktsDropped_Object((1,3,6,1,4,1,10876,101,1,14,1,1,11),_NatStatTotalNumberOfPktsDropped_Type())
natStatTotalNumberOfPktsDropped.setMaxAccess(_F)
if mibBuilder.loadTexts:natStatTotalNumberOfPktsDropped.setStatus(_A)
_NatStatTotalNumberOfSessionsClosed_Type=Counter32
_NatStatTotalNumberOfSessionsClosed_Object=MibScalar
natStatTotalNumberOfSessionsClosed=_NatStatTotalNumberOfSessionsClosed_Object((1,3,6,1,4,1,10876,101,1,14,1,1,12),_NatStatTotalNumberOfSessionsClosed_Type())
natStatTotalNumberOfSessionsClosed.setMaxAccess(_F)
if mibBuilder.loadTexts:natStatTotalNumberOfSessionsClosed.setStatus(_A)
class _NatIKEPortTranslation_Type(Status):defaultValue=2
_NatIKEPortTranslation_Type.__name__=_H
_NatIKEPortTranslation_Object=MibScalar
natIKEPortTranslation=_NatIKEPortTranslation_Object((1,3,6,1,4,1,10876,101,1,14,1,1,13),_NatIKEPortTranslation_Type())
natIKEPortTranslation.setMaxAccess(_E)
if mibBuilder.loadTexts:natIKEPortTranslation.setStatus(_A)
class _NatIKETimeout_Type(Integer32):defaultValue=28800
_NatIKETimeout_Type.__name__=_D
_NatIKETimeout_Object=MibScalar
natIKETimeout=_NatIKETimeout_Object((1,3,6,1,4,1,10876,101,1,14,1,1,14),_NatIKETimeout_Type())
natIKETimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:natIKETimeout.setStatus(_A)
class _NatIPSecTimeout_Type(Integer32):defaultValue=28800
_NatIPSecTimeout_Type.__name__=_D
_NatIPSecTimeout_Object=MibScalar
natIPSecTimeout=_NatIPSecTimeout_Object((1,3,6,1,4,1,10876,101,1,14,1,1,15),_NatIPSecTimeout_Type())
natIPSecTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:natIPSecTimeout.setStatus(_A)
class _NatIPSecPendingTimeout_Type(Integer32):defaultValue=30
_NatIPSecPendingTimeout_Type.__name__=_D
_NatIPSecPendingTimeout_Object=MibScalar
natIPSecPendingTimeout=_NatIPSecPendingTimeout_Object((1,3,6,1,4,1,10876,101,1,14,1,1,16),_NatIPSecPendingTimeout_Type())
natIPSecPendingTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:natIPSecPendingTimeout.setStatus(_A)
class _NatIPSecMaxRetry_Type(Integer32):defaultValue=3
_NatIPSecMaxRetry_Type.__name__=_D
_NatIPSecMaxRetry_Object=MibScalar
natIPSecMaxRetry=_NatIPSecMaxRetry_Object((1,3,6,1,4,1,10876,101,1,14,1,1,17),_NatIPSecMaxRetry_Type())
natIPSecMaxRetry.setMaxAccess(_E)
if mibBuilder.loadTexts:natIPSecMaxRetry.setStatus(_A)
class _SipAlgPort_Type(Integer32):defaultValue=5060
_SipAlgPort_Type.__name__=_D
_SipAlgPort_Object=MibScalar
sipAlgPort=_SipAlgPort_Object((1,3,6,1,4,1,10876,101,1,14,1,1,18),_SipAlgPort_Type())
sipAlgPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sipAlgPort.setStatus(_A)
class _NatSipAlgPartialEntryTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(212,86400))
_NatSipAlgPartialEntryTimeOut_Type.__name__=_D
_NatSipAlgPartialEntryTimeOut_Object=MibScalar
natSipAlgPartialEntryTimeOut=_NatSipAlgPartialEntryTimeOut_Object((1,3,6,1,4,1,10876,101,1,14,1,1,19),_NatSipAlgPartialEntryTimeOut_Type())
natSipAlgPartialEntryTimeOut.setMaxAccess(_E)
if mibBuilder.loadTexts:natSipAlgPartialEntryTimeOut.setStatus(_A)
_NatDynamicTransTable_Object=MibTable
natDynamicTransTable=_NatDynamicTransTable_Object((1,3,6,1,4,1,10876,101,1,14,1,2))
if mibBuilder.loadTexts:natDynamicTransTable.setStatus(_A)
_NatDynamicTransEntry_Object=MibTableRow
natDynamicTransEntry=_NatDynamicTransEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1))
natDynamicTransEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:natDynamicTransEntry.setStatus(_A)
class _NatDynamicTransInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatDynamicTransInterfaceNum_Type.__name__=_D
_NatDynamicTransInterfaceNum_Object=MibTableColumn
natDynamicTransInterfaceNum=_NatDynamicTransInterfaceNum_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,1),_NatDynamicTransInterfaceNum_Type())
natDynamicTransInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:natDynamicTransInterfaceNum.setStatus(_A)
_NatDynamicTransLocalIp_Type=IpAddress
_NatDynamicTransLocalIp_Object=MibTableColumn
natDynamicTransLocalIp=_NatDynamicTransLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,2),_NatDynamicTransLocalIp_Type())
natDynamicTransLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natDynamicTransLocalIp.setStatus(_A)
_NatDynamicTransTranslatedLocalIp_Type=IpAddress
_NatDynamicTransTranslatedLocalIp_Object=MibTableColumn
natDynamicTransTranslatedLocalIp=_NatDynamicTransTranslatedLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,3),_NatDynamicTransTranslatedLocalIp_Type())
natDynamicTransTranslatedLocalIp.setMaxAccess(_F)
if mibBuilder.loadTexts:natDynamicTransTranslatedLocalIp.setStatus(_A)
class _NatDynamicTransLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NatDynamicTransLocalPort_Type.__name__=_D
_NatDynamicTransLocalPort_Object=MibTableColumn
natDynamicTransLocalPort=_NatDynamicTransLocalPort_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,4),_NatDynamicTransLocalPort_Type())
natDynamicTransLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natDynamicTransLocalPort.setStatus(_A)
_NatDynamicTransTranslatedLocalPort_Type=Integer32
_NatDynamicTransTranslatedLocalPort_Object=MibTableColumn
natDynamicTransTranslatedLocalPort=_NatDynamicTransTranslatedLocalPort_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,5),_NatDynamicTransTranslatedLocalPort_Type())
natDynamicTransTranslatedLocalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:natDynamicTransTranslatedLocalPort.setStatus(_A)
_NatDynamicTransOutsideIp_Type=IpAddress
_NatDynamicTransOutsideIp_Object=MibTableColumn
natDynamicTransOutsideIp=_NatDynamicTransOutsideIp_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,6),_NatDynamicTransOutsideIp_Type())
natDynamicTransOutsideIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natDynamicTransOutsideIp.setStatus(_A)
class _NatDynamicTransOutsidePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NatDynamicTransOutsidePort_Type.__name__=_D
_NatDynamicTransOutsidePort_Object=MibTableColumn
natDynamicTransOutsidePort=_NatDynamicTransOutsidePort_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,7),_NatDynamicTransOutsidePort_Type())
natDynamicTransOutsidePort.setMaxAccess(_C)
if mibBuilder.loadTexts:natDynamicTransOutsidePort.setStatus(_A)
_NatDynamicTransLastUseTime_Type=Integer32
_NatDynamicTransLastUseTime_Object=MibTableColumn
natDynamicTransLastUseTime=_NatDynamicTransLastUseTime_Object((1,3,6,1,4,1,10876,101,1,14,1,2,1,8),_NatDynamicTransLastUseTime_Type())
natDynamicTransLastUseTime.setMaxAccess(_F)
if mibBuilder.loadTexts:natDynamicTransLastUseTime.setStatus(_A)
_NatGlobalAddressTable_Object=MibTable
natGlobalAddressTable=_NatGlobalAddressTable_Object((1,3,6,1,4,1,10876,101,1,14,1,3))
if mibBuilder.loadTexts:natGlobalAddressTable.setStatus(_A)
_NatGlobalAddressEntry_Object=MibTableRow
natGlobalAddressEntry=_NatGlobalAddressEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,3,1))
natGlobalAddressEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:natGlobalAddressEntry.setStatus(_A)
class _NatGlobalAddressInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatGlobalAddressInterfaceNum_Type.__name__=_D
_NatGlobalAddressInterfaceNum_Object=MibTableColumn
natGlobalAddressInterfaceNum=_NatGlobalAddressInterfaceNum_Object((1,3,6,1,4,1,10876,101,1,14,1,3,1,1),_NatGlobalAddressInterfaceNum_Type())
natGlobalAddressInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:natGlobalAddressInterfaceNum.setStatus(_A)
_NatGlobalAddressTranslatedLocalIp_Type=IpAddress
_NatGlobalAddressTranslatedLocalIp_Object=MibTableColumn
natGlobalAddressTranslatedLocalIp=_NatGlobalAddressTranslatedLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,3,1,2),_NatGlobalAddressTranslatedLocalIp_Type())
natGlobalAddressTranslatedLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natGlobalAddressTranslatedLocalIp.setStatus(_A)
_NatGlobalAddressMask_Type=IpAddress
_NatGlobalAddressMask_Object=MibTableColumn
natGlobalAddressMask=_NatGlobalAddressMask_Object((1,3,6,1,4,1,10876,101,1,14,1,3,1,3),_NatGlobalAddressMask_Type())
natGlobalAddressMask.setMaxAccess(_E)
if mibBuilder.loadTexts:natGlobalAddressMask.setStatus(_A)
_NatGlobalAddressEntryStatus_Type=RowStatus
_NatGlobalAddressEntryStatus_Object=MibTableColumn
natGlobalAddressEntryStatus=_NatGlobalAddressEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,3,1,4),_NatGlobalAddressEntryStatus_Type())
natGlobalAddressEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natGlobalAddressEntryStatus.setStatus(_A)
_NatLocalAddressTable_Object=MibTable
natLocalAddressTable=_NatLocalAddressTable_Object((1,3,6,1,4,1,10876,101,1,14,1,4))
if mibBuilder.loadTexts:natLocalAddressTable.setStatus(_A)
_NatLocalAddressEntry_Object=MibTableRow
natLocalAddressEntry=_NatLocalAddressEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,4,1))
natLocalAddressEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:natLocalAddressEntry.setStatus(_A)
class _NatLocalAddressInterfaceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatLocalAddressInterfaceNumber_Type.__name__=_D
_NatLocalAddressInterfaceNumber_Object=MibTableColumn
natLocalAddressInterfaceNumber=_NatLocalAddressInterfaceNumber_Object((1,3,6,1,4,1,10876,101,1,14,1,4,1,1),_NatLocalAddressInterfaceNumber_Type())
natLocalAddressInterfaceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:natLocalAddressInterfaceNumber.setStatus(_A)
_NatLocalAddressLocalIp_Type=IpAddress
_NatLocalAddressLocalIp_Object=MibTableColumn
natLocalAddressLocalIp=_NatLocalAddressLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,4,1,2),_NatLocalAddressLocalIp_Type())
natLocalAddressLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natLocalAddressLocalIp.setStatus(_A)
_NatLocalAddressMask_Type=IpAddress
_NatLocalAddressMask_Object=MibTableColumn
natLocalAddressMask=_NatLocalAddressMask_Object((1,3,6,1,4,1,10876,101,1,14,1,4,1,3),_NatLocalAddressMask_Type())
natLocalAddressMask.setMaxAccess(_E)
if mibBuilder.loadTexts:natLocalAddressMask.setStatus(_A)
_NatLocalAddressEntryStatus_Type=RowStatus
_NatLocalAddressEntryStatus_Object=MibTableColumn
natLocalAddressEntryStatus=_NatLocalAddressEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,4,1,4),_NatLocalAddressEntryStatus_Type())
natLocalAddressEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natLocalAddressEntryStatus.setStatus(_A)
_NatStaticTable_Object=MibTable
natStaticTable=_NatStaticTable_Object((1,3,6,1,4,1,10876,101,1,14,1,5))
if mibBuilder.loadTexts:natStaticTable.setStatus(_A)
_NatStaticEntry_Object=MibTableRow
natStaticEntry=_NatStaticEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,5,1))
natStaticEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:natStaticEntry.setStatus(_A)
class _NatStaticInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatStaticInterfaceNum_Type.__name__=_D
_NatStaticInterfaceNum_Object=MibTableColumn
natStaticInterfaceNum=_NatStaticInterfaceNum_Object((1,3,6,1,4,1,10876,101,1,14,1,5,1,1),_NatStaticInterfaceNum_Type())
natStaticInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:natStaticInterfaceNum.setStatus(_A)
_NatStaticLocalIp_Type=IpAddress
_NatStaticLocalIp_Object=MibTableColumn
natStaticLocalIp=_NatStaticLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,5,1,2),_NatStaticLocalIp_Type())
natStaticLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natStaticLocalIp.setStatus(_A)
_NatStaticTranslatedLocalIp_Type=IpAddress
_NatStaticTranslatedLocalIp_Object=MibTableColumn
natStaticTranslatedLocalIp=_NatStaticTranslatedLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,5,1,3),_NatStaticTranslatedLocalIp_Type())
natStaticTranslatedLocalIp.setMaxAccess(_E)
if mibBuilder.loadTexts:natStaticTranslatedLocalIp.setStatus(_A)
_NatStaticEntryStatus_Type=RowStatus
_NatStaticEntryStatus_Object=MibTableColumn
natStaticEntryStatus=_NatStaticEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,5,1,4),_NatStaticEntryStatus_Type())
natStaticEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natStaticEntryStatus.setStatus(_A)
_NatStaticNaptTable_Object=MibTable
natStaticNaptTable=_NatStaticNaptTable_Object((1,3,6,1,4,1,10876,101,1,14,1,6))
if mibBuilder.loadTexts:natStaticNaptTable.setStatus(_A)
_NatStaticNaptEntry_Object=MibTableRow
natStaticNaptEntry=_NatStaticNaptEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1))
natStaticNaptEntry.setIndexNames((0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:natStaticNaptEntry.setStatus(_A)
class _NatStaticNaptInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatStaticNaptInterfaceNum_Type.__name__=_D
_NatStaticNaptInterfaceNum_Object=MibTableColumn
natStaticNaptInterfaceNum=_NatStaticNaptInterfaceNum_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,1),_NatStaticNaptInterfaceNum_Type())
natStaticNaptInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:natStaticNaptInterfaceNum.setStatus(_A)
_NatStaticNaptLocalIp_Type=IpAddress
_NatStaticNaptLocalIp_Object=MibTableColumn
natStaticNaptLocalIp=_NatStaticNaptLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,2),_NatStaticNaptLocalIp_Type())
natStaticNaptLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natStaticNaptLocalIp.setStatus(_A)
class _NatStaticNaptStartLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NatStaticNaptStartLocalPort_Type.__name__=_D
_NatStaticNaptStartLocalPort_Object=MibTableColumn
natStaticNaptStartLocalPort=_NatStaticNaptStartLocalPort_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,3),_NatStaticNaptStartLocalPort_Type())
natStaticNaptStartLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natStaticNaptStartLocalPort.setStatus(_A)
class _NatStaticNaptEndLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NatStaticNaptEndLocalPort_Type.__name__=_D
_NatStaticNaptEndLocalPort_Object=MibTableColumn
natStaticNaptEndLocalPort=_NatStaticNaptEndLocalPort_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,4),_NatStaticNaptEndLocalPort_Type())
natStaticNaptEndLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natStaticNaptEndLocalPort.setStatus(_A)
class _NatStaticNaptProtocolNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17,255)));namedValues=NamedValues(*((_J,6),(_K,17),(_L,255)))
_NatStaticNaptProtocolNumber_Type.__name__=_D
_NatStaticNaptProtocolNumber_Object=MibTableColumn
natStaticNaptProtocolNumber=_NatStaticNaptProtocolNumber_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,5),_NatStaticNaptProtocolNumber_Type())
natStaticNaptProtocolNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:natStaticNaptProtocolNumber.setStatus(_A)
_NatStaticNaptTranslatedLocalIp_Type=IpAddress
_NatStaticNaptTranslatedLocalIp_Object=MibTableColumn
natStaticNaptTranslatedLocalIp=_NatStaticNaptTranslatedLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,6),_NatStaticNaptTranslatedLocalIp_Type())
natStaticNaptTranslatedLocalIp.setMaxAccess(_E)
if mibBuilder.loadTexts:natStaticNaptTranslatedLocalIp.setStatus(_A)
class _NatStaticNaptTranslatedLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NatStaticNaptTranslatedLocalPort_Type.__name__=_D
_NatStaticNaptTranslatedLocalPort_Object=MibTableColumn
natStaticNaptTranslatedLocalPort=_NatStaticNaptTranslatedLocalPort_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,7),_NatStaticNaptTranslatedLocalPort_Type())
natStaticNaptTranslatedLocalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:natStaticNaptTranslatedLocalPort.setStatus(_A)
class _NatStaticNaptDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_NatStaticNaptDescription_Type.__name__=_G
_NatStaticNaptDescription_Object=MibTableColumn
natStaticNaptDescription=_NatStaticNaptDescription_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,8),_NatStaticNaptDescription_Type())
natStaticNaptDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:natStaticNaptDescription.setStatus(_A)
_NatStaticNaptEntryStatus_Type=RowStatus
_NatStaticNaptEntryStatus_Object=MibTableColumn
natStaticNaptEntryStatus=_NatStaticNaptEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,6,1,9),_NatStaticNaptEntryStatus_Type())
natStaticNaptEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natStaticNaptEntryStatus.setStatus(_A)
_NatIfTable_Object=MibTable
natIfTable=_NatIfTable_Object((1,3,6,1,4,1,10876,101,1,14,1,7))
if mibBuilder.loadTexts:natIfTable.setStatus(_A)
_NatIfEntry_Object=MibTableRow
natIfEntry=_NatIfEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,7,1))
natIfEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:natIfEntry.setStatus(_A)
class _NatIfInterfaceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatIfInterfaceNumber_Type.__name__=_D
_NatIfInterfaceNumber_Object=MibTableColumn
natIfInterfaceNumber=_NatIfInterfaceNumber_Object((1,3,6,1,4,1,10876,101,1,14,1,7,1,1),_NatIfInterfaceNumber_Type())
natIfInterfaceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:natIfInterfaceNumber.setStatus(_A)
class _NatIfNat_Type(Status):defaultValue=2
_NatIfNat_Type.__name__=_H
_NatIfNat_Object=MibTableColumn
natIfNat=_NatIfNat_Object((1,3,6,1,4,1,10876,101,1,14,1,7,1,2),_NatIfNat_Type())
natIfNat.setMaxAccess(_E)
if mibBuilder.loadTexts:natIfNat.setStatus(_A)
class _NatIfNapt_Type(Status):defaultValue=2
_NatIfNapt_Type.__name__=_H
_NatIfNapt_Object=MibTableColumn
natIfNapt=_NatIfNapt_Object((1,3,6,1,4,1,10876,101,1,14,1,7,1,3),_NatIfNapt_Type())
natIfNapt.setMaxAccess(_E)
if mibBuilder.loadTexts:natIfNapt.setStatus(_A)
class _NatIfTwoWayNat_Type(Status):defaultValue=2
_NatIfTwoWayNat_Type.__name__=_H
_NatIfTwoWayNat_Object=MibTableColumn
natIfTwoWayNat=_NatIfTwoWayNat_Object((1,3,6,1,4,1,10876,101,1,14,1,7,1,4),_NatIfTwoWayNat_Type())
natIfTwoWayNat.setMaxAccess(_E)
if mibBuilder.loadTexts:natIfTwoWayNat.setStatus(_A)
_NatIfEntryStatus_Type=RowStatus
_NatIfEntryStatus_Object=MibTableColumn
natIfEntryStatus=_NatIfEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,7,1,5),_NatIfEntryStatus_Type())
natIfEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natIfEntryStatus.setStatus(_A)
_NatIPSecSessionTable_Object=MibTable
natIPSecSessionTable=_NatIPSecSessionTable_Object((1,3,6,1,4,1,10876,101,1,14,1,8))
if mibBuilder.loadTexts:natIPSecSessionTable.setStatus(_A)
_NatIPSecSessionEntry_Object=MibTableRow
natIPSecSessionEntry=_NatIPSecSessionEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1))
natIPSecSessionEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:natIPSecSessionEntry.setStatus(_A)
class _NatIPSecSessionInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatIPSecSessionInterfaceNum_Type.__name__=_D
_NatIPSecSessionInterfaceNum_Object=MibTableColumn
natIPSecSessionInterfaceNum=_NatIPSecSessionInterfaceNum_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,1),_NatIPSecSessionInterfaceNum_Type())
natIPSecSessionInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecSessionInterfaceNum.setStatus(_A)
_NatIPSecSessionLocalIp_Type=IpAddress
_NatIPSecSessionLocalIp_Object=MibTableColumn
natIPSecSessionLocalIp=_NatIPSecSessionLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,2),_NatIPSecSessionLocalIp_Type())
natIPSecSessionLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecSessionLocalIp.setStatus(_A)
_NatIPSecSessionTranslatedLocalIp_Type=IpAddress
_NatIPSecSessionTranslatedLocalIp_Object=MibTableColumn
natIPSecSessionTranslatedLocalIp=_NatIPSecSessionTranslatedLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,3),_NatIPSecSessionTranslatedLocalIp_Type())
natIPSecSessionTranslatedLocalIp.setMaxAccess(_F)
if mibBuilder.loadTexts:natIPSecSessionTranslatedLocalIp.setStatus(_A)
_NatIPSecSessionOutsideIp_Type=IpAddress
_NatIPSecSessionOutsideIp_Object=MibTableColumn
natIPSecSessionOutsideIp=_NatIPSecSessionOutsideIp_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,4),_NatIPSecSessionOutsideIp_Type())
natIPSecSessionOutsideIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecSessionOutsideIp.setStatus(_A)
class _NatIPSecSessionSPIInside_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NatIPSecSessionSPIInside_Type.__name__=_D
_NatIPSecSessionSPIInside_Object=MibTableColumn
natIPSecSessionSPIInside=_NatIPSecSessionSPIInside_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,5),_NatIPSecSessionSPIInside_Type())
natIPSecSessionSPIInside.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecSessionSPIInside.setStatus(_A)
class _NatIPSecSessionSPIOutside_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NatIPSecSessionSPIOutside_Type.__name__=_D
_NatIPSecSessionSPIOutside_Object=MibTableColumn
natIPSecSessionSPIOutside=_NatIPSecSessionSPIOutside_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,6),_NatIPSecSessionSPIOutside_Type())
natIPSecSessionSPIOutside.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecSessionSPIOutside.setStatus(_A)
_NatIPSecSessionLastUseTime_Type=Integer32
_NatIPSecSessionLastUseTime_Object=MibTableColumn
natIPSecSessionLastUseTime=_NatIPSecSessionLastUseTime_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,7),_NatIPSecSessionLastUseTime_Type())
natIPSecSessionLastUseTime.setMaxAccess(_F)
if mibBuilder.loadTexts:natIPSecSessionLastUseTime.setStatus(_A)
_NatIPSecSessionEntryStatus_Type=RowStatus
_NatIPSecSessionEntryStatus_Object=MibTableColumn
natIPSecSessionEntryStatus=_NatIPSecSessionEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,8,1,8),_NatIPSecSessionEntryStatus_Type())
natIPSecSessionEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natIPSecSessionEntryStatus.setStatus(_A)
_NatIPSecPendingTable_Object=MibTable
natIPSecPendingTable=_NatIPSecPendingTable_Object((1,3,6,1,4,1,10876,101,1,14,1,9))
if mibBuilder.loadTexts:natIPSecPendingTable.setStatus(_A)
_NatIPSecPendingEntry_Object=MibTableRow
natIPSecPendingEntry=_NatIPSecPendingEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1))
natIPSecPendingEntry.setIndexNames((0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m),(0,_B,_n))
if mibBuilder.loadTexts:natIPSecPendingEntry.setStatus(_A)
class _NatIPSecPendingInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatIPSecPendingInterfaceNum_Type.__name__=_D
_NatIPSecPendingInterfaceNum_Object=MibTableColumn
natIPSecPendingInterfaceNum=_NatIPSecPendingInterfaceNum_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,1),_NatIPSecPendingInterfaceNum_Type())
natIPSecPendingInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecPendingInterfaceNum.setStatus(_A)
_NatIPSecPendingLocalIp_Type=IpAddress
_NatIPSecPendingLocalIp_Object=MibTableColumn
natIPSecPendingLocalIp=_NatIPSecPendingLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,2),_NatIPSecPendingLocalIp_Type())
natIPSecPendingLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecPendingLocalIp.setStatus(_A)
_NatIPSecPendingTranslatedLocalIp_Type=IpAddress
_NatIPSecPendingTranslatedLocalIp_Object=MibTableColumn
natIPSecPendingTranslatedLocalIp=_NatIPSecPendingTranslatedLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,3),_NatIPSecPendingTranslatedLocalIp_Type())
natIPSecPendingTranslatedLocalIp.setMaxAccess(_F)
if mibBuilder.loadTexts:natIPSecPendingTranslatedLocalIp.setStatus(_A)
_NatIPSecPendingOutsideIp_Type=IpAddress
_NatIPSecPendingOutsideIp_Object=MibTableColumn
natIPSecPendingOutsideIp=_NatIPSecPendingOutsideIp_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,4),_NatIPSecPendingOutsideIp_Type())
natIPSecPendingOutsideIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecPendingOutsideIp.setStatus(_A)
class _NatIPSecPendingSPIInside_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NatIPSecPendingSPIInside_Type.__name__=_D
_NatIPSecPendingSPIInside_Object=MibTableColumn
natIPSecPendingSPIInside=_NatIPSecPendingSPIInside_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,5),_NatIPSecPendingSPIInside_Type())
natIPSecPendingSPIInside.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecPendingSPIInside.setStatus(_A)
class _NatIPSecPendingSPIOutside_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NatIPSecPendingSPIOutside_Type.__name__=_D
_NatIPSecPendingSPIOutside_Object=MibTableColumn
natIPSecPendingSPIOutside=_NatIPSecPendingSPIOutside_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,6),_NatIPSecPendingSPIOutside_Type())
natIPSecPendingSPIOutside.setMaxAccess(_C)
if mibBuilder.loadTexts:natIPSecPendingSPIOutside.setStatus(_A)
_NatIPSecPendingLastUseTime_Type=Integer32
_NatIPSecPendingLastUseTime_Object=MibTableColumn
natIPSecPendingLastUseTime=_NatIPSecPendingLastUseTime_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,7),_NatIPSecPendingLastUseTime_Type())
natIPSecPendingLastUseTime.setMaxAccess(_F)
if mibBuilder.loadTexts:natIPSecPendingLastUseTime.setStatus(_A)
_NatIPSecPendingNoOfRetry_Type=Integer32
_NatIPSecPendingNoOfRetry_Object=MibTableColumn
natIPSecPendingNoOfRetry=_NatIPSecPendingNoOfRetry_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,8),_NatIPSecPendingNoOfRetry_Type())
natIPSecPendingNoOfRetry.setMaxAccess(_F)
if mibBuilder.loadTexts:natIPSecPendingNoOfRetry.setStatus(_A)
_NatIPSecPendingEntryStatus_Type=RowStatus
_NatIPSecPendingEntryStatus_Object=MibTableColumn
natIPSecPendingEntryStatus=_NatIPSecPendingEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,9,1,9),_NatIPSecPendingEntryStatus_Type())
natIPSecPendingEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natIPSecPendingEntryStatus.setStatus(_A)
_NatIKESessionTable_Object=MibTable
natIKESessionTable=_NatIKESessionTable_Object((1,3,6,1,4,1,10876,101,1,14,1,10))
if mibBuilder.loadTexts:natIKESessionTable.setStatus(_A)
_NatIKESessionEntry_Object=MibTableRow
natIKESessionEntry=_NatIKESessionEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1))
natIKESessionEntry.setIndexNames((0,_B,_o),(0,_B,_p),(0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:natIKESessionEntry.setStatus(_A)
class _NatIKESessionInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NatIKESessionInterfaceNum_Type.__name__=_D
_NatIKESessionInterfaceNum_Object=MibTableColumn
natIKESessionInterfaceNum=_NatIKESessionInterfaceNum_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1,1),_NatIKESessionInterfaceNum_Type())
natIKESessionInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:natIKESessionInterfaceNum.setStatus(_A)
_NatIKESessionLocalIp_Type=IpAddress
_NatIKESessionLocalIp_Object=MibTableColumn
natIKESessionLocalIp=_NatIKESessionLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1,2),_NatIKESessionLocalIp_Type())
natIKESessionLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natIKESessionLocalIp.setStatus(_A)
_NatIKESessionTranslatedLocalIp_Type=IpAddress
_NatIKESessionTranslatedLocalIp_Object=MibTableColumn
natIKESessionTranslatedLocalIp=_NatIKESessionTranslatedLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1,3),_NatIKESessionTranslatedLocalIp_Type())
natIKESessionTranslatedLocalIp.setMaxAccess(_F)
if mibBuilder.loadTexts:natIKESessionTranslatedLocalIp.setStatus(_A)
_NatIKESessionOutsideIp_Type=IpAddress
_NatIKESessionOutsideIp_Object=MibTableColumn
natIKESessionOutsideIp=_NatIKESessionOutsideIp_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1,4),_NatIKESessionOutsideIp_Type())
natIKESessionOutsideIp.setMaxAccess(_C)
if mibBuilder.loadTexts:natIKESessionOutsideIp.setStatus(_A)
class _NatIKESessionInitCookie_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NatIKESessionInitCookie_Type.__name__=_I
_NatIKESessionInitCookie_Object=MibTableColumn
natIKESessionInitCookie=_NatIKESessionInitCookie_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1,5),_NatIKESessionInitCookie_Type())
natIKESessionInitCookie.setMaxAccess(_C)
if mibBuilder.loadTexts:natIKESessionInitCookie.setStatus(_A)
_NatIKESessionLastUseTime_Type=Integer32
_NatIKESessionLastUseTime_Object=MibTableColumn
natIKESessionLastUseTime=_NatIKESessionLastUseTime_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1,6),_NatIKESessionLastUseTime_Type())
natIKESessionLastUseTime.setMaxAccess(_F)
if mibBuilder.loadTexts:natIKESessionLastUseTime.setStatus(_A)
_NatIKESessionEntryStatus_Type=RowStatus
_NatIKESessionEntryStatus_Object=MibTableColumn
natIKESessionEntryStatus=_NatIKESessionEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,10,1,7),_NatIKESessionEntryStatus_Type())
natIKESessionEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natIKESessionEntryStatus.setStatus(_A)
_NatPortTrigInfoTable_Object=MibTable
natPortTrigInfoTable=_NatPortTrigInfoTable_Object((1,3,6,1,4,1,10876,101,1,14,1,11))
if mibBuilder.loadTexts:natPortTrigInfoTable.setStatus(_A)
_NatPortTrigInfoEntry_Object=MibTableRow
natPortTrigInfoEntry=_NatPortTrigInfoEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,11,1))
natPortTrigInfoEntry.setIndexNames((0,_B,_s),(0,_B,_t),(0,_B,_u))
if mibBuilder.loadTexts:natPortTrigInfoEntry.setStatus(_A)
class _NatPortTrigInfoAppName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NatPortTrigInfoAppName_Type.__name__=_G
_NatPortTrigInfoAppName_Object=MibTableColumn
natPortTrigInfoAppName=_NatPortTrigInfoAppName_Object((1,3,6,1,4,1,10876,101,1,14,1,11,1,1),_NatPortTrigInfoAppName_Type())
natPortTrigInfoAppName.setMaxAccess(_E)
if mibBuilder.loadTexts:natPortTrigInfoAppName.setStatus(_A)
class _NatPortTrigInfoInBoundPortRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,11))
_NatPortTrigInfoInBoundPortRange_Type.__name__=_G
_NatPortTrigInfoInBoundPortRange_Object=MibTableColumn
natPortTrigInfoInBoundPortRange=_NatPortTrigInfoInBoundPortRange_Object((1,3,6,1,4,1,10876,101,1,14,1,11,1,2),_NatPortTrigInfoInBoundPortRange_Type())
natPortTrigInfoInBoundPortRange.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortTrigInfoInBoundPortRange.setStatus(_A)
class _NatPortTrigInfoOutBoundPortRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,11))
_NatPortTrigInfoOutBoundPortRange_Type.__name__=_G
_NatPortTrigInfoOutBoundPortRange_Object=MibTableColumn
natPortTrigInfoOutBoundPortRange=_NatPortTrigInfoOutBoundPortRange_Object((1,3,6,1,4,1,10876,101,1,14,1,11,1,3),_NatPortTrigInfoOutBoundPortRange_Type())
natPortTrigInfoOutBoundPortRange.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortTrigInfoOutBoundPortRange.setStatus(_A)
class _NatPortTrigInfoProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17,255)));namedValues=NamedValues(*((_J,6),(_K,17),(_L,255)))
_NatPortTrigInfoProtocol_Type.__name__=_D
_NatPortTrigInfoProtocol_Object=MibTableColumn
natPortTrigInfoProtocol=_NatPortTrigInfoProtocol_Object((1,3,6,1,4,1,10876,101,1,14,1,11,1,4),_NatPortTrigInfoProtocol_Type())
natPortTrigInfoProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortTrigInfoProtocol.setStatus(_A)
_NatPortTrigInfoEntryStatus_Type=RowStatus
_NatPortTrigInfoEntryStatus_Object=MibTableColumn
natPortTrigInfoEntryStatus=_NatPortTrigInfoEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,11,1,5),_NatPortTrigInfoEntryStatus_Type())
natPortTrigInfoEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natPortTrigInfoEntryStatus.setStatus(_A)
_NatPolicyTable_Object=MibTable
natPolicyTable=_NatPolicyTable_Object((1,3,6,1,4,1,10876,101,1,14,1,12))
if mibBuilder.loadTexts:natPolicyTable.setStatus(_A)
_NatPolicyEntry_Object=MibTableRow
natPolicyEntry=_NatPolicyEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,12,1))
natPolicyEntry.setIndexNames((0,_B,_v),(0,_B,_w),(0,_B,_x))
if mibBuilder.loadTexts:natPolicyEntry.setStatus(_A)
class _NatPolicyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_NatPolicyType_Type.__name__=_D
_NatPolicyType_Object=MibTableColumn
natPolicyType=_NatPolicyType_Object((1,3,6,1,4,1,10876,101,1,14,1,12,1,1),_NatPolicyType_Type())
natPolicyType.setMaxAccess(_C)
if mibBuilder.loadTexts:natPolicyType.setStatus(_A)
class _NatPolicyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NatPolicyId_Type.__name__=_D
_NatPolicyId_Object=MibTableColumn
natPolicyId=_NatPolicyId_Object((1,3,6,1,4,1,10876,101,1,14,1,12,1,2),_NatPolicyId_Type())
natPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:natPolicyId.setStatus(_A)
class _NatPolicyAclName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_NatPolicyAclName_Type.__name__=_I
_NatPolicyAclName_Object=MibTableColumn
natPolicyAclName=_NatPolicyAclName_Object((1,3,6,1,4,1,10876,101,1,14,1,12,1,3),_NatPolicyAclName_Type())
natPolicyAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:natPolicyAclName.setStatus(_A)
_NatPolicyTranslatedIp_Type=IpAddress
_NatPolicyTranslatedIp_Object=MibTableColumn
natPolicyTranslatedIp=_NatPolicyTranslatedIp_Object((1,3,6,1,4,1,10876,101,1,14,1,12,1,4),_NatPolicyTranslatedIp_Type())
natPolicyTranslatedIp.setMaxAccess(_E)
if mibBuilder.loadTexts:natPolicyTranslatedIp.setStatus(_A)
_NatPolicyEntryStatus_Type=RowStatus
_NatPolicyEntryStatus_Object=MibTableColumn
natPolicyEntryStatus=_NatPolicyEntryStatus_Object((1,3,6,1,4,1,10876,101,1,14,1,12,1,5),_NatPolicyEntryStatus_Type())
natPolicyEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:natPolicyEntryStatus.setStatus(_A)
_NatRsvdPortTrigInfoTable_Object=MibTable
natRsvdPortTrigInfoTable=_NatRsvdPortTrigInfoTable_Object((1,3,6,1,4,1,10876,101,1,14,1,13))
if mibBuilder.loadTexts:natRsvdPortTrigInfoTable.setStatus(_A)
_NatRsvdPortTrigInfoEntry_Object=MibTableRow
natRsvdPortTrigInfoEntry=_NatRsvdPortTrigInfoEntry_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1))
natRsvdPortTrigInfoEntry.setIndexNames((0,_B,_y))
if mibBuilder.loadTexts:natRsvdPortTrigInfoEntry.setStatus(_A)
class _NatRsvdPortTrigInfoAppIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_NatRsvdPortTrigInfoAppIndex_Type.__name__=_D
_NatRsvdPortTrigInfoAppIndex_Object=MibTableColumn
natRsvdPortTrigInfoAppIndex=_NatRsvdPortTrigInfoAppIndex_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,1),_NatRsvdPortTrigInfoAppIndex_Type())
natRsvdPortTrigInfoAppIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natRsvdPortTrigInfoAppIndex.setStatus(_A)
_NatRsvdPortTrigInfoLocalIp_Type=IpAddress
_NatRsvdPortTrigInfoLocalIp_Object=MibTableColumn
natRsvdPortTrigInfoLocalIp=_NatRsvdPortTrigInfoLocalIp_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,2),_NatRsvdPortTrigInfoLocalIp_Type())
natRsvdPortTrigInfoLocalIp.setMaxAccess(_F)
if mibBuilder.loadTexts:natRsvdPortTrigInfoLocalIp.setStatus(_A)
_NatRsvdPortTrigInfoRemoteIp_Type=IpAddress
_NatRsvdPortTrigInfoRemoteIp_Object=MibTableColumn
natRsvdPortTrigInfoRemoteIp=_NatRsvdPortTrigInfoRemoteIp_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,3),_NatRsvdPortTrigInfoRemoteIp_Type())
natRsvdPortTrigInfoRemoteIp.setMaxAccess(_F)
if mibBuilder.loadTexts:natRsvdPortTrigInfoRemoteIp.setStatus(_A)
class _NatRsvdPortTrigInfoStartTime_Type(TimeStamp):defaultValue=0
_NatRsvdPortTrigInfoStartTime_Type.__name__=_M
_NatRsvdPortTrigInfoStartTime_Object=MibTableColumn
natRsvdPortTrigInfoStartTime=_NatRsvdPortTrigInfoStartTime_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,4),_NatRsvdPortTrigInfoStartTime_Type())
natRsvdPortTrigInfoStartTime.setMaxAccess(_F)
if mibBuilder.loadTexts:natRsvdPortTrigInfoStartTime.setStatus(_A)
class _NatRsvdPortTrigInfoAppName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NatRsvdPortTrigInfoAppName_Type.__name__=_G
_NatRsvdPortTrigInfoAppName_Object=MibTableColumn
natRsvdPortTrigInfoAppName=_NatRsvdPortTrigInfoAppName_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,5),_NatRsvdPortTrigInfoAppName_Type())
natRsvdPortTrigInfoAppName.setMaxAccess(_F)
if mibBuilder.loadTexts:natRsvdPortTrigInfoAppName.setStatus(_A)
class _NatRsvdPortTrigInfoInBoundPortRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,11))
_NatRsvdPortTrigInfoInBoundPortRange_Type.__name__=_G
_NatRsvdPortTrigInfoInBoundPortRange_Object=MibTableColumn
natRsvdPortTrigInfoInBoundPortRange=_NatRsvdPortTrigInfoInBoundPortRange_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,6),_NatRsvdPortTrigInfoInBoundPortRange_Type())
natRsvdPortTrigInfoInBoundPortRange.setMaxAccess(_F)
if mibBuilder.loadTexts:natRsvdPortTrigInfoInBoundPortRange.setStatus(_A)
class _NatRsvdPortTrigInfoOutBoundPortRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,11))
_NatRsvdPortTrigInfoOutBoundPortRange_Type.__name__=_G
_NatRsvdPortTrigInfoOutBoundPortRange_Object=MibTableColumn
natRsvdPortTrigInfoOutBoundPortRange=_NatRsvdPortTrigInfoOutBoundPortRange_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,7),_NatRsvdPortTrigInfoOutBoundPortRange_Type())
natRsvdPortTrigInfoOutBoundPortRange.setMaxAccess(_F)
if mibBuilder.loadTexts:natRsvdPortTrigInfoOutBoundPortRange.setStatus(_A)
class _NatRsvdPortTrigInfoProtocol_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17,255)));namedValues=NamedValues(*((_J,6),(_K,17),(_L,255)))
_NatRsvdPortTrigInfoProtocol_Type.__name__=_D
_NatRsvdPortTrigInfoProtocol_Object=MibTableColumn
natRsvdPortTrigInfoProtocol=_NatRsvdPortTrigInfoProtocol_Object((1,3,6,1,4,1,10876,101,1,14,1,13,1,8),_NatRsvdPortTrigInfoProtocol_Type())
natRsvdPortTrigInfoProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:natRsvdPortTrigInfoProtocol.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:Status,'futureNatMIB':futureNatMIB,'nat':nat,'natStatInfo':natStatInfo,'natEnable':natEnable,'natTypicalNumberOfEntries':natTypicalNumberOfEntries,'natTranslatedLocalPortStart':natTranslatedLocalPortStart,'natIdleTimeOut':natIdleTimeOut,'natTcpTimeOut':natTcpTimeOut,'natUdpTimeOut':natUdpTimeOut,'natTrcFlag':natTrcFlag,'natStatDynamicAllocFailureCount':natStatDynamicAllocFailureCount,'natStatTotalNumberOfTranslations':natStatTotalNumberOfTranslations,'natStatTotalNumberOfActiveSessions':natStatTotalNumberOfActiveSessions,'natStatTotalNumberOfPktsDropped':natStatTotalNumberOfPktsDropped,'natStatTotalNumberOfSessionsClosed':natStatTotalNumberOfSessionsClosed,'natIKEPortTranslation':natIKEPortTranslation,'natIKETimeout':natIKETimeout,'natIPSecTimeout':natIPSecTimeout,'natIPSecPendingTimeout':natIPSecPendingTimeout,'natIPSecMaxRetry':natIPSecMaxRetry,'sipAlgPort':sipAlgPort,'natSipAlgPartialEntryTimeOut':natSipAlgPartialEntryTimeOut,'natDynamicTransTable':natDynamicTransTable,'natDynamicTransEntry':natDynamicTransEntry,_N:natDynamicTransInterfaceNum,_O:natDynamicTransLocalIp,'natDynamicTransTranslatedLocalIp':natDynamicTransTranslatedLocalIp,_P:natDynamicTransLocalPort,'natDynamicTransTranslatedLocalPort':natDynamicTransTranslatedLocalPort,_Q:natDynamicTransOutsideIp,_R:natDynamicTransOutsidePort,'natDynamicTransLastUseTime':natDynamicTransLastUseTime,'natGlobalAddressTable':natGlobalAddressTable,'natGlobalAddressEntry':natGlobalAddressEntry,_S:natGlobalAddressInterfaceNum,_T:natGlobalAddressTranslatedLocalIp,'natGlobalAddressMask':natGlobalAddressMask,'natGlobalAddressEntryStatus':natGlobalAddressEntryStatus,'natLocalAddressTable':natLocalAddressTable,'natLocalAddressEntry':natLocalAddressEntry,_U:natLocalAddressInterfaceNumber,_V:natLocalAddressLocalIp,'natLocalAddressMask':natLocalAddressMask,'natLocalAddressEntryStatus':natLocalAddressEntryStatus,'natStaticTable':natStaticTable,'natStaticEntry':natStaticEntry,_W:natStaticInterfaceNum,_X:natStaticLocalIp,'natStaticTranslatedLocalIp':natStaticTranslatedLocalIp,'natStaticEntryStatus':natStaticEntryStatus,'natStaticNaptTable':natStaticNaptTable,'natStaticNaptEntry':natStaticNaptEntry,_Y:natStaticNaptInterfaceNum,_Z:natStaticNaptLocalIp,_a:natStaticNaptStartLocalPort,_b:natStaticNaptEndLocalPort,_c:natStaticNaptProtocolNumber,'natStaticNaptTranslatedLocalIp':natStaticNaptTranslatedLocalIp,'natStaticNaptTranslatedLocalPort':natStaticNaptTranslatedLocalPort,'natStaticNaptDescription':natStaticNaptDescription,'natStaticNaptEntryStatus':natStaticNaptEntryStatus,'natIfTable':natIfTable,'natIfEntry':natIfEntry,_d:natIfInterfaceNumber,'natIfNat':natIfNat,'natIfNapt':natIfNapt,'natIfTwoWayNat':natIfTwoWayNat,'natIfEntryStatus':natIfEntryStatus,'natIPSecSessionTable':natIPSecSessionTable,'natIPSecSessionEntry':natIPSecSessionEntry,_e:natIPSecSessionInterfaceNum,_f:natIPSecSessionLocalIp,'natIPSecSessionTranslatedLocalIp':natIPSecSessionTranslatedLocalIp,_g:natIPSecSessionOutsideIp,_h:natIPSecSessionSPIInside,_i:natIPSecSessionSPIOutside,'natIPSecSessionLastUseTime':natIPSecSessionLastUseTime,'natIPSecSessionEntryStatus':natIPSecSessionEntryStatus,'natIPSecPendingTable':natIPSecPendingTable,'natIPSecPendingEntry':natIPSecPendingEntry,_j:natIPSecPendingInterfaceNum,_k:natIPSecPendingLocalIp,'natIPSecPendingTranslatedLocalIp':natIPSecPendingTranslatedLocalIp,_l:natIPSecPendingOutsideIp,_m:natIPSecPendingSPIInside,_n:natIPSecPendingSPIOutside,'natIPSecPendingLastUseTime':natIPSecPendingLastUseTime,'natIPSecPendingNoOfRetry':natIPSecPendingNoOfRetry,'natIPSecPendingEntryStatus':natIPSecPendingEntryStatus,'natIKESessionTable':natIKESessionTable,'natIKESessionEntry':natIKESessionEntry,_o:natIKESessionInterfaceNum,_p:natIKESessionLocalIp,'natIKESessionTranslatedLocalIp':natIKESessionTranslatedLocalIp,_q:natIKESessionOutsideIp,_r:natIKESessionInitCookie,'natIKESessionLastUseTime':natIKESessionLastUseTime,'natIKESessionEntryStatus':natIKESessionEntryStatus,'natPortTrigInfoTable':natPortTrigInfoTable,'natPortTrigInfoEntry':natPortTrigInfoEntry,'natPortTrigInfoAppName':natPortTrigInfoAppName,_s:natPortTrigInfoInBoundPortRange,_t:natPortTrigInfoOutBoundPortRange,_u:natPortTrigInfoProtocol,'natPortTrigInfoEntryStatus':natPortTrigInfoEntryStatus,'natPolicyTable':natPolicyTable,'natPolicyEntry':natPolicyEntry,_v:natPolicyType,_w:natPolicyId,_x:natPolicyAclName,'natPolicyTranslatedIp':natPolicyTranslatedIp,'natPolicyEntryStatus':natPolicyEntryStatus,'natRsvdPortTrigInfoTable':natRsvdPortTrigInfoTable,'natRsvdPortTrigInfoEntry':natRsvdPortTrigInfoEntry,_y:natRsvdPortTrigInfoAppIndex,'natRsvdPortTrigInfoLocalIp':natRsvdPortTrigInfoLocalIp,'natRsvdPortTrigInfoRemoteIp':natRsvdPortTrigInfoRemoteIp,'natRsvdPortTrigInfoStartTime':natRsvdPortTrigInfoStartTime,'natRsvdPortTrigInfoAppName':natRsvdPortTrigInfoAppName,'natRsvdPortTrigInfoInBoundPortRange':natRsvdPortTrigInfoInBoundPortRange,'natRsvdPortTrigInfoOutBoundPortRange':natRsvdPortTrigInfoOutBoundPortRange,'natRsvdPortTrigInfoProtocol':natRsvdPortTrigInfoProtocol})