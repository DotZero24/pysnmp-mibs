_G='alaMsgSrvGlobalConfigGroup'
_F='alaMsgSrvGlobalRestart'
_E='alaMsgSrvGlobalConfigStatus'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-MSG-SRV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1MsgSrvMIB,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1MsgSrvMIB')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
alcatelIND1MsgSrvMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,79,1))
if mibBuilder.loadTexts:alcatelIND1MsgSrvMIB.setRevisions(('2013-06-05 00:00',))
_AlcatelIND1MsgSrvMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1MsgSrvMIBNotifications=_AlcatelIND1MsgSrvMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,79,1,0))
if mibBuilder.loadTexts:alcatelIND1MsgSrvMIBNotifications.setStatus(_A)
_AlcatelIND1MsgSrvMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1MsgSrvMIBObjects=_AlcatelIND1MsgSrvMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,79,1,1))
if mibBuilder.loadTexts:alcatelIND1MsgSrvMIBObjects.setStatus(_A)
class _AlaMsgSrvGlobalConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaMsgSrvGlobalConfigStatus_Type.__name__=_C
_AlaMsgSrvGlobalConfigStatus_Object=MibScalar
alaMsgSrvGlobalConfigStatus=_AlaMsgSrvGlobalConfigStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,79,1,1,1),_AlaMsgSrvGlobalConfigStatus_Type())
alaMsgSrvGlobalConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMsgSrvGlobalConfigStatus.setStatus(_A)
class _AlaMsgSrvGlobalRestart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('restart',2)))
_AlaMsgSrvGlobalRestart_Type.__name__=_C
_AlaMsgSrvGlobalRestart_Object=MibScalar
alaMsgSrvGlobalRestart=_AlaMsgSrvGlobalRestart_Object((1,3,6,1,4,1,6486,801,1,2,1,79,1,1,2),_AlaMsgSrvGlobalRestart_Type())
alaMsgSrvGlobalRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMsgSrvGlobalRestart.setStatus(_A)
_AlcatelIND1MsgSrvMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1MsgSrvMIBConformance=_AlcatelIND1MsgSrvMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,79,1,2))
if mibBuilder.loadTexts:alcatelIND1MsgSrvMIBConformance.setStatus(_A)
_AlcatelIND1MsgSrvMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1MsgSrvMIBGroups=_AlcatelIND1MsgSrvMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,79,1,2,1))
if mibBuilder.loadTexts:alcatelIND1MsgSrvMIBGroups.setStatus(_A)
_AlcatelIND1MsgSrvMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1MsgSrvMIBCompliances=_AlcatelIND1MsgSrvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,79,1,2,2))
if mibBuilder.loadTexts:alcatelIND1MsgSrvMIBCompliances.setStatus(_A)
alaMsgSrvGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,79,1,2,1,1))
alaMsgSrvGlobalConfigGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:alaMsgSrvGlobalConfigGroup.setStatus(_A)
alcatelIND1MsgSrvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,79,1,2,2,1))
alcatelIND1MsgSrvMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:alcatelIND1MsgSrvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1MsgSrvMIB':alcatelIND1MsgSrvMIB,'alcatelIND1MsgSrvMIBNotifications':alcatelIND1MsgSrvMIBNotifications,'alcatelIND1MsgSrvMIBObjects':alcatelIND1MsgSrvMIBObjects,_E:alaMsgSrvGlobalConfigStatus,_F:alaMsgSrvGlobalRestart,'alcatelIND1MsgSrvMIBConformance':alcatelIND1MsgSrvMIBConformance,'alcatelIND1MsgSrvMIBGroups':alcatelIND1MsgSrvMIBGroups,_G:alaMsgSrvGlobalConfigGroup,'alcatelIND1MsgSrvMIBCompliances':alcatelIND1MsgSrvMIBCompliances,'alcatelIND1MsgSrvMIBCompliance':alcatelIND1MsgSrvMIBCompliance})