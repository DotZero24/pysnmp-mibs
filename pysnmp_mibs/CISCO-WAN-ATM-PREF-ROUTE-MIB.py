_M='cwaPrefRouteMIBGroups'
_L='cwaPrefRouteNwElemRowStatus'
_K='cwaPrefRouteNwElemPortId'
_J='cwaPrefRouteNwElemNodeId'
_I='cwaPrefRouteRowStatus'
_H='cwaPrefRouteNwElemCount'
_G='cwaPrefRouteNwElemPos'
_F='not-accessible'
_E='cwaPrefRouteId'
_D='Unsigned32'
_C='read-create'
_B='CISCO-WAN-ATM-PREF-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PnniNodeId,PnniPortId=mibBuilder.importSymbols('PNNI-MIB','PnniNodeId','PnniPortId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoWanATMPrefRouteMIB=ModuleIdentity((1,3,6,1,4,1,9,9,99996))
if mibBuilder.loadTexts:ciscoWanATMPrefRouteMIB.setRevisions(('2002-06-25 00:00',))
class RouteId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoWanATMPrefRouteMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWanATMPrefRouteMIBNotifs=_CiscoWanATMPrefRouteMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,99996,0))
_CiscoWanATMPrefRouteMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanATMPrefRouteMIBObjects=_CiscoWanATMPrefRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,99996,1))
_CwaPrefRouteConfTable_Object=MibTable
cwaPrefRouteConfTable=_CwaPrefRouteConfTable_Object((1,3,6,1,4,1,9,9,99996,1,1))
if mibBuilder.loadTexts:cwaPrefRouteConfTable.setStatus(_A)
_CwaPrefRouteConfEntry_Object=MibTableRow
cwaPrefRouteConfEntry=_CwaPrefRouteConfEntry_Object((1,3,6,1,4,1,9,9,99996,1,1,1))
cwaPrefRouteConfEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cwaPrefRouteConfEntry.setStatus(_A)
_CwaPrefRouteId_Type=RouteId
_CwaPrefRouteId_Object=MibTableColumn
cwaPrefRouteId=_CwaPrefRouteId_Object((1,3,6,1,4,1,9,9,99996,1,1,1,1),_CwaPrefRouteId_Type())
cwaPrefRouteId.setMaxAccess(_F)
if mibBuilder.loadTexts:cwaPrefRouteId.setStatus(_A)
class _CwaPrefRouteNwElemCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CwaPrefRouteNwElemCount_Type.__name__=_D
_CwaPrefRouteNwElemCount_Object=MibTableColumn
cwaPrefRouteNwElemCount=_CwaPrefRouteNwElemCount_Object((1,3,6,1,4,1,9,9,99996,1,1,1,2),_CwaPrefRouteNwElemCount_Type())
cwaPrefRouteNwElemCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaPrefRouteNwElemCount.setStatus(_A)
_CwaPrefRouteRowStatus_Type=RowStatus
_CwaPrefRouteRowStatus_Object=MibTableColumn
cwaPrefRouteRowStatus=_CwaPrefRouteRowStatus_Object((1,3,6,1,4,1,9,9,99996,1,1,1,3),_CwaPrefRouteRowStatus_Type())
cwaPrefRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaPrefRouteRowStatus.setStatus(_A)
_CwaPrefRouteNwElemTable_Object=MibTable
cwaPrefRouteNwElemTable=_CwaPrefRouteNwElemTable_Object((1,3,6,1,4,1,9,9,99996,1,2))
if mibBuilder.loadTexts:cwaPrefRouteNwElemTable.setStatus(_A)
_CwaPrefRouteNwElemEntry_Object=MibTableRow
cwaPrefRouteNwElemEntry=_CwaPrefRouteNwElemEntry_Object((1,3,6,1,4,1,9,9,99996,1,2,1))
cwaPrefRouteNwElemEntry.setIndexNames((0,_B,_E),(0,_B,_G))
if mibBuilder.loadTexts:cwaPrefRouteNwElemEntry.setStatus(_A)
class _CwaPrefRouteNwElemPos_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CwaPrefRouteNwElemPos_Type.__name__=_D
_CwaPrefRouteNwElemPos_Object=MibTableColumn
cwaPrefRouteNwElemPos=_CwaPrefRouteNwElemPos_Object((1,3,6,1,4,1,9,9,99996,1,2,1,1),_CwaPrefRouteNwElemPos_Type())
cwaPrefRouteNwElemPos.setMaxAccess(_F)
if mibBuilder.loadTexts:cwaPrefRouteNwElemPos.setStatus(_A)
_CwaPrefRouteNwElemNodeId_Type=PnniNodeId
_CwaPrefRouteNwElemNodeId_Object=MibTableColumn
cwaPrefRouteNwElemNodeId=_CwaPrefRouteNwElemNodeId_Object((1,3,6,1,4,1,9,9,99996,1,2,1,2),_CwaPrefRouteNwElemNodeId_Type())
cwaPrefRouteNwElemNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaPrefRouteNwElemNodeId.setStatus(_A)
_CwaPrefRouteNwElemPortId_Type=PnniPortId
_CwaPrefRouteNwElemPortId_Object=MibTableColumn
cwaPrefRouteNwElemPortId=_CwaPrefRouteNwElemPortId_Object((1,3,6,1,4,1,9,9,99996,1,2,1,3),_CwaPrefRouteNwElemPortId_Type())
cwaPrefRouteNwElemPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaPrefRouteNwElemPortId.setStatus(_A)
_CwaPrefRouteNwElemRowStatus_Type=RowStatus
_CwaPrefRouteNwElemRowStatus_Object=MibTableColumn
cwaPrefRouteNwElemRowStatus=_CwaPrefRouteNwElemRowStatus_Object((1,3,6,1,4,1,9,9,99996,1,2,1,4),_CwaPrefRouteNwElemRowStatus_Type())
cwaPrefRouteNwElemRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaPrefRouteNwElemRowStatus.setStatus(_A)
_CwaPrefRouteConformance_ObjectIdentity=ObjectIdentity
cwaPrefRouteConformance=_CwaPrefRouteConformance_ObjectIdentity((1,3,6,1,4,1,9,9,99996,2))
_CwaPrefRouteCompliances_ObjectIdentity=ObjectIdentity
cwaPrefRouteCompliances=_CwaPrefRouteCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,99996,2,1))
_CwaPrefMIBGroups_ObjectIdentity=ObjectIdentity
cwaPrefMIBGroups=_CwaPrefMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,99996,2,2))
cwaPrefRouteMIBGroups=ObjectGroup((1,3,6,1,4,1,9,9,99996,2,2,1))
cwaPrefRouteMIBGroups.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cwaPrefRouteMIBGroups.setStatus(_A)
cwaPrefMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,99996,2,1,1))
cwaPrefMIBCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:cwaPrefMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RouteId':RouteId,'ciscoWanATMPrefRouteMIB':ciscoWanATMPrefRouteMIB,'ciscoWanATMPrefRouteMIBNotifs':ciscoWanATMPrefRouteMIBNotifs,'ciscoWanATMPrefRouteMIBObjects':ciscoWanATMPrefRouteMIBObjects,'cwaPrefRouteConfTable':cwaPrefRouteConfTable,'cwaPrefRouteConfEntry':cwaPrefRouteConfEntry,_E:cwaPrefRouteId,_H:cwaPrefRouteNwElemCount,_I:cwaPrefRouteRowStatus,'cwaPrefRouteNwElemTable':cwaPrefRouteNwElemTable,'cwaPrefRouteNwElemEntry':cwaPrefRouteNwElemEntry,_G:cwaPrefRouteNwElemPos,_J:cwaPrefRouteNwElemNodeId,_K:cwaPrefRouteNwElemPortId,_L:cwaPrefRouteNwElemRowStatus,'cwaPrefRouteConformance':cwaPrefRouteConformance,'cwaPrefRouteCompliances':cwaPrefRouteCompliances,'cwaPrefMIBCompliance':cwaPrefMIBCompliance,'cwaPrefMIBGroups':cwaPrefMIBGroups,_M:cwaPrefRouteMIBGroups})