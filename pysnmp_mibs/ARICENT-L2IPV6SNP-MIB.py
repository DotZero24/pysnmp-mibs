_S='fsIpv6SnpRagSrcIPv6EntryNo'
_R='fsIpv6SnpRagSrcIPv6ListNo'
_Q='forward'
_P='fsIpv6SnpRagPortNumber'
_O='fsIpv6SnpRagPrefixListEntryNo'
_N='fsIpv6SnpRagPrefixListNo'
_M='fsIpv6SnpRagAclEntryNo'
_L='fsIpv6SnpRagAclNo'
_K='fsIpv6SnpRagPolicyId'
_J='enable'
_I='disable'
_H='fsIpv6SnpContexId'
_G='none'
_F='read-create'
_E='not-accessible'
_D='ARICENT-L2IPV6SNP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsIpv6Snp=ModuleIdentity((1,3,6,1,4,1,29601,2,122))
if mibBuilder.loadTexts:fsIpv6Snp.setRevisions(('2018-06-18 00:00',))
class VlanList(TextualConvention,OctetString):status=_A
class Ipv6AddressPrefix(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsIpv6SnpSystem_ObjectIdentity=ObjectIdentity
fsIpv6SnpSystem=_FsIpv6SnpSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,122,1))
_FsIpv6SnpSystemTable_Object=MibTable
fsIpv6SnpSystemTable=_FsIpv6SnpSystemTable_Object((1,3,6,1,4,1,29601,2,122,1,1))
if mibBuilder.loadTexts:fsIpv6SnpSystemTable.setStatus(_A)
_FsIpv6SnpSystemEntry_Object=MibTableRow
fsIpv6SnpSystemEntry=_FsIpv6SnpSystemEntry_Object((1,3,6,1,4,1,29601,2,122,1,1,1))
fsIpv6SnpSystemEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fsIpv6SnpSystemEntry.setStatus(_A)
class _FsIpv6SnpContexId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIpv6SnpContexId_Type.__name__=_B
_FsIpv6SnpContexId_Object=MibTableColumn
fsIpv6SnpContexId=_FsIpv6SnpContexId_Object((1,3,6,1,4,1,29601,2,122,1,1,1,1),_FsIpv6SnpContexId_Type())
fsIpv6SnpContexId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpContexId.setStatus(_A)
class _FsIpv6SnpSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsIpv6SnpSystemControl_Type.__name__=_B
_FsIpv6SnpSystemControl_Object=MibTableColumn
fsIpv6SnpSystemControl=_FsIpv6SnpSystemControl_Object((1,3,6,1,4,1,29601,2,122,1,1,1,2),_FsIpv6SnpSystemControl_Type())
fsIpv6SnpSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpSystemControl.setStatus(_A)
class _FsIpv6SnpRagStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_FsIpv6SnpRagStatus_Type.__name__=_B
_FsIpv6SnpRagStatus_Object=MibTableColumn
fsIpv6SnpRagStatus=_FsIpv6SnpRagStatus_Object((1,3,6,1,4,1,29601,2,122,1,1,1,3),_FsIpv6SnpRagStatus_Type())
fsIpv6SnpRagStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagStatus.setStatus(_A)
class _FsIpv6SnpTraceLevel_Type(Integer32):defaultValue=4
_FsIpv6SnpTraceLevel_Type.__name__=_B
_FsIpv6SnpTraceLevel_Object=MibTableColumn
fsIpv6SnpTraceLevel=_FsIpv6SnpTraceLevel_Object((1,3,6,1,4,1,29601,2,122,1,1,1,4),_FsIpv6SnpTraceLevel_Type())
fsIpv6SnpTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpTraceLevel.setStatus(_A)
_FsIpv6SnpRagPolicy_ObjectIdentity=ObjectIdentity
fsIpv6SnpRagPolicy=_FsIpv6SnpRagPolicy_ObjectIdentity((1,3,6,1,4,1,29601,2,122,2))
_FsIpv6SnpRagPolicyTable_Object=MibTable
fsIpv6SnpRagPolicyTable=_FsIpv6SnpRagPolicyTable_Object((1,3,6,1,4,1,29601,2,122,2,1))
if mibBuilder.loadTexts:fsIpv6SnpRagPolicyTable.setStatus(_A)
_FsIpv6SnpRagPolicyEntry_Object=MibTableRow
fsIpv6SnpRagPolicyEntry=_FsIpv6SnpRagPolicyEntry_Object((1,3,6,1,4,1,29601,2,122,2,1,1))
fsIpv6SnpRagPolicyEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:fsIpv6SnpRagPolicyEntry.setStatus(_A)
class _FsIpv6SnpRagPolicyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsIpv6SnpRagPolicyId_Type.__name__=_B
_FsIpv6SnpRagPolicyId_Object=MibTableColumn
fsIpv6SnpRagPolicyId=_FsIpv6SnpRagPolicyId_Object((1,3,6,1,4,1,29601,2,122,2,1,1,1),_FsIpv6SnpRagPolicyId_Type())
fsIpv6SnpRagPolicyId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagPolicyId.setStatus(_A)
class _FsIpv6SnpRagDeviceRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('host',1),('router',2)))
_FsIpv6SnpRagDeviceRole_Type.__name__=_B
_FsIpv6SnpRagDeviceRole_Object=MibTableColumn
fsIpv6SnpRagDeviceRole=_FsIpv6SnpRagDeviceRole_Object((1,3,6,1,4,1,29601,2,122,2,1,1,2),_FsIpv6SnpRagDeviceRole_Type())
fsIpv6SnpRagDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagDeviceRole.setStatus(_A)
class _FsIpv6SnpRagMbit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),(_G,2)))
_FsIpv6SnpRagMbit_Type.__name__=_B
_FsIpv6SnpRagMbit_Object=MibTableColumn
fsIpv6SnpRagMbit=_FsIpv6SnpRagMbit_Object((1,3,6,1,4,1,29601,2,122,2,1,1,3),_FsIpv6SnpRagMbit_Type())
fsIpv6SnpRagMbit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagMbit.setStatus(_A)
class _FsIpv6SnpRagObit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),(_G,2)))
_FsIpv6SnpRagObit_Type.__name__=_B
_FsIpv6SnpRagObit_Object=MibTableColumn
fsIpv6SnpRagObit=_FsIpv6SnpRagObit_Object((1,3,6,1,4,1,29601,2,122,2,1,1,4),_FsIpv6SnpRagObit_Type())
fsIpv6SnpRagObit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagObit.setStatus(_A)
class _FsIpv6SnpMatchRagAclId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIpv6SnpMatchRagAclId_Type.__name__=_B
_FsIpv6SnpMatchRagAclId_Object=MibTableColumn
fsIpv6SnpMatchRagAclId=_FsIpv6SnpMatchRagAclId_Object((1,3,6,1,4,1,29601,2,122,2,1,1,5),_FsIpv6SnpMatchRagAclId_Type())
fsIpv6SnpMatchRagAclId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpMatchRagAclId.setStatus(_A)
class _FsIpv6SnpMatchRagPrefixListId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIpv6SnpMatchRagPrefixListId_Type.__name__=_B
_FsIpv6SnpMatchRagPrefixListId_Object=MibTableColumn
fsIpv6SnpMatchRagPrefixListId=_FsIpv6SnpMatchRagPrefixListId_Object((1,3,6,1,4,1,29601,2,122,2,1,1,6),_FsIpv6SnpMatchRagPrefixListId_Type())
fsIpv6SnpMatchRagPrefixListId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpMatchRagPrefixListId.setStatus(_A)
class _FsIpv6SnpMatchRagSrcIp6ListId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIpv6SnpMatchRagSrcIp6ListId_Type.__name__=_B
_FsIpv6SnpMatchRagSrcIp6ListId_Object=MibTableColumn
fsIpv6SnpMatchRagSrcIp6ListId=_FsIpv6SnpMatchRagSrcIp6ListId_Object((1,3,6,1,4,1,29601,2,122,2,1,1,7),_FsIpv6SnpMatchRagSrcIp6ListId_Type())
fsIpv6SnpMatchRagSrcIp6ListId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpMatchRagSrcIp6ListId.setStatus(_A)
class _FsIpv6SnpRagHopLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsIpv6SnpRagHopLimit_Type.__name__=_B
_FsIpv6SnpRagHopLimit_Object=MibTableColumn
fsIpv6SnpRagHopLimit=_FsIpv6SnpRagHopLimit_Object((1,3,6,1,4,1,29601,2,122,2,1,1,8),_FsIpv6SnpRagHopLimit_Type())
fsIpv6SnpRagHopLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagHopLimit.setStatus(_A)
class _FsIpv6SnpRagRouterPreference_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('medium',0),('high',1),(_G,2),('low',3)))
_FsIpv6SnpRagRouterPreference_Type.__name__=_B
_FsIpv6SnpRagRouterPreference_Object=MibTableColumn
fsIpv6SnpRagRouterPreference=_FsIpv6SnpRagRouterPreference_Object((1,3,6,1,4,1,29601,2,122,2,1,1,9),_FsIpv6SnpRagRouterPreference_Type())
fsIpv6SnpRagRouterPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagRouterPreference.setStatus(_A)
_FsIpv6SnpRagPolicyRowStatus_Type=RowStatus
_FsIpv6SnpRagPolicyRowStatus_Object=MibTableColumn
fsIpv6SnpRagPolicyRowStatus=_FsIpv6SnpRagPolicyRowStatus_Object((1,3,6,1,4,1,29601,2,122,2,1,1,10),_FsIpv6SnpRagPolicyRowStatus_Type())
fsIpv6SnpRagPolicyRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpv6SnpRagPolicyRowStatus.setStatus(_A)
_FsIpv6SnpRagACLTable_Object=MibTable
fsIpv6SnpRagACLTable=_FsIpv6SnpRagACLTable_Object((1,3,6,1,4,1,29601,2,122,2,2))
if mibBuilder.loadTexts:fsIpv6SnpRagACLTable.setStatus(_A)
_FsIpv6SnpRagAclEntry_Object=MibTableRow
fsIpv6SnpRagAclEntry=_FsIpv6SnpRagAclEntry_Object((1,3,6,1,4,1,29601,2,122,2,2,1))
fsIpv6SnpRagAclEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:fsIpv6SnpRagAclEntry.setStatus(_A)
class _FsIpv6SnpRagAclNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsIpv6SnpRagAclNo_Type.__name__=_B
_FsIpv6SnpRagAclNo_Object=MibTableColumn
fsIpv6SnpRagAclNo=_FsIpv6SnpRagAclNo_Object((1,3,6,1,4,1,29601,2,122,2,2,1,1),_FsIpv6SnpRagAclNo_Type())
fsIpv6SnpRagAclNo.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagAclNo.setStatus(_A)
class _FsIpv6SnpRagAclEntryNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsIpv6SnpRagAclEntryNo_Type.__name__=_B
_FsIpv6SnpRagAclEntryNo_Object=MibTableColumn
fsIpv6SnpRagAclEntryNo=_FsIpv6SnpRagAclEntryNo_Object((1,3,6,1,4,1,29601,2,122,2,2,1,2),_FsIpv6SnpRagAclEntryNo_Type())
fsIpv6SnpRagAclEntryNo.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagAclEntryNo.setStatus(_A)
_FsIpv6SnpRagAclSrcMacAddress_Type=MacAddress
_FsIpv6SnpRagAclSrcMacAddress_Object=MibTableColumn
fsIpv6SnpRagAclSrcMacAddress=_FsIpv6SnpRagAclSrcMacAddress_Object((1,3,6,1,4,1,29601,2,122,2,2,1,3),_FsIpv6SnpRagAclSrcMacAddress_Type())
fsIpv6SnpRagAclSrcMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagAclSrcMacAddress.setStatus(_A)
_FsIpv6SnpRagAclRowStatus_Type=RowStatus
_FsIpv6SnpRagAclRowStatus_Object=MibTableColumn
fsIpv6SnpRagAclRowStatus=_FsIpv6SnpRagAclRowStatus_Object((1,3,6,1,4,1,29601,2,122,2,2,1,4),_FsIpv6SnpRagAclRowStatus_Type())
fsIpv6SnpRagAclRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpv6SnpRagAclRowStatus.setStatus(_A)
_Fsipv6SnpRagPrefixListTable_Object=MibTable
fsipv6SnpRagPrefixListTable=_Fsipv6SnpRagPrefixListTable_Object((1,3,6,1,4,1,29601,2,122,2,3))
if mibBuilder.loadTexts:fsipv6SnpRagPrefixListTable.setStatus(_A)
_FsIpv6SnpRagPrefixListEntry_Object=MibTableRow
fsIpv6SnpRagPrefixListEntry=_FsIpv6SnpRagPrefixListEntry_Object((1,3,6,1,4,1,29601,2,122,2,3,1))
fsIpv6SnpRagPrefixListEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListEntry.setStatus(_A)
class _FsIpv6SnpRagPrefixListNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsIpv6SnpRagPrefixListNo_Type.__name__=_B
_FsIpv6SnpRagPrefixListNo_Object=MibTableColumn
fsIpv6SnpRagPrefixListNo=_FsIpv6SnpRagPrefixListNo_Object((1,3,6,1,4,1,29601,2,122,2,3,1,1),_FsIpv6SnpRagPrefixListNo_Type())
fsIpv6SnpRagPrefixListNo.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListNo.setStatus(_A)
class _FsIpv6SnpRagPrefixListEntryNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsIpv6SnpRagPrefixListEntryNo_Type.__name__=_B
_FsIpv6SnpRagPrefixListEntryNo_Object=MibTableColumn
fsIpv6SnpRagPrefixListEntryNo=_FsIpv6SnpRagPrefixListEntryNo_Object((1,3,6,1,4,1,29601,2,122,2,3,1,2),_FsIpv6SnpRagPrefixListEntryNo_Type())
fsIpv6SnpRagPrefixListEntryNo.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListEntryNo.setStatus(_A)
_FsIpv6SnpRagPrefixListPrefix_Type=Ipv6AddressPrefix
_FsIpv6SnpRagPrefixListPrefix_Object=MibTableColumn
fsIpv6SnpRagPrefixListPrefix=_FsIpv6SnpRagPrefixListPrefix_Object((1,3,6,1,4,1,29601,2,122,2,3,1,3),_FsIpv6SnpRagPrefixListPrefix_Type())
fsIpv6SnpRagPrefixListPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListPrefix.setStatus(_A)
class _FsIpv6SnpRagPrefixListLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FsIpv6SnpRagPrefixListLength_Type.__name__=_B
_FsIpv6SnpRagPrefixListLength_Object=MibTableColumn
fsIpv6SnpRagPrefixListLength=_FsIpv6SnpRagPrefixListLength_Object((1,3,6,1,4,1,29601,2,122,2,3,1,4),_FsIpv6SnpRagPrefixListLength_Type())
fsIpv6SnpRagPrefixListLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListLength.setStatus(_A)
class _FsIpv6SnpRagPrefixListGe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsIpv6SnpRagPrefixListGe_Type.__name__=_B
_FsIpv6SnpRagPrefixListGe_Object=MibTableColumn
fsIpv6SnpRagPrefixListGe=_FsIpv6SnpRagPrefixListGe_Object((1,3,6,1,4,1,29601,2,122,2,3,1,5),_FsIpv6SnpRagPrefixListGe_Type())
fsIpv6SnpRagPrefixListGe.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListGe.setStatus(_A)
class _FsIpv6SnpRagPrefixListLe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsIpv6SnpRagPrefixListLe_Type.__name__=_B
_FsIpv6SnpRagPrefixListLe_Object=MibTableColumn
fsIpv6SnpRagPrefixListLe=_FsIpv6SnpRagPrefixListLe_Object((1,3,6,1,4,1,29601,2,122,2,3,1,6),_FsIpv6SnpRagPrefixListLe_Type())
fsIpv6SnpRagPrefixListLe.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListLe.setStatus(_A)
_FsIpv6SnpRagPrefixListRowStatus_Type=RowStatus
_FsIpv6SnpRagPrefixListRowStatus_Object=MibTableColumn
fsIpv6SnpRagPrefixListRowStatus=_FsIpv6SnpRagPrefixListRowStatus_Object((1,3,6,1,4,1,29601,2,122,2,3,1,7),_FsIpv6SnpRagPrefixListRowStatus_Type())
fsIpv6SnpRagPrefixListRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpv6SnpRagPrefixListRowStatus.setStatus(_A)
_FsIpv6SnpRagPortTable_Object=MibTable
fsIpv6SnpRagPortTable=_FsIpv6SnpRagPortTable_Object((1,3,6,1,4,1,29601,2,122,2,4))
if mibBuilder.loadTexts:fsIpv6SnpRagPortTable.setStatus(_A)
_FsIpv6SnpRagPortEntry_Object=MibTableRow
fsIpv6SnpRagPortEntry=_FsIpv6SnpRagPortEntry_Object((1,3,6,1,4,1,29601,2,122,2,4,1))
fsIpv6SnpRagPortEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:fsIpv6SnpRagPortEntry.setStatus(_A)
_FsIpv6SnpRagPortNumber_Type=InterfaceIndex
_FsIpv6SnpRagPortNumber_Object=MibTableColumn
fsIpv6SnpRagPortNumber=_FsIpv6SnpRagPortNumber_Object((1,3,6,1,4,1,29601,2,122,2,4,1,1),_FsIpv6SnpRagPortNumber_Type())
fsIpv6SnpRagPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagPortNumber.setStatus(_A)
class _FsIpv6SnpRagPortStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_FsIpv6SnpRagPortStatus_Type.__name__=_B
_FsIpv6SnpRagPortStatus_Object=MibTableColumn
fsIpv6SnpRagPortStatus=_FsIpv6SnpRagPortStatus_Object((1,3,6,1,4,1,29601,2,122,2,4,1,2),_FsIpv6SnpRagPortStatus_Type())
fsIpv6SnpRagPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPortStatus.setStatus(_A)
class _FsIpv6SnpRagPortPolicyId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIpv6SnpRagPortPolicyId_Type.__name__=_B
_FsIpv6SnpRagPortPolicyId_Object=MibTableColumn
fsIpv6SnpRagPortPolicyId=_FsIpv6SnpRagPortPolicyId_Object((1,3,6,1,4,1,29601,2,122,2,4,1,3),_FsIpv6SnpRagPortPolicyId_Type())
fsIpv6SnpRagPortPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPortPolicyId.setStatus(_A)
class _FsIpv6SnpRagPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stateless',1),('stateful',2)))
_FsIpv6SnpRagPortMode_Type.__name__=_B
_FsIpv6SnpRagPortMode_Object=MibTableColumn
fsIpv6SnpRagPortMode=_FsIpv6SnpRagPortMode_Object((1,3,6,1,4,1,29601,2,122,2,4,1,4),_FsIpv6SnpRagPortMode_Type())
fsIpv6SnpRagPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPortMode.setStatus(_A)
class _FsIpv6SnpRagPortCurrentState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('na',0),('learn',1),(_Q,2),('block',3)))
_FsIpv6SnpRagPortCurrentState_Type.__name__=_B
_FsIpv6SnpRagPortCurrentState_Object=MibTableColumn
fsIpv6SnpRagPortCurrentState=_FsIpv6SnpRagPortCurrentState_Object((1,3,6,1,4,1,29601,2,122,2,4,1,5),_FsIpv6SnpRagPortCurrentState_Type())
fsIpv6SnpRagPortCurrentState.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsIpv6SnpRagPortCurrentState.setStatus(_A)
class _FsIpv6SnpRagPortTriggerStateChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('learn',1),(_Q,2),('block',3)))
_FsIpv6SnpRagPortTriggerStateChange_Type.__name__=_B
_FsIpv6SnpRagPortTriggerStateChange_Object=MibTableColumn
fsIpv6SnpRagPortTriggerStateChange=_FsIpv6SnpRagPortTriggerStateChange_Object((1,3,6,1,4,1,29601,2,122,2,4,1,6),_FsIpv6SnpRagPortTriggerStateChange_Type())
fsIpv6SnpRagPortTriggerStateChange.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPortTriggerStateChange.setStatus(_A)
class _FsIpv6SnpRagPortLearnTime_Type(Integer32):defaultValue=240;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,900))
_FsIpv6SnpRagPortLearnTime_Type.__name__=_B
_FsIpv6SnpRagPortLearnTime_Object=MibTableColumn
fsIpv6SnpRagPortLearnTime=_FsIpv6SnpRagPortLearnTime_Object((1,3,6,1,4,1,29601,2,122,2,4,1,7),_FsIpv6SnpRagPortLearnTime_Type())
fsIpv6SnpRagPortLearnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPortLearnTime.setStatus(_A)
if mibBuilder.loadTexts:fsIpv6SnpRagPortLearnTime.setUnits('seconds')
class _FsIpv6SnpRagPortTrustState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trusted',1),('untrusted',2)))
_FsIpv6SnpRagPortTrustState_Type.__name__=_B
_FsIpv6SnpRagPortTrustState_Object=MibTableColumn
fsIpv6SnpRagPortTrustState=_FsIpv6SnpRagPortTrustState_Object((1,3,6,1,4,1,29601,2,122,2,4,1,8),_FsIpv6SnpRagPortTrustState_Type())
fsIpv6SnpRagPortTrustState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPortTrustState.setStatus(_A)
_FsIpv6SnpRagPortVlanlist_Type=VlanList
_FsIpv6SnpRagPortVlanlist_Object=MibTableColumn
fsIpv6SnpRagPortVlanlist=_FsIpv6SnpRagPortVlanlist_Object((1,3,6,1,4,1,29601,2,122,2,4,1,9),_FsIpv6SnpRagPortVlanlist_Type())
fsIpv6SnpRagPortVlanlist.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagPortVlanlist.setStatus(_A)
_FsIpv6SnpRagPortRowStatus_Type=RowStatus
_FsIpv6SnpRagPortRowStatus_Object=MibTableColumn
fsIpv6SnpRagPortRowStatus=_FsIpv6SnpRagPortRowStatus_Object((1,3,6,1,4,1,29601,2,122,2,4,1,10),_FsIpv6SnpRagPortRowStatus_Type())
fsIpv6SnpRagPortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpv6SnpRagPortRowStatus.setStatus(_A)
_FsIPv6SnpRagSrcIPv6ListTable_Object=MibTable
fsIPv6SnpRagSrcIPv6ListTable=_FsIPv6SnpRagSrcIPv6ListTable_Object((1,3,6,1,4,1,29601,2,122,2,5))
if mibBuilder.loadTexts:fsIPv6SnpRagSrcIPv6ListTable.setStatus(_A)
_FsIpv6SnpRagSrcIPv6ListEntry_Object=MibTableRow
fsIpv6SnpRagSrcIPv6ListEntry=_FsIpv6SnpRagSrcIPv6ListEntry_Object((1,3,6,1,4,1,29601,2,122,2,5,1))
fsIpv6SnpRagSrcIPv6ListEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:fsIpv6SnpRagSrcIPv6ListEntry.setStatus(_A)
class _FsIpv6SnpRagSrcIPv6ListNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsIpv6SnpRagSrcIPv6ListNo_Type.__name__=_B
_FsIpv6SnpRagSrcIPv6ListNo_Object=MibTableColumn
fsIpv6SnpRagSrcIPv6ListNo=_FsIpv6SnpRagSrcIPv6ListNo_Object((1,3,6,1,4,1,29601,2,122,2,5,1,1),_FsIpv6SnpRagSrcIPv6ListNo_Type())
fsIpv6SnpRagSrcIPv6ListNo.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagSrcIPv6ListNo.setStatus(_A)
class _FsIpv6SnpRagSrcIPv6EntryNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsIpv6SnpRagSrcIPv6EntryNo_Type.__name__=_B
_FsIpv6SnpRagSrcIPv6EntryNo_Object=MibTableColumn
fsIpv6SnpRagSrcIPv6EntryNo=_FsIpv6SnpRagSrcIPv6EntryNo_Object((1,3,6,1,4,1,29601,2,122,2,5,1,2),_FsIpv6SnpRagSrcIPv6EntryNo_Type())
fsIpv6SnpRagSrcIPv6EntryNo.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpv6SnpRagSrcIPv6EntryNo.setStatus(_A)
_FsIpv6SnpRagSrcIPv6Addr_Type=Ipv6AddressPrefix
_FsIpv6SnpRagSrcIPv6Addr_Object=MibTableColumn
fsIpv6SnpRagSrcIPv6Addr=_FsIpv6SnpRagSrcIPv6Addr_Object((1,3,6,1,4,1,29601,2,122,2,5,1,3),_FsIpv6SnpRagSrcIPv6Addr_Type())
fsIpv6SnpRagSrcIPv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagSrcIPv6Addr.setStatus(_A)
class _FsIpv6SnpRagSrcIPv6PrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FsIpv6SnpRagSrcIPv6PrefixLength_Type.__name__=_B
_FsIpv6SnpRagSrcIPv6PrefixLength_Object=MibTableColumn
fsIpv6SnpRagSrcIPv6PrefixLength=_FsIpv6SnpRagSrcIPv6PrefixLength_Object((1,3,6,1,4,1,29601,2,122,2,5,1,4),_FsIpv6SnpRagSrcIPv6PrefixLength_Type())
fsIpv6SnpRagSrcIPv6PrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpv6SnpRagSrcIPv6PrefixLength.setStatus(_A)
_FsIpv6SnpRagSrcIPv6RowStatus_Type=RowStatus
_FsIpv6SnpRagSrcIPv6RowStatus_Object=MibTableColumn
fsIpv6SnpRagSrcIPv6RowStatus=_FsIpv6SnpRagSrcIPv6RowStatus_Object((1,3,6,1,4,1,29601,2,122,2,5,1,5),_FsIpv6SnpRagSrcIPv6RowStatus_Type())
fsIpv6SnpRagSrcIPv6RowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpv6SnpRagSrcIPv6RowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'VlanList':VlanList,'Ipv6AddressPrefix':Ipv6AddressPrefix,'fsIpv6Snp':fsIpv6Snp,'fsIpv6SnpSystem':fsIpv6SnpSystem,'fsIpv6SnpSystemTable':fsIpv6SnpSystemTable,'fsIpv6SnpSystemEntry':fsIpv6SnpSystemEntry,_H:fsIpv6SnpContexId,'fsIpv6SnpSystemControl':fsIpv6SnpSystemControl,'fsIpv6SnpRagStatus':fsIpv6SnpRagStatus,'fsIpv6SnpTraceLevel':fsIpv6SnpTraceLevel,'fsIpv6SnpRagPolicy':fsIpv6SnpRagPolicy,'fsIpv6SnpRagPolicyTable':fsIpv6SnpRagPolicyTable,'fsIpv6SnpRagPolicyEntry':fsIpv6SnpRagPolicyEntry,_K:fsIpv6SnpRagPolicyId,'fsIpv6SnpRagDeviceRole':fsIpv6SnpRagDeviceRole,'fsIpv6SnpRagMbit':fsIpv6SnpRagMbit,'fsIpv6SnpRagObit':fsIpv6SnpRagObit,'fsIpv6SnpMatchRagAclId':fsIpv6SnpMatchRagAclId,'fsIpv6SnpMatchRagPrefixListId':fsIpv6SnpMatchRagPrefixListId,'fsIpv6SnpMatchRagSrcIp6ListId':fsIpv6SnpMatchRagSrcIp6ListId,'fsIpv6SnpRagHopLimit':fsIpv6SnpRagHopLimit,'fsIpv6SnpRagRouterPreference':fsIpv6SnpRagRouterPreference,'fsIpv6SnpRagPolicyRowStatus':fsIpv6SnpRagPolicyRowStatus,'fsIpv6SnpRagACLTable':fsIpv6SnpRagACLTable,'fsIpv6SnpRagAclEntry':fsIpv6SnpRagAclEntry,_L:fsIpv6SnpRagAclNo,_M:fsIpv6SnpRagAclEntryNo,'fsIpv6SnpRagAclSrcMacAddress':fsIpv6SnpRagAclSrcMacAddress,'fsIpv6SnpRagAclRowStatus':fsIpv6SnpRagAclRowStatus,'fsipv6SnpRagPrefixListTable':fsipv6SnpRagPrefixListTable,'fsIpv6SnpRagPrefixListEntry':fsIpv6SnpRagPrefixListEntry,_N:fsIpv6SnpRagPrefixListNo,_O:fsIpv6SnpRagPrefixListEntryNo,'fsIpv6SnpRagPrefixListPrefix':fsIpv6SnpRagPrefixListPrefix,'fsIpv6SnpRagPrefixListLength':fsIpv6SnpRagPrefixListLength,'fsIpv6SnpRagPrefixListGe':fsIpv6SnpRagPrefixListGe,'fsIpv6SnpRagPrefixListLe':fsIpv6SnpRagPrefixListLe,'fsIpv6SnpRagPrefixListRowStatus':fsIpv6SnpRagPrefixListRowStatus,'fsIpv6SnpRagPortTable':fsIpv6SnpRagPortTable,'fsIpv6SnpRagPortEntry':fsIpv6SnpRagPortEntry,_P:fsIpv6SnpRagPortNumber,'fsIpv6SnpRagPortStatus':fsIpv6SnpRagPortStatus,'fsIpv6SnpRagPortPolicyId':fsIpv6SnpRagPortPolicyId,'fsIpv6SnpRagPortMode':fsIpv6SnpRagPortMode,'fsIpv6SnpRagPortCurrentState':fsIpv6SnpRagPortCurrentState,'fsIpv6SnpRagPortTriggerStateChange':fsIpv6SnpRagPortTriggerStateChange,'fsIpv6SnpRagPortLearnTime':fsIpv6SnpRagPortLearnTime,'fsIpv6SnpRagPortTrustState':fsIpv6SnpRagPortTrustState,'fsIpv6SnpRagPortVlanlist':fsIpv6SnpRagPortVlanlist,'fsIpv6SnpRagPortRowStatus':fsIpv6SnpRagPortRowStatus,'fsIPv6SnpRagSrcIPv6ListTable':fsIPv6SnpRagSrcIPv6ListTable,'fsIpv6SnpRagSrcIPv6ListEntry':fsIpv6SnpRagSrcIPv6ListEntry,_R:fsIpv6SnpRagSrcIPv6ListNo,_S:fsIpv6SnpRagSrcIPv6EntryNo,'fsIpv6SnpRagSrcIPv6Addr':fsIpv6SnpRagSrcIPv6Addr,'fsIpv6SnpRagSrcIPv6PrefixLength':fsIpv6SnpRagSrcIPv6PrefixLength,'fsIpv6SnpRagSrcIPv6RowStatus':fsIpv6SnpRagSrcIPv6RowStatus})