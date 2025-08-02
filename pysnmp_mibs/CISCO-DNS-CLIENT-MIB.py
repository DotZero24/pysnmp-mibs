_W='ciscoDNSDomainNameConfigGroup'
_V='ciscoDNSServerConfigGroup'
_U='cdcDNSDomainNameStatus'
_T='cdcDNSDomainName'
_S='cdcDefaultDNSDomainName'
_R='cdcDNSServerStatus'
_Q='cdcDNSServerAddr'
_P='cdcDNSServerAddrType'
_O='cdcDNSServerNextAvailIndex'
_N='cdcNoOfDNSServerConfig'
_M='cdcDNSConfigEnable'
_L='cdcDNSDomainNameIndex'
_K='not-accessible'
_J='cdcDNSServerIndex'
_I='read-only'
_H='read-write'
_G='Integer32'
_F='InetAddressType'
_E='SnmpAdminString'
_D='read-create'
_C='Unsigned32'
_B='CISCO-DNS-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoDNSClientMIB=ModuleIdentity((1,3,6,1,4,1,9,9,436))
if mibBuilder.loadTexts:ciscoDNSClientMIB.setRevisions(('2004-09-09 00:00',))
_CiscoDNSClientMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDNSClientMIBNotifs=_CiscoDNSClientMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,436,0))
_CiscoDNSClientMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDNSClientMIBObjects=_CiscoDNSClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,436,1))
_CdcConfigGroup_ObjectIdentity=ObjectIdentity
cdcConfigGroup=_CdcConfigGroup_ObjectIdentity((1,3,6,1,4,1,9,9,436,1,1))
class _CdcDNSConfigEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CdcDNSConfigEnable_Type.__name__=_G
_CdcDNSConfigEnable_Object=MibScalar
cdcDNSConfigEnable=_CdcDNSConfigEnable_Object((1,3,6,1,4,1,9,9,436,1,1,1),_CdcDNSConfigEnable_Type())
cdcDNSConfigEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:cdcDNSConfigEnable.setStatus(_A)
class _CdcNoOfDNSServerConfig_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CdcNoOfDNSServerConfig_Type.__name__=_C
_CdcNoOfDNSServerConfig_Object=MibScalar
cdcNoOfDNSServerConfig=_CdcNoOfDNSServerConfig_Object((1,3,6,1,4,1,9,9,436,1,1,2),_CdcNoOfDNSServerConfig_Type())
cdcNoOfDNSServerConfig.setMaxAccess(_I)
if mibBuilder.loadTexts:cdcNoOfDNSServerConfig.setStatus(_A)
class _CdcDNSServerNextAvailIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdcDNSServerNextAvailIndex_Type.__name__=_C
_CdcDNSServerNextAvailIndex_Object=MibScalar
cdcDNSServerNextAvailIndex=_CdcDNSServerNextAvailIndex_Object((1,3,6,1,4,1,9,9,436,1,1,3),_CdcDNSServerNextAvailIndex_Type())
cdcDNSServerNextAvailIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cdcDNSServerNextAvailIndex.setStatus(_A)
_CdcDNSServerTable_Object=MibTable
cdcDNSServerTable=_CdcDNSServerTable_Object((1,3,6,1,4,1,9,9,436,1,1,4))
if mibBuilder.loadTexts:cdcDNSServerTable.setStatus(_A)
_CdcDNSServerEntry_Object=MibTableRow
cdcDNSServerEntry=_CdcDNSServerEntry_Object((1,3,6,1,4,1,9,9,436,1,1,4,1))
cdcDNSServerEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cdcDNSServerEntry.setStatus(_A)
class _CdcDNSServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CdcDNSServerIndex_Type.__name__=_C
_CdcDNSServerIndex_Object=MibTableColumn
cdcDNSServerIndex=_CdcDNSServerIndex_Object((1,3,6,1,4,1,9,9,436,1,1,4,1,1),_CdcDNSServerIndex_Type())
cdcDNSServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cdcDNSServerIndex.setStatus(_A)
class _CdcDNSServerAddrType_Type(InetAddressType):defaultValue=1
_CdcDNSServerAddrType_Type.__name__=_F
_CdcDNSServerAddrType_Object=MibTableColumn
cdcDNSServerAddrType=_CdcDNSServerAddrType_Object((1,3,6,1,4,1,9,9,436,1,1,4,1,2),_CdcDNSServerAddrType_Type())
cdcDNSServerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdcDNSServerAddrType.setStatus(_A)
_CdcDNSServerAddr_Type=InetAddress
_CdcDNSServerAddr_Object=MibTableColumn
cdcDNSServerAddr=_CdcDNSServerAddr_Object((1,3,6,1,4,1,9,9,436,1,1,4,1,3),_CdcDNSServerAddr_Type())
cdcDNSServerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cdcDNSServerAddr.setStatus(_A)
_CdcDNSServerStatus_Type=RowStatus
_CdcDNSServerStatus_Object=MibTableColumn
cdcDNSServerStatus=_CdcDNSServerStatus_Object((1,3,6,1,4,1,9,9,436,1,1,4,1,4),_CdcDNSServerStatus_Type())
cdcDNSServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cdcDNSServerStatus.setStatus(_A)
class _CdcDefaultDNSDomainName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CdcDefaultDNSDomainName_Type.__name__=_E
_CdcDefaultDNSDomainName_Object=MibScalar
cdcDefaultDNSDomainName=_CdcDefaultDNSDomainName_Object((1,3,6,1,4,1,9,9,436,1,1,5),_CdcDefaultDNSDomainName_Type())
cdcDefaultDNSDomainName.setMaxAccess(_H)
if mibBuilder.loadTexts:cdcDefaultDNSDomainName.setStatus(_A)
_CdcDNSDomainNameTable_Object=MibTable
cdcDNSDomainNameTable=_CdcDNSDomainNameTable_Object((1,3,6,1,4,1,9,9,436,1,1,6))
if mibBuilder.loadTexts:cdcDNSDomainNameTable.setStatus(_A)
_CdcDNSDomainNameEntry_Object=MibTableRow
cdcDNSDomainNameEntry=_CdcDNSDomainNameEntry_Object((1,3,6,1,4,1,9,9,436,1,1,6,1))
cdcDNSDomainNameEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cdcDNSDomainNameEntry.setStatus(_A)
class _CdcDNSDomainNameIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CdcDNSDomainNameIndex_Type.__name__=_C
_CdcDNSDomainNameIndex_Object=MibTableColumn
cdcDNSDomainNameIndex=_CdcDNSDomainNameIndex_Object((1,3,6,1,4,1,9,9,436,1,1,6,1,1),_CdcDNSDomainNameIndex_Type())
cdcDNSDomainNameIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cdcDNSDomainNameIndex.setStatus(_A)
class _CdcDNSDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CdcDNSDomainName_Type.__name__=_E
_CdcDNSDomainName_Object=MibTableColumn
cdcDNSDomainName=_CdcDNSDomainName_Object((1,3,6,1,4,1,9,9,436,1,1,6,1,2),_CdcDNSDomainName_Type())
cdcDNSDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:cdcDNSDomainName.setStatus(_A)
_CdcDNSDomainNameStatus_Type=RowStatus
_CdcDNSDomainNameStatus_Object=MibTableColumn
cdcDNSDomainNameStatus=_CdcDNSDomainNameStatus_Object((1,3,6,1,4,1,9,9,436,1,1,6,1,3),_CdcDNSDomainNameStatus_Type())
cdcDNSDomainNameStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cdcDNSDomainNameStatus.setStatus(_A)
_CiscoDNSClientMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDNSClientMIBConformance=_CiscoDNSClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,436,2))
_CiscoDNSClientMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDNSClientMIBCompliances=_CiscoDNSClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,436,2,1))
_CiscoDNSClientMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDNSClientMIBGroups=_CiscoDNSClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,436,2,2))
ciscoDNSServerConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,436,2,2,1))
ciscoDNSServerConfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoDNSServerConfigGroup.setStatus(_A)
ciscoDNSDomainNameConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,436,2,2,2))
ciscoDNSDomainNameConfigGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoDNSDomainNameConfigGroup.setStatus(_A)
ciscoDNSClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,436,2,1,1))
ciscoDNSClientMIBCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoDNSClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDNSClientMIB':ciscoDNSClientMIB,'ciscoDNSClientMIBNotifs':ciscoDNSClientMIBNotifs,'ciscoDNSClientMIBObjects':ciscoDNSClientMIBObjects,'cdcConfigGroup':cdcConfigGroup,_M:cdcDNSConfigEnable,_N:cdcNoOfDNSServerConfig,_O:cdcDNSServerNextAvailIndex,'cdcDNSServerTable':cdcDNSServerTable,'cdcDNSServerEntry':cdcDNSServerEntry,_J:cdcDNSServerIndex,_P:cdcDNSServerAddrType,_Q:cdcDNSServerAddr,_R:cdcDNSServerStatus,_S:cdcDefaultDNSDomainName,'cdcDNSDomainNameTable':cdcDNSDomainNameTable,'cdcDNSDomainNameEntry':cdcDNSDomainNameEntry,_L:cdcDNSDomainNameIndex,_T:cdcDNSDomainName,_U:cdcDNSDomainNameStatus,'ciscoDNSClientMIBConformance':ciscoDNSClientMIBConformance,'ciscoDNSClientMIBCompliances':ciscoDNSClientMIBCompliances,'ciscoDNSClientMIBCompliance':ciscoDNSClientMIBCompliance,'ciscoDNSClientMIBGroups':ciscoDNSClientMIBGroups,_V:ciscoDNSServerConfigGroup,_W:ciscoDNSDomainNameConfigGroup})