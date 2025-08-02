_N='alaGlobalRouteTableMIBGroup'
_M='alaGrtRouteTag'
_L='alaGrtRouteMetric'
_K='alaGrtRouteVrfName'
_J='alaGrtRouteNextHop'
_I='alaGrtRouteMaskLen'
_H='alaGrtRouteDest'
_G='alaGrtRouteDistinguisher'
_F='Integer32'
_E='read-only'
_D='InetAddress'
_C='not-accessible'
_B='ALCATEL-IND1-GRT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1GlobalRouteTableMIB,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1GlobalRouteTableMIB')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1GRTMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,16,1))
if mibBuilder.loadTexts:alcatelIND1GRTMIB.setRevisions(('2007-04-03 00:00',))
class AlaGrtRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AlcatelIND1GRTMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBConformance=_AlcatelIND1GRTMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,1))
_AlcatelIND1GRTMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBCompliances=_AlcatelIND1GRTMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,1,1))
_AlcatelIND1GRTMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBGroups=_AlcatelIND1GRTMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,1,2))
_AlcatelIND1GRTMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBObjects=_AlcatelIND1GRTMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2))
_AlaGrtConfig_ObjectIdentity=ObjectIdentity
alaGrtConfig=_AlaGrtConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1))
_AlaGrtRouteTable_Object=MibTable
alaGrtRouteTable=_AlaGrtRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1))
if mibBuilder.loadTexts:alaGrtRouteTable.setStatus(_A)
_AlaGrtRouteEntry_Object=MibTableRow
alaGrtRouteEntry=_AlaGrtRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1))
alaGrtRouteEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:alaGrtRouteEntry.setStatus(_A)
_AlaGrtRouteDistinguisher_Type=AlaGrtRouteDistinguisher
_AlaGrtRouteDistinguisher_Object=MibTableColumn
alaGrtRouteDistinguisher=_AlaGrtRouteDistinguisher_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,1),_AlaGrtRouteDistinguisher_Type())
alaGrtRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteDistinguisher.setStatus(_A)
class _AlaGrtRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaGrtRouteDest_Type.__name__=_D
_AlaGrtRouteDest_Object=MibTableColumn
alaGrtRouteDest=_AlaGrtRouteDest_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,2),_AlaGrtRouteDest_Type())
alaGrtRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteDest.setStatus(_A)
_AlaGrtRouteDestType_Type=InetAddressType
_AlaGrtRouteDestType_Object=MibTableColumn
alaGrtRouteDestType=_AlaGrtRouteDestType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,3),_AlaGrtRouteDestType_Type())
alaGrtRouteDestType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteDestType.setStatus(_A)
class _AlaGrtRouteMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AlaGrtRouteMaskLen_Type.__name__=_F
_AlaGrtRouteMaskLen_Object=MibTableColumn
alaGrtRouteMaskLen=_AlaGrtRouteMaskLen_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,4),_AlaGrtRouteMaskLen_Type())
alaGrtRouteMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteMaskLen.setStatus(_A)
class _AlaGrtRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaGrtRouteNextHop_Type.__name__=_D
_AlaGrtRouteNextHop_Object=MibTableColumn
alaGrtRouteNextHop=_AlaGrtRouteNextHop_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,5),_AlaGrtRouteNextHop_Type())
alaGrtRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteNextHop.setStatus(_A)
_AlaGrtRouteNextHopType_Type=InetAddressType
_AlaGrtRouteNextHopType_Object=MibTableColumn
alaGrtRouteNextHopType=_AlaGrtRouteNextHopType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,6),_AlaGrtRouteNextHopType_Type())
alaGrtRouteNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteNextHopType.setStatus(_A)
_AlaGrtRouteMetric_Type=Unsigned32
_AlaGrtRouteMetric_Object=MibTableColumn
alaGrtRouteMetric=_AlaGrtRouteMetric_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,7),_AlaGrtRouteMetric_Type())
alaGrtRouteMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:alaGrtRouteMetric.setStatus(_A)
_AlaGrtRouteTag_Type=Unsigned32
_AlaGrtRouteTag_Object=MibTableColumn
alaGrtRouteTag=_AlaGrtRouteTag_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,8),_AlaGrtRouteTag_Type())
alaGrtRouteTag.setMaxAccess(_E)
if mibBuilder.loadTexts:alaGrtRouteTag.setStatus(_A)
_AlaGrtRouteVrfName_Type=SnmpAdminString
_AlaGrtRouteVrfName_Object=MibTableColumn
alaGrtRouteVrfName=_AlaGrtRouteVrfName_Object((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,2,1,1,1,9),_AlaGrtRouteVrfName_Type())
alaGrtRouteVrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:alaGrtRouteVrfName.setStatus(_A)
alaGlobalRouteTableMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,1,2,1))
alaGlobalRouteTableMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:alaGlobalRouteTableMIBGroup.setStatus(_A)
alaGlobalRouteTableCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,16,1,1,1,1))
alaGlobalRouteTableCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:alaGlobalRouteTableCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaGrtRouteDistinguisher':AlaGrtRouteDistinguisher,'alcatelIND1GRTMIB':alcatelIND1GRTMIB,'alcatelIND1GRTMIBConformance':alcatelIND1GRTMIBConformance,'alcatelIND1GRTMIBCompliances':alcatelIND1GRTMIBCompliances,'alaGlobalRouteTableCompliance':alaGlobalRouteTableCompliance,'alcatelIND1GRTMIBGroups':alcatelIND1GRTMIBGroups,_N:alaGlobalRouteTableMIBGroup,'alcatelIND1GRTMIBObjects':alcatelIND1GRTMIBObjects,'alaGrtConfig':alaGrtConfig,'alaGrtRouteTable':alaGrtRouteTable,'alaGrtRouteEntry':alaGrtRouteEntry,_G:alaGrtRouteDistinguisher,_H:alaGrtRouteDest,'alaGrtRouteDestType':alaGrtRouteDestType,_I:alaGrtRouteMaskLen,_J:alaGrtRouteNextHop,'alaGrtRouteNextHopType':alaGrtRouteNextHopType,_L:alaGrtRouteMetric,_M:alaGrtRouteTag,_K:alaGrtRouteVrfName})