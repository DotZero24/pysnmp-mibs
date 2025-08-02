_l='qtechDhcpSnoopingMIBGroup'
_k='qtechSNDhcpBindingsStatus'
_j='qtechSNDhcpBindingsLeasedTime'
_i='qtechSNDhcpBindingsInterface'
_h='qtechSNDhcpBindingsIpAddress'
_g='qtechDhcpPktIfRateDiscardNum'
_f='qtechUntrustedReplyPktNum'
_e='qtechNomatchSnpBindTblDhcpPktNum'
_d='qtechIpNomatchSnpBindTblPktNum'
_c='qtechArpNomatchSnpBindTblPktNum'
_b='qtechChaddrNomatchSrcMacDhcpPktNum'
_a='qtechDhcpSnpStatisticVlanId'
_Z='qtechDhcpSnpStatisticIfDescr'
_Y='qtechSNDhcpAddressBindEnable'
_X='qtechSNDhcpIfSuppressionEnable'
_W='qtechSNDhcpIfTrustEnable'
_V='qtechSNDhcpMatchMacAddressEnable'
_U='qtechSNDhcpRelayAgentInfoOptEnable'
_T='qtechSNDhcpDatabaseUpdateInterval'
_S='qtechSNDhcpFeatureEnable'
_R='qtechSNDhcpBindingsAddrType'
_Q='qtechSNDhcpBindingsMacAddress'
_P='qtechSNDhcpBindingsVlan'
_O='qtechDhcpSnpStatisticVlanIndex'
_N='qtechDhcpSnpStatisticIfIndex'
_M='qtechSNDhcpAddressBindIndex'
_L='qtechSNDhcpIfSuppressionIndex'
_K='qtechSNDhcpIfTrustIndex'
_J='seconds'
_I='DisplayString'
_H='Integer32'
_G='qtechDhcpTrapMacAddress'
_F='read-create'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='QTECH-DHCP-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechDhcpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,42))
if mibBuilder.loadTexts:qtechDhcpSnoopingMIB.setRevisions(('2007-10-18 00:00',))
_QtechDhcpSnoopingMIBTraps_ObjectIdentity=ObjectIdentity
qtechDhcpSnoopingMIBTraps=_QtechDhcpSnoopingMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,0))
_QtechDhcpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
qtechDhcpSnoopingMIBObjects=_QtechDhcpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,1))
_QtechSNDhcpGlobal_ObjectIdentity=ObjectIdentity
qtechSNDhcpGlobal=_QtechSNDhcpGlobal_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,1,1))
_QtechSNDhcpFeatureEnable_Type=TruthValue
_QtechSNDhcpFeatureEnable_Object=MibScalar
qtechSNDhcpFeatureEnable=_QtechSNDhcpFeatureEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,1,1),_QtechSNDhcpFeatureEnable_Type())
qtechSNDhcpFeatureEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNDhcpFeatureEnable.setStatus(_A)
_QtechSNDhcpDatabaseUpdateInterval_Type=Unsigned32
_QtechSNDhcpDatabaseUpdateInterval_Object=MibScalar
qtechSNDhcpDatabaseUpdateInterval=_QtechSNDhcpDatabaseUpdateInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,1,2),_QtechSNDhcpDatabaseUpdateInterval_Type())
qtechSNDhcpDatabaseUpdateInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNDhcpDatabaseUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechSNDhcpDatabaseUpdateInterval.setUnits(_J)
_QtechSNDhcpRelayAgentInfoOptEnable_Type=TruthValue
_QtechSNDhcpRelayAgentInfoOptEnable_Object=MibScalar
qtechSNDhcpRelayAgentInfoOptEnable=_QtechSNDhcpRelayAgentInfoOptEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,1,3),_QtechSNDhcpRelayAgentInfoOptEnable_Type())
qtechSNDhcpRelayAgentInfoOptEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNDhcpRelayAgentInfoOptEnable.setStatus(_A)
_QtechSNDhcpMatchMacAddressEnable_Type=TruthValue
_QtechSNDhcpMatchMacAddressEnable_Object=MibScalar
qtechSNDhcpMatchMacAddressEnable=_QtechSNDhcpMatchMacAddressEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,1,4),_QtechSNDhcpMatchMacAddressEnable_Type())
qtechSNDhcpMatchMacAddressEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNDhcpMatchMacAddressEnable.setStatus(_A)
_QtechSNDhcpInterface_ObjectIdentity=ObjectIdentity
qtechSNDhcpInterface=_QtechSNDhcpInterface_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,1,2))
_QtechSNDhcpIfTrustTable_Object=MibTable
qtechSNDhcpIfTrustTable=_QtechSNDhcpIfTrustTable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,1))
if mibBuilder.loadTexts:qtechSNDhcpIfTrustTable.setStatus(_A)
_QtechSNDhcpIfTrustEntry_Object=MibTableRow
qtechSNDhcpIfTrustEntry=_QtechSNDhcpIfTrustEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,1,1))
qtechSNDhcpIfTrustEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechSNDhcpIfTrustEntry.setStatus(_A)
_QtechSNDhcpIfTrustIndex_Type=InterfaceIndex
_QtechSNDhcpIfTrustIndex_Object=MibTableColumn
qtechSNDhcpIfTrustIndex=_QtechSNDhcpIfTrustIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,1,1,1),_QtechSNDhcpIfTrustIndex_Type())
qtechSNDhcpIfTrustIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNDhcpIfTrustIndex.setStatus(_A)
_QtechSNDhcpIfTrustEnable_Type=TruthValue
_QtechSNDhcpIfTrustEnable_Object=MibTableColumn
qtechSNDhcpIfTrustEnable=_QtechSNDhcpIfTrustEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,1,1,2),_QtechSNDhcpIfTrustEnable_Type())
qtechSNDhcpIfTrustEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNDhcpIfTrustEnable.setStatus(_A)
_QtechSNDhcpIfSuppressionTable_Object=MibTable
qtechSNDhcpIfSuppressionTable=_QtechSNDhcpIfSuppressionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,2))
if mibBuilder.loadTexts:qtechSNDhcpIfSuppressionTable.setStatus(_A)
_QtechSNDhcpIfSuppressionEntry_Object=MibTableRow
qtechSNDhcpIfSuppressionEntry=_QtechSNDhcpIfSuppressionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,2,1))
qtechSNDhcpIfSuppressionEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qtechSNDhcpIfSuppressionEntry.setStatus(_A)
_QtechSNDhcpIfSuppressionIndex_Type=InterfaceIndex
_QtechSNDhcpIfSuppressionIndex_Object=MibTableColumn
qtechSNDhcpIfSuppressionIndex=_QtechSNDhcpIfSuppressionIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,2,1,1),_QtechSNDhcpIfSuppressionIndex_Type())
qtechSNDhcpIfSuppressionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNDhcpIfSuppressionIndex.setStatus(_A)
_QtechSNDhcpIfSuppressionEnable_Type=TruthValue
_QtechSNDhcpIfSuppressionEnable_Object=MibTableColumn
qtechSNDhcpIfSuppressionEnable=_QtechSNDhcpIfSuppressionEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,2,1,2),_QtechSNDhcpIfSuppressionEnable_Type())
qtechSNDhcpIfSuppressionEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNDhcpIfSuppressionEnable.setStatus(_A)
_QtechSNDhcpAddressBindTable_Object=MibTable
qtechSNDhcpAddressBindTable=_QtechSNDhcpAddressBindTable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,3))
if mibBuilder.loadTexts:qtechSNDhcpAddressBindTable.setStatus(_A)
_QtechSNDhcpAddressBindEntry_Object=MibTableRow
qtechSNDhcpAddressBindEntry=_QtechSNDhcpAddressBindEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,3,1))
qtechSNDhcpAddressBindEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qtechSNDhcpAddressBindEntry.setStatus(_A)
_QtechSNDhcpAddressBindIndex_Type=InterfaceIndex
_QtechSNDhcpAddressBindIndex_Object=MibTableColumn
qtechSNDhcpAddressBindIndex=_QtechSNDhcpAddressBindIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,3,1,1),_QtechSNDhcpAddressBindIndex_Type())
qtechSNDhcpAddressBindIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNDhcpAddressBindIndex.setStatus(_A)
_QtechSNDhcpAddressBindEnable_Type=TruthValue
_QtechSNDhcpAddressBindEnable_Object=MibTableColumn
qtechSNDhcpAddressBindEnable=_QtechSNDhcpAddressBindEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,3,1,2),_QtechSNDhcpAddressBindEnable_Type())
qtechSNDhcpAddressBindEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNDhcpAddressBindEnable.setStatus(_A)
_QtechDhcpSnpFalsePktStatisticTable_Object=MibTable
qtechDhcpSnpFalsePktStatisticTable=_QtechDhcpSnpFalsePktStatisticTable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4))
if mibBuilder.loadTexts:qtechDhcpSnpFalsePktStatisticTable.setStatus(_A)
_QtechDhcpSnpFalsePktStatisticEntry_Object=MibTableRow
qtechDhcpSnpFalsePktStatisticEntry=_QtechDhcpSnpFalsePktStatisticEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1))
qtechDhcpSnpFalsePktStatisticEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:qtechDhcpSnpFalsePktStatisticEntry.setStatus(_A)
_QtechDhcpSnpStatisticIfIndex_Type=InterfaceIndex
_QtechDhcpSnpStatisticIfIndex_Object=MibTableColumn
qtechDhcpSnpStatisticIfIndex=_QtechDhcpSnpStatisticIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,1),_QtechDhcpSnpStatisticIfIndex_Type())
qtechDhcpSnpStatisticIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDhcpSnpStatisticIfIndex.setStatus(_A)
_QtechDhcpSnpStatisticVlanIndex_Type=VlanIndex
_QtechDhcpSnpStatisticVlanIndex_Object=MibTableColumn
qtechDhcpSnpStatisticVlanIndex=_QtechDhcpSnpStatisticVlanIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,2),_QtechDhcpSnpStatisticVlanIndex_Type())
qtechDhcpSnpStatisticVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDhcpSnpStatisticVlanIndex.setStatus(_A)
class _QtechDhcpSnpStatisticIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDhcpSnpStatisticIfDescr_Type.__name__=_I
_QtechDhcpSnpStatisticIfDescr_Object=MibTableColumn
qtechDhcpSnpStatisticIfDescr=_QtechDhcpSnpStatisticIfDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,3),_QtechDhcpSnpStatisticIfDescr_Type())
qtechDhcpSnpStatisticIfDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpSnpStatisticIfDescr.setStatus(_A)
_QtechDhcpSnpStatisticVlanId_Type=VlanIndex
_QtechDhcpSnpStatisticVlanId_Object=MibTableColumn
qtechDhcpSnpStatisticVlanId=_QtechDhcpSnpStatisticVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,4),_QtechDhcpSnpStatisticVlanId_Type())
qtechDhcpSnpStatisticVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpSnpStatisticVlanId.setStatus(_A)
_QtechChaddrNomatchSrcMacDhcpPktNum_Type=Counter32
_QtechChaddrNomatchSrcMacDhcpPktNum_Object=MibTableColumn
qtechChaddrNomatchSrcMacDhcpPktNum=_QtechChaddrNomatchSrcMacDhcpPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,5),_QtechChaddrNomatchSrcMacDhcpPktNum_Type())
qtechChaddrNomatchSrcMacDhcpPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechChaddrNomatchSrcMacDhcpPktNum.setStatus(_A)
_QtechArpNomatchSnpBindTblPktNum_Type=Counter32
_QtechArpNomatchSnpBindTblPktNum_Object=MibTableColumn
qtechArpNomatchSnpBindTblPktNum=_QtechArpNomatchSnpBindTblPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,6),_QtechArpNomatchSnpBindTblPktNum_Type())
qtechArpNomatchSnpBindTblPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpNomatchSnpBindTblPktNum.setStatus(_A)
_QtechIpNomatchSnpBindTblPktNum_Type=Counter32
_QtechIpNomatchSnpBindTblPktNum_Object=MibTableColumn
qtechIpNomatchSnpBindTblPktNum=_QtechIpNomatchSnpBindTblPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,7),_QtechIpNomatchSnpBindTblPktNum_Type())
qtechIpNomatchSnpBindTblPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpNomatchSnpBindTblPktNum.setStatus(_A)
_QtechNomatchSnpBindTblDhcpPktNum_Type=Counter32
_QtechNomatchSnpBindTblDhcpPktNum_Object=MibTableColumn
qtechNomatchSnpBindTblDhcpPktNum=_QtechNomatchSnpBindTblDhcpPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,8),_QtechNomatchSnpBindTblDhcpPktNum_Type())
qtechNomatchSnpBindTblDhcpPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNomatchSnpBindTblDhcpPktNum.setStatus(_A)
_QtechUntrustedReplyPktNum_Type=Counter32
_QtechUntrustedReplyPktNum_Object=MibTableColumn
qtechUntrustedReplyPktNum=_QtechUntrustedReplyPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,9),_QtechUntrustedReplyPktNum_Type())
qtechUntrustedReplyPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechUntrustedReplyPktNum.setStatus(_A)
_QtechDhcpPktIfRateDiscardNum_Type=Counter32
_QtechDhcpPktIfRateDiscardNum_Object=MibTableColumn
qtechDhcpPktIfRateDiscardNum=_QtechDhcpPktIfRateDiscardNum_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,2,4,1,10),_QtechDhcpPktIfRateDiscardNum_Type())
qtechDhcpPktIfRateDiscardNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpPktIfRateDiscardNum.setStatus(_A)
_QtechSNDhcpBindings_ObjectIdentity=ObjectIdentity
qtechSNDhcpBindings=_QtechSNDhcpBindings_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,1,3))
_QtechSNDhcpBindingsTable_Object=MibTable
qtechSNDhcpBindingsTable=_QtechSNDhcpBindingsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1))
if mibBuilder.loadTexts:qtechSNDhcpBindingsTable.setStatus(_A)
_QtechSNDhcpBindingsEntry_Object=MibTableRow
qtechSNDhcpBindingsEntry=_QtechSNDhcpBindingsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1))
qtechSNDhcpBindingsEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:qtechSNDhcpBindingsEntry.setStatus(_A)
_QtechSNDhcpBindingsVlan_Type=VlanIndex
_QtechSNDhcpBindingsVlan_Object=MibTableColumn
qtechSNDhcpBindingsVlan=_QtechSNDhcpBindingsVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1,1),_QtechSNDhcpBindingsVlan_Type())
qtechSNDhcpBindingsVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNDhcpBindingsVlan.setStatus(_A)
_QtechSNDhcpBindingsMacAddress_Type=MacAddress
_QtechSNDhcpBindingsMacAddress_Object=MibTableColumn
qtechSNDhcpBindingsMacAddress=_QtechSNDhcpBindingsMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1,2),_QtechSNDhcpBindingsMacAddress_Type())
qtechSNDhcpBindingsMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNDhcpBindingsMacAddress.setStatus(_A)
class _QtechSNDhcpBindingsAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_QtechSNDhcpBindingsAddrType_Type.__name__=_H
_QtechSNDhcpBindingsAddrType_Object=MibTableColumn
qtechSNDhcpBindingsAddrType=_QtechSNDhcpBindingsAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1,3),_QtechSNDhcpBindingsAddrType_Type())
qtechSNDhcpBindingsAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNDhcpBindingsAddrType.setStatus(_A)
_QtechSNDhcpBindingsIpAddress_Type=IpAddress
_QtechSNDhcpBindingsIpAddress_Object=MibTableColumn
qtechSNDhcpBindingsIpAddress=_QtechSNDhcpBindingsIpAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1,4),_QtechSNDhcpBindingsIpAddress_Type())
qtechSNDhcpBindingsIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechSNDhcpBindingsIpAddress.setStatus(_A)
_QtechSNDhcpBindingsInterface_Type=InterfaceIndex
_QtechSNDhcpBindingsInterface_Object=MibTableColumn
qtechSNDhcpBindingsInterface=_QtechSNDhcpBindingsInterface_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1,5),_QtechSNDhcpBindingsInterface_Type())
qtechSNDhcpBindingsInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechSNDhcpBindingsInterface.setStatus(_A)
_QtechSNDhcpBindingsLeasedTime_Type=Unsigned32
_QtechSNDhcpBindingsLeasedTime_Object=MibTableColumn
qtechSNDhcpBindingsLeasedTime=_QtechSNDhcpBindingsLeasedTime_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1,6),_QtechSNDhcpBindingsLeasedTime_Type())
qtechSNDhcpBindingsLeasedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSNDhcpBindingsLeasedTime.setStatus(_A)
if mibBuilder.loadTexts:qtechSNDhcpBindingsLeasedTime.setUnits(_J)
_QtechSNDhcpBindingsStatus_Type=RowStatus
_QtechSNDhcpBindingsStatus_Object=MibTableColumn
qtechSNDhcpBindingsStatus=_QtechSNDhcpBindingsStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,3,1,1,7),_QtechSNDhcpBindingsStatus_Type())
qtechSNDhcpBindingsStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechSNDhcpBindingsStatus.setStatus(_A)
_QtechDhcpTrapMacAddress_Type=MacAddress
_QtechDhcpTrapMacAddress_Object=MibScalar
qtechDhcpTrapMacAddress=_QtechDhcpTrapMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,42,1,4),_QtechDhcpTrapMacAddress_Type())
qtechDhcpTrapMacAddress.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:qtechDhcpTrapMacAddress.setStatus(_A)
_QtechDhcpSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
qtechDhcpSnoopingMIBConformance=_QtechDhcpSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,2))
_QtechDhcpSnoopingMIBCompliances_ObjectIdentity=ObjectIdentity
qtechDhcpSnoopingMIBCompliances=_QtechDhcpSnoopingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,2,1))
_QtechDhcpSnoopingMIBGroups_ObjectIdentity=ObjectIdentity
qtechDhcpSnoopingMIBGroups=_QtechDhcpSnoopingMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,42,2,2))
qtechDhcpSnoopingMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,42,2,2,1))
qtechDhcpSnoopingMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_G)))
if mibBuilder.loadTexts:qtechDhcpSnoopingMIBGroup.setStatus(_A)
qtechDhcpSnoopingNoResponseTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,42,0,1))
qtechDhcpSnoopingNoResponseTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:qtechDhcpSnoopingNoResponseTrap.setStatus(_A)
qtechDhcpSnoopingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,42,2,1,1))
qtechDhcpSnoopingMIBCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:qtechDhcpSnoopingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechDhcpSnoopingMIB':qtechDhcpSnoopingMIB,'qtechDhcpSnoopingMIBTraps':qtechDhcpSnoopingMIBTraps,'qtechDhcpSnoopingNoResponseTrap':qtechDhcpSnoopingNoResponseTrap,'qtechDhcpSnoopingMIBObjects':qtechDhcpSnoopingMIBObjects,'qtechSNDhcpGlobal':qtechSNDhcpGlobal,_S:qtechSNDhcpFeatureEnable,_T:qtechSNDhcpDatabaseUpdateInterval,_U:qtechSNDhcpRelayAgentInfoOptEnable,_V:qtechSNDhcpMatchMacAddressEnable,'qtechSNDhcpInterface':qtechSNDhcpInterface,'qtechSNDhcpIfTrustTable':qtechSNDhcpIfTrustTable,'qtechSNDhcpIfTrustEntry':qtechSNDhcpIfTrustEntry,_K:qtechSNDhcpIfTrustIndex,_W:qtechSNDhcpIfTrustEnable,'qtechSNDhcpIfSuppressionTable':qtechSNDhcpIfSuppressionTable,'qtechSNDhcpIfSuppressionEntry':qtechSNDhcpIfSuppressionEntry,_L:qtechSNDhcpIfSuppressionIndex,_X:qtechSNDhcpIfSuppressionEnable,'qtechSNDhcpAddressBindTable':qtechSNDhcpAddressBindTable,'qtechSNDhcpAddressBindEntry':qtechSNDhcpAddressBindEntry,_M:qtechSNDhcpAddressBindIndex,_Y:qtechSNDhcpAddressBindEnable,'qtechDhcpSnpFalsePktStatisticTable':qtechDhcpSnpFalsePktStatisticTable,'qtechDhcpSnpFalsePktStatisticEntry':qtechDhcpSnpFalsePktStatisticEntry,_N:qtechDhcpSnpStatisticIfIndex,_O:qtechDhcpSnpStatisticVlanIndex,_Z:qtechDhcpSnpStatisticIfDescr,_a:qtechDhcpSnpStatisticVlanId,_b:qtechChaddrNomatchSrcMacDhcpPktNum,_c:qtechArpNomatchSnpBindTblPktNum,_d:qtechIpNomatchSnpBindTblPktNum,_e:qtechNomatchSnpBindTblDhcpPktNum,_f:qtechUntrustedReplyPktNum,_g:qtechDhcpPktIfRateDiscardNum,'qtechSNDhcpBindings':qtechSNDhcpBindings,'qtechSNDhcpBindingsTable':qtechSNDhcpBindingsTable,'qtechSNDhcpBindingsEntry':qtechSNDhcpBindingsEntry,_P:qtechSNDhcpBindingsVlan,_Q:qtechSNDhcpBindingsMacAddress,_R:qtechSNDhcpBindingsAddrType,_h:qtechSNDhcpBindingsIpAddress,_i:qtechSNDhcpBindingsInterface,_j:qtechSNDhcpBindingsLeasedTime,_k:qtechSNDhcpBindingsStatus,_G:qtechDhcpTrapMacAddress,'qtechDhcpSnoopingMIBConformance':qtechDhcpSnoopingMIBConformance,'qtechDhcpSnoopingMIBCompliances':qtechDhcpSnoopingMIBCompliances,'qtechDhcpSnoopingMIBCompliance':qtechDhcpSnoopingMIBCompliance,'qtechDhcpSnoopingMIBGroups':qtechDhcpSnoopingMIBGroups,_l:qtechDhcpSnoopingMIBGroup})