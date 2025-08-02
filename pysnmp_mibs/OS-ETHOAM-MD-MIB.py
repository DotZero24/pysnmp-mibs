_L='osEthOamMdMandatoryGroup'
_K='osEthOamMdAdminStatus'
_J='osEthOamMdCPorts'
_I='osEthOamMdName'
_H='osEthOamMdFormat'
_G='osEthOamMdSupport'
_F='osEthOamMdLevel'
_E='OctetString'
_D='read-create'
_C='Integer32'
_B='OS-ETHOAM-MD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntryValidator,PortList,oaOptiSwitch=mibBuilder.importSymbols('OS-COMMON-TC-MIB','EntryValidator','PortList','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osEthOamMd=ModuleIdentity((1,3,6,1,4,1,6926,2,13))
if mibBuilder.loadTexts:osEthOamMd.setRevisions(('2010-08-01 00:00',))
_OsEthOamMdCapabilities_ObjectIdentity=ObjectIdentity
osEthOamMdCapabilities=_OsEthOamMdCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,13,1))
class _OsEthOamMdSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsEthOamMdSupport_Type.__name__=_C
_OsEthOamMdSupport_Object=MibScalar
osEthOamMdSupport=_OsEthOamMdSupport_Object((1,3,6,1,4,1,6926,2,13,1,1),_OsEthOamMdSupport_Type())
osEthOamMdSupport.setMaxAccess('read-only')
if mibBuilder.loadTexts:osEthOamMdSupport.setStatus(_A)
_OsEthOamMdTable_Object=MibTable
osEthOamMdTable=_OsEthOamMdTable_Object((1,3,6,1,4,1,6926,2,13,2))
if mibBuilder.loadTexts:osEthOamMdTable.setStatus(_A)
_OsEthOamMdEntry_Object=MibTableRow
osEthOamMdEntry=_OsEthOamMdEntry_Object((1,3,6,1,4,1,6926,2,13,2,1))
osEthOamMdEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:osEthOamMdEntry.setStatus(_A)
class _OsEthOamMdLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OsEthOamMdLevel_Type.__name__=_C
_OsEthOamMdLevel_Object=MibTableColumn
osEthOamMdLevel=_OsEthOamMdLevel_Object((1,3,6,1,4,1,6926,2,13,2,1,1),_OsEthOamMdLevel_Type())
osEthOamMdLevel.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:osEthOamMdLevel.setStatus(_A)
class _OsEthOamMdFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('dnsLikeName',2),('macAddressAndUint',3),('charString',4)))
_OsEthOamMdFormat_Type.__name__=_C
_OsEthOamMdFormat_Object=MibTableColumn
osEthOamMdFormat=_OsEthOamMdFormat_Object((1,3,6,1,4,1,6926,2,13,2,1,2),_OsEthOamMdFormat_Type())
osEthOamMdFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:osEthOamMdFormat.setStatus(_A)
class _OsEthOamMdName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,43))
_OsEthOamMdName_Type.__name__=_E
_OsEthOamMdName_Object=MibTableColumn
osEthOamMdName=_OsEthOamMdName_Object((1,3,6,1,4,1,6926,2,13,2,1,3),_OsEthOamMdName_Type())
osEthOamMdName.setMaxAccess(_D)
if mibBuilder.loadTexts:osEthOamMdName.setStatus(_A)
_OsEthOamMdCPorts_Type=PortList
_OsEthOamMdCPorts_Object=MibTableColumn
osEthOamMdCPorts=_OsEthOamMdCPorts_Object((1,3,6,1,4,1,6926,2,13,2,1,4),_OsEthOamMdCPorts_Type())
osEthOamMdCPorts.setMaxAccess('read-write')
if mibBuilder.loadTexts:osEthOamMdCPorts.setStatus(_A)
_OsEthOamMdAdminStatus_Type=EntryValidator
_OsEthOamMdAdminStatus_Object=MibTableColumn
osEthOamMdAdminStatus=_OsEthOamMdAdminStatus_Object((1,3,6,1,4,1,6926,2,13,2,1,90),_OsEthOamMdAdminStatus_Type())
osEthOamMdAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osEthOamMdAdminStatus.setStatus(_A)
_OsEthOamMdConformance_ObjectIdentity=ObjectIdentity
osEthOamMdConformance=_OsEthOamMdConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,13,100))
_OsEthOamMdMIBCompliances_ObjectIdentity=ObjectIdentity
osEthOamMdMIBCompliances=_OsEthOamMdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,13,100,1))
_OsEthOamMdMIBGroups_ObjectIdentity=ObjectIdentity
osEthOamMdMIBGroups=_OsEthOamMdMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,13,100,2))
osEthOamMdMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,13,100,2,1))
osEthOamMdMandatoryGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:osEthOamMdMandatoryGroup.setStatus(_A)
osEthOamMdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,13,100,1,1))
osEthOamMdMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:osEthOamMdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osEthOamMd':osEthOamMd,'osEthOamMdCapabilities':osEthOamMdCapabilities,_G:osEthOamMdSupport,'osEthOamMdTable':osEthOamMdTable,'osEthOamMdEntry':osEthOamMdEntry,_F:osEthOamMdLevel,_H:osEthOamMdFormat,_I:osEthOamMdName,_J:osEthOamMdCPorts,_K:osEthOamMdAdminStatus,'osEthOamMdConformance':osEthOamMdConformance,'osEthOamMdMIBCompliances':osEthOamMdMIBCompliances,'osEthOamMdMIBCompliance':osEthOamMdMIBCompliance,'osEthOamMdMIBGroups':osEthOamMdMIBGroups,_L:osEthOamMdMandatoryGroup})