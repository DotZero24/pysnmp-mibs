_W='etsysEncrDot1xAuthConfigGroup'
_V='etsysEncrDot1xAuthStationReauthenticate'
_U='etsysEncrDot1xAuthStationInitialize'
_T='etsysEncrDot1xAuthReauthenticate'
_S='etsysEncrDot1xAuthInitialize'
_R='etsysEncrDot1xAuthKeyTxEnabled'
_Q='etsysEncrDot1xAuthReAuthEnabled'
_P='etsysEncrDot1xAuthReAuthPeriod'
_O='etsysEncrDot1xAuthMaxReq'
_N='etsysEncrDot1xAuthServerTimeout'
_M='etsysEncrDot1xAuthSuppTimeout'
_L='etsysEncrDot1xAuthTxPeriod'
_K='etsysEncrDot1xAuthQuietPeriod'
_J='etsysEncrDot1xAuthControlledPortControl'
_I='etsysEncrDot1xAuthAdminControlledDirections'
_H='etsysDot1xAuthStationAddress'
_G='ENTERASYS-8021X-EXTENSIONS-MIB'
_F='dot1xPaePortNumber'
_E='IEEE8021-PAE-MIB'
_D='read-write'
_C='OctetString'
_B='ENTERASYS-ENCR-8021X-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysDot1xAuthStationAddress,=mibBuilder.importSymbols(_G,_H)
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
dot1xPaePortNumber,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysEncr8021xConfigMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,19))
if mibBuilder.loadTexts:etsysEncr8021xConfigMIB.setRevisions(('2002-03-14 20:45',))
_EtsysEncrDot1xConfigObjects_ObjectIdentity=ObjectIdentity
etsysEncrDot1xConfigObjects=_EtsysEncrDot1xConfigObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,19,1))
_EtsysEncrDot1xAuthConfigBranch_ObjectIdentity=ObjectIdentity
etsysEncrDot1xAuthConfigBranch=_EtsysEncrDot1xAuthConfigBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,19,1,1))
_EtsysEncrDot1xAuthPortConfigTable_Object=MibTable
etsysEncrDot1xAuthPortConfigTable=_EtsysEncrDot1xAuthPortConfigTable_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1))
if mibBuilder.loadTexts:etsysEncrDot1xAuthPortConfigTable.setStatus(_A)
_EtsysEncrDot1xAuthPortConfigEntry_Object=MibTableRow
etsysEncrDot1xAuthPortConfigEntry=_EtsysEncrDot1xAuthPortConfigEntry_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1))
etsysEncrDot1xAuthPortConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysEncrDot1xAuthPortConfigEntry.setStatus(_A)
class _EtsysEncrDot1xAuthAdminControlledDirections_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthAdminControlledDirections_Type.__name__=_C
_EtsysEncrDot1xAuthAdminControlledDirections_Object=MibTableColumn
etsysEncrDot1xAuthAdminControlledDirections=_EtsysEncrDot1xAuthAdminControlledDirections_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,1),_EtsysEncrDot1xAuthAdminControlledDirections_Type())
etsysEncrDot1xAuthAdminControlledDirections.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthAdminControlledDirections.setStatus(_A)
class _EtsysEncrDot1xAuthControlledPortControl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthControlledPortControl_Type.__name__=_C
_EtsysEncrDot1xAuthControlledPortControl_Object=MibTableColumn
etsysEncrDot1xAuthControlledPortControl=_EtsysEncrDot1xAuthControlledPortControl_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,2),_EtsysEncrDot1xAuthControlledPortControl_Type())
etsysEncrDot1xAuthControlledPortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthControlledPortControl.setStatus(_A)
class _EtsysEncrDot1xAuthQuietPeriod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthQuietPeriod_Type.__name__=_C
_EtsysEncrDot1xAuthQuietPeriod_Object=MibTableColumn
etsysEncrDot1xAuthQuietPeriod=_EtsysEncrDot1xAuthQuietPeriod_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,3),_EtsysEncrDot1xAuthQuietPeriod_Type())
etsysEncrDot1xAuthQuietPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthQuietPeriod.setStatus(_A)
class _EtsysEncrDot1xAuthTxPeriod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthTxPeriod_Type.__name__=_C
_EtsysEncrDot1xAuthTxPeriod_Object=MibTableColumn
etsysEncrDot1xAuthTxPeriod=_EtsysEncrDot1xAuthTxPeriod_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,4),_EtsysEncrDot1xAuthTxPeriod_Type())
etsysEncrDot1xAuthTxPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthTxPeriod.setStatus(_A)
class _EtsysEncrDot1xAuthSuppTimeout_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthSuppTimeout_Type.__name__=_C
_EtsysEncrDot1xAuthSuppTimeout_Object=MibTableColumn
etsysEncrDot1xAuthSuppTimeout=_EtsysEncrDot1xAuthSuppTimeout_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,5),_EtsysEncrDot1xAuthSuppTimeout_Type())
etsysEncrDot1xAuthSuppTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthSuppTimeout.setStatus(_A)
class _EtsysEncrDot1xAuthServerTimeout_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthServerTimeout_Type.__name__=_C
_EtsysEncrDot1xAuthServerTimeout_Object=MibTableColumn
etsysEncrDot1xAuthServerTimeout=_EtsysEncrDot1xAuthServerTimeout_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,6),_EtsysEncrDot1xAuthServerTimeout_Type())
etsysEncrDot1xAuthServerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthServerTimeout.setStatus(_A)
class _EtsysEncrDot1xAuthMaxReq_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthMaxReq_Type.__name__=_C
_EtsysEncrDot1xAuthMaxReq_Object=MibTableColumn
etsysEncrDot1xAuthMaxReq=_EtsysEncrDot1xAuthMaxReq_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,7),_EtsysEncrDot1xAuthMaxReq_Type())
etsysEncrDot1xAuthMaxReq.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthMaxReq.setStatus(_A)
class _EtsysEncrDot1xAuthReAuthPeriod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthReAuthPeriod_Type.__name__=_C
_EtsysEncrDot1xAuthReAuthPeriod_Object=MibTableColumn
etsysEncrDot1xAuthReAuthPeriod=_EtsysEncrDot1xAuthReAuthPeriod_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,8),_EtsysEncrDot1xAuthReAuthPeriod_Type())
etsysEncrDot1xAuthReAuthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthReAuthPeriod.setStatus(_A)
class _EtsysEncrDot1xAuthReAuthEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthReAuthEnabled_Type.__name__=_C
_EtsysEncrDot1xAuthReAuthEnabled_Object=MibTableColumn
etsysEncrDot1xAuthReAuthEnabled=_EtsysEncrDot1xAuthReAuthEnabled_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,9),_EtsysEncrDot1xAuthReAuthEnabled_Type())
etsysEncrDot1xAuthReAuthEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthReAuthEnabled.setStatus(_A)
class _EtsysEncrDot1xAuthKeyTxEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthKeyTxEnabled_Type.__name__=_C
_EtsysEncrDot1xAuthKeyTxEnabled_Object=MibTableColumn
etsysEncrDot1xAuthKeyTxEnabled=_EtsysEncrDot1xAuthKeyTxEnabled_Object((1,3,6,1,4,1,5624,1,2,19,1,1,1,1,10),_EtsysEncrDot1xAuthKeyTxEnabled_Type())
etsysEncrDot1xAuthKeyTxEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthKeyTxEnabled.setStatus(_A)
_EtsysEncrDot1xAuthPortInitTable_Object=MibTable
etsysEncrDot1xAuthPortInitTable=_EtsysEncrDot1xAuthPortInitTable_Object((1,3,6,1,4,1,5624,1,2,19,1,1,2))
if mibBuilder.loadTexts:etsysEncrDot1xAuthPortInitTable.setStatus(_A)
_EtsysEncrDot1xAuthPortInitEntry_Object=MibTableRow
etsysEncrDot1xAuthPortInitEntry=_EtsysEncrDot1xAuthPortInitEntry_Object((1,3,6,1,4,1,5624,1,2,19,1,1,2,1))
etsysEncrDot1xAuthPortInitEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysEncrDot1xAuthPortInitEntry.setStatus(_A)
class _EtsysEncrDot1xAuthInitialize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthInitialize_Type.__name__=_C
_EtsysEncrDot1xAuthInitialize_Object=MibTableColumn
etsysEncrDot1xAuthInitialize=_EtsysEncrDot1xAuthInitialize_Object((1,3,6,1,4,1,5624,1,2,19,1,1,2,1,1),_EtsysEncrDot1xAuthInitialize_Type())
etsysEncrDot1xAuthInitialize.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthInitialize.setStatus(_A)
class _EtsysEncrDot1xAuthReauthenticate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthReauthenticate_Type.__name__=_C
_EtsysEncrDot1xAuthReauthenticate_Object=MibTableColumn
etsysEncrDot1xAuthReauthenticate=_EtsysEncrDot1xAuthReauthenticate_Object((1,3,6,1,4,1,5624,1,2,19,1,1,2,1,2),_EtsysEncrDot1xAuthReauthenticate_Type())
etsysEncrDot1xAuthReauthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthReauthenticate.setStatus(_A)
_EtsysEncrDot1xAuthStationInitTable_Object=MibTable
etsysEncrDot1xAuthStationInitTable=_EtsysEncrDot1xAuthStationInitTable_Object((1,3,6,1,4,1,5624,1,2,19,1,1,3))
if mibBuilder.loadTexts:etsysEncrDot1xAuthStationInitTable.setStatus(_A)
_EtsysEncrDot1xAuthStationInitEntry_Object=MibTableRow
etsysEncrDot1xAuthStationInitEntry=_EtsysEncrDot1xAuthStationInitEntry_Object((1,3,6,1,4,1,5624,1,2,19,1,1,3,1))
etsysEncrDot1xAuthStationInitEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysEncrDot1xAuthStationInitEntry.setStatus(_A)
class _EtsysEncrDot1xAuthStationInitialize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthStationInitialize_Type.__name__=_C
_EtsysEncrDot1xAuthStationInitialize_Object=MibTableColumn
etsysEncrDot1xAuthStationInitialize=_EtsysEncrDot1xAuthStationInitialize_Object((1,3,6,1,4,1,5624,1,2,19,1,1,3,1,1),_EtsysEncrDot1xAuthStationInitialize_Type())
etsysEncrDot1xAuthStationInitialize.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthStationInitialize.setStatus(_A)
class _EtsysEncrDot1xAuthStationReauthenticate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xAuthStationReauthenticate_Type.__name__=_C
_EtsysEncrDot1xAuthStationReauthenticate_Object=MibTableColumn
etsysEncrDot1xAuthStationReauthenticate=_EtsysEncrDot1xAuthStationReauthenticate_Object((1,3,6,1,4,1,5624,1,2,19,1,1,3,1,2),_EtsysEncrDot1xAuthStationReauthenticate_Type())
etsysEncrDot1xAuthStationReauthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xAuthStationReauthenticate.setStatus(_A)
_EtsysEncrDot1xConfigConformance_ObjectIdentity=ObjectIdentity
etsysEncrDot1xConfigConformance=_EtsysEncrDot1xConfigConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,19,2))
_EtsysEncrDot1xConfigGroups_ObjectIdentity=ObjectIdentity
etsysEncrDot1xConfigGroups=_EtsysEncrDot1xConfigGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,19,2,1))
_EtsysEncrDot1xConfigCompliances_ObjectIdentity=ObjectIdentity
etsysEncrDot1xConfigCompliances=_EtsysEncrDot1xConfigCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,19,2,2))
etsysEncrDot1xAuthConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,19,2,1,1))
etsysEncrDot1xAuthConfigGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:etsysEncrDot1xAuthConfigGroup.setStatus(_A)
etsysEncrDot1xAuthInitGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,19,2,1,2))
etsysEncrDot1xAuthInitGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:etsysEncrDot1xAuthInitGroup.setStatus(_A)
etsysEncrDot1xConfigCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,19,2,2,1))
etsysEncrDot1xConfigCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:etsysEncrDot1xConfigCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysEncr8021xConfigMIB':etsysEncr8021xConfigMIB,'etsysEncrDot1xConfigObjects':etsysEncrDot1xConfigObjects,'etsysEncrDot1xAuthConfigBranch':etsysEncrDot1xAuthConfigBranch,'etsysEncrDot1xAuthPortConfigTable':etsysEncrDot1xAuthPortConfigTable,'etsysEncrDot1xAuthPortConfigEntry':etsysEncrDot1xAuthPortConfigEntry,_I:etsysEncrDot1xAuthAdminControlledDirections,_J:etsysEncrDot1xAuthControlledPortControl,_K:etsysEncrDot1xAuthQuietPeriod,_L:etsysEncrDot1xAuthTxPeriod,_M:etsysEncrDot1xAuthSuppTimeout,_N:etsysEncrDot1xAuthServerTimeout,_O:etsysEncrDot1xAuthMaxReq,_P:etsysEncrDot1xAuthReAuthPeriod,_Q:etsysEncrDot1xAuthReAuthEnabled,_R:etsysEncrDot1xAuthKeyTxEnabled,'etsysEncrDot1xAuthPortInitTable':etsysEncrDot1xAuthPortInitTable,'etsysEncrDot1xAuthPortInitEntry':etsysEncrDot1xAuthPortInitEntry,_S:etsysEncrDot1xAuthInitialize,_T:etsysEncrDot1xAuthReauthenticate,'etsysEncrDot1xAuthStationInitTable':etsysEncrDot1xAuthStationInitTable,'etsysEncrDot1xAuthStationInitEntry':etsysEncrDot1xAuthStationInitEntry,_U:etsysEncrDot1xAuthStationInitialize,_V:etsysEncrDot1xAuthStationReauthenticate,'etsysEncrDot1xConfigConformance':etsysEncrDot1xConfigConformance,'etsysEncrDot1xConfigGroups':etsysEncrDot1xConfigGroups,_W:etsysEncrDot1xAuthConfigGroup,'etsysEncrDot1xAuthInitGroup':etsysEncrDot1xAuthInitGroup,'etsysEncrDot1xConfigCompliances':etsysEncrDot1xConfigCompliances,'etsysEncrDot1xConfigCompliance':etsysEncrDot1xConfigCompliance})