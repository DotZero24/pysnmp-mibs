_G='mitelDnsHostTableHostName'
_F='mitelDnsHostTableIpAddress'
_E='MITEL-DNSGROUP-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
mitelIpGrpDnsGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,1,3))
if mibBuilder.loadTexts:mitelIpGrpDnsGroup.setRevisions(('2003-03-21 03:18','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelRouterIpGroup_ObjectIdentity=ObjectIdentity
mitelRouterIpGroup=_MitelRouterIpGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,1))
class _MitelDnsGrpDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelDnsGrpDomainName_Type.__name__=_D
_MitelDnsGrpDomainName_Object=MibScalar
mitelDnsGrpDomainName=_MitelDnsGrpDomainName_Object((1,3,6,1,4,1,1027,4,8,1,1,3,1),_MitelDnsGrpDomainName_Type())
mitelDnsGrpDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsGrpDomainName.setStatus(_A)
_MitelDnsGrpPrimaryDns_Type=IpAddress
_MitelDnsGrpPrimaryDns_Object=MibScalar
mitelDnsGrpPrimaryDns=_MitelDnsGrpPrimaryDns_Object((1,3,6,1,4,1,1027,4,8,1,1,3,2),_MitelDnsGrpPrimaryDns_Type())
mitelDnsGrpPrimaryDns.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsGrpPrimaryDns.setStatus(_A)
_MitelDnsGrpSecondaryDns_Type=IpAddress
_MitelDnsGrpSecondaryDns_Object=MibScalar
mitelDnsGrpSecondaryDns=_MitelDnsGrpSecondaryDns_Object((1,3,6,1,4,1,1027,4,8,1,1,3,3),_MitelDnsGrpSecondaryDns_Type())
mitelDnsGrpSecondaryDns.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsGrpSecondaryDns.setStatus(_A)
class _MitelDnsGrpQueryOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local-first',1),('dns-first',2),('dns-only',3)))
_MitelDnsGrpQueryOrder_Type.__name__=_C
_MitelDnsGrpQueryOrder_Object=MibScalar
mitelDnsGrpQueryOrder=_MitelDnsGrpQueryOrder_Object((1,3,6,1,4,1,1027,4,8,1,1,3,4),_MitelDnsGrpQueryOrder_Type())
mitelDnsGrpQueryOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsGrpQueryOrder.setStatus(_A)
_MitelDnsGrpAnswerTtl_Type=Integer32
_MitelDnsGrpAnswerTtl_Object=MibScalar
mitelDnsGrpAnswerTtl=_MitelDnsGrpAnswerTtl_Object((1,3,6,1,4,1,1027,4,8,1,1,3,5),_MitelDnsGrpAnswerTtl_Type())
mitelDnsGrpAnswerTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsGrpAnswerTtl.setStatus(_A)
_MitelDnsGrpDnsPort_Type=Integer32
_MitelDnsGrpDnsPort_Object=MibScalar
mitelDnsGrpDnsPort=_MitelDnsGrpDnsPort_Object((1,3,6,1,4,1,1027,4,8,1,1,3,6),_MitelDnsGrpDnsPort_Type())
mitelDnsGrpDnsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsGrpDnsPort.setStatus(_A)
class _MitelDnsGrpFilterEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MitelDnsGrpFilterEnabled_Type.__name__=_C
_MitelDnsGrpFilterEnabled_Object=MibScalar
mitelDnsGrpFilterEnabled=_MitelDnsGrpFilterEnabled_Object((1,3,6,1,4,1,1027,4,8,1,1,3,7),_MitelDnsGrpFilterEnabled_Type())
mitelDnsGrpFilterEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsGrpFilterEnabled.setStatus(_A)
_MitelDnsGrpDnsStatistics_ObjectIdentity=ObjectIdentity
mitelDnsGrpDnsStatistics=_MitelDnsGrpDnsStatistics_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,1,3,9))
_MitelDnsStatsQueryTotal_Type=Integer32
_MitelDnsStatsQueryTotal_Object=MibScalar
mitelDnsStatsQueryTotal=_MitelDnsStatsQueryTotal_Object((1,3,6,1,4,1,1027,4,8,1,1,3,9,1),_MitelDnsStatsQueryTotal_Type())
mitelDnsStatsQueryTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsStatsQueryTotal.setStatus(_A)
_MitelDnsStatsQueryFiltered_Type=Integer32
_MitelDnsStatsQueryFiltered_Object=MibScalar
mitelDnsStatsQueryFiltered=_MitelDnsStatsQueryFiltered_Object((1,3,6,1,4,1,1027,4,8,1,1,3,9,2),_MitelDnsStatsQueryFiltered_Type())
mitelDnsStatsQueryFiltered.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsStatsQueryFiltered.setStatus(_A)
_MitelDnsStatsQueryLocal_Type=Integer32
_MitelDnsStatsQueryLocal_Object=MibScalar
mitelDnsStatsQueryLocal=_MitelDnsStatsQueryLocal_Object((1,3,6,1,4,1,1027,4,8,1,1,3,9,3),_MitelDnsStatsQueryLocal_Type())
mitelDnsStatsQueryLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsStatsQueryLocal.setStatus(_A)
_MitelDnsStatsQueryLocalFail_Type=Integer32
_MitelDnsStatsQueryLocalFail_Object=MibScalar
mitelDnsStatsQueryLocalFail=_MitelDnsStatsQueryLocalFail_Object((1,3,6,1,4,1,1027,4,8,1,1,3,9,4),_MitelDnsStatsQueryLocalFail_Type())
mitelDnsStatsQueryLocalFail.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsStatsQueryLocalFail.setStatus(_A)
_MitelDnsStatsQueryExternal_Type=Integer32
_MitelDnsStatsQueryExternal_Object=MibScalar
mitelDnsStatsQueryExternal=_MitelDnsStatsQueryExternal_Object((1,3,6,1,4,1,1027,4,8,1,1,3,9,5),_MitelDnsStatsQueryExternal_Type())
mitelDnsStatsQueryExternal.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsStatsQueryExternal.setStatus(_A)
_MitelDnsStatsQueryExternalFail_Type=Integer32
_MitelDnsStatsQueryExternalFail_Object=MibScalar
mitelDnsStatsQueryExternalFail=_MitelDnsStatsQueryExternalFail_Object((1,3,6,1,4,1,1027,4,8,1,1,3,9,6),_MitelDnsStatsQueryExternalFail_Type())
mitelDnsStatsQueryExternalFail.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsStatsQueryExternalFail.setStatus(_A)
_MitelDnsStatsQueryInvalid_Type=Integer32
_MitelDnsStatsQueryInvalid_Object=MibScalar
mitelDnsStatsQueryInvalid=_MitelDnsStatsQueryInvalid_Object((1,3,6,1,4,1,1027,4,8,1,1,3,9,7),_MitelDnsStatsQueryInvalid_Type())
mitelDnsStatsQueryInvalid.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsStatsQueryInvalid.setStatus(_A)
_MitelDnsGrpDnsHostTable_Object=MibTable
mitelDnsGrpDnsHostTable=_MitelDnsGrpDnsHostTable_Object((1,3,6,1,4,1,1027,4,8,1,1,3,10))
if mibBuilder.loadTexts:mitelDnsGrpDnsHostTable.setStatus(_A)
_MitelDnsGrpDnsHostEntry_Object=MibTableRow
mitelDnsGrpDnsHostEntry=_MitelDnsGrpDnsHostEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,3,10,1))
mitelDnsGrpDnsHostEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:mitelDnsGrpDnsHostEntry.setStatus(_A)
_MitelDnsHostTableIpAddress_Type=IpAddress
_MitelDnsHostTableIpAddress_Object=MibTableColumn
mitelDnsHostTableIpAddress=_MitelDnsHostTableIpAddress_Object((1,3,6,1,4,1,1027,4,8,1,1,3,10,1,1),_MitelDnsHostTableIpAddress_Type())
mitelDnsHostTableIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsHostTableIpAddress.setStatus(_A)
class _MitelDnsHostTableHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_MitelDnsHostTableHostName_Type.__name__=_D
_MitelDnsHostTableHostName_Object=MibTableColumn
mitelDnsHostTableHostName=_MitelDnsHostTableHostName_Object((1,3,6,1,4,1,1027,4,8,1,1,3,10,1,2),_MitelDnsHostTableHostName_Type())
mitelDnsHostTableHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDnsHostTableHostName.setStatus(_A)
_MitelDnsHostTableRowStatus_Type=RowStatus
_MitelDnsHostTableRowStatus_Object=MibTableColumn
mitelDnsHostTableRowStatus=_MitelDnsHostTableRowStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,3,10,1,3),_MitelDnsHostTableRowStatus_Type())
mitelDnsHostTableRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelDnsHostTableRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterIpGroup':mitelRouterIpGroup,'mitelIpGrpDnsGroup':mitelIpGrpDnsGroup,'mitelDnsGrpDomainName':mitelDnsGrpDomainName,'mitelDnsGrpPrimaryDns':mitelDnsGrpPrimaryDns,'mitelDnsGrpSecondaryDns':mitelDnsGrpSecondaryDns,'mitelDnsGrpQueryOrder':mitelDnsGrpQueryOrder,'mitelDnsGrpAnswerTtl':mitelDnsGrpAnswerTtl,'mitelDnsGrpDnsPort':mitelDnsGrpDnsPort,'mitelDnsGrpFilterEnabled':mitelDnsGrpFilterEnabled,'mitelDnsGrpDnsStatistics':mitelDnsGrpDnsStatistics,'mitelDnsStatsQueryTotal':mitelDnsStatsQueryTotal,'mitelDnsStatsQueryFiltered':mitelDnsStatsQueryFiltered,'mitelDnsStatsQueryLocal':mitelDnsStatsQueryLocal,'mitelDnsStatsQueryLocalFail':mitelDnsStatsQueryLocalFail,'mitelDnsStatsQueryExternal':mitelDnsStatsQueryExternal,'mitelDnsStatsQueryExternalFail':mitelDnsStatsQueryExternalFail,'mitelDnsStatsQueryInvalid':mitelDnsStatsQueryInvalid,'mitelDnsGrpDnsHostTable':mitelDnsGrpDnsHostTable,'mitelDnsGrpDnsHostEntry':mitelDnsGrpDnsHostEntry,_F:mitelDnsHostTableIpAddress,_G:mitelDnsHostTableHostName,'mitelDnsHostTableRowStatus':mitelDnsHostTableRowStatus})