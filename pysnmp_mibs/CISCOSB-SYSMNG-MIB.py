_N='rlSysmngResourcePerUnitUnitId'
_M='rlSysmngResourcePerUnitRouteType'
_L='rlSysmngResourceUsageType'
_K='read-write'
_J='rlSysmngResourceRouteType'
_I='rlSysmngTcamAllocPoolType'
_H='rlSysmngTcamAllocProfileName'
_G='vlanMapping'
_F='Integer32'
_E='not-accessible'
_D='CISCOSB-SYSMNG-MIB'
_C='read-only'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percents,switch001=mibBuilder.importSymbols('CISCOSB-MIB','Percents','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TruthValue')
rlSysmngMib=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,204))
if mibBuilder.loadTexts:rlSysmngMib.setRevisions(('2010-10-31 00:00',))
class SysmngResourceRouteType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('ipmv4',3),('ipmv6',4),('nonIp',5),('ipv4Policy',6),('ipv6Policy',7),(_G,8),('totalCount',9)))
class SysmngResourceRouteUsageType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('ipv4Neighbor',1),('ipv4Address',2),('ipv4Route',3),('ipv6Neighbor',4),('ipv6Address',5),('ipv6OnlinkPrefix',6),('ipv6Route',7),('ipmv4Route',8),('ipmv4RouteStarG',9),('ipmv6Route',10),('ipmv6RouteStarG',11),('ipv4PolicyRoute',12),('ipv6PolicyRoute',13),(_G,14)))
class SysmngPoolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('router',1),('iscsi',2),('voip',3),('misc',4)))
_RlSysmngTcamAllocations_ObjectIdentity=ObjectIdentity
rlSysmngTcamAllocations=_RlSysmngTcamAllocations_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,204,1))
_RlSysmngTcamAllocationsTable_Object=MibTable
rlSysmngTcamAllocationsTable=_RlSysmngTcamAllocationsTable_Object((1,3,6,1,4,1,9,6,1,101,204,1,1))
if mibBuilder.loadTexts:rlSysmngTcamAllocationsTable.setStatus(_A)
_RlSysmngTcamAllocationsEntry_Object=MibTableRow
rlSysmngTcamAllocationsEntry=_RlSysmngTcamAllocationsEntry_Object((1,3,6,1,4,1,9,6,1,101,204,1,1,1))
rlSysmngTcamAllocationsEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:rlSysmngTcamAllocationsEntry.setStatus(_A)
_RlSysmngTcamAllocProfileName_Type=DisplayString
_RlSysmngTcamAllocProfileName_Object=MibTableColumn
rlSysmngTcamAllocProfileName=_RlSysmngTcamAllocProfileName_Object((1,3,6,1,4,1,9,6,1,101,204,1,1,1,1),_RlSysmngTcamAllocProfileName_Type())
rlSysmngTcamAllocProfileName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSysmngTcamAllocProfileName.setStatus(_A)
_RlSysmngTcamAllocPoolType_Type=SysmngPoolType
_RlSysmngTcamAllocPoolType_Object=MibTableColumn
rlSysmngTcamAllocPoolType=_RlSysmngTcamAllocPoolType_Object((1,3,6,1,4,1,9,6,1,101,204,1,1,1,2),_RlSysmngTcamAllocPoolType_Type())
rlSysmngTcamAllocPoolType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSysmngTcamAllocPoolType.setStatus(_A)
class _RlSysmngTcamAllocMinRequiredEntries_Type(Unsigned32):defaultValue=0
_RlSysmngTcamAllocMinRequiredEntries_Type.__name__=_B
_RlSysmngTcamAllocMinRequiredEntries_Object=MibTableColumn
rlSysmngTcamAllocMinRequiredEntries=_RlSysmngTcamAllocMinRequiredEntries_Object((1,3,6,1,4,1,9,6,1,101,204,1,1,1,3),_RlSysmngTcamAllocMinRequiredEntries_Type())
rlSysmngTcamAllocMinRequiredEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngTcamAllocMinRequiredEntries.setStatus(_A)
class _RlSysmngTcamAllocStaticConfigEntries_Type(Unsigned32):defaultValue=0
_RlSysmngTcamAllocStaticConfigEntries_Type.__name__=_B
_RlSysmngTcamAllocStaticConfigEntries_Object=MibTableColumn
rlSysmngTcamAllocStaticConfigEntries=_RlSysmngTcamAllocStaticConfigEntries_Object((1,3,6,1,4,1,9,6,1,101,204,1,1,1,4),_RlSysmngTcamAllocStaticConfigEntries_Type())
rlSysmngTcamAllocStaticConfigEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngTcamAllocStaticConfigEntries.setStatus(_A)
class _RlSysmngTcamAllocInUseEntries_Type(Unsigned32):defaultValue=0
_RlSysmngTcamAllocInUseEntries_Type.__name__=_B
_RlSysmngTcamAllocInUseEntries_Object=MibTableColumn
rlSysmngTcamAllocInUseEntries=_RlSysmngTcamAllocInUseEntries_Object((1,3,6,1,4,1,9,6,1,101,204,1,1,1,5),_RlSysmngTcamAllocInUseEntries_Type())
rlSysmngTcamAllocInUseEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngTcamAllocInUseEntries.setStatus(_A)
class _RlSysmngTcamAllocPoolSize_Type(Unsigned32):defaultValue=0
_RlSysmngTcamAllocPoolSize_Type.__name__=_B
_RlSysmngTcamAllocPoolSize_Object=MibTableColumn
rlSysmngTcamAllocPoolSize=_RlSysmngTcamAllocPoolSize_Object((1,3,6,1,4,1,9,6,1,101,204,1,1,1,6),_RlSysmngTcamAllocPoolSize_Type())
rlSysmngTcamAllocPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngTcamAllocPoolSize.setStatus(_A)
_RlSysmngResource_ObjectIdentity=ObjectIdentity
rlSysmngResource=_RlSysmngResource_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,204,2))
_RlSysmngResourceTable_Object=MibTable
rlSysmngResourceTable=_RlSysmngResourceTable_Object((1,3,6,1,4,1,9,6,1,101,204,2,1))
if mibBuilder.loadTexts:rlSysmngResourceTable.setStatus(_A)
_RlSysmngResourceEntry_Object=MibTableRow
rlSysmngResourceEntry=_RlSysmngResourceEntry_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1))
rlSysmngResourceEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:rlSysmngResourceEntry.setStatus(_A)
_RlSysmngResourceRouteType_Type=SysmngResourceRouteType
_RlSysmngResourceRouteType_Object=MibTableColumn
rlSysmngResourceRouteType=_RlSysmngResourceRouteType_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,1),_RlSysmngResourceRouteType_Type())
rlSysmngResourceRouteType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSysmngResourceRouteType.setStatus(_A)
class _RlSysmngResourceCurrentUse_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentUse_Type.__name__=_B
_RlSysmngResourceCurrentUse_Object=MibTableColumn
rlSysmngResourceCurrentUse=_RlSysmngResourceCurrentUse_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,2),_RlSysmngResourceCurrentUse_Type())
rlSysmngResourceCurrentUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentUse.setStatus(_A)
class _RlSysmngResourceCurrentUseHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentUseHw_Type.__name__=_B
_RlSysmngResourceCurrentUseHw_Object=MibTableColumn
rlSysmngResourceCurrentUseHw=_RlSysmngResourceCurrentUseHw_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,3),_RlSysmngResourceCurrentUseHw_Type())
rlSysmngResourceCurrentUseHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentUseHw.setStatus(_A)
class _RlSysmngResourceCurrentMax_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentMax_Type.__name__=_B
_RlSysmngResourceCurrentMax_Object=MibTableColumn
rlSysmngResourceCurrentMax=_RlSysmngResourceCurrentMax_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,4),_RlSysmngResourceCurrentMax_Type())
rlSysmngResourceCurrentMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentMax.setStatus(_A)
class _RlSysmngResourceCurrentMaxHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentMaxHw_Type.__name__=_B
_RlSysmngResourceCurrentMaxHw_Object=MibTableColumn
rlSysmngResourceCurrentMaxHw=_RlSysmngResourceCurrentMaxHw_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,5),_RlSysmngResourceCurrentMaxHw_Type())
rlSysmngResourceCurrentMaxHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentMaxHw.setStatus(_A)
class _RlSysmngResourceTemporaryMax_Type(Unsigned32):defaultValue=0
_RlSysmngResourceTemporaryMax_Type.__name__=_B
_RlSysmngResourceTemporaryMax_Object=MibTableColumn
rlSysmngResourceTemporaryMax=_RlSysmngResourceTemporaryMax_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,6),_RlSysmngResourceTemporaryMax_Type())
rlSysmngResourceTemporaryMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceTemporaryMax.setStatus(_A)
class _RlSysmngResourceTemporaryMaxHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourceTemporaryMaxHw_Type.__name__=_B
_RlSysmngResourceTemporaryMaxHw_Object=MibTableColumn
rlSysmngResourceTemporaryMaxHw=_RlSysmngResourceTemporaryMaxHw_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,7),_RlSysmngResourceTemporaryMaxHw_Type())
rlSysmngResourceTemporaryMaxHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceTemporaryMaxHw.setStatus(_A)
class _RlSysmngResourceCurrentNexthopMax_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentNexthopMax_Type.__name__=_B
_RlSysmngResourceCurrentNexthopMax_Object=MibTableColumn
rlSysmngResourceCurrentNexthopMax=_RlSysmngResourceCurrentNexthopMax_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,8),_RlSysmngResourceCurrentNexthopMax_Type())
rlSysmngResourceCurrentNexthopMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentNexthopMax.setStatus(_A)
class _RlSysmngResourceCurrentNexthopMaxHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentNexthopMaxHw_Type.__name__=_B
_RlSysmngResourceCurrentNexthopMaxHw_Object=MibTableColumn
rlSysmngResourceCurrentNexthopMaxHw=_RlSysmngResourceCurrentNexthopMaxHw_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,9),_RlSysmngResourceCurrentNexthopMaxHw_Type())
rlSysmngResourceCurrentNexthopMaxHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentNexthopMaxHw.setStatus(_A)
class _RlSysmngResourceCurrentNexthopUse_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentNexthopUse_Type.__name__=_B
_RlSysmngResourceCurrentNexthopUse_Object=MibTableColumn
rlSysmngResourceCurrentNexthopUse=_RlSysmngResourceCurrentNexthopUse_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,10),_RlSysmngResourceCurrentNexthopUse_Type())
rlSysmngResourceCurrentNexthopUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentNexthopUse.setStatus(_A)
class _RlSysmngResourceCurrentNexthopUseHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourceCurrentNexthopUseHw_Type.__name__=_B
_RlSysmngResourceCurrentNexthopUseHw_Object=MibTableColumn
rlSysmngResourceCurrentNexthopUseHw=_RlSysmngResourceCurrentNexthopUseHw_Object((1,3,6,1,4,1,9,6,1,101,204,2,1,1,11),_RlSysmngResourceCurrentNexthopUseHw_Type())
rlSysmngResourceCurrentNexthopUseHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceCurrentNexthopUseHw.setStatus(_A)
_RlSysmngRouterResourceAction_Type=Integer32
_RlSysmngRouterResourceAction_Object=MibScalar
rlSysmngRouterResourceAction=_RlSysmngRouterResourceAction_Object((1,3,6,1,4,1,9,6,1,101,204,3),_RlSysmngRouterResourceAction_Type())
rlSysmngRouterResourceAction.setMaxAccess(_K)
if mibBuilder.loadTexts:rlSysmngRouterResourceAction.setStatus(_A)
_RlSysmngResourceUsage_ObjectIdentity=ObjectIdentity
rlSysmngResourceUsage=_RlSysmngResourceUsage_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,204,4))
_RlSysmngResourceUsageTable_Object=MibTable
rlSysmngResourceUsageTable=_RlSysmngResourceUsageTable_Object((1,3,6,1,4,1,9,6,1,101,204,4,1))
if mibBuilder.loadTexts:rlSysmngResourceUsageTable.setStatus(_A)
_RlSysmngResourceUsageEntry_Object=MibTableRow
rlSysmngResourceUsageEntry=_RlSysmngResourceUsageEntry_Object((1,3,6,1,4,1,9,6,1,101,204,4,1,1))
rlSysmngResourceUsageEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:rlSysmngResourceUsageEntry.setStatus(_A)
_RlSysmngResourceUsageType_Type=SysmngResourceRouteUsageType
_RlSysmngResourceUsageType_Object=MibTableColumn
rlSysmngResourceUsageType=_RlSysmngResourceUsageType_Object((1,3,6,1,4,1,9,6,1,101,204,4,1,1,1),_RlSysmngResourceUsageType_Type())
rlSysmngResourceUsageType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSysmngResourceUsageType.setStatus(_A)
class _RlSysmngResourceUsageNum_Type(Unsigned32):defaultValue=0
_RlSysmngResourceUsageNum_Type.__name__=_B
_RlSysmngResourceUsageNum_Object=MibTableColumn
rlSysmngResourceUsageNum=_RlSysmngResourceUsageNum_Object((1,3,6,1,4,1,9,6,1,101,204,4,1,1,2),_RlSysmngResourceUsageNum_Type())
rlSysmngResourceUsageNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourceUsageNum.setStatus(_A)
_RlSysmngResourcePerUnit_ObjectIdentity=ObjectIdentity
rlSysmngResourcePerUnit=_RlSysmngResourcePerUnit_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,204,5))
_RlSysmngResourcePerUnitTable_Object=MibTable
rlSysmngResourcePerUnitTable=_RlSysmngResourcePerUnitTable_Object((1,3,6,1,4,1,9,6,1,101,204,5,1))
if mibBuilder.loadTexts:rlSysmngResourcePerUnitTable.setStatus(_A)
_RlSysmngResourcePerUnitEntry_Object=MibTableRow
rlSysmngResourcePerUnitEntry=_RlSysmngResourcePerUnitEntry_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1))
rlSysmngResourcePerUnitEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:rlSysmngResourcePerUnitEntry.setStatus(_A)
_RlSysmngResourcePerUnitRouteType_Type=SysmngResourceRouteType
_RlSysmngResourcePerUnitRouteType_Object=MibTableColumn
rlSysmngResourcePerUnitRouteType=_RlSysmngResourcePerUnitRouteType_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,1),_RlSysmngResourcePerUnitRouteType_Type())
rlSysmngResourcePerUnitRouteType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitRouteType.setStatus(_A)
_RlSysmngResourcePerUnitUnitId_Type=Unsigned32
_RlSysmngResourcePerUnitUnitId_Object=MibTableColumn
rlSysmngResourcePerUnitUnitId=_RlSysmngResourcePerUnitUnitId_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,2),_RlSysmngResourcePerUnitUnitId_Type())
rlSysmngResourcePerUnitUnitId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitUnitId.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentUse_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentUse_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentUse_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentUse=_RlSysmngResourcePerUnitCurrentUse_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,3),_RlSysmngResourcePerUnitCurrentUse_Type())
rlSysmngResourcePerUnitCurrentUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentUse.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentUseHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentUseHw_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentUseHw_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentUseHw=_RlSysmngResourcePerUnitCurrentUseHw_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,4),_RlSysmngResourcePerUnitCurrentUseHw_Type())
rlSysmngResourcePerUnitCurrentUseHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentUseHw.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentMax_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentMax_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentMax_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentMax=_RlSysmngResourcePerUnitCurrentMax_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,5),_RlSysmngResourcePerUnitCurrentMax_Type())
rlSysmngResourcePerUnitCurrentMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentMax.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentMaxHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentMaxHw_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentMaxHw_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentMaxHw=_RlSysmngResourcePerUnitCurrentMaxHw_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,6),_RlSysmngResourcePerUnitCurrentMaxHw_Type())
rlSysmngResourcePerUnitCurrentMaxHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentMaxHw.setStatus(_A)
class _RlSysmngResourcePerUnitTemporaryMax_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitTemporaryMax_Type.__name__=_B
_RlSysmngResourcePerUnitTemporaryMax_Object=MibTableColumn
rlSysmngResourcePerUnitTemporaryMax=_RlSysmngResourcePerUnitTemporaryMax_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,7),_RlSysmngResourcePerUnitTemporaryMax_Type())
rlSysmngResourcePerUnitTemporaryMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitTemporaryMax.setStatus(_A)
class _RlSysmngResourcePerUnitTemporaryMaxHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitTemporaryMaxHw_Type.__name__=_B
_RlSysmngResourcePerUnitTemporaryMaxHw_Object=MibTableColumn
rlSysmngResourcePerUnitTemporaryMaxHw=_RlSysmngResourcePerUnitTemporaryMaxHw_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,8),_RlSysmngResourcePerUnitTemporaryMaxHw_Type())
rlSysmngResourcePerUnitTemporaryMaxHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitTemporaryMaxHw.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentNexthopMax_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentNexthopMax_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentNexthopMax_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopMax=_RlSysmngResourcePerUnitCurrentNexthopMax_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,9),_RlSysmngResourcePerUnitCurrentNexthopMax_Type())
rlSysmngResourcePerUnitCurrentNexthopMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentNexthopMax.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentNexthopMaxHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentNexthopMaxHw_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentNexthopMaxHw_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopMaxHw=_RlSysmngResourcePerUnitCurrentNexthopMaxHw_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,10),_RlSysmngResourcePerUnitCurrentNexthopMaxHw_Type())
rlSysmngResourcePerUnitCurrentNexthopMaxHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentNexthopMaxHw.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentNexthopUse_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentNexthopUse_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentNexthopUse_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopUse=_RlSysmngResourcePerUnitCurrentNexthopUse_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,11),_RlSysmngResourcePerUnitCurrentNexthopUse_Type())
rlSysmngResourcePerUnitCurrentNexthopUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentNexthopUse.setStatus(_A)
class _RlSysmngResourcePerUnitCurrentNexthopUseHw_Type(Unsigned32):defaultValue=0
_RlSysmngResourcePerUnitCurrentNexthopUseHw_Type.__name__=_B
_RlSysmngResourcePerUnitCurrentNexthopUseHw_Object=MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopUseHw=_RlSysmngResourcePerUnitCurrentNexthopUseHw_Object((1,3,6,1,4,1,9,6,1,101,204,5,1,1,12),_RlSysmngResourcePerUnitCurrentNexthopUseHw_Type())
rlSysmngResourcePerUnitCurrentNexthopUseHw.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSysmngResourcePerUnitCurrentNexthopUseHw.setStatus(_A)
class _RlRouterHwReactivate_Type(Integer32):defaultValue=0
_RlRouterHwReactivate_Type.__name__=_F
_RlRouterHwReactivate_Object=MibScalar
rlRouterHwReactivate=_RlRouterHwReactivate_Object((1,3,6,1,4,1,9,6,1,101,204,6),_RlRouterHwReactivate_Type())
rlRouterHwReactivate.setMaxAccess(_K)
if mibBuilder.loadTexts:rlRouterHwReactivate.setStatus(_A)
class _RlRouterHwStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('inRecovery',2),('suspended',3)))
_RlRouterHwStatus_Type.__name__=_F
_RlRouterHwStatus_Object=MibScalar
rlRouterHwStatus=_RlRouterHwStatus_Object((1,3,6,1,4,1,9,6,1,101,204,7),_RlRouterHwStatus_Type())
rlRouterHwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRouterHwStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SysmngResourceRouteType':SysmngResourceRouteType,'SysmngResourceRouteUsageType':SysmngResourceRouteUsageType,'SysmngPoolType':SysmngPoolType,'rlSysmngMib':rlSysmngMib,'rlSysmngTcamAllocations':rlSysmngTcamAllocations,'rlSysmngTcamAllocationsTable':rlSysmngTcamAllocationsTable,'rlSysmngTcamAllocationsEntry':rlSysmngTcamAllocationsEntry,_H:rlSysmngTcamAllocProfileName,_I:rlSysmngTcamAllocPoolType,'rlSysmngTcamAllocMinRequiredEntries':rlSysmngTcamAllocMinRequiredEntries,'rlSysmngTcamAllocStaticConfigEntries':rlSysmngTcamAllocStaticConfigEntries,'rlSysmngTcamAllocInUseEntries':rlSysmngTcamAllocInUseEntries,'rlSysmngTcamAllocPoolSize':rlSysmngTcamAllocPoolSize,'rlSysmngResource':rlSysmngResource,'rlSysmngResourceTable':rlSysmngResourceTable,'rlSysmngResourceEntry':rlSysmngResourceEntry,_J:rlSysmngResourceRouteType,'rlSysmngResourceCurrentUse':rlSysmngResourceCurrentUse,'rlSysmngResourceCurrentUseHw':rlSysmngResourceCurrentUseHw,'rlSysmngResourceCurrentMax':rlSysmngResourceCurrentMax,'rlSysmngResourceCurrentMaxHw':rlSysmngResourceCurrentMaxHw,'rlSysmngResourceTemporaryMax':rlSysmngResourceTemporaryMax,'rlSysmngResourceTemporaryMaxHw':rlSysmngResourceTemporaryMaxHw,'rlSysmngResourceCurrentNexthopMax':rlSysmngResourceCurrentNexthopMax,'rlSysmngResourceCurrentNexthopMaxHw':rlSysmngResourceCurrentNexthopMaxHw,'rlSysmngResourceCurrentNexthopUse':rlSysmngResourceCurrentNexthopUse,'rlSysmngResourceCurrentNexthopUseHw':rlSysmngResourceCurrentNexthopUseHw,'rlSysmngRouterResourceAction':rlSysmngRouterResourceAction,'rlSysmngResourceUsage':rlSysmngResourceUsage,'rlSysmngResourceUsageTable':rlSysmngResourceUsageTable,'rlSysmngResourceUsageEntry':rlSysmngResourceUsageEntry,_L:rlSysmngResourceUsageType,'rlSysmngResourceUsageNum':rlSysmngResourceUsageNum,'rlSysmngResourcePerUnit':rlSysmngResourcePerUnit,'rlSysmngResourcePerUnitTable':rlSysmngResourcePerUnitTable,'rlSysmngResourcePerUnitEntry':rlSysmngResourcePerUnitEntry,_M:rlSysmngResourcePerUnitRouteType,_N:rlSysmngResourcePerUnitUnitId,'rlSysmngResourcePerUnitCurrentUse':rlSysmngResourcePerUnitCurrentUse,'rlSysmngResourcePerUnitCurrentUseHw':rlSysmngResourcePerUnitCurrentUseHw,'rlSysmngResourcePerUnitCurrentMax':rlSysmngResourcePerUnitCurrentMax,'rlSysmngResourcePerUnitCurrentMaxHw':rlSysmngResourcePerUnitCurrentMaxHw,'rlSysmngResourcePerUnitTemporaryMax':rlSysmngResourcePerUnitTemporaryMax,'rlSysmngResourcePerUnitTemporaryMaxHw':rlSysmngResourcePerUnitTemporaryMaxHw,'rlSysmngResourcePerUnitCurrentNexthopMax':rlSysmngResourcePerUnitCurrentNexthopMax,'rlSysmngResourcePerUnitCurrentNexthopMaxHw':rlSysmngResourcePerUnitCurrentNexthopMaxHw,'rlSysmngResourcePerUnitCurrentNexthopUse':rlSysmngResourcePerUnitCurrentNexthopUse,'rlSysmngResourcePerUnitCurrentNexthopUseHw':rlSysmngResourcePerUnitCurrentNexthopUseHw,'rlRouterHwReactivate':rlRouterHwReactivate,'rlRouterHwStatus':rlRouterHwStatus})