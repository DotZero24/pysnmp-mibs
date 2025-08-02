_F='osSecurePushMibMandatoryGroup'
_E='osSecurePushConfAdminStatus'
_D='osSecurePushSupport'
_C='Integer32'
_B='OS-SECURE-PUSH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osSecurePush=ModuleIdentity((1,3,6,1,4,1,6926,2,24))
if mibBuilder.loadTexts:osSecurePush.setRevisions(('2012-12-19 00:00',))
_OsSecurePushGeneral_ObjectIdentity=ObjectIdentity
osSecurePushGeneral=_OsSecurePushGeneral_ObjectIdentity((1,3,6,1,4,1,6926,2,24,1))
class _OsSecurePushSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsSecurePushSupport_Type.__name__=_C
_OsSecurePushSupport_Object=MibScalar
osSecurePushSupport=_OsSecurePushSupport_Object((1,3,6,1,4,1,6926,2,24,1,1),_OsSecurePushSupport_Type())
osSecurePushSupport.setMaxAccess('read-only')
if mibBuilder.loadTexts:osSecurePushSupport.setStatus(_A)
class _OsSecurePushConfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unknown',1),('askFromServer',2)))
_OsSecurePushConfAdminStatus_Type.__name__=_C
_OsSecurePushConfAdminStatus_Object=MibScalar
osSecurePushConfAdminStatus=_OsSecurePushConfAdminStatus_Object((1,3,6,1,4,1,6926,2,24,1,2),_OsSecurePushConfAdminStatus_Type())
osSecurePushConfAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:osSecurePushConfAdminStatus.setStatus(_A)
_OsSecurePushConformance_ObjectIdentity=ObjectIdentity
osSecurePushConformance=_OsSecurePushConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,24,100))
_OsSecurePushMIBCompliances_ObjectIdentity=ObjectIdentity
osSecurePushMIBCompliances=_OsSecurePushMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,24,100,1))
_OsSecurePushMIBGroups_ObjectIdentity=ObjectIdentity
osSecurePushMIBGroups=_OsSecurePushMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,24,100,2))
osSecurePushMibMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,24,100,2,1))
osSecurePushMibMandatoryGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:osSecurePushMibMandatoryGroup.setStatus(_A)
osSecurePushMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,24,100,1,1))
osSecurePushMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:osSecurePushMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osSecurePush':osSecurePush,'osSecurePushGeneral':osSecurePushGeneral,_D:osSecurePushSupport,_E:osSecurePushConfAdminStatus,'osSecurePushConformance':osSecurePushConformance,'osSecurePushMIBCompliances':osSecurePushMIBCompliances,'osSecurePushMIBCompliance':osSecurePushMIBCompliance,'osSecurePushMIBGroups':osSecurePushMIBGroups,_F:osSecurePushMibMandatoryGroup})