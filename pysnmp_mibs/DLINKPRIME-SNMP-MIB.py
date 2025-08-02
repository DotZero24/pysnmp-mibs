_L='dpSnmpCommunityAccessListName'
_K='dpSnmpTrapGlobalNotifyEnable'
_J='dpSnmpTrapGlobalEnabled'
_I='dpSnmpServiceEnabled'
_H='dpSnmpHostIndex'
_G='not-accessible'
_F='dpSnmpCommunityName'
_E='Integer32'
_D='SnmpAdminString'
_C='DLINKPRIME-SNMP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
SnmpAdminString,SnmpEngineID,SnmpSecurityModel=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D,'SnmpEngineID','SnmpSecurityModel')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dlinkPrimeSnmpMIB=ModuleIdentity((1,3,6,1,4,1,171,15,15))
if mibBuilder.loadTexts:dlinkPrimeSnmpMIB.setRevisions(('2014-06-03 00:00',))
_DpSnmpMIBNotifications_ObjectIdentity=ObjectIdentity
dpSnmpMIBNotifications=_DpSnmpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,15,0))
_DpSnmpMIBObjects_ObjectIdentity=ObjectIdentity
dpSnmpMIBObjects=_DpSnmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,15,1))
_DpSnmpGeneral_ObjectIdentity=ObjectIdentity
dpSnmpGeneral=_DpSnmpGeneral_ObjectIdentity((1,3,6,1,4,1,171,15,15,1,1))
_DpSnmpServiceEnabled_Type=TruthValue
_DpSnmpServiceEnabled_Object=MibScalar
dpSnmpServiceEnabled=_DpSnmpServiceEnabled_Object((1,3,6,1,4,1,171,15,15,1,1,1),_DpSnmpServiceEnabled_Type())
dpSnmpServiceEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dpSnmpServiceEnabled.setStatus(_A)
_DpSnmpMIBTrap_ObjectIdentity=ObjectIdentity
dpSnmpMIBTrap=_DpSnmpMIBTrap_ObjectIdentity((1,3,6,1,4,1,171,15,15,1,2))
_DpSnmpTrapGlobalEnabled_Type=TruthValue
_DpSnmpTrapGlobalEnabled_Object=MibScalar
dpSnmpTrapGlobalEnabled=_DpSnmpTrapGlobalEnabled_Object((1,3,6,1,4,1,171,15,15,1,2,1),_DpSnmpTrapGlobalEnabled_Type())
dpSnmpTrapGlobalEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dpSnmpTrapGlobalEnabled.setStatus(_A)
class _DpSnmpTrapGlobalNotifyEnable_Type(Bits):namedValues=NamedValues(*(('linkUp',0),('linkDown',1),('coldStart',2),('warmStart',3),('authentication',4)))
_DpSnmpTrapGlobalNotifyEnable_Type.__name__='Bits'
_DpSnmpTrapGlobalNotifyEnable_Object=MibScalar
dpSnmpTrapGlobalNotifyEnable=_DpSnmpTrapGlobalNotifyEnable_Object((1,3,6,1,4,1,171,15,15,1,2,2),_DpSnmpTrapGlobalNotifyEnable_Type())
dpSnmpTrapGlobalNotifyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dpSnmpTrapGlobalNotifyEnable.setStatus(_A)
_DpSnmpAccessCfg_ObjectIdentity=ObjectIdentity
dpSnmpAccessCfg=_DpSnmpAccessCfg_ObjectIdentity((1,3,6,1,4,1,171,15,15,1,3))
_DpSnmpCommunityTable_Object=MibTable
dpSnmpCommunityTable=_DpSnmpCommunityTable_Object((1,3,6,1,4,1,171,15,15,1,3,1))
if mibBuilder.loadTexts:dpSnmpCommunityTable.setStatus(_A)
_DpSnmpCommunityEntry_Object=MibTableRow
dpSnmpCommunityEntry=_DpSnmpCommunityEntry_Object((1,3,6,1,4,1,171,15,15,1,3,1,1))
dpSnmpCommunityEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:dpSnmpCommunityEntry.setStatus(_A)
_DpSnmpCommunityName_Type=SnmpAdminString
_DpSnmpCommunityName_Object=MibTableColumn
dpSnmpCommunityName=_DpSnmpCommunityName_Object((1,3,6,1,4,1,171,15,15,1,3,1,1,1),_DpSnmpCommunityName_Type())
dpSnmpCommunityName.setMaxAccess(_G)
if mibBuilder.loadTexts:dpSnmpCommunityName.setStatus(_A)
_DpSnmpCommunityAccessListName_Type=DisplayString
_DpSnmpCommunityAccessListName_Object=MibTableColumn
dpSnmpCommunityAccessListName=_DpSnmpCommunityAccessListName_Object((1,3,6,1,4,1,171,15,15,1,3,1,1,3),_DpSnmpCommunityAccessListName_Type())
dpSnmpCommunityAccessListName.setMaxAccess(_B)
if mibBuilder.loadTexts:dpSnmpCommunityAccessListName.setStatus(_A)
_DpSnmpHostTable_Object=MibTable
dpSnmpHostTable=_DpSnmpHostTable_Object((1,3,6,1,4,1,171,15,15,1,3,2))
if mibBuilder.loadTexts:dpSnmpHostTable.setStatus(_A)
_DpSnmpHostEntry_Object=MibTableRow
dpSnmpHostEntry=_DpSnmpHostEntry_Object((1,3,6,1,4,1,171,15,15,1,3,2,1))
dpSnmpHostEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:dpSnmpHostEntry.setStatus(_A)
_DpSnmpHostIndex_Type=Unsigned32
_DpSnmpHostIndex_Object=MibTableColumn
dpSnmpHostIndex=_DpSnmpHostIndex_Object((1,3,6,1,4,1,171,15,15,1,3,2,1,1),_DpSnmpHostIndex_Type())
dpSnmpHostIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:dpSnmpHostIndex.setStatus(_A)
_DpSnmpHostIPv4Addr_Type=IpAddress
_DpSnmpHostIPv4Addr_Object=MibTableColumn
dpSnmpHostIPv4Addr=_DpSnmpHostIPv4Addr_Object((1,3,6,1,4,1,171,15,15,1,3,2,1,2),_DpSnmpHostIPv4Addr_Type())
dpSnmpHostIPv4Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:dpSnmpHostIPv4Addr.setStatus(_A)
class _DpSnmpHostSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2c',2)))
_DpSnmpHostSecurity_Type.__name__=_E
_DpSnmpHostSecurity_Object=MibTableColumn
dpSnmpHostSecurity=_DpSnmpHostSecurity_Object((1,3,6,1,4,1,171,15,15,1,3,2,1,3),_DpSnmpHostSecurity_Type())
dpSnmpHostSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:dpSnmpHostSecurity.setStatus(_A)
class _DpSnmpHostCommunityName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_DpSnmpHostCommunityName_Type.__name__=_D
_DpSnmpHostCommunityName_Object=MibTableColumn
dpSnmpHostCommunityName=_DpSnmpHostCommunityName_Object((1,3,6,1,4,1,171,15,15,1,3,2,1,4),_DpSnmpHostCommunityName_Type())
dpSnmpHostCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:dpSnmpHostCommunityName.setStatus(_A)
_DpSnmpMIBConformance_ObjectIdentity=ObjectIdentity
dpSnmpMIBConformance=_DpSnmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,15,2))
_DpSnmpCompliances_ObjectIdentity=ObjectIdentity
dpSnmpCompliances=_DpSnmpCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,15,2,1))
_DpSnmpGroups_ObjectIdentity=ObjectIdentity
dpSnmpGroups=_DpSnmpGroups_ObjectIdentity((1,3,6,1,4,1,171,15,15,2,2))
dpSnmpSysCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,15,2,2,1))
dpSnmpSysCfgGroup.setObjects((_C,_I))
if mibBuilder.loadTexts:dpSnmpSysCfgGroup.setStatus(_A)
dpSnmpTrapCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,15,2,2,2))
dpSnmpTrapCfgGroup.setObjects(*((_C,_J),(_C,_K)))
if mibBuilder.loadTexts:dpSnmpTrapCfgGroup.setStatus(_A)
dpSnmpCommunityExtGroup=ObjectGroup((1,3,6,1,4,1,171,15,15,2,2,3))
dpSnmpCommunityExtGroup.setObjects((_C,_L))
if mibBuilder.loadTexts:dpSnmpCommunityExtGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'dlinkPrimeSnmpMIB':dlinkPrimeSnmpMIB,'dpSnmpMIBNotifications':dpSnmpMIBNotifications,'dpSnmpMIBObjects':dpSnmpMIBObjects,'dpSnmpGeneral':dpSnmpGeneral,_I:dpSnmpServiceEnabled,'dpSnmpMIBTrap':dpSnmpMIBTrap,_J:dpSnmpTrapGlobalEnabled,_K:dpSnmpTrapGlobalNotifyEnable,'dpSnmpAccessCfg':dpSnmpAccessCfg,'dpSnmpCommunityTable':dpSnmpCommunityTable,'dpSnmpCommunityEntry':dpSnmpCommunityEntry,_F:dpSnmpCommunityName,_L:dpSnmpCommunityAccessListName,'dpSnmpHostTable':dpSnmpHostTable,'dpSnmpHostEntry':dpSnmpHostEntry,_H:dpSnmpHostIndex,'dpSnmpHostIPv4Addr':dpSnmpHostIPv4Addr,'dpSnmpHostSecurity':dpSnmpHostSecurity,'dpSnmpHostCommunityName':dpSnmpHostCommunityName,'dpSnmpMIBConformance':dpSnmpMIBConformance,'dpSnmpCompliances':dpSnmpCompliances,'dpSnmpGroups':dpSnmpGroups,'dpSnmpSysCfgGroup':dpSnmpSysCfgGroup,'dpSnmpTrapCfgGroup':dpSnmpTrapCfgGroup,'dpSnmpCommunityExtGroup':dpSnmpCommunityExtGroup})