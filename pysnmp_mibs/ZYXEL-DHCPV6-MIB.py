_L='zyDhcpv6ServerPDClientDUID'
_K='zyDhcpv6ServerInfoIfIndex'
_J='zyDhcpv6RelayVid'
_I='Unsigned32'
_H='zyDhcpv6ClientIfIndex'
_G='read-create'
_F='read-only'
_E='not-accessible'
_D='Integer32'
_C='ZYXEL-DHCPV6-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDhcpv6=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,21))
_ZyxelDhcpv6Setup_ObjectIdentity=ObjectIdentity
zyxelDhcpv6Setup=_ZyxelDhcpv6Setup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,21,1))
_ZyDhcpv6MaxNumberOfRelays_Type=Integer32
_ZyDhcpv6MaxNumberOfRelays_Object=MibScalar
zyDhcpv6MaxNumberOfRelays=_ZyDhcpv6MaxNumberOfRelays_Object((1,3,6,1,4,1,890,1,15,3,21,1,1),_ZyDhcpv6MaxNumberOfRelays_Type())
zyDhcpv6MaxNumberOfRelays.setMaxAccess(_F)
if mibBuilder.loadTexts:zyDhcpv6MaxNumberOfRelays.setStatus(_A)
_ZyxelDhcpv6RelayTable_Object=MibTable
zyxelDhcpv6RelayTable=_ZyxelDhcpv6RelayTable_Object((1,3,6,1,4,1,890,1,15,3,21,1,2))
if mibBuilder.loadTexts:zyxelDhcpv6RelayTable.setStatus(_A)
_ZyxelDhcpv6RelayEntry_Object=MibTableRow
zyxelDhcpv6RelayEntry=_ZyxelDhcpv6RelayEntry_Object((1,3,6,1,4,1,890,1,15,3,21,1,2,1))
zyxelDhcpv6RelayEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:zyxelDhcpv6RelayEntry.setStatus(_A)
_ZyDhcpv6RelayVid_Type=Integer32
_ZyDhcpv6RelayVid_Object=MibTableColumn
zyDhcpv6RelayVid=_ZyDhcpv6RelayVid_Object((1,3,6,1,4,1,890,1,15,3,21,1,2,1,1),_ZyDhcpv6RelayVid_Type())
zyDhcpv6RelayVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyDhcpv6RelayVid.setStatus(_A)
_ZyDhcpv6RelayHelperIpAddress_Type=InetAddress
_ZyDhcpv6RelayHelperIpAddress_Object=MibTableColumn
zyDhcpv6RelayHelperIpAddress=_ZyDhcpv6RelayHelperIpAddress_Object((1,3,6,1,4,1,890,1,15,3,21,1,2,1,2),_ZyDhcpv6RelayHelperIpAddress_Type())
zyDhcpv6RelayHelperIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6RelayHelperIpAddress.setStatus(_A)
_ZyDhcpv6RelayHelperIpAddressType_Type=InetAddressType
_ZyDhcpv6RelayHelperIpAddressType_Object=MibTableColumn
zyDhcpv6RelayHelperIpAddressType=_ZyDhcpv6RelayHelperIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,21,1,2,1,3),_ZyDhcpv6RelayHelperIpAddressType_Type())
zyDhcpv6RelayHelperIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6RelayHelperIpAddressType.setStatus(_A)
_ZyDhcpv6RelayOptionIfIdState_Type=EnabledStatus
_ZyDhcpv6RelayOptionIfIdState_Object=MibTableColumn
zyDhcpv6RelayOptionIfIdState=_ZyDhcpv6RelayOptionIfIdState_Object((1,3,6,1,4,1,890,1,15,3,21,1,2,1,4),_ZyDhcpv6RelayOptionIfIdState_Type())
zyDhcpv6RelayOptionIfIdState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6RelayOptionIfIdState.setStatus(_A)
_ZyDhcpv6RelayOptionRemoteIdData_Type=DisplayString
_ZyDhcpv6RelayOptionRemoteIdData_Object=MibTableColumn
zyDhcpv6RelayOptionRemoteIdData=_ZyDhcpv6RelayOptionRemoteIdData_Object((1,3,6,1,4,1,890,1,15,3,21,1,2,1,5),_ZyDhcpv6RelayOptionRemoteIdData_Type())
zyDhcpv6RelayOptionRemoteIdData.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6RelayOptionRemoteIdData.setStatus(_A)
_ZyDhcpv6RelayRowStatus_Type=RowStatus
_ZyDhcpv6RelayRowStatus_Object=MibTableColumn
zyDhcpv6RelayRowStatus=_ZyDhcpv6RelayRowStatus_Object((1,3,6,1,4,1,890,1,15,3,21,1,2,1,6),_ZyDhcpv6RelayRowStatus_Type())
zyDhcpv6RelayRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zyDhcpv6RelayRowStatus.setStatus(_A)
_ZyxelDhcpv6ClientTable_Object=MibTable
zyxelDhcpv6ClientTable=_ZyxelDhcpv6ClientTable_Object((1,3,6,1,4,1,890,1,15,3,21,1,3))
if mibBuilder.loadTexts:zyxelDhcpv6ClientTable.setStatus(_A)
_ZyxelDhcpv6ClientEntry_Object=MibTableRow
zyxelDhcpv6ClientEntry=_ZyxelDhcpv6ClientEntry_Object((1,3,6,1,4,1,890,1,15,3,21,1,3,1))
zyxelDhcpv6ClientEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:zyxelDhcpv6ClientEntry.setStatus(_A)
_ZyDhcpv6ClientIfIndex_Type=Integer32
_ZyDhcpv6ClientIfIndex_Object=MibTableColumn
zyDhcpv6ClientIfIndex=_ZyDhcpv6ClientIfIndex_Object((1,3,6,1,4,1,890,1,15,3,21,1,3,1,1),_ZyDhcpv6ClientIfIndex_Type())
zyDhcpv6ClientIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zyDhcpv6ClientIfIndex.setStatus(_A)
class _ZyDhcpv6ClientIaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('iana',1)))
_ZyDhcpv6ClientIaType_Type.__name__=_D
_ZyDhcpv6ClientIaType_Object=MibTableColumn
zyDhcpv6ClientIaType=_ZyDhcpv6ClientIaType_Object((1,3,6,1,4,1,890,1,15,3,21,1,3,1,2),_ZyDhcpv6ClientIaType_Type())
zyDhcpv6ClientIaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ClientIaType.setStatus(_A)
class _ZyDhcpv6ClientIaTypeRapidCommit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('rapidCommit',1)))
_ZyDhcpv6ClientIaTypeRapidCommit_Type.__name__=_D
_ZyDhcpv6ClientIaTypeRapidCommit_Object=MibTableColumn
zyDhcpv6ClientIaTypeRapidCommit=_ZyDhcpv6ClientIaTypeRapidCommit_Object((1,3,6,1,4,1,890,1,15,3,21,1,3,1,3),_ZyDhcpv6ClientIaTypeRapidCommit_Type())
zyDhcpv6ClientIaTypeRapidCommit.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ClientIaTypeRapidCommit.setStatus(_A)
_ZyDhcpv6ClientOptionDnsState_Type=EnabledStatus
_ZyDhcpv6ClientOptionDnsState_Object=MibTableColumn
zyDhcpv6ClientOptionDnsState=_ZyDhcpv6ClientOptionDnsState_Object((1,3,6,1,4,1,890,1,15,3,21,1,3,1,4),_ZyDhcpv6ClientOptionDnsState_Type())
zyDhcpv6ClientOptionDnsState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ClientOptionDnsState.setStatus(_A)
_ZyDhcpv6ClientOptionDomainListState_Type=EnabledStatus
_ZyDhcpv6ClientOptionDomainListState_Object=MibTableColumn
zyDhcpv6ClientOptionDomainListState=_ZyDhcpv6ClientOptionDomainListState_Object((1,3,6,1,4,1,890,1,15,3,21,1,3,1,5),_ZyDhcpv6ClientOptionDomainListState_Type())
zyDhcpv6ClientOptionDomainListState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ClientOptionDomainListState.setStatus(_A)
_ZyDhcpv6ClientInfoRefreshMinimum_Type=Unsigned32
_ZyDhcpv6ClientInfoRefreshMinimum_Object=MibTableColumn
zyDhcpv6ClientInfoRefreshMinimum=_ZyDhcpv6ClientInfoRefreshMinimum_Object((1,3,6,1,4,1,890,1,15,3,21,1,3,1,6),_ZyDhcpv6ClientInfoRefreshMinimum_Type())
zyDhcpv6ClientInfoRefreshMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ClientInfoRefreshMinimum.setStatus(_A)
_ZyDhcpv6ServerMaxInfoNumber_Type=Integer32
_ZyDhcpv6ServerMaxInfoNumber_Object=MibScalar
zyDhcpv6ServerMaxInfoNumber=_ZyDhcpv6ServerMaxInfoNumber_Object((1,3,6,1,4,1,890,1,15,3,21,1,4),_ZyDhcpv6ServerMaxInfoNumber_Type())
zyDhcpv6ServerMaxInfoNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:zyDhcpv6ServerMaxInfoNumber.setStatus(_A)
_ZyxelDhcpv6ServerTable_Object=MibTable
zyxelDhcpv6ServerTable=_ZyxelDhcpv6ServerTable_Object((1,3,6,1,4,1,890,1,15,3,21,1,5))
if mibBuilder.loadTexts:zyxelDhcpv6ServerTable.setStatus(_A)
_ZyxelDhcpv6ServerInfoEntry_Object=MibTableRow
zyxelDhcpv6ServerInfoEntry=_ZyxelDhcpv6ServerInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,21,1,5,1))
zyxelDhcpv6ServerInfoEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:zyxelDhcpv6ServerInfoEntry.setStatus(_A)
class _ZyDhcpv6ServerInfoIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_ZyDhcpv6ServerInfoIfIndex_Type.__name__=_D
_ZyDhcpv6ServerInfoIfIndex_Object=MibTableColumn
zyDhcpv6ServerInfoIfIndex=_ZyDhcpv6ServerInfoIfIndex_Object((1,3,6,1,4,1,890,1,15,3,21,1,5,1,1),_ZyDhcpv6ServerInfoIfIndex_Type())
zyDhcpv6ServerInfoIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zyDhcpv6ServerInfoIfIndex.setStatus(_A)
_ZyDhcpv6ServerInfoDNSServerIpAddress_Type=InetAddress
_ZyDhcpv6ServerInfoDNSServerIpAddress_Object=MibTableColumn
zyDhcpv6ServerInfoDNSServerIpAddress=_ZyDhcpv6ServerInfoDNSServerIpAddress_Object((1,3,6,1,4,1,890,1,15,3,21,1,5,1,2),_ZyDhcpv6ServerInfoDNSServerIpAddress_Type())
zyDhcpv6ServerInfoDNSServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ServerInfoDNSServerIpAddress.setStatus(_A)
class _ZyDhcpv6ServerInfoRefreshTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(600,4294967295))
_ZyDhcpv6ServerInfoRefreshTime_Type.__name__=_I
_ZyDhcpv6ServerInfoRefreshTime_Object=MibTableColumn
zyDhcpv6ServerInfoRefreshTime=_ZyDhcpv6ServerInfoRefreshTime_Object((1,3,6,1,4,1,890,1,15,3,21,1,5,1,3),_ZyDhcpv6ServerInfoRefreshTime_Type())
zyDhcpv6ServerInfoRefreshTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ServerInfoRefreshTime.setStatus(_A)
_ZyDhcpv6ServerInfoRowStatus_Type=RowStatus
_ZyDhcpv6ServerInfoRowStatus_Object=MibTableColumn
zyDhcpv6ServerInfoRowStatus=_ZyDhcpv6ServerInfoRowStatus_Object((1,3,6,1,4,1,890,1,15,3,21,1,5,1,100),_ZyDhcpv6ServerInfoRowStatus_Type())
zyDhcpv6ServerInfoRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zyDhcpv6ServerInfoRowStatus.setStatus(_A)
_ZyDhcpv6ServerMaxPDNumber_Type=Integer32
_ZyDhcpv6ServerMaxPDNumber_Object=MibScalar
zyDhcpv6ServerMaxPDNumber=_ZyDhcpv6ServerMaxPDNumber_Object((1,3,6,1,4,1,890,1,15,3,21,1,6),_ZyDhcpv6ServerMaxPDNumber_Type())
zyDhcpv6ServerMaxPDNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:zyDhcpv6ServerMaxPDNumber.setStatus(_A)
_ZyxelDhcpv6PDTable_Object=MibTable
zyxelDhcpv6PDTable=_ZyxelDhcpv6PDTable_Object((1,3,6,1,4,1,890,1,15,3,21,1,7))
if mibBuilder.loadTexts:zyxelDhcpv6PDTable.setStatus(_A)
_ZyxelDhcpv6ServerPDEntry_Object=MibTableRow
zyxelDhcpv6ServerPDEntry=_ZyxelDhcpv6ServerPDEntry_Object((1,3,6,1,4,1,890,1,15,3,21,1,7,1))
zyxelDhcpv6ServerPDEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:zyxelDhcpv6ServerPDEntry.setStatus(_A)
_ZyDhcpv6ServerPDClientDUID_Type=DisplayString
_ZyDhcpv6ServerPDClientDUID_Object=MibTableColumn
zyDhcpv6ServerPDClientDUID=_ZyDhcpv6ServerPDClientDUID_Object((1,3,6,1,4,1,890,1,15,3,21,1,7,1,1),_ZyDhcpv6ServerPDClientDUID_Type())
zyDhcpv6ServerPDClientDUID.setMaxAccess(_E)
if mibBuilder.loadTexts:zyDhcpv6ServerPDClientDUID.setStatus(_A)
_ZyDhcpv6ServerPDClientName_Type=DisplayString
_ZyDhcpv6ServerPDClientName_Object=MibTableColumn
zyDhcpv6ServerPDClientName=_ZyDhcpv6ServerPDClientName_Object((1,3,6,1,4,1,890,1,15,3,21,1,7,1,2),_ZyDhcpv6ServerPDClientName_Type())
zyDhcpv6ServerPDClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ServerPDClientName.setStatus(_A)
_ZyDhcpv6ServerPDIfIndex_Type=Integer32
_ZyDhcpv6ServerPDIfIndex_Object=MibTableColumn
zyDhcpv6ServerPDIfIndex=_ZyDhcpv6ServerPDIfIndex_Object((1,3,6,1,4,1,890,1,15,3,21,1,7,1,3),_ZyDhcpv6ServerPDIfIndex_Type())
zyDhcpv6ServerPDIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ServerPDIfIndex.setStatus(_A)
_ZyDhcpv6ServerPDPrefix_Type=InetAddress
_ZyDhcpv6ServerPDPrefix_Object=MibTableColumn
zyDhcpv6ServerPDPrefix=_ZyDhcpv6ServerPDPrefix_Object((1,3,6,1,4,1,890,1,15,3,21,1,7,1,4),_ZyDhcpv6ServerPDPrefix_Type())
zyDhcpv6ServerPDPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ServerPDPrefix.setStatus(_A)
class _ZyDhcpv6ServerPDPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_ZyDhcpv6ServerPDPrefixLength_Type.__name__=_D
_ZyDhcpv6ServerPDPrefixLength_Object=MibTableColumn
zyDhcpv6ServerPDPrefixLength=_ZyDhcpv6ServerPDPrefixLength_Object((1,3,6,1,4,1,890,1,15,3,21,1,7,1,5),_ZyDhcpv6ServerPDPrefixLength_Type())
zyDhcpv6ServerPDPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ServerPDPrefixLength.setStatus(_A)
_ZyDhcpv6ServerPDRowStatus_Type=RowStatus
_ZyDhcpv6ServerPDRowStatus_Object=MibTableColumn
zyDhcpv6ServerPDRowStatus=_ZyDhcpv6ServerPDRowStatus_Object((1,3,6,1,4,1,890,1,15,3,21,1,7,1,100),_ZyDhcpv6ServerPDRowStatus_Type())
zyDhcpv6ServerPDRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zyDhcpv6ServerPDRowStatus.setStatus(_A)
_ZyxelDhcpv6Status_ObjectIdentity=ObjectIdentity
zyxelDhcpv6Status=_ZyxelDhcpv6Status_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,21,2))
_ZyxelDhcpv6ClientInfoTable_Object=MibTable
zyxelDhcpv6ClientInfoTable=_ZyxelDhcpv6ClientInfoTable_Object((1,3,6,1,4,1,890,1,15,3,21,2,1))
if mibBuilder.loadTexts:zyxelDhcpv6ClientInfoTable.setStatus(_A)
_ZyxelDhcpv6ClientInfoEntry_Object=MibTableRow
zyxelDhcpv6ClientInfoEntry=_ZyxelDhcpv6ClientInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,21,2,1,1))
zyxelDhcpv6ClientInfoEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:zyxelDhcpv6ClientInfoEntry.setStatus(_A)
_ZyDhcpv6ClientInfoRestart_Type=EnabledStatus
_ZyDhcpv6ClientInfoRestart_Object=MibTableColumn
zyDhcpv6ClientInfoRestart=_ZyDhcpv6ClientInfoRestart_Object((1,3,6,1,4,1,890,1,15,3,21,2,1,1,1),_ZyDhcpv6ClientInfoRestart_Type())
zyDhcpv6ClientInfoRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpv6ClientInfoRestart.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelDhcpv6':zyxelDhcpv6,'zyxelDhcpv6Setup':zyxelDhcpv6Setup,'zyDhcpv6MaxNumberOfRelays':zyDhcpv6MaxNumberOfRelays,'zyxelDhcpv6RelayTable':zyxelDhcpv6RelayTable,'zyxelDhcpv6RelayEntry':zyxelDhcpv6RelayEntry,_J:zyDhcpv6RelayVid,'zyDhcpv6RelayHelperIpAddress':zyDhcpv6RelayHelperIpAddress,'zyDhcpv6RelayHelperIpAddressType':zyDhcpv6RelayHelperIpAddressType,'zyDhcpv6RelayOptionIfIdState':zyDhcpv6RelayOptionIfIdState,'zyDhcpv6RelayOptionRemoteIdData':zyDhcpv6RelayOptionRemoteIdData,'zyDhcpv6RelayRowStatus':zyDhcpv6RelayRowStatus,'zyxelDhcpv6ClientTable':zyxelDhcpv6ClientTable,'zyxelDhcpv6ClientEntry':zyxelDhcpv6ClientEntry,_H:zyDhcpv6ClientIfIndex,'zyDhcpv6ClientIaType':zyDhcpv6ClientIaType,'zyDhcpv6ClientIaTypeRapidCommit':zyDhcpv6ClientIaTypeRapidCommit,'zyDhcpv6ClientOptionDnsState':zyDhcpv6ClientOptionDnsState,'zyDhcpv6ClientOptionDomainListState':zyDhcpv6ClientOptionDomainListState,'zyDhcpv6ClientInfoRefreshMinimum':zyDhcpv6ClientInfoRefreshMinimum,'zyDhcpv6ServerMaxInfoNumber':zyDhcpv6ServerMaxInfoNumber,'zyxelDhcpv6ServerTable':zyxelDhcpv6ServerTable,'zyxelDhcpv6ServerInfoEntry':zyxelDhcpv6ServerInfoEntry,_K:zyDhcpv6ServerInfoIfIndex,'zyDhcpv6ServerInfoDNSServerIpAddress':zyDhcpv6ServerInfoDNSServerIpAddress,'zyDhcpv6ServerInfoRefreshTime':zyDhcpv6ServerInfoRefreshTime,'zyDhcpv6ServerInfoRowStatus':zyDhcpv6ServerInfoRowStatus,'zyDhcpv6ServerMaxPDNumber':zyDhcpv6ServerMaxPDNumber,'zyxelDhcpv6PDTable':zyxelDhcpv6PDTable,'zyxelDhcpv6ServerPDEntry':zyxelDhcpv6ServerPDEntry,_L:zyDhcpv6ServerPDClientDUID,'zyDhcpv6ServerPDClientName':zyDhcpv6ServerPDClientName,'zyDhcpv6ServerPDIfIndex':zyDhcpv6ServerPDIfIndex,'zyDhcpv6ServerPDPrefix':zyDhcpv6ServerPDPrefix,'zyDhcpv6ServerPDPrefixLength':zyDhcpv6ServerPDPrefixLength,'zyDhcpv6ServerPDRowStatus':zyDhcpv6ServerPDRowStatus,'zyxelDhcpv6Status':zyxelDhcpv6Status,'zyxelDhcpv6ClientInfoTable':zyxelDhcpv6ClientInfoTable,'zyxelDhcpv6ClientInfoEntry':zyxelDhcpv6ClientInfoEntry,'zyDhcpv6ClientInfoRestart':zyDhcpv6ClientInfoRestart})