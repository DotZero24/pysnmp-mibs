_K='dot5SrRouteGroup'
_J='dot5SrRouteStatus'
_I='dot5SrRouteDescr'
_H='dot5SrRouteControl'
_G='dot5SrRouteDestination'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-create'
_B='TOKENRING-STATION-SR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
dot5SrMIB=ModuleIdentity((1,3,6,1,2,1,42))
class SourceRoute(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Dot5SrMIBObjects_ObjectIdentity=ObjectIdentity
dot5SrMIBObjects=_Dot5SrMIBObjects_ObjectIdentity((1,3,6,1,2,1,42,1))
_Dot5SrRouteTable_Object=MibTable
dot5SrRouteTable=_Dot5SrRouteTable_Object((1,3,6,1,2,1,42,1,1))
if mibBuilder.loadTexts:dot5SrRouteTable.setStatus(_A)
_Dot5SrRouteEntry_Object=MibTableRow
dot5SrRouteEntry=_Dot5SrRouteEntry_Object((1,3,6,1,2,1,42,1,1,1))
dot5SrRouteEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:dot5SrRouteEntry.setStatus(_A)
_Dot5SrRouteDestination_Type=MacAddress
_Dot5SrRouteDestination_Object=MibTableColumn
dot5SrRouteDestination=_Dot5SrRouteDestination_Object((1,3,6,1,2,1,42,1,1,1,2),_Dot5SrRouteDestination_Type())
dot5SrRouteDestination.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dot5SrRouteDestination.setStatus(_A)
class _Dot5SrRouteControl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Dot5SrRouteControl_Type.__name__=_D
_Dot5SrRouteControl_Object=MibTableColumn
dot5SrRouteControl=_Dot5SrRouteControl_Object((1,3,6,1,2,1,42,1,1,1,3),_Dot5SrRouteControl_Type())
dot5SrRouteControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dot5SrRouteControl.setStatus(_A)
_Dot5SrRouteDescr_Type=SourceRoute
_Dot5SrRouteDescr_Object=MibTableColumn
dot5SrRouteDescr=_Dot5SrRouteDescr_Object((1,3,6,1,2,1,42,1,1,1,4),_Dot5SrRouteDescr_Type())
dot5SrRouteDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:dot5SrRouteDescr.setStatus(_A)
_Dot5SrRouteStatus_Type=RowStatus
_Dot5SrRouteStatus_Object=MibTableColumn
dot5SrRouteStatus=_Dot5SrRouteStatus_Object((1,3,6,1,2,1,42,1,1,1,5),_Dot5SrRouteStatus_Type())
dot5SrRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot5SrRouteStatus.setStatus(_A)
_Dot5SrConformance_ObjectIdentity=ObjectIdentity
dot5SrConformance=_Dot5SrConformance_ObjectIdentity((1,3,6,1,2,1,42,2))
_Dot5SrGroups_ObjectIdentity=ObjectIdentity
dot5SrGroups=_Dot5SrGroups_ObjectIdentity((1,3,6,1,2,1,42,2,1))
_Dot5SrCompliances_ObjectIdentity=ObjectIdentity
dot5SrCompliances=_Dot5SrCompliances_ObjectIdentity((1,3,6,1,2,1,42,2,2))
dot5SrRouteGroup=ObjectGroup((1,3,6,1,2,1,42,2,1,1))
dot5SrRouteGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:dot5SrRouteGroup.setStatus(_A)
dot5SrCompliance=ModuleCompliance((1,3,6,1,2,1,42,2,2,1))
dot5SrCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:dot5SrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SourceRoute':SourceRoute,'dot5SrMIB':dot5SrMIB,'dot5SrMIBObjects':dot5SrMIBObjects,'dot5SrRouteTable':dot5SrRouteTable,'dot5SrRouteEntry':dot5SrRouteEntry,_G:dot5SrRouteDestination,_H:dot5SrRouteControl,_I:dot5SrRouteDescr,_J:dot5SrRouteStatus,'dot5SrConformance':dot5SrConformance,'dot5SrGroups':dot5SrGroups,_K:dot5SrRouteGroup,'dot5SrCompliances':dot5SrCompliances,'dot5SrCompliance':dot5SrCompliance})