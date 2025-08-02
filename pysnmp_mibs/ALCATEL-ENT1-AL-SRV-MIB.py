_G='alaActiveLeaseSrvGlobalConfigGroup'
_F='alaActiveLeaseSrvGlobalRestart'
_E='alaActiveLeaseSrvGlobalConfigStatus'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-AL-SRV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1ActiveLeaseSrvMIB,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1ActiveLeaseSrvMIB')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
alcatelIND1ActiveLeaseSrvMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,80,1))
if mibBuilder.loadTexts:alcatelIND1ActiveLeaseSrvMIB.setRevisions(('2013-06-05 00:00',))
_AlcatelIND1ActiveLeaseSrvMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBNotifications=_AlcatelIND1ActiveLeaseSrvMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,80,1,0))
if mibBuilder.loadTexts:alcatelIND1ActiveLeaseSrvMIBNotifications.setStatus(_A)
_AlcatelIND1ActiveLeaseSrvMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBObjects=_AlcatelIND1ActiveLeaseSrvMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,80,1,1))
if mibBuilder.loadTexts:alcatelIND1ActiveLeaseSrvMIBObjects.setStatus(_A)
class _AlaActiveLeaseSrvGlobalConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaActiveLeaseSrvGlobalConfigStatus_Type.__name__=_C
_AlaActiveLeaseSrvGlobalConfigStatus_Object=MibScalar
alaActiveLeaseSrvGlobalConfigStatus=_AlaActiveLeaseSrvGlobalConfigStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,80,1,1,1),_AlaActiveLeaseSrvGlobalConfigStatus_Type())
alaActiveLeaseSrvGlobalConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaActiveLeaseSrvGlobalConfigStatus.setStatus(_A)
class _AlaActiveLeaseSrvGlobalRestart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('restart',2)))
_AlaActiveLeaseSrvGlobalRestart_Type.__name__=_C
_AlaActiveLeaseSrvGlobalRestart_Object=MibScalar
alaActiveLeaseSrvGlobalRestart=_AlaActiveLeaseSrvGlobalRestart_Object((1,3,6,1,4,1,6486,801,1,2,1,80,1,1,2),_AlaActiveLeaseSrvGlobalRestart_Type())
alaActiveLeaseSrvGlobalRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:alaActiveLeaseSrvGlobalRestart.setStatus(_A)
_AlcatelIND1ActiveLeaseSrvMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBConformance=_AlcatelIND1ActiveLeaseSrvMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,80,1,2))
if mibBuilder.loadTexts:alcatelIND1ActiveLeaseSrvMIBConformance.setStatus(_A)
_AlcatelIND1ActiveLeaseSrvMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBGroups=_AlcatelIND1ActiveLeaseSrvMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,80,1,2,1))
if mibBuilder.loadTexts:alcatelIND1ActiveLeaseSrvMIBGroups.setStatus(_A)
_AlcatelIND1ActiveLeaseSrvMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBCompliances=_AlcatelIND1ActiveLeaseSrvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,80,1,2,2))
if mibBuilder.loadTexts:alcatelIND1ActiveLeaseSrvMIBCompliances.setStatus(_A)
alaActiveLeaseSrvGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,80,1,2,1,1))
alaActiveLeaseSrvGlobalConfigGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:alaActiveLeaseSrvGlobalConfigGroup.setStatus(_A)
alcatelIND1ActiveLeaseSrvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,80,1,2,2,1))
alcatelIND1ActiveLeaseSrvMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:alcatelIND1ActiveLeaseSrvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1ActiveLeaseSrvMIB':alcatelIND1ActiveLeaseSrvMIB,'alcatelIND1ActiveLeaseSrvMIBNotifications':alcatelIND1ActiveLeaseSrvMIBNotifications,'alcatelIND1ActiveLeaseSrvMIBObjects':alcatelIND1ActiveLeaseSrvMIBObjects,_E:alaActiveLeaseSrvGlobalConfigStatus,_F:alaActiveLeaseSrvGlobalRestart,'alcatelIND1ActiveLeaseSrvMIBConformance':alcatelIND1ActiveLeaseSrvMIBConformance,'alcatelIND1ActiveLeaseSrvMIBGroups':alcatelIND1ActiveLeaseSrvMIBGroups,_G:alaActiveLeaseSrvGlobalConfigGroup,'alcatelIND1ActiveLeaseSrvMIBCompliances':alcatelIND1ActiveLeaseSrvMIBCompliances,'alcatelIND1ActiveLeaseSrvMIBCompliance':alcatelIND1ActiveLeaseSrvMIBCompliance})