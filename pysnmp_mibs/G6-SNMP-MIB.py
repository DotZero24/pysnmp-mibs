_L='browserIndex'
_K='v3ConfigIndex'
_J='v1v2ConfigIndex'
_I='deviceInfoIndex'
_H='enabled'
_G='disabled'
_F='read-only'
_E='not-accessible'
_D='G6-SNMP-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Snmp_ObjectIdentity=ObjectIdentity
snmp=_Snmp_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,65))
_DeviceInfoTable_Object=MibTable
deviceInfoTable=_DeviceInfoTable_Object((1,3,6,1,4,1,3181,10,6,3,65,1))
if mibBuilder.loadTexts:deviceInfoTable.setStatus(_A)
_DeviceInfoEntry_Object=MibTableRow
deviceInfoEntry=_DeviceInfoEntry_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1))
deviceInfoEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:deviceInfoEntry.setStatus(_A)
class _DeviceInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_DeviceInfoIndex_Type.__name__=_C
_DeviceInfoIndex_Object=MibTableColumn
deviceInfoIndex=_DeviceInfoIndex_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1,1),_DeviceInfoIndex_Type())
deviceInfoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceInfoIndex.setStatus(_A)
_DeviceInfoSysDescription_Type=DisplayString
_DeviceInfoSysDescription_Object=MibTableColumn
deviceInfoSysDescription=_DeviceInfoSysDescription_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1,2),_DeviceInfoSysDescription_Type())
deviceInfoSysDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:deviceInfoSysDescription.setStatus(_A)
_DeviceInfoSysName_Type=DisplayString
_DeviceInfoSysName_Object=MibTableColumn
deviceInfoSysName=_DeviceInfoSysName_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1,3),_DeviceInfoSysName_Type())
deviceInfoSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInfoSysName.setStatus(_A)
_DeviceInfoSysLocation_Type=DisplayString
_DeviceInfoSysLocation_Object=MibTableColumn
deviceInfoSysLocation=_DeviceInfoSysLocation_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1,4),_DeviceInfoSysLocation_Type())
deviceInfoSysLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInfoSysLocation.setStatus(_A)
_DeviceInfoSysGroup_Type=DisplayString
_DeviceInfoSysGroup_Object=MibTableColumn
deviceInfoSysGroup=_DeviceInfoSysGroup_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1,5),_DeviceInfoSysGroup_Type())
deviceInfoSysGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInfoSysGroup.setStatus(_A)
_DeviceInfoSysContact_Type=DisplayString
_DeviceInfoSysContact_Object=MibTableColumn
deviceInfoSysContact=_DeviceInfoSysContact_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1,6),_DeviceInfoSysContact_Type())
deviceInfoSysContact.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInfoSysContact.setStatus(_A)
_DeviceInfoSysObjectId_Type=DisplayString
_DeviceInfoSysObjectId_Object=MibTableColumn
deviceInfoSysObjectId=_DeviceInfoSysObjectId_Object((1,3,6,1,4,1,3181,10,6,3,65,1,1,7),_DeviceInfoSysObjectId_Type())
deviceInfoSysObjectId.setMaxAccess(_F)
if mibBuilder.loadTexts:deviceInfoSysObjectId.setStatus(_A)
_V1v2ConfigTable_Object=MibTable
v1v2ConfigTable=_V1v2ConfigTable_Object((1,3,6,1,4,1,3181,10,6,3,65,2))
if mibBuilder.loadTexts:v1v2ConfigTable.setStatus(_A)
_V1v2ConfigEntry_Object=MibTableRow
v1v2ConfigEntry=_V1v2ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1))
v1v2ConfigEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:v1v2ConfigEntry.setStatus(_A)
class _V1v2ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_V1v2ConfigIndex_Type.__name__=_C
_V1v2ConfigIndex_Object=MibTableColumn
v1v2ConfigIndex=_V1v2ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1,1),_V1v2ConfigIndex_Type())
v1v2ConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:v1v2ConfigIndex.setStatus(_A)
class _V1v2ConfigEnableSnmpV1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V1v2ConfigEnableSnmpV1_Type.__name__=_C
_V1v2ConfigEnableSnmpV1_Object=MibTableColumn
v1v2ConfigEnableSnmpV1=_V1v2ConfigEnableSnmpV1_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1,2),_V1v2ConfigEnableSnmpV1_Type())
v1v2ConfigEnableSnmpV1.setMaxAccess(_B)
if mibBuilder.loadTexts:v1v2ConfigEnableSnmpV1.setStatus(_A)
class _V1v2ConfigEnableSnmpV2c_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V1v2ConfigEnableSnmpV2c_Type.__name__=_C
_V1v2ConfigEnableSnmpV2c_Object=MibTableColumn
v1v2ConfigEnableSnmpV2c=_V1v2ConfigEnableSnmpV2c_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1,3),_V1v2ConfigEnableSnmpV2c_Type())
v1v2ConfigEnableSnmpV2c.setMaxAccess(_B)
if mibBuilder.loadTexts:v1v2ConfigEnableSnmpV2c.setStatus(_A)
_V1v2ConfigGetCommunity_Type=DisplayString
_V1v2ConfigGetCommunity_Object=MibTableColumn
v1v2ConfigGetCommunity=_V1v2ConfigGetCommunity_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1,4),_V1v2ConfigGetCommunity_Type())
v1v2ConfigGetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:v1v2ConfigGetCommunity.setStatus(_A)
_V1v2ConfigSetCommunity_Type=DisplayString
_V1v2ConfigSetCommunity_Object=MibTableColumn
v1v2ConfigSetCommunity=_V1v2ConfigSetCommunity_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1,5),_V1v2ConfigSetCommunity_Type())
v1v2ConfigSetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:v1v2ConfigSetCommunity.setStatus(_A)
_V1v2ConfigSnmpV1v2Username_Type=DisplayString
_V1v2ConfigSnmpV1v2Username_Object=MibTableColumn
v1v2ConfigSnmpV1v2Username=_V1v2ConfigSnmpV1v2Username_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1,6),_V1v2ConfigSnmpV1v2Username_Type())
v1v2ConfigSnmpV1v2Username.setMaxAccess(_B)
if mibBuilder.loadTexts:v1v2ConfigSnmpV1v2Username.setStatus(_A)
class _V1v2ConfigPermitV1v2SetCommands_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V1v2ConfigPermitV1v2SetCommands_Type.__name__=_C
_V1v2ConfigPermitV1v2SetCommands_Object=MibTableColumn
v1v2ConfigPermitV1v2SetCommands=_V1v2ConfigPermitV1v2SetCommands_Object((1,3,6,1,4,1,3181,10,6,3,65,2,1,7),_V1v2ConfigPermitV1v2SetCommands_Type())
v1v2ConfigPermitV1v2SetCommands.setMaxAccess(_B)
if mibBuilder.loadTexts:v1v2ConfigPermitV1v2SetCommands.setStatus(_A)
_V3ConfigTable_Object=MibTable
v3ConfigTable=_V3ConfigTable_Object((1,3,6,1,4,1,3181,10,6,3,65,3))
if mibBuilder.loadTexts:v3ConfigTable.setStatus(_A)
_V3ConfigEntry_Object=MibTableRow
v3ConfigEntry=_V3ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,3,65,3,1))
v3ConfigEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:v3ConfigEntry.setStatus(_A)
class _V3ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_V3ConfigIndex_Type.__name__=_C
_V3ConfigIndex_Object=MibTableColumn
v3ConfigIndex=_V3ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,3,65,3,1,1),_V3ConfigIndex_Type())
v3ConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:v3ConfigIndex.setStatus(_A)
class _V3ConfigEnableSnmpV3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V3ConfigEnableSnmpV3_Type.__name__=_C
_V3ConfigEnableSnmpV3_Object=MibTableColumn
v3ConfigEnableSnmpV3=_V3ConfigEnableSnmpV3_Object((1,3,6,1,4,1,3181,10,6,3,65,3,1,2),_V3ConfigEnableSnmpV3_Type())
v3ConfigEnableSnmpV3.setMaxAccess(_B)
if mibBuilder.loadTexts:v3ConfigEnableSnmpV3.setStatus(_A)
class _V3ConfigSecurityModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('usm',0),('vacm',1)))
_V3ConfigSecurityModel_Type.__name__=_C
_V3ConfigSecurityModel_Object=MibTableColumn
v3ConfigSecurityModel=_V3ConfigSecurityModel_Object((1,3,6,1,4,1,3181,10,6,3,65,3,1,3),_V3ConfigSecurityModel_Type())
v3ConfigSecurityModel.setMaxAccess(_B)
if mibBuilder.loadTexts:v3ConfigSecurityModel.setStatus(_A)
_V3ConfigSnmpEngineId_Type=DisplayString
_V3ConfigSnmpEngineId_Object=MibTableColumn
v3ConfigSnmpEngineId=_V3ConfigSnmpEngineId_Object((1,3,6,1,4,1,3181,10,6,3,65,3,1,4),_V3ConfigSnmpEngineId_Type())
v3ConfigSnmpEngineId.setMaxAccess(_B)
if mibBuilder.loadTexts:v3ConfigSnmpEngineId.setStatus(_A)
_V3ConfigTrapEngineId_Type=DisplayString
_V3ConfigTrapEngineId_Object=MibTableColumn
v3ConfigTrapEngineId=_V3ConfigTrapEngineId_Object((1,3,6,1,4,1,3181,10,6,3,65,3,1,5),_V3ConfigTrapEngineId_Type())
v3ConfigTrapEngineId.setMaxAccess(_B)
if mibBuilder.loadTexts:v3ConfigTrapEngineId.setStatus(_A)
_BrowserTable_Object=MibTable
browserTable=_BrowserTable_Object((1,3,6,1,4,1,3181,10,6,3,65,4))
if mibBuilder.loadTexts:browserTable.setStatus(_A)
_BrowserEntry_Object=MibTableRow
browserEntry=_BrowserEntry_Object((1,3,6,1,4,1,3181,10,6,3,65,4,1))
browserEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:browserEntry.setStatus(_A)
class _BrowserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_BrowserIndex_Type.__name__=_C
_BrowserIndex_Object=MibTableColumn
browserIndex=_BrowserIndex_Object((1,3,6,1,4,1,3181,10,6,3,65,4,1,1),_BrowserIndex_Type())
browserIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:browserIndex.setStatus(_A)
_BrowserGet_Type=DisplayString
_BrowserGet_Object=MibTableColumn
browserGet=_BrowserGet_Object((1,3,6,1,4,1,3181,10,6,3,65,4,1,2),_BrowserGet_Type())
browserGet.setMaxAccess(_B)
if mibBuilder.loadTexts:browserGet.setStatus(_A)
_BrowserNext_Type=DisplayString
_BrowserNext_Object=MibTableColumn
browserNext=_BrowserNext_Object((1,3,6,1,4,1,3181,10,6,3,65,4,1,3),_BrowserNext_Type())
browserNext.setMaxAccess(_B)
if mibBuilder.loadTexts:browserNext.setStatus(_A)
_BrowserSet_Type=DisplayString
_BrowserSet_Object=MibTableColumn
browserSet=_BrowserSet_Object((1,3,6,1,4,1,3181,10,6,3,65,4,1,4),_BrowserSet_Type())
browserSet.setMaxAccess(_B)
if mibBuilder.loadTexts:browserSet.setStatus(_A)
_BrowserWalk_Type=DisplayString
_BrowserWalk_Object=MibTableColumn
browserWalk=_BrowserWalk_Object((1,3,6,1,4,1,3181,10,6,3,65,4,1,5),_BrowserWalk_Type())
browserWalk.setMaxAccess(_B)
if mibBuilder.loadTexts:browserWalk.setStatus(_A)
_SnmpEngineBoots_Type=Unsigned32
_SnmpEngineBoots_Object=MibScalar
snmpEngineBoots=_SnmpEngineBoots_Object((1,3,6,1,4,1,3181,10,6,3,65,100),_SnmpEngineBoots_Type())
snmpEngineBoots.setMaxAccess(_F)
if mibBuilder.loadTexts:snmpEngineBoots.setStatus(_A)
_SnmpEngineRuntime_Type=Unsigned32
_SnmpEngineRuntime_Object=MibScalar
snmpEngineRuntime=_SnmpEngineRuntime_Object((1,3,6,1,4,1,3181,10,6,3,65,101),_SnmpEngineRuntime_Type())
snmpEngineRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:snmpEngineRuntime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'management':management,'snmp':snmp,'deviceInfoTable':deviceInfoTable,'deviceInfoEntry':deviceInfoEntry,_I:deviceInfoIndex,'deviceInfoSysDescription':deviceInfoSysDescription,'deviceInfoSysName':deviceInfoSysName,'deviceInfoSysLocation':deviceInfoSysLocation,'deviceInfoSysGroup':deviceInfoSysGroup,'deviceInfoSysContact':deviceInfoSysContact,'deviceInfoSysObjectId':deviceInfoSysObjectId,'v1v2ConfigTable':v1v2ConfigTable,'v1v2ConfigEntry':v1v2ConfigEntry,_J:v1v2ConfigIndex,'v1v2ConfigEnableSnmpV1':v1v2ConfigEnableSnmpV1,'v1v2ConfigEnableSnmpV2c':v1v2ConfigEnableSnmpV2c,'v1v2ConfigGetCommunity':v1v2ConfigGetCommunity,'v1v2ConfigSetCommunity':v1v2ConfigSetCommunity,'v1v2ConfigSnmpV1v2Username':v1v2ConfigSnmpV1v2Username,'v1v2ConfigPermitV1v2SetCommands':v1v2ConfigPermitV1v2SetCommands,'v3ConfigTable':v3ConfigTable,'v3ConfigEntry':v3ConfigEntry,_K:v3ConfigIndex,'v3ConfigEnableSnmpV3':v3ConfigEnableSnmpV3,'v3ConfigSecurityModel':v3ConfigSecurityModel,'v3ConfigSnmpEngineId':v3ConfigSnmpEngineId,'v3ConfigTrapEngineId':v3ConfigTrapEngineId,'browserTable':browserTable,'browserEntry':browserEntry,_L:browserIndex,'browserGet':browserGet,'browserNext':browserNext,'browserSet':browserSet,'browserWalk':browserWalk,'snmpEngineBoots':snmpEngineBoots,'snmpEngineRuntime':snmpEngineRuntime})