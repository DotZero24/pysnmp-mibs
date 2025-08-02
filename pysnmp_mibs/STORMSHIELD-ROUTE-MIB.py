_E='snsRouteIndex'
_D='STORMSHIELD-ROUTE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsRoute=ModuleIdentity((1,3,6,1,4,1,11256,1,14))
if mibBuilder.loadTexts:snsRoute.setRevisions(('2017-02-20 00:00',))
_SnsRouteTable_Object=MibTable
snsRouteTable=_SnsRouteTable_Object((1,3,6,1,4,1,11256,1,14,1))
if mibBuilder.loadTexts:snsRouteTable.setStatus(_A)
_SnsRouteEntry_Object=MibTableRow
snsRouteEntry=_SnsRouteEntry_Object((1,3,6,1,4,1,11256,1,14,1,1))
snsRouteEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsRouteEntry.setStatus(_A)
class _SnsRouteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnsRouteIndex_Type.__name__=_C
_SnsRouteIndex_Object=MibTableColumn
snsRouteIndex=_SnsRouteIndex_Object((1,3,6,1,4,1,11256,1,14,1,1,1),_SnsRouteIndex_Type())
snsRouteIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteIndex.setStatus(_A)
_SnsRouteType_Type=DisplayString
_SnsRouteType_Object=MibTableColumn
snsRouteType=_SnsRouteType_Object((1,3,6,1,4,1,11256,1,14,1,1,2),_SnsRouteType_Type())
snsRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteType.setStatus(_A)
_SnsRouteIPVersion_Type=Integer32
_SnsRouteIPVersion_Object=MibTableColumn
snsRouteIPVersion=_SnsRouteIPVersion_Object((1,3,6,1,4,1,11256,1,14,1,1,3),_SnsRouteIPVersion_Type())
snsRouteIPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteIPVersion.setStatus(_A)
_SnsRouteRouterName_Type=SnmpAdminString
_SnsRouteRouterName_Object=MibTableColumn
snsRouteRouterName=_SnsRouteRouterName_Object((1,3,6,1,4,1,11256,1,14,1,1,4),_SnsRouteRouterName_Type())
snsRouteRouterName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteRouterName.setStatus(_A)
_SnsRouteGatewayName_Type=SnmpAdminString
_SnsRouteGatewayName_Object=MibTableColumn
snsRouteGatewayName=_SnsRouteGatewayName_Object((1,3,6,1,4,1,11256,1,14,1,1,5),_SnsRouteGatewayName_Type())
snsRouteGatewayName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteGatewayName.setStatus(_A)
_SnsRouteGatewayAddr_Type=DisplayString
_SnsRouteGatewayAddr_Object=MibTableColumn
snsRouteGatewayAddr=_SnsRouteGatewayAddr_Object((1,3,6,1,4,1,11256,1,14,1,1,6),_SnsRouteGatewayAddr_Type())
snsRouteGatewayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteGatewayAddr.setStatus(_A)
_SnsRouteGatewayType_Type=DisplayString
_SnsRouteGatewayType_Object=MibTableColumn
snsRouteGatewayType=_SnsRouteGatewayType_Object((1,3,6,1,4,1,11256,1,14,1,1,7),_SnsRouteGatewayType_Type())
snsRouteGatewayType.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteGatewayType.setStatus(_A)
_SnsRouteLastCheck_Type=DisplayString
_SnsRouteLastCheck_Object=MibTableColumn
snsRouteLastCheck=_SnsRouteLastCheck_Object((1,3,6,1,4,1,11256,1,14,1,1,8),_SnsRouteLastCheck_Type())
snsRouteLastCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteLastCheck.setStatus(_A)
_SnsRouteState_Type=DisplayString
_SnsRouteState_Object=MibTableColumn
snsRouteState=_SnsRouteState_Object((1,3,6,1,4,1,11256,1,14,1,1,9),_SnsRouteState_Type())
snsRouteState.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteState.setStatus(_A)
_SnsRouteStateLastChange_Type=DisplayString
_SnsRouteStateLastChange_Object=MibTableColumn
snsRouteStateLastChange=_SnsRouteStateLastChange_Object((1,3,6,1,4,1,11256,1,14,1,1,10),_SnsRouteStateLastChange_Type())
snsRouteStateLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteStateLastChange.setStatus(_A)
_SnsRouteActive_Type=Integer32
_SnsRouteActive_Object=MibTableColumn
snsRouteActive=_SnsRouteActive_Object((1,3,6,1,4,1,11256,1,14,1,1,11),_SnsRouteActive_Type())
snsRouteActive.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteActive.setStatus(_A)
_SnsRouteActiveLastChange_Type=DisplayString
_SnsRouteActiveLastChange_Object=MibTableColumn
snsRouteActiveLastChange=_SnsRouteActiveLastChange_Object((1,3,6,1,4,1,11256,1,14,1,1,12),_SnsRouteActiveLastChange_Type())
snsRouteActiveLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteActiveLastChange.setStatus(_A)
_SnsRouteSysDefaultGateway_Type=Integer32
_SnsRouteSysDefaultGateway_Object=MibTableColumn
snsRouteSysDefaultGateway=_SnsRouteSysDefaultGateway_Object((1,3,6,1,4,1,11256,1,14,1,1,13),_SnsRouteSysDefaultGateway_Type())
snsRouteSysDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteSysDefaultGateway.setStatus(_A)
_SnsRouteSysDefaultGatewayLastChange_Type=DisplayString
_SnsRouteSysDefaultGatewayLastChange_Object=MibTableColumn
snsRouteSysDefaultGatewayLastChange=_SnsRouteSysDefaultGatewayLastChange_Object((1,3,6,1,4,1,11256,1,14,1,1,14),_SnsRouteSysDefaultGatewayLastChange_Type())
snsRouteSysDefaultGatewayLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteSysDefaultGatewayLastChange.setStatus(_A)
_SnsRouteRtid_Type=Integer32
_SnsRouteRtid_Object=MibTableColumn
snsRouteRtid=_SnsRouteRtid_Object((1,3,6,1,4,1,11256,1,14,1,1,15),_SnsRouteRtid_Type())
snsRouteRtid.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteRtid.setStatus(_A)
_SnsRouteUsagePrct_Type=DisplayString
_SnsRouteUsagePrct_Object=MibTableColumn
snsRouteUsagePrct=_SnsRouteUsagePrct_Object((1,3,6,1,4,1,11256,1,14,1,1,16),_SnsRouteUsagePrct_Type())
snsRouteUsagePrct.setMaxAccess(_B)
if mibBuilder.loadTexts:snsRouteUsagePrct.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsRoute':snsRoute,'snsRouteTable':snsRouteTable,'snsRouteEntry':snsRouteEntry,_E:snsRouteIndex,'snsRouteType':snsRouteType,'snsRouteIPVersion':snsRouteIPVersion,'snsRouteRouterName':snsRouteRouterName,'snsRouteGatewayName':snsRouteGatewayName,'snsRouteGatewayAddr':snsRouteGatewayAddr,'snsRouteGatewayType':snsRouteGatewayType,'snsRouteLastCheck':snsRouteLastCheck,'snsRouteState':snsRouteState,'snsRouteStateLastChange':snsRouteStateLastChange,'snsRouteActive':snsRouteActive,'snsRouteActiveLastChange':snsRouteActiveLastChange,'snsRouteSysDefaultGateway':snsRouteSysDefaultGateway,'snsRouteSysDefaultGatewayLastChange':snsRouteSysDefaultGatewayLastChange,'snsRouteRtid':snsRouteRtid,'snsRouteUsagePrct':snsRouteUsagePrct})