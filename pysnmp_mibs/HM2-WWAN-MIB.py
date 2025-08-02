_q='hm2WwanSimCardStatus'
_p='hm2WwanSimCardPin1Status'
_o='hm2WwanDataPlanMonthlyUsageRx'
_n='hm2WwanDataPlanMonthlyUsageTx'
_m='hm2WwanDataPlanLimitMeasureUnit'
_l='hm2WwanDataPlanMonthlyLimit'
_k='hm2WwanDataPlanWarningThreshold'
_j='hm2WwanDataConnectionApnCurrent'
_i='hm2WwanDataConnectionStatus'
_h='hm2WwanCellularRegistration'
_g='hm2WwanLtePersistenceInterval'
_f='hm2WwanLtePersistence'
_e='hm2WwanCellularOperator'
_d='hm2WwanCellularRoamingStatus'
_c='Hm2SimCardRole'
_b='hm2WwanSimCardSimId'
_a='hm2WwanDataPacketStatsSimId'
_Z='Hm2LimitUnit'
_Y='hm2WwanDataPlanSimId'
_X='Hm2PdpType'
_W='Hm2AuthType'
_V='hm2WwanDataConnectionSimId'
_U='Hm2TrapBits'
_T='Hm2TechnologyLevel'
_S='Hm2CellularNetworks'
_R='unknown'
_Q='failure'
_P='Unsigned32'
_O='lte'
_N='HmActionValue'
_M='not-accessible'
_L='InetAddressType'
_K='00000000'
_J='hm2WwanSimCardRoleCurrent'
_I='Integer32'
_H='InetAddress'
_G='hm2WwanCellularActiveSimId'
_F='HmEnabledStatus'
_E='SnmpAdminString'
_D='HM2-WWAN-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmActionValue,HmEnabledStatus,HmLargeDisplayString,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_N,_F,'HmLargeDisplayString','HmTimeSeconds1970','hm2ConfigurationMibs')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2WwanMib=ModuleIdentity((1,3,6,1,4,1,248,11,125))
if mibBuilder.loadTexts:hm2WwanMib.setRevisions(('2015-05-29 12:00',))
class Hm2CellularNetworks(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('auto',1),('gsm',2),('umts',3),(_O,4),('gsmumts',5),('gsmlte',6),('umtslte',7),('none',8)))
class Hm2TechnologyLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('utms',2)))
class Hm2AuthType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('pap',2),('chap',3),('papchap',4)))
class Hm2PdpType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('ipv4v6',3)))
class Hm2ConnectionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',1),('active',2),('idle',3),('connecting',4),('reconnecting',5),(_Q,6)))
class Hm2LimitUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('kb',1),('mb',2),('gb',3)))
class Hm2SimCardRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('primary',2),('backup',3)))
class Hm2SimCardStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('simPresent',1),('simAbsent',2),('simLocked',3),('simUnlocked',4),('simInactive',5),('simActive',6)))
class Hm2Pin1Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notVerified',1),('verified',2),('blocked',3),('disabled',4),('wrongCode',5)))
class Hm2RegistrationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notRegistered',1),('registering',2),('registered',3),(_Q,4)))
class Hm2RoamingStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('home',1),('roaming',2),('roamingDisabled',3)))
class Hm2TrapBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('roamingActive',0),('ltePersistenceSwitch',1),('cellularRegistrationFailed',2),('dataConnectionSetup',3),('dataPlanWarningThreshold',4),('simPin1Status',5),('failoverConnectionBackupSim',6),('failoverRegistrationBackupSim',7),('failoverRoamingBackupSim',8),('failoverDataLimitBackupSim',9),('failoverRegistrationModemReset',10)))
class Hm2SimCardsListIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('sim1',0),('sim2',1),('sim3',2),('sim4',3)))
class Hm2SimCardsListActive(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noSim',0),('sim1',1),('sim2',2),('sim3',3),('sim4',4)))
class Hm2ModemOperationalState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*(('online',0),('low-power',1),('offline',2),('reset',3),('shutting-down',4),('persistent-low-power',5),(_R,255)))
class Hm2CellularDataTech(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_R,0),('gsm',1),('umts',2),('edge',3),('hsdpa',4),('hsupa',5),('hsdpa-hsupda',6),(_O,7),('hsdpaplus',8),('hsdpaplus-hsupa',9),('dchsdpaplus',10),('dchsdpaplus-hsupa',11)))
_Hm2WwanMibNotifications_ObjectIdentity=ObjectIdentity
hm2WwanMibNotifications=_Hm2WwanMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,125,0))
_Hm2WwanMibObjects_ObjectIdentity=ObjectIdentity
hm2WwanMibObjects=_Hm2WwanMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,125,1))
_Hm2WwanGeneralGroup_ObjectIdentity=ObjectIdentity
hm2WwanGeneralGroup=_Hm2WwanGeneralGroup_ObjectIdentity((1,3,6,1,4,1,248,11,125,1,1))
class _Hm2WwanAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanAdminStatus_Type.__name__=_F
_Hm2WwanAdminStatus_Object=MibScalar
hm2WwanAdminStatus=_Hm2WwanAdminStatus_Object((1,3,6,1,4,1,248,11,125,1,1,1),_Hm2WwanAdminStatus_Type())
hm2WwanAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanAdminStatus.setStatus(_A)
class _Hm2WwanCellularSelection_Type(Hm2CellularNetworks):defaultValue=1
_Hm2WwanCellularSelection_Type.__name__=_S
_Hm2WwanCellularSelection_Object=MibScalar
hm2WwanCellularSelection=_Hm2WwanCellularSelection_Object((1,3,6,1,4,1,248,11,125,1,1,2),_Hm2WwanCellularSelection_Type())
hm2WwanCellularSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanCellularSelection.setStatus(_A)
class _Hm2WwanLtePersistence_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanLtePersistence_Type.__name__=_F
_Hm2WwanLtePersistence_Object=MibScalar
hm2WwanLtePersistence=_Hm2WwanLtePersistence_Object((1,3,6,1,4,1,248,11,125,1,1,4),_Hm2WwanLtePersistence_Type())
hm2WwanLtePersistence.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanLtePersistence.setStatus(_A)
class _Hm2WwanLtePersistenceInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_Hm2WwanLtePersistenceInterval_Type.__name__=_I
_Hm2WwanLtePersistenceInterval_Object=MibScalar
hm2WwanLtePersistenceInterval=_Hm2WwanLtePersistenceInterval_Object((1,3,6,1,4,1,248,11,125,1,1,5),_Hm2WwanLtePersistenceInterval_Type())
hm2WwanLtePersistenceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanLtePersistenceInterval.setStatus(_A)
class _Hm2WwanFailoverTechnologyLevel_Type(Hm2TechnologyLevel):defaultValue=2
_Hm2WwanFailoverTechnologyLevel_Type.__name__=_T
_Hm2WwanFailoverTechnologyLevel_Object=MibScalar
hm2WwanFailoverTechnologyLevel=_Hm2WwanFailoverTechnologyLevel_Object((1,3,6,1,4,1,248,11,125,1,1,6),_Hm2WwanFailoverTechnologyLevel_Type())
hm2WwanFailoverTechnologyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanFailoverTechnologyLevel.setStatus(_A)
class _Hm2WwanBackupSimFailoverConnection_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanBackupSimFailoverConnection_Type.__name__=_F
_Hm2WwanBackupSimFailoverConnection_Object=MibScalar
hm2WwanBackupSimFailoverConnection=_Hm2WwanBackupSimFailoverConnection_Object((1,3,6,1,4,1,248,11,125,1,1,7),_Hm2WwanBackupSimFailoverConnection_Type())
hm2WwanBackupSimFailoverConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverConnection.setStatus(_A)
class _Hm2WwanBackupSimFailoverRegistration_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanBackupSimFailoverRegistration_Type.__name__=_F
_Hm2WwanBackupSimFailoverRegistration_Object=MibScalar
hm2WwanBackupSimFailoverRegistration=_Hm2WwanBackupSimFailoverRegistration_Object((1,3,6,1,4,1,248,11,125,1,1,8),_Hm2WwanBackupSimFailoverRegistration_Type())
hm2WwanBackupSimFailoverRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverRegistration.setStatus(_A)
class _Hm2WwanBackupSimFailoverRoaming_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanBackupSimFailoverRoaming_Type.__name__=_F
_Hm2WwanBackupSimFailoverRoaming_Object=MibScalar
hm2WwanBackupSimFailoverRoaming=_Hm2WwanBackupSimFailoverRoaming_Object((1,3,6,1,4,1,248,11,125,1,1,9),_Hm2WwanBackupSimFailoverRoaming_Type())
hm2WwanBackupSimFailoverRoaming.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverRoaming.setStatus(_A)
class _Hm2WwanBackupSimFailoverDataLimit_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanBackupSimFailoverDataLimit_Type.__name__=_F
_Hm2WwanBackupSimFailoverDataLimit_Object=MibScalar
hm2WwanBackupSimFailoverDataLimit=_Hm2WwanBackupSimFailoverDataLimit_Object((1,3,6,1,4,1,248,11,125,1,1,10),_Hm2WwanBackupSimFailoverDataLimit_Type())
hm2WwanBackupSimFailoverDataLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverDataLimit.setStatus(_A)
class _Hm2WwanModemResetFailoverRegistration_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanModemResetFailoverRegistration_Type.__name__=_F
_Hm2WwanModemResetFailoverRegistration_Object=MibScalar
hm2WwanModemResetFailoverRegistration=_Hm2WwanModemResetFailoverRegistration_Object((1,3,6,1,4,1,248,11,125,1,1,11),_Hm2WwanModemResetFailoverRegistration_Type())
hm2WwanModemResetFailoverRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanModemResetFailoverRegistration.setStatus(_A)
class _Hm2WwanBackupSimTechnologyLevel_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanBackupSimTechnologyLevel_Type.__name__=_F
_Hm2WwanBackupSimTechnologyLevel_Object=MibScalar
hm2WwanBackupSimTechnologyLevel=_Hm2WwanBackupSimTechnologyLevel_Object((1,3,6,1,4,1,248,11,125,1,1,12),_Hm2WwanBackupSimTechnologyLevel_Type())
hm2WwanBackupSimTechnologyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanBackupSimTechnologyLevel.setStatus(_A)
class _Hm2WwanFailoverCycle_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanFailoverCycle_Type.__name__=_F
_Hm2WwanFailoverCycle_Object=MibScalar
hm2WwanFailoverCycle=_Hm2WwanFailoverCycle_Object((1,3,6,1,4,1,248,11,125,1,1,13),_Hm2WwanFailoverCycle_Type())
hm2WwanFailoverCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanFailoverCycle.setStatus(_A)
class _Hm2WwanSetTrap_Type(Hm2TrapBits):defaultBinValue='11111111111'
_Hm2WwanSetTrap_Type.__name__=_U
_Hm2WwanSetTrap_Object=MibScalar
hm2WwanSetTrap=_Hm2WwanSetTrap_Object((1,3,6,1,4,1,248,11,125,1,1,14),_Hm2WwanSetTrap_Type())
hm2WwanSetTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSetTrap.setStatus(_A)
_Hm2WwanDataGroup_ObjectIdentity=ObjectIdentity
hm2WwanDataGroup=_Hm2WwanDataGroup_ObjectIdentity((1,3,6,1,4,1,248,11,125,1,2))
_Hm2WwanDataConnectionTable_Object=MibTable
hm2WwanDataConnectionTable=_Hm2WwanDataConnectionTable_Object((1,3,6,1,4,1,248,11,125,1,2,1))
if mibBuilder.loadTexts:hm2WwanDataConnectionTable.setStatus(_A)
_Hm2WwanDataConnectionEntry_Object=MibTableRow
hm2WwanDataConnectionEntry=_Hm2WwanDataConnectionEntry_Object((1,3,6,1,4,1,248,11,125,1,2,1,1))
hm2WwanDataConnectionEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:hm2WwanDataConnectionEntry.setStatus(_A)
_Hm2WwanDataConnectionSimId_Type=Hm2SimCardsListIndex
_Hm2WwanDataConnectionSimId_Object=MibTableColumn
hm2WwanDataConnectionSimId=_Hm2WwanDataConnectionSimId_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,1),_Hm2WwanDataConnectionSimId_Type())
hm2WwanDataConnectionSimId.setMaxAccess(_M)
if mibBuilder.loadTexts:hm2WwanDataConnectionSimId.setStatus(_A)
class _Hm2WwanDataConnectionAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanDataConnectionAdminStatus_Type.__name__=_F
_Hm2WwanDataConnectionAdminStatus_Object=MibTableColumn
hm2WwanDataConnectionAdminStatus=_Hm2WwanDataConnectionAdminStatus_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,2),_Hm2WwanDataConnectionAdminStatus_Type())
hm2WwanDataConnectionAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionAdminStatus.setStatus(_A)
class _Hm2WwanDataConnectionApn_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2WwanDataConnectionApn_Type.__name__=_E
_Hm2WwanDataConnectionApn_Object=MibTableColumn
hm2WwanDataConnectionApn=_Hm2WwanDataConnectionApn_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,3),_Hm2WwanDataConnectionApn_Type())
hm2WwanDataConnectionApn.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionApn.setStatus(_A)
class _Hm2WwanDataConnectionApnCurrent_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2WwanDataConnectionApnCurrent_Type.__name__=_E
_Hm2WwanDataConnectionApnCurrent_Object=MibTableColumn
hm2WwanDataConnectionApnCurrent=_Hm2WwanDataConnectionApnCurrent_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,4),_Hm2WwanDataConnectionApnCurrent_Type())
hm2WwanDataConnectionApnCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionApnCurrent.setStatus(_A)
class _Hm2WwanDataConnectionUser_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2WwanDataConnectionUser_Type.__name__=_E
_Hm2WwanDataConnectionUser_Object=MibTableColumn
hm2WwanDataConnectionUser=_Hm2WwanDataConnectionUser_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,5),_Hm2WwanDataConnectionUser_Type())
hm2WwanDataConnectionUser.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionUser.setStatus(_A)
class _Hm2WwanDataConnectionPassword_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2WwanDataConnectionPassword_Type.__name__=_E
_Hm2WwanDataConnectionPassword_Object=MibTableColumn
hm2WwanDataConnectionPassword=_Hm2WwanDataConnectionPassword_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,6),_Hm2WwanDataConnectionPassword_Type())
hm2WwanDataConnectionPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionPassword.setStatus(_A)
class _Hm2WwanDataConnectionAuth_Type(Hm2AuthType):defaultValue=1
_Hm2WwanDataConnectionAuth_Type.__name__=_W
_Hm2WwanDataConnectionAuth_Object=MibTableColumn
hm2WwanDataConnectionAuth=_Hm2WwanDataConnectionAuth_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,7),_Hm2WwanDataConnectionAuth_Type())
hm2WwanDataConnectionAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionAuth.setStatus(_A)
class _Hm2WwanDataConnectionPdpType_Type(Hm2PdpType):defaultValue=1
_Hm2WwanDataConnectionPdpType_Type.__name__=_X
_Hm2WwanDataConnectionPdpType_Object=MibTableColumn
hm2WwanDataConnectionPdpType=_Hm2WwanDataConnectionPdpType_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,8),_Hm2WwanDataConnectionPdpType_Type())
hm2WwanDataConnectionPdpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionPdpType.setStatus(_A)
class _Hm2WwanDataConnectionIpAddressType_Type(InetAddressType):defaultValue=1
_Hm2WwanDataConnectionIpAddressType_Type.__name__=_L
_Hm2WwanDataConnectionIpAddressType_Object=MibTableColumn
hm2WwanDataConnectionIpAddressType=_Hm2WwanDataConnectionIpAddressType_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,9),_Hm2WwanDataConnectionIpAddressType_Type())
hm2WwanDataConnectionIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionIpAddressType.setStatus(_A)
class _Hm2WwanDataConnectionIpAddress_Type(InetAddress):defaultHexValue=_K
_Hm2WwanDataConnectionIpAddress_Type.__name__=_H
_Hm2WwanDataConnectionIpAddress_Object=MibTableColumn
hm2WwanDataConnectionIpAddress=_Hm2WwanDataConnectionIpAddress_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,10),_Hm2WwanDataConnectionIpAddress_Type())
hm2WwanDataConnectionIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionIpAddress.setStatus(_A)
class _Hm2WwanDataConnectionDnsPrimaryType_Type(InetAddressType):defaultValue=1
_Hm2WwanDataConnectionDnsPrimaryType_Type.__name__=_L
_Hm2WwanDataConnectionDnsPrimaryType_Object=MibTableColumn
hm2WwanDataConnectionDnsPrimaryType=_Hm2WwanDataConnectionDnsPrimaryType_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,11),_Hm2WwanDataConnectionDnsPrimaryType_Type())
hm2WwanDataConnectionDnsPrimaryType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsPrimaryType.setStatus(_A)
class _Hm2WwanDataConnectionDnsPrimary_Type(InetAddress):defaultHexValue=_K
_Hm2WwanDataConnectionDnsPrimary_Type.__name__=_H
_Hm2WwanDataConnectionDnsPrimary_Object=MibTableColumn
hm2WwanDataConnectionDnsPrimary=_Hm2WwanDataConnectionDnsPrimary_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,12),_Hm2WwanDataConnectionDnsPrimary_Type())
hm2WwanDataConnectionDnsPrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsPrimary.setStatus(_A)
class _Hm2WwanDataConnectionDnsSecondaryType_Type(InetAddressType):defaultValue=1
_Hm2WwanDataConnectionDnsSecondaryType_Type.__name__=_L
_Hm2WwanDataConnectionDnsSecondaryType_Object=MibTableColumn
hm2WwanDataConnectionDnsSecondaryType=_Hm2WwanDataConnectionDnsSecondaryType_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,13),_Hm2WwanDataConnectionDnsSecondaryType_Type())
hm2WwanDataConnectionDnsSecondaryType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsSecondaryType.setStatus(_A)
class _Hm2WwanDataConnectionDnsSecondary_Type(InetAddress):defaultHexValue=_K
_Hm2WwanDataConnectionDnsSecondary_Type.__name__=_H
_Hm2WwanDataConnectionDnsSecondary_Object=MibTableColumn
hm2WwanDataConnectionDnsSecondary=_Hm2WwanDataConnectionDnsSecondary_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,14),_Hm2WwanDataConnectionDnsSecondary_Type())
hm2WwanDataConnectionDnsSecondary.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsSecondary.setStatus(_A)
_Hm2WwanDataConnectionIpAddressCurrentType_Type=InetAddressType
_Hm2WwanDataConnectionIpAddressCurrentType_Object=MibTableColumn
hm2WwanDataConnectionIpAddressCurrentType=_Hm2WwanDataConnectionIpAddressCurrentType_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,15),_Hm2WwanDataConnectionIpAddressCurrentType_Type())
hm2WwanDataConnectionIpAddressCurrentType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionIpAddressCurrentType.setStatus(_A)
class _Hm2WwanDataConnectionIpAddressCurrent_Type(InetAddress):defaultHexValue=_K
_Hm2WwanDataConnectionIpAddressCurrent_Type.__name__=_H
_Hm2WwanDataConnectionIpAddressCurrent_Object=MibTableColumn
hm2WwanDataConnectionIpAddressCurrent=_Hm2WwanDataConnectionIpAddressCurrent_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,16),_Hm2WwanDataConnectionIpAddressCurrent_Type())
hm2WwanDataConnectionIpAddressCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionIpAddressCurrent.setStatus(_A)
_Hm2WwanDataConnectionDnsPrimaryCurrentType_Type=InetAddressType
_Hm2WwanDataConnectionDnsPrimaryCurrentType_Object=MibTableColumn
hm2WwanDataConnectionDnsPrimaryCurrentType=_Hm2WwanDataConnectionDnsPrimaryCurrentType_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,17),_Hm2WwanDataConnectionDnsPrimaryCurrentType_Type())
hm2WwanDataConnectionDnsPrimaryCurrentType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsPrimaryCurrentType.setStatus(_A)
class _Hm2WwanDataConnectionDnsPrimaryCurrent_Type(InetAddress):defaultHexValue=_K
_Hm2WwanDataConnectionDnsPrimaryCurrent_Type.__name__=_H
_Hm2WwanDataConnectionDnsPrimaryCurrent_Object=MibTableColumn
hm2WwanDataConnectionDnsPrimaryCurrent=_Hm2WwanDataConnectionDnsPrimaryCurrent_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,18),_Hm2WwanDataConnectionDnsPrimaryCurrent_Type())
hm2WwanDataConnectionDnsPrimaryCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsPrimaryCurrent.setStatus(_A)
_Hm2WwanDataConnectionDnsSecondaryCurrentType_Type=InetAddressType
_Hm2WwanDataConnectionDnsSecondaryCurrentType_Object=MibTableColumn
hm2WwanDataConnectionDnsSecondaryCurrentType=_Hm2WwanDataConnectionDnsSecondaryCurrentType_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,19),_Hm2WwanDataConnectionDnsSecondaryCurrentType_Type())
hm2WwanDataConnectionDnsSecondaryCurrentType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsSecondaryCurrentType.setStatus(_A)
class _Hm2WwanDataConnectionDnsSecondaryCurrent_Type(InetAddress):defaultHexValue=_K
_Hm2WwanDataConnectionDnsSecondaryCurrent_Type.__name__=_H
_Hm2WwanDataConnectionDnsSecondaryCurrent_Object=MibTableColumn
hm2WwanDataConnectionDnsSecondaryCurrent=_Hm2WwanDataConnectionDnsSecondaryCurrent_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,20),_Hm2WwanDataConnectionDnsSecondaryCurrent_Type())
hm2WwanDataConnectionDnsSecondaryCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionDnsSecondaryCurrent.setStatus(_A)
class _Hm2WwanDataConnectionMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_Hm2WwanDataConnectionMtu_Type.__name__=_I
_Hm2WwanDataConnectionMtu_Object=MibTableColumn
hm2WwanDataConnectionMtu=_Hm2WwanDataConnectionMtu_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,21),_Hm2WwanDataConnectionMtu_Type())
hm2WwanDataConnectionMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionMtu.setStatus(_A)
class _Hm2WwanDataConnectionFailedRetry_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,32))
_Hm2WwanDataConnectionFailedRetry_Type.__name__=_I
_Hm2WwanDataConnectionFailedRetry_Object=MibTableColumn
hm2WwanDataConnectionFailedRetry=_Hm2WwanDataConnectionFailedRetry_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,22),_Hm2WwanDataConnectionFailedRetry_Type())
hm2WwanDataConnectionFailedRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataConnectionFailedRetry.setStatus(_A)
_Hm2WwanDataConnectionFailedRetryCurrent_Type=Unsigned32
_Hm2WwanDataConnectionFailedRetryCurrent_Object=MibTableColumn
hm2WwanDataConnectionFailedRetryCurrent=_Hm2WwanDataConnectionFailedRetryCurrent_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,23),_Hm2WwanDataConnectionFailedRetryCurrent_Type())
hm2WwanDataConnectionFailedRetryCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionFailedRetryCurrent.setStatus(_A)
_Hm2WwanDataConnectionStatus_Type=Hm2ConnectionStatus
_Hm2WwanDataConnectionStatus_Object=MibTableColumn
hm2WwanDataConnectionStatus=_Hm2WwanDataConnectionStatus_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,24),_Hm2WwanDataConnectionStatus_Type())
hm2WwanDataConnectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionStatus.setStatus(_A)
_Hm2WwanDataConnectionStatusErrorReason_Type=HmLargeDisplayString
_Hm2WwanDataConnectionStatusErrorReason_Object=MibTableColumn
hm2WwanDataConnectionStatusErrorReason=_Hm2WwanDataConnectionStatusErrorReason_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,25),_Hm2WwanDataConnectionStatusErrorReason_Type())
hm2WwanDataConnectionStatusErrorReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionStatusErrorReason.setStatus(_A)
_Hm2WwanDataConnectionActivatedCount_Type=Unsigned32
_Hm2WwanDataConnectionActivatedCount_Object=MibTableColumn
hm2WwanDataConnectionActivatedCount=_Hm2WwanDataConnectionActivatedCount_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,26),_Hm2WwanDataConnectionActivatedCount_Type())
hm2WwanDataConnectionActivatedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionActivatedCount.setStatus(_A)
_Hm2WwanDataConnectionStartTime_Type=Unsigned32
_Hm2WwanDataConnectionStartTime_Object=MibTableColumn
hm2WwanDataConnectionStartTime=_Hm2WwanDataConnectionStartTime_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,27),_Hm2WwanDataConnectionStartTime_Type())
hm2WwanDataConnectionStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionStartTime.setStatus(_A)
_Hm2WwanDataConnectionUpTime_Type=Unsigned32
_Hm2WwanDataConnectionUpTime_Object=MibTableColumn
hm2WwanDataConnectionUpTime=_Hm2WwanDataConnectionUpTime_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,28),_Hm2WwanDataConnectionUpTime_Type())
hm2WwanDataConnectionUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionUpTime.setStatus(_A)
_Hm2WwanDataConnectionTotalUpTime_Type=Unsigned32
_Hm2WwanDataConnectionTotalUpTime_Object=MibTableColumn
hm2WwanDataConnectionTotalUpTime=_Hm2WwanDataConnectionTotalUpTime_Object((1,3,6,1,4,1,248,11,125,1,2,1,1,29),_Hm2WwanDataConnectionTotalUpTime_Type())
hm2WwanDataConnectionTotalUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataConnectionTotalUpTime.setStatus(_A)
_Hm2WwanDataPlanTable_Object=MibTable
hm2WwanDataPlanTable=_Hm2WwanDataPlanTable_Object((1,3,6,1,4,1,248,11,125,1,2,2))
if mibBuilder.loadTexts:hm2WwanDataPlanTable.setStatus(_A)
_Hm2WwanDataPlanEntry_Object=MibTableRow
hm2WwanDataPlanEntry=_Hm2WwanDataPlanEntry_Object((1,3,6,1,4,1,248,11,125,1,2,2,1))
hm2WwanDataPlanEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:hm2WwanDataPlanEntry.setStatus(_A)
_Hm2WwanDataPlanSimId_Type=Hm2SimCardsListIndex
_Hm2WwanDataPlanSimId_Object=MibTableColumn
hm2WwanDataPlanSimId=_Hm2WwanDataPlanSimId_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,1),_Hm2WwanDataPlanSimId_Type())
hm2WwanDataPlanSimId.setMaxAccess(_M)
if mibBuilder.loadTexts:hm2WwanDataPlanSimId.setStatus(_A)
class _Hm2WwanDataPlanMonthlyLimit_Type(Unsigned32):defaultValue=0
_Hm2WwanDataPlanMonthlyLimit_Type.__name__=_P
_Hm2WwanDataPlanMonthlyLimit_Object=MibTableColumn
hm2WwanDataPlanMonthlyLimit=_Hm2WwanDataPlanMonthlyLimit_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,2),_Hm2WwanDataPlanMonthlyLimit_Type())
hm2WwanDataPlanMonthlyLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataPlanMonthlyLimit.setStatus(_A)
class _Hm2WwanDataPlanLimitMeasureUnit_Type(Hm2LimitUnit):defaultValue=1
_Hm2WwanDataPlanLimitMeasureUnit_Type.__name__=_Z
_Hm2WwanDataPlanLimitMeasureUnit_Object=MibTableColumn
hm2WwanDataPlanLimitMeasureUnit=_Hm2WwanDataPlanLimitMeasureUnit_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,3),_Hm2WwanDataPlanLimitMeasureUnit_Type())
hm2WwanDataPlanLimitMeasureUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataPlanLimitMeasureUnit.setStatus(_A)
class _Hm2WwanDataPlanWarningThreshold_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2WwanDataPlanWarningThreshold_Type.__name__=_I
_Hm2WwanDataPlanWarningThreshold_Object=MibTableColumn
hm2WwanDataPlanWarningThreshold=_Hm2WwanDataPlanWarningThreshold_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,4),_Hm2WwanDataPlanWarningThreshold_Type())
hm2WwanDataPlanWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataPlanWarningThreshold.setStatus(_A)
class _Hm2WwanDataPlanReset_Type(HmActionValue):defaultValue=1
_Hm2WwanDataPlanReset_Type.__name__=_N
_Hm2WwanDataPlanReset_Object=MibTableColumn
hm2WwanDataPlanReset=_Hm2WwanDataPlanReset_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,5),_Hm2WwanDataPlanReset_Type())
hm2WwanDataPlanReset.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataPlanReset.setStatus(_A)
class _Hm2WwanDataPlanResetDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Hm2WwanDataPlanResetDay_Type.__name__=_I
_Hm2WwanDataPlanResetDay_Object=MibTableColumn
hm2WwanDataPlanResetDay=_Hm2WwanDataPlanResetDay_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,6),_Hm2WwanDataPlanResetDay_Type())
hm2WwanDataPlanResetDay.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataPlanResetDay.setStatus(_A)
_Hm2WwanDataPlanLastReset_Type=HmTimeSeconds1970
_Hm2WwanDataPlanLastReset_Object=MibTableColumn
hm2WwanDataPlanLastReset=_Hm2WwanDataPlanLastReset_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,7),_Hm2WwanDataPlanLastReset_Type())
hm2WwanDataPlanLastReset.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPlanLastReset.setStatus(_A)
class _Hm2WwanDataPlanCutoffThreshold_Type(Integer32):defaultValue=100
_Hm2WwanDataPlanCutoffThreshold_Type.__name__=_I
_Hm2WwanDataPlanCutoffThreshold_Object=MibTableColumn
hm2WwanDataPlanCutoffThreshold=_Hm2WwanDataPlanCutoffThreshold_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,8),_Hm2WwanDataPlanCutoffThreshold_Type())
hm2WwanDataPlanCutoffThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanDataPlanCutoffThreshold.setStatus(_A)
_Hm2WwanDataPlanMonthlyUsageTx_Type=Counter64
_Hm2WwanDataPlanMonthlyUsageTx_Object=MibTableColumn
hm2WwanDataPlanMonthlyUsageTx=_Hm2WwanDataPlanMonthlyUsageTx_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,9),_Hm2WwanDataPlanMonthlyUsageTx_Type())
hm2WwanDataPlanMonthlyUsageTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPlanMonthlyUsageTx.setStatus(_A)
_Hm2WwanDataPlanMonthlyUsageRx_Type=Counter64
_Hm2WwanDataPlanMonthlyUsageRx_Object=MibTableColumn
hm2WwanDataPlanMonthlyUsageRx=_Hm2WwanDataPlanMonthlyUsageRx_Object((1,3,6,1,4,1,248,11,125,1,2,2,1,10),_Hm2WwanDataPlanMonthlyUsageRx_Type())
hm2WwanDataPlanMonthlyUsageRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPlanMonthlyUsageRx.setStatus(_A)
_Hm2WwanDataPacketStatsTable_Object=MibTable
hm2WwanDataPacketStatsTable=_Hm2WwanDataPacketStatsTable_Object((1,3,6,1,4,1,248,11,125,1,2,3))
if mibBuilder.loadTexts:hm2WwanDataPacketStatsTable.setStatus(_A)
_Hm2WwanDataPacketStatsEntry_Object=MibTableRow
hm2WwanDataPacketStatsEntry=_Hm2WwanDataPacketStatsEntry_Object((1,3,6,1,4,1,248,11,125,1,2,3,1))
hm2WwanDataPacketStatsEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:hm2WwanDataPacketStatsEntry.setStatus(_A)
_Hm2WwanDataPacketStatsSimId_Type=Hm2SimCardsListIndex
_Hm2WwanDataPacketStatsSimId_Object=MibTableColumn
hm2WwanDataPacketStatsSimId=_Hm2WwanDataPacketStatsSimId_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,1),_Hm2WwanDataPacketStatsSimId_Type())
hm2WwanDataPacketStatsSimId.setMaxAccess(_M)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsSimId.setStatus(_A)
_Hm2WwanDataPacketStatsTxOk_Type=Counter64
_Hm2WwanDataPacketStatsTxOk_Object=MibTableColumn
hm2WwanDataPacketStatsTxOk=_Hm2WwanDataPacketStatsTxOk_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,2),_Hm2WwanDataPacketStatsTxOk_Type())
hm2WwanDataPacketStatsTxOk.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsTxOk.setStatus(_A)
_Hm2WwanDataPacketStatsRxOk_Type=Counter64
_Hm2WwanDataPacketStatsRxOk_Object=MibTableColumn
hm2WwanDataPacketStatsRxOk=_Hm2WwanDataPacketStatsRxOk_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,3),_Hm2WwanDataPacketStatsRxOk_Type())
hm2WwanDataPacketStatsRxOk.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsRxOk.setStatus(_A)
_Hm2WwanDataPacketStatsTxErrors_Type=Counter64
_Hm2WwanDataPacketStatsTxErrors_Object=MibTableColumn
hm2WwanDataPacketStatsTxErrors=_Hm2WwanDataPacketStatsTxErrors_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,4),_Hm2WwanDataPacketStatsTxErrors_Type())
hm2WwanDataPacketStatsTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsTxErrors.setStatus(_A)
_Hm2WwanDataPacketStatsRxErrors_Type=Counter64
_Hm2WwanDataPacketStatsRxErrors_Object=MibTableColumn
hm2WwanDataPacketStatsRxErrors=_Hm2WwanDataPacketStatsRxErrors_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,5),_Hm2WwanDataPacketStatsRxErrors_Type())
hm2WwanDataPacketStatsRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsRxErrors.setStatus(_A)
_Hm2WwanDataPacketStatsTxOverflows_Type=Counter64
_Hm2WwanDataPacketStatsTxOverflows_Object=MibTableColumn
hm2WwanDataPacketStatsTxOverflows=_Hm2WwanDataPacketStatsTxOverflows_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,6),_Hm2WwanDataPacketStatsTxOverflows_Type())
hm2WwanDataPacketStatsTxOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsTxOverflows.setStatus(_A)
_Hm2WwanDataPacketStatsRxOverflows_Type=Counter64
_Hm2WwanDataPacketStatsRxOverflows_Object=MibTableColumn
hm2WwanDataPacketStatsRxOverflows=_Hm2WwanDataPacketStatsRxOverflows_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,7),_Hm2WwanDataPacketStatsRxOverflows_Type())
hm2WwanDataPacketStatsRxOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsRxOverflows.setStatus(_A)
_Hm2WwanDataPacketStatsTxBytesOk_Type=Counter64
_Hm2WwanDataPacketStatsTxBytesOk_Object=MibTableColumn
hm2WwanDataPacketStatsTxBytesOk=_Hm2WwanDataPacketStatsTxBytesOk_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,8),_Hm2WwanDataPacketStatsTxBytesOk_Type())
hm2WwanDataPacketStatsTxBytesOk.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsTxBytesOk.setStatus(_A)
_Hm2WwanDataPacketStatsRxBytesOk_Type=Counter64
_Hm2WwanDataPacketStatsRxBytesOk_Object=MibTableColumn
hm2WwanDataPacketStatsRxBytesOk=_Hm2WwanDataPacketStatsRxBytesOk_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,9),_Hm2WwanDataPacketStatsRxBytesOk_Type())
hm2WwanDataPacketStatsRxBytesOk.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsRxBytesOk.setStatus(_A)
_Hm2WwanDataPacketStatsTxDropped_Type=Counter64
_Hm2WwanDataPacketStatsTxDropped_Object=MibTableColumn
hm2WwanDataPacketStatsTxDropped=_Hm2WwanDataPacketStatsTxDropped_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,10),_Hm2WwanDataPacketStatsTxDropped_Type())
hm2WwanDataPacketStatsTxDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsTxDropped.setStatus(_A)
_Hm2WwanDataPacketStatsRxDropped_Type=Counter64
_Hm2WwanDataPacketStatsRxDropped_Object=MibTableColumn
hm2WwanDataPacketStatsRxDropped=_Hm2WwanDataPacketStatsRxDropped_Object((1,3,6,1,4,1,248,11,125,1,2,3,1,11),_Hm2WwanDataPacketStatsRxDropped_Type())
hm2WwanDataPacketStatsRxDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanDataPacketStatsRxDropped.setStatus(_A)
_Hm2WwanSimCardGroup_ObjectIdentity=ObjectIdentity
hm2WwanSimCardGroup=_Hm2WwanSimCardGroup_ObjectIdentity((1,3,6,1,4,1,248,11,125,1,3))
_Hm2WwanSimCardTable_Object=MibTable
hm2WwanSimCardTable=_Hm2WwanSimCardTable_Object((1,3,6,1,4,1,248,11,125,1,3,1))
if mibBuilder.loadTexts:hm2WwanSimCardTable.setStatus(_A)
_Hm2WwanSimCardEntry_Object=MibTableRow
hm2WwanSimCardEntry=_Hm2WwanSimCardEntry_Object((1,3,6,1,4,1,248,11,125,1,3,1,1))
hm2WwanSimCardEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:hm2WwanSimCardEntry.setStatus(_A)
_Hm2WwanSimCardSimId_Type=Hm2SimCardsListIndex
_Hm2WwanSimCardSimId_Object=MibTableColumn
hm2WwanSimCardSimId=_Hm2WwanSimCardSimId_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,1),_Hm2WwanSimCardSimId_Type())
hm2WwanSimCardSimId.setMaxAccess(_M)
if mibBuilder.loadTexts:hm2WwanSimCardSimId.setStatus(_A)
class _Hm2WwanSimCardAdminStatus_Type(HmEnabledStatus):defaultValue=1
_Hm2WwanSimCardAdminStatus_Type.__name__=_F
_Hm2WwanSimCardAdminStatus_Object=MibTableColumn
hm2WwanSimCardAdminStatus=_Hm2WwanSimCardAdminStatus_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,2),_Hm2WwanSimCardAdminStatus_Type())
hm2WwanSimCardAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardAdminStatus.setStatus(_A)
class _Hm2WwanSimCardRole_Type(Hm2SimCardRole):defaultValue=1
_Hm2WwanSimCardRole_Type.__name__=_c
_Hm2WwanSimCardRole_Object=MibTableColumn
hm2WwanSimCardRole=_Hm2WwanSimCardRole_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,3),_Hm2WwanSimCardRole_Type())
hm2WwanSimCardRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardRole.setStatus(_A)
_Hm2WwanSimCardRoleCurrent_Type=Hm2SimCardRole
_Hm2WwanSimCardRoleCurrent_Object=MibTableColumn
hm2WwanSimCardRoleCurrent=_Hm2WwanSimCardRoleCurrent_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,4),_Hm2WwanSimCardRoleCurrent_Type())
hm2WwanSimCardRoleCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanSimCardRoleCurrent.setStatus(_A)
_Hm2WwanSimCardStatus_Type=Hm2SimCardStatus
_Hm2WwanSimCardStatus_Object=MibTableColumn
hm2WwanSimCardStatus=_Hm2WwanSimCardStatus_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,5),_Hm2WwanSimCardStatus_Type())
hm2WwanSimCardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanSimCardStatus.setStatus(_A)
class _Hm2WwanSimCardSetActive_Type(HmActionValue):defaultValue=1
_Hm2WwanSimCardSetActive_Type.__name__=_N
_Hm2WwanSimCardSetActive_Object=MibTableColumn
hm2WwanSimCardSetActive=_Hm2WwanSimCardSetActive_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,6),_Hm2WwanSimCardSetActive_Type())
hm2WwanSimCardSetActive.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardSetActive.setStatus(_A)
class _Hm2WwanSimCardPin1_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,8))
_Hm2WwanSimCardPin1_Type.__name__=_E
_Hm2WwanSimCardPin1_Object=MibTableColumn
hm2WwanSimCardPin1=_Hm2WwanSimCardPin1_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,7),_Hm2WwanSimCardPin1_Type())
hm2WwanSimCardPin1.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardPin1.setStatus(_A)
_Hm2WwanSimCardPin1Mode_Type=HmEnabledStatus
_Hm2WwanSimCardPin1Mode_Object=MibTableColumn
hm2WwanSimCardPin1Mode=_Hm2WwanSimCardPin1Mode_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,8),_Hm2WwanSimCardPin1Mode_Type())
hm2WwanSimCardPin1Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardPin1Mode.setStatus(_A)
_Hm2WwanSimCardPin1Status_Type=Hm2Pin1Status
_Hm2WwanSimCardPin1Status_Object=MibTableColumn
hm2WwanSimCardPin1Status=_Hm2WwanSimCardPin1Status_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,9),_Hm2WwanSimCardPin1Status_Type())
hm2WwanSimCardPin1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanSimCardPin1Status.setStatus(_A)
_Hm2WwanSimCardPin1VerifyTries_Type=Integer32
_Hm2WwanSimCardPin1VerifyTries_Object=MibTableColumn
hm2WwanSimCardPin1VerifyTries=_Hm2WwanSimCardPin1VerifyTries_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,10),_Hm2WwanSimCardPin1VerifyTries_Type())
hm2WwanSimCardPin1VerifyTries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanSimCardPin1VerifyTries.setStatus(_A)
_Hm2WwanSimCardPin1UnblockTries_Type=Integer32
_Hm2WwanSimCardPin1UnblockTries_Object=MibTableColumn
hm2WwanSimCardPin1UnblockTries=_Hm2WwanSimCardPin1UnblockTries_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,11),_Hm2WwanSimCardPin1UnblockTries_Type())
hm2WwanSimCardPin1UnblockTries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanSimCardPin1UnblockTries.setStatus(_A)
class _Hm2WwanSimCardPuk1_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Hm2WwanSimCardPuk1_Type.__name__=_E
_Hm2WwanSimCardPuk1_Object=MibTableColumn
hm2WwanSimCardPuk1=_Hm2WwanSimCardPuk1_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,12),_Hm2WwanSimCardPuk1_Type())
hm2WwanSimCardPuk1.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardPuk1.setStatus(_A)
class _Hm2WwanSimCardRoamingMode_Type(HmEnabledStatus):defaultValue=2
_Hm2WwanSimCardRoamingMode_Type.__name__=_F
_Hm2WwanSimCardRoamingMode_Object=MibTableColumn
hm2WwanSimCardRoamingMode=_Hm2WwanSimCardRoamingMode_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,13),_Hm2WwanSimCardRoamingMode_Type())
hm2WwanSimCardRoamingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardRoamingMode.setStatus(_A)
class _Hm2WwanSimCardIccid_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(22,22))
_Hm2WwanSimCardIccid_Type.__name__=_E
_Hm2WwanSimCardIccid_Object=MibTableColumn
hm2WwanSimCardIccid=_Hm2WwanSimCardIccid_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,14),_Hm2WwanSimCardIccid_Type())
hm2WwanSimCardIccid.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2WwanSimCardIccid.setStatus(_A)
class _Hm2WwanSimCardImsi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(15,15))
_Hm2WwanSimCardImsi_Type.__name__=_E
_Hm2WwanSimCardImsi_Object=MibTableColumn
hm2WwanSimCardImsi=_Hm2WwanSimCardImsi_Object((1,3,6,1,4,1,248,11,125,1,3,1,1,15),_Hm2WwanSimCardImsi_Type())
hm2WwanSimCardImsi.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanSimCardImsi.setStatus(_A)
_Hm2WwanInformationGroup_ObjectIdentity=ObjectIdentity
hm2WwanInformationGroup=_Hm2WwanInformationGroup_ObjectIdentity((1,3,6,1,4,1,248,11,125,1,4))
_Hm2WwanCellularInformationGroup_ObjectIdentity=ObjectIdentity
hm2WwanCellularInformationGroup=_Hm2WwanCellularInformationGroup_ObjectIdentity((1,3,6,1,4,1,248,11,125,1,4,1))
_Hm2WwanCellularActiveSimId_Type=Hm2SimCardsListActive
_Hm2WwanCellularActiveSimId_Object=MibScalar
hm2WwanCellularActiveSimId=_Hm2WwanCellularActiveSimId_Object((1,3,6,1,4,1,248,11,125,1,4,1,1),_Hm2WwanCellularActiveSimId_Type())
hm2WwanCellularActiveSimId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularActiveSimId.setStatus(_A)
_Hm2WwanCellularRegistration_Type=Hm2RegistrationStatus
_Hm2WwanCellularRegistration_Object=MibScalar
hm2WwanCellularRegistration=_Hm2WwanCellularRegistration_Object((1,3,6,1,4,1,248,11,125,1,4,1,2),_Hm2WwanCellularRegistration_Type())
hm2WwanCellularRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularRegistration.setStatus(_A)
class _Hm2WwanCellularOperator_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2WwanCellularOperator_Type.__name__=_E
_Hm2WwanCellularOperator_Object=MibScalar
hm2WwanCellularOperator=_Hm2WwanCellularOperator_Object((1,3,6,1,4,1,248,11,125,1,4,1,3),_Hm2WwanCellularOperator_Type())
hm2WwanCellularOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularOperator.setStatus(_A)
_Hm2WwanCellularNetwork_Type=Hm2CellularNetworks
_Hm2WwanCellularNetwork_Object=MibScalar
hm2WwanCellularNetwork=_Hm2WwanCellularNetwork_Object((1,3,6,1,4,1,248,11,125,1,4,1,4),_Hm2WwanCellularNetwork_Type())
hm2WwanCellularNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularNetwork.setStatus(_A)
_Hm2WwanCellularMcc_Type=Integer32
_Hm2WwanCellularMcc_Object=MibScalar
hm2WwanCellularMcc=_Hm2WwanCellularMcc_Object((1,3,6,1,4,1,248,11,125,1,4,1,5),_Hm2WwanCellularMcc_Type())
hm2WwanCellularMcc.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularMcc.setStatus(_A)
_Hm2WwanCellularMnc_Type=Integer32
_Hm2WwanCellularMnc_Object=MibScalar
hm2WwanCellularMnc=_Hm2WwanCellularMnc_Object((1,3,6,1,4,1,248,11,125,1,4,1,6),_Hm2WwanCellularMnc_Type())
hm2WwanCellularMnc.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularMnc.setStatus(_A)
_Hm2WwanCellularLac_Type=Integer32
_Hm2WwanCellularLac_Object=MibScalar
hm2WwanCellularLac=_Hm2WwanCellularLac_Object((1,3,6,1,4,1,248,11,125,1,4,1,7),_Hm2WwanCellularLac_Type())
hm2WwanCellularLac.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularLac.setStatus(_A)
_Hm2WwanCellularBsic_Type=Integer32
_Hm2WwanCellularBsic_Object=MibScalar
hm2WwanCellularBsic=_Hm2WwanCellularBsic_Object((1,3,6,1,4,1,248,11,125,1,4,1,8),_Hm2WwanCellularBsic_Type())
hm2WwanCellularBsic.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularBsic.setStatus(_A)
_Hm2WwanCellularCellId_Type=Integer32
_Hm2WwanCellularCellId_Object=MibScalar
hm2WwanCellularCellId=_Hm2WwanCellularCellId_Object((1,3,6,1,4,1,248,11,125,1,4,1,9),_Hm2WwanCellularCellId_Type())
hm2WwanCellularCellId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularCellId.setStatus(_A)
_Hm2WwanCellularBand_Type=Integer32
_Hm2WwanCellularBand_Object=MibScalar
hm2WwanCellularBand=_Hm2WwanCellularBand_Object((1,3,6,1,4,1,248,11,125,1,4,1,10),_Hm2WwanCellularBand_Type())
hm2WwanCellularBand.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularBand.setStatus(_A)
_Hm2WwanCellularChannel_Type=Integer32
_Hm2WwanCellularChannel_Object=MibScalar
hm2WwanCellularChannel=_Hm2WwanCellularChannel_Object((1,3,6,1,4,1,248,11,125,1,4,1,11),_Hm2WwanCellularChannel_Type())
hm2WwanCellularChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularChannel.setStatus(_A)
_Hm2WwanCellularSignalStrength_Type=Integer32
_Hm2WwanCellularSignalStrength_Object=MibScalar
hm2WwanCellularSignalStrength=_Hm2WwanCellularSignalStrength_Object((1,3,6,1,4,1,248,11,125,1,4,1,12),_Hm2WwanCellularSignalStrength_Type())
hm2WwanCellularSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularSignalStrength.setStatus(_A)
_Hm2WwanCellularSignalStrengthLte_Type=Integer32
_Hm2WwanCellularSignalStrengthLte_Object=MibScalar
hm2WwanCellularSignalStrengthLte=_Hm2WwanCellularSignalStrengthLte_Object((1,3,6,1,4,1,248,11,125,1,4,1,13),_Hm2WwanCellularSignalStrengthLte_Type())
hm2WwanCellularSignalStrengthLte.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularSignalStrengthLte.setStatus(_A)
_Hm2WwanCellularSignalQuality_Type=Integer32
_Hm2WwanCellularSignalQuality_Object=MibScalar
hm2WwanCellularSignalQuality=_Hm2WwanCellularSignalQuality_Object((1,3,6,1,4,1,248,11,125,1,4,1,14),_Hm2WwanCellularSignalQuality_Type())
hm2WwanCellularSignalQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularSignalQuality.setStatus(_A)
_Hm2WwanCellularSignalQualityLte_Type=Integer32
_Hm2WwanCellularSignalQualityLte_Object=MibScalar
hm2WwanCellularSignalQualityLte=_Hm2WwanCellularSignalQualityLte_Object((1,3,6,1,4,1,248,11,125,1,4,1,15),_Hm2WwanCellularSignalQualityLte_Type())
hm2WwanCellularSignalQualityLte.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularSignalQualityLte.setStatus(_A)
_Hm2WwanCellularRoamingStatus_Type=Hm2RoamingStatus
_Hm2WwanCellularRoamingStatus_Object=MibScalar
hm2WwanCellularRoamingStatus=_Hm2WwanCellularRoamingStatus_Object((1,3,6,1,4,1,248,11,125,1,4,1,16),_Hm2WwanCellularRoamingStatus_Type())
hm2WwanCellularRoamingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularRoamingStatus.setStatus(_A)
_Hm2WwanCellularBitErrorRate_Type=Integer32
_Hm2WwanCellularBitErrorRate_Object=MibScalar
hm2WwanCellularBitErrorRate=_Hm2WwanCellularBitErrorRate_Object((1,3,6,1,4,1,248,11,125,1,4,1,17),_Hm2WwanCellularBitErrorRate_Type())
hm2WwanCellularBitErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularBitErrorRate.setStatus(_A)
_Hm2WwanCellularCurrentTxRate_Type=Unsigned32
_Hm2WwanCellularCurrentTxRate_Object=MibScalar
hm2WwanCellularCurrentTxRate=_Hm2WwanCellularCurrentTxRate_Object((1,3,6,1,4,1,248,11,125,1,4,1,18),_Hm2WwanCellularCurrentTxRate_Type())
hm2WwanCellularCurrentTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularCurrentTxRate.setStatus(_A)
_Hm2WwanCellularCurrentRxRate_Type=Unsigned32
_Hm2WwanCellularCurrentRxRate_Object=MibScalar
hm2WwanCellularCurrentRxRate=_Hm2WwanCellularCurrentRxRate_Object((1,3,6,1,4,1,248,11,125,1,4,1,19),_Hm2WwanCellularCurrentRxRate_Type())
hm2WwanCellularCurrentRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularCurrentRxRate.setStatus(_A)
_Hm2WwanCellularMaxTxRate_Type=Unsigned32
_Hm2WwanCellularMaxTxRate_Object=MibScalar
hm2WwanCellularMaxTxRate=_Hm2WwanCellularMaxTxRate_Object((1,3,6,1,4,1,248,11,125,1,4,1,20),_Hm2WwanCellularMaxTxRate_Type())
hm2WwanCellularMaxTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularMaxTxRate.setStatus(_A)
_Hm2WwanCellularMaxRxRate_Type=Unsigned32
_Hm2WwanCellularMaxRxRate_Object=MibScalar
hm2WwanCellularMaxRxRate=_Hm2WwanCellularMaxRxRate_Object((1,3,6,1,4,1,248,11,125,1,4,1,21),_Hm2WwanCellularMaxRxRate_Type())
hm2WwanCellularMaxRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularMaxRxRate.setStatus(_A)
_Hm2WwanCellularDataTech_Type=Hm2CellularDataTech
_Hm2WwanCellularDataTech_Object=MibScalar
hm2WwanCellularDataTech=_Hm2WwanCellularDataTech_Object((1,3,6,1,4,1,248,11,125,1,4,1,22),_Hm2WwanCellularDataTech_Type())
hm2WwanCellularDataTech.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanCellularDataTech.setStatus(_A)
_Hm2WwanModemInformationGroup_ObjectIdentity=ObjectIdentity
hm2WwanModemInformationGroup=_Hm2WwanModemInformationGroup_ObjectIdentity((1,3,6,1,4,1,248,11,125,1,4,2))
class _Hm2WwanModemManufacturer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2WwanModemManufacturer_Type.__name__=_E
_Hm2WwanModemManufacturer_Object=MibScalar
hm2WwanModemManufacturer=_Hm2WwanModemManufacturer_Object((1,3,6,1,4,1,248,11,125,1,4,2,1),_Hm2WwanModemManufacturer_Type())
hm2WwanModemManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanModemManufacturer.setStatus(_A)
class _Hm2WwanModemModel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2WwanModemModel_Type.__name__=_E
_Hm2WwanModemModel_Object=MibScalar
hm2WwanModemModel=_Hm2WwanModemModel_Object((1,3,6,1,4,1,248,11,125,1,4,2,2),_Hm2WwanModemModel_Type())
hm2WwanModemModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanModemModel.setStatus(_A)
class _Hm2WwanModemRevision_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2WwanModemRevision_Type.__name__=_E
_Hm2WwanModemRevision_Object=MibScalar
hm2WwanModemRevision=_Hm2WwanModemRevision_Object((1,3,6,1,4,1,248,11,125,1,4,2,3),_Hm2WwanModemRevision_Type())
hm2WwanModemRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanModemRevision.setStatus(_A)
class _Hm2WwanModemImei_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Hm2WwanModemImei_Type.__name__=_E
_Hm2WwanModemImei_Object=MibScalar
hm2WwanModemImei=_Hm2WwanModemImei_Object((1,3,6,1,4,1,248,11,125,1,4,2,4),_Hm2WwanModemImei_Type())
hm2WwanModemImei.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanModemImei.setStatus(_A)
_Hm2WwanModemOperationalState_Type=Hm2ModemOperationalState
_Hm2WwanModemOperationalState_Object=MibScalar
hm2WwanModemOperationalState=_Hm2WwanModemOperationalState_Object((1,3,6,1,4,1,248,11,125,1,4,2,5),_Hm2WwanModemOperationalState_Type())
hm2WwanModemOperationalState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2WwanModemOperationalState.setStatus(_A)
hm2WwanRoamingActiveTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,1))
hm2WwanRoamingActiveTrap.setObjects(*((_D,_d),(_D,_e),(_D,_G)))
if mibBuilder.loadTexts:hm2WwanRoamingActiveTrap.setStatus(_A)
hm2WwanLtePersistenceSwitchTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,2))
hm2WwanLtePersistenceSwitchTrap.setObjects(*((_D,_f),(_D,_g),(_D,_G)))
if mibBuilder.loadTexts:hm2WwanLtePersistenceSwitchTrap.setStatus(_A)
hm2WwanCelluarRegistrationFailedTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,3))
hm2WwanCelluarRegistrationFailedTrap.setObjects(*((_D,_h),(_D,_G)))
if mibBuilder.loadTexts:hm2WwanCelluarRegistrationFailedTrap.setStatus(_A)
hm2WwanDataConnectionSetupTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,4))
hm2WwanDataConnectionSetupTrap.setObjects(*((_D,_i),(_D,_G),(_D,_j)))
if mibBuilder.loadTexts:hm2WwanDataConnectionSetupTrap.setStatus(_A)
hm2WwanDataPlanWarningThresholdTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,5))
hm2WwanDataPlanWarningThresholdTrap.setObjects(*((_D,_k),(_D,_G),(_D,_l),(_D,_m),(_D,_n),(_D,_o)))
if mibBuilder.loadTexts:hm2WwanDataPlanWarningThresholdTrap.setStatus(_A)
hm2WwanSimCardPin1StatusTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,6))
hm2WwanSimCardPin1StatusTrap.setObjects(*((_D,_p),(_D,_G),(_D,_J),(_D,_q)))
if mibBuilder.loadTexts:hm2WwanSimCardPin1StatusTrap.setStatus(_A)
hm2WwanBackupSimFailoverConnectionTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,7))
hm2WwanBackupSimFailoverConnectionTrap.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverConnectionTrap.setStatus(_A)
hm2WwanBackupSimFailoverRegistrationTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,8))
hm2WwanBackupSimFailoverRegistrationTrap.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverRegistrationTrap.setStatus(_A)
hm2WwanBackupSimFailoverRoamingTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,9))
hm2WwanBackupSimFailoverRoamingTrap.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverRoamingTrap.setStatus(_A)
hm2WwanBackupSimFailoverDataLimitTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,10))
hm2WwanBackupSimFailoverDataLimitTrap.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:hm2WwanBackupSimFailoverDataLimitTrap.setStatus(_A)
hm2WwanModemResetFailoverRegistrationTrap=NotificationType((1,3,6,1,4,1,248,11,125,0,11))
hm2WwanModemResetFailoverRegistrationTrap.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:hm2WwanModemResetFailoverRegistrationTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_S:Hm2CellularNetworks,_T:Hm2TechnologyLevel,_W:Hm2AuthType,_X:Hm2PdpType,'Hm2ConnectionStatus':Hm2ConnectionStatus,_Z:Hm2LimitUnit,_c:Hm2SimCardRole,'Hm2SimCardStatus':Hm2SimCardStatus,'Hm2Pin1Status':Hm2Pin1Status,'Hm2RegistrationStatus':Hm2RegistrationStatus,'Hm2RoamingStatus':Hm2RoamingStatus,_U:Hm2TrapBits,'Hm2SimCardsListIndex':Hm2SimCardsListIndex,'Hm2SimCardsListActive':Hm2SimCardsListActive,'Hm2ModemOperationalState':Hm2ModemOperationalState,'Hm2CellularDataTech':Hm2CellularDataTech,'hm2WwanMib':hm2WwanMib,'hm2WwanMibNotifications':hm2WwanMibNotifications,'hm2WwanRoamingActiveTrap':hm2WwanRoamingActiveTrap,'hm2WwanLtePersistenceSwitchTrap':hm2WwanLtePersistenceSwitchTrap,'hm2WwanCelluarRegistrationFailedTrap':hm2WwanCelluarRegistrationFailedTrap,'hm2WwanDataConnectionSetupTrap':hm2WwanDataConnectionSetupTrap,'hm2WwanDataPlanWarningThresholdTrap':hm2WwanDataPlanWarningThresholdTrap,'hm2WwanSimCardPin1StatusTrap':hm2WwanSimCardPin1StatusTrap,'hm2WwanBackupSimFailoverConnectionTrap':hm2WwanBackupSimFailoverConnectionTrap,'hm2WwanBackupSimFailoverRegistrationTrap':hm2WwanBackupSimFailoverRegistrationTrap,'hm2WwanBackupSimFailoverRoamingTrap':hm2WwanBackupSimFailoverRoamingTrap,'hm2WwanBackupSimFailoverDataLimitTrap':hm2WwanBackupSimFailoverDataLimitTrap,'hm2WwanModemResetFailoverRegistrationTrap':hm2WwanModemResetFailoverRegistrationTrap,'hm2WwanMibObjects':hm2WwanMibObjects,'hm2WwanGeneralGroup':hm2WwanGeneralGroup,'hm2WwanAdminStatus':hm2WwanAdminStatus,'hm2WwanCellularSelection':hm2WwanCellularSelection,_f:hm2WwanLtePersistence,_g:hm2WwanLtePersistenceInterval,'hm2WwanFailoverTechnologyLevel':hm2WwanFailoverTechnologyLevel,'hm2WwanBackupSimFailoverConnection':hm2WwanBackupSimFailoverConnection,'hm2WwanBackupSimFailoverRegistration':hm2WwanBackupSimFailoverRegistration,'hm2WwanBackupSimFailoverRoaming':hm2WwanBackupSimFailoverRoaming,'hm2WwanBackupSimFailoverDataLimit':hm2WwanBackupSimFailoverDataLimit,'hm2WwanModemResetFailoverRegistration':hm2WwanModemResetFailoverRegistration,'hm2WwanBackupSimTechnologyLevel':hm2WwanBackupSimTechnologyLevel,'hm2WwanFailoverCycle':hm2WwanFailoverCycle,'hm2WwanSetTrap':hm2WwanSetTrap,'hm2WwanDataGroup':hm2WwanDataGroup,'hm2WwanDataConnectionTable':hm2WwanDataConnectionTable,'hm2WwanDataConnectionEntry':hm2WwanDataConnectionEntry,_V:hm2WwanDataConnectionSimId,'hm2WwanDataConnectionAdminStatus':hm2WwanDataConnectionAdminStatus,'hm2WwanDataConnectionApn':hm2WwanDataConnectionApn,_j:hm2WwanDataConnectionApnCurrent,'hm2WwanDataConnectionUser':hm2WwanDataConnectionUser,'hm2WwanDataConnectionPassword':hm2WwanDataConnectionPassword,'hm2WwanDataConnectionAuth':hm2WwanDataConnectionAuth,'hm2WwanDataConnectionPdpType':hm2WwanDataConnectionPdpType,'hm2WwanDataConnectionIpAddressType':hm2WwanDataConnectionIpAddressType,'hm2WwanDataConnectionIpAddress':hm2WwanDataConnectionIpAddress,'hm2WwanDataConnectionDnsPrimaryType':hm2WwanDataConnectionDnsPrimaryType,'hm2WwanDataConnectionDnsPrimary':hm2WwanDataConnectionDnsPrimary,'hm2WwanDataConnectionDnsSecondaryType':hm2WwanDataConnectionDnsSecondaryType,'hm2WwanDataConnectionDnsSecondary':hm2WwanDataConnectionDnsSecondary,'hm2WwanDataConnectionIpAddressCurrentType':hm2WwanDataConnectionIpAddressCurrentType,'hm2WwanDataConnectionIpAddressCurrent':hm2WwanDataConnectionIpAddressCurrent,'hm2WwanDataConnectionDnsPrimaryCurrentType':hm2WwanDataConnectionDnsPrimaryCurrentType,'hm2WwanDataConnectionDnsPrimaryCurrent':hm2WwanDataConnectionDnsPrimaryCurrent,'hm2WwanDataConnectionDnsSecondaryCurrentType':hm2WwanDataConnectionDnsSecondaryCurrentType,'hm2WwanDataConnectionDnsSecondaryCurrent':hm2WwanDataConnectionDnsSecondaryCurrent,'hm2WwanDataConnectionMtu':hm2WwanDataConnectionMtu,'hm2WwanDataConnectionFailedRetry':hm2WwanDataConnectionFailedRetry,'hm2WwanDataConnectionFailedRetryCurrent':hm2WwanDataConnectionFailedRetryCurrent,_i:hm2WwanDataConnectionStatus,'hm2WwanDataConnectionStatusErrorReason':hm2WwanDataConnectionStatusErrorReason,'hm2WwanDataConnectionActivatedCount':hm2WwanDataConnectionActivatedCount,'hm2WwanDataConnectionStartTime':hm2WwanDataConnectionStartTime,'hm2WwanDataConnectionUpTime':hm2WwanDataConnectionUpTime,'hm2WwanDataConnectionTotalUpTime':hm2WwanDataConnectionTotalUpTime,'hm2WwanDataPlanTable':hm2WwanDataPlanTable,'hm2WwanDataPlanEntry':hm2WwanDataPlanEntry,_Y:hm2WwanDataPlanSimId,_l:hm2WwanDataPlanMonthlyLimit,_m:hm2WwanDataPlanLimitMeasureUnit,_k:hm2WwanDataPlanWarningThreshold,'hm2WwanDataPlanReset':hm2WwanDataPlanReset,'hm2WwanDataPlanResetDay':hm2WwanDataPlanResetDay,'hm2WwanDataPlanLastReset':hm2WwanDataPlanLastReset,'hm2WwanDataPlanCutoffThreshold':hm2WwanDataPlanCutoffThreshold,_n:hm2WwanDataPlanMonthlyUsageTx,_o:hm2WwanDataPlanMonthlyUsageRx,'hm2WwanDataPacketStatsTable':hm2WwanDataPacketStatsTable,'hm2WwanDataPacketStatsEntry':hm2WwanDataPacketStatsEntry,_a:hm2WwanDataPacketStatsSimId,'hm2WwanDataPacketStatsTxOk':hm2WwanDataPacketStatsTxOk,'hm2WwanDataPacketStatsRxOk':hm2WwanDataPacketStatsRxOk,'hm2WwanDataPacketStatsTxErrors':hm2WwanDataPacketStatsTxErrors,'hm2WwanDataPacketStatsRxErrors':hm2WwanDataPacketStatsRxErrors,'hm2WwanDataPacketStatsTxOverflows':hm2WwanDataPacketStatsTxOverflows,'hm2WwanDataPacketStatsRxOverflows':hm2WwanDataPacketStatsRxOverflows,'hm2WwanDataPacketStatsTxBytesOk':hm2WwanDataPacketStatsTxBytesOk,'hm2WwanDataPacketStatsRxBytesOk':hm2WwanDataPacketStatsRxBytesOk,'hm2WwanDataPacketStatsTxDropped':hm2WwanDataPacketStatsTxDropped,'hm2WwanDataPacketStatsRxDropped':hm2WwanDataPacketStatsRxDropped,'hm2WwanSimCardGroup':hm2WwanSimCardGroup,'hm2WwanSimCardTable':hm2WwanSimCardTable,'hm2WwanSimCardEntry':hm2WwanSimCardEntry,_b:hm2WwanSimCardSimId,'hm2WwanSimCardAdminStatus':hm2WwanSimCardAdminStatus,'hm2WwanSimCardRole':hm2WwanSimCardRole,_J:hm2WwanSimCardRoleCurrent,_q:hm2WwanSimCardStatus,'hm2WwanSimCardSetActive':hm2WwanSimCardSetActive,'hm2WwanSimCardPin1':hm2WwanSimCardPin1,'hm2WwanSimCardPin1Mode':hm2WwanSimCardPin1Mode,_p:hm2WwanSimCardPin1Status,'hm2WwanSimCardPin1VerifyTries':hm2WwanSimCardPin1VerifyTries,'hm2WwanSimCardPin1UnblockTries':hm2WwanSimCardPin1UnblockTries,'hm2WwanSimCardPuk1':hm2WwanSimCardPuk1,'hm2WwanSimCardRoamingMode':hm2WwanSimCardRoamingMode,'hm2WwanSimCardIccid':hm2WwanSimCardIccid,'hm2WwanSimCardImsi':hm2WwanSimCardImsi,'hm2WwanInformationGroup':hm2WwanInformationGroup,'hm2WwanCellularInformationGroup':hm2WwanCellularInformationGroup,_G:hm2WwanCellularActiveSimId,_h:hm2WwanCellularRegistration,_e:hm2WwanCellularOperator,'hm2WwanCellularNetwork':hm2WwanCellularNetwork,'hm2WwanCellularMcc':hm2WwanCellularMcc,'hm2WwanCellularMnc':hm2WwanCellularMnc,'hm2WwanCellularLac':hm2WwanCellularLac,'hm2WwanCellularBsic':hm2WwanCellularBsic,'hm2WwanCellularCellId':hm2WwanCellularCellId,'hm2WwanCellularBand':hm2WwanCellularBand,'hm2WwanCellularChannel':hm2WwanCellularChannel,'hm2WwanCellularSignalStrength':hm2WwanCellularSignalStrength,'hm2WwanCellularSignalStrengthLte':hm2WwanCellularSignalStrengthLte,'hm2WwanCellularSignalQuality':hm2WwanCellularSignalQuality,'hm2WwanCellularSignalQualityLte':hm2WwanCellularSignalQualityLte,_d:hm2WwanCellularRoamingStatus,'hm2WwanCellularBitErrorRate':hm2WwanCellularBitErrorRate,'hm2WwanCellularCurrentTxRate':hm2WwanCellularCurrentTxRate,'hm2WwanCellularCurrentRxRate':hm2WwanCellularCurrentRxRate,'hm2WwanCellularMaxTxRate':hm2WwanCellularMaxTxRate,'hm2WwanCellularMaxRxRate':hm2WwanCellularMaxRxRate,'hm2WwanCellularDataTech':hm2WwanCellularDataTech,'hm2WwanModemInformationGroup':hm2WwanModemInformationGroup,'hm2WwanModemManufacturer':hm2WwanModemManufacturer,'hm2WwanModemModel':hm2WwanModemModel,'hm2WwanModemRevision':hm2WwanModemRevision,'hm2WwanModemImei':hm2WwanModemImei,'hm2WwanModemOperationalState':hm2WwanModemOperationalState})