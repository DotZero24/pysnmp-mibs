_z='gvrpNotificationGroup'
_y='gvrpPortStatsGroup'
_x='gvrpPortConfigGroup'
_w='gvrpPortBaseGroup'
_v='gvrpVlanLimitReachedEvent'
_u='alaGvrpPortStatsClearStats'
_t='alaGvrpPortStatsInvalidMsgsReceived'
_s='alaGvrpPortStatsTotalMsgsTransmitted'
_r='alaGvrpPortStatsTotalMsgsReceived'
_q='alaGvrpPortStatsTotalPDUTransmitted'
_p='alaGvrpPortStatsTotalPDUReceived'
_o='alaGvrpPortStatsLeaveAllTransmitted'
_n='alaGvrpPortStatsLeaveEmptyTransmitted'
_m='alaGvrpPortStatsLeaveInTransmitted'
_l='alaGvrpPortStatsEmptyTransmitted'
_k='alaGvrpPortStatsJoinInTransmitted'
_j='alaGvrpPortStatsJoinEmptyTransmitted'
_i='alaGvrpPortStatsLeaveAllReceived'
_h='alaGvrpPortStatsLeaveEmptyReceived'
_g='alaGvrpPortStatsLeaveInReceived'
_f='alaGvrpPortStatsEmptyReceived'
_e='alaGvrpPortStatsJoinInReceived'
_d='alaGvrpPortStatsJoinEmptyReceived'
_c='alaGvrpPortConfigProviderBpduMac'
_b='alaGvrpPortConfigLeaveAllTimer'
_a='alaGvrpPortConfigLeaveTimer'
_Z='alaGvrpPortConfigJoinTimer'
_Y='alaGvrpPortConfigRegistrationToStaticVlan'
_X='alaGvrpPortConfigRegistrationToStaticVlanRestrict'
_W='alaGvrpPortConfigRegistrationToStaticVlanLearn'
_V='alaGvrpPortConfigApplicantBitmap'
_U='alaGvrpPortConfigAllowApplicantBitmap'
_T='alaGvrpPortConfigRestrictedApplicantBitmap'
_S='alaGvrpPortConfigRegistrationBitmap'
_R='alaGvrpPortConfigAllowRegistrationBitmap'
_Q='alaGvrpPortConfigRestrictedRegistrationBitmap'
_P='alaGvrpPortConfigApplicantMode'
_O='alaGvrpPortConfigRegistrarMode'
_N='alaGvrpTransparentSwitching'
_M='alaGvrpGlobalClearStats'
_L='alaGvrpPortStatsIfIndex'
_K='not-accessible'
_J='alaGvrpPortConfigIfIndex'
_I='default'
_H='alaGvrpMaxVlanLimit'
_G='milliseconds'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='ALCATEL-ENT1-GVRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Gvrp,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Gvrp')
VlanBitmap,=mibBuilder.importSymbols('ALCATEL-ENT1-VLAN-STP-MIB','VlanBitmap')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1GVRPMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1))
if mibBuilder.loadTexts:alcatelIND1GVRPMIB.setRevisions(('2010-05-13 00:00','2007-07-02 00:00'))
_AlcatelIND1GVRPMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1GVRPMIBNotifications=_AlcatelIND1GVRPMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1,0))
if mibBuilder.loadTexts:alcatelIND1GVRPMIBNotifications.setStatus(_A)
_AlcatelIND1GVRPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1GVRPMIBObjects=_AlcatelIND1GVRPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1,1))
if mibBuilder.loadTexts:alcatelIND1GVRPMIBObjects.setStatus(_A)
class _AlaGvrpGlobalClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('reset',1)))
_AlaGvrpGlobalClearStats_Type.__name__=_E
_AlaGvrpGlobalClearStats_Object=MibScalar
alaGvrpGlobalClearStats=_AlaGvrpGlobalClearStats_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,1),_AlaGvrpGlobalClearStats_Type())
alaGvrpGlobalClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpGlobalClearStats.setStatus(_A)
class _AlaGvrpTransparentSwitching_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaGvrpTransparentSwitching_Type.__name__=_E
_AlaGvrpTransparentSwitching_Object=MibScalar
alaGvrpTransparentSwitching=_AlaGvrpTransparentSwitching_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,2),_AlaGvrpTransparentSwitching_Type())
alaGvrpTransparentSwitching.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpTransparentSwitching.setStatus(_A)
class _AlaGvrpMaxVlanLimit_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4094))
_AlaGvrpMaxVlanLimit_Type.__name__=_E
_AlaGvrpMaxVlanLimit_Object=MibScalar
alaGvrpMaxVlanLimit=_AlaGvrpMaxVlanLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,3),_AlaGvrpMaxVlanLimit_Type())
alaGvrpMaxVlanLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpMaxVlanLimit.setStatus(_A)
_GvrpPortConfig_ObjectIdentity=ObjectIdentity
gvrpPortConfig=_GvrpPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4))
_AlaGvrpPortConfigTable_Object=MibTable
alaGvrpPortConfigTable=_AlaGvrpPortConfigTable_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1))
if mibBuilder.loadTexts:alaGvrpPortConfigTable.setStatus(_A)
_AlaGvrpPortConfigEntry_Object=MibTableRow
alaGvrpPortConfigEntry=_AlaGvrpPortConfigEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1))
alaGvrpPortConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:alaGvrpPortConfigEntry.setStatus(_A)
_AlaGvrpPortConfigIfIndex_Type=InterfaceIndex
_AlaGvrpPortConfigIfIndex_Object=MibTableColumn
alaGvrpPortConfigIfIndex=_AlaGvrpPortConfigIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,1),_AlaGvrpPortConfigIfIndex_Type())
alaGvrpPortConfigIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:alaGvrpPortConfigIfIndex.setStatus(_A)
class _AlaGvrpPortConfigRegistrarMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fixed',2),('forbidden',3)))
_AlaGvrpPortConfigRegistrarMode_Type.__name__=_E
_AlaGvrpPortConfigRegistrarMode_Object=MibTableColumn
alaGvrpPortConfigRegistrarMode=_AlaGvrpPortConfigRegistrarMode_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,2),_AlaGvrpPortConfigRegistrarMode_Type())
alaGvrpPortConfigRegistrarMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigRegistrarMode.setStatus(_A)
class _AlaGvrpPortConfigApplicantMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('participant',1),('nonparticipant',2),('active',3)))
_AlaGvrpPortConfigApplicantMode_Type.__name__=_E
_AlaGvrpPortConfigApplicantMode_Object=MibTableColumn
alaGvrpPortConfigApplicantMode=_AlaGvrpPortConfigApplicantMode_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,3),_AlaGvrpPortConfigApplicantMode_Type())
alaGvrpPortConfigApplicantMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigApplicantMode.setStatus(_A)
_AlaGvrpPortConfigRestrictedRegistrationBitmap_Type=VlanBitmap
_AlaGvrpPortConfigRestrictedRegistrationBitmap_Object=MibTableColumn
alaGvrpPortConfigRestrictedRegistrationBitmap=_AlaGvrpPortConfigRestrictedRegistrationBitmap_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,4),_AlaGvrpPortConfigRestrictedRegistrationBitmap_Type())
alaGvrpPortConfigRestrictedRegistrationBitmap.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigRestrictedRegistrationBitmap.setStatus(_A)
_AlaGvrpPortConfigAllowRegistrationBitmap_Type=VlanBitmap
_AlaGvrpPortConfigAllowRegistrationBitmap_Object=MibTableColumn
alaGvrpPortConfigAllowRegistrationBitmap=_AlaGvrpPortConfigAllowRegistrationBitmap_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,5),_AlaGvrpPortConfigAllowRegistrationBitmap_Type())
alaGvrpPortConfigAllowRegistrationBitmap.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigAllowRegistrationBitmap.setStatus(_A)
_AlaGvrpPortConfigRegistrationBitmap_Type=VlanBitmap
_AlaGvrpPortConfigRegistrationBitmap_Object=MibTableColumn
alaGvrpPortConfigRegistrationBitmap=_AlaGvrpPortConfigRegistrationBitmap_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,6),_AlaGvrpPortConfigRegistrationBitmap_Type())
alaGvrpPortConfigRegistrationBitmap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortConfigRegistrationBitmap.setStatus(_A)
_AlaGvrpPortConfigRestrictedApplicantBitmap_Type=VlanBitmap
_AlaGvrpPortConfigRestrictedApplicantBitmap_Object=MibTableColumn
alaGvrpPortConfigRestrictedApplicantBitmap=_AlaGvrpPortConfigRestrictedApplicantBitmap_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,7),_AlaGvrpPortConfigRestrictedApplicantBitmap_Type())
alaGvrpPortConfigRestrictedApplicantBitmap.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigRestrictedApplicantBitmap.setStatus(_A)
_AlaGvrpPortConfigAllowApplicantBitmap_Type=VlanBitmap
_AlaGvrpPortConfigAllowApplicantBitmap_Object=MibTableColumn
alaGvrpPortConfigAllowApplicantBitmap=_AlaGvrpPortConfigAllowApplicantBitmap_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,8),_AlaGvrpPortConfigAllowApplicantBitmap_Type())
alaGvrpPortConfigAllowApplicantBitmap.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigAllowApplicantBitmap.setStatus(_A)
_AlaGvrpPortConfigApplicantBitmap_Type=VlanBitmap
_AlaGvrpPortConfigApplicantBitmap_Object=MibTableColumn
alaGvrpPortConfigApplicantBitmap=_AlaGvrpPortConfigApplicantBitmap_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,9),_AlaGvrpPortConfigApplicantBitmap_Type())
alaGvrpPortConfigApplicantBitmap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortConfigApplicantBitmap.setStatus(_A)
_AlaGvrpPortConfigRegistrationToStaticVlanLearn_Type=VlanBitmap
_AlaGvrpPortConfigRegistrationToStaticVlanLearn_Object=MibTableColumn
alaGvrpPortConfigRegistrationToStaticVlanLearn=_AlaGvrpPortConfigRegistrationToStaticVlanLearn_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,10),_AlaGvrpPortConfigRegistrationToStaticVlanLearn_Type())
alaGvrpPortConfigRegistrationToStaticVlanLearn.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigRegistrationToStaticVlanLearn.setStatus(_A)
_AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Type=VlanBitmap
_AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Object=MibTableColumn
alaGvrpPortConfigRegistrationToStaticVlanRestrict=_AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,11),_AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Type())
alaGvrpPortConfigRegistrationToStaticVlanRestrict.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigRegistrationToStaticVlanRestrict.setStatus(_A)
_AlaGvrpPortConfigRegistrationToStaticVlan_Type=VlanBitmap
_AlaGvrpPortConfigRegistrationToStaticVlan_Object=MibTableColumn
alaGvrpPortConfigRegistrationToStaticVlan=_AlaGvrpPortConfigRegistrationToStaticVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,12),_AlaGvrpPortConfigRegistrationToStaticVlan_Type())
alaGvrpPortConfigRegistrationToStaticVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortConfigRegistrationToStaticVlan.setStatus(_A)
class _AlaGvrpPortConfigJoinTimer_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaGvrpPortConfigJoinTimer_Type.__name__=_F
_AlaGvrpPortConfigJoinTimer_Object=MibTableColumn
alaGvrpPortConfigJoinTimer=_AlaGvrpPortConfigJoinTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,13),_AlaGvrpPortConfigJoinTimer_Type())
alaGvrpPortConfigJoinTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigJoinTimer.setStatus(_A)
if mibBuilder.loadTexts:alaGvrpPortConfigJoinTimer.setUnits(_G)
class _AlaGvrpPortConfigLeaveTimer_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,2147483647))
_AlaGvrpPortConfigLeaveTimer_Type.__name__=_F
_AlaGvrpPortConfigLeaveTimer_Object=MibTableColumn
alaGvrpPortConfigLeaveTimer=_AlaGvrpPortConfigLeaveTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,14),_AlaGvrpPortConfigLeaveTimer_Type())
alaGvrpPortConfigLeaveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigLeaveTimer.setStatus(_A)
if mibBuilder.loadTexts:alaGvrpPortConfigLeaveTimer.setUnits(_G)
class _AlaGvrpPortConfigLeaveAllTimer_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,2147483647))
_AlaGvrpPortConfigLeaveAllTimer_Type.__name__=_F
_AlaGvrpPortConfigLeaveAllTimer_Object=MibTableColumn
alaGvrpPortConfigLeaveAllTimer=_AlaGvrpPortConfigLeaveAllTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,15),_AlaGvrpPortConfigLeaveAllTimer_Type())
alaGvrpPortConfigLeaveAllTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigLeaveAllTimer.setStatus(_A)
if mibBuilder.loadTexts:alaGvrpPortConfigLeaveAllTimer.setUnits(_G)
class _AlaGvrpPortConfigProviderBpduMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaGvrpPortConfigProviderBpduMac_Type.__name__=_E
_AlaGvrpPortConfigProviderBpduMac_Object=MibTableColumn
alaGvrpPortConfigProviderBpduMac=_AlaGvrpPortConfigProviderBpduMac_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,4,1,1,16),_AlaGvrpPortConfigProviderBpduMac_Type())
alaGvrpPortConfigProviderBpduMac.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortConfigProviderBpduMac.setStatus(_A)
_GvrpPortStats_ObjectIdentity=ObjectIdentity
gvrpPortStats=_GvrpPortStats_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5))
_AlaGvrpPortStatsTable_Object=MibTable
alaGvrpPortStatsTable=_AlaGvrpPortStatsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1))
if mibBuilder.loadTexts:alaGvrpPortStatsTable.setStatus(_A)
_AlaGvrpPortStatsEntry_Object=MibTableRow
alaGvrpPortStatsEntry=_AlaGvrpPortStatsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1))
alaGvrpPortStatsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:alaGvrpPortStatsEntry.setStatus(_A)
_AlaGvrpPortStatsIfIndex_Type=InterfaceIndex
_AlaGvrpPortStatsIfIndex_Object=MibTableColumn
alaGvrpPortStatsIfIndex=_AlaGvrpPortStatsIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,1),_AlaGvrpPortStatsIfIndex_Type())
alaGvrpPortStatsIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:alaGvrpPortStatsIfIndex.setStatus(_A)
_AlaGvrpPortStatsJoinEmptyReceived_Type=Counter32
_AlaGvrpPortStatsJoinEmptyReceived_Object=MibTableColumn
alaGvrpPortStatsJoinEmptyReceived=_AlaGvrpPortStatsJoinEmptyReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,2),_AlaGvrpPortStatsJoinEmptyReceived_Type())
alaGvrpPortStatsJoinEmptyReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsJoinEmptyReceived.setStatus(_A)
_AlaGvrpPortStatsJoinInReceived_Type=Counter32
_AlaGvrpPortStatsJoinInReceived_Object=MibTableColumn
alaGvrpPortStatsJoinInReceived=_AlaGvrpPortStatsJoinInReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,3),_AlaGvrpPortStatsJoinInReceived_Type())
alaGvrpPortStatsJoinInReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsJoinInReceived.setStatus(_A)
_AlaGvrpPortStatsEmptyReceived_Type=Counter32
_AlaGvrpPortStatsEmptyReceived_Object=MibTableColumn
alaGvrpPortStatsEmptyReceived=_AlaGvrpPortStatsEmptyReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,4),_AlaGvrpPortStatsEmptyReceived_Type())
alaGvrpPortStatsEmptyReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsEmptyReceived.setStatus(_A)
_AlaGvrpPortStatsLeaveInReceived_Type=Counter32
_AlaGvrpPortStatsLeaveInReceived_Object=MibTableColumn
alaGvrpPortStatsLeaveInReceived=_AlaGvrpPortStatsLeaveInReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,5),_AlaGvrpPortStatsLeaveInReceived_Type())
alaGvrpPortStatsLeaveInReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsLeaveInReceived.setStatus(_A)
_AlaGvrpPortStatsLeaveEmptyReceived_Type=Counter32
_AlaGvrpPortStatsLeaveEmptyReceived_Object=MibTableColumn
alaGvrpPortStatsLeaveEmptyReceived=_AlaGvrpPortStatsLeaveEmptyReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,6),_AlaGvrpPortStatsLeaveEmptyReceived_Type())
alaGvrpPortStatsLeaveEmptyReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsLeaveEmptyReceived.setStatus(_A)
_AlaGvrpPortStatsLeaveAllReceived_Type=Counter32
_AlaGvrpPortStatsLeaveAllReceived_Object=MibTableColumn
alaGvrpPortStatsLeaveAllReceived=_AlaGvrpPortStatsLeaveAllReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,7),_AlaGvrpPortStatsLeaveAllReceived_Type())
alaGvrpPortStatsLeaveAllReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsLeaveAllReceived.setStatus(_A)
_AlaGvrpPortStatsJoinEmptyTransmitted_Type=Counter32
_AlaGvrpPortStatsJoinEmptyTransmitted_Object=MibTableColumn
alaGvrpPortStatsJoinEmptyTransmitted=_AlaGvrpPortStatsJoinEmptyTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,8),_AlaGvrpPortStatsJoinEmptyTransmitted_Type())
alaGvrpPortStatsJoinEmptyTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsJoinEmptyTransmitted.setStatus(_A)
_AlaGvrpPortStatsJoinInTransmitted_Type=Counter32
_AlaGvrpPortStatsJoinInTransmitted_Object=MibTableColumn
alaGvrpPortStatsJoinInTransmitted=_AlaGvrpPortStatsJoinInTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,9),_AlaGvrpPortStatsJoinInTransmitted_Type())
alaGvrpPortStatsJoinInTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsJoinInTransmitted.setStatus(_A)
_AlaGvrpPortStatsEmptyTransmitted_Type=Counter32
_AlaGvrpPortStatsEmptyTransmitted_Object=MibTableColumn
alaGvrpPortStatsEmptyTransmitted=_AlaGvrpPortStatsEmptyTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,10),_AlaGvrpPortStatsEmptyTransmitted_Type())
alaGvrpPortStatsEmptyTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsEmptyTransmitted.setStatus(_A)
_AlaGvrpPortStatsLeaveInTransmitted_Type=Counter32
_AlaGvrpPortStatsLeaveInTransmitted_Object=MibTableColumn
alaGvrpPortStatsLeaveInTransmitted=_AlaGvrpPortStatsLeaveInTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,11),_AlaGvrpPortStatsLeaveInTransmitted_Type())
alaGvrpPortStatsLeaveInTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsLeaveInTransmitted.setStatus(_A)
_AlaGvrpPortStatsLeaveEmptyTransmitted_Type=Counter32
_AlaGvrpPortStatsLeaveEmptyTransmitted_Object=MibTableColumn
alaGvrpPortStatsLeaveEmptyTransmitted=_AlaGvrpPortStatsLeaveEmptyTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,12),_AlaGvrpPortStatsLeaveEmptyTransmitted_Type())
alaGvrpPortStatsLeaveEmptyTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsLeaveEmptyTransmitted.setStatus(_A)
_AlaGvrpPortStatsLeaveAllTransmitted_Type=Counter32
_AlaGvrpPortStatsLeaveAllTransmitted_Object=MibTableColumn
alaGvrpPortStatsLeaveAllTransmitted=_AlaGvrpPortStatsLeaveAllTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,13),_AlaGvrpPortStatsLeaveAllTransmitted_Type())
alaGvrpPortStatsLeaveAllTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsLeaveAllTransmitted.setStatus(_A)
_AlaGvrpPortStatsTotalPDUReceived_Type=Counter32
_AlaGvrpPortStatsTotalPDUReceived_Object=MibTableColumn
alaGvrpPortStatsTotalPDUReceived=_AlaGvrpPortStatsTotalPDUReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,14),_AlaGvrpPortStatsTotalPDUReceived_Type())
alaGvrpPortStatsTotalPDUReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsTotalPDUReceived.setStatus(_A)
_AlaGvrpPortStatsTotalPDUTransmitted_Type=Counter32
_AlaGvrpPortStatsTotalPDUTransmitted_Object=MibTableColumn
alaGvrpPortStatsTotalPDUTransmitted=_AlaGvrpPortStatsTotalPDUTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,15),_AlaGvrpPortStatsTotalPDUTransmitted_Type())
alaGvrpPortStatsTotalPDUTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsTotalPDUTransmitted.setStatus(_A)
_AlaGvrpPortStatsTotalMsgsReceived_Type=Counter32
_AlaGvrpPortStatsTotalMsgsReceived_Object=MibTableColumn
alaGvrpPortStatsTotalMsgsReceived=_AlaGvrpPortStatsTotalMsgsReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,16),_AlaGvrpPortStatsTotalMsgsReceived_Type())
alaGvrpPortStatsTotalMsgsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsTotalMsgsReceived.setStatus(_A)
_AlaGvrpPortStatsTotalMsgsTransmitted_Type=Counter32
_AlaGvrpPortStatsTotalMsgsTransmitted_Object=MibTableColumn
alaGvrpPortStatsTotalMsgsTransmitted=_AlaGvrpPortStatsTotalMsgsTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,17),_AlaGvrpPortStatsTotalMsgsTransmitted_Type())
alaGvrpPortStatsTotalMsgsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsTotalMsgsTransmitted.setStatus(_A)
_AlaGvrpPortStatsInvalidMsgsReceived_Type=Counter32
_AlaGvrpPortStatsInvalidMsgsReceived_Object=MibTableColumn
alaGvrpPortStatsInvalidMsgsReceived=_AlaGvrpPortStatsInvalidMsgsReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,18),_AlaGvrpPortStatsInvalidMsgsReceived_Type())
alaGvrpPortStatsInvalidMsgsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGvrpPortStatsInvalidMsgsReceived.setStatus(_A)
class _AlaGvrpPortStatsClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('reset',1)))
_AlaGvrpPortStatsClearStats_Type.__name__=_E
_AlaGvrpPortStatsClearStats_Object=MibTableColumn
alaGvrpPortStatsClearStats=_AlaGvrpPortStatsClearStats_Object((1,3,6,1,4,1,6486,801,1,2,1,36,1,1,5,1,1,19),_AlaGvrpPortStatsClearStats_Type())
alaGvrpPortStatsClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGvrpPortStatsClearStats.setStatus(_A)
_AlcatelIND1GVRPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1GVRPMIBConformance=_AlcatelIND1GVRPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1,2))
if mibBuilder.loadTexts:alcatelIND1GVRPMIBConformance.setStatus(_A)
_AlcatelIND1GVRPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1GVRPMIBGroups=_AlcatelIND1GVRPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1,2,1))
if mibBuilder.loadTexts:alcatelIND1GVRPMIBGroups.setStatus(_A)
_AlcatelIND1GVRPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1GVRPMIBCompliances=_AlcatelIND1GVRPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36,1,2,2))
if mibBuilder.loadTexts:alcatelIND1GVRPMIBCompliances.setStatus(_A)
gvrpPortBaseGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,36,1,2,1,1))
gvrpPortBaseGroup.setObjects(*((_B,_M),(_B,_N),(_B,_H)))
if mibBuilder.loadTexts:gvrpPortBaseGroup.setStatus(_A)
gvrpPortConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,36,1,2,1,2))
gvrpPortConfigGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:gvrpPortConfigGroup.setStatus(_A)
gvrpPortStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,36,1,2,1,3))
gvrpPortStatsGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:gvrpPortStatsGroup.setStatus(_A)
gvrpVlanLimitReachedEvent=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,36,1,0,1))
gvrpVlanLimitReachedEvent.setObjects((_B,_H))
if mibBuilder.loadTexts:gvrpVlanLimitReachedEvent.setStatus(_A)
gvrpNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,36,1,2,1,4))
gvrpNotificationGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:gvrpNotificationGroup.setStatus(_A)
alcatelIND1GVRPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,36,1,2,2,1))
alcatelIND1GVRPMIBCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:alcatelIND1GVRPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1GVRPMIB':alcatelIND1GVRPMIB,'alcatelIND1GVRPMIBNotifications':alcatelIND1GVRPMIBNotifications,_v:gvrpVlanLimitReachedEvent,'alcatelIND1GVRPMIBObjects':alcatelIND1GVRPMIBObjects,_M:alaGvrpGlobalClearStats,_N:alaGvrpTransparentSwitching,_H:alaGvrpMaxVlanLimit,'gvrpPortConfig':gvrpPortConfig,'alaGvrpPortConfigTable':alaGvrpPortConfigTable,'alaGvrpPortConfigEntry':alaGvrpPortConfigEntry,_J:alaGvrpPortConfigIfIndex,_O:alaGvrpPortConfigRegistrarMode,_P:alaGvrpPortConfigApplicantMode,_Q:alaGvrpPortConfigRestrictedRegistrationBitmap,_R:alaGvrpPortConfigAllowRegistrationBitmap,_S:alaGvrpPortConfigRegistrationBitmap,_T:alaGvrpPortConfigRestrictedApplicantBitmap,_U:alaGvrpPortConfigAllowApplicantBitmap,_V:alaGvrpPortConfigApplicantBitmap,_W:alaGvrpPortConfigRegistrationToStaticVlanLearn,_X:alaGvrpPortConfigRegistrationToStaticVlanRestrict,_Y:alaGvrpPortConfigRegistrationToStaticVlan,_Z:alaGvrpPortConfigJoinTimer,_a:alaGvrpPortConfigLeaveTimer,_b:alaGvrpPortConfigLeaveAllTimer,_c:alaGvrpPortConfigProviderBpduMac,'gvrpPortStats':gvrpPortStats,'alaGvrpPortStatsTable':alaGvrpPortStatsTable,'alaGvrpPortStatsEntry':alaGvrpPortStatsEntry,_L:alaGvrpPortStatsIfIndex,_d:alaGvrpPortStatsJoinEmptyReceived,_e:alaGvrpPortStatsJoinInReceived,_f:alaGvrpPortStatsEmptyReceived,_g:alaGvrpPortStatsLeaveInReceived,_h:alaGvrpPortStatsLeaveEmptyReceived,_i:alaGvrpPortStatsLeaveAllReceived,_j:alaGvrpPortStatsJoinEmptyTransmitted,_k:alaGvrpPortStatsJoinInTransmitted,_l:alaGvrpPortStatsEmptyTransmitted,_m:alaGvrpPortStatsLeaveInTransmitted,_n:alaGvrpPortStatsLeaveEmptyTransmitted,_o:alaGvrpPortStatsLeaveAllTransmitted,_p:alaGvrpPortStatsTotalPDUReceived,_q:alaGvrpPortStatsTotalPDUTransmitted,_r:alaGvrpPortStatsTotalMsgsReceived,_s:alaGvrpPortStatsTotalMsgsTransmitted,_t:alaGvrpPortStatsInvalidMsgsReceived,_u:alaGvrpPortStatsClearStats,'alcatelIND1GVRPMIBConformance':alcatelIND1GVRPMIBConformance,'alcatelIND1GVRPMIBGroups':alcatelIND1GVRPMIBGroups,_w:gvrpPortBaseGroup,_x:gvrpPortConfigGroup,_y:gvrpPortStatsGroup,_z:gvrpNotificationGroup,'alcatelIND1GVRPMIBCompliances':alcatelIND1GVRPMIBCompliances,'alcatelIND1GVRPMIBCompliance':alcatelIND1GVRPMIBCompliance})