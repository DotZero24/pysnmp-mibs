_AN='cl2natInstanceTranslationStatisticsGroup'
_AM='cl2natInstanceStatisticsGroup'
_AL='cl2natInstanceConfigGroup'
_AK='cl2natGlobalStatisticsGroup'
_AJ='cl2natTranslatesOut'
_AI='cl2natTranslatesIn'
_AH='cl2natPassThruIgmpOut'
_AG='cl2natPassThruIgmpIn'
_AF='cl2natDroppedIgmpOut'
_AE='cl2natDroppedIgmpIn'
_AD='cl2natPassThruMulticastOut'
_AC='cl2natPassThruMulticastIn'
_AB='cl2natDroppedMulticastOut'
_AA='cl2natDroppedMulticastIn'
_A9='cl2natPassThruUnicastOut'
_A8='cl2natPassThruUnicastIn'
_A7='cl2natFixupSccpOut'
_A6='cl2natFixupSipOut'
_A5='cl2natFixupSnmpOut'
_A4='cl2natFixupFtpOut'
_A3='cl2natFixupProfinetOut'
_A2='cl2natFixupCipOut'
_A1='cl2natFixupIcmpOut'
_A0='cl2natFixupArpOut'
_z='cl2natTranslatedUnicastOut'
_y='cl2natDroppedUnicastOut'
_x='cl2natUnmatchedOut'
_w='cl2natFixupSccpIn'
_v='cl2natFixupSipIn'
_u='cl2natFixupSnmpIn'
_t='cl2natFixupFtpIn'
_s='cl2natFixupProfinetIn'
_r='cl2natFixupCipIn'
_q='cl2natFixupIcmpIn'
_p='cl2natFixupArpIn'
_o='cl2natTranslatedUnicastIn'
_n='cl2natDroppedUnicastIn'
_m='cl2natUnmatchedIn'
_l='cl2natInterfaceConfigStorageType'
_k='cl2natInstStorageIpStorageType'
_j='cl2natInstConfigStorageType'
_i='cl2natInstIpRowStatus'
_h='cl2natInterfaceConfigInstanceName'
_g='cl2natInstIpAddressMask'
_f='cl2natInterfaceConfigRowStatus'
_e='cl2natInstConfigInstanceRowStatus'
_d='cl2natInstIpToIpAddressType'
_c='cl2natInstIpToIpAddress'
_b='cl2natInstIpRange'
_a='cl2natInstConfigFixup'
_Z='cl2natInstConfigPermitOut'
_Y='cl2natInstConfigPermitIn'
_X='cl2natTotalPacketTranslated'
_W='cl2natTotalTranslationEntryConfigured'
_V='cl2natTotalFixups'
_U='cl2natTotalUnmatched'
_T='cl2natTotalMatched'
_S='cl2natTotalInstances'
_R='cl2natInstIpAddressType'
_Q='multicast'
_P='unmatched'
_O='cl2natInstIpFromIpAddress'
_N='cl2natInstIpFromIpAddressType'
_M='cl2natInstIpDirection'
_L='cl2natInstConfigInstanceName'
_K='SnmpAdminString'
_J='InetAddress'
_I='cl2natInterfaceConfigVlanIndex'
_H='cl2natInterfaceConfigIfIndex'
_G='Integer32'
_F='Bits'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='CISCO-L2NAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoInetAddressMask,=mibBuilder.importSymbols('CISCO-TC','CiscoInetAddressMask')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
ciscoL2natMIB=ModuleIdentity((1,3,6,1,4,1,9,9,806))
if mibBuilder.loadTexts:ciscoL2natMIB.setRevisions(('2013-04-16 00:00',))
_CiscoL2natMIBObjects_ObjectIdentity=ObjectIdentity
ciscoL2natMIBObjects=_CiscoL2natMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,806,1))
_Cl2natTotalInstances_Type=Counter32
_Cl2natTotalInstances_Object=MibScalar
cl2natTotalInstances=_Cl2natTotalInstances_Object((1,3,6,1,4,1,9,9,806,1,1),_Cl2natTotalInstances_Type())
cl2natTotalInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTotalInstances.setStatus(_A)
_Cl2natTotalMatched_Type=Counter64
_Cl2natTotalMatched_Object=MibScalar
cl2natTotalMatched=_Cl2natTotalMatched_Object((1,3,6,1,4,1,9,9,806,1,2),_Cl2natTotalMatched_Type())
cl2natTotalMatched.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTotalMatched.setStatus(_A)
_Cl2natTotalUnmatched_Type=Counter64
_Cl2natTotalUnmatched_Object=MibScalar
cl2natTotalUnmatched=_Cl2natTotalUnmatched_Object((1,3,6,1,4,1,9,9,806,1,3),_Cl2natTotalUnmatched_Type())
cl2natTotalUnmatched.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTotalUnmatched.setStatus(_A)
_Cl2natTotalFixups_Type=Counter64
_Cl2natTotalFixups_Object=MibScalar
cl2natTotalFixups=_Cl2natTotalFixups_Object((1,3,6,1,4,1,9,9,806,1,4),_Cl2natTotalFixups_Type())
cl2natTotalFixups.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTotalFixups.setStatus(_A)
_Cl2natTotalTranslationEntryConfigured_Type=Unsigned32
_Cl2natTotalTranslationEntryConfigured_Object=MibScalar
cl2natTotalTranslationEntryConfigured=_Cl2natTotalTranslationEntryConfigured_Object((1,3,6,1,4,1,9,9,806,1,5),_Cl2natTotalTranslationEntryConfigured_Type())
cl2natTotalTranslationEntryConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTotalTranslationEntryConfigured.setStatus(_A)
_Cl2natTotalPacketTranslated_Type=Counter64
_Cl2natTotalPacketTranslated_Object=MibScalar
cl2natTotalPacketTranslated=_Cl2natTotalPacketTranslated_Object((1,3,6,1,4,1,9,9,806,1,6),_Cl2natTotalPacketTranslated_Type())
cl2natTotalPacketTranslated.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTotalPacketTranslated.setStatus(_A)
_Cl2natInstConfigInstanceTable_Object=MibTable
cl2natInstConfigInstanceTable=_Cl2natInstConfigInstanceTable_Object((1,3,6,1,4,1,9,9,806,1,7))
if mibBuilder.loadTexts:cl2natInstConfigInstanceTable.setStatus(_A)
_Cl2natInstConfigInstanceEntry_Object=MibTableRow
cl2natInstConfigInstanceEntry=_Cl2natInstConfigInstanceEntry_Object((1,3,6,1,4,1,9,9,806,1,7,1))
cl2natInstConfigInstanceEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cl2natInstConfigInstanceEntry.setStatus(_A)
class _Cl2natInstConfigInstanceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Cl2natInstConfigInstanceName_Type.__name__=_K
_Cl2natInstConfigInstanceName_Object=MibTableColumn
cl2natInstConfigInstanceName=_Cl2natInstConfigInstanceName_Object((1,3,6,1,4,1,9,9,806,1,7,1,1),_Cl2natInstConfigInstanceName_Type())
cl2natInstConfigInstanceName.setMaxAccess(_E)
if mibBuilder.loadTexts:cl2natInstConfigInstanceName.setStatus(_A)
class _Cl2natInstConfigPermitIn_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_P,0),('igmp',1),(_Q,2)))
_Cl2natInstConfigPermitIn_Type.__name__=_F
_Cl2natInstConfigPermitIn_Object=MibTableColumn
cl2natInstConfigPermitIn=_Cl2natInstConfigPermitIn_Object((1,3,6,1,4,1,9,9,806,1,7,1,2),_Cl2natInstConfigPermitIn_Type())
cl2natInstConfigPermitIn.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstConfigPermitIn.setStatus(_A)
class _Cl2natInstConfigPermitOut_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_P,0),('igmp',1),(_Q,2)))
_Cl2natInstConfigPermitOut_Type.__name__=_F
_Cl2natInstConfigPermitOut_Object=MibTableColumn
cl2natInstConfigPermitOut=_Cl2natInstConfigPermitOut_Object((1,3,6,1,4,1,9,9,806,1,7,1,3),_Cl2natInstConfigPermitOut_Type())
cl2natInstConfigPermitOut.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstConfigPermitOut.setStatus(_A)
class _Cl2natInstConfigFixup_Type(Bits):defaultBinValue='1111';namedValues=NamedValues(*(('arp',0),('icmp',1),('profinet',2),('cip',3),('snmp',4)))
_Cl2natInstConfigFixup_Type.__name__=_F
_Cl2natInstConfigFixup_Object=MibTableColumn
cl2natInstConfigFixup=_Cl2natInstConfigFixup_Object((1,3,6,1,4,1,9,9,806,1,7,1,4),_Cl2natInstConfigFixup_Type())
cl2natInstConfigFixup.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstConfigFixup.setStatus(_A)
_Cl2natInstConfigStorageType_Type=StorageType
_Cl2natInstConfigStorageType_Object=MibTableColumn
cl2natInstConfigStorageType=_Cl2natInstConfigStorageType_Object((1,3,6,1,4,1,9,9,806,1,7,1,5),_Cl2natInstConfigStorageType_Type())
cl2natInstConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natInstConfigStorageType.setStatus(_A)
_Cl2natInstConfigInstanceRowStatus_Type=RowStatus
_Cl2natInstConfigInstanceRowStatus_Object=MibTableColumn
cl2natInstConfigInstanceRowStatus=_Cl2natInstConfigInstanceRowStatus_Object((1,3,6,1,4,1,9,9,806,1,7,1,6),_Cl2natInstConfigInstanceRowStatus_Type())
cl2natInstConfigInstanceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstConfigInstanceRowStatus.setStatus(_A)
_Cl2natInstIpInstanceIpTable_Object=MibTable
cl2natInstIpInstanceIpTable=_Cl2natInstIpInstanceIpTable_Object((1,3,6,1,4,1,9,9,806,1,8))
if mibBuilder.loadTexts:cl2natInstIpInstanceIpTable.setStatus(_A)
_Cl2natInstIpInstanceIpEntry_Object=MibTableRow
cl2natInstIpInstanceIpEntry=_Cl2natInstIpInstanceIpEntry_Object((1,3,6,1,4,1,9,9,806,1,8,1))
cl2natInstIpInstanceIpEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R))
if mibBuilder.loadTexts:cl2natInstIpInstanceIpEntry.setStatus(_A)
class _Cl2natInstIpDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inside',1),('outside',2)))
_Cl2natInstIpDirection_Type.__name__=_G
_Cl2natInstIpDirection_Object=MibTableColumn
cl2natInstIpDirection=_Cl2natInstIpDirection_Object((1,3,6,1,4,1,9,9,806,1,8,1,1),_Cl2natInstIpDirection_Type())
cl2natInstIpDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:cl2natInstIpDirection.setStatus(_A)
class _Cl2natInstIpAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('host',1),('range',2),('network',3)))
_Cl2natInstIpAddressType_Type.__name__=_G
_Cl2natInstIpAddressType_Object=MibTableColumn
cl2natInstIpAddressType=_Cl2natInstIpAddressType_Object((1,3,6,1,4,1,9,9,806,1,8,1,2),_Cl2natInstIpAddressType_Type())
cl2natInstIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:cl2natInstIpAddressType.setStatus(_A)
_Cl2natInstIpFromIpAddressType_Type=InetAddressType
_Cl2natInstIpFromIpAddressType_Object=MibTableColumn
cl2natInstIpFromIpAddressType=_Cl2natInstIpFromIpAddressType_Object((1,3,6,1,4,1,9,9,806,1,8,1,3),_Cl2natInstIpFromIpAddressType_Type())
cl2natInstIpFromIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:cl2natInstIpFromIpAddressType.setStatus(_A)
class _Cl2natInstIpFromIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_Cl2natInstIpFromIpAddress_Type.__name__=_J
_Cl2natInstIpFromIpAddress_Object=MibTableColumn
cl2natInstIpFromIpAddress=_Cl2natInstIpFromIpAddress_Object((1,3,6,1,4,1,9,9,806,1,8,1,4),_Cl2natInstIpFromIpAddress_Type())
cl2natInstIpFromIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cl2natInstIpFromIpAddress.setStatus(_A)
_Cl2natInstIpToIpAddressType_Type=InetAddressType
_Cl2natInstIpToIpAddressType_Object=MibTableColumn
cl2natInstIpToIpAddressType=_Cl2natInstIpToIpAddressType_Object((1,3,6,1,4,1,9,9,806,1,8,1,5),_Cl2natInstIpToIpAddressType_Type())
cl2natInstIpToIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstIpToIpAddressType.setStatus(_A)
class _Cl2natInstIpToIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_Cl2natInstIpToIpAddress_Type.__name__=_J
_Cl2natInstIpToIpAddress_Object=MibTableColumn
cl2natInstIpToIpAddress=_Cl2natInstIpToIpAddress_Object((1,3,6,1,4,1,9,9,806,1,8,1,6),_Cl2natInstIpToIpAddress_Type())
cl2natInstIpToIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstIpToIpAddress.setStatus(_A)
_Cl2natInstIpAddressMask_Type=CiscoInetAddressMask
_Cl2natInstIpAddressMask_Object=MibTableColumn
cl2natInstIpAddressMask=_Cl2natInstIpAddressMask_Object((1,3,6,1,4,1,9,9,806,1,8,1,7),_Cl2natInstIpAddressMask_Type())
cl2natInstIpAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstIpAddressMask.setStatus(_A)
class _Cl2natInstIpRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Cl2natInstIpRange_Type.__name__=_G
_Cl2natInstIpRange_Object=MibTableColumn
cl2natInstIpRange=_Cl2natInstIpRange_Object((1,3,6,1,4,1,9,9,806,1,8,1,8),_Cl2natInstIpRange_Type())
cl2natInstIpRange.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstIpRange.setStatus(_A)
_Cl2natInstStorageIpStorageType_Type=StorageType
_Cl2natInstStorageIpStorageType_Object=MibTableColumn
cl2natInstStorageIpStorageType=_Cl2natInstStorageIpStorageType_Object((1,3,6,1,4,1,9,9,806,1,8,1,9),_Cl2natInstStorageIpStorageType_Type())
cl2natInstStorageIpStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natInstStorageIpStorageType.setStatus(_A)
_Cl2natInstIpRowStatus_Type=RowStatus
_Cl2natInstIpRowStatus_Object=MibTableColumn
cl2natInstIpRowStatus=_Cl2natInstIpRowStatus_Object((1,3,6,1,4,1,9,9,806,1,8,1,10),_Cl2natInstIpRowStatus_Type())
cl2natInstIpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInstIpRowStatus.setStatus(_A)
_Cl2natInterfaceConfigTable_Object=MibTable
cl2natInterfaceConfigTable=_Cl2natInterfaceConfigTable_Object((1,3,6,1,4,1,9,9,806,1,9))
if mibBuilder.loadTexts:cl2natInterfaceConfigTable.setStatus(_A)
_Cl2natInterfaceConfigEntry_Object=MibTableRow
cl2natInterfaceConfigEntry=_Cl2natInterfaceConfigEntry_Object((1,3,6,1,4,1,9,9,806,1,9,1))
cl2natInterfaceConfigEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cl2natInterfaceConfigEntry.setStatus(_A)
_Cl2natInterfaceConfigIfIndex_Type=Unsigned32
_Cl2natInterfaceConfigIfIndex_Object=MibTableColumn
cl2natInterfaceConfigIfIndex=_Cl2natInterfaceConfigIfIndex_Object((1,3,6,1,4,1,9,9,806,1,9,1,1),_Cl2natInterfaceConfigIfIndex_Type())
cl2natInterfaceConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cl2natInterfaceConfigIfIndex.setStatus(_A)
_Cl2natInterfaceConfigVlanIndex_Type=Unsigned32
_Cl2natInterfaceConfigVlanIndex_Object=MibTableColumn
cl2natInterfaceConfigVlanIndex=_Cl2natInterfaceConfigVlanIndex_Object((1,3,6,1,4,1,9,9,806,1,9,1,2),_Cl2natInterfaceConfigVlanIndex_Type())
cl2natInterfaceConfigVlanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cl2natInterfaceConfigVlanIndex.setStatus(_A)
class _Cl2natInterfaceConfigInstanceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Cl2natInterfaceConfigInstanceName_Type.__name__=_K
_Cl2natInterfaceConfigInstanceName_Object=MibTableColumn
cl2natInterfaceConfigInstanceName=_Cl2natInterfaceConfigInstanceName_Object((1,3,6,1,4,1,9,9,806,1,9,1,3),_Cl2natInterfaceConfigInstanceName_Type())
cl2natInterfaceConfigInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natInterfaceConfigInstanceName.setStatus(_A)
_Cl2natInterfaceConfigStorageType_Type=StorageType
_Cl2natInterfaceConfigStorageType_Object=MibTableColumn
cl2natInterfaceConfigStorageType=_Cl2natInterfaceConfigStorageType_Object((1,3,6,1,4,1,9,9,806,1,9,1,4),_Cl2natInterfaceConfigStorageType_Type())
cl2natInterfaceConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natInterfaceConfigStorageType.setStatus(_A)
_Cl2natInterfaceConfigRowStatus_Type=RowStatus
_Cl2natInterfaceConfigRowStatus_Object=MibTableColumn
cl2natInterfaceConfigRowStatus=_Cl2natInterfaceConfigRowStatus_Object((1,3,6,1,4,1,9,9,806,1,9,1,5),_Cl2natInterfaceConfigRowStatus_Type())
cl2natInterfaceConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cl2natInterfaceConfigRowStatus.setStatus(_A)
_Cl2natInterfaceStatisticsTable_Object=MibTable
cl2natInterfaceStatisticsTable=_Cl2natInterfaceStatisticsTable_Object((1,3,6,1,4,1,9,9,806,1,10))
if mibBuilder.loadTexts:cl2natInterfaceStatisticsTable.setStatus(_A)
_Cl2natInterfaceStatisticsEntry_Object=MibTableRow
cl2natInterfaceStatisticsEntry=_Cl2natInterfaceStatisticsEntry_Object((1,3,6,1,4,1,9,9,806,1,10,1))
cl2natInterfaceStatisticsEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cl2natInterfaceStatisticsEntry.setStatus(_A)
_Cl2natFixupArpIn_Type=Counter64
_Cl2natFixupArpIn_Object=MibTableColumn
cl2natFixupArpIn=_Cl2natFixupArpIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,1),_Cl2natFixupArpIn_Type())
cl2natFixupArpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupArpIn.setStatus(_A)
_Cl2natFixupIcmpIn_Type=Counter64
_Cl2natFixupIcmpIn_Object=MibTableColumn
cl2natFixupIcmpIn=_Cl2natFixupIcmpIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,2),_Cl2natFixupIcmpIn_Type())
cl2natFixupIcmpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupIcmpIn.setStatus(_A)
_Cl2natFixupCipIn_Type=Counter64
_Cl2natFixupCipIn_Object=MibTableColumn
cl2natFixupCipIn=_Cl2natFixupCipIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,3),_Cl2natFixupCipIn_Type())
cl2natFixupCipIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupCipIn.setStatus(_A)
_Cl2natFixupProfinetIn_Type=Counter64
_Cl2natFixupProfinetIn_Object=MibTableColumn
cl2natFixupProfinetIn=_Cl2natFixupProfinetIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,4),_Cl2natFixupProfinetIn_Type())
cl2natFixupProfinetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupProfinetIn.setStatus(_A)
_Cl2natFixupFtpIn_Type=Counter64
_Cl2natFixupFtpIn_Object=MibTableColumn
cl2natFixupFtpIn=_Cl2natFixupFtpIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,5),_Cl2natFixupFtpIn_Type())
cl2natFixupFtpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupFtpIn.setStatus(_A)
_Cl2natFixupSnmpIn_Type=Counter64
_Cl2natFixupSnmpIn_Object=MibTableColumn
cl2natFixupSnmpIn=_Cl2natFixupSnmpIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,6),_Cl2natFixupSnmpIn_Type())
cl2natFixupSnmpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupSnmpIn.setStatus(_A)
_Cl2natFixupSipIn_Type=Counter64
_Cl2natFixupSipIn_Object=MibTableColumn
cl2natFixupSipIn=_Cl2natFixupSipIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,7),_Cl2natFixupSipIn_Type())
cl2natFixupSipIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupSipIn.setStatus(_A)
_Cl2natFixupSccpIn_Type=Counter64
_Cl2natFixupSccpIn_Object=MibTableColumn
cl2natFixupSccpIn=_Cl2natFixupSccpIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,8),_Cl2natFixupSccpIn_Type())
cl2natFixupSccpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupSccpIn.setStatus(_A)
_Cl2natUnmatchedIn_Type=Counter64
_Cl2natUnmatchedIn_Object=MibTableColumn
cl2natUnmatchedIn=_Cl2natUnmatchedIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,9),_Cl2natUnmatchedIn_Type())
cl2natUnmatchedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natUnmatchedIn.setStatus(_A)
_Cl2natTranslatedUnicastIn_Type=Counter64
_Cl2natTranslatedUnicastIn_Object=MibTableColumn
cl2natTranslatedUnicastIn=_Cl2natTranslatedUnicastIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,10),_Cl2natTranslatedUnicastIn_Type())
cl2natTranslatedUnicastIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTranslatedUnicastIn.setStatus(_A)
_Cl2natDroppedUnicastIn_Type=Counter64
_Cl2natDroppedUnicastIn_Object=MibTableColumn
cl2natDroppedUnicastIn=_Cl2natDroppedUnicastIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,11),_Cl2natDroppedUnicastIn_Type())
cl2natDroppedUnicastIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natDroppedUnicastIn.setStatus(_A)
_Cl2natDroppedMulticastIn_Type=Counter64
_Cl2natDroppedMulticastIn_Object=MibTableColumn
cl2natDroppedMulticastIn=_Cl2natDroppedMulticastIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,12),_Cl2natDroppedMulticastIn_Type())
cl2natDroppedMulticastIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natDroppedMulticastIn.setStatus(_A)
_Cl2natPassThruUnicastIn_Type=Counter64
_Cl2natPassThruUnicastIn_Object=MibTableColumn
cl2natPassThruUnicastIn=_Cl2natPassThruUnicastIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,13),_Cl2natPassThruUnicastIn_Type())
cl2natPassThruUnicastIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natPassThruUnicastIn.setStatus(_A)
_Cl2natPassThruMulticastIn_Type=Counter64
_Cl2natPassThruMulticastIn_Object=MibTableColumn
cl2natPassThruMulticastIn=_Cl2natPassThruMulticastIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,14),_Cl2natPassThruMulticastIn_Type())
cl2natPassThruMulticastIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natPassThruMulticastIn.setStatus(_A)
_Cl2natPassThruIgmpIn_Type=Counter64
_Cl2natPassThruIgmpIn_Object=MibTableColumn
cl2natPassThruIgmpIn=_Cl2natPassThruIgmpIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,15),_Cl2natPassThruIgmpIn_Type())
cl2natPassThruIgmpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natPassThruIgmpIn.setStatus(_A)
_Cl2natDroppedIgmpIn_Type=Counter64
_Cl2natDroppedIgmpIn_Object=MibTableColumn
cl2natDroppedIgmpIn=_Cl2natDroppedIgmpIn_Object((1,3,6,1,4,1,9,9,806,1,10,1,16),_Cl2natDroppedIgmpIn_Type())
cl2natDroppedIgmpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natDroppedIgmpIn.setStatus(_A)
_Cl2natFixupArpOut_Type=Counter64
_Cl2natFixupArpOut_Object=MibTableColumn
cl2natFixupArpOut=_Cl2natFixupArpOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,17),_Cl2natFixupArpOut_Type())
cl2natFixupArpOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupArpOut.setStatus(_A)
_Cl2natFixupIcmpOut_Type=Counter64
_Cl2natFixupIcmpOut_Object=MibTableColumn
cl2natFixupIcmpOut=_Cl2natFixupIcmpOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,18),_Cl2natFixupIcmpOut_Type())
cl2natFixupIcmpOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupIcmpOut.setStatus(_A)
_Cl2natFixupCipOut_Type=Counter64
_Cl2natFixupCipOut_Object=MibTableColumn
cl2natFixupCipOut=_Cl2natFixupCipOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,19),_Cl2natFixupCipOut_Type())
cl2natFixupCipOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupCipOut.setStatus(_A)
_Cl2natFixupProfinetOut_Type=Counter64
_Cl2natFixupProfinetOut_Object=MibTableColumn
cl2natFixupProfinetOut=_Cl2natFixupProfinetOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,20),_Cl2natFixupProfinetOut_Type())
cl2natFixupProfinetOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupProfinetOut.setStatus(_A)
_Cl2natFixupFtpOut_Type=Counter64
_Cl2natFixupFtpOut_Object=MibTableColumn
cl2natFixupFtpOut=_Cl2natFixupFtpOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,21),_Cl2natFixupFtpOut_Type())
cl2natFixupFtpOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupFtpOut.setStatus(_A)
_Cl2natFixupSnmpOut_Type=Counter64
_Cl2natFixupSnmpOut_Object=MibTableColumn
cl2natFixupSnmpOut=_Cl2natFixupSnmpOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,22),_Cl2natFixupSnmpOut_Type())
cl2natFixupSnmpOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupSnmpOut.setStatus(_A)
_Cl2natFixupSipOut_Type=Counter64
_Cl2natFixupSipOut_Object=MibTableColumn
cl2natFixupSipOut=_Cl2natFixupSipOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,23),_Cl2natFixupSipOut_Type())
cl2natFixupSipOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupSipOut.setStatus(_A)
_Cl2natFixupSccpOut_Type=Counter64
_Cl2natFixupSccpOut_Object=MibTableColumn
cl2natFixupSccpOut=_Cl2natFixupSccpOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,24),_Cl2natFixupSccpOut_Type())
cl2natFixupSccpOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natFixupSccpOut.setStatus(_A)
_Cl2natUnmatchedOut_Type=Counter64
_Cl2natUnmatchedOut_Object=MibTableColumn
cl2natUnmatchedOut=_Cl2natUnmatchedOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,25),_Cl2natUnmatchedOut_Type())
cl2natUnmatchedOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natUnmatchedOut.setStatus(_A)
_Cl2natDroppedUnicastOut_Type=Counter64
_Cl2natDroppedUnicastOut_Object=MibTableColumn
cl2natDroppedUnicastOut=_Cl2natDroppedUnicastOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,26),_Cl2natDroppedUnicastOut_Type())
cl2natDroppedUnicastOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natDroppedUnicastOut.setStatus(_A)
_Cl2natTranslatedUnicastOut_Type=Counter64
_Cl2natTranslatedUnicastOut_Object=MibTableColumn
cl2natTranslatedUnicastOut=_Cl2natTranslatedUnicastOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,27),_Cl2natTranslatedUnicastOut_Type())
cl2natTranslatedUnicastOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTranslatedUnicastOut.setStatus(_A)
_Cl2natPassThruUnicastOut_Type=Counter64
_Cl2natPassThruUnicastOut_Object=MibTableColumn
cl2natPassThruUnicastOut=_Cl2natPassThruUnicastOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,28),_Cl2natPassThruUnicastOut_Type())
cl2natPassThruUnicastOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natPassThruUnicastOut.setStatus(_A)
_Cl2natDroppedMulticastOut_Type=Counter64
_Cl2natDroppedMulticastOut_Object=MibTableColumn
cl2natDroppedMulticastOut=_Cl2natDroppedMulticastOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,29),_Cl2natDroppedMulticastOut_Type())
cl2natDroppedMulticastOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natDroppedMulticastOut.setStatus(_A)
_Cl2natPassThruMulticastOut_Type=Counter64
_Cl2natPassThruMulticastOut_Object=MibTableColumn
cl2natPassThruMulticastOut=_Cl2natPassThruMulticastOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,30),_Cl2natPassThruMulticastOut_Type())
cl2natPassThruMulticastOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natPassThruMulticastOut.setStatus(_A)
_Cl2natDroppedIgmpOut_Type=Counter64
_Cl2natDroppedIgmpOut_Object=MibTableColumn
cl2natDroppedIgmpOut=_Cl2natDroppedIgmpOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,31),_Cl2natDroppedIgmpOut_Type())
cl2natDroppedIgmpOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natDroppedIgmpOut.setStatus(_A)
_Cl2natPassThruIgmpOut_Type=Counter64
_Cl2natPassThruIgmpOut_Object=MibTableColumn
cl2natPassThruIgmpOut=_Cl2natPassThruIgmpOut_Object((1,3,6,1,4,1,9,9,806,1,10,1,32),_Cl2natPassThruIgmpOut_Type())
cl2natPassThruIgmpOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natPassThruIgmpOut.setStatus(_A)
_Cl2natInterfaceIpStatisticsTable_Object=MibTable
cl2natInterfaceIpStatisticsTable=_Cl2natInterfaceIpStatisticsTable_Object((1,3,6,1,4,1,9,9,806,1,11))
if mibBuilder.loadTexts:cl2natInterfaceIpStatisticsTable.setStatus(_A)
_Cl2natInterfaceIpStatisticsEntry_Object=MibTableRow
cl2natInterfaceIpStatisticsEntry=_Cl2natInterfaceIpStatisticsEntry_Object((1,3,6,1,4,1,9,9,806,1,11,1))
cl2natInterfaceIpStatisticsEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:cl2natInterfaceIpStatisticsEntry.setStatus(_A)
_Cl2natTranslatesIn_Type=Counter64
_Cl2natTranslatesIn_Object=MibTableColumn
cl2natTranslatesIn=_Cl2natTranslatesIn_Object((1,3,6,1,4,1,9,9,806,1,11,1,1),_Cl2natTranslatesIn_Type())
cl2natTranslatesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTranslatesIn.setStatus(_A)
_Cl2natTranslatesOut_Type=Counter64
_Cl2natTranslatesOut_Object=MibTableColumn
cl2natTranslatesOut=_Cl2natTranslatesOut_Object((1,3,6,1,4,1,9,9,806,1,11,1,2),_Cl2natTranslatesOut_Type())
cl2natTranslatesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cl2natTranslatesOut.setStatus(_A)
_CiscoL2natMIBConformance_ObjectIdentity=ObjectIdentity
ciscoL2natMIBConformance=_CiscoL2natMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,806,3))
_CiscoL2natMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoL2natMIBCompliances=_CiscoL2natMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,806,3,1))
_CiscoL2natMIBGroups_ObjectIdentity=ObjectIdentity
ciscoL2natMIBGroups=_CiscoL2natMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,806,3,2))
cl2natGlobalStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,806,3,2,1))
cl2natGlobalStatisticsGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cl2natGlobalStatisticsGroup.setStatus(_A)
cl2natInstanceConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,806,3,2,2))
cl2natInstanceConfigGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cl2natInstanceConfigGroup.setStatus(_A)
cl2natInstanceStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,806,3,2,3))
cl2natInstanceStatisticsGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:cl2natInstanceStatisticsGroup.setStatus(_A)
cl2natInstanceTranslationStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,806,3,2,4))
cl2natInstanceTranslationStatisticsGroup.setObjects(*((_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cl2natInstanceTranslationStatisticsGroup.setStatus(_A)
ciscoL2natMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,806,3,1,1))
ciscoL2natMIBCompliance.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:ciscoL2natMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoL2natMIB':ciscoL2natMIB,'ciscoL2natMIBObjects':ciscoL2natMIBObjects,_S:cl2natTotalInstances,_T:cl2natTotalMatched,_U:cl2natTotalUnmatched,_V:cl2natTotalFixups,_W:cl2natTotalTranslationEntryConfigured,_X:cl2natTotalPacketTranslated,'cl2natInstConfigInstanceTable':cl2natInstConfigInstanceTable,'cl2natInstConfigInstanceEntry':cl2natInstConfigInstanceEntry,_L:cl2natInstConfigInstanceName,_Y:cl2natInstConfigPermitIn,_Z:cl2natInstConfigPermitOut,_a:cl2natInstConfigFixup,_j:cl2natInstConfigStorageType,_e:cl2natInstConfigInstanceRowStatus,'cl2natInstIpInstanceIpTable':cl2natInstIpInstanceIpTable,'cl2natInstIpInstanceIpEntry':cl2natInstIpInstanceIpEntry,_M:cl2natInstIpDirection,_R:cl2natInstIpAddressType,_N:cl2natInstIpFromIpAddressType,_O:cl2natInstIpFromIpAddress,_d:cl2natInstIpToIpAddressType,_c:cl2natInstIpToIpAddress,_g:cl2natInstIpAddressMask,_b:cl2natInstIpRange,_k:cl2natInstStorageIpStorageType,_i:cl2natInstIpRowStatus,'cl2natInterfaceConfigTable':cl2natInterfaceConfigTable,'cl2natInterfaceConfigEntry':cl2natInterfaceConfigEntry,_H:cl2natInterfaceConfigIfIndex,_I:cl2natInterfaceConfigVlanIndex,_h:cl2natInterfaceConfigInstanceName,_l:cl2natInterfaceConfigStorageType,_f:cl2natInterfaceConfigRowStatus,'cl2natInterfaceStatisticsTable':cl2natInterfaceStatisticsTable,'cl2natInterfaceStatisticsEntry':cl2natInterfaceStatisticsEntry,_p:cl2natFixupArpIn,_q:cl2natFixupIcmpIn,_r:cl2natFixupCipIn,_s:cl2natFixupProfinetIn,_t:cl2natFixupFtpIn,_u:cl2natFixupSnmpIn,_v:cl2natFixupSipIn,_w:cl2natFixupSccpIn,_m:cl2natUnmatchedIn,_o:cl2natTranslatedUnicastIn,_n:cl2natDroppedUnicastIn,_AA:cl2natDroppedMulticastIn,_A8:cl2natPassThruUnicastIn,_AC:cl2natPassThruMulticastIn,_AG:cl2natPassThruIgmpIn,_AE:cl2natDroppedIgmpIn,_A0:cl2natFixupArpOut,_A1:cl2natFixupIcmpOut,_A2:cl2natFixupCipOut,_A3:cl2natFixupProfinetOut,_A4:cl2natFixupFtpOut,_A5:cl2natFixupSnmpOut,_A6:cl2natFixupSipOut,_A7:cl2natFixupSccpOut,_x:cl2natUnmatchedOut,_y:cl2natDroppedUnicastOut,_z:cl2natTranslatedUnicastOut,_A9:cl2natPassThruUnicastOut,_AB:cl2natDroppedMulticastOut,_AD:cl2natPassThruMulticastOut,_AF:cl2natDroppedIgmpOut,_AH:cl2natPassThruIgmpOut,'cl2natInterfaceIpStatisticsTable':cl2natInterfaceIpStatisticsTable,'cl2natInterfaceIpStatisticsEntry':cl2natInterfaceIpStatisticsEntry,_AI:cl2natTranslatesIn,_AJ:cl2natTranslatesOut,'ciscoL2natMIBConformance':ciscoL2natMIBConformance,'ciscoL2natMIBCompliances':ciscoL2natMIBCompliances,'ciscoL2natMIBCompliance':ciscoL2natMIBCompliance,'ciscoL2natMIBGroups':ciscoL2natMIBGroups,_AK:cl2natGlobalStatisticsGroup,_AL:cl2natInstanceConfigGroup,_AM:cl2natInstanceStatisticsGroup,_AN:cl2natInstanceTranslationStatisticsGroup})