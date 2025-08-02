_l='fsDhcpSnoopingMIBGroup'
_k='fsSNDhcpBindingsStatus'
_j='fsSNDhcpBindingsLeasedTime'
_i='fsSNDhcpBindingsInterface'
_h='fsSNDhcpBindingsIpAddress'
_g='fsDhcpPktIfRateDiscardNum'
_f='fsUntrustedReplyPktNum'
_e='fsNomatchSnpBindTblDhcpPktNum'
_d='fsIpNomatchSnpBindTblPktNum'
_c='fsArpNomatchSnpBindTblPktNum'
_b='fsChaddrNomatchSrcMacDhcpPktNum'
_a='fsDhcpSnpStatisticVlanId'
_Z='fsDhcpSnpStatisticIfDescr'
_Y='fsSNDhcpAddressBindEnable'
_X='fsSNDhcpIfSuppressionEnable'
_W='fsSNDhcpIfTrustEnable'
_V='fsSNDhcpMatchMacAddressEnable'
_U='fsSNDhcpRelayAgentInfoOptEnable'
_T='fsSNDhcpDatabaseUpdateInterval'
_S='fsSNDhcpFeatureEnable'
_R='fsSNDhcpBindingsAddrType'
_Q='fsSNDhcpBindingsMacAddress'
_P='fsSNDhcpBindingsVlan'
_O='fsDhcpSnpStatisticVlanIndex'
_N='fsDhcpSnpStatisticIfIndex'
_M='fsSNDhcpAddressBindIndex'
_L='fsSNDhcpIfSuppressionIndex'
_K='fsSNDhcpIfTrustIndex'
_J='seconds'
_I='DisplayString'
_H='Integer32'
_G='fsDhcpTrapMacAddress'
_F='read-create'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='FS-DHCP-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsDhcpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,42))
if mibBuilder.loadTexts:fsDhcpSnoopingMIB.setRevisions(('2007-10-18 00:00',))
_FsDhcpSnoopingMIBTraps_ObjectIdentity=ObjectIdentity
fsDhcpSnoopingMIBTraps=_FsDhcpSnoopingMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,0))
_FsDhcpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
fsDhcpSnoopingMIBObjects=_FsDhcpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,1))
_FsSNDhcpGlobal_ObjectIdentity=ObjectIdentity
fsSNDhcpGlobal=_FsSNDhcpGlobal_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,1,1))
_FsSNDhcpFeatureEnable_Type=TruthValue
_FsSNDhcpFeatureEnable_Object=MibScalar
fsSNDhcpFeatureEnable=_FsSNDhcpFeatureEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,1,1),_FsSNDhcpFeatureEnable_Type())
fsSNDhcpFeatureEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNDhcpFeatureEnable.setStatus(_A)
_FsSNDhcpDatabaseUpdateInterval_Type=Unsigned32
_FsSNDhcpDatabaseUpdateInterval_Object=MibScalar
fsSNDhcpDatabaseUpdateInterval=_FsSNDhcpDatabaseUpdateInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,1,2),_FsSNDhcpDatabaseUpdateInterval_Type())
fsSNDhcpDatabaseUpdateInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNDhcpDatabaseUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:fsSNDhcpDatabaseUpdateInterval.setUnits(_J)
_FsSNDhcpRelayAgentInfoOptEnable_Type=TruthValue
_FsSNDhcpRelayAgentInfoOptEnable_Object=MibScalar
fsSNDhcpRelayAgentInfoOptEnable=_FsSNDhcpRelayAgentInfoOptEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,1,3),_FsSNDhcpRelayAgentInfoOptEnable_Type())
fsSNDhcpRelayAgentInfoOptEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNDhcpRelayAgentInfoOptEnable.setStatus(_A)
_FsSNDhcpMatchMacAddressEnable_Type=TruthValue
_FsSNDhcpMatchMacAddressEnable_Object=MibScalar
fsSNDhcpMatchMacAddressEnable=_FsSNDhcpMatchMacAddressEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,1,4),_FsSNDhcpMatchMacAddressEnable_Type())
fsSNDhcpMatchMacAddressEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNDhcpMatchMacAddressEnable.setStatus(_A)
_FsSNDhcpInterface_ObjectIdentity=ObjectIdentity
fsSNDhcpInterface=_FsSNDhcpInterface_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,1,2))
_FsSNDhcpIfTrustTable_Object=MibTable
fsSNDhcpIfTrustTable=_FsSNDhcpIfTrustTable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,1))
if mibBuilder.loadTexts:fsSNDhcpIfTrustTable.setStatus(_A)
_FsSNDhcpIfTrustEntry_Object=MibTableRow
fsSNDhcpIfTrustEntry=_FsSNDhcpIfTrustEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,1,1))
fsSNDhcpIfTrustEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsSNDhcpIfTrustEntry.setStatus(_A)
_FsSNDhcpIfTrustIndex_Type=InterfaceIndex
_FsSNDhcpIfTrustIndex_Object=MibTableColumn
fsSNDhcpIfTrustIndex=_FsSNDhcpIfTrustIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,1,1,1),_FsSNDhcpIfTrustIndex_Type())
fsSNDhcpIfTrustIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNDhcpIfTrustIndex.setStatus(_A)
_FsSNDhcpIfTrustEnable_Type=TruthValue
_FsSNDhcpIfTrustEnable_Object=MibTableColumn
fsSNDhcpIfTrustEnable=_FsSNDhcpIfTrustEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,1,1,2),_FsSNDhcpIfTrustEnable_Type())
fsSNDhcpIfTrustEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNDhcpIfTrustEnable.setStatus(_A)
_FsSNDhcpIfSuppressionTable_Object=MibTable
fsSNDhcpIfSuppressionTable=_FsSNDhcpIfSuppressionTable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,2))
if mibBuilder.loadTexts:fsSNDhcpIfSuppressionTable.setStatus(_A)
_FsSNDhcpIfSuppressionEntry_Object=MibTableRow
fsSNDhcpIfSuppressionEntry=_FsSNDhcpIfSuppressionEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,2,1))
fsSNDhcpIfSuppressionEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:fsSNDhcpIfSuppressionEntry.setStatus(_A)
_FsSNDhcpIfSuppressionIndex_Type=InterfaceIndex
_FsSNDhcpIfSuppressionIndex_Object=MibTableColumn
fsSNDhcpIfSuppressionIndex=_FsSNDhcpIfSuppressionIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,2,1,1),_FsSNDhcpIfSuppressionIndex_Type())
fsSNDhcpIfSuppressionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNDhcpIfSuppressionIndex.setStatus(_A)
_FsSNDhcpIfSuppressionEnable_Type=TruthValue
_FsSNDhcpIfSuppressionEnable_Object=MibTableColumn
fsSNDhcpIfSuppressionEnable=_FsSNDhcpIfSuppressionEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,2,1,2),_FsSNDhcpIfSuppressionEnable_Type())
fsSNDhcpIfSuppressionEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNDhcpIfSuppressionEnable.setStatus(_A)
_FsSNDhcpAddressBindTable_Object=MibTable
fsSNDhcpAddressBindTable=_FsSNDhcpAddressBindTable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,3))
if mibBuilder.loadTexts:fsSNDhcpAddressBindTable.setStatus(_A)
_FsSNDhcpAddressBindEntry_Object=MibTableRow
fsSNDhcpAddressBindEntry=_FsSNDhcpAddressBindEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,3,1))
fsSNDhcpAddressBindEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:fsSNDhcpAddressBindEntry.setStatus(_A)
_FsSNDhcpAddressBindIndex_Type=InterfaceIndex
_FsSNDhcpAddressBindIndex_Object=MibTableColumn
fsSNDhcpAddressBindIndex=_FsSNDhcpAddressBindIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,3,1,1),_FsSNDhcpAddressBindIndex_Type())
fsSNDhcpAddressBindIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNDhcpAddressBindIndex.setStatus(_A)
_FsSNDhcpAddressBindEnable_Type=TruthValue
_FsSNDhcpAddressBindEnable_Object=MibTableColumn
fsSNDhcpAddressBindEnable=_FsSNDhcpAddressBindEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,3,1,2),_FsSNDhcpAddressBindEnable_Type())
fsSNDhcpAddressBindEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNDhcpAddressBindEnable.setStatus(_A)
_FsDhcpSnpFalsePktStatisticTable_Object=MibTable
fsDhcpSnpFalsePktStatisticTable=_FsDhcpSnpFalsePktStatisticTable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4))
if mibBuilder.loadTexts:fsDhcpSnpFalsePktStatisticTable.setStatus(_A)
_FsDhcpSnpFalsePktStatisticEntry_Object=MibTableRow
fsDhcpSnpFalsePktStatisticEntry=_FsDhcpSnpFalsePktStatisticEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1))
fsDhcpSnpFalsePktStatisticEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:fsDhcpSnpFalsePktStatisticEntry.setStatus(_A)
_FsDhcpSnpStatisticIfIndex_Type=InterfaceIndex
_FsDhcpSnpStatisticIfIndex_Object=MibTableColumn
fsDhcpSnpStatisticIfIndex=_FsDhcpSnpStatisticIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,1),_FsDhcpSnpStatisticIfIndex_Type())
fsDhcpSnpStatisticIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpSnpStatisticIfIndex.setStatus(_A)
_FsDhcpSnpStatisticVlanIndex_Type=VlanIndex
_FsDhcpSnpStatisticVlanIndex_Object=MibTableColumn
fsDhcpSnpStatisticVlanIndex=_FsDhcpSnpStatisticVlanIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,2),_FsDhcpSnpStatisticVlanIndex_Type())
fsDhcpSnpStatisticVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpSnpStatisticVlanIndex.setStatus(_A)
class _FsDhcpSnpStatisticIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDhcpSnpStatisticIfDescr_Type.__name__=_I
_FsDhcpSnpStatisticIfDescr_Object=MibTableColumn
fsDhcpSnpStatisticIfDescr=_FsDhcpSnpStatisticIfDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,3),_FsDhcpSnpStatisticIfDescr_Type())
fsDhcpSnpStatisticIfDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpSnpStatisticIfDescr.setStatus(_A)
_FsDhcpSnpStatisticVlanId_Type=VlanIndex
_FsDhcpSnpStatisticVlanId_Object=MibTableColumn
fsDhcpSnpStatisticVlanId=_FsDhcpSnpStatisticVlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,4),_FsDhcpSnpStatisticVlanId_Type())
fsDhcpSnpStatisticVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpSnpStatisticVlanId.setStatus(_A)
_FsChaddrNomatchSrcMacDhcpPktNum_Type=Counter32
_FsChaddrNomatchSrcMacDhcpPktNum_Object=MibTableColumn
fsChaddrNomatchSrcMacDhcpPktNum=_FsChaddrNomatchSrcMacDhcpPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,5),_FsChaddrNomatchSrcMacDhcpPktNum_Type())
fsChaddrNomatchSrcMacDhcpPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsChaddrNomatchSrcMacDhcpPktNum.setStatus(_A)
_FsArpNomatchSnpBindTblPktNum_Type=Counter32
_FsArpNomatchSnpBindTblPktNum_Object=MibTableColumn
fsArpNomatchSnpBindTblPktNum=_FsArpNomatchSnpBindTblPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,6),_FsArpNomatchSnpBindTblPktNum_Type())
fsArpNomatchSnpBindTblPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpNomatchSnpBindTblPktNum.setStatus(_A)
_FsIpNomatchSnpBindTblPktNum_Type=Counter32
_FsIpNomatchSnpBindTblPktNum_Object=MibTableColumn
fsIpNomatchSnpBindTblPktNum=_FsIpNomatchSnpBindTblPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,7),_FsIpNomatchSnpBindTblPktNum_Type())
fsIpNomatchSnpBindTblPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpNomatchSnpBindTblPktNum.setStatus(_A)
_FsNomatchSnpBindTblDhcpPktNum_Type=Counter32
_FsNomatchSnpBindTblDhcpPktNum_Object=MibTableColumn
fsNomatchSnpBindTblDhcpPktNum=_FsNomatchSnpBindTblDhcpPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,8),_FsNomatchSnpBindTblDhcpPktNum_Type())
fsNomatchSnpBindTblDhcpPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNomatchSnpBindTblDhcpPktNum.setStatus(_A)
_FsUntrustedReplyPktNum_Type=Counter32
_FsUntrustedReplyPktNum_Object=MibTableColumn
fsUntrustedReplyPktNum=_FsUntrustedReplyPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,9),_FsUntrustedReplyPktNum_Type())
fsUntrustedReplyPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsUntrustedReplyPktNum.setStatus(_A)
_FsDhcpPktIfRateDiscardNum_Type=Counter32
_FsDhcpPktIfRateDiscardNum_Object=MibTableColumn
fsDhcpPktIfRateDiscardNum=_FsDhcpPktIfRateDiscardNum_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,2,4,1,10),_FsDhcpPktIfRateDiscardNum_Type())
fsDhcpPktIfRateDiscardNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpPktIfRateDiscardNum.setStatus(_A)
_FsSNDhcpBindings_ObjectIdentity=ObjectIdentity
fsSNDhcpBindings=_FsSNDhcpBindings_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,1,3))
_FsSNDhcpBindingsTable_Object=MibTable
fsSNDhcpBindingsTable=_FsSNDhcpBindingsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1))
if mibBuilder.loadTexts:fsSNDhcpBindingsTable.setStatus(_A)
_FsSNDhcpBindingsEntry_Object=MibTableRow
fsSNDhcpBindingsEntry=_FsSNDhcpBindingsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1))
fsSNDhcpBindingsEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:fsSNDhcpBindingsEntry.setStatus(_A)
_FsSNDhcpBindingsVlan_Type=VlanIndex
_FsSNDhcpBindingsVlan_Object=MibTableColumn
fsSNDhcpBindingsVlan=_FsSNDhcpBindingsVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1,1),_FsSNDhcpBindingsVlan_Type())
fsSNDhcpBindingsVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNDhcpBindingsVlan.setStatus(_A)
_FsSNDhcpBindingsMacAddress_Type=MacAddress
_FsSNDhcpBindingsMacAddress_Object=MibTableColumn
fsSNDhcpBindingsMacAddress=_FsSNDhcpBindingsMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1,2),_FsSNDhcpBindingsMacAddress_Type())
fsSNDhcpBindingsMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNDhcpBindingsMacAddress.setStatus(_A)
class _FsSNDhcpBindingsAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_FsSNDhcpBindingsAddrType_Type.__name__=_H
_FsSNDhcpBindingsAddrType_Object=MibTableColumn
fsSNDhcpBindingsAddrType=_FsSNDhcpBindingsAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1,3),_FsSNDhcpBindingsAddrType_Type())
fsSNDhcpBindingsAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNDhcpBindingsAddrType.setStatus(_A)
_FsSNDhcpBindingsIpAddress_Type=IpAddress
_FsSNDhcpBindingsIpAddress_Object=MibTableColumn
fsSNDhcpBindingsIpAddress=_FsSNDhcpBindingsIpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1,4),_FsSNDhcpBindingsIpAddress_Type())
fsSNDhcpBindingsIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSNDhcpBindingsIpAddress.setStatus(_A)
_FsSNDhcpBindingsInterface_Type=InterfaceIndex
_FsSNDhcpBindingsInterface_Object=MibTableColumn
fsSNDhcpBindingsInterface=_FsSNDhcpBindingsInterface_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1,5),_FsSNDhcpBindingsInterface_Type())
fsSNDhcpBindingsInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSNDhcpBindingsInterface.setStatus(_A)
_FsSNDhcpBindingsLeasedTime_Type=Unsigned32
_FsSNDhcpBindingsLeasedTime_Object=MibTableColumn
fsSNDhcpBindingsLeasedTime=_FsSNDhcpBindingsLeasedTime_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1,6),_FsSNDhcpBindingsLeasedTime_Type())
fsSNDhcpBindingsLeasedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSNDhcpBindingsLeasedTime.setStatus(_A)
if mibBuilder.loadTexts:fsSNDhcpBindingsLeasedTime.setUnits(_J)
_FsSNDhcpBindingsStatus_Type=RowStatus
_FsSNDhcpBindingsStatus_Object=MibTableColumn
fsSNDhcpBindingsStatus=_FsSNDhcpBindingsStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,3,1,1,7),_FsSNDhcpBindingsStatus_Type())
fsSNDhcpBindingsStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSNDhcpBindingsStatus.setStatus(_A)
_FsDhcpTrapMacAddress_Type=MacAddress
_FsDhcpTrapMacAddress_Object=MibScalar
fsDhcpTrapMacAddress=_FsDhcpTrapMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,42,1,4),_FsDhcpTrapMacAddress_Type())
fsDhcpTrapMacAddress.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:fsDhcpTrapMacAddress.setStatus(_A)
_FsDhcpSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
fsDhcpSnoopingMIBConformance=_FsDhcpSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,2))
_FsDhcpSnoopingMIBCompliances_ObjectIdentity=ObjectIdentity
fsDhcpSnoopingMIBCompliances=_FsDhcpSnoopingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,2,1))
_FsDhcpSnoopingMIBGroups_ObjectIdentity=ObjectIdentity
fsDhcpSnoopingMIBGroups=_FsDhcpSnoopingMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,42,2,2))
fsDhcpSnoopingMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,42,2,2,1))
fsDhcpSnoopingMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_G)))
if mibBuilder.loadTexts:fsDhcpSnoopingMIBGroup.setStatus(_A)
fsDhcpSnoopingNoResponseTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,42,0,1))
fsDhcpSnoopingNoResponseTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:fsDhcpSnoopingNoResponseTrap.setStatus(_A)
fsDhcpSnoopingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,42,2,1,1))
fsDhcpSnoopingMIBCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:fsDhcpSnoopingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsDhcpSnoopingMIB':fsDhcpSnoopingMIB,'fsDhcpSnoopingMIBTraps':fsDhcpSnoopingMIBTraps,'fsDhcpSnoopingNoResponseTrap':fsDhcpSnoopingNoResponseTrap,'fsDhcpSnoopingMIBObjects':fsDhcpSnoopingMIBObjects,'fsSNDhcpGlobal':fsSNDhcpGlobal,_S:fsSNDhcpFeatureEnable,_T:fsSNDhcpDatabaseUpdateInterval,_U:fsSNDhcpRelayAgentInfoOptEnable,_V:fsSNDhcpMatchMacAddressEnable,'fsSNDhcpInterface':fsSNDhcpInterface,'fsSNDhcpIfTrustTable':fsSNDhcpIfTrustTable,'fsSNDhcpIfTrustEntry':fsSNDhcpIfTrustEntry,_K:fsSNDhcpIfTrustIndex,_W:fsSNDhcpIfTrustEnable,'fsSNDhcpIfSuppressionTable':fsSNDhcpIfSuppressionTable,'fsSNDhcpIfSuppressionEntry':fsSNDhcpIfSuppressionEntry,_L:fsSNDhcpIfSuppressionIndex,_X:fsSNDhcpIfSuppressionEnable,'fsSNDhcpAddressBindTable':fsSNDhcpAddressBindTable,'fsSNDhcpAddressBindEntry':fsSNDhcpAddressBindEntry,_M:fsSNDhcpAddressBindIndex,_Y:fsSNDhcpAddressBindEnable,'fsDhcpSnpFalsePktStatisticTable':fsDhcpSnpFalsePktStatisticTable,'fsDhcpSnpFalsePktStatisticEntry':fsDhcpSnpFalsePktStatisticEntry,_N:fsDhcpSnpStatisticIfIndex,_O:fsDhcpSnpStatisticVlanIndex,_Z:fsDhcpSnpStatisticIfDescr,_a:fsDhcpSnpStatisticVlanId,_b:fsChaddrNomatchSrcMacDhcpPktNum,_c:fsArpNomatchSnpBindTblPktNum,_d:fsIpNomatchSnpBindTblPktNum,_e:fsNomatchSnpBindTblDhcpPktNum,_f:fsUntrustedReplyPktNum,_g:fsDhcpPktIfRateDiscardNum,'fsSNDhcpBindings':fsSNDhcpBindings,'fsSNDhcpBindingsTable':fsSNDhcpBindingsTable,'fsSNDhcpBindingsEntry':fsSNDhcpBindingsEntry,_P:fsSNDhcpBindingsVlan,_Q:fsSNDhcpBindingsMacAddress,_R:fsSNDhcpBindingsAddrType,_h:fsSNDhcpBindingsIpAddress,_i:fsSNDhcpBindingsInterface,_j:fsSNDhcpBindingsLeasedTime,_k:fsSNDhcpBindingsStatus,_G:fsDhcpTrapMacAddress,'fsDhcpSnoopingMIBConformance':fsDhcpSnoopingMIBConformance,'fsDhcpSnoopingMIBCompliances':fsDhcpSnoopingMIBCompliances,'fsDhcpSnoopingMIBCompliance':fsDhcpSnoopingMIBCompliance,'fsDhcpSnoopingMIBGroups':fsDhcpSnoopingMIBGroups,_l:fsDhcpSnoopingMIBGroup})