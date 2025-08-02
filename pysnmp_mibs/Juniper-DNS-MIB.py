_U='juniDnsLocalDomainNameListGroup'
_T='juniDnsV4V6ServerListGroup'
_S='juniDnsServerListGroup'
_R='juniDnsEnableGroup'
_Q='juniDnsV4V6ServerListAddressType'
_P='juniDnsV4V6ServerListAddress'
_O='juniDnsLocalDomainNameListRowStatus'
_N='juniDnsLocalDomainNameListName'
_M='juniDnsLocalDomainNameListNextIndex'
_L='juniDnsServerListAddress'
_K='juniDnsEnable'
_J='juniDnsLocalDomainNameListIndex'
_I='obsolete'
_H='not-accessible'
_G='juniDnsServerListIndex'
_F='read-only'
_E='juniDnsServerListRowStatus'
_D='juniDnsServerListNextIndex'
_C='read-create'
_B='Juniper-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC','JuniEnable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
juniDnsMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,47))
if mibBuilder.loadTexts:juniDnsMIB.setRevisions(('2006-09-15 08:32','2003-09-11 15:50','2002-09-16 21:44','2001-03-22 19:29'))
class JuniNextServerListIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ServerListIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class JuniNextLocalDomainNameListIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class LocalDomainNameListIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class LocalDomainName(TextualConvention,OctetString):status=_A;displayHint='1025a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1025))
_JuniDnsObjects_ObjectIdentity=ObjectIdentity
juniDnsObjects=_JuniDnsObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,47,1))
_JuniDnsGeneral_ObjectIdentity=ObjectIdentity
juniDnsGeneral=_JuniDnsGeneral_ObjectIdentity((1,3,6,1,4,1,4874,2,2,47,1,1))
_JuniDnsEnable_Type=JuniEnable
_JuniDnsEnable_Object=MibScalar
juniDnsEnable=_JuniDnsEnable_Object((1,3,6,1,4,1,4874,2,2,47,1,1,1),_JuniDnsEnable_Type())
juniDnsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:juniDnsEnable.setStatus(_A)
_JuniDnsServerList_ObjectIdentity=ObjectIdentity
juniDnsServerList=_JuniDnsServerList_ObjectIdentity((1,3,6,1,4,1,4874,2,2,47,1,2))
_JuniDnsServerListNextIndex_Type=JuniNextServerListIndex
_JuniDnsServerListNextIndex_Object=MibScalar
juniDnsServerListNextIndex=_JuniDnsServerListNextIndex_Object((1,3,6,1,4,1,4874,2,2,47,1,2,1),_JuniDnsServerListNextIndex_Type())
juniDnsServerListNextIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDnsServerListNextIndex.setStatus(_A)
_JuniDnsServerListTable_Object=MibTable
juniDnsServerListTable=_JuniDnsServerListTable_Object((1,3,6,1,4,1,4874,2,2,47,1,2,2))
if mibBuilder.loadTexts:juniDnsServerListTable.setStatus(_A)
_JuniDnsServerListEntry_Object=MibTableRow
juniDnsServerListEntry=_JuniDnsServerListEntry_Object((1,3,6,1,4,1,4874,2,2,47,1,2,2,1))
juniDnsServerListEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:juniDnsServerListEntry.setStatus(_A)
_JuniDnsServerListIndex_Type=ServerListIndex
_JuniDnsServerListIndex_Object=MibTableColumn
juniDnsServerListIndex=_JuniDnsServerListIndex_Object((1,3,6,1,4,1,4874,2,2,47,1,2,2,1,1),_JuniDnsServerListIndex_Type())
juniDnsServerListIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDnsServerListIndex.setStatus(_A)
_JuniDnsServerListAddress_Type=IpAddress
_JuniDnsServerListAddress_Object=MibTableColumn
juniDnsServerListAddress=_JuniDnsServerListAddress_Object((1,3,6,1,4,1,4874,2,2,47,1,2,2,1,2),_JuniDnsServerListAddress_Type())
juniDnsServerListAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDnsServerListAddress.setStatus(_I)
_JuniDnsServerListRowStatus_Type=RowStatus
_JuniDnsServerListRowStatus_Object=MibTableColumn
juniDnsServerListRowStatus=_JuniDnsServerListRowStatus_Object((1,3,6,1,4,1,4874,2,2,47,1,2,2,1,3),_JuniDnsServerListRowStatus_Type())
juniDnsServerListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDnsServerListRowStatus.setStatus(_A)
_JuniDnsV4V6ServerListAddressType_Type=InetAddressType
_JuniDnsV4V6ServerListAddressType_Object=MibTableColumn
juniDnsV4V6ServerListAddressType=_JuniDnsV4V6ServerListAddressType_Object((1,3,6,1,4,1,4874,2,2,47,1,2,2,1,4),_JuniDnsV4V6ServerListAddressType_Type())
juniDnsV4V6ServerListAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDnsV4V6ServerListAddressType.setStatus(_A)
_JuniDnsV4V6ServerListAddress_Type=InetAddress
_JuniDnsV4V6ServerListAddress_Object=MibTableColumn
juniDnsV4V6ServerListAddress=_JuniDnsV4V6ServerListAddress_Object((1,3,6,1,4,1,4874,2,2,47,1,2,2,1,5),_JuniDnsV4V6ServerListAddress_Type())
juniDnsV4V6ServerListAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDnsV4V6ServerListAddress.setStatus(_A)
_JuniDnsLocalDomainNameList_ObjectIdentity=ObjectIdentity
juniDnsLocalDomainNameList=_JuniDnsLocalDomainNameList_ObjectIdentity((1,3,6,1,4,1,4874,2,2,47,1,3))
_JuniDnsLocalDomainNameListNextIndex_Type=JuniNextLocalDomainNameListIndex
_JuniDnsLocalDomainNameListNextIndex_Object=MibScalar
juniDnsLocalDomainNameListNextIndex=_JuniDnsLocalDomainNameListNextIndex_Object((1,3,6,1,4,1,4874,2,2,47,1,3,1),_JuniDnsLocalDomainNameListNextIndex_Type())
juniDnsLocalDomainNameListNextIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDnsLocalDomainNameListNextIndex.setStatus(_A)
_JuniDnsLocalDomainNameListTable_Object=MibTable
juniDnsLocalDomainNameListTable=_JuniDnsLocalDomainNameListTable_Object((1,3,6,1,4,1,4874,2,2,47,1,3,2))
if mibBuilder.loadTexts:juniDnsLocalDomainNameListTable.setStatus(_A)
_JuniDnsLocalDomainNameListEntry_Object=MibTableRow
juniDnsLocalDomainNameListEntry=_JuniDnsLocalDomainNameListEntry_Object((1,3,6,1,4,1,4874,2,2,47,1,3,2,1))
juniDnsLocalDomainNameListEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:juniDnsLocalDomainNameListEntry.setStatus(_A)
_JuniDnsLocalDomainNameListIndex_Type=LocalDomainNameListIndex
_JuniDnsLocalDomainNameListIndex_Object=MibTableColumn
juniDnsLocalDomainNameListIndex=_JuniDnsLocalDomainNameListIndex_Object((1,3,6,1,4,1,4874,2,2,47,1,3,2,1,1),_JuniDnsLocalDomainNameListIndex_Type())
juniDnsLocalDomainNameListIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDnsLocalDomainNameListIndex.setStatus(_A)
_JuniDnsLocalDomainNameListName_Type=LocalDomainName
_JuniDnsLocalDomainNameListName_Object=MibTableColumn
juniDnsLocalDomainNameListName=_JuniDnsLocalDomainNameListName_Object((1,3,6,1,4,1,4874,2,2,47,1,3,2,1,2),_JuniDnsLocalDomainNameListName_Type())
juniDnsLocalDomainNameListName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDnsLocalDomainNameListName.setStatus(_A)
_JuniDnsLocalDomainNameListRowStatus_Type=RowStatus
_JuniDnsLocalDomainNameListRowStatus_Object=MibTableColumn
juniDnsLocalDomainNameListRowStatus=_JuniDnsLocalDomainNameListRowStatus_Object((1,3,6,1,4,1,4874,2,2,47,1,3,2,1,3),_JuniDnsLocalDomainNameListRowStatus_Type())
juniDnsLocalDomainNameListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDnsLocalDomainNameListRowStatus.setStatus(_A)
_JuniDnsConformance_ObjectIdentity=ObjectIdentity
juniDnsConformance=_JuniDnsConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,47,2))
_JuniDnsCompliances_ObjectIdentity=ObjectIdentity
juniDnsCompliances=_JuniDnsCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,47,2,1))
_JuniDnsGroups_ObjectIdentity=ObjectIdentity
juniDnsGroups=_JuniDnsGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,47,2,2))
juniDnsEnableGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,47,2,2,1))
juniDnsEnableGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:juniDnsEnableGroup.setStatus(_A)
juniDnsServerListGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,47,2,2,2))
juniDnsServerListGroup.setObjects(*((_B,_D),(_B,_L),(_B,_E)))
if mibBuilder.loadTexts:juniDnsServerListGroup.setStatus(_I)
juniDnsLocalDomainNameListGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,47,2,2,3))
juniDnsLocalDomainNameListGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:juniDnsLocalDomainNameListGroup.setStatus(_A)
juniDnsV4V6ServerListGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,47,2,2,4))
juniDnsV4V6ServerListGroup.setObjects(*((_B,_D),(_B,_E),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:juniDnsV4V6ServerListGroup.setStatus(_A)
juniDnsCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,47,2,1,1))
juniDnsCompliance.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:juniDnsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JuniNextServerListIndex':JuniNextServerListIndex,'ServerListIndex':ServerListIndex,'JuniNextLocalDomainNameListIndex':JuniNextLocalDomainNameListIndex,'LocalDomainNameListIndex':LocalDomainNameListIndex,'LocalDomainName':LocalDomainName,'juniDnsMIB':juniDnsMIB,'juniDnsObjects':juniDnsObjects,'juniDnsGeneral':juniDnsGeneral,_K:juniDnsEnable,'juniDnsServerList':juniDnsServerList,_D:juniDnsServerListNextIndex,'juniDnsServerListTable':juniDnsServerListTable,'juniDnsServerListEntry':juniDnsServerListEntry,_G:juniDnsServerListIndex,_L:juniDnsServerListAddress,_E:juniDnsServerListRowStatus,_Q:juniDnsV4V6ServerListAddressType,_P:juniDnsV4V6ServerListAddress,'juniDnsLocalDomainNameList':juniDnsLocalDomainNameList,_M:juniDnsLocalDomainNameListNextIndex,'juniDnsLocalDomainNameListTable':juniDnsLocalDomainNameListTable,'juniDnsLocalDomainNameListEntry':juniDnsLocalDomainNameListEntry,_J:juniDnsLocalDomainNameListIndex,_N:juniDnsLocalDomainNameListName,_O:juniDnsLocalDomainNameListRowStatus,'juniDnsConformance':juniDnsConformance,'juniDnsCompliances':juniDnsCompliances,'juniDnsCompliance':juniDnsCompliance,'juniDnsGroups':juniDnsGroups,_R:juniDnsEnableGroup,_S:juniDnsServerListGroup,_U:juniDnsLocalDomainNameListGroup,_T:juniDnsV4V6ServerListGroup})