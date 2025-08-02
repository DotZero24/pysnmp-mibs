_M='agentResCtlStaticIPAddress'
_L='agentResCtlStaticHostName'
_K='agentResCtlDnsNameServerIP'
_J='agentResCtlDnsNameServerIPType'
_I='agentResCtlDomainListName'
_H='InetAddress'
_G='read-create'
_F='OctetString'
_E='not-accessible'
_D='Integer32'
_C='LANCOM-DNS-RESOLVER-CONTROL-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,'InetAddressType')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fastPathDnsResControlMIB=ModuleIdentity((1,3,6,1,4,1,2356,16,1,37))
if mibBuilder.loadTexts:fastPathDnsResControlMIB.setRevisions(('2011-12-14 00:00','2011-01-26 00:00','2007-05-23 00:00','2005-03-28 11:00'))
class DnsCacheEntryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dnsCacheAddresstype',1),('dnsCacheCnametye',2)))
_FastPathDnsResCtlMIBObjects_ObjectIdentity=ObjectIdentity
fastPathDnsResCtlMIBObjects=_FastPathDnsResCtlMIBObjects_ObjectIdentity((1,3,6,1,4,1,2356,16,1,37,1))
_AgentResCtlglobal_ObjectIdentity=ObjectIdentity
agentResCtlglobal=_AgentResCtlglobal_ObjectIdentity((1,3,6,1,4,1,2356,16,1,37,1,1))
_AgentResCtlAdminMode_Type=TruthValue
_AgentResCtlAdminMode_Object=MibScalar
agentResCtlAdminMode=_AgentResCtlAdminMode_Object((1,3,6,1,4,1,2356,16,1,37,1,1,1),_AgentResCtlAdminMode_Type())
agentResCtlAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentResCtlAdminMode.setStatus(_A)
class _AgentResCtlDefDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AgentResCtlDefDomainName_Type.__name__=_F
_AgentResCtlDefDomainName_Object=MibScalar
agentResCtlDefDomainName=_AgentResCtlDefDomainName_Object((1,3,6,1,4,1,2356,16,1,37,1,1,2),_AgentResCtlDefDomainName_Type())
agentResCtlDefDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentResCtlDefDomainName.setStatus(_A)
class _AgentResCtlCacheFlushStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dnsCacheFlushEnable',1),('dnsCacheFlushDisable',2)))
_AgentResCtlCacheFlushStatus_Type.__name__=_D
_AgentResCtlCacheFlushStatus_Object=MibScalar
agentResCtlCacheFlushStatus=_AgentResCtlCacheFlushStatus_Object((1,3,6,1,4,1,2356,16,1,37,1,1,3),_AgentResCtlCacheFlushStatus_Type())
agentResCtlCacheFlushStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentResCtlCacheFlushStatus.setStatus(_A)
class _AgentResCtlRequestTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_AgentResCtlRequestTimeout_Type.__name__=_D
_AgentResCtlRequestTimeout_Object=MibScalar
agentResCtlRequestTimeout=_AgentResCtlRequestTimeout_Object((1,3,6,1,4,1,2356,16,1,37,1,1,4),_AgentResCtlRequestTimeout_Type())
agentResCtlRequestTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentResCtlRequestTimeout.setStatus(_A)
class _AgentResCtlRequestRetransmits_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AgentResCtlRequestRetransmits_Type.__name__=_D
_AgentResCtlRequestRetransmits_Object=MibScalar
agentResCtlRequestRetransmits=_AgentResCtlRequestRetransmits_Object((1,3,6,1,4,1,2356,16,1,37,1,1,5),_AgentResCtlRequestRetransmits_Type())
agentResCtlRequestRetransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:agentResCtlRequestRetransmits.setStatus(_A)
_AgentResCtlDomainListTable_Object=MibTable
agentResCtlDomainListTable=_AgentResCtlDomainListTable_Object((1,3,6,1,4,1,2356,16,1,37,1,1,6))
if mibBuilder.loadTexts:agentResCtlDomainListTable.setStatus(_A)
_AgentResCtlDomainListEntry_Object=MibTableRow
agentResCtlDomainListEntry=_AgentResCtlDomainListEntry_Object((1,3,6,1,4,1,2356,16,1,37,1,1,6,1))
agentResCtlDomainListEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:agentResCtlDomainListEntry.setStatus(_A)
_AgentResCtlDomainListName_Type=DisplayString
_AgentResCtlDomainListName_Object=MibTableColumn
agentResCtlDomainListName=_AgentResCtlDomainListName_Object((1,3,6,1,4,1,2356,16,1,37,1,1,6,1,1),_AgentResCtlDomainListName_Type())
agentResCtlDomainListName.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentResCtlDomainListName.setStatus(_A)
_AgentResCtlDomainListNameStatus_Type=RowStatus
_AgentResCtlDomainListNameStatus_Object=MibTableColumn
agentResCtlDomainListNameStatus=_AgentResCtlDomainListNameStatus_Object((1,3,6,1,4,1,2356,16,1,37,1,1,6,1,2),_AgentResCtlDomainListNameStatus_Type())
agentResCtlDomainListNameStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentResCtlDomainListNameStatus.setStatus(_A)
_AgentResCtlSourceInterface_Type=InterfaceIndexOrZero
_AgentResCtlSourceInterface_Object=MibScalar
agentResCtlSourceInterface=_AgentResCtlSourceInterface_Object((1,3,6,1,4,1,2356,16,1,37,1,1,7),_AgentResCtlSourceInterface_Type())
agentResCtlSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentResCtlSourceInterface.setStatus(_A)
class _AgentResCtlServicePortSrcInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('servicePortEnable',1),('servicePortDisable',2)))
_AgentResCtlServicePortSrcInterface_Type.__name__=_D
_AgentResCtlServicePortSrcInterface_Object=MibScalar
agentResCtlServicePortSrcInterface=_AgentResCtlServicePortSrcInterface_Object((1,3,6,1,4,1,2356,16,1,37,1,1,8),_AgentResCtlServicePortSrcInterface_Type())
agentResCtlServicePortSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentResCtlServicePortSrcInterface.setStatus(_A)
_AgentResCtlServConfig_ObjectIdentity=ObjectIdentity
agentResCtlServConfig=_AgentResCtlServConfig_ObjectIdentity((1,3,6,1,4,1,2356,16,1,37,1,2))
_AgentResCtlServConfigTable_Object=MibTable
agentResCtlServConfigTable=_AgentResCtlServConfigTable_Object((1,3,6,1,4,1,2356,16,1,37,1,2,1))
if mibBuilder.loadTexts:agentResCtlServConfigTable.setStatus(_A)
_AgentResCtlConfigIPEntry_Object=MibTableRow
agentResCtlConfigIPEntry=_AgentResCtlConfigIPEntry_Object((1,3,6,1,4,1,2356,16,1,37,1,2,1,1))
agentResCtlConfigIPEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:agentResCtlConfigIPEntry.setStatus(_A)
_AgentResCtlDnsNameServerIPType_Type=InetAddressType
_AgentResCtlDnsNameServerIPType_Object=MibTableColumn
agentResCtlDnsNameServerIPType=_AgentResCtlDnsNameServerIPType_Object((1,3,6,1,4,1,2356,16,1,37,1,2,1,1,1),_AgentResCtlDnsNameServerIPType_Type())
agentResCtlDnsNameServerIPType.setMaxAccess(_E)
if mibBuilder.loadTexts:agentResCtlDnsNameServerIPType.setStatus(_A)
class _AgentResCtlDnsNameServerIP_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AgentResCtlDnsNameServerIP_Type.__name__=_H
_AgentResCtlDnsNameServerIP_Object=MibTableColumn
agentResCtlDnsNameServerIP=_AgentResCtlDnsNameServerIP_Object((1,3,6,1,4,1,2356,16,1,37,1,2,1,1,2),_AgentResCtlDnsNameServerIP_Type())
agentResCtlDnsNameServerIP.setMaxAccess(_E)
if mibBuilder.loadTexts:agentResCtlDnsNameServerIP.setStatus(_A)
_AgentResCtlDnsNameServerStatus_Type=RowStatus
_AgentResCtlDnsNameServerStatus_Object=MibTableColumn
agentResCtlDnsNameServerStatus=_AgentResCtlDnsNameServerStatus_Object((1,3,6,1,4,1,2356,16,1,37,1,2,1,1,3),_AgentResCtlDnsNameServerStatus_Type())
agentResCtlDnsNameServerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentResCtlDnsNameServerStatus.setStatus(_A)
_AgentResCtlStaticServConfig_ObjectIdentity=ObjectIdentity
agentResCtlStaticServConfig=_AgentResCtlStaticServConfig_ObjectIdentity((1,3,6,1,4,1,2356,16,1,37,1,3))
_AgentResCtlStaticServConfigTable_Object=MibTable
agentResCtlStaticServConfigTable=_AgentResCtlStaticServConfigTable_Object((1,3,6,1,4,1,2356,16,1,37,1,3,1))
if mibBuilder.loadTexts:agentResCtlStaticServConfigTable.setStatus(_A)
_AgentResCtlStaticServEntry_Object=MibTableRow
agentResCtlStaticServEntry=_AgentResCtlStaticServEntry_Object((1,3,6,1,4,1,2356,16,1,37,1,3,1,1))
agentResCtlStaticServEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:agentResCtlStaticServEntry.setStatus(_A)
class _AgentResCtlStaticHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AgentResCtlStaticHostName_Type.__name__=_F
_AgentResCtlStaticHostName_Object=MibTableColumn
agentResCtlStaticHostName=_AgentResCtlStaticHostName_Object((1,3,6,1,4,1,2356,16,1,37,1,3,1,1,1),_AgentResCtlStaticHostName_Type())
agentResCtlStaticHostName.setMaxAccess(_E)
if mibBuilder.loadTexts:agentResCtlStaticHostName.setStatus(_A)
_AgentResCtlStaticIPAddress_Type=IpAddress
_AgentResCtlStaticIPAddress_Object=MibTableColumn
agentResCtlStaticIPAddress=_AgentResCtlStaticIPAddress_Object((1,3,6,1,4,1,2356,16,1,37,1,3,1,1,2),_AgentResCtlStaticIPAddress_Type())
agentResCtlStaticIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentResCtlStaticIPAddress.setStatus(_A)
_AgentResCtlStaticNameServerStatus_Type=RowStatus
_AgentResCtlStaticNameServerStatus_Object=MibTableColumn
agentResCtlStaticNameServerStatus=_AgentResCtlStaticNameServerStatus_Object((1,3,6,1,4,1,2356,16,1,37,1,3,1,1,3),_AgentResCtlStaticNameServerStatus_Type())
agentResCtlStaticNameServerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentResCtlStaticNameServerStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'DnsCacheEntryType':DnsCacheEntryType,'fastPathDnsResControlMIB':fastPathDnsResControlMIB,'fastPathDnsResCtlMIBObjects':fastPathDnsResCtlMIBObjects,'agentResCtlglobal':agentResCtlglobal,'agentResCtlAdminMode':agentResCtlAdminMode,'agentResCtlDefDomainName':agentResCtlDefDomainName,'agentResCtlCacheFlushStatus':agentResCtlCacheFlushStatus,'agentResCtlRequestTimeout':agentResCtlRequestTimeout,'agentResCtlRequestRetransmits':agentResCtlRequestRetransmits,'agentResCtlDomainListTable':agentResCtlDomainListTable,'agentResCtlDomainListEntry':agentResCtlDomainListEntry,_I:agentResCtlDomainListName,'agentResCtlDomainListNameStatus':agentResCtlDomainListNameStatus,'agentResCtlSourceInterface':agentResCtlSourceInterface,'agentResCtlServicePortSrcInterface':agentResCtlServicePortSrcInterface,'agentResCtlServConfig':agentResCtlServConfig,'agentResCtlServConfigTable':agentResCtlServConfigTable,'agentResCtlConfigIPEntry':agentResCtlConfigIPEntry,_J:agentResCtlDnsNameServerIPType,_K:agentResCtlDnsNameServerIP,'agentResCtlDnsNameServerStatus':agentResCtlDnsNameServerStatus,'agentResCtlStaticServConfig':agentResCtlStaticServConfig,'agentResCtlStaticServConfigTable':agentResCtlStaticServConfigTable,'agentResCtlStaticServEntry':agentResCtlStaticServEntry,_L:agentResCtlStaticHostName,_M:agentResCtlStaticIPAddress,'agentResCtlStaticNameServerStatus':agentResCtlStaticNameServerStatus})