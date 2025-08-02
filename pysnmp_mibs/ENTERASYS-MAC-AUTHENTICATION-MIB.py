_w='etsysMACAuthenticationSystemGroup2'
_v='etsysMACAuthenticationSystemGroup'
_u='etsysMACAuthenticationMACListRowStatus'
_t='etsysMACAuthenticationMACListPorts'
_s='etsysMACAuthenticationMACListPasswordValid'
_r='etsysMACAuthenticationMACListPassword'
_q='etsysMACAuthenticationCurrentMACListEntries'
_p='etsysMACAuthenticationMaxMACListEntries'
_o='etsysMACAuthenticationSystemUserNameFormat'
_n='etsysMACAuthenticationDuration'
_m='etsysMACAuthenticationSessionPort'
_l='etsysMACAuthenticationMACReauthEnabled'
_k='etsysMACAuthenticationMACReauthPeriod'
_j='etsysMACAuthenticationMACReauthenticate'
_i='etsysMACAuthenticationMACInitialize'
_h='etsysMACAuthenticationSupplicantPort'
_g='etsysMACAuthenticationLastFailedAuthCause'
_f='etsysMACAuthenticationAuthenticationsAllocated'
_e='etsysMACAuthenticationAuthenticationsAllowed'
_d='etsysMACAuthenticationPortReauthEnabled'
_c='etsysMACAuthenticationPortReauthPeriod'
_b='etsysMACAuthenticationPortQuietPeriod'
_a='etsysMACAuthenticationPortEnable'
_Z='etsysMACAuthenticationPortReauthenticate'
_Y='etsysMACAuthenticationPortInitialize'
_X='etsysMACAuthenticationMACListMaskLen'
_W='etsysMACAuthenticationMACListAddress'
_V='etsysMACAuthenticationPort'
_U='PortList'
_T='etsysMACAuthenticationSystemGroup3'
_S='etsysMACAuthenticationSystemAccountEnable'
_R='etsysMACAuthenticationMode'
_Q='etsysMACAuthenticationMACAddress'
_P='SnmpAdminString'
_O='etsysMACAuthenticationPortUserNameSignificantBits'
_N='etsysMACAuthenticationMACUserPassword'
_M='etsysMACAuthenticationSystemEnable'
_L='not-accessible'
_K='Unsigned32'
_J='Integer32'
_I='etsysMACAuthenticationMACSessionGroup'
_H='etsysMACAuthenticationMACConfigGroup'
_G='etsysMACAuthenticationPortConfigGroup'
_F='EnabledStatus'
_E='deprecated'
_D='read-only'
_C='read-write'
_B='current'
_A='ENTERASYS-MAC-AUTHENTICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_U)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
etsysMACAuthenticationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,25))
if mibBuilder.loadTexts:etsysMACAuthenticationMIB.setRevisions(('2017-06-07 10:35','2014-12-19 10:51','2014-12-05 10:51','2014-12-03 12:00','2013-05-17 15:10','2013-01-31 13:34','2002-07-18 18:12'))
_EtsysMACAuthenticationObjects_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationObjects=_EtsysMACAuthenticationObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,1))
_EtsysMACAuthenticationSystem_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationSystem=_EtsysMACAuthenticationSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,1,1))
class _EtsysMACAuthenticationSystemEnable_Type(EnabledStatus):defaultValue=2
_EtsysMACAuthenticationSystemEnable_Type.__name__=_F
_EtsysMACAuthenticationSystemEnable_Object=MibScalar
etsysMACAuthenticationSystemEnable=_EtsysMACAuthenticationSystemEnable_Object((1,3,6,1,4,1,5624,1,2,25,1,1,1),_EtsysMACAuthenticationSystemEnable_Type())
etsysMACAuthenticationSystemEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationSystemEnable.setStatus(_B)
class _EtsysMACAuthenticationMACUserPassword_Type(SnmpAdminString):defaultValue=OctetString('NOPASSWORD')
_EtsysMACAuthenticationMACUserPassword_Type.__name__=_P
_EtsysMACAuthenticationMACUserPassword_Object=MibScalar
etsysMACAuthenticationMACUserPassword=_EtsysMACAuthenticationMACUserPassword_Object((1,3,6,1,4,1,5624,1,2,25,1,1,2),_EtsysMACAuthenticationMACUserPassword_Type())
etsysMACAuthenticationMACUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationMACUserPassword.setStatus(_E)
class _EtsysMACAuthenticationPortUserNameSignificantBits_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_EtsysMACAuthenticationPortUserNameSignificantBits_Type.__name__=_J
_EtsysMACAuthenticationPortUserNameSignificantBits_Object=MibScalar
etsysMACAuthenticationPortUserNameSignificantBits=_EtsysMACAuthenticationPortUserNameSignificantBits_Object((1,3,6,1,4,1,5624,1,2,25,1,1,3),_EtsysMACAuthenticationPortUserNameSignificantBits_Type())
etsysMACAuthenticationPortUserNameSignificantBits.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationPortUserNameSignificantBits.setStatus(_E)
class _EtsysMACAuthenticationMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('password',1),('radiusUsername',2),('macList',3)))
_EtsysMACAuthenticationMode_Type.__name__=_J
_EtsysMACAuthenticationMode_Object=MibScalar
etsysMACAuthenticationMode=_EtsysMACAuthenticationMode_Object((1,3,6,1,4,1,5624,1,2,25,1,1,4),_EtsysMACAuthenticationMode_Type())
etsysMACAuthenticationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationMode.setStatus(_B)
class _EtsysMACAuthenticationSystemAccountEnable_Type(EnabledStatus):defaultValue=1
_EtsysMACAuthenticationSystemAccountEnable_Type.__name__=_F
_EtsysMACAuthenticationSystemAccountEnable_Object=MibScalar
etsysMACAuthenticationSystemAccountEnable=_EtsysMACAuthenticationSystemAccountEnable_Object((1,3,6,1,4,1,5624,1,2,25,1,1,5),_EtsysMACAuthenticationSystemAccountEnable_Type())
etsysMACAuthenticationSystemAccountEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationSystemAccountEnable.setStatus(_B)
class _EtsysMACAuthenticationSystemUserNameFormat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hyphen',1),('none',2),('colon',3)))
_EtsysMACAuthenticationSystemUserNameFormat_Type.__name__=_J
_EtsysMACAuthenticationSystemUserNameFormat_Object=MibScalar
etsysMACAuthenticationSystemUserNameFormat=_EtsysMACAuthenticationSystemUserNameFormat_Object((1,3,6,1,4,1,5624,1,2,25,1,1,6),_EtsysMACAuthenticationSystemUserNameFormat_Type())
etsysMACAuthenticationSystemUserNameFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationSystemUserNameFormat.setStatus(_B)
_EtsysMACAuthenticationPortConfig_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationPortConfig=_EtsysMACAuthenticationPortConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,1,2))
_EtsysMACAuthenticationPortConfigTable_Object=MibTable
etsysMACAuthenticationPortConfigTable=_EtsysMACAuthenticationPortConfigTable_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1))
if mibBuilder.loadTexts:etsysMACAuthenticationPortConfigTable.setStatus(_B)
_EtsysMACAuthenticationPortConfigEntry_Object=MibTableRow
etsysMACAuthenticationPortConfigEntry=_EtsysMACAuthenticationPortConfigEntry_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1))
etsysMACAuthenticationPortConfigEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:etsysMACAuthenticationPortConfigEntry.setStatus(_B)
_EtsysMACAuthenticationPort_Type=InterfaceIndex
_EtsysMACAuthenticationPort_Object=MibTableColumn
etsysMACAuthenticationPort=_EtsysMACAuthenticationPort_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,1),_EtsysMACAuthenticationPort_Type())
etsysMACAuthenticationPort.setMaxAccess(_L)
if mibBuilder.loadTexts:etsysMACAuthenticationPort.setStatus(_B)
_EtsysMACAuthenticationPortInitialize_Type=TruthValue
_EtsysMACAuthenticationPortInitialize_Object=MibTableColumn
etsysMACAuthenticationPortInitialize=_EtsysMACAuthenticationPortInitialize_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,2),_EtsysMACAuthenticationPortInitialize_Type())
etsysMACAuthenticationPortInitialize.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationPortInitialize.setStatus(_B)
_EtsysMACAuthenticationPortReauthenticate_Type=TruthValue
_EtsysMACAuthenticationPortReauthenticate_Object=MibTableColumn
etsysMACAuthenticationPortReauthenticate=_EtsysMACAuthenticationPortReauthenticate_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,3),_EtsysMACAuthenticationPortReauthenticate_Type())
etsysMACAuthenticationPortReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationPortReauthenticate.setStatus(_B)
class _EtsysMACAuthenticationPortEnable_Type(EnabledStatus):defaultValue=2
_EtsysMACAuthenticationPortEnable_Type.__name__=_F
_EtsysMACAuthenticationPortEnable_Object=MibTableColumn
etsysMACAuthenticationPortEnable=_EtsysMACAuthenticationPortEnable_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,4),_EtsysMACAuthenticationPortEnable_Type())
etsysMACAuthenticationPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationPortEnable.setStatus(_B)
class _EtsysMACAuthenticationPortQuietPeriod_Type(Unsigned32):defaultValue=30
_EtsysMACAuthenticationPortQuietPeriod_Type.__name__=_K
_EtsysMACAuthenticationPortQuietPeriod_Object=MibTableColumn
etsysMACAuthenticationPortQuietPeriod=_EtsysMACAuthenticationPortQuietPeriod_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,5),_EtsysMACAuthenticationPortQuietPeriod_Type())
etsysMACAuthenticationPortQuietPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationPortQuietPeriod.setStatus(_B)
class _EtsysMACAuthenticationPortReauthPeriod_Type(Unsigned32):defaultValue=3600
_EtsysMACAuthenticationPortReauthPeriod_Type.__name__=_K
_EtsysMACAuthenticationPortReauthPeriod_Object=MibTableColumn
etsysMACAuthenticationPortReauthPeriod=_EtsysMACAuthenticationPortReauthPeriod_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,6),_EtsysMACAuthenticationPortReauthPeriod_Type())
etsysMACAuthenticationPortReauthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationPortReauthPeriod.setStatus(_B)
class _EtsysMACAuthenticationPortReauthEnabled_Type(EnabledStatus):defaultValue=2
_EtsysMACAuthenticationPortReauthEnabled_Type.__name__=_F
_EtsysMACAuthenticationPortReauthEnabled_Object=MibTableColumn
etsysMACAuthenticationPortReauthEnabled=_EtsysMACAuthenticationPortReauthEnabled_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,7),_EtsysMACAuthenticationPortReauthEnabled_Type())
etsysMACAuthenticationPortReauthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationPortReauthEnabled.setStatus(_B)
_EtsysMACAuthenticationAuthenticationsAllowed_Type=Unsigned32
_EtsysMACAuthenticationAuthenticationsAllowed_Object=MibTableColumn
etsysMACAuthenticationAuthenticationsAllowed=_EtsysMACAuthenticationAuthenticationsAllowed_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,8),_EtsysMACAuthenticationAuthenticationsAllowed_Type())
etsysMACAuthenticationAuthenticationsAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationAuthenticationsAllowed.setStatus(_B)
_EtsysMACAuthenticationAuthenticationsAllocated_Type=Unsigned32
_EtsysMACAuthenticationAuthenticationsAllocated_Object=MibTableColumn
etsysMACAuthenticationAuthenticationsAllocated=_EtsysMACAuthenticationAuthenticationsAllocated_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,9),_EtsysMACAuthenticationAuthenticationsAllocated_Type())
etsysMACAuthenticationAuthenticationsAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationAuthenticationsAllocated.setStatus(_B)
_EtsysMACAuthenticationLastFailedAuthCause_Type=SnmpAdminString
_EtsysMACAuthenticationLastFailedAuthCause_Object=MibTableColumn
etsysMACAuthenticationLastFailedAuthCause=_EtsysMACAuthenticationLastFailedAuthCause_Object((1,3,6,1,4,1,5624,1,2,25,1,2,1,1,10),_EtsysMACAuthenticationLastFailedAuthCause_Type())
etsysMACAuthenticationLastFailedAuthCause.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationLastFailedAuthCause.setStatus(_B)
_EtsysMACAuthenticationMACConfig_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationMACConfig=_EtsysMACAuthenticationMACConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,1,3))
_EtsysMACAuthenticationMACConfigTable_Object=MibTable
etsysMACAuthenticationMACConfigTable=_EtsysMACAuthenticationMACConfigTable_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1))
if mibBuilder.loadTexts:etsysMACAuthenticationMACConfigTable.setStatus(_B)
_EtsysMACAuthenticationMACConfigEntry_Object=MibTableRow
etsysMACAuthenticationMACConfigEntry=_EtsysMACAuthenticationMACConfigEntry_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1,1))
etsysMACAuthenticationMACConfigEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:etsysMACAuthenticationMACConfigEntry.setStatus(_B)
_EtsysMACAuthenticationMACAddress_Type=MacAddress
_EtsysMACAuthenticationMACAddress_Object=MibTableColumn
etsysMACAuthenticationMACAddress=_EtsysMACAuthenticationMACAddress_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1,1,1),_EtsysMACAuthenticationMACAddress_Type())
etsysMACAuthenticationMACAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:etsysMACAuthenticationMACAddress.setStatus(_B)
_EtsysMACAuthenticationSupplicantPort_Type=InterfaceIndex
_EtsysMACAuthenticationSupplicantPort_Object=MibTableColumn
etsysMACAuthenticationSupplicantPort=_EtsysMACAuthenticationSupplicantPort_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1,1,2),_EtsysMACAuthenticationSupplicantPort_Type())
etsysMACAuthenticationSupplicantPort.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationSupplicantPort.setStatus(_B)
_EtsysMACAuthenticationMACInitialize_Type=TruthValue
_EtsysMACAuthenticationMACInitialize_Object=MibTableColumn
etsysMACAuthenticationMACInitialize=_EtsysMACAuthenticationMACInitialize_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1,1,3),_EtsysMACAuthenticationMACInitialize_Type())
etsysMACAuthenticationMACInitialize.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationMACInitialize.setStatus(_B)
_EtsysMACAuthenticationMACReauthenticate_Type=TruthValue
_EtsysMACAuthenticationMACReauthenticate_Object=MibTableColumn
etsysMACAuthenticationMACReauthenticate=_EtsysMACAuthenticationMACReauthenticate_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1,1,4),_EtsysMACAuthenticationMACReauthenticate_Type())
etsysMACAuthenticationMACReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationMACReauthenticate.setStatus(_B)
_EtsysMACAuthenticationMACReauthPeriod_Type=Unsigned32
_EtsysMACAuthenticationMACReauthPeriod_Object=MibTableColumn
etsysMACAuthenticationMACReauthPeriod=_EtsysMACAuthenticationMACReauthPeriod_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1,1,5),_EtsysMACAuthenticationMACReauthPeriod_Type())
etsysMACAuthenticationMACReauthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationMACReauthPeriod.setStatus(_B)
_EtsysMACAuthenticationMACReauthEnabled_Type=EnabledStatus
_EtsysMACAuthenticationMACReauthEnabled_Object=MibTableColumn
etsysMACAuthenticationMACReauthEnabled=_EtsysMACAuthenticationMACReauthEnabled_Object((1,3,6,1,4,1,5624,1,2,25,1,3,1,1,6),_EtsysMACAuthenticationMACReauthEnabled_Type())
etsysMACAuthenticationMACReauthEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationMACReauthEnabled.setStatus(_B)
_EtsysMACAuthenticationMACSession_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationMACSession=_EtsysMACAuthenticationMACSession_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,1,4))
_EtsysMACAuthenticationSessionTable_Object=MibTable
etsysMACAuthenticationSessionTable=_EtsysMACAuthenticationSessionTable_Object((1,3,6,1,4,1,5624,1,2,25,1,4,1))
if mibBuilder.loadTexts:etsysMACAuthenticationSessionTable.setStatus(_B)
_EtsysMACAuthenticationSessionEntry_Object=MibTableRow
etsysMACAuthenticationSessionEntry=_EtsysMACAuthenticationSessionEntry_Object((1,3,6,1,4,1,5624,1,2,25,1,4,1,1))
etsysMACAuthenticationSessionEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:etsysMACAuthenticationSessionEntry.setStatus(_B)
_EtsysMACAuthenticationSessionPort_Type=InterfaceIndex
_EtsysMACAuthenticationSessionPort_Object=MibTableColumn
etsysMACAuthenticationSessionPort=_EtsysMACAuthenticationSessionPort_Object((1,3,6,1,4,1,5624,1,2,25,1,4,1,1,1),_EtsysMACAuthenticationSessionPort_Type())
etsysMACAuthenticationSessionPort.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationSessionPort.setStatus(_B)
_EtsysMACAuthenticationDuration_Type=Unsigned32
_EtsysMACAuthenticationDuration_Object=MibTableColumn
etsysMACAuthenticationDuration=_EtsysMACAuthenticationDuration_Object((1,3,6,1,4,1,5624,1,2,25,1,4,1,1,2),_EtsysMACAuthenticationDuration_Type())
etsysMACAuthenticationDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationDuration.setStatus(_B)
_EtsysMACAuthenticationMACListConfig_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationMACListConfig=_EtsysMACAuthenticationMACListConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,1,5))
_EtsysMACAuthenticationMaxMACListEntries_Type=Unsigned32
_EtsysMACAuthenticationMaxMACListEntries_Object=MibScalar
etsysMACAuthenticationMaxMACListEntries=_EtsysMACAuthenticationMaxMACListEntries_Object((1,3,6,1,4,1,5624,1,2,25,1,5,1),_EtsysMACAuthenticationMaxMACListEntries_Type())
etsysMACAuthenticationMaxMACListEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationMaxMACListEntries.setStatus(_B)
_EtsysMACAuthenticationCurrentMACListEntries_Type=Unsigned32
_EtsysMACAuthenticationCurrentMACListEntries_Object=MibScalar
etsysMACAuthenticationCurrentMACListEntries=_EtsysMACAuthenticationCurrentMACListEntries_Object((1,3,6,1,4,1,5624,1,2,25,1,5,2),_EtsysMACAuthenticationCurrentMACListEntries_Type())
etsysMACAuthenticationCurrentMACListEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationCurrentMACListEntries.setStatus(_B)
_EtsysMACAuthenticationMACListTable_Object=MibTable
etsysMACAuthenticationMACListTable=_EtsysMACAuthenticationMACListTable_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3))
if mibBuilder.loadTexts:etsysMACAuthenticationMACListTable.setStatus(_B)
_EtsysMACAuthenticationMACListEntry_Object=MibTableRow
etsysMACAuthenticationMACListEntry=_EtsysMACAuthenticationMACListEntry_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3,1))
etsysMACAuthenticationMACListEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:etsysMACAuthenticationMACListEntry.setStatus(_B)
_EtsysMACAuthenticationMACListAddress_Type=MacAddress
_EtsysMACAuthenticationMACListAddress_Object=MibTableColumn
etsysMACAuthenticationMACListAddress=_EtsysMACAuthenticationMACListAddress_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3,1,1),_EtsysMACAuthenticationMACListAddress_Type())
etsysMACAuthenticationMACListAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:etsysMACAuthenticationMACListAddress.setStatus(_B)
class _EtsysMACAuthenticationMACListMaskLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_EtsysMACAuthenticationMACListMaskLen_Type.__name__=_K
_EtsysMACAuthenticationMACListMaskLen_Object=MibTableColumn
etsysMACAuthenticationMACListMaskLen=_EtsysMACAuthenticationMACListMaskLen_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3,1,2),_EtsysMACAuthenticationMACListMaskLen_Type())
etsysMACAuthenticationMACListMaskLen.setMaxAccess(_L)
if mibBuilder.loadTexts:etsysMACAuthenticationMACListMaskLen.setStatus(_B)
class _EtsysMACAuthenticationMACListPassword_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_EtsysMACAuthenticationMACListPassword_Type.__name__=_P
_EtsysMACAuthenticationMACListPassword_Object=MibTableColumn
etsysMACAuthenticationMACListPassword=_EtsysMACAuthenticationMACListPassword_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3,1,3),_EtsysMACAuthenticationMACListPassword_Type())
etsysMACAuthenticationMACListPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationMACListPassword.setStatus(_B)
_EtsysMACAuthenticationMACListPasswordValid_Type=TruthValue
_EtsysMACAuthenticationMACListPasswordValid_Object=MibTableColumn
etsysMACAuthenticationMACListPasswordValid=_EtsysMACAuthenticationMACListPasswordValid_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3,1,4),_EtsysMACAuthenticationMACListPasswordValid_Type())
etsysMACAuthenticationMACListPasswordValid.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMACAuthenticationMACListPasswordValid.setStatus(_B)
class _EtsysMACAuthenticationMACListPorts_Type(PortList):defaultHexValue=''
_EtsysMACAuthenticationMACListPorts_Type.__name__=_U
_EtsysMACAuthenticationMACListPorts_Object=MibTableColumn
etsysMACAuthenticationMACListPorts=_EtsysMACAuthenticationMACListPorts_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3,1,5),_EtsysMACAuthenticationMACListPorts_Type())
etsysMACAuthenticationMACListPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationMACListPorts.setStatus(_B)
_EtsysMACAuthenticationMACListRowStatus_Type=RowStatus
_EtsysMACAuthenticationMACListRowStatus_Object=MibTableColumn
etsysMACAuthenticationMACListRowStatus=_EtsysMACAuthenticationMACListRowStatus_Object((1,3,6,1,4,1,5624,1,2,25,1,5,3,1,6),_EtsysMACAuthenticationMACListRowStatus_Type())
etsysMACAuthenticationMACListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMACAuthenticationMACListRowStatus.setStatus(_B)
_EtsysMACAuthenticationConformance_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationConformance=_EtsysMACAuthenticationConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,2))
_EtsysMACAuthenticationGroups_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationGroups=_EtsysMACAuthenticationGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,2,1))
_EtsysMACAuthenticationCompliances_ObjectIdentity=ObjectIdentity
etsysMACAuthenticationCompliances=_EtsysMACAuthenticationCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,25,2,2))
etsysMACAuthenticationSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,25,2,1,1))
etsysMACAuthenticationSystemGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:etsysMACAuthenticationSystemGroup.setStatus(_E)
etsysMACAuthenticationPortConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,25,2,1,2))
etsysMACAuthenticationPortConfigGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:etsysMACAuthenticationPortConfigGroup.setStatus(_B)
etsysMACAuthenticationMACConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,25,2,1,3))
etsysMACAuthenticationMACConfigGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:etsysMACAuthenticationMACConfigGroup.setStatus(_B)
etsysMACAuthenticationMACSessionGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,25,2,1,4))
etsysMACAuthenticationMACSessionGroup.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:etsysMACAuthenticationMACSessionGroup.setStatus(_B)
etsysMACAuthenticationSystemGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,25,2,1,5))
etsysMACAuthenticationSystemGroup2.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:etsysMACAuthenticationSystemGroup2.setStatus(_E)
etsysMACAuthenticationSystemGroup3=ObjectGroup((1,3,6,1,4,1,5624,1,2,25,2,1,6))
etsysMACAuthenticationSystemGroup3.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_R),(_A,_S),(_A,_o)))
if mibBuilder.loadTexts:etsysMACAuthenticationSystemGroup3.setStatus(_B)
etsysMACAuthenticationMACListGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,25,2,1,7))
etsysMACAuthenticationMACListGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:etsysMACAuthenticationMACListGroup.setStatus(_B)
etsysMACAuthenticationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,25,2,2,1))
etsysMACAuthenticationCompliance.setObjects(*((_A,_v),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:etsysMACAuthenticationCompliance.setStatus(_E)
etsysMACAuthenticationCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,25,2,2,2))
etsysMACAuthenticationCompliance2.setObjects(*((_A,_w),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:etsysMACAuthenticationCompliance2.setStatus(_E)
etsysMACAuthenticationCompliance3=ModuleCompliance((1,3,6,1,4,1,5624,1,2,25,2,2,3))
etsysMACAuthenticationCompliance3.setObjects(*((_A,_T),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:etsysMACAuthenticationCompliance3.setStatus(_E)
etsysMACAuthenticationCompliance4=ModuleCompliance((1,3,6,1,4,1,5624,1,2,25,2,2,4))
etsysMACAuthenticationCompliance4.setObjects(*((_A,_T),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:etsysMACAuthenticationCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysMACAuthenticationMIB':etsysMACAuthenticationMIB,'etsysMACAuthenticationObjects':etsysMACAuthenticationObjects,'etsysMACAuthenticationSystem':etsysMACAuthenticationSystem,_M:etsysMACAuthenticationSystemEnable,_N:etsysMACAuthenticationMACUserPassword,_O:etsysMACAuthenticationPortUserNameSignificantBits,_R:etsysMACAuthenticationMode,_S:etsysMACAuthenticationSystemAccountEnable,_o:etsysMACAuthenticationSystemUserNameFormat,'etsysMACAuthenticationPortConfig':etsysMACAuthenticationPortConfig,'etsysMACAuthenticationPortConfigTable':etsysMACAuthenticationPortConfigTable,'etsysMACAuthenticationPortConfigEntry':etsysMACAuthenticationPortConfigEntry,_V:etsysMACAuthenticationPort,_Y:etsysMACAuthenticationPortInitialize,_Z:etsysMACAuthenticationPortReauthenticate,_a:etsysMACAuthenticationPortEnable,_b:etsysMACAuthenticationPortQuietPeriod,_c:etsysMACAuthenticationPortReauthPeriod,_d:etsysMACAuthenticationPortReauthEnabled,_e:etsysMACAuthenticationAuthenticationsAllowed,_f:etsysMACAuthenticationAuthenticationsAllocated,_g:etsysMACAuthenticationLastFailedAuthCause,'etsysMACAuthenticationMACConfig':etsysMACAuthenticationMACConfig,'etsysMACAuthenticationMACConfigTable':etsysMACAuthenticationMACConfigTable,'etsysMACAuthenticationMACConfigEntry':etsysMACAuthenticationMACConfigEntry,_Q:etsysMACAuthenticationMACAddress,_h:etsysMACAuthenticationSupplicantPort,_i:etsysMACAuthenticationMACInitialize,_j:etsysMACAuthenticationMACReauthenticate,_k:etsysMACAuthenticationMACReauthPeriod,_l:etsysMACAuthenticationMACReauthEnabled,'etsysMACAuthenticationMACSession':etsysMACAuthenticationMACSession,'etsysMACAuthenticationSessionTable':etsysMACAuthenticationSessionTable,'etsysMACAuthenticationSessionEntry':etsysMACAuthenticationSessionEntry,_m:etsysMACAuthenticationSessionPort,_n:etsysMACAuthenticationDuration,'etsysMACAuthenticationMACListConfig':etsysMACAuthenticationMACListConfig,_p:etsysMACAuthenticationMaxMACListEntries,_q:etsysMACAuthenticationCurrentMACListEntries,'etsysMACAuthenticationMACListTable':etsysMACAuthenticationMACListTable,'etsysMACAuthenticationMACListEntry':etsysMACAuthenticationMACListEntry,_W:etsysMACAuthenticationMACListAddress,_X:etsysMACAuthenticationMACListMaskLen,_r:etsysMACAuthenticationMACListPassword,_s:etsysMACAuthenticationMACListPasswordValid,_t:etsysMACAuthenticationMACListPorts,_u:etsysMACAuthenticationMACListRowStatus,'etsysMACAuthenticationConformance':etsysMACAuthenticationConformance,'etsysMACAuthenticationGroups':etsysMACAuthenticationGroups,_v:etsysMACAuthenticationSystemGroup,_G:etsysMACAuthenticationPortConfigGroup,_H:etsysMACAuthenticationMACConfigGroup,_I:etsysMACAuthenticationMACSessionGroup,_w:etsysMACAuthenticationSystemGroup2,_T:etsysMACAuthenticationSystemGroup3,'etsysMACAuthenticationMACListGroup':etsysMACAuthenticationMACListGroup,'etsysMACAuthenticationCompliances':etsysMACAuthenticationCompliances,'etsysMACAuthenticationCompliance':etsysMACAuthenticationCompliance,'etsysMACAuthenticationCompliance2':etsysMACAuthenticationCompliance2,'etsysMACAuthenticationCompliance3':etsysMACAuthenticationCompliance3,'etsysMACAuthenticationCompliance4':etsysMACAuthenticationCompliance4})