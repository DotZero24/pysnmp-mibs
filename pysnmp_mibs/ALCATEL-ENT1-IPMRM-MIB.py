_K='alaIpmrmConfigMIBGroup'
_J='alaIpmrmExtendedBoundaryStatus'
_I='alaIpmrmFailoverHolddown'
_H='alaIpmrmMbrProtocolApps'
_G='alaIpmrmMbrStatus'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-IPMRM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ipmrm,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Ipmrm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1IPMRMMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,10,1))
if mibBuilder.loadTexts:alcatelIND1IPMRMMIB.setRevisions(('2012-04-03 00:00','2014-12-04 00:00'))
_AlcatelIND1IPMRMMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBObjects=_AlcatelIND1IPMRMMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,1))
_AlaIpmrmGlobalConfig_ObjectIdentity=ObjectIdentity
alaIpmrmGlobalConfig=_AlaIpmrmGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,1,1))
class _AlaIpmrmMbrStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmMbrStatus_Type.__name__=_C
_AlaIpmrmMbrStatus_Object=MibScalar
alaIpmrmMbrStatus=_AlaIpmrmMbrStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,1,1,1),_AlaIpmrmMbrStatus_Type())
alaIpmrmMbrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpmrmMbrStatus.setStatus(_A)
class _AlaIpmrmMbrProtocolApps_Type(Bits):namedValues=NamedValues(*(('dvmrp',0),('pim',1)))
_AlaIpmrmMbrProtocolApps_Type.__name__='Bits'
_AlaIpmrmMbrProtocolApps_Object=MibScalar
alaIpmrmMbrProtocolApps=_AlaIpmrmMbrProtocolApps_Object((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,1,1,2),_AlaIpmrmMbrProtocolApps_Type())
alaIpmrmMbrProtocolApps.setMaxAccess('read-only')
if mibBuilder.loadTexts:alaIpmrmMbrProtocolApps.setStatus(_A)
class _AlaIpmrmFailoverHolddown_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaIpmrmFailoverHolddown_Type.__name__=_C
_AlaIpmrmFailoverHolddown_Object=MibScalar
alaIpmrmFailoverHolddown=_AlaIpmrmFailoverHolddown_Object((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,1,1,3),_AlaIpmrmFailoverHolddown_Type())
alaIpmrmFailoverHolddown.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpmrmFailoverHolddown.setStatus(_A)
if mibBuilder.loadTexts:alaIpmrmFailoverHolddown.setUnits('seconds')
class _AlaIpmrmExtendedBoundaryStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmExtendedBoundaryStatus_Type.__name__=_C
_AlaIpmrmExtendedBoundaryStatus_Object=MibScalar
alaIpmrmExtendedBoundaryStatus=_AlaIpmrmExtendedBoundaryStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,1,1,4),_AlaIpmrmExtendedBoundaryStatus_Type())
alaIpmrmExtendedBoundaryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpmrmExtendedBoundaryStatus.setStatus(_A)
_AlcatelIND1IPMRMMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBConformance=_AlcatelIND1IPMRMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,2))
_AlcatelIND1IPMRMMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBCompliances=_AlcatelIND1IPMRMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,2,1))
_AlcatelIND1IPMRMMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBGroups=_AlcatelIND1IPMRMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,2,2))
alaIpmrmConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,2,2,1))
alaIpmrmConfigMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:alaIpmrmConfigMIBGroup.setStatus(_A)
alaIpmrmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,10,1,2,1,1))
alaIpmrmCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:alaIpmrmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1IPMRMMIB':alcatelIND1IPMRMMIB,'alcatelIND1IPMRMMIBObjects':alcatelIND1IPMRMMIBObjects,'alaIpmrmGlobalConfig':alaIpmrmGlobalConfig,_G:alaIpmrmMbrStatus,_H:alaIpmrmMbrProtocolApps,_I:alaIpmrmFailoverHolddown,_J:alaIpmrmExtendedBoundaryStatus,'alcatelIND1IPMRMMIBConformance':alcatelIND1IPMRMMIBConformance,'alcatelIND1IPMRMMIBCompliances':alcatelIND1IPMRMMIBCompliances,'alaIpmrmCompliance':alaIpmrmCompliance,'alcatelIND1IPMRMMIBGroups':alcatelIND1IPMRMMIBGroups,_K:alaIpmrmConfigMIBGroup})