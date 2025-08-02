_O='alaOSPF3ConfigMIBGroup'
_N='alaOspf3MTUCheck'
_M='alaOspf3RestartInitiate'
_L='alaOspf3RestartStrictLsaChecking'
_K='alaOspf3RestartHelperSupport'
_J='alaOspf3TimerSpfHold'
_I='alaOspf3TimerSpfDelay'
_H='alaOspf3OrigRouteTag'
_G='Unsigned32'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='ALCATEL-IND1-OSPF3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ospf3,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Ospf3')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1OSPF3MIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,13,1))
if mibBuilder.loadTexts:alcatelIND1OSPF3MIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1OSPF3MIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBObjects=_AlcatelIND1OSPF3MIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1))
_AlaProtocolOspf3_ObjectIdentity=ObjectIdentity
alaProtocolOspf3=_AlaProtocolOspf3_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1))
class _AlaOspf3OrigRouteTag_Type(Unsigned32):defaultValue=0
_AlaOspf3OrigRouteTag_Type.__name__=_G
_AlaOspf3OrigRouteTag_Object=MibScalar
alaOspf3OrigRouteTag=_AlaOspf3OrigRouteTag_Object((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1,1),_AlaOspf3OrigRouteTag_Type())
alaOspf3OrigRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3OrigRouteTag.setStatus(_A)
class _AlaOspf3TimerSpfDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaOspf3TimerSpfDelay_Type.__name__=_C
_AlaOspf3TimerSpfDelay_Object=MibScalar
alaOspf3TimerSpfDelay=_AlaOspf3TimerSpfDelay_Object((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1,2),_AlaOspf3TimerSpfDelay_Type())
alaOspf3TimerSpfDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3TimerSpfDelay.setStatus(_A)
class _AlaOspf3TimerSpfHold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaOspf3TimerSpfHold_Type.__name__=_C
_AlaOspf3TimerSpfHold_Object=MibScalar
alaOspf3TimerSpfHold=_AlaOspf3TimerSpfHold_Object((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1,3),_AlaOspf3TimerSpfHold_Type())
alaOspf3TimerSpfHold.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3TimerSpfHold.setStatus(_A)
class _AlaOspf3RestartHelperSupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaOspf3RestartHelperSupport_Type.__name__=_C
_AlaOspf3RestartHelperSupport_Object=MibScalar
alaOspf3RestartHelperSupport=_AlaOspf3RestartHelperSupport_Object((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1,4),_AlaOspf3RestartHelperSupport_Type())
alaOspf3RestartHelperSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3RestartHelperSupport.setStatus(_A)
class _AlaOspf3RestartStrictLsaChecking_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaOspf3RestartStrictLsaChecking_Type.__name__=_C
_AlaOspf3RestartStrictLsaChecking_Object=MibScalar
alaOspf3RestartStrictLsaChecking=_AlaOspf3RestartStrictLsaChecking_Object((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1,5),_AlaOspf3RestartStrictLsaChecking_Type())
alaOspf3RestartStrictLsaChecking.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3RestartStrictLsaChecking.setStatus(_A)
class _AlaOspf3RestartInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaOspf3RestartInitiate_Type.__name__=_C
_AlaOspf3RestartInitiate_Object=MibScalar
alaOspf3RestartInitiate=_AlaOspf3RestartInitiate_Object((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1,6),_AlaOspf3RestartInitiate_Type())
alaOspf3RestartInitiate.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3RestartInitiate.setStatus(_A)
class _AlaOspf3MTUCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaOspf3MTUCheck_Type.__name__=_C
_AlaOspf3MTUCheck_Object=MibScalar
alaOspf3MTUCheck=_AlaOspf3MTUCheck_Object((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,1,1,7),_AlaOspf3MTUCheck_Type())
alaOspf3MTUCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3MTUCheck.setStatus(_A)
_AlcatelIND1OSPF3MIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBConformance=_AlcatelIND1OSPF3MIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,2))
_AlcatelIND1OSPF3MIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBCompliances=_AlcatelIND1OSPF3MIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,2,1))
_AlcatelIND1OSPF3MIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBGroups=_AlcatelIND1OSPF3MIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,2,2))
alaOSPF3ConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,2,2,1))
alaOSPF3ConfigMIBGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:alaOSPF3ConfigMIBGroup.setStatus(_A)
alcatelIND1OSPF3MIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,13,1,2,1,1))
alcatelIND1OSPF3MIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:alcatelIND1OSPF3MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1OSPF3MIB':alcatelIND1OSPF3MIB,'alcatelIND1OSPF3MIBObjects':alcatelIND1OSPF3MIBObjects,'alaProtocolOspf3':alaProtocolOspf3,_H:alaOspf3OrigRouteTag,_I:alaOspf3TimerSpfDelay,_J:alaOspf3TimerSpfHold,_K:alaOspf3RestartHelperSupport,_L:alaOspf3RestartStrictLsaChecking,_M:alaOspf3RestartInitiate,_N:alaOspf3MTUCheck,'alcatelIND1OSPF3MIBConformance':alcatelIND1OSPF3MIBConformance,'alcatelIND1OSPF3MIBCompliances':alcatelIND1OSPF3MIBCompliances,'alcatelIND1OSPF3MIBCompliance':alcatelIND1OSPF3MIBCompliance,'alcatelIND1OSPF3MIBGroups':alcatelIND1OSPF3MIBGroups,_O:alaOSPF3ConfigMIBGroup})