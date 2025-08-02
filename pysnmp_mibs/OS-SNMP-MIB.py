_P='osSnmpMandatoryGroup'
_O='osSnmpChangeLogMode'
_N='osSnmpAlarmMangerMode'
_M='osSnmpChangeCliNodeName'
_L='osSnmpChangeCliCommand'
_K='osSnmpChangeCliUser'
_J='osSnmpChangeV3User'
_I='osSnmpChangeV2Community'
_H='osSnmpChangeSourceAddress'
_G='read-write'
_F='enable'
_E='disable'
_D='Integer32'
_C='accessible-for-notify'
_B='OS-SNMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adva,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','adva')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osSnmp=ModuleIdentity((1,3,6,1,4,1,629,2544,7))
if mibBuilder.loadTexts:osSnmp.setRevisions(('2020-12-09 00:00',))
_OsSnmpNotificationObjects_ObjectIdentity=ObjectIdentity
osSnmpNotificationObjects=_OsSnmpNotificationObjects_ObjectIdentity((1,3,6,1,4,1,629,2544,7,1))
_OsSnmpChangeSourceAddress_Type=DisplayString
_OsSnmpChangeSourceAddress_Object=MibScalar
osSnmpChangeSourceAddress=_OsSnmpChangeSourceAddress_Object((1,3,6,1,4,1,629,2544,7,1,1),_OsSnmpChangeSourceAddress_Type())
osSnmpChangeSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osSnmpChangeSourceAddress.setStatus(_A)
_OsSnmpChangeV2Community_Type=DisplayString
_OsSnmpChangeV2Community_Object=MibScalar
osSnmpChangeV2Community=_OsSnmpChangeV2Community_Object((1,3,6,1,4,1,629,2544,7,1,2),_OsSnmpChangeV2Community_Type())
osSnmpChangeV2Community.setMaxAccess(_C)
if mibBuilder.loadTexts:osSnmpChangeV2Community.setStatus(_A)
_OsSnmpChangeV3User_Type=DisplayString
_OsSnmpChangeV3User_Object=MibScalar
osSnmpChangeV3User=_OsSnmpChangeV3User_Object((1,3,6,1,4,1,629,2544,7,1,3),_OsSnmpChangeV3User_Type())
osSnmpChangeV3User.setMaxAccess(_C)
if mibBuilder.loadTexts:osSnmpChangeV3User.setStatus(_A)
_OsSnmpChangeCliUser_Type=DisplayString
_OsSnmpChangeCliUser_Object=MibScalar
osSnmpChangeCliUser=_OsSnmpChangeCliUser_Object((1,3,6,1,4,1,629,2544,7,1,4),_OsSnmpChangeCliUser_Type())
osSnmpChangeCliUser.setMaxAccess(_C)
if mibBuilder.loadTexts:osSnmpChangeCliUser.setStatus(_A)
_OsSnmpChangeCliCommand_Type=DisplayString
_OsSnmpChangeCliCommand_Object=MibScalar
osSnmpChangeCliCommand=_OsSnmpChangeCliCommand_Object((1,3,6,1,4,1,629,2544,7,1,5),_OsSnmpChangeCliCommand_Type())
osSnmpChangeCliCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:osSnmpChangeCliCommand.setStatus(_A)
_OsSnmpChangeCliNodeName_Type=DisplayString
_OsSnmpChangeCliNodeName_Object=MibScalar
osSnmpChangeCliNodeName=_OsSnmpChangeCliNodeName_Object((1,3,6,1,4,1,629,2544,7,1,6),_OsSnmpChangeCliNodeName_Type())
osSnmpChangeCliNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:osSnmpChangeCliNodeName.setStatus(_A)
_OsSnmpCfg_ObjectIdentity=ObjectIdentity
osSnmpCfg=_OsSnmpCfg_ObjectIdentity((1,3,6,1,4,1,629,2544,7,2))
class _OsSnmpAlarmMangerMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OsSnmpAlarmMangerMode_Type.__name__=_D
_OsSnmpAlarmMangerMode_Object=MibScalar
osSnmpAlarmMangerMode=_OsSnmpAlarmMangerMode_Object((1,3,6,1,4,1,629,2544,7,2,1),_OsSnmpAlarmMangerMode_Type())
osSnmpAlarmMangerMode.setMaxAccess(_G)
if mibBuilder.loadTexts:osSnmpAlarmMangerMode.setStatus(_A)
class _OsSnmpChangeLogMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OsSnmpChangeLogMode_Type.__name__=_D
_OsSnmpChangeLogMode_Object=MibScalar
osSnmpChangeLogMode=_OsSnmpChangeLogMode_Object((1,3,6,1,4,1,629,2544,7,2,2),_OsSnmpChangeLogMode_Type())
osSnmpChangeLogMode.setMaxAccess(_G)
if mibBuilder.loadTexts:osSnmpChangeLogMode.setStatus(_A)
_OsSnmpConformance_ObjectIdentity=ObjectIdentity
osSnmpConformance=_OsSnmpConformance_ObjectIdentity((1,3,6,1,4,1,629,2544,7,100))
_OsSnmpMIBCompliances_ObjectIdentity=ObjectIdentity
osSnmpMIBCompliances=_OsSnmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,2544,7,100,1))
_OsSnmpMIBGroups_ObjectIdentity=ObjectIdentity
osSnmpMIBGroups=_OsSnmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,2544,7,100,2))
osSnmpMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,2544,7,100,2,1))
osSnmpMandatoryGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:osSnmpMandatoryGroup.setStatus(_A)
osSnmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,2544,7,100,1,1))
osSnmpMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:osSnmpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osSnmp':osSnmp,'osSnmpNotificationObjects':osSnmpNotificationObjects,_H:osSnmpChangeSourceAddress,_I:osSnmpChangeV2Community,_J:osSnmpChangeV3User,_K:osSnmpChangeCliUser,_L:osSnmpChangeCliCommand,_M:osSnmpChangeCliNodeName,'osSnmpCfg':osSnmpCfg,_N:osSnmpAlarmMangerMode,_O:osSnmpChangeLogMode,'osSnmpConformance':osSnmpConformance,'osSnmpMIBCompliances':osSnmpMIBCompliances,'osSnmpMIBCompliance':osSnmpMIBCompliance,'osSnmpMIBGroups':osSnmpMIBGroups,_P:osSnmpMandatoryGroup})