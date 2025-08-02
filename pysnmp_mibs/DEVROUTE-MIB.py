_H='aniDevRouteMask'
_G='aniDevRouteNextHop'
_F='aniDevRouteDest'
_E='DEVROUTE-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aniDevRoute=ModuleIdentity((1,3,6,1,4,1,4325,2,9))
_AniDevRouteTable_Object=MibTable
aniDevRouteTable=_AniDevRouteTable_Object((1,3,6,1,4,1,4325,2,9,1))
if mibBuilder.loadTexts:aniDevRouteTable.setStatus(_A)
_AniDevRouteEntry_Object=MibTableRow
aniDevRouteEntry=_AniDevRouteEntry_Object((1,3,6,1,4,1,4325,2,9,1,1))
aniDevRouteEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:aniDevRouteEntry.setStatus(_A)
_AniDevRouteDest_Type=IpAddress
_AniDevRouteDest_Object=MibTableColumn
aniDevRouteDest=_AniDevRouteDest_Object((1,3,6,1,4,1,4325,2,9,1,1,1),_AniDevRouteDest_Type())
aniDevRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevRouteDest.setStatus(_A)
_AniDevRouteIfIndex_Type=Integer32
_AniDevRouteIfIndex_Object=MibTableColumn
aniDevRouteIfIndex=_AniDevRouteIfIndex_Object((1,3,6,1,4,1,4325,2,9,1,1,2),_AniDevRouteIfIndex_Type())
aniDevRouteIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteIfIndex.setStatus(_A)
_AniDevRouteMetric1_Type=Integer32
_AniDevRouteMetric1_Object=MibTableColumn
aniDevRouteMetric1=_AniDevRouteMetric1_Object((1,3,6,1,4,1,4325,2,9,1,1,3),_AniDevRouteMetric1_Type())
aniDevRouteMetric1.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteMetric1.setStatus(_A)
_AniDevRouteMetric2_Type=Integer32
_AniDevRouteMetric2_Object=MibTableColumn
aniDevRouteMetric2=_AniDevRouteMetric2_Object((1,3,6,1,4,1,4325,2,9,1,1,4),_AniDevRouteMetric2_Type())
aniDevRouteMetric2.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteMetric2.setStatus(_A)
_AniDevRouteMetric3_Type=Integer32
_AniDevRouteMetric3_Object=MibTableColumn
aniDevRouteMetric3=_AniDevRouteMetric3_Object((1,3,6,1,4,1,4325,2,9,1,1,5),_AniDevRouteMetric3_Type())
aniDevRouteMetric3.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteMetric3.setStatus(_A)
_AniDevRouteMetric4_Type=Integer32
_AniDevRouteMetric4_Object=MibTableColumn
aniDevRouteMetric4=_AniDevRouteMetric4_Object((1,3,6,1,4,1,4325,2,9,1,1,6),_AniDevRouteMetric4_Type())
aniDevRouteMetric4.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteMetric4.setStatus(_A)
_AniDevRouteNextHop_Type=IpAddress
_AniDevRouteNextHop_Object=MibTableColumn
aniDevRouteNextHop=_AniDevRouteNextHop_Object((1,3,6,1,4,1,4325,2,9,1,1,7),_AniDevRouteNextHop_Type())
aniDevRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevRouteNextHop.setStatus(_A)
class _AniDevRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('invalid',2),('direct',3),('indirect',4)))
_AniDevRouteType_Type.__name__=_D
_AniDevRouteType_Object=MibTableColumn
aniDevRouteType=_AniDevRouteType_Object((1,3,6,1,4,1,4325,2,9,1,1,8),_AniDevRouteType_Type())
aniDevRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevRouteType.setStatus(_A)
class _AniDevRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('is-is',9),('es-is',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14)))
_AniDevRouteProto_Type.__name__=_D
_AniDevRouteProto_Object=MibTableColumn
aniDevRouteProto=_AniDevRouteProto_Object((1,3,6,1,4,1,4325,2,9,1,1,9),_AniDevRouteProto_Type())
aniDevRouteProto.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteProto.setStatus(_A)
_AniDevRouteAge_Type=Integer32
_AniDevRouteAge_Object=MibTableColumn
aniDevRouteAge=_AniDevRouteAge_Object((1,3,6,1,4,1,4325,2,9,1,1,10),_AniDevRouteAge_Type())
aniDevRouteAge.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteAge.setStatus(_A)
_AniDevRouteMask_Type=IpAddress
_AniDevRouteMask_Object=MibTableColumn
aniDevRouteMask=_AniDevRouteMask_Object((1,3,6,1,4,1,4325,2,9,1,1,11),_AniDevRouteMask_Type())
aniDevRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevRouteMask.setStatus(_A)
_AniDevRouteMetric5_Type=Integer32
_AniDevRouteMetric5_Object=MibTableColumn
aniDevRouteMetric5=_AniDevRouteMetric5_Object((1,3,6,1,4,1,4325,2,9,1,1,12),_AniDevRouteMetric5_Type())
aniDevRouteMetric5.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteMetric5.setStatus(_A)
_AniDevRouteInfo_Type=ObjectIdentifier
_AniDevRouteInfo_Object=MibTableColumn
aniDevRouteInfo=_AniDevRouteInfo_Object((1,3,6,1,4,1,4325,2,9,1,1,13),_AniDevRouteInfo_Type())
aniDevRouteInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevRouteInfo.setStatus(_A)
class _AniDevRouteFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('network',1),('host',2)))
_AniDevRouteFlag_Type.__name__=_D
_AniDevRouteFlag_Object=MibTableColumn
aniDevRouteFlag=_AniDevRouteFlag_Object((1,3,6,1,4,1,4325,2,9,1,1,14),_AniDevRouteFlag_Type())
aniDevRouteFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevRouteFlag.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'aniDevRoute':aniDevRoute,'aniDevRouteTable':aniDevRouteTable,'aniDevRouteEntry':aniDevRouteEntry,_F:aniDevRouteDest,'aniDevRouteIfIndex':aniDevRouteIfIndex,'aniDevRouteMetric1':aniDevRouteMetric1,'aniDevRouteMetric2':aniDevRouteMetric2,'aniDevRouteMetric3':aniDevRouteMetric3,'aniDevRouteMetric4':aniDevRouteMetric4,_G:aniDevRouteNextHop,'aniDevRouteType':aniDevRouteType,'aniDevRouteProto':aniDevRouteProto,'aniDevRouteAge':aniDevRouteAge,_H:aniDevRouteMask,'aniDevRouteMetric5':aniDevRouteMetric5,'aniDevRouteInfo':aniDevRouteInfo,'aniDevRouteFlag':aniDevRouteFlag})