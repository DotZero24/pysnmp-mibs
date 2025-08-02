_N='osLicenseActivationMIBGroup'
_M='osActvFeatMgmtKey'
_L='osActvFeatMgmtParam'
_K='osActvFeatMgmtStatus'
_J='osMplsActivationSatus'
_I='osMplsActivationLicense'
_H='osRoutingProtocolsActivationSatus'
_G='osRoutingProtocolsActivationLicense'
_F='osActvFeatMgmtId'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='OS-LICENSE-ACTIVATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osLicenseActivation=ModuleIdentity((1,3,6,1,4,1,6926,2,27))
if mibBuilder.loadTexts:osLicenseActivation.setRevisions(('2014-02-04 00:00',))
class OsActivationLicense(TextualConvention,OctetString):status=_A;displayHint='12a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
class OsActivationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('active',2),('notActive',3),('notSupported',4)))
_OsRoutingProtocolsActivation_ObjectIdentity=ObjectIdentity
osRoutingProtocolsActivation=_OsRoutingProtocolsActivation_ObjectIdentity((1,3,6,1,4,1,6926,2,27,1))
_OsRoutingProtocolsActivationLicense_Type=OsActivationLicense
_OsRoutingProtocolsActivationLicense_Object=MibScalar
osRoutingProtocolsActivationLicense=_OsRoutingProtocolsActivationLicense_Object((1,3,6,1,4,1,6926,2,27,1,1),_OsRoutingProtocolsActivationLicense_Type())
osRoutingProtocolsActivationLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:osRoutingProtocolsActivationLicense.setStatus(_A)
_OsRoutingProtocolsActivationSatus_Type=OsActivationStatus
_OsRoutingProtocolsActivationSatus_Object=MibScalar
osRoutingProtocolsActivationSatus=_OsRoutingProtocolsActivationSatus_Object((1,3,6,1,4,1,6926,2,27,1,2),_OsRoutingProtocolsActivationSatus_Type())
osRoutingProtocolsActivationSatus.setMaxAccess(_E)
if mibBuilder.loadTexts:osRoutingProtocolsActivationSatus.setStatus(_A)
_OsMplsActivation_ObjectIdentity=ObjectIdentity
osMplsActivation=_OsMplsActivation_ObjectIdentity((1,3,6,1,4,1,6926,2,27,2))
_OsMplsActivationLicense_Type=OsActivationLicense
_OsMplsActivationLicense_Object=MibScalar
osMplsActivationLicense=_OsMplsActivationLicense_Object((1,3,6,1,4,1,6926,2,27,2,1),_OsMplsActivationLicense_Type())
osMplsActivationLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:osMplsActivationLicense.setStatus(_A)
_OsMplsActivationSatus_Type=OsActivationStatus
_OsMplsActivationSatus_Object=MibScalar
osMplsActivationSatus=_OsMplsActivationSatus_Object((1,3,6,1,4,1,6926,2,27,2,2),_OsMplsActivationSatus_Type())
osMplsActivationSatus.setMaxAccess(_E)
if mibBuilder.loadTexts:osMplsActivationSatus.setStatus(_A)
_OsActvFeatMgmtTable_Object=MibTable
osActvFeatMgmtTable=_OsActvFeatMgmtTable_Object((1,3,6,1,4,1,6926,2,27,8))
if mibBuilder.loadTexts:osActvFeatMgmtTable.setStatus(_A)
_OsActvFeatMgmtEntry_Object=MibTableRow
osActvFeatMgmtEntry=_OsActvFeatMgmtEntry_Object((1,3,6,1,4,1,6926,2,27,8,1))
osActvFeatMgmtEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:osActvFeatMgmtEntry.setStatus(_A)
class _OsActvFeatMgmtId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('os600withGigaPorts',1),('securePush',2),('routingProtocols',3),('mplsProtocols',4)))
_OsActvFeatMgmtId_Type.__name__=_D
_OsActvFeatMgmtId_Object=MibTableColumn
osActvFeatMgmtId=_OsActvFeatMgmtId_Object((1,3,6,1,4,1,6926,2,27,8,1,1),_OsActvFeatMgmtId_Type())
osActvFeatMgmtId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:osActvFeatMgmtId.setStatus(_A)
_OsActvFeatMgmtStatus_Type=OsActivationStatus
_OsActvFeatMgmtStatus_Object=MibTableColumn
osActvFeatMgmtStatus=_OsActvFeatMgmtStatus_Object((1,3,6,1,4,1,6926,2,27,8,1,2),_OsActvFeatMgmtStatus_Type())
osActvFeatMgmtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osActvFeatMgmtStatus.setStatus(_A)
_OsActvFeatMgmtParam_Type=Unsigned32
_OsActvFeatMgmtParam_Object=MibTableColumn
osActvFeatMgmtParam=_OsActvFeatMgmtParam_Object((1,3,6,1,4,1,6926,2,27,8,1,3),_OsActvFeatMgmtParam_Type())
osActvFeatMgmtParam.setMaxAccess(_C)
if mibBuilder.loadTexts:osActvFeatMgmtParam.setStatus(_A)
_OsActvFeatMgmtKey_Type=OsActivationLicense
_OsActvFeatMgmtKey_Object=MibTableColumn
osActvFeatMgmtKey=_OsActvFeatMgmtKey_Object((1,3,6,1,4,1,6926,2,27,8,1,4),_OsActvFeatMgmtKey_Type())
osActvFeatMgmtKey.setMaxAccess(_C)
if mibBuilder.loadTexts:osActvFeatMgmtKey.setStatus(_A)
_OsLicenseActivationConformance_ObjectIdentity=ObjectIdentity
osLicenseActivationConformance=_OsLicenseActivationConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,27,100))
_OsLicenseActivationMIBCompliances_ObjectIdentity=ObjectIdentity
osLicenseActivationMIBCompliances=_OsLicenseActivationMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,27,100,1))
_OsLicenseActivationMIBGroups_ObjectIdentity=ObjectIdentity
osLicenseActivationMIBGroups=_OsLicenseActivationMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,27,100,2))
osLicenseActivationMIBGroup=ObjectGroup((1,3,6,1,4,1,6926,2,27,100,2,1))
osLicenseActivationMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:osLicenseActivationMIBGroup.setStatus(_A)
osLicenseActivationMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,27,100,1,1))
osLicenseActivationMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:osLicenseActivationMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OsActivationLicense':OsActivationLicense,'OsActivationStatus':OsActivationStatus,'osLicenseActivation':osLicenseActivation,'osRoutingProtocolsActivation':osRoutingProtocolsActivation,_G:osRoutingProtocolsActivationLicense,_H:osRoutingProtocolsActivationSatus,'osMplsActivation':osMplsActivation,_I:osMplsActivationLicense,_J:osMplsActivationSatus,'osActvFeatMgmtTable':osActvFeatMgmtTable,'osActvFeatMgmtEntry':osActvFeatMgmtEntry,_F:osActvFeatMgmtId,_K:osActvFeatMgmtStatus,_L:osActvFeatMgmtParam,_M:osActvFeatMgmtKey,'osLicenseActivationConformance':osLicenseActivationConformance,'osLicenseActivationMIBCompliances':osLicenseActivationMIBCompliances,'osLicenseActivationMIBCompliance':osLicenseActivationMIBCompliance,'osLicenseActivationMIBGroups':osLicenseActivationMIBGroups,_N:osLicenseActivationMIBGroup})