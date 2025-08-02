_D='rip2IfConfAddress'
_C='RIPv2-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rip2IfConfAddress,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelRouterRipExtensionGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,6))
if mibBuilder.loadTexts:mitelRouterRipExtensionGroup.setRevisions(('2003-03-24 10:36','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelRipExtGrpIfConfTable_Object=MibTable
mitelRipExtGrpIfConfTable=_MitelRipExtGrpIfConfTable_Object((1,3,6,1,4,1,1027,4,8,1,6,1))
if mibBuilder.loadTexts:mitelRipExtGrpIfConfTable.setStatus(_A)
_MitelRipExtGrpIfConfEntry_Object=MibTableRow
mitelRipExtGrpIfConfEntry=_MitelRipExtGrpIfConfEntry_Object((1,3,6,1,4,1,1027,4,8,1,6,1,1))
mitelRipExtGrpIfConfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mitelRipExtGrpIfConfEntry.setStatus(_A)
class _MitelIfConfTblSendDefaultRoutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MitelIfConfTblSendDefaultRoutes_Type.__name__=_B
_MitelIfConfTblSendDefaultRoutes_Object=MibTableColumn
mitelIfConfTblSendDefaultRoutes=_MitelIfConfTblSendDefaultRoutes_Object((1,3,6,1,4,1,1027,4,8,1,6,1,1,1),_MitelIfConfTblSendDefaultRoutes_Type())
mitelIfConfTblSendDefaultRoutes.setMaxAccess('read-write')
if mibBuilder.loadTexts:mitelIfConfTblSendDefaultRoutes.setStatus(_A)
class _MitelIfConfTblRipType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rip',1),('triggerRip',2)))
_MitelIfConfTblRipType_Type.__name__=_B
_MitelIfConfTblRipType_Object=MibTableColumn
mitelIfConfTblRipType=_MitelIfConfTblRipType_Object((1,3,6,1,4,1,1027,4,8,1,6,1,1,2),_MitelIfConfTblRipType_Type())
mitelIfConfTblRipType.setMaxAccess('read-only')
if mibBuilder.loadTexts:mitelIfConfTblRipType.setStatus(_A)
_MitelIfConfTblRowStatus_Type=RowStatus
_MitelIfConfTblRowStatus_Object=MibTableColumn
mitelIfConfTblRowStatus=_MitelIfConfTblRowStatus_Object((1,3,6,1,4,1,1027,4,8,1,6,1,1,3),_MitelIfConfTblRowStatus_Type())
mitelIfConfTblRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelIfConfTblRowStatus.setStatus(_A)
mibBuilder.exportSymbols('MITEL-RIP2EXTENSION-MIB',**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterRipExtensionGroup':mitelRouterRipExtensionGroup,'mitelRipExtGrpIfConfTable':mitelRipExtGrpIfConfTable,'mitelRipExtGrpIfConfEntry':mitelRipExtGrpIfConfEntry,'mitelIfConfTblSendDefaultRoutes':mitelIfConfTblSendDefaultRoutes,'mitelIfConfTblRipType':mitelIfConfTblRipType,'mitelIfConfTblRowStatus':mitelIfConfTblRowStatus})