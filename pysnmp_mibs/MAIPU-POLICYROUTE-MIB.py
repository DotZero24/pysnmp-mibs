_E='policyRouteIfindex'
_D='MAIPU-POLICYROUTE-MIB'
_C='read-write'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_B,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
policyRoute=ModuleIdentity((1,3,6,1,4,1,5651,3,81,6))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RouteMib_ObjectIdentity=ObjectIdentity
routeMib=_RouteMib_ObjectIdentity((1,3,6,1,4,1,5651,3,81))
class _PolicyRouteLocal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PolicyRouteLocal_Type.__name__=_B
_PolicyRouteLocal_Object=MibScalar
policyRouteLocal=_PolicyRouteLocal_Object((1,3,6,1,4,1,5651,3,81,6,1),_PolicyRouteLocal_Type())
policyRouteLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:policyRouteLocal.setStatus(_A)
_PolicyRouteTable_Object=MibTable
policyRouteTable=_PolicyRouteTable_Object((1,3,6,1,4,1,5651,3,81,6,2))
if mibBuilder.loadTexts:policyRouteTable.setStatus(_A)
_PolicyRouteEntry_Object=MibTableRow
policyRouteEntry=_PolicyRouteEntry_Object((1,3,6,1,4,1,5651,3,81,6,2,1))
policyRouteEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:policyRouteEntry.setStatus(_A)
_PolicyRouteIfindex_Type=Unsigned32
_PolicyRouteIfindex_Object=MibTableColumn
policyRouteIfindex=_PolicyRouteIfindex_Object((1,3,6,1,4,1,5651,3,81,6,2,1,1),_PolicyRouteIfindex_Type())
policyRouteIfindex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:policyRouteIfindex.setStatus(_A)
class _PolicyRouteRoutemap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PolicyRouteRoutemap_Type.__name__=_B
_PolicyRouteRoutemap_Object=MibTableColumn
policyRouteRoutemap=_PolicyRouteRoutemap_Object((1,3,6,1,4,1,5651,3,81,6,2,1,2),_PolicyRouteRoutemap_Type())
policyRouteRoutemap.setMaxAccess(_C)
if mibBuilder.loadTexts:policyRouteRoutemap.setStatus(_A)
_PolicyRouteCache_Type=EnabledStatus
_PolicyRouteCache_Object=MibTableColumn
policyRouteCache=_PolicyRouteCache_Object((1,3,6,1,4,1,5651,3,81,6,2,1,3),_PolicyRouteCache_Type())
policyRouteCache.setMaxAccess(_C)
if mibBuilder.loadTexts:policyRouteCache.setStatus(_A)
_PolicyRouteRowStatus_Type=RowStatus
_PolicyRouteRowStatus_Object=MibTableColumn
policyRouteRowStatus=_PolicyRouteRowStatus_Object((1,3,6,1,4,1,5651,3,81,6,2,1,4),_PolicyRouteRowStatus_Type())
policyRouteRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:policyRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'EnabledStatus':EnabledStatus,'routeMib':routeMib,'policyRoute':policyRoute,'policyRouteLocal':policyRouteLocal,'policyRouteTable':policyRouteTable,'policyRouteEntry':policyRouteEntry,_E:policyRouteIfindex,'policyRouteRoutemap':policyRouteRoutemap,'policyRouteCache':policyRouteCache,'policyRouteRowStatus':policyRouteRowStatus})