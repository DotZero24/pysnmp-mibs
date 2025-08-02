_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelIpGrpLogicalGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,1,5))
if mibBuilder.loadTexts:mitelIpGrpLogicalGroup.setRevisions(('2003-03-24 09:13','1999-03-01 00:00'))
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
_MitelIpLogGrpLogicalTable_Object=MibTable
mitelIpLogGrpLogicalTable=_MitelIpLogGrpLogicalTable_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1))
if mibBuilder.loadTexts:mitelIpLogGrpLogicalTable.setStatus(_A)
_MitelIpLogGrpLogicalEntry_Object=MibTableRow
mitelIpLogGrpLogicalEntry=_MitelIpLogGrpLogicalEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1))
mitelIpLogGrpLogicalEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mitelIpLogGrpLogicalEntry.setStatus(_A)
_MitelIpLogAdvertisementAddress_Type=IpAddress
_MitelIpLogAdvertisementAddress_Object=MibTableColumn
mitelIpLogAdvertisementAddress=_MitelIpLogAdvertisementAddress_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1,1),_MitelIpLogAdvertisementAddress_Type())
mitelIpLogAdvertisementAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpLogAdvertisementAddress.setStatus(_A)
class _MitelIpLogMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_MitelIpLogMaxAdvertisementInterval_Type.__name__=_C
_MitelIpLogMaxAdvertisementInterval_Object=MibTableColumn
mitelIpLogMaxAdvertisementInterval=_MitelIpLogMaxAdvertisementInterval_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1,2),_MitelIpLogMaxAdvertisementInterval_Type())
mitelIpLogMaxAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpLogMaxAdvertisementInterval.setStatus(_A)
class _MitelIpLogMinAdvertisementInterval_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_MitelIpLogMinAdvertisementInterval_Type.__name__=_C
_MitelIpLogMinAdvertisementInterval_Object=MibTableColumn
mitelIpLogMinAdvertisementInterval=_MitelIpLogMinAdvertisementInterval_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1,3),_MitelIpLogMinAdvertisementInterval_Type())
mitelIpLogMinAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpLogMinAdvertisementInterval.setStatus(_A)
class _MitelIpLogAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,9000))
_MitelIpLogAdvertisementLifetime_Type.__name__=_C
_MitelIpLogAdvertisementLifetime_Object=MibTableColumn
mitelIpLogAdvertisementLifetime=_MitelIpLogAdvertisementLifetime_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1,4),_MitelIpLogAdvertisementLifetime_Type())
mitelIpLogAdvertisementLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpLogAdvertisementLifetime.setStatus(_A)
class _MitelIpLogPerformRouterDiscovery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MitelIpLogPerformRouterDiscovery_Type.__name__=_C
_MitelIpLogPerformRouterDiscovery_Object=MibTableColumn
mitelIpLogPerformRouterDiscovery=_MitelIpLogPerformRouterDiscovery_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1,5),_MitelIpLogPerformRouterDiscovery_Type())
mitelIpLogPerformRouterDiscovery.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpLogPerformRouterDiscovery.setStatus(_A)
_MitelIpLogSolicitationAddress_Type=IpAddress
_MitelIpLogSolicitationAddress_Object=MibTableColumn
mitelIpLogSolicitationAddress=_MitelIpLogSolicitationAddress_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1,6),_MitelIpLogSolicitationAddress_Type())
mitelIpLogSolicitationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpLogSolicitationAddress.setStatus(_A)
_MitelIpLogStatus_Type=RowStatus
_MitelIpLogStatus_Object=MibTableColumn
mitelIpLogStatus=_MitelIpLogStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,5,1,1,7),_MitelIpLogStatus_Type())
mitelIpLogStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelIpLogStatus.setStatus(_A)
mibBuilder.exportSymbols('MITEL-IPLOGICAL-MIB',**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterIpGroup':mitelRouterIpGroup,'mitelIpGrpLogicalGroup':mitelIpGrpLogicalGroup,'mitelIpLogGrpLogicalTable':mitelIpLogGrpLogicalTable,'mitelIpLogGrpLogicalEntry':mitelIpLogGrpLogicalEntry,'mitelIpLogAdvertisementAddress':mitelIpLogAdvertisementAddress,'mitelIpLogMaxAdvertisementInterval':mitelIpLogMaxAdvertisementInterval,'mitelIpLogMinAdvertisementInterval':mitelIpLogMinAdvertisementInterval,'mitelIpLogAdvertisementLifetime':mitelIpLogAdvertisementLifetime,'mitelIpLogPerformRouterDiscovery':mitelIpLogPerformRouterDiscovery,'mitelIpLogSolicitationAddress':mitelIpLogSolicitationAddress,'mitelIpLogStatus':mitelIpLogStatus})